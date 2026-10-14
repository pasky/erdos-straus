# STERILE_EXPLICIT — the function-field class-divisor machinery over ℤ: explicit sterile Mordell points (O219, spark relay Y9)

Status: in progress (O219). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on DEPTH_ASPECT.md §3 ((J)26 Thm 3.1, reviews R178/R187), FF_STERILE_PUSH.md (O216, Lemmas 1.1–1.6, 2.1),
POINTWISE_MORDELL17*.md (= M17, M17B, M17C, M17D), STERILE_STEER.md. Scripts `scripts/se_*`.

## 0. Iteration log

* (I1) Dictionary. O216's Case B tuples (m', g', w, C, v) with m'wC = T^s + v, w + C = g'v are *literally* the ℤ
  P-data of M17 (N-points of Σ^II_N, N = r^K): 4d·a·b = N + e, a + b = c·e. So (m', g', w, C, v) ↔ (4d, c, a, b, e),
  E = L'w − 1 ↔ f = 4acd − 1, Lemma 1.1(i) Ev = T^s + m'w² ↔ ef = N + 4a²d (ET (2.19)), and the FF degree identity
  y + t = max(a, b) ↔ the size relation ce = a + b ∈ (b, 2b]. Every FF route has a ℤ twin (§1, Table 1.2).
* (I2) Continuum steering (`scripts/se_rate.py`, EVIDENCE/Assessment). With sizes a = N^α, c = N^γ, d = N^δ, e = N^ε
  (α + γ + δ + ε = 1 up to O(1/log N), 2α + δ ≤ 1), and a divisor loss τ(m) ≤ C(η)m^η charged where no class
  bound applies, the best route exponent θ*(η) = max_pattern min_route is 0.400 (η = 0), 0.417 (0.1), 0.467 (0.2),
  0.500 (0.25), 0.533 (0.3). ET's four-regime argument tolerates only η ≈ 1/18 (its loss is η·(1 + 4/5) on top of 2/5),
  which is why (J)26's r₀ is a tower. The transplant tolerates η < 1/4. The binding corner is
  a ≈ b ≈ d ≈ N^{1/3}, e ≈ N^{1/6}: balanced triple factorisations of (N + e)/4 with a ≡ −b (mod e), exactly at the
  Coppersmith threshold for the class route (modulus e vs divisor b ≈ m^{1/2} of m = (N+e)/(4a), threshold m^{1/4}).
