# FRIEZE_ES — the A₂ frieze dictionary of the five ES slices, deepened (task O210, spark relay Y2)

Status: in progress (O210); hostile-reviewed by R208 (reviews/frieze-es-review.md; R208 repairs marked). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
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
obstruction cannot be topological mod 4; it must be 2-adic of depth 3. (R208 repair: more precisely, the sign is the
mod-4 *spur* property of the walk — a mod-4 function of the frieze that is not a homotopy invariant; "depth 3" is the
cherry-depth *sum* of §2.) This led to (I2).
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
   * Otherwise v₂(h′) = v₂(c) = 1, so b = 1 (R208 repair of "b = v₂(c) = 1"): Ns ≡ 3 (8) and the factor is −1.

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
CERTIFIED: `scripts/y2_even_edge.py 100000`, 0 failures, 8 068 square-control words (`logs/y2_even_edge_1e5.txt`; N = 1 excluded — with its 5 words, 8 073; R208).

*Remark (what this replaces).* DK proved Thm 4.5 by a 512-cell check mod 8. CHI_FLIP gave a 2-adic Hasse-invariant
proof. Here the proof is three Jacobi computations, one per position of the even edge, each using two Ptolemy relations:
the one through the even edge and one through the odd opposite vertex.
(R208 repair, novelty: the statement of Thm 1.2 for all formal words and all odd N is MODEL_SPECIFIC Thm 3.1(a) ((J)32),
which already covers boundary words and N ≡ 3 (4); CHI_FLIP ((J)33) proves it via Hilbert reciprocity plus a 320-cell
enumeration. New here are Lemma 1.1 (the even edge) and the short computation-free proof.)
(R208 addition: since 8 | ee′ ⟺ some q_i ≡ 0 (4), Thm 1.2 shows that χ = (−h′/N) is a function of (c, m, s) **mod 4**:
40 odd-N cells, 30 with χ = −1 (checked, letters < 80). So 8 is a period of the DK/CHI_FLIP cell law, but 4 is the
minimal one.)

## 2. The 2-adic transport and the tree picture (PROVED; memo y2_twoadic_tree_transport)

From the case proofs: if o is the odd cluster variable opposite the even edge, then
`(h′/N) = −(−1/N)(2/o)` (even edge {c,m} or {m,s}), and `(h′/N) = −(−2/N)(2/o)` (the relation through o contains N).
**For N ≡ 1 (8): (h′/N) = −(2/o).** CERTIFIED: `scripts/y2_transport.py 2000`, all cells.
*Proof (R208 repair: written out).* o = h, h′, s, c, m for the even edge {c,m}, {m,s}, {h′,c}, {s,h}, {h,h′}. Case A:
(h′/N) = −(−1/N)(c/h) and (c/h) = (2/h)^a = (2/h), since a ≥ 2 forces h ≡ 7 (8). Cases B, C: (h′/N) =
(2/(No))^b(−1/o) = −(−2/N)(2/o)·(2/(No))^{b−1}, and b ≥ 2 forces 8 | ee′, hence No ≡ 7 (8). ∎ (o need not be small: o = h
or h′ can be ≍ N.)
In the Bruhat–Tits tree T₂ the five ends form two cherries plus a lone end o. The sign is "the cherry depths sum to
≥ 3", and T1 is "both cherries have depth exactly 1".

## 3. Where T1 lives: positivity (memo y2_positivity_is_T1; R208 repair of labels)

PROVED: positivity is necessary for Thm 1.2 / Cor 1.4. For every odd M ≥ 3 the signed word (4, −(M² + 3)/4, −1) has
N = M² and quiddity c = 4 (R208; the box search `scripts/y2_signed.py 40` is now only a check).
By inspection: the proof of Thm 1.2 uses positivity only in the reciprocity steps. The reading "T1 is the archimedean
factor of Hilbert reciprocity, entering through positivity" is CHI_FLIP Thm 1.1 (ε_∞ = −1 because the path form is
positive definite; (J)13, (J)33) in frieze language. Consequences (Assessment):
* SVZ's lifting theory (tame, signed, unit boundary) is T1-blind. Every closed 5-walk on F₄ is strongly contractible (§0, I1).
* A criterion that depends on N only through N mod n cannot separate odd squares M² from primes ≡ M² (mod n), so it
  cannot force a −1 word (Cor 1.4). (R208 repair of "finite-ring frieze theory is N-blind beyond N mod 8".)
* **Any frieze-theoretic ES proof must use the positivity of the frieze archimedeanly** (Assessment, steering rule).

## 4. Polygon size: the pentagon is the unique size where the zero locus is a Jacobi fibre (memo y2_hexagon_degeneration)

Let Z_r(N) be "some interior word of HJ length r at N has a short diagonal (quiddity) ≡ 0 (mod 4)". Each such vertex
gives 4/N as r unit fractions (vertex fan).
* r = 2: for N ≡ 1 (4), Z₂ is empty, because xy = N + 1 ≡ 2 (4) (PROVED).
* r = 3: Z₃ ⟺ some word has (h′/N) = −1 (Thm 1.2). This is a Jacobi fibre, empty at squares (T1).
* r = 4: **Z₄(N) holds for every N ≡ 1 (4), N ≥ 5**, via the word (2, 2, 2, (N+3)/4). Its 4-diagonal K(2,2,2) = 4 cuts
  off a free triangle that contains the N-side (PROVED, explicit identity). In particular Z₄ holds at all odd squares.
* r ≡ 0 (4): (2^{r−1}, k) has K = rk − r + 1 and end quiddity K(2^{r−1}) = r ≡ 0 (4). Its N-class is 1 (mod r), which
  contains odd squares (PROVED).
* 5 ≤ r ≤ 12: explicit odd-square witnesses (`scripts/y2_witness.py 12 40`): r = 5: 25 = K(2,3,2,2,3); r = 6:
  49 = K(2,2,3,2,2,4); r = 7: 81; r = 9: 49; r = 10: 81; r = 11: 225 (CERTIFIED).
* **All r ≥ 5 (PROVED, R208 repair of the former CONJECTURE).** w = (2, 2, 2, 4, 2^{r−5}, k). With p = (2,2,2,4,2^{r−5}),
  K(2^j, 4, 2^l) = 2jl + 3j + 3l + 4 gives Q := K(p) = 9(r − 5) + 13 and K(p⁻) = Q − 9, so K(w) = kQ − Q + 9 ≡ 9 (mod Q).
  Take N = (2Q + 3)² and k = (N + Q − 9)/Q ≥ 2. The letter 4 is a quiddity. (Checked r ≤ 60, `scripts/review_r208_polygon.py`.)
So for every r ≥ 4 the zero locus meets the squares, where (A/N) = +1, so it is not contained in the fibre
{(A/N) = −1}. (Definition, R208: "the zero locus of length r is a Jacobi fibre" means: among interior length-r words at
N ≡ 1 (4), {some q_i ≡ 0 (4)} = {(A/N) = −1}. For r = 2 the zero locus is empty while the −1 fibre is not, e.g. N = 5,
(2, 3).)

**Theorem 4.1 (degeneration; PROVED).** In the pentagon every 4w-diagonal cut leaves a divisor event.
* If the cut-off triangle contains the N-side, the other piece is a length-2 word at 4w, which needs 4w + 1 = xy
  with y ≡ −N (mod 4w) (Type I a = 1). For w = 1 the only option is the formal (1, 5)/(5, 1), which gives N ≡ 3 (4).
* Otherwise the quadrilateral containing N gives hs = N + 4w (c = 4w), hh′ = 1 + 4wN (m = 4w) or ch′ = N + 4w (s = 4w)
  (R208 repair). PROVED content: the piece identification; "divisor event" (B2) is the Assessment reading.
The hexagon escapes because K(2, 2, 2) = 4 is an interior length-3 word at 4. Interior words at 4 are exactly (4) and
(2, 2, 2), and there is no length-2 interior word at 4 because 5 is prime.

**Reading.** Two independent facts single out the pentagon:
1. mod-2 rigidity (one quiddity pattern, so the sign is one bit);
2. the absence of an N-free sub-word at 4 of length 2.
This parallels (J)32 (m = 4 is the unique numerator whose slices form a character fibre). Here r = 3 is the unique
polygon size whose zero locus is a character fibre (PROVED for all r ≥ 2; R208 repair).

## 5. Constructive attempts (barrier as steering wheel)

| attempt | hypothesis of the barrier it tries to violate | outcome |
|---|---|---|
| SVZ lifting ⟹ sign is topological (I1) | "congruence-only data" (B1): uses homotopy instead | killed: all odd closed walks on F₄ are strongly contractible; signed theory is T1-blind (§3) |
| Lift spur-walks mod 8 to positive friezes at N | "fixed finite slice set" (B2): all 80 classes at once | no hidden local obstruction (EVIDENCE N ≤ 2·10⁴); lifting = SQ₅ lottery (~100 words, 80 classes) |
| Transport (h′/N) = −(2/o), choose o small | "moving modulus" (B2): modulus becomes the small o | the sign moves to o, but a word with prescribed o is a divisor event (fixed o: B2; growing o: H-A) |
| Hexagon + ear (ES = hexagon with a mergeable pair) | "bounded multiplicity" (B3): hexagons are plentiful and N-free | merging two arcs = an ear = a divisor condition, so it returns to the pentagon |
| Windmill on F(N) | H-B parity | multilinear surface, only the reflection; #F₋(p) even (y2_parity_involution) |
| Zamolodchikov forcing | "no deterministic input" | forces an even edge (mod 2) only; mod 4 is impossible by T1 |
| Positivity (CC ear-lemma analogue) | §3 says a proof must use positivity | positivity forces *sizes* (for interior words some letter is ≲ (2N)^{1/3}), not residues. A size-forced word has its sign fixed by congruences of N (B1), which T1 kills |

## 6. Verdict (O210 checkpoint 1)
* **PROVED (new as statements; elementary):**
  * Even-edge theorem (Thm 1.2): for every positive formal pentagon frieze at odd N,
    (h′/N) = (−1/N)(−1)^{[8 | ee′]}. This gives a 3-case, computation-free proof of DK Thm 4.5 and of its extension to
    formal words and N ≡ 3 (4), which is MODEL_SPECIFIC Thm 3.1(a) (R208 repair: the extension is not new).
  * The transport law (h′/N) = −(2/o) for N ≡ 1 (8) (§2).
  * Positivity is necessary for the sign law (§3, explicit signed family); "SVZ/finite-ring frieze theory is T1-blind"
    is Assessment (R208 repair).
  * Pentagon degeneration of the hexagon proof (Thm 4.1). r = 3 is the unique polygon size with a Jacobi-fibre zero
    locus (all r; R208 repair of the former CONJECTURE).
* **CERTIFIED:**
  * 5 115 860 words (all odd N ≤ 10⁵);
  * 2·10⁶ random words with N up to ~10¹²;
  * square controls: 8 068 + 20 406 words, 0 zero-mod-4.
* **Assessment:** no deterministic existence mechanism. The frieze language makes the barrier map sharper. The sign is
  one 2-adic bit at a unique even edge, transportable to a small modulus o, and enforced at squares only through
  positivity. Every existence attempt still needs a word with a prescribed small datum, which is B2/H-A.
* **ES is not solved; no infinite case of ES is claimed.**

## 7. Literature used
* SVZ: Short–Van Son–Zabolotskii, arXiv:2312.12953 (Thm 1.6 and the definitions read in the PDF).
* Böhmler–Cuntz, arXiv:2407.12596.
* Cuntz–Holm–Jørgensen, arXiv:1909.02332 (authors verified via the arXiv API).
* Morier-Genoud–Ovsienko, arXiv:1811.01229 (continuants = frieze entries; per R205).
* Ventas, arXiv:2605.04551 (sources/lit2026). Per R205 it has the V₁ row and the boundary-word shots of LENGTH_THREE;
  nothing in §§1–4 depends on it.
* In-campaign precursor: BRAINSTORM/farey_chain_frieze.md (O144).
