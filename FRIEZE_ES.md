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
