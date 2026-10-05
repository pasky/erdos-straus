# The Haar avoider exponent (task O46)

Branch `side-agent/haar-exponent`. Labels follow the house rules. ES is not
solved here or anywhere; everything below is about the profinite (Haar)
avoider density `δ*(T)` of the multiplier frame, i.e. a pure probability
problem on `∏_ℓ ℤ_ℓ`. Nothing here is a statement about primes unless
explicitly said (§5).

Notation. `𝓛 := log T`, `Φ(T) := log(1/δ*(T))`. The target exponent `a` is
defined by `Φ(T) = 𝓛^{a+o(1)}` (if it exists). Before this note:
`𝓛² ≪ Φ ≪ 𝓛^6` (lower: OMEGA8 Prop 6.6, single-prime events, modulo the
standard shifted-prime divisor bound (D'); upper: OMEGA11 Cor 3.3 modulo ET
Prop 1.4; OMEGA12 claims `𝓛^5 log𝓛`). Numerics: local exponent 2.26→2.58
(POINTWISE_SIZE §7.2).

**Results of this note (checkpoint 1).** (i) A Janson-type inequality for
atomic events on product spaces under a lopsided local lemma (Thm 1.4) —
needed because Harris fails for one-hot variables. (ii) **`log(1/δ*(T)) ≫
𝓛³/log𝓛`** (Thm 2.1, PROVED modulo the sieve fundamental lemma), improving
the lower bound `𝓛²`; so `a ≥ 3`. (iii) Negative-association arguments alone
cannot pass `𝓛²` (Prop 1.5). (iv) The Monte Carlo data fit `𝓛³/log𝓛` with a
constant ratio 0.069–0.070, explaining the measured exponent 2.3–2.6 as
`3 − 1/log𝓛` (§3, EVIDENCE). Conjecture: `a = 3`.

## 0. The event system

Haar measure on `Ẑ`, restricted to the class `n ≡ 1 (24)`. For each
`M ≤ T`, `M ≡ 3 (4)`, `A_M := (M+1)/4`, and each `D | A_M²`, the **event**
`E_{M,D} := {n ≡ −4D (mod M)}`. `δ*(T)` = Haar measure (normalised in
`1 (24)`) of the set where no event occurs. Distinct pairs `(M, −4D mod M)`
are distinct events; repeated ones are counted once.

For an odd prime ℓ the **coordinate** is `X_ℓ := n mod ℓ^{f}` (f large);
the coordinates are independent and uniform on units (and on the fibre
`X_3 ≡ 1 (3)` at ℓ=3). Since `ℓ | M ⇒ ℓ ∤ A_M ⇒ ℓ ∤ D`, every event is an
**atomic event** (a partial assignment): `E_{M,D} = ⋂_{ℓ|M} {X_ℓ ≡ −4D (mod ℓ^{v_ℓ(M)})}`.
For squarefree M only `X_ℓ mod ℓ` matters, and `P(E_{M,D}) = 1/φ(M)`.

Two atomic events **share a bit** if they share a coordinate on which they
prescribe compatible residues and they are compatible on all shared
coordinates (then `P(E∩E') = P(E)P(E')/P(shared part) > 0`); they
**conflict** if on some shared coordinate the prescribed residues are
incompatible (then `E∩E' = ∅`).

## 1. General tools for atomic events on product spaces (PROVED)

Throughout §1: `(X_v)` independent random variables with arbitrary finite
(or countable) ranges; atomic events `E = {X_v ∈ a_{E,v} for v ∈ S_E}` where
each `a_{E,v}` is a single value (or, for prime powers, a residue class —
the arguments below only use that the restriction of E to `S_E∖S` is again
atomic and that `E` factorises over coordinates). For a family `𝓕` write
`Av(𝓕) := ⋂_{E∈𝓕} Ē`.

**Lemma 1.1 (compatible events; PROVED).** Let A be atomic and let 𝓒 be a
family of atomic events none of which conflicts with A. Then
`P(A ∩ Av(𝓒)) ≤ P(A)·P(Av(𝓒))`.

*Proof.* Condition on A, i.e. fix `X_v = a_{A,v}` for `v∈S_A`. For `C∈𝓒`,
`C∩A = A∩C'` where `C'` is the atomic event C with the coordinates in
`S_A` deleted (they agree with A, as C does not conflict with A); `C'` is
independent of `(X_v)_{v∈S_A}` and `C' ⊇ C`. Hence
`P(Av(𝓒) | A) = P(⋂ C̄') ≤ P(⋂ C̄) = P(Av(𝓒))`. ∎

**Lemma 1.2 (negative association; PROVED, classical input).** Let `𝓕_1, …, 𝓕_r`
be families of atomic events such that no event of `𝓕_i` shares a bit with
an event of `𝓕_j` (`i≠j`). Then `P(⋂_i Av(𝓕_i)) ≤ ∏_i P(Av(𝓕_i))`.

*Proof.* Encode each `X_v` by its one-hot indicator vector `(1[X_v=a])_a`.
A one-hot vector of a single random variable is negatively associated
(Joag-Dev–Proschan 1983, multinomial with one trial), and independent unions
of NA families are NA. An atomic event is a nondecreasing function of the
indicators `1[X_v=a_{E,v}]`, `v∈S_E` (its *bits*); `Av(𝓕_i)` is a
nonincreasing function of the bits of `𝓕_i`, and by hypothesis the bit sets
of different `𝓕_i` are disjoint. NA gives `E∏f_i ≤ ∏Ef_i` for nonnegative
nonincreasing `f_i` on disjoint index sets. ∎

(For residue classes mod `ℓ^v` with different v the "bits" are the
indicators of residues mod `ℓ^{f}`; an event uses the bits of its class.
Two events share a bit iff their classes intersect, i.e. iff they are
compatible at ℓ.)

**Lemma 1.3 (lopsided local lemma and its inflation bound; PROVED, standard).**
Let 𝓕 be a family of atomic events, `Γ(E) := {E'∈𝓕: E' conflicts with E}`,
and suppose there are `x_E∈(0,1)` with `P(E) ≤ x_E∏_{E'∈Γ(E)}(1−x_{E'})`.
Then for every atomic event A (in 𝓕 or not) and every `𝓢 ⊂ 𝓕`,

```
P(A | Av(𝓢)) ≤ P(A) · ∏_{E'∈𝓢, E' conflicts with A} (1−x_{E'})^{−1}.
```

*Proof.* The lopsided local lemma (Erdős–Spencer 1991) holds with the
lopsidependency graph Γ, because `P(E | Av(𝓢')) ≤ P(E)` whenever no event
of `𝓢'` conflicts with E (Lemma 1.1). Its proof gives, by induction on
`|𝓢|`, `P(E | Av(𝓢)) ≤ x_E` for `E∈𝓕∖𝓢`. For A, split `𝓢 = 𝓢_1 ∪ 𝓢_2`
with `𝓢_1` the events conflicting with A. Then
`P(A | Av(𝓢)) ≤ P(A | Av(𝓢_2)) / P(Av(𝓢_1) | Av(𝓢_2))`; the numerator is
`≤ P(A)` by Lemma 1.1, and the denominator is
`∏_{E∈𝓢_1}(1 − P(E | Av(earlier ∪ 𝓢_2))) ≥ ∏_{E∈𝓢_1}(1−x_E)`. ∎

**Theorem 1.4 (Janson-type lower bound for atomic events; PROVED).** Under
the hypothesis of Lemma 1.3, put `K := max_{E∈𝓕} ∏_{E'∈Γ(E)}(1−x_{E'})^{−1}`,
`μ := Σ_{E∈𝓕} P(E)` and `Δ := Σ_{{E,E'}: E≠E' share a bit} P(E∩E')`. Then

```
−log P(Av(𝓕)) ≥ μ − KΔ,      and      −log P(Av(𝓕)) ≥ min(μ/2, μ²/(4KΔ)).
```

*Proof.* Order `𝓕 = {E_1,…,E_N}`, `B_i := Av({E_j: j<i})`, so
`P(Av(𝓕)) = ∏_i(1−P(E_i|B_i))` and `−log P(Av) ≥ Σ_i P(E_i | B_i)`. Let
`B_i^d := Av({E_j: j<i, S_j∩S_i=∅})`; then `B_i ⊂ B_i^d`, so
`P(E_i|B_i) ≥ P(E_i)P(B_i|E_i)/P(B_i^d)`. Conditioning on `E_i`, events
`E_j` (`j<i`) conflicting with `E_i` are impossible, those sharing a bit
become `E_j'` (coordinates of `S_i` deleted; `P(E_i)P(E_j')=P(E_i∩E_j)`),
and `B_i^d` is independent of `E_i`. Hence

```
P(B_i | E_i) ≥ P(B_i^d) − Σ_{j<i, j shares a bit with i} P(E_j' ∩ B_i^d).
```

`B_i^d` is the avoidance of a subfamily of 𝓕, and every event conflicting
with `E_j'` conflicts with `E_j`; so Lemma 1.3 gives
`P(E_j' | B_i^d) ≤ K P(E_j')`. Therefore
`P(E_i|B_i) ≥ P(E_i) − K Σ_{j<i, j~i} P(E_i∩E_j)`, and summing over i gives
the first bound (if the right side is negative the inequality
`P(E_i|B_i) ≥ ` it is trivial). For the second: a subfamily
`𝓕' ⊂ 𝓕` satisfies the hypothesis with the same `x_E` (Γ shrinks) and
`P(Av(𝓕)) ≤ P(Av(𝓕'))`. Taking `𝓕'` random with inclusion probability
p, `E μ' = pμ`, `E Δ' = p²Δ`, so some `𝓕'` has `μ'−KΔ' ≥ pμ − p²KΔ`; take
`p = min(1, μ/(2KΔ))`. ∎

*Remarks.* (i) Δ only counts bit-sharing (compatible) pairs; conflicting
pairs, which carry all the "one coordinate, many residues" structure, cost
nothing except through K. (ii) Without some local-lemma control the
statement is false in spirit: Harris' inequality fails for one-hot
variables (`P(X=r | X≠r') > P(X=r)`), which is why Lemma 1.3 is needed for
`P(E_j'|B_i^d)`. (iii) With `x_E = 2P(E)`, `P(E) ≤ 1/8` and
`Σ_{E'∈Γ(E)} P(E') ≤ 1/8` the hypothesis holds and `K ≤ e^{1/3}`.

**Proposition 1.5 (the packing barrier: NA alone stops at `𝓛²`; PROVED).**
Lemma 1.2 bounds `δ* ≤ ∏_{E∈𝓕}(1−P(E))` for every family 𝓕 of pairwise
bit-disjoint events. For every such family of squarefree-modulus ES events,
`Σ_{E∈𝓕, ω(M_E)≥2} P(E) ≤ Σ_{3≤q≤T} 2/(q−1) ≪ log 𝓛`.

*Proof.* Charge each multi-prime event to its least prime q. Bit-disjoint
events through q prescribe pairwise distinct residues mod q, so at most
`q−1` of them, and each has `P(E) = 1/φ(M) ≤ 1/((q−1)·q')` with `q'>q`
another prime of M, so `≤ 2/(q−1)²` for q≥3. Summing: `≤ Σ_q 2/(q−1)`. ∎

So the single-prime bound `Φ ≫ 𝓛²` of OMEGA8 Prop 6.6 is the limit of
"independent/negatively correlated subfamily" arguments; going beyond it
needs the positive-correlation bookkeeping of Theorem 1.4.

## 2. Lower bound: `Φ(T) ≫ 𝓛³/log𝓛` (PROVED modulo the sieve fundamental lemma)

**Theorem 2.1.** There are absolute constants `c>0`, `T_0` such that for
`T ≥ T_0`

```
log(1/δ*(T)) ≥ c·𝓛³/log𝓛.
```

So the Haar exponent satisfies `a ≥ 3` (if it exists; in any case
`liminf log Φ/log𝓛 ≥ 3`). The only external input is the fundamental lemma
of sieve theory (e.g. Friedlander–Iwaniec, *Opera de Cribro*, Lemma 6.3 /
Cor. 6.10; Halberstam–Richert Thm 2.5), used for a lower bound on rough
numbers in progressions to small moduli. No Bombieri–Vinogradov or
Elsholtz–Tao input is used.

**The family.** Put `y := 𝓛^5`, `N_0 := 𝓛²`, and write `D* := ∏ p^{⌈v_p(D)/2⌉}`
(so `D | A² ⟺ D* | A`; every integer D is uniquely `D = κt²`, κ squarefree,
and `D* = κt`; for given `n` there are exactly `2^{ω(n)}` integers with
`D* = n`). Let

```
𝓕 := { E_{M,D} :  √T ≤ M ≤ T,  M squarefree, all prime factors of M > y,
                  M ≡ 3 (4),  n := D* ∈ [N_0, T^{1/10}],  n | A_M }.
```

Facts used repeatedly:
* (F1) `D ≤ n² ≤ T^{1/5} < M/4`, so different D give different residues
  `−4D mod M`: the listed events are distinct, and
  `P(E_{M,D}) = 1/φ(M)`.
* (F2) for y-rough squarefree `m ≤ T`, `ω(m) ≤ 𝓛/log y` and
  `φ(m) ≥ m(1−𝓛/(y log y)) ≥ m/2`.
* (F3) `Σ_{n≤x}2^{ω(n)}/n ≤ (1+log x)²`, `Σ_{n≤x}2^{ω(n)} ≤ x(1+log x)`,
  `Σ_{n>x}2^{ω(n)}/n² ≪ (1+log x)/x`.
* (F4) for an AP `v ≡ c (mod d)` in `[v_0, V]` with least element `v_1 ≥ v_0`:
  `Σ 1/v ≤ 1/v_1 + log(V/v_0)/d`.
* (F5) for `m ≥ 1` and `0<α≤1` with `ω(m)y^{−α} ≤ 1`:
  `Σ_{g|m, g>1, g y-rough squarefree} g^{−α} ≤ (1+y^{−α})^{ω(m)}−1 ≤ 2ω(m)y^{−α}`.

**Lemma 2.2 (the mass; PROVED mod fundamental lemma).** `μ := Σ_{E∈𝓕}P(E) ≥ c_1𝓛³/log y`.

*Proof.* By (F1), `μ ≥ Σ_{N_0≤n≤T^{1/10}} 2^{ω(n)} Σ_{M} 1/M`, M over
y-rough squarefree `M∈[√T,T]` with `M ≡ −1 (mod 4n)` (this implies
`M≡3 (4)` and `n | A_M`; primes dividing 2n never divide M). For a dyadic
block `(X,2X] ⊂ [√T,T]`, sift the progression (length `X/(4n) ≥ X^{4/5}/4`)
by the primes `p<y`, `p∤2n`, with sifting level `X^{1/2}` and
`s = log X/(2log y) ≥ 𝓛/(20 log𝓛) → ∞`: the fundamental lemma gives at
least `(X/4n)∏_{p<y}(1−1/p)(1−O(e^{−s})) − O(X^{1/2}) ≥ c_2X/(n log y)`
y-rough elements. Non-squarefree ones (divisible by `p²`, `p≥y`) number
`≤ Σ_{y≤p≤√(2X)}(X/(4np²)+1) ≤ X/(4ny) + √(2X)`, negligible since
`n ≤ X^{1/5}`. So each block contributes `≥ c_2/(4n log y)`, there are
`≥ 𝓛/(2log2) − 1` blocks, and
`Σ_{N_0≤n≤T^{1/10}} 2^{ω(n)}/n ≥ (3/π²−o(1))(𝓛/10)²` (the range `n<N_0`
removes only `O((log𝓛)²)`). ∎

**Lemma 2.3 (local-lemma hypothesis; PROVED).** For `T ≥ T_0` every
`E∈𝓕` has `P(E) ≤ 1/8` and `Σ_{E'∈Γ(E)}P(E') ≤ 1/8`. Hence Theorem 1.4
applies to 𝓕 with `x_E=2P(E)`, `K ≤ e^{1/3}`.

*Proof.* `P(E) ≤ 2/√T`. Let `w_q := Σ_{E'∈𝓕: q|M'}P(E')`; events
conflicting with E share a prime `q | M`, so
`Σ_{Γ(E)}P ≤ Σ_{q|M}w_q ≤ (𝓛/log y)·max_{q>y}w_q`. Writing `M'=qv`,
`qv ≡ −1 (4n')`, `qv ≥ √T`, (F2) and (F4) give
`w_q ≤ (2/q)Σ_{D'}(𝓛/(4n') + min(1,q/√T))`. The first part is
`≤ 𝓛³/(2q)` by (F3); the second is `≤ (2/q)min(1,q/√T)·T^{1/10}(1+𝓛) ≤ 4𝓛T^{−2/5}`.
So `Σ_{Γ(E)}P ≤ (𝓛/log y)(𝓛³/(2y) + 4𝓛T^{−2/5}) = O(1/(𝓛 log𝓛))`. ∎

**Lemma 2.4 (the pair sum; PROVED).** `Δ := Σ_{bit-sharing pairs}P(E∩E') ≤ C𝓛²`.

*Proof.* Let `E=E_{M,D}`, `E'=E_{M',D'}` be distinct and share a bit; put
`g := gcd(M,M') > 1`, `M=gv`, `M'=gv'` (`gcd(v,v')=1`, g is y-rough so
`g>y`). Compatibility on every prime of g means `g | D−D'`. Also
`M ≠ M'` (if `M=M'` then `M | D−D'`, and E = E' by (F1)). By (F2),
`P(E∩E') = 1/(φ(g)φ(v)φ(v')) ≤ 8/(gvv')`. For fixed g and D the admissible
v satisfy `gv ≡ −1 (mod 4n)` and `gv ≥ √T`, so by (F4)

```
σ(g,n) := Σ_v 1/v ≤ 𝓛/(4n) + min(1, g/√T).                         (2.1)
```

*(a) D = D'.* Then `v ≠ v'`, and `v ≡ v' ≡ −g^{−1} (mod 4n)`. Sum over g
first: for fixed `(v,n)`, g runs over a progression mod 4n with `g > y`,
so `Σ_g 1/g ≤ 1/y + 𝓛/(4n)`. Then, ordering `v<v'`,
`Σ_{v<v', v'≡v (4n)} 1/(vv') ≤ Σ_{v≤T}(1/v)(1+𝓛)/(4n) ≤ (1+𝓛)²/(4n)`.
Hence

```
Δ_a ≤ 16 Σ_{n≥N_0} 2^{ω(n)} (1/y + 𝓛/(4n))(1+𝓛)²/(4n) ≪ 𝓛^4/y + 𝓛³ log N_0/N_0 ≪ 𝓛 log𝓛.
```

*(b) D ≠ D'.* Now `g | m := |D−D'|`, `0 < m < T^{1/5}`, so `g < T^{1/5}`
and (2.1) gives `σ(g,n) ≤ 𝓛/(4n) + T^{−3/10}`. Summing over g with (F5)
(`α=1`, `ω(m) ≤ 𝓛`):

```
Δ_b ≤ Σ_{D≠D'} Σ_{g|m} (8/g) (𝓛/(4n) + T^{−3/10})(𝓛/(4n') + T^{−3/10})
    ≤ (2𝓛/y)·[ (𝓛²/2)(Σ_D 1/n)² + 4T^{−3/10}𝓛·#𝓓·Σ_D1/n + 8T^{−3/5}(#𝓓)² ],
```

where 𝓓 is the set of D with `D* ≤ T^{1/10}`: `Σ_D 1/n ≤ 𝓛²`,
`#𝓓 ≤ T^{1/10}(1+𝓛)` by (F3). So `Δ_b ≤ 𝓛^7/y + O(T^{−1/10}𝓛^5) ≪ 𝓛²`. ∎

*Proof of Theorem 2.1.* All events of 𝓕 involve only primes `> y > 3`, so
they are independent of `n mod 24`, and `δ*(T) ≤ P(Av(𝓕))`. Theorem 1.4
with Lemmas 2.2–2.4: `Φ ≥ μ − e^{1/3}Δ ≥ c_1𝓛³/(5log𝓛) − C𝓛² ≫ 𝓛³/log𝓛`. ∎

*Remarks.* (i) The restriction `M ≥ √T ≥ (D*)^5` is what makes the
progression "first terms" in (2.1) harmless; the restriction `D* ≥ 𝓛²`
removes the small-D hubs (`D=1`: residue −4 at every prime), whose same-D
pairs would otherwise make `Δ_a ≍ μ`. (ii) The `log𝓛` loss is the price of
`y`-roughness (`Σ_{M y-rough}1/M ≍ 𝓛/log y`); y must exceed the per-prime
loads `w_q ≈ 𝓛³/q` for the local lemma, and `y ≥ 𝓛^{4+ε}` is needed for
`Δ_b`'s crude count (an averaged count would allow `y ≈ 𝓛^{3+ε}`; the loss
stays `≍ log𝓛`). (iii) The statement is Haar-only; it is a lower bound on
`log(1/δ*)`, i.e. it says the profinite avoider set is *small*.
(iv) Asymptotic only: at `T ≤ 10^7` one has `T^{1/10} < N_0`, so 𝓕 is
empty; no conflict with the measured `Φ(65535) ≈ 38`.

## 3. Reconciliation with the Monte Carlo exponent (EVIDENCE / Assessment)

`scripts/haar_fit.py` (output `data/haar/fit.txt`) takes the
multilevel-splitting table of POINTWISE_SIZE §7.2 unchanged.

| T | 𝓛 | Φ (MC) | `Φ/(𝓛³/log𝓛)` | `I/(𝓛³/log𝓛)` | local exponent of Φ | `3−1/log𝓛` |
|---|---|---|---|---|---|---|
| 127 | 4.84 | 5.47 | 0.0759 | 0.0856 | 2.13 | 2.37 |
| 511 | 6.24 | 9.40 | 0.0709 | 0.0865 | 2.20 | 2.45 |
| 1023 | 6.93 | 12.02 | 0.0699 | 0.0873 | 2.36 | 2.48 |
| 2047 | 7.62 | 15.11 | 0.0693 | 0.0880 | 2.44 | 2.51 |
| 4095 | 8.32 | 18.77 | 0.0691 | 0.0888 | 2.53 | 2.53 |
| 8191 | 9.01 | 23.08 | 0.0694 | 0.0895 | 2.59 | 2.55 |
| 16383 | 9.70 | 27.99 | 0.0696 | 0.0904 | 2.58 | 2.56 |
| 32767 | 10.40 | 33.4 | 0.0696 | 0.0913 | 2.39 | 2.57 |
| 65535 | 11.09 | ~38.5 | 0.0679 | 0.0921 | | 2.58 |

* The ratio `Φ/(𝓛³/log𝓛)` is constant to ±1% (0.0691–0.0699) over
  `1023 ≤ T ≤ 32767`, the range where the MC is reliable (the last row is
  biased low, POINTWISE_SIZE §7.2). The shape of Theorem 2.1 has local
  exponent `3 − 1/log𝓛`, which is 2.48→2.57 here — exactly the measured
  2.3→2.6 drift.
* Least squares on `T ≥ 127`: `Φ = c𝓛^a` gives `a = 2.39` (max log-residual
  0.043); `Φ = c𝓛^a/log𝓛` gives `a = 2.90` (residual 0.028).
* The independence exponent `I(T)` (§7.1(c)) also tracks `𝓛³/log𝓛` with a
  slowly rising ratio, consistent with `I ≍ 𝓛³` (its local exponent 2.8 at
  `2^20`).

**Assessment 3.1.** The measured exponent 2.3–2.6 is not a different
exponent: it is `a = 3` seen through a `1/log𝓛` correction of exactly the
type that Theorem 2.1's proof produces. Conjecture: `Φ(T) ≍ 𝓛³/log𝓛`
(CONJECTURE; the lower bound is Theorem 2.1, the upper bound is open —
best known `𝓛^5 log𝓛`, OMEGA12, and `𝓛^6` OMEGA11). Under the RA heuristic
(POINTWISE_SIZE §7.3) this predicts
`log W(p) ≍ (log p·log log p)^{1/3}` for the record values.

## 4. What this means on the prime side (Assessment unless stated)

* **Haar-only.** Theorem 2.1 is a statement about `δ*(T)` alone. The one
  rigorous link to primes is POINTWISE_SIZE Prop 7.1(a) (fixed T): for every
  fixed `T ≥ T_0`, the proportion of hard primes with `W(p) > T` is
  `δ*(T) ≤ exp(−c𝓛³/log𝓛)` (PROVED, as a fixed-T density statement).
* **Ceiling under RA.** Under the random-avoider heuristic RA, record values
  satisfy `log W ≲ (log p·log log p)^{1/3}`; so the prime-side exponent of
  the Ω-programme cannot exceed 1/3 even heuristically, and the current 1/6
  (OMEGA11) / 1/5 (OMEGA12, under review) are a factor 2 resp. 5/3 away in
  the exponent. (Assessment.)
* **BRW/Thorner–Zaman route (OMEGA8 §6.6 analogue; PROVED bookkeeping).**
  For every minorant `B ≤ F` on a class-of-one fibre, `μ = E B ≤ δ` and
  `log(1/μ) ≥ Φ(T) − log φ(Q) ≥ …`; more simply, on the full Haar space
  `μ/φ(Q) ≤ δ*(T)`. For BRW expansions as written (`M_1 ≥ 1`) this gives
  `K ≥ 1 + log(1/μ)`, and with the quarantine cost
  `log φ(Q) ≤ Φ − log(1/μ)` one of `K`, `log Q` is `≥ Φ/2 ≫ 𝓛³/log𝓛`. Through
  POINTWISE_OMEGA Thm 4.1 (`log p ≳ K·max(log Z,K)`) this caps that route at
  exponent `≤ 1/6+o(1)`; it is not a cap for the O9 linear transfer, whose
  condition does not contain `log(1/μ)`. (No universal statement over all
  representations is claimed, cf. OMEGA8 §6.6, R34a.)
* **Transfer costs.** Any prime-side use of a Haar improvement passes
  through OMEGA9/OMEGA11: the quarantine `log Q` and the junta modulus. The
  lower bound shows `log Q + log(1/μ) ≥ Φ ≫ 𝓛³/log𝓛` for class-of-one
  constructions, so no class-of-one design can have *both* `log Q` and
  `log(1/μ)` below `𝓛^{3−ε}`.

## 5. Status (checkpoint 1)

| item | statement | label |
|---|---|---|
| Lemma 1.1–1.3 | compatible-event inequality, NA for bit-disjoint families, lopsided LLL inflation | PROVED (standard inputs: Joag-Dev–Proschan, Erdős–Spencer) |
| Thm 1.4 | `−log P(Av) ≥ μ − KΔ`, and `≥ min(μ/2, μ²/(4KΔ))`, for atomic events under lopsided LLL | PROVED |
| Prop 1.5 | bit-disjoint (NA-only) families give at most `𝓛² + O(log𝓛)` | PROVED |
| Thm 2.1 | `log(1/δ*(T)) ≫ 𝓛³/log𝓛` | PROVED modulo the sieve fundamental lemma |
| §3 | MC data: `Φ/(𝓛³/log𝓛) = 0.069–0.070` for `1023 ≤ T ≤ 32767` | EVIDENCE |
| Conj. 3.1 | `Φ ≍ 𝓛³/log𝓛`, i.e. `a = 3` | CONJECTURE |
| upper bound below `𝓛^5` | — | OPEN (in progress) |

Known now: `𝓛³/log𝓛 ≪ Φ ≪ 𝓛^5 log𝓛` (upper bound from OMEGA12, under review;
`𝓛^6` from OMEGA11, reviewed).

## Replay

```
PYTHONPATH=scripts uv run python scripts/haar_fit.py      # §3 table, data/haar/fit.txt
```
