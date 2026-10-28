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
* *Statement.* Best known pointwise bound: |E(p)| = |R(p) − M(p)| ≪ p^{2/5+o(1)} (PROVED relative to ET Prop 1.7; divisor
  bound, no cancellation), against M(p) ≍ (log p)². Weil on the modular hyperbola 𝓗 = {xy ≡ 1 (mod 4p)} has error p^{1/2+o(1)}
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
rule out:* growing/p-dependent roots, Pell or class-group cycle data.

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
* Σ_{p≤N} f_I(p) ≪ N log²N (PROVED rel. Kuznetsov/Petersson, Weil, twisted Weil, Selberg 3/16, λ₁ > 1/4; (D)32b;
  *needs expert scrutiny*).
* m/n density transition at log N ≍ m^{1/3}: upper half Thm U (PROVED rel. BV, Shiu; ineffective), lower half Thm L′
  (PROVED rel. ET Thm 7.1, BT, Shiu, PV); sharp order CONDITIONAL on SEL_m ((D)31 follow-ups).
* Moving windows (board #2 slate, (J)105; PROVED rel. Henriot's erratum, Siegel–Walfisz, Mertens): for 0 < α < 1/6, all but
  O(X/L^{4/3−2α−ε}) primes p ≡ 1 (8) in [X, 2X] have a Type II solution at *every* forced prime window q ≡ 3 (8) in
  [L^α, 2L^α] (L = log X). Witness-location information; says nothing about hard primes.
* Almost-all caps: for A > 1, #{p ≤ X : e*(p) > (log X)^A/4} ≤ X^{2/A+o(1)} — a power saving for A > 2; and
  #{p ≤ X : e*(p) > p^ε} ≪_ε (log X)^{⌈4/ε⌉} (`CAP_BOUNDED.md` Thm 3.2; PROVED rel. Montgomery's large sieve, PNT in APs;
  (J)83).

**5.2 Unconditional, pointwise — for relaxations or thin families, not ES.**
* The BM main term: M_BM(p) ≥ (3/(16π²) − o(1))(log p)² (Burgess) for every large prime; five-slice analogue
  ≥ (45/(32π²) − o(1))L² ((J)100, (J)105). Main terms only.
* The BM layer is pointwise free: for odd n, some t ≡ 0 (4), t ≤ 4ℓ(n), has M_t^lev(n) > 0 iff n is not a square ((J)103).
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
  II-ad u ≡ 3 (8) branch of 15·2^s + 1 is sterile for every root degree ((J)102).
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

**5.5 Standing conjectures with evidence** (CONJECTURE; EVIDENCE ranges in brackets).
SQ: for odd n, Type I ∪ Type II empty ⟺ n square [odd non-squares ≤ 10⁷]; SQ₅ (five slices; n ≠ 105) [10⁶]; SQ_± and 3SQ
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
* Exact identities: no linear relation between 56 ES counts and 54 classical functions (CERTIFIED, that finite dictionary); no
  finite fixed-level Eisenstein-type identity certifies Type I/II counts (PROVED via T1) → (I)5, (J)7 Thm 9.1. Growing-level
  identities remain open ((J)10: the T1-respecting W(n) identity exists, positivity is the spin event).
* Automorphic normal form (theta quotient, weight ½, Serre–Stark) → Eisenstein-only, exact, but does not decide one integer → (J)101.
* Dirichlet series / moments / Euler-product hardness laws → averages (B6) → `BRAINSTORM/anal_*`.
* Spectral/interlacing, faithful Euler systems, single-character Siegel dichotomy, ultraproduct transfer → displayed mechanisms fail, not universal no-go theorems (Assessment) → `BREADTH_Z45.md` §§1–4 (board #4 addendum, 2026-10-19).

*Algebraic / forcing*
* Congruence coverings, identity families, bounded search, seed-component (signed graph) line → B1; seed component sterile under H / Dickson → `POINTWISE_SIZE`, `FORMAL_CLOSURE.md`, STATUS "line 2: CLOSED".
* Reciprocity / Chebotarev / Rédei / higher power residues to force the class → parity only → (J)93, (J)96, (J)104.
* Non-abelian Frobenius, quartic data → inert on finite witness sets → (J)96, `MODP_RECIPROCITY.md`.
* Pigeonhole across shifts j or d → privacy of large primes → SS8 Lemma 2.3.
* Signed solutions then "reflect to positive" → no |d|- or square-class-preserving move; class-changing transfers are B2 → (J)52, (J)89 Lemma 4.1/Cor 4.2.
* Polynomial auxiliary budgets at a general prime; near-square / CF-norm / A² − pB² windows (coprime cases); p − 1 divisibility data → irreducibility / never Jacobi-forced / sterile point → (J)84 (Props 4.2–4.3).
* Class-group composition / slice-lattice walks (Astra bridge) → add reachability, never existence (3361) → (J)82.
* Fixed roots, least-non-residue roots in the forest F_n → fail i.o. under Dickson → (J)106.
* Bounded windows; balanced-lattice caps; GRH cap routes → bounded/slow cap is not ES; cap 0 is B2 → (J)83, (J)85, (J)91.
* Menu ladder from thin families to primes → positive-density rungs collapse to B1/B2 → (J)76, (J)78, (J)79.
* 2-adic / Fano pigeonhole beyond 4/p → used up (forcing only M ∈ {2,3,4}) → (J)57; no global Fano law on the 2-isogeny graph → (J)65.
* Windmills / involutions with finite affine menus → barred (CONDITIONAL) → (J)2 Thm 6.1.
* Fermat / binary-form certificates p = Q(u,v) → miss infinitely many primes of every square class → (J)3.

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

1. **Cancellation on a height-dependent subset of the modular hyperbola.** Bound E(p) = R(p) − M(p) better than the divisor
   bound p^{2/5+o(1)} *by cancellation*, i.e. any non-trivial estimate for #{(x, y) : xy ≡ 1 (mod 4p), x ≡ y ≡ −1 (mod 4C),
   C = (xy − 1)/4p} in a range. *Why:* "the only lead not ruled out" (`PARITY_AUDIT` §2–3); even a weak power saving would be
   the first class-aware single-integer input of this shape.
2. **Growing roots in the forest F_p** (edge uv ⇔ uv | p + u + v). Fixed roots and the least-non-residue root fail i.o. under
   Dickson, and the component of 1 can be as small as 8 vertices i.o. (CONDITIONAL on Dickson, `LOWER_TAIL_ASTRA.md` Thms 3.1,
   5.1) — so Fable's spark "|comp(1)| ≫ (log p)² unconditionally" is false under Dickson and the growth claim behind it was
   retracted (`LOWER_TAIL_FABLE.md` §2, R286 repair D5). Open: can p-dependent roots, or full reduction-cycle / Pell / class-group data,
   force a bichromatic edge (Astra's open questions)? An almost-all size bound for comp(1) is a different, open question.
   *Why:* the forest is the cleanest combinatorial form of ES₅.
3. **Beyond the BM layer.** Control the class of the level divisor inside the coset {χ_{−t} = −1} at a single n, beyond the
   BM character: the coset has φ(t)/2 classes, exactly one (−1) good, and still contains the other genus characters, which
   can obstruct (the (★)-failure n = 7 at t = 12; (J)103 §2 Reading). *Why:* it is the next layer after the one proved free.
4. **A polylog lower bound for M_gen(p)** unconditionally (GRH gives only log log p; (J)98). *(z48 update: `LOWERTAIL_DEEP_ASTRA.md` Thm 5.4 gives M_gen(p) ≥ (2/π⁴ − o(1)) log²p from **any fixed Dirichlet zero-free strip**, hence CONDITIONAL on OAI-003 or GRH; an unconditional version and any transfer to R(p) remain open.)* *Why:* M_gen is the finer
   T1-exact main term; with it the one-sided target could be stated relative to the genus series.
5. **BM-corrected Harris/FKG inequality over primes** ((J)103 §3; recorded there only as a
   CONJECTURE shape, T1-consistent). *Why:* the only variance loophole identified. *Caution:* it would imply a power-saving
   exceptional-set bound for (★), far beyond every method mapped in (D)9–(D)24 — so this item is hard, not tractable.
6. **Full-factor-multiset realisation** (`CLASS_FORCING.md` §6): can fixed Frobenius data of p restrict the classes of *all*
   prime factors of p + 4d jointly (Thm 5.2 excludes single factors)? *Why:* the precise residue of "reciprocity forces
   parity never class".
7. **General-m Stickelberger identity** (`TWO_POWER_LADDER.md`; proved for m = 3, 4 only). *Why:* would close the
   higher-reciprocity route at every layer, or reveal an exceptional m.
8. **Thin families still open:** 15·2^s + 1 (u ≡ 7 (8) valuation branch — reduces to a 2-adic approximation problem — and
   menus II-ac, I-ac, II-cd; two-base boundary at X = 2^t3^{t′}), 4^s + 297 (not attempted), 4^s + 33, 4^s + 273 ((J)102; routes
   board's champion lane). *Why:* concrete, finite-looking, and the only setting where forced-budget identities have beaten
   every ET covering.
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
13. **Cap 0 / bounded cap pointwise** (R200 M1): a bounded cap for every prime under a standard hypothesis, or replacing
    Hypothesis W by a standard one ((J)85, (J)91). *Why:* the only pointwise positive mechanism; its last step is B2.
14. **ES ⇒ ES₅?** Is every ES prime a five-slice prime (λ(p) ≤ 3)? (56 % of solutions below 3000 lie outside the five-slice
    image; `LOWER_TAIL_FABLE.md`.) *Why:* decides whether the cleaner Legendre-form/forest picture loses anything.
15. **A "prime T1"** for disproof ((J)97): a global invariant at one prime forcing all ≍ (log p)³ events into the wrong
    class — or a proof that none exists beyond squares. *Why:* the only conceivable disproof shape.
16. *(Housekeeping item resolved, R290 repair:* the (★) constants (log p)²/8 and 3/(2π²)(log p)² are the all-integer and the
    prime densities of the same ordered count; see §2.2 and `reviews/frontier-review.md` task (2).)

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
