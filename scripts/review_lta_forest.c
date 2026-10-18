/* R285 from-scratch check of LOWER_TAIL_ASTRA §2–§6 census (reviewer code, independent of z43_astra_*).
 * Usage: review_lta_forest N SCANLIM
 *   N: odd primes and odd squares <= N are processed (edges by divisor enumeration of n+u, u small).
 *   SCANLIM: for odd n <= SCANLIM (primes and squares) the edge set is ALSO rebuilt by the O(n)
 *            residue-parent scan v=2..n+2, r=(-n mod v), and compared edge-by-edge.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

typedef long long ll;
static int *spf;
static void die(const char *m, ll n, ll a, ll b){fprintf(stderr,"FAIL %s n=%lld %lld %lld\n",m,n,a,b);exit(1);}

static int jac(ll a, ll n){ /* Jacobi (a/n), n odd positive */
  int s=1; a%=n; if(a<0)a+=n;
  while(a){ while(!(a&1)){a>>=1; ll r=n&7; if(r==3||r==5)s=-s;}
    ll t=a;a=n;n=t; if((a&3)==3&&(n&3)==3)s=-s; a%=n;}
  return n==1?s:0;
}
static ll gcdl(ll a,ll b){while(b){ll t=a%b;a=b;b=t;}return a;}
static int five(ll t,ll u,ll v,ll k){return t%k==0||u%k==0||v%k==0||(t*u-1)%k==0||(t*v-1)%k==0;}

/* union-find */
static int *uf,*ufstamp; static int curstamp=0;
static int find(int x){ if(ufstamp[x]!=curstamp){ufstamp[x]=curstamp;uf[x]=x;} while(uf[x]!=x){ if(ufstamp[uf[x]]!=curstamp){ufstamp[uf[x]]=curstamp;uf[uf[x]]=uf[x];} uf[x]=uf[uf[x]]; x=uf[x];} return x;}

int main(int argc,char**argv){
  int N=atoi(argv[1]); int SCAN=atoi(argv[2]);
  int M=N+3000;
  spf=calloc(M+1,sizeof(int));
  for(int i=2;i<=M;i++) if(!spf[i]) for(ll j=i;j<=M;j+=i) if(!spf[j]) spf[j]=i;
  uf=malloc((N+5)*sizeof(int)); ufstamp=calloc(N+5,sizeof(int));
  int *par=malloc((N+5)*sizeof(int)); int *parst=calloc(N+5,sizeof(int));
  int *eu=malloc(200000*sizeof(int)),*ev=malloc(200000*sizeof(int));
  char *pos=malloc(N+5),*neg=malloc(N+5); int *mn=malloc((N+5)*sizeof(int)); int *cst=calloc(N+5,sizeof(int));
  int *dep=malloc((N+5)*sizeof(int)); int *depst=calloc(N+5,sizeof(int));
  ll nprim=0,np1=0,nsq=0,edges1=0,neg1=0,root1fail=0,lsmall=0,lfail=0,nofive=0;
  int r1list[20],nr1=0,lflist[20],nlf=0; int maxroot=0,maxrootn=0,maxdep=0,maxdepn=0,maxdepp=0,maxdeppn=0;
  ll scanchecked=0;
  for(int n=3;n<=N;n+=2){
    int isp=(spf[n]==n); int r=(int)(sqrtl((long double)n)+0.5); while((ll)r*r>n)r--; while((ll)(r+1)*(r+1)<=n)r++;
    int issq=((ll)r*r==n);
    if(!isp&&!issq) continue;
    curstamp++;
    int ne=0;
    for(ll u=1;(u-1)*u<=n+1;u++){
      int x=(int)(n+u); int ds[2048]; int nd=1; ds[0]=1;
      while(x>1){int q=spf[x],e=0; while(x%q==0){x/=q;e++;} int old=nd; ll pw=1; for(int k=0;k<e;k++){pw*=q; for(int j=0;j<old;j++){ if(nd>=2048)die("nd",n,0,0); ds[nd++]=(int)(ds[j]*pw);}}}
      for(int j=0;j<nd;j++){ ll v=ds[j]; if(v<=u||v>n+2) continue;
        if((n+u+v)%(u*v)) continue;
        if(ne>=200000) die("ne",n,0,0);
        eu[ne]=(int)u; ev[ne]=(int)v; ne++; }
    }
    /* unique parent & parent formula & forest */
    for(int i=0;i<ne;i++){ int v=ev[i],u=eu[i];
      if(parst[v]==curstamp) die("two parents",n,v,u);
      parst[v]=curstamp; par[v]=u;
      if(u!=(int)(((-(ll)n)%v+v)%v)) die("parent formula",n,u,v);
      int a=find(u),b=find(v); if(a==b) die("cycle",n,u,v); uf[a]=b; }
    /* residue-parent scan cross-check */
    if(n<=SCAN){ int cnt=0;
      for(ll v=2;v<=n+2;v++){ ll rr=((-(ll)n)%v+v)%v; if(rr==0) continue; if((n+v+rr)%(v*rr)) continue; cnt++;
        if(parst[v]!=curstamp||par[v]!=rr) die("scan mismatch",n,v,rr);} 
      if(cnt!=ne) die("scan count",n,cnt,ne); scanchecked++; }
    /* depth: distance to component min via parent chain */
    for(int i=0;i<ne;i++){ int v=ev[i]; int d=0,x=v; while(parst[x]==curstamp){x=par[x];d++;}
      if(d>maxdep){maxdep=d;maxdepn=n;} if(isp&&d>maxdepp){maxdepp=d;maxdeppn=n;} }
    if(issq){ nsq++; for(int i=0;i<ne;i++){ ll u=eu[i],v=ev[i],t=(n+u+v)/(u*v); if(five(t,u,v,4)) die("square five",n,u,v);} continue; }
    nprim++;
    if(n==131||n==241) for(int i=0;i<ne;i++){ ll u=eu[i],v=ev[i],t=(n+u+v)/(u*v); if(five(t,u,v,8)) die("eight",n,u,v); nofive++; }
    for(int i=0;i<ne;i++){ ll u=eu[i],v=ev[i],t=(n+u+v)/(u*v); ll A=t*u-1;
      if(t*u*v-u-v!=n) die("word",n,u,v);
      if(gcdl(u*v,n)!=1) die("nonunit at prime",n,u,v);
      if(jac(A,n)!=jac(u,n)*jac(v,n)) die("sign identity",n,u,v);
      if(jac(t*v-1,n)!=jac(A,n)) die("A*",n,u,v);
      if(n%4==1 && ((jac(A,n)==-1)!=five(t,u,v,4))) die("five-slice",n,u,v); }
    if(n%4!=1) continue;
    np1++; edges1+=ne;
    for(int i=0;i<ne;i++){ if(jac(eu[i],n)!=jac(ev[i],n)) neg1++; }
    /* components */
    for(int i=0;i<ne;i++){ int w[2]={eu[i],ev[i]}; for(int k=0;k<2;k++){int c=find(w[k]); if(cst[c]!=curstamp){cst[c]=curstamp;pos[c]=neg[c]=0;mn[c]=w[k];}
        if(jac(w[k],n)==1)pos[c]=1; else neg[c]=1; if(w[k]<mn[c])mn[c]=w[k];}}
    int c1=find(1); int mixed1=(cst[c1]==curstamp&&pos[c1]&&neg[c1]);
    if(!mixed1){root1fail++; if(nr1<16)r1list[nr1++]=n;}
    int l=2; while(jac(l,n)!=-1) l++;
    if(parst[l]==curstamp) lsmall++;
    int cl=find(l); int mixedl=(cst[cl]==curstamp&&pos[cl]&&neg[cl]);
    if(!mixedl){lfail++; if(nlf<16)lflist[nlf++]=n;}
    int best=N+10; for(int i=0;i<ne;i++){int c=find(eu[i]); if(pos[c]&&neg[c]&&mn[c]<best)best=mn[c];}
    if(best==N+10) die("no mixed component",n,0,0);
    if(best>maxroot){maxroot=best;maxrootn=n;}
  }
  printf("N=%d odd_primes=%lld squares=%lld p1mod4=%lld edges=%lld bichromatic=%lld scanchecked=%lld\n",N,nprim,nsq,np1,edges1,neg1,scanchecked);
  printf("root1_fail=%lld first:",root1fail); for(int i=0;i<nr1;i++)printf(" %d",r1list[i]); printf("\n");
  printf("lnr_smaller_neighbour=%lld lnr_component_fail=%lld first:",lsmall,lfail); for(int i=0;i<nlf;i++)printf(" %d",lflist[i]); printf("\n");
  printf("max_least_mixed_root=%d first_at=%d max_depth_all=%d at=%d max_depth_primes=%d at=%d eight_edges_checked=%lld\n",maxroot,maxrootn,maxdep,maxdepn,maxdepp,maxdeppn,nofive);
  return 0;
}
