# z52d avenue — batch Q12 (113 items) summary
ES is OPEN. Rows: `out_Q12.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. Non-proof-attempt batch:
63 rows are calibration/engineering (fingerprints of U(p), solution-geometry statistics, OEIS/analogy items, tooling), handled briefly.
**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 0 | 0 | 0 | 67 | 67 |
| known-false | 27 | 0 | 0 | 0 | 27 |
| circular | 12 | 0 | 0 | 0 | 12 |
| unclear | 4 | 3 | 0 | 0 | 7 |
Novelty: 0 → 59, 1 → 54, 2 → 0. All plaus-3 rows are calibration lemmas or main-term statements (yield none).
**Plausibility ≥ 2 AND novelty ≥ 1 with any yield beyond calibration**: only **Z3164** (*almost all primes have a (★) certificate with prime
level C*). That is an exceptional-set statement on existing CRT/sieve lines (B6) with no pointwise content. The other 35 such rows are calibration.
Highest non-calibration plausibility: Z2033 (non-S₃ involution with odd fixed-point count; M5/T1), Z3104 (MSS interlacing over windows),
Z2973 (Smith-type profile distribution, B6), all plaus 1.
**Recurring missing theorems**
1. *Local/main-term hardness = RESIDUE_HARDNESS F + BM L-value* (B3, main term only): Z0688, Z0806, Z0808, Z0812, Z0820, Z0888, Z0958, Z1747, Z1948, Z3124.
2. *Fixed finite menus / bounded certificate size* (B1/B2 Thm 2.2(iii)): Z0842, Z1036, Z1229, Z1418, Z1474, Z2001, Z2934, Z3024, Z3108, Z3176; Z0934 (k(p) ≤ C log p, see below).
3. *Bounded procedures / identity families / DSL formulas* (B1, Mordell–Schinzel, Thm C under H): Z0955, Z1096, Z1180, Z1296, Z1380, Z1587, Z2438, Z2349.
4. *Reciprocity/forcing gives parity, not class* (CLASS_FORCING): Z0672, Z1009, Z1029, Z1628, Z2623, Z3132.
5. *Privacy of large primes bars cross-shift/cross-level pooling*: Z1219, Z1947, Z3009, Z3016, Z3146, Z2980 (two-line union).
6. *One-coordinate / thinner-lottery windows* (circular, ES-strength): Z1371 (C_min), Z1945 (least e), Z3085 (one dyadic range), Z0859 (x | z family),
   Z3111 ((★)-failure list exact ⇔ H⁻_BM), Z1620 (log-density c(p) = R(p) ≥ 1), Z2902 (smoothed H⁻_BM), Z3155 (Sun-style refinements).
7. *Count congruences / exact identities / bounded-level modularity* (M5/T1): Z1937, Z3092, Z1537, Z1538, Z2033.
**New in this pass** (scripts `scripts/z52d_avenue_Q12_*.py`, timeout 60)
* **Z1521 (PROVED, three lines).** Type I with d ∈ {1, 2, 3} is impossible at every p ≡ 1 (24) (gcd(c, p) = 1). The reasons: divisors of p² + 4c² are
  ≡ 1 (4), of p² + 8c² are ≡ 1, 3 (8), of p² + 12c² are ≡ 1 (3), while f ≡ −p forces 3 (4), 7 (8), 2 (3). In general a finite d-set D is sterile on
  p ≡ 1 (mod 4∏D), which explains Pass 1's "0 of 267". Fixed imaginary quadratic fields are genus characters (B1/B5).
* **Z1937 (whole-class forms falsified).** On primes ≡ 1 (24), R(p) takes every residue its evenness allows mod m ≤ 12 (< 12 000; zeros 409,
  577, 5569, 9601 reproduce the census), and f(p) hits 0 mod every m ≤ 12 (< 2500). Sub-progressions and partial counts were not tested (row: unclear).
* **Z0707 (falsified).** minlcm(p)/p is non-practical for 68 of 194 primes < 1200 (37 → 10: 40 = 37 + 2 + 1). The min-lcm solution usually uses p itself.
* **Z0939 (explained, checked).** For p ≡ 5 (8) the lex-first solution ((p+3)/4, (px₀+2)/3, px₀y₀/2) is the max-z solution, since x₀ is even and
  px₀ ≡ 1 (3). Verified at all 109 such primes < 3000. So A257843 is confined to p ≡ 1 (8): a 2-adic parity fact.
* **Z0861** is answered by P00 Z0216 (chain failures ⟺ (p+1)/2 has no prime ≡ 3 (4); density ≍ (log x)^{−1/2}).
**Corrections / cautions.** Z1620: (★) is a finite search (C ≲ p/4), so the normalised log-density c(p) is 0 at every p; only the unnormalised
total is ⟺ R(p) ≥ 1. Z0934: Type I cannot give small k (p | 4k − 1). On the (★) sublattice k ≥ witness/4, so OMEGA13 Thm 5.1 makes k(p) ≤ C log p
very likely false i.o. (the h > 1 Type II lines are unchecked). Z2944: S₁(p) ≤ R(p), so S₁ = 0 at every (★)-failure. Z2349: Salez uses 7 filters, not an infinite family (Pass 1).
**Assessment.** Q12 contains no architecture escaping B1/B2/B3/B6, privacy or the reciprocity-parity barrier. The batch's value is calibration:
hardness is one local axis (F) plus lottery noise; certificates are privately supplied by large primes; fixed fields/menus/procedures are sterile on
the Mordell-hard classes for the reasons the barrier map states.
