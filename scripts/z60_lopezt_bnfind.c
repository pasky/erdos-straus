// z60 LOPEZT: least BN witness g (g=3 mod 4, (-n mod g) | (g+1)/4) for a single n, exhaustive up to (4n+1)/3 (Lemma 1.1(ii)).
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
int main(int argc,char**argv){ u64 n=atoll(argv[1]); u64 gmax=(4*n+1)/3;
  for(u64 g=3; g<=gmax; g+=4){ if(n%g==0) continue; u64 r=g-n%g; if(((g+1)/4)%r==0){ printf("%llu BN g=%llu a=%llu\n",n,g,r); return 0;} }
  printf("%llu BN none\n",n); return 0; }
