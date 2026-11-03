# Z55_TDF — TRYHARD lane TDF: Problem TD (power saving for the strip sums T(h))

ES is OPEN. Nothing here proves or disproves it. Problem TD concerns an **upper bound** (hypothesis TD(η) of
`Z54_BILINDIV.md` §4.1, which by its Corollary T gives a power saving for the balanced block count N(U, U) = 2N₄).
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / Assessment. Brief: `z52bbriefs/z55_tryhard.md`, Problem TD.
Scripts `scripts/z55_tdf_*`, data `data/z55/tdf/`.

**Verdict: TD(η) is NOT proved, for any η > 0.** What is proved is the *n-averaged* form: the mean square of
T_n(h) over any interval of integers n of length ≥ 16U⁴ is ≪ (h⁴ + log U)·U, i.e. square-root size on average
(Theorem LS, §2). Consequently TD(η) with C₀ = 1 holds for all primes p in the fourth-root range outside a set of
size O(U^{3+7η} log U) — for every η < 1/7 this is o(π(U⁴)) (Corollary 2.4). The averaged statement is *not* a
better bound for N₂ on average (Markov on the first moment is better, §2.5); its content is about T itself.
The pointwise statement sits at the self-dual point of the Dirichlet divisor problem (divisors d ≍ √x of integers in an
interval of length x^{1/4}), where not even the lattice-point count |E1| has a provable asymptotic (§3, Assessment).

## 0. Notation and the object

* p an odd prime, U ≥ 2 an integer with 16U³ ≤ p; the fourth-root range is c₁p^{1/4} ≤ U ≤ c₂p^{1/4}.
* For an arbitrary integer n (not only primes) put

  c_h(m, s) := 1[U² < m ≤ 4U², 2U < s ≤ 4U, s² − 4m ≥ 1] · e(h√(s² − 4m)),

  T_n(h) := Σ_{m} Σ_{s ≡ −n (mod m)} c_h(m, s)   (sum over all integers m, s; the support of c_h cuts it to U² < m ≤ 4U²,
  2U < s ≤ 4U).

  Since m > U² ≥ 2U, for each m at most one s ∈ (2U, 4U] has s ≡ −n (mod m). For U ≥ 5 one has m > U² > 4U, so that s
  is the least nonnegative residue s_m := (−n) mod m, and T_n(h) = Σ_{U²<m≤4U²} 1[s_m ∈ (2U, 4U], s_m² − 4m ≥ 1]
  e(h√(s_m² − 4m)); the scripts use this form (all runs have U ≥ 6). For U ≤ 4 only the congruence form is meant.
* **Lemma 0.1 (PROVED).** For n = p prime, T_p(h) equals the strip sum T(h) of the brief, i.e. the sum over lattice
  points (k, m) ∈ ℤ² with p + 2U < km ≤ p + 4U, U² < m ≤ 4U², (km − p)² − 4m ≥ 1 of e(h√((km − p)² − 4m)).
  *Proof.* Given m ∈ (U², 4U²], the integers k with km ∈ (p + 2U, p + 4U] correspond bijectively (k ↦ s := km − p) to
  the integers s ∈ (2U, 4U] with s ≡ −p (mod m); there is at most one since m > 2U. The discriminant
  (km − p)² − 4m = s² − 4m and the phase agree term by term. ∎
  Primality is not used; the same identification holds for every integer n ≥ 1.
* **Hypothesis TD(η)** (Z54 §4.1): there is C₀ with |T_p(h)| ≤ C₀U^{1−η} for all 1 ≤ h ≤ U^{η}, uniformly for primes p
  and U in the fourth-root range.
* Sizes: |E1⁺| := T_n(0) ≈ 1.5U (EVIDENCE, §4, for n ≍ U⁴). In the fourth-root range |E1⁺| ≤ |E1| ≤ Σ_{s} τ(n + s)
  ≪ U^{1+ε} (Z54 Cor T); this is not uniform in arbitrary n (e.g. n = lcm(1, …, 4U²) − 4U gives T_n(0) = 3U² − 1).

## 1. What was attacked

1. **Pointwise, via the Farey/Poisson dual** (§2.1 identity, used pointwise). Stops: the dual has ≍ hU² relevant
   terms per level and is self-dual (§3.1).
2. **Pointwise, via exponent pairs after the θ-expansion** (Z54 §4.3 style). Stops: no exponent pair, including the
   conjectural limit (0, 1/2), reaches p ≥ 16U³ (§3.2, Assessment with a PROVED bookkeeping identity).
3. **Pointwise, via the h-mean square / pair correlation of w_k mod 1.** Stops: needs an upper bound for the clustering
   of √D_k mod 1 at scale U^{−η}, which is the same lattice-point problem in thin curvilinear regions (§3.3).
4. **n-averaged, via the large sieve.** Succeeds: Theorem LS (§2). This is the proved content of the lane.

## 2. Theorem LS: the mean square over n (PROVED)

### 2.1 Farey expansion

**Lemma 2.1 (PROVED).** For every integer n,

  T_n(h) = Σ_{d ≤ 4U²} Σ*_{b mod d} e(nb/d) Γ(b/d),   Γ(b/d) := Σ_{m ≡ 0 (mod d)} (1/m) Σ_s c_h(m, s) e(sb/d),

where Σ* runs over b with gcd(b, d) = 1, and the m-sum is over U² < m ≤ 4U².
*Proof.* 1[n ≡ −s (mod m)] = (1/m) Σ_{b mod m} e(b(n + s)/m). As b runs over the residues mod m, the fraction b/m mod 1
runs exactly once over each reduced fraction b′/d with d | m (d = m/gcd(b, m)). Substituting and collecting the terms
with a given reduced fraction b′/d gives the claim. ∎

*Numerical check (floating point, EVIDENCE; (U, h) ∈ {(6,1), (10,1), (10,3)}):* `scripts/z55_tdf_farey_check.py`
evaluates both sides at four values of n; max discrepancy 2.1·10⁻¹⁰ (`data/z55/tdf/farey_check.txt`).

**Lemma 2.2 (PROVED).** For each d, with A_{d,r} := Σ_{m ≡ 0 (d)} (1/m) Σ_{s ≡ r (mod d)} c_h(m, s),

  Σ*_{b mod d} |Γ(b/d)|² ≤ Σ_{b mod d} |Γ(b/d)|² = d · Σ_{r mod d} |A_{d,r}|².

*Proof.* Γ(b/d) = Σ_{r mod d} e(rb/d) A_{d,r}; Parseval on ℤ/dℤ. ∎

### 2.2 Bounds for A_{d,r}

Throughout, ν_{d,r} := #{s ∈ (2U, 4U] : s ≡ r (mod d)} ≤ 2U/d + 1, and the number of multiples of d in (U², 4U²] is
≤ 3U²/d + 1; each 1/m is < 1/U².

**Lemma 2.3 (trivial bound; PROVED).** |A_{d,r}| ≤ 4ν_{d,r}/d. In particular, for 2U < d ≤ 4U²: ν_{d,r} ≤ 1, at most 2U
residues r have ν_{d,r} = 1, and |A_{d,r}| ≤ 4/d; for U < d ≤ 2U: ν_{d,r} ≤ 2 and Σ_r ν_{d,r} = 2U.
*Proof.* The number of multiples of d in (U², 4U²] is ≤ 4U²/d and each 1/m < 1/U², so Σ_{m ≡ 0 (d)} 1/m ≤ 4/d; then
the triangle inequality. For d > 2U an interval of length 2U contains at most one element of each residue class; for
d > U at most two. ∎

**Lemma 2.4 (Kusmin–Landau bound for small d; PROVED).** For every d ≥ 1 and every s ∈ (2U, 4U],

  | Σ_{m ≡ 0 (mod d)} (1/m) c_h(m, s) | ≤ (4h²d + 1)/U² + 4/(hdU).

*Proof.* Write m = dt. The integers t with dt ∈ (U², 4U²] and s² − 4dt ≥ 1 form an interval 𝓘 (both are one-sided
conditions on t). Split 𝓘 = 𝓘₁ ∪ 𝓘₂, 𝓘₁ := {t ∈ 𝓘 : s² − 4dt < 16h²d²}, 𝓘₂ := {t ∈ 𝓘 : s² − 4dt ≥ 16h²d²}; both are
intervals of integers.
* *Edge part 𝓘₁.* Its length is ≤ (16h²d² − 1)/(4d) + 1 ≤ 4h²d + 1, and each term has modulus 1/m < 1/U².
* *Kusmin–Landau part 𝓘₂.* On the real hull of 𝓘₂ put φ(t) := h√(s² − 4dt); it is smooth there since
  s² − 4dt ≥ 16h²d² > 0 holds at the largest t of 𝓘₂, hence throughout. φ′(t) = −2hd/√(s² − 4dt) is negative and
  monotone (|φ′| increases with t). Bounds: |φ′| ≤ 2hd/(4hd) = 1/2 and |φ′| ≥ 2hd/s ≥ 2hd/(4U) = hd/(2U) =: λ.
  If hd > U then λ > 1/2 contradicts |φ′| ≤ 1/2, so 𝓘₂ = ∅ and there is nothing to prove. Otherwise 0 < λ ≤ 1/2 and
  λ ≤ |φ′(t)| ≤ 1/2 on the hull, i.e. φ′ ∈ [−1 + λ, −λ], so Lemma 2.4′ below (with j = −1) gives, for every
  sub-interval 𝓙 ⊂ 𝓘₂ of integers, |Σ_{t ∈ 𝓙} e(φ(t))| ≤ 2/λ.
  Abel summation with the positive decreasing weights 1/(dt): |Σ_{t ∈ 𝓘₂} (1/(dt)) e(φ(t))| ≤ (max weight) ·
  max_{𝓙} |Σ_{𝓙} e(φ)| ≤ (1/U²) · 2/λ = (1/U²) · 4U/(hd) = 4/(hdU).
Adding the two parts gives the claim. ∎

**Lemma 2.4′ (Kusmin–Landau with explicit constant; PROVED).** Let f be continuously differentiable on [a, b] with f′
monotone and f′(x) ∈ [j + λ, j + 1 − λ] for some integer j and some 0 < λ ≤ 1/2, for all x ∈ [a, b]. Then
|Σ_{a ≤ t ≤ b, t ∈ ℤ} e(f(t))| ≤ 2cot(πλ) + 2 ≤ 2/λ.
*Proof.* (Standard; Montgomery, *Ten lectures*, Ch. 3, with the constant tracked.) If [a, b] contains no integer the
sum is empty. Otherwise let the integers in [a, b] be t₀ < t₁ < … < t_R (if R = 0 the sum has one term and 1 ≤ 2/λ). Put θ_r := f(t_{r+1}) − f(t_r) = f′(ξ_r) with
ξ_r ∈ (t_r, t_{r+1}); the ξ_r increase with r, so (θ_r) is monotone and θ_r ∈ [j + λ, j + 1 − λ]. Since
e(f(t_{r+1})) − e(f(t_r)) = e(f(t_r))(e(θ_r) − 1) and e(θ_r) ≠ 1, with u_r := 1/(e(θ_r) − 1) = −1/2 − (i/2)cot(πθ_r)
we get Σ_{r=0}^{R−1} e(f(t_r)) = Σ_{r=0}^{R−1} [e(f(t_{r+1})) − e(f(t_r))] u_r = Σ_{r=1}^{R−1} e(f(t_r))(u_{r−1} − u_r)
+ e(f(t_R))u_{R−1} − e(f(t₀))u₀ (Abel). Now |u_{r−1} − u_r| = (1/2)|cot πθ_{r−1} − cot πθ_r|, and cot(πθ_r) is monotone
in r with values in [cot(π(1 − λ)), cot(πλ)] = [−cot πλ, cot πλ], so Σ_r |u_{r−1} − u_r| ≤ cot(πλ); also
|u_r| ≤ 1/2 + (1/2)cot(πλ). Adding the last term e(f(t_R)) of modulus 1:
|Σ_{r=0}^{R} e(f(t_r))| ≤ cot(πλ) + 2(1/2 + cot(πλ)/2) + 1 = 2cot(πλ) + 2 ≤ 2/(πλ) + 2 ≤ 2/λ, the last step because
λ ≤ 1/2 ≤ 1 − 1/π. ∎

### 2.3 The Farey mass 𝒢

**Lemma 2.5 (PROVED).** 𝒢 := Σ_{d ≤ 4U²} Σ*_{b mod d} |Γ(b/d)|² ≤ 2700 h⁴ U + 32 U log(2U)   (U ≥ 2, h ≥ 1).
*Proof.* By Lemma 2.2, 𝒢 ≤ Σ_d d Σ_r |A_{d,r}|².
* *d > 2U.* By Lemma 2.3, at most 2U residues contribute, each with |A_{d,r}| ≤ 4/d, so the d-term is
  ≤ d · 2U · 16/d² = 32U/d, and Σ_{2U < d ≤ 4U²} 32U/d ≤ 32U log(4U²/(2U)) = 32U log(2U).
* *U < d ≤ 2U.* By Lemma 2.3, |A_{d,r}|² ≤ 16ν_{d,r}²/d² ≤ 32ν_{d,r}/d² (as ν ≤ 2), so the d-term is
  ≤ d · (32/d²) Σ_r ν_{d,r} = 64U/d, and Σ_{U < d ≤ 2U} 64U/d ≤ 64U log 2 < 45U.
* *d ≤ U.* Here ν_{d,r} ≤ 2U/d + 1 ≤ 3U/d, and by Lemma 2.4 (applied to each of the ν_{d,r} values of s)
  |A_{d,r}| ≤ (3U/d)((4h²d + 1)/U² + 4/(hdU)) = 12h²/U + 3/(dU) + 12/(hd²).
  Using (x + y + z)² ≤ 3(x² + y² + z²), the d-term is ≤ d · d · 3(144h⁴/U² + 9/(d²U²) + 144/(h²d⁴))
  = 432h⁴d²/U² + 27/U² + 432/(h²d²). Summing over d ≤ U: Σ_{d ≤ U} d² ≤ (U + 1)³/3 ≤ 1.125U³ for U ≥ 2, so the
  first part is ≤ 486h⁴U; the second is ≤ 27/U ≤ 14; the third is ≤ 432π²/6 < 711.
Total ≤ 486h⁴U + 725 + 45U + 32U log(2U) ≤ 2700h⁴U + 32U log(2U) for U ≥ 2, h ≥ 1 (725 + 45U ≤ 2214h⁴U). ∎

*Remark (what 𝒢 is; PROVED identity, EVIDENCE sizes).* T_n(h) is periodic in n with period L = lcm(1, …, 4U²), and
by orthogonality of the distinct reduced fractions, (1/L)Σ_{n mod L} |T_n(h)|² = 𝒢 exactly. So 𝒢 is the true mean
square of T over a full period. Numerically 𝒢 is close to the mean of |E1⁺| over the sampled windows (U = 6: 𝒢 = 9.41
vs 9.77; U = 10: 15.84 vs 16.03), and the denominators d ≤ 2U carry 7–9 % of 𝒢 in these examples. The h⁴ in Lemma
2.5 is an artefact of the crude edge-part bound; it is harmless for the corollaries (h ≤ U^{η} with η small).

### 2.4 The theorem and its corollaries

**Theorem LS (PROVED).** For all integers M, N ≥ 1, U ≥ 2, h ≥ 1,

  Σ_{M < n ≤ M+N} |T_n(h)|² ≤ (N + 16U⁴) · 𝒢 ≤ (N + 16U⁴)(2700 h⁴ U + 32 U log(2U)).

*Proof.* By Lemma 2.1, T_n(h) = Σ_ρ Γ(ρ) e(nρ) over the reduced fractions ρ = b/d with d ≤ Q := 4U². These are
distinct mod 1 and pairwise at distance ≥ 1/Q² (|b/d − b′/d′| ≥ 1/(dd′)). The large sieve inequality in its dual form
(Montgomery–Vaughan; Selberg: for δ-spaced points x_ρ, Σ_{M<n≤M+N} |Σ_ρ c_ρ e(nx_ρ)|² ≤ (N + δ^{−1} − 1) Σ_ρ |c_ρ|²,
which is the adjoint of the usual form and has the same norm) with δ = 1/Q² gives the first inequality; Lemma 2.5 the
second. ∎

*Numerical check (floating point, EVIDENCE; `data/z55/tdf/farey_check.txt`):* with M = U⁴, N = 2000–3000 the ratio
LHS/((N + 16U⁴)𝒢) is 0.13 (U = 6) and 0.012 (U = 10) — consistent, and mean_n |T_n|² is close to 𝒢 already on these
short windows (where the large sieve gives nothing), EVIDENCE that the n-average is of square-root size at every scale.

**Corollary 2.2 (exceptional set; PROVED).** Let 0 < η ≤ 1/2, H ≥ 1. Then

  #{n ∈ (M, M+N] : max_{1≤h≤H} |T_n(h)| > U^{1−η}} ≤ (N + 16U⁴) · U^{2η−1} · (2700 H⁵ + 32 H log(2U)).

*Proof.* Chebyshev: the count is ≤ U^{2η−2} Σ_{h≤H} Σ_n |T_n(h)|², and Σ_{h≤H} h⁴ ≤ H⁵. ∎

**Corollary 2.3 (almost all n in the fourth-root range; PROVED).** Fix 0 < η < 1/7 and 0 < c₁ < c₂. For all integers
n ∈ [U⁴/c₂⁴, U⁴/c₁⁴] outside an exceptional set of size ≪_{c₁} U^{3+7η} log U, one has |T_n(h)| ≤ U^{1−η} for all
1 ≤ h ≤ U^{η}; i.e. TD(η) with C₀ = 1 holds at n. The exceptional set is o(U⁴/log U), while the interval contains
≍_{c₁,c₂} U⁴/log U primes.
*Proof.* Corollary 2.2 with M = ⌊U⁴/c₂⁴⌋, N = ⌈U⁴/c₁⁴⌉, H = ⌊U^{η}⌋: (N + 16U⁴)U^{2η−1}(2700U^{5η} + 32U^{η}log 2U)
≪ U^{3+7η} log U. ∎

**Corollary 2.4 (almost all primes; PROVED).** For 0 < η < 1/7, TD(η) with C₀ = 1 holds for every prime p in the
fourth-root range except for ≪ U^{3+7η} log U of them (out of ≍ U⁴/log U). For those p, Z54 Corollary T gives
N₂(p, U) ≪_ε U^{1−η+ε}.
*Proof.* A subset of Corollary 2.3's good set; Z54 Cor T needs only TD(η) at the given p. ∎

### 2.5 Honest scope of Theorem LS

* It says nothing about any individual prime. The fourth-root range forces p ≍ U⁴, and the large sieve term 16U⁴ is
  of the size of the whole range, so for windows N ≪ U⁴ the theorem only gives the exceptional-set bound
  ≪ U^{4+2η−1}(…) regardless of N: one cannot localise the average to n ∈ [p, p + p^{1−δ}].
* For N₂ on average it is weaker than the trivial first moment: Σ_{M<n≤M+N} N₂(n, U) ≤ Σ_{u,B ∈ (U,2U]} (N/(uB) + 1)
  ≪ N + U², so for N ≥ U² one has #{n : N₂(n, U) > U^{1−η}} ≪ N U^{η−1} (Markov), while Corollary 2.4 gives only
  N U^{7η−1}.
* Its value is as a statement about T: the "square-root size" of T(h) seen numerically (Z54 §6.1, §4 below) is
  PROVED in mean square over n, with the exceptional set bounded by a power. The pointwise problem is entirely about the
  individual n.
* Primality plays no role anywhere in §2 (consistent with the brief's warning: the statement is an upper bound and does
  not imply ES; at odd squares n = m² the argument proceeds identically).

### 2.6 A pointwise constant-factor bound (PROVED; modest)

**Proposition 2.6 (PROVED).** In the fourth-root range (p prime, c₁p^{1/4} ≤ U ≤ c₂p^{1/4}, 16U³ ≤ p),

  N₄(p, U) ≤ N₂(p, U) ≤ (log 2 / 2)·U + O_{c₁,c₂}(U^{14/15}) = 0.3466…U + O(U^{14/15}),

against the trivial N₂ ≤ U/2. (Not a power saving; recorded because it is the only *pointwise* improvement found.)
*Proof.*
* *Vertex-disjointness.* For u ∈ (U, 2U] there is at most one B ∈ (U, 2U] with B ≡ −p (mod u), since the interval has
  length U < u. Hence each u lies in at most one 2-cycle {u, B}, and both members of a 2-cycle lie in
  dom f := {u ∈ (U, 2U] : some B ∈ (U, 2U] has u | p + B}. So N₂ ≤ |dom f|/2.
* *Exact form.* u ∈ dom f iff (p + U, p + 2U] contains a multiple of u, and it contains at most one, so
  |dom f| = Σ_{U<u≤2U} (⌊(p + 2U)/u⌋ − ⌊(p + U)/u⌋) = UΣ_{U<u≤2U} 1/u + Σ_u [ψ((p + U)/u) − ψ((p + 2U)/u)],
  with ψ(x) := x − ⌊x⌋ − 1/2. The first term is U log 2 + O(1).
* *ψ-sums.* For x ∈ {p + U, p + 2U} and H ≥ 1, the standard consequence of Vaaler's inequality (Graham–Kolesnik,
  *Van der Corput's method*, Thm A.6, and the bound derived from it, Σ_{u∈J}ψ(g(u)) ≪ |J|/H +
  Σ_{1≤h≤H} h^{−1}|Σ_{u∈J} e(hg(u))|; the implied constant is absolute) and the exponent pair (κ, λ) = (1/14, 11/14) = A²(1/2, 1/2)
  applied to g(u) = hx/u on (U, 2U] (F/U ≍ hx/U² ≍ hU² in the fourth-root range) give
  Σ_{U<u≤2U} e(hx/u) ≪ (hU²)^{1/14} U^{11/14} = h^{1/14}U^{13/14}, hence
  Σ_u ψ(x/u) ≪ U/H + H^{1/14}U^{13/14} ≪ U^{14/15} with H = U^{1/15}. (This is the same estimate as Z54 Prop 5.3(a),
  there via Titchmarsh's fourth-derivative test, which gives the identical exponents.)
* So |dom f| = U log 2 + O(U^{14/15}) and N₂ ≤ |dom f|/2. ∎

*EVIDENCE consistency:* Z54 §6.2 reports |dom f|/U = 0.66–0.73 at 10¹²–10¹⁴ (log 2 = 0.693).

## 3. Why the pointwise statement resists (Assessment; heuristic unless marked PROVED)

Everything in this section is an assessment of methods. Only the two displayed facts marked PROVED are claimed as
theorems; the size statements are stationary-phase heuristics.

### 3.1 Self-duality

For a single n, Lemma 2.1 writes T_n(h) as a sum over ≍ U⁴ reduced fractions b/d, d ≤ 4U², with
Σ|Γ(b/d)|² = 𝒢 ≍ U (upper bound PROVED, Lemma 2.5; lower bound EVIDENCE). If the coefficients were of comparable size,
each would be ≍ U^{−3/2}, |T_n| ≍ U^{1/2} would be square-root cancellation in the dual, and |T_n| ≤ U^{1−η} would need
cancellation by a factor U^{3/2+η} among ≍ U⁴ dual terms with phases e(nb/d). Since these phases are the distribution
of n mod d for d ≍ U² ≍ √n, this is the original question again: the problem is self-dual at the fourth-root range
(Z54 §4.2 reached the same conclusion through the k-Poisson route).

### 3.2 One-variable exponent pairs cannot reach the admissible range

Consider the smoothed sum T_φ(h) of Z54 §4.3, for which the expansion T_φ(h) = Σ_ν Σ_{k} c_ν(k) e(−νn/k) is exact and
absolutely convergent (Z54; K := n/U² ≍ U² in the fourth-root range). Stationary phase in the θ-variable suggests
|c_ν(k)| ≍ K^{−1}(U/h)^{1/2} for ≍ hK values of ν (heuristic; Z54 Prop 4.3 has the rigorous Parseval form). If each
k-sum Σ_k c_ν(k)e(−νn/k) is bounded by an exponent pair (κ, λ) applied to the phase νn/k (F/K ≍ νn/K² ≍ hU²), the
outcome is

  |T_φ(h)| ≲ hK · K^{−1}(U/h)^{1/2} · (hU²)^κ K^λ = h^{1/2+κ} U^{1/2+2κ} K^λ,

which is ≤ U^{1−η} only if K ≤ U^{(1/2 − 2κ − η)/λ}, i.e. n = KU² ≤ U^{2 + (1/2 − 2κ − η)/λ}.
**PROVED (elementary):** for every exponent pair, (1/2 − 2κ)/λ ≤ 1, with equality only for (κ, λ) = (0, 1/2). Indeed
λ > 0 and λ ≥ 1/2 − κ ≥ 1/2 − 2κ; if 1/2 − 2κ ≤ 0 the quotient is ≤ 0, otherwise it is ≤ 1 by the last inequality,
with equality forcing κ = 0 and λ = 1/2. So this route gives TD(η) only when n < U³, outside the admissible 16U³ ≤ n,
for every exponent pair including the conjectural limit. Examples: (1/6, 2/3) needs n ≤ U^{2.25}; (2/7, 4/7) needs
n ≤ U^{1.875}. This locates the range where Z54 Prop 4.3's implementation class would work; it says nothing about
arguments exploiting the ν- and k-variables jointly.

### 3.3 Averaging over h / pair correlation

Z54 Theorem T needs only Σ_{h≤H}|T(h)| ≤ HU^{1−η}, and Σ_{h≤H}|T(h)|² = Σ_{k,k′∈E1⁺} Σ_{h≤H} e(h(w_k − w_{k′})) is H
times a (Dirichlet-kernel) pair correlation of the points w_k mod 1 at scale 1/H. A bound Σ_{h≤H}|T(h)|² ≪ HU^{2−2η}
is therefore a statement that the *centred* pair correlation of {w_k mod 1} at scale U^{−η} is ≪ U^{2−2η} (ordinary
density control, #{pairs with ‖w_k − w_{k′}‖ ≤ t} ≪ U²t, is not enough: it gives Σ_h|T(h)|² ≪ U² log H, i.e. no
saving). The coincident pairs are harmless: **PROVED**, r(D) := #{k ∈ E1⁺ : D_k = D} ≤ τ(n² − D) for n ≍ U⁴ (each k
with D_k = D gives a distinct m with m | n + s, hence m | n² − s², and 4m = s² − D gives m | s² − D, so
m | n² − D; distinct k give distinct m), so Σ_D r(D)² ≤ U^{ε}Σ_D r(D) ≪ U^{1+ε}. The non-coincident pairs at scale t unwind to lattice points (m, k) in a union
of ≍ U thin curvilinear regions {c² ≤ (km − n)² − 4m ≤ (c + t)²} ∩ strip, each of area ≍ t; bounds for lattice points
near curves (Huxley–Sargos type, Mλ_r^{2/(r(r+1))} with M = U², λ_r ≍ U^{2−2r}) give ≫ U^{4/3} per unit t, far above
the trivial U, and in any case control density only, not the centred correlation. So this route needs the same
equidistribution of n mod m at window scale that is the problem.

### 3.4 Directions, not alternatives

I did not find a way around the following, any of which would be new: (a) an individual-n asymptotic
#{(m, k) : n + 2U < km ≤ n + 4U, U² < m ≤ 4U²} = 2U log 4 + O(U^{1−η}) for n ≍ U⁴ (the error term Σ_{d≍√x}ψ(x/d) has
no known pointwise bound below x^{0.3149}, and the short-interval divisor asymptotic at length x^{1/4} is open) —
this is the h = 0 analogue, not shown to imply TD but of the same type; (b) a genuinely bilinear estimate for
Σ_ν Σ_k c_ν(k)e(−νn/k) (Z54 §4.3's "joint cancellation"); (c) square-root cancellation in Σ_{m∼M} τ(m) e(2√(mn)) at
M ≍ √n, the Voronoi dual of (a).

## 4. Numerics (EVIDENCE)

`scripts/z55_tdf_numerics.py` (numpy, brute force over m ∈ (U², 4U²]).
* *Pointwise* (`data/z55/tdf/point_U300.txt`, `point_U1000.txt`): primes p ≈ cU⁴, c ∈ {1, 2.5, 6, 16}, h = 1..8.
  U = 300: |E1⁺| ≈ 400–465, √|E1⁺| ≈ 20–22, |T(h)| ∈ [2.0, 39.9]. U = 1000: |E1⁺| ≈ 1470–1600, √ ≈ 39,
  |T(h)| ∈ [6.7, 87.3].
  Square-root size; max/√|E1⁺| ≈ 2.2.
* *Mean square* (`data/z55/tdf/meansq.txt`): U = 100, n ∈ (10⁸, 10⁸ + 4000] (222 primes), h = 1..6:
  mean_n |T_n(h)|² = 150–158 vs mean |E1⁺| = 152.1; over primes only 132–168. U = 300, n ∈ (8.1·10⁹, +3000] (124
  primes): mean_n |T_n|² = 429–452 vs mean |E1⁺| = 441.6; primes 394–499. So the data are consistent with
  E_n|T_n(h)|² ≈ E_n|E1⁺| with no visible h-dependence, already on windows of length 3000 ≪ U⁴.
* *Theorem LS check*: §2.1, §2.4 (`data/z55/tdf/farey_check.txt`).

## 5. Summary of labels

| statement | label |
|---|---|
| Lemma 0.1 (T_p = brief's T; identification valid for all n) | PROVED |
| Lemma 2.1 (Farey expansion), 2.2 (Parseval) | PROVED (+ floating-point check, EVIDENCE) |
| Lemma 2.3, 2.4, 2.4′ (bounds for A_{d,r}; explicit Kusmin–Landau), 2.5 (𝒢 ≤ 2700h⁴U + 32U log 2U) | PROVED |
| Theorem LS (mean square over n ≤ (N + 16U⁴)𝒢) | PROVED (+ floating-point check, EVIDENCE) |
| Corollaries 2.2–2.4 (exceptional sets; TD(η) for almost all n, almost all primes, η < 1/7) | PROVED |
| Prop 2.6 (N₂ ≤ (log 2/2)U + O(U^{14/15}), pointwise) | PROVED (constant factor only) |
| TD(η) for all primes in the fourth-root range | OPEN (not proved here) |
| §3 (self-duality, exponent-pair range, clustering) | Assessment (heuristic sizes); only the two items marked PROVED are theorems |
| §4 sizes | EVIDENCE |
