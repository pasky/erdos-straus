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
| Remark 1.4 | square base (all unit squares, incl. p = 2): avoids every class containing no square; (a,D)/Case-A classes contain none in tests | EVIDENCE (base only) |
| Thm 2.3 | sequential sieve limit with a *capped* measure: heavy coordinates are not conditioned but leak; no (NDE), no sup bound; cost ×2 + log 2 if leak ≤ 1/2 | PROVED |
| Thm 2.3′, Lemma 2.1′ | abstract sequential step: any blocks + step inequality + leak; leak lemma for in-block sequential orders | PROVED |
| Lemma 2.4, Cor 2.5 | second moment `E_{Q'} p_ℓ² ≪_{ε,B} ℓ^{−2+ε}` (uniform in W); leak `≪_B W^{−1/4}` | PROVED |
| Remark 2.5′ | all of §§2.3, 4 for caps `min(1/4, ℓ^{−κ})`, any κ ∈ (0,1) | PROVED |
| **Thm 2.7** | **(η,B)-gapped ℛ(M)-families: `S_λ ≪_B η^{−1}λ^{3/4}` unconditionally** — EB's (E_δ), (★_δ), H_light, (NDE) not needed | PROVED |
| §2.4 | capped measure on the real system: theorem-compatible caps give leak 0 at W = 300 (X = 10⁵); looser caps give 0.06–0.07 at W = 30 (X = 10⁵, 10⁶) | EVIDENCE |
| Lemma 3.1, 3.2 | (E_δ) in u-form; values from q have Legendre sign `−(n\|q)` | PROVED |
| Heur 3.3 | entropy count predicts `sup_n\|F_ℓ\| ≈ π(y)ℓ^{o(1)}`, i.e. (E_δ) for δ < η/(1+η) | HEURISTIC; (E_δ) OPEN, no longer needed |
| Lemma 4.0 | second moment with prime-power top primes (M = qℓ^v) | PROVED |
| Prop 4.1 | all classes (twin, prime-power included) with top prime `≤ e^{λ^{1/4}}`: singleton windows, cost ≪ λ^{3/4} | PROVED |
| Lemma 4.2, Cor 4.3 | linear-window inequality (one prime per term); all classes with top prime `> e^{λ/2}` cost `O(e^{−λ/4})` | PROVED |
| **Thm 4.4** | cap `≪_B η^{−1}λ^{3/4}` for ℛ(M)-families with `M ≤ P(M)^{1+B}` in which every modulus with top prime in `(e^{λ^{1/4}}, e^{λ/2}]` is window-resolved (all gapped ones are) | PROVED |
| Lemma 6.1–6.3 | soft-unary Prop 2.4; composition; Markov removal of high-incidence residues | PROVED |
| Conj 6.4 | k-ary comparison inequality (arithmetic-free, weak `d log(mass)` form): product law vs its sequential k-ary conditioning | OPEN (sharpened gap) |
| Prop 6.5 | Conj 6.4 ⇒ `S_λ ≪_B η^{−1}λ^{3/4}log λ` for all ℛ(M) with M ≤ P(M)^{1+B}, twins included | PROVED |
| §6.4 | exact toy window LPs: binary constraints extract a smaller share of their void than unary; the sequential σ is costly in dense toys | EVIDENCE (weak) |
| Lemma 6.6 | fibre tilting for Λ² majorants: `saving(g²) ≤ αλ/2 + log(Q_F/\|R\|) + avg_{c∈R}Ξ_c` (removes ET's fibre-variance term) | PROVED |
| Red 6.7, Conj 6.8 | H_MS^{Sel} (Λ² cap, all ℛ(M), any B, twins) ⇐ empty-fibre density + good fibres (SKETCH) + sparse noise stability via cluster expansion (Conj 6.8; binary case plausibly within reach via POINTWISE_OMEGA2 Lemma 2.1) | SKETCH / OPEN |
| Lemma 6.9 | two-prime events, good fibre: Mayer/Kotecký–Preiss expansion converges for the single and doubled systems (Penrose + PO2 Lemma 2.1), δ ≤ e^{−6}/8 | PROVED |
| (6.1) | single-edge diagonal bound: too strong as stated (Lemma 6.11), replaced by (6.2) | superseded |
| Lemma 6.10, 6.11 | gluing identity `Z₂/Z₁² = E_S[1 + E(r−1)²]`; one shared prime gives `ρ̃_j Var(deg_j)` | PROVED |
| (6.2)/(6.3) | `Ξ_bin ≤ C[Σ_e ρ̃ρ̃′π_e + Σ_j ρ̃_j q_j]` via approximate factorisation of the pinned density; both terms proved summable; this is the remaining step for the two-prime Λ² cap | OPEN |
| Conj 4.5_r | r-ary window inequality (local boost), `r ≤ (1+B)(1+η)`; would remove the residual. r = 2 alone does not suffice | OPEN |

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
   distinct primes p are independent, and for every `a` and every `p^e | Q₀`,

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

**Remark 1.4 (square base; review S1).** Replace `R_W` by the *square
base*: `n mod p^e` a unit square for every `p^e ∥ Q₀`, including `p = 2`
(inflation `γ(2) ≤ 8`). It is still a product measure. A class mod G that
contains no integer square mod G has, by CRT, some `p^e ∥ G` at which its
residue is not a square, so the square base avoids it. For ℛ(M) this is
Lemma 1.1. `scripts/twin_square_base_check.py` finds **no** square mod G in
all 12,000 (a,D)-classes `−(4D+a) mod 4a·g(D)` with `a ≤ 40`, `D ≤ 300`, and
in all 16,406 Case-A classes `−m^{−1} mod 4g(d)`, `m | 4d+1`, with
`d ≤ 3000` (EVIDENCE; the Mordell / Elsholtz–Tao obstruction predicts it,
but no proof is written here). Only the base changes; Lemma 2.4 and the
gapped structure for (a,D)-moduli are not done.

## 2. Capped distortion: heavy coordinates leak instead of being conditioned

EB reduced the (η,B)-gapped balanced moduli to H_light, and H_light to the
sup statement (E_δ). This section shows that **no sup statement is needed**.
The device is a variant of the *distortion method* (Hough, Ann. Math. 181
(2015); Balister–Bollobás–Morris–Sahasrabudhe–Tiba, "On the Erdős covering
problem: the density of the uncovered set", arXiv:1811.03547, Invent.
Math. 228 (2022), def. (5) and Thm 3.1). In BBMST the sequential measure is
distorted at every prime, by at most a fixed factor at heavy fibres, and
the result bounds the density of the uncovered set, i.e. the majorant
`1_𝒜` only. Here the variant is: condition fully at light coordinates, do
not condition at all at heavy coordinates (they stay uniform), and let the
heavy hits *leak*. Full conditioning at light coordinates is what ET
Prop 2.4 needs for general level-λ majorants; leaving heavy coordinates
uniform is what makes Lemma 2.2's inflation cap hold by construction. The leaked mass is controlled by a second moment, i.e. by an
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
`p^e` with `e ≤ E_p` (`p ∤ Q₀`) or `p^e | Q₀` (partial powers allowed;
(R2) is stated for all `p^e | Q₀`, and marginalisation gives it from
`p^e ∥ Q₀`). For every `a`,

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

### 2.2′ The abstract sequential step (review T5)

§4 uses blocks that are not windows in the sense of (U). The proof of
Theorem 2.3 uses only three inputs, so it is stated abstractly.

**Setting.** Q₀, R with (R1)–(R2); coordinates `y_ℓ = n mod ℓ^{E_ℓ}` for
the primes `ℓ > W` of the family, independent and uniform under U; an
ordered partition of these primes into **blocks** `V_1, …, V_J`; for each
block j and each history h (base residue and the blocks before j) a
probability law `σ_j(h)` on `Ω_{V_j} = Π_{ℓ∈V_j} ℤ/ℓ^{E_ℓ}`. `Q'` is the law
of the history built by drawing the base uniformly from R and then each
block from `σ_j(h)`. A function on `Ω_{V_j}` is *λ-level* if it is a sum of
terms each depending on `y_T` with `Σ_{ℓ∈T} log ℓ ≤ λ`.

**Theorem 2.3′ (abstract sequential sieve limit; PROVED).** Assume
* (S) *step inequality:* for every j, every h, and every λ-level `f ≥ 0`
  on `Ω_{V_j}`, `E_U f ≥ e^{−Φ_j(h)} E_{σ_j(h)} f`, with `Φ_j(h) ≥ 0`;
* (L) *leak:* `𝔏 = Q'(final history ∉ 𝒜) ≤ 1/2`.

Then every majorant ν of level λ of 𝒜 satisfies
`log(1/Eν) ≤ log(Q₀/|R|) + log 2 + 2 Σ_j E_{Q'}Φ_j(H_{<j})`.

*Proof.* Let `g_j(h) = E_U[ν | H_{<j} = h]`. Given h, the block residues are
independent and uniform under U, so `f(y) := g_{j+1}(h, y)` equals
`E_U[ν | h, y_{V_j}]`. Each term `1[n ≡ b_i (d_i)]` of ν contributes a
function of `y_{T_i ∩ V_j}` (times a constant), so f is λ-level, and f ≥ 0.
By (S), `g_j(h) = E_U f ≥ e^{−Φ_j(h)} E_{σ_j(h)}[g_{j+1}(h, Y)]`. Downward
induction from `g_{J+1} ≥ 1_𝒜` gives (2.2), and the conclusion follows as in
Theorem 2.3. ∎

**Instances.**
* *Window step* (Theorem 2.3): `V_j` a window satisfying (U), `σ_j(h)` the
  product capped law. (S) holds with `Φ_j = Φ_j^{light}`: put
  `f̃(x_L) = E_U[f | x_L]`, which is λ-level in the light indicators; then
  `E_σ f = f̃(0)`, and ET Prop 2.4 applies.
* *Singleton step* (Prop 4.1): `V_j = {ℓ}`, σ uniform off `F̂_ℓ(h)` if
  light, uniform if heavy. (S) holds with `Φ = −log(1−p_ℓ(h))` resp. 0,
  since `E_U f ≥ (1−p)E_σ f` for `f ≥ 0`.
* *Linear step* (Cor 4.3): V with one block prime per term, σ the
  in-block sequential capped law; (S) is Lemma 4.2.
* Conjecture 4.5_r is exactly a step inequality (S) for unresolved blocks.

**Lemma 2.1′ (leak for sequential orders; PROVED).** Fix a total order of
the primes `> W` that refines the block order. Suppose every condition C
of the family, other than pure small ones (excluded by (R1)), is
*decided at* a prime `ℓ(C)`: all its requirements other than the one at
`ℓ(C)` concern the base or primes earlier in the order. Suppose also that,
within each block, `σ_j(h)` draws the coordinates in this order, with
`y_ℓ` uniform off `F̂_ℓ(past)` if `p_ℓ(past) ≤ δ_ℓ` and uniform otherwise.
Here `F̂_ℓ(past) ⊆ ℤ/ℓ^{E_ℓ}` is the set of residues completing a condition
decided at ℓ, and `past` is everything earlier in the order. Then
`𝔏 ≤ Σ_ℓ E_{Q'}[p_ℓ 1{p_ℓ > δ_ℓ}]`.

*Proof.* As Lemma 2.1, with "window" replaced by "position in the order".
∎

Lemma 2.1 is the case of windows satisfying (U), where within a window
the order is irrelevant because F̂ depends only on earlier windows.

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
`q ∈ 𝒬_ℓ^{(B)}`, `D | A_q²` and `n ≡ −4D (mod q)`. (N_ℓ counts all
cofactors `q ≤ ℓ^B`, so it is a function of the *full* `Q'` history, not of
`H_{<j(ℓ)}`; the bound `|F_ℓ(H_{<j})| ≤ N_ℓ(n)` holds pointwise, and
expectations below are over the full `Q'` law, to which Lemma 2.2 applies
for every m. Restricting to the family's cofactors gives the same bound.) Expand `N_ℓ²` as a sum
over pairs of pairs. A pair contributes `Q'(n ≡ a (mod lcm(q,q')))` if
compatible and 0 otherwise. By Lemma 2.2 this is `≤ Γ(m)/m ≤ 3^{ω(m)}/m`
with `m = lcm(q,q')`. Each q carries `τ(A_q²) ≤ C_ε' ℓ^{ε/4}` divisors D,
since `A_q ≤ ℓ^{B+1}` (take `C_ε'` for exponent `ε/(4(B+1))`). The number
of pairs (q,q') with `lcm = m` is `τ(m²)`. So

    E N_ℓ² ≤ C_ε'² ℓ^{ε/2} Σ_{m ≤ ℓ^{2B}} 3^{ω(m)} τ(m²)/m
           ≤ C_ε'² ℓ^{ε/2} Π_{p ≤ ℓ^{2B}} (1 + 9/p + Σ_{e≥2} 3(2e+1)p^{−e})
           ≪ C_ε'² ℓ^{ε/2} (1 + 2B log ℓ)^{9} ≪_{ε,B} ℓ^{ε}.

Divide by `ℓ²`. ∎

**Corollary 2.5 (leak; PROVED).** There is `W₀(B)` such that `𝔏 ≤ 1/2`
whenever `W ≥ W₀(B)`, uniformly in η and in the family.

*Proof.* Lemma 2.1 and Markov: `E[p 1{p > δ}] ≤ E[p²]/δ`. So
`𝔏 ≤ Σ_{ℓ>W} ℓ^{1/2} · C(1/4,B) ℓ^{−7/4} ≪_B W^{−1/4}`. ∎

**Convention (review T6).** From here on, `W₀(B)` is chosen with the
constant of Lemma 4.0 (prime-power tops), which exceeds Lemma 2.4's by a
factor `(2+B)²`. Then Corollary 2.5 holds for every family considered in
§4 as well.

**Remark 2.5′ (other caps; PROVED).** Everything in §§2.3, 4 holds with
`δ_ℓ = min(1/4, ℓ^{−κ})` for any fixed `κ ∈ (0,1)`, with `W₀ = W₀(B,κ)` and
`K = K(W,B,κ)`:
* Cor 2.5: Markov with `δ = ℓ^{−κ}` gives `𝔏 ≪_{B,κ} Σ_{ℓ>W} ℓ^{κ−2+ε}`;
  take `ε < (1−κ)/2`;
* Lemma 2.2: `γ'(ℓ) = (1−δ_ℓ)^{−1} ≤ 4/3` still, since `δ ≤ 1/4`, so
  Lemma 2.4 is unchanged;
* Lemma 2.6: `h(ℓ) ≤ 2ℓ^{−κ}`; ET Cor 3.6's large-divisor range then needs
  `Σ_d h(d)d^{−1+κ/2} < ∞` (Euler factors `1 + O(p^{−1−κ/2})`), which holds.

Only `κ = 1/2` is used in the theorems; the remark covers the numerics of
§2.4.

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
| 10⁵ | 100 | 0 (δ = 1/4) | 5.67 | 100% | primes 31–255 |
| 10⁵ | 100 | 0.5 | 25.5 (saved: `capped_X1e5_W30_k0.5.txt`) | 100% | everywhere below 2¹⁷ |

Theorem-compatible caps `δ_p = min(1/4, p^{−0.2})` (all types, X = 10⁵,
100 samples; `data/twin/capped_X1e5_W*_k0.2_cap.txt`):

| W | expected leak | realised leak |
|---:|---:|---:|
| 30 | 5.67 | 100% |
| 100 | 0.64 | 46% |
| 300 | 0 | 0% (no heavy coordinate in any sample) |

So at X = 10⁵ the leak hypothesis `𝔏 ≤ 1/2` is *attainable* at toy scale
with W = 300 (caps allowed by Remark 2.5′), for the full system including
twin classes. This does not test whether W₀ must grow with X. B is
unbounded in these runs (all `M ≤ X`), whereas W₀ is proved only for fixed
B. At W = 300, X = 10⁵ every cofactor is `< 334`, so the system is sparse.

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
  By Lemma 3.2, the values produced by cofactors q with `(n|q) = 1` are
  non-residues mod ℓ. QR-compatibility of the W-smooth part alone does not
  give this: for `M = 31·37`, `D = 1`, the value `−4 mod 37` is a residue.
* **The κ = 0.2 runs are not theorem-compatible.** Theorem 2.3 needs
  `δ_p ≤ 1/4` (ET Prop 2.4), while `31^{−0.2} ≈ 0.50` and the X = 10⁵ run
  has mean light probability 0.386 at p = 31. They support the distortion
  idea, not the theorem's regime. The theorem-compatible runs
  (`δ_p = min(1/4, p^{−κ})`, Remark 2.5′) are in the second table above.

## 3. The extremal statement (E_δ) itself

Theorem 2.7 takes (E_δ) off the critical path. It is not settled here.
This section records what was found about it.

**Lemma 3.1 (u-form; PROVED).** For every integer n,

    F_ℓ(n) = { −(4u)^{−1} mod ℓ : u = sk², 4sk | qℓ+1, q | 4un+1, q ∈ 𝒬_ℓ }.

So the value depends only on u, and q is activated iff `q | 4un+1`.
Equivalently, for n coprime to `lcm 𝒬_ℓ` and `N ≡ −(4n)^{−1}` modulo
`lcm 𝒬_ℓ`: u is active iff
`u − N` has a divisor `q ∈ 𝒬_ℓ` with `q ≡ −ℓ^{−1} (mod 4sk)`.

(Every active q is coprime to n, since `q | 4un+1`; for general n, apply
the second form with `lcm 𝒬_ℓ` replaced by the lcm of the cofactors
coprime to n.)

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

### 4.1 What breaks, and the prime-power interface

Fix a window structure. Call a modulus M **window-resolved** if the last
window meeting its primes `> W` contains exactly one of them, to exponent
one. This is ET's (U). For EB's η-windows every η-gapped M is resolved
(EB Lemma 2.1). An η-twin M may be resolved too (its top two primes can
straddle a window boundary). An **unresolved** M has, in its last window,
either a prime power `ℓ^v` (`v ≥ 2`) or `r ≥ 2` distinct primes. With
`M ≤ P(M)^{1+B}` and window log-ratio `1+η`, `r ≤ (1+B)(1+η)`. Example
(review): `M = 101·103·109 ≡ 3 (mod 4)` has three primes in one η = 1/4
window above W = 30, and its class with D = 1 is a *ternary* event.

Inside the window an unresolved condition is an r-ary event on the window
residues, and ET Proposition 2.4 needs independent single-coordinate hit
indicators. The capped measure of §2 does not change this. Throughout this
section B is fixed, all ℛ(M)-classes considered have `M ≤ P(M)^{1+B}`, and
the QR base, the caps `δ_ℓ = ℓ^{−1/2}`, `W = W₀(B)` and the leak bookkeeping
are as in §2.

**Prime-power coordinates.** In the windows of §§4.2–4.3 the coordinate at
ℓ is the full residue `n mod ℓ^{E_ℓ}`. Given the earlier history h, the
conditions with top prime ℓ forbid a set `F̂_ℓ(h) ⊆ ℤ/ℓ^{E_ℓ}`, a union of
classes mod `ℓ^v`. Put `p_ℓ(h) = |F̂_ℓ(h)|/ℓ^{E_ℓ}`. A light coordinate is
uniform on the complement of `F̂_ℓ(h)` (full-fibre conditioning); a heavy
one is uniform. Lemma 2.1 and Lemma 2.2 hold verbatim for this transition
(a residue class mod `ℓ^e` has probability `≤ (1−δ_ℓ)^{−1}ℓ^{−e}`).

**Lemma 4.0 (second moment with prime powers; PROVED).** For every prime
`ℓ > W`, with windows processed in any order compatible with the
sequential construction,
`E_{Q'} p_ℓ(H)² ≤ C(ε,B) ℓ^{−2+ε}`, with `C(ε,B)` as in Lemma 2.4 up to a
factor `(2+B)²`.

*Proof.* Write each modulus with top prime ℓ as `M = qℓ^v`, `(q,ℓ) = 1`,
`1 ≤ v ≤ 1+B`. The class `−4D (mod M)` is active at h iff
`n ≡ −4D (mod q)`, a condition on the earlier history only, and then it
forbids one class mod `ℓ^v`, of density `ℓ^{−v}`. So
`p_ℓ(h) ≤ Σ_v ℓ^{−v} N_{ℓ,v}(h)`, with `N_{ℓ,v}` the number of active pairs
`(q,D)` with `qℓ^v ≤ ℓ^{1+B}`. The proof of Lemma 2.4 bounds
`E N_{ℓ,v}² ≪_{ε,B} ℓ^{ε}` (it uses only `q ≤ ℓ^B`, Lemma 2.2 for lcm's of
cofactors, and `τ(A²) ≤ ℓ^{o(1)}`; it never uses `P(q) ≤ y`). Minkowski:
`(E p_ℓ²)^{1/2} ≤ Σ_v ℓ^{−v}(E N_{ℓ,v}²)^{1/2}`. ∎

So Corollary 2.5 (leak `≪_B W^{−1/4}`) holds for the whole family, twin
and prime-power classes included, for the window orders used below.
Lemma 2.6 (first moment) sums over all M with `P(M)` in a range, so it
also covers them.

### 4.2 Low range: everything below `e^{λ^{1/4}}` is free

**Proposition 4.1 (PROVED).** Put `s₁ = λ^{1/4}` and assume `s₁ > log W`.
Process every prime `ℓ ∈ (W, e^{s₁}]` as its own window, with the
prime-power coordinate of §4.1. Every ℛ(M)-class with `P(M) ≤ e^{s₁}`
(any shape) is then decided at its top prime, and these windows cost at
most `(8/3)·K'(W,B)·(1+B)³·λ^{3/4}` in (2.1).

*Proof.* At the singleton window `{ℓ}` the history fixes every requirement
of a condition with top prime ℓ except the one on `n mod ℓ^{E_ℓ}`. The
induction step of Theorem 2.3 needs no Proposition 2.4 here: if ℓ is light
at h, `E f̃ = (1−p)f̃(hit-free) + p·f̃(hit) ≥ (1−p) f̃(hit-free)` with
`f̃ ≥ 0`, so `Φ = −log(1−p_ℓ(h)) ≤ (4/3)p_ℓ(h)`; if ℓ is heavy, nothing is
conditioned and the hit leaks. By Lemma 2.2, as in Lemma 2.6,
`Σ_{W<ℓ≤e^{s₁}} E_{Q'} p_ℓ ≤ Σ_{M ≤ e^{(1+B)s₁}} τ(A_M²)Γ(M)/M ≤
K'((1+B)s₁)³`. Multiply by 4/3 and by the factor 2 of (2.1). ∎

So in this range windows are not needed at all: the cost is the void
(≈ mass), which is what EB Theorem 2.5 pays there anyway (its "cubic
branch", `Σ_{s_j ≤ s*} X_j`).

### 4.3 Top range: linear windows are free

**Lemma 4.2 (linear window inequality; PROVED).** Let V be a finite set of
coordinates `y_ℓ` with finite state spaces and independent laws `U_ℓ`, and
let `f(y_V) = c₀ + Σ_{ℓ∈V} g_ℓ(y_ℓ) ≥ 0` with `E_{U_ℓ} g_ℓ = 0`. Let σ be
any probability law on the product whose one-coordinate marginals satisfy
`σ_ℓ ≤ (1+ε_ℓ)U_ℓ` and `Σ_y (U_ℓ − σ_ℓ)⁺(y) ≤ δ_ℓ`. Then

    E_U f ≥ E_σ f / (1 + max_ℓ(ε_ℓ + δ_ℓ)).

*Proof.* `E_U f = c₀`. Put `m_ℓ = −min g_ℓ ≥ 0`. Since f ≥ 0 at the point
where every `g_ℓ` is minimal, `Σ m_ℓ ≤ c₀`. With `r = dσ_ℓ/dU_ℓ`,
`E_σ g_ℓ = E_U[g_ℓ(r−1)] ≤ E_U[g_ℓ⁺(r−1)⁺] + E_U[g_ℓ⁻(1−r)⁺] ≤ ε_ℓ E_U g_ℓ⁺
+ m_ℓ δ_ℓ ≤ m_ℓ(ε_ℓ+δ_ℓ)`, using `E_U g⁺ = E_U g⁻ ≤ m_ℓ`. Sum over ℓ. ∎

(The review notes that applying `σ_ℓ ≤ (1+ε_ℓ)U_ℓ` to `g_ℓ + m_ℓ ≥ 0`
gives the same with `max ε_ℓ` alone.)

**Corollary 4.3 (PROVED).** Assume `λ/2 > log W`. Let
`V = {ℓ : λ/2 < log ℓ ≤ λ}` be one window, processed sequentially inside
itself (increasing ℓ, prime-power coordinates, caps). Every condition
with top prime in V is decided at its top prime, whatever its shape, and
the window costs at most `2 log(1 + 3e^{−λ/4})` in (2.1).

*Proof.* A term of ν has level ≤ λ, so it involves at most one prime of
V. Hence `f(y_V) = E_U[g_next | h, y_V]`, as a function of the residues
`y_ℓ = n mod ℓ^{E_ℓ}`, has the form of Lemma 4.2. Take σ = the in-window
sequential capped law. Each one-coordinate marginal is a mixture of laws
uniform on a set of density `≥ 1−δ_ℓ`, so `ε_ℓ ≤ 2δ_ℓ` and the TV defect is
`≤ δ_ℓ`, with `δ_ℓ = ℓ^{−1/2} ≤ e^{−λ/4}`. And `E_σ f` is the expectation of
`g_next` under the `Q'` transition. So the induction step holds with
`Φ = log(1 + 3e^{−λ/4})`, doubled by (2.1). Windows above `e^λ` are
invisible and cost 0 (ET Step 0), in any order. ∎

Lemma 4.2 is special to one window prime per term. For two or more, a
λ-level f can exploit unary avoidance (Selberg's Λ² with one prime per
factor has level 2 and saves `≍ log(1+μ)` when `μ = Σ p_ℓ` is large). So no
bound of the form `1 + O(max p)` can hold, and Proposition 2.4's
interpolation is needed.

### 4.4 What is proved, and the residual range

**Theorem 4.4 (PROVED).** Fix B and `W = W₀(B)` (convention after Cor 2.5), and let `λ ≥ (2 log W)^4`.
Let 𝔊 be any family of ℛ(M)-classes with `M ≤ P(M)^{1+B}`, plus any
W-smooth classes, such that every modulus M of 𝔊 with top prime in
`(e^{λ^{1/4}}, e^{λ/2}]` is window-resolved for EB's η-windows. (All
η-gapped moduli qualify.) Then every majorant of level λ satisfies
`log(1/Eν) ≪_B η^{−1}λ^{3/4}`.

*Proof.* Apply Theorem 2.3′ with these blocks: singletons on
`(W, e^{λ^{1/4}}]` (singleton step, Prop 4.1); EB's η-windows restricted to
`(e^{λ^{1/4}}, e^{λ/2}]`, where every condition is resolved, so (U) holds
(window step); one sequential block V on `(e^{λ/2}, e^λ]` (linear step,
Corollary 4.3); singletons above `e^λ` (constant f, Φ = 0). Order: increasing
primes. Every condition is decided at its top prime; so Lemma 2.1′ applies.
With Lemma 4.0 and Corollary 2.5 (W₀ as in the convention after it), it
gives `𝔏 ≤ 1/2`. The middle windows cost what they cost in Theorem 2.7. ∎

**The residual.** Moduli with top prime in `(e^{λ^{1/4}}, e^{λ/2}]` that are
unresolved: their last η-window contains a prime power or `2 ≤ r ≤
(1+B)(1+η)` of their primes. There a term of ν may involve
`2 ≤ d_j = ⌊λ/s_j⌋ < λ^{3/4}` primes of a window. By ET Lemma 3.8, η-twin
moduli carry `≫_η (log x)³` supply, so the residual is not negligible by
mass.

### 4.5 The missing window inequality

**Conjecture 4.5_r (r-ary window inequality; OPEN).** Let V be a window of
primes with costs `s_ℓ ∈ (s, (1+η)s]`, residues `y_ℓ` independent uniform,
unary forbidden sets with `p_ℓ ≤ 1/4`, and, for `2 ≤ k ≤ r`, k-ary
forbidden sets `F_T ⊆ Π_{ℓ∈T} ℤ/ℓ` (|T| = k) of density `π_T`. Let σ be the
in-window sequential capped law (primes in increasing order; at ℓ, uniform
off the unary set and off the classes activated by earlier residues). Light
and heavy are decided by the *total* activated density at ℓ (unary plus
activated k-ary), as in Lemma 2.1′; heavy coordinates are uniform, and the
bound `p_ℓ ≤ 1/4` refers to light ones.
Then for every λ-level `f ≥ 0` and every α > 0,

    log(E_σ f / E_U f) ≤ C_r[ αλ + Σ_ℓ p_ℓ e^{−α s_ℓ} + Σ_{2≤|T|≤r} π_T e^{−α Σ_{ℓ∈T} s_ℓ} ]
                         + O_r(log(2+λ/s) + log(2+μ)),

μ the total mass. (Prime-power alphabets, for `ℓ^v | M`, belong to the
same statement with `ℤ/ℓ^{E_ℓ}` coordinates.)

The case r = 2 is EB's route 3 (local boost) in the 2-prime case. With the
profiles bounded by Lemma 2.6, Conjecture 4.5_r for `r = ⌊(1+B)(1+η)⌋`
would remove the residual in Theorem 4.4 for that B. The k-ary term carries
`e^{−α·(k s)}`: a k-prime condition costs its full modulus, which is the
H_MS heuristic. Conjecture 4.5_2 alone does **not** suffice once
`(1+B)(1+η) ≥ 3` (review: `101·103·109`); projecting a ternary event to
two coordinates enlarges it.

**Routes tried here, and why they stall (HEURISTIC unless marked).** All
statements concern a window with `s > λ^{1/4}`.
1. *Splitting windows* (finer windows of log-ratio `1+η'`, or random
   sub-windows). A binary condition is resolved only if its primes fall in
   different sub-windows. If the supply of ET Lemma 3.8 scales like η'
   (not proved), the unresolved mass is `≍ η'λ³` in total, so
   `η' ≲ λ^{−3}` would be needed; with the window bound of ET Prop 2.4 each
   window pays `≥ αλ`, so this route cannot work with that bound. (This
   says nothing about better window bounds.)
2. *Over-conditioning* (forbid one end of every binary condition, making
   the system unary and independent). A binary condition has codimension
   2; forbidding one end gives it weight `1/ℓ₁` instead of `1/(ℓ₁ℓ₂)`.
   For a typical history the number of active binary conditions with a
   given lower prime is heuristically `≍ #(primes in V)·(log X)^{O(1)} ≫ ℓ₁`.
3. *Leak.* Under the unary-conditioned law the expected number of binary
   hits is the window's twin mass, unless unary conditioning suppresses
   them, which nothing indicates. If hits are roughly Poisson, the leak
   probability is `≈ 1 − e^{−mass}`, close to 1 when the mass is large.
4. *Void* (condition the product law on "no binary hit"). Under weak
   correlations this costs ≈ the twin mass ≈ `η s³` per window. That is
   fine for `s ≲ λ^{1/4}`, where Proposition 4.1 is the rigorous version,
   and too large above, where ET's window cost is `(λ/s)(1 + log(s⁴/λ))`.
5. *One prime per term* (Lemma 4.2; PROVED). This needs `d_j = 1`, i.e.
   `s > λ/2`, and it fails for `d ≥ 2`, as explained after Corollary 4.3.
   Proposition 2.4's proof (thinning, symmetrisation over each band,
   interpolation in the band counts) uses the independence of the window
   coordinates essentially. With k-ary conditions, the hit indicators at
   later primes depend on all earlier residues of the window.

## 5. What this says about the global question

Question (3): is 3/4 sharp for all nonnegative CRT majorants of forced
classes with moduli `≤ N^{O(1)}`?

**Proved here (internally).** For each fixed B, the cap
`S_λ ≪_B η^{−1}λ^{3/4}` holds for every family of ℛ(M)-classes with
`M ≤ P(M)^{1+B}`, plus all W₀(B)-smooth classes, in which every modulus
with top prime in `(e^{λ^{1/4}}, e^{λ/2}]` is window-resolved (Theorem
4.4). Under the hypotheses of ET Lemma 2.9 (family slice primes
`≤ N^{O(1)}`, and a final bound `N·Eν + Σ|a_i|` with `Σ|a_i| < N`) the
level may be taken `λ ≍ L = log N`, so these families cannot give an
exceptional-set exponent θ > 3/4. Since Lemma 2.9's λ depends on ν, the
family hypothesis of Theorem 4.4 must hold for every λ in
`[Λ₀, (A+1)L + S]` (review T7). This is automatic for the two families
named below, read with that λ-range: the gapped ones need no λ, and "top
prime `≤ e^{λ^{1/4}}` or `> e^{λ/2}`" is then required for all λ in the
range. The theorem includes:
* all dominant and all η-gapped balanced moduli (Theorem 2.7), with no
  hypothesis. EB's (E_δ), (★_δ), H_light and (NDE) are not needed;
* all moduli, twin and prime-power included, with top prime
  `≤ e^{λ^{1/4}}` or `> e^{λ/2}`.

**Not covered.**
1. Unresolved moduli (η-twin, prime-power top, or ≥ 3 primes in the last
   window) with top prime in `(e^{λ^{1/4}}, e^{λ/2}]`. These are reduced to
   Conjecture 4.5_r with `r ≤ (1+B)(1+η)`. By ET Lemma 3.8 they carry a
   positive proportion of the cubic supply, so this is the genuine open
   core.
2. Moduli with `log M / log P(M)` unbounded. Every proof here is for
   fixed B, with constants `W₀(B)`, `K(W₀(B),B)` that are not tracked;
   there is no summation over B. (Unweighted, the share of moduli with
   `P(M) < M^{1/(1+B)}` is `ρ(1+B)` by Dickman; the weighted share is not
   known.)
3. (a,D)-classes and Case-A classes: Lemma 1.1 is proved for ℛ(M) only.
   ET Cor 3.6 covers dominant (a,D)-families. The two results cover their
   families **separately**. A family mixing balanced ℛ(M)-classes with
   dominant (a,D)-classes is covered by neither: the avoider set of a union
   is the intersection, and caps do not add. Remark 1.4 (square base)
   removes the base obstruction for such mixtures. Lemma 2.4 and the gapped
   structure for (a,D)-moduli remain to be done.

**Verdict.** Not settled. The balanced door is reduced to a bounded-arity
window inequality (Conjecture 4.5_r) in the range
`(e^{λ^{1/4}}, e^{λ/2}]`, plus uniformity in B. Every mechanism examined
here (heavy histories, small-prime correlations, η-gapped balance) turned
out harmless once the measure was chosen correctly. No proof or
construction points towards (B).

## 6. Attack on Conjecture 4.5_r: reduction to a pure comparison inequality

Status of this section: Conjecture 4.5_r is **not proved**. It is reduced
to a sharper, arithmetic-free statement (Conjecture 6.4), together with a
weaker sufficient form for the exponent question (Proposition 6.5). All
steps of the reduction are proved; the evidence for 6.4 is toy-scale.

### 6.1 Soft unary conditions

**Lemma 6.1 (ET Prop 2.4 for soft unary conditions; PROVED).** Let the
coordinates `y_ℓ` (ℓ ∈ V) be independent with laws `U_ℓ`. Let
`x_ℓ ∈ {0,1}` be a function of `y_ℓ` and private independent randomness,
with `p_ℓ = P(x_ℓ = 1)`, `p_ℓ ≤ 1/4` when `s_ℓ ≤ λ`, and `p_ℓ < 1`. Let σ be
the law of y given `x = 0`. Then for every λ-level `f ≥ 0` (in y),
`E_U f ≥ e^{−Φ} E_σ f`, with Φ the right side of ET (2.3) for the `p_ℓ`.

In particular, every product law `σ^× = ⊗σ_ℓ` with
`dσ_ℓ/dU_ℓ ≤ (1−p_ℓ)^{−1}` is reached at cost Φ(p): take
`P(x_ℓ = 1 | y_ℓ) = 1 − (1−p_ℓ)dσ_ℓ/dU_ℓ`.

*Proof.* Given x, the `y_ℓ` are independent and the law of `y_ℓ` depends on
`x_ℓ` only. So `f̃(x) = E[f | x]` is λ-level in x, `f̃ ≥ 0`, and
`E_σ f = f̃(0)`. The x's are independent Bernoulli, so ET Prop 2.4 applies.
∎

**Lemma 6.2 (composition; PROVED).** If `E_U f ≥ e^{−Φ₁}E_{σ₁} f` and
`E_{σ₁} f ≥ e^{−Φ₂}E_σ f` for all λ-level `f ≥ 0`, then the step
inequality (S) holds for σ with `Φ₁ + Φ₂`. (Immediate.)

So a block with unary and k-ary conditions splits into two parts. The
unary part is handled by Lemma 6.1 (product law σ^×, light unary sets). The
k-ary part is a comparison between the product law σ^× and its conditioning
on k-ary avoidance.

### 6.2 Removing bad residues

For a residue a at ℓ ∈ V and a history, let the **incident weight**
`c_ℓ(a)` be the σ^×-probability that some activated k-ary class through
`(ℓ, a)` is completed by the other coordinates. Let
`m_{≥2}(ℓ) = Σ_a σ^×_ℓ(a) c_ℓ(a)`; this is at most the k-ary mass incident
to ℓ.

**Lemma 6.3 (Markov removal; PROVED).** For θ > 0, adding to the unary
forbidden set at ℓ the residues with `c_ℓ(a) > θ` raises `p_ℓ` by at most
`m_{≥2}(ℓ)/θ`. Afterwards every incident weight is ≤ θ. Summed over a
window, the unary profile grows by at most `r·μ_{≥2}/θ`, where `μ_{≥2}` is
the window's k-ary mass. By Lemma 2.6 this is again `O_{B,θ}(s_j³)` in
`Q'`-expectation.

*Proof.* Markov: `σ^×_ℓ{c_ℓ > θ} ≤ m_{≥2}(ℓ)/θ`. Each k-ary class is
incident to at most r primes. ∎

(The removed residues are typically the small-u values `−(4u)^{−1}`, which
lie on very many twin classes; cf. Lemma 3.1.)

### 6.3 The sharpened gap

**Conjecture 6.4 (k-ary comparison inequality; OPEN).** Let `ν = ⊗ν_ℓ` be
a product law on a block V with costs `s_ℓ ∈ (s, (1+η)s]`, and
`d = ⌊λ/s⌋`. Let `ℱ` be a family of hard k-ary constraints
(`2 ≤ k ≤ r`) on V with all incident weights `≤ θ ≤ θ₀(r)` and total
ν-mass `μ_{≥2}`. Let σ be the sequential law (increasing ℓ; at ℓ, `ν_ℓ`
conditioned off the residues activated by earlier coordinates, uniform if
that set has ν_ℓ-mass `> δ_ℓ`). Then for every λ-level `f ≥ 0`,

    E_σ f ≤ exp( C_r [ d·log(2 + μ_{≥2}) + 1 ] ) · E_ν f.

This statement contains no arithmetic and no unary sieve. It is a binary
(k-ary) analogue of ET Prop 2.4, in its weak "d·log(mass)" form.

**Proposition 6.5 (sufficiency; PROVED).** Assume Conjecture 6.4 for
`r = ⌊(1+B)(1+η)⌋`. Then for every fixed B, every family of ℛ(M)-classes
with `M ≤ P(M)^{1+B}` (twin, prime-power top and all other shapes
included) plus W₀-smooth classes has

    S_λ ≪_B η^{−1} λ^{3/4} log λ.

In particular no such family gives an exponent θ > 3/4.

*Proof.* Apply Theorem 2.3′ with the blocks of Theorem 4.4, but with every
condition admitted in the middle windows. Order the primes increasingly;
every condition is decided at its top prime. In a middle window take
`σ_j = σ` of Conjecture 6.4, over the product law `σ^×` given by
Lemma 6.1, after the Markov removal of Lemma 6.3 with θ = θ₀. Steps:
* unary part: Lemma 6.1, cost `Φ_j^{light}` with the enlarged profile;
* k-ary part: Conjecture 6.4, cost `C_r(d_j log(2+μ_{≥2,j}) + 1)`;
* compose by Lemma 6.2.

Taking `Q'`-expectations and using concavity of log together with
Lemma 2.6 (k-ary masses are part of the cubic window mass) gives
`E log(2+μ_{≥2,j}) ≤ log(2 + K s_j³)`. Hence the k-ary costs sum to
`≪ Σ_{s_j>λ^{1/4}} (λ/s_j) log λ ≪ η^{−1}λ^{3/4} log λ`. The unary costs are
as in Theorem 2.7, with `K` replaced by `K(1 + r/θ₀)`. The leak: σ_j is
sequential and capped, so Lemma 2.1′ applies. The second moment
(Lemma 4.0) uses only the caps and Lemma 2.2, which holds for σ_j:
each coordinate is uniform on a set of density `≥ 1−δ_ℓ` given the past. ∎

The extra `log λ` is the price of the weak form. Conjecture 4.5_r, the
H_MS form with `e^{−αΣs}` weights, would remove it.

### 6.4 Evidence and caveats (EVIDENCE, toy scale)

`scripts/twin_window_lp.py` solves the exact LP
`C*_d = max{E_σ f / E_U f : f ≥ 0 on all of (ℤ/L)^m, f a sum of d-juntas}`
for toy blocks: m coordinates of size L = 5, κ = 2 random forbidden points
per pair. As a comparison it solves the same LP for a unary block of
equal mass (data `data/twin/lp/`).

With σ = uniform on the avoid set (`log C*_d ≤` void, and `log C*_d ≥` the
block's own d-junta sieve saving):

| m | d | binary mass | binary void | binary `log C*` | unary mass | unary void | unary `log C*` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 2 | 0.80 | 0.825 | 0.602 (73%) | 1.0 | 1.116 | 0.916 (82%) |
| 5 | 3 | 0.80 | 0.825 | 0.747 (91%) | 1.0 | 1.116 | 1.044 (94%) |
| 5 | 4 | 0.80 | 0.825 | 0.825 (100%) | 1.0 | 1.116 | 1.115 (100%) |
| 6 | 2 | 1.20 | 1.234 | 0.770 (62%) | 1.2 | 1.339 | 0.916 (68%) |

Reading.
* At equal d, binary constraints yield a somewhat *smaller* fraction of
  their void than unary constraints of comparable mass. This points the
  same way as H_MS (a binary condition uses two of the d coordinates) and
  agrees with ET §5.8 and EB §3.2. It is weak evidence: the toys are dense
  (`p ≈ 1/5`), tiny (m ≤ 6), and far from the sparse regime of the theorem.
* **Caveat on the choice of σ.** With the *sequential* σ the same toys
  give `log C*` *above* the void: 0.693 vs 0.519 (m = 4, d = 2) and
  1.367 vs 0.825 (m = 5, d = 3) (`series_L5_k2_d*.txt`). In a dense block
  the sequential law has density up to `≈ (L/(L−κ'))^m` at some points,
  more than `1/U(avoid)`. In the theorem's regime every conditional
  density is capped by `(1−δ_ℓ)^{−1}` with `δ_ℓ ≤ ℓ^{−1/2}`, so this skew
  is negligible there. But it shows that Conjecture 6.4 is false without
  the caps and the sparsity θ, and that the choice of σ is part of the
  problem.

### 6.5 A remark on the Λ² route

ET Theorem 5.5 caps Selberg-type majorants `g²` on arbitrary systems, with
no windows, via `P(A∩A')/P(A)²`. Its proof works for any probability σ̃
on A in place of `U|A` (PROVED, same proof). Since `g ≥ 1` on A,
`E_U[g·dσ̃/dU] ≥ 1`. Cauchy–Schwarz and the noise operator then give

    saving(g²) ≤ αλ/2 + log E_S[ 1 + χ²(σ̃_S ‖ U_S) ],

with S the random set containing each coordinate independently with
probability `ρ_i = e^{−α s_i}` and `σ̃_S` the marginal on S. For σ̃ = U|A
this is ET's `Ξ_A`. The freedom in σ̃ addresses ET's observation that a
fibrewise bound "alone would not suffice": tilting σ̃ towards fibres with
small future profile turns the fibre average `E e^{+X}` into
`(E e^{−X})^{−1}`. No bound on the χ²-functional for the real system is
proved here. Twin conditions enter it only through marginals on S that
contain both of their primes, i.e. with weight `ρ_{ℓ₁}ρ_{ℓ₂}`.

### 6.6 The Λ² route: fibre tilting, and a reduction of H_MS^{Sel}

This follows tactic (i): the Λ² special case first. ET Theorem 5.5 needs no
windows, so twin and all other balanced moduli enter only as events. ET
listed three obstacles to H_MS^{Sel}:
* (S)+fibre: small primes, the fibre-variance term `Ξ^{fib}`, and the
  density of empty fibres;
* the correlation inequality;
* the lower bound for J.

The first is removed exactly by the next lemma.

**Lemma 6.6 (fibre tilting; PROVED).** In the setting of ET Theorem 5.5,
let F be a set of coordinates. Their residues c (the *fibre*) range over
`ℤ/Q_F`. For each fibre c let `A_c = A ∩ {fibre = c}` and
`Ξ_c(α) = log[P(A_c ∩ A'_c | c)/P(A_c | c)²]`, where in `A'_c` the
coordinates outside F are ρ-correlated (`ρ_i = e^{−α s_i}`) and the
fibre is shared. Then for every set R of fibres with `A_c ≠ ∅` for
`c ∈ R`, every `g ∈ V_{λ/2}` with `g ≥ 1` on A satisfies

    saving(g²) ≤ αλ/2 + log(Q_F/|R|) + avg_{c∈R} Ξ_c(α).

The coordinates in F may be charged primes.

*Proof.* Let `σ̃ = Σ_{c∈R} π_c U(·| c, A)` with weights π to be chosen, and
`h = dσ̃/dU`. Since `g ≥ 1` on `A ⊇ supp σ̃`, `E_U[gh] ≥ 1`, so
`E g² ≥ 1/‖Π_{V_{λ/2}}h‖²`. As in ET, `‖Π_V h‖² ≤ e^{αλ/2}⟨h, T_ρ h⟩`
whenever `ρ_i ≥ e^{−αs_i}`. `⟨h,T_ρh⟩ = Σ_T(Π_{i∈T}ρ_i)‖ĥ_T‖²` is
nondecreasing in every `ρ_i`, so we may put `ρ_i = 1` on F. Then the copy
shares the fibre, and

    ⟨h, T_ρ h⟩ = Σ_c Q_F^{−1} (π_c Q_F / P(A_c|c))² P(A_c∩A'_c | c) = Q_F Σ_{c∈R} π_c² e^{Ξ_c}.

The minimum over probability vectors π on R is at `π_c ∝ e^{−Ξ_c}`, with
value `Q_F / Σ_{c∈R} e^{−Ξ_c} = (Q_F/|R|)/avg_R e^{−Ξ_c}`, which is
`≤ (Q_F/|R|) e^{avg_R Ξ_c}` by Jensen. ∎

ET's warning example `A = {c = c₀} × Ω_large` is consistent with the lemma:
`Ξ_c = 0` there, but `log(Q_F/|R|) = log Q_F`. With the uniform σ̃ = U|A
the fibre average would be `log avg_c e^{Ξ_c}·(…)`, i.e. maximum-like.
Tilting makes it an average.

**Reduction 6.7 (SKETCH; not proved).** Take F = all primes `≤ w := λ^C`
(any exponents) and let R be the fibres that avoid every w-smooth class.
Then H_MS^{Sel} (`saving(g²) ≪ λ^{3/4}(log λ)^{O(1)}` for *all* ℛ(M), any
B, twins included) would follow from three steps.
1. *Empty-fibre density:* `log(Q_F/|R|) ≤ (log λ)^{O(1)}`. Sketch: QR base
   at the primes `≤ W₁ = (log λ)^{C'}` (Lemma 1.3; cost `π(W₁) log 2`).
   Then the asymmetric local lemma (as in POINTWISE_OMEGA2 Thm 3.1,
   step 2, with `x_E = 2P(E)`) for the w-smooth classes having a prime in
   `(W₁, w]`, whose incident masses are `≤ (log λ)^{O(1)}/p ≤ 1/(8 log λ)`.
   The w-smooth mass with QR weights is `(log w)^{O(1)}`.
2. *Good fibres:* restrict R to the fibres in which every coordinate
   `ℓ > w` has incident event mass `≤ θ`. The bad fibres are `o(|R|)`, by
   Markov on second moments of the incident masses (Lemma 2.4/4.0 type:
   `E p_ℓ² ≪ ℓ^{−2+ε}`), with the conditional local lemma bounding the
   inflation of the uniform law on R. Summed over `ℓ > w` this is
   `≪ θ^{−2}w^{−1+ε}`. Residues of high incidence are quarantined first
   (Lemma 6.3 = POINTWISE_OMEGA2 Lemma 2.2).
3. *Sparse noise stability (the core):* in a good fibre all coordinates
   are independent and every incident mass is ≤ θ. A Kotecký–Preiss cluster
   expansion of `log P(A_c)` and `log P(A_c∩A'_c)` (polymers: event sets
   connected through shared primes) should give `Ξ_c` as the sum of the
   *mixed* clusters. The leading one is the diagonal pair (E, E′):

       Σ_E [P(E∩E′) − P(E)²] ≤ Σ_E P(E) Π_{ℓ∈S(E)}(ρ_ℓ + 1/ℓ) ≤ (1+o(1)) Σ_C P(C|c) M_C^{>w,−α}.

   Here `ℓ > w` makes `Π(1+ℓ^{α−1}) = 1+o(1)`. Its fibre average is
   `≪ α^{−3}` by ET Lemma 3.1 for **all** ℛ(M), with no B restriction.

Conjecture 6.8 below is step 3 alone. Steps 1–2 are routine but not
written.

**Conjecture 6.8 (sparse noise stability; OPEN).** Let `X_i` be
independent, and 𝓔 a finite family of events, each depending on the
coordinates `S(E)`. Assume every coordinate has incident weight
`Σ_{E∋i} P(E) e^{a|S(E)|} ≤ θ ≤ θ₀(a)`, plus a codegree condition of
POINTWISE_OMEGA2 §10.2 type for events with `|S(E)| ≥ 3`. Let A be "no
event", and A′ the ρ-correlated copy. Then

    log [P(A∩A′)/P(A)²] ≤ (1 + O(θ)) Σ_E P(E)(Π_{i∈S(E)}(ρ_i + (1−ρ_i)P_i(E)) − P(E)),

where `P_i(E)` is the marginal factor at i (for congruence events,
`1/ℓ^{e}`).

For **graph-type** systems (`|S(E)| ≤ 2`), POINTWISE_OMEGA2 Lemma 2.1 (the
pseudoforest bound under a vertex-degree hypothesis) is exactly the
tree-counting estimate that the Kotecký–Preiss convergence criterion needs.
So the binary case of 6.8 looks within reach of standard polymer
technology. The k-ary case meets POINTWISE_OMEGA2's codegree-hub
obstruction (§10.4, Prop 11.4: the `−4D` families). Codegree hubs are
sets of two or more vertices lying in many events. They are not removed by
vertex quarantine.

**What a proof of 6.8 would give.** For r = 2 (all events on at most two
large primes per fibre, e.g. twin moduli `kℓ₁ℓ₂` with k w-smooth, plus
dominant moduli), the Λ² cap `λ^{3/4}(log λ)^{O(1)}`. This is a proved
H_MS^{Sel} for that family, twins included, with no windows and no B. The
ES family also has moduli with three or more large primes, so the full
H_MS^{Sel} needs the k-ary case.

**Tactic (ii), direct binary Prop 2.4 by symmetrising over the residue
alphabets: assessment only, not attempted in detail.** The uniform law on
`ℤ/ℓ` is invariant under permuting residues, but the forbidden sets are
not. Averaging the window inequality over residue permutations therefore
replaces the given binary structure by a random one (the "annealed"
system). That bounds an average over structures, not the given one. For
general (non-Λ²) majorants this route needs a further transference, which
was not found. The Λ² route avoids it because there everything is an L²
quantity.

### 6.7 Conjecture 6.8 for events on at most two primes: convergence proved, comparison step open

**Tool (Kotecký–Preiss, Comm. Math. Phys. 103 (1986) 491–498, Thm 1;
version used).** Let polymers γ carry weights `w(γ) ∈ ℝ`, with a symmetric
reflexive incompatibility relation `≁`, and let
`Z = Σ_{pairwise compatible families} Π w(γ)`. Suppose there are
`a, d : polymers → [0,∞)` with

    Σ_{γ′ ≁ γ} |w(γ′)| e^{a(γ′)+d(γ′)} ≤ a(γ)     for every γ.

Then `log Z = Σ_X φ(X) w^X`, summed over clusters X, converges absolutely,
and `Σ_{X ≁ γ} |φ(X) w^X| e^{d(X)} ≤ a(γ)` for every γ.

**Tool (Penrose tree-graph inequality, 1967).** If `f_e ∈ [−1, 0]` for
every edge of the complete graph on V, then
`|Σ_{G connected spanning V} Π_{e∈G} f_e| ≤ Σ_{T spanning tree} Π_{e∈T} |f_e|`.

**Setting.** We work in one good fibre, with unary constraints absorbed
into the product base `ν = ⊗ν_ℓ` (ν_ℓ uniform off the unary set). The
binary constraints are points `(ℓ,a; ℓ′,b)`. Put
`f_{ℓℓ′}(y) = −1[(y_ℓ, y_ℓ′)` is a forbidden point`] ∈ {−1, 0}`. In the
vertex language of POINTWISE_OMEGA2 §2, a vertex is a residue `a` at ℓ,
`p(a) = ν_ℓ(a)`, `deg(a) = Σ_{points (ℓ,a;ℓ′,b)} ν_ℓ′(b)` (the incident
weight), and `w_ℓ = Σ_a p(a) deg(a)`. Then
`Z₁ := P_ν(no binary point) = E_ν Π_{ℓ<ℓ′}(1 + f_{ℓℓ′})`.

**Lemma 6.9 (convergence; PROVED).** Use the Mayer expansion: polymers are
prime sets V with `|V| ≥ 2`, `w(V) = E_ν Σ_{G connected spanning V} Π_{e∈G}
f_e`, and V ≁ V′ iff `V ∩ V′ ≠ ∅`. Then `Z₁ = Σ_{disjoint families} Π w(V)`.
If `deg(a) ≤ δ ≤ e^{−6}/2` for every vertex, the Kotecký–Preiss condition
holds with `a(V) = d(V) = |V|`. The same holds for the doubled system: the
ρ-coupled pair `(y, y′)` at each prime, with
`f^{(2)}_e = (1+f_e(y))(1+f_e(y′)) − 1 ∈ {−1,0}`, base conditioned on unary
avoidance in both copies. There the requirement is `δ ≤ e^{−6}/8`.

*Proof.* Expanding `Π(1+f_e)` over graphs and grouping by connected
components gives the polymer representation. By independence of distinct
primes, the expectation factors over components. By Penrose (pointwise in
y, as `f_e(y) ∈ {−1,0}`), `|w(V)| ≤ Σ_{T tree on V} P_ν(every edge of T is
hit)`. A hit prime-level tree fixes one residue per prime, so it is
dominated by a vertex-level tree at distinct primes. POINTWISE_OMEGA2
Lemma 2.1's tree count (rooted at a vertex at ℓ) gives
`Σ_{V∋ℓ, |V|=v} |w(V)| ≤ w_ℓ e^v δ^{v−2} ≤ e^v δ^{v−1}`. Hence

    Σ_{V′≁V} |w(V′)| e^{2|V′|} ≤ |V| · Σ_{v≥2} e^{3v} δ^{v−1} ≤ |V| · 2e⁶δ ≤ |V|.

Doubled system: a doubled edge is hit iff it is hit in copy 1 or copy 2.
The vertex degree of `(a, a′)` is at most
`(deg(a) + deg(a′))·(16/9)² ≤ 4δ`, using the base marginals
`≤ (1−p)^{−1}ν`, `p ≤ 1/4`. Repeat with 4δ. ∎

So in a good fibre, `log Z₁` and `log Z₂` (doubled) are absolutely
convergent cluster sums, with every prime's cluster mass ≤ |V| = O(1).
This also gives the lower bound `log Z₁ ≥ −Σ_ℓ(cluster mass through ℓ)`
without any correlation inequality. That is ET's missing ingredient 1, in
the binary sparse regime.

**The remaining step (precise failure point; OPEN).** Conjecture 6.8 for
two-prime events needs

    Ξ_bin := log Z₂(ρ) − log Z₂(0) ≤ (1 + O(δ)) Σ_e [P(e hit in both copies) − P(e)²] + O(δ)·(same),     (6.1)

with `log Z₂(0) = 2 log Z₁` (independent copies). The natural proof is
`Ξ_bin = ∫₀¹ Σ_ℓ ρ_ℓ ∂_{ρ_ℓ} log Z₂(tρ) dt`, with
`∂_{ρ_ℓ} log Z₂ = Σ_{X∋ℓ} φ(X) ∂_{ρ_ℓ} w^X`. Here `∂_{ρ_ℓ}` replaces the
base law at ℓ by (diagonal − product). This signed measure inflates the
weight of *mixed* polymers (those using ℓ in both copies at the same
residue) by a factor up to ≈ ℓ relative to their ρ = 0 value. So KP's
bound `Σ|φ w^X| ≤ a` does not control the derivative directly. What is
needed is a **weighted** Kotecký–Preiss estimate, with `d(X)` carrying a
factor `e^{(number of mixed coordinates)·log(ρ_ℓ ℓ)}`. One then has to show
that a mixed cluster costs its diagonal weight `Π_{i∈mixed}(ρ_i + 1/ℓ_i)`
times `O(δ)` per extra prime. This is a standard-looking but unproved
perturbation lemma. It is the precise point at which the two-prime Λ²
theorem stops. Steps 1–2 of Reduction 6.7 (empty-fibre density, good
fibres) were not written out in this session.

**Status of the two-prime Λ² theorem:** not proved. Reduced to the
weighted-KP derivative bound (6.1). Convergence (Lemma 6.9) is proved, and
so is the fibre tilting (Lemma 6.6).

### 6.8 The perturbation step: gluing identity, corrected target, remaining lemma

**Correction to (6.1).** The bound (6.1) with only the single-edge
diagonal is too strong. Lower-support terms of the form `ρ̃_j·Var` appear
already for one shared prime (Lemma 6.11). The correct target is (6.2)
below. All objects are in one good fibre as in §6.7. The base `ν = ⊗ν_ℓ` is
uniform off the unary sets.

**Unary part (exact; PROVED).** Conditioning the ρ-coupled pair at ℓ on
"both copies avoid the unary set of density p" gives
`μ̃_ℓ = ρ̃_ℓ·Diag_ν + (1−ρ̃_ℓ)·(ν⊗ν)`, with `ρ̃_ℓ = ρ_ℓ/(1−p_ℓ+ρ_ℓ p_ℓ) ≤ (4/3)ρ_ℓ`
for `p ≤ 1/4`. Hence

    P(A∩A′)/P(A)² = Π_ℓ (1 + ρ_ℓ p_ℓ/(1−p_ℓ)) · Z₂/Z₁²,

where `Z₁ = P_ν(no binary point)` and `Z₂` is the binary avoidance
probability under `⊗μ̃_ℓ`. The first factor is ET Cor 5.6's unary term, so
`log` of it is `≤ (4/3)Σ_ℓ ρ_ℓ p_ℓ`. *Proof:*
`P(both avoid) = (1−p)² + ρp(1−p)`; the conditioned law puts mass
`ρ(1−p)/((1−p)²+ρp(1−p))` on the diagonal, and the diagonal and product
parts are each uniform on the allowed set. ∎

**Lemma 6.10 (gluing identity; PROVED).** Let S be a random set of primes,
containing each ℓ independently with probability `ρ̃_ℓ`, and let
`r(y_S) = P_ν(no binary point | y_S)/Z₁`. Then

    Z₂/Z₁² = E_S[ E_{ν_S}[ r(y_S)² ] ] = E_S[ 1 + E_{ν_S}(r(y_S) − 1)² ].

*Proof.* Expand `⊗μ̃_ℓ` as the mixture over S: coordinates in S are glued
(`y_ℓ = y′_ℓ ~ ν_ℓ`), the others are independent copies. Given the glued
values `y_S`, the two copies are independent, each with avoidance
probability `Z₁ r(y_S)`. Finally `E_{ν_S} r = 1`. ∎

So `log(Z₂/Z₁²) ≤ E_S E_{ν_S}(r−1)²`, by `log(1+x) ≤ x` and Jensen.

**Lemma 6.11 (one shared prime; PROVED).** For `S = {j}`,
`E(r−1)² = Var_ν(r_j)` with `r_j(a) = P(no binary point | y_j = a)/Z₁`.
If the system consists of the edges at j only (a star), then
`r_j(a) = Π_{ℓ′}(1 − κ_{a,ℓ′}/ℓ′)/E_ν Π(…)`, where `κ_{a,ℓ′}` is the
number of forbidden points `(j,a; ℓ′, ·)`. So
`Var(r_j) = Var_ν(deg_j)(1+O(δ))`, with `deg_j(a) = Σ_{ℓ′} κ_{a,ℓ′}/ℓ′`.

*Proof.* Direct computation; in a star the partners are independent given
`y_j`. ∎

In particular, a single shared prime contributes
`ρ̃_j Var_ν(deg_j)`. This is *not* of the single-edge form `ρ̃_jρ̃_ℓ′ π_e`:
it involves cross terms between different partners ℓ′, ℓ″ of the same
residue a. These are ET Assessment 5.8's "off-diagonal (O)" terms. After
the Markov quarantine (Lemma 6.3, `deg ≤ δ`) they satisfy
`Var(deg_j) ≤ q_j := Σ_a ν_j(a) deg_j(a)²`.

**Target (6.2) (OPEN).** In a good fibre with `deg ≤ δ ≤ δ₀`,

    E_S E_{ν_S}(r − 1)² ≤ C [ Σ_{e=(ℓ,ℓ′)} ρ̃_ℓ ρ̃_{ℓ′} π_e + Σ_j ρ̃_j q_j ].        (6.2)

**What (6.2) would give (PROVED reduction).** Both terms are summable as
needed:
* the diagonal `Σ_e ρ̃ρ̃′π_e`: its fibre average is `≤ (16/9)Σ_C P(C)
  M_C^{>w, −α}`, which is `≪ α^{−3}` for all ℛ(M) by ET Lemma 3.1;
* `Σ_j ρ̃_j q_j ≤ Σ_{j>w} q_j`: the fibre average of `q_j` is a
  pair-of-conditions count at j of second-moment type (as in Lemma 2.4), of
  size `≪ j^{−2+ε}`. So it sums to `≪ w^{−1+ε}`. Good fibres can be required
  to have `Σ_j q_j ≤ 1` at Markov cost `o(1)` in `log(Q_F/|R|)`.

Then Lemma 6.6 gives `saving(g²) ≤ αλ/2 + C α^{−3} + log(Q_F/|R|) + O(1)`,
i.e. the two-prime Λ² cap `≪ λ^{3/4}` (plus the empty-fibre term of
Reduction 6.7 step 1).

**Where the proof of (6.2) stands.** Write `r = dσ_S/dν_S` with
`σ = ν|A`. (6.2) follows from an approximate factorisation:

    r(y_S) = 1[no binary point inside S] · Π_{j∈S} r_j(y_j) · exp(Σ_{j≠j′∈S} η_{jj′}(y_S)) / N_S,     (6.3)

with pair corrections satisfying `|η_{jj′}| ≤ C(π_{jj′}-type path weights)`
and `Σ_{j′} sup|η_{jj′}| ≤ Cδ`. Given (6.3), one would argue in three steps:
* `E(r−1)²` splits into the product part (`Σ_j Var r_j ≤ C Σ_{j∈S} q_j`);
* the inside-S hits contribute `P(hit inside S) ≤ Σ_{e⊂S} π_e`;
* the pair corrections are handled by an exponential-moment bound over S.
  That bound is a graph-type sum with vertex weights `ρ̃_j`, edge weights
  `Cπ`, row sums `≤ Cδ`, i.e. POINTWISE_OMEGA2 Lemma 2.1 again.

The natural proof of (6.3) is the Kotecký–Preiss expansion of §6.7 for the
pinned system. Clusters touching one pinned prime give `r_j`, and clusters
touching two give `η`, with the pinned-cluster bound
`Σ_{X∋γ}|φ w^X| ≤ |w(γ)|e^{a(γ)}` (Kotecký–Preiss; Friedli–Velenik,
*Statistical Mechanics of Lattice Systems*, Thm 5.4). Two points remain
unproved:
1. a pinned site j makes every edge at j a *unary* constraint at its
   partner, so the pinned system's base changes with `y_j`. The cluster
   weights must be compared across different pinnings with relative error
   `O(δ)·deg_j(y_j)`, uniformly;
2. the normalisation `N_S` must be shown to be `exp(O(Σ_{j∈S} q_j +
   Σ_{e⊂S}π_e))`.

An alternative is to expand the coupling instead of gluing. Then
`μ̃_j = (ν⊗ν)(1 + g_j)` with `g_j = ρ̃_j(1[y=y′]/ν(y) − 1)`, which is
*doubly centred* (`E_{y′} g_j = E_y g_j = 0`). That kills every cluster
term in which only one copy touches j. But `g_j` is not repulsive
(it reaches `≈ ρ̃_j ℓ` on the diagonal), so Penrose's inequality does not
apply to it, and a mixed tree-graph bound would be needed.

**Status.** The two-prime Λ² theorem is reduced to the factorisation
(6.3), equivalently (6.2). Proved so far: Lemma 6.6 (fibre tilting),
Lemma 6.9 (convergence), Lemma 6.10 (gluing identity), Lemma 6.11 and the
summability of both terms of (6.2). Reduction 6.7 steps 1–2 were not
written in this session.

## Replay

```
# Lemma 1.1: Jacobi symbol of every Case-B class, M <= 20000 (~1 min)
PYTHONPATH=scripts uv run --with sympy python scripts/twin_jacobi_check.py 20000
# Remark 1.4: (a,D) and Case-A classes contain no square mod their modulus (~3 min)
uv run --with sympy python scripts/twin_square_base_check.py 40 300 3000
# §6.4: exact toy window LPs (each < 20 min, < 4 GB; m=6,7 at d=3 did not finish in 50 min)
for d in 2 3; do for m in 4 5; do uv run --with scipy --with numpy python scripts/twin_window_lp.py $m 5 $d 2 1; done; done   # sequential sigma
for d in 2 3 4; do uv run --with scipy --with numpy python scripts/twin_window_lp.py 5 5 $d 2 1 uniform; done
uv run --with scipy --with numpy python scripts/twin_window_lp.py 6 5 2 2 1 uniform
# §2.4: capped measure Q' with QR base, real system (X=1e5: ~3 min per run; X=1e6, 20 samples: ~40 min, < 4 GB)
cd scripts
uv run python twin_capped.py 100000 100 30 0.2 > ../data/twin/capped_X1e5_W30_k0.2.txt
uv run python twin_capped.py 100000 100 30 0   > ../data/twin/capped_X1e5_W30_k0.txt
uv run python twin_capped.py 100000 100 30 0 dom,gapM,gapB > ../data/twin/capped_X1e5_W30_k0_gapped.txt
uv run python twin_capped.py 100000 100 30 0.5 > ../data/twin/capped_X1e5_W30_k0.5.txt
uv run python twin_capped.py 1000000 20 30 0.2 > ../data/twin/capped_X1e6_W30_k0.2.txt
for W in 30 100 300; do uv run python twin_capped.py 100000 100 $W 0.2 all cap > ../data/twin/capped_X1e5_W${W}_k0.2_cap.txt; done
```
