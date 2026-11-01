/* Z0524: for each n in [2,NMAX] and each modulus q in 2..12 and residue r in [0,q),
   decide whether 4/n = 1/x+1/y+1/z has a solution (x<=y<=z, positive integers) with x≡y≡z≡r (mod q).
   Full enumeration (x in [ceil(n/4), floor(3n/4)], y,z from divisors of B^2, B=n x, as in z52b_p1_U05_ucount.c).
   Output: per (q,r): number of n<=NMAX with no such solution ("fails"), and the first failing n's; plus per-n fail list file.
   Build: gcc -O2 -o /tmp/z52d_big/G1/apk scripts/z52d_p2_NC0_Z0524.c   Run: ./apk NMAX  (ulimit -v 4000000) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LIM 3300000
static int spf[LIM+1];
static int pf[64], pe[64], np;
static long divs[1 << 22];
static void addfac(int m, int mult) {
  while (m > 1) { int q = spf[m], e = 0; while (m % q == 0) { m /= q; e++; }
    int i; for (i = 0; i < np && pf[i] != q; i++); if (i == np) { pf[np] = q; pe[np] = 0; np++; }
    pe[i] += e * mult; }
}
#define QMAX 12
int main(int argc, char **argv) {
  long NMAX = argc > 1 ? atol(argv[1]) : 3000;
  for (int i = 2; i <= LIM; i++) if (!spf[i]) for (int j = i; j <= LIM; j += i) if (!spf[j]) spf[j] = i;
  /* index pairs (q,r): id = q*(q-1)/2 + r  for q=2..12, r<q  -> total 77 */
  int nid = 0; int qid[80], rid[80];
  for (int q = 2; q <= QMAX; q++) for (int r = 0; r < q; r++) { qid[nid] = q; rid[nid] = r; nid++; }
  static long fails[80]; memset(fails, 0, sizeof fails);
  static long firstfail[80][5]; for (int i = 0; i < 80; i++) for (int j = 0; j < 5; j++) firstfail[i][j] = -1;
  FILE *fo = fopen("/tmp/z52d_big/G1/Z0524_perN_fails.txt", "w");
  for (long n = 2; n <= NMAX; n++) {
    char ach[80]; memset(ach, 0, sizeof ach);
    long xlo = (n + 3) / 4, xhi = (3 * n) / 4;
    for (long x = xlo; x <= xhi; x++) {
      long A = 4 * x - n; if (A <= 0) continue;
      np = 0; addfac((int)n, 2); addfac((int)x, 2);
      long nd = 1; divs[0] = 1;
      for (int i = 0; i < np; i++) { long cur = nd;
        for (int e = 1; e <= pe[i]; e++) { long pw = 1; for (int k = 0; k < e; k++) pw *= pf[i];
          for (long j = 0; j < cur; j++) divs[nd++] = divs[j] * pw; } }
      long B = n * x; __int128 B2 = (__int128)B * B;
      for (long t = 0; t < nd; t++) {
        long d = divs[t];
        if (((d + B) % A) != 0) continue;
        __int128 y = ((__int128)B + d) / A; if (y < x) continue;
        __int128 z = ((__int128)B + B2 / d) / A; if (z < y) continue;
        if (((__int128)B + B2 / d) % A != 0) continue;
        long yy = (long)y, zz = (long)z;
        for (int q = 2; q <= QMAX; q++) {
          long r1 = x % q; if (yy % q == r1 && zz % q == r1) {
            for (int id = 0; id < nid; id++) if (qid[id] == q && rid[id] == r1) ach[id] = 1; }
        }
      }
    }
    int nf = 0;
    for (int id = 0; id < nid; id++) if (!ach[id]) {
      fails[id]++; nf++;
      for (int j = 0; j < 5; j++) if (firstfail[id][j] < 0) { firstfail[id][j] = n; break; }
      fprintf(fo, "%ld q=%d r=%d\n", n, qid[id], rid[id]);
    }
  }
  fclose(fo);
  printf("NMAX=%ld\n", NMAX);
  for (int id = 0; id < nid; id++)
    printf("q=%2d r=%2d fails=%ld first=%ld %ld %ld\n", qid[id], rid[id], fails[id],
           firstfail[id][0], firstfail[id][1], firstfail[id][2]);
  return 0;
}
