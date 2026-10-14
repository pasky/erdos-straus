# y2 — The even edge: a three-case frieze proof of "zero quiddity mod 4 ⟺ Jacobi −1" (O210)

Labels as in DISCOVERIES.md. **ES is not solved; no infinite case of ES is claimed.**
Notation (LENGTH_THREE Prop 1.1): a positive (formal) word (c, m, s), letters ≥ 1, N = mcs − c − s > 0,
h = cm − 1, h′ = ms − 1. Quiddity cycle at V₁…V₅: (q₁, …, q₅) = (h′, c, m, s, h). Ptolemy relations
`q₁q₂ = N + q₄, q₂q₃ = 1 + q₅, q₃q₄ = 1 + q₁, q₄q₅ = N + q₂, q₅q₁ = 1 + N q₃`  (P)
(the frozen side N sits between V₅ and V₁).

## Idea
Replace DK's 512-cell check of (J)9 / LENGTH_THREE Cor 1.2 by a structural frieze argument: (i) mod 2 the
pentagon frieze is *rigid* (Lyness/Zamolodchikov parity); (ii) the sign is then a 2-adic property of one edge.

**Lemma 1 (parity rigidity; PROVED).** If N is odd, exactly two of q₁, …, q₅ are even, and they are cyclically
adjacent ("the even edge"). The vertex opposite the even edge is odd. (No positivity needed.)
*Proof.* Mod 2, (P) reads q_iq_{i+1} ≡ 1 + q_{i+3}. Not all q_i are odd: otherwise q_{i+3} would be even. If q_i is
even, the relations at i−1 and i make q_{i+2}, q_{i+3} odd, and the relation at i+3 gives q_{i+4} ≡ 1 + q_{i+1}.
So exactly one of q_{i±1} is even. ∎
(Mod 2 the pentagon frieze is a rotation of (1, 0, 0, 1, 1): the closed 5-walk on the Farey graph of X(2) = K₃
must wind ±3, so it has exactly two backtracks, and they are consecutive.)

**Theorem 2 (even-edge sign law; PROVED for all positive formal words, all odd N).** Let e, e′ be the even edge. Then
`  (h′/N) = (−1/N) · (−1)^{[8 | ee′]}.`
For N ≡ 1 (4): (h′/N) = −1 ⟺ 8 | ee′ ⟺ one of the five cluster variables is ≡ 0 (mod 4). This recovers DK Thm 4.5 /
LENGTH_THREE Cor 1.2 and extends it to formal words. (R208 repair: the extension to formal words and N ≡ 3 (4) is
MODEL_SPECIFIC Thm 3.1(a); new here are Lemma 1 and the computation-free proof.)
*Proof.* Only three cases up to the reversal (c ↔ s, h ↔ h′). Write v₂ for 2-adic valuations.
* **A: even edge {c, m}** (mirror {m, s}). Here h ≡ −1 (mod 2^{v₂(c)+v₂(m)}) and h ≡ 3 (4). So (h′/N) = (h/N), because
  hh′ ≡ 1 (N). Reciprocity gives (h/N) = (−1/N)(N/h). From hs = N + c we get (N/h) = (−c/h) = −(c/h). Write c = 2^a c′.
  Since h ≡ −1 (c′) and h ≡ 3 (4), (c′/h) = 1, so (c/h) = (2/h)^a. That is −1 exactly when a = 1 and h ≡ 3 (8), i.e.
  when cm ≡ 4 (8).
* **B: even edge {h′, c}** (mirror {s, h}). Write h′ = 2^b h″. The relation h′c = N + s gives N ≡ −s (h″) and
  s ≡ −N (4). The relation ms = h′ + 1 gives h′ ≡ −1 (s), so (h″/s) = (2/s)^b(−1/s). Collecting the reciprocity signs
  (they cancel because (N + s − 2)/2 is odd) gives (h′/N) = (2/(Ns))^b · (−1/s), with (−1/s) = −(−1/N). Finally
  Ns ≡ −1 + h′c (mod 8).
* **C: even edge {h, h′}** (the N-side). Here hh′ = 1 + Nm, so m ≡ −N (4). Using N ≡ −s (h″), ms ≡ 1 (h″),
  hh′ ≡ 1 (m) and h ≡ −1 (m), one gets (h′/N) = (2/(Nm))^b · (−1/m), with (−1/m) = −(−1/N). Finally
  Nm = hh′ − 1 (mod 8).
In each case the factor is +1 if 8 | ee′. If ee′ ≡ 4 (8), then v₂(e) = v₂(e′) = 1 and the factor is −1 (the odd
quantity is ≡ 3 (mod 8)). ∎ (Full case computations: FRIEZE_ES.md §1.)

**Corollary 3 (T1 in frieze form; PROVED).** If N = M² is odd, then every positive pentagon frieze at N has
ee′ ≡ 4 (mod 8): both even cluster variables are ≡ 2 (mod 4). The reason is (h′/M²) = 1 = (−1/M²).

## Literature
* Lyness 5-cycle / Zamolodchikov periodicity for A₂: classical; Conway–Coxeter (1973).
* Friezes with coefficients: Cuntz–Holm–Jørgensen, *Frieze patterns with coefficients*, Forum Math. Sigma 8 (2020)
  e17, arXiv:1909.02332 (abstract verified). Our object is their pentagon with boundary (1, 1, 1, 1, N).
* Jacobi-symbol algorithms via continued fractions: classical (Eisenstein, Zolotarev). Theorem 2 is the length-3
  specialisation in frieze clothing. I found no statement of the even-edge form (search not exhaustive).

## Barrier screen
It proves a known equivalence. It is not an existence mechanism.
* B5/T1: Corollary 3 locates T1 exactly: at squares the even edge is always (2, 2) mod 4.
* B2: the even edge is a moving object (where it sits depends on the word).
* B1, B3, B4, B6: not engaged.

## Cheap numerics
`scripts/y2_even_edge.py 100000` (≈ 2 min) checked all 5 115 860 positive formal words with odd N ≤ 10⁵ against Lemma 1
and Theorem 2, including the N ≡ 3 (4) law; 0 failures (`logs/y2_even_edge_1e5.txt`). Even-edge positions:
{h′,c} 1 060 359, {s,h} 1 060 359, {h,h′} 1 234 202, {c,m} 880 470, {m,s} 880 470. Odd-square control: 8 068 words, all with
ee′ ≡ 4 (8).

## Assessment
PROVED and CERTIFIED. It is a cleaner proof of a known equivalence (R208: incl. the formal-word / N ≡ 3 (4) form, MODEL_SPECIFIC Thm 3.1(a)), and it covers formal words
and to N ≡ 3 (4). The structure is new as a statement: the sign is a single 2-adic bit carried by the unique even
edge. It also points to a natural object, the 2-adic tropical frieze (memo y2_twoadic_tree_transport; R208 repair of a dangling memo name). Promise as a route:
1/5. As a tool it is useful, since it reduces "find a −1 word" to "find a word whose even edge has 2-adic weight ≥ 3".
