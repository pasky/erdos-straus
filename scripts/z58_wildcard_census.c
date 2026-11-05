// z58 WILDCARD: converse-of-T1 census for the full Type II family of numerator K (K = 4 or 8, any K ≡ 0 mod 4).
//   N_II^K(n) := #{(a,b,c,d) in N^4 : K abcd = a + b + n c}.
// Target-set form (Z57_BFII Lemma 1.1(d), same proof for any K): N_II^K(n) >= 1 iff some f ≡ -1 (mod K) has
//   -n mod f  in  T_f = { a c^{-1} mod f : a c | (f+1)/K }     [then d = (f+1)/(K a c), b = (c n + a)/f >= 1].
// For every odd n in [lo,hi) we find the least witness f <= FMAX (bitmap lookup).  n with no witness <= FMAX are
// split into odd squares (zero by T1, PROVED; printed as SQ only if requested) and "UNRES" non-squares, which are then
// decided EXACTLY by the (a,b) loop:  K a b d = n + e, e | a+b  (e = (a+b)/c), at most one e per (a,b) since K ab > a+b.
// Output: summary + one line per non-square n with no witness <= FMAX ("ZERO n" or "LATE n f a b c d").
// Usage: census K lo hi FMAX [primes_only(0/1)] [mod4 filter: 0=all odd,1,3] [coprime(0/1)]
// coprime=1: count only solutions with gcd(a b d, n) = 1 (Elsholtz-Tao Type II proper; automatic at primes).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
static long K;
static uint8_t **bm; // bm[f] bitmap of size f (only f ≡ -1 mod K)
static int COP; static int DODD; // env Z58DODD=1: only solutions with d odd (complement of the numerator-2K family)
static u64 DUMP; // env Z58DUMP=k: print "W n f" for n divisible by k (k=1: all)
static long gcdl(long a,long b){while(b){long t=a%b;a=b;b=t;}return a;}
static long inv(long c,long f){ long t=0,nt=1,r=f,nr=c%f; while(nr){long q=r/nr,tmp=t-q*nt;t=nt;nt=tmp;tmp=r-q*nr;r=nr;nr=tmp;} if(r!=1) return -1; if(t<0)t+=f; return t;}
static int issq(u64 n){u64 r=(u64)sqrtl((long double)n); while(r*r>n)r--; while((r+1)*(r+1)<=n)r++; return r*r==n;}
// exact decision: returns 1 and fills witness if N_II^K(n) >= 1
static int exact(u64 n,long*oa,long*ob,long*oc,long*od){
  for(u64 a=1;;a++){ if(K*a*a > n + 2*a) break; // a <= b: K a b >= K a^2, n + e <= n + 2b ... use b-loop bound below
    for(u64 b=a;;b++){ u64 q=K*a*b; if(q > n + a + b) break; u64 r=(q - n%q)%q; if(r==0||r>a+b) continue; if((a+b)%r) continue;
      if(DODD && (((n+r)/q)&1)==0) continue;
      if(COP){ u64 dd=(n+r)/q; if(gcdl((long)((u64)a*b%n),(long)n)!=1 || gcdl((long)(dd%n),(long)n)!=1) continue; }
      *oa=a;*ob=b;*oc=(a+b)/r;*od=(n+r)/q; return 1; }
    }
  return 0;}
int main(int argc,char**argv){
  K=atol(argv[1]); u64 lo=strtoull(argv[2],0,10),hi=strtoull(argv[3],0,10); long FMAX=atol(argv[4]);
  int primes_only=argc>5?atoi(argv[5]):0; int m4=argc>6?atoi(argv[6]):0; COP=argc>7?atoi(argv[7]):0; DODD=getenv("Z58DODD")?atoi(getenv("Z58DODD")):0; DUMP=getenv("Z58DUMP")?strtoull(getenv("Z58DUMP"),0,10):0;
  bm=calloc(FMAX+1,sizeof(uint8_t*));
  for(long f=K-1;f<=FMAX;f+=K){ long m=(f+1)/K; bm[f]=calloc(f/8+1,1);
    for(long c=1;c<=m;c++){ if(m%c) continue; long ci=inv(c,f); if(ci<0) continue; long mc=m/c;
      for(long a=1;a<=mc;a++){ if(mc%a) continue; if(DODD && ((mc/a)&1)==0) continue; long t=(long)((u64)a*ci%f); bm[f][t>>3]|=1<<(t&7);} } }
  // sieve for primality flag (segmented)
  u64 sq=(u64)sqrtl((long double)hi)+2; char*small=calloc(sq+1,1); long*pr=malloc(sizeof(long)*(sq+1)); long np=0;
  for(u64 i=2;i<=sq;i++) if(!small[i]){pr[np++]=i; for(u64 j=i*i;j<=sq;j+=i) small[j]=1;}
  u64 SEG=1<<24; char*seg=malloc(SEG);
  long *hist=calloc(FMAX+2,sizeof(long)); long tested=0,nsq=0,nlate=0,nzero=0,nzeroP=0; long maxf=0; u64 argmax=0;
  long maxfP=0; u64 argmaxP=0;
  for(u64 s=lo;s<hi;s+=SEG){u64 e=s+SEG<hi?s+SEG:hi; memset(seg,0,e-s);
    for(long i=0;i<np;i++){u64 q=pr[i]; if(q*q>=e) break; u64 st=((s+q-1)/q)*q; if(st<q*q) st=q*q; for(u64 j=st;j<e;j+=q) seg[j-s]=1;}
    for(u64 n=s;n<e;n++){ if(!(n&1)||n<3) continue; if(m4 && (long)(n&3)!=m4) continue;
      int isp=!seg[n-s]; if(primes_only && !isp) continue; tested++;
      long best=0;
      for(long f=K-1;f<=FMAX;f+=K){ long t=(long)((f - n%f)%f); if(!(bm[f][t>>3]&(1<<(t&7)))) continue;
        if(!COP){best=f;break;}
        long m=(f+1)/K; int ok=0; // enumerate (a,c) with ac|m, a c^{-1} = t, check gcd(a d, n)=1
        for(long c=1;c<=m&&!ok;c++){ if(m%c) continue; long ci=inv(c,f); if(ci<0) continue; long mc=m/c;
          for(long a=1;a<=mc;a++){ if(mc%a) continue; if((long)((u64)a*ci%f)!=t) continue; long d=mc/a; if(DODD && !(d&1)) continue;
            if(gcdl((long)(n%(u64)a),a)==1 && gcdl((long)(n%(u64)d),d)==1){ok=1;break;} } }
        if(ok){best=f;break;} }
      if(best && DUMP && (n%DUMP==0)) printf("W %llu %ld\n",n,best);
      if(best){ hist[best]++; if(best>maxf){maxf=best;argmax=n;} if(isp&&best>maxfP){maxfP=best;argmaxP=n;} continue; }
      if(issq(n)){ nsq++; continue; }
      long a,b,c,d; nlate++;
      if(exact(n,&a,&b,&c,&d)){ long f=K*a*c*d-1; printf("LATE %llu %s f=%ld a=%ld b=%ld c=%ld d=%ld\n",n,isp?"P":"C",f,a,b,c,d); }
      else { nzero++; if(isp) nzeroP++; printf("ZERO %llu %s\n",n,isp?"P":"C"); }
      fflush(stdout);
    }}
  printf("# coprime=%d dodd=%d\n",COP,DODD); printf("# K=%ld range [%llu,%llu) odd%s mod4=%d FMAX=%ld: tested %ld; squares(no witness, T1) %ld; nonsquare without witness<=FMAX %ld; exact zeros %ld (primes %ld)\n",
    K,lo,hi,primes_only?" primes":"",m4,FMAX,tested,nsq,nlate,nzero,nzeroP);
  printf("# max least witness %ld at n=%llu; among primes %ld at p=%llu\n",maxf,argmax,maxfP,argmaxP);
  long cum=0; printf("# hist (f count cumfrac) for f with count>0 (f>=1000 only listed if count>0):\n");
  for(long f=K-1;f<=FMAX;f+=K){ if(hist[f]){cum+=hist[f]; if(f<200||f>=1000) printf("# %ld %ld %.8f\n",f,hist[f],(double)cum/tested);} }
  return 0;}
