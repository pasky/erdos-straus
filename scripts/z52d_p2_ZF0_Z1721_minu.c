/* Full minimal-u scan, symmetry u<=k. Within least u choose least k;
   count all k at that u, not just the selected witness. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
static int *spf;static uint32_t dv[10000];
static int divisors(int n){int nd=1;dv[0]=1;while(n>1){int q=spf[n],base=nd,pw=1;while(n%q==0){n/=q;pw*=q;for(int j=0;j<base;j++)dv[nd++]=dv[j]*pw;}}return nd;}
int main(int argc,char**argv){if(argc!=2)return 2;int N=atoi(argv[1]),M=N+10000;spf=calloc(M+1,4);for(int i=2;i<=M;i++)if(!spf[i])for(int j=i;j<=M;j+=i)if(!spf[j])spf[j]=i;puts("p,u,k,C,kchoices");uint64_t hist[32]={0};for(int p=5;p<=N;p+=4)if(spf[p]==p){int u,k=0,c=0,choices=0;for(u=1;4LL*u*u-2*u<=p;u++){int nd=divisors(p+u);for(int j=0;j<nd;j++){int d=dv[j],b=(p+u)/d;if((d+1)%(4*u)||b<u)continue;choices++;int lg=0;for(int x=b;x>1;x/=2)lg++;hist[lg]++;if(!k||b<k){k=b;c=(d+1)/(4*u);}}if(k)break;}printf("%d,%d,%d,%d,%d\n",p,k?u:0,k,c,choices);}fprintf(stderr,"all-min-u-k-log2-hist");for(int i=0;i<32;i++)fprintf(stderr," %llu",(unsigned long long)hist[i]);fprintf(stderr,"\ncpu=%.3f\n",(double)clock()/CLOCKS_PER_SEC);free(spf);}
