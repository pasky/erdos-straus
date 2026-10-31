// z52b pass1 U09 (Z1848): R(p) = #{(u,B,C): 4uBC-u-B=p} for primes p read from stdin (one per line).
// Output: p R minC.   Build: gcc -O2 -o z52b_p1_U09_families scripts/z52b_p1_U09_families.c
#include <stdio.h>
int main(){
  long p; 
  while(scanf("%ld",&p)==1){
    long R=0, minC=0;
    for(long u=1; (4*u-1)-u <= p; u++){
      for(long B=1; ; B++){
        long t=(4*u-1)*B-u; if(t>p) break;
        long s=p+u+B, q=4*u*B;
        if(s%q==0){ long C=s/q; R++; if(minC==0||C<minC) minC=C; }
      }
    }
    printf("%ld %ld %ld\n",p,R,minC);
  }
  return 0;
}
