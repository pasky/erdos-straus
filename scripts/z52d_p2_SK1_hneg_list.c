#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(){ long p; while(scanf("%ld",&p)==1){ long D=-4*p,h=0; long amax=(long)sqrt((double)(-D)/3.0)+1;
 for(long a=1;a<=amax;a++) for(long b=-a+1;b<=a;b++){ long num=b*b-D; if(num%(4*a)) continue; long c=num/(4*a); if(c<a) continue; if(c==a&&b<0) continue;
   long g=a, y=labs(b); while(y){long t=g%y; g=y; y=t;} y=labs(c); long gg=g; while(y){long t=gg%y; gg=y; y=t;} if(gg!=1) continue; h++; }
 printf("%ld %ld\n",p,h);} return 0; }
