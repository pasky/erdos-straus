/* R282 from-scratch: k-union census over primes via words (Cor 1.2). usage: k8 PB K */
#include <stdio.h>
#include <stdlib.h>
int isp(long x){if(x<2)return 0;for(long q=2;q*q<=x;q++)if(x%q==0)return 0;return 1;}
int main(int c,char**v){long PB=atol(v[1]),K=atol(v[2]);int nu=0,nc=0,nb=0,n1=0;
 for(long p=3;p<PB;p++){ if(!isp(p))continue; int at=0,av=0;
  for(long t=1;t<=p+2&&!(at&&av);t++) for(long u=1;;u++){ long den=t*u-1; if(den>p+u||u>p+2)break; if(den>0&&(p+u)%den==0){long w=(p+u)/den; if(t%K==0)at=1; if(w%K==0||u%K==0)av=1;}}
  if(!at)nc++; if(!av){nb++; if(nb<=10)printf("b1fail %ld\n",p);} if(!at&&!av){nu++; if(p%4==1)n1++; printf("unionfail %ld\n",p);} }
 printf("K=%ld p<%ld: union failures %d (%d are 1 mod 4), c=1 failures %d, b=1 failures %d\n",K,PB,nu,n1,nc,nb);}
