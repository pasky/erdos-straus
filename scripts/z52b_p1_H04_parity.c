/* Z1650: parities of natural solution counts at Mordell-hard primes p <= P:
   f(p) = #{x<=y<=z : 4/p = 1/x+1/y+1/z}, split into Type I (p | exactly one denominator) / Type II (two);
   also counts with x minimal & y = z etc. Prints per-prime counts; summary of parities. */
#include <stdio.h>
#include "z52b_p1_H04_fac.h"
static int hard(u64 p){u64 r=p%840;return r==1||r==121||r==169||r==289||r==361||r==529;}
int main(int argc,char**argv){u64 P=atoll(argv[1]);long par[6][2]={{0}};int np=0;
 for(u64 p=5;p<=P;p+=4){if(!isprime(p)||!hard(p))continue;np++;
  long f=0,fI=0,fII=0,fyz=0,fxy=0;
  for(u64 x=p/4+1;4*x<=3*p;x++){u64 a=4*x-p,b=p*x,g=gcdu(a,b);a/=g;b/=g;
    u64 pr[64];int ex[64];int k=factor(b,pr,ex);for(int i=0;i<k;i++)ex[i]*=2;
    /* enumerate divisors D of b^2 with D<=b */
    static u64 d[1<<17];int nd=1;d[0]=1;
    for(int i=0;i<k;i++){int cur=nd;u128 pw=1;for(int e=1;e<=ex[i];e++){pw*=pr[i];if(pw>b)break;for(int j=0;j<cur;j++){u128 v=(u128)d[j]*pw;if(v<=b)d[nd++]=(u64)v;}}}
    for(int j=0;j<nd;j++){u64 D=d[j];if((D+b)%a)continue;u64 y=(D+b)/a;u128 z=((u128)b*b/D+b)/a;if(y<x)continue;
      f++;int c=(x%p==0)+(y%p==0)+(z%p==0);if(c==1)fI++;else fII++;if(y==z)fyz++;if(x==y)fxy++;}}
  long v[6]={f,fI,fII,fyz,fxy,f-fyz};for(int i=0;i<6;i++)par[i][v[i]&1]++;
  printf("%llu f=%ld fI=%ld fII=%ld y=z:%ld x=y:%ld\n",(unsigned long long)p,f,fI,fII,fyz,fxy);}
 const char*nm[6]={"f","f_I","f_II","#(y=z)","#(x=y)","f-#(y=z)"};
 printf("hard primes: %d\n",np);for(int i=0;i<6;i++)printf("%-10s even %ld odd %ld\n",nm[i],par[i][0],par[i][1]);}
