# AGENT_REPORT_O67 — (CC)/(A*) for residue-dense multi-rough classes (checkpoint 1)

Branch `side-agent/astar-dense`; deliverable `EXCEPTIONAL_LARGESIEVE5.md`
(LS5), script `scripts/largesieve5_cover_toy.py`.

The work was self-reviewed with the review tool (hostile review R67, deep
mode). All of its FATAL and MAJOR items were applied in LS5; they are listed
below.

**Verdict:** (CC)/(A*) is **not proved**. The checkpoint has four sound
structural steps, a corrected picture of what the route must look like, and
toy evidence.

## Proved (R67: sound)

1. **Lemma 1.1: the full family suffices.** Large-sieve caps pass down to
   subfamilies, so (A*) is needed only for the full forced family `𝔊_X`.
   Caveat: smooth fibres filter classes by smooth congruences.
2. **Lemma 1.2: rational labels.** Every forced class (ℛ, (a,D), Case A,
   selector) is `−r/s mod G`. Distinct labels that are congruent mod g have
   `H₁H₂ ≥ g/2`.
3. **Prop 2.1: a tilted fibre law.** Use truncated forbidding and the law
   `σ ∝ Q'·1_𝒜·e^{−2Σw_ℓp̃_ℓ}`. Its damped collision is
   `≤ Z^{−2} ≤ e^{6m_c+1}`. This is LS4's (B) without a global threshold, and
   LS4 Thm 4.2 holds with (A*) for this law.
   * Truncated forbidding (`p̃ = min(p, δ)`) replaces LS4's light/heavy
     cap. That cap is discontinuous, which R67 M4 pointed out.
   * **Retracted:** an earlier claim that LS4 Lemma 5.1 and Thm 5.2 transfer
     verbatim to the tilted law. The pinned representation carries a
     prefactor `Z^{−1}`, and the tilt can bias towards pivotal residues
     (R67 M3).
4. **Lemma 3.1: label partition.** In the product model, `P(E_S)` is at most
   `Π_{ℓ∈S}ℓ^{−1}` times a sum over partitions and *distinct* labels; this
   is an inequality. Same-label coincidences collapse to a single residue
   vector.

## Corrections from R67 (applied)

* **The undamped product model fails uniformly in X (FATAL for that
  model).** Take `D < ℓ` and the primes `q ≡ −ℓ^{−1} (mod 4D)`. These give
  matched classes with total probability `Σ1/q = ∞`, so
  `P(E_{{ℓ}}) → (ℓ−1)/ℓ`.

  In the true law, a witness whose top lies outside S acts only through the
  path after that top, i.e. through the tilt `≤ 2w_q/q` or through further
  coincidences. The correct covering statement must therefore **charge
  outside tops by their damping**. That requires a soft-pivotal lemma, which
  is not written. The 0/1 pivotal method cannot be uniform in X except with
  deterministic residue sets, as in LS4 Lemma 5.1.
* **(LCH) withdrawn.** As stated it is false: the Linnik/`2^t`-divisor
  example shows this, and it also omitted the sum over witness S-parts. The
  target is (4.1) with per-prime slack `ℓ^{1−γ}`, for damped weights.
* **"Long witnesses are harmless" downgraded to Assessment.** Two
  corrections: the label sum is `(log X)²`, not convergent, and the `D ≤ A`
  restriction has been added.

## Remaining diagnosis (Assessment)

Four things are missing:
* **(C2):** cross-label coincidences at S-primes.
* **(C3):** sharing of outside primes between witnesses of different blocks.
* **Short witnesses.** A label of a modulus with a tiny outside cofactor has
  weight up to 1 whatever its height. This defeats sup-over-residue
  arguments, including Lenstra and Coppersmith–Howgrave-Graham–Nagaraj
  divisor-in-class bounds. What is needed is an averaged multi-block sum
  over labels and moduli.
* **The soft-pivotal transfer** from the product model to the tilted fibre
  law.

Cor 4.2 (`|S| ≤ c₀ log log N`, `log X ≤ (log N)^A`) is a SKETCH only.

## Evidence

Exact enumeration on the full ℛ(M) family over 6 primes:
* Lemma 1.2 holds on the toy.
* The per-prime correlation loss of the covering events is ≈ 1.42 at most
  for |S| ≤ 4. R67 reran this and the numbers reproduce. This is toy scale
  only, in the undamped model.

## Decision requested from the parent

Three options:
* **(a)** Write the soft-pivotal lemma for the tilted law. It must handle the
  tilt bias per coordinate and charge outside tops by `w_q/q`. Then attack
  (C2)/(C3) with averaged label sums. This is research level and takes
  several more sessions.
* **(b)** Accept the checkpoint as an obstruction and route analysis, and
  merge LS5 as Assessment plus four small proved lemmas.
* **(c)** Redirect to proving the tilt's per-coordinate bias bound, so that
  LS4 Thm 5.2 is recovered for the tilted law. This is a smaller and
  concrete step.

Replay: `ulimit -v 8000000; timeout 900 env PYTHONPATH=scripts uv run --with numpy python scripts/largesieve5_cover_toy.py` (about 1 minute).
