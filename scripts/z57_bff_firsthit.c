// z57 BFF: first-hit statistics.  For primes p = 1 (4) in [A, B], scan d = 3 (mod 4) upward and
// record d1(p) := least d with 4*n_d | d+1, n_d = d - (p mod d)  (defect form, memo Lemma 1.2);
// also d1prime(p): least such d that is prime; and whether the hit lies in G* (always true when
// d <= p^{3/4} + p^{1/12} + 1 ... but we record anyway), and the exponent log d1 / log p.
// Output: p d1 n1 C1 inG d1prime  (d1 = 0 means no hit with d <= DMAX(p)).
// usage: firsthit A B [dmaxexp]   (scan d up to p^dmaxexp, default 0.80)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

static int isprime64(uint64_t n){ if(n<2)return 0; if(n%2==0)return n==2; for(uint64_t q=3;q*q<=n;q+=2) if(n%q==0) return 0; return 1; }

int main(int argc,char**argv){
  uint64_t A=strtoull(argv[1],0,10), B=strtoull(argv[2],0,10);
  double ex = argc>3? atof(argv[3]) : 0.80;
  if(A%4!=1) A += (5 - A%4)%4;
  for(uint64_t p=A; p<=B; p+=4){
    if(!isprime64(p)) continue;
    uint64_t dmax=(uint64_t)pow((double)p, ex)+10;
    uint64_t d1=0,n1=0,C1=0,dp=0; int inG=0;
    for(uint64_t d=3; d<=dmax; d+=4){
      uint64_t r=p%d; uint64_t n=d-r;
      if((d+1)%(4*n)==0){
        if(!d1){ d1=d; n1=n; C1=(d+1)/(4*n);
          uint64_t m=(p+n)/d; __int128 P=n<m?n:m, Q=n<m?m:n; inG = (Q*Q*Q*Q > P*(__int128)p); }
        if(isprime64(d)){ dp=d; break; }
      }
    }
    printf("%llu %llu %llu %llu %d %llu\n",(unsigned long long)p,(unsigned long long)d1,(unsigned long long)n1,(unsigned long long)C1,inG,(unsigned long long)dp);
  }
  return 0;
}
