# GLOBAL_FANO — from the in-word Fano pigeonhole to the supersingular 2-isogeny graph (task O233, spark relay Z3)

Status: checkpoint (O233). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on FOUR_ADIC_INPUT.md (O224, Fano Thm 1.3, bit law Prop 1.4), CONSTRUCTIVE_ES.md ((J)35), CHI_FLIP.md ((J)33),
TES_FINITE.md ((J)31), TWISTED_T1.md ((J)19), WINDMILL_REDUCTION Prop 10.3. Memos BRAINSTORM/z9_*.md, scripts
scripts/z9_*, data data/z9/.

Notation. p ≡ 1 (mod 4) prime; a word w = (t, u, v), tuv − u − v = p, A = tu − 1, A* = tv − 1, AA* = tp + 1; L_w the
path lattice; 𝔊⁻_p the classes of det-p lattices isotropic at 2 (= edges of the supersingular 2-isogeny graph G_p modulo
⟨Frob, w₂⟩, CONSTRUCTIVE_ES Thm 2.1); vertices = maximal orders = vertex lattices F = L + ℤx/2 (half-integral, disc p).
The tool `scripts/z9_graph.py` builds G_p/Frob on the lattice side (canonical forms, exact). Edge counts reproduce
CONSTRUCTIVE_ES's |𝔊⁻_p| (4, 7, 9, 15, 69, 166 at p = 37, 73, 97, 193, 1009, 2521).

## 0. Iteration log (construction first; each attempt with the barrier hypothesis it met)
(I1) **Parity/degree law over G_p** (brief goal 1, literal). Path classes P(p), odd-degree vertices of the path subgraph, the
pointer digraph. All 609 primes p ≡ 1 (4) ≤ 10⁴: P(p) is even 47.6 % of the time, the path subgraph has no odd vertex at 3
primes, and pointers to both ends occur except at 17 primes. No law (z9_pointer_parity). *Hypothesis met:* the only
involutions (reversal, w₂, Frob) are already quotiented out, and exactly computable counts are genus data (§3).
(I2) **Look at what is structured instead.** Path edges are 4× enriched in loops of G_p/Frob. Explained exactly: loop ⟺ the
edge lattice represents 2 (§1, PROVED). This leads to Frobenius *layers* (L represents m ⟺ a compatible degree-m isogeny
E^{(p)} → E). Path edges live in the layers of their letters, and each layer is a deterministic class-number-sized set.
*Modification tried:* force a certificate in a low layer. Inside layer m the path condition is a Mordell-type divisor slice
(B2), e.g. the spine m = 1 misses 5013 primes ≡ 1 (8) below 10⁶ (CONSTRUCTIVE_ES Cor 3.3).
(I3) **Identify the layer object** (§4): layer t = supersingular reduction of the CM points of discriminant −4tp on X₀(2).
The certificate inside it is the ray-class condition "the class contains an ideal of norm A ≡ −1 (mod t) dividing tp + 1".
That is WINDMILL Prop 10.3's residue event. *Hypothesis met:* moving modulus (the ray-class modulus t is the layer index).
*Modification tried:* make t fixed (one layer) — this is a fixed finite slice set, which fails i.o. under H (B2).
(I4) **Brandt / class-number counts** (goal 4; z9_brandt_screen). Hecke-equivariant linear data sees only the mass of the path
set, and full-rank Siegel–Weil makes that mass the word count itself (tautology, no main term). Degree-2 data sees planes
up to genus, but the glue residue ±1 is missing. Class-wise data (Schiemann) is complete but is the problem itself.
(I5) **Widen the target shape** (z9_triangle_shapes): the other near-orthogonal shape (cyclic plumbings) is decoupled. At 47 of 329
primes ≤ 5000 the χ = −1 triangle classes exist but none is a path class. A triangle word carries no Egyptian identity.
(I6) **Depth bits** (goal 2): proved that a depth-k pentagon vector is a non-backtracking walk of k − 1 half-steps in G_p
(§2), so 8/p is the X₀(4) refinement. The bits are functions of v₂(t) or of v₂(tp + 1) and its split (Prop 2.3).
(I7) **Order-3 Fano** (goal 3, the sharp test; z9_order3_fano): in TES's Type II word family the cubic symbol χ₃ does not control
λ-adic divisibility of the numerator. At all 13 failure primes with N ≤ 787 there are hundreds of target-χ₃ words, and at 7 of them even target words with
λ⁴ | T (killed by the 2-primary anchor). So TES failures are **bit failures** (8/131-type), not character failures.

## 1. Loops = representations of 2 (PROVED; z9_frobenius_layers Lemma 1)
**Theorem 1.1.** For p ≥ 11 and an edge (E, C) of G_p with lattice L: r_L(m) = #{x ∈ End(E, C) : deg x = mp} for m < p/4
(all such x have trace 0), and (E, C) is a loop of G_p/Frob ⟺ L represents 2 (⟺ E/C ≅ E^{(p)}). Proof in the memo: a
trace argument through the ramified prime P of End E, and ε² = −2p cannot fix C, so ker ε ⊇ C and ε factors through
Frobenius. CERTIFIED: all 9489 edges of all p ≡ 1 (4), 5 ≤ p ≤ 2000, 0 exceptions (`scripts/z9_loops.py`).
*Reading.* Layers: L ∈ layer m ⟺ r_L(m) > 0. Layer 1 is the 𝔽_p-spine and layer 2 the loops. A path edge lies in the layers t, u, v of its
letters, so certificates sit near Frobenius (tuv ≈ p, letters small). That is the "near-spine" geometry behind CONSTRUCTIVE_ES's
Frobenius distance.

## 2. Depth = walk length; 8/p is a level-4 problem (PROVED + CERTIFIED; z9_depth_walks)
**Theorem 2.1.** A primitive x in an edge lattice L with v₂(Q(x)) = k ≥ 2 determines the alternating chain
L₁ = L, F_j = L_j + ℤx/2^j, L_{j+1} = (the unique classical index-2 sublattice of F_j containing x/2^j). It is a non-backtracking
walk in G_p of exactly k − 1 half-steps. The vertex step uses the local Fano structure at a vertex: F/2F carries the conic
{q = 0} with three points, which are the three edges at the vertex, and the polar radical r is its nucleus; the classical index-2 sublattices are the three
hyperplanes through r. CERTIFIED in coordinates on all 1190 pentagon pointers of all χ = −1 words, p ≤ 200 (`scripts/z9_depth_walk.py`).
**Corollary 2.2.** Word ∈ S₈ ⟺ some pentagon walk has ≥ 2 half-steps, i.e. the pointer continues the certificate edge through
the pointed endpoint into a second edge. Equivalently, the pentagon element fixes a cyclic 4-isogeny (a point of X₀(4)). This makes
O224's tree-depth Assessment exact (the distance is k − 2 half-steps beyond the pointed endpoint).
**Proposition 2.3 (correlation).** With all letters odd, v₂A + v₂A* = v₂(tp + 1) =: s, and the two pointers, if both exist, run in
opposite directions. So 8 | A or 8 | A* forces s ≥ 4, and for s = 4 only a lopsided split works. With t even, the depth of e₂ is v₂(t).
So the bit is a function of a letter or of (t, p) mod 2^s and is shared by all words with that t. This is the mechanism of O224's
excess of S₈-empty primes.

## 3. What global data can and cannot see (z9_brandt_screen)
| level | data | sees | status |
|---|---|---|---|
| L1 | Hecke-equivariant / trace-formula / mass | Σ_path 1/|Aut| = word count (full-rank Siegel–Weil is a tautology) | PROVED (linear algebra) |
| L2 | degree-2 Siegel–Weil on planes M = [[v,−1],[−1,t]] | M up to genus; glue residue ±1 invisible (Prop 10.3 shadow) | PROVED placement (O224 Prop 3.1) |
| L3 | class-wise theta series (Schiemann) | everything, but "∃ class" is the problem itself | B2 |
| layers | r_L(m), m small; spine, loops | deterministic sets ≍ h(−4mp) | PROVED (Thm 1.1) |
So a global pigeonhole would have to act on the glue residue of a binary plane. Equivalently (§4) it would have to act on a
ray-class condition mod t on CM points, and t is part of the solution.

## 4. The Heegner-layer dictionary (Assessment with PROVED algebra; z9_heegner_layers)
In E(L_w): ε = −(1 + ij), ε² = −tp, j ⊥ ε, nrd j = A, i = (1 + ε)j/A (PROVED). By Deuring lifting, ((E, C), ε) is the reduction at the
ramified prime p of a CM point of X₀(2) with CM by an order containing ℤ[√−tp]. **Certificate edges in layer t are the reductions
whose ideal class contains an ideal of norm A ≡ −1 (mod t) with A | tp + 1.** This puts CONSTRUCTIVE_ES ((J)35) and WINDMILL's
ℤ[√−tp] framework (Prop 10.3 / Rem 10.4) on one geometric object. Equidistribution of these CM points among supersingular points
(Michel 2004 type) sees the genus only.

## 5. Controls
* **T1 / what plays G_p at m².** No definite algebra B_{m²,∞} exists, so there is no graph and every count is vacuous (CONSTRUCTIVE_ES 5.4).
* **Composite 105 (CERTIFIED, inline computation with `z9_lib`).** For n = 105 the analogue graph *does* exist: the 2-neighbour component of
  ⟨1, 3, 35⟩ (2-adically isotropic, det 105) has 4 vertex classes and 4 edge classes. But none of the 11 words of 105 is
  2-adically isotropic, so there is no path edge. **Any global forcing argument must use primality beyond the existence of a
  2-isogeny-type graph**, so it cannot be a statement about 3-regular graphs with mass (p − 1)/24 alone.
* **TES (goal 3).** The order-3 analogue has no Fano: §0 (I7). It is consistent with TES's 16 certified failures and with ES-five's
  absence of failures to 10⁸: ES's numerator 4 is at the character level (zero bits), TES's 9 = λ⁴ is not (Assessment).

## 6. Outcome
* PROVED: Thm 1.1 (loops ⟺ represents 2; layers), Thm 2.1 / Cor 2.2 / Prop 2.3 (depth = walk length; 8/p as X₀(4); bit
  correlation), the L1 claim of §3, and the algebra of §4.
* EVIDENCE: no parity/degree law to 10⁴; triangle decoupling to 5000; TES χ₃ independence to N ≤ 787 (one slice).
* Negative (precise): a global Fano over G_p would have to force a ray-class residue mod a varying t on the CM points of
  layer t (B2, moving modulus). Every exactly computable global quantity is at most genus-level (L1/L2). The existence of
  the graph alone cannot suffice (105).
* No positive ES claim is made, so no 10⁶ triple-check was required. All numerical claims are reproducible with the
  listed scripts.
