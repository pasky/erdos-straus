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

---

# Round 2 (merged `side-agent/sterility-r17` at 926cf6c)

## R2.1 Round-1 repairs: all 9 applied correctly, 3 small leftovers

I checked m1–m9 in POINTWISE_MORDELL17.md. Lemma 1.3 is stated and proved correctly and credited.
The threshold is 56561/83521, `B_k` uses `4D_Q`, Cor 4.2 is CONDITIONAL with `p≡1 (24)`, the m7
correction is in, and so on. The "28 of them in `C_5∪C_7`" figure in §3 matches my brute-force
pickle (168 boxes, 28 in-cell). Leftovers:
* **r1.** The §3 heading still says "(CERTIFIED by one engine; independent re-check pending)".
  Comp. 3.1 is now reproduced by two independent engines (this review, Claim C). Update the label.
* **r2.** The m1 wording comes back twice. §6 says "stop at `N^{2/5+o(1)}` ineffectively", and
  AGENT_REPORT checkpoint 2, row (b), says "ET gives `N^{2/5+o(1)}`, which is ineffective". Use
  "non-explicit".
* **r3.** The checkpoint-1 table in AGENT_REPORT_O83 still shows 0.677207, `8D_Q`, "ineffective" and
  the withdrawn "moduli exceed 10⁵" text. This is acceptable as history, but mark it "superseded,
  see repairs table".

## R2.2 §5–6, checked from scratch (`scripts/review_m17_round2.py`, using my own enumerations)

| claim | verdict | evidence |
|---|---|---|
| Lemma 5.1 (Q, P boxes = balls centred at `−a/b`) | **SOUND** | Re-derived: (2.3) `c(4abd−1)=n(a+b)`; (2.20) `bf = Nc+a`. Checked on all Q data k≤7 (both orientations) and all 1017 P data K≤9: 0 mismatches. 0 P data with `17∣a,b`; 0 Q data with `17∣c` |
| Q⁻¹ = Q | **SOUND** | equal box sets at k = 1, 3, 5, 7 (4, 112, 352, 1052 boxes) |
| Lemma 5.2 (U never new) | **SOUND-AFTER-REPAIRS** (n1, n2; the statement is true) | Re-derived both cases. For every in-cell U datum (286 of 1208, k≤7) I rebuilt the proof's Σ^II point `(b',c',a',i)` at `17^{α−β}`, checked the equation and the centre `−b'/c'`, and found a P box of strictly lower level containing the U box: 286/286; `α−β` always odd |
| New-box counts in C_5 | **SOUND** (reproduced exactly) | level 2: P 4; 3: Q 8, P 16; 4: P 34; 5: Q 29, P 54; 7: Q 94 (P levels 6–7 absent, as in the author's run) |
| §6 "(a,b) determines the P-point" | **SOUND** | brute force over all `(a,b)` with `2ab ≤ 17^K`, `e = (−17^K mod 4ab) ∣ a+b`, `17∤cd`: the sets for K = 1, 3, 5 equal the enumerated P data exactly |
| §6 (a,s,t) parametrisation | **SOUND-AFTER-REPAIRS** (n4) | brute force over `(a,s,t)` (bounds `4a²t ≤ N+2a`, `f ∣ N+4a²t`), with `17∤st`: the sets equal the P data for K = 1, 3, 5 |
| periodicity in K mod `ord_{4ab}(17)` (nesting per `(a,b)`) | **SOUND** | 300 pairs, K up to 120: 8301 checks, 0 violations beyond `K₀` |
| radius `≤ (2ab)^{−1/2}`; "scaled vs primitive" | **SOUND** | elementary, re-derived |
| Digit-set test (EVIDENCE, negative) | **SOUND** (n5 numbers) | my `t` medians are 0.179, 0.249, 0.176, 0.121 and maxima 0.857, 0.867, 0.989, 0.883 (levels 3, 4, 5, 7). The conclusion (no fixed θ) stands |
| Conjecture 4.3 | correctly labelled CONJECTURE | — |
| discrete-log heuristic / Assessment | acceptable as Assessment (n6 wording) | Note: `D_P(K)` = 2, 32, 121, 258, 604 against `K³` = 1, 27, 125, 343, 729 (K = 1..9 odd). The author's `K³` heuristic matches the data strikingly well; worth stating as EVIDENCE |

## R2.3 Round-2 defects (all MINOR; no FATAL or MAJOR)

* **n1 (Lemma 5.2, "strictly lower level").** The P box has level `⌈(α−β)/2⌉`. It equals the U level
  `α+β` exactly when `(α,β) = (1,0)`, i.e. `k=1`, where the two boxes coincide. The statement survives
  because no level-1 box meets `C_5∪C_7` (Comp. 3.1). Repair: say "level ≤ k, strictly lower for
  k ≥ 2; level-1 boxes miss the cells", or restrict to k ≥ 2.
* **n2 (Lemma 5.2, "U is empty at even levels").** As written, the proof only covers data with
  `17∤i` ("so 17∤i" relies on the box ≡ 1 being out of the cells). So it proves the parity only for
  in-cell U data. The full claim is still true. In case α>β the Σ^II point `(b',c',a',i)` exists
  whether or not `17∣i` (only `17∤e` is used). Lemma 1.3's reciprocity argument applies to *any*
  N-point of `Σ^II_{N'}`: `f = 4ACD−1 ≡ −1 (mod 4D)` and `f ∣ 4C²DN'+1` give `(N'/f) = −1`, so
  `N'` is not a square. Hence `α−β` is odd, and so is k. Repair: cite Lemma 1.3's argument, not
  "ET Prop 1.6". When `17∣i` the point is not a Type II solution, so the *statement* of Prop 1.6
  does not apply; this is the same issue as m2. Numerically, no U datum with `17∣i` exists at k≤7.
* **n3 (Lemma 5.1 hypotheses/remarks).** In (i), `17∤bc` can be weakened to the Q-datum condition
  `17∤e`, since then `4abd−1 = 17^k e` directly. The remark "for Q, `17∣c` forces box ≡1 (§2)"
  points to an argument §2 does not contain. The right reason is one line: `c ∣ a+b`, so
  `a ≡ −b (mod 17)` and `−a/b ≡ 1`.
* **n4 (§6 (a,s,t)).** "the P-data at level K are exactly the `(a,s,t)` with `f ∣ s·17^K+a` and
  `b≥a`" omits `17∤st` (= `17∤cd`). Without it one gets all N-points of `Σ^II_{17^K}`, not P-data.
  The "ever admissible iff `−a/s ∈ ⟨17⟩ (mod f)`" also tacitly needs `gcd(a,f)=1` and
  `17^K ≥ 4a²t − 2a`. Add these.
* **n5 (digit-set numbers).** "Median ≈0.15–0.2, max 0.87–0.99" does not match my values at levels
  4 (median 0.249) and 7 (median 0.121). Report the per-level numbers, or define `t` precisely if
  your definition differs.
* **n6 (overclaims in §6 and the report).**
  * "No method of that kind can reach the `N^{1/2−δ}` that is needed" is unproven. Rephrase as "we
    see no way for divisor-bound methods to …".
  * The heuristic "`Σ τ(a+b)/(4a·b)·b ≍ log³`" is garbled. The intended expression is
    `Σ_{a≤b, ab≤N} τ(a+b)/(4ab) ≍ (log N)³`.
  * AGENT_REPORT says "Sterility of C_5 is reduced, *exactly*, to an explicit bound". Theorem 4.1 is
    a *sufficient* condition, not an equivalence: overlaps can make the true union much smaller
    than the count bound. It is also a bound for both Q and P, not only P. Say "reduced to (a
    sufficient condition)".

## Round-2 summary

The repairs are good (r1–r3 are cosmetic). §5–6 are mathematically sound. Lemma 5.1, the new-box
data and the two §6 reparametrisations were reproduced exactly by independent brute force.
Lemma 5.2's statement is right, but its proof needs the two small fixes n1 and n2. The analytic
part of §6 is honestly labelled Assessment, apart from the overclaims in n6.

Replay (round 2): `ulimit -v 8000000; uv run python -u scripts/review_m17_round2.py /tmp/r83`
(~30 min, dominated by the `(a,s,t)` brute force at K=5; needs the round-1 enumeration files).

## Repairs applied (by the reviewer, on branch `side-agent/review-mordell17`)

At the parent's request, the reviewer applied r1–r3 and n1–n6 to POINTWISE_MORDELL17.md and
AGENT_REPORT_O83.md. One commit per item; each change is marked "(R83 round-2 repair …, applied by
reviewer)".
* r1: the §3 label now reads CERTIFIED by two independent engines.
* r2: "ineffective(ly)" is replaced by "non-explicit" in §6 and the report.
* r3: the report's checkpoint-1 section is marked superseded, with the list of corrected items.
* n1: Lemma 5.2 now says the P-box has level ≤ k, strictly lower for k ≥ 2, with equality only at
  (α,β)=(1,0). The report row is updated to match.
* n2: Lemma 5.2's parity claim now holds for all U-data, via Lemma 1.3's reciprocity applied to any
  N-point of Σ^II, in place of the ET Prop 1.6 statement.
* n3: Lemma 5.1's remark is fixed: `17∤e` suffices, and `17|c` gives `−a/b ≡ 1`.
* n4: the (a,s,t) parametrisation now includes `17∤st`, `gcd(a,f)=1` and the exact `b≥a` bound
  `4a²t ≤ 17^K + 2a/s`.
* n5: the digit-set statistics are given per level.
* n6: three overclaims are softened ("no method can", "equivalent in difficulty", "reduced,
  exactly"), and the heuristic formula is fixed.
* Addition: the EVIDENCE line `D_P(K)` vs `K³` in §6.

No mathematical content was changed beyond these items.
