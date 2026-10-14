# FRIEZE_ES — the A₂ frieze dictionary of the five ES slices, deepened (task O210, spark relay Y2)

Status: in progress (O210). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on LENGTH_THREE.md (O206), DEDEKIND_ES ((J)9), CHI_FLIP, MODEL_SPECIFIC ((J)32). Memos BRAINSTORM/y2_*,
scripts scripts/y2_*.

Notation. Word (c, m, s) ∈ ℤ³_{≥1}, N = mcs − c − s > 0, h = cm − 1, h′ = ms − 1. The quiddity cycle
(q₁, …, q₅) = (h′, c, m, s, h) sits at the vertices V₁, …, V₅ of the pentagon. Its frozen sides are
(V₁V₂, …, V₅V₁) = (1, 1, 1, 1, N), and the Ptolemy relations are
`q₁q₂ = N + q₄, q₂q₃ = 1 + q₅, q₃q₄ = 1 + q₁, q₄q₅ = N + q₂, q₅q₁ = 1 + N q₃`.   (P)

## 0. Iteration log
(I1) SVZ lifting (Short–Van Son–Zabolotskii, arXiv:2312.12953, Thm 1.6: a tame frieze mod n lifts to ℤ iff its
Farey-complex path is strongly contractible). Guess: the ES sign is the mod-4 homotopy class. **Killed**: every
closed 5-walk on F₄ (the octahedron) is strongly contractible (`y2_f4_walks.py`; §2). Modification: the
obstruction cannot be topological mod 4; it must be 2-adic of depth 3. This led to (I2).
(I2) Mod 2 the pentagon frieze is rigid, and the sign is a 2-adic bit of the unique even edge (§1, PROVED).

## 1. The even-edge theorem (PROVED; CERTIFIED for all 5 115 860 formal words, odd N ≤ 10⁵)

**Lemma 1.1.** For odd N, exactly two cluster variables are even, and they are adjacent. (Proof: memo y2_even_edge.)

**Theorem 1.2.** For every positive formal word with N odd: (h′/N) = (−1/N)·(−1)^{[8 | ee′]}, where e, e′ is the even edge.

*Proof, case A (e, e′) = (c, m)* (the mirror (m, s) is the same under reversal). Here s, h, h′ are odd and
h = cm − 1 ≡ −1 (mod 2^{a+b}), with a = v₂(c), b = v₂(m) ≥ 1, so h ≡ 3 (4).
1. hh′ = 1 + Nm gives (h′/N) = (h/N).
2. Reciprocity: (h/N) = (N/h)(−1)^{(h−1)(N−1)/4} = (−1/N)(N/h).
3. hs = N + c gives (N/h) = (−c/h) = −(c/h).
4. Write c = 2^a c′. Then h ≡ −1 (c′), so (h/c′) = (−1/c′), and (c′/h) = (h/c′)(−1/c′) = 1 because h ≡ 3 (4).
   So (c/h) = (2/h)^a.
5. If a + b ≥ 3, then h ≡ 7 (8) and (2/h) = 1. If a = b = 1, then h ≡ 3 (8) and (c/h) = −1.

So (h′/N) = −(−1/N)·(−1)^{[cm ≡ 4 (8)]} = (−1/N)(−1)^{[8 | cm]}.

*Case B (e, e′) = (h′, c)* (mirror (s, h)). Here m, s, h are odd. Write b = v₂(h′), h′ = 2^b h″.
1. h′c = N + s gives N ≡ −s (h″) and s ≡ −N (4).
2. (h′/N) = (2/N)^b (h″/N) = (2/N)^b (N/h″) ε₁, with ε₁ = (−1)^{(h″−1)(N−1)/4}.
3. (N/h″) = (−1/h″)(s/h″) and (s/h″) = (h″/s) ε₂, with ε₂ = (−1)^{(s−1)(h″−1)/4}.
4. ms = 1 + h′ gives h′ ≡ −1 (s), so (h″/s) = (2/s)^b (−1/s).
5. The sign ε₁ε₂(−1/h″) = (−1)^{((h″−1)/2)((N+s−2)/2 + 1)} = 1, because (N + s − 2)/2 is odd.
6. Hence (h′/N) = (2/(Ns))^b (−1/s), with (−1/s) = −(−1/N).
7. Ns = −N² + N h′c ≡ −1 + h′c (mod 8).
   * If 8 | h′c: Ns ≡ 7 and the factor is 1.
   * Otherwise b = v₂(c) = 1: Ns ≡ 3 (8) and the factor is −1.

*Case C (e, e′) = (h, h′)* (the frozen side N). Here c, m, s are odd, and hh′ = 1 + Nm gives m ≡ −N (4).
1. As in B: (h′/N) = (2/N)^b (N/h″) ε₁.
2. N ≡ −s (h″) and ms ≡ 1 (h″), so (N/h″) = (−1/h″)(m/h″).
3. (m/h″) = (h″/m)(−1)^{(m−1)(h″−1)/4}.
4. hh′ ≡ 1 (m) and h ≡ −1 (m) give (h′/m) = (−1/m), so (h″/m) = (2/m)^b(−1/m).
5. The signs cancel because (N + m − 2)/2 is odd.
6. Hence (h′/N) = (2/(Nm))^b(−1/m), with (−1/m) = −(−1/N) and Nm = hh′ − 1.
7. Conclude as in B. ∎

**Corollary 1.3 (DK Thm 4.5 extended).** For N ≡ 1 (4) and every formal word: (h′/N) = −1 ⟺ 8 | ee′ ⟺ some q_i ≡ 0 (mod 4).
**Corollary 1.4 (T1).** At odd squares every positive pentagon frieze has ee′ ≡ 4 (mod 8).
CERTIFIED: `scripts/y2_even_edge.py 100000`, 0 failures, 8 068 square-control words (`logs/y2_even_edge_1e5.txt`).

*Remark (what this replaces).* DK proved Thm 4.5 by a 512-cell check mod 8. CHI_FLIP gave a 2-adic Hasse-invariant
proof. Here the proof is three Jacobi computations, one per position of the even edge, each using two Ptolemy relations:
the one through the even edge and one through the odd opposite vertex.

## 2. The 2-adic transport and the tree picture (PROVED; memo y2_twoadic_tree_transport)

From the case proofs: if o is the odd cluster variable opposite the even edge, then
`(h′/N) = −(−1/N)(2/o)` (even edge {c,m} or {m,s}), and `(h′/N) = −(−2/N)(2/o)` (the relation through o contains N).
**For N ≡ 1 (8): (h′/N) = −(2/o).** CERTIFIED: `scripts/y2_transport.py 2000`, all cells.
In the Bruhat–Tits tree T₂ the five ends form two cherries plus a lone end o. The sign is "the cherry depths sum to
≥ 3", and T1 is "both cherries have depth exactly 1".

## 3. Where T1 lives: positivity (PROVED by inspection; memo y2_positivity_is_T1)

The proof of Thm 1.2 uses positivity only in the reciprocity steps. Signed (tame) friezes at odd squares do have
zero-mod-4 quiddities (`scripts/y2_signed.py 40`). So T1 is the archimedean factor of Hilbert reciprocity, entering
through the positivity of the frieze. Consequences:
* SVZ's lifting theory (tame, signed) is T1-blind. Every closed 5-walk on F₄ is strongly contractible (§0, I1).
* Finite-ring frieze theory is N-blind beyond N mod 8.
* **Any frieze-theoretic ES proof must use the positivity of the frieze archimedeanly.**

## 4. Polygon size: the pentagon is the unique size where the zero locus is a Jacobi fibre (memo y2_hexagon_degeneration)

Let Z_r(N) be "some interior word of HJ length r at N has a short diagonal (quiddity) ≡ 0 (mod 4)". Each such vertex
gives 4/N as r unit fractions (vertex fan).
* r = 2: for N ≡ 1 (4), Z₂ is empty, because xy = N + 1 ≡ 2 (4) (PROVED).
* r = 3: Z₃ ⟺ some word has (h′/N) = −1 (Thm 1.2). This is a Jacobi fibre, empty at squares (T1).
* r = 4: **Z₄(N) holds for every N ≡ 1 (4), N ≥ 9**, via the word (2, 2, 2, (N+3)/4). Its 4-diagonal K(2,2,2) = 4 cuts
  off a free triangle that contains the N-side (PROVED, explicit identity). In particular Z₄ holds at all odd squares.
* r ≡ 0 (4): (2^{r−1}, k) has K = rk − r + 1 and end quiddity K(2^{r−1}) = r ≡ 0 (4). Its N-class is 1 (mod r), which
  contains odd squares (PROVED).
* 5 ≤ r ≤ 12: explicit odd-square witnesses (`scripts/y2_witness.py 12 40`): r = 5: 25 = K(2,3,2,2,3); r = 6:
  49 = K(2,2,3,2,2,4); r = 7: 81; r = 9: 49; r = 10: 81; r = 11: 225 (CERTIFIED).
So for r ∈ {4, …, 12} the zero locus meets the squares, where (A/N) = +1, and it is not contained in a Jacobi
fibre. CONJECTURE: the same holds for all r ≥ 4 (EVIDENCE: r ≤ 12).

**Theorem 4.1 (degeneration; PROVED).** In the pentagon every 4w-diagonal cut leaves a divisor event.
* If the cut-off triangle contains the N-side, the other piece is a length-2 word at 4w, which needs 4w + 1 = xy
  with y ≡ −N (mod 4w) (Type I a = 1). For w = 1 the only option is the formal (1, 5)/(5, 1), which gives N ≡ 3 (4).
* Otherwise the quadrilateral containing N has hs = N + 4w.
The hexagon escapes because K(2, 2, 2) = 4 is an interior length-3 word at 4. Interior words at 4 are exactly (4) and
(2, 2, 2), and there is no length-2 interior word at 4 because 5 is prime.

**Reading.** Two independent facts single out the pentagon:
1. mod-2 rigidity (one quiddity pattern, so the sign is one bit);
2. the absence of an N-free sub-word at 4 of length 2.
This parallels (J)32 (m = 4 is the unique numerator whose slices form a character fibre). Here r = 3 is the unique
polygon size whose zero locus is a character fibre (for r ≤ 12 and r ≡ 0 (4); CONJECTURE beyond).
