// z53_wildcard_counts.c — for each prime p on stdin print
//   p  Rstar  NII  NII_a1  Nh2
// Rstar  = #{(u,B): u<=B, 4uB | p+u+B}                               ((*) pairs, unordered)
// NII    = #{(a,k,h): a<=k, h | a+k, 4ak | p + (a+k)/h}               (full Type II, unordered in (a,k), C determined)
// NII_a1 = same with a = 1  (Lopez b=1 line incl. h>1)
// Nh2    = same with h = 2 only (first non-(*) layer)
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
int main(void){
  u64 p;
  while(scanf("%llu",&p)==1){
    u64 Rs=0,N2=0,Na1=0,Nh2=0;
    for(u64 a=1; 3*a-1<=p; a++){
      for(u64 k=a; 4*a*k-a-k<=p; k++){
        u64 s=a+k, q=4*a*k;
        for(u64 h=1; h<=s; h++){
          if(s%h) continue;
          if((p + s/h)%q==0){ N2++; if(h==1) Rs++; if(a==1) Na1++; if(h==2) Nh2++; }
        }
      }
    }
    printf("%llu %llu %llu %llu %llu\n",p,Rs,N2,Na1,Nh2); fflush(stdout);
  }
  return 0;
}
