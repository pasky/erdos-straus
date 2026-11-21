/* Opus cross-review: independent re-implementation of the z80 P_K short-shift
   prefix (z80_pshift.c), written without reusing its code.
   usage: z80_xr_pshift r K J [truth]
   Factorisation: full segmented trial sieve by ALL primes <= sqrt(max M)
   (different from the author's cube-root + recorded-big-prime scheme).
   Count per shift e (r !| e): e<=32 -> tau(M^2); else greedy g as specified,
   then for each divisor v of y^2 compute u0 = -M * v^{-1} mod e DIRECTLY by
   multiplying inverses of the primes of y (not the (g/y)(y^2/v) trick);
   charge 2 if u0<=g and u0 | g^2.
   truth mode (small J only): additionally enumerate all genuine P_K tuples
   4abd=N+e, a+b=ce (a,b,c,d units mod r) and the set H={h | M^2, h=-M mod e},
   and assert #distinct centres(e) <= #H(e) <= bound(e) for every e. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>
typedef uint64_t u64; typedef unsigned __int128 u128; typedef uint32_t u32;
static u32 *pr; static size_t npr;
static void primes_upto(u64 L){
  u64 s=1; while((s+1)*(s+1)<=L) s++;
  char *c=calloc(s+1,1); u32 *small=malloc(sizeof(u32)*(s+1)); size_t ns=0;
  for(u64 i=2;i<=s;i++) if(!c[i]){small[ns++]=i; for(u64 j=i*i;j<=s;j+=i)c[j]=1;}
  size_t cap=L/10+1000; if(L>1000) { /* pi(x) < 1.26 x/ln x */ double x=(double)L; double lg=0; u64 t=L; while(t>1){t>>=1;lg+=1;} cap=(size_t)(1.26*x/(lg*0.6931))+1000; }
  pr=malloc(sizeof(u32)*cap); npr=0;
  const u64 B=1<<22; char *seg=malloc(B);
  for(u64 lo=2;lo<=L;lo+=B){ u64 hi=lo+B-1; if(hi>L) hi=L; memset(seg,0,hi-lo+1);
    for(size_t k=0;k<ns;k++){ u64 p=small[k]; if(p*p>hi) break; u64 st=p*p>lo?p*p:((lo+p-1)/p)*p; for(u64 j=st;j<=hi;j+=p) seg[j-lo]=1; }
    for(u64 j=lo;j<=hi;j++) if(!seg[j-lo]){ assert(npr<cap); pr[npr++]=(u32)j; } }
  free(seg); free(c); free(small);
}
#define S (1<<21)
#define MF 16
static u64 res[S], fp[S][MF]; static unsigned char fe[S][MF], nfp[S];
static u64 pmod(u64 b,u64 x,u64 m){u64 t=1%m;b%=m;while(x){if(x&1)t=(u128)t*b%m;b=(u128)b*b%m;x>>=1;}return t;}
static int64_t egcd_inv(int64_t a,int64_t m){int64_t g=m,x=0,x1=1,a1=a%m; if(a1<0)a1+=m; int64_t b=a1; /* invert b mod m */
  int64_t r0=m,r1=b,s0=0,s1=1; while(r1){int64_t q=r0/r1,t=r0-q*r1;r0=r1;r1=t;t=s0-q*s1;s0=s1;s1=t;} (void)g;(void)x;(void)x1; assert(r0==1); return s0<0?s0+m:s0;}
/* globals for enumeration */
static u64 E_, G_, G2_, cnt_; static int ny; static u64 yinv[MF]; static int yex[MF];
static void walk(int i,u64 key){ /* key = -M * v^{-1} mod e */
  if(i==ny){ u64 u0=key?key:E_; if(u0<=G_ && G2_%u0==0) cnt_+=2; return; }
  u64 k=key; for(int j=0;j<=2*yex[i];j++){ walk(i+1,k); k=k*yinv[i]%E_; } }
/* truth enumeration */
static u64 R_, W_; static int nf_; static u64 P_[MF]; static int X_[MF];
static u64 *cent; static size_t ncent, capc; static u64 Mcur;
static void addc(u64 x){ if(ncent==capc){capc=capc?2*capc:1024;cent=realloc(cent,capc*8);} cent[ncent++]=x; }
static int cmpu(const void*a,const void*b){u64 x=*(u64*)a,y=*(u64*)b;return x<y?-1:x>y;}
/* enumerate a|M, b|M/a, d=M/(ab) via exponent vectors */
static int ea[MF], eb[MF];
static void enum_b(int i,u64 a,u64 b){
  if(i==nf_){ u64 d=Mcur/a/b; if((a+b)%E_) return; u64 c=(a+b)/E_; if(a%R_==0||b%R_==0||c%R_==0||d%R_==0) return;
    u64 x=(W_+1-(u64)((u128)4*a%W_*(c%W_)%W_*(d%W_)%W_))%W_; u64 y=(W_+1-(u64)((u128)4*b%W_*(c%W_)%W_*(d%W_)%W_))%W_; addc(x); addc(y); return; }
  u64 bb=b; for(int j=0;j<=X_[i]-ea[i];j++){ enum_b(i+1,a,bb); bb*=P_[i]; } }
static void enum_a(int i,u64 a){
  if(i==nf_){ enum_b(0,a,1); return; }
  u64 aa=a; for(int j=0;j<=X_[i];j++){ ea[i]=j; enum_a(i+1,aa); aa*=P_[i]; } ea[i]=0; }
static u64 hcount; static u64 Mmod;
static void enum_h(int i,u64 hm){ if(i==nf_){ if(hm==(E_-Mmod)%E_) hcount++; return; }
  u64 k=hm; for(int j=0;j<=2*X_[i];j++){ enum_h(i+1,k); k=k*(P_[i]%E_)%E_; } }
int main(int argc,char**argv){
  assert(argc==4||argc==5); u64 r=strtoull(argv[1],0,10); int K=atoi(argv[2]), J=atoi(argv[3]); int truth=argc==5;
  assert(K%2==1 && J>=1 && J<=30 && r>=3);
  u128 N=1; for(int i=0;i<K;i++) N*=r; assert(N/4 < ((u128)1<<63));
  u64 W=1; for(int i=0;i<(K+1)/2;i++) W*=r; R_=r; W_=W;
  u64 first=(u64)((4-(N%4))%4); if(first==0) first=4; /* e = -N mod 4, e>=1 */
  u64 Ecut=(u64)1<<J; u64 num = Ecut>first ? (Ecut-1-first)/4+1 : 0;
  u64 M0=(u64)((N+first)/4); u64 Mmax=M0+num; u64 sq=1; while((u128)(sq+1)*(sq+1)<=Mmax) sq++;
  primes_upto(sq);
  u64 sum=0; int jc=0; u64 tsum=0, hsum=0;
  printf("%lu %d %d",r,K,J);
  for(u64 n0=0;n0<num;n0+=S){ u64 len=num-n0<S?num-n0:S;
    for(u64 i=0;i<len;i++){res[i]=M0+n0+i; nfp[i]=0;}
    u64 base=M0+n0;
    for(size_t k=0;k<npr;k++){ u64 p=pr[k]; u64 st=(p-base%p)%p; for(u64 i=st;i<len;i+=p){ int x=0; while(res[i]%p==0){res[i]/=p;x++;} assert(x>0); int t=nfp[i]++; assert(t<MF); fp[i][t]=p; fe[i][t]=x; } }
    for(u64 i=0;i<len;i++){ if(res[i]>1){ int t=nfp[i]++; assert(t<MF); fp[i][t]=res[i]; fe[i][t]=1; }
      u64 e=first+4*(n0+i), M=M0+n0+i;
      while(jc<=J && ((u64)1<<jc)<=e){ printf(" %lu",sum); jc++; }
      if(e%r==0) continue;
      /* verify factorisation */
      { u128 pr2=1; for(int t=0;t<nfp[i];t++) for(int z=0;z<fe[i][t];z++) pr2*=fp[i][t]; assert(pr2==M); }
      u64 add;
      if(e<=32){ add=1; for(int t=0;t<nfp[i];t++) add*=2*fe[i][t]+1; }
      else { u64 g=1; ny=0; for(int t=0;t<nfp[i];t++){ u64 p=fp[i][t]; int l=fe[i][t]; while(l>0 && p<=e/g){g*=p;l--;} if(l){ yinv[ny]=(u64)egcd_inv((int64_t)(p%e),(int64_t)e); yex[ny]=l; ny++; } }
        E_=e; G_=g; G2_=g*g; cnt_=0; walk(0,(e-M%e)%e); add=cnt_; }
      if(truth){ E_=e; nf_=nfp[i]; for(int t=0;t<nf_;t++){P_[t]=fp[i][t];X_[t]=fe[i][t];} Mcur=M; ncent=0; enum_a(0,1);
        qsort(cent,ncent,8,cmpu); u64 dist=0; for(size_t z=0;z<ncent;z++) if(!z||cent[z]!=cent[z-1]) dist++;
        hcount=0; Mmod=M%e; if(e==1){ hcount=1; for(int t=0;t<nf_;t++) hcount*=2*X_[t]+1; } else enum_h(0,1%e);
        if(!(dist<=hcount && hcount<=add)){ fprintf(stderr,"VIOLATION e=%lu dist=%lu H=%lu bound=%lu\n",e,dist,hcount,add); }
        tsum+=dist; hsum+=hcount; }
      sum+=add; } }
  while(jc<=J){ printf(" %lu",sum); jc++; } printf("\n");
  if(truth) fprintf(stderr,"truth r=%lu K=%d J=%d: sum distinct centres per e=%lu, sum #H=%lu, bound=%lu\n",r,K,J,tsum,hsum,sum);
  (void)pmod; return 0; }
