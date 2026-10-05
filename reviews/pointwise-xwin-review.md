# R32: hostile review of O32 / POINTWISE_XWIN.md

Reviewer branch `side-agent/review-xwin` (merged `side-agent/xwin-average` at 8d89852).
From-scratch scripts: `scripts/review_xw_*.py`.

## Verdict summary (filled in claim by claim)

| claim | verdict |
|---|---|
| Lemma 1.1 (half-set) | SOUND (brute-forced, a≤300, 1.1M failing pairs) |
| Thm 1.2 / Cor 1.3 (fixed-set stacking, exponent 1+J/2) | SOUND |
| Cor 1.4 (two-sided orders) | SOUND-AFTER-REPAIRS (labels: MINOR-1, MINOR-2) |
| Thm 1.5 (uniform, Z=o(log log N)) | SOUND-AFTER-REPAIRS (MAJOR-1: stated range Z≤L excludes the advertised Z≈3.6L; proof extends) |
| §1.3 census | EVIDENCE reproduced bit-for-bit (10^6,10^7,10^8) |
| Lemma 2.1 | SOUND (exact/MC check) |
| Thm 2.2 / Cor 2.3 | SOUND (MINOR-4, MINOR-5 cosmetic); priority to notes Thm 14.9 correctly stated |
| Prop 3.2 | SOUND as scoped |
| §3.3 GRH/EH remarks | unlabeled; MINOR-6 |

**Overall:** no FATAL defects, one MAJOR (statement-range, trivially
repairable), six MINOR. The main new content — Lemma 1.1 and the exact
exponent `1+J/2` for every fixed window set, including composite windows — is
correct; the proposed ledger entry (H)17 is supported once MAJOR-1 is fixed
(or the `0.22` claim is dropped / marked as requiring `Z≤C_0L`).

Process note: `git merge --ff-only side-agent/xwin-average` was impossible
(main had advanced past the fork point of my branch); I did a plain
`git merge` into my own review branch only.

## Lemma 1.1 — half-set lemma

Definition checked against POINTWISE_SIZE §8.1: `Rat_q(x)={u/v mod q: uv|x, gcd(u,v)=1}`.
There is no separate "exponent budget" in the definition; the budget `|f_r|≤v_r(x)`
of Cor 8.3(b)/notes §70 F3 is simply the constraint `uv|x`. Lemma 1.1 uses only
`u=r`, `u=rs`, `u=r,v=s` for distinct primes `r,s|x`, all of which satisfy `uv|x`
whatever the exponents; so "no budget exceptions" is correct (the lemma is a pure
necessary condition, the budget can only remove elements from Rat, never add).

Re-derivation: −1 is a non-square mod a (a has a prime factor ≡3 (4)), so the
Klein orbits are of size 4 (g²≠1) or 2 (g²=1, `{g,−g}`); checked all six
coincidences. Excluding `gh=−1` and `g/h=−1` for distinct classes, plus `−1∉C`,
is exactly "C meets one half of each orbit, and picks 1 from {1,−1}". Equal-class
pairs (two primes in one class g): `g²≠−1`, `g/g=1`, harmless. Count of orbits:
`2^{ω(a)}` involutions (a odd, CRT), so `β(a)=(φ−2^ω)/4+2^{ω−1}−1`. ✔.

**From-scratch check** (`scripts/review_xw_halfset.py 300 20000`): for every
a≡3 (4), 3≤a≤300 (incl. composites), every x≤20000 and 2000 random x∈[10^8,10^12]
coprime to a, full enumeration of Rat_a(x); whenever −1∉Rat_a(x), verified C(x)
lies in some S_σ. Also verified `|S_σ|=φ(a)/2`, number of 2-orbits `=2^{ω−1}`
and the β formula. 1,119,553 failing pairs, no counterexample (15 s). EVIDENCE
supporting a proof I find correct.

Minor remark (no defect): Remark (iii) is right that the lemma only concerns
the −1 target, so the theorems below bound a superset of window failure.

## Theorem 1.2 / Corollary 1.3 — fixed-set stacking

Re-derived line by line; **SOUND**.

* Sieve input = notes Lemma 12.1. I re-checked its proof: Parseval
  `(1/ℓ)[(ℓ−ν)g²+ν]=g` with `g=ν/(ℓ−ν)`, Cauchy–Schwarz gives (12.2), large
  sieve with `Q=X^{1/2}`, Markov `H(Q)≥V^{-1}/2` when `log Q≥2Λ`. Gives `|S|≤4XV`. ✔
* Sifted classes: for odd `ℓ>y`, `ℓ|p+a ⇒ ℓ|x_a ⇒ ℓ mod a∈C(x_a)⊆S_{σ_a}`; so
  removing `{t: ℓ|24t+1+a}` when `ℓ mod a∉S_{σ_a}` is legitimate. Roots distinct
  for `ℓ>2max A` (also `ℓ∤a`, `ℓ∤24`). `ν(ℓ)≤J+1<ℓ` since `max A≥4J−1`. ✔
* `Λ≤(J+1)(log z+O(1))=(log X)/5+O_A(1)≤(log X)/4`. ✔
* Density: `G∖S_σ` is exactly `φ(a)/2` reduced classes, so Mertens in APs mod
  the fixed a gives `½ log log z+O_a(1)` per window, regardless of which
  selection; the sum over windows is additive, **no independence between
  windows is needed** (the large sieve takes arbitrary root sets). Windows
  sharing prime factors (e.g. a=15 and a=3) are harmless: the per-ℓ root
  `−(1+a)/24 mod ℓ` depends on a only as an integer. ✔
* Uniformity in the class sets: only finitely many (`2^{Σβ}`) selection
  vectors, each with the same `V` up to `O_A(1)`. ✔
* Cor 1.3: `p>3Z` makes every `a≤Z` admissible (`x_a<p`), and
  `gcd(x_a,a)=gcd(x_a,p)=1`, so Lemma 1.1 applies; `J(Z)=⌊(Z+1)/4⌋` ✔;
  `T(N,7)≪N/(log N)^2`, `T(N,11)≪N/(log N)^{5/2}`, `T(N,23)≪N/(log N)^4` ✔.
* The claim that it upgrades POINTWISE_WINDOW §6's joint "dimension ≥J/2"
  Assessment to a theorem is correct: Lemma 1.1 removes the `<qφ(q)`
  exceptional primes of Lemma 6.1 that blocked a clean sieve.

## Corollary 1.4 — two-sided orders: SOUND-AFTER-REPAIRS (labels only)

Equivalences `a_min≥7 ⟺ a_min>3` (Z=3, J=1, exponent 3/2) and
`a_min≥11 ⟺ a_min>7` (Z=7, J=2, exponent 2) ✔. Lower bounds: W1 counts
`p≡1 (840)` (⊂ `p≡1 (24)`) with window 3 failing ⇒ `a_min≥7` ✔; W2 analogous on EH.

* **MINOR-1** (Table row 1.4 / Cor 1.4 first bullet): status written "PROVED"
  but W1 is "PROVED modulo cited sieve theorems S1–S3" (S1, the semi-linear
  β-sieve, not read in a primary source per POINTWISE_WINDOW §2.1). Repair:
  label the lower half "PROVED modulo the sieve theorems cited for W1".
* **MINOR-2** (Cor 1.4): the counts `#{p≤x: a_min(p)≥7}` do not say `p≡1 (24)`;
  the upper bound (Thm 1.2) is proved only for that class. Either add
  `p≡1 (24)` or note that the same sieve with `p=4t+1` covers all `p≡1 (4)`.

## Theorem 1.5 — uniform stacking (not previously reviewed): SOUND-AFTER-REPAIRS

Re-derived: `y=exp(L²)`, `log z=ℒ/(5(J+1))`. SW for `a≤L=(log y)^{1/2}`,
partial summation gives per-class error `≪∫_{L²}^∞e^{−c√u}du≪e^{−c_1L}`; with
`≤Z` windows × `≤Z` classes the total is `o(1)` ✔. Main term
`(1+J/2)log(log z/log y)`, and `log(log z/log y)=L−2log L−log(5(J+1))≥L−3log L−C`
for `J≤L` ✔; `y<z` and `Λ≤ℒ/5+O(J)≤ℒ/4` ✔; `e^{−(L−3logL−C)}≍L³/ℒ` ✔. Union
over `2^{β_tot}` vectors ✔; `β(a)=φ/4+2^{ω−2}−1` exactly, so the bound is ✔.
For `Z=o(L)`: `β_tot=O(Z²)=o(JL)` and `(J+1)log L=o(JL)`, giving
`π(N)ℒ^{−(1/2−o(1))J}` ✔. SW is used only for moduli `≤(log y)^{1/2}`, where
even the effective Landau–Page bound suffices; "modulo SW" is just "PROVED
(constants possibly ineffective)".

Numerics (`scripts/review_xw_beta.py`): `β_tot(Z)/(Z²/4π²)=0.971, 1.0005, 1.0005`
at `Z=100,1000,5000` ✔; optimising `−(Z/8)L+(log2/4π²)Z²` gives `Z*=π²L/(4log2)=3.56L`
and `c=0.2225` ✔.

* **MAJOR-1** (Thm 1.5 statement vs. its consequence, POINTWISE_XWIN lines
  ≈157–166 and table row 1.5): the theorem is stated "uniformly for `3≤Z≤L`",
  but the advertised `N exp(−0.22(log log N)²)` is evaluated at
  `Z≈3.6L>L`, outside the stated range. The proof does extend (SW holds for
  `a≤3.6L≤(log y)^{1/2}·3.6`; `log(5(J+1))≤log L+C` still; `Λ` bound still), so
  this is a statement-range bug, not a mathematical gap. Repair: state the
  theorem for `3≤Z≤C_0L` with any fixed `C_0` (constants depending on `C_0`),
  or for `Z≤L^{A}`; then the 0.22 claim follows (as `c=0.2225−o(1)`).
  (Graded MAJOR only because, as written, a headline claim is not covered by
  the theorem it is derived from.)
* **MINOR-3**: `c≈0.22` uses `β_tot~Z²/(4π²)`, an asymptotic; write the constant as
  `c=π²/(64 log 2)−o(1)=0.2225−o(1)` to make it a theorem.

## §2: Lemma 2.1, Theorem 2.2, Corollary 2.3 — SOUND (minor cosmetics)

**Lemma 2.1.** Re-derived the second moment: diagonal `μ_N`; pairs with a
coordinate where exactly one is 0 contribute `1/n²` each (≤`μ_N²`); equal-support
pairs with `D≠∅`: `B²=1, A=τB`, giving `t/n²` (≤`5^k` pairs) or, if `A=1`, `B=τ`
with prob `1/n` (≤`3^k−1` pairs). Chebyshev and `3^k−1≥(2/3)3^k` give the bound;
Poisson generating function ✔. Matches notes Lemma 12.5 (same second moment,
there used with Paley–Zygmund). **From-scratch check**
(`scripts/review_xw_signed.py`): exact ρ_k (multiset enumeration) / Monte Carlo
for `a∈{3,7,11,15,19,23,35,39,55,63,91,105}`, `k≤12`: no violation, max
`ρ_k/bound=0.17`; the lower bound `ρ_k≥2^{−k}` (prime a, exact cases) also holds.
(Remark: for composite `a≡3 (4)` the kernel of the Jacobi character `(·/a)` is an
index-2 subgroup avoiding −1, so `ρ_k≥2^{−k}` holds for every such a, not only
primes.)

**Theorem 2.2.** Checked each step.
* SW input: `a≤ℒ^θ=(log y)^{θ/δ}`, fixed power of `log y`, partial summation from
  `u≥y` gives error `≪e^{−c√log y}`; times `φ(a)≤ℒ` gives η ✔. `λ=(1−θ−δ)L−log L−O(1)` ✔.
* Step 0: distinct primes of `R_a`, `u,v` products of disjoint subsets, `uv|x_a` ⇒
  `Σ±⊆Rat_a(x_a)`, so the class tuple is bad ✔. Event description of `R_a=R`
  (with `m_a`) ✔.
* Step 1: `log Q≤MJ log y'≤Jℒ^{1−θ}/100≤ℒ/100` ✔ (J≤ℒ^θ); CRT class mod Q since
  `ℓ∤24` ✔; roots `p≡0`, `p≡−a` for `ℓ≤m_a` distinct (`ℓ>y>Z`) ✔;
  `Λ≤ℒ/20+ℒ/50≤log(X/Q)/4` ✔; correction `(J+1)MJ/y=o(1)` ✔;
  `e^{−λ(y,z_0)}~20ℒ^{δ−1}`, `4·20=80`, `80X≈80N/48≤2N` ✔.
* Step 2 factorisation (dropping disjointness enlarges) ✔.
* Step 3: grouping ordered tuples by class tuple and SW per class gives
  `e^{−λ}(λ+η)^kρ_k/k!` ✔; `|R|=M` case: badness inherited by `R'`, Poisson
  probability ≤1, `Σ_{m}1/m=λ`, `3^{−6L}=ℒ^{−6.59}`, `(5/9)^{6L}=ℒ^{−3.53}` ✔.

**§2.3 / Cor 2.3.** The three exponents `c−b+b log(b/c)` (Chernoff, needs `b<c`),
`b log3−θ` (`φ(a)≤ℒ^θ`), `b log(9/5)` (`2^{ω}=ℒ^{o(1)}`) ✔; all positive iff
`θ<(1−θ)log 3` ⟺ `θ<θ_*=log3/(1+log3)` ✔ (matches notes (14.21)/Thm 14.9 value
0.52349…). Uncapped: `d≥min(2(1−θ)/3−θ, 4(1−θ)/9)=4(1−θ)/9` iff `θ≤2/11` ✔;
`d(0.1)≥0.40` ✔. Uniformity of `ℒ^{o(1)}` over `a≤Z` ✔. Dyadic covering:
`O(f)` blocks, `log N'=(1+o(1))log N` since `f=o(ℒ)`, block sum `≤4N`, head
`Ne^{−f}` dominated since `d/4<1` ✔. Priority to notes Thm 14.9 correctly
acknowledged; the "not a new frontier" label is honest.

* **MINOR-4** ((2.1)): the Chernoff term should read
  `e^{−(λ+η)}(e(λ+η)/k_0)^{k_0}` with `k_0≤λ+η` (K has mean `λ+η`, not λ).
  Immaterial (η→0).
* **MINOR-5** (Lemma 2.1 Remark): "(e.g. the squares, a prime)" — the lower bound
  `2^{−k}` holds for all `a≡3 (4)` via `ker(·/a)`; worth saying since §2 is
  applied to composite a.

## §1.3 census (EVIDENCE) — reproduced exactly

`scripts/review_xw_census.py` (own sieve, own Rat enumeration, both targets −1
and −p, admissibility `p∤x_a`) reproduces every entry of the §1.3 table
bit-for-bit at `x=10^6,10^7,10^8` (e.g. `10^8`: 289372, 54226, 18868, 11250,
5125, 1742; normalised 0.229, 0.184, 0.275, 0.703, 1.375, 2.006). "Flat within
9%" ✔ (worst: Z=19, 1.313→1.427, 8.7%). Runtime 6 s.

## §3 — Goals 2–4, Proposition 3.2

* **§3.1 (Goal 2).** "Almost every W1 prime has `a_min=7`" follows from
  `T(x,7)≪x/(log x)^2=o(|𝒲_1|)` ✔ (inherits W1's "modulo cited sieve theorems");
  W2 analogue on EH with `T(x,11)≪x/(log x)^{5/2}` ✔. The "≤N/(log N)^A for every A"
  deduction ✔. "Not a finite union of classes" ✔ (a density-1 finite union of
  classes is cofinite in `p≡1 (24)`, contradicted by W1).
* **Prop 3.2: SOUND as scoped.** Jensen with weights `δ_a/D`:
  `Σδ_a log u_a≤D log(ℒ/D)≤ℒ/e` ✔. The scope paragraph is honest; the statement
  is essentially a one-line inequality about a chosen majorant shape, and the
  label "PROVED (scope limited)" is acceptable.
* **§3.2** is explicitly "no theorem" ✔.
* **MINOR-6** (§3.3, GRH and EH bullets): these are unlabeled claims. The GRH
  bullet is a proof sketch I find plausible (with `y=ℒ^C`, need `C>2θ` both for
  `(J+1)MJ/y=o(1)` and for the GRH error `φ(a)y^{−1/2}log y→0`); the EH bullet
  ("levels beyond X carry no information about integers ≤X") is an Assessment
  about this argument only. Repair: label both "Assessment (sketch)" and record
  the constraint `C>2θ`.

## Cross-checks of citations / priority

* notes Lemma 12.1 (many-root large sieve): statement and proof as used ✔.
* notes Lemma 12.5: same second moment as Lemma 2.1 ✔ ("= up to presentation" fair).
* notes Thm 70.9 is for **prime** a only; Thm 1.2 covers composite a too (new) ✔.
* notes Cor 71.4 / (71.26): uses prime moduli 3,7,11,19,23,31 and exponents
  `δ_J`; the author's comparisons (`T(N,11)`: 3/2 vs 23/30; `T(N,23)`: 3 vs
  859/990 for the extra exponent) are like-for-like on the counted event
  (`a_1(p)>a_J` is implied by `a_min>a_J`) ✔. The improvement claim is correct.
* notes Thm 14.9: `θ_*=log3/(1+log3)=0.5234946…` ✔; priority acknowledged ✔.
* External sieve theorems for W1/W2 were not re-read here (outside scope; see
  POINTWISE_WINDOW review).
