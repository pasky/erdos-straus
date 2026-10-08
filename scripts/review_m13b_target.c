/* R95 from-scratch exhaustive search of II3 / I3 / I1 classes containing x(u) (u_11,u_13 given mod q^16),
 * e = 4a'd'm-1 <= X.  Different method from m13b_target.c: no discrete log and NO cap on the T-level.
 * Key point: the box condition e = -u_q (mod q^{v_q(ad)}) forces v_q(a)+v_q(d) <= w_q := v_q(e+u_q)
 * (and = 0 if q | e), so all T-parts (a_T,d_T) are enumerated exhaustively.
 * Conditions (ET Prop 1.9 + Lemma 1.1, re-derived):
 *  II3 (a,d,e): (4ad,e)=1, e=-1 mod 4a'd' (by construction), e=-u (mod (ad)_T), e' | 4a^2d+1, e_T | u+4a^2d
 *  I3  (c,d,f)=(a,d,e): same but f_T | u^2+4c^2d
 *  I1  (a,d,f)=(a,d,e): f | 4a^2d+1, f = -u (mod (ad)_T)
 * usage: review_m13b_target u11 u13 X     prints HIT lines and a summary. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned long long u64; typedef unsigned __int128 u128;
static u64 mulm(u64 a, u64 b, u64 m) { return (u64)((u128)(a % m) * (b % m) % m); }
static const u64 Q[2] = {11, 13}; static u64 QP[2][17]; static u64 U[2];
static int val(u64 x, int t) { int v = 0; while (x && x % Q[t] == 0 && v < 16) { x /= Q[t]; v++; } return v; }
/* (4 a^2 d + 1) mod m, with a = aT*ap, d = dT*dp */
static u64 F4(u64 aT, u64 ap, u64 dT, u64 dp, u64 m) {
    u64 a = mulm(aT, ap, m), d = mulm(dT, dp, m);
    return (mulm(mulm(4, mulm(a, a, m), m), d, m) + 1) % m;
}
int main(int argc, char **argv) {
    for (int t = 0; t < 2; t++) { QP[t][0] = 1; for (int k = 1; k <= 16; k++) QP[t][k] = QP[t][k-1] * Q[t]; }
    U[0] = strtoull(argv[1], 0, 10) % QP[0][16]; U[1] = strtoull(argv[2], 0, 10) % QP[1][16];
    u64 X = strtoull(argv[3], 0, 10); u64 L = (X + 1) / 4 + 1;
    uint32_t *spf = calloc(L + 1, 4);
    for (u64 i = 2; i <= L; i++) if (!spf[i]) for (u64 j = i; j <= L; j += i) if (!spf[j]) spf[j] = (uint32_t)i;
    u64 hits[3] = {0, 0, 0}, ntrip = 0, ncombo = 0; static u64 dv[1 << 15];
    for (u64 e = 3; e <= X; e += 4) {
        u64 n = (e + 1) / 4, B = 1, g = e; int vB[2], w[2];
        for (int t = 0; t < 2; t++) { vB[t] = 0; while (g % Q[t] == 0) { g /= Q[t]; B *= Q[t]; vB[t]++; } }
        for (int t = 0; t < 2; t++) w[t] = vB[t] ? 0 : val(e + U[t] % QP[t][16] , t);
        /* note: U[t] < q^16, e+U[t] fits; valuation capped at 16 (never reached for e<=1e12) */
        /* divisors of n that are prime to 143 (a' and d' must be T-free; n is prime to e so fine) */
        int nd = 1; dv[0] = 1; u64 x = n;
        while (x > 1) { u64 p = spf[x]; int k = 0; while (x % p == 0) { x /= p; k++; }
            int cur = nd; u64 pk = 1;
            for (int s = 1; s <= k; s++) { pk *= p; for (int i = 0; i < cur; i++) dv[nd++] = dv[i] * pk; } }
        for (int ia = 0; ia < nd; ia++) { u64 ap = dv[ia]; if (ap % 11 == 0 || ap % 13 == 0) continue;
          for (int id = 0; id < nd; id++) { u64 dp = dv[id]; if (dp % 11 == 0 || dp % 13 == 0) continue;
            if ((n / ap) % dp) continue; ntrip++;
            /* T-parts: alpha_t + delta_t <= w[t] */
            for (int a0 = 0; a0 <= w[0]; a0++) for (int d0 = 0; a0 + d0 <= w[0]; d0++)
            for (int a1 = 0; a1 <= w[1]; a1++) for (int d1 = 0; a1 + d1 <= w[1]; d1++) {
                ncombo++;
                u64 aT = QP[0][a0] * QP[1][a1], dT = QP[0][d0] * QP[1][d1];
                int okg = F4(aT, ap, dT, dp, g) == 0;          /* e' | 4a^2d+1 */
                if (okg) {
                    int ok3 = 1, ok3b = 1;
                    for (int t = 0; t < 2; t++) if (vB[t]) {
                        u64 qm = QP[t][vB[t]]; u64 s = (F4(aT, ap, dT, dp, qm) + qm - 1) % qm; /* 4a^2d mod q^v */
                        if ((s + U[t]) % qm) ok3 = 0;
                        if ((s + mulm(U[t], U[t], qm)) % qm) ok3b = 0;
                    }
                    if (ok3) { hits[0]++; printf("HIT II3 a=%llu*%llu d=%llu*%llu e=%llu\n", aT, ap, dT, dp, e); }
                    if (ok3b) { hits[1]++; printf("HIT I3 c=%llu*%llu d=%llu*%llu f=%llu\n", aT, ap, dT, dp, e); }
                    if (F4(aT, ap, dT, dp, e) == 0) { hits[2]++; printf("HIT I1 a=%llu*%llu d=%llu*%llu f=%llu\n", aT, ap, dT, dp, e); }
                }
            } } }
    }
    printf("SUMMARY u=(%llu,%llu) X=%llu triples=%llu Tcombos=%llu hits II3=%llu I3=%llu I1=%llu\n", U[0], U[1], X, ntrip, ncombo, hits[0], hits[1], hits[2]);
    return 0;
}
