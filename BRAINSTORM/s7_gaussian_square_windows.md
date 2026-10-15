# s7_gaussian_square_windows — a positive-density FORCED budget at primes, and why it is useless (O247, (i)/(v))

## Idea
Mandatory (i) asks for any positive-density mechanism forcing the exponent budget at a window. Gaussian structure gives
one: for p = a² + b² (a odd, b even) and signs ±, the window m = 2AB + 2A + 2B + 1 (A = ±a, B = ±b, m > 0) satisfies
m ≡ 3 (4) and **K_m = ((A + B + 1)/2)² is a perfect square** — every exponent of K is even and ≥ 2, at every prime
p ≡ 1 (4) (identity: (A + B + 1)² = p + m). This is the exact opposite of (J)64: budget forced, subgroup not
(K is a square, so (K/m) = 1 and reciprocity forces no non-residue prime).

## Literature
CAP_POINTWISE Thm 1.1 (forced subgroup, unforced budget); NEAR_SQUARE / (J)61 (near-square windows K = S²);
POINTWISE_BINARYFORM (binary-form families); CONDITIONAL_ES Prop 2.3 (B3 scale).

## Barrier screen
B3/B2: the window has size m ≍ ab ≍ p (sector-dependent), so cap 0 asks for d | S⁴ in one residue class mod m ≍ p: a
1/m lottery with τ(S⁴) ≈ p^{o(1)} tickets. The forced budget is real but sits at the wrong scale (B3: main term
≤ p^{o(1)}). T1: at n = c², the representation (c, 0) gives m = 2c + 1, K = ((c+1)/2)² and the window must fail (CAP_DOWN
T1) — consistent, since the condition is a congruence lottery, not forced.

## Cheap numerics (scripts/s7_gauss_lvalue.py)
All primes p ≡ 1 (4) ≤ 10⁶: 78 239 Gaussian square windows, cap-0 rate 1.0·10⁻⁴; control windows of the same size
(m + 4j, |j| ≤ 3): rate 1.0·10⁻⁴. The forced square budget gives no measurable advantage.

## Assessment
EVIDENCE + PROVED identity. Positive-density forced budgets exist (norm-form structure) but only at windows of size ≍ p,
where they are swamped by the residue lottery. Combined with s7_normform_collapse (Type I/II polynomial families in
binary-form coordinates are ET identities in n), the norm-form route to forced budgets is closed at both ends: small
windows have no algebraic structure, large ones have structure but no leverage.
