# AGENT REPORT O71 — the soft-pivotal lemma (branch `side-agent/soft-pivotal`)

Deliverable: `EXCEPTIONAL_LARGESIEVE6.md` (LS6), `scripts/largesieve6_softpivotal_toy.py`.
**(A\*) is not proved.** ES is not solved. Checkpoint 1, self-reviewed.

## What is new (labels as in LS6 §0)

1. **Prefactors are free (Lemma 1.1, Cor 1.2; PROVED).** (A\*) enters LS4
   Thm 4.2 only through LS4 Lemma 1.1, where a global prefactor Λ costs
   `2β log Λ` (`β = (log N)^{−1/4}`). Hence the tilt normalisation
   `Z^{−1} ≤ (4/3)e^{8m_c/3}` (the obstacle of LS5's caution R67 M3) is
   harmless (cost `(16/3)βm_c + 2β log(4/3)`): LS4 Thm 4.2, Lemma 5.1, Thm 5.2,
   Cor 5.3 hold for LS5's tilted law, and **no tilt-bias estimate is ever needed** — tilt factors can be
   bounded by 1 pointwise.
2. **Soft-pivotal bound (Prop 2.2; Walsh form Prop 4.2; PROVED).** In LS4's
   pinned coin representation, split Ψ into hard (0/1) factors and the soft
   exponential `e^{−Y*}`. A witness class with top q outside S is charged only
   `w_qΔ_q ≤ w_qN_q/q` (its damping) — except through the 0/1 leak factor
   `λ_q`, which is non-constant only on heavy steps. Prop 2.2 (Leibniz over factors)
   overcounts by Bell numbers when many factors depend on one event; Prop 4.2
   (all soft factors as one exponential, expanded in the Walsh basis of the
   corner cube, XOR covers) removes this. Lemma 3.1 describes pivotality by
   upward chains of varying classes through divergent outside coordinates.
3. **One rough prime, uniform in X (Thm 5.1; PROVED for a fixed fibre).**
   `|σ̂_tilt(θ)|` for `supp θ = {ℓ}` is bounded by `Z^{−1}` times explicit damped
   first moments of class masses through ℓ (and through prime sets, with their
   factors removed). The undamped divergence `Σ_q 1/q` of the LS5 caveat is
   gone; no residue/label information is used. The leak tail decays only like
   `ℓ^{−1/4}`, so the rate is γ < 1/4. Granting first-moment inputs (FM2)
   (a combined damped sum with exponent caps at shared primes — uniform-in-P
   bounds are false; heuristically Shiu in APs + a Titchmarsh-type bound over
   the prime top; *not written*; pointwise divisor bounds provably
   insufficient) and a second moment over the smooth part c, this gives
   (A\*) for frequencies with one rough prime and the all-level cap for large
   sieves whose frequency denominators have ≤ 1 prime factor > z
   (CONDITIONAL).
4. **Reduction (Thm 6.1; PROVED implication).** The all-level 3/4 cap for all
   forced mixtures ⟸ (DCC): a *first-moment* damped covering count on the
   product space of coins and pinned values (no tilt, no conditioning, no
   signs).
5. **Obstruction to the naive residue bound (Prop 6.2; PROVED, asymptotic
   Assessment)** and **the isolated arithmetic statement (RD; CONJECTURE)**.
   Small-height labels (−4, −1, −4d, …) put damped mass ≍ `e^{−2γt_p}/γ`
   (`t_p = log p/log z`) on a single residue at every prime, so no residue-uniform dispersion holds; they must
   be removed by LS4's deterministic residue sets (now valid for the tilt).
   (RD) asks for residue dispersion `≤ (log N)^C Π_{p∈P}p^{−γ₀}` of the damped
   mass of **large-height** labels, with residues mod p and gain p per shared
   prime (with uncapped prime-power gains it is false — review) — a divisors-of-`A²`-in-residue-classes bound
   *on average over the cofactor*; long cofactors are fine, short ones (one
   cofactor per divisor) are the open part (CHN/Lenstra give O(1) per modulus,
   not the needed `p^{−γ₀}` on average).
6. **Route (Assessment, not written):** (FM) + (RD) + small-height removal ⟹
   (DCC). Missing beyond (RD): the overlap combinatorics for supports of
   unbounded size (per-prime losses `2^{O(|S|)}` are affordable only for
   `|S| ≲ log z`), and divergence cascades of the coin coupling (supercritical
   in undamped mass for huge X; harmless for |S| = 1 because everything after
   the first divergence is bounded by a damped tail).

## Evidence

`scripts/largesieve6_softpivotal_toy.py` (seeds 1–5, pool {3,5,7,11,13},
exact enumeration of the tilted law): all of (2.1), Prop 2.2, Prop 4.2 hold
(max exact/bound 0.81, 0.049, 0.073); Lemma 4.1's first inequality checked
pointwise 1.3·10⁶ times.

## Self-review (review tool, deep) and repairs applied

No FATAL against the PROVED core (Lemma 1.1/Cor 1.2, Lemma 2.1/Prop 2.2,
Lemma 3.1, Lemma 4.1/Prop 4.2 incl. the negative-`Y*` correction, Prop 6.2
mechanism). Repaired: prime-power gains at shared primes now capped by the
witness's exponent (Thm 5.1: `ν_{>r}(P; C)`, constant 160; the coin step at
r keeps the `x_r` congruence); (FM2) restated as the combined quantity
(uniform-in-P version false); leak rate `ℓ^{−1/4}` ⇒ γ < 1/4; (DCC) given a
`min`-form so that Thm 5.1 really is its |S| = 1 case; damping consistency
for K → 4K in Thm 6.1; a false Minkowski height bound removed; (RD)
restated with exponent caps; script docstring corrected and the Prop
2.2/4.2 comparisons asserted.

## Points for the hostile reviewer

* Prop 4.2: sign of `L_ℓ` in `Y* = 2Y − ΣL` (fixed during self-review; costs
  `2^{|S|}`), the subcube/base-point maxima, and Lemma 4.1's minimal-cover step.
* Thm 5.1: the conditional-expectation step `E[Y_{>r}|𝓕_{≤r}] ≤ Θ_r` with the
  r-factor dropped; the lcm/shared-prime-set bound (`ν_{>r}(P)`, sum over all
  `P ⊆ primes(G_C)`); the divergence probability `≤ 2U(F^∪∖F^∩) ≤ 4Σ r^{−v}`
  (truncation).
* Fibre filter (R67b D1): Thm 5.1 is per fibre; the passage to "c off an
  exceptional event" needs second moments over c (stated, not proved).
* Labels: everything in §6 beyond Thm 6.1 and Prop 6.2 is Assessment/CONJECTURE.

## Replay

    ulimit -v 8000000
    timeout 1800 env PYTHONPATH=scripts uv run python scripts/largesieve6_softpivotal_toy.py 1 2 3 4 5
