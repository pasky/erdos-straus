// class number h(D) of primitive positive definite binary quadratic forms of discriminant D<0 (D = b^2-4ac, D ≡ 0,1 mod 4),
// via reduced forms (|b| <= a <= c, b>=0 if |b|=a or a=c). Reads "p" per line, prints "p h(-4p) h(-8p) h(-3p) h(-20p)"
// (only meaningful when those are discriminants; -3p and -8p, -4p fundamental for p prime ≡1 mod 4, p>3).
#include <stdio.h>
#include <stdlib.h>
static long hD(long D){ // D<0
  long h=0; long A=-D;
  for(long a=1; 3*a*a<=A; a++) for(long b=-a+1; b<=a; b++){
      long t=b*b-D; if(t%(4*a)) continue; long c=t/(4*a); if(c<a) continue;
      if(c==a && b<0) continue; // reduced: b>=0 when a==c (|b|=a case handled: b=-a excluded by range)
      h++; }
  return h; }
int main(){ long p; while(scanf("%ld",&p)==1){ printf("%ld %ld %ld %ld %ld\n", p, hD(-4*p), hD(-8*p), hD(-3*p), hD(-20*p)); } return 0; }
