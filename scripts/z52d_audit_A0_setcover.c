// z52d audit A0, item Z2001: greedy set cover of primes p ≡ 1 (mod 24) in [X, 2X)
// by (★) menu items (u,C): item covers p iff (4uC-1) | (p+u)  [p = 4uBC - u - B with B = (p+u)/(4uC-1)].
// Usage: z52d_audit_A0_setcover X
// Output: #targets, #uncoverable ((★) failures), #items with >=1 hit, greedy menu size, and the greedy
// coverage curve at fractions 50/90/99/100 %, plus the number of greedy items covering exactly 1 new prime.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef struct { int32_t s; int32_t c; } HE;
static HE *heap; static long hn = 0;
static void hpush(int32_t s, int32_t c) { long i = hn++; heap[i].s = s; heap[i].c = c;
  while (i > 0) { long p = (i - 1) / 2; if (heap[p].c >= heap[i].c) break; HE t = heap[p]; heap[p] = heap[i]; heap[i] = t; i = p; } }
static HE hpop(void) { HE top = heap[0]; heap[0] = heap[--hn]; long i = 0;
  for (;;) { long l = 2 * i + 1, r = l + 1, b = i; if (l < hn && heap[l].c > heap[b].c) b = l; if (r < hn && heap[r].c > heap[b].c) b = r;
    if (b == i) break; HE t = heap[b]; heap[b] = heap[i]; heap[i] = t; i = b; } return top; }

int main(int argc, char **argv) {
  long X = atol(argv[1]); long Y = 2 * X;
  char *comp = calloc(Y + 1, 1); comp[0] = comp[1] = 1;
  for (long i = 2; i * i <= Y; i++) if (!comp[i]) for (long j = i * i; j <= Y; j += i) comp[j] = 1;
  int32_t *tidx = malloc(sizeof(int32_t) * (Y + 1)); long nt = 0;
  for (long n = 0; n <= Y; n++) tidx[n] = -1;
  for (long n = X; n < Y; n++) if (!comp[n] && n % 24 == 1) tidx[n] = nt++;
  free(comp);
  // pass 1: count incidences; pass 2: fill CSR
  long ninc = 0, nsets = 0;
  for (int pass = 0; pass < 2; pass++) {
    static long *off; static int32_t *el; static int32_t *su, *sc;
    if (pass == 1) { off = malloc(sizeof(long) * (nsets + 1)); el = malloc(sizeof(int32_t) * ninc);
      su = malloc(sizeof(int32_t) * nsets); sc = malloc(sizeof(int32_t) * nsets); }
    long k = 0, s = 0;
    for (long u = 1; 4 * u - 1 - u <= Y; u++)
      for (long C = 1;; C++) {
        long m = 4 * u * C - 1; if (m - u >= Y) break;
        long r = ((-u) % m + m) % m; long n0 = X + ((r - X % m) % m + m) % m;
        long cnt = 0;
        for (long n = n0; n < Y; n += m) if (tidx[n] >= 0 && n + u >= m) { // B >= 1
          if (pass == 1) el[k + cnt] = tidx[n]; cnt++; }
        if (cnt) { if (pass == 1) { off[s] = k; su[s] = u; sc[s] = C; } s++; k += cnt; }
      }
    if (pass == 0) { ninc = k; nsets = s; continue; }
    off[nsets] = k;
    // coverable targets
    char *cov = calloc(nt, 1); long ncoverable = 0;
    for (long i = 0; i < ninc; i++) if (!cov[el[i]]) { cov[el[i]] = 1; ncoverable++; }
    memset(cov, 0, nt);
    heap = malloc(sizeof(HE) * nsets);
    for (long t = 0; t < nsets; t++) hpush(t, off[t + 1] - off[t]);
    long covered = 0, chosen = 0, singles = 0; int mark[4] = {0, 0, 0, 0}; double fr[4] = {0.5, 0.9, 0.99, 1.0};
    long msz[4]; long maxm_chosen = 0;
    printf("X=%ld targets=%ld uncoverable=%ld items_with_hits=%ld incidences=%ld mean_R=%.2f\n", X, nt, nt - ncoverable,
           nsets, ninc, (double)ninc / nt);
    while (covered < ncoverable && hn > 0) {
      HE h = hpop(); long c = 0;
      for (long i = off[h.s]; i < off[h.s + 1]; i++) if (!cov[el[i]]) c++;
      if (c < h.c) { if (c > 0) hpush(h.s, c); continue; }
      for (long i = off[h.s]; i < off[h.s + 1]; i++) cov[el[i]] = 1;
      covered += c; chosen++; if (c == 1) singles++;
      long m = 4L * su[h.s] * sc[h.s] - 1; if (m > maxm_chosen) maxm_chosen = m;
      if (chosen <= 10) printf("  pick %ld: (u,C)=(%d,%d) m=%ld new=%ld\n", chosen, su[h.s], sc[h.s], m, c);
      for (int j = 0; j < 4; j++) if (!mark[j] && covered >= fr[j] * ncoverable) { mark[j] = 1; msz[j] = chosen; }
    }
    printf("greedy_menu=%ld singletons=%ld max_m=%ld  size@50%%=%ld @90%%=%ld @99%%=%ld @100%%=%ld\n", chosen, singles,
           maxm_chosen, msz[0], msz[1], msz[2], msz[3]);
    // lower bound: number of targets whose every covering item covers only that target (forced singletons)
    long *deg1 = calloc(nt, sizeof(long)); // per target: number of items covering >=2 targets
    for (long t = 0; t < nsets; t++) if (off[t + 1] - off[t] >= 2) for (long i = off[t]; i < off[t + 1]; i++) deg1[el[i]]++;
    long forced = 0; for (long i = 0; i < nt; i++) if (deg1[i] == 0) forced++;
    printf("targets_with_no_shared_item=%ld (minus uncoverable %ld)\n", forced - (nt - ncoverable), nt - ncoverable);
  }
  return 0;
}
