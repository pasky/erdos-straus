/* R180: from-scratch recomputation of Cor 4.4 (LORENZINI_W).
   M = 151351200. Mark n in [0,3M) certified by a fixed-pair family of modulus d | M with n >= its size threshold.
   U_M := classes of unmarked n in [2M,3M) (all thresholds <= 2M). Then list unmarked n < 2M whose class is NOT in U_M
   and check (W) for them by direct search. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef long long ll;
static const ll M = 151351200LL;
int main(void){
  ll L = 3*M; unsigned char *mk = calloc(L,1); if(!mk){puts("oom");return 1;}
  ll writes=0, nfam=0;
  for (ll d=3; d<=M; d++){ if (M%d) continue;
    /* (x,y): xy = d+1 */
    for (ll x=2; x*x<=d+1 || x<=(d+1)/2; x++){ if ((d+1)%x) continue; ll y=(d+1)/x; if (y<2) break;
      ll c=((-x)%d+d)%d, thr=2*d-x; ll n=c; if(n<thr) n+=((thr-n+d-1)/d)*d;
      for(;n<L;n+=d){mk[n]=1;writes++;} nfam++; }
    /* (x,z): xz = d */
    for (ll x=2; x<=d/2; x++){ if (d%x) continue; ll z=d/x; if (z<2) break;
      ll c=((-(x+z))%d+d)%d, thr=2*d-x-z; ll n=c; if(n<thr) n+=((thr-n+d-1)/d)*d;
      for(;n<L;n+=d){mk[n]=1;writes++;} nfam++; }
  }
  unsigned char *inU = calloc(M,1); ll U=0;
  for (ll n=2*M;n<3*M;n++) if(!mk[n]){inU[n-2*M]=1;U++;}
  printf("families %lld writes %lld |U_M| = %lld density %.3e\n",nfam,writes,U,(double)U/M);
  /* mod 12 projection */
  int p12[12]={0}; for(ll r=0;r<M;r++) if(inU[r]) p12[r%12]=1;
  printf("U_M mod 12:"); for(int i=0;i<12;i++) if(p12[i]) printf(" %d",i); puts("");
  /* small n not in U_M and not marked */
  ll cnt=0;
  for (ll n=2;n<2*M;n++){ if(mk[n]||inU[n%M]) continue;
    /* direct (W) search: exists x>=2, d=xy-1>=2x-1 with d | n+x, (n+x)/d>=2 */
    int ok=0;
    for (ll x=2; !ok && 2*(2*x-1)<=n+x; x++){
      for (ll y=2; ; y++){ ll d=x*y-1; if (2*d>n+x) break; if((n+x)%d==0){ok=1;break;} } }
    if(!ok){ printf("non-value outside U_M: %lld\n",n); cnt++; }
  }
  printf("done; non-values outside U_M below 2M: %lld\n",cnt);
  return 0;
}
