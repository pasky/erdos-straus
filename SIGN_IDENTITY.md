# SIGN_IDENTITY — exact identities for the ES sign N₋(n) (task O205, wave Y-b)

Status: in progress (O205). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on CHI_FLIP.md (χ = −ε₂(Q_w)), CONSTRUCTIVE_ES.md (Eichler orders of level 2), MODEL_SPECIFIC.md Thm 3.1,
KUDLA_ES/DIFF_DEEP/LDP_DEEP ((J)13, (J)16–18), GROWING_IDENTITIES (J)10, EXACT_FORMULA (I)5, STRONG_APPROX_ES Thm 9.1.
Scripts `scripts/si_*`.

Notation (as CHI_FLIP). Word w = (t, u, v) ∈ ℤ³_{≥1}, K(w) = tuv − u − v = n odd; A = tu − 1, A* = tv − 1,
AA* = tn + 1; χ(w) = (−A/n); G_w = [[v, −1, 0], [−1, t, −1], [0, −1, u]], det n. X_n = all positive words.
N_±(n) = #{w ∈ X_n : χ(w) = ±1}, S(n) = N₊ − N₋. SQ₅ (CONJECTURE): N₋(n) > 0 ⟺ n odd non-square, n ≠ 105.
Fingerprints: N₋(m²) = 0; N₋(105) = 0; N₊(n) = 0 at 38 values n ≡ 3 (4) ≤ 10⁶ (15, 311, 455, 495, …).

## 0. Iteration log
(I1) Setup: enumerator `scripts/si_census.c` with several weightings (§1).
(I2) Barrier targeted: Thm 9.1's "finite Eisenstein combination". Tried: (a) linear relations with 48 classical columns incl.
Kronecker–Hurwitz sums (§3, no relation); (b) *all* holomorphic modular forms — killed by size (d₃-type averages), not by
T1 (Thm 2.2); (c) zero-set equivalence with a weight-3/2 eigenform (Waldspurger route, hook (3)) — killed because the
root-number mechanism vanishes on whole congruence classes (Prop 2.4). (d) Gross–Keating/Kudla (hook (1)): exact
dictionary in which **both** signs are |Diff| = 1 cycles, at the two bad fibres of X₀(2p) (§4).

## 1. Exact reformulations of the sign (PROVED, elementary)

**Lemma 1.1 ((u,v)-form).** For odd n, w ↦ (u, v) is a bijection X_n → {(u, v) ∈ ℤ²_{≥1} : uv | n + u + v}, with
t = (n + u + v)/(uv), A = (n + u)/v, A* = (n + v)/u. If gcd(uv, n) = 1 then **χ(w) = (−uv/n)**; so the sign of a word
depends only on m = uv, and
  N₋(n) = Σ_{m : (−m/n) = −1} c_m(n) (+ words with gcd(uv, n) > 1),  c_m(n) := #{u | m : m | n + u + m/u},
c_m(n) a function of n mod m. Every word has (u − 1)(v − 1) ≤ n + 1, hence **|X_n| ≤ 2 Σ_{u ≤ √(n+1)+1} d(n + u) ≪ n^{1/2+ε}**.
*Proof.* tuv − u − v = n ⟺ uv·t = n + u + v; Av = (tu − 1)v = n + u. With gcd(v, n) = 1, A ≡ u·v⁻¹ (mod n), so
(−A/n) = (−uv/n). For u ≤ v: v | n + u and u ≤ √(n+1) + 1. ∎ CHECKED (`scripts/si_uvform.py 1500`): all 35 184 words of odd
n ≤ 1500 (= census total), 31 968 with gcd(uv, n) = 1, 0 mismatches. (The non-residue −uv already appears in
CONSTRUCTIVE Prop 4.1(c) for primes; the point here is that χ is a function of the product uv.)
*Reading.* SQ₅(n) asks for a product m = uv, −m a non-residue mod n, with u + m/u ≡ −n (mod m) and the size condition
t ≥ 1. Each pair (u, v) is a Mordell-type identity covering the class n ≡ −(u + v) (mod uv) with a sign fixed by
(t, u, v) mod 8 (CHI_FLIP Cor 1.2): B1/B2 shape, nothing new — but the m-grading is what §2 uses.

**Lemma 1.2 (trivial certificates; PROVED).** N₋(n) ≥ 1 if n ≡ 3 (mod 4) (word (1, 2, n + 2), A = 1) or n ≡ 5 (mod 8)
(word (1, 3, (n + 3)/2), A = 2). For a prime p ≡ 1 (mod 4) and a prime q ≡ 3 (mod 4) with p ≡ −1 (mod q), the word
(1, q + 1, (p + 1)/q + 1) has A = q and χ = (q/p) = (p/q) = (−1/q) = −1. Hence (Dirichlet + CRT) **for every modulus M
and every class r mod M with gcd(r, M) = 1, r ≡ 1 (mod 4), there are infinitely many primes p ≡ r (M) with N₋(p) ≥ 1**
(take q ∤ M, q ≡ 3 (4), and p ≡ r (M), p ≡ −1 (q)). (Mordell/CHI_FLIP §3.1 in a Chebotarev-uniform form; also true
for p split completely in any fixed number field K, taking q unramified in K — Chebotarev in K(ζ_q).)

## 2. What kind of object can carry an exact identity? Size and T1 screens (PROVED unless labelled)

**Lemma 2.1 (averages).** Of the 512 cells (t, u, v) mod 8, 320 have K odd; χ = −1 on 240, χ = +1 on 80
(`scripts/si_cells.py`; CHI_FLIP Cor 1.2 makes χ a cell function). Hence, X → ∞,
  Σ_{n≤X odd} N₋(n) ~ (15/32)·X log²X/2,  Σ N₊ ~ (5/32)·X log²X/2,  Σ S ~ −(5/16)·X log²X/2,  Σ |X_n| ~ (5/8)·X log²X/2.
*Proof.* #{(t, u, v) ≡ c (mod 8) : tuv ≤ X} ~ X log²X/(2·512) (hyperbola method). Words with t ≤ 2 number O(X log X);
for t ≥ 3, tuv − u − v ≥ tuv/3, and the triples with X < tuv ≤ X + u + v number ≤ Σ_{uv ≤ 3X}((u + v)/(uv) + 1) = O(X log X). ∎
(Numerically the ratio ΣN₋/ΣN₊ is 2.40 at X = 10⁵, 2.50 at 10⁶, creeping to 3 with 1/log X corrections.)
So all four sequences have **d₃-size** (rank-3 divisor size), while (Lemma 1.1) |X_n| ≪ n^{1/2+ε}.

**Theorem 2.2 (no holomorphic modular generating function).** Let a ∈ {N₋, N₊, S, |X|}. There is no finite sum f of
holomorphic modular forms (weights k ∈ ½ℤ_{>0}, any congruence subgroup, any character/multiplier) whose n-th
coefficient equals a(n) for every odd n.
*Proof.* Replacing f by ½(f(z) − f(z + ½)) we may assume f is supported on odd n. By Lemma 2.1 and Abel summation,
F(y) := Σ_{n odd} |a(n)| e^{−2πny} ≍ y^{−1} log²(1/y), and |f(x + iy)| ≤ F(y); also Σ a(n) e^{−2πny} ≍ y^{−1}log²(1/y).
Write f = Σ_k (E_k + g_k) (Eisenstein + cusp part in weight k). (i) If some E_k ≠ 0 with k > 1, take the largest such k
and a cusp a/c where E_k has non-zero constant term; then |f(a/c + iy)| ≍ y^{−k} (slash by γ ∈ SL₂(ℤ), γ(∞) = a/c;
distinct weights give distinct powers of y; cusp parts and weights k′ < k are o(y^{−k})), contradicting ≤ F(y). (ii) So
all components of weight > 1 are cuspidal. If moreover all weights are ≤ 2, then |f(iy)| ≪ y^{−1} (weight ≤ 1 forms:
≪ y^{−k}; cusp forms of weight k: ≪ y^{−k/2}), contradicting Σ a(n)e^{−2πny} ≍ y^{−1}log²(1/y). (iii) If a cusp
component of weight K ≥ 5/2 is present (K maximal), Rankin–Selberg gives Σ_{n≤X}|a_{g_K}(n)|² ≍ X^K, hence
Σ_{n≤X}|a(n)|² ≫ X^K ≥ X^{5/2} (the lower-weight part has mean square O(X^{K−1/2}) once (i) is used); but
Σ_{n≤X}|a(n)|² ≤ max_{n≤X}|X_n|·Σ_{n≤X}|X_n| ≪ X^{3/2+ε} (Lemma 1.1). ∎
*Scope.* Covers every theta series of every lattice (positive definite or with harmonic polynomial), every Hecke
eigenform of any weight and level, Eisenstein series of every weight (Thm 9.1's class is the special case of weight-1
Eisenstein + exponent-0 divisor sums), and finite combinations of all of these. It does **not** cover: holomorphic parts
of harmonic Maass forms (mock forms; but Zagier's ℋ has y^{−3/2} growth and is excluded by the same size argument
once its completion is used — Assessment), derivatives in s of Eisenstein series, GL(3) objects, sums over unboundedly
many levels. The mechanism is **size, not T1**: X_n is a cubic surface with three free letters; every GL(2) object has
the wrong average (log¹ or a power). This is the first screen any identity must pass: *its natural home has d₃-size.*

**Proposition 2.3 (T1 kills finite divisor-rank combinations, any rank; extends STRONG_APPROX Thm 9.1).** Let
E(n) = Σ_{k≥0} Σ_i c_{k,i} d_k(n; ψ_{k,i,1}, …, ψ_{k,i,k}),  d_k(n; ψ₁..ψ_k) := Σ_{d₁⋯d_k = n} Π_j ψ_j(d_j)
(d₀ := 1, the constant function), a finite combination with Dirichlet characters of conductors dividing L. If
E(m²) = 0 for every odd m composed of primes ≡ 1 (mod L), then E(n) = 0 for **every** n composed of primes ≡ 1 (mod L).
In particular E ≠ N₋ (on such n), because N₋(p) ≥ 1 for infinitely many primes p ≡ 1 (mod lcm(4, L)) (Lemma 1.2).
*Proof.* On such n all character values are 1, so E(n) = Σ_k C_k d_k(n), C_k := Σ_i c_{k,i}. With m = ℓ^a:
0 = E(ℓ^{2a}) = C₀ + Σ_{k≥1} C_k·binom(2a + k − 1, k − 1) for all a ≥ 0 (a = 0: E(1) = N₋(1) = 0). The right side is a
polynomial in a in which the k-th term has degree k − 1 and leading coefficient 2^{k−1}/(k−1)!; so C_K = 0 for the largest
K ≥ 2, inductively C_k = 0 for k ≥ 2, and C₀ + C₁ = 0. Then E ≡ C₀ + C₁ = 0 on the semigroup. ∎
*Reading.* d₃-size objects (Thm 2.2's only survivors among divisor-type functions) are exactly the rank-3 terms, and
T1 at all squares couples the ranks completely (prime squares alone do **not**: 3 − d(n) is 1 at primes and 0 at ℓ²;
ℓ⁴, ℓ²ℓ′² are needed). A d₃-Eisenstein identity is GL(3)-Eisenstein; T1 kills it as in Thm 9.1.
