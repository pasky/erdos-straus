/* z48 forestconn: component structure of the word forest F_p.
 *
 * F_p: vertices 1..p+2, u<v adjacent iff uv | p+u+v.  Unique possible smaller neighbour of v is
 * a_v = (-p mod v), an edge iff a_v > 0 and a_v | p+v (gcd(v,p)=1).  Because parents are smaller,
 * the path between x<y in F_p uses only vertices <= y, so the components of F_p restricted to
 * [1,V] are exactly (full components) ∩ [1,V]: one left-to-right pass gives everything.
 *
 * Usage:
 *   range LO HI VCAP   : all primes p == 1 (mod 24), LO <= p <= HI (HI <= 2^31), vertices <= min(VCAP,p+2)
 *   list VCAP          : primes (64-bit) from stdin, one per line ("tag p"), vertices <= min(VCAP,p+2)
 * Output: one CSV row per prime on stdout (in input order), aggregates on stderr.
 * Every edge is also checked: slot(t,u,v) <=> chi(u)chi(v) = -1   (failures are fatal).
 * Build: gcc -O2 -fopenmp -Wall -Wextra -Werror scripts/z48_forestconn_scan.c -lm -o /tmp/z48fc_scan
 */
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>
typedef uint64_t U;
typedef int64_t I;

static U mulm(U a,U b,U m){return (unsigned __int128)a*b%m;}
static U powm(U a,U e,U m){U r=1;a%=m;while(e){if(e&1)r=mulm(r,a,m);a=mulm(a,a,m);e>>=1;}return r;}
static int isprime64(U n){
  static const U sm[]={2,3,5,7,11,13,17,19,23,29,31,37};
  if(n<2)return 0;
  for(int i=0;i<12;i++){if(n==sm[i])return 1;if(n%sm[i]==0)return 0;}
  U d=n-1;int s=0;while(!(d&1)){d>>=1;s++;}
  for(int i=0;i<12;i++){U x=powm(sm[i],d,n);if(x==1||x==n-1)continue;int j;for(j=1;j<s;j++){x=mulm(x,x,n);if(x==n-1)break;}if(j==s)return 0;}
  return 1;
}
static int jacobi(U a,U n){int s=1;a%=n;while(a){while(!(a&1)){a>>=1;U r=n&7;if(r==3||r==5)s=-s;}U t=a;a=n;n=t;if((a&3)==3&&(n&3)==3)s=-s;a%=n;}return n==1?s:0;}

#define NC 6
static const double CS[NC]={0.25,0.5,1.0,2.0,4.0,8.0};
#define DEPTHB 64
#define SIZEB 40

typedef struct {
  U p,N; int full; double L2;
  U r, H4, H4u, H4t, rho, B1, rootr, Br, depthr, depthH4;
  U c1size,c1max,crsize, ncomp,nmixed,K,Ksize,minmixsize,maxdepth,largest,nsingle;
  U Vc[NC], ncompc[NC], nmixc[NC], c1c[NC], largestc[NC], maxdepthc[NC], singlec[NC], c1mixc[NC];
  U edges, negedges;
  char tag[32];
} Row;

typedef struct { int8_t*chi; uint32_t*root; uint8_t*depth; uint32_t*size,*maxv,*firstmix; uint32_t*tmp; U cap; } Work;

static uint32_t*spf; static U spfN;
static U fails=0;
/* aggregates (only for range mode / full forests) */
#define RU 65
static U agg_isroot[RU], agg_mixL2[RU], agg_mixfull[RU], agg_mixL2any[RU];
static U agg_depth[DEPTHB], agg_size_full[SIZEB], agg_size_L2[SIZEB], agg_depth_L2[DEPTHB];

static void alloc_work(Work*w,U N){
  if(w->cap>=N)return;
  free(w->chi);free(w->root);free(w->depth);free(w->size);free(w->maxv);free(w->firstmix);free(w->tmp);
  w->cap=N;
  w->chi=malloc(N+1);w->root=malloc(4*(N+1));w->depth=malloc(N+1);
  w->size=malloc(4*(N+1));w->maxv=malloc(4*(N+1));w->firstmix=malloc(4*(N+1));w->tmp=malloc(4*(N+1));
  if(!w->chi||!w->root||!w->depth||!w->size||!w->maxv||!w->firstmix||!w->tmp){fprintf(stderr,"OOM N=%lu\n",(unsigned long)N);exit(3);}
}
static int lg2(U x){int b=0;while(x>1){x>>=1;b++;}return b;}

static void analyze(U p,U VCAP,Work*w,Row*R,int doagg){
  memset(R->Vc,0,sizeof(U)*NC*8);
  U N = (VCAP < p+2) ? VCAP : p+2;
  R->p=p;R->N=N;R->full=(N==p+2);R->L2=log((double)p)*log((double)p);
  alloc_work(w,N);
  int8_t*chi=w->chi;uint32_t*root=w->root,*size=w->size,*maxv=w->maxv,*fm=w->firstmix;uint8_t*dep=w->depth;
  /* colours */
  if(N>spfN){fprintf(stderr,"spf table too small\n");exit(3);}
  chi[1]=1; R->r=0;
  for(U v=2;v<=N;v++){
    if(v>=p){chi[v]=(v==p)?0:chi[v-p];continue;}
    U q=spf[v];
    if(q==v) chi[v]=(v==2)?((p%8==1||p%8==7)?1:-1):(int8_t)jacobi(p%v,v); /* p==1 mod 4: (v/p)=(p/v) */
    else chi[v]=chi[q]*chi[v/q];
    if(!R->r&&chi[v]==-1)R->r=v;
  }
  /* pass */
  U Vc[NC]; for(int c=0;c<NC;c++){Vc[c]=(U)floor(CS[c]*R->L2); R->Vc[c]=Vc[c];}
  root[1]=1;dep[1]=0;size[1]=1;maxv[1]=1;fm[1]=0;
  U ncomp=1,nmixed=0,nsingle=1,largest=1,maxdepth=0,edges=0,neg=0;
  R->H4=R->H4u=R->H4t=R->rho=0;
  int ci=0; while(ci<NC&&Vc[ci]<2){R->ncompc[ci]=0;ci++;} /* too small: marked unavailable */
  for(U v=2;v<=N;v++){
    U a=(v-p%v)%v; int has=0; U t=0;
    if(a&&v!=p&&(p+v)%a==0){has=1;t=(U)(((unsigned __int128)p+a+v)/((unsigned __int128)a*v));}
    if(has){
      U rho=root[a]; root[v]=rho; dep[v]=dep[a]+1; if(dep[v]>maxdepth)maxdepth=dep[v];
      if(size[rho]==1)nsingle--;
      size[rho]++; maxv[rho]=v; if(size[rho]>largest)largest=size[rho];
      int s=chi[a]*chi[v];
      int sl=(t%4==0)||(a%4==0)||(v%4==0)||((t%4)*(a%4)%4==1)||((t%4)*(v%4)%4==1);
      edges++; if(s==-1)neg++;
      if((s==-1)!=sl){
        #pragma omp critical
        {fails++;fprintf(stderr,"SLOT FAIL p=%lu u=%lu v=%lu t=%lu s=%d slot=%d\n",(unsigned long)p,(unsigned long)a,(unsigned long)v,(unsigned long)t,s,sl);}
      }
      if(!fm[rho]&&chi[v]!=chi[rho]&&chi[v]!=0){
        fm[rho]=v; nmixed++;
        if(!R->H4){R->H4=v;R->H4u=a;R->H4t=t;R->rho=rho;R->depthH4=dep[v];}
      }
    } else {
      root[v]=v;dep[v]=0;size[v]=1;maxv[v]=v;fm[v]=0;ncomp++;nsingle++;
    }
    while(ci<NC&&Vc[ci]==v){
      R->ncompc[ci]=ncomp;R->nmixc[ci]=nmixed;R->c1c[ci]=size[1];R->largestc[ci]=largest;
      R->maxdepthc[ci]=maxdepth;R->singlec[ci]=nsingle;R->c1mixc[ci]=(fm[1]!=0);ci++;
    }
  }
  for(;ci<NC;ci++){R->ncompc[ci]=0;} /* V_c > N: not computed (marked by ncomp=0) */
  R->edges=edges;R->negedges=neg;R->ncomp=ncomp;R->nmixed=nmixed;R->nsingle=nsingle;R->largest=largest;R->maxdepth=maxdepth;
  R->B1=fm[1];R->c1size=size[1];R->c1max=maxv[1];
  if(R->r&&R->r<=N){U rr=R->r;R->rootr=root[rr];R->Br=(root[rr]<rr)?root[rr]:fm[rr];R->crsize=size[root[rr]];R->depthr=dep[rr];}
  else {R->rootr=R->Br=R->crsize=R->depthr=0;}
  /* smallest bichromatic component: minimal max-vertex, and minimal size */
  R->K=0;R->Ksize=0;R->minmixsize=0;
  for(U v=1;v<=N;v++) if(root[v]==v&&fm[v]){
    if(!R->K||maxv[v]<R->K){R->K=maxv[v];R->Ksize=size[v];}
    if(!R->minmixsize||size[v]<R->minmixsize)R->minmixsize=size[v];
  }
  if(doagg){
    U ld[DEPTHB]={0},ls[SIZEB]={0},ldl[DEPTHB]={0},lsl[SIZEB]={0};
    for(U v=1;v<=N;v++){ld[dep[v]<DEPTHB?dep[v]:DEPTHB-1]++; if(root[v]==v)ls[lg2(size[v])]++;}
    U V1=Vc[2]<N?Vc[2]:N; uint32_t*cnt=w->tmp;
    for(U v=1;v<=V1;v++)cnt[v]=0;
    for(U v=1;v<=V1;v++){cnt[root[v]]++;ldl[dep[v]<DEPTHB?dep[v]:DEPTHB-1]++;}
    for(U v=1;v<=V1;v++)if(root[v]==v)lsl[lg2(cnt[v])]++;
    U lr[RU]={0},lm[RU]={0},lf[RU]={0},la[RU]={0};
    for(U u=1;u<RU&&u<=N;u++){
      if(root[u]==u){lr[u]=1; if(fm[u]){lf[u]=1; if(fm[u]<=Vc[2])lm[u]=1;}}
      { U rho=root[u]; if(fm[rho]&&fm[rho]<=Vc[2]&&u<=Vc[2])la[u]=1; }
    }
    #pragma omp critical
    {for(int i=0;i<RU;i++){agg_isroot[i]+=lr[i];agg_mixL2[i]+=lm[i];agg_mixfull[i]+=lf[i];agg_mixL2any[i]+=la[i];}
     for(int i=0;i<DEPTHB;i++){agg_depth[i]+=ld[i];agg_depth_L2[i]+=ldl[i];}for(int i=0;i<SIZEB;i++){agg_size_full[i]+=ls[i];agg_size_L2[i]+=lsl[i];}}
  }
}

static void header(void){
  printf("tag,p,N,full,L2,r,H4,H4u,H4t,rho,depthH4,B1,rootr,Br,depthr,c1size,c1max,crsize,ncomp,nmixed,K,Ksize,minmixsize,maxdepth,largest,nsingle,edges,negedges");
  for(int c=0;c<NC;c++)printf(",V%g,ncomp%g,nmix%g,c1size%g,c1mix%g,largest%g,maxdepth%g,nsingle%g",CS[c],CS[c],CS[c],CS[c],CS[c],CS[c],CS[c],CS[c]);
  printf("\n");
}
static void emit(const Row*R){
  printf("%s,%lu,%lu,%d,%.4f,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu",R->tag,
    (unsigned long)R->p,(unsigned long)R->N,R->full,R->L2,(unsigned long)R->r,(unsigned long)R->H4,(unsigned long)R->H4u,(unsigned long)R->H4t,(unsigned long)R->rho,(unsigned long)R->depthH4,
    (unsigned long)R->B1,(unsigned long)R->rootr,(unsigned long)R->Br,(unsigned long)R->depthr,(unsigned long)R->c1size,(unsigned long)R->c1max,(unsigned long)R->crsize,
    (unsigned long)R->ncomp,(unsigned long)R->nmixed,(unsigned long)R->K,(unsigned long)R->Ksize,(unsigned long)R->minmixsize,(unsigned long)R->maxdepth,(unsigned long)R->largest,(unsigned long)R->nsingle,
    (unsigned long)R->edges,(unsigned long)R->negedges);
  for(int c=0;c<NC;c++)printf(",%lu,%lu,%lu,%lu,%lu,%lu,%lu,%lu",(unsigned long)R->Vc[c],(unsigned long)R->ncompc[c],(unsigned long)R->nmixc[c],(unsigned long)R->c1c[c],(unsigned long)R->c1mixc[c],(unsigned long)R->largestc[c],(unsigned long)R->maxdepthc[c],(unsigned long)R->singlec[c]);
  printf("\n");
}
static void build_spf(U N){
  spfN=N; spf=calloc(N+1,4); if(!spf){fprintf(stderr,"OOM spf\n");exit(3);}
  for(U i=2;i<=N;i++) if(!spf[i]){ for(U j=i;j<=N;j+=i) if(!spf[j]) spf[j]=(uint32_t)i; }
}
int main(int argc,char**argv){
  if(argc==5&&!strcmp(argv[1],"range")){
    U LO=strtoull(argv[2],0,10),HI=strtoull(argv[3],0,10),VCAP=strtoull(argv[4],0,10);
    if(HI>(1ULL<<31)){fprintf(stderr,"HI too big\n");return 2;}
    U NN=(VCAP<HI+2)?VCAP:HI+2; build_spf(NN);
    /* primes == 1 mod 24 via spf (needs HI <= NN) or MR */
    U cnt=0; U*ps=malloc(sizeof(U)*(HI/24+2));
    for(U p=(LO<=1?25:LO+((25-LO%24)%24));p<=HI;p+=24){ if((p<=NN)?spf[p]==p:isprime64(p)) ps[cnt++]=p; }
    Row*rows=calloc(cnt,sizeof(Row));
    #pragma omp parallel
    { Work w={0};
      #pragma omp for schedule(dynamic,1)
      for(U i=0;i<cnt;i++){ U ii=cnt-1-i; /* large first */ strcpy(rows[ii].tag,"range"); analyze(ps[ii],VCAP,&w,&rows[ii],1); }
    }
    header(); for(U i=0;i<cnt;i++)emit(&rows[i]);
    fprintf(stderr,"range LO=%lu HI=%lu VCAP=%lu primes=%lu slot_failures=%lu\n",(unsigned long)LO,(unsigned long)HI,(unsigned long)VCAP,(unsigned long)cnt,(unsigned long)fails);
    U te=0,tn=0; for(U i=0;i<cnt;i++){te+=rows[i].edges;tn+=rows[i].negedges;}
    fprintf(stderr,"edges_checked=%lu negative=%lu\n",(unsigned long)te,(unsigned long)tn);
    fprintf(stderr,"depth_hist_all_vertices(N):");for(int i=0;i<DEPTHB;i++)if(agg_depth[i])fprintf(stderr," %d:%lu",i,(unsigned long)agg_depth[i]);fprintf(stderr,"\n");
    fprintf(stderr,"depth_hist_vertices<=L2:");for(int i=0;i<DEPTHB;i++)if(agg_depth_L2[i])fprintf(stderr," %d:%lu",i,(unsigned long)agg_depth_L2[i]);fprintf(stderr,"\n");
    fprintf(stderr,"compsize_log2_hist(N):");for(int i=0;i<SIZEB;i++)if(agg_size_full[i])fprintf(stderr," %d:%lu",i,(unsigned long)agg_size_full[i]);fprintf(stderr,"\n");
    fprintf(stderr,"compsize_log2_hist(<=L2):");for(int i=0;i<SIZEB;i++)if(agg_size_L2[i])fprintf(stderr," %d:%lu",i,(unsigned long)agg_size_L2[i]);fprintf(stderr,"\n");
    fprintf(stderr,"per-small-vertex u: is_root / root&comp(u) bichromatic within log^2p / root&comp bichromatic in F_p|N / comp containing u bichromatic within log^2p (u<=log^2p)\n");
    for(int u=1;u<RU;u++)fprintf(stderr,"u=%d %lu %lu %lu %lu\n",u,(unsigned long)agg_isroot[u],(unsigned long)agg_mixL2[u],(unsigned long)agg_mixfull[u],(unsigned long)agg_mixL2any[u]);
    return fails?1:0;
  }
  if(argc==3&&!strcmp(argv[1],"list")){
    U VCAP=strtoull(argv[2],0,10);
    char tag[32]; unsigned long long pp; U cnt=0,capn=1024; U*ps=malloc(8*capn); char(*tags)[32]=malloc(32*capn);
    while(scanf("%31s %llu",tag,&pp)==2){
      if(pp%4!=1||!isprime64(pp)){fprintf(stderr,"skip non-prime or p!=1 mod 4: %llu\n",pp);continue;}
      if(cnt==capn){capn*=2;ps=realloc(ps,8*capn);tags=realloc(tags,32*capn);}
      ps[cnt]=pp; snprintf(tags[cnt],32,"%s",tag); cnt++;
    }
    build_spf(VCAP+2);
    Row*rows=calloc(cnt,sizeof(Row));
    #pragma omp parallel
    { Work w={0};
      #pragma omp for schedule(dynamic,1)
      for(U i=0;i<cnt;i++){ strcpy(rows[i].tag,tags[i]); analyze(ps[i],VCAP,&w,&rows[i],0); }
    }
    header(); for(U i=0;i<cnt;i++)emit(&rows[i]);
    fprintf(stderr,"list VCAP=%lu primes=%lu slot_failures=%lu\n",(unsigned long)VCAP,(unsigned long)cnt,(unsigned long)fails);
    return fails?1:0;
  }
  fprintf(stderr,"usage: range LO HI VCAP | list VCAP < primes\n"); return 2;
}
