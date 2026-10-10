# R126 — hostile review of O126 (GEOMETRY_ES.md, AGENT_REPORT_O126.md, scripts/geo_*.py)

Reviewer branch `side-agent/review-geometry`, merged `side-agent/geometry-es` at review start.
Sources checked against the actual text: BL = `sources/bright-loughran-1908.02526.pdf` (pdftotext),
ET = `sources/elsholtz-tao-1107.1010.pdf` (§2, Props 2.2/2.3/2.6, Lemma 2.8). Yamamoto 1965 NOT accessed.
From-scratch scripts: `scripts/review_geo_*.py` (no author code reused).

## Summary verdicts

| claim | verdict |
|---|---|
| §1 BL restatement (Lemmas 2.1–3.11, Thms 1.2, 1.5–1.9, Cors 1.3, 1.4, Rem 1.10, 3.12) | SOUND-AFTER-REPAIRS (D1, D2) |
| §1 "BM only obstruction for fixed n ⟺ ES(n)" | SOUND for n ≥ 2; FALSE at n = 1 (D1) |
| §2.1 nine rational lines, nodes, boundary | SOUND (verified symbolically, `review_geo_sym.py` (B)) |
| §2.2 Prop 2.1 toric model | SOUND — reviewer supplies the missing symbolic proof (see §R2) |
| §2.2 integral/positive points ↔ primitive s with 4s_i ∣ nS | SOUND |
| §2.3 Prop 2.2 matrix forms | SOUND (checked against ET (2.1)–(2.21), Props 2.2, 2.6) |
| §3.1 (F1)/(F2)/(F3) equations, splitness | SOUND (symbolic) |
| §3.1 α\|F1 = (n(n−4t), −w), α\|F2 = (−λ, −nZ) | SOUND (F2 had no proof — D4); verified at every place on 16622 solutions |
| §3.1 Br_vert = Br ℚ for (F1) | SOUND (sketch is adequate; D5 cosmetic) |
| §3.1 "only conic-bundle class on Bl_V Π̄ is H − V_k" | SOUND |
| Thm 3.1 | SOUND (= BL Lemma 3.10 + two trivial cases; no novelty, correctly attributed) |
| Prop 3.2 (statement) | SOUND; its use as "the structural reason" / "all conic bundles split" is a GAP (D3) |
| Cor 3.3 / "Aim (B) negative for every fibration" | SOUND for every fibration — but only via Thm 3.1 (real place), not via splitness; "n²-type bounds" wrong (D6) |
| §4.1 total family, m(s), ES(p) ⟺ ∃s: m(s) = p | SOUND |
| §4.2 S-integral reformulations | SOUND in substance; "𝒰₁(ℤ[1/p])⁺ infinite" unproved, "in general … finite set" overgeneralised (D7) |
| §4.3 X_d: signature (1,2), forms [f,4ad,de] of disc −4d, Spin/T with T = R¹ℚ(√−d), CT–Xu SA | SOUND |
| Prop 4.1 | SOUND-AFTER-REPAIRS: "Σ^I_{p,d}(ℤ) finite" is FALSE without c ≠ 0 (D8) |
| Cor 4.2 | SOUND as Assessment; the "PROVED" part needs a precise statement (D9) |
| §5.1 BL Cor 1.3 in ET coordinates (unit pair = (a,b)) | SOUND |
| Prop 5.1 (Type I ⇒ (−d/p) = −1; ⟺ BL's condition) | SOUND, PROVED; verified on all 11998 Type I solutions p < 2000; novelty: folklore (D10) |
| Prop 5.2 (Type II: (−d/f) = −1, (f/p) = −(−1/p), ⟺ BL) | SOUND, PROVED; verified on all 4624 Type II solutions p < 2000; = Yamamoto 1965 Lem 4 (D10) |
| "BM removes exactly the Type I levels with (−d/p) = +1, never a Type II level" | SOUND — and can be made a genuine local BM statement (remark R3) |
| d*(p) bounds (Burgess 1/(4√e), GRH log²p) | SOUND |
| §5.3 completeness bounds a ≤ √p/2 + 1 (II), a ≤ 3p/4d (I) | SOUND (re-derived; no solution p < 2000 violates them) |
| §5.3 fixed-level numbers | REPRODUCED EXACTLY by independent code (R4) |
| §6 scope table | SOUND except the Harpaz/SwD row (D3) |
| (SHT) ⇒ ES for p > p₀; labelled CONJECTURE-level, "not standard" | SOUND (label honest) |
| §7 | SOUND for n ≥ 2 (D1) |

## Defects

**D1 (MINOR, but a genuine error inherited from BL). n = 1 breaks Thm 1.8 and the §1 equivalence.**
Location: §0 bullet 1, §1 "What BL leave open" item 1, §7 bullet 1 ("BL Thm 1.8 says the BM set is non-empty
for **every** n"). BL state Thm 1.8 "for all n ∈ ℕ" (p. 4), but their proof (§3.8) needs a prime p | n for
Lemmas 3.6/3.7; for n = 1 there is none. In fact for n = 1: W₁ ≠ ∅ (the node 0 is integral; U₁(ℝ)⁺ ≠ ∅), and
by BL Lemmas 3.1, 3.5, 3.8 the invariant sum is inv_∞ = −1, inv_p = +1 for all finite p, so W₁^{Br} = ∅. Hence
for n = 1 "BM is the only obstruction" is TRUE (BM explains the failure) while ES(1) is FALSE: the claimed
"literal equivalence" fails at n = 1. (BL's own Thm 1.1 correctly says n ≥ 2.) Repair: say "for every n ≥ 2"
throughout; optionally remark that n = 1 is the one case where BM *does* obstruct (a nice sanity check).
For n ≥ 2 the equivalence is literally right, including positivity and the integral model:
𝒰_n(ℤ) ∩ (U_n(ℝ)⁺ × ∏𝒰_n(ℤ_p)) = U_n(ℕ) and BL p. 3 states ES ⟺ (1.3) for exactly this W.

**D2 (MINOR). BL Thm 1.9 misquoted.** Location: §1 bullet "Thm 1.9". BL Thm 1.9 is about
`U_n(ℚ) → U_n(𝔸_ℚ)^{Br}_•` (rational points, adelic space with π₀ at ∞), not `𝒰_n(ℤ) → …`. The substance
("BM is not the only obstruction to SA") is right. Repair: quote verbatim. Also BL's Lemma 3.10 is a *Lemma*
(the brief's "Prop 3.10" does not exist; the author's "Lemma 3.10" is right). All other BL citations
(Lemmas 2.1–2.4, Prop 2.5, 2.6, Cor 2.7, 2.9, Thm 1.7, Lemmas 3.1, 3.2, 3.4–3.8, 3.11, Thm 1.2, 1.5, Cor 1.3,
1.4, Rem 1.10, 3.12) match the PDF text.

**D3 (MAJOR — overclaimed scope/causality). Prop 3.2 does not show what §3.2, §0 and the §6 table use it for.**
Prop 3.2 (no non-constant map from a *whole* non-split torus T to V_n ≅ G_m²) is true, but a fibre C of an
arbitrary fibration of U_n need not lie in V_n: C ∩ V_n = C \ (L₁₂ ∪ L₂₃ ∪ L₃₁ ∪ E) can be a *punctured*
non-split torus, and punctured tori do have non-constant units (e.g. on T : x² − 2y² = 1, x − 1 is a unit on
T \ {(1,0)}; with two rational punctures the unit rank is 2 and embeddings into G_m² exist). So Prop 3.2 rules
out non-split torus curves only *inside V_n*, i.e. disjoint from the lines and E. Splitness was actually
proved only for the plane-conic bundles (F1)–(F3). Consequences:
* §6 row "Harpaz / Swinnerton-Dyer descent": "all conic bundles of U_n are split … (PROVED that the fibres
  split)" is not proved; only (F1)–(F3) are.
* §3.2 title "Why no fibre can be a Pell conic" and "structural reason: the torus is split": the *true* reason
  is BL Lemma 3.10 (real-place boundedness, inequality (3.6)), which covers every curve in U_n, split or not.
The arithmetic conclusion (Thm 3.1, Cor 3.3: every fibration of U_n has only finitely many integral points on
every non-line fibre) is correct for **every** fibration — it does not need splitness at all.
Repair: state "(F1)–(F3) are split; curves contained in V_n are never non-split tori (Prop 3.2); for an
arbitrary fibration, Thm 3.1 alone gives finiteness"; downgrade the §6 cell to "plane-conic bundles split
(PROVED); all conic bundles split: not claimed"; drop "structural reason".

**D4 (MINOR). α|F2 = (−λ, −nZ) is stated without proof.** Location: §3.1 (F2). One-line proof (reviewer):
on u₁ = λu₂ the residual equation is u₃·Z = nλu₂, so −u₂/u₃ = −Z/(nλ) ≡ −nλZ mod squares, and
α = (−λu₂/u₃, −u₂/u₃) = (−λ, −u₂/u₃) = (−λ, −nλZ) = (−λ, −nZ) + (−λ, λ) = (−λ, −nZ). Verified at every
place on all 16622 solutions (p < 2000) in four orientations (`review_geo_genus.py`). Add it.

**D5 (MINOR, cosmetic). Br_vert sketch.** Location: §3.1. (a) In Ũ_n the fibre of u₁ over t = 0 is
L₁₂ + L₁₃ + E (u₁ vanishes on E), and L₁₂, L₁₃ do not meet each other (they meet E), so "L₁₂ ∪ L₁₃ meeting at
P" describes U_n, not Ũ_n. (b) Rational points on the fibres are not needed; one geometrically integral
multiplicity-1 component per closed fibre plus Faddeev (residue at ∞ is determined) suffices. Conclusion
unaffected.

**D6 (MINOR). Cor 3.3 "u_i ≤ n²-type bounds" is false.** Positive solutions can have max u_i ≍ n⁴: for
n ≡ 3 (mod 4), u = ((n+1)/4, nu₁+1, nu₁(nu₁+1)), e.g. 4/7 = 1/2 + 1/15 + 1/210. Repair: "u_i ≪ n⁴"
(u₁ ≤ 3n/4, u₂ ≤ 2nu₁/(4u₁−n), u₃ ≤ n u₁ u₂).

**D7 (MINOR). §4.2.** (a) "`𝒰₁(ℤ[1/p])⁺` is infinite (it contains `p^{−k}U_{p^k}(ℕ)` for all k)": containment is
right, but infinitude needs infinitely many k with a solution of 4/p^k having some u_i prime to p (scaled
solutions of 4/p give the *same* point of U₁(ℚ)). This is easy for p ≡ 3 (4) or p ≡ 2 (3) (explicit families),
but for p in a square class mod 840 it is itself an ES-type statement. Repair: "is infinite for p ≢ □ (mod 840)
(polynomial identities at p^{12j+1}); in general this is not needed for the argument" — the argument only uses
that finiteness does not *exclude* S-integral SA. (b) "In general X(ℚ) is discrete in X(𝔸) …, so a condition
at all places is a Hasse-principle question for a **finite** set" is false in general (x² − 2y² = 1 with
W = ℝ_{>0}² × ∏ℤ_p contains infinitely many points). Here finiteness comes from BL Lemma 3.10. Repair: cite it.

**D8 (MINOR-to-MAJOR inside a PROVED proposition). Prop 4.1: `Σ^I_{p,d}(ℤ)` is infinite whenever (−d/p) = +1.**
As defined, `Σ^I_{p,d} = {(a,c,e,f) : ef − 4da² = 1, f + p = 4cda}` has no non-vanishing condition. Taking
c = 0: f = −p, e = −(4da² + 1)/p, integral for all a in a residue class mod p as soon as −4d is a square mod p.
Example p = 5, d = 1: (e,f,a,c) = (−1,−5,1,0), (−13,−5,4,0), (−29,−5,6,0), … (checked in
`review_geo_levels.py`). These map to `(−a²dp, 0, 0) ∈ L₂₃`, consistent with Thm 3.1. Repair: require
`c ≠ 0` (ET's Σ^I has all six coordinates non-zero). Then finiteness holds: the map to U_p is 2:1 (a,b,c ↦ −a,−b,−c
at fixed d), b = 0 forces pe = −1, b = −a forces ce = 0, and bp = −c would put u on M_k with u_k = p/4 ∉ ℤ;
so the image avoids the lines and BL Lemma 3.10 applies. The shrinking-target conclusion is unaffected.

**D9 (MINOR). Cor 4.2 is a meta-statement labelled PROVED.** "No SA, descent or fibration theorem whose output is
'integral points in a prescribed adelic open set' can by itself produce ES solutions" is not a mathematical
statement until "adelic open set" is restricted: a real open box around one point isolates any single integral
point. The provable core (reviewer): for every open `W_f ⊂ ∏_ℓ X_d(ℤ_ℓ)`, `X_d(ℤ) ∩ W_f` is empty or infinite
(a point is moved by an infinite congruence subgroup of the arithmetic group, which stays in W_f), whereas the
level-d ES set of p is finite (D8-repaired Prop 4.1); hence no statement "X_d(ℤ) ∩ W_f ≠ ∅" (SA away from ∞)
certifies an ES point. State that, label it PROVED, and leave the rest as Assessment.

**D10 (MINOR — attribution/novelty). §5.1 "now identified as BL's α", report item 5 "Novelty unchecked".**
BL's own Appendix A (pp. 15–16) already derives Yamamoto's reciprocity conditions from Cor 1.3. In particular
Yamamoto [24, Lem. 4] (Type 2): with Mordell's (u₁, u₂/p, u₃/p) = (bcd, abd, acd), q = 4abd − 1 satisfies
(p/q) = −1. Under the dictionary (a,b,c)_Mordell = (c,a,b)_ET this q is ET's f = 4acd − 1, so **Prop 5.2's
"(p/f) = −1" (= O128's genus lemma) is Yamamoto 1965 Lem. 4, derived from α by BL themselves.** For Type I,
the statement (−d/p) = −1 is the two-line reason why the Mordell/ET families {n ≡ −f (mod 4ad), f | 4a²d+1}
(ET Prop 1.9, first family) only cover non-residue classes mod 4d; its identification with α is again in the
spirit of BL App. A (Yamamoto's (p/4abq) = −1). I could not access Yamamoto 1965 itself and did not find the
literal sentence "(−d/p) = −1 at level d" in ET. Repair: cite BL App. A for both, say "known/folklore; we only
record it in ET coordinates", drop "now identified".

## Remarks (non-defects)

**R2 — symbolic proof of Prop 2.1 (the author's flagged weak point).** In ℙ² with coordinates X and
σ = X₁+X₂+X₃, the linear system φ(X) = (4X₁X₂X₃ : nσX₂X₃ : nσX₁X₃ : nσX₁X₂) maps into S_n
(`review_geo_sym.py` (A): S_n∘φ ≡ 0, and 1/u_i = 4X_i/(nσ) = s_i, Σs_i = 4/n). Its base locus is exactly the
six simple base points: the three coordinate points and V₁, V₂, V₃ = (0:1:−1), (1:0:−1), (1:−1:0) (all
multiplicity 1, checked). Each of the four lines X_i = 0 and σ = 0 contains three base points, so in Bl₆ℙ² they
are (−2)-curves, contracted to the four nodes; σ = 0 goes to P = (1:0:0:0). So Bl₆ℙ² → S_n is the minimal
resolution (Cayley's classical model). Pulling back x₀ = 4X₁X₂X₃: the total transform is ΣX̃_i + 2ΣE_coord +
ΣE_{V_k}, minus the base divisor ΣE gives x₀^* = ΣX̃_i + ΣE_coord. Hence
Ũ_n = Bl₆ℙ² \ (ΣX̃_i + ΣE_coord) = Bl_{V}ℙ² \ (strict transform of X₁X₂X₃ = 0), exactly Prop 2.1, with E = σ̃ and
L_ij = E_{V_k} \ X̃_k. Self-intersections: σ̃² = 1 − 3 = −2, X̃_k² = 0 in Bl_V ℙ² ✓. The Markoff comparison
(two points per side ⇔ boundary of three (−1)-curves, D² = 3) is also consistent with D² = 9 − 6.

**R3 — Prop 5.1 is a genuine BM obstruction on the level-d cover.** On Σ^I_{p,d}(ℤ_p), 4abd = pe + 1 gives
(abd/p) = 1, hence inv_p α = ((−ab)/p) = (−d/p) *locally*; with inv_∞ = −1 on the positive part and inv_ℓ = 1
for ℓ ≠ p (BL 3.5, 3.8), every positive adelic point of Σ^I_{p,d} has invariant sum (−d/p)·(−1), so for
(−d/p) = +1 the obstruction is a bona fide BM obstruction on the integral model of the level-d chart. The
author's Jacobi-symbol proof is global; the local version would sharpen §5.1's wording.

**R4 — independent reproduction of §5.3** (`review_geo_levels.py`, log `logs/review_geo_levels.txt`):
Type II level 1, p ≡ 1 (24), p < 1.5·10⁶: 14183 primes, 73 failures, first 97, 193, 673, …, last 1456921 —
identical. Type I, p ≡ 1 (24), p < 10⁵, (−d/p) = −1: d = 5: 0/603; d = 7: 42/612 (97, 433, 601, …);
d = 11: 23/611 (193, 457, …); d = 13: 88/608 (73, 97, …) — identical. Level sets from full enumeration:
97: I {5,14,17,26}, II {2,5}; 73: I {5,7,10,11}; 193: II {2,5}; 673: II {2,3,5,17} — identical. The d = 5
identity-level argument (p ≡ 13, 17 (20) ⇒ f ∈ {7, 3} | 21) is correct.

## Overall verdict
No FATAL defects. O126 is a correct and honestly labelled "negative map". Its PROVED content is either
restatement of BL (Thm 3.1 = BL Lemma 3.10; §1), elementary (§2, §4.1, §4.2), or folklore re-expressed (§5.1–5.2,
cf. BL App. A / Yamamoto). Must-fix before citing: D3 (splitness ≠ the reason; "all conic bundles split" not
proved), D8 (Prop 4.1 finiteness false without c ≠ 0), D1 (n = 1), D10 (attribution). The rest is cosmetic.
Aim (B) "negative for every fibration" is right **for every fibration**, but because of BL Lemma 3.10 (real
place), not because of splitness.

## Round-1 repairs applied
At the parent's request the reviewer applied D1–D10 and R2–R4 directly in `GEOMETRY_ES.md` and
`reviews/agent-reports/AGENT_REPORT_O126.md`, each marked "(R126 repair)".
