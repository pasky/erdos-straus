# bsH_kth_power_law — the k-th power law of ES_q Type II moduli; Kummer CM data are ordinary at P (O181)

**ES is not solved here.** Labels as in DISCOVERIES.md. Deep version: DRINFELD_ES.md §1. Script `scripts/bsH_kpower_law.py`.

## Idea
Over F_q[T] with k | q − 1, μ_k ⊂ F_q, so k-th power reciprocity lives on the base ring (over ℚ cubic reciprocity
needs ℤ[ζ₃]). Push FUNCTIONFIELD_ES Prop 4.1 (quadratic sign law) to order k and ask whether the degree-k CM datum
f^{1/k} of a Type II modulus f is "supersingular" at P (embeds in D_{P,∞}^{(k)}), the order-k analogue of KUDLA's
Diff = {p}.
## Literature
Rosen, *Number Theory in Function Fields* (2002), Ch. 3 (k-th power reciprocity; R181 repair D12: theorem number not checked); Gekeler, *On finite
Drinfeld modules*, J. Algebra 141 (1991) (supersingular rank-k modules, End⁰ = D_{P,∞}); embedding criterion for
maximal subfields: Pierce, *Associative Algebras*, §13 and §18 (from memory; R181 repair D12: section numbers unchecked, criterion
itself standard, e.g. Reiner, *Maximal Orders*, §32).
## Statement (PROVED)
(P/f)_k = ε_k^{(1+deg f)(1+deg Ad)−1}, ε_k = (−1)^{(q−1)/k}; for odd k this is 1, so (f/P)_k = 1: P splits
completely in F(f^{1/k}), which therefore never embeds in a degree-k division algebra ramified at P.
## Barrier screen
B5/T1: the k-analogue of T1 is *reversed* (k-th powers satisfy the law automatically and are enriched ×≈k).
B2: a constraint on certificates, not an existence statement. Thm 9.1 / Prop 10.3: n/a (no counts / classes).
## Cheap numerics (EVIDENCE)
q = 7, 13, A = T, T², n = 3, 4: 4 042 Type II data, 0 mismatches; (f/P)₃ = 1 on all; control uniform. Cubes Q³:
mean N_II 7.0 vs 2.15 at primes (q = 7), 3.2 vs 1.12 (q = 13).
## Assessment
PROVED structural negative: the order-k "Diff = {P}" never happens for ES_q. Promise 1. The reason (target −1 is
2-torsion) is isolated in bsH_bl_order_q1 / bsH_twisted_targets.
