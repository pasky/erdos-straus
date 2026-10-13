# R184 — independent hostile review (reviewer 2 of 2) of O180 `LORENZINI_W.md`

Reviewer: side-agent `review-lorenzini-2`. Did NOT read `reviews/lorenzini-w-review.md`.
From-scratch code: `scripts/review_lw2_cover.py`, `scripts/review_lw2_brute.c` (+ further `review_lw2_*` below).
Source checked: `sources/lorenzini/CriticalPolynomialOfAGraph.txt` (arXiv:2311.06367 text), Example 6.2(a), Prop 6.3, Remark 6.4.

## Summary verdicts
| claim | verdict |
|---|---|
| Thm 9.1 (even n ≥ 16, n ≠ 510, are values) | **SOUND** (proof re-derived end to end; minor presentational defects only) |
| Novelty of Thm 9.1 | not found in literature (§2) |
| Prop 8.1 / Cor 8.2 | SOUND (§3) |
| Prop 6.1 | SOUND-AFTER-REPAIRS (§4, D6–D7) |

## 1. Theorem 9.1 — re-derivation (SOUND)

**Reduction (checked against Lorenzini's exact statement).** Lorenzini Prop 6.3(a) (p. 24): "V_{A₃}(2) contains all even positive
integers n, except possibly those of the form n = 2^m − 2 with m odd or m = 2, 4." His proof: z = 2 gives x(2y − 1) = n + 2, solvable
with x, y ≥ 2 when n + 2 is neither prime nor a 2-power; for even m > 4 the word (4, (2^{m−3}+1)/3, 6). I re-derived both:
for even n, n + 2 is even (never prime for n ≥ 2), so if n + 2 = 2^a·u with u ≥ 3 odd take 2y − 1 = u, x = 2^a ≥ 2; and
24·(2^{m−3}+1)/3 − 10 = 2^m − 2 with 3 | 2^{m−3}+1 ⟺ m − 3 odd, y ≥ 2 ⟺ m ≥ 6. m = 2, 4 give n = 2, 14 (excluded by n ≥ 16).
So the residue is exactly n = 2^m − 2, m odd, as the author states. No hidden hypothesis.

**The six families (symbolic).** With n = 2^m − 2:
* (x,z) = (3,3): 9y − 6 = n ⟺ 9 | 2^m + 4 ⟺ 2^m ≡ 5 (mod 9) ⟺ m ≡ 5 (mod 6) (2^k mod 9: 2,4,8,7,5,1).
* (x,z) = (6,12): 72y − 18 = n ⟺ 72 | 2^m + 16 ⟺ (m ≥ 3) ∧ 2^m ≡ 2 (mod 9) ⟺ m ≥ 3, m ≡ 1 (mod 6).
* (x,y) = (7,2): 13z − 7 = n ⟺ 13 | 2^m + 5 ⟺ 2^m ≡ 8 (mod 13) ⟺ m ≡ 3 (mod 12) (ord₁₃2 = 12).
* (x,z) = (3,9): 27y − 12 = n ⟺ 27 | 2^m + 10 ⟺ 2^m ≡ 17 (mod 27) ⟺ m ≡ 15 (mod 18) (ord₂₇2 = 18).
* (x,y) = (10,11): 109z − 10 = n ⟺ 109 | 2^m + 8 ⟺ m ≡ 21 (mod 36) (ord₁₀₉2 = 36).
* (x,z) = (8,74): 592y − 82 = n ⟺ 16 | 2^m + 80 ∧ 37 | 2^m + 80 ⟺ m ≥ 4 ∧ 2^m ≡ 31 (mod 37) ⟺ m ≥ 4, m ≡ 9 (mod 36).
`review_lw2_cover.py` recomputes each m-class set by direct evaluation of 2^m over 4 periods at two windows (m ∈ [11,155) and
[1001,1145)): the sets agree with the table, and their union is **all 18 odd classes mod 36** (residue classes: 6+6+3+2+1+1 = 19 with
one overlap, 15 covered twice). Orders ord₉ = 6, ord₁₃ = 12, ord₂₇ = 18, ord₃₇ = ord₁₀₉ = 36 confirmed.

**Size thresholds.** Third letter ≥ 2 ⟺ n ≥ 2d − x ((x,y) kind) or n ≥ 2xz − x − z ((x,z) kind); the worst is (8,74): n ≥ 1102.
m ≥ 11 gives n ≥ 2046. ✓. Fixed letters are all ≥ 2. ✓. Explicit (x,y,z) with exact integers verified for every odd m ≤ 4001:
the only failures are m = 1, 3, 9 (n = 0, 6, 510), exactly the stated exceptions; m = 5, 7 are in fact also caught by families
(3,3) and (6,12). Brute force for m ≤ 11: n = 30 → (3,4,3) only; 126 → (6,2,12),(12,2,6); 510 → none; 2046 → (3,228,3),(8,10,26),(26,10,8).

**Independent brute force (`review_lw2_brute.c`, x ≤ z symmetric enumeration, 16 s).** All n ≤ **10⁸**: the non-values are exactly
{0, 2, 6, 14, 510} (even) and {1, 3, 5, 9, 11, 15, 35, 105} (odd). This matches L_{A₃} of Lorenzini Ex. 6.2(a) and the even
statement of Thm 9.1 including "the even part of the complement is exactly {0, 2, 6, 14, 510}".

**Verdict: SOUND.** The proof is complete and elementary; I found no quantifier or threshold error.
Minor defects (presentation only) listed in §5 (D1–D2).

## 2. Novelty of Thm 9.1 (searched 2026-10-13; Assessment: NOT FOUND in the literature → plausibly new)
What I checked:
* **Lorenzini's paper itself** (sources/…/CriticalPolynomialOfAGraph.txt = arXiv:2311.06367): Example 6.2(a) asks whether the complement of
  V_{A₃}(2) is exactly L_{A₃}; p. 24: "We have not been able to answer this question beyond the following remarks" (Prop 6.3), and Remark 6.4 lists
  2^{2m+1} − 2 = 0, 6, 30, 126, 510, 2046, … noting 0, 6, 510 fail and 30, 126 are attained exactly once. So the even case was open in the paper.
* **Citing works** (Semantic Scholar citation list for arXiv:2311.06367, 7 entries): Wang–Lu EJC 2026; Behera–Chhetri–Yadav, *Arithmetical structures on
  ladder graphs* (arXiv:2604.25671); Archer–Diaz-Lopez–Glass–Louwsma (arXiv:2505.05392); Archer–Melles (arXiv:2504.08539); Chhetri–Behera–Yadav, *Fan graphs*
  (arXiv:2503.01913); Archer et al. EJC 2024 (2301.02114); Diaz-Lopez–Louwsma LAA 2022. I downloaded the four arXiv ones and grepped the text: none mentions
  xyz − x − z, 510, or the values of d_{A₃}; they cite Lorenzini for arithmetical-structure background only.
* **Wang & Lu**, *The critical polynomials of simple connected graphs*, EJC **33(3) (2026) #P3.80**, doi:10.37236/13899 (downloaded from combinatorics.org).
  Main result: V_G(2) is *dense* in Z_{≥0} for every connected simple graph (Thm 5), via Dirichlet. Final section: "it remains an open problem whether the
  complement of V_{d_G}(2) in Z_{≥0} is finite." No A₃-specific statement, no even-n result.
* **Lorenzini's later preprints** in sources/ (*Intersection matrices of wild cyclic quotient singularities*, 2025-10-12; *Questions on wild Z/pZ-quotient
  singularities*): cite [23] only for 5.3(c)/Remark 1.4/2.1(c); nothing about A₃ values.
* Web searches (Jina) for "xyz − x − z", the exceptional list 0,1,2,3,5,6,9,11,14,15,35,105,510 (OEIS), MathOverflow, and "Lorenzini critical polynomial
  2^m − 2": no hit settling the even case. The nearby Conrey–Shah arXiv:2112.15551 treats xyz + x + y + z (a different polynomial; Lorenzini cites it).
Limits: I could not query MathSciNet/zbMATH/Google Scholar "cited by" directly (Google Scholar reports 9 citations, S2 lists 7; two unseen).
**Assessment:** the even half appears new as far as an open-web search can tell. "Settles the even half of Lorenzini's question" is accurate in substance; the proof is
so short (a 36-periodic covering) that I would phrase the novelty claim modestly ("we could not find this in the literature").

## 3. Prop 8.1 and Cor 8.2 (SOUND; one attribution/scope remark)
**Prop 8.1 re-derived.** (2,2,z): 4z − 2 − z = 3z − 2, so z = (n+2)/3 ∈ Z ⟺ n ≡ 1 (3), z ≥ 2 ⟺ n ≥ 4. (3,y,4): 12y − 7 = n ⟺ n ≡ 5 (12),
y ≥ 2 ⟺ n ≥ 17. n ≡ 1 (4), 3 ∤ n splits into n ≡ 1 (12) and n ≡ 5 (12); the only such n < 13 failing is 5 (no word; checked). ✓
`scripts/review_lw2_prop81.py 2·10⁶`: all n ≡ 1 (4), 3 ∤ n, 13 ≤ n < 2·10⁶: 0 bad words. For the 74 415 primes in range I computed the HJ
continued fraction of p/A, A = xy − 1, with my own HJ routine: it is exactly [[z, y, x]] (length 3; consistent with DK Lemma 1.1, A·A* = yp + 1),
and the Legendre census is: p ≡ 1 (12): (A/p) = +1 for all 37 180; p ≡ 5 (12): (A/p) = −1 for all 37 235. This matches the author's sign paragraph
((p+3)/4 ≡ 3·4⁻¹, (3/p) = (p/3) by QR since p ≡ 1 (4)).
**Cor 8.2 logic.** HJ_DEEP §3: for n ≡ 1 (4), interior-SQ₅(n) ⟺ "L₃(n) contains a −1 word" (DK Thm 4.5) ⟺ (W)(n) ∧ (S)(n), where (W)(n) ⟺ L₃(n) ≠ ∅
by DK Lemma 1.1 and (S) carries the non-square hypothesis (primes are non-squares). With (W)(p) proved, interior-SQ₅(p) ⟺ (S)(p). ✓ The statement is a
tautological consequence, correctly labelled; it inherits DK Thm 4.5 (not re-reviewed here; reviewed earlier in the campaign).
Remarks (MINOR, see D4–D5): (i) for p ≡ 5 (12) the (3,·,4) word *is* a −1 word, so (S)(p) and interior-SQ₅(p) are outright PROVED there; Cor 8.2 is
informative only for p ≡ 1 (12). The note says this in prose but the Cor should state it. (ii) Attribution: (2,2,·) is the z = 2 slice of Lorenzini
6.3(b) (3 | n + 2), and (3,·,4) is his z = 4 slice with divisor (n+4)/3 ≡ 3 (mod 4); so Prop 8.1 is a two-line extension of Lorenzini 6.3(c) (it drops his
mod-9 condition). "SHARP/deflationary" is fair; "new" would not be.
**"What remains" (§9, last paragraph) re-derived.** Odd n: n ≡ 1 (3) ⇒ 3 | n + 2 (6.3(b)); n ≡ 5 (12) ⇒ Prop 8.1; left: n ≡ 3, 9, 11 (12) with n + 2
prime (n + 2 odd, so never a 2-power). Odd exceptions 3, 9, 11, 15, 35, 105 all lie there (5 ≡ 5 (12) is in E_W). Even n: Thm 9.1. ✓ The density remark
(Dirichlet for primes ≡ 1 (mod M) gives n ≡ −1 (mod M) with n + 2 prime) is correct.

## 4. Prop 6.1 (density bound): SOUND at sketch level (complete modulo standard theorems); minor repairs
Re-derived step by step:
* **Avoided classes.** p prime ≤ Q = √N, x | p + 1, 2 ≤ x ≤ (p+1)/2: the word (x, (p+1)/x, (n+x)/p) has d = xy − 1 = p, y ≥ 2, and z ≥ 2 ⟺ n ≥ 2p − x,
  true for n > N = Q² ≥ 2p (Q ≥ 2). The classes −x mod p are distinct (x < p), count ω(p) = τ(p+1) − 2 < p. ✓
* **Large sieve.** S ⊂ (N, 2N] avoids ω(p) classes mod every p ≤ Q ⇒ |S| ≤ (N + Q²)/L (Montgomery / Montgomery–Vaughan). ✓
* **L ≥ e_k.** Squarefree m = p₁⋯p_k with p_i ∈ I = (Q^{1/(2k)}, Q^{1/k}] has m ≤ Q, and ω/(p − ω) ≥ ω/p. ✓
* **G.** Σ_{p ≤ y} τ(p+1) = C y + o(y), C = ζ(2)ζ(3)/ζ(6) ≈ 1.9436 (the shift a = +1 has no local correction factor). Partial summation over
  I gives C·log(b/a) + o(log(b/a)) + O(1) = (C/2 + o(1)) log Q/k, valid because log a = log Q/(2k) → ∞ for k ≍ √log Q. ✓
  Numerically (`scripts/review_lw2_titchmarsh.py 10⁷`, own code): Σ_{p≤y} τ(p+1)/y = 1.925, 1.933, 1.935 at y = 10⁵, 10⁶, 10⁷ (→ C, slow
  log log y/log y convergence); G on (10⁵, 10⁷] = 8.24 vs the main-term formula 8.28. ✓
* **e_k ≥ (G^k/k!)(1 − O(k²/G²)).** True with the explicit form k!e_k ≥ G^k − C(k,2)·S₂·G^{k−2}, S₂ = Σ_{p∈I} g(p)². **But** with k = ⌊ε√log Q⌋ one has
  G ≍ √log Q/ε, so k/G → 2ε²/C is a *constant*, not o(1) (see D6). The argument still works: S₂(I) → 0 (tail of a convergent series) or take ε small so that
  the correction is ≤ 1/2. Then e_k ≥ ½ (eG/k)^k/(e√k) ≥ exp(c′√log Q) with c′ ≈ ε log(eC/(2ε²)) > 0. ✓ Dyadic summation: ✓.
**Labels.** The Titchmarsh divisor asymptotic is an unconditional theorem (Linnik 1961; Rodriquez 1965 and Halberstam 1967 via Bombieri–Vinogradov), and only
the lower bound Σ_{p≤y} τ(p+1) ≫ y is needed. So "PROVED relative to the Titchmarsh divisor theorem" can simply be "PROVED (using the Titchmarsh
divisor theorem)". Nothing is hidden: c is absolute, no parameter dependence.
**Context remark (D7).** "Lorenzini/Wang give density 1 only" understates Lorenzini: his Prop 6.3(a,b) immediately gives #E ∩ [1, N] ≤ π(N + 2) + log₂ N ≪ N/log N.
Prop 6.1 is still a genuine improvement (exp(−c√log N) vs 1/log N), but the comparison sentence should say so.

## 5. Defects
No FATAL or MAJOR defects found. All headline mathematical claims checked hold.

**D1 (MINOR, §9 Thm 9.1 proof, sentence "It is ≥ 2 as soon as n ≥ 2·592, i.e. m ≥ 11").** "i.e." is not an equivalence (2·592 is a sufficient bound; the exact
worst threshold is n ≥ 1102 from (8,74)). *Repair:* "It is ≥ 2 for n ≥ 2·592 − 82 = 1102, in particular for all odd m ≥ 11." Also note that m = 5, 7 are
already caught by the (3,3) and (6,12) families, so only m = 1, 3, 9 are genuine exceptions.
**D2 (MINOR, §9, "L = 36 is the least period among {12, 36, 60, …}").** The set {12, 36, 60, …} is an odd choice (24 is skipped). My own search
(`scripts/review_lw2_period.py 3000 72`: all fixed-pair families with modulus ≤ 3000) finds that no even period L < 36 works (12 misses m ≡ 9; 18 misses 3, 9;
24 misses 9, 21; 30 misses 3, 9, 21) and 36 works. *Repair:* "36 is the least even period L for which a covering exists using families of modulus ≤ 3000
(checked all L ≤ 36)."
**D3 (MINOR, header and §0 citation).** "T. Wang, EJC 33(3) #P80 (2026)" → **T. Wang and L. Lu, *The critical polynomials of simple connected graphs*, Electron.
J. Combin. 33(3) (2026), #P3.80, doi:10.37236/13899.** Their "open problem" sentence concerns finiteness of the complement for general G (they prove density 1
for V_G(2), all connected simple G); it is not A₃-specific. Phrase accordingly.
**D4 (MINOR, Cor 8.2).** For p ≡ 5 (mod 12) the (3, (p+7)/12, 4) word has (A/p) = −1, so (S)(p) and interior-SQ₅(p) are PROVED there outright (this is the
classical p ≡ 2 (3) ES identity). *Repair:* add "(S)(p) holds for p ≡ 5 (mod 12); Cor 8.2 has content only for p ≡ 1 (mod 12)" into the Cor statement.
**D5 (MINOR, Prop 8.1 attribution).** (2,2,·) is the z = 2 slice of Lorenzini 6.3(b) and (3,·,4) is his z = 4 slice with divisor (n+4)/3 ≡ 3 (mod 4).
Prop 8.1 is a two-line strengthening of Lorenzini 6.3(c) (dropping his mod-9 condition). *Repair:* say so; do not count it as new.
**D6 (MINOR, Prop 6.1 proof, "e_k ≥ (G^k/k!)(1 − O(k²/G²))" with k = ⌊ε√log Q⌋).** k/G tends to the constant 2ε²/C, so O(k²/G²) is not o(1).
*Repair:* "with the explicit bound k!e_k ≥ G^k(1 − k²S₂/(2G²)), S₂ = Σ_{p∈I} g(p)² → 0, the bracket is ≥ 1/2 for large Q".
**D7 (MINOR, Prop 6.1 remarks and label).** (a) Lorenzini 6.3(b) already gives ≪ N/log N exceptions; "density 1 only" should be corrected. (b) Label
"PROVED relative to the Titchmarsh divisor asymptotic" → "PROVED" (Titchmarsh–Linnik is unconditional; only the ≫ y lower bound is used).
**D8 (MINOR, novelty phrasing in §0 item 0 / §9 title).** "settled" / "new as far as I can tell" is supported by my search (§2), but the search cannot exclude a
private communication or an unindexed citer (Google Scholar shows 9 citers, Semantic Scholar 7, which I checked). *Repair:* keep "(new as far as we can tell;
not in Lorenzini 2024, Wang–Lu 2026, or the citing papers [list])".

## 6. Final verdicts
| claim | verdict |
|---|---|
| **Thm 9.1** (every even n ≥ 16, n ≠ 510, is xyz − x − z, x,y,z ≥ 2) | **SOUND** (independently re-proved; brute force to 10⁸ agrees; D1, D2 cosmetic) |
| Novelty of Thm 9.1 | **Not found in the literature** (Assessment, §2; D3, D8) |
| Prop 8.1 | **SOUND** (D5 attribution) |
| Cor 8.2 | **SOUND** (D4: strengthen statement for p ≡ 5 (12)) |
| "What remains of (W)" (§9) | **SOUND** |
| Prop 6.1 | **SOUND-AFTER-REPAIRS** (D6 proof wording, D7 label/context; no mathematical gap) |

**Repairs applied (R184, after merging main with R180 repairs).** In `LORENZINI_W.md` and `reviews/agent-reports/AGENT_REPORT_O180.md`, marked "(R184 repair, Dk)":
D1 (threshold wording + m = 5, 7 remark), D2 (least even period, with the review_lw2_period result), D3 (Wang–Lu citation, header and report),
D4 (Cor 8.2: (S)(p) proved for p ≡ 5 (12)), D5 (Prop 8.1 attribution to Lorenzini's z = 2/4 slices), D8 (modest novelty phrasing in §0, §9 title and the report).
D6 and D7 had already been fixed by the R180 repairs (exact k!e_k bound with T → 0; Titchmarsh label; the ≪ N/log N baseline), so I skipped them.
