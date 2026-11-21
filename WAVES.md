# WAVES — chronological log, newest first

*One entry per wave, **at most 12 lines** excluding the heading. Waves before z53 are grouped. Write the entry at wave
export, following `AGENTS.md` §2–§3. Each entry has four parts:*
* *`+` positive results (with a label and a file);*
* *`−` negative results, compressed to one or two lines;*
* *`→` targets the wave opened or closed;*
* *`R` review status.*

*Items that pass the STATUS gate (`AGENTS.md` §3) are promoted to `STATUS.md`: records, refutations and target changes.
The `−` lines only compress; full scopes are in the cited notes and FRONTIER §6. Waves before z44 are in `STATUS_HISTORY.md`
(ledger (J)1–(J)110) and in `DISCOVERIES.md`.*

### z79 (2026-11-21): GPT-6.2 Astra 7-lane multi-round burst — R(n) ≪ n^{6801/21497+ε}, sterile r ≥ 149 (+137) & depth-14 at 17, Type I/II log³p & 3/4 primorial tails, cubic/quadratic 3/4 pullbacks, cofinal-PA/IE₁⁻ (Sep)
`+` PROVED (analytic record), unconditional for every `n ≥ 2`: **`R(n) ≪_ε n^{6801/21497+ε}`** (≈ 0.316370, rel. z78 §§7,13, Weil, twice-used stationary phase, divisor/2nd-derivative bounds and Trudgian–Yang *Math. Comp.* 2025 Lemma 1.1 + B-transform; Bourgain fallback `999/3157`, classical no-exponent-pair fallback **`25/79`**, intermediate `13/41`; two independent Opus reviews incl. `REVIEW_ANALYTIC_PUSH_6801_OPUS2.md`, superseding z78 `46/145`) via exact second conductor differencing, signed `ℓ`-pooling, second Poisson transform and `k(Q+k)` product multiplicity; uniform numerator (`M≥1`, `θ∈{6801/21497, 999/3157, 25/79}`): **`R_M(n) ≪_ε n^ε[1 + min{n^θ M^{1−5θ}, (n/M²)^{1/3}}]`** (CONDITIONAL on EPC: `n^ε[1+(n/M²)^{4/13}]`; `notes/z79/ANALYTIC_PUSH.md`).
`+` PROVED (almost-all & primorial-fibre lower bounds, `notes/z79/LOWER_TAIL.md`, 5 Opus reviews): rel. BV (all primes, fixed `ε > 0`), **`R(p) ≥ (9/(32π²)−ε)log²p`** (third disjoint small-`4ab` chart + equal-sum spike cut) and **`f_II(p) ≥ (1/(896ζ(3))−ε)log³p`** (settling `Z53_PZ` §9.5 Conj. B) outside `O_ε(π(X)/logˢX)` (`s=2,3`); at smaller `c_A`, all three (`R ≫_A log²p`, `f_II ≫_A log³p`, Type I `f_I ≫_A log³p` rel. BV, BT; external Type I priority unverified) hold outside `O_A(π(X)/log^A X)` and relatively on shallow primorial fibres `p ≡ 1 (Q_σ)` (`0<σ<σ_A`, rel. `(G)` or CONDITIONAL on GRH; truncated bulk counts concentrate); also `exp(−c L^{3/4})` (`f_I, f_II`) and `exp(−c L^{2/3})` (`R`) primorial tails at smaller thresholds `L^{3/4}, L^{2/3}` (`0<σ<1/2` CONDITIONAL on GRH).
`+` PROVED (polynomial pullbacks & HJ height, `notes/z79/WILD_ES.md`, 3 Opus reviews): `3/4` ES exceptional-set bound transfers to parameter intervals of positive values (`a>0`, coeff. `≤exp(b(log H)^{1/4})`) of **nondegenerate quadratics** (incl. simultaneous `j²+d`), **all integral cubics** (odd-permutation fixed point + quadratic ideal norm pruning), and fixed-degree binomials (nonzero shift if even), plus genuine word tails on squarefree `sj²` (unrestricted parameters lose `(log log H)^{-1/3}`) and eligible primorial fibres; **HJ3** (self-contained energy proof): for each fixed `κ < 1/3`, infinitely many `p ≡ 1 (840)` have finite least good HJ denominator `A_min(p) > exp((log p)^κ)` (subsequence without `(G)` rel. Montgomery/Landau–Page; every admissible large prime `f` rel. `(G)`).
`+` PROVED (coverings, computer-assisted, `notes/z79/R17_ALLDEPTH.md`, 2 full Opus replays + independent C/Python P-endpoint re-implementation): sterile Mordell points exist for every prime **`r ≥ 149` and `r = 137`** (slashing 293 → 149, 28 of 55 gap primes cleared; exact integer/rational Chebyshev-Vandermonde & run-DP ledger on `[149,283]∪{137}`, no libm; inherited z78 libm dependencies retained for `r ≥ 919`; 27 primes remain; `r = 13` covered at level 1). CERTIFIED: at `r = 17`, `5` and `1/5` survive all seven families through **depth 14** (4-index P search of short-index bound `O((17^L)^{2/5})` + inherited Q≤15). PROVED: integral Vieta Q-descent (`pq | V ⇒ dh ≤ (p+q)/2+√(pq)`, excluding Q hits at `5 | 4dcH−6` for `x=5`, `7 | V` for `x=7`).
`+` PROVED (thin families & moving depth, `notes/z79/PROTH_ALLM.md`, `ES_ENGINE.md`): full all-exponent `ES((4^m−1)2^s+1)` for **`m = 11, 12`** (`1 ≤ m ≤ 12`); reflected cubic norm `ord([3]) | 2·3^{j−1}` giving infinite cores at every `v₃(h) = j ≥ 1` (full progression-relative density for qualifying `3 ∥ h`; `3^j|s` or `3∤s` for `j>1`), exact `h = 3^j` layerwise sign subgroup (`+1` at 7, `ord | 6·3^{j−6}` modulo `U_j` for `j≥6` rel. z78 anchor), `6 | [units:R]` for `9 | h`, odd-order `h = 7^{4t+2}`/8-prime (`h≡−1(5)`) cores, and infinite `m` with ES outside 28 classes mod 3,825,360 + density-1 good words inside each; `24(a³+b³)−23` on positive `(1,0) mod 35, (5,17) mod 23` (`N^{2/3+o(1)}` `U₇` values), Baier–Zhao `q² | p+u` primes, and linear-sieve mandatory depth `d(X)→∞` among divisors `A ≤ X^γ, A ≡ −1(u)` at one selected shift per block on `≥ X/(log X)^{2+o(1)}` primes.
`+` PROVED (logic, `notes/z79/IE1_BASE.md`, 3 Opus reviews): over ANY countable PA base, a fresh ES-failing prime `P ≡ 1 (d)` in normal `IOpen + Lag` coexists simultaneously with cofinal-PA Pell (nonsquares in the cofinal PA subring), all standard balanced norm & positive-rank elliptic windows (all isogeny classes), and z78 height windows; separate seeds `P = 1+UV` (face rigidity: 2–3 `(Sep)` at `P−1`) and `P = 1+T!X` (strict PA square specialization: `R/P` & `R/X` fields, `(P−1,T!)` principal, all prime-primary least tests at `P−1`, lock at `P−1−T!`). Positive `IE₁⁻`: parameter-free Farey/Bézout, `(Sep)`, proper reduction of positive-definite integral binary forms, conditional Hurwitz 4-square descent, stable range 1 for `R/hR` (`h>1`).
`−` Barriers / method-cx: **BARRIER-BROAD** (`IE1_BASE.md` §§4, 7–8, 13) — `IE₁⁻ ⊢ (Sep)` puts every nonzero prime ideal in a unique maximal (Gelfand nonzero principal quotients), 2–3 split excludes unital domain maps with `0≠ker e⊆2R∩3R` and a 2–3 shared axis (`(Sep)` excludes finite shared BCM axes), nonstandard PA subring forces continuum-many minimal primes over some `hR` (`h∈B`), pole-descent towers freeze `P−1` factors; same-band Selberg product-law `d/(d+1)` floor & Plancherel `6/19` Fejér coherence (`ANALYTIC_PUSH.md` §§1, 7); squarefree-base gap-9 covariance counterexample (`LOWER_TAIL.md` §8); odd-`ord_p(2)` (`p≠3`) reflected-product gluing obstruction & odd-power `p≡7(8)` boundary (`PROTH_ALLM.md` §§6–7); `2j²` zero `U₇` words (`WILD_ES.md` §5); `ℤ₁₇` local-congruence insufficiency (`R17_ALLDEPTH.md`).
`→` Closed: `Z53_PZ` §9.5 Conj. B; Type I almost-all `log³p`; sterile `149 ≤ r ≤ 283` + `137`; Proth `m = 11, 12`; all-isogeny simultaneous window model; z79 `6801/21497` (`25/79`, `999/3157`, `M^{1−5θ}`) twice Opus-reviewed (`46/145` second review closed earlier in z78 housekeeping `c66c0b62c`). Open: ES, `IE₁`/`IE₁⁻`/`IΔ₀`, 27 primes `17 ≤ r ≤ 139` (`r ≠ 137`), Proth all-`m` core & infinite all-`s`, `θ > 3/4` on `E(N)`, breaking `6/19` toward `3/10`.
`R` All 7 lanes by GPT-6.2 Astra (`deep`), 2–3 rounds each; every round independently Opus-reviewed (`data/z79/xreview/`, **21** Opus reviews total); `6801/21497` (`25/79`, `999/3157`, `M^{1−5θ}`) has a second independent Opus review on main (`REVIEW_ANALYTIC_PUSH_6801_OPUS2.md`, ACCEPT); `R17` R2 independently replayed byte-for-byte + independent C/Python P-endpoint search with different cutoffs; `ES_ENGINE` R1 AP overclaim caught and withdrawn. None owed.

### z78 (2026-11-20): GPT-6.2 Astra 6-lane multi-round burst — F₃[T] Conj. 0.2 proved, R(n) ≪ n^{46/145+ε}, sterile r ≥ 293, BCM+QR+TS model, Proth m ≤ 10
`+` PROVED (function fields): **F₃[T] Conjecture 0.2** — for `q = 3`, `A = T²` both designated slice points `x*_c` are uncovered, so there is no finite linear covering (rel. the tuple/parity and minimum-level reductions and Mason–Stothers: two-sided reconstruction, two log-derivative contacts forcing `deg g′ < N` and a monic T-unit determinant `W` of degree ≤ 1/≤ 2, then a third exact elimination; `notes/z78/F3_CONJ.md`; `F3Endpoint.lean` checks only the large-level §6 algebra; CERTIFIED separately: brute force N = 4..15, filtered census to N = 38).
`+` PROVED (analytic record), unconditional for every `n ≥ 2`: `R(n) ≪_ε n^{46/145+ε}` (≈ 0.317241; two independent Opus reviews, superseding intermediate 20/63 and 272/857, also twice-reviewed) — positive conductor average before the B-process, fourth moment, Erdős–Turán spacing with third-derivative test in common quartic bands; uniform `R_M` bound. CONDITIONAL on Dirichlet GRH: `log(1+e*(n)) ≤ (2√2+o(1))√(log₂R·log₃R)` (method constant, not a lower bound) (`notes/z78/ANALYTIC_WILD.md`).
`+` PROVED (coverings), computer-assisted: sterile Mordell points on the r-generic line for every prime **r ≥ 293** (round 1: `r ≥ 919` rel. SE/ZL/z77 incl. inherited libm rows and BBR 2012, Opus caught and fixed a nesting-order error; round 2: on [293, 919) the integer/rational ledger, including tail envelopes, uses BBR 2012 Thm 1.2, the reduction, z76/z77 lemmas and round-1 integer inputs (packed bounds and layer/P₇ tables), but no libm-dependent row; it starts from exact depth-three unions and uses exact P₇ counts where available. The round-2 margin is smallest at 293 and exceeds 2,427 ppm there. Opus independently reproduced all 95 depth-three rows for primes 293..911 and all nine load-bearing exact P₇ new-cell counts; every prime 17..283 fails this sufficient bound, which is not coverage; `notes/z78/R17_PUSH.md` §§7–11, `R17_R2EXACT.md`). CERTIFIED: exact `L1+P₃+Q₃+P₅` marginal unions for every prime `5 ≤ r ≤ 211` (`R17_EXACT.md`); at `r = 17`, 5 and its inverse survive all seven families through depth 11 (not all-depth).
`+` PROVED (thin families): full `ES((4^m−1)2^s+1)`, all `s ≥ 0`, for `m = 7, 8, 9, 10` (computer-assisted); good-word core progressions with square-unit closure and density one on each fixed exponent progression for `2 ≤ m ≤ 131`, `m = 365` (certificates) and `h = 2m−1 = 4^i+1` (two independent lanes) or `2^{12t+6}+13` (hand proofs); for `h = 7^i` an explicit progression of y gives good words at `(2^{h+1}−1)y³+1 ≡ 1 (840)`. **Lean 4**: `proth_four_pow_core` (ES on positive multiples of a period depending on i), `proth63` (every s); density and noncovering not formalised (`notes/z78/PROTH_ALLM.md`, `WILD_ES.md` §1).
`+` PROVED (logic): one `IOpen + Bézout + BCM + Lagrange + full prime QR + universal TS` model with `¬ES(P)` (not an external PID; fails `L(Div)`). Three separate normal `IOpen + Lag + PW` ES-countermodels: the multiquadratic-height one misses the cubic norm window `C₃`; the all-standard-balanced-norm one misses `Ell(y²=x³−2)`; the third fills those and that elliptic window but misses `Ell(y²=x³−36x)`; none satisfies `IE₁⁻`. Separately, over any countable PA base a normal `IOpen + Lag` end extension has a fresh ES-failing prime with the specified pointed height windows and misses the `√2` window (`notes/z78/IE1_UNITS.md`).
`+` PROVED (disproof side; rel. ET, mean-value and internal energy/transfer inputs): for each large prime `f ≡ 3 (4)` some `p > f` has seven-chart ET minimum `H_ES(p) = f`; infinitely often all seven period searches exceed `exp((log p)^κ)`, `κ < 1/8` (PNT) or `κ < 1/4` (Gallagher, or GRH); CERTIFIED 192 panel minima (`WILD_ES.md` §6; not every coordinate or search grammar).
`−` Barriers / nulls: **BARRIER-BROAD** window barriers for `IE₁⁻` (cubic unit descent in the §4 towers, elliptic windows, end extensions cannot repair an old bounded miss; the no-lock fair-chain route stays open; `IE1_UNITS.md` §§4–15); mock-row lower-bound obstruction below 3/10 for the signed-Cauchy norm, cap-menu and MPZ-depth limits (`ANALYTIC_WILD.md`); bounded-menu rigidity for Proth cores (`PROTH_RIGIDITY.md`); integer port of the F₃ elimination at `r = 17`, `x = 5`: P hits need `e ≤ 466(rN)^{1/4}`, ineffective Subspace finiteness per square class, abc-conditional exclusion of deep P hits with `de ≤ N^θ` (`R17_ENDPOINT.md`); bounded tame/nonabelian blindness at 8/131, 8/241 and no positive integral move to a larger prime on the four-line open (`WILD_ES.md` Thms C, C.2, J); Assessment: Masullo's unrefereed GRH announcement is NULL for B2 (`MASULLO_GRH_TRANSFER.md`).
`→` Closed: F₃[T] Conj. 0.2; universal TS in a BCM+Lag+QR model; Proth `m = 7..10`; sterile range `293 ≤ r < 7,219`. Open: ES, `IE₁`/`IE₁⁻`/`IΔ₀`, primes `17 ≤ r ≤ 283`, Proth core for arbitrary m and all exponents for `m > 10`, `θ > 3/4` on `E(N)`.
`R` All six lanes by GPT-6.2 Astra (`deep`), 2–4 rounds each; all merged work has Opus reviews (`data/z78/xreview/`). R17 has two Opus replays (round 1 at 919, round 2 at 293; replay gaps fixed). 20/63, 272/857 and 46/145 (`REVIEW_ANALYTIC_WILD_46145_OPUS2.md`, ACCEPT) have two independent Opus reviews each. The orchestrator hand-checked F3_CONJ §6 and rebuilt the merged Lean tree (`data/z78/lean/main_merged_build.txt`). Masullo skim (research mode) superseded by an Opus grading, Astra-reviewed. Astra consistency review of export 3176d7132: changes required, applied in 168e1aff6; the 293 update was merged afterwards.

### z77 (2026-11-20): GPT-6.2 Astra 5-lane burst — sterile r ≥ 7,219 (level-1 gap closed), bounded étale-BM blindness, (4^m−1)2^s+1 (m≤6) & ∞ c·2^s+d
`+` PROVED (coverings & thin families): sterile Mordell points on the r-generic line exist for every prime **r ≥ 7,219** (393× total drop from 2.84·10⁶, rel. SE/ZL/z76 inputs), and exact level-1 union (CERTIFIED 17 ≤ r ≤ 181,391 + z76 tail) closes the level-1 survival gap (`notes/z77/R17_F3.md`); full ES for **`(4^m−1)2^s + 1` (m = 4, 5, 6: k = 255, 1023, 4095)** via moving cyclotomic products and for **infinitely many fixed-base-2 pairs `c_J·2^s + d_J`** with distinct odd `c_J` and no finite ET/divisor cover (`notes/z77/PROOF_S_WILD.md`).
`+` PROVED (broad barrier): **bounded-exponent étale-Brauer blindness** on `S_n°, X_n°, U_n°` (`s ≠ 1` for `k = 4`, `s ∉ {1,2}` for `k = 8`, outer-integral positive adeles) — for fixed `(m, M)` a `q^{mM}` repair lifts to some rational twist of every finite ℚ-group torsor of geometric monodromy exponent dividing `m` orthogonal to `Br(W)[M]` (incl. `(x,y)` for even `m, M`); `mM | E` is sharp for the specified one-coordinate repair on the simultaneous coordinate cover (`notes/z77/DISPROOF_KUMMER.md`).
`+` PROVED (logic structure): `C ⊊ D ⊊ R` BCM+Lag+QR ES countermodel over a nonstandard true-arithmetic cut `C⁺ ≡ ℕ` with global cut-coefficient linear minimization (`D` has TS/`L(Div)`, `R` fails both and lacks Pell windows); separately, exact multiquadratic unit-height equivalence `H(A*) = Γ⁰[G]` for simultaneous Pell windows in integrally closed `IOpen` proper end extensions of a PA cut (`IE₁⁻` forces it on standard-prime systems; `notes/z77/IE1_NONPID.md`).
`−` Barriers / nulls: unchanged z76 BCM successor fails TS and `L(Div)`, ordinary-only rotations fail at a forced circle class (`IE1_NONPID.md` §5); primorial-fibre sharpness forces `(log log H)^{1/3}` loss for many short witnesses at z75 all-integer height + Assessment of a `n^{1/20}` deficit at `θ = 3/10` for the hypothetical `W^{1/2}` kernel majorant (`ANALYTIC_413.md`); `𝔽₃[T]` orientation-A `deg M ≥ ⌈(N+1)/2⌉` (`F3_TARGET.md`); 23.3M square-offset primes & 1.88M composites (`DISPROOF_KUMMER.md`), 7,771-prime U₇ panel (`PROOF_S_WILD.md`) give no refutation.
`→` Closed: level-1 survival gap `2·10⁴ ≤ r < 177,505`, Proth `(4^m−1)2^s+1` for `m = 4, 5, 6`, bounded-exponent upstairs étale-BM on coordinate opens. Open: ES, `IE₁`/`IE₁⁻`/`IΔ₀`, `17 ≤ r < 7,219` (Conj 4.2), `𝔽₃[T]` Conj. 0.2, `θ > 3/4` on `E(N)`.
`R` All 5 lanes authored by GPT-6.2 Astra (`deep`), orchestrated by Fable (`best`), and independently cross-reviewed by Claude Opus (ACCEPT or ACCEPT-WITH-FIXES, fixes applied; two passes on `IE1_NONPID` and `DISPROOF_KUMMER`; Opus replayed the new `R17_F3` tables across all 15,202 primes, not inherited SE/ZL high rows); export cross-reviewed by Astra (`deep`).

### z76 (2026-11-20): GPT-6.2 Astra 6-lane burst — QR+TS PID, BCM+Lag+QR, IE₁/PID barrier, R(n) ≪ n^{7955/24966+ε}, sterile r ≥ 177,505, R₈ 1.59T, GRH M_gen ∼ M₀
`+` PROVED (logic): one external IOpen PID with `internal Dirichlet + Lagrange + full internal prime QR (both supplements) + universal TS + L(D) + ¬ES(P)`; separately, one Bézout model with `IOpen + BCM + Lagrange + full internal prime QR + ¬ES(P)` (`notes/z76/QR_TS_BCM.md`). Separately: full-QR + Dirichlet + Lag + L(D) PID where `P` alone lacks a least QNR; rank-one Pell model upgraded with arbitrary fixed-modulus polynomial congruence filters; geometric twisted-root Pell PID (`notes/z76/IE1_BREAK.md`).
`+` PROVED (analytic & covering records): pointwise `R(n) ≪_ε n^{8/25+ε}` (classical tests + Weil) and `n^{7955/24966+ε}` (rel. Trudgian–Yang) via conductor shifts (`ANALYTIC_34.md`); sterile Mordell threshold slashed 16× to **r ≥ 177,505** + dense `x²+Dy²` prime cores hit `(S)` at density 1 of primes in any reduced progression inside `1 mod 4` (`PROOF_LIFT.md`); CONDITIONAL on Dirichlet GRH: `M_gen(p) ∼ M₀(p)` at primes `p ≡ 1 (4)`, and under quadratic GRH + unproved `PC(F,η)`: `log F(y) ≤ c_η√y ⇒` eventual ES (`ALPO_TRANSFER.md`).
`+` PROVED / CERTIFIED / EVIDENCE (fibres & records): Vieta parameter descent gives non-BM sterile Type II fibres `Y_{n,c}` at every even `c ≥ 2` with `n = c² + 1`, plus some `c ≍ n^{1/3+ε}` for every large odd nonsquare and prescribed `c(n) = ⌊(log n)^A⌋` (`A > 3`) for density-1 primes (`DISPROOF_DEEP.md`); CERTIFIED new in-𝔐 R₈ prime floor **1,590,284,203,561** (`R = 52`, 4 checkers) + EVIDENCE from `p mod 1,058,400` controls showing a cheap-witness square-shift deficit (`DISPROOF_COMP.md`).
`−` Barriers: **BARRIER-BROAD** — no nonstandard external IOpen PID satisfies `IE₁`, and any nonstandard external PID with `IE₁⁻ + ¬ES(P)` implies ES false in ℕ (`IE1_BREAK.md` §4); `alpo.ge/remark.pdf` transfer barriers (sharp path-quadric norm, `tr(A^{2j}) = 2N₂`, missing-frequency Gram lemma, higher-rank stable-range common-square transport, `ALPO_TRANSFER.md`); square-Kummer unrestricted BM inherits downstairs reconstruction (`DISPROOF_DEEP.md` §3).
`→` Closed: simultaneous QR+TS PID, BCM+Lag+QR model. Open: ES, `IE₁`/`IE₁⁻`/`IΔ₀`, `r = 17`, `𝔽₃[T]` Conj. 0.2, `θ > 3/4` on `E(N)`.
`R` All 6 lanes authored by GPT-6.2 Astra (`deep`), orchestrated by Fable (`best`), and independently cross-reviewed by Claude Opus (ACCEPT or ACCEPT-WITH-FIXES, fixes applied; two passes on `IE1_BREAK` and `DISPROOF_*`); master-file export cross-reviewed by Astra (`deep`).

### z75 (2026-11-20): GPT-6.2 Astra 6-lane burst — BCM+4-squares, full prime QR, Lean 15·2^s+1 & 4^s+{33,273,297}, subexp e*(n), 2/3 (★)/U₇, trillion-scale R₈
`+` PROVED (logic): `IOpen + Bézout + BCM + Lagrange (4 squares) ⊬ ES` via twisted dyadic-axis end extensions (`notes/z75/BCM4_PUSH2.md`); separate external IOpen PID with `internal Dirichlet + Lagrange + full internal prime QR + L(D) ⊬ ES` (`BCM4_QR.md`, `BCM4_PUSH2.md`); unary `L(D)` holds in every external IOpen PID (`IE1_ES.md`); separate rank-one normal `IOpen + Lag` model repairs variable-radicand supplied-unit Pell windows with negative Pell and ¬ES(P) (`IE1_PUSH2.md`).
`+` PROVED (thin families & (S)): **Lean 4** full `ES(15·2^s + 1)` (`lean/ES/ES/Proth15.lean`, moving cyclotomic divisor) + corollary `15·b^s+1` (`b ≡ 2 mod L`); **finite certificates** (not Lean) for full `ES(4^s + k)`, `k ∈ {33, 273, 297}`; **(S)** tightened from 28 to the exact 24 odd-square classes mod 840 (`notes/z75/CONJS_GEN.md`, `THIN_CYCLO.md`).
`+` PROVED (analytic records): unconditional effective `e*(n) ≤ exp(C√(log R · log log(3R)))` (`R = rad(n)`), explicit `4e*(p)+3 ≤ √(4p/3)` at `p ≡ 1 (8)`, **CONDITIONAL** on Dirichlet GRH alone `exp(O(√(log₂R · log₃R)))` (`ANALYTIC_BREAK.md`); shift-uniform `O(H exp(−c(log H)^{2/3}))` prime lower tail on both C-parities of (★) separately and on U₇ (all-integer form loses a `(log log H)^{1/3}` factor; `ANALYTIC_PUSH2.md`).
`+` PROVED / CERTIFIED (obstructions & censuses): open-surface `Br(V)[m]` (kernel `s ≠ 1` / `s ∉ {1,2}`) vs unbounded 2-power-conductor existence dichotomy on `S°, X°, U°` (`DISPROOF_OBSTRUCT.md`); sharp cubic cutoff giving infinitely many non-BM sterile Type II fibres `Y_{p,c}` (`DISPROOF_PUSH2.md`); 10 new R₈ prime zeros raising in-𝔐 floor to **1,511,088,831,001**; `(MS⁺₁₀₅)` to 10¹¹, Type A to 2·10¹¹, `U₇/U_II/N_II` to 2·10¹⁰.
`−` Barriers: 3 frozen `REVIEW_GEN` maps non-universal (`CONJS_GEN.md`); single-pivot fold matching, thin-core `a^m±b^m` (`m ≥ 3`) density-0 barrier, Stepanov flat-mask degree (`1 ≤ m < p`), signed two-endpoint miss at 1,269,241 (`PROOF_WILD*.md`); dyadic idempotence `J² = J` (`BCM4_QR.md`), circle class `(s,x)` (`BCM4_PUSH2.md`), linear root search miss in modified QR PID (`IE1_PUSH2.md`).
`→` Closed: BCM+4-squares, Lagrange iteration, `15·2^s+1`, `4^s+{33,273,297}`, 3 frozen class-map tests, 4 non-square (S) classes. Open: ES, IE₁/IΔ₀, QR+TS, θ > 3/4 on E(N).
`R` Authored by GPT-6.2 Astra (`deep`), orchestrated by Fable (`best`). Independent Claude Opus cross-reviews ACCEPT or ACCEPT-WITH-FIXES (fixes applied, Lean compiled) for Lanes 1, 2, 4 (excl. §6 full ES counts), 5, 6; Lane 3 (`PROOF_WILD*`, barriers only) self-checked; master-file export cross-reviewed by Astra (`deep`).

### z74 (2026-11-19): ordinary-prime transfers, formula menus, weak-arithmetic models
`+` PROVED: one external IOpen PID with internal Dirichlet, universal prime two-squares, universal NR and Lagrange, in
    which a nonstandard P ≡ 1 (840) fails ES. It uses positive reciprocal descent, which bypasses the z66 arc obstruction
    (`LOGIC_JOINT_NR_TS.md`). Built on it: IOpen + Bézout + BCM + five squares ⊬ ES (`LOGIC_FIVE_SQUARE_BCM.md`).
`+` PROVED, in separate non-Bézout models: IOpen + Lag + Pell⁺ ⊬ ES, still with Pell⁻ and TS at irreducibles ≡ 1 (4) added
    (`LOGIC_POSITIVE_PELL_AUDIT.md`, `LOGIC_NEGATIVE_PELL_TS_TEST.md`). One Lagrange end extension: BCM at every old cutoff.
`+` PROVED, unconditional: fixed polynomial whole-triple menus in Gaussian + *integral* Pell data miss density one of the
    primes on a progression (`GAUSSIAN_PELL_MENU.md`); with Pell data alone, every prime of a class (`PELL_ES_MENU_NOGO.md`).
`−` Method counterexamples (`Z74_CHECKPOINT.md`): one-slot repair; 214729 misses both slots at all 16 divisor shifts
    (infinitely many under Dickson); 193 fails both windows at every root-eligible shift; hull BCM; Pell remainders escape.
`→` Open: BCM + four squares, iterating the Lagrange extension, the joint non-PID NR Variant (conditional, assembly owed).
`R` Authored by Astra. Assigned Opus cross-reviews all done: ACCEPT or ACCEPT-WITH-FIXES, fixes applied, no WRONG claim
    (`data/z74/xreview/REVIEW_*_OPUS.md`). Astra's own side audits served as review inputs, not as reviewed results.

### z73 (2026-11-19): weak theories with Bézout and PIDs
`+` PROVED countermodels:
    * IOpen + Bézout ⊬ ES (`Z73_OPEN_BEZOUT.md`, `LOGIC_BEZOUT.md`).
    * Per unit-square class, an external IOpen PID with a failing prime (`Z73_PID_SQUARE.md`).
    * One PID failing, for each standard unit-square class, in every interval (a, a+b), a ≥ 1, b infinite, with Bertrand
      and internal Dirichlet (`LOGIC_PID_INTERVAL_AUDIT.md`, `LOGIC_PID_DIRICHLET_AUDIT.md`).
    * In landing (non-PID) Bézout models: collection with PD and TS (`LOGIC_BEZOUT_NORM_COLLECTION.md`), short intervals
      and greatest prime divisors (`Z73_SHORT_INTERVAL.md`, `LOGIC_GREATEST_PRIME.md`).
`+` Row descent: IOpen + Bézout + Dirichlet has the same prime-tail dichotomy as IOpen (`Z73_ES_ROW_DESCENT.md`). Also the
    marked-section characterisation and composite-shift forcing criteria.
`−` Smith's PID alone does not give ES failure. Two four-term starts get trapped at 101641; a third reaches a solution (`data/z72/counter_tail/ROUND3.md`).
`R` Authored by Astra. Opus cross-reviews ACCEPT or ACCEPT-WITH-FIXES, fixes applied (`data/z74/xreview/`: Z73BASE,
    PIDEXT, COLLECT, NRMODELS, Z72PHASE).

### z72 (2026-11-19): phase criteria at prime shifts
`+` PROVED: a sharp two-factor criterion at a prime shift (`Z72_PAIR_PHASE.md`). With shifts not restricted to primes,
    support ≤ 2 Type II holds on a relative-density-one set of primes p ≡ 1 (4) (elementary). An exact sieve to 5·10⁸
    finds no failure (two independent engines). There is no all-prime implication.
`+` The closest nonexact triple for p ≡ 1 (24) (`EXTREMAL_ES.md`).
`−` At 1201 no prime shift has support ≤ 2. Monotone repair fails at 73. Frozen class-group menus miss a d = 2 fibre
    (`data/z72/mixproof.md`). Equal phase costs give opposite fixed-x outcomes at c = 43 (`PHASE43_DENOMINATORS.md`).
`R` Authored by Astra. Opus cross-review: ACCEPT-WITH-FIXES, fixes applied (`data/z74/xreview/REVIEW_Z72PHASE_OPUS.md`).

### z71 (2026-11-10): literature refresh
`−` No new mechanism. Dahan arXiv:2611.08717 gets 5/7 by the 3/4-note architecture, and its pointwise part is B2 with a
    cap (`Z71_LIT.md`).
`R` Orchestrator-reviewed only.

### z70 (2026-11-10): z69 leftovers. Campaign PAUSED afterwards.
`+` The e-ideal dictionary in the prime case (`Z70_CLASS.md`). Thm LS: the level sum is not modular (`Z70_LOOSE.md`).
`−` Scoped exclusions GW, AMB and REP (`Z70_LOOSE.md`, `Z70_GEN.md`).
`→` Three frozen generative class-map tests (`data/z70/xreview/REVIEW_GEN.md`).
`R` Astra: ACCEPT-WITH-FIXES.

### z69 (2026-11-10): hard-prime mining, nonlinear U₇ rules, Fable 5.2 ideation
`−` Finite polynomial divisor rules on the specified curves fail infinitely often (CONDITIONAL on Schinzel H;
    `Z69_NL7.md`). Mining and ideation gave nulls; only minor lemmas.
    Files: `Z69_*.md`.
`R` Astra.

### z68 (2026-11-09): (S) via p-adaptive words, U₇ tryhard
`+` PROVED: the cut identity and a partial contraction on refinements of length-three words (`Z68_SIGN.md`; it need not
    preserve goodness). Primes failing U₇ are ≪_A N/(log N)^A (`Z68_U7O.md`). GRH bridge: under GRH, (PC) with
    log F(y) ≤ y^{1/2−ε} gives eventual ES (`Z68_PC2.md`). CONJECTURES B and C are in `Z68_U7F.md`.
`−` Bounded-letter cascades fail (CONDITIONAL on Dickson). Two-prime covering gives no fixed-factor gain.
`R` Astra.

### z67 (2026-11-09): making the uncovered set explicit
`+` PROVED (computer-assisted): (S) leaves U_S nonempty for every ℓ ≥ 11. U is Haar-null (`Z67_ELL0.md`, `Z67_K11.md`).
`−` Candidate π° killed in cross-review.
`R` Astra.

### z66 (2026-11-08): the uncovered set U, the next logical rung
`+` PROVED: U ⊋ squares, and as ℓ grows almost all non-square one-prime slices lie in U (`Z66_UCOVER.md`). U is Haar-null
    in the profinite unit group (z67). IOpenLin + Bézout ⊬ (MS)
    (`Z66_IE1.md`).
`−` The arc method (odd-square landing) is dead from IOpen + Lagrange upward (bypassed in z74 by descent). No H★ engine.
`R` Astra.

### z65 (2026-11-08): logical strength, char-p lifting
`+` PROVED: T1 + two squares still ⊬ ES (`Z65_LOGIC2.md`). Dichotomy: NOI proves a class tail ⟺ IOpen does ⟺ finite
    ET coverage ⟺ the class misses U.
`−` Good-reduction lifting is dead at p ≡ 1 (12) (`Z65_LIFT.md`).
`R` Astra.

### z64 (2026-11-08): unprovability, conjecture (S), cross-field equivalents
`+` PROVED: normal open induction does not prove ES on any class of 𝔐, while IOpen proves every other class mod 840
    (`Z64_UNPROV.md`). (S) is proved for non-square n ≡ 1 (4) outside 28 of the 210 classes (`Z64_SDEEPF.md`).
`−` Ten cross-field equivalences, none of whose tools works at a single prime (`Z64_EQUIV.md`). PA/ZFC independence is
    judged unrealistic.
`R` Astra.

### z63 (2026-11-07): precedent hunt
`+` Euclidean paths are loops in Γ₀(n). Conjecture (S) stated, with (S)(p) ⟹ ES(p) (`Z63_EUCLID.md`).
`−` No precedent known for a pointwise hit of this kind (`Z63_PRECEDENT.md`).
`R` Astra.

### z62 (2026-11-07): new proof paradigms at one prime
`+` The exact arrangement form of R(p) = 0. Lemma P0: parity and index arguments are equivalent to certificate weights.
`−` No inverse theorem; uniform parity non-vanishing is refuted (`Z62_*.md`).
`R` Astra.

### z61 (2026-11-07): board on new mechanisms
`+` A divisor-residue pigeonhole criterion, which repackages the ρ-ratio criterion (`Z61_PIGEON.md`).
`−` The board found no new mechanism; the valuation-transport rules are dead (`Z61_TRANSPORT*.md`). Board memo:
    `~/.pi/boards/20261107-es-newmech/memo.md`.

### z60 (2026-11-06): clean-statement attack, three generators
`+` U₇ census, CERTIFIED: the odd non-square zeros up to 10¹⁰ are exactly Z₇ (`Z60_LOPEZ.md`).
`+` R-zeros along non-square polynomials have density 0 (`Z60_MS105.md` Thm 3).
`+` Signed T1 (`Z60_SIGNED.md`).
`−` RAYCLASS, DYNAMICS and TRACE are exact encodings that end at B2. **Spending rule adopted:** no more re-encoding waves
    (`OPERATIONS.md`).
`→` Targets (MS-U₇) and (MS⁺₁₀₅). Full summary: `Z60_SUMMARY.md`.
`R` Astra per lane; FRONTIER consistency review `data/z60/xreview/REVIEW_FRONTIER_Z60.md` (likewise for z53–z59).

### z59 (2026-11-05): survivors of z58
`+` CERTIFIED: the (MS⁺) census to 10¹² (9 primes and 18 composites, the largest 17,401,609), and the odd non-square U_II zeros up to 10¹⁰
    are {105, 4545}.
`+` 13 explicit Waldspurger zeros (`Z59_WALDS.md`).
`−` Cusp/Waldspurger no-go. `Z59_MSPLUS.md` Prop 2.2 withdrawn. Full summary: `Z59_SUMMARY.md`.

### z58 (2026-11-05): sixteen lanes on (MS)
`+` PROVED: the positive-integral BM set is empty iff n is a square, and 4545 is a non-BM Hasse failure (`Z58_STRUCT*.md`).
`+` CERTIFIED: (★) at all primes in 𝔐 ∩ (10¹⁰, 3·10¹¹].
`+` Kandukoori–Ramesh–Kumar have a 3/4 claim in a commit dated 2026-07-30, Lean-conditional on nine analytic axioms at
    the time. Commit-date ordering only, not verified public priority; it must be cited (`Z58_LIT.md`).
`−` Scoped no-gos for Hecke and ternary-theta proxies, Mordell menus, function-field analogues and weak arithmetic. Full
    summary: `Z58_SUMMARY.md`.

### z57 (2026-11-05): synthesis
`+` CONJECTURE (MS): R(p) ≥ 1 for every prime p > 10¹⁷ in 𝔐. PROVED: (MS) ⟹ ES, via Mordell and Salez (`Z57_SYNTH.md`).
`+` Type II genus main term ≥ 10⁻¹⁰·log³p at large p ≡ 1 (4) (`Z57_BFII.md` Thm G). 𝔊*-zeros are ≪ x/(log x)^A (`Z57_BFO.md`).
`−` No complementarity: four implications refuted (`Z57_COMPLEMENT.md`). Full summary: `Z57_SUMMARY.md`.

### z56 (2026-11-04)
`+` M_gen(p) ≥ (5/6 − o(1))·M₀ at large p ≡ 1 (4) (`Z56_FAMDESIGN.md` Thm V).
`+` #{p ≤ X : R(p) = 0} ≤ X·exp(−0.08√log X) for X ≥ X₀ (`Z56_FAMTRY.md`).
`+` Lean HC infrastructure. Drafts `paper/es-count-note` and `paper/es-hc-note`.
`−` K(4) open. Full summary: `Z56_SUMMARY.md`.

### z55 (2026-11-04)
`+` The (H⁻_𝔉) inequality fails at the checked zero primes (CERTIFIED); the eventual statement is open (`Z55_CROSSF.md` §4). A positive proportion of primes have R_𝔉 ≥ 2 (`Z55_CROSSO.md`).
    HC ≤ 64 below 10¹².
`−` TD is not proved for any η > 0. Full summary: `Z55_SUMMARY.md`.

### z54 (2026-11-03)
`+` K(4) ⟺ P(4,15). Theorem Q: HC ≥ 7 at primes p = 5m² + 1 with 4 | m. HC ≤ 8 for primes p ≡ 1 (4) outside 𝔐.
`−` Triangle-inequality and character-side square-sieve routes give nothing. Full summary: `Z54_SUMMARY.md`.

### z53 (2026-11-01)
`+` M_gen(p) ≫ log²p unconditionally at large p ≡ 1 (4) (`Z53_GENUSLVAL.md`). R(n) ≪ n^{12/37+ε} (`Z53_SQSIEVE.md`).
`+` Almost-all R(p) ≥ (1/64 − ε)log²p (`Z53_PZ.md`). ES(15·2^s + 1) CERTIFIED for s ≤ 3·10⁶.
`−` The oracle no-go (`Z53_NONCRTLOGIC.md`) and the lattice no-go (`Z53_LATTICE.md`). Full summary: `Z53_SUMMARY.md`.

### z52–z52d (2026-10-30 … 11-01): breadth-first connection generation, triage, depth lanes
`+` `BM_LVALUE.md` Thm A (exact L-value formula) and Cor 3.1 (M_BM ≥ 0.1402·log²p at large p ≡ 1 (8)).
`+` Lean: ES(3·2^s + 1); 15·2^s + 1 off s ≡ 0, 240 (360).
`+` The I3_𝒞 zeros among primes p ≡ 1 (4) up to 10⁹ are {5, 13, 17, 2521} (`Z52_BANKED.md`).
`−` Pass 1 over 2284 items found 0 new-structural (`ES_CONNECTIONS_TODO.md`). Depth lanes narrowed (`Z52D_*.md`). The
    coprime SQ statement in FRONTIER §5.5 was wrong.

### z50–z51 (2026-10-29/30): exceptional-set offensive
`+` E_U(N) ≪ N·exp(−c(log N)^{2/3}…). The supply-law caps 3/4 (ES) and 2/3 (U/ES₅) are attained (`EXSET_*.md`,
    `BREADTH_Z45.md` §15–16).
`+` Cap relaxation at (log log X)^{1+ε} with a power-saving exceptional set (`EXSET_LINNIK_CAPS.md`).
`−` Nothing beyond 3/4 for ES or 2/3 for U, even conditionally on a standard hypothesis.

### z44–z49 (2026-10-19 … 10-29): boards #3/#4, breadth, forests
`+` No étale-Brauer descent obstruction for any n ≥ 2 (`BRAUER_TWISTS.md`). Q3 refuted (`Q3_PIVOT.md`).
`+` Forest witnesses are not polylog; H₂ refuted (`H4_NOT_POLYLOG.md`). I3 counts (`I3_DEEP_*.md`).
`−` Nine new fields and two boards all end at B2 (`BREADTH_Z45.md` §1–14).
