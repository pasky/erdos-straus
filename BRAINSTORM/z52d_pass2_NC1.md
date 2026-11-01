# z52d Pass 2 — batch NC1 (80 items, all Pass-1 `needs-compute`)

Counts: nothing 74 · covered 4 (Z1248, Z1256, Z1263, Z1840) · needs-compute 1 (Z1363) · interesting 1 (Z1686) · skipped 0 (80 lines in `data/z52b/pass2/outcome_NC1.jsonl`).
Interesting: **Z1686** (class number h(−4p) vs witness count R(p): residual partial correlation 0.105 after controlling for log p, p mod 840 and Legendre symbols (p/q), q = 11…47).
Most items: honest `nothing` (step done, empty) or explicit not-done (ill-specified or literature not accessible). Premise findings: Z1435/Z1951 (Mordell copy: no 4/n text in the retrievable chapters), Z1833 (premise true), Z1358 (my recalled Rademacher form is wrong for most triples; normalisation unresolved).
Substantive side results: greedy/Sylvester a=3 slice (Z1263), exact gcd lemma (Z1210/Z1251), Z1351 witness-transport lemma (AP of density 1/d), Z1377 kernel test (g not 2- or 3-regular in window), Z1394 run statistics to 10⁹.

## Z1686 — class number vs witness count (interesting)

* **What.** R(p) = Σ_{C ≤ 50} #{d | 4Cp+1 : d ≤ √(4Cp+1), d ≡ −1 (mod 4C)}, normalised by log²p; h(−4p) by reduced-form count, normalised by √p. Primes p ≡ 1 (mod 4), p < 10⁵ (n = 4783).
* **Numbers.** Raw Pearson 0.4639. Given log p and p mod 840 (class dummies): 0.2161. Additionally given Legendre symbols (p/q), q ∈ {11,13,…,47}: **0.1047**. Within-class shuffle null (keeps p mod 840, destroys pairing): mean −0.0001, sd 0.0155.
* **Reading.** The raw correlation is mostly residue-driven (both quantities depend on whether small primes split in Q(√−p) and divide 4Cp+1). A residual ~0.10 survives the small-prime Legendre controls. Mundane explanations not yet excluded: residue dependence mod 9, 16, 25, 49 (not in the controls), and Legendre symbols q ≥ 53.
* **Reproduce.** `uv run --with numpy --with sympy python scripts/z52d_p2_NC1_classnum_partial.py` → `data/z52b/pass2/NC1/classnum_partial.json`.
* **Next.** Control for p mod lcm(4C : C ≤ 50) and for (p/q), q < 200. If ≥ 0.05 remains, test whether the residual concentrates in the Mordell square classes mod 840 (where the campaign locates all difficulty).

## Covered / substantive side results

* **Z1263 (covered):** the e = 3 slice criterion (succeeds iff (p+3)/4 has a prime factor ≡ 2 mod 3; fails with density ≍ 1/√log N) is in `BRAINSTORM/y4_catalogue.md:14–15,44`; the greedy continuation is in `greedy_algorithm_dynamics.md:30–31`. Our 2-term completion check: 0.42 / 0.51 / 0.52 / 0.59 success on sampled primes per decade up to 10⁷.
* **Z1351 (nothing, exact lemma):** a witness (C,d) of p witnesses p + 24k iff d | 96Ck, i.e. k ≡ 0 mod d (3 ∤ d). 228 228 instances, 0 violations.
* **Z1377 (nothing):** k-kernel rank of g(n) (least C with a witness, all n ≤ 2²¹, columns n ≤ 700): full rank at every depth for k = 2 (127/127 at depth 6) and growing for k = 3. Controls: binary digit sum saturates for k = 2 (rank 2), base-3 digit sum for k = 3 (rank 2).
* **Z1394 (nothing):** longest run of consecutive primes ≡ 1 mod 24 with no C ≤ 2 witness: 7, first reached at p = 476 870 257 (up to 10⁹). A class-matched independent model (per p mod 840) predicts the observed tail.

## Not done (explicit)

Z1363 (Dirichlet series needs f(n) to 3·10⁴, ~100 CPU-min, over the cap); Z1391 (Salez seven equations fetched at PDF lines 322–336, census not implemented); Z1565/Z1662 (Guy UPINT D11 not accessible); Z1564/Z1952 (Obláth, Dickson not accessible); Z1435/Z1951 (chapter 30 not in the retrievable copy); Z1409, Z1401, Z1720, Z1776, Z1777, Z1786, Z1797, Z1814, Z1848, Z1889, Z1890, Z1894, Z1908, Z1922, Z1936 (not run; reasons in the outcome file).

## Reproduction

* C witness scan: `gcc -O2 -o z52d_cmin scripts/z52d_p2_NC1_cmin.c`; `./z52d_cmin 1000000000 10 24 runs` (run statistics), `./z52d_cmin 1000000000 2 24 list > /tmp/list_c2_1e9.txt` (per-prime status), `./z52d_cmin 10000000 50 4 list` (Z1516 data).
* Model/controls: `scripts/z52d_p2_NC1_runs_model.py`, `scripts/z52d_p2_NC1_kernel.py`, `scripts/z52d_p2_NC1_misc{,2,3}.py`, `scripts/z52d_p2_NC1_small.py`.
