# HJ_DEEP — the Hirzebruch–Jung / Farey reformulation in depth: one sign, one shape (O174)

Status: internal research note, SPARK phase. **ES is not solved here, nor any infinite case of it.** Labels as in
DISCOVERIES.md. Builds on DEDEKIND_ES.md (DK) and the memos BRAINSTORM/bsA_*.md. Scripts `scripts/bsA_*`.
Notation as in DK: n/A = [[v,t,u]], A = tu − 1, A* = tv − 1, L₃(n) = length-3 words (letters ≥ 2), λ(n) = least HJ
length of a Jacobi non-residue.

## 0. Summary
1. **A single identity behind every length-3 word (§1, PROVED).** tuv − u − v = n ⟺ t/n = 1/(uv) + 1/(un) + 1/(vn).
   ES's (A)3 slice is the case t = 4c. All of Type II is the same identity at the numerator cp with 4c | t, and the
   sign is then automatic: (A/p) = −(−1/p) (§2, PROVED, elementary).
2. **SQ₅ splits into a sign-free half and a pure-sign half (§3, EVIDENCE to 10⁸).**
   * (W) Every n ∉ E_W = {2, 3, 5, 6, 9, 11, 14, 15, 35, 105, 510} has a length-3 word. The SQ₅ exception 105 is a
     (W)-exception, i.e. 105 has no length-3 word at all.
   * (S) For non-square n ≡ 1 (4), L₃(n) ≠ ∅ ⟹ L₃(n) contains a Jacobi −1 word.
   Both hold for all n < 10⁸ (`scripts/bsA_ws.c`). So SQ₅ (interior five slices) holds for every non-square n ≡ 1 (4),
   n < 10⁸, n ∉ {5, 105}. That is 100× DK's range. (S) is exactly the statement that "T1 is the only obstruction".
   (W) admits no proof by a finite covering with fixed-pair families (Lemma 3.2, PROVED). **(W) is exactly an open question of Lorenzini**
   (*The critical polynomial of a graph*, 2022, Example 6.2(a)): xyz − x − z is the critical polynomial of the path A₃, and his
   conjectural exceptional list is E_W ∪ {0, 1}.
3. **One-line forms of the sign** (memos; PROVED for r ≤ 5): sign = (w·w − n − r + 1)/4 mod 2 with w the Wu vector of
   the plumbing (bsA_wu_rokhlin_sign). HJ length = popcount of Minkowski's ?(A/n) (bsA_minkowski_stern).
4. Construction log (§4): six attempts, each steered by a named barrier hypothesis. None escapes. The final reduction of
   (S) is a precise "sign set restricted to a divisor class" statement (Prop 4.1), i.e. H-A.

## 1. The master identity (PROVED, one line)
**Lemma 1.1.** For integers t, u, v ≥ 1 and n ≥ 1: `tuv − u − v = n ⟺ t/n = 1/(uv) + 1/(un) + 1/(vn)`.
*Proof.* 1/(uv) + (u+v)/(uvn) = (n + u + v)/(uvn), which equals t/n iff n + u + v = tuv. ∎
So a length-3 HJ fraction n/A = [[v,t,u]] is the same thing as a three-term "Type II-shape" expansion of t/n.
* t = 4c gives 4/n = 1/(cuv) + 1/(cun) + 1/(cvn): DK Cor 1.2's (A)3 slice.
* The other four DK slices (4 | tu−1, tv−1, u, v) are the same word read through Type I a = 1 and the e-slice (DK Thm 4.5).
So **(W) below asks: for every n, does *some* numerator t ≥ 2 admit this shape with u, v ≥ 2?** ES asks for t ≡ 0 (mod 4)
(or the four sister cells), and the sign theorem turns "the sister cells" into "Jacobi −1".

## 2. All of Type II is length-3 HJ words at multiples of p; the sign is automatic (PROVED)
**Prop 2.1 (dictionary).** The ET Type II parameter tuples (a,b,c,d), i.e. 4abd = n + e with a + b = ce (CONDITIONAL_ES
Lemma 1.2; every Type II solution of a prime arises so), are in bijection with the words
`K(a, 4cd, b) = 4abcd − a − b = cn` (letters a, b ≥ 1, middle 4cd). The ES triple (abd, acdn, bcdn) is Lemma 1.1 with
numerator t = 4cd at denominator cn (giving 4d/n = 1/(ab) + 1/(acn) + 1/(bcn)), divided by d.
*Scope (R-self repair).* The outer letters a, b may equal 1, so these are **formal** three-letter words K(a,4cd,b). They are genuine
HJ fractions of length 3 only when a, b ≥ 2. For example 4/5 = 1/2 + 1/5 + 1/10 has (a,b,c,d) = (1,2,1,1) and formal word [[2,4,1]] = [[2,3]].
An interior word forces p = 4abd − (a+b)/c ≥ 4ab − a − b ≥ 12.
*Proof.* (4acd − 1)(4bcd − 1) = 16abc²d² − 4cd(a+b) + 1 = 4c²d·(4abd − e) + 1 = 4cd·cn + 1, so K(a,4cd,b) = cn.
Conversely, from 4abcd − a − b = cn we get c(4abd − n) = a + b, so e := 4abd − n > 0 and a + b = ce. ∎
So **ES_II(p) ⟺ for some c ≥ 1, the number cp is K(a, t, b) for a formal word with a, b ≥ 1 and middle t ≡ 0 (mod 4c)**. DK's
five-slice theorem is the case c = 1, where the modulus 4c = 4 is fixed and can be traded for a sign. For c > 1 the moving
modulus 4c returns (B2).

**Prop 2.2 (sign law).** For every Type II word, A = 4cd·a − 1 satisfies (A/p) = −(−1/p).
*Proof.* A ≡ 3 (mod 4), so by reciprocity (A/p) = (−1/p)(p/A). From A·A* = 4cd·cp + 1 we get p·4c²d ≡ −1 (mod A), so
(p/A) = (−1/A)(4c²d/A) = −(d/A) (c is coprime to A, because A ≡ −1 mod c). Write d = 2^j d′. Since A ≡ −1 (mod d′) and
A ≡ 3 (mod 4), (d′/A) = (−1/d′)(A/d′) = (−1/d′)² = 1. If j ≥ 1 then 8 | 4cd, so A ≡ −1 (mod 8) and (2/A) = 1. Hence
(d/A) = 1 and (A/p) = −(−1/p). ∎
This is the HJ form of (I)7 (Yamamoto; Bright–Loughran: on Type II, (f/p) = −(−1/p), with f = A). For p ≡ 1 (4), **every
Type II solution is a formal three-letter word at cp whose A mod p is a non-residue**. So the general Type II problem is
"some multiple cp has a formal three-letter word with middle ≡ 0 (4c)", and the sign is never the obstruction.
EVIDENCE/CERTIFIED (`scripts/bsA_typeII_words.py 3000`): all 9 431 Type II solutions (a ≤ b) of primes p < 3000 rebuilt.
4/p was checked in exact rationals, together with the word identity and the HJ expansion (cp)/A = [[v, 4cd, u]] (letters ≥ 2):
0 failures. Sign table (both orientations): p ≡ 1 (4): 6 376 words, all −1; p ≡ 3 (4): 12 486, all +1. At odd squares < 3000:
0 Type II words (T1).

**Lemma 2.3 (scaling is a reparametrisation; PROVED).** DK 8.3 (K(av′, t, au′) = a·K(v′, at, u′)) maps a multiplier-c′ Type II
word [[v′, 4c′d′, u′]] with a² | d′ to the multiplier-ac′ word [[av′, 4c′d′/a, au′]]. Both give the *same* ES triple
(u′v′d′, u′c′d′p, v′c′d′p), since in ET coordinates (a·u′)(a·v′)(d′/a²) = u′v′d′, etc. So the only sign-flipping transfer in DK
moves between parametrisations of one solution and creates nothing at fixed p.
*Remark (Type I, general a).* The same computation for ET Type I (4abd = tn + 1, a + b = ct) gives
K(a, 4cd, b) = c(t(n−1) + 1). The numerator is not a multiple of n, so general Type I has no fixed-numerator word form. (Only
a = 1, Lemma 1.1 at n with 4 | A, is a word of n.) I found no better HJ encoding of Type I with a > 1.

## 3. SQ₅ = (W) ∧ (S): a sign-free half and a pure-sign half
For n ≡ 1 (4), the interior five-slice condition is "L₃(n) contains a Jacobi −1 word" (DK Thm 4.5). Split it as follows.
* **(W) (sign-free existence; CONJECTURE).** Every integer n ≥ 2, n ∉ E_W := {2, 3, 5, 6, 9, 11, 14, 15, 35, 105, 510} is
  tuv − u − v with t, u, v ≥ 2. By Lemma 1.1 this says t/n has a Type-II-shape expansion for *some* t ≥ 2.
* **(S) (pure sign; CONJECTURE).** If n ≡ 1 (4) is not a square and L₃(n) ≠ ∅, then some word of L₃(n) has (A/n) = −1.
Trivially, for n ≡ 1 (4): interior-SQ₅(n) ⟺ (W)(n) ∧ (S)(n). At odd squares (W) holds (n ≥ 25), but the analogue of (S) *without* the
non-square hypothesis fails there, because Jacobi is +1 on all of L₃(m²). (S) itself excludes squares. So **(S) is precisely the
statement "T1 is the only obstruction for words"**,
and (W) is a T1-free divisor problem.

**EVIDENCE 3.1 (`scripts/bsA_ws.c`, exhaustive enumeration of all words with tuv − u − v < N; 54 s for N = 10⁸).**
* (W): the exceptions below 10⁸ are exactly E_W. This was cross-checked independently by the HJ algorithm over all A for n < 3000.
* (S): there are **0 violations** below 10⁸. No odd square < 10⁸ has a −1 word (Prop 3.1 control).
* Hence interior five-slice ES holds for every non-square n ≡ 1 (4), 13 ≤ n < 10⁸, n ≠ 105. This extends DK 9.1 from 10⁶ to
  10⁸, and it explains DK's lone exception: **105 has no length-3 word at all** (105 ∈ E_W). The sign plays no role there.
* Small-|L₃| census (`scripts/bsA_smallL3.py 200000`). Only 30 non-square n ≡ 1 (4) < 2·10⁵ have 1 ≤ |L₃(n)| ≤ 6, and
  every one has a −1 word. 18 of the 30 are *all* −1, e.g. 17, 29, 41, 69 with |L₃| = 2, and 33, 45, 125, 189, 209 with |L₃| = 4.
  The independent-coin model with q = 0.7 per reversal pair predicts ≈ 2–3 all-(+1) cases among them. Observing 0 is mild
  evidence that signs within L₃(n) are positively correlated toward −1, but it is not significant.
* No injection: N₊(n) > N₋(n) occurs at 1 385 non-square n ≡ 1 (4) < 2·10⁵ (first 97, 241, 265, …). The minimum of N₋/|L₃| is
  1/12, at n = 111969. So (S) cannot be proved by a sign-reversing injection L₃⁺ → L₃⁻.

**Lemma 3.2 (no finite covering of (W) by fixed-pair families; PROVED).** A word with two letters fixed holds on a residue class:
(t,u) fixed ⟺ n ≡ −u (mod tu − 1) (then v = (n+u)/(tu−1)), and similarly for (t,v); (u,v) fixed ⟺ n ≡ −(u+v) (mod uv).
For any finite family of such pairs, let M be the lcm of the moduli. Then **the class n ≡ −1 (mod M) meets none of them**.
Type (t,u) would need tu − 1 | u − 1 (type (t,v) is the same with u ↔ v), and type (u,v) would need uv | u + v − 1, both impossible for letters ≥ 2 since
0 < u − 1 < tu − 1 and 0 < u + v − 1 < uv. ∎
So (W), like ES, cannot be settled by fixed-pair congruence families. It needs moving moduli or some other idea. The escaping class n ≡ −1 is exactly where the excluded boundary t = 1
((u−1)(v−1) = n+1) would work, just as ES's escaping class (squares) is where the sign is trivial.
Numerically (`scripts/bsA_cover2.py M`), the uncovered fraction of ℤ/M is 0.16 % (M = 720720) and 0.09 % (M = 12252240), and
it contains 105, 366, 510, 1806, 1905, … and M − 1.
**Literature: (W) is an open question of Lorenzini.** D. Lorenzini, *The critical polynomial of a graph* (preprint dated
4 Dec 2022; PDF at dinolorenzini.franklinresearch.uga.edu, text checked by me). For a graph G, d_G = det(Diag(x) − A_G). For G = A₃
this is d_{A₃} = xyz − x − z, which is exactly our chain Gram determinant (bsA_selling_sandpile). Example 6.2(a) says that
"computations indicate" the complement of V_{A₃}(2) is contained in L_{A₃} = [0,1,2,3,5,6,9,11,14,15,35,105,510], and the text
continues: "It is natural to wonder whether d_{A₃} takes every non-negative value when x, y, z ≥ 2, except for the values listed
in L_{A₃}. We have not been able to answer this question beyond the following remarks". Prop 6.3 (partial results) covers even
n except possibly n = 2^m − 2 with m odd or m = 2, 4 (the latter give the genuine exceptions 2 and 14), odd n with n + 2 composite, and n ≡ 1 (4) with n ≡ 2, 8 (9). His proof uses the z = 2 and z = 4 slices, i.e.
our u = 2, 4 shapes. **So (W) is precisely Lorenzini's A₃ question**, and EVIDENCE 3.1 checks it to 10⁸. His computational range
is not stated in the text I read. Remark 6.4 notes that among the values 2^{2m+1} − 2 = 0, 6, 30, 126, 510, … the values 0, 6 and 510 are not achieved,
while 30 and 126 are achieved exactly once.
*Reading.* SQ₅ on n ≡ 1 (4) = Lorenzini's A₃ critical-polynomial question + the pure-sign statement (S). ES's five slices are
"the critical polynomial of the path A₃ takes the value p at a point where the critical group's pairing is non-square"
(bsA_selling_sandpile D2–D3). (W) is T1-free, has a published status (open), and is the natural first target for any H-A
technology. Lemma 3.2 shows why Lorenzini's congruence arguments (Prop 6.3) cannot finish it.

## 4. Construction log (barrier as steering wheel)
**Prop 4.1 (exact reduction of (S); PROVED, elementary).** Fix n odd and t ≥ 2. The words with middle t are the factorisations
tn + 1 = X·Y with X ≡ Y ≡ −1 (mod t) and X, Y ≥ 2t − 1 (X = A). Give each prime q | tn + 1 the sign σ_n(q) := (q/n). Then
sign(word) = Π_{q^k ‖ X} σ_n(q)^k, and the product over all prime factors of tn + 1 is ((tn+1)/n) = 1. So the complementary
divisor Y has the same sign, which is the reversal symmetry. Hence
**For n ≡ 1 (4) non-square with L₃(n) ≠ ∅: (S) fails at n ⟺ for every t, every admissible divisor X of tn + 1 lies in the kernel of the character σ_n on the divisor group.**
At n = m², σ_n ≡ 1 (T1). At non-squares σ_n is a non-trivial character, but the admissible divisors form a sparse set,
whose structure is the moving-modulus class condition X ≡ −1 (mod t). This is the SYNTHESIS_SPARKS skeleton (sign layer
= genus character on prime factors; class layer = individual divisor in a class) in its sharpest form.

Attempts. Each names the hypothesis it tried to violate, then the outcome.
* **C1. Radius growth (violates "fixed finite slice set").** Let the HJ radius R grow. Pigeonhole gives
  λ(p) ≤ (6/π² + o(1)) ln²p unconditionally (bsA_farey_lnr_pigeonhole Thm 3). But there is no ES meaning for R ≥ 4: the divisor form is
  *exactly* length 3 (Lemma 1.1). **Dead (B3).**
* **C2. Multiplier growth (violates "fixed numerator").** Allow cp (Prop 2.1). The sign is now automatic (Prop 2.2), but the
  class condition becomes 4c | t with a moving modulus. The union over c is the full Type II count, ≍ log³p *on average* over p (no pointwise lower bound is known). **Reduces to H-A.**
* **C3. Sign-flipping transfers (violates "symmetries preserve the sign").** Scaling is the only flip (DK 8.3). At fixed p it is a
  reparametrisation (Lemma 2.3), rotations preserve the sign (DK 8.2), and Vieta moves act on the wrong space (bsA_fricke_vieta F2).
  **Dead (PROVED as stated).**
* **C4. Genus/lattice moves (violates "abelian data only").** By bsA_selling_sandpile D3 and Thm W, the sign is the Wu class.
  Kneser neighbours at primes q ∤ n preserve all local data at n, hence the Wu class. Passing from G⁺ to G⁻ needs a change at the
  primes dividing n, which is the sign layer again. **Dead.**
* **C5. Injections and parity (H-B).** There is no sign-reversing injection L₃⁺ → L₃⁻ (1 385 counterexamples, §3). The product of
  signs over L₃(p) is +1 at primes (reversal pairs). Parity laws of sub-counts were already screened by DK C5 (820 sub-counts,
  none odd for all p ≡ 1 (24)). **No mechanism.**
* **C6. Prove the sign-free half (W) first (violates "T1 blocks every route": T1 does not apply to (W)).** Explicit shapes give the
  following. u = 2 works unless n + 2 is prime or a power of 2. t = 2 works unless 2n + 1 is prime. u = 3 works unless n + 3 has no
  proper divisor ≡ 2 (mod 3) that is ≥ 5, and so on. A finite list of shapes would have to exclude infinitely many prime
  constellations (n + 2, 2n + 1, … all prime). That is not known unconditionally. By Lemma 3.2, no finite covering by fixed-pair families proves it (other congruence
  constructions are not classified there).
  **(W) needs H-A too, but it is the cleanest T1-free test bed** for a moving-modulus argument.

## 5. Verdict (Assessment) and exact scope
* **PROVED:** Lemma 1.1 (master identity), Prop 2.1 (Type II = multiplier words), Prop 2.2 (sign law (A/p) = −(−1/p), the HJ form
  of (I)7), Lemma 2.3 (scaling = reparametrisation), Lemma 3.2 (no finite covering for (W)), Prop 4.1 (exact reduction of (S)).
  From the memos: Thm W (sign = Wu-square, r ≤ 5), M1 (HJ length = popcount ∘ ?), Thm 3 (Farey least non-residue ≪ ln²p),
  D1–D3 (Selling/sandpile/genus), F1–F2 (Fricke cubic, no Vieta route).
* **EVIDENCE:** (W) with exceptional set E_W, and (S), both for all n < 10⁸. Hence interior SQ₅ for all non-square n ≡ 1 (4), n < 10⁸ (n ≠ 5, 105).
* **CONJECTURE:** (W); (S). Together they are equivalent to interior SQ₅ on n ≡ 1 (4), which implies ES for primes p ≡ 1 (4).
* **Assessment.** The HJ reformulation is now as clean as I can make it: **one shape (length 3, equivalently t/n has a Type-II-shape
  expansion) and one sign (the Wu/Jacobi class)**. The two halves are separately simple: (W) is T1-free with finitely many
  exceptions, and (S) is "T1 is the only obstruction". Their *conjunction* is ES's class layer, and every mechanism I tried
  sees only one half at a time. No route to ES. The most useful outputs for the campaign are the (W)/(S) split (which isolates a
  T1-free sub-problem with a sharp exceptional set) and the 10⁸ verification.
