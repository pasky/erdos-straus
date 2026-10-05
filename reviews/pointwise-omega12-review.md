# Hostile review R45a of POINTWISE_OMEGA12.md (O45) — headline Thm 5.1 / H_ω(2)

Reviewer 1 of 2. Scope: §§1–5 (Lemmas 1.1, 2.1, 2.2, 3.1, 4.1, Cor 4.2,
Thm 5.1) and §7 numerics. §6/6A (Thms 6.1, 6.3, Lemma 6.2) only skimmed.
Reviewed commit: side-agent/homega @ 1eeefea (merged into this branch).
ET = Elsholtz–Tao arXiv:1107.1010, read from `sources/elsholtz-tao-1107.1010.pdf`
(pdftotext), statements quoted below are from that file.

## Summary verdicts (filled in as the review proceeds)

| claim | verdict |
|---|---|
| Lemma 1.1 | (pending) |
| Lemma 2.1 | (pending) |
| Lemma 2.2 | (pending) |
| Lemma 3.1 | (pending) |
| Lemma 4.1 | (pending) |
| Cor 4.2 | (pending) |
| Thm 5.1 | (pending) |
| §7 numerics | (pending) |

## Per-claim notes

### Lemma 1.1 — SOUND
(a) `ℓ^i|M ⇔ i≤v_ℓ(M)` ✓. (b) `H_{x+y}−H_x≤H_y` ✓ (applied per prime). (c)
`ℓ^i>Y ⇒ i>log Y/log ℓ ⇒ 1/i<log ℓ/log Y`, ≤v such i, `Σ v log ℓ = log N` ✓.
Re-derived; no hidden hypothesis (Y≥2 only to keep log Y>0).

### Lemma 2.1 — SOUND (re-derived + brute force)
Re-derivation. `D|A²`, `D≤A`, write `D=da²` (d squarefree). For each p,
`v_p(D)≤2v_p(A)`; if `v_p(D)=2k` then `v_p(da)=k≤v_p(A)`, if `=2k+1` then
`v_p(da)=k+1≤v_p(A)` (as `2k+1≤2v`). So `da|A`, `b:=A/(da)`, and `D≤A ⇔ a≤b` ✓.
`M=4dab−1`, `M+P=4da(a+b)`, `gcd(g,4da)=1` ⇒ `g|a+b` ✓. `4acd=N+f` ✓.
`N≥f−2/e` ⇒ `2N≥4acd−2/e` ⇒ `N≥2acd−1≥acd` ✓. Involution: `D` invertible mod M,
`4A≡1`, so `4A²/D+1≡(4D)^{-1}(4D+1)` ✓. Injectivity ✓. Factor 2 from the
involution (fixed point D=A double-counted, harmless) ✓.

Brute force (`scripts/review_o12a_atoms.py`, own enumeration of divisors of
`A²`, own converse enumeration over `(a,c,d,f)` with `gcd(M,P)=e` test): all
identities hold, the map is injective, and the converse count equals the
atom count (bijection onto the quadruples with `gcd(4dab−1,P)=e`):

| T | atoms all D | atoms D≤A | converse | S_0' | Ω_0' | Σ_I | Σ_II |
|---|---|---|---|---|---|---|---|
| 2000 | 9472 | 4986 | 4986 | 16.0234 | 31.5015 | 8.9590 | 23.2568 |
| 10⁴ | 69106 | 35803 | 35803 | 28.7539 | 62.1826 | 18.3728 | 45.2982 |

At 10⁴ these agree with the author's §7 table to all printed digits.
Full `Ω_0` (all D) = 120.73 ≤ `2(Σ_I+Σ_II)` = 127.34 ✓.

## Defects

| 10⁵ | 1070466 | 547733 | 547733 | 58.0370 | 139.4231 | 42.8550 | 99.9057 |

(10⁶ row: see §7 below.)

### ET statements actually used (checked against the PDF)

* **Prop 1.4** (p. 4): for `A,B>1`, `k≪(AB)^{O(1)}`:
  `Σ_{a≤A}Σ_{b≤B} τ(kab²+1) ≪ AB log(A+B) log(1+k)`. Used with `k=4`,
  ET's `(a,b)=(d,a)`, ET's `(A,B)=(2B,2A)≥2` ✓ (strict `>1` holds).
* **Thm 7.1** (p. 25): `N>1`, P of degree D with **non-negative integer**
  coefficients `≤N^l`, `ρ(p^j)≤C` for **all** primes p and all `j≥1`; then
  `Σ_{n≤N}τ(P(n)) ≪_{D,l,C} N Σ_{m≤N}ρ(m)/m`. No irreducibility or
  fixed-divisor hypothesis. ✓
* **Cor 7.4** (p. 29): `a,b≪N^{O(1)}` ⇒ `Σ_{n≤N}τ(an+b) ≪ τ((a,b))N log N`. ✓
* **(7.10)** (p. 30): `Σ_{a≤A}Σ_{m≤B}ρ_{ka}(m)/m ≪ A log B log(1+k)`. ET state it
  inside the `A≤B` case, but the proof (pp. 30–32: q<A, A≤q≤kA, q>kA ranges)
  never uses `A≤B`; reviews/exceptional-kary3-review.md already verified it
  for all `A,B≥2`, `k≥1`, absolute constant. Here `k=4` is fixed anyway, and
  the author only uses it in the regime ET's `A≤B` (`B≤A` here) ✓.

### Lemma 2.2 — SOUND (modulo ET Prop 1.4)
`Σ_{c∈[C,2C)}1/c≤1+log 2<2` ✓, τ(P) choices of f per `(a,d)` (c-sum independent
of f) ✓, `1/(ad)≤1/(AB)` ✓. Block count `O(𝓛²)·O(𝓛)`, `log(A+B+2)≤𝓛+O(1)` ⇒ `S_0≪𝓛^4` ✓.

### Lemma 3.1 — SOUND (modulo ET Prop 1.4); one MINOR presentational gap
Small q: for `ℓ|4ad`, `N≡−f (ℓ)` and `f|P`, `P≡1 (ℓ)` for `ℓ|ad`, P odd for
`ℓ=2` ⇒ `ℓ∤N` ✓. Otherwise `4ad` is a unit mod q, c lies in one class, and
`#{c∈[C,2C): c≡c_0 (q)} ≤ ⌈C/q⌉ ≤ 2C/q` for `q≤C` ✓ (this is the "full
period" point: no first-term loss because the c-window has length `C≥q`).
`1/N≤1/(adC)`; `Σ_{q≤C}1/(iq)≤log log C+O(1)` (Mertens + convergent
`Σ_{i≥2}`) ✓. Large q: Lemma 1.1(c) with `N≤M≤T` ✓. Sum over
`C=2^j`: `(𝓛/log2)(1+H_J)≪𝓛 log𝓛` ✓; `Σ_{(A,B)}log(A+B+2)≪𝓛³` ✓.
The averaging is honest: per `(A,B)` the bound is `log(A+B+2)·Σ_j(…)`, no
hidden dependence of constants on C. (MINOR m1 below: q=2 at C=1.)
