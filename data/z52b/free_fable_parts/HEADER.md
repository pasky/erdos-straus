## Method and coverage notes

**Method.** Free association (lane `free`, seat fable), breadth-first. I walked through lenses in turn — physics
(stat-mech, integrable systems, RMT, quantum chaos, localization), CS (complexity, SAT, automata, lattices/Coppersmith,
program synthesis, ML), history of Egyptian fractions (Sylvester, Rhind, Yamamoto, Croot, Bloom), people/communities,
algebraic & analytic number theory (class groups, ray class fields, sieves, Eisenstein/trace formulas), topology/
dynamics, logic, recreational math, and meta items — and for each lens wrote down every connection that survived a
one-minute nonsense check. No barrier screening (per the z52b brief); repo barriers are mentioned only as tags.

**Conventions.** "C-form" = the c = 1 sub-case of Type II: 4Cp + 1 = ab with a ≡ b ≡ −1 (mod 4C) (equivalently the
word p = 4Cuv − u − v). It is a *sufficient* condition for ES, strictly weaker than full Type II (ff′ = 4c²dp + 1,
f ≡ f′ ≡ −1 mod 4cd): primes 409, 577, 5569, 9601 have Type II certificates but no C-form certificate with C < 1500
(`scripts/z52b_free_fable_sanity.py`). Items that speak of "C_min(p)" or "winning C" mean this C-form unless they say
(c,d); such quantities may be undefined for the exceptional primes, and every such item should be re-read with the full
(c,d) family in mind.

**Verified during the lane** (small ranges, `scripts/z52b_free_fable_sanity.py`): C = 1 C-form wins ⟺ 4p+1 has a prime
factor ≡ 3 (mod 4); gcd(4Cp+1, 4C′p+1) | 4(C′ − C); odd squares m² (m ≤ 39) have no C-form certificate with C < 100;
the subgroup-vs-subset-product gap of gate G4 is ≈ 21% of (p, C) pairs in the tested range. Literature citations marked
as facts were checked by web search (Lenstra 1984, Bloom 2112.03726, Salez 1406.6307, Abdulaziz 2008, Charton 2308.15594,
Croot 2003, HKRS 2307.02749); anything else is phrased as "check whether".

**Not covered / thin.** Very little on: higher-rank automorphic methods, arithmetic statistics of cubic surfaces
beyond Brauer–Manin, model-theoretic/o-minimal methods, specific Lean tactic engineering, and the sibling campaign's
files (not read). Items are deliberately unranked except the top-10 list above.
