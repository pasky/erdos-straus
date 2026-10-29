/* z50 lsmass: per-prime character forcing reach (EVIDENCE for §4.2).
   For a prime p == 1 (mod 8) and a small odd prime q not dividing p, a non-residue a mod q is "forced away" if the
   integer n with n == p (mod m) for all m coprime to q but n == a (mod q) would carry a U word with pivot q*m:
   u in S = 4Z u (8Z+7), u | q*m+1, n == -u (mod q*m). Since n == p (mod m), this means m | p+u, and -u == a (mod q).
   We enumerate u in S, u <= U, factor p+u, run over divisors m of p+u with gcd(m,q)=1, q*m <= p/2, u | q*m+1,
   and record for each residue a = -u mod q the least pivot q*m reaching it.  M_q = max over non-residues a of that
   least pivot (infinite if some non-residue is unreached). Prints q, (p/q), M_q.
   Usage: z50_lsmass_forcing p U qmax */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll; typedef unsigned long long ull;
static int inS(ll x){ return x%4==0 || x%8==7; }
static int legendre(ll a, ll q){ a%=q; if(a<0)a+=q; ll r=1,b=a,e=(q-1)/2; while(e){ if(e&1) r=r*b%q; b=b*b%q; e>>=1;} return r==1?1:(r==0?0:-1); }
int main(int argc,char**argv){
  ll p=atoll(argv[1]), U=atoll(argv[2]); int qmax=atoi(argv[3]);
  int qs[100]; int nq=0; for(int q=3;q<=qmax;q+=2){ int pr=1; for(int d=3;d*d<=q;d+=2) if(q%d==0){pr=0;break;} if(pr && p%q) qs[nq++]=q; }
  ll *best[100]; for(int i=0;i<nq;i++){ best[i]=malloc(sizeof(ll)*qs[i]); for(int a=0;a<qs[i];a++) best[i][a]=-1; }
  /* small primes for trial division */
  int LIM=2000000; char *comp=calloc(LIM+1,1); int *pr=malloc(sizeof(int)*200000); int np=0;
  for(int i=2;i<=LIM;i++){ if(!comp[i]){ pr[np++]=i; for(ll j=(ll)i*i;j<=LIM;j+=i) comp[j]=1; } }
  for(ll u=3; u<=U; u++){ if(!inS(u)) continue;
    ll x=p+u; ll ps[64]; int es[64]; int k=0;
    for(int i=0;i<np && (ll)pr[i]*pr[i]<=x;i++){ if(x%pr[i]==0){ int e=0; while(x%pr[i]==0){x/=pr[i];e++;} ps[k]=pr[i]; es[k]=e; k++; } }
    if(x>1){ ps[k]=x; es[k]=1; k++; }
    static ll divs[200000]; int nd=1; divs[0]=1;
    for(int i=0;i<k;i++){ int cur=nd; ll pw=1; for(int e=1;e<=es[i];e++){ pw*=ps[i]; for(int j=0;j<cur && nd<200000;j++) divs[nd++]=divs[j]*pw; } }
    for(int j=0;j<nd;j++){ ll m=divs[j];
      for(int i=0;i<nq;i++){ ll q=qs[i]; if(m%q==0) continue; if((__int128)q*m*2 > p) continue;
        if( ((__int128)q*m+1) % u ) continue;
        ll a=((-u)%q+q)%q; ll piv=q*m; if(best[i][a]<0 || piv<best[i][a]) best[i][a]=piv; }
    }
  }
  for(int i=0;i<nq;i++){ ll q=qs[i]; ll Mq=0; int unreached=0, nnr=0;
    for(ll a=1;a<q;a++) if(legendre(a,q)==-1){ nnr++; if(best[i][a]<0) unreached++; else if(best[i][a]>Mq) Mq=best[i][a]; }
    printf("q=%lld (p/q)=%d nonres=%d unreached=%d maxminpivot=%lld\n", q, legendre(p,q), nnr, unreached, Mq);
  }
  return 0;
}
