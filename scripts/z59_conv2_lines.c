// z59 CONV2: census of unions of coordinate lines of the numerator-K Type II family
//   K abcd = a + b + n c   (K ≡ 0 mod 4; K = 4 is Elsholtz–Tao Type II, K = 8 its d-even half / numerator 8).
// Lines (bit mask LINES): 1 = {c = 1}  (the (★) line; K = 8: R_8, the C-even half of (★))
//                         2 = {a = 1 or b = 1}  (López Type A / "b = 1 line")
//                         4 = {d = 1}
//                         8 = full family (no restriction)
// Target-set form (Z57_BFII Lemma 1.1(d), any K): a solution exists iff some f ≡ -1 (mod K) has
//   -n mod f in T_f(LINES) = { a c^{-1} : (a, c, d) with a c d = m_f := (f+1)/K and (a,c,d) on a selected line }.
// Every solution (a,b,c,d) has the two witnesses f = K acd - 1 (target a/c) and f' = K bcd - 1 (target b/c); a solution
// with b = 1 is found through f' (whose "a"-coordinate is 1), so restricting the a-coordinate of the witness to 1 captures
// the union a = 1 ∪ b = 1.
// For each odd n in [lo, hi) (optionally n ≡ 1 mod 4, primes only): least witness f <= FMAX by bitmap lookup; non-squares
// without witness <= FMAX are decided EXACTLY by the (a,b) loop K a b d = n + e, e | a + b (e = (a+b)/c), a <= b, with the
// line filters applied to the solution (c == 1; a == 1; d == 1).  Odd squares are zeros (T1, PROVED) and only counted.
// Output: "ZERO n P|C" / "LATE n P|C f a b c d" lines + summary.
// Usage: lines K LINES lo hi FMAX [primes_only 0/1] [mod4 0/1/3]
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef unsigned long long u64;
static long K; static int LINES;
static uint8_t **bm;
static long inv(long c,long f){ long t=0,nt=1,r=f,nr=c%f; while(nr){long q=r/nr,tmp=t-q*nt;t=nt;nt=tmp;tmp=r-q*nr;r=nr;nr=tmp;} if(r!=1) return -1; if(t<0)t+=f; return t;}
static int issq(u64 n){u64 r=(u64)sqrtl((long double)n); while(r*r>n)r--; while((r+1)*(r+1)<=n)r++; return r*r==n;}
static int online(u64 a,u64 b,u64 c,u64 d){
  if(LINES&8) return 1;
  if((LINES&1)&&c==1) return 1;
  if((LINES&2)&&(a==1||b==1)) return 1;
  if((LINES&4)&&d==1) return 1;
  return 0;}
static int exact(u64 n,u64*oa,u64*ob,u64*oc,u64*od){
  for(u64 a=1;;a++){ if((u64)K*a*a > n + 2*a) break;
    for(u64 b=a;;b++){ u64 q=(u64)K*a*b; if(q > n + a + b) break; u64 r=(q - n%q)%q; if(r==0||r>a+b) continue; if((a+b)%r) continue;
      u64 c=(a+b)/r, d=(n+r)/q; if(!online(a,b,c,d)) continue;
      *oa=a;*ob=b;*oc=c;*od=d; return 1; } }
  return 0;}
int main(int argc,char**argv){
  if(argc<6){fprintf(stderr,"usage: lines K LINES lo hi FMAX [primes_only] [mod4]\n");return 1;}
  K=atol(argv[1]); LINES=atoi(argv[2]); u64 lo=strtoull(argv[3],0,10),hi=strtoull(argv[4],0,10); long FMAX=atol(argv[5]);
  int primes_only=argc>6?atoi(argv[6]):0; int m4=argc>7?atoi(argv[7]):0;
  if(K<4||K%4||LINES<1||LINES>15||FMAX<K-1||hi<=lo){fprintf(stderr,"bad args\n");return 1;}
  bm=calloc(FMAX+1,sizeof(uint8_t*)); if(!bm) return 2;
  for(long f=K-1;f<=FMAX;f+=K){ long m=(f+1)/K; bm[f]=calloc(f/8+1,1); if(!bm[f]) return 2;
    for(long c=1;c<=m;c++){ if(m%c) continue; long ci=inv(c,f); if(ci<0) continue; long mc=m/c;
      for(long a=1;a<=mc;a++){ if(mc%a) continue; long d=mc/a;
        int ok=(LINES&8)||((LINES&1)&&c==1)||((LINES&2)&&a==1)||((LINES&4)&&d==1); if(!ok) continue;
        long t=(long)((u64)a*ci%f); bm[f][t>>3]|=1<<(t&7);} } }
  u64 sq=(u64)sqrtl((long double)hi)+2; char*small=calloc(sq+1,1); long*pr=malloc(sizeof(long)*(sq+1)); long np=0;
  for(u64 i=2;i<=sq;i++) if(!small[i]){pr[np++]=i; for(u64 j=i*i;j<=sq;j+=i) small[j]=1;}
  u64 SEG=1<<24; char*seg=malloc(SEG);
  long tested=0,nsq=0,nlate=0,nzero=0,nzeroP=0,maxf=0,maxfP=0; u64 argmax=0,argmaxP=0;
  for(u64 s=lo;s<hi;s+=SEG){u64 e=s+SEG<hi?s+SEG:hi; memset(seg,0,e-s);
    for(long i=0;i<np;i++){u64 q=pr[i]; if(q*q>=e) break; u64 st=((s+q-1)/q)*q; if(st<q*q) st=q*q; for(u64 j=st;j<e;j+=q) seg[j-s]=1;}
    for(u64 n=s;n<e;n++){ if(!(n&1)||n<3) continue; if(m4 && (long)(n&3)!=m4) continue;
      int isp=!seg[n-s]; if(primes_only && !isp) continue; tested++;
      long best=0;
      for(long f=K-1;f<=FMAX;f+=K){ long t=(long)((f - n%f)%f); if(bm[f][t>>3]&(1<<(t&7))){best=f;break;} }
      if(best){ if(best>maxf){maxf=best;argmax=n;} if(isp&&best>maxfP){maxfP=best;argmaxP=n;} continue; }
      if(issq(n)){ nsq++; continue; }
      u64 a,b,c,d; nlate++;
      if(exact(n,&a,&b,&c,&d)){ printf("LATE %llu %s f=%llu a=%llu b=%llu c=%llu d=%llu\n",n,isp?"P":"C",(u64)K*a*c*d-1,a,b,c,d); }
      else { nzero++; if(isp) nzeroP++; printf("ZERO %llu %s\n",n,isp?"P":"C"); }
      fflush(stdout); } }
  printf("# K=%ld LINES=%d range [%llu,%llu) odd%s mod4=%d FMAX=%ld: tested %ld; odd squares %ld; non-squares w/o witness<=FMAX %ld; exact zeros %ld (primes %ld)\n",
    K,LINES,lo,hi,primes_only?" primes":"",m4,FMAX,tested,nsq,nlate,nzero,nzeroP);
  printf("# max least witness (bitmap hits) %ld at n=%llu; primes %ld at p=%llu\n",maxf,argmax,maxfP,argmaxP);
  return 0;}
