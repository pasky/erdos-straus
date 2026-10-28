/* Independent I3 census: factor n+u, rather than sieve word progressions.
   Build: cc -O2 -Wall -Wextra scripts/z49_i3astra_census.c -o /tmp/i3census
   Run: /tmp/i3census 100000 > data/z49_i3astra/census.txt
   Memory < 50 MB at the default bound (includes the hard-prime controls). */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

static uint32_t *spf;
static uint64_t count(uint32_t n) {
    uint64_t ans=0;
    for (uint32_t u=3; 3ULL*u*u-2*u<=n; ++u) {
        uint32_t ds[2048]={1}, len=1, a=n+u;
        while(a>1) {
            uint32_t p=spf[a], old=len, power=1;
            do {
                a/=p; power*=p;
                for(uint32_t j=0;j<old;j++) {
                    if(len>=2048) { fputs("divisor buffer exhausted\n",stderr); exit(2); }
                    ds[len++]=ds[j]*power;
                }
            } while(a>1 && spf[a]==p);
        }
        for(uint32_t j=0;j<len;j++) {
            uint32_t A=ds[j], v=(n+u)/A;
            if(A>=3*u-1 && (A+1)%u==0 && v>=u)
                ans+=(v==u ? 1 : 2);
        }
    }
    return ans;
}
int main(int argc,char **argv) {
    uint32_t N=argc>1 ? (uint32_t)strtoul(argv[1],NULL,10) : 100000;
    if(N<3 || N>10000000) { fputs("require 3 <= N <= 10000000\n",stderr); return 2; }
    uint32_t controls[]={17,241,193,409,577,2521,3361,5569,9601,66529,8813281,49,121,1225,1600,19600,2433600};
    uint32_t max=N>8813281 ? N : 8813281, cap=max+4000;
    spf=calloc((size_t)cap+1,sizeof(*spf));
    if(!spf) { fputs("allocation failed\n",stderr); return 2; }
    for(uint32_t p=2;p<=cap;p++) if(!spf[p]) {
        spf[p]=p;
        if((uint64_t)p*p<=cap)
            for(uint32_t j=p*p;j<=cap;j+=p) if(!spf[j]) spf[j]=p;
    }
    unsigned zeros=0;
    printf("N %u\n",N);
    for(uint32_t n=3;n<=N;n++) {
        uint64_t k=count(n);
        if(!k) { printf("ZERO %u\n",n); zeros++; }
        if(n<=500) printf("SMALL %u %llu\n",n,(unsigned long long)k);
    }
    printf("ZEROS %u\n",zeros);
    for(unsigned i=0;i<sizeof(controls)/sizeof(*controls);i++)
        printf("CONTROL %u %llu\n",controls[i],(unsigned long long)count(controls[i]));
    free(spf);
    return 0;
}
