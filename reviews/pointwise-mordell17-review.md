# Hostile review R83 — POINTWISE_MORDELL17.md (+ §2.1 table of POINTWISE_MORDELL.md)

Reviewer: side agent R83 (branch `side-agent/review-mordell17`), merged `side-agent/sterility-r17`
at d4ea35a. From-scratch scripts: `scripts/review_m17_*.py`.

Status: IN PROGRESS.

## Summary verdicts

(filled in below, claim by claim)

### Claim A — §2.1 T-generic table (POINTWISE_MORDELL) at T={17} and Lemma 1.1: **SOUND** (one simplification found)

Re-derived from scratch, starting from the *statement* of ET Prop 1.9 (arXiv:1107.1010 p. 8,
read from sources/elsholtz-tao-1107.1010.pdf), not from ET's coordinate formulas. A class `r mod M`,
`M = 17^k N`, `17∤N`, contains `x(u)` iff `r ≡ 1 (N)` and `u ≡ r (17^k)`. Family by family:

* I1 `−f mod 4ad`, `f|4a²d+1`: `4(ad)'|f+1`; box `−f mod (ad)_17`. (17|f forces 17∤ad, level 0.)
* I2 `{−f mod 4ac}∩{−c/a mod f}`, `(4ac,f)=1`: `4(ac)'|f+1`, `f'|a+c`; box `−f mod (ac)_17` or `−c/a mod f_17`.
* I3 `{−f mod 4cd}∩{n²≡−4c²d mod f}`, `(4cd,f)=1`: `4(cd)'|f+1`, `f'|4c²d+1`; box `−f` resp. the roots.
* I4 `−1/e mod 4ab`, `e|a+b`, `(e,4ab)=1`: `4(ab)'|e+1`; box `−1/e`.
* II1 `−e mod 4ab`: same conditions, box `−e`.
* II2 `−4a²d mod f`, `4ad|f+1`: `f'|4a²d+1`; box `−4a²d mod f_17`.
* II3 `−4a²d−e mod 4ade`, `(4ad,e)=1`: `T`-free part of the modulus is `4(ad)'e'`; since `(ad)'|a²d`,
  conditions `4(ad)'|e+1`, `e'|4a²d+1`; box `−4a²d−e` mod `(ade)_17`.

This is exactly the table. Splitting by where the 17 sits (I2, I3, II3 forbid both by their gcd
condition) gives exactly Lemma 1.1's types; I re-verified the I2(17|f) ↔ Q⁻¹ and the P-inversion
algebra by hand (correct). Level-0 (Lemma 1.2): all three rigid forms at `F=1` give a solution of
`4/1 = 1/x+1/y+1/z` in positive integers, impossible — correct.

Numerical confirmation (from scratch): `scripts/review_m17_brute.py` reads the classes *literally off
the Prop 1.9 statement* (CRT, all roots for I3, primitivity checked), all moduli `M ≤ 10⁶`, and
intersects with the 17-generic line, levels ≤3. Result: 295 (family, box) pairs (168 distinct boxes,
all cells); **no level-0 class**; **every one of them lies in the complete enumeration** of
`scripts/review_m17_enum.c` + `review_m17_union.py` (built from my own derivation of the types),
under the family→type map of Lemma 1.1 (I1→P; I2→U/Q⁻¹; I3→P/√Q; I4→U⁻¹; II1→U; II2→Q; II3→P/Q).
At M≤10⁵ the brute force sees 106 distinct boxes, matching the author's number.

**New observation (PROVED, reviewer): the (√Q) type is empty, and (Q) lives only at odd levels in
non-residue cells.** For a (Q)-datum, `f = 4adm−1 = 17^k g`. Since `f ≡ −1 (mod 4d)`, Jacobi
reciprocity gives `(d/f) = 1` (odd part: `(d_o/f) = (f/d_o)(−1)^{(d_o−1)/2} = 1`; 2-part: `f ≡ 7 (8)`
when `d` is even), and `(−1/f) = −1`; so `(−d/f) = −1`. As `g | 4a²d+1`, `−d·(2a)² ≡ 1 (mod g)`, so
`(−d/g) = 1`. Hence `(−d/17)^k = −1`: **k is odd and `−4a²d` is a non-residue mod 17**, so
`n² ≡ −4a²d (mod 17^k)` has no root. Consequently the I3(17|f) classes never meet the 17-generic
line, the union `P∪Q∪Q⁻¹∪U∪U⁻¹` is the whole story, and **the inversion symmetry `C_5 ↔ C_7` is
exact (no √Q caveat needed)**. Confirmed numerically: 0 √Q boxes at levels ≤5 (see Claim C).
The same reciprocity argument applied to a (P)-datum (`f=4ni−1 | 4·17^K a'²d'+1`, `f ≡ −1 mod 4d'`)
gives `(17^K/f) = −1`, i.e. **K odd** — a direct proof of "even K empty" (see defect m2).

### Claim B — Lemmas 2.1–2.3, Cor 2.4, level bookkeeping: **SOUND**; §2 measure "Consequence": **SOUND-AFTER-REPAIRS** (citations)

Re-derived independently (my parametrisations differ from the author's code, see Claim C):
* (Q): with `m=(f+1)/(4ad)`, `4adm ≡ 1` and `4a²d ≡ −1 (mod g)` give `g | a+m`; with `j=(a+m)/g`,
  `j(4adm−1) = F(a+m)`, i.e. `4·a·m·j·d = F(a+m)+j` = ET (2.3) for `(a,m,j,d)`, `n=F`. The equation is
  symmetric in `(a,m)`, the swapped datum `(m,d,f)` is again a (Q)-datum (checked: `g | 4m²d+1`), so
  one N-point with `a≤b` gives exactly the two boxes `−4a²d`, `−4b²d`. The I2(17|f) data satisfy the
  *same* equation with `(a,c,t,h)`; box `−c/a ≡ −1/(4a²t)`. ✔
* (U): `4iabc = F(a+b+c)` with `i = F(e+1)/(4ab)`; note `(ab)_17 = F` must be imposed separately (it is
  not implied by the equation); the author's code does impose it (`nn % 17`), as does mine. The box
  `−e = −(x/y+x/z)` is a function of the ES solution, so `#boxes ≤ #ordered solutions` ✔.
* (P): `(4ni−1)(4nj−1) = 4·17^K a'²d'+1` with `K = 2α+δ = k+α`, `α ≤ k`; so `K ∈ [k,2k]`, i.e. a
  given N-point of `Σ^II_{17^K}` produces boxes at levels `K−α`, `0≤α≤⌊K/2⌋`, all centred at the
  same integer `−f`; the largest is at level `⌈K/2⌉` ✔. Weight `17^{1−⌈K/2⌉}` relative to a cell, and
  `B_k` collects `K ∈ {2k−1, 2k}` ✔. Converse direction (every N-point with `17∤cd`, every `α`)
  verified numerically: `review_m17_union.py` rebuilds `(a,d) = (17^α a', 17^{K−2α} d')` for every
  enumerated N-point and asserts the raw (P) conditions (374 box-checks for K≤6, more at K=7).
* Cor 2.4: correct (any level-0 datum is an N-point of `Σ_1`, i.e. a solution of `4/1`); the
  sentence "For (P), `K≥1` as `k≥1`... and `k=0` forces `K=0`" is garbled but the content is right.

§2 "Consequence" (convergence): the conclusion is right but the citations are not (defects m1, m2).

### Claim D — Theorem 4.1 (measure criterion) and Corollary 4.2: **SOUND** (as implications; label nits)

* Thm 4.1: boxes are clopen subsets of `ℤ_17`; a level-`k` box has relative measure `17^{1−k}` in a
  cell; σ-subadditivity gives the claim. `B_k` over-counts (all cells, √Q included — √Q is in fact
  empty, Claim A, so `8D_Q` may be replaced by `4D_Q`), which is harmless. The P bookkeeping (level
  `⌈K/2⌉`, `K ∈ {2k−1,2k}`, `D_P(2k)=0`) is right. No compactness is needed. The threshold must be a
  *lower* bound for the uncovered fraction; see m4 for the rounding.
* Cor 4.2: a finite polynomial covering gives (ET Prop 1.9, "only if" direction, proof in ET §10 —
  I read the case analysis; it is exhaustive: Type I {a,d}, {a,c}×deg f∈{0,1}, {c,d}×deg f∈{0,1};
  Type II {a,c,e}, {a,c,d}, {a,d,e}, {c,d,e}) finitely many family classes containing all large
  target primes. Their union is clopen and misses `x(u)`, hence a basic neighbourhood
  `{x ≡ u (17^L), x ≡ 1 (Q)}`; choosing `840·11·13 | Q` (author: "x_q = 1") this class is primitive,
  contains infinitely many primes (Dirichlet), each with `p ≡ 1 (24)`, square mod 5,7,11,13, non-square
  mod 17, i.e. Mordell-hard with `n_p = 17`. Contradiction. ✔ The distinction 17-generic vs `n_p=17`
  is handled correctly: the 17-generic line is a measure-zero subset of the closure of the target
  primes, and a single sterile point on it suffices to rule out a finite covering (the converse is not
  claimed and would be false-directional).
* §4 numerics re-checked (`scripts/review_m17_tail.py`): "≈0.84" is 0.8447 ✔; the sufficient
  hypothetical bounds (`D_Q+D_U ≤ 17^{k/2}`, `k≥8`; `D_P(K) ≤ 17^{K/4}`, `K≥11`) give tail 0.0070 < 0.01 ✔.
