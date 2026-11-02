/* z54 BILINJAC — the actual Poisson (l, C) bilinear form at the balanced block, by dyadic frequency shells.
   S_Q^sm := sum_{C in (W,2W]} sum_k Phi((4Ck-n)/V) chi_Q(f(C,k)),  Phi(t) = exp(-pi (t-3)^2)  (Schwartz; Lemma P holds)
          = sum_l sum_C a_l(C) e(-l n/(4CQ)) G_C(l),  a_l(C) = (V/(4CQ)) Phihat(l V/(4CQ)),  Phihat(x) = e(-3x) exp(-pi x^2),
   G_C(l) = sum_{k mod Q} chi_Q(f(C,k)) e(l k/Q)   (SQSIEVE Lemma P / Lemma W).
   Prints the direct sum, the dual total, and per dyadic shell |l| in [2^j, 2^{j+1}) (and l = 0):
     |shell sum|, l2 := (sum |term|^2)^{1/2} (random-phase benchmark), l1 := sum |term| (trivial bound), #terms.
   usage: shells n V W q q'          (Q = q q', distinct odd primes; n < 2^62) */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
typedef long long ll; typedef unsigned long long ull;
static int jac(ull a, ull n){ int t=1; a%=n; while(a){ while(!(a&1)){ a>>=1; ull r=n&7; if(r==3||r==5) t=-t;} ull tmp=a; a=n; n=tmp; if((a&3)==3 && (n&3)==3) t=-t; a%=n;} return n==1?t:0; }
static int jq(ll a, ll Q){ ll r=a%Q; if(r<0) r+=Q; return jac((ull)r,(ull)Q); }
int main(int argc,char**argv){
  if(argc<6){fprintf(stderr,"usage\n");return 1;}
  ll n=atoll(argv[1]); double V=atof(argv[2]); ll W=atoll(argv[3]); ll q1=atoll(argv[4]), q2=atoll(argv[5]); ll Q=q1*q2;
  /* direct */
  double direct=0;
  for(ll C=W+1;C<=2*W;C++){ ll k0=(ll)floor((n-2.0*V)/(4.0*C)); ll k1=(ll)ceil((n+8.0*V)/(4.0*C));
    for(ll k=(k0<1?1:k0);k<=k1;k++){ double t=(double)(4*C*k-n)/V; double ph=exp(-M_PI*(t-3)*(t-3)); if(ph<1e-18) continue;
      __int128 s=(__int128)4*C*k-n; __int128 f=s*s-4*(__int128)k; ll fm=(ll)(f%Q); direct+=ph*jq(fm,Q); } }
  /* G table */
  double complex *G=malloc(sizeof(double complex)*Q*Q); ll nQ=((n%Q)+Q)%Q;
  int *ch=malloc(sizeof(int)*Q);
  for(ll c=0;c<Q;c++){
    for(ll k=0;k<Q;k++){ ll s=((4*c%Q)*k%Q - nQ + Q)%Q; ll f=((s*s)%Q - (4*k)%Q + Q)%Q; ch[k]=jq(f,Q); }
    for(ll l=0;l<Q;l++){ double complex z=0; for(ll k=0;k<Q;k++) if(ch[k]) z+=ch[k]*cexp(2*M_PI*I*(double)((l*k)%Q)/Q); G[c*Q+l]=z; }
  }
  int NS=64; double complex *sh=calloc(NS,sizeof(double complex)); double *l2=calloc(NS,sizeof(double)), *l1=calloc(NS,sizeof(double)); ll *nt=calloc(NS,sizeof(ll));
  double complex total=0;
  for(ll C=W+1;C<=2*W;C++){
    double sc=V/(4.0*C*Q); ll lmax=(ll)ceil(6.5/sc); ll M=4*C*Q; ll r=n%M; /* e(-l n/(4CQ)) = e(-l r/M) */
    ll c=C%Q;
    for(ll l=-lmax;l<=lmax;l++){
      double x=l*sc; double amp=sc*exp(-M_PI*x*x); if(amp<1e-30) continue;
      double complex ah=amp*cexp(-2*M_PI*I*3.0*x);
      ll lr=(ll)(((__int128)l*r)%M); double complex ph=cexp(-2*M_PI*I*(double)lr/(double)M);
      ll lm=((l%Q)+Q)%Q; double complex term=ah*ph*G[c*Q+lm];
      ll al=l<0?-l:l; int j= al==0?0: 1+(int)floor(log2((double)al)); if(j>=NS) j=NS-1;
      sh[j]+=term; l2[j]+=creal(term*conj(term)); l1[j]+=cabs(term); nt[j]++; total+=term;
    }
  }
  printf("n=%lld V=%.0f W=%lld Q=%lld*%lld=%lld  direct S_Q^sm=%.6f  dual total=%.6f%+.6fi  (diff %.2e)\n",n,V,W,q1,q2,Q,direct,creal(total),cimag(total),cabs(total-direct));
  printf("  scale: l* = 4WQ/V = %.0f ; random-model sqrt(sum Phi^2) ~ sqrt|A|\n", 4.0*W*Q/V);
  printf("  shell(j: |l| in [2^(j-1),2^j))  #terms        |sum|       l2        l1     |sum|/l2\n");
  for(int j=0;j<NS;j++) if(nt[j]) printf("  %2d %14lld %12.4f %10.4f %12.2f %8.3f\n",j,nt[j],cabs(sh[j]),sqrt(l2[j]),l1[j],cabs(sh[j])/sqrt(l2[j]));
  /* cumulative from the top */
  double complex cum=0; printf("  cumulative from top shell down: "); for(int j=NS-1;j>=0;j--) if(nt[j]){ cum+=sh[j]; printf("[%d]%.2f ",j,cabs(cum)); } printf("\n");
  return 0;
}
