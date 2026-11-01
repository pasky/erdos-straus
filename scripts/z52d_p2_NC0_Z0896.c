// Z0896: count S(p) = #{(x,y,z) in Z_{>0}^3 : x <= y, z <= p^2, 1/x + 1/y - 1/z = 4/p} for primes p.
// Method (divisor form, exact): for fixed x, c = 4x - p (!=0 since p odd), d = p x, the equation becomes
//   1/y - 1/z = c/d  <=>  (d - c y)(c z + d) = d^2.  Put m = d - c y (a divisor of d^2, m>0), then
//   y = (d - m)/c,  z = (d^2/m - d)/c.  Range: x < p/2 (since 2/x > 4/p).  Output per prime:
//   output per prime: p  S  O(ordered over (x,y))  minz
// Usage: ./z52d_p2_NC0_Z0896 pmax [brute_pmax]   (brute check for p <= brute_pmax, prints mismatch)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll; typedef unsigned long long ull; typedef __int128 i128;  // d^2 = p^2 x^2 overflows 64 bits for p x > 4.3e9
static int *spf;
static int isprime_small(ll n){ if(n<2) return 0; for(ll d=2;d*d<=n;d++) if(n%d==0) return 0; return 1; }
// count for one prime p; returns S (x<=y), fills O (ordered in x,y) and minz
static ll count_p(ll p, ll *O, ll *minz, ll *nsol_sumx){ (void)0;
  ll S=0; *O=0; *minz=-1; ll p2=p*p;
  for(ll x=1; 2*x<p; x++){
    ll c = 4*x - p, d = p*x;  // d <= p^2/2 < 2^33 for p<=2e5
    // factor d^2 = p^2 x^2 : exponents
    int np=0; ll pr[32]; int ex[32];
    ll v=x; // add primes of x
    while(v>1){ int q=spf[v]; int e=0; while(v%q==0){v/=q;e++;}
      int i; for(i=0;i<np;i++) if(pr[i]==q) break; if(i==np){pr[np]=q;ex[np]=0;np++;} ex[i]+=2*e; }
    { int i; for(i=0;i<np;i++) if(pr[i]==p) break; if(i==np){pr[np]=p;ex[np]=0;np++;} ex[i]+=2; }
    // enumerate divisors m of d^2 via iterative product
    i128 dd2 = (i128)d*(i128)d;
    // iterative enumeration with stack
    ull divs_cap = 1; for(int i=0;i<np;i++) divs_cap *= (ex[i]+1);
    i128 *dv = malloc(sizeof(i128)*divs_cap); ll nd=1; dv[0]=1;
    for(int i=0;i<np;i++){ ll cur=nd; i128 pw=1; for(int e=1;e<=ex[i];e++){ pw*=pr[i]; for(ll j=0;j<cur;j++) dv[nd++]=dv[j]*pw; } }
    for(ll k=0;k<nd;k++){
      i128 m = dv[k];
      i128 num = dd2 / m - d;   // d^2/m - d  (may be negative)
      i128 mm = (i128)d - m;    // d - m
      if(c==0) continue;
      if(mm % c != 0 || num % c != 0) continue;
      i128 y = mm / c, z = num / c;
      if(y < x || z < 1) continue;   // y>=x, z>=1 (y>=1 implied)
      if(z > p2) continue;
      S++; if(y==x) *O += 1; else *O += 2;
      if(*minz<0 || z < *minz) *minz = z;
      if(nsol_sumx) *nsol_sumx += x;
    }
    free(dv);
  }
  return S;
}
// brute force for small p (x<=y, z<=p^2)
static ll brute_p(ll p){
  ll S=0; ll p2=p*p;
  // no a-priori bound on y when 4x<p: z integer <= p^2 forces y <= p^3 x (y(px-k(p-4x))=kpx, k<=p^2)
  for(ll x=1; x<=p; x++) for(ll y=x; y<=p*p*p*x; y++){
    // need 1/z = 1/x+1/y-4/p > 0 with z<=p^2: solve numerically exactly
    // 1/z = (p(x+y) - 4xy)/(pxy)
    ll num = p*(x+y) - 4*x*y; ll den = p*x*y;
    if(num<=0) continue;
    if(den % num) continue; // z = den/num must be integer
    ll z = den/num; if(z<=p2) S++;
  }
  return S;
}
int main(int argc,char**argv){
  ll pmax=atoll(argv[1]); ll bmax = argc>2? atoll(argv[2]) : 0;
  spf = calloc(pmax+2, sizeof(int));
  for(ll i=2;i<=pmax;i++) if(!spf[i]) for(ll j=i;j<=pmax;j+=i) if(!spf[j]) spf[j]=i;
  // brute-force check on small primes
  int bad=0; ll nb=0;
  for(ll p=5;p<=bmax;p++){ if(!isprime_small(p)) continue; ll O,mz; ll a=count_p(p,&O,&mz,NULL), b=brute_p(p); nb++;
    if(a!=b){ bad++; fprintf(stderr,"MISMATCH p=%lld fast=%lld brute=%lld\n",p,a,b);} }
  if(bmax) printf("# brute check primes<=%lld: %lld checked, mismatches=%d\n", bmax, nb, bad);
  for(ll p=5;p<=pmax;p++){ if(p%4!=1 || !isprime_small(p)) continue;
    ll O,mz; ll S=count_p(p,&O,&mz,NULL);
    printf("%lld %lld %lld %lld\n", p, S, O, mz);
  }
  return 0;
}
