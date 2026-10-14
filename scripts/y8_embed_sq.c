// y8_embed_sq: "three-squares SQ" for composite n. For odd n <= N, count words w of X_n (tuv-u-v=n) with
// Diff(T_w) != {2}, i.e. some odd prime l with v_l(n) odd and (-A/l) = -1 (A = tu-1) -- equivalently (TWO_FIBRES Thm A)
// n*G_w is NOT a Gram matrix of three integer vectors. Prints non-square n = 1 (mod 4) where every word embeds (E = 0),
// plus summary. usage: y8_embed_sq N
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static int jac(ll a, ll n){ a%=n; if(a<0)a+=n; int r=1; while(a){ while(!(a&1)){a>>=1; ll m=n&7; if(m==3||m==5) r=-r;} ll t=a;a=n;n=t; if((a&3)==3&&(n&3)==3) r=-r; a%=n;} return n==1?r:0; }
int main(int argc,char**argv){
  ll N=atoll(argv[1]);
  int *spf=calloc(N+1,sizeof(int));
  for(ll i=2;i<=N;i++) if(!spf[i]) for(ll j=i;j<=N;j+=i) if(!spf[j]) spf[j]=i;
  // odd-exponent primes of n
  ll *E=calloc(N+1,sizeof(ll)), *W=calloc(N+1,sizeof(ll));
  for(ll t=1;t<=N+2;t++)
    for(ll u=1; u <= (t==1 ? N+2 : (N+1)/(t-1)); u++){
      ll A=t*u-1; if(A<=0) continue;
      for(ll v=1;;v++){
        ll n=A*v-u; if(n>N) break; if(n<1||!(n&1)) continue;
        W[n]++;
        ll m=n; int bad=0;
        while(m>1){ ll l=spf[m]; int e=0; while(m%l==0){m/=l;e++;} if((e&1) && jac(-A,l)==-1){bad=1;break;} }
        if(bad) E[n]++;
      }
    }
  ll cnt=0;
  for(ll n=1;n<=N;n+=2){
    ll r=(ll)sqrtl((long double)n); while(r*r>n) r--; while((r+1)*(r+1)<=n) r++;
    int sq=(r*r==n);
    if(sq && E[n]) printf("SQUARE WITH NON-EMBEDDABLE WORD %lld\n",n);
    if(!sq && E[n]==0){ cnt++; printf("all-embeddable non-square n=%lld (n mod 4=%lld, words=%lld)\n",n,n%4,W[n]); }
  }
  printf("N=%lld: non-squares with every word Z^3-embeddable: %lld\n",N,cnt);
}
