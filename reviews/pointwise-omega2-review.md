# Hostile review of POINTWISE_OMEGA2.md (branch `side-agent/omega-hub` @ 3f43543)

Reviewer: side agent (review-omega2). Scope: POINTWISE_OMEGA2.md,
reviews/agent-reports/AGENT_REPORT_O2.md, scripts/omega2_*.py as of 3f43543.
Context used: POINTWISE_OMEGA.md (PO) §1, Thm 4.1, §6.2 (H_MIN, Thm 6.2),
§9 (Lemma 9.1/9.2 setting); paper/es-omega-note.tex (definition of W, 𝓡).

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects are numbered
D1, D2, … with severity FATAL / MAJOR / MINOR / COSMETIC.

## Per-item verdicts

Bottom line: Theorem 5.1 survives. 0 FATAL, 0 MAJOR, 2 MINOR defects (D1, D2;
both wording). Defect table and overall verdict are at the end.
Reviewer scripts: `reviews/omega2-review-scripts/` (`bf_lemma12.py`,
`check_I_indep.py`).

### Item 1 — Lemma 1.1 (closed form of support-truncated B_L): **SOUND**

Re-derived. `Σ_{F⊆A, supp F⊆U}(−1)^{|F|} = I(U)` (alternating sum over the
subsets of `{E∈A: supp E⊆U}`, empty F included); Möbius on the Boolean
lattice; every `supp F⊆V`; swapping sums gives
`Σ_{W⊆V, I(W)=1, |W|≤L} Σ_{j=0}^{L−|W|}(−1)^j binom(N−|W|,j)`, and the
partial alternating row sum is `(−1)^k binom(n−1,k)` for `n≥1`. `I(V)=1` iff
`A=∅`, so for `A≠∅` only `W⊊V` occur, `N−|W|−1≥0`, and for `N≤L` every
binomial vanishes. No gap.

Independent brute force (reviewer code, written without reading the
author's script): `reviews/omega2-review-scripts/bf_lemma12.py`. Events are
arbitrary subsets of `∏_{supp}Ω_ℓ` (supports 1–3, `|Ω_ℓ|≤3`, up to 5
primes, up to 9 events), all outcomes, all `0≤L≤|𝒫|+1`; `B_L` computed by
enumerating `F⊆A(x)`. Closed form = definition in 102 277 cases (seeds
11, 12, 13), 0 failures. Mutation check (sign `(−1)^w` instead of
`(−1)^{L−w}`): 213 failures in 4 412 cases, so the test has teeth.

### Item 2 — Lemma 1.2 (pointwise minorant): **SOUND**

Re-derived: `|R_L| ≤ Σ_w binom(N,w)binom(N,L−w)=binom(2N,L)` (Vandermonde);
`f(N+1)/f(N)=2(2N+1)(N−L)/((2N+2−L)(2N+1−L))`, and with `N=L+t` the
difference denominator − numerator is `L²+3L+4t+2` (checked by hand);
`f(L+1)=binom(2L+2,L)≤4^{L+1}`; `binom(N,L+1)=e_{L+1}(1_V)≤e_{L+1}(a)` by
monotonicity. Both inequalities hold in all 102 277 brute-force cases
(same script). Observed `max |B_L|/(4^{L+1}e_{L+1}(a)) = 1/4` over cases with
`A≠∅, N≥L+1`: the constant is lossy by a factor ≥4 in practice, which is
harmless.

### Item 3 — Lemma 1.3 (mean, mass, twist reduce to `E∏(1+za)`): **SOUND**

(1) termwise `e_{L+1}(a)≤z^{−(L+1)}∏(1+za_ℓ)`; with `z=16`,
`2·4^{L+1}·16^{−(L+1)} = 2·4^{−(L+1)}`. Correct.
(2) Grouping by `U=supp F`: on a cell c of the U-coordinates the
coefficient is `κ(U,c)=Σ_{F⊆A_U(c), supp F=U}(−1)^{|F|}`; Möbius gives
`|κ|≤2^{|U|}`; κ vanishes unless every `ℓ∈U` is covered by an occurring
event (trivially, since `supp F=U` forces this). Hence
`M_1(B_L)≤Σ_U 2^{|U|}E∏_{ℓ∈U}a_ℓ=E∏(1+2a_ℓ)`. Non-unit cells get κ=0
(no event occurs at a non-unit coordinate), so the expansion is into unit
classes as PO Thm 4.1 requires (`gcd(b_i,d_i)=1`). The `G_{L+1}` expansion
has nonnegative coefficients (products of event indicators are indicators
of intersections of unit classes), so mass = mean. The brute force also
computes the exact merged cell expansion of `B_L` and checks
`M_1(B_L) ≤ E∏(1+2a_ℓ)` for every L: 0 failures.

PO Thm 4.1's `M_1=Σ|c_i|/φ(d_i)` is representation-dependent; using the
merged-cell representations of `B_L` and `G_{L+1}` separately and the
triangle inequality is legitimate. No defect.

### Item 4 — Lemma 2.1 (pseudoforest exponential-moment bound): **SOUND** (one MINOR wording defect)

Re-derived step by step.

* *Expansion.* `1+z(s+d)≤(1+zs)(1+zd)` for `s,d≥0`;
  `∏_ℓ(1+zd_ℓ)=Σ_{(U,f)}z^{|U|}1[F occurs]` with `d_ℓ=Σ_{edges e at ℓ}1_e`.
  Correct.
* *Pseudoforest.* If F occurs, at most one vertex of F per prime (vertices
  at one prime are disjoint). Choose for each `e∈F` one `ℓ` with `f(ℓ)=e`;
  e is incident to the unique F-vertex at ℓ, and distinct e give distinct
  ℓ, hence distinct vertices. So `E(K)↪V(K)` per component. Correct.
* *Multiplicity.* For fixed F only `ℓ∈π(F)` can lie in U, and `f(ℓ)` must be
  an F-edge at the F-vertex at ℓ: `≤∏_v(1+z deg_F v)≤e^{2z|E(F)|}`. Correct
  (when F has two vertices at one prime the count may differ, but then
  `P(F)=0`).
* *Singles.* Independence of `s_ℓ` (`ℓ∉π(F)`) from F; `(1+z)^{|π(F)|}≤e^{z|V(F)|}`.
  Correct.
* *Components.* F ↦ set of its components is injective, `P(F)=∏_K P(K)` or
  0, so `Σ_F∏_K w_K≤∏_K(1+w_K)`. Correct.
* *Trees.* `P(K)=P(T)` for a spanning tree (same vertex set); `≤binom(v,2)`
  extra edges. BFS encoding with nested sums, each inner sum
  `Σ_{|C|=c, C⊆N(v_i)}∏p ≤ deg(v_i)^c/c!` bounded uniformly, the root factor
  `deg(v_0)δ^{c_1−1}`, total δ-power `v−2`;
  `Σ_{c_1+…+c_v=v−1}∏1/c_i! = v^{v−1}/(v−1)! = v^v/v! ≤ e^v`;
  `Σ_{v_0}p(v_0)deg(v_0)=2S_2`. Correct.
* *Sum.* `1+(j+2)²/2=3+2j+j²/2`; I recomputed
  `Σ_j(3+2j+j²/2)e^{−j}=3·1.5820+2·0.9207+½·1.9922=7.583`, so the factor
  `2·7.583≤16` holds.

Degree condition: used only via `e^{3z+1}δ≤e^{−1}`, i.e. `δ≤e^{−3z−2}`,
exactly as stated. Remark (i) is right: a complete bipartite hub on vertices
of degree ≤δ is allowed; what is forbidden is a *vertex* of large degree,
and Lemma 2.2 removes those.

**D1 (MINOR, Lemma 2.1 *Trees*, "this is injective").** The encoding
`(v_0; C_1,…,C_v)` is injective on *rooted* trees, and every tree is
counted once per root; the subsequent bound sums over `v_0`, so the
inequality is right but "injective" should read "each tree is recovered
from (v_0, C_1, …) for every choice of root; we overcount by a factor v".
Also the edge graph must be *simple* (`C_i⊆N(v_i)`): the text never says
that two atoms producing the same class mod `ℓℓ'` give one edge. The
script dedups (`edges` is a dict keyed by vertex pair), so only the prose
needs "edges are distinct classes mod ℓℓ'; repeated atoms are merged".

Not tested numerically: the hypothesis `δ≤e^{−50}` makes any finite
instance meaningless, and the author says so (§6). The proof is short and
checked by hand above.

### Item 5 — Lemma 2.2 (forbidding hub vertices, Markov cost): **SOUND**

`Σ_{v∈H at ℓ}p(v)≤Σ_{v at ℓ}p(v)deg(v)/δ=w_ℓ/δ` because
`Σ_v p(v)deg(v)=Σ_{edges at ℓ}p(u)p(w)` (each edge at ℓ has exactly one
endpoint at ℓ, since edges join distinct primes); `Σ_ℓ w_ℓ=2S_2`.
"No new event ⇒ no old event": an old edge through `v∈H` occurring forces
`X_{ℓ_v}∈V_v⊆S^+_{ℓ_v}`. Degrees of surviving vertices only drop; vertices
in H have no edges left. Correct and genuinely cheap: under (W)
(`w_ℓ≤δ/32`) a hub vertex even has `p(v)<1/32` individually.

### Item 6 — Theorem 3.1 (abstract criterion): **SOUND**

*Citation check.* Haeupler–Saha–Srinivasan, "New constructive aspects of
the Lovász local lemma", J. ACM 58(6) (2011), arXiv:1001.1231. I fetched the
arXiv version: **Theorem 2.1** there reads "If the LLL-conditions from
Theorem 1.1 are met, … for any event B determined by P,
`Pr[B | ∧_{A∈𝒜}Ā] ≤ Pr[B]·∏_{C∈Γ(B)}(1−x_C)^{−1}`", in the variable
setting where `Γ(B)` = events of 𝒜 sharing a variable with B. This is
exactly the form used (variables `X_ℓ`, adjacency = intersecting supports).
Citation correct; the remark "immediate from the Alon–Spencer proof" is
also correct (`P(B|∩Ā)≤P(B∩⋂_{A∉Γ(B)}Ā)/P(⋂_{Γ(B)}Ā | ⋂_{A∉Γ(B)}Ā)`).

*Step 1.* Lemma 2.2 with (W): `g^+_ℓ≤1/32+1/32`; (I) persists. Correct.

*Step 2 (LLL).* Variable-setting dependency graph (supports meet) is a
valid lopsided/mutual-independence graph. Single at ℓ: neighbours = edges
at ℓ, `∏(1−x)≥1−2w_ℓ≥1/2`; edge at ℓ,ℓ': two singles (`x≤2g^+≤1/8`) and
edges at ℓ or ℓ', `≥(7/8)²(1−4δ/32)≥1/2`. With `x_E=2P(E)` the condition
`P(E)≤x_E∏(1−x)` holds. `1−x≥e^{−1.1x}` on `[0,1/8]`
(`−log(7/8)=0.1335<0.1375`). Correct.

*Step 3.* `z=16`, `δ=e^{−50}=e^{−3z−2}` — matches Lemma 2.1 exactly
(`6z+2=98`). `4^{L+1}≥200e^{Λ+λ}` gives `E|B−1[A=∅]|≤e^{−λ}/100`;
`M_1≤e^Λ+4^{L+1}16^{−(L+1)}e^Λ≤2e^Λ`; `log(M_1/μ)≤Λ+λ+log 2−log .99`.
Each term is on `≤2(L+1)` primes. All budgets
`O(S_1+(2/δ+16e^{98}+3)S_2+1)=O(Σ+1)` with an astronomical absolute
constant. Correct.

*Step 4 (twist).* μ_ψ in PO Thm 4.1 is `Σ_{i: f|d_i}c_iψ(b_i)/φ(d_i)`; the
terms with `f∤d_i` have Haar-mean-zero twist (a prime of f is a free unit
coordinate), so `μ_ψ=E_Haar[Bψ]`. f is odd (gcd with Q, 2|Q) and real
primitive, hence squarefree, with primes in 𝒫. The factorisation
`1[A=∅]=1_{Ā'}1[X_{ℓ_0}∉Forb(X_{−ℓ_0})]` is right (an event at `ℓ_0` is
the single or an edge `{u,w}`, u at `ℓ_0`, which fires iff `X_{ℓ_0}∈V_u` and
w occurs). `E_{X_{ℓ_0}}χ_0=0` swaps `∉Forb` for `∈Forb`. Conditional LLL
for "w occurs" against the sub-family defining `Ā'` (a sub-family of an
LLL family satisfies the condition with the same x): `Γ` = single and edges
at `ℓ_w`, `∏(1−x)≥(7/8)(1−2δ/32)`; the author's `(7/8)(15/16)` is looser
but fine. Final numbers: `0.01+0.064/0.936=0.0784<0.08`, `μ/4≥0.2475P`.
Correct.

No defect. The theorem is a clean, genuinely CRT-only statement.

### Item 7 — Lemma 4.1 (global mass for an arbitrary quarantine): **SOUND**

Re-derived. `1/φ(r)≪log log T/r = log log T·m/M`, `M=4A−1≥3A`. The
involution `D↦A²/D` keeps M (hence `r_Π>1`) and preserves `m|4D+1`
(multiply `4A²/D+1` by the unit D: `4A²+D≡¼+D≡(1+4D)/4≡0 (m)`, using
`4A≡1 (m)`). `D=sr'²|A²` with s squarefree implies `sr'|A` (prime by prime:
`1+2v_q(r')≤2v_q(A)⇒v_q(A)≥v_q(r')+1`), so `A=sr'k`, `k≥r'` when `D≤A`.
`m | (4sr'k−1)+(4sr'²+1)=4sr'(k+r')` and `gcd(m,4sr')=1`, so `m|k+r'`;
`(s,r',k)` determines the atom. Inner sum: the least admissible k has
`k+r'≥m` and `k≥r'`, so `k≥m/2`, giving `≤(3+log T)/m`. Final divisor
bound: `τ(4sr'²+1)≤τ*`, `Σ_{s,r'}1/(sr')≤(1+𝓛)²`. Nothing in the proof
uses the shape of Π. With the *explicit* Wigert constant
(`τ(n)≤2^{1.5379 log n/log log n}`) the exponent is
`≈1.066·𝓛/log 𝓛`; I use this below for the effectivity check.

### Item 8 — Construction 4.2 and Lemma 4.3 ((I), (W), (G), mass, log Q): **SOUND**

* *(I).* For `ℓ∈Π` every `ℓ^v‖M≤T` has `v≤e_ℓ`, so `m|Q`, `n≡1 (m)`;
  `r=1` is Fact 1.1; otherwise `n≡−4D (M)` forces `m|4D+1` and the
  single/edge `−4D mod r`. `−4D` is a unit mod M (`gcd(A_M,M)=1`), so all
  events are unit classes. The equivalence of PO's `𝓡(M)={−4D: D|A_M²}`
  with the paper's `{−uv^{−1}: uvw=A_M}` holds (`v^{−1}≡4uw`, and every
  `D|A²` is `u²w` with `uvw=A`, take `u_p=max(0,d_p−a_p)`).
* *Supports.* `r≤T<y³`, all prime factors `>y`, so
  `r∈{ℓ,ℓ²,ℓℓ'}`; no `ℓ²ℓ'`. Correct.
* *(W).* `#M=mℓℓ'≤T/(ℓℓ')`, `≤τ(A²)≤τ(A)²≤τ*²` atoms each,
  `1/φ(ℓℓ')≤4/(ℓℓ')`, `Σ_{ℓ'>y}ℓ'^{−2}≤2/y`: `w_ℓ≤8τ*²T/(ℓ²y)≤8τ*²T/y³`,
  `T/y³=e^{−6𝓛/log 𝓛}`. Correct.
* *(G).* Atoms surviving Π with `r_Π∈{ℓ,ℓ²}` and trivial 𝓑-part survive
  `Π_0` with `r_{Π_0}=r_Π` (since `m_{Π_0}|m_Π|4D+1`), so their union has
  Haar mass `≤g^{(0)}_ℓ≤1/64` (ℓ∉𝓑). Otherwise `M=mbℓ` (`bℓ²`, `b²ℓ`
  exceed `y³>T`): `≤|𝓑|T/(yℓ)` moduli, weight `≤2/ℓ`. Correct, as is
  `|𝓑|≤64S_tot(Π_0)` (union bound, `Σ_ℓ g^{(0)}_ℓ≤S_tot(Π_0)`).
* *Mass, log Q.* `Σ≤S_tot(Π)` by the union bound; `π(y)𝓛≤1.26·y·𝓛/log y<3.8y`,
  `|𝓑|𝓛=T^{o(1)}`. Correct.

*Effectivity.* With Wigert's explicit `τ(n)≤2^{1.5379 log n/log log n}`
the exponents become `≈(2.13−6)𝓛/log 𝓛` in (W) and `≈(3.2−6)𝓛/log 𝓛` in
(G); both still → −∞, and `w_ℓ≤e^{−50}/32` needs roughly `𝓛/log 𝓛≥15`,
i.e. `T≳e^{60}`. So "effective" is honest (astronomical, as disclosed).

*Independent numerical check of (I)* (reviewer code
`reviews/omega2-review-scripts/check_I_indep.py`; independent of the
author's code: 𝓡(M) built from the paper's `uvw` definition, survival
tested as `c≡1 (mod m_Π)` on classes rather than on D): `T=1000, y=T^{0.4}`
(200 forced survivors) and `T=3000, y=T^{0.36}` (100), all with `W(n)>T`,
0 mismatches; the class-of-one assertion and the support-≤2 assertion hold
for every M. Free-prime count (158 at T=1000) agrees with the author's
script. Mutation (skip the edge rejection): 20/200 mismatches, so the test
discriminates. (Thresholds `gbad=1/4`, `y=T^θ`: illustration only, as the
author says.)

### Item 9 — Theorem 5.1 (instantiation of PO Thm 4.1 / Thm 6.2): **SOUND** (one MINOR defect)

* Hypotheses of PO Thm 4.1: moduli `d_i=∏_{ℓ∈U}ℓ^{e_ℓ}`, `ℓ∈𝒫`, coprime to
  Q; unit classes (Item 3); `B≤1[W>T]` on `n≡1 (Q)` (Lemma 1.2 + (I));
  `μ>0`; twist (Thm 3.1 Step 4). Correct.
* `ℓ_0∈(R,2R]`: all prime factors of `d_i` are `≤T<ℓ_0`; the minorant
  persists on `1 mod Qℓ_0`; the set of characters to twist-check shrinks.
  `log Z≤5y+log 2R+log max d_i≤6y` since `log max d_i≤C(Σ+1)𝓛=T^{o(1)}`.
* `K≤1+C(Σ+1)=e^{O(𝓛/log 𝓛)}` (the e^{98} constant is absorbed);
  `log p≤C_1K·6y=T^{1/3}e^{O(𝓛/log 𝓛)}`. Budgets match H_MIN(θ) for every
  θ>1/3 (log Q, log max d_i ≤ T^{1/3+o(1)}, log(M_1/μ) ≤ T^{o(1)}).
* `840|Q` (`y≥7`), so `p≡1 (840)` is Mordell-hard; `p>Qℓ_0>T`.
* `W(p)>T` is certified literally: Thm 4.1 yields
  `Σ_{p≡1(Qℓ_0)} log p·1[W(p)>T] ≥ Σ log p·B(p) > 0`.
* Refuting `H_MOD(A)` (`W(p)≤(log p)^A` for all large hard p, notes
  (51.19)) for `A<3` follows. `log L_h(T)≤T^{1/3+o(1)}` follows.

**D2 (MINOR, Thm 5.1 proof, last line "Inverting, 𝓛 ≥ 3 log log p − O(log log p/log log log p)").**
The inversion needs an *upper* bound on 𝓛 to turn `O(𝓛/log 𝓛)` into
`O(log log p/log log log p)`. One line suffices: if `𝓛≥4 log log p` then
`W(p)>T≥(log p)^4` already; otherwise `𝓛/log 𝓛≪log log p/log log log p`.
Add this sentence.

### Item 10 — §6 EVIDENCE, §7 Assessment, AGENT_REPORT_O2, quick checks: **SOUND**

Replayed (under `ulimit -v 8000000`):
* `omega2_abstract_check.py 300 1` → 207 361 cases, 0 failures (1.5 s), as
  stated.
* `omega2_es.py checkI 1000 0.4 0.25 200` → 200/200 forced survivors with
  `W(n)>T`, 0 mismatches; random mode yields no void sample, as disclosed.
* `omega2_es.py 10000 0.4 0.05 2000 0.25` → reproduces the `10⁴` table row
  exactly (log Q 109.2, 1215 free primes, S_1 15.256, 3529 edges, S_2
  0.632, max w_ℓ 0.181, 555 hub vertices, hub mass 8.224, max deg after
  0.0482, `#events>N` in 0 samples). (`data/omega2/*` exist in 3f43543;
  not re-imported here.)

§6 is honest about its limits: finite-T runs are illustrations, not
instances; Lemma 2.1 is not tested quantitatively; the `N≤12` Lemma 1.2
line is vacuous at `10⁵`. §7 is correctly labelled Assessment; its
diagnosis (θ<1/3 needs per-prime smallness of H_PP type and a hypergraph
Lemma 2.1, because a k-uniform pseudoforest can close several cycles per
component) is accurate. Report numbers (≈1.37M = 207 361 + 1 166 784
brute-force cases) match the document.

## Summary of defects

| # | Severity | Location | Issue | Fix |
|---|---|---|---|---|
| D1 | MINOR | Lemma 2.1, *Trees* ("this is injective"); Setting 2.0/Constr. 4.2 | encoding is injective on rooted trees (overcount ×v, harmless); simplicity of the edge graph (repeated atoms giving the same class mod ℓℓ' are one edge) is used but not stated | reword; add "edges are distinct classes mod ℓℓ'" |
| D2 | MINOR | Thm 5.1 proof, last line ("Inverting, 𝓛 ≥ 3 log log p − O(…)") | needs an upper bound on 𝓛 to convert `O(𝓛/log 𝓛)` | add: "if 𝓛≥4 log log p then W(p)>T≥(log p)^4; else 𝓛/log 𝓛 ≪ log log p/log log log p" |

No FATAL or MAJOR defect found.

## Overall verdict

| Item | Verdict |
|---|---|
| Lemma 1.1 | SOUND |
| Lemma 1.2 | SOUND (independent brute force, 102 277 cases, 0 failures) |
| Lemma 1.3 | SOUND (mass bound also brute-forced) |
| Lemma 2.1 | SOUND-AFTER-REPAIRS (D1, wording only) |
| Lemma 2.2 | SOUND |
| Theorem 3.1 (incl. HSS citation, Step 4 twist) | SOUND |
| Lemma 4.1 | SOUND |
| Construction 4.2 / Lemma 4.3 | SOUND (independent check of (I)) |
| Theorem 5.1 | SOUND-AFTER-REPAIRS (D2, one sentence) |
| §6/§7/report | SOUND |

**Headline.** I could not break Theorem 5.1. `H_MIN(θ)` for every θ>1/3
and `W(p) ≥ (log p)^3·exp(−C log log p/log log log p)` for infinitely many
Mordell-hard p are correct modulo PO Theorem 4.1 (Thorner–Zaman), after the
two MINOR textual repairs. The proof idea holds up: truncating by
*support size* puts the error on primes, not events, and the Markov
quarantine of high-degree vertices is enough for the pseudoforest moment
bound. Label suggestion: **PROVED modulo Thorner–Zaman (via PO Thm 4.1)**,
same standing as PO Thm 5.1.
