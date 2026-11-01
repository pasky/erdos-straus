# Z53_SQSIEVE — depth lane SQSIEVE (follow-up to HYPSUMPROD; FRONTIER §7.1): the square sieve on the tied hyperbola — exponent, reach, reverse direction

ES is OPEN. Nothing here proves or disproves it, and nothing here is progress on the *existence* of a solution of 4/p.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal results are internally reviewed only
(not refereed).

Brief: `z52bbriefs/z53_depth.md`, lane kickoff `z52bbriefs/z53_lanes.md` §SQSIEVE. Predecessor: `Z53_HYPSUMPROD.md`
(Theorem 1: R(n) ≪ n^{1/3−1/225}(log n)², cross-reviewed in `data/z53/xreview/REVIEW_HYPSUMPROD.md`). Scripts
`scripts/z53_sqsieve_*`, data `data/z53/sqsieve/`.

*Status: CHECKPOINT 1 (skeleton; statements, why open, first lemmas and first falsifier checks).*

## 0. Notation (as in HYPSUMPROD)

n ≥ 2; R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}. Dyadic block 𝔅(U,V,W): u ∈ (U,2U], B ∈ (V,2V], C ∈ (W,2W]; N(U,V,W) its
count; UVW ≍ n for nonempty blocks; exponents U = n^α, V = n^β, W = n^γ, α + β + γ = 1 + O(1/log n). Trivial bound
N ≤ n^{o(1)} min(U, V, W) (Z52D Thm 1). By the symmetry (u,B,C) ↦ (B,u,C) we may take U ≤ V.
Strip coordinates (HYPSUMPROD Lemma 1.1): k = uB, s = u + B = 4Ck − n, and f(C,k) := (4Ck − n)² − 4k = (u − B)².
χ_Q = Jacobi symbol mod Q = qq′ (q ≠ q′ odd primes).

## 1. Statements attacked

**(S1) Exponent.** Improve the HYPSUMPROD exponent 1/3 − 1/225 ≈ 0.32889 for R(n) ≪ n^{θ+ε}, uniformly in n.
→ Theorem A (target): **R(n) ≪_ε n^{12/37+ε}** (12/37 ≈ 0.32432), PROVED relative to the same textbook inputs as HYPSUMPROD
(third-derivative test) plus Weil's Kloosterman bound; n^{21/65+ε} relative to Bourgain's exponent pair (13/84+ε, 55/84+ε);
n^{4/13+ε} CONDITIONAL on the exponent pair (ε, 1/2).
**(S2) Reach.** Determine the block shapes (α, β, γ) where the square sieve beats min(α, β, γ); does it reach the balanced
block u, B ≍ n^{1/4}, C ≍ n^{1/2}? → Proposition B (target): explicit linear region; at the balanced block the route
is *exactly* at the trivial exponent even under the exponent-pair conjecture (scoped barrier: needs beyond-square-root
cancellation in the dual C-sums).
**(S3) Reverse direction.** Is there a lower-bound, square-sensitive version (must vanish at odd squares n = m²)?
→ Theorem C (target): square-sensitivity is exactly the Brauer–Manin twist (−k/n) (squares of f on the strip at coprime
points lie in 𝒜⁻ = {(−k/n) = −1}, empty at n = m²); every square-sieve datum of fixed (auxiliary) conductor is the same at
odd squares; lower bounds reduce to closed items (low-conductor universality, Cor A′) or to B2.

## 2. Why this is not already closed
HYPSUMPROD proved Theorem 1 with exponent 74/225 using absolute values of per-class discrepancies (Q² residue classes, each
bounded by Vaaler + third-derivative test); it did not use the Fourier structure of the character in the k-variable, did not
smooth the strip, did not optimise per block (it used a single near-cube region with η-loss), and left reach and the
reverse direction open ("not pursued"; §4.3 "not an impossibility theorem"; §5 one sentence). None of the closed items
(one-step dualization at fixed conductor; ET/Fejér with max|S_h| input; Cauchy–Schwarz in the function variable;
low-conductor universality) covers the new step: here Poisson is applied in k *inside* each fixed C with a χ_Q-twist, and
the dual sums are complete Kloosterman sums (mod Q) times exponential sums in C — an upper-bound argument, not a main-term
or positivity argument.

## 3. First lemmas (PROVED; checked numerically)

**Lemma W (complete twisted sums).** For an odd prime q, c, ℓ, n ∈ ℤ let G^{(q)}_c(ℓ) := Σ_{k mod q} (f(c,k)/q) e(ℓk/q).
Then |G| ≤ 2√q if q ∤ ℓ; if q | ℓ, G = K_q(c) ∈ {0, −1, q − 1} (HYPSUMPROD Lemma 1.3). Consequently Σ_{c mod q}|G_c(ℓ)| ≤ 2q^{3/2}
for every ℓ, and for Q = qq′: Σ_{c mod Q}|G^{(Q)}_c(ℓ)| ≤ 4Q^{3/2}.
*Proof sketch (full proof in §4).* For q ∤ c, q ∤ ℓ complete the square in k and open the Legendre symbol by Gauss sums: the sum
becomes a Kloosterman sum S(·,·;q) (or a Ramanujan-type sum of modulus 1 in the degenerate-discriminant case); Weil. For
q | c it is a Gauss sum (modulus √q). CRT for Q.
*Check:* `scripts/z53_sqsieve_checks.py 23 20000`: all 27 962 cases (q ≤ 23, all n, c, ℓ mod q) pass; max |G|/√q = 1.931.

**Lemma P (Poisson in k).** For Φ ∈ C_c^∞(ℝ), C ≥ 1, Q ≥ 1, S > 0:
Σ_{k∈ℤ} Φ((4Ck − n)/S) χ_Q(f(C,k)) = Σ_{ℓ∈ℤ} (S/(4CQ)) Φ̂(ℓS/(4CQ)) e(−ℓn/(4CQ)) G^{(Q)}_C(ℓ).
*Check:* `scripts/z53_sqsieve_poisson.py` (Gaussian Φ): agreement to 10⁻¹¹ at n = 1 000 003, 999 999 937, 998 001 = 999²
(odd square), 8 813 281 (test prime) (`data/z53/sqsieve/poisson_check.txt`).

**Lemma BM (Brauer–Manin twist in strip coordinates).** n odd, (u,B,C) a (★) triple with gcd(uBC, n) = 1 ⇒ (−uB/n) = −1
(Jacobi). [Known content: `BM_CORRECTED_COUNT.md` Thm 1.1 for primes.] Check: 87 388 coprime triples with odd n ≤ 20 000,
0 violations.

## 4. Theorem A (the exponent 12/37) — statement and full proof

**Theorem A (PROVED, relative to Weil's bound for Kloosterman sums and van der Corput's third-derivative test).** For
every ε > 0 and every n ≥ 2,  **R(n) ≪_ε n^{12/37+ε}**  (12/37 = 0.324324…; HYPSUMPROD: 74/225 = 0.328889…). The
cube block U = V = W ≍ n^{1/3} has N ≪_ε n^{17/54+ε} (17/54 = 0.31481; HYPSUMPROD: 8/25). Nothing about primality is used;
the bound holds at odd squares, where R = 0.

**Theorem A′ (PROVED relative to Bourgain's exponent pair).** If (κ, λ) is an exponent pair (Graham–Kolesnik sense) with
λ = κ + 1/2, then R(n) ≪_ε n^{4/(13−4κ)+ε}. With Bourgain's pair (13/84 + ε, 55/84 + ε) (J. Bourgain, *Decoupling,
exponential sums and the Riemann zeta function*, JAMS 30 (2017), arXiv:1408.5794, **Theorem 6**; the source gives a
sketch of proof and defers the class of admissible phases to Graham–Kolesnik Ch. 3; see `data/z53/sqsieve/LIT_CHECK.md`):
**R(n) ≪_ε n^{21/65+ε}** (21/65 = 0.323077). With (κ, λ) = (1/6, 2/3) this recovers 12/37.
**Corollary A″ (CONDITIONAL on the exponent-pair conjecture (ε, 1/2 + ε)):** R(n) ≪_ε n^{4/13+ε} (0.307692).

### 4.1 Blocks, smoothing, square detection
Fix Φ ∈ C_c^∞(ℝ), 0 ≤ Φ ≤ 1, Φ = 1 on [1, 4], supp Φ ⊂ [1/2, 5]; Φ̂(ξ) := ∫Φ(t)e(−ξt)dt and
Ψ(x) := sup_{|ξ| ≥ |x|}(|Φ̂(ξ)| + |ξΦ̂′(ξ)|), so Ψ is non-increasing in |x| and Ψ(x) ≪_A (1 + |x|)^{−A} for every A.
Every (★) triple lies in exactly one dyadic block 𝔅(U,V,W) (U, V, W ∈ {2^j : j ≥ 0}·½). Since u + B ≤ 2uB ≤ 2uBC,
n = 4uBC − u − B ≥ 2uBC, so n < 4uBC ≤ 2n; hence u, B, C ≤ n/2, O(log³ n) blocks are nonempty, and nonempty blocks have
n/32 ≤ UVW < n/2. As N(U,V,W) = N(V,U,W) we assume U ≤ V.

**Lemma 1′ (smoothed square detection; PROVED).** Put ω(C,k) := 1_{(W,2W]}(C)·Φ((4Ck − n)/V) and, for a ≠ 0,
w(a) := Σ_{(C,k)∈ℤ²: f(C,k)=a} ω(C,k). Then N(U,V,W) ≤ 2Σ_{m≥1} w(m²) + τ(n), and ω(C,k) ≠ 0 ⇒ 1 ≤ k and f(C,k) ≤ 25V².
*Proof.* A block triple with u ≠ B has s := u + B ∈ (U + V, 2U + 2V] ⊂ (V, 4V] (U ≤ V), so with k := uB we get
4Ck − n = s (HYPSUMPROD Lemma 1.1(i)), Φ(s/V) = 1, ω(C,k) = 1, and f(C,k) = (u − B)² ≥ 1. Given (C,k), s = 4Ck − n is
determined and {u, B} is the root set of z² − sz + k, so at most two ordered triples map to (C,k). Triples with u = B satisfy
u(4uC − 2) = n, so u | n and C is determined by u: at most τ(n) of them. If ω(C,k) ≠ 0 then s = 4Ck − n ∈ [V/2, 5V], so
4Ck ≥ n + V/2 > 0 gives k ≥ 1 and f = s² − 4k ≤ 25V². ∎

**Square sieve.** Let 𝒫 be the primes in (P, 2P] (P ≥ 3), P₀ := |𝒫|, and assume 2^{P₀} ≥ 25V². HYPSUMPROD Lemma 1.2 (a
proved variant of Heath-Brown, Math. Ann. 266 (1984), Thm 1; positive squares a > 2^{P₀} carry no weight by Lemma 1′) gives
  Σ_{m≥1} w(m²) ≤ (4/P₀)·S₁ + 4·max_{q≠q′∈𝒫} |S_{qq′}|,  S_Q := Σ_{(C,k)∈ℤ²} ω(C,k) χ_Q(f(C,k)),     (4.1)
where S₁ (Q = 1, χ₁ ≡ 1) bounds Σ_a w(a), and Σ_a w(a)(a/Q) = S_Q because χ_Q(0) = 0.

### 4.2 Lemma W (complete twisted sums; PROVED relative to Weil's Kloosterman bound)
For an odd prime q and c, ℓ ∈ ℤ put G^{(q)}_c(ℓ) := Σ_{k mod q} (f(c,k)/q) e(ℓk/q) (Legendre symbol). Then
(a) q | ℓ: G = K_q(c) := Σ_k (f(c,k)/q) equals 0 if q | c, q − 1 if q ∤ c and q | 4cn + 1, and −1 otherwise;
(b) q ∤ ℓ: |G| ≤ 2√q;
(c) for every ℓ: Σ_{c mod q} |G^{(q)}_c(ℓ)| ≤ 2q^{3/2};
(d) for Q = qq′ (q ≠ q′) and G^{(Q)}_c(ℓ) := Σ_{k mod Q} χ_Q(f(c,k)) e(ℓk/Q): G^{(Q)}_c(ℓ) = G^{(q)}_c(ℓq̄′)·G^{(q′)}_c(ℓq̄)
    (q̄′ q′ ≡ 1 mod q, q̄ q ≡ 1 mod q′), hence Σ_{c mod Q} |G^{(Q)}_c(ℓ)| ≤ 4Q^{3/2} and |G^{(Q)}_c(ℓ)| ≤ 4√Q unless q | ℓ or q′ | ℓ.
*Proof.* f(c,k) = 16c²k² − (8cn + 4)k + n². (a) is HYPSUMPROD Lemma 1.3.
(b) If q | c: f ≡ n² − 4k; substituting t = n² − 4k (a bijection of ℤ/q), G = e(ℓ·4̄n²/q)Σ_t (t/q)e(−ℓ4̄t/q), a Gauss sum of
modulus √q. If q ∤ c: A := 16c² is a nonzero square mod q; with r := (8cn + 4)(2A)⁻¹ and d := 16(4cn + 1)(4A²)⁻¹ (mod q) we
have f(c,k) ≡ A((k − r)² − d), so G = e(ℓr/q)·H, H := Σ_x ((x² − d)/q) e(ℓx/q). If d ≡ 0: H = Σ_{x≠0} e(ℓx/q) = −1.
If d ≢ 0: write (y/q) = g⁻¹Σ_{t mod q}(t/q)e(ty/q) (valid for all y, g the quadratic Gauss sum, g² = (−1/q)q) and
Σ_x e((tx² + ℓx)/q) = (t/q)·g·e(−\overline{4t}ℓ²/q) for t ≢ 0; hence H = Σ_{t≢0} e((−dt − 4̄ℓ²t̄)/q) = S(−d, −4̄ℓ²; q), a
Kloosterman sum with q ∤ d·ℓ, and Weil's bound |S(a,b;q)| ≤ 2√q (q ∤ ab; Iwaniec–Kowalski, *Analytic Number Theory*,
Thm 11.11 / Cor 11.12; Weil, PNAS 34 (1948)) gives |H| ≤ 2√q.
(c) For q ∤ ℓ use (b) for each of the q classes. For q | ℓ, by (a): one class gives 0, at most one class gives q − 1, the
others −1: total ≤ 2q − 3.
(d) χ_Q = χ_qχ_{q′}, 1/(qq′) ≡ q̄′/q + q̄/q′ (mod 1), and CRT k ↔ (k mod q, k mod q′); the sum factors. Summing over
c mod Q ↔ (c mod q, c mod q′) multiplies the two bounds (c). ∎
*Check (EVIDENCE/CERTIFIED for the range):* `scripts/z53_sqsieve_checks.py 23 …`: all 27 962 cases (q ≤ 23, all n, c, ℓ mod q)
satisfy (a)–(c); max |G|/√q over q ∤ ℓ is 1.931.

### 4.3 Lemma P (Poisson in k; PROVED)
For integers C ≥ 1, Q ≥ 1 (Q = 1 or Q = qq′):
  Σ_{k∈ℤ} Φ((4Ck − n)/V) χ_Q(f(C,k)) = Σ_{ℓ∈ℤ} a_ℓ(C) e(−ℓn/(4CQ)) G^{(Q)}_C(ℓ),  a_ℓ(C) := (V/(4CQ)) Φ̂(ℓV/(4CQ)),
with G^{(1)} ≡ 1. *Proof.* Write k = k₀ + Qj (k₀ mod Q); f(C,k) mod Q depends only on k₀. For fixed k₀ apply Poisson
summation in j to g(x) := Φ((4CQx + 4Ck₀ − n)/V) (smooth, compactly supported): substituting t = (4CQx + 4Ck₀ − n)/V,
ĝ(ℓ) = (V/(4CQ)) Φ̂(ℓV/(4CQ)) e(−ℓn/(4CQ)) e(ℓk₀/Q). Multiply by χ_Q(f(C,k₀)) and sum over k₀. The ℓ-series converges
absolutely (Φ̂ is Schwartz). ∎ *Check:* `scripts/z53_sqsieve_poisson.py` (Gaussian Φ) agrees to ≤ 1.3·10⁻¹¹ at four n
(including the odd square 999² and the test prime 8 813 281), `data/z53/sqsieve/poisson_check.txt`.

### 4.4 Proposition D (the strip sums; PROVED relative to Lemma W and the third-derivative test)
Let V, W ≥ 1 and Q = 1 or Q = qq′ with Q ≤ W. Then, with c depending only on Φ,
  |S_Q| ≤ c·[ V/Q + V/W + Q·n^{1/6}W^{1/2}V^{−1/6} + Q^{1/2}V^{1/6}W n^{−1/6} + Q^{3/2} ].     (4.2)
*Proof.* By Lemma P, S_Q = Σ_{ℓ∈ℤ} Σ_{C∈(W,2W]} a_ℓ(C) e(−ℓn/(4CQ)) G_C(ℓ) (finite C-sum, absolutely convergent ℓ-sum).
*(i) ℓ = 0.* G_C(0) = K(C) := K_q(C)K_{q′}(C) (Q = qq′) or 1 (Q = 1). By Lemma W(a), |K_q(c)| ≤ 1 + q·1_{D_q}(c) with D_q a
single class mod q, and a class mod m meets (W, 2W] in ≤ W/m + 1 integers, so Σ_{C∈(W,2W]} |K(C)| ≤ W + q(W/q + 1) +
q′(W/q′ + 1) + Q(W/Q + 1) ≤ 4W + 3Q. Since |a₀(C)| ≤ V|Φ̂(0)|/(4QW), the ℓ = 0 term is ≤ |Φ̂(0)|(V/Q + V/W) (and
≤ |Φ̂(0)|V/4 for Q = 1).
*(ii) ℓ ≠ 0: classes and partial summation.* Group C by c₀ ≡ C (mod Q): the ℓ-term is ≤ Σ_{c₀ mod Q} |G_{c₀}(ℓ)|·
|Σ_{C∈(W,2W], C≡c₀} a_ℓ(C) e(φ_ℓ(C))|, φ_ℓ(C) := −ℓn/(4CQ). With ξ = ℓV/(4CQ) we have |ξ| ≥ |ℓ|V/(8QW) on (W, 2W],
|a_ℓ(C)| ≤ (V/(4QW))Ψ(ℓV/(8QW)), and a_ℓ′(C) = −(V/(4QC²))(Φ̂(ξ) + ξΦ̂′(ξ)), so ∫_W^{2W}|a_ℓ′| ≤ (V/(8QW))Ψ(ℓV/(8QW)).
Abel summation over the arithmetic progression gives
  |Σ_{C≡c₀} a_ℓ(C)e(φ_ℓ(C))| ≤ (3V/(8QW)) Ψ(ℓV/(8QW)) · E_Q(ℓ),  E_Q(ℓ) := max_{c₀} max_{J⊂(W,2W] interval} |Σ_{C∈J, C≡c₀ (Q)} e(φ_ℓ(C))|.
With Lemma W(c,d): |S_Q − (ℓ = 0 term)| ≤ (3V/(2QW))·Q^{3/2}·Σ_{ℓ≠0} Ψ(ℓV/(8QW)) E_Q(ℓ).
*(iii) Third-derivative test.* Write C = c₀ + Qj; j runs over the integers of an interval of length ≤ W/Q, and
g(j) := φ_ℓ(c₀ + Qj) has g‴(j) = (3/2)ℓnQ²/C⁴, so λ₃ ≤ |g‴| ≤ 16λ₃ with λ₃ := (3/32)|ℓ|nQ²/W⁴. Titchmarsh, *Theory of the
Riemann zeta-function*, 2nd ed., Thm 5.11 (p. 106; b − a ≥ 1) — and the trivial bound ≤ 2 for intervals of length < 1 — give
  E_Q(ℓ) ≤ c[(W/Q)λ₃^{1/6} + (W/Q)^{1/2}λ₃^{−1/6} + 2] ≤ c′[|ℓ|^{1/6}n^{1/6}W^{1/3}Q^{−2/3} + |ℓ|^{−1/6}n^{−1/6}W^{7/6}Q^{−5/6} + 2].
*(iv) The ℓ-sum.* For σ ∈ {1/6, 0, −1/6} and every M > 0: Σ_{ℓ≠0} Ψ(ℓ/M)|ℓ|^σ ≤ c_σ M^{1+σ} (for M ≥ 1 split at |ℓ| = M and
use Ψ(x) ≪ |x|^{−2}; for M < 1 use Ψ(ℓ/M) ≪ M²ℓ^{−2} ≤ M^{1+σ}ℓ^{−2}). Taking M = 8QW/V,
  (V/(QW))Q^{3/2}·[(QW/V)^{7/6}n^{1/6}W^{1/3}Q^{−2/3} + (QW/V)^{5/6}n^{−1/6}W^{7/6}Q^{−5/6} + QW/V]
  = Q n^{1/6}W^{1/2}V^{−1/6} + Q^{1/2}V^{1/6}W n^{−1/6} + Q^{3/2}. ∎
*Remark (where the gain over HYPSUMPROD comes from).* HYPSUMPROD bounded Σ_{c₀,k₀}|E(c₀,k₀)| — absolute values over all Q²
residue classes of the strip discrepancy — and lost Q² · (per-class discrepancy). Here the character is Fourier-expanded in
k *before* any absolute value: the k₀-sum becomes a complete Kloosterman-type sum (size √Q, Lemma W) and only the c₀-classes
(Q of them) are summed absolutely; smoothing in s removes the Vaaler truncation. Net effect at the cube: discrepancy
Q·T^{5/6} instead of T^{6/7}Q^{9/7} (T = n^{1/3}).

### 4.5 Assembly (PROVED; exponent bookkeeping exact)
Let 𝔅(U,V,W) be a nonempty block, U ≤ V, and α := log U/log n, β := log V/log n, γ := log W/log n, so
|α + β + γ − 1| ≤ 5/log n. Put θ* := 12/37.
*Case 1: min(α, γ) ≤ θ*.* The trivial bound N ≤ min(U, W)·max_{m≤4n²}τ(m) ≪_ε n^{θ*+ε} (fix u: B | n + u; fix C: 4Cu − 1 | 4Cn + 1).
*Case 2: α, γ > θ*.* Then β ≥ α > θ* and β ≤ 1 − α − γ + 5/log n < 13/37 + 5/log n. Take P := n^{ρ*}, ρ* := (7β/6 − 1/6 − γ/2)/3,
𝒫 = primes in (P, 2P], so Q = qq′ ∈ (P², 4P²]. By (4.1), Lemma 1′ and (4.2) (with Q = 1 for S₁, P₀ ≫ P/log P):
  N ≪ (log n/P)·[V + V/W + n^{1/6}W^{1/2}V^{−1/6} + V^{1/6}W n^{−1/6} + 1] + V/P² + V/W + P²n^{1/6}W^{1/2}V^{−1/6} + P V^{1/6}W n^{−1/6} + P³ + τ(n).
In exponents (base n, up to O(1/log n) and the log factor), with β = 1 − α − γ:
  β − ρ* = 2ρ* + 1/6 + γ/2 − β/6 = (11β + 1 + 3γ)/18 = (12 − 11α − 8γ)/18 < (12 − 19θ*)/18 = θ*,
and the remaining terms ρ* + β/6 + γ − 1/6, 3ρ*, β − γ, β − 2ρ*, 1/6 + γ/2 − β/6 − ρ*, β/6 + γ − 1/6 − ρ* are all ≤ θ* on the
closed triangle {α ≥ θ*, γ ≥ θ*, β ≥ α}: every term is linear in (α, γ), so it suffices to check the three vertices
(α, β, γ) = (12/37, 13/37, 12/37), (12/37, 12/37, 13/37), (25/74, 25/74, 12/37); exact rational evaluation in
`scripts/z53_sqsieve_exponents.py` (output `data/z53/sqsieve/exponents.txt`) gives maxima 12/37, 104/333, 421/1332. The side
conditions hold on the triangle with room: ρ* ≥ 4/333 > 0 (so P₀ ≫ n^{0.012}/log n and 2^{P₀} ≥ 25V² for n ≥ n₀), and
2ρ* ≤ 2/37 < 12/37 < γ (so Q ≤ 4P² ≤ W for n ≥ n₀). The O(1/log n) perturbations of the exponents cost O(1) factors.
Summing over the O(log³ n) blocks: R(n) ≪_ε n^{12/37+ε}. At the cube (α = β = γ = 1/3): ρ* = 1/54, N ≪ n^{17/54+ε}.
For Theorem A′ replace (iii) by the exponent-pair bound E_Q(ℓ) ≪ (|ℓ|n/W²)^κ(W/Q)^λ + 2 (phase x ↦ ℓn/(4Q²x) on x ∈ (W/Q, 2W/Q],
shifted by c₀/Q < 1, which lies in the Graham–Kolesnik class with s = 2, y = |ℓ|n/(4Q²) ≥ N² for N = W/Q ≥ N₀); then (iv)
gives Q^{3/2+κ−λ}n^κW^{λ−κ}V^{−κ} + Q^{3/2} in place of the two third-derivative terms, i.e. P²n^κW^{1/2}V^{−κ} when
λ − κ = 1/2; ρ* := ((1 + κ)β − κ − γ/2)/3 and the same vertex check with θ* = 4/(13 − 4κ) (script; Bourgain:
21/65; conjectural κ = 0: 4/13). ∎

*Why 12/37 and not 17/54 (the cube value).* The worst block is the off-cube shape (α, β, γ) = (12/37, 13/37, 12/37): the
square sieve's main term is |𝒜|/P ≍ V/P with V = max(U, V), while the trivial bound is min(U, W); asymmetry U < V costs.
