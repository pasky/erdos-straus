/* R128: independent brute-force f_II(n) = #{ordered (x,y,z): 4/n=1/x+1/y+1/z, n|y, n|z, gcd(x,n)=1}.
   Enumerate sorted s1<=s2<=s3 (s1 in (n/4,3n/4], s2 in [s1, 2B/A]), then all distinct permutations. */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static u64 gcd(u64 a,u64 b){while(b){u64 t=a%b;a=b;b=t;}return a;}
static int t2(u64 x,u64 y,u64 z,u64 n){return gcd(x,n)==1 && y%n==0 && z%n==0;}
int main(int argc,char**argv){ int N=atoi(argv[1]);
 for(int n=2;n<=N;n++){ u64 cnt=0;
  for(u64 s1=n/4+1; 4*s1<=3*(u64)n; s1++){
   u64 A=4*s1-n, B=(u64)n*s1; u64 y0=(B+A-1)/A; if(y0*A==B) y0++; if(y0<s1) y0=s1;
   for(u64 s2=y0; s2*A<=2*B; s2++){ u64 den=A*s2-B; u128 num=(u128)B*s2; if(num%den) continue;
     u64 s3=(u64)(num/den); if(s3<s2) continue;
     u64 P[6][3]={{s1,s2,s3},{s1,s3,s2},{s2,s1,s3},{s2,s3,s1},{s3,s1,s2},{s3,s2,s1}};
     for(int i=0;i<6;i++){ int dup=0; for(int j=0;j<i;j++) if(P[j][0]==P[i][0]&&P[j][1]==P[i][1]&&P[j][2]==P[i][2]) dup=1;
       if(!dup && t2(P[i][0],P[i][1],P[i][2],n)) cnt++; } } }
  printf("%d %llu\n",n,cnt);} return 0;}
