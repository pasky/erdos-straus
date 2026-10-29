/* z50 lsmass: depletion of the CRT avoider set of the U word family, by pivot level D.
   Fibre n = 8m+1 <= N. U-certificate (strict CONTEXT definition): a word (t,u,v), n = tuv-u-v, with an endpoint
   e in S = 4Z u (8Z+7) whose partner endpoint is >= 2.
   W1: pivot M = tu-1 (2 <= M <= D), u | M+1, v = (n+u)/M:
        (i) u in S, v >= 2       : class n == -u (mod M), n >= 2M - u
        (ii) u >= 2, v in S       : class n == M*r - u (mod 8M) for r in {0,4,7} (v mod 8), n >= M*r'-u
   W2: pivot uv <= D, t = (n+u+v)/(uv) >= 1: class n == -(u+v) (mod uv), (u in S, v>=2) or (v in S, u>=2).
   Output: survivors, and occupancy mod l for a few primes l, for each D in a list; the last D = N is the full set.
   Usage: z50_lsmass_depletion N            */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
static int inS(ll x){ return (x%4==0) || (x%8==7); }
static ll gcdll(ll a, ll b){ while(b){ ll t=a%b; a=b; b=t;} return a<0?-a:a; }
static ll N, Mf; static unsigned char *dead; static unsigned char *mark_D; /* mark_D[m] = level index at which killed */
static int curlev;
/* kill all n = 8m+1 <= N with n == b (mod G), n >= nmin; requires compatibility with n==1 mod 8 */
static ll egcd(ll a, ll b, ll *x, ll *y){ if(!b){*x=1;*y=0;return a;} ll x1,y1; ll g=egcd(b,a%b,&x1,&y1); *x=y1; *y=x1-(a/b)*y1; return g; }
static void kill(ll b, ll G, ll nmin){
  /* solve 8m+1 == b mod G  ->  8m == b-1 mod G */
  ll g = gcdll(8, G); ll rhs = ((b-1)%G+G)%G;
  if (rhs % g) return;
  ll Gp = G/g; ll x,y; egcd(8/g, Gp, &x, &y); x%=Gp; if(x<0)x+=Gp;
  ll m0 = ((rhs/g)%Gp) * x % Gp;
  ll mmin = (nmin>1)? (nmin-1+7)/8 : 0;
  if (m0 < mmin){ ll k=(mmin-m0+Gp-1)/Gp; m0 += k*Gp; }
  for (ll m=m0; m<Mf; m+=Gp) if(!dead[m]){ dead[m]=1; mark_D[m]=(unsigned char)curlev; }
}
int main(int argc, char**argv){
  N = atoll(argv[1]); Mf = (N-1)/8 + 1;
  dead = calloc(Mf,1); mark_D = calloc(Mf,1);
  ll Ds[16]; int nD=0; for(ll D=100; D<N; D*=10) Ds[nD++]=D; Ds[nD++]=N;
  ll *spf = calloc(N+3, sizeof(ll));
  for (ll i=2;i<=N+2;i++) if(!spf[i]) for(ll j=i;j<=N+2;j+=i) if(!spf[j]) spf[j]=i;
  ll prevD = 1;
  ll Ls[4] = {101, 1009, 10007, 100003};
  for (int li=0; li<nD; li++){
    ll D = Ds[li]; curlev = li+1;
    /* W1 pivots in (prevD, D] */
    for (ll M = (prevD<2?2:prevD+1); M<=D; M++){
      /* divisors of M+1 */
      ll x=M+1; ll ps[40]; int es[40]; int k=0;
      while(x>1){ ll p=spf[x]; int e=0; while(x%p==0){x/=p;e++;} ps[k]=p; es[k]=e; k++; }
      ll divs[20000]; int nd=1; divs[0]=1;
      for(int i=0;i<k;i++){ int cur=nd; ll pw=1; for(int e=1;e<=es[i];e++){ pw*=ps[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pw; } }
      for (int j=0;j<nd;j++){ ll u=divs[j];
        if (inS(u)) kill(((-u)%M+M)%M, M, 2*M);
        if (u>=2){ ll rs[3]={0,4,7}; for(int r=0;r<3;r++){ ll v0 = rs[r]==0?8:rs[r]; ll G=8*M; ll b=((M*rs[r]-u)%G+G)%G; kill(b, G, M*v0-u); } }
      }
    }
    /* W2 pivots uv in (prevD, D] */
    for (ll u=1; u<=D; u++) for (ll v=1; u*v<=D; v++){
      if (u*v <= prevD) continue;
      if ((inS(u) && v>=2) || (inS(v) && u>=2)){ ll q=u*v; kill(((-(u+v))%q+q)%q, q, q-u-v>1?q-u-v:1); }
    }
    prevD = D;
    ll surv=0; for(ll m=1;m<Mf;m++) if(!dead[m]) surv++;
    printf("D=%lld survivors(n>1)=%lld", D, surv);
    for (int t=0;t<4;t++){ ll l=Ls[t]; if (l*l > 4*N) continue; unsigned char *occ=calloc(l,1); ll c=0;
      for(ll m=1;m<Mf;m++) if(!dead[m]){ ll r=(8*m+1)%l; if(!occ[r]){occ[r]=1;c++;} }
      printf("  occ mod %lld = %lld", l, c); free(occ); }
    printf("\n"); fflush(stdout);
  }
  /* list non-square survivors at full level */
  printf("non-square survivors:");
  for(ll m=1;m<Mf;m++) if(!dead[m]){ ll n=8*m+1; ll r=(ll)__builtin_sqrtl((long double)n); while(r*r>n)r--; while((r+1)*(r+1)<=n)r++; if(r*r!=n) printf(" %lld", n); }
  printf("\n");
  return 0;
}
