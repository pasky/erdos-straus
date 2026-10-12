# Brainstorm O141(a): ES in weak arithmetic — Shepherdson's model and open induction

Status: the main theorem (Thm S) is PROVED (elementary). Nothing here proves any case of ES. Verdict at the end:
**PARTIAL**. We get a clean non-provability theorem, IOpen ⊬ ES, and an exact description of ES inside
Shepherdson's model. The obstruction is the "formal point 1" (Theorem M) together with an archimedean sign
argument. It is not a new route to ES.

## 1. Idea

ES is Π⁰₁. Put `ES(n) :≡ ∃x,y,z ≥ 1 : 4xyz = n(xy+yz+zx)`. Any solution with x ≤ y ≤ z satisfies
x ≤ 3n/4, y ≤ 2nx and z ≤ nxy, so z ≤ 2n⁴. Hence ES(n) is equivalent, over very weak theories, to a
Δ₀ formula with a polynomial bound. Two formalisations matter:
* `ES_all :≡ ∀n ≥ 2 ES(n)`;
* `ES_prime :≡ ∀p (p irreducible ∧ p ≥ 2 → ES(p))`.

In N they are equivalent by descent: a solution for d | n scales to one for n.

Question: which weak theories prove ES? A non-provability result needs an explicit model with a
counterexample. Open induction IOpen (discretely ordered ring with induction for quantifier-free formulas)
is the natural first target. By Shepherdson's criterion, its models are exactly the discretely ordered rings
that are integer parts of their real closure.

**Shepherdson's model** `M` (Shepherdson 1964) consists of the Puiseux polynomials
`n = n₀ + Σ_{0<q} a_q t^q`. Here q ranges over finitely many positive rationals, the coefficients a_q are
real algebraic, and n₀ ∈ Z. The element t is positive and infinite, so n > 0 iff its leading coefficient is
positive. Every n ∈ M is a polynomial in s = t^{1/k} for some k, so it defines a real function on
[0,∞). Write `n₀ = n(0)` (the "standard part" at 0; the map n ↦ n₀ is a ring homomorphism M → Z). For
every standard m, divisibility by m in M depends only on n₀.

### Theorem S (PROVED). Let n ∈ M, n ≥ 2.
1. If n has a zero ρ ∈ [0,∞) (as a function of real t), then M ⊨ ES(n).
2. If n has no zero in [0,∞), then n₀ ≥ 1, and M ⊨ ES(n) ⟺ N ⊨ ES(n₀).
   In particular `n = 1 + t` (more generally any n with n₀ = 1 and no zero in [0,∞)) has **no** solution in M.

*Proof of 1.*
* If n₀ = 0, take x = y = z = 3n/4 ∈ M; its constant term is 0.
* Otherwise let ρ > 0 and s₀ = ρ^{1/k}. Then s₀ is real algebraic, and m := s/s₀ − 1 ∈ M. In R_alg[s] we
  have n = m·q, and q has positive leading coefficient because m and n do.
* Put x = y = n·s/(2s₀) and z = q·s/(4s₀). All three lie in M (constant term 0) and are positive.
  Moreover 2/x + 1/z = (4s₀/s)(1+m)/n = 4/n. (Checked symbolically: `scripts/bs_logic_shepherdson.py` (i).)

*Proof of 2, (⇐).* If 4/n₀ = 1/a + 1/b + 1/c in positive integers, then x = an/n₀, y = bn/n₀, z = cn/n₀
lie in M (constant terms a, b, c) and solve 4/n. (Script, (ii).)

*Proof of 2, (⇒): the sign lemma.*
* Let X, Y, Z ∈ M be positive with 4XYZ = n(XY+YZ+ZX). View all four as polynomials in one s = t^{1/k}
  over the real closed field R_alg. Then 1/X + 1/Y + 1/Z = φ := 4/n as rational functions, and φ is
  analytic on [0,∞) because n has no zero there.
* Suppose XYZ has a zero in [0,∞), and let ρ be the largest one. Let S be the set of W ∈ {X,Y,Z} with
  W(ρ) = 0; it is nonempty. Write W = c_W·u^{k_W}(1+O(u)), where u = s − ρ, and let K = max k_W.
* The coefficient of u^{−K} in Σ1/W equals Σ_{k_W = K} 1/c_W, and it must vanish because φ has no pole at
  ρ. So at least two of the c_W with k_W = K have opposite signs.
* Hence some W ∈ {X,Y,Z} is negative on (ρ, ρ+ε). But X, Y, Z have no zero on (ρ,∞), so their signs there
  equal their signs at +∞, which are positive. This is a contradiction.
* So X, Y, Z have no zero on [0,∞), and they are positive there by the IVT over a real closed field. Then
  X(0), Y(0), Z(0) are positive integers. Evaluating at s = 0 (n(0) = n₀ ≠ 0) gives 4/n₀ = Σ 1/W(0). ∎

### Corollaries (PROVED unless labelled).
* **C1.** IOpen ⊬ ES_all. Indeed M ⊨ IOpen, 1+t ≥ 2, and 4/1 is not a sum of three positive unit fractions.
  The same witness defeats every formulation that restricts n by standard congruences. For example,
  ES restricted to n ≡ 1 (mod 840) fails at 1 + 840t.
* **C2.** Every nonstandard element of M is a product of two nonstandard elements. Hence M has no
  nonstandard irreducibles (Shepherdson's original observation; reproved by factoring over R_alg after
  refining s and rescaling constant terms to 1 and n₀). Therefore M ⊨ ES_prime iff ES_prime holds in N.
  * *Hence, if ES is true, IOpen + ES_prime ⊬ ES_all.* Descent through prime factors is genuinely
    unavailable in IOpen; IΔ₀ proves that every n ≥ 2 has an irreducible divisor, and so recovers the
    equivalence.
* **C3 (signed ES holds everywhere in M).** Drop positivity. For n₀ ≡ 1 (mod 4), take x = y = n(1−n)/2
  and z = (n−1)/4. For the other n₀, use the standard positive identities, which are valid in M because
  divisibility by 2 and 4 depends only on n₀. So inside M **positivity is the only obstruction**; it is the
  model-theoretic face of the "signed collisions are free" remark in LONGSHOT_PIGEONHOLE.
* **C4 (Puiseux layers are ES-conservative).** The proof works over any real closed coefficient field K.
  Here M₀ ⊨ IOpen is an integer part of K, and M₀ + tK[t^{Q>0}] is built with t > K. For n with no
  zero in K_{≥0}, it gives ES(n) ⟺ M₀ ⊨ ES(n₀). Adding an infinite Puiseux layer creates counterexamples
  only at elements whose "standard part" is a unit ±1 (n₀ = −1 cannot occur under 2, but it appears in
  signed variants).

## 2. Literature anchor

* J. C. Shepherdson, "A non-standard model for a free variable fragment of number theory", Bull. Acad.
  Polon. Sci. 12 (1964). It gives the model M, the IP criterion, no infinite primes, and √2 "rational".
  From memory; standard; consistent with the abstracts below.
* Wilkie (Logic Colloquium '77): a discretely ordered ring extends to a model of IOpen iff it maps onto
  every Z/nZ. Verified as quoted on MathOverflow q/23796.
* M. Otero, "On Diophantine equations solvable in models of open induction", JSL 55 (1990) 779–786.
  It shows that every model of IOpen embeds into one where x₁²+…+x₄² = a is solvable; JSTOR abstract
  verified. That paper is about *existence* in extensions; ours is *nonexistence* in a fixed model.
* Berarducci–Otero, "A recursive nonstandard model of normal open induction", JSL 61 (1996). Its
  abstract confirms that Shepherdson's model is not normal and has no infinite primes.
* S. Mohsenipour, "A recursive nonstandard model for open induction with GCD property and cofinal
  primes", Logic in Tehran (LNL 26). Title and author verified; contents not read.
* Macintyre–Marker, "Primes and their residue rings in models of open induction", APAL 43 (1989).
  Title verified; contents not read.
* S. T. Smith, "Fermat's last theorem and Bezout's theorem in GCD domains", JPAA (1992). Its snippet
  says that some FLT cases are provable in IOpen + GCD; contents not read.
* We found no prior statement about Erdős–Straus in weak arithmetic. Searches were brief; novelty is
  modest in any case, since the technique is standard.

## 3. Barrier screen

* **B1 / Theorem M.** Thm S is a *realisation* of B1 rather than an escape from it. The element 1+t is
  ≡ 1 modulo every standard m, i.e. its profinite image is the rational point 1, and Theorem M already
  says congruence data cannot exclude ES failing there (cf. Cor 17.3.1, "from the rational point 1").
  The new ingredient is the archimedean sign lemma: positivity at ∞ propagates down to the standard part
  unless n has a real zero.
* **B5 (odd squares).** In M, every n₀ ≥ 2 is handled by scaling from ES(n₀) ∈ N, odd squares
  included. So Shepherdson-type models can only produce counterexamples at *unit* standard parts. They
  never see the square-class difficulty, because their residue map lands in Z, not in Ẑ \ Z.
  * Realising a square-mimicking profinite point (DEPTH3 q*) as the residue of an element needs a model
    whose map to Ẑ has non-integral image *and* in which Type I/II stay empty. Thm S shows that Puiseux
    layers over such an M₀ simply reduce to M₀ (C4). So this is no easier than building M₀ itself.
* **B2, B3, B4, B6.** Not applicable. No counting is involved, and the result is exact at each n.
* **What this says about provability.** Any proof of ES must use more than IOpen. At minimum it needs
  either the existence of prime/irreducible divisors (a Δ₀-LNP consequence), which kills the fake-1
  witness, or an argument specific to primes. That is a weak, expected constraint. It does *not* bear
  on the hard core (primes p ≡ 1 (24) in square classes).

## 4. Experiment

`scripts/bs_logic_shepherdson.py` checks identities (i)–(iii) of the proofs and the signed solution of C3
at n = 1 + s⁴ = (s²+√2s+1)(s²−√2s+1); for the signed solution X has leading coefficient −1/2. All pass.

## 5. Viability Assessment: **PARTIAL**

* By-product theorem (PROVED, elementary): Thm S and corollaries C1–C4. In particular IOpen ⊬ ES_all,
  and, if ES is true, IOpen + ES_prime ⊬ ES_all.
* Natural next question: is IOpen ⊬ ES_prime? This needs a model of IOpen with a nonstandard prime
  p ≡ 1 (mod all m) and no zero in [0,∞) (in some function-ring sense), so that the sign lemma applies.
  Candidates are Mohsenipour's GCD model with cofinal primes and the Biljakovic–Kotchetov–Kuhlmann
  truncation IPs (where some elements are prime). If such a p exists in a "Puiseux-like" model, the
  sign lemma should give IOpen + GCD ⊬ ES_prime.
  * This is a logic result only. It cannot inform the analytic hard core, because every such
    counterexample sits over the standard unit 1, where ES fails trivially.
* No route to ES: the angle collapses to Theorem M at the point 1 (B1) for every model of this shape.
