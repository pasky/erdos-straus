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
* N = 10⁹: see below (run in progress at time of writing).
Small-|L₃| census (`scripts/review_hj_census.c 200000`, own enumeration n = d·v − u): 30 non-square n ≡ 1 (4) < 2·10⁵ with
1 ≤ |L₃| ≤ 6, 18 of them all −1; |L₃| = 2 at 17, 29, 41, 69; |L₃| = 4 all −1 at 33, 45, 125, 189, 209 (also 13 has |L₃|=4 with
N₋=2, and 1617 with |L₃|=4 all −1 — the note's "e.g." list is not exhaustive, fine). N₊ > N₋ at 1 385 n, first 97, 241, 265;
min N₋/|L₃| = 1/12 at n = 111969. All ✓. Coin model q = 0.7: I get Σ 0.3^{#reversal classes} ≈ 2.8 (✓ "≈ 2–3");
P(0 | Poisson 2.8) ≈ 0.06, so "not significant" is fair (borderline).
