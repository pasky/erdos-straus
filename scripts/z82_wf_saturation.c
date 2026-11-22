/* Complete negative closure, no stopping at reciprocal hits. Fixed 1e6 ceiling. */
#include <assert.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#define P 1000000
static int sp[2*P+1],fifo[P],divs[4096]; static unsigned char qr[P],seen[P];
int main(void){for(int i=2;i<=2*P;i++)if(!sp[i])for(int j=i;j<=2*P;j+=i)if(!sp[j])sp[j]=i;
 int np=0,missing=0;uint64_t total=0;for(int p=841;p<=P;p+=840){if(sp[p]!=p)continue;np++;memset(qr,0,p);memset(seen,0,p);for(int i=1;i<=p/2;i++)qr[(uint64_t)i*i%p]=1;
 int q=2;while(qr[q])q++;int tail=1;fifo[0]=q;seen[q]=1;
 for(int i=0;i<tail;i++){int n=p+fifo[i],cnt=1;divs[0]=1;while(n>1){int l=sp[n],old=cnt,pow=1;do{pow*=l;n/=l;assert(cnt+old<=4096);for(int j=0;j<old;j++)divs[cnt++]=divs[j]*pow;}while(n%l==0);}
 for(int j=0;j<cnt;j++){int d=divs[j];if(d<p&&!qr[d]&&!seen[d]){seen[d]=1;fifo[tail++]=d;}}}
 if(tail!=p/2){missing++;printf("MISS %d q %d reachable %d\n",p,q,tail);}total+=tail;}
 printf("up to %d primes %d nonsaturations %d total vertices %llu\n",P,np,missing,(unsigned long long)total);}
