/* print primes p ≡ A (mod M) in [LO, HI) (segmented sieve). Usage: primes LO HI M A */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
int main(int c,char**v){ uint64_t lo=strtoull(v[1],0,10), hi=strtoull(v[2],0,10), M=strtoull(v[3],0,10), A=strtoull(v[4],0,10);
 uint64_t r=(uint64_t)sqrtl((long double)hi)+2; char *s=calloc(r+1,1); uint64_t *pr=malloc(sizeof(uint64_t)*(r/2+10)); int np=0;
 for(uint64_t i=2;i<=r;i++) if(!s[i]){ pr[np++]=i; for(uint64_t j=i*i;j<=r;j+=i) s[j]=1; }
 const uint64_t B=1<<20; char *seg=malloc(B);
 for(uint64_t b=lo;b<hi;b+=B){ uint64_t e=b+B<hi?b+B:hi; for(uint64_t i=0;i<e-b;i++) seg[i]=1;
  for(int k=0;k<np;k++){ uint64_t p=pr[k]; if(p*p>=e) break; uint64_t st=((b+p-1)/p)*p; if(st<p*p) st=p*p; for(uint64_t j=st;j<e;j+=p) seg[j-b]=0; }
  for(uint64_t i=0;i<e-b;i++) if(seg[i] && b+i>=2 && (b+i)%M==A) printf("%lu\n",b+i); }
 return 0; }
