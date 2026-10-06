# Hostile review R83 — POINTWISE_MORDELL17.md (+ §2.1 table of POINTWISE_MORDELL.md)

Reviewer: side agent R83 (branch `side-agent/review-mordell17`), merged `side-agent/sterility-r17`
at d4ea35a. From-scratch scripts: `scripts/review_m17_*.py`.

Status: round 1 complete. No FATAL or MAJOR defects; 9 MINOR.

## Summary verdicts

(see the table at the end)

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

### Claim C — Computation 3.1: **SOUND** (independently reproduced through level 5, and the Q/U part of level 7)

Independent engine: `scripts/review_m17_enum.c` (my own parametrisations, different loops from the
author's `m17_enum.c`):
* S-mode: all `(a,m,d,j)` with `j(4adm−1) = F(a+m)`, `a≤m`, looped over `(a,d,j)` with the bound
  `j(4a²d−1) ≤ 2Fa` (from `j≥1`, `m≥a`); raw (Q) conditions re-checked on every hit; one hit gives
  the II2, I2(17|f) and I3(17|f) boxes of both orientations.
* U-mode: sorted `u≤v≤w` of `4iuvw = F(u+v+w)`, `4iuv ≤ 3F`; every choice of `c`; raw (U) conditions.
* P-mode: `4a'd'ij = i+j+17^K a'`, `i≤j`, looped over `(i,d')` with `4d'i² ≤ N+2i` and then `a'` with
  `(4a'd'i−1) | 4d'i²+N` (equivalent, as `gcd(4d'i, 4a'd'i−1)=1`); every hit is turned back into a raw
  (P)-datum `(17^α a', 17^{K−2α} d', f)` for every `α ≤ K/2` and the raw conditions are asserted.
* Union: exact, by marking residues mod `17^L` in the cell (`scripts/review_m17_union.py`).

Results (identical in `C_5` and `C_7`):

| level | covered (reviewer) | author |
|---|---|---|
| 2 | 0.235294 | 0.235294 |
| 3 | 0.314879 | 0.314879 |
| 4 | 0.321799 | 0.321799 |
| 5 | 0.322793 (exact: uncovered 56561/83521 = 0.677206930…) | 0.322793 |
| 7 (Q,U only; P for K≤9) | 0.322797 (uncovered 16346035/24137569) | 0.322797 |

Data counts agree exactly with the author's: `D_Q(k)` = 2, 0, 73, 0, 245, 0, 707 (k=1..7); `D_U(k)` = 4, 0,
68, 0, 310, 0, 826; `D_P(K)` = 2, 0, 32, 0, 121, 0, 258, 0 (K=1..8; K=8 computed, 0 as predicted by the
reciprocity argument); `D_P(9)` = 604. √Q boxes: 0 at every level. **u = 5, 7 lie in no box of level ≤5
and in no Q/U box of level ≤7** ✔. P is closed under inversion level by level, and the union is exactly
inversion-symmetric ✔. Level-2 boxes in C_5: {56, 107, 226, 243} mod 289 ✔.
Box sets of the two engines coincide: P K=7 (392 boxes mod 17⁴) and P K=9 (782 boxes mod 17⁵) equal.
(My P-mode is the slow one: K=9 took 1 h 55 min; the author's 6 min. My first K=9 output overflowed
u64 when printing f* — caught by the raw-condition asserts and fixed; f* is now rebuilt exactly.)
Completeness cross-check against the raw Prop 1.9 brute force (M ≤ 10⁶): 0 missing (Claim A).

### Claim E — §4 "Status of the hypothesis", Assessment, novelty: **SOUND as Assessment** (wording nits)

The reduction is exactly as stated: Theorem 4.1's hypothesis is open, and the author does not claim it.
The 1/10 margin for (P) is real: a level-`⌈K/2⌉` box against `f_II ≪ N^{2/5+o(1)}`. I agree that
explicit divisor bounds cannot close it at any computable level. Using Nicolas–Robin,
`τ(m) ≤ m^{1.5379·log2/loglog m}`, the per-application loss falls below `m^{1/10}` only when
`loglog m > 10.7`, i.e. `K ≳ 15000`. Two caveats on wording:
* "my O(N) scan is infeasible at K=11". ET Remark 3.1 gives an `N^{2/5+o(1)}` algorithm. At
  `N = 17^{11} ≈ 3.4·10^{13}` that is about `4·10^5` factorisations, which is cheap, so levels 6–7 are
  computable. They would not change the logic.
* Novelty: two web searches found no prior statement. The arithmetic engine behind the parity and
  cell restrictions is the classical Yamamoto/Schinzel reciprocity of ET Prop 1.6 (compare the √Q
  argument in Claim A). The new content is the box/ES-solutions dictionary and the measure reduction.
  It is plausible that this is new. Not verified beyond ET and the two searches.

## Defects

**FATAL:** none. **MAJOR:** none.

**MINOR**

* **m1 (§2 "Consequence", §4 "Ineffective convergence").** ET Prop 1.7 *as stated* bounds `f_I(n)`,
  `f_II(n)` (Type I/II *solutions*, coprimality conditions included) and `f(p)` for primes only. It
  does not bound `f(17^k)`, the count of all ordered solutions, which the first series uses. Repair:
  (a) bound (Q) by N-points of `Σ^I_{17^k}` and cite the *proof* of Prop 1.7 (ET §3 counts N-points
  obeying Lemma 2.8, and Lemma 2.8's proof uses only the equations); (b) bound (U) by ET's ref. [8]
  (Browning–Elsholtz, `f(n) ≪ n^{2/3+ε}` for all n), or by a direct argument. Also, "ineffective" is
  the wrong word: the bounds are effective but not explicit, and any explicit version is far too weak
  (Claim E). Say "non-explicit".
* **m2 (§3 "Even K are empty", Lemma-table summary).** ET Prop 1.6's *statement* concerns Type I/II
  solutions. The N-points used here (Q: ET's `c=j` may be divisible by 17; P: ET's `a=i`, `b=j` may be)
  are not a priori Type I/II solutions. ET's proof (§4) uses only (2.1), (2.2), (2.13), (2.14), so it
  does apply. Repair: cite the proof, or use the direct reciprocity argument from Claim A, which gives
  `K` odd for (P) and `k` odd for (Q) in two lines. For (U), even levels are only *computed* empty
  (k = 2, 4, 6; I reproduced this). That is fine, because `B_k` keeps `D_U(k)` for all `k`.
* **m3 (Lemma 1.1, §4 `B_k`).** The (√Q) type is empty (Claim A, PROVED). Drop the "only (√Q) may break
  the symmetry" caveat: the `C_5 ↔ C_7` symmetry is exact. `B_k` can use `4D_Q` instead of `8D_Q`.
  This is harmless as it stands.
* **m4 (Theorem 4.1 threshold, rounding).** The exact uncovered fraction after level 5 is
  `56561/83521 = 0.6772069300…`, which is *less than* the stated threshold 0.677207. As written, the
  theorem is false for tails in `[0.67720693, 0.677207)`. Repair: state the threshold as `56561/83521`
  (or 0.677206).
* **m5 (Cor 4.2 wording).** "primes `p` with `(p/17)=−1` and `(p/q)=+1` for `5≤q<17`" is called
  "Mordell-hard primes with `n_p=17`". The latter also requires `p ≡ 1 (24)`. The proof covers both,
  since `Q` can be chosen divisible by 24. Also, Cor 4.2 is an implication from an unproven
  hypothesis: label it CONDITIONAL (on a sterile point), not PROVED.
* **m6 (§3 EVIDENCE claim "the measure added per level falls by roughly a factor 17–20 per level").**
  The data say otherwise. The increments are 0.235294, 0.079585, 0.006920, 0.000994 (levels 2–5),
  ratios ≈ 3.0, 11.5, 7.0. Repair: state the actual ratios. The "geometric decay" in the Assessment
  rests on three increments only.
* **m7 (AGENT_REPORT_O83, "Corrections to POINTWISE_MORDELL §5").** The report says the level-2
  boxes in `C_5` have "moduli exceed[ing] 10⁵, which is why the earlier brute-force run did not see
  them". That is false. The box `56 mod 289` comes from the I1 class `(a,d,f) = (1003, 17, 96759)`,
  i.e. `n ≡ −96759 ≡ 39649 (mod 68204)`, with `68204 = 4·17²·59 < 10⁵` (`39649 ≡ 1 mod 236`,
  `≡ 56 mod 289`, `96759·707 = 4a²d+1`). My raw brute force at `M ≤ 10⁵` sees all four level-2 boxes.
  Hence **POINTWISE_MORDELL §5's statement "the cells `x_17≡5`, `7` are entirely uncovered by all
  classes with `M≤10⁵` (k=2)" is itself false**. The old run must have truncated I1 (cf. the
  `MORDELL_I1CAP` knob). Forward this to R80. Comp. 5.1 (u=5 in no class with `M≤10⁶`) is consistent
  with my data.
* **m8 (Cor 2.4 text).** "For (P), `K≥1` as `k≥1`... and `k=0` forces `K=0`" is garbled. Write:
  "`k=0` forces `α=δ=0`, hence an N-point of `Σ^II_1`, i.e. a solution of `4/1`".
* **m9 (Replay).** The P-engine claim "≈8 min" for K=9 reproduces: 6 min here. No issue. Note that
  §3's "Validation (completeness)" relies on the unreviewed `mordell_tgen.py`. My raw brute force
  replaces it (0 missing at `M ≤ 10⁶`).

## Summary verdicts

| claim | verdict |
|---|---|
| §2.1 T-generic table (at T={17}) | SOUND (re-derived from the Prop 1.9 statement; brute force M≤10⁶ agrees) |
| Lemma 1.1 (box types, P-inversion) | SOUND; √Q is in fact empty (m3), so the C_5↔C_7 symmetry is exact |
| Lemma 1.2 / Cor 2.4 (no level 0) | SOUND (m8 wording) |
| Lemmas 2.1–2.3 (bijections, half level ⌈K/2⌉, 17^{1−k} weights) | SOUND |
| §2 measure bound, convergence | SOUND-AFTER-REPAIRS (m1, m2: cite proofs not statements; "non-explicit") |
| Computation 3.1 | SOUND: reproduced exactly by an independent engine through level 5 (+Q/U level 7); u=5,7 in no box |
| Theorem 4.1 | SOUND-AFTER-REPAIRS (m4: threshold must be 56561/83521, not the rounded-up 0.677207) |
| Corollary 4.2 | SOUND as an implication (m5: label CONDITIONAL, fix the target-set wording) |
| §4 status / Assessment / novelty | SOUND as Assessment (m6 overstated decay; K=11 is computable) |
| AGENT_REPORT correction to POINTWISE_MORDELL §5 | WRONG diagnosis (m7); POINTWISE_MORDELL §5 "M≤10⁵ leaves C_5 uncovered" is false |

Replay (reviewer):
```
gcc -O2 -o /tmp/r83/enum scripts/review_m17_enum.c
cd /tmp/r83; for k in 1 2 3 4 5 6 7; do ./enum S $k > S$k.txt; ./enum U $k > U$k.txt; done
for K in 1 2 3 4 5 6 7 8 9; do ./enum P $K > P$K.txt; done      # P 9: ~2 h, P 8: ~5 min
PYTHONPATH=scripts uv run python scripts/review_m17_brute.py 1000000 3 /tmp/r83/brute_1e6.pkl   # ~5 min
PYTHONPATH=scripts uv run python scripts/review_m17_union.py /tmp/r83 5 /tmp/r83/brute_1e6.pkl
PYTHONPATH=scripts uv run python scripts/review_m17_union.py /tmp/r83 7      # needs ~1 GB
uv run python scripts/review_m17_tail.py
```
