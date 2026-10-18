# AGENT_REPORT_O266 — Zaremba 2026 growth method → ES in CF coordinates (spark relay on O261)

Branch side-agent/zaremba-transfer (merged side-agent/b2-across-fields first). Main file `ZAREMBA_TRANSFER.md`; memos
`BRAINSTORM/z36_*.md` (7, indexed in BRAINSTORM/README.md); scripts `scripts/z36_*.py`; source excerpts
`sources/lit2026g/{z36_shkredov_zhang_method,rickards_stange,chang_partial_quotients}.txt`.
**ES is not solved; no infinite case is claimed.** The 2026 preprints are unrefereed; every use is labelled CONDITIONAL.

## SHARP:
1. **T1 has a published thin-orbit home: Rickards–Stange reciprocity obstructions** (arXiv:2401.01860, Duke Math. J. 2025;
   new to the campaign, which knew only the Apollonian HKRS case). Same source (Kronecker symbol invariant along CF/Euclid
   moves ↔ DEDEKIND_ES Cor 4.1), same obstruction ("symbol −1 ⇒ never a square" ↔ T1 via Thm 4.5/Prop 3.1), same
   conjectural shape ("every non-square beyond an explicit bound": RS Conj 2.15 n > 10569, Conj 2.22 v > 7.97·10¹² ↔
   DEDEKIND 4.4 n > 28225). RS *prove* the fat case (Ψ, δ = 1: Thm 2.8, all n except squares and 15 sporadic values) by a
   lattice line with ≍ n points + Pólya–Vinogradov — and refute Bourgain–Kontorovich's alphabet local–global conjecture
   (Thm 2.20). ES-five = the length-3 (dimension-0, hyperbola instead of line) truncation. ZAREMBA_TRANSFER §5.
   Spawnable spark: **Question R** — for finitely generated Γ ⊆ Ψ with δ > 1 − κ/8 (RS Thm 2.10), can growth methods prove
   that every large admissible non-square prime is a denominator? (first thin-orbit local–global with a reciprocity
   obstruction; requires keeping the middle window inside Γ and a main term vanishing at squares).
2. **The method's true input is density, not a power count ("M1⁺")**: Shkredov needs |A|N^κ ≫ q with ε < 1/18 ⇒
   1 − w ≤ κ/8 (κ ≥ 2^{−1656}, M = 22000). Zaremba-5 has a power count q^{0.67} and is still out of reach (Zhang Rem 1.3).

## Main results (labels)
* **Ladder (§2).** ES-five ⟺ λ(p) ≤ 3 (DEDEKIND Cor 4.6). |S_L(p)| polylog for fixed L (121 words at L = 3, p ≈ 10⁶),
  p^{θ} for L = c log p (θ(1) ≈ 0.85). EVIDENCE.
* **Theorem A (PROVED, elementary, self-contained proof; KNOWN in substance — Chang Thm 5 / Larcher, primitive roots are
  non-residues):** λ(p) ≤ 1 + 10(1 + log p)(1 + log⌈10(1 + log p)⌉). Inequalities checked at p = 11…10⁶; bound vs
  witnesses at all 78 495 primes ≤ 10⁶, 0 violations; odd squares: no Jacobi −1 at all.
* **Lemma C / D (PROVED):** tuv − u − v = p ⟺ t ≡ ū + v̄ (mod p) & tuv − u − v < 2p; enlarging the region only certifies
  multiples kp (ES(kp) ⇐ ES(k)), so the "alphabet knob" is vacuous; ES-five is the origin-box degenerate case of
  Shkredov's Lemma 15 / Zhang (3.4).
* **Hypothesis ZQ_M** (non-residue with all digits ≤ M; EVIDENCE: ZQ₄ for all primes < 2·10⁴, ZQ₃ except 277, windows at
  10⁵, 10⁶) ⟹ **Theorem B (CONDITIONAL)** λ(p) ≤ 1.04 M log p + O(M): the 2026 machinery, even χ-twisted, would buy only the
  log log p factor over Theorem A (Chang's open question).
* **Why the preprints don't give ZQ (Assessment):** window conflict ε < 1/18 (gluing intervals < q^{1/9}) vs Burgess ε > 1/8;
  Zaremba holds at squares, ZQ fails there, so growth alone cannot prove it; Zaremba(M) ⟹ ZQ_{4Mn_p} only (PROVED
  reduction via Shk Lemma 10).
* **Numerator-free rung** (drop χ, keep L = 3) = Lorenzini's (W), already in the campaign ((J)15, bsG_even_half); my
  recount: 12 exceptions ≤ 2·10⁶, max 510. No new claim.

## Answer to the brief's goals
(1) extracted (§1, memo z36_density_threshold). (2) least power-count rung: L ≍ ε log p; least rung the method could
touch: L ≥ C₀ log p with C₀ astronomically large, and only with a χ-twist that does not exist; least *theorem* rung:
L ≍ log p log log p (pigeonhole). Gap to L = 3 quantified (density ≍ 1 vs ≍ log² p certificates). No pointwise theorem
below log p log log p obtained. (3) no semigroup/product substitute for M1⁺ (Lemma D; Euclid recursion returns B2).
(4) numerics as above; T1 controls at 997² and all odd squares ≤ 10⁶.

## Sparks (not pursued)
* Question R above (RS thin semigroups + growth + reciprocity main term).
* χ-twisted Zaremba (ZQ_M) as a stand-alone problem: needs character cancellation on glued Cantor sets at scale < q^{1/4};
  maybe via Salié-sum completion of the twisted Lemma 14 count Σ χ(a + 2j) 1[(a+2j)(b+2j) ≡ 1].
* "Reciprocity singular series": for ES slices, predict a₀(n) + a_T(n) by a main term carrying a factor (1 − χ-type) that
  vanishes at squares; compare with RS Table 1 structure; test whether the ES five-slice deficit near squares ((J)53/(J)55)
  matches a reciprocity main term.
* Is the ES five-slice family literally a length-3 sub-family of an RS Ψ-type orbit (explicit matrix embedding with a
  fixed seed)? I stated the dictionary at the level of invariants only.
