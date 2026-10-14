# SIGN_IDENTITY — exact identities for the ES sign N₋(n) (task O205, wave Y-b)

Status: checkpoint 1 (O205). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.

**Summary (checkpoint 1).** No exact positive identity for N₋ was found; the outcome is a sharpened map of where one
could live, plus one exact dictionary.
* *Size class (Thm 2.2, PROVED).* N₋, N₊, S, |X_n| have averages ~c·X log²X (Lemma 2.1), so **no finite sum of
  holomorphic modular forms of any weight (½ℤ_{>0}), level or character** has them as coefficients — theta series,
  Hecke eigenforms, holomorphic Eisenstein series all excluded, by size and independently of T1 (R205-self repair:
  holomorphic only; mock/non-holomorphic objects and arbitrary KH-type constructions are not covered).
* *T1 at all square shapes (Prop 2.3, PROVED).* Finite combinations of twisted k-fold divisor functions d_k (any rank k,
  i.e. GL(k)-Eisenstein type of exponent 0) vanishing at all odd squares vanish on the semigroup of primes ≡ 1 (mod L);
  with Lemma 1.2 (N₋(p) ≥ 1 for infinitely many p in every class ≡ 1 mod 4) they cannot equal N₋. Generalises
  Thm 9.1 along the rank axis (Thm 9.1 has divisor exponents; this has rank, exponent 0).
* *Waldspurger/Θ route (Prop 2.4, PROVED relative to Waldspurger; R205-self repair: scope restricted).* For a weight-3/2
  eigenform whose Shimura lift has **non-square** conductor, the zero set contains whole root-number classes of
  n ≡ 3 (4), where N₋ ≥ 1 is proved: no zero-set equivalence. Square conductors (e.g. 121) are not covered.
* *Dictionary (Prop 4.1, PROVED; moduli reading Assessment).* For n = p **every** word, of either sign, gives a pair of
  special endomorphisms with Gram T_w = t·diag(v,u) − [[1,−1],[−1,1]] and |Diff(T_w)| = 1: Diff = {p} (χ = −1, char p,
  Eichler level 2 in B_{p,∞}) or {2} (χ = +1, char 2, Eichler level p in B_{2,∞}) — the two bad fibres of X₀(2p). With
  the cycles Z(2p·T_w) on X₀(2p) (R204 repair: not Z(T_w); see §4) and Zhu's arithmetic Siegel–Weil formula, the family sum is N₋^μ log p + N₊^μ log 2 (CONDITIONAL): SQ₅(p) ⟺ the family sum is
  not in ℚ·log 2. The family, not the Eisenstein series, carries the lottery (moving level t, hyperbola extraction; B2).
* *Numerics (§3, CERTIFIED finite statement).* No linear relation with 48 classical columns (class numbers, KH sums,
  twisted divisor sums, ternary theta coefficients) for any of 8 weightings, n ≤ 12 000, per class mod 8 (exact
  rational rank on a row subset).
* *Small exact facts (Lemma 1.1).* X_n ≅ {(u,v) : uv | n + u + v}, and χ(w) = (−uv/n₀), n₀ := the part of n prime to uv
  (= (−uv/n) when gcd(uv, n) = 1): χ depends only on m = uv; |X_n| ≪ n^{1/2+ε}.
Builds on CHI_FLIP.md (χ = −ε₂(Q_w)), CONSTRUCTIVE_ES.md (Eichler orders of level 2), MODEL_SPECIFIC.md Thm 3.1,
KUDLA_ES/DIFF_DEEP/LDP_DEEP ((J)13, (J)16–18), GROWING_IDENTITIES (J)10, EXACT_FORMULA (I)5, STRONG_APPROX_ES Thm 9.1.
Scripts `scripts/si_*`.

Notation (as CHI_FLIP). Word w = (t, u, v) ∈ ℤ³_{≥1}, K(w) = tuv − u − v = n odd; A = tu − 1, A* = tv − 1,
AA* = tn + 1; χ(w) = (−A/n); G_w = [[v, −1, 0], [−1, t, −1], [0, −1, u]], det n. X_n = all positive words.
N_±(n) = #{w ∈ X_n : χ(w) = ±1}, S(n) = N₊ − N₋. SQ₅ (CONJECTURE): N₋(n) > 0 ⟺ n odd non-square, n ≠ 105.
Fingerprints: N₋(m²) = 0; N₋(105) = 0; N₊(n) = 0 at 38 values n ≡ 3 (4) ≤ 10⁶ (15, 311, 455, 495, …).

## 0. Iteration log
(I1) Setup: enumerator `scripts/si_census.c` with several weightings (§3).
(I2) Barrier targeted: Thm 9.1's "finite Eisenstein combination". Tried: (a) linear relations with 48 classical columns incl.
Kronecker–Hurwitz sums (§3, no relation); (b) *all* holomorphic modular forms — killed by size (d₃-type averages), not by
T1 (Thm 2.2); (c) zero-set equivalence with a weight-3/2 eigenform (Waldspurger route, hook (3)) — killed because the
root-number mechanism vanishes on whole congruence classes (Prop 2.4). (d) Gross–Keating/Kudla (hook (1)): exact
dictionary in which **both** signs are |Diff| = 1 cycles, at the two bad fibres of X₀(2p) (§4).

## 1. Exact reformulations of the sign (PROVED, elementary)

**Lemma 1.1 ((u,v)-form).** For odd n, w ↦ (u, v) is a bijection X_n → {(u, v) ∈ ℤ²_{≥1} : uv | n + u + v}, with
t = (n + u + v)/(uv), A = (n + u)/v, A* = (n + v)/u. Always **χ(w) = (−uv/n₀)**, n₀ := Π_{ℓ | n, ℓ ∤ uv} ℓ^{v_ℓ(n)}
(so χ = (−uv/n) when gcd(uv, n) = 1; R205-self repair: e.g. (1, 3, 9) ∈ X₁₅ has χ = −1 but (−27/15) = 0); so the sign of a
word depends only on m = uv, and N₋(n) = Σ_{m : (−m/n₀(m)) = −1} c_m(n), c_m(n) := #{u | m : m | n + u + m/u},
c_m(n) a function of n mod m. Every word has (u − 1)(v − 1) ≤ n + 1, hence **|X_n| ≤ 2 Σ_{u ≤ √(n+1)+1} d(n + u) ≪ n^{1/2+ε}**.
*Proof.* tuv − u − v = n ⟺ uv·t = n + u + v; Av = (tu − 1)v = n + u. With gcd(v, n) = 1, A ≡ u·v⁻¹ (mod n), so
(−A/n) = (−uv/n). In general, if ℓ | n and ℓ | u then ℓ | Av with ℓ ∤ A (AA* = tn + 1), so ℓ | v (and symmetrically);
then A = tu − 1 ≡ −1 (mod ℓ) and ℓ contributes (−A/ℓ)^{v_ℓ(n)} = 1, while for ℓ ∤ uv, A ≡ uv⁻¹ (mod ℓ). For u ≤ v:
v | n + u and u ≤ √(n+1) + 1. ∎ CHECKED (`scripts/si_uvform.py 1500`): all 35 184 words of odd n ≤ 1500 (= census
total), 31 968 with gcd(uv, n) = 1; both formulas and the prime-sharing claim, 0 mismatches. (The non-residue −uv already appears in
CONSTRUCTIVE Prop 4.1(c) for primes; the point here is that χ is a function of the product uv.)
*Reading.* SQ₅(n) asks for a product m = uv, −m a non-residue mod n, with u + m/u ≡ −n (mod m) and the size condition
t ≥ 1. Each pair (u, v) is a Mordell-type identity covering the class n ≡ −(u + v) (mod uv) with a sign fixed by
(t, u, v) mod 8 (CHI_FLIP Cor 1.2): B1/B2 shape, nothing new — but the m-grading is what §2 uses.

**Lemma 1.2 (trivial certificates; PROVED).** N₋(n) ≥ 1 if n ≡ 3 (mod 4) (word (1, 2, n + 2), A = 1) or n ≡ 5 (mod 8)
(word (1, 3, (n + 3)/2), A = 2). For a prime p ≡ 1 (mod 4) and a prime q ≡ 3 (mod 4) with p ≡ −1 (mod q), the word
(1, q + 1, (p + 1)/q + 1) has A = q and χ = (q/p) = (p/q) = (−1/q) = −1. Hence (Dirichlet + CRT) **for every modulus M
and every class r mod M with gcd(r, M) = 1, r ≡ 1 (mod 4), there are infinitely many primes p ≡ r (M) with N₋(p) ≥ 1**
(take q ∤ M, q ≡ 3 (4), and p ≡ r (M), p ≡ −1 (q), p ≡ 1 (4) imposed separately if 4 ∤ M). (Mordell/CHI_FLIP §3.1
in a Chebotarev-uniform form; also true for p split completely in any fixed number field K: let K′ be the Galois closure
of K(i) and q ≡ 3 (4) unramified in K′; then K′ ∩ ℚ(ζ_q) = ℚ (every subfield ≠ ℚ of ℚ(ζ_q) ramifies at q), so Chebotarev
in K′(ζ_q) gives p split in K′ with p ≡ −1 (q). No certificates beyond the Mordell mechanism.)

## 2. What kind of object can carry an exact identity? Size and T1 screens (PROVED unless labelled)

**Lemma 2.1 (averages).** Of the 512 cells (t, u, v) mod 8, 320 have K odd; χ = −1 on 240, χ = +1 on 80
(`scripts/si_cells.py`; CHI_FLIP Cor 1.2 makes χ a cell function). Hence, X → ∞,
  Σ_{n≤X odd} N₋(n) ~ (15/32)·X log²X/2,  Σ N₊ ~ (5/32)·X log²X/2,  Σ S ~ −(5/16)·X log²X/2,  Σ |X_n| ~ (5/8)·X log²X/2.
*Proof.* #{(t, u, v) ≡ c (mod 8) : tuv ≤ X} ~ X log²X/(2·512) (hyperbola method). Words with t ≤ 2 number O(X log X);
for t ≥ 3, tuv − u − v ≥ tuv/3, and the triples with X < tuv ≤ X + u + v number ≤ Σ_{uv ≤ 3X}((u + v)/(uv) + 1) = O(X log X). ∎
(Numerically the ratio ΣN₋/ΣN₊ is 2.40 at X = 10⁵, 2.50 at 10⁶, creeping to 3 with 1/log X corrections.)
So all four sequences have **d₃-size averages** (X log²X; R205-self repair: this does not identify "rank 3" — e.g.
1∗1∗1∗ψ has the same average), while (Lemma 1.1) |X_n| ≪ n^{1/2+ε}. (Triples with t ≤ 2 and K ≤ 0 are excluded from
both counts and are O(X log X) in number.)

**Theorem 2.2 (no holomorphic modular generating function).** Let a ∈ {N₋, N₊, S, |X|}. There is no finite sum f of
holomorphic modular forms (weights k ∈ ½ℤ_{>0}, any congruence subgroup, any character/multiplier) whose n-th
coefficient equals a(n) for every odd n.
*Proof.* Replacing f by ½(f(z) − f(z + ½)) we may assume f is supported on odd n (R204 repair: this presumes integral
exponents; for expansions in q^{(m+κ)/h} use instead the character average of the translates f(z + j/2), j mod 2h, which
keeps exactly the exponents ≡ 1 (mod 2) and is again a finite sum of holomorphic modular forms). By Lemma 2.1 and Abel summation,
F(y) := Σ_{n odd} |a(n)| e^{−2πny} ≍ y^{−1} log²(1/y), and |f(x + iy)| ≤ F(y); also Σ a(n) e^{−2πny} ≍ y^{−1}log²(1/y).
Write f = Σ_k (E_k + g_k) (Eisenstein + cusp part in weight k). (i) If some E_k ≠ 0 with k > 1, take the largest such k
and a cusp a/c where E_k has non-zero constant term; then |f(a/c + iy)| ≍ y^{−k} (slash by γ ∈ SL₂(ℤ), γ(∞) = a/c:
f(a/c + iy) = Σ_{k′} (i/(cy))^{k′}(b_{k′,γ} + O(e^{−c′/y})), so cusp components of any weight are exponentially small on
this ray — R204 repair: the generic bound y^{−K/2} would not suffice — and weights k′ < k are o(y^{−k})), contradicting ≤ F(y). (ii) So
all components of weight > 1 are cuspidal. If moreover all weights are ≤ 2, then |f(iy)| ≪ y^{−1} (weight ≤ 1 forms:
≪ y^{−k}; cusp forms of weight k: ≪ y^{−k/2}), contradicting Σ a(n)e^{−2πny} ≍ y^{−1}log²(1/y). (iii) If a cusp
component of weight K ≥ 5/2 is present (K maximal), Rankin–Selberg gives Σ_{n≤X}|a_{g_K}(n)|² ≍ X^K, hence
Σ_{n≤X}|a(n)|² ≫ X^K ≥ X^{5/2} (the lower-weight part has mean square O(X^{K−1/2}) once (i) is used); but
Σ_{n≤X}|a(n)|² ≤ max_{n≤X}|X_n|·Σ_{n≤X}|X_n| ≪ X^{3/2+ε} (Lemma 1.1). ∎
*Shorter proof (R205-self repair, suggested by the reviewer; uses only cusp 0).* For each component f_k of weight k,
f_k(iy) = (iy)^{−k}(f_k|S)(i/y) = b_k (iy)^{−k} + O(y^{−k}e^{−c/y}) (the expansion of f_k|S at ∞ has constant term b_k,
possibly 0, and otherwise exponentially decaying terms, also with a multiplier shift). So f(iy) = Σ_k b_k (iy)^{−k} +
O(y^{−K}e^{−c/y}): either ≍ y^{−k₀} for some k₀ or exponentially small, never ≍ y^{−1}log²(1/y) as Lemma 2.1 forces. ∎
*Scope.* Covers every theta series of every lattice (positive definite or with harmonic polynomial), every Hecke
eigenform of any weight and level, holomorphic Eisenstein series of every weight, and finite combinations of all of these (R204 repair: Thm 9.1's class
is *not* a sub-case — it contains d(n) and other parity-mismatched twisted σ_k, coefficients of non-holomorphic
Eisenstein series). It does **not** cover: holomorphic parts
of harmonic Maass forms (mock forms; but Zagier's ℋ has y^{−3/2} growth and is excluded by the same size argument
once its completion is used — Assessment), derivatives in s of Eisenstein series, GL(3) objects, sums over unboundedly
many levels. The mechanism is **size, not T1**: X_n is a cubic surface with three free letters; every holomorphic modular form has
the wrong average (a power of X, no logarithm; R204 repair: log¹ averages such as d(n) are non-holomorphic). This is the first screen any identity must pass: *its natural home has d₃-size.*

**Proposition 2.3 (T1 kills finite divisor-rank combinations, any rank; generalises STRONG_APPROX Thm 9.1 along the
rank axis — exponent 0, any rank — whereas Thm 9.1 allows divisor exponents).** Let
E(n) = Σ_{k≥0} Σ_i c_{k,i} d_k(n; ψ_{k,i,1}, …, ψ_{k,i,k}),  d_k(n; ψ₁..ψ_k) := Σ_{d₁⋯d_k = n} Π_j ψ_j(d_j)
(d₀ := 1, the constant function), a finite combination with Dirichlet characters of conductors dividing L. If
E(m²) = 0 for every odd m composed of primes ≡ 1 (mod L), then E(n) = 0 for **every** n composed of primes ≡ 1 (mod L).
In particular E ≠ N₋ (on such n), because N₋(p) ≥ 1 for infinitely many primes p ≡ 1 (mod lcm(4, L)) (Lemma 1.2).
*Proof.* On such n all character values are 1, so E(n) = Σ_k C_k d_k(n), C_k := Σ_i c_{k,i}. With m = ℓ^a:
0 = E(ℓ^{2a}) = C₀ + Σ_{k≥1} C_k·binom(2a + k − 1, k − 1) for all a ≥ 0 (a = 0: E(1) = 0 is the hypothesis at m = 1). The right side is a
polynomial in a in which the k-th term has degree k − 1 and leading coefficient 2^{k−1}/(k−1)!; so C_K = 0 for the largest
K ≥ 2, inductively C_k = 0 for k ≥ 2, and C₀ + C₁ = 0. Then E ≡ C₀ + C₁ = 0 on the semigroup. ∎
*Reading.* The d₃-size average needs terms of rank ≥ 3 (R205-self repair: not "exactly rank 3"), and
T1 at all squares couples the ranks completely (prime squares alone do **not**: 3 − d(n) is 1 at primes and 0 at ℓ²;
the even powers ℓ^{2a}, a ≤ K, of a single prime suffice — R204 repair: ℓ²ℓ′² is never used). Finite GL(k)-Eisenstein-type identities (exponent 0) die by T1 as in Thm 9.1; GL(3) cuspidal
contributions are not covered (their averages over ℓ^{2a} need Sym^{2a} information).

**Proposition 2.4 (hook (3): a Waldspurger/Θ zero-set equivalence fails for eigenforms whose lift has non-square
conductor; PROVED relative to Waldspurger 1981 and the root-number formula for quadratic twists; R205-self repair:
the first version claimed all eigenforms — false for square conductors, e.g. 121b1, where ε(F ⊗ χ_D) = −χ_D(−121) = +1
for every negative fundamental D prime to 11).** Thm 2.2 excludes equality; the softer hope is "N₋(n) > 0 ⟺ a_g(n) ≠ 0"
for a weight-3/2 eigenform g (T1 would be a(1) = 0 propagated by a(m²) = a(1)·(multiplicative in m)). Let g be a
weight-3/2 Hecke eigenform (cuspidal, non-unary) **with trivial character** on Γ₀(4M) (R204 repair: with a nebentypus ψ,
ψ² ≠ 1, there is no self-dual root-number vanishing, and for quadratic ψ the twist is ψχ_{−n}; not covered) with Shimura lift F of weight 2 and conductor N, and suppose **N is not
a square**. For squarefree n ≡ 3 (mod 4) with gcd(n, N) = 1, D := −n is a negative fundamental discriminant prime to N,
and Waldspurger gives a(n)² = c(n)·L(F ⊗ χ_D, 1), c(n) depending only on the classes of n in ℚ_v^*/ℚ_v^{*2}, v | 4N∞
(R204 repair: this is the Cor. 2 / ε-dichotomy form — Waldspurger 1981 Thm 1 + Cor. 2, or the explicit Baruch–Mao formula;
the ratio form of Thm 1 alone is vacuous on a class where all central values vanish, which is the class Z used below).
Here ε(F ⊗ χ_D) = ε(F)·χ_D(−N) = −ε(F)·(D/N) (Kronecker), and D ↦ (D/N) is non-constant on {D ≡ 1 (4), gcd(D, N) = 1}
because N is not a square (odd part non-square: CRT mod the odd part; odd part square, 2-part 2^odd: (D/2) separates
D ≡ 1, 5 (8)). So there is an invertible class Z mod 4N, inside n ≡ 3 (4), on which ε(F ⊗ χ_{−n}) = −1 and hence
a(n) = 0 for all squarefree n ∈ Z prime to N; but N₋(n) ≥ 1 for **every** n ≡ 3 (4) (Lemma 1.2, PROVED). Hence
{a_g = 0} ≠ {N₋ = 0}. ∎ (The comparison uses only proved certificates, not SQ₅.)
*Reading.* Both T1 and root-number vanishing are Hilbert reciprocity; but a twist family's reciprocity sign is a
**character of n** (vanishes on whole classes), whereas ES's T1 is the **square condition on n** itself; the *conjectured*
ES zero set (SQ₅) is {squares} ∪ {105}, and the proved part (n ≡ 3 mod 4 never in it) already rules out whole-class
zeros. (Kohnen's plus space is even easier: a(n) = 0 for all n ≡ 1, 2 (mod 4) while N₋(n) ≥ 1 for n ≡ 5 (8).)
*Not covered:* square conductors (twist signs constant on fixed-sign D), unary theta / non-cuspidal forms, and linear
combinations of eigenforms (no zero-set control).

## 3. Numerical identity screen (CERTIFIED finite statement; `scripts/si_census.c`, `scripts/si_fit.py`)

Census (`si_census N`, cross-checked against CHI_FLIP's `cf_census.c` for all odd n ≤ 10⁵, 0 differences): per odd n,
N₊, N₋, interior N₊/N₋, Σt over each sign. Fingerprints reproduced: N₋(105) = 0 (|X₁₀₅| = 11), N₋(m²) = 0, N₊(15) =
N₊(311) = 0.
**Linear-relation test.** Targets N₊, N₋, S, |X|, interior N_±, t-weighted N_± on odd n ≤ 12 000, separately in each
class n mod 8 (≈ 1500 rows, exact rational rank (Fractions) of [columns] vs [columns | target] on the first 120 rows of the class — a relation on
all rows restricts to these rows, so a rank increase certifies non-membership; R205-self repair: the earlier mod-(2⁶¹ − 1)
rank alone is not a certificate, a ℚ-relation need not survive reduction; rational ranks of the columns 37, 32, 32, 34
equal the mod-P ranks on all rows). Dictionary (48 columns): 1, n; 12H(kn) for
k ∈ {1, 3, 4, 8, 12, 16, 24}; Kronecker–Hurwitz sums Σ_s H(kn − js²) for (k, j) ∈ {(1,1), (4,1), (8,1), (4,2), (8,2),
(4,8), (16,1), (3,1), (12,1)} and the alternating (4,1), (8,1); σ₀, σ₁ twisted by (D/·), D ∈ {1, −4, ±8, −3, 12, 5, −7};
Σ_{d|n} min(d, n/d); τ(n + 1), τ(n + 2), τ(n + 3), τ(2n + 1); r_Q(n) for Q = ⟨1,1,1⟩, ⟨1,1,2⟩, ⟨1,2,2⟩, ⟨1,1,3⟩,
⟨1,2,3⟩, ⟨1,3,5⟩; [n = □]. **Result: no target lies in the ℚ-span in any class (all 32 cases certified)** (relative least-squares residual
0.09–0.69; best: N₋ and S for n ≡ 7 (8), residual 0.11/0.14, i.e. a correlation with H(n) through L(1, χ₋ₙ), not an identity).
Scope: this dictionary and range only; it complements EXACT_FORMULA (I)5 (Type I/II counts, 54 columns) with the X_n
sign counts. Thm 2.2 explains the outcome for the modular part of the dictionary (wrong size class); the τ(n + s)
columns are shifted d₂-objects, still of size log¹.

## 4. Hook (1): the Gross–Keating/Kudla dictionary — both signs are |Diff| = 1 cycles, at the two bad fibres of X₀(2p)

**Proposition 4.1 (PROVED, from CHI_FLIP Thm 1.1 and CONSTRUCTIVE Thm 1.2/Prop 4.1).** For a word w ∈ X_n let
i = 1 + e₁e₂, j = 1 + e₂e₃ ∈ C₀(L_w) (trace zero, i² = −A*, j² = −A, ij + ji = −2) and T_w := [[A*, 1], [1, A]] their
Gram matrix (Q = nrd). Then
(a) **T_w = t·diag(v, u) − R, R := [[1, −1], [−1, 1]], det T_w = tn**, and for fixed n, w ↦ T_w is injective (t = det T_w/n, then u, v);
(b) ℚ⟨i, j⟩ = C₀(L_w) ⊗ ℚ ≅ (−A*, −tnA*), and its finite ramification set (Kudla's Diff(T_w) for the incoherent
collection ramified only at ∞) is **Diff(T_w) = {2 : χ(w) = +1} ∪ {ℓ | n : (−A/ℓ)^{v_ℓ(n)} = −1}**, of odd size;
(c) for n = p prime: |Diff(T_w)| = 1 for **every** word: Diff = {p} ⟺ χ = −1 (i, j ∈ Eichler order of level 2 in B_{p,∞},
i.e. a 2-isogeny of supersingular curves in characteristic p) and Diff = {2} ⟺ χ = +1 (i, j ∈ Eichler order of level p
in B_{2,∞}, i.e. a supersingular curve in characteristic 2 with a cyclic p-subgroup);
(d) at n = m² (odd): Diff(T_w) = {2} for every word (T1).
CHECKED (`scripts/si_diff.py 2000`): Hilbert-symbol ramification of (−A*, −tnA*) equals the formula in (b), with odd size,
on all 50 003 words of odd n ≤ 2000, 0 mismatches. (R204: = 3 ≤ n ≤ 2000; reproduced from scratch on all 50 008 words
incl. n = 1, `scripts/review_si_lemmas.py`. Attribution: (b) is CHI_FLIP Thm 1.1 in Clifford language, (c) is
CONSTRUCTIVE Thm 1.2(c), KUDLA_ES Thms 1.2/1.4 give Diff = {p} at certificate indices; new here are T_w = tD − R and the
uniform packaging.)
*Moduli reading (Assessment; standard Deligne–Rapoport/Ribet).* The supersingular points of X₀(2)_{𝔽_p} are the singular
points of the special fibre X₀(2p)_{𝔽_p}; those of X₀(p)_{𝔽₂} are the singular points of X₀(2p)_{𝔽₂}. So the words of X_p
are path-shaped pairs of special endomorphisms at the singular points of the **two bad fibres of one arithmetic surface
X₀(2p)/ℤ**, and χ records **which residue characteristic** carries the cycle Z(T_w): p (certificate) or 2 (non-certificate).
*Log-separation (CONDITIONAL on an arithmetic Siegel–Weil formula of the KRY / Du–Yang / Sankaran–Shi–Yang shape on
X₀(2p), i.e. ĉ(T) = Σ_ℓ μ_ℓ(T) log ℓ with μ_ℓ(T) ∈ ℚ_{>0} iff Diff(T) = {ℓ} and Z(T) ≠ ∅ — not verified for the bad
fibres here).* Σ_{w ∈ X_p} ĉ(T_w) = N₋^μ(p)·log p + N₊^μ(p)·log 2, so by ℚ-independence of log 2, log p,
**ES-five(p) ⟺ the family sum Σ_{w∈X_p} ĉ(T_w) ∉ ℚ·log 2**; at odd squares the family sum is a rational multiple of log 2.
This is an exact "transcendence-separated" form of SQ₅.
*(R204 repair — normalization, citation, label.)* In the standard X₀(N) normalization (Zhu, arXiv 2304.10696, lattice
∆(N) = {[[−Na, b], [c, a]]}, Q = det; cycles Z(T, ϕ) = pairs x₁, x₂ ∈ Hom(E, E′) ⊥ π) one has ∆(N) ⊗ ℚ_ℓ ≅ N·(M₂^{tr=0}, det),
so Diff(T, ∆(N)) = Ram(algebra of T/N). The cycle meant above is therefore **Z(2p·T_w)** (data (πi, πj)), for which
Diff = Ram(T_w) as in (b); with T_w itself Diff(T_w, ∆(2p)) ≠ Ram(T_w) on 1604 of 2958 words of primes p < 400
(`scripts/review_si_scale.py`). Sankaran–Shi–Yang treat only odd squarefree N > 3 and do not cover X₀(2p); Zhu's
Thm 1.2.1 (arbitrary N; preprint, not re-checked here) does. For positive definite T with Diff(T) = {ℓ} the arithmetic
degree of Ẑ(T) is already (rational ≥ 0)·log ℓ, > 0 iff Z(T) ≠ ∅, by geometry alone (0-cycle in the supersingular
locus at ℓ); Siegel–Weil only identifies it with an Eisenstein-derivative coefficient. So the decomposition with
ĉ(2pT_w) needs no Siegel–Weil input beyond the moduli reading (Assessment), the Eisenstein form is CONDITIONAL on Zhu's
theorem, and the "⟺" is a tautological reformulation of Prop 4.1(c) (N₋(p) > 0 ⟺ some term carries log p), not new
information.
*Why it does not open the door (barrier screen).* (i) The family F_p = {tD − R : D = diag(v,u) ≥ 1, det = tp} is, for
fixed t, a Fourier projection at level t (T₁₂ = 1, T_ii ≡ −1 mod t) followed by a **hyperbola restriction**
(T₁₁T₂₂ = tp + 1); for fixed p, t ≤ p + 2, but across p the levels are unbounded — a level-t projection per t plus a
non-linear extraction (B2; GROWING_IDENTITIES §3). No modular evaluation of the family sum is established here (R205-self
repair: earlier "exists" overclaimed; no pullback/Fourier–Jacobi identity known to us sees det T). (ii) Each ĉ(T)
depends on T only through local data (that is the content of any Siegel–Weil formula): the family sum is
Σ_t Σ_{a | tp+1, a ≡ −1 (t)} (local weight) — the divisor-in-class count again. (iii) Geometric counts of Z(T) over all
curves are genus data (DIFF_DEEP: "∃ curve" is vacuous). So the dictionary converts SQ₅ into a statement about a
non-modular family of coefficients of a modular object; the family, not the object, carries the lottery.
*Same with GK genus 3 (Assessment).* For p prime, χ(w) = −1 ⟺ the ternary G_w (det p) has C₀(G_w) ≅ B_{p,∞}; this is
Gross–Keating's Diff(G_w) = {p} for T_v·T_t·T_u on X(1)×X(1) (diagonal of G_w = (v, t, u)). GK's triple intersection
sums over **all** off-diagonals; the path shape (−1, 0, −1) with det = p is again a non-linear extraction.

## 5. Repair log (self-review R205-self, deep reviewer via `review`; all findings accepted)
* FATAL Prop 2.4 (square-conductor counterexample 121b1): restricted to non-square conductor, n ≡ 3 (4) argument; no
  longer uses the conjectural zero set.
* MAJOR: "zero set {squares, 105}" stated as fact → marked conjectural (SQ₅); χ = (−uv/n) unconditional was false
  ((1,3,9) ∈ X₁₅) → universal form χ = (−uv/n₀), checked; si_fit mod-P rank was not a certificate → exact rational ranks
  on row subsets added (all 32 cases certified; reviewer independently confirmed on 100 rows); §4 "no modular evaluation
  exists" → "none established"; t ≤ p + 2 for fixed p; scope of Thm 2.2 limited to holomorphic forms and "rank 3" claims
  removed (1∗1∗1∗ψ has the same average).
* MINOR: Lemma 1.2 (p ≡ 1 (4) imposed; Galois-closure disjointness spelled out); Lemma 2.1 (K ≤ 0 triples); shorter proof
  of Thm 2.2 at cusp 0; Prop 2.3's E(1) = 0 from hypothesis and its relation to Thm 9.1 qualified; Prop 4.1 injectivity
  for fixed n.
