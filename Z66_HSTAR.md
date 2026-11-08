# Z66_HSTAR — the missing Hurwitz-type lemma (H★): design and screening of realisation problems for (★)/Type II/(S) (wave z66, lane HSTAR). Verdict: NARROWED (a centraliser obstruction, a polynomial-extraction lemma, scoped transparency results, an exhaustive small-degree census); no working engine identified; no HOT LEAD

**ES is OPEN.** Nothing here proves or disproves ES, (MS), (★), Type II or (S) at any prime. Labels: PROVED /
CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Brief:
`z52bbriefs/z66_lanes.md` §HSTAR (+ z58 common rules, z53 depth brief). Scripts `scripts/z66_hstar_*`, data
`data/z66/hstar/`. Literature notes with URLs and V/V2 flags: `data/z66/hstar/src/lit_hurwitz.md`, `lit_geometry.md`
(two research subagents). Items marked ✔ were re-read by me in the source; V = verified by a subagent. Checkpoint 1
(Lemma Ord, KT1, pre-registered KT1–KT3): commit 60f4c4f56. Hostile review (deep): §9; all findings applied.

## 0. Bottom line

1. **(H★) made precise (§1).** A *realisation scheme* is:
   * a datum 𝒟(n) computed from n;
   * a set of realisations;
   * an extraction map ε from realisations to certificates.

   It is *sound* if every realisation yields a certificate. An (H★) is a sound scheme plus an *engine*: a theorem
   proving realisability at the primes of a class. Soundness makes non-realisability at odd squares automatic (T1).
   So F1 never tests the scheme; it tests the **engine**, whose hypotheses must fail at squares (or wherever
   certificates do not exist).
2. **Theorem Ord (PROVED, §3).** Every representation 4/p = 1/x + 1/y + 1/z (p ≥ 5 prime) has an entry pk with k ≥ 2,
   p ∤ k (likewise k/p for p > k ≥ 4). Hence every ES pair (X, G) at p ≡ 1 (4) contains an element of order pk.
   So **no group in which elements of order p have p-group centralisers carries an ES pair**: S_p, A_p, every
   transitive subgroup of S_p, AGL₁(p), PSL₂(p), Frobenius groups with kernel C_p.

   SWZ's prime-degree engine uses primality exactly through C_{S_p}(P) = P (their Lemma 2.5). So no ES pair can
   live in the groups that engine works with. KT1 CERTIFIED: 8 334 representations, p ≤ 3000, 0 exceptions.
3. **Scoped transparency / blindness results (§4).**
   * **T (PROVED from Grothendieck; Obus Thm 1.5 + Rem 1.9 ✔).** For Galois covers with **prime-to-p monodromy**,
     the realisations over F̄_p and over ℂ correspond bijectively, preserving discrete invariants. A char-p
     construction cannot enlarge such a realisation set.
   * **DD (PROVED, logic).** A realisation-independent extraction makes the scheme a deterministic witness rule.
   * **Aff (PROVED).** Affine-monodromy data of degree p have an explicitly parametrised realisation set (three
     cases). The engine is superfluous there: the scheme reduces to an elementary arithmetic statement about the
     parameters.
   * **N (PROVED).** The verified arithmetic Hurwitz families (Corvaja–Petronio–Zannier; Petronio 3.13/3.14) are
     realisable at every *admissible* odd square, so they cannot be data of a sound scheme indexed by the degree.
   * **CPZ-T1 (PROVED).** ¬(★)_{C=1}(n) ⟹ the CPZ datum at degree 4n + 1 is realisable (one-way only;
     n = 11 shows the converse fails). T1 for every C is a norm statement: 4Cm² + 1 = N(1 + 2m√−C).
   * **2V (PROVED).** Every polynomial (★)- or Type II-identity in (x, y), p = x² + y², is a fixed congruence menu in
     p. So the free engine at all p ≡ 1 (4) (Fermat, alias CPZ) feeds no polynomial extraction beyond Mordell-type
     menus.
   * **Pos (PROVED, trivial).** The *unrestricted* (★) equation has an integral point at every n. So an engine that
     only proves existence of solutions of the unrestricted equation over rings without an ordering is T1-blind.
   * **K-block (PROVED for naked-cover schemes; CONDITIONAL on SWZ beyond degree 31; KT3 fired).** If realisations
     are all covers with given fixed-shape compatible partitions of degree 4Cn + 1, the scheme is unsound at prime
     4Cn + 1, with domain-valid witnesses n = 7 (degree 29, Wang et al.) and, for the dihedral family, n = 9
     (degree 37, unconditional). Block-*equipped* schemes are not excluded.
4. **Design catalogue (§5).** Nine designs, classified by the pre-registered KT2 rule:
   * five are type I or T1-blind or blocked as scoped: D1 naked, D2 polynomial, D4, D6, D8;
   * four are **unresolved — no working extraction identified**: D3 in higher genus, D5, D7 for general ε, D9; plus
     block-equipped D1.

   KT2 therefore does **not** fire in the strong sense "none survives". It records that no design has a working
   engine.
5. **Necessary conditions (§6).** A scheme for (★) extracting through an ES pair must use groups with p-elements
   centralised by prime-to-p elements (Ord). If its realisations have prime-to-p monodromy, char p adds no
   realisations (T). In the Wewers setting (three-point covers, p ∥ |G|) the signature is read off the char-p datum
   (Z65 Prop O). ES pairs with p² | |G| exist (homology covers, §6). The special-map / cyclic-Sylow results cited
  here do not apply to them.

**Verdict: NARROWED.** Useful centraliser obstruction, polynomial-extraction lemma, transparency in the prime-to-p and
Wewers settings, reproducible census. No working new engine identified. Several broader extraction and lifting
possibilities remain unexcluded (§5 "unresolved" rows, §6). No HOT LEAD.

## 1. Precise statement attacked

**Definition (realisation scheme).** A realisation scheme for a target T is 𝔖 = (𝒟, Real, ε):
* for every odd n ≥ 5, a *datum* 𝒟(n), i.e. finite data computed from n (a group or degree, conjugacy classes or
  partitions, a base orbifold, a characteristic);
* a set Real(𝒟(n)) of realisations (branched covers, possibly equipped with extra structure such as a block system;
  G-curves; monodromy tuples; char-p curves; lattices; …);
* a map ε: Real(𝒟(n)) → Cert_T(n).

Targets: T ∈ {(★), Type II, (S∃), ES}. Here (S∃)(n) is the existential witness statement "L₃(n) contains a word A
with (A/n) = −1". (The repository's (S) is the conditional statement "for non-squares with L₃(n) ≠ ∅ …"; (S∃) is
the part that implies ES at primes.)

*Soundness:* ε is defined at every n, so Real(𝒟(n)) ≠ ∅ ⟹ T(n). An **(H★)** is a sound scheme together with an
*existence engine*: a theorem whose hypotheses hold at every prime p of a class 𝒫 (e.g. 𝔐 mod 840) and which proves
Real(𝒟(p)) ≠ ∅.

*Type I* (Z64_EQUIV §5): the engine realises data that already contain a certificate, e.g. a signature.

*The definition is semantic, not a non-circularity criterion.* The tautological scheme 𝒟(n) = n, Real = Cert,
ε = id qualifies. No effective extraction or complexity bound is required. All content lies in an engine proved
independently of the certificate search.

**Targets (brief).**
* (a) Design an (H★) with 𝒟(p) fixed by p whose realisability fails at odd squares.
* (b) Decide whether char-p construction + lifting, or Riemann existence + group theory (PSL₂ generation, Conder-type
  constructions), can be its engine.

The existence of an (H★) with a working engine is an open question. The scoped statements below are PROVED where
marked.

**Remark 1.1 (F1 is automatic; PROVED, trivial).** If 𝔖 is sound and T ∈ {(★), Type II, (S∃)}, then
Real(𝒟(m²)) = ∅ for every odd m, because Cert_T(m²) = ∅:
* (★) by T1;
* Type II by Z58_WILDCARD (N_II(m²) = 0);
* (S∃) because (A/m²) = 1.

So a sound scheme always "fails at squares". The real F1 question is **which hypothesis of the engine fails at
m²**.

**Why this is not already closed.**
* Z65_LIFT killed char-p + lifting *as a construction of ES curves* (Thm G, Prop O). It named (H★) as the one
  surviving escape (§5.3) and screened five shapes without theorems.
* Z64_EQUIV Lemma H covers only degree-p *realisability*, not extraction.
* Neither memo treats extraction maps other than the signature, the centraliser structure ES pairs force, tame
  realisation problems, or the verified arithmetic Hurwitz families (CPZ/Petronio, Wei–Wu–Xu, Pakovich) as
  engines. There was also no exhaustive small-degree census.
* `git grep`: 0 hits for Kani, lifting invariant, theta-characteristic, anti-isometry, Abhyankar; Pakovich only in a
  source file.
* Zolotarev's sign dictionary is known (`BRAINSTORM/bsB_zolotarev_transpose.md`: sign layer only) and is not redone.

## 2. Mandatory falsifier table (final)

Mechanism under test: an (H★) — a sound realisation scheme plus an engine (char-p + lifting, Riemann existence +
group theory, or a verified arithmetic Hurwitz theorem).

| screen | behaviour |
|---|---|
| **F1 odd squares** | Automatic for sound schemes (Remark 1.1); the screen bites on engines. SWZ's engine (degree p) does not apply at composite degree, so it passes F1 vacuously. But Theorem Ord shows that the groups it works in cannot carry ES pairs. The verified arithmetic families (CPZ, Petronio 3.13/3.14) are realisable at every admissible odd square (Lemma N), so they are T1-blind as degree-indexed data. Engines proving only existence of unrestricted (★)-solutions over unordered rings are T1-blind (Lemma Pos). No engine examined has a hypothesis that fails at m² *and* comes with a working extraction. |
| **F2 C-even / numerator 8** | Theorem Ord_k (k ≥ 4, **p > k**) holds for 8/p (p > 8; note 8/7 = 1/2 + 1/2 + 1/7), so the centraliser obstruction is numerator-blind. Lemma 2V and Lemma K-block go through for the C-even sub-line with 4C → 8C′ (same proofs). T and DD are numerator-blind. No design distinguishes C odd from C even. |
| **F3 composites** | Prime-degree engines see composites only through imprimitivity of the *degree* (Wei–Wu–Xu, Pervova–Petronio Thm 1.4). That is a different arithmetic event from R(n) = 0. *Assessment:* 4545 and the 285 R-zeros have no special Hurwitz meaning (not a proved universal negative). Block extraction yields *a* divisor of 4Cn + 1, not one in the class −1 (mod 4C) (dihedral family, KT3). |
| **F4 known zeros** | All 14 (★)-zeros and 38 𝔊*-zeros are ≡ 1 (mod 12) (Z65_LIFT §1). Theorem Ord applies there: every ES pair needs an element of order pk, k ≥ 2. By Z65 Thm G every ES curve there has bad reduction. No engine examined proves anything at them. At a zero of the C = 1 line, 4n + 1 is a coprime sum of two squares, so the CPZ datum is realisable (Prop CPZ-T1). The converse does not hold. |

**No HOT LEAD.**

## 3. Theorem Ord: ES pairs force large p-centralisers

**Theorem Ord (PROVED).** Let p ≥ 5 be prime and 4/p = 1/x + 1/y + 1/z with x, y, z ≥ 1. Then some entry equals pk
with k ≥ 2 and p ∤ k.

*Proof.* By Z65_LIFT Lemma P no entry is divisible by p², so each entry is p·(unit) or prime to p.
* If p divides no entry, the sum has denominator prime to p; impossible.
* If p divides all three, x = px′ etc., then 1/x′ + 1/y′ + 1/z′ = 4 > 3; impossible.
* (Type I) p divides exactly x = px′. Then 1/y + 1/z = (4x′ − 1)/(px′) with p ∤ yz. Since gcd(4x′ − 1, x′) = 1, the
  right side keeps p in its reduced denominator unless p | 4x′ − 1. Hence 4x′ ≥ p + 1 and x′ ≥ (p + 1)/4 > 1.
* (Type II) p divides exactly x = px′ and y = py′. If x′ = y′ = 1 then 1/z = 2/p; impossible. So max(x′, y′) ≥ 2. ∎

(Type II with x′ = 1 forces z(3y′ − 1) = py′, hence 3y′ − 1 = p and z = y′. This is Mordell's triple
(p, p(p+1)/3, (p+1)/3), whose entry p(p+1)/3 has k = (p+1)/3 ≥ 2.)

**Corollary Ord (PROVED, from Theorem Ord + Z64_EQUIV Lemma A and its Corollary).** Let p ≡ 1 (mod 4), p ≥ 5, and let
(X, G) be an ES pair at p, i.e. |G|(p − 4) = p(2g − 2).
* G contains an element g of order pk with k ≥ 2, p ∤ k.
* So P = ⟨g^k⟩ has order p and g ∈ C_G(P), and C_G(P) is not a p-group.
* Consequently no group in which every element of order p has a p-group centraliser carries an ES pair at p.

This includes:
* S_p and A_p (the centraliser of a p-cycle is the cyclic group it generates);
* every transitive G ≤ S_p (contains a p-cycle by Cauchy; C_G ⊆ C_{S_p});
* AGL₁(𝔽_p);
* PSL₂(𝔽_p) (C(u) is the unipotent radical, of order p);
* every Frobenius group with kernel of order p.

*Proof.* By Lemma A's Corollary, X/G ≅ P¹ with three cone points of orders (x, y, z), 1/x + 1/y + 1/z = 4/p, and G is
generated by g₁, g₂, g₃ of exactly these orders with g₁g₂g₃ = 1. Apply Theorem Ord. ∎

**Theorem Ord_k (PROVED; F2).** For k ≥ 4 and a prime **p > k**, every representation k/p = 1/x + 1/y + 1/z has an
entry pk′ with k′ ≥ 2, p ∤ k′. *Proof.*
* No p² (Lemma P's proof: two entries of maximal valuation B ≥ 2 force p/k < a ≤ p²/(kp − 2) < (p + 1)/k).
* Type III needs Σ1/x′ = k > 3.
* Type I needs p | kx′ − 1, so x′ ≥ (p + 1)/k > 1.
* Type II with x′ = y′ = 1 needs z = p/(k − 2) ∈ ℤ, impossible for p > k ≥ 4. ∎

So Corollary Ord holds for numerator 8 at primes p > 8, i.e. the C-even / 8/p line is treated identically. (p > k is
needed: 8/7 = 1/2 + 1/2 + 1/7.)

*Reading (Assessment).* SWZ's Lemma 2.5 (C_{S_p}(P) = P, N_{S_p}(P) = P ⋊ 𝔽_p^×) is where their engine uses
primality. Corollary Ord says no ES pair at p ≡ 1 (4) can live in such groups: an ES certificate needs C_p *times
something* inside a cyclic subgroup. This sharpens two things:
* Z65 Lemma S (the monodromy group of a degree-p cover with its own signature) to *all* curves with such actions;
* Z65's PSL₂(p) remark, which becomes a theorem.

It does **not** exclude extracting certificates from degree-p covers by other means (§5, D7).

**KT1 (CERTIFIED).** `scripts/z66_hstar_ord_check.py 3000` → `data/z66/hstar/kt1_ord_3000.txt`:
* all 8 334 representations (x ≤ y ≤ z) for the 211 primes p ≡ 1 (4), 5 ≤ p ≤ 3000, contain an entry pk with k ≥ 2,
  p ∤ k;
* 0 exceptions; 0 entries divisible by p²;
* the script exits non-zero if it fires.

The reviewer reran it at 1000: 80 primes, 2 078 representations, 0 exceptions. The checkpoint draft expected Mordell
exceptions; the script showed none, which led to the statement above.

## 4. Transparency and blindness results

### 4.1 Theorem T (prime-to-p transparency)

**Theorem T (PROVED from Obus arXiv:1703.01191 Thm 1.5 and Rem 1.9 ✔, which cite SGA1 XIII Cor 2.12).** Let p be a
prime, k = F̄_p, R = W(k) (or any complete DVR of characteristic 0 with residue field k), and K̄ an algebraic closure
of Frac R. Let B ⊂ P¹ be a finite set of R-sections with pairwise distinct reductions (e.g. {0, 1, ∞}). Let G be a
finite group with **p ∤ |G|**. Then reduction gives a bijection, preserving ramification indices, between
isomorphism classes of:
* G-Galois covers of P¹_{K̄} branched only over B;
* G-Galois covers of P¹_k branched only over B̄.

Hence every discrete invariant determined by the monodromy tuple is preserved: cycle types of the degree-d
quotients, block systems, genera of intermediate quotients.

*Proof.* Rem 1.9 gives an isomorphism φ′ of the maximal prime-to-p quotients of π₁(P¹ ∖ B) in characteristic 0 and
in characteristic p. A G-Galois cover with p ∤ |G| corresponds to a surjection onto G that factors through the
prime-to-p quotient, so the two sets correspond bijectively. Thm 1.5 gives the lift with the same ramification
indices, and its uniqueness. ∎

*Scope.* The hypothesis is prime-to-p **monodromy**. Tame ramification alone is weaker, and covers with p | |G| but
tame inertia are not covered. Theorem T is a statement about realisation *sets*: a char-p construction cannot
produce a prime-to-p realisation that does not already exist over ℂ. It does not say that a char-p *argument* cannot
be a new proof of existence. It says only that what such an argument proves is a char-0 statement, decidable by
finite group theory (a monodromy-tuple count). By Theorem Ord, ES-pair schemes have p | |G|, so T does not apply to
them.

### 4.2 Data-determined extraction and affine monodromy

**Lemma DD (PROVED, logic).** Suppose ε is constant on Real(𝒟(n)) for every n, say ε ≡ f(𝒟(n)). Then:
* the scheme with any engine proves "f(𝒟(p)) ∈ Cert_T(p) for p ∈ 𝒫", a *deterministic witness rule*
  p ↦ f(𝒟(p));
* the engine contributes the existence of a realisation, i.e. a (possibly non-trivial) *proof* that the rule
  works;
* if f ∘ 𝒟 is computable and total, membership in 𝒫 is decidable and certificates are checkable, then
  correctness of the rule is a Π⁰₁ statement;
* if T is square-obstructed ((★), Type II, (S∃); **not** ES) and f ∘ 𝒟 is a polynomial identity in p on residue
  classes mod q, with positive integral values on the whole class, then ET Prop 1.6 / T1 bars it on every square
  class mod q.

A data-determined output is a witness rule, not automatically a certificate supplied in the datum, and not
automatically trivial.

(A realisation-independent output need not be "supplied in the datum". DD only says that the scheme *is* a witness
rule, so its content can be judged as such: WITNESS lane, z58.)

*Proof.* Soundness plus Real(𝒟(p)) ≠ ∅ gives f(𝒟(p)) ∈ Cert(p). The last point is the standard identity barrier: an
integer-valued polynomial rule giving positive certificates on a class gives them at the odd squares of the class
(for large squares), which contradicts T1. ∎

**Prop Aff (PROVED).** Let p be an odd prime and 𝒟(p) a 3-point datum of degree p such that the realisations
considered have monodromy inside AGL₁(𝔽_p) (σ_i : x ↦ a_i x + b_i, multipliers a_i with a₁a₂a₃ = 1). Up to
simultaneous conjugation inside AGL₁ (which is also S_p-conjugacy here: a conjugator between two such transitive
tuples normalises the common translation subgroup, the unique Sylow-p, hence lies in AGL₁), the transitive
realisations are exactly as follows. The branch cycles are labelled and non-identity; the cases are stated after
reordering where needed.
* **(no translation)** all a_i ≠ 1, with σ₁, σ₂ having distinct fixed points. Moving the first fixed point to 0
  and the second to 1 gives σ₂ = a₂x + (1 − a₂); a further scaling gives the normal form σ₁ = a₁x, σ₂ = a₂x + 1.
  Parameter (a₁, a₂);
* **(one multiplier 1)** a₁ = 1, i.e. σ₁ a translation (a p-cycle), normal form σ₁ = x + 1, σ₂ = a₂x; parameter a₂,
  with a₃ = a₂⁻¹;
* **(all multipliers 1)** three translations x + 1, x + t, x − 1 − t with t ∉ {0, −1}: **p − 2 classes**, parameter t,
  for the datum ([p], [p], [p]).

All parameter values with the prescribed orders are realised. So the realisation set is explicit, and any extraction
is a function of these elementary parameters. The scheme is equivalent to an arithmetic statement about a set that
can be written down without any engine; SWZ is superfluous for such data.

*Proof.*
* Multipliers multiply and are conjugation-invariant. An element with a ≠ 1 has one fixed point and cycles of length
  ord a; with a = 1 and b ≠ 0 it is a p-cycle.
* If two non-translations share their fixed point, the group fixes it: intransitive. Otherwise conjugate the first
  fixed point to 0 and scale the second to 1. Their commutator is a non-trivial translation, so the group is
  transitive.
* With σ₁ a translation, normalise it to x + 1 and conjugate σ₂'s fixed point to 0.
* Three translations: normalise σ₁ = x + 1. Then σ₂ = x + t, and t is invariant under the centraliser of σ₁ in AGL₁
  (the translations). Transitivity holds for any non-zero translation. ∎

(The checkpoint version claimed a multiplier-only parametrisation; the reviewer's ([p],[p],[p]) counterexample is
the third case.)

*Reading.* A certificate condition such as "len(p/A) = 3 and (A/p) = −1" for a parameter A is an archimedean size
condition on an integer representative. The Hurwitz layer imposes only multiplicative orders.

### 4.3 Near-Euclidean arithmetic families and the norm side of T1

**Verified engines (literature; V by subagent, `lit_hurwitz.md` (a1), (a2)).**
* CPZ Thm 1.1 (Elem. Math. 67 (2012); arXiv:0810.0591): for d = 4k + 1, the datum (1,4,…,4), (1,4,…,4), (1,2,…,2)
  is realisable ⟺ d = x² + y².
* Petronio (Winter Braids LN 7 (2020)) Thm 3.13: [2,…,2,1], [4,…,4,1], [4,…,4,1] is realisable ⟺ d = x² + y² with
  x, y of different parity.
* Petronio Thm 3.14: [2,…,2,1], [3,…,3,1], [6,…,6,1] (needs d ≡ 1 (6)) and [3,…,3,1]³ (needs d ≡ 1 (3)) are
  realisable ⟺ d = x² + xy + y².

No family non-realisable exactly at squares is known (`lit_hurwitz.md` (a5)).

**Lemma N (PROVED, from these statements).**
* The CPZ and Petronio 3.13 data are defined at every odd square d = m² (m² ≡ 1 (4)) and realisable there:
  m² = m² + 0², with m odd and 0 even.
* The Petronio 3.14 data are defined at d = m² iff 3 ∤ m (then m² ≡ 1 (6)), and realisable there:
  m² = m² + m·0 + 0².

So no sound scheme whose datum at n is one of these families *at degree n* exists. (For a reparametrised degree
d = f(n) the conclusion does not transfer automatically.) ∎

**Prop CPZ-T1 (PROVED).** Let n ≥ 1 and N = 4n + 1. Then:
* (★)_{C=1}(n) ⟺ N has a divisor ≡ 3 (mod 4) ⟺ N has a prime factor ≡ 3 (mod 4) ⟺ N is not a sum of two coprime
  squares.
* Hence ¬(★)_{C=1}(n) ⟹ the CPZ datum at degree N is realisable. Contrapositive: CPZ(N) non-realisable ⟹
  (★)_{C=1}(n).
* The converse fails. At n = 11, 45 = 6² + 3² makes CPZ(45) realisable, while (u, B) = (1, 4) gives
  4·1·4 − 1 − 4 = 11, a (★)_1 certificate.

At odd squares n = m², N = (2m)² + 1² is a coprime sum: this is T1 on the C = 1 line.

**General C (PROVED).** 4Cm² + 1 = N(1 + 2m√−C) is a primitive norm from ℤ[√−C]. Every prime q | 4Cm² + 1 is odd
and prime to 2Cm, hence (−C/q) = 1, i.e. χ_{−4C}(q) = +1. The Kronecker character χ_{−4C} is odd, so χ_{−4C}(−1) = −1.
A divisor d ≡ −1 (mod 4C) would have χ_{−4C}(d) = −1. But χ_{−4C} is multiplicative and equals +1 on every prime
factor. So there is no such divisor: T1 for every C, as a norm statement.

(This is a statement about norms, not a Hurwitz realisation theorem for general C.)

*Proof of the C = 1 chain.*
* (★)_{C=1}(n) ⟺ (4u − 1)(4B − 1) = 4n + 1 with u, B ≥ 1 ⟺ N has a divisor ≡ 3 (mod 4) (its cofactor is then also
  ≡ 3 (mod 4) and ≥ 3).
* For odd N such a divisor exists iff some prime factor is ≡ 3 (mod 4).
* N is a sum of two coprime squares iff every odd prime factor is ≡ 1 (mod 4) (classical).
* The CPZ implication uses CPZ Thm 1.1. ∎

*Reading (Assessment, scoped).* Euclidean (lattice/CM) Hurwitz families realise **norm** conditions, and T1 is a norm
condition. For C = 1 every failure of (★)_1 makes the CPZ datum realisable, but some successes do too. To get (★)_1
from CPZ one would have to prove *non*-realisability: an obstruction (type III). That needs 4p + 1 to be a non-norm,
which is stronger than (★)_1 (it needs a prime ≡ 3 (4) to an odd power).

### 4.4 Lemma 2V: polynomial extraction from two-square realisations

CPZ is a free engine at every prime p ≡ 1 (4): p = x² + y² (Fermat). Can a certificate be read off (x, y)
polynomially?

**Lemma 2V (PROVED).** Let a, b, c, d ∈ ℚ[x, y] take positive integer values on a residue class
Λ = {x ≡ x₀, y ≡ y₀ (mod M)} and satisfy, identically,

  4abcd = a + b + c(x² + y²)  (Type II; (★) is the case c = 1).

Write p = x² + y². Then the solution is a *fixed congruence menu*, of one of two kinds:
* three of a, b, c, d are constants and the fourth is (p + const)/const or (const·p + const)/const;
* or a and c are quadratic and b, d constant: a = p/(4bd) + a₁, c = (p/(4bd) + a₁ + b)/(4bd·a₁), with a constant a₁
  (b ↔ a symmetric).

In every case each unknown is an affine function of p with constant coefficients, so the identity is an identity in
p on a residue class. By ET Prop 1.6 / T1 such menus never cover a square class of p. Hence **no finite set of
polynomial extractions covers the classes y ≡ 0 (mod M′)**: there p ≡ x² is a square class mod M′.

*Proof.*
* **Positivity.** Λ contains integer points in every rational direction, arbitrarily far out. So positivity forces
  every top homogeneous part a_top, … to be ≥ 0 on ℝ². A non-zero binary form of odd degree changes sign
  (f(−v) = −f(v)), so **every non-constant one of a, b, c, d has even degree**.
* **No cancellation.** Top parts of a, b, c(x² + y²) are ≥ 0 and non-zero, so a + b + c(x² + y²) has degree
  max(α, β, γ + 2), with α = deg a etc. The left side has degree α + β + γ + δ.
* **Maximum α** (ties assigned here first). Then β = γ = δ = 0 and a(4bcd − 1) = b + c·p: a menu. The case of
  maximum β is symmetric.
* **Maximum γ + 2** (strictly bigger than α and β). Then α + β + δ = 2 with even degrees, so exactly one of a, b, d
  is quadratic and the other two are constant.
  * **d quadratic.** Top parts: 4ab·d_top·c_top = c_top·(x² + y²), so d_top = (x² + y²)/(4ab). Then
    c·(4abd − p) = a + b, where L := 4abd − p has degree ≤ 1. Since a + b is a positive constant, L ≠ 0, and
    deg(cL) = 0 forces c and L constant: a menu.
  * **a quadratic.** Write a = p/(4bd) + a₁ with deg a₁ ≤ 1. Substituting into a(4bcd − 1) = b + cp gives
    4bd·a₁·c = p/(4bd) + a₁ + b. The right side has degree 2, and its top part x² + y² is irreducible over ℚ, so it
    is irreducible over ℚ. If c were constant the degrees would not match; hence a₁ is constant and c is the stated
    quadratic: a menu. b is symmetric.
* **(★) case** c = 1: the same analysis with γ = 0. ∎

(The same degree argument covers (S∃): tuv − u − v = x² + y². Its sign is a mod-8 cell condition on the letters
(DK Thm 4.5), so it also reduces to fixed menus.)

*Scope.* Lemma 2V needs an **identity** in ℚ[x, y] and **positive integral values on the whole residue coset** Λ.
Non-polynomial extraction from (x, y) (continued fractions of x/y, factorisations of x ± y, …) is still an extraction
map under §1. It is **not excluded**: D2 with general ε is unresolved, like D7 with general ε.

### 4.5 Lemma Pos (the unrestricted equation)

**Lemma Pos (PROVED, trivial).** For every integer n, (u, B, C) = (1, −n − 1, 0) solves 4uBC − u − B = n. So the
**unrestricted** (★) equation has solutions over ℤ, ℤ_ℓ, ℤ/M and 𝔽_p at every n, squares included. An engine whose
only output is the existence of such solutions is T1-blind. Z58_STRUCT Thm A: the *positive*-integral BM set is
empty exactly at squares, and "without Ω_n it is false".

*Scope.* This does not exclude non-archimedean constructions with additional conditions, or geometric constructions
whose degrees, orders and dimensions (automatically positive integers) carry the certificate. Realisation problems
do carry positivity in this way. That is why ES pairs encode positive (x, y, z).

### 4.6 Lemma K-block: naked block schemes at degree 4Cn + 1

Z65_LIFT §5.3 left one shape open: degree 4Cp + 1, with a block system of size d ≡ −1 (mod 4C) as the certificate.
There are two kinds of scheme:
* *naked*: Real = all covers with the given partitions, and ε reads off a block size;
* *block-equipped*: Real = covers *together with* a non-trivial block system.

**Lemma K-block (naked schemes).** Let 𝒟_C(n) be a family of 3-point branch data of degree N = 4Cn + 1 of *fixed
shape*: its partitions are given by formulas in N valid for all N in the progression (e.g. [N], [2^{(N−1)/2}, 1],
[N − 3, 3], [3, 1^{N−3}]), and it is compatible (Riemann–Hurwitz, parity) for all such N. If N = 4Cn + 1 is prime,
then:
* 𝒟_C(n) is realisable;
* every realisation is primitive (prime degree), so ε has no block to read;
* (★)_C(n) is false (N has no non-trivial divisor).

So the naked scheme is unsound.
* **CONDITIONAL** on SWZ Thm 1.1 for general prime N.
* **Unconditional** for N ≤ 31 by Wang et al. (arXiv:2512.06545, "we verify the prime-degree conjecture for all
  primes less than 32", ✔ abstract). Domain-valid instance: C = 1, n = 7, N = 29 prime.
* **Unconditional for every N** for the dihedral family ([N], [2^{(N−1)/2}, 1], [2^{(N−1)/2}, 1]): D_N acting
  naturally realises it at every odd N. Domain-valid instance at a square: C = 1, n = 9, N = 37 prime, so
  (★)_1(9) fails while the datum is realised (primitively).

Even at composite N the dihedral family's blocks are *all* the divisors of N, whatever their class mod 4C. ∎

*Block-equipped schemes are not excluded by K-block.* At prime N they have no realisations, so they are not
contradicted there. Their engine would have to prove that an *imprimitive* realisation with block size ≡ −1 (mod 4C)
exists, which in particular produces such a divisor of 4Cp + 1. No engine of that kind is known. This shape stays
**unresolved** (Assessment: such an engine would be a divisor-existence theorem for 4Cp + 1, i.e. B2 itself).

**One-element lemma (PROVED, elementary).** An element σ of type [L^m, 1] (one fixed point, all other cycles of
length L) forces every σ-invariant block system to have block size d ≡ 1 (mod L): the fixed point's block is σ-stable
and consists of the fixed point plus whole L-cycles. With L = 4C this is the *wrong* class.

**KT3 (pre-registered at checkpoint 1; FIRED for naked schemes).** `scripts/z66_hstar_hurwitz_small.c` decides,
exhaustively over S_N (N ≤ 10), realisability, primitivity and block sizes of every compatible 3-point datum. Data:
`data/z66/hstar/hurwitz_N{4..10}.txt`. The reviewer reran N = 4–10 byte-identically.

| N | realisable | imprimitive-only | exceptional |
|---:|---:|---:|---:|
| 4 | 7 | 3 | 1 |
| 5 | 17 | 0 | 0 |
| 6 | 57 | 15 | 6 |
| 7 | 141 | 0 | 0 |
| 8 | 428 | 41 | 14 |
| 9 | 1072 | 18 | 7 |
| 10 | 2952 | 117 | 35 |

* N = 4 has the single EKS exception [3,1],[2,2],[2,2]. The primes 5 and 7 have none, consistent with SWZ and Wang
  et al. No complete per-degree table was found in the literature for comparing the composite counts.
* At N = 9 (C = 1, n = 2; 3 ≡ −1 (mod 4)), 18 data are realisable only imprimitively, all with block size 3: these
  are the candidate block data. Fixed shapes among them are realisable (primitively) at N = 5 and 7:
  * the dihedral ([N], [2^{(N−1)/2}, 1]²);
  * ([N], [N−3, 3], [2, 1^{N−2}]);
  * ([N−3, 3]², [3, 1^{N−3}]);

  all of genus 0 for every N (`P` flags in `hurwitz_N5.txt`, `hurwitz_N7.txt`). N = 5, 7 lie outside the domain
  odd n ≥ 5. The domain-valid failures are the K-block instances N = 29 (Wang et al.) and N = 37 (dihedral,
  unconditional).
* The remaining candidates contain [3,3,3] (they need 3 | N) or have shapes undefined or incompatible at small primes.
* **Naked D1 is killed** by the pre-registered rule. Block-equipped D1 is unresolved (above).

## 5. Design catalogue and KT2 classification

KT2 rule (pre-registered): each design is classified as
* (a) type I;
* (b) T1-blind;
* (c) blocked by Theorem Ord / Theorem T / Lemma Pos;
* (d) survives.

After review a fifth label is used: **(u) unresolved** — not excluded, but no working extraction or engine
identified.

| # | design (datum 𝒟(p); realisation; extraction ε) | engine | class | reason |
|---|---|---|---|---|
| D1n | degree 4Cp + 1 fixed-shape data; all covers; block size | Riemann existence / SWZ | **(b)**-type unsound; KT3 fired | Lemma K-block (n = 7, N = 29; dihedral n = 9, N = 37) |
| D1e | as D1n, realisations equipped with a block system | — | **(u)** | needs an engine producing imprimitive realisations with d ≡ −1 (4C), i.e. a divisor of 4Cp + 1 in the class (Assessment: this is B2) |
| D2 | CPZ datum at degree p; Lattès-type cover; (x, y) ↦ certificate | Fermat (CPZ) | **(b)** for polynomial ε (under 2V's identity + full-coset positivity hypotheses); general ε: **(u)** | Lemma 2V; Lemma N; Prop CPZ-T1 (one-way) |
| D3 | A_N-data with odd-order inertia; covers; lifting invariant (±1) | Fried Cor 2.3 (genus 0); Fried Thm 1.3 concerns only 3-cycle Nielsen classes with r ≥ n ≥ 5 (V) | genus 0: witness rule via DD (not automatically type I); higher genus: **(u)** | genus-0 invariant data-determined, s = ∏_cycles (2/ℓ) (Fried Cor 2.3, V; Serre's formula, V2). Higher genus: no map from realisations to length-3 words or (u, B, C) is known; not excluded |
| D4 | K-curve Y with signature (x, y′, z′); G = C_p × K; Type II certificate from the signature | Riemann existence | **(a)** | Lemma Split: the certificate is the signature; for p ∤ \|K\| the K-part is prime-to-p, so Theorem T applies to it |
| D5 | Γ₀(p)-dessin (PSL₂(ℤ) acting on P¹(𝔽_p)); closed path T^B R^{4C} T^u at 0; (u, B, C) | canonical object | **(u)** | loops exist for every (★)(kp) solution, k ≥ 1; k = 1 is a size condition that no bound in sight supplies. Not excluded. Z63_EUCLID covers the H₁ version |
| D6 | CM curve E, End ⊇ ℤ[√(−Cp)], α = 1 + 2√(−Cp); factorisation α = ψ∘φ with deg φ ≡ −1 (4C) (φ anti-symplectic on E[4C]) | CM theory | **(a)** | a factor φ ↔ a divisor of 4Cp + 1 (E10); covered by Z60_RAYCLASS. Kani's reducibility criterion was NOT FOUND in source and is not used |
| D7 | degree-p data; covers; general ε | SWZ (CONDITIONAL) | ES-pair ε: **(c)**; data-determined ε: witness rule (DD); affine data: elementary (Aff); general ε: **(u)** | Corollary Ord excludes extraction via ES pairs on the monodromy group. Other realisation-dependent extractions (word orders, Hurwitz-orbit data, lifting invariants) are not excluded; none is known that outputs (★)-certificates |
| D8 | PSL₂(𝔽_q) / Conder / Macbeath generating triples | group generation | **(a)**; **(c)** at q = p | Corollary Ord kills q = p; for q ≠ p the signature is input |
| D9 | quasi-p groups as Galois groups over A¹_{F̄_p} (Abhyankar–Raynaud–Harbater; V via Obus survey) | char-p existence | **(u)** (Assessment) | no route from an A¹-cover to a three-point ES pair is known; when a three-point lift with p ∥ \|G\| exists its signature is read off the char-p datum (Prop O) |

**Lemma Split (PROVED).** Let p ≥ 5 be prime and K a finite group with p ∤ |K|. Consider ES pairs (X, G) at p with
G = C_p × K that are **triangle covers**, i.e. X/G ≅ P¹ with three cone points. (For p ≡ 1 (4) this is automatic
by Z64_EQUIV Lemma A's Corollary.) Every such pair is Type II. Such pairs correspond (up to an automorphism of C_p fixing the generator choice c₂ = 1) to
K-curves Y = X/C_p → P¹ with marked points of orders (x, y′, z′) and a generating triple (k₁, k₂, k₃) of K of these
orders, k₁k₂k₃ = 1, such that

  p/x + 1/y′ + 1/z′ = 4.

A marked point with y′ = 1 or z′ = 1 is kept even if Y → P¹ is unramified there.

*Proof.*
* (⟹) Write the generators g_i = (c_i, k_i), c₁ + c₂ + c₃ = 0 in C_p, not all c_i = 0 (G is generated).
  * Exactly one c_i ≠ 0 is impossible.
  * Three non-zero c_i would make all three orders divisible by p, excluded by Theorem Ord's proof.
  * So exactly two are non-zero, say c₁ = 0, c₂ = −c₃ ≠ 0; normalise c₂ = 1.
  * Then ord g₁ = ord k₁ = x and ord g_j = p·ord k_j (p ∤ |K|). Now 1/x + 1/(py′) + 1/(pz′) = 4/p; multiply by p.
* (⟸) g₁ = (0, k₁), g₂ = (1, k₂), g₃ = (−1, k₃) generate C_p × K since p ∤ |K|. ∎

**(★) is a proper sub-family.** (★) corresponds to cyclic K = C_{uBC} with (x, y′, z′) = (uBC, BC, uC); then
(p + u + B)/(uBC) = 4 ⟺ 4uBC − u − B = p. Not every cyclic K-curve is of this form. At p = 409, take K = C₂₃₄ with
generating triple (2, 115, 117) of orders (117, 234, 2): 409/117 + 1/234 + 1/2 = 936/234 = 4. This gives the Type II
representation 4/409 = 1/117 + 1/95706 + 1/818, while R(409) = 0 (FRONTIER §2.1). So D4 extracts *Type II*
certificates. Its (★)-extraction is defined only on the sub-family above.

**KT2 outcome.**
* *Excluded as scoped* (type I / unsound / blocked): D1n; D2 with polynomial ε (2V hypotheses); D4; D6; D8; and D7
  restricted to ES-pair, data-determined or affine extraction.
* *Unresolved*: D1e, D2 with general ε, D3 in higher genus, D5, D7 with general ε, D9.

The classifications in this catalogue are **Assessments** built on the scoped lemmas. They do not prove that all
possible engines are dead.

**No design has a working engine.** The pre-registered strong outcome "every design in (a)–(c)" did *not* occur.

## 6. Necessary conditions (scoped) and where the open space is

**Prop Nec (PROVED as the conjunction of the cited results).** Let 𝔖 be a sound realisation scheme for (★)
(Type II, (S∃)) with engine E.
* (i) If ε factors through an ES pair (X, G) at p ≡ 1 (4), then G has an element of order pk, k ≥ 2 (Corollary Ord).
  E cannot be confined to groups with p-group centralisers of p-elements, which includes SWZ's.
* (ii) If the realisations have prime-to-p monodromy, a char-p construction produces exactly the char-0
  realisations (Theorem T).
* (iii) In the Wewers setting — three-point G-covers with p ∥ |G| lifted from special G-maps — the lifted signature
  is read off the char-p datum (Z65 Prop O). So a certificate *read as the signature* must already be in the char-p
  construction.
* (iv) If ε is data-determined, 𝔖 is a deterministic witness rule (DD); polynomial rules are barred on square
  classes.
* (v) By Remark 1.1, E's hypotheses must fail at every odd square.

Among the verified engines:
* SWZ satisfies (v) (degree = p), but (i) excludes ES-pair extraction from its groups.
* Wewers lifting does **not** reach the cyclic Lemma-F covers. By Z65_LIFT Prop E their marked stable reduction is
  exceptional (σ = 1 at the tame point), so they are not lifts of special G-maps. (The checkpoint version said the
  opposite; that was wrong.) Prop O is used only within its own hypotheses.
* CPZ / Petronio are realisable at admissible squares (Lemma N).

**ES pairs outside the Wewers setting exist (PROVED; supplied by the reviewer).** Let (X, G) be an ES pair of genus
g ≥ 2 and Γ its orbifold group. The subgroup K = ker(π₁(X) → H₁(X, 𝔽_p)) is characteristic in π₁(X) ⊲ Γ, hence
normal in Γ. So X̃ = ℍ/K is an unramified (C_p)^{2g}-cover of X on which G̃ = Γ/K acts, with
1 → (C_p)^{2g} → G̃ → G → 1. Both 2g − 2 and |G| are multiplied by p^{2g}, so the ES ratio and the signature are
preserved.

Example: at p = 5 the cyclic C₁₀ pair of signature (2, 5, 10) has genus 2. Its mod-5 homology cover has genus 626 and
group order 6250 ⊇ (C₅)⁴, and 6250·(5 − 4) = 5·(2·626 − 2).

So ES pairs with non-cyclic Sylow p-subgroups exist. The special-map / cyclic-Sylow results cited here
(Raynaud–Wewers, Obus) do not apply to them; this is not a claim that no lifting theorem could. The
signature, however, is still the original triple: such pairs give no new certificates.

### 6.1 Where characteristic p creates integers (Assessment)
Integers that are *outputs* of char-p constructions:
* new-tail invariants σ_new of a stable reduction (in (1/m_G)ℤ, m_G | p − 1 when p ∥ |G|; Obus Lemma 3.5 as used in
  Z65 Prop E), subject to the vanishing-cycle sum;
* congruences forced by a geometric condition (Z65 Thm G: potentially good reduction forces 3m − 1 = p);
* p-ranks / Hasse–Witt data.

In the Wewers setting none of these enters the lifted *signature* (Prop O). Whether they could feed a different,
realisation-dependent extraction is **not** settled here. (The checkpoint version's broader claim — that every lifted
discrete invariant is read off the datum, and that stabilisers specialise without change — was unsupported and is
withdrawn.)

*Assessment.* An (H★) of SWZ type would need a char-p construction whose output (not input) contains the integer k
of an element of order pk, or (★)-data directly. No such construction is known.

## 7. Kill tests, screens, verdict, FRONTIER text, bottom line

**Kill tests (pre-registered at checkpoint 1, commit 60f4c4f56).**
* **KT1 (kill Theorem Ord): PASSED.** 8 334 representations, p ≤ 3000, 0 exceptions (CERTIFIED).
* **KT2 (design decision rule): did not reach the strong outcome.** No design has a working engine, but five are
  unresolved rather than excluded (§5).
* **KT3 (block design, naked): FIRED** (census CERTIFIED; domain-valid failures at n = 7, N = 29 via Wang et al., and
  for the dihedral family at n = 9, N = 37 unconditionally).

**FRONTIER §4 hard screens for the best item (Theorem Ord as a screening tool).**

| screen | pass/fail |
|---|---|
| T1 squares | Remark 1.1 + Prop Nec (v): the engine's hypotheses must fail at m²; no engine examined has one that also comes with a working extraction |
| 8/131 (numerator 8) | Theorem Ord_k is numerator-uniform for p > k; nothing separates C even from C odd. Fails as a route; neutral as a screen |
| tied modulus | D1/D6 make the tie a block size or an isogeny degree mod 4C. Naked block data cannot see the class (K-block); one element of type [L^m, 1] forces the class +1 |
| fixed p | Theorem Ord and Theorem T are pointwise at fixed p; no engine produces a certificate at a fixed p |

**Verdict: NARROWED.** No HOT LEAD.
* *Strengthened (small, PROVED):*
  * Theorem Ord / Ord_k (every ES pair needs an element of order pk, k ≥ 2; anti-SWZ centraliser obstruction);
  * Theorem T (prime-to-p transparency for realisation schemes);
  * Prop Aff (three-case parametrisation);
  * Prop CPZ-T1 (one-way; T1 as a norm statement for all C);
  * Lemma 2V;
  * Lemma Split ((★) a proper sub-family);
  * Lemma K-block for naked schemes;
  * the homology-cover construction of ES pairs with p² | |G| (reviewer).
* *Excluded as scoped:* naked block schemes; polynomial extraction from two-square realisations; ES-pair extraction
  in groups with p-group centralisers; prime-to-p char-p constructions beyond Riemann existence; the Euclidean
  families as degree-indexed data.
* *Unresolved:* block-equipped schemes, higher-genus lifting-invariant designs, the Γ₀(p)-dessin size bound, general
  extraction from degree-p covers, non-polynomial extraction from two-square realisations, Abhyankar-type
  constructions, and ES pairs outside the Wewers setting.

**Proposed FRONTIER text (z66 block; not applied here).**
> *(z66 HSTAR, `Z66_HSTAR.md`; internal.)* The missing lemma (H★) of Z65_LIFT was formalised as a sound realisation
> scheme plus an existence engine. F1 is automatic for sound schemes, so the screen bites on the engine.
>
> Results:
> * PROVED: every 3-term representation of 4/p (and of k/p, p > k ≥ 4) has a denominator pk with k ≥ 2. So every
>   ES pair contains an element of order pk, and no group whose p-elements have p-group centralisers carries one:
>   S_p, A_p, transitive groups of degree p, AGL₁(p), PSL₂(p). This is precisely the structure through which
>   Song–Wen–Zhang's prime-degree engine uses primality.
> * Prime-to-p realisation schemes gain no realisations from characteristic p (Grothendieck). This is a statement
>   about realisation sets, not a ban on new characteristic-p proofs.
> * The verified arithmetic Hurwitz families (Corvaja–Petronio–Zannier, Petronio) realise norm conditions and are
>   realisable at every admissible odd square. T1 is a norm statement (4Cm² + 1 = N(1 + 2m√−C)), and every failure
>   of (★)_1(n) makes the CPZ datum at 4n + 1 realisable (one-way).
> * Polynomial identities in (x, y), p = x² + y², positive and integral on a full residue coset, give only
>   congruence menus. Non-polynomial extraction is unresolved.
> * Fixed-shape "naked" block data at degree 4Cn + 1 are realisable at prime 4Cn + 1 (dihedral family
>   unconditionally; general shapes unconditionally to 31, conditionally on SWZ beyond), hence unsound.
>
> No design screened has a working engine. Block-equipped schemes, higher-genus lifting invariants, general
> extraction from degree-p covers and ES pairs with non-cyclic Sylow p-subgroups (which exist, via homology covers)
> remain unexcluded.

**Bottom line.** The brief asked for a Hurwitz-type realisation problem with p-determined data that fails at squares
and is solvable by characteristic-p or group-theoretic methods. Soundness alone makes any certificate-producing
scheme fail at squares, so the question is the engine. What is now proved:
* The one engine whose hypotheses fail at squares for a structural reason, prime-degree Hurwitz (SWZ), works in
  groups whose p-elements are self-centralising, and no ES pair lives in such a group.
* Prime-to-p constructions in characteristic p realise nothing new (as sets of realisations; new *proofs* are not
  excluded).
* The verified arithmetic Hurwitz families see *norms*. They are realisable at admissible squares, and they detect
  failures of (★)_1, not its solutions.
* Naked block data detect *a* divisor, not one in the class −1 (mod 4C).

What is not excluded: schemes whose realisations carry extra structure (block systems, lifting invariants in higher
genus, size-bounded dessin loops), general extraction from degree-p covers, non-polynomial extraction from (x, y),
and constructions outside the Wewers setting. The scheme definition is semantic (the tautological scheme
𝒟(n) = n, Real = Cert, ε = id qualifies), so the content always lies in an independently proved engine. For none of these is a working engine known. This is a narrowing, not a closure.

## 8. Sources (✔ = re-read by me; V/V2 = verified by research subagent, see `data/z66/hstar/src/`)
* ✔ Obus, *Lifting of curves with automorphisms*, arXiv:1703.01191v2 (Adv. Lect. Math. 46 (2019) 9–59): Thm 1.5
  (tame Riemann existence converse; cites SGA1 XIII Cor 2.12), Rem 1.9 (prime-to-p π₁ isomorphism).
* ✔ (abstract; PDF §3.3–§4) Wang, Li, Zhou, Wei, Ye, Shi, Xu, arXiv:2512.06545v2: complete list of non-realisable
  3-point partition triples for d ≤ 31; prime-degree conjecture verified for primes < 32; Types 0–III, with Type II =
  Wei–Wu–Xu's common-divisor criterion.
* V Corvaja–Petronio–Zannier, Elem. Math. 67 (2012) 169–181, arXiv:0810.0591, Thm 1.1.
* V Petronio, Winter Braids LN 7 (2020), Exposé 2, Thms 3.13, 3.14 (the reviewer also checked the PDF).
* V Pakovich, JKTR 18 (2009) 271–302, Thm 1.1 (Laurent passports). V Pervova–Petronio, AGT 6 (2006), Props 1.2–1.3,
  Thms 1.4–1.5. V2 EKS 1984 Prop 5.7 (via Pervova–Petronio).
* V Fried, Israel J. Math. 179 (2010) (page range not verified), arXiv:math/0611591: Thm 1.2, Thm 1.3, Cor 2.3
  (genus-0 lifting invariant; attributed to Serre 1990, V2).
* V Obus, arXiv:1208.3909v3 Thm 5.2 (good reduction, cyclic p-Sylow; Raynaud 1999 Thm 0 V2).
* NOT FOUND (not used): Kani's anti-isometry reducibility criterion; Singerman's inclusion list; EEK torsion-free
  index theorem.
* In-repo: Z65_LIFT (Lemma P, Prop O, Prop E, Lemma S, Thm G), Z64_EQUIV (Lemma A, E10, §5 types), Z58_STRUCT
  (Thm A), Z58_WILDCARD, `BRAINSTORM/bsB_zolotarev_transpose.md`, Z63_EUCLID, Z60_RAYCLASS.

## 9. Review log
**Hostile deep review** (`review` tool, deep mode; the reviewer ran as openai/gpt-6-astra; no provider error; on
commits 60f4c4f56..e4b3b63c8). Verdict: MAJOR REVISION; no FATAL (ES/(MS) never claimed).

*Verified by the reviewer:*
* Theorem Ord / Ord_k case analysis and the centraliser list;
* Theorem T's core statement against Obus Thm 1.5 / Rem 1.9;
* the general-C norm argument and the oddness of χ_{−4C};
* Lemma 2V exhaustiveness (no missing case);
* both scripts rerun (census N = 4–10 byte-identical; Ord check at 1000 and 3000).

*Findings and fixes (all applied):*
1. **MAJOR.** The Spec theorem imposed p ∥ |G| without justification, and the "non-cyclic Sylow ES pairs unsettled"
   claim missed the homology-cover construction. → Spec replaced by Prop Nec, scoped to the Wewers setting; the
   construction and the p = 5 example (genus 626, order 6250) added in §6.
2. **MAJOR.** §6.1's generalised transparency was unsupported. → Withdrawn; §6.1 now says what is not settled.
3. **MAJOR.** Prop Aff missed the all-translation case (([p],[p],[p]) has p − 2 classes). → Three-case
   parametrisation; the "type I" wording replaced by "elementary, engine superfluous".
4. **MAJOR.** T, DD and Pos were over-interpreted into no-go statements. → Each is re-scoped (T: prime-to-p
   monodromy, realisation sets; DD: witness rule, Π⁰₁ only under computability; Pos: unrestricted equation only).
   D3 (higher genus), D5 and D7 (general ε) are reclassified as unresolved; the Fried "r ≥ n" sentence is removed.
5. **MAJOR.** K-block was narrower than claimed, and the KT3 witnesses were outside the domain. → Naked vs
   block-equipped schemes separated; domain-valid witnesses n = 7 (N = 29) and n = 9 (N = 37, dihedral,
   unconditional); the "incompatible ⟹ type I" claim withdrawn.
6. **MAJOR.** Lemma N was false for the Eisenstein families at 3 | m. → "Every admissible odd square" (3 ∤ m), with
   the degree-indexing caveat.
7. **MAJOR.** CPZ-T1 had been strengthened into an obstruction/existence dichotomy; n = 11 refutes the converse. →
   One-way statement only; readings rewritten.
8. **MAJOR.** Lemma Split's "(★) is the cyclic case" was false (p = 409, K = C₂₃₄). → (★) is a proper sub-family;
   generator normalisation and trivial marked points specified.

**Cross-model review** (`data/z66/xreview/REVIEW_HSTAR.md`; verdict ACCEPT-WITH-FIXES; no provider errors).
The reviewer independently re-derived Ord/Ord_k, Corollary Ord, Theorem T (against Obus), N, CPZ-T1, 2V, K-block,
Split and the homology cover. It reproduced KT1 and the census (N = 4–8 byte-identical), plus an independent
all-block-subsets check at N = 4–6. Fixed:
1. **WRONG → fixed.** §6's "Wewers lifting reaches the cyclic Lemma-F covers" contradicted Z65 Prop E. It is
   replaced by the correct statement: they are exceptional and are not lifts of special G-maps. "No lifting theory
   covers non-cyclic Sylow" is narrowed to "the cited special-map/cyclic-Sylow results do not apply" (§0, §6).
2. D2 with general (non-polynomial) ε is now **unresolved**. 2V's identity and full-coset positivity/integrality
   hypotheses are carried into the scope, the catalogue and the FRONTIER text. T's "sets, not proofs" scope is added
   to the bottom line and the FRONTIER text.
3. DD: decidability and checkability for Π⁰₁; square-obstructed target and polynomial-identity hypotheses (not ES)
   in the barrier bullet; "witness rule, not automatically a supplied certificate". Aff: labelled non-identity
   cycles, all a_i ≠ 1 in the no-translation case, and the b₂ = 1 − a₂ → 1 normalisation. Split: p ≥ 5 and the
   triangle hypothesis. D3: genus-0 sign via Fried Cor 2.3 is a witness rule; Thm 1.3 concerns only 3-cycle classes.
4. The scheme definition is stated as semantic (with the tautological example). Catalogue/KT2 classifications are
   labelled Assessment. F3's "no special Hurwitz meaning" is labelled Assessment. Verdict stays NARROWED.

*Minor fixes (internal review):*
* Lemma 2V: ties, even degrees, and removal of an impossible listed case.
* p > k carried for numerator 8 (8/7 counterexample).
* (S∃) defined separately from (S).
* The KT1 script now exits non-zero on failure.
* The Fried bibliographic page range is normalised.
