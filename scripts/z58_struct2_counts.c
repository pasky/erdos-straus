// z58 STRUCT2: exact N_II(n) = #{(a,b,c,d) in N^4 : 4abcd = a+b+nc} (ordered) for all n ≡ 1 (mod 4) in [lo, hi),
// via the (a,b)-loop 4abd = n + e, e | a+b, c = (a+b)/e (at most one e per (a,b): e = -n mod 4ab).  Also prints the
// c = 1 count R(n) and the number of solutions with gcd(abd, n) = 1 ("coprime", genuine ET Type II).
// Output: n N_II R_c1 N_cop
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static u64 g(u64 x,u64 y){while(y){u64 t=x%y;x=y;y=t;}return x;}
int main(int argc,char**argv){
  if(argc<3){fprintf(stderr,"usage: counts lo hi\n");return 1;}
  u64 lo=strtoull(argv[1],0,10),hi=strtoull(argv[2],0,10);
  if(hi>2000000000ULL){fprintf(stderr,"hi too large\n");return 1;}
  u64 n0=lo; while(n0%4!=1) n0++;
  for(u64 n=n0;n<hi;n+=4){ u64 N=0,R=0,Cp=0;
    for(u64 a=1;4*a<=n+a+1;a++) for(u64 b=1;;b++){ u64 q=4*a*b; if(q>n+a+b) break; u64 e=(q-n%q)%q;
      if(e==0||e>a+b||(a+b)%e) continue; N++; if(e==a+b) R++; u64 d=(n+e)/q; if(g(a*b*d,n)==1) Cp++; }
    printf("%llu %llu %llu %llu\n",n,N,R,Cp); }
  return 0; }
