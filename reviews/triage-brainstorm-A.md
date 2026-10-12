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

**covering_distortion_dual (O150c; memo: COLLAPSES B1/B6).** AGREE. The dictionary is accurate:
* Hough minimum modulus ↔ W(p);
* BBMST uncovered density ↔ δ*(T);
* Gale–Stewart/König ↔ TYPEI2 Thm A.

Non-coverability by identity classes is unconditional via the odd-square classes (Mordell/Schinzel/Yamamoto), as
(c1) says. False-negative check: the only conditional ingredient in the barrier family is Hypothesis H in Thm C /
Thm 2.2(iii), and it concerns factorisation-shape steps. Covering technology is Haar-measure-only and parity-blind,
so (c2) correctly sends that to the WINDOW/WINDOW2 parity line rather than to covering systems. The observation
that BBMST Thm 3.1 fails on the raw system (removed mass = 1 at 2, 3, 5, 7) is right and trivial. Open sub-question:
(c4), distortion inside the quarantined fibre to remove the (log𝓛)^5 in log 1/δ*(T). It is Haar-side only (it would
settle POINTWISE_HAAR Conj 3.1 up to constants), so it is irrelevant to pointwise ES. Novelty: the dictionary is
an exposition; nothing new. **Promise 0** for ES (1 for a Haar-side tidy-up).

**elliptic_fibration_es (O143 memo 3; memo: COLLAPSES to integrality-vs-rationality and B2).** AGREE.
* P1 (N = 4s/n = (Σu)(Σ1/u), so the pencil does not depend on n) is right.
* The fibre bookkeeping is consistent: deg_N Δ = 6 gives an I₆ at ∞, Euler numbers 2+3+1+6 = 12, and Shioda–Tate
  gives MW rank 8 − 8 = 0.
* So ES points are never specialisations of sections over the N-line.
* False-negative check: base changes N = N(t) with positive generic rank give sections. Their integral
  specialisations are parametric families in which n is a function of t: polynomial-value families (density 0,
  cf. ident_form_families) or congruence identities (Thm M). B1 applies either way.

The Lang-scale point (ES points have ĥ ≪ log p while the conductor is p^{O(1)}) is Assessment but robust. Rank,
Heegner or GZ technology produces points of height ≈ a power of the conductor, never existence of a small point,
which is the same scale mismatch as B3. Minor correction: the per-point "non-torsion" in P3 is fully PROVED for
each tested point. By Mazur, a torsion point has order ≤ 12, so the chord–tangent check up to order 12 settles it.
The memo's worry about ℤ/12 and ℤ/2×ℤ/6 concerns only a general proof for all p ≡ 1 (4). Open sub-question:
none for ES. "ES points ↔ rank-jump fibres" is a curiosity. Novelty: C_N is classical (Bremner–Guy–Nowakowski,
cited from memory); the fibre table is probably known; the ES reading is plausibly new but inert. **Promise 1.**

**farey_chain_frieze (O144; memo: PARTIAL as a reformulation, COLLAPSES to B2 as a route).** AGREE. Lemma C.0 was
re-derived by hand: k₁q₃ + q₀ = k₁k₂q₂ − (q₀+q₂) + q₀ = (k₁k₂−1)q₂. Prop C.1 is then nearly tautological. Any
triple (dq₀q₁, dq₁q₂, dq₂q₃) with the two divisibilities sums to (1/d)·span. The Type I/II chain assignments check
out. The "unscaled chain ⟺ g square" classification (EVIDENCE, p < 1500) and the L² mass heuristic for the unscaled
sub-family are plausible. False-negative check: the frieze/Farey geometry is n-agnostic, and the only arithmetic is
the span divisibility, which is the slice divisor event. Correctly B2. Open sub-question: the weak CONJECTURE that
unscaled chains miss infinitely many primes. It is a sub-family failure, uninteresting. Novelty: a repackaging of
ET's SL₂ matrices; probably folklore in frieze language. **Promise 0.**

**farey_ford_cf (O144a; memo: COLLAPSES B2/B1).** AGREE. Lemma A.1 restates ET Prop 2.2 (bound N b = pe + 1 ≤ 2pb + 1
⇒ N ≤ 2p + 1/b, consistent with the memo's N ≤ 2p + 2). B1 holds because, at fixed N, e₀ ≡ −p⁻¹ (mod N) is
congruence data. The B5 line (the failing step at m² is the divisor event, never CF input) and the Zaremba screen
(Zaremba controls the size of partial quotients, the divisor event does not see sizes, and bounded type *thins* the
family by p^{2δ_A−2}) are correct. False-negative check: one could ask whether a *thin-semigroup* orbit (BK/Huang
technology) could be designed so that the divisor event is built into the semigroup. The generators would have to
depend on p through e ≡ −p⁻¹ (mod N), so the orbit is a moving family and the BK circle method (fixed semigroup,
almost-all q) has no pointwise version. Open sub-question: none. Novelty: low (restatement); the
"Ford-circle-of-denominator-p misses {5, 17, 41, 241}" census is a curiosity. **Promise 0.**
