# POINTWISE_WINDOW — unconditional Ω-results for the window statistic `a_min(p)`

Task O10. Builds on `POINTWISE_SIZE.md` §§8–11 (window frame, Lemma 8.2,
Cor 8.3, Prop 8.4, Lemma 11.3, Prop 11.4, Assessment 11.5).
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. **Cited** = external theorem whose statement we read (in the
source or in an archived secondary source), proof not re-checked.

Status: IN PROGRESS (sections are added one at a time).

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
