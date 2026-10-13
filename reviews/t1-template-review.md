# R183 — hostile review of O183 `T1_TEMPLATE.md` (T1-bearing ES variants provable at primes)

Reviewer: R183 side agent. Documents: T1_TEMPLATE.md (merged from side-agent/t1-template), BRAINSTORM/bsJ_mute_place_unit_orbit.md,
reviews/agent-reports/AGENT_REPORT_O183.md. From-scratch scripts: `scripts/review_t1t_*.py` (own ℤ[φ] / ℤ[∛2] / ℤ[√d]
arithmetic, own tame and 2-adic Hilbert symbols; none of the author's `t1t_*` code is used).

Status: in progress.

## Summary verdicts

(filled in claim by claim below)

## Claim-by-claim

### C1. Definition of V_φ (§1) — SOUND
`4/n = 1/x + 1/y + 1/z`, x, y, z ∈ ℤ[φ], σ₁(x), σ₁(y), σ₁(z) > 0, σ₂-signs not all equal, n odd positive integer.
Normalisation is unambiguous (σ₁(φ) = 1.618…, σ₂(φ) = −0.618…, N(φ) = −1). Under α(u) = (−u₁/u₃, −u₂/u₃) the
conditions pin inv_{σ₁} = ½ and inv_{σ₂} = 0 (Thm 2.1(a), re-derived in C5). The "Anchor/partner bookkeeping"
paragraph is labelled Assessment and is in fact proved later (Cor 2.2). Only remark: the definition is for n ∈ ℤ;
Thm 1.3(a) and Cor 2.2 also speak of n = m² with m ∈ O — see defect m1.

### C2. Lemma 1.1 (Cl_{4∞₁} ≅ ℤ/2, χ = χ_{−φ}) — SOUND
Re-derived. h(ℚ(√5)) = 1, so Cl_{4∞₁} = ((O/4)^* × {±1}_{σ₁}) / image(O^*). From scratch
(`scripts/review_t1t_zphi.py`, check L11): |(O/4)^*| = 12, φ has order 6 mod 4, φ³ ≡ 1 + 2φ, the image of
±φ^j has order 12, (−1, +) ∉ image; so |Cl_{4∞₁}| = 2 with non-trivial class (−1, +). Character: for a unit u in
an unramified 2-adic field, (u, w)_2 = 0 for all w ∈ U^{(2)} = 1 + 4O_2 (K_2(√w)/K_2 unramified, u a norm), so the
conductor of K(√−φ)/K divides 4·∞₁ (σ₁(−φ) < 0, σ₂(−φ) > 0, −φ a unit) and the character is non-trivial, hence
equals the unique non-trivial character of Cl_{4∞₁}. Numerically: on every degree-one prime 𝔮 met in the Prop 1.2
run (split ℓ and 𝔮 = (√5)), "𝔮 has a generator ≡ −1 (mod 4) with σ₁ > 0" (computed by explicit normalisation over
±φ^j, j < 6) ⟺ (−φ/𝔮) = −1 (computed through the residue map φ ↦ r) — all instances agree (counts in C3).
Note χ((√5)) = (−3/5)... = (2/5) = −1 (φ ≡ 3 mod √5): the ramified prime is always in the non-trivial class.

### C3. Proposition 1.2 (explicit unit Type II solutions) — SOUND-AFTER-REPAIRS (proof gap at σ₂, claim true)
Algebra re-derived: e ≡ −n (mod 4), x + η = e(g+1)/4, 4/n − 1/x = e/(nx) = 1/y + 1/z; σ₁-positivity; x prime to
n (a prime 𝔭 | (x, n) divides 4x − n = e | a_k ≡ 4η (mod n)); n | y, n | z. All correct.
**Gap (defect M1):** the σ₂ step says "sgn z = −sgn x · sgn y, so the three signs are not all equal". This is a
non-sequitur: sgn x = sgn y = −1 gives sgn z = −1, i.e. all three negative — which V_φ forbids. The claim is
nevertheless true: σ₂(x) < 0 means σ₂(e) < −n and σ₂(y) < 0 means σ₂(g) < −1, whence σ₂(a_k) = σ₂(e)σ₂(g) > n;
but σ₂(a_k) = n + 4σ₂(η) < n since σ₂(η) = σ₂(φ)^{2k+1} < 0. So (−, −) is impossible and the conclusion holds.
Numerics (from scratch, exact ℤ[φ] arithmetic with exact sign tests of P + Q√5): see C3-numerics below.

## Defects
