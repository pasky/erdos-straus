# Z59_WALDS — the cusp / Waldspurger residue after TERNARY (CHECKPOINT 1 — work in progress)

Status: z59 lane WALDS (brief `z52bbriefs/z59_lanes.md` §WALDS; common rules `z52bbriefs/z58_lanes.md`, `z53_depth.md`).
Internal; not yet reviewed. **ES is OPEN; nothing here proves or disproves ES, (★), (MS) or (MS⁺).**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z59_walds_*`,
data `data/z59/walds/`.

Notation as in `Z58_TERNARY.md`: g ∈ M_{3/2}(Γ₀(4N), ψ) a ternary-theta proxy g = Σ cᵢθ_{Lᵢ} + h (one quadratic
nebentypus ψ), 𝒞₁(2N) = {n ≥ 1 : n ∈ ℤ_q^{×2} for all q | 2N}; for N with odd prime divisors in {3,5,7}, 𝒞₁(2N) ⊇ 𝔐
(TERNARY Cor F1). Thm F: if g(ℓ²) = 0 for all large primes ℓ then on 𝒞₁ the genus part vanishes and g(p) = h⊥(p).

## 0. MANDATORY FALSIFIER TABLE (checkpoint version; re-stated at the end)

Mechanism examined: a *valid* (g(n) ≠ 0 ⟹ R(n) ≥ 1) half-integral-weight proxy whose 𝔐-coefficients are, after
TERNARY Thm F, pure cusp coefficients; positivity is to come from Waldspurger central values L(½, φ ⊗ ψ̄χ_{−4}χ_p).

| screen | behaviour (checkpoint) |
|---|---|
| F1 odd squares | m² (gcd(m,2N)=1) lies in 𝒞₁ with squarefree part t = 1; Waldspurger's twist at t = 1 is **φ ⊗ ψ̄χ_{−4}** (the *Gaussian* twist, field ℚ(√−1) for ψ = 1 — the same field as the C = 1 norm form 4m²+1 = N(1+2mi) of T1). Theorem W1 (below): T1 forces, for every Shimura eigensystem φ contributing at any 𝒞₁-prime, L(½, φ ⊗ ψ̄χ_{−4}) = 0. Non-squareness is used exactly here. |
| F2 C-even | Theorem W1 is a negative, line-blind statement; it applies verbatim to R₈-support proxies (R₈ also vanishes on squares). No positive claim, so nothing false is proved. |
| F3 composites | the 18 non-square composite R-zeros in 𝔐 (≤ 10¹⁰, last 17 401 609) are all squarefree, so lie in 𝒞₁ with their own twist χ_t; to be screened (§4). |
| F4 known zeros | the 9 in-𝔐 (★)-zero primes 5569 … 8 813 281: to be screened for the T1-admissible ("Gauss-exceptional") eigensystems (§4). |

## 1. Precise statements attacked

(Q1, dictionary) For g as above, valid at prime squares, give the exact formula for g(p), p ∈ 𝒞₁ prime: which φ,
which twist, which nonvanishing would force a (★) hit.
(Q2) Is "L(½, φ ⊗ ψ̄χ_{−4p}) ≠ 0 for all large p in the class" implied by GRH / known / as hard as (MS)?
(Q3) Falsifiers: central values and root numbers at the 9 in-𝔐 zeros, the 18 composite zeros, and at t = 1.

## 2. First lemma (checkpoint): Theorem W1 (statement; proof in §2 of the final memo)

**Theorem W1 (PROVED relative to TERNARY (S1)–(S5), Waldspurger 1981 Prop. 1 and Cor. 2 (read from the primary PDF,
J. Math. Pures Appl. 60, pp. 377, 379), and linear independence of distinct cuspidal eigenvalue systems).**
Let g be as in TERNARY Thm F with g(ℓ²) = 0 for all large primes ℓ. Write h⊥ = Σ_φ h_φ (Waldspurger Prop. 1:
h_φ ∈ S_{3/2}(4N, ψ, φ), φ running over weight-2 newforms of character ψ² = 1). Then h_φ(1) = 0 for every φ, and for
every squarefree t ∈ 𝒞₁(2N): h_φ(t)² · L(½, φ ⊗ ψ̄χ_{−4}) = 0. Hence if g(p) ≠ 0 at a prime p ∈ 𝒞₁(2N), p ∤ N,
some φ with h_φ(p) ≠ 0 has **L(½, φ ⊗ ψ̄χ_{−4}) = 0** ("Gauss-exceptional").

First falsifier (running): enumerate the Gauss-exceptional φ at small levels; if none at the levels of interest, every
T1-valid proxy there vanishes at every squarefree n ∈ 𝒞₁ — the cusp residue is empty, not just unforced.
