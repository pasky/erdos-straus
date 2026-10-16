# z23 — the Astra–Claude meeting point (2k, 1) is a finite set, empty for 99 primes ≤ 10⁶ (O251)

## Idea
ASTRA_BRIDGE Thm 3.4(c): ES "of this shape" = lattice points (2k, 1) with k | h on some slice lattice L_ρ(g) ⊂ ℤ[√−p].
Before designing a descent towards it, ask whether the target exists. LATTICE_MEETING Prop 1.1: the target set is
{(a, b, k) : a + b = k(4ab − p)} ⟷ {(a, g) : g | p + 4a², g ≡ −1 (mod 4a)}, ES point 4/p = 1/(ab) + 1/(pka) + 1/(pkb),
finite since (4a−1)(4b−1) ≤ 4p + 1.
## Literature
Elsholtz–Tao 2013 Prop 1.3 (Type II parametrisation, here ET's d = 1); FIXED_MODULUS_SHOTS Lemma 1.1 (certificate cube,
3cd ≤ p + 1); EXP_OPEN row II-ad.
## Barrier screen
B1/B2: per a, "p + 4a² has a divisor ≡ −1 (mod 4a)" — a divisor-class event with solution-dependent modulus; finitely
many a ≤ √p/2. T1: empty at odd squares (Cor 1.2(a)). Hypothesis that kills the descent: the target is restricted to
height Y = 1 (square ET d). Violating it: heights √d (z23_norm_blind_predicate, LATTICE_MEETING Thm 1.4).
## Cheap numerics
`scripts/z23_meet.py 1000000`: exactly 99 of 39 175 primes p ≡ 1 (4) ≤ 10⁶ have 𝓜(p) = ∅ (13, 37, 97, 181, 193, …),
all ≡ 1 (12); independent k-scan agrees on p ≤ 2·10⁴. `scripts/z23_rescue.py`: rescued at ET d = 2 (96), 3 (1), 5 (2).
## Assessment
PROVED (Prop 1.1) + CERTIFIED (list). Negative for the O251 descent as posed: "Y = 1 reachable for every p" is false.
Corrective: the full meeting set is the square-class meeting Y_k² ≡ d | k.
