// z69 MINE round 2 Part B: test candidate letters c in the three U7 roles, exactly.
// stdin lines: "p n c_1 ... c_n" (p odd prime-ish, c_i >= 1). stdout: "p i role x y z" for every candidate i that yields a
// word (role 0: x = c, 1: y = c, 2: z = c), at most one line per (i, role); then "END p".
//  x-role: divisor d of p+c, d = -1 mod lcm(8,c)          -> word (c, (d+1)/c, (p+c)/d)
//  z-role: divisor e of p+c, e = -1 mod c, 8 | x*y         -> word ((p+c)/e, (e+1)/c, c)
//  y-role: divisor D of c p + 1, D = -1 mod lcm(8,c)        -> word ((D+1)/c, c, (M/D+1)/c)
// Every word is verified with 128-bit arithmetic (x*y*z - x - z == p, 8 | x*y), abort on failure.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 *pr; static int npr;
static u64 gcd(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static int divisors(u64 m,u64 *d,int cap){ int nd=1; d[0]=1;
  for(int i=0;i<npr && pr[i]*pr[i]<=m;i++){u64 q=pr[i]; if(m%q) continue; int e=0; while(m%q==0){m/=q;e++;}
    int cur=nd; u64 pw=1; if(cur*(e+1)>cap) return -1; for(int k=1;k<=e;k++){pw*=q; for(int j=0;j<cur;j++) d[nd++]=d[j]*pw;}}
  if(m>1){ if((u128)pr[npr-1]*pr[npr-1] < m){fprintf(stderr,"factor bound %llu\n",m); exit(2);} if(2*nd>cap) return -1; int cur=nd; for(int j=0;j<cur;j++) d[nd++]=d[j]*m; }
  return nd; }
static void check(u64 p,u64 x,u64 y,u64 z){ u128 v=(u128)x*y*z; if(v - x - z != (u128)p || ((u128)x*y)%8){fprintf(stderr,"BAD word p=%llu (%llu,%llu,%llu)\n",p,x,y,z); exit(3);} }
int main(){
  int LIM=2000000; char *s=calloc(LIM+1,1); pr=malloc(sizeof(u64)*160000);
  for(int i=2;i<=LIM;i++) if(!s[i]){pr[npr++]=i; for(long j=(long)i*i;j<=LIM;j+=i) s[j]=1;}
  static u64 d[200000]; u64 p; int n;
  while(scanf("%llu %d",&p,&n)==2){
    for(int i=0;i<n;i++){ u64 c; if(scanf("%llu",&c)!=1) return 1;
      u64 L = 8/gcd(8,c)*c; u64 N=p+c;
      int nd=divisors(N,d,200000); if(nd<0){fprintf(stderr,"div cap\n"); return 4;}
      int okx=0, okz=0;
      for(int j=0;j<nd;j++){ u64 dd=d[j];
        if(!okx && dd%L==L-1){ u64 x=c,y=(dd+1)/c,z=N/dd; check(p,x,y,z); printf("%llu %d 0 %llu %llu %llu\n",p,i,x,y,z); okx=1; }
        if(!okz && dd%c==(c-1)%c){ u64 x=N/dd, y=(dd+1)/c; if(y>=1 && ((u128)x*y)%8==0){ check(p,x,y,c); printf("%llu %d 2 %llu %llu %llu\n",p,i,x,y,c); okz=1; } }
      }
      // y-role
      u128 M=(u128)c*p+1; if(M>(u128)18000000000000000000ULL){fprintf(stderr,"M overflow\n"); return 5;}
      u64 Mm=(u64)M; u64 sq;
      // exact integer sqrt
      { long double r=sqrtl((long double)Mm); sq=(u64)r; while((u128)sq*sq>M) sq--; while((u128)(sq+1)*(sq+1)<=M) sq++; }
      int oky=0;
      for(u64 D=L-1; D<=sq && !oky; D+=L){ if(Mm%D==0){ u64 x=(D+1)/c, z=(Mm/D+1)/c; check(p,x,c,z); printf("%llu %d 1 %llu %llu %llu\n",p,i,x,c,z); oky=1; } }
      for(u64 E=c-1; E<=sq && !oky; E+=c){ if(E==0) continue; if(Mm%E==0){ u64 D=Mm/E; if(D%L==L-1){ u64 x=(D+1)/c, z=(E+1)/c; check(p,x,c,z); printf("%llu %d 1 %llu %llu %llu\n",p,i,x,c,z); oky=1; } } }
    }
    printf("END %llu\n",p); fflush(stdout);
  }
  return 0;
}
