# Z56_FAMATTACK — joint attack on positivity of the full (★) count R(p)

Status: z56 lane FAMATTACK (brief `z52bbriefs/z53_depth.md` + `z56_lanes.md` §3). Internal, work in progress.
**ES is OPEN; nothing here proves or disproves it, or (★), at any infinite set of primes.** Labels: PROVED /
CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z56_famattack_*`, data
`data/z56/famattack/`.

## 0. Checkpoint 1 (skeleton)

### (a) Statement attacked

R(n) := #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n} (FRONTIER §2.1).

**Target (FA).** There is p₀ such that R(p) ≥ 1 for every prime p ≡ 1 (mod 4), p > p₀. (CERTIFIED context: R(p) = 0
at exactly 14 primes p ≡ 1 (4) below 10¹⁰, the largest 8 813 281.)

**Joint-window form (FA-W).** Partition the unordered solution set (u < B) into windows 𝒲₁, …, 𝒲_J (sets of
parameter triples defined by size conditions on u, B, C), R(p) = Σ_j R_j(p), with main terms M_j(p) (genus or
density) and remainders X_j = R_j − M_j. FA follows from any inequality of the form
  Σ_j X_j(p) ≥ −(1 − ε)·Σ_j M_j(p)  for p > p₀,  together with Σ_j M_j(p) ≥ 1/ε.
The brief asks whether the *joint* structure — Thm-U lower bounds on many windows, Thm X density control,
the switch d ↔ (4Cp+1)/d, the spin dictionary, dual-large-sieve variance, and the fact that different u-windows involve
disjoint sets of integers p + u — yields such an inequality when no single window does.

### (b) Why this is not already closed

* Thm U (GENUSLVAL) bounds one genus subfamily's main term; CROSSF refutes positivity for one standard-window family
  below 10¹⁵. Neither speaks to the *union* of windows, whose mean is ≈ 0.15 log²p (≈ 20× the Thm-U family) and whose
  certified zero set ends at 8.8·10⁶.
* The closed items (z53 brief list, FRONTIER §6) concern single windows / fixed conductor / one-variable sections /
  Fourier minorants with proper-subgroup support. None addresses a cross-window inequality.
* Escape hatch being tested: an inequality *linking* window remainders at one p (compensation), which would make the
  union strictly better than independent windows.

### (c) First falsifier (computation; status below)

**F1 (cross-window association, pre-registered).** If windows can compensate each other at one p, their counts must be
*negatively* associated across primes once the shared main-term drivers are removed. Windows: u-bins
a = log u/log p ∈ [0,.1), [.1,.2), [.2,.3), [.3,.4), [.4,.5) (u = min(u,B); the bins use disjoint integer sets p + u).
Decision rule (fixed before looking): compute the pairwise correlation of window counts within strata of p mod 840
(removes local-factor main-term variation). A within-stratum pooled correlation below −4 standard errors in any pair is
a lead (compensation exists, push on it); all pairs ≥ −2 s.e. kills "compensation through disjointness" at the
resolution of the data (EVIDENCE only, cannot kill a pointwise theorem).

Engine: `scripts/z56_famattack_wcount.c` (exact R(n) with a 5×5 (u, C) window grid). Validation: agrees with brute
force (`scripts/z56_famattack_brute.py`) at all odd n ≤ 3001; reproduces exactly the 14 known zero primes ≤ 10⁷
(409 … 8 813 281) and R = 0 at odd squares (CERTIFIED for those ranges).

*Result:* pending.
