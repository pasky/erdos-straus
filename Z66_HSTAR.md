# Z66_HSTAR — the missing Hurwitz-type lemma (H★): design and screening of realisation problems for (★)/Type II/(S) (wave z66, lane HSTAR). Verdict: NARROWED (seven scoped no-go results, one structural theorem); no HOT LEAD

**ES is OPEN.** Nothing here proves or disproves ES, (MS), (★), Type II or (S) at any prime. Labels: PROVED /
CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Brief:
`z52bbriefs/z66_lanes.md` §HSTAR (+ z58 common rules, z53 depth brief). Scripts `scripts/z66_hstar_*`, data
`data/z66/hstar/`. Literature notes with URLs and V/V2 flags: `data/z66/hstar/src/lit_hurwitz.md`, `lit_geometry.md`
(two research subagents). Items marked ✔ were re-read by me in the source. Checkpoint 1 (Lemma Ord, KT1, pre-registered
KT1–KT3): commit 60f4c4f56.

## 0. Bottom line

1. **(H★) made precise (§1).** A *realisation scheme* is a datum 𝒟(n) computed from n, a set of realisations, and an
   extraction map ε from realisations to certificates. It is *sound* if every realisation yields a certificate. An
   (H★) is a sound scheme plus an *engine*: a theorem proving realisability at the primes of a class. Soundness makes
   non-realisability at odd squares automatic (T1). So F1 never tests the scheme; it tests the **engine**, whose
   hypotheses must fail at squares.
2. **Theorem Ord (PROVED, §3).** Every representation 4/p = 1/x + 1/y + 1/z (p ≥ 5 prime) has an entry pk with
   k ≥ 2, p ∤ k. Hence every ES pair (X, G) at p ≡ 1 (4) contains an element of order pk. So **no group in which
   elements of order p have p-group centralisers carries an ES pair.** This covers S_p, A_p, every transitive
   subgroup of S_p, AGL₁(p), PSL₂(p) and Frobenius groups with kernel C_p. It also holds for numerator 8. SWZ's engine
   uses primality exactly through C_{S_p}(P) = P (their Lemma 2.5). Theorem Ord says that this structure can never
   carry an ES certificate. KT1 CERTIFIED: 8 334 representations, p ≤ 3000, 0 exceptions.
3. **Six transparency / blindness results (§4), each scoped:**
   * **T (tame transparency; PROVED from Grothendieck, Obus Thm 1.5 + Rem 1.9 ✔).** If the realisations of a
     datum are covers with prime-to-p monodromy, then they are the same in characteristic p and in characteristic 0.
     "Construct in char p" then adds nothing. By Theorem Ord, ES-pair schemes are wild at p; every *tame* scheme
     must extract its certificate from something other than an ES pair.
   * **DD (data-determined extraction; PROVED, trivial).** If ε is constant on the realisations of each datum, the
     scheme is a deterministic witness rule p ↦ f(𝒟(p)), and the engine only certifies that the rule works. With
     the SWZ engine (degree p) this is forced for affine monodromy: affine realisations are parametrised by their
     multipliers, so the scheme is type I (Prop Aff).
   * **N (near-Euclidean arithmetic Hurwitz families are T1-blind; PROVED from CPZ Thm 1.1 ✔, Petronio Thms
     3.13–3.14 V).** These are the only verified Hurwitz families whose realisability depends on the arithmetic of the
     degree. All of them are realisable at every odd square. Moreover T1 itself is a norm statement:
     4Cm² + 1 = N(1 + 2m√−C). For C = 1, the CPZ datum at degree 4n + 1 is realisable *whenever (★)_{C=1}(n) fails*
     (Prop CPZ-T1). **Lattice/Euclidean realisation problems encode the obstruction side of (★), not the existence
     side.**
   * **2V (polynomial extraction from two-square realisations; PROVED).** Every polynomial (★)- or Type II-identity
     in (x, y) with p = x² + y² reduces to a fixed congruence menu in p. So the one free engine at all primes
     p ≡ 1 (4) (Fermat, alias CPZ) feeds no polynomial extraction beyond Mordell-type menus.
   * **Pos (positivity; PROVED, trivial).** (★) has the integral point (1, −n − 1, 0) at every n. So any engine that
     yields only non-archimedean or algebraic existence is T1-blind. T1 lives at the real place (Z58_STRUCT Thm A).
   * **K-block (block/imprimitivity schemes at degree 4Cn + 1; CONDITIONAL on SWZ Thm 1.1 in general,
     unconditional for 4Cn + 1 ≤ 31 by Wang et al. arXiv:2512.06545 ✔ abstract).** A fixed-shape compatible family of
     branch data is realisable whenever 4Cn + 1 is prime, where (★)_C(n) is false. So no such family is sound.
     **KT3 fired** on the natural candidate (the dihedral family; exhaustive census N ≤ 10, CERTIFIED).
4. **Design catalogue (§5): nine designs, all classified by the pre-registered KT2 rule.** Eight land in type I,
   T1-blind, or blocked by Theorem Ord / T. One (D4, the centraliser-split C_p × K form) is what every ES pair at
   p looks like locally. Its extraction is the K-signature, which is type I. **No design survives (KT2).**
5. **Specification theorem (§6, PROVED as a conjunction of §§3–4; Assessment for "natural").** An (H★) for (★) that is
   solved by char-p construction + lifting must:
   * (i) be wild at p, with p-elements centralised by prime-to-p elements;
   * (ii) extract the certificate by a realisation-dependent, non-signature invariant;
   * (iii) carry an archimedean positivity input;
   * (iv) have an engine whose hypotheses fail at odd squares.

   The SWZ engine meets (iv) through "degree = p", but it violates (i). The lifting engines meet (i) (Lemma-F
   covers) but violate (ii) (Prop O, type I). No known engine meets all four.

**Verdict: NARROWED** — (H★) via char-p + lifting or via Riemann existence + group theory is DEAD for every design
class examined (scoped theorems + KT2/KT3). No HOT LEAD. The surviving shape is §6's (i)–(iv). No natural candidate
is known.

## 1. Precise statement attacked

**Definition (realisation scheme).** A realisation scheme for a target T ∈ {(★), Type II, (S), ES} is
𝔖 = (𝒟, Real, ε):
* for every odd n ≥ 5, a *datum* 𝒟(n), i.e. finite data computed from n (a group or degree, conjugacy classes or
  partitions, a base orbifold, a characteristic);
* a set Real(𝒟(n)) of realisations (branched covers, G-curves, monodromy tuples, char-p curves, lattices, …);
* a map ε: Real(𝒟(n)) → Cert_T(n).

*Soundness:* ε is defined at every n, so Real(𝒟(n)) ≠ ∅ ⟹ T(n). An **(H★)** is a sound scheme together with an
*existence engine*: a theorem whose hypotheses hold at every prime p of a class 𝒫 (e.g. 𝔐 mod 840) and which
proves Real(𝒟(p)) ≠ ∅.

*Type I* (Z64_EQUIV §5): the engine realises every datum that already contains a certificate, e.g. a signature.

**Targets (brief).**
* (a) Design an (H★) with 𝒟(p) fixed by p whose realisability fails at odd squares.
* (b) Decide whether char-p construction + lifting, or Riemann existence + group theory (PSL₂ generation, Conder-type
  constructions), can be its engine.

The existence of an (H★) with a working engine is an open question. The scoped no-go statements below are PROVED
where marked.

**Remark 1.1 (F1 is automatic; PROVED, trivial).** If 𝔖 is sound and T ∈ {(★), Type II, (S)}, then
Real(𝒟(m²)) = ∅ for every odd m, because Cert_T(m²) = ∅ (T1; for Type II see Z58_WILDCARD/T1, for (S) the Jacobi
symbol (A/m²) = 1). So a sound scheme always "fails at squares". The real F1 question is **which hypothesis of the
engine fails at m²**.

**Why this is not already closed.**
* Z65_LIFT killed char-p + lifting *as a construction of ES curves* (Thm G, Prop O). It named (H★) as the one
  surviving escape (§5.3) and screened five shapes without theorems.
* Z64_EQUIV Lemma H covers only degree-p *realisability*, not extraction.
* Neither memo treats:
  * extraction maps other than the signature;
  * the centraliser structure that ES pairs force;
  * tame realisation problems;
  * the verified arithmetic Hurwitz families (CPZ/Petronio, Wei–Wu–Xu, Pakovich) as engines;
  * the exhaustive small-degree census.
* `git grep` finds 0 hits for Kani, lifting invariant, theta-characteristic, anti-isometry and Abhyankar, and only a
  source file for Pakovich.
* Zolotarev's sign dictionary is known (`BRAINSTORM/bsB_zolotarev_transpose.md`: it captures the sign layer only) and
  is not redone. Lifting invariants are the one sign mechanism added here (D3).

## 2. Mandatory falsifier table (final)

Mechanism under test: an (H★) — a sound realisation scheme plus an engine (char-p + lifting, Riemann existence +
group theory, or a verified arithmetic Hurwitz theorem).

| screen | behaviour |
|---|---|
| **F1 odd squares** | Automatic for sound schemes (Remark 1.1), so the screen bites on engines. SWZ's engine (degree p) passes vacuously (it says nothing at composite degree), but Theorem Ord shows its primality mechanism cannot carry ES pairs, and DD/Prop Aff make its other extractions type I. The verified arithmetic families (CPZ, Petronio 3.13/3.14) are realisable at every odd square (Lemma N): T1-blind. Engines over F̄_p or ℤ/M only are T1-blind (Lemma Pos). The step that would have to use primality — "the engine's hypothesis fails at m²" — exists only for SWZ (degree prime), and there the extraction is the problem. |
| **F2 C-even / numerator 8** | Theorem Ord_k (k ≥ 4, p > k) holds verbatim for 8/p, so the centraliser obstruction is numerator-blind. Lemma 2V and Lemma K-block hold for the C-even sub-line with 4C → 8C′ (same proofs). Theorem T and DD are numerator-blind. No design distinguishes C odd from C even. |
| **F3 composites** | Prime-degree engines see composites only through EKS-type imprimitivity, i.e. through the *degree's* factorisation (Wei–Wu–Xu Type II, Pervova–Petronio Thm 1.4). That is a different arithmetic event from R(n) = 0: 4545 and the 285 R-zeros have no special Hurwitz meaning. Lemma K-block: block extraction gives *a divisor* of 4Cn + 1, not one in the class −1 (mod 4C) (dihedral family, KT3). |
| **F4 known zeros** | All 14 (★)-zeros and 38 𝔊*-zeros are ≡ 1 (mod 12) (Z65_LIFT §1). Theorem Ord applies there: every ES pair needs C_p × C_k with k ≥ 2 inside G. Every ES curve there has bad reduction (Z65 Thm G). No engine examined proves anything at them. Prop CPZ-T1: at a (★)_{C=1}-zero n, 4n + 1 is a sum of two coprime squares, so the CPZ datum is realisable there: the norm side *sees* the zeros of the C = 1 line, as obstruction. |

**No HOT LEAD.**

## 3. Theorem Ord: ES pairs force large p-centralisers

**Theorem Ord (PROVED).** Let p ≥ 5 be prime and 4/p = 1/x + 1/y + 1/z with x, y, z ≥ 1. Then some entry equals pk
with k ≥ 2 and p ∤ k.

*Proof.* By Z65_LIFT Lemma P no entry is divisible by p². So each entry is p·(unit) or prime to p.
* If p divides no entry, the sum has denominator prime to p; impossible.
* If p divides all three, x = px′ etc., then 1/x′ + 1/y′ + 1/z′ = 4 > 3; impossible.
* (Type I) p divides exactly x = px′. Then 1/y + 1/z = (4x′ − 1)/(px′) with p ∤ yz. Since gcd(4x′ − 1, x′) = 1, the
  right side keeps p in its reduced denominator unless p | 4x′ − 1. Hence 4x′ ≥ p + 1 and x′ ≥ (p + 1)/4 > 1.
* (Type II) p divides exactly x = px′ and y = py′. If x′ = y′ = 1 then 1/z = 2/p; impossible. So max(x′, y′) ≥ 2. ∎

(Type II with x′ = 1 forces z(3y′ − 1) = py′, hence 3y′ − 1 = p and z = y′. This is Mordell's triple
(p, p(p+1)/3, (p+1)/3), whose entry p(p+1)/3 has k = (p+1)/3 ≥ 2.)

**Corollary Ord (PROVED, from Theorem Ord + Z64_EQUIV Lemma A and its Corollary).** Let p ≡ 1 (mod 4), p ≥ 5, and
let (X, G) be an ES pair at p, i.e. |G|(p − 4) = p(2g − 2).
* G contains an element g of order pk with k ≥ 2, p ∤ k.
* Hence P = ⟨g^k⟩ has order p and g ∈ C_G(P), so C_G(P) is not a p-group.
* Consequently no group in which every element of order p has a p-group centraliser carries an ES pair at p.

This includes:
* S_p and A_p (the centraliser of a p-cycle is the cyclic group it generates);
* every transitive G ≤ S_p (contains a p-cycle by Cauchy; C_G ⊆ C_{S_p});
* AGL₁(𝔽_p);
* PSL₂(𝔽_p) (C(u) is the unipotent radical, of order p);
* every Frobenius group with kernel of order p.

*Proof.* By Lemma A's Corollary, X/G ≅ P¹ with three cone points of orders (x, y, z), 1/x + 1/y + 1/z = 4/p. G is
generated by g₁, g₂, g₃ of exactly these orders with g₁g₂g₃ = 1. Apply Theorem Ord. ∎

**Theorem Ord_k (PROVED; F2).** For k ≥ 4 and a prime p > k, every representation k/p = 1/x + 1/y + 1/z has an entry
pk′ with k′ ≥ 2, p ∤ k′. *Proof.*
* No p² (Lemma P's proof: two entries of maximal valuation B ≥ 2 force p/k < a ≤ p²/(kp − 2) < (p + 1)/k).
* Type III needs Σ1/x′ = k > 3.
* Type I needs p | kx′ − 1, so x′ ≥ (p + 1)/k > 1.
* Type II with x′ = y′ = 1 needs z = p/(k − 2) ∈ ℤ, impossible for p > k ≥ 4. ∎

So Corollary Ord holds verbatim for numerator 8: the C-even / 8/p line is treated identically.

*Reading (Assessment).* SWZ's Lemma 2.5 (C_{S_p}(P) = P, N_{S_p}(P) = P ⋊ 𝔽_p^×) is where their engine uses
primality. Corollary Ord says that this very structure is incompatible with ES pairs at every p ≡ 1 (4): an ES
certificate needs C_p *times something*. This sharpens two things:
* Z65 Lemma S, which treated only the monodromy group of a degree-p cover with its own signature, to *all* curves
  with such actions;
* Z65's PSL₂(p) remark, which becomes a theorem.

Any group-theoretic engine for ES pairs must produce elements of order pk, i.e. a direct factor C_p × C_k inside
cyclic subgroups. Lemma-F covers (C_{puBC}) are of this kind.

**KT1 (CERTIFIED).** `scripts/z66_hstar_ord_check.py 3000` → `data/z66/hstar/kt1_ord_3000.txt`:
* all 8 334 representations 4/p = 1/x + 1/y + 1/z (x ≤ y ≤ z) for the 211 primes p ≡ 1 (4), 5 ≤ p ≤ 3000, contain
  an entry pk with k ≥ 2, p ∤ k;
* 0 exceptions; 0 entries divisible by p².

The checkpoint draft expected Mordell exceptions. The script showed none, which led to the statement above.

## 4. Transparency and blindness results

### 4.1 Theorem T (tame transparency)

**Theorem T (PROVED from Obus arXiv:1703.01191 Thm 1.5 and Rem 1.9 ✔, which cite SGA1 XIII Cor 2.12).** Let p be a
prime, k = F̄_p, R = W(k) (or any complete DVR of characteristic 0 with residue field k), and K̄ an algebraic closure
of Frac R. Let B ⊂ P¹ be a finite set of R-sections with pairwise distinct reductions (e.g. {0, 1, ∞}). Let G be a
finite group with p ∤ |G|. Then reduction gives a bijection between:
* G-Galois covers of P¹_{K̄} branched only over B;
* G-Galois covers of P¹_k branched only over B̄.

It preserves ramification indices. Hence it preserves every discrete invariant determined by the monodromy tuple:
the cycle types of the degree-d quotients, block systems, the genera of intermediate quotients, and the Hurwitz
classes.

*Proof.* Rem 1.9 gives an isomorphism φ′ of the maximal prime-to-p quotients of π₁(P¹ ∖ B) in characteristic 0
and in characteristic p (prime-to-p Riemann existence). A G-Galois cover with p ∤ |G| corresponds to a surjection
onto G that factors through the prime-to-p quotient, so the sets of G-covers correspond bijectively. Thm 1.5 gives
the lift, with the same ramification indices, and its uniqueness. Discrete invariants of the monodromy tuple are
transported by φ′. ∎

**Consequence.** For any realisation scheme whose realisations have prime-to-p monodromy:

  Real over F̄_p = Real over ℂ (after fixing branch points),

so "construct in char p + lift" proves exactly what Riemann existence proves. Theorem Ord shows that ES-pair schemes
have p | |G|, so they are wild. A *tame* (H★) must therefore extract the certificate from something other than an ES
pair, for instance the prime-to-p quotient of D4 below. There char p is useless.

### 4.2 Data-determined extraction and affine monodromy

**Lemma DD (PROVED, logic).** Suppose ε is constant on Real(𝒟(n)) for every n, say ε ≡ f(𝒟(n)). Then:
* the scheme with any engine proves "f(𝒟(p)) ∈ Cert_T(p) for p ∈ 𝒫";
* this is a *deterministic witness rule* p ↦ f(𝒟(p)), and its correctness is a Π⁰₁ arithmetic statement;
* the engine contributes only the *existence* of a realisation.

If moreover f ∘ 𝒟 is polynomial in p on residue classes mod q, ET Prop 1.6 / T1 bars it on every square class mod q.

*Proof.* Soundness plus Real(𝒟(p)) ≠ ∅ gives f(𝒟(p)) ∈ Cert(p). The last sentence is the standard identity barrier:
an integer-valued polynomial rule that gives positive certificates on a class gives them at the odd squares of that
class, which contradicts T1. ∎

**Prop Aff (PROVED).** Let 𝒟(p) be a 3-point datum of degree p whose realisations all have monodromy inside
AGL₁(𝔽_p). Then:
* realisations ↔ pairs (a₁, a₂) ∈ (𝔽_p^×)² with ord a₁, ord a₂, ord(a₁a₂) prescribed by the data (up to simultaneous
  conjugation);
* every such pair is realised.

So the realisation set is the explicit set of multiplier pairs, and any extraction ε(a₁, a₂) is type I: the scheme is
equivalent to the arithmetic statement "some multiplier pair of the given orders satisfies the certificate
condition".

*Proof.*
* Elements of AGL₁ are x ↦ ax + b. Non-identity elements with a = 1 are p-cycles. With a ≠ 1 they have exactly one
  fixed point and cycles of length ord a. The multiplier of a product is the product of the multipliers, and
  conjugation preserves multipliers.
* Given (a₁, a₂) with a₁, a₂, a₁a₂ ≠ 1, take σ₁ = (x ↦ a₁x) and σ₂ = (x ↦ a₂x + 1). Then σ₁ and σ₂ have distinct
  fixed points (0 and 1/(1 − a₂)), so they generate C_p ⋊ ⟨a₁, a₂⟩, which is transitive.
* Products are handled the same way. If a datum contains a p-cycle, the multipliers of the other two branch cycles
  are inverse to each other, which is again a pair of prescribed orders. ∎

*Reading.* A certificate condition such as "len(p/A) = 3 and (A/p) = −1" for a multiplier A is an archimedean size
condition on the integer representative of A. The Hurwitz layer imposes only multiplicative orders. This is the
SWZ-side form of Lemma Pos (§4.5).

### 4.3 Near-Euclidean arithmetic families and the norm side of T1

**Verified engines (literature).**
* CPZ Thm 1.1 (✔ arXiv:0810.0591v1; Elem. Math. 67 (2012)): for d = 4k + 1, the datum
  (1,4,…,4), (1,4,…,4), (1,2,…,2) is realisable ⟺ d = x² + y².
* Petronio (Winter Braids LN 7 (2020)) Thm 3.13: the datum [2,…,2,1], [4,…,4,1], [4,…,4,1] is realisable ⟺
  d = x² + y² with x, y of different parity.
* Petronio Thm 3.14: two data, each realisable ⟺ d = x² + xy + y².

(Both Petronio items are V by subagent from the numdam PDF.) These are the only arithmetic-iff results located
(`lit_hurwitz.md` (a5): no family non-realisable exactly at squares is known).

**Lemma N (PROVED, from these statements).** Each of these families is realisable at every odd square d = m²:
* m² = m² + 0², with m odd and 0 even (different parity);
* m² = m² + m·0 + 0².

So none of them, and no family realisable on a set containing the odd squares, can be the datum of a sound scheme
for (★), Type II or (S) (Remark 1.1). ∎

**Prop CPZ-T1 (PROVED).** Let n ≥ 1 and N = 4n + 1. Then:
* (★)_{C=1}(n) ⟺ N has a divisor ≡ 3 (mod 4) ⟺ N has a prime factor ≡ 3 (mod 4) ⟺ N is not a sum of two coprime
  squares.
* Hence ¬(★)_{C=1}(n) ⟹ the CPZ datum at degree N is realisable.
* Equivalently, CPZ(N) non-realisable ⟹ (★)_{C=1}(n).

At odd squares n = m², N = (2m)² + 1² is a coprime sum, and this is T1 on the C = 1 line.

For general C: 4Cm² + 1 = N(1 + 2m√−C) is a primitive norm from ℤ[√−C]. So all its prime factors q satisfy
χ_{−4C}(q) = +1, while −1 ∉ ker χ_{−4C}. This is T1 for every C, as a norm statement.

*Proof.*
* (★)_{C=1}(n) ⟺ (4u − 1)(4B − 1) = 4n + 1 for some u, B ≥ 1 ⟺ N has a divisor ≡ 3 (mod 4). Such a divisor is
  automatically ≥ 3, and its cofactor is also ≡ 3 (mod 4).
* For odd N, a divisor ≡ 3 (4) exists iff some prime factor is ≡ 3 (4). (Products of primes ≡ 1 (4) are ≡ 1 (4);
  conversely a prime factor ≡ 3 (4) is itself such a divisor.)
* N is a sum of two coprime squares iff every odd prime factor is ≡ 1 (4) (classical).
* The CPZ direction uses CPZ Thm 1.1: a coprime sum of two squares is a sum of two squares.
* General C: a prime q | a² + Cb² with q ∤ Cb has (−C/q) = 1. Here b = 2m and a = 1, and q | 4Cm² + 1 implies
  q ∤ 2Cm. Also χ_{−4C}(−1) = −1 because χ_{−4C} is odd. ∎

*Reading (Assessment).* Euclidean (lattice/CM) Hurwitz families realise **norm** conditions. T1 is a norm condition.
So these families detect the *failure* of (★)_C. An engine for (★) would have to prove **non**-realisability of a
norm datum at 4Cp + 1. That is an obstruction (type III), and even then only the genus layer follows: an inert
prime factor, not a divisor in the class −1 (B2: class inside the coset).

### 4.4 Lemma 2V: polynomial extraction from two-square realisations

CPZ is a free engine at every prime p ≡ 1 (4): p = x² + y² (Fermat), and the realisation determines the Gaussian
integer x + iy up to units and conjugation. Can a certificate be read off (x, y) polynomially?

**Lemma 2V (PROVED).** Let a, b, c, d (resp. u, B, C) be polynomials in ℚ[x, y]. Suppose they take positive integer
values on a residue class Λ = {x ≡ x₀, y ≡ y₀ (mod M)} and satisfy, identically,

  4abcd = a + b + c(x² + y²)  (Type II; (★) is the case c = 1).

Then the solution is a *fixed congruence menu*:
* either three of a, b, c, d are constants and the fourth is (p + const)/const with p = x² + y²;
* or (a, b, d constant, c linear in p) the analogous form;
* or a quadratic a, c with a = p/(4bd) + a₁, c = (p/(4bd) + a₁ + b)/(4bd·a₁) for constants b, d, a₁.

In every case each unknown is an affine function of p with constant coefficients, so the identity is an identity in
p on a residue class. By ET Prop 1.6 / T1 such menus never cover a square class of p. Hence **no finite set of
polynomial extractions covers the classes y ≡ 0 (mod M′)**: there p ≡ x² is a square class mod M′.

*Proof.*
* Positivity on Λ (which contains integer points in every rational direction) forces the top homogeneous parts
  a_top, b_top, c_top, d_top to be ≥ 0 on ℝ² and non-zero.
* So there is no cancellation of top parts in a + b + c(x² + y²), and its degree is max(α, β, γ + 2), with α = deg a
  etc. The left side has degree α + β + γ + δ.
* If the maximum is α, then β = γ = δ = 0 and a(4bcd − 1) = b + c·p: a congruence menu. β is symmetric.
* If the maximum is γ + 2, then α + β + δ = 2. Two of a, b, d linear (or a·d linear·linear) would need
  x² + y² = 4·(product of two rational linear forms)/const as top parts. That is impossible, since x² + y² is
  irreducible over ℚ.
* So exactly one of a, b, d is quadratic, with top part (x² + y²)/(4 × the product of the other two constants):
  * **d quadratic.** c·(4abd − p) = a + b with 4abd − p of degree ≤ 1 forces c and 4abd − p = (a + b)/c constant: a
    menu.
  * **a quadratic.** Write a = p/(4bd) + a₁ with deg a₁ ≤ 1. Substituting gives 4bd·a₁·c = p/(4bd) + a₁ + b. The
    right side is irreducible over ℚ of degree 2 (its top part is x² + y²). So a₁ is constant and c is the stated
    quadratic: a menu. b is symmetric.
* The (★) case c = 1 is the same computation, with (4Cu − 1)(4CB − 1) = 4Cp + 1 forced to have u or B constant. ∎

(The same degree argument covers (S): tuv − u − v = x² + y². Its sign condition is a mod-8 cell condition on the
letters (DK Thm 4.5), so it too reduces to fixed menus.)

*Scope.* Non-polynomial extraction from (x, y), e.g. continued fractions of x/y or factorisations of x ± y, is not
excluded. It is no longer a realisation-theoretic step: it is ordinary arithmetic with the two-square
representation as input.

### 4.5 Lemma Pos (positivity is the real place)

**Lemma Pos (PROVED, trivial).** For every integer n, (u, B, C) = (1, −n − 1, 0) solves 4uBC − u − B = n. So T(n) for
T = (★) holds over ℤ, ℤ_ℓ, ℤ/M and 𝔽_p at every n, squares included. Any engine whose output is a solution over a
ring without an ordering is T1-blind. (Z58_STRUCT Thm A: the *positive*-integral BM set is empty exactly at
squares; "without Ω_n it is false".)

Realisation problems do carry positivity automatically: orders, degrees, genera and cycle lengths are positive
integers. That is why ES pairs encode positive (x, y, z), and why F̄_p-constructions can only *transport* such
integers (Prop O), not produce new ones.

### 4.6 Lemma K-block: block/imprimitivity schemes at degree 4Cn + 1

Z65_LIFT §5.3 left one shape open: degree 4Cp + 1, with a block system of size d ≡ −1 (mod 4C) as the certificate.

**Lemma K-block.** Let 𝒟_C(n) be a family of 3-point branch data of degree N = 4Cn + 1 of *fixed shape*: its
partitions are given by formulas in N valid for all N in the progression (e.g. [N], [2^{(N−1)/2}, 1],
[4C^{(N−1)/4C}, 1]), and it is compatible (Riemann–Hurwitz, parity) for all such N. If 4Cn + 1 = q is prime, then
𝒟_C(n) is realisable while (★)_C(n) is false (q has no non-trivial divisor). So the scheme is unsound.
* **CONDITIONAL** on SWZ Thm 1.1 for general q.
* **Unconditional** for q ≤ 31 by Wang et al. (arXiv:2512.06545: "we verify the prime-degree conjecture for all
  primes less than 32", ✔ abstract). It is also re-checked here for q ∈ {5, 7} (KT3).

A sound block scheme must therefore use data that are *incompatible* at prime 4Cn + 1. Compatibility is decided by
the partitions, so this means data defined through the factorisation of 4Cn + 1, i.e. data containing the
certificate (type I). ∎

A second, independent obstruction (PROVED, elementary): an element σ of type [L^m, 1] (one fixed point, all other
cycles of length L) forces every σ-invariant block system to have block size d ≡ 1 (mod L). The fixed point's block
is σ-stable, with one fixed point plus L-cycles. With L = 4C this is the *wrong* class; the class −1 cannot be forced
by one element of this kind.

**KT3 (pre-registered at checkpoint 1; FIRED).** `scripts/z66_hstar_hurwitz_small.c` decides, exhaustively over S_N
(N ≤ 10), realisability, primitivity and block sizes of every compatible 3-point datum. Data:
`data/z66/hstar/hurwitz_N{4..10}.txt`.
* Exceptional counts: N = 4: 1 (EKS's [3,1],[2,2],[2,2] ✓), 5: 0, 6: 6, 7: 0, 8: 14, 9: 7, 10: 35. Primes 5 and 7
  have none, consistent with SWZ and Wang et al.
* At N = 9 = 4·2 + 1 (C = 1; 3 ≡ −1 (mod 4), so (★)_1(2) holds), 18 data are realisable only imprimitively, all
  with block size 3: these are the candidate block data.
* Those that extend to fixed shapes compatible at small N are realisable (primitively) at the primes N = 5 and
  N = 7. Examples, all genus 0 for every N:
  * the dihedral datum ([N], [2^{(N−1)/2}, 1], [2^{(N−1)/2}, 1]);
  * ([N], [N−3, 3], [2, 1^{N−2}]);
  * ([N−3, 3], [N−3, 3], [3, 1^{N−3}]).

  Each line is CERTIFIED in `hurwitz_N5.txt`, `hurwitz_N7.txt` (`P` flag). At N = 5, 4n + 1 = 5 has no divisor
  ≡ 3 (mod 4), so (★)_1(1) is false and these schemes are unsound. More generally, N = 5 and N = 7 have 0
  exceptional data, so *every* fixed shape compatible there is realisable there.
* The dihedral family's blocks are *all* divisors of N, whatever their class mod 4C. At N = 25 the blocks have size
  5 ≡ 1 (mod 4), and (★)_1(6) fails (25 = 5²).
* The remaining candidates contain [3,3,3] (i.e. need 3 | N), or have shapes undefined or incompatible at N = 5, 7.
  At prime N ≤ 31 they are realisable whenever compatible (Wang et al.); otherwise they are type I.
* **D1 is killed** by the pre-registered rule.

## 5. Design catalogue and KT2 classification

KT2 rule (pre-registered): each design is classified as
* (a) type I;
* (b) T1-blind;
* (c) blocked by Theorem Ord / Theorem T / Lemma Pos;
* (d) survives.

| # | design (datum 𝒟(p); realisation; extraction ε) | engine | class | reason |
|---|---|---|---|---|
| D1 | degree 4Cp + 1 data; covers; block size | Riemann existence / SWZ | **(a)+(b)**; KT3 fired | Lemma K-block; dihedral family gives all divisors |
| D2 | CPZ datum at degree p; Lattès-type cover; (x, y) ↦ certificate | Fermat (CPZ) | **(b)** for polynomial ε | Lemma 2V; Lemma N; Prop CPZ-T1 (norm side = obstruction side) |
| D3 | A_N-data with odd-order inertia; covers; lifting invariant (±1) | Fried Thm 1.3 (r ≥ n ≥ 5: both invariants occur; V, `lit_hurwitz.md` (c)) | **(a)** | genus-0 invariant is data-determined, s = ∏_cycles (2/ℓ) (Fried Cor 2.3, V; attributed to Serre, V2), so DD applies. In higher genus the sign is realisation-dependent but carries one bit and no letters (t, u, v). (S)'s sign is a mod-8 function of the letters (DK Thm 4.5), so a ±1 invariant can encode it only if the letters are data (type I) |
| D4 | K-curve Y with signature (x, y′, z′); G = C_p × K; ε = (u, B, C) from signature | Riemann existence (tame) | **(a)** + T | Lemma Split below; char p useless (Theorem T, p ∤ \|K\|) |
| D5 | Γ₀(p)-dessin (PSL₂(ℤ) acting on P¹(𝔽_p)); closed path T^B R^{4C} T^u at 0; (u, B, C) | canonical object | **(c)** Pos | loops exist for (★)(kp) for every k with R(kp) ≥ 1; k = 1 is a size condition (Lemma Pos). Z63_EUCLID covers the H₁ version |
| D6 | CM curve E with End ⊇ ℤ[√(−Cp)], α = 1 + 2√(−Cp); factorisation α = ψ∘φ with deg φ ≡ −1 (4C), i.e. φ anti-symplectic on E[4C] | CM theory / Kani gluing | **(a)** | a factor φ ↔ a divisor of 4Cp + 1 (E10); the gluing (E × E′)/Γ_ψ always exists for any anti-isometry. Kani's reducibility criterion was NOT FOUND in source, so it is not used. Covered by Z60_RAYCLASS |
| D7 | any degree-p datum; covers; any ε | SWZ (CONDITIONAL) | **(c)** + DD | Corollary Ord (no ES pairs in transitive G ≤ S_p); data-determined ε = witness rule (DD); affine realisations type I (Prop Aff); 2-transitive monodromy offers only Burnside/CFSG data (p = (q^k − 1)/(q − 1), …) |
| D8 | PSL₂(𝔽_q) / Conder / Macbeath generating triples | group generation | **(a)**, **(c)** at q = p | Corollary Ord kills q = p. For q ≠ p the signature is input (Macbeath realises any admissible triple) |
| D9 | quasi-p groups as Galois groups over A¹_{F̄_p} (Abhyankar–Raynaud–Harbater; V via Obus survey) | char-p existence | **(a)/(c)** (Assessment) | lifts of wild A¹-covers have more than 3 branch points in general. An ES pair needs exactly 3 (Lemma A). When a 3-point lift exists its signature is read off the char-p datum (Prop O). No ES content enters through quasi-p-ness |

**Lemma Split (PROVED).** Let p be an odd prime and K a finite group with p ∤ |K|. Type II ES pairs (X, G) at p with
G = C_p × K correspond to K-curves Y = X/C_p → P¹ with signature (x, y′, z′) and generating triple
(k₁, k₂, k₃) of these orders such that

  p/x + 1/y′ + 1/z′ = 4,  p ∤ y′z′.

(★) is the cyclic case K = C_{uBC}, (x, y′, z′) = (uBC, BC, uC).

*Proof.*
* (⟹) Generators g_i = (c_i, k_i) with c₁ + c₂ + c₃ = 0. Type II means exactly two c_i ≠ 0, say c₁ = 0. Then
  ord g₁ = ord k₁ = x, ord g_j = p·ord k_j for j = 2, 3, and 1/x + 1/(py′) + 1/(pz′) = 4/p. Multiply by p.
* (⟸) Take g₁ = (0, k₁), g₂ = (1, k₂), g₃ = (−1, k₃). They generate C_p × K because p ∤ |K|.
* Check on (★): (p + u + B)/(uBC) = 4 ⟺ 4uBC − u − B = p. ∎

So every ES pair of this shape is a C_p-decoration of a *tame* K-curve whose signature carries the certificate. That
is type I: Riemann existence realises any signature. In char p the K-part lifts uniquely (Theorem T), so char p
contributes nothing.

**KT2 outcome: every design lands in (a)–(c). None survives.**

## 6. Specification theorem: what a surviving (H★) must look like

**Theorem Spec (PROVED as the conjunction of the cited results; "natural" is Assessment).** Let 𝔖 be a sound
realisation scheme for (★) (or Type II, or (S)) with an engine E.
* (i) If ε factors through an ES pair (X, G) at p, then G contains C_p × C_k with k ≥ 2 (Corollary Ord). E cannot be
  any engine that works inside groups with self-centralising p-elements, including SWZ's.
* (ii) If E is a char-p construction followed by lifting, then:
  * either the realisations are tame, and E = Riemann existence (Theorem T);
  * or they are wild three-point covers with p ∥ |G|, and every lifted discrete invariant is read off the char-p
    datum (Z65 Prop O), so ε's output must be produced by the char-p construction itself.
* (iii) If ε is data-determined, 𝔖 is a deterministic witness rule (DD). If it is polynomial on classes, it is barred
  on square classes.
* (iv) If E proves only non-archimedean existence, E is T1-blind (Lemma Pos). So E needs an ordered/archimedean input.
* (v) By Remark 1.1, E's hypotheses must fail at every odd square.

Among the verified engines:
* SWZ satisfies (iv) and (v) (degree = p; partitions are positive), but by (i) and (iii) it can only power witness
  rules or type-I extractions.
* Wewers / Oort lifting satisfies (i), since Lemma-F covers have G = C_{puBC}, but fails (ii).
* CPZ / Petronio fail (v): they are realisable at squares.
* Fried satisfies (v) only through its group-theoretic hypotheses (r ≥ n). Its output is a sign (D3).

### 6.1 Where characteristic p does create integers (Assessment)
Three sources of integers are *outputs*, not inputs, of a char-p construction:
* the new-tail invariants σ_new of a stable reduction. Under p ∥ |G| they lie in (1/m_G)ℤ with m_G | p − 1
  (Obus Lemma 3.5 as used in Z65 Prop E). They obey the vanishing-cycle sum Σ_prim σ_j + Σ_new(σ_j − 1) = 1;
* forced congruences from a geometric condition, e.g. Z65 Thm G, where potentially good reduction forced
  3m − 1 = p;
* p-ranks / Hasse–Witt data (Deuring–Shafarevich).

None of them enters the *signature* of a lifted three-point cover: stabiliser orders of the marked points are carried
by the char-p datum (Z65 Prop O for p ∥ |G|; in general the generic stabiliser of a branch point specialises to
the stabiliser of its reduction). The created integers have denominators dividing p − 1 (or are congruences of
identity type, Thm G). They are not divisors of 4Cp + 1 in a residue class. The one region where no lifting theory
is available is ES pairs with **non-cyclic** Sylow p-subgroup. Lemma P only forces p ∥ element orders, not
|G|_p = p. Whether such ES pairs exist was not settled here; even if they do, the signature-transparency argument
above does not depend on the Sylow structure.

*Assessment.* A surviving (H★) would be a realisation problem whose discrete data are fixed by p, whose
realisations are wild covers with groups containing C_p × C_k, and whose existence is proved by a char-p
construction that *creates* the integer k. In SWZ the integers (the partitions) are inputs; nothing in the
Raynaud–Wewers theory creates new ones (Prop O). No candidate is known, and §5 lists the natural ones that fail.

## 7. Kill tests, screens, verdict, FRONTIER text, bottom line

**Kill tests (pre-registered at checkpoint 1, commit 60f4c4f56).**
* **KT1 (kill Theorem Ord): PASSED.** 8 334 representations, p ≤ 3000, 0 exceptions (CERTIFIED).
* **KT2 (design decision rule): FIRED.** All nine designs are in classes (a)–(c) (§5). (H★) via these engines is
  DEAD as scoped.
* **KT3 (block design D1): FIRED.** The fixed-shape block datum is realisable at prime degrees 5 and 7, where
  (★)_1 fails (exhaustive census, CERTIFIED). In general this follows from Lemma K-block (CONDITIONAL on SWZ;
  unconditional to degree 31 by Wang et al.).

**FRONTIER §4 hard screens for the best item (Theorem Ord / Theorem Spec as a screening tool).**

| screen | pass/fail |
|---|---|
| T1 squares | Spec (v) states exactly which engine hypothesis must fail at m²; no engine examined has one that also leaves a working extraction |
| 8/131 (numerator 8) | Theorem Ord_k is numerator-uniform; nothing separates C even from C odd. Fail as a route; neutral as a screen |
| tied modulus | D1/D6 make the tie a block size or an isogeny degree mod 4C; Lemma K-block shows block data cannot force the class −1 (one-element lemma: [L^m, 1] forces +1) |
| fixed p | Theorem Ord and Theorem T are pointwise at fixed p; no engine produces a certificate at a fixed p |

**Verdict: NARROWED.** No HOT LEAD.
* *Strengthened (small, PROVED):*
  * Theorem Ord / Ord_k (every ES pair needs C_p × C_k, k ≥ 2; the anti-SWZ centraliser obstruction);
  * Theorem T (tame transparency for realisation schemes);
  * Prop CPZ-T1 (T1 as a norm statement; Euclidean Hurwitz data encode the obstruction side);
  * Lemma 2V;
  * Lemma Split;
  * Lemma K-block (CONDITIONAL / unconditional ≤ 31).
* *Narrowed / dead:* (H★) via char-p + lifting, Riemann existence + PSL₂/Conder/Macbeath generation, verified
  arithmetic Hurwitz families, lifting invariants, block data, CM gluing — all as scoped in §5.
* *Surviving:* only the shape of §6 (a char-p construction that *creates* the integer k of an element of order pk).

**Proposed FRONTIER text (z66 block; not applied here).**
> *(z66 HSTAR, `Z66_HSTAR.md`; internal.)* The missing lemma (H★) of Z65_LIFT was formalised as a sound realisation
> scheme plus an existence engine. F1 is automatic for sound schemes, so the screen bites on the engine.
>
> Results:
> * PROVED: every 3-term representation of 4/p (and of k/p, p > k ≥ 4) has a denominator pk with k ≥ 2. So every
>   ES pair contains an element of order pk, and no group with self-centralising p-elements carries one: S_p, A_p,
>   transitive groups of degree p, AGL₁(p), PSL₂(p). This is precisely the structure through which Song–Wen–Zhang's
>   prime-degree engine uses primality.
> * Tame realisation schemes gain nothing from characteristic p (Grothendieck).
> * The verified arithmetic Hurwitz families (Corvaja–Petronio–Zannier, Petronio) realise norm conditions, are
>   realisable at all odd squares, and encode the *failure* of (★)_C (T1 = "4Cm² + 1 is a norm from ℤ[√−C]").
> * Polynomial extraction from p = x² + y² gives only congruence menus.
> * Fixed-shape block data at degree 4Cn + 1 are realisable at prime 4Cn + 1 (SWZ; unconditional ≤ 31), hence
>   unsound.
>
> Nine designs were screened, and none survives. A surviving (H★) would need a characteristic-p construction that
> creates the integer k of an element of order pk; none is known.

**Bottom line.** The brief asked for a Hurwitz-type realisation problem with p-determined data that fails at squares
and is solvable by characteristic-p or group-theoretic methods. Soundness alone makes any certificate-producing
scheme fail at squares, so the real question is the engine. There the picture is sharp:
* The one engine whose hypotheses fail at squares for a structural reason, prime-degree Hurwitz (SWZ), works
  through self-centralising p-subgroups. Every ES certificate needs the opposite: a p-element with a non-trivial
  prime-to-p centraliser.
* Tame engines in characteristic p are just Riemann existence.
* The arithmetic Hurwitz families that do see the degree's arithmetic see *norms*. T1 is a norm statement, so they
  see the obstruction to (★), not its solutions.
* Block data can certify a divisor, but not one in the residue class −1 (mod 4C).

What would be needed is a characteristic-p construction that creates, rather than transports, the integer k in an
element of order pk. Nothing in the Raynaud–Wewers theory does that. The lane closes the realisation-problem route as
far as the known engines reach. It leaves only that very specific shape open.

## 8. Sources (✔ = re-read by me; V/V2 = verified by research subagent, see `data/z66/hstar/src/`)
* ✔ Obus, *Lifting of curves with automorphisms*, arXiv:1703.01191v2 (Adv. Lect. Math. 46 (2019) 9–59): Thm 1.5
  (tame Riemann existence converse; cites SGA1 XIII Cor 2.12), Rem 1.9 (prime-to-p π₁ isomorphism).
* ✔ (abstract) Wang, Li, Zhou, Wei, Ye, Shi, Xu, arXiv:2512.06545v2: complete list of non-realisable 3-point
  partition triples for d ≤ 31; prime-degree conjecture verified for primes < 32. ✔ (PDF §4): Types 0–III, with
  Type II = Wei–Wu–Xu's common-divisor criterion.
* V Corvaja–Petronio–Zannier, Elem. Math. 67 (2012) 169–181, arXiv:0810.0591, Thm 1.1.
* V Petronio, Winter Braids LN 7 (2020), Exposé 2, Thms 3.13, 3.14.
* V Pakovich, JKTR 18 (2009) 271–302, Thm 1.1 (Laurent passports). V Pervova–Petronio, AGT 6 (2006), Props 1.2–1.3,
  Thms 1.4–1.5. V2 EKS 1984 Prop 5.7 (via Pervova–Petronio).
* V Fried, Israel J. Math. 179 (2010), arXiv:math/0611591: Thm 1.2, Thm 1.3, Cor 2.3 (genus-0 lifting invariant;
  attributed to Serre 1990, V2).
* V Obus, arXiv:1208.3909v3 Thm 5.2 (good reduction, cyclic p-Sylow; Raynaud 1999 Thm 0 V2).
* NOT FOUND (not used): Kani's anti-isometry reducibility criterion; Singerman's inclusion list; EEK torsion-free
  index theorem.
* In-repo: Z65_LIFT (Lemma P, Prop O, Lemma S, Thm G), Z64_EQUIV (Lemma A, E10, §5 types), Z58_STRUCT (Thm A),
  `BRAINSTORM/bsB_zolotarev_transpose.md`, Z63_EUCLID, Z60_RAYCLASS.

## 9. Review log
(pending: hostile reviewer subagent, deep mode)
