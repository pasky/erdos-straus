# y2 — Combinatorial models for positive friezes with boundary (1,1,1,1,N) and (Q²,1,1,1,n) (O210)

Labels as in DISCOVERIES.md. **ES is not solved.** Item (c) of the brief.

## Idea
Conway–Coxeter: positive integral friezes with unit boundary ↔ triangulations. Find the analogue for one frozen
value N, and look for enumerative (H-E) identities there.

## Results
**Proposition 1 (sub-polygon model; PROVED, elementary; the general principle is Cuntz–Holm–Jørgensen's "cutting out
subpolygons").** Positive formal pentagon friezes at N ↔ 5-tuples of Farey vertices
(0, ∞, c, c − 1/m, N/h′), consecutive ones Farey-adjacent, with the turning letters ≥ 1. Equivalently: a triangulated
polygon P (the Farey triangles under the path, plus the CF fan from 0 to N/h′) and five marked vertices, four of
whose consecutive pairs are arcs of the triangulation. Then N is the Conway–Coxeter entry λ(V₅, V₁) of P. So
each such frieze IS a sub-pentagon of a classical frieze. The model exists, but P is determined by the word (by the
regular CF of N/h′), so it is a relabelling.

**Proposition 2 (snake graphs; classical in substance).** λ(V₅, V₁) = N is the number of perfect matchings of the
snake graph of the arc V₅V₁ in P (Musiker–Schiffler–Williams expansion; continuants = perfect matchings, cf.
Morier-Genoud–Ovsienko, *Farey boat* arXiv:1811.01229, per R205). The vertex-fan identities of LENGTH_THREE §2 are
the "first-tile" splittings of these matchings. An ES slice (some quiddity ≡ 0 (4)) is a congruence on the
matching count of a *different* arc. No identity relates the counts of different arcs beyond Ptolemy (= the
skein relation).

**Proposition 3 (ES^{(S)} side).** For a pentagon with frozen (Q², 1, 1, 1, n), the side of λ-length Q² is NOT an arc
of an integral Farey triangulation: integral vectors with det Q² cannot be followed by an integral unimodular
neighbour unless one rescales the decoration (LENGTH_THREE §6). Hence ES^{(S)} friezes are sub-pentagons of
*rescaled* (non-Ford) decorations. CHJ's realisability problem ("which friezes with coefficients come from
subpolygons") is the precise home of this. For Q > 1 they are generally not realisable by a unit-boundary CC
frieze with integral vectors. Assessment, not proved in general.

**Count (EVIDENCE).** #F(N) = Σ_{m ≥ 1} #{h | mN + 1 : h ≡ −1 (m), (mN+1)/h ≡ −1 (m)} (m = 1 gives τ(N + 1)). Values
at primes 5…37: 11, 13, 17, 15, 19, 21, 25, 25, 23, 19. No closed form was found, as expected: it is the (★)
divisor convolution of HJ_DEEP.

## Iteration
* Hoped for an H-E identity Σ_{friezes} (weight) = (closed form) that sees the sign. Every such sum over sub-polygons
  is a sum over words, i.e. over (m, h). The sign-weighted sum is GROWING_IDENTITIES' W(n) ((J)10), whose
  positivity is the spin event.
* Violate "unit sides": CHJ friezes with coefficients on larger polygons are cut from triangulations, and the ES
  constraint becomes "four sides are arcs". The sole freedom is again the triangulation ↔ CF of N/A.

## Literature
* M. Cuntz, T. Holm, P. Jørgensen, *Frieze patterns with coefficients*, Forum Math. Sigma 8 (2020) e17,
  arXiv:1909.02332 (authors verified via the arXiv API; the orchestrator's note "Cuntz–Holm–Pagano" appears to be a
  slip).
* Conway–Coxeter (1973). Musiker–Schiffler–Williams, *Positivity for cluster algebras from surfaces* (2011), from
  memory. Morier-Genoud–Ovsienko arXiv:1811.01229.
* In-campaign precursor: BRAINSTORM/farey_chain_frieze.md (O144).

## Barrier screen
B2: the triangulation is the CF of N/A, the unknown. H-E: no new identity. T1: the models are N-agnostic.

## Assessment
Dictionary (PROVED, relabelling). Promise 0/5. It answers (c): yes, there is a model (sub-polygons of triangulations
/ snake graphs), but it is the word itself in other clothing.
