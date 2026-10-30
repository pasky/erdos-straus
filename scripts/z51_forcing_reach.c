/* z51 forcing: full Type I/II forcing reach (EXSET_CHAR_FORCING §6).
   For a prime p == 1 (mod 4) and every odd prime q <= QMAX (q != p), a residue r mod q (q !| r) is REACHED if some
   Elsholtz-Tao certificate class whose modulus is exactly divisible by q contains the profinite point
   "p at every modulus prime to q, r at q":
     Type II (a,b,e): e | a+b, class n == -e (mod 4ab)          [x=abd, y=acdn, z=bcdn, c=(a+b)/e, d=(n+e)/(4ab)]
        with a = q*a1 (q !| a1*b*e): need 4*a1*b | p+e and e | q*a1+b; reached r = -e mod q; size 4*q*a1*b <= p.
     Type I  (b,c,e): e | b+c, class n == -e^{-1} (mod 4bc)    [x=n*b*c*k, y=g*b, z=g*c, k=(e n+1)/(4bc), g=k(b+c)/e]
        with b = q*b1: need 4*b1*c | e*p+1 and e | q*b1+c; reached r = -e^{-1} mod q; size 4*q*b1*c <= p
        (class modulus <= p for both types, so that the class has representatives of the size of p; then
        e <= (a+b) <= p/4+1 for both types; E2 = p/4 is exact for Type II, E1 = p/12 truncates a negligible Type I tail).
   (a,b ordered, so q may sit in either coordinate.)  e ranges over e == 3 (mod 4), e <= E2 (Type II), e <= E1 (Type I).
   Factorisations by sieving: p+e with primes <= sqrt(p+E2); e*p+1 with primes <= sqrt(E1*p+1) (residue e == -p^{-1}).
   Output per q: legendre (p/q), #QNR classes, #QNR unreached, #QR unreached, mean hits per QNR class, min hits,
   mean number of distinct productive (type,e) per QNR class (each (type,e) feeds exactly one class mod q).
   Also writes up to W random witnesses (q r type e a1 b) for independent exact checking.
   Usage: z51_forcing_reach p E2 E1 QMAX outfile [W [WRATE]]  (each hit is a witness with prob 1/WRATE) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long long ll; typedef unsigned long long ull; typedef unsigned int u32;
static ll mulmod(ll a, ll b, ll m){ return (ll)((__int128)a*b % m); }
static ll powmod(ll a, ll e, ll m){ ll r=1%m; a%=m; if(a<0)a+=m; while(e){ if(e&1) r=mulmod(r,a,m); a=mulmod(a,a,m); e>>=1;} return r; }
static ll egcd_inv(ll a, ll m){ ll g=m, x=0, x1=1, a1=a%m; if(a1<0)a1+=m; ll b=a1; ll t0=0,t1=1; ll r0=m,r1=b; while(r1){ ll qq=r0/r1, t; t=r0-qq*r1; r0=r1; r1=t; t=t0-qq*t1; t0=t1; t1=t; } (void)g;(void)x;(void)x1; if(r0!=1) return -1; t0%=m; if(t0<0)t0+=m; return t0; }
static ll gcdll(ll a, ll b){ while(b){ ll t=a%b; a=b; b=t;} return a<0?-a:a; }
static int *pr; static int npr;
static int QMAX; static int qlist[4000]; static int nq; static int qidx[100000];
static u32 *hits[4000]; static u32 *hitsE[4000]; static ll stampE[4000]; static ll curstamp=0;
static FILE *wf; static ull WRATE=4096; static ll wcount=0, W=0; static ull rng=88172645463325252ULL;
static ull xr(){ rng^=rng<<13; rng^=rng>>7; rng^=rng<<17; return rng; }
#define MAXF 24
typedef struct { ll p[MAXF]; unsigned char e[MAXF]; int k; } fac_t;
static ll divs[1<<17]; static int nd;
static void gendivs(fac_t *f){ nd=1; divs[0]=1; for(int i=0;i<f->k;i++){ int cur=nd; ll pw=1; for(int j=1;j<=f->e[i];j++){ pw*=f->p[i]; for(int t=0;t<cur;t++){ if(nd<(1<<17)) divs[nd++]=divs[t]*pw; } } } }
/* process one shifted integer M = N/4 with factorisation f; type 2: e, bound P = p (size 4*q*a1*b <= P); type 1: bound = e*p */
static void process(fac_t *f, ll M, ll e, __int128 bound, int type){
  gendivs(f); curstamp++;
  int ndd=nd; static ll D[1<<17]; memcpy(D,divs,sizeof(ll)*ndd);
  for(int i=0;i<ndd;i++){ ll a1=D[i]; ll rest=M/a1;
    for(int j=0;j<ndd;j++){ ll b=D[j]; if(rest%b) continue;
      __int128 base=(__int128)4*a1*b; if(base*3>bound) continue;
      ll g=gcdll(a1,e); if(b%g) continue; ll eg=e/g; ll c;
      if(eg==1) c=0; else { ll inv=egcd_inv((a1/g)%eg,eg); if(inv<0) continue; ll bb=(b/g)%eg; c=(ll)((__int128)(eg-bb)%eg*inv%eg); }
      ll qmaxsz = (ll)(bound/base); if(qmaxsz>QMAX) qmaxsz=QMAX;
      for(ll q=(c?c:eg); q<=qmaxsz; q+=eg){ if(q<3 || q>=100000) continue; int qi=qidx[q]; if(qi<0) continue;
        if(a1%q==0 || b%q==0 || e%q==0) continue;
        ll r; if(type==2){ r=((-e)%q+q)%q; } else { r=(q-powmod(e%q,q-2,q))%q; }
        hits[qi][r]++; if(stampE[qi]!=curstamp){ stampE[qi]=curstamp; hitsE[qi][r]++; }
        if(W && (xr()%WRATE)==0 && wcount<W){ fprintf(wf,"%lld %lld %d %lld %lld %lld\n",q,r,type,e,a1,b); wcount++; }
      }
    }
  }
}
int main(int argc,char**argv){
  if(argc<6){ fprintf(stderr,"usage: p E2 E1 QMAX outfile [W]\n"); return 1; }
  ll p=atoll(argv[1]); ll E2=atoll(argv[2]); ll E1=atoll(argv[3]); QMAX=atoi(argv[4]); const char*out=argv[5]; W=argc>6?atoll(argv[6]):0; if(argc>7) WRATE=atoll(argv[7]);
  ll L1=(ll)sqrtl((long double)E1*p+1)+2, L2=(ll)sqrtl((long double)p+E2)+2; ll LIM=L1>L2?L1:L2; if(LIM<200000) LIM=200000;
  char *comp=calloc(LIM+1,1); pr=malloc(sizeof(int)*(size_t)(LIM/5+1000)); npr=0;
  for(ll i=2;i<=LIM;i++){ if(!comp[i]){ pr[npr++]=(int)i; if(i*i<=LIM) for(ll j=i*i;j<=LIM;j+=i) comp[j]=1; } }
  free(comp);
  for(int i=0;i<100000;i++) qidx[i]=-1; nq=0;
  for(int i=1;i<npr && pr[i]<=QMAX;i++){ if(pr[i]==p) continue; qlist[nq]=pr[i]; qidx[pr[i]]=nq; hits[nq]=calloc(pr[i],sizeof(u32)); hitsE[nq]=calloc(pr[i],sizeof(u32)); stampE[nq]=-1; nq++; }
  char fn[600]; if(W){ snprintf(fn,sizeof fn,"%s.wit",out); wf=fopen(fn,"w"); }
  const ll SEG=1<<20;
  /* Type II: N = p+e, e == 3 mod 4 */
  { ll *rem=malloc(sizeof(ll)*SEG); fac_t *F=malloc(sizeof(fac_t)*SEG);
    for(ll e0=3; e0<=E2; e0+=4*SEG){ ll cnt=0; for(ll t=0;t<SEG && e0+4*t<=E2;t++){ rem[t]=p+e0+4*t; F[t].k=0; cnt++; }
      for(int i=0;i<npr && (ll)pr[i]*pr[i]<=p+E2;i++){ ll l=pr[i];
        /* indices t with l | p+e0+4t */
        if(l==2){ for(ll t=0;t<cnt;t++){ int ex=0; while(rem[t]%2==0){rem[t]/=2;ex++;} if(ex){ F[t].p[F[t].k]=2; F[t].e[F[t].k]=ex; F[t].k++; } } continue; }
        ll r=((-(p+e0))%l+l)%l; ll inv4=powmod(4,l-2,l); ll t0=mulmod(r,inv4,l);
        for(ll t=t0;t<cnt;t+=l){ int ex=0; while(rem[t]%l==0){rem[t]/=l;ex++;} if(ex && F[t].k<MAXF){ F[t].p[F[t].k]=l; F[t].e[F[t].k]=ex; F[t].k++; } } }
      for(ll t=0;t<cnt;t++){ if(rem[t]>1 && F[t].k<MAXF){ F[t].p[F[t].k]=rem[t]; F[t].e[F[t].k]=1; F[t].k++; }
        /* remove factor 4 */ ll e=e0+4*t; ll N=p+e; ll M=N/4; fac_t g=F[t]; for(int i=0;i<g.k;i++) if(g.p[i]==2){ g.e[i]-=2; if(g.e[i]==0){ g.p[i]=g.p[g.k-1]; g.e[i]=g.e[g.k-1]; g.k--; } break; }
        process(&g,M,e,(__int128)p,2); } }
    free(rem); free(F); }
  /* Type I: N = e*p+1, e == 3 mod 4 */
  if(E1>=3){ ll *rem=malloc(sizeof(ll)*SEG); fac_t *F=malloc(sizeof(fac_t)*SEG);
    for(ll e0=3; e0<=E1; e0+=4*SEG){ ll cnt=0; for(ll t=0;t<SEG && e0+4*t<=E1;t++){ rem[t]=(e0+4*t)*p+1; F[t].k=0; cnt++; }
      ll top=(ll)sqrtl((long double)(e0+4*(cnt-1))*p+1)+1;
      for(int i=0;i<npr && pr[i]<=top;i++){ ll l=pr[i];
        if(l==2){ for(ll t=0;t<cnt;t++){ int ex=0; while(rem[t]%2==0){rem[t]/=2;ex++;} if(ex){ F[t].p[F[t].k]=2; F[t].e[F[t].k]=ex; F[t].k++; } } continue; }
        if(p%l==0) continue;
        /* (e0+4t)p+1 == 0 mod l  <=> t == (-p^{-1} - e0) * 4^{-1} */
        ll pinv=powmod(p%l,l-2,l); ll r=((-pinv - e0)%l+l)%l; ll t0=mulmod(r,powmod(4,l-2,l),l);
        for(ll t=t0;t<cnt;t+=l){ int ex=0; while(rem[t]%l==0){rem[t]/=l;ex++;} if(ex && F[t].k<MAXF){ F[t].p[F[t].k]=l; F[t].e[F[t].k]=ex; F[t].k++; } } }
      for(ll t=0;t<cnt;t++){ if(rem[t]>1 && F[t].k<MAXF){ F[t].p[F[t].k]=rem[t]; F[t].e[F[t].k]=1; F[t].k++; }
        ll e=e0+4*t; ll N=e*p+1; ll M=N/4; fac_t g=F[t]; for(int i=0;i<g.k;i++) if(g.p[i]==2){ g.e[i]-=2; if(g.e[i]==0){ g.p[i]=g.p[g.k-1]; g.e[i]=g.e[g.k-1]; g.k--; } break; }
        process(&g,M,e,(__int128)p,1); } }
    free(rem); free(F); }
  FILE *fo=fopen(out,"w");
  fprintf(fo,"# p=%lld E2=%lld E1=%lld QMAX=%d\n# q (p/q) nQNR unreachedQNR unreachedQR meanhitsQNR minhitsQNR mean_distinct_e_QNR\n",p,E2,E1,QMAX);
  int qstar=-1;
  for(int i=0;i<nq;i++){ int q=qlist[i]; int nnr=0,unr=0,unq=0; double sh=0, se=0; u32 mn=0xffffffff;
    for(int r=1;r<q;r++){ int leg=powmod(r,(q-1)/2,q)==1?1:-1; if(leg==-1){ nnr++; sh+=hits[i][r]; se+=hitsE[i][r]; if(hits[i][r]<mn) mn=hits[i][r]; if(!hits[i][r]) unr++; } else { if(!hits[i][r]) unq++; } }
    int lp = powmod(p%q,(q-1)/2,q)==1?1:-1;
    fprintf(fo,"%d %d %d %d %d %.2f %u %.3f\n",q,lp,nnr,unr,unq,sh/nnr,mn,se/nnr);
    if(unr && qstar<0) qstar=q;
    if(q<=61 && unr){ fprintf(fo,"#   q=%d unreached QNR residues:",q); for(int r=1;r<q;r++) if(powmod(r,(q-1)/2,q)!=1 && !hits[i][r]) fprintf(fo," %d",r); fprintf(fo,"  (p mod q = %lld)\n", p%q); } }
  fprintf(fo,"# qstar %d\n",qstar); fclose(fo); if(W) fclose(wf);
  printf("p=%lld qstar=%d\n",p,qstar);
  return 0;
}
