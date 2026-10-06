# AGENT REPORT O69: Type-I depth on {n_p = 7} (branch side-agent/typei-sterile)

Deliverable: `POINTWISE_TYPEI2.md` (results table at top, Replay at the end); scripts
`scripts/typei2_{formal.py,balls.py,s27.c,union.py,points.py,signcheck.c,nearmiss.c}`.

## Goal (1): compactness gap of Remark 6.2(ii): CLOSED (Theorem A)
* Certificates `(c,k,F)` define clopen classes `Cl(κ)⊂Ẑ`, and `Σ_r` (the closure of `{p hard, n_p=r}`
  in `Ẑ^×`) is compact. If no covering of height ≤X exists, compactness gives a point `x*∈Σ_r` that
  no height-≤X certificate covers.
* At `x*`, perturb only the q-adic components where `x*_q` is a root of some `N_{c,k}`. At most one
  value `ck²` per q can be a root, and the perturbation keeps `v_q(N_{V'})` fixed for the other
  values. This gives a fixing class `𝒞`. A certificate with B-smooth `d|f_{c,k}` on `𝒞` transfers
  back to `x*` (Step 3). The H-argument of Thm 2.1 (Steps 4–5) then gives `ck_min>X`.
* Result: under H, `C*(r)` equals the least height `X_r` of a finite covering, and `C(r)=∞` iff a
  *sterile point* (no certificate at all) exists in `Σ_r`. The direction `C*(r)≤X_r` is
  unconditional. Forcedness is not needed.

## Goal (2): C(7): not decided; large certified lower bound and an explicit candidate sterile point
* Reductions (PROVED). At points that are squares off 7, only slices with `v_7(c)` odd matter. For
  fixed other components, each certificate is a 7-adic ball. The residue-one point is covered at
  level 1 by exactly `(7,3,11), (7,3,23), (14,2,15)`.
* {2,7}-generic points (`x_q=1` for q≠2,7). Rigid parametrisation (Lemma 2.4):
  `c'JJ'−u=Λ`, `u|J+J'`, finitely many certificates per level, enumerated completely to
  `Λ≤3·10⁸`. The union of boxes leaves ≈1.03% of `Σ'` uncovered (EVIDENCE, slowly decreasing). All
  surviving integral points have `x_7=−1`.
* **Sign point** `x̂_w=(w at 2; −1 at 7; 1 elsewhere)`, `w≡9 (16)`. Here `x̂²=1` at every odd prime,
  so `N=1+4ck²` is an honest integer and certificates are integer solutions of (2.2). Square-family
  certificates are excluded by a 2-adic argument (Lemma 3.1, PROVED).
* **Computation 3.2 (CERTIFIED).** A factorisation-free exact checker (`typei2_signcheck.c`, about
  `√N/4ck<1` candidates per slice) found **no certificate at `x̂_9` for any slice with
  `ck≤3·10⁹`** (7.6·10⁹ slices). It was cross-checked by a sympy factoring engine (to `10⁶`, same
  slice count) and by the Λ-enumeration (to `ck≤8660`). Hence:
  * every finite Type-I covering of `{n_p=7}` has height `>3·10⁹`;
  * under H (explicit finite family from Thm A), **`C(7)>3·10⁹`** (was ≥539).
* Not proved: sterility of `x̂_9`, i.e. `C(7)=∞` under H (Conjecture 3.4).
  * Evidence (§5): the 2-adic near-miss mass per dyadic height bin decays (≈0.01 at `2³⁰`). The
    mechanism is partly proved: a non-square near miss needs a small divisor in a fixed odd class,
    which forces a deep 2-part.
  * A proof would need uniform bounds on divisors of `1+4ck²` in a residue class below
    `≈2^{α+2γ}k_o`. I see no route to that. Heuristically a `1/log` decay (hence eventual covering
    of a.e. w) is not excluded either. So I do **not** claim either direction for C(7).

## Goal (3): other r
* Sign points exist iff `r≡3 (4)` (PROVED).
* For `r≡3 (8)` every sign point is killed by `(r(r+1)/4, 2, 2r+1)` (`1+4ck²=(2r+1)²`; PROVED).
* For `r≡7 (8)` Lemma 3.1 holds. No certificate with `ck≤10⁹` exists at the sign points for
  `r=23, 31, 47`, so under H `C(r)>10⁹` and coverings need height `>10⁹` (CERTIFIED).
* For `r≡1 (4)` (including r=5, where C(5)=10) no sign point exists. This is suggestive but not a
  theorem. Suggested follow-up: a covering search for r=13.

## Things for the reviewer to check
* Theorem A Steps 2–3. The perturbation exponent T must exceed `v_q(4X!)`; this was repaired in the
  last commit.
* Lemma 3.1 case analysis (the 2-adic valuations of `1+7^s`).
* `typei2_signcheck.c` completeness. Every divisor pair has a member `≤√N` in the class ξ or `ξ^{−1}`,
  because `N≡1 (mod 4ck)`; the arithmetic is 128-bit.
* The Haar-measure normalisation in `typei2_union.py`. The §2.2 numbers are EVIDENCE only.
