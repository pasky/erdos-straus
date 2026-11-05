// z57 BFF exhaustive decider: for every prime p = 1 (mod 4) in [A, B], decide R_G*(p) >= 1.
// Method (memo Z57_BFF.md Lemmas 1.2-1.3): a (*) solution (n, m, C), p = 4nmC - n - m, with
// P = min(n,m), Q = max(n,m) lies in G* iff Q^4 > P p; then d_P := 4PC - 1 satisfies d_P Q = p + P
// and d_P <= floor(p^{3/4}) + 1.  For d = 3 (mod 4) put n_d := d - (p mod d); HIT(d) <=> 4 n_d | d+1,
// and then (n_d, (p+n_d)/d, (d+1)/(4 n_d)) is a solution.  So R_G*(p) >= 1 iff some d = 3 (4),
// d <= floor(p^{3/4}) + 1, has HIT(d) with the solution in G*.  We scan d upward and stop at the
// first G* hit.  Output: one line per G*-zero ("Z p"), plus a summary line.
// usage: decide A B
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

typedef unsigned __int128 u128;

static int in_gstar(uint64_t p, uint64_t n, uint64_t m){
  uint64_t P = n<m?n:m, Q = n<m?m:n;
  // exact: if Q >= 2^32 then Q^4 >= 2^128 > P*p (P < p < 2^63); else Q^4 < 2^128 fits in u128
  if (Q >= (1ULL<<32)) return 1;
  u128 q2 = (u128)Q*Q; u128 q4 = q2*q2; u128 pp = (u128)P*p;
  return q4 > pp;
}

static uint64_t dmax_of(uint64_t p){
  // floor(p^{3/4}) + 1, computed safely: find largest D with D^4 <= p^3 via long double then adjust in integers
  long double x = powl((long double)p, 0.75L);
  uint64_t D = (uint64_t)x;
  // adjust: want D = floor(p^{3/4}): D^4 <= p^3 < (D+1)^4
  u128 p3 = (u128)p*p*p;
  while ((u128)D*D*D*D > p3) D--;
  while ((u128)(D+1)*(D+1)*(D+1)*(D+1) <= p3) D++;
  return D + 1;
}

// returns 1 if a G* hit exists, 0 otherwise; sets *dfirst
static int decide(uint64_t p, uint64_t *dfirst){
  uint64_t dmax = dmax_of(p);
  for (uint64_t d = 3; d <= dmax; d += 4){
    uint64_t r = p % d; uint64_t n = d - r;
    if ((d + 1) % (4*n) == 0){
      uint64_t m = (p + n) / d;
      if (in_gstar(p, n, m)) { *dfirst = d; return 1; }
    }
  }
  *dfirst = 0; return 0;
}

int main(int argc, char**argv){
  uint64_t A = strtoull(argv[1],0,10), B = strtoull(argv[2],0,10);
  const uint64_t SEG = 1ULL<<26; // segment of odd numbers
  // small primes up to sqrt(B)
  uint64_t lim = (uint64_t)sqrtl((long double)B) + 2;
  unsigned char *sm = calloc(lim+1,1);
  for (uint64_t i=2;i<=lim;i++) if(!sm[i]) for(uint64_t j=i*i;j<=lim;j+=i) sm[j]=1;
  uint64_t *pr = malloc(sizeof(uint64_t)*(lim/2+10)); size_t np=0;
  for (uint64_t i=3;i<=lim;i+=2) if(!sm[i]) pr[np++]=i;
  unsigned char *seg = malloc(SEG);
  uint64_t nprimes=0, nzeros=0, maxd=0, maxdp=0; long double sumlogexp=0;
  if (A < 5) A = 5;
  uint64_t lo = A | 1; // odd
  while (lo <= B){
    uint64_t hi = lo + 2*SEG - 2; if (hi > B) hi = B; // odd numbers lo, lo+2, ..., hi
    size_t len = (hi - lo)/2 + 1;
    memset(seg, 0, len);
    for (size_t k=0;k<np;k++){
      uint64_t q = pr[k]; if (q*q > hi) break;
      uint64_t s = ((lo + q - 1)/q)*q; if (s < q*q) s = q*q; if ((s&1)==0) s += q;
      for (uint64_t j=s; j<=hi; j+=2*q) seg[(j-lo)/2] = 1;
    }
    for (size_t i=0;i<len;i++){
      if (seg[i]) continue;
      uint64_t p = lo + 2*i; if (p%4 != 1) continue;
      nprimes++;
      uint64_t d;
      if (!decide(p,&d)) { nzeros++; printf("Z %llu\n",(unsigned long long)p); fflush(stdout); }
      else { if (d>maxd){maxd=d;maxdp=p;} }
    }
    lo = hi + 2;
  }
  printf("# [%llu,%llu] primes=1(4): %llu  G*-zeros: %llu  max first-hit d: %llu at p=%llu\n",
    (unsigned long long)A,(unsigned long long)B,(unsigned long long)nprimes,(unsigned long long)nzeros,(unsigned long long)maxd,(unsigned long long)maxdp);
  return 0;
}
