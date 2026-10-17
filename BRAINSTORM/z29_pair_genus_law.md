# z29_pair_genus_law — T1 as a Jacobi identity on b = 1 pairs, and its 2-adic escape (O259; B1_LINE §1)

**Idea.** Write the b = 1 line as pairs {S, T}, ST | p + S + T, 4 | S (Lemma 1.1). Locate exactly where the non-residue that
T1 demands sits, hoping for a b = 1-specific "escape" that the c = 1 line (★) lacks.
**Literature.** ET 2013 Prop 1.6 (Type I/II vanish at squares); O258 Lemma 2.2(a) ((w/p) = −1); classical covering identities
(Mordell, Diophantine Equations ch. 30; the classes 5 (12), 13 (24)).
**Result (PROVED).** (ST/p) = −1 always, and (S′T/p) = −(2/p)^k with S = 2^k S′ (Lemma 1.2). So for p ≡ 1 (8) the odd part
holds a non-residue prime. At p ≡ 5 (8) with v₂(S) odd, 2 is the non-residue ("free" pairs). (★) has the same structure
(free pairs with v₂(x) = 1). Both lines are trivial outside p ≡ 1 (24) for b = 1 (pairs (3, 4), (3, 8)) and p ≡ 1 (8) for
(★) (pair (1, 2)) (Prop 1.4).
**Barrier screen.** B1: the escape only acts on classes already covered by fixed identities. T1: the law IS T1 (no pair can
have odd part all-QR at p ≡ 1 (8)), so odd squares fail as they must. B5/B6 n/a. 105: composite, outside the scope (gcd
argument uses primality).
**Cheap numerics.** `z29_genus.py 20000`: 12 717 b = 1 and 5 710 (★) pairs, 0 violations; free pairs only in the class
(p mod 8, v₂ mod 2) = (5, odd).
**Assessment.** PROVED, correct, non-discriminating. The first reading ("2-adic escape makes b = 1 more robust") was refuted
within the iteration: the escape is shared with (★) and acts only on classes that are trivial anyway.
