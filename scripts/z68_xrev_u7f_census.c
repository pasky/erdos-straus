/* Independent U7 census by unordered outer letters and middle letter.
 * Not the lane's (f,r,t) enumeration. Includes y=1 words.
 * gcc -O3 -Wall -Wextra -o /tmp/u7fx scripts/z68_xrev_u7f_census.c
 * ulimit -v 6000000; timeout 1800 /tmp/u7fx 100000000
 * Memory: about 2.13*N bytes; single threaded. N <= 1e9.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
typedef uint64_t U;
static uint8_t *fac, *hits;
static void record(U p,U x,U y,U z) {
    if ((p&7)!=1 || p<17 || (fac[p]&128)) return;
    unsigned e=(unsigned)((x&1)?z:x)&7;
    uint8_t b=e==0?1:e==4?2:e==2?4:8;
    if ((x*y&7)==0) {
        U f=x*y-1;
        if (!(fac[f]&128)) b|=16;
        if ((fac[f]&127)<=2) b|=32;
    }
    if ((z*y&7)==0) {
        U f=z*y-1;
        if (!(fac[f]&128)) b|=16;
        if ((fac[f]&127)<=2) b|=32;
    }
    hits[p/8]|=b;
}
int main(int argc,char **argv) {
    U N=argc==2?strtoull(argv[1],0,10):0;
    if(N<17 || N>1000000000ULL) return 2;
    U F=2*N+1;
    fac=calloc(F+1,1); hits=calloc(N/8+1,1);
    if(!fac || !hits) return 3;
    fac[0]=fac[1]=128;
    for(U q=2;q<=F;q++) if(!fac[q]) {
        fac[q]=1;
        for(U v=2*q;v<=F;v+=q) fac[v]=(fac[v]+1)|128;
    }
    /* y>=2: x<=z and p=(xy-1)z-x imply x<=1+sqrt(N+1).
     * Skip y for which xy*z can never be 0 mod 8 at x+z=7 mod 8.
     * Once x,y are fixed, p=1 mod 8 selects z in one residue mod 8.
     */
    for(U x=1;2*x*x<=N+2*x;x++) {
        U ymax=(N+2*x)/(x*x);
        for(U y=2;y<=ymax;y++) {
            U z0=(15-(x&7))&7;
            if((x*y*z0)&7) continue;
            U z=x+((z0+8-(x&7))&7), d=x*y-1;
            U zmax=(N+x)/d;
            for(;z<=zmax;z+=8) {
                U p=d*z-x;
                record(p,x,y,z);
            }
        }
    }
    /* y=1: p+1=(x-1)(z-1); both letters >1. */
    for(U x=2;(x-1)*(x-1)<=N+1;x++) {
        U z0=(15-(x&7))&7;
        if((x*z0)&7) continue;
        U z=x+((z0+8-(x&7))&7), zmax=(N+1)/(x-1)+1;
        for(;z<=zmax;z+=8) record((x-1)*(z-1)-1,x,1,z);
    }
    U count=0,zero=0,np=0,no2=0,one=0,hist[16]={0};
    for(U p=17;p<=N;p+=8) if(!(fac[p]&128)) {
        count++; unsigned h=hits[p/8],t=h&15; hist[t]++;
        if(!t) {zero++;printf("ZERO %llu\n",(unsigned long long)p);}
        if(!(h&16)) {np++;printf("NOPRIME %llu\n",(unsigned long long)p);}
        if(!(h&32)) {no2++;printf("NOOM2 %llu\n",(unsigned long long)p);}
        if(t && !(t&(t-1))) {one++;printf("ONETYPE %llu mask=%u\n",(unsigned long long)p,t);}
    }
    printf("N=%llu primes=%llu zeros=%llu noprime=%llu noom2=%llu single=%llu\n",
        (unsigned long long)N,(unsigned long long)count,(unsigned long long)zero,
        (unsigned long long)np,(unsigned long long)no2,(unsigned long long)one);
    for(unsigned t=0;t<16;t++) if(hist[t]) printf("TYPESET %x %llu\n",t,(unsigned long long)hist[t]);
    free(fac); free(hits); return 0;
}
