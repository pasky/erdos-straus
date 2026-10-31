// z52b pass1 U09 core: for primes p ≡ 1 (mod 4), p <= X, enumerate the (★) triples
//   R(p) = #{(u,B,C) in N^3 : 4uBC - u - B = p}   (Type II family, c=1)
// Output per prime: p R minC minMax mask64
//   minC   = smallest C among triples (0 if none)
//   minMax = min over triples of max(uBC, pBC, puC)  (denominators of 4/p = 1/(uBC)+1/(pBC)+1/(puC))
//   mask64 = bit (C-1) set iff some triple with that C exists, for C <= 64
// Build: gcc -O2 -o z52b_p1_U09_core scripts/z52b_p1_U09_core.c ; ./z52b_p1_U09_core X > out.txt
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
static int isprime_arr_check(long n){ if(n<2) return 0; for(long d=2; d*d<=n; d++) if(n%d==0) return 0; return 1; }
int main(int argc, char**argv){
  long X = argc>1 ? atol(argv[1]) : 200000;
  char *comp = calloc(X+1,1);
  for(long i=2;i*i<=X;i++) if(!comp[i]) for(long j=i*i;j<=X;j+=i) comp[j]=1;
  for(long p=5;p<=X;p++){
    if(comp[p] || p%4!=1) continue;
    long R=0, minC=0, mu=0, mb=0; long double dummy=0; unsigned long long minMax=0; uint64_t mask=0;
    // u,B >=1 with 4uB - u - B <= p  (needed since C >= 1 gives 4uBC - u - B = p >= 4uB - u - B)
    for(long u=1; ; u++){
      // minimal B for which 4uB-u-B<=p holds is B=1; loop until (4u-1)B - u > p
      if((4*u-1)*1 - u > p) break;
      for(long B=1; ; B++){
        long long t = (long long)(4*u-1)*B - u;   // 4uB - u - B
        if(t > p) break;
        long long s = p + u + B;                    // must be divisible by 4uB, quotient C >= 1
        long long q = 4LL*u*B;
        if(s % q == 0){
          long long C = s / q;
          R++;
          if(minC==0 || C<minC){ minC=C; mu=u; mb=B; }
          unsigned long long a = (unsigned long long)u*B*C, b=(unsigned long long)p*B*C, c=(unsigned long long)p*u*C;
          unsigned long long m = a; if(b>m) m=b; if(c>m) m=c;
          if(minMax==0 || m<minMax) minMax=m;
          if(C<=64) mask |= (1ULL<<(C-1));
        }
      }
    }
    printf("%ld %ld %ld %llu %llu %ld %ld\n", p, R, minC, (unsigned long long)minMax, (unsigned long long)mask, mu, mb);
  }
  return 0;
}
