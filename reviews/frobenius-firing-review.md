# R196 — independent hostile review of FROBENIUS_FIRING.md (O196)

Reviewer: R196 side agent (branch side-agent/review-frobenius), independent of the author's self-review (the "R196 #k"
markers already in the file are the author's own deep-self-review repairs, not this review).
Document reviewed: FROBENIUS_FIRING.md at merge of side-agent/frobenius-firing.
From-scratch scripts: `scripts/review_frob_*.py` (own integer factorisation/primality, own F_q arithmetic; nothing
imported from `ff_frob_*` or `fm_poly`).

(Review in progress — sections are filled in one claim at a time.)

## Summary verdicts

* **Thm 4.2 (ES^{(y)} for every odd n > 1; Type II shape at every non-square; exact-T1): SOUND** (PROVED relative to
  UNIT_ORBIT Lemma 2.2, as labelled). Re-derived independently:
  - *Class choice.* M = 4·rad(n)·s₁…s₄ with a ≡ 3 (4), a ≡ −1 (s_i), a mod rad(n) as in UNIT_ORBIT Thm 2.4(a)
    (a ≢ 0, 1 mod ℓ | n, Jacobi (a/n) = −1 via ℓ₀ ≥ 5). CRT-compatible (s_i ∤ n odd, −1 ≡ 3 mod 4 consistent), and
    every hypothesis of Lemma 2.2 holds: gcd(a, M) = 1, a ≡ 3 (4), a ≢ 1 mod each odd ℓ | M (for ℓ = s_i: −1 ≢ 1
    since s_i odd). Lemma 2.2's sieve sifts only ℓ ∤ M; the s_i never divide (r − 1)/2 (r ≡ −1 mod s_i), so nothing
    changes in the sieve.
  - *Reciprocity.* (r − 1)/2 odd ⇒ (s/r) = (r/s)(−1)^{(s−1)/2} = (−1/s)(−1)^{(s−1)/2} = ((−1)^{(s−1)/2})² = 1.
    So Γ_r ⊆ (F_r^*)², which has odd order (r − 1)/2; a proper subgroup has index with an odd prime factor
    dividing (r − 1)/2, hence ≥ x^{1/4−ε}; |Γ_r| ≤ x^{3/4+ε}; Lemma 2.3 (k = 4) gives ≪ x^{(3/4+ε)·5/4} = o(x/log²x)
    for ε < 1/20 (15/16 + 5ε/4 < 1). Since Γ_r = (F_r^*)² has odd order, Q ↦ Q² is a bijection of it, so −n/4 = Q²
    with Q ∈ ⟨S⟩ (non-negative exponents, finite group). r ≠ s_i, r ∤ n automatic.
  - *Solution.* Prop 2.1: z = n·x·((r+1)/4)/Q² has denominator dividing Q², even s-adic valuation when negative
    (re-derived: 4rx = n(r+1) + 4Q², σ = v_s(r+1) < 2c ⇒ v_s(x) = σ, v_s(z) = 2σ − 2c); s_i odd and s_i | r + 1 ⇒
    s_i | (r + 1)/4 | y; s_i ∤ 2n. Type II shape at every ℓ | n inherited from Prop 2.1. n ≡ 3 (4): Q = 1, z ∈ ℤ.
  - *(b)* An ES^{(y)} solution is an ES^{(S′)} solution, S′ := {ℓ : v_ℓ(z) < 0} (odd, prime to n, even
    valuations); Lemma 1.1/Cor 1.2 of UNIT_ORBIT need exactly these hypotheses (x, y ∈ ℤ, z ∈ ℤ[1/S′], parity).
    The statement correctly says "Type I/II shape at *every* prime of m" (consistent with UNIT_ORBIT's R186 m2 repair).
  - *(c)* n = t^{2^j}, t not a square, k = n/t; primes of den(kz) = primes of den(z) (they are prime to n ⊇ primes
    of k), parity unchanged, ℓ | y ⇒ ℓ | ky. S must be chosen prime to n (= prime to t, same radical) — it is.
  - Not trivial: (b) shows ES^{(y)} has the same exact T1 as ES^{(S)}, so no Type-I/II polynomial covering can prove
    it (UNIT_ORBIT Rem (4) transfers), i.e. the sieve is genuinely needed.
  - Numerics (own code): see Checks. Only label/wording issues (m1, m2 below).

* **Cor 4.3 (shot family: ES^{(y)} ⇔ rad(Q) | (r+1)/4; ES ⇔ Q | (r+1)/4): SOUND** as a statement about the
  Prop 2.1 solution. Re-derived: v_s(z) < 0 ⇔ σ < c (for c ≤ σ < 2c, v_s(z) = 2σ − 2c ≥ 0 — the author's proof
  states this correctly); ES^{(y)} at s then needs s | y = n(r+1)/4 ⇔ σ ≥ 1 (s ∤ n). So ES^{(y)} ⇔ ∀ s | Q:
  (σ ≥ c or σ ≥ 1) ⇔ σ ≥ 1 ⇔ rad(Q) | r + 1 ⇔ rad(Q) | (r+1)/4 (rad(Q) odd). ES ⇔ ∀ s | Q: σ ≥ c ⇔ Q | (r+1)/4.
  Brute-force test (own code, S = {3,5,7,11}, 1568 random shots incl. 38 ES^{(y)}-but-not-ES and 72 ES cases):
  0 mismatches of either equivalence, and every shot is an ES^{(S)} solution. The interpretive tail ("exactly the
  B2 obstruction", Kummer–Chebotarev reading) is Assessment, not part of what is proved (m2).

## Defects

## Checks performed
