# Brainstorm O152(b): topological / fixed-point existence arguments for ES

Status: **ES is not solved here.** Verdict: COLLAPSES (reduces to memo (a) or to local data). Two small
PROVED observations (Lemma T, Prop K).

## 1. Idea

Prove existence of an ES solution for p from a topological principle applied to a finite structure K(p):
* combinatorial: Sperner / Tucker (combinatorial Borsuk–Ulam) / mod-2 degree / Smith theory
  (`χ(K^{ℤ/2}) ≡ χ(K) (mod 2)`) / Lefschetz–Hopf for a simplicial self-map of a finite complex;
* arithmetic-geometric: Grothendieck–Lefschetz trace formula for Frobenius on the ES surface over F_q,
  Chevalley–Warning / Ax–Katz;
* discrete intermediate value theorem: an integer-valued h on a connected graph with `|Δh| ≤ 1` along
  edges that takes both signs has a zero.
It would prove ES if the forced object (fully labelled simplex, fixed cell, zero of h, F_q-point) were,
or mapped to, a positive integral solution for every p.

## 2. Literature anchor

Sperner, Tucker, Smith theory, Lefschetz–Hopf, Grothendieck–Lefschetz, Chevalley–Warning: standard (from
memory). In complexity terms (`BRAINSTORM/logic_complexity.md`): Sperner/Tucker/degree arguments are PPAD/PPA
totality proofs; Jeřábek (as cited there) puts FACTOR in PPA∩PPP (randomised). No ES-specific topological
argument is known to me.

## 3. Screen

**Lemma T (PROVED; standard bookkeeping).** Each finite principle above, applied to a finite complex K(p)
with a map Φ from the forced cells to positive solutions, yields an identity
`Σ_{sol} w(sol) = I(p)` where `w(sol)=Σ_{cells c ↦ sol} ε(c)` with explicit signs/multiplicities and I(p)
is the "topological side": mod 2 for Sperner (handshake: #fully labelled ≡ #boundary-labelled), Tucker,
mod-2 degree and Smith (`χ(K^G) ≡ χ(K)`); in ℤ for Lefschetz–Hopf (`L(f)=Σ_i(−1)^i tr(f_#|C_i)`, the
Hopf trace counts cells mapped onto themselves with orientation signs). So the mod-2 principles are
instances of WINDMILL Lemma 1 / memo (a) (an odd weighted count), and the ℤ-valued one is a signed exact
identity of the kind in B2 ("exact class-number identities"). The topological side I(p) plays the role of
#Fix σ in (a): it must be *computed* for every p, and it must not be computable from p mod M (else B1/T1,
cf. Prop S in memo (c)). Nothing new beyond (a)/(c) is gained by phrasing the parity topologically.

**Prop K (PROVED, elementary): the solution complex is parity-blind.** Let K(p) be the 2-complex whose
vertices are the denominators occurring in positive solutions of 4/p and whose 2-cells are the solutions
`{x,y,z}`. Then (i) any two distinct denominators lie in at most one solution (z is determined by x,y);
(ii) positive solutions have distinct coordinates (WINDMILL Lemma 4); hence every edge lies in exactly one
triangle, `E=3f`, `χ(K)=V−2f`, and K is homotopy equivalent to the bipartite incidence graph
(denominators ∪ solutions, 3f edges), with `b₁ = 2f−V+c` (c = #components). Consequently every
Euler-characteristic, Smith or mod-2 Lefschetz argument on K sees f(p) only with weight 2 — the
topological analogue of WINDMILL Prop 5 (S₁₁₂ sees ES with weight 6). The parities of V and c were already
found to be ~50/50 (WINDMILL §3.3).

**Grothendieck–Lefschetz / Chevalley–Warning.** These count points of a variety over F_q (or mod N).
Any existence statement they give is a statement about local solutions, true for p and for every n with
the same local data — in particular for m² when restricted to Type I/II. Collapses at T1/B5 (local and
spinor conditions hold at odd squares, (I)4) and at B1 (Theorem C: local/congruence data cannot certify
ES). For general solutions, local solvability holds for all n (Bright–Loughran: no BM obstruction), so
there is nothing to lift; the lift is ES itself ((I)7).

**Discrete IVT.** Integrality of z is a divisibility, not a zero of a slowly varying function. If h is
polynomial in a path parameter and `|h(t+1)−h(t)| ≤ 1` on a long path, h has degree ≤ 1 with slope ≤ 1
(for unbounded paths), so its zero is a *linear congruence-type* event — a covering certificate (B1). A
non-polynomial h (e.g. defined through divisors) must be constructed so that its zeros are ES
certificates; the sign change then has to be proved for every p, which is the original problem. No
reduction gained (Assessment, not a theorem).

## 4. Experiment

None needed beyond Prop K (whose inputs are proved) and memo (a)'s E1–E4; the relevant parities (V,
components, edges of the solution/refactor graph) were measured in WINDMILL §3.3 (45–56% odd).

## 5. Viability

**COLLAPSES.** Finite topological principles = weighted parity/signed counts (Lemma T) → memo (a)/(c);
the canonical complex is parity-blind (Prop K); F_q-Lefschetz/Chevalley–Warning are local (B1/B5);
discrete IVT needs a slowly varying function whose zeros are divisibility events, which reduces to a
congruence certificate or to ES itself. By-products: Lemma T, Prop K (both PROVED, elementary).
