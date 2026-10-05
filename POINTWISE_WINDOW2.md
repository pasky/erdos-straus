# POINTWISE_WINDOW2 — two windows (`a_min(p)≥11`) beyond EH; the parity question as a theorem

Task O29 (branch `side-agent/window-parity`). Builds on `POINTWISE_WINDOW.md`
(Thm W1, Thm W2, Lemma 1.2, §§6–7) and `POINTWISE_SIZE.md` §§8–11.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
**Model-PROVED** = proved inside an explicitly defined axiomatic model (§3),
not a statement about the primes.

Status: in progress.

## 0. Results at a glance

(filled in at checkpoint)

## 1. Exact form of the two-window problem

Throughout, p is a Mordell-hard prime, so `p≡1 (24)` and `(p/3)=(p/7)=+1`
(the six Mordell classes mod 840 are squares mod 3, 7 and 8).
`n_3=(p+3)/4`, `n_7=(p+7)/4`, so **`n_7=n_3+1`** (consecutive integers; in
particular `gcd(n_3,n_7)=1`).

**Lemma 1.1 (PROVED).** For hard p, `a_min(p)≥11` iff windows 3 and 7 both fail.
Window 3 fails iff `n_3` has no prime factor `≡2 (3)` (POINTWISE_WINDOW §1).

**Lemma 1.2 (norm-form reformulation; PROVED).** For hard p the F1-failure of
both windows ("both clean") is equivalent to: `n_3` is primitively represented by
`a²+ab+b²` and `n_3+1` is primitively represented by `c²+cd+2d²`.
So "both clean" ⟺ `p=4n−3` with `(n, n+1)` a pair of consecutive integers
which are norms of primitive elements of `Z[ω]` and `Z[(1+√−7)/2]`, i.e. an
integral point of the quaternary quadric
`c²+cd+2d² − (a²+ab+b²) = 1` with `4(a²+ab+b²)−3` prime.

*Proof.* Both fields have class number 1. A prime r is inert in `Q(√−3)` iff
`r≡2 (3)` (including r=2), and inert in `Q(√−7)` iff `(r/7)=−1` (2 splits since
`−7≡1 (8)`). A positive integer coprime to the discriminant is a primitive norm
iff it has no inert prime factor. `3∤n_3` and `7∤n_7` because `p≡1 (21)`. ∎

This is exactly the shape of Friedlander–Iwaniec's hyperbolic PNT (FI09,
archived now: `sources/window2/fi09-hyperbolic-pnt.{pdf,txt}`), where
`p∓2` are sums of two squares, i.e. `x_1²+…+x_4²=p` on the quadric
`x_1x_4−x_2x_3=1`. FI09's lower bound needs level `θ<1` close to 1;
Sedunova 2026 (arXiv:2609.28200, archived) confirms it is still open
unconditionally and gets only `P_7` (square-free distances, ≤7 prime
factors) from the unconditional level `x^{1/6}` of `r(n−2)r(n+2)`.
The best unconditional "one complete absence + one almost-prime" result is
Nath–Xie (arXiv:2501.16723, archived): `p=m²+n²+1` with `Ω(p+2)≤9`, by a
semi-linear × linear vector sieve.

## 3. The Type-I + parity model 𝒯𝒫(θ) and fake sequences

### 3.1 Definition
A *configuration* is `C=(B_3,B_7)`, where `B_q` is the multiset of log-sizes
`t=log r/log x` of the q-bad prime factors of `n_q`. *Parity* means that `|B_3|` and
`|B_7|` are even (POINTWISE_WINDOW Lemma 1.2: this is a congruence fact for hard p).
The information of level θ is the set of correlation functions
`ρ(S)=E[#embeddings of S into C]` for all `S=(S_3,S_7)` with `ΣS≤θ`. These are
exactly the Type-I data `|A_{d_1d_2}|`, `d_1|n_3`, `d_2|n_7` bad squarefree, `d_1d_2≤x^θ`.
A *fake* is a nonnegative measure ν on parity configurations with the same ρ(S)
for `ΣS≤θ`. **Model statement:** Type-I + parity at level θ cannot prove
"both clean" if some fake ν has `ν(∅,∅)=0`.

### 3.2 Two-block fakes (Lemma 3.2, Model-PROVED)
Let `U,V` be disjoint nonempty configurations, each even in each window, with
`min U+min V>θ`. Then `δ=−[∅]−[U⊔V]+[U]+[V]` has `ρ_δ(S)=0` for every S with `ΣS≤θ`.
*Proof.* Take `S⊂U⊔V`. If `S=∅` the contribution is `−1−1+1+1=0`. If `∅≠S⊂U`
(or `⊂V`) it is `−1+1=0`. If S meets both U and V, then `ΣS≥min U+min V>θ`, so S
is outside the level. ∎
Hence, if the true law μ satisfies `R(θ):=μ{C≠∅ : C θ-splittable} ≥ τ:=μ(∅,∅)`,
a fake with no clean element exists. (Remove τ of target mass, and remove
splittable C up to its true mass. Add U and V; adding is unconstrained.) Here C is
*θ-splittable* if `C=U⊔V` as in the lemma. The optimal split puts `c_1=min C` in
U and takes for V the two largest points of one window (Lemma 3.3: any V has
two points in some window, so `min V≤` that window's second largest).

*Trivial range (Model-PROVED).* For θ<1/2, a single window already admits
`U={a,b}` with `a,b∈(θ,1−θ)`. So a fake exists even for one window. For θ≥1/2 the
one-window block fakes are impossible: four points with `min U+min V>1/2`
would have sum >1. This matches W1 (one window at BV level).

### 3.3 The true law and the MC (EVIDENCE, preliminary)
Heuristic true law for one window (bad primes ≥ x^ε, clean weight 1):
density `∏(1/2t_i)·(1−Σt)^{−1/2}` (half the primes are bad, by Mertens; the
clean cofactor contributes `(log x^{1−Σt})^{−1/2}`). The two windows are
taken as independent. `scripts/window2_blockfake.py 2e6 0.02 1`:

| θ | 0.40 | 0.45 | 0.50 | 0.55 | 0.60 | 0.70 | 0.80 |
|---|---|---|---|---|---|---|---|
| R(θ)/τ | 1.53 | 0.83 | **0.42** | 0.24 | 0.13 | 0.04 | 0.007 |

ε-stability (4·10⁶ samples, seed 2):

| ε | P(clean,clean) | θ=0.40 | 0.45 | **0.50** | 0.55 | 0.60 | 0.70 |
|---|---|---|---|---|---|---|---|
| 0.05 | 0.114 | 0.98 | 0.63 | **0.40** | 0.23 | 0.13 | 0.04 |
| 0.02 | 0.045 | 1.53 | 0.83 | **0.42** | 0.24 | 0.13 | 0.04 |
| 0.01 | 0.023 | 2.27 | 1.05 | **0.48** | 0.28 | 0.19 | 0.05 |
| 0.005 | 0.011 | 3.35 | 1.30 | **0.42** | 0.22 | 0.14 | 0.06 |

For θ<1/2 the ratio grows as ε→0, as the trivial range predicts. For θ≥1/2 it is
stable within the Monte Carlo noise; the weight `(1−Σt)^{−1/2}` has a heavy
tail. At θ=1/2, R/τ≈0.43±0.05.
So at BV level (θ=1/2), two-block fakes remove only ≈43% of the target mass. They
do **not** give an obstruction there. The ε-stability and multi-block fakes
(m blocks, `Σ min U_j>θ`) are still to be checked. If no fake exists at θ=1/2,
the LP dual is a Type-I sieve at BV level, i.e. a candidate unconditional route
to Goal 1.
