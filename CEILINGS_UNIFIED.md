# One sieve limit behind both ceilings (task O60)

Branch `side-agent/unify-ceilings`. Labels follow the house rules. ES is not
solved here or anywhere. Nothing below improves the exceptional-set exponent
3/4 or the pointwise exponent 1/4.

Notation. `T` = witness-modulus cutoff, `𝓛 = log T`. `W(p)` = least witness
modulus `kℓ` as in notes (51.1)–(51.2). "The note" = `paper/es-threequarter-note.tex`
(INTERNALLY PROVED, (B)11). `t = log X`, `K = ⌊X^κ⌋`, `A_X`, `H_X`, `L_K`,
`f_c(ℓ)`, `μ_c` as in the note §§2–4. `P_*` / `E_*` = Haar measure on units
`Ẑ^×` (for a function of `n mod L`: uniform on `(ℤ/L)^×`).

## 0. Dictionary (Assessment, made precise in §§1–4)

| | exceptional set (note, KARY) | pointwise (OMEGA13/14) |
|---|---|---|
| system | atoms of modulus `kℓ ≤ KX ≤ T` | events of modulus `≤ T` |
| mass / dimension `κ` | `μ_c ≍ t³` (note Cor 4.3) | `≍ 𝓛³/log𝓛` (OMEGA14 §4) |
| certificate | majorant `S_yQ_r(H_X)`, `r ≍ t³` | minorant `B ≤ F` |
| level needed | `log q ≍ r·t ≍ t⁴` (note Thm 8.2) | `log D ≍ κ𝓛 ≍ 𝓛⁴` (OMEGA14 Thm 4.5) |
| level available | `log N` (rounding) | `log x` (transfer to primes ≤ x) |
| result | `t ≍ (log N)^{1/4}`, saving `t³` | `𝓛 ≍ (log x)^{1/4}` |

Both are the single relation `λ ≍ 𝓛·κ(𝓛) = 𝓛⁴` between the level `λ` (log of
the largest CRT modulus) and the size `𝓛` of the moduli that can be fully
exploited. The exceptional exponent is `κ(λ^{1/4}) = λ^{3/4}`, the pointwise
exponent is `λ^{1/4}`; with Haar exponent `a` they are `a/(a+1)` and
`1/(a+1)`, so they sum to 1.

## 1. The note's void is a Haar bound: `log(1/δ*(T)) ≫ 𝓛³` without log loss

**Proposition 1.1 (PROVED given the note's Cor 4.3 = notes Thm 34.8/76.2,
INTERNALLY PROVED).** There are `c, T_0 > 0` such that for `T ≥ T_0`,
with `X = T^{1/(1+κ)}`:
```
P_*(H_X(n) = 0) ≤ exp(−a_h' t³),   and   δ*(T) ≤ 8·exp(−c𝓛³),
```
where `δ*(T)` is the POINTWISE_HAAR avoider density (Haar on `Ẑ^×`, normalised
on `n ≡ 1 (24)`). Hence `log(1/δ*(T)) ≫ 𝓛³`, removing the `1/log𝓛` loss of
POINTWISE_HAAR Thm 2.1; with OMEGA13 Thm 3.4,
`𝓛³ ≪ log(1/δ*(T)) ≪ 𝓛³(log𝓛)^5`.

*Proof.* Condition on `c = n mod L_K`. Under `P_*`, `c` is a unit mod `L_K`,
and the coordinates `n mod ℓ` for the primes `ℓ ∈ (X^{1/2}, X]` (all `> K`, so
coprime to `L_K`) are independent of `c` and of each other, each uniform on
`(ℤ/ℓ)^×` (CRT on unit groups). By note Lemma 2.2, at fixed `ℓ` the active
atoms have pairwise distinct projections mod `ℓ`, and these are units
(atom residue `−uv^{-1}`, `ℓ ∤ uv` as `uv < ℓ`). So
```
P_*(H_X = 0 | c) = ∏_ℓ (1 − f_c(ℓ)/(ℓ−1)) ≤ ∏_ℓ (1 − f_c(ℓ)/ℓ) ≤ e^{−μ_c}.
```
For reduced `c`, note Cor 4.3 gives `μ_c ≥ a_h t² h(K(K)) ≥ a_h a_0 κ t³/2`
(note Lemma 3.2). Averaging over `c` gives the first bound. Conditioning on
`n ≡ 1 (24)` only restricts `c mod 3` (`3 | L_K` since `9 ∈ K(K)`) and the
independent coordinate `n mod 8`; the fibre bound holds for every unit `c`,
so it holds after conditioning. Every atom is a witness class of modulus
`kℓ ≤ KX = T` (note Lemma 2.1 with `w = (kℓ+1)/(4uv)`; equivalently a class of
`ℛ(kℓ)`, (B)1), so `{no event of modulus ≤ T} ⊆ {H_X = 0}`. Finally `t ≍ 𝓛`.
(The factor 8 is not needed but harmless.) ∎

*Remark 1.2 (Assessment).* POINTWISE_HAAR proved `≫ 𝓛³/log𝓛` by a Janson
inequality over squarefree `𝓛⁵`-rough moduli. The note's family is simpler
for this purpose: one large prime per atom plus a revealed small coordinate
`c` makes the events conditionally independent, so the exact product
replaces Janson. The two documents were never cross-referenced. The new
dependency is BV (via the note's supply theorem); POINTWISE_HAAR used only the
fundamental lemma. Both lower bounds remain valid.

## 2. Witness-modulus tail relative to π(x) (goal (b))

**Theorem 2.1 (PROVED given the note (INTERNALLY PROVED, (B)11) and the
classical prime number theorem in progressions, uniform for
`q ≤ exp(c₂√log x)`, with the Landau–Page exceptional term ("Page's theorem";
Davenport, *Multiplicative Number Theory*, Ch. 20)).**
There are absolute `c, c₁ > 0` such that, uniformly for `x ≥ 3` and
`3 ≤ T ≤ exp(c₁(log x)^{1/4})`,
```
#{p ≤ x prime : W(p) > T} ≪ π(x)·exp(−c(log T)³).
```
This upgrades ledger (A)9 / notes Thm 51.2(2) in two ways: the label (it
was CLAIMED/PROVISIONAL because Thm 34.8 was; the note now proves that input),
and the normalisation (`π(x)` instead of `N`, which matters when
`(log T)³ ≲ log log x`). No `polylog` loss.

*Proof.* Bounded `T` is trivial; let `T ≥ T_0`. Put `X = T^{1/(1+κ)}`,
`t = log X`, so `KX ≤ T`; let `y = Bt³` and `r` the least even integer
`≥ D_B t³`, with `B, D_B` as in note Thm 8.2 (enlarging `D_B` is allowed
there). Put `ν = S_y Q_r(H_X)`. Then `ν ≥ 0` on ℤ (note Lemma 8.1), and for a
prime `p > y` with `W(p) > T` we have `H_X(p) = 0` (an active atom is a
witness of modulus `kℓ ≤ T`, notes (51.2)), so `ν(p) = 1`. Hence
`#{p ≤ x : W(p) > T} ≤ y + Σ_{p≤x} ν(p)`, and `y = Bt³` is negligible.

*Case A: `c_a t³ ≥ 2 log log x`.* Choose `c₁` with `log x ≥ C_0 t⁴`. By note
Thm 8.2, `Σ_{p≤x} ν(p) ≤ Σ_{n≤x} ν(n) ≪ x e^{−c_a t³} ≤ x e^{−c_a t³/2}/log x`.

*Case B: `c_a t³ < 2 log log x`.* Then `t⁴ ≪ (log log x)^{4/3}`, so by the
ledger (ledger of note Thm 8.2) every term modulus `q` and the coefficient sum satisfy
`q, T_abs ≤ e^{C t⁴} ≤ exp(c₂√log x)` for `x ≥ x_0`.
(i) *Prime sum.* Write `ν = Σ_i c_i 1[n ≡ a_i (q_i)]`. Then
`Σ_{p≤x} ν(p) ≤ T_abs√x + (2/log x)Σ_{n≤x} ν(n)Λ(n)` (`ν ≥ 0`, `‖ν‖_∞ ≤ T_abs`),
and `Σ_{n≤x}νΛ = Σ_i c_i ψ(x; q_i, a_i)`. Terms with `(a_i,q_i) > 1` contribute
`≤ T_abs(log x)²`. For `(a,q)=1`, `q ≤ exp(c₂√log x)`, Page's theorem gives
`ψ(x;q,a) = x/φ(q) − 1_{q_1|q} χ_1(a) x^{β_1}/(φ(q)β_1) + O(x e^{−c₃√log x})`,
where `χ_1` (primitive mod `q_1`) is the possible exceptional real character
for this range. (Davenport Ch. 20; also Montgomery–Vaughan I, Cor. 11.17 —
the form of this classical statement was recalled, not re-checked against a
PDF; any version with range `q ≤ exp(c₂√log x)` and error `x e^{−c₃√log x}`
suffices, as only `t⁴ ≪ (log log x)^{4/3}` is needed.) Define the unit-Haar functional `E_*f = Σ_{(a_i,q_i)=1} c_i/φ(q_i)`
and `χ̃_1 = χ_1(n mod q_1)` on `Ẑ^×`. Since `∫_{n≡a (q)} χ̃_1 dP_* = χ_1(a)/φ(q)`
if `q_1 | q` and `= 0` otherwise (primitivity: `χ_1` is non-trivial on the kernel of
`(ℤ/q_1)^× → (ℤ/(q,q_1))^×` when `q_1 ∤ q`), the main terms sum to
`x·E_*[ν(1 − εχ̃_1)]`, `ε = x^{β_1−1}/β_1 ∈ [0, 2]` (`β_1 ≥ 1/2`). As `ν ≥ 0`
on every residue class, hence on `Ẑ^×`, this is `≤ 3x E_*ν`. So
```
Σ_{p≤x} ν(p) ≤ (6x/log x)·E_*ν + O(x e^{−c₃√log x /2}).
```
The error is `≪ π(x)e^{−t³}`-negligible since `t³ ≪ log log x`.
(ii) *Unit mean.* On units `S_y = 1`, so `E_*ν = E_* Q_r(H_X)`. Condition on
the unit `c = n mod L_K`; as in Prop 1.1, `H_X = Σ_ℓ I_ℓ` with independent
Bernoulli `I_ℓ` of mean `f_c(ℓ)/(ℓ−1) ≤ 2f_c(ℓ)/ℓ`, so
`E_*((H_X)_m | c) ≤ (2μ_c)^m ≤ (2C_u t³)^m` (note Cor 4.3) and
`P_*(H_X = 0 | c) ≤ e^{−μ_c} ≤ e^{−a t³}` (Prop 1.1). By note Lemma 8.1,
`E_*Q_r(H) ≤ P_*(H=0) + E_*(H)_{r+1}/(r+1)! ≤ e^{−a t³} + (2eC_u t³/(r+1))^{r+1}
≤ 2e^{−a t³}` once `D_B ≥ 2e²C_u` and `D_B ≥ 2a`.
Combining: `Σ_{p≤x}ν(p) ≪ π(x)e^{−a t³}`. In both cases `t ≍ log T`. ∎

*Remark 2.2 (scope).* Case B is exactly the Siegel-model transfer
`(1 − εχ_1)P` that POINTWISE_OMEGA15 Thm 3.1 analyses for minorants: for
*majorants* the exceptional character costs only the factor `1 + ε ≤ 3`,
because a majorant is non-negative. This asymmetry (upper bounds tolerate
Siegel zeros, lower bounds need `E_*[B(1−εχ)] > 0`) is the familiar one.
Theorem 2.1 is the "typical-size" statement on the exceptional side; the
pointwise side asks for the *opposite* inequality (some `p ≤ x` with
`W(p) > T`), whose certificate must be a minorant (§4).

## 3. Goal (a): the Haar-side route to an exceptional-set bound

**What the heuristic route is.** "Upper-bound sieve over the avoider system with
witness moduli `≤ T = exp(c(log N)^{1/4})`" needs (i) a Haar void
`P(no witness ≤ T) ≤ e^{−c𝓛³}` and (ii) a majorant certifying it at level
`≤ log N`. The note does exactly this: (i) is its Lemma 7.1 (fibre product,
the same computation as Prop 1.1 here), (ii) is the Bonferroni majorant
`S_yQ_r(H_X)`, `r ≍ t³`, level `≍ t⁴` (note Thm 8.2). So:

**Proposition 3.1 (PROVED; consequence of Theorem 2.1 at
`T = exp(c₁(log N)^{1/4})`).** `E_pr(N) ≤ #{p ≤ N: W(p) > T} ≪ π(N)·exp(−c(log N)^{3/4})`.
This is the prime part of the note's Theorem 1.1 with `π(N)` in place of
`N`; at this scale the two are the same statement (the factor
`N/π(N) ≍ log N = e^{log log N}` is absorbed by `c`). It is a reproof, **not** an improvement, and the
"Haar-side route" is not a new route: it *is* the note's route.

*Assessment 3.2 (the other Haar family).* POINTWISE_HAAR's Janson family
(squarefree `𝓛⁵`-rough moduli, several large primes per modulus) would give
a different route only if its factorial moments `E(H)_m ≤ (Cμ)^m` held for
`m ≍ μ`. Overlapping moduli make this a correlation problem the note avoids
(its moment proof uses one large prime per atom, note Thm 6.3). It cannot
beat the note: by KARY3 Thm 4.1 any majorant of any forced-class family
saves `≤ Cλ^{3/4}`, and on the Haar side the void `≍ 𝓛³` holds up to
`(log𝓛)^5` (Prop 1.1, OMEGA13 Thm 3.4). Not pursued.

**Corollary 3.3 (a cubic integer-CRT saving costs level `𝓛⁴`; PROVED from
KARY3 Thm 4.1).** Let `𝔊_T` be the ℛ(M)-classes with `M ≤ T`
together with the selector classes `0 mod p`, `p ≤ y`. Every CRT majorant
`ν ≥ 1_{𝒜(𝔊_T)}` of level `λ ≥ λ₀` (all term moduli `≤ e^λ`) with
`log(1/Eν) ≥ s` has `λ ≥ (s/C)^{4/3}`. In particular an integer-CRT saving
`c𝓛³` (with selectors) needs level `≥ c'𝓛⁴`, and the note's `ν_X` attains
such a saving at level `≤ C''𝓛⁴` (ledger of note Thm 8.2). So for savings of
the cubic order the majorant-side critical level is `≍ 𝓛⁴`. (This is *not*
a statement that the full unit-Haar void `δ*(T)` is certified: its exponent
is known only between `c𝓛³` and `C𝓛³(log𝓛)^5`.)

*Proof.* KARY3 Thm 4.1 gives `s ≤ log(1/Eν) ≤ Cλ^{3/4}`. ∎

(The selector classes are needed only to make the void small on `Ẑ`; without
them `n ≡ 0 mod P_z` keeps the integer-CRT void `≥ e^{−O(z)}`.)

## 4. The common sieve limit (goal (c))

### 4.1 The abstract statement

**Setting 4.0** (= POINTWISE_OMEGA14 Setting 1.2). Independent coordinates:
small `X_s`, big `(X_b)_{b∈𝔅}`, each big `b` of cost `c_b ≥ L`. A family 𝓕
of events, each `{X_s ∈ Σ_E} ∩ {X_{b(E)} ∈ Γ_E}` with exactly one big
coordinate. Given `x_s`: `Ω_b(x_s)`, `p_b(x_s) = P(X_b ∈ Ω_b)`, assume
`p_b ≤ p* ≤ 1/4`; `P(x_s) = Σ_b p_b`, `R(x_s) = Σ_b p_b/(1−p_b)`
(`P ≤ R ≤ 4P/3`); `H = Σ_b 1[X_b ∈ Ω_b(x_s)]`; `F = 1[H = 0]`.
`𝒱_k` = span of functions of `X_s` and at most `k` big coordinates. A
function of level `λ` (cost `≤ λ`) lies in `𝒱_k`, `k = ⌊λ/L⌋`. `E_s` =
conditional expectation given `x_s`.

**Theorem 4.1 (two-sided order-k sieve limit; PROVED, from cited lemmas).**
Fix `x_s`, write `P = P(x_s)`.
* (U−) *Upper limit.* For `k ≥ 1`, every `G ∈ 𝒱_k` with `G ≥ F` has
  `log(1/E_s G) ≤ k·log(C₀(P+4k)/k) + (4/3)k + ½log(22k+22) + 3`.
  In particular a saving `log(1/E_s G) ≥ P/2` forces `k ≥ c₀P` (absolute `c₀ > 0`).
* (U+) *Upper achievability.* For even `k ≥ e²P`, `G = Q_k(H) ∈ 𝒱_k`,
  `G ≥ F`, `E_s G ≤ e^{−P} + e^{−(k+1)} ≤ 2e^{−P}`.
* (L−) *Lower limit.* Every `B ∈ 𝒱_k` with `B ≤ F` has `E_s B ≤ 0` once
  `P ≥ (5/3)(k+1)`, i.e. whenever `k ≤ 0.6P − 1`.
* (L+) *Lower achievability.* For odd `k ≥ e²P`, `B = Q_k(H) ∈ 𝒱_k`, `B ≤ F`,
  `E_s B ≥ e^{−(4/3)P} − e^{−(k+1)} > 0`.

So the critical *order* is `k* ≍ P` **for both one-sided problems**. If in
addition the big costs are comparable (`L ≤ c_b ≤ AL`) and the small
coordinates read by the certificate are booked separately (cost `λ_s`), the
critical *level* is `λ* ≍_A L·P + λ_s`: "dimension times log-size". (Without
comparable costs only the lower bound `λ ≥ L·k` on the level is valid.) This is the
large-dimension sieve limit (`β_κ ≍ κ`) in the one-big-coordinate setting.

*Proof.* (U−): given `x_s`, the big coordinates with unary patterns
`X_b ∈ Ω_b` form EXCEPTIONAL_KARY's §1 setting with every coordinate light
(`p_b ≤ 1/4 = δ`); the sequential process replaces every hit coordinate, so
its output `y` always lies in the avoider set and `G(y) ≥ 1`; `G` is k-local.
KARY Thm 2.5 gives `E_s G ≥ E e^{−Φ} ≥ e^{−EΦ}`, and KARY Cor 2.6 with
`M = m̄ = P` (deterministic here) bounds `EΦ`. For the consequence, at
`k = εP` the right side is `≤ εP(log(C₀(1+4ε)/ε) + 4/3) + O(log P) < P/2` for
`ε ≤ c₀`, `P ≥ P₀`. (U+), (L+): `Q_k(h) = Σ_{j≤k}(−1)^j C(h,j)` equals 1 at
`h = 0` and `(−1)^k C(h−1,k)` for `h ≥ 1`, with `|C(h−1,k)| ≤ C(h,k+1)` (note
Lemma 8.1); `C(H,j)` is a sum of products of `j` indicators of distinct big
coordinates, so `Q_k(H) ∈ 𝒱_k`; `E_s C(H,k+1) = e_{k+1}(p) ≤ (eP/(k+1))^{k+1}
≤ e^{−(k+1)}`; and `E_s F = ∏(1−p_b) ∈ [e^{−(4/3)P}, e^{−P}]`. (L−): OMEGA14
Thm 1.3 (fibrewise form, which is how it is proved): planting applies when
`R ≥ (k+1)+(2k+1)r*`, `r* ≤ 1/3`, which follows from `R ≥ P ≥ (5/3)(k+1)`. ∎

*Novelty: none claimed for Thm 4.1 itself.* (U−) is KARY's binomial
extrapolation (its core is Peled–Yadin–Yehudayoff / Benjamini–Gurel-Gurevich–Peled,
`reviews/novelty-audit-2026-10.md`); (L−) is OMEGA14's planting (LP dual of
lower-bound sieves); (U+),(L+) are Bonferroni. The point is that the *same*
statement, at the *same* scale, with the *same* mass function, drives both
ceilings (§4.2).

### 4.2 The two ES instances are the same instance

Both ceilings use Setting 4.0 with **one big prime per event**, big cost
`L ≍ 𝓛`, and big mass `P ≍ 𝓛³` (up to `log𝓛`):

| | note / KARY (majorants) | OMEGA13/14 (minorants) |
|---|---|---|
| small coordinates | `n mod L_K P_y` (`c`, selector) | `n mod` primes `≤ T^{0.6}` |
| big coordinates | `n mod ℓ`, `ℓ ∈ (X^{1/2}, X]`, cost `≥ t/2` | `n mod ℓ`, `ℓ > T^{0.6}`, cost `≥ 0.6𝓛` |
| big mass `P(x_s)` | `μ_c ≍ t³` for unit `c` (note Cor 4.3) | `μ ≫ 𝓛³/log𝓛` (OMEGA14 Lemma 2.2), concentrated (Lemma 2.3) |
| certificate used | (U+) with `k = r ≍ t³` (note Thm 8.2) | (L+)-type, level `𝓛·S_res ≍ 𝓛⁴log𝓛` (OMEGA13 §5, BRW not Bonferroni) |
| barrier | (U−), summed over scales (KARY3 Thm 4.1) | (L−) + concentration (OMEGA14 Thm 2.4/4.5) |
| level budget `λ` | `≤ (A+1)log N` (KARY3 Cor 4.2 projection) | `≤ c log x` (Gallagher transfer, OMEGA14 Cor 4.6) |

*Multi-scale form of (U−) (Assessment: a reading of KARY3's ledger, not a
new proof).* KARY3 Thm 4.1's ledger is (U−) applied to the dyadic scale
blocks `s = 2^i λ^{1/4}` with order `k_s = ⌊λ/s⌋` and block mass `≤ 8K₃′s³`,
each costing `≤ (λ/s)(c₁ + i log 16)`, plus the full mass `≍ λ^{3/4}` of the
scales below `λ^{1/4}`. In words,
```
S(λ) ≍ Σ_{dyadic s} min( μ(s), (λ/s)(1 + log⁺(μ(s)s/λ)) ),   μ(s) ≍ s³,
```
which is dominated by `s ≍ λ^{1/4}`, where `μ(s) = λ/s`, i.e. `λ = s·μ(s)`.
(KARY's sequential coupling is what lets multi-prime events and several
scales be handled at once; the arithmetic per block is (U−).)

**Proposition 4.2 (the note's atoms block every low-level minorant; PROVED
given note Cor 4.3 (INTERNALLY PROVED; inputs BV and Brun–Titchmarsh) and
OMEGA14 Lemma 1.1/Thm 1.3 (PROVED, elementary)).** There are absolute
`c, T_0 > 0` such that for `T ≥ T_0`, every modulus `Q` with `log Q ≤ T^{0.05}`
and every unit class `r mod Q`: if `B` is a function on the fibre
`{n ∈ Ẑ^× : n ≡ r (Q)}` of level `≤ D` (OMEGA14 Setting 2.0: a combination of
functions of `n mod qQ`, `q ≤ D`), `B ≤ F_T` pointwise (`F_T` = no ES event
of modulus `≤ T`), and `log D ≤ c(log T)⁴`, then `E_fibre B ≤ 0`.

This sharpens OMEGA14 Thm 4.5 (`log D ≤ c𝓛⁴/log𝓛`, modulo (G), the effective
Page bound and the fundamental lemma) by removing the `log𝓛` and those three
inputs. Consequently, in OMEGA14 Cor 4.6 the optimality of OMEGA13 Thm 5.1
holds up to a factor `(log log p)^{1/4}` in `𝓛` (it was `(log log p)^{1/2}`).
*(Suggested by the self-review of this file.)*

*Proof.* Let `X = T^{1/(1+κ)}`, `t = log X`. Big coordinates: `X_ℓ = n mod ℓ`
for the primes `ℓ ∈ (X^{1/2}, X]` with `ℓ ∤ Q`; small: all other coordinates
(the fibre fixes some of them). On the fibre the big coordinates are
independent and uniform on units. A function of `n mod qQ`, `q ≤ D`, reads only
big `ℓ | q`, fewer than `2 log D/t` of them, so it lies in `𝒱_k`,
`k = ⌊2 log D/t⌋`. Family 𝓕: the note's atoms (ES events of modulus
`kℓ ≤ KX ≤ T`) with `ℓ ∤ Q`; each reads `c = n mod L_K` (small) and one big
`X_ℓ`. Given any small configuration, `c` is a unit, and the active atoms at
`ℓ` give `f_c(ℓ)` distinct unit classes (note Lemma 2.2), with
`f_c(ℓ) ≤ z_j² ≤ ℓ^{1/3}`, so `p_ℓ = f_c(ℓ)/(ℓ−1) ≤ 2X^{−1/3} =: p*`. By note
Cor 4.3 (uniform in `c`) and Lemma 3.2, `Σ_ℓ f_c(ℓ)/ℓ ≥ a t³` with an
absolute `a > 0`. At most `2 log Q/t` big primes divide `Q`, each of them
carrying `≤ p*`, so `R ≥ P ≥ a t³ − 4 log Q·X^{−1/3}/t ≥ a t³/2` for `T ≥ T_0`.
This holds for *every* small configuration, so OMEGA14 Lemma 4.1 (Thm 1.3
with an empty exceptional set) gives `E B ≤ 0` whenever
`(k+1)+(2k+1)r* ≤ (5/3)(k+1) ≤ a t³/2`. That holds if `log D ≤ c t⁴` with
`c` small, and `t ≍ 𝓛`. `B ≤ F_T ≤ F_𝓕` because 𝓕 consists of ES events of
modulus `≤ T`. ∎

### 4.3 The unified sieve-limit statement

Put `κ(𝓛) := log(1/δ*(e^𝓛))` (the Haar avoider exponent; `c𝓛³ ≤ κ(𝓛) ≤
C𝓛³(log𝓛)^5` by Prop 1.1 and OMEGA13 Thm 3.4) and `λ*(𝓛) := 𝓛·κ(𝓛)`
(dimension × log-size). For a level `λ` let `𝓛_c(λ) := sup{𝓛 : λ*(𝓛) ≤ λ}`
(generalised inverse), so `𝓛_c(λ) = λ^{1/4}` up to `(log λ)^{O(1)}`.

**Theorem 4.3 (the ES sieve limit; PROVED as the conjunction of the cited
results, each with its own status and scope).** Up to constants and, where
marked, factors `(log λ)^{O(1)}`:
1. *(majorants)* `S(λ) := sup` over forced-class mixtures and level-`λ` CRT
   majorants of the saving satisfies `cλ^{3/4} ≤ S(λ) ≤ Cλ^{3/4}`: the upper
   bound for *every* mixture by KARY3 Thm 4.1 (PROVED, internal), the lower
   bound for *one* mixture (the note's atoms and selectors, `ν_X` at
   `t ≍ λ^{1/4}`; INTERNALLY PROVED). Integer-CRT savings of cubic order at
   cutoff `T` cost level `≍ 𝓛⁴` (Cor 3.3).
2. *(minorants)* on every fibre with `log Q ≤ T^{0.05}`, no positive minorant
   of `F_T` has level `log D ≤ c𝓛⁴` (Prop 4.2); on OMEGA13's constructed good
   fibre a positive minorant of level `log D ≤ C𝓛⁴log𝓛` exists (OMEGA13 §5,
   PROVED modulo the inputs listed in (H)26). So the least positive-minorant
   level is `≍ 𝓛⁴` up to one `log𝓛`.
3. *(the ceilings)* With budget `λ ≍ log N` (coefficient-sum rounding) resp.
   `λ ≍ log x` (O9-type prime transfer), item 1 gives the exceptional ceiling
   `S(λ) ≍ λ^{3/4}`, and item 2 gives the pointwise ceiling
   `𝓛 ≲ λ^{1/4}` (achieved up to `(log λ)^{1/4}`). Both are the single relation
   `λ ≍ 𝓛·𝓛³` between level and usable cutoff, read once for the saving `𝓛³`
   and once for the cutoff `𝓛`; the product of the two exponents' quantities
   is `λ` by construction (an identity, not an extra theorem).

*Status of item 3.* "Ceiling" means the cap for the respective
architectures exactly as scoped in (D)24/(D)27 (coefficient-sum CRT methods,
large sieves of the listed kinds) and (H)27/(H)28 (Haar-minorant transfers
requiring `log x ≫ log Z`, orbit-uniform linear certificates). Within those
scopes item 3 is a PROVED consequence of items 1–2; outside them it is an
Assessment. *Mechanism (Assessment).* In both cases the relevant structure
is a one-big-prime subfamily of mass `P ≍ 𝓛³` at big cost `≍ 𝓛` (§4.2), and
the cut-off order is `k ≍ P` (Thm 4.1). The full ES system is not a
one-big-coordinate system: on the minorant side the subfamily is used only
for the obstruction (a Bonferroni minorant of the subfamily does not minorise
full avoidance), and OMEGA13's positive minorant is built differently (BRW).
The extrapolation "Haar exponent `a` ⇒ exponents `a/(a+1)`, `1/(a+1)`" is
CONDITIONAL on the same mechanism (one-big-prime mass `≍ 𝓛^a`, uniform in the
small coordinates); the Haar exponent alone does not imply it.

*Remark 4.4 (why the two sides are not the same inequality).* (U−) and (L−)
are dual LP statements of opposite sign: (U−) produces a measure on the
avoider set that is within `e^{O(k log(P/k))}` of the true law on non-negative
order-k tests (KARY / LARGESIEVE2 Lemma 1.1 "comparison measure"); (L−)
produces a measure on the *hit* set that equals the true law on all order-k
tests (OMEGA14 planting). Together: for `𝓛 ≫ λ^{1/4}` (up to logs), level-`λ`
information cannot tell the true law apart from a law living on `{F_T = 0}`,
nor (up to `e^{Cλ^{3/4}}`) from one living on `{F_T = 1}`. Neither direction
implies the other in general; what they share is the threshold `k ≍ P`.

### 4.4 Toy LP (EVIDENCE)

`scripts/unify_toy_lp.py` (exact rational LP with asserted exact primal certificates; output
`data/unify_toy_lp.txt`; optimality is the solver's, independently
re-checked at the threshold cases by exact dual distributions in the self-review):
`n = 40` i.i.d. bits, mass `P = np`; optimal symmetric order-`k` majorant
and minorant of `F = 1[no bit]` (symmetrisation loses nothing, KARY Lemma 2.3).

| `P` | `log(1/E F)` | least `k` with minorant `E B > 0` | least `k` with majorant saving `≥ 90%` |
|---|---|---|---|
| 2 | 2.05 | 3 | 6 |
| 4 | 4.21 | 7 | 8 |
| 6 | 6.50 | 11 | 12 |
| 8 | 8.93 | 15 | 14 |

Both thresholds are `≈ 2P ± 2`: the same order for both one-sided
problems, as Theorem 4.1 asserts (its constants `0.6` and `e²` are not
sharp). Below threshold the majorant still saves a positive amount growing
roughly linearly in `k` (cf. (U−)), while the minorant is identically useless (cf. (L−)): the asymmetry that
makes the exceptional side degrade gracefully (saving `λ^{3/4}` from any level)
and the pointwise side fail sharply (no positive minorant below `λ*`).

## 5. Section for the campaign summary

**One sieve limit behind both ceilings (CEILINGS_UNIFIED.md).** The
exceptional-set exponent 3/4 and the pointwise exponent 1/4 come from one
mechanism. The ES witness system truncated at moduli `≤ T` contains a
one-big-prime subfamily (big prime of log-size `≍ log T`) whose mass is
`≍ (log T)³` uniformly in the small coordinates: a sieve of dimension
`κ ≍ (log T)³`, matching the Haar exponent. For such a system, order-`k`
certificates are trivial below `k ≍ κ` on *both* sides: majorants save
`≲ k log(κ/k)`, minorants have mean `≤ 0` (Thm 4.1, PROVED; ingredients
known: binomial extrapolation, planting, Bonferroni). So the level needed
is `≍ κ·log T ≍ (log T)⁴`.
* A level `λ ≍ log N` exploits moduli up to `log T ≍ λ^{1/4}` and saves
  `≍ λ^{3/4}`: the 3/4 note, sharp by KARY3.
* A prime transfer up to `x` allows `λ ≍ log x`. It therefore certifies
  `W(p) > T` only for `log T ≲ (log x)^{1/4}`: OMEGA13, sharp by OMEGA14 and
  Prop 4.2.

Thm 4.3 is PROVED as a conjunction of cited results, within their scopes.
Outside those scopes it is an Assessment. The extrapolation to a general
mass exponent `a` (`a/(a+1)`, `1/(a+1)`) is CONDITIONAL on the same mechanism.

By-products, all PROVED given the INTERNALLY PROVED 3/4 note:
* **`log(1/δ*(T)) ≫ (log T)³`** with no `log log T` loss (Prop 1.1): the
  note's void lemma is a Haar bound. With OMEGA13,
  `𝓛³ ≪ log(1/δ*) ≪ 𝓛³(log𝓛)^5`.
* **Witness-modulus tail relative to π(x):**
  `#{p ≤ x : W(p) > T} ≪ π(x)e^{−c(log T)³}` uniformly for
  `log T ≤ c₁(log x)^{1/4}` (Thm 2.1, also using the classical uniform PNT
  in progressions with a Landau–Page exceptional term). This upgrades
  ledger (A)9 from CLAIMED/PROVISIONAL and fixes its normalisation.
* **No positive minorant below level `c(log T)⁴`** on any fibre with
  `log Q ≤ T^{0.05}` (Prop 4.2). This sharpens OMEGA14 Thm 4.5 (which has a
  `/log log T` loss and needs (G), Page and the fundamental lemma). So
  OMEGA13's exponent `(log p)^{1/4}(log log p)^{−1/4}` is optimal within the
  minorant-transfer architecture up to `(log log p)^{1/4}` in `log W`.
* The "Haar-side route" to the 3/4 bound is the note's own route (§3). It
  reproves the 3/4 bound for primes and does not improve it.

**Proposed ledger changes (for the parent).**
* (A)9: relabel "INTERNALLY PROVED (via the 3/4 note, (B)11); see
  CEILINGS_UNIFIED Thm 2.1 for the `π(x)` form".
* (H)25/(H)26: lower bound `𝓛³/log𝓛` → `𝓛³` (CEILINGS_UNIFIED Prop 1.1).
* (H)27: Thm 4.5's `c𝓛⁴/log𝓛` → `c𝓛⁴`, inputs reduced to the note's BV
  (CEILINGS_UNIFIED Prop 4.2); Cor 4.6's gap `(log log p)^{1/2}` → `(log log p)^{1/4}`.
* New cross-entry: Thm 4.1 / Thm 4.3 as above.

**Open / not done.**
* A *lower* typical-size bound `#{p ≤ x: W(p) > T} ≥ π(x)e^{−C𝓛³polylog}`
  for `log T ≤ c(log x)^{1/4}/polylog`. This would make the tail law
  two-sided in the whole sieve range.
  * OMEGA13's transfer gives existence.
  * A count would follow from OMEGA9 Thm 1.1's main term, except in its
    Case A (exceptional character with conductor dividing the quarantine
    modulus): there the factor `λ = 1 − x^{β₁−1}/β₁` can be as small as
    `Z^{−1/2}`.
  * Not attempted (Assessment).
* Heuristic truth (Assessment): `#{p ≤ x: W(p) > T} = π(x)e^{−𝓛^{3+o(1)}}`
  up to `𝓛 ≈ (log x)^{1/3}`. Both ceilings sit at `(log x)^{1/4}` because
  that is where `λ*(𝓛) = log x`, not because the distribution changes there.
* Within the scoped architectures above, neither ceiling can be beaten.
  Methods outside them remain possible (Assessment). Examples:
  * tuple counts or hybrid large-class accounting, (D)21–(D)26;
  * Type II or support-aware prime input, (H)28;
  * prime transfers not requiring `log x ≫ log Z`.

  No implication from an improvement on one side to the other is known.

## Replay

```
PYTHONPATH=scripts uv run python scripts/unify_toy_lp.py   # §4.4, ~10 min, exact LP
```
Everything else in this file is a written proof with pointers.
