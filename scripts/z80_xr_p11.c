/* Opus cross-review of R17_WALK: independent re-implementation of the P11 short-shift
   split bound of z80_fullprefix.c (NOT the author's code path).
   usage: z80_xr_p11 r idx J [truth]
   Same window convention as the author: e = e0 + 4*i, e0 in {1,3} with e0 = -N mod 4, N = r^11,
   window idx covers i in [idx*2^28, min((idx+1)*2^28, #{e<2^J})).
   Bound per unit shift e (r does not divide e):
     e<=32: tau(M^2);  else greedy split M=g*y (ascending primes, take each copy while g*p<=e),
     count 2*#{(u,v): v|y^2, u|g^2, u<=g, u*v == -M (mod e)}.
   Differences from the author's engine: (1) the large-prime sieve keeps the SMALLEST prime in
   (Y,sqrt(max M)] rather than the last writer; (2) M is recomputed as (N+e)/4 directly;
   (3) the count is organised by u: residues of all v|y^2 are sorted and, for each admissible
   u|g^2 with u<=g, the class -M/u is located by binary search (author walks M/v residues);
   (4) each cofactor q = x/P is checked to be 1 or >= P (smallest-prime invariant) and the
   unrecorded cofactor x is checked to be < Y^2 or to have no recorded divisor (consistency).
   truth mode (small J only): for every e enumerate all divisors h of M^2 with h == -M mod e and
   all unit tuples (a<=b, abd=M, e|a+b, r∤abcde), assert #centres <= #H_e <= bound.
*/
#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef uint64_t u64; typedef unsigned __int128 u128;
#define WIN (1ULL<<28)
#define BLK (1<<16)
#define SEG (1<<21)
static u64 *sp; static int nsp;           /* small primes <= Y */
static u64 *lp;                            /* smallest large prime per position */
static u128 Mx[BLK]; static u64 fp[BLK][24]; static int fk[BLK][24], fn[BLK];
static u128 big_sentinel_res[BLK];
static int cmpu(const void*a,const void*b){u64 x=*(u64*)a,y=*(u64*)b;return x<y?-1:x>y;}
static u64 inv(u64 a,u64 m){ /* a unit mod m */
  __int128 t=0,nt=1,rr=m,nr=a%m; while(nr){__int128 q=rr/nr,z=t-q*nt;t=nt;nt=z;z=rr-q*nr;rr=nr;nr=z;} assert(rr==1); if(t<0)t+=m; return (u64)t;}
static u64 *vres; static size_t vcap;
static int truth;
static u64 count_bound(int i,u64 e,u128 M){
  int n=fn[i];
  if(e<=32){u64 c=1;for(int j=0;j<n;j++)c*=2*fk[i][j]+1;return c;}
  /* ascending order already (insertion is ascending): verify */
  for(int j=1;j<n;j++)assert(fp[i][j]>fp[i][j-1]);
  u64 g=1; u64 lpv[24]; int lk[24], nl=0;
  for(int j=0;j<n;j++){u64 p=fp[i][j];int k=fk[i][j];
    while(k && p!=UINT64_MAX && (u128)g*p<=e){g*=p;k--;}
    if(k){lpv[nl]=(p==UINT64_MAX)?(u64)(big_sentinel_res[i]%e):p%e;lk[nl++]=k;}}
  /* residues of all v | y^2 */
  size_t nv=1; for(int j=0;j<nl;j++)nv*=(2*lk[j]+1);
  if(nv>vcap){vcap=nv*2;vres=realloc(vres,vcap*sizeof(u64));assert(vres);}
  vres[0]=1%e; size_t cur=1;
  for(int j=0;j<nl;j++){size_t base=cur;u64 pw=1;for(int t=1;t<=2*lk[j];t++){pw=(u128)pw*lpv[j]%e;for(size_t s=0;s<base;s++)vres[cur++]=(u128)vres[s]*pw%e;}}
  assert(cur==nv); qsort(vres,nv,sizeof(u64),cmpu);
  /* admissible u: divisors of g^2 with u<=g. Enumerate divisors of g^2 from the funded primes */
  u64 gp[24];int gk[24],ng=0;{u64 x=g;for(int j=0;j<n&&x>1;j++){u64 p=fp[i][j];if(p==UINT64_MAX)break;int k=0;while(x%p==0){x/=p;k++;}if(k){gp[ng]=p;gk[ng++]=2*k;}}assert(x==1);}
  static u64 us[1<<17];int nu=1;us[0]=1;
  for(int j=0;j<ng;j++){int b=nu;u128 pw=1;for(int t=1;t<=gk[j];t++){pw*=gp[j];if(pw>g)break;for(int s=0;s<b;s++){u128 z=(u128)us[s]*pw;if(z<=g){assert(nu<(1<<17));us[nu++]=(u64)z;}}}}
  u64 Me=(u64)(M%e),ct=0;
  /* batch inversion of all u mod e (Montgomery trick) */
  static u64 pre[(1<<17)+1],ui[1<<17]; pre[0]=1%e; for(int s=0;s<nu;s++)pre[s+1]=(u128)pre[s]*(us[s]%e)%e;
  u64 iv=inv(pre[nu],e); for(int s=nu-1;s>=0;s--){ui[s]=(u128)iv*pre[s]%e; iv=(u128)iv*(us[s]%e)%e;}
  for(int s=0;s<nu;s++){u64 u=us[s]; /* need v == -M * u^{-1} */
    assert((u128)ui[s]*(u%e)%e==1%e);
    u64 target=(u128)(e-Me)*ui[s]%e;
    /* count occurrences of target in sorted vres */
    size_t lo=0,hi=nv;while(lo<hi){size_t m=(lo+hi)/2;if(vres[m]<target)lo=m+1;else hi=m;}
    while(lo<nv&&vres[lo]==target){ct+=2;lo++;}}
  return ct;
}
/* truth: all divisors of M^2, from the full factorisation (requires all primes < 2^64) */
static u64 truth_check(int i,u64 e,u128 M,u64 r,u64 bound){
  int n=fn[i]; for(int j=0;j<n;j++)if(fp[i][j]==UINT64_MAX)return 0;
  static u128 dv[1<<22];size_t nd=1;dv[0]=1;
  /* divisors of M^2 that are <= M (pruned, no overflow); partners M^2/h handled by residues */
  for(int j=0;j<n;j++){size_t b=nd;u128 pw=1;for(int t=1;t<=2*fk[i][j];t++){if(pw>M/fp[i][j])break;pw*=fp[i][j];for(size_t s=0;s<b;s++){if(dv[s]>M/pw)continue;assert(nd<(1<<22));dv[nd++]=dv[s]*pw;}}}
  u128 M2r=(u128)((e-(u64)(M%e))%e); u64 H=0; u64 Me=(u64)(M%e),M2e=(u128)Me*Me%e;
  for(size_t s=0;s<nd;s++){u128 h=dv[s];if(h%e==M2r)H++; if(h<M){u64 hp=(u128)M2e*inv((u64)(h%e),e)%e; if(hp==M2r)H++;}}
  /* genuine tuples: a<=b, d=M/(ab) */
  u64 cen=0,nh=0; static u128 hs[4096]; static u128 dm[1<<22];size_t nm=0;for(size_t s=0;s<nd;s++)if(M%dv[s]==0)dm[nm++]=dv[s];
  for(size_t s=0;s<nm;s++){u128 a=dm[s];u128 R=M/a;
    for(size_t t=0;t<nm;t++){u128 b=dm[t];if(b<a||R%b)continue;u128 d=R/b;
      if((a+b)%e)continue;
      u128 c=(a+b)/e;
      if(a%r==0||b%r==0||d%r==0||c%r==0||e%r==0)continue;
      u128 h1=a*a*d; u64 be=(u64)(b%e),de=(u64)(d%e); assert(h1<=M && h1%e==M2r%e && (u128)be*be%e*de%e==M2r%e);
      /* h2=b^2 d=M^2/h1 is keyed as (h1,1) to avoid 256-bit products */
      u128 k1=h1<<1,k2=(h1<<1)|1; int f1=0,f2=0;for(u64 z=0;z<nh;z++){if(hs[z]==k1)f1=1;if(hs[z]==k2)f2=1;}
      if(!f1){assert(nh<4096);hs[nh++]=k1;} if(!f2&&a!=b){assert(nh<4096);hs[nh++]=k2;}}}
  cen=nh;
  if(!(cen<=H&&H<=bound)){fprintf(stderr,"TRUTH FAIL e=%lu cen=%lu H=%lu bound=%lu\n",e,cen,H,bound);exit(3);}
  return cen;
}
int main(int argc,char**argv){
  assert(argc>=4);u64 r=atoll(argv[1]),idx=atoll(argv[2]);int J=atoi(argv[3]);truth=argc>4;
  assert(r>=13&&r<=97&&J>=12&&J<=32);
  u128 N=1;for(int j=0;j<11;j++)N*=r;
  u64 e0=(u64)((4-(unsigned)(N%4))%4);assert(e0==1||e0==3);
  u64 tot=((1ULL<<J)-e0+3)/4; u64 off=idx*WIN; assert(off<tot); u64 size=tot-off; if(size>WIN)size=WIN;
  u128 Mlo=(N+e0+4*off)/4, Mhi=(N+e0+4*(off+size-1))/4;
  /* Y: least integer with Y^3 > Mhi */
  u64 Y=1; while((u128)Y*Y*Y<=Mhi)Y++;
  u64 L=(u64)1<<36; {u64 lo=0,hi=L;while(hi-lo>1){u64 m=(lo+hi)/2;if((u128)m*m<=Mhi)lo=m;else hi=m;}L=lo;} /* floor sqrt */
  /* small primes <= max(Y, sqrt L) */
  u64 S=Y; unsigned char *c=calloc(S+1,1); sp=malloc(sizeof(u64)*(S/2+10));
  for(u64 p=2;p<=S;p++)if(!c[p]){sp[nsp++]=p;for(u64 q=p*p;q<=S;q+=p)c[q]=1;}
  free(c);
  lp=calloc(size,sizeof(u64));assert(lp);
  unsigned char *seg=malloc(SEG);
  for(u64 s=Y+1;s<=L;s+=SEG){u64 n=(L-s+1<SEG)?L-s+1:SEG;memset(seg,0,n);
    for(int j=0;j<nsp;j++){u64 p=sp[j];if(p*p>s+n-1)break;u64 a=(s%p)?p-s%p:0;for(;a<n;a+=p)seg[a]=1;}
    for(u64 a=0;a<n;a++)if(!seg[a]){u64 P=s+a; u64 i0=(u64)((P-(u64)(Mlo%P))%P);
      for(u64 i=i0;i<size;i+=P)if(!lp[i])lp[i]=P;}}
  free(seg);
  u64 total=0,cen=0;
  for(u64 b0=0;b0<size;b0+=BLK){int n=(size-b0<BLK)?size-b0:BLK;
    for(int i=0;i<n;i++){Mx[i]=Mlo+b0+i;fn[i]=0;}
    for(int j=0;j<nsp;j++){u64 p=sp[j];u64 i0=(u64)((p-(u64)((Mlo+b0)%p))%p);
      for(u64 i=i0;i<(u64)n;i+=p){int k=0;while(Mx[i]%p==0){Mx[i]/=p;k++;}assert(k>0);fp[i][fn[i]]=p;fk[i][fn[i]++]=k;assert(fn[i]<22);}}
    for(int i=0;i<n;i++){u64 e=e0+4*(off+b0+i); u128 M=(N+e)/4; assert(M==Mlo+b0+i && (N+e)%4==0);
      u128 x=Mx[i]; u64 P=lp[b0+i];
      if(P){assert(x%P==0);u128 q=x/P;assert(q==1||q>=P);assert(q<((u128)1<<64));
        if(q==P){fp[i][fn[i]]=P;fk[i][fn[i]++]=2;}
        else{fp[i][fn[i]]=P;fk[i][fn[i]++]=1;if(q>1){fp[i][fn[i]]=(u64)q;fk[i][fn[i]++]=1;}}}
      else if(x>1){ /* x has no prime factor <= L, hence prime */
        if(x>=((u128)1<<64)-1){fp[i][fn[i]]=UINT64_MAX;fk[i][fn[i]++]=1;big_sentinel_res[i]=x;}
        else{fp[i][fn[i]]=(u64)x;fk[i][fn[i]++]=1;}}
      if(e%r==0)continue;
      u64 bnd=count_bound(i,e,M); total+=bnd;
      if(truth)cen+=truth_check(i,e,M,r,bnd);
    }}
  printf("%lu %d %lu %lu %lu",r,J,off,size,total);if(truth)printf(" truth_centres %lu",cen);printf("\n");
  free(lp);return 0;}
