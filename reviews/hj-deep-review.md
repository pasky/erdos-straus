# R174 — hostile review of O174 (HJ_DEEP.md + BRAINSTORM/bsA_*.md)

Reviewer branch `side-agent/review-hj-deep`; author branch `side-agent/spark-hj-brainstorm` merged at start.
From-scratch scripts: `scripts/review_hj_*` (none reuse author code).

## Summary verdicts
**Overall: no FATAL defect. One MAJOR (a quantifier error in the headline equivalence (W) ∧ (S) ⟺ interior SQ₅, trivially
repairable) and ~16 MINOR.** Every numerical claim I re-ran from scratch reproduced exactly; (W)/(S) extended to 10⁹.

| Claim | Verdict |
|---|---|
| HJ_DEEP Lemma 1.1 (master identity) | SOUND |
| Prop 2.1 (Type II = formal words K(a,4cd,b) = cn) | SOUND |
| Prop 2.2 (sign law (A/p) = −(−1/p)) | SOUND (true for all odd n; = Yamamoto Lem. 4 / GEOMETRY_ES Prop 5.2 in HJ dress, as the note says) |
| Lemma 2.3 (scaling = reparametrisation) | SOUND |
| §3 split interior-SQ₅(n) ⟺ W(n) ∧ S(n) (pointwise) | SOUND (tautological given DK Thm 4.5) |
| §5 "(W); (S) together are equivalent to interior SQ₅ on n ≡ 1 (4)" | **GAP → SOUND-AFTER-REPAIRS** (D1, MAJOR) |
| EVIDENCE 3.1: E_W exact, (S) 0 violations, to 10⁸ | SOUND (reproduced with a different algorithm; extended to **10⁹**) |
| "interior SQ₅ for all non-square n ≡ 1 (4) < 10⁸ except 5, 105" | SOUND (EVIDENCE; full λ ≤ 3 SQ₅ holds at 5 too) |
| Small-|L₃| census, no-injection numbers | SOUND (all numbers reproduced) |
| "(W) is exactly Lorenzini's open question" | SOUND-AFTER-REPAIRS (quotations verified on arXiv:2311.06367; cite the JNT 2024 version, D2) |
| Lemma 3.2 (no finite fixed-pair covering) | SOUND (D11 minor) |
| Prop 4.1 (exact reduction of (S)) | SOUND (a reformulation; D10) |
| bsA_wu Thm W (r ≤ 5) | SOUND (reproduced; also random r ≤ 10) |
| bsA_wu Rokhlin reading | GAP → SOUND-AFTER-REPAIRS (orientation sign wrong under the standard convention for n ≡ 3 (4); mod 16 drops Arf term; ES case n ≡ 1 (4) unaffected; D3) |
| bsA_minkowski M1–M3 | SOUND (M1 re-checked to n < 2000: 1 215 787 pairs) |
| bsA_farey Lemma 1, 2, Thm 3 | SOUND (Yao–Knuth statement verified) |
| bsA_lens P1–P4 | SOUND-AFTER-REPAIRS (criterion ±k² correct; minor scope/citation points D7) |
| bsA_toric_ksb_wahl K2 | SOUND but vacuous sign framing (D5) |
| bsA_fricke_vieta F1–F3 | SOUND (F1 reproduced; F2 scope wording D15) |
| bsA_selling_sandpile D1–D3 | SOUND (D14 minor) |
| bsA_hecke H1–H3 | SOUND as labelled |
| bsA_farey_graph_metric λ_F = λ | SOUND, but provable outright whenever λ ≤ 3 (D6) |

## Claim-by-claim checks

### HJ_DEEP Lemma 1.1 (master identity) — SOUND
1/(uv) + 1/(un) + 1/(vn) = (n+u+v)/(uvn); equals t/n iff n+u+v = tuv. One line, correct for all integers ≥ 1.
The bullet "t = 4c gives 4/n = 1/(cuv)+1/(cun)+1/(cvn)" is correct (divide the identity by c).

### Prop 2.1 (Type II = formal words K(a,4cd,b) = cn) — SOUND
Re-derived: with K(x,y,z) = xyz − x − z, 4abcd − a − b = c(4abd − e) = cn using a + b = ce; converse c(4abd − n) = a + b
forces e := 4abd − n > 0 and c | a+b. ES triple: 1/(abd) + 1/(acdn) + 1/(bcdn) = (cn + a + b)/(abcdn) = c(n+e)/(abcdn) = 4/n. ✓.
"Bijection" is between tuples (a,b,c,d) and pairs (c, word) — the word alone at numerator cn records c = N/n and d = T/(4c),
so this is fine; it is *not* a bijection with ES triples (Lemma 2.3 exhibits collisions) — the text does not claim that.
Bound p ≥ 4ab − a − b ≥ 12 for a, b ≥ 2: ✓. The reliance on ET Props 2.2/2.6 ("every Type II solution of a prime arises
so") is correctly cited via CONDITIONAL_ES Lemma 1.2.

### Prop 2.2 (sign law (A/p) = −(−1/p) on Type II) — SOUND (in fact holds for every odd n, not only primes)
Re-derived step by step: A = 4cda − 1 ≡ 3 (4) ⇒ (A/n) = (−1/n)(n/A) (Jacobi reciprocity, gcd(A,n) = 1 because
A·A* = 4c²d·n + 1). 4c²d·n ≡ −1 (mod A) and (−1/A) = −1 give (n/A) = −(d/A) (c, 2 coprime to A). For d = 2^j d′:
A ≡ −1 (mod d′) and reciprocity give (d′/A) = (−1/d′)² = 1; j ≥ 1 ⇒ 8 | 4cd ⇒ A ≡ −1 (8) ⇒ (2/A) = 1. ✓
Nothing in the proof uses primality; the statement is true for every odd n (Jacobi symbol), which the text could say.

### Lemma 2.3 (scaling = reparametrisation) — SOUND
K(av′,t,au′) = a²tu′v′ − a(u′+v′) = a·K(v′,at,u′). With middle 4c′d′/a, multiplier ac′, one needs 4ac′ | 4c′d′/a ⟺ a² | d′,
exactly the stated hypothesis; then d = d′/a² and (a u′)(a v′)(d′/a²) = u′v′d′ etc.: same ES triple. Note also that
A is literally unchanged: A_new = (4c′d′/a)(a u′) − 1 = 4c′d′u′ − 1 = A_old. ✓ (MINOR wording, see defects.)
Type I remark: 4abcd − a − b = c(tn+1) − ct = c(t(n−1)+1). ✓

### §3 split interior-SQ₅ = (W) ∧ (S) — SOUND (tautological given DK Thm 4.5), with a scope caveat
For n ≡ 1 (4): interior-SQ₅(n) :⟺ ∃ A ∈ L₃(n) with (A/n) = −1 (DK Thm 4.5). Writing W(n) :⟺ L₃(n) ≠ ∅ and
S(n) :⟺ (L₃(n) ≠ ∅ ⇒ ∃ −1 word), the equivalence interior-SQ₅(n) ⟺ W(n) ∧ S(n) is pure logic. ✓
Caveat: "SQ₅" in DK §9 is λ(n) ≤ 3 (boundary length-2 certificates included). The note's "SQ₅ (interior five slices)" is the
*stronger* interior statement; at n = 5 the full SQ₅ holds (5/2 = [[3,2]], (2/5) = −1, λ(5) = 2) while interior SQ₅ fails.
The note does say "interior" in §0/§3, but AGENT_REPORT SHARP 1 says "interior SQ₅ holds … except 5 and 105" and §5 says
"(W);(S) together are equivalent to interior SQ₅ on n ≡ 1 (4)" without the exceptional set → see defect list.

### EVIDENCE 3.1 ((W) exceptions = E_W, (S) 0 violations, to 10⁸) — SOUND (independently reproduced; extended, see below)
Own equivalent form: n = tuv − u − v (t,u,v ≥ 2) ⟺ n + u = d·v with d = tu − 1 = A, i.e.
**n + u has a divisor d ≡ −1 (mod u), d ≥ 2u − 1, with cofactor v ≥ 2**; WLOG u ≤ v (reversal A ↔ A* = tv − 1 preserves the
Jacobi sign since AA* = tn + 1 ≡ 1 mod n), whence 2u(u − 1) ≤ n. Also gcd(A, n) = 1 automatically.
`scripts/review_hj_ws.c` searches *per n* (smallest-prime-factor table + divisor enumeration of n + u, early exit; every hit
is reconstructed and re-verified as tuv − u − v = n; Jacobi computed directly, not via DK's cell rule). Odd squares are
enumerated *completely*. Result for N = 10⁸ (9 s):
* (W) exceptions in [2, 10⁸): exactly 2 3 5 6 9 11 14 15 35 105 510 = E_W. ✓
* (S) violations: 0. ✓  Odd squares < 10⁸ (4 999 of them): 0 words with Jacobi −1 (T1 control). ✓
* By-product (new, EVIDENCE): every n < 10⁸ outside E_W has a word with **min(u,v) ≤ 12** (max of the least outer letter is 12,
  attained at n = 1379). So empirically eleven one-letter shapes u ∈ {2,…,12} (each a *moving-modulus* divisor condition:
  n + u has a divisor ≡ −1 (mod u) in [2u−1, (n+u)/2]) already cover (W). Lemma 3.2 says nothing about such one-letter
  families; this sharpens the C6 discussion.
* **N = 10⁹** (same program, ~5 min, 4 GB spf table): (W) exceptions in [2, 10⁹) are again exactly E_W; (S) violations 0;
  15 810 odd squares, none with a −1 word; least outer letter still ≤ 12 for every n ∉ E_W. So the note's 10⁸ claims are
  confirmed and extend to 10⁹ (EVIDENCE).
Small-|L₃| census (`scripts/review_hj_census.c 200000`, own enumeration n = d·v − u): 30 non-square n ≡ 1 (4) < 2·10⁵ with
1 ≤ |L₃| ≤ 6, 18 of them all −1; |L₃| = 2 at 17, 29, 41, 69; |L₃| = 4 all −1 at 33, 45, 125, 189, 209 (also 13 has |L₃|=4 with
N₋=2, and 1617 with |L₃|=4 all −1 — the note's "e.g." list is not exhaustive, fine). N₊ > N₋ at 1 385 n, first 97, 241, 265;
min N₋/|L₃| = 1/12 at n = 111969. All ✓. Coin model q = 0.7: I get Σ 0.3^{#reversal classes} ≈ 2.8 (✓ "≈ 2–3");
P(0 | Poisson 2.8) ≈ 0.06, so "not significant" is fair (borderline).

### Lorenzini attribution ("(W) is exactly Lorenzini's open question") — SOUND-AFTER-REPAIRS (citation details)
Source accessed: arXiv:2311.06367v1 (dated 14 Nov 2023), saved as `sources/r174/lorenzini-2311.06367.{pdf,txt}`; published
as D. Lorenzini, *The critical polynomial of a graph*, **J. Number Theory 257 (2024) 215–248** (confirmed by the citation in
Wang–Lu, EJC 33(3) (2026) #P3.80, `sources/r174/wang-ejc-v33i3p80.{pdf,txt}`). I did not access the 4 Dec 2022 website PDF the
author used; the arXiv text agrees verbatim on every quoted point:
* Example 6.2(a): "Computations indicate that the complement of V_{A₃}(2) in ℤ≥0 is contained in the following set
  L_{A₃} := [0, 1, 2, 3, 5, 6, 9, 11, 14, 15, 35, 105, 510]." ✓ (also stated in the Introduction, p. 6).
* "It is natural to wonder whether d_{A₃}(x,y,z) = xyz − x − z takes every non-negative value when x, y, z ≥ 2, except for
  the values listed in L_{A₃}. We have not been able to answer this question beyond the following remarks." ✓
* Prop 6.3 (a)(b)(c) as summarised ✓; Remark 6.4 (0, 6, 510 not achieved; 30, 126 achieved "exactly once", (3,4,3) and
  (12,2,6)) ✓ — "exactly once" is up to the x ↔ z symmetry; 126 has the two ordered words (6,2,12), (12,2,6) (my check).
* Identification: our tuv − u − v with middle t is d_{A₃}(x,y,z) with (x,y,z) = (u,t,v); "x,y,z ≥ 2" = letters ≥ 2; and
  L_{A₃} = E_W ∪ {0,1}. ✓. Our computation shows every element of E_W is a genuine exception, so the question is exactly
  "(W) ⟺ complement of V_{A₃}(2) equals L_{A₃}" (Lorenzini only asserts "contained in"; the equality of the finite part is
  our computation). ✓
* Status: Wang–Lu (2026) still describe cofiniteness of the complement as open for general G ("it remains an open problem
  whether the complement of V_{d_G}(2) in ℤ≥0 is finite") and prove only density of a subset. A web search found no
  resolution of the A₃ case. So "open" is accurate to the best of my search.
* Small inaccuracy: Lorenzini's proof of 6.3(a) uses the fixed pair (x,z) = (4,6) (for 2^m − 2, m even ≥ 6) in addition to
  the z = 2 and z = 4 slices; the note says "His proof uses the z = 2 and z = 4 slices". MINOR.
* "His computational range is not stated" — correct for the arXiv text too.

### Lemma 3.2 (no finite fixed-pair covering of (W)) — SOUND (with a residue-level caveat)
Re-derived: (t,u) fixed ⇒ n + u = v(tu−1) ⇒ n ≡ −u (mod tu−1); (u,v) fixed ⇒ n ≡ −(u+v) (mod uv). In the class
n ≡ −1 (mod M), a (t,u)-family would need tu−1 | u−1 with 0 < u−1 < tu−1 (impossible), a (u,v)-family uv | u+v−1 with
0 < u+v−1 < uv (since uv − u − v + 1 = (u−1)(v−1) ≥ 1; impossible). ✓
Caveat (MINOR): "(t,u) fixed ⟺ n ≡ −u (mod tu−1)" is only "⟹"; the converse needs the third letter ≥ 2
(n ≥ 2tu − u − 2). Irrelevant for the lemma (which only uses ⟹).
Scope: the lemma says nothing about one-letter families (u fixed, t and v free — a moving-modulus divisor condition),
and empirically those already suffice for (W) to 10⁹ with u ≤ 12 (above). The note correctly says "other congruence
constructions are not classified there"; the §0 phrase "admits no proof by a finite covering with fixed-pair families" is
accurate. Numerics re-done from scratch (`scripts/review_hj_cover.py`): uncovered fraction 0.1607 % (M = 720720; first
uncovered residues 15, 105, 366, 510, 1455, 1806, 1905, …) and 0.0852 % (M = 12252240; 105, 366, 510, 1806, 1905, …),
M − 1 uncovered in both. ✓ (the note's "0.09 %" is a rounding of 0.085 %; fine).

### Prop 4.1 (exact reduction of (S)) — SOUND (but it is a tautological restatement; label it so)
Words with middle t ⟷ factorisations tn+1 = XY, X ≡ Y ≡ −1 (mod t), X, Y ≥ 2t−1: (X+1)(Y+1)/t² = uv and
XY = t(tuv − u − v) + 1 ✓ both ways. (X/n) = Π σ_n(q)^k by multiplicativity of the Jacobi symbol in the top argument ✓;
((tn+1)/n) = (1/n) = 1 ⇒ (Y/n) = (X/n) ✓. The displayed "⟺" is then the definition of (S) rewritten. σ_n = (·/n) is a
non-trivial Dirichlet character mod n iff n is not a square ✓. Nothing is wrong; but "PROVED" + "sharpest form" oversells a
restatement — suggest "PROVED (reformulation)".

### §4 construction log — spot checks
* C2: "Type II count ≍ log³p on average" — ET Thm 1.1 gives Σ_{p≤N} f_II(p) ≍ N log²N, i.e. average ≍ log³N over primes ✓.
* C5: "product of signs over L₃(p) is +1 at primes (reversal pairs)": correct, but the reason is incomplete — one also needs
  that there are no palindromes u = v at primes (A = A* ⇒ A² ≡ 1 (p) ⇒ A = p − 1, whose HJ length is p − 1 ≠ 3). At composite
  n palindromes exist (n = 21 has |L₃| = 1). MINOR.
* C6 shape claims re-derived: u = 2 fails ⟺ n + 2 is an odd prime or a power of 2 ✓; t = 2 fails ⟺ 2n + 1 prime ✓
  ((2u−1)(2v−1) = 2n+1); u = 3 as stated ✓. The concluding sentence "A finite list of shapes would have to exclude infinitely
  many prime constellations … That is not known unconditionally" understates the heuristic situation: under Schinzel's
  hypothesis H one expects every fixed finite list of one-letter shapes to fail infinitely often (choose n with each n + u
  equal to a small cofactor times a prime in a suitable class), so finite shape lists are conditionally *refuted*, not
  merely unproved — while my data show u ≤ 12 suffices below 10⁹. This contrast is worth one sentence. MINOR (Assessment).

### bsA_wu_rokhlin_sign Thm W (sign = Wu square) — SOUND (r ≤ 5 PROVED rel. DK Cor 4.1); Rokhlin reading GAP (orientation)
* Re-checked from scratch (`scripts/review_hj_wu.py`, own continuants, own Jacobi, own mod-2 solve for ε):
  exhaustive letters 2..9, r ≤ 5: **24 692 odd words, 0 failures** (same count as the author); random words r ≤ 10, letters
  ≤ 200: 39 278 odd words, 0 failures (this does *not* use DK Cor 4.1, so it also tests Cor 4.1's mod-8 dependence);
  w·w − n − r + 1 ∈ {0, 4} (mod 8) always ✓; odd squares m < 60, all A with r ≤ 9: 10 948 words, all have w·w ≡ n + r − 1
  (W2 ✓).
* The r ≤ 5 proof is valid: ε depends on letters mod 2, w·w = Σε_i b_i − 2Σε_iε_{i+1} and n mod 8 on letters mod 8, and
  (A/n) on letters mod 8 for fixed r by DK Cor 4.1 (PROVED). (The same argument proves every fixed r by a 8^r check; the
  limit 5 is arbitrary.)
* Cor W1's second sentence ("the genus G⁻(p) is exactly {Λ : w·w ≡ p + 6 (8)}" for general ternary lattices) rests on the
  general-lattice EVIDENCE / an unverified van der Blij–Milgram recollection, not on the r ≤ 5 proof. Label it EVIDENCE. MINOR.
* **Rokhlin reading.** Kaplan's formula is μ(Y) ≡ σ(X) − L′·L′ + 8·Arf(L′) (mod 16) for a characteristic sublink L′ (Kaplan,
  Trans. AMS 254 (1979), from my memory too — I could not access it); the memo drops the Arf term, so its "mod 16" is not
  justified, but **mod 8 the Arf term vanishes**, so the mod-8 statement is robust. The sign convention is not: with the
  common convention L(p,q) = −p/q surgery on the unknot (Gompf–Stipsicz §5.3), L(n,A) bounds the *negative*-definite plumbing
  (σ = −r, w·w = −εᵀGε), giving μ(L(n,A)) ≡ εᵀGε − r, hence **(A/n) = +1 ⟺ μ(L(n,A)) ≡ n − 1 (mod 8)** (sanity: L(n,1) bounds
  the Euler-number −n disc bundle, μ = n − 1; Poincaré sphere = ∂(−E₈) gives μ = −8 ≡ 8 ✓ for the σ − w² convention).
  The memo's "1 − n" is the opposite orientation (+p/q surgery). For n ≡ 1 (mod 4) — the only ES case — 1 − n ≡ n − 1 (mod 8),
  so the ES content is unaffected; for n ≡ 3 (4) the memo's statement is wrong under the standard convention. MINOR; repair:
  state the orientation convention and "mod 8 only".

### bsA_minkowski_stern M1–M3 — SOUND (M1: proof sketch from two classical conversions + exhaustive check)
* What is PROVED vs checked: M1's proof is a sketch combining (i) Salem's/Denjoy's binary expansion of ?, quoted from memory,
  and (ii) the classical regular-CF → HJ-string conversion (the same as bsA_farey Lemma 2). Both inputs are classical and
  correct; the terminal-block bookkeeping is the only original step. The "exhaustive check n < 200" is a check, not part of
  the proof. Acceptable as PROVED (relative to classical facts); better to cite the conversion (e.g. Hirzebruch's/
  Riemenschneider's duality, or Popescu-Pampu's "The geometry of continued fractions and the topology of surface
  singularities") instead of "from memory".
* Re-checked from scratch (`scripts/review_hj_minkowski.py 2000`; ? computed from the exact series
  2Σ(−1)^{j+1}2^{−(a₁+…+a_j)} with big integers, HJ length by the direct ceiling algorithm): **M1 holds for all 1 215 787
  coprime pairs with n < 2000, 0 failures.** M2 (?(s(m)/s(2^k+m)) = m/2^k and coprimality) for all 16 369 pairs k ≤ 13, 0
  failures. M3 is then a correct transcription of DK Cor 4.6 (p ≡ 1 (8)), using that M2 is a bijection between reduced
  A/p ∈ (0,1) and odd-or-reduced dyadics (classical Stern–Brocot fact; my k ≤ 13 check covers it numerically). ✓
* MINOR: the barrier paragraph has a garbled sentence ("… is a heuristic guess only, with / with a bilinear continuant
  structure …") — duplicated "with", dangling clause.

### bsA_farey_lnr_pigeonhole Lemma 1, Lemma 2, Thm 3 — SOUND
* Lemma 1: r(p/q) = 1 + r(q/c); any HJ word with all letters ≥ 2 and length r has numerator ≥ r + 1, so r(q/c) ≤ q − 1 ✓.
  (Checked r(n/A) ≤ A for all coprime pairs n < 2000.) λ ≤ n_p uses that the least QNR is prime ✓.
* Lemma 2 re-checked for all 1 215 786 coprime pairs 3 ≤ n < 2000: 0 failures ✓.
* Thm 3: for p ≡ 1 (4), A ↦ p − A preserves QNR; min(r(p/A), r(p/(p−A))) ≤ S(A)/2; λ ≤ ½·avg_QNR S ≤ Σ_{A<p} S(A)/(p − 1).
  ✓ (the step avg_QNR S ≤ 2·avg_all S uses S ≥ 0 only — correct, if wasteful).
  **Citation verified** (PubMed abstract of Yao–Knuth, PNAS 72 (1975) 4720): "The sum of all partial quotients in the regular
  continued fraction expansions of m/n, for 1 ≤ m ≤ n, is 6π⁻² n (ln n)² + O(n log n (log log n)²)." ✓ Hence
  λ(p) ≤ (6/π²) ln²p + O(ln p (ln ln p)²) unconditionally ✓. Numerically Σ S/(p ln²p) = 0.773 (p = 10009), 0.741 (p = 100049),
  converging slowly to 0.608, consistent with the error term.
* The GRH comparison (Bach: n_p < 2 ln²p) is correct but is a comparison against a crude conversion; "first unconditional
  polylog bound" is plausible but unsupported beyond a negative literature search (Assessment) — fine as labelled.
* Rukavishnikova is flagged "NOT verified" ✓ (correctly conditional).

### bsA_lens_homotopy_surgery P1–P4 — SOUND-AFTER-REPAIRS (minor citation/orientation points)
* **P1 criterion.** The classical statement (Whitehead 1941; e.g. Hatcher's/Cohen's expositions) is: L(p,q) ≃ L(p,q′) iff
  qq′ ≡ ±k² (mod p), and *orientation-preserving* homotopy equivalent iff qq′ ≡ k² (mod p). With q′ = 1: L(p,A) ≃ L(p,1) iff
  A or −A is a square mod p. The memo states this correctly (I could not access Whitehead's paper; the criterion is standard
  textbook material). For p ≡ 1 (4) prime, −1 is a square, so ≃ L(p,1) ⟺ (A/p) = +1 ✓, orientation irrelevant ✓.
  Cosmetic: "L(p,1) = S³_p(unknot)" holds only up to orientation (with L(p,q) = −p/q surgery, S³_p(U) = −L(p,1) = L(p,−1));
  harmless for homotopy type.
* Scope numerics re-done (`scripts/review_hj_lens.py`, own brute force of L₃(m²) and of the ±square criterion):
  25: 2 of 4 (A = 3, 17); 169: 4 of 10; 289: 6 of 8; 841: 8 of 16 — all ✓, and Jacobi = +1 on every word ✓. (Extra: at
  m² with every prime of m ≡ 3 (4), e.g. 49, every unit is ±square, so 0 such words — consistent.)
* **P2.** Linking-form argument is standard and correct: Y_{±p}(K) for K ⊂ ℤHS³ has H₁ = ℤ/p generated by a meridian with
  self-linking ±1/p, while L(p,A) has a generator with self-linking ±A/p (convention-dependent sign / inverse); so A ≡ ±k².
  Greene, *The lens space realization problem*, Ann. Math. 177 (2013) 449–511 — scope as now stated (classifies lens spaces
  that are positive integral surgery on knots in S³; a subset of the QR side) ✓. Not accessed by me beyond the abstract
  level; the necessary condition used is elementary and does not depend on Greene.
* **P3.** "(A/p) is an invariant of K up to mirror": mirror is A ↦ −A, so this needs (−1/p) = 1; true in the stated context
  (p ≡ 1 (8)) but false as a general statement for p ≡ 3 (4). MINOR wording. Lisca G&T 11 (2007): lens spaces bounding ℚHB⁴
  need p = m² ✓ (|H₁| of a ℚHB⁴ boundary is a square).
* **P4.** Matveev's bound c(L(p,q)) ≤ S(p,q) − 3 ✓ (classical). The attribution "sharp in proven cases (Jaco–Rubinstein–
  Tillmann, J. Topology 2009, p even)" is from memory and, to my recollection, inaccurate in scope: JRT J. Topol. 2 (2009)
  treat the family L(2n,1) (and a few related families); the general even-p cases came in later JRT papers (ℤ₂-Thurston norm).
  I could not verify either. MINOR: mark "from memory, scope unverified" or cite precisely.

### Prop 2.1/2.2 EVIDENCE recount — SOUND
`scripts/review_hj_typeII.py 3000` (own enumeration: a ≤ b, then the d-window (n+1)/(4ab) ≤ d ≤ (n+a+b)/(4ab)): 9 431 Type II
tuples at primes < 3000, 0 identity failures (exact rationals), sign table {p ≡ 1 (4): 6 376 × (−1); p ≡ 3 (4): 12 486 × (+1)}
— identical to the note. Extra: the sign law holds for all 55 532 oriented words at **all odd non-square n < 3000** (composites
included), confirming the remark under Prop 2.2; 0 tuples at odd squares ✓.
Note on wording: the evidence line says the HJ expansion "(cp)/A = [[v,4cd,u]] (letters ≥ 2)" was checked — the author's script
checks it only for a, b ≥ 2 (correct, since outer letter 1 is not an HJ word); the sentence should say "when a, b ≥ 2". MINOR.

### bsA_toric_ksb_wahl K1–K3 — SOUND, but K2's sign framing is vacuous (MINOR)
K2 re-derived: T-singularities are 1/(dm²)(1, dma − 1) (KSB 1988 Prop 3.10; plus the A_k, which are the m = 1 case); at prime
index p = dm² forces m = 1, A ≡ −1, i.e. A_{p−1} = [[2,…,2]] of length p − 1. **But this already excludes every length-3 word at
every prime p ≥ 5, QR or QNR**, since length 3 ≠ p − 1. The sentence "(−1/p) = +1 for p ≡ 1 (4). So for p ≡ 1 (4) no ES
certificate singularity is ℚ-Gorenstein smoothable" suggests a sign mechanism where there is none; no length-3 singularity of
prime index is ℚ-Gorenstein smoothable. Repair: state K2 as a length statement; the "complement of the QR side" reading
should be dropped. K1, K3 (dual string [[2^{v−2},3,2^{t−3},3,2^{u−2}]], Christophersen–Stevens from memory) fine as labelled.

### bsA_fricke_vieta F1–F3 — SOUND (F2's "precise negative answer" is scoped to this embedding)
`scripts/review_hj_fricke.py`: for all 1 331 words with v,t,u ≤ 12: γ = M(v)M(t)M(u) = [[n,−A*],[A,−t]], T = tuv − t − u − v,
(x,y,z) = (A*−1, A−1, uv−2), and the displayed Fricke cubic all hold exactly (0 failures). F2 is correct as a statement about
this embedding (Vieta moves fix the boundary traces (v,t,u,T), which carry all ES data). "Precise negative answer to the
Markoff question" is too strong: it rules out Vieta moves *in this particular character-variety embedding*, not every
Markoff-type encoding of ES words. MINOR: say "for the Fricke embedding by boundary traces". F3 with the R-self repair
(T ≥ 3, "three-letter periodic presentation") is fine; the ⟺ there is DK Thm 4.5 restated.

### bsA_selling_sandpile D1–D3 — SOUND (one understatement)
D1 conorms (v−1, t−2, u−1, 1, 1, 0) and D2 (reduced Laplacian; tree number = det = n) verified symbolically and for all
v,t,u ≤ 12 (`scripts/review_hj_fricke.py`). D2 says the sandpile group is ℤ/n "when that group is cyclic (always so when n is
prime)": in fact it is **always** cyclic for a linear chain (the 2×2 minor on rows {1,2}, columns {2,3} is 1; checked). MINOR.
D3: (G⁻¹)₁₁ = A/n, (G⁻¹)₃₃ = A*/n ✓; the p-adic symbol of an odd ternary lattice of determinant p is ⟨unimodular rank 2⟩ ⊕ ⟨pε⟩,
two values distinguished by the square class of ε ✓. "Siegel mass formula, ≍ p classes (from memory)" — plausible
(mass ≍ p for ternary determinant p), unverified. The Lorenzini citation repeats "preprint, 4 Dec 2022" (see defect list).

### bsA_hecke_cusp_excursions H1–H3 — SOUND as labelled
H1 (torus diag(k,k⁻¹) acts on P¹(𝔽_p) by A ↦ k²A; orbits on 𝔽_p^* are QR, QNR) ✓. H2 correctly labelled heuristic; the
Gauss-sum line is right (Σ_A χ(A)e(mA/p) = χ(m)G(χ) for real χ). H3's dictionary is DK's; the size statement is labelled
average-only ✓. No defects beyond style.

### bsA_farey_graph_metric — SOUND, but the main "EVIDENCE/CONJECTURE λ_F = λ" is essentially trivial (MINOR)
The memo's own distance-2 bullet (d_F(∞, p/A) ≤ 2 ⟺ A | p ± 1, and divisors of p − 1 are QRs for p ≡ 1 (8)), together with
d_F = 1 only at A = 1, **proves** λ_F(p) = 2 ⟺ λ(p) = 2. Since λ_F ≤ λ, it follows that λ_F(p) = λ(p) for every p with λ(p) ≤ 3,
i.e. for every p ≡ 1 (8) where five-slice ES holds (all p < 10⁶ by DK). The BFS evidence for p < 6000 is therefore implied,
and "CONJECTURE λ_F = λ" is only open when λ(p) ≥ 4, which never happens in range. Repair: state this as a PROVED remark; the
"my expectation was wrong / sign freedom does not trivialise anything" reading should be weakened accordingly (the distance-3
signed words were never needed).

## Defects (numbered; location → suggested repair)

**D1 (MAJOR, quantifier error).** HJ_DEEP §5 CONJECTURE bullet: "(W); (S). Together they are equivalent to interior SQ₅ on
n ≡ 1 (4)", and §0 item 2 / AGENT_REPORT "SQ₅ = (W) ∧ (S)". (W) as stated quantifies over **all** n ≥ 2 (even n, n ≡ 3 (4)),
so the global conjunction (W) ∧ (S) is *strictly stronger* than interior SQ₅ on n ≡ 1 (4); only the pointwise statement
interior-SQ₅(n) ⟺ W(n) ∧ S(n) (n ≡ 1 (4)) is an equivalence, and globally one must also exclude the (W)-exceptions 5, 105.
Likewise "(W) is exactly Lorenzini's question" is true for the global (W), which is *more* than ES needs. Repair: write
"interior SQ₅ on non-square n ≡ 1 (4), n ∉ {5, 105} ⟺ (W)|_{n ≡ 1 (4)} ∧ (S); Lorenzini's question is the global (W), a
strengthening" (and for ES at primes only (W)|_{p ≡ 1 (4) prime} ∧ (S)|_{primes} is needed).

**D2 (MINOR, citation).** HJ_DEEP §0 item 2 and §3 "Literature", bsA_selling_sandpile "Literature", AGENT_REPORT SHARP 1:
"preprint dated 4 Dec 2022". The paper is published: D. Lorenzini, *The critical polynomial of a graph*, J. Number Theory 257
(2024) 215–248, arXiv:2311.06367 (text saved in `sources/r174/`). All quotations agree with the arXiv text. Also, Lorenzini's
Prop 6.3 proof uses the fixed pair (x,z) = (4,6) for 2^m − 2 besides the z = 2, 4 slices; and "achieved exactly once" in
Remark 6.4 is up to x ↔ z. Add: Wang–Lu, EJC 33(3) (2026) #P3.80 still list cofiniteness as open (density only).

**D3 (MINOR, bsA_wu "Rokhlin reading").** With L(p,q) = −p/q surgery on the unknot (Gompf–Stipsicz), L(n,A) bounds the
negative-definite plumbing, μ ≡ εᵀGε − r (mod 8), and Thm W gives (A/n) = +1 ⟺ μ(L(n,A)) ≡ **n − 1** (mod 8) (sanity:
μ(L(3,1)) = 2, computed both from the −3 disc bundle and from the even −A₂ plumbing of L(3,2) = −L(3,1)). The memo's 1 − n
is for −L(n,A); the two agree iff n ≡ 1 (4), so ES is unaffected. Kaplan's mod-16 formula carries an extra 8·Arf(L′) term
that the memo omits; it vanishes mod 8. Repair: state the orientation convention, "mod 8", and that the statement is
convention-dependent for n ≡ 3 (4); keep "from memory" for Kaplan.

**D4 (MINOR, bsA_wu Cor W1 label).** "the genus G⁻(p) is exactly {Λ : w·w ≡ p + 6 (8)}" for general ternary lattices is not
covered by the r ≤ 5 proof (which is about linear plumbings); label EVIDENCE/classical-from-memory.

**D5 (MINOR, bsA_toric_ksb_wahl K2).** At prime index the only T-singularity is A_{p−1} of HJ length p − 1, so *no* length-3
singularity (QR or QNR) is ℚ-Gorenstein smoothable for p ≥ 5; the appeal to (−1/p) = +1 and the "certificates lie outside the
QR world" reading is vacuous. Repair: state K2 as a length statement; drop the sign framing.

**D6 (MINOR, bsA_farey_graph_metric).** The memo's own distance-2 analysis proves λ_F(p) = 2 ⟺ λ(p) = 2, hence λ_F = λ
whenever λ ≤ 3 (all p ≡ 1 (8) < 10⁶ by DK). Replace "CONJECTURE λ_F = λ (EVIDENCE p < 6000)" by this PROVED remark and
weaken the "sign freedom does not trivialise anything" reading (distance-3 signed words never enter).

**D7 (MINOR, bsA_lens).** P3 "(A/p) is an invariant of K up to mirror" needs (−1/p) = 1 (mirror is A ↦ −A); say "for p ≡ 1 (4)".
P4: the JRT attribution ("J. Topology 2009, p even") is from memory and likely too broad (the 2009 paper treats L(2n,1));
mark scope unverified. Cosmetic: L(p,1) = S³_p(U) only up to orientation.

**D8 (MINOR, HJ_DEEP §4 C5).** "product of signs over L₃(p) is +1 at primes (reversal pairs)" also needs "no palindromes u = v at
primes" (A = A* forces A = p − 1, of HJ length p − 1). Add that half-line.

**D9 (MINOR, HJ_DEEP §4 C6, Assessment).** "A finite list of shapes would have to exclude infinitely many prime constellations
… not known unconditionally": under Schinzel's H one expects every fixed finite list of one-letter shapes to fail infinitely
often, so such lists are conditionally refuted, not merely unproved. Worth recording the contrasting EVIDENCE found here:
every n < 10⁹ outside E_W has a word with min(u,v) ≤ 12 (max 12, at n = 1379).

**D10 (MINOR, Prop 4.1 label).** The displayed ⟺ is the definition of (S) rewritten via multiplicativity of (·/n); label
"PROVED (reformulation)" and soften "sharpest form".

**D11 (MINOR, Lemma 3.2).** "(t,u) fixed ⟺ n ≡ −u (mod tu − 1)" is only ⟹ (the converse needs v = (n+u)/(tu−1) ≥ 2). The
proof uses only ⟹; fix the symbol.

**D12 (MINOR, Prop 2.2 scope, improvement).** The proof never uses primality; the sign law holds for every odd n (checked for
all odd non-square n < 3000, 55 532 oriented words). Say so; it is consistent with "Type II words do not exist at squares".

**D13 (MINOR, Prop 2.2 EVIDENCE wording).** "the HJ expansion (cp)/A = [[v, 4cd, u]] (letters ≥ 2)" — the script checks it only
when a, b ≥ 2 (correctly); write "(when a, b ≥ 2)".

**D14 (MINOR, bsA_selling_sandpile D2).** The sandpile group of a linear chain is always cyclic (a 2×2 minor equals 1), not only
"when n is prime".

**D15 (MINOR, bsA_fricke_vieta F2).** "Precise negative answer to the Markoff/Vieta/BGS question" holds for the boundary-trace
(Fricke) embedding only; say so.

**D16 (MINOR, bsA_minkowski_stern).** Garbled sentence in the barrier screen ("… a heuristic guess only, with / with a bilinear
continuant structure …"). M1's proof cites the Salem/Denjoy expansion and the CF→HJ conversion "from memory"; give a reference
(e.g. Popescu-Pampu, *The geometry of continued fractions and the topology of surface singularities*, 2007) — the result itself
is verified to n < 2000.

**D17 (MINOR, HJ_DEEP §4 C1).** "there is no ES meaning for R ≥ 4: the divisor form is exactly length 3 (Lemma 1.1)" — Lemma 1.1
shows length-3 words ⟺ Type-II-shape expansions; it does not show longer words have no Egyptian-fraction reading. Label the
"Dead" verdict as Assessment.

## Scripts (all from scratch, none reuse author code)
`review_hj_ws.c` ((W)/(S) per-n divisor search, to 10⁹), `review_hj_census.c` (small-|L₃| census, N₊/N₋), `review_hj_cover.py`
(Lemma 3.2 numerics), `review_hj_wu.py` (Thm W), `review_hj_minkowski.py` (M1, M2, Lemma 1–2, Thm 3 sanity),
`review_hj_lens.py` (P1 scope), `review_hj_fricke.py` (F1, D1–D2, cyclicity), `review_hj_typeII.py` (Prop 2.1/2.2 recount).
Sources fetched: `sources/r174/lorenzini-2311.06367.*`, `sources/r174/wang-ejc-v33i3p80.*`.
