// y8_smooth: for primes p = 1 (4) given on stdin, enumerate all positive words (t,u,v) of X_p
// (tuv-u-v=p), A=tu-1, A*=tv-1, chi=(A/p) (Legendre; equals (-A/p) for p=1 mod 4).
// Output: p lnr N Nm S Sm R Rm F Fm  (F: "split-free" words: the (lnr-1)-rough part of A is 1 or all of the rough part of tp+1 — forced +; Fm must be 0)
// earlier fields:   (R/Rm: words with neither A nor A* Y-smooth, Y = argv[1] (default 100), and their chi=-1 count)  where S = #words with A or A* (lnr-1)-smooth ("forced +"), Sm = #those with chi=-1 (must be 0).
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static ll pw(ll b, ll e, ll m){ll r=1;b%=m;while(e){if(e&1)r=(__int128)r*b%m;b=(__int128)b*b%m;e>>=1;}return r;}
static int leg(ll a, ll p){a%=p; if(a<0)a+=p; if(!a) return 0; return pw(a,(p-1)/2,p)==1?1:-1;}
static ll rough(ll a, ll B){ for(ll q=2;q<B;q++) while(a%q==0) a/=q; return a; } // (B-1)-rough part
static int smooth(ll a, ll B){ // all prime factors < B
  for(ll q=2;q<B && q*q<=a;q++) while(a%q==0) a/=q;
  if(a==1) return 1;
  // remaining a: if a < B and prime factors removed... check a's factors all < B
  for(ll q=2;q<B;q++){ while(a%q==0) a/=q; if(a==1) return 1; }
  return a==1;
}
int main(int argc,char**argv){
  ll p; ll Y=argc>1?atoll(argv[1]):100;
  while(scanf("%lld",&p)==1){
    ll lnr=2; while(leg(lnr,p)==1) lnr++; // least non-residue (prime automatically)
    ll N=0,Nm=0,S=0,Sm=0,R=0,Rm=0,F=0,Fm=0;
    for(ll t=1;t<=p+2;t++)
      for(ll u=1; u <= (t==1 ? p+2 : (p+1)/(t-1)); u++){ // A<=p+u <=> (t-1)u<=p+1
        ll A=t*u-1; if(A<=0) continue;
        if((p+u)%A) continue;
        ll v=(p+u)/A; if(v<1) continue;
        ll As=t*v-1;
        int c=leg(A,p); N++; if(c<0) Nm++;
        if(smooth(A,lnr)||smooth(As,lnr)){S++; if(c<0) Sm++;}
        { ll rA=rough(A,lnr), rN=rough(As,lnr)*rA; if(rA==1||rA==rN){F++; if(c<0) Fm++;} }
        if(!smooth(A,Y+1)&&!smooth(As,Y+1)){R++; if(c<0) Rm++;}
      }
    printf("%lld %lld %lld %lld %lld %lld %lld %lld %lld %lld\n",p,lnr,N,Nm,S,Sm,R,Rm,F,Fm);
    fflush(stdout);
  }
}
