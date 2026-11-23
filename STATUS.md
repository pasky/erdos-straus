# STATUS — the master summary of current results

*Last wave included: **z83** (2026-11-23). This file is curated, not a log, and is capped at about 250 lines. Rules for
changing it are in `AGENTS.md` §3. When this page and a source note disagree, the source wins; fix this page.
The wave-by-wave history is in `WAVES.md` (z44 onwards) and in `STATUS_HISTORY.md` (through 2026-10-19). The
expert-level deep reference is `FRONTIER.md`. Citations of "STATUS.md §…" written before 2026-11-19 refer to
`STATUS_HISTORY.md`.*

## 0. Bottom line

* **The Erdős–Straus conjecture (ES) is open.** Nothing here proves it, conditionally on any standard conjecture or
  otherwise. Nothing here disproves it either.
* All proofs are reviewed internally only: hostile reviews by other model instances, usually including one cross-lab
  review (GPT "Astra" for Claude work, and Claude Opus for Astra work). **Nothing is externally refereed.** No campaign theorem has been posted or submitted. The only
  external contribution is an audit of other people's claimed proofs, plasma-ai/erdos#65, merged 2026-11-10.
* **Where everything ends (Assessment; FRONTIER one-paragraph summary, §2–3).** About 280 tasks up to 2026-10-19 and about
  30 waves since, across every phase, several advisory boards and three labs' models, all reduce to one statement, called
  **B2**. A single integer, determined by p and the slice parameters, must have a divisor in a residue class whose
  modulus is itself part of the solution. Only polylog(p) winners are expected.
  * A single hit R(p) ≥ 1 on the c = 1 line is *sufficient* for ES(p), not necessary.
  * The counting target H⁻_BM, R(p) ≥ ε·M_BM(p), is stronger still. Like every eventual bound, it gives ES only above a
    threshold, plus a finite check below it.
  * The main term M_BM(p) ≍ log²p is an unconditional theorem (§1B).
  * No standard conjecture is known to imply the lower tail.
  * No precedent of this shape is known for any natural problem.
* **Campaign state.** The campaign runs in bursts, one per new frontier model. Between bursts it is idle. Waves **z75–z83**
  (z83: 2026-11-23, 8 GPT-6.2 Astra lanes, 2–3 review rounds each incl. verification; **25** hostile Claude Opus cross-lab review reports incl. two independent second audits of the logic records) pushed four fronts while ES in ℕ remains open; no pointwise mechanism emerged and B2 is unchanged.
  PROVED (rel. inputs in §1B,D–E, §2 item 4): the z82 full-Farey model `T_F` is **not** a model of `IE₁⁻` (it fails a provable digit-lifting sentence); new models `T_Π`/`T_mix` repair that and still have `¬ES(P)`; ES-provability in `IE₁⁻` and in `IE₁` is one question (Kaye's known conservation), about models of an `∀E₁` rule theory `U`. CERTIFIED: the capped relaxation holds with cap 10 for every prime with least quadratic nonresidue `≤379`, hence for all primes `≤10²⁵` (not cap 0 = ES). The gap-tail record gains a log-log factor at intermediate cutoffs (§1D). On `≍X/log²X` primes `1 (840)` window 3 fails with at most four 7-inert factors of `x₇`, all `≥X^{211/3000}`; the corresponding at-most-two population and `g=11` population remain CONDITIONAL (§1D). Single-window asymptotics rely on unrefereed JLL inputs.

Notation: 𝔐 = {1, 121, 169, 289, 361, 529} mod 840 (Mordell's hard classes). R(p) = the (★)/c = 1 Type II count.
M₀(p) ∼ (3/(2π²))log²p is its expected size. It is a finite sum with an O(log p) secondary term; the exact form is in
`BM_LVALUE.md`. Definitions are in FRONTIER §2.

## 1. Headline positive results

Each item carries a label, then a pointer. "PROVED rel. X" means proved relative to the published theorems X.

### A. Exceptional set and almost-all results (averages; they say nothing about a given p)
* **E(N) ≪ N exp(−c(log N)^{3/4})**, improving Vaughan's 2/3. INTERNALLY PROVED; `paper/es-threequarter-note`. External 3/4 claims: Kandukoori–Ramesh–Kumar (m=4 and each fixed m; repo commit dates precede ours, `Z58_LIT.md`); Trybushnyi (`arXiv:2611.14167`; Lean deposit Zenodo 23188522 dated 2026-10-06, before our 2026-10-08 `m^{−1/4}` statement): `E_K(N) ≤ N exp(−c((log N)³/K)^{1/4})` for `h=⌊log₂(N)⌋≥4096` (base 2), `K≥4`, `Kh≥2⁶¹`, `2⁹⁰K≤h³`, explicit c (1.1(b)), as stated; external proofs and Lean not audited (`notes/z81/LIT.md` §0.4). Our short-interval, AP, exceptional-prime-in-short-interval and m/p-transition variants are not in either (`paper/es-mn-short-note`); Dahan claims 5/7 (`Z71_LIT.md`).
  (z80, PROVED rel. Paredes–Sasyk 1.3, TZ 1.4, Stark, Landau–Page and internal z79 TQ/AP2; `notes/z80/BEYOND_34.md` §§1–4,14.) For fixed d≥1, every nonconstant integral F of degree ≤d, ‖F‖∞≤exp(b_d(log H)^{1/4}): ≪_d H exp(−c_d(log H)^{3/4}) arguments per H consecutive integers have F(j)>0 failing ES; same exponent relatively among prime arguments if their population is ≥H/(log H)^C, C>0 fixed (not relative to prime values); genuine word tails off rational scalars times squares; z79 ramified-pencil/primorial scopes retained (`notes/z79/WILD_ES.md` §§5,7).
  No effective pullback onset or priority claim. Audited CRT/product-law sharpness: `paper/sieve-limits-note.tex`, `notes/z79/ANALYTIC_PUSH.md` §1.
* **Σ_{p≤N} f_I(p) ≪ N log²N**, which removes Elsholtz–Tao's log log N. PROVED rel. the trace formulae, Weil, twisted Weil,
  Selberg 3/16 and λ₁(SL₂(ℤ)) > 1/4; it needs expert scrutiny. `paper/es-typei-heegner-note`.
* **U and ES₅ are sufficient restrictions (U ⟹ ES₅ ⟹ ES).** E_U(N) ≪ N·exp(−c(log N)^{2/3}(log log N)^{−1/3}) over
  n ≡ 1 (4). Without the log log, failures are ≪ N·exp(−c(log N)^{2/3}) at primes p ≡ 1 (4) for U, and at all primes for
  ES₅. 2/3 is sharp for the audited CRT architectures. PROVED; `EXSET_BEYOND_CRT.md`, `EXSET_I3.md` §7.3 (z50).
* **Almost-all lower bounds** (PROVED rel. z79 Haar moments, PNT/Mertens, upper sieve, Bettin–Chandee Thm 1, BV/BT; `notes/z80/R_BELOW_619.md` §§4–5.6).
  For fixed ε>0, R(p)≥(C−ε)M₀(p), each d-parity ≥(C/2−ε)M₀(p), C=238447111/317627388, outside O_ε(π(X)/log²X) primes p≤X.
  For fixed even v≥2 the f_I, f_II lower coefficients of log³p are b_v−ε and b_v+1/(14ζ(3)v³)−ε respectively, where b_v=log(3/2)/(3·21³ζ(3)v³), outside O_{v,ε}(π(X)/log^{3v/2}X).
  PROVED rel. Burgess and BM_LVALUE: |M_BM−M₀|≪_A(log log(3p))² outside O_A(π(X)/log^A X); Akaka's earlier rate claim is for strict Type II only.
  Normal order R/M₀→1 in prime probability is CONDITIONAL on Bettin–Chandee–Radziwiłł Conj. 1 (§5.6) or the signed two-cell estimate (H) at individual cutoff 2/3 (§5.1).
  Smaller-coefficient arbitrary-log bounds and smaller-count stretched-exponential tails retain the z79 ranges (power fibres rel. (G) or CONDITIONAL on Dirichlet GRH; `notes/z79/LOWER_TAIL.md`).
* **Shift-uniform 2/3 lower tail on both C-parities of (★) and U₇:** outside ≪ H·exp(−c(log H)^{2/3}) primes per
  interval (M, M+H], both R_odd and R₈ separately have ≥ δ(log H)^{2/3} ordered witnesses (improving `Z56_FAMTRY`'s 1/2
  exponent for R(p) = 0 and `Z68_U7O`'s N/(log N)^A for U₇; unspecified c, ineffective onset). PROVED rel. BV, BT and
  Mertens; Opus-reviewed; novelty unverified; `notes/z75/ANALYTIC_PUSH2.md`.
* **Density transition for m/p:**
  * It lies at log N ≍ m^{1/3} up to a (log log N)^{1/3} factor. Thm U is PROVED rel. the internal 3/4 theorem, BV and
    Shiu; Thm L′ is PROVED rel. ET, Brun–Titchmarsh, Shiu and Pólya–Vinogradov.
  * The sharp order on both sides is CONDITIONAL on a uniform (SEL_m) (`paper/es-mn-short-note` §8–§9).

### B. Pointwise at every large prime p ≡ 1 (4): main terms and relaxations, not ES
* **Genus main term:** M_gen(p) ≥ (5/6 − o(1))·M₀(p) unconditionally for large p ≡ 1 (4) (PROVED rel. Burgess and
  Heath-Brown's quadratic large sieve; `Z56_FAMDESIGN.md` Thm V). **CONDITIONAL on Dirichlet GRH:** M_gen(p) ∼ M₀(p),
  including the Burgess corner and both edges (no numerical onset; Opus-reviewed, `notes/z76/ALPO_TRANSFER.md` Thm G).
* **Brauer–Manin-corrected main term:**
  * Exact L-value formula T(p) = (σ/4)E(χ_p)L(1,χ_p)² + O(p^{−1/16}log p). PROVED, cross-model reviewed; `BM_LVALUE.md`
    Thm A.
  * Hence M_BM ≥ 0.1402·log²p and M_BM ≥ 0.9225·M₀ at large p ≡ 1 (8) (Cor 3.1).
  * The odd-square obstruction T1 is built in exactly (`BM_CORRECTED_COUNT.md`).
* **Type II genus main term ≥ 10⁻¹⁰·log³p** for large p ≡ 1 (4). PROVED, genus part only; `Z57_BFII.md` Thm G.
* **Upper side:** PROVED unconditionally for every n ≥ 2: **R(n) ≪_ε n^{6801/21497+ε}** (≈ 0.316370, rel. z78 §§7,13,
  Weil, twice-used stationary phase, divisor/2nd-derivative bounds and Trudgian–Yang *Math. Comp.* 2025 Lemma 1.1 +
  B-transform; Bourgain fallback `999/3157`, classical no-exponent-pair fallback **`25/79`**, intermediate `13/41`; two
  independent Opus reviews incl. `REVIEW_ANALYTIC_PUSH_6801_OPUS2.md`, superseding z78 `46/145`). PROVED (`notes/z80/R_BELOW_619.md` §§2–2.1, rel. the z79 bound, divisor bounds, Dirichlet approximation, Erdős–Turán and exponent pairs):
  for integers `M≥1,n≥2`, `D=n/M²`, `θ∈{6801/21497,999/3157,25/79}`, `R_M(n) ≪_ε n^ε[1+min{n^θ M^{1−5θ}, D^{1/3}, n^{1/2}M^{−7/6}, max(D^{55/181},D^{1/2}M^{−1/4})}]`; CONDITIONAL on EPC, `≪_ε n^ε(1+D^{4/13})`.
  Fixed-4 `6801/21497` unchanged; no fourth-root `N₂` saving and no breach of `6/19`. The z79 ES₅ word transfer stands; external priority unverified (`notes/z79/ANALYTIC_PUSH.md` §§5–8).
* **Capped relaxation (pointwise).** 4/n = 1/x + 1/y + 1/z, x, y ∈ ℤ_{>0}, z ∈ ℚ_{>0}, den z = r², r odd, (r, n) = 1, rad r | y, v_ℓ(r) ≤ e. PROVED effective: e*(n) ≤ exp(C√(log R · log₂(3R))), R=rad(n)>1; explicit 4e*(p)+3 ≤ √(4p/3) at primes p≡1 (8) (`notes/z75/ANALYTIC_BREAK.md`). **(z83 RECORD, `notes/z83/CAP_POINTWISE.md` §6, repository comparison only.)** CERTIFIED (two same-lane engines + Opus regeneration and sampled/range-limited Fraction replay; rel. Mordell, the ES check below 2·10⁶ and Sorenson's published `L_{379,2}>10²⁵`): `e*(p) ≤ 10` for every prime with least quadratic nonresidue `n_p ≤ 379` (all six hard classes), in particular for **all primes `p ≤ 10²⁵`**; the atlas gives upper bound 1 at `n_p ∈ {11,13,17,19}`. Not cap 0.
  (z80–z82, `notes/z80/BEYOND_34.md` §§10–12, `notes/z81/CAP_ZERO.md` §1, `notes/z82/CAP_CONST.md` §8; Q twice independently Opus-reviewed.) PROVED, ineffective (rel. Maynard 1.1, large sieve, Linnik, TZ/Stark, Dickman/Mertens/PNT, z75): prime-power root or root 1 with `log(1+e) ≤ exp(o(log U·log₃U/log₂U))`, `U=log R` (CONDITIONAL on Dirichlet GRH same at `U=log₂R`); polylog `log(1+e) ≪_C (log U)^C` (`C>2`) CONDITIONAL on Chowla's least-prime conjecture alone at `U=log R`, and Chowla+GRH at `U=log₂R` (recovering z80 §12's Montgomery rate from weaker hypotheses; the stronger least-prime bound `p(a,q) ≪ q log^J(2q)` gives `O_J((log U log₂U)²)` at the respective scales, still requiring GRH at the smaller scale).
  **Cap-E exceptional sets (z81–z82, `CAP_ZERO` V, `CAP_CONST` H/C/U/UB/UP/J; independent second review of H/U/UB/UP/J; effectivity/priority unverified):** PROVED (rel. BV, BT, Shiu, Gallagher, Vaughan, internal unrefereed TQ/z79 transfer and `CAP_INTERPOLATION` §1): uniformly for integers `1≤E≤λ=log₂N` (`L=log N`), `#{2≤n≤N : e*(n)>E} ≪ N exp(−c L exp(−λ/(E+4))/log(2E+6))` (fixed-`E` saving `(E+3)/(E+4)`, sharp for polynomial-level whole-avoider single-`f` CRT majorants, Thm C; `E=1` recovers z81 `4/5`, root 1 or prime `(3/4,1/4)` in V; J/`CAP_TO_ES` K: in the same CRT method, allowing all denominator exponents ≤ fixed `d₀` instead of even ones gives `(d₀+3)/(d₀+4)`, cubefree `5/6`). At cap `⌈(log₂X)^{1+ε}⌉`, `O_ε(X^{1−c_ε})` exceptions among odd integers (all exceptions `1 (8)`; `EXSET_LINNIK_CAPS.md` Thms 4.2,4.5). ES ⟺ e*=0; fixed-window δ_p=0 cap 0 is B2 (`CAP_DOWN.md`).

### C. ES proved on infinite thin families (computer-assisted and Lean-checked)
* **All `(4^m−1)2^s + 1` (`1 ≤ m ≤ 30`), `7·4^s + 9`, and `4^s + k`** for k ∈ {9, 33, 57, 81, 105, 129, 153, 177, 201, 225,
  249, 273, 297} (all s ≥ 0). PROVED, computer-assisted (`paper/es-exponential-families`; Opus-reviewed `notes/z75/CONJS_GEN.md`,
  `THIN_CYCLO.md`, `notes/z77/PROOF_S_WILD.md`, `notes/z78/PROTH_ALLM.md` §3, `notes/z79/PROTH_ALLM.md` §4, and m = 13–30 in
  `notes/z80/PROTH_CORE.md` §§2, 9; no primality assumption). **Lean 4** (zero `sorry`/`native_decide`): `3·2^s+1`, `15·2^s+1`,
  `63·2^s+1` for every s (`Proth3`, `Proth15`, `ProthCore.proth63`); `k(z²−1)+1` transfer for positive `k≡15 (16), t≡7 (8)`, `z=t(k−1)−1` (`ProthQuadratic`, z80 §3). Infinitely many non-ET-coverable families: `15·b^s+1` (`b ≡ 2 mod L`), `c_J·2^s+d_J` (`PROOF_S_WILD.md` §3).
* **Good-word cores, not all exponents** (PROVED; `notes/z78/PROTH_ALLM.md`, `notes/z79/PROTH_ALLM.md`, `notes/z80/PROTH_CORE.md` §§1,6,8). For h=2m−1, square-unit core and relative density one in every fixed exponent progression for 2≤m≤200 and m=365,1094;
  also odd h≥5 with 3∤h and equal nonzero v₂(ord_p 2) for p|h. Retain h=4^i+1, 5^j (Lean core only), 2^{12t+6}+13 and qualifying v₃(h)=j≥1 classes (full for qualifying 3∥h; restricted to 3^j|s or 3∤s for j>1).
  Earlier odd-order h=7^{4t+2} and 8-prime products (h≡−1 mod 5); separately ky³+1 on a progression (h=7^i, z78).
  For m≥11, m≡11 mod τ of z80 §6, ES holds off P₉|s, P₉=497,943,285,840; on a selected infinite subset possible exceptions have relative density zero even within that class.
  Open: core for all h; all s for infinitely many m, or for every m>30.

### D. Structure and obstruction theorems (what a proof has to beat)
* **Brauer–Manin and open-surface exponent dichotomy.** On (★) and Type II models, positive-integral BM is empty iff n is
  a square (`Z58_STRUCT*.md`, 4545 non-BM; sterile fibres Y_{p,c} down to `c = ⌊√n⌋`, `DISPROOF_DEEP.md`). On coordinate
  opens S_n°, X_n°, U_n° (kernel s ≠ 1 for k = 4, s ∉ {1, 2} for k = 8), fixed-exponent Brauer and étale-Brauer tests on
  outer-integral positive adeles fail to obstruct (`DISPROOF_OBSTRUCT.md`, `DISPROOF_KUMMER.md`, FRONTIER §3), whereas
  unbounded 2-power-conductor characters at one prime detect existence (`DISPROOF_OBSTRUCT.md`, `DISPROOF_DEEP.md` §3).
* **Finite procedures fail at trap points** (method barrier). Covers, polynomial menus, and finite oracle programs with a
  finite formal tree at the trap fail: PROVED (`Z53_NONCRTLOGIC.md`; prime failures CONDITIONAL on H); unconditional for
  Gaussian + integral negative-Pell menus (`GAUSSIAN_PELL_MENU.md`; see FRONTIER §6 for the z83 rational-gate extension). The sterile subset of the r-generic line has **positive measure** for
  every prime **r ≥ 83 and r = 73** (PROVED, computer-assisted rel. SE, BBR 2012 Thm 1.2, z76–z79 inputs; exact integer/
  rational ledger on `[83, 283] ∪ {73}`, no libm; inherited z78 libm dependencies only for `r ≥ 919`; `notes/z79/R17_ALLDEPTH.md`,
  `notes/z80/R17_CRUSH.md`, `R17_WALK.md`, full Opus replays each round; 15 primes `17 ≤ r ≤ 79`, `r ≠ 73`, uncrossed).
* **Witness sizes are not polylog.** For fixed κ < 1/12, or κ < 1/6 with Gallagher or GRH, infinitely many p have no
  forest edge with larger endpoint in [4, exp((log p)^κ)]. Only {1,2} and {2,3} remain. This refutes Conjecture H₂.
  PROVED rel. the internal energy lemma; `H4_NOT_POLYLOG.md`. Both Type II witness moduli are ≥ the least quadratic
  non-residue at p ≡ 1 (4) (`Z57_BFII.md`).
* **Actual additive windows** (z80 `EXTREME.md` §§6–7,10; z81 `GAP_ES.md` §10; z82 `GAP11_JLL.md` §§1–8 & `BEYOND_34.md` §§2,6–8, independent second review of G/G′ and `GAP11_JLL` Thms 5–6; z83 `notes/z83/G11_OMEGA2.md`, `THIN_DISP.md`, `BEYOND34_MOMENTS.md`): PROVED: distinct fixed positive `k_j≡3 (4)` fail jointly on `O_K(X/log^{1+J/2}X)` primes `1 (4)` in `(X,2X]`; `g(p)=3` on density 1 in `1 (840)`. For each fixed positive `k≡3 (4)` the failure count on each hard class `r (840)` is `∼c_{k,r}X/log^{3/2}X` (`c_{k,r}>0` explicit, rel. unrefereed JLL v2 §§2–3,5–8 as specified, MV III reciprocal bound and z80 H; for `k=3,7`, `c_{k,r}=A_k/192`, `A₃=2.2132…, A₇=2.2405…`; independently `≍` on 𝔐 rel. FHRSS 1.1(2), `g≥7` i.o.).
  **(z82–z83 RECORDS, PROVED unconditionally, no JLL):** on `≍X/log²X` primes `1 (840)` in `(X,2X]` window `k=3` fails and `x₇` has **at most 4** 7-inert prime factors with multiplicity, all `≥X^{211/3000}` (rel. BV, Pan; z83 `notes/z83/G11_OMEGA2.md` Thm E, superseding z82 `GAP11_JLL` Thm 5's `0.057`; the cap four is unchanged). Gap-tail phase curve (`BEYOND_34` G/G′, rel. BV, BT, Mertens, linear sieve; parallel `GAP11_JLL` §5 precursor): for `L=log X, l=log L`, `#{p≤X : g(p)>K} ≪ X exp(−cW)` with `W=L^{min((2+α)/3,3/4)}` at `K=exp(L^α)` (`0<α<1` fixed; `3/4` at `exp(C L^{1/4})`), at `K=L^β`, `W=L^{1−β/(z log 3)}/l^{1/(2z)}`, `z=3e·3^{−1/β}`, for fixed `log 3/(1+log 3)<β<log 3` (at `β=1`: `L^{1−1/(e log 3)}/l^{1/(2e)}`), and `W=L^{2/3}l^{1/6}`, `L^{2/3}l^{1/3}` for `β=log 3`, `β>log 3` (z82 G/G′ at the endpoints; z83 `notes/z83/BEYOND34_MOMENTS.md` I improves only the intermediate log-log factor, unchanged at `β=1`); no prescribed-p bound. Model comparison: FRONTIER §6, V.
  Pointwise effective breaks (`GAP_ES` §10): `K_gen(p) ≪ p^{0.187}`, `K_sub(p) ≪ p^{0.198}` (CONDITIONAL on Dirichlet GRH: `K_sub ≪ log²p`, `BEYOND_34` §9.4; not a bound on g). CONDITIONAL on ordinary prime level `D(0.9544)` (EH suffices; z83 `G11_OMEGA2` Thm C, no JLL) or thin-sequence `T₃⁻(0.455)` (Thm D, rel. z82 Thm 2 with its unrefereed JLL inputs and z80 G): `≍X/log²X` primes in `(X,2X]`, `p≡1 (840)`, have `g(p)=11`; CONDITIONAL on one signed mixed-root estimate `MR⁻(.578)` (implied by `D(θ)`, `θ>.578`; Thm F) the four-factor cap drops to **two**, all `≥X^{0.09}`, on `≍X/log²X` primes (separately, NZ-B for the original `.579` list). CONDITIONAL on G's signed primitive-weight estimate at `.18`: all `≥X^{.154}`, primitive mass `≫X/log^{3/2}X`, hence `≫X/log³X` distinct primes. Unbounded finite g CONDITIONAL on Dickson. CERTIFIED: max g=127 on 𝔐-primes ≤5·10¹² at 3,153,419,441,929 (first genus break k=27, 4 budget misses).
* **All seven ET period searches and good-word denominators can be superpolylog (z78–z79, Opus-reviewed).** For each large
  prime `f ≡ 3 (4)` some `p > f` has seven-chart ET minimum `H_ES(p) = f`; infinitely often all seven period searches exceed
  `exp((log p)^κ)`, `κ < 1/8` (PNT) or `κ < 1/4` (Gallagher, or GRH; also without `(G)` along a clean-scale subsequence;
  `notes/z78/WILD_ES.md` §6, 192 panel minima CERTIFIED). **(z79, `notes/z79/WILD_ES.md` §9, self-contained energy proof):**
  for each fixed **`κ < 1/3`**, infinitely many `p ≡ 1 (840)` have finite least good HJ denominator `A_min(p) > exp((log p)^κ)`
  (subsequence without `(G)` rel. Montgomery/Landau–Page; every admissible large prime `f` rel. `(G)`). Not all coordinates/grammars.
* **Function fields:** ES_q(T) has no finite linear covering for q = 3^r, r ≥ 2 ((J)51, (J)56, (J)67). **q = 3, A = T²
  (z78):** both designated slice points x*_c are uncovered (former Conjecture 0.2), so no finite linear covering. PROVED rel.
  the tuple/parity and minimum-level reductions and Mason–Stothers (`notes/z78/F3_CONJ.md`; Opus reviewed §§1–5, then §§6–7
  with dependencies; `F3Endpoint.lean` checks only the large-level §6 algebra under its hypotheses). CERTIFIED separately:
  brute force N = 4..15, filtered census to N = 38. Not a result for A = T or integer ES. (z83, PROVED, monic model `FUNCTIONFIELD_ES.md` Def. 1.1; `notes/z83/ES_JUGULAR.md` Thm E:) for monic `A` of degree `k>0`, fixed `n>2k` and large `q` of characteristic ≥5, the only unit classes mod `A` in which **all** degree-`n` primes succeed are `−2` and `−D`, `D` monic dividing `A+1`; every other class has `O_n(q^{n−k−1})` successes (order attained on a family for `n>2(k+1)`).
* **Numerator blindness:** M^□ is a theorem for every M ≡ 0 (4), while 8/n fails at n = 131 and 241 ((J)41, FRONTIER §1).
  A proof needs a 4-specific input.

### E. Logic: weak arithmetic does not prove ES (PROVED, internal; nonstandard countermodels)
In each model a nonstandard prime fails ES. The models are *separate* unless stated, so do not combine their axiom lists.
Every item has had at least one cross-lab review: z64–z65 Claude work by Astra, and z73–z80 Astra work by Opus
(`data/z74/xreview/`, `notes/z75/*REVIEW*`, `data/z75/ie1/`, `data/z76/`, `data/z77/`, `data/z78/xreview/`, `data/z79/xreview/`, `data/z80/xreview/`).
* **Normal open induction** (+ gcd, irreducible divisors, and all true universal ring sentences) does not prove ES on any
  class of 𝔐; IOpen proves it on every other class mod 840 (`Z64_UNPROV.md`; + T1 and two squares: `Z65_LOGIC2.md`).
* **IOpen + Bézout** does not prove ES (`Z73_OPEN_BEZOUT.md`, `LOGIC_BEZOUT.md`); a separate model adds full collection,
  PD and TS (`LOGIC_BEZOUT_NORM_COLLECTION.md`). Prime-tail dichotomy with Dirichlet: `Z73_ES_ROW_DESCENT.md`.
* **External IOpen PIDs (all satisfy unary L(D), `IE1_ES.md`; no nonstandard one satisfies IE₁, `IE1_BREAK.md`):**
  * Interval PIDs: per unit-square class, failing primes in every infinite interval with Bertrand + Dirichlet (`Z73_PID_SQUARE.md`, `LOGIC_PID_{INTERVAL,DIRICHLET}_AUDIT.md`).
  * **Unified QR + TS + Lag + Dirichlet + L(D) PID (z76, Opus-reviewed):** internal Dirichlet, Lagrange, L(D), **full internal prime QR** (both supplements, two squareclasses) and **universal TS** fail ES at P ≡ 1 (840) (`notes/z76/QR_TS_BCM.md`).
  * Separate full-QR + Dirichlet + Lag + L(D) PID where **P alone** fails least-nonresidue search (`notes/z76/IE1_BREAK.md`).
* **IOpen + Bézout + BCM + Lagrange (four squares) + full internal prime QR + universal TS ⊬ ES (z78, Opus-reviewed):**
  one countable model (recursive rotation repair of the z76 twisted dyadic-axis tower; both supplements, exactly two nonzero
  squareclasses modulo each odd prime, two squares at every prime ≡ 1 (4)) with P ≡ 1 (840) failing ES (`notes/z78/IE1_UNITS.md` §§1–3,
  strengthening `notes/z76/QR_TS_BCM.md`; not an external PID; fails even plain least divisor above a threshold below every BCM bound at P, also in pointed elementary copies and their convex subrings containing P, `notes/z82/BCM_LDIV.md` §2).
* **Variable-radicand Pell-window & power-cut models (z75–z83, Opus-reviewed; `IE1_ES.md`, `IE1_PUSH2.md`, `FAREY_PROOF.md`, `notes/z82/FAREY_IE1.md`, `BCM_LDIV.md`, `notes/z83/IE1_DECIDER.md`, `notes/z83/BCM_TS_LDIV.md`):** **z82 LANDMARK RECORD (`T_F`, `FAREY_IE1` §§7–12, rel. its §0 inputs; twice independently Opus-reviewed incl. `REVIEW_FAREY_IE1_TF_OPUS2.md`):** PROVED: a countable power cut **`T_F`** combines `IOpen+Bézout+global (Sep)+Lag+internal Dirichlet+full supplied-unit PW+z80 factorial strings over every non-initial PA subring` with full Farey, `Th(n)` at every modulus, and proper Gauss reduction of every positive definite integral binary form, still with `¬ES(P)` (nonstandard prime `P≡1 (840)` with the PA flag; fails BCM by z81 §15). **z83 (PROVED, `IE1_DECIDER` §§1–3; twice independently Opus-audited): `T_F` is not a model of `IE₁⁻`** — `IE₁⁻` proves the digit-lifting sentence Π (`X+2X²` is onto modulo every `h` without odd divisor `>1`), but in `T_F` it misses `P` modulo `H=2^L`; `C` is the largest convex Π-subring. Distinct earlier **`T*`** (`FAREY_PROOF` §§2–12; z82 `FAREY_IE1` §§3–4): reduces all forms of discriminant `−4D` at positive cut scalar `D=ds²` (`d` squarefree) iff `s∈C`, and at `D=kP` for positive cut scalar `k≤cP` for some `c∈C⁺` or square-part root `s_k∈C`, retains disc −4, root-conditional two squares and z79 §3 norm/elliptic windows, fails `Th(P)`, TS, BCM, `L(Div)`. Separate **`T_g`** (`FAREY_PROOF` §13, `BCM_LDIV` §§1,6–7): unary Boolean affine-divisibility minimization incl. fixed-level (★); the §1 schedule fails least search for `(A²+u)²|h+(A²+u)Y`; another (§§6–7) codes squarefree scalar residues and minimizes `t²|h+tY` for positive squarefree scalar `h`, but can fail at `(A⁴+u)²|h²+(A⁴+u)Y`.
  **z83 RECORDS (PROVED rel. `IE1_DECIDER` §§6–9 and `BCM_TS_LDIV` §§3,6–11; `T_Π` twice independently Opus-audited, its z82-queue preservation is an interface audit, not a replay):** new full-Farey power cuts keeping the whole `T_F` package and `¬ES(P)`: **`T_Π`** satisfies every digit lift `DL` (for `h>0` and each fixed degree, `X+bG(X)≡a (mod h)` is solvable unless `h` has a divisor `>1` coprime to `b`; scalar and nonscalar `h`); the interleaved **`T_mix`** also has `B/qB ≺ T_mix/qT_mix` properly at every cut scalar prime `q>C` and Boolean affine least search. Both fail TS at `P` (none of `−1, 2, 3, 6` is a square mod `P`), BCM, and full unary `L(Div)` (a quintic at the square of a smooth squarefree scalar has hits but no least hit, despite square roots of `P` at every prime component). Whether `T_Π`/`T_mix` satisfy `IE₁⁻`, or the rule theory `U` of §2 item 4, is unknown.
* **Window models (PROVED, separate; `notes/z78/IE1_UNITS.md` §§4–9, `notes/z79/IE1_BASE.md` §§3,11, `notes/z80/IE1_SPLIT.md` §§6,9–10,12–19).** z78 separates successive norm/elliptic windows; z79 realizes cofinal-PA Pell, standard balanced norm, positive-rank elliptic and z78 pointed-height windows in normal IOpen+Lag over any countable PA base. (z80) `IE₁⁻ ⊢ T=IOpen+Bézout+global (Sep)+IW₂`, yet `T ⊬ ES`: Model 2 (with Lag, Dirichlet, primary isolation, true-arithmetic cofinal PA ring) has ¬ES(P), `P≡1 (d)` on a nonstandard PA cut, least QNR 2 at P, Pell windows for nonsquares in the cofinal PA ring, standard balanced norm and standard positive-rank elliptic windows, and disc −4 reduction; full Farey, variable reduction, uniform prime short vectors, supplied-unit PW, BCM, `L(Div)` and `IE₁⁻` fail. No separation from `IE₁⁻`.
* **Not claimed:** independence from IE₁, IE₁⁻, IΔ₀, PA or ZFC; a standard counterexample; BCM in a PID (see FRONTIER §3
  for the nonstandard external-PID barrier on IE₁ and IE₁⁻ ES countermodels).

### F. Certified computations (exact, finite; engines and ranges are in the cited files)
* (★) holds at all 355,096,166 primes in 𝔐 ∩ (10¹⁰, 3·10¹¹] (`Z58_SUMMARY.md` §3).
* The non-square zeros of R in 𝔐 up to 10¹² are exactly 9 primes and 18 composites, largest 17,401,609 (one engine;
  `Z59_MSPLUS.md`). **(MS⁺₁₀₅)** (non-square n ≡ 1 (4), gcd(n, 105) = 1, n > 29,210,401) CERTIFIED to **3·10¹¹**: z58 to 10¹⁰, two same-lab engines on (10¹⁰,3·10¹¹],
  cross-lab replay on (10¹¹,2·10¹¹] and separately coded cross-lab verification on (2·10¹¹,3·10¹¹] (`notes/z75/DISPROOF_PUSH2.md`, `notes/z80/EXTREME.md` §§9,13).
* Odd non-square zeros up to **2·10¹⁰** (two engines in (10¹⁰, 2·10¹⁰], `notes/z75/DISPROOF_PUSH2.md`; earlier ≤ 10¹⁰ in
  `Z58_WILDCARD.md`, `Z59_SUMMARY.md`, `Z60_LOPEZ.md`): N_II only 4545; U_II only {105, 4545}; U₇ only the 8 composites of Z₇
  (105-multiples to 5·10¹⁰). On primes `p≡1 (8)`, six-cofactor U₇ Conjecture C (hence B and U₇) is CERTIFIED to **111·10⁹** (z68 to 10⁹; z81 one interval sieve + same-engine Opus replay on `(10⁹,111·10⁹]`, independent enumeration at the two new 3-cofactor exceptions; `notes/z81/S_U7_FORCE.md` §1).
* Among primes p ≡ 1 (4) up to **2·10¹¹**, the b = 1 line (López Type A) fails only at 193, 2521 and 66529 (two engines;
  `B1_LINE.md`, `notes/z75/DISPROOF_PUSH2.md`).
* **R₈ (C-even (★)) threshold floor:** 12 additional certified prime zeros across all classes in z75–z76 and z80 raise the in-𝔐 floor
  to **6,955,940,568,721** (≡ 361 mod 840, R = 42, full 8/p passes; independent exhaustive checks incl. Opus); no later prime zero on
  1 mod 120120 below 10¹⁴ (one AP engine, replayed). Earlier floors 1,590,284,203,561, 1,511,088,831,001, …
  (`notes/z75/DISPROOF_PUSH2.md`, `notes/z76/DISPROOF_COMP.md`, `notes/z80/EXTREME.md`).

## 2. Current open targets (statements whose proof would matter)
Ranked by the campaign (Assessment). Definitions are in the cited files.
1. **(MS-U₇)**: U₇(p) for 𝔐-primes p > 10¹⁷. **(MS⁺₁₀₅)**: R(n) ≥ 1 for non-square n ≡ 1 (4), (n, 105) = 1,
   n > 29,210,401 (CERTIFIED to 3·10¹¹, coverage: §1F). Cleanest sufficient single-sentence targets. (MS) ⟹ (MS-U₇) ⟹ (MS-U) ⟹ (MS-II)
   (`Z57_SYNTH.md`, `Z59_MSPLUS.md`, `Z60_LOPEZ.md` §4.2, `Z60_SUMMARY.md` §5).
2. **H⁻_BM:** R(p) ≥ ε·M_BM(p) for large p (FRONTIER §2.4). Also conjecture **(S)** (`Z63_EUCLID.md`), now PROVED for all
   non-square n ≡ 1 (4) outside the exact **24 odd-square classes mod 840** (`notes/z75/CONJS_GEN.md` Thm 2, Opus-reviewed). For the z83 walk criterion see FRONTIER §6.
3. **Structure / U₇ / class groups:** U₇ Conjecture B and the six-cofactor clause of C remain open; the three-exception clause of C is **false** at `2,238,327,841` and `4,367,159,449` (`notes/z81/S_U7_FORCE.md` §1). `Z70_CLASS.md` open list (Rédei 4-rank, small-split-prime orbits, solution-graph moves); z81 §§4,6 bound abelian exponents of quadratic ring-class menus (dividing `2^r`, sharp via real-only menus; `4` with simultaneous reflection, e.g. common odd ramified `p`; `2` Hilbert-only). Information only, not divisor occurrence.
4. **Logic:** IE₁, IE₁⁻, IΔ₀ and IΔ₀ + exp remain open (no nonstandard external IOpen PID satisfies IE₁; assuming ES in ℕ, any IE₁⁻ ES countermodel is non-PID with nonstandard PA cut and `J ≠ 0`, `IE1_BREAK.md` §4). **One question (z83):** `IE₁⁻ ⊢ ES ⟺ IE₁ ⊢ ES ⟺ U ⊢ ES`, where `U` is the `∀E₁`-axiomatized closure of `IOpen` under bounded-existential induction on theorems (known conservation, credited to Kaye 1990 by Jeřábek 2020 §5; original unseen, exact form proved in `notes/z83/IE1_DECIDER.md` §10). The displayed least-search and numerical leastness schemes are not `∀E₁` tests; that alone does not classify their consequences. Global BCM is dispensable (`notes/z83/BCM_TS_LDIV.md` §10). `IE₁⁻` proves all digit lifts `DL` (`IE1_DECIDER` §§1,6), parameter-free Farey/Bézout, `(Sep)`, proper reduction of positive-definite binary forms, conditional Hurwitz descent, factorial strings over non-initial PA subrings, existence of a divisibility-minimal (prime) failure **if ES fails**, and guarded prime reduction (`IE1_BASE.md`, `IE1_SPLIT.md`, `BCM_LDIV.md` §4), and positive→negative Pell descent at primes `1 mod 4` (`FAREY_PROOF.md` §1). PROVED (`ES_JUGULAR` §6): the fragment of `U` given by `IOpen` + normalized gcd/compatible CRT + rational Farey + proper binary reduction + `DL` does not prove ES (model `T_Π`, §1E). Open: a model of `U` with `¬ES` (or an `IE₁` proof); first concrete test — does `IE₁` prove the true `∀E₁` sentence “every prime has a square root of 2, 3 or 6”, TS, or the QR supplements (all fail at `P` in `T_Π`; Smith 1993 gives one direction of fixed-prime reciprocity, not this disjunction)? Separately open: `L(Div)` in a BCM+TS ES-countermodel (`BCM_LDIV` §§3,8; z83 `BCM_TS_LDIV` §§4,8).
5. **Coverings:** all-depth sterility for the **15 remaining primes** `17 ≤ r ≤ 79`, `r ≠ 73` (each fails the current
   sufficient bound; `r = 13` is fully covered at level 1), above all `r = 17`. CERTIFIED: 5 and its inverse survive all
   seven families through **P depth 16** (4-index search) and **Q odd level 39** (rational walk; independent Opus searches;
   not all-depth: the cylinder `5 mod 17¹⁴` contains P centres at arbitrarily large depth; `notes/z80/R17_WALK.md`). At `r = 17`, `x = 5`, PROVED: `e ≤ 466(rN)^{1/4}` for P (`17^L ≥ 10⁶`), Subspace
   finiteness per square class, **CONDITIONAL on abc** no sufficiently deep P hit with `de ≤ N^θ` (`θ < 1/4`, `R17_ENDPOINT.md`),
   and integral Vieta Q-descent (`pq | V ⇒ dh ≤ (p+q)/2+√(pq)`, excluding Q hits at `5 | 4dcH−6` for `x = 5` and `7 | V` for `x = 7`, `R17_ALLDEPTH.md`). F₃[T] Conj. 0.2 is closed (§1D).
6. **Analytic sub-problems:** FRONTIER §7 (e.g. θ > 3/4 on E(N) — z81 `SPECIFIC_CLASS` gives integer joint miss proportion `(log X)^{-kI_*+o_k(1)}` for fixed `k` distinct `3 mod 4` prime windows in `[log X,2 log X]`, conditional `.751` under (M) or `BEYOND_34` (U)+(P) and `N^{1−δ}` under (DR); no named-conjectural route to `θ>3/4` is known here; chart and comparison limits in FRONTIER §6; bounded cap `e*=O(1)` — uniform `1≤E≤log₂N` saving `L exp(−λ/(E+4))/log(2E+6)`, polylog pointwise log-cap CONDITIONAL on Chowla (`notes/z82/CAP_CONST.md` §§6,8), now `e*(p)≤10` for `n_p≤379` in particular for all primes `p≤10²⁵` (z83, §1B); unconditional `g(p)≥11` i.o. — now `k=3` failure + `Ω_inert(x₇)≤4` all `≥X^{211/3000}` unconditionally, `≤2` CONDITIONAL on `MR⁻(.578)`, `g=11` on `≍X/log²X` primes `1 (840)` CONDITIONAL on `D(0.9544)` or thin `T₃⁻(.455)` with its unrefereed JLL inputs (§1D); `R(n)` past `6/19` toward `3/10`; unconditional normal order `R(p)∼M₀(p)`, `X^{19/12+o(1)}` vs `O(X^{1−δ})`, `R_BELOW_619.md` §5.6).

## 3. Negative results: summarised, not listed
Most of the campaign's output is scoped no-gos, meaning "method class X cannot do it". They are kept out of this page on
purpose.
* **Where they live:** the barrier map as theorems is FRONTIER §3, the proof screening checklist is FRONTIER §4, and the
  dead ends are FRONTIER §6, one line each. Every no-go, scope included, is in its own note and in `WAVES.md`.
* **The pattern:** every analytic, sieve, spectral, automorphic, geometric, algebraic, dynamical, logical and cross-field
  re-encoding tried so far ends at B2, at a non-standard hypothesis, or at evidence. So a new memo that "ends at B2 again"
  is not news.
* **Rule for new work:** before starting, run the FRONTIER §4 checklist. A barrier only changes this page if it rules out
  a *broad* class of proofs that the current text does not already rule out (`AGENTS.md` §3).

## 4. Refuted or corrected claims (do not rely on the old versions)
* **Refuted, or refuted in the checked range:**
  * Conjecture H₂ (polylog forest witnesses): `H4_NOT_POLYLOG.md`.
  * The (H⁻_𝔉) inequality fails at the checked primes with R_𝔉 = 0 < M_𝔉. M_𝔉 > 0 was replayed through the 10¹²-range
    scans, and zeros were found up to 10¹⁵. So any true version needs a large p₀, but the eventual statement is **not**
    disproved (`Z55_CROSSF.md` §4(ii)).
  * **Three-exception clause of z68 U₇ Conjecture C** (`c ∈ {1,3,5}` except `{3361, 21841, 76441}`): **false** at `2,238,327,841` and `4,367,159,449` (CERTIFIED, independent Opus enumeration, `notes/z81/S_U7_FORCE.md` §1; both satisfy B and six-cofactor C).
  * Q3 pivot universality, at p = 7,909,441: `Q3_PIVOT.md`.
  * x* sterile, at r = 13: `es-coverings-note`.
  * Former C_SQ, at 288, 336 and 4545: `espaper` v11.
* **z82 export corrections** (`notes/z82/BCM_LDIV.md` §9; `notes/z82/WALKS_FIBRES.md` §2): the two quadratic least-search failures are in different schedules; 14,476 excludes a small closed miss, not a small successful closure.
* **Corrections:** the coprime form of SQ is false at 105, 345, 561 and 5985 (`Z52_BANKED.md` §1(d)).
  `Z59_MSPLUS.md` Prop 2.2 is withdrawn.
* **Priority:** Do not claim the 3/4 bound, or its initial-segment `m^{−1/4}` form, as first: K-R-K (`m=4`, fixed `m`) and Trybushnyi (`arXiv:2611.14167`; uniform `K`, Zenodo 23188522 dated 2026-10-06 before our 2026-10-08 `m`-uniform commit) are earlier by dated evidence in `notes/z81/LIT.md` §0.4; public-visibility dates unverified. Several "new" items are known (FRONTIER §1, `Z58_LIT.md`).
* **Labels:** `espaper.tex` headlines labelled CLAIMED/PROVISIONAL stay provisional unless restated above.

## 5. Map of master files
| file | role | updated |
|---|---|---|
| `README.md` | orientation for humans | rarely |
| `AGENTS.md` | rules: where results go, anti-deluge policy | when the process changes |
| **`STATUS.md`** | **this page: curated current results** | at wave export if an `AGENTS.md` §3 rule fires; corrections immediately |
| `WAVES.md` | chronological log, at most 12 lines per wave | every wave |
| `FRONTIER.md` | expert reference: reduction, barrier map, checklist, records, dead ends, open problems | at wave export, in place |
| `OPERATIONS.md` | orchestrator directives, models, quota, pause state | when they change |
| `paper/README.md` | status of the write-ups in `paper/` | when a paper changes |
| `DISCOVERIES.md` | ledger (A)–(J)110, frozen 2026-10-19 | frozen |
| `STATUS_HISTORY.md`, `CAMPAIGN_SUMMARY.md`, `Z53_SUMMARY.md`…`Z60_SUMMARY.md` | historical snapshots | frozen |
