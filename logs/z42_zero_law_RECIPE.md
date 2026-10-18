# z42 zero-law (O273 item 4) — how to regenerate (EVIDENCE run of 2026-10-18)

Build: `gcc -O2 -o zl scripts/z42_zero_law.c -lm`; every run under `ulimit -v 4000000`.
1. `./zl mark 8 1000000000 1 > z8_1e9.txt` (55 s; lines `Z n`, summary last line: 499 984 188 admissible, 2 748 892 zeros).
2. Zero proxies: `awk '/^Z/{print $2}' z8_1e9.txt | ./zl proxy 8 1000000000 > zall.prox` (≈ 20 CPU-min; split in 2).
3. Population: Python `random.seed(273)`; 40 000 draws `random.randrange(500000001, 1000000001, 2)`, skipping squares
   → `pop.txt`; `./zl proxy 8 1000000000 < pop.txt > pop.prox` (committed: `z42_zero_law_m8_pop_proxy.txt.gz`).
4. Exact M (`./zl exact 8 1000000000 < list`): all zeros in [5e8,1e9] with proxy ≥ 22, all zeros in [1e8,5e8) with
   proxy ≥ 24, all zeros < 1e8 with proxy ≥ 24 (`exact 8 100000000`), and the first 300 lines of pop.txt
   (committed: `z42_zero_law_m8_exact_zeros.txt.gz` (n M M0), `z42_zero_law_m8_exact_pop.txt.gz`).
5. Fit: `scripts/z42_zero_law_fit.py --zprox zall.prox --zexact <exact zeros> --pprox pop.prox --pexact <exact pop>
   --lo 5e8 --hi 1e9 --nadm 249995369` → `z42_zero_law_m8_1e9.txt`.
m = 12, 16: `./zl mark m 10000000 5000000`; 3 000 zeros by `shuf --random-source=<(yes 273) -n 3000`, 3 000 population
draws (`random.seed(m)`, odd non-squares, m = 12 also prime to 3) in [5e6, 1e7], all with exact M; fit with
`--nadm admissible·3000/zeros` → `z42_zero_law_m12_m16_1e7.txt`.
