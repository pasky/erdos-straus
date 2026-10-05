# Hostile review R45a of POINTWISE_OMEGA12.md (O45) — headline Thm 5.1 / H_ω(2)

Reviewer 1 of 2. Scope: §§1–5 (Lemmas 1.1, 2.1, 2.2, 3.1, 4.1, Cor 4.2,
Thm 5.1) and §7 numerics. §6/6A (Thms 6.1, 6.3, Lemma 6.2) only skimmed.
Reviewed commit: side-agent/homega @ 1eeefea (merged into this branch).
ET = Elsholtz–Tao arXiv:1107.1010, read from `sources/elsholtz-tao-1107.1010.pdf`
(pdftotext), statements quoted below are from that file.

## Summary verdicts

| claim | verdict |
|---|---|
| Lemma 1.1 | SOUND |
| Lemma 2.1 | SOUND (brute-forced bijection to 10⁶) |
| Lemma 2.2 | SOUND mod ET Prop 1.4 |
| Lemma 3.1 | SOUND mod ET Prop 1.4 (MINOR m1) |
| Lemma 4.1 | SOUND mod ET Prop 1.4, Thm 7.1, Cor 7.4, (7.10) (MINOR m2–m4) |
| Cor 4.2 | SOUND |
| Thm 5.1 | SOUND mod ET: H_ω(2) holds as stated |
| §7 numerics | SOUND (reproduced independently at 10⁴,10⁵,10⁶) |

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

### Lemma 4.1 — SOUND (modulo ET Prop 1.4, Thm 7.1, Cor 7.4, (7.10))
Identity `Σ_{e|P}h(e)=Σ_{q|P}(1/i)τ(P/q)` ✓ (also brute-forced on 3000 P's in
`scripts/review_o12a_R.py`). `q|P ⇒ ℓ` odd, `ℓ∤ad` ✓.
*Large q:* `P≤4(2A−1)²(2B−1)+1<32Z³` ✓; `2log(32Z³)/log Z≤8.5` for `Z≥16` ✓;
`Z<16`: `h(P)≤Ω(P)≪1` ✓.
*Quadratic case (A≥B, Z=A≥16, q≤A^{1/2}).* `x_0≠0` (P(0)=1), `a≥A≥q>x_0 ⇒ a'≥1` ✓,
`a'≤⌊2A/q⌋=N'`, `N'≥⌊2A^{1/2}⌋≥A^{1/2}` ✓. Coefficients `4dq, 8dx_0,
(4dx_0²+1)/q` are non-negative integers `<16A^{3/2}≤N'^5` iff `A≥16` ✓.
Root counts — the specific point the brief asked about:
  - `p=2`: Q odd-valued (P odd, q odd) ⇒ `ρ_Q(2^j)=0` ✓;
  - `p=ℓ`: `Q(a')≡0 (ℓ^j) ⇔ P(qa'+x_0)≡0 (ℓ^{i+j})`; `a'↦qa'+x_0 mod ℓ^{i+j}`
    is injective from `ℤ/ℓ^j`, and P has ≤2 roots mod `ℓ^{i+j}` ⇒ `ρ_Q(ℓ^j)≤2` ✓
    (in fact ≤1, Hensel lift of the single root ≡x_0);
  - `p∤2ℓ`: q unit mod `p^j` ⇒ `ρ_Q(p^j)=ρ_{4d}(p^j)≤2` (0 if p|d) ✓.
  So (7.2) holds with `C=2` for **all** `p,j`; constant `≪_{2,5,2}` absolute,
  independent of `d,q,x_0` ✓. Brute force (`scripts/review_o12a_rho.py`:
  39 values of d, q∈{3,9,27,5,25,7,49,13,169,17,289}, every root `x_0`, all
  prime powers `≤400` incl. 2-powers and ℓ-powers): 40 546 checks, `ρ_Q≤2`,
  `ρ_Q(2^j)=0`, `ρ_Q(m)=ρ_{4d}(m)` for `ℓ∤m` ✓. Multiplicativity step
  `Σ_{m≤N'}ρ_Q(m)/m ≤ (Σ_jρ_Q(ℓ^j)ℓ^{−j})Σ_{m≤2A}ρ_{4d}(m)/m ≤ 2Σ…` ✓.
  Then `(1/(AB))·2·(2A/q)·2·Σ_{d<2B}Σ_{m≤2A}ρ_{4d}(m)/m ≪ (1/(qB))·B log A` by
  (7.10) with ET's `(A,B,k)=(2B,2A,4)` ✓.
*Linear case (B>A, Z=B≥16, q≤B^{1/2}).* `d_0∈(0,q)` unique, `d≥B≥q ⇒ d'≥1` ✓,
`b_a≤4a²` odd, `gcd(4a²,b_a)=1` ✓ (brute-forced too). Coefficients `≤16B²≤N^6`
iff `B≥16` ✓. Cor 7.4 with fixed exponent 6 ⇒ constant absolute ✓.
`Σ_{a∈[A,2A)}1/a<2` ✓.
*Sum over q:* `Σ_{q≤Z^{1/2}}1/(iq)≪log log Z` ✓. No hidden log: each q costs
`≪log Z/q` uniformly, the per-q constants are absolute.
Numerically (own code, T=10⁴, all blocks `A²B≤T`): `max R/(log(Z+2)loglog(Z+16))
= 1.2903` at `(A,B)=(8,2)` — matches the author; per-q normalised pieces
`F(q)=q·Σ_{q|P}τ(P/q)/(ad)/log Z` stay `≤1.32` (worst `(A,B,q)=(64,1,5)`).
(10⁶ run: §7.)

### Cor 4.2 — SOUND
For fixed `(a,c,d)`, `f↦e=P/f` is a bijection on divisors, so the f-sum is
`≤Σ_{e|P}h(e)` ✓; `Σ_c1/c<2` ✓; `𝓛` values of C × `O(𝓛²)` pairs × `𝓛 log𝓛` ✓.

### Thm 5.1 — SOUND (modulo the four ET inputs, all correctly stated)
`Ω_0≤2(Σ_I+Σ_II)` (Lemma 2.1, checked numerically: 120.7≤127.3 at 10⁴,
273.9≤285.5 at 10⁵). `Ω♯` in O11 §4 is `Σ_{all (M,D)} s·h` with
`s=C log log T·g/M`, so `Ω♯=C log log T·Ω_0` exactly as the author writes ✓.
Hence `Ω♯≪𝓛^4(log𝓛)^2`, i.e. **H_ω(2)** of O11 §4, modulo ET ✓.

### §7 numerics — SOUND (independently reproduced to all printed digits)
Own enumeration (`scripts/review_o12a_atoms.py`, divisors of `A_M²` from
scratch; converse enumeration over `(a,c,d,f)`), `data/review_o12a/`:

| T | atoms (D≤A) | converse | S_0' | Ω_0' | mean h | Σ_I | Σ_II | (Σ_I+Σ_II)/Ω_0' | Ω_0(all D) ≤ 2(Σ_I+Σ_II) |
|---|---|---|---|---|---|---|---|---|---|
| 10⁴ | 35 803 | 35 803 | 28.7539 | 62.1826 | 2.163 | 18.3728 | 45.2982 | 1.024 | 120.73 ≤ 127.34 |
| 10⁵ | 547 733 | 547 733 | 58.0370 | 139.4231 | 2.402 | 42.8550 | 99.9057 | 1.024 | 273.87 ≤ 285.52 |
| 10⁶ | 7 777 872 | 7 777 872 | 105.0291 | 274.8096 | 2.617 | 87.0516 | 194.1566 | 1.023 | 543.19 ≤ 562.42 |

All match the author's table. Lemma 4.1 ratio (`scripts/review_o12a_R.py`,
all 126 blocks `A²B≤10⁶`): max `1.2903` at `(8,2)`, decreasing in large
blocks (≈0.32–0.34 at `Z≈5·10⁵`); per-q pieces `F(q)≤1.313`
(`data/review_o12a/R_1e6.txt`). Lemma 3.1's two inner inequalities checked
**without implied constants** at 10⁵ (`scripts/review_o12a_l31.py`): small-q
part ≤ `(2/(ad))Σ_{q≤C}1/(iq)` for every `(a,d,f,C)` (worst ratio 0.111);
large-q pointwise bound holds for every quadruple; N always odd. Mass per
c-scale decreasing (8.90 at C=1, 4.36 at C=64), mean `h(N)` rising slowly
(1.52→1.85), consistent with the author's 10⁶ profile.

### §6/6A — not reviewed in depth (reviewer 2's scope)
Spot-check of Lemma 6.2's arithmetic only: `ℓ>𝓛 ⇒ ℓ−1≥⌊𝓛⌋>𝓛−1`,
`∏ℓ/(ℓ−1)≤exp(1.45𝓛/(𝓛−1))≤e^{2.9}` at `𝓛=2`, decreasing ✓; ℓ=2 never divides
M ✓; `θ(x)<1.01624x` (Rosser–Schoenfeld) ✓. The transfer of Lemma 6.2 into
O11 Lemma 2.2 / Thm 3.2 was not re-checked here.

## Defects

No FATAL, no MAJOR defects found in §§1–5.

**m1 (MINOR, Lemma 3.1 proof, "Split h(N) … at q≤C / q>Y").** For `C=1`,
`Y=2`, the split omits `q=2`. Harmless (N|M odd), but say so. Repair: add
"(`q=2` never divides the odd N)" after the split.

**m2 (MINOR, Lemma 4.1, "ET prove (7.10) for ET's A≤B").** Accurate but
slightly misleading: (7.10)'s proof does not use `A≤B` (verified in
reviews/exceptional-kary3-review.md and re-read here). Repair: cite that
review, or keep as is (the author only uses the `A≤B` regime anyway).

**m3 (MINOR, Lemma 4.1, root count at p=ℓ).** `ρ_Q(ℓ^j)≤2` is proved; in
fact `ρ_Q(ℓ^j)≤1` (only the Hensel lift of `x_0` is ≡x_0 mod q). Cosmetic;
it would also make the factor `(1+2/(ℓ−1))` → `ℓ/(ℓ−1)`. No repair needed.

**m4 (MINOR, Lemma 4.1 coefficient bound "≤8dq").** The three coefficients
are `4dq`, `8dx_0<8dq`, `(4dx_0²+1)/q<4dq`; the bound holds but the
constant term's bound needs `x_0≤q−1` — one clause would make it explicit.

## Summary verdict
Theorem 5.1 (`Ω_0≪𝓛^4log𝓛`, hence H_ω(2): `Ω♯≪𝓛^4(log𝓛)^2`) is
**SOUND, PROVED modulo ET Prop 1.4, Thm 7.1, Cor 7.4 and (7.10)**, whose
hypotheses are met as the author claims (in particular (7.2) at `p=2` and
`p=ℓ` for the shifted quadratic). The label "PROVED mod ET" is appropriate.
Only cosmetic repairs m1–m4 are suggested. §6 not reviewed here.
