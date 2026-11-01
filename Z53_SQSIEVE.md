# Z53_SQSIEVE — depth lane SQSIEVE (follow-up to HYPSUMPROD; FRONTIER §7.1): the square sieve on the tied hyperbola — exponent, reach, reverse direction

ES is OPEN. Nothing here proves or disproves it, and nothing here is progress on the *existence* of a solution of 4/p.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal results are internally reviewed only
(not refereed).

Brief: `z52bbriefs/z53_depth.md`, lane kickoff `z52bbriefs/z53_lanes.md` §SQSIEVE. Predecessor: `Z53_HYPSUMPROD.md`
(Theorem 1: R(n) ≪ n^{1/3−1/225}(log n)², cross-reviewed in `data/z53/xreview/REVIEW_HYPSUMPROD.md`). Scripts
`scripts/z53_sqsieve_*`, data `data/z53/sqsieve/`.

*Status: full draft, hostile review 1 applied (checkpoint 1 was commit facb8fc5).* Verdict: (S1) **strengthened** —
R(n) ≪ n^{12/37+ε}; (S2) **narrowed**; (S3) **narrowed** (closed for quadratic σ-minorants; open otherwise). See §9.

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
block u, B ≍ n^{1/4}, C ≍ n^{1/2}? → §5.1 (exact gain region) and Proposition B2: at the balanced block every
implementation of the k-Poisson route is *exactly* at the trivial exponent, even granting square-root cancellation in
every C-sum (scoped barrier: what is missing is a bilinear (ℓ, C) cancellation estimate).
**(S3) Reverse direction.** Is there a lower-bound, square-sensitive version (must vanish at odd squares n = m²)?
→ Theorem C1, Lemma C3, Proposition C4: squares of f on the strip at coprime points lie in 𝒜⁻ = {(−k/n) = −1} (the
Brauer–Manin twist), which is empty at n = m²; the complete sums and the ℓ = 0 main terms of the auxiliary-conductor sums
depend on n only through n mod Q; Heath-Brown-type quadratic minorants have non-positive main coefficient (so a lower bound
needs signed estimates of the auxiliary sums); conic/representation-count lower bounds reduce to B2 or closed items.

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
*Proof sketch (full proof in §4.2).* For q ∤ c, q ∤ ℓ complete the square in k and open the Legendre symbol by Gauss sums: the sum
becomes a Kloosterman sum S(·,·;q) (or a sum of absolute value 1 in the degenerate-discriminant case); Weil. For
q | c it is a Gauss sum (modulus √q). CRT for Q.
*Check:* `scripts/z53_sqsieve_checks.py 23 20000`: all 27 962 cases (q ≤ 23, all n, c, ℓ mod q) pass; max |G|/√q = 1.931.

**Lemma P (Poisson in k).** For Φ ∈ C_c^∞(ℝ), C ≥ 1, Q ≥ 1, S > 0:
Σ_{k∈ℤ} Φ((4Ck − n)/S) χ_Q(f(C,k)) = Σ_{ℓ∈ℤ} (S/(4CQ)) Φ̂(ℓS/(4CQ)) e(−ℓn/(4CQ)) G^{(Q)}_C(ℓ).
*Check:* `scripts/z53_sqsieve_poisson.py` (Gaussian Φ; Lemma P holds verbatim for Schwartz Φ): agreement to 10⁻¹¹ at n = 1 000 003, 999 999 937, 998 001 = 999²
(odd square), 8 813 281 (test prime) (`data/z53/sqsieve/poisson_check.txt`).

**Lemma BM (= Theorem C1 below; Brauer–Manin twist in strip coordinates).** n odd, (u,B,C) a (★) triple with gcd(uBC, n) = 1 ⇒ (−uB/n) = −1
(Jacobi). [Known content: `BM_CORRECTED_COUNT.md` Thm 1.1 for primes.] Check: 87 388 coprime triples with odd n ≤ 20 000,
0 violations.

## 4. Theorem A (the exponent 12/37) — statement and full proof

**Theorem A (PROVED, relative to Weil's bound for Kloosterman sums and van der Corput's third-derivative test).** For
every ε > 0 and every n ≥ 2,  **R(n) ≪_ε n^{12/37+ε}**  (12/37 = 0.324324…; HYPSUMPROD: 74/225 = 0.328889…). The
cube block U = V = W ≍ n^{1/3} has N ≪_ε n^{17/54+ε} (17/54 = 0.31481; HYPSUMPROD: n^{8/25}(log n)²). Nothing about primality is used;
the bound holds at odd squares, where R = 0.

**Theorem A′ (PROVED for a general exponent pair; the Bourgain instance is CONDITIONAL on the literature result).** If
(κ, λ) is an exponent pair (Graham–Kolesnik sense) with λ = κ + 1/2 and 0 ≤ κ < 1/4, then R(n) ≪_ε n^{4/(13−4κ)+ε}
(at κ = 1/4 the value is the trivial 1/3). With Bourgain's pair (13/84 + ε, 55/84 + ε) (J. Bourgain, *Decoupling,
exponential sums and the Riemann zeta function*, JAMS 30 (2017), arXiv:1408.5794, **Theorem 6**; the source gives a
sketch of proof and defers the class of admissible phases to Graham–Kolesnik Ch. 3; see `data/z53/sqsieve/LIT_CHECK.md`):
**R(n) ≪_ε n^{21/65+ε}** (21/65 = 0.323077) — relative to Bourgain's Theorem 6 as an exponent pair for the model phases
of the Graham–Kolesnik class (its proof in the source is a sketch whose "suitable F" hypotheses are not listed; we do not
re-verify it). With (κ, λ) = (1/6, 2/3) this recovers 12/37.
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
Let V, W ≥ 1 and Q = 1 or Q = qq′ (the hypothesis Q ≤ W of the draft is not needed: when W/Q < 1 the trivial "+2" applies;
it holds in all applications anyway). Then, with c depending only on Φ,
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
and the remaining terms ρ* + β/6 + γ − 1/6, 3ρ*, β − γ, β − 2ρ*, 1/6 + γ/2 − β/6 − ρ*, β/6 + γ − 1/6 − ρ* (and the
trivially dominated β − γ − ρ*, −ρ*, and the exponent 0+ε of τ(n)) are all ≤ θ* on the
closed triangle {α ≥ θ*, γ ≥ θ*, β ≥ α}: every term is linear in (α, γ), so it suffices to check the three vertices
(α, β, γ) = (12/37, 13/37, 12/37), (12/37, 12/37, 13/37), (25/74, 25/74, 12/37); exact rational evaluation in
`scripts/z53_sqsieve_exponents.py` (output `data/z53/sqsieve/exponents.txt`) gives maxima 12/37, 104/333, 421/1332. The side
conditions hold on the triangle with room: ρ* ≥ 4/333 > 0 (so P₀ ≫ n^{0.012}/log n and 2^{P₀} ≥ 25V² for n ≥ n₀), and
2ρ* ≤ 2/37 < 12/37 < γ (so Q ≤ 4P² ≤ W for n ≥ n₀). The O(1/log n) perturbations of the exponents cost O(1) factors.
Summing over the O(log³ n) blocks: R(n) ≪_ε n^{12/37+ε}. At the cube (α = β = γ = 1/3): ρ* = 1/54, N ≪ n^{17/54+ε}.
For Theorem A′ replace (iii) by the exponent-pair bound E_Q(ℓ) ≪ (|ℓ|n/W²)^κ(W/Q)^λ + 2. Justification: for ℓ > 0 the
phase is −X/(j + c₀/Q) with X = ℓn/(4Q²), j in an interval of length ≤ N := W/Q; after peeling off ≤ 1 boundary term the
j-range lies in a dyadic interval (N′, 2N′] with N′ ≍ N, and for N ≥ N₀ the shifted phase lies in the Graham–Kolesnik class
F(N′, P, s = 2, y = X, ε) (relative derivative error O(1/N)); the condition y ≥ N′² is |ℓ|n ≥ 4W²·O(1), which holds because
γ ≤ 13/37 + o(1) < 1/2 in Case 2 (and for S₁); ℓ < 0 by complex conjugation. Then (iv)
gives Q^{3/2+κ−λ}n^κW^{λ−κ}V^{−κ} + Q^{3/2} in place of the two third-derivative terms, i.e. P²n^κW^{1/2}V^{−κ} when
λ − κ = 1/2; ρ* := ((1 + κ)β − κ − γ/2)/3 and the same vertex check with θ* = 4/(13 − 4κ) (script; Bourgain:
21/65; conjectural κ = 0: 4/13). ∎

*Why 12/37 and not 17/54 (the cube value).* The worst block is the off-cube shape (α, β, γ) = (12/37, 13/37, 12/37): the
square sieve's main term is |𝒜|/P ≍ V/P with V = max(U, V), while the trivial bound is min(U, W); asymmetry U < V costs.

## 5. Reach: block-shape map, and the balanced block

### 5.1 Where the §4 bound beats the trivial bound (PROVED; endpoints solved exactly by hand, script is a grid cross-check)
For a block (α, β, γ) with α ≤ β the §4 bound has exponent θ_A(β, γ) := max of the linear terms of §4.5 at ρ = ρ*(β, γ), and
**it beats the trivial exponent t = min(α, γ) by a power wherever θ_A < t, ρ* > 0, 2ρ* < γ** — a polygon cut out by finitely
many linear inequalities. On the diagonal U = V (α = β, γ = 1 − 2β) the gain region is exactly (from
`scripts/z53_sqsieve_reach.py`, endpoints solved by hand):

| input for the C-class sums | diagonal gain region (β) | cube exponent | global exponent |
|---|---|---|---|
| third-derivative test (Thm A) | (4/13, 14/41) = (0.3077, 0.3415) | 17/54 = 0.3148 | 12/37 = 0.3243 |
| Bourgain pair (Thm A′) | (55/181, 197/575) = (0.3039, 0.3426) | 59/189 = 0.3122 | 21/65 = 0.3231 |
| conjectural pair (0, 1/2) (Cor A″) | (1/4, 5/14) = (0.25, 0.3571) | 5/18 = 0.2778 | 4/13 = 0.3077 |
| HYPSUMPROD (for comparison) | ≈ (0.31, 0.335) (grid) | 8/25 = 0.32 | 74/225 = 0.3289 |

### 5.2 The balanced block (Proposition B2; PROVED, scoped to the §4 implementation)
Call an *implementation of §4* any argument that (i) applies Lemma 1′ and the square sieve (4.1), (ii) expands S_Q by
Lemma P, (iii) bounds the dual by the triangle inequality over ℓ and over c₀ mod Q and by Abel summation as in §4.4(ii)
(with the true weights |G_{c₀}(ℓ)|, |a_ℓ(C)| or upper bounds for them), and (iv) bounds the C-class sums, for every ℓ with
|ℓ| ≥ ℓ₁ := 16W²/n (the range where the phase has |derivative| ≥ 1 in j), by E_Q(ℓ) ≤ e_ℓ(W/Q) with e_ℓ(N) ≥ c√N for a
fixed c > 0; for |ℓ| < ℓ₁ any bound is allowed (e.g. Kusmin–Landau). Condition (iv) holds for every exponent-pair bound
(y/N² = |phase′| ≥ 1 and λ ≥ 1/2 give (y/N²)^κN^λ ≥ N^{1/2}) and for the second- and third-derivative tests (by AM–GM,
Nλ₂^{1/2} + λ₂^{−1/2} ≥ 2N^{1/2} and Nλ₃^{1/6} + N^{1/2}λ₃^{−1/6} ≥ 2N^{3/4}); in particular Theorem A's own proof is an
implementation.
**Proposition B2.** (a) No bound for the C-class sums that is uniform in 1 ≤ ℓ ≤ L (L ≥ 2N) beats √N/2. (b) For blocks
with W ≥ 2V/ξ₀ (ξ₀ = ξ₀(Φ) > 0 below; roughly γ ≥ β) and P ≥ P₁(Φ), every implementation of §4 gives a block bound
≫ max(V/P, P²W^{1/2}) ≥ V^{2/3}W^{1/6}, exponent (2β + γ/2)/3 — the Cor A″ value — and at the balanced block
U = V ≍ n^{1/4}, W ≍ n^{1/2} this is ≫ V ≍ n^{1/4}: **the trivial exponent; no implementation of §4 reaches the
balanced block, even granting square-root cancellation in every C-sum.**
*Proof.* (a) For any real x₁, …, x_N and L ≥ 2N − 1, with X_ℓ := Σ_j e(ℓx_j) and the Fejér kernel
F_L(t) = Σ_{|ℓ|≤L}(1 − |ℓ|/(L+1))e(ℓt) = (L+1)⁻¹|Σ_{m=0}^{L}e(mt)|² ≥ 0:
Σ_{|ℓ|≤L}(1 − |ℓ|/(L+1))|X_ℓ|² = Σ_{j,j′}F_L(x_j − x_{j′}) ≥ N(L+1). Removing ℓ = 0 (|X₀|² = N²) and using |X_{−ℓ}| = |X_ℓ|:
2Σ_{ℓ=1}^{L}|X_ℓ|² ≥ N(L+1) − N² ≥ N(L+1)/2, so max_{1≤ℓ≤L}|X_ℓ| ≥ (N/4)^{1/2}. (Here N = ⌊W/Q⌋ or ⌈W/Q⌉ is the number of
points x_j = −n/(4Q(c₀ + Qj)) of a C-class sum.)
(b) Fix Q = qq′ with 11 ≤ q < q′ and Q ≤ W. *Weights.* Φ̂(0) = ∫Φ ≥ 3, so |Φ̂(ξ)| ≥ 1 for |ξ| ≤ ξ₀ (ξ₀ > 0 depending only on Φ);
hence |a_ℓ(C)| ≥ V/(8QW) for 1 ≤ ℓ ≤ L₀ := ξ₀QW/V and all C ∈ (W, 2W]. *Kloosterman weights.* Call c mod Q good if
q ∤ c, q′ ∤ c, c ∉ D_q ∪ D_{q′}; at most 2q′ + 2q classes are bad, and Q − 2q − 2q′ ≥ Q/2 as (q − 4)(q′ − 4) ≥ 16. For good c,
|K_q(c)| = |K_{q′}(c)| = 1, so Lemma W gives |G_c(ℓ)| ≤ 4√Q for every ℓ; and Parseval gives Σ_{ℓ mod Q}|G_c(ℓ)|² =
Q·#{k mod Q : (f(c,k), Q) = 1} ≥ Q·(q − 2)(q′ − 2) ≥ Q²/2 (f(c,·) has ≤ 2 roots mod q). Hence Σ_{ℓ mod Q}Σ_{c good}|G_c(ℓ)| ≥
(Q/2)(Q²/2)/(4√Q) = Q^{5/2}/16, and any block of Q consecutive ℓ carries Σ_ℓΣ_{c₀}|G_{c₀}(ℓ)| ≥ Q^{5/2}/16.
*Assembly.* The implementation's dual bound is ≥ Σ_{ℓ₁≤ℓ≤L₀}(V/(8QW))Σ_{c₀}|G_{c₀}(ℓ)|·e_ℓ(W/Q). Since UVW < n/2 and
U ≥ 1/2, W < n/V, so ℓ₁ = 16W²/n < 16W/V ≤ L₀/2 once Q ≥ 32/ξ₀ (P ≥ P₁); and L₀ ≥ 2Q when W ≥ 2V/ξ₀. So [ℓ₁, L₀] contains
≥ L₀/(2Q) − 1 ≥ L₀/(4Q) disjoint blocks of Q consecutive integers, and the bound is ≥ (V/(8QW))·(L₀/(4Q))·(Q^{5/2}/16)·
c(W/Q − 1)^{1/2} ≫ Q·W^{1/2}. Its bound for S₁ is ≥ its ℓ = 0 term ≫ V. With Q > P² and P₀ ≤ P, the block bound is
≫ max(V/P, P²W^{1/2}) ≥ V^{2/3}W^{1/6}; at the balanced block W ≍ V² (≥ 2V/ξ₀ for n ≥ n₀) this is ≫ max(V/P, P²V) ≥ V. ∎
*Remarks.* (1) The truth is not the obstruction: in the balanced block at n ≈ 10¹⁶ (|𝒜| ≈ 3 400–3 600) the actual sums have
rms |S_Q| ≈ |𝒜|^{1/2} over 9 045 pairs q < q′ ∈ (1000, 2000] at a prime, an odd square and a near-square alike (§7.2); with
|S_Q| ≲ |𝒜|^{1/2+o(1)} for Q up to |𝒜| the sieve would give n^{1/8+o(1)} there. The loss is in (iii)–(iv): summing ℓ first
undoes Lemma P exactly (it returns the per-C sums, each with ≤ 1 term in the balanced block, since |J_C| ≍ V/W ≍ n^{−1/4}),
so any improvement must be a *joint* (ℓ, C) — i.e. bilinear — cancellation statement for Σ_{ℓ,C} G_C(ℓ)e(ℓn/(4CQ)).
(2) Exact reformulation (PROVED, k = m/C): S_Q = Σ_{m∈I} Σ_{C | m, W<C≤2W} Φ((4m − n)/V) χ_Q((4m − n)² − 4m/C), I an interval
of length ≍ V ≍ n^{1/4} at n/4: a χ_Q-twisted sum over the divisors near √m of the integers of an interval of length m^{1/4}.
Even the untwisted asymptotic for Σ_{x<m≤x+y}τ(m) is known only for y ≥ x^{θ+ε} with θ the Dirichlet-divisor exponent
(θ = 131/416 by Huxley 2003; Assessment, not re-verified in this lane), and here y = x^{1/4}.
(3) Averaging over the moduli (the sieve needs only P₀⁻²Σ_{q≠q′}|S_{qq′}|) does not help through the large sieve: the
values f(C,k) are |𝒜| ≍ V points of [1, 25V²] (density ≍ 1/V), and the quadratic large sieve (Heath-Brown, Acta Arith. 72
(1995)) bounds Σ_{Q~P²}|S_Q|² by ≈ (P² + V²)·|𝒜|, i.e. average |S_Q| ≲ V^{3/2}/P, worse than trivial (Assessment; the
large sieve does not see sparsity). This is the "square sieve + large sieve" option of the brief. (The Heath-Brown–Pierce
paper on class-number moments, arXiv:1409.3177, in fact uses the large sieve without the square sieve; LIT_CHECK item 6.)
(4) Off-diagonal (U ≪ V) the main term |𝒜|/P ≍ V/P exceeds the trivial min(U, W) unless V/U ≤ P — the sieve candidates
are all splittings of s ≍ V; no reparametrisation by the symmetric pair (u, B) reduces this (u, B are the only symmetric
pair of (★); fixing B or u gives linear equations).

## 6. The reverse direction: lower bounds and square-sensitivity (Theorem C)

The brief asks whether any *lower-bound* version of the square-sieve count — #{(C,k) ∈ strip : f(C,k) = □} from below —
can be square-sensitive (vanish at odd squares n = m², where R(m²) = 0). Answer (scoped): the square-sensitive ingredient
we identify is the Brauer–Manin twist (C1); Heath-Brown-type quadratic minorants cannot produce a lower bound from
upper-bound inputs (C3); the other named lower-bound routes reduce to B2 or closed items (C4). That no *other*
square-sensitive weight exists is not proved (Assessment).

**Theorem C1 (BM twist in strip coordinates; PROVED; content known for primes, `BM_CORRECTED_COUNT.md` Thm 1.1).**
Let n ≥ 3 be odd and (u, B, C) a (★) triple; x := 4Cu − 1, y := 4CB − 1. (i) (n/x) = −1 (Jacobi); in particular R(m²) = 0
(T1). (ii) If gcd(uBC, n) = 1 then (−uB/n) = −1. Hence every point (C, k) of the strip with f(C,k) a square and
gcd(Ck, n) = 1 lies in 𝒜⁻ := {(C,k) : (−k/n) = −1}, and 𝒜⁻ = ∅ when n is an odd square ((−k/m²) ∈ {0, 1}).
*Proof.* (i) xy = 4Cn + 1, so gcd(x, n) = 1 and 4Cn ≡ −1 (mod x); x ≡ 3 (mod 4), so (4Cn/x) = (−1/x) = −1. Write C = 2^a C′
with C′ odd. If a ≥ 1 then 8 | 4C | x + 1, so (2/x) = 1. By reciprocity (C′/x) = (x/C′)(−1)^{((C′−1)/2)((x−1)/2)}; since
x ≡ −1 (mod C′), (x/C′) = (−1/C′) = (−1)^{(C′−1)/2}, and (x − 1)/2 is odd, so (C′/x) = 1. Thus (C/x) = 1 and (n/x) = −1.
At n = m², (m²/x) = 1: contradiction. (ii) By reciprocity, (x/n) = (n/x)(−1)^{((n−1)/2)((x−1)/2)} = −(−1/n). Mod n, xy ≡ 1, so
x(x + 1)(y + 1) ≡ (x + 1)(1 + x) = (x + 1)²; gcd(x + 1, n) = gcd(4Cu, n) = 1, so (x/n) = ((x + 1)(y + 1)/n) = (16C²uB/n)
= (uB/n). Hence (−uB/n) = (−1/n)(x/n) = −1. ∎ *Check:* 87 388 coprime triples, odd n ≤ 20 000: no violation
(`data/z53/sqsieve/checks.txt`); in every computed strip all squares lie in 𝒜⁻ and |𝒜⁻| = 0 at odd squares (§7).

So a square-sensitive square sieve must carry the weight (1 − (−k/n))/2 — a character of conductor n, i.e. the BM layer,
whose main term is already free pointwise (FRONTIER §2.2, §4 item 13). The auxiliary characters (·/qq′) of the sieve have
conductor ≤ 4P² = n^{o(1)}-to-n^{0.06}; their complete sums (Lemma W) and the ℓ = 0 terms of S_Q depend on n only through
n mod Q and the block parameters (PROVED, by inspection of Lemma W and §4.4(i)). This is the closed "low-conductor
universality" phenomenon in strip form.

**Lemma C3 (square-sieve minorants have non-positive main coefficient; PROVED).** Let 𝒫 be a set of P₀ odd primes,
σ(a) := Σ_{q∈𝒫}(a/q), ν(a) := #{q ∈ 𝒫 : q | a}, w ≥ 0 finitely supported on ℤ∖{0} with ν(a) ≤ P₀ − 1 on supp w. Let
D(x) = a₀ + a₁x + a₂x² be a *minorant*: D(σ(a)) ≤ 1_□(a) for all a ∈ supp w. Assume (H) non-squares in supp w realise the
σ-values ±x₀ for some x₀ ≥ √P₀ and ±ε₀ for some ε₀ ∈ {0, 1}. Then a₀ + a₂(P₀ − ν(a)) ≤ 0 for all a ∈ supp w, and
  D⁺·Σ_{m≥1} w(m²) ≥ Σ_a w(a)D(σ(a)) = Σ_a w(a)(a₀ + a₂(P₀ − ν(a))) + a₁·Σ_{q∈𝒫}S_q + a₂·Σ_{q≠q′}S_{qq′},
  D⁺ := max(0, max_{□∈supp w} D(σ)), S_Q := Σ_a w(a)(a/Q),
so the first sum on the right is ≤ 0: **a positive lower bound must come entirely from a signed lower bound for
a₁·Σ_q S_q + a₂·Σ_{q≠q′}S_{qq′}** — the auxiliary character sums, which the upper-bound sieve only needs small in absolute value.
*Proof.* D(x) + D(−x) = 2(a₀ + a₂x²), and D ≤ 0 at σ-values of non-squares. If a₂ ≥ 0: a₀ + a₂(P₀ − ν) ≤ a₀ + a₂P₀ ≤
a₀ + a₂x₀² ≤ 0. If a₂ < 0: a₀ + a₂(P₀ − ν) ≤ a₀ + a₂ε₀² ≤ 0 since P₀ − ν ≥ 1 ≥ ε₀². The identity is σ(a)² = (P₀ − ν(a)) + Σ_{q≠q′}(a/qq′) summed
against w; the inequality is the minorant property (squares contribute ≤ D⁺ each, non-squares ≤ 0). ∎
(H) holds in every strip computed in §7 (with x₀ the least integer ≥ √P₀ with x₀ ≡ P₀ (mod 2), ε₀ ∈ {0, 1}: σ = 0, or both
σ = ±1, and both σ = ±x₀ are realised by non-squares; flag "(H):1" in all 14 runs, `strip_*.txt`; CERTIFIED for those runs).
*Reading (Assessment).* Heath-Brown's upper bound uses the majorant D = (2σ/P₀)², main coefficient ≈ 4/P₀ > 0; minorants
are forced to main coefficient ≤ 0. The signed combination would have to be shown ≥ (const)·P₀² at a prime and must be
≤ 0 at odd squares; each S_{qq′} is a sum of |𝒜| terms of square-root size (EVIDENCE §7), and each square contributes
≈ P₀² to Σ_{q≠q′}S_{qq′}, so the needed signed accuracy is o(1) per pair on average — the count itself.

**Falsifier F3 (EVIDENCE; `scripts/z53_sqsieve_lambda.py`).** Z := (Σ_𝒜 σ(f)² − P₀|𝒜|)/P₀² = #□·(1 − o(1)) + noise. Over 150
primes p ≡ 1 (24) and 150 odd squares near 10¹⁰ (cube strips, |𝒜| ≈ 1 300, P₀ = 10): sd(Z) = 4.86 (primes), 4.87 (squares)
vs the random model √(2|𝒜|)/P₀ = 5.11, while the mean square count is 0.41 (primes) and 0 (squares). The per-n signal
(≤ 1 per square) is buried in noise ≈ 5: the statistic does not separate primes from odd squares pointwise. Even the
n-average does not resolve the square contribution at this sample size: mean Z is −2.12 (primes) vs −3.07 (squares), a gap
of 0.94 ≈ 1.7 standard errors, but prime strips *without* squares already average −2.32, so most of the gap is not the
squares (and n-averages are excluded by B6/T7 anyway).

**Proposition C4 (the other lower-bound routes reduce to closed items; PROVED identities + pointers).**
(a) *Conic parametrisation.* For fixed C, f(C,k) = r² with s = 4Ck − n is C(s² − r²) = n + s, i.e.
(2Cs − 1)² − (2Cr)² = 4Cn + 1 with factor pair (2C(s − r) − 1, 2C(s + r) − 1) = (4Cu − 1, 4CB − 1): integral points of the conic
family are exactly the tied divisors d ≡ −1 (mod 4C) of the single integers 4Cn + 1 (FRONTIER §2.1 divisor form). A sieve
lower bound over the family is a lower bound for B2 itself.
(b) *Representation counts (Duke/Iwaniec type).* At each level 4C the generating series is an Eisenstein/theta quotient
with no cusp forms (`METAPLECTIC_ES.md` Thm K), so a "main term + cusp bound" route has nothing to bound and its main term is
the class-blind average; counting integral points of the quadric xy − 4nC = 1 with *fixed*-level congruences certifies the
tie only at ≤ τ(q²) heights (HYPSUMPROD Cor A′), and such counts are T1-blind (low-conductor universality).
**Verdict for (S3): closed for Heath-Brown-type quadratic σ-minorants (Lemma C3, PROVED under (H)); open otherwise.**
The square-sensitive ingredient identified is the BM twist (C1, conductor n); conic/representation lower bounds are B2 or
closed items (C4). Assessment: we see no route by which the square sieve's tie-detection could reach positivity, but this
is not a theorem.

## 7. Computations (scripts `scripts/z53_sqsieve_*`, data `data/z53/sqsieve/`, < 50 kB)

### 7.1 Lemma checks (CERTIFIED for the stated finite ranges)
* `z53_sqsieve_checks.py 23 20000`: Lemma W (a)–(c) for all odd primes q ≤ 23 and all (n, c, ℓ) mod q (27 962 cases; max
  |G|/√q = 1.931); Lemma W(d) (CRT factorisation) in 273 594 cases (Q ∈ {15, 35, 33, 77}, all c, ℓ mod Q, n over the even
  residues mod Q; max error 1.9·10⁻¹⁴) and the Kloosterman identity H = S(−d, −4̄ℓ²; q) of Lemma W(b) for all d, ℓ ≢ 0,
  q ≤ 17 (556 cases; max error 1.8·10⁻¹⁵); Lemma C1(ii) for all 87 388 (★) triples with odd n ≤ 20 000 and gcd(uBC, n) = 1 (0 violations; no triple
  at an odd square).
* `z53_sqsieve_poisson.py`: Lemma P with Gaussian Φ to ≤ 1.3·10⁻¹¹ (n = 1 000 003, 999 999 937, 998 001 = 999²,
  8 813 281).
* `z53_sqsieve_exponents.py`: exact rational vertex check of §4.5 (Thm A, A′ with Bourgain's pair, A″, and the (1/6, 2/3)
  exponent-pair form); `z53_sqsieve_reach.py`: diagonal reach (§5.1).

### 7.2 Strip statistics (EVIDENCE; `z53_sqsieve_strip.c`; columns: |𝒜|, squares, |𝒜⁻|, rms and max |S_Q| over pairs)

| n | type | block | P (P₀) | |𝒜| | □ | |𝒜⁻| | rms S_Q | max S_Q | √|𝒜| |
|---|---|---|---|---|---|---|---|---|---|
| 10 000 000 000 000 753 | prime ≡ 1 (24) | balanced, V = 10⁴, W = 6.25·10⁶ | 1000 (135) | 3 403 | 0 | 1 762 | 57.8 | 217 | 58.3 |
| 10 000 000 200 000 001 = (10⁸+1)² | odd square | same | 1000 (135) | 3 561 | 0 | 0 | 59.6 | 221 | 59.7 |
| 10 000 000 200 000 005 | near-square m² + 4 | same | 1000 (135) | 3 561 | 0 | 1 300 | 60.1 | 240 | 59.7 |
| 1 000 000 000 000 249 | prime ≡ 1 (24) | cube-type, W = 4·10⁴, s ∈ (5·10⁴, 4·10⁵] | 100 (21) | 60 681 | 0 | 30 303 | 233.5 | 673 | 246.3 |
| 1 000 000 025 191 729 = 31 622 777² | odd square | same | 100 (21) | 60 774 | 0 | 0 | 246.7 | 726 | 246.5 |
| 1 000 000 025 191 733 | near-square | same | 100 (21) | 60 773 | 0 | 30 081 | 253.5 | 710 | 246.5 |
| 8 813 281 | test prime (★ fails) | W = 100, s ∈ (150, 1200] | 50 (10) | 177 | 0 | 83 | 12.7 | 30 | 13.3 |
| 712 321 | test prime (★ fails) | W = 40, s ∈ (60, 500] | 30 (7) | 78 | 0 | 39 | 8.2 | 17 | 8.8 |
| 1 000 000 007 | prime | W = 300, s ∈ (500, 4000] | 50 (10) | 605 | 1 | 291 | 24.3 | 62 | 24.6 |
| 1 000 014 129 = 31 623² | odd square | same | 50 (10) | 603 | 0 | 0 | 29.5 | 72 | 24.6 |

(P = 100 runs of the balanced block: `strip_balanced.txt`.) All squares found lie in 𝒜⁻; |𝒜⁻| = 0 at odd squares (C1);
rms |S_Q| ≈ √|𝒜| everywhere, including the balanced block (Prop B2 Remark 1): the character sums are T1-blind and
square-root size, exactly as an n-uniform upper-bound input must be. (H) of Lemma C3 holds in every run.

### 7.3 Falsifier F3 (EVIDENCE): see §6 (`lambda_falsifier.txt`).

## 8. FRONTIER §4 hard screens (for Theorem A and for the reverse-direction question)
1. **T1 (odd squares).** Theorem A is an n-uniform upper bound, true at m² (R = 0); it does not and cannot imply positivity.
   For the reverse direction, T1 is located in strip coordinates: the square-sensitive ingredient identified is the BM
   twist (Theorem C1); the auxiliary-conductor sums S_Q behave the same at odd squares, near-squares, test primes and
   primes (EVIDENCE §7.2, F3).
2. **8/131.** The upper-bound argument transfers to other numerators (it uses only the root structure of (u, B) and a
   linear relation level·k ↔ s): harmless for an upper bound; silent on 8/131.
3. **Tied modulus.** Used, as in HYPSUMPROD: the tie is the square condition; the moving modulus 4C is absorbed into the
   strip, and only fixed auxiliary moduli Q appear. The new step is cancellation in the *k*-direction via complete
   Kloosterman sums, not a tie-breaking lower bound (B2 untouched).
4. **Fixed p.** Passed: pointwise in n; averages only over C, k (within the strip), ℓ, and the auxiliary primes.

## 9. Verdict
* **(S1) strengthened.** R(n) ≪_ε n^{12/37+ε} for every n (Theorem A; PROVED relative to Weil's Kloosterman bound and the
  third-derivative test); n^{21/65+ε} relative to Bourgain's exponent pair (Thm A′); n^{4/13+ε} under the exponent-pair
  conjecture (Cor A″). The saving over p^{1/3} grows from 1/225 ≈ 0.0044 to 1/111 ≈ 0.0090 (2/195 ≈ 0.0103 with Bourgain).
  The cube block drops from n^{8/25}(log n)² to n^{17/54+ε}. What it buys: the FRONTIER error benchmark |E(p)| ≪ p^{θ} improves to
  θ = 12/37 + ε. What it does not buy: anything about positivity.
* **(S2) narrowed.** Exact reach of the bound (§5.1); no implementation of the k-Poisson square sieve reaches the balanced
  block, even with square-root cancellation in every C-sum (Prop B2, PROVED for the specified class); the truth (rms |S_Q|
  ≈ |𝒜|^{1/2}) is fine, so what is missing is a bilinear (ℓ, C) cancellation estimate — or, equivalently, χ_Q-twisted
  divisor sums over divisors near √m of integers in an interval of length m^{1/4}.
* **(S3) narrowed: closed for quadratic σ-minorants, open otherwise.** Heath-Brown-type quadratic minorants have
  non-positive main coefficient (Lemma C3, PROVED under (H)), so a lower bound would need signed estimates of the
  auxiliary sums; the square-sensitive ingredient identified is the BM twist (C1); conic/representation-count lower bounds
  are B2 or closed items (C4). EVIDENCE F3: the detection statistic does not separate primes from odd squares pointwise.
  Assessment (not a theorem): no route from the square sieve's tie-detection to positivity is visible.

## 10. Proposed FRONTIER §7 text (do NOT edit FRONTIER here)
Append to §7.1:
> *(z53, `Z53_SQSIEVE.md`; internal.)* **Square-sieve exponent improved to 12/37.** Smoothing the strip in s and applying
> Poisson in k *inside* each C turns the χ_{qq′}-twist into complete Kloosterman sums (size √Q) times exponential sums
> Σ_{C≡c₀ (Q)} e(ℓn/(4CQ)); with the third-derivative test and per-block optimisation, R(n) ≪ n^{12/37+ε} for every n
> (worst block (α, β, γ) = (12/37, 13/37, 12/37); cube n^{17/54+ε}); n^{21/65+ε} with Bourgain's exponent pair; n^{4/13+ε}
> under the exponent-pair conjecture. Reach: no k-Poisson implementation reaches the balanced block, even with square-root
> C-sums (the truth is square-root; a bilinear (ℓ, C) estimate would be needed). Reverse direction: Heath-Brown-type
> quadratic minorants have non-positive main coefficient (Lemma C3), so any lower bound must come from signed estimates of
> the auxiliary character sums; the only square-sensitive ingredient identified is the BM twist (−uB/n) = −1; conic /
> representation lower bounds are B2. (Internal, unrefereed; the k-Poisson step is the standard square-sieve technique,
> new here only in its application to this strip; no predecessor found in a literature search.)
In §3 ("Tied modulus") and §2.2 replace "p^{1/3−1/225+o(1)}" by "p^{12/37+o(1)} (z53 SQSIEVE; p^{21/65+o(1)} relative to
Bourgain's exponent pair)". In §6 add: "square-sieve lower bounds via quadratic minorants → main coefficient ≤ 0 (signed
auxiliary-sum estimates needed); square-sensitive ingredient identified: the BM twist → `Z53_SQSIEVE` §6".

## 11. Bottom line
The square sieve on the tied hyperbola has more in it than HYPSUMPROD extracted: opening the character in the k-variable
by Poisson summation, inside each fixed C, produces complete Kloosterman sums of square-root size, and the remaining
exponential sums in C are classical. This proves R(n) ≪ n^{12/37+ε} for every n (n^{21/65+ε} with Bourgain's exponent pair,
n^{4/13+ε} conditionally). The route stops short of the balanced block u, B ≍ p^{1/4} for a structural reason, even with
square-root C-sums: summing the dual frequencies first undoes the Poisson step, and the strip there has ≤ 1 point per C.
In the reverse direction the square sieve is one-sided in a precise sense — every quadratic minorant has a non-positive
main coefficient — and the square-sensitive ingredient we can identify is the Brauer–Manin twist. Our assessment (not a
theorem) is that the square sieve can keep improving the error benchmark but gives no visible route to positivity. ES
remains open.

## 12. Reproduction
```
cd $REPO
ulimit -v 4000000; timeout 900 uv run --with sympy python scripts/z53_sqsieve_checks.py 23 20000        # ~1 min
for a in "1000003 3 5 90 130 100" "999999937 7 11 900 1100 1000" "998001 3 7 90 120 100" "8813281 5 13 180 230 200"; do
  timeout 600 uv run --with sympy python scripts/z53_sqsieve_poisson.py $a; done
timeout 60 uv run python scripts/z53_sqsieve_exponents.py; timeout 300 uv run python scripts/z53_sqsieve_reach.py
gcc -O2 -o /tmp/z53strip scripts/z53_sqsieve_strip.c -lm
ulimit -v 3000000; timeout 900 /tmp/z53strip 10000000000000753 6250000 20000 40000 1000     # balanced block, ~1 min
timeout 900 /tmp/z53strip 1000000000000249 40000 50000 400000 100                            # cube-type, ~1 min
timeout 1500 uv run --with sympy python scripts/z53_sqsieve_lambda.py /tmp/z53strip 1e10 150 40   # F3, ~5 min
```

## 13. Review log
**Hostile review 1** (deep-mode subagent; `reviews/z53_sqsieve_review1.md`). Verdict **CORRECT WITH FIXES**; no FATAL issue.
It re-derived every power in Lemma 1′, Lemma W (including the Kloosterman reduction and the CRT factorisation, checked
numerically in 92 409 + all q ≤ 17 cases), Lemma P, Prop D and §4.5; independently recomputed with exact arithmetic the
exponents 12/37, 17/54, 21/65, 4/13 (θ = 4/(13 − 4κ)), the worst block (12/37, 13/37, 12/37), all §5.1 endpoints, and
reproduced the scripts and two strips byte-for-byte. Fixes applied:
* F1 (MAJOR): Prop B2's implementation class (iv) required ℓ-uniform bounds, which excluded Theorem A's own proof; now (iv)
  asks e_ℓ(N) ≥ c√N only for |ℓ| ≥ 16W²/n (satisfied by exponent pairs and the 2nd/3rd-derivative tests), (a) is stated
  for ℓ-uniform bounds, and (b) sums over [ℓ₁, L₀].
* F2 (MAJOR): overclaims on (S3) removed ("dead", "only through BM", "cannot touch positivity"): (S3) is now "closed for
  quadratic σ-minorants (PROVED under (H)); open otherwise", with the no-route statement labelled Assessment (§1, §6, §9,
  §10, §11).
* F3: hypothesis (H) is now checked exactly (σ = 0 or both σ = ±1, and both ±x₀) — flag (H):1 in all 14 strip runs
  (rerun; S_Q columns byte-identical); x₀ wording fixed.
* F4: the F3 n-average reading corrected (gap 0.94 ≈ 1.7 s.e., mostly not the squares).
* F5: B2(b) now assumes W ≥ 2V/ξ₀ and P ≥ P₁.
* F6: Theorem A′ — κ < 1/4; y ≥ N² justified by γ < 1/2; boundary term peeled; Bourgain instance labelled conditional on the
  (sketched) literature result.
* F7, F8, F9: §1 aligned with §6/§9; Q ≤ W in Prop D not needed; C3 coefficients renamed a₀, a₁, a₂; HYPSUMPROD cube bound
  carries (log n)²; Lemma P holds for Schwartz Φ; CRT and Kloosterman checks added to `z53_sqsieve_checks.py`; timings.
