// Numerical companion for EXCEPTIONAL_THETA.md, hypothesis H_EM (Section 5).
//
// Complete multiplier-identity system: for every M <= Q, M = 3 (mod 4),
// A = (M+1)/4, the forced classes R(M) = { -4D mod M : D | A^2 }  (notes Lemma 18.1).
// For every prime p in [P0, P0+span) we compute the first M (ascending) with
// p mod M in R(M).  We print, for a grid of Q' <= Q,
//   void(Q')    = fraction of primes with no forced class mod M <= Q'
//   mass_pr(Q') = sum_{M<=Q'} |R(M) cap units| / phi(M)   (prime-conditioned first moment)
//   ratio       = -log void / mass_pr
// H_EM ("no super-cubic effective mass") predicts that -log void stays O(mass);
// a growing ratio would indicate correlation-driven extra saving.
//
// build: g++ -O2 -std=c++17 -o /tmp/theta_void_primes scripts/theta_void_primes.cpp
// run:   /tmp/theta_void_primes Q P0 span
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
typedef unsigned long long u64;

static vector<pair<u64,int>> factor(u64 n) {
    vector<pair<u64,int>> f;
    for (u64 p = 2; p * p <= n; ++p) if (n % p == 0) { int e = 0; while (n % p == 0) { n /= p; ++e; } f.push_back({p, e}); }
    if (n > 1) f.push_back({n, 1});
    return f;
}
static u64 gcdu(u64 a, u64 b) { while (b) { u64 t = a % b; a = b; b = t; } return a; }

int main(int argc, char** argv) {
    if (argc < 4) { fprintf(stderr, "usage: Q P0 span\n"); return 1; }
    u64 Q = strtoull(argv[1], 0, 10), P0 = strtoull(argv[2], 0, 10), span = strtoull(argv[3], 0, 10);
    // forced-class bitsets
    vector<vector<uint8_t>> bits(Q + 1);
    vector<double> massAll(Q + 1, 0.0), massPr(Q + 1, 0.0);
    for (u64 M = 3; M <= Q; M += 4) {
        u64 A = (M + 1) / 4;
        auto f = factor(A);
        vector<u64> divs = {1};
        for (auto& pe : f) {  // divisors of A^2
            size_t sz = divs.size(); u64 pk = 1;
            for (int e = 1; e <= 2 * pe.second; ++e) { pk *= pe.first; for (size_t i = 0; i < sz; ++i) divs.push_back(divs[i] * pk); }
        }
        bits[M].assign(M, 0);
        u64 cnt = 0, cntu = 0;
        for (u64 D : divs) {
            u64 r = (M - (4 * (D % M)) % M) % M;
            if (!bits[M][r]) { bits[M][r] = 1; ++cnt; if (gcdu(r, M) == 1) ++cntu; }
        }
        // phi(M)
        u64 m = M, ph = M;
        for (auto& pe : factor(m)) ph = ph / pe.first * (pe.first - 1);
        massAll[M] = (double)cnt / M;
        massPr[M] = (double)cntu / ph;
    }
    // segmented sieve of primes in [P0, P0+span), in chunks of 1e8
    u64 lim = (u64)sqrtl((long double)(P0 + span)) + 1;
    vector<uint8_t> small(lim + 1, 1); small[0] = small[1] = 0;
    for (u64 i = 2; i * i <= lim; ++i) if (small[i]) for (u64 j = i * i; j <= lim; j += i) small[j] = 0;
    vector<u64> sp; for (u64 p = 2; p <= lim; ++p) if (small[p]) sp.push_back(p);
    vector<u64> firstHist(Q + 2, 0);  // index Q+1 = none
    u64 nprimes = 0;
    const u64 CH = 100000000ULL;
    vector<uint8_t> seg(CH);
    for (u64 lo = P0; lo < P0 + span; lo += CH) {
        u64 hi = min(lo + CH, P0 + span), len = hi - lo;
        fill(seg.begin(), seg.begin() + len, 1);
        for (u64 p : sp) {
            if (p * p >= hi) break;
            u64 s = max(p * p, (lo + p - 1) / p * p);
            for (u64 j = s; j < hi; j += p) seg[j - lo] = 0;
        }
        for (u64 i = 0; i < len; ++i) if (seg[i]) {
            u64 p = lo + i; if (p < 2) continue; ++nprimes;
            u64 hit = Q + 1;
            for (u64 M = 3; M <= Q; M += 4) if (bits[M][p % M]) { hit = M; break; }
            firstHist[hit]++;
        }
    }
    printf("# primes in [%llu,%llu): %llu ; Q=%llu\n", P0, P0 + span, nprimes, Q);
    printf("# %8s %12s %12s %10s %10s %10s\n", "Q'", "void", "voids", "mass_pr", "mass_all", "ratio");
    u64 surv = nprimes; double mp = 0, ma = 0; u64 nextQ = 10;
    for (u64 M = 1; M <= Q; ++M) {
        surv -= firstHist[M]; mp += massPr[M]; ma += massAll[M];
        if (M == nextQ || M == Q) {
            double v = (double)surv / nprimes;
            printf("  %8llu %12.4e %12llu %10.4f %10.4f %10.4f\n", M, v, surv, mp, ma, surv ? -log(v) / mp : NAN);
            nextQ = (u64)llround(nextQ * 1.5);
            if (nextQ <= M) nextQ = M + 1;
        }
    }
    return 0;
}
