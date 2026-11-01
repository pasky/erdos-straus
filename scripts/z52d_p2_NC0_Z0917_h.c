// Z0917 helper: class number h(-4p) of the discriminant D=-4p (p prime), by counting reduced primitive-or-not
// binary quadratic forms (a,b,c), b^2-4ac=D, |b|<=a<=c, b>=0 if |b|==a or a==c. (Forms of any content: for D=-4p
// with p prime the only non-primitive possibility is content 2 with D/4 = -p, which is a discriminant only if
// -p = 1 mod 4, so we count primitive forms with gcd(a,b,c)=1.)  Output: p h(-4p)
// Usage: ./z52d_p2_NC0_Z0917_h pmax   (primes p = 1 mod 4 up to pmax)
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static ll gcdll(ll a, ll b){ if(a<0)a=-a; if(b<0)b=-b; while(b){ll t=a%b;a=b;b=t;} return a; }
static ll h_neg4p(ll p){
  ll D = -4*p; ll absD = 4*p; ll h=0;
  for(ll a=1; 3*a*a <= absD; a++){
    for(ll b=-a; b<=a; b++){         // reduced: |b|<=a<=c
      if(b & 1) continue;            // D even => b even
      ll num = b*b - D;              // b^2 + 4p = 4ac
      if(num % (4*a)) continue;
      ll c = num/(4*a);
      if(c < a) continue;
      if((b==a || b==-a || a==c) && b<0) continue;   // Gauss normalisation
      if(gcdll(gcdll(a,b),c)!=1) continue;           // primitive forms
      h++;
    }
  }
  return h;
}
static int isprime_ll(ll n){ if(n<2) return 0; for(ll d=2; d*d<=n; d++) if(n%d==0) return 0; return 1; }
int main(int argc, char **argv){
  ll pmax = atoll(argv[1]);
  for(ll p=3; p<=pmax; p++){ if(p%4!=1 || !isprime_ll(p)) continue; printf("%lld %lld\n", p, h_neg4p(p)); }
  return 0;
}
