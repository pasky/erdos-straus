#include <stdio.h>
int isp(long n){if(n<2)return 0;for(long d=2;d*d<=n;d++)if(n%d==0)return 0;return 1;}
int main(){long cnt=0;for(long p=5;p<500;p++){if(p%4!=1||!isp(p))continue;
 for(long mu=p+1;mu<=p*p+p+(p+1)/4;mu++){for(long A=2;p*A<2*mu;A+=2){long D=2*mu*A-p*A*A-1;if(D>0&&mu%D==0&&D%p)cnt++;}}}
 printf("%ld\n",cnt);}
