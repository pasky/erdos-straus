// z70 LOOSE item 3 (IDEAA #10): Type I with an explicit d-selection rule.
// Type I point at (p, d): exists a <= A, f | 4a^2 d + 1, f = -p (mod 4ad), p + f >= 4ad
//   (then c = (p+f)/4ad, e = (4a^2d+1)/f, b = (pe+1)/4ad; a Type I solution 4abd = pe+1, ce = a+b).
// Rules (pre-registered, Z70_LOOSE.md §1.3): NP d = least prime non-residue; Q3 d = least prime q = 3 (4) non-residue;
// CF d = first partial quotient a_i (i>=1, first period) of sqrt(p), non-square, (a_i/p) = -1;
// GA (Gaussian) p = a0^2 + b0^2, a0 odd: first of a0, odd(b0), a0+b0, |a0-b0|, a0+2b0, 2a0+b0 non-square with (d/p) = -1.
// Decoy for each rule: uniform random non-square d' with (d'/p) = -1, |d'-d| <= max(2, d/10), d' != d if possible.
// usage: z70_loose_typeI range N [A] [GAsub] [P0]   (only p >= P0 processed; primes p = 1 mod 24, p <= N; GA on every GAsub-th prime)
//        z70_loose_typeI list file [A]         (all p = 1 mod 4 in file, first column)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
typedef unsigned long long u64; typedef __uint128_t u128;
static int A = 2000;
static u64 mulmod(u64 a, u64 b, u64 m){ return (u64)((u128)a*b % m); }
static int jacobi(long long a, long long n){ // n odd positive
  a %= n; if (a < 0) a += n; int t = 1;
  while (a){ while (!(a & 1)){ a >>= 1; long long r = n & 7; if (r == 3 || r == 5) t = -t; }
    long long tmp = a; a = n; n = tmp; if ((a & 3) == 3 && (n & 3) == 3) t = -t; a %= n; }
  return n == 1 ? t : 0;
}
static int issq(u64 x){ u64 r = (u64)sqrtl((long double)x); while (r*r > x) r--; while ((r+1)*(r+1) <= x) r++; return r*r == x; }
// small primes for trial division
static int *pr; static int npr;
static void mkprimes(int L){ char *s = calloc(L+1,1); pr = malloc(sizeof(int)*(L/2+10)); npr = 0;
  for (int i = 2; i <= L; i++) if (!s[i]){ pr[npr++] = i; for (long long j = (long long)i*i; j <= L; j += i) s[j] = 1; } free(s); }
static int isprime_u(u64 n){ if (n < 2) return 0; for (int i = 0; i < npr && (u64)pr[i]*pr[i] <= n; i++) if (n % pr[i] == 0) return n == (u64)pr[i]; return 1; }
// divisor tables per d (cached)
typedef struct { int d; u64 **dv; int *nd; } Tab;
static Tab *cache = NULL; static int ncache = 0, capcache = 0;
static int cmpu(const void*x,const void*y){ u64 a=*(u64*)x,b=*(u64*)y; return a<b?-1:a>b; }
static void divisors(u64 N, u64 **out, int *cnt){
  u64 ps[64]; int es[64], k = 0; u64 m = N;
  for (int i = 0; i < npr && (u64)pr[i]*pr[i] <= m; i++) if (m % pr[i] == 0){ int e = 0; while (m % pr[i] == 0){ m /= pr[i]; e++; } ps[k] = pr[i]; es[k++] = e; }
  if (m > 1){ if ((u64)pr[npr-1]*pr[npr-1] < m){ fprintf(stderr,"trial bound too small for %llu\n",N); exit(2);} ps[k] = m; es[k++] = 1; }
  int tot = 1; for (int i = 0; i < k; i++) tot *= es[i] + 1;
  u64 *d = malloc(sizeof(u64)*tot); int c = 1; d[0] = 1;
  for (int i = 0; i < k; i++){ int c0 = c; u64 pp = 1; for (int e = 1; e <= es[i]; e++){ pp *= ps[i]; for (int j = 0; j < c0; j++) d[c++] = d[j]*pp; } }
  qsort(d, c, sizeof(u64), cmpu); *out = d; *cnt = c;
}
static Tab *gettab(int d){
  for (int i = 0; i < ncache; i++) if (cache[i].d == d) return &cache[i];
  if (ncache == capcache){ capcache = capcache ? 2*capcache : 64; cache = realloc(cache, sizeof(Tab)*capcache); }
  Tab *t = &cache[ncache++]; t->d = d; t->dv = malloc(sizeof(u64*)*(A+1)); t->nd = malloc(sizeof(int)*(A+1));
  for (int a = 1; a <= A; a++) divisors(4ULL*a*a*d + 1, &t->dv[a], &t->nd[a]);
  return t;
}
static long long hitA; // the a of the found point
static int slice(u64 p, int d){ // Type I point at (p,d) with a <= A ?
  if (d <= 20000){ Tab *t = gettab(d);
    for (int a = 1; a <= A; a++){ u64 g = 4ULL*a*d; for (int j = 0; j < t->nd[a]; j++){ u64 f = t->dv[a][j]; if ((p + f) % g == 0 && p + f >= g){ hitA = a; return 1; } } }
    return 0; }
  for (int a = 1; a <= A; a++){ u64 g = 4ULL*a*d, N = g*a + 1, f = (g - p % g) % g; if (f == 0) f = g;
    for (; f <= N; f += g) if (N % f == 0 && p + f >= g){ hitA = a; return 1; } }
  return 0;
}
static u64 rng = 88172645463325252ULL; static u64 xr(void){ rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return rng; }
static int decoy(u64 p, int d){
  int w = d/10 > 2 ? d/10 : 2; int lo = d - w < 2 ? 2 : d - w, hi = d + w; int cand[4096], nc = 0, self = 0;
  for (int x = lo; x <= hi && nc < 4096; x++) if (!issq(x) && jacobi(x, (long long)p) == -1){ if (x == d) self = 1; else cand[nc++] = x; }
  if (!nc) return self ? d : -1; return cand[xr() % nc];
}
// rules
static int rule_np(u64 p){ for (int i = 0; i < npr; i++) if (jacobi(pr[i], p) == -1) return pr[i]; return -1; }
static int rule_q3(u64 p){ for (int i = 0; i < npr; i++) if (pr[i] % 4 == 3 && jacobi(pr[i], p) == -1) return pr[i]; return -1; }
static int rule_cf(u64 p){ // partial quotients of sqrt(p), first period
  u64 a0 = (u64)sqrtl((long double)p); while (a0*a0 > p) a0--; while ((a0+1)*(a0+1) <= p) a0++;
  long long m = 0, dd = 1, a = a0;
  for (long long it = 0; it < 50000000; it++){ m = dd*a - m; dd = (p - m*m)/dd; a = (a0 + m)/dd;
    if (a < 1000000 && !issq(a) && jacobi(a, p) == -1) return (int)a; if (a == 2*(long long)a0) return -1; }
  return -1; }
static u64 isqrt_(u64 x){ u64 r = (u64)sqrtl((long double)x); while (r*r > x) r--; while ((r+1)*(r+1) <= x) r++; return r; }
static int rule_ga(u64 p){ // p = a0^2 + b0^2 via Cornacchia
  u64 x = 2; for (;; x++) if (jacobi(x, p) == -1) break; // non-residue
  u64 e = (p-1)/4, r = 1, b = x; while (e){ if (e & 1) r = mulmod(r,b,p); b = mulmod(b,b,p); e >>= 1; } // r^2 = -1
  u64 A0 = p, B0 = r, L = isqrt_(p); while (B0 > L){ u64 t = A0 % B0; A0 = B0; B0 = t; }
  u64 aa = B0, bb = isqrt_(p - aa*aa); if (aa*aa + bb*bb != p){ fprintf(stderr,"cornacchia fail %llu\n",p); exit(3);} if (!(aa & 1)){ u64 t = aa; aa = bb; bb = t; }
  u64 ob = bb; while (!(ob & 1)) ob >>= 1;
  long long c[6] = {(long long)aa, (long long)ob, (long long)(aa+bb), llabs((long long)aa-(long long)bb), (long long)(aa+2*bb), (long long)(2*aa+bb)};
  for (int i = 0; i < 6; i++) if (c[i] >= 2 && c[i] < 2000000000LL && !issq(c[i]) && jacobi(c[i], p) == -1) return (int)c[i];
  return -1; }
#define NR 4
static const char *rn[NR] = {"NP","Q3","CF","GA"};
static long long cov[NR], dcov[NR], tot[NR], undef[NR], bb[NR], cc[NR], nodec[NR]; static double dsum[NR]; static int dmax[NR];
static void one(u64 p, int doGA, int verbose){
  int ds[NR] = {rule_np(p), rule_q3(p), rule_cf(p), doGA ? rule_ga(p) : -2};
  if (verbose) printf("%llu", p);
  for (int r = 0; r < NR; r++){ if (ds[r] == -2) continue; tot[r]++;
    if (ds[r] < 0){ undef[r]++; if (verbose) printf(" %s:undef", rn[r]); continue; }
    int h = slice(p, ds[r]); long long ha = hitA; int dd = decoy(p, ds[r]); int hd = dd > 0 ? slice(p, dd) : -1;
    cov[r] += h; dsum[r] += ds[r]; if (ds[r] > dmax[r]) dmax[r] = ds[r];
    if (hd < 0) nodec[r]++; else { dcov[r] += hd; if (h && !hd) bb[r]++; if (hd && !h) cc[r]++; }
    if (verbose) printf(" %s:d=%d:%s%s(dec %d:%d)", rn[r], ds[r], h ? "hit" : "MISS", h ? "" : "", dd, hd);
    if (verbose && h) printf("[a=%lld]", ha);
  }
  if (verbose) printf("\n");
}
static void report(void){
  for (int r = 0; r < NR; r++){ if (!tot[r]) continue; long long def = tot[r] - undef[r];
    printf("rule %s: primes=%lld undefined=%lld covered=%lld (%.5f of all) decoy covered=%lld (of %lld with decoy) McNemar b=%lld c=%lld z=%+.2f mean d=%.1f max d=%d\n",
      rn[r], tot[r], undef[r], cov[r], (double)cov[r]/tot[r], dcov[r], def - nodec[r], bb[r], cc[r], (bb[r]+cc[r]) ? (bb[r]-cc[r])/sqrt((double)(bb[r]+cc[r])) : 0.0, def ? dsum[r]/def : 0, dmax[r]); }
}
int main(int argc, char **argv){
  if (argc < 3) return 1; if (argc > 3) A = atoi(argv[3]);
  mkprimes(4000000);
  // fixture
  { int fx = slice(1033, 132); printf("fixture (1033, d=132): %s a=%lld\n", fx ? "found" : "NOT FOUND", hitA); }
  if (!strcmp(argv[1], "range")){ u64 N = strtoull(argv[2],0,10); int sub = argc > 4 ? atoi(argv[4]) : 30; u64 P0 = argc > 5 ? strtoull(argv[5],0,10) : 0;
    char *s = calloc(N/2+2, 1); for (u64 i = 3; i*i <= N; i += 2) if (!s[i/2]) for (u64 j = i*i; j <= N; j += 2*i) s[j/2] = 1;
    long long k = 0;
    for (u64 p = 25; p <= N; p += 24) if (!s[p/2]){ if (p < P0){ k++; continue; } one(p, (k % sub) == 0, 0); k++; if (k % 100000 == 0){ fprintf(stderr, "%llu %lld\n", p, k); } }
    report();
  } else { FILE *F = fopen(argv[2], "r"); char line[512];
    while (fgets(line, sizeof line, F)){ if (line[0] == '#') continue; u64 p = strtoull(line, 0, 10); if (p < 5 || p % 4 != 1) continue; one(p, 1, 1); }
    report(); }
  return 0;
}
