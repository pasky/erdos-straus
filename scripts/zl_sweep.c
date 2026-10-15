/* zl_sweep.c -- O228 (STERILE_LOWER.md §6). Joint level-1 sweep (Lemma 3.1) over all n in [X0, X1).
   P: exact count of ALL P-data (a <= b) of n (Lemma 3.1(i)): triples (a,c,d), f = 4acd-1, n == -4a^2 d (mod f),
      c n >= 4a^2 c d - 2a.
   Q: exact count of the Q-data (a <= b) of n with a < A and a*d > Y (Lemma 3.1(ii)): rows a, d in (Y/a, (2 X1 + 2)/(4a)],
      m = 4a^2 d + 1 fully factored by a sieve in d (primes <= sqrt(m)); every divisor f <= X1 + 1 of m and every c with
      n = 4acd - f in [X0, X1) and n a + c >= a f.   (acd <= (n+1)/2 => d <= (2n+2)/(4a), f <= n + 2.)
   Counts are kept only for PRIME n (odd n, prime bitmap); 16-bit saturating (65535 = overflow -> caller fails closed).
   Env (O228 round 2; unset = previous behaviour): ZL_ALO=a0 -> Q rows a in [a0, A) only; ZL_NOP=1 -> skip P;
   ZL_BIN=file -> also write the raw uint16 arrays JP, JQ (odd n in [X0, X1)) for merging split runs (zl_merge.py).
   Usage: zl_sweep X0 X1 A Y q [all]     prints per cell [2^{j/q}, 2^{(j+1)/q}) (cells clipped to [X0,X1)):
      "C j lo hi maxP maxQ max(P+Q) nprimes"    ("all": count every odd n, no prime filter -- validation mode). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef uint64_t u64; typedef unsigned __int128 u128;
static u64 X0, X1, A, Y; static int ALL = 0;
static uint16_t *JP, *JQ; static uint8_t *isp;      /* index (n - X0) >> 1, n odd */
static uint32_t *pr; static long npr;
static inline void inc(uint16_t *J, u64 n){ u64 i = (n - X0) >> 1; if((ALL || isp[i]) && J[i] != 65535) J[i]++; }
static void primes_upto(u64 B){ uint8_t *s = calloc(B + 1, 1); pr = malloc(sizeof(uint32_t) * (B / 2 + 10)); npr = 0;
  for(u64 i = 2; i <= B; i++){ if(s[i]) continue; pr[npr++] = (uint32_t)i; for(u64 j = i * i; j <= B; j += i) s[j] = 1; } free(s); }
static u64 isqrt64(u64 x){ u64 r = (u64)sqrtl((long double)x); while(r * r > x) r--; while((r + 1) * (r + 1) <= x) r++; return r; }
static u64 inv_mod(u64 a, u64 p){ int64_t t = 0, nt = 1; int64_t r = (int64_t)p, nr = (int64_t)(a % p);
  while(nr){ int64_t q = r / nr, tmp = t - q * nt; t = nt; nt = tmp; tmp = r - q * nr; r = nr; nr = tmp; } if(t < 0) t += (int64_t)p; return (u64)t; }

static void sweepP(void){
  for(u64 a = 1; 4 * a * a - 2 * a < X1; a++)
    for(u64 d = 1; 4 * a * a * d - 2 * a < X1; d++){
      u64 q4 = 4 * a * a * d;
      for(u64 c = 1; ; c++){
        u64 f = 4 * a * c * d - 1;
        if(f > q4 && f - q4 >= X1) break;            /* least positive member of the class is f - 4a^2 d >= X1 */
        u64 lo = q4 - (2 * a) / c; if(lo < X0) lo = X0; /* ceil(4a^2 d - 2a/c) */
        u64 N0 = (f - q4 % f) % f;                      /* == -4a^2 d (mod f) */
        u64 N = (lo <= N0) ? N0 : N0 + ((lo - N0 + f - 1) / f) * f;
        if(N == 0) N = f;
        if(!(N & 1)) N += f;                            /* f odd: parity alternates */
        for(; N < X1; N += 2 * f) inc(JP, N);
      }
    }
}

#define L 32768
#define MF 16
static u64 cof[L]; static uint32_t fp[L][MF]; static uint8_t fe[L][MF], nf[L];
static u64 dv[1 << 16];
static void sweepQ(void){
  u64 *delta = malloc(sizeof(u64) * npr), *nxt = malloc(sizeof(u64) * npr);
  u64 ALO = getenv("ZL_ALO") ? strtoull(getenv("ZL_ALO"), 0, 10) : 1; if(ALO < 1) ALO = 1;
  for(u64 a = ALO; a < A; a++){
    u64 dlo = Y / a + 1, dhi = (2 * X1 + 2) / (4 * a);
    if(dlo > dhi) continue;
    u64 mmax = 4 * a * a * dhi + 1, P = isqrt64(mmax); long np = 0;
    while(np < npr && pr[np] <= P) np++;
    if(np == npr && (u64)pr[npr - 1] < P){ fprintf(stderr, "prime table too small\n"); exit(3); }
    u64 a2 = (4 * a * a);
    for(long i = 1; i < np; i++){ u64 p = pr[i]; if(a % p == 0){ delta[i] = ~0ULL; continue; }
      delta[i] = (p - inv_mod(a2 % p, p)) % p; u64 s = dlo % p; nxt[i] = dlo + (delta[i] + p - s) % p; }
    for(u64 d0 = dlo; d0 <= dhi; d0 += L){
      u64 len = (dhi - d0 + 1 < L) ? dhi - d0 + 1 : L;
      for(u64 k = 0; k < len; k++){ cof[k] = a2 * (d0 + k) + 1; nf[k] = 0; }
      for(long i = 1; i < np; i++){ if(delta[i] == ~0ULL) continue; u64 p = pr[i];
        u64 d = nxt[i];
        for(; d < d0 + len; d += p){ u64 k = d - d0; uint8_t e = 0; while(cof[k] % p == 0){ cof[k] /= p; e++; }
          if(e == 0){ fprintf(stderr, "sieve root error a=%llu p=%llu\n", (unsigned long long)a, (unsigned long long)p); exit(4); }
          if(nf[k] >= MF){ fprintf(stderr, "MF overflow\n"); exit(5); } fp[k][nf[k]] = (uint32_t)p; fe[k][nf[k]] = e; nf[k]++; }
        nxt[i] = d; }
      for(u64 k = 0; k < len; k++){
        u64 d = d0 + k, m = a2 * d + 1, x = 4 * a * d;
        int nd = 1; dv[0] = 1;                      /* divisors <= X1 + 1 */
        int nfac = nf[k]; u64 extra = cof[k];
        for(int j = 0; j <= nfac; j++){
          u64 p; int e;
          if(j < nfac){ p = fp[k][j]; e = fe[k][j]; } else { if(extra == 1) break; p = extra; e = 1; }
          int cur = nd;
          for(int t = 0; t < cur; t++){ u64 v = dv[t];
            for(int r = 0; r < e; r++){ if(v > (X1 + 1) / p) break; v *= p; if(nd >= (1 << 16)){ fprintf(stderr, "dv overflow\n"); exit(6); } dv[nd++] = v; } }
        }
        (void)m;
        for(int t = 0; t < nd; t++){ u64 f = dv[t];
          u64 c = (X0 + f + x - 1) / x;
          for(;; c++){ u64 n = x * c - f; if(n >= X1) break; if(n < X0) continue;
            if(n * a + c >= a * f) inc(JQ, n); }
        }
      }
    }
  }
  free(delta); free(nxt);
}

int main(int argc, char **argv){
  if(argc < 6){ fprintf(stderr, "usage: zl_sweep X0 X1 A Y q [all]\n"); return 2; }
  X0 = strtoull(argv[1], 0, 10); X1 = strtoull(argv[2], 0, 10); A = strtoull(argv[3], 0, 10); Y = strtoull(argv[4], 0, 10);
  int q = atoi(argv[5]); ALL = (argc > 6);
  if(!(X0 & 1)) X0++;                                 /* odd n only */
  u64 M = (X1 - X0 + 1) / 2 + 1;
  JP = calloc(M, 2); JQ = calloc(M, 2); isp = malloc(M);
  u64 Pmax = isqrt64((A > 1 ? A : 1) * (2 * X1 + 2) + 1) + 2; if(Pmax < isqrt64(X1) + 2) Pmax = isqrt64(X1) + 2;
  primes_upto(Pmax);
  for(u64 i = 0; i < M; i++) isp[i] = 1;              /* odd n in [X0, X1): sieve */
  for(long i = 1; i < npr && (u64)pr[i] * pr[i] < X1; i++){ u64 p = pr[i];
    u64 s = ((X0 + p - 1) / p) * p; if(s < p * p) s = p * p; if(!(s & 1)) s += p;
    for(; s < X1; s += 2 * p) isp[(s - X0) >> 1] = 0; }
  if(!getenv("ZL_NOP")) sweepP(); fprintf(stderr, "P done\n");
  sweepQ(); fprintf(stderr, "Q done\n");
  if(getenv("ZL_BIN")){ FILE *fb = fopen(getenv("ZL_BIN"), "wb"); if(!fb){ perror("ZL_BIN"); return 7; }
    if(fwrite(JP, 2, M, fb) != M || fwrite(JQ, 2, M, fb) != M){ fprintf(stderr, "short write\n"); return 7; } fclose(fb); }
  /* cells */
  int j0 = (int)floor(q * log2((double)X0)) - 1, j1 = (int)ceil(q * log2((double)X1)) + 1;
  for(int j = j0; j <= j1; j++){
    long double lo = powl(2.0L, (long double)j / q), hi = powl(2.0L, (long double)(j + 1) / q);
    u64 ilo = (u64)ceill(lo), ihi = (u64)ceill(hi);    /* integers n with lo <= n < hi */
    if(ilo < X0) ilo = X0; if(ihi > X1) ihi = X1; if(ilo >= ihi) continue;
    unsigned mp = 0, mq = 0, ms = 0; u64 cnt = 0;
    for(u64 n = ilo | 1; n < ihi; n += 2){ u64 i = (n - X0) >> 1; if(!ALL && !isp[i]) continue; cnt++;
      unsigned p = JP[i], qq = JQ[i]; if(p > mp) mp = p; if(qq > mq) mq = qq;
      unsigned s = (p == 65535 || qq == 65535) ? 131070 : p + qq; if(s > ms) ms = s; }
    printf("C %d %llu %llu %u %u %u %llu\n", j, (unsigned long long)ilo, (unsigned long long)ihi, mp, mq, ms, (unsigned long long)cnt);
  }
  if(getenv("ZL_DUMP")) for(u64 n = X0; n < X1; n += 2) printf("N %llu %u %u\n", (unsigned long long)n, JP[(n - X0) >> 1], JQ[(n - X0) >> 1]);
  return 0;
}
