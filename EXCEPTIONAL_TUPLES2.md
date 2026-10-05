# EXCEPTIONAL_TUPLES2 — TC_θ above 3/4 (task O24, branch `side-agent/tc-theta`)

Status: **checkpoint (O24); hostile review R24 (`reviews/exceptional-tuples2-review.md`, branch `side-agent/review-tuples2`) SOUND, minor repairs D1–D7 applied.** Labels follow `DISCOVERIES.md`. PROVED means
proved in this file (internal, unrefereed). ES is not solved. No θ > 3/4 is
claimed unconditionally.

Notation: `T1` = `EXCEPTIONAL_TUPLES.md` (Defs §1, Thm 2.1, Cor 2.2–2.3,
Prop 2.4, Prop 4.2). Prime family `𝒫_y`, classes `𝓡(ℓ)`, `p_ℓ = F(ℓ)/ℓ`,
`μ_y = Σ p_ℓ`, hit count `f_y`, order-j sums `S_j(N)`, CRT values
`e_j = e_j(p)`, TC(N; K, y, η) and TC_θ exactly as in T1 §2.

## 0. Summary

| item | statement | label |
|---|---|---|
| Lemma 1.1, Cor 1.2 | each class of 𝓡(ℓ) is `−r/s mod ℓ` with `rs | A_ℓ` ("form" (r,s)); all hits of one form divide the single integer `ns + r ≤ Ns + r`; tuples whose form-group has product `> Ns + r` have `C_T(N) = 0` though `δ_T > 0`. The class −1 (form (1,1)) lies in every 𝓡(ℓ) | PROVED |
| Thm 2.1, 2.2 | the CRT mass `Z_j` of such forced-zero tuples satisfies `Z_{u₀} ≥ (σ_y/2)^{u₀}/u₀!`, `u₀ = ⌈log(N+2)/log(y/2)⌉`; in the TC_θ calibration `Z_{u₀} ≥ η_K e^{K/(2e²)}` for **every θ > 2/3** | PROVED |
| Cor 2.3 | TC_θ (θ > 2/3) holds only if the admissible tuples carry an aggregate CRT **excess** ≥ the forced-zero mass; TC_θ is incompatible with "admissible tuples are CRT-accurate" | PROVED |
| Lemma 3.1 | for the class −1 (form (1,1)) the interval count is one-sided: `C = ⌊(N+1)/q⌋ ≤ N/q + 1/q` (Kubilius truncation + floors); false for general forms (e.g. (r,s) = (1,2), ℓ = 7, N = 3) | PROVED |
| Ass. 3.2 | **literal TC_θ is false for every θ ∈ (2/3,1)**: it needs a conspiratorial excess `N^{1/2−o(1)}` times the square-root noise floor; true for θ < 2/3 (T1 Prop 2.4) | Assessment |
| Thm 4.1, Cor 4.2 | the truncation-aware hypothesis TC^𝔄_θ, and the one-sided alternating hypothesis TC^alt_θ, imply `E(N) ≤ (e+3)N exp(−(2/e²)(log N)^θ)` resp. `≤ (2e+2)N exp(…)`; the forced-zero correction to the CRT mass cancels in the alternating sum: `|Σ_{j≤K}(−1)^jZ_j| ≤ 2εΠ(1−p)+2e^{−K}` (4.1′, Euler-characteristic argument) | PROVED |
| §4 status | TC^𝔄 is also expected false above 2/3 (floor deficits); **TC^alt_θ (one-sided: degree-K Brun sieve on [1,N] at most ≈ twice the CRT avoider density) is the correct form of the door** | Assessment |
| §5 | toy numerics: class −1 forced zeros exceed η_K by 10³–10⁵ at the T1 test parameters; the T1 §5(b) moment deficits are an initial-segment effect (absent on far translates), about one third explained by single-form effects | EVIDENCE |
| Cor 6.1 | for the pure prime family every CRT majorant of level ≤ A log N saves ≤ C(log N)^{2/3}; so TC^alt_θ for any θ > 2/3 needs CRT accuracy at moduli `exp(c(log N)^{3θ/2})` | PROVED (from T1 Thm 3.1) |
| Ass. 6.2 | no known theorem (BV/EH/BFI/dispersion, roots-of-congruences equidistribution, fixed-shift correlations, Kubilius) supplies TC^alt_θ for any θ > 2/3 | Assessment |
| Prop 7.1 | T1 Cor 3.4 gap closed for block-sparse K2 families (≤ r primes of each modulus in every `(x, x²]`): order-k majorants save `≤ C(log N)^{3/4}(log log N)^{3/4} + Ckr(log log N)²` | PROVED (K2 Thm 5.1's proof, d-locality changed) |

**Verdict.** Task (B) is settled in the following sense. The tuple-count
hypothesis TC_θ of T1/(D)21, as stated (each moment `S_j` CRT-accurate to
absolute precision η_K), can hold for θ > 2/3 only if an implausible
compensating excess occurs (PROVED necessary condition, Cor 2.3): the class −1 sits in every 𝓡(ℓ), so its hits are
prime divisors of the one integer n+1, and the CRT moments contain a
forced-zero mass far above η_K (Thm 2.2). TC_θ can then only hold through
an implausible compensating excess (Cor 2.3, Ass. 3.2). So the expected
failure threshold of the literal hypothesis is **θ = 2/3**, not ≈ 1 as the
squares (T1 Prop 4.2) suggested. Proved: TC holds below 2/3, and above
2/3 it *requires* that excess. That TC_θ actually fails above 2/3 is an
Assessment (CONJECTURE), not a theorem. This does **not** close the door:
the forced-zero correction lives in individual moments and cancels in the
alternating sum that T1 Thm 2.1 actually uses (Thm 4.1); the analogous
cancellation of the floor deficits is heuristic. The
correct door is TC^alt_θ, a one-sided Brun-sieve statement, which still
gives `E(N) ≤ (2e+2)N exp(−(2/e²)(log N)^θ)` (Cor 4.2). Task (A): no
positive result; TC^alt_θ for θ > 2/3 is beyond CRT by Cor 6.1 and no
known theorem reaches its level `exp(c(log N)^{3θ/2})` (Ass. 6.2). No
structured obstruction to TC^alt below θ = 1 was found: the forced-zero
correction provably cancels in it, the floor deficits heuristically do,
and the square-type obstructions (n = c·k²) have polynomial density. Task (C): closed for block-sparse families (Prop 7.1).

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
`≈ e^{μ_{y/2}}/√μ`; the threshold θ = 2/3 does not move.)

**Corollary 2.3 (literal TC_θ forces a CRT excess; PROVED).** Let
θ ∈ (2/3, 1), N ≥ N₀(θ), and suppose TC(N; K_N, y_K, η_K) holds. Then

    Σ_{T∈𝔄, |T|=u₀} (C_T(N) − Nδ_T) ≥ N(Z_{u₀} − η_K) ≥ (1 − e^{−K/(2e²)}) N Z_{u₀} > 0,   (2.2)

i.e. the admissible u₀-tuples must carry, in aggregate, **more** integers
than CRT predicts, by at least `N(Z_{u₀} − η_K)`. Equivalently: TC_θ
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

**Lemma 3.1 (the class −1 is one-sided; PROVED).** Let G be a nonempty set of
primes `ℓ ≡ 3 (4)`, `ℓ ≤ y`, `q_G = Π_G ℓ`, and `T_G` the tuple with class
−1 at each ℓ ∈ G. Then `C_{T_G}(N) = ⌊(N+1)/q_G⌋ ≤ N/q_G + 1/q_G`, and
`= 0` if `q_G > N+1`. Hence the pure-(1,1) part `Σ_{|G|=j} C_{T_G}(N)` of
`S_j(N)` equals its CRT value `N Σ_{|G|=j} 1/q_G` minus the forced-zero
mass `N Σ_{q_G > N+1} 1/q_G` minus the floor deficit
`Σ_{q_G ≤ N+1} ({(N+1)/q_G} − 1/q_G)`; the last is `≥ −Σ_G 1/q_G
≥ −(log log y + 1)^j/j!`.

*Proof.* `n ≤ N` with `q_G | n+1` ⟺ `n+1 ∈ q_Gℤ ∩ [2, N+1]`; there are
`⌊(N+1)/q_G⌋` such (q_G ≥ 3). ∎

So for the class −1 (not for general forms: `(r,s) = (1,2)`, ℓ = 7, N = 3
gives `C = 1 > 4/7`), the interval count is **never** above CRT by more than
`1/q`, and it is below CRT by the full CRT share once `q > N+1`, and by the
fractional part `{(N+1)/q}` (≈ ½ on average over N, Assessment) below that.
These are the Kubilius truncation and rounding effects of the single
integer `n + 1`. The floor deficit has the same order of magnitude as the
forced-zero mass: the number of j-sets of primes of 𝒬 with product
`≤ N+1` at `j = ⌊log(N+1)/log y⌋ ≤ |𝒬|` is `≥ (|𝒬|−j)^j/j!`, which in the
TC_θ calibration is `≥ N·exp(−(log N)^{1−θ/2+o(1)})` (as `y^j ≥ (N+1)/y`
loses only `exp((log N)^{θ/2})` and `θ/2 < 1 − θ/2`), again `≫ Nη_K` for
θ > 2/3.

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
whose true value is expected (Ass. 3.2; not proved) to differ from CRT by
`≫ η_K`; what Theorem 2.1 of T1
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
`N(2Π(1−p_ℓ) + 2e^{−K}) + KηN`. Its CRT mean lies in
`[Π(1−p_ℓ), Π(1−p_ℓ) + e^{−K}]`, so TC^alt is a deliberately relaxed
one-sided upper-bound hypothesis (interval sum at most about twice the CRT
mean), not an accuracy statement.

**Theorem 4.1 (PROVED).** Let K be even, `K ≥ e²μ_y`, and
`u₁ := ⌊log N/log y⌋ + 1 ≥ 4(1 + log y)`. Put
`ε := 4(2e(1+log y)/u₁)^{u₁}` and assume ε ≤ 1. Under the CRT law,

    Σ_{j=0}^K (−1)^j e_j^𝔄 ≤ Π_ℓ(1−p_ℓ)(1+2ε) + e^{−K}.               (4.1)

More precisely (two-sided), `|Σ_{j≤K}(−1)^j e_j^𝔄 − Π(1−p_ℓ)| ≤
2εΠ(1−p_ℓ) + e^{−K}`, and hence, since `Σ_{j≤K}(−1)^j e_j` lies in
`[Π(1−p_ℓ), Π(1−p_ℓ) + e^{−K}]` (T1 Thm 2.1's identity),

    |Σ_{j≤K}(−1)^j Z_j| ≤ 2εΠ(1−p_ℓ) + 2e^{−K}.                         (4.1′)

This is the precise sense in which the forced-zero correction "cancels".

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
The bound `|a(H) − 1[H=∅]| ≤ 2^{|H|}` (on the event that H ≠ ∅ and every
nonempty group is inadmissible; `= 0` otherwise) and the |T| > K tail are
two-sided, which gives the two-sided form and (4.1′). The final claim is
T1 Thm 2.1's Bonferroni step with `e_j^𝔄` in place of
`e_j`. ∎

**Corollary 4.2 (PROVED implication).** For every θ ∈ (0,1), TC^𝔄_θ
implies `E(N) ≤ (e+3) N exp(−(2/e²)(log N)^θ)` for N ≥ N₀(θ). TC^alt_θ
(same calibration) implies `E(N) ≤ (2e+2) N exp(−(2/e²)(log N)^θ)`.

*Note (not a reduction).* The TC^alt half is a one-line consequence of
the pointwise Bonferroni inequality `ν_K ≥ 1[f_y = 0]`: TC^alt_θ is
essentially the desired conclusion restricted to one specific majorant.
Its factor 2 is not cosmetic at toy scale: at N = 10⁷, y = 1000 the
[1,N] avoider count is 1.22× its CRT value (≈ the √N squares: 3162
against `NΠ(1−p) ≈ 13270`), versus 0.99–1.01× on far translates
(EVIDENCE, R24 `scripts/review_t2_translates.py`).

*Proof.* In the calibration, `u₁ ≍ (log N)^{1−θ/2}` and
`log y_K ≍ (log N)^{θ/2}`, so `u₁/log y_K → ∞` and `ε → 0`; then as in T1
Cor 2.2. For TC^alt: `Π(1−p_ℓ) ≤ e^{−μ_{y_K}} < e^{1−K/e²}` (T1 Cor 2.2's
proof), so `2Π(1−p) + 2e^{−K} + Kη_K ≤ (2e + 2)e^{−K/e²}` for large K. ∎

**Status of the repaired hypotheses.**
* TC ⇒ TC^alt (T1 Thm 2.1's proof); TC^𝔄 ⇒ TC^alt up to the factor
  `1+2ε` (Thm 4.1). For θ < 2/3 all three hold (T1 Prop 2.4; the
  termwise bound applies verbatim to admissible tuples).
* TC^𝔄_θ is **also** expected false for θ > 2/3, for the same reason as
  §3: admissible pure single-form tuples with `q ≤ N+1` have the exact
  count `⌊(N+1)/q⌋`, a deficit of `{(N+1)/q} − 1/q` each, and there are
  `N exp(−(log N)^{1−θ/2+o(1)}) ≫ Nη_K` of them at order
  `⌊log N/log y⌋` (Lemma 3.1). Whether their total `Σ({(N+1)/q} − 1/q)`
  is of that size at the calibrated N is not proved (individual terms can
  be negative when `q | N+1`; the size `≈ ½` per tuple is an average over
  N). (Assessment.)
* TC^alt fails for even `K ≥ (e²/2+ε) log N`, N ≥ N₀(ε) (squares: T1
  Prop 4.2's proof uses only the Bonferroni bound; the factor 2 in TC^alt
  only changes N₀). The calibrated endpoint θ = 1
  (`K ≈ 2 log N`) is not decided by this argument, as in T1.
* In the alternating sum the forced-zero (truncation) correction to the
  CRT mass is an Euler-characteristic term `χ_φ`, which vanishes unless
  every hit sits in an inadmissible group (Thm 4.1, PROVED). The floor
  deficits are *empirical* errors, not CRT-mass corrections; that they
  also cancel in the alternating sum is the heuristic content of TC^alt
  (for the class −1 alone it is the fundamental lemma for sieving `n + 1`,
  whose relative error is `u^{−u(1+o(1))}`). So
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

## 5. Numerics (EVIDENCE, toy scale)

Scripts: `scripts/tuples2_forced.py` (class −1 forced zeros, exact DP with
logs rounded down, so a lower bound; pure class −1 floor deficits by
enumeration), `scripts/tuples2_allforms.py` (the same summed over all
forms (r,s), 4rs−1 ≤ y; collisions between forms ignored, so an estimate),
`scripts/tuples2_translates.py` (moments on `[t+1, t+N]`).

**(a) Forced zeros versus η_K already at toy scale.** At the T1 §5(c)
test parameters (`K` = first even integer ≥ e²μ_y):

| N, y | K | η_K | u₀ | Thm 2.1 bound `e_{u₀}(q)` | `Z^{(1,1)}_{u₀}` | `max_j Z^{(1,1)}_j/η_K` (j ≤ 12) |
|---|---|---|---|---|---|---|
| 10⁸, 1000 | 46 | 4.3·10⁻⁵ | 3 | 2.0·10⁻⁵ | 1.6·10⁻⁴ | 9.2·10² (j = 8) |
| 10⁸, 3000 | 60 | 5.0·10⁻⁶ | 3 | 1.4·10⁻⁵ | 2.1·10⁻³ | 1.8·10⁵ (j = 10) |

(`data/tuples2/forced_*.txt`.) So the class −1 forced zeros alone violate
the TC precision by factors 10³–10⁵ at these parameters; the multi-form
tuples would have to compensate. Caveat (R24-D6): T1 §5(c) found that
even the `rand` control fails the TC test for y ≥ 300, so at toy scale
exceeding η_K is not ES-specific, and toy data cannot show that the
compensation is absent beyond noise. The statement here concerns a
deterministic CRT mass. (Consistent with Ass. 3.2: at (10⁸, 1000), j = 8,
the observed T1 deficit, 0.90%, has the same sign as and exceeds the
pure-(1,1) forced-zero share `Z^{(1,1)}_8/e_8 = 2.1·10⁻³`.)

**(b) The T1 §5(b) moment deficits are an initial-segment effect.** Ratios
`S_j/(N e_j)` at N = 10⁷, y = 1000 (`data/tuples2/translates_1e7_1000.txt`):

| window | j = 4 | 6 | 8 | 10 | 12 |
|---|---|---|---|---|---|
| [1, N] | 0.9982 | 0.9914 | 0.9737 | 0.9385 | 0.8827 |
| t = 10¹² | 1.0000 | 1.0001 | 1.0016 | 1.0112 | 1.0473 |
| t = 2.718·10¹² | 1.0000 | 0.9996 | 0.9982 | 0.9949 | 0.9858 |
| t = 3.14·10¹³ | 1.0002 | 1.0010 | 1.0000 | 0.9814 | 0.9022 |
| t = 10¹⁵ | 1.0000 | 1.0002 | 1.0001 | 0.9955 | 0.9643 |

On far translates the j ≤ 8 ratios are 1 to within 0.2% (both signs; j ≥
10 is tail-noise dominated), while [1,N] has a systematic deficit. This is
what the mechanism of §1 predicts: the constraint `ns + r ≤ Ns + r` is a
property of small integers.

**(c) How much of the [1,N] deficit is single-form?** Relative deficit
`1 − S_j/(N e_j)` (T1 data) versus the single-form estimate
`(Z_all + Fl_all)/e_j` (`data/tuples2/allforms_*_1000.txt`), y = 1000:

| N | j = 8 observed | single-form | j = 12 observed | single-form |
|---|---|---|---|---|
| 10⁶ | 7.2% | 2.3% | 15.4% | 8.4% |
| 10⁷ | 2.6% | 0.81% | 11.7% | 3.7% |
| 10⁸ | 0.90% | 0.25% | 6.3% | 1.5% |

The `randqnr` control (T1) shows 0.15% (j = 8) and 1.7% (j = 12) at
N = 10⁸; `rand` shows none. So single-form effects account for roughly a
third of the toy deficit, quadratic-character structure for a further
part; the rest (≈ 0.5% at j = 8, N = 10⁸) is unexplained, decays with N at
the same rate as the single-form part, and is also absent on translates.
Caveat: `tuples2_allforms.py` sums forced-zero events form by form, so
tuples inadmissible in two forms (and colliding representatives) are
counted more than once; "about a third" is an uncontrolled estimate, not a
decomposition of the observed deficit.
Plausible source (untested): small-height relations between two forms.
None of this bears on asymptotic θ; it only shows that the deviations of
§§2–3 are real and visible, and all of the same sign (deficit).

**(d) Tail sampling at small y.** At N = 10⁶, y = 100 the histogram of
`f_y` matches the CRT law within Poisson noise (e.g. 972/119/5 integers
with f = 8/9/10 against 1021/120/9.7 predicted), so the large T1 ratio
deviations at j ≥ 8 there come from a handful of integers.

## 6. The positive direction: what TC^alt_θ needs

**Corollary 6.1 (CRT cap 2/3 for the pure prime family; PROVED from T1
Thm 3.1).** Fix A ≥ 1. Let `y ≤ N^A` and let ν ≥ 0 be a CRT majorant
(`ν = Σ a_i 1[n ≡ b_i (d_i)]`, ν ≥ 0 on ℤ) with ν ≥ 1 on the avoider set
`{f_y = 0}` of the prime family, all of whose terms have level
`Σ_{ℓ∈𝒫_y, ℓ | d_i, ℓ ≥ ℓ₀} log ℓ ≤ λ`, `λ ≥ log N`. Then
`log(1/Eν) ≤ C_A λ^{2/3}`. Hence (as in T1 Cor 3.3) every method that
evaluates such a ν on [1,N] with CRT main terms (bound `≥ ½N·Eν`) and
level `λ ≤ A' log N` saves at most `C(log N)^{2/3}`; Brun's pure sieve
(T1 Prop 2.4) attains this order.

*Proof.* Put the primes `ℓ < ℓ₀` (with `p_ℓ > 1/4`; e.g. ℓ = 3, 7) into
the small modulus Q₀ of a prime-slice system; then `|R|/Q₀ =
Π_{ℓ<ℓ₀}(1−p_ℓ) ≫ 1`, and every slice prime has `p_ℓ ≤ τ(A_ℓ²)/ℓ ≤ 1/4`
for ℓ₀ large. Apply T1 Thm 3.1 with k = 1, `L₀ = λ₀ = λ`. By partial
summation from `μ_x ≤ C(log x)²` (T1 (1.3)),
`Σ_ℓ p_ℓ ℓ^{−α} ≤ ∫ αx^{−α−1}μ_x dx ≤ 2C α^{−2}`. The tail term is
`e^{−αλ}μ_y ≤ C(A log N)²e^{−αλ}`. With `α = λ^{−1/3}` all terms are
`O(λ^{2/3})` (`αλ = λ^{2/3} ≥ (log N)^{2/3}` kills the tail; the G-terms
are `O(log²λ + log λ·log log y)`). ∎

So for the pure prime family the CRT exponent is exactly 2/3, and the
literal TC door closes exactly there (§§2–3). TC^alt_θ for any θ > 2/3
(not only θ > 3/4) is a non-CRT statement: by Cor 6.1 a saving
`(log N)^θ` needs level `λ ≥ c(log N)^{3θ/2}`, so the Bonferroni majorant
`ν_K` must be evaluated
with CRT accuracy on terms of level `≥ c(log N)^{3θ/2}`, i.e. moduli
`Q = exp(c(log N)^{3θ/2})`, super-polynomial in N for θ > 2/3.

**Assessment 6.2 (no known theorem supplies TC^alt_θ for θ > 2/3).**
* Level of distribution. All BV/EH/BFI-type results, and all dispersion
  estimates, concern moduli `< N` (a class of modulus > N meets [1,N] at
  most once). The required level is `exp(c(log N)^{3θ/2})`.
* Beyond N, the only "equidistribution of CRT points" results are for
  roots of a *fixed* polynomial congruence (Hooley; Duke–Friedlander–
  Iwaniec; Tóth), at macroscopic test functions on `ν/q mod 1`. TC^alt
  needs the points `b_T/q_T` at the microscopic scale `N/q_T`, for a family
  of linear systems with K growing; that is equivalent to counting the
  integers n ≤ N with prescribed hits, i.e. to the sieve problem itself.
* Fixed-shift / fixed-form correlations (T1 Prop 4.3, §4.2): the forms of
  §1 make the "shift" picture precise. A tuple of order j spans ≈ j
  distinct forms; correlations along r fixed forms are capped at
  `O(r log log N)` (T1 Prop 4.3, whose proof applies verbatim to the
  integers `ns + r` in place of `n + 4D`).
* Kubilius-type models hold *inside* one form (one integer `ns + r`),
  which is exactly where literal TC fails (§3), and they say nothing
  about joint behaviour across ≍ (log N)^θ forms.

So the positive direction is closed off from every known technique, and
the target is sharper than T1 stated: not "TC_θ with θ > 3/4" (false
above 2/3 under the natural heuristic) but "Brun's sieve of degree
(log N)^θ, θ > 2/3, is CRT-accurate on [1,N] for the prime family"
(TC^alt_θ), with the E(N) gain appearing only for θ > 3/4.

## 7. The gap in T1 Cor 3.4 (T1 §6 item 2)

T1 Cor 3.4 bounds an order-k majorant of a composite-moduli K2 family by
its level `kA log N`, so it only excludes `k < (log N)^{4θ/3−1}`. The
prime-slice proof (T1 Thm 3.1) uses that an order-k term depends on ≤ k
slice primes in *every* scale. For composite moduli this fails: one class
of modulus `≤ N^A` can have up to `A log N/s` primes in `(e^s, e^{2s}]`.
That, not the weights, is the real obstruction. It disappears for
block-sparse families.

**Proposition 7.1 (PROVED, by K2 Thm 5.1's proof with one change).** Let
𝔊 be a K2 family (Def 2.0 there) with all moduli `≤ N^A`, such that every
modulus has at most r prime factors in every interval `(x, x²]`, x ≥ 2
(an N-free condition; it implies ≤ r primes in each block
`V_i ⊆ (e^s, e^{2s}]` of K2 §5, continued past `e^{λ₀/2}`, for every N). Let ν be a majorant of
`𝒜(𝔊)` each of whose terms has level `≤ λ₀ := A log N` or is an
intersection of at most k classes of 𝔊. Then

    log(1/Eν) ≤ C λ₀^{3/4}(log λ₀)^{3/4} + C k r (log log N)².

Hence, for methods as in T1 Cor 3.3 (bound `≥ ½N·Eν`), a saving
`(log N)^θ` with θ > 3/4 needs `k ≥ c(log N)^θ/(r(log log N)²)`; for
bounded r this closes the gap of T1 Cor 3.4 up to a `log log N` factor.

*Proof.* K2 §1 records that the level enters the proof of K2 Thm 5.1 only
through d-locality: in block `V_i` every term of ν depends on at most
`d_i` block primes, and EK Thm 2.5 accepts any arity. Here a term of
level `≤ λ₀` has `≤ λ₀/s` primes in `V_i` (`s = 2^is₁`), and an
intersection of ≤ k classes has `≤ kr`. So `d_i ≤ λ₀/s + kr` for every
block, including blocks above `e^{λ₀/2}` (where low-level terms have at
most one prime), which we treat as further dyadic blocks up to `N^A`
instead of K2's linear block and empty tail. Keep K2's base, leak,
singletons below `e^{s₁}` with `s₁ = λ₀^{1/4}(log λ₀)^{−3/4}`, and block
step bound `EΦ_i ≤ d_i log(C₀(E M_{V_i} + 4d_i)/d_i) + (4/3)d_i +
½log(22d_i+22) + 3`. Its main part `g(d) = d log(C₀(M+4d)/d)` has
`g(d)/d` decreasing, hence is subadditive, `g(a+b) ≤ g(a) + g(b)`, and the
remaining terms are subadditive up to O(1) per block; so the cost at
`d_i ≤ λ₀/s + kr` splits into the two parts below. The λ₀/s part
reproduces K2's sum `Cλ₀^{3/4}(log λ₀)^{3/4}`. The kr part costs, per
block, `kr·log(C₀(8K₃s³(log 2s)³ + 4kr)/(kr)) + O(kr) ≤ C kr log log N`
(as `s ≤ A log N`), over `O(log log N)` blocks. ∎

*Scope.* This uses K2 Thm 5.1's proof structure as described in K2 §§1,
5; the blocks above `e^{λ₀/2}` reuse the generic block step (first
moments `𝔐(y)` hold for all y, K2 Cor 3.7). Families with unboundedly many
primes per block per modulus remain open: there one would have to show
that dense classes (r+1 primes in one block; mass `≲ (log 2)^{r+1}/(r+1)!`
per block relative) can be absorbed into the leak. Not attempted.

## Replay

```
cd scripts
for a in "1e6 100" "1e6 1000" "1e8 1000" "1e8 3000"; do uv run python tuples2_forced.py $a 12 > ../data/tuples2/forced_$(echo $a|tr ' ' _).txt; done   # §5(a); ~1 min total
for a in "1e8 1000" "1e7 1000" "1e6 1000"; do uv run python tuples2_allforms.py $a 13 > ../data/tuples2/allforms_$(echo $a|tr ' ' _).txt; done        # §5(c); seconds
uv run python tuples2_translates.py 1e7 1000 0,1e12,2.718281828e12,3.14159265e13,1e15 13 > ../data/tuples2/translates_1e7_1000.txt   # §5(b); ~5 min, < 1 GB
```
§5(c)'s "observed" column is T1's `data/tuples/moments_N{1e6,1e7,1e8}_es.txt` (y = 1000 block).
§5(d): histogram of f_y vs the exact Poisson-binomial law at N = 10⁶, y = 100 (one-off check, ~10 lines of numpy using `tuples_moments.R_set`).
