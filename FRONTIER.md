# FRONTIER — the Erdős–Straus problem as of 2026-10-19: where to start

*Audience: a strong number theorist (or a fresh AI team) who has never seen this repository and wants to start from the current
frontier instead of rediscovering it. Task O279 (consolidation C3). No new mathematics here: every statement is a summary of a
repository file, with a pointer. When a summary and its source disagree, the source wins.*

> **The Erdős–Straus conjecture (ES) is not solved — not here, not anywhere.** No case of "ES for all large primes" is
> proved here, conditionally on any standard conjecture or otherwise. The literature was checked through 2026-09-28
> (`LITERATURE_2026.md`; the verification record was re-checked on 2026-10-18); every recent claimed proof has an identifiable gap.

**Labels** (as in `DISCOVERIES.md`). PROVED = complete proof in the repo, possibly *relative to* named published theorems;
CONDITIONAL = proved assuming a named hypothesis (GRH, Dickson, Hypothesis H, SEL, …); CERTIFIED = an exact finite computation,
independently reproduced; EVIDENCE = numerics or heuristics only; CONJECTURE = stated, open; Assessment = a judgement or
interpretation, not a theorem. Everything PROVED here is *internally* reviewed (hostile reviews in `reviews/`), and **none of it
is externally refereed.** Pointers like (J)100 are entries in the ledger `DISCOVERIES.md`.

**One-paragraph summary.** After ~280 tasks, a dozen phases and two advisory boards with seats from three labs, every route the
campaign or its sibling (`../erdos-straus-astra`) tried ends (Assessment, R290 repair) at one statement: *a single specific integer, determined by p,
must have a divisor in a residue class whose modulus is itself part of the solution* ("B2", the tied-modulus divisor
event), with only polylog(p) expected winners. In counting form this is a **one-sided lower tail at one integer**,
R(p) ≥ ε·M_BM(p), where the main term M_BM(p) ≫ (log p)² is now an unconditional theorem and the odd-square obstruction
(T1) is built into it exactly. No standard conjecture is known to imply this lower tail, and a literature survey found no
every-n theorem of this shape (polylog main term, no averaging) for any natural problem. §3 maps the barriers as theorems with scopes,
§4 turns them into a five-minute screening checklist, §7 lists well-posed sub-problems.

## 1. The problem and the known landscape

**The problem.** ES: for every integer n ≥ 2, 4/n = 1/x + 1/y + 1/z has a solution in positive integers. A solution for n
gives one for every multiple of n, and the classes n ≡ 0, 2, 3 (mod 4) have identities, so ES reduces to **primes
p ≡ 1 (mod 4)**, in practice p ≡ 1 (mod 24). Mordell's identities reduce further: a counterexample must lie in
n ≡ 1, 121, 169, 289, 361, 529 (mod 840) — the square classes mod 840. These "Mordell-hard" primes are where all difficulty
sits (`AMPLIFY_EXCEPTION.md:7–12`, `LITERATURE_2026.md`).

**Verification.** ES holds for all n ≤ 10¹⁷ (Salez); Mihnea–Dumitru (arXiv:2509.00128, 2025, unrefereed preprint) report
10¹⁸ (`DISPROOF_AVENUES.md:63`). Internally (EVIDENCE): f_I(p) ≥ 1 and f_II(p) ≥ 1 for every prime 5 ≤ p ≤ 10⁸ (Type I and Type
II separately); min f_II/log³p ≈ 0.012 (STATUS, phase (I)). Adversarial searches at 10¹⁸–10²⁵ (BPSW-probable primes) never
approached failure: the hardest relative to controls, p = 2054098191162848070241, still has 870 solutions on its cheapest 1024
e-slices alone (0.26× controls); the smallest absolute count seen was 612 (`DISPROOF_AVENUES.md:246–290`, EVIDENCE).

**Parametrisations (Elsholtz–Tao, ET = J. Aust. Math. Soc. 94 (2013)).** ET call a solution (x, y, z) of 4/n Type I if n | x and n is coprime to y, z, and Type II if
n | y, z and n is coprime to x; for a prime p every solution is Type I (p divides exactly one denominator) or Type II (two).
(R290 repair: for composite n the coprimality matters — 4/9 = 1/3 + 1/18 + 1/18 = 1/4 + 1/6 + 1/36 are neither type, and T1
below is false for the naive "n divides one/two denominators" reading.) In divisor form (`CONDITIONAL_ES.md` §1, PROVED):
* Type I ⟺ f | p² + 4c²d with f ≡ −p (mod 4cd); Type II ⟺ ff′ − 4c²dp = 1 with f ≡ f′ ≡ −1 (mod 4cd).
* e-slice form: ES(p) ⟺ ∃ e ≡ −p (mod 4) with −1 ∈ {ab⁻¹ mod e : ab | N}, N = (p+e)/4 (Type II) or (pe+1)/4 (Type I).
* Counts: Σ_{p≤N} f(p) is ≍ N log²N up to a log log N (ET Thm 1.1); the average of f(n) over all n is ≍ log³n; for almost
  all n, f(n) ≥ (log n)^{log 6 + o(1)} (Elsholtz–Planitzer). Expected solutions per prime are therefore *polylogarithmic*.

**The odd-square obstruction T1** (ET Prop 1.6; Yamamoto 1965; Bright–Loughran Cor 1.3–1.4). For odd m,
f_I(m²) = f_II(m²) = 0: odd squares have no Type I/II solutions, although all local, genus and spinor conditions hold there
(`reviews/redteam-automorphic.md` §4, phase (I) Prop 8.3). (This is no obstruction to ES(m²): any solution for m scales to one for m².) T1 is the single most
useful test in this document: **any mechanism producing Type I/II solutions must contain a step that is false at n = m².**

**Brauer–Manin (Bright–Loughran 2020, BL).** U_n : 4xyz = n(xy + xz + yz) has Br U_n / Br ℚ ≅ ℤ/2, there is **no
Brauer–Manin obstruction to ES at any n ≥ 2** (BL Thm 1.1/1.8; n = 1 *is* BM-obstructed), a BM obstruction to strong
approximation always exists, and BM does not explain all failures of strong approximation (`LITERATURE_2026.md:224–230`,
`DISPROOF_AVENUES.md:18–53`). So a counterexample would be a non-BM integral Hasse failure.

**Exceptional set.** Vaughan (1970): E(N) ≪ N exp(−c(log N)^{2/3}). The campaign's original line (all internal, unrefereed):
* E(N) ≪ N exp(−c(log N)^{2/3}(log log N)^{1/3}) (`paper/vaughan-loglog-note.tex`; PROVED).
* **E(N) ≪ N exp(−c(log N)^{3/4})** (`paper/es-threequarter-note.tex`; INTERNALLY PROVED, three reviews incl. a blind
  audit). Extends to every interval of length H (E(I) ≪ H exp(−c(log H)^{3/4}), (D)30) and to m/n uniformly in m ≥ 4
  (E_m(I) ≪ H exp(−c(log H)^{3/4} m^{−1/4}), (D)31).
* 3/4 is proved *sharp* for every CRT/coefficient-sum sieve architecture analysed (`EXCEPTIONAL_KARY3.md`, (D)24; STATUS
  "Exceptional-set exponent"); θ > 3/4 needs non-CRT input (tuple counts of growing order, residue-dense large sieves, weak
  SPW — each reduced to a precisely stated open statement).
* Elsholtz–Tao's Type I sum: **Σ_{p≤N} f_I(p) ≪ N log²N unconditionally** — removing the log log N that ET list as open
  ((D)32/32a/32b, `paper/es-typei-heegner-note`; PROVED relative to Kuznetsov/Petersson, Weil, twisted Weil, Selberg 3/16,
  λ₁(SL₂(ℤ)) > 1/4; *needs expert scrutiny*).

**Thin infinite families proved here** (PROVED, computer-assisted; Wave Z): ES holds for all n = 4^s + k, k ∈ {9, 57, 81,
129, 153, 177, 201, 225, 249} ((J)62), all 4^s + 105 ((J)69; every member Mordell-hard), and — sharpest — **all 3·2^s + 1**
((J)74, (J)75), **all 7·4^s + 9** ((J)75), **all 63·2^s + 1** ((J)80). The last three provably admit *no* finite covering by
Elsholtz–Tao/divisor classes ((J)22 Cor 1.5, (J)68 Lemma 3.1); they are reached by windows whose exponent budget is forced by
an algebraic factorisation (Sophie Germain, 4X⁴ + 1 = (2X² + 2X + 1)(2X² − 2X + 1)) or a moving-gap cubic class. Open:
15·2^s + 1, 4^s + 297 (and 4^s + 33, 4^s + 273). None of this transfers to primes ((J)76: every positive-density rung of the
menu ladder collapses to B1/B2).

**Other numerators.** m/n for m ≥ 5 has genuine exceptions for large m (Schinzel exceptions n_m ≥ exp(m^{1/3+o(1)}),
Pomerance–Weingartner); **8/n fails at n = 131 and 241** (E₈ ∩ primes < 2000 = {2, 3, 11, 17, 131, 241}; `AMPLIFY_EXCEPTION.md`
Thm 2.5, CERTIFIED; the 8/n failures are known, PW Table 1). 5/n and 7/n have no known exception (7/n: none in [3, 10¹³],
PW). This matters for §4: a numerator-uniform argument without a threshold would prove 8/131 ((J)41).

## 2. The reduction everything ends at: the single-integer lower tail

### 2.1 The (★) count and its exact forms (PROVED; `SINGLE_P_COUNT.md:40–94`, `BM_CORRECTED_COUNT.md:24–25`)

For odd n ≥ 3 let **R(n) := #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}.** Each triple gives the Type II solution
4/n = 1/(uBC) + 1/(nBC) + 1/(nuC) (injectively, `PARITY_AUDIT.md` Lemma 2.1′), so **R(p) ≥ 1 ⇒ ES(p).** (★) is the c = 1
line of Elsholtz–Tao Type II (the h = 1 subfamily). Equivalent forms for a prime p:
* pair form: R(p) = #{(u, B) ∈ ℕ² : gcd(u, B) = 1, p ≡ −(u+B) (mod 4uB)};
* divisor form: R(p) = Σ_{C≥1} #{d | 4Cp + 1 : d ≡ −1 (mod 4C)} (twice the count with d < √(4Cp+1); R(p) is even);
* trial form: R(p) = Σ_{(u,C) ∈ 𝓡} 1[(4uC − 1) | p + u], |𝓡| = (p/4) log p + O(p) (`PARITY_AUDIT.md` Lemma 2.1);
* SL₂ form: matrices [[a, p],[c, d]] ∈ SL₂(ℤ) with c ∈ 4ℕ, a, d ≥ 1, a ≡ d ≡ −1 (mod c).

So R(p) is a sum of ≍ p log p rare events with polylog mean: the *tied-modulus divisor event* of §3.

**Genus split.** With 𝒫(n) = {(u,B) : gcd(u,B) = 1, u + B odd, 4uB − u − B ≤ n}, q = 4uB, a = −(u+B):
R*(n) = Σ_{𝒫(n)} 1[n ≡ a (mod q)] = M_gen(n) + X(n), where M_gen is exactly the contribution of the characters of order ≤ 2
mod q and X that of order ≥ 3; R*(p) = R(p). **T1 lives entirely in the genus part:** M_gen(m²) = X(m²) = R*(m²) = 0.

**Census** (CERTIFIED to 10⁸ by two independent engines, extended to 10¹⁰ by one): among primes p ≡ 1 (4), (★) fails at
exactly **14 primes ≤ 10¹⁰**, from 409 to 8 813 281 ((J)89, `B1_LINE.md` §3.6); the b = 1 line (López 2024 Type A: p + 4d has a divisor ≡ −1 (mod 4d)) fails exactly
at 193, 2521, 66529 among primes p ≡ 1 (4) ≤ 10¹¹; the union of the two lines never fails ≤ 10⁸ ((J)89, (J)90). Note: (★)
failing is *not* ES failing.

### 2.2 The Brauer–Manin main term (PROVED, unconditional; `BM_CORRECTED_COUNT.md` §§1–2, (J)100)

* **BL's Brauer class is one Kronecker character per pair** (Thm 1.1): at the rational point P_{u,B} = (uBC, pBC, puC),
  inv_∞ α = −1 and inv_p α = (−uB/p) = χ_{−4uB}(p), while χ_{−4uB}(−(u+B)) = −1 identically. In the orthogonality expansion of
  1[p ≡ a (mod q)], the pair {1, χ_{−4uB}} contributes φ(q)⁻¹(1 − χ_{−4uB}(p)) = φ(q)⁻¹(1 + inv_∞·inv_p). BM is *one* of the
  s(q) real characters mod q, not the whole genus layer.
* **Definition.** M_BM(n) := Σ_{(u,B) ∈ 𝒫(n), gcd(n,q)=1} (1 − χ_{−4uB}(n))/φ(4uB). Each term is 0 or 2/φ(q); M_BM ≥ 0; it is
  mean-preserving pair by pair; **M_BM(m²) = 0 at every odd square** (T1 exactly); for primes M_BM(p) = M₀(p) − T(p) with
  M₀ = Σ 1/φ(4uB) and T(p) = Σ (−uB/p)/φ(4uB), a single Legendre symbol summed over a hyperbolic region.
* **Theorem 2.2.** M_BM(p) ≥ (3/(16π²) − o(1))(log p)² ≈ 0.0190 (log p)² (Burgess), ≥ (1/(32π²) − o(1))(log p)² (Pólya–
  Vinogradov); M₀(p) = (3/(2π²) + o(1))(log p)²; under GRH M_BM ∼ M₀ (CONDITIONAL).
* *(z52c, `BM_LVALUE.md` Thm A; PROVED, internal, cross-model reviewed.)* T(p) = (σ/4)·E(χ_p)·L(1, χ_p)² + O(p^{−1/16} log p)
  with an explicit Euler product E (sign χ_p(2)); for p ≡ 1 (4), T ≈ E·(h(p) log ε_p)²/p. Hence M_BM(p) ≥ M₀(p) − o(1) at
  p ≡ 5 (8) and M_BM(p) ≥ 0.1402 (log p)² ≥ 0.9225·M₀(p) at p ≡ 1 (8) (Stephens' bound on L(1, χ)), improving Theorem 2.2's
  0.0190. Main term only (B3); it explains only 4–5 % of the variance of R − M₀ (EVIDENCE).
* *(z52c, `RESIDUE_HARDNESS.md`; EVIDENCE + two PROVED lemmas.)* The full residue class of p (not just its characters) shifts
  the expected count: p ≡ 1 (mod q) forces the cheap denominators' shifts into the latest class mod 4q. A parameter-free
  local-density factor F fits all class means mod 3…16, 840 (class 1 is the hardest of 96 mod 840), absorbs the p ≡ 1 (q)
  and "practical p − 1" effects, and raises corr(model, log R) from 0.49 to 0.71. Main-term refinement only.
* **Two-sided asymptotics are false** (Prop 3.1, via Linnik): infinitely many p ≡ 1 (4) have
  R(p) ≥ exp((log 2/L_Lin − o(1)) log p/log log p), so every bound |R − M| ≤ (log p)^{O(1)} fails infinitely often (in the
  harmless direction). Only a one-sided statement can be true.

*Two normalisations of "the main term" — reconciled (R290 repair; `reviews/frontier-review.md` task (2)).* `PARITY_AUDIT.md`
Lemma 2.1 writes R(p) = M(p) + E(p) with M(p) = Σ_𝓡 1/(4uC − 1) = (log p)²/8 + O(log p) (PROVED): the zero Fourier frequency,
i.e. the density for *arbitrary integers* n. For *primes*, −u is a unit mod m = 4uC − 1, so the density is 1/φ(m), and
Σ_𝓡 1/φ(m) ∼ (1/8)∏_{ℓ odd}(1 + ℓ⁻²)(log p)² = (3/(2π²))(log p)² — the same constant as BM_CORRECTED's M₀ = Σ_𝒫 1/φ(4uB)
(which depends on p only through its size). Both count *ordered* triples (u, B, C) (R(p) is even; distinct (★) solutions
are R/2). So 1/8 is right for the all-integer average, 3/(2π²) for primes; at primes E(p) has mean ≈ +0.027(log p)².
EVIDENCE (R290, from scratch, windows of 2·10⁵ at 10⁶ and 10⁷): mean R over primes = 0.165, 0.163 × (log p)² (≈ M₀ + 0.2 log p);
mean R over all n = 0.133, 0.132 × (log p)² (≈ Σ1/m + 0.15 log p). Individual values (R(p) = 44, 52, 68 at p ≈ 10⁸, 10⁹, 10¹⁰)
fluctuate by ± ~15 and support neither constant. Nothing below depends on the constant.

### 2.3 The exact theta-quotient normal form (PROVED; `METAPLECTIC_ES.md` Thm K, (J)101)

Fix the level t ≥ 2 and count *ES words of level t*, R_t(n) := #{(u, v) : u, v ≥ 2, tuv − u − v = n} (for 4 | t, t = 4C,
these are the (★) triples with that C, up to the boundary u or B = 1). Put X = q^{t−1}, Q = q^t, θ(x) = (x; Q)_∞(Q/x; Q)_∞,
D_t^∓(N) := #{d | N : d ≡ ∓1 (mod t)}, σ_χ(N) = Σ_{d|N} χ(d). Then (K1′)
  q^{t−2}(Q;Q)_∞² θ(X²)/θ(X)² = Σ_{n≥0} (D_t⁻ − D_t⁺)(tn + 1) qⁿ = −(2/φ(t)) Σ_{n≥0} Σ_{χ mod t odd} σ_χ(tn + 1) qⁿ,
and R_t(n) = D_t⁻(tn+1) − β_t(n) with the explicit boundary term β_t(n) = 2·1[(t−1) | (n+1)] − 1[n = t−2] (K2). Since R_t =
½(D_t⁻ + D_t⁺) + ½(D_t⁻ − D_t⁺) − β_t, **the odd-character component of each level series is exactly a Kronecker theta
quotient** and the even component is an even-character divisor sum (Eisenstein data; no cusp forms appear in the identity). For 4 | t, T1 is an exact cancellation (D_t⁻(tm² + 1) = 0). The all-level word series is
Σ_{t,u,v≥2} q^{tuv−u−v} = Σ_{u,v≥2} q^{2uv−u−v}/(1 − q^{uv}). Also PROVED: holomorphic weight-½ forms are supported on finitely many square
classes (Serre–Stark), and the five-slice failure set is not such a support. Modular identification after normalisation and
the shifted-d₃ / GL(3)-Eisenstein reading are Assessment. *What this does not do:* an exact automorphic normal form does not
resolve the competition between ≍ log²p events at a single integer (B2/B3).

### 2.4 What would suffice (CONDITIONAL; `BM_CORRECTED_COUNT.md` §3.1)

  **H⁻_BM(ε, p₀):  R(p) ≥ ε·M_BM(p) for every prime p > p₀ (some fixed 0 < ε < 1).**

With Theorem 2.2 this gives R(p) ≥ 1, hence ES(p), for all large p; with a finite census, ES for all n. It is *not refuted by
T1* (both sides vanish at squares). It needs p₀ ≥ 8.9·10⁶ (the (★) census). **Honest reading** (Assessment, the source's own):
H⁻_BM is "ES-(★) in disguise up to ε" — a quantitative strengthening of (★), not a weakening; what the BM analysis buys is that
the main term is now unconditionally of the right size and square-exact. No implication from GRH/GLH, Elliott–Halberstam/BFI,
Montgomery, Kuznetsov/θ or any other standard equidistribution conjecture is established, "and none is known to us"
(`BM_CORRECTED_COUNT.md` §3.3; `SINGLE_P_COUNT` (J)98: GRH gives only M_gen(p) ≥ (1 − o(1)) log log p). Each of those
controls averages over the integer, the modulus or the character — never one integer with a polylog main term.

*Numerics for H⁻_BM* (EVIDENCE). Primes ≤ 10⁶: min M_BM/L² = 0.062 (far above the proved 0.019), mean M_BM/L² = 0.149 at p > 5·10⁵ (`BM_CORRECTED_COUNT.md` §3.2). Zero law (measured on odd non-squares
n ∈ [10⁵, 10⁶], with R* and the mod-8-refined main term M_BM8): P(R* = 0 | M)
is ≈ 1.5–2.8 × the swap-Poisson value e^{−M/2} for M < 22, possibly fatter beyond (6 zeros). Whether log P(0 | M(n))/log n → −∞
is "exactly the open question; nothing at 10⁶ decides it." Precedent for caution: for Markoff surfaces (same (log m)²
class-number scale) there are infinitely many integral Hasse failures *with non-empty BM set* (Loughran–Mitankin Thm 1.5;
Ghosh–Sarnak).

*Related exact reductions.* Five-slice ES (ES₅; λ(p) ≤ 3 in continued-fraction length) has a T1-exact BM main term with
principal constant **45/(8π²)** (`BOARD2_SLATE.md` Prop 3.4: Assessment — Dirichlet-series sketch plus EVIDENCE fit) and
unconditional Burgess bound M(p) ≥ (45/(32π²) − o(1))L² (Thm 3.5, PROVED; (J)105;
this *corrects* the board memo's 33/(8π²), so cite BOARD2_SLATE, not the memo). In level coordinates
M_t^lev(n) = (τ(N) − σ_{χ_{−t}}(N))/φ(t) ≥ 0 (N = tn + 1), and **some 4 | t ≤ 4ℓ(n) has M_t^lev(n) > 0 iff n is not a
square** (ℓ(n) = least odd prime with (n/ℓ) = −1; `SYNTHESIS_SPARKS9.md` Prop 2.2, (J)103): *the BM layer is pointwise free.*
What remains is the class of the divisor inside the coset {χ_{−t} = −1} (size φ(t)/2), where the other genus and higher-order
characters are active. The expected number of "hit" levels is ≈ (0.44 → 0.97)·log p for p ≤ 3·10⁶ (EVIDENCE): critical, not
supercritical.

## 3. The barrier map, as theorems with exact hypotheses

Format: **statement** · *scope* · rules out · does NOT rule out · pointer. The classic six (B1–B6) come from the automorphic
phase (`reviews/redteam-automorphic.md` §4 collapse tests T1–T8, `reviews/redteam-automorphic-2.md` §2–3); the rest were added
in Waves Y–AC. A barrier "with known technology" is an Assessment about methods, never an impossibility theorem for ES.

**B1 — formal genericity (congruences, identities, bounded search).** `POINTWISE_SIZE.md` Thms M, C, Prop A; (H)-ledger.
* *Statement.* Thm M (PROVED): a deterministic procedure (ring operations, floor division, sign/size tests, full
  factorisations, loops over the resulting lists) whose run at a profinite "square-mimicking" point is finite follows that
  formal run at every admissible p (one congruence class, all polynomials met take prime values). Thm C (CONDITIONAL on
  Hypothesis H): every *correct* bounded witness-producing procedure fails for infinitely many p ≡ 1 (24). Prop A (PROVED):
  eventual-sign size comparisons (against p^θ, divisors in [p^θ, 2p^θ], …) stay inside the scope. Instances: Mordell–Schinzel
  (square classes are not solvable by polynomials), ET's odd-square remark, FORMAL_CLOSURE Thm F (the signed seed component
  is sterile for infinitely many p = 24q + 1, under H for 6402 explicit polynomials; the sibling needs Dickson for only 159
  linear forms). Quantitative form: the least Type II witness modulus satisfies W(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4}) for infinitely
  many Mordell-hard primes, so no multiplier mechanism with witness moduli ≤ exp((log p)^{1/4−ε}) proves ES
  (`POINTWISE_OMEGA13.md` Thm 5.1, PROVED modulo Gallagher, Nair–Tenenbaum and the energy bound).
* *Rules out:* congruence coverings, finite unions of polynomial/identity families, bounded searches, Haar/CRT majorants.
* *Does NOT rule out:* (E1) a search over a p-dependent family of integers whose length grows with p, or (E2) non-quasi-
  polynomial primitives (⌊p^θ⌋, the least non-residue, orders) *whose actual factorisations are then used*. Whether fixed
  non-abelian Frobenius data escape was left open there (later: inert on finite witness sets, (J)96, and see B-reciprocity).

**B2 — divisor-class reduction (the tied-modulus divisor event).** `reviews/redteam-automorphic-2.md` Lemma 2.1 / Thm 2.2, (I)8.
* *Statement.* Every two-coordinate slice of ET's varieties is either a finite union of congruence classes of p, or "one
  integer N_θ(p) has a divisor in a residue class mod q_θ" (PROVED, elementary). All encodings tried (Heegner/Hecke, Type II
  shells, ternary forms, quaternion orders in B_{p,∞}, Brauer–Manin, fibrations, class-number identities, GRH/GLH/covering
  conjectures) are such slices (Thm 2.2(i),(ii), PROVED relative to the reviewed statements). Thm 2.2(iii) (CONDITIONAL on H):
  any argument certifying ES(p) through a *fixed* finite set Θ₀ of slices fails for infinitely many p ≡ 1 (24).
* *Scope:* (iii) needs Θ₀ fixed independently of p.
* *Rules out:* any fixed finite menu of slices, however clever the auxiliary input.
* *Does NOT rule out:* growing, p-dependent families of slices (hatch H-A) or a parity-breaking count at fixed p (H-B) — but
  see "tied modulus" below for why both are, so far, the same wall.

**B3 — scale constraint.** `CONDITIONAL_ES.md` Prop 2.3, Remark 2.4; phase (I) Prop 5.4.
* *Statement* (PROVED relative to ET Thm 1.1). If a hypothesis drives an ES-detector with target main term M(p) and error
  ≤ M/2 through an encoding with fibres ≤ μ(p), then M(p) ≤ 2μ(p)f(p); for μ ≤ p^{o(1)} (every natural lattice/Heegner/matrix
  parametrisation), M(p) ≤ p^{o(1)} for all p outside a density-zero set. Thickening a target to width K/p (Prop 5.4) is
  exactly averaging over n with |n − p| ≤ K.
* *Rules out:* every "main term = power of p, error = smaller power" argument (Heegner/CM equidistribution with |D| ≥ p^κ,
  power-scale covering conjectures, termwise GRH).
* *Does NOT rule out* (Remark 2.4): a polylog main term with a power-small error (M ≍ log²p, error ≪ p^{−η}), high-
  multiplicity encodings, families of size p^{o(1)} with unrestricted auxiliaries. This is exactly where §2 sits.

**B4 — deterministic pigeonhole / large fibres.** `LONGSHOT_PIGEONHOLE.md` Thm 2.2, `LONGSHOT_FIBRED.md` Thm 3.1.
* *Statement.* Transparent covering certificates (residues of the prime factors below the modulus, plus one opaque cofactor)
  covering a coset of size ≥ φ(e)e^{−θ}/2 (θ < 1/2; R135 remark: any θ < 1) fail, simultaneously in every e-slice of both
  types, for a set of primes of positive lower relative density inside p ≡ 1 (mod 8∏_{3≤ℓ≤Y}ℓ) (PROVED relative to classical
  inputs; certificates that merely hit −1 or cover smaller cosets are not excluded; R290 repair); pigeonhole collisions give only signed solutions. Algebraic/orbit
  recipes with bounded covolume ratio: the fibre factor cancels and B3 returns (PROVED relative to the counting theorems).
* *Scope:* transparent coset-covering certificates; arithmetic-group orbits with a covolume count.
* *Does NOT rule out:* CONJECTURE PH (`LONGSHOT_PIGEONHOLE.md` Conj 5.1: for every large p some e ≡ −p (mod 4) with
  φ(e) ≥ 40 has a full-coset cover; EVIDENCE: all Mordell-hard primes < 10⁶ except 3529, 110881 (e ≤ 2000), 300-prime samples
  after 10^k up to 10⁸ (e ≤ 5000), 14 selected hard primes ≤ 3.7·10⁷ (e ≤ 20000); R290 repair) —
  open, and by Thm 2.2 not easier than the lottery it replaces (Assessment).

**B5 = T1 — the odd-square test.** ET Prop 1.6; `PARITY_AUDIT.md` Lemma 3.2; (J)13 (T1 = Kudla's Diff-parity = Hilbert
reciprocity for the incoherent ternary collection).
* *Statement.* f_I(m²) = f_II(m²) = 0 for odd m, while local/genus/spinor conditions all hold; at the level of single events:
  for any square n = m² and every u ≥ 1, n + u has no divisor ≡ −1 (mod 4u) (PROVED). At a prime p ≡ 1 (4), any hit f | p + u,
  f ≡ −1 (mod 4u), has a prime factor ℓ with (ℓ/p) = −1 (Lemma CT / Lemma 3.2).
* *Rules out* (for routes producing Type I/II solutions): every route whose steps are all true at odd squares: "local + spinor ⇒ global", Siegel–Weil/genus averages,
  full-rank theta series, BM-type corrections alone, fibration/descent through finitely many families.
* *Does NOT rule out:* routes that use the quadratic character at p (non-residues) in an essential way.
  T1 is *one* order-2 obstruction; it deforms to near-squares (p = m² + k with tk + 1 = c² forces level t to χ = +1, (J)53,
  (J)55), explaining a 6–7σ deficit there.

**B6 = T7 — the average leak.** Any estimate averaged over p, or over a level/discriminant attached to p (spectral large
sieve, DI Thm 7, Kuznetsov with exceptional eigenvalues, Bombieri–Vinogradov, zero-density), says nothing at a single p.
Concretely: Σ_{p≤N} f_I(p) ≪ N log²N ((D)32b) and the 3/4 exceptional-set bound are theorems *on average*; neither establishes
ES for a prescribed prime. Fixed-p variance diagnostics were tried and fail ((J)103: "critical"). Use T7 against every cited estimate.

**B-fin — ES is a finite search with moving moduli.** (J)23, (J)25, (J)28 (`UNIT_ORBIT_ES.md`, `FIXED_MODULUS_SHOTS.md`,
`SYNTHESIS_SPARKS2.md`).
* *Statement.* Every certifying modulus of ES(p) is O(p²); ES itself has **no infinite fixed-modulus shot family** (scoped
  no-go, PROVED: for a fixed-coefficient affine Type II shot αp + β a divisor h certifies iff h ≡ −1 (mod 4M) with
  M ∈ 𝓜(α, β), and every M ≥ √height/2; any fixed Chebotarev firing set admits only finitely many shots). By contrast the
  T1-bearing cousins with infinitely many fixed-modulus shots are **theorems**: ES^{(S)} (4/n = 1/x + 1/y + Q²/Z, mute primes
  S, |S| ≥ 4) for every n coprime to 2S, unconditionally (Gupta–Murty sieve); V_φ over ℤ[φ] under GRH; and ES^□ (third
  denominator may carry an odd square) from ONE Dirichlet prime r ≡ 3 (4) with (n/r) = −1 (PROVED, elementary).
* *Rules out:* "transport a proved cousin back": the cousins' search at fixed n is infinite with a fixed firing modulus; ES's is
  finite (O(p²)) with moduli that move. A provable T1-bearing variant is by itself weak evidence about ES ((J)28).
* *Does NOT rule out:* a mechanism that transports ES^{(S)}/V_φ certificates into the O(p²) box, or a new finite-search
  mechanism. Neither is known. The gap is an exponent cap: a shot is an ES solution iff Q | (r+1)/4 instead of
  rad(Q) | (r+1)/4 ((J)34).

**Tied modulus / height-dependent target.** `PARITY_AUDIT.md` Lemma 2.1′, Assessment 2.2, Remark 3.1; (J)87.
* *Statement.* Previous elementary pointwise benchmark: |E(p)| = |R(p) − M(p)| ≪ p^{1/3+o(1)} (PROVED, elementary block count
  N(U,V) ≤ p^{o(1)}min(U, V, p/(UV)+1), `Z52D_HYPERBOLA.md` Thm 1; ET Prop 1.7's p^{2/5} is for the full Type II count; no
  cancellation either way), against M(p) ≍ (log p)². *(z53, cross-model reviewed:)* now R(n) ≪_ε n^{12/37+ε} for every n
  (`Z53_SQSIEVE.md` Thm A, PROVED rel. Weil's Kloosterman bound and the third-derivative test; preceded by
  R(n) ≪ n^{1/3−1/225}(log n)² for n ≥ 2 in `Z53_HYPSUMPROD.md` Thm 1, the first power saving in this campaign; external
  priority is unverified): near the cube the tie is a perfect-square condition, detected by Heath-Brown's
  square sieve. Upper bound uniform in n, valid at odd squares — silent on positivity. Weil on the modular hyperbola 𝓗 = {xy ≡ 1 (mod 4p)} has error p^{1/2+o(1)}
  even for one box, and (★) is ≍ p height-sub-counts, so Weil does not even bound E(p). Remark 3.1 (Assessment): every result
  beating Weil/Selberg–Hooley averages over a variable *independent of the modulus* (the residue, the moduli q ≤ x^θ with n
  free, the sequence variable). At one p, either the averaged variable *is* the modulus of the class condition ((u,C), (u,B)
  coordinates), or, on 𝓗 where x, y are free, the class condition depends on the height: x ≡ y ≡ −1 (mod 4C),
  C = (xy − 1)/(4p). "These are two descriptions of one obstruction."
* *Rules out* (as Assessment): H-B (parity-breaking à la Friedlander–Iwaniec at fixed p) with known inputs; it collapses into
  H-A. Type II/bilinear fixed-modulus savings (Blomer–Pascadi, KMS, Bourgain–Garaev) need saving p^{1−o(1)} on unit
  coefficients.
* *Does NOT rule out:* cancellation on 𝓗 with a height-dependent target — "the only lead not ruled out". No lower bound for
  the difficulty of (★) is proved; under an independent-incidence model the variance is ≈ M(p).

**Reciprocity forces parity, never class; the Stickelberger m = 2 coincidence.** `CLASS_FORCING.md` Thms 2.1, 5.2 ((J)93);
`TWO_POWER_LADDER.md` Thms 3.1, 3.2 ((J)104); (J)89, (J)96.
* *Statement.* CLASS_FORCING Thm 2.1 (PROVED): on a fixed line with modulus t and G = (ℤ/t)^×, every character ψ(N) of the
  total product is a function of p mod t — the forced quotient is all of G and **no reciprocity law (quadratic, cubic,
  quartic, Eisenstein, Artin for ray class fields mod t) adds information about [N] ∈ G**; Frobenius in a finite Galois Ω sees
  exactly the image of [p] in G/G_G. Thm 5.2 (PROVED, unconditional): for any Chebotarev class C compatible with p ≡ 1 (4),
  any d and any a ∈ (ℤ/4d)^×, infinitely many p with Frob_p ∈ C have p + 4d with a prime factor ℓ ≡ a (mod 4d), ℓ arbitrarily
  large — no class is forbidden for a single large factor. The one individual link is χ_{−4d}(ℓ) = (ℓ/p) (parity). Every
  bounded-level forced rule with small primes fails on all four lines at every p ≡ 1 (mod M). Higher reciprocity:
  TWO_POWER_LADDER Thm 3.2 (PROVED for m = 3, 4): the ES datum is the norm component D = ∏ x_a, forcing sees the
  Stickelberger component S = ∏ x_a^{a⁻¹}; D is determined by S only modulo μ_m^{gcd(2,m)} (m = 3: S says nothing about D;
  m = 4: D² = S², a free sign). Thm 3.1 (PROVED; ℓ ∤ m, 4 | lcm(M, m)): along forced progressions no congruence determines
  a character layer beyond its quadratic part. For **m = 2, S = D** — that coincidence *is* the BM layer and T1 (Assessment);
  there is no odd-order BM layer. 2-group levels alone do not suffice (1,298 primes ≤ 10⁶ have no word at any such level).
* *Rules out:* getting the divisor *class* (as opposed to its quadratic parity) from reciprocity, Chebotarev, Rédei or
  higher power-residue data, at bounded level or along forced progressions with one varying level prime.
* *Does NOT rule out:* joint restrictions on *all* varying prime factors of tn + 1 simultaneously (the "full factor
  multiset" realisation question, CLASS_FORCING §6); the general-m Stickelberger identity is not proved.

**Privacy of large primes.** `SYNTHESIS_SPARKS8.md` Lemma 2.3 (PROVED): gcd(jp + 1, j′p + 1) | j − j′, so a prime ℓ > J
divides at most one of jp + 1 (j ≤ J); likewise p + 4d (d ≤ D) for ℓ > 4D. *Reading (Assessment):* pigeonhole across shifts
can only collide small primes ℓ ≤ J, i.e. congruence (B1) data, blind at the T1 point; the large prime factors that make the
lottery succeed are private to one integer, so a deterministic mechanism must produce a divisor of ONE integer in ONE moving
class (B2) with no cross-shift leverage. *Does NOT rule out:* mechanisms that never pool across shifts.

**Positivity obstruction (and why positivity is not the bottleneck).** (J)52 (`SYNTHESIS_SPARKS4.md`), (J)84 Thm A
(`JOINT_BUDGET.md`), (J)89 Lemma 4.1.
* *Statement.* (J)84 Thm A (PROVED, elementary): with p a free variable and slice parameters polynomial in an auxiliary u,
  every ES side number is (p-free content) × (irreducible in ℚ[u, p]); the only non-trivial input is d > 0 (a signed slice
  d = −w² makes p² + 4c²d split identically). So a thin-family algebraic budget needs a relation p = φ(u) (irreducible top
  part ⇒ the (J)79 collapse; variable-linear φ ⇒ a B2 event). Prop 4.2: windows m with p + m = c·w² are Jacobi-forced iff
  (c/p) = −1; so near-square windows m = w² − p, CF norms |P_k² − pQ_k²| (gcd(Q_k, m) = 1) and m | A² − pB² (gcd(B, m) = 1) have
  (p/m) = +1 and are never forced (general c is not excluded, but then c supplies the non-residue; CF/Pell data used as other
  coordinates is not covered). p is a non-square modulo every class modulus 4ab (Prop 4.3), so auxiliaries handing over
  divisors of p − 1 pin p to the sterile point locally.
  (J)52 (PROVED): positive words ⟺ definite path forms; the three-bit law "certificate ⟺ χ·s_∞ = −1" holds for all words,
  signed included. (J)89 Lemma 4.1 (PROVED; p ≡ 1 (4), gcd(p, cd) = 1, Type I divisibility): signed slices have (|d|/p) = +1,
  positive ones (d/p) = −1; hence no move preserving |d| (or its square class mod p) takes signed points to positive ones
  (Cor 4.2), and there is no Vieta-type involution.
* *Rules out:* "solve the signed problem, then reflect back" by |d|-preserving moves; polynomial algebraic budgets at a
  general prime. A transfer that changes the square class of d is not excluded — it must find a non-residue *and* produce the
  divisor in the new class, i.e. B2 again (Assessment).
* *Does NOT rule out:* anything about ES directly — the signed relaxation SQ_± is *just as much a lottery* (Assessment):
  positivity is T1's anchor (the archimedean Hilbert factor), not the source of difficulty. Residual of Thm A: φ* reducible
  of degree ≥ 2 in every variable.

**Numerator blindness; numerator models with real exceptions.** (J)41 (`SYNTHESIS_SPARKS3.md`), (J)46/(J)49, (J)86
(`AMPLIFY_EXCEPTION.md` Thm 2.5), (J)88 (`NONCONG_LIFTS.md`).
* *Statement.* (J)41 Thm 1.1 (PROVED): for every M ≡ 0 (4) the □-relaxation M^□(n) holds at every odd non-square n prime to
  M (one Dirichlet prime), and the M-shot mechanism keeps T1 exactly. Yet M/p fails at 278 known pairs (M ∈ {8, 12, 16, 20,
  24}; CERTIFIED), e.g. 8/131 has no unit-fraction solution but 8/131 = 1/20 + 1/131 + 9/2620. Threshold-robust form (relative
  to Pomerance–Weingartner Thm 1.2): for every M ≡ 0 (4) with M ≥ 6.52·10⁹ some prime p ∈ (M², 2M²) has M^□(p) and not M/p.
  Full T1 holds for every 4 | M and fails for M = 3, 5, 6, 7, 11, 19 (certified); among failure-free numerators (3, 4, 5, 7)
  only 4 has full T1. (J)86: numerator models k/n have genuine exceptions (8/131, 8/241) and refute every k-uniform law shape
  tested (e.g. the square law p ∈ E_k ⇒ p² ∈ E_k fails: 8/11 is exceptional, 8/121 = 1/18 + 1/99 + 1/2178). (J)88:
  fixed-slice separations between k = 4 and 4 | k ≥ 8 exist but fail for one-parameter polynomial families.
* *Rules out* (Assessment): any argument whose every step — shot identities, overflow duality, T1/BM/Diff-parity, box
  finiteness, sieves, composition, class-group pigeonhole — works uniformly in the numerator **without a threshold**; it
  would prove 8/131.
* *Does NOT rule out:* k-uniform arguments valid only for p > p₀(k); 4-specific inputs. The cleanest known 4-specific input:
  **m = 4 is the unique numerator whose five HJ slices are exactly a quadratic-character fibre** S₄ = {χ = −1} ((J)32), with
  χ = minus the 2-adic isotropy sign of the path form ((J)33); the 2-adic pigeonhole content is used up by a Fano-plane
  argument ((J)57: forcing only for M ∈ {2, 3, 4}).

**No BM obstruction / the shape of a disproof.** (J)97 (`DISPROOF_AVENUES.md`).
* *Statement.* BL Thm 1.8 (PROVED, literature): (U_n(ℝ)₊ × ∏_p U_n(ℤ_p))^{Br} ≠ ∅ for every n ≥ 2. So a counterexample is a
  non-BM integral failure. The "n = 1 shadow" (CONDITIONAL on Dickson/H): primes p ≡ 1 (mod Q) with prime slice cofactors
  empty any *finite* set of ET slices. EVIDENCE: a universal zero law across the numerator ladder m = 4…24,
  P(f = 0) ≈ exp(−0.535 μ^{0.91}) by local cell mean μ (underpredicts top-μ zeros by ×3–5); adversarial BPSW-probable primes at
  10¹⁸–10²⁵ stay far from failure (at least 612 solutions on the cheap slices).
* *Assessment.* P(ES false) "well under 10⁻³", all of it model risk (a floor/mixture or a global non-congruential mechanism);
  model-internal estimates are < 10⁻³⁰. A disproof would need a **"prime T1"**: a global invariant forcing all ≍ (log p)³
  divisor events into the wrong class at one prime. None is known; T1 itself exists only because squares make every relevant
  prime a residue.
* *Does NOT rule out:* non-BM Hasse failures in principle — the Markoff precedent (§2.4) shows they occur at the same scale.

**The power ladder is flat.** (J)108 (`POWER_LADDER_ES.md`). ES_(k): 4/n = 1/x + 1/y + Q^k/Z with Q odd, gcd(Q, n) = 1 and
**gcd(Q, Z) = 1** (lowest terms are essential: without them every rung is the same, Remark 1.2). Odd k (Thm 2.1, PROVED): for
odd n take the least Q ≡ −n (mod 4) prime to n and 4x = n + Q^k: 4/n = 1/(2x) + 1/(2x) + Q^k/(nx); at primes Q ∈ {1, 3}; all
n by a finite covering plus scaling; T1 is dead (odd squares get Type I-shaped solutions). Even k (Thm 2.3): one Dirichlet
prime r ≡ 3 (4) with (n/r) = −1, chosen with r ≢ 1 modulo the odd primes of k, as for ES^□; T1 intact for this Type II-shaped
construction. By scaling every rung holds for every n ≥ 2 (Cor 2.5) — the ladder carries one bit of *mechanism* (k mod 2) and
zero bits of truth; **no rung is strictly between ES^□ and ES in difficulty** (Assessment). Reason (PROVED bits + Assessment):
the relevant single-modulus index is i_k(g) = gcd(k, g − 1), which the construction makes 1 (odd k) or 2 (even k) by choosing
the prime; the ladder is flat because ord(T1) = 2 coincides with the unavoidable 2-part of every shot index — "a coincidence of the prime 2" (over ℤ[ω], TES
separates the two). *Rules out:* climbing from ES^□ to ES through intermediate power relaxations. *By-product:* the variant whose third
numerator may be a power of one fixed prime q (4/n = 1/x + 1/y + q^c/Z, "one mute prime") holds for every n prime to q, PROVED
per q under an elementary hypothesis on q (Thm 5.1; checked for all q ≤ 10⁶; all non-square q under GRH).

**The M1a/M1b/M2–M5 pattern: B2 is not any solved problem.** (J)94 (`B2_ACROSS_FIELDS.md` "The pattern", Assessment; 13
fields surveyed). Every pointwise existence theorem surveyed uses at least one input that B2 lacks:

| input | used by (examples) | B2 lacks it because |
|---|---|---|
| M1a power-size count of final objects | Duke, ternary forms, 290-thm, Bourgain–Gamburd–Sarnak, Shkredov/Zhang Zaremba (claimed) | count ≍ (log p)²–(log p)³ |
| M1b power-size auxiliary set + pigeonhole/volume | Thue/Minkowski (p = x² + y²), Dirichlet/Pell | target class depends on the exact height; covering needs sub-power windows ((J)85) |
| M2 fixed-modulus character/group event | least QNR / primitive roots under GRH, Lipshitz LGP | tied modulus (fixed only in CF coordinates, where M1 fails) |
| M3 homogeneity / group action | strong approximation for groups, BGS, one-class genera | U_n not homogeneous; finite automorphism group |
| M5 count congruence (parity / mod-p count) | Zagier windmill, Chevalley–Warning, EGZ | T1: count is 0 at odd squares, so the congruence must see the quadratic character (finite-menu affine involutions barred, (J)2, CONDITIONAL) |
| M4 freedom to choose objects | AGP Carmichael, Bloom/Croot, fibration methods | p and K = (p+q)/4 are forced |

The sharpest test is Zaremba, *claimed* proved pointwise in 2026 (Shkredov arXiv:2603.14116, every prime/squarefree q; X. Zhang
arXiv:2605.02518, all q, building on Shkredov's framework — unrefereed; only the statements were checked here, not the
proofs): pointwise by M1 + M2; ES₅ keeps M2 but has only
≍ log²p certificates (the quadratic non-residues A with HJ-length(p/A) ≤ 3). Known-in-substance: λ(p) ≤ (6/π²) log p log log p
+ O(log p) (Aistleitner–Borda–Hauke attribution, (J)105), with ES₅ ⟺ λ(p) ≤ 3; the Zaremba method reaches ES only at CF length
≍ log p log log p, a known relaxation ((J)95). Literature survey ((J)103, Assessment): **no every-n theorem was found for any natural
problem with a polylog main term.**

**Rooted constructions and bounded windows die under Dickson.** (J)106 (`LOWER_TAIL_ASTRA.md`), (J)83 (`CAP_BOUNDED.md`).
The positive-word endpoint graph F_n (edge uv iff uv | n + u + v) is a **forest** (each v > 1 has at most one smaller
neighbour, −n mod v; PROVED), and, for unit endpoints and n ≡ 1 (4) (automatic at primes p > 3), five-slice certificates are exactly its
bichromatic edges (χ_n-colouring). Under Dickson,
for every fixed H, infinitely many p ≡ 1 (24) have every component meeting {1,…,H} monochromatic; rooting at the least
non-residue also fails i.o. (p = 2521 + 9240a with (p + 11)/12 prime). For every M, infinitely many p ≡ 1 (8) have no window
certificate with m ≤ M at any cap (CONDITIONAL on Dickson). *Rules out:* fixed finite root sets and bounded windows. *Does NOT
rule out:* growing/p-dependent roots, class-group cycle data, arbitrary functions of Pell-cycle data. (The principal-cycle
root menu itself fails i.o. under H: `Z52D_PELLCYCLE.md` Thm 1.1, see §7.2.)

## 4. What a proof would need — a five-minute screening checklist

Screen an idea against every line *before* investing in it. Each line names the barrier that killed earlier ideas of that
kind. **Scope (read this):** the barriers of §3 are theorems about *specified classes of arguments* (fixed menus, bounded
multiplicity, numerator-uniform steps, …) or Assessments about known methods; they are not necessary conditions for every
conceivable proof, and a proof need not take the form of a lower bound for (★). Treat a failed line as "this is the step
that must be new", not as a refutation — but then that step must be named and justified. Nothing proposed in this campaign
has passed all lines.

1. **It must fail at odd squares (T1/B5).** Name the step that is false at n = m². In practice the argument must use the
   quadratic character of p essentially (in every solution of 4/p with p ≡ 1 (4), every denominator prime to p has a prime
   factor ℓ with (ℓ/p) = −1; Lemma CT). Local/genus/spinor/Siegel–Weil/BM-type steps are all true at m²; they cannot carry
   the argument. (Composite-n descent must be checked separately: a solution for m scales to one for m², so T1 does not bind arguments
   that produce mixed or scaled solutions.)
2. **It must fail for numerator 8 at 131 and 241** (i.e. it must not also prove 8/131, 8/241) (and 8/11, 8/17; numerator blindness (J)41, (J)86). If every step works
   for M/n with M ≡ 0 (4) uniformly and without a threshold, the argument proves false statements. Say where 4 enters
   (candidate: the χ-fibre S₄ of (J)32) or which threshold p₀(M) the argument needs.
3. **It must not be numerator-uniform in its laws** — no k-uniform transport, square law or recombination law (all refuted
   on k/n models, (J)86, (J)88).
4. **It must break the tied modulus (B2, PARITY_AUDIT Remark 3.1).** Identify the modulus of the class condition. If it is
   fixed, find where the height dependence went (x ≡ y ≡ −1 mod 4C with C = (xy − 1)/4p); if it moves with the solution, say
   which theorem controls divisors of *one* integer in a moving class with error below a (log p)² main term. No such theorem
   is known. A fixed finite menu of slices fails infinitely often (CONDITIONAL on H, (I)8), as do fixed root sets and
   bounded windows (CONDITIONAL on Dickson, (J)106, (J)83).
5. **p must stay fixed throughout (B6/T7).** List every averaged variable in every cited estimate. Averages over p, over the
   level/discriminant attached to p, over residues a, or over moduli q ≤ x^θ with n free do not by themselves reach one p;
   an averaged input is fine only if the step that recovers the prescribed p is identified.
6. **Scale (B3).** If it is "main term ≥ 2·error", compute the main term: power-size main terms with ≤ p^{o(1)}-to-one
   encodings are impossible for almost all p. The live regime is polylog main term with error below it at one integer.
   (R290 repair) Use the prime density 1/φ(m), not 1/m, when computing an expected count at a prime: for (★) this is
   3/(2π²) vs 1/8 times (log p)² (§2.2).
7. **One-sided only.** Any claimed two-sided asymptotic R(p) = M(p)(1 + o(1)), or |R − M| ≤ (log p)^{O(1)}, is false
   infinitely often (Linnik, `BM_CORRECTED_COUNT` Prop 3.1).
8. **Not congruence + factorisation shape (B1).** If the input is p mod M plus the factorisation shapes of fixed
   polynomials in p (even with size comparisons against p^θ), it fails at a square-mimicking point under H. You need a
   p-dependent growing family (E1) or non-quasi-polynomial primitives (E2) *and* control of their actual factorisations.
9. **Class, not parity.** If the forcing comes from reciprocity, Chebotarev, Rédei or higher residue symbols, it delivers
   only the quadratic layer of the divisor class (CLASS_FORCING Thm 2.1, TWO_POWER_LADDER Thms 3.1–3.2). ES needs the class:
   the BM-allowed half contains φ(4u)/2 residue classes mod 4u, and ES needs the single class −1 among them.
10. **No pooling of large primes across shifts** (privacy, SS8 Lemma 2.3): a collision across jp + 1 or p + 4d involves only
    primes ≤ the shift range, i.e. congruence data.
11. **No signed detour by reflection** ((J)52, (J)89 Lemma 4.1, Cor 4.2): signed Type I slices have the wrong Legendre
    symbol, so no |d|-preserving (or square-class-preserving) move reaches positive points; a class-changing transfer is a new
    B2 problem.
12. **No relaxation-then-transport without a transport theorem.** ES^□, ES^{(S)}, V_φ, capped ES^{(y,e)}, odd power rungs,
    and ES at CF length ≍ log p log log p are theorems (or near-theorems) *because* they have fixed-modulus shots or
    density; the power ladder is flat ((J)108) and ES is a finite O(p²) search with moving moduli ((J)25). Say how
    certificates get back into the O(p²) box with cap 0.
13. **No BM/local-global shortcut.** There is no BM obstruction at any n ≥ 2, so BM supplies nothing to prove; "BM is the
    only obstruction on U_n" is literally ES(n) ((I)7). The BM main term is free pointwise ((J)103 Prop 2.2) — the problem
    is the class inside the coset.
14. **Run it on the test primes.** (★) fails at 14 primes p ≡ 1 (4) ≤ 10¹⁰: 409, 577, 5569, 9601, 23929, 83449, 102001,
    329617, 712321, …, 8 813 281 (`BM_CORRECTED_COUNT.md` §3.2, `B1_LINE.md` §3.6); the b = 1 line fails at 193, 2521, 66529;
    at p = 3361 the only Type II solutions are 1/850 + 1/(3361·25) + 1/(3361·170) and 1/841 + 1/(3361·290) + 1/(3361·8410), all
    on non-split slices ((J)82; 3361 is conjecturally the only prime without a prime-modulus Type II certificate, PM-II,
    exhaustive to 10⁸); at p = 5101441 the a = 1 slice has a single solution. A mechanism claiming that one fixed line or
    grammar always succeeds must survive these (the board found an HJ grammar that traps at 193).
15. **Square classes mod 840 and near-squares.** The hardest primes are in the Mordell classes and at bounded p − m²; T1
    deforms there ((J)53, (J)55). Check the idea at p = m² + k with small k.
16. **Thin-family wins do not transfer.** Forced-budget windows (Sophie Germain, moving-gap cubic) prove 3·2^s + 1 etc.;
    at a general prime the side numbers are irreducible in ℚ[u, p] ((J)84), so an algebraic budget needs p = φ(u).
17. **Covering certificates must use large prime factors (B4; R290 repair).** If the plan is to cover the target coset −K_e
    from the prime factors of N_e(p), certificates built from the factors below e (plus one opaque cofactor) fail on a
    positive-density set of primes (`LONGSHOT_PIGEONHOLE.md` Thm 2.2); collisions/pigeonhole give only signed solutions. Say
    which theorem controls the residues of the large prime factors — that is the lottery (B2) again.

**Profile that passes all the screens** (Assessment, distilled from the above and both boards; not a theorem): a single-integer
statement at fixed p; uses the quadratic character of p (vanishes at squares); 4-specific or with an explicit threshold;
controls the *class* of a divisor of one integer in a modulus tied to the solution; one-sided, with error below a
(log p)² main term; not an average over any parameter attached to p. Board #2 (seats from three labs) was unanimous that
no single-prime lower-tail mechanism is known.

## 5. Best partial results and conditional results

*All internal; none externally refereed. "PROVED rel. X" = proved relative to the published theorems X.*

**5.1 Unconditional, on average / almost all** (B6 applies to every item).
* E(N) ≪ N exp(−c(log N)^{3/4}) (INTERNALLY PROVED; `paper/es-threequarter-note`), shift-uniform in every interval of length H
  and in progressions n ≡ b (mod q) for q ≤ exp(c′(log(H/q))^{3/4}) or q with all prime factors large ((D)30; large smooth q
  open), uniform in the numerator m ((D)31); 3/4 sharp for CRT architectures ((D)24, (D)27, (D)28).
* *(z50, `BREADTH_Z45.md` §15.)* ES₅ and U: E_ES₅(N) ≤ E_U(N) ≪ N exp(−c(log N)^{2/3}(log log N)^{−1/3}) over n ≡ 1 (4)
  (`EXSET_I3.md` §7.3), and #{p ≤ N : U(p) fails} ≪ N exp(−c(log N)^{2/3}) at primes (`EXSET_BEYOND_CRT.md` Thm 3.1;
  `EXSET_SIEVE_MASS.md` 3.5). INTERNALLY PROVED, Vaughan-type. **2/3 is sharp for the audited whole-avoider CRT
  architectures over U/ES₅ classes** (native, endpoint-pair, selector, coefficient-sum and CRT-admissible large-sieve
  evaluations, exactly-covered forcing families; not arbitrary prime-law majorants), and for native I3 classes, by the
  supply-law cap λ^{d/(d+1)} (up to log factors) with d = 2 (ES ratio classes: d = 3). Nothing beyond 3/4 (ES) or 2/3
  (U/ES₅/I3) is known, even conditionally on a standard hypothesis.
* Σ_{p≤N} f_I(p) ≪ N log²N (PROVED rel. Kuznetsov/Petersson, Weil, twisted Weil, Selberg 3/16, λ₁ > 1/4; (D)32b;
  *needs expert scrutiny*).
* m/n density transition at log N ≍ m^{1/3}: upper half Thm U (PROVED rel. BV, Shiu; ineffective), lower half Thm L′
  (PROVED rel. ET Thm 7.1, BT, Shiu, PV); sharp order CONDITIONAL on SEL_m ((D)31 follow-ups).
* Moving windows (board #2 slate, (J)105; PROVED rel. Henriot's erratum, Siegel–Walfisz, Mertens): for 0 < α < 1/6, all but
  O(X/L^{4/3−2α−ε}) primes p ≡ 1 (8) in [X, 2X] have a Type II solution at *every* forced prime window q ≡ 3 (8) in
  [L^α, 2L^α] (L = log X). Witness-location information; says nothing about hard primes.
* Almost-all caps: for A > 1, #{p ≤ X : e*(p) > (log X)^A/4} ≤ X^{2/A+o(1)} — a power saving for A > 2; and
  #{p ≤ X : e*(p) > p^ε} ≪_ε (log X)^{⌈4/ε⌉} (`CAP_BOUNDED.md` Thm 3.2; PROVED rel. Montgomery's large sieve, PNT in APs;
  (J)83). *(z51, `BREADTH_Z45.md` §16; PROVED, internal.)* Much stronger now: #{p ≤ X : e*(p) > ⌈(log log X)^{1+ε}⌉} ≪_ε X^{1−c_ε}
  (`EXSET_LINNIK_CAPS.md` Thm 4.2; Gallagher + Montgomery, untruncated growing exponent box), the same for all odd n ≡ 1 (8)
  (Thm 4.5), and X^{1/A+o(1)} at cap (log X)^A/4 for every A > 1 (Heath-Brown). These concern the cap relaxation only;
  cap 0 (ES) lacks the power-dense class supply that drives them.
* *(z53, `Z53_PZ.md` Thm A; PROVED rel. Bombieri–Vinogradov and elementary divisor sums; cross-model reviewed.)* For every
  η ∈ (0, 1), once X ≥ X₀(η) (ineffective): #{p ≤ X : R(p) < (1 − η)(log p)²/64} ≪ η^{−2} π(X)/log X. So R(p) ≫ log²p, hence f(p) ≫ log²p, for almost all
  primes — vs. ET Thm 1.8's (log p)^{0.549} on a density-1 set of primes. Truncation to trial moduli 4uC − 1 ≤ X^{1/4−o(1)}
  keeps every pair correlation inside BV. The full second moment of R is *not* proved. Average statement; says nothing
  about a prescribed p (B6). EVIDENCE (one-engine check, independent session computation, not part of the PZ memo's
  cross-review; `scripts/z53_summary_rcheck.c`, output `data/z53/summary/rcheck_1e7_1.6e8.txt`): in the four dyadic
  windows from 10⁷ to 1.6·10⁸, primes p ≡ 1 (4) with R(p) < log²p/64 number 16/302990, 10/581517, 6/1117686 and
  7/2152350; no R(p) = 0 occurred.
* *(z55, `Z55_CROSSO.md`; cross-model reviewed.)* Theorem P (PROVED, unconditional, rel. Bombieri–Vinogradov,
  Brun–Titchmarsh, Mertens):
  * Hypotheses: exponents 0 < α₀ < α₁ < β < γ with θ := α₁ + γ < 1/2, e.g. the Thm-U-admissible window
    (0.075, 0.1, 0.29, 0.39).
  * Conclusion: a proportion ≥ 2μ(1 − 2θ)/(2(1 − 2θ) + 32μ) − o(1) of the primes p ≡ 1 (4) in every dyadic
    (x/2, x], x ≥ x₀, have R_𝔉(p) ≥ 2, where μ = ¼·log(α₁/α₀)·log(γ/β). The example window gives ≈ 0.00118.
  * Theorem A (CONDITIONAL on HV): for the same fixed exponent windows and every 0 < ε < 1, all but o(x/log x) primes
    p ≡ 1 (4) in (x/2, x] satisfy R_𝔉(p) ≥ (1 − ε)M̃_x(p) ≫ log²p. Dyadic summation gives R_𝔉(p) ≫ log²p for all but
    o(π(x)) primes p ≡ 1 (4), p ≤ x. HV says
    V₈(x) = o(log³x), where V₈ is an explicit prime-free pair sum, the Haar variance of the family. The reduction is
    PROVED by the dual large sieve.
  * Theorem A′ (CONDITIONAL on HW: W_z(x) = o(log³x/(log log x)⁴), where W_z is the nonnegative pair sum at
    z = (log x)²): almost all p ≡ 1 (4) have
    R_𝔉(p) ≫ log²p/(log log p)².
  * HV and HW are open. EVIDENCE for HV exists only in fixed non-exponent windows.
  * Not pointwise (B6). Compare the certified zeros in §7 item 3.
* *(z55, `Z55_TDO.md`, `Z55_TDF.md`; PROVED; cross-model reviewed; upper bound only.)*
  * TD in mean square: Σ_{N₀<n≤N₀+N}|T_n(h)|² ≤ C(N + 16U⁴)hU(1 + log 4U²) (TDO Thm M). TDF Thm LS gives the bound
    (N + 16U⁴)(2700h⁴U + 32U log 2U). The variables are integers: U ≥ 5, h ≥ 1, N₀ ≥ 0, N ≥ 1 for TDO; U ≥ 2, h ≥ 1,
    N ≥ 1 and any signed starting integer for TDF.
  * TDO Thm A: fix 0 < η < 1/8 and 0 < c₁ ≤ c₂. For X ≥ X₀(η, c₁, c₂), all but ≪_{η,c₁,c₂} X^{1−η/4} primes
    p ∈ (X, 2X] satisfy |T_{p,U}(h)| ≤ 2U^{1−η} for every integer U in their fourth-root range and every
    1 ≤ h ≤ U^η.
  * TDF Cor 2.4: for 0 < η < 1/7 and each fixed U, TD(η) with C₀ = 1 holds at all but ≪ U^{3+7η}log U of the primes
    in that U's fourth-root range. No exceptional set uniform in U is claimed there.
  * Primality is not used. There is no new consequence for the (★) block, whose almost-all bound already follows from
    a first moment (TDO Remark 4.3).
* *(z55, `Z55_TDCAL.md` Prop A, Cor A′; PROVED; cross-model reviewed; upper bound only.)* For integers X ≥ 0, Y ≥ 1,
  U ≥ 2; the exceptional-set conclusions assume fixed 0 < η < 1 and ε > 0.
  Σ_{X<n≤X+Y}N₂(n, U) ≤ Σ_{X+2U<M≤X+Y+4U}τ(M)².
  * For X ≍ U⁴, at most O_ε(U^{η+ε}) integers in any window of U consecutive integers have N₂(n, U) > U^{1−η}.
  * #{p ≤ X : N₂(p, U_p) > U_p^{1−η}} ≪ X^{(3+η)/4+ε}, with U_p = ⌊p^{1/4}⌋.
  * So R2's conclusion holds on average with no TD-type input. Averaged TD itself is not addressed.

**5.2 Unconditional, pointwise — for relaxations or thin families, not ES.**
* The BM main term: M_BM(p) ≥ (3/(16π²) − o(1))(log p)² (Burgess) for every large prime; five-slice analogue
  ≥ (45/(32π²) − o(1))L² ((J)100, (J)105). Main terms only.
* The BM layer is pointwise free: for odd n, some t ≡ 0 (4), t ≤ 4ℓ(n), has M_t^lev(n) > 0 iff n is not a square ((J)103).
  *(z52.)* So is the genus layer: every non-square n ≡ 1 (4) has a level t = 4r at which no odd real character mod t
  obstructs (GT1, PROVED rel. Dirichlet; Linnik-size t; `Z52_BANKED.md` §1(b)). Only the class of the divisor remains.
* **Self-generated mute set** ((J)64, `CAP_POINTWISE.md`): for a prime window q = 4x − n with q ≡ 4 − n (8) and (q/n) = −1,
  reciprocity forces −1 ∈ ⟨primes of x⟩ mod q, giving 4/n = 1/x + 1/y + 1/z with z of square denominator and exponent cap
  e < q. Hence e*(n) ≪ rad(n)^5 for every odd n > 1 (PROVED, effective) and e*(n) ≤ (16 log n + 70)² for odd non-squares
  (CONDITIONAL on GRH). Improved: e*(n) ≪_ε n₀^{1/4+ε} for n ≡ 1 (8) (rel. Pollack, ineffective), e*(p) ≤ (p − 5)/8 for primes
  p ≡ 1 (8) (effective) ((J)66). ES is cap 0; cap 0 at a window is exactly the B2 event. The first genuinely pointwise
  positive mechanism of the campaign — for a relaxation.
* Provable T1-bearing cousins: ES^{(S)} (|S| ≥ 4, unconditional), ES^□ (elementary), V_φ (GRH; unconditional with a
  power-saving exceptional set), ES_(k) for every k and every n ≥ 2 ((J)108 Cor 2.5; the even-k construction itself works at odd non-squares and
  extends by scaling), M^□ for all M ≡ 0 (4) ((J)41) — see B-fin for why they don't
  transfer.
* Thin families: all 3·2^s + 1, 7·4^s + 9, 63·2^s + 1, 4^s + 105, 4^s + k (nine k) (PROVED, computer-assisted; §1). The
  II-ad u ≡ 3 (8) branch of 15·2^s + 1 is sterile for every root degree ((J)102). *(z53, `Z53_THIN15.md`, cross-model reviewed.)* ES(15·2^s + 1)
  is CERTIFIED for every s ≤ 3·10⁶ (before: s ≤ 52 in the open class 60 | s); the class 60 | s stays open for all larger s.
* Function fields: one mute place makes the ES variant over F_q[T] a theorem at every P, unconditionally and effectively
  (Bilharz/Weil; (J)30) — even where ES_q itself has no finite covering. ES over F_q[T] is a theorem in several
  small-characteristic cases ((J)4).

**5.3 Obstruction-side theorems** (useful because they bound what coverings can do).
* Sterile Mordell points exist on the r-generic line for every prime r ≥ 2^{21.44} ≈ 2.8·10⁶: no finite ET covering handles
  all primes with least QNR r (PROVED, computer-assisted; (J)70). r ≤ 13 is covered at level 1; r = 17 is open.
* Function fields: ES_q(T^k) has no finite linear covering for q = 3^r, r ≥ 2; ES_q(T) none for q = 3^r, r ≥ 2, via a Weil-
  reciprocity root-product law ((J)51, (J)56, (J)67; ET-type coverings included by (J)73). Only q = 3 (CONJECTURE 0.2) is open.
* W(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4}) for infinitely many Mordell-hard primes (`POINTWISE_OMEGA13.md`; rel. Gallagher,
  Nair–Tenenbaum, energy bound); the Haar avoider exponent and the tail exponent of W over primes are both 3.
* Infinitely many 3·2^s + 1 etc. lie outside every finite ET covering ((J)22 Cor 1.5, (J)68).
* *(z53, cross-model reviewed.)* **B1 with oracles** (`Z53_NONCRTLOGIC.md` Thms A, T). Theorems M/C of `POINTWISE_SIZE` extend to
  programs calling arbitrary finite-valued oracles of p: Frobenius classes in fixed fields, power-residue symbols, h(p) mod m,
  or any predicate. For each correct witness-producing procedure in the stated formal language, with a defined finite formal
  tree at the specified trap point, Thms A/T prove failure at every sufficiently large admissible input; infinitely many
  prime failures are CONDITIONAL on H for the augmented finite polynomial family. Arbitrary finite-valued oracles are
  allowed; Boolean/counting certificates and growing searches are not excluded. The formal odd-square principle holds for
  every primitive irreducible P with P(0) = 1 and no positive real root, by Hilbert reciprocity in ℚ(β) at explicit trap
  points (nonlinear traps only in that scope). Individual primitive reductions enumerated there: bounded use of
  CF/Pell/unit data of √p, ⌊cp^θ⌋ (rational c, θ), ord_p(a), or the factorisations of p ± 1 fails at every sufficiently
  large admissible input, and at infinitely many primes CONDITIONAL on H. This closes item E3 of `POINTWISE_SIZE` §4.2 for
  that scope. *Necessary condition (Cor T3(c), Prop S).* For a witness procedure to succeed at admissible primes of every
  trap point, it must escape a fixed finite formal menu and produce non-formal integers carrying non-residue prime factors
  (necessary, not sufficient; non-formality alone does not supply them). This is a pointwise trap/admissibility statement;
  prime infinitude is conditional on H. The least non-residue supplies a fully factored non-residue, and its bounded
  finite-tree procedures reduce value by value to the r-generic line.
* *(z53, `Z53_LATTICE.md` Thm A; PROVED; cross-model reviewed.)* For odd n ≥ 6.8·10¹⁷, no Def. 1.1 full-rank
  convex Thue scheme in (u, B, C), with its exactness/size conditions and positive-octant covering or Minkowski hypothesis,
  exists. Such a scheme would need a full-rank lattice coset, an exactness modulus and a convex body in the positive octant
  meeting Thue's conditions; efficient exactness cosets do not exist (index ≥ D^{4/3}/277), and convex bodies inside the
  exactness shell are small (vol K ≤ 15.12D²/n when D ≤ n/17). No full-rank coset imposes 4C | X+1 at all its points with
  C ≥ 1; deriving the class only at selected points is not excluded (Prop D). For degree ≤ δ encodings and odd exactness
  primes ℓ > 3δ with positive-dimensional coset image mod ℓ, Thm B pins the image to a point or forces ℓ to divide u, B, C,
  X or Y (the B4 shape); it is structural, not a general nonlinear no-go. This scopes the M1b Assessment; nonconvex, nonlinear and lower-rank schemes are not covered.
* **Forest witnesses are not polylog** (`H4_NOT_POLYLOG.md`, z49; cross-reviewed SOUND).
  * PROVED, relative to the internal OMEGA10/11 energy lemma: infinitely many primes p have no forest edge with larger
    endpoint in [4, exp((log p)^κ)], and A_min(p) > exp((log p)^κ).
  * Ranges: κ < 1/12 effective; κ < 1/6 relative to Gallagher's theorem, or under GRH.
  * Refutes FOREST_H4 Conjecture H₂, and every target that bounds both endpoints, or the covering modulus, by a polylog.
  * Prime-Haar model (`CONJECTURE_S_MODEL.md`): −log δ(H) ≥ c(log H)² is PROVED. The matching upper bound
    −log δ(H) ≤ C(log H)^{2+o(1)} is CONDITIONAL on a first-term hypothesis FT_β; unconditionally L⁶ log L stands.

**5.4 Conditional implications toward ES** (each hypothesis is ES-strength or non-standard).
* **H⁻_BM(ε, p₀) ⟹ ES(p) for all sufficiently large primes p**; ES for all n then additionally needs a finite census below
  the resulting threshold (§2.4; PROVED implication; no standard conjecture known to imply H⁻_BM).
* Conjecture X_slice (∃ c, f: cf | p + c + f, f(p + c + f)/(cf) ≡ 1 (4)) ⟹ ES(p) for all sufficiently large primes p (`CONDITIONAL_ES.md` Thm 6.1; X_slice is stated for large p and is
  ES-strength, single-slice; EVIDENCE: solves every prime < 3000 and every Mordell-hard prime < 2·10⁶).
* Caps, not ES: Hypothesis W (balanced lattice) ⟹ e*(p) ≤ (log log p)^{2+o(1)}; GRH + EQ ⟹ (log₂p)^{13/2+o(1)}; GRH + S ⟹
  (log₂p)^{9/2+o(1)} ((J)85, (J)91; EQ, S non-standard; GRH alone does not reach (log₂p)^{O(1)} this way).
* Amplification criteria ((J)86, PROVED): an exceptional family F ⊆ E with F(N) ≥ N e^{−o((log N)^{2/3})} infinitely often
  contradicts Vaughan (exponent 3/4 with the internal note); one successor in (p, p + f(p)] with f = e^{o((log p)^{2/3})}
  suffices for linear-scale branching. These are sharp "would suffice" targets for a disproof-by-propagation or a
  proof-by-contradiction; no propagation law is known.
* *(z54; cross-model reviewed.)* Class-layer hypothesis for HC: Lot_Λ(C) (∃p₀ ∀ prime p > p₀, p ≡ 1 (8),
  ∀X ≤ X_max(p) = exp(3√(C log p)): Λ(p, X) ≥ C log p ⟹ HC(p) ≤ X; ES-specific, open, B2 restated for a joint family)
  ⟹ HC(p) ≤ exp(√(8C log p) + O(1)) = p^{o(1)} for every sufficiently large prime p ≡ 1 (8) (`Z54_HCWIN.md` Thm D,
  CONDITIONAL; the needed anatomy mass is supplied unconditionally by Thm A2). Since finite HC(p) gives ES(p) (§7.2),
  Lot_Λ(C) is ES-strength.
* *(z54; not ES — kill side and upper-bound side.)* EH(1 − η₀) for some absolute, uncomputed η₀ ∈ (0, 1/10] (implied by
  the standard Elliott–Halberstam conjecture) ⟹ #{p ≤ x : p ≡ 1 (8), p + 4 and 4p + 1 have all prime factors ≡ 1 (4)}
  ≫ x/(log x)², hence ≫ x/(log x)² primes p ≤ x with HC(p) > 4, i.e. the kill K(4) (`Z54_HCKILL.md` Thm E,
  CONDITIONAL). TD(η), 0 < η ≤ 1/2 (|T(h)| ≤ C₀U^{1−η} for 1 ≤ h ≤ U^η, uniformly for primes p and U in the fourth-root
  range) ⟹ N₂(p, U) ≪ U^{1−η+ε}, hence balanced block N(U, U) ≪ p^{(1−η)/4+ε} (`Z54_BILINDIV.md` Thm T / Cor T,
  CONDITIONAL; an upper bound, silent on positivity; §7 item 1).

**5.5 Standing conjectures with evidence** (CONJECTURE; EVIDENCE ranges in brackets).
SQ: for odd n, V_I(n) ∪ V_II(n) empty (ET N-points, no coprimality) ⟺ n square [odd non-squares ≤ 10⁷] (z52 repair: with the
coprime Type I/II of §1 the statement is false at 105, 345, 561, 5985 — a transcription error here, not in O146/(J)1; `Z52_BANKED.md` §1(d)); SQ₅ (five slices; n ≠ 105) [10⁶]; SQ_± and 3SQ
(exception-free companions, (J)52, (J)53); PH (full-coset covers; all Mordell-hard primes < 10⁶ except 3529, 110881 at e ≤ 2000,
samples to 10⁸, 14 hard primes ≤ 3.7·10⁷; R290 repair); PM-II (3361 only) [10⁸]; X_win: a_min(p) ≪ log p;
U ((J)58); b = 1 line has exactly the three failures 193, 2521, 66529 (López; [10¹¹]); López's union conjecture; CONJECTURE 0.2
(F₃[T] sterile point x*_c); x** sterile (r = 13; certified through ES level 2.59·10¹⁰).

## 6. Dead ends (one line each; do not repeat without a new ingredient)

*Analytic / counting at one prime*
* GRH character-by-character on (★) → misses by p^{1−o(1)}; GRH gives M_gen ≥ (1 − o(1)) log log p only → `CONDITIONAL_ES` §3, (J)98.
* Two-sided asymptotic / |X| < M_gen (O260's H_X) → false i.o. by Linnik → `BM_CORRECTED_COUNT` Prop 3.1.
* Heegner/CM small-scale equidistribution, GLH, power-scale covering conjectures → scale constraint B3 → `CONDITIONAL_ES` §4, §7.
* Spectral/Kuznetsov/Heegner treatment of Type I at fixed p → averages over level (B6); tubes of width 1/p → (I)3, `POINTWISE_SPECTRAL.md`.
* Weil / Selberg–Hooley / bilinear fixed-modulus savings → tied modulus; need p^{1−o(1)} saving → `PARITY_AUDIT` §2.
* H-B, parity-breaking (Friedlander–Iwaniec) at fixed p → collapses into H-A → `PARITY_FIXED_P.md` (J)6, (J)87.
* Fixed-p variance / Janson / level-Poisson second-moment → critical, far tail fatter than Poisson → (J)103 §3.
* Exceptional set via the audited CRT architectures (caps 3/4 ES, 2/3 U/ES₅, native-only for I3), exactly-covered forcing,
  divisor switching or CRT-certified Janson chains → capped; constant-loss whole-shift products → θ ≤ log 2; marginal-only
  transfers → scoped blindness → `BREADTH_Z45.md` §15 (z50).
* Exact identities: no linear relation between 56 ES counts and 54 classical functions (CERTIFIED, that finite dictionary); no
  finite fixed-level Eisenstein-type identity certifies Type I/II counts (PROVED via T1) → (I)5, (J)7 Thm 9.1. Growing-level
  identities remain open ((J)10: the T1-respecting W(n) identity exists, positivity is the spin event).
* Automorphic normal form (theta quotient, weight ½, Serre–Stark) → Eisenstein-only, exact, but does not decide one integer → (J)101.
* Dirichlet series / moments / Euler-product hardness laws → averages (B6) → `BRAINSTORM/anal_*`.
* Spectral/interlacing, faithful Euler systems, single-character Siegel dichotomy, ultraproduct transfer → displayed mechanisms fail, not universal no-go theorems (Assessment) → `BREADTH_Z45.md` §§1–4 (board #4 addendum, 2026-10-19).
* (z53) Summing the hyperbola dual over conductors or frequencies at fixed p → `Z53_HYPKLOOST.md` (scoped):
  * Fejér-weighted frequency sums are window-smoothed counts; the full unweighted projection onto conductors dividing M
    is a class average. Arbitrary weighted cross-conductor sums are not covered (Thms B, C).
  * Kloosterman fractions: DFI Theorem 2 and Bettin–Chandee require, respectively, C̄ ≲ p^{1/37} and C̄ ≲ p^{1/21} for
    their displayed bounds to save (necessary conditions only, ignoring ε-losses). DFI Theorem 1 does save on skew KF
    sums, e.g. U ≍ p^{1/5}, V ≍ p^{3/5}, bounded b; no saving for the tied block count follows here (K(c)).
* (z53) λ-uniform box majorants and shift-uniform class-blind fibre majorants → floored at the trivial block bound →
  `Z53_HYPSUMPROD.md` Props B, C (other uses of the tools are not excluded).
* (z53) Square sieve toward positivity → `Z53_SQSIEVE.md` Lemma C3: under (H) and ν(a) ≤ P₀−1 on the support of
  nonnegative weights, quadratic σ-minorants have no positive diagonal main term. (H) is checked on finite strips only,
  not proved for general application weights. Signed auxiliary-sum inputs remain open.
* (z53) One prescribed class modulus (fixed-modulus multiplicative representation) → `Z53_NONCRTSMOOTH.md` Cor B1: for
  fixed η > 0 and one q = q(X) ∈ 4ℕ with q ≤ X^{1/2}, prescribed independently of p, all but o(π(X)) primes p ≤ X have no
  E(q,κ) with κ ≤ q/(log X)^{2+η}. This limits an almost-all guarantee at that q, not simultaneously over q; for fixed q
  the threshold eventually falls below 1. Aggregation over q is the remaining Type II route (Assessment), not a necessity
  for every ES proof: ES is Type I or Type II.
* (z54) Norm-only character-side inputs to the balanced-block square sieve → `Z54_BILINJAC.md` Prop M, Cor M′: used
  directly, Heath-Brown's real-character large sieve (square-class ℓ²-mass D(w)) returns ≥ √D(w) ≥ M_s(w) (the square
  mass), adding nothing to its input, and sup-norm/support/range bilinear Jacobi bounds (HB Cor 4) return ≥ (1 − 1/P₀) × the trivial bound.
  Inputs using more than these norms are not excluded.
* (z54) Balanced block via divisor/geometry tools, specified implementations only → `Z54_BILINDIV.md` Props 4.3, 5.1,
  5.3, 5.4 (see §7 item 1); joint (ν, k) cancellation, actual auxiliary-curve counts, Salberger/p-adic variants and AP
  methods with p-dependent moduli remain open.
* (z54) Exact layer R_𝔉 − G_𝔉 bounded block by block → `Z54_EXACTSUM.md` Theorem N: on a fixed window
  0 < α₀ < α₁ ≤ β < γ with 8U₁X ≤ P, U₁ > 3U₀, X ≥ 12Y, n-uniform bounds (over n ≡ 1 (24) in [P, 2P]) on the conductor blocks D_f or frequency sums W(a,q), summed by the
  triangle inequality, total ≥ P^{α₁−o(1)} (from prime f ≡ 1 (4) in (U₁/3, U₁]). Prime-sensitive, one-sided and
  grouped-block (cross-u) methods are not excluded.
* (z55) TD via one-variable exponent pairs after the θ-expansion → `Z55_TDF.md` §3.2: for every exponent pair,
  (1/2 − 2κ)/λ ≤ 1 (PROVED). The heuristic bound expression therefore gives TD only for n < U³, outside the range
  16U³ ≤ n (Assessment for the route). Joint (ν, k) methods are not covered.
* (z55) Per-frequency benchmark class for the strip count and TD (triangle inequality over ν, majorants
  ≥ c‖c(ν)‖₂) → `Z55_TDCAL.md` Prop C:
  * for nonzero nonnegative test functions φ, Φ, the nonzero-frequency benchmark is ≍ U, so every bound for the
    smoothed count minus its main term in this class is at least ≫ U (PROVED);
  * the TD top piece is bounded only by ≫ h^{1/2}U^{3/2} (via BILINDIV Prop 4.3). This uses BILINDIV's smoothed
    level-parametrized weights and 1 ≤ h ≤ U, not the sharp sum T(h);
  * not excluded: joint (ν, m) estimates below the benchmark, spectral methods on other transforms, arithmetic NC
    bounds.
* (z55) Pointwise genus-character minorants of the exact class count → `Z55_CROSSF.md` §2.4(a): no pointwise Fourier
  minorant of a class indicator with Fourier support in a proper subgroup of characters has positive mean (PROVED).
  Other positivity routes are not covered.
* (z55) Averaging the exact R_𝔉 over u, w or C at fixed p → `Z55_CROSSF.md` Lemma 1.3: every one-variable section is a
  single-integer divisor-in-progression event (PROVED identities). "No free average" is Assessment; transformed and
  dispersion forms are not excluded.
* (z55) "R_𝔉(p) ≥ 1 for all p ≥ p₀" on the standard-window Thm U family with p₀ ≤ 1.000005·10¹⁵ →
  `Z55_CROSSF.md` §3: false.
  * CERTIFIED zeros up to 1 000 005 280 000 049, e.g. 5.4 % of a 10¹³ sample;
  * (H⁻_𝔉) fails at every zero with M_𝔉 > 0; positivity of M_𝔉 was certified at all 192 469 recorded exhaustive-scan
    zeros, not asserted here for every sampled zero;
  * larger p₀ is open. Assessment: the model's expected-count crossover is ≈ 10¹²⁴.

*Algebraic / forcing*
* Congruence coverings, identity families, bounded search, seed-component (signed graph) line → B1; seed component sterile under H / Dickson → `POINTWISE_SIZE`, `FORMAL_CLOSURE.md`, STATUS "line 2: CLOSED".
* Reciprocity / Chebotarev / Rédei / higher power residues to force the class → parity only → (J)93, (J)96, (J)104.
* Non-abelian Frobenius, quartic data → inert on finite witness sets → (J)96, `MODP_RECIPROCITY.md`.
* Pigeonhole across shifts j or d → privacy of large primes → SS8 Lemma 2.3.
* Signed solutions then "reflect to positive" → no |d|- or square-class-preserving move; class-changing transfers are B2 → (J)52, (J)89 Lemma 4.1/Cor 4.2.
* Polynomial auxiliary budgets at a general prime; near-square / CF-norm / A² − pB² windows (coprime cases); p − 1 divisibility data → irreducibility / never Jacobi-forced / sterile point → (J)84 (Props 4.2–4.3).
* Class-group composition / slice-lattice walks (Astra bridge) → add reachability, never existence (3361) → (J)82.
* Fixed roots, least-non-residue roots in the forest F_n → fail i.o. under Dickson → (J)106.
* Witness windows bounding *both* forest endpoints, or the covering modulus A, by (log p)^C → false i.o., unconditionally
  (`H4_NOT_POLYLOG.md`, z49). Only one-coordinate windows (u_min, HC, the least López vertex) remain open.
* Bounded windows; balanced-lattice caps; GRH cap routes → bounded/slow cap is not ES; cap 0 is B2 → (J)83, (J)85, (J)91.
* Menu ladder from thin families to primes → positive-density rungs collapse to B1/B2 → (J)76, (J)78, (J)79.
* 2-adic / Fano pigeonhole beyond 4/p → used up (forcing only M ∈ {2,3,4}) → (J)57; no global Fano law on the 2-isogeny graph → (J)65.
* Windmills / involutions with finite affine menus → barred (CONDITIONAL) → (J)2 Thm 6.1. Finite-group actions on X by a
  fixed common finite affine menu: the fixed-point rule with K ⊆ Γ^{(2)} (ℤ/3, odd order, A₃ ⊂ S₃) and the Wielandt orbit
  rule with m ≥ 3 fail on a positive-density set of p ≡ 1 (24) **unconditionally** (generic orbits have size ≤ 2); the parity
  rules are (J)2 verbatim, barred given a BH-order lower bound; 2-power class-group data (8-, 16-rank, h mod 16) show no
  association with certificate parities to 2·10⁸ (EVIDENCE) → `Z52D_PARITY.md` Thms C, D (z52d, cross-model reviewed).
* Signed bounded-order Fourier/character inverse for window obstructions (Z3003 route) → false for B ≤ 952, all B under
  Dickson; no tested non-BM character (conductor ≤ 200) covers more than ~16 % of a prime's forced obstructions (EVIDENCE)
  → `Z52D_FOURIER.md` Thm B, §4 (z52d).
* Principal-cycle (Pell) root menu R3 ∪ U in F_p → frozen to a polynomial recipe at near-square primes; fails i.o. under H →
  `Z52D_PELLCYCLE.md` Thm 1.1 (z52d).
* Fermat / binary-form certificates p = Q(u,v) → miss infinitely many primes of every square class → (J)3.
* (z53) Witness procedures with arbitrary finite-valued oracles of p (Frobenius, power residues, h(p) mod m, bounded
  CF/Pell data) → `Z53_NONCRTLOGIC.md` Thms A, T: for each correct witness-producing procedure in the stated formal
  language, with a defined finite formal tree at the specified trap point, failure at every sufficiently large admissible
  input (PROVED); infinitely many prime failures are CONDITIONAL on H for the augmented finite polynomial family.
  Boolean/counting certificates and growing searches are not excluded.
* (z53) Joint Rédei / factor-multiset forcing → `Z53_GENUSREDEI.md`: for a fixed finite family of lines satisfying §1
  and an admissible datum Π in a fixed finite Galois field, five necessary pointwise laws are PROVED; completeness for
  complete decorated configurations with squarefree rough parts is CONDITIONAL on BHC (JRT); under BHC, bounded-level
  forcing from Π alone is exactly B1 (F), while prescribed factor decorations can additionally force events.
* (z53) Class-group roots in F_p → `Z53_FORESTCLASS.md` Cor 1.1: the bounded menus enumerated there fail infinitely often
  under Dickson (CONDITIONAL), even with unrestricted component exploration. Arbitrary bounded class-group functions,
  other p-dependent split classes and individual real-cycle prefixes are not covered.
* (z53) Identities → `Z53_WILDCARD.md` Prop 2.4: for a ℚ-irreducible binary quadratic form Q, identities
  Q(x,y) = 4CuB−u−B with nonzero C, u, B ∈ ℚ[x,y] taking positive integer values on a full-rank coset give only fixed
  congruence menus. Rational functions, thin loci and nonpolynomial choices are not covered.
* (z53) Convex lattice schemes → `Z53_LATTICE.md` Thm A: for odd n ≥ 6.8·10¹⁷, no Def. 1.1 full-rank convex Thue scheme
  in (u, B, C), with its exactness/size conditions and positive-octant covering or Minkowski hypothesis, exists.
* (z54) Quadratic-family confinement of growing HC windows → `Z54_HCKILL.md` Props F4–F6: a two-variable quadratic F
  (nondegenerate quadratic part, full-rank lattice coset) confines at most one window integer (F6); one-variable families
  p = (y² + δ)/(4a), with integers a, δ ≥ 1, admit only finitely many formal ratios (a : δ) confining all of 𝒞 ∩ [4, X], X ≥ 8 (F4, Faltings),
  and none confines a prime line q ≡ 7 (8) with q ∤ δ (F5). Higher-degree (x² + y⁴-type) constructions are not covered.
* (z54) Spin theorems / direct complete-fibre averaging on the exact class layer → `Z54_EXACTSPIN.md` Lemma 4.5,
  Cor 5.1, Prop 5.2 (scoped): fixed-modulus fibres on the (★) support have ≤ 6τ(u) points; FIMR/Koymans–Milovic
  hypotheses are not met (Assessment); the smooth Fourier majorant for the cubic layer needs better-than-square-root (W).
  Transformed sums, signed or non-Fourier methods are not excluded.
* (z55) Exact cancellation of a hit by a bounded group of genus non-hits on the exact layer → `Z55_CROSSU.md` §4.1:
  * excluded on moving windows for large p, since q_u ≥ (2/√15)√u (PROVED);
  * no one-coordinate Vieta involution exists on xyz = x + y + p (§4.3);
  * not covered: large groups, approximate cancellation, positivity maps, multi-coordinate moves.
* (z55) Full-family confinement identities for P(4,15) on known prime-value families → `Z55_P415.md` Lemmas A1, A2
  (PROVED):
  * a fully free square variable forces finitely many g;
  * a nonconstant, absolutely irreducible F + 4 (or 4F + 1) on a full-rank coset in ≥ 2 variables is not confined;
  * not covered: rank-one quadratics (Theorem Q), thin restrictions, other uses of those theorems.
* (z55) Fixed finite certificate coverings for HC, including classes containing no squares → `Z55_HCF.md` Thm 3.1,
  Cor 3.2 (PROVED):
  * no finite family of certificate congruences covers {p ≡ 1 (840), p ≡ R (ℓ)}, for prime ℓ ≥ 11 and a non-residue
    R < (ℓ − 1)/3;
  * so HC ≤ F(ℓ_p) cannot be proved by a finite family for each value of ℓ_p;
  * not excluded: growing moduli, unbounded certificate families.
* (z55) Small-modulus HC certificates → `Z55_HCO.md` Cor 2.3 (PROVED rel. Linnik): infinitely many p ≡ 1 (8) have no
  certificate with modulus μ ≤ log p/(1.02L₀) − O(1).
  * This is logarithmic only; polylogarithmic moduli are not excluded.
  * EVIDENCE: 101 of the 126 hard primes below 10¹² have a certificate with c, μ ≤ ⌊log²p⌋.

*Geometry / relaxations / transfers*
* Brauer–Manin, fibrations, descent, strong approximation → no BM obstruction; "BM only obstruction" = ES(n) → (I)7, `GEOMETRY_ES.md`.
* Finite descent–Brauer on covers with image-integrality → nonempty at every n≥2, including numerator-8 failures (PROVED, specified smooth-locus scope) → `BRAUER_TWISTS.md` (board #4 addendum, 2026-10-19).
* Fixed-q positive pivot rewriting → q=2,3 trapped despite ES (CERTIFIED); Q3 refuted; q=5 traps board-reported, not all move sets excluded → `Q3_PIVOT.md` (board #4 addendum, 2026-10-19).
* Propagation / global-positivity shapes → supplied mechanisms are restatements or divisor-gated; unrestricted norm descent, integral Y–Δ and rule Λ remain open (Assessment) → `PROPAGATION_CLOSURE.md` (board #4 addendum, 2026-10-19).
* Local + spinor ⇒ global, Siegel–Weil, ternary-form representation inputs → true at odd squares (T1) → (I)1, (I)4.
* Quaternion orders / supersingular graph / Eichler orders → dictionary only (genus layer) → (I)6, (J)33, (J)35, (J)65.
* Transport of ES^{(S)}, V_φ, ES^□ certificates into ES → no transport; ES is a finite search → (J)25, (J)28.
* Intermediate power rungs → ladder is flat → (J)108.
* Zaremba / thin orbits / CF length → needs density; reaches only λ ≍ log p log log p → (J)95.
* Amplifying one exception (transport, congruence recombination, non-congruential lifts) → isolated / T1-blocked / collapse to B2 → (J)86, (J)88.
* Cross-field net (13 fields) → no sharp transfer; pattern M1a–M5 → (J)94.
* Boards: Davenport forcing, √−2 norm shifts, clean-side norm towers, one-child lemma, W_binom, HJ grammars (trap at 193), CEGAR, Λ-damped counts, iso-modulus packets, Fermat splitting, consecutive blocks, mod-8 escape → each refuted or a restatement → `~/.pi/boards/20261018-es-routes/memo.md` §dead, `…-es-lowertail/memo.md` §dead.
* 51 brainstorm memos (logic, LLL/Janson, Markoff/Ghosh–Sarnak, tropical, p-adic, motivic, Maynard–Tao, entropy decrement, Kahn–Kalai, …) → none LIVE as an ES route (the one LIVE tag is an obstruction-side function-field result; R290 repair), promise ≤ 2/5 → `BRAINSTORM/README.md`.

## 7. Open sub-problems that are well-posed and plausibly tractable

Ordered roughly by (relevance to the lower tail) × (tractability), an Assessment. None is claimed to lead to ES.

1. **Cancellation on a height-dependent subset of the modular hyperbola.** Bound E(p) = R(p) − M(p) better than the
   elementary bound *by cancellation*, i.e. any non-trivial estimate for #{(x, y) : xy ≡ 1 (mod 4p), x ≡ y ≡ −1 (mod 4C),
   C = (xy − 1)/4p} in a range. *Why:* even a weak power saving would be the first class-aware single-integer input of this
   shape (`PARITY_AUDIT` §2–3).
   *(z52d update, `Z52D_HYPERBOLA.md`, cross-model reviewed.)* The elementary benchmark is p^{1/3+o(1)} (PROVED; ET's
   p^{2/5} is for full Type II), and the balanced block u, B ≍ p^{1/4} has N ≤ p^{1/4}. Its standard one-step
   implementations are closed (PROVED, each scoped to the stated implementation): one-step dualization at fixed conductor
   (≤ K·p^{o(1)} pairs per conductor ≥ q/K, the complete a-sum gives c_d(n)); the Erdős–Turán/Fejér route with max_h |S_h|
   (square-root input reproduces the trivial bound); Cauchy–Schwarz in the function variable (no off-diagonal). For smoothly
   weighted blocks the conductor ≤ m^{1−ε} part is a universal constant up to O(m^{−A}) at primes *and* rough odd squares
   (PROVED), so a remainder bound uniform over rough n cannot give positivity. EVIDENCE (10⁵ primes at 10¹²): block errors
   look swap-Poisson; the RESIDUE_HARDNESS factor lives in the boundary strips, not the interior. Still open: cancellation
   across conductors/frequencies, short-segment beyond-square-root bounds, the 2-cycle count of x ↦ (−p mod x), unbalanced
   blocks. It is no longer "the only lead not ruled out" — it is B2 at its self-dual scale with the standard tools closed.
   *(z53, five lanes, each cross-model reviewed; `Z53_SUMMARY.md` §1.)*
   * **Upper side moved (PROVED).** R(n) ≪_ε n^{12/37+ε} for every n (`Z53_SQSIEVE.md` Thm A, rel. Weil + third-derivative test;
     n^{21/65+ε} with Bourgain's exponent pair; n^{4/13+ε} under the exponent-pair conjecture). This builds on
     `Z53_HYPSUMPROD.md` Thm 1, R(n) ≪ n^{1/3−1/225}(log n)² for n ≥ 2, the first power saving in this campaign; external
     priority is unverified. Near the cube, a (★) triple is a point (C, k) of a thin strip where
     (4Ck − n)² − 4k is a square, and Heath-Brown's square sieve detects the tie. The bound is uniform in n and valid at
     squares. The gain lives near the cube. Proposition B2 excludes a balanced-block power saving only for the §4
     k-Poisson implementation with Q = qq′ ≤ W, triangle inequalities over frequencies and residue classes, Abel
     summation, and C-sum majorants e_ℓ(W/Q) ≥ c√(W/Q) for |ℓ| ≥ 16W²/n. Other implementations remain unexcluded. The
     missing input is a bilinear (ℓ, C) cancellation, equivalently χ_Q-twisted
     divisor sums near √m of integers in an interval of length m^{1/4}. Lower-bound use (Lemma C3): under (H) and ν(a) ≤ P₀−1 on
     the support of nonnegative weights, quadratic σ-minorants have no positive diagonal main term. (H) is checked on
     finite strips only, not proved for general application weights. Signed auxiliary-sum inputs remain open.
   * **Floors for other tools (PROVED, scoped to the stated majorants; `Z53_HYPSUMPROD.md` Props B, C).**
     * λ-uniform hyperbola box majorants (Weil, Cilleruelo–Garaev, Bourgain–Garaev, Shkredov) are ≥ c·W.
     * Shift-uniform class-blind fibre majorants are ≥ (log 2 − o(1))·U. Here the majorant is valid for every shift
       n₀ ≤ X, with V → ∞ and X/V → ∞; this is not a pointwise lower bound for the actual fibre count.
     * Other uses of these tools are not excluded.
     * Lenstra/CHN/Shiu per-fibre bounds remove only n^{o(1)}.
   * **Cross-conductor sums (`Z53_HYPKLOOST.md`; narrowed).**
     * Fejér-weighted frequency sums are window-smoothed counts; the full unweighted projection onto conductors dividing
       M is a class average (Thms B, C). Arbitrary weighted cross-conductor sums are not covered.
     * Kloosterman fractions collapse by reciprocity to a sawtooth phase (K(c)). DFI Theorem 2 and Bettin–Chandee
       require, respectively, C̄ ≲ p^{1/37} and C̄ ≲ p^{1/21} for their displayed bounds to save (necessary conditions
       only, ignoring ε-losses). DFI Theorem 1 does save on skew KF sums, e.g. U ≍ p^{1/5}, V ≍ p^{3/5}, bounded b; no
       saving for the tied block count follows here.
     * Uncertainty lemmas (PROVED): common-polynomial frequency certificates with positive mean require degree
       H ≥ q_max/2 = 8UV; pairwise conductor certificates require primitive frequencies for each pair contributing
       positive mean. These are restrictions on the specified certificate classes, not all positivity arguments.
     * Survives: positivity from the top of the spectrum using primality; negative-mean certificates; joint or
       nonlinear methods.
   * **2-cycle target R2 (PROVED reduction; R2 CONDITIONAL on uniform MIX; `Z53_HYP2CYCLE.md` Thm R).**
     * A power-saving second-order equidistribution hypothesis MIX (in (p mod u, p mod f(u))) implies R2. No method for
       MIX is known.
     * The displayed HB14/HB15 black-box auxiliary-curve bounds times a uniform per-curve bound, on a full box or full
       grid, give no power saving (Prop D). Occupancy pruning, specific-curve arguments and other implementations
       remain open.
     * T1 kills the colour layer, not the 2-cycles. So R2 is an upper-bound methods test that has no standalone ES
       implication; indirect use in a larger argument is not excluded (Assessment).
   * **Fixed-modulus multiplicative representation (`Z53_NONCRTSMOOTH.md` Thm B, Cor B1; PROVED).** For fixed η > 0 and
     one q = q(X) ∈ 4ℕ with q ≤ X^{1/2}, prescribed independently of p, all but o(π(X)) primes p ≤ X have no E(q,κ) with
     κ ≤ q/(log X)^{2+η}. This limits an almost-all guarantee at that q, not simultaneously over q; for fixed q the
     threshold eventually falls below 1. Aggregation over q is the remaining Type II route (Assessment), not a necessity
     for every ES proof: ES is Type I or Type II.
   * **Genus exact layers (`Z53_GENUSX.md` Lemma 4.1).** Lemma 4.1 rewrites the exact subfamily counts R_𝔉 and G_𝔉 as
     sums over free w of functions of (p mod w, ⌊p/w⌋). The unresolved centred layers are T_w = G_𝔉 − M_𝔉 and
     T_uw = R_𝔉 − G_𝔉 − T_u; they also subtract density terms. Assessment: these are B2-shaped gaps connected to this
     item, not a proved B2 equivalence or universal convergence theorem. Both layers remain open; separate bounds
     suffice but are not individually necessary, since they could compensate.
   * **Assessment.** No lane supplied single-prime positivity; the scoped obstructions leave undeveloped survivors,
     including those retained by WILDCARD and LIT.
   *(z54, two lanes, each with internal hostile and cross-model review; upper-bound work only, silent on positivity;
   `Z54_SUMMARY.md` §1.)*
   * **Jacobi-symbol side (`Z54_BILINJAC.md`; narrowed).** N(U, V, W) counts (★) triples with u ∈ (U, 2U], B ∈ (V, 2V],
     C ∈ (W, 2W], U ≤ V; the balanced block has U ≍ V ≍ n^{1/4}, W ≍ n^{1/2}, trivial bound N ≤ n^{1/4+o(1)}.
     * Prop M / Cor M′ (PROVED; Cor M′ relative to the statements quoted in its LIT_CHECK, for their *direct* use as inputs
       to the square sieve's (Q, a) form, the only Jacobi-symbol bilinear form present): inputs seeing the weights only
       through the square-class ℓ²-mass D(w) (Heath-Brown's real-character large sieve, Cor 2) return ≥ √D(w) ≥ M_s(w),
       adding nothing to the bound on D(w) they need; inputs depending only on sup-norm, support and range (HB Cor 4, any
       sup-norm bilinear Jacobi bound for coefficients of modulus ≤ 1) return ≥ (1 − 1/P₀) × the trivial bound. Direct
       CFS does not apply (Assessment); PV/Burgess bound only the non-square part (PROVED identity remark, not a no-go for
       weighted or completed uses). Inputs using more than these norms are not excluded.
     * After Poisson the (ℓ, C) coefficients are Kloosterman sums, not Jacobi symbols (PROVED identity (F3)).
     * Thm R (PROVED): for W ≥ 2V and (log n)² ≤ P ≤ V, uniformly in odd n ≥ n₀(ε),
       N(U, V, W) ≪_ε n^ε[V/P + P²·max|T_Q(a, b)|], the max over Q = qq′ (q ≠ q′ primes in (P, 2P]) and
       (a, b) ≢ (0, 0) mod Q, T_Q the additively twisted strip sums. So TS(δ; V^{δ/3}) (|T_Q| ≤ V^{1−δ}, fixed δ ∈ (0, 1])
       gives N ≪ n^ε V^{1−δ/3}, and |T_Q| ≪ V^{1/2+ε} for Q ≤ 4V^{1/3} gives N ≪ n^{5/24+ε} (CONDITIONAL). TS is
       sufficient; it is necessary only for twist-blind S_Q-bounds (Prop R′). Joint use of the Kloosterman structure,
       weighted Fourier estimates and averages over the moduli are not covered.
     * Assessment: square-root TS is a twisted, dyadic analogue of Jutila's conjecture Δ(x+h) − Δ(x) ≪ x^ε√h at
       h = x^{1/4} (no implication either way is proved). The checked literature (search-limited) gives no power-saving
       pointwise bound even for the untwisted strip count. Exponent-pair majorants on the C-sums give V^{κ+2λ} ≥ V
       (PROVED as a computation of that bound expression only).
     * CERTIFIED: N_bal(n) := #{(★) triples with n^{1/4}/2 < u, B ≤ 2n^{1/4}} ≤ 20 for every odd n ≤ 10⁹ (maximum at
       n = 635 674 641; 14 over primes p ≡ 1 (24)). EVIDENCE: sampled S_Q and T₆₁ sums at 10¹⁰–10¹⁴, and
       nonzero-ℓ Poisson shells at 10¹⁰ and 10¹², are consistent with square-root cancellation. The ℓ = 0 shell is a
       main term; the additive experiments do not test the composite moduli of TS.
   * **Divisor/geometry side (`Z54_BILINDIV.md`; narrowed, one new sufficient condition).** p an odd prime, U ≥ 2 an integer,
     16U³ ≤ p; throughout this bullet assume c₁p^{1/4} ≤ U ≤ c₂p^{1/4}, with fixed 0 < c₁ ≤ c₂ and sufficiently large U;
     N₂(p, U) := #{{u, B} ⊂ (U, 2U], u ≠ B : uB | p + u + B} (2-cycles; the balanced (★) block is N(U, U) = 2N₄,
     N₄ ≤ N₂ the sub-count with 4 | (p + u + B)/(uB)); E1⁺ := lattice points (k, m) with p + 2U < km ≤ p + 4U,
     U² < m ≤ 4U², D := (km − p)² − 4m ≥ 1; T(h) := Σ_{E1⁺} e(h√D).
     * Theorem T (PROVED): for every ε > 0, A ≥ 2 and 0 < δ ≤ 1/2, with H = U^ε/δ,
       N₂ ≤ 4δ|E1⁺| + 8δΣ_{1≤h≤H}|T(h)| + C(ψ, ε, A)|E1⁺|U^{−εA}; and |E1⁺| ≪_ε U^{1+ε}.
     * Corollary T (CONDITIONAL on TD(η), 0 < η ≤ 1/2: |T(h)| ≤ C₀U^{1−η} for 1 ≤ h ≤ U^η, uniformly for primes p and U in
       the fourth-root range c₁p^{1/4} ≤ U ≤ c₂p^{1/4}): N₄ ≤ N₂ ≪ U^{1−η+ε}, hence N(U, U) ≪ p^{(1−η)/4+ε}. Pairs with
       B − u ≤ U^{1−η} number ≪ U^{1−η+ε} (Remark 4.1, PROVED), so TD is needed only where √D ≥ U^{1−η}.
     * TD is first order (one remainder phase per level); z53's MIX is second order; neither is shown to imply the other.
       EVIDENCE: max_h|T(h)|/√|E1⁺| ≤ 3.2 at 10¹²–10¹⁸ (h ≤ 20, extended runs to h ≤ 178), at primes, odd squares and
       near-squares.
     * Scoped closures, each for the specified implementation only:
       * Prop 4.3 (PROVED): for the smoothed top-range sub-sum T_φ (not T itself), implementations that expand in the
         remainder phase, use the triangle inequality over the frequency ν, and bound each k-sum with |ν| ≥ hU no better
         than square root (an assumption defining the class) give Σ_{|ν|≥hU} b_ν ≫ h^{1/2}U^{3/2} (fourth-root range,
         1 ≤ h ≤ U). The reverse order is the uncancelled count ≤ |E1| ≪ U^{1+ε}; its size ≍ U is EVIDENCE only.
       * Prop 5.1(a) (PROVED): the untied divisor-in-AP form has modulus q = p at the endpoint q ≍ x^{2/3}, where direct
         insertion of the classical asymptotic fails by p^ε; a fixed-Q relaxation (Q fixed independently of p) has
         CRT-model main term ≍ U² (Prop 5.1(b), Assessment).
       * Prop 5.3 (PROVED): each one-sided divisibility (anatomy) filter keeps ≫ U^{1−ε} values of u.
       * Prop 5.4 (PROVED relative to HB15 as restated): any black-box HB15 bound (auxiliary-surface count × per-curve
         bound ≥ 1), with any occupancy pruning, is ≥ 1/5 of Σ(min side + 1) on the same boxes, i.e. of "≤ 1 solution
         per u". Counting the actual auxiliary curves, Salberger's global method and p-adic variants are not covered.
       * Prop 5.5 (PROVED): for sufficiently small c = c(c₂) > 0 and sufficiently large U, E1 points with k in
         any window of length ⌊cU^{2/3}⌋ are collinear; a line of primitive direction
         (a, −b), a, b ≥ 1, carries ≤ 2√(2U/(ab)) + 2 of them. EVIDENCE: lines with ≥ 3 points carry 2.5–9.7 % of E1,
         with no detected enrichment of tie events.
     * Missing (Assessment): a joint (ν, k) cancellation (the additive analogue of the bilinear (ℓ, C) estimate), or
       TD/MIX themselves.
   * **Convergence note (Assessment).** Both gap-1 lanes end at a joint/bilinear cancellation (TS, TD or MIX) that no lane
     supplied; these are sufficient conditions, none shown necessary. The z54 exact-layer lanes (item 3) end at cross-u
     cancellation within a dyadic slice, among ≍ U distinct integers p + u with moving moduli 4u: B2 in tied form,
     connected to this item. As for z53, this is not a proved B2 equivalence; `Z54_EXACTSUM.md` Theorem N excludes only
     n-uniform block-by-block bounds.
   *(z55, three lanes, each with internal hostile and cross-model review; upper-bound work only, silent on positivity;
   `Z55_SUMMARY.md` §1.)*
   * **Tryhard TD (`Z55_TDO.md`, `Z55_TDF.md`): TD(η) NOT proved for any η > 0.**
     * Only averaged forms are proved (§5.1): TDO Thm M and TDF Thm LS (mean square over n); TDO Thm A (almost all
       primes, all U at once, η < 1/8); TDF Cor 2.4 (each fixed U, η < 1/7).
     * No primality is used. They give nothing new for N₂, where a first moment suffices.
   * **Pointwise constant factors (PROVED; not power savings; trivial bound U/2).**
     * TDF Prop 2.6: N₄ ≤ N₂ ≤ (log 2/2)U + O_{c₁,c₂}(U^{14/15}).
     * TDCAL Remark A‴ (PROVED rel. Titchmarsh Thm 5.13): N₂ ≤ (1 − log 2)U + O(U^{1−3/56+ε}) ≈ 0.307U.
   * **Weaker sufficient conditions (PROVED implications; both conditions open).**
     * TDF §3.3: TD(η) ⟹ DC_ε(U^{−η}) ⟹ N₂ ≪_ε U^{1−η+ε}. Here DC_ε(t₀) says
       #{k ∈ E1⁺ : w_k mod 1 ∈ I} ≪_ε U^{1+ε}|I| for all intervals with |I| ≥ t₀.
     * TD ⟹ DC without the U^ε is not claimed, since the zero mode |E1⁺| is known only to be ≪ U^{1+ε}. The 2-cycle
       levels are a subset of the square-discriminant levels, not all of them.
     * TDCAL Prop D: TD(η) ⟹ NC(η) ⟹ N₂ ≪ U^{1−η+ε}. Here NC(η) says 𝒜(U^{−η}) ≪_ε U^{1−η+ε}, with
       𝒜(δ) = #{k ∈ E1⁺ : ‖w_k‖ ≤ δ}. This one-sided near-integer count is what Thm T's Fourier route actually
       delivers.
     * A sharp-order τ-perturbed tie bound over |τ| ≤ 13U^{1−η} is a stronger sufficient condition for NC; no converse
       is established. The displayed elementary τ-window estimate U^{1+ε} + TU^{1/2+ε} does not reach it.
     * A Fejér pair-correlation bound is one sufficient ℓ² input (Assessment: second order, like MIX).
   * **Calibration (`Z55_TDCAL.md`; narrowed).**
     * Lemma S(a) (PROVED): |E1| is exactly the part of D(p + 2U, 2U) = Σ_{p+2U<M≤p+4U}τ(M) with divisor in
       (U², 4U²]. That is a central slice (divisors ≍ √x) of the short-interval divisor problem at length ≍ x^{1/4}.
     * Assessment (search-limited): no checked source gives a power-saving pointwise asymptotic for this slice.
       Li–Yang's Δ(x) ≪ x^{0.31448…+ε} reaches only lengths ≥ x^{0.31448…+ε}.
     * Lemma S(c) (PROVED): every strip point has m | p² − D. The contribution to T(h) from w ≤ U^{(1−η)/2} is
       O_ε(U^{1−η+ε}) for every integer h ≥ 1; this is not sharp TD(η) for the full sum.
     * Thm B (PROVED): fix the smooth test functions of TDCAL §6, 0 < σ ≤ 1, 0 < ε < 1 and A > 0; take sufficiently
       large U and integer 1 ≤ h ≤ U. Then the natural smooth expansions in θ_m = {−p/m} carry, up to O(U^{−A}),
       * for smoothed CNT and TS_{N₂}: only |ν| ≤ U^{1+ε};
       * for a smoothed TD piece at w ≍ W ∈ [U^σ, 4U]: only ν ∈ [hU³/(2W), 64hU³/W].
     * These bands are disjoint for these particular expansions but depend on the representation (Remark B2). No
       implication between TD and short-interval divisor statements is established either way.
     * Prop C (PROVED; one row Assessment): the benchmark class is "triangle inequality over ν with majorants
       ≥ c‖c(ν)‖₂". In it, for nonzero nonnegative test functions φ, Φ, the nonzero-frequency benchmark is ≍ U, so
       every bound for the smoothed count minus its main term in this class is at least ≫ U. The targets need further
       factors:
       * U^η for CNT(η);
       * U^{1/2} for the central-slice square root;
       * h^{1/2}U^{1/2+η} for the TD(η) top piece (via BILINDIV Prop 4.3). This uses BILINDIV's smoothed
         level-parametrized weights and 1 ≤ h ≤ U, not the sharp sum T(h);
       * the piece-W row is Assessment.
     * Prop E (PROVED identity): the direct completion of m | p + s exhibits no Kloosterman sum. No spectral-method
       exclusion is made.
   * **EVIDENCE.**
     * At 10¹⁰, T(h)/√|E1⁺| is compatible with the unit complex-Gaussian model (TDCAL §10): 96 000 generic (p, h),
       structured prime families, odd squares.
     * In four samples of 200 consecutive primes near 10⁸, 10¹⁰, 10¹² and 10¹⁴, with h = 1,…,8, the mean of
       |T(h)|²/U is 1.45–1.53 (TDO Table 5.1; EVIDENCE, not a pointwise bound).
   * **Assessment.**
     * Pointwise TD sits at a self-dual point (TDO §6, TDF §3.1).
     * In TDF §3.2's specific heuristic θ-expansion bound expression, a one-variable exponent-pair estimate would give
       TD only for n < U³; joint-variable methods are not excluded.
     * Missing: a joint (ν, m) estimate below the per-frequency benchmark, or an arithmetic proof of NC or DC_ε at
       one p.
2. **Growing roots in the forest F_p** (edge uv ⇔ uv | p + u + v). Fixed roots and the least-non-residue root fail i.o. under
   Dickson, and the component of 1 can be as small as 8 vertices i.o. (CONDITIONAL on Dickson, `LOWER_TAIL_ASTRA.md` Thms 3.1,
   5.1) — so Fable's spark "|comp(1)| ≫ (log p)² unconditionally" is false under Dickson and the growth claim behind it was
   retracted (`LOWER_TAIL_FABLE.md` §2, R286 repair D5). Open: can p-dependent growing root sets force a bichromatic edge
   (Astra's open questions)? *(z52d, `Z52D_PELLCYCLE.md`, cross-model reviewed:)* the principal-cycle root menu R3 ∪ U of √p
   and (1+√p)/2 (all P_k, Q_k, a_k, convergents ≤ p + 2, unit coordinates) cannot: under H there are infinitely many
   p = m² + 1 ≡ 1 (24) where every component meeting it is monochromatic, even with unrestricted forest exploration (Thm 1.1,
   CONDITIONAL on H); unconditionally, at every prime m² + 1 with 60 | m the cycle roots other than 1, 2, 4 are isolated
   (Prop 1.6). Arbitrary functions of cycle data, and cycle data used as other coordinates, are not covered. An almost-all size bound for comp(1) is a different, open question.
   *Why:* the forest is the cleanest combinatorial form of ES₅.
   *(z49 update.)*
   * Certificate ⟺ bichromatic is proved three times. The coordinate form is also proved: some coordinate of some word
     lies in 4ℤ ∪ (8ℤ − p) (`LOWERTAIL_ROUND2_FABLE.md` Thm 1).
   * The polylog form of the attachment gap is **false** i.o. (`H4_NOT_POLYLOG.md`). Any forest proof must reach
     witnesses whose larger endpoint exceeds exp((log p)^κ).
   * The open target is one-coordinate: HC(p) ≪ (log p)^A, with HC(p) ≤ 64 CERTIFIED to 10⁸ and Landau-type.
   * Inverse-problem and global-identity searches were negative (`FOREST_INVERSE.md`).
   *(z53 update, five lanes, cross-model reviewed.)*
   * **Fixed-family certification wall (`Z53_HCSHIFTS.md` Thm W; PROVED).**
     * For each fixed polynomial family satisfying W's prime-valued factorisation hypotheses throughout a fixed window X,
       p is constant modulo every odd prime ℓ ≤ ⌊X/4⌋+1. Every member except possibly the least satisfies
       log p > (1/4+o(1))X. This bounds the certified window, not actual HC(p); a sequence of families contributing
       their least members and other certification mechanisms are not excluded.
     * Under a non-standard uniform Bateman–Horn bound, the reach is HC > c log p/log log p i.o. (CONDITIONAL).
     * Smooth-part certificates (Prop W3, PROVED relative to Linnik): at infinitely many primes there is a window
       X ≥ (1/10.4−o(1))log p in which every certificate with coordinate x ∈ 𝒞, x ≤ X splits the (X+1)-rough part
       nontrivially. No exclusion at larger polylogarithmic coordinates follows.
   * **Model-based recalibration (Assessment).** HCSHIFTS's occupancy model (`Z53_HCSHIFTS.md` §3.2, fitted to data at
     10⁹–10¹³), with independent draws across primes for the infinitely-often conclusion, predicts HC > C log p
     infinitely often and eventual HC ≤ (log p)^A for A ≥ 2 log 2. HCHYP's distinct uniform-residue model
     (`Z53_HCHYP.md` Thm M) proves failure below 2 log 2 and eventual success above it; equality is undecided there. Its
     Cor M3 is a non-implication in the model's line-data space, not an arithmetic non-implication or refutation of
     Conjecture 3.4 (HC ≪ log p). Model-motivated target: HC(p) ≤ (log p)^A with A > 2 log 2 ≈ 1.386; equality is also
     consistent with HCSHIFTS's occupancy model, but undecided in HCHYP.
   * **No standard conjecture is shown to imply the target (`Z53_HCHYP.md`; narrowed).** HCHYP gives a hypothesis catalogue,
     not a non-implication theorem. The sufficient hypotheses identified here are ES-specific far-lower-tail assumptions
     (LT, H⁻_BM type); no exhaustive non-implication theorem is claimed.
   * **Exceptional set (`Z53_UPPER.md` T4.1–T4.3; PROVED rel. BV/Siegel–Walfisz).**
     * For fixed 0 < θ ≤ 1/2 and x ≥ x₀(θ), #{p ≤ x prime : p ≡ 1 (4), HC(p) > x^θ+1} ≤ 16x exp(−0.15√(θ log x)); x₀ is
       ineffective.
     * For fixed A > 0 and 0 < ε < 1, #{p ≤ x prime : p ≡ 1 (4), HC(p) > (log x)^A} ≪_{A,ε} x exp(−(1−ε)A(log log x)²),
       with ineffective constants.
     * Correct, but not an advance on existing exceptional-set rates (cross-model review).
     * For fixed 0 < θ < 1, pointwise HC(p) ≪ p^θ is open and would imply ES for sufficiently large primes. UPPER §5.4
       heuristically estimates ≍ log X·log p certificate pairs up to coordinate X, hence ≍ θ log²p at X = p^θ; this
       supplies no pointwise lower bound.
   * **Class-group roots (`Z53_FORESTCLASS.md`).**
     * The bounded menus enumerated in Cor 1.1 fail infinitely often under Dickson (CONDITIONAL), even with unrestricted
       component exploration. Arbitrary bounded class-group functions, other p-dependent split classes and individual
       real-cycle prefixes are not covered.
     * The full reduced-form minimum set of discriminant −4p cannot be enumerated by a fixed finite list of
       polynomial-valued roots (Prop 2, PROVED relative to Siegel). No corresponding cardinality/escape result is
       established for truncated SM, SMN or SP, positive discriminants, or polynomially indexed growing enumerations.
     * Lemma G (PROVED): for a ∈ SM, a ≥ 3, the target genus coset contains at least τ(p+a)/[G:G²] divisors. This
       removes the genus obstruction, not the exact-class obstruction; arbitrary SP roots are not covered.
     * EVIDENCE: the measured SM advantage is consistent with a genus explanation; genus-conditioned MH point estimates
       are 0.930–1.081, without an established confidence interval or detection threshold.
     * CERTIFIED for primes p ≡ 1 (8), p ≤ 10⁸: SP has no failures; SM fails only at 19441. SP/SM are the filters
       a ≤ ⌊√p⌋+1 with p/−p square mod a, respectively; failure means no root reaches a bichromatic component.
   *(z54, three lanes, each with internal hostile and cross-model review; `Z54_SUMMARY.md` §3.)*
   * **Kill side (`Z54_HCKILL.md`; strengthened conditionally, narrowed).** S := {n ≥ 1 : all prime factors ≡ 1 (4)};
     K(X): infinitely many primes p ≡ 1 (8) with HC(p) > X.
     * Lemma 1.1 (PROVED): for prime p, [p ≡ 1 (8) and HC(p) > 4] ⟺ [p ≡ 1 (8), p + 4 ∈ S, 4p + 1 ∈ S]. So
       K(4) = K(5) = K(6) = P(4,15), and every K(X), X ≥ 4, implies P(4,15). Lemma 1.2 (PROVED): among x ∈ 𝒞 exactly the
       lines x | 24 (4, 8, 12, 24) are pure subgroup conditions. Remark 1.3 (PROVED identity): P(4,15) is an S-refined
       det-15 analogue of Friedlander–Iwaniec's hyperbolic prime number theorem.
     * Theorem Q (PROVED): every prime p = 5m² + 1 with 4 | m has 12 | m and HC(p) ≥ 7; hence K(4) is CONDITIONAL on
       Bunyakovsky for the single polynomial 720k² + 1. CERTIFIED: all 5 719 such primes ≤ 10¹² have HC(p) ≥ 7.
     * Theorem E (CONDITIONAL on EH(1 − η₀), some absolute uncomputed η₀ ∈ (0, 1/10]; implied by standard EH):
       #{p ≤ x : p ≡ 1 (8), p + 4 ∈ S, 4p + 1 ∈ S} ≫ x/(log x)² (x ≥ x₀), the order of the unconditional upper bound (`LOWERTAIL_ROUND2_FABLE.md` Thm 3.2). An
       independent adaptation of the Friedlander–Iwaniec 2009 template, not a citation. With BV the same implementation
       proves only Prop A (PROVED rel. BV): for fixed 0 < ζ < 1/4, ≫_ζ x/(log x)² primes p ≡ 1 (8) with (p + 4)(4p + 1)
       free of prime factors ≡ 3 (4) below x^ζ. Assessment: in this implementation the gap is a level deficit (θ₀ vs 1/2)
       or a parity-type switched count; unconditional K(4) is open (no unconditional source located, coverage-limited).
     * Quadratic confinement (PROVED unless labelled): a two-variable quadratic F (nondegenerate quadratic part) confines at
       most one of the window integers λ_iF + μ_i on a full-rank lattice coset (Prop F6; quadratic F only). One-variable
       families p = (y² + δ)/(4a), with integers a, δ ≥ 1: line 4's formal square-class conditions form a rational conic (Prop F2; Theorem Q is one
       integral point); lines {4, 7} give the elliptic curve E₇ of conductor 735 and rank 1 (Prop F3; rank CERTIFIED by
       PARI bounds [1, 1]; none of 17 sampled ratios gives an integral family, EVIDENCE); lines {4, 7, 8} give genus-17
       curves, so only finitely many formal ratios (a : δ) confine all of 𝒞 ∩ [4, X], X ≥ 8 (Prop F4, Faltings). A family
       confining a prime line q ≡ 7 (8) has q | δ (Prop F5), so no fixed such family confines an unbounded window.
       Existence of any admissible family beyond X = 4 is undetermined.
     * K(7) (Assessment, scoped to the direct confinement-sieve implementation): four half-dimensional conditions give
       dimension 2 and s = 2 < β₂ ≈ 4.27, so no lower bound even at level 1. For fixed X ≥ 7 Dickson remains the recorded
       route.
     * CERTIFIED exact counts of primes p ≡ 1 (8) with HC(p) > 4 to 10¹¹ (65 618 311 at 10¹¹); EVIDENCE: their ratio to the
       half-dimensional prediction rises 0.81 → 0.966 from 10⁵ to 10¹¹ (the asymptotic is CONJECTURE).
   * **Upper side, three layers (`Z54_HCWIN.md`; narrowed, one conditional strengthening).** For p ≡ 1 (8):
     Λ(p, X) := Σ_{lines at x ∈ 𝒞, x ≤ X} min(1, τ(N)/φ(x)) (anatomy mass); Γ(p, X) the genus mass, Γ = 0 on every line at
     odd squares (Lemma 1.1(d), PROVED).
     * Theorem B (PROVED rel. Henriot's uniform Nair–Tenenbaum bound and BV): with X = (log T)^θ, κ = θ/log 2, the sum of
       Λ(p, X) over primes p ≡ 1 (8) in (T, 2T] is ≤ π*(T)(log T)^{g(κ)+o(1)} = o(π*(T) log T) for 1 < κ < 2 (upper bound
       only; g(κ) = κ log 2 − κ log κ + κ − 1), and ≥ c(θ)π*(T) log T log log T for κ > 2. So 2 log 2 separates two proved
       regimes of an average (B6); the boundary is undecided.
     * Theorem A (PROVED): Turán–Kubilius over the window variable sees only primes ≤ X^{1/2} (A1: for prime p, 8 < X < p and
       3 ≤ z ≤ X^{1/2},
       |ω_z(N_x) − μ_z| > t√(1 + log log z) for only O(|𝒳|/t²) x ≤ X); and Λ_E(p, X) ≥ (1/8)log²X − O(log X) for every odd
       p and 6 ≤ X < p (A2, outer layer; holds at squares). Pointwise Anat at polylogarithmic X: no known approach
       (Assessment).
     * Theorem C (PROVED in the HCHYP model 𝔐 only): for each fixed K ≥ 1 and each fixed
       deterministic function K(p) ≥ 1 with K(p) → ∞, the conjunction [for all large p
       some line is K-big, 2^k ≥ Kφ(x)] ∧ [for all large p every K-big line succeeds] has 𝔐-probability 0, at every
       window. That a model-compatible class hypothesis must be joint is Assessment. Prop M′ (𝔐 only):
       HC(p) ≤ (log p)^{2 log 2} eventually, 𝔐-a.s. (HCHYP's boundary case, in the model).
     * For C > 0 and X_max(p) ≤ exp((log p)^{3/4}), Lot_Λ(C): ∃p₀ ∀ prime p > p₀, p ≡ 1 (8), ∀X ≤ X_max(p): Λ(p, X) ≥ C log p ⟹ HC(p) ≤ X; Lot_Γ(C) the same with Γ.
       Prop L (𝔐 only): Lot_Γ(C) a.s. for C > 2, Lot_Λ(C) for C > 4. Theorem S (PROVED implication): Anat(A, C) ∧ Lot(C)
       (same mass, X_max ≥ (log p)^A) ⟹ HC(p) ≤ (log p)^A for all large p ≡ 1 (8); a sufficient route only, S_A does not
       imply Anat.
     * Theorem D (CONDITIONAL on Lot_Λ(C) with X_max(p) = exp(3√(C log p))): every sufficiently large prime p ≡ 1 (8) has
       HC(p) ≤ exp(√(8C log p) + O(1)) = p^{o(1)}. Lot is ES-specific, open and B2 restated for a joint family, not a
       mechanism (§5.4).
     * EVIDENCE: in the samples at 10⁹, 10¹¹, 10¹³ and 4·10¹⁵, pooled over x ∈ [64, 1024), observed success rates in
       genus-mass bins m ≥ ½ lie within about four percentage points of the bin-averaged laws 1 − e^{−m} (endpoint) or
       1 − e^{−m/2} (level); small-m rates fall short. This is not a calibrated conditional probability. In the
       consecutive-prime samples of 50 000 primes each from 10¹¹ and 10¹³ and 20 000 from 4·10¹⁵, every failure occurs at
       Γ = 0. The separate 10¹² scan has class failures, including 25 at X = 16. Finite data cannot test the eventual Lot.
   * **Unprimed attempt (`Z54_UPPER2.md`; target HC(p) ≤ (log p)³ not proved, not refuted).** Mostly an independent
     reproof of `Z53_UPPER.md` / `LOWERTAIL_ROUND2_FABLE.md` results, its sieve theorems weaker than Z53's (its §0.1).
     * Prop 3.1 (PROVED; Mordell's classes are classical): HC(p) ≤ 8 for every prime p ≡ 1 (8), p > 7, outside the six
       classes 1, 121, 169, 289, 361, 529 (mod 840), via six explicit words.
     * New: CERTIFIED HC(p) ≤ 64 and HC(p) ≤ (log p)³ for all primes 5 ≤ p ≤ 10⁹, p ≡ 1 (4) (max 64 at p = 21 841 only).
       EVIDENCE: HC(p) ≤ (log p)³ in five samples of 10⁵ consecutive primes p ≡ 1 (4) starting at 10¹⁰, 10¹², …, 10¹⁸.
     * Prop 6.3(a) (PROVED; already `Z53_UPPER.md` Cor 3.2) excludes covering by finitely many fixed-level tests only;
       growing-level congruence arguments and prime-sensitive sieves are not excluded.
   *(z55, three lanes, each with internal hostile and cross-model review; `Z55_SUMMARY.md` §3.)*
   * **Kill side (`Z55_P415.md`; narrowed, one unconditional strengthening, not P(4,15)).** 𝒬 := the primes ≡ 3 (4);
     Ω_𝒬 counts 𝒬-factors with multiplicity.
     * Theorem U (PROVED; not GENUSLVAL's Thm U):
       * Inputs: BV; Nath–Xie's vector-sieve Prop 3.10, with FI *Opera de Cribro* Thm 11.12 as quoted there; a
         κ-dimensional upper-bound sieve; Shiu.
       * Statement: there are absolute, unspecified δ ∈ (0, 1/100] and c > 0 with
         #{p ≤ x : p ≡ 1 (8), p + 4 ∈ S, 4p + 1 has no prime factor ≡ 3 (4) below x^δ} ≥ c·x/(log x)² for x ≥ x₀.
       * Hence Ω_𝒬(4p + 1) < 1/δ + 1 (and even) for these p. The same holds with the shifts exchanged.
       * K(4) = P(4,15) needs Ω_𝒬(4p + 1) = 0.
       * Unaudited Assessment: the unweighted model suggests δ ≈ 0.031; a separate Richert-weighted model, using
         δ = 0.008, suggests Ω_𝒬(4p + 1) ≤ 10. Neither is proved.
     * Level ledger (Assessment; model numerics; sufficient levels found, not barriers, not audited):
       * the product linear sieve with switching (HCKILL Thm E route) needs ≈ 0.996 under ordinary EH with BV
         switching, and ≈ 0.976 only with an additional GEH-type switched input;
       * the vector sieve with switching needs ≈ 1.22, which is above 1 and unusable;
       * known levels fall far short: BV 1/2; Lichtman 66/107, for fixed residues and well-factorable weights only;
       * suggested routes (not a necessity theorem): EH-strength level in CRT-varying classes, or Type II input for the
         det-15 shell.
     * Lemmas A1, A2 (PROVED):
       * A1: if p = cA² + g, with A over a full residue class, confines both shifts, then c(g + 4) and c(4g + 1) are
         squares, so g takes finitely many values.
       * A2 (Lang–Weil): on a full-rank coset in k ≥ 2 variables, a nonconstant F + 4 (resp. 4F + 1) that is absolutely
         irreducible is not confined.
       * So full-family identity constructions on the following cannot confine both shifts: a² + b⁴, a² + p⁴, x² + y²
         (y prime), x³ + 2y³, binary cubics, power-basis incomplete norm forms, nondegenerate quadratics.
       * Not covered: rank-one quadratics (Theorem Q), thin restrictions, other uses of these theorems.
     * Prop C (PROVED by citation, Lemke Oliver 2012 Thm 1): infinitely many P₂ values n = 720k² + 1 have n ≡ 1 (8),
       n + 4 ∈ S and 4n + 1 ∈ S. No ES content: the difficulty of K(4) is primality.
     * CERTIFIED (cross-model rerun exact): among the 22 280 854 primes p ≡ 1 (8), p ≤ 10¹⁰, with p + 4 ∈ S,
       Ω_𝒬(4p + 1) = 0, 2, 4, 6, 8, 10 for 7 962 940, 12 902 238, 1 378 173, 37 005, 496 and 2 of them.
   * **Tryhard HC (`Z55_HCO.md`, `Z55_HCF.md`): HC(p) ≤ (log p)^A for every large prime p ≡ 1 (4) NOT proved.** The
     target is ES-sufficient and coordinate-constrained; ES is not known to imply it.
     * CERTIFIED (HCO C3.1): HC(p) ≤ 64 for every prime p ≡ 1 (4), p < 10¹² (18 803 924 340 primes).
       * The value 64 occurs only at p = 21 841. The maximum on [10⁸, 10¹²) is 60, at p = 818 789 590 249.
       * Cross-review audit: fresh rerun below 10⁸, π(10¹²) check, independent verification (certificate and
         minimality) of all 126 records with HC ≥ 44. The full 10¹² run was not repeated.
       * HCF separately reran the z53 program to 2·10⁹.
     * HCO (PROVED):
       * Lemma 2.1: if (k/p) = −1, then p + 4k has an odd number (with multiplicity) of prime factors ℓ with
         (ℓ/p) = −1.
       * Prop 2.2: each certificate lies in a fixed-divisor or fixed-cofactor congruence family, with μ = min(d, ce) on
         U and μ = min(d, e) on T, e = N/d. For odd c, also impose p′ ≡ −c (mod 8); the full condition is then a class
         modulo lcm(μ, 8), not μ alone.
       * Cor 2.3 (given Linnik): infinitely many p ≡ 1 (8) have no certificate with μ ≤ log p/(1.02L₀) − O(1). This is
         logarithmic only; polylogarithmic moduli are not excluded.
     * EVIDENCE (HCO E4.1): for the 126 primes p < 10¹² with HC ≥ 44, the least modulus at c = HC(p) lies in
       [p^{0.138}, p^{0.636}].
       * Over the window c, μ ≤ ⌊log²p⌋, however, 101 of the 126 have a small-modulus certificate (cross-model
         review).
       * It is open whether a proof needs a polylog-modulus covering or control of mid-size divisors.
       * E4.3 (EVIDENCE): among primes p ≡ 1 (8), P(HC > 4) is 0.087 on [0, 10⁸) and 0.056 on [9.52·10¹¹, 10¹²). The
         cumulative maximum stays 64; the maximum above 10⁸ is 60, and the final window's maximum is 47.
     * HCF Theorem 3.1 (PROVED; elementary plus Dirichlet):
       * Inputs: a nonempty finite set S of primes ≥ 11, an integer 1 ≤ R < (min S − 1)/3, and arbitrary C ≥ 3, Y ≥ 2.
       * Conclusion: infinitely many primes p ≡ 1 (8) with p ≡ R (mod ℓ^{J_ℓ}) for ℓ ∈ S, and p ≡ 1 (mod ℓ′^{a(ℓ′)})
         for the other primes ℓ′ ≤ Y, have no certificate (c, d) with c ≤ C and d supported on S ∪ {primes ≤ Y}.
       * Cor 3.2: no finite family of certificate congruences covers {p ≡ 1 (840), p ≡ R (ℓ)}, for prime ℓ ≥ 11 and a
         non-residue R < (ℓ − 1)/3. Such a class contains no squares. Cor 3.3 is the profinite form.
       * Prop 3.4 (rel. Linnik): for every A ≥ 0, infinitely many p ≡ 1 (8) are non-residues mod every prime ℓ ≡ ±3 (8) in
         [11, κ′_A log p], and all their certificates with c ≤ κ_A(log p)^A have a prime factor > κ′_A log p.
       * Consequence: HC(p) ≤ F(ℓ_p), with ℓ_p the least non-residue prime, cannot be proved by a finite certificate
         family for each value of ℓ_p. Already ℓ_p = 11, p ≡ 2 (11) is uncoverable. So the GRH route cannot be
         completed by fixed coverings.
       * HC ≤ F(ℓ_p) itself is not refuted. Growing moduli and unbounded certificate families are not excluded.
       * For covering-type arguments, the odd-square test is necessary but not sufficient (Assessment).
     * HCF (PROVED):
       * L2.1: for prime p ≡ 1 (8), p > 15, and c ∈ {7, 15}, c is a word coordinate iff the odd part of p + c or
         cp + 1 has a prime factor q with (q/c) = −1.
       * P1.2: for c ∈ 𝒞_p, 3 ≤ c < p, and N = sq with q prime and q ∤ s: on U, success is equivalent to a divisor of s
         being −1 or −p modulo c; on T, it is equivalent to a divisor of s being −1 modulo c.
       * The large-CRT samples for T3.1 are EVIDENCE (BPSW probable primes).
3. **Beyond the BM layer.** Control the class of the level divisor inside the coset {χ_{−t} = −1} at a single n, beyond the
   BM character: the coset has φ(t)/2 classes, exactly one (−1) good, and still contains the other genus characters, which
   can obstruct (the (★)-failure n = 7 at t = 12; (J)103 §2 Reading). *Why:* it is the next layer after the one proved free.
   *(z52d, `Z52D_FOURIER.md`, cross-model reviewed.)* In window coordinates the BM character χ_{−e} carries an exact,
   explicit share of the Fourier obstruction mass and obstructs only unforced windows (PROVED); the other odd real obstructions
   are χ_p twisted by even genus characters of the window (Assessment) — i.e. exactly this item. A signed bounded-order
   character inverse lemma for obstructed windows is false for B ≤ 952 (PROVED + CERTIFIED; every B under Dickson), and no
   tested non-BM character (conductor ≤ 200, mass share c ≥ 0.15) covers more than about 16 % of a surveyed prime's forced
   obstructions (mean 10 %, mostly (·/3); EVIDENCE, 30 hard / 116 matched / 400 random primes). The "exceptional
   character / regime split" variant thus reduces to this item plus B2.
   *(z53, cross-model reviewed.)*
   * **Genus layer per slice (`Z53_GENUSLVAL.md` Prop C; PROVED).** For squarefree u ≡ 1 (4), u ≤ p^α with fixed
     α < 3/5, Prop C gives an L-value approximation to S_u with power-saving additive error. The nonprincipal sum runs over
     η ≠ 1 and has prefactor 1/(2φ(u)); the principal term retains L′ and H′ terms. EVIDENCE: maximum relative error
     0.1292 % in 18 tested slices with X_u ≥ 10⁵, including (★)-zero primes; net cross terms remove about 38 % in one
     displayed slice. Aggregate M_gen(p) = o(log²p) is excluded by Thm U (item 4).
   * **Density-level class control on a subfamily (`Z53_GENUSX.md` Thm X; PROVED, unconditional, effective).**
     * On the Thm U family with window conditions (C1), (C2*), (C4), all characters of order ≥ 3 mod 8u contribute only
       their genus value to the density main term (T_u = O(p^{−δ} log p)). The input is Burgess mod p, class by class.
     * With (C3) the exact-class density main term is ≥ (c − o(1)) log²p, with c up to ≈ 0.0019.
     * Not controlled: the two exact-divisor layers. Lemma 4.1 rewrites the exact subfamily counts R_𝔉 and G_𝔉 as sums
       over free w of functions of (p mod w, ⌊p/w⌋). The unresolved centred layers are T_w = G_𝔉 − M_𝔉 and
       T_uw = R_𝔉 − G_𝔉 − T_u; they also subtract density terms.
     * Assessment: these are B2-shaped gaps connected to §7.1, not a proved B2 equivalence or universal convergence
       theorem. Both layers remain open; separate bounds suffice but are not individually necessary, since they could
       compensate.
     * EVIDENCE in standard-window samples outside Theorem X's hypotheses, at scales 10⁹–10¹²: var(R_𝔉 − G_𝔉) is about
       88–93 % and var(G_𝔉 − M̂) about 9–10 % of var(R_𝔉 − M̂). Only the former is compared with swap-Poisson, with
       variance/(2·mean G_𝔉) ≈ 0.81–1.02. These proxy statistics do not validate Theorem X.
   *(z54, two lanes on the exact layer R_𝔉 − G_𝔉 = T_u + T_uw, each with internal hostile and cross-model review;
   `Z54_SUMMARY.md` §2. Setting of `Z53_GENUSX.md` §1: U_i = p^{α_i}, Y = p^β, X = p^γ, 8U₁X ≤ p, Y ≥ U₁.)*
   * **Exponential sums in p/w (`Z54_EXACTSUM.md`; narrowed).**
     * Identities (PROVED, Props 3.1, 3.2): R_𝔉/2 = Σ_{q odd squarefree}Σ_{a mod* q}W(a, q), with
       W(a, q) = Σ_{u∈𝒰, q|u}u⁻¹Σ_w e(a(⌈p/w⌉ + 2)/(2q)) over shell w with ⌈p/w⌉ ≡ 6 (8); and R_𝔉 − G_𝔉 = Σ_{f>1}D_f, D_f
       the part from primitive non-real characters mod f of the level divisor w″. Lemma 3.3 (PROVED): at odd squares
       R = G = M = M^cls = 0, so T_u = T_w = T_uw = 0; T1 does not constrain upper bounds for T_uw, and the
       square-sensitive input of this route is Thm U.
     * Theorem N (PROVED; scoped no-go): fixed window 0 < α₀ < α₁ ≤ β < γ with 8U₁X ≤ P, U₁ > 3U₀, X ≥ 12Y. For P ≥ P₀
       and every prime f ≡ 1 (4) in (U₁/3, U₁], some n ∈ [P, 2P], n ≡ 1 (24), has D_f(n) ≥ 1 and Σ_{a mod* f}W(a, f)(n) ≥ 1/2;
       block f sees only the integer n + f. Hence bounds on |D_f(n)| (resp. |W(a, q)(n)|) valid for all such n, summed by
       the triangle inequality, total ≥ (1/3 − o(1))U₁/log U₁ (resp. ≥ (1/6 − o(1))U₁/log U₁) = P^{α₁−o(1)}, against the
       target o(log²P). Not excluded: bounds using the primality of p, one-sided estimates, bounds combining blocks before
       absolute values (cross-u), other transformations; composite f and f ≤ U₁/3 are not covered by the construction.
     * Lemma 4.1, Cor 4.2 (PROVED relative to an exponent pair (κ, λ) with κ > 0): for a dyadic box u ∼ U, k ∼ K with
       2U ≤ p, K² ≤ p, H* ≥ 1 and K ≥ qJ₀, the number of (u, k) with f | u, k ≡ c (mod q), k | p + u (q ≥ 1, f | q, f odd,
       gcd(c, f) = 1) equals its density up to O(E + 1), E = (p^κK^{λ−κ})^{1/(1+κ)}, uniformly in q, f, c. This is the
       *plain* shell: transfer to the squarefree-w GX layers is Assessment, not carried out, and no certified bound for
       the GX layers is obtained.
     * Prop 4.3 (PROVED arithmetic): windows satisfying Thm U, Thm X (with GX's (C4) relaxed to the inequality (C4′) its
       proof uses) and Lemma 4.1's condition at the worst box exist with the classical pair A³B = (1/30, 13/15), e.g.
       (α₀, α₁, β, γ) = (0.200, 0.204, 0.7925, 0.7955); on that example Lemma 4.1, summed over c ≡ 6 (8) with
       gcd(c, d) = 1, certifies the plain-shell conductor-d blocks (f = d, q = 8d) for d ≤ p^θ, any fixed θ < 1/2800 (a sufficient range, not a barrier). All such windows have class-hit level C ≤ p^{(1−2κ−λ)/(4(λ−κ))}, ≤ p^{0.025} for every
       tabulated non-conjectural pair.
     * EVIDENCE (10⁹–10¹⁴, non-reconciled windows): in dyadic u-slices, blocks fed by one integer p + u carry
       ≈ 0.90–1.03 of var(R − G) (blocks fed by ≥ 16 integers ≤ 0.0035); for q ≥ 11 the W(a, q) have median rms at the
       random-phase benchmark. Cross-u decorrelation is a finite-sample heuristic.
     * Survives (Assessment): cross-u cancellation within a dyadic slice, i.e. B2 in tied form.
   * **Higher-order symbols (`Z54_EXACTSPIN.md`; narrowed).** Standing hypotheses of GENUSX §4 (Y ≥ U₁, 8U₁X ≤ p, p large);
     orders k ≥ 3.
     * Lemmas 3.1, 3.2 (PROVED): R_𝔉 − G_𝔉 = S₂ + S_o with S₂ = Σ_{4|k}Δ_k (characters of order divisible by 4) and
       S_o = Σ_{k≥3, 4∤k}Δ_k. Both vanish pointwise off the genus, hence at odd squares (gcd(u, m) = 1), via the empty
       genus; Δ_k with 4 | k also vanish there, Δ_k with 4 ∤ k need not (CERTIFIED nonzero Δ₃, Δ₅, Δ₆, Δ₇ on 600 squares).
     * Dictionary at prime u = ℓ for k | ℓ − 1 (PROVED; finite CERTIFIED checks on 3 817 cubic and 7 822 quartic shell points at 24
       primes): the order-k part is the Ramanujan sum c_k of (−w″/𝔩)_k = (−1/𝔩)_k(p/𝔩)_k(2w/𝔩)_k⁻¹, whose p-factor is the
       Frobenius of 𝔩 in ℚ(ζ_k, p^{1/k}) (Lemma 4.1). For k = 3, (x/π)₃ = Ξ_p(θ)Ξ_{2w₁}(θ)⁻¹(3/π)₃^{−v}, an anticyclotomic
       character of the angle θ = π/π̄ with a ramified factor at 3 (Lemma 4.2). For k = 4, (x/π)₄ = ε(π, w)(π/p)₄(π/w)₄⁻¹
       with (π/p)₄ = (ℓ/ρ)₄⁻¹(π/ρ)₂, and (π/q)₄ = (π/κ)₂(−p/κ)₄⁻¹ for split q = κκ̄ | w (Lemma 4.4). No bounded-degree
       identification of the full layer is established, and none is excluded.
     * Scoped limitations (PROVED statements, except the explicitly labelled Assessment): complete sums of the
       cubic symbol over a unit norm fibre (norm coprime to the modulus) vanish when the modulus
       m is prime to 3 and not a cube (quartic: m odd with some prime to an odd power) (Lemma 4.3), but on the (★) support every fixed-modulus fibre has
       ≤ 6τ(u) points and every fixed-argument fibre is one integer's divisor set (Lemma 4.5). Assessment (in the original
       coordinates): this excludes only the direct complete-fibre average. Characters of order dividing a fixed K do not reconstruct the class event outside a
       finite menu 𝒰_K of u (Lemma 3.3). The cubic prime-u layer (3 ∤ w″) is a twisted equidistribution problem for roots
       of N(α) ≡ −p (mod c) in shrinking discs (Prop 4.6, identity); the smooth Fourier majorant with triangle inequalities
       in m and c yields an o(C²r²) bound from (W) ≪ C^{2−δ}|m|^A when A ≥ 0 and δ > (1 − θ)(2 + A) ≥ 1, with
       r = C^{θ−1}, θ ≤ 1/2 and cube moduli excluded (Prop 5.2). Here C²r² is the expected smooth-count scale; no lower
       bound for that count or transfer to the prime/window-weighted layer is proved.
     * Assessment: FIMR / Koymans–Milovic do not apply as stated (no matching spin representation of the layer is
       supplied; the base fields ℚ(ζ₃), ℚ(i) have only an involution; shell weights do not match their summation sets;
       conductor-p and order uniformity are missing). B6 is not the obstruction.
     * EVIDENCE (10⁹–10¹⁴): no significant individual-sample bias at any listed order ≤ 24 (|mean z| ≤ 0.18); a pooled
       +0.03σ (3.0 se) offset of R − G is unexplained. Such tests detect residue-class bias only and cannot falsify an
       o(log²p) bound. S₂ and S_o each carry ≈ ½ of var(R − G).
     * Survives (Assessment): a fixed-p theory of symbols over a moving family of fields indexed by u ≤ p^{α₁}; signed or
       non-Fourier methods for the root problem (per fixed order); Type II structure in w ↦ r_w.
   *(z55, three lanes on problem CROSS and the exact layer, each with internal hostile and cross-model review;
   `Z55_SUMMARY.md` §2. Problem CROSS: for some window admissible for `Z53_GENUSLVAL.md` Thm U, show R_𝔉(p) ≥ 1, or
   ≥ c log²p, for every sufficiently large prime p ≡ 1 (4).)*
   * **CROSS NOT proved (`Z55_CROSSO.md`, `Z55_CROSSF.md`).**
   * **Certified recalibration (`Z55_CROSSF.md` §3; CERTIFIED counts).**
     * Window: the z53 engine's standard window, the boundary approached by strict Thm U windows:
       U₀ = round(p^{1/12} − ½), U₁ = ⌊p^{1/3}/2⌋, Y = ⌊p^{1/3}⌋, X = ⌊p^{2/3}/4⌋ (decreased until 8U₁X ≤ p).
     * Exhaustive ranges (two scanners agree on the 10⁸ range; the cross-review reran that range byte-identically,
       independently recounted 512 sampled primes at 10⁸ and 10¹⁰, and audited the remaining counts from saved data; it
       did not rerun the 10¹⁵ zeros): primes p ≡ 1 (4)
       with hits(p) = R_𝔉(p)/2 = 0:

       | range | zero primes | fraction |
       |---|---|---|
       | [10⁸, 1.02·10⁸] | 21 233 / 54 198 | 39.2 % |
       | [10⁹, 10⁹ + 10⁷] | 83 874 / 240 944 | 34.8 % |
       | [10¹⁰, 10¹⁰ + 10⁷] | 51 773 / 217 331 | 23.8 % |
       | [10¹¹, 10¹¹ + 10⁷] | 30 069 / 197 020 | 15.3 % |
       | first primes above 10¹² | 5 520 / 58 878 | 9.4 % |

     * Samples:

       | scale | zero primes | fraction |
       |---|---|---|
       | 10¹³ | 444 / 8 290 | 5.4 % |
       | 10¹⁴ | 79 / 2 238 | 3.5 % |
       | 10¹⁵ | 9 / 535 | 1.7 % |
       | 10¹⁶ | 0 / 108 | 0 % |

     * Largest certified zero: 1 000 005 280 000 049.
     * Consequences:
       * CROSS for this family fails at each such prime. Any threshold p₀ for "R_𝔉 ≥ 1 for p ≥ p₀" in this window
         therefore exceeds 1.000005·10¹⁵. The same holds for every subfamily contained in this window, since R_𝔉 is
         monotone in the family.
       * (H⁻_𝔉) of `Z53_GENUSX.md`, X_𝔉 ≥ −(1 − ε)M_𝔉, is false at every zero with M_𝔉 > 0. The cross-model review
         certified M_𝔉 > 0 at all 192 469 recorded exhaustive-scan zeros.
       * Eventual positivity with unspecified p₀ is not refuted.
     * EVIDENCE: the five exhaustive scans have approximately Poisson-shaped hit counts with resolved overdispersion,
       var/mean ≈ 1.03–1.07. The smaller samples at 10¹³–10¹⁶ have ratios ≈ 1.06, 1.02, 1.08, 0.83. Across the nine
       datasets mean/log²p ranges approximately from 0.00249 to 0.00335, non-monotonically. The model constant
       1/(3π⁴) ≈ 0.003422 is half of Thm U's lower-bound coefficient, not a proved mean.
     * Assessment (model only): model hits ~ Poisson(c log²p) with c = 1/(3π⁴).
       * It predicts ≈ 5.6·10³⁰ zero primes, concentrated near 10⁶³.
       * The expected tail count is 1 near p ≈ 10¹²⁴. This is an expected-count crossover for this standard-window
         model with its assumed c, not a certified last exception; no theorem forces a proof's p₀.
       * Assessment: this model has an expected-tail-count crossover near 10¹²⁴, not a proved lower bound on a proof's
         threshold or a last-exception prediction with a specified confidence. Exhaustive testing to that scale is
         infeasible; an effective proof's explicit constants could still be checked. Enlarging the family's mean or
         finding another positivity mechanism is a suggested route, not a necessity theorem.
   * **Exact forms (`Z55_CROSSF.md` Lemmas 1.1–1.3, `Z55_CROSSO.md` Lemma 1.1; PROVED).**
     * For (u, w) ∈ 𝔉(p), a hit is equivalent to the existence of an integer C ≥ 1 with p = 8uwC − u − 2w,
       equivalently 4Cp + 1 = (4uC − 1)(8wC − 1). All recovered variables retain the family's integrality, window,
       parity, squarefreeness and coprimality restrictions.
     * Both factors are non-residues mod p, so R(m²) = 0 at odd squares.
     * Each one-variable section (fixing u, w, C or d) is a single-integer divisor-in-progression event.
     * Assessment (non-bankable): the averages found reach only density level or the principal character.
   * **Positive proportion and almost all (`Z55_CROSSO.md`; see §5.1).**
     * Theorem P (PROVED, unconditional): on windows with α₁ + γ < 1/2, a positive proportion of the primes
       p ≡ 1 (4) have R_𝔉(p) ≥ 2.
     * Theorems A, A′: almost all, CONDITIONAL on HV resp. HW. Both are open; the case analysis for HW is only
       sketched.
   * **Cross-u cancellation (`Z55_CROSSU.md`; inconclusive on (CU), narrowed only by reformulations).**
     * Target (CU) (CONJECTURE, not proved): R_𝔉(p) − G_𝔉(p) = o(log²p) as p → ∞ through primes p ≡ 1 (24), on a window
       with M_𝔉 ≫ log²p.
     * CONDITIONAL: (CU), Z53_GENUSLVAL Theorem U and (X-w), on one common admissible window, give (★) for all
       sufficiently large primes in that progression.
     * Standing hypotheses for these reformulations: U₀ ≥ 1, Y ≥ U₁, 8U₁X ≤ p, and the stated family restrictions.
       Here 𝔖₃ is the shell restricted to d ≡ 3 (4).
     * Lemma A (PROVED; class index): on a shell point with level d put j := (u·(u⁻¹ mod d) − 1)/d ∈ [1, u).
       * Then j ≡ −d⁻¹ (mod u), and at primes j = ⌊u·(d⁻¹ mod p)/p⌋.
       * On 𝔖₃, an exact hit is equivalent to j = 1, and genus membership is equivalent to j ∈ □_u.
       * On 𝔖₃, (d/p) = −(j/u).
     * Lemma B (PROVED): on 𝔖₃, exact hits are precisely the shell points whose ceiling Euclidean expansion of (p, d)
       has length 3.
     * Lemma C (PROVED): for c > 0, N_c is twice the number of representations
       1/(cp) = 1/(2wtu) + 1/(2wtp) + 1/(ctup), with positive integral t and (u, w) ∈ 𝔖₃; summands with gcd(c, u) > 1
       are zero. Fibrewise, G|_u = q_u⁻¹ Σ_{c∈□_u} N_c|_u, where q_u = |□_u|. This is not an average over one fixed
       global set of c.
     * §4.1 (PROVED, scoped): q_u = |□_u| ≥ (2/√15)√u for odd squarefree u.
       * So on moving windows (U₀ → ∞) and for each fixed K, a hit cannot be cancelled exactly by K genus non-hits for
         large p.
       * Large groups, approximate cancellation and positivity maps are not excluded.
     * On the switchable domain where d is odd squarefree in (Y, X] and gcd(d, up) = 1, swapping w and d gives
       j′ ≡ 2p⁻¹j⁻¹ (mod u); for a switch within 𝔖₃, both d and w must be 3 (mod 4). It can reverse a hit's sign, but no cancellation follows.
     * EVIDENCE (10⁹–10¹⁴, 1 000 primes plus controls):
       * the hit class is not distinguished among 18 index classes;
       * for 300 primes at 10¹²–10¹³, firing-set pair differences have bootstrap intervals containing zero against a
         descriptive genus-weighted benchmark, not the exact conditional law; a weak excess of close-u pairs is not
         excluded;
       * these tests cannot support or falsify (CU).
     * Assessment: no cross-u mechanism was found. B2 in tied form survives.
4. **CLOSED (z53).** `Z53_GENUSLVAL.md` Thm U (PROVED, unconditional, effective; cross-model reviewed CORRECT): M_gen(p) ≥
   (2/(3π⁴) − o(1))(log p)² ≈ 0.0068 log²p at every sufficiently large prime p ≡ 1 (4). It uses Burgess for cube-free conductors on Thm 5.4's
   subfamily with sharp windows. The square-sensitive step is that ηχ_{−4up} is non-principal because p divides its
   conductor, and this is the step that fails at odd squares. Still open: the transfer X(p) ≥ −(1 − ε)M_gen(p), which is
   ES-(★) strength (see item 3), and the sharp constant (observed min 0.084, sample-specific). *Original item:* **A polylog lower bound
   for M_gen(p)** unconditionally (GRH gives only log log p; (J)98). *(z48 update: `LOWERTAIL_DEEP_ASTRA.md` Thm 5.4 gives M_gen(p) ≥ (2/π⁴ − o(1)) log²p from **any fixed Dirichlet zero-free strip**, hence CONDITIONAL on OAI-003 or GRH; at z48 an unconditional version and transfer were open; z53 closes the genus lower bound only.)* *Why:* M_gen is the finer
   T1-exact main term; with it the one-sided target could be stated relative to the genus series.
5. **BM-corrected Harris/FKG inequality over primes** ((J)103 §3; recorded there only as a
   CONJECTURE shape, T1-consistent). *Why:* the only variance loophole identified. *Caution:* it would imply a power-saving
   exceptional-set bound for (★), far beyond every method mapped in (D)9–(D)24 — so this item is hard, not tractable.
6. **Full-factor-multiset realisation** (`CLASS_FORCING.md` §6): can fixed Frobenius data of p restrict the classes of *all*
   prime factors of p + 4d jointly (Thm 5.2 excludes single factors)? *Why:* the precise residue of "reciprocity forces
   parity never class".
   *(z53, `Z53_GENUSREDEI.md`, cross-model reviewed.)* This is now **CONDITIONALLY closed (relative to BHC) for fixed
   finite families of levels**; only the pointwise laws and the partial-configuration result below are unconditional. Here BHC is a Bateman–Horn–Chebotarev hypothesis, not HC(p).
   * Objects: a fixed finite family of lines satisfying §1, an admissible Frobenius datum Π of p in a fixed finite
     Galois field, and the joint decorated configuration of the large prime factors (their classes, power symbols at p
     and the joint Rédei matrix).
   * PROVED: five necessary pointwise laws.
   * CONDITIONAL on BHC: completeness for complete decorated configurations with squarefree rough parts (JRT).
   * Unconditionally (U): finite partial configurations satisfying (L3), (L5) occur on a positive-lower-density set of
     primes; residual cofactors need not be prime or squarefree.
   * CONDITIONAL on BHC (F): bounded-level forcing from Π alone is exactly B1; prescribed factor decorations can
     additionally force events.
   * Open: growing level families (B2), p-dependent class-group data, repeated large factors.
7. **General-m Stickelberger identity** (`TWO_POWER_LADDER.md`; proved for m = 3, 4 only). *Why:* would close the
   higher-reciprocity route at every layer, or reveal an exceptional m.
8. **Thin families still open:** 15·2^s + 1 (u ≡ 7 (8) valuation branch — reduces to a 2-adic approximation problem — and
   menus II-ac, I-ac, II-cd; two-base boundary at X = 2^t3^{t′}), 4^s + 297 (not attempted), 4^s + 33, 4^s + 273 ((J)102; routes
   board's champion lane). *Why:* concrete, finite-looking, and the only setting where forced-budget identities have beaten
   every ET covering.
   *(z52d, `Z52D_THINFAMILY.md`, cross-model reviewed.)* A certificate that is C-finite in 2-power roots is a root family
   (PROVED), so recurrence fitting adds no new menu (other bases not covered); BM on minimal certificates found no low-order
   recurrence (EVIDENCE only). For 15·2^s + 1 at μ = 0, moving-gap root families with irreducible smallest coordinate lie
   in menus A (⊇ II-ad), A′ (⊇ I-ac) or C; C is empty (PROVED); the u ≡ 3 (8) branch of A is empty (PROVED); A and A′ with
   integer u are certified empty for v₂(c) ≤ 3000 (beyond: Ridout-finite per p ≥ 5, ineffective; p = 3 open). Open:
   reducible-x families (II-ac/II-cd), the ranges beyond the certified bounds, non-2-power exponential certificates.
   Formalised: ES(3·2^s + 1) for all s in Lean (`lean/ES/ES/Proth3.lean`, standard axioms; z52d Z1894).
   *(z53, `Z53_THIN15.md`, cross-model reviewed; narrowed.)*
   * ES(15·2^s + 1) is CERTIFIED for s ≤ 3·10⁶.
   * Menu II-cd (B′): in B′'s odd-power shape, each fixed odd prime exponent p gives four Thue equations, each with at
     most one positive solution (Bennett); SG shape is separately excluded.
   * Menu II-ac (B): B's odd-integer-u branch is Ridout-finite for each fixed odd prime exponent p, including 3,
     ineffectively and non-uniformly in p; general rational-u finiteness is not proved. B is certified empty for integer
     u with E ≤ 3000, dyadic u with ip ≤ 72, integer w, and dyadic SG w with 4i−2 ≤ 90.
   * Sign lemma (PROVED): no rule polynomial in 2^{s/2} reaches μ = 0.
   * ET/divisor-class coverings alone fail: residue 0 survives. A general finite congruence covering must include a rule
     valid on all sufficiently large multiples of a modulus; such coverings are not excluded.
   * Polynomial dependence on multiplicatively independent extra exponential bases collapses to the 2-power variable,
     giving a μ = 0 root family only on a residue-0 progression.
   * Open: Laurent/rational dependence, binomial menus beyond certified ranges and non-binomial patterns including
     D = 3 II-d and D = 6.
9. **Uniform multiplicity on the r-generic line** (`SIBLING.md` Conj 4.2; EVIDENCE: r ≤ 61 through depth 4, r = 19 through 6,
   r = 17 through 7) and **r = 17**. Level-1 survival of a non-residue cell is CERTIFIED only for r < 2·10⁴ (and fails for
   r ≤ 13). *Why:* Conj 4.2 on 17 ≤ r < 2^{21.44}, plus level-1 survival where not yet certified, would give sterile r-generic
   points for every prime r ≥ 17 — a sharp threshold ((J)77).
10. **F₃[T], CONJECTURE 0.2** (the thirds corner x*_c is uncovered). *Why:* the last open case of function-field sterility;
    a percolation/König question ((J)71, (J)72, (J)77).
11. **Question R / restricted Hypothesis TG** (`QUESTION_R.md`, (J)99): self-levelled SL₂ words and the theta multiplier.
    *Why:* the exact Rickards–Stange form of T1; open in its own right.
12. **Exceptional-set exponent θ > 3/4**: weak SPW (log(K/η) = O((log N)^{3/4})), the shift-uniform avoider count (W_𝔊),
    TC^alt_θ, residue dispersion (RD′) (STATUS "Exceptional-set exponent"). *Why:* the sharpest averaged statement; each
    is reduced to a precise open estimate.
    *(z50 update, `BREADTH_Z45.md` §15.)* The audited whole-avoider CRT architectures are capped at their supply exponent
    (3/4 ES, 2/3 U/ES₅; I3 native classes 2/3). Two concrete proposed non-CRT statements: (i) **RLD-U / FL∞**, an upper
    bound e^{C(s)}·(Mertens product) for the prime-modulus U sieve at z = N^{1/s}, off the squares — a fundamental lemma in
    dimension ≍ log z at level s ≪ dimension (EVIDENCE to 10¹⁰). With the Titchmarsh-type asymptotic Σ_{ℓ≤z} w(ℓ)/ℓ ~
    C_V log z, C_V > 1/2, and some 1 < s < 2C_V, it gives #{n ≤ N, n ≡ 1 (4): U fails} = #odd squares + o(√N)
    (`EXSET_ARITH_JANSON_OPUS.md` Cor 6.1, CONDITIONAL; C_V ≈ 0.74 empirical). (ii) **Linnik confinement** (one sufficient
    route): a common set of primes q ≤ (log X)^{2+δ}, quadratic residues modulo every exceptional prime, generating
    ≥ X^{1+c} integers below X²; this would give a power saving at primes (`EXSET_SIEVE_MASS.md` §4.2). Other routes
    stay formally open (signed interval information, alternative I3 presentations, bounded-shift forcing, prime-only
    positivity). Assessment: (i) and (ii) look as hard as the pointwise problem. Not available: universal arithmetic
    Janson with O(√N) error (false), marginal-only transfers (scoped blindness), constant-loss whole-shift product bounds
    (θ ≤ log 2).
    *(z51 update, `BREADTH_Z45.md` §16.)* Both statements were attacked by six lanes and a board; neither moved. New: a
    route beyond 3/4 CONDITIONAL on a new nonstandard hypothesis MF₁ — a fixed positive reciprocal-weighted QR bias of
    ES-exceptional primes on the primes in (C log p, 2C log p] — gives E_ES(X) ≪ X exp(−c log X/log log X)
    (`EXSET_CHAR_FORCING.md` Cor 5.4; MF₁ is implied by a stronger pointwise majority-reach statement observed at all 36
    sampled primes for C = 1/2); Heath-Brown lowers Linnik's requirement to (log X)^{1+δ}. Scoped barriers: sparse-plane
    sterility (no finite native ES₅/U word-class family certifies a sparse squarefree quadratic bias, `EXSET_LINNIK.md`
    Thm 2.5/Cor 2.6), an axiomatic prime-detection barrier on the 4ℤ line (`EXSET_DEPTH_BREAK.md` Thm 2.3), no
    implication from an audited named hypothesis to RLD-U (`EXSET_HIGHDIM_SIEVE.md`). Function fields: in the iterated
    large-q model, monodromy breaks depth (ρ_{n,p} ≤ exp(−0.0043n²), n ≥ 12; CFSG + Chebotarev), with no known integer
    transfer (`EXSET_FUNCTION_FIELD.md`). Evidence: the top band ℓ > √(2N) of the prime U family has zero probability close
    to exp(−mean) at fixed scale (N ≤ 10¹¹), suggesting but not proving TB_pow.
13. **Cap 0 / bounded cap pointwise** (R200 M1): a bounded cap for every prime under a standard hypothesis, or replacing
    Hypothesis W by a standard one ((J)85, (J)91). *Why:* the only pointwise positive mechanism; its last step is B2.
14. **ES ⇒ ES₅?** Is every ES prime a five-slice prime (λ(p) ≤ 3)? (56 % of solutions below 3000 lie outside the five-slice
    image; `LOWER_TAIL_FABLE.md`.) *Why:* decides whether the cleaner Legendre-form/forest picture loses anything.
    *(z52.)* The coprime-category analogue fails on composites: 3985 has coprime Type I solutions but every five-slot word
    has gcd(uv, 3985) = 5 (CERTIFIED). At primes the coprimality is automatic and the question is unchanged.
15. **A "prime T1"** for disproof ((J)97): a global invariant at one prime forcing all ≍ (log p)³ events into the wrong
    class — or a proof that none exists beyond squares. *Why:* the only conceivable disproof shape.
    *(z52 calibration, `ES_APPROACH_GENERATORS.md` G2–G4.)* In the pencil 4xyz − n(xy+yz+zx) = m² (m ≥ 1), the class (−q, −d)
    gives a positive-integral Brauer–Manin obstruction on a positive-density set of locally soluble n (PROVED). At
    k = 0 it ramifies on the exceptional conic for non-square n, so primes escape it. The siblings S_{n,−4} (for 2 ≤ n ≤ 10⁵
    fails only at 2, 9, 21, 165, 945, 1197) and ES over ℤ[i] with first-quadrant denominators (up to reflection, six
    Gaussian-prime failures, none for 10⁴ < N ≤ 10⁶) have failures only in low-count cells. This is consistent with
    lottery-type failures; no further invariant was found (Assessment). No prime T1 was found.
16. *(Housekeeping item resolved, R290 repair:* the (★) constants (log p)²/8 and 3/(2π²)(log p)² are the all-integer and the
    prime densities of the same ordered count; see §2.2 and `reviews/frontier-review.md` task (2).)
17. **Conjecture I3** (z48/z49): every n > 2 433 600 is tuv − u − v with t, u, v ≥ 3. It is sign-free, prime-free and
    character-free; the class-free count is ≥ c log²n at every n (PROVED), and I3 is its single-class restriction.
    What is known (`I3_DEEP_ASTRA.md`, `I3_DEEP_FABLE.md`):
    * Haar survival with both endpoints ≤ H: c L²/(log L)² ≤ −log δ₃ ≤ C L⁶/log L.
    * The exceptional set is ≪ N exp(−c(log N)^{2/3}(log log N)^{−1/3}).
    * I3 holds on 2^k ± 1, 2^k ± 3, 7·2^k − 1, 5·2^k − 1 and 3·2^k + 1, by exponent coverings.
    * The zero at 1560² is explained by the local model (square depletion plus 2³·3·5·13 | m).
    *Why:* it is the minimal test problem for any single-integer tied-class method. No standard conjecture is known to
    imply it.
    *(z52.)* The certificate-restricted version I3_𝒞(p) ≥ 1 (a word with t, u, v ≥ 3 and a coordinate in 4ℤ ∪ (8ℤ − p))
    implies ES₅(p), hence ES(p) (PROVED). Its zeros at primes p ≡ 1 (4) ≤ 10⁹ are exactly 5, 13, 17, 2521, and the least
    certifying interior endpoint is u ≤ 39 throughout (CERTIFIED, `Z52_BANKED.md` §1(e), T1). It is ES-strength.

## 8. Pointers into the repository

* **Start:** `STATUS.md` (wave headlines, newest first; ES-not-solved banner), `DISCOVERIES.md` (ledger with labels; (J)57–(J)108
  for Waves Z–AC), `CAMPAIGN_SUMMARY.md` (human-readable overview), `PROJECT.md` (original plan).
* **§2 lower tail:** `SINGLE_P_COUNT.md` (pair form, genus split), `BM_CORRECTED_COUNT.md` (M_BM, H⁻_BM, Linnik, numerics),
  `METAPLECTIC_ES.md` (Theorem K), `SYNTHESIS_SPARKS9.md` (level coordinates, BM layer free), `BOARD2_SLATE.md` (five-slice
  constant 45/(8π²), ABH, moving windows), `LOWER_TAIL_ASTRA.md` (forest), `LOWER_TAIL_FABLE.md` (two-target form), board
  memos `~/.pi/boards/20261018-es-lowertail/memo.md` and `…/20261018-es-routes/memo.md` (note: the lower-tail memo's
  five-slice constants are superseded by BOARD2_SLATE; R290 repair: these memos are outside the repository and may be
  unavailable to an external reader — BOARD2_SLATE and STATUS record their outcomes).
* **§3 barriers:** `POINTWISE_SIZE.md` (B1), `reviews/redteam-automorphic.md` §4 and `reviews/redteam-automorphic-2.md` §2–3
  (T1–T8, B2, hatches H-A…H-G), `CONDITIONAL_ES.md` (B3, X_slice), `LONGSHOT_PIGEONHOLE.md` / `LONGSHOT_FIBRED.md` (B4),
  `PARITY_AUDIT.md` (tied modulus), `CLASS_FORCING.md`, `TWO_POWER_LADDER.md`, `SYNTHESIS_SPARKS8.md` (privacy, b = 1 line),
  `JOINT_BUDGET.md`, `SYNTHESIS_SPARKS4.md` (positivity), `SYNTHESIS_SPARKS3.md` (numerator blindness), `AMPLIFY_EXCEPTION.md`,
  `NONCONG_LIFTS.md`, `DISPROOF_AVENUES.md`, `POWER_LADDER_ES.md`, `B2_ACROSS_FIELDS.md`, `ZAREMBA_TRANSFER.md`,
  `FIXED_MODULUS_SHOTS.md`, `UNIT_ORBIT_ES.md`.
* **Sibling bridge:** `ASTRA_BRIDGE.md` (the lattice L_ρ(g): Astra sources (m, 1), Claude shots (2k, Y), ES = intersection;
  PROVED), `LATTICE_MEETING.md`, `HARD_PAIR.md`, `ASTRA_BRIEF_DIRECTION2.md`. The sibling `../erdos-straus-astra` is read-only.
* **Literature:** `LITERATURE_2026.md` (survey to 2026-09-28, claimed proofs and their gaps), `LITERATURE_AUTOMORPHIC.md`,
  `sources/`.
* **Papers** (`paper/README.md`; all internal): `es-threequarter-note` (INTERNALLY PROVED), `vaughan-loglog-note`,
  `es-typei-heegner-note` (Σ f_I ≪ N log²N), `es-mn-short-note`, `sieve-limits-note`, `es-subexp-note`, `es-omega-note`,
  `es-window-note`, `es-coverings-note`, `es-automorphic-barrier-note`, `pointwise-obstruction`, `energy-dnf-note`.
* **Reproducibility:** `verify.py` (lettered blocks re-run reviewers' from-scratch checks), `scripts/` (e.g. `z38_*` for
  BM_CORRECTED_COUNT, `z39_kronecker.py` for Theorem K), `logs/`. Run with `PYTHONPATH=scripts uv run python …`.
* **Reviews:** `reviews/` (hostile reviews per result), `reviews/agent-reports/` (task reports O1–O279), novelty audits
  `reviews/novelty-audit-2026-10*.md`.
