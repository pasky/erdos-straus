# z36 — ES-five as a Möbius gluing of two origin intervals (O266 memo 3)

## Idea
Put ES-five in the exact shape of the Shkredov/Zhang gluing equation and see which hypothesis of Lemma 15 / Thm 3.6 fails.
Details: ZAREMBA_TRANSFER.md §3 (Lemmas C, D).

## Literature
Shk Lemma 15 (g(α + a) = β + b, (α, β) ∈ S ⊆ [N]², |S| ≥ N^{1+δ}, asymptotic |S||A||B|/q with error |A|^{1/2}|B|^{1/2}|S|^{1−κ});
Zhang (3.1)–(3.5) (g_j = [[2j, 1 − 4j²], [−1, 2j]], a one-parameter family of HJ two-letter words);
Shparlinski, Modular hyperbolas (Japan. J. Math. 2012) Thm 13 (asymptotic only for XY ≥ m^{3/2}; via sources/lit2026/O13_LITERATURE_NOTES.md);
Bourgain–Garaev arXiv:1211.4184 Thm 2 (x⁻¹ + y⁻¹ + z⁻¹ = λ in short intervals: an *upper* bound |I|^{2/3+o(1)}).

## Content
* **Lemma C (PROVED).** tuv − u − v = p ⟺ t ≡ ū + v̄ (mod p) and tuv − u − v < 2p (t, u, v ≥ 2).
* Möbius form: v = h_t(u), h_t(x) = x/(tx − 1). ES-five asks: does some h_t (t ≤ T) send the interval [U] into [V], UVT ≍ p
  (+ the Jacobi cell condition)? Same shape as Zhang's g_j a = −b, but the glued sets are **boxes at the origin**
  (A = B = {0}, S = [U] × [V]), and the expected count per dyadic box is UVT/p ≍ 1.
* **Lemma D (PROVED).** Enlarging the box (tuv − u − v < (K + 1)p) yields exactly the certificates of kp, k ≤ K; ES(kp) ⇐ ES(k),
  so the "alphabet/region knob" is vacuous. The only live knobs are the length L and the character.
* (Goal 3 of O266, the semigroup question.) A length-3 certificate is the word T^vS·T^tS·T^uS; as an alphabet walk it has
  ≍ p log² p walks of archimedean size ≤ p hitting a codimension-1 target mod p: expected log² p. No sub-structure
  (product of shorter certificates) exists at a prime: the Euclid recursion A ∈ L₃(p) ⟺ (−p mod A) ∈ L₂(A) only
  re-expresses the certificate as a divisor of A + 1 (DEDEKIND_ES 5.4), the B2 event.

## Barrier screen
B2 returns in the archimedean region (the box UVT ≍ p is the tied size of SYNTHESIS_SPARKS8 Prop 1.4, now visible as
"origin boxes"); B3: one expected solution per box; T1: the Jacobi cell condition. Lemma 15 needs dense A, B — violated.

## Cheap numerics
Lemma C is a two-line identity; DEDEKIND_ES's checks of L₃(p) cover it. No new script.

## Assessment
PROVED dictionary + Assessment. Not SHARP: it identifies the ES gluing as the *degenerate* case (point sets, origin
box) of the Zaremba gluing, where no growth input applies.
