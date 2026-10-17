# z28_complete_levels — where "visible" means "transports" (O257; NONCONG_LIFTS §2.4–2.5)

**Idea.** O253 showed invisibility (p ≡ □ mod the input level) kills determined lifts. Converse question: at which
levels L is visibility *sufficient*, i.e. every non-square unit class mod L lies in a witness class with H | L
("complete level")? A complete level containing a non-residue prime of p would make every source witness at that
level transport.
**Results.** (i) CERTIFIED: for k = 4 the complete levels with L ≤ 1600 are all 7-smooth, and a 7-smooth L is complete
iff (3 | L ⟹ 8 | L) and (7 | L ⟹ 24 | L) (L ≤ 6000; "if" PROVED by monotonicity + 16 base levels). For k = 8, 12 there is
no complete level km, m ≤ 400. (ii) **Thm 2.6 (PROVED):** the point x_{ℓ,2} (2 at ℓ, 1 elsewhere) lies in no witness
class for every 4 | k ≥ 8 and odd ℓ ∤ k; for k = 4 it is covered iff ℓ ∈ {3, 5} (Mordell's slices (1,6), (1,5), (2,5)).
So no level divisible by a prime ℓ ≡ ±3 (8) is complete — for k ≥ 8 including 3, 5; for k = 4 for all such ℓ ≥ 11.
(iii) For p ∈ 𝓜, p is a square modulo every 7-smooth level, so every complete level is invisible to p.
**Literature.** Mordell's six classes mod 840 (Mordell 1969); Salez arXiv:1406.6307 (S₁₁ = {7, 8, 10}, filters);
MODEL_SPECIFIC §4.1 (O197: uncovered classes mod 840/9240/120120 for m = 4…12); POINTWISE_MORDELL (Σ_r coverings,
sterile points).
**Barrier screen.** B1: completeness is a finite-level covering notion — exactly Mordell's theorem at level 840, and
Thm 2.6 shows it cannot extend to ℓ ≡ ±3 (8), ℓ ≥ 11 for ES. T1: built in (squares never covered). (J)41: Thm 2.6 is a
*non*-numerator-blind statement (4 vs 8 differ), via an inequality b₀(k − 4/g) ≤ 3 — numerator size, not reciprocity.
**Cheap numerics.** `scripts/z28_complete_levels.py`, `z28_adelic_fast.py`, `z28_adelic_scan.py`, `z28_x2_check.py`
(hits exactly the four Mordell classes for k = 4, ℓ ∈ {3, 5}; none otherwise, k ≤ 32, ℓ < 60, a ≤ b ≤ 300).
**Assessment.** PROVED (Thm 2.6) + CERTIFIED/EVIDENCE. The only 4-specific resource the lift picture has is Mordell
completeness, and it is exhausted on 𝓜. Spark: extend Thm 2.6 to x_{ℓ,r}, r = least non-residue (the Case-A
parametrisation L = ckas − (a + c)/b₀, L | a + rc bounds L ≤ poly(r)), giving "complete levels are 7-smooth" for k = 4.
