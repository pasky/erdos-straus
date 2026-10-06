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
`2/(Q log 2) ≤ 1/(2 log 2Q)`. Multiply by `w_Q/Y` and sum over Q. ∎

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
