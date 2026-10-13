# bsD_metaplectic_cubic — Weil indices (μ₈) and Kubota's cubic metaplectic theta: does the "cubic Siegel–Weil" world see the ray class? (O177)

**ES is not solved here.** Labels as in DISCOVERIES.md. No script.

## Idea
Kudla's Diff lives on the metaplectic **double** cover: incoherence = product of local Weil-representation signs.
Two ways the coefficient group might be larger than ±1: (1) the Weil index γ_v(V) takes values in μ₈, not ±1;
(2) Kubota's n-fold metaplectic covers of GL₂ over K ⊇ μ_n carry theta functions (Kubota, Patterson) whose Fourier
coefficients are n-th order Gauss sums, i.e. n-th power residue symbols — a "degree-n theta" that could, in principle,
see an order-n ray condition.

## Literature
Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111 (1964) (Weil index); Rao, *On some explicit
formulas in the theory of Weil representation*, Pacific J. Math. 157 (1993) (explicit γ_ℓ); Kubota, *On automorphic
functions and the reciprocity law in a number field* (Kinokuniya, 1969); Patterson, *A cubic analogue of the theta
series*, J. reine angew. Math. 296 (1977); Heath-Brown–Patterson, *The distribution of Kummer sums at prime
arguments*, J. reine angew. Math. 310 (1979); Kazhdan–Patterson, *Metaplectic forms*, Publ. IHÉS 59 (1984)
(exceptional representations; no Howe duality for n ≥ 3 in the classical sense). All from memory; page-level
details unverified in this session.

## Analysis
**Prop 1 (the μ₈ of the Weil index adds no order ≥ 3 information about ℓ; CONDITIONAL on the explicit formula as recalled — R177 repair).** For
odd ℓ and a non-degenerate quadratic space V over ℚ_ℓ, γ_ℓ(V) is a product of ε_ℓ^{k} (ε_ℓ = 1 if ℓ ≡ 1 (4), i if
ℓ ≡ 3 (4)), Legendre symbols of unit parts of det V, and the Hasse invariant (Rao, Thm A.4-type formula). As a
function of the rational prime ℓ (V fixed rational data), ℓ ↦ ε_ℓ is a function of ℓ mod 4, i.e. of the quadratic
character (−1/ℓ). So the parity mechanism of bsC_parity_quadratic_only Prop 1 extends verbatim to Weil indices:
**μ₈-valued incoherence still sees ℓ only through quadratic characters** (ℓ = 2 is a fixed place).
**Prop 2 (cubic theta sees only Dirichlet data of f; CONDITIONAL on the recalled form of Patterson's coefficients — R177 repair).** Patterson's cubic theta function
on the cubic cover of GL₂/ℚ(ζ₃) has coefficients τ(m) built from cubic Gauss sums g(m), which depend on m through
cubic residue symbols (·/m)₃. For the ES divisor f (rational, prime to 3q) and π | q (q ≡ 1 mod 3), cubic
reciprocity gives (π/f)₃ = (f/π)₃ = a cubic Dirichlet character of f mod q. So any cubic-theta weighting of
certificates by symbols "π modulo f" collapses to the class of f mod q — information the ray condition already
names (tautology, as in bsD_eichler_degree_k Prop 1). The *genuinely* non-abelian information in cubic Gauss sums
(the argument of g(f), equidistributed by Heath-Brown–Patterson) is unrelated to the class of f and is averaged
information (B6).

## Barrier screen
* **Hypotheses → escapes.** (i) Weil-index escape fails (Prop 1). (ii) Cubic covers: there is no Siegel–Weil formula
  identifying a cubic theta integral with a cubic Eisenstein series *for a dual pair attached to the ES quadric* —
  the n-fold covers (n ≥ 3) of Sp/SL₂ have no dual-pair theta correspondence with orthogonal groups (Kazhdan–Patterson
  exceptional representations are not Weil representations), so ES's quadratic Gram data cannot be fed in.
* **B1** (Prop 2: tautological Dirichlet data); **B6** (Heath-Brown–Patterson is an average over primes);
  **T1** passes (no forcing claimed).

## Assessment
Negative (CONDITIONAL reductions, Prop 1–2 — R177 repair; the "no dual-pair theta correspondence for n ≥ 3" bullet
should read "no Siegel–Weil identity ingesting a quadratic Gram matrix is known"; literature statements from memory). The "cubic Siegel–Weil" world exists
(Kubota–Patterson) but its coefficients see the ES divisor only through the Dirichlet character mod q (by cubic
reciprocity) or through averaged Gauss-sum arguments; and it cannot ingest ES's quadratic Gram data. Promise 0–1.
