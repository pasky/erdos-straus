# POINTWISE_WINDOW2 — two windows (`a_min(p)≥11`) beyond EH; the parity question as a theorem

Task O29 (branch `side-agent/window-parity`). Builds on `POINTWISE_WINDOW.md`
(Thm W1, Thm W2, Lemma 1.2, §§6–7) and `POINTWISE_SIZE.md` §§8–11.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
**Model-PROVED** = proved inside an explicitly defined axiomatic model (§3),
not a statement about the primes.

Status: checkpoint 1 (2026-10-05), not yet reviewed.

## 0. Results at a glance

| # | statement | label |
|---|---|---|
| Lemma 1.2 | both windows F1-clean ⟺ `n,n+1` are primitive norms from `Q(√−3)`, `Q(√−7)` (an FI09-type quadric) | PROVED |
| Thm P1 (§2) | the sign classes `(p/3)=±1` have identical sieve data, and `−1` never has window 3 clean: parity is necessary. Jointly only `(+,+)` vs `(+,−)` (not all four classes; R29 M1) | PROVED (mod BV/EH) |
| Lemma 3.2, 3.6 | two-block and product fakes in the Type-I+parity model 𝒯𝒫(θ) | Model-PROVED |
| §3.2 | one window: fakes for θ<1/2; no block fake at θ=1/2 | Model-PROVED |
| §3.3–3.4 | block/tree fakes reach only ≈40–45% of target at θ=1/2 | EVIDENCE (MC; infinite-variance estimator, no error bar — R29 m3) |
| Prop 3.7 | two windows: a fake with no both-clean mass at θ=1/2 (discrete model) | CERTIFIED (residual 2.6e-15) |
| §3.5 | discrete model ε=0.1, K=8: one-window min ν(∅)/τ ≥0.744128 at θ=1/2; two-window threshold θ_2∈(0.5,0.7] | CERTIFIED (reviewer exact duals, R29 m6; model only) |
| §3.5 | same grid: θ_2∈(0.6,0.7] | EVIDENCE (θ=0.6 fake uncertified) |
| §6.1 | bounded reweighting of primes (ν≤Cμ, C≥3.5) still admits the fake (discrete model of a coarse heuristic law; model indication only, not about primes) | EVIDENCE (residual ≤1e-9) |
| §6.2 | switching caps ν≤Kμ on large-prime configurations restore positivity at θ=1/2 iff K≲2–3 (model indication only; per-configuration caps are stronger than real switched bounds, R29 m4) | EVIDENCE (coarse grid) |
| §6.3 | slice-separable fakes cannot reach the target; the fake is genuinely mixed-level | Model-PROVED reduction; separable-LP min 0.430>0 on the grid (EVIDENCE, R29 m1) |
| §4 | Goal 1 (unconditional `a_min≥11`) not reached; routes (ii), (iv), (v) closed, (i) open | Assessment |

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

**Theorem P1 (PROVED; the "parity necessary" half uses only BV — a theorem — resp. EH for
D>x^{1/2}; only the `A^+` lower bound inherits Thm W1's "modulo S1–S3").** Let
`A^±={p≤x : p≡1 (8), p≡1 (5·7), (p/3)=±1}`. For every squarefree odd d composed of
primes `≡2 (3)`, `|A^±_d|=#{p∈A^±: d|(p+3)/4}=g(d)·li(x)/(2φ(280))+r^±_d` with `g(d)=1/φ(d)` for `5∤d` and
`g(d)=0` for `5|d` (since `p≡1 (5)` gives `n_3≡1 (5)`; as in W1), i.e. the
same main term and `Σ_{d≤x^{1/2}(log x)^{-B}}|r^±_d|≪x/(log x)^A` (BV). Yet:
* `A^−`: `(p+3)/4≡2 (3)`, so it has an odd number of prime factors `≡2 (3)` and is
  never clean. `S(A^−,P_3,x)=0`.
* `A^+`: `S(A^+,P_3,x)≫x/(log x)^{3/2}` (Thm W1).

Hence no argument that uses only the sieve data (at any level D at which both
satisfy the remainder bound, so `D≤x^{1−ε}` under EH) can prove that window 3
fails. A proof must use `(p/3)=+1`, i.e. Lemma 1.2's parity.

*Joint version (restricted after review R29, M1).* For windows 3 and 7 jointly,
the four sign classes `((p/3),(p/7))` do **not** all have identical joint sieve data:
3 is window-7 bad (`(3/7)=−1`) and `3|n_7=(p+7)/4` for *every* p with `(p/3)=−1` and for
*no* p with `(p/3)=+1`, so `|A_{d_1·3}|` separates `(p/3)=−1` from `+1`. The joint
barrier holds only for the pair `(+,+)` vs `(+,−)` (sets `{p≤x: p≡1 (8), p≡1 (5), (p/3)=+1,
(p/7)=±1}`): these have identical joint data
`|A_{d_1,d_2}|` (main terms equal by the same BV argument; `3∤n_7` and `5∤n_3n_7` in both),
and `(+,−)` has no both-clean element since `(−1)^{Ω_7^−(n_7)}=(p/7)`. (Reviewer
check `scripts/review_w2_p1joint.py 3e6`: same zero pattern at `3|d_2`, `5|d_2`, noise-level
differences elsewhere; (+,−): 0 both-clean of 3417.)
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

*Trivial range (Model-PROVED).* For θ<1/2, a single window already admits the
fake `δ=−[∅]+[{a,b}]` with `a,b>θ` and `a+b<1` (each nonempty S⊂{a,b} has ΣS>θ).
This is not an instance of Lemma 3.2 (there V=∅). So a fake exists even for one window. For θ≥1/2 the
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
roughly stable across runs; the weight `(1−Σt)^{−1/2}` has a heavy
tail. At θ=1/2, R/τ≈0.4–0.45 across runs. *No error bar is claimed (R29 m3):* the weight
`(1−Σt)^{−1/2}` has infinite second moment (`∫(1−s)^{−1}ds` diverges), so the MC estimator
has infinite variance and a "±0.05" is not statistically valid (reviewer reruns at θ=0.4 swing
1.46–3.48 across seeds). These MC numbers are rough indications only; they are superseded by
the exact discrete LP of §3.5.
So at BV level (θ=1/2), two-block fakes remove only roughly 40–45% of the target mass (MC indication). They
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
is positive at θ=1/2 on this grid (a model fact; it is *not* derived from W1, which uses
switching — R29 M3).

*Certified values (R29 m6).* The reviewer's `scripts/review_w2_lp.py` (own model build,
HiGHS, then an **exact rational dual-feasibility check**, ρ to 40 digits; a dual y with
`Σ_S y_S emb(S,C) ≤ [C=∅]` for all C proves `ν(∅) ≥ y·ρ` for every fake) gives CERTIFIED lower
bounds on this grid: one window θ=0.5: **≥0.744128**; θ=0.6: **≥0.827541**; two windows
θ=0.7: **≥0.497087**; θ=0.8: **≥0.728369**. The two-window θ=0.6 fake is *not* certified
(the 203-column support re-solved at 40 digits has negative entries). Since visible sets grow
with θ, min ν(∅)/τ is nondecreasing in θ; with Prop 3.7 this makes θ_2∈(0.5,0.7] CERTIFIED
on the grid ε=0.1, K=8, while θ_2∈(0.6,0.7] remains EVIDENCE. **For two windows the full LP finds a
fake at θ=0.5 and 0.6**, although block fakes reach only ≈40–45% of the target mass (MC).
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
same model the one-window LP gives min ν(∅)/τ≥0.744128>0 at θ=1/2 (CERTIFIED by the
reviewer's exact dual, R29 m6). So *in this discrete model* one window is decided by
Type-I + parity at level 1/2 and two windows are not. (This is not a statement about W1,
which uses switching; R29 M3.)

**Scope of Prop 3.7 (R29 M2, M4).** Prop 3.7 is a statement about a discrete model only:
* *Coarse heuristic law.* The "true law" μ is the heuristic law of §3.3 (independent
  windows, Mertens density, clean weight `(1−Σt)^{−1/2}`), discretised on 8 bins with ε=0.1.
  It is not derived from the primes.
* *ε=0.1 is far from the regime.* At ε=0.1 the model's own normalised one-window correlations
  `r(S)=ρ_μ(S)/(∏w_k^{S_k}/S_k!)/ρ_μ(∅)` range over [0.82, 1.87] and differ between the even
  and odd laws (e.g. single point at bin 0.115: 1.349 vs 1.081; reviewer
  `scripts/review_w2_rhocheck.py`). For actual primes BV + fundamental lemma give `r(S)≈1`
  independent of parity (Thm P1). So the model's Type-I data partly encode parity and differ
  from real sieve data by up to ~90%. Refinement does not fix this within reach (spreads
  [0.71,1.76] at ε=0.07, K=9; [0.82,1.64] at ε=0.05, K=10). Every θ=1/2 computation in this
  document uses ε=0.1. A reviewer LP at ε=0.07, K=9 returns min 0 only with ν/μ≤10³ at relative
  residual 3.4·10⁻⁴ (EVIDENCE of the weakest kind, uncertified).
* *Bad-prime data only.* The model contains only the counts `|A_{d_1d_2}|` for *bad*
  squarefree `d_1d_2≤x^{1/2}`. Real BV-level Type-I data also include good and mixed d. The fake
  reweights configurations with different cofactor sizes `1−Σt`, so it is **not** shown to
  match those data.

Hence the relevance of Prop 3.7 to actual sieve methods is EVIDENCE of the weakest kind.

## 4. Goal 1 routes (i)–(v): status

Unconditional `a_min≥11` for infinitely many hard p was **not** reached. Route by route:

* **Sieves whose only inputs are `|A_{d_1d_2}|` for bad squarefree `d_1d_2≤x^{1/2}`, the
  parities and the total mass:** blocked in the discrete model ε=0.1, K=8 (coarse heuristic
  law) by Prop 3.7. This does not cover sieves that use good or mixed d (not in the model),
  and ε=0.1 is far from the asymptotic regime (§3.7 Scope; R29 M2, M4). A proof must use information outside
  𝒯𝒫(1/2). Such information includes primality of p in a switched variable (W1's `T_2`
  bound uses it, and so does W2's `T^{(q)}`), Type-II sums, or level >1/2.
  (The model statement is CERTIFIED only for the grid ε=0.1, K=8; the
  continuum version is an Assessment.)
* **(ii) Level beyond 1/2 for well-factorable weights** (BFI; Maynard 2020; Lichtman).
  These results need a *fixed* residue class a. The two-window remainders
  involve `p≡−3 (d_1)`, `p≡−7 (d_2)`, i.e. the class `CRT(−3,−7) mod d_1d_2`. This is
  not fixed (equivalently `n_3≡0 (d_1)`, `n_3≡−1 (d_2)` for consecutive `n_3, n_3+1`).
  Moreover, the model LP is still 0 at θ=0.6 (grid, uncertified) and positive only
  from θ≈0.7 in the coarse grid. Even a level of 3/5 for the right weights
  would not suffice in the model. Window 3 *alone* has the fixed class a=−3, so one-window
  data beyond 1/2 are a priori available; reviewer mixed-level test (R29 m7, `review_w2_lp.py
  --onewin=T_1`: joint data at level 1/2 plus one-window data `(S_3,∅)`, `(∅,S_7)` up to T_1):
  T_1=0.55, 0.6 → fake persists (min 0, primal uncertified); T_1=0.7 → CERTIFIED ≥0.16298.
  So at BFI/Maynard-type levels (≤3/5) the model obstruction persists on the grid (EVIDENCE;
  same ε=0.1 caveats as §3.7). **Assessment: closed** (in the model).
* **(i) Bilinear/Type-II input.** The sequence `r_{−3}(n)r_{−7}(n+1)` (§1) is the
  window analogue of Sedunova's `r(n−2)r(n+2)`. Only its Type-I level `x^{1/6}` is
  known there, and no Type-II estimate is known. A Chen-type switch would need BV for the
  F1-clean-weighted sequence in the switched variable, a level-1/2 statement about a
  half-dimensional sifted set. That is not available. **Assessment: open, no foothold found.**
* **(iii) Smaller-dimension sifted sequence.** Not applicable: `a_min` is defined
  at primes, and ES reduces to primes. Sedunova-type relaxations (almost-prime p)
  say nothing about ES.
* **(iv) Maynard–Tao.** It produces several primes, each satisfying *one* condition.
  "p and p+24 both window-3-clean" gives windows 3 and 27 of p (same character
  χ_{−3}), not windows 3 and 7. No admissible-tuple trick turns two characters
  on one prime into one character on two primes, because window q's sifting set
  depends on q. **Assessment: closed.**
* **(v) Sub-families / smooth moduli.** A congruence class fixes only the
  divisibility of `n_q` by the primes of the modulus (POINTWISE_WINDOW §6,
  PROVED for fixed moduli). A class-of-one modulus `L≤p^c` (Linnik/Chang/
  Thorner–Zaman) leaves cofactors `((b+q)/4+(L/4)k)/A_q` that face the same
  two-condition problem in a progression, with less level. **Assessment: closed.**

**Goal 3** (`a_min≥15`) was not attempted, since Goal 1 failed.

## 5. Goal 2: what is proved about the parity obstruction

1. **Parity is necessary** (Theorem P1, PROVED modulo BV/EH, actual primes):
   sieve data cannot distinguish `(p/q)=+1` from `(p/q)=−1`, and in the second
   case window q never fails by F1.
2. **One window** (two separate statements; R29 M3).
   (a) *Actual primes:* window 3 fails for ≫x/(log x)^{3/2} hard p (Thm W1, PROVED modulo the
   cited sieve theorems). W1 uses Type-I data at level 1/2, parity **and switching** (its `T_2`
   bound applies the prime-pair upper sieve S2 to `p=4mr_1r_2−3`). So W1 is *not* evidence that
   Type-I + parity alone suffices for one window.
   (b) *Model:* for θ<1/2 there are explicit one-window fakes (Model-PROVED, §3.2); no block fake
   exists at θ=1/2 (Model-PROVED); on the grid ε=0.1, K=8 the one-window LP at θ=1/2 is positive,
   min ν(∅)/τ≥0.744128 (CERTIFIED by the reviewer's exact dual, model only). The continuum
   statement "the one-window threshold in 𝒯𝒫(θ) is exactly 1/2" is unproved at θ=1/2.
3. **Parity is not sufficient for two windows at level 1/2** (Prop 3.7,
   CERTIFIED in the discrete model ε=0.1, K=8). Mechanism: the window marginals
   couple (§3.5). Two-block and product fakes (Lemmas 3.2, 3.6, Model-PROVED)
   do *not* suffice; the LP fake is genuinely joint. This is a discrete-model statement
   about a coarse heuristic law whose own Type-I data are far from those of the primes at
   ε=0.1 (§3.7 Scope; R29 M4).
4. **Where the two-window threshold lies:** in the coarse model θ_2∈(0.6,0.7]
   (the bracket (0.5,0.7] is CERTIFIED on the grid, the sharper (0.6,0.7] is EVIDENCE;
   grid-dependent, decreasing under refinement at θ=0.7). W2 reaches
   two windows at `θ=1−ε_0`, but only by using primality (switching), which is
   outside the model.

So the window obstruction is not Selberg's parity barrier itself; that one is
removed by the congruence (Lemma 1.2). It is a **parity-constrained
vector-sieve barrier**: Type-I data at level 1/2, even with both parities, does
not determine joint cleanliness (discrete model only; see the caveats below). In the model, no lower-bound
sieve can give `a_min≥11` if its only inputs are the bad-prime counts
`{|A_{d_1d_2}|: d_1d_2 bad squarefree, d_1d_2≤x^{1/2}}`, the parity congruences and the total mass.
This covers β-sieves, vector sieves, Buchstab iterations without switching,
and the Bonferroni-with-parity subtraction of POINTWISE_WINDOW §7.2.

*Caveats (R29 M2, M4).* "In the model" means: one discrete grid (eps=0.1, K=8) of a coarse
heuristic law, whose own Type-I data deviate from product form by up to ~90% and depend on
parity, unlike the real data of Thm P1 (see "Scope of Prop 3.7"). Sieves using Type-I data
for good or mixed d are not covered. Nothing here is proved about sieve methods on actual
primes; the transfer from the model is EVIDENCE of the weakest kind.

## Replay
```
export PYTHONPATH=scripts
uv run python scripts/window2_blockfake.py 2e6 0.02 1                 # §3.3, ~1 min
uv run python scripts/window2_treefake.py 2e6 0.02 3 0.5 0.55 0.6      # §3.4, ~3 min
uv run --with scipy python scripts/window2_lp.py 0.1 8 0.5 --one       # §3.5 one window (0.744)
uv run --with scipy python scripts/window2_lp.py 0.1 8 0.5             # §3.5 two windows (0)
uv run --with scipy python scripts/window2_feas.py 0.1 8 0.5 --dump=/tmp/f.json
uv run --with scipy python scripts/window2_polish.py 0.1 8 0.5 /tmp/f.json /tmp/p.json
uv run python scripts/window2_verify.py /tmp/p.json                    # §3.7 residual ~1e-15
```
(Run each under `ulimit -v 8000000`. The ε=0.1, K=12 LP needs ~4 GB.)

## 6. Adding primality information to the model (step 2 of the follow-up)

### 6.1 Capacity: does it matter if the fake is supported on integers / on primes?
*Integers.* In the heuristic law the configuration distribution of `(n_3,n_7)` is
the same for random integers n and for primes p; the densities differ by the uniform
factor log x. So an integer capacity `ν≤C·μ_int=C(log x)μ` is vacuous as x→∞.
**This constraint does not restore positivity** (Assessment, immediate from the model).

*Primes with bounded weights.* The fake must be a reweighting of the primes,
`0≤ν≤Cμ` with C fixed (`window2_lp.py 0.1 8 0.5 --cap=C`):

| C | 2 | 2.5 | 3 | 3.5 | 4 | 5 | 10 | 10³ |
|---|---|---|---|---|---|---|---|---|
| min ν(∅)/τ | 0.373 | 0.207 | 0.078 | **0** | 0 | 0 | 0 | 0 |

The cap-5 fake was checked by `window2_verify.py`: residual 6.9·10⁻⁷,
max ν/μ = 5, ν(∅)=0. **So, in the discrete model, already a reweighting of the model's true law with weights ≤3.5
satisfies all of the model's level-1/2 bad-prime Type-I data and both parities and has no
both-clean mass** (discrete model "true law" = coarse heuristic law at eps=0.1, K=8; EVIDENCE,
LP residual ≤10⁻⁶). The threshold is
C*∈(3,3.5) on this grid. This is a model indication only, not a statement about
primes (R29 M2, M4; see "Scope of Prop 3.7"). In the model, "bounded-weight reweighting" is
therefore not enough information. The useful primality information must be *structural*:
it is the switched sieve (§6.2), not a size bound.

*Numerical robustness note.* `window2_lp.py` passes HiGHS rescaled entries
`emb·μ(C)/ρ(S)`, and some of these fall below HiGHS's `small_matrix_value`, so they are silently
dropped. `window2_feas.py` now normalises columns. With `--bisect` it finds the minimal
`ν(∅)/τ` at which an L∞ relative residual ≤10⁻⁹ is attainable. It re-confirms every number above:
one window 0.744 (θ=.5) and 0.828 (θ=.6); two windows 0 (θ=.5), **0 (θ=.6, now with
residual ≤10⁻⁹)**, 0.497 (θ=.7); cap=2: 0.373; cap≥3.5: 0. The unbounded θ=0.5 fake
is now found directly with residual 1.3·10⁻¹⁵.

### 6.2 Switching as configuration caps
W1's `T_2` and W2's `T^{(q)}` bound configurations with a large prime r by sifting
r (and `p=ar−q`) *as primes*. In the model, this is an upper bound `ν(C)≤K·μ(C)` on
configurations C that have a point (prime factor) of size `≥x^α`. K is the
constant of the switched upper-bound sieve; K=1 would be a perfect upper bound.
`window2_feas.py 0.1 8 0.5 --swcap=K:α --bisect` gives min ν(∅)/τ:

| α \ K | 1 | 2 | 3 |
|---|---|---|---|
| 0.6 | 0.459 | 0.111 | 0 |
| 0.45 | 0.801 | 0.173 | 0 |
| 0.3 | 0.965 | 0.250 | 0 |

**So positivity at θ=1/2 does come back in the model once primality enters as a
switched upper bound, but only if that bound is within a factor ≈2–3 of the truth
on large-prime configurations** (EVIDENCE, coarse grid, uncertified bracket
width 2.4·10⁻⁴). For comparison, the simplest switched problem is a prime-pair count
`#{r: ar−q prime}` (dimension 2, level `y^{1/2}`). Its best known upper constant is about
3.4 times the Hardy–Littlewood value (Chen/Wu-type twin-prime constants, recalled, not
re-checked), which is just on the wrong side of K≈3. The switched problems here
also carry the other window's half-dimensional condition, and a *configuration*
(not just a sifting) condition on the remaining factors. **Assessment:** an
unconditional two-window proof along "Type-I at BV + parity + switching" needs
switched upper bounds that are sharper than current twin-prime technology,
uniformly over configurations. This is a quantitative, not a qualitative,
barrier in the model. The caps here act on bins of a coarse grid, so the
thresholds K≈2–3 are indicative only.

*Direction of the comparison (R29 m4).* A per-configuration cap (nu(C) at most K times mu(C)
for each single configuration C) is *stronger* information than a switched upper-bound sieve on
actual primes provides: such a sieve bounds aggregates over families of configurations, not each
configuration. So for realistic (aggregate) caps the required K is at most as large as the
per-configuration values found here (2 to 3), and possibly no K works at all. The comparison
with the twin-prime constant is heuristic. All K and C thresholds in sections 6 and 7 are model
indications on one coarse grid (eps=0.1, K=8) of a heuristic law, not statements about primes
(R29 M2, M4).

### 6.3 Toward an analytic description of the joint fake (partial; step 3)
*Shape of the certified θ=1/2 fake* (`data/window2/fake_eps0.1_K8_theta0.5.json.gz`).
It removes the target (−1·τ) and true mass on one-sided pair configurations
`(P,∅)` and `(∅,Q)` (each ≈0.04–0.05τ). It adds mass on other one-sided pairs
(up to `ν/μ≈10`) and a little on two-sided configurations, e.g. `({.205,.649},{.115,.866})`.
These configurations carry points >1/2, which are invisible individually.

*Slice reduction (Model-PROVED algebra).* Write `δ=Σ_Q δ(·,Q)⊗[Q]`. A sufficient set of
conditions for zero visible correlations is:
1. every window-3 slice `δ(·,Q)` has zero correlations for all nonempty `S_3` with `s_3≤1/2`;
2. the slice totals `m(Q)=Σ_Pδ(P,Q)` form a window-7 measure with zero correlations
   at level 1/2, total mass included.

The slice `Q=∅` contains the target entry −1. By the one-window LP (ε=0.1, K=8)
its non-clean part can add at most 0.256, so `m(∅)≤−0.744`. Positive `m(Q)` are free
(add mass at `(∅,Q)`). (R29 m1: the earlier prose chain here "negative ones cost at most 1.256μ_7(Q); homogeneity then caps Σ_{Q≠∅}m(Q) at 0.256·1.256≈0.32" was not
derived and is withdrawn.) Instead, the reviewer solved the full slice-separable LP
(conditions (1)+(2), ν≥0; `scripts/review_w2_slice.py 0.1 8 0.5`): **min ν(∅,∅)/τ = 0.430 > 0**
(EVIDENCE: primal LP on the grid ε=0.1, K=8, no dual certificate). It also confirms
`m(∅)≤−0.744` (max one-window non-clean total with ν'(∅)=0 is `μ_tot−0.74413`).
**So slice-separable fakes cannot work on this grid.** The certified fake uses the weaker
mixed conditions: for `S_7≠∅` the window-3 level is only `1/2−s_7`, so slices whose Q
has visible points need fewer zero correlations. This is the precise sense in
which the fake is "joint". A closed-form continuum construction exploiting
it was **not** obtained. The continuum model theorem (fake at θ=1/2 for ε→0)
remains open; Prop 3.7 is the strongest statement proved.

## 7. Switching on actual primes: the required constant versus known ones (started)

### 7.1 Translation of the §6.2 caps (Assessment, with one new number)
A §6.2 cap applies to a configuration in which some `n_q` has a q-bad prime `r≥x^α`,
`n_q=m·r` with m in a prescribed class. On primes, the cap means an upper bound for
`#{r∈I prime : 4mr−q prime}` (plus the other window's sifting conditions on
`mr+(q'−q)/4`), summed over m. That is a Chen-type switched prime-pair count in the variable r.
With BV in r (level `(x/m)^{1/2}`) and the linear upper sieve, the bound is
**4×** the Hardy–Littlewood main term. Wu-type weighted switching (Chen's method;
Wu 2004 for twin primes, ≈3.39–3.40×; recalled, not re-checked) is the best known.

Required constant (coarse grid ε=0.1, K=8, θ=1/2, α=0.6; `window2_feas.py
--swcap=K:0.6 --v=0`): feasible fake (no positivity) at **K=2.75** (residual
4·10⁻¹⁶). Infeasible at K=2.5 (residual 1.6·10⁻³) and K=2.25. So
**K*∈(2.5,2.75]**, while the best known switched prime-pair constant is ≈3.4. The
numerical gap is a factor ≈1.25–1.35, under the generous assumption that the caps
need hold only *bin-wise* and only on configurations with a prime factor ≥x^{0.6}.
The real switched counts also carry the other window's half-dimensional
conditions, which makes them no easier. **No unconditional `a_min≥11` follows.**
Not done (context limit): the K*(α) curve for α<0.6, a finer grid, and a check
of the exact Wu constant in the source.
