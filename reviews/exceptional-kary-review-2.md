# Second hostile review: EXCEPTIONAL_KARY.md (headline Thm 4.5)

Reviewer: side-agent/review-kary-2. Subject: branch `side-agent/kary-comparison`
at `e35bf60` (includes Lemma 4.2′). First review:
`side-agent/review-kary:reviews/exceptional-kary-review.md` (all SOUND, ETw
inputs taken on trust). This review re-derives the ETw inputs from scratch,
re-derives KARY Thm 2.5 / Thm 4.1, and sanity-checks the headline.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered E1, E2, …
(E-prefix to avoid clashing with the first review's D-numbers.)

## Part 1 — ETw inputs, re-derived, and their use in KARY

### 1.1 ETw Lemma 1.3 (QR base) and Lemma 1.1 / Cor 1.2 — SOUND

* Lemma 1.1 re-derived: `A = (M+1)/4`, `gcd(A,M) = gcd(A,4A−1) = 1`; `D = sr²`,
  `D | A² ⇔ sr | A` (s squarefree), so `4s | M+1`. `(−4D|M) = (−1|M)(s|M) = −(s|M)`.
  For odd s, `M ≡ −1 (mod 4s)` gives `(M|s) = (−1|s)` and reciprocity with
  `(M−1)/2` odd gives `(s|M) = (−1|s)(−1)^{(s−1)/2} = 1`. For `s = 2s'`,
  `8 | M+1` ⇒ `(2|M) = 1`. Hence `(−4D|M) = −1`. Correct.
* Cor 1.2: n a nonzero QR at every `p | M` ⇒ `(n|M) = 1 ≠ (−4D|M)`. W-smooth
  Case-B moduli are odd, so only odd `p ≤ W` matter; `R_W` imposes exactly that.
* Lemma 1.3(2): the factor at odd `p^e ∥ Q₀` keeps `p^{e−1}(p−1)/2` of `p^e`
  residues; at `p = 2` nothing is imposed. `log(Q₀/|R_W|) = Σ_{3≤p≤W} log(2p/(p−1))`,
  independent of Q₀ and of the family. (3): a single class mod `p^e` has
  probability `≤ 2/(p^{e−1}(p−1)) = γ(p)/p^e`. CRT product ⇒ independence.
* Use in KARY: base term `O_B(1)` once `W = W₀(B)` is fixed; (R1) for the
  W-smooth classes; (R2) feeds Γ. Q₀ may be arbitrarily large (powers of small
  primes from the family's W-smooth parts) without affecting either. Within
  hypotheses.

### 1.2 ETw Lemma 2.2 (inflation) under KARY's law — SOUND

* Re-derived: for `m = Π p^e`, `Q'(n ≡ a mod m) = E[Π_p 1{n ≡ a mod p^e}]`.
  Peel coordinates from the last in the processing order: given everything
  earlier, the base factor is `≤ γ(p)/p^e` (R2, independence across p), and
  a coordinate `ℓ > W` has conditional law uniform on `Ω_ℓ ∖ F_ℓ` with
  `|F_ℓ|/ℓ^{E_ℓ} ≤ δ_ℓ` (light) or uniform (heavy). A class mod `ℓ^e`
  (`e ≤ E_ℓ`) is a union of `ℓ^{E_ℓ−e}` points, so its conditional
  probability is `≤ (1−δ_ℓ)^{−1}ℓ^{−e}` pointwise in the past. Product bound.
* KARY Lemma 2.1(2) gives exactly this conditional law for the plain rule
  (`P(y_ℓ=a | past) = ν_ℓ(a)1{a∉F_ℓ}/(1−p_ℓ)` when light). The c's do not
  enter the y-history, so the chain rule is over y alone. `δ_ℓ = ℓ^{−1/2} ≤ 1/4`
  needs `W ≥ 16` (ETw §2.3 assumes it; `W₀(B) ≥ 16` implicit — fine).
* γ′(ℓ) = (1−ℓ^{−1/2})^{−1} for ℓ > W (the decaying form; O7-1 repair present).

### 1.3 ETw Lemma 2.1′ (leak) and KARY Lemma 4.3 — SOUND

* Re-derived: a final history outside 𝒜 satisfies some class C. Pure-small C
  are excluded by (R1). Otherwise C is decided at its top prime ℓ (all
  cofactor primes are smaller, hence earlier in the increasing order; the
  W-smooth part is in the base; the top requirement mod `ℓ^v` is one
  coordinate mod `ℓ^{E_ℓ}`). When ℓ is processed, the other requirements are
  already met, so `y_ℓ` lies in the completing set `⊆ F_ℓ`. Light ℓ: impossible
  (`y_ℓ ∉ F_ℓ`). Heavy ℓ: `y_ℓ = c_ℓ` uniform, hit probability `p_ℓ` given the
  past. Union bound: `𝔏 ≤ Σ_ℓ E[p_ℓ 1{p_ℓ > δ_ℓ}]`.
* This covers all four block types of Thm 4.5 uniformly, including the
  singletons above `e^λ`: those must still condition at light ℓ (else the
  leak bound fails), and they do; their cost is 0 because f is constant in
  `y_ℓ`, not because σ = U. KARY's text ("singletons above `e^λ` (cost 0)")
  is correct but terse; ETw Cor 4.3 says the same.
* Cor 2.5 arithmetic: Markov `E[p1{p>δ}] ≤ E p²/δ`; with ε = 1/4,
  `Σ_{ℓ>W} ℓ^{1/2}·Cℓ^{−7/4} = CΣℓ^{−5/4} ≪ W^{−1/4}`. Uniform in the family
  and in λ because C(ε,B) is W-free (item 1.4).

### 1.4 ETw Lemma 2.4 / Lemma 4.0 (second moment, prime-power tops) — SOUND

* Re-derived. Write each modulus with top ℓ as `M = qℓ^v`, `(q,ℓ)=1`,
  `q ≤ ℓ^{1+B−v} ≤ ℓ^B`. The class `−4D (mod M)` contributes to `F_ℓ` only if
  `n ≡ −4D (mod q)` (all primes of q precede ℓ), and then contributes one class
  mod `ℓ^v`. So pointwise `p_ℓ ≤ Σ_v ℓ^{−v}N_{ℓ,v}(n)`. Expand `N²` over pairs
  of pairs; a compatible pair is one class mod `m = lcm(q,q')`, probability
  `≤ Γ(m)/m ≤ 3^{ω(m)}/m` (item 1.2; `γ(2)=1`, `γ(3)=3`, `γ(p) ≤ 5/2` for odd
  `5 ≤ p ≤ W`, `γ′(ℓ) ≤ 4/3` above W). `#{(q,q'): lcm = m} = τ(m²)` (2e+1 choices
  per `p^e ∥ m`). `τ(A_q²) ≤ C_ε ℓ^{ε/4}` since `A_q ≤ ℓ^{1+B}`. Euler product
  `Π_{p≤ℓ^{2B}}(1 + 9/p + O(p^{−2})) ≪ (2B log ℓ)^9`. Minkowski over v. The
  constant is **W-free** (only `Γ ≤ 3^ω` enters), which is what lets W₀(B) be
  chosen afterwards.
* Use in KARY (Lemma 4.2(3)): needs (a) item 1.2 for lcm's of cofactors —
  holds for KARY's law; (b) `p_ℓ` is the density of classes decided at ℓ —
  holds because in-block cofactor primes precede ℓ in the increasing order.
  ETw's "any order compatible with the sequential construction" is satisfied.
  Note the bound is pointwise in the full y-history, so KARY's in-block
  dependence (which ETw's windows lacked) is irrelevant.

### 1.5 ETw Lemma 2.6 → KARY Lemma 4.2′ (first moment on dyadic blocks) — SOUND

* Step 1 re-derived as in 1.4 with one class: `E 1{active} ≤ Γ(q)/q`, and
  `ℓ^{−v}Γ(q)/q ≤ Γ(M)/M` because `γ′ ≥ 1`; `≤ τ(A_M²)` values of D. Light mass
  `M_V ≤ Σ_{ℓ∈V} p_ℓ`.
* Step 2 is ET Lemma 3.1 / Cor 3.6 with `h(p) = γ′(p) − 1`: `h(2) = 0`,
  `h(3) = 2`, `h(p) ≤ 3/2` for `5 ≤ p ≤ W`, `h(ℓ) ≤ (4/3)ℓ^{−1/2}` above W. The two
  convergence conditions (Shiu range `Σ h(e)/φ(e) < ∞`; large divisors
  `Σ h(e)e^{−3/4} < ∞`) hold, with constant `K₀(W)` (a finite Euler product
  over `p ≤ W`, so `(log W)^{O(1)}`). This analytic mean value is an ET input,
  not an ETw one; it is window-free and B-free, and was reviewed with ET. I
  did not re-derive Shiu's theorem.
* Step 3 re-checked: `Σ_{M≤X} τΓ/M = S(X)/X + ∫_1^X S(x)x^{−2}dx ≤
  K₀(log²(X+2) + log³(X+2))`; `log X = 2(1+B)s ≥ 2log W ≥ 5.5` gives the
  factor 1.3 (`1.01³·(1+1/5) ≈ 1.24`). Dropping `P(M) ∈ V` is a valid upper
  bound (nonnegative terms). `M ≤ P(M)^{1+B} ≤ e^{2(1+B)s}`. Correct.
* Hypotheses: ETw Lemma 2.6 was stated for η-windows with `s_j ≤ λ`; the
  restriction `s_j ≤ λ` is not used in its proof, and Lemma 4.2′ restates the
  bound for any `V ⊆ (e^s, e^{2s}]`, `s ≥ log W`. Thm 4.5 has `s ≥ s₁ > 2log W`.
