/* R98b: from-scratch count of N-points of Sigma^II_{17^K} (4abcd=a+b+Nc), a<=b, 17∤cd, via (a,b):
   e = (-N mod 4ab) must be >0, divide a+b, and d=(N+e)/(4ab)>=1. Reports count with and without 17∤ab. */
#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){ int K=atoi(argv[1]); long long N=1; for(int i=0;i<K;i++) N*=17;
  long long all=0,no17ab=0;
  for(long long a=1; 4*a*a <= N+2*a; a++) for(long long b=a; 4*a*b <= N+a+b; b++){
    long long m=4*a*b, e=(m-N%m)%m; if(e==0||(a+b)%e) continue;
    long long c=(a+b)/e, d=(N+e)/m; if(d<1||c%17==0||d%17==0) continue;
    if(4*a*b*c*d!=a+b+N*c){printf("BUG\n");return 1;}
    all++; if(a%17&&b%17) no17ab++; }
  printf("K=%d D_P=%lld (17∤ab: %lld)\n",K,all,no17ab); }
