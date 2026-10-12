/* bs_corr_count_twin.c: bs_corr_count.c plus the numbers of Type I / II solutions on twin slices
   e^2 = 1 (mod 4ab); output "n fI fII twinI twinII".  Derived from bs_corr_count.c: exact counts f_I(n), f_II(n) of V_I(n), V_II(n) with a<=b (same enumeration
   as bs_corr_vempty.c, without early exit).  Reads n from stdin, prints "n fI fII".          */
#include <stdio.h>
typedef long long ll; static ll tw1, tw2;
static ll cnt_II(ll n){ ll s=0;
  for(ll a=1; 4*a*a <= n+2*a; a++) for(ll d=1; 4*a*a*d <= n+2*a; d++){
    ll N=n+4*a*a*d, q=4*a*d;
    for(ll f=q-1; f<=N; f+=q){ if(N%f) continue; ll c=(f+1)/q,e=N/f,b=c*e-a;
      if(b>=a && 4*a*b*d==n+e){ s++; if((e*e-1)%(4*a*b)==0) tw2++; } } }
  return s; }
static ll cnt_I(ll n){ ll s=0;
  for(ll a=1; 4*a <= 2*n+2; a++) for(ll d=1; 4*a*d <= 2*n+2; d++){
    ll M=4*a*a*d+1, q=4*a*d;
    for(ll c=n/q+1; q*c <= 2*n+2; c++){ ll f=q*c-n; if(f>M) break; if(M%f) continue;
      ll e=M/f,b=c*e-a; if(b>=a && 4*a*b*d==n*e+1){ s++; if((e*e-1)%(4*a*b)==0) tw1++; } } }
  return s; }
int main(){ ll n; while(scanf("%lld",&n)==1){ tw1=tw2=0; ll I=cnt_I(n), II=cnt_II(n); printf("%lld %lld %lld %lld %lld\n",n,I,II,tw1,tw2);} return 0; }
