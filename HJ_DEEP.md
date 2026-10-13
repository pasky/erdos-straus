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
   (W) admits no finite-covering proof (Lemma 3.2, PROVED).
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
numerator t = 4cd at denominator cn, divided by c.
*Proof.* (4acd − 1)(4bcd − 1) = 16abc²d² − 4cd(a+b) + 1 = 4c²d·(4abd − e) + 1 = 4cd·cn + 1, so K(a,4cd,b) = cn.
Conversely, from 4abcd − a − b = cn we get c(4abd − n) = a + b, so e := 4abd − n > 0 and a + b = ce. ∎
So **ES_II(p) ⟺ for some c ≥ 1, the number cp has a length-3 HJ fraction whose middle letter is ≡ 0 (mod 4c)**. DK's
five-slice theorem is the case c = 1, where the modulus 4c = 4 is fixed and can be traded for a sign. For c > 1 the moving
modulus 4c returns (B2).

**Prop 2.2 (sign law).** For every Type II word, A = 4cd·a − 1 satisfies (A/p) = −(−1/p).
*Proof.* A ≡ 3 (mod 4), so by reciprocity (A/p) = (−1/p)(p/A). From A·A* = 4cd·cp + 1 we get p·4c²d ≡ −1 (mod A), so
(p/A) = (−1/A)(4c²d/A) = −(d/A) (c is coprime to A, because A ≡ −1 mod c). Write d = 2^j d′. Since A ≡ −1 (mod d′) and
A ≡ 3 (mod 4), (d′/A) = (−1/d′)(A/d′) = (−1/d′)² = 1. If j ≥ 1 then 8 | 4cd, so A ≡ −1 (mod 8) and (2/A) = 1. Hence
(d/A) = 1 and (A/p) = −(−1/p). ∎
This is the HJ form of (I)7 (Yamamoto; Bright–Loughran: on Type II, (f/p) = −(−1/p), with f = A). For p ≡ 1 (4), **every
Type II solution is a short word at cp whose letter-pair (A mod p) is a non-residue**. So the general Type II problem is
"some multiple cp has a short word with middle ≡ 0 (4c)", and the sign is never the obstruction.
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
