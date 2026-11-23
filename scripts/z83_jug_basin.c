/* Full distances to the nearest reciprocal exit. Predecessors generated on
   demand through integer multiples, not through the forward factor engine. */
#include <assert.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LEVELS 256
struct summary { uint64_t hist[LEVELS], sinks,extra,np,n; int record,p,x; };
static void census(int p, unsigned char *com, unsigned char *qr,
                   int *fifo, unsigned char *ds, struct summary *s){
    memset(qr,0,p); memset(ds,255,p); qr[0]=1;
    /* Sequential squares modulo p by first differences. */
    int square=0;
    for(int a=0;a<p/2;++a){square+=2*a+1; if(square>=p)square-=p; qr[square]=1;}
    int end=0;
    /* Smaller outer letter b need not be negative. A=p+b divided by the
       other letter v is t*b-1. Scan the divisors by trial (through sqrt),
       avoiding duplicate vertices. O(p) loop at b<=sqrt(p). */
    for(int b=2;2*b*b-2*b<=p;++b){int n=p+b;
        for(int k=1;k*k<=n;++k)if(n%k==0){int ds2[2]={k,n/k};
            for(int z=0;z<2;++z){int d=ds2[z],v=n/d;
                if(v<b || (d+1)%b || (d+1)/b<2 || qr[v]==qr[b])continue;
                int x=qr[b]?v:b;
                if(ds[x]==255){ds[x]=0;fifo[end++]=x;}
            }
        }
    }
    for(int i=0;i<end;++i){int x=fifo[i];assert(!qr[x]);
        for(int a=x-p%x;a<p;a+=x)if(!qr[a] && ds[a]==255){
            assert(ds[x]<254);ds[a]=ds[x]+1;fifo[end++]=a;
        }
    }
    for(int x=2;x<p;++x)if(!qr[x]){++s->n;
        if(ds[x]==255){if(!com[p+x])++s->sinks;else ++s->extra;}
        else {assert(com[p+x]);++s->hist[ds[x]];
            if(ds[x]>s->record){s->record=ds[x];s->p=p;s->x=x;}
        }
    }++s->np;
}
int main(int argc,char **argv){if(argc!=5){fprintf(stderr,"low high modulus residue\n");return 2;}
    int lo=atoi(argv[1]),hi=atoi(argv[2]),m=atoi(argv[3]),r=atoi(argv[4]);
    if(lo<5||hi<lo||hi>50000000||m<8||m>hi||m%8||r<1||r>=m||r%8!=1)return 2;
    unsigned char *com=calloc(2UL*hi+1,1),*qr=malloc(hi),*ds=malloc(hi);
    int *fifo=malloc((hi/2UL+1)*sizeof(*fifo));assert(com&&qr&&ds&&fifo);
    for(int l=2;l*l<=2*hi;++l)if(!com[l])for(int j=l*l;j<=2*hi;j+=l)com[j]=1;
    struct summary s={0};
    for(int p=lo+(r-lo%m+m)%m;p<=hi;p+=m)if(!com[p])census(p,com,qr,fifo,ds,&s);
    printf("[%d,%d] %d mod %d primes %" PRIu64 " negative vertices %" PRIu64 " prime-shift sinks %" PRIu64 " other misses %" PRIu64 "\n",lo,hi,r,m,s.np,s.n,s.sinks,s.extra);
    printf("distances");for(int k=0;k<=s.record;k++)printf(" %" PRIu64,s.hist[k]);
    printf("\nfirst maximum (p,x,depth) %d %d %d\n",s.p,s.x,s.record);
    free(fifo);free(ds);free(qr);free(com);
}
