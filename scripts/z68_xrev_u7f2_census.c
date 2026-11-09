/* Independent delta census: unordered outer letters, not lane's f,r sieve.
 * Memory <= 2.13*N bytes; N<=1e9; one process. Also direct fixed-n mode.
 * gcc -O3 -Wall -Wextra -Werror -o /tmp/u7f2 scripts/z68_xrev_u7f2_census.c
 * ulimit -v 6000000; timeout 1800 /tmp/u7f2 1000000000
 * /tmp/u7f2 0 < list.txt prints every canonical witness for each input n.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
typedef uint64_t U;
static uint8_t *composite, *hits;
static const U cs[]={1,3,5,7,9,25};
static unsigned mask(U f) {
    unsigned m=0;
    for(unsigned i=0;i<6;i++)
        if(f%cs[i]==0 && !composite[f/cs[i]]) m|=1U<<i;
    return m;
}
static void record(U p,U x,U y,U z) {
    if(p<17 || composite[p]) return;
    unsigned m=0;
    if((x*y)%8==0) m|=mask(x*y-1);
    if((z*y)%8==0) m|=mask(z*y-1);
    hits[p/8]|=m;
}
static int direct(void) {
    unsigned long long n;
    int status;
    while((status=scanf("%llu",&n))==1) {
        if(n<1 || n>1000000000ULL) return 2;
        printf("N %llu\n",n);
        for(U f=7;f<=2*n+1;f+=8) {
            U r=(f-n%f)%f;
            if(r && (f+1)%r==0)
                printf("W %llu %llu %llu %llu\n",(unsigned long long)f,
                    (unsigned long long)r,(unsigned long long)((f+1)/r),
                    (unsigned long long)((n+r)/f));
        }
    }
    return status==EOF ? 0 : 2;
}
int main(int argc,char **argv) {
    if(argc!=2) return 2;
    U N=strtoull(argv[1],0,10);
    if(!N) return direct();
    if(N<17 || N>1000000000ULL) return 2;
    U F=2*N+1;
    composite=calloc(F+1,1);hits=calloc(N/8+1,1);
    if(!composite || !hits) return 3;
    composite[0]=composite[1]=1;
    for(U q=2;q*q<=F;q++) if(!composite[q])
        for(U v=q*q;v<=F;v+=q) composite[v]=1;
    for(U x=1;2*x*x<=N+2*x;x++) {
        U ymax=(N+2*x)/(x*x);
        for(U y=2;y<=ymax;y++) {
            U z0=(15-(x%8))%8;
            if((x*y*z0)%8) continue;
            U z=x+((z0+8-x%8)%8), d=x*y-1;
            for(U zmax=(N+x)/d;z<=zmax;z+=8) record(d*z-x,x,y,z);
        }
    }
    for(U x=2;(x-1)*(x-1)<=N+1;x++) {
        U z0=(15-(x%8))%8;
        if(x*z0%8) continue;
        U z=x+((z0+8-x%8)%8);
        for(U zmax=(N+1)/(x-1)+1;z<=zmax;z+=8)
            record((x-1)*(z-1)-1,x,1,z);
    }
    U bounds[]={10000000,100000000,1000000000};
    for(unsigned b=0;b<3;b++) {
        U B=bounds[b];if(B>N) continue;
        U cnt=0,n1=0,n13=0,n135=0,none=0,n3=0,n5=0;
        for(U p=17;p<=B;p+=8) if(!composite[p]) {
            unsigned m=hits[p/8];cnt++;
            n1+=!(m&1);n13+=!(m&3);n135+=!(m&7);none+=!m;
            n3+=!(m&2);n5+=!(m&4);
            if(B==N && !(m&1)) printf("NOPRIME %llu mask=%u\n",(unsigned long long)p,m);
        }
        printf("COUNT %llu %llu %llu %llu %llu %llu %llu %llu\n",
            (unsigned long long)B,(unsigned long long)cnt,(unsigned long long)n1,
            (unsigned long long)n13,(unsigned long long)n135,(unsigned long long)none,
            (unsigned long long)n3,(unsigned long long)n5);
    }
    free(composite);free(hits);return 0;
}
