# R273 — hostile review of O261 (B2_ACROSS_FIELDS.md, BRAINSTORM/z31_*.md, sources/lit2026g/)

Reviewer: R273 side agent (branch side-agent/review-b2-fields), merged side-agent/b2-across-fields at review start.
Status: in progress (claims written one at a time).

## Claim (1) — headline: Zaremba claimed proved pointwise (Shkredov 2603.14116 Cor 1; X. Zhang 2605.02518 Thm 1.2)

**Verdict: SOUND** (as a literature report; label "claimed, 2026 preprints, proofs not checked" is the right grade).

What I checked independently (fresh downloads of export.arxiv.org abs pages and arXiv PDFs, pdftotext, 2026-10-17/18):
* **arXiv:2603.14116** exists: I. D. Shkredov, "On some results of Korobov and Larcher and Zaremba's conjecture";
  v1 14 Mar 2026, **v2 24 Jun 2026 (latest version; no v3)**. v2 comment: "41 pages. 1. Some minor typos have been corrected,
  and clarifications have been made. 2. … the proof of technical Lemma 32 has been broken down into three auxiliary lemmas,
  simplified, and clarified. 3. In the appendix, we provide a crude upper bound for the absolute constant M in the case of a
  prime denominator". Not withdrawn. Verbatim (v2 p. 2, l. 65–69 of pdftotext):
  > Corollary 1. There is an absolute constant M ⩾ 2 such that for any prime (or square–free) number p there exists a,
  > (a, p) = 1 such that a/p = [0; c1, …, cs], cj ⩽ M, j = 1, …, s.
  Abstract: "We prove, in particular, the well-known Zaremba conjecture … for any prime denominator." Thm 8 (all M ≥ M₀,
  all q ∈ Z: ≥ q^{2w_M−1−o(1)} numerators with cj ≤ 100M) matches the excerpt file.
* **arXiv:2605.02518** exists: Xin Zhang, "Expansion in SL₂(ℤ/qℤ) and Zaremba's conjecture"; v1 4 May 2026, **v2 8 May 2026
  (latest; comment "Typos in v1 corrected")**. Verbatim: "In this paper we prove / Theorem 1.2. Zaremba's conjecture holds."
  with Conjecture 1.1 = "∃ M ∀ q ∈ ℕ ∃ a < q, gcd(a, q) = 1, all partial quotients ≤ M". Remark 1.3: M effectively computable
  but large.
* **Disputes / reception:** web search found no withdrawal, erratum or published objection. Positive signals: Shkredov v2
  itself cites Zhang ([64]: "now possess a proof of Zaremba's conjecture in full generality"); A. Kontorovich (X, 5 May 2026)
  publicly announced Zhang's proof "based on a breakthrough of Ilya Shkredov"; Stanford seminar (3 Jun 2026); Google Scholar
  "cited by 3" for Shkredov. Still unrefereed as far as I could find → "claimed" is correct.
* **Mechanism (from the papers, Zhang §4 outline + Shkredov §§1,3–4):** Diophantine reformulation (MMS26 Lemma 2): bounded
  partial quotients ⟺ x‖ax/q‖·q ≫ q/M for all 1 ≤ x < q. Small x (< t) are controlled by a ∈ Z_M(t), a Cantor/Ahlfors–David set
  containing K = Λ₁ ∔ [1, N] with |Λ₁| ≍ t^{2w_M}, t²N ≍ q, t ≈ q^{1/2−τ}; large x by a⁻¹ (mod q) ∈ Z_M(t). So one counts
  a ∈ K ∩ K⁻¹, i.e. solutions of (a + 2j)(b + 2j) ≡ 1 (mod q) — an equation g_j·a = −b for g_j ∈ SL₂(ℤ/q) with a generating set of
  size ≈ q^{2τ} (Zhang Rem 1.4: this is why Bourgain–Varjú does not suffice and a Helfgott-type product theorem for general q
  is needed). The remaining middle range x ∈ [t, q/(4Mt)] is handled by Shkredov's "critical denominators" Diophantine idea.
  Expected count |K|²/q ≍ q^{2w_M−1} = q^{1−O(1/M)}.
  The author's summary ("growth in SL₂(ℤ/qℤ) on two Cantor half-sets of size q^{w_M}, count q^{2w_M−1}") is accurate.

Defects:
1. **MINOR** (B2_ACROSS_FIELDS §4.1 / table row 1): Zhang's theorem is *not independent* of Shkredov — Zhang supplies the
   SL₂(ℤ/qℤ) growth input (his Thm 3.6) and explicitly runs "the framework provided by the proof of Theorem 8 in [Shk26]".
   A gap in Shkredov's Thm 8 framework would sink both. Repair: add "(Zhang = Shkredov's Thm 8 framework + new expansion for
   general q; not an independent proof)".
2. **MINOR** (§4.1): the mechanism summary omits the middle range x ∈ [t, q/(4Mt)] (Shkredov's new "critical denominators"
   idea) — this, not the growth input alone, is what makes M absolute rather than O(log q/log log q) (MMS26). Relevant for the
   "M1+M2" attribution in §5: the pointwise theorem also needs an Ahlfors–David *structure* input, which the §5 spark already
   hints at. Repair: one sentence.
3. **MINOR** (§6 ledger): record arXiv version status (Shkredov v2 24 Jun 2026, Zhang v2 8 May 2026, latest as of
   2026-10-18; not withdrawn; unrefereed).
