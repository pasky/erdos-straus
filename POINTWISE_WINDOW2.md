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

## 2. The parity barrier for windows, realised by actual primes (Theorem P1)

Sieve axioms (Opera de Cribro ch. 11 style): a sieve method for "window 3
fails" uses as input `X`, the density g, and the counts `|A_d|` for squarefree
`d|P_3(z)` (with `P_3` the primes `≡2 (3)`), `d≤D`, with `Σ_{d≤D}|r_d|` small.
It uses nothing else about A.

**Theorem P1 (PROVED, modulo BV, resp. EH for D>x^{1/2}).** Let
`A^±={p≤x : p≡1 (8), p≡1 (5·7), (p/3)=±1}`. For every squarefree odd d composed of
primes `≡2 (3)`, `|A^±_d|=#{p∈A^±: d|(p+3)/4}=li(x)/(2φ(280)φ(d))+r^±_d`, with the
same main term and `Σ_{d≤x^{1/2}(log x)^{-B}}|r^±_d|≪x/(log x)^A` (BV). Yet:
* `A^−`: `(p+3)/4≡2 (3)`, so it has an odd number of prime factors `≡2 (3)` and is
  never clean. `S(A^−,P_3,x)=0`.
* `A^+`: `S(A^+,P_3,x)≫x/(log x)^{3/2}` (Thm W1).

Hence no argument that uses only the sieve data (at any level D at which both
satisfy the remainder bound, so `D≤x^{1−ε}` under EH) can prove that window 3
fails. A proof must use `(p/3)=+1`, i.e. Lemma 1.2's parity. The same holds jointly for windows
3 and 7 with the four sign classes `((p/3),(p/7))`; three of them have no
both-clean element.
*Proof.* For `p≡1 (8)`, `n_3` is odd, and `n_3≡p·4^{−1}≡p (3)`. By Lemma 1.2 of
POINTWISE_WINDOW, `(−1)^{Ω_3^−(n_3)}=(p/3)`. Conditions mod 8, 3, 35 and `d|n_3`
(i.e. `p≡−3 (d)`, `(d,840)=1`) are independent residue conditions, so BV applies
to both classes with the same main term. ∎

This is Selberg's parity example (`{λ(n)=±1}`) realised by actual primes. The
Liouville function of the bad part is a Dirichlet character of p. That makes the
barrier *removable by a congruence* (which is why W1 holds), but it also makes
parity **necessary** input. §3 asks whether parity is also *sufficient* for two
windows at level 1/2. Answer, in a discrete model: no (Prop 3.7).

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

### 3.4 Composed (tree) block fakes: no gain (EVIDENCE)
Two-block fakes compose. The pieces U and V that one step adds can be split again,
and each further split removes one more unit of target mass. So a true
configuration C carries a *capacity* `cap(C)=max(0, max_{valid U⊔V} 1+cap(U)+cap(V))`,
and a fake exists if `Σ_C μ(C)cap(C)≥τ`. (Correlations still vanish, because
the construction is a sum of Lemma 3.2 fakes; positivity is unaffected, because
the intermediate pieces are added before they are removed.)

The product construction `ν=α⊗μ_7+μ_3⊗β−α⊗β` uses one-window fakes α, β at
levels a, b<1/2 with a+b≥1/2. It is algebraically valid (the visible region
`s_3+s_7≤1/2` is covered by `{s_3≤a}∪{s_7≤b}`, and ν(∅,∅)=0). Expanded, it is
exactly the two-block fake with `U=(P,∅)`, `V=(∅,Q)`. So it is not a new family.

`scripts/window2_treefake.py 2e6 0.02 3 0.5 0.55 0.6` (exact recursion over all
splits; no configuration exceeded 14 points). Results: tree capacity/τ = 0.451
(θ=0.5), 0.239 (0.55), 0.144 (0.6), identical to the two-block ratio. Every
splittable configuration in the sample has cap=1. The extra mass from deeper
trees is zero within sampling, because cap ≥ 2 needs two near-half pairs plus
small points in a single configuration.

**Assessment.** Block-type fakes do not reach the target at θ=1/2. The remaining
question is the full LP (§3.5).

### 3.5 The discretised LP (EVIDENCE, model)
`scripts/window2_lp.py EPS K THETA [--one]` solves the primal LP exactly in a
discretised model. Points lie on K log-spaced bins in `[ε,1]`, with representative
values `g_k` and bin masses `½ln(e_{k+1}/e_k)`. The true law is that of §3.3. The
constraints are all visible correlations, matched exactly. Variables are
rescaled to `ν/μ` and rows to `ρ(S)`. Rows with `ρ(S)=0` (S contained in no
configuration) are dropped.

ε=0.1, K=8, bins at 0.115, 0.154, 0.205, 0.274, 0.365, 0.487, 0.649, 0.866:

| θ | one window: min ν(∅)/τ | two windows: min ν(∅)/τ |
|---|---|---|
| 0.4 | 0 (fake) | — |
| 0.5 | 0.744 | **0 (fake)** |
| 0.6 | 0.828 | **0 (fake)** |
| 0.7 | — | 0.497 |
| 0.75 | — | 0.567 |
| 0.8 | — | 0.728 |

(θ≥0.9: HiGHS reports numerical trouble; not used.) The one-window column
reproduces the model threshold 1/2 (W1). **For two windows the full LP finds a
fake at θ=0.5 and 0.6**, although block fakes reach only 43% of the target mass.
The optimal fake at θ=0.6 removes the target and rearranges one-window
pair configurations (P,∅) and (∅,Q). It does not need (P,Q) mass.

**Grid dependence above 0.6** (min ν(∅)/τ for two windows):

| (ε,K) | (0.2,5) | (0.15,6) | (0.12,7) | (0.1,8) | (0.1,10) |
|---|---|---|---|---|---|
| θ=0.7 | 0.91 | 0.81 | 0.17 | 0.50 | 0.28 |
| θ=0.8 | 0.93 | 0.88 | 0.63 | 0.73 | 0.71 |

At θ=0.5, ε=0.1, K=12 (182329 configurations) the value is again **0**. Above 0.6
the value falls as the grid is refined, but not monotonically. The
discretisation (and the clipped `(1−Σ)^{−1/2}` weight) is coarse, so the
continuum threshold θ_2 of the two-window model is **not** determined. The
data are consistent with θ_2 ≥ 0.6 and do not exclude θ_2 → 1 as ε→0.

*Why two windows are weaker than one (Assessment, partial explanation).* The
window-3 marginal of a fake, `δ_3=Σ_{C_7}δ(·,C_7)`, must be a one-window
zero-correlation measure at level 1/2. Its value at ∅ is
`−τ_3τ_7+Σ_{C_7≠∅}δ(∅,C_7)`. So target mass may be moved to "window 3 clean, window 7 not"
without touching the window-3 marginal at ∅. The window-7 marginal then has to
remove only a fraction `≈P(window 3 clean)` of its clean mass, and its removal budget is
`Σ_{C_3}μ(C_3,C_7)` (all window-3 configurations), not `τ_3μ_7`. As ε→0 that fraction
is `≍ε^{1/2}→0`. This coupling has no one-window analogue. It is
the reason the one-window threshold (1/2) does not carry over. Making it a
continuum construction (handling the mixed correlations) is open. Product
fakes `μ−γ_3⊗γ_7` (Lemma 3.6 below) do *not* realise it.

**Lemma 3.6 (product fakes; Model-PROVED).** Let `γ_q` be window-q signed measures with zero
correlations at levels a and b, `γ_q(∅)=−μ_q(∅)`, and `|γ_q(C)|≤μ_q(C)` for C≠∅.
Then `ν=μ_3⊗μ_7−γ_3⊗γ_7` is a fake at level a+b with ν(∅,∅)=0.
*Proof.* `ρ_{γ_3⊗γ_7}(S)=ρ_{γ_3}(S_3)ρ_{γ_7}(S_7)`, and `s_3+s_7≤a+b` forces `s_3≤a` or `s_7≤b`.
`ν(∅,∅)=τ_3τ_7−τ_3τ_7=0`. Positivity follows from `|γ_3γ_7|≤μ_3μ_7` termwise. ∎
The hypothesis asks for a 2-bounded one-window fake (`0≤μ+γ≤2μ`). In the
coarse grid (ε=0.1, K=8), `--one --cap=2` gives min ν(∅)/τ = 0.45, 0.54, 0.63
at a = 0.2, 0.25, 0.3. So no 2-bounded fake exists there, and the LP fakes of
§3.5 are not of product type.

### 3.7 Certified fake at θ=1/2 in the discrete model (CERTIFIED, floating point)
Pipeline: `window2_feas.py` (L∞-residual feasibility LP with ν(∅)=0), then
`window2_polish.py` (NNLS on the LP support, giving a square 89×89 system), then
`window2_verify.py`. The verifier is independent: it rebuilds bins, weights and
parity, and recomputes every visible correlation by brute force.
For ε=0.1, K=8, θ=0.5 (12769 configurations, 89 visible correlations):
ν≥0, **ν(∅,∅)=0**, max relative correlation residual **2.6·10⁻¹⁵**. The
support has 89 configurations, all with `ν/μ≥0.154`, so the solution is
interior and robust under small perturbations of the data. Total removed
true mass is 3.15τ. Some configurations carry up to 9.3·10⁴ times their true mass. (The
model has no capacity bound; for integers the available capacity is ≍log x
times the prime mass, so realisability as an integer sequence would need this
factor to stay bounded. Not checked.) Dump: `data/window2/fake_eps0.1_K8_theta0.5.json.gz`.
θ=0.6: the LP is feasible to residual 5·10⁻⁴, but the polish stalls at
1.5·10⁻⁴ (not certified). θ=0.7: infeasible (best residual 4.2%).

**Proposition 3.7 (discrete model; CERTIFIED).** In the discrete 𝒯𝒫(1/2) model with
ε=0.1, K=8, the Type-I correlations of level 1/2 together with the parity of both
windows do not imply that any configuration has both windows clean. In the
same model the one-window LP gives min ν(∅)/τ=0.744>0 at θ=1/2. So one
window is decided by Type-I + parity at level 1/2 and two windows are not.
