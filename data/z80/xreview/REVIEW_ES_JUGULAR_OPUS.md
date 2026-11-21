# Hostile cross-lab review (Claude Opus) of `notes/z80/ES_JUGULAR.md` (commit f55746968)

Scope reviewed: everything in `git log main..`, i.e. the note, `scripts/z80_{square_span,cofactor,jugular_trap}.py`,
`data/z80/jugular/{span,basin,trap}.txt`. No ES / (S) / U₇ claim is made, and none is implied. Nothing needs escalating.

**Verdict: ACCEPT the mathematics (A, B, C and the certified counts all hold). Minor revisions on labels, scope and
wording. The significance is low: Theorem A's corollary carries almost no information, and Theorem C kills a rule the
census already shows failing at 13 % of primes.** Triage METHOD-CX and "STATUS delta: none" are right.

## 1. Replays (bounded: `ulimit -v 6000000`, `timeout ≤ 1800`)
* All three replay commands reproduce the committed `trap.txt`, `span.txt` and `basin.txt` **byte-identically**
  (cofactor at 10⁷: 62 s; span at 10⁷: 68 s; trap: under 1 s).
* **Independent re-implementation of the basin census** (my own Miller–Rabin plus Pollard-rho factoring, Euler criterion
  instead of the Jacobi routine, and my own outer-star test): at 10⁷ there are 3426 primes ≡ 1 (840). The plus rule misses
  454 of them, first 7561 (basin size 5) and last 9951481. The ± rule misses 3, first 21841 (162 visited) and last
  1726201. This agrees exactly.
* **Independent span check up to 10⁵.** I enumerated words by brute force over (t, u), with u ≤ v and t·u² − 2u ≤ p, and
  used separate F₂ elimination. Results: 45 primes, 36 spanned, 10 direct, 26 endpoint. The per-prime tuples and word
  counts at 2521, 3361, 4201, 5881, 76441 and 78121 match. In every spanned case a bichromatic word exists, as the
  logic requires (see §5).
* **Independent check of Theorem A, including its converse, by brute force** for all 186 primes p ≡ 1 (8) below 6000.
  A vertex x reaches q **iff** x is odd or p + x is composite: 0 exceptions. Saturation (every odd seed reaches every
  nonresidue) also held at all 186 primes.
* **Independent check of the Theorem C instance** (Miller–Rabin, Pollard rho):
  * r, p, S, L and K are all prime, and q = 17.
  * The negative-prime closure from 17 is exactly {17, r}.
  * The words containing 11, 17 or r in any slot are exactly {(17, 11, r)}. For the middle slot r, u and v were
    searched below 200, which the uv < 187 bound in the proof justifies.
  * χ(tu − 1) = χ(186) = +1, so the word is neutral.

## 2. Theorem A: correct
* **Orbit step.** x ↦ (p + x)/2^{ν₂(p+x)} is injective on odd representatives. Its inverse is y ↦ 2^ν·y − p, with ν the
  unique exponent such that 2^ν·y ∈ (p, 2p). The map is the first return of the single cycle z ↦ [z/2] on x⟨2⟩, so the
  odd representatives form **one** cycle, as claimed. The even-representative arrow 2^j·e − p → e is right: j ≥ 1 and
  2^j·e < 2p. ✓
* **Closure under divisors of z and of p + z, via odd parts.** ✓ H ⊆ residues and 2 ∈ H. ✓
* **Covering lemma.** I checked both orientations of the small gap. D ∈ (p/m, 2p/m) holds strictly: mD = 2p would force
  m | 2p. Also 1 ≤ s ≤ m − 1 and 0 < y = p − sD < D. ✓
* **Adjoining a residue m.** y ∈ (x/m)H is a nonresidue, y < 2p/m ≤ p, and y divides [my] or p + [my]. Hence
  y ∈ C ⇒ x/m ∈ C ⇒ m⁻¹C ⊆ C ⇒ m ∈ H. ✓ The step m = q, with q as the divisor of qy, is right. ✓
* **Even case.** This is right, but "it is < p since p + x < 2p" is too terse. The reason is that p + x is odd and
  composite, so every prime factor is at most (p + x)/3 < p. Please say so.
* **Missing converse.** The converse is trivial but unstated. If x is even and p + x is prime, x has **no** out-arrow,
  because 1 is a residue and the divisor p + x exceeds p − 1. So A is an exact characterisation, and the note should say
  so, because of §3 below.

## 3. The corollary is correct but nearly empty
The corollary assumes p + x = (tx − 1)v is composite. With A and its converse, the backward basin of q is *exactly* the set
of nonresidues x for which x is odd or p + x is composite. So "a reverse search from q contains a negative endpoint of
every such word" just restates that a negative endpoint is a nonresidue with p + x composite, which is the definition.
The note already says it is "not a reduction". It should add plainly that **the reverse basin is essentially the whole
negative half**, so the corollary does not localise words at all. As written, the closing line "solves the accessibility
question for negative endpoints" oversells it.

## 4. Theorem B: correct as a PROVED-rel. sketch. Fix the label.
* **BGK, coset translation and completion.** The main term B|H|/p against the error |H|p^{−η} log p needs only γ < η. The
  constraint "min(η/3, 1/4)" is never used. Drop it, or justify it.
* **Size of H.** H contains the squares of the p^{γ/2}-smooth integers up to p − 1. These have density ρ(2/γ) > 0, and
  each square has at most 2 preimages, so |H| ≫ p. ✓
* **Pólya–Vinogradov step.** A coset of bounded index has discrepancy O(√p log p). So B = p^{2/3} covers, and every
  residue up to p^{1/3} lies in H. ✓
* **Burgess step.** With r = 4 on N = p^{1/3} the bound is N^{3/4}·p^{5/64+ε} = p^{21/64+ε}, which is below
  p^{1/3} = p^{21.33/64}. That gives a power saving, so a proper subgroup H inside the residues is impossible. ✓
* **H is fixed.** H is a fixed stabiliser, so "adjoining" means proving membership. There is no circularity. ✓
* **Label.** "Partial summation" is not used. Pólya–Vinogradov / Gauss sums *are* used but are not in the label.
* **§0 problems.**
  * The §0 label ("rel. elementary finite group arithmetic and quadratic reciprocity") **omits B's dependencies**:
    BGK, Burgess, Dickman–de Bruijn and Pólya–Vinogradov.
  * The §0 Scope line omits B's hypothesis entirely: p large, with ord_p(2) ≥ p^δ.
  * Both should be fixed before export.
* **Unconditional for almost all p.** B covers almost all primes, since ord_p 2 ≥ p^{1/2} for almost all p. Saturation
  held at every small prime I tested. That suggests the order hypothesis is a proof artefact. This is worth one sentence,
  labelled EVIDENCE.

## 5. Theorem C: correct. Label correct (instance CERTIFIED; infinitude CONDITIONAL on Dickson).
* **Identities.** p + 17 = 186r, p + r = 102S, 11p + 1 = 1116S, 17p + 1 = 6K and p + 11 = 12L all check.
* **Least nonresidue.** Since p ≡ 1 (840·143), q = 17, because p ≡ −5 (17) is a non-square. χ(31) = (−17/31) = (14/31)
  = +1, since 13² ≡ 14. So χ(r) = −1 and χ(S) = +1 for every j. The closure statement needs S to be prime, and S is one
  of the Dickson forms. ✓
* **All six slot cases, checked by hand.**
  * Outer 17: v ≡ 5 (17). The divisors of 186 are ≡ {1, 2, 3, 6, 14, 11, 8, 16} (17). Only v = r works.
  * Outer r: u < 94 and u ≡ 17 (mod r).
  * Middle 11: the only factor pair is {186, 6S}.
  * Middle 17: there is none.
  * Outer 11: L ≡ 1 (11) and no divisor of 12 is ≡ −1 (11).
  * Middle r: uv = 186 and u + v = 17 is impossible (the discriminant is negative). Only r > 170 is needed; r > 1000 is
    stated.
* **Dickson admissibility.**
  * Primes 2, 3 and 5 are asserted in the script. Every slope ≡ 0 and every constant is a unit there.
  * For ℓ ≥ 7, at most 5 classes are excluded, and constant reductions are units since gcd(a, b) = 1.
  * The "distinct slopes / nonproportional" remark is irrelevant to Dickson but harmless.
* **Significance.**
  * The plus-rule closure already misses at 454 of 3426 primes up to 10⁷ (`basin.txt`). The prime-only descent is dead
    empirically, and the conditional infinite family adds little beyond the **all-slot isolation** of the single word.
  * The composite-divisor walk of A/B escapes this trap trivially: by B, it saturates whenever ord_p 2 is large.
  * So C kills only the prime-only rule combined with the one-letter-kept move rule. The note says this, but §0 should
    name the two rules explicitly.
* **Replay gap.** `z80_jugular_trap.py` never computes the prime closure {17, r}. It checks only χ(r) = −1. The middle
  slot r is a hard-coded impossibility test, not an enumeration. The proof covers both, and my independent run confirms
  them, but the replay script does not certify the closure claim on its own.

## 6. Certified statistics and the span question
* **Missing explanation.** The note never says why the span statistic matters. For any word, χ(A) = χ(u)χ(v) = χ(uv),
  because p + u = v(tu − 1). So if [q] is an F₂-combination of the classes [u_i·v_i], then −1 = χ(q) = Πχ(A_i), and some
  word is bichromatic. "Spanned" is therefore a multiplicative *certificate* that (S)(p) holds, without naming the
  word. Say so in one sentence; otherwise the statistic reads as unmotivated. My check found no violation.
* **Enumeration bound.** The least-letter bound k³ − 2k ≤ p is right, because tuv − u − v increases in each letter.
* **Label.** The CERTIFIED block says "single Python implementation". With §1 above, it can now cite independent
  coverage: basin to 10⁷ and span to 10⁵ (this review).

## 7. Form
* The screening paragraph maps FRONTIER §4 items loosely. Item 13 is BM, yet it sits in the "transport" group (1–5, 9,
  12–14), while the second sentence says no "BM … obstruction" is used and cites 6–8, 10–11 and 17–19. Items 1 and 2
  are falsifier screens handled in the table, not transport steps. Please regroup.
* The parenthetical "the only divisor of 186 ≡ 1 is 1 modulo 17 (meaning: only the divisor 1 has that residue)" is
  garbled. Use "the only divisor of 186 that is ≡ 1 (mod 17) is 1".
* The trap script's docstring says "inert-prime two-cycle", a term the note never defines. The closure {17, r} is
  presumably meant.
* The data files have no provenance header giving the command and commit. That is acceptable, since the note gives the
  commands.
* The F2 and F3 rows are mostly boilerplate. That is fine, but F2's sentence "a saturated walk would not furnish any
  reciprocal word" is an Assessment, not a screen result.
* The heading order "## §0" followed by "# Title" is unconventional. This is cosmetic.
* §0 "Review: none" should become a pointer to this file.

## 8. Required before export
1. Fix the §0 label and Scope to include Theorem B's dependencies and its ord_p(2) ≥ p^δ hypothesis.
2. State A's converse, and make clear that the corollary's reverse basin is essentially all nonresidues.
3. Correct B's label: drop "partial summation", add Pólya–Vinogradov. Explain γ, or relax it to γ < η.
4. Add one sentence explaining why "spanned" implies a bichromatic word.

Optional: add the closure computation to the trap script, and fix the screening-item grouping.
No master-file change is warranted beyond at most one FRONTIER §6 line for the prime-only descent trap. It should merge
with any existing forest or cofactor dead-end line that has the same root cause (cf. `Z53_FORESTCLASS.md`).
