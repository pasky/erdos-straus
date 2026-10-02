# EXCEPTIONAL_TWIN — (E_δ), the heavy coordinates, and η-twin windows (task O1)

Status: **in progress.** Labels follow `DISCOVERIES.md`. PROVED means proved
here and checked internally only. Notation follows `EXCEPTIONAL_THETA.md`
(ET) and `EXCEPTIONAL_BALANCED.md` (EB).

## 0. Status at a glance

| item | statement | label |
|---|---|---|
| Lemma 1.1 | every Case-B class `−4D (mod M)` has Jacobi symbol `(−4D \| M) = −1` | PROVED (classical; Mordell) |
| Cor 1.2 | an n that is a nonzero square mod every prime of M avoids every class of ℛ(M) | PROVED |
| Lemma 1.3 | QR base: a product measure on small residues, supported on avoiders of all W-smooth classes, inflation `2p/(p−1)` per prime | PROVED |
| Thm 2.3 | sequential sieve limit with a *capped* measure: heavy coordinates are not conditioned but leak; no (NDE), no sup bound; cost ×2 + log 2 if leak ≤ 1/2 | PROVED |
| Lemma 2.4, Cor 2.5 | second moment `E_{Q'} p_ℓ² ≪_{ε,B} ℓ^{−2+ε}` (uniform in W); leak `≪_B W^{−1/4}` | PROVED |
| **Thm 2.7** | **(η,B)-gapped ℛ(M)-families: `S_λ ≪_B η^{−1}λ^{3/4}` unconditionally** — EB's (E_δ), (★_δ), H_light, (NDE) not needed | PROVED |
| §2.4 | capped measure on the real system (X = 10⁵, 10⁶, W = 30): leak 0.06–0.07 | EVIDENCE |
| Lemma 3.1, 3.2 | (E_δ) in u-form; values from q have Legendre sign `−(n\|q)` | PROVED |
| Heur 3.3 | entropy count predicts `sup_n\|F_ℓ\| ≈ π(y)ℓ^{o(1)}`, i.e. (E_δ) for δ < η/(1+η) | HEURISTIC; (E_δ) OPEN, no longer needed |
| Prop 4.1 | all classes (twin included) with top prime `≤ e^{λ^{1/4}}`: singleton windows, cost ≪ λ^{3/4} | PROVED |
| Lemma 4.2, Cor 4.3 | linear-window inequality (one prime per term); all classes with top prime `> e^{λ/2}` cost `O(e^{−λ/4})` | PROVED |
| **Thm 4.4** | cap `≪_B η^{−1}λ^{3/4}` for ℛ(M)-families with `M ≤ P(M)^{1+B}` unless an η-twin modulus has top prime in `(e^{λ^{1/4}}, e^{λ/2}]` | PROVED |
| Conj 4.5 | binary window inequality (2-prime local boost); would remove the twin range restriction | OPEN |

## 1. The quadratic-residue base (Mordell obstruction, used constructively)

### 1.1 Forced classes are Jacobi non-residues

**Lemma 1.1 (PROVED; classical, Mordell).** Let `M ≡ 3 (mod 4)`,
`A = (M+1)/4`, and `D | A²`. Then `gcd(D, M) = 1` and the Jacobi symbol
satisfies `(−4D | M) = −1`.

*Proof.* `gcd(A, M) = gcd(A, 4A−1) = 1`, so `gcd(D, M) = 1`. Write
`D = s r²` with s squarefree. Then `g(D) = s r`, and `D | A²` iff
`sr | A` (EB Lemma 4.1). So `4s | M+1`, i.e. `M ≡ −1 (mod 4s)`. Now
`(−4D|M) = (−1|M)(2|M)²(r|M)²(s|M) = −(s|M)`, because `M ≡ 3 (mod 4)`.
* If s is odd: reciprocity gives `(s|M) = (M|s)(−1)^{((s−1)/2)((M−1)/2)}`.
  Here `(M|s) = (−1|s) = (−1)^{(s−1)/2}` and `(M−1)/2` is odd. So
  `(s|M) = 1`.
* If s is even, `s = 2s'` with s' odd: `8 | M+1`, so `(2|M) = 1`, and
  `(s'|M) = 1` as before (`M ≡ −1 (mod 4s')`).

Hence `(−4D|M) = −1`. ∎

Check: `scripts/twin_jacobi_check.py` verifies the statement for all
159,390 classes with `M ≤ 20000`.

**Corollary 1.2 (PROVED).** Let n be an integer that is a nonzero quadratic
residue modulo every prime p | M. Then n lies in no class of ℛ(M).

*Proof.* `(n|M) = Π_{p^e ∥ M} (n|p)^e = 1 ≠ −1 = (−4D|M)`. ∎

This is the classical obstruction (Mordell; Schinzel; Elsholtz–Tao's
"odd-square" remark): polynomial ES identities never cover squares. Here it
is used in the opposite direction, as a cheap way to build measures that
live on avoiders.

### 1.2 The QR base

Fix `W ≥ 3`. Let `Q₀` be a common multiple of the W-smooth parts of all
moduli of the family, with `P_W | Q₀`. Put

    R_W = { c mod Q₀ : (c|p) = 1 for every odd prime p ≤ W }.

**Lemma 1.3 (QR base; PROVED).**
1. Every `c ∈ R_W` avoids every class of ℛ(M) whose modulus M is W-smooth.
   More generally, if `n mod Q₀ ∈ R_W`, the Jacobi factor `(n|q_s)` equals 1
   for every W-smooth odd `q_s`.
2. `log(Q₀/|R_W|) = Σ_{3≤p≤W} log(2p/(p−1)) = π(W) log 2 + O(log log W)`.
3. Under the uniform measure on `R_W`, the residues `c mod p^{e}` for
   distinct primes p are independent, and for every `a` and `p^e ∥ Q₀`,

       P(c ≡ a (mod p^e)) ≤ γ(p)/p^e,    γ(p) = 2p/(p−1) (p odd),  γ(2) = 1.

*Proof.* (1) Corollary 1.2, since every prime of M is ≤ W. The Jacobi factor
`(n|q_s)` depends only on n modulo the primes of `q_s`.
(2) By CRT, `R_W` is a product over the prime-power factors of Q₀. For odd
`p ≤ W` with `p^e ∥ Q₀` the factor has `p^{e−1}(p−1)/2` elements out of
`p^e`. (3) The product structure gives independence. A single residue
`a mod p^e` has probability `≤ 1/(p^{e−1}(p−1)/2) = (2p/(p−1))/p^e`. ∎

So the QR base is a **product** measure. This is the point: the base
inflation in every later estimate is the multiplicative weight γ, whose
Euler product over `p ≤ W` is `Π(1 + γ(p)/(p−1)) ≍ (log W)^{O(1)}`. The
uniform measure on the exact small-avoider set (ET Cor 3.6) has inflation
`≤ L' = e^{O(W^{1+C})}` instead, with no product structure.

## 2. Capped distortion: heavy coordinates leak instead of being conditioned

EB reduced the (η,B)-gapped balanced moduli to H_light, and H_light to the
sup statement (E_δ). This section shows that **no sup statement is needed**.
The device is the "distortion" trick of Balister–Bollobás–Morris–
Sahasrabudhe–Tiba (Erdős covering problem): condition the sequential measure
only where the hit probability is small, and let the remaining (heavy) hits
*leak*. The leaked mass is controlled by a second moment, i.e. by an
average, never by a supremum. The QR base of §1 keeps the base inflation
polylogarithmic, which is what makes the leak summable.

### 2.1 The capped sequential measure

**Setting.** As in ET §2.6: small modulus `Q₀`, slice primes 𝒫 (coprime to
Q₀) split into ordered windows `W₁ ⊔ … ⊔ W_J`, conditions `E_C` satisfying
(U), histories `H_{<j}`, sets `F_ℓ(h)` and `p_ℓ(h) = |F_ℓ(h)|/ℓ`. The small
residue set R must satisfy:
* (R1) every `c ∈ R` avoids every condition with `S(C) = ∅` (pure small);
* (R2) under the uniform law on R, `P(c ≡ a (mod p^e)) ≤ γ(p)/p^e` for all
  `p^e ∥ Q₀`, and the residues at distinct primes are independent.

`R_W` of Lemma 1.3 satisfies both for Case-B families. Fix thresholds
`δ_ℓ ∈ (0, 1/4]` for `ℓ ∈ 𝒫`.

**The capped measure `Q'`.** `c = n mod Q₀` is uniform on R. Given
`H_{<j} = h`, the residues `n mod ℓ` (`ℓ ∈ W_j`) are independent;
* if `p_ℓ(h) ≤ δ_ℓ` (ℓ is *light* at h), `n mod ℓ` is uniform on
  `ℤ/ℓ ∖ F_ℓ(h)`;
* otherwise (ℓ is *heavy* at h), `n mod ℓ` is uniform on `ℤ/ℓ`.

Higher digits of `n mod ℓ^{E_ℓ}` are uniform and independent. So `Q'` never
conditions at a heavy coordinate, and it needs no "no dead end" hypothesis.

The **leak** is `𝔏 := Q'(final history ∉ 𝒜)`.

**Lemma 2.1 (leak bound; PROVED).**
`𝔏 ≤ Σ_{ℓ∈𝒫} E_{Q'}[p_ℓ(H_{<j(ℓ)}) · 1{p_ℓ(H_{<j(ℓ)}) > δ_ℓ}]`.

*Proof.* A final history outside 𝒜 satisfies some condition C. Its
small part is not a pure small condition by (R1), so `S(C) ≠ ∅`; let
`ℓ = ℓ(C)`, in window j. At the transition into window j the history h
already meets every requirement of C except the one at ℓ, so `b_{C,ℓ} ∈
F_ℓ(h)` and `n mod ℓ ∈ F_ℓ(h)`. A light coordinate never takes such a value
under `Q'`. So ℓ was heavy at h, and the hit has conditional probability
`p_ℓ(h)`. Take a union bound over ℓ. ∎

**Lemma 2.2 (inflation; PROVED).** Let m be a product of prime powers
`p^e` with `e ≤ E_p` (`p ∤ Q₀`) or `p^e ∥ Q₀`. For every `a`,

    Q'(n ≡ a (mod m)) ≤ Π_{p^e ∥ m} γ'(p)/p^e,
    γ'(p) = γ(p) (p | Q₀),   γ'(p) = (1−δ_p)^{−1} (p ∈ 𝒫).

*Proof.* Chain rule over the base and the windows. At the base, (R2). At a
window, given any past, a light coordinate is uniform on at least
`p(1−δ_p)` residues, a heavy one on all p, and the higher digits are
uniform. ∎

This is ET Lemma 2.8 with `p*` replaced by the *cap* `δ_p`, which holds by
construction rather than by hypothesis.

### 2.2 The sequential bound with leak

**Theorem 2.3 (capped sequential sieve limit; PROVED).** In the setting
of §2.1, let ν be a majorant of level λ of 𝒜. If `𝔏 ≤ 1/2`, then

    log(1/Eν) ≤ log(Q₀/|R|) + log 2 + 2 Σ_j E_{Q'}[Φ_j^{light}(H_{<j})],      (2.1)

where `Φ_j^{light}(h)` is the right side of ET (2.3) for the coordinates
`ℓ ∈ W_j` that are light at h and have `log ℓ ≤ λ`, with `α = α_j`.
Windows with `log min W_j > λ` contribute 0.

*Proof.* Let `g_j(h) = E_U[ν | H_{<j} = h]` (uniform measure). We show by
downward induction on j that, for **every** history h at window j,

    g_j(h) ≥ E_{Q'}[ 1_𝒜(H_{<J+1}) · exp(−Σ_{i≥j} Φ_i^{light}(H_{<i})) | H_{<j} = h ].   (2.2)

*Base, j = J+1.* The full history decides membership in 𝒜, and ν ≥ 0
everywhere with ν ≥ 1 on 𝒜. So `g_{J+1}(h) ≥ 1_𝒜(h)`.

*Step.* Fix h. Under U given h, the window residues are independent and
uniform, so the hit indicators `x_ℓ = 1[n mod ℓ ∈ F_ℓ(h)]` are independent
`Bern(p_ℓ(h))`. Split them as `x = (x_L, x_H)` (light, heavy at h) and put

    f̃(x_L) = E_U[ g_{j+1}(H_{<j+1}) | H_{<j} = h, x_L ].

* `E f̃ = g_j(h)`, and `f̃ ≥ 0`.
* f̃ is λ-level in `x_L`. Given h, each term `1[n ≡ b_i (d_i)]` of ν has
  conditional expectation `Π_{ℓ ∈ T_i ∩ W_j} P(n ≡ b_i (ℓ^{·}) | h, x_ℓ)`
  times a factor independent of x, by independence of the window
  coordinates. Averaging over `x_H` leaves a function of
  `x_{T_i ∩ L}` only.
* Light coordinates have `p_ℓ(h) ≤ δ_ℓ ≤ 1/4` and `p_ℓ(h) < 1`.
* Given `x_L = 0`, the law of `H_{<j+1}` is exactly the `Q'` transition:
  light residues uniform off `F_ℓ(h)`, heavy residues uniform.

If `f̃(0) = 0`, (2.2) holds because its right side is
`≤ e^{−Φ_j(h)} f̃(0) = 0` by the last bullet and the induction hypothesis.
Otherwise ET Proposition 2.4 applied to `f̃/f̃(0)` gives
`E f̃ ≥ f̃(0) e^{−Φ_j^{light}(h)}`. By the last bullet and the induction
hypothesis, `f̃(0) = E_{Q'}[g_{j+1}(H_{<j+1}) | h]` is at least the
conditional expectation in (2.2) at j+1. Since `Φ_j^{light}(h)` is a function
of h, (2.2) follows at j. For windows above the level, f̃ is constant
(ET Step 0), and `Φ = 0`.

*Conclusion.* By (R1)–(R2) and `ν ≥ 0`,
`Eν ≥ (|R|/Q₀) · avg_{c∈R} g_1(c) ≥ (|R|/Q₀) · E_{Q'}[1_𝒜 e^{−S}]` with
`S = Σ_j Φ_j^{light} ≥ 0`. Jensen on the conditional law `Q'(· | 𝒜)` gives

    E_{Q'}[1_𝒜 e^{−S}] ≥ Q'(𝒜) · exp(−E_{Q'}[S 1_𝒜]/Q'(𝒜)) ≥ ½ · exp(−2 E_{Q'} S),

using `Q'(𝒜) = 1 − 𝔏 ≥ 1/2` and `S ≥ 0`. ∎

So the heavy coordinates cost nothing in (2.1). They enter only through
`𝔏`, which must be ≤ 1/2, and through Lemma 2.2's caps.

### 2.3 Application: (η,B)-gapped ℛ(M)-families, unconditionally

Fix `B ≥ 0`, `0 < η < 1` and `W ≥ 16`. Use EB's windows
`W_j = {ℓ : s_j < log ℓ ≤ s_{j+1}}` with `s₀ = log W`, `s_j = s₀(1+η)^{j−1}`,
the QR base `R = R_W`, and thresholds `δ_ℓ = ℓ^{−1/2}`. The family 𝔊
consists of
* ℛ(M)-classes with M (η,B)-gapped (EB §2.4) and `P(M) > W`, and
* any ℛ(M)-classes with W-smooth modulus.

The second kind is pure small and is avoided by `R_W` (Lemma 1.3(1)), so
(R1) holds. By EB Lemma 2.1, the first kind satisfies (U), with
`ℓ(C) = P(M)` and all cofactor primes in earlier windows or in `Q₀`.
Write `Γ(m) = Π_{p | m} γ'(p)` with γ' as in Lemma 2.2. Then `γ'(3) = 3`,
`γ'(p) ≤ 5/2` for odd `p ≥ 5`, `γ'(ℓ) ≤ 4/3` for `ℓ > W`, so
`Γ(m) ≤ 3^{ω(m)}`.

**Lemma 2.4 (second moment; PROVED).** For every `ε > 0` there is
`C(ε,B)`, independent of W, η and the family, such that for every prime
`ℓ > W`,

    E_{Q'}[ p_ℓ(H)² ] ≤ C(ε,B) · ℓ^{−2+ε}.

*Proof.* `|F_ℓ(h)|` is at most the number `N_ℓ(n)` of pairs `(q,D)` with
`q ∈ 𝒬_ℓ^{(B)}`, `D | A_q²` and `n ≡ −4D (mod q)`. Expand `N_ℓ²` as a sum
over pairs of pairs. A pair contributes `Q'(n ≡ a (mod lcm(q,q')))` if
compatible and 0 otherwise. By Lemma 2.2 this is `≤ Γ(m)/m ≤ 3^{ω(m)}/m`
with `m = lcm(q,q')`. Each q carries `τ(A_q²) ≤ C_ε' ℓ^{ε/4}` divisors D,
since `A_q ≤ ℓ^{B+1}` (take `C_ε'` for exponent `ε/(4(B+1))`). The number
of pairs (q,q') with `lcm = m` is `τ(m²)`. So

    E N_ℓ² ≤ C_ε'² ℓ^{ε/2} Σ_{m ≤ ℓ^{2B}} 3^{ω(m)} τ(m²)/m
           ≤ C_ε'² ℓ^{ε/2} Π_{p ≤ ℓ^{2B}} (1 + 9/p + Σ_{e≥2} 3(2e+1)p^{−e})
           ≪ C_ε'² ℓ^{ε/2} (2B log ℓ)^{9} ≪_{ε,B} ℓ^{ε}.

Divide by `ℓ²`. ∎

**Corollary 2.5 (leak; PROVED).** There is `W₀(B)` such that `𝔏 ≤ 1/2`
whenever `W ≥ W₀(B)`, uniformly in η and in the family.

*Proof.* Lemma 2.1 and Markov: `E[p 1{p > δ}] ≤ E[p²]/δ`. So
`𝔏 ≤ Σ_{ℓ>W} ℓ^{1/2} · C(1/4,B) ℓ^{−7/4} ≪_B W^{−1/4}`. ∎

**Lemma 2.6 (first moment, cubic windows; PROVED).** There is
`K = K(W,B)` such that for every window j with `s_j ≤ λ`,

    E_{Q'} Σ_{ℓ ∈ W_j} p_ℓ(H_{<j}) ≤ K · ((1+B)s_j)³.

*Proof.* By Lemma 2.2, as in ET Lemma 2.8, the left side is at most
`Σ_{M: P(M) ∈ W_j} τ(A_M²) Γ(M)/M`. Write `Γ(M) = Σ_{d | M} h(d)` with h
multiplicative, supported on squarefree d, `h(p) = γ'(p) − 1`. Then
`h(p) ≤ 2` for `p ≤ W` and `h(ℓ) ≤ 2ℓ^{−1/2}` for `ℓ > W`. This is the
weight structure of ET Cor 3.6 (there `h(p) ≤ 1/(p−1) + 3p^{−δ}`, here with
`δ = 1/2` and finitely many bounded exceptions `p ≤ W`). Its proof of
Lemma 3.1 goes through:
* Shiu range `d ≤ x^{1/2}`: needs `Σ_d h(d)/φ(d) < ∞` (a finite product
  over `p ≤ W` times a convergent one);
* large divisors: needs `Σ_d h(d) d^{−1+1/4} < ∞` (Euler factors
  `1 + O(p^{−5/4})` for `p > W`).

So `Σ_{M≤x, M≡3(4)} τ(A²)Γ(M) ≪_W x log²x`. Partial summation over
`M ≤ e^{(1+B)s_{j+1}}` with `P(M) > e^{s_j}`, as in EB Lemma 2.4, gives the
claim. ∎

**Theorem 2.7 (the gapped cap, unconditional; PROVED).** Fix `B ≥ 0` and
take `W = W₀(B)` (Corollary 2.5). For every `0 < η < 1`, every family 𝔊 as
above, and every majorant ν of level `λ ≥ log W`,

    log(1/Eν) ≤ C·K^{1/4}(1+B)^{3/4} η^{−1} λ^{3/4} + O_B(η^{−1} log²λ) + O_B(1),

with C absolute and `K = K(W₀(B),B)`. In particular `S_λ ≪_B η^{−1}λ^{3/4}`.

*Proof.* Theorem 2.3 applies by Corollary 2.5. The R-term is
`log(Q₀/|R_W|) = O_B(1)` (Lemma 1.3). The light profile is at most the full
profile, so Lemma 2.6 bounds it and, by concavity,
`E log(16μ_j + 16)`. The window sum of `E_{Q'}Φ_j^{light}` is then exactly
the computation in the proof of EB Theorem 2.5, with `K = K(W,B)` and with
no heavy-charge term. Multiply by 2 as in (2.1). ∎

**What this removes.** For each fixed B, the (η,B)-gapped part of the
balanced door no longer depends on anything open:
* (E_δ), (★_δ), H_light and (NDE) of EB are **not needed**. EB Prop 4.4 is
  superseded, and EB Conj 4.4W is moot.
* The heavy histories seen numerically in EB §3.1 are harmless: they leak
  with total probability `≪ W^{−1/4}`.
* The pure small conditions (all W-smooth classes, of any shape, twin or
  not) are absorbed into the R-term `≈ π(W) log 2`.
* ET Cor 3.6 is recovered for ℛ(M)-classes (dominant moduli are
  (η, C)-gapped), with a different R-term.

**Scope (what it does not cover).**
* η-twin moduli: (U) fails, see §4.
* Gapped moduli with `log M/log P(M)` unbounded: Lemma 2.4 uses
  `τ(A_q²) ≤ ℓ^{o(1)}`, i.e. `q ≤ ℓ^B`, and there is still no summation
  over B (EB review D19).
* (a,D)-classes and Case-A classes: Lemma 1.1 is proved for ℛ(M) only.
  EB's balanced analysis is also restricted to ℛ(M).

### 2.4 Numerics: the capped measure on the real system (EVIDENCE)

`scripts/twin_capped.py` samples `Q'` on the full Case-B system (all ℛ(M),
`M ≤ X`, all types including twin), primes in increasing order (singleton
windows), QR base for `p ≤ W = 30`. It asserts Lemma 1.3(1) on every sample
(no class with top prime ≤ W is ever hit; it never fired). Thresholds
`δ_p = p^{−κ}`.

| X | samples | κ | expected leak `E Σ p 1{heavy}` | realised leak | where |
|---|---:|---:|---:|---:|---|
| 10⁵ | 100 | 0.2 | 0.056 | 4% | primes 32–127 only |
| 10⁶ | 20 | 0.2 | 0.070 | 5% | primes 32–127 only |
| 10⁵ | 100 | 0 (δ = 1/4) | 5.67 | 100% | primes 32–255 |
| 10⁵ | 100 | 0.5 | 25.5 | 100% | everywhere below 2¹⁷ |

Reading.
* With a threshold of order 1/2 just above W (κ = 0.2: `δ_31 ≈ 0.50`),
  the leak is already far below 1/2 at these toy scales, for the full
  system, twin included, at both X. No heavy coordinate occurs above 128.
* The theorem's choice κ = 1/2 is far outside the asymptotic regime here:
  typical `p_ℓ ≈ (log X)³/ℓ` exceeds `ℓ^{−1/2}` for all `ℓ ≲ (log X)⁶`. The
  proof allows any fixed `κ ∈ (0,1)` (Lemma 2.6 needs `Σ_p p^{−1−κ/2} < ∞`,
  Corollary 2.5 needs `Σ_ℓ ℓ^{κ−2+ε} < ∞`), so W₀(B) is large but finite.
* Right above W the QR base *raises* hit probabilities: classes whose
  W-smooth part is compatible with the QR residues get weight `≈ 2^{ω}`.
  Lemma 1.1 caps their contribution at ℓ: every value they produce is a
  non-residue mod ℓ.

## 3. The extremal statement (E_δ) itself

Theorem 2.7 takes (E_δ) off the critical path. It is not settled here.
This section records what was found about it.

**Lemma 3.1 (u-form; PROVED).** For every integer n,

    F_ℓ(n) = { −(4u)^{−1} mod ℓ : u = sk², 4sk | qℓ+1, q | 4un+1, q ∈ 𝒬_ℓ }.

So the value depends only on u, and q is activated iff `q | 4un+1`.
Equivalently, with `N ≡ −(4n)^{−1}` modulo `lcm 𝒬_ℓ`: u is active iff
`u − N` has a divisor `q ∈ 𝒬_ℓ` with `q ≡ −ℓ^{−1} (mod 4sk)`.

*Proof.* EB Lemma 4.1 gives values `−r/k` with `4srk = qℓ+1`. Modulo ℓ,
`r ≡ (4sk)^{−1}`, so `−r/k ≡ −(4sk²)^{−1}`. Modulo q, `4srk ≡ 1`, so
`4sk(nk+r) ≡ 4sk²n + 1`, and `4sk` is a unit mod q. ∎

**Lemma 3.2 (sign constraint; PROVED).** A value v produced at ℓ by a
cofactor q satisfies `(v|ℓ) = −(n|q)`. In particular, if `(n|q) = 1` for
every active q, then `|F_ℓ(n)| ≤ (ℓ−1)/2`.

*Proof.* Lemma 1.1 for `M = qℓ`: `(n|q)(v|ℓ) = (−4D|q)(−4D|ℓ) = −1`. ∎

**Heuristic 3.3 (entropy count; HEURISTIC).** The residue of n modulo
`lcm 𝒬_ℓ^{(B)}` carries `≈ Bπ(y)log ℓ` nats. If the activation sets
`S_q = {−1/(4u)}` were independent random sets of size `ℓ^{o(1)}`, a first
moment over sets of m simultaneously active cofactors of size ≈ ℓ^{B'}
gives `m log m ≲ B π(y) log ℓ`, so `sup_n |F_ℓ(n)| ≈ π(y)ℓ^{o(1)}`. This
matches Prop 4.3 of EB (dominant witnesses) and the greedy data of EB §4.3.
It predicts (E_δ) for every `δ < η/(1+η)`. A counterexample would need
*coherent* activation sets. The only coherent family found is small u
(`u = 1` is active for every q when `n ≡ −1/4`), and it produces a single
value; for `n ≡ −r₀/k₀` of small height the count is a divisor sum,
`(log ℓ)^{O(1)}` on average.

**Status.** (E_δ) is OPEN in both directions. It is no longer needed for
the balanced door (Theorem 2.7). It remains a natural extremal problem:
how many cofactors `q ≤ ℓ^B` can a single residue activate with distinct
values?

## 4. η-twin moduli

### 4.1 What breaks

An η-twin modulus has its two top primes `ℓ₁ < ℓ₂` in the same window (or
`P(M)² | M`). Hypothesis (U) fails: inside the window the condition is a
*binary* event `(n mod ℓ₁, n mod ℓ₂) = (b₁, b₂)`, and ET Proposition 2.4
needs independent single-coordinate hit indicators. The capped measure of
§2 does not help with this: it controls *which* coordinates are
conditioned, not the window inequality. Throughout this section B is fixed,
all ℛ(M)-classes considered have `M ≤ P(M)^{1+B}`, and the QR base, the
caps `δ_ℓ = ℓ^{−1/2}`, `W = W₀(B)` and the leak bookkeeping are as in §2.

Two facts used below hold for twin classes verbatim:
* Lemma 2.4 (second moment) never used `P(q) ≤ y`; it holds for all
  cofactors `q ≤ ℓ^B` with `P(q) < ℓ` (or `P(q) = ℓ` for `ℓ² | M`, where the
  coordinate is `n mod ℓ^{E_ℓ}` and each class still contributes `≤ 1/ℓ`).
  So the leak bound, Corollary 2.5, covers the whole family.
* Lemma 2.6 (first moment) sums over all M with `P(M)` in a range; twin M
  are included.

The leak argument (Lemma 2.1, Theorem 2.3) also holds if a window is
processed *sequentially inside itself* (primes in increasing order), as
long as the window inequality used in the induction step is valid for the
resulting in-window law. Lemma 2.2 holds for any such order.

### 4.2 Low range: twin classes below `e^{λ^{1/4}}` are free

**Proposition 4.1 (PROVED).** Put `s₁ = λ^{1/4}`. Process every prime
`ℓ ∈ (W, e^{s₁}]` as its own window. Then every ℛ(M)-class with
`P(M) ≤ e^{s₁}` (any shape: gapped, twin, `P(M)² | M`) satisfies (U) for
these windows, and the total cost of these windows in (2.1) is at most
`(8/3)·K'(W,B)·(1+B)³·λ^{3/4}`.

*Proof.* A singleton window `{ℓ}` meets every condition with top prime ℓ
in exactly one prime, so (U) holds (for `ℓ² | M`, use the coordinate
`n mod ℓ^{E_ℓ}`). For a singleton window the induction step needs no
Proposition 2.4: if ℓ is light at h, `E f̃ = (1−p)f̃(0) + p f̃(1) ≥
(1−p)f̃(0)`, so `Φ = −log(1−p_ℓ(h)) ≤ (4/3)p_ℓ(h)`; if ℓ is heavy, the
window is skipped and the hit leaks. By Lemma 2.2 (as in Lemma 2.6),
`Σ_{W<ℓ≤e^{s₁}} E_{Q'} p_ℓ ≤ Σ_{M ≤ e^{(1+B)s₁}} τ(A_M²)Γ(M)/M ≤
K'((1+B)s₁)³`. Multiply by 4/3 and by the factor 2 of (2.1). ∎

So in this range windows are not needed at all: the cost is the void
(≈ mass), which is what EB Theorem 2.5 pays there anyway (its "cubic
branch", `Σ_{s_j ≤ s*} X_j`).

### 4.3 Top range: linear windows are free

**Lemma 4.2 (linear window inequality; PROVED).** Let V be a set of
coordinates with independent uniform laws `U_ℓ`, and let
`f(y_V) = c₀ + Σ_{ℓ∈V} g_ℓ(y_ℓ) ≥ 0` with `E_{U_ℓ} g_ℓ = 0`. Let σ be any
probability law on `Π_ℓ ℤ/ℓ^{E_ℓ}` whose one-coordinate marginals satisfy
`σ_ℓ ≤ (1+ε_ℓ)U_ℓ` and `Σ_y (U_ℓ − σ_ℓ)⁺(y) ≤ δ_ℓ`. Then

    E_U f ≥ E_σ f / (1 + max_ℓ(ε_ℓ + δ_ℓ)).

*Proof.* `E_U f = c₀`. Put `m_ℓ = −min g_ℓ ≥ 0`. Since f ≥ 0 at the point
where every `g_ℓ` is minimal, `Σ m_ℓ ≤ c₀`. With `r = dσ_ℓ/dU_ℓ`,
`E_σ g_ℓ = E_U[g_ℓ(r−1)] ≤ E_U[g_ℓ⁺(r−1)⁺] + E_U[g_ℓ⁻(1−r)⁺] ≤ ε_ℓ E_U g_ℓ⁺
+ m_ℓ δ_ℓ ≤ m_ℓ(ε_ℓ+δ_ℓ)`, using `E_U g⁺ = E_U g⁻ ≤ m_ℓ`. Sum over ℓ. ∎

**Corollary 4.3 (PROVED).** Let `V = {ℓ : λ/2 < log ℓ ≤ λ}` be one window,
processed sequentially inside itself with caps. Every condition with top
prime in V satisfies the in-window (U), whatever its shape, and the window
costs at most `log(1 + 3e^{−λ/4})` in (2.1).

*Proof.* A term of ν has level ≤ λ, so it involves at most one prime of
V. Hence `f(y_V) = E_U[g_next | h, y_V]` has the form of Lemma 4.2 (as a
function of the residues, not of hit indicators). Take σ = the in-window
sequential capped law. Each one-coordinate marginal is a mixture of laws
uniform on at least `ℓ(1−δ_ℓ)` residues, so `ε_ℓ ≤ 2δ_ℓ` and
`δ_ℓ`-TV `≤ δ_ℓ`, with `δ_ℓ = ℓ^{−1/2} ≤ e^{−λ/4}`. Given h, f̃'s value
under σ is the expectation of `g_next` under the `Q'` transition. Windows
above `e^λ` are invisible and cost 0 (ET Step 0), in any order. ∎

This is EB's route 4. Lemma 4.2 is special to one coordinate per term:
for two, `f = (Σ_ℓ z_ℓ)²` with mean-zero `z_ℓ` has `Σ_ℓ max z_ℓ⁻`-type
quantities of order m² against `E f = m`, and the argument breaks.

### 4.4 What is proved, and the residual range

**Theorem 4.4 (PROVED).** Fix B and `W = W₀(B)`. Let 𝔊 be any family of
ℛ(M)-classes with `M ≤ P(M)^{1+B}`, plus any W-smooth classes, such that
every **η-twin** modulus M of 𝔊 has

    P(M) ≤ e^{λ^{1/4}}   or   P(M) > e^{λ/2}.

Then every majorant of level λ satisfies `log(1/Eν) ≪_B η^{−1}λ^{3/4}`.

*Proof.* Windows: singletons on `(W, e^{λ^{1/4}}]` (Prop 4.1); EB's
η-windows on `(e^{λ^{1/4}}, e^{λ/2}]`, where only gapped classes have their
top prime, so (U) holds by EB Lemma 2.1; one sequential window V on
`(e^{λ/2}, e^λ]` (Corollary 4.3); singletons above. Theorem 2.3 applies by
Corollary 2.5. The middle windows cost what they cost in Theorem 2.7. ∎

**The residual.** η-twin moduli whose top prime lies in
`(e^{λ^{1/4}}, e^{λ/2}]`. There a term of ν may involve
`2 ≤ d_j = ⌊λ/s_j⌋ < λ^{3/4}` primes of a window, and the window's twin
mass is large (`≍ η s_j³ ≫ 1` heuristically, ≥ `c_η s_j³` summed over a
dyadic range by ET Lemma 3.8).

### 4.5 The missing window inequality, and why the obvious routes fail

**Conjecture 4.5 (binary window inequality; OPEN).** Let V be a window of
primes with costs `s_ℓ ∈ (s, (1+η)s]`, residues `y_ℓ` independent uniform,
unary forbidden sets with `p_ℓ ≤ 1/4`, and binary forbidden sets
`F_{ℓℓ'} ⊆ ℤ/ℓ × ℤ/ℓ'` of density `π_{ℓℓ'}`. Let σ be the in-window
sequential law (primes in increasing order; at ℓ, uniform off the unary set
and off the binary sets activated by the earlier residues; capped as in §2).
Then for every λ-level `f ≥ 0` and every α > 0,

    log(E_σ f / E_U f) ≤ C[ αλ + Σ_ℓ p_ℓ e^{−α s_ℓ} + Σ_{ℓ<ℓ'} π_{ℓℓ'} e^{−α(s_ℓ+s_ℓ')} ]
                         + O(log(2+λ/s) + log(2+μ)),

μ the total (unary + binary) mass.

This is EB's route 3 (local boost) in the 2-prime case. With the binary
profile bounded by Lemma 2.6, Conjecture 4.5 would remove the range
restriction in Theorem 4.4, for every fixed B. The binary term carries
`e^{−2αs}`, i.e. a binary condition costs its full modulus, which is the
H_MS heuristic.

**Why the routes tried here do not prove it.** In each case the obstruction
is quantitative and is stated at the scale of a window with `s > λ^{1/4}`.
1. *Splitting windows* (finer windows of log-ratio `1+η'`, or random
   sub-windows). A binary condition is resolved only if its two primes fall
   in different sub-windows. The unresolved twin mass is heuristically
   `≍ η'·λ³` in total (HEURISTIC: the η'-dependence of ET Lemma 3.8's
   supply is not proved), so `η' ≲ λ^{−3}` is needed, i.e. `≳ λ³` windows,
   each paying `≥ αλ + O(log λ)`.
2. *Over-conditioning* (forbid one end of every binary condition, which
   makes the system unary and independent). Given a typical history, the
   number of active binary conditions with a given lower prime ℓ₁ is
   `≍ #(primes in V)·(log X)^{O(1)}`, which exceeds ℓ₁ by a factor
   `≍ e^{ηs}`: everything is forbidden. A binary condition has codimension
   2; making it codimension 1 multiplies its weight by ≈ `e^{s}`.
3. *Leak.* Under any unary-conditioned law the expected number of binary
   hits in V is the window's twin mass, `≫ 1` for `s ≫ 1`.
4. *Void* (condition the product law on "no binary hit"). Costs the twin
   void ≈ twin mass ≈ `η s³` per window. This is fine exactly for
   `s ≲ λ^{1/4}` (Proposition 4.1) and too large above, where the
   sieve-limit cost of the window is `(λ/s)(1 + log(s⁴/λ))`.
5. *One coordinate per term* (Lemma 4.2) needs `d_j = 1`, i.e. `s > λ/2`.
   For `d ≥ 2` a λ-level f can exploit unary avoidance (this is the sieve),
   so no bound of the form `1 + O(max p)` can hold, and Proposition 2.4's
   interpolation is needed. Its proof (thinning, symmetrisation over each
   band, interpolation in the band counts) uses independence of the
   coordinates in an essential way; with binary conditions the hit
   indicators at the upper primes depend on all residues at the lower ones.

An observation that supports the conjecture (HEURISTIC; one test function,
first order in the binary densities): for `f = (Σ_ℓ z_ℓ(y_ℓ))²` with `|z_ℓ| ≤ 1`, `E z_ℓ = 0`, the
binary conditions change `E f` by at most `2Σ_{ℓ<ℓ'} π_{ℓℓ'}·(1+o(1))`
(each forbidden pair shifts one covariance by `≤ 1/(ℓℓ')` per forbidden
point), against `E_U f = m = #V`. So a level-2 *quadratic* test sees the
binary system only through its mass, not through `e^{s}`-inflated weights.

## 5. What this says about the global question

Question (3): is 3/4 sharp for all nonnegative CRT majorants of forced
classes with moduli `≤ N^{O(1)}`?

**Proved here (internally).** For each fixed B, the cap
`S_λ ≪_B η^{−1}λ^{3/4}` (with `λ ≍ L = log N` by ET Lemma 2.9) holds for
every family of ℛ(M)-classes with `M ≤ P(M)^{1+B}`, plus all W₀(B)-smooth
classes, in which no η-twin modulus has its top prime in
`(e^{λ^{1/4}}, e^{λ/2}]` (Theorem 4.4). This includes:
* all dominant and all η-gapped balanced moduli (Theorem 2.7), with no
  hypothesis. EB's (E_δ), (★_δ), H_light and (NDE) are not needed;
* all η-twin moduli with top prime `≤ e^{λ^{1/4}}` or `> e^{λ/2}`.

**Not covered.**
1. η-twin moduli with top prime in `(e^{λ^{1/4}}, e^{λ/2}]` — reduced to
   Conjecture 4.5. This carries a positive proportion of the cubic supply
   (ET Lemma 3.8), so it is the genuine open core.
2. Moduli with `log M / log P(M)` unbounded. Every proof here is for fixed
   B, with constants `W₀(B)`, `K(W₀(B),B)` that are not tracked; there is no
   summation over B. (Unweighted, the share of moduli with
   `P(M) < M^{1/(1+B)}` is `ρ(1+B)` by Dickman; the weighted share is not
   known.)
3. (a,D)-classes and Case-A classes: Lemma 1.1 is proved for ℛ(M) only.
   For these, ET Cor 3.6 still covers the dominant part.

**Verdict.** Not settled. The balanced door is now reduced to a single
named inequality about one window with binary conditions (Conjecture 4.5),
plus the uniformity in B. Nothing found here points towards (B): every
mechanism examined (heavy histories, small-prime correlations, η-gapped
balance) turned out harmless once the measure was chosen correctly.

## Replay

```
# Lemma 1.1: Jacobi symbol of every Case-B class, M <= 20000 (~1 min)
PYTHONPATH=scripts uv run --with sympy python scripts/twin_jacobi_check.py 20000
# §2.4: capped measure Q' with QR base, real system (X=1e5: ~3 min per run; X=1e6, 20 samples: ~40 min, < 4 GB)
cd scripts
uv run python twin_capped.py 100000 100 30 0.2 > ../data/twin/capped_X1e5_W30_k0.2.txt
uv run python twin_capped.py 100000 100 30 0   > ../data/twin/capped_X1e5_W30_k0.txt
uv run python twin_capped.py 100000 100 30 0 dom,gapM,gapB > ../data/twin/capped_X1e5_W30_k0_gapped.txt
uv run python twin_capped.py 100000 100 30 0.5   # 25.5 expected leak, quoted in §2.4 (not saved)
uv run python twin_capped.py 1000000 20 30 0.2 > ../data/twin/capped_X1e6_W30_k0.2.txt
```
