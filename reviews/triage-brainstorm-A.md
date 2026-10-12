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

**ff_erdos_straus (O140a; memo: PARTIAL, no route; collapses to B2/B3 at fixed P).** AGREE with the verdict; the
by-products are correct as far as checked.
* Lemma 1.1: the t^{−d₁} coefficient is the number m ∈ {1,2,3} of minimal-degree monic denominators, nonzero in
  char ≥ 5, and must equal lc(A/P) = 1.
* Prop 1.2(ii): 4 ∉ {1,2,3} mod char ≥ 5.
* Thm 2.1 counting, re-derived. Case 1 is X, then a, b | X, then κ | a+b, and P = AX − E. Case 2 has E | AXa₁ + b,
  which is nonzero since both terms are monic of different degree. This gives ≤ 2D(2n)³q^{n−k} against ≍ q^n/n
  irreducibles.

Thm 2.1 is the cleanest "B3 in its sharpest form" statement in the batch: the fixed-P solution variety has expected
dimension −k. One mis-statement in the B3 screen: "the q → ∞ regime is the only place with pointwise function-field
technology" is too strong. Fixed q with n → ∞ has Sawin–Shusterman-type étale-cohomology results (Chowla/twin
primes over F_q[t] for fixed large q). The verdict still holds there, by B3 rather than by Thm 2.1. At a single P the
H-A family has q^{cn} members with main term poly(n), so square-root (Deligne) savings, ≈ q^{cn/2}, dwarf the main
term. Those results are averages over P anyway (B6).

False-negative check: in F_q[t] the T1 square obstruction is absent (§3.2), and Prop 4.1 kills only *linear*
families. So a function-field ES_q(t) *theorem* via char-p-specific identities (additive/Frobenius polynomials,
P ↦ P^q) is not excluded. That is a genuinely open FF question. By construction it cannot transfer to ℤ, where odd
squares are sterile, so it has no value for ES. Open sub-question (FF-only): does ES_q(t, P) hold for all P of degree
≥ 5 at q = 5, and is there a Frobenius-identity proof? Novelty: Thm 2.1, Prop 4.1 and the degree-parity explanation
of the missing T1 obstruction are plausibly new, elementary and inert for ES. **Promise 1** for ES (2 as a
standalone function-field curiosity).

**gon_fermat_certificates (O148a; memo: COLLAPSES to B2 at "F ≡ t (M) ⇒ F = t").** AGREE, and this is the most
instructive memo in the half.
* Re-derived Lemma 3.1 (Type II): (4acd−1)(4bcd−1) = 4cd(4abcd − a − b) + 1 = 4c²dp + 1.
* Re-derived the three-linear-forms remark: XYZ = n²(X+Y+Z+2n) (3·11·75 = 25·99 at n = 5).

The memo correctly notes that Fermat-type GoN certificates pass B1 (a modular square root is not a Theorem-M
operation) and B3 (exact existence with main term ≍ 1). They die at B2 because every ES slice is a level set of a
*split* rational form, and on split forms the GoN step needs a known divisor of N_θ(p). False-negative check on
the *higher-dimensional* encodings, which the memo screens only for the three anisotropic candidates:
* The natural ternary object is the isotropic form Q(e,f,a) = ef − 4da² representing p, with f ≡ −1 (mod 4ad).
* GoN/representation theory gives representations of p freely. The obstruction is the **congruence modulo a
  coordinate** (the modulus 4ad moves with the unknown a). No convex body or lattice encodes "f ≡ −1 (mod 4ad)"
  with a varying.
* Fixing a makes it B2. Keeping a free gives a union over a of lattices, i.e. H-A.
* Type I cannot even start Fermat-style: level d needs (−d/p) = −1, so there is no √−d mod p to build Λ from.

So the verdict is right, with the precise obstacle "modulus depends on the unknown" (the same object as redteam-2
E2/(I)1 Q_d). Hostile notes:
* The B5 line relies on "Lemma CT" without a file pointer. Check that its scope (p ≡ 1 (24)?) matches "every ES
  denominator prime to p".
* The Theorem C extension to quadratic input P(q) = F(w₀+qw₁) is honestly marked unproved.

Open sub-question (the best in the gon cluster): is there *any* lattice/body formulation in which the ES modulus is
fixed while the unknown varies? For instance, a lattice in (a, f, e, k) with f = −1 + 4adk, linearised by fixing the
product ad = m and summing over the factorisations of m. That is H-A in lattice clothing, but it is the one place
where Minkowski-type exactness (main term ≍ 1, no error term) might combine with aggregation. Novelty: Lemma 3.1 is
folklore. The "Fermat certificates escape B1/B3 but not B2" screen is a useful, plausibly new piece of barrier
bookkeeping. **Promise 2.**

**gon_incidence_kloosterman (O148c; memo: all five sub-ideas COLLAPSE).** AGREE. Re-derived the compact forms.
* Type I ⟺ (4abd−1) | p(a+b). Since 4abd − 1 > a + b, primality of p forces p | 4abd − 1.
* Type II ⟺ r = (−p mod 4ab) divides a+b. Here e ≤ a+b < 4ab pins e = r.

These are correct and folklore-level. (c1) is the key sub-idea, and the memo's diagnosis is exactly right. The Weil
step controls the *fixed* modulus p and is idle. All the content is the moving-modulus event e | a+b, with
expectation O(1) per dyadic box (EVIDENCE at p = 20161: ≈ 0.03 witnesses per box; 685/694 boxes with ≥ 100
hyperbola points are empty). False-negative check: one could hope for a box shape adapted to the genus/e-structure,
e.g. restricting to (a,b) with a + b ≡ 0 mod small e, so that boxes become "rich". That is the e-slice
reformulation again (a fixed finite e-set is Thm 2.2(iii)). Growing e-sets is H-A. (c3)'s BGK screen is right:
D = divisors of N is not a subgroup and |D| ≤ p^{o(1)}. (c5) (Σ_e(N) = H_e when orders are small; only e = 3 for
squarefree N) is correct and classical in effect. Open sub-question: none beyond H-A. Novelty: folklore-level
reformulations; the box census is new EVIDENCE that a box-wise certificate cannot exist. **Promise 1.**

**gon_lll_relation_lattice (O148b; memo: (b1) COLLAPSES, (b2) PARTIAL as a reformulation).** AGREE, with one
**mild overclaim**. (b1) is right: Coppersmith/Lenstra/CHN give "root ⇒ root of h" and multiplicity *upper* bounds,
and a short vector exists in every such lattice, odd squares included. The (b2) split of an e-slice into a membership
half (−1 ∈ H_e) and a box half (coset of the relation lattice L_e meets ∏[−v_i, v_i]) is an exact, useful restatement
of PIGEONHOLE Lemma 1.1. (i) (membership fails at odd squares) is correct.

Overclaim: "the genus/matroid half of ES is a theorem" (stated as PROVED) needs, for every large prime p ≡ 1 (4), a
prime q ≡ 3 (mod 4) with (q/p) = −1 and q ≤ (p+4)/3. The memo itself flags the needed Linnik/Burgess-type input as
"from memory, not checked". This is almost certainly true unconditionally: the condition is a union of index-4
classes mod 4p, and least-prime-in-a-non-residue-class results (Linnik–Vinogradov / Pollack-type bounds ≪ p^{1/4+ε})
suffice. But it is a citation gap, so the label should be CONDITIONAL-on-citation, not PROVED. It is also
content-free for ES: the membership half is a single congruence condition and was never the obstacle.

The box half (ℓ^∞ inhomogeneous minimum; Kannan–Lovász useless since λ_i ≥ 1) is correctly reduced to B4
(deterministic covering needs many prime factors) or B2 (probabilistic). The EVIDENCE table (membership stable at
≈ 50 %, box success decaying like τ(N²)/|H_e|) is consistent. Open sub-question: the Rogers/Ajtai mean-value idea for
the covering radius of L_e is H-A in lattice language. Novelty: a repackaging of PIGEONHOLE Lemmas 1.1/1.2; the
two-half decomposition is a nice expository by-product. **Promise 1.**

**graph_cayley_moves (O150a; memo: COLLAPSES to B1 (M1–M3) and B2 (M4)).** AGREE. Thm A.1 was checked independently
(`scripts/triage_chord.py`). It draws 2·10⁵ random pairs of real points of Ω, with arbitrary special index and
arbitrary projective sign, and computes the third chord point from the quadratic σ₃(P + tQ) = c₁t + c₂t². All
2·10⁵ third points have type (2,2); none is in Ω. That is stronger than the memo's integral test, since the special
indices are mixed. The arc-parity proof sketch is plausible; I did not re-run the 16-case enumeration.

False-negative check on Cor A.3: projection from a fixed seed P₀ is the birational (Geiser-type) involution
σ_{P₀} of 𝒞. Cor A.3 is therefore just "positive points of N = p ↔ their σ_{P₀}-images". The abundance of signed
points is irrelevant: the conditions (integrality, level 4, N = p) transport through σ_{P₀} unchanged. Correctly B2,
a bijective restatement. M2 (bounded ET translations) → B1 is right; Mordell's square classes make that part
unconditional. Open sub-question: the tangent case of A.1 (EVIDENCE only). It is inert for ES. Novelty: A.1/A.2 (no
real line meets the (1,3) sign locus of Σ1/X_i = 0 three times) is elementary and plausibly new. It explains why
Mordell–Weil-style dynamics has no positivity mechanism, but it has no ES leverage. **Promise 0.**

**greedy_algorithm_dynamics (O150b; memo: COLLAPSES to B1 and, for growing J, to the window frame = B2).** AGREE.
Prop B.1 was re-derived by hand for all three algorithms. For greedy: x = (p+3)/4 is odd and ≡ 1 (3), the remainder
is 3/(px), y = (px+2)/3 is odd, and the remainder 2/(pxy) has odd denominator. Engel leaves 3/p, 2/p, 1/p. Golomb
leaves 2/b″ with b″ odd. Prop B.2 (J(p) = (a_min−3)/4, offset greedy = window statistic) is a correct dictionary.
False-negative check: Remark B.3 states the dichotomy correctly. Fixed pruning is Thm M; growing pruning is the
e-slice/window lottery, i.e. a growing parameter set Θ(p) of H-A type. An "algorithm" is just a witness procedure,
and Thm C / Thm 2.2(iii) cover exactly the bounded-Θ ones. Open sub-question: X_win(C) (J(p) ≪ log p), already a
named campaign conjecture. Novelty: folklore (B.1) plus a dictionary (B.2). **Promise 0.**

**hardness_law (O153 W2; memo: PARTIAL as an EVIDENCE law / COLLAPSES as a route).** AGREE on the route. Both
Siegel-world horns are screened correctly.
* D unrelated to p: χ_D is orthogonal to the residues of the prime factors of N_θ(p) against p.
* D = p (or −4p): the easy regime, since few small residues means large r.
* The GRH horn is (I)2.

**Cross-memo inconsistency to flag (hostile):**
* *Exponent.* This memo fits r ∝ L₅₀(p)^{−0.37} on p ≡ 1 (24), 10⁶–2·10⁷, and extrapolates a structural cost of at most
  L^{0.37} = (log log p)^{O(1)}. anal_euler_product_law fits the same exponent *decaying like 1/log p*
  (β·log p ≈ 4.5 for f_II; at log p ≈ 15.5 that predicts β ≈ 0.29, consistent with 0.37 given the different class
  mod 24 vs mod 8). The fixed-exponent extrapolation is therefore pessimistic; the true structural cost is likely a
  relative O(log log p/log p). The conclusion "the danger is not χ_p" only gets stronger.
* *Dispersion.* This memo finds the residual after one-hot moduli ≤ 97 only ≈ 2× Poisson in variance
  (0.148² / 0.106²). anal_moments_structured finds 9–23× overdispersion after a coarser local fit, and attributes much
  of it to τ₃ of shifts (p+e)/4.

These are reconcilable, and the reconciliation matters. τ₃((p+e)/4) is heavily driven by the *small* prime factors
of p + e, which are congruence data mod small q. The rich one-hot fit therefore absorbs most of the "shift" effect.
The honest summary across both memos: at accessible p, log f ≈ (congruence data at moduli ≤ 100) + (near-Poisson
noise, ≈ 2× overdispersed). The non-congruence remainder is small.

Open sub-question: the memo's own suggested follow-up (residual vs Poisson after moduli ≤ 10³, at 10⁸, f_I too). It is
cheap and gives a falsifiable "f = congruence factor × Poisson" form of the ET heuristic, but it is EVIDENCE only.
Novelty: the numerics are plausibly new; the reading is the standard Haar + Poisson heuristic. **Promise 1.**

**ident_form_families (O145b; memo: PARTIAL, COLLAPSES at coverage).** AGREE on the verdict. The by-products check
out.
* Prop 3.4's factorisation, by hand: (t²+2m²+k)² − 4m²t² = t⁴ + 2kt² + (k+2m²)² = P² + 4m²(m²+k).
* The headline example, by script (`scripts/triage_tfamily.py`): p = 27830² + 21 = 774508921 is prime and
  ≡ 361 (mod 840), a Mordell-hard class. Both f = t² ∓ 2t + 23 give genuine solutions of 4/p via the (c,d) = (1,22)
  Type I slice (exact Fraction check).
* So non-congruence polynomial families do solve Mordell-hard primes, outside Thm C's proved scope (linear
  parameter).

The verdict "density 0, no route" is right for one-variable families: ≪ x^{1/2} primes. The **false-negative risk sits
in the two-variable question**, which the memo leaves UNCLEAR and which is the same gap canonical_invariants leaves
UNCLEAR ("polynomial (u,v)-recipe … UNCLEAR as a theorem"):
* Could a Type I identity in (u,v) solve every prime p = u² + kv² in some (u,v)-classes? That would be a
  positive-density, non-congruence certificate.
* Thm C does not apply as proved. Computing (u,v) from p needs a modular square root, which is the
  gon_fermat_certificates escape from Theorem M.
* The natural obstruction is the *Pythagorean specialisation*. Principal forms represent squares Q(u,v) = m², and
  an identity holding in ℚ(u,v) specialises there. To contradict ET Prop 1.6 one must show that the Type I
  coprimality/shape survives specialisation at a Zariski-dense set of square values.
* The memo proves "no 2-variable extension" only for the constant-level shape.
* A second, cheaper route: the Lemma 3.1(a) trap fails for one-variable t² + k (t − √−k is never ≡ a unit), but
  in two variables (u,v) ≡ (1,0) profinitely makes u + v√−k ≡ 1. So a Thm C-style trap plausibly exists for
  *every* k. This needs checking for non-homogeneous procedure values h(u,v).

**Strongest open sub-question:** prove "no two-variable Type I identity on a binary quadratic form covers a set of
primes containing a hard class", either by the Pythagorean specialisation or by the two-variable trap. A proof
extends the barrier to Fermat + identity certificates; a counterexample would be a major positive find. Novelty:
* Prop 3.2 (Type II families on positive-definite quadratics are old) and the classification in Prop 3.4: plausibly
  new, elementary.
* The k = 21/37 hard-prime families: plausibly new curiosities.
* Lemma 3.1(a) (Thm C extends to t² + 1 under H): a genuine small extension of the barrier.

**Promise 2** (bounded, well-posed obstruction question; good for a short depth task).

**ident_invariants (O145a; memo: COLLAPSES to B2, and B1 for h(−4p)).** AGREE. This memo overlaps heavily with
canonical_invariants; the two should be read together. Lemma 3.1 re-derived: f+1 = 4cdk gives 2k(2cdk−1) = cp,
then c | 2k, then j(2cdk−1) = p, so p = 4dk² − 1 ≡ 3 (4). Scope caveat: it shows only that the *diagonal* f = f' of
ff' − 4c²dp = 1 is empty for p ≡ 1 (4). "Units of ℚ(√p) never give Type II solutions" is true only for that
dictionary (unit = diagonal point). Units entering a non-diagonal point via another order are not excluded. The memo
does say "any unit-based rule must use … other slices — B2", so this is wording, not substance.

The class-number signal decaying 8.5 → 2.5 as the QR pattern enters the baseline is a good falsification design. It
supports "h(−4p) = Euler product of congruence data". The E3 bits (2 quartic, 2/3 cubic) are null, with the quartic
bit's sign flipping between independent samples. That matches the apollonian_reciprocity quartic test (an
independent null). False-negative check: the Chebotarev-independence Assessment for E3 bits is the right heuristic,
and H-D remains "choose θ, not decide a fibre". Open sub-question: none new. The unit-*residue* test missing from
canonical_invariants is also absent here: the regulator enters only through log ε/√p (size), not through ε mod q.
Novelty: Lemma 3.1 is folklore-level; the null regressions are new EVIDENCE. **Promise 0.**
