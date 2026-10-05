# Review R45b of POINTWISE_OMEGA12.md (reviewer 2 of 2: §6–6B, the exponent assembly)

Reviewer: hostile side agent (branch side-agent/review-omega12b). Reviewed: POINTWISE_OMEGA12.md at
`side-agent/homega` 1eeefea (merged non-ff into this branch, since main had moved on).
Scope: Thm 6.1, Lemma 6.2, Thm 6.3, Haar corollary, §6A last para, §6B table; their use of O11
Lemma 1.1/Cor 1.2/Lemma 2.1/Lemma 2.2/Lemma 3.1/Thm 3.2/Cor 3.3/Cor 4.1 and O9 Thm 1.1.
Thm 5.1 (H_ω(2)) and §§1–4 are taken as given (other reviewer), except where noted.

STATUS: round 1 complete. **No FATAL, no MAJOR defect found in my scope.** 3 MINOR + 1 cosmetic.

## Summary verdicts

| claim | verdict |
|---|---|
| Thm 6.1 (`(log p)^{1/5}(loglog p)^{−2/5}`), as implication from Thm 5.1, ET, (G), O10 Thm 3.4 | **SOUND** |
| Lemma 6.2 (pre-quarantine `ℓ≤𝓛`, `s_1=e³g/M`, LLL `Σw≤c`, (I), cost `1.02𝓛+7`) | **SOUND** (m2, m4) |
| Thm 6.3 (`(log p)^{1/5}(loglog p)^{−1/5}`; bottleneck = quarantine charge `𝓛Ω_0`) | **SOUND** |
| Haar corollary `log(1/δ*)≪𝓛^5log𝓛` | **SOUND** (m1: needs only ET) |
| §6A last para / §6B last row (`Ω_0≍𝓛^4log𝓛`, CONJECTURE) | label OK; "EVIDENCE" parenthetical overstated (m3) |

## Defects

No FATAL. No MAJOR.

* **m1 (MINOR, §6B table row "Lemma 6.2, Thm 6.3" and Thm 6.3's last display).** The row lumps
  `log(1/δ*)≪𝓛^5log𝓛` under "PROVED mod (G), ET, OMEGA10 Thm 3.4". The Haar bound uses only the local lemma
  and the quarantine (O11 Cor 3.3 is labelled "PROVED modulo ET"). *Repair:* split it into its own row,
  "PROVED mod ET Prop 1.4/Thm 7.1/Cor 7.4/(7.10)" (the ET inputs of Thm 5.1).
* **m2 (MINOR, Lemma 6.2 / §7).** For every `T<e^{11}≈6·10^4` the odd primes `≤𝓛` are among `{3,5,7}`, so
  Lemma 6.2's start is identical to O11's at every T in §7's tables; the document has no numerical check of
  the lemma and the reader might think the `10^4..10^6` data illustrate it. *Repair:* one sentence saying the
  lemma is vacuous at computable T (my D3 stress-test with a pre-set range `y=30,200` found
  `max P(E)/(e³g/M)≤0.063`, LLL sums `≤c`; cite or reproduce if desired).
* **m3 (MINOR, §6A last para, §6B last row).** "CONJECTURE (EVIDENCE at 3 values of T)" for `Ω_0≍𝓛^4log𝓛`.
  The §7 data support only the growth of the *mean* `Ω_0'/S_0'` (2.16, 2.40, 2.62 vs `log𝓛`=2.22, 2.44,
  2.63). The normalised quantities *decrease*: `S_0'/𝓛^4 = 0.00400, 0.00330, 0.00288` and
  `Ω_0'/(𝓛^4log𝓛) = 0.00389, 0.00325, 0.00287` at `T=10^{4,5,6}`. So the `≍` (in particular `S_0≫𝓛^4`, which
  §5 says is not proved) has no numerical support at these T. *Repair:* "CONJECTURE; EVIDENCE only for the
  mean of h growing like log𝓛; the order of `S_0` is unknown (normalised `S_0'/𝓛^4` still decreasing at
  `10^6`)". The headline is unaffected (it only uses upper bounds).
* **m4 (cosmetic, Lemma 6.2).** (a) "`log(8·105·∏_{ℓ≤𝓛}ℓ)`" double-counts 3,5,7 and includes 2; the actual
  start is `Q=8∏_{odd ℓ≤max(𝓛,7)}ℓ`. Harmless upper bound; say so. (b) The number of unramified primes
  `ℓ|M` with `ℓ>𝓛` is `≤𝓛/log𝓛`, so the Euler factor is `≤exp(𝓛/((𝓛−1)log𝓛))=1+o(1)`; `e³` (via
  `ω(M)≤1.45𝓛`) is valid but very crude (observed ratio ≤0.063·e³≈1.27). Optional.

## Derivations

### D1. Lemma 6.2 (re-derived)

* Fibre probability (O11 Setting 2.0): coordinate `X_ℓ` uniform on the fibre `1+ℓ^{a}ℤ mod ℓ^{f}` (units if
  `a=0`). Fixing `X_ℓ mod ℓ^v` (`v>a`) has probability `ℓ^{−(v−a)}` if `a≥1` (the fibre mod `ℓ^v` has `ℓ^{v−a}`
  elements, uniform), `1/φ(ℓ^v)` if `a=0`. Off supp (`v≤a`) the factor is 1 and `ℓ^v | gcd(M,Q)`. So
  `P(E)=∏_{ℓ∈supp,a≥1}ℓ^{a}/ℓ^{v}·∏_{ℓ∈supp,a=0}(ℓ/(ℓ−1))ℓ^{−v}·1 = (gcd(M,Q)/M)·∏_{ℓ∈supp,a_ℓ=0}ℓ/(ℓ−1)` — an
  *equality*, matching the author's display. ✓
* Monotonicity: the procedure only raises exponents, so `a_ℓ≥1` for every odd `ℓ≤𝓛` at every stage; hence
  `a_ℓ=0 ⇒ ℓ>𝓛`. Need `a_ℓ=1≤f_ℓ=⌊𝓛/logℓ⌋`, i.e. `ℓ≤T`: true since `𝓛≤T`. ✓
* Euler factor: `ℓ>𝓛 ⇒ ℓ−1>𝓛−1≥1`, number of such `ℓ|M` is `≤log M/log𝓛 ≤ 𝓛/log 𝓛` (author uses the cruder
  `ω(M)≤1.45𝓛`). `∏(1+1/(ℓ−1))≤exp(#/(𝓛−1))≤exp(1.45𝓛/(𝓛−1))≤e^{2.9}` at `𝓛=2`, decreasing in 𝓛. ✓
  (Sharper: `≤exp(𝓛/((𝓛−1)log𝓛))→1`; irrelevant to the exponent.)
* `gcd(M,Q)|g` by survival (`gcd(M,Q)|4D+1`). So `P(E)≤e³g/M=s_1`. ✓ (from-scratch check: D3.)
* Start cost: `Q_start=8·∏_{odd ℓ≤max(𝓛,7)}ℓ`, `log Q_start≤log 840+θ(𝓛)≤6.73+1.01624𝓛` (Rosser–Schoenfeld
  1962 Thm 9: `θ(x)<1.01624x` for `x>0` — correct citation). ✓
* Cost of the iteration: O11 Lemma 2.2's charging sums, over the *steps actually taken* `(ℓ,a→a+1)`,
  `logℓ<𝓛w_ℓ(Q_i)/(c(a+1))≤(𝓛/c)Σ_{v_ℓ(M)≥a+1}s_1/(a+1)`. The pre-set steps `(ℓ≤𝓛, 0→1)` are not charged
  (paid by `θ(𝓛)`), so the sum over taken steps is `≤(𝓛/c)Σ_{(M,D)}s_1·h(M)`. The only Lemma 2.1 input is
  `w_ℓ(Q_i)≤Σ_{v_ℓ(M)≥a+1}s_1`, valid at every stage `Q_i` because `P(E)≤s_1` holds for every Q reached (not
  for every Q — the author correctly says "every Q reached"). ✓
* (LLL): unchanged — at termination every `ℓ` with `a_ℓ<f_ℓ` (in particular every pre-set ℓ that remains a
  coordinate) has `w_ℓ≤c(a_ℓ+1)logℓ/𝓛`; `ℓ∈supp E ⇒ a_ℓ+1≤v_ℓ(M)`; sum `≤c·logM/𝓛≤c`. The stopping test is
  applied to the pre-set primes too (the loop ranges over all odd ℓ with `a_ℓ<f_ℓ`). ✓
* (I): O11 Lemma 2.1's (I) proof uses only `n≡1 (Q)` and Fact 1.1, no structure of Q. ✓

**Verdict Lemma 6.2: SOUND** (pending numerical check D3).

### D3. From-scratch numerics for Lemma 6.2 (`scripts/review_o12b_quarantine.py`, `data/review_o12b/quarantine.txt`)

Own implementation: all atoms `D|A_M²` (69 106 at `T=10^4`), atomic iteration (all violators raised per round),
exact fibre probabilities. EVIDENCE only:
* At every `T≤e^{11}≈6·10^4` one has `{odd ℓ≤𝓛}⊆{3,5,7}`, so Lemma 6.2's start **coincides** with O11's at
  every T where anything can be computed (confirmed: identical runs at `10^3,10^4`). To exercise the mechanism
  I added a pre-quarantine bound `y≥𝓛` (y=30, 200): every surviving atom at every stage has
  `P(E)/(e³g/M) ≤ 0.063` (so `P(E)≤s_1` with ample room; the e³ is very loose), `max_EΣ_{supp}w_ℓ ≤ c` at
  `c=1/64` (0.01437) and `c=1/8` (0.1032), and `log Q ≤ log Q_start + (𝓛/c)Ω_1` by orders of magnitude.
* Start cost `log Q_start=log 840=6.73≤1.02𝓛+7` at `y=𝓛` ✓ (the "False" lines in the data are for `y>𝓛`,
  where the `1.02𝓛+7` bound is not claimed).
* Atomic `T=10^4,c=1/64`: `log Q=1944`, 293 primes, `max Σw=0.01437`; author's distinct-event variant
  (O11 table): 1900, 287, 0.0144 — consistent with R44a's remark that the variants differ slightly.

### D2. Exponent chain (Thms 6.1, 6.3, Haar corollary), re-derived

Ingredients and their sizes (`c=1/64`; ≪-constants absolute, T large):

| term | Thm 6.1 (O11 start, `s=C log𝓛·g/M`) | Thm 6.3 (Lemma 6.2 start, `s_1=e³g/M`) |
|---|---|---|
| start cost | `log 840` | `≤1.02𝓛+7` |
| quarantine charge `(𝓛/c)Σ s·h` | `64𝓛·C log𝓛·Ω_0 ≪ 𝓛^5(log𝓛)^2` | `64e³𝓛Ω_0 ≪ 𝓛^5 log𝓛` |
| `S_tot(Q)≤Σs` | `≪𝓛^4log𝓛` | `≤e³S_0≪𝓛^4` |
| junta `τ=2𝓛⌈log₂(100m²(S+1)e^{3S})⌉`, `m≤T²` | `≈(6/ln2)𝓛S+O(𝓛²) ≪𝓛^5log𝓛` | `≪𝓛^5` |
| cell moduli of B `≤e^{2τ+3𝓛}`, `ℓ_aux≤2max(T,e^{2τ+3𝓛})` | `≪𝓛^5log𝓛` | `≪𝓛^5` |
| `log Z=log(Qℓ_aux)+log max d_i` | `≪𝓛^5(log𝓛)^2` | `≪𝓛^5log𝓛` |

* Bottleneck in both: the quarantine charge (as the author says). In Thm 6.3 the junta is smaller by a
  factor `log𝓛`, so the next improvement would have to come from `Ω_0` (author's §6A last para) ✓.
* Transfer (O11 Lemma 3.1 = O9 Thm 1.1 with fibre cells): `log x ≥ C_2(1+log A)log Z` with `A≤1.03`
  (O9 Lemma 2.1, needs `E[F−B]≤δ/100`, supplied by BRW with EL_mod: `m²·S_tot·e^{−3S}/(100m²(S+1)) ≤
  e^{−3S}/100 ≤ δ/100` as `δ≥e^{−2.2S_tot}`, any `S≥S_tot` may be used in τ). μ enters O9 Thm 1.1 only via
  A, so no `log(1/δ)` term; `A≤Z^{1/4}` trivially. Hence `log p≤log x≪log Z` ✓. `p≡1 (840)` ⇒ Mordell-hard ✓.
* Conversion: `log p ≤ K𝓛^5 log𝓛` and `log𝓛 ≤ log log p` (since `p>T`) give
  `𝓛 ≥ K^{−1/5}(log p)^{1/5}(log log p)^{−1/5}`; `W(p)>T=e^𝓛` ✓. Likewise `(loglog p)^{−2/5}` for Thm 6.1 ✓
  (matches O11 Cor 4.1 with `B=2`; O11 Cor 4.1 reviewed SOUND in R44b). The direction of the loglog
  substitution is the safe one.
* Twist (O8 Lemma 3.3 as used in O11 Thm 3.2): needs only `1.07w_{ℓ_0}≤0.02` and neighbourhood sums `≤1/32`;
  `ℓ_0` coprime to Q is a coordinate (`a=0`), so `w_{ℓ_0}≤c logℓ_0/𝓛≤c`. The extra fact `ℓ_0>𝓛` is true but
  unused ✓.
* Cell consistency: O11's argument is for any graded Q (pre-set fibres included) ✓.
* Haar corollary (`c=1/8`): `log Q≤1.02𝓛+7+8e³𝓛Ω_0≪𝓛^5log𝓛`; LLL with neighbourhood sums `≤1/4` gives
  `δ≥exp(−2·2ln2·S_tot)≥e^{−4S_1}` on the class of one, and `δ*≥δ/φ(Q)` ✓. Needs only ET (not (G), not O10
  Thm 3.4) — see m1.
* Unconditional remark ("nothing changes without ET"): `S_0` is then only `exp(O(𝓛/log𝓛))`, which dominates
  everything; Lemma 6.2 removes a `log𝓛` from a quantity that is already super-polynomial. ✓

**Verdicts: Thm 6.1 SOUND; Thm 6.3 SOUND; Haar corollary SOUND (label slightly over-hypothesised, m1);** all
as implications from Thm 5.1, ET, (G), O10 Thm 3.4 — no hidden parameter-dependence of constants found
(`c, C_1, C_2, A` absolute; Lemma 6.2's pre-set range `ℓ≤𝓛` depends on T but is paid explicitly).
