// Pseudo-squares per OEIS A002189: a(k) = least non-square positive m = 1 (mod 8) with (m/p)=+1 for the first k odd primes p.
// Usage: z52d_p2_TO3_pseudosq LIMIT -> prints "k a(k)" for all k with a(k) <= LIMIT (scan over m = 1 mod 8).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static int jacobi(int64_t a, int64_t n){ int t=1; a%=n; if(a<0)a+=n;
  while(a){ while(!(a&1)){ a>>=1; int64_t r=n&7; if(r==3||r==5) t=-t; }
    int64_t tmp=a; a=n; n=tmp; if((a&3)==3 && (n&3)==3) t=-t; a%=n; }
  return n==1?t:0; }
int main(int argc,char**argv){ int64_t LIM=atoll(argv[1]);
  int64_t sz=(int64_t)sqrt((double)LIM)+10000;
  char *comp=calloc(sz+1,1); int64_t *pr=malloc(sizeof(int64_t)*(sz/2+100)); int np=0;
  for(int64_t i=3;i<=sz;i+=2){ if(!comp[i]){ pr[np++]=i; for(int64_t j=i*i;j<=sz;j+=2*i) comp[j]=1; } }
  // first K odd primes = all primes 3..; compute a(k) = least m that is QR for first k odd primes and nonsquare
  // scan m increasing; for each m, the largest k such that m is QR for first k odd primes is computed (early exit).
  int64_t best_k=0; int64_t kmax_prime=np;
  for(int64_t m=9;m<=LIM;m+=8){
    int64_t s=(int64_t)sqrt((double)m); while(s*s>m)s--; while((s+1)*(s+1)<=m)s++;
    if(s*s==m) continue;
    int k=0;
    for(int i=0;i<np;i++){ int64_t p=pr[i]; if(m%p==0){ break; } if(jacobi(m,p)!=1) break; k++; }
    if(k>best_k){ best_k=k; printf("%d %lld\n", k, (long long)m); fflush(stdout); }
  }
  return 0; }
