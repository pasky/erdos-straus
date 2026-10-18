# z41_choosable_ladder — the whole 2-power ladder at one prime is CHOOSABLE by the level, but never reaches the class −1 (O272; §4)

**Idea.** Violate Thm 3.1's hypothesis "congruence data on the level": pick the level prime q by its Frobenius in
ℚ(ζ_m, (−ℓ)^{1/m}) (equivalently its Gaussian/cyclotomic lift mod ℓ).
**Literature.** Chebotarev; Hecke equidistribution of Gaussian primes in ray classes.
**Result.** Prop 4.1 (PROVED): for odd non-square n there is ℓ ≡ 3 (4), (n/ℓ) = −1, and for every m = 2^j the forced primes q ≡ 1 (m)
with −ℓ ∈ G_{4q}^m have relative density 2/m (among forced q ≡ 1 (m); over all forced q the fractions are ≈ 0.75, 0.69, 0.67);
with v₂(q − 1) = j fixed exactly, the whole 2-part of −ℓ's class is trivial; at q ≡ 3 (4) this is even FORCED (the 2-Sylow is
(ℤ/2)², characters χ_{−4}, χ_{−t}) — so "lottery shrinks to the odd part" holds trivially there, the odd part being (q − 1)/2. Prop 4.2 (PROVED, trivial): a prime ℓ < t − 1 is never ≡ −1 (t); a divisor in class −1 has size ≥ t − 1 (and is not the full cofactor N/ℓ,
whose class is [ℓ]⁻¹), and once a
divisor d is fixed the level is the residue of −n⁻¹ mod d — no free parameter: the ES lottery itself.
**Barrier screen.** B2: the lottery shrinks to the odd part only for the small prime, which cannot carry the class; the
individual large prime factors are uncontrolled (CLASS_FORCING Thm 5.2). B3/B6: choosing levels by Frobenius is a density statement over q, not pointwise.
**Cheap numerics.** `scripts/z41_minus_l.py`: 1405/2819, 350/1406, 82/713 ≈ 1/2, 1/4, 1/8 (n = 13, ℓ = 7), same for four others.
**Assessment.** PROVED (positive density) + PROVED (size obstruction). Choosable ≠ forced; dead end for a pointwise mechanism.
