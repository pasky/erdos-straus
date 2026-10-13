# bsA_fricke_vieta — Markoff/Vieta dynamics for HJ words: the word is a point of a Fricke cubic, ES lives on the base (O174)

## Idea (brief item: "is the ES surface a Markov-type surface whose Vieta moves could reach a certificate?")
Let M(a) = [[a,−1],[1,0]] = T^aS. For a word, γ = M(v)M(t)M(u) = [[n, −A*],[A, −t]], with n = tuv − u − v and A = tu − 1
(`scripts/bsA_fricke.py`, asserted). Two exact structures:

**F1 (Fricke cubic, PROVED by the classical trace identity; checked for v,t,u ≤ 8).** Put a = M(v), b = M(t), c = M(u),
d = (abc)⁻¹, and let the boundary traces be (v, t, u, T) with **T = tr γ = tuv − t − u − v** (cyclically symmetric). Then
x = tr ab = vt − 2 = A* − 1, y = tr bc = tu − 2 = A − 1, z = tr ac = uv − 2 lie on the Fricke–Goldman cubic of the
four-holed sphere
x² + y² + z² + xyz = (vt + uT)x + (tu + vT)y + (vu + tT)z + 4 − v² − t² − u² − T² − vtuT.
This is a genuine Markoff-type surface, with Vieta involutions x ↦ (vt+uT) − yz − x, etc. (mapping class group of
the four-holed sphere; Painlevé VI family).
**F2 (no move reaches ES; PROVED, immediate).** The Vieta group acts on the *fibre* over fixed boundary traces
(v,t,u,T). But the ES unknowns are the boundary traces themselves: n = T + t, the sign (A/n) is a function of (t,u,v) mod 4
(DK 8.1). So every Vieta orbit consists of points with the *same* ES status. Orbits move between representations of
F₃ that are not of the form (M(v),M(t),M(u)), and they never change (v,t,u). The ES "surface" tuv − u − v = n, being the
base, is linear in each variable. It has no involutions (cayley_markoff_cm P3), and the only symmetries preserving n are
the Klein group and the rotations with u = t. **BGS-type transitivity mod n therefore acts on the wrong space.**
**F3 (cyclic words = Zagier cycles; PROVED, classical reduction theory).** The cyclic word (v,t,u) is the minus-CF (Zagier)
reduced cycle of the hyperbolic class [γ] of trace T, and its rotations have numerators T + t, T + u, T + v. So
five-slice ES(n) ⟺ **some hyperbolic conjugacy class of SL₂(ℤ) with trace T = n − t has Zagier cycle of length exactly 3,
containing t, with (tu−1 / n) = −1.** Length 3 is extreme for trace T. The closed geodesic of [γ] has length
2 log ε ≈ 2 log T, and a Zagier cycle of length 3 means it makes only three cusp excursions, so it spends almost all
of that length high in the cusp. (I make no claim about the typical cycle length in the discriminant T² − 4.)

## Literature
Goldman, *Trace coordinates on Fricke spaces* (Handbook of Teichmüller theory I, 2009; from memory). Bourgain–Gamburd–Sarnak,
Markoff triples and strong approximation (C. R. 2016; from memory). Cantat–Loray, *Dynamics on character varieties*
(Ann. Inst. Fourier 2009; from memory, Painlevé VI). Zagier, *Zetafunktionen und quadratische Körper* (1981; reduction
theory of minus CFs).

## Barrier screen
* F2 kills the brief's Markoff/BGS route exactly: the hypothesis that fails is "the group acts on ES data".
* A modification that violates it would need a correspondence that changes the boundary traces while fixing n. Among
  boundary-changing moves, scaling (DK 8.3) changes n by a factor and rotation changes n by u − t. Nothing else is
  algebraic and degree-preserving (the base is linear in each variable).
* F3 is the H-A / B3 picture in geodesic language: a closed geodesic of length ≍ 2 log T with only three excursions is a
  polylog-probability event (see bsA_hecke_cusp_excursions).

## Cheap numerics
`scripts/bsA_fricke.py`: the cubic F1 holds for all 343 words with v,t,u ∈ [2,8], and γ has entries (n, A) as stated.

## Assessment
Precise negative answer to the Markoff/Vieta/BGS question, PROVED as stated. Promise 0/5. By-product: the cyclically
symmetric "trace cubic" T = tuv − t − u − v organises the three rotations of a word, with numerators T + t, T + u, T + v
(F3).
