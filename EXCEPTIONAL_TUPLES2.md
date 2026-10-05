# EXCEPTIONAL_TUPLES2 — TC_θ above 3/4 (task O24, branch `side-agent/tc-theta`)

Status: **in progress (O24).** Labels follow `DISCOVERIES.md`. PROVED means
proved in this file (internal, unrefereed). ES is not solved. No θ > 3/4 is
claimed unconditionally.

Notation: `T1` = `EXCEPTIONAL_TUPLES.md` (Defs §1, Thm 2.1, Cor 2.2–2.3,
Prop 2.4, Prop 4.2). Prime family `𝒫_y`, classes `𝓡(ℓ)`, `p_ℓ = F(ℓ)/ℓ`,
`μ_y = Σ p_ℓ`, hit count `f_y`, order-j sums `S_j(N)`, CRT values
`e_j = e_j(p)`, TC(N; K, y, η) and TC_θ exactly as in T1 §2.

## 0. Plan / working notes

1. **Form grouping.** A hit `n ∈ −4D (mod ℓ)` corresponds to a unique
   triple (r, s, m), `gcd(r,s)=1`, `rsm = A_ℓ`, `D = r²m`, and
   `n ≡ −4D ⟺ ℓ | ns + r`. Hits with the same *form* (r,s) all divide the
   single integer `ns + r ≤ Ns + r`. This is a rigorous size constraint
   that the CRT law ignores (§1).
2. **Truncation deficit.** The CRT mass `e_j` includes tuples with a
   same-form group of product `> Ns + r`; their interval count is exactly 0.
   Compute that mass and compare with the TC precision `η_K` (§2).
3. Consequence for TC_θ (literal) vs a corrected, truncation-aware TC, and
   whether the corrected version still gives Cor 2.3 (§3).
4. Numerics: explain the T1 §5(b) moment deficits (§4).

## 1. Forms: a rigorous size constraint invisible to CRT

**Lemma 1.1 (form parametrisation; PROVED).** Let ℓ ≡ 3 (mod 4) be prime,
`A = (ℓ+1)/4`. The map `(r,s,m) ↦ D = r²m` is a bijection from triples of
positive integers with `rsm = A`, `gcd(r,s) = 1` onto the divisors of A².
For such a triple and every n ∈ ℤ,

    n ≡ −4D (mod ℓ)  ⟺  ℓ | ns + r.                                     (1.1)

In particular `(r,s,m) = (1,1,A)` (D = A) gives the class `−1 mod ℓ`,
which lies in `𝓡(ℓ)` for **every** ℓ ≡ 3 (mod 4).

*Proof.* Given D | A², write `D/A = r/s` in lowest terms. Then `s | A`;
put `A = s a'`, so `D = r a'`, and `D | A² = s²a'²` gives `r | s²a'`, hence
`r | a'` (as `gcd(r,s) = 1`). So `a' = rm`, `A = rsm`, `D = r²m`. The
inverse direction is clear (`r²m | r²s²m²`). For (1.1): `4rsm = ℓ+1 ≡ 1`,
so `4r²m ≡ r/s (mod ℓ)` (s | A < ℓ is invertible), and `n ≡ −r/s` iff
`ℓ | ns + r`. ∎

Call `φ = (r,s)` the **form** of the class. The primes having a class of
form φ are exactly the ℓ ≤ y with `ℓ ≡ −1 (mod 4rs)` (then `m = A/(rs)`).
Distinct D may give the same residue mod ℓ; fix once and for all one
representative D (hence one form) per residue of `𝓡(ℓ)`, taking `D = A`
(form (1,1)) for the residue −1.

**Corollary 1.2 (forced zeros; PROVED).** Let T be a set of pairs
`(ℓ, b)` (distinct ℓ ∈ 𝒫_y, `b ∈ 𝓡(ℓ)`), and for a form φ = (r,s) let
`T_φ` be the pairs of T whose representative has form φ. If for some φ

    Π_{(ℓ,b)∈T_φ} ℓ > Ns + r,                                           (1.2)

then `C_T(N) = 0`, although `δ_T = Π_{T} ℓ^{−1} > 0`.

*Proof.* For n ∈ [1,N] in all classes of T, (1.1) gives
`Π_{T_φ} ℓ | ns + r`, and `1 ≤ ns + r ≤ Ns + r`. ∎

Call T **admissible** if (1.2) fails for every φ; let `𝔄` be the set of
admissible tuples, `e_j^𝔄 = Σ_{|T|=j, T∈𝔄} δ_T`, and
`Z_j := e_j − e_j^𝔄` (the CRT mass of forced-zero j-tuples). Then exactly

    S_j(N) = Σ_{|T|=j, T∈𝔄} C_T(N),   S_j(N) − N e_j = Σ_{T∈𝔄,|T|=j}(C_T − Nδ_T) − N Z_j.   (1.3)

*Remark.* T1's shift form (Lemma 1.3) groups hits by D; the class −1
has `D = A_ℓ`, a different shift `4A_ℓ = ℓ+1` for each ℓ, so the common
integer `n + 1` is invisible there. The form grouping is the natural one:
all hits of form φ divide the one integer `ns + r`. This is the Kubilius
situation (hits = divisors of one integer) *inside* each form.

## 2. The forced-zero mass beats the TC precision for every θ > 2/3

Let `𝒬 = 𝒬_y = {ℓ prime : y/2 < ℓ ≤ y, ℓ ≡ 3 (mod 4)}`,
`σ_y = Σ_{ℓ∈𝒬} 1/ℓ`, and `u₀ = u₀(N,y) = ⌈log(N+2)/log(y/2)⌉`.
By the prime number theorem for progressions mod 4,
`σ_y = (log 2 + o(1))/(2 log y)`; we only use `σ_y ≥ c₂/log y` (y ≥ y₀).

**Theorem 2.1 (PROVED).** For all N ≥ 1, y ≥ 4 with `u₀ ≤ σ_y y/4`,
and every m ≥ 0,

    Z_{u₀+m} ≥ e_{u₀}(q) · e_m(p⁻) ≥ ((σ_y/2)^{u₀}/u₀!) · e_m(p⁻),

where `q = (1/ℓ)_{ℓ∈𝒬}` and `p⁻ = (p_ℓ)_{ℓ ≤ y/2}`. In particular
`Z_{u₀} ≥ (σ_y/2)^{u₀}/u₀!`.

*Proof.* For U ⊆ 𝒬 with |U| = u₀ and V an m-set of pairs (ℓ, b),
distinct primes `ℓ ≤ y/2`, `b ∈ 𝓡(ℓ)`, put
`T = {(ℓ, −1 mod ℓ) : ℓ ∈ U} ∪ V`. Its form-(1,1) part contains U, and
`Π_U ℓ > (y/2)^{u₀} ≥ N + 2 > N·1 + 1`, so T is forced zero
(Cor 1.2). The map (U, V) ↦ T is injective (U = the primes of T in
(y/2, y]). `δ_T = Π_U ℓ^{−1}·Π_V ℓ^{−1}` and `Σ_V Π_V ℓ^{−1} = e_m(p⁻)`.
Summing gives the first inequality. For the second, ordering the u₀
elements, `u₀!·e_{u₀}(q) ≥ Π_{i<u₀}(σ_y − i·max q) ≥ (σ_y − u₀·2/y)^{u₀}
≥ (σ_y/2)^{u₀}`. ∎

**Theorem 2.2 (TC_θ meets the forced zeros; PROVED).** Fix θ ∈ (2/3, 1).
For N ≥ N₀(θ), with `K = K_N = 2⌈(log N)^θ⌉`, `y = y_K`, `η = η_K` (T1
Cor 2.2–2.3), we have `u₀ ≤ K` and

    Z_{u₀} ≥ η_K · exp(K/(2e²)).                                      (2.1)

*Proof.* By T1 (1.3) and the definition of `y_K`, `log y_K ≍ K^{1/2}`
(T1 Cor 2.2), so `u₀ ≤ 1 + log(N+2)/log(y_K/2) ≤ C₁ log N/K^{1/2}`, which
is `o(K)` and `≤ σ_y y/4` for large N. By Theorem 2.1 and `u₀! ≤ u₀^{u₀}`,

    log Z_{u₀} ≥ −u₀ log(2u₀ log y_K / c₂) ≥ −C₁ (log N/K^{1/2}) log(C₃ log N) =: −Λ_N,

using `u₀ log y_K ≤ 3 log N` for large N. Also
`log(1/η_K) = K/e² + log K`. Since `K ≍ (log N)^θ`,
`Λ_N ≍ (log N)^{1−θ/2} log log N`, and `1 − θ/2 < θ` for θ > 2/3, we get
`Λ_N + log K ≤ K/(2e²)` for N large, i.e. (2.1). ∎

(With `m` at the peak of `e_m(p⁻)` one gains a further factor
`≈ e^{μ_{y/2}}/μ`; the threshold θ = 2/3 does not move.)

**Corollary 2.3 (literal TC_θ forces a CRT excess; PROVED).** Let
θ ∈ (2/3, 1), N ≥ N₀(θ), and suppose TC(N; K_N, y_K, η_K) holds. Then

    Σ_{T∈𝔄, |T|=u₀} (C_T(N) − Nδ_T) ≥ N(Z_{u₀} − η_K) ≥ (1 − e^{−K/(2e²)}) N Z_{u₀} > 0,   (2.2)

i.e. the admissible u₀-tuples must carry, in aggregate, **more** integers
than CRT predicts, by at least the forced-zero mass. Equivalently: TC_θ
is incompatible with the statement *"admissible tuples are CRT-accurate in
aggregate to precision η_K at order u₀"*.

*Proof.* (1.3) with j = u₀ and `S_{u₀} − N e_{u₀} ≥ −η_K N`. ∎

**Scale.** `u₀ ≍ (log N)^{1−θ/2}` lies below the order `(log N)^{θ}`
that carries the peak moments, and the forced zeros come from the single
class −1 (the integer n + 1). Relative to the CRT moment,
`Z_{u₀}/e_{u₀} ≥ (σ_y/(2μ_y))^{u₀} = exp(−(log N)^{1−θ/2+o(1)})`, while
the precision demanded is `η_K/e_{u₀} ≤ e^{−(2/e²)(log N)^θ}`. At θ < 2/3
the inequality reverses and TC holds (T1 Prop 2.4): **2/3 is exactly the
point where the literal moment hypothesis starts to "see" the integer
structure of single forms.**

## 3. Is literal TC_θ false above 2/3?

**Lemma 3.1 (the class −1 is one-sided; PROVED).** Let G be a set of
primes `ℓ ≡ 3 (4)`, `ℓ ≤ y`, `q_G = Π_G ℓ`, and `T_G` the tuple with class
−1 at each ℓ ∈ G. Then `C_{T_G}(N) = ⌊(N+1)/q_G⌋ ≤ N/q_G + 1/q_G`, and
`= 0` if `q_G > N+1`. Hence the pure-(1,1) part of every `S_j(N)` is at
most its CRT value plus `Σ_{|G|=j} 1/q_G ≤ (log log y)^j/j!`, minus the
forced-zero mass, minus `Σ_{q_G ≤ N+1} ({(N+1)/q_G} − 1/q_G)·`(≥ 0 up to `1/q_G`).

*Proof.* `n ≤ N` with `q_G | n+1` ⟺ `n+1 ∈ q_Gℤ ∩ [2, N+1]`; there are
`⌊(N+1)/q_G⌋` such (q_G ≥ 3). ∎

So inside one form, the interval count is **never** above CRT by more than
`1/q`, and it is below CRT by the full CRT share once `q > N+1`, and by the
fractional part `{(N+1)/q}` (≈ ½ on average over N, Assessment) below that.
These are the Kubilius truncation and rounding effects of the single
integer `n + 1`. The floor deficit has the same order of magnitude as the
forced-zero mass: the number of j-sets of primes of 𝒬 with product
`≤ N+1` at `j = ⌊log(N+1)/log y⌋` is `≥ (|𝒬|−j)^j/j! = N·exp(−(log N)^{1−θ/2+o(1)})`
in the TC_θ calibration, again `≫ Nη_K` for θ > 2/3.

**Assessment 3.2 (literal TC_θ is false for every θ ∈ (2/3, 1); heuristic).**
By (1.3) and Cor 2.3, TC_θ holds only if the admissible u₀-tuples
over-represent [1,N] by at least `N Z_{u₀}`, and (by Lemma 3.1) this excess
must come from tuples that are **not** pure class −1. Compare with the
natural fluctuation scale. The sum `S_{u₀}` is a sum over N integers of
`binom(f(n), u₀)`, whose CRT second moment is
`≤ E f^{2u₀}/u₀!² ≤ (μ+2u₀)^{2u₀}/u₀!² ≤ (2μ)^{2u₀}/u₀!²` (Poisson moment
bound; `u₀ ≤ μ/2` for large N), so a square-root-cancellation model gives
fluctuations `≲ N^{1/2}(2μ)^{u₀}/u₀!`.
Against `N Z_{u₀} ≥ N(σ_y/2)^{u₀}/u₀!` the ratio is
`N^{1/2}(σ_y/(4μ))^{u₀} = N^{1/2 − o(1)}` (as `u₀ log(μ log y) = o(log N)`).
So TC_θ would need the multi-form tuples to conspire to an aggregate
excess `N^{1/2−o(1)}` times the noise floor, matching (to precision η_K) a
deficit that comes from the unrelated integer `n + 1`. No mechanism for
this is known or plausible: multi-form tuples have no common integer, and
their CRT solutions have no small rational representative. **We therefore
expect TC_θ to be false for every θ ∈ (2/3, 1)**, and true for θ < 2/3
(T1 Prop 2.4). This is an Assessment, not a theorem: a proof would need an
upper bound for the multi-form tuple counts above modulus N, which is the
same kind of input that TC itself needs.

**Consequence.** The moment-by-moment hypothesis is the wrong door. A
method that "verifies TC_θ" for θ > 2/3 would have to evaluate moments
whose true value differs from CRT by `≫ η_K`; what Theorem 2.1 of T1
actually uses is only the alternating sum, where (§4) the single-form
deviations cancel.

## 4. The repaired door: truncation-aware and alternating forms

**Hypothesis TC^𝔄(N; K, y, η).** For `1 ≤ j ≤ K`,
`|S_j(N) − N e_j^𝔄| ≤ ηN`. By (1.3) this says exactly that the
*admissible* j-tuples are CRT-accurate in aggregate. TC^𝔄_θ is TC^𝔄 with
the T1 calibration `K = K_N`, `y = y_K`, `η = η_K`.

**Hypothesis TC^alt(N; K, y, η)** (K even). `Σ_{j=0}^K (−1)^j S_j(N) ≤
N(2Π_ℓ(1−p_ℓ) + 2e^{−K}) + KηN`. This is the only consequence of TC that
T1 Thm 2.1 uses; it says that the degree-K Bonferroni (Brun pure-sieve)
majorant `ν_K(n) = Σ_{j≤K}(−1)^j binom(f_y(n), j)` has interval sum at most
its CRT mean plus `KηN`.

**Theorem 4.1 (PROVED).** Let K be even, `K ≥ e²μ_y`, and
`u₁ := ⌊log N/log y⌋ + 1 ≥ 4(1 + log y)`. Put
`ε := 4(2e(1+log y)/u₁)^{u₁}` and assume ε ≤ 1. Under the CRT law,

    Σ_{j=0}^K (−1)^j e_j^𝔄 ≤ Π_ℓ(1−p_ℓ)(1+2ε) + e^{−K}.               (4.1)

Hence, under TC^𝔄(N; K, y, η),
`#{n ≤ N : f_y(n) = 0} ≤ Σ_{j≤K}(−1)^j S_j(N) ≤ N(Π(1−p_ℓ)(1+2ε) + e^{−K} + Kη)`;
in particular TC^𝔄 ⇒ TC^alt when ε ≤ 1/2. (TC ⇒ TC^alt by T1 Thm 2.1.)

*Proof.* Let H be the CRT hit set: independently for each ℓ ∈ 𝒫_y, no
hit with probability `1 − p_ℓ`, else the pair (ℓ, b) with probability 1/ℓ
for each `b ∈ 𝓡(ℓ)`. Then `δ_T = P(T ⊆ H)`, so
`Σ_{j≤K}(−1)^j e_j^𝔄 = E Σ_{T⊆H, T∈𝔄, |T|≤K} (−1)^{|T|}`. Dropping the
condition |T| ≤ K changes this by at most `E#{T ⊆ H : |T| > K} =
Σ_{j>K} e_j ≤ Σ_{j>K}(eμ_y/j)^j ≤ e^{−K}`. Now admissibility is a
condition on each form-group separately, so

    a(H) := Σ_{T⊆H, T∈𝔄} (−1)^{|T|} = Π_φ χ_φ(H_φ),   χ_φ(G) := Σ_{U⊆G admissible} (−1)^{|U|}.

If G is admissible, so are all its subsets and `χ_φ(G) = 1[G = ∅]`; always
`|χ_φ(G)| ≤ 2^{|G|}`. Hence `a(H) = 1[H = ∅]` unless H ≠ ∅ and *every*
nonempty group `H_φ` is inadmissible, in which case `|a(H)| ≤ 2^{|H|}`.
An inadmissible group of form (r,s) has `Π ℓ > Ns + r ≥ N` with all
`ℓ ≤ y`, so it has at least u₁ elements. For any fixed set H₀ of pairs,
`P(H = H₀) ≤ Π(1−p_ℓ)·Π_{(ℓ,b)∈H₀} 1/(ℓ(1−p_ℓ))`, and `p_ℓ < 1/2`
(all classes are non-residues, `F(ℓ) ≤ (ℓ−1)/2`). Therefore

    E a(H) − P(H=∅) ≤ Π(1−p_ℓ) [Π_φ (1 + Σ_{k≥u₁} e_k(w_φ)) − 1],   w_φ = (4/ℓ)_{ℓ≤y, ℓ≡−1 (4rs)},

(over-counting by letting a prime occur in several forms only increases
the right side). With `4rsk − 1 ≥ 3rsk`,
`W_φ := Σ w_φ ≤ (4/(3rs))(1 + log y) ≤ 2(1+log y)/(rs) ≤ u₁/2`, so
`Σ_{k≥u₁} e_k(w_φ) ≤ Σ_{k≥u₁} W_φ^k/k! ≤ 2(eW_φ/u₁)^{u₁} =: t_φ`. Summing
over forms (`rs ≤ y`), `Σ_φ t_φ ≤ 2(2e(1+log y)/u₁)^{u₁} Σ_m τ(m)m^{−u₁}
≤ ε` (`ζ(u₁)² ≤ 2` for u₁ ≥ 3), and `Π(1+t_φ) − 1 ≤ e^{ε} − 1 ≤ 2ε`.
The final claim is T1 Thm 2.1's Bonferroni step with `e_j^𝔄` in place of
`e_j`. ∎

**Corollary 4.2 (PROVED implication).** For every θ ∈ (0,1), TC^𝔄_θ
implies `E(N) ≤ (e+3) N exp(−(2/e²)(log N)^θ)` for N ≥ N₀(θ). TC^alt_θ
(same calibration) implies the same.

*Proof.* In the calibration, `u₁ ≍ (log N)^{1−θ/2}` and
`log y_K ≍ (log N)^{θ/2}`, so `u₁/log y_K → ∞` and `ε → 0`; then as in T1
Cor 2.2. For TC^alt this is T1 Cor 2.2's arithmetic directly. ∎

**Status of the repaired hypotheses.**
* TC ⇒ TC^alt (T1 Thm 2.1's proof); TC^𝔄 ⇒ TC^alt up to the factor
  `1+2ε` (Thm 4.1). For θ < 2/3 all three hold (T1 Prop 2.4; the
  termwise bound applies verbatim to admissible tuples).
* TC^𝔄_θ is **also** expected false for θ > 2/3, for the same reason as
  §3: admissible pure single-form tuples with `q ≤ N+1` have the exact
  count `⌊(N+1)/q⌋`, a deficit of `{(N+1)/q} − 1/q` each, and there are
  `N exp(−(log N)^{1−θ/2+o(1)}) ≫ Nη_K` of them at order
  `⌊log N/log y⌋` (Lemma 3.1). (Assessment.)
* TC^alt is immune to every single-form effect: in the alternating sum the
  Kubilius truncation is an Euler-characteristic term `χ_φ`, which vanishes
  unless every hit sits in an inadmissible group (proof of Thm 4.1). So
  **TC^alt_θ is the correct form of the tuple-count door**, and
  momentwise correlation hypotheses (TC, TC^𝔄, any precision-η statement
  about individual S_j) are the wrong instrument above 2/3.

**What TC^alt is.** `ν_K` is a CRT majorant of order K (terms = j-tuples,
j ≤ K), so TC^alt_θ is the statement that the Brun pure sieve of degree
`K ≍ (log N)^θ` for the prime family is CRT-accurate on [1,N]. Its terms
have moduli up to `exp(c(log N)^{3θ/2}) ≫ N`. T1 Cor 3.3 does not cap
order-K majorants, so there is no proved obstruction; but the "tuple-count
door" is not an independent door. It is precisely *Brun's sieve used
beyond its level of distribution*, for the pure prime family, whose own
CRT cap is `(log N)^{2/3}` (T1 Thm 3.1 with mass `Σ p_ℓ ℓ^{−α} ≍ α^{−2}`;
see §6).
