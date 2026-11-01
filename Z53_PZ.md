# Z53_PZ — R(p) ≫ log²p for almost all primes (wave z53b, side target Z2362)

**ES is open. Nothing here proves or disproves ES at any prescribed prime.** Labels: PROVED / CONDITIONAL / CERTIFIED /
EVIDENCE / CONJECTURE / Assessment. Everything is internally reviewed only. Scripts `scripts/z53_pz_*`, data `data/z53/pz/`.
Kickoff: `z53_lanes.md` §PZ (ES_CONNECTIONS_TODO Z2362).

## 0. Verdict and summary

**Verdict: STRENGTHENED (an average statement; B6 applies).** The Z2362 target asked for a positive proportion. We prove the
stronger concentration form, with an explicit constant and an explicit exceptional-set rate:

> **Theorem A (PROVED rel. Bombieri–Vinogradov and elementary divisor-sum bounds).** For every η ∈ (0,1) there is X₀(η) such that
> for X ≥ X₀(η)
>   #{p ≤ X prime : R(p) < (1 − η)(log p)²/64} ≤ (C/η²)·π(X)/log X,
> where C is an absolute constant (C = 6·10³ is admissible for large X). In particular R(p) ≥ (1/64 − ε) log²p for all but
> O_ε(X/log²X) primes p ≤ X, and **f(p) ≥ f_II(p) ≥ R(p) ≫ log²p for almost all primes.**

* **Literature check** (research subagent; verified from source text, §10). The best almost-all-primes lower bound we found is
  Elsholtz–Tao (J. Aust. Math. Soc. 94 (2013), arXiv:1107.1010v6) **Thm 1.8**: f(p) ≫ (log p)^{(log 3)/2 − o(1)} ≈ (log p)^{0.549}
  on a set of primes of relative density 1. ET **Remark 1.3** calls control of Σ f_II(p)² "out of reach of our methods, as the
  level of the relevant divisor sums becomes too great to handle". The average is ≍ log²p (ET Thm 1.1), so Theorem A reaches the
  true order for almost all p. (Assessment: new as far as we can see. Caveat: an X post we could not open seems to make a
  similar claim; see §10.)
* **The idea, in one line.** Only a *lower* bound is needed, so truncate R to the trial-form events m = 4uC−1 ≤ Q = X^{1/4−o(1)},
  weighted by φ(m)/m ≤ 1. All pair correlations then live at level lcm(m,m') ≤ X^{1/2−o(1)}, inside Bombieri–Vinogradov. The
  variance becomes an explicit character sum. In the trial fibration each residue class r mod d is **one lattice cell**
  (u ≡ −r, C ≡ −(4r)⁻¹ mod d), so the variance is a sum of hyperbolic progression-sum deviations. These are O(log³Q), against a
  mean² of order log⁴Q. This sidesteps ET's "level too great" obstruction; nothing about moduli > X^{1/2} is used.
* **Constant.** κ = 1/64 ≈ 0.0156 against the mean ≈ (3/(2π²)) log²p ≈ 0.152 log²p. Here 1/16 comes from level 1/4 (area
  (1/4)²), ×2 from the u↔B-symmetric trial fibration, and ×(π²/12) from the φ(m)/m weights. Upgrades: unweighted trial
  fibration ⇒ 3/(16π²) ≈ 0.0190; adding the pair fibration ⇒ 9/(32π²) ≈ 0.0285 (§9.2, sketched, not claimed). Level 1/4 is the
  ceiling of this method (§9.2).
* **Positive proportion (the literal Z2362 ask)** follows a fortiori. The full second moment Σ_p R(p)² ≪ π(X) log⁴X is *not*
  proved, and is not needed.
* **Screens (§11).** T1: passes; the step false at odd squares is BV equidistribution of units. 8/131: passes vacuously
  (density statement). Tied modulus: handled only on average. **Fixed p: FAILS (B6).** The 14 primes ≤ 10¹⁰ with R(p) = 0 are
  admissible exceptions.
* **Numerics (EVIDENCE, §8).** The exact model variance V of the truncated family satisfies V/log³Q = 0.0211–0.0215 (flat) for
  Q = 10²…3·10⁴. Empirical variances over 7.2·10⁵ primes near 10¹² match the model formula to 3 digits.

## 1. Statements

R(n) := #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n} (FRONTIER §2.1). Every triple gives the Type II solution
4/n = 1/(uBC) + 1/(nBC) + 1/(nuC), injectively, so f(p) ≥ f_II(p) ≥ R(p) when f counts ordered triples (x,y,z). The trial
form: for a prime p, a pair (u,C) with m := 4uC − 1 dividing p + u gives B = (p+u)/m and a triple.

**Target as briefed (Z2362):** ∃ c > 0 with R(p) ≥ c log²p for a positive proportion of p ≤ X.
**Proved (Theorem A, §0):** the almost-all form, κ = 1/64, exceptional set ≪ π(X)/(η² log X).
**Not proved:** (ii) of the brief, Σ_{p≤X} R(p)² ≤ C₂π(X)log⁴X (moduli > X^{1/2}; cf. ET Rem. 1.3). Also not proved:
concentration of R itself (R(p)/M₀(p) → 1 in density). The upper tail of R is untouched; Linnik's large values (FRONTIER
§2.2) are compatible with everything here.
**Why not closed:** every closed item is a pointwise (fixed p) mechanism or an average that loses the constant. Theorem A is an
averaged one-sided statement at the right order, obtained by discarding the high-level part of R.

## 2. The truncated family

Fix X large, L := log X, and A₀ := 200. Let B₀ = B(A₀) be the Bombieri–Vinogradov exponent of §3, and put

  Q := X^{1/4} L^{−B₀/2},  Y := (Q+1)/4,  𝒯 := {(u,C) ∈ ℕ² : m_{uC} := 4uC − 1 ≤ Q} = {(u,C) : uC ≤ Y}.

For an odd n define the weighted truncated count
  N(n) := Σ_{(u,C)∈𝒯} c_{uC}·1[m_{uC} | n + u],  c_{uC} := φ(m_{uC})/m_{uC} ∈ (0,1].
The event m | n + u is n ≡ a (mod m) with a = −u, and gcd(u, 4uC−1) = 1, so a is a unit mod m.

**Lemma 2.1 (PROVED).** If p is prime and p ≥ (Q+1)²/4, then R(p) ≥ 2N(p).
*Proof.* Each (u,C) ∈ 𝒯 with m | p+u gives B := (p+u)/m ∈ ℕ with 4uBC − u − B = Bm − u = p. So it gives a triple of R(p)
with 4uC−1 ≤ Q, and different (u,C) give different triples. By the symmetry (u,B,C) ↦ (B,u,C) of 4uBC − u − B, each (B',C)
with 4B'C−1 ≤ Q and m | p + B' gives a triple of R(p) with 4BC − 1 ≤ Q. No triple lies in both sets. If 4uC ≤ Q+1 and
4BC ≤ Q+1, then p = 4uBC − u − B < 4uBC ≤ 4uBC·C = (4uC)(4BC)/4 ≤ (Q+1)²/4. Hence R(p) ≥ 2#{(u,C) ∈ 𝒯 : m | p+u} ≥ 2N(p),
because c ≤ 1. ∎

**The mean.** M := Σ_{(u,C)∈𝒯} c_{uC}/φ(m_{uC}) = Σ_{uC≤Y} 1/(4uC−1).

**Lemma 2.2 (PROVED).** M ≥ (1/8) log²Y.
*Proof.* 1/(4uC−1) > 1/(4uC). Also Σ_{C≤Y/u} 1/C ≥ log(⌊Y/u⌋+1) ≥ log(Y/u). So M ≥ (1/4)Σ_{u≤Y} f(u) with
f(t) = log(Y/t)/t, which is decreasing and ≥ 0 on [1,Y]. Then Σ_{u=1}^{⌊Y⌋} f(u) ≥ ∫_1^{⌊Y⌋+1} f⁺ ≥ ∫_1^Y f = (1/2)log²Y. ∎

(Asymptotically M = (1/8)log²Y + O(log Y). Numerically M/log²Q = 0.1199–0.1209 for Q = 10³…3·10⁴, data/z53/pz/exactV.txt.)

## 3. Bombieri–Vinogradov input: first and second moments

**BV** (Bombieri 1965, A. I. Vinogradov 1965). Verified statement: Tao, 254A Notes 3 (2015), **Theorem 17**:
Σ_{q≤Q} sup_{a∈(ℤ/q)^×}|Δ(Λ1_{[1,x]}; a (q))| ≪_A x log^{−A}x for Q ≤ x^{1/2}log^{−B}x, B = B(A). The form with max over
y ≤ x is Davenport, *Multiplicative Number Theory*, Ch. 28. The π-form below follows by partial summation, with prime powers
and p | q contributing O(x^{1/2}) per q.
For every A > 0 there is B = B(A) such that
  Σ_{q ≤ X^{1/2}L^{−B}} max_{(a,q)=1} |π(X; q, a) − π(X)/φ(q)| ≪_A X L^{−A}.
We use A = A₀ = 200, B₀ = B(A₀). Note Q² = X^{1/2}L^{−B₀}.

**Divisor-sum facts (classical).** (D1) Σ_{n≤x} τ(n)^k ≪_k x(log x)^{2^k−1}. (D2) n/φ(n) ≪ log log n. (D3) τ(ab) ≤ τ(a)τ(b),
φ(ab) ≥ φ(a)φ(b). Let r(m) := #{(u,C) : 4uC − 1 = m} ≤ τ(m+1).

**Lemma 3.1 (first moment; PROVED rel. BV).** S₁ := Σ_{p≤X} N(p) = π(X)·M + O(X L^{−90}).
*Proof.* S₁ = Σ_{(u,C)} c·π(X; m, −u) = π(X)Σ c/φ(m) + Σ c·E(X; m, −u), with E(X;q,a) := π(X;q,a) − π(X)/φ(q). Also
|E| ≤ 3X/φ(q) trivially. Hence |Σ cE| ≤ Σ_{m≤Q} r(m) max_a|E(X;m,a)|. By Cauchy–Schwarz this is
≤ (Σ_m r(m)²·3X/φ(m))^{1/2}(Σ_m max_a|E|)^{1/2}. By (D1) for τ(m+1)², (D2) and partial summation,
Σ_{m≤Q} r(m)²/φ(m) ≪ L⁵. Hence the error is ≪ (X L⁵)^{1/2}(X L^{−200})^{1/2} = X L^{−97.5}. ∎

**Lemma 3.2 (second moment; PROVED rel. BV).** S₂ := Σ_{p≤X} N(p)² = π(X)·Σ_{P,P' ∈ 𝒯, compatible} c_P c_{P'}/φ([m_P, m_{P'}]) +
O(X L^{−10}). Here P = (u,C) and P' = (u',C') are *compatible* iff u ≡ u' (mod g), g := gcd(m_P, m_{P'}).
*Proof.* The system p ≡ −u (m), p ≡ −u' (m') is solvable iff −u ≡ −u' (mod g). It is then a single class mod n := [m,m'],
and that class is a unit. So S₂ = Σ_compat cc'(π(X)/φ(n) + E(X; n, ·)), with n ≤ Q² = X^{1/2}L^{−B₀}. Let
ν(n) := #{(P,P') : [m_P,m_{P'}] = n}. Then ν(n) ≤ ρ(n)² with ρ(n) := Σ_{m|n} r(m) ≤ Σ_{m|n} τ(m+1). By Hölder,
ρ(n)⁴ ≤ τ(n)³ Σ_{m|n} τ(m+1)⁴. So, using (D3),

  Σ_{n≤Q²} ρ(n)⁴/φ(n) ≤ Σ_{m≤Q²} τ(m+1)⁴ Σ_{k≤Q²/m} τ(mk)³/φ(mk)
                      ≤ (Σ_{m≤Q²} τ(m+1)⁴τ(m)³/φ(m))·(Σ_{k≤Q²} τ(k)³/φ(k)) ≪ L^{161}·L⁹.

For the first factor: Cauchy–Schwarz and (D1) give Σ_{m≤x} τ(m+1)⁴τ(m)³ ≤ (Σ τ(m+1)⁸)^{1/2}(Σ τ(m)⁶)^{1/2} ≪ x(log x)^{159}.
Then use (D2) and partial summation. By Cauchy–Schwarz as in Lemma 3.1,
Σ_compat |E| ≤ (Σ_n ν(n)²·3X/φ(n))^{1/2}(Σ_{n≤Q²} max_a|E(X;n,a)|)^{1/2} ≪ (X L^{170})^{1/2}(X L^{−200})^{1/2} = X L^{−15}. ∎
(The exponents are wasteful; any polylog bound on Σ ν²/φ suffices once A₀ is large.)

## 4. The variance as a character sum

**Lemma 4.1 (variance identity; PROVED, elementary).** Let 𝒫 be a finite family of P = (q_P, a_P, β_P), with gcd(a_P,q_P) = 1
and weights β_P ≥ 0. For a primitive character ψ of conductor d put S_ψ := Σ_{P : d | q_P} β_P ψ̄(a_P)/φ(q_P). Then
  Σ_{P,P' compatible} β_Pβ_{P'}/φ([q_P,q_{P'}]) = Σ_ψ |S_ψ|²   (ψ over all primitive characters, including ψ = 1).
*Proof.* φ([q,q'])φ(gcd(q,q')) = φ(q)φ(q'), since each prime of q or q' appears in the product the same number of times on
both sides. So the left side is Σ_{P,P'} ββ'·φ(g)1[a ≡ a' (mod g)]/(φ(q)φ(q')), with g = gcd(q,q'). By orthogonality,
φ(g)1[a≡a' (g)] = Σ_{χ mod g} χ̄(a)χ(a'). Each χ mod g is induced by a unique primitive ψ of conductor d | g, with χ(a) = ψ(a)
for a coprime to g. So φ(g)1[a ≡ a' (g)] = Σ_{d|g} Σ*_{ψ mod d} ψ̄(a)ψ(a'). Exchange the sums: d | g ⟺ d | q and d | q'. ∎

Apply this with q_P = m_P, a_P = −u, β_P = c_P. Then β_P/φ(q_P) = 1/m_P, ψ = 1 gives S₁ = M, and
  V := Σ_{d>1} Σ*_{ψ mod d} |S_ψ|²,  S_ψ = Σ_{(u,C)∈𝒯: d | m_{uC}} ψ̄(−u)/m_{uC}.
Combining Lemmas 3.1, 3.2 and 4.1:

  Σ_{p≤X}(N(p) − M)² = S₂ − 2M S₁ + M²π(X) = π(X)·V + O(X L^{−8}).   (4.1)

**Lemma 4.2 (Parseval reduction; PROVED).** For d > 1 and r ∈ (ℤ/d)^*, let
A_r^{(d)} := Σ_{(u,C)∈𝒯 : d | 4uC−1, u ≡ −r (mod d)} 1/(4uC−1). Then for any real numbers Λ_d,
  V ≤ Σ_{1<d≤Q} φ(d) Σ_{r∈(ℤ/d)^*} (A_r^{(d)} − Λ_d)².
*Proof.* For d > 1 a primitive ψ mod d is non-principal. So Σ*_{ψ mod d}|S_ψ|² ≤ Σ_{χ≠χ₀ mod d}|T_χ|², where
T_χ := Σ_{d|m} χ̄(−u)/m. Expanding |T_χ|² and summing over all χ mod d gives
Σ_χ |T_χ|² = φ(d)Σ_{r}(A_r^{(d)})² (−u is a unit mod d). Removing χ₀ subtracts (Σ_r A_r)². Hence
Σ_{χ≠χ₀}|T_χ|² = φ(d)Σ_r (A_r − Ā)² ≤ φ(d)Σ_r (A_r − Λ_d)², with Ā the mean over r. Terms with d > Q vanish, since d | m ≤ Q. ∎

**The one-cell structure (the point of using the trial fibration).** If d | 4uC − 1, then gcd(d, 4u) = 1. So for odd d > 1
the conditions u ≡ −r (mod d), d | 4uC−1 are equivalent to

  u ≡ x_r := −r,  C ≡ y_r := −(4r)⁻¹  (mod d).

Hence A_r^{(d)} = Σ_{u ≡ x_r, C ≡ y_r (d), uC ≤ Y} 1/(4uC−1) is a single lattice cell. This is a hyperbolic progression sum,
and there is no sum over factorisations of d. For even d, A_r = 0. In the *pair* fibration (modulus 4uB, residue −(u+B)) one
instead gets a sum over the 2^{ω(d)} splittings d = d₁d₂ (d₁ | u, d₂ | B), and the cross terms between splittings need extra
work (§9.2).

## 5. Hyperbolic progression sums

Throughout §5, d ≥ 1 and x, y ∈ ℤ. Let u₀, C₀ ∈ [1, d] be the least positive integers with u₀ ≡ x and C₀ ≡ y (mod d).

**Lemma 5.1 (one variable; PROVED).** For Z > 0 let h(Z) := Σ_{1≤C≤Z, C≡y (d)} 1/C. Then
  |h(Z) − 1[C₀ ≤ Z]/C₀ − (1/d)log⁺(Z/d)| ≤ 2/d.
*Proof.* Case Z < C₀ + d. Then h(Z) = 1[C₀≤Z]/C₀ and log⁺(Z/d) < log((C₀+d)/d) ≤ log 2.
Case Z ≥ C₀ + d (so Z ≥ d). Let J := ⌊(Z − C₀)/d⌋ ≥ 1 and θ := C₀/d ∈ (0,1]. Then
h(Z) = 1/C₀ + (1/d)Σ_{j=1}^J 1/(j+θ). Comparing the decreasing function 1/(t+θ) with its integral,
Σ_{j=1}^J 1/(j+θ) lies between log((J+1+θ)/(1+θ)) ≥ log((J+1)/2) and 1/(1+θ) + log((J+θ)/(1+θ)) ≤ 1 + log(J+1).
For the size of J+1: J + 1 ≤ Z/d + 1 ≤ 2Z/d. Also J + 1 > (Z − C₀)/d ≥ Z/d − 1, which is ≥ Z/(2d) when Z ≥ 2d; and
J + 1 ≥ 1 > Z/(2d) when Z < 2d. So log(J+1) ∈ [log(Z/d) − log 2, log(Z/d) + log 2]. Hence
|Σ_j 1/(j+θ) − log(Z/d)| ≤ 1 + log 2 < 2. ∎

**Lemma 5.2 (hyperbolic cell; PROVED).** Let Y ≥ 1, H := Σ_{u≡x, C≡y (d); u,C≥1; uC≤Y} 1/(uC), and Λ := (1/(2d²))(log⁺(Y/d²))².
Put 𝓛 := log(4Y) + 2 and assume d ≤ 4Y. Then
  |H − Λ| ≤ 1/(u₀C₀) + 𝓛/(dC₀) + 𝓛/(du₀) + 3𝓛(1 + log d)/d².
*Proof.* H = Σ_{u≡x, u≤Y}(1/u)h(Y/u). Inserting Lemma 5.1 splits H = H₁ + H₂ + H₃ with
H₁ = (1/C₀)Σ_{u≡x, u≤Y/C₀} 1/u, H₂ = (1/d)Σ_{u≡x, u≤Y/d} (1/u)log(Y/(ud)), and |H₃| ≤ (2/d)Σ_{u≡x,u≤Y} 1/u.
By Lemma 5.1 applied to u, Σ_{u≡x, u≤Z} 1/u ≤ 1/u₀ + (log⁺(Z/d) + 2)/d. So
  |H₁| ≤ 1/(u₀C₀) + (log⁺(Y/d) + 2)/(dC₀),  |H₃| ≤ 2/(du₀) + 2(log⁺(Y/d) + 2)/d².
For H₂, let g(t) := log(Y/(td))/t on (0, Y/d]. Then g ≥ 0 and g is non-increasing, since g' = −(1 + log(Y/(td)))/t² ≤ 0.
If u₀ > Y/d then H₂ = 0, and Y < du₀ ≤ d², so Λ = 0. Otherwise d·H₂ = g(u₀) + Σ_{j=1}^J g(u₀+jd) with
J = ⌊(Y/d − u₀)/d⌋. For each j, g(u₀+jd) ≤ (1/d)∫_{u₀+(j−1)d}^{u₀+jd} g and g(u₀+jd) ≥ (1/d)∫_{u₀+jd}^{u₀+(j+1)d} g⁺. Since
u₀+(J+1)d > Y/d,
  (1/(2d))(log⁺(Y/((u₀+d)d)))² ≤ Σ_{j=1}^J g(u₀+jd) ≤ (1/(2d))log²(Y/(u₀d)).
Write λ := log⁺(Y/d²) and δ := log(d/u₀) ∈ [0, log d]. Then 0 ≤ log(Y/(u₀d)) ≤ λ + δ and log⁺(Y/((u₀+d)d)) ≥ (λ − log 2)⁺
(because u₀ + d ≤ 2d). Since dΛ = λ²/(2d),
  |dH₂ − g(u₀) − dΛ| ≤ (1/(2d))·max{(λ+δ)² − λ², λ² − ((λ−log2)⁺)²} ≤ (λδ + δ²/2 + λ log 2)/d,
and 0 ≤ g(u₀)/d ≤ (λ+δ)/(du₀). Now λ + δ ≤ log(4Y): if Y ≥ d² this sum is log Y − log d; otherwise λ = 0 and
δ ≤ log d ≤ log 4Y. Also log⁺(Y/d) ≤ log Y. Moreover λδ + δ²/2 + λ log2 ≤ log(4Y)(1.5 log d + 1), using
δ² ≤ log d·log(4Y). Collecting terms:
1/(u₀C₀) + (log Y+2)/(dC₀) + (log 4Y + 2)/(du₀) + [2(log Y + 2) + log(4Y)(1.5 log d + 1)]/d²
≤ 1/(u₀C₀) + 𝓛/(dC₀) + 𝓛/(du₀) + 3𝓛(1+log d)/d². ∎

## 6. The variance bound

**Proposition 6.1 (PROVED).** With 𝓛 = log(Q+1) + 2 and K₁ := Σ_{d≥2}(1 + log d)²/d² (≈ 4.51),
  V ≤ (16/9)(1 + log 4Q²)(1 + log Q)² + (8ζ(2)/9)𝓛² log Q + 4K₁𝓛² = (32/9 + 8ζ(2)/9 + o(1))·log³Q ≈ 5.02·log³Q.
*Proof.* For even d, A_r^{(d)} = 0; take Λ_d = 0. Fix an odd d with 1 < d ≤ Q, and r ∈ (ℤ/d)^*. Let (u₀, C₀) ∈ [1,d]² be the least positive representatives of
(x_r, y_r) = (−r, −(4r)⁻¹) (§4). Note d ≤ Q < 4Y. Since 1/(4uC−1) = 1/(4uC) + 1/(4uC(4uC−1)),
  A_r^{(d)} = H_r/4 + E_r,  0 < E_r ≤ (1/12)Σ_{u≡x_r, C≡y_r} (uC)^{−2} ≤ (1/12)(1/u₀² + ζ(2)/d²)(1/C₀² + ζ(2)/d²).
(Here 4uC − 1 ≥ 3uC, and Σ_{u≡x}u^{−2} ≤ u₀^{−2} + Σ_{j≥1}(jd)^{−2}.) Since u₀, C₀, d ≥ 1,
E_r ≤ (1/12)[1/(u₀C₀) + ζ(2)/(du₀) + ζ(2)/(dC₀) + ζ(2)²/d²]. Take Λ_d := Λ/4 with Λ from Lemma 5.2. Using 𝓛 ≥ 3.38,
ζ(2)/12 ≤ 𝓛/12 and ζ(2)²/12 ≤ 𝓛/4. Then Lemma 5.2 gives
  |A_r − Λ_d| ≤ (1/3)[1/(u₀C₀) + 𝓛/(dC₀) + 𝓛/(du₀) + 3𝓛(1+log d)/d²].
Apply (a+b+c+e)² ≤ 4(a²+b²+c²+e²). As r runs over (ℤ/d)^*, the u₀ are distinct elements of [1,d], and so are the C₀. Hence
Σ_r u₀^{−2}, Σ_r C₀^{−2} < ζ(2). With φ(d) ≤ d:
  φ(d)Σ_r (A_r − Λ_d)² ≤ (4/9)[φ(d)Σ_r (u₀C₀)^{−2} + 2ζ(2)𝓛²/d + 9𝓛²(1+log d)²/d²].
Sum over 1 < d ≤ Q (Σ_{2≤d≤Q} 1/d ≤ log Q) and use Lemma 4.2:
  V ≤ (4/9)[T + 2ζ(2)𝓛² log Q + 9K₁𝓛²],  T := Σ_{1<d≤Q} φ(d)Σ_{r∈(ℤ/d)^*} (u₀(r)C₀(r))^{−2}.
*Bound for T.* The map r ↦ (u₀, C₀) is injective into {(u,C) ∈ [1,d]² : d | 4uC − 1}, since 4u₀C₀ ≡ 4(−r)(−(4r)⁻¹) = 1. So
  T ≤ Σ_{u,C≤Q} (uC)^{−2} Σ_{d | 4uC−1} d = Σ_{u,C≤Q} σ(4uC−1)/(uC)² ≤ Σ_{u,C≤Q} 4uC(1 + log 4Q²)/(uC)² ≤ 4(1+log 4Q²)(1+log Q)²,
using σ(n) = nΣ_{e|n}1/e ≤ n(1 + log n). This gives the stated bound. ∎

**Corollary 6.2.** V/M² ≤ 64·(5.02 + o(1))·log³Q/log⁴Y = (321 + o(1))/log Q = (1285 + o(1))/log X.

(EVIDENCE: the true V is about 0.0215·log³Q (§8), so the bound is ≈ 230 times too large. It has the right order.)

## 7. Proof of Theorem A

Let η ∈ (0,1) and X ≥ X₀(η). By (4.1) and Chebyshev,
  #{p ≤ X : |N(p) − M| ≥ (η/2)M} ≤ (π(X)V + O(XL^{−8}))/((η/2)²M²) ≤ (4/η²)(1285 + o(1))·π(X)/L.
Let p ∈ (X^{1/2}, X] be outside this set. Then p ≥ (Q+1)²/4 and Lemma 2.1 applies. With Lemma 2.2 and
log Y ≥ L/4 − (B₀/2)log L − log 4,
  R(p) ≥ 2N(p) ≥ (1 − η/2)·(1/4)log²Y ≥ (1 − η/2)(1 − O(log L/L))·L²/64 ≥ (1 − η)L²/64 ≥ (1−η)(log p)²/64
for X ≥ X₀(η). The primes p ≤ X^{1/2} number ≤ π(X)/L for large X. So the exceptional set has size
≤ (5140/η² + 1)π(X)/L. ∎

*Remarks.* (i) The rate is O(π(X)/log X). It comes from V ≍ log³Q against M² ≍ log⁴Q; the numerics show V/M² ≈ 1.5/log Q
(§8), so this is the true order of the method. (ii) In every fixed class b mod W (W fixed, gcd(b,W) = 1), all but
O_W(π(X; W, b)/log X) primes satisfy the bound, because π(X; W, b) ≫_W π(X). This covers the Mordell classes mod 840 and
p ≡ 1 (24). (iii) X₀(η) is ineffective: the implied constant in BV depends on Siegel's theorem. (iv) R(p) ≥ 2N(p) also counts only the solutions certified by moduli ≤ X^{1/4}. So (log p)²/64 is a lower bound
for the *cheap* part of R(p) alone.

## 8. Numerics and controls (EVIDENCE; exact model sums CERTIFIED-style but single-engine)

All commands use `timeout` and `ulimit -v 6000000`. Outputs are in `data/z53/pz/`.
* `scripts/z53_pz_exactV_trial.c Q 1` computes the exact model variance V = Σ_{P,P'}φ(g)1[compat]/(mm') − M² of Theorem A's
  family by brute-force double sum. `scripts/z53_pz_exactV.c Q` does the same for the pair family. Results are in
  `exactV.txt`:

  | Q | log Q | #𝒯 | M | M/log²Q | V | V/M² | V/log³Q |
  |---|---|---|---|---|---|---|---|
  | 10² | 4.61 | 87 | 2.552 | 0.1204 | 2.099 | 0.322 | 0.02149 |
  | 10³ | 6.91 | 1421 | 5.722 | 0.1199 | 6.944 | 0.212 | 0.02107 |
  | 3·10³ | 8.01 | 5089 | 7.708 | 0.1203 | 10.89 | 0.183 | 0.02121 |
  | 10⁴ | 9.21 | 19960 | 10.23 | 0.1206 | 16.70 | 0.160 | 0.02138 |
  | 3·10⁴ | 10.31 | 68094 | 12.84 | 0.1209 | 23.54 | 0.143 | 0.02149 |

  V/log³Q is flat at ≈ 0.0215, matching Prop. 6.1's order (its constant 5.02 is ≈ 230× too large), and V/M² ≈ 1.47/log Q.
  M/log²Q → 1/8 from below, as expected.
  *Pair family (unweighted, modulus 4uB):* V/log³Q = 0.0316, 0.0339, 0.0357, 0.0379 for Q = 10², 10³, 3·10³, 10⁴. This
  drifts slowly upward, consistent with log³Q·log log Q or with a log³Q term plus negative lower-order corrections. V/M² still
  decreases (0.45 → 0.20). This is the cross-splitting effect of §4 (EVIDENCE; see §9.2).
* *Model = reality check.* `scripts/z53_pz_window.c 10¹² 2·10⁷ Q` takes the 723 063 primes in [10¹², 10¹² + 2·10⁷). Their
  empirical variance/mean² of the unweighted counts reproduces the model formula: pair family 0.44939/0.25385/0.19867 vs
  model 0.44980/0.25412/0.19873 for Q = 10², 10³, 10⁴. (`window_Y1e12_H2e7.txt`)
* *Lower tail of Theorem A's N on the same window* (`scripts/z53_pz_window2.c`, `window2_Y1e12_H2e7.txt`):

  | Q | M | class | var/M² | #{N<0.5M}/n | #{N<0.25M}/n |
  |---|---|---|---|---|---|
  | 10³ | 5.72 | all | 0.212 | 0.125 | 0.0240 |
  | 10⁴ | 10.23 | all | 0.160 | 0.074 | 0.0067 |
  | 10⁵ | 16.06 | all | 0.128 | 0.041 | 0.0012 |
  | 10⁵ | 16.06 | p≡1 (24) | 0.096 | 0.061 | 0.0021 |

  The lower tail thins as Q grows, as Theorem A predicts. The class p ≡ 1 (24) has a lower conditional mean (14.80 vs 16.07 at
  Q = 10⁵; the deficit shrinks from 14% to 8% as Q grows from 10³ to 10⁵). This is the RESIDUE_HARDNESS effect, of order
  log Q, which is lower order against log²Q. (Q = 10⁵ exceeds level 1/4 at p ≈ 10¹²; it is shown as a trend only.)
* *Controls.* (a) **Odd squares (T1):** all 5 odd squares in the window have N_pair = 0. Since R(m²) = 0, also N(m²) = 0. The
  model mean M > 0 is *not* attained at squares: squares are not equidistributed among units mod m. That is exactly the BV
  input, which fails for squares (§11). (b) **The 14 primes ≤ 10¹⁰ with R(p) = 0** (FRONTIER §4 item 14: 409, 577, 5569, …,
  8 813 281) have N(p) = 0. They are admissible exceptions, consistent with an exceptional set of size ≪ π(X)/log X. (c) **Scale
  of the threshold at accessible heights:** at p ≈ 10¹², (log p)²/64 ≈ 11.9, while the mean of R is ≈ 0.152 log²p ≈ 116. So
  Theorem A says nothing new numerically at accessible heights. Its content is asymptotic.

## 9. Extensions, limits, and what the method cannot do

**9.1 The brief's first-moment question (PROVED rel. BV and the repo's main-term asymptotics).** Untruncated, at level
X^{1/2}L^{−B} in each of the three fibrations (pair modulus 4uB; trial moduli 4uC−1 and 4BC−1), the three regions of the
log-simplex are disjoint for p > X/L^{2B}. Each has mass (3/(2π²))(L/2)²(1+o(1)) (`BM_CORRECTED_COUNT.md` M₀ asymptotic for
the pair form; FRONTIER §2.2 normalisation for the trial form). BV for each family (as in Lemma 3.1) gives
  Σ_{p≤X} R(p) ≥ (9/(8π²) − o(1))·π(X)·L²,  c₁ = 9/(8π²) ≈ 0.114,
against the conjectural full mean ≈ 3/(2π²) ≈ 0.152 (the missing quarter is the central triangle, where all three moduli exceed
X^{1/2}). The Paley–Zygmund route would then need (ii), Σ R(p)² ≪ π(X)L⁴. That is open here, and per ET Rem. 1.3 out of reach
of divisor-sum methods. Theorem A makes it unnecessary.

**9.2 Upgrades of κ (Assessment / sketched, NOT claimed).**
* *Unweighted trial family* (c = 1 instead of φ(m)/m). Then 1/φ(m) = (1/m)Σ_{s|m}μ²(s)/φ(s). For each s the cell A_r splits
  into φ(s′) cells mod lcm(d,s) (s′ = s/(s,d)), and Lemma 5.2 applies to each. The 1/u₀-spikes over the s′-cells sum to
  ≤ 1/u₀(r) + (1+log s′)/d, and Minkowski over s converges. The resulting bound is V ≪ log³Q·(log log Q)^{O(1)}, which would give
  κ = 3/(16π²) ≈ 0.0190. Not written out in full; therefore not claimed.
* *Adding the pair fibration* (disjoint from the trial ones for p > Q²): κ → 9/(32π²) ≈ 0.0285. Here A_r is a sum over the
  2^{ω(d)} splittings d = d₁d₂, and the triangle inequality over splittings loses 4^{ω(d)} — fatal, since
  Σ_{d≤Q} 4^{ω(d)}/d ≍ log⁴Q. A proof must use that spikes of different splittings sit on different residue fibres. A fibre
  argument (functions of r mod d₂ vs r mod e₂ correlate only through r mod gcd(d₂,e₂)) gives a cross term ≪ L²·gcd/d², with
  total Σ_d L²∏_{ℓ|d}(1+3/ℓ)/d ≍ L³. We checked this heuristically, not rigorously. Numerics (§8) show V_pair/log³Q drifting
  slowly upward, so the honest status is EVIDENCE that V_pair = o(log⁴Q).
* *Level beyond 1/4.* The second moment needs lcm(m,m') ≤ X^{1/2−o(1)} for *all* pairs in the family, so Q ≤ X^{1/4}. Pairs with
  lcm > X^{1/2} have positive weighted proportion as soon as Q = X^{1/4+δ}. Brun–Titchmarsh there loses a factor ≥ 2, so
  Var = o(M²) fails by this method. BFI-type level > 1/2 needs a fixed residue, but our residues vary with the modulus.
  So (Assessment) within "BV + pair correlations" the almost-all constant is capped by the level-1/4 regions. Each fibration
  region {modulus ≤ X^{1/4}} is 1/16 of the log-simplex mass, so the reachable fraction is ≤ 3/16 of M₀ (κ ≤ 9/(32π²)). We prove
  2/16 of M₀ times the weight loss π²/12 (κ = 1/64).

**9.3 Concentration of R itself.** Theorem A is concentration of the *truncated* count. Concentration of R (R(p)/M₀(p) → 1 in
density) would need the variance of the untruncated count. That is the same as (ii) with the sharp constant. The repo's Z2461
evidence (E[R²]/E[R]² = 1.11 on primes ≡ 1 (4) to 10⁸, decaying like 1 + 2/log N) is consistent with it (EVIDENCE only).
Linnik's two-sided obstruction (FRONTIER §2.2: R(p) ≥ exp(c log p/log log p) infinitely often) concerns a density-zero set
in the *upper* tail and is compatible with both.

**9.4 What it says about B2 / hard primes.** Nothing pointwise (B6). Remark (ii) of §7 extends it to every fixed residue
class, including the Mordell-hard classes. The exceptional set ≪ π(X)/log X is far weaker than the ES exceptional-set bounds
(N exp(−c(log N)^{3/4})). Theorem A is a statement about the *size* of the cheap certificate count, not about ES itself.
## 10. Literature (research subagent, 2026-11-01; [V] = read in full text, [A] = abstract only)

* Elsholtz–Tao, arXiv:1107.1010v6 [V]. Thm 1.1: N log²N ≪ Σ_{p≤N} f_II(p) ≪ N log²N, and
  N log²N ≪ Σ_{p≤N} f(p) ≪ N log²N log log N. Upper bound on a density-1 set: f(p) = O_ε(log³p log log p) (Markov).
  **Thm 1.8:** f(p) ≫ (log p)^{0.549} for p in a subset of primes of relative density 1, via f(p) ≫ 3^{w₄(p+1)} or
  3^{w₃(p+3)} and Barban's normal-order lemma (their Lemma A.3). **Rem. 1.3:** higher moments of f_I(p), f_II(p) "seem …
  out of reach of our methods, as the level of the relevant divisor sums becomes too great to handle".
* Elsholtz–Planitzer, arXiv:1805.02945 (PRSE A 2020) [V]. Thm 3: f₃(4,n) ≥ exp((log 6 + o(1)) log log n) for a density-1 set of
  *integers*. For primes they cite ET's (log p)^{0.549}. Thm 4 concerns infinitely many primes, not a density.
* Jiang arXiv:2609.09204 (withdrawn), Pomerance–Weingartner arXiv:2511.16817 [A], Jia 2012, Rios arXiv:1302.0872 [A]: no
  almost-all lower bound for counts.
* An X post by @brianakaka (search snippet only: "A density-one lower bound for strict Erdős–Straus solution counts: For almost
  all primes, the number of strictly ordered Type-II solutions has a quantitative…") could not be opened, and no matching
  paper was found. **Possible independent claim; unverified.** Priority is therefore uncertain (Assessment).
* Variance-over-primes technique: Barban's Turán–Kubilius inequality for shifted primes (Elliott, *Probabilistic Number Theory
  II*, Thm 12.10, as quoted in ET Lemma A.3) is the closest classical analogue. Theorem A is a Turán–Kubilius statement for the
  non-additive "tied" divisor count Σ_u #{m | p+u : m ≡ −1 (4u)}, made possible by the one-cell structure.

## 11. FRONTIER §4 hard screens

1. **T1 (odd squares): PASS.** No statement about n = m² is made. The step false at odd squares is the BV equidistribution of
   n mod m over the units (Lemmas 3.1–3.2): squares occupy only the square classes, and indeed N(m²) = R(m²) = 0. The proof
   uses primality exactly there.
2. **8/131: PASS (vacuously).** A numerator-uniform version is a density-one statement and cannot be refuted by finitely many
   failures.
3. **Tied modulus: handled on average only.** The events m | p + u with m ≡ −1 (mod 4u) *are* the tied divisor events. The
   argument averages them over p and never forces one at a given p.
4. **Fixed p: FAIL (B6).** Theorem A says nothing about any prescribed p. The 14 known primes with R(p) = 0 are allowed
   exceptions.

## 12. Proposed FRONTIER text and bottom line

**Proposed FRONTIER §5.1 bullet:**
* *(z53, `Z53_PZ.md`; PROVED rel. Bombieri–Vinogradov, internal review.)* **R(p) ≥ (1/64 − ε)log²p for all but
  O_ε(π(X)/log X) primes p ≤ X**, hence f(p) ≥ f_II(p) ≫ log²p for almost all primes. This improves the literature's
  (log p)^{0.549} (Elsholtz–Tao Thm 1.8) to the true average order. The method is the variance of the trial-form count
  truncated at moduli ≤ X^{1/4}: pair correlations sit at level X^{1/2}, and each residue class mod d is one hyperbolic cell,
  so V ≪ log³Q against M² ≍ log⁴Q. Level 1/4 caps the constant at ≤ 9/(32π²) for this method. The full second moment
  Σ R(p)² (ET Rem. 1.3) remains open and is not needed. B6: nothing pointwise.

**Proposed FRONTIER §7 text (replacing/closing Z2362):**
* *Z2362 closed (z53, `Z53_PZ.md`):* positive proportion, and in fact density one, with κ = 1/64. Open follow-ups:
  (a) push κ to 9/(32π²) (unweighted trial count + pair fibration; the pair case needs a rigorous cross-splitting fibre
  lemma, EVIDENCE in §9.2); (b) concentration of R itself (R/M₀ → 1 in density), which needs the untruncated variance and is
  equivalent in difficulty to ET Rem. 1.3; (c) an exceptional set o(π(X)/log X), which needs V = o(log³Q) and is false for
  this family (V ≍ log³Q numerically).

**Bottom line.** Z2362 is answered in a stronger form. For almost all primes p, the count R(p) of (★) certificates, and hence
the number of Type II Erdős–Straus solutions, is at least (1/64 − ε)log²p, the same order as its mean. The exceptional set is
O(π(X)/log X). The proof is short and classical: truncate to the cheap moduli m = 4uC − 1 ≤ X^{1/4} with weights φ(m)/m, and
compute the variance over primes by Bombieri–Vinogradov at level X^{1/2}. The trial fibration makes each residue class one
hyperbolic lattice cell, so the variance is O(log³) against a squared mean of order log⁴. It is unconditional and internally
proved. It is not externally refereed, and a possible independent claim is unverified. It is purely an average statement:
it says nothing about any prescribed prime, and therefore nothing about B2.

## 13. Review log

*(pending: hostile reviewer subagent; cross-model review.)*
