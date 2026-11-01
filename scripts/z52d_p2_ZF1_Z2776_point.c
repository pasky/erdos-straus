// z52d Pass-2 ZF1/S6 item Z2776: is the profinite limit point (A at all primes != 3, D3 in Z_3) of an exponential family
// c*3^k+d in some I3 word class (E: uv | n+u+v; L: (tu-1) | n+u; u,v,t >= 3) with modulus <= M?  Usage: prog A D3 M
// test whether profinite point P (value A at primes != 3, value D3 in Z_3) lies in some I3 word class with modulus <= M
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static ll mod(ll a, ll m){ a%=m; return a<0?a+m:a; }
int main(int argc,char**argv){ ll A=atoll(argv[1]), D3=atoll(argv[2]), M=atoll(argv[3]); int found=0;
  // E words: m=uv; condition n ≡ -(u+v) mod m ; split m=3^a w
  for(ll u=3;u*u<=M;u++) for(ll v=u;u*v<=M;v++){ ll m=u*v, w=m, q=1; while(w%3==0){w/=3;q*=3;}
    if(mod(A+u+v,w)==0 && mod(D3+u+v,q)==0){ printf("E u=%lld v=%lld m=%lld\n",u,v,m); if(++found>5) return 0; } }
  for(ll t=3;3*t-1<=M;t++) for(ll u=3;t*u-1<=M;u++){ ll m=t*u-1, w=m, q=1; while(w%3==0){w/=3;q*=3;}
    if(mod(A+u,w)==0 && mod(D3+u,q)==0){ printf("L t=%lld u=%lld m=%lld\n",t,u,m); if(++found>5) return 0; } }
  if(!found) printf("none up to %lld\n",M); return 0; }
