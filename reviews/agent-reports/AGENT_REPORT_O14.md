# AGENT REPORT O14 — B-removal for EXCEPTIONAL_KARY Thm 4.5; (a,D)/Case-A extension

Branch: `side-agent/kary-no-b`. Deliverable: `EXCEPTIONAL_KARY2.md`;
scripts `scripts/kary2_square_check.py`, `scripts/kary2_moments.py`;
data `data/kary2/`.

## Result (checkpoint 1)

**Theorem 5.1 (PROVED internally; the Case-A part is modulo Elsholtz–Tao
Prop. 1.4, the same input as ET Lemma 3.7).** For any finite mixture 𝔊
of ℛ(M)-, (a,D)- and Case-A forced classes with arbitrary moduli (no B,
no dominant prime, any number of primes), every majorant of level λ of
`𝒜(𝔊)` has `log(1/Eν) ≤ Cλ^{3/4}(log λ)^{3/4}`, with C, W absolute.
* **Thm 5.2:** under `G ≤ P(G)^{1+B}`, the bound is `≪_B λ^{3/4}` for all
  three types. So EK Thm 4.5 extends to (a,D)/Case A with no log loss.
* **Cor 6.1:** for coefficient-sum methods (`N·Eν + Σ|a_i|`,
  `Σ|a_i| < N`) whose family primes are `≤ N^{O(1)}`, the saving is
  `≪ (log N)^{3/4}(log log N)^{3/4}`. So no θ > 3/4 is possible.

## How

* **Where B entered EK** (§1): only in (B1) the block first moment, (B2)
  the singleton first moment, and (B3) the pointwise τ-bound in the
  second moment (leak). The k-ary step, the base, the leak mechanism and
  the top block are B-free. The number of primes per modulus enters
  nowhere (goal 1 check). This is unlike the Λ² route of TW4.
* **Base for (a,D)/Case A** (§2). Lemmas 2.1–2.2 prove that no (a,D)- or
  Case-A class contains a square mod its modulus. The (a,D) proof goes
  via Lemma 3.2 of ET plus Mordell. Case A uses a direct Jacobi
  computation. This proves ETw Remark 1.4's numerical observation. The
  square base `R_W^□` then has R-term `≤ 2W`.
* **First moments without B** (§3). Each sum is split at `G = y^{u₀}`,
  with `u₀ ≍ log log y`:
  * the body is the old bounded-B sum, with `B = u₀`;
  * the tail is bounded by Rankin (`e^{−u}`) combined with Cauchy–Schwarz
    against crude polylogarithmic second moments of the shifted divisor
    weight, and it is `O(1)`.
  The (a,D) sum is a pure Euler product `≪ (log y)³` with no loss. For
  Case A, the crude moments come from a self-contained small-divisor
  domination plus box count (Lemmas 3.4–3.5). The price is
  `(log log y)³`, hence `(log λ)^{3/4}` in the cap, with
  `s₁ = λ^{1/4}(log λ)^{−3/4}`. No (D)/(H)/(G) split is needed.
* **Second moments** (§4). AM–GM reduces `E N²` to a cofactor sum, which
  needs no size bound on the cofactor. Long blocks use Rankin together
  with Cauchy–Schwarz (Shiu for ℛ(M); Lemma 3.5 for Case A); short
  blocks use pointwise divisor bounds. The result is
  `E p_ℓ² ≪ ℓ^{−7/4+o(1)}`, so the leak is `≤ 1/2` with W absolute.

## Deviations, caveats

* Theorem 5.1 has a `(log λ)^{3/4}` loss. It sharpens the exponent
  statement but does not give the exact `λ^{3/4}`. The loss comes only
  from smooth-dominated moduli (Remark 3.8). Removing it would need
  shifted-smooth divisor sums `Σ_{M≤x,P(M)≤y}τ(A_M²) ≪ Ψ(x,y)log²x`
  (Fouvry–Tenenbaum type). TW4 §11 predicted `λ^{3/4}log λ`.
* Case A depends on ET Prop 1.4 (body only); ℛ(M)+(a,D) families are
  unconditional.
* Constants are astronomically large for Case A (`c₂ = 2^{15}+2` in
  Lemma 3.5). This does not matter for the statement, since the
  constants are absolute.
* Self-review (codex, deep) found four defects, all repaired:
  * Cor 6.1 used the saving inequality in the wrong direction (this is
    inherited from ET's prose after Lemma 2.9; the parent may want to
    check ET's own wording);
  * a projection of ν onto residues mod lcm(moduli) was missing before
    ET Lemma 2.9;
  * `Q₀` must be W-smooth;
  * a typo in §3.

## Suggested ledger / STATUS changes (not made; parent's call)

* DISCOVERIES (D)17, "Open": replace with a pointer to (D)18.
* New (D)18: "3/4 sharp for all ℛ(M)/(a,D)/Case-A forced-class CRT
  majorants, no B (EXCEPTIONAL_KARY2 Thm 5.1/Cor 6.1): saving
  `≪ (log N)^{3/4}(log log N)^{3/4}`; with bounded B `≪ (log N)^{3/4}`
  for all three types (Thm 5.2). PROVED (internal, one self-review);
  Case A modulo ET Prop 1.4."
* STATUS "A θ>3/4 proof would need …": drop the B-removal bullet. Add
  "other forced classes beyond the three types (any family with the
  no-square property and cubic-polylog first moments is covered, KARY2
  §6 item 2)".
* ETw Remark 1.4: its square-base observation is now proved (KARY2
  Lemmas 2.1–2.2).

## Replay

```
cd scripts
uv run --with sympy python kary2_square_check.py 60 600 6000   # ~1 s
uv run --with numpy python kary2_moments.py 1000000 10000000   # ~3 s
```

Stopping here for the parent's review.
