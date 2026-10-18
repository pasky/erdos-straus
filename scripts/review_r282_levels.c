/* R282 from-scratch: for primes p = 1 mod 4 <= X: R = #(*)-words (4|t), NL = #distinct levels t (4|t) carrying a word.
   Output: p R NL */
#include <stdio.h>
#include <stdlib.h>
int main(int c,char**v){ long X=atol(v[1]); int *R=calloc(X+1,4),*NL=calloc(X+1,4); int *last=calloc(X+1,4); char*comp=calloc(X+1,1);
 for(long t=4;t<=X+2;t+=4) for(long u=1;;u++){ long m=t*u-1; if(m-u>X) break;
   for(long w=1;;w++){ long n=w*m-u; if(n>X)break; if(n<1)continue; R[n]++; if(last[n]!=t){last[n]=t;NL[n]++;} } }
 for(long i=2;i*i<=X;i++) if(!comp[i]) for(long j=i*i;j<=X;j+=i) comp[j]=1;
 for(long p=5;p<=X;p+=4) if(!comp[p]) printf("%ld %d %d\n",p,R[p],NL[p]);
}
