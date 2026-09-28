// Prefilter for the depth-3 search: primes p = 4*s*q + 1 (q prime, q > s)
// for which the two-move criterion (9) FAILS (seed distance >= 3).
// Exact for these inputs: every h | t^2 = s^2 q^2 is tested, either by the
// a-interval  (4a-1)h - a | (t+a)^2, 1 <= a <= min(t, (4t^2+h)/(4h-1)),
// or by a divisor D | (ph-t)^2 with D = -h (mod 4h-1) from a full
// factorization (64-bit deterministic Miller-Rabin + Pollard rho).
// Survivors are re-checked (and families A/B run) by scripts/depth3.py.
//
// Build: g++ -O3 -march=native -std=c++17 -pthread -o /tmp/d3sieve scripts/depth3_sieve.cpp
// Run:   /tmp/d3sieve S Q0 Q1 THREADS  > survivors.txt
#include <algorithm>
#include <atomic>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <mutex>
#include <thread>
#include <vector>
#include <map>
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

struct Job { u64 s; u64 q0, q1; };
static std::mutex outmu;
static std::atomic<u64> ntested{0}, nsurv{0};

// returns true iff criterion (9) succeeds
static bool crit9(u64 s, u64 q, const std::vector<u64>& cs) {
    u64 t = s * q, p = 4 * t + 1;
    // order: j=0 small c first, then j=1, then j=2
    for (int j = 0; j <= 2; ++j) {
        for (u64 c : cs) {
            u128 h = c; for (int k = 0; k < j; ++k) h *= q;
            u128 K = 4 * h - 1;
            u128 bound = ((u128)4 * t * t + h) / K;
            if (bound <= 200000 || j == 2) {
                u128 amax = std::min<u128>(bound, t);
                for (u128 a = 1; a <= amax; ++a) {
                    u128 e = (4 * a - 1) * h - a;
                    u128 x = t + a;
                    if (x % e == 0) return true;
                    // (t+a)^2 may exceed 128 bits only for huge t; t < 2^60 here
                    if ((x % e) * (x % e) % e == 0) return true;
                }
                continue;
            }
            // factor m = p h - t
            Fac f;
            if (j == 0) { f = factor((u64)(p * c - t)); }
            else { f = merge(factor(p * c - s), Fac{{q, 1}}); } // m = q (p c - s)
            u64 K64 = (u64)K; u64 target = (u64)((K - h % K) % K);
            if (hit(f, K64, target)) return true;
        }
    }
    return false;
}

int main(int argc, char** argv) {
    if (argc < 5) { fprintf(stderr, "usage: S Q0 Q1 THREADS\n"); return 1; }
    u64 s = strtoull(argv[1], 0, 10), Q0 = strtoull(argv[2], 0, 10), Q1 = strtoull(argv[3], 0, 10);
    int T = atoi(argv[4]);
    for (u64 k = 2; smallp.size() < NSMALL; ++k) if (isprime64(k)) smallp.push_back(k);
    std::vector<u64> cs;
    for (u64 c = 1; c <= s * s; ++c) if ((s * s) % c == 0) cs.push_back(c);
    if (Q0 <= s) Q0 = s + 1;
    const u64 CH = 1000000;
    std::atomic<u64> next{Q0};
    auto worker = [&]() {
        std::vector<char> comp;
        for (;;) {
            u64 lo = next.fetch_add(CH);
            if (lo >= Q1) break;
            u64 hi = std::min(Q1, lo + CH);
            std::vector<std::pair<u64, u64>> out;
            for (u64 q = lo | 1; q < hi; q += 2) {
                // cheap prefilter by small primes for q and p
                u64 p = 4 * s * q + 1;
                bool bad = false;
                for (int i = 1; i < 30; ++i) { u64 r = smallp[i]; if ((q % r == 0 && q != r) || (p % r == 0 && p != r)) { bad = true; break; } }
                if (bad || !isprime64(q) || !isprime64(p) || s % q == 0) continue;
                ntested++;
                if (!crit9(s, q, cs)) out.push_back({q, p});
            }
            if (!out.empty()) {
                std::lock_guard<std::mutex> g(outmu);
                for (auto [q, p] : out) printf("%llu %llu\n", p, q);
                fflush(stdout);
                nsurv += out.size();
            }
        }
    };
    std::vector<std::thread> th;
    for (int i = 0; i < T; ++i) th.emplace_back(worker);
    for (auto& x : th) x.join();
    fprintf(stderr, "s=%llu q in [%llu,%llu): tested %llu primes, crit9-fail %llu\n", s, Q0, Q1,
            (u64)ntested, (u64)nsurv);
}
