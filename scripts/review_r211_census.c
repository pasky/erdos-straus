/* R211 from-scratch census for O213 (SHARP 4, SHARP 5, item (b)).
   Enumerates ALL words (c,m,s), letters >= 1, N = c*m*s - c - s in [1, X], N == 1 (mod 4),
   and records per N: least certificate vertex o (formal / interior), position class flags, counts.
   Certificate (N == 1 mod 4): some vertex of (h', c, m, s, h) is == 0 mod 4 (FRIEZE Cor 1.3).
   Positions (by parity): H = m even (o in {h,h'}); C = m odd, c xor s even... precisely
     edge {c,m}: o=h; {m,s}: o=h'; {h',c}: o=s; {s,h}: o=c; {h,h'}: o=m.
   Build: gcc -O2 -o /tmp/r211census scripts/review_r211_census.c ; run: /tmp/r211census X  */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

typedef long long ll;
enum { POS_H = 1, POS_C = 2, POS_M = 4 };

static uint32_t *minoF, *minoI;     /* least certificate o, 0 = none */
static uint8_t *posF, *posI;        /* position mask of certificates attaining min o */
static uint8_t *fl;                 /* bit0 H-cert formal, bit1 H-cert interior, bit2 C formal, bit3 C interior,
                                       bit4 M formal, bit5 M interior, bit6 4|m-cert formal, bit7 4|m interior */
static uint16_t *cntH, *cntC, *cntM; /* formal certificate counts with c <= s */
static uint16_t *cntHI;              /* interior H certificate count, c <= s */
static uint16_t *nInt;               /* number of interior certificate words (ordered) */

static int isprime(ll n) { if (n < 2) return 0; for (ll d = 2; d * d <= n; d++) if (n % d == 0) return 0; return 1; }
static int issq(ll n) { ll r = (ll)sqrtl((long double)n); while (r * r > n) r--; while ((r + 1) * (r + 1) <= n) r++; return r * r == n; }

int main(int argc, char **argv) {
    ll X = argc > 1 ? atoll(argv[1]) : 1000000;
    ll XC = argc > 2 ? atoll(argv[2]) : 1000000;  /* composite / small-range limit */
    size_t n = X + 1;
    minoF = calloc(n, 4); minoI = calloc(n, 4); posF = calloc(n, 1); posI = calloc(n, 1); fl = calloc(n, 1);
    cntH = calloc(n, 2); cntC = calloc(n, 2); cntM = calloc(n, 2); cntHI = calloc(n, 2); nInt = calloc(n, 2);
    if (!minoF || !minoI || !posF || !posI || !fl || !cntH || !cntC || !cntM || !cntHI || !nInt) { fprintf(stderr, "oom\n"); return 1; }
    ll nwords = 0;
    for (ll c = 1; c <= X + 2; c++) {
        for (ll m = 1;; m++) {
            ll g = c * m - 1;
            if (g == 0) continue;
            if (g - c > X) break;
            for (ll s = 1; s <= (X + c) / g; s++) {
                ll N = g * s - c;
                if (N < 1 || (N & 3) != 1) continue;
                nwords++;
                ll h = g, hp = m * s - 1;
                ll q[5] = { hp, c, m, s, h };
                int cert = 0;
                for (int i = 0; i < 5; i++) if ((q[i] & 3) == 0) cert = 1;
                if (!cert) continue;
                /* even edge and o */
                int ev[2], k = 0;
                for (int i = 0; i < 5; i++) if (!(q[i] & 1)) { if (k < 2) ev[k] = i; k++; }
                if (k != 2) { fprintf(stderr, "parity fail %lld %lld %lld\n", c, m, s); return 2; }
                int i0 = ((ev[1] - ev[0]) == 1) ? ev[0] : ev[1];
                if (!((ev[1] - ev[0]) == 1 || (ev[1] - ev[0]) == 4)) { fprintf(stderr, "adjacency fail\n"); return 2; }
                ll o = q[(i0 + 3) % 5];
                if ((o & 7) != 7 && (N & 7) == 1) { fprintf(stderr, "o mod 8 fail\n"); return 2; }
                int pos = (i0 == 1 || i0 == 2) ? POS_H : (i0 == 0 || i0 == 3) ? POS_C : POS_M;
                int interior = (c >= 2 && m >= 2 && s >= 2);
                uint32_t oo = o > 4000000000LL ? 4000000000U : (uint32_t)o;
                if (minoF[N] == 0 || oo < minoF[N]) { minoF[N] = oo; posF[N] = pos; } else if (oo == minoF[N]) posF[N] |= pos;
                if (interior) {
                    if (minoI[N] == 0 || oo < minoI[N]) { minoI[N] = oo; posI[N] = pos; } else if (oo == minoI[N]) posI[N] |= pos;
                    if (nInt[N] < 65535) nInt[N]++;
                }
                int b = pos == POS_H ? 0 : pos == POS_C ? 2 : 4;
                fl[N] |= 1 << b; if (interior) fl[N] |= 1 << (b + 1);
                if (m % 4 == 0) { fl[N] |= 64; if (interior) fl[N] |= 128; }
                if (c <= s) {
                    if (pos == POS_H) { if (cntH[N] < 65535) cntH[N]++; if (interior && cntHI[N] < 65535) cntHI[N]++; }
                    if (pos == POS_C && cntC[N] < 65535) cntC[N]++;
                    if (pos == POS_M && cntM[N] < 65535) cntM[N]++;
                }
            }
        }
    }
    printf("X=%lld words(N==1 mod 4)=%lld\n", X, nwords);

    /* ---- primes p == 1 (8) */
    char *comp = calloc(n, 1); for (ll i = 2; i * i <= X; i++) if (!comp[i]) for (ll j = i * i; j <= X; j += i) comp[j] = 1;
    for (int mode = 0; mode < 2; mode++) {
        uint32_t *mino = mode ? minoI : minoF; uint8_t *pp = mode ? posI : posF;
        ll np = 0, fail = 0, hist[4] = {0}, firstpos[3] = {0}, at7[3] = {0}, maxo = 0, maxp = 0, second = 0, secp = 0, ge119 = 0, ge119not120 = 0;
        for (ll p = 9; p <= X; p += 8) {
            if (comp[p]) continue;
            np++;
            uint32_t o = mino[p];
            if (!o) { fail++; continue; }
            if (o == 7) hist[0]++; else if (o == 15) hist[1]++; else if (o == 23) hist[2]++; else hist[3]++;
            int fp = (pp[p] & POS_H) ? 0 : (pp[p] & POS_C) ? 1 : 2; firstpos[fp]++;
            if (o == 7) for (int t = 0; t < 3; t++) if (pp[p] & (1 << t)) at7[t]++;
            if (o > maxo) { second = maxo; secp = maxp; maxo = o; maxp = p; } else if (o > second) { second = o; secp = p; }
            if (o >= 119) { ge119++; if (p % 120 != 1) ge119not120++; }
        }
        printf("[%s] primes p==1(8): %lld, no certificate: %lld; o*=7:%lld (%.2f%%) 15:%lld 23:%lld >=31:%lld\n",
               mode ? "interior" : "formal", np, fail, hist[0], 100.0 * hist[0] / np, hist[1], hist[2], hist[3]);
        printf("   first-success pos (ties H>C>M): H %lld C %lld M %lld; at o*=7 firing: H %lld C %lld M %lld\n",
               firstpos[0], firstpos[1], firstpos[2], at7[0], at7[1], at7[2]);
        printf("   max o* = %lld at p=%lld; second %lld at p=%lld; #o*>=119: %lld, of which not ==1 (120): %lld\n",
               maxo, maxp, second, secp, ge119, ge119not120);
        printf("   hard primes (o*>=119):");
        for (ll p = 9; p <= X; p += 8) if (!comp[p] && mino[p] >= 119) printf(" %lld:%u", p, mino[p]);
        printf("\n");
    }
    /* ---- SQ_H and position classes at primes */
    {
        ll np8 = 0, fH[2] = {0}, fC[2] = {0}, fM[2] = {0}, f4m = 0, np4 = 0, fH4[2] = {0};
        double sH = 0, sC = 0, sM = 0, sH840 = 0, sC840 = 0, sM840 = 0; ll n840 = 0; int minH = 99999; ll minHp[8]; int nmin = 0;
        double sHI = 0; int minHI = 99999; ll minHIp = 0;
        printf("4|m-slice failures at primes ==1(8) <= %lld:", XC);
        for (ll p = 5; p <= X; p += 4) {
            if (comp[p]) continue;
            np4++;
            if (!(fl[p] & 1)) fH4[0]++;
            if (!(fl[p] & 2)) fH4[1]++;
            if ((p & 7) != 1) continue;
            np8++;
            for (int t = 0; t < 2; t++) { if (!(fl[p] & (1 << t))) fH[t]++; if (!(fl[p] & (4 << t))) fC[t]++; if (!(fl[p] & (16 << t))) fM[t]++; }
            if (!(fl[p] & 64)) { f4m++; if (p <= XC) printf(" %lld", p); }
            sH += cntH[p]; sC += cntC[p]; sM += cntM[p]; sHI += cntHI[p];
            if (p % 840 == 1) { n840++; sH840 += cntH[p]; sC840 += cntC[p]; sM840 += cntM[p]; }
            if (cntH[p] < minH) { minH = cntH[p]; nmin = 0; }
            if (cntH[p] == minH && nmin < 8) minHp[nmin++] = p;
            if (cntHI[p] < minHI) { minHI = cntHI[p]; minHIp = p; }
        }
        printf("  (total to X: %lld)\n", f4m);
        printf("primes ==1(8): %lld; SQ_H fails formal %lld interior %lld; class C fails formal %lld interior %lld; class M fails formal %lld interior %lld\n",
               np8, fH[0], fH[1], fC[0], fC[1], fM[0], fM[1]);
        printf("primes ==1(4): %lld; SQ_H fails formal %lld interior %lld\n", np4, fH4[0], fH4[1]);
        printf("mean counts (formal, c<=s): H %.2f C %.2f M %.2f; at p==1(840) (%lld primes): %.2f %.2f %.2f; mean interior H %.2f\n",
               sH / np8, sC / np8, sM / np8, n840, sH840 / n840, sC840 / n840, sM840 / n840, sHI / np8);
        printf("min formal H count %d at", minH); for (int i = 0; i < nmin; i++) printf(" %lld", minHp[i]);
        printf("; min interior H count %d at %lld\n", minHI, minHIp);
    }
    /* ---- non-square N == 1 (4) <= XC, odd squares */
    {
        ll nn = 0, f5F = 0, f5I = 0, fHF = 0, fHI = 0, sqcert = 0, nsq = 0;
        printf("non-square N==1(4) <= %lld: SQ5 formal fails:", XC);
        for (ll N = 5; N <= XC; N += 4) { if (issq(N)) continue; if (!minoF[N]) printf(" %lld", N); }
        printf("\n  SQ5 interior fails:");
        for (ll N = 5; N <= XC; N += 4) { if (issq(N)) continue; if (!minoI[N]) printf(" %lld", N); }
        printf("\n  SQ_H formal fails:");
        for (ll N = 5; N <= XC; N += 4) {
            if (issq(N)) { nsq++; if (minoF[N]) sqcert++; continue; }
            nn++; if (!minoF[N]) f5F++; if (!minoI[N]) f5I++;
            if (!(fl[N] & 1)) { fHF++; printf(" %lld%s", N, isprime(N) ? "(P)" : ""); }
            if (!(fl[N] & 2)) fHI++;
        }
        printf("\n  count %lld non-squares; SQ5 fails F %lld I %lld; SQ_H fails formal %lld interior %lld\n", nn, f5F, f5I, fHF, fHI);
        printf("odd squares ==1(4) in [5,%lld]: %lld, with any certificate: %lld\n", XC, nsq, sqcert);
    }
    return 0;
}
