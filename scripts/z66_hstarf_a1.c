// z66 HSTARF: exhaustive a=1 sub-family check: count d>=1 with a divisor q = -1 (mod 4d) of p+4d (d <= (p+2)/4 suffices). usage: ./a1 p1 p2 ...
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef unsigned long long u64;
int main(int argc,char**argv){ for(int i=1;i<argc;i++){ u64 p=strtoull(argv[i],0,10); long cnt=0;
  for(u64 d=1; 4*d-1<=p+4*d; d++){ if(d>p) break; u64 n=4*d,N=p+4*d; for(u64 q=n-1;q<=N;q+=n) if(N%q==0){ cnt++; if(cnt<=3) printf("p=%llu d=%llu q=%llu\n",p,d,q);} }
  printf("p=%llu a1count=%ld\n",p,cnt);} }
