/* z51 linnik: per-prime forcing reach with the FULL ES Type II ratio classes (EXSET_LINNIK §6, EVIDENCE).
   Classes: R(M) = { n == -4D (mod M) : M == 3 (mod 4), A = (M+1)/4, D | A^2 }  (CAP_INTERPOLATION Prop 5.1, e = 0:
   every prime p == -4D (mod M), p not dividing DM, has an ES solution).  Profinite forcing as in z50 lane B:
   fix a prime p, a small prime q (q not dividing p); a residue a mod q is "forced away" if the point x with x == p mod m
   for all m coprime to q and x == a mod q lies in some R(qm) class with gcd(m,q)=1 and pivot qm <= PB, i.e.
   m | p + 4D and a == -4D (mod q).  For each q we report the number of non-residues reached, the number of distinct
   labels, and the least pivot bound needed to reach all non-residues (if reached).
   mode 1 ("plane"): replace p by 1 in the m-coordinates (x == 1 mod m): the r-generic / plane point.
   Usage: z51_linnik_forcing_es p qmax PB mode */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
static int *spf; static ll SPFN;
static int legendre(ll a, ll q){ a%=q; if(a<0)a+=q; ll r=1,b=a,e=(q-1)/2; while(e){ if(e&1) r=r*b%q; b=b*b%q; e>>=1;} return r==1?1:(r==0?0:-1); }
static int isprime(ll n){ if(n<2) return 0; for(ll d=2;d*d<=n;d++) if(n%d==0) return 0; return 1; }
int main(int argc,char**argv){
  if(argc<5){ fprintf(stderr,"usage: p qmax PB mode\n"); return 1; }
  ll p=atoll(argv[1]); int qmax=atoi(argv[2]); ll PB=atoll(argv[3]); int mode=atoi(argv[4]);
  ll pm = mode==1 ? 1 : p;             /* value of x in the m-coordinates */
  SPFN = PB/4+10; spf = calloc(SPFN+1,sizeof(int));
  for(ll i=2;i<=SPFN;i++) if(!spf[i]) for(ll j=i;j<=SPFN;j+=i) if(!spf[j]) spf[j]=(int)i;
  static ll divs[1<<20];
  for(int q=3;q<=qmax;q+=2){ if(!isprime(q) || p%q==0) continue;
    ll *best = malloc(sizeof(ll)*q); for(int a=0;a<q;a++) best[a]=-1;
    long nlabels=0;
    for(ll m=1; m*q<=PB; m++){ if(m%q==0) continue; ll M=m*q; if(M%4!=3) continue;
      ll A=(M+1)/4; /* factor A */
      ll ps[40]; int es[40]; int k=0; ll x=A;
      while(x>1){ int pr=spf[x]; int e=0; while(x%pr==0){x/=pr;e++;} ps[k]=pr; es[k]=2*e; k++; }
      int nd=1; divs[0]=1;
      for(int i=0;i<k;i++){ int cur=nd; ll pw=1; for(int e=1;e<=es[i];e++){ pw*=ps[i]; for(int j=0;j<cur && nd<(1<<20);j++) divs[nd++]=divs[j]*pw; } }
      ll target = ((-pm) % m + m) % m;   /* need 4D == -pm (mod m) */
      for(int j=0;j<nd;j++){ ll D=divs[j];
        if( ((4*(D%m))%m) != target ) continue;
        if(mode==0 && (D%p==0)) continue;
        nlabels++;
        ll a = ((-4*(D%q))%q + q)%q;
        if(best[a]<0 || M<best[a]) best[a]=M;
      }
    }
    int nnr=0, reached=0; ll worst=0;
    for(ll a=1;a<q;a++) if(legendre(a,q)==-1){ nnr++; if(best[a]>=0){ reached++; if(best[a]>worst) worst=best[a]; } }
    int rres=0; for(ll a=1;a<q;a++) if(legendre(a,q)==1 && best[a]>=0) rres++;
    printf("q=%d (p/q)=%d nonres=%d reached=%d labels=%ld residues_hit=%d maxminpivot=%lld\n", q, legendre(p,q), nnr, reached, nlabels, rres, reached==nnr?worst:-1);
    fflush(stdout);
    free(best);
  }
  return 0;
}
