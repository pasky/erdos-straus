# z52b Pass 1 — batch U05 (§2 untried, 207 items) — redo after pass1_U_fix

1. Batch U05 complete (all 207 items redone under pass1_U_fix); outcomes in `data/z52b/pass1/outcome_U05.jsonl`. ES remains OPEN.
2. Counts: nothing 133, covered 37, interesting 4, needs-compute 1, skipped 32 (meta/tooling or restatement only; listed in the outcome file).
3. Interesting: **Z1521** (Type I with d∈{1,2,3} is blind to p≡1 mod 24), **Z0939** (A257843 membership confined to p≡1 mod 8), **Z3018** (22 mod-840 classes uncertified at C≤50 include all six Mordell classes), **Z2652** (non-square triangle pairing exists for all tested p; not shown to imply ES).
4. Needs-compute: **Z1391** only (Salez seven-equation census; requires the full text of arXiv 1406.6307, est. 1–2 h).
5. Scope caveat: the 32 `skipped` items are meta/tooling (proof-search engineering, outreach, scheduling) or restatements (Z2651, Z2691, Z1258); I read rule 3 as covering these. Everything else has a computed or lookup result.

## Reproduction
* `gcc -O2 -o /tmp/ucount scripts/z52b_p1_U05_ucount.c` (U(n) = unordered count, = A192787; validated against f4 col 1 for n≤3000); `UDUMP=1` prints solutions.
* `scripts/z52b_p1_U05_cform.c` (C-form census) and `scripts/z52b_p1_U05_cmin.c` (early-exit C_min); data in `data/z52b/pass1/U05/2nd/`.
* Solution dumps for `z52b_p1_U05_sol.py`, `_fits.py`, `_final.py`, `_last.py`, `_sandpile.py`: `seq 3 3000 | UDUMP=1 /tmp/ucount | grep ^S > /tmp/u05/dump_n3000.txt` and `awk '$1>=5 && $1<=20000' primes | UDUMP=1 /tmp/ucount | grep ^S > /tmp/u05/dump_p2e4.txt` (too large to commit: 62 MB, 7.6 MB).

## Interesting items

### Z1521 — Type I with d∈{1,2,3} is blind to p≡1 (mod 24) (interesting)
Repo definition (FRONTIER §1): Type I(c,d) ⟺ some f | p²+4c²d with f ≡ −p (mod 4cd).
* For p≡1(4), p≤2·10⁴ (1125 primes): no Type I solution with d∈{1,2,3} and c≤30 for **any of the 267 primes ≡1 (mod 24)**; c up to 120 rescues none (`typeI2_out.txt`). For the other three classes mod 24 (5, 13, 17), **858/858 primes** have such a solution with c≤30 (`typeI3_out.txt`, class counts 281/281, 288/288, 289/289).
* For p≡1 (24) the solutions come from d∈{5,7,10,11} (d≤12); 29 of these 267 primes have no Type I solution with d≤12, c≤30 (5569 among them).
* Partial proof for d=3 (checked numerically, 16,648 tests, 0 violations): if p≡1 (mod 3), p∤c, then 3 | 4cd forces f≡−p≡2 (mod 3); every prime q | p²+12c² with q∤6c satisfies (−3/q)=1, so q≡1 (mod 3); f is odd, so f cannot be ≡2 (mod 3). Hence d=3 is impossible for these p.
* Why it matters: the d∈{1,2,3} family (imaginary quadratic fields Q(i), Q(√−2), Q(√−3)) with c unbounded covers 76% of primes and excludes exactly the class p≡1 (24), the repo's hard class. Next: prove the d=1 and d=2 analogues (same mod-8/mod-3 bookkeeping with f≡g≡−p mod 4cd, fg=p²+4c²d), and test d=5,7,10,11 on the same primes.
* Reproduce: `python3 scripts/z52b_p1_U05_typeI3.py`, `scripts/z52b_p1_U05_typeI2.py`.

### Z0939 — A257843 membership confined to p≡1 (mod 8) (interesting)
A257843 = n where the lexicographically first solution ≠ the max-z solution.
* Reproduced OEIS terms 89, 113, 161, 233, 281, … (all n≤3000).
* For primes p≡1(4), p≤2·10⁴: membership 23% overall; **0% for p≡5 (mod 8)** (classes 5 and 13 mod 24, ≈570 primes), 25% for class 1 mod 24, 67% for class 17 mod 24.
* Next: prove that for p≡5 (mod 8) the lex-first solution has the largest z (a 2-adic argument); check whether the rate on p≡1 (8) depends on p mod 16 or 32.
* Reproduce: `scripts/z52b_p1_U05_sol.py` (needs the dump above).

### Z3018 — mod-840 class certification at C≤50 (interesting)
A class mod 840 is "certified" if some C≤50 wins for every sampled prime in it (≥5 primes per class, p≡1(4), p≤1e5).
* 74 classes certified, covering 77.6% of the primes; the 22 uncertified classes are 1, 37, 109, 121, 157, 169, 241, 289, 337, 361, 409, 421, 457, 529, 541, 577, 589, 661, 709, 757, 781, 829.
* These include **all six Mordell hard classes** (1, 121, 169, 289, 361, 529) and the R-zero classes 409 and 577. The 102 class-wide wins at C≤50 are all explained by a divisor of 4Cr+1 supported on {3,5,7} that is ≡ −1 (mod 4C) (Z1497), so the certified classes are congruence covers by small primes.
* Caveat: class sizes are sample sizes (≥5 primes), so "uncertified" is empirical. Next: check the 16 non-Mordell uncertified classes at C≤200, and whether the uncertified set equals the set of classes with no {3,5,7}-supported certificate.
* Reproduce: `scripts/z52b_p1_U05_last.py` and `scripts/z52b_p1_U05_cf2.py`.

### Z2652 — non-square triangle pairing for every tested prime (interesting, low confidence)
Triangle multigraph with multiplicities x,y,z: τ = xy+yz+zx; the cofactor pairing class on Z/p is the Legendre class of x+y (classes of x+y, x+z, y+z agree since (x+y)(x+z) ≡ x² mod p).
* For all 1125 primes p≡1(4), p≤2·10⁴ there is a triangle with τ=p and non-square pairing (k*=3). The criterion agrees with the C≤5 C-form on 1082 primes and holds without a C≤5 certificate on 43 primes.
* Open: this is not shown to imply ES. Next step: try to turn a triangle (x,y,z) into a three-term decomposition of 4/p, and test whether the 43 extra primes coincide with C-form failures at C≤200.
* Reproduce: `scripts/z52b_p1_U05_tri.py`, `scripts/z52b_p1_U05_sandpile.py`.

## Other notable computed facts (nothing, for calibration)
* C-form census: the exact C≤200 exception set for p≡1(4), p≤1e5 is {409, 577, 5569, 9601, 23929, 60217, 83449, 98017}; to 1e6 with C≤20000 it is {409, 577, 5569, 9601, 23929, 83449, 102001, 184837, 329617, 712321}; 434437, 571741, 706801, 881269 win only at C=3879, 1489, 4016, 1695 (`cmin_p1e6_C1000.txt`, `final_out.txt`).
* U(n) reproduced (validated against column 1 of f4_all_30000 for n≤3000); the Z0688 least-QNR records reproduce the item's numbers exactly (0.397, 0.369, 0.543, 0.526, 0.362, 0.293).
* Z1497/Z3018: all 102 class-wide wins come from {3,5,7}-divisors (congruence covering).
* Forests F_p (Z2792, Z2681, Z2678, Z2840): edge products generate F_p^* for all 180 primes tested; the F₂ flat-colouring space is not trivial (dim ≥3); forests are bipartite so the Hoffman bound is vacuous; the configuration model predicts a giant ≈4%, observed largest component ≈6.5%.
* Sandpile/fan (Z2784, Z2677): T(−1,−1) = (−1)^{|E|} (bicycle dimension 0 for all 275 fan words); Hermitian ℤ/4 holonomy leaves det = p.
* Solution graph (Z1964/Z2991): single-denominator moves only, median 5 components per prime; no two solutions share two denominators, so no Vieta-type moves.
