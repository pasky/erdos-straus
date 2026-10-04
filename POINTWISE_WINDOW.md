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
  `c_f=2(e^γ/2π)^{1/2}>0` (from `∫_1^s ≥ ∫_1^s dt/(2(t−1))^{1/2}·…`; precisely
  `t(t−1)≤2(t−1)` on `[1,2]`, so `∫_1^s dt/√(t(t−1)) ≥ √2·√(s−1)`, and `s≤2`).
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
