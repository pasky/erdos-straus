# DIFF_DEEP — the supersingular / Diff-parity route taken to depth (task O176)

Status: internal research note, SPARK phase. **ES is not solved here, nor any infinite case of it.** Labels as in
DISCOVERIES.md. Builds on KUDLA_ES.md (O172, as repaired by R172: D3 Z(T) ≠ ∅ iff |Diff(T)| = 1; D4 congruences are
sufficient, only the genus shadow is necessary; D5 the Type II index T' = [[f,1],[1,f']] is a *chosen* index; D8 Kudla
data are genus-invariant; D9 coset Schwartz functions see the full ray class, but as the split-plane count).
Memos: BRAINSTORM/bsC_*.md. Scripts `scripts/bsC_*`.

**Question (orchestrator).** Is ES at p equivalent to a statement about (small) endomorphisms of *some* of the ≈ p/12
supersingular curves mod p, with an existence theorem lurking in the geometry of maximal orders of B_{p,∞}?

**Answer in one paragraph.** (§1) The quantifier "some supersingular curve" is vacuous: a configuration of Gram T exists
on some curve iff Diff(T) = {p}, which every certificate index satisfies by genus theory; the "every curve" version is
false *for Type I configurations* (Type I certificates live on ≪ p^{3/5+o(1)} = o(p) curves; Type II / union version
open, Assessment) (R176 repair, D4/D7). (§2) The ray-class condition *can* be moved onto the curve as a
level structure, and then it is free: every maximal order contains, for every M, special endomorphisms x with
nrd(x) ≡ −1 (mod M). Type II becomes exactly a **level-vs-determinant** inequality for a pair of special endomorphisms
(Thm 2.1: `4h | gcd(h, G)²`, h = det/p, G = level); the deterministic lift misses it by a factor ≍ f^{3/2} ≥ M^{3/2} in
the determinant (Prop 2.4) — the scale barrier B3 in geometry-of-numbers form. (§3) Type I has the same shape with
the Eichler orientation. (§4) What a breakthrough would have to prove, stated as a lattice problem in the genus of
maximal orders.

## 1. The supersingular transfer and its exact hypotheses

**Theorem 1.1 (supersingular transfer; PROVED; = bsC_supersingular_transfer Thm 1).** For positive definite
half-integral binary T: there is a supersingular E/𝔽̄_p with trace-zero x, y ∈ End E of Gram T ⟺ B_T ≅ B_{p,∞} ⟺
Diff(T) = {p}. (Every order lies in a maximal order; Deuring.)

**Corollary 1.2.** ES(p) ⟺ the arithmetic set S_p of certificate-shaped indices is non-empty; every T ∈ S_p has
Diff(T) = {p} (KUDLA_ES Thms 1.2(b)/1.4(b)), so the curves add no condition. (PROVED.)

**Proposition 1.3 (∀E is false for Type I; PROVED relative to ET Prop 1.7, f_I(n) ≪ n^{3/5+O(1/log log n)}, and the
divisor bound).** Λ_{d,ab} is an Eichler order of level e;
exactly τ(e) maximal orders contain it; e ≤ (p+1)² + 1. So ≤ 2Στ(e) ≪ p^{3/5+o(1)} = o(p) of the ≈ p/12 curves carry a
Type I certificate (p^{o(1)} would need f_I(p) ≪ p^{o(1)}, which ET call difficult; R176 repair D4). (bsC_supersingular_transfer Prop 3; asymptotic only — numerically f_I(p) ≥ p/12 still holds at p ≈ 10⁴.)

**The hypotheses that make §1 vacuous, and the modification tried for each** (construction log):
* (H1) *the configuration is specified by its Gram matrix* — violated by adding level structure (§2, §3);
* (H2) *the quantifier is "∃ curve"* — "∀ curve" is false (1.3); "a canonical curve" (CM by the least d with
  (−d/p) = −1, or the spine j ∈ 𝔽_p) is QUATERNION_ES Prop 2.2 / the Heegner forms of disc −4p (B2);
* (H3) *Kudla data are genus functions* (R172 D8) — violated only by non-K-invariant Schwartz functions (R172 D9),
  which turn the count into the split-plane coset count (B2);
* (H4) *parity sees quadratic data* — over every base field, for Diff data that are ℚ-rational at ℓ
  (bsC_parity_quadratic_only Prop 1; for F-rational data the local Diff above ℓ can see higher-order characters —
  R176 repair D2); the ray condition is quadratic only for M | 24.

## 2. Type II as a level-versus-determinant condition on a pair of special endomorphisms

Notation: for trace-zero x, y in a maximal order O ⊂ B_{p,∞}, ⟨x,y⟩ := trd(xȳ)/2, T(x,y) its Gram matrix. For an
odd n ≥ 3 and integers f, f' ≥ 1 put `h := (ff' − 1)/n`, `G := gcd(f+1, f'+1)` (the *level* of [[f,1],[1,f']]: the
largest G with `fX² + 2XY + f'Y² ≡ −(X − Y)² (mod G)`).

**Theorem 2.1 (Type II = level vs determinant; PROVED, elementary).** Let n ≥ 3 be odd. Type II tuples (a,b,c,d) of n
with a ≤ b are in bijection with triples (f, f', c), f ≤ f', such that
`n | ff' − 1`, `4c² | h`, `h | c·G`,
via f = 4acd − 1, f' = 4bcd − 1 and, conversely, d = h/(4c²), M := 4cd = h/c, a = (f+1)/M, b = (f'+1)/M. A valid c
exists iff **`4h | gcd(h, G)²`** (take c = h/gcd(h,G)). In particular, for n = p:
**Type II(p) ⟺ some supersingular E/𝔽̄_p has trace-zero x, y ∈ End E with ⟨x,y⟩ = 1 whose Gram determinant
ph = nrd(x)nrd(y) − 1 satisfies 4h | gcd(h, level)².**
*Proof.* (⇒) ff' = 1 + 4c²dn (O131/(I)4), so h = 4c²d = cM, and M | f+1, f'+1, so M | G, i.e. h | cG. (⇐) put d := h/(4c²) ∈ ℤ and M := 4cd = h/c; then h | cG says M | G, so
a = (f+1)/M, b = (f'+1)/M are positive integers; ff' = 1 + nh = 1 + 4c²dn and f ≡ f' ≡ −1 (M), which is (I)4's Type II criterion. Minimal c: h | cG ⟺ (h/g) | c with
g = gcd(h,G); 4c² | h is then weakest at c = h/g, giving 4h²/g² | h ⟺ 4h | g². Geometric form: Thm 1.1 applied to
T = [[f,1],[1,f']], whose Diff is {p} by KUDLA_ES Thm 1.4; conversely p | det T for x, y in a maximal order since
the reduced discriminant of ℤ⟨x,y⟩ is 4·det T (R176 repair D11). ∎
*Check* (`scripts/bsC_level_det.py 300`, 13 s): for every prime and odd square n ≤ 300, brute-force enumeration of
(f, f', c) with ff' up to the largest certificate value reproduces the tuple count exactly (68 values of n, 0
mismatches; 0 solutions at the odd squares, the T1 control).

**Proposition 2.2 (the Gram form; PROVED).** With M = 4cd: `fX² + 2XY + f'Y² = M(aX² + bY²) − (X − Y)²`, so the
binary lattice ℤx + ℤy is "a scaled diagonal lattice minus a square". On E[M] (p ∤ M), x and y act as involutions
(x² = −f ≡ 1), x + y is nilpotent ((x+y)² = −Mce), and k := xy + 1 is trace-zero with k² = −4c²dp (bsC_eichler_
orientation Prop 2). With κ := k/(2c), κ² = −dp, Type II is the commutative identity
(2ad + κ)(2bd + κ) = de(1 + 2cκ) in ℤ[κ] (bsC_typeII_commutative Lemma 1; with k itself the identity is false —
R176 repair D3).

**Proposition 2.3 (the level is free on one endomorphism; PROVED).** Let O be any maximal order of B_{p,∞}, M ≥ 2
with p ∤ M, and x₀ ∈ M₂(ℤ/M) with tr x₀ = 0, x₀² = 1. Then there is x ∈ O⁰ with x ≡ x₀ (mod MO), hence
`nrd(x) ≡ −1 (mod M)`, and with `nrd(x) ≤ M²·ρ(O⁰)²`, ρ the covering radius of O⁰ (in the nrd-norm); ρ(O⁰)² ≪ p
(successive minima λ₁λ₂λ₃ ≍ p² and λ₁λ₂ ≥ p/4 by Kaneko, so λ₃ ≪ p).
*Proof.* O/MO ≅ M₂(ℤ/M); lift x₀ to x' ∈ O; trd(x') ≡ 0 (M); since trd(O) = ℤ pick z ∈ O with trd z = −trd(x')/M and
put x = x' + Mz ∈ O⁰. The coset x + MO⁰ (MO ∩ O⁰ = MO⁰) contains a vector within M·ρ of 0. x² ≡ x₀² = 1 gives
nrd x = −x² ≡ −1. ∎ So the ray condition `f ≡ −1 (mod M)` — the B2 core of Type II — is *deterministically* realised on
every supersingular curve, for every M, at size f ≪ M²p.

**Proposition 2.4 (where the cost goes: the exactness gap; PROVED identity + Assessment).** Fix x ∈ O⁰, nrd x = f.
Every y ∈ O⁰ with ⟨x,y⟩ = 1 is y = x/f + y_⊥ with y_⊥ ⊥ x, and
`det T(x,y) = ff' − 1 = f·nrd(y_⊥)` (PROVED: nrd(y) = 1/f + nrd(y_⊥)).
Imposing y ≡ y₀ (mod M) puts y_⊥ in an affine coset of the rank-2 lattice Λ_x = x^⊥ ∩ MO⁰, det Λ_x ≍ M⁴·p²f up to
constants and an index factor. Theorem 2.1 needs `det T = ph ≤ pG²/4`, i.e. **nrd(y_⊥) ≤ pM²/(4f)** at level G = M. *Assessment
(typical lattices, λ₁ ≍ λ₂):* the coset's smallest vector has nrd ≍ (det Λ_x)^{1/2} ≍ M²p·f^{1/2}/4, so the
deterministic choice misses by the factor
`(M²p f^{1/2}) / (pM²/f) ≍ f^{3/2} ≥ (M − 1)^{3/2}`,
and the probability that a given (O, x) admits a good y is ≍ f^{−3/2}. Summing over the p/12 orders, the ≍ M² involution
classes x₀ and x in the coset (≍ F^{3/2}/(M³p) of them with nrd x ≤ F per order, up to the mass normalisation) gives
Σ_M Σ_{f ≤ F} O(1/(Mf)) ≍ log² F (the congruence f ≡ −1 (M) is already in the coset count; the index factor in
det Λ_x can be ≍ f for special x, shrinking the gap to f^{1/2} — R176 repair D6) — the polylog lottery of ES, reproduced from the
geometric side (B3). The congruence is free; the price is that the second endomorphism must hit a *specific* norm
(a binary representation of one number), which is the shrinking target.

**2.5 A canonical curve (EVIDENCE; `scripts/bsC_canonical_curve.py 20000 4`, 46 s).** Modification of (H2): fix ONE
curve — the one with Ibukiyama's order O(q, r) (q the least prime ≡ 3 (8) with (p/q) = −1; a curve over 𝔽_p, i = Frobenius)
— and search its trace-zero part O⁰ = O ∩ B⁰ (not the Gross lattice; R176 repair D5) for pairs x, y with ⟨x,y⟩ = 1, nrd y ≤ 4p, satisfying Thm 2.1. Every pair found is
a genuine certificate pair (asserted against the divisor criterion). Primes p ≡ 1 (24) < 2·10⁴: the canonical curve
carries a Type II configuration (f' ≤ 4p) for **144 of 267** p; by range of p (5000-blocks): 47/76, 34/67, 30/57,
33/67, while the number of certificate pairs of p with f' ≤ 4p grows (mean 7.9 → 14.1). Reading (Assessment): the
certificates are spread over the ≈ h(−4p)/2 ≍ √p curves of the 𝔽_p-spine (and the d-spines for d > 1), and a fixed curve
gets a ≈ (#certificates)/(#spine curves) share; the hit rate decays slowly, consistent with (H2) failing for a single
canonical curve. No hidden "privileged curve" effect is visible.

## 3. Type I: the same shape, with the Eichler orientation

Λ_{d,m} (m = ab) is an Eichler order of level e (§1.3). By bsC_eichler_orientation Prop 1, **Type I(p) ⟺ there are a
supersingular E, a cyclic C ⊂ E of order e and u, v ∈ End(E, C) with u² = −d, v² = −m, uv + vu = 1, 4dm − 1 = pe, and an
integer a | m with v ≡ a on C** (then (v − a)(v + a) = −ace and v − a factors through E → E/C). The orientation χ(v)
runs over all square roots of −m mod e as C varies, so the geometric datum is free (as in Prop 2.3); the cost is the
*divisor* condition a | m, which — unlike Type II — is **not** a Gram-matrix condition at all: Type II is entirely a
condition on the Gram matrix of a pair (Thm 2.1: entries + level), whereas Type I needs a factorisation of one entry
(m = ab). In the Type II language the factorisation is hidden in G = gcd(f + 1, f' + 1) (M = 4cd | G). (PROVED
dictionary; Assessment on the comparison.) This asymmetry is why Type II is the better test bed.

## 4. What a positive result would have to prove (the open lattice problem)

By Thm 2.1, ES Type II at p is equivalent to the following statement about the genus 𝒢_p of maximal orders of B_{p,∞}:

> **(LD_p)** Some O ∈ 𝒢_p contains trace-zero x, y with ⟨x, y⟩ = 1 such that h := (nrd x · nrd y − 1)/p satisfies
> 4h | gcd(h, G)², G = gcd(nrd x + 1, nrd y + 1).

Known geometry gives, for every O and every M: x with nrd x ≡ −1 (M) (Prop 2.3), and pairs with det T ≥ p (Kaneko,
sharp). (LD_p) asks for **h = g·t with g = gcd(h, G) and 4t | g** at determinant ph. *(R176 repair D1: the size
relaxation "level G ≥ 2√h" is necessary only and vacuous — non-certificate pairs with G ≥ 2√h and Diff = {p} exist for
437/438 primes 5 < p < 3000, reviews/diff-deep-review.md.)* Generic pairs have G = O(1); the deterministic lift
achieves level M only at h ≍ M²f^{3/2} (Prop 2.4, Assessment), a factor ≥ M^{3/2} short. No theorem in the reduction
theory of definite quaternary/ternary lattices that we know produces "high level at low covolume" without a counting
main term (B3), and any such theorem must fail at n = m² (Thm 2.1 holds verbatim for odd n, and has no solutions at odd
squares — T1), so it must use that p is prime through Diff-parity (Thm 1.1 needs |Diff| = 1) — i.e. through the
*existence* of the supersingular genus, which is exactly the part that is free. *Assessment:* (LD_p) is a faithful
geometric restatement of the H-A core (moving modulus M = 4cd, now the level of a lattice pair), not an escape.

## 5. Verdict

* PROVED: supersingular transfer (1.1–1.2); ∀E false for Type I (1.3); Type II ⟺ level-vs-determinant (2.1, checked);
  Gram form and involution structure (2.2); deterministic level lift (2.3); parity over any base is quadratic for
  ℚ-rational Diff data (bsC_parity_quadratic_only Prop 1; the "any mechanism" reading is Assessment, R176 D2);
  Galois-orbit obstruction to valence-formula arguments (bsC_valence_borcherds; relative to Siegel + divisor bound,
  R176 D4); Type II commutative factorisation (bsC_typeII_commutative).
* EVIDENCE: canonical-curve hit rate ≈ 50% and slowly decaying (2.5); quadratic slices (4cd | 24) miss 71/9732 primes
  p ≡ 1 (24) below 10⁶.
* Assessment: the supersingular/Deuring route is genus-vacuous at the level of curves and, once the ray condition is
  put on the curve as a level structure, the obstruction re-appears as an exactness (size) condition with a gap factor
  ≍ f^{3/2} — B3 in geometry-of-numbers form. **No route to ES.** The sharpest new object is (LD_p).
