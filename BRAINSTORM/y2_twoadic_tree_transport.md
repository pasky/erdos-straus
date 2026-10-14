# y2 — The ES sign as a cherry depth in the 2-adic tree, and the transport law (h′/N) = −(2/o) (O210)

Labels as in DISCOVERIES.md. **ES is not solved.** Notation: FRIEZE_ES.md. Item (e) of the brief: tropical friezes.

## Idea
Tropicalise the pentagon frieze at the prime 2. For primitive integral vectors u, v, the 2-adic valuation v₂(det(u, v))
is the Gromov product of the two ends [u], [v] ∈ P¹(ℚ₂) seen from the standard vertex v₀ = [ℤ₂²] of the Bruhat–Tits
tree T₂ (classical: it is the depth to which the rays from v₀ coincide). So the 2-adic valuation pattern of the
frieze is a **tree metric** on five ends, and Ptolemy tropicalises to the four-point condition.

**Dictionary (PROVED, elementary).** v₀ has three neighbours, labelled by P¹(F₂) = {0, 1, ∞}. For odd N, consecutive
pentagon vertices leave v₀ along different edges (all five sides are odd). By FRIEZE_ES Lemma 1.1 the colour pattern
around the pentagon is (a, b, a, b, c). So the five ends form two **cherries**, {V_{i−1}, V_{i+1}} and
{V_i, V_{i+2}}, and one lone end V_{i+3} (the odd vertex o opposite the even edge). The even-edge quiddities are the
cherry depths: v₂(e) = depth of {V_{i−1}, V_{i+1}} and v₂(e′) = depth of {V_i, V_{i+2}}.

**Theorem 1 (restating FRIEZE_ES Thm 1.2; PROVED).** (h′/N) = (−1/N)·(−1)^{[depth₁ + depth₂ ≥ 3]}. At odd squares both
cherries split at depth exactly 1 (T1). ES five-slice certificate (N ≡ 1 (4)) ⟺ some positive pentagon at N has a
cherry of depth ≥ 2 ⟺ two ends at distance 2 in the pentagon agree mod 4 up to sign (the spur of
y2_farey_complex_lifting).

**Theorem 2 (transport law; PROVED from the case proofs of FRIEZE_ES Thm 1.2; CERTIFIED).** Let o be the odd cluster
variable opposite the even edge.
* If the edge is {c, m} or {m, s} (the relation through o has no N), then (h′/N) = −(−1/N)(2/o).
* If the edge is {h′, c}, {s, h} or {h, h′} (the relation through o contains N), then (h′/N) = −(−2/N)(2/o).
In particular, **for N ≡ 1 (mod 8): (h′/N) = −(2/o).** The quadratic character of the big modulus N is carried by the
character of 2 at the *small* modulus o. Here o is h, s, c or m, i.e. a letter in four of the five positions.
*Proof.* In the proof of Thm 1.2, ee′ ≡ 0 (8) ⟺ the odd quantity σ + τo ≡ 0 (8). Since o ≡ −στ⁻¹ (4) is ≡ 3 (4),
this is the statement o ≡ −στ⁻¹ (8). Then compare (2/o) with (2/−στ⁻¹) for σ, τ ∈ {1, N}. ∎
(R208 repair, explicit: Case A (c/h) = (2/h)^a = (2/h) since a ≥ 2 forces h ≡ 7 (8); Cases B, C (h′/N) =
(2/(No))^b(−1/o) = −(−2/N)(2/o)(2/(No))^{b−1}, and b ≥ 2 forces No ≡ 7 (8). o need not be small: o = h, h′ can be ≍ N.)
CERTIFIED: `scripts/y2_transport.py 2000`, all formal words with odd N ≤ 2000, every (N mod 8, edge) cell consistent.

## Constructive iteration
* *Try:* use the transport. Pick a small prime o ≡ 7 (8) (2 is a QR) and look for a word at a prime p ≡ 1 (8) with o
  opposite the even edge. In case C (o = m, all letters odd) this means a divisor h ≡ m − 1 (mod 2m) of mp + 1.
  *Screen:* for fixed o this is a fixed-modulus shot (B2: fails i.o. under H). With o growing it is H-A. The transport
  moves the *character* to a small modulus, but the *existence* of a word with a given o is still a divisor event.
* *Try:* the tree has an obvious move, rotating the 5 ends by an element of SL₂(ℤ₂) fixing v₀. It does not preserve
  the archimedean constraint (four unit sides and det N), so it is not a move on words. Dead.

## Literature
Bruhat–Tits tree, Gromov products of ends and valuations of determinants: Serre, *Trees*, Ch. II.1 (from memory).
Tropical friezes: L. Guo, *On tropical friezes associated with Dynkin diagrams*, IMRN 2013 (from memory, not
verified). CHI_FLIP's χ = −ε₂(Q_w) is the same 2-adic fact in quadratic-form language. The transport law is an
instance of Hilbert reciprocity (Π_v (h′, N)_v = 1) localised at the even edge.

## Barrier screen
* B2: Theorem 2 transports the sign, not the existence.
* T1: depth (1, 1) at squares. The theorem shows *where* T1 lives in the tree but does not escape it.
* B5: any statement about tree configurations alone is N-blind beyond N mod 8 (as for F₄).

## Cheap numerics
`scripts/y2_transport.py 2000` prints the (N mod 8, edge position, (h′/N), (2/o)) table: two cells per row type, as
predicted, 0 exceptions.

## Assessment
PROVED dictionary. SHARP-ish: "(h′/N) = −(2/o) for N ≡ 1 (8)" is a crisp reciprocity transport inside the frieze.
Promise as a route: 1/5. The transport is exact, but the existence of a word with a prescribed o is B2/H-A.
