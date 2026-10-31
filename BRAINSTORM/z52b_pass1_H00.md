# z52b pass 1 — batch H00 (complete: 25 items)

- Outcomes (25): nothing 16, covered 8 (Z0109, Z0120, Z0124, Z0145, Z0148, Z0181, Z0190, Z0211), interesting 1 (Z0199), needs-compute 0, skipped 0.
- Interesting, Z0199: p ≡ 1 (mod q) lowers #solutions U(p) beyond the character (q/p) (q = 7: −0.13 ± 0.006 in log U). The class of one is the hardest square class mod 5, 7, 11, 13 and 840, a graded count-level form of the class-of-one sterility (ident_numerators Lemma 3.1). See §Z0199.
- Proved side facts: Z0142, 4/n = Σ1/a_i² forces 4 | n; Z0196, no q-integer ES (set q = 0); Z0135, 1/x+1/y+1/z = 4/w is not partition regular; Z0069, the matrix version is trivial; Z0183, the series(a, parallel(3, 9)) identity.
- Corrections to repo memos: Z0067, the Bradford–Ionascu cone contains −ℕ, so it is trivial on the real axis (other_rings.md §4 overstates); Z0199 sharpens ident_numerators §4's "square coset equally hard".
- Records: data/z52b/pass1/outcome_H00.jsonl; scripts scripts/z52b_p1_H00_*; data data/z52b/pass1/H00/ (raw count files are read from the main checkout's untracked data/z52b/raw/).

## Z0199 — class-of-one hardness beyond quadratic characters (interesting)

**Setup.** `uv run --with numpy --with sympy python scripts/z52b_p1_H00_pm1smooth.py`. It uses 8966 primes p ≡ 1 (4),
100 < p ≤ 2·10⁵, with U(p) = #solutions of 4/p from data/z52b/raw/f4_all_30000.txt and the main checkout's
data/z52b/raw/pr_20001_200000.txt. The baseline model regresses log(U+1) on 1, log p, log log p and (q/p) for primes q < 80, as in
scripts/z52b_fingerprint_qweights.py. For p ≡ 1 (4) and odd q, q | p − 1 ⇒ (q/p) = 1, so 1[q | p−1] is the "class of one"
inside the square coset. 1[3 | p−1] and 1[8 | p−1] are collinear with (3/p) and (2/p), so they are not identifiable.

**Observed (EVIDENCE).**
* Adding the indicators 1[q | p−1] for q = 5, 7, 11, 13 and 1[16 | p−1] gives these coefficients, all far beyond their SEs:
  q = 5: −0.059 ± 0.006, 7: −0.131 ± 0.006, 11: −0.057 ± 0.008, 13: −0.052 ± 0.008, 16 | p−1: −0.095 ± 0.006.
  The R² gain over the 25-variable character model is 0.021.
  With all q = 5..47 (part 2) they are 19: −0.049 ± 0.010, 17: −0.013, 23: −0.033, and become insignificant above about 29.
* Mean residual of the character-only model, by square class (part 3):
  mod 5: r = 1: −0.029, r = 4: +0.029; mod 7: r = 1: −0.087, 2: +0.008, 4: +0.079;
  mod 11: r = 1 is the lowest (−0.046); mod 13: r = 1 is the lowest (−0.045);
  mod 840 (the 6 Mordell squares): r = 1: −0.366 (87 primes); 121: −0.315; 169: −0.263; 289: −0.209; 361: −0.272; 529: −0.217.
* By the number of q ∈ {3, 5, 7, 11, 13} dividing p − 1, the mean residual for 0..4 divisors is
  +0.014, +0.029, −0.037, −0.132, −0.279 (n = 2312, 4024, 2155, 424, 49).
* Adding these indicators does **not** remove the q mod 3 dichotomy of the character weights q·β_q
  (fingerprint item 152; e.g. q = 7: −0.11 → +0.04 but q = 37, 43 stay ≈ +0.28, +0.23).

**Why it might matter for ES.** The hardest primes are those with p ≡ 1 modulo many small q: profinitely close to 1.
Lemma 3.1 of ident_numerators shows that point is sterile for every ET-shaped family, and this computation shows the
sterility already acts *gradedly* at finite level on the counts. A hardness model (M_BM or any singular series) that
sees only quadratic characters misses this factor. ident_numerators §4 read 0.43 vs 0.49 (17 class-of-one primes, m = 4) as
"whole square coset equally hard"; with 87 primes in the mod-840 class of one the gap is real (Assessment).

**Next step.** Compute E[U(p) | p mod q] with the full residue class kept, not just the character, from the Type I/II
pair enumeration (local density of pairs (u, B) with −(u+B) ≡ p (mod gcd(q, 4uB))). Check that it predicts the −0.13 at
q = 7 and the class ordering mod 840. Then fold the full-residue factor into the BM main term and re-test
H⁻_BM-type lower-tail statistics.

## Notes (not "interesting"; recorded for reproducibility)

**Z0067: Gaussian ES cones.** `scripts/z52b_p1_H00_gauss.py NORMMAX A` runs an exhaustive search, complete for A ≥ 1.
The smallest denominator satisfies |a| ≤ 3|n|/4, and the two-term remainder is solved through all Gaussian divisors of N².
* Bradford–Ionascu cone K = Q1 ∪ Q3 (closed): every first-quadrant n ∉ {0, 1, i, 1+i} with N(n) ≤ 2000 has a
  solution (1614 values; CERTIFIED by the search). For real n it is trivial, since −ℕ ⊂ K. So
  BRAINSTORM/other_rings.md §4, which says the Gaussian cone is "discrete, a lottery again", overstates the case for rational inputs.
* Closed Q1 cone only: for real n, Im(1/a) ≤ 0 for every a ∈ Q1, so all denominators are real and the problem is exactly ES
  (PROVED). Exceptions with N(n) ≤ 4000 (3205 values) number 12, i.e. 6 up to the symmetry n ↦ i·n̄:
  2+5i (29), 3+4i = (2+i)² (25), 4+5i (41), 5+6i (61), 10+13i (269), 2+17i (293). There are none in 293 < N ≤ 4000.
  Reproduce: `uv run --with sympy python scripts/z52b_p1_H00_gauss.py 4000 2 q1` (≈ 2 min) → `data/z52b/pass1/H00/gauss_Q1_4000_2.json`.
