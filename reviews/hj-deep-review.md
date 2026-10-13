# R174 — hostile review of O174 (HJ_DEEP.md + BRAINSTORM/bsA_*.md)

Reviewer branch `side-agent/review-hj-deep`; author branch `side-agent/spark-hj-brainstorm` merged at start.
From-scratch scripts: `scripts/review_hj_*` (none reuse author code).

## Summary verdicts
(filled at the end)

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
