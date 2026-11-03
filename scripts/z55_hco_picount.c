// z55 HCO: independent-ish check of the census prime enumeration: count primes = 1, 3 (mod 4) below B with the same
// segmented sieve as z55_hco_census.c, for comparison with the known pi(10^12) = 37 607 912 018.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>
typedef unsigned long long u64;
int main(int argc,char**argv){ u64 A=strtoull(argv[1],0,10),B=strtoull(argv[2],0,10);
  u64 sq=1; while(sq*sq<B) sq++; char*cs=calloc(sq+1,1); int*bp=malloc(sizeof(int)*(sq+1)); int nbp=0;
  for(u64 i=2;i<=sq;i++) if(!cs[i]){ bp[nbp++]=i; for(u64 j=i*i;j<=sq;j+=i) cs[j]=1; }
  const u64 SEG=1ULL<<22; u64 nseg=(B-A+SEG-1)/SEG; long c1=0,c3=0,c2=0;
  #pragma omp parallel reduction(+:c1,c3,c2)
  { char*sv=malloc(SEG);
    #pragma omp for schedule(dynamic,1)
    for(u64 s=0;s<nseg;s++){ u64 lo=A+s*SEG, hi=lo+SEG; if(hi>B) hi=B; memset(sv,0,hi-lo);
      for(int i=0;i<nbp;i++){ u64 q=bp[i]; if(q*q>=hi) break; u64 st=((lo+q-1)/q)*q; if(st<q*q) st=q*q; for(u64 j=st;j<hi;j+=q) sv[j-lo]=1; }
      for(u64 p=lo;p<hi;p++){ if(p<2||sv[p-lo]) continue; if((p&3)==1) c1++; else if((p&3)==3) c3++; else c2++; } }
    free(sv); }
  printf("[%llu,%llu): p=1(4) %ld  p=3(4) %ld  p=2 %ld  total %ld\n",A,B,c1,c3,c2,c1+c3+c2); return 0; }
