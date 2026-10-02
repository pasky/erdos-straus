// EXCEPTIONAL_BALANCED.md §3.3 (route 8, part iii): void probabilities among real
// primes for the Case-B forced-class system R(M) = {-4D mod M : D | ((M+1)/4)^2},
// M = 3 (mod 4), M <= Q, restricted to three nested families by modulus type
// (P = P(M), P2 = P(M/P), eta = 1/4):
//   F1 "dom"     : P >= M^{2/3}
//   F2 "nontwin" : dom, or gapped P >= P2^{1+eta}
//   F3 "all"     : everything (adds the eta-twin moduli)
//   F4 "dom+twin": dom and eta-twin, no gapped  (order-symmetric comparison,
//                  review D15)
// For each prime p in [P0, P0+span) we find the first M <= Q in each family with
// p mod M in R(M), and print void(Q') and the prime-conditioned masses
// mass_pr(Q') = sum |R(M) cap units|/phi(M) per family.  EVIDENCE only.
// build: g++ -O2 -std=c++17 -o /tmp/balanced_void scripts/balanced_void.cpp
// run:   /tmp/balanced_void Q P0 span
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
static u64 lpf(u64 n) { u64 P = 1; for (auto& pe : factor(n)) P = max(P, pe.first); return P; }

int main(int argc, char** argv) {
    if (argc < 4) { fprintf(stderr, "usage: Q P0 span\n"); return 1; }
    u64 Q = strtoull(argv[1], 0, 10), P0 = strtoull(argv[2], 0, 10), span = strtoull(argv[3], 0, 10);
    vector<vector<uint8_t>> bits(Q + 1);
    vector<int> type(Q + 1, -1);            // 0 dom, 1 gap, 2 twin
    vector<double> mass[3];
    for (int t = 0; t < 3; ++t) mass[t].assign(Q + 1, 0.0);
    for (u64 M = 3; M <= Q; M += 4) {
        u64 P = lpf(M), r = M / P, P2 = r > 1 ? lpf(r) : 1;
        int t;
        if (pow((double)P, 1.5) >= (double)M) t = 0;
        else if (pow((double)P2, 1.25) <= (double)P) t = 1;
        else t = 2;
        type[M] = t;
        u64 A = (M + 1) / 4;
        auto f = factor(A);
        vector<u64> divs = {1};
        for (auto& pe : f) {
            size_t sz = divs.size(); u64 pk = 1;
            for (int e = 1; e <= 2 * pe.second; ++e) { pk *= pe.first; for (size_t i = 0; i < sz; ++i) divs.push_back(divs[i] * pk); }
        }
        bits[M].assign(M, 0);
        u64 cntu = 0;
        for (u64 D : divs) {
            u64 rr = (M - (4 * (D % M)) % M) % M;
            if (!bits[M][rr]) { bits[M][rr] = 1; if (gcdu(rr, M) == 1) ++cntu; }
        }
        u64 ph = M;
        for (auto& pe : factor(M)) ph = ph / pe.first * (pe.first - 1);
        mass[t][M] = (double)cntu / ph;
    }
    u64 lim = (u64)sqrtl((long double)(P0 + span)) + 1;
    vector<uint8_t> small(lim + 1, 1); small[0] = small[1] = 0;
    vector<u64> sp;
    for (u64 i = 2; i <= lim; ++i) if (small[i]) { sp.push_back(i); for (u64 j = i * i; j <= lim; j += i) small[j] = 0; }
    vector<u64> hist[4];
    for (int t = 0; t < 4; ++t) hist[t].assign(Q + 2, 0);   // first hit M (Q+1 = void)
    u64 nprimes = 0;
    const u64 CH = 100000000ULL;
    vector<uint8_t> seg;
    for (u64 lo = P0; lo < P0 + span; lo += CH) {
        u64 hi = min(lo + CH, P0 + span);
        seg.assign(hi - lo, 1);
        for (u64 p : sp) {
            if (p * p >= hi) break;
            u64 s = max(p * p, (lo + p - 1) / p * p);
            for (u64 j = s; j < hi; j += p) seg[j - lo] = 0;
        }
        for (u64 i = 0; i < hi - lo; ++i) if (seg[i]) {
            u64 n = lo + i; if (n < 2) continue;
            ++nprimes;
            u64 first[4] = {Q + 1, Q + 1, Q + 1, Q + 1};
            int found = 0;
            for (u64 M = 3; M <= Q && found < 4; M += 4) {
                if (!bits[M][n % M]) continue;
                int t = type[M];
                // family k contains types <= k (0:dom, 1:dom+gap, 2:all); 3: dom+twin
                for (int k = t; k < 3; ++k) if (first[k] == Q + 1) { first[k] = M; ++found; }
                if (t != 1 && first[3] == Q + 1) { first[3] = M; ++found; }
            }
            for (int k = 0; k < 4; ++k) hist[k][first[k]]++;
        }
    }
    printf("# Q=%llu P0=%llu span=%llu primes=%llu\n", Q, P0, span, nprimes);
    printf("# Q' | voids dom nontwin all domtwin | mass_pr dom nontwin all domtwin\n");
    u64 surv[4] = {nprimes, nprimes, nprimes, nprimes};
    double cm[4] = {0, 0, 0, 0};
    u64 next = 10;
    for (u64 M = 1; M <= Q; ++M) {
        for (int k = 0; k < 4; ++k) surv[k] -= hist[k][M];
        if (M >= 3 && (M % 4) == 3) {
            int t = type[M];
            for (int k = t; k < 3; ++k) cm[k] += mass[t][M];
            if (t != 1) cm[3] += mass[t][M];
        }
        if (M == next || M == Q) {
            printf("%llu %llu %llu %llu %llu %.6f %.6f %.6f %.6f\n", M, surv[0], surv[1], surv[2], surv[3], cm[0], cm[1], cm[2], cm[3]);
            next = (u64)(next * 1.3) + 1;
        }
    }
    return 0;
}
