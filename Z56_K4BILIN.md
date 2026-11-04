# Z56_K4BILIN — Type II / bilinear attack on K(4) = P(4,15)

**ES is OPEN.** Nothing here proves or disproves it. All results are internal (internally reviewed only).
Lane K4BILIN (wave z56). Scripts `scripts/z56_k4bilin_*`, data `data/z56/k4bilin/`.

Notation (as in `Z54_HCKILL.md`, `Z55_P415.md`): 𝒬 = {primes ≡ 3 (mod 4)}; S = {n ≥ 1 : every prime factor ≡ 1 (mod 4)};
χ = χ₋₄; r(N) = #{(a, b) ∈ ℤ² : a² + b² = N}; r*(N) = #{(a, b) : a² + b² = N, gcd(a, b) = 1}; N₁ = n + 4, N₂ = 4n + 1, so
4N₁ − N₂ = 15. ω, Ω: number of distinct / all prime factors. Fix the class n₀ = 97 (mod 120): then n ≡ 1 (mod 8),
n ≡ 1 (mod 3), n ≡ 2 (mod 5), and N₁ ≡ 101, N₂ ≡ 29 (mod 120), so (nN₁N₂, 30) = 1. Put
  **a\*_n := r\*(n + 4)·r\*(4n + 1)·1[n ≡ 97 (mod 120)],   A\*_d(x) := Σ_{n ≤ x, d | n} a\*_n.**
For odd N ≡ 1 (mod 4): r\*(N) > 0 ⟺ N ∈ S, and then r\*(N) = 4·2^{ω(N)}. So a\*_n = 16·2^{ω(N₁)+ω(N₂)}·1_S(N₁)1_S(N₂) on
the class, and **a\*_p > 0 for a prime p ⟺ p is a P(4,15) prime in the class 97 (mod 120).**

## 0. Verdict: **narrowed** (no unconditional K(4)); one unconditional "dual" theorem; exact missing estimates

1. **Lemma T\* (PROVED, relative to FI 2009 Lemma 4.1 = Smith's theorem on r in progressions).** The S-weighted dense
   sequence (a\*_n) has level of distribution x^{1/6−ε}, with the explicit multiplicative density
   g\*(ℓ) = 1/(ℓ + 2χ(ℓ)) (ℓ ≥ 7). (det-15, S-refined analogue of Sedunova's Lemma 2 for det 1.)
2. **Proposition P (PROVED, same inputs + the linear β-sieve + Shiu).** #{n ≤ x : n ≡ 97 (120), n + 4 ∈ S, 4n + 1 ∈ S,
   Ω(n) ≤ 12} ≫ x/(log x)⁹. This is the *dual* of P415 Theorem U: there p is prime and one shift is only "bounded
   anatomy"; here both shifts are exactly in S and n is only a P₁₂. No ES content (composite n), but it isolates the
   gap of the dense route as a pure P₁₂ → P₁ (parity / Type II) gap.
3. **Route D — the exact missing bilinear estimate (§4).** Theorem V (CONDITIONAL, via Harman's sieve): P(4,15), indeed
   Σ_{p ≤ x} a\*_p log p ~ H\*·A\*_1(x), follows from **(TII\*)**: for all |α_m| ≤ τ(m), |β_n| ≤ τ(n),
   Σ_{x^{1/6−ε} < m ≤ x^{2/3−ε}} Σ_n α_m β_n (a\*_{mn} − λ w_{mn}) ≪ x(log x)^{−A}, with w the explicit multiplicative local
   model of §4.1. Prop D (PROVED implication): (TII\*) at a split (x/N, N) follows from (a) Type I for a\* at level ≈ N
   (known: x^{1/6}) and (b) an asymptotic, for almost all (n₁, n₂) ∈ (N, 2N]², of the **one-variable four-fold
   correlation** Σ_m r\*(n₁m + 4) r\*(4n₁m + 1) r\*(n₂m + 4) r\*(4n₂m + 1). No one-variable correlation of ≥ 3 values of r or
   τ is known individually (Blomer 2017: triple τ only on average over shifts; Heath-Brown 2003 / Matthiesen 2012 need
   ≥ 2 free variables) (Assessment).
4. **Route P — prime-variable bilinear input (dispersion) (§5).** Within the Friedlander–Iwaniec architecture (one shift
   exact via r\* = 4·(1 ∗ χ) with divisors up to √x, the other by the semi-linear lower sieve sifting past x^{1/4}) the
   main term needs primes equidistributed to moduli k·d with k up to ≍ √x and d > x^{1/4}: **level > 3/4 is necessary in
   this architecture (PROVED, trivial: f(s) = 0 for s ≤ 1)**; the model gives sufficient levels 0.757 (ideal switching)
   … ≈ 1.0, and 0.908 in P415's GEH-switched model (P415's best there: 0.976; ordinary EH 0.996) (Assessment). The best
   dispersion results for compatible residue structures reach 1/2 + small (Maynard III, MPZ) or 66/107 ≈ 0.617 (one
   fixed residue only, Lichtman). Gap ≥ 0.13 in level even against the fixed-residue record.
5. **Route S (§4.4, Assessment).** Type II information *for the S-sieve* on 4p + 1 is Σ α_m β_n 1_ℙ((mn − 1)/4), whose
   dispersion produces Σ_m Λ((mn₁ − 1)/4)Λ((mn₂ − 1)/4): twin-prime-type (parity-blocked). Not a route.
6. **EVIDENCE (§6): the missing Type II estimate looks true.** Up to 10¹⁰ the a\*-weighted mass of primes, of P₂ = pq in
   every 0.05-band of log p/log x across the whole Type II range, of Ω = 3, of n ∈ S and of λ(n) = ±1 all match the
   multiplicative local model to within 0.4 % (most within 0.1 %); Friedlander–Iwaniec's bilinear quantity (B) shows
   square-root (random-sign) cancellation, while Selberg's parity sequence a\*(1 + λ) shows none; the asymptotic-sieve
   prediction Σ_p a_p log p = H·A holds to 0.3 % at 4·10⁸; g\*(ℓ) is confirmed to 4 digits.

**Bottom line (Assessment).** K(4) is a *level* problem in the prime variable (solved under EH(θ₀), HCKILL Thm E) and a
*Type II* problem in the dense variable. Both formulations are now pinned down: the dense route needs (TII\*) — at
least as strong, via dispersion, as one-variable four-fold r\*-correlations — plus Type I beyond x^{1/6}; the prime route
needs level > 3/4 for primes in CRT-mixed classes with χ- and semi-linear-sieve weights. Neither is within reach of
known bilinear technology. Numerically the dense sequence behaves exactly like its local model across the full Type II
range, so no hidden obstruction (parity-type or algebraic) is visible.

## 1. Statements attacked; why not closed

* **P(4,15)** (OPEN; = K(4) by HCKILL Lemma 1.1, PROVED): infinitely many primes p ≡ 1 (8) with p + 4, 4p + 1 ∈ S.
* **Route D (dense sequence).** Detect primes inside the weighted set (a\*_n), which has mean ≍ 1 (Σ_{n≤x} a\*_n ≍ x):
  Type I = A\*_d, Type II = Σ α_m β_n a\*_{mn}. Lane task: prove the Type I side, state the Type II estimate that is
  missing, test it.
* **Route P (prime variable).** HCKILL Thm E / FI 2009 / P415 §2 sieve primes p by N₁, N₂; level > 1/2 for primes comes
  only from bilinear (dispersion) methods. Lane task: the level the best architecture needs, and what dispersion gives.
* **Route S.** Type II for the semi-linear sieve itself.

**Why not closed.** P415 proved Theorem U and a ledger for the vector / product-linear sieves; it did not treat the
dense-sequence formulation (its Type I level, its Type II requirement), the FI architecture's threshold, or the actual
bilinear inputs. HCKILL/P415 call the remaining deficit "parity-type"; §4–§5 split it precisely into a Type II gap
(dense route) and a level gap (prime route). Nothing here is in FRONTIER §6 or the closed list. Literature for this lane
was re-verified from sources (`data/z56/k4bilin/lit_report.md`, research subagent; tags VERIFIED / ABSTRACT-ONLY /
UNVERIFIED there); I read Friedlander–Iwaniec "Asymptotic sieve for primes" (arXiv math/9811186, Theorem 1 and
hypotheses (R), (R1), (B), (B1)–(B3)) and the FI 2009 text (`sources/window2/fi09-hyperbolic-pnt.txt`) myself.

## 2. Lemma T\*: Type I for the dense sequence

**Input (Smith; FI 2009 Lemma 4.1, read in the published text).** For (c, q) = 1 and y ≥ 1,
  Σ_{m ≤ y, m ≡ c (q)} r(m) = (πy/q)∏_{p | q}(1 − χ(p)/p)·ε(c, q) + O_ε(q^{−1/2} y^{2/3+ε}),
with ε(c, q) = 1 if 4 ∤ q and ε(c, q) = 1 + χ(c) if 4 | q. (FI: "this gives the asymptotic within the range q < x^{2/3−ε}".)

**Lemma T\* (PROVED relative to the input).** There is c\* > 0 such that for squarefree d with (d, 30) = 1 and x ≥ 2,
  A\*_d(x) = g\*(d)·c\*x + r\*_d(x),   g\*(d) = ∏_{ℓ | d} 1/(ℓ + 2χ(ℓ)),
  |r\*_d(x)| ≪_ε d^{−1/2}x^{11/12+ε} + x^{1−3ε}/d + x^{1/2+ε}
(ε > 0 small; the middle term is the tail e₁e₂ > E = x^{8ε} of the proof). Consequently
  Σ_{d ≤ D, (d,30)=1} μ²(d)|r\*_d(x)| ≪ x^{1−ε}  for D = x^{1/6−4ε}  (ε small).

*Proof.* (i) *Expansion.* For every N, r\*(N) = Σ_{e² | N} μ(e) r(N/e²) (a representation with gcd g is g times a primitive
representation of N/g²). Hence a\*_n = Σ_{e₁² | N₁, e₂² | N₂} μ(e₁)μ(e₂) r(N₁/e₁²) r(N₂/e₂²). Since (N₁, N₂) | 15 and
(N₁N₂, 30) = 1, the e_i are coprime to each other and to 30; if d | n then (d, N₁N₂) | 4 forces (d, e₁e₂) = 1.

(ii) *Large e (tail).* Using r ≪ x^{ε}, the terms with e₁e₂ > E contribute to A\*_d at most
x^{ε} Σ_{e₁ > √E or e₂ > √E} #{n ≤ x : d | n, e₁² | N₁, e₂² | N₂} ≪ x^{ε}Σ_{e > √E, e² ≤ 4x+1}(x/(de²) + 1)
≪ x^{1+ε}/(d√E) + x^{1/2+ε} = x^{1−3ε}/d + x^{1/2+ε} (the number of admissible pairs (e₁, e₂) for one n is
≤ τ(N₁)τ(N₂) ≪ x^{ε}, absorbed in the x^{ε}; e₁e₂ > E forces e₁ > √E or e₂ > √E; (d, e_i) = 1 gives the CRT count).
Summed over d ≤ D this is ≪ x^{1−3ε}log x + D x^{1/2+ε} ≪ x^{1−2ε} for D ≤ x^{1/6}.

(iii) *Small e: one r opened.* Fix e₁, e₂ with e₁e₂ ≤ E. Put u = N₁/e₁², v = N₂/e₂² (both ≡ 1 (mod 4), v ≡ 5 (mod 8)).
FI 2009 (3.1)/(4.5): for m ≡ 1 (mod 4), r(m) = 8Σ_{kl = m, k < √m} χ(k) + 4χ(√m) (last term only for squares). Open
r(v): the square terms contribute O(x^{1/2+ε}) in total. The remaining sum is
  8 Σ_k χ(k) Σ_{u} r(u),  u ≤ (x + 4)/e₁²,  u > (k²e₂² + 15)/(4e₁²),
  u ≡ 4·ē₁² (mod d),  4e₁²u ≡ 15 (mod e₂²k),  e₁²u ≡ 101 (mod 120),
(the conditions d | n = e₁²u − 4, e₂²k | N₂ = 4e₁²u − 15, n ≡ 97 (120)). Here k | v, so (k, 30de₁) = 1, while k and e₂
may share primes; the three moduli d, e₂²k, 120 are pairwise coprime and each residue is a unit (15, 4e₁², 101 are units
there). So u runs over one reduced class c mod q = 120·d·e₂²·k, 8 | q, χ(c) = χ(101) = 1, and the input applies (as a
difference of two values of y ≤ (x+4)/e₁²). The error terms total
  Σ_{e₁e₂ ≤ E} Σ_{k ≤ 2√x/e₂} (120de₂²k)^{−1/2}(x/e₁²)^{2/3+ε} ≪ d^{−1/2}x^{2/3+ε}·x^{1/4}·Σ_{e₁,e₂} e₁^{−4/3}e₂^{−3/2}
  ≪ d^{−1/2}x^{11/12+ε}.
Summed over d ≤ D: ≪ D^{1/2}x^{11/12+ε} ≪ x^{1−ε} for D = x^{1/6−4ε}.

(iv) *Main term.* The main terms are 8·Σ χ(k)·(2π/q)∏_{p | q}(1 − χ(p)/p)·(x + 4 − (k²e₂² + 15)/4)/e₁², summed over
k < √(4x+1)/e₂ and e₁e₂ ≤ E. As in the proof of FI 2009 Lemma 4.2: the k²-part is ≪ x^{1/2+ε}/d (partial summation with
Σ_{k ≤ K} χ(k)h(k) ≪ log K for the bounded multiplicative weights h(k) = ∏_{p | k}(1 − χ(p)/p) restricted to (k, m) = 1,
which follows from h = 1 ∗ (μ-supported ν with |ν(p)| ≤ 1/p) and |Σ_{b ≤ t}χ(b)1_{(b,m)=1}| ≤ 2^{ω(m)}); the k-tail
k > √(4x+1)/e₂ of the completed series is ≪ x^{1/2+ε}e₂/d; and completing the e-sums costs ≪ x/(dE)·x^{ε} as in (ii).
The completed main term is x·C·Σ_{e₁,e₂,k} μ(e₁)μ(e₂)χ(k)/(d e₁²e₂² k)·∏_{p | de₂k}(1 − χ(p)/p) with the stated coprimality
conditions, an Euler product (absolutely convergent in e₁, e₂; in k it is L(1, χ) times an absolutely convergent
product, as in FI). For ℓ | d the local factor is (1/ℓ)(1 − χ(ℓ)/ℓ) (no e or k at ℓ). For ℓ ∤ 30d it is
  E_ℓ = [e₁ = e₂ = 1: Σ_{j≥0} χ(ℓ)^j ℓ^{−j}·(1 − χ(ℓ)/ℓ)^{[j≥1]} = 1 + χ(ℓ)/ℓ] + [e₁ = ℓ, k ⊥ ℓ: −1/ℓ²]
     + [e₂ = ℓ, any k-power: −ℓ^{−2}(1 − χ(ℓ)/ℓ)Σ_j χ(ℓ)^jℓ^{−j} = −1/ℓ²]  = 1 + χ(ℓ)/ℓ − 2/ℓ².
Hence the main term is c\*x·∏_{ℓ | d} (1/ℓ)(1 − χ(ℓ)/ℓ)/E_ℓ, and (ℓ − χ)/(ℓ² + χℓ − 2) = 1/(ℓ + 2χ) for χ = ±1
((ℓ² + ℓ − 2) = (ℓ − 1)(ℓ + 2), (ℓ² − ℓ − 2) = (ℓ + 1)(ℓ − 2)). c\* > 0: Concretely (d = 1): c\* = C₁·∏_{ℓ≥7}E_ℓ with C₁ > 0 and
∏_{ℓ≥7}E_ℓ = ∏_{ℓ≥7}(1 + χ(ℓ)/ℓ)·∏_{ℓ≥7}(1 − 2/(ℓ² + χ(ℓ)ℓ)); the second product converges absolutely with positive
factors, and ∏_{p odd}(1 + χ(p)/p) = L(1, χ)·∏_{p odd}(1 − p^{−2}) = (π/4)(8/π²) = 2/π (the k-series, as in FI), so
∏_{ℓ≥7}(1 + χ(ℓ)/ℓ) = (2/π)/((2/3)(6/5)) > 0. ∎

*Remarks.* (1) The structure is FI 2009 Lemma 4.2 (det 1, r·r), with the d^{−1/2} saving that Sedunova
(arXiv:2609.28200, Lemma 2 and Remark 1, per the lit report) also records; the exponent 1/6 comes from summing the
individual Weil-type error over k < √x. (2) Numerically (`spectrum_1e10.txt`), Σ_{ℓ | n} a\*_n/Σ a\*_n = 0.20009,
0.11111, 0.06669, 0.05258, 0.05879, 0.04761, 0.03229, 0.03447 for ℓ = 7, …, 31, against 1/(ℓ + 2χ(ℓ)) = 0.20000,
0.11111, 0.06667, 0.05263, 0.05882, 0.04762, 0.03226, 0.03448. (3) g\*(ℓ) < 1 and g\*(ℓ) = 1/ℓ + O(1/ℓ²): a linear
(κ = 1) sieve density.

## 3. Proposition P (unconditional dual of Theorem U)

**Proposition P (PROVED relative to: Lemma T\*; the linear β-sieve lower bound, Rosser–Iwaniec, as quoted in Nath–Xie
arXiv:2501.16723 (3.4)/Lemma 3.6 and used in HCKILL Thm E Step 2; the Shiu/Halberstam–Richert mean-value upper bound).**
For x ≥ x₀,
  #{n ≤ x : n ≡ 97 (mod 120), n + 4 ∈ S, 4n + 1 ∈ S, Ω(n) ≤ 12} ≫ x/(log x)⁹.
In particular there are infinitely many n ≡ 1 (mod 8) with at most 12 prime factors (all ≥ x^{1/13}) and both window
integers of line 4 in S.

*Proof.* Sift the sequence (a\*_n)_{n≤x} by the primes ℓ ≥ 7 (the primes 2, 3, 5 never divide n). By Lemma T\* the
remainders satisfy Σ_{d < D, d | P(z)} |r\*_d| ≪ x^{1−ε} with D = x^{1/6−4ε}, and g\* satisfies the linear sieve axiom
∏_{w ≤ ℓ < z}(1 − g\*(ℓ))^{−1} ≤ (log z/log w)(1 + K/log w). Take s = 2.1 and z = D^{1/s}. The lower bound
S(𝒜\*, z) ≥ c\*x·V(z)(f(s) + o(1)) − Σ|r\*_d|, with f(s) = 2e^γ log(s − 1)/s, f(2.1) = 0.1617… > 0 and V(z) ≍ 1/log x,
gives Σ_{n ≤ x, (n, P(z)) = 1} a\*_n ≫ x/log x. Every such n has all prime factors ≥ z = x^{(1/6−4ε)/2.1}, so
Ω(n) < 2.1/(1/6 − 4ε) < 13 for ε small, i.e. Ω(n) ≤ 12; and a\*_n > 0 means N₁, N₂ ∈ S. For the count, a\*_n² =
256·4^{ω(N₁)+ω(N₂)} ≤ 128(16^{ω(N₁)} + 16^{ω(N₂)}), and Σ_{m ≤ 4x+1} 16^{ω(m)}1_S(m) ≪ x(log x)^{16/2 − 1} = x(log x)⁷
(nonnegative multiplicative function, value 16 on primes ≡ 1 (4), 0 on 𝒬; Shiu/Halberstam–Richert). By Cauchy–Schwarz
the number of sifted n with a\*_n > 0 is ≥ (x/log x)²/(x(log x)⁷) up to constants. ∎

*Remarks.* (1) This is the det-15, S-refined analogue of Sedunova's unconditional ω(n) ≤ 7 for det 1 (her Thm 2, via
weighted sieves, per the lit report); a Richert-weighted version should lower 12 similarly (Assessment, not done). (2)
Duality with P415 Theorem U: U keeps *primality* and one exact shift; P keeps *both shifts exact* and loses primality to
P₁₂. K(4) needs both. (3) No ES content: ES at composite n follows from a prime factor. (4) The sieve here is
parity-blocked exactly as for twin primes: Type I information alone (any level < 1) cannot give Ω(n) = 1 (Selberg's
example a\*_n(1 + λ(n)) has the same Type I data up to a factor; §6 checks this numerically for the (B) quantity).

## 4. Route D: the exact missing bilinear estimate

### 4.1 The model and Theorem V (CONDITIONAL)

Model: w_n := f(n)·1[n ≡ 97 (120)], f multiplicative, f(ℓ^e) = c_ℓ := (ℓ − 1)/(ℓ − 1 + 2χ(ℓ)) for ℓ ≥ 7, e ≥ 1. Then
the w-density of {ℓ | n} is (c_ℓ/ℓ)/(1 − 1/ℓ + c_ℓ/ℓ) = g\*(ℓ), and elementarily (f = 1 ∗ h, h supported on
ℓ-powers with h(ℓ) = c_ℓ − 1 = O(1/ℓ), h(ℓ^j) = 0 for j ≥ 2) W_d(x) := Σ_{n≤x, d|n} w_n = g\*(d)W(x) + O(x^{ε}).
Let λ := c\*x/W(x) (≍ 1).

**Harman's sieve (Fundamental Theorem; Harman, *Prime-detecting sieves* Thm 3.1, as restated in Teräväinen's notes —
book not accessed; VERIFIED-2nd in the lit report).** If for some Y, λ, α > 0 and β ≤ 1/2, (I) Σ_{m ≤ M} c_m Σ_n (a_{mn} −
λb_{mn}) = O(Y) for all |c_m| ≤ τ(m) with some M > x^α, and (II) Σ_{x^α < m < x^{α+β}} Σ_n α_m β_n(a_{mn} − λb_{mn}) =
O(Y) for all |α_m| ≤ τ(m), |β_n| ≤ τ(n), then S(𝒜, x^β) = λS(ℬ, x^β) + O(Y log³x). (Stated there for sets; the proof
is linear in the sequences and applies verbatim to nonnegative weights — standard, Assessment.)

**Theorem V (CONDITIONAL on (TII\*)).** Let α₀ = 1/6 − 4ε. Assume
  **(TII\*)** Σ_{x^{α₀} < m < x^{α₀+1/2}} Σ_n α_m β_n (a\*_{mn} − λw_{mn}) ≪ x(log x)^{−A}  for all |α_m| ≤ τ(m), |β_n| ≤ τ(n)
(A large fixed). Then Σ_{√x < p ≤ x} a\*_p = λΣ_{√x<p≤x} w_p + O(x(log x)^{−A+3}) ≍ x/log x, hence P(4,15) with
≫ x/(log x)⁹ primes p ≤ x in the class 97 (mod 120).
*Proof.* Apply Harman with α = α₀ − ε and M = x^{α₀}. (I): Σ_{m≤M} c_m(A\*_m − λW_m) = Σ c_m(r\*_m − λ·O(x^ε)), and
Σ_{m ≤ M} τ(m)|r\*_m| ≤ (Σ_m τ(m)²|r\*_m|)^{1/2}(Σ_m |r\*_m|)^{1/2}; the first factor is ≤ (Σ_m τ(m)²(A\*_m + g\*(m)c\*x))^{1/2}
≪ (Σ_n a\*_n τ₄(n)·τ(n) + x(log x)^C)^{1/2} ≪ (x(log x)^{C})^{1/2} (Cauchy–Schwarz with Σ a\*_n² ≪ x(log x)⁷ from Prop P's
proof), the second is ≪ x^{(1−ε)/2} by Lemma T\*; so (I) holds with Y = x^{1−ε/3}. (II) is (TII\*). Harman with β = 1/2 gives
S(𝒜\*, √x) = λS(𝒲, √x) + O(x(log x)^{3−A}); S(𝒜\*, √x) = Σ_{√x<p≤x} a\*_p + O(x^{1/2+ε}) and λΣ_p w_p ≍ x/log x
(PNT in progressions; c_p = 1 + O(1/p)). The count follows by Cauchy–Schwarz as in Prop P. ∎
(Heuristically λΣ_{p≤x} w_p log p = H\*·A\*_1(x)(1 + o(1)) with the asymptotic-sieve constant
H\* = ∏_{ℓ=2,3,5}(1 − 1/ℓ)^{−1}·∏_{ℓ≥7}(1 − g\*(ℓ))(1 − 1/ℓ)^{−1} = 3.4460…; observed Σ_p a\*_p log p/(H\*A\*_1) = 1.0038
at 4·10⁸, §6.)

*Why FI's asymptotic sieve does not help here (read from the source).* FI's Theorem 1 needs (R) at level D with
x^{2/3} < D < x (R1) and (B) only for √D/Δ < N < √x/δ with Möbius-type coefficients; it is designed for sequences with
very high Type I level (FI: "(B) can be realistic only if D is somewhat larger than x^{2/3+ε}"). Our Type I level is
x^{1/6}. Harman's version trades Type I level for a wider Type II range; with α₀ = 1/6 the range is [x^{1/6}, x^{2/3}].

### 4.2 Prop D (PROVED implication): what (TII\*) reduces to

Let E_n := a\*_n − λw_n. For N ≤ x^{1/2}, β supported on (N, 2N] with |β| ≤ τ, and |α_m| ≤ τ(m):
  |Σ_{m,n} α_m β_n E_{mn}|² ≤ (Σ_{m ≤ x/N} τ(m)²)·Σ_{n₁,n₂ ∈ (N,2N]} τ(n₁)τ(n₂)|Σ_{m ≤ x/max(n₁,n₂)} E_{mn₁}E_{mn₂}|
(Cauchy–Schwarz in m). So (TII\*) at this split follows from
  **(C4_N)** Σ_{n₁,n₂ ∈ (N,2N]} τ(n₁)τ(n₂)|Σ_m E_{mn₁}E_{mn₂}| ≪ x N (log x)^{−2A−C}.
Expanding E_{mn₁}E_{mn₂}: (a) the a\*a\* part is, for n₁ ≠ n₂, the **one-variable four-fold correlation**
Σ_m r\*(n₁m + 4)r\*(4n₁m + 1)r\*(n₂m + 4)r\*(4n₂m + 1) (four pairwise affinely independent linear forms in one variable m,
coefficients of size N, length x/N); (b) the a\*w parts are Type I sums of a\* to modulus n₁ (or n₂) twisted by the
multiplicative weight f(mn₂), i.e. Type I at level ≈ N — beyond Lemma T\* once N > x^{1/6}; (c) ww is elementary.
Cauchy–Schwarz in n instead gives the same structure with the roles exchanged (forms in n with coefficients m ~ x/N).
So, along the dispersion route, (TII\*) needs: Type I for a\* up to level x^{1/2} (twisted), and the four-fold
correlation for almost all (n₁, n₂). **Status (Assessment, sources in the lit report):** Type I for r(n−2)r(n+2)-type
sequences is known only to x^{1/6} (Sedunova; spectral methods give X^{0.281} for the *divisor* analogue in a fixed
progression, Grimmelt–Merikoski Cor. 1.3, nothing comparable found for r); no asymptotic is known for any one-variable
correlation of three or more values of r or τ (Blomer, arXiv:1512.03278, calls Σ τ(n)τ(n−h)τ(n+h) "an extremely
interesting and challenging open problem"; his Cor. 1 needs an average over h ≥ N^{1/3+ε}); the linear-correlation
theorems (Heath-Brown, *Linear relations amongst sums of two squares*, Thm 1; Matthiesen, arXiv:1106.4690 Thm 1.1,
1205.4145, 1011.0019) need ≥ 2 free variables (no two forms affinely dependent), which a one-variable system never has.

### 4.3 What the dense route needs, as one ledger line
**(TI)** level x^{θ_I} for a\* (have θ_I = 1/6) and **(TII)** for every split with both factors ≥ x^{θ_I}. Raising θ_I
shrinks the Type II range ([x^{θ_I}, x^{1/2}] by symmetry); FI's asymptotic sieve would need θ_I > 2/3 and then only a
narrow balanced Type II range. In every version the Type II input is a bilinear correlation of a\* at scale x — via
dispersion a one-variable four-fold r\*-correlation.

### 4.4 Route S (Assessment): Type II for the S-sieve itself is twin-prime-type
The semi-linear sieve on 𝒜 = {4p + 1} uses Type I sums Σ_p 1[d | 4p + 1] (BV level 1/2). Type II information for that
sieve would be Σ_{m,n} α_m β_n 1_ℙ((mn − 1)/4) for bilinear α, β; Cauchy–Schwarz in m yields
Σ_m 1_ℙ((mn₁ − 1)/4)1_ℙ((mn₂ − 1)/4), a binary correlation of primes along two linear forms (Hardy–Littlewood type,
parity-blocked). So the "swap roles" idea — get S-information on 4p + 1 bilinearly — trades the half-dimensional
problem for a twin-prime problem; the S-condition itself needs no Type II (r\* = Σ_{e²|N}μ(e)·4(1 ∗ χ)(N/e²) is an exact
divisor sum: its only cost is level 1/2).

## 5. Route P: what level the prime variable needs, and what dispersion supplies

**Architecture (FI 2009 §§6–7, transposed).** Make shift A exact with r\*(A) = Σ_{e²|A}μ(e)·4Σ_{k | A/e²}χ(k) (divisors
k up to √(A/e²) after the hyperbola switch; level exactly 1/2, the √x boundary handled for a single fixed residue by
BFI Theorem 9 as in FI 2009 Thm 5); make shift B exact with Iwaniec's semi-linear lower sieve of level D = x^{θ_D},
sifting range z = x^{θ_z}, plus switching for the configurations with two 𝒬-primes ≥ z (z > x^{1/4} so that Ω_𝒬 ∈ {0, 2}).
The main term needs
  **(BFI_χλ)** Σ_{k ≤ 2√x} χ(k) Σ_{d ≤ x^{θ_D}} λ_d [π(x; 120kd, c_{k,d}) − li(x)/φ(120kd)] ≪ x(log x)^{−A},
c_{k,d} ≡ 97 (120), ≡ the root of A (mod k), ≡ the root of B (mod d) — a CRT-mixed residue, fixed on each factor.

**Necessity inside the architecture (PROVED, trivial).** The semi-linear β-sieve lower function satisfies f(s) = 0 for
s ≤ 1 (β = 1), so a positive main term needs D > z > x^{1/4}: **the moduli 120kd reach x^{3/4+} — level > 3/4.**

**Sufficient levels in the P415 model (Assessment; `scripts/z56_k4bilin_firoute.py`, `data/z56/k4bilin/firoute.txt`).**
Positivity f(θ_D/θ_z) > L·B(θ_z) with B(θ) = F(1/θ) − F(1)√θ the two-𝒬-prime Buchstab mass (P415 §1.4) and L ≥ 1 the
switched-sum loss. Minimal θ_D: 0.257 (L = 1, ideal), 0.282 (2), 0.385 (4), 0.446 (8), 0.474 (16), 0.487 (32), 0.497
(128), 0.4996 (1000); in P415's GEH-switched model (L = pen·2/θ_D): 0.408 (pen 1), 0.458 (pen 2.35), 0.480 (pen 5). Total
level 1/2 + θ_D: **0.757 … 1.0; 0.908 in the GEH-switched model**, against P415's 0.976 (product linear sieve, same
model) and 0.996 (ordinary EH). (FI themselves handle the switched sum unconditionally with r's own level 2/3 and small
upper sieves — a large L, hence θ_D → 1/2, their "θ close to 1".) These are model numbers, not theorems, and not
barriers.

**What bilinear (dispersion) technology supplies (lit report, Q5).** One fixed residue, well-factorable weights:
4/7 (BFI Thm 10), 3/5 (Maynard), 66/107 ≈ 0.617 (Lichtman, triply well-factorable; Corollary 1.5 in arXiv:2309.08522,
VERIFIED there). Residues depending on the factorisation: Maynard III (arXiv:2006.08250) Thms 1.2–1.3, level x^{1/2+δ}
with δ < 1/1000-type and a factor of convenient size; Zhang/Polymath MPZ, all roots of a fixed polynomial, smooth
squarefree moduli, level 1/2 + 2ϖ, ϖ small. **Gap: ≥ 3/4 − 0.617 ≈ 0.13 even against the single-fixed-residue record,
≈ 1/4 against the results that allow CRT-mixed residues.** The CRT-mixed residue c_{k,d} is the second obstruction: the
spectral (Kloosterman) dispersion results need one fixed residue a ≪ x^ε (Maynard III, p. 2, quoted in the lit report).

## 6. Numerics (CERTIFIED exact integer counts where stated; the readings are EVIDENCE)

All runs: `gcc -O2`, `ulimit -v 6000000`, `timeout` ≤ 1700 s; each < 1 min.
1. **PNT in the dense sequence** (`scripts/z56_k4bilin_typeii.c`; `data/z56/k4bilin/typeii_<X>_c<class>.txt`). Exact
   sums; cross-checked against an independent SymPy computation at 10⁶ (Σa = 352 832, #{a > 0} = 2 254, #S-pairs =
   2 037, of which 535 prime, Σμa = −3 904: identical). Asymptotic-sieve prediction Σ_p a_p log p = H·A (H over all
   primes, g as in FI Lemma 4.2 form for r·r): observed ratio 0.980 (10⁶), 1.0025 (10⁸), 1.0033 (4·10⁸); for a\*:
   0.972, 1.0037, 1.0038 with H\* = 3.44604. P(4,15) primes ≡ 97 (120) up to 4·10⁸: 105 771.
2. **(B)-test** (FI asymptotic sieve's bilinear quantity with γ ≡ 1): B(N) = Σ_m|Σ_{N<n≤2N} μ(mn)w_{mn}|/Σw. At 4·10⁸,
   N = x^{0.50}: B_a = 0.0362 against the random-sign reference R_a = 0.0353 and the trivial T_a = 0.166; S-indicator
   version 0.0284/0.171; **Selberg control w = a(1 + λ): B = T = 0.167 at every N** (no cancellation, as it must). At
   N = x^{0.4}: 0.087 vs R 0.080 vs T 0.166. Cancellation is random-sign-like; nothing parity-like is visible.
3. **Type II spectrum** (`scripts/z56_k4bilin_spectrum.c`; `spectrum_1e9.txt`, `spectrum_1e10.txt`). ρ(C) = (Σ_C a\*/Σ_C w)
   normalised by the global ratio, at 10¹⁰: primes 1.0005; P₂ = pq with log p/log x in [0.05, 0.10) … [0.45, 0.50):
   1.0009, 0.9999, 1.0001, 0.9992, 1.0016, 1.0000, 0.9996, 0.9997, 0.9960; Ω = 3: 0.9997; n ∈ S: 0.9996; λ = ±1:
   1.0000, 1.0000. The P₂ bands are exactly Harman's Type II pieces (α = 1_ℙ on m ~ x^t, β = 1_ℙ).
4. **Controls.** *Odd squares (T1):* m² + 4 and 4m² + 1 are primitive sums of two squares for odd m, so a\*_{m²} > 0
   always; the class 97 (mod 120) contains no squares (97 is a non-residue mod 5). In the class 1 (mod 120) at 10⁸ the
   squares carry 1.13 % of Σa and produce a visible Liouville bias (Σλa/Σa = +0.0082 vs −0.0028 in class 97) and a
   1.1 % deficit in the PNT ratio (0.9893) — the T1 structure, of size O(√x·polylog), invisible to Type II at scale x.
   *FRONTIER §4 item-14 test primes:* 193, 2521, 3361, 5569, 9601, 83449, 329617, 712321, 8 813 281, 66529, 5 101 441
   are P(4,15) primes (HC > 4); 409, 577, 23929, 102001 are not (p + 4 ∉ S), consistent with HCKILL §5. Only 577 and
   329617 lie in the class 97 (mod 120); most test primes are ≡ 1 or 49 (mod 120) — the analysis transfers to every
   admissible class (Remark: for p ≡ 1 (mod 5), 5 | N₁ and 5 | N₂; the 5-part is split off before applying Lemma 4.1,
which needs a reduced class).

## 7. FRONTIER §4 hard screens (best items: Lemma T\*, Prop P, Theorem V, Route P threshold)

1. **T1 squares.** Kill side: the confinement holds at odd squares (a\*_{m²} > 0); nothing here claims an upper-side
   mechanism. The squares are a thin (√x) set and do not affect Type I/II at scale x (§6.4). Passes trivially.
2. **8/131.** P(4,15) is line-4-specific (HCKILL Lemma 1.1); everything here is about the pair (p + 4, 4p + 1).
3. **Tied modulus.** Not applicable (kill side; the class condition is the fixed character χ₋₄).
4. **Fixed p.** All results are densities / infinitude statements; nothing concerns a prescribed p (K(4) does not need it).

## 8. Proposed FRONTIER §7.2 text (do not edit FRONTIER here)

> *(z56, `Z56_K4BILIN.md`; kill side, Type II lane.)* With a\*_n = r\*(n + 4)r\*(4n + 1) on n ≡ 97 (120) (a\*_p > 0 ⟺ p is
> a P(4,15) prime there): **Lemma T\*** (PROVED rel. Smith/FI Lemma 4.1) — level x^{1/6} with density
> g\*(ℓ) = 1/(ℓ + 2χ₋₄(ℓ)); **Prop P** (PROVED) — ≫ x/(log x)⁹ integers n ≡ 1 (8) with n + 4, 4n + 1 ∈ S and Ω(n) ≤ 12 (dual of
> P415 Thm U: both shifts exact, primality lost). **Theorem V** (CONDITIONAL): P(4,15) follows from the Type II estimate
> (TII\*) for a\* on [x^{1/6}, x^{2/3}] (Harman's sieve); by dispersion (TII\*) needs Type I to ≈ x^{1/2} and one-variable
> four-fold r\*-correlations — no one-variable ≥ 3-fold correlation of r or τ is known. **Prime route:** inside the FI
> architecture the main term needs primes in CRT-mixed classes to level > 3/4 (PROVED for the architecture; model 0.76–1.0,
> 0.908 GEH-switched, vs P415's 0.976); dispersion supplies ≤ 0.617 (single fixed residue) or 1/2 + δ (mixed residues).
> Type II for the S-sieve itself is twin-prime-type. EVIDENCE: to 10¹⁰ a\* matches its multiplicative local model on
> primes and on every P₂ band of the Type II range to ≤ 0.4 %; FI's (B) shows random-sign cancellation (Selberg control
> shows none). K(4) = a Type II problem in the dense variable, a level problem in the prime variable; both open.

## 9. Reproduction

* `uv run --with numpy python scripts/z56_k4bilin_firoute.py > data/z56/k4bilin/firoute.txt` (uses
  `scripts/z55_p415_sieve.py`; < 1 min).
* `gcc -O2 -o typeii scripts/z56_k4bilin_typeii.c -lm; ./typeii X CLASS` (X = 10⁸, 4·10⁸; CLASS = 97, 1).
* `gcc -O2 -o spectrum scripts/z56_k4bilin_spectrum.c -lm; ./spectrum X` (X = 10⁹, 10¹⁰; 10¹⁰ needs ≈ 3.3 GB, 10 s).
* Literature: `data/z56/k4bilin/lit_report.md` (research subagent; verification tags per claim).

## 10. Review log
(pending)
