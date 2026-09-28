// Survey of ALL primes p = 1 (mod 24), p a residue mod 5 and 7 (the other
// primes have dist 2 by DEPTH3.md Lemma 4), in [P0,P1): output those for which
// the two-move criterion (9) is NOT established by this program.
// For each divisor h of t^2 (ascending) it uses the a-interval when
// (4t^2+h)/(4h-1) <= 2e5, else a full 64-bit factorization of m = ph - t when
// m < 2^64; larger m are skipped ("undecided"). A prime is printed unless some
// h succeeds, so the output is a SUPERSET of the (9)-failures; it is
// re-checked exactly by depth3_batch.py (without --skip9).
// Build: g++ -O3 -march=native -std=c++17 -pthread -o /tmp/d3all scripts/depth3_allp.cpp
// Run:   /tmp/d3all P0 P1 THREADS > cand.txt
#include <algorithm>
#include <atomic>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <mutex>
#include <thread>
#include <vector>
typedef unsigned long long u64;
typedef __uint128_t u128;
typedef __int128 i128;

static u64 mulmod(u64 a, u64 b, u64 m) { return (u128)a * b % m; }
static u64 powmod(u64 a, u64 e, u64 m) {
    u64 r = 1 % m; a %= m;
    while (e) { if (e & 1) r = mulmod(r, a, m); a = mulmod(a, a, m); e >>= 1; }
    return r;
}
static bool isprime64(u64 n) {
    if (n < 2) return false;
    static const u64 sp[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (u64 q : sp) { if (n % q == 0) return n == q; }
    u64 d = n - 1; int s = 0;
    while (!(d & 1)) { d >>= 1; ++s; }
    for (u64 a : sp) {
        u64 x = powmod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool comp = true;
        for (int r = 1; r < s; ++r) { x = mulmod(x, x, n); if (x == n - 1) { comp = false; break; } }
        if (comp) return false;
    }
    return true;
}
static u64 gcdu(u64 a, u64 b) { while (b) { u64 t = a % b; a = b; b = t; } return a; }
static u64 rho(u64 n) {
    if (n % 2 == 0) return 2;
    for (u64 c = 1;; ++c) {
        u64 y = 2, x = 2, g = 1, q = 1, ys = 2;
        u64 m = 128, r = 1;
        auto f = [&](u64 v) { return (mulmod(v, v, n) + c) % n; };
        do {
            x = y;
            for (u64 i = 0; i < r; ++i) y = f(y);
            u64 k = 0;
            do {
                ys = y;
                for (u64 i = 0; i < std::min(m, r - k); ++i) { y = f(y); q = mulmod(q, x > y ? x - y : y - x, n); }
                g = gcdu(q, n); k += m;
            } while (k < r && g == 1);
            r <<= 1;
        } while (g == 1);
        if (g == n) {
            do { ys = f(ys); g = gcdu(x > ys ? x - ys : ys - x, n); } while (g == 1);
        }
        if (g != n) return g;
    }
}
static void factor_rec(u64 n, std::vector<u64>& out) {
    if (n == 1) return;
    if (isprime64(n)) { out.push_back(n); return; }
    u64 d = rho(n);
    factor_rec(d, out); factor_rec(n / d, out);
}
static const int NSMALL = 200;
static std::vector<u64> smallp;
typedef std::vector<std::pair<u64, int>> Fac;
static Fac factor(u64 n) {
    Fac f;
    for (u64 q : smallp) {
        if (q * q > n) break;
        if (n % q == 0) { int e = 0; while (n % q == 0) { n /= q; ++e; } f.push_back({q, e}); }
    }
    if (n > 1) {
        std::vector<u64> ps; factor_rec(n, ps); std::sort(ps.begin(), ps.end());
        for (u64 q : ps) { if (!f.empty() && f.back().first == q) f.back().second++; else f.push_back({q, 1}); }
    }
    return f;
}
// is there a divisor D of (prod f)^2 with D = target mod K ?
static bool hit(const Fac& f, u64 K, u64 target) {
    std::vector<u64> res{1 % K};
    for (auto [q, e] : f) {
        size_t n0 = res.size();
        u64 qm = q % K, pw = 1 % K;
        for (int k = 1; k <= 2 * e; ++k) {
            pw = mulmod(pw, qm, K);
            for (size_t i = 0; i < n0; ++i) res.push_back(mulmod(res[i], pw, K));
        }
        std::sort(res.begin(), res.end()); res.erase(std::unique(res.begin(), res.end()), res.end());
    }
    return std::binary_search(res.begin(), res.end(), target % K);
}
static Fac merge(Fac a, const Fac& b) {
    for (auto [q, e] : b) {
        bool found = false;
        for (auto& pr : a) if (pr.first == q) { pr.second += e; found = true; }
        if (!found) a.push_back({q, e});
    }
    return a;
}


static std::mutex outmu;
static std::atomic<u64> ntested{0}, nsurv{0};

static bool crit9_general(u64 p) {
    u64 t = (p - 1) / 4;
    Fac ft = factor(t);
    std::vector<u64> hs{1};
    for (auto [q, e] : ft) {
        size_t n0 = hs.size(); u64 pw = 1;
        for (int k = 1; k <= 2 * e; ++k) { pw *= q; for (size_t i = 0; i < n0; ++i) hs.push_back(hs[i] * pw); }
    }
    std::sort(hs.begin(), hs.end());
    for (u64 h64 : hs) {
        u128 h = h64, K = 4 * h - 1;
        u128 bound = ((u128)4 * t * t + h) / K;
        if (bound <= 200000) {
            u128 amax = std::min<u128>(bound, t);
            for (u128 a = 1; a <= amax; ++a) {
                u128 e = (4 * a - 1) * h - a, x = t + a, r = x % e;
                if (r * r % e == 0) return true;
            }
            continue;
        }
        u128 m = (u128)p * h - t;
        if (m >> 64) continue;  // undecided here; left for the exact re-check
        if (hit(factor((u64)m), (u64)K, (u64)((K - h % K) % K))) return true;
    }
    return false;
}

int main(int argc, char** argv) {
    if (argc < 4) { fprintf(stderr, "usage: P0 P1 THREADS\n"); return 1; }
    u64 P0 = strtoull(argv[1], 0, 10), P1 = strtoull(argv[2], 0, 10);
    int T = atoi(argv[3]);
    if (P1 > (1ULL << 40)) { fprintf(stderr, "P1 too large\n"); return 1; }
    for (u64 k = 2; smallp.size() < NSMALL; ++k) if (isprime64(k)) smallp.push_back(k);
    const u64 CH = 24000000;
    std::atomic<u64> next{P0 - P0 % 24};
    auto worker = [&]() {
        for (;;) {
            u64 lo = next.fetch_add(CH);
            if (lo >= P1) break;
            u64 hi = std::min(P1, lo + CH);
            std::vector<u64> out;
            for (u64 p = lo + 1; p < hi; p += 24) {
                if (p < P0 || p < 100) continue;
                u64 r5 = p % 5, r7 = p % 7;
                if (!(r5 == 1 || r5 == 4) || !(r7 == 1 || r7 == 2 || r7 == 4)) continue;
                if (!isprime64(p)) continue;
                ntested++;
                if (!crit9_general(p)) out.push_back(p);
            }
            if (!out.empty()) {
                std::lock_guard<std::mutex> g(outmu);
                for (u64 p : out) printf("%llu\n", p);
                fflush(stdout);
                nsurv += out.size();
            }
        }
    };
    std::vector<std::thread> th;
    for (int i = 0; i < T; ++i) th.emplace_back(worker);
    for (auto& x : th) x.join();
    fprintf(stderr, "p in [%llu,%llu): tested %llu primes (1 mod 24, residue mod 5,7), candidates %llu\n",
            P0, P1, (u64)ntested, (u64)nsurv);
}
