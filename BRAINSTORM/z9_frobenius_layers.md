# z9_frobenius_layers — loops of G_p/Frob are exactly the edges whose lattice represents 2; path edges sit in low Frobenius layers (O233)

## Idea
Look for global structure of the certificate (path-shaped) edges inside the supersingular 2-isogeny graph G_p. First thing
the data shows (`scripts/z9_stats.py`, all 609 primes p ≡ 1 (mod 4), p ≤ 10⁴): path edges are strongly enriched in loops of
the type graph G_p/Frob (22.6 % of path classes are loops against 5.8 % of all edges; up to 3000: 26.7 % vs 10.2 %).
Explain it exactly.

**Lemma 1 (PROVED, short; Deuring + CONSTRUCTIVE_ES Prop 3.1).** Let p ≥ 11, (E, C) a supersingular 2-isogeny, L = L(E, C) ∈ 𝔊⁻_p
its edge lattice. For 1 ≤ m < p/4 one has r_L(m) = #{x ∈ End(E, C) : deg x = mp}. In particular
**(E, C) is a loop of G_p/Frob (E/C ≅ E or E^{(p)}) ⟺ L represents 2**, and (E, C) lies on the 𝔽_p-spine ⟺ L represents 1.
*Proof.* Let O = End E and P = {x ∈ O : p | nrd x}. P is the two-sided prime over p, stable under conjugation, so for x ∈ P
we get trd x = x + x̄ ∈ P ∩ ℤ = pℤ. If deg x = mp with m < p/4, then |trd x| ≤ 2√(mp) < p, so trd x = 0. Hence every
x ∈ End(E, C) of degree mp lies in E⁰, and CONSTRUCTIVE_ES Prop 3.1 gives r_L(m) = #{ε ∈ E⁰ : nrd ε = mp}.
(⇐, m = 2.) Take ε ∈ End(E, C) with ε² = −2p. If ε(C) = C, then ε² = −2p would act on C as a bijection, but −2p kills E[2].
So ε(C) = 0. Since deg ε = 2p with p ∥ 2p, ε = σ∘Fr with σ separable of degree 2, and ker ε(𝔽̄_p) = C. Then ε = θ∘φ_C with
θ: E/C → E of degree p and trivial kernel on points, i.e. θ is Frobenius up to isomorphism, so E ≅ (E/C)^{(p)}. As j ∈ 𝔽_{p²},
E/C ≅ E^{(p)}.
(⇒.) Suppose E/C ≅ E^{(p)}. Then ε := ι∘Fr∘φ_C : E → E/C ≅ E^{(p)} → E^{(p²)} ≅ E has degree 2p and kills C, so ε ∈ End(E, C).
By the trace argument, r_L(2) > 0. Now suppose E/C ≅ E with j(E) ∉ 𝔽_p. Then O contains an element of degree 2, so E has CM by
an order of discriminant −4, −7 or −8. Those j-invariants (1728, −3375, 8000) lie in 𝔽_p, a contradiction. So that case
reduces to the previous one. The spine statement (m = 1) is CONSTRUCTIVE_ES Cor 3.2. ∎
CERTIFIED (`scripts/z9_loops.py 5 2000`, every edge of G_p/Frob for all p ≡ 1 (4) with 5 ≤ p ≤ 2000, 9489 edges; for 5 ≤ p < 11
the identity also held): loop ⟺ r_L(2) > 0 with 0 exceptions. Joint table: 1191 loops, all representing 2; 8298 non-loops,
none representing 2. Edges representing both 1 and 2 (79) are all path-shaped. They are ⟨1⟩ ⊥ [[2, 1], [1, (p+1)/2]],
the word (1, (p+3)/2, 3), χ = (−2/p), i.e. Mordell's q = 2.

**Reading.** For a path word w = (t, u, v), L_w represents its three letters, so the certificate edge lies in Frobenius
layers t, u and v at once. "Layer m" (for m < p/4) means that some degree-m isogeny E^{(p)} → E is compatible with C; for larger m the trace-zero qualification is needed (e.g. m = p: Verschiebung is always compatible, yet r_L(p) = 0 for p ≡ 1 (4)). Letters are small
(t·u·v ≈ p), so path edges live in low layers. Layers 1 and 2 are the spine and the loops. Each layer is a deterministic,
class-number-sized edge set: Σ_L r_L(m)/|Aut L| is an Eichler class-number expression of size ≍ √(mp) up to logs. Inside layer m, a path edge with
letter m is a divisor event:
* m = t (middle letter): (mu − 1)(mv − 1) = mp + 1;
* m = u (end letter): (tm − 1)(tv − 1) = tp + 1, i.e. p + m ≡ 0 (mod tm − 1).

So layer m replays a Mordell-type slice. ES-five(p) ⟺ some low layer contains a path edge. The layers are the "near-spine"
structure of G_p behind CONSTRUCTIVE_ES Cor 3.2.

## Literature
Deuring correspondence; Kohel's thesis (1996) for the structure of the ℓ-isogeny graph near 𝔽_p; Delfs–Galbraith (2016),
the 𝔽_p-subgraph (spine); Arpin et al., "Adventures in supersingularland" (2022), loops and the Frobenius involution on G_p;
Gross (1987), Prop 3.1-type theta series of the Gross lattice. The loop ⟺ "represents 2" equivalence is a standard type of
statement (loops of G_p/Frob correspond to 2-isogenies to the conjugate). This edge-lattice formulation was not found in the campaign.

## Barrier screen
B2: inside each layer, path-ness is "mp + 1 (resp. tp + 1) has a divisor ≡ −1 mod the letter". The layer is form-class data
(Prop 10.3: Σ r_L(m)/|Aut| is a genus/Eichler mass), and the path condition is its residue refinement. B3: layer sizes ≍ h(−4mp)
are far above the polylog path count, so no main term forces a hit. T1: at n = m² there is no B_{n,∞}, so there are no layers (CONSTRUCTIVE_ES 5.4).
B6/Prop 10.3: the layer populations are exactly computable (traces of Brandt matrices B(m) restricted to the
Frobenius-twisted part). Which of their edges are path edges is not.

## Cheap numerics
`scripts/z9_loops.py 5 2000` (joint table above). `scripts/z9_stats.py lo hi` gives the per-prime V, E, loops, P, path-loops, …;
`data/z9/stats_p1mod4_1e4.txt` (609 primes).

## Assessment
PROVED (Lemma 1), clean and small. It explains a visible numerical pattern (loops are rich in certificates) and gives
CONSTRUCTIVE_ES's "Frobenius distance" a graph meaning in layers 1, 2. No forcing: inside each layer the path condition is
a Mordell-type divisor slice. Promise 1/5 as an existence route; useful as a dictionary entry.
