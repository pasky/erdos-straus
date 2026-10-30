/* z51 linnik §8 (EVIDENCE): conditional non-residue probability of the avoider of the ES ratio classes.
   Sieve the primes p <= N, p == 1 (mod 24), by all classes R(M) = { -4D mod M : M == 3 (4), D | ((M+1)/4)^2 } with
   M <= H (CAP_INTERPOLATION Prop 5.1, e = 0; only classes with p > 4D... no threshold needed: every prime p == -4D mod M
   with p not dividing DM has ES).  For H in a ladder, report the number of surviving primes and, for each small prime
   q in a list, the fraction of survivors with (p/q) = -1.  The square-like survivors (residues at every small q) are
   what Linnik counts; the question is how fast the non-residue fraction at q decays with the level H.
   Usage: z51_linnik_tilt N Hmax */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
static int legendre(ll a, ll q){ a%=q; if(a<0)a+=q; ll r=1,b=a,e=(q-1)/2; while(e){ if(e&1) r=r*b%q; b=b*b%q; e>>=1;} return r==1?1:(r==0?0:-1); }
int main(int argc, char**argv){
  ll N = atoll(argv[1]); ll Hmax = atoll(argv[2]);
  char *comp = calloc(N+1,1); for(ll i=2;i*i<=N;i++) if(!comp[i]) for(ll j=i*i;j<=N;j+=i) comp[j]=1;
  char *alive = calloc(N+1,1); ll nalive=0;
  for(ll p=25;p<=N;p++) if(!comp[p] && p%24==1){ alive[p]=1; nalive++; }
  int qs[] = {5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}; int nq = sizeof(qs)/sizeof(int);
  ll H = 3; ll next = 100;
  static ll divs[1<<16];
  printf("H survivors | nonres-fraction at q = "); for(int i=0;i<nq;i++) printf("%d ", qs[i]); printf("\n");
  for(ll M=3; M<=Hmax; M+=4){
    ll A=(M+1)/4; ll x=A; ll ps[30]; int es[30]; int k=0;
    for(ll d=2; d*d<=x; d++) if(x%d==0){ int e=0; while(x%d==0){x/=d;e++;} ps[k]=d; es[k]=2*e; k++; }
    if(x>1){ ps[k]=x; es[k]=2; k++; }
    int nd=1; divs[0]=1;
    for(int i=0;i<k;i++){ int cur=nd; ll pw=1; for(int e=1;e<=es[i];e++){ pw*=ps[i]; for(int j=0;j<cur && nd<(1<<16);j++) divs[nd++]=divs[j]*pw; } }
    /* distinct residues -4D mod M */
    for(int j=0;j<nd;j++){ ll D=divs[j]; ll r = ((-4*(D%M))%M+M)%M; if(r==0) continue;
      for(ll n=r; n<=N; n+=M) if(alive[n]){ if(D%n==0 || M%n==0) continue; alive[n]=0; nalive--; }
    }
    if(M+4>next || M+4>Hmax){
      long cnt[64]={0}; for(ll p=25;p<=N;p++) if(alive[p]) for(int i=0;i<nq;i++) if(legendre(p,qs[i])==-1) cnt[i]++;
      printf("%lld %lld |", M, nalive); for(int i=0;i<nq;i++) printf(" %.3f", nalive? (double)cnt[i]/nalive:0.0); printf("\n"); fflush(stdout);
      next*=2;
    }
  }
  return 0;
}
