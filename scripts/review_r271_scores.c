/* R271 from-scratch scores for p = 1 (4) prime in [P1, P2]: N1, fII (ordered, gcd(a,c)=1), m0, e0 (brute, e <= 199).
   Type II: c(4abd - p) = a + b.  e0: least e = 3 (4) with e/H = 1/x + 1/y, H = (pe+1)/4 (brute over x).
   Output: p N1 fII m0 e0    Usage: review_r271_scores P1 P2 */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static ll g(ll x, ll y){ while(y){ ll t=x%y; x=y; y=t; } return x; }
int main(int argc, char **argv){
  ll P1=atoll(argv[1]), P2=atoll(argv[2]);
  char *comp=calloc(P2+1,1); for(ll i=2;i*i<=P2;i++) if(!comp[i]) for(ll j=i*i;j<=P2;j+=i) comp[j]=1;
  for(ll p=P1+((5-P1%4)%4); p<=P2; p+=4){ if(p%4!=1||comp[p]) continue;
    ll N1=0, F=0, m0=-1;
    for(ll a=1; 3*a<=p+1; a++) for(ll b=1; 4*a*b<=p+a+b; b++){
      ll ab4=4*a*b; for(ll d=p/ab4+1; ab4*d-p<=a+b; d++){ ll w=ab4*d-p; if((a+b)%w) continue; ll c=(a+b)/w;
        if(b==1) N1++; if(g(a,c)==1) F++; if(m0<0||w<m0) m0=w; } }
    ll e0=0;
    for(ll e=3;e<=199 && !e0;e+=4){ ll H=(p*e+1)/4; for(ll x=H/e+1; x<=2*H/e; x++){ ll num=e*x-H; if(num>0 && (x*H)%num==0){ e0=e; break; } } }
    printf("%lld %lld %lld %lld %lld\n",p,N1,F,m0,e0);
  }
  return 0; }
