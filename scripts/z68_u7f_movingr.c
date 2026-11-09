// z68 U7F §9: for each prime p in a list (stdin, one per line), enumerate ALL U7 witnesses f <= 2p+1
// (f = 7 mod 8, r = (-p mod f) | f+1), factor f by trial division, and report
//   c(f) := f / P^{v_P(f)}  (P = largest prime factor)  -- the "borrowed cofactor"; c = 1 <=> prime power witness
//   omega(f), r, y, z, type (residue mod 8 of the even outer letter of (r, t)).
// Output per prime: p, #witnesses, min c, min c over omega<=2, and the witness list.
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
int main(){
  u64 p;
  while(scanf("%llu",&p)==1){
    u64 minc=~0ULL, minc2=~0ULL, best=0, best2=0; int nw=0;
    printf("p=%llu:",p);
    for(u64 f=7; f<=2*p+1; f+=8){
      u64 r=f-(p%f); if(r==f) continue; if((f+1)%r) continue;
      // factor f
      u64 m=f, P=1, pe=1; int om=0;
      for(u64 q=3;q*q<=m;q+=2){ if(m%q==0){ om++; u64 e=1; while(m%q==0){m/=q;e*=q;} P=q; pe=e; } }
      if(m>1){ om++; P=m; pe=m; }
      u64 c=f/pe; u64 t=(p+r)/f, y=(f+1)/r;
      u64 ev = (r&1)? t : r; int type=ev&7;
      nw++;
      printf(" [f=%llu c=%llu om=%d r=%llu y=%llu z=%llu ty=%d]",f,c,om,r,y,t,type);
      if(c<minc){minc=c;best=f;}
      if(om<=2 && c<minc2){minc2=c;best2=f;}
    }
    printf("\nSUMMARY p=%llu nwit=%d minc=%llu (f=%llu) minc_om2=%llu (f=%llu)\n",p,nw,minc,best,minc2,best2);
  }
  return 0;
}
