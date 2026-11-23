/* Finite saturation certificates, including small-order starts. p <= 1e9,
   so 64-bit products suffice. Odd composite sieve in 8 MB blocks; all
   factorizations by primes from sieve to 31623. Bounded hash load <0.4.
   Failure to certify is reported, not called a nonsaturation. */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define Y 31623
#define B 8388608
#define CAP 524288
#define LIM 200000
static unsigned char com[B],u[Y+1];static int pr[4000],nl,fac[16],nf;
static int seen[CAP],lab[CAP];
static int power(int a,int h,int p){uint64_t b=a,r=1;for(;h;h>>=1,b=b*b%p)if(h&1)r=r*b%p;return r;}
static void factor(int n){nf=0;for(int i=0;i<nl&&pr[i]*pr[i]<=n;++i){int l=pr[i];if(n%l)continue;
    fac[nf++]=l;while(!(n%l))n/=l;}if(n>1)fac[nf++]=n;assert(nf<16);}
/* Smallest divisor h' of p-1 divisible by h with m^h'=1. */
static int join(int m,int h,int p){if(power(m,h,p)==1)return h;int n=p-1;
    for(int i=0;i<nf;i++){int l=fac[i];while(n/l%h==0 && n%l==0 && power(m,n/l,p)==1)n/=l;}return n;}
int main(int ac,char**av){if(ac!=3)return 2;int lo=atoi(av[1]),hi=atoi(av[2]);if(lo<5||lo>hi||hi>1000000000)return 2;
    for(int i=2;i<=Y;++i)if(!u[i]){pr[nl++]=i;for(int j=i*i;j<=Y;j+=i)u[j]=1;}
    int np=0,bad=0,fail29=0,n29=0,wr=0,wp=0,wi=0,wb=0,wbp=0,serial=0;
    for(int s=lo;s<=hi;s+=B){int n=hi-s+1;if(n>B)n=B;memset(com,0,n);
        for(int i=0;i<nl&&(int64_t)pr[i]*pr[i]<s+n;i++){int l=pr[i],j=(l-s%l)%l;
            if(s+j==l)j+=l;
            for(;j<n;j+=l)com[j]=1;}
        for(int d=(1-s%8+8)%8;d<n;d+=8){if(com[d])continue;int p=s+d;++np;factor(p-1);int h=join(2,1,p),idx=(p-1)/h;
            int oddcase=p%24==17 && h%2==1;n29+=oddcase;
            if(idx>wi)wi=idx;
            for(int m=3;m<p&&h*2!=p-1;++m){if(power(m,(p-1)/2,p)!=1)break;h=join(m,h,p);}
            int rounds=0;
            while(2*h!=p-1){int I=(p-1)/h;if(I>LIM)break;int count=0,b=0;++serial;
                while(b+1<p && b<LIM && count<I){int v=power(++b,h,p);
                    unsigned j=(((uint32_t)v*2654435761u)>>(32-19));
                    while(seen[j]==serial && lab[j]!=v)j=(j+1)&(CAP-1);
                    if(seen[j]!=serial){seen[j]=serial;lab[j]=v;++count;}}
                if(count!=I)break;
                if(b>wb){wb=b;wbp=p;}
                int h0=h;
                for(int m=3;m<p && (int64_t)m*b<2LL*p && m<LIM;++m){if(power(m,(p-1)/2,p)==1)h=join(m,h,p);if(h!=h0)break;}
                if(h==h0)break;
                ++rounds;
            }
            if(h*2!=p-1){printf("uncertified %d final index %d oddcase %d\n",p,(p-1)/h,oddcase);bad++;fail29+=oddcase;}
            if(rounds>wr){wr=rounds;wp=p;}
        }
    }printf("[%d,%d] primes 1 mod 8 %d uncertified %d; 17 mod 24 odd ord(2) %d uncertified %d\n",lo,hi,np,bad,n29,fail29);
    printf("largest initial index %d largest completed B %d at %d max successful enlargements %d first %d\n",wi,wb,wbp,wr,wp);
}
