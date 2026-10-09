/* emn2_scan.c — O102: m-representability of primes p (m/p = 1/x+1/y+1/z), via
 * Pomerance–Weingartner Cor 2.2 (Type I) and Cor 2.4 (Type II):
 *   Type II: exists a,b,e: e | a+b, mab | p+e   (then mab <= 2p, PW (3.4); e < mab so
 *            e = (-p mod mab) is forced)
 *   Type I : exists a,d,f: f | m a^2 d + 1, mad | p+f   (mad <= 3p, PW Lemma 7.4)
 * Primes p | m are skipped (proportions are over p not dividing m).
 * count=2: also print each exceptional prime as 'E p' (for per-prime validation).
 * Usage: emn2_scan m P1 P2 [count [stride]]  (stride k: test every k-th prime)   -> scans primes p in (P1, P2]
 * Output: m P1 P2 nprimes nrep nTypeIIonly nTypeIonly [sumII sumI] (counts of tuples if count=1)
 * Counting mode counts Type II tuples (a,b) and Type I tuples (a,d,f) (f a divisor in the class).
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static int isprime(u64 n){ if(n<2) return 0; for(u64 q=2;q*q<=n;q++) if(n%q==0) return 0; return 1; }
static int64_t inv_mod(int64_t a, int64_t mod){ /* a^{-1} mod mod, assumes gcd=1 */
  int64_t g=mod, x=0, x1=1, a1=a%mod; if(a1<0)a1+=mod; int64_t b=a1;
  int64_t r0=mod, r1=b, s0=0, s1=1; while(r1){ int64_t q=r0/r1, t=r0-q*r1; r0=r1; r1=t; t=s0-q*s1; s0=s1; s1=t; }
  (void)g;(void)x;(void)x1; if(r0!=1) return -1; s0%=mod; if(s0<0) s0+=mod; return s0; }
static u64 isqrt(u64 n){ u64 r=(u64)__builtin_sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++; return r; }
/* Type II tuples */
static long typeII(u64 m, u64 p, int count){ long c=0;
  for(u64 a=1; m*a*a<=2*p /* a<=b */; a++) for(u64 b=a; m*a*b<=2*p; b++){
      u64 Q=m*a*b; u64 r=(Q - p%Q)%Q; if(r==0) continue; if((a+b)%r==0){ c++; if(!count) return 1; } }
  return c; }
/* Type I tuples: f | n = m a^2 d + 1, f ≡ -p (mod Q), Q = m a d <= 3p. Enumerate f <= sqrt(n) in class -p,
   and cofactors g <= sqrt(n) with g ≡ -p^{-1} (mod Q) (since f g ≡ 1 mod Q). */
static long typeI(u64 m, u64 p, int count){ long c=0;
  for(u64 a=1; m*a<=3*p; a++) for(u64 d=1; m*a*d<=3*p; d++){
      u64 Q=m*a*d; u128 n=(u128)m*a*a*d+1; u64 s=isqrt((u64)n); /* n < 2^64 for our ranges */
      u64 r=(Q - p%Q)%Q; if(r==0) continue; /* f ≡ r mod Q */
      for(u64 f=r; f<=s; f+=Q) if((u64)(n%f)==0){ c++; if(!count) return 1; }
      int64_t pinv=inv_mod((int64_t)(p%Q),(int64_t)Q); if(pinv<0) continue;
      u64 g0=(Q-(u64)pinv)%Q; if(g0==0) g0=Q; /* g ≡ -p^{-1} */
      for(u64 g=g0; g<=s; g+=Q) if((u64)(n%g)==0){ u64 f=(u64)(n/g); if(f==g) continue; c++; if(!count) return 1; }
  }
  return c; }
int main(int argc,char**argv){ if(argc<4){fprintf(stderr,"usage\n");return 1;}
  u64 m=strtoull(argv[1],0,10), P1=strtoull(argv[2],0,10), P2=strtoull(argv[3],0,10); int count=argc>4?atoi(argv[4]):0; u64 stride=argc>5?strtoull(argv[5],0,10):1; if(!stride) stride=1; u64 idx=0;
  long np=0,nrep=0,n2only=0,n1only=0; double s2=0,s1=0;
  for(u64 p=P1+1;p<=P2;p++){ if(!isprime(p)) continue; if(m%p==0) continue; if((idx++)%stride) continue; np++;
    long t2=typeII(m,p,count==1), t1=typeI(m,p,count==1);
    if(count==2 && !t2 && !t1) printf("E %llu\n",p);
    if(t2||t1) nrep++;
    if(t2&&!t1) n2only++;
    if(t1&&!t2) n1only++;
    s2+=t2; s1+=t1; }
  printf("%llu %llu %llu %ld %ld %ld %ld %.6f %.6f\n",m,P1,P2,np,nrep,n2only,n1only,count?s2/np:-1.0,count?s1/np:-1.0);
  return 0; }
