// z55 CROSSO: exact R_F(n) for the Theorem U family via Lemma 4.1 (loop over the free variable w).
// usage: z55_crosso_R n U0 U1 Y X [v]   (prints n R hits; v=1 prints each hit u w C)
// R_F = 2 #{ w in (Y,X] : r=(-n mod w) in U (sqfree, =1 mod 4, U0<r<=U1), w odd sqfree, gcd(w, r n)=1,
//             ceil(n/w) = -2 mod 8r }.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef __int128 i128;
static int sqfree(u64 x){ for(u64 q=2;q*q<=x;q++){ if(x%q==0){ x/=q; if(x%q==0) return 0; } } return 1; }
static u64 gcd(u64 a,u64 b){ while(b){u64 t=a%b;a=b;b=t;} return a; }
int main(int argc,char**argv){
  if(argc<6){fprintf(stderr,"usage\n");return 1;}
  u64 n=strtoull(argv[1],0,10),U0=strtoull(argv[2],0,10),U1=strtoull(argv[3],0,10),Y=strtoull(argv[4],0,10),X=strtoull(argv[5],0,10);
  int v=argc>6?atoi(argv[6]):0;
  long R=0;
  for(u64 w=Y+1; w<=X; w++){
    if(!(w&1)) continue;
    u64 r=(w - n%w)%w; if(r<=U0||r>U1||(r&3)!=1) continue;
    u64 m=(n+r)/w; // = ceil(n/w)
    if((m+2)%(8*r)) continue;
    if(gcd(w,r)!=1||gcd(w,n)!=1||!sqfree(w)||!sqfree(r)) continue;
    R+=2; if(v) printf("hit u=%llu w=%llu C=%llu\n",r,w,(m+2)/(8*r));
  }
  printf("%llu %ld\n",n,R);
  return 0;
}
