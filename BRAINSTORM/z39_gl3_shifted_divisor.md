# z39_gl3_shifted_divisor — the level sum is an additively shifted ternary divisor function (O269)

**ES is not solved here.** Labels as in DISCOVERIES.md. Deep version: METAPLECTIC_ES §4.

## Idea
Thm K makes every level a GL(2) Eisenstein object; the sum over levels is where B2 lives. Sum in the other order to
identify the automorphic home of the full count R(n) (and of N₋, by twisting).

## Statement (PROVED, trivial identity; reading Assessment)
Σ_n R(n)q^n = Σ_{t,u,v≥2} q^{tuv−u−v} = Σ_{u,v≥2} q^{2uv−u−v}/(1 − q^{uv}) (PROVED). Analogy only: with t, u, v ≥ 2 the
unshifted series Σ q^{tuv} has coefficients d₃(n) − 3d₂(n) + 3 − 1[n = 1], and the specialisation x = y = q⁻¹ of
Σ_{t,u,v≥1} x^u y^v q^{tuv} diverges (t = u = 1), so R is a boundary-truncated, additively shifted relative of
Σ d₃(n)q^n (SL₃(ℤ) minimal-parabolic Eisenstein coefficients).
Equivalently R(n) = #{(u, v) : uv | n + u + v, n ≥ 2uv − u − v} (SIGN_IDENTITY Lemma 1.1): a union of arithmetic
progressions −(u+v) mod uv — the B1 covering picture — and the generating function is the corresponding sum of
geometric series. So R is "d₃ with an additive shift −u − v", the GL(3) analogue of Kronecker's GL(2) identity
(x^u y^v q^{uv} → x^u y^v q^{tuv}). Average Σ_{n≤X} N₋ ~ (15/64) X log²X ((J)39) vs Σ d₃ ~ ½X log²X.

## Literature
Bump, *Automorphic forms on GL(3,ℝ)*, LNM 1083 (d₃ as Eisenstein coefficients); Friedlander–Iwaniec, "Incomplete
Kloosterman sums and a divisor problem", Ann. Math. 121 (1985) (d₃ in progressions — the averaged analogue);
Heath-Brown, "The divisor function d₃(n) in arithmetic progressions", Acta Arith. 47 (1986).

## Barrier screen
B6: d₃-in-progressions results are averages over moduli or over n; at one n they say nothing. B1: the (u, v)-first
order is literally a congruence covering. B3: log² = triple pole of ζ³ — the expected-count scale. B2: fixing n and
summing over t is a shifted convolution of d₃-type at a single point. T1: invisible in K₃ (it lives in the
Jacobi-symbol twist of N₋, i.e. in characters of the levels).

## Cheap numerics
Identity checked as a power series to q^{1500} by `scripts/z39_kronecker.py` (via the per-level form).

## Assessment
PROVED identity (folklore-level); the GL(3) reading is Assessment. Confirms (J)39's steering ("divisor rank ≥ 3,
unboundedly many levels") with an explicit object; no route. Promise 0–1/5.
