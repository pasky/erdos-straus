# Referee report R86: `paper/es-coverings-note.tex` (coverings note, author report O86)

Reviewer: hostile referee side agent, branch `side-agent/referee-coverings`. I reviewed the paper
as merged from `side-agent/coverings-note` (20 pp.). The author's document was not edited.

## Recommendation

**Accept after minor revision. No FATAL defects.**

I re-derived the framework (Lemma 2.4, Prop 2.5, Remark 2.6, Problem 1's "equivalently") from
scratch, and it is correct.

All numerical spot checks I re-implemented agree with the paper. The one exception is a wrong
integer in the proof of Thm 5.1 (D2). That error also appears in the source PM and in its review.

There is one **MAJOR** defect, D1. One sentence after Conj 5.4 says that sterility would show Thm
5.1(b) "cannot be improved to a statement with no exceptional classes". Thm 5.1 is a statement
about ES, so this contradicts the paper's own disclaimer that a sterile point says nothing about
ES. The fix is one clause.

There are 16 MINOR defects. Most are scope or wording slips against the reviewed sources. The
most important minor ones are:

- D3: the scope of the brute-force completeness check in Comp 6.3.
- D4: the hypotheses of Cited Thm 3.2.
- D6: the "summable bound would close the question" claim in Rem 4.13.

"ES is open" is stated clearly in the abstract, the introduction and the closing results paragraph.

## Verdict per section / claim

| item | verdict |
|---|---|
| Lemma 2.1 (families yield positive solutions for all n≥1) | SOUND. The table matches ET Prop 1.9 verbatim (checked against `sources/elsholtz-tao-1107.1010.pdf` p. 8). Identity, integrality and positivity were re-checked from scratch on 367,524 (family, triple, n) cases. |
| Cited Thm 2.2 (ET Prop 1.9) | SOUND. ET p. 8: "all sufficiently large primes in this residue class lie in one of a finite number of residue classes from one of following families". The paper's union form and its Type I / Type II remark are faithful. |
| Lemma 2.4 | SOUND-AFTER-REPAIRS (D8, wording of "clopen" and "union of reduced classes"). |
| Prop 2.5 | SOUND. Re-derived, see §A. One wording repair (D9). |
| Remark 2.6, Remark 2.7 | SOUND |
| Prop 3.1 | SOUND, modulo the cited Mordell–Schinzel theorem. The ET p. 8 wording ("a primitive congruence class n = r mod q which is a perfect square, cannot be solved by polynomials") is exactly what the proof uses, with r = m². The x=1 case is genuinely elementary. "ET also derive it" overstates what ET do (D13). |
| "Mordell-hard primes admit no finite covering" paragraph | SOUND. It only needs the x=1 case plus ET Prop 1.9, so it is unconditional and elementary modulo ET. Saying so would strengthen the text (D13). |
| Cited Thm 3.2 (Theorem C/C1) | SOUND-AFTER-REPAIRS (D4: dropped quantifier and class, mis-definition of "bounded"). The label and the novelty hedge match the source and its novelty audit. |
| Remark 3.3 | SOUND (Assessment, correctly labelled). |
| Thm 4.1 C(5)=10 | SOUND. The proof was re-derived by hand, and a from-scratch census over all 1,628 hard primes p<3·10⁵ with n_p=5 gives max ck_min = 10, ck_min(193) = 10, and ck_min = 5 when p≡2 (5). |
| Thm 4.2 | SOUND. The (i) threshold and the (ii) sketch were re-derived. Label nit: D10. |
| Thm 4.3 and the text after it | SOUND (labels match PT1 and R31). |
| Lemma 4.4 | SOUND. Citation nit: D11. |
| Prop 4.6 | SOUND-AFTER-REPAIRS. (b) was checked numerically for r = 11, 19, 43, 59, 67, 83 and several w. The (a) sketch contains a false sub-claim (D5). |
| Lemma 4.7, Comp 4.8, Cor 4.9 | SOUND. I re-derived min(F,e) ≤ √(1+4X²/r) < 2X/√r+1 and re-checked all four height bounds of Cor 4.9. The engine scopes match PT3/R72. Nits: D12, D14. A sanity search found no certificate at x̂₉ with ck ≤ 6000; the residue-one cover by (7,3,11), (7,3,23), (14,2,15) was confirmed for x₇ = 3, 5, 6 respectively. |
| Lemma 4.10 (Vieta) | SOUND (re-derived line by line). |
| Prop 4.11 | SOUND as a sketch with pointer; the labels match PT3. |
| Prop 4.12 | SOUND. Re-derived, including the compatibility (−7/F) = (F/7) for F≡3 (4), and the CRT for the class of (7p₀,1,F). |
| Remark 4.13 | SOUND-AFTER-REPAIRS (D6). |
| Conj 4.14 and evidence | SOUND (labels). |
| Thm 5.1 | SOUND-AFTER-REPAIRS (D2: a wrong integer in the proof). Both certificates were replayed with `review_mordell_check.py` (CERTIFICATE OK, uncovered = listed exceptions). They were also replayed with a third, from-scratch solver: 360 and 2160 targets, uncovered {112561} and the six listed residues, every covering identity verified at the residue. The fractions 1/360 = 1/(46080/128) and 6/2160 were re-derived. |
| §5.2, Comp 5.2, Cor 5.3 | SOUND (scopes match PM/R80). |
| Conj 5.4 and the following paragraph | GAP / MAJOR wording (D1). |
| Lemma 6.1, Prop 6.2 | SOUND. I re-derived (c)'s identity and the parity argument. |
| Comp 6.3 | SOUND-AFTER-REPAIRS (D3: scope of the brute-force cross-check). My own brute force over all seven families with modulus ≤ 10⁵ finds no level-1 box in C₅ and exactly 4 level-2 boxes (u ≡ 56, 107, 226, 243 mod 289), i.e. covered fraction 4/17 = 0.235294, as in the table. It finds no level-0 hit. 56561/83521 = 0.677207 matches 1 − 0.322793. |
| Thm 6.4, Cor 6.5, Conj 6.6 | SOUND. The threshold arithmetic was checked. |
| Status paragraph | SOUND. I recomputed the 0.84 tail as 0.8447 and confirmed <0.01. The BE bound is quoted correctly from ET p. 6 ("f(n) ≪_ε n^{2/3+ε}"). Nit: D7. |
| Assessment 6.7 | SOUND (Assessment). |
| Problem 1 "equivalently" | SOUND, see §A.3. Wording nit: D9. |
| Bibliography | Mostly verified. Mordell entry likely wrong (D15); two items unverifiable (D16). |

## A. Re-derivations of the framework (points 1 and 3 of O86)

### A.1 Lemma 2.4 and the topology

- **Units.** If x ∈ 𝒫′, then each neighbourhood x + q^kẐ contains infinitely many primes of 𝒫. At most one of them equals q, so x_q ≢ 0 (mod q), and x_q ∈ ℤ_q^×.
- **Compactness.** 𝒫′ is closed (a derived set in a T₁ space), hence compact.
- **Primes vs accumulation points.** A prime p is never in 𝒫′, since p_p ∉ ℤ_p^×. So the closure of 𝒫 is 𝒫 ⊔ 𝒫′. This is the correct reason for using accumulation points rather than closure, as the author says.
- **The relative topology.** Ẑ^× = ∏ℤ_q^× is closed but **not open** in Ẑ. A set "defined modulo M" in Ẑ is therefore never a subset of Ẑ^×. Σ must be read as (union of reduced classes mod M) ∩ Ẑ^×, which is clopen *relative to* Ẑ^×. With that reading the proof of 𝒫(Σ)′ = Σ is correct:
  - "⊂": the first half of the lemma puts the limit point in Ẑ^×.
  - "⊃": x + QẐ with M | Q is a reduced class because x is a unit, so Dirichlet's theorem applies.

### A.2 Prop 2.5

**(a)** Finitely many ET classes cover the compact set 𝒫′, and U is open. If 𝒫∖U were infinite, its accumulation point would lie in 𝒫′ ⊂ U, which is impossible. Correct.

**(b), first sentence.** The union of the classes is clopen and contains a cofinite subset of 𝒫, hence contains 𝒫′ ∋ x. Correct.

**(b), second sentence.** This is the direction that uses ET Prop 1.9.
- x lies in the closed set ⋃C_j, so x ∈ C_j for some j.
- ET Prop 1.9 gives finitely many ET classes K_i containing all large primes of C_j. Their union is clopen and misses x (x is sterile).
- So some x + QẐ ⊂ C_j misses ⋃K_i, with Q a multiple of the modulus of C_j.
- This set is a reduced class, so it contains infinitely many primes. They lie in C_j but in no K_i, which contradicts ET Prop 1.9. Correct.

Nothing in this argument needs uniformity in j or any growth condition, and no circularity is present. The cited statement is used exactly as ET state it: "all sufficiently large primes in this residue class lie in one of a finite number of residue classes from one of the following families". The Type I / Type II split is harmless, because ET p. 8 say that every solvable primitive class is of one of the two types.

**Final "iff".**
- "⇒" is (b).
- "⇐" is (a). An ET class is a finite union of primitive residue classes mod M(κ), together with non-reduced classes that contain at most finitely many primes (D9). Each primitive piece is solvable by polynomials by Lemma 2.1. Correct.

### A.3 Problem 1's "equivalently"

- **The square set is closed.** S = ∏_q (ℤ_q^×)² is closed, since each factor is an open, and therefore closed, subgroup of finite index.
- **"⇒".** Let x be sterile with x ∉ S. Some basic clopen V = (x + QẐ) ∩ Ẑ^× misses S. Then 𝒫(V)′ = V ∋ x by Lemma 2.4, so Prop 2.5(b) shows that 𝒫(V) has no cofinite polynomial covering.
- **"⇐".** A clopen Σ ⊂ Ẑ^× is compact, so it is a finite union of basic sets, i.e. it is defined mod some M. Lemma 2.4 gives 𝒫(Σ)′ = Σ. Prop 2.5(a) then gives a sterile point in Σ, which is not a square point because Σ ∩ S = ∅.
- **Conclusion.** The equivalence is correct. It uses closedness of S (in "⇒") and the "defined mod M" consequence of compactness (in "⇐"). Both deserve one sentence in the paper (D9).

## B. Numbered defects

### MAJOR

**D1 (MAJOR; §5.3, the paragraph after Conj 5.4, l. 922: "so that Theorem 5.1(b) cannot be improved to a statement with no exceptional classes").**
- **Problem.** Thm 5.1(b) asserts solvability of ES outside six classes. Improving it to "no exceptional classes" would be the statement that ES holds for all primes with (p/13) = −1. A sterile point cannot rule that out; the paper itself says (end of §1) that a sterile point "would say nothing about whether ES holds for those primes". As written, the sentence is false, or at best an unproved claim about ES.
- **Repair.** Replace the sentence with: "…so that the method of Theorem 5.1(b), a finite list of polynomial classes, cannot be extended to cover all such primes up to finitely many exceptions."

### MINOR

**D2 (MINOR, factual; proof of Thm 5.1, l. 834: "the third lift $592801$ of $112561$ modulo $720720$").**
- **Problem.** The lifts of 112561 mod 720720 are 112561, 352801 and **593041** (= 112561 + 2·240240). The number 592801 is divisible by 11, so it is not even a unit residue. I checked that 593041 ≡ 4 (mod 9) is not among the six exceptions of (b), so the claim holds with the corrected number.
- **Repair.** Replace 592801 by 593041 in the paper. The same typo is in `POINTWISE_MORDELL.md:128` and `reviews/pointwise-mordell-review.md:69`; flag it to the PM owner.

**D3 (MINOR, certified-scope overstatement; Comp 6.3, l. ~1061: "Completeness was also checked against a brute force … for all moduli ≤10⁶ ($0$ boxes missing)").**
- **Problem.** The source (PM17:133–136; R83) ran `review_m17_brute.py 1000000 3`, i.e. boxes of **level ≤ 3** only (168 boxes). Level-4 and level-5 boxes with modulus ≤ 10⁶ were not cross-checked by that brute force.
- **Repair.** Write "…for all moduli ≤ 10⁶ and all boxes of level ≤ 3 (168 boxes, 0 missing)".

**D4 (MINOR; Cited Thm 3.2 and the paragraph before it, ll. 379–395).**

(i) *Dropped quantifier.* PS Theorem C (POINTWISE_SIZE.md:465–467) requires P ∈ 𝒫 (primitive, irreducible, positive leading coefficient) and q* "nondegenerate **for every h ∈ 𝒫**". The paper's "nondegenerate in the sense of [PS, §1.2]" loses the universal quantifier, which the step-1 review (D4) explicitly asked for.
- *Repair:* "Let P = uX+v ∈ 𝒫 be linear and q* square-mimicking for P and nondegenerate for every h ∈ 𝒫 (in the sense of [PS, §1.2])".

(ii) *Wrong definition of "bounded".* The paper says "*bounded* if the number of steps is bounded independently of p". In PS (l. 134) a bounded program is one using only (P1)–(P8): loops run over lists fixed at entry, such as factor or divisor lists, whose length grows with p. The paper's definition contradicts its own "loops over the lists so produced" and narrows Corollary C1 to a different class.
- *Repair:* "*bounded* if it uses only these operations, each loop running over a list fixed at loop entry (so it halts on every input; the number of steps may grow with p)".

**D5 (MINOR, false sub-claim in a sketch; proof of Prop 4.6(a), l. ~629: "Since $v_2(1+r^{s})=3$ for odd $s$ when $r\equiv7\pmod8$").**
- **Problem.** For odd s, v₂(1+r^s) = v₂(1+r), which equals 3 only if r ≡ 7 (mod 16). For r = 31 and 47 it is 5 and 4. PT2 (l. 377–380, after R69) uses only "≥ 3".
- **Repair.** Follow PT2's wording. In the case j=1 we have F = 1+2r^s with s = a+2b odd. Since r^s ≡ r (mod 16) and 2r ≡ 14 (mod 16) for r ≡ 7 (mod 8), this gives −F = −1−2r^s ≡ 1 (mod 16), which contradicts w ≡ 9 (mod 16). Use only "v₂(1+r^s) ≥ 3" (to get the 2-adic level t ≥ 4), never "= 3".

**D6 (MINOR, overclaim; Remark 4.13, l. ~778 and Problem 2, l. 1164: "An explicit summable bound for the number of $f$ with given $t_{\min}$ would therefore close the question").**
- **Problem.** Summability alone does not suffice. The tail Σ_{f≥Y} 2^{5−t_min(f)} must be shown smaller than μ(U_Y), which is known only at Y = 10¹⁰ (≥ 0.6086). Pushing Y further requires recomputing U_Y. The source (PT3:195) states the quantitative condition.
- **Repair.** Write "An explicit bound making $\sum_{f\ge10^{10}}2^{5-t_{\min}(f)}<0.6$ would close the question; summability alone (let alone $o(2^T)$) does not suffice."

**D7 (MINOR, wording drift; §6 status paragraph, l. ~1118: "so what is needed is an explicit bound (6.1)").**
- **Problem.** (6.1) is sufficient, not shown necessary. R83 n6 had changed the source to "closing the P-tail amounts to…" and labelled it Assessment.
- **Repair.** Write "so it would suffice to have an explicit bound (6.1)…".

**D8 (MINOR; Lemma 2.4 statement, l. ~265).**
- **Problem.** "$\Sigma\subset\Zhu$ clopen, defined modulo $M$ (a union of reduced classes modulo $M$)" is literally inconsistent, because a union of classes of Ẑ is not inside Ẑ^× (§A.1).
- **Repair.** Write "$\Sigma=\{x\in\Zhu: x\bmod M\in R\}$ for a set $R$ of reduced residues modulo $M$ (so $\Sigma$ is clopen in $\Zhu$; note $\Zhu$ is closed but not open in $\Zh$)". Apply the same reading to Σ_r, Σ_hard and Σ_r^np.

**D9 (MINOR, exposition; Prop 2.5 final sentence and Problem 1).**
- **Problem 1.** The "iff" passes silently from "finitely many ET classes" to "finitely many primitive classes solvable by polynomials". The I3 class is a union of several classes mod 4cdf. An I2 class with (c,f) > 1 contains no units at all.
- **Repair 1.** Add: "Each ET class is a finite union of residue classes modulo $M(\kappa)$; the non-primitive ones contain at most finitely many primes, and each primitive one is solvable by polynomials by Lemma 2.1."
- **Problem 2.** Problem 1's "equivalently" is correct (§A.3) but unproved in the paper.
- **Repair 2.** Add "(the square points form a closed set, and a clopen subset of $\Zhu$ is defined modulo some $M$; apply Lemma 2.4 and Prop 2.5)". Also write "whose primes, up to finitely many, admit no finite covering".

**D10 (MINOR, label; Thm 4.2(iii)).** The item is tagged "(proved)" but contains "Under H, $C^*(r)=X_r$". **Repair:** split it as "(proved) $X_r=\infty$ iff …; (conditional on H) $C^*(r)=X_r$ …".

**D11 (MINOR, citation; Lemma 4.4).** It is stated for general r but cited to [PT2, Lemma 2.1], which is stated for Σ₇. The general-r statement is PT2 §4 ("Lemma 2.1 holds verbatim"). **Repair:** cite "[PT2, Lemma 2.1 and §4]".

**D12 (MINOR; Lemma 4.7, "explicitly computable from the factorisation of $f+1$").** The source (PT3:45) also uses $r^{v_r(f-1)}$, since $r^{a+b} \mid f-1$. **Repair:** write "from the factorisations of $f+1$ and the $r$-part of $f-1$".

**D13 (MINOR; after Prop 3.1, "ET also derive it from their vanishing result").**
- **Problem.** ET only assert "(this also follows from Proposition 1.6)" (p. 8) and do not carry out the derivation. For composite odd squares, passing from polynomial solutions to Type I/II solutions needs coprimality, which ET do not discuss.
- **Repair.** Write "ET remark that it also follows from their vanishing result…".
- **Suggested addition.** Note that the Mordell-hard paragraph uses only the elementary x = 1 case, so that statement does not depend on the Mordell–Schinzel citation (only on ET Prop 1.9).

**D14 (MINOR; Comp 4.8, last sentence: "On ten test points with known certificates … identical certificate sets").**
- **Problem.** By PT3:79–80, four of the ten points have no certificates (counts 3, 0, 0, 0, 13, 35, 7, 4, 2, 0). The (7, −15) comparison matches only after removing F = 15 certificates (R72 D1).
- **Repair.** Write "On ten test points (six with certificates, 66 certificates in total) the two engines agree, after the F = 15 normalisation of [PT3, …]".

**D15 (MINOR, bibliography; [Mordell] "Academic Press, 1969, Chapter 30").**
- **Problem.** ET's ref. [44] reads "Diophantine Equations, **volume 30** of Pure and Applied Mathematics, Academic Press, 1969". "Chapter 30" looks like a conflation with the series volume. The book was not accessed, so the chapter cannot be confirmed.
- **Repair.** Write "Pure and Applied Mathematics 30, Academic Press, London–New York, 1969 (not accessed; cited via [ET])". Drop the chapter.

**D16 (MINOR, bibliography verification; point 4 of O86).** Checked against Crossref (and ET's reference list / LITERATURE_2026.md):

| entry | status |
|---|---|
| BL | Bull. LMS 52(4) 746–761 (2020) ✓ (also LITERATURE_2026.md:14 and the arXiv PDF title) |
| BE | Illinois J. Math. 55(2) (2011) ✓. Title ✓. Pages 685–696 not confirmable from Crossref (no page data); plausible. |
| CHN | Math. Comp. 77 (no. 261) 531–545 ✓ (online 2007, volume 2008) |
| NR | Canad. Math. Bull. 26(4) 485–492 (1983) ✓ |
| Lenstra | Math. Comp. 42 (no. 165) 331–340 (1984) ✓ |
| ET | J. Aust. Math. Soc. 94(1) 50–105 (2013) ✓ |
| SS | Acta Arith. 4 185–208 (1958) ✓ |
| Schinzel | Funct. Approx. 28 (2000) ✓. Pages 187–194 from ET [68] ✓. |
| Yamamoto | matches ET [88] ✓ |
| MD | The author order "S. Mihnea and B. C. Dumitru" follows LITERATURE_2026.md ("Spiridon Mihnea, Bogdan C. Dumitru"). The given name / surname split is **unverified**; check it on the arXiv page. |

**Repair:** for BE, add "no. 2"; otherwise none.

## C. Other points raised in O86

- **Point 5 (sketches of Prop 4.11 and the Lemma 6.1 classification).** These are acceptable as labelled sketches with exact pointers. The source reviews (R72, R83 Claim A) re-derived them.
- **Point 6 (length).** Dropping Thm 4.3 is not recommended. It is the only statement that explains why no bound ck_min ≤ f(n_p) is provable without refuting H. If space is needed, shorten the Comp 4.8 provenance prose and the Data paragraph of §5.3 instead.
- **Novelty hedging.** The hedging is adequate throughout:
  - Theorem C is described as a "partial novelty".
  - Thm 5.1 is called a repackaging of Salez, with Mihnea–Dumitru credited.
  - ET's "finite set of covering congruence strategies" remark (p. 6) is quoted correctly.
  - Bright–Loughran is cited for the Brauer–Manin identification.

  The phrase "the classical Mordell–Schinzel obstruction" in the abstract is fine.
- **Self-containedness.** The paper is self-contained except for:
  - the cited ET results (Prop 1.7 proof, Prop 1.9, Lemma 2.8);
  - Mordell–Schinzel;
  - the internal working notes, for the sketched proofs and the certified computations.

  This is correctly signposted.

## D. Scripts (from scratch; none reuse the author's code)

- `scripts/review_r86_families.py`: Lemma 2.1 identities, integrality and positivity on 367,524 (family, triple, n) cases.
- `scripts/review_r86_typei.py`: Thm 4.1 census for p < 3·10⁵, and ck_min ≥ n_p for hard p < 6·10⁴.
- `scripts/review_r86_sign.py`: Prop 4.6(b), the residue-one cover, and a small exhaustive search at x̂₉ (ck ≤ 6000).
- `scripts/review_r86_r13.py`: third-engine replay of both r = 13 certificates. The earlier reviewer script `review_mordell_check.py` was also re-run: both certificates OK.
- `scripts/review_r86_m17.py`: brute force over the seven families, modulus ≤ 10⁵, for level ≤ 2 boxes on the 17-generic line.
