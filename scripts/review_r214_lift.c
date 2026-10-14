/* R214 from-scratch check of TWO_FIBRES Thm A (iii),(iv) and Thm B.
 * Independent of the author's y1_* code.
 *
 * Words: w=(t,u,v) >= 1 with n = t*u*v - u - v (n odd). A = tu-1, A* = tv-1, A*A = tn+1.
 * Diff(T_w): ramification (finite primes) of the quaternion algebra (-A*, -t n A*) computed by
 * Hilbert symbols from scratch (not by the author's formula).
 *
 * modes:
 *   iii  N1 N2        : all odd n in [N1,N2]: compare  "exists x,y in Z^3 |x|^2=A*,|y|^2=A, x.y=1"  with Diff=={2}
 *                       also count lifts admitting x × y ≡ ±(x+y) (mod t) (orientation fixed by O(3) reflection)
 *   iiip P1 P2        : same, primes only
 *   iv   N1 N2        : n*G_w Gram in Z^3 (direct search a,b,c) vs Diff=={2}
 *   B    M1 M2        : odd m in [M1,M2], n=m^2: G_w itself Gram in Z^3 (index-m sublattice)
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long long ll;

static ll isqrt_ll(ll x){ if(x<0) return -1; ll r=(ll)sqrtl((long double)x); while(r*r>x) r--; while((r+1)*(r+1)<=x) r++; return r; }
static int is_prime(ll n){ if(n<2) return 0; for(ll d=2;d*d<=n;d++) if(n%d==0) return 0; return 1; }

/* Legendre symbol (a/p), p odd prime */
static int legendre(ll a, ll p){ a%=p; if(a<0)a+=p; if(a==0) return 0; ll r=1,b=a,e=(p-1)/2; while(e){ if(e&1) r=(__int128)r*b%p; b=(__int128)b*b%p; e>>=1;} return r==1?1:-1; }

/* Hilbert symbol (a,b)_p for nonzero integers a,b, p prime */
static int hilbert(ll a, ll b, ll p){
  int al=0,be=0; while(a%p==0){a/=p;al++;} while(b%p==0){b/=p;be++;}
  if(p!=2){
    int s=1; if((al*be)%2 && ((p-1)/2)%2) s=-s;
    if(be%2) s*=legendre(a,p);
    if(al%2) s*=legendre(b,p);
    return s;
  } else {
    ll u=((a%8)+8)%8, v=((b%8)+8)%8;
    int eu=((u-1)/2)%2, ev=((v-1)/2)%2;
    int wu=((u*u-1)/8)%2, wv=((v*v-1)/8)%2;
    int e=(eu*ev + al*wv + be*wu)%2; return e?-1:1;
  }
}
/* Diff == {2} ? returns 1 if ramified exactly at {2}; also returns whether ramified at 2 */
static int diff_is_2(ll t, ll n, ll As){
  ll a=-As, b=-(t*n*As);
  /* primes dividing 2*A* * t * n */
  ll cand[64]; int nc=0; cand[nc++]=2;
  ll xs[3]={As,t,n};
  for(int k=0;k<3;k++){ ll x=xs[k]; for(ll d=2; d*d<=x; d++) if(x%d==0){ int dup=0; for(int j=0;j<nc;j++) if(cand[j]==d) dup=1; if(!dup) cand[nc++]=d; while(x%d==0) x/=d; }
    if(x>1){ int dup=0; for(int j=0;j<nc;j++) if(cand[j]==x) dup=1; if(!dup) cand[nc++]=x; } }
  int ram2=0, ramodd=0;
  for(int j=0;j<nc;j++){ int h=hilbert(a,b,cand[j]); if(h==-1){ if(cand[j]==2) ram2=1; else ramodd=1; } }
  return ram2 && !ramodd;
}

/* enumerate y in Z^3 with x.y = k, |y|^2 = M; x has x[2] > 0. callback returns 1 to stop. */
typedef int (*cb_t)(const ll*y, void*ctx);
static int solve_dot(const ll*x, ll k, ll M, cb_t cb, void*ctx){
  ll x1=x[0],x2=x[1],x3=x[2]; ll Y=isqrt_ll(M);
  ll q=x2*x2+x3*x3;
  for(ll y1=-Y;y1<=Y;y1++){
    ll R=M-y1*y1; ll c=k-x1*y1;
    /* q*y2^2 - 2 c x2 y2 + c^2 - x3^2 R = 0 ; disc/4 = x3^2 (q R - c^2) */
    __int128 D=(__int128)q*R-(__int128)c*c; if(D<0) continue;
    ll s=isqrt_ll((ll)D); if((__int128)s*s!=D) continue;
    for(int sg=-1;sg<=1;sg+=2){ if(sg==1 && s==0) break;
      __int128 num=(__int128)c*x2+(__int128)sg*x3*s; if(num%q) continue; ll y2=(ll)(num/q);
      ll r3=c-x2*y2; if(r3%x3) continue; ll y3=r3/x3;
      if(y1*y1+y2*y2+y3*y3!=M) continue;
      ll y[3]={y1,y2,y3}; if(cb(y,ctx)) return 1; }
  }
  return 0;
}
/* canonical reps 0<=x1<=x2<=x3 of m (m>0) */
static int canon_reps(ll m, ll (*out)[3], int maxo){
  int c=0; for(ll a=0;3*a*a<=m;a++) for(ll b=a;a*a+2*b*b<=m;b++){ ll r=m-a*a-b*b; ll s=isqrt_ll(r); if(s*s==r && s>=b){ if(c<maxo){out[c][0]=a;out[c][1]=b;out[c][2]=s;} c++; } } return c; }

/* ---------- mode iii ---------- */
typedef struct { ll t; const ll*x; int xisAs; int found_cong; } ctx3;
static int cb3(const ll*y, void*vc){ ctx3*c=(ctx3*)vc; c->found_cong|=0;
  const ll *X,*Yv; ll yy[3]={y[0],y[1],y[2]}; if(c->xisAs){X=c->x;Yv=yy;} else {X=yy;Yv=c->x;}
  ll z[3]={X[1]*Yv[2]-X[2]*Yv[1], X[2]*Yv[0]-X[0]*Yv[2], X[0]*Yv[1]-X[1]*Yv[0]};
  ll t=c->t; int okp=1, okm=1;
  for(int i=0;i<3;i++){ ll s=X[i]+Yv[i]; if(((z[i]-s)%t+t)%t) okp=0; if(((z[i]+s)%t+t)%t) okm=0; }
  if(okp||okm){ c->found_cong=1; return 1; }
  return 0; /* keep searching for a congruent one */ }
static int cbany(const ll*y, void*vc){ (void)y; *(int*)vc=1; return 1; }

static int lift_iii(ll t, ll A, ll As, int want_cong, int*cong){
  ll m = A<As?A:As, M = A<As?As:A; int xisAs = (As<=A); /* canonical vector carries norm m */
  static ll reps[20000][3]; int nr=canon_reps(m,reps,20000); if(nr>20000){fprintf(stderr,"reps overflow\n"); exit(1);}
  int found=0; *cong=0;
  for(int i=0;i<nr;i++){
    if(!want_cong){ int f=0; solve_dot(reps[i],1,M,cbany,&f); if(f){found=1;break;} }
    else { ctx3 c={t,reps[i],xisAs,0}; int f=0; solve_dot(reps[i],1,M,cbany,&f); if(f){ found=1; solve_dot(reps[i],1,M,cb3,&c); if(c.found_cong){*cong=1; break;} } }
  }
  return found;
}

/* enumerate words of n: callback(t,u,v) */
typedef void (*wcb)(ll t, ll u, ll v, ll n, void*ctx);
static void words(ll n, wcb f, void*ctx){
  for(ll t=1;t<=n+2;t++){ ll P=t*n+1; for(ll A=t-1; A*A<=P; A+=t){ if(A<1) continue; if(P%A) continue; ll As=P/A; if((As+1)%t) continue;
      ll u=(A+1)/t, v=(As+1)/t; f(t,u,v,n,ctx); if(As!=A) f(t,v,u,n,ctx); } }
}

typedef struct { ll words, d2, lift, mism, cong, congtested; int want_cong; ll sample_mism[4][4]; ll nchi_plus_notd2; int primemode; ll chi_plus, chi_minus; } st3;
static int jacobi(ll a, ll n){ a%=n; if(a<0)a+=n; int r=1; while(a){ while(a%2==0){ a/=2; ll m8=n%8; if(m8==3||m8==5) r=-r; } ll tmp=a;a=n;n=tmp; if(a%4==3&&n%4==3) r=-r; a%=n; } return n==1?r:0; }
static void w3(ll t, ll u, ll v, ll n, void*vc){ st3*s=(st3*)vc; ll A=t*u-1, As=t*v-1; s->words++;
  int d2=diff_is_2(t,n,As); int cong=0; int L=lift_iii(t,A,As,s->want_cong,&cong);
  int chi=jacobi(-A,n); if(chi==1) s->chi_plus++; else s->chi_minus++;
  if(chi==1 && !d2) s->nchi_plus_notd2++;
  if(s->primemode && (d2 != (chi==1))) { printf("PRIME DIFF/CHI MISMATCH n=%lld w=(%lld,%lld,%lld)\n",n,t,u,v); }
  s->d2+=d2; s->lift+=L; if(L!=d2){ if(s->mism<4){s->sample_mism[s->mism][0]=n;s->sample_mism[s->mism][1]=t;s->sample_mism[s->mism][2]=u;s->sample_mism[s->mism][3]=v;} s->mism++; }
  if(L && s->want_cong){ s->congtested++; s->cong+=cong; if(!cong) printf("no congruent lift: n=%lld w=(%lld,%lld,%lld)\n",n,t,u,v); }
}

/* ---------- mode iv / B: Gram s*G_w with G=[[v,-1,0],[-1,t,-1],[0,-1,u]] ---------- */
#define MAXL 200000
static ll Al[MAXL][3], Cl[MAXL][3]; static int nA, nC;
static int cbA(const ll*y, void*c){ (void)c; if(nA<MAXL){Al[nA][0]=y[0];Al[nA][1]=y[1];Al[nA][2]=y[2];} nA++; return 0; }
static int cbC(const ll*y, void*c){ (void)c; if(nC<MAXL){Cl[nC][0]=y[0];Cl[nC][1]=y[1];Cl[nC][2]=y[2];} nC++; return 0; }
static int gram_embed(ll s, ll t, ll u, ll v){
  static ll reps[20000][3]; int nr=canon_reps(s*t,reps,20000); if(nr>20000){fprintf(stderr,"overflow\n");exit(1);}
  for(int i=0;i<nr;i++){ nA=nC=0; solve_dot(reps[i],-s,s*v,cbA,NULL); if(!nA) continue; solve_dot(reps[i],-s,s*u,cbC,NULL);
    if(nA>MAXL||nC>MAXL){fprintf(stderr,"list overflow\n");exit(1);}
    for(int a=0;a<nA;a++) for(int c=0;c<nC;c++) if(Al[a][0]*Cl[c][0]+Al[a][1]*Cl[c][1]+Al[a][2]*Cl[c][2]==0) return 1; }
  return 0;
}
typedef struct { ll words, d2, emb, mism; } st4;
static void w4(ll t, ll u, ll v, ll n, void*vc){ st4*s=(st4*)vc; s->words++; ll As=t*v-1; int d2=diff_is_2(t,n,As); int e=gram_embed(n,t,u,v);
  s->d2+=d2; s->emb+=e; if(e!=d2){ s->mism++; if(s->mism<5) printf("iv mismatch n=%lld (%lld,%lld,%lld) d2=%d emb=%d\n",n,t,u,v,d2,e);} }
static void wB(ll t, ll u, ll v, ll n, void*vc){ st4*s=(st4*)vc; s->words++; ll As=t*v-1; int d2=diff_is_2(t,n,As); int e=gram_embed(1,t,u,v);
  s->d2+=d2; s->emb+=e; if(!e||!d2){ s->mism++; if(s->mism<5) printf("B failure n=%lld (%lld,%lld,%lld) d2=%d emb=%d\n",n,t,u,v,d2,e);} }

int main(int argc, char**argv){
  if(argc<4){fprintf(stderr,"usage\n");return 1;}
  const char*mode=argv[1]; ll N1=atoll(argv[2]), N2=atoll(argv[3]);
  if(!strcmp(mode,"iii")||!strcmp(mode,"iiip")||!strcmp(mode,"iiic")){
    st3 s; memset(&s,0,sizeof s); s.want_cong=!strcmp(mode,"iiic"); s.primemode=!strcmp(mode,"iiip");
    for(ll n=N1;n<=N2;n++){ if(n%2==0) continue; if(s.primemode && !is_prime(n)) continue; words(n,w3,&s); }
    printf("mode=%s range=[%lld,%lld] words=%lld Diff={2}:%lld lifts:%lld mismatches:%lld chi+:%lld chi-:%lld chi+&Diff!={2}:%lld",mode,N1,N2,s.words,s.d2,s.lift,s.mism,s.chi_plus,s.chi_minus,s.nchi_plus_notd2);
    if(s.want_cong) printf(" cong_tested:%lld cong_ok:%lld",s.congtested,s.cong);
    printf("\n"); for(int i=0;i<s.mism&&i<4;i++) printf("  mismatch n=%lld w=(%lld,%lld,%lld)\n",s.sample_mism[i][0],s.sample_mism[i][1],s.sample_mism[i][2],s.sample_mism[i][3]);
  } else if(!strcmp(mode,"iv")){
    st4 s; memset(&s,0,sizeof s); for(ll n=N1;n<=N2;n++){ if(n%2==0) continue; words(n,w4,&s);} 
    printf("mode=iv range=[%lld,%lld] words=%lld Diff={2}:%lld embed:%lld mismatches:%lld\n",N1,N2,s.words,s.d2,s.emb,s.mism);
  } else if(!strcmp(mode,"B")){
    st4 s; memset(&s,0,sizeof s); for(ll m=N1;m<=N2;m++){ if(m%2==0) continue; words(m*m,wB,&s);} 
    printf("mode=B m in [%lld,%lld] words=%lld Diff={2}:%lld embed(G_w itself):%lld failures:%lld\n",N1,N2,s.words,s.d2,s.emb,s.mism);
  }
  return 0;
}
