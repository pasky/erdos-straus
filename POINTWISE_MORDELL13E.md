# POINTWISE_MORDELL13E — is x** = x(2,15) sterile? Complete enumeration by ES level (task O107)

Status: work in progress (side agent O107, branch `side-agent/xss-sterility`). Labels as in DISCOVERIES.md.
Builds on POINTWISE_MORDELL13B.md (§1 Lemma 1.1/1.2, §2 Cor. 2.5, §4 engine), POINTWISE_MORDELL13C.md (§3, §5).

Notation as in 13B: `T={11,13}`, `x** = x(2,15)` (`x_11=2`, `x_13=15`, `x_q=1` for q∉T). A *box* is
`(fam, M_T, r mod M_T)` of a T-generic datum; x** lies in the class iff `r≡2 (11^{v_11(M_T)})` and
`r≡15 (13^{v_13(M_T)})` (13B Lemma 1.1, CRT).

## 0. Baseline: all ES levels ≤ 4·10⁷ (CERTIFIED, 13B engine)

`scripts/m13e_boxtest.py 2 15 R` over the 13B/13C engine output (R = all 32 T-units `1<N≤4·10⁷` plus
`N=11⁴13⁴`; 229963 boxes): **0 boxes contain x\*\***. Positive control: the same test at x* = (2,2) returns
exactly the two data of 13B Thm 3.1 (II3 (8,33,11999), I2 (125,88,11999); re-found at four levels by the
non-canonical inversion).

## 1. A faster complete ES engine (m13e_es) and the per-level test

*Engine.* `scripts/m13e_es.c N [xlo xhi]` lists all `(x,y)` of ordered solutions `x≤y≤z` of `4/N=1/x+1/y+1/z`
with `x` in the given part of `(N/4,3N/4]`. Method of `m13b_es.c` (13B §4): `r/s=(4x−N)/(Nx)` reduced, `y=(D+s)/r` for
the divisors `D≤s` of `s²` with `D≡−s (mod r)`, `y≥x`. Changes: segmented sieve (no `O(N)` memory), 128-bit `s, D`,
and the congruence is solved by meet-in-the-middle (since `gcd(r,s)=1`, every `D | s²` is a unit mod r; split
the primes of s into two groups with balanced divisor counts; hash the group-1 residues `d₁ mod r`, scan the group-2
values `−s·d₂⁻¹ mod r`). `z` is not printed; `scripts/m13e_inv.py` recomputes `z=1/(4/N−1/x−1/y)` exactly and
aborts unless it is an integer `≥y`. It also aborts unless the chunk files tile `(N/4,3N/4]` (completion lines).
Then it applies the validated 13B inversion (`m13b_invert.cands/boxes_of`, Lemmas 2.1–2.4) and tests every box
against x** and x*. Speed: ≈1.1 µs per x at `N≈3·10⁷` (9× faster than m13b_es); with a bitmap prefilter on the
hash probes (commit after 91a45ed) ≈0.9 µs per x at `N≈10¹⁰`.
*Validation.* (i) Output identical (as sets of `(x,y)`) to `m13b_es` for N = 11, 121, 143, 1331, 1859, 2197, 24167,
371293, 32166277. (ii) At N = 32166277 the box set is identical to the 13B/13C engine output (25116 boxes).
(iii) At N = 1859 the two x* data are re-found. Chunked and unchunked runs agree.
(iv) Large N (128-bit regime, `s>2⁶⁴`): `scripts/m13e_es_check.py` (plain Python, sympy factorisation, all divisors
of `s²`) on 10 x-ranges at `N=10604499373` (near N/4, N/3, N/2, 3N/4, and around engine solutions): 6417 solutions,
identical. (v) The full rerun of all 32 levels `N≤4·10⁷` gives box sets identical to 13B's run
(`scripts/m13e_cmp_runs.py`, 209295 boxes).

## 2. What reciprocity gives at x** (PROVED, elementary)

**Lemma 2.1 (parity of the ES level).** Let a T-generic datum have a box containing a point x with
`x_11≡2 (11)`, `x_13≡2 (13)` (e.g. x* or x**; note `15≡2 (13)`), and let N be its ES level (13B Cor. 2.5). Then
`v_T(N)=v_11(N)+v_13(N)` is **odd**, except for I3, where `v_T(N)≡v_T(f)+1 (mod 2)`.
*Proof.* 13B Lemma 1.2 uses only `x_q mod q` (its proof is via `(q/g)`, `(−2/q)`, `(2/q)`), so it holds verbatim
in the cell. ES levels (13B §2): II1/I4 `N=(ab)_T`; II2 `N=f_T`; I2 `N=(ac)_T f_T`; II3 `N=e_T a_T² d_T`;
I3 `N=f_T c_T² d_T`; I1 `N=a_T² d_T`. Hence `v_T(N)≡v_T(ab)`, `v_T(f)`, `v_T(ac)+v_T(f)`, `v_T(d)+v_T(e)`,
`v_T(d)+v_T(f)`, `v_T(d) (mod 2)` respectively, and 13B Lemma 1.2 gives the claim. ∎
*Check:* `scripts/m13e_parity_check.py`: all 6062 engine boxes (levels ≤ 4·10⁷ and 11⁴13⁴) that meet the (2,2) cell
satisfy it.

*Scope: why reciprocity cannot separate x** from x* (Assessment).* Every quadratic (or higher power-residue) symbol
of the T-primes is a character of `(ℤ/q)^×` and sees only `x_q mod q`. Since `x**≡x* (mod 143)` and x* *is*
covered (13B Thm 3.1, level 1859), no argument that depends on `x mod 143` alone can show x** sterile. Sterility
of x** must use the 13-adic digit `15≢2 (mod 13²)`, i.e. the non-torsion part of `ℤ₁₃^×`, which no reciprocity
law sees. The usable content is a restriction on the levels: by Lemma 2.1 together with 13C Comp. 3.1
(x** in no box of T-level dividing `11²13²`), a box containing x** has T-level F with `v_11(F)≥3` or
`v_13(F)≥3`, and every family except I3 has odd `v_T(N)`.

## 3. x** through ES level 4.6·10⁹ (CERTIFIED)

**Computation 3.1.** `scripts/m13e_run.sh 1 4600000000 R` (all 49 T-units `1<N≤4.6·10⁹`; 2 035 665 ES solutions,
319 007 distinct boxes; ≈2.8 h on 2 cores; `logs/o107_run1.log`): **no box contains x\*\***. The x\* control
re-finds exactly the two data of 13B Thm 3.1 (at 6 levels, non-canonical re-finds). `scripts/m13e_summary.py R`.

*Consequences.* (a) Since every class containing the T-generic point x\*\* comes from a T-generic datum (13B Lemma 1.1)
whose ES level N satisfies `M_T ≤ N ≤ M_T²` (13B Cor. 2.5): **x\*\* lies in no ET class (seven families, any T-free
modulus) whose ES level is ≤ 4.6·10⁹**, in particular in none with T-level `M_T ≤ 67822`. With 13C Comp. 3.1 the
T-levels `F∤11²13²` that are now complete are `11³, 13³, 11⁴, 13⁴, 11³·13, 11·13³`.
(b) This is complementary to the targeted searches (13B Comp. 5.3, 13C Comp. 5.1–5.2), which bound the T-free
size (`e ≤ 2·10⁹` resp. `2·10⁸`) but not the level. Here the level is bounded and `e` is not: e.g. for II3,
`e = 4a'd'm−1 ≈ 4z/N` with `z` the largest denominator, which can be as large as `≈ N³`.

**Computation 3.2 (local box mass near x\*\*; CERTIFIED for the stated levels).** `scripts/m13e_density.py R k K`.
Put `C_k = {x_11≡2 (11^k), x_13≡15 (13^k)}`, and for a box β let `μ_k(β)=|β∩C_k|/|C_k|`. Boxes are counted at the
first level where they appear.
* `C_2` (one of the 15 uncovered k=2 subcells of 13C Comp. 3.1): boxes of level ≤ 4.6·10⁹ cover **56.25%** of it
  (union, boxes with `M_T | 11⁴13⁴`). Their mass per level falls from 0.1–0.3 at `N≈10⁵–6·10⁷`
  (dominated by single-prime levels `11⁵`, `13⁵`, `11⁷`) to 0.6–3.6·10⁻² at `N≈2–3·10⁹`.
* `C_3`: **only 7 boxes of level ≤ 4.6·10⁹ meet `C_3` at all** (levels 2357947691, 2786665453, 3293331899), with
  total mass `7.7·10⁻⁵`. So `C_3`, a neighbourhood of x\*\* of relative T-measure `1/(1331·2197)`, is at least
  99.99% free of boxes of level ≤ 4.6·10⁹ (not 100%: the 7 boxes are finer than resolution 5 and were not unioned,
  hence "at least").

**Computation 3.3 (near misses; CERTIFIED for the stated levels).** `scripts/m13e_closest.py 2 15 R`. For a box let
`a_q = min(v_q(M_T), v_q(r−x**_q))` (agreement), *miss* `= ∏ q^{v_q(M_T)−a_q}` (=1 iff the box contains x\*\*). Among the
319 007 boxes of level ≤ 4.6·10⁹ the smallest miss is **11**, attained by e.g.
* II3 `(a,d,e)=(183703,3,65219)`, `M_T=11³13²`, ES level 38014691: it agrees with x\*\* modulo `11²13²` and fails only
  in the third 11-adic digit;
* II3/I3/I1 `(4602,1859,18538271)`, `M_T=11·13³`: it agrees modulo `13³` and fails mod 11.

The deepest 13-adic agreement is `13⁴` (with miss 1331). So x\*\* is not isolated from the boxes by a wide margin: it is
missed by one digit in several independent ways, and its survival is "generic", not structural.

## 4. What a proof of sterility would need

**Proposition 4.1 (measure criterion near x\*\*; PROVED, as MORDELL17 Thm 4.1).** Let `N₀` be a level through which
the enumeration is complete, `U = 1 − |C_3 ∩ ⋃_{N(β)≤N₀} β|/|C_3|` (Comp. 3.2: `U ≥ 1−7.7·10⁻⁵` for `N₀=4.6·10⁹`).
If `Σ_{β: N(β)>N₀} μ_3(β) < U`, then `C_3` contains a sterile point: a point of Σ₁₃(main) in no ET class of the seven families.
Hence (13B §5, Dirichlet) no finite ET covering exists for the Mordell-hard primes with `(p/11)=(p/13)=−1`.
*Proof.* Countable additivity: the boxes of level `>N₀` cover at most `Σμ_3 < U` of `C_3`, which is less than what
the levels `≤N₀` leave uncovered. ∎

*What the hypothesis needs.* A box of T-level F meeting `C_3` without containing all of it has `v_11(F)≥4` or `v_13(F)≥4`,
and `μ_3(β) = 11^{−max(0,v_11(F)−3)}13^{−max(0,v_13(F)−3)}`. So one needs an explicit bound for the number of T-generic
data of ES level N whose box lies in `C_3`, summable against these weights, for **every** `N>N₀`. That is the open
explicit-ES-count problem of MORDELL17 §4/§6 (P-type data have box level ≈ `N^{1/2}`, against ET's
`N^{2/5+o(1)}` solutions with non-explicit constants). It is now posed at two primes instead of one. Nothing here closes it.

*For x\*\* itself* no measure argument suffices (a point has measure 0). By §2, a proof cannot use only `x mod 143`.
It would have to show, for every T-level F with `v_11(F)≥3` or `v_13(F)≥3`, that the box centres at F avoid the
specific 13-adic digit pattern of 15 (`15 = 2 + 1·13`). Comp. 3.3 shows that the centres come within one digit of x\*\*
in several unrelated ways. We see no structure to exploit (Assessment).
