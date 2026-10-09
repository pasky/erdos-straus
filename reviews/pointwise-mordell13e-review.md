# Review R107 of POINTWISE_MORDELL13E.md (O107, branch side-agent/xss-sterility) — light, hostile

Reviewer: side agent R107 (branch `side-agent/review-m13e`). Scripts: `scripts/review_m13e_*.py` (from scratch).

## Verdicts

| claim | verdict |
|---|---|
| Lemma 2.1 (parity of ES level in the (2,2) cell) | SOUND |
| §2 scope (x** ≡ x* mod 143 ⇒ no mod-143 argument) | SOUND-AFTER-REPAIRS (minor overstatement, repaired) |
| Comp 3.1 (x** in no class of ES level < 2.59·10¹⁰) | SOUND (CERTIFIED is the right label) |
| Comp 3.2 (C_3 part) / Comp 3.3 (smallest miss 11) | SOUND (recounted, spot) |
| Prop 4.1 (measure criterion; reduction) | SOUND |
| Labels | SOUND after defect 1 |

No FATAL or MAJOR defect found.

## Lemma 2.1 — SOUND

Re-derived. 13B Lemma 1.2 needs only: for q | (relevant T-part), the class condition reduced mod q,
i.e. `f≡−x_q`, `2a²d≡−1` (II3/II2, from `e_T | x_q+4a²d` and `x_q≡2 (q)`), `c²d≡−1` (I3, from
`f_T | x_q²+4c²d`), `c≡−2a` (I2), `2e≡−1` (I4) mod q. All of these depend on `x_q mod q` only, so the lemma
holds on the whole cell `x_11≡2 (11), x_13≡2 (13)` (15≡2 mod 13: yes). The ES-level formulas (13B Lemmas
2.1–2.4, Cor 2.5) give the parities stated: II1/I4 `v_T(ab)`, II2 `v_T(f)`, I2 `v_T(ac)+v_T(f)`, II3
`v_T(e)+v_T(d)` (since `N=e_T a_T² d_T`), I1 `v_T(d)`, I3 `v_T(f)+v_T(d)` (`N=f_T c_T² d_T`); with Lemma 1.2
(`v_T(d)` odd for I3) this is the statement.

*From-scratch check* (`scripts/review_m13e_parity.py 3000 {1,2}`): random T-generic data of all 7 families
(T-parts up to `11³`, `13³`, `11²13`, …), literal classes from the ET Prop 1.9 residues (own code), ES level
**verified by the explicit ES identity** of 13B Lemmas 2.1–2.4 (exact fractions) for every T-generic datum
(≈38 000), `M_T ≤ N ≤ M_T²` for all; 906 data whose box meets the (2,2) cell: **0 parity failures**. The I3
exception is non-vacuous (both parities of `v_T(f)` occur). Negative control: in the cell (2,1) the same test
fails for 25 of 208 data, so the check has teeth.

## §2 scope — SOUND-AFTER-REPAIRS

`15 ≡ 2 (mod 13)`, so x** ≡ x* (mod 143); x* lies in the II3 class (8,33,11999) (13B Thm 3.1, re-found below by
the independent pipeline at level 1859). Any criterion that is a function of `x mod 143` would therefore declare x*
sterile too: contradiction. That sentence is PROVED (trivially) and correctly so labelled in §5. The add-on
"the non-torsion part of `ℤ₁₃^×`, which no reciprocity law sees" is too strong: Dirichlet characters of
conductor 13² (order 13) are non-trivial on `1+13ℤ₁₃` and separate 15 from 2 (`15·2⁻¹ ≡ 1 mod 13`, `≢ 1 mod 169`).
Repaired in place (defect 1).

## Comp 3.1 — SOUND

*Completeness of `m13e_es.c` (read line by line).* For `x ≤ y ≤ z` one has `N/4 < x ≤ 3N/4` (range
`N//4+1 … 3N//4` correct). With `r/s = (4x−N)/(Nx)` reduced, `(ry−s)(rz−s)=s²`, `D=ry−s>0`, `y ≤ z ⇔ D ≤ s`;
`y` integral ⇔ `D ≡ −s (r)`, and then `s²/D ≡ −s` automatically (D is a unit mod r because `gcd(r,s)=1`), so
`z` is integral. Every solution is therefore a divisor `D ≤ s` of `s²` in that residue class. The code:
* factors `s = Nx/g` from the factorisation of N, the segmented-sieve factorisation of x (primes `p²≤hi`
  removed; the cofactor is 1 or a prime since `p² > hi ≥ x`), minus that of g (aborts if g does not divide out);
* enumerates all `d₁ ≤ s` over group-1 primes and all `d₂ ≤ s` over group-2 primes (the early `break` on `v>s`
  is monotone in the exponent; every `D=d₁d₂ ≤ s` has both factors `≤ s`), so nothing is pruned wrongly;
* matches `d₁ ≡ −s·d₂⁻¹ (r)` exactly (residues tracked by `mulmod`; operands `< r < 2³⁵` at these N, so the
  double-precision quotient is off by ≤1 and the correction loops fix it; `r ≥ 2⁵⁰` aborts), then checks
  `d₁d₂ ≤ s` via `d₁ ≤ ⌊s/d₂⌋` (exact) and `y ≥ x`;
* the hash table (linear probing, size `≥2n₁`, `n₁ ≤ 2²²` < table `2²⁴`) and the bitmap prefilter can only
  produce extra probes, never false negatives; divisor overflow (`DMAX`) aborts without a completion line.
128-bit: `s ≤ N·3N/4 < 10²⁰`, products `≤ s·P < 10³¹` fit in `u128`. `m13e_inv.py` recomputes `z` exactly and
asserts the chunk tiling — false positives and missing chunks cannot pass silently.

*Independent re-runs* (from-scratch or other-reviewer code only):
* `scripts/review_m13e_cmp.py /tmp/o107/run <all 20 T-units ≤ 4·10⁵>`: plain-Python ES enumeration + the R95
  reviewer-derived inversion and literal ET classes (`review_m13b_enum.py`). At every level the **ES solution sets
  are identical** to the author's raw chunk files (not only counts), and **independent boxes ⊆ author boxes** at
  every level (0 missing). The author has 2306 extra boxes (union); all are literal ET boxes whose stored datum has
  canonical ES level outside the tested list (non-canonical re-finds, as documented in 13B §4). x* found exactly
  (II3, I2 at 1859); x** in no independent box.
* `scripts/review_m13e_spot.py` (own enumeration: sympy factorisation, *all* divisors of `s²`, exact fractions) on
  random 20000-x windows (30% near N/4, where solutions are dense): N = 13⁹, 8973037931, 5436100813 (run 2, bitmap
  engine; 1.32·10⁶ x with `Nx > 2⁶⁴`) and 4599777611, 2357947691 (run 1, older engine): 2.6·10⁶ x, 34 018
  solutions, **all windows identical**.
* `scripts/review_m13e_hits.py`: own box test on all 54 pkl files: 54 = all T-units `1<N≤13⁹`, none in
  `(13⁹, 11¹⁰)`; 2 865 550 ES solutions (matches); **0 boxes contain x\*\***; x* data exactly the two of 13B.
* Consequence (a) re-checked: T-units `≤161050` are 11, 13, 121, 143, 169, 1331, 1573, 1859, 2197, 14641, 17303,
  20449, 24167, 28561 (11⁵ = 161051 just misses), and `N ≤ M_T² < 11¹⁰` puts all their data in range; the
  "newly complete" list `11³,13³,11⁴,13⁴,11³13,11·13³` is right.
*Residual dependence* (not new, stated in 13B): completeness of `m13b_invert.cands` (now additionally confirmed at all
levels ≤ 4·10⁵ by the independent inversion) and 13B Lemma 1.1 (R95-reviewed).

## Comp 3.2 (C_3) / 3.3 — SOUND (spot)

`scripts/review_m13e_c3.py`: 445 655 distinct boxes; exactly 7 meet `C_3`, at levels 2357947691 (5), 2786665453,
3293331899, total mass `7.73·10⁻⁵` (sum over boxes, i.e. an upper bound for the union — fine for Prop 4.1).
Smallest miss 11 (e.g. I3 at `M_T = 11³·13`). The `C_2` numbers were not re-checked.

## Prop 4.1 — SOUND

Boxes are clopen subsets of `ℤ₁₁^× × ℤ₁₃^×` (the slice `x_q=1`, q∉T), countably many; any class containing a slice
point is T-generic (13B Lemma 1.1), so a slice point outside all boxes is sterile. If the levels `≤N₀` leave a set
of relative measure U of `C_3` uncovered and the levels `>N₀` have `Σμ₃ < U`, the uncovered part has positive
measure (subadditivity). `U ≥ 1−7.7·10⁻⁵` uses the union bound in the right direction. The weight formula
`μ₃ = 11^{−max(0,v₁₁−3)}13^{−max(0,v₁₃−3)}` is right for a single-residue box meeting `C_3`. A sterile point x
in the slice is a limit of primes in the Mordell-hard, `(p/11)=(p/13)=−1` set (`x_q=1` off T, `x_11, x_13`
non-residues), and the complement of a finite union of classes is open, so Dirichlet gives an uncovered prime:
the direction "sterile point ⇒ no finite covering" is correct. The hypothesis is (correctly) not claimed.

## Defects

1. MINOR (§2 "Scope", last sentence of the first paragraph). "non-torsion part of `ℤ₁₃^×`, which no reciprocity
   law sees" overstates: characters of conductor 13² see it. **Repaired in place (R107 repair)**; the PROVED part is
   only the trivial "no function of `x mod 143`" statement. The report (item 3) says "(quadratic or higher
   reciprocity at 11 and 13)" — acceptable if read as conductor-q symbols.
2. MINOR (`m13e_es.c`, hash `stamp`, uint32). In an unchunked run with more than 2³² x-values (`N ≳ 8.6·10⁹`
   with the default range) the stamp wraps; stale/never-written slots then look occupied. This can only cause extra
   probes, spurious candidates (rejected by `m13e_inv.py`) or a hang — not a missed solution — and the actual runs
   used chunks of 2.5·10⁸. Suggested: reset `ht` when `stamp` wraps, or document "chunks < 2³² x".
3. MINOR (§1, `mulmod` comment "valid for a, b < m < 2⁵⁰"). True but stated without argument; at these N
   `r < 2³⁵`, so the margin is huge. No change needed.

No other issues. Labels in §5 and the report are appropriate (Comp 3.1 CERTIFIED; Lemma 2.1, Prop 4.1 PROVED;
x** sterility OPEN).
