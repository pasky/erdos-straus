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
