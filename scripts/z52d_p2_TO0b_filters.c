// z52d pass2 TO0b: filtered ES census for 4/p = 1/x+1/y+1/z (x<=y<=z), all primes 5 <= p < N.
// Per prime: p, total count, #no denominator = 1 mod 3 (Z0200), #with p not dividing x (Z0202, predicate p does not divide x),
// #with max denominator <= p^2/8 (Z0201), #chain solutions x|y|z (Z0216), (x-predicate only).
// Also per prime: min over sols of max(z)/p^2 (Z0201 c(p)) as a double, and whether x,y,z all = 1 mod 3 possible.
// usage: z52d_p2_TO0b_filters N
#include <stdio.h>
#include <stdlib.h>
typedef long long ll; typedef __int128 i128;
static int *spf; static int SPFN;
static ll gcdll(ll a, ll b){ while(b){ ll t=a%b; a=b; b=t;} return a; }
static int factor_small(ll n, int *ps, int *es){
  int k=0; while(n>1){ int q=spf[n]; int e=0; while(n%q==0){ n/=q; e++; } ps[k]=q; es[k]=e; k++; }
  return k;
}
int main(int argc, char **argv){
  int N = atoi(argv[1]);
  SPFN = 4*N+10;
  spf = calloc(SPFN+1, sizeof(int));
  for(int i=2;i<=SPFN;i++) if(!spf[i]) for(int j=i;j<=SPFN;j+=i) if(!spf[j]) spf[j]=i;
  i128 *divs = malloc(sizeof(i128)*4000000);
  for(int p=5;p<N;p++){
    if(spf[p]!=p) continue;
    ll cnt=0, cn1=0, cpnd=0, cszs=0, cchain=0; double best=-1;
    for(ll x=p/4+1; 4*x<=3LL*p; x++){
      if(4*x<=p) continue;
      ll a=4*x-p; ll bfull=(ll)p*x;
      ll g=gcdll(a,bfull); a/=g;
      int pp[64],pe[64],np=0;
      { int tp[32],te[32]; int k=factor_small(x,tp,te);
        for(int i=0;i<k;i++){ pp[np]=tp[i]; pe[np]=te[i]; np++; }
        int found=0; for(int i=0;i<np;i++) if(pp[i]==p){ pe[i]+=1; found=1; }
        if(!found){ pp[np]=p; pe[np]=1; np++; } }
      { int tp[32],te[32]; int k=factor_small(g,tp,te);
        for(int i=0;i<k;i++) for(int j=0;j<np;j++) if(pp[j]==tp[i]) pe[j]-=te[i]; }
      i128 bval=1; for(int j=0;j<np;j++) for(int e=0;e<pe[j];e++) bval*=pp[j];
      i128 nd=1; for(int j=0;j<np;j++) nd*=(2*pe[j]+1);
      if(nd>4000000){ fprintf(stderr,"too many divisors p=%d x=%lld\n",p,x); exit(1); }
      ll ndiv=(ll)nd; ll cur=1; divs[0]=1;
      for(int j=0;j<np;j++){ ll base=cur; i128 pw=1;
        for(int e=1;e<=2*pe[j];e++){ pw*=pp[j]; for(ll t=0;t<base;t++) divs[e*base+t]=divs[t]*pw; }
        cur=base*(2*pe[j]+1); }
      for(ll i=0;i<ndiv;i++){
        i128 d=divs[i]; if(d>bval) continue;
        i128 zz=bval*bval/d;
        if( (d+bval)%a ) continue;
        if( (zz+bval)%a ) continue;
        i128 y=(d+bval)/a, z=(zz+bval)/a;
        if(y<(i128)x) continue;
        cnt++;
        ll yy=(ll)y, zl=(ll)z;   // y,z < 2^63 for p < 1e6 (z <= ~p^2 * ...) -- guarded below
        if(x%3!=1 && yy%3!=1 && zl%3!=1) cn1++;
        if(x%p!=0) cpnd++;
        double r = (double)zl/((double)p*(double)p);
        if(r<=0.125) cszs++;
        if(best<0 || r<best) best=r;
        if(yy%x==0 && zl%yy==0) cchain++;
      }
    }
    printf("%d\t%lld\t%lld\t%lld\t%lld\t%lld\t%.6f\n", p, cnt, cn1, cpnd, cszs, cchain, best);
    fflush(stdout);
  }
  return 0;
}
