// z50 ajopus: per-shift (independent-shift) prediction of the chain deficit for the prime U family.
// For each shift v in V (v ≡ 0 (4) or 7 (8)), v <= vmax, sieve I = {n<=N, n ≡ 1 (8)} by the events
// l | n+v, l prime ≡ -1 (mod v), l <= z, l < n+v (proper), and compare with the Haar product prod(1-1/l).
// Output: sum over v of [log(actual_v) - log(model_v)]  (positive = more survivors than Haar), cumulative by v.
// Usage: pershift N z vmax
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef long long ll;
int main(int argc,char**argv){ ll N=atoll(argv[1]), z=atoll(argv[2]), vmax=atoll(argv[3]);
  ll K=(N-1)/8+1; unsigned char *al=malloc(K); char *comp=calloc(z+2,1);
  for(ll i=2;i*i<=z;i++) if(!comp[i]) for(ll j=i*i;j<=z;j+=i) comp[j]=1;
  double tot=0;
  for(ll v=3; v<=vmax; v++){ if(!(v%4==0 || v%8==7)) continue;
    memset(al,1,K); al[0]=0; ll nal=K-1; double lm=0;
    for(ll l=v-1; l<=z; l+=v){ if(l<3||comp[l]) continue;
      lm += log1p(-1.0/l);
      ll inv8; { ll b=8%l,e=l-2,r=1; while(e){ if(e&1) r=r*b%l; b=b*b%l; e>>=1;} inv8=r; }
      ll c=((-v)%l+l)%l; ll k0=((c-1)%l+l)%l*inv8%l; ll excl=-1; if(v<l){ ll n0=l-v; if(n0%8==1) excl=(n0-1)/8; }
      for(ll k=k0;k<K;k+=l){ if(k==excl) continue; if(al[k]){al[k]=0; nal--;} } }
    double d = log((double)nal/(K-1)) - lm; tot += d;
    if(v<=64 || v%256==0 || v==vmax) printf("v=%lld dev=%.5f cum=%.5f\n",v,d,tot);
  }
  printf("TOTAL per-shift deviation (log actual - log Haar) = %.5f\n",tot); return 0; }
