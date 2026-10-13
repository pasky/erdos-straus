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
