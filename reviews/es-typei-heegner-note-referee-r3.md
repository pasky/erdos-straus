# Referee report R122 (round 3) — paper/es-typei-heegner-note.tex, O122 revision

Referee: hostile side agent R122. Base: `side-agent/heegner-note-v3` @ a528abf (merged into
`side-agent/referee-heegner-r3`). Scope (brief): the unconditional Main Theorem (Σ_{p≤N} f_I(p) ≪ N log²N relative
to (B1)–(B5)), Appendix A (effective DI Thm 7 / Drappeau Lemma 4.10), completeness/honesty of (B1)–(B5), Cor 9.1
"a character" vs even χ, Thm A.4 growth, the corrections list, status framing, internal consistency.
From-scratch checks: `scripts/review_r122_checks.py` (all pass; see §C). Drappeau checked against
`sources/o116/drappeau-1504.05549.pdf` (arXiv v-numbering); DI not available as a source PDF here — DI locators are
taken on trust from the earlier reviews (R118, R121A/B), which had the scan.

## A. Verdicts per claim

| Claim | Verdict |
|---|---|
| Prop A.3 (effective (8.19) with nebentypus, branches A, B, C1, C2) | **SOUND** (re-derived line by line; numerals checked) |
| Thm A.4 (effective DI Thm 7 / Dr Lemma 4.10, incl. growth with H ∋ 200cK₁) | **SOUND** (growth re-derived here, see §B.3; repaired text) |
| Lemma A.2 (toolkit a, b, c) | **SOUND** (re-derived; (a) "class E(B log2+o(1))" made precise, R122 repair) |
| (M), (PS) | **SOUND** (re-derived; PS randomly tested, worst ratio 0.84 ≤ 2) |
| Props A.5–A.7 (effective Thm 2, Thm 14, Lemma 8.1) | **NOT RE-DERIVED here** (statements + pointers only in the paper; derivations in `scripts/ttl3_*.md`, reviewed R121A/B, RA–RC). Constant arithmetic in §A.5 checked. |
| Thm A.1 / Thm 9.8 (EFF) | **SOUND-AFTER-REPAIRS** (conversion K vs K² slip, m3) relative to (B1)–(B5) and the TTL3 derivation files |
| Thm 9.9(ii) = Theorem 1 (≪ N log²N) | **SOUND** relative to cited inputs + Thm 9.8 (bookkeeping in ε, w_N re-checked) |
| Thm 9.9(i) = Theorem 2, (iii) | **SOUND** relative to the published DI7/Dr4.10 *read as uniform in q₀* (the reading is flagged in the intro; abstract now says so, R122 repair) |
| (B1)–(B5) list | **SOUND-AFTER-REPAIRS**: complete as far as I can see for the appendix (residual spectrum is listed separately in the intro); (B3) needed the "not certified / Dr only sketches the proof" caveat in the intro list (M1) |
| Cor 9.1 "a character" | **SOUND-AFTER-REPAIRS** (m1: now "even", which is all that is used) |
| §A.6 corrections list | **SOUND** as attributed/hedged (Dr items checked against the PDF where possible, §B.5) |
| Abstract/intro status | **SOUND-AFTER-REPAIRS** (M1, m2, m4) |
| Internal consistency (old conditional remnants) | one remnant repaired (m5); MN-note numbering unchanged per author (not re-checked against the MN note) |

No FATAL. One MAJOR (honesty of the (B3) statement in the intro, repaired). Recommendation: §E.

## B. Line-by-line notes

### B.1 Prop A.3 (re-derived)
(A) Q ≤ Q₀: (M) with Y′=1 gives Y^{1/2}·K₂(Q+N^{1+δ})N ≤ Q^{1−δ}N^{−1/2}·2K₂Q^{1+δ}N = 2K₂Q²N^{1/2} ≤ 2K₂Q₀Q^{1+4δ}N
(uses Q ≤ Q₀, N ≥ 1) ✓. (B) Y < Q ≤ Y₁=Q+N, so (M) is monotone only; (NY₁)^δ ≤ (2Q²)^δ, Q+N+Y₁ ≤ 4Q, 4·2^{0.1} ≤ 10 ✓.
(C) Q^{2δ} ≥ 2π from Q₀; C = πQ^{1−2δ}/q₀ ≤ Q/2; QYN = Q^{3−2δ}, NY/Q = Q^{1−2δ}, error ≤ 3cQ^{1+3δ}N ✓.
(C1) C ≥ N ≥ 1 and C ≤ Q/2, so the induction hypothesis (claim for Q ≤ 2^{k−1}Q₀) applies at (C,N); Y_C ≤ Y so (M)
gives (Q/C)^{1−δ}; (PS) gives 2(1+t²); ∫(1+t²)/(1+t⁴) = √2π (checked numerically);
2√2π·π^{5δ} ≤ 15.8 ≤ 45 for δ ≤ 1/10; Q^{10δ²} ≥ 90c from Q₀ ✓.
(C2) Y ≥ Q ≥ 2πN ≥ Y₁ = C+N ≥ 1, (M) and (P1) at C (P1 is for all Q>0, empty if 16C<1); worst numerical ratio 8.0 ≤ 10;
the t-integral via (PS) gives 2√2π·10 = 88.9 ≤ 90 ✓ (the text omits "(PS)" in (C2) but the factor 90 includes it).
Closing: H ≥ 200cK₁ ⇒ 90cK₁+3c ≤ H/2 ✓. Matches `scripts/ttl3_nebentypus.md` (which used the more generous 1000cK₁).

### B.2 Thm A.4 (re-derived)
Y ≤ Y₂: (M) + Prop A.3 ✓; Y > Y₂: (Y/Y₂)^{1/2}HQ^{1+4δ}N = HQ^{5δ}√(NY)N ✓ (Y₂ ≥ Q^{1−2δ} ≥ 1). N>Q or Q<1: (M) with
Y₁ ≤ 2N (resp. 1+N), the factor (1+√(Y/N)) covers both Y ≤ Y₁ and Y > Y₁ ✓.

### B.3 Growth of K₇ with H ∋ 200cK₁ (the author flagged it as borrowed) — re-derived
With L := e^{B/δ} ≥ e^{10}: log(200cK₁) ≤ log200 + 2L; log(10K₁) ≤ log10 + L;
log(2K₂Q₀) ≤ log2 + L + (log90 + L)/(10δ²) + δ^{−1}, and δ^{−2} ≤ e^{2/δ}/4 gives (L/(10δ²)) ≤ e^{(B+2)/δ}/40.
All three are ≤ e^{(B+3)/δ} since e^{1/δ} ≥ e^{10}. Grid check over B ∈ [1,3000], δ ∈ [10⁻³,0.1]: worst ratio 1e−12.
**SOUND.** Repair (R122): the proof now displays the 200cK₁ term explicitly instead of "as in Cor 2.3".

### B.4 Conversion (proof of Thm A.1)
Blocks (Q_i,16Q_i], Q_i ≥ 1/16, count ≤ 2+log M₀ ✓. (2M₀t)^{5δ}(2+log M₀) ≤ (12/ε)(M₀t)^ε with δ=ε/6 (via Lemma A.2(b) with
r=1): grid-checked, worst log-gap −1.47 ✓. Constant budget: 3·12/ε = 36/ε ≤ 200/ε ✓.
log log(200ε^{−1}K₇^χ(ε/6)) ≤ (24B_χ+30)/ε ✓; A₀ = 16728 < 2·10⁴ for B_W ≤ 3, C_W ≤ 10 ✓.
δ = ε/6 ≤ 1/24 ≤ 1/10 ✓. Chain K_{T2}(δ/4), K₁₄(δ/4), D(δ/4) → K₁,c ≤ exp(exp(405/δ)) → K₇ ≤ exp(exp(408/δ)) re-checked ✓;
twisted: 4B_χ ≥ 1600 ≥ 404 so the untwisted K₁₄ is absorbed ✓.

### B.5 Drappeau (checked against the PDF)
* Lemma 4.2 (p. ~9): `S_aa(m,n;c) ≪ (m,n,c)^{1/2} τ(c)^{O(1)} (cq₀)^{1/2}` — implied constant and the exponent O(1) are
  unspecified, and the proof is only sketched ("In the general case, one obtains"). (B3) correctly says "absolute
  C_W, B_W", but the *intro* list did not say they are uncertified (M1).
* §4.1: χ modulo q₀ | q, κ ∈ {0,1} with χ(−1) = (−1)^κ. So for odd χ Drappeau's forms have weight 1. The paper uses
  only even χ (Prop 9.4 applies Cor 9.1 with χ even mod q); Appendix A is stated for even χ. Cor 9.1's "a character"
  was therefore broader than what is proved in Appendix A (m1).
* Lemma 4.9/4.10 statements match the quotation in §9 (Q ≥ q₀, Y ≥ 1, interval sequence) ✓; "q₀ appears only with
  negative powers" remark ✓; after Lemma 4.10 Drappeau renames q → q₀q, so level q₀q ✓ (Appendix A convention).
* Lemma 4.5 is the Kuznetsov formula for Dirichlet characters ✓ (B1).
* Correction 6 items (S_∞∞ → S_χ, dx/x, index n, argument order) concern pp. 17–18; I could see the text but did not
  re-verify each typo individually; their attribution is hedged ("none affects the theorems") ✓.

### B.6 Theorem 9.9 bookkeeping
(ii) ε = w/64, w_N = 128A₀/log𝓛 ⇒ 64A₀/w = (log𝓛)/2 ⇒ log C_ε ≤ 𝓛^{1/2}; (11/64)δ𝓛 ≥ 22A₀𝓛/log𝓛 dominates
½𝓛^{1/2}+(C+1)log𝓛 for 𝓛 ≥ 𝓛₀(A₀) ✓. Strip cost (w_N𝓛+1)N𝓛log𝓛 ≪ A₀N𝓛² ✓. Uniformity of the implied
constants in ε: Prop 9.4 states its implied constant depends only on φ, W, uniformly in ε ≤ 1/4 ✓ (R118 area, not re-derived).

## C. From-scratch scripts
`scripts/review_r122_checks.py` (`uv run --with sympy --with mpmath`): Prop A.3 numerals over δ ∈ [10⁻⁴, 0.1] and a
(Q,N) grid; √2π integral; (PS) on 300 random weighted families; Thm A.4 growth (log-space grid); conversion inequalities;
K² ≤ 3log²(2t); A₀ value; Lemma A.2(a) for τ^B, n ≤ 2·10⁴; (a+1)2^{−aδ/B} ≤ 2B/δ; Lemma A.2(c) |h^{(p)}| ≤ 9^p(p!)² for
p ≤ 10 (worst ratio 0.90). ALL OK.

## D. Defects (with repairs applied, marked "(R122 repair)" in the .tex)

**M1 (MAJOR — honesty of a black box; intro list (B3), lines ~107–108).** The intro states (B3) as "a twisted Weil
bound with absolute constants [Dr, Lemma 4.2]" with no caveat. Drappeau's Lemma 4.2 has unspecified constant and
exponent (τ(c)^{O(1)}) and only a proof sketch; the appendix says the values are not certified, the intro (which is
what readers see) did not. *Repair applied:* intro (B3) now says the constants are absolute but unspecified in [Dr]
(proof sketched there), not certified here, and that only their finiteness enters Theorem 1. Appendix (B3) also notes
that Dr only sketches the proof.

**m1 (MINOR — Cor 9.1, line ~1780).** "χ a character modulo q₀" vs Appendix A / Thm 9.8 "even χ". In Drappeau odd χ
means weight 1, which Appendix A does not treat. *Repair applied:* Cor 9.1 now says "an even character" with a
remark that only even χ are used (Prop 9.4).

**m2 (MINOR — abstract).** The abstract did not say that Theorem 2's route reads Dr's ≪_ε as uniform in q₀, nor that
the long computations behind Appendix A are in internal derivation files. *Repair applied* (one clause each).

**m3 (MINOR — proof of Thm A.1).** "the ⌊log₂t⌋+1 ≤ 3log²(2t) closed intervals": Cauchy–Schwarz plus the sum over
intervals costs K², and what is needed is K² = (⌊log₂t⌋+1)² ≤ 3log²(2t) (true: K ≤ log(2t)/log2, 1/log²2 = 2.08).
*Repair applied.*

**m4 (MINOR — intro "Status and dependencies", and §A.7).** "Some fixed absolute numerical majorants were only
shape-checked; this affects the numerical value of A₀, not the result." This is correct only because the reviews
(R121B) checked structurally that no parameter (δ, Q, N, q₀, χ) enters those steps; the sentence should say so,
otherwise it overclaims. *Repair applied* in both places.

**m5 (MINOR — §10 Assessment 10.1, line ~2192).** Remnant "None enters the conditional proof" — there are now
unconditional proofs too. *Repair applied:* "None enters any proof in this note."

**m6 (MINOR — Lemma A.2(a)).** "(class E(B log2+o(1)))" is not a class statement (o(1) as δ→0). *Repair applied:*
"in particular of class E(2B) for 0<δ≤1/4" (checked: B2^{B/δ}log(2B/δ) ≤ e^{2B/δ}, grid worst gap −4.5 in log).

**m7 (MINOR — Thm A.4 proof, growth).** Borrowed "as in Cor 2.3"; re-derived (§B.3). *Repair applied:* the 200cK₁
term is now bounded explicitly in the proof.

**m8 (MINOR — Prop A.3 (C2), presentation).** The main-term bound 90cK₁ uses (PS) (factor 2(1+t²), integral √2π);
the text cites only (M) and (P1). *Repair applied:* "(M), (P1) at C and (PS)".

Not defects, but noted: Props A.5–A.7 are statements with mechanism summaries; their proofs live in
`scripts/ttl3_*.md`. The labels ("proved relative to … and [TTL3]") say this honestly. A journal version would need
those derivations in the paper.

## E. Recommendation
**Accept as an internal draft after the R122 repairs** (all applied; two clean pdflatex runs). Theorem 1
(≪ N log²N) is correctly labelled PROVED relative to the classical inputs (B1)–(B5), the inherited ET/MN3 reduction, and
the internal TTL3 derivation files; it is not externally refereed and the paper says so. Highest-value next step for
external credibility: write Props A.5–A.7 out in full (or in a supplementary appendix) and certify C_W, B_W.
