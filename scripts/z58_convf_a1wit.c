// z58 CONVF: quick (INCOMPLETE: misses witnesses f>sqrt(p+4d) whose cofactor is not = -1 mod 4d) a=1 witness scan for primes p (argv); d<=2e6; E marks even d
#include <stdio.h>
#include <stdlib.h>
int main(int argc,char**argv){ for(int i=1;i<argc;i++){ long p=atol(argv[i]); int cnt=0, evenfound=0; printf("p=%ld:",p);
  for(long d=1; d<=2000000 && cnt<6; d++){ long m=p+4*d; // divisors f of m with f = -1 mod 4d: f=4dc-1 ; check both f and m/f
    for(long c=1;;c++){ long f=4*d*c-1; if((__int128)f*f>m) break; if(m%f==0){ long g=m/f; if(g%(4*d)==4*d-1 || 1){ /* f itself is a witness */ printf(" (c=%ld,d=%ld%s)",c,d,d%2==0?"E":""); cnt++; if(d%2==0)evenfound=1; }
        if(g%(4*d)==4*d-1 && g!=f){ printf(" (c=%ld,d=%ld%s)",(g+1)/(4*d),d,d%2==0?"E":""); cnt++; if(d%2==0)evenfound=1; } } }
    if(cnt>=6) break; }
  printf("  [a=1 witnesses found: %d, even-d: %s]\n",cnt,evenfound?"yes":"no"); } return 0; }
