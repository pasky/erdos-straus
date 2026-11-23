/* Exhaust all EVEN x in the smallest-coordinate range, restricted to one
   odd anchor l|x as well as 2,p. If empty, test the complete even-x box. */
#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
static int *sp;
static int cmp(const void*a,const void*b){int x=*(const int*)a,y=*(const int*)b;return (x>y)-(x<y);}
static int anchor(int p,int k,int x){
    int u=x,n2=0;while(!(u&1)){u/=2;n2++;}
    do {int l=sp[u],nl=0;if(u>1)do{u/=l;nl++;}while(u%l==0);
        int64_t amax=1;for(int j=0;j<=nl;++j){for(int e=0;e<=n2;++e){int64_t b=1LL<<e;
            /* +/- both signs, up to simultaneous reversal. */
            int64_t z=amax*b;
            if((z+1)%k==0||(p*z+1)%k==0||(z+p)%k==0||
               (amax+b)%k==0||(p*amax+b)%k==0||(p*b+amax)%k==0)return 1;
        }amax*=l;}
    }while(u>1);
    return 0;
}
static int full(int p,int k,int x){
    int ds[4096],n=1,u=x;ds[0]=1;
    while(u>1){int l=sp[u],a=n,pw=1;do{pw*=l;u/=l;assert(n+a<=4096);
        for(int i=0;i<a;i++)ds[n++]=ds[i]*pw;
    }while(u%l==0);}
    for(int i=0;i<n;i++)ds[i]%=k;
    qsort(ds,n,sizeof(ds[0]),cmp);
    for(int i=0;i<n;i++){int z=k-ds[i],y=k-(int)((int64_t)ds[i]*p%k);
        if(bsearch(&z,ds,n,sizeof(int),cmp)||bsearch(&y,ds,n,sizeof(int),cmp))return 1;}
    return 0;
}
int main(int argc,char**argv){if(argc!=3)return 2;
    int lo=atoi(argv[1]),hi=atoi(argv[2]);if(lo<5||hi<lo||hi>100000000)return 2;
    sp=calloc(hi+1UL,sizeof(int));assert(sp);sp[1]=1;
    for(int l=2;l<=hi;l++)if(!sp[l]){sp[l]=l;if(l<=hi/l)for(int j=l*l;j<=hi;j+=l)if(!sp[j])sp[j]=l;}
    int np=0,na=0,nf=0,ne=0,rec=0,rp=0;const int M[]={1,121,169,289,361,529};
    for(int p=lo;p<=hi;p++){if(sp[p]!=p)continue;int ok=0;for(int j=0;j<6;j++)ok|=p%840==M[j];if(!ok)continue;
        np++;int k;
        for(k=7;k<=2*p;k+=8)if(anchor(p,k,(p+k)/4))break;
        if(k<=2*p){na++;if(k>rec){rec=k;rp=p;}}else{
            for(k=7;k<=2*p;k+=8)if(full(p,k,(p+k)/4))break;
            if(k<=2*p){if(nf<16)printf("one-anchor miss p=%d least full even k=%d\n",p,k);nf++;}
            else {if(ne<16)printf("all-even miss p=%d\n",p);ne++;}
        }
    }printf("[%d,%d] primes %d one-anchor %d max finite k %d at %d full-only %d all-even misses %d\n",lo,hi,np,na,rec,rp,nf,ne);
    free(sp);
}
