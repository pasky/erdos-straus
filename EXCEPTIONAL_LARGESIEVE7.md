# EXCEPTIONAL_LARGESIEVE7 — residue dispersion (RD) for large-height labels (task O73)

Status: **in progress** (agent O73, branch `side-agent/residue-dispersion`).
ES is not solved; nothing here claims it. Labels as in `DISCOVERIES.md`.
Notation: LS4/LS5/LS6 = `EXCEPTIONAL_LARGESIEVE{4,5,6}.md`, K2 =
`EXCEPTIONAL_KARY2.md`. `z = exp((log N)^{1/4})`, `β = 1/log z`,
`w_q = (Kq^{−γ})^{2β} = K^{2β}e^{−2γ log q/log z}`; `Γ` as in K2
(`Γ(m) = Π_{ℓ|m}γ'(ℓ)`, `γ'(ℓ) = (1−ℓ^{−1/2})^{−1}` for rough ℓ).
The target is LS6 §6.2 (RD).

## 0. Plan and summary (updated as the work proceeds)

| item | statement | label |
|---|---|---|
| Lemma 1.1 | **triple parametrisation of ℛ(M)**: `ℛ(M) = {−u/v mod M : gcd(u,v)=1, 4uv \| M+1}`; with `t = (M+1)/(4uv)` the class `−4D`, `D = u²t`, also equals `−4u²t` and `−1/(4v²t)`, so `H* ≤ min(max(u,v), 4u²t, 4v²t)` | PROVED (elementary) |
| Lemma 1.2 | **residue pinning**: if `p \| M` and the class is `≡ a (mod p)`, then `4uvt ≡ 1`, `u ≡ −av`, `v²t ≡ −1/(4a)`, `u²t ≡ −a/4 (mod p)`; a residue `a` fixes `(u mod p, t mod p)` as a function of `v mod p` | PROVED (elementary) |

## 1. The ℛ(M) classes as triples

**Lemma 1.1 (triple parametrisation; PROVED, elementary).** Let
`M ≡ 3 (mod 4)`, `A = (M+1)/4`. The map `(u,v) ↦ D = Au/v` is a bijection
from `{(u,v) ∈ ℕ² : gcd(u,v) = 1, uv | A}` onto `{D ∈ ℕ : D | A²}`. With
`t := A/(uv)` one has `D = u²t`, `D′ := A²/D = v²t`, and

    −4D ≡ −u/v ≡ −4u²t ≡ −1/(4v²t)   (mod M).

Hence `ℛ(M) = {−u/v mod M : gcd(u,v) = 1, 4uv | M+1}`, and the least label
height of the class obeys `H*(−4D mod M) ≤ min(max(u,v), 4u²t, 4v²t)`.

*Proof.* Given `D | A²` put `g = gcd(D,A)`, `u = D/g`, `v = A/g`; then
`gcd(u,v) = 1`, and `D | A²` gives `u | (A²/g) = Av`, so `u | A`; with
`v | A` and coprimality, `uv | A`; and `Au/v = gu = D`. Conversely if
`D = Au/v` with `gcd(u,v)=1`, `uv | A`, then `D = (A/v)u` is an integer,
`A²/D = (A/u)v` is an integer, and `gcd(D,A) = (A/v)gcd(u,v) = A/v`, so
`(u,v)` is recovered from D as above (injectivity). `D = (A/v)u = u²t`,
`A²/D = v²t`. Mod M, `4A ≡ 1`, so `−4D = −4Au/v ≡ −u/v`; and
`uvt = A ≡ 1/4` gives `1/v ≡ 4ut`, `1/u ≡ 4vt`, whence `−u/v ≡ −4u²t ≡
−1/(4v²t)`. The three rationals are labels of the class (v, u, 1 are
units mod M since `uv | A` and `gcd(A,M) = 1`). ∎

*Remarks.* (a) This is the classical `4/M = 1/x + 1/y + 1/z`
parametrisation in label form; for `(M, D) = (167, 9)` (R71's example):
`A = 42`, `(u,v,t) = (3,14,1)`, labels `−3/14, −36, −1/784`, and the true
`H* = 13` (label `−13/5`) is smaller than all three — the lemma only gives
an upper bound for `H*`, which is the direction needed (we must *remove*
small-height classes, so we may keep any class whose `H*` is large).
(b) The LS6 concentration examples are triples with one small height:
the class `−4` (`D = 1`) is `(u,v,t) = (1,A,1)` (label `−4u²t = −4`); the
class `−1/k` (`D = A/k`, `k | A`, `gcd(k, A/k) = 1`) is `(1,k,A/k)` (label
`−u/v = −1/k`). Script check: `scripts/largesieve7_triples.py` (all
`M ≡ 3 (4)`, `M < 20000`, every prime `p | M`: 159390 triples).

**Lemma 1.2 (residue pinning; PROVED, elementary).** Let p be a prime,
`p | M`, and let `(u,v,t)` be as in Lemma 1.1. Then `p ∤ uvt`,
`4uvt ≡ 1 (mod p)`, and if the class satisfies `−4D ≡ a (mod p)` then
`a ≢ 0` and

    u ≡ −a v,     v²t ≡ −1/(4a),     u²t ≡ −a/4     (mod p).

Conversely, given `a ≢ 0` and `v ≢ 0 (mod p)`, the residues
`u ≡ −av` and `t ≡ −1/(4av²)` are the unique ones with
`4uvt ≡ 1` and `−u/v ≡ a (mod p)`.

*Proof.* `uvt = A = (M+1)/4 ≡ 1/4 (mod p)` as `p | M` (p odd). Reduce
Lemma 1.1's congruence mod p: `a ≡ −u/v`, so `u ≡ −av`; then
`4(−av)vt ≡ 1` gives `v²t ≡ −1/(4a)`, and `u²t = a²v²t ≡ −a/4`. The
converse is the same computation backwards. ∎

So a class of ℛ(M) through p lying in the residue `a (mod p)` is a lattice
point `(u,v,t)` of the **curve** `𝒞_a = {(−ar, r, −1/(4ar²)) : r ∈ 𝔽_p^×}`
(reduced mod p), with the modulus recovered as `M = 4uvt − 1`. This is the
mechanism of the whole note: a residue condition mod p is a condition
on the divisor triple *in every scale*, and a short cofactor (one M per
triple) is no longer an obstacle, because the triple itself must lie on
𝒞_a.

## 2. Damped mass in arithmetic progressions (Shiu + Rankin)

Fix a threshold `y ≥ z` (below `y = max P`). For `n ≥ 1` put

    W_y(n) := w_{P(n)} Γ(n) n^{−1} · 1[P(n) > y]                      (2.0)

(`P(n)` = largest prime factor; Γ as in K2, so `Γ(n) ≤ 8·3^{ω(n)}`,
`γ'(ℓ) ≤ 3`, `γ'(ℓ) = 1 + O(ℓ^{−1/2})` for `ℓ > W`). For `Y ≥ 2` let

    Ξ_y(Y) := Σ_{Q = 2^j ≥ y/2} w_Q · (log 2Q / log Y) · exp(−log Y / (2 log 2Q)).

**Lemma 2.1 (damped Brun–Titchmarsh in progressions; PROVED, given
Shiu's theorem [Shiu 1980, Thm 1]).** Fix `α ∈ (0, 1/2)`. There is
`C = C(α, W)` such that for all `y ≥ z`, `Y ≥ 2`, `k ≥ 1`, `c` with
`gcd(c,k) = 1` and `k ≤ Y^{1−α}`:

    Σ_{Y < n ≤ 2Y, n ≡ c (k)} W_y(n) ≤ C · Ξ_y(Y) / k.

*Proof.* Split by `P(n) ∈ (Q, 2Q]`, `Q = 2^j ≥ y/2`; there `w_{P(n)} ≤ w_Q`
(w decreasing) and `1/n < 1/Y`. With `η = 1/log 2Q` and
`f(n) = 1[P(n) ≤ 2Q]Γ(n)n^η` (multiplicative, `f(ℓ^l) ≤ 3e^l`,
`f(n) ≪_ε n^ε` uniformly since `η ≤ 1/log z`), Rankin's inequality
`1 ≤ (n/Y)^η` on `n > Y` and Shiu's theorem (`x = 2Y`, interval length
`Y ≥ x^{1/2}`, modulus `k ≤ Y^{1−α}`) give

    Σ_{Y<n≤2Y, n≡c(k), P(n)≤2Q} Γ(n) ≤ Y^{−η} Σ f(n) ≪ Y^{−η}·(Y/φ(k))·(log Y)^{−1}·exp(Σ_{ℓ≤2Q, ℓ∤k} f(ℓ)/ℓ).

Now `f(ℓ)/ℓ ≤ γ'(ℓ)/ℓ + eγ'(ℓ)η log ℓ/ℓ`, so the exponential is
`≪_W log 2Q · Π_{ℓ|k, ℓ≤2Q}(1 − 1/ℓ)` (Mertens; `Σ_{ℓ≤2Q} η log ℓ/ℓ ≤ 1+o(1)`;
`e^{−1/ℓ} ≤ (1−1/ℓ)e^{1/ℓ²}`). Since
`φ(k)/k = Π_{ℓ|k}(1−1/ℓ)` and `Π_{ℓ|k, ℓ>2Q}(1−1/ℓ)^{−1} ≤ e^{2ω(k)/Q} ≤
e^{2 log Y/(Q log 2)}`, we get `(1/φ(k))·Π_{ℓ|k,ℓ≤2Q}(1−1/ℓ) ≤
k^{−1}e^{2log Y/(Q log 2)}`, and `Y^{−η}e^{2 log Y/(Q log 2)} ≤
e^{−log Y/(2 log 2Q)}` because `Q ≥ y/2 ≥ z/2` makes
`2/(Q log 2) ≤ 1/(2 log 2Q)`. Multiply by `w_Q/Y` and sum over Q. Shiu's implied constant depends only
on `α`, the interval exponent, and the growth data `A₁ = 3e`,
`A₂(ε)` (from `8·3^{ω(n)} ≪_ε n^{ε/2}`, `n^η ≤ n^{ε/2}`) of f, which are **uniform in Q**
(η ≤ 1/log z ≤ ε/2 for N large); k = 1 is covered by taking modulus 2
with both classes. ∎

**Lemma 2.2 (sums of Ξ; PROVED, elementary).** For `r ≥ 0`:

    Σ_{Y = 2^i ≥ 2} (log Y)^r Ξ_y(Y) ≤ C_r Σ_{Q=2^j ≥ y/2} w_Q (log 2Q)^{r+2} ≤ C′_r (log z / γ)^{r+3}.

*Proof.* For fixed Q put `L = log 2Q/log 2 ≥ 1`; then
`Σ_{i ≥ 1} i^{r−1} e^{−i/(2L)} ≤ C_r L^{r}(1 + log L) ≤ C_r L^{r+1}`;
multiply by `w_Q log 2Q·(log 2)^{r−1}`. Finally
`w_Q = K^{2β}e^{−2γ j log 2/log z}` with `K^{2β} ≤ z^{γβ} = e^γ` (as
`K ≤ z^{γ/2}`), and `Σ_j (j log 2)^{s}e^{−2γ j log 2/log z} ≤
C_s (log z/γ)^{s+1}`. ∎

(The bound is uniform in X: the damping `w_Q` makes the sum over the top
converge, and Rankin's factor makes the sum over n at fixed top converge.
This is the "Shiu in progressions" input of (FM2), in damped form.)

## 3. (RD) at a single prime for the ℛ(M) classes

For a rough prime p and `a ∈ (ℤ/p)^×` let

    μ^{ℛ,>}_a(p) := Σ_{M ≡ 3 (4), p | M, P(M/p) > p}  Σ_{C ∈ ℛ(M): b_C ≡ a (p), H*(C) > p^{1/4}}  w_{P(M)}Γ(M)·p/M,

the ℛ-part of LS6's `μ^>_a({p})` for the **full** family (all moduli M,
smooth parts included; the rough-modulus subfamily present in every fibre
is a sub-sum; fibres are discussed in §6). With `n = M/p`, Lemma 1.1 and
`Γ(M) ≤ 2Γ(n)`:

    μ^{ℛ,>}_a(p) ≤ 2 Σ_{(u,v,t) ∈ 𝒯_a(p)} W_p((4uvt − 1)/p),                 (3.0)

    𝒯_a(p) := {(u,v,t) ∈ ℕ³ : 4uvt ≡ 1, u ≡ −av (mod p), min(max(u,v), 4u²t, 4v²t) > p^{1/4}}

(every class is `−4D` for at least one `D | A²`, i.e. one triple; the
triple's three label heights are `≥ H*(C)`; coprimality of `(u,v)` is
dropped).

**Theorem 3.1 ((RD) at one prime, ℛ(M) classes; PROVED, given Shiu's
theorem).** There is an absolute C such that for every prime `p ≥ z`,
every `a ≢ 0 (mod p)` and every X (the bound does not depend on X):

    μ^{ℛ,>}_a(p) ≤ C γ^{−5} (log p)^{6} · p^{−1/12}.

*Proof.* Fix `α = 1/100`. Split `𝒯_a(p)` into dyadic boxes
`B = [U,2U)×[V,2V)×[T,2T)` (U, V, T powers of 2) and put `Y_B = UVT/p`.
Triples in B have `n = (4uvt−1)/p ∈ [3Y_B, 32Y_B)`, and `n > p` (as
`P(n) > p`), so only boxes with `UVT > p²/32` occur. Distinct triples
with the same `(v,t)` give distinct n. Four cases.

*Case L_u: `16VT ≤ Y_B^{1−α}`.* Fix `(v,t)`. The admissible u are those
with `4uvt ≡ 1 (p)`, and `n = (4uvt−1)/p` then runs injectively through
the single class `n ≡ −p^{−1} (mod 4vt)` (reduced, since `pn ≡ −1`).
Lemma 2.1 with `k = 4vt ≤ Y^{1−α}` for every dyadic `Y ∈ [Y_B, 32Y_B]`
gives `Σ_u W_p(n) ≤ C Ξ̂(Y_B)/(vt)`, `Ξ̂(Y_B) := Σ_{Y=2^i∈[Y_B,32Y_B]}Ξ_p(Y)`.
The pairs `(v,t)` in the box satisfy `v²t ≡ c′ := −1/(4a) (mod p)`
(Lemma 1.2) and `4v²t > p^{1/4}`. For each v, t lies in one class mod p;
for each t, v lies in at most two; hence their number is
`≤ min(V(T/p+1), 2T(V/p+1)) ≤ 2VT/p + 2min(V,T)`, and it is 0 unless
`32·max(V,T)³ ≥ 4(2V)²(2T) > p^{1/4}`, i.e. unless
`max(V,T) ≥ p^{1/12}/4`. So

    Σ_B ≤ C Ξ̂(Y_B)·(2/p + 2·1[max(V,T) ≥ p^{1/12}/4]/max(V,T)).

*Case L_v: `16UT ≤ Y_B^{1−α}`.* Same, with the roles of u and v exchanged:
pairs `(u,t)` with `u²t ≡ −a/4 (p)` and `4u²t > p^{1/4}`; n runs through
the class `−p^{−1} mod 4ut`. Same bound with `max(U,T)`.

*Case L_t: `16UV ≤ Y_B^{1−α}`.* Fix `(u,v)`; n runs through
`−p^{−1} mod 4uv`. Pairs: `u ≡ −av (p)`, `max(u,v) > p^{1/4}`; number
`≤ min(V(U/p+1), U(V/p+1)) ≤ UV/p + min(U,V)`, zero unless
`max(U,V) ≥ p^{1/4}/2`. Same bound with `max(U,V)` and `p^{1/4}/2`.

*Case S: none of the three.* Multiplying the three failed inequalities,
`16³(UVT)² > (UVT/p)^{3(1−α)}`, so `UVT < C p^{(3−3α)/(1−3α)} ≤ Cp^{3.07}`,
and each side, e.g. `U = UVT/(VT) < 16p^{1−α}(UVT)^α ≤ Cp^{1.021}`.
Counting as above (fix the variable with the fewest values; the other two
are then each in one class mod p, resp. v in two classes when t is fixed):
`#(𝒯_a ∩ B) ≤ 2(1 + Cp^{0.021})²·min(U,V,T)`. Here `n ≤ 32Y_B ≤ Cp^{2.07}`,
so `W_p(n) ≤ Γ(n)/n ≤ C_δp^{δ}·p/(UVT)` (no damping used). With
`min(U,V,T) ≤ (UVT)^{1/3}` and `UVT > p²/32`:
`Σ_B ≤ C_δ p^{1+δ+0.042}(UVT)^{−2/3} ≤ C p^{−0.28}`. There are
`≤ (C log p)³` such boxes.

*Summation.* Every box is in at least one case; assign it to one. The
`2/p` terms: for a dyadic `Y = 2^i`, the boxes with `Y ∈ [Y_B, 32Y_B]`
number `≤ 6(i + log₂p + 1)²`, so their total is
`≤ (C/p)Σ_i (i + log p)²Ξ_p(2^i) ≤ (C/p)(log p)²(log z/γ)^5` (Lemma 2.2,
r ≤ 2). The `1/max` terms: `Σ_U Ξ̂(UVT/p) ≤ 6Σ_iΞ_p(2^i) ≤ C(log z/γ)³`
for each (V,T), and `Σ_{V,T: max(V,T) ≥ p^{1/12}/4} 2/max(V,T) ≤
C log p·p^{−1/12}` (there are `2k+1` dyadic pairs with `max = 2^k`).
Cases L_v, L_t alike (L_t even with `p^{−1/4}`). Case S: `≤ Cp^{−1/4}`.
Collect, use `log z ≤ log p` and (3.0). ∎

*Remarks.* (a) **Why the short cofactors cause no trouble.** LS6 §6.2
feared the regime "one cofactor per divisor", where divisor-in-class
bounds (Lenstra, Coppersmith–Howgrave-Graham–Nagaraj) give only `O(1)`
per modulus. In the triple picture there is no distinguished divisor:
whichever of u, v, t is long carries the progression (Case L), and
when none is long (Case S) the whole configuration lives at scale
`≤ p^{1+o(1)}` per coordinate with total `UVT ≥ p²/32`, where the
residue condition (two of the three coordinates pinned mod p by the
third) beats the weight `p/(UVT)` trivially. The pinning of Lemma 1.2 —
a residue mod p of the class fixes the residues of **two** of the
coordinates — is what replaces divisor-in-residue-class bounds.
(b) The exponent 1/12 comes only from the small-height cut at
`p^{1/4}` (a height `> H₀` forces some coordinate `> (H₀/32)^{1/3}`); with
cut `p^{κ}` the same proof gives `p^{−min(κ/3, 1/4)}`. The concentration of
Prop 6.2 of LS6 (the class `−4`, triple `(1, A, 1)`, height `4u²t = 4`)
is exactly the kind of triple removed by the cut: in Case L_v the term
`1/max(U,T)` is attained by a single pair `(u,t)` of small `4u²t` in the
pinned class, carrying damped mass `≍ 1/(ut)` over all cofactors.

## 4. Several primes: (RD) as stated in LS6 is false; what survives

LS6's (RD) asks, for sets P of up to `(log N)^C` rough primes, for
`μ^>_a(P) ≤ (log N)^C Π_{p∈P}p^{−γ₀}` with the height cut
`H*(C) > max_{p∈P}p^{1/4}`. The cut depends only on the **largest** prime,
while the claimed gain is a product over **all** of P. A single label of
height just above `(max P)^{1/4}` refutes it.

**Proposition 4.1 (label obstruction; PROVED, elementary — fundamental
lemma of the sieve for the fibre version).** Let `y ≥ z^{16}`, let
`P ⊆ (z, y]` be any set of primes, `P̄ = Π_{p∈P}p`, and let k be a prime
in `(2y^{1/4}, 4y^{1/4}]` with `k ∉ P` (exists as `|P| ≤ (log N)^C`). Put `a_p ≡ −1/k (mod p)` (p ∈ P). Then the
rough-modulus classes alone give

    μ^>_a(P) ≥ c · w_{2y} / (y^{1/4} log z)        (c > 0 absolute).

Consequently, for every fixed `γ₀ > 0` and C, (RD) fails (for N large)
for every P consisting of at least `⌈1/(2γ₀)⌉ + 1` primes in `[y/2, y]`,
`y = z^{16}` — in every fibre, since rough-modulus classes are present in
every fibre (LS5 §1, R67b).

*Proof.* For a prime `r ∈ (y, 2y]` and a z-rough `j ≤ y` with
`j ≡ −(P̄r)^{−1} (mod 4k)` put `M = P̄rj`. Then `4k | M+1`, so
(Lemma 1.1 with `(u,v) = (1,k)`) the class `−1/k mod M` belongs to ℛ(M);
its residue at every `p ∈ P` is `a_p`; `top = r > max P` (as `j ≤ y < r`);
and its least label height is exactly k: the label `−1/k` has height
`k < √(M/2)`, and by LS5 Lemma 1.2 every other label of the class has
height `≥ M/(2k) > k`. So `H* = k > (max P)^{1/4}`, and the class
contributes `w_rΓ(M)P̄/M ≥ w_{2y}/(rj)`. Distinct (r, j) give distinct
moduli. The fundamental lemma (sifting `j ≤ x`, `j ≡ c (mod 4k)`, by the
primes `≤ z` not dividing 4k; `x/(4k) ≥ y^{5/8}/16 ≥ z^{9}`, sieve level `z^5`) gives
`#{j ≤ x : …} ≫ x/(k log z)` for `x ∈ [y^{7/8}, y]`, hence
`Σ_j 1/j ≫ log y/(k log z)`; and `Σ_{y<r≤2y}1/r ≫ 1/log y`. Multiply. For
the consequence: with `|P| = m` primes in `[y/2, y]`,
`Π_{p∈P}p^{−γ₀} ≤ (y/2)^{−mγ₀} ≤ (y/2)^{−1/2−γ₀}`, while
`μ^>_a(P) ≥ c e^{−32γ−1}y^{−1/4}/log z` (`w_{2y} ≥ e^{−2γ log 2y/log z}` up to
`K^{2β} ≥ 1`); the ratio is `≥ y^{1/4+γ₀}/(log N)^{O(1)} → ∞` since
`y ≥ z = e^{(log N)^{1/4}}`. ∎

So the height cut must scale with the **product** P̄ (a label of height H
puts mass `≍ 1/H` — times the cofactor mass — on one residue vector
mod P̄ whatever P is). Even then a second effect appears:

*Remark 4.2 (short cofactors relative to P̄; Assessment).* A single class
C through P with cofactor `n = G_C/P̄` contributes `w_{P(n)}Γ/n` to
`μ_{b_C}(P)` — independently of its residue and height. If some class with
`H*(C) > P̄^{κ}` has `n < P̄^{γ₀}/(log N)^C`, the product-cut (RD) fails at
that P. Generic classes of ℛ(P̄n) have `H* ≍ √(P̄n)`; but proving that
some `(P̄n+1)/4` with `y < n < P̄^{γ₀}`, `P(n) > y`, has a factorisation
`uvt` with all three heights `> P̄^{κ}` is a sieve problem beyond the
sifting range (the n-range is far shorter than the moduli involved), and
is not done here. So: product-cut (RD) for **short** cofactors
`n < P̄^{1/2}` — open in both directions; for long cofactors see Thm 4.3.

**Theorem 4.3 (product-cut (RD) for long cofactors, ℛ(M) classes;
PROVED, given Shiu's theorem).** Let P be a finite set of primes `> z`,
`P̄ = Π_{p∈P}p`, `y = max P`, `a = (a_p) ∈ Π_p(ℤ/p)^×`, `κ ∈ (0,1]`,
`η ∈ (0,1]`, and

    μ^{ℛ}_a(P; κ, η) := Σ_{M = P̄n, M≡3(4), P(n)>y, n ≥ P̄^{1/2+η}} Σ_{C∈ℛ(M): b_C≡a_p (p) ∀p∈P, H*(C) > P̄^{κ}} w_{P(n)}Γ(M)P̄/M.

Then, uniformly in X, `μ^{ℛ}_a(P; κ, η) ≤ C_η γ^{−5}(log P̄)^{6}·4^{|P|}·(P̄^{−κ/3} + P̄^{−η/2})`.
(`4^{|P|} ≤ P̄^{2/log z}`, so this is `≤ (log P̄)^{O(1)}P̄^{−min(κ/3,η/2)+o(1)}`.)

*Proof.* As Theorem 3.1, with p replaced by P̄ and these changes.
(i) Lemma 1.2 at each `p ∈ P` and CRT: `4uvt ≡ 1`, `u ≡ −av`,
`v²t ≡ c′`, `u²t ≡ c″ (mod P̄)`; v determines `(u, t) mod P̄`, u determines
v, and t determines v up to `2^{|P|}` classes. (ii) `Y_B = UVT/P̄`; the
damped weight is `W_y` (top `> y`), and Lemma 2.1 is applied with this y.
(iii) Pair counts become `≤ 2^{|P|}(VT/P̄ + min(V,T))` (similarly for the
other pairs), and the height cut forces `max ≥ P̄^{κ/3}/4`; so the L-cases
give `2^{|P|}·C(log P̄)^{6}γ^{−5}(P̄^{−1} + P̄^{−κ/3})` after summation (the
summation of Thm 3.1 verbatim, `log p → log P̄`). (iv) Case S: take
`α = η/100`; the three failed inequalities give `UVT < CP̄^{(3−3α)/(1−3α)} ≤ CP̄^{3+6.2α}` and
sides `≤ CP̄^{1+2.1α}`, the point count is
`≤ 2^{|P|}(1+CP̄^{2.1α})²min(U,V,T)`, `W_y(n) ≤ C_δP̄^{δ}·P̄/(UVT)`, and now
`UVT ≥ P̄n/32 ≥ P̄^{3/2+η}/32` (long cofactor), so with `δ = η/10`
`Σ_B ≤ 2^{|P|}C_ηP̄^{1+4.2α+δ}(UVT)^{−2/3} ≤ 2^{|P|}C_ηP̄^{4.2α+δ−2η/3}
≤ 2^{|P|}C_ηP̄^{−η/2}`, over `≤ (C log P̄)³` boxes. (v) `Γ(M) ≤ 2Γ(n)` as
`Π_{p∈P}γ′(p) ≤ e^{2|P|z^{−1/2}} ≤ 2`. ∎

*What the three results say together (ℛ(M) classes).*
* One prime: (RD) holds, rate `p^{−1/12}` (Thm 3.1).
* Several primes, LS6's cut `max_{p∈P}p^{1/4}`: false (Prop 4.1) — the
  cut has to grow with P̄.
* Several primes, product cut `P̄^{κ}`: true for cofactors
  `n ≥ P̄^{1/2+η}` (Thm 4.3); for short cofactors `y < n < P̄^{1/2}` a single
  class already weighs `≍ 1/n`, so no bound of the form `Π p^{−γ₀}` can hold
  without an extra condition (Remark 4.2) — those witnesses must be
  handled in the (DCC) combinatorics, where such a class is "almost all
  shared primes": its only non-shared prime factors are those of the short
  cofactor n.

## 5. The other class types; the H*-cut must be a residue cut

In a fibre the classes are the **rough parts** (modulus `G_r`, residue
`b mod G_r`, LS5 §1/R67b), and `H*` is the least label height **mod
`G_r`**. (For ℛ(M), Lemma 1.1's labels are labels mod M, hence mod `M_r`,
so Theorems 3.1/4.3 apply verbatim to the rough parts.)

**Proposition 5.1 ((RD) with the H*-cut fails at one prime for (a,D)
classes; PROVED, elementary).** Let `z < ℓ < p < q` be primes, and consider
the (a,D) class with `a = pq`, `D = ℓ` (so `g(D) = ℓ`, `G = 4pqℓ`), i.e.
`x ≡ −(4ℓ + pq) (mod 4pqℓ)`; its rough part is `x mod pqℓ` with
`x ≡ −4ℓ (mod pq)`, `x ≡ −pq (mod ℓ)`. Then `H*(x mod pqℓ) ≥ pq/(4ℓ+1)`,
its residue mod p is `−4ℓ`, and its top is q. Hence, in every fibre c
(the class is present for the q with `pq ≡ −c−4ℓ… ` i.e. for the q in one
class mod 4, by the smooth-part filter),

    μ^>_{−4ℓ}({p}) ≥ Σ_{q>p prime, q in one class mod 4} w_q Γ(pqℓ)/(qℓ) ≥ c e^{−2γ t_p}/(γ t_p ℓ),   t_p = log p/log z,

(Mertens in classes mod 4; the asymptotic as in LS6 Prop 6.2). With
`ℓ ∈ (z, 2z)` and `p = z^{T}`, `T ≥ 2/γ₀`, this exceeds
`(log N)^C p^{−γ₀}` for N large. So **(RD) as formulated in LS6 (cut on
the class height `H*(C)`) is false already for `|P| = 1`** once (a,D)
classes are in the family.

*Proof.* If `−r/s ≡ x (mod pqℓ)` with `gcd(s, pqℓ) = 1` and
`H = max(r,s) < pq/(4ℓ+1)`, then `r ≡ 4ℓs (mod pq)` and
`|r − 4ℓs| ≤ (4ℓ+1)H < pq` force `r = 4ℓs`; mod ℓ the class gives
`r ≡ pqs (mod ℓ)`, so `ℓ | pqs`, i.e. `ℓ | s` — contradiction. The
weight of the class in `μ({p})` is `w_qΓ(G_r)p/G_r = w_qΓ/(qℓ)`. The
smooth part of G is 4 and the class is present at c iff
`c ≡ −(4ℓ+pq) (mod 4)`, a condition on `q mod 4`. The sum over q is
`≍ ∫_{t_p}^∞ e^{−2γt}dt/t`. Comparison: `p^{−γ₀} = e^{−γ₀T log z}` while
the lower bound is `≥ e^{−O(γT)}/(Tz)`; `γ₀T log z ≥ 2 log z`. ∎

*Why this is harmless, and the correct formulation.* The residue
`−4ℓ (mod p)` is the residue of the **small** label `−4ℓ`
(height `4ℓ ≤ p^{1/4}` for `T ≥ 5`): the class has large height but sits
on a small-height residue. LS6's route (§6.1 Assessment, LS4 Lemma 5.1)
uses the small-height structure only through the **deterministic residue
sets** `R_p(H₀) = {λ mod p : H(λ) ≤ H₀}`: pinned values in `R_p` pay
`p^{−1/2}` there, and only residues **outside** `R_p` need dispersion.
So the statement actually needed is the residue-cut form

> **(RD′)** for `a ∉ R_P(H₀)` (no label of height `≤ H₀` is `≡ a (mod P̄)`),
> `μ_a(P)` — summed over **all** classes through P with top `> max P` — is
> `≤ (log N)^C·P̄^{−γ₀}`, with `H₀ = P̄^{κ}`.

Since a class with a label of height `≤ H₀` puts its residue in `R_P(H₀)`,
`a ∉ R_P(H₀)` forces `H*(C) > H₀` for every class in residue a; hence the
H*-cut statement implies (RD′), and **for ℛ(M) classes Theorems 3.1 and
4.3 give (RD′)** (|P| = 1, and |P| ≥ 1 with long cofactors). Prop 4.1
also refutes the multi-prime (RD′) with the cut `max_{p∈P}p^{1/4}` (the
residue `−1/k` there lies outside `R_P((max P)^{1/4})` — `k` exceeds that
height, and any other label congruent to `−1/k` mod P̄ has height
`≥ P̄/(2k)`), so the product cut `P̄^{κ}` is needed in (RD′) as well.

*(a,D) and Case A under (RD′) (Assessment; not proved here).* The same
pinning mechanism is available:
* (a,D), `p | a`: the residue is `−4D (mod p)`, so `D ≡ d₀` is pinned;
  writing `D = e f²`-type with `g(D) ≍ ef`, the pairs `(e,f)` lie on
  `ef² ≡ d₀ (mod p)` — the same curve as the `(v,t)` pairs of Thm 3.1
  — and `a ∉ R_p(H₀)` gives `4D > H₀`. `p | g`: the residue is `−a`, so
  the parameter a is pinned mod p with least representative `> H₀`; a
  one-variable progression (Lemma 2.1).
* Case A (`G = 4rh`, `mm′ = 4rh²+1`, class `−1/m`): `p | rh` gives
  `mm′ ≡ 1`, so `m ≡ −1/a` **and** `m′ ≡ −a (mod p)` are both pinned, and
  `a ∉ R_p(H₀)` gives `m, m′ > H₀`. The long-variable regimes need
  divisors of `4rh²+1` in progressions (the ElT Prop 1.4 / K2 Lemma 3.6
  inputs, in damped form); the short regime is a count of points of
  `mm′ = 4rh²+1` with both factors pinned mod p. Not written.
