# REVIEW_LIFT — hostile review of `Z65_LIFT.md` (branch side-agent/z65-lift, head d751ce2ad), wave z65

Reviewer: Claude Opus. It stands in for the cross-model reviewer because the OpenAI/Codex token has expired, so this
is a *same-family* review. A truly cross-model pass is still owed if the infrastructure comes back. ES is OPEN.
Script: `scripts/z65_xrev_lift_check.py`. Scratch reruns: `/tmp/xrev_LIFT/`. Limits used: `ulimit -v 4000000`,
`timeout` on every command.

## 0. Sources verified
* **SWZ.** arXiv API: 2609.20572v1, "The Hurwitz existence problem in prime degree" (Song, Wen, Zhang;
  2026-09-17). I re-downloaded the PDF and it is **md5-identical** to `data/z65/lift/src/swz.pdf`. I checked M1–M5
  against my own pdftotext of it:
  * Thm 5.1: Henrio's moment criterion. It needs e_j ∈ F_p^× with Σ = 0 and no zero proper sub-sum.
  * Lemma 5.3: P_Λ′ = c∏(y − a_j)^{e_j−1}, which gives two branch values.
  * Lemma 5.5: σ = (r − 1)/(p − 1).
  * Lemma 4.7: tame inertia is preserved under lifting.
  * Thm 4.8: requires p ∥ |G|, B_wild = ∅ and three primitive tails, and invokes Wewers Cor 4.6.
  * Lemma 8.1: common regular P, N_{S_p}(P), v_p(p!) = 1.

  The extraction in §2.2 is **accurate**, and its "discrete data given / continuous problem over F̄_p" reading is fair.
* **Wewers, math/0205026** (memo's copy). Checked:
  * Lemma 1.4(1)–(4), stated under *mild* reduction; p ∥ |G| implies mildness.
  * Cor 1.11 (vanishing cycles), Def 2.1 (exceptional), Def 2.7 (special: σ < 2, σ ≠ 1, exactly three σ < 1).
* **Obus, 1208.3909.**
  * §1: if p divides some ramification index, the marked cover has bad reduction.
  * Lemma 3.5: σ_b > 0, σ_b ∈ (1/m_G)ℤ, and σ ≥ 1 + 1/m_G on new tails.
  * Thm 3.6: vanishing cycles for **cyclic p-Sylow**, r − 2 = Σ_new(σ − 1) + Σ_prim σ.
* **Hernández, 1112.2425 Thm 3.1.** Matches the memo: fpt = Σ⟨1/d_i⟩_L + p^{−L}.

## 1. Per-claim table

| claim | label | my check | verdict |
|---|---|---|---|
| Lemma A + Corollary (Z64_EQUIV E3): for p ≡ 1 (4), only signatures (0; x, y, z) with Σ1/· = 4/p | PROVED (z64) | Re-derived the h ≥ 1, r = 5 and r = 4 casework by hand. 4/p = 1/a + 1/b forces 4a′ − 1 = p, i.e. p ≡ 3 (4). Reran `z64_equiv_orbifold.py`: the sporadic list has no prime ≡ 1 (4). | CORRECT |
| G0: smooth model unique, G acts on it, G acts faithfully on X_k (H¹ + Lefschetz 2 − 2g < 0), Ô = R[[Z]], Serre I = P ⋊ C_m with i = 1 off P | standard | Each step checked. A smooth model with g ≥ 1 is the minimal regular model. Equivariant specialisation of H¹ gives L(g) = 2 − 2g < 0, while L(g) = #Fix ≥ 0 in char 0. | CORRECT |
| G1: g ∈ I∖1 has exactly i(g) fixed points in the residue disc, all simple | PROVED | G(Z) − Z reduces to order i(g); apply Weierstrass preparation over complete R. A multiple fixed point would mean g′(w) = 1, and in char 0 a finite-order automorphism with g′(w) = 1 is the identity. | CORRECT |
| G2(a),(b): cluster identities | PROVED | Stab(w) ≤ I, and orbit ∩ D is a single I-orbit of size \|I\|/e. Since P is the normal Sylow, S_w ∩ P has order π. Both double counts redone. | CORRECT |
| G3: cluster shapes | PROVED | Every nonzero term in (a) is ≥ 1/2. A wild singleton gives (\|P\|/π)(π − 1) < \|P\| ≤ 2(\|P\| − 1), and an empty wild cluster gives 0 on the left of (b); both are contradictions. | CORRECT |
| G4 valuation casework ⟹ (m, p, pm), p = 3m − 1 | PROVED | Every branch redone. Highlights: (i) \|W\| = 3, all p-powers: the count of exponents equal to B is ≢ 0 (mod p); (ii) a = b ≥ 2: D = 4p^{a−1} − 1 divides p + 4; (iii) a = b = 1: 3m − 1 \| p. | CORRECT |
| Converse: z^m = y^p − y, C_pm, g = (p − 1)(m − 1)/2, lifts by Sekiguchi–Oort–Suwa | PROVED | Char-p Riemann–Hurwitz redone: d_∞ = 2pm − m − 1 gives 2g − 2 = 3m² − 5m ✓. Checked the p = 5 model y² = x⁵ − 1 → Y² = t⁵ + āt ✓. G2 on this example holds with equality, (p − 1)(m + 1) ✓. | CORRECT-WITH-FIX (F2) |
| Corollary: every ES curve at p ≡ 1 (12) has bad reduction (all of 𝔐, the (★)-zeros) | PROVED | Follows directly. It applies to *any* (X, G), however X was constructed, so it covers lifts of a subgroup too. | CORRECT |
| Theorem G_k (k ≥ 4, p > k) | PROVED | Redone. Survivors satisfy (k − 1)m − 1 = p. The hypothesis p ∤ k(k − 1)(k − 2) is redundant given p > k. | CORRECT-WITH-FIX (F4) |
| KT1: 11 800 representations (p ≤ 1500) → 122 Mordell survivors, 0 others | CERTIFIED | Their script reran byte-identical. My script uses an independent test: the raw G2 (a)/(b) inequalities with \|P\| = p^t (t ≤ 3) and e′ \| m, not the G3 summary. It gives 11 800 / 122 / 0. Also clean for k = 5, 6, 7 (p ≤ 700) and k = 8 (p ≤ 1500), and no p² divides any denominator. | AGREE |
| KT3: numerator 8 | CERTIFIED | Reran identical. The memo's text is **miscounted**: the run has **38** identity triples (= #{p ≤ 1500 : p ≡ 6 (7)}) plus (2, 2, 7), i.e. 39 survivors in all, not "39 triples plus (2, 2, 7)". | CORRECT-WITH-FIX (F3) |
| Prop O: lifted indices are read off the special G-map (Lemma 1.4(3)(4)) | PROVED | Verified in the source. Close to tautological: it is the definition of a lift together with Lemma 1.4. | CORRECT |
| "(BR) adds no existence power" / type I / KT2 fired → DEAD as construction | Assessment / pre-registered rule | KT2 was pre-registered at 4c2ebc54d (an ancestor; text checked) and was applied as written. Caveat: Prop O does not exclude a *non-constructive* char-p existence proof of a datum whose invariants are forced. The memo concedes this in §7 scope and §5.3 (H★), so the label is honest. | ACCEPT (scoped) |
| Prop E: cyclic p-Sylow, bad reduction, m_G = 1 ⟹ exceptional; abelian Type II ⟹ σ_x = 1 | PROVED | The integer-σ argument is right. **Citation gap:** the proof uses Wewers Cor 1.11, which is stated under mild reduction (p-part of inertia ≤ p). For a cyclic p-Sylow of order ≥ p² the right source is Obus 1208.3909 Thm 3.6, already in the memo's sources. Also missing: *why* an abelian ES cover has a cyclic p-Sylow. In Type II, (ab)_p = 1 gives b_p = a_p⁻¹, so P = ⟨a_p⟩. | CORRECT-WITH-FIX (F1) |
| Remark: PSL₂(F_q) has m_G = 2, which "forces" σ_x = 1/2 plus a new tail with σ = 3/2 | remark | m_G = 2 only when p ∤ q; for q = p, m_G = (p − 1)/2. "Forces" also holds only outside the exceptional case. | FIX (F5) |
| Lemma S: the Galois closure of a three-point degree-p cover is not an ES curve with its monodromy group | PROVED | Case split redone: an element has p \| order iff it is a p-cycle; 3/p and 2/p have p-power denominators. The statement concerns the pair (X, Mon). X might be ES for a larger G ⊇ Mon, which Lemma S does not address. | CORRECT-WITH-FIX (F6, wording) |
| §5.4 fpt_p(x^d + y^d + z^d) = 4/p for d = (p + 1)/2 | PROVED + CERTIFIED | Digits of 2/(p + 1) are .1 (p − 2) repeating, so L = 1. Script reran identical (p < 2000). fpt ≤ lct = 6/(p + 1) ✓. Peripheral. | CORRECT |
| Chevalley "finite or cofinite" (§5.3) | PROVED | The image in Spec ℤ is constructible. | CORRECT |
| (H★) and the screened candidates | Assessment | Reasonable, and labelled as such. No overclaim. | OK |

## 2. Falsifier table (§1 of memo)
* **F1 (odd squares).** Correct: 3m − 1 ≡ 2 (mod 3), and squares are 0 or 1 mod 3.
* **F2 (numerator 8).** Correct apart from the KT3 count (F3 below).
* **F3 (composites).** Correct: the mechanism has no meaning at composite n.
* **F4.** "All 14 (★)-zero primes ≡ 1 (mod 3)" is ✓, but the entry is incomplete: it omits the **38 𝔊*-zero
  primes**. I checked them: all 38 are ≡ 1 (mod 12), so Theorem G's corollary covers them too. Add this.
* There is no HOT LEAD claim to break. The "T1-blind" characterisation is accurate.

## 3. Labels and overclaims
* ES status is stated as OPEN throughout. "DEAD" is scoped to the two lifting branches *as constructions* (§7) ✓.
* **Bottom line:** "is now completely classified" overreaches slightly. Theorem G classifies *signatures*. It does not
  show that every good-reduction ES curve is the cyclic z^m = y^p − y example. Say "classified at the level of
  signatures" (F2).
* The memo correctly records that the earlier internal review was a self-review (§9).

## 4. Required fixes, in priority order
1. **F1 (Prop E, citation and hypothesis).** Cite Obus 1208.3909 Thm 3.6 (vanishing cycles, cyclic p-Sylow) in
   place of, or alongside, Wewers Cor 1.11, which needs mild reduction. Alternatively restrict Prop E to p ∥ |G|.
   Add the one line: abelian Type II ⟹ b_p = a_p⁻¹ ⟹ P = ⟨a_p⟩ is cyclic, of order p because no denominator of
   4/p is divisible by p².

   The p² fact has a short proof that should go in:
   * Two terms with v_p = B ≥ 2 force x < p/3 and 1/b + 1/c = p(4x − p)/x > 2.
   * Three such terms would need 1/a + 1/b + 1/c = 4p^{B−1} > 3.
2. **F2 (scope of the converse and of the bottom line).** "G is cyclic of order pm, and the special fibre is
   z^m = y^p − y" describes the *constructed* examples; reword it that way. Reword "completely classified" to "classified
   at the level of signatures".
3. **F3 (KT3 count).** The KT3 run gives 38 triples with 7m = p + 1, plus (2, 2, 7), for 39 survivors in all. Fix §1
   F2 and §3.4.
4. **F4 (G_k).** Drop the redundant hypothesis p ∤ k(k − 1)(k − 2), or note that p > k implies it. (2, 2, 7) is
   excluded by p > k.
5. **F5 (PSL₂ remark).** Add "with p ∤ q" and "in the non-exceptional case".
6. **F6 (Lemma S wording).** Say "(X, Mon) is not an ES pair". Add the 38 𝔊*-zeros to the F4 row.

## 5. Verdict
**ACCEPT-WITH-FIXES.** Theorem G and G_k, Lemmas G1–G3, the valuation casework, the converse, the Corollary,
Prop O and Lemma S all re-derive correctly. The decisive numbers (KT1, KT3, fpt) reproduce: byte-identical reruns,
plus an independent G2-level check for k = 4…8. Prop E is correct but needs its vanishing-cycle citation fixed (F1).
None of the fixes changes a verdict. "DEAD as a construction route" follows from Theorem G together with Prop O and
the pre-registered KT2 rule, within the stated scope. (H★) is correctly left open. This is a same-family stand-in;
a genuinely cross-model review remains owed.
