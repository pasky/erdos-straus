/* R8 AP sieve. Index i represents n = 1 + step*(start+i). See lane note.
   Every exclusion has a primality or a positive-witness justification. */
#include <assert.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef long long I;
static int primes[200000], np;
static unsigned char *reject;
static I step, first, length, last, kill[64][3];
static int nk;

static I gcd(I a, I b) {
    while (b) { I r=a%b; a=b; b=r; }
    return a;
}
static I inv(I a, I m) {
    I x=1, y=0, b=m;
    while (b) { I q=a/b, r=a%b, t=x-q*y; a=b; b=r; x=y; y=t; }
    return (x%m+m)%m;
}
/* Cross off n=res mod mod even when step is not a unit. */
static void cross(I mod, I res) {
    I g=gcd(step,mod), r=(res-first%mod)%mod;
    if (r%g) return;
    I m=mod/g, start=(((r/g+m)%m)*inv(step/g,m))%m;
    for (I i=start; i<length; i+=m) reject[i]=1;
}
static int transfer_hit(I n) {
    for (int i=0; i<nk; i++) {
        I u=kill[i][0], b=kill[i][1], c=kill[i][2];
        if ((n+u)%(8*u*c-1)==0 || (n+b)%(8*b*c-1)==0 || (n+b+u)%(8*b*u)==0)
            return 1;
    }
    return 0;
}
/* All sorted u<=b. Factor the short interval of n+u simultaneously;
   test every divisor d for d=8uc-1 and b=(n+u)/d. */
static int exact_rows(I n) {
    int h=(int)sqrtl(n/8.0L)+2;
    assert((I)8*h*h-2*h>n);
    I *rem=calloc(h+1,sizeof(I)), *divs=malloc(16384*sizeof(I));
    int (*fac)[12]=calloc(h+1,sizeof(*fac)), *nf=calloc(h+1,sizeof(int));
    assert(rem && divs && fac && nf);
    for (int u=1; u<=h; u++) rem[u]=n+u;
    for (int i=0; i<np; i++) {
        I q=primes[i];
        if (q*q>n+h) break;
        for (I u=q-n%q; u<=h; u+=q) {
            assert(nf[u]<12);
            fac[u][nf[u]++]=q;
            while (!(rem[u]%q)) rem[u]/=q;
        }
    }
    int hits=0;
    for (int u=1; u<=h; u++) {
        I num=n+u;
        int nd=1; divs[0]=1;
        for (int j=0; j<nf[u]; j++) {
            I q=fac[u][j], p=1;
            int base=nd;
            while (num%q==0) {
                p*=q; num/=q;
                assert(nd+base<=16384);
                for (int k=0; k<base; k++) divs[nd++]=divs[k]*p;
            }
        }
        assert(num==rem[u]);
        if (num>1) {
            assert(nd*2<=16384);
            for (int k=0; k<nd; k++) divs[nd+k]=divs[k]*num;
            nd*=2;
        }
        for (int k=0; k<nd; k++) {
            I d=divs[k], b=(n+u)/d;
            if (b<u || (d+1)%(8*u)) continue;
            hits++;
            printf("W %lld %d %lld %lld\n",n,u,b,(d+1)/(8*u));
        }
    }
    free(rem); free(divs); free(fac); free(nf);
    return hits;
}
int main(int argc, char **argv) {
    if (argc<5) { fprintf(stderr,"step lower-index count dlimit [witness file]\n"); return 2; }
    step=atoll(argv[1]); I st=atoll(argv[2]); length=atoll(argv[3]); I bound=atoll(argv[4]);
    assert(step>0 && step%8==0 && st>0 && length>0 && length<=200000000);
    assert(bound>=7 && bound<=2000000 && (__int128)step*((__int128)st+length)+1<4000000000000LL);
    first=1+step*st; last=first+step*(length-1);
    if (argc>5) {
        FILE *f=fopen(argv[5],"r"); assert(f);
        I u,b,c;
        while (fscanf(f,"%lld%lld%lld",&u,&b,&c)==3) {
            assert(nk<64 && u>0 && b>0 && c>0);
            assert((__int128)8*u*b*c<10000000000000LL);
            kill[nk][0]=u; kill[nk][1]=b; kill[nk++][2]=c;
        }
        fclose(f);
    }
    reject=calloc(length,1); assert(reject);
    int h=sqrtl(last+sqrtl(last)+10)+1;
    unsigned char *a=calloc(h+1,1); assert(a);
    for (int q=2; q<=h; q++) if (!a[q]) {
        primes[np++]=q;
        for (I j=(I)q*q; j<=h; j+=q) a[j]=1;
        if (first>q) cross(q,0);
        else for (I i=0; i<length; i++) if (first+step*i!=q && (first+step*i)%q==0) reject[i]=1;
    }
    free(a);
    I tot=0, late=0, hard=0, zeros=0, killed=0;
    for (I i=0; i<length; i++) if (!reject[i]) {
        tot++;
        if (transfer_hit(first+step*i)) { killed++; reject[i]=1; }
    }
    for (I t=1; t<=60000; t++) for (I u=1; u*u<=t; u++) if (t%u==0) {
        I b=t/u;
        cross(8*t,-u-b); cross(8*t-1,-u);
        if (u!=b) cross(8*t-1,-b);
    }
    for (I i=0; i<length; i++) if (!reject[i]) {
        late++;
        I n=first+step*i;
        int ok=0;
        for (I d=480007; d<=bound; d+=8) {
            I r=d-n%d;
            if ((d+1)/8%r==0) { ok=1; break; }
        }
        if (!ok) {
            hard++; int count=exact_rows(n);
            printf("EX %lld %d\n",n,count);
            if (!count) zeros++;
        }
    }
    printf("# range %lld %lld step %lld primes %lld filter_excluded %lld late %lld exact %lld zeros %lld\n",
           first,last,step,tot,killed,late,hard,zeros);
    free(reject);
}
