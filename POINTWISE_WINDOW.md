# POINTWISE_WINDOW — unconditional Ω-results for the window statistic `a_min(p)`

Task O10. Builds on `POINTWISE_SIZE.md` §§8–11 (window frame, Lemma 8.2,
Cor 8.3, Prop 8.4, Lemma 11.3, Prop 11.4, Assessment 11.5).
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. **Cited** = external theorem whose statement we read (in the
source or in an archived secondary source), proof not re-checked.

Status: checkpoint 1 (2026-10-04). Not yet reviewed.

## 0. Results at a glance

| # | statement | label |
|---|---|---|
| W1 (§2) | `#{p≤x hard : a_min(p)≥7} ≫ x/(log x)^{3/2}`, via `p≡1 (840)` and window 3 failing; order sharp | **PROVED** modulo cited sieve theorems (semi-linear lower sieve, Selberg upper sieve, BV). This makes POINTWISE_SIZE Prop 11.4 rigorous; no gap found. Cross-citation: FHRSS 2025 Thm 1.1(2) |
| W2 (§4) | `#{p≤x hard : a_min(p)≥11} ≫ x/(log x)^2` | **CONDITIONAL** on Elliott–Halberstam |
| Lemma 1.2 | parity of the number of q-bad factors of `n_q` equals `(p/q)` | PROVED |
| Lemma 6.1 | every failing window costs sieve dimension `≥1/2`; congruence classes cannot lower it | PROVED |
| Prop 7.2 | the generic one-step Buchstab route for two windows has margin exactly 0 at level x | PROVED (computation) |
| §7.1 | sift-to-`√x` route: K=7 at BV, K=11 at EH, nothing beyond at any level if `β^{opt}_{3/2}>2` | Assessment |
| §7.3 | `a_min→∞` unconditionally: not reached; obstruction is dimension growth against `z≤x^{1/2}` plus the linear-sieve parity threshold at J=2; a single window has **no** parity barrier | Assessment |
| §3, §5 | `N_3(x)/(x/(log x)^{3/2})` flat at 0.0123–0.0126 to `10^{11}`; joint F1 counts flat at scale `x/(log x)^{1+J/2}` for J≤8; 5731 primes `p<10^{11}`, `p≡1 (840)`, with `a_min≥35` by F1 alone | EVIDENCE |

Goal 2 answer: the largest K reached unconditionally is **7**. K=11 is
reached on EH. Unconditional K=11 needs level `ϑ≥1`, or a bilinear
(parity-breaking) input, for a two-condition semi-linear problem on
shifted primes. We know of no such result in the literature (searched
2026-10-04; nearest: FHRSS 2025, one form only).

## 1. Setup: window failure as a sifting condition

Notation as in POINTWISE_SIZE §8.1. `p≡1 (mod 8)` prime, `q≡3 (mod 4)`,
`0<q<3p`, `n_q:=x_q=(p+q)/4`. A prime `r` is **q-bad** if the Jacobi symbol
`(r/q)=−1`, **q-good** otherwise (for `r∤q`; `r|n_q` implies `r∤q`, Lemma 8.2).

**Lemma 1.1 (F1 as a sifting condition; PROVED).** If `n_q` has no q-bad
prime factor, window q fails (both targets), i.e. `Rat_q(n_q)∩{−1,−p}=∅`.

*Proof.* Lemma 8.2 gives `(r/q)=(r/p)` for every prime `r|n_q`; so "no q-bad
factor" is exactly F1 (Cor 8.3(a)). ∎

The point of writing F1 via `(r/q)` rather than `(r/p)`: the sifting set
`P_q={r prime : (r/q)=−1}` is a union of residue classes mod `4q`, of
relative density 1/2 among primes, **independent of p**. So "window q
fails by F1" is a half-dimensional sifting condition on the shifted prime
`(p+q)/4`, with a p-independent sifting set.

**Lemma 1.2 (parity of the bad part; PROVED).** Let `Ω_q^-(n)` be the
number of q-bad prime factors of n counted with multiplicity. For
`gcd(n_q,q)=1`, `(−1)^{Ω_q^-(n_q)}=(n_q/q)=(p/q)`.

*Proof.* Multiplicativity of the Jacobi symbol: `(n_q/q)=∏_{r|n_q}(r/q)^{v_r}=(−1)^{Ω_q^-}`;
and `4n_q≡p (mod q)`, `(4/q)=1`. ∎

So if `(p/q)=+1`, every `n_q` has an **even** number of q-bad factors.
Whether bad factors are present at all is not a congruence datum
(Lemma 11.3); their parity is. This is why the half-dimensional problem has
no Selberg parity barrier at the level of a single window (§4).

**Window 3.** `P_3={r≡2 (mod 3)}` (Jacobi `(r/3)=−1` iff `r≡2 (3)`; this
includes `r=2`). For `p≡1 (mod 3)`, window 3 fails **iff** `n_3` has no
prime factor `≡2 (mod 3)` (the converse of Lemma 1.1 holds at q=3: a factor
`r≡2` gives `u=r,v=1`, `u/v≡2≡−1≡−p (mod 3)`). Then `a_min(p)≥7`.

## 2. Theorem W1: `a_min(p)≥7` for `≫x/(log x)^{3/2}` hard primes (Prop 11.4 made rigorous)

**Theorem W1 (PROVED modulo the cited sieve theorems S1–S3 below).**
```
N_3(x) := #{p≤x prime : p≡1 (mod 840), (p+3)/4 has no prime factor ≡2 (mod 3)} ≫ x/(log x)^{3/2}.
```
Every such p is Mordell-hard (`1` is one of Mordell's six classes mod 840)
and has `a_min(p)≥7` (§1, window 3). The order is sharp: `N_3(x)≪x/(log x)^{3/2}`
by any upper-bound sieve of dimension 1/2 (notes Thm 70.9 is this bound on
all shifted primes).

### 2.1 Cited inputs

* **S1 (semi-linear sieve, lower bound).** H. Iwaniec, *The half dimensional
  sieve*, Acta Arith. 29 (1976) 69–95; in the β-sieve form of
  Friedlander–Iwaniec, *Opera de Cribro* (AMS Colloq. Publ. 57, 2010),
  Theorem 11.13 with `κ=1/2`, `β=1`. We use it exactly as it is quoted and
  applied in Teräväinen, arXiv:1611.08585, §6, display (6.4)
  (archived: `sources/sieve/teravainen-1611.08585.{pdf,txt}`, lines ≈1440–1465).
  Statement used: let `A` be a finite weighted sequence, `P` a set of primes,
  `g` multiplicative on squarefree `d|P(z)` with `0≤g(ℓ)<1` and the
  dimension condition
  `∏_{w≤ℓ<z, ℓ∈P}(1−g(ℓ))^{−1} ≤ (log z/log w)^{1/2}(1+K/log w)` (`2≤w<z`).
  Write `|A_d|=g(d)X+r_d`. Then for `D=z^s`, `1≤s≤2`,
  ```
  S(A,P,z) ≥ X·V(z)·(f(s)+o(1)) − Σ_{d<D, d|P(z)} |r_d|,
  f(s) = (e^γ/(π s))^{1/2} ∫_1^s dt/(t(t−1))^{1/2},   V(z)=∏_{ℓ<z,ℓ∈P}(1−g(ℓ)),
  ```
  `o(1)→0` as `D→∞`, uniformly for s in compact subsets of `[1,2]` (Teräväinen
  writes the error as `O((log N)^{−0.1})`). We only use: **`f(s)>0` for
  `s>1`, and `f(s)≥c_f (s−1)^{1/2}` for `1<s≤2`** with
  `c_f=(e^γ/π)^{1/2}≈0.753`: on `[1,2]`, `t(t−1)≤2(t−1)`, so
  `∫_1^s dt/√(t(t−1)) ≥ √2·√(s−1)`, and `(e^γ/(πs))^{1/2}≥(e^γ/(2π))^{1/2}` for `s≤2`.
* **S2 (upper-bound sieve for prime pairs).** Uniformly in integers
  `a≥1` with `3∤a`, `2|a`, and `y≥3`:
  `#{r≤y prime : ar−3 prime} ≤ C_0·(a/φ(a))·y/(log y)^2`, `C_0` absolute.
  This is the standard dimension-2 upper bound (Halberstam–Richert, *Sieve
  Methods*, Thm 3.12, the case `ap+b`, `b=−3`; or Selberg's sieve directly):
  sift `{r(ar−3): r≤y}` by primes `ℓ<ξ=y^{1/4}`; the number of classes is
  `ω(ℓ)=2` for `ℓ∤6a`, `ω(ℓ)=1` for `ℓ|6a` (`ℓ=2`: `ar−3` odd; `ℓ=3∤a`: only
  `r≡0`; `ℓ|a`: `ar−3≡−3≢0`), independent of the *size* of a. Selberg's
  bound gives `≪ y∏_{ℓ<ξ}(1−ω(ℓ)/ℓ) + ξ^2(log ξ)^2 ≪ (a/φ(a))y/(log y)^2`.
  Uniformity in large a (here up to `a≈x^{1/2+ε}≫y`) holds because only
  `ω(ℓ)` enters. Primes `r<ξ` contribute `≤ξ`.
* **S3 (Bombieri–Vinogradov).** For every A there is B with
  `Σ_{k≤x^{1/2}(log x)^{−B}} max_{(b,k)=1}|π(x;k,b)−li(x)/φ(k)| ≪_A x/(log x)^A`.
* Mertens in progressions mod 3:
  `∏_{ℓ<w, ℓ≡j (3)}(1−1/ℓ)^{−1} = c_j(log w)^{1/2}(1+O(1/log w))`, `j=1,2`.

### 2.2 Proof of Theorem W1

Fix `0<ε≤1/20` (chosen at the end, absolutely). Put
`z=x^{1/2−ε}`, `D=x^{1/2}(log x)^{−B}/840` (B from S3 with A=2),
`s=log D/log z`. Then `s→1/(1−2ε)`, so for `x≥x_0(ε)`: `1+ε≤s≤2`.

**Sifting data.** `A={n_p=(p+3)/4 : p≤x, p≡1 (mod 840)}`,
`P={ℓ prime: ℓ≡2 (mod 3)}`. Since `p≡1 (840)`, `n_p≡1 (mod 210)`; so no `n_p`
is divisible by 2, 3, 5 or 7. Set `g(2)=g(5)=0` (and `r_d=0` if `2|d` or
`5|d`). For squarefree `d|P(z)` with `(d,10)=1` we have `(d,840)=1`, and
`d|n_p ⟺ p≡−3 (mod d)`; with `p≡1 (840)` this is one reduced class
`b_d mod 840d`. So
`|A_d|=π(x;840d,b_d)`, `X=li(x)/φ(840)=li(x)/192`, `g(d)=1/φ(d)`,
`r_d=π(x;840d,b_d)−li(x)/φ(840d)`.

* *Dimension.* For `ℓ≡2 (3)`, `ℓ≥11`: `1−g(ℓ)=(1−1/ℓ)(1−(ℓ−1)^{−2})`, so by
  Mertens mod 3, `∏_{w≤ℓ<z}(1−g(ℓ))^{−1}=(log z/log w)^{1/2}(1+O(1/log w))`.
  S1's hypothesis holds with `κ=1/2`; and `V(z)≥c_V(log x)^{−1/2}`, `c_V>0` absolute.
* *Remainder.* `Σ_{d<D}|r_d| ≤ Σ_{k≤840D} max_b|π(x;k,b)−li(x)/φ(k)| ≪ x/(log x)^2` (S3).

**Step 1 (lower bound to z).** By S1 and `f(s)≥c_f(s−1)^{1/2}≥c_fε^{1/2}`,
```
S(A,P,z) ≥ (li(x)/192)·c_V(log x)^{−1/2}·(c_f ε^{1/2}−o(1)) − O(x/(log x)^2) ≥ c_1 ε^{1/2} x/(log x)^{3/2}
```
for `x≥x_0(ε)`, with `c_1>0` **absolute** (independent of ε).

**Step 2 (structure of survivors).** Let `n=n_p` be counted by `S(A,P,z)`.
Its bad (`≡2 mod 3`) prime factors are all `≥z`. If there are k of them
(with multiplicity), then `z^k≤n<x`, so `k<1/(1/2−ε)<3`. By Lemma 1.2
(`(p/3)=1`), k is even. So `k∈{0,2}`. If `k=0`, window 3 fails: p is counted
by `N_3(x)`. If `k=2`, `n=m r_1 r_2` with bad primes `z≤r_1≤r_2` and every
prime factor of m `≡1 (mod 3)`. Hence `N_3(x)≥S(A,P,z)−T_1−T_2`, where
`T_1` counts `r_1=r_2` and `T_2` counts `r_1<r_2`.

**Step 3 (`T_1`).** `T_1≤Σ_{r≥z} x/r^2≤2x/z=2x^{1/2+ε}`.

**Step 4 (`T_2`, the only real work).** Here `p=4mr_1r_2−3`, so
`T_2 ≤ Σ_{m,r_1} #{r_2≤y prime : a r_2−3 prime}`, with `a=4mr_1` and
`y=(x+3)/(4mr_1)`. Only pairs with `y>r_1` contribute (`r_2>r_1`). Hence
`r_1≤√x`, `m≤(x+3)/(4z^2)≤x^{2ε}`, and `log y≥log z≥(log x)/3`. Also
`2|a`, `3∤a`. By S2, each inner count is
`≤C_0(a/φ(a))y/(log y)^2 ≤ 9C_0·x/(log x)^2·1/(φ(m)(r_1−1))`. Now
* `Σ_{z≤r_1≤√x}1/(r_1−1) = log(log√x/log z)+O(1/log x) = log(1/(1−2ε))+o(1) ≤ 3ε`;
* `Σ_{m≤x^{2ε}, ℓ|m⇒ℓ≡1(3)} 1/φ(m) ≤ ∏_{ℓ≤x^{2ε},ℓ≡1(3)}(1+ℓ/(ℓ−1)^2)`
  `≤ ∏(1−1/ℓ)^{−1}·∏_ℓ(1+(ℓ−1)^{−2}) ≤ C_2(2ε log x)^{1/2}`.

So `T_2≤C_3 ε^{3/2} x/(log x)^{3/2}`, with `C_3=27√2·C_0C_2` absolute.

**Step 5.** `N_3(x) ≥ (c_1ε^{1/2}−C_3ε^{3/2})x/(log x)^{3/2} − 2x^{1/2+ε}`. Take
`ε=min(1/20, c_1/(2C_3))`: `N_3(x)≥(c_1/2)ε^{1/2}x/(log x)^{3/2}` for `x≥x_0`. ∎

**Remarks.**
* The whole difficulty of "complete absence" sits in Step 4. The
  semi-linear sieve's limit `β=1` lets z go up to `x^{1/2−ε}` at BV level, so
  at most two large bad primes remain, and parity removes the odd case. The
  gain `ε^{1/2}` (main) vs `ε^{3/2}` (pairs) is the extra factor `Σ1/r_1≍ε`.
  This is the classical route of Iwaniec (1972) for `p=x^2+y^2+1` (cf.
  Teräväinen §6, which handles the same `T` with a linear upper sieve and a
  numerical inequality instead of the `ε→0` limit).
* Compared with Prop 11.4's sketch: the "uniform prime-pair upper-bound
  sieve" is S2 (only `ω(ℓ)` enters, so uniformity in `a≫y` is automatic);
  the "weighted summation over m" is the `1/φ(m)` Euler product; the
  `(s−1)^{1/2}` behaviour is the explicit lower bound for f. No other
  gap was found. **Status of Prop 11.4: PROVED modulo S1–S3 (cited).**
* Effectivity: S1 and S2 are effective; S3 (BV) is ineffective through
  Siegel's theorem, so `x_0` is ineffective. One can replace BV by a
  Siegel-free BV variant at the cost of nothing structural; not pursued.

## 3. Numerical check of W1 (EVIDENCE)

`scripts/window_w1.py XMAX` (segmented sieve on `p=840k+1`, `n=210k+1`;
cross-checked against brute-force sympy factorisation at `x=10^6`, 244 = 244;
a random subsample of the counted primes is re-checked with the independent
`Rat_q` routine of `pointwise_size_amin.amin`, asserting `a_min≥7`).

| x | primes `p≡1 (840)` | window 3 fails (`N_3`) | fraction | `N_3/(x/(log x)^{3/2})` |
|---|---|---|---|---|
| 1e6 | 395 | 244 | 0.6177 | 0.0125 |
| 1e7 | 3426 | 1945 | 0.5677 | 0.0126 |
| 1e8 | 30061 | 15912 | 0.5293 | 0.0126 |
| 1e9 | 264770 | 131924 | 0.4983 | 0.0124 |
| 1e10 | 2369556 | 1118043 | 0.4718 | 0.0124 |
| 1e11 | 21445485 | 9622751 | 0.4487 | 0.0123 |

The normalised count is flat (0.0123–0.0126) over five decades, as W1
and the matching upper bound predict. The fraction itself decays like
`(log x)^{−1/2}` (`fraction·(log x)^{1/2}` = 2.30, 2.28, 2.27, 2.26, 2.26, 2.26).
Re-check of 300 random counted `p<10^11`: all have `a_min≥7`; the
distribution of `a_min` is `{7:148, 11:113, 15:23, 19:11, 23:3, 27:1, 31:1}`.
So conditioning on window 3 failing, window 7 fails about half the time —
the joint (two-window) event is common numerically; the obstacle in §4 is
purely one of proof technology.

### 2.3 An independent citation route for W1

Fuchs–Hsu–Rickards–Schindler–Stange, *Primes represented by shifted
quadratic forms: on primitivity and congruence classes*, arXiv:2504.20289
(archived `sources/sieve/2504.20289.{pdf,txt}`), Theorem 1.1(2): for a
primitive positive definite form `f` with `(a,2D)=1`, `B≥1`, `A≠0`,
`gcd(A,B)=1`, `2|AB` or `D≢5 (8)`, and `gcd(m,2DB)=1`, `gcd(l−A,m)=1`, the
number of primes `p≤N`, `p≡l (m)`, primitively represented by `Bf(x,y)+A`
is `≫N/(log N)^{3/2}`. Take `f=x^2+xy+y^2` (`D=−3`, `a=1`), `B=4`, `A=−3`,
`m=35`, `l=1`. A primitive value `n=f(x,y)` has no prime factor `≡2 (3)`
(such primes are inert in `Z[ω]`, so `r|f(x,y)` forces `r|x,y`). Moreover
`n` is odd (x, y not both even) and `n≡(x−y)^2 (mod 3)`. For `p=4n−3` prime,
`3∤n`, so `n≡1 (3)`. Hence `p≡1 (mod 24)`; with `p≡1 (35)` this gives
`p≡1 (840)`. So FHRSS Thm 1.1(2) implies W1 directly. Their proof is
Iwaniec's 1972 argument, i.e. the same S1–S3 route. We cite it as a
cross-check, not as an independent proof.

## 4. Two windows: `a_min(p)≥11` under Elliott–Halberstam (Theorem W2)

### 4.1 Why W1's proof stops at one window

W1 works because the semi-linear sieve has sifting limit `β_{1/2}=1`. At BV
level `x^{1/2}` it therefore sifts up to `z=x^{1/2−ε}`. Then at most two
large bad primes survive; parity (Lemma 1.2) removes one of them, and the
two-prime configurations cost `ε^{3/2}` against a main term `ε^{1/2}`.

Two windows (3 and 7) form a sieve problem of **dimension 1** on the
primes. For a prime `ℓ∤840` the forbidden classes of p are `−3 mod ℓ` if
`ℓ≡2 (3)`, and `−7 mod ℓ` if `(ℓ/7)=−1`. The characters mod 3 and mod 7 are
independent, so `Σ_{ℓ<z}ω(ℓ)log ℓ/ℓ=log z+O(1)`. The linear sieve has
`β_1=2`, so sifting up to `z=x^{1/2−ε}` needs level `D=z^{2+}≈x^{1−2ε+}`.
That is the Elliott–Halberstam range, not the BV range. At BV level the
two-window sieve only reaches `z<x^{1/4}`. Each window can then carry two or
four large bad primes, and the two-bad configurations are no longer
small. §5 quantifies this.

### 4.2 Statement

**Theorem W2 (CONDITIONAL on EH for primes).** Assume EH: for every
`η,A>0`, `Σ_{k≤x^{1−η}} max_{(b,k)=1}|π(x;k,b)−li(x)/φ(k)| ≪_{η,A} x/(log x)^A`.
Then
```
N_{3,7}(x) := #{p≤x : p≡1 (840), (p+3)/4 has no prime factor ≡2 (3),
               (p+7)/4 has no prime factor r with (r/7)=−1}  ≫ x/(log x)^2,
```
and every such p is hard with `a_min(p)≥11` (Lemma 1.1 at q=3 and q=7).

### 4.3 Proof (same skeleton as W1, with the linear sieve)

* **Cited S1'.** Linear sieve lower bound: Jurkat–Richert / Iwaniec,
  e.g. *Opera de Cribro* Thm 11.13 with `κ=1`, `β=2` (as quoted by Teräväinen §6,
  (6.6)), or Halberstam–Richert Thm 8.4. Under `(Ω_1)`, for `2≤s≤3`:
  `S(A,P,z)≥XV(z)(f(s)+o(1))−Σ_{d<D,d|P(z)}|r_d|` with
  `f(s)=2e^γ log(s−1)/s`. Since `log(1+u)≥u/2` on `[0,1]`, we get
  `f(s)≥(e^γ/3)(s−2)` for `2<s≤3`.
* **Data.** `A={p≤x : p≡1 (840)}`, `X=li(x)/192`. Put
  `P=P_3∪P_7` (primes `≡2 (3)` or with `(ℓ/7)=−1`), `ω` as above,
  `g(ℓ)=ω(ℓ)/(ℓ−1)`. For `ℓ|840` there are no forbidden classes: `n_3≡1`
  and `n_7≡2 (mod 210)`, `n_7/2` odd, and 2 is 7-good. `ω(ℓ)≤2<ℓ−1`, and
  `(Ω_1)` holds by Mertens mod 21. `V(z)≥c_V/log x`. `r_d` is a sum of at
  most `2^{ω(d)}` prime-count discrepancies mod `840d`, so
  `Σ_{d<D}μ^2(d)|r_d|≪x/(log x)^2` for `D=x^{1−ε}/840` by EH (with the usual
  Cauchy–Schwarz/trivial bound to absorb the `2^{ω(d)}` weight).
* **Parameters.** `z=x^{1/2−ε}`, `s=log D/log z→(1−ε)/(1/2−ε)=2+2ε/(1−2ε)`. So
  `f(s)≥(2/3)e^γε(1−o(1))` and `S(A,P,z)≥c_1εx/(log x)^2`, with `c_1` absolute.
* **Survivors.** For each `q∈{3,7}` the q-bad factors of `n_q` are all
  `≥z`, so there are at most two of them. Their number is even (Lemma 1.2:
  `(p/3)=(p/7)=1`), so it is 0 or 2. Hence
  `N_{3,7}≥S−T_1−T^{(3)}−T^{(7)}`. Here `T_1≪x^{1/2+ε}` counts
  square factors `r^2`, `r≥z`. `T^{(q)}` counts sifted p with
  `n_q=mr_1r_2`, `z≤r_1<r_2` q-bad, and m q-good with `m≤x^{2ε}`.
* **`T^{(q)}`, keeping the other window.** Fix `(m,r_1)`, put `a=4mr_1`, and
  count primes `r_2≤y=(x+q)/a` such that `ar_2−q` is prime **and**
  `n_{q'}=mr_1r_2+(q'−q)/4` has no q'-bad prime factor `<z`. Sifting `r_2`
  by primes `ℓ<y^{1/10}` (with `ℓ∤42a`) removes the classes
  `0`, `q/a`, and `(q−q')/a` (the last only when ℓ is q'-bad). These are
  distinct for `ℓ>7`. This is an upper-bound problem of dimension `5/2`. By
  Selberg's upper-bound sieve (level `y^{1/5}`, trivial remainders), the count
  is `≪(a/φ(a))^3 y/(log y)^{5/2}`. Summing as in W1, Step 4, with
  `Σ_{z≤r_1≤√x}1/r_1≤3ε` and
  `Σ_{m≤x^{2ε}, m q-good}(m/φ(m))^3/m≪(ε log x)^{1/2}`, gives
  `T^{(q)}≤C ε^{3/2}x/(log x)^2`.
* **Conclusion.** `N_{3,7}(x)≥(c_1ε−2Cε^{3/2})x/(log x)^2−O(x^{1/2+ε})`. Then
  take ε small. ∎

The essential new point compared with W1 is keeping the other window's
half-dimensional condition inside the upper bound for `T^{(q)}`. Without
it, `T^{(q)}≍ε^{3/2}x/(log x)^{3/2}` would swamp the main term
`εx/(log x)^2`.

## 5. Joint F1 failure of the first J windows (EVIDENCE)

`scripts/window_joint.py XMAX J` counts the primes `p=840k+1≤x` for which windows
`3,7,…,4J−1` are **all** F1-clean, i.e. every prime factor r of `n_q` has
`(r/q)=+1`. This implies `a_min(p)≥4J+3`. The counts are cross-checked
against brute-force sympy factorisation at `x=10^6` for `J≤3`
(395/244/160/52 both ways). Prime counts
(`p≡1 (840)`): `x=10^6…10^11`: 395, 3426, 30061, 264770, 2369556, 21445485.

| x \ J | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 1e6 | 244 | 160 | 52 | 28 | 9 | 4 | 2 | 1 |
| 1e8 | 15912 | 8912 | 2675 | 1614 | 496 | 172 | 95 | 24 |
| 1e10 | 1118043 | 549500 | 147738 | 77906 | 22340 | 6789 | 3816 | 939 |
| 1e11 | 9622751 | 4486561 | 1147221 | 572604 | 156751 | 45947 | 24351 | 5731 |

Normalised by `x/(log x)^{1+J/2}` (the sieve-dimension prediction):

| x \ J | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 1e8 | 0.0126 | 0.0302 | 0.0390 | 0.1009 | 0.1331 | 0.1980 | 0.4695 | 0.5090 |
| 1e10 | 0.0124 | 0.0291 | 0.0376 | 0.0951 | 0.1309 | 0.1908 | 0.5147 | 0.6078 |
| 1e11 | 0.0123 | 0.0288 | 0.0370 | 0.0930 | 0.1282 | 0.1891 | 0.5044 | 0.5974 |

Each column is roughly flat, as the dimension-`J/2` heuristic predicts.
The joint events are abundant: 5731 primes `p<10^11` in the single class
`1 mod 840` have `a_min≥35` by F1 alone. Window 27 uses the same
character as window 3 (`(r/27)=(r/3)`), which is why the `J=7` survival
ratio is high (24351/45947). The classes `−3` and `−27 mod ℓ` are still
distinct, so the dimension still adds.

## 6. Dimension bookkeeping: every failing window costs dimension ≥ 1/2

**Lemma 6.1 (PROVED).** Let `q≡3 (4)` and `G=(Z/q)^×`, and suppose window q
fails for p. Let `C_big` be the set of residue classes `c∈G` containing at
least q distinct primes dividing `n_q`, and put `K=⟨C_big⟩≤G`. Then
`−1∉K`, so `[G:K]≥2`. Moreover, `n_q` has fewer than `q·φ(q)` distinct prime
factors whose class lies outside K.

*Proof.* Suppose `−1∈K`. Then `−1=∏_{c∈C_big}c^{e_c}` with `0≤e_c<ord(c)≤q`.
For each `c∈C_big`, choose `e_c` distinct primes `r|n_q` in class c, and let
u be the product of all the chosen primes and `v=1`. Then `uv|n_q` is
squarefree and `u/v≡−1 (mod q)`, so `−1∈Rat_q(n_q)` and the window succeeds,
a contradiction. Every class outside K is outside `C_big`, so it holds
`<q` of the primes, and there are `<φ(q)` such classes. ∎

**Consequence (dimension count; PROVED as a counting statement).** The
primes in classes outside K form a set of relative density
`1−1/[G:K]≥1/2`, and all but `O_q(1)` of them must be absent from `n_q`.
So the failure of window q is contained in a finite union, over subgroups
`K∌−1` and over the `O_q(1)` exceptional primes, of events of sieve
dimension `≥1/2`. For the first J windows the forbidden classes `−q mod ℓ`
are distinct for `ℓ>4J`. Hence "windows `3,…,4J−1` all fail" is covered by
sieve events of dimension `≥J/2`. This is the rigorous form of the
"dimension `≥K/8`" bookkeeping in Assessment 11.5. The `O_q(1)` exceptional
primes change only `log log` factors in upper bounds, not the dimension.

**Congruence restrictions do not help (PROVED; complements Lemma 11.3).**
Restricting p to a class mod Q fixes the divisibility of `n_q` by the
primes `ℓ|Q`, and nothing else. The sifting set of window q loses at most
the finitely many primes dividing Q, so its density, and hence the
dimension, is unchanged. Choosing p in clever classes can force small
prime factors of the `n_q`, but it cannot lower the dimension `J/2`. The
suggestion "kill some windows by F1 through congruences" is therefore
impossible for every window (Lemma 11.3), and it saves nothing in
dimension (this paragraph).

**The upper-bound side matches (Assessment, standard).** An upper-bound
sieve of dimension `J/2` gives
`#{p≤x : windows 3,…,4J−1 all F1-clean} ≪_J x/(log x)^{1+J/2}`. The
normalised counts of §5 are flat at exactly this scale.

## 7. How far the sieve routes go; which parity obstruction applies

### 7.1 Route A: sift to `z≈x^{1/2}`, then parity (W1, W2)

This route sifts all windows up to `z=x^{1/2−ε}`. Each window is then
left with zero or two large bad primes (Lemma 1.2), and the two-prime
configurations cost an extra factor `ε^{1/2}`. It needs a lower-bound sieve
of dimension `κ=J/2` that is positive at `s=log D/log z≈2ϑ`, where `D=x^ϑ` is
the level. So it needs `β_{J/2}≤2ϑ`, with `β_κ` the sifting limit.

| J (windows) | K reached | κ | needs | available |
|---|---|---|---|---|
| 1 | 7 | 1/2 | `β_{1/2}=1≤2ϑ`: ϑ≥1/2 | BV: **unconditional (W1)** |
| 2 | 11 | 1 | `β_1=2≤2ϑ`: ϑ≥1 (any `ϑ>1−2ε`) | **EH (W2)** |
| ≥3 | ≥15 | ≥3/2 | `β_{3/2}≤2ϑ≤2` | impossible if `β^{opt}_{3/2}>2` |

* `β_{1/2}=1` and `β_1=2` are optimal (Iwaniec; Selberg's parity examples).
* The optimal sifting limit is non-decreasing in κ, because a κ'-dimensional
  problem satisfies `(Ω_κ)` for every `κ≥κ'`. Hence `β^{opt}_{3/2}≥2`, and
  route A can at best be borderline at `J=3` even at level `x`.
* All sieves we know of have `β_{3/2}` near 3 (DHR-type; recalled from
  memory, not re-checked). Moduli `>x` carry no information about primes
  `≤x`, so no level hypothesis rescues route A for `J≥3`.

**Assessment 7.1.** Route A is exhausted at `K=11`. It reaches
`K=7` unconditionally and `K=11` only on EH.

### 7.2 Route B: sift lower, subtract large-bad configurations

Sift to `z=x^{1/s}` with s larger, and subtract the p for which some window
keeps large bad primes. Use the Bonferroni inequality with parity: if a
window has two or more large bad primes, the smaller one is `<√x`, so
`1[clean_q] ≥ 1 − #{q-bad r|n_q : z≤r<√x}`.

**Proposition 7.2 (zero margin at level x; PROVED, as a computation with
the linear-sieve functions).** Take `J=2` and level `D=x` (EH taken
literally), with `2≤s≤3`. Bound each subtracted set `A_r` by the linear
upper sieve, at level `D/r` with sifting limit z. Then the main term and
the subtraction cancel identically:
```
f(s) − Σ_{q∈{3,7}} (1/2)∫_{1/s}^{1/2} F(s(1−α)) dα/α
  = 2e^γ log(s−1)/s − ∫_{1/s}^{1/2} 2e^γ dα/(s α(1−α)) = 0 .
```
(The bad primes of each window have density 1/2, so
`Σ_{r∈P_q, r≈x^α} g(r)` contributes `(1/2)dα/α`. The level for `A_r` is
`x^{1−α}`, and `F(t)=2e^γ/t` for `t≤3`. The integral is
`(2e^γ/s)[log(α/(1−α))]_{1/s}^{1/2}=(2e^γ/s)log(s−1)`.)

So the generic one-step Buchstab route sits **exactly** at the threshold
at level x, and is negative at level `x^{1/2}`. There the `A_r` with
`r>D^{1−o(1)}` cannot even be bounded without switching. W2 escapes
only because route A uses more than the sieve axioms: the parity of
the bad count is a congruence datum (Lemma 1.2). That forces a sifted
`n_q/r` of size `≤x^{1/2+ε}` to be `m·r_2`, which the generic bound `F(1)` does not see.

### 7.3 Which parity obstruction applies (answer to Goal 3)

* **Single window: none.** Selberg's parity barrier says a sieve cannot
  tell an even number of prime factors from an odd one. For a window,
  the parity of the number of *bad* prime factors is fixed by a
  congruence (Lemma 1.2: `(−1)^{Ω_q^-(n_q)}=(p/q)`). So the event
  "no bad factor" is a half-dimensional problem with sifting limit 1,
  and W1 proves it at BV level. The parity information is an *input*,
  not an obstruction.
* **Two windows: the linear-sieve parity threshold.** The joint problem
  has dimension 1, and its sieve functions f, F are the linear ones.
  These are extremal, attained by Selberg's λ-twisted sequences.
  Proposition 7.2 shows the generic route has margin exactly 0 at level
  x. Route A survives at level x only by feeding in the
  congruence-parity of Lemma 1.2. At BV level (`ϑ=1/2`), the two-window
  problem asks a linear sieve to sift beyond `z=x^{1/4}=D^{1/2}`, which is
  precisely where the Selberg example forces `f(s)=0` (`s≤2`).
  Unconditional `K=11` would therefore need either a level of
  distribution `ϑ≥1` for the relevant sequences, or a genuinely bilinear
  (Chen-switching / Type-II) input that breaks the linear-sieve parity
  barrier for this problem. We have done neither.
* **Unboundedly many windows: dimension, not parity.** By Lemma 6.1,
  `a_min(p)>4J−1` costs dimension `≥J/2` (Route A needs
  `β_{J/2}≤2`, which fails for large J; Route B's subtracted mass per
  window is comparable to the clean mass once `z≤x^{1/3}`, and there are
  J windows). Any proof of `a_min(p)→∞` along a subsequence must
  therefore produce primes p for which an unbounded number of shifted
  values `(p+q)/4` simultaneously avoid a density-1/2 set of primes
  (up to `O_q(1)` exceptions), i.e. a lower bound in a sieve problem of
  unbounded dimension with complete-absence conditions. No such result
  is known for *any* family of unboundedly many shifts of primes. The
  closest known results produce one condition (Iwaniec 1972; FHRSS 2025),
  or "many" but not all conditions (Maynard–Tao). **Assessment:**
  `a_min→∞` unconditionally is out of reach of present sieve technology.
  The obstruction is the growth of the sieve dimension against the
  bounded sifting range `z≤x^{1/2}`, plus the linear-sieve parity
  threshold already at `J=2`. It is not the formal-genericity obstruction:
  Lemma 11.3 and Lemma 6.1 show that failure is never
  congruence-forced, so the formal adversary is no help unconditionally.

## 8. What is new relative to POINTWISE_SIZE §11

* Prop 11.4 (SKETCH) becomes Theorem W1, with checked hypotheses. The
  pieces are: the explicit dimension condition; BV with the modulus
  `840d`; the parity step (Lemma 1.2); the `T_2` bound via the uniform
  prime-pair sieve and the `1/φ(m)` Euler product; and the lower bound
  `f(s)≥(e^γ/π)^{1/2}(s−1)^{1/2}`. No gap was found in the sketch.
* Assessment 11.5's "for K=7 (windows 3 and 7, dimension 1) the leftover
  configurations are of the same order as the main term" is now precise.
  This is the K=11 statement: the windows ≤7 failing gives `a_min≥11`. The
  `a_min≥7` in 11.5's wording counts windows `<7`. At BV level the route
  is negative, and Prop 7.2 shows it has margin exactly 0 at level x.
  Route A (sift to `√x` + parity) still wins at level x, which gives W2.
* Lemma 6.1 replaces the heuristic "each window ≥1/2" with a proved
  covering statement that includes F3-type failures.

## Replay

```
export PYTHONPATH=scripts
(ulimit -v 10000000; uv run python scripts/window_w1.py 1e11 300)    # ~20 s; data/pointwise_window/w1_1e11.json
(ulimit -v 10000000; uv run python scripts/window_joint.py 1e11 8)   # ~3 min; data/pointwise_window/joint_1e11_8.json
(ulimit -v 10000000; uv run python scripts/window_joint.py 1e10 8)   # ~15 s
```
Sources: `sources/sieve/teravainen-1611.08585.{pdf,txt}` (semi-linear and
linear sieve statements as used, §6) and `sources/sieve/2504.20289.{pdf,txt}`
(FHRSS, Thm 1.1). Opera de Cribro, Iwaniec 1972/1976 and
Halberstam–Richert are not archived (books or paywalled). Their
statements are taken from the archived secondary source where possible.
