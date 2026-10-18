/* O275: complete positive-word forests, streamed AP construction.
 * Build: cc -O2 -std=c11 scripts/z43_astra_forest.c -o /tmp/z43-astra-forest
 * Run: /tmp/z43-astra-forest 1000000
 * Memory: O(N + number of words at selected primes/squares), no dense graphs.
 */
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct { int u, v, next; } Edge;
static Edge *edges;
static size_t used, capacity;
static int *head;
static void add(int n, int u, int v) {
    if (used == capacity) {
        capacity = capacity ? 2*capacity : 65536;
        assert(capacity < 100000000); /* <1.2 GB edge storage */
        Edge *next = realloc(edges, capacity*sizeof(*edges));
        assert(next); edges=next;
    }
    edges[used]=(Edge){u,v,head[n]}; head[n]=(int)used++;
}
static int jacobi(int a, int n) {
    int s=1; a%=n;
    while(a) {
        while(!(a&1)) { a/=2; if(n%8==3 || n%8==5) s=-s; }
        int tmp=a; a=n; n=tmp;
        if(a%4==3 && n%4==3) s=-s;
        a%=n;
    }
    return n==1?s:0;
}
static int root(int v, int *parent) {
    while(parent[v]) v=parent[v];
    return v;
}
static int check_divisors(int n, int *parent, int *spf) {
    int count=0;
    for(int u=1;(int64_t)(u-1)*(u-1)<=n+1;u++) {
        int ds[4096], nd=1, x=n+u; ds[0]=1;
        while(x>1) {
            int q=spf[x], power=1, old=nd;
            while(x%q==0) {
                x/=q; power*=q;
                for(int j=0;j<old;j++) {assert(nd<4096);ds[nd++]=ds[j]*power;}
            }
        }
        for(int j=0;j<nd;j++) {
            int v=ds[j];
            if(v>u && (n+(int64_t)u+v)%((int64_t)u*v)==0) {
                assert(parent[v]==u); count++;
            }
        }
    }
    return count;
}
static int five(int t,int u,int v,int k) {
    return t%k==0 || u%k==0 || v%k==0 ||
           ((int64_t)t*u-1)%k==0 || ((int64_t)t*v-1)%k==0;
}
int main(int argc, char **argv) {
    const int N=argc>1?atoi(argv[1]):1000000;
    assert(N>=300 && N<=10000000);
    unsigned char *prime=calloc(N+1,1), *selected=calloc(N+1,1);
    head=malloc((N+1)*sizeof(int));
    int *parent=calloc(N+3,sizeof(int));
    int *seen=calloc(N+3,sizeof(int)), *verts=malloc((N+3)*sizeof(int));
    int *mixed=calloc(N+3,sizeof(int));
    assert(prime&&selected&&head&&parent&&seen&&verts&&mixed);
    for(int n=2;n<=N;n++) prime[n]=1;
    for(int i=2;(int64_t)i*i<=N;i++) if(prime[i])
        for(int j=i*i;j<=N;j+=i) prime[j]=0;
    for(int n=0;n<=N;n++) {head[n]=-1; selected[n]=prime[n];}
    for(int m=3;(int64_t)m*m<=N;m+=2) selected[m*m]=1;
    /* For u<=v, n=tuv-u-v, t>=1. u=1 requires t>=2.
       Diagonals are omitted. (u-1)^2<=N+1 is a necessary cutoff. */
    for(int u=1;(int64_t)(u-1)*(u-1)<=N+1;u++) {
        int vmax=u==1?N+1:(N+u)/(u-1);
        for(int v=u+1;v<=vmax;v++) {
            int64_t q=(int64_t)u*v;
            int64_t n=(u==1?2:1)*q-u-v;
            for(;n<=N;n+=q) if(n>=3 && selected[n]) add((int)n,u,v);
        }
    }
    int S=N+2;
    while((int64_t)(S-N-2)*(S-N-2)<=N+1) S++;
    int *spf=calloc(S+1,sizeof(int)); assert(spf);
    for(int i=2;i<=S;i++) if(!spf[i])
        for(int j=i;j<=S;j+=i) if(!spf[j]) spf[j]=i;
    long primes=0, squares=0, eligible=0, allfail=0, seedfail=0;
    long seed12fail=0, negative_edges=0, word_count=0;
    int maxdepth=0, maxdepthn=0, max_seed_min=0, max_seed_n=0;
    int first_seed[16], nfirst=0, first_qnr[16], nqnr=0;
    long qnr_fail=0, qnr_parent_hits=0;
    for(int n=3;n<=N;n+=2) if(selected[n]) {
        int nv=0, ec=0, neg=0, seedneg=0, seed12neg=0, minroot=N+3;
        for(int e=head[n];e>=0;e=edges[e].next) {
            int u=edges[e].u,v=edges[e].v;
            assert(parent[v]==0); parent[v]=u;
            if(seen[u]!=n) {seen[u]=n; verts[nv++]=u;}
            if(seen[v]!=n) {seen[v]=n; verts[nv++]=v;}
            assert(u<v && (n+u+v)%((int64_t)u*v)==0);
            assert(u==(v-n%v)%v);
            int t=(int)((n+(int64_t)u+v)/((int64_t)u*v));
            assert((int64_t)t*u*v-u-v==n);
            int a=t*u-1;
            if(n%4==1) {
                assert((jacobi(a,n)==-1)==five(t,u,v,4));
                if(prime[n]) assert(jacobi(a,n)==jacobi(u,n)*jacobi(v,n));
            }
            if(!prime[n]) assert(!five(t,u,v,4));
            if(n==131 || n==241) assert(!five(t,u,v,8));
            neg+=jacobi(a,n)==-1;
            ec++;
        }
        int roots=0;
        for(int j=0;j<nv;j++) {
            int v=verts[j],r=root(v,parent),dep=0;
            for(int x=v;parent[x];x=parent[x]) dep++;
            if(dep>maxdepth) {maxdepth=dep; maxdepthn=n;}
            roots+=parent[v]==0;
            if(prime[n] && jacobi(v,n)!=jacobi(r,n)) {
                mixed[r]=n;
                if(r<minroot) minroot=r;
                if(r==1) seedneg=1;
                if(r<=2) seed12neg=1;
            }
        }
        assert(ec==nv-roots);
        assert(ec==check_divisors(n,parent,spf));
        if(prime[n]) {
            primes++;
            if(n%4==1) {
                eligible++; word_count+=ec; negative_edges+=neg;
                int qnr=2; while(jacobi(qnr,n)!=-1) qnr++;
                qnr_parent_hits+=parent[qnr]!=0;
                if(mixed[root(qnr,parent)]!=n) {
                    qnr_fail++;
                    if(nqnr<16) first_qnr[nqnr++]=n;
                }
                allfail+=neg==0;
                if(!seedneg) {
                    seedfail++;
                    if(nfirst<16) first_seed[nfirst++]=n;
                }
                seed12fail+=!seed12neg;
                if(minroot<N+3 && minroot>max_seed_min) {
                    max_seed_min=minroot;max_seed_n=n;
                }
            }
        } else squares++;
        if(n==193 || n==2521 || n==66529 || n==131 || n==241) {
            printf("fixture n=%d edges=%d roots=%d negative=%d seed1=%d seed12=%d minroot=%d\n",
                   n,ec,roots,neg,seedneg,seed12neg,minroot);
        }
        for(int j=0;j<nv;j++) parent[verts[j]]=0;
    }
    printf("N=%d primes_odd=%ld squares=%ld p1mod4=%ld stored_edges=%zu bytes=%zu\n",
           N,primes,squares,eligible,used,capacity*sizeof(*edges));
    printf("p1mod4_edges=%ld negative_edges=%ld five_failures=%ld seed1_failures=%ld seed12_failures=%ld\n",
           word_count,negative_edges,allfail,seedfail,seed12fail);
    printf("first_seed1_failures:");for(int i=0;i<nfirst;i++) printf(" %d",first_seed[i]);puts("");
    printf("max_depth=%d at=%d max_least_mixed_root=%d at=%d\n",maxdepth,maxdepthn,max_seed_min,max_seed_n);
    printf("least_QNR_component_failures=%ld least_QNR_parent_hits=%ld\n",qnr_fail,qnr_parent_hits);
    printf("first_QNR_component_failures:");for(int i=0;i<nqnr;i++) printf(" %d",first_qnr[i]);puts("");
    puts("independent SPF-divisor enumeration agrees at every prime and square");
    free(edges);free(head);free(prime);free(selected);free(parent);free(seen);free(verts);free(spf);free(mixed);
}
