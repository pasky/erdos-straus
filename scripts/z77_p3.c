/* r^3 short shifts: peel factors at most e off M. Full-range uint64_t
   with hard input cap r <= 50000. See R17_F3.md. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <assert.h>
typedef uint64_t U;
#define R 50000
#define C 32
static unsigned char comp[R+1];
static U rest[C*R/4+2],g[C*R/4+2],cost[C*R/4+2];
int main(int argc,char **argv){assert(argc==2); int hi=atoi(argv[1]);assert(hi>=17&&hi<=R);
 for(int j=2;j*j<=hi;j++)if(!comp[j])for(int t=j*j;t<=hi;t+=j)comp[t]=1;
 for(U r=17;r<=hi;r++)if(!comp[r]){
    U N=r*r*r,lo=N/4+1,hiM=(N+C*r-1)/4, len=hiM-lo+1;
    for(U k=0;k<len;k++){rest[k]=lo+k;g[k]=cost[k]=1;}
    for(U p=2;p<=r;p++)if(!comp[p])for(U k=(p-lo%p)%p;k<len;k+=p){
       U e=4*(lo+k)-N;unsigned j=0;do{rest[k]/=p;if(g[k]<=e/p)g[k]*=p;else j++;}while(rest[k]%p==0);cost[k]*=2*j+1;}
    U sum[6]={0}, tot=0;
    for(U k=0;k<len;k++){U e=4*(lo+k)-N, x=rest[k];
       if(x<=(e/g[k])){g[k]*=x; x=1;}
       U mult=x==1?1:x<(r+1)*(r+1)?3:9;
       tot+=cost[k]*mult*(g[k]<=e/g[k]?1:2);
       for(int j=0;j<6;j++)if(e<r*(1u<<j))sum[j]=tot;}
    printf("%lu",(unsigned long)r); for(int j=0;j<6;j++)printf(" %lu",(unsigned long)sum[j]);puts("");
 }
}
