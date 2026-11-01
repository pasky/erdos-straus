// Z2859 ("Chowla for (.|p) along words" cell): for primes p = 1 (8), enumerate interior length-3 words
// p = mcs - c - s (c,m,s >= 2), A = ms - 1 (DEDEKIND_ES: p/A = [[c,m,s]]), and the signs (A/p).
// Output per prime: p |L3| N- (N- = # words with (A/p) = -1).
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static int jacobi(ll a, ll n){ int r=1; a%=n; if(a<0)a+=n; while(a){ while(!(a&1)){ a>>=1; ll t=n&7; if(t==3||t==5) r=-r; } ll t=a;a=n;n=t; if((a&3)==3&&(n&3)==3) r=-r; a%=n; } return n==1?r:0; }
static int isprime(ll n){ if(n<2)return 0; for(ll d=2;d*d<=n;d++) if(n%d==0) return 0; return 1; }
int main(int argc,char**argv){ ll p0=atoll(argv[1]), p1=atoll(argv[2]);
  for(ll p=p0;p<=p1;p++){ if(p%8!=1||!isprime(p)) continue; ll L=0,Nm=0;
    for(ll s=2; 2*s-1<=p; s++) for(ll m=2; ; m++){ ll A=m*s-1; if(2*A>p+s) break; if((p+s)%A) continue; ll c=(p+s)/A; if(c<2) continue; L++; if(jacobi(A,p)==-1) Nm++; }
    printf("%lld %lld %lld\n",p,L,Nm); }
  return 0; }
