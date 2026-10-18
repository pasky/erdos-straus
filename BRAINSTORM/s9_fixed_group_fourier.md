# s9_fixed_group_fourier — second moments over the characters of a fixed group are phase-blind (O271, mandatory (iii))

## Idea
Look for a family attached to ONE p over which a second-moment / Paley–Zygmund argument is deterministic: orthogonality over
the characters of a fixed group G — (ℤ/p)^* on the board's F4 tube (4abd ≡ a + b (mod p), p < 4abd < 2p), (ℤ/t)^* at one level
(Thm K), (ℤ/4uB)^* at one pair (O268).

## Literature
Board memo 2026-10-18, finalist F4 (fixed-modulus tube + characters mod p; "B3 unchanged" — fable's dissent); CONDITIONAL_ES
Prop 2.3 (scale constraint); PARITY_AUDIT ((J)87; |E(p)| ≪ p^{2/5+o(1)}, the p^{1/2}-type loss).

## Statement (SYNTHESIS_SPARKS9 Lemma 3.1; PROVED, elementary)
For n : G → ℝ_{≥0} with S = Σ n, Q = Σ n², the Cauchy–Schwarz/Parseval certificate for n(g₀) > 0 succeeds iff
S² > (|G| − 1)Q; it is independent of g₀ and forces supp n = G. So it can never certify a single class unless every class is
occupied. At one prime the (★) objects number ≍ (log p)² while |G| ∈ {p − 1, φ(t), φ(4uB)} is much larger in every useful slicing.

## Barrier screen
B3 in its sharpest form: the ℓ² size of the non-principal Fourier mass is fixed by Parseval (diagonal ≥ (|G| − 1)S); only the
phases of individual n̂(ψ) could help (H-B parity breaking). T1: irrelevant (the lemma fails before any sign enters). B6: this is
the fixed-p half of "variance at fixed p"; the over-p half is s9_janson_dependency.

## Cheap numerics
None needed (an identity). Equivalent form: with m̄ = S/|G| and V = |G|⁻¹Σ(n(g) − m̄)², the certificate holds iff
m̄² > (|G| − 1)·V. On the F4 tube at one prime (|G| = p − 1, ≍ p log²p tube points, so m̄ ≍ log²p) Poisson-size fluctuations
V ≈ m̄ would require m̄ > p − 2: fails by a factor ≍ p/log²p. Same at one level (G = (ℤ/t)^*, S = τ(tp + 1)) and at one pair.

## Assessment
PROVED steering lemma: deterministic second moments over a fixed group cannot certify ES at one prime; this is exactly why the
board's F4 stays an audit. No route.
