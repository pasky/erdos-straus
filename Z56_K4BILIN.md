# Z56_K4BILIN — Type II / bilinear attack on K(4) = P(4,15)

**ES is OPEN.** Nothing here proves or disproves it. All results are internal (internally reviewed only).
Lane K4BILIN (wave z56). Scripts `scripts/z56_k4bilin_*`, data `data/z56/k4bilin/`. Revised after a hostile internal
review (`data/z56/k4bilin/internal_review.md`, §10), which found one FATAL error in the first draft (a false Type II
hypothesis); it is withdrawn and turned into Lemma N below.

Notation (as in `Z54_HCKILL.md`, `Z55_P415.md`): 𝒬 = {primes ≡ 3 (mod 4)}; S = {n ≥ 1 : every prime factor ≡ 1 (mod 4)};
χ = χ₋₄; r(N) = #{(a, b) ∈ ℤ² : a² + b² = N}; r\*(N) = #{(a, b) : a² + b² = N, gcd(a, b) = 1}; N₁ = n + 4, N₂ = 4n + 1, so
4N₁ − N₂ = 15. ω, Ω: number of distinct / all prime factors. For a prime ℓ ∤ 30, "the shift classes mod ℓ" are
n ≡ −4 and n ≡ −4̄ := −(4⁻¹) (mod ℓ) (where ℓ | N₁, resp. ℓ | N₂; distinct as ℓ ∤ 15). Fix the class n₀ = 97 (mod 120):
then n ≡ 1 (8), n ≡ 1 (3), n ≡ 2 (5), N₁ ≡ 101, N₂ ≡ 29 (mod 120), so (nN₁N₂, 30) = 1. Put
  **a\*_n := r\*(n + 4)·r\*(4n + 1)·1[n ≡ 97 (mod 120)],   A\*_d(x) := Σ_{n ≤ x, d | n} a\*_n.**
For odd N ≡ 1 (mod 4): r\*(N) > 0 ⟺ N ∈ S, and then r\*(N) = 4·2^{ω(N)}. So a\*_n = 16·2^{ω(N₁)+ω(N₂)}·1_S(N₁)1_S(N₂) on
the class, and **a\*_p > 0 for a prime p ⟺ p is a P(4,15) prime in the class 97 (mod 120).**

## 0. Verdict: **narrowed** (no unconditional K(4)); one unconditional "dual" theorem; the Type II target corrected

1. **Lemma T\* (PROVED, relative to FI 2009 Lemma 4.1 = Smith's theorem on r in progressions).** (a\*_n) has level of
   distribution x^{1/6−ε} (any fixed ε > 0) for all moduli d coprime to 30, with the explicit density
   g̃(d) = d⁻¹∏_{ℓ | d} ℓ/(ℓ + 2χ(ℓ)), i.e. g\*(ℓ) = 1/(ℓ + 2χ(ℓ)) at primes. (det-15, S-refined analogue of FI 2009
   Lemma 4.2 / Sedunova's Lemma 2 for det 1.)
2. **Proposition P (PROVED: Lemma T\* + linear β-sieve + Shiu-type mean value bound).** #{n ≤ x : n ≡ 97 (120),
   n + 4 ∈ S, 4n + 1 ∈ S, Ω(n) ≤ 12} ≫ x/(log x)⁹. Dual of P415 Theorem U (there: p prime, one shift exact, the other
   of bounded 𝒬-anatomy; here: both shifts exact, n only a P₁₂). No ES content (n not required to be prime). P415 Prop C
   already had P₂ values with both shifts in S on a thin quadratic family (≫ √x/log x); the new feature is the
   near-linear count and the explicit S-weighted distribution law, not a first almost-prime version.
3. **Lemma N (PROVED; negative; found by the internal review for ℓ = 7).** a\* is *not* locally multiplicative in n:
   it vanishes on the shift classes of every inert ℓ and is doubled-weight on those of every split ℓ. Hence the
   natural multiplicative comparison model fails every Type II hypothesis with logarithmic saving (explicit 0/1
   coefficients force mn ≡ −4 (mod ℓ)); more generally any comparison model must carry the residue information of
   every inert prime ℓ ≤ (log x)^{A/2}/(log log x) if a saving (log x)^{−A} is required. The first draft's (TII\*) was
   false for this reason and is withdrawn.
4. **Route D — the corrected missing estimate (§4, CONDITIONAL / Assessment).** The natural target is (TII_W): Type II
   smallness of a\* − λν_W on m ∈ (x^{1/6−5ε}, x^{2/3−5ε}), where ν_W is the W-tricked local model (all shift-class
   information at primes ℓ < W = (log x)^{B}). Theorem V′ (CONDITIONAL; implication given in outline): (TII_W) ⟹
   P(4,15). Cauchy–Schwarz (Prop D, a *sufficient* strategy, not a necessity) converts (TII_W) into one-variable
   four-fold r\*-correlations with W-local singular series plus twisted Type I to level ≈ the smaller factor; no
   applicable estimate of either kind was found (coverage-limited).
5. **Route P — prime-variable bilinear input (§5).** In the Friedlander–Iwaniec architecture with the full hyperbola
   range k ≤ √x on the exact shift and the semi-linear lower sieve sifting past x^{1/4} on the other, the total modulus
   level is 1/2 + θ_D with θ_D > 1/4: **budget > 3/4 for this architecture** (elementary bookkeeping, not a barrier for
   other methods). Model sufficient levels 0.757 (ideal switching) … ≈ 1.0; 0.908 in P415's GEH-switched model (P415's
   product-linear sieve: 0.976 in that model, 0.996 under ordinary EH) — model-to-model comparisons, not theorems.
   Dispersion results: 66/107 ≈ 0.617 for a single fixed residue with triply well-factorable weights (Lichtman; tag
   ABSTRACT-ONLY in the lit report), 1/2 + δ (δ tiny) for factor-dependent residues with a conveniently sized factor
   (Maynard III Thm 1.2, VERIFIED). Gap ≥ 57/428 ≈ 0.133 even against the fixed-residue level.
6. **Route S (§4.4, Assessment).** The dispersion attempt at Type II for the S-sieve on 4p + 1 leads to averaged binary
   prime correlations along m ↦ (mn_i − 1)/4 — twin-prime-type. A diagnosis of that attempt, not an impossibility proof.
7. **Diagnostics (§6; integer counts exact, ratios floating point).** To 10¹⁰ the a\*-mass of primes, of P₂ = pq in each
   0.05-band of log p/log x for log p/log x ∈ [0.05, 0.5), of Ω = 3, of n ∈ S and of λ(n) = ±1 matches the
   multiplicative model to within 0.4 % (most within 0.1 %); FI's bilinear quantity (B) (γ ≡ 1) shows random-sign
   cancellation for a, a\*, 1_S-pairs once the inner sums are long, and none for Selberg's control a(1 + λ). These are
   tests with coefficients equidistributed modulo small primes; by Lemma N they *cannot* validate an all-coefficient
   Type II statement — they only show no global (non-local) bias at these scales.

**Bottom line (Assessment).** K(4) is a level problem in the prime variable (solved under EH(θ₀), HCKILL Thm E) and a
Type II problem in the dense variable (a\* has level x^{1/6} unconditionally and gives P₁₂, Prop P). In the dense
formulation the Type II target must be W-tricked (Lemma N); in that form it is the natural pseudorandomness statement
and is consistent with all diagnostics, but no available method addresses it. In the prime formulation the FI
architecture needs > 3/4 for primes in CRT-mixed classes; known bilinear results stop at ≈ 0.617 (single residue).

## 1. Statements attacked; why not closed

* **P(4,15)** (OPEN; = K(4) by HCKILL Lemma 1.1, PROVED): infinitely many primes p ≡ 1 (8) with p + 4, 4p + 1 ∈ S.
* **Route D (dense sequence).** Detect primes inside (a\*_n) (mean ≍ 1). Lane task: prove the Type I side, state the
  missing Type II estimate, test it.
* **Route P (prime variable).** HCKILL Thm E / FI 2009 / P415 §2 sieve primes by N₁, N₂; level > 1/2 for primes comes
  from bilinear (dispersion) methods. Lane task: level needed by the best architecture vs what dispersion gives.
* **Route S.** Type II for the semi-linear sieve itself ("swap roles").

**Why not closed.** P415 proved Theorem U and a ledger for the vector / product-linear sieves; it did not treat the
dense-sequence formulation, the FI architecture's budget, or the actual bilinear inputs. Nothing here is in FRONTIER §6
or the closed list. Literature: `data/z56/k4bilin/lit_report.md` (research subagent; tags VERIFIED / VERIFIED-2nd /
ABSTRACT-ONLY / UNVERIFIED per claim); I read Friedlander–Iwaniec, "Asymptotic sieve for primes" (arXiv math/9811186:
Theorem 1, hypotheses (R), (R1), (B), (B1)–(B3)) and the FI 2009 text (`sources/window2/fi09-hyperbolic-pnt.txt`).

## 2. Lemma T\*: Type I for the dense sequence

**Input (Smith; FI 2009 Lemma 4.1, read in the published text).** For (c, q) = 1 and y ≥ q,
  Σ_{m ≤ y, m ≡ c (q)} r(m) = (πy/q)∏_{p | q}(1 − χ(p)/p)·ε(c, q) + O_ε(q^{−1/2} y^{2/3+ε}),
ε(c, q) = 1 if 4 ∤ q, ε(c, q) = 1 + χ(c) if 4 | q. (FI state it for (a, q) = 1 without a range and add "this gives the
asymptotic within the range q < x^{2/3−ε}"; it cannot hold uniformly for y < q — e.g. y = 1, c = 1 — so we use it only
for y ≥ q, and for 0 < y < q we bound the sum trivially: at most one term, O(y^{ε}).)

**Lemma T\* (PROVED relative to the input).** There is c\* > 0 such that for every d ≥ 1 with (d, 30) = 1, every fixed
η > 0 small, and x ≥ 2,
  A\*_d(x) = g̃(d)·c\*x + r\*_d(x),   g̃(d) = d⁻¹∏_{ℓ | d} ℓ/(ℓ + 2χ(ℓ)),
  |r\*_d(x)| ≪_η d^{−1/2}x^{11/12+η} + x^{1−3η}/d + x^{1/2+10η}   for d ≤ x^{1/6},
and A\*_d = 0 if (d, 30) > 1. (For d > x^{1/6} only the trivial A\*_d ≪ (x/d + 1)x^{η} is used.) Consequently, for every
fixed ε > 0 (with η = ε/10), Σ_{d ≤ D, (d,30)=1} |r\*_d(x)| ≪ x^{1−η} for D = x^{1/6−ε}: level x^{1/6−ε}.

*Proof.* (i) *Expansion.* r(N) = Σ_{g² | N} r\*(N/g²) (split a representation by its gcd), so r\*(N) = Σ_{e² | N} μ(e)r(N/e²)
and a\*_n = Σ_{e₁² | N₁, e₂² | N₂} μ(e₁)μ(e₂) r(N₁/e₁²) r(N₂/e₂²). On the class, (N₁, N₂) = 1 and (N₁N₂, 30) = 1, so
(e₁, e₂) = 1, (e₁e₂, 30) = 1; if d | n then (d, N₁N₂) = 1, so (d, e₁e₂) = 1. All r-values are ≪ x^{η/4}; the number of
pairs (e₁, e₂) attached to one n is ≤ τ(N₁)τ(N₂) ≪ x^{η/4}.

(ii) *Tail e₁e₂ > E := x^{8η}.* Then e₁ > √E or e₂ > √E; by CRT ((d, e_i) = 1) the number of n ≤ x with d | n and
e₁² | N₁ is ≤ x/(de₁²) + 1 (similarly for e₂). The tail contributes ≪ x^{η}Σ_{√E < e ≤ √(4x+1)}(x/(de²) + 1)
≪ x^{1+η}/(d√E) + x^{1/2+η} = x^{1−3η}/d + x^{1/2+η}.

(iii) *Small e: open r(N₂/e₂²).* Fix e₁e₂ ≤ E; u = N₁/e₁², v = N₂/e₂². Here v ≡ 5 (mod 8) (e₂² ≡ 1 (8)), so v is never a
square and FI 2009 (3.1)/(4.5) gives r(v) = 8Σ_{kl = v, k < √v} χ(k). The (e₁, e₂)-term of A\*_d is
  8 Σ_{k < √(4x+1)/e₂} χ(k) Σ_u r(u),   (k²e₂² + 15)/(4e₁²) < u ≤ (x + 4)/e₁²,
  u ≡ 4ē₁² (mod d),  4e₁²u ≡ 15 (mod e₂²k),  e₁²u ≡ 101 (mod 120)
(d | n = e₁²u − 4; e₂²k | N₂ = 4e₁²u − 15; n ≡ 97 (120)). Here k | v, so (k, 30de₁) = 1 (a common prime of k and e₁ would
divide (N₁, N₂) = 1); k and e₂ may share primes. The moduli d, e₂²k, 120 are pairwise coprime and the three residues
are units, so u runs over one reduced class c mod q = 120·d·e₂²·k, with 8 | q and χ(c) = χ(101) = 1. Upper endpoint:
q ≪ d·E·√x ≤ x^{2/3+8η} < (x + 4)/e₁² (as e₁² ≤ E), so the input applies there. Lower endpoint y₀ = (k²e₂² + 15)/(4e₁²):
if y₀ ≥ q use the input, else the trivial O(x^{η}) (main term at y₀ < q is O(1) as well). Errors:
  Σ_{e₁e₂≤E} Σ_{k ≤ 2√x/e₂} [(120de₂²k)^{−1/2}(x/e₁²)^{2/3+η} + x^{η}] ≪ d^{−1/2}x^{11/12+η}Σ e₁^{−4/3}e₂^{−3/2} + x^{1/2+η}E
  ≪ d^{−1/2}x^{11/12+η} + x^{1/2+9η}.
Summed over d ≤ x^{1/6−ε}: ≪ x^{1−ε/2+η} + x^{2/3+9η}.

(iv) *Main term.* The input's main terms are 8χ(k)·(2π/q)∏_{p | q}(1 − χ(p)/p)·((x + 4)/e₁² − y₀). Write
h(k) = ∏_{p | k, p ∤ e₂}(1 − χ(p)/p) = Σ_{b | k} ν(b), ν squarefree-supported, |ν(p)| ≤ 1/p. By inclusion–exclusion
|Σ_{k ≤ K, (k,30de₁)=1} χ(k)| ≤ 2^{ω(30de₁)}, hence Σ_{k ≤ K, (k, 30de₁) = 1} χ(k)h(k) ≪ x^{η}log 2K and, by partial summation,
Σ_{k≤K} χ(k)h(k)k ≪ K x^{η}. Therefore, for fixed (e₁, e₂): the y₀-part (∝ k²/k) is ≪ x^{1/2+η}/(d e₁² e₂) and completing
the k-series to k > 2√x/e₂ costs ≪ x^{1/2+η}/(d e₁² e₂). Summing over e₁e₂ ≤ E: ≪ x^{1/2+2η}/d. Completing the e-sums costs
≪ x^{1+η}·Σ_{e₁e₂ > E}(e₁e₂)^{−2}/d ≪ x^{1−7η}/d. The completed main term is
  c₁·(x/d)∏_{p | d}(1 − χ(p)/p)·Σ_{e₁,e₂,k}^{(coprimality as above)} μ(e₁)μ(e₂)χ(k)/(e₁²e₂²k)·∏_{p | e₂k, p ∤ d}(1 − χ(p)/p),
which factors over primes (absolutely in e₁, e₂; the k-part is L(1, χ)-type, summed in the usual order, as in FI).
At ℓ | d the local factor is ℓ^{−j}(1 − χ(ℓ)/ℓ) for ℓ^j ∥ d (no e, k at ℓ). At ℓ ∤ 30d it is
  E_ℓ = [e₁ = e₂ = 1: 1 + Σ_{j≥1}χ(ℓ)^jℓ^{−j}(1 − χ(ℓ)/ℓ) = 1 + χ(ℓ)/ℓ] + [e₁ = ℓ (so ℓ ∤ k): −ℓ^{−2}]
      + [e₂ = ℓ, any power of ℓ in k: −ℓ^{−2}(1 − χ(ℓ)/ℓ)Σ_{j≥0}χ(ℓ)^jℓ^{−j} = −ℓ^{−2}] = 1 + χ(ℓ)/ℓ − 2/ℓ².
Hence main = c\*x·∏_{ℓ^j ∥ d} ℓ^{−j}(1 − χ(ℓ)/ℓ)/E_ℓ, and (ℓ − χ)/(ℓ² + χℓ − 2) = 1/(ℓ + 2χ) for χ = ±1 ((ℓ² + ℓ − 2) =
(ℓ − 1)(ℓ + 2), (ℓ² − ℓ − 2) = (ℓ + 1)(ℓ − 2)), giving g̃(d). Positivity: c\* = C₁∏_{ℓ≥7}E_ℓ with C₁ > 0 (the factors at
2, 3, 5 from q), E_ℓ = (1 + χ(ℓ)/ℓ)(1 − 2/(ℓ² + χ(ℓ)ℓ)); the second product converges absolutely with positive factors;
the first, in the usual order, is ∏_{p odd}(1 + χ(p)/p)/((2/3)(6/5)) with ∏_{p odd}(1 + χ(p)/p) = L(1, χ)∏_{p odd}(1 − p^{−2})
= (π/4)(8/π²) = 2/π. ∎

*Checks.* The internal review re-derived E_ℓ, verified the identity symbolically and enumerated residues mod 7, …, 31
(shift class of an inert prime weight 0, of a split prime weight 2, else 1) recovering P(ℓ | n) = 1/(ℓ + 2χ(ℓ)) exactly.
Numerically (`spectrum_1e10.txt`) Σ_{ℓ|n}a\*_n/Σa\*_n = 0.20009, 0.11111, 0.06669, 0.05258, 0.05879, 0.04761, 0.03229,
0.03447 for ℓ = 7, 11, …, 31 vs 1/(ℓ + 2χ(ℓ)) = 0.20000, 0.11111, 0.06667, 0.05263, 0.05882, 0.04762, 0.03226, 0.03448.
*Remark.* The exponent 1/6 is FI's/Sedunova's: the individual Weil-quality error summed over k < √x (Sedunova
arXiv:2609.28200 Lemma 2 and Remark 1, per the lit report). Beyond it needs averaging of the AP errors over k
(Kloosterman/spectral; the divisor analogue in one fixed progression reaches X^{0.281}, Grimmelt–Merikoski
arXiv:2404.08502 Cor. 1.3; nothing comparable was found for r).

## 3. Proposition P (unconditional dual of Theorem U)

**Proposition P (PROVED relative to: Lemma T\*; the linear (κ = 1, β = 2) Rosser–Iwaniec lower bound, as quoted in
Nath–Xie arXiv:2501.16723 (3.4)/Lemma 3.6 and used in HCKILL Thm E Step 2; the Shiu/Halberstam–Richert mean-value upper
bound for nonnegative multiplicative functions).** For x ≥ x₀,
  #{n ≤ x : n ≡ 97 (mod 120), n + 4 ∈ S, 4n + 1 ∈ S, Ω(n) ≤ 12} ≫ x/(log x)⁹,
and every n counted has all prime factors > x^{1/13}.

*Proof.* Sift (a\*_n)_{n≤x} by the primes ℓ ≥ 7 (2, 3, 5 never divide n). Fix 0 < ε < 1/780, D = x^{1/6−ε}; Lemma T\*
gives Σ_{d < D, d | P(z)}|r\*_d| ≪ x^{1−ε/10}, and g\*(ℓ) = 1/ℓ + O(1/ℓ²) < 1 satisfies the dimension-one product axiom
∏_{w≤ℓ<z}(1 − g\*(ℓ))^{−1} ≤ (log z/log w)(1 + K/log w). With s = 2.1, z = D^{1/s}: S(𝒜\*, z) ≥ c\*x·V(z)(f(s) − o(1)) −
Σ|r\*_d|, f(s) = 2e^γ log(s − 1)/s, f(2.1) = 0.16167… > 0, V(z) ≍ 1/log x; so Σ_{n ≤ x, (n, P(z)) = 1} a\*_n ≫ x/log x.
As ε < 1/780, (1/6 − ε)/2.1 > 1/13, so z > x^{1/13} and Ω(n) ≤ 12 for every sifted n ≤ x (multiplicity counted; n need not
be squarefree). a\*_n > 0 means N₁, N₂ ∈ S. Count: a\*_n² = 256·4^{ω(N₁)+ω(N₂)}1_S(N₁)1_S(N₂) ≤ 128[16^{ω(N₁)}1_S(N₁) +
16^{ω(N₂)}1_S(N₂)], and Σ_{m ≤ 4x+1}16^{ω(m)}1_S(m) ≪ x(log x)^{16/2−1} = x(log x)⁷ (value 16 on primes ≡ 1 (4), 0 on 𝒬).
Cauchy–Schwarz: #{sifted n with a\*_n > 0} ≥ (Σa\*)²/Σa\*² ≫ (x/log x)²/(x(log x)⁷). ∎

*Remarks.* (1) Sedunova's Thm 2 (det 1, r(n−2)r(n+2), squarefree n, weighted count, ω(n) ≤ 7) is the closest analogue;
the statements are not directly comparable. A Richert-weighted version should lower 12 (Assessment, not done).
(2) Duality: Theorem U keeps primality and one exact shift; Prop P keeps both shifts exact and loses primality to P₁₂.
(3) (Assessment) By the parity principle, Type I information alone is not expected to separate Ω(n) = 1 from Ω(n)
even; the Selberg-type sequence a\*(1 + λ) has no primes and, heuristically, the same Type I data up to a factor.

## 4. Route D: what Type II information is needed

### 4.1 Lemma N (PROVED): a\* has local Type II structure; the multiplicative model fails

Let w_n := f(n)·1[n ≡ 97 (120)], f multiplicative with f(ℓ^e) = c_ℓ := (ℓ − 1)/(ℓ − 1 + 2χ(ℓ)) (ℓ ≥ 7, e ≥ 1). Its
divisibility densities equal those of a\* (W_d = g̃(d)W + O(x^{η}) by f = 1 ∗ h, h(ℓ) = c_ℓ − 1 = O(1/ℓ)), and Σa\*/Σw
→ λ₀ ∈ (0, ∞) (numerically 35.07).

**Lemma N.** Let ℓ ≥ 7 be a prime ≡ 3 (mod 4), M = x^{1/3}, N = x/(4M), b ≡ 97 (mod 120) with b ≡ −4 (mod ℓ), and
α_m = 1[M < m ≤ 2M, m ≡ 1 (mod 120ℓ)], β_n = 1[N < n ≤ 2N, n ≡ b (mod 120ℓ)]. Then a\*_{mn} = 0 for all these pairs, while
Σ_{m,n} α_m β_n w_{mn} ≫ x/(ℓ²(log log x)²). Consequently for any fixed λ > 0 the Type II sum Σ αβ(a\* − λw) is
≪ −x/(ℓ²(log log x)²), and no Type II estimate with saving (log x)^{−A} (A > 0) holds for a\* − λw. The same holds for
any comparison model ν with ν(t) ≫ (log log x)^{−2} on t ≡ −4 (mod ℓ), t ≡ 97 (120), for every inert
ℓ ≤ (log x)^{A/2}/(log log x)^2.

*Proof.* mn ≡ 97 (120) and mn ≡ −4 (mod ℓ), so ℓ | N₁ = mn + 4 with ℓ ∈ 𝒬, hence N₁ ∉ S and a\*_{mn} = 0; mn ≤ 4MN = x.
The number of pairs is ≍ MN/(120ℓ)² ≍ x/ℓ². Since c_p ≥ (p − 1)/(p + 1) ≥ (1 − 1/p)², f(t) ≥ (φ(t)/t)² ≫ (log log x)^{−2}. ∎

(First found by the internal review for ℓ = 7, which also checked it numerically: at x = 10⁹, M = 3000, N = 83 333,
396 such pairs carry a\*-mass exactly 0 and model mass 404.8.) **Reading.** A shift-defined sequence carries forbidden
(inert ℓ) and doubled (split ℓ) residue classes modulo every prime; Type II comparisons with arbitrary divisor-bounded
coefficients see them. This is a local obstruction to a *formulation*, not to K(4).

### 4.2 The corrected target (TII_W) and Theorem V′ (CONDITIONAL; implication in outline)

Local densities: for ℓ ≥ 7 inert, δ_ℓ(c) = 0 on the two shift classes and ℓ/(ℓ − 2) elsewhere; for ℓ split, δ_ℓ(c) =
2ℓ/(ℓ + 2) on the shift classes and ℓ/(ℓ + 2) elsewhere (mean 1 over ℤ/ℓ; δ_ℓ(0)/ℓ = g\*(ℓ)). Formally a\* is
proportional to ∏_ℓ δ_ℓ(n mod ℓ) — it is "entirely local", and pseudorandomness can only mean agreement with a
truncated product. For W ≥ 7 put
  ν_W(n) := 1[n ≡ 97 (120)]·∏_{7 ≤ ℓ < W} δ_ℓ(n mod ℓ)·∏_{ℓ ≥ W, ℓ | n} c_ℓ.
**(TII_W)** For W = (log x)^{B}, α = 1/6 − 5ε and all |α_m| ≤ τ(m), |β_n| ≤ τ(n):
  Σ_{x^{α} < m < x^{α+1/2}} Σ_n α_m β_n (a\*_{mn} − λ_W ν_W(mn)) ≪ x(log x)^{−A}   (λ_W := Σ_{n≤x} a\*_n / Σ_{n≤x} ν_W(n)).
By Lemma N, (TII_W) with saving (log x)^{−A} is impossible unless B ≥ A/2 (roughly); with B ≥ A it is not refuted by
single-prime conspiracies (an adversary at an inert ℓ ≥ W gains ≪ x/ℓ²), and a large-sieve heuristic bounds
simultaneous conspiracies at ℓ ∈ [W, min(M, N)^{1/2}] by ≪ x/W (Assessment).

**Theorem V′ (CONDITIONAL on (TII_W) with B, A large; the implication is given in outline only).** (TII_W) implies
Σ_{p ≤ x} a\*_p ≫ x/log x, hence P(4,15) with ≫ x/(log x)⁹ primes p ≤ x, p ≡ 97 (120).
*Outline.* Harman's sieve (Fundamental Theorem; *Prime-detecting sieves* Thm 3.1 as restated in Teräväinen's notes,
VERIFIED-2nd; stated for sets, the combinatorial proof is linear in the sequences — a weighted version is assumed
here, Assessment) with 𝒜 = (a\*_n), ℬ = (λ_Wν_W(n)), β = 1/2, Type II = (TII_W), Type I with M = x^{1/6−4ε} > x^{α}:
Σ_{m≤M} c_m Σ_n(a\*_{mn} − λ_Wν_W(mn)) — Lemma T\* (all d coprime to 30) gives Σ_{m≤M}τ(m)|r\*_m| ≪ x^{1−η/3} (Cauchy–
Schwarz: (Σ τ²(A\*_m + g̃(m)c\*x))^{1/2}(Σ|r\*_m|)^{1/2} with Σ_n a\*_n τ₃(n)·τ(n) ≪ x(log x)^{C}), and the ν_W side is
elementary except that ν_W is periodic modulo P(W) = ∏_{7≤ℓ<W}ℓ, a huge modulus: expanding ∏_{ℓ<W}δ_ℓ =
Σ_{q | P(W)}∏_{ℓ|q}(δ_ℓ − 1) gives class functions mod q with sup-norm ≤ ∏_{ℓ|q}(2 + O(1/ℓ)) and mean O(∏ 1/ℓ); q ≤ x^{1/3}
is exact counting, q > x^{1/3} is ≪ x·exp(−c log x/log log x) by Rankin's trick (Σ_{q|P(W), q>Q}3^{ω(q)}/q ≤
Q^{−σ}∏_{ℓ<W}(1 + 3ℓ^{σ−1}), σ = 1/log W). The same expansion plus Bombieri–Vinogradov (q ≤ x^{1/2}(log x)^{−C}) and Rankin
(larger q) evaluates Σ_p ν_W(p) ≫ x/log x. Harman then gives Σ_{√x<p≤x}a\*_p = λ_W Σ_{√x<p≤x}ν_W(p) + O(x(log x)^{3−A}).
Not written out in full; label accordingly.

### 4.3 Prop D (PROVED inequality; a sufficient strategy, not a necessity)

Let E_n := a\*_n − λ_Wν_W(n), N ≤ x^{1/2}, β supported on (N, 2N], |β_n| ≤ τ(n), |α_m| ≤ τ(m). Then
  |Σ_{m,n} α_m β_n E_{mn}|² ≤ (Σ_{m ≤ x/N} τ(m)²)·Σ_{n₁,n₂ ∈ (N,2N]} τ(n₁)τ(n₂)|Σ_{m ≤ x/max(n₁,n₂)} E_{mn₁}E_{mn₂}|,
so (TII_W) at this split follows from Σ_{n₁,n₂}τ(n₁)τ(n₂)|Σ_m E_{mn₁}E_{mn₂}| ≪ xN(log x)^{−2A−C}. Expanding: (a) the
a\*a\* part is, for n₁ ≢ n₂ … with n₁ ≡ n₂ (mod 120) units (else no m has both mn_i ≡ 97), the one-variable correlation
Σ_m r\*(n₁m + 4)r\*(4n₁m + 1)r\*(n₂m + 4)r\*(4n₂m + 1)1[mn₁ ≡ 97 (120)] — four affine forms in one variable with distinct
roots (pairwise non-proportional), coefficients of size N; its main term is a pair-dependent singular series which must
cancel against (b) the two mixed terms, Type I sums of a\* to moduli ≈ n_i twisted by ν_W(mn_j) (twisted Type I at
level ≈ N, beyond Lemma T\* once N > x^{1/6}), and (c) the ν_Wν_W term; (d) the diagonal and a quantitative
exceptional set of pairs must be bounded. Status (Assessment; coverage-limited, lit report Q1, Q3): no asymptotic was
found for any nondegenerate one-variable correlation of three or more values of r or τ with individual shifts
(Blomer, arXiv:1512.03278, calls Σ τ(n)τ(n−h)τ(n+h) "an extremely interesting and challenging open problem"; his Cor. 1
averages over h ≥ N^{1/3+ε}); the linear-correlation theorems (Heath-Brown, *Linear relations amongst sums of two
squares*, Thm 1; Matthiesen arXiv:1106.4690 Thm 1.1, 1205.4145, 1011.0019) need ≥ 2 free variables with no two forms
affinely dependent, which one-variable systems never satisfy. Nothing here shows these inputs are *necessary* for (TII_W).

### 4.4 FI's asymptotic sieve; Route S (Assessment)
*FI asymptotic sieve (read from the source).* Theorem 1 needs (R) at level x^{2/3} < D < x and (B) for √D/Δ < N < √x/δ
with γ(n, C)μ(mn) coefficients (and squarefree support, removable with extra hypotheses, their §9); FI note (B) "can be
realistic only if D is somewhat larger than x^{2/3+ε}". Our Type I level is x^{1/6}; Harman's version trades level for a
wider Type II range.
*Route S.* Type I information for the semi-linear sieve on {4p + 1} is BV (level 1/2). A dispersion attempt at Type II
information Σ α_m β_n 1_ℙ((mn − 1)/4) yields Σ_m 1_ℙ((mn₁ − 1)/4)1_ℙ((mn₂ − 1)/4) averaged over (n₁, n₂) — binary prime
correlations (twin-prime type). The S-condition itself needs no Type II: r\* = Σ_{e²|N}μ(e)·r(N/e²) with r = 4(1 ∗ χ) is
an exact divisor sum whose cost is level 1/2.

## 5. Route P: what level the prime variable needs, and what dispersion supplies

**Architecture (FI 2009 §§6–7, transposed).** Shift A exact via r\*(A) = Σ_{e² | A}μ(e)·r(A/e²), r(v) = 8Σ_{k|v, k<√v}χ(k)
(divisors k up to √x: level 1/2; the √x boundary for a single fixed residue is BFI Theorem 9 as used in FI 2009 Thm 5;
BFI Thm 9's exact statement is UNVERIFIED in the lit report). Shift B exact via Iwaniec's semi-linear lower sieve of
level D = x^{θ_D}, sifting range z = x^{θ_z} > x^{1/4} (so Ω_𝒬(B) ∈ {0, 2}), plus switching for the two-𝒬-prime
configurations. Schematically (e = 1 piece; the e² moduli, (k, d) = 1, coprimality with 30 and endpoints as in Lemma T\*)
the main term needs
  **(BFI_χλ)** Σ_{k ≤ 2√x, (k,30)=1} χ(k)Σ_{d ≤ x^{θ_D}, (d,30k)=1} λ_d [π(x; 120kd, c_{k,d}) − li(x)/φ(120kd)] ≪ x(log x)^{−A},
c_{k,d} ≡ 97 (120), ≡ the root of A (mod k), ≡ the root of B (mod d): a CRT-mixed residue, fixed on each factor.

**Budget for this architecture (elementary).** The semi-linear β-sieve lower function has f(s) = 0 for s ≤ 1, so a
positive main term needs D > z > x^{1/4}; with the full hyperbola range on A the moduli reach x^{3/4+}. This is
bookkeeping for this architecture with absolute-value-free but full-range moduli; cancellation in k, other
decompositions or other switching are not covered. Not a barrier.

**Sufficient levels in the P415 model (Assessment; `scripts/z56_k4bilin_firoute.py` → `firoute.txt`, reproduced byte
for byte by the review).** Positivity f(θ_D/θ_z) > L·B(θ_z), B(θ) = F(1/θ) − F(1)√θ the two-𝒬-prime Buchstab mass
(P415 §1.4), L ≥ 1 the switched-sum loss. Minimal θ_D: 0.257 (L = 1), 0.282 (2), 0.385 (4), 0.446 (8), 0.474 (16), 0.487
(32), 0.494 (64), 0.497 (128), 0.4996 (1000); GEH-switched model (L = pen·2/θ_D): 0.408 (pen 1), 0.458 (2.35), 0.480 (5).
Total 1/2 + θ_D: 0.757 … ≈ 1.0, 0.908 in the GEH-switched model vs P415 §2(b)'s 0.9764 (same extra GEH-type input) and
0.9962 (ordinary EH, BV switching). Grid optimisation of tabulated floating-point sieve functions; not certified; FI
handle the switched sum unconditionally (r's own level 2/3, small upper sieves), i.e. large L, hence θ_D → 1/2.

**What dispersion supplies (lit report Q5; tags there).** Single fixed residue, well-factorable weights: 4/7 (BFI
Thm 10, via Maynard I, VERIFIED), 3/5 (Maynard), 66/107 ≈ 0.6168 (Lichtman arXiv:2309.08522 Cor. 1.5 — ABSTRACT-ONLY in
the lit report; the statement is quoted there from the abstract page). Factor-dependent residues: Maynard III
(arXiv:2006.08250) Thm 1.2 (VERIFIED): level x^{1/2+δ}, δ < 1/1000, factor-size constraints, residue mod q₃ free; Thm 1.3
concerns a prime *minorant* of mass ≥ π(x)/8, not all primes. Zhang/Polymath MPZ (VERIFIED-2nd): all roots of a
fixed monic polynomial, smooth squarefree moduli, level 1/2 + 2ϖ, ϖ small (transfer to (p + 4)(4p + 1) not checked in a
source). None is shown to apply to χ(k)·(semi-linear λ_d) weights (well-factorability of semi-linear weights unproved
here). **Gap: 3/4 − 66/107 = 57/428 ≈ 0.133 even against the single-residue level; ≈ 1/4 against mixed-residue results.**

## 6. Numerics (integer sums exact; ratios, logs and model weights floating point) — diagnostics only

All: `gcc -O2`, `ulimit -v 6000000`, `timeout` ≤ 1700 s; each < 1 min. Reproduced byte for byte by the internal review
(typeii 10⁸, 4·10⁸; spectrum 10⁹, 10¹⁰) and cross-checked at 10⁶ by independent SymPy code (Σa = 352 832,
#{a > 0} = 2 254, #S-pairs = 2 037, prime S-pairs 535, Σμa = −3 904, Σλa = −4 800, Σa\* = 313 920, Σμa\* = −576,
Σ_p a_p = 95 296, Σ_p a\*_p = 82 688).
1. **PNT in the dense sequence** (`scripts/z56_k4bilin_typeii.c`; `typeii_<X>_c<class>.txt`). Asymptotic-sieve prediction
   Σ_p a_p log p = H·A (H over all primes, g(ℓ) = (ℓ − χ)/(ℓ(ℓ + χ)), FI Lemma 4.2 form): 0.980 (10⁶), 1.0025 (10⁸),
   1.0033 (4·10⁸); for a\* with H\* = 3.44604: 0.972, 1.0037, 1.0038 — within 0.4 %. P(4,15) primes ≡ 97 (120) up to
   4·10⁸: 105 771 (exact).
2. **(B)-test** (FI's bilinear quantity with γ ≡ 1 only): B(N) = Σ_m|Σ_{N<n≤2N, mn≤x} μ(mn)w_{mn}|/Σw, T(N) the same with
   |·| inside, R_a the random-sign reference Σ_m(2/π · Σ_n a²)^{1/2}/Σa. At x = 4·10⁸, N = 20 000 = √x (FI's range stops
   short of √x; diagnostic only): B_a = 0.0362 (R_a 0.0353, T_a 0.166), B_{a\*} = 0.0374 (T 0.168), 1_S-pairs 0.0284 (T
   0.171); at N = x^{0.4}: B_a 0.087 (R 0.080), B_{a\*} 0.090. At N = x^{0.2} (≈ 52, a handful of terms per m) B = T for
   every sequence. Selberg control w = a(1 + λ): B = T exactly at every N (μ(t)(1 + λ(t)) = 2·1[t squarefree, Ω even]),
   values 0.166–0.177. So: random-sign-like cancellation once inner sums are long; no global parity bias visible.
3. **Spectrum against the multiplicative model** (`scripts/z56_k4bilin_spectrum.c`; `spectrum_1e9.txt`,
   `spectrum_1e10.txt`). ρ(C) = (Σ_C a\*/Σ_C w)/(Σa\*/Σw) at 10¹⁰: primes 1.0005; P₂ = pq, log p/log x ∈ [0.05, 0.10) …
   [0.45, 0.50): 1.0009, 0.9999, 1.0001, 0.9992, 1.0016, 1.0000, 0.9996, 0.9997, 0.9960; Ω = 3: 0.9997; n ∈ S: 0.9996;
   λ = ±1: 1.0000, 1.0000. These classes are equidistributed modulo small primes, so Lemma N's local discrepancies
   average out; the agreement shows no *global* bias, it does not test all-coefficient Type II.
4. **Controls.** *Odd squares (T1):* m² + 4, 4m² + 1 are primitive sums of two squares for odd m, so a\*_{m²} > 0; class 97
   contains no squares (97 is a non-residue mod 5). In class 1 (mod 120) at 10⁸ the squares carry 1.13 % of Σa, produce a
   Liouville bias (Σλa/Σa = +0.0082 vs −0.0028 in class 97) and a 1.1 % deficit of the PNT ratio (0.9893): the T1
   structure, O(√x·polylog), thin at scale x. *FRONTIER §4 item-14 test primes:* 193, 2521, 3361, 5569, 9601, 83449,
   329617, 712321, 8 813 281, 66529, 5 101 441 are P(4,15) primes; 409, 577, 23929, 102001 are not (p + 4 ∉ S),
   consistent with HCKILL §5 (independently re-factored by the review). Only 577 and 329617 are ≡ 97 (120); most are
   ≡ 1 or 49 (120). The class 97 was chosen for convenience; other classes (e.g. p ≡ 1 (5), where 5 | N₁N₂) need their
   own local argument, not given here.

## 7. FRONTIER §4 hard screens

Kill side: the screens are upper-side ES tests and are "not applicable" rather than "passed".
1. **T1 squares.** The confinement holds at odd squares (a\*_{m²} > 0); squares are a √x-thin set (§6.4). No upper-side claim.
2. **8/131.** P(4,15) is line-4-specific (HCKILL Lemma 1.1).
3. **Tied modulus.** Not applicable (fixed character χ₋₄).
4. **Fixed p.** Density / infinitude statements only.

## 8. Proposed FRONTIER §7.2 text (do not edit FRONTIER here)

> *(z56, `Z56_K4BILIN.md`; kill side, Type II lane; internally reviewed, one FATAL draft error withdrawn.)* With
> a\*_n = r\*(n + 4)r\*(4n + 1) on n ≡ 97 (120) (a\*_p > 0 ⟺ p is a P(4,15) prime there): **Lemma T\*** (PROVED rel. Smith /
> FI 2009 Lemma 4.1): level x^{1/6−ε}, density g\*(ℓ) = 1/(ℓ + 2χ₋₄(ℓ)). **Prop P** (PROVED): ≫ x/(log x)⁹ integers n ≡ 1 (8),
> Ω(n) ≤ 12, with n + 4, 4n + 1 ∈ S (dual of P415 Thm U; no ES content). **Lemma N** (PROVED): a\* vanishes on the shift
> classes of inert primes, so Type II for a\* must be W-tricked (an explicit 0/1-coefficient counterexample kills the
> multiplicative comparison model). Corrected target (TII_W) on [x^{1/6}, x^{2/3}] ⟹ P(4,15) (Theorem V′, CONDITIONAL,
> outline); by Cauchy–Schwarz one sufficient route needs one-variable four-fold r\*-correlations with local singular series
> and twisted Type I to ≈ √x — none available. **Prime route:** the FI architecture's full-range budget is > 3/4 for primes
> in CRT-mixed classes (model 0.76–1.0; 0.908 in P415's GEH-switched model vs 0.976 there); dispersion gives ≈ 0.617 for a
> single residue, 1/2 + δ for mixed residues. Diagnostics to 10¹⁰: a\* matches its multiplicative model on primes and P₂
> bands to ≤ 0.4 %, FI's (B) shows random-sign cancellation (Selberg control none) — averaged tests, not Type II proofs.

## 9. Reproduction

* `uv run --with numpy python scripts/z56_k4bilin_firoute.py > data/z56/k4bilin/firoute.txt` (needs
  `scripts/z55_p415_sieve.py`; < 1 min).
* `gcc -O2 -o typeii scripts/z56_k4bilin_typeii.c -lm; ./typeii X CLASS` (X = 10⁸, 4·10⁸; CLASS = 97, 1; 4·10⁸ ≈ 3.6 GB).
* `gcc -O2 -o spectrum scripts/z56_k4bilin_spectrum.c -lm; ./spectrum X` (X = 10⁹, 10¹⁰; 10¹⁰ ≈ 3.3 GB, 10 s).
* Literature: `data/z56/k4bilin/lit_report.md`. Internal review: `data/z56/k4bilin/internal_review.md`.

## 10. Review log

* **Internal hostile review** (deep-mode subagent, `data/z56/k4bilin/internal_review.md`): REJECT of the first draft's
  Type II frontier; Lemma T\* core, Prop P and all numerics confirmed (byte-identical reruns, independent SymPy checks,
  symbolic check of g\*). Fixes applied: (1) FATAL — the draft's (TII\*) (comparison with the multiplicative model w) is
  false by an explicit mod-7 counterexample; withdrawn, turned into Lemma N (generalised to all inert ℓ), target replaced
  by the W-tricked (TII_W) with Theorem V′ labelled CONDITIONAL / outline; (2) (C4_N) withdrawn as an attainable target
  for the old E; Prop D kept as an inequality and sufficient strategy, with local singular series, mixed terms, fixed-class
  indicators, diagonal and exceptional sets made explicit; "affinely independent" corrected to "distinct roots"; necessity
  claims reversed to sufficiency; literature nonexistence claims scoped; (3) Smith's input used only for y ≥ q with a
  trivial bound below, endpoints handled, k- and e-tails written out, Lemma T\* extended to all moduli coprime to 30 with
  g̃(d) (needed for Harman's Type I); (4) r\* = 4(1 ∗ χ) error in the overview corrected; (BFI_χλ) marked schematic with its
  coprimality/e² provisions; the > 3/4 statement scoped as a full-range budget for one architecture; (5) Lichtman tag
  corrected to ABSTRACT-ONLY, Maynard III Thm 1.3 described as a minorant, MPZ transfer qualified; (6) numerics relabelled
  as diagnostics; B-test now also run for a\* (`typeii_*` regenerated), "0.3 %" → "0.4 %", B = T for the control at
  every N with varying value; t = 0.2 rows noted as uninformative; (7) ε < 1/780 for Ω ≤ 12; novelty credited to P415
  Prop C / Sedunova; "composite" → "not required to be prime"; transfer to other classes not claimed.
