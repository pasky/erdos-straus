/* bsG_devT: multi-prime deviations nu(T,c): nu = c (integer >= 0) at primes of T = {primes <= P}, nu = -1 at all other primes.
   (x,y): d=xy-1 | nu+x <=> d_T | c+x and d_{T'} | x-1 ;  (x,z): m=xz | nu+x+z <=> m_T | c+x+z and m_{T'} | x+z-1.
   usage: bsG_devT P cmax D  -> prints uncovered c (moduli <= D). gcc -O2 -o /tmp/bsG_devT scripts/bsG_devT.c */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static int P; static int isT(ll p){ return p<=P; }
static ll tpart(ll d){ ll t=1; for(ll p=2;p<=P;p++){ int pr=1; for(ll q=2;q*q<=p;q++) if(p%q==0){pr=0;break;} if(!pr) continue; while(d%p==0){ d/=p; t*=p; } } return t; }
int main(int argc,char**argv){ P=atoi(argv[1]); ll cmax=atoll(argv[2]), D=atoll(argv[3]);
  ll *tp=malloc(sizeof(ll)*(D+2)); for(ll d=1; d<=D+1; d++) tp[d]=tpart(d);
  int unc=0;
  for(ll c=0;c<=cmax;c++){ int found=0;
    for(ll x=2; !found && 2*x-1<=D; x++){
      for(ll y=2; x*y-1<=D; y++){ ll d=x*y-1, t=tp[d], r=d/t; if((x-1)%r==0 && (c+x)%t==0){ found=1; break; } }
      if(found) break;
      for(ll z=2; x*z<=D; z++){ ll m=x*z, t=tp[m], r=m/t; if((x+z-1)%r==0 && (c+x+z)%t==0){ found=1; break; } } }
    if(!found){ unc++; if(unc<=30) printf(" %lld",c); } }
  printf("\nP=%d: %d uncovered c in [0,%lld] (D=%lld)\n",P,unc,cmax,D); return 0; }
