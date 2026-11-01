/* z53 FORESTCLASS: whole-forest engine for F_n (n odd, n >= 5), with class-group root sets.
 *
 * F_n: vertices 1..n+2, u != v adjacent iff uv | n+u+v.  Colour chi(v) = Jacobi (v/n).
 * Facts used (LOWER_TAIL_ASTRA Lemma 2.1, Z52D_PELLCYCLE Lemmas 1.2-1.3, FOREST_INVERSE Cor C):
 *   - for gcd(x,n)=1, the neighbours of x are exactly v = (n+x)/D, D | n+x, D == -1 (mod x), v != x;
 *   - every edge {u<v} has u(u-1) <= n+1, so all edges are found from small endpoints u <= Us = isqrt(n)+2;
 *   - vertices > Us are leaves (only their parent -n mod v).
 * For composite n (odd squares, controls) vertices sharing a factor with n get colour 0 and are never
 * counted in a bichromatic edge (only unit-endpoint edges are certificates; T1 control).
 *
 * Root sets over a in [1, R] with R = isqrt(n)+1 (all small endpoints):
 *   ALL; SM = {a : -n is a square mod a} (first coefficients of reduced forms of disc -4n, a <= sqrt n);
 *   SP = {a : n is a square mod a} (Q-values of all reduction cycles of disc 4n, PELLCYCLE Prop 2.4);
 *   NR = {a : chi(a) = -1}; SMN = SM ∩ NR (non-principal-genus minima); SQ = perfect squares.
 * For each set: size, #roots whose component is bichromatic (hit), #roots at depth <= 1, <= 2,
 * least hit root a and its rank in the set, least hit root a > 100 and its rank.
 * depth(a) = 1 + graph distance from a to the nearest endpoint of a bichromatic edge (inf if none).
 *
 * Input: one odd n per line on stdin.  Output: one line per n (key=value), plus, with -s FILE, global
 * stratified counts (chi, a mod 8, inSM, inSP, floor(log2 a)) -> (count, nonisolated, inBichromComp).
 * Build: gcc -O2 -o /tmp/z53fc scripts/z53_forestclass_forest.c -lm
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

typedef uint64_t u64; typedef int64_t i64; typedef unsigned __int128 u128;

static u64 isqrt64(u64 n){ u64 r=(u64)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++; return r; }

static int jacobi(u64 a, u64 n){ /* n odd positive */
  int t=1; a%=n; while(a){ while(!(a&1)){ a>>=1; u64 r=n&7; if(r==3||r==5) t=-t; }
    u64 tmp=a; a=n; n=tmp; if((a&3)==3 && (n&3)==3) t=-t; a%=n; }
  return n==1?t:0; }

/* primes */
static uint32_t *primes; static int nprimes;
static void sieve_primes(uint32_t lim){
  char *c=calloc(lim+1,1); nprimes=0; primes=malloc(sizeof(uint32_t)*(lim/2+100));
  for(uint32_t i=2;i<=lim;i++){ if(!c[i]){ primes[nprimes++]=i; for(u64 j=(u64)i*i;j<=lim;j+=i) c[j]=1; } }
  free(c); }

/* smallest prime factor table for root-set membership */
static uint32_t *spf; static uint32_t spflim=0;
static void build_spf(uint32_t lim){
  if(lim<=spflim) return; free(spf); spf=calloc(lim+1,sizeof(uint32_t)); spflim=lim;
  for(uint32_t i=2;i<=lim;i++) if(!spf[i]){ for(u64 j=i;j<=lim;j+=i) if(!spf[j]) spf[j]=i; } }

/* union find over small vertices */
static int32_t *uf;
static int32_t findr(int32_t x){ while(uf[x]!=x){ uf[x]=uf[uf[x]]; x=uf[x]; } return x; }
static void unite(int32_t a,int32_t b){ a=findr(a); b=findr(b); if(a!=b) uf[a]=b; }

typedef struct { u64 u, v; int8_t bi; } edge_t;
static edge_t *edges; static size_t nedges, capedges;
static void add_edge(u64 u,u64 v,int bi){ if(nedges==capedges){ capedges=capedges?2*capedges:1024; edges=realloc(edges,capedges*sizeof(edge_t)); } edges[nedges].u=u; edges[nedges].v=v; edges[nedges].bi=bi; nedges++; }

/* stratified global counts */
#define NB 32
static u64 strat[3][8][2][2][NB][3];
/* genus-count strata: chi, a mod 8, inSM, log2 bucket, genus bucket gb -> count, nonisolated, inBichrom */
#define NG 44
static u64 gstrat[3][8][2][NB][NG][3];
static uint8_t *gbuck; /* per small vertex genus bucket */
/* genus count g(u) = #{d | n+u : d in (-n)G^2 mod u}; mu = g*|X|/phi(u); bucket 0 if g=0 else 1+clamp(floor(2 log2 mu)+20) */
static int genus_bucket(u64 n, u64 u, u64 *pr, int *ex, int k){
  if(u<3) return 1+20;
  u64 x=u; int v2=0; while(!(x&1)){ x>>=1; v2++; }
  uint32_t L[16]; int nl=0; u64 phi=1;
  while(x>1){ u64 l=spf[x]; int e=0; while(x%l==0){ x/=l; e++; } L[nl++]=(uint32_t)l; phi*=(l-1); for(int i=1;i<e;i++) phi*=l; }
  if(v2>=1) phi*= (1ULL<<(v2-1));
  int r=nl+(v2==2?1:0)+(v2>=3?2:0);
  u64 c=(u-(n%u))%u;
  #define BITS(q) ({ unsigned b_=0; for(int i_=0;i_<nl;i_++) if(jacobi((q)%L[i_],L[i_])==-1) b_|=1u<<i_; \
     if(v2==2){ if(((q)&3)==3) b_|=1u<<nl; } if(v2>=3){ if(((q)&3)==3) b_|=1u<<nl; if(((q)&7)==3||((q)&7)==5) b_|=1u<<(nl+1);} b_; })
  unsigned tb=BITS(c);
  static u64 st[1<<12], nw[1<<12]; int S=1<<r; for(int i=0;i<S;i++) st[i]=0; st[0]=1;
  for(int j=0;j<k;j++){ unsigned b=BITS(pr[j]%u); u64 od=(u64)(ex[j]+1)/2, ev=(u64)ex[j]/2+1;
    for(int i=0;i<S;i++) nw[i]=st[i]*ev+st[i^b]*od; for(int i=0;i<S;i++) st[i]=nw[i]; }
  u64 g=st[tb]; if(getenv("Z53DBG")) printf("G %lu %lu %lu %lu\n", n, u, g, phi>>0);
  if(!g) return 0;
  double mu=(double)g*(double)S/(double)phi; int bb=(int)floor(2*log2(mu))+20; if(bb<0) bb=0; if(bb>NG-2) bb=NG-2; return 1+bb;
}


static int ndivlist; static u64 divs[1<<16];
static void gen_divs(u64 *pr, int *ex, int k){
  ndivlist=1; divs[0]=1;
  for(int i=0;i<k;i++){ int cur=ndivlist; u64 m=1; for(int e=1;e<=ex[i];e++){ m*=pr[i]; for(int j=0;j<cur;j++){ if(ndivlist<(1<<16)) divs[ndivlist++]=divs[j]*m; } } }
}

int main(int argc, char **argv){
  const char *stratfile=NULL; int quiet=0;
  for(int i=1;i<argc;i++){ if(!strcmp(argv[i],"-s")&&i+1<argc) stratfile=argv[++i]; else if(!strcmp(argv[i],"-q")) quiet=1; }
  u64 n; uint32_t plim=0;
  while(scanf("%lu",&n)==1){
    if(n<5 || !(n&1)) continue;
    u64 Us=isqrt64(n)+2;
    u64 R=isqrt64(n)+1; /* roots */
    uint32_t need=(uint32_t)isqrt64(n+Us)+2;
    if(need>plim){ free(primes); plim=need*2; sieve_primes(plim); }
    build_spf((uint32_t)Us+2);
    uf=realloc(uf,sizeof(int32_t)*(Us+2)); for(u64 i=0;i<=Us+1;i++) uf[i]=(int32_t)i;
    nedges=0; gbuck=realloc(gbuck,Us+3);
    /* segmented factorisation of n+u, u in [1,Us] */
    const u64 B=1<<16; u64 *rem=malloc(B*sizeof(u64)); uint32_t (*fl)[24]=malloc(B*sizeof(*fl)); uint8_t *fc=malloc(B);
    uint32_t *nmod=malloc(sizeof(uint32_t)*nprimes); int np=0; while(np<nprimes && primes[np]<=need) { nmod[np]=(uint32_t)(n%primes[np]); np++; }
    for(u64 u0=1; u0<=Us; u0+=B){
      u64 u1=u0+B; if(u1>Us+1) u1=Us+1; u64 len=u1-u0;
      for(u64 i=0;i<len;i++){ rem[i]=n+u0+i; fc[i]=0; }
      for(int k=0;k<np;k++){ u64 l=primes[k]; u64 r=(l-nmod[k])%l; /* u ≡ r mod l */
        u64 off=(r+l-(u0%l))%l; for(u64 i=off;i<len;i+=l){ if(fc[i]<24) fl[i][fc[i]++]=(uint32_t)l; } }
      for(u64 i=0;i<len;i++){
        u64 u=u0+i, N=n+u, m=N; u64 pr[32]; int ex[32]; int k=0;
        for(int j=0;j<fc[i];j++){ u64 l=fl[i][j]; int e=0; while(m%l==0){ m/=l; e++; } pr[k]=l; ex[k]=e; k++; }
        if(m>1){ pr[k]=m; ex[k]=1; k++; }
        if(fc[i]>=24){ fprintf(stderr,"too many factors\n"); exit(1); }
        if(u<=R) gbuck[u]=(uint8_t)genus_bucket(n,u,pr,ex,k);
        gen_divs(pr,ex,k);
        if(ndivlist>=(1<<16)){ fprintf(stderr,"too many divisors\n"); exit(1); }
        for(int j=0;j<ndivlist;j++){ u64 D=divs[j]; if(D%u != (u-1)%u) continue; u64 v=N/D; if(v==u) continue;
          if(v<u) continue; /* found from the smaller endpoint */
          /* gcd conditions: need uv | n+u+v; D == -1 mod u and v = N/D gives u | n+v? check exactly */
          u128 s=(u128)n+u+v; if(s % ((u128)u*v)) continue;
          int cu=jacobi(u,n), cv=jacobi(v%n==0?0:v,n); if(v%n==0) cv=0;
          int bi=(cu*cv==-1);
          add_edge(u,v,bi);
          if(v<=Us) unite((int32_t)u,(int32_t)v);
        }
      }
    }
    free(rem); free(fl); free(fc); free(nmod);
    /* component bichrom flags and depth via multi-source BFS on small graph */
    uint8_t *cbi=calloc(Us+2,1); int32_t *dep=malloc(sizeof(int32_t)*(Us+2)); for(u64 i=0;i<=Us+1;i++) dep[i]=INT32_MAX;
    uint8_t *noniso=calloc(Us+2,1);
    /* adjacency (small-small) CSR */
    int32_t *deg=calloc(Us+3,sizeof(int32_t)); size_t nbi=0;
    for(size_t e=0;e<nedges;e++){ noniso[edges[e].u]=1; if(edges[e].v<=Us){ noniso[edges[e].v]=1; deg[edges[e].u]++; deg[edges[e].v]++; } if(edges[e].bi){ nbi++; cbi[findr((int32_t)edges[e].u)]=1; } }
    int32_t *st=malloc(sizeof(int32_t)*(Us+3)); st[0]=0; for(u64 i=0;i<=Us+1;i++) st[i+1]=st[i]+deg[i];
    int32_t *adj=malloc(sizeof(int32_t)*(st[Us+2]+1)); int32_t *pos=malloc(sizeof(int32_t)*(Us+3)); memcpy(pos,st,sizeof(int32_t)*(Us+3));
    for(size_t e=0;e<nedges;e++) if(edges[e].v<=Us){ adj[pos[edges[e].u]++]=(int32_t)edges[e].v; adj[pos[edges[e].v]++]=(int32_t)edges[e].u; }
    int32_t *q=malloc(sizeof(int32_t)*(Us+3)); int qh=0,qt=0;
    for(size_t e=0;e<nedges;e++) if(edges[e].bi){ u64 a=edges[e].u; if(dep[a]>1){ dep[a]=1; q[qt++]=(int32_t)a; } if(edges[e].v<=Us){ u64 b=edges[e].v; if(dep[b]>1){ dep[b]=1; q[qt++]=(int32_t)b; } } }
    while(qh<qt){ int32_t x=q[qh++]; for(int32_t j=st[x];j<st[x+1];j++){ int32_t y=adj[j]; if(dep[y]>dep[x]+1){ dep[y]=dep[x]+1; q[qt++]=y; } } }
    /* root sets */
    enum {ALL,SM,SP,NR,SMN,SQ,NSET}; const char *nm[NSET]={"ALL","SM","SP","NR","SMN","SQ"};
    u64 cnt[NSET]={0}, hit[NSET]={0}, h1[NSET]={0}, h2[NSET]={0}, first[NSET]={0}, frank[NSET]={0}, first100[NSET]={0}, frank100[NSET]={0};
    u64 sqb=1;
    for(u64 a=1;a<=R;a++){
      int c=jacobi(a,n); if(c==0) continue;
      /* membership: SM (-n square mod a), SP (n square mod a) */
      int sm=1, sp=1; u64 x=a; int v2=0; while(!(x&1)){ x>>=1; v2++; }
      if(v2>=2 && ((n+0)%4)!=3) sm=0; /* -n ≡ 3 mod 4 when n ≡ 1 mod 4: not a square mod 4 */
      if(v2>=2 && (n%4)==3) { if(v2>=3 && ((-(i64)(n%8)+8)%8)!=1) sm=0; }
      if(v2>=2 && (n%4)!=1) sp=0;
      if(v2>=3 && (n%8)!=1) sp=0;
      while(x>1){ u64 l=spf[x]; while(x%l==0) x/=l; int lp=jacobi(n%l,l); int lm=jacobi((l-n%l)%l,l); if(lm!=1) sm=0; if(lp!=1) sp=0; }
      int sq=0; while(sqb*sqb<a) sqb++; if(sqb*sqb==a) sq=1;
      int inset[NSET]={1,sm,sp,c==-1,sm&&c==-1,sq};
      int isbi=cbi[findr((int32_t)a)]; int d=dep[a];
      int b=0; { u64 y=a; while(y>1){ y>>=1; b++; } }
      if(b<NB) { u64 *s=strat[c+1][a%8][sm][sp][b]; s[0]++; s[1]+=noniso[a]; s[2]+=isbi; u64 *g=gstrat[c+1][a%8][sm][b][gbuck[a]]; g[0]++; g[1]+=noniso[a]; g[2]+=isbi; }
      for(int k=0;k<NSET;k++) if(inset[k]){ cnt[k]++; if(isbi){ hit[k]++; if(d<=1) h1[k]++; if(d<=2) h2[k]++; if(!first[k]){ first[k]=a; frank[k]=cnt[k]; } if(a>100 && !first100[k]){ first100[k]=a; frank100[k]=cnt[k]; } } }
    }
    if(!quiet){
      printf("n=%lu ndig=%d edges=%zu bi=%zu Us=%lu", n, (int)log10((double)n)+1, nedges, nbi, Us);
      for(int k=0;k<NSET;k++) printf(" %s=%lu/%lu/%lu/%lu f=%lu@%lu f100=%lu@%lu", nm[k], cnt[k], hit[k], h1[k], h2[k], first[k], frank[k], first100[k], frank100[k]);
      printf("\n"); fflush(stdout);
    }
    free(cbi); free(dep); free(noniso); free(deg); free(st); free(adj); free(pos); free(q);
  }
  if(stratfile){ FILE *f=fopen(stratfile,"w"); fprintf(f,"# chi amod8 inSM inSP log2bucket count nonisolated inBichromComp\n");
    for(int c=0;c<3;c++) for(int m=0;m<8;m++) for(int a=0;a<2;a++) for(int b=0;b<2;b++) for(int k=0;k<NB;k++){ u64 *s=strat[c][m][a][b][k]; if(s[0]) fprintf(f,"%d %d %d %d %d %lu %lu %lu\n",c-1,m,a,b,k,s[0],s[1],s[2]); }
    fclose(f);
    char gf[4096]; snprintf(gf,sizeof gf,"%s.genus",stratfile); f=fopen(gf,"w"); fprintf(f,"# chi amod8 inSM log2bucket genusbucket count nonisolated inBichromComp\n");
    for(int c=0;c<3;c++) for(int m=0;m<8;m++) for(int a=0;a<2;a++) for(int k=0;k<NB;k++) for(int g=0;g<NG;g++){ u64 *s=gstrat[c][m][a][k][g]; if(s[0]) fprintf(f,"%d %d %d %d %d %lu %lu %lu\n",c-1,m,a,k,g,s[0],s[1],s[2]); }
    fclose(f); }
  return 0; }
