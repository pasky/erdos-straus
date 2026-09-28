// Complete enumeration of the signed ES refactor graph at one prime p = 4t+1,
// with connected components.  Finite evidence only; NOT a proof of anything.
//
// Method (SIGNED_REFACTOR.md §3): every vertex has a positive p-free
// denominator x <= 2t, and is (x, p*m, p*x*m/f) with f = (4x-p)m - x a
// nonzero signed divisor of p*x^2.  We enumerate x in [1,2t], every divisor
// d | x^2 and f in {d,-d,pd,-pd} with f = -x (mod 4x-p).  This is exact and
// has no height cutoff.  Components: union-find on shared denominators.
//
// Build: g++ -std=c++17 -O3 -fopenmp -march=native scripts/signed_components.cpp -o /tmp/signed_components
// Run:   /tmp/signed_components P [--threads K] [--dump S] [--query DEN]... [--path DEN]...
// Output: one JSON line summary; with --dump S, every NON-SEED sterile
//   component of size >= S is printed as lines "C <id> <size>" followed by
//   "V x y z" lines (exact integers) -- recheck them with Python.
// Range: p < 2^31 so that all denominators (|pm| <= p^4/4) fit in __int128.
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <numeric>
#include <string>
#include <vector>
#include <omp.h>

typedef __int128 i128;
typedef unsigned __int128 u128;

static std::string s128(i128 v) {
    if (v == 0) return "0";
    bool neg = v < 0;
    u128 u = neg ? (u128)(-(v + 1)) + 1 : (u128)v;
    std::string s;
    while (u) { s.push_back(char('0' + int(u % 10))); u /= 10; }
    if (neg) s.push_back('-');
    std::reverse(s.begin(), s.end());
    return s;
}

struct Vtx { i128 a, b, c; };
static bool operator<(const Vtx& u, const Vtx& v) {
    if (u.a != v.a) return u.a < v.a;
    if (u.b != v.b) return u.b < v.b;
    return u.c < v.c;
}
static bool operator==(const Vtx& u, const Vtx& v) { return u.a == v.a && u.b == v.b && u.c == v.c; }

static i128 gcd128(i128 a, i128 b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b) { i128 r = a % b; a = b; b = r; }
    return a;
}

static uint64_t mulmod(uint64_t a, uint64_t b, uint64_t m) { return (uint64_t)((u128)a * b % m); }
static int64_t inv_mod(int64_t a, int64_t m) {  // m >= 1, gcd(a,m)=1
    if (m == 1) return 0;
    int64_t g = m, x = 0, x1 = 1, a1 = ((a % m) + m) % m;
    int64_t b = a1;
    // extended Euclid on (b, g)
    int64_t old_r = b, r = g, old_s = 1, s = 0;
    while (r) { int64_t qq = old_r / r; int64_t tmp = old_r - qq * r; old_r = r; r = tmp; tmp = old_s - qq * s; old_s = s; s = tmp; }
    (void)x; (void)x1;
    if (old_r != 1) { fprintf(stderr, "inverse failure\n"); exit(3); }
    return ((old_s % m) + m) % m;
}

// identity check modulo a 61-bit prime (sanity; the construction is exact)
static const uint64_t MP = 2305843009213693951ULL;  // 2^61-1
static uint64_t red(i128 v) { i128 r = v % (i128)MP; if (r < 0) r += MP; return (uint64_t)r; }
static bool check_mod(uint64_t p, const Vtx& v) {
    uint64_t x = red(v.a), y = red(v.b), z = red(v.c);
    uint64_t lhs = mulmod(4, mulmod(x, mulmod(y, z, MP), MP), MP);
    uint64_t s = (mulmod(x, y, MP) + mulmod(x, z, MP)) % MP;
    s = (s + mulmod(y, z, MP)) % MP;
    return lhs == mulmod(p % MP, s, MP);
}

int main(int argc, char** argv) {
    if (argc < 2) { fprintf(stderr, "usage: P [--threads K] [--dump S]\n"); return 1; }
    uint64_t p = strtoull(argv[1], nullptr, 10);
    int threads = 8; long dump = -1; std::vector<i128> queries, paths;
    for (int i = 2; i < argc; ++i) {
        if (!strcmp(argv[i], "--threads") && i + 1 < argc) threads = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--dump") && i + 1 < argc) dump = atol(argv[++i]);
        else if (!strcmp(argv[i], "--path") && i + 1 < argc) paths.push_back((i128)strtoll(argv[++i], nullptr, 10));
        else if (!strcmp(argv[i], "--query") && i + 1 < argc) queries.push_back((i128)strtoll(argv[++i], nullptr, 10));
        else { fprintf(stderr, "bad arg %s\n", argv[i]); return 1; }
    }
    if (p < 5 || p % 4 != 1 || p >= (1ULL << 31)) { fprintf(stderr, "need p=1 mod 4, 5<=p<2^31\n"); return 1; }
    // primality by trial division (p < 2^31)
    for (uint64_t d = 2; d * d <= p; ++d) if (p % d == 0) { fprintf(stderr, "p not prime\n"); return 1; }
    const uint64_t t = (p - 1) / 4, N = 2 * t;
    omp_set_num_threads(threads);

    // primes up to sqrt(N)
    uint64_t R = 1; while ((R + 1) * (R + 1) <= N) ++R;
    std::vector<uint32_t> primes;
    {
        std::vector<char> comp(R + 1, 0);
        for (uint64_t i = 2; i <= R; ++i) if (!comp[i]) { primes.push_back((uint32_t)i); for (uint64_t j = i * i; j <= R; j += i) comp[j] = 1; }
    }
    const uint64_t B = 1 << 15;
    const uint64_t nblocks = (N + B) / B;
    std::vector<std::vector<Vtx>> found(threads);

#pragma omp parallel
    {
        int tid = omp_get_thread_num();
        std::vector<uint64_t> rem(B);
        std::vector<uint32_t> fp(B * 12);
        std::vector<uint8_t> fe(B * 12), nf(B);
        std::vector<uint64_t> divs;
        divs.reserve(1 << 16);
        std::vector<Vtx>& out = found[tid];
#pragma omp for schedule(dynamic, 1)
        for (uint64_t blk = 0; blk < nblocks; ++blk) {
            uint64_t L = blk * B + 1, H = std::min(N, L + B - 1);
            if (L > N) continue;
            uint64_t len = H - L + 1;
            for (uint64_t i = 0; i < len; ++i) { rem[i] = L + i; nf[i] = 0; }
            for (uint32_t ell : primes) {
                uint64_t first = ((L + ell - 1) / ell) * ell;
                for (uint64_t y = first; y <= H; y += ell) {
                    uint64_t i = y - L; uint8_t e = 0;
                    while (rem[i] % ell == 0) { rem[i] /= ell; ++e; }
                    fp[i * 12 + nf[i]] = ell; fe[i * 12 + nf[i]] = e; ++nf[i];
                }
            }
            for (uint64_t i = 0; i < len; ++i) {
                uint64_t x = L + i;
                if (rem[i] > 1) { fp[i * 12 + nf[i]] = (uint32_t)rem[i]; fe[i * 12 + nf[i]] = 1; ++nf[i]; }
                // divisors of x^2
                divs.clear(); divs.push_back(1);
                for (int k = 0; k < nf[i]; ++k) {
                    uint64_t ell = fp[i * 12 + k]; int e2 = 2 * fe[i * 12 + k];
                    size_t old = divs.size(); uint64_t pw = 1;
                    for (int j = 0; j < e2; ++j) { pw *= ell; for (size_t u = 0; u < old; ++u) divs.push_back(divs[u] * pw); }
                }
                int64_t q = 4 * (int64_t)x - (int64_t)p;
                int64_t Q = q < 0 ? -q : q;
                // want f = -x (mod q), f = s*d with s in {1,-1,p,-p}
                int64_t xm = (int64_t)(x % (uint64_t)Q);
                int64_t pinv = inv_mod((int64_t)(p % (uint64_t)Q), Q);
                int64_t tg[4];
                tg[0] = (Q - xm) % Q;                    // s=1: d = -x
                tg[1] = xm % Q;                          // s=-1: d = x
                tg[2] = (int64_t)mulmod((uint64_t)((Q - xm) % Q), (uint64_t)pinv, (uint64_t)Q);  // s=p
                tg[3] = (int64_t)mulmod((uint64_t)xm, (uint64_t)pinv, (uint64_t)Q);              // s=-p
                for (uint64_t d : divs) {
                    int64_t r = (int64_t)(d % (uint64_t)Q);
                    for (int s = 0; s < 4; ++s) {
                        if (r != tg[s]) continue;
                        i128 f = (i128)d;
                        if (s >= 2) f *= (i128)p;
                        if (s & 1) f = -f;
                        i128 num = (i128)x + f;
                        if (num % q) { fprintf(stderr, "congruence bug\n"); exit(4); }
                        i128 m = num / q;
                        if (m == 0) continue;
                        if (m % (i128)p == 0) { fprintf(stderr, "m divisible by p\n"); exit(4); }
                        i128 g = gcd128(f, m);
                        i128 fg = f / g, mg = m / g;
                        i128 px = (i128)p * (i128)x;
                        if (px % fg) { fprintf(stderr, "divisibility bug\n"); exit(4); }
                        i128 z = (px / fg) * mg;
                        i128 a3[3] = {(i128)x, (i128)p * m, z};
                        std::sort(a3, a3 + 3);
                        Vtx v{a3[0], a3[1], a3[2]};
                        if (!check_mod(p, v)) { fprintf(stderr, "identity failure\n"); exit(4); }
                        out.push_back(v);
                    }
                }
            }
        }
    }
    std::vector<Vtx> V;
    for (auto& f : found) { V.insert(V.end(), f.begin(), f.end()); std::vector<Vtx>().swap(f); }
    std::sort(V.begin(), V.end());
    V.erase(std::unique(V.begin(), V.end()), V.end());
    size_t n = V.size();
    // union-find via denominators
    std::vector<size_t> par(n);
    std::iota(par.begin(), par.end(), 0);
    auto find = [&](size_t u) { while (par[u] != u) { par[u] = par[par[u]]; u = par[u]; } return u; };
    std::vector<std::pair<i128, size_t>> den;
    den.reserve(3 * n);
    for (size_t i = 0; i < n; ++i) {
        den.push_back({V[i].a, i});
        if (V[i].b != V[i].a) den.push_back({V[i].b, i});
        if (V[i].c != V[i].b) den.push_back({V[i].c, i});
    }
    std::sort(den.begin(), den.end(), [](const std::pair<i128, size_t>& u, const std::pair<i128, size_t>& v) { return u.first < v.first || (u.first == v.first && u.second < v.second); });
    for (size_t i = 1; i < den.size(); ++i)
        if (den[i].first == den[i - 1].first) { size_t a = find(den[i].second), b = find(den[i - 1].second); if (a != b) par[a] = b; }
    std::vector<size_t> sz(n, 0), pos(n, 0);
    size_t npos = 0;
    for (size_t i = 0; i < n; ++i) { size_t r = find(i); sz[r]++; if (V[i].a > 0) { pos[r]++; npos++; } }
    Vtx sd{-(i128)2 * p * t, -(i128)2 * p * t, (i128)t};
    size_t seedi = std::lower_bound(V.begin(), V.end(), sd) - V.begin();
    if (seedi >= n || !(V[seedi] == sd)) { fprintf(stderr, "seed missing\n"); return 5; }
    size_t sroot = find(seedi);
    std::map<size_t, size_t> sterile_hist;
    size_t ncomp = 0, npcomp = 0, maxster = 0, maxster_root = 0, npos_nonseed_max = 0;
    for (size_t i = 0; i < n; ++i) if (find(i) == i) {
        ncomp++;
        if (i == sroot) continue;
        if (pos[i] == 0) { sterile_hist[sz[i]]++; if (sz[i] > maxster) { maxster = sz[i]; maxster_root = i; } }
        else { npcomp++; npos_nonseed_max = std::max(npos_nonseed_max, sz[i]); }
    }
    (void)maxster_root;
    printf("{\"p\": %llu, \"V\": %zu, \"pos\": %zu, \"ncomp\": %zu, \"seedsize\": %zu, \"seedpos\": %zu, \"maxsterile\": %zu, \"nposcomp_nonseed\": %zu, \"maxposcomp_nonseed\": %zu, \"sterile_hist\": {",
           (unsigned long long)p, n, npos, ncomp, sz[sroot], pos[sroot], maxster, npcomp, npos_nonseed_max);
    bool first = true;
    for (auto& kv : sterile_hist) { printf("%s\"%zu\": %zu", first ? "" : ", ", kv.first, kv.second); first = false; }
    printf("}}\n");
    for (i128 qd : queries) {
        // component(s) containing a vertex with denominator qd
        std::map<size_t, size_t> hits;
        for (auto& pr : den) if (pr.first == qd) hits[find(pr.second)]++;
        printf("Q %s fibre=%zu", s128(qd).c_str(), (size_t)0 + [&]{ size_t c = 0; for (auto& kv : hits) c += kv.second; return c; }());
        for (auto& kv : hits) printf(" comp(size=%zu,pos=%zu,seed=%d)", sz[kv.first], pos[kv.first], kv.first == sroot ? 1 : 0);
        printf("\n");
    }
    for (i128 qd : paths) {
        // multi-source BFS from every vertex containing qd to the nearest positive vertex
        std::vector<long> prev(n, -2);
        std::vector<size_t> bfs;
        for (auto& pr : den) if (pr.first == qd) { prev[pr.second] = -1; bfs.push_back(pr.second); }
        std::vector<size_t> start_of(den.size());
        // index: denominator -> range in den
        long hit = -1;
        for (size_t h = 0; h < bfs.size() && hit < 0; ++h) {
            size_t u = bfs[h];
            if (V[u].a > 0) { hit = (long)u; break; }
            i128 ds[3] = {V[u].a, V[u].b, V[u].c};
            for (i128 dd : ds) {
                auto lo = std::lower_bound(den.begin(), den.end(), std::make_pair(dd, (size_t)0));
                for (auto it = lo; it != den.end() && it->first == dd; ++it)
                    if (prev[it->second] == -2) { prev[it->second] = (long)u; bfs.push_back(it->second); }
            }
        }
        printf("P %s", s128(qd).c_str());
        if (hit < 0) printf(" none\n");
        else {
            std::vector<size_t> path;
            for (long u = hit; u >= 0; u = prev[u]) path.push_back((size_t)u);
            printf(" len=%zu\n", path.size() - 1);
            for (auto it = path.rbegin(); it != path.rend(); ++it)
                printf("  %s %s %s\n", s128(V[*it].a).c_str(), s128(V[*it].b).c_str(), s128(V[*it].c).c_str());
        }
    }
    if (dump >= 0) {
        std::map<size_t, std::vector<size_t>> members;
        for (size_t i = 0; i < n; ++i) { size_t r = find(i); if (r != sroot && pos[r] == 0 && (long)sz[r] >= dump) members[r].push_back(i); }
        for (auto& kv : members) {
            printf("C %zu %zu\n", kv.first, kv.second.size());
            for (size_t i : kv.second) printf("V %s %s %s\n", s128(V[i].a).c_str(), s128(V[i].b).c_str(), s128(V[i].c).c_str());
        }
    }
    return 0;
}
