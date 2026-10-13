/* bsG_dev: is the single-prime deviation nu(l,c) (nu = -1 at every prime q != l, nu = c in Z_l, c >= 0 an integer)
   covered by a fixed-pair family with modulus <= D?
   (x,y): d=xy-1 | nu+x  <=>  d_{l'} | x-1  and  l^{v_l(d)} | c+x
   (x,z): xz | nu+x+z    <=>  (xz)_{l'} | x+z-1  and  l^{v_l(xz)} | c+x+z
   usage: bsG_dev l cmax D   -> prints c values (0..cmax) NOT covered, else first witness
   gcc -O2 -o /tmp/bsG_dev scripts/bsG_dev.c */
#include <stdio.h>
#include <stdlib.h>
typedef long long ll;
static ll lpart(ll d, ll l, ll *rest){ ll p=1; while(d%l==0){ d/=l; p*=l; } *rest=d; return p; }
int main(int argc,char**argv){ ll l=atoll(argv[1]), cmax=atoll(argv[2]), D=atoll(argv[3]); int verbose=argc>4;
  for(ll c=0;c<=cmax;c++){ int found=0; ll wx=0,wy=0; char typ='-';
    for(ll x=2; !found && 2*x-1<=D; x++){
      for(ll y=2; x*y-1<=D; y++){ ll d=x*y-1, r; ll lp=lpart(d,l,&r);
        if((x-1)%r==0 && (c+x)%lp==0){ found=1; wx=x; wy=y; typ='Y'; break; } }
      if(found) break;
      for(ll z=2; x*z<=D; z++){ ll m=x*z, r; ll lp=lpart(m,l,&r);
        if((x+z-1)%r==0 && (c+x+z)%lp==0){ found=1; wx=x; wy=z; typ='Z'; break; } } }
    if(!found) printf("l=%lld c=%lld UNCOVERED (D=%lld)\n",l,c,D);
    else if(verbose) printf("l=%lld c=%lld covered by %c (%lld,%lld)\n",l,c,typ,wx,wy); }
  return 0; }
