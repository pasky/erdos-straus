# POINTWISE_WINDOW3 — Chen–Wu switching for two windows (`a_min(p)≥11`): a faithful model

Task O39 (branch `side-agent/window-switching`). Builds on POINTWISE_WINDOW2.md
(model 𝒯𝒫(θ), Prop 3.7, §6.2 caps, §7.1) and POINTWISE_WINDOW.md (W1, W2).
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment;
Model-PROVED / Model-CERTIFIED = inside the discrete model of WINDOW2 §3.

Status: checkpoint 1 (2026-10-05), not yet reviewed. Report: `reviews/agent-reports/AGENT_REPORT_O39.md`.

## 0. Results at a glance

| # | statement | label |
|---|---|---|
| §1 | a real switched sieve gives *aggregate* family bounds (marginal caps SW_K; with extra sifting of the other window: families F(q,C_q,Z)), not per-configuration caps | Assessment (derivation) |
| §2 | continuum heuristic law is parity-blind (≤0.3%); R29-M4 spread was a binning artefact; cell-integrated law repairs it | EVIDENCE (quadrature) |
| §3 | marginal caps need K*∈(1.07,1.1) (ε=0.1,K=8) | EVIDENCE |
| §4.1 | real family constants K(ζ)=4 (ζ=ε), 8.1–14.7 for ζ≥0.133 (composed linear×semi-linear upper sieves) | Assessment (computation) |
| §4.2, §8 | uniform prefix-family constant needed: K*∈(2,2.5) on (0.1,8); K*≤2.5 on (0.1,10), (0.1,12), (0.07,9); (2.5,3] with outer visibility | EVIDENCE |
| Prop 8.1 | fakes with all *prefix*-family bounds at K=2.5 (and 3, 4) | EVIDENCE, 50-digit verified (ε=0.1,K=8; not interval arithmetic) |
| §5 | best switched constants: 4 (BV), 3.91 (Chen/Wu double sieve), 3.3996 (twins, BFI levels); ≥2 at any level | checked in Wu 2004 |
| §6–7 | good-prime Type-I data: frozen good conditional ⇒ spurious positivity; full two-type model ⇒ no gain, K=4 fake persists | EVIDENCE |
| — | unconditional `a_min≥11` via Type-I + parity + Chen switching | **not reached**; numerical gap K*≈2–2.5 (continuum Assessment: [2,3]) vs ≥3.9 known |

## 1. What a real switched sieve provides (the faithful constraint)

Fix a hard-prime window q∈{3,7}, q' the other one. Chen's switching for a family
of configurations in which `n_q=(p+q)/4` has a q-bad prime factor r:
write `n_q=m·r`, so `p=4mr−q`, and count primes in the *switched sequence*
```
E = E_q(𝓜,I) = { 4mr−q : m∈𝓜, r∈I prime, mr≤(x+q)/4 },
```
where `𝓜` is an arbitrary set of integers (any prescribed factorisation type
for the rest of `n_q`), I a range of primes. E is a bilinear (convolution)
sequence `α*β` with `β=1_{primes}` (Siegel–Walfisz). By Bombieri–Vinogradov for
convolutions (Motohashi 1976; Bombieri–Friedlander–Iwaniec I, Thm 0; level
`x^{1/2−o(1)}` when `I⊂[x^η, x^{1−η}]`), the linear upper-bound sieve on E counts
its primes to within the factor `F(2)·e^{−γ}·2/θ·… = 2/θ = 4` of the expected count
(Selberg/Brun–Titchmarsh constant at level θ=1/2). The other window's condition
"`n_{q'}=mr+(q'−q)/4` has no q'-bad prime `<x^η`" can be imposed in the same
upper sieve by the fundamental lemma at negligible cost.

What this **cannot** see: the large-prime configuration of `n_{q'}` (a "has a
prime factor in bin k" condition is not a sieve upper-bound condition), and the
split of mass between individual joint configurations. So, in the model, the
basic switched sieve (no condition on `n_{q'}` beyond `x^η`) gives the **marginal caps**
```
(SW_K)   Σ_{C_{q'}} ν(C_q, C_{q'}) ≤ K · Σ_{C_{q'}} μ(C_q, C_{q'})   for every window-q configuration C_q≠∅,
```
for both q, with `K=4` (BV level, Selberg) as the baseline. (Assessment: we did not check the
precise hypotheses of the convolution BV theorem for every `(𝓜,I)`, nor that its main term equals
the model's μ; at fixed ε the fundamental-lemma sifting to `x^ε` also uses part of the level.) (Each
point of C_q may serve as the switched prime r; the bound holds per C_q as soon as
one point is switchable, and multiplicities cancel between the two sides.)
These are *aggregate* constraints: weaker than WINDOW2 §6.2's per-joint-configuration
caps `ν(C)≤Kμ(C)`, so the required K under (SW_K) is at most the §6.2 threshold.
LP duality: the dual of "min ν(∅,∅) s.t. Type-I correlations at level θ, parity,
ν≥0, (SW_K)" is exactly a Chen-type lower bound
`Σ_S y_S ρ(S) − K Σ_{q,C_q} λ_{q,C_q} μ_q(C_q)` with `λ≥0` — a Type-I sieve minus switched upper bounds.

**Scope.** We do not claim these (and the §4 families) exhaust what switching can give. Other
Chen-type inequalities (weighted, iterated, or with divisibility restrictions on `n_{q'}` imposed
before sieving) are not modelled. All "fake" statements below are relative to the stated families.

Refinements a sieve *can* add (to be tested, §3): (a) restrict I to one bin and
𝓜 to a fixed factorisation type (already in SW_K: C_q is fixed); (b) impose
"no q'-bad prime `<z'`" with larger `z'` in the switched upper sieve, a dimension
`1+1/2` upper sieve with its own constant `K(z')`.

## 2. Model fidelity (repairing R29-M4)

### 2.1 The continuum heuristic law is parity-blind; the K=8 bias is a binning artefact (EVIDENCE, quadrature)
Continuum law of one window: Poisson points of intensity `dt/(2t)` on `[ε,1]`, cofactor weight
`(u−Σt)^{−1/2}`. The Type-I data of a visible S (sum s) are `∏(dt/2t)·½(F_+(1−s)±F_−(1−s))`,
sign `(−1)^{|S|}`, where `F_±(u)=Σ_k (±1)^k/k!∫∏dt_i/(2t_i)(u−Σt)^{−1/2}`. Real data
(BV + fundamental lemma, Thm P1) are `∝∏g(d)`, parity-blind: they need `F_+` constant and `F_−≈0`.
`/tmp`-free replay: `scripts/window3_cont.py EPS 4000` (grid quadrature, step 1/4000):

| ε | F_+(0.5) | F_+(1) | F_−(0.5)/F_+(0.5) | F_−(1)/F_+(1) |
|---|---|---|---|---|
| 0.10 | 4.145 | 4.161 | 3.1e-3 | 1.0e-3 |
| 0.05 | 5.864 | 5.887 | 1.4e-3 | 4.8e-4 |
| 0.02 | 9.287 | 9.325 | 5.3e-4 | 1.8e-4 |
| 0.01 | 13.17 | 13.23 | 2.6e-4 | 9e-5 |

So the continuum heuristic's data are product-form to 0.4% and parity-blind to 0.3% **already at
ε=0.1**. The R29 spread `r(S)∈[0.82,1.87]` comes from the discretisation of WINDOW2 (point
masses at bin centres, cofactor weight evaluated at the centre sum), not from ε.
**Repair adopted:** μ(C) := exact cell integral of the continuum law over the bin cell of C
(sub-grid quadrature, `scripts/window3_model.py`). Then ρ(S)=Σ_C emb(S,C)μ(C) are the exact
cell-aggregated continuum data, product-form and parity-blind to the accuracy above.

### 2.2 Cell-integrated law: data product-form and parity-blind to ≤0.27% (EVIDENCE, quadrature N=4000)
`scripts/window3_rcheck.py EPS K 0.5` computes `r(S)=ρ(S)/(∏w_k^{S_k}/S_k!)/ρ(∅)` for all visible S
(rep convention), for the even law and for the odd ("(p/3)=−1") law:

| (ε,K) | window configs (even) | r(S) range, even law | max \|r_even(S)−r_odd(S)\| |
|---|---|---|---|
| (0.1, 8) | 197 | [0.999993, 1.000004] | 2.7e-3 |
| (0.1, 12) | 685 | [0.999997, 1.000003] | 2.7e-3 |
| (0.07, 9) | 842 | [0.9999998, 1.0] | 2.2e-3 |
| (0.05, 10) | 4110 | [0.9999998, 1.0] | 1.9e-3 |

(Compare R29: [0.82,1.87] for WINDOW2's point-mass law.) The residual parity sensitivity is the
continuum `F_−` (it is ≍ the density of x^ε-smooth cofactors in reality, even smaller, but
≤0.3% either way). **R29-M4 is repaired for the data**: every LP below uses this law.
(The cell-integrated law includes configurations whose cell straddles Σ=1, with their mass
below 1; hence more configurations than WINDOW2 at the same grid.)

## 3. The LP on the faithful law (ε=0.1, K=8, θ=1/2, rep visibility)

`scripts/window3_lp.py` (columns normalised; dual bound computed from HiGHS duals with an
explicit penalty for dual violations, `x_j≤ρ_0/μ_j` from the total-mass row; "cert" = this
float dual bound equals the primal value). Window configs 195 (LP columns; joint 195² = 38025), rows 89 (two-window). The §2.2 count 197 is before `window3_lp.py` drops cells of mass <1e-14·max — (4,0,1,0,0,1,0,0) and (5,1,2,0,0,0,0,0), min cell sums 0.9995 and 0.9890, quadrature masses 1.8e-18 and 9.2e-17.

| constraint set | min ν(∅,∅)/τ | status |
|---|---|---|
| one window, none | 0.4893 | cert (dual 0.48929) |
| two windows, none | 0 | fake, residual 5e-15 (max ν/μ 1.6e19: unbounded) |
| per-config caps `x_C≤K` on all C≠∅ (`--swpc=K:0.1`), K=2 | 0.2407 | cert |
| same, K=2.25 | 0.1045 | cert |
| same, K=2.5 / 3 | 0 / 0 | fake, residual 3e-15 |
| per-config caps on C with a point in the top cell `[0.75,1]` (`--swpc=K:0.6`), K=1.01 | 0 | fake, residual 1e-13 |
| **marginal caps (SW_K), all C_q≠∅**, K=1.03 | 0.077 | primal only (residual 5e-9), dual not certified |
| same, K=1.05 | 0.055 | primal only |
| same, K=1.07 | 0.032 | primal only |
| same, K=1.1 / 1.15 / 1.2 / 2 / 4 | 0 | fake, residual ≤2.3e-8 |

So on the faithful law: (i) one-window positivity at θ=1/2 survives (0.489, certified on the
grid); (ii) bounded reweighting needs `K*∈(2.25,2.5)`; (iii) WINDOW2 §7.1's α=0.6 bin caps are
useless here (the fake avoids top-cell configurations); (iv) **the faithful aggregate switching
constraint (SW_K) needs K*∈(1.07,1.1)** — essentially a *perfect* switched upper bound — against
the baseline K=4 (and ≈3.4 even if Wu-type twin-prime technology transferred). (EVIDENCE on this grid.)

*Mechanism (from the K=1.05 primal).* The fake removes the target and inflates the one-sided
configurations `(C_3,∅)` and `(∅,C_7)` (pairs of window-3 bad primes, window 7 clean) by
`ν/μ≈2.2`, while emptying `(C_3,C_7≠∅)`. The C_3-marginal stays ≤K because `μ_7(∅)/M_7≈0.48`.
A switched sieve on `n_3=m·r` cannot tell "n_7 clean" from "n_7 has two large bad primes",
so (SW_K) cannot block this. Only a switched bound that *also sifts n_7 to a high level* can
(§4).

## 4. Switched bounds that also sift the other window

### 4.1 Families and their real constants
For window q, a fixed `C_q≠∅` and a set Z of cells, the family
`F(q,C_q,Z)={(C_q,C_{q'}): C_{q'} has no point in Z}` is a family a switched upper sieve
can bound: sift `E_q` for primality of `p` *and* sift `n_{q'}=mr+(q'−q)/4` by the q'-bad primes
in Z. Constraint: `ν(F)≤K(Z)μ(F)`. (`Z=∅`: the marginal caps of §3; `Z`=all cells: per-config
cap on `(C_q,∅)`.) `--swz=K:prefix` uses `Z=[ε,ζ)` for every cell edge ζ; `--swz=K:all:j`
every subset of the first j cells.

Real constants, prefix `Z=[ε,ζ)` (`scripts/window3_kz.py 0.1 8`): compose the linear upper
sieve for primality at level `x^{θ_1}` (constant `2/θ_1`) with Iwaniec's semi-linear upper sieve
for `n_{q'}` at level `x^{θ_2}`, `θ_1+θ_2=1/2`:
`K(ζ)=min_{θ_2}(2/θ_1)F_{1/2}(θ_2/ζ)/σ_even(ζ)`, `F_{1/2}(s)=2(e^γ/(πs))^{1/2}` on `(0,2]`
(the function consistent, via the β-sieve delay equations, with the f(s) quoted in
Teräväinen (6.4); F_{1/2}(3)=1.0037, F_{1/2}(4)=1.0001), σ_even(ζ)=model truth relative to
`V(x^ζ)` (≈1.00 for ζ≤0.42, 1.13 at 0.56). Result of this one construction: K(ε)=4 (the marginal, fundamental lemma taken
as free), **K(0.133)=8.1, K(0.178)=9.3, K(0.237)=10.8, K(0.316)=12.4, K(0.422)=14.1,
K(≥0.56)=14.7** (optimum θ_2=1/6 throughout). A joint Selberg Λ² of mixed dimension would do
somewhat better (for ζ≥1/4 its constant is `4Γ(5/2)e^{γ/2}(4ζ)^{1/2}/σ ≈ 7.1(4ζ)^{1/2}/σ`), but
these composed values are *worse* than the trivial bound from the marginal cap, `F_ζ⊂` marginal
family ⇒ `K(ζ)≤4/P(no bad point<ζ)` (=4.6, 5.3, 6.2, 7.1, 8.0, 8.4 at the edges above). So the
8–15 figures are one conservative construction, not a limitation of switching. What matters
below: all these constants are ≥ the prime-pair constant, ≈3.9–4 at BV level with present
technology (≥3.4 if Wu-type improvements transferred, §5; Assessment). (Assessment: these are standard sieve-constant
computations; the semi-linear F is derived, not read in a primary source.)

### 4.2 LP with generous uniform constants (ε=0.1, K=8, θ=1/2)
Giving *every* family the same constant K (far more generous than §4.1):

| families | K=1.2 | K=2 | K=2.5 | K=3 | K=4 |
|---|---|---|---|---|---|
| prefix Z (all ζ, incl. ζ=1) | 0.720 | 0.084 | 0 | 0 | 0 |
| all Z ⊂ first 6 cells | — | — | — | — | 0 |

(0 = fake, residual ≤2e-8; positive values: primal only, dual not certified.)
**So even if every switched family — sifting the other window to any depth — were bounded
with the prime-pair constant 4 (or 2.5), Type-I + parity + switching would not prove a single
two-window failure in this model.** Threshold for uniform constants: `K*∈(2,2.5)`.

## 5. Best known constants for the switched counts (goal 2)

Source checked: J. Wu, *Chen's double sieve, Goldbach's conjecture and the twin prime problem*,
Acta Arith. 114 (2004) 215–273 = arXiv:0705.1652, archived `sources/window3/0705.1652.{pdf,txt}`
(§1, pp. 1–4); part 2 (Acta Arith. 131 (2008) 367–387) = arXiv:0709.3764, archived (it improves
the *lower* bound `D_{1,2}`, irrelevant here). Constants as ratios to the Hardy–Littlewood value
(Goldbach `D(N)~2Θ(N)`, twins `π_2~Π(x)`):

| method | Goldbach `D(N)` | twins `π_2(x)` | inputs |
|---|---|---|---|
| Selberg Λ² (1949) | 8 | — | level from Selberg |
| Bombieri–Davenport (1966) | **4** | 4 | linear sieve + BV (level 1/2) |
| Chen (1978) double sieve | 3.9171 | 3.9171 | + Chen's weighted inequalities + switching |
| Wu 2004 Thm 1 / Thm 3 | 3.91045 | **3.3996** | twins: + BFI/Fouvry mean-value theorems with well-factorable weights (level > 1/2, *fixed* residue class) |
| any sieve, even at level 1 (EH) | ≥2 | ≥2 | Selberg's parity example for upper bounds (`F(2)=e^γ` at `D=x`) |

(Checked in source: 16→12→8→7.8342→7.8209 for `D(N)≤aΘ(N)`, "the constant a is half of the
corresponding constant in the Goldbach problem" for twins at equal technology, 3.418→3.406→3.3996
for twins; Wu: "It seems very difficult to prove (1.2) with a constant strictly less than 8 by the
method in [1]", the linear sieve bounds are attained by Selberg's parity sequences, and Remark 1(i):
the double-sieve gain "works for all sequences satisfying the Chen–Iwaniec switching principle".)

**Which applies to the window switched sequences** `E_q={4mr−q}` (bilinear, residue class
`q·4^{−1} mod d` fixed, but primes enter through the convolution `𝓜*𝒫`): BV for convolutions
(level 1/2) is available, so **K=4 is the natural baseline** (Assessment; hypotheses not checked in detail, §1). Chen's double sieve plausibly
transfers (Wu's Remark 1(i)), giving ≈3.91 — not checked for convolution sequences, and it
needs the switching principle *for E itself*. Wu's 3.3996 needs level >1/2 with well-factorable
weights for primes in a fixed class; for convolutions `α*β` with arbitrary α (the configuration
set 𝓜) such mean-value theorems are not known to us at the required generality
(Assessment, not searched exhaustively). The half-dimensional extra condition (§4.1) only makes the
constants larger (K(ζ)≈8–15 with composed sieves). **Recalled vs checked:** the table's rows are
checked in Wu's §1; "≥2 at level 1" is the standard parity statement (recalled; it is Wu's
remark about (1.3) at ν=1); the K(ζ) values of §4.1 are our computations.

## 6. Good-prime Type-I data (R29-M2) change the picture

Real Type-I data at level θ include `|A_d|` for *all* `d≤x^θ`, also d with good prime factors.
Option `--good` adds the rows `(S,G)`: S a bad sub-multiset, G a multiset of *good* points
(≥x^ε, intensity `dt/(2t)` as for bad primes), `ΣS+ΣG≤θ`, per window and jointly. Their model
values are `Σ_C ν(C)emb(S,C)μ_G(C)/μ(C)`, with `μ_G(C)=μ(C+G)·∏(C_k+G_k)!/(C_k!G_k!)` the
cell-integrated density of "bad config C and good points G" (the good part of a bad-free
cofactor has the same `(u−Σ)^{−1/2}` structure). **Caveat:** this keeps the *true conditional law
of the good part given C*. A real fake may change that law too, so these LPs restrict the fakes:
a fake found here is a genuine fake for full Type-I data, but a positive value is **not** a
lower bound for the full problem.

ε=0.1, K=8, θ=1/2 (`window3_lp2.py ... --cg --good`; residual ≤3e-6, elastic ≤2e-5: EVIDENCE):

| | bad-only rows (§3–4) | + good rows (fixed good conditional) |
|---|---|---|
| one window, no switching | 0.489 | 0.997 |
| two windows, no switching | 0 (fake) | **0.307** |
| two windows, uniform families K=4 | 0 (fake) | 0.313 |
| two windows, uniform families K=2 | 0.084 | 0.329 |

So the WINDOW2/§3–4 fakes **violate the good-prime Type-I data** as soon as the good part keeps its
true conditional law: they move mass between configurations with different cofactor sizes
`1−ΣC`, and good divisors see the cofactor size (exactly R29-M2). Whether a fake survives when
the good conditional may *also* be altered is the real question; it needs the full two-type
model (bad and good points both recorded), §7.

## 7. Full two-type model: good-prime data do not help once fakes may move good parts

`scripts/window3_full.py` records bad *and* good points ≥x^ε in each window. Law: same Poisson
intensity `dt/(2t)` for both types, remainder density H (x^ε-smooth, bad-free part) defined by
exact discrete back-substitution so that summing out good points reproduces the bad-only law of §2
up to grid error (H≥0 checked: min 2.7e-7; review toy check ε=0.5, K=1: marginal 0.999998 vs 1,
from rounded-grid mass of excluded cells). Data: all `(S_B,S_G)` with `ΣS_B+ΣS_G≤θ`. Target: `B_3=B_7=∅`
(any good part). Families (`--swz=K`, prefix Z, uniform K) for every `C_q=(B_q,G_q)` with
`B_q≠∅`; `--swgood` adds `B_q=∅, G_q≠∅` (switching a *good* prime of `n_q`).

One window, θ=1/2 (min ν(clean)/τ):

| (ε,K) | bad-only rows | all rows (bad+good) | §6 fixed-conditional |
|---|---|---|---|
| (0.15,6) | 0.6691 | 0.6691 | — |
| (0.1,6) | 0 | 0 | — |
| (0.1,8) | 0.48929 | 0.48929 | 0.997 |

Two windows, (ε,K)=(0.15,6), θ=1/2 (65025 joint configurations, 53 rows; residual ≤2e-15):

| constraints | min ν(both clean)/τ |
|---|---|
| bad-only rows, no switching | 0 (fake) |
| all rows, no switching | 0 (fake) |
| all rows + families K=4 (± `--swgood`) | 0 (fake) |
| all rows + families K=2 (± `--swgood`) | 0.411 |
| all rows + families K=1.2 | 0.809 |

**Conclusion (EVIDENCE, coarse grids):** once a fake may also change the good part of the
factorisation, the good-prime Type-I data add *nothing* (identical LP values on all one-window
grids tested). §6's large values came only from freezing the good conditional law. R29-M2 is
answered in the model: the obstruction is not an artefact of omitting good divisors. The picture
of §4 (fake at uniform K=4, positivity at K=2) is reproduced in the full model.
(Heuristic reason: good and bad points have the same intensity, so the data depend on
`S_B⊔S_G` essentially type-blindly, except through the parity boundary terms.)

## 8. Robustness of the K=4 fake (bad-only rows, uniform prefix families, `window3_lp2.py --cg`)

Column generation (restricted master with elastic rows, pricing over all joint columns, stop
when no reduced cost < −1e-9; final elastic = 0). min ν(∅,∅)/τ:

| grid / variant | K=4 | K=3 | K=2.5 | K=2 |
|---|---|---|---|---|
| (0.1, 8), rep | 0 | 0 | 0 | 0.084 |
| (0.1, 8), **outer** visibility (157 rows: *more* information than reality) | 0 | 0 | 0.023 | — |
| (0.1, 10), rep | 0 | — | 0 | — |
| (0.1, 12), rep (666 window configs, 443k joint) | — | 0 | 0 | ≤0.0574 (restricted-master value = an *upper* bound; CG stalled at iteration 13 with reduced costs ≥ −0.011, so 0 is not excluded) |
| (0.07, 9), rep (758 window configs, 575k joint) | 0 | — | 0 | running at checkpoint (iteration 9: 0.144, far from converged) |
| (0.15, 6), full two-type model (§7) | 0 | — | — | 0.411 |
| (0.1, 8), rep, θ=0.55 / 0.6 / 0.65 | 0 / 0 / 0.060 | | | |

All fakes: residual ≤3.6e-10 (most ≤4e-14). Raw logs: `data/window3/runs_*.jsonl{,.err}`. (0.05,10) did not finish within 4 h (not used).
So the K=4 fake is stable under grid refinement, under the generous visibility convention, and in
the full two-type model; and with switching at K=4 the Type-I level would have to exceed 0.6
(positivity from θ≈0.65 on the coarse grid).

### 8.1 High-precision verified fakes (ε=0.1, K=8, rep, θ=1/2)
`window3_lp.py 0.1 8 0.5 --swz=K−0.001:prefix --certify --certK=K`: solve the LP with caps
slightly *below* K, then repair the float solution on its support by the minimum-norm correction
(50-digit mpmath) making every visible correlation exact, and check `x≥0`, `x_∅=0` and every
family row ≤ K (all rows, in 50 digits):

| K | support | min ν/μ on support | max correlation residual | worst family excess | |
|---|---|---|---|---|---|
| 4 | 514 | 0.0211 | <1e-40 (50 digits) | −1.0e-3 | verified |
| 3 | 605 | 0.1669 | <1e-40 | −1.0e-3 | verified |
| 2.5 | 628 | 0.0566 | <1e-40 | −1.0e-3 | verified |

**Proposition 8.1 (discrete model; EVIDENCE, 50-digit verified, data = float cell-integrated law).** In the
faithful discrete model (ε=0.1, K=8, cell-integrated law of §2, rep visibility, θ=1/2), Type-I
data, both parities and *every* switched family bound `ν(F(q,C_q,[ε,ζ)))≤Kμ(F)` (all q, all
`C_q≠∅`, all cell edges ζ, including ζ=1) with **K=2.5** do not force a single both-clean
configuration. Every constant currently available for these switched counts is ≥3.9 (§4.1, §5;
Assessment). So switched bounds *of this prefix-family form* with present constants are
insufficient in this model. (The check is 50-digit floating point, not interval arithmetic,
on the normalised float matrices; it covers every visible row, every family row, x≥0 and x_∅=0.)

## Replay
```
export PYTHONPATH=scripts; ulimit -v 8000000
uv run --with numpy python scripts/window3_cont.py 0.1 4000                    # §2.1
uv run --with numpy python scripts/window3_rcheck.py 0.1 8 0.5                  # §2.2
uv run --with scipy python scripts/window3_lp.py 0.1 8 0.5 --one                # §3 (0.4893)
uv run --with scipy python scripts/window3_lp.py 0.1 8 0.5 --swm=1.05           # §3 marginal caps
uv run --with scipy python scripts/window3_lp.py 0.1 8 0.5 --swpc=2.25:0.1      # §3 per-config caps
uv run --with numpy python scripts/window3_kz.py 0.1 8                          # §4.1 K(zeta)
uv run --with scipy python scripts/window3_lp2.py 0.1 8 0.5 --swz=2:prefix --drop=1e-3 --cg   # §4.2, §8
uv run --with scipy python scripts/window3_lp2.py 0.1 8 0.5 --swz=4:prefix --drop=1e-3 --cg --good  # §6
uv run --with scipy python scripts/window3_full.py 0.15 6 0.5 --swz=4 --swgood  # §7
uv run --with scipy --with mpmath python scripts/window3_lp.py 0.1 8 0.5 --swz=2.499:prefix --certify --certK=2.5  # §8.1
scripts/window3_batch.sh OUT 14400 "0.1 12 0.5 --swz=2:prefix --drop=1e-3 --cg"   # §8 large grids (hours)
```
