# s3_eps_mu_sieve — (J)23 Gupta–Murty sieve × (J)38 ε_μ slot: the sieve variable and the ES slot coincide

**Combines:** (J)23 (sieve over primes r with r | n + 4Q², Q ∈ ⟨S⟩, fixed firing modulus), (J)38 Thm 1.3 (ES at μ = nj + t
⟺ |N ε_μ| = 4tj − 1 divides μ), (J)25 Thm 2.1 (finitely many shots per firing set).

## Idea
Run the (J)23 sieve over μ instead of over r: choose μ so that the single element ε_μ has norm dividing μ.

## Result (PROVED, elementary)
4tj − 1 | nj + t ⟺ 4tj − 1 | n + 4t² (multiply by 4t: 4t(nj + t) = n(4tj − 1) + n + 4t², and gcd(4t, 4tj − 1) = 1).
So on the t-line, the ES slots ε_μ (μ = nj + t, j ≥ 1) fire exactly at the divisors g = 4tj − 1 of the ONE number
n + 4t² lying in the class −1 (mod 4t): the (J)23 shot with Q = t and the cap-0 condition Q | (g+1)/4. Sieving μ
along a line is therefore sieving the divisors of a single integer — a finite set (cf. GROWING_MUTE Prop 2.1) — and
across lines it is the shot family n + 4t² with the moving firing modulus 4t (B2; (J)25 Thm 2.1 kills any fixed
firing set). The (J)23 sieve succeeds because its Q is free in ⟨S⟩ (typically Q ≫ r, overflow Q₁ = Q); the ES slot
needs Q = t ≤ (g+1)/4.

## Literature
Gupta–Murty (Artin with |S| ≥ 3 primes) as used in UNIT_ORBIT_ES; COMPOSITION_ES Thm 1.3.

## Barrier screen
B2/B3: moving modulus 4t; (J)25 Cor 2.3 (only three modulus-4 shots).

## Cheap numerics
Identity verified on all odd n < 400, t, j < 40 (`scripts/s3_bit_vs_box.py`, 0 mismatches).

## Assessment
Dictionary closing the brief's "(J)23 sieve × (J)38 ε_μ" item: the two objects are the same shot, with Q = t forced
small on the ES side. Collapses to (J)25/(J)34. Promise 0.
