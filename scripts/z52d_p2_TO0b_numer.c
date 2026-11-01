// z52d pass2 TO0b: generic-numerator census. For each prime p < N (all primes >= 5, optionally p = 1 mod 4 only),
// count solutions of m/p = 1/x + 1/y + 1/z with x <= y <= z positive integers (ordered by x<=y<=z).
// Same algorithm as scripts/z52d_p2_TO1_es.c (divisors of b^2, b = p*x/g), generalised from numerator 4 to m.
// Output per prime: p cnt minX_slack(=m*x-p min over sols, -1 if none) minMaxDen(z) 
// usage: z52d_p2_TO0b_numer N m [mod4]   (mod4=1 restricts to p = 1 mod 4)
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
  int N = atoi(argv[1]); ll m = atoll(argv[2]); int mod4 = (argc>3 && argv[3][0]=='1');
  SPFN = 4*N+10;
  spf = calloc(SPFN+1, sizeof(int));
  for(int i=2;i<=SPFN;i++) if(!spf[i]) for(int j=i;j<=SPFN;j+=i) if(!spf[j]) spf[j]=i;
  i128 *divs = malloc(sizeof(i128)*4000000);
  for(int p=2;p<N;p++){
    if(spf[p]!=p || p<3) continue;
    if(mod4 && p%4!=1) continue;
    ll cnt=0, E=-1; i128 M=-1;
    for(ll x=p/m+1; m*x<=3LL*p; x++){
      if(m*x<=p) continue;
      ll a=m*x-p; ll bfull=(ll)p*x;
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
        if(E<0) E=m*x-p;
        if(M<0 || z<M) M=z;
      }
    }
    printf("%d\t%lld\t%lld\t%lld\n", p, cnt, E, (ll)M);
    fflush(stdout);
  }
  return 0;
}
