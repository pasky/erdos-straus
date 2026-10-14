# y2 — Parity/involution forcing on the set of pentagon friezes at N (H-B screen) (O210)

Labels as in DISCOVERIES.md. **ES is not solved.**

## Idea
Zagier-windmill style: find involutions on the finite set F(N) of positive formal pentagon friezes at N (words
(c, m, s), letters ≥ 1, K = N) whose fixed points are computable. A parity mismatch between #F(N) and #F₊(N) (sign +1)
would then force F₋(N) ≠ ∅.

## Results
**Lemma 1 (PROVED).** The equation mcs − c − s = N is multilinear (degree 1 in each letter). So there are no
Vieta-jump involutions on the cubic surface. The only symmetry of the frieze fixing the frozen side N is the reflection
(c, m, s) ↦ (s, m, c). It preserves the sign, because (h/N) = (h′/N) by hh′ ≡ 1 (N).

**Lemma 2 (PROVED).** At a prime p the reflection has exactly one fixed point, (1, p + 2, 1), since c = s gives
c(mc − 2) = p. That fixed point has even edge {h, h′} = {p + 1, p + 1} with ee′ = (p + 1)² ≡ 4 (8) for p ≡ 1 (4), so it
has sign +1. **Hence #F(p) is odd, #F₊(p) is odd, and #F₋(p) is even.** No parity forcing: F₋(p) = ∅ is
parity-consistent.

EVIDENCE (`/tmp` probe recorded here, all N ≡ 1 (4), 5 ≤ N < 3000): at all 211 primes #F is odd and #F₋ ≡ 0 (2), with
#F₋ mod 4 split 101 (≡ 0) / 110 (≡ 2), so no mod-4 law either. At odd squares #F₋ = 0 (T1).

## Iteration
* Hypothesis violated by windmills: Zagier's involution lives on a *quadratic* surface (x² + 4yz = p), which has a
  Vieta structure. The ES frieze surface is multilinear, so the only involutions are the dihedral ones (Lemma 1).
* Modification: pass to the *hexagon* (y2_hexagon_degeneration), where the frieze surface at N has many more
  symmetries. But ES is the subset of hexagons with an ear, which is not involution-stable (ears break the dihedral
  action except the reflection).
* Modification: mutations of the frozen variable (exchange N with another side) leave the class of
  "(1,1,1,1,N)-friezes". Dead.

## Literature
Zagier, *A one-sentence proof…*, AMM 97 (1990). INVOLUTION_ES / WINDMILL_REDUCTION ((J)2, (J)5) for the
campaign's windmill screens.

## Barrier screen
H-B (parity at fixed p): closed for dihedral involutions by Lemma 2. B5: consistent, since the sign-preserving
reflection gives no information at squares either.

## Assessment
NEGATIVE, PROVED (Lemmas 1–2). Promise 0/5. The frieze surface is multilinear, so it has no windmill.
