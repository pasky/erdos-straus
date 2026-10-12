/* bs_corr_vempty.c: for each n in [N0,N1], decide whether V_I(n) u V_II(n) is empty,
   V_I(n)  = {4abd = n e + 1, a+b = c e},  V_II(n) = {4abd = n + e, a+b = c e}, all >= 1.
   Exhaustive with a<=b (symmetry). Prints n with V empty, plus counts. Early exit.
   Usage: bs_corr_vempty N0 N1 [skip_squares(0/1)] [odd_only(0/1)]                                     */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef long long ll;
static int has_II(ll n){           /* 4a^2 d <= n + 2a ; f=4acd-1 | n+4a^2 d ; b=ce-a >= a */
  for(ll a=1; 4*a*a <= n+2*a; a++)
    for(ll d=1; 4*a*a*d <= n+2*a; d++){
      ll N = n + 4*a*a*d, q = 4*a*d;
      for(ll f = q-1; f <= N; f += q){ if(N % f) continue;
        ll c=(f+1)/q, e=N/f, b=c*e-a; if(b>=a && 4*a*b*d==n+e) return 1; }
    }
  return 0;
}
static int has_I(ll n){            /* 4acd <= 2n+1 ; f=4acd-n>0 , f | 4a^2 d+1 ; b=ce-a>=a */
  for(ll a=1; 4*a <= 2*n+2; a++)
    for(ll d=1; 4*a*d <= 2*n+2; d++){
      ll M = 4*a*a*d+1, q=4*a*d;
      ll c0 = n/q + 1;                       /* f = q c - n > 0 */
      for(ll c=c0; q*c <= 2*n+2; c++){ ll f=q*c-n; if(f> M) break; if(M % f) continue;
        ll e=M/f, b=c*e-a; if(b>=a && 4*a*b*d==n*e+1) return 1; }
    }
  return 0;
}
int main(int argc,char**argv){
  ll N0=atoll(argv[1]), N1=atoll(argv[2]); int skipsq = argc>3?atoi(argv[3]):1; int oddonly = argc>4?atoi(argv[4]):0;
  ll empt=0, tested=0;
  for(ll n=N0;n<=N1;n++){
    ll r=(ll)llround(sqrtl((long double)n)); int sq=(r*r==n);
    if(sq && skipsq) continue;
    if(oddonly && n%2==0) continue;
    tested++;
    if(has_II(n)||has_I(n)) continue;
    empt++; printf("EMPTY n=%lld%s\n", n, sq?" (square)":"");
  }
  printf("tested=%lld empty=%lld\n",tested,empt);
  return 0;
}
