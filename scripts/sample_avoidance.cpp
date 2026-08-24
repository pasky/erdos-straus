// Reproduce the §27.5 avoidance sample.
// Build: g++ -O3 -DNDEBUG -std=c++20 -pthread -o sample_avoidance scripts/sample_avoidance.cpp
// Full run: ./sample_avoidance --output sample.tsv
// Small direct-oracle check: ./sample_avoidance --self-test
#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <limits>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <thread>
#include <vector>

namespace {
constexpr std::uint64_t kSeedBase = 27006400ULL;
constexpr std::uint64_t kSeedStep = 0x9e3779b97f4a7c15ULL;
constexpr std::uint64_t kSampleLo = 100000000000000ULL;
constexpr std::uint64_t kSampleHiExclusive = 900000000000000000ULL;
constexpr int kMaxX = 6400;
constexpr std::array<int, 8> kCutoffs = {50, 100, 200, 400, 800, 1600, 3200, 6400};

struct Config {
    std::uint64_t samples_per_stream = 100000000ULL;
    std::uint64_t chunk_size = 10000000ULL;
    int streams = 24;
    std::string output;
    bool self_test = false;
};

struct ModulusTable {
    std::vector<int> moduli;
    std::vector<std::vector<std::uint8_t>> hit;
};

struct ChunkResult {
    int stream = 0;
    int chunk = 0;
    std::uint64_t seed = 0;
    std::uint64_t start = 0;
    std::uint64_t draws = 0;
    std::array<std::uint64_t, kCutoffs.size()> survivors{};
    std::uint64_t sample_sum = 0;
    std::uint64_t sample_xor = 0;
};

std::uint64_t stream_seed(int stream) {
    // Unsigned arithmetic specifies reduction modulo 2^64.
    return kSeedBase + kSeedStep * static_cast<std::uint64_t>(stream);
}

std::uint64_t mix64(std::uint64_t x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

ModulusTable make_tables(int max_x) {
    ModulusTable tables;
    for (int m = 3; m <= max_x; m += 4) {
        const std::uint64_t a = static_cast<std::uint64_t>(m + 1) / 4;
        const std::uint64_t square = a * a;
        std::vector<std::uint8_t> residues(static_cast<std::size_t>(m), 0);
        for (std::uint64_t d = 1; d * d <= square; ++d) {
            if (square % d != 0) continue;
            const auto mark = [&](std::uint64_t divisor) {
                const std::uint64_t four_d_mod = (4 * (divisor % static_cast<std::uint64_t>(m))) %
                                                 static_cast<std::uint64_t>(m);
                const std::uint64_t residue = (static_cast<std::uint64_t>(m) - four_d_mod) %
                                              static_cast<std::uint64_t>(m);
                residues[static_cast<std::size_t>(residue)] = 1;
            };
            mark(d);
            if (d != square / d) mark(square / d);
        }
        tables.moduli.push_back(m);
        tables.hit.push_back(std::move(residues));
    }
    return tables;
}

int first_hit_modulus(std::uint64_t n, const ModulusTable& tables) {
    for (std::size_t i = 0; i < tables.moduli.size(); ++i) {
        const int m = tables.moduli[i];
        if (tables.hit[i][static_cast<std::size_t>(n % static_cast<std::uint64_t>(m))]) return m;
    }
    return kMaxX + 1;
}

bool direct_hit(std::uint64_t n, int m) {
    const std::uint64_t a = static_cast<std::uint64_t>(m + 1) / 4;
    const std::uint64_t square = a * a;
    for (std::uint64_t d = 1; d <= square; ++d) {
        if (square % d == 0 && (n + 4 * d) % static_cast<std::uint64_t>(m) == 0) return true;
    }
    return false;
}

void run_self_test() {
    const auto tables = make_tables(100);
    for (std::uint64_t n = 100000; n < 101000; ++n) {
        for (std::size_t i = 0; i < tables.moduli.size(); ++i) {
            const int m = tables.moduli[i];
            const bool table_value = tables.hit[i][static_cast<std::size_t>(n % m)] != 0;
            if (table_value != direct_hit(n, m)) throw std::runtime_error("residue-table/direct-oracle mismatch");
        }
    }

    std::mt19937_64 rng(stream_seed(0));
    std::uniform_int_distribution<std::uint64_t> distribution(kSampleLo, kSampleHiExclusive - 1);
    std::array<std::uint64_t, 2> early{};
    std::array<std::uint64_t, 2> oracle{};
    constexpr std::array<int, 2> cutoffs = {50, 100};
    for (int j = 0; j < 10000; ++j) {
        const std::uint64_t n = distribution(rng);
        int first = 101;
        for (std::size_t i = 0; i < tables.moduli.size(); ++i) {
            if (tables.hit[i][static_cast<std::size_t>(n % tables.moduli[i])]) {
                first = tables.moduli[i];
                break;
            }
        }
        for (std::size_t c = 0; c < cutoffs.size(); ++c) {
            early[c] += first > cutoffs[c];
            bool survives = true;
            for (int m = 3; m <= cutoffs[c]; m += 4) {
                if (direct_hit(n, m)) {
                    survives = false;
                    break;
                }
            }
            oracle[c] += survives;
        }
    }
    if (early != oracle) throw std::runtime_error("early-exit/direct-oracle count mismatch");
    std::cout << "self-test passed: residue tables and 10,000-draw early-exit counts match direct oracle\n";
}

void sample_stream(int stream, const Config& config, const ModulusTable& tables,
                   std::vector<ChunkResult>& results) {
    const std::uint64_t seed = stream_seed(stream);
    std::mt19937_64 rng(seed);
    std::uniform_int_distribution<std::uint64_t> distribution(kSampleLo, kSampleHiExclusive - 1);
    const std::uint64_t chunk_count =
        (config.samples_per_stream + config.chunk_size - 1) / config.chunk_size;
    for (std::uint64_t chunk = 0; chunk < chunk_count; ++chunk) {
        ChunkResult result;
        result.stream = stream;
        result.chunk = static_cast<int>(chunk);
        result.seed = seed;
        result.start = chunk * config.chunk_size;
        result.draws = std::min(config.chunk_size, config.samples_per_stream - result.start);
        for (std::uint64_t j = 0; j < result.draws; ++j) {
            const std::uint64_t n = distribution(rng);
            const int first_hit = first_hit_modulus(n, tables);
            for (std::size_t c = 0; c < kCutoffs.size(); ++c) {
                result.survivors[c] += first_hit > kCutoffs[c];
            }
            result.sample_sum += n;
            result.sample_xor ^= mix64(n ^ (result.start + j));
        }
        results[static_cast<std::size_t>(stream) * chunk_count + chunk] = result;
    }
}

void write_results(std::ostream& out, const Config& config, const std::vector<ChunkResult>& results) {
    out << "# erdos-straus avoidance sampler v1\n"
        << "# rng=std::mt19937_64 distribution=std::uniform_int_distribution<uint64_t>\n"
        << "# interval=[" << kSampleLo << ',' << kSampleHiExclusive << ")\n"
        << "# seed[t]=(27006400+0x9e3779b97f4a7c15*t) mod 2^64\n"
        << "# streams=" << config.streams << " samples_per_stream=" << config.samples_per_stream
        << " chunk_size=" << config.chunk_size << " max_X=" << kMaxX << "\n"
        << "stream\tchunk\tseed\tstart\tdraws";
    for (int cutoff : kCutoffs) out << "\tsurvive_" << cutoff;
    out << "\tsample_sum_mod_2^64\tsample_mix_xor\n";
    for (const auto& row : results) {
        out << row.stream << '\t' << row.chunk << '\t' << row.seed << '\t'
            << row.start << '\t' << row.draws;
        for (auto count : row.survivors) out << '\t' << count;
        out << '\t' << row.sample_sum << '\t' << row.sample_xor << '\n';
    }
}

Config parse_args(int argc, char** argv) {
    Config config;
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        auto value = [&](const char* option) -> std::string {
            if (++i >= argc) throw std::runtime_error(std::string("missing value for ") + option);
            return argv[i];
        };
        if (arg == "--self-test") config.self_test = true;
        else if (arg == "--output") config.output = value("--output");
        else if (arg == "--samples-per-stream") config.samples_per_stream = std::stoull(value("--samples-per-stream"));
        else if (arg == "--chunk-size") config.chunk_size = std::stoull(value("--chunk-size"));
        else if (arg == "--streams") config.streams = std::stoi(value("--streams"));
        else throw std::runtime_error("unknown argument: " + arg);
    }
    if (config.streams <= 0 || config.chunk_size == 0 || config.samples_per_stream == 0)
        throw std::runtime_error("stream and sample counts must be positive");
    return config;
}
}  // namespace

int main(int argc, char** argv) {
    try {
        const Config config = parse_args(argc, argv);
        if (config.self_test) {
            run_self_test();
            return 0;
        }
        const auto tables = make_tables(kMaxX);
        const std::uint64_t chunks_per_stream =
            (config.samples_per_stream + config.chunk_size - 1) / config.chunk_size;
        std::vector<ChunkResult> results(static_cast<std::size_t>(config.streams) * chunks_per_stream);
        std::vector<std::thread> workers;
        workers.reserve(static_cast<std::size_t>(config.streams));
        for (int stream = 0; stream < config.streams; ++stream)
            workers.emplace_back(sample_stream, stream, std::cref(config), std::cref(tables), std::ref(results));
        for (auto& worker : workers) worker.join();

        if (config.output.empty()) {
            write_results(std::cout, config, results);
        } else {
            std::ofstream file(config.output);
            if (!file) throw std::runtime_error("cannot open output file: " + config.output);
            write_results(file, config, results);
        }
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "sample_avoidance: " << error.what() << '\n';
        return 1;
    }
}
