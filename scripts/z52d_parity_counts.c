/* z52d PARITY lane (C3 falsifier): per-prime certificate counts and h(-4p) for primes p = 1 (mod 24), p <= X.
   Output (one line per prime):  p nE nB r4 nEA fII h mis
     nE  = #edges {u,v} (u<v) of the word forest F_p: uv | p+u+v   (so |X(p)| = 2 nE + 1, the extra word is (p+2,1,1))
     nB  = #bichromatic edges: (u/p)(v/p) = -1                      (= five-slice ES certificates, FOREST_* memos)
     r4  = #edges with 4 | t, t = (p+u+v)/(uv)                      (= R(p)/2, the (*) count of PARITY_AUDIT / J6)
     nEA = |E(p)| = #ordered words (t,u,v) in X(p) with 4 | tu-1   (INVOLUTION_ES ES part)
     fII = ordered Type II count #{(a,b,c,d): 4abcd = a+b+pc, gcd(a,c)=1} (weight 2 if b>a, 1 if b=a),
           same enumeration as scripts/bs_prob_fII.c
     h   = h(-4p), number of reduced forms (a,2b',c), ac - b'^2 = p
     mis = #edges where [bichromatic] != [4 divides a slot in {t,u,v,tu-1,tv-1}]   (must be 0, PROVED identity)
   Build: gcc -O2 -o /tmp/z52d_parity_counts scripts/z52d_parity_counts.c -lm
   Usage: z52d_parity_counts X [X0] > out.txt   (primes p in [X0, X]; memory ~ 5.4 X + 4 (X-X0) bytes) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef long long ll;
static uint32_t *spf; static ll SMAX;
static ll gcdl(ll x, ll y){ while(y){ ll t=x%y; x=y; y=t;} return x; }
static int jacobi(ll a, ll n){ /* n odd positive */
  int s=1; a%=n; if(a<0) a+=n;
  while(a){ while(!(a&1)){ a>>=1; ll r=n&7; if(r==3||r==5) s=-s; }
    ll t=a; a=n; n=t; if((a&3)==3 && (n&3)==3) s=-s; a%=n; }
  return n==1 ? s : 0; }
static ll dv[1<<16];
static int divisors(ll N){ /* all divisors of N (N < SMAX) into dv, returns count */
  int nd=1; dv[0]=1;
  while(N>1){ ll q=spf[N]; int e=0; while(N%q==0){ N/=q; e++; }
    int cur=nd; ll pw=1; for(int k=1;k<=e;k++){ pw*=q; for(int j=0;j<cur;j++) dv[nd++]=dv[j]*pw; } }
  return nd; }
int main(int argc, char **argv){
  ll X = atoll(argv[1]); ll X0 = argc > 2 ? atoll(argv[2]) : 0; if(X0 < 1) X0 = 1;
  SMAX = (4*X)/3 + 2*(ll)sqrt((double)X) + 64;
  spf = calloc(SMAX+1, 4);
  for(ll i=2;i<=SMAX;i++) if(!spf[i]){ for(ll j=i;j<=SMAX;j+=i) if(!spf[j]) spf[j]=(uint32_t)i; }
  uint32_t *cnt = calloc(X-X0+1, 4);
  for(ll a=1; 4*a*a <= X+2*a; a++)
    for(ll d=1; 4*a*a*d <= X + 2*a; d++){
      for(ll c=1; ; c++){
        ll f = 4*a*c*d - 1;
        ll e0 = (2*a + c - 1)/c;
        ll p0 = e0*f - 4*a*a*d;
        if(p0 > X) { if(e0==1) break; else continue; }
        if(gcdl(a,c)!=1) continue;
        ll e1 = e0; if(p0 < X0) e1 = (X0 + 4*a*a*d + f - 1)/f; if(e1 < e0) e1 = e0;
        for(ll e=e1, p=e1*f-4*a*a*d; p<=X; e++, p+=f){ ll b = c*e - a; cnt[p-X0] += (b==a)?1:2; }
      }}
  ll pst = 25; if(X0 > pst) pst = X0 + ((25 - X0 % 24) % 24 + 24) % 24;
  for(ll p=pst; p<=X; p+=24){
    if(spf[p]!=p) continue;
    ll nE=0,nB=0,r4=0,nEA=0,mis=0;
    ll umax = 1 + (ll)sqrt((double)(p+1)) + 1;
    for(ll u=1; u<=umax; u++){
      int nd = divisors(p+u);
      for(int j=0;j<nd;j++){ ll v=dv[j]; if(v<=u) continue;
        if((p+u+v)%(u*v)) continue;
        ll t=(p+u+v)/(u*v);
        nE++;
        int bi = jacobi(u,p)*jacobi(v,p) == -1;
        nB += bi;
        if(t%4==0) r4++;
        if((t*u-1)%4==0) nEA++;
        if((t*v-1)%4==0) nEA++;
        int slot = (t%4==0)||(u%4==0)||(v%4==0)||((t*u-1)%4==0)||((t*v-1)%4==0);
        if(slot!=bi) mis++;
      }
    }
    ll h=0;
    for(ll b=0; 3*b*b <= p; b++){
      ll N=p+b*b; int nd=divisors(N);
      for(int j=0;j<nd;j++){ ll a=dv[j], c=N/a; if(a<2*b || a>c) continue;
        h++; if(b>0 && 2*b<a && a<c) h++; }
    }
    printf("%lld %lld %lld %lld %lld %u %lld %lld\n", p,nE,nB,r4,nEA,cnt[p-X0],h,mis);
  }
  return 0;
}
