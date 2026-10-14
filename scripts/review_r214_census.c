/* R214 from-scratch census of N_-(p), N_+(p) (words of X_p, chi = (-A/p)), independent of si_census.c.
 * usage: review_r214_census lo hi        -> summary over primes p in [lo,hi]
 *        review_r214_census list p1 p2 ...-> per-prime N-, N+
 * Reports: #primes p = 1 (4), p > 5 with N- < N+; worst ratios; N- mod 8 distribution (p = 1 mod 8 / 5 mod 8);
 * mean N- over p = 1 (8); check N-(p) >= omega_3(p+1) for p = 1 (4); parity N-(p) = [p = 3 (4)] (mod 2).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
static int jacobi(ll a, ll n){ a%=n; if(a<0)a+=n; int r=1; while(a){ while(a%2==0){ a/=2; ll m8=n%8; if(m8==3||m8==5) r=-r; } ll t=a;a=n;n=t; if(a%4==3&&n%4==3) r=-r; a%=n; } return n==1?r:0; }
static void count(ll p, ll*Nm, ll*Np){
  ll m=0,q=0;
  for(ll t=1;t<=p+2;t++){ ll P=t*p+1; for(ll A=t-1; A*A<=P; A+=t){ if(A<1) continue; if(P%A) continue; ll As=P/A; if((As+1)%t) continue;
      int c=jacobi(-A,p); int c2=jacobi(-As,p); if(c!=c2){fprintf(stderr,"reversal chi mismatch p=%lld\n",p); exit(1);} 
      int mult=(As!=A)?2:1; if(c==-1) m+=mult; else q+=mult; } }
  *Nm=m; *Np=q;
}
static int omega3(ll x){ int c=0; for(ll d=3; d*d<=x; d+=2) if(x%d==0){ if(d%4==3) c++; while(x%d==0) x/=d; } while(x%2==0) x/=2; if(x>1 && x%4==3) c++; return c; }
int main(int argc,char**argv){
  if(argc>=2 && !strcmp(argv[1],"list")){ for(int i=2;i<argc;i++){ ll p=atoll(argv[i]),a,b; count(p,&a,&b); printf("p=%lld N-=%lld N+=%lld\n",p,a,b);} return 0; }
  ll lo=atoll(argv[1]), hi=atoll(argv[2]);
  char*sv=calloc(hi+1,1); for(ll i=2;i<=hi;i++) sv[i]=1; for(ll i=2;i*i<=hi;i++) if(sv[i]) for(ll j=i*i;j<=hi;j+=i) sv[j]=0;
  ll n14=0, viol=0, mod8[2][8]={{0}}, cnt18=0; double sum18=0; ll om_fail=0, par_fail=0;
  for(ll p=(lo<3?3:lo); p<=hi; p++){ if(!sv[p]) continue; ll Nm,Np; count(p,&Nm,&Np);
    if((Nm%2) != (p%4==3)) par_fail++;
    if(p%4==1){ if(Nm<omega3(p+1)) om_fail++;
      if(p>5){ n14++; if(Nm<Np){ viol++; if(Nm*4<=Np) printf("  strong violation p=%lld N-=%lld N+=%lld\n",p,Nm,Np);} }
      mod8[p%8==1?0:1][Nm%8]++; }
    if(p%8==1){ cnt18++; sum18+=Nm; }
  }
  printf("range [%lld,%lld]: primes p=1(4),p>5: %lld; N-<N+ at %lld; parity failures %lld; N-<omega3(p+1) failures %lld\n",lo,hi,n14,viol,par_fail,om_fail);
  printf("N- mod 8 (p=1 mod 8): "); for(int r=0;r<8;r++) printf("%lld ",mod8[0][r]); printf("\nN- mod 8 (p=5 mod 8): "); for(int r=0;r<8;r++) printf("%lld ",mod8[1][r]);
  printf("\nmean N- over p=1(8): %.2f (%lld primes)\n", cnt18?sum18/cnt18:0, cnt18);
  return 0;
}
