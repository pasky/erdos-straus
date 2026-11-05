// z58 WILDCARD: exact counts N^{(K)}(n) = #{(a,b,c,d) in N^4 : K abcd = a + b + n c} (ordered (a,b)) and the c = 1 line,
// for primes p ≡ 1 (mod 4) in [lo, hi), for K = 4, 8, ..., 4*KMAXQ.  Exact (a,b)-loop: K a b d = n + e, e | a + b
// (e = (a+b)/c); since K ab > a + b there is at most one e per (a,b): e = (-n mod Kab) if 1 <= e <= a+b and e | a+b.
// Output per prime: p N4 R4(c=1) N8 R8 N12 R12 ...
// Usage: count lo hi KMAXQ [step]  (step: take every step-th prime ≡ 1 mod 4)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64;
static int isprime(u64 n){ if(n<2) return 0; for(u64 q=2;q*q<=n;q++) if(n%q==0) return 0; return 1; }
int main(int argc,char**argv){
  u64 lo=strtoull(argv[1],0,10),hi=strtoull(argv[2],0,10); int KQ=atoi(argv[3]); int step=argc>4?atoi(argv[4]):1; int cnt=0;
  for(u64 n=lo|1;n<hi;n+=2){ if((n&3)!=1||!isprime(n)) continue; if((cnt++)%step) continue;
    printf("%llu",n);
    for(int kq=1;kq<=KQ;kq++){ u64 K=4*kq; u64 N=0,R=0;
      for(u64 a=1;K*a+0 <= n + a + 1;a++){            // b >= 1: K a b <= n + a + b needs K a <= n + a + 1 at b = 1
        for(u64 b=1;;b++){ u64 q=K*a*b; if(q > n + a + b) break; u64 r=(q - n%q)%q; if(r==0||r>a+b) continue;
          if((a+b)%r) continue; N++; if(r==a+b) R++; } }
      printf(" %llu %llu",N,R); }
    printf("\n"); fflush(stdout); }
  return 0; }
