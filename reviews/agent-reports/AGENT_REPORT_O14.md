# AGENT REPORT O14 — B-removal for EXCEPTIONAL_KARY Thm 4.5; (a,D)/Case-A extension

Branch: `side-agent/kary-no-b`. Deliverable: `EXCEPTIONAL_KARY2.md`;
scripts `scripts/kary2_square_check.py`, `scripts/kary2_moments.py`;
data `data/kary2/`.

## Result (checkpoint 2, after both hostile reviews)

Both reviews found Theorem 5.1 SOUND. Every defect from both is now
applied (list below).

**Theorem 5.1 (PROVED internally; the Case-A part uses Elsholtz–Tao
Prop. 1.4, published, not re-proved, the same input as ET Lemma 3.7).**
Take any finite mixture 𝔊 of ℛ(M)-, (a,D)-, Case-A and **selector**
(`0 mod p`) classes, with arbitrary moduli: no B, no dominant prime, any
number of primes. Every majorant of level λ of the *whole* avoider set
`𝒜(𝔊)` then satisfies `log(1/Eν) ≤ Cλ^{3/4}(log λ)^{3/4}`, with C, W
absolute. These constants are astronomically large, so the statement is
asymptotic only.
* **Thm 5.2:** under `G ≤ P(G)^{1+B}`, the bound is `≪_B λ^{3/4}` for all
  four types. This covers the 3/4 note's selector majorant `S_y·Q_r`,
  whose atoms are ℛ(kℓ) with `B < 1/120` (Remark 5.4).
* **Cor 6.1:** the setting is nonnegative CRT majorants of the avoider set
  of such a family, with rounding `Σ|a_i| < N` and family primes
  `≤ N^{O(1)}`. Their saving is `≪ (log N)^{3/4}(log log N)^{3/4}`. So no
  method *of this class* gives θ > 3/4. The excluded methods are listed in
  §6: large sieve beyond prime slices, inter-frequency cancellation,
  weights < 1, ν ≥ 1 only on [1,N] or on exceptional primes, non-CRT
  input, and other class types.

## Review defects applied

* **Review 1 (`side-agent/review-kary2`)**
  * D1 (selector scope): selector classes are now a fourth type
    (Def 2.0).
    * Base: they contain 0 but no unit square, so Lemma 2.3(1) is now
      stated for "no unit square".
    * First moment: `≪ log log y` (Lemma 3.3′).
    * Second moment: +1 deterministic, q = 1 (Lemma 4.2).
    * Remark 5.4 gives the 3/4-note reading.
  * D2: the Lemma 3.1 Euler-factor step is repaired (`y₀ ≥ e^{10}`,
    `p^{−0.9e}`).
  * D3: `c_q = 2^{7q+1}+1`; "u ≥ u₀−δ ≥ 1".
  * D4: "no θ > 3/4" is qualified in the §0 table and in this report.
  * §1 now lists all three uses of `q ≤ ℓ^B` in (B3).
  * The ET side note is recorded after Cor 6.1.
* **Review 2 (`side-agent/review-kary2b`)**
  * D1: as review 1 D1.
  * D2: "ElT" denotes Elsholtz–Tao, separately from ET =
    EXCEPTIONAL_THETA. The label "PROVED, using ElT Prop 1.4 (published,
    not re-proved)" replaces "modulo".
  * D3: the large sieve and NONCRT Thm 2.3 are explicitly marked as not
    transferred.
  * D4: the requirement "ν ≥ 1 on all of 𝒜" is made explicit, and the
    weaker variants are listed as excluded.
  * D5: C absorbs `2W + log 2`; asymptotic-only wording.
  * D6: the Schinzel pointer is added as an unchecked remark.
  * The coverage list from (C) and the reviewers' independent checks
    (§7) are recorded.

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

## Caveats

* Theorem 5.1 has a `(log λ)^{3/4}` loss, which comes only from
  smooth-dominated moduli (Remark 3.8). It is expected to be an
  artefact of the proof, but this is unproved. TW4 §11 predicted
  `λ^{3/4}log λ`.
* Case A uses ElT Prop 1.4 (body only). ℛ(M), (a,D) and selector classes
  use no external input.
* The constants are absolute but astronomically large (review 2:
  log W ≈ 10^{10–11}).

## Suggested ledger / STATUS changes (not made; parent's call)

* DISCOVERIES (D)17, "Open": replace with a pointer to (D)18.
* New (D)18: use review 2's suggested entry (its §(C)), which matches the
  final text.
* STATUS "A θ>3/4 proof would need …":
  * drop the B-removal bullet;
  * add "classes outside the four types (any family with no unit square
    in its W-smooth classes, cubic-polylog first moments and `ℓ^{o(1)}`
    cofactor second moments is covered, KARY2 §6 item 2)";
  * add "majorants ≥ 1 only on [1,N] or on exceptional primes".
* ETw Remark 1.4: its square-base observation is now proved (KARY2
  Lemmas 2.1–2.2).
* ET, after Lemma 2.9: the "Consequence" paragraph uses s where
  `S = log(1/Eν)` is needed. The conclusion is unaffected (KARY2 Cor 6.1
  side note).

## Replay

```
cd scripts
uv run --with sympy python kary2_square_check.py 60 600 6000   # ~1 s
uv run --with numpy python kary2_moments.py 1000000 10000000   # ~3 s
```

Checkpoint 2 complete; stopping for merge.
