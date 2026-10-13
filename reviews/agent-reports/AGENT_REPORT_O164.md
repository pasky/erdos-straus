# AGENT REPORT O164 — windmills beyond finite menus (checkpoint 1)

Branch `side-agent/windmill-reduction`. Main file `WINDMILL_REDUCTION.md`; scripts `scripts/wr_*`.
**ES is not solved; no positive claim about ES is made.** No candidate mechanism survived, so there is nothing to
triple-check at 10⁶. All negative findings are labelled EVIDENCE/Assessment.

## Results

1. **§1 Dictionary: Zagier's windmill is the dihedral symmetry of Conway rivers.** CERTIFIED for all primes
   p ≡ 1 (4), p ≤ 1300 (`wr_zagier_river.py`). The rotation ζσ on X(p) has exactly h⁺(p) cycles, one per narrow class,
   of length (river period)/2. ζ and σ swap C ↔ C⁻¹ and reflect the principal cycle, which has odd length. Hence each
   has exactly one fixed point on that cycle: the principal form for ζ, and p = b² + 4a² for σ. This is Smith/Legendre in
   topograph language (folklore; no novelty claimed). It isolates three ingredients: (W1) a rotation whose cycles are
   classes; (W2) a class-inverting involution; (W3) an anchor that makes one ambiguous cycle odd.
2. **§2 Class-group form of Type II (PROVED; explicit formula checked on 4360 instances).** ES(p) holds if some form
   `[k, B, c]` of discriminant −4gp has `4g | B`, `B | k+1` (Lemma 2.4). This is the (I)4 Heegner dictionary made
   explicit as a non-genus condition on (class, represented value, root). The slice g = 1 alone fails for 15 of the 267
   primes p ≡ 1 (24) below 20000 (exhaustive). Self-check correction: at odd squares, non-coprime ES-forms exist (1539 for
   m < 80); coprime ones do not, which is what T1 says.
3. **§3 Legendre/SQUFOF midpoints (EVIDENCE, negative).** The forced second ambiguous form of the principal cycle of
   √N is tested for N = tp+1 and N = (p+e)/4. It is an ES certificate at roughly (any-rate)/(number of factor pairs):
   2.2% against 14.6%, and 1.7% against 7.4%. So there is no forcing and no bias.
4. **§4 Type I σ-symmetric river (EVIDENCE, negative).** The river of `[c,p,−cd]` (discriminant p²+4c²d) holds 33% of all
   factor pairs but only 24% of the ES ones. No enrichment.
5. **§5 Structural items (PROVED algebra plus Assessment).**
   - 5.1: positive ES lives on definite (CM) discriminants −4gp, and the p ↦ −p version is signed ES, which is
     indefinite and easy. Definite discriminants have no rivers, so (W1) is unavailable on the Heegner side. A Zagier-type
     windmill would have to live on an indefinite auxiliary discriminant and carry its fixed points over to CM data, the
     way σ does in Zagier.
   - 5.2: an X-slice certificate is exactly the face p next to an ambiguous edge `[−t, A−B, p]` of discriminant T²−4.
     So it is a reflection fixed point, but on a discriminant that depends on the certificate (B2 in reflection language).
   - 5.3: X-slice ES is equivalent to a small-product point of the modular hyperbola AB ≡ 1 (p). Involutions that are
     algebraic over 𝔽_p see only square-root data, while the ES condition depends on the sizes of the lifts.

## Honest assessment
No finite set with a reduction-type involution whose fixed points are ES certificates was found. Every forced
ambiguous object I tested (principal midpoints, σ-symmetric classes) behaves like a random divisor. The clearest
structural reason is 5.1 together with 5.2. Reflection fixed points on a fixed discriminant are genus or two-squares data
of that discriminant, while ES certificates need a discriminant (T, or g together with a residue modulus) chosen per
solution.

## Sparks (not pursued)
- **Indefinite-to-definite transport.** Look for an indefinite discriminant Δ(p) whose σ-type fixed edges `[a,b,−a]`
  (Δ = b²+4a²) map to coprime ES-forms of discriminant −4gp. This is the Zagier pattern (W1 to W3) with CM output.
  Search Δ = p·k² + (small) and 4p+1-type shifts by computer.
- **Mixing 𝔽_p-involutions with lift sizes** on the modular hyperbola (5.3), in the style of Gauss's lemma or
  Zolotarev. Zolotarev's lemma turns the Legendre symbol into the sign of a permutation of [1,p). A permutation parity
  whose fixed points are small-product points would be an H-B-type parity-breaker.
- **Ambiguous rivers of discriminant T²−4 with T running through a p-dependent progression** (5.2): a growing family in
  which the factorisation of T²−4 is known, (T−2)(T+2). Joint factorisation is free here, which might be an H-A foothold.
- **q-indexed (Euclid-type) menus on X(p):** Lemma 4.1 needs finitely many pieces. A uniform infinite menu whose
  non-symmetry pieces foliate the space (piece q acts only on its own leaf {P∘g_q = P}) is the one shape that escapes,
  and it has not been searched.

---
# Checkpoint 2 (sparks A–D)

**ES is not solved. No candidate mechanism was found, so there is nothing to triple-check.** New sections: WINDMILL_REDUCTION §6–§9.

- **(B) Parity, §6 (EVIDENCE, negative).** `|E(p)|` (X-slice certificates) is odd for 211 and even for 174 of the 385 primes
  p ≡ 1 (24) below 30000. Its parity is not determined by p mod 16, 5 or 7, by h(−4p) mod 16, by the two-squares
  coordinates, or by the quartic character of 2. Among 283 congruence-defined sub-counts (≤ 2 literals) **none is constantly
  odd**. The constantly even ones all come from the swap on the locus `4|A, 4|B`. So a Zolotarev-type identity would have to
  weight elements by size/lift data. I did not find such a weight.
- **(A) Transport, §7 (PROVED algebra plus EVIDENCE).** Atkin–Lehner reflections σ_k of rivers have as fixed points exactly
  `Δ = b² + 4ka²`, i.e. CM points of `x² + 4ky²`. Type I's `p² + 4dc²` *is* such a fixed edge. Its ES content is a second,
  ambiguous fixed point, and §4 found that point not enriched for ES. The diagonal Type II transport `p = k² − 4gb²`,
  `k ≡ −1 (4gb)` (p a face of the disc-16g principal river, g growing) misses 2093 of 2212 primes below 2·10⁵. As T1 control,
  no odd square below 2·10⁵ has a coprime diagonal certificate. Assessment: reflections supply the CM half of a certificate,
  never the residue-class divisor half.
- **(C) §8 (PROVED algebra).** T²−4 rivers give no free joint factorisation. The factorisation actually used is `T+2 = tτ`
  together with `uv = (p+τ)/t`, not `(T−2)(T+2)`.
- **(D) §9 (reformulation only).** Windmills on X-certificates are self-maps of the box modular hyperbola. Infinite menus are
  𝔽_p-automorphisms chosen by lift region. Their fixed points are square roots mod p, so certificates would need
  `A² ≡ c` with small t. Not searched.

**Updated sparks:** (1) a Gauss-lemma weight `w(A) = [lift condition]` on H_p whose sum mod 2 equals `|E(p)| + 1`.
Search over weights built from ⌊AĀ/p⌋ and ⌊kA/p⌋ (Dedekind-sum-like quantities have known reciprocity laws mod 2).
(2) Reflections whose fixed-point equation is bilinear, for example on pairs of forms (Bhargava cubes, where three forms of
the same discriminant compose to 1). A cube-level involution could give "CM point + divisor" in one fixed-point equation.
This is the most promising untested idea.

---
# Checkpoint 3 (spark 2: Bhargava cubes)

**ES is not solved. No candidate was found.** New: WINDMILL_REDUCTION §10, `scripts/wr_cube_class.py`.

- **Lemma 10.1 (PROVED).** Divisor-form certificates are exactly the forms `[m,2,m'']` of disc −4tp. Equivalently they are
  ideal divisors 𝔪 of `(1+√−tp)` with `N𝔪 ≡ −1 (t)`, `4 | N𝔪`. As cubes they are the balanced triples
  `(𝔪, 𝔪'', O; 1+√−tp)`.
- **Computation 10.2 (CERTIFIED for p ≤ 5000, t ≤ 39).** The class map is injective on the divisors of `(1+√−tp)`, apart from
  the trivial pairs {1,N} and {2,N/2}. So the divisors form an embedded Boolean hypercube in Cl(−4tp), and the complement
  involution is class inversion.
- **Proposition 10.3 (PROVED).** `N𝔞 mod ℓ` is a class invariant only modulo squares, because principal norms are
  `≡ x² (mod ℓ)`. Cube classes are pairs of classes, since δ is absorbed by rescaling, and the S₃ ⋉ (ℤ/2)³ symmetries act on
  them by automorphisms. So every class/cube mechanism, including its involution fixed-point counts, sees only the genus
  shadow `(m/ℓ) = (−1/ℓ)` of the ES condition. The full condition is class data iff `t | 24`, i.e. t = 3 for odd
  `t ≡ 3 (4)`. That is the congruence-covering regime (B1). This is an obstruction theorem with exact scope: it covers
  mechanisms that factor through SL₂-classes of forms or SL₂³-classes of cubes.
- **What escapes:** structures that remember the generator δ = 1+√−tp itself, for example balanced triples up to a smaller
  equivalence, or non-maximal orders. I conjecture but have not proved that ring class groups don't help, because they
  record residues of generators, not norms.
- Spark 1 (a Gauss-lemma weight) was not attempted.

**Overall O164 assessment (Assessment).**
- The windmill/reduction programme separates cleanly into a part with CM/genus content (reflections, ambiguous forms,
  classes, cubes) and the residue-class divisor part. Each of §§3, 4, 6, 7, 10 shows the first part reaching the second
  only through quadratic characters.
- A breakthrough along these lines would need an object that remembers *elements*, not ideal classes. Zagier's own set does
  this: it lists simple forms, i.e. elements of the topograph, not classes. For definite discriminants no such finite
  rotation-closed set is known (5.1).

**Remaining sparks:**
1. An element-level finite set for the definite discriminant −4tp: pairs (form, vector) in a box. A "definite topograph
   walk" that is a rotation on vectors of norm ≤ X; its fixed points would be elements.
2. The Gauss-lemma weight on H_p (spark 1).
3. Balanced triples with δ fixed up to units, plus their natural involutions; check this against Prop 10.3's escape clause.
