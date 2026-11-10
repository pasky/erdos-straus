// Independent unordered-outer-letter certificate census. Build: cc -O2 FILE -lm -o OUT
// Run OUT N. Arrays contain only n=1 mod 4; at N=1e9 total storage <501 MB.
#include <assert.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static int cert(long x,long y,long z) {
    return !(x%4) || !(y%4) || !(z%4) || (y%4==3 && (x%4==3 || z%4==3));
}
static int square(long n) {
    long s=(long)sqrt((double)n);
    return s*s==n || (s+1)*(s+1)==n;
}
int main(int argc,char **argv) {
    assert(argc==2);
    long N=strtol(argv[1],NULL,10);
    assert(N>=5 && N<=1000000000L);
    size_t size=(size_t)(N/4+1);
    uint8_t *cnt=calloc(size,1), *composite=calloc(size,1);
    assert(cnt && composite);
    // x<=z implies n>=x*x*y-2*x >= (x-1)^2-1.
    for(long x=1;(x-1)*(x-1)<=N+1;x++) {
        long ymax=(N+2*x)/(x*x);
        for(long y=1;y<=ymax;y++) {
            long f=x*y-1;
            if(!f) continue;
            long low=(x+1+f-1)/f;
            if(low<x) low=x;
            long high=(N+x)/f;
            // Intersect n=1 mod 4 and the certificate predicate before visiting z.
            for(long r=0;r<4;r++) {
                if(((f*r-x-1)%4) || !cert(x,y,r)) continue;
                long first=low+((r-low)%4+4)%4;
                for(long z=first;z<=high;z+=4) {
                    long n=f*z-x;
                    if(n<5) continue;
                    size_t i=(size_t)(n/4);
                    int c=cnt[i]+(x==z?1:2);
                    cnt[i]=(uint8_t)(c>255?255:c);
                }
            }
        }
    }
    long root=(long)sqrt((double)N);
    uint8_t *small=calloc((size_t)root+1,1);
    assert(small);
    for(long q=2;q<=root;q++) if(!small[q]) {
        for(long t=q*q;t<=root;t+=q) small[t]=1;
        if(q==2) continue;
        long start=q*q;
        while(start%4!=1) start+=q;
        for(long n=start;n<=N;n+=4*q) composite[n/4]=1;
    }
    long sq=0,zeros=0;
    for(long n=5;n<=N;n+=4) {
        if(square(n)) { assert(!cnt[n/4]); sq++; }
        else if(!cnt[n/4]) { zeros++; assert(n==105); }
    }
    printf("N=%ld; square zeros=%ld; non-square zeros=%ld\n",N,sq,zeros);
    for(int k=0;k<=8;k+=2) {
        long total=0,last=0,primes=0,lastp=0;
        for(long n=5;n<=N;n+=4) if(!square(n) && cnt[n/4]<=k) {
            total++;last=n;
            if(!composite[n/4]) {primes++;lastp=n;}
        }
        printf("cnt<=%d: %ld last=%ld; primes=%ld last=%ld\n",k,total,last,primes,lastp);
    }
    for(long lo=1024;lo<N;lo*=4) {
        long hi=lo*4<N?lo*4:N,am=0,ap=0;
        int mn=256,mp=256;
        for(long n=lo+1;n<=hi;n+=4) if(!square(n)) {
            if(cnt[n/4]<mn) {mn=cnt[n/4];am=n;}
            if(!composite[n/4] && cnt[n/4]<mp) {mp=cnt[n/4];ap=n;}
        }
        printf("block (%ld,%ld]: %d at %ld; primes %d at %ld\n",lo,hi,mn,am,mp,ap);
    }
    free(small);free(composite);free(cnt);
    return 0;
}
