/* R206 from-scratch recheck of TORSION_FIRING Prop 4.2 EVIDENCE and Prop 4.3, written WITHOUT elliptic curves:
 *   (a)(n): exists c,d >= 1 with (4c^2 d - 1)^2 <= 4n and an integer divisor h of n + 4c^2 d with h = -1 (mod 4cd);
 *   (b)(n): exists 1 <= c with (c - 1)^2 <= 4n and a divisor h of n + c with h = -1 (mod 4c);
 *   (iii)(n): exists d >= 1 such that 4dn + 1 has a divisor h = -1 (mod 4d)   [j = 1 face, any size]
 *            (d bounded by 3cd <= n+1 of FMS Lemma 1.1, i.e. d <= (n+1)/3).
 * By Deuring-Waterhouse, (a)/(b) are exactly Prop 4.2's "E(F_p) of trace 1 - 4c^2 d / 1 - c has a subgroup of order
 * h" (a finite abelian group has subgroups of every order dividing its order), so this checks the EVIDENCE claim and
 * shows that it is a pure divisor statement.
 * Usage: review_tf_hasse N [J]   (primes 5..N and odd squares 9..N; (iii) vs (b) compared for n <= J)
 */
#include <stdio.h>
#include <stdlib.h>
typedef unsigned long long u64;
static unsigned *spf; static u64 SPFN;
static void build(u64 N) { SPFN = N; spf = calloc(N + 1, sizeof(unsigned));
    for (u64 i = 2; i <= N; i++) if (!spf[i]) for (u64 j = i; j <= N; j += i) if (!spf[j]) spf[j] = (unsigned)i; }
/* does m have a divisor h = -1 mod M ? (m <= SPFN) */
static int hasdiv(u64 m, u64 M) {
    u64 ps[32]; int es[32], k = 0; u64 t = m;
    while (t > 1) { u64 q = spf[t]; int e = 0; while (t % q == 0) { t /= q; e++; } ps[k] = q; es[k++] = e; }
    u64 divs[1 << 14]; int nd = 1; divs[0] = 1;
    for (int i = 0; i < k; i++) { int cur = nd; u64 pw = 1; for (int e = 1; e <= es[i]; e++) { pw *= ps[i];
        for (int j = 0; j < cur; j++) divs[nd++] = divs[j] * pw; } }
    for (int j = 0; j < nd; j++) if ((divs[j] + 1) % M == 0) return 1;
    return 0;
}
static int isq(u64 n) { u64 r = 0; while ((r + 1) * (r + 1) <= n) r++; return r * r == n; }
static int A(u64 n) { for (u64 c = 1; (4 * c * c - 1) * (4 * c * c - 1) <= 4 * n; c++)
    for (u64 d = 1; (4 * c * c * d - 1) * (4 * c * c * d - 1) <= 4 * n; d++) if (hasdiv(n + 4 * c * c * d, 4 * c * d)) return 1; return 0; }
static int B(u64 n) { for (u64 c = 1; (c - 1) * (c - 1) <= 4 * n; c++) if (hasdiv(n + c, 4 * c)) return 1; return 0; }
static int C3(u64 n) { for (u64 d = 1; 3 * d <= n + 1; d++) if (hasdiv(4 * d * n + 1, 4 * d)) return 1; return 0; }
int main(int argc, char **argv) {
    u64 N = strtoull(argv[1], 0, 10), J = argc > 2 ? strtoull(argv[2], 0, 10) : 0;
    u64 need = N + 4 * (u64)(2 * __builtin_sqrt((double)N) + 2) + 10;
    u64 needJ = 4 * (J + 1) / 3 * J + J + 10; if (needJ > need) need = needJ;
    build(need);
    int np = 0, fa = 0, fb = 0, both = 0, sqa = 0, sqb = 0, nsq = 0, mism = 0;
    for (u64 n = 5; n <= N; n += 2) {
        int pr = (spf[n] == n), sq = isq(n);
        if (!pr && !sq) continue;
        int a = A(n), b = B(n);
        if (pr) { np++; if (!a) { fa++; printf("(a) fails: %llu\n", n); } if (!b) { fb++; printf("(b) fails: %llu\n", n); } if (!a && !b) both++;
            if (n <= J && C3(n) != b) { mism++; printf("Prop4.3 mismatch %llu\n", n); } }
        else { nsq++; sqa += a; sqb += b; }
    }
    printf("primes 5..%llu: %d; (a) fails %d, (b) fails %d, both fail %d; Prop 4.3 (iii) vs (b) mismatches (n<=%llu): %d\n",
           N, np, fa, fb, both, J, mism);
    printf("odd squares 9..%llu: %d; (a) holds %d, (b) holds %d\n", N, nsq, sqa, sqb);
    return 0;
}
