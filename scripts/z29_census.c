// z29_census.c — O259: segmented census of the b = 1 line of ES Type II at primes p ≡ 1 (mod 4).
// Mutual-shift form (B1_LINE.md Lemma 1.1): b = 1 at p  <=>  ∃ s, t ≥ 1: s t | p + s + t and 4 | s·t
// (then exactly one of s, t is ≡ 0 mod 4).  WLOG s = min(s,t) <= 1 + sqrt(p+1) (complete).
// With t | p + s, p + s = t u, the condition is s | u + 1.
// Algorithm (independent of O258's s8_lines.c window code): for s = 1, 2, ... factor p + s (segmented sieve table),
// test all divisors t >= s. First hit -> done. If no hit for s <= S, an exact fallback scans all s <= 1 + sqrt(p+1).
// env Z29_LINE=2: census of the c = 1 line (★) instead of b = 1.
// usage: z29_census LO HI [S [HARD]]   (prints records of the least hitting s, failures, totals; primes with least s >= HARD)
//        z29_census count LO HI   (prints, per prime, N1(p) = number of solutions; for heuristics; small ranges)
//        z29_census countlist MAXP < primes   [SIG] (prints p N1(p) Nc1(p) N1_{s>SIG}(p); Nc1 = number of (★) = c=1 line pairs)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
typedef long long ll; typedef unsigned long long ull;
#define MAXF 16
static uint32_t *sp; static int nsp;
static void small_primes(ll B){ char *c=calloc(B+1,1); sp=malloc(sizeof(uint32_t)*(B/2+10)); nsp=0;
  for(ll i=2;i<=B;i++){ if(c[i]) continue; sp[nsp++]=i; for(ll j=i*i;j<=B;j+=i) c[j]=1; } free(c); }
typedef struct { uint32_t q[MAXF]; uint8_t k; } fent;
// fill table T[0..len) with the primes <= sqrt(lo+len) dividing lo+i
static void factor_range(ll lo, ll len, fent *T){
  for(ll i=0;i<len;i++) T[i].k=0;
  ll hi=lo+len; for(int j=0;j<nsp;j++){ ll q=sp[j]; if(q*q>hi) break; ll st=((lo+q-1)/q)*q;
    for(ll x=st;x<hi;x+=q){ fent *e=&T[x-lo]; if(e->k<MAXF) e->q[e->k++]=(uint32_t)q; else { fprintf(stderr,"MAXF overflow\n"); exit(1);} } } }
static ll pr[MAXF+1]; static int ex[MAXF+1]; static ll dv[1<<16];
static int expand(ll n, const fent *e){ int k=0; ll r=n; for(int i=0;i<e->k;i++){ ll q=e->q[i]; pr[k]=q; ex[k]=0; while(r%q==0){ r/=q; ex[k]++; } k++; }
  if(r>1){ pr[k]=r; ex[k]=1; k++; } return k; }
static int gendiv(int k){ int nd=1; dv[0]=1; for(int i=0;i<k;i++){ int cur=nd; ll pp=1; for(int e=1;e<=ex[i];e++){ pp*=pr[i]; for(int j=0;j<cur;j++) dv[nd++]=dv[j]*pp; } } return nd; }
// number of hits (t >= s) at shift s for prime p, given the factorisation entry of p+s; stop at first if one>0
static int LINE=1; // 1 = b=1 line, 2 = c=1 line (★): pairs with u == -1 mod 4s
static int hits(ll p, ll s, const fent *e, int one){ if(LINE==2){ ll n=p+s; int k=expand(n,e); int nd=gendiv(k); int h=0;
    for(int i=0;i<nd;i++){ ll t=dv[i]; if(t<=s) continue; if(((n/t)+1)%(4*s)==0){ h++; if(one) return h; } } return h; }
  if(!((s&3)==0 || (s&3)==3)) return 0; ll n=p+s; int k=expand(n,e); int nd=gendiv(k); int h=0;
  for(int i=0;i<nd;i++){ ll t=dv[i]; if(t<s) continue; if(t==s) continue; ll u=n/t; if((u+1)%s) continue; if(!((s&3)==0 || (t&3)==0)) continue; h++; if(one) return h; }
  return h; }
static fent *T2; static ll c1cnt, bigcnt, SIG=64;
// c = 1 line hits at shift s ((★): N = (u+1)/s == 0 mod 4, i.e. u == -1 mod 4s), t > s
static int hitsc1(ll p, ll s, const fent *e){ ll n=p+s; int k=expand(n,e); int nd=gendiv(k); int h=0;
  for(int i=0;i<nd;i++){ ll t=dv[i]; if(t<=s) continue; ll u=n/t; if((u+1)%(4*s)==0) h++; } return h; }
// exact: least s with a hit (0 if none), or full count if cnt!=NULL (then also c=1 count in c1cnt). Chunked tables.
static ll exact(ll p, ll s0, ll *cnt){ ll smax=1+(ll)sqrtl((long double)p+1)+1; ll first=0; const ll CH=1<<18;
  T2=realloc(T2,sizeof(fent)*CH); if(cnt){ c1cnt=0; bigcnt=0; }
  for(ll a=s0;a<=smax;a+=CH){ ll len=CH; if(a+len>smax+1) len=smax+1-a; factor_range(p+a,len,T2);
    for(ll s=a;s<a+len;s++){ int h=hits(p,s,&T2[s-a],cnt==NULL); if(cnt) c1cnt+=hitsc1(p,s,&T2[s-a]);
      if(h){ if(!first) first=s; if(!cnt) return first; *cnt+=h; if(s>SIG) bigcnt+=h; } } }
  return first; }
int main(int argc,char**argv){
  if(argc>1 && !strcmp(argv[1],"count")){ ll LO=atoll(argv[2]), HI=atoll(argv[3]); small_primes((ll)sqrtl((long double)HI*1.01)+1000);
    for(ll p=LO+((5-LO%4+4)%4);p<=HI;p+=4){ int isp=1; for(int j=0;j<nsp && (ll)sp[j]*sp[j]<=p;j++) if(p%sp[j]==0){isp=0;break;} if(!isp||p<5) continue;
      ll c=0; exact(p,1,&c); printf("%lld %lld\n",p,c); }
    return 0; }
  if(argc>1 && !strcmp(argv[1],"countlist")){ ll MX=atoll(argv[2]); if(argc>3) SIG=atoll(argv[3]); small_primes((ll)sqrtl((long double)MX*1.01)+1000); ll p;
    while(scanf("%lld",&p)==1){ ll c=0; exact(p,1,&c); printf("%lld %lld %lld %lld\n",p,c,c1cnt,bigcnt); fflush(stdout); } return 0; }
  if(getenv("Z29_LINE")) LINE=atoi(getenv("Z29_LINE"));
  ll LO=atoll(argv[1]), HI=atoll(argv[2]); ll S=argc>3?atoll(argv[3]):512; ll HARD=argc>4?atoll(argv[4]):0; ll L=1<<20;
  small_primes((ll)sqrtl((long double)HI+S+L)+1000);
  fent *T=malloc(sizeof(fent)*(L+S+1)); ll np=0, nfb=0, nfail=0, rec=0; ll hist[16]={0};
  for(ll base=LO; base<=HI; base+=L){ ll len=L; if(base+len>HI+1) len=HI+1-base; factor_range(base,len+S+1,T);
    for(ll i=0;i<len;i++){ ll p=base+i; if((p&3)!=1 || p<5) continue; if(T[i].k && !(T[i].k==1 && T[i].q[0]==p)) continue; // composite
      np++; ll first=0;
      for(ll s=1;s<=S;s++){ if(hits(p,s,&T[i+s],1)){ first=s; break; } }
      if(!first){ nfb++; first=exact(p,S+1,NULL); }
      if(!first){ nfail++; printf("FAIL p=%lld\n",p); fflush(stdout); continue; }
      int b=0; while((1LL<<(b+1))<=first && b<15) b++; hist[b]++;
      if(HARD && first>=HARD){ printf("HARD %lld %lld\n",p,first); }
      if(first>rec){ rec=first; printf("record least s=%lld at p=%lld\n",first,p); fflush(stdout);} } }
  printf("range [%lld,%lld] S=%lld: primes p=1(4): %lld, fallback: %lld, failures: %lld, max least s: %lld\n",LO,HI,S,np,nfb,nfail,rec);
  printf("hist log2(least s):"); for(int b=0;b<16;b++) printf(" %lld",hist[b]); printf("\n");
  return 0; }
