# LONGSHOT_FIBRED — fibred encodings of Erdős–Straus solutions (task O136, long shot B)

**ES is not solved, here or anywhere. Nothing below proves ES(p) for any new p.**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment, as in DISCOVERIES.md.

Notation. `n ≥ 2`; `Sol(n)` = the finite set of positive solutions `(x,y,z)` of `4/n = 1/x+1/y+1/z`;
`Sol_I(n)`, `Sol_II(n)` the Type I / Type II solutions (ET: Type I = `n | x`, `gcd(n,yz) = 1`; Type II =
`n | y, n | z`, `gcd(n,x) = 1`); `f(n) = #Sol_I(n) + #Sol_II(n)`. ET Prop 1.6: `f(m²) = 0` for odd m.
For a prime p every solution is Type I or II, so `Sol(p) ≠ ∅ ⟺ f(p) > 0`.

## 0. Summary

(written at the end)

## 1. Fibred encodings: definition and the trivial decomposition

**Definition 1.1.** A *fibred encoding at n* is a triple `(E, ht, φ)`: a countable set `E = E(n)`, a height
`ht : E → [0,∞)` with `E(≤H) := {e : ht(e) ≤ H}` finite, and a map `φ : E → Sol(n)` (or into `Sol_I ∪ Sol_II`).
It is *power-fibred* if `#E(≤H) = c(n)H^δ(1+o(1))` as `H → ∞` (n fixed) for some `δ > 0`, `c(n) ≥ 0`.
A *counting route* proves this asymptotic with `c(n)` given by an independent formula and then reads off
`c(n) > 0 ⇒ E ≠ ∅ ⇒ Sol(n) ≠ ∅`.

**Lemma 1.2 (fibre decomposition; PROVED, trivial).** Suppose each fibre `E_s = φ^{−1}(s)` has a limit
`c_s := lim_H #E_s(≤H)/H^δ` (finite, possibly 0). Then `c(n) = Σ_{s∈Sol(n)} c_s`, a finite sum.
*Proof.* `E = ⊔_s E_s` with `#Sol(n) < ∞`; add the limits. ∎

*Reading.* The H-asymptotic is free (n is fixed; no uniformity in n is needed), and the scale constraint
(CONDITIONAL_ES Prop 2.3; RT1 Prop 2.4 / §5.5), which bounds main terms by `μ·f(n)`, is blind to it because
`#E(≤H)` grows like `H^δ`. But the *constant* `c(n)` is still a sum over the finitely many solutions. So the
question is never the H-asymptotic. It is whether some method evaluates `c(n)` without knowing `Sol(n)`.
§§2–3 classify the encodings by how `φ` is computed and show what `c(n)` can be.

**Lemma 1.3 (weighted scale constraint; PROVED, trivial).** In Lemma 1.2 put `w_max(n) = max_s c_s` and let
`μ(n)` be the largest number of "pieces" (orbits, components) of E lying over one solution, each piece of
density `≤ w_max^{piece}`. Then `c(n) ≤ f(n)·max_s c_s ≤ f(n)·μ(n)·w^{piece}_max(n)`. In particular a route
that proves `c(n) ≥ M(n)/2` from a main term `M(n)` needs `M(n)/w_max(n) ≤ 2 f(n)`; by ET (via CONDITIONAL_ES
Prop 2.3 / RT1 §5.5) this is `≤ 2ξ log³n log log n` outside a density-o(1) set of primes (any ξ → ∞),
`≤ 2p^δ'` outside `O(N^{1−δ'} log³N)` primes `p ≤ N`, and `≤ 2p^{3/5+o(1)}` for every p.
*Proof.* Lemma 1.2 and the three bounds on `f(p)` merged in RT1 §5.5. ∎

So a power-fibred encoding escapes the scale constraint *only* if the fibre densities `c_s` vary by a power of
n across solutions, or if the main-term formula for `c(n)` is not of the "count with error term" kind at all.
The rest of this file determines, for each mechanism that produces power fibres, what the densities `c_s` are.
