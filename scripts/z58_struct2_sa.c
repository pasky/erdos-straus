// z58 STRUCT2: "integral strong approximation" test for X_n : 4abcd = a + b + nc (positive points).
// For n ≡ 1 (mod 4) in [lo, hi) (all, or primes only), record which residue classes of the coordinates are hit by
// positive integral points: d mod 2, c mod 2, a mod 3, c mod 3, d mod 3, c mod 5, d mod 5, a mod 4, c mod 4, d mod 4.
// Output: n N_II isprime mask_d2 mask_c2 mask_a3 mask_c3 mask_d3 mask_c5 mask_d5 mask_a4 mask_c4 mask_d4  (bit r = class r hit)
// Usage: sa lo hi [primes_only]
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static int isprime(u64 n){ if(n<2) return 0; for(u64 q=2;q*q<=n;q++) if(n%q==0) return 0; return 1; }
int main(int argc,char**argv){
  if(argc<3){fprintf(stderr,"usage: sa lo hi [primes_only]\n");return 1;}
  u64 lo=strtoull(argv[1],0,10),hi=strtoull(argv[2],0,10); int po=argc>3?atoi(argv[3]):0;
  if(hi>2000000000ULL){fprintf(stderr,"hi too large\n");return 1;}
  u64 n0=lo; while(n0%4!=1) n0++;
  for(u64 n=n0;n<hi;n+=4){ int pr=isprime(n); if(po&&!pr) continue; u64 N=0; unsigned m[10]={0};
    for(u64 a=1;4*a<=n+a+1;a++) for(u64 b=1;;b++){ u64 q=4*a*b; if(q>n+a+b) break; u64 e=(q-n%q)%q;
      if(e==0||e>a+b||(a+b)%e) continue; u64 c=(a+b)/e, d=(n+e)/q; N++;
      m[0]|=1u<<(d%2); m[1]|=1u<<(c%2); m[2]|=1u<<(a%3); m[3]|=1u<<(c%3); m[4]|=1u<<(d%3);
      m[5]|=1u<<(c%5); m[6]|=1u<<(d%5); m[7]|=1u<<(a%4); m[8]|=1u<<(c%4); m[9]|=1u<<(d%4); }
    printf("%llu %llu %d",n,N,pr); for(int i=0;i<10;i++) printf(" %u",m[i]); printf("\n"); }
  return 0; }
