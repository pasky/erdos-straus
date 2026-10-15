# z11_lines_branching — why exponent-covering trees diverge: ℓ-lines through square points (O235)

**Idea.** Replace the global-period lifting (z8_adaptive) by a per-branch tree on Ẑ (z11_tree.c; node = μ mod L, split one
prime digit at a time, leaves = one class with L_M | L). Measure falls fast (k = 105: 3·10⁻¹¹ at depth 14, vs O232's
8.5·10⁻⁸) but stuck nodes multiply ×12–164 per two levels (R244 repair D9; Assessment from one greedy heuristic, D10; measures in double precision, D8) — also for k = 297, which has a single square point and no mixed points.
**Mechanism.** Stuck nodes sit near the ℓ-line X_{x,ℓ} = {μ_ℓ′ = x for ℓ′ ≠ ℓ}: pure (square) at every q with ℓ ∤ ord_q(4),
generic at the others — the exponential analogue of the r-generic lines of (J)26/(J)54, but with infinitely many generic
primes. The lines themselves are covered (z11_line.py: 3-line of 297 fully covered, by classes with v₃(L_M) ≤ 2 (CERTIFIED, R244 replay — D7)), but only by classes
whose periods contain large new primes ℓ′; splitting on ℓ′ leaves the on-line child pure (survives) plus ℓ′ − 1 off-line
2-D lines. Convergence needs fibre coverage ≥ 1 − 1/ℓ′, which the q ≤ 10⁶ supply does not give.
**Barrier screen.** B1 over Ẑ: the qualitative obstruction is not known to persist (no *integer* unit squares unless c₀ + k ∈ 4^ℤ; non-integer points of Λ ∩ Sq^× open — R244 repair D2); the quantitative one looks like a branching process.
**Assessment.** EVIDENCE + diagnosis. Sharp question: is there a (J)26-type measure argument on ℓ-lines? Heuristically no
(Σ τ²/q over q with ℓ | ord diverges), so expect huge but finite coverings (CONJECTURE E, weak).
