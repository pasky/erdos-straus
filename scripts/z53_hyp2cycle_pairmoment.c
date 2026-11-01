/* z53_hyp2cycle_pairmoment.c — second factorial moments of N2 and N4 in the independent-CRT model
   (p uniform over units mod a common multiple).  For two distinct pairs with moduli q1,q2 and target residues
   a_i = -(u_i+B_i) mod q_i:  P(both) = [a1 == a2 mod g] / phi(lcm(q1,q2)),  g = gcd(q1,q2),
   phi(lcm) = phi(q1) phi(q2) / phi(g).  Prints E N, E N(N-1), ratio E N(N-1)/(E N)^2, for
   N2 (q = uB, coprime pairs) and N4 (q = 4uB, coprime pairs with u+B odd).   usage: ./pairmoment U */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static ll gcdl(ll a,ll b){ while(b){ll t=a%b;a=b;b=t;} return a; }
static ll phil(ll n){ ll r=n; for(ll l=2;l*l<=n;l++) if(n%l==0){ while(n%l==0) n/=l; r-=r/l; } if(n>1) r-=r/n; return r; }
int main(int argc,char**argv){ ll U=atoll(argv[1]);
  for(int mode=2;mode<=4;mode+=2){
    ll cap=U*U; ll *q=malloc(sizeof(ll)*cap), *a=malloc(sizeof(ll)*cap); double *ph=malloc(sizeof(double)*cap); ll m=0;
    for(ll u=U+1;u<=2*U;u++) for(ll B=u+1;B<=2*U;B++){ if(gcdl(u,B)!=1) continue; if(mode==4 && !((u+B)&1)) continue;
        ll Q=(mode==4?4:1)*u*B; q[m]=Q; a[m]=((-(u+B))%Q+Q)%Q; ph[m]=(double)phil(Q); m++; }
    double E1=0,E2=0;
    for(ll i=0;i<m;i++) E1+=1.0/ph[i];
    #pragma omp parallel for reduction(+:E2) schedule(dynamic,16)
    for(ll i=0;i<m;i++) for(ll j=i+1;j<m;j++){ ll g=gcdl(q[i],q[j]); if((a[i]-a[j])%g) continue;
        E2+=2.0*(double)phil(g)/(ph[i]*ph[j]); }
    printf("U=%lld N%d pairs=%lld EN=%.6f EN(N-1)=%.6f ratio=%.4f var/mean=%.4f\n",U,mode,m,E1,E2,E2/(E1*E1),(E2+E1-E1*E1)/E1);
    free(q);free(a);free(ph);
  }
  return 0; }
