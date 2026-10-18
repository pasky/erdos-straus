# z33_census_tiers — forced vs actual vs cap-relaxed certification to 10⁶; T1 factor by factor (O263; §7; EVIDENCE)

**Idea.** Measure how much of the b = 1 line the forced mechanism certifies, and compare with the actual event and with
the generated-subgroup relaxation; T1 control.
**Result (EVIDENCE; logs/z33_census_1e6_D200.txt, logs/z33_haar_forced.txt).** Levels ≤ 200, 39 175 primes p ≡ 1 (4) ≤ 10⁶:
actual fails at 193, 2521, 66529, 252001; Gen (−1 ∈ ⟨factors⟩) never fails; forced F₁₀/F₃₀ fail at 734/43 primes; the exponent-2
shadow X2 fails at 73 primes (incl. 2521; 193 and 66529 pass). All tiers (Gen included) fail at all 499 odd squares.
**Sharp-ish observation (PROVED).** Gen fails at every odd square at every level, because every ℓ | m² + 4d has
χ_{−4d}(ℓ) = (m²/ℓ) = 1, so ⟨factors⟩ ⊂ ker χ_{−4d} ∌ −1. At a prime, χ_{−4d}(ℓ) = (ℓ/p): T1 vs prime is visible factor by
factor through exactly one quadratic link, and nowhere else.
**Assessment.** The forced mechanism is an ET covering: high coverage, never complete (Thm 3.4). No new existence mechanism.
