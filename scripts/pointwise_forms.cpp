// Experimental pointwise ES certificates from reduced forms of discriminant -4p.
// This is a bounded search, NOT a proof that the construction always succeeds.
// Build: c++ -std=c++17 -O3 -Wall -Wextra -Wconversion pointwise_forms.cpp -o /tmp/es-forms
// Run:   /tmp/es-forms 10000000 --certificates > /tmp/es-form-certificates.txt
// Memory: about 5.34 * limit bytes, plus small vectors; limit is capped at 10^7.
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

namespace {
constexpr uint32_t max_limit = 10000000;
std::vector<uint32_t> spf;

std::vector<uint64_t> square_divisors(uint32_t n) {
    std::vector<uint64_t> divisors{1};
    while (n > 1) {
        const uint32_t prime = spf[n];
        unsigned exponent = 0;
        do {
            n /= prime;
            ++exponent;
        } while (n > 1 && n % prime == 0);
        const auto old_size = divisors.size();
        uint64_t power = 1;
        for (unsigned j = 1; j <= 2 * exponent; ++j) {
            power *= prime;
            for (size_t i = 0; i < old_size; ++i)
                divisors.push_back(divisors[i] * power);
        }
    }
    return divisors;
}

struct Hit {
    uint64_t divisor = 0;
    unsigned type = 0;
};

Hit window_hit(uint32_t p, uint32_t x) {
    const uint32_t q = 4 * x - p;
    if (x % p == 0) return {};
    const uint64_t target_ii = (q - x % q) % q;
    const uint64_t target_i = (q - (uint64_t(p) * x) % q) % q;
    for (const auto d : square_divisors(x)) {
        if (d % q == target_ii) return {d, 2};
        if (d % q == target_i) return {d, 1};
    }
    return {};
}
} // namespace

int main(int argc, char** argv) {
    uint32_t limit = 100000;
    bool certificates = false;
    if (argc > 3 || (argc == 3 && std::string(argv[2]) != "--certificates")) {
        std::cerr << "usage: es-forms [limit [--certificates]]\n";
        return 2;
    }
    if (argc >= 2) {
        char* end = nullptr;
        const unsigned long parsed = std::strtoul(argv[1], &end, 10);
        if (end == argv[1] || *end != '\0' || parsed < 73 || parsed > max_limit) {
            std::cerr << "limit must be an integer in [73, 10000000]\n";
            return 2;
        }
        limit = static_cast<uint32_t>(parsed);
    }
    certificates = argc == 3;

    spf.resize(size_t(limit) + 1);
    for (uint32_t i = 2; i <= limit; ++i) {
        if (spf[i]) continue;
        spf[i] = i;
        if (uint64_t(i) * i <= limit)
            for (uint32_t j = i * i; j <= limit; j += i)
                if (!spf[j]) spf[j] = i;
    }

    auto cap = static_cast<uint32_t>(std::sqrt(4.0 * limit / 3));
    while (3ULL * (cap + 1) * (cap + 1) <= 4ULL * limit) ++cap;
    while (3ULL * cap * cap > 4ULL * limit) --cap;
    // B = 2b. Retain the largest root 0 <= b <= A/2 for each residue p mod A.
    // For a given A, a reduced form exists iff the largest such root has C >= A.
    // Primitivity is automatic: -4p is fundamental and A < p.
    std::vector<std::vector<int16_t>> roots(cap + 1);
    for (uint32_t a = 1; a <= cap; ++a) {
        roots[a].assign(a, -1);
        for (uint32_t b = 0; 2 * b <= a; ++b)
            roots[a][(a - uint64_t(b) * b % a) % a] = static_cast<int16_t>(b);
    }

    if (certificates) std::cout << "# limit " << limit << '\n';
    uint32_t count = 0, record = 0;
    for (uint32_t p = 73; p <= limit; p += 24) {
        if (spf[p] != p) continue;
        bool found = false;
        for (uint32_t a = 1; 3ULL * a * a <= 4ULL * p; ++a) {
            const int32_t b = roots[a][p % a];
            if (b < 0) continue;
            const uint64_t numerator = uint64_t(p) + uint64_t(b) * uint64_t(b);
            if (numerator < uint64_t(a) * a) continue;
            const uint64_t c = numerator / a;
            const uint32_t x = a * (p / (4 * a) + 1);
            const Hit hit = window_hit(p, x);
            if (!hit.type) continue;
            if (std::gcd(uint64_t(a), std::gcd(uint64_t(2 * b), c)) != 1) {
                std::cerr << "internal error: nonprimitive form\n";
                return 2;
            }
            if (certificates) {
                std::cout << p << ' ' << a << ' ' << 2 * b << ' ' << c << ' '
                          << x << ' ' << hit.divisor << ' ' << hit.type << '\n';
            } else if (a > record) {
                std::cout << "record p=" << p << " A=" << a << " B=" << 2 * b
                          << " x=" << x << " q=" << 4 * x - p
                          << " d=" << hit.divisor << " type=" << hit.type << '\n';
            }
            if (a > record) record = a;
            found = true;
            break;
        }
        ++count;
        if (!found) {
            std::cerr << "CONSTRUCTION FAILURE p=" << p << " (not an ES counterexample)\n";
            return 1;
        }
    }
    if (certificates) std::cout << "# checked " << count << '\n';
    else std::cout << "PASS limit=" << limit << " primes=" << count << " max-first-A=" << record << '\n';
}
