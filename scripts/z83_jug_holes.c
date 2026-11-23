/* Literal forward BFS at the two sealed primes, with odd SPF compression.
   < 720 MB at the larger prime. No exit test: enumerate all successors.
   Print a minimum and size for each missing doubling cycle when it really is
   an entire missing cycle. No assumption needed to compute reachability. */
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int has(uint64_t *a,int i){return (a[i>>6]>>(i&63))&1;}
static void put(uint64_t *a,int i){a[i>>6]|=UINT64_C(1)<<(i&63);}
int main(int ac,char**av){if(ac!=2)return 2;int p=atoi(av[1]);if(p!=178481&&p!=164511353)return 2;
    uint16_t *sp=calloc(p,sizeof(*sp));int *todo=malloc((size_t)(p/2)*sizeof(int));
    uint64_t *qr=calloc((p+63)/64,8),*seen=calloc((p+63)/64,8);assert(qr&&seen&&todo&&sp);
    for(int i=3;i*i<2*p;i+=2)if(!sp[i>>1])for(int j=i*i;j<2*p;j+=2*i)if(!sp[j>>1])sp[j>>1]=(uint16_t)i;
    int z=0;for(int i=0;i<p/2;i++){z+=2*i+1;if(z>=p)z-=p;put(qr,z);}
    int q=1;while(has(qr,q))++q;
    int end=1;todo[0]=q;put(seen,q);
    for(int i=0;i<end;i++){
        int n=p+todo[i],ds[4096],nd=1;ds[0]=1;
        while(n>1){int l=(n%2?sp[n>>1]:2);if(!l)l=n;int m=nd,pw=1;do{pw*=l;n/=l;assert(nd+m<=4096);
            for(int j=0;j<m;j++)ds[nd++]=pw*ds[j];}while(n%l==0);}
        for(int j=0;j<nd;j++){int d=ds[j];if(d<p&&!has(qr,d)&&!has(seen,d)){put(seen,d);assert(end<p/2);todo[end++]=d;}}
    }
    printf("prime %d seed %d reachable %d missing %d\n",p,q,end,p/2-end);
    for(int x=1;x<p;++x)if(!has(qr,x)&&!has(seen,x)){int y=x,h=0;do{assert(!has(seen,y));put(seen,y);h++;y=(2*y)%p;}while(y!=x);printf(" missing cycle %d %d\n",x,h);}
    free(sp);free(todo);free(qr);free(seen);
}
