/* R282 from-scratch: for all n <= X count words (t,u,v), t*u*v-u-v=n: W, A (4|t), B (4|u or 4|v), U (some coord = 0 mod 4).
   F = #words with one of the five ES-five conditions (= #sigma=-1 words for p = 1 mod 4). Output for primes p = 1 mod 4: p W A B U F */
#include <stdio.h>
#include <stdlib.h>
int main(int c,char**v){ long X=atol(v[1]);
 int *W=calloc(X+1,4),*A=calloc(X+1,4),*B=calloc(X+1,4),*U=calloc(X+1,4),*F=calloc(X+1,4); char*comp=calloc(X+1,1);
 for(long t=1;t<=X+2;t++) for(long u=1;;u++){ long m=t*u-1; if(m-u>X || (t==1 && u>X+2)) break; if(m<1) continue;
   for(long w=1;;w++){ long n=w*m-u; if(n>X)break; if(n<1)continue; W[n]++;
     int a=(t%4==0), b=(u%4==0||w%4==0); A[n]+=a; B[n]+=b; U[n]+=(a||b); F[n]+=(a||b||(t*u-1)%4==0||(t*w-1)%4==0);} }
 for(long i=2;i*i<=X;i++) if(!comp[i]) for(long j=i*i;j<=X;j+=i) comp[j]=1;
 for(long p=5;p<=X;p+=4) if(!comp[p]) printf("%ld %d %d %d %d %d\n",p,W[p],A[p],B[p],U[p],F[p]);
}
