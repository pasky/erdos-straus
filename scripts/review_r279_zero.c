#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static long g(long a,long b){while(b){long t=a%b;a=b;b=t;}return a;}
int main(){ long N=1000000; int *R=calloc(N+1,sizeof(int));
 for(long u=1;3*u-1<=N;u++) for(long B=1;4*u*B-u-B<=N;B++){ if(!((u+B)&1)||g(u,B)!=1) continue; long q=4*u*B; for(long n=q-u-B;n<=N;n+=q) R[n]++; }
 long K[]={10000,30000,100000,300000,1000000}; int k=0; long z=0;
 for(long n=3;n<=N;n+=2){ long r=(long)llround(sqrt((double)n)); if(r*r!=n && R[n]==0) z++; if(n+1==K[k]||n==K[k]-1||n==K[k]){} 
   if(k<5 && n+2>K[k]){ printf("Z(%ld)=%ld\n",K[k],z); k++; } }
}
