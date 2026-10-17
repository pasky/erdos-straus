// review_r270_engine.c — R270 from-scratch b = 1 line engine (different algorithm from z29_census.c).
// b = 1 at prime p == 1 (4)  <=>  exists s,t >= 1 with s*t | p+s+t and 4 | s*t   (Lemma 1.1, re-derived in review).
// Phase A (sieve): for every pair s < t with s*t <= L and 4 | s*t, mark all p == -(s+t) (mod s*t) in the segment as solved.
// Phase B (exact fallback, no factor tables): for each s <= 1+sqrt(p+1), enumerate t == -p (mod s) with t <= sqrt(p+s)
//   and u == -1 (mod s) with u <= sqrt(p+s) (t = (p+s)/u); test s*t | p+s+t, 4 | s*t directly.
// env R270_LINE=2: the c = 1 line (★) instead: exists s,t >= 1 with 4*s*t | p+s+t (min <= (1+sqrt(4p+1))/4).
// usage: engine LO HI L        -> census of primes p == 1 (4) in [LO,HI]: count, #fallback, failures
//        engine least < list   -> least s for each p (Phase B only, ascending s), prints "p s t"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
typedef long long ll; typedef unsigned long long ull;
static ll isqrt_(ll n){ ll r=(ll)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++; return r; }
static int LINE=1;
static int test(ll p, ll s, ll t){ if(s<1||t<1) return 0; ull st=(ull)s*(ull)t; if(LINE==2) return ((ull)(p+s+t))%(4*st)==0; if(st%4) return 0; return ((ull)(p+s+t))%st==0; }
// least s with a pair (min coordinate s, any partner); returns s and sets *T; 0 if none
static ll least(ll p, ll *T){ ll B=1+isqrt_(p+1); if(LINE==2) B=(1+isqrt_(4*p+1))/4+1;
  for(ll s=1;s<=B;s++){ ll n=p+s, r=isqrt_(n);
    ll t0=((-p)%s+s)%s; if(t0==0) t0=s;
    for(ll t=t0;t<=r;t+=s) if(n%t==0 && test(p,s,t)){ *T=t; return s; }
    for(ll u=s-1;u<=r;u+=s){ if(u<1) continue; if(n%u==0){ ll t=n/u; if(test(p,s,t)){ *T=t; return s; } } } }
  return 0; }
// all pairs {s<t} (count), Phase B style but without early exit; u-branch skips t <= sqrt to avoid double count
static ll countall(ll p){ ll B=(LINE==2)?(1+isqrt_(4*p+1))/4+1:1+isqrt_(p+1); ll c=0;
  for(ll s=1;s<=B;s++){ ll n=p+s, r=isqrt_(n);
    ll t0=((-p)%s+s)%s; if(t0==0) t0=s;
    for(ll t=t0;t<=r;t+=s) if(t>s && n%t==0 && test(p,s,t)) c++;
    for(ll u=s-1;u<=r;u+=s){ if(u<1) continue; if(n%u==0){ ll t=n/u; if(t>r && t>s && test(p,s,t)) c++; } } }
  return c; }
int main(int argc,char**argv){
  if(getenv("R270_LINE")) LINE=atoi(getenv("R270_LINE"));
  if(argc>1 && !strcmp(argv[1],"count")){ ll p; while(scanf("%lld",&p)==1){ printf("%lld %lld\n",p,countall(p)); fflush(stdout);} return 0; }
  if(argc>1 && !strcmp(argv[1],"least")){ ll p; while(scanf("%lld",&p)==1){ ll t=0; ll s=least(p,&t); printf("%lld %lld %lld\n",p,s,t); fflush(stdout);} return 0; }
  ll LO=atoll(argv[1]), HI=atoll(argv[2]), L=atoll(argv[3]);
  // pairs
  ll np_=0, cap=1<<20; ll *PM=malloc(sizeof(ll)*cap), *PR=malloc(sizeof(ll)*cap);
  for(ll s=1;s*s<=L;s++) for(ll t=s;s*t<=L;t++){ ll m=s*t; if(LINE==2) m*=4; else if(m%4) continue; ll r=((-(s+t))%m+m)%m; if(r%4!=1) continue; // odd p==1(4) only
      if(np_==cap){ cap*=2; PM=realloc(PM,sizeof(ll)*cap); PR=realloc(PR,sizeof(ll)*cap);} PM[np_]=m; PR[np_]=r; np_++; }
  fprintf(stderr,"pairs (useful) with st<=%lld: %lld\n",L,np_);
  ll SQ=isqrt_(HI)+1; char *cs=calloc(SQ+1,1); ll *sp=malloc(sizeof(ll)*(SQ+1)); ll nsp=0;
  for(ll i=2;i<=SQ;i++){ if(cs[i]) continue; sp[nsp++]=i; for(ll j=i*i;j<=SQ;j+=i) cs[j]=1; }
  const ll SEG=1LL<<26; char *comp=malloc(SEG), *solved=malloc(SEG);
  ll nprime=0, nfb=0, nfail=0, n3=0;
  for(ll base=LO; base<=HI; base+=SEG){ ll len=SEG; if(base+len>HI+1) len=HI+1-base;
    memset(comp,0,len); memset(solved,0,len);
    for(ll j=0;j<nsp;j++){ ll q=sp[j]; if(q*q>base+len-1) break; ll st=((base+q-1)/q)*q; if(st<q*q) st=q*q; for(ll x=st;x<base+len;x+=q) comp[x-base]=1; }
    for(ll k=0;k<np_;k++){ ll m=PM[k], r=PR[k]; ll st=base+(((r-base)%m)+m)%m; for(ll x=st;x<base+len;x+=m) solved[x-base]=1; }
    for(ll i=0;i<len;i++){ ll p=base+i; if(p>=3 && (p&3)==3 && !comp[i]) n3++; if(p<5 || (p&3)!=1 || comp[i]) continue; nprime++;
      if(solved[i]) continue; nfb++; ll t; ll s=least(p,&t);
      if(!s){ nfail++; printf("FAIL %lld\n",p); fflush(stdout); }
      else if(s*t>L && s>=64) { printf("LATE %lld s=%lld t=%lld\n",p,s,t); } } }
  printf("range [%lld,%lld] L=%lld primes==1(4): %lld fallback: %lld failures: %lld primes==3(4): %lld\n",LO,HI,L,nprime,nfb,nfail,n3);
  return 0; }
