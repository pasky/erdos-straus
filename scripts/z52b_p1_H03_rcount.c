// R(p) = #{(u,B,C): 4uBC-u-B=p} for all primes p ≡ 1 (4) in [LO,X]; prints "p R".
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
int main(int c,char**v){u64 LO=strtoull(v[1],0,10),X=strtoull(v[2],0,10);
 char*s=calloc(X+1,1);for(u64 i=2;i*i<=X;i++)if(!s[i])for(u64 j=i*i;j<=X;j+=i)s[j]=1;
 for(u64 p=5;p<=X;p+=4){if(s[p]||p<LO)continue;u64 R=0;
  for(u64 C=1;4*C-1<=p+1;C++)for(u64 u=1;u*(4*C-1)<=p+1;u++){u64 m=4*u*C-1;if((p+u)%m==0)R++;}
  printf("%llu %llu\n",p,R);}
}
