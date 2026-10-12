# Triage red team A (O156): hostile triage of BRAINSTORM memos a–i

Scope: the 22 files `BRAINSTORM/[a-i]*` (addcomb_… through invol_windmill_signature). None of them was written by
O146 or O154 (checked: memo headers + `git log -- BRAINSTORM`; neither task has a memo or report on this branch), so all
22 are triaged here. Labels as in DISCOVERIES.md. ES is not solved; nothing here proves any case of it.
Spot-check scripts: `scripts/triage_*.py` (named per memo where used).

Format per memo: **verdict-validity** (AGREE / DISAGREE / PARTIAL with the memo's own verdict) · overclaims ·
strongest open sub-question · novelty of by-products · **promise 0–5**.

## Per-memo triage

**addcomb_unit_fraction_density (O142c; memo: COLLAPSES B3).** AGREE. Bloom's Prop 1 forces |S| ≥ N^{1−o(1)} terms and
the circle-method engine needs equidistribution of many q-adic residues per prime power; three terms have none, so the
method has no k = 3 shadow beyond the local "every ℓ-adic pole cancels" rule (§3.2), which is exactly how ET derive the
Type I/II parametrisation. §3.3's "f_II(p) ≍ log³p on average (from memory)" is consistent with ET Thm 1.7
(Σ_{p≤N} f(p) ≍ N log²N up to loglog, over N/log N primes). §3.4 (e-slice condition is purely multiplicative on the
unit part) is correct and one line. No false negative: the method's hypotheses (many terms, density in A) are
simply absent. Open sub-question: none of substance. By-products: known (ET §2). **Promise 0.**

**anal_dirichlet_series (O151a; memo: COLLAPSES B6/T7, 3/4 ceiling, B2/H-E).** AGREE with the verdict, but **one
mis-scoped PROVED item**. Prop A.1 (E finite ⟺ P_E continues along the real axis to s = 0, by Landau) is correct and
tautological. **Prop A.2 is overclaimed:** "D_g − D_f is holomorphic on Re s > 0" needs Σ_{p∈S} f(p)p^{−σ} < ∞ for all
σ > 0, i.e. f(p) ≤ p^{o(1)} on S. That pointwise bound is not known; the best is f(p) ≪ p^{3/5+O(1/loglog p)} (ET; cf.
POINTWISE_MN3 Lemma 5.2 for the m-analogue). As proved, the invisibility holds on Re s > 3/5 (and on Re s > 0 only
conditional on a sub-polynomial pointwise bound, or for S chosen inside {p : f(p) ≤ p^{ε}} — which the counterfactual
cannot guarantee). The conclusion (linear Dirichlet-series data leak exactly as T7) survives with 3/5 in place of 0, since
everything known about D_f lives at Re s ≥ 1 anyway. Open sub-question: none useful for pointwise ES (the memo's own
"continue D_II past 1/2" is an average). Novelty: A.1/A.2 folklore-level. **Promise 0.**

**anal_euler_product_law (O151c; memo: COLLAPSES B1; (E2) spurious).** AGREE. A pointwise law in the Legendre symbols
is a CRT conditional mean (Prop A / Thm F), so it cannot certify any p. The B5 point is right: at m² the zero is the
global Jacobi identity (EXF Prop 2.1), not the limit of an Euler product. The EVIDENCE (β·log p ≈ 6.2 constant over
three decades for f_I, p ≡ 1 (8)) has a heuristic explanation the memo does not spell out, and that explanation makes
the law expected rather than surprising. The Legendre symbols of small q fix the genus sign (−d/p) only for
Y-smooth d. In the log-uniform measure on d ≤ p^{O(1)} (the measure ET's mass lives in), the Y-smooth d carry a
fraction ≈ Σ_{q≤Y} 1/q / log p of the mass. So a relative effect `(A/log p)·Σ χ_p(q)/q` is what the Haar/CEILINGS
model predicts. Hostile note: "relative O(loglog p/log p)" is asymptotic only. At p ≈ 3·10⁶ the fitted β ≈ 0.42
still moves g by ±40 %, so the law explains a lot of variance at accessible p (R² 0.55). Open sub-question: none
pointwise. The memo's averaged CONJECTURE (an asymptotic for Σ_{p≡r(Q)} f(p) with an explicit local factor) is
plausibly provable by ET-style averaging but irrelevant to ES. Novelty: the numerics are plausibly new; the
mechanism is the standard Haar heuristic. **Promise 1.**

**anal_moments_structured (O151b; memo: COLLAPSES B3/B6, B1/B4, B2).** AGREE. Checked by hand:
* the row II{a,d} lift. A divisor f ≡ −1 (mod 4ad) of p + 4a²d gives c = (f+1)/4ad, e = (p+4a²d)/f and b = ce − a > 0
  (because (f+1)(p+4a²d) > 4a²d·f), with 4abd = p + e. So the "sterile ⇒ structured" direction is valid.
* Prop B.1. Exponent 2 of (ℤ/4ad)^× for 4ad | 24 means every element of the subgroup H is a squarefree-divisor
  residue.
* The B5 remark. Every prime factor of m² + 4 is ≡ 1 (mod 4).
* Remark B.2 (the extension to 4ad ∤ 24 fails) is correct and useful.

The 10-condition sieve bound N/(log N)^{1+κ′} is weaker than known results, as the memo says. The Chebyshev
arithmetic (Var/μ² ≈ 1/log p ⇒ E(N) ≪ π(N)/log N) is right. False-negative check: one could add the Type I
exponent-2 slices to Prop B.1's nine Type II slices, or use all slices with q_θ | 24·k for a fixed k. Either way the
set stays finite (Thm 2.2(iii) / B4), so the verdict stands. The fixed-p "lottery is driven by τ₃ of a few shifts
(p+e)/4" is EVIDENCE at accessible p and is exactly H-A. Open sub-question: the CONJECTURE var(log f(p)) → 0
(f(p) ~ μ(p) for almost all p). It is averaged and a plausible Turán–Kubilius-style exercise, but it gives nothing
pointwise. Novelty: Prop B.1 is folklore (Mordell/Yamamoto-era "p + 4 has a prime factor ≡ 3 (4) ⇒ ES"). The
variance-law numerics are plausibly new. **Promise 1.**

**apollonian_reciprocity (O144b; memo: COLLAPSES as a route / PARTIAL as structure).** AGREE. Prop B.2 is a correct
reading of BL Cor 2.7: Br U_n/Br ℚ ≅ ℤ/2 over ℚ, so no quartic BM obstruction exists over ℚ. Prop B.1 (the BM set
stays non-empty after imposing the Type I or the Type II p-adic shape) I checked only at the level of the invariant
bookkeeping. The Type II computation `inv_p = ((1 − 4/X)/p)`, with 1 − 4/X ranging over all residues ≠ 0, 1, is
right. The decisive false-negative question is whether an HKRS-type *non-BM* (thin-orbit) invariant could hide in ES.
The memo answers it correctly in two independent ways:
* (i) at fixed n the integral points off the lines are finite (BL Lemma 3.10), so there is no infinite orbit to carry
  an invariant;
* (ii) every HKRS family {u·m^d}, d ≥ 2, contains at most one prime.

What the memo understates: (ii) also kills the analogy as a *disproof* heuristic for primes. HKRS obstructions are
multiplicative-shape sets, and primes avoid them trivially. The census "odd Type I/II zeros ≤ 2·10⁷ = odd squares ∪
{105}", with 105 a convention artefact, is a nice T1 sanity check of the counting code. The quartic-symbol split
is EVIDENCE with a proper congruence control. Open sub-question: none for ES. Novelty: Prop B.1/B.2 are low-novelty
readings of BL. The quartic test is new but expected-null. **Promise 1.**

**canonical_invariants (O153 W1; memo: COLLAPSES, B3 for unit size and B2 for representation seeds).** AGREE, with
one untested sub-branch.
* Lemma A (x ≤ 3n/4, y ≤ 2nx, z ≤ nxy ⇒ z ≤ 9n⁴/8): re-derived; folklore.
* Prop B (the archimedean use of ε_p is confined to the power-sparse set {log ε_p ≪ log p}): correct, and the
  cleanest B3 instance in the batch.
* Prop C (a Cornacchia seed carries √−d mod p plus a Hecke angle): correct.

Hostile point: the experiment (§4) tests only the *representation* seeds (e | u, e | v for p = u² + v²). The unit
**residues** (ε_p mod q), which the memo itself classifies as non-abelian Frobenius data in ℚ(√p, ζ_m, ε_p^{1/m}),
are dismissed by Assessment only ("can enter only by choosing θ", H-D). That is the right *logical* placement. A
seed can at best steer θ; it cannot decide a fibre. Still, the cheap empirical test was not run: condition the e-slice
success on ε_p mod e (or on ε_p being an m-th power residue mod small q). Prior: null, by the same CM-torus logic as
EXF Thm 5.2 (but EXF covers dihedral data of ℚ(√−d), not unit residues of ℚ(√p)). Open sub-question: that unit-residue
test. Even a positive bias would only be a better θ-ordering (H-A), not a proof. Novelty: Lemma A and Prop C are
folklore. The power-sparsity count is a Hooley-heuristic replication. **Promise 1.**

**cayley_markoff_cm (O143 memo 1; memo: PARTIAL / COLLAPSES to B2 at fixed (K, β)).** AGREE. Spot-checked
(`scripts/triage_cayley.py`, sympy):
* the P2 identity X²+Y²+Z²−XYZ−4 = −64e₃/e₁³;
* X²−4 = −16(y₀+y₁)(y₂+y₃)/e₁².

By hand, (u₁+u₂)(4u₃−n) = n·u₃(u₁+u₂)²/(u₁u₂) ≡ n·u₁u₂u₃ mod squares. This gives D ≡ d for Type I and D ≡ dn for
Type II, as claimed. False-negative check on P5: the Markoff moves act *across* n, so the only way they could prove
ES(p) is a descent ("every p is reached from some smaller n by a move"). Orbits contain ≪ (log N)² points below N,
against ≍ N log³N solutions, so almost all points are orbit-singletons below N and no descent exists. The memo states
this (B1/T6), and the verdict is right. P3 (U_n has no Vieta involution: there are no square terms, and the line
through the node at infinity keeps one affine point) is correct and is the key structural reason. Open sub-question:
the Assessment-level orbit count in P5 (comparing height to norm on a rank-2 subgroup of T_K¹(ℚ)) is unproved but
unimportant. Novelty: P1/P2 are classical (Cayley cubic = SU(2) character variety). P4, the CM parametrisation
recovering ET's −4d / −4dp levels as the CM field of the character point, is a neat dictionary and plausibly new
as a formulation, but it is only a relabelling (it is valid at odd squares too). **Promise 1.**
