# Hostile cross-lab review, round 2 (Claude Opus) of `notes/z80/ES_JUGULAR.md` at eefb78516 — priority: Theorem D (§5)

Scope: all of `git log main..` (f55746968, 3efcb419b, eefb78516). For A–C, this round checks only that the
round-1 fixes (`REVIEW_ES_JUGULAR_OPUS.md`) were applied. The new material is `§0`, §5 / Theorem D,
`scripts/z80_kernel_budget.py` and `data/z80/jugular/kernel.txt`. The note makes no claim of ES, (S), U₇ or Type I
existence, and none is implied. Nothing needs escalating.

**Verdict: ACCEPT Theorem D mathematically.** I re-derived every step and found no gap. The gaps I found are in
statement, form and context. There are no FATAL or MAJOR mathematical issues. Six items should be fixed before
export (§9). The significance is modest. D is a correct quantitative strengthening of the pointwise witness barrier
(`Z57_BFII.md` Cor 2.4), proved by the B4-style residue-profile sieve. For each fixed q its threshold is a **constant**,
not a function of p. Triage BARRIER-SCOPED and "STATUS delta: none" are right.

## 1. Replays and independent checks (bounded: `ulimit -v 6000000`, `timeout` ≤ 1800 s)
* **`z80_kernel_budget.py 10000000`** reproduces the committed `kernel.txt` byte-for-byte (72 s wall, 173 MB RSS).
  `z80_jugular_trap.py` reproduces the new `trap.txt`, including `prime closure [17, 607717433]`, byte-for-byte.
  `span.txt`, `basin.txt` and their scripts have not changed since the round-1 replay.
* **Independent re-implementation of the kernel census to 10⁶.** It uses its own SPF sieve, Euler criterion and brute
  enumeration of every word with u ≤ v, t ≥ 2 and A = tu − 1 | p + u, so it does not use the cube-root least-letter
  engine. Result: `[(1,'P>q'),16] [(1,'all'),146] [(1,'direct'),0] [(3,'P>q'),42] [(3,'all'),249] [(3,'direct'),80]`.
  The author's script at 10⁶ gives identical bins. So the census is now covered by two engines to 10⁶, and by one
  engine (replayed) to 10⁷.
* **Type II identities, brute force.** For every positive (a, b, c, d, e) with 4abd = p + e and a + b = ce, at all
  primes p ≡ 1 (4) below 3000 (6376 parametrisations), I checked:
  * f = 4acd − 1 divides cp + a, and f′ = 4bcd − 1 divides cp + b;
  * the Jacobi symbols (p/f) and (p/f′) are both −1;
  * f′ < 4p when b ≤ a, and f′ < 2p²/(a²de) when b > a;
  * the norm identity [d(2b + a)]² − de·f′ = d(da² + e).

  There were 0 failures.
* **Trap-prime good word.** At p = 113035442521 I checked that 34 | p + 5 and that v = 3324571839 satisfies
  7·5·v − 5 − v = p, with χ(34) = −1. For general j, r ≡ 5 (17) gives p = 186r − 17 ≡ −5 (17), so the word persists.

## 2. Sign profile and class costs ✓
* **The profile** (p ≡ 1 (840), (p/l) = +1 for odd l ≤ Y with l ≠ q, (p/q) = −1) is a finite set of reduced classes
  mod 840·∏_{l≤Y} l, and it is nonempty for q > 7.
  * Since p ≡ 1 (4), χ_p(l) = (p/l), so q is the least nonresidue.
  * On Y-smooth integers coprime to p, χ_p(n) = (−1)^{v_q(n)}.
* **Class cost.** At a profile prime l the conditional density of p ≡ a (l^k) is 2/φ(l^k) or 0. At l > Y it is
  1/φ(l^k). At 2, 5 and 7 the 840 condition costs the bounded factors 2, 2 and 3. So C₀·2^{ω(m)}/φ(m) is a valid upper
  bound with **absolute** C₀. ✓
* **Strengthening available.** The bound is the limiting density, so D also holds with natural (not just lower)
  relative density, and "relative" can be dropped: the profile has positive density among all primes for fixed q.
  The statement should say so, and should give the actual density 2^{−π(Y)+O(1)}. "Positive relative density" without
  a named reference set is ambiguous.

## 3. Word calculation ✓ (one typo)
* **Sign forcing.** χ(tu − 1) = χ(uv) follows from p + u = (tu − 1)v. If sf(uv) is Y-smooth, q must appear to odd
  order. ✓
* **Coprimality.** A common prime of u and v divides p, and u, v < p. The condition is therefore the single unit
  class p ≡ −u − v (mod uv). ✓
* **uv ≤ p** holds because p = tuv − u − v ≥ 2uv − uv. This needs interior letters u, v ≥ 2. ✓
* **Euler factors.** At l ≤ Y, l ≠ q, the factor is 1 + 4Σ_k 1/φ(l^k) = 1 + 4l/(l − 1)². At l > Y only even
  exponents occur and the product is bounded. At q the odd exponents cost ≤ 5/q. Mertens gives a total
  ≤ K·(log Y)⁴/q = K c⁴ with K absolute. So c is absolute and the "< 1/4" choice is legitimate. ✓
* **Typo.** In the BT tail the weight should be 4^{ω(m)}/φ(m) (orientations × class cost), not 2^{ω(m)}/φ(m).
  This is harmless: the sum runs over m = s h² with s in a finite set, so it converges either way.
* **Order of limits.** I checked the interchange (BT, then counting, then limits).
  * Upper density of the bad set B ≤ d(B_T) + limsup_X |B \ B_T| / π_prof(X).
  * d(B_T) ≤ Σ_{m ≤ T} cost (PNT, fixed moduli).
  * The BT range T < m ≤ √X contributes ≪_prof tail(T).
  * The range √X < m ≤ X contributes ≪ X^{3/4+ε} = o(X/log X).
  * Then let T → ∞.

  The constants depend on the profile only in the tail terms, which vanish. **No uniformity in q is needed there,
  and none is used.** ✓
* **The weak exponent 1/4 is a presentational choice.** With Y = exp(q^β), β < 1/4, the bad mass is q^{4β−1} → 0 and
  the relative density is 1 − o(1). Suggest stating it that way. "exp(c q^{1/4}) with c small" hides that the true
  statement is "density 1 − O((log Y)⁴/q)".

## 4. Type II calculation ✓
* **Divisibility.** cp + a = 4abcd − b = b·f, and (f, c) = 1. ✓ gcd(p, f) = 1: if p | f then p | a, but f ≡ −1 (a). ✓
* **χ(f) = −1.** This follows from `Z57_BFII.md` Lemma 2.1 and Prop 2.2 (checked: p ≡ −a/c (f), (ac/f) = 1, f ≡ 3 (4)),
  then Jacobi reciprocity with p ≡ 1 (4). ✓
* **Class count.** There are ≤ τ₃((f+1)/4) classes, one per (a, c) with ac | (f + 1)/4. The other orientation has the
  same shape after swapping a ↔ b. ✓
* **Tilted product.** With α = 1/log Z: q < Z gives q^α ≤ e. Σ_{l≤Z} 4l^α/l = 4 log log Z + O(α Σ log l / l)
  = 4 log log Z + O(1). Higher powers converge for α ≤ 1/4. At l > Z, Σ l^{−2+2α} converges. So the product is
  ≪ (log Z)⁴/q with an absolute constant. ✓
* **Cauchy–Schwarz on a block.** Σ C₀ τ₃ 2^ω/φ ≤ C₀ · max f/φ(f) · (Σ_S 4^ω/f)^{1/2} (Σ τ₃(f+1)²/f)^{1/2}.
  The first factor is ≤ F^{−α}·(tilted sum) by Rankin. The second is ≪ (log 3F)⁸, by τ₃² ≤ τ₉ and
  Σ_{n≤x} τ₉ ≪ x(log x)⁸ on a **dyadic** block (on [1, x] it would be (log x)⁹; the block restriction is what the
  note needs). ✓
* **Dyadic sum.** Σ_j 2^{−jα/2} j⁴ log j ≍ (log Z)⁵ log log Z. The total is ≪ q^{−1/2}(log Z)⁷ log log Z, which → 0
  iff β < 1/14. So the stated 1/15 is correct. ✓ The bound is only q^{−1/2}, which loses against the word bound.
  Hölder with higher moments would push β towards 1/4, which is optional.
* **Large-modulus tail (the real novelty).** I checked each step.
  * 2abd ≤ p, using e ≤ a + b ≤ 2ab.
  * b ≤ a gives f′ < 8abd ≤ 4X.
  * b ≥ a gives f′ < 2X²/(a²de). So f′ > X^{3/2} forces a²de ≤ 2√X.
  * The norm identity holds (§1).
  * For non-square D = des: x + h√D ∈ ℤ[√D] ⊂ O_K generates an O_K-ideal of norm N.
  * There are #{ideals of norm N} = Σ_{m|N} χ_Δ(m) ≤ τ(N) such ideals. The note says "prime-ideal decomposition"; it
    would help to quote this formula.
  * Generators of one ideal differ by units. Both are totally positive, so they differ by ε₊^k.
  * Tr ε₊ ≥ 3 gives log ε₊ ≥ 0.96, uniformly in D. The range is α ∈ (√N, 2x). This yields O(log X) per ideal.
    The bound is **uniform in the discriminant**, as claimed. ✓
  * For square D, factor the difference of squares. ✓
  * The number of triples is in fact O(√X log X); the note's O(√X log² X) is a harmless overcount.
  * τ(N) ≪ X^ε with N ≪ X. The total is O(X^{1/2+ε}) = o(X/log X). ✓
  * **Correct warning.** The note is right that naive integer counting up to X² would fail; this is the step a
    careless version would get wrong.
* **Middle range.** X < f ≤ X^{3/2}: there are ≤ X^{3/4} values of h per kernel, each with τ₃ ≪ X^ε classes and at
  most one integer ≤ X per class. ✓

## 5. The (★) witness and the intersection ✓
* **The witness word.** Take g ≡ 3 (4), g > Y, t = 4, u = (g + 1)/4, so 4u ≡ 1 (g) and u is a square mod g. Then
  χ_p(g) = (−u/g) = −1. The word is a C = 1 (★) triple (FRONTIER §2.1), interior for p large. ✓
* **Avoidance density.** Avoiding a finite set G of such primes has conditional density Π(1 − 1/(g − 1)), since g is
  prime to the profile modulus. This → 0, because Σ 1/g diverges on 3 (4). ✓
* **Intersection.** The lower density is ≥ 1 − 1/4 − o_q(1) − 0 > 0. ✓ Natural density exists via finite truncations:
  for fixed f the Type II event is a union of classes mod lcm(f, c), and for fixed m the word event is a single class.
  Upper-bounding it by the mod-f class is legitimate. ✓
* **Consistency.** The witness word must itself carry a prime > Y in sf(uv). That is consistent, since g need not
  divide v.

## 6. Sharpness — a falsifier row the note lacks (substantive, but confirms D)
**D cannot be upgraded to "all profile primes" at q ≡ 3 (4).** For such q:
* if p ≡ −4 (q) (allowed: −4 is a nonresidue mod q), the word (u, t, v) = (q, ((p+4)/q + 1)/4, 4) is good, interior
  for p > 10q, and has sf(uv) = q. The kernel script even **asserts** this.
* if p ≡ −1 (q), the Type II point (a, b, c, d, e) = (1, (p + 1)/q, 1, (q + 1)/4, 1 + b) has f = q.

So each conclusion fails on relative density ≥ 2/(q − 1). The 1/q factor in both Euler products is therefore
sharp in order, and "positive density, not all" is forced. At q ≡ 1 (4) kernel exactly q is impossible pointwise (the
note's argument, which is correct), but kernels such as 2q or qℓ are not. Please add this as the D falsifier/sharpness
line. It is the best evidence that the theorem is calibrated rather than vacuous.

## 7. Significance, scope and priority (challenge)
* **Threshold scale.** For fixed q the threshold Y (or Z) is a constant while p → ∞ along the family. Expressed in p,
  D gives no growing bound: "exponentially large in a power of q" is literally true but invites misreading. The honest
  phrasing is that the odd-valuation kernel must leave the support of the prescribed residue profile. Pointwise, the
  old barrier (Z57 Cor 2.4) gives only f ≥ ℓ ≥ q. D adds that q alone, or q times profile primes and an arbitrary
  square, cannot carry the kernel.
* **What it kills.** It kills constructions of words or Type II points whose endpoint product or modulus is
  (smooth) × q^{odd} × □. Examples are Pell/norm-form or square-shift recipes that put all the "new" arithmetic into a
  square part. Those are worth recording as one FRONTIER §6 line. It is not BARRIER-BROAD: it says nothing about
  solutions using a prime > Y, which is what typical solutions do.
* **Nearest internal relatives — please cite them.**
  * `Z57_BFII.md` Cor 2.4 is the pointwise predecessor. The note cites only Prop 2.2.
  * `LONGSHOT_PIGEONHOLE.md` Thm 2.2 / FRONTIER B4 and checklist item 17 use the same "p ≡ 1 (8∏_{l≤Y} l) profile +
    positive lower density" technique, against coset-covering certificates.
  * `notes/z79/WILD_ES.md` §7 (end) already observes that a hit with f wholly B₀-smooth contradicts (−uv/f) = −1. That
    is the pointwise seed of D's sign forcing.
  * `ES_CONNECTIONS_TODO.md` Z2406 (essentially full F₂-rank of word kernels) is the empirical counterpart.

  The z78 §6 / z79 §9 distinction in the note is correct: those bound the *size* of the least modulus in terms of p,
  whereas D bounds the *prime support of every kernel* with only a constant size consequence. External priority was
  not checked; "no external priority claim" is the right posture. A likely classical relative is the
  Mordell/Yamamoto nonresidue obstruction, which D refines.
* **A cheap extension (optional).** The word denominators are also covered. A = tu − 1 ≤ p + u, so there is no X² tail.
  There are τ(A + 1) classes, and the same CS gives q^{−1/2}(log Z)^{9/2}. So every good word's A has sf(A) with a
  prime > exp(q^β) for β < 1/9. Together with §5's bullet 1, this would cover both word objects.
* **Sign carrier.** "These large primes need not be nonresidues" is correct and important. Keep it in §0.

## 8. Form
1. **§0 Review line** still reads as if the round-1 cross-review covered the note. At eefb78516 Theorem D, which is
   now the §0 Result, had **no** cross-review. Update it to point to this file, and mark D's verdict.
2. **The §0 Result** describes only D. "need" should be "have", and "exponentially large in a power of q" should be
   qualified as in §7. The title ("The cofactor walk: …") no longer matches the headline.
3. **Undefined terms in §5:** "good word" (χ(tu − 1) = −1), "interior" (all letters ≥ 2), "(★) word" (t = 4C, FRONTIER
   §2.1), and "positive Type II parameterisation" (`Z57_BFII.md` (2.15)). D's proof depends on each.
4. **Misplaced proof.** The trap-prime good word (5, 7, (p + 5)/34) is a proof, not a certificate. Move it from the §5
   CERTIFIED block to §3. It does materially sharpen §3's scope: the trapped primes satisfy (S) via a disjoint word,
   which strengthens round 1's "low significance" remark.
5. **Label of D:** add "Rankin/Cauchy–Schwarz and elementary divisor-moment bounds" (minor). ET's parametrisation is
   needed only to read "every Type II solution" in §0 from the parametrised statement. That is fine.
6. **"Controls for D."** "Items 4–9, 15–17 of the preflight" lumps item 17 (B4) without discussion. D is closest to B4,
   so say how it differs: D constrains every solution rather than a certificate recipe.
7. **Census claim.** "At 435/3426 primes the best attainable largest prime of sf(uv) exceeds q" replays, and is now
   independently confirmed to 10⁶ (§1). The data file has no provenance header, as in round 1.
8. **Round-1 fixes.** All four required fixes were applied: the §0 label/scope for B, A's converse and the corollary's
   reverse basin, B's label with γ < min(η, 1), and the span ⇒ bichromatic sentence. The optional trap closure and
   screening regrouping were also applied. Not applied: the optional EVIDENCE sentence that B's order hypothesis looks
   like an artefact. The "o(π(X)) exceptions" sentence is correct: the count of primes is ≤ log₂ Π_{k≤X^δ}(2^k − 1)
   = O(X^{2δ}).

## 9. Required before export
1. Update the §0 Review line to cite this review for D. Rephrase the Result per §7/§8.2 ("constant in p for fixed q";
   "density 1 − O((log Y)⁴/q)" if adopted).
2. Add the §6 sharpness row (q ≡ 3 (4): p ≡ −4 and p ≡ −1 mod q give kernel / modulus exactly q).
3. Define good / interior / (★) / Type II parametrisation in §5, or point to their definitions.
4. Fix the BT-tail weight 2^{ω} → 4^{ω}. Optionally fix the triple count to O(√X log X) and quote Σ_{m|N} χ_Δ(m) ≤ τ(N).
5. Cite Z57 Cor 2.4, B4/LONGSHOT_PIGEONHOLE Thm 2.2 and z79 §7 as the nearest relatives, and state the difference.
6. Move the trap-prime word remark to §3.

Master files: at most one FRONTIER §6 line ("smooth-kernel × square constructions of words/Type II moduli fail on a
positive-density profile set at each large q; sharp to O(1/q)"). Merge it with the B4 / witness-barrier root cause if
an existing line fits. No STATUS change.
