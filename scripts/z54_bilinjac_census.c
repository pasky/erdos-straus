/* z54 BILINJAC census of the balanced block.
   For every n <= X: Nbal(n) := #{(u,B,C) in N^3 : 4uBC - u - B = n, n^{1/4}/2 < u, B <= 2 n^{1/4}}.
   (union of the O(1) dyadic blocks around the balanced block; ordered triples.)
   Enumerates all (u,B,C) with u,B <= 2 X^{1/4}; total work ~ O(X).
   Output: histogram of Nbal over (a) all odd n, (b) primes p = 1 mod 24, (c) odd squares; max and argmax.
   usage: census X */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
typedef long long ll;
int main(int argc,char**argv){
  ll X=atoll(argv[1]);
  uint8_t *cnt=calloc(X+1,1); if(!cnt){fprintf(stderr,"oom\n");return 1;}
  ll umax=(ll)(2*pow((double)X,0.25))+2;
  for(ll u=1;u<=umax;u++) for(ll B=1;B<=umax;B++){
    /* n = 4uBC-u-B ; need n^{1/4}/2 < u <= 2 n^{1/4}, same for B: n in [max(u,B)^4/16, 16 min(u,B)^4) */
    ll mx=u>B?u:B, mn=u<B?u:B;
    double lo=pow((double)mx,4)/16.0, hi=16.0*pow((double)mn,4);
    if(lo>=hi) continue;
    ll C0=(ll)((lo+u+B)/(4.0*u*B))-1; if(C0<1) C0=1;  /* float start, widened by one step */
    for(ll C=C0;;C++){ ll n=4*u*B*C-u-B; if(n>X) break; if((double)n>=hi+16) break; /* float range only prunes; membership is the exact test below */ if(n<1) continue;
      /* exact integer test: n^{1/4}/2 < x <= 2 n^{1/4}  <=>  n < 16 x^4  and  x^4 <= 16 n   (x = u, B) */
      ll mn4=mn*mn*mn*mn, mx4=mx*mx*mx*mx;
      if(n < 16*mn4 && mx4 <= 16*n){ if(cnt[n]==255){fprintf(stderr,"counter saturation at n=%lld\n",n);return 3;} cnt[n]++; }
    }
  }
  /* sieve primes */
  uint8_t *comp=calloc(X+1,1); for(ll i=2;i*i<=X;i++) if(!comp[i]) for(ll j=i*i;j<=X;j+=i) comp[j]=1;
  ll hall[256]={0}, hp[256]={0}, hs[256]={0}; ll mall=0,amall=0,mp=0,amp=0,ms=0,ams=0;
  for(ll n=3;n<=X;n+=2){ int c=cnt[n]; hall[c]++; if(c>mall){mall=c;amall=n;}
    if(!comp[n] && n%24==1){ hp[c]++; if(c>mp){mp=c;amp=n;} } }
  for(ll m=3;m*m<=X;m+=2){ ll n=m*m; int c=cnt[n]; hs[c]++; if(c>ms){ms=c;ams=n;} }
  printf("X=%lld  Nbal(n) = #{(u,B,C): 4uBC-u-B=n, n^(1/4)/2 < u,B <= 2n^(1/4)}\n",X);
  printf("max over odd n: %lld at n=%lld (n^(1/4)=%.1f); over primes =1 mod 24: %lld at %lld; over odd squares: %lld at %lld\n",mall,amall,pow((double)amall,0.25),mp,amp,ms,ams);
  printf("value  #odd n  #primes1mod24  #oddsquares\n");
  for(int c=0;c<256;c++) if(hall[c]||hp[c]||hs[c]) printf("%3d %12lld %12lld %8lld\n",c,hall[c],hp[c],hs[c]);
  /* by decade: max over odd n in [10^j,10^{j+1}) */
  for(ll lo=1000;lo<X;lo*=10){ ll hi=lo*10>X?X:lo*10; int m=0; ll am=0; double s=0; ll k=0; for(ll n=lo+1-(lo%2==0?0:1);n<=hi;n+=2){ if(n%2==0) continue; if(cnt[n]>m){m=cnt[n];am=n;} s+=cnt[n]; k++; }
    printf("decade [%lld,%lld]: max Nbal=%d at n=%lld (n^(1/4)=%.1f), mean=%.4f\n",lo,hi,m,am,pow((double)am,0.25),s/k); }
  return 0;
}
