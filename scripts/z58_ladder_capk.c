// z58 LADDER: exponent-cap ladder.  R^(k)(n) := #{d = 3 (4), 3 <= d <= (4n+1)/3 : r = (-n mod d) >= 1, r | m^k, m = (d+1)/4}.
// k = 1 is R(n) (Lemma A.1);  k >= 2 is the cap relaxation (rad(r) | m and v_l(r) <= k v_l(m)).  Prints R^(1..4) and R^(inf).
// Usage: z58_ladder_capk n1 n2 ...
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static u64 g(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static int divpow(u64 r,u64 m,int k){ // r | m^k ?  (k<=0 means k = infinity: rad(r) | m)
  for(int i=0; k<=0 || i<k; i++){ if(r==1) return 1; u64 h=g(r,m); if(h==1) return 0; r/=h; } return r==1; }
int main(int argc,char**argv){
  for(int a=1;a<argc;a++){ u64 n=strtoull(argv[a],0,10); u64 c[5]={0}; u64 first2=0;
    for(u64 d=3; 3*d<=4*n+1; d+=4){ u64 r=(d-n%d)%d; if(!r) continue; u64 m=(d+1)/4;
      for(int k=1;k<=4;k++) if(divpow(r,m,k)){ c[k]++; if(k==2&&!first2) first2=d; }
      if(divpow(r,m,0)) c[0]++; }
    printf("%llu R1=%llu R2=%llu R3=%llu R4=%llu Rinf=%llu first_d_k2=%llu\n",n,c[1],c[2],c[3],c[4],c[0],first2); }
  return 0; }
