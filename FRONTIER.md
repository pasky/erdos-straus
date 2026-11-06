# FRONTIER — the Erdős–Straus problem as of 2026-10-19: where to start

*Audience: a strong number theorist (or a fresh AI team) who has never seen this repository and wants to start from the current
frontier instead of rediscovering it. Task O279 (consolidation C3). No new mathematics here: every statement is a summary of a
repository file, with a pointer. When a summary and its source disagree, the source wins.*

> **The Erdős–Straus conjecture (ES) is not solved — not here, not anywhere.** No case of "ES for all large primes" is
> proved here, conditionally on any standard conjecture or otherwise. The literature was checked through 2026-09-28
> (`LITERATURE_2026.md`; the verification record was re-checked on 2026-10-18); every recent claimed proof has an identifiable gap.
> *(z58: literature addendum in `Z58_LIT.md`, sources accessed/searched 2026-11-05; bounded searches, not a completeness
> guarantee. It includes the priority item under "Exceptional set" in §1; the K-R-K standard-axiom CI closure is at the
> 2026-10-30 commit.)*

*Orchestration directives (papers are campaign artifacts, edit freely; wave mechanics): `OPERATIONS.md`.*

**Labels** (as in `DISCOVERIES.md`). PROVED = complete proof in the repo, possibly *relative to* named published theorems;
CONDITIONAL = proved assuming a named hypothesis (GRH, Dickson, Hypothesis H, SEL, …); CERTIFIED = an exact finite computation,
independently reproduced; EVIDENCE = numerics or heuristics only; CONJECTURE = stated, open; Assessment = a judgement or
interpretation, not a theorem. *(z58–z60 convention: for z58, z59 and z60 data, CERTIFIED denotes the exact finite computation in the cited
memo, with its stated engine and independent-check coverage. It does not mean a second full-range census; the ranges
independently reproduced or checked pointwise are specified separately.)* Everything PROVED here is *internally* reviewed (hostile reviews in `reviews/`), and **none of it
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

**Verification.** ES holds for all n ≤ 10¹⁷ (Salez); Spiridon Mihnea and Dumitru C. Bogdan (arXiv:2509.00128, 2025, unrefereed preprint) report
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
  *(z58 priority note, `Z58_LIT.md` §2.1; cross-model reviewed.)*
  * **External prior claim.** Kandukoori–Ramesh–Kumar (K-R-K), *An improved bound for the exceptional set of the
    Erdős–Straus equation*, state Theorem 1: E(N) ≪ N exp(−c(log N)^{3/4}) for all N ≥ 3, with the same saving for
    exceptional primes. Theorem 2 covers E_m for each *fixed* m ≥ 4.
  * **Source.** PDF dated 2026-07-29, archived in `data/z58/lit/sources/`; no arXiv record was found; unrefereed as far as known.
  * **Lean repository.** The root commit is dated 2026-07-30 and already has the 3/4 saving, then conditional on nine
    named analytic axioms. HEAD `f6c99eaa` (2026-10-30) closes with Lean's three standard axioms: the CI was verified,
    the project was not rebuilt locally, and the analytic proof was not re-audited.
  * **Chronology.** The campaign's note was first committed 2026-09-06. That date dates the file, not the discovery.
    Exact public priority is unverified (no dated public snapshot).
  * **Required wording.** Cite K-R-K wherever the internal 3/4 bound is mentioned. Do not call the campaign's bound
    first. *(Applied 2026-11-05: the note's abstract and introduction now cite K-R-K and claim no priority.)*
    *(z59 PAPERS, `data/z59/papers/CHANGES.md`: the sweep now covers every note quoting 3/4 — "claimed earlier", no
    priority, "shares this architecture but differs in its details"; false "no 3/4-type bound for m ≠ 4" and "first
    exponent improvement since 1970" claims removed. `es-mn-short-note` claims new only the short-interval/progression
    forms, uniformity in m, Cor D, Thms U, L′, relative to K-R-K's *stated* theorems; the K-R-K analytic proof is still
    not audited.)*
  * **What may still be campaign-new** (Assessment, to be compared): (D)30 and (D)31. Count-note Theorems A–D are
    not superseded.
  * Akaka Zenodo v0.8 (22905042, 2026-09-22) claims, as an author claim with a *claimed* Lean certificate and specialist
    review outstanding: there are absolute constants c, C, X₀ > 0 such that for every real X ≥ X₀ and each integer
    4 ≤ m ≤ (log X)³, at most CmX/(log X)⁴ primes in (X, 2X] have R_II,m(p) < c(log X)³/m. This concerns the full
    strict Type II family.
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
Pomerance–Weingartner, *Ramanujan J.* 69 (2026), art. 31, per z58 LIT); **8/n fails at n = 131 and 241** (E₈ ∩ primes < 2000 = {2, 3, 11, 17, 131, 241}; `AMPLIFY_EXCEPTION.md`
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
failing is *not* ES failing. *(z56.)* Two further independent engines (`Z56_FAMDESIGN.md` §4.3 decider, `Z56_PRIMET1.md` §4.2
sieve) reproduce exactly these 14 zeros and find none in (8 813 281, 10¹⁰]; their cross-reviews checked stored outputs and
samples, not a full 10¹⁰ rerun.

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

*(z57, `Z57_SYNTH.md`; two internal hostile reviews + cross-model review ACCEPT-WITH-FIXES; `Z57_SUMMARY.md` §1.)*
**The minimal missing statement (MS) for the (★) route.**
* **(MS)** *For every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 := {1, 121, 169, 289, 361, 529} there is an integer d ≥ 3,
  d ≡ 3 (mod 4), such that r = (−p mod d) ∈ {1, …, d − 1} divides (d + 1)/4* (necessarily d ≤ (4p + 1)/3; d must be
  positive). For a prime p this is equivalent to R(p) ≥ 1, i.e. to X(p) > −M_gen(p) (PROVED; Lemma A.1, essentially
  `Z56_FAMTRY.md` Lemmas 1.1–1.4, and Lemma 1.2).
* **(MS) ⟹ ES** (PROVED relative to Mordell's classical reduction to p mod 840 ∈ 𝔐 and Salez's verification of ES for
  n ≤ 10¹⁷, whose §§4.1–4.3 the cross-review checked; not a fresh certification below 10¹⁷). Threshold 10¹⁰ also
  suffices relative to the internal censuses (§2.1: no (★) zero at primes p ≡ 1 (4) in (8 813 281, 10¹⁰]; the (★) ∪ b = 1
  union has no zero at primes p ≡ 1 (4) ≤ 10⁸).
* Scope: *sufficient, not necessary* (ES could be proved via other Type II lines, Type I, or a non-counting argument).
  "Weakest sufficient target among the (★) subfamily-positivity statements" is Assessment, restricted to that menu; no
  strict separation of the eventual statements is claimed. The proved main terms do not weaken (MS) logically. By this
  route (MS) is needed at *every* p > 10¹⁷: an eventual statement with unspecified or astronomical p₀ does not finish ES
  (a statement about this route, not a necessity theorem).
* **Ladder (Prop 1.1, PROVED; rungs are statements for primes p > P in 𝔐).** L2 = (MS): R ≥ 1. L3: R_𝔊* ≥ 1.
  L3′: R_odd ≥ 1 (C odd). L3″: R₈ ≥ 1 (C even; the c = 1 line of 8/p, §4 item 2). L4: R_H3 ≥ 1 (complete levels
  64C³ ≤ p). L5: X_𝔊* ≥ −(1 − ε)M_𝔊*, fixed 0 < ε < 1. L6(η): X(p) ≥ −(5/(4π²) − η)L², fixed η > 0, L = log p.
  Arrows: L4 ⟹ L3 ⟹ L2; L3′ ⟹ L2; L3″ ⟹ L2; L5 ⟹ L3 wherever M_𝔊*(p) > 0; L6(η) ⟹ R(p) ≥ ηL²/2 > 0 for
  p ≥ p_V(η) (Thm V). **No arrow L6 ⟹ L5 or L5 ⟹ L4 is claimed.** Data at P = 10¹⁰: L2, L3 consistent; L3″ false
  (CERTIFIED, §4 item 2); L4 at risk (model; 873 zeros ≤ 10¹⁰, last 9 466 909 909); L5, L6 not refuted (L5 needs
  P ≥ 564 661 441, being false at every 𝔊*-zero with M_𝔊* > 0).
* Uniform diagnostic (EVIDENCE; long-double evaluation of exact finite genus sums): the η = 0 form X ≥ −(5/(4π²))L²
  fails at 7 of the 334 primes p ≡ 1 (4) in (10⁷, 10⁸] with R(p) ≤ 8, all outside 𝔐; it holds at all 249 tested
  Mordell-class primes (closest +0.0064 L²), where M_gen/L² has mean 0.117 < 5/(4π²). The count is a lower bound (R > 8
  untested). No eventual statement is refuted.
* Effectivity (Assessment: hypothetical Burgess envelope plus fitted zero-tail models; `Z57_SYNTH.md` §3.I). Lemma E1
  (PROVED): on a Theorem-V slice at Burgess margin μ the optimised Burgess bound saves at most p^{−μ²/(1+a)} — for the
  worst allowed conductor in this single Burgess bound expression, not a bound on true cancellation, at smaller actual
  conductors, or for other arguments. For uniform-margin subfamilies F_μ ⊂ 𝔊*_{1/15} (fits on all primes p ≡ 1 (4) in
  [10⁵, 10⁸], Mordell-domain refit as diagnostic): at 50 % of the Burgess-only area the (K, k) = (1, 2) envelope
  crossover is ≈ 10^{39.3} and the fitted zero crossover x* ≈ 10^{23.9} (Mordell domain 10^{23.3}); at 79 % they are
  ≈ 10^{162.8} and x* ≈ 10^{14.4}. Conditionally on monotone model tails, max(envelope crossover, x*) ≳ 10^{23} for every
  uniform-margin family. These are envelope crossovers and model extrapolations, not lower bounds on the threshold of any
  actual theorem. No z53–z56 input controls the remainder X with explicit constants. Also `Z57_BFO.md` §4.2 (Assessment):
  even with constant 1 in Burgess, the relative bound at length q^{1/3} is 0.995 at q = 10¹⁰, so Theorem V's architecture
  as written does not give p₀ ≤ 10¹⁰ (a calibration of the displayed model bound, not a theorem about every Burgess-based
  argument).

*(z58, sixteen lanes on (MS), each with internal hostile review and a cross-model review, all ACCEPT-WITH-FIXES with the
fixes applied and not re-reviewed; `Z58_SUMMARY.md`.)* **(MS) remains open; no HOT LEAD; B2 did not move.** New data and
targets for this section:
* **Census extensions** (CERTIFIED; `Z58_SUMMARY.md` §3).
  * **(★) holds at every prime p ∈ 𝔐 with 10¹⁰ < p ≤ 3·10¹¹**: 355 096 166 primes (`Z58_TRYO.md` §8.6). One
    engine; the cross-review checked 8 732 primes in independent slices. This certifies full (★), not R₈ or R_𝔊*.
  * **Zeros of R on 𝔐, all non-square n ≤ 10¹¹** (`Z58_LADDER.md` §3): exactly 9 primes (the in-𝔐 (★)-zeros, the
    last 8 813 281) and 18 composites, the last 17 401 609 = 47·370 247. None among the 128 491 751 primes and
    585 009 682 non-square composites in 𝔐 ∩ (10⁸, 10¹¹]. One engine; the cross-review decided 42 832 inputs pointwise.
  * `Z58_LOGIC.md` §4 independently sieves this to 10¹⁰: two implementations agree to 4·10⁹.
* **CONJECTURE (MS⁺)** (`Z58_LOGIC.md` §4): *R(n) ≥ 1 for every non-square n > 17 401 609 with n mod 840 ∈ 𝔐.*
  * It is primality-blind on 𝔐, and MS⁺(P) ⟹ (MS) for P ≤ 10¹⁷.
  * It is consistent with the censuses to 10¹¹ (z59: to 10¹², below). In 𝔐 on [10⁷, 10⁸], mean R/L² is 0.1189 for composites against 0.1246 for
    primes (CERTIFIED means).
  * Finite data do not establish it, and do not show that 𝔐 is necessary.
* **CONJECTURE CONV-II** (`Z58_WILDCARD.md` §1): *every odd non-square n ≥ 3 other than n = 4545 has N_II(n) ≥ 1*, where
  N_II(n) = #{(a, b, c, d) ∈ ℕ⁴ : 4abcd = a + b + nc}.
  * Status: CERTIFIED for n ≤ 10¹⁰; PROVED for n ≡ 3 (4).
  * The prime form (MS-II), N_II(p) ≥ 1 for primes p > 10¹⁷ in 𝔐, is implied by (MS) and implies ES relative to
    Mordell + Salez.
  * At the z58 checkpoint this was singled out as the only carried target whose *statement* passes F1–F4 (§4) in the
    tested ranges: a "HOT TARGET" (Assessment about the statement), **not a mechanism**. z59 adds the smaller-family
    CONJECTURE U_II with explicit exceptions {105, 4545} and its sharper census/profile (below; §7 item 19).
  * 4545 = 3²·5·101 is a genuine positive-integral Hasse failure with a nonempty BM set (`Z58_STRUCT2.md` Thm 4.1,
    PROVED + CERTIFIED).
* **Proved surrogate lower bounds, not bounds for R.**
  * `Z58_TRYF2.md` Thm A (PROVED): M₂(p) ≥ c₀ log²p for every prime p ≡ 1 (4), p ≥ p₀ (c₀ = 1/300 works). Here
    M₂ = Σ_C 4m_{2,C}/φ(4C) and R = M₂ + E₂ tautologically. What is missing is exactly E₂ > −M₂ pointwise.
  * `Z58_TRYF.md` Thm 2.1 (PROVED, Burgess; asymptotic, for primes p ≡ 1 (4); in the source's form: for every
    ε ∈ (0, 1/8), p ≥ p₀(ε) and 3 ≤ X ≤ 2p). The Jacobi layer L₂ of the character expansion satisfies
    |L₂| ≤ (1/64 + o(1))log²p against L₀ = (1/8)log²p + O(log p). No numerical onset is evaluated.
  * Thm 3.2 (CONDITIONAL): (★) for all sufficiently large primes p ≡ 1 (24), assuming HCE(δ) for a fixed δ > 0 at all
    sufficiently large such primes. HCE is a non-standard lower bound on L_r + L_n, stronger than the target. Of the
    twelve original R₈ zeros, only six lie in its 1 mod 24 domain.
  * For n = m², on the unit-restricted sum gcd(d, m) = 1, the Jacobi layer cancels the principal layer termwise;
    non-unit d cannot be hits and are excluded.
* **Least witness** (`Z58_WITNESS.md`; CERTIFIED). Every prime p ≡ 1 (4) ≤ 10¹⁰ with R(p) ≥ 1 has a solution with
  min(u, B, C) ≤ 201, and ≤ 0.52 log²p. CONJECTURE W: every prime p ≡ 1 (4), p > 8 813 281, has a (★) solution with
  min(u, B, C) ≤ (log p)². W ⟹ (MS).

*(z59, five math lanes on the z58 survivors, each with internal hostile review and a cross-model review, all
ACCEPT-WITH-FIXES with the fixes applied and not re-reviewed; `Z59_SUMMARY.md`.)* **(MS), (MS⁺), CONV-II remain open; no
HOT LEAD; B2 did not move.** New data and sharper targets:
* **(MS⁺) census to 10¹²** (`Z59_MSPLUS.md` §6; CERTIFIED, one engine = the z58 LADDER decider). No zero among the
  1 046 544 177 primes and 5 381 870 962 non-square composites in 𝔐 ∩ (10¹¹, 10¹²]. So the non-square R-zeros on 𝔐 up to
  10¹² are exactly the 9 primes and 18 composites ending at 17 401 609. Cross-review: chunk reconciliation, an
  independent-engine slice, the extremal input; no second full-range engine.
* **Primality-free variants** (`Z59_MSPLUS.md` §1, §5.3; CONJECTURE; CERTIFIED to 10¹⁰ via the z58 LOGIC census).
  * **(MS⁺₁₀₅):** R(n) ≥ 1 for every non-square n ≡ 1 (4) with gcd(n, 105) = 1 and n > 29 210 401 (all classes, no
    Mordell input). Strictly stronger than (MS⁺) (which it implies with the finite range to 29 210 401, covered by census).
  * **(R⁺_y), y ≥ 47:** R(n) ≥ 1 for every non-square n ≡ 1 (4) > 8 813 281 with all prime factors > y. For y = 47 there
    are 19 such zeros ≤ 10¹⁰, the last 8 813 281 = the last (★)-zero prime; for y > 47 the domain shrinks, so the same
    cutoff is certified sufficient (count and actual last zero may differ).
  * Reusing an (MS) proof for fixed-y-rough non-squares requires every primality-dependent step to remain valid (fixed-y
    roughness does not force gcd(n, u) = 1 for witnesses: n = 9 553 913 = 1093·8741 has witness (1093, 2186, 1)). This
    initially gives only the Mordell domain and the threshold 10¹⁷. The all-class (R⁺_y) additionally needs removal of any
    Mordell-class dependence and coverage down to 8 813 281; the census to 10¹⁰ does not cover a gap up to 10¹⁷. A proof
    needing y(n) → ∞ is not a proof of (R⁺₄₇).
  * "As good a target as (MS⁺)" is an Assessment. All variants inherit T1 by hypothesis, and R₈ has the same odd local
    factors (half the leading mean).
* **Local mean of R** (`Z59_MSPLUS.md` Thm 1, Remark 2.3; PROVED). For fixed Q = 2^k·Q′ (k ≥ 2, Q′ odd squarefree) and
  a ≡ 1 (4), the class mean is (𝔖_Q(a)/8)log²X + O_Q(log X), 𝔖_Q = ∏_{q|Q′}σ_q with σ_q = 1 + 1/q² (q ∤ a),
  1 − 1/q + 1/q² (q | a); 2-adic factor 1. So the leading term is Jacobi-blind (𝔐 differs from other unit classes only
  at O(log X); the size of that term is not derived — the proposed second-order expansion was WITHDRAWN after review),
  each odd q | n multiplies the leading constant by (q² − q + 1)/(q² + 1) (dead moduli), and R₈ has the same odd
  local factors and exactly half the leading coefficient.
  EVIDENCE: zero law P(R(n) = 0) ≈ exp(−0.3·m(n)), fitted with the proxy m, log n and Jacobi depth as separate
  covariates. Agreement within ≈ 1.5× (worst ≈ 1.63×) concerns the four large *training* groups only; the OOS 21 | n row
  is ≈ 3× off and held-out g7 ≈ 17× off. Later total counts are ≈ 1.4–1.5× low (pre-registered decade [10¹⁰, 10¹¹]:
  18 observed vs 13.0 / 11.5; no pass criterion, not a passed test), and the 𝔐-prime zeros of 10⁶–10⁷ ≈ 6× low
  (unexplained). The R₈ comparison (≈ 5× the R-law at the halved mean) is a rough all-p ≡ 1 (4) Assessment, not an
  in-𝔐 calibrated law; only four of the twelve screen R₈ primes are in 𝔐.
* **CONJECTURE U_II** (`Z59_CONV2.md` §1, where it is called U). U_II := (c = 1) ∪ (a = 1) ⊂ Type II; (MS-U) is its prime
  conjecture label. *U_II is not the older word-family predicate U of the U/ES₅ and RLD-U passages (§§5–7): at n = 4545
  the old U has the word (t, u, v) = (7, 14, 47), while U_II has no witness; old-U theorems are not theorems about U_II.* Lemma 1(iii) (PROVED): U_II(n) ≥ 1 ⟺ ∃ T ≥ 1 such
  that Tn + 1 has a divisor f ≡ −1 (mod L_T), L_T = T if 4 | T, 4T otherwise — **a single one-parameter line** (the a = 1
  half is the known "cn + 1 mod 4c" form). CONJECTURE: every odd non-square n ∉ {105, 4545} has U_II(n) ≥ 1.
  * CERTIFIED for n ≤ 10¹⁰ (zeros exactly 105, 4545; previously to 4·10⁶). Independent direct census to 10⁹; one engine
    above. No prime U_II-zero ≤ 10¹¹ (inherited from the B1_LINE a = 1 census, not recomputed).
  * At primes it is López's Conjecture 1 (prior). U_II ⟹ CONV-II (105 = full-family solution (3, 3, 2, 3)).
    **(MS-U)**: U_II(p) ≥ 1 for primes p > 10¹⁷ in 𝔐; (MS) ⟹ (MS-U) ⟹ (MS-II), so (MS-U) ⟹ ES rel. Mordell + Salez.
  * U_II asks for more than CONV-II; that it is harder to prove is *not* claimed. In the certified range the full family
    beyond U_II is needed only at n = 105; the a = 1 branch of U_II itself uses c ≥ 2.
  * Numerator 8: U_II⁽⁸⁾ has 819 odd non-square zeros ≤ 10⁸ (61 primes, last 3 869 153; 758 composites, last 93 398 595).
* **Minimal ρ for Type II at p ≡ 1 (24)** (`Z59_CONVO.md` §6; CERTIFIED, independently reproduced). With ρ = 4abd − p,
  every prime p ≡ 1 (24) ≤ 10⁸ (719 781 primes) has a witness with ρ ≤ 107 (record 8 803 369 → 107). Under Dickson no
  uniform bound on ρ suffices (Thm 7.7, CONDITIONAL; exact prior result `DISPROOF_AVENUES.md` §3 Prop 3.1).

*(z60, eight lanes — LOPEZ, LOPEZT, MS105, MS105T, SIGNED, RAYCLASS, DYNAMICS, TRACE — each with internal hostile review and a
cross-model review, all ACCEPT-WITH-FIXES with the fixes applied and not re-reviewed; `Z60_SUMMARY.md`.)* **(MS), (MS⁺),
(MS⁺₁₀₅), U_II, (MS-U), CONV-II remain open; no HOT LEAD; B2 did not move.** New data and one sharper target:
* **CONJECTURE U₇** (`Z60_LOPEZ.md` §4.2, Lemma 7). U₇(n): some f ≡ 7 (mod 8) has (−n mod f) | f + 1 ⟺ n has a word
  with 8 | xy ⟺ some gn + 1 has a divisor ≡ −1 (mod lcm(8, g)) (PROVED equivalences). Sign-free (no Jacobi filter, no branch
  split); U₇(m²) = 0 for odd m; U₇ holds on every n ≡ 3 (4); on n ≡ 1 (4), (★) ⊂ U₇ ⊂ U_II and U₇ = (★) ∪ (A-line words
  with cd even) (the A-line agrees with López Type A at primes, not at arbitrary composites); U⁽⁸⁾ ⊂ U₇. CONJECTURE: every odd non-square n ∉ Z₇ := {105, 1465, 3865, 4545, 10305, 12145, 39361, 67425} has
  U₇(n). CERTIFIED (`scripts/z60_lopez_u7.c`): the odd non-square U₇-zeros ≤ 10¹⁰ are exactly Z₇ — among odd non-squares
  n ≤ 10⁸ the zeros are exactly Z₇ (the 4999 odd squares are zeros by T1, skipped), and there is no non-square zero with
  n ≡ 1 (4) in (10⁸, 10¹⁰];
  no zero among the 7 071 222 859 non-square n ∈ 𝔐 ∩ (10¹⁰, 10¹²]. Independent word enumeration ≤ 10⁶, LATE-certificate and
  random-input checks; above 10⁶ one engine. (MS) ⟹ (MS-U₇) ⟹ (MS-U) ⟹ (MS-II) are implications; strictness is not claimed,
  and "sharper" does not mean easier (U₇ has 8 zeros, U_II 2). The union (★) ∪ (A-line with f ≡ 3 (8)) leaves 42
  non-square zeros with n ≡ 1 (4), n ≤ 10⁷, including the sole prime 9601.
* **López branches at hard primes** (`Z60_LOPEZ.md` §3; counts CERTIFIED, reading EVIDENCE, one engine). On all 6 354 932
  primes p ≡ 1 (24) ≤ 10⁹ the two U_II branches' least witnesses are *positively* dependent in the deep tails (99–99.9 %;
  1.2–5.9× conditional independence after stratification, up to 16× raw; 59–107 joint events at the deepest a/f thresholds,
  only 10 in the T-coordinate, so the extreme-tail ratios are rough) and weakly negatively dependent in the bulk (≈ 94 %:
  0.81–0.95). In the modulus coordinate, for each fixed X, the truncated branch vectors are exchangeable in the *limiting* prime
  distribution over 𝔐-primes or p ≡ 1 (24) (Prop E, PROVED; not exact finite-sample symmetry, independence, uniformity in
  growing X, or same-prime rescue). Pooled ratios do not imply positive dependence in every stratum; causal readings are
  hypotheses.
* **Least López witness** (`Z60_LOPEZT.md` §3.1; CERTIFIED). Over the 719 781 primes p ≡ 1 (24) < 10⁸ the least witness
  modulus g* of the union is ≤ 10487 (at p = 9 658 489); g* = 7 for 50.06 %; g* ≥ (1/5 − o(1)) log p infinitely often (PROVED).
* **Near-square threat to (MS⁺₁₀₅)** (`Z60_MS105.md` §2; CERTIFIED first-hit searches, one engine per run, bounded replays
  by the cross-review). Every non-square n = s·m² ≡ 1 (4), gcd(n, 105) = 1, s·m² < 2⁶⁴ with squarefree kernel s ≤ 10⁵ has
  R(n) ≥ 1 except the 16 known zeros < 10⁶ (67 872 056 404 inputs, 11 061 kernels). High-m windows on the 106 admissible
  kernels s ≤ 1000 contain 3 876 571 898 inputs to n ≈ 10³⁷, with no UNK. Near squares m² + c, c ∈ ±{8, 16, …, 200}, odd
  m ≤ 10⁹, restricted to positive non-squares coprime to 105, have UNK only at 15 known zeros ≤ 1.26·10⁷. Among all 52 Lehmer
  pseudosquares ≤ 4.24·10²⁴ only 2641 and 18 001 are zeros. The sampled locally-square inputs to ≈ 4·10³⁵ have no UNK.
  Windows and samples are not interval completeness to the largest n quoted; ≈ 8.3·10¹⁰ counts input occurrences.
  **(MS⁺₁₀₅) is not refuted.** EVIDENCE: maximal square-mimicry only lowers mean hit counts (≈ 30 % pseudosquares,
  ≈ 11–17 % locally square). The R₈ control covers the 106 admissible kernels s ≤ 1000 and 6 086 436 506 inputs (not the
  expanded kernel-≤ 10⁵ domain); it leaves 281 UNK above 10¹⁰, up to 1.84·10¹⁹ (no C-even witness d ≤ 10⁸; not certified
  zeros). R has no UNK above 10⁶ on this domain, or on its larger census.
* **Cover of (MS⁺₁₀₅)-type classes** (`Z60_MS105T.md` Thm 4.1; CERTIFIED, independently reproduced). Every n ≡ 1 (4),
  gcd(n, 105) = 1, n ≥ 1 441 440, outside 6275 of the 164 736 such classes mod 1 441 440 has R(n) ≥ 1 (3024 of the 6275
  uncovered classes are square classes). For n ≡ 1 (4), n ≤ 3·10⁷: 361 non-square R-zeros and 2739 odd squares;
  38 non-square zeros are coprime to 105 (14 primes, 24 composites).
  Fixed covers cannot finish (§3 z60).
* **Single-field family S₁** (`Z60_RAYCLASS.md` §6; CERTIFIED, one engine). S₁(n) = #{(a, b, c) : 4abc = a + b + nc} (Type II
  with d = 1) has 160 prime zeros p ≡ 1 (4) ≤ 10⁷ (25 in 𝔐), although it rescues all 14 (★)-zero primes — this refutes all-prime
  positivity of S₁ only; eventual S₁ positivity remains open. EVIDENCE (7 254 primes p ≡ 1 (4) in [10⁶, 1.2·10⁶]): the Spearman
  correlation of S₁ with L(1, χ₋₄ₚ) is 0.875; the part of R at levels C that are not squares (t₀ > 1) has correlation 0.053
  (p-value ≈ 5.9·10⁻⁶: small but non-zero; "uncorrelated" is descriptive), while all of R has correlation 0.426.

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

**(z58) Scoped no-gos from the (MS) probe** (`Z58_SUMMARY.md` §1). Each item is a theorem about a *specified class of
objects or arguments*. None is a necessity theorem for every proof, and none proves or refutes (MS).
* **Fixed-level Hecke proxies** (`Z58_AUTOMORPH.md` Thm A, Cor A1).
  * Setting: 𝓗_M, functions on (n, M) = 1 given by fixed finite combinations of holomorphic newform/Eisenstein eigenvalue
    systems of integral weight k ≥ 1 and level dividing M, their n^j-twists (j ≥ 0 integer), and the specified
    character-weighted real-parameter divisor sums with finitely many derivatives. Not all GL₂ automorphic systems.
  * Thm A (PROVED relative to Deligne/Deligne–Serre, purity and Chebotarev), at odd primes p ∤ M: if
    a(1) = a(p²) = a(p⁴) = … = 0 and the Satake multiset at p has no pair γ, −γ, then a(p^m) = 0 for all m.
    Collision-freeness holds at a positive-density set of primes, all ≡ 1 (mod 840), which depends on the chosen
    combination; no common positive-density set for all 𝓗 is asserted. For all-Eisenstein a, it holds at every
    p ≡ 1 (mod lcm(L, 840)).
  * Cor A1: no a ∈ 𝓗_M is both valid (a(n) ≠ 0 ⟹ R(n) ≥ 1 for every n ≡ 1 (4) coprime to M) and effective (a(p) ≠ 0
    at every sufficiently large 𝔐-prime in the domain); no a ∈ 𝓗_M equals R on all n ≡ 1 (4) coprime to M.
  * Not covered: prime-only support/equality, which does not provide square vanishing and is not excluded by this
    theorem; prime-only arguments whose error lies outside 𝓗. These are escapes E1 (half-integral weight), E2
    (coefficients outside 𝓗, e.g. variable-level sums) and E3 (higher depth / non-GL₂), plus signed minorants.
* **Ternary theta proxies lose the genus term on 𝔐** (`Z58_TERNARY.md` Thm F, Cor F1).
  * Thm F (PROVED relative to (S1)–(S5): Siegel, Duke–Schulze-Pillot, unary/U^⊥ decomposition, Shimura T(ℓ²)). Let
    g ∈ M_{3/2}(Γ₀(4N), ψ) be a combination of positive-definite ternary theta series (one rational determinant square
    class) plus a cusp form. If g(ℓ²) = 0 for all large primes ℓ, then the genus part E vanishes on
    𝒞₁(2N) = {n : n ∈ (ℤ_ℓ^×)² ∀ℓ | 2N}, and g(p) = h⊥(p) (cusp, orthogonal to unary thetas) at primes p ∈ 𝒞₁(2N).
  * Cor F1 (PROVED): the squares of (ℤ/840)^× are exactly 𝔐. So if the odd primes of N lie in {3, 5, 7}, a valid proxy
    has no genus main term at any 𝔐-prime p ∤ N.
  * Scope: one nebentypus, genus-theta combinations, the unit class; prime-only support (no square vanishing) is not
    covered. The square obstruction applies at the identity's own
    modulus; finer-modulus identities and off-𝒞₁ classes are not excluded.
  * What survives is the cusp route. A single eigenform needs Waldspurger nonvanishing (open, Goldfeld-type, when the
    root number is +1), or a new thin-set Heegner-incidence theorem (E1′).
* **Positive-integral Brauer–Manin detects exactly non-squareness on the (★) and Type II models** (`Z58_STRUCT.md` Thm A,
  `Z58_STRUCT2.md` Thm B; PROVED).
  * Both S_n : 4uBC − u − B = n and X_n : 4abcd = a + b + nc have Br/Br(ℚ) ≅ ℤ/2 (a transcendental quaternion class),
    π₁ = 1 and étale-BM = BM.
  * For n ≥ 1, the positive-integral BM set (real region u, B, C > 0, resp. a, b, c, d > 0; displayed ℤ-models) is
    **empty iff n is a square** for numerator 4, and iff n ∈ □ ∪ 2□ for numerator 8. Without the positivity
    restriction these models have integral points at every n.
  * Cor A′ (S_n): BM (even étale-BM) nonemptiness does not give a positive integral point. This fails at the 14 (★)-zero
    primes and the 285 composites, and on the C-even model at the 1 270 R₈-zero primes ≤ 10⁸ and the 12 in [10¹⁰, 1.1·10¹⁰].
    Primality alone does not rescue it.
  * X_n: 4545 has a nonempty BM set and local points (also under ET coprimality) but N_II(4545) = 0 (Thm 4.1). An argument
    using only BM-nonemptiness plus primality, π₁, Br, local solvability and smoothness is refuted at the listed
    parameters if it transfers verbatim to the specified fixed open-closed local classes (CERTIFIED class table).
  * Not covered: further hypotheses, eventual positivity above a larger threshold, the open S°, fibre arithmetic.
  * Contrast with BL (§1): on the all-solution ES surface U_n the BM set is nonempty for n ≥ 2. On the displayed (★)
    surface and Type II threefold, positive-integral BM obstructs exactly the squares (numerator 8: □ ∪ 2□), but
    nonemptiness is not sufficient for a positive integral point.
* **Mordell case splits** (`Z58_MORDELL.md`).
  * Lemma P (PROVED): if nonzero U, B, C ∈ ℚ[t] satisfy 4UBC − U − B = a + Mt identically, with integers a and M ≥ 1,
    then two coordinates are constant. When they give positive-integral certificates, the family is contained in one
    H_d residue or one K_{u,B} class. Arbitrary one-parameter algorithms and rational or piecewise families are not
    covered.
  * Thms S1/S3 and the exact B criterion (PROVED): explicit sterility of the 1-points x_{ℓ,R}; sterile for every
    R ≤ (ℓ − 1)/2.
  * Cor S2 (PROVED, with Dirichlet): let ℓ be an odd prime and M ≥ 1 with ℓ ∤ M. Then every finite union of H_d and
    K_{u,B} classes misses infinitely many primes p ≡ 1 (mod M), p ≡ R (mod ℓ), at non-residues R with x_{ℓ,R} sterile. At M = 840 this applies to class 1; the other five Mordell
    classes are open.
  * Prop C1 (PROVED): polynomial certificates U, B, C ∈ ℚ[x, y] for a degree-2 f with irreducible top form (e.g.
    x² + 840y²) satisfying 4UBC − U − B = f have two constant coordinates. The congruence interpretation (validity is
    then a fixed-modulus congruence on p = f(x, y)) assumes the constant coordinates are positive integers and the
    identity supplies a positive-integral solution at some point with f > 0. Not covered: rational, piecewise or
    divisor uses of (x, y).
* **Function-field analogue** (`Z58_FFIELD.md`; an analogy, not a reduction).
  * Cor 3.2 (PROVED relative to Chebotarev): no fixed N₀ gives MS_q(N₀) for all q ≡ 3 (4). So fixed-degree, large-q
    positivity is impossible and any threshold must grow, N₀(q) → ∞.
  * Prop 3.3 (PROVED relative to function-field RH): witness menus d | M with deg M ≤ (1/2 − δ)n leave ≫ q^n/(n 2^{ω(M)})
    avoiders. A sufficient range, not a sharp barrier.
  * Prop 3.1 (PROVED): local word counts at ℓ ∤ f are residue-blind, also over ℤ.
  * Fixed-q methods are not excluded.
* **Bounded coordinates** (PROVED unless marked).
  * `Z58_TRYF2.md` Prop 2.1: for every U, every prime p ≡ 1 (mod 840·L_U) has no hit with two coordinates ≤ U. A fixed
    finite u with B, C unbounded is not excluded.
  * `Z58_WITNESS.md` Prop 3.1 (CONDITIONAL on Dickson): for every S, infinitely many p ≡ 1 (840) have min(u, B, C) > S.
    Fixed-congruence selectors p mod M ↦ (d or (u, C)) fail on 𝔐 (PROVED).
  * `Z58_LOGIC.md` Prop 5.4: polylog (u, C)/(B, C) menus fail i.o. (modulo the OMEGA13 cited inputs); growing polylog
    (u, B) menus are open.
  * `Z58_LADDER.md` Cor 1.3: no bounded D works for SC(D). Prop 1.2: SC(D) with D ≤ p^θ, θ < 1/(4√e), would give a
    beyond-Burgess n_p bound on 𝔐. Lemma 3.1: R^{(k)}(m₀²) = 0 for every odd m₀ at every exponent cap k ≤ ∞.
* **Logic** (`Z58_LOGIC.md`).
  * Prop 2.1 (PROVED): (MS) is Π⁰₁, so a counterexample p gives a brute-force Q-refutation of length p^{O(1)} (not a
    known poly(log p)-length refutation), and independence from PA/ZFC would imply truth. For a class-restricted rung
    the zero must belong to its domain.
  * Thm 3.1 (PROVED relative to Buss witnessing): S¹₂ ⊢ (MS) yields a polynomial-time hit-or-nontrivial-factor-pair
    algorithm on n > 10¹⁷ with n mod 840 ∈ 𝔐. It must find hits at those primes and split any composite R-zeros in that
    domain. This is neither a general factoring algorithm nor a complete-factorisation guarantee.
  * Thm 6.2 (PROVED): IOpen ⊬ MS⁺★(P) for every numeral P (pseudo-squares n₀ + 840t, Shepherdson's model); CONDITIONAL
    on (MS) for the version with (MS★) added. This is a weak-theory barrier, not a general proof-method barrier.
* **Type II structure** (`Z58_WILDCARD.md` Lemmas 4.1–4.4, PROVED).
  * Numerator nesting: N^{(8)} is the d-even half of N_II.
  * Twisted T1: for K ≡ 0 (mod 4), N^{(K)}(s·m²) = 0 for every odd s | K/4 and every odd m.
  * Inheritance to multiples is conditional on divisibility (N_II(5) > 0, N_II(4545) = 0).
  * Odd N_II-zeros n ≡ 1 (4) have (n + 1)/2, n + 4 and 4n + 1 composed of primes ≡ 1 (4).

**(z59) Scoped no-gos from the survivor probe** (`Z59_SUMMARY.md` §1). Same reading as the z58 block: theorems about
specified classes, none a necessity theorem for every proof, none proves or refutes (MS).
* **The Waldspurger residue of ternary-theta proxies** (`Z59_WALDS.md` §3–§4).
  * Thm W1 (PROVED rel. Waldspurger 1981 Prop 1 / Cor 2, Shimura's T(ℓ²) formula, TERNARY Thm F). Let
    g ∈ M_{3/2}(Γ₀(4N), ψ) be a ternary-theta proxy (one quadratic ψ) with g(m²) = 0 for every m built from primes > ℓ₀
    (every valid proxy). Then every Shimura component has g_φ(1) = 0, and at squarefree t ∈ 𝒞₁(2N), t > 1,
    g(t) = Σ g_φ(t) over the **Gauss-exceptional** φ only: those whose twist G_φ = φ ⊗ ψχ₋₄ has L(G_φ, ½) = 0. T1 pins
    a(1); Waldspurger carries it to the whole square class. Cor W2: no Gauss-exceptional φ ⟹ g vanishes on squarefree 𝒞₁.
  * Lemma W1′ (PROVED rel. Cor 2): each φ with an L-non-zero anchor in 𝒞₁ (or satisfying Waldspurger's (H2)) gives at most
    one line on squarefree 𝒞₁. Prop W4: for p ∈ 𝒞₁(2N), a non-zero single-eigensystem restriction has g(p) ≠ 0 iff
    L(½, G_φ ⊗ χ_p) ≠ 0, under W1′'s L-non-zero anchor hypothesis (with non-zero coefficient restriction), or under (H2)
    with K_φ(g) ≠ 0. Only if g is valid does g(p) ≠ 0 force R(p) > 0; for several contributing eigensystems under (H2),
    non-cancellation of the sum is required ((b)/(c) need (H2) for every contributing φ). The L-value controls g(p) ≠ 0,
    not the sign of g(p). (d): one non-zero value at a squarefree R-zero in 𝒞₁ makes a single-line proxy invalid.
    Remark W3: the root number is constant on 𝒞₁ (PROVED); vanishing of sign −1 coefficient components there needs (H2),
    else CONDITIONAL on (W-loc).
  * Prop W5 (PROVED, elementary): for g effective on a prime class 𝒞, eventual validity on 𝒞 is equivalent to eventual
    R(p) ≥ 1 on 𝒞 — a reformulation, not a circularity theorem. This does not by itself give (MS), which requires every
    𝔐-prime p > 10¹⁷: the effectiveness and validity thresholds must both be ≤ 10¹⁷, or the finite gap covered. Lemma W0 (PROVED rel. Thm F): a lattice of level 4N with r_L(ℓ²) = 0 for
    large ℓ represents no n ∈ 𝒞₁(2N); so termwise (★)-recipe lattices never reach the square class (any ψ, non-negative
    combinations).
  * CERTIFIED (exact, finite): at 24 levels L | 3360 and every ψ (121 (L, ψ) pairs), every valid proxy vanishes on
    𝒞₁ ∩ [1, B] (B ≈ 10⁴; full space, except L = 840, ψ ∈ {1, χ₈, χ₂₁}: TERNARY class only; χ₁₀₅, χ₈₄₀ full space to
    B = 8000). The 15 non-zero T1-kernels are non-zero at known R-zeros (5569, 9601, 23929; 1969, 2641, 5161).
  * PROVED: "L(G_φ ⊗ χ_p, ½) ≠ 0 at *every* p in the class" is false for the explicitly tested conductor-84 twist at
    (168, χ₁₆₈) (13 𝒞₁-primes, six in 𝔐: 1009, 1129, 1201, 1801, 4201, 4729); not a statement about every eigensystem.
    Eventual non-vanishing is unproved; GRH does not give it (Assessment). For rational G_φ (elliptic curves), a
    residue-class refinement of CKRS with a positive constant in the chosen class predicts infinitely many prime-twist
    zeros; this refinement is not stated in CKRS and is CONJECTURE; irrational eigensystems need a further extension.
  * Not excluded: (E-a) levels with several Gauss-exceptional φ plus a validity identity proved from independent input
    (none supplied); (E-b) coset thetas; (E-c) mixed ψ signed combinations; (E-d) higher half-integral weight; (E-e)
    off-𝒞₁ classes (for a termwise recipe-lattice strategy: growing/adaptive levels with some odd level prime ℓ,
    (p/ℓ) = −1, hence ℓ ≥ n_p — B2 / n_p wall; not a necessity theorem for arbitrary signed multi-eigensystem proxies).
* **Type II coordinate lines** (`Z59_CONV2.md` §§2–4; PROVED).
  * Prop 3.1: within one coordinate system, on a *shared* integer the c = 1 and a = 1 events are nested (T-system: for
    4 | T an a = 1 event on Tn + 1 is a (★) event; shift system: the reverse), so rescue there is one-directional; a (★)-zero
    is rescued by a = 1 only via 4 ∤ T. Not a statement about every coordinate system (n = 193, T = 8).
  * Prop 4.2: all c-line events on 4mn + 1 lie in the greatest event E_{r(m)} (r(m)² the largest square dividing m), whose
    union they are; incomparable c can rescue each other (m = 36).
  * Prop 4.1: equation-scaling transports (inheritance, numerator ladder, ET dilation, compositions) give no descent into
    a prime p (the source must be divisible by p); N_II(p)[k | c] = N^{(4k)}(pk), and no Type II solution at p has p | c.
  * Prop 2.1: Type II relaxes the tie on 4mp + 1 from 4m to ≥ 2√(4m) (never a bounded modulus). §3: fixed finite (T, f)
    menus fail on a congruence class (Z57_BFII Prop 3.2 argument). Adaptive or growing arguments across integers are not excluded.
* **Means and dead moduli** (`Z59_MSPLUS.md`). The fixed-Q leading residue-class coefficient of Thm 1 (§2.4 z59) is
  Jacobi-blind; R₈ has the same odd local factors and half the leading coefficient. These leading means alone supply
  neither non-square discrimination nor pointwise positivity (Assessment); square-sensitive main terms (e.g. M_BM, §2.2),
  other density inputs or additional arithmetic steps are not excluded. Lemma 4.1 (PROVED): for each fixed positive
  non-square s ≡ 1 (4), R(s m²) = 0 on a density-0 set of odd m; thin infinite zero subfamilies are not excluded (no positive-density twisted T1 for (★), unlike numerator K ≥ 8). Unconditional product / divisor /
  q²-scaling closures of R ≥ 1 fail (CERTIFIED: 12 538 801 = 517·24 253; 4545).
* **Witness constraints, rederived** (`Z59_CONVO.md`, `Z59_MSPF.md`; PROVED, largely prior: Z57_BFII, Z58_CONVF,
  JOINT_BUDGET, Z56_FAMTRY, Z57_SYNTH, Z58_WITNESS). Every hit modulus d of a non-square n ≡ 1 (4) has (d/n) = −1, hence
  d ≥ q₁(n) ≥ 11 on 𝔐; for every D infinitely many non-square n in every 𝔐-class have no witness d ≤ D (MSPF Lemma 1.8,
  an incremental strengthening). The one-character "escape ⟹ solution" implication for the ρ-ratio criterion is refuted
  by 4545 and at the prime 8 803 369 (CERTIFIED); other bounded-order character or congruence arguments are not excluded
  (p ≡ 73 mod 168 forces ρ = 7).

**(z60) Scoped no-gos from the clean-statement attack and three new generators** (`Z60_SUMMARY.md` §1). Same reading as
the z58/z59 blocks: theorems about specified classes, none a necessity theorem for every proof, none proves or refutes (MS).
* **Signed and multi-eigensystem automorphic proxies** (`Z60_SIGNED.md` §§2–5; PROVED rel. Siegel, Duke, Waldspurger 1981,
  Rankin–Selberg etc. as cited). A *signed minorant* is valid if g(n) > 0 ⟹ R(n) ≥ 1; T1 then gives only g(m²) ≤ 0.
  Scope: fixed-level theta-class proxies (finite real combinations of positive-lattice theta series plus cusp forms); there
  signed T1 forces either eventual negativity at all 𝒞₁-primes (a valid but useless minorant; the genus part need not vanish)
  or the support-form structure, with only Gauss-exceptional components on squarefree 𝒞₁. Non-genus Eisenstein / general
  polynomial-growth objects are not classified.
  * Thm S1 (weight 3/2, ternary-theta class, one quadratic ψ): if g(ℓ²) ≤ 0 at all large primes ℓ, then E(1) ≤ 0; E(1) < 0
    makes g(p) < 0 at every sufficiently large p ∈ 𝒞₁(2N) (ineffective); E(1) = 0 forces the genus part to vanish on 𝒞₁ and
    all Shimura anchors to vanish, so on squarefree t ∈ 𝒞₁, t > 1, only components with L(½, φ ⊗ ψχ₋₄) = 0 survive (recovers
    WALDS W1). Thm S2: the same for any finite mixture of quadratic ψ (support and signed forms), using squares m² of good
    squarefree m including composite m. Prop S3: weight ≥ 5/2, one ψ (mixed-ψ *support* extension also PROVED).
  * **Mixed ψ in weight ≥ 5/2, signed: the extension is FALSE** (PROVED counterexample at level 8, rank 5, A₁ = θ₁/10,
    A₂ = θ₂/8, g = A₂ − (3/2)A₁: g(m²) < 0 for every odd m, g(p) > 0 for every prime p ≡ 17 (24); off 𝔐, negative at all 53
    𝔐-primes ≤ 20 000; not shown valid, nor positive at all large 𝔐-primes). Non-quadratic nebentypus: Assessment only.
  * Cosets: genus conclusions CONDITIONAL on (SWc), for one underlying genus / determinant class, class by class only; no
    global or cusp dichotomy is proved; the termwise-recipe exclusion is also conditional on (SWc). Lemma S4 / Cor S4′ (S4′ CONDITIONAL on (Dom)): if g(n) = F(n)(1 + o(1))
    on n ≡ 1 (M) with F eventually non-zero of constant sign (S4′: an explicit dominant periodic term), and g(m²) ≤ 0 for large
    odd m, then g(p) < 0 at all large primes p ≡ 1 (M) — such exponential objects are square-blind.
  * Prop S5 (PROVED, elementary; support form): for a fixed finite-dimensional real space V, a valid support proxy effective
    at every large p ∈ 𝒞₁ exists iff S(p) ∉ W = span{S(z) : z ∈ 𝒞₁, R(z) = 0} for those p; generic real coefficients then
    avoid all prime cancellations. So **cancellation is not the obstruction**; what is missing is the non-degeneracy plus an
    independent validity mechanism (none known). Under W1′'s non-zero-L-anchor / (H2) hypotheses, with Λ the full
    span of the exceptional lines **and W = 0**, S(p) ∉ W becomes (𝒟_N): for every prime p ∈ 𝒞₁ above the stated threshold
    there exists an exceptional G_φ (possibly depending on p) with L(½, G_φ ⊗ χ_p) ≠ 0. In general the criterion is a linear
    condition on signed square roots of central values, not their mere non-vanishing; validity still needs an independent
    mechanism. Genericity does not transfer to rational
    coefficients or to the signed cone (common-K joint sign feasibility, unresolved).
  * CERTIFIED: at L = 168, 240, 280 every valid mixed-ψ support proxy vanishes on 𝒞₁ ∩ [1, B] (B = 40 000 / 30 000 / 30 000).
  * Not excluded: integral-weight signed proxies (AUTOMORPH B1); mixed-ψ signed in weight ≥ 5/2; off-𝒞₁ primes; varying /
    adaptive levels (open; for the termwise recipe-lattice / off-𝒞₁ strategy, reaching a hard prime outside the level's
    square class requires an odd level prime q with (p/q) = −1, hence q ≥ n_p — not a necessity theorem for arbitrary signed
    or multi-eigensystem proxies); non-quadratic characters; coset cusp parts; general mock /
    Rademacher objects where (Dom) fails; level sums; FJ / indefinite lifts (reductions only, Assessment).
* **No p-independent link law between the U_II branches** (`Z60_LOPEZ.md` Prop D). For every X there are infinitely many
  primes p ≡ 1 (mod 840) at which both branches fail at every witness modulus f ≤ X (PROVED, Dirichlet); in the shift and
  middle-letter coordinates CONDITIONAL on Dickson. One-sided laws are refuted at 5569 (B never fires, A at a = 2). Adaptive /
  p-dependent links and counting arguments are not excluded. Coupling lemma (PROVED): at p ≡ 1 (4) every witness of either
  branch has a prime factor ℓ with (ℓ/p) = −1.
* **Fixed witness menus and covers, again** (`Z60_LOPEZT.md` Lemma 1.2; `Z60_MS105T.md` Prop 3.1, Thm 3.2, Cor 3.3, Cor 3.4;
  PROVED, D-part prior: `Z55_HCF` Thm 3.1 / Cor 3.2–3.3). For every fixed M infinitely many primes p ≡ 1 (4), gcd(p, 105) = 1
  (resp. p ≡ 1 (24)) lie in no good class modulo divisors of M (resp. have no witness g ≤ M); for an odd prime q and a
  positive integer r with q ∤ r and q > 3r + 1, the profinite point x_q = r, x_ℓ = 1 for every prime ℓ ≠ q lies in no good class (∀ M ∃^∞ p — not one prime avoiding every M, not a zero). For every B
  infinitely many such primes have every solution with uk, kC, uC > B (not an existence statement). Growing / size-controlled
  searches are not excluded.
* **Polynomial zero families** (`Z60_MS105.md` Thm 3; PROVED rel. Hilbert irreducibility (Serre, Cohen) and Chebotarev). For
  f ∈ ℤ[t] non-constant with positive leading coefficient: if f = g², g ∈ ℚ[t], then R(f(t)) = 0 whenever g(t) is an odd
  integer; otherwise {t : R(f(t)) = 0} has natural density 0. No positive-density zero family along a non-square univariate
  polynomial; not finiteness, not sporadic zeros, univariate only (compositions can create squares). Holds for R₈ unless f or
  2f is a square. Twisted T1 (Lemma 1, PROVED): for n = s·m² every solution has s ∤ uC, s ∤ BC. Prop 4: for d ≡ 3 (4), if a and
  b are both d-form hits at the same d, ab is not a hit there; more generally, for gcd(ab, d) = 1, a product hit requires
  (a/d)(b/d) = −1 (necessary, not sufficient; no obstruction to all conditional gluing / descent); unconditional scaling ascent fails (12 538 801).
* **Ray-class / class-number information in one field** (`Z60_RAYCLASS.md`; PROVED). Lemma 1: (★), the a = 1 line and full
  Type II are ideal-divisor events of β_r = 1 + r√(−t₀n) with norm ≡ −1 modulo t₀r², 4t₀r², 2t₀r (orders containing β_r; for (★) at
  C = t₀s², r = 2s, the norm modulus is 4C = t₀r²).
  Cor 2.1: for n = s·m², no (★) hit at levels C with s | C (for primes this kills only C ≥ n). Prop 3.1 (standard CFT): for
  prime n = p with p ∤ 4C, the indicator [N𝔞 ≡ −1 (mod 4C)] on all ideals coprime to the modulus and conductor can be
  class-determined in some order only if C ∈ {1, 2, 3, 6} (and even then not necessarily); the residue information is at most
  the real-character shadow, a "visible layer" GV_C (additional information on the particular divisor set of a fixed β is
  not excluded), and Prop 3.2: every odd non-square has a level with GV_C, including all known zeros. Prop 5.1:
  class numbers are T1-blind (squares have large ring class numbers); Siegel is ineffective. Prop 4.1: data of two orders in
  two fields *can* carry information beyond the per-field quadratic shadow (group theory PROVED; the particular quartic
  cyclotomic identification is sample-certified only; no (★)-internal configuration was constructed). Prop 4.2 proves Artin
  total-product identities for abelian extensions whose conductor is coprime to (β); on the odd-r a = 1 branch with even Nβ
  the odd-part formula is an elementary norm identity, not Art((β)). No additional forcing relation was found (Assessment);
  this is not a theorem excluding other relations among individual factors. Not excluded: non-CFT relations between individual factors across levels (E1), twist averaging
  (E2), cross-field characters as sieve input (E3); not a blanket no-go for class-group or single-field methods.
* **Single long orbit** (`Z60_DYNAMICS.md` §§2–5). PROVED: R(n) = R°(n) + #{u = 1 or B = 1}, R° = hits of one p-dependent
  Kloosterman / marked Hecke-point orbit (Lemma 1″: for odd n ≥ 5, A with 1 ≤ A < n, gcd(A, n) = 1 and minus continued fraction of n/A of length
  exactly 3, [[c, m, s]], 4 | m) in a
  target T_n of ≤ n(1 + log n)² points; the shell index is the tied modulus. Prop 3 / Cor 3: a Fourier-ℓ¹ (Weil-completion)
  minorant certificate needs |T| > 2p^{5/2}/(p − 1 + 2√p), so none exists for p ≥ 10⁴ (missing exponent ½ up to logs, in
  that norm only). Prop 4′: on Γ\ℍ every hit point is equivalent to a non-hit point — no surface minorant at any rate.
  CONDITIONAL on a Γ\G rate ε ≍ p^{−1/2+θ+o(1)}, θ = 7/64, with an L²-Sobolev norm S ≥ c_K‖·‖∞ on a **fixed compact K**,
  and a certificate supported in K, normalised by max_hits f = 1: the relative margin (∫f − εS(f))/(εS(f)) is
  ≤ p^{−1/6−θ+o(1)}/c_K (exponent −53/192); the resulting orbit-hole condition is necessary, not an impossibility theorem.
  Not excluded: target-specific cancellation, other norms, orbit holes, Γ\G certificates with tiny margin, the QNR
  half-orbit (for n ≡ 1 (4), Prop 6: Σ_x χ_n(x)1_T(x, x̄) = −R°(n)). Not "dynamics impossible".
* **Hecke trace formula on Γ(4C)** (`Z60_TRACE.md`). Lemma 1 (PROVED): Γ = Qγ − I, Q = 4C, maps (★) at level C to positive
  split or repeated-root points (repeated roots only at even n) of the Hecke set {det = 4Cn + 1, ≡ −I (mod Q)}; ES_k(C, m²) = 0 for odd m. Thm 2 (exact elliptic + hyperbolic +
  scalar trace identity; odd weight isolates ES from the trivial points): CERTIFIED on a sparse finite list, **CONDITIONAL
  on the local Lemma 3** in general (Lemma 3 CERTIFIED on 21 044 cases, not proved; Cohen–Strömberg via secondary
  quotation). For odd k ≥ 3, conditional on Thm 2 / Lemma 3, the worst-case Deligne certificate B = D fires only if
  the average normalised eigenvalue exceeds 1 − 6/((k − 1)Q − 6) (Cor 4.3; only (k, Q) = (3, 4) lacks a ρ-free constraint); at
  k = 3 it never fired at C = 2 (n ≤ 3000) or C = 3 (n ≤ 600) — finite evidence, not universal non-firing. A level-uniform
  absolute square-root bound (fixed odd k ≥ 3, all levels, all n) is refuted, CONDITIONAL on Thm 2, by a family at n ≡ 5 (8)
  (outside the Mordell-hard domain). Not excluded: sharper single-N bounds at Mordell-hard primes, one-sided estimates, other C-ranges.

## 4. What a proof would need — a five-minute screening checklist

Screen an idea against every line *before* investing in it. Each line names the barrier that killed earlier ideas of that
kind. **Scope (read this):** the barriers of §3 are theorems about *specified classes of arguments* (fixed menus, bounded
multiplicity, numerator-uniform steps, …) or Assessments about known methods; they are not necessary conditions for every
conceivable proof, and a proof need not take the form of a lower bound for (★). Treat a failed line as "this is the step
that must be new", not as a refutation — but then that step must be named and justified. Nothing proposed in this campaign
has passed all lines.

1. **It must fail at odd squares (T1/B5).** Name the step that is false at n = m². In practice the argument must use the
   quadratic character of p essentially (in every solution of 4/p with p ≡ 1 (4), every denominator prime to p has a prime
   factor ℓ with (ℓ/p) = −1; Lemma CT). Local/genus/spinor/Siegel–Weil steps are all true at m²; they cannot carry
   the argument. *(z58 precision.)* The older local/genus screens do not by themselves force a point. On the
   all-solution ES surface U_n, the BM set is nonempty for n ≥ 2 (BL). In contrast, on the displayed (★) surface and
   Type II threefold, for n ≥ 1, positive-integral BM nonemptiness detects exactly non-squareness (numerator 8:
   exclusion of □ ∪ 2□; `Z58_STRUCT.md` Thm A, `Z58_STRUCT2.md` Thm B). So BM itself does fail at squares on these
   models, but nonemptiness is not sufficient for a positive integral point (item 13). (Composite-n descent must be checked separately: a solution for m scales to one for m², so T1 does not bind arguments
   that produce mixed or scaled solutions.)
   *(z59.)* Two opposite calibrations. Half-integral weight: T1 is *stronger* than "no genus term" — for ternary-theta
   proxies it kills every Shimura component on squarefree 𝒞₁ except the Gauss-exceptional ones (`Z59_WALDS.md` Thm W1,
   §3 z59). Means: the fixed-Q leading residue-class coefficient of R is Jacobi-blind (`Z59_MSPLUS.md` Thm 1;
   R₈: same odd local factors, half the coefficient), so these leading means alone supply neither non-square
   discrimination nor pointwise positivity (Assessment); square-sensitive main terms (M_BM, §2.2), other density inputs
   or additional arithmetic steps are not excluded — name where the non-square input comes from. Kernel form of T1 in
   z59 coordinates: for the U_II T-system, every odd prime factor of Tm² + 1 lies in ker χ_{−T} (χ_{−T}(−1) = −1); for the
   ρ-system, with odd m, ρ ≡ 3 (4) and gcd(m, ρ) = 1, all prime factors of (m² + ρ)/4 lie in ker λ_ρ — non-coprime
   squares are excluded instead by `Z59_CONVO.md` Lemma 2.1 (e.g. m = ρ = 11: (121 + 11)/4 = 33 has λ₁₁(11) = 0); for
   (★), every admissible (d, k) has (−k/d) = −1 (`Z59_MSPF.md` Lemma 1.3).
   *(z60.)* **Signed T1.** A one-sided (minorant) proxy only gets g(m²) ≤ 0 from T1. For fixed-level theta-class proxies (finite
   real combinations of positive-lattice theta series plus cusp forms), in weight 3/2 with one or finitely many quadratic ψ
   and weight ≥ 5/2 with one ψ, signed T1 forces either eventual negativity at all 𝒞₁-primes, or the support-form structure,
   with only Gauss-exceptional components remaining on squarefree 𝒞₁ (`Z60_SIGNED.md` S1–S3, §3 z60). This fails in integral
   weight (AUTOMORPH B1) and for mixed ψ in weight ≥ 5/2 (explicit counterexample, proved positive at every p ≡ 17 (24));
   non-genus Eisenstein / general polynomial-growth objects are not classified. So for a signed proxy, name which of these
   classes it is in. Further T1 locations (z60, PROVED): for n ≡ 1 (4), the hits of the DYNAMICS orbit lie in the
   χ_n = −1 coset, which is empty iff n is a square (`Z60_DYNAMICS.md` Lemma 2); the RAYCLASS square-class field
   kills every level C with s | C for n = s·m² (`Z60_RAYCLASS.md` Cor 2.1); twisted T1 s ∤ uC, s ∤ BC (`Z60_MS105.md` Lemma 1);
   every witness of either López branch at p ≡ 1 (4) has a prime factor ℓ with (ℓ/p) = −1 (`Z60_LOPEZ.md`). Square-mimicking
   composites coprime to 105 (kernels ≤ 10⁵, pseudosquares, locally-square n) were *not* zeros above 29 210 401 in the tested inputs (§2 z60).
2. **It must fail for numerator 8 at 131 and 241** (i.e. it must not also prove 8/131, 8/241) (and 8/11, 8/17; numerator blindness (J)41, (J)86). If every step works
   for M/n with M ≡ 0 (4) uniformly and without a threshold, the argument proves false statements. Say where 4 enters
   (candidate: the χ-fibre S₄ of (J)32) or which threshold p₀(M) the argument needs.
   *(z57, `Z57_SYNTH.md` §2.1; cross-model reviewed.)* Concrete screen above 10¹⁰: the C-even half of (★) is exactly the
   c = 1 Type II line of 8/p (Lemma 2.1, PROVED; R = R_odd + R₈). CERTIFIED: R₈(p) = 0 at 1 270 primes p ≡ 1 (4) ≤ 10⁸ and
   at exactly 12 of the 21 668 737 primes p ≡ 1 (4) in [10¹⁰, 1.1·10¹⁰] ("exactly 12" rests on one audited exhaustive
   engine; all twelve zeros were re-verified by independent enumerators, also by the cross-review); four are in Mordell's
   classes (10 301 993 881, 10 529 331 121, 10 532 106 649, 10 868 474 401, each with R > 0), the largest zero is
   10 917 229 157. So "R₈(p) ≥ 1 for all primes p > 10¹⁰ in Mordell's classes" is false, and an argument for (MS) (§2.4)
   at threshold 10¹⁰ that remains valid on the C-even sub-line proves a false statement: it needs a step that fails for that
   sub-line, or a larger threshold for it. These zeros lie above the internal 10¹⁰ full-(★) census range and below
   Salez's 10¹⁷; they do not refute (MS). A zero of R₈ is a zero of one line of 8/p, not a failure of 8/p. Model
   (Assessment): ≈ 0.003 expected R₈ zeros above 10¹⁷ (crossover ≈ 10^{14.4}), so at the Salez threshold the screen reverts
   to the qualitative form above.
   *(z58.)* **Extended R₈ zero list.** `Z58_DISPROOF.md` found two more R₈-zero primes, both ≡ 1 (mod 840) and so in
   𝔐: **20 840 951 041** (R = 24) and **23 296 553 281** (R = 36). They are CERTIFIED by exact enumeration and re-verified
   by the cross-review. They come from a *sampled* design search, not an interval census, so there is no completeness
   claim above 1.1·10¹⁰. The original twelve-zero screen is `data/z58/screens/r8_zeros_1e10.txt`; the two new zeros
   are in `Z58_DISPROOF.md` §4 and its archived runs `data/z58/disproof/runA/` (files D1b, D1c, D2), independently
   verified in `data/z58/xreview/REVIEW_DISPROOF.md`.
   Distinguish two numerator-8 objects (`Z58_WILDCARD.md` Lemma 4.1, `Z58_STRUCT2.md`):
   * the c = 1 line R₈, which has the zeros above;
   * the full numerator-8 Type II family N^{(8)} (the d-even half of N_II). It has 22 odd prime zeros ≤ 10⁹ (last
     35 569) and 107 odd non-square composite zeros (last 1 239 315), but witnesses (c > 1) at the twelve screen R₈-zero primes in [10¹⁰, 1.1·10¹⁰]. CERTIFIED to
     10⁹.

   So an argument that also proves C-even positivity over a range containing a certified R₈ zero is refuted: it must
   distinguish that sub-line, or use a threshold excluding those zeros. The new zeros require P₈ ≥ 23 296 553 281 for a
   claim over p > P₈ in 𝔐; they do not refute eventual C-even positivity or an argument starting at 10¹⁷. For full
   numerator-8 Type II, the prime census requires P₈ ≥ 35 569 for p > P₈, but does not prove positivity beyond that
   cutoff.
   *(z59.)* Line-level numerator-8 data (CERTIFIED): the U_II-line at numerator 8, U_II⁽⁸⁾ = (c = 1) ∪ (a = 1) of 8/n, has 819 odd
   non-square zeros ≤ 10⁸, 61 of them prime (last 3 869 153), the last composite 93 398 595 (`Z59_CONV2.md` §0). The
   leading local mean of R₈ has the same odd local factors as R and exactly half the coefficient (`Z59_MSPLUS.md` Remark
   2.3, PROVED), so a step using only these leading means cannot separate them. Full d-even Type II has witnesses (all
   with c ≥ 2) at the 12 screen R₈-zero primes (`Z59_CONVO.md` §9). Among the 20 504 𝔐-primes ≤ 10⁷ with R > 0, C-even
   witnesses are absent at 186 (last 9 965 881), C-odd at 118 (last 9 744 001) and prime-d witnesses at 136 (last
   9 831 889); including the nine R-zeros: 195, 127, 145 (`Z59_MSPF.md` §4). So for a statement over p > P in 𝔐 this
   census requires P ≥ 9 744 001 (C-odd), P ≥ 9 831 889 (prime d), and P ≥ 9 965 881 for C-even (strengthened above to
   P₈ ≥ 23 296 553 281). None of these data refutes eventual positivity.
   *(z60.)* U⁽⁸⁾ ⊂ U₇ (`Z60_LOPEZ.md` Lemma 7(iv)): at f ≡ 7 (8) an argument for U₇ must use the targets r | f + 1 with
   v₂((f + 1)/8) < v₂(r) < 3, else it proves U⁽⁸⁾ (547 non-square zeros n ≡ 1 (4) ≤ 10⁸) — this binds the full CONJECTURE U₇ at its in-domain U⁽⁸⁾
   failures; the finite screen alone imposes no such requirement on (MS-U₇), which starts above 10¹⁷. For the López union at
   numerator 8 (S₈: 45 zero primes p ≡ 1 (4) ≤ 10⁸, last 3 869 153; 61 over all odd primes): at an S₈-zero prime included in
   a theorem's range, an S₄/P* witness must use g ≡ 3 (8) or a non-liftable U5 divisor (on B4 the shift divisor is odd)
   (`Z60_LOPEZT.md` §1, §3.4; p = 83449); an eventual claim may instead exclude these finite failures by its threshold. The
   R₈ control of `Z60_MS105.md` §2.6 covers the 106 admissible kernels s ≤ 1000 (6 086 436 506 inputs, not the expanded
   kernel-≤ 10⁵ domain); it leaves 281 inputs above 10¹⁰ with no C-even witness d ≤ 10⁸ (to 1.84·10¹⁹; not certified
   zeros), while R has no UNK above 10⁶ on this domain or its larger census. A transported C-even positivity claim is refuted
   only if its asserted range contains a certified R₈ zero. The examined orbit completion bounds (DYNAMICS) also fail for the
   C-even target; the per-C trace identity (TRACE) alone does not imply that an existential all-C argument transports to
   even C. Eventual C-even positivity remains open.
3. **It must not be numerator-uniform in its laws** — no k-uniform transport, square law or recombination law (all refuted
   on k/n models, (J)86, (J)88).
4. **It must break the tied modulus (B2, PARITY_AUDIT Remark 3.1).** Identify the modulus of the class condition. If it is
   fixed, find where the height dependence went (x ≡ y ≡ −1 mod 4C with C = (xy − 1)/4p); if it moves with the solution, say
   which theorem controls divisors of *one* integer in a moving class with error below a (log p)² main term. No such theorem
   is known. A fixed finite menu of slices fails infinitely often (CONDITIONAL on H, (I)8), as do fixed root sets and
   bounded windows (CONDITIONAL on Dickson, (J)106, (J)83).
   *(z60.)* Three new exact encodings put the tie in new clothes, not away: an ideal divisor of β_r = 1 + r√(−t₀n), in an
   order containing β_r, with norm ≡ −1 (mod 4C = t₀r²) for (★) at C = t₀s², r = 2s (`Z60_RAYCLASS.md` Lemma 1); the shell
   index c of the orbit: a shell hit requires 4 | c and d | cn + 1 with d ≡ −1 (mod c), d ≤ n − 1 and (cn + 1)/d ≤ n − 1
   (`Z60_DYNAMICS.md` Lemma 1′); positive split or repeated-root points (repeated roots only at even n) of the Hecke set
   ≡ −I (mod 4C) (`Z60_TRACE.md` Lemma 1). Fixed covers / witness menus fail
   again (`Z60_MS105T.md` Prop 3.1, `Z60_LOPEZT.md` Lemma 1.2; prior Z55_HCF); MS105T's missing input is a pointwise lower bound
   for divisors of n + k or 4Cn + 1 in progressions whose modulus grows with the shift (Assessment).
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
   *(z60.)* For prime n = p with p ∤ 4C, the indicator [N𝔞 ≡ −1 (mod 4C)] on all ideals coprime to the modulus and conductor
   can be class-determined in some order only if C ∈ {1, 2, 3, 6}, and even then not necessarily; the residue information is
   at most the real-character shadow GV_C, which holds at some level for every odd non-square, including all known zeros
   (`Z60_RAYCLASS.md` Props 3.1–3.2; e.g. at 64–90 levels C ≤ 300 at each (★)-zero prime). This does not exclude additional
   information on the particular divisor set of a fixed β. The barriers above (total products, forced progressions) are
   scoped forcing statements, not a universal restriction on all information in joint class data: cross-field class data can
   carry information beyond the per-field quadratic shadow (Prop 4.1, group theory PROVED). The particular quartic cyclotomic
   identification is sample-certified only; no (★)-internal configuration was constructed and no forcing relation on
   individual factors was found.
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
    *(z58, `Z58_STRUCT.md` Thm A, `Z58_STRUCT2.md` Thm B; PROVED.)* The statement above concerns U_n. On the displayed
    (★) surface and full Type II threefold (positive real region, n ≥ 1), the positive-integral BM set is empty
    **iff n is a square** (numerator 8: n ∈ □ ∪ 2□). So BM re-derives T1 and nothing else. The listed known
    non-square zeros, on their respective models, are non-BM failures: the 14 (★) primes, the 285 composites, the R₈
    primes, and 4545 for Type II. A "BM-nonempty + primality ⟹ point" step is refuted at the listed parameters if it transfers verbatim to
    the fixed local classes of `Z58_STRUCT2.md` §5.2. This does not exclude additional hypotheses or eventual positivity
    above a larger threshold (§3, z58).
14. **Run it on the test primes.** (★) fails at 14 primes p ≡ 1 (4) ≤ 10¹⁰: 409, 577, 5569, 9601, 23929, 83449, 102001,
    329617, 712321, …, 8 813 281 (`BM_CORRECTED_COUNT.md` §3.2, `B1_LINE.md` §3.6); the b = 1 line fails at 193, 2521, 66529;
    at p = 3361 the only Type II solutions are 1/850 + 1/(3361·25) + 1/(3361·170) and 1/841 + 1/(3361·290) + 1/(3361·8410), all
    on non-split slices ((J)82; 3361 is conjecturally the only prime without a prime-modulus Type II certificate, PM-II,
    exhaustive to 10⁸); at p = 5101441 the a = 1 slice has a single solution. A mechanism claiming that one fixed line or
    grammar always succeeds must survive these (the board found an HJ grammar that traps at 193).
    *(z58, composite screen refined; CERTIFIED counts, EVIDENCE reading; `Z58_SUMMARY.md` §2.)*
    * Where the 285 (★) composite zeros ≤ 7 999 801 sit: 265 have a factor 3, 5 or 7, and 270 lie outside 𝔐.
    * Above 10⁸, every non-square composite zero ≤ 10¹⁰ is divisible by 3, 5 or 7 (`Z58_LOGIC.md`). The 486 non-square
      composite zeros n ≡ 1 (4) ≤ 10¹⁰ include 16 coprime to 1155, the last 17 401 609 (`Z58_TERNARY.md`).
    * In 𝔐, the composite zeros are 18 up to 10¹¹, the last 17 401 609 (`Z58_LADDER.md`, one engine).
    * Small factors are not the whole story: 897 961 = 443·2027 is a zero.

    So a primality-blind argument on 𝔐 needs threshold ≥ 17 401 609 (cf. (MS⁺), §2.4). An argument that also proves
    full Type II at composites must respect **4545** (`Z58_WILDCARD.md`; N_II(4545) = 0, the only odd non-square
    N_II-zero ≤ 10¹⁰), which is not explained by BM or local conditions. A threshold-free argument on the a = 1 line must
    survive 193, 2521, 66529, and one on c ≤ 2 must survive 102001 and 8 813 281 (`Z58_CONVF.md`, CERTIFIED to 10⁸).
    *(z59; CERTIFIED unless marked.)*
    * (MS⁺) on 𝔐: no non-square zero in (17 401 609, 10¹²] (`Z59_MSPLUS.md` §6, one engine). Thresholds for
      primality-free variants (z58 LOGIC census, ≤ 10¹⁰): all prime factors > y with y = 7 (i.e. gcd(n, 105) = 1, all
      classes) → 29 210 401; y = 47 → exact last zero 8 813 281 (19 zeros), and for every y ≥ 47 the cutoff 8 813 281 is
      certified sufficient (the actual last zero may be smaller); 11 ≤ y ≤ 43 → 17 401 609; 3 ≤ y < 7 → 7 479 950 569; no condition → 9 919 520 121 (3 | n).
    * Of the 285 composites: 214 in the groups 3 | n, 15 | n, 21 | n, 105 | n; 51 in 5 | n, 7 | n, 35 | n; 20 coprime to 105
      (15 in 𝔐, all squarefree). The composite zeros sit predominantly where the dead-moduli factor is lowest (EVIDENCE
      reading); dead moduli explain a correlation, not every zero.
    * The U_II-line ((★) ∪ a = 1) fails at only **105 and 4545** among odd non-squares ≤ 10¹⁰ (`Z59_CONV2.md`). An argument
      that proves U_II, or a = 1 rescue, at composites must respect 105 (full Type II holds there); a full Type II argument
      must respect 4545. A U_II theorem whose asserted domain includes the fourteen (★)-zero primes must rescue them via a = 1
      with 4 ∤ T (Prop 3.1); (MS-U), starting at 10¹⁷, need not include them.
    * 4545 also refutes "some prime factor escapes the quadratic kernel ⟹ solution" (`Z59_CONVO.md` §4).
    * Keep (★)- and 𝔊*-zeros apart: the 14 (★)-zero primes are among the 38 𝔊*-zeros; the other 24 have R > 0 (11 of
      the 20 in 𝔐). A 𝔊*-zero obstructs only the subfamily.
    *(z60; CERTIFIED unless marked.)*
    * A U₇ argument (§2 z60) whose domain includes composites must fail at the eight composites of Z₇ = {105, 1465, 3865, 4545,
      10305, 12145, 39361, 67425} (all ≡ 1 (8), divisible by 5 or 7); U₇ rescues all 14 (★)-zero primes only through A-line
      words with cd even; of the 285 (★)-composites exactly these 8 are U₇-zeros (cross-review count). U₇'s B- and A-target
      halves have respectively 14 and 12 zero primes p ≡ 1 (4), p ≤ 10⁸.
    * An all-prime positivity claim for the specific d = 1 family S₁ is refuted by its 160 zero primes p ≡ 1 (4), p ≤ 10⁷ (25 in
      𝔐, largest 8 841 673), although S₁ rescues all 14 (★)-zero primes; S₁ = 0 at the 𝔊*-zeros 37 and 1621
      (`Z60_RAYCLASS.md`). Eventual S₁ positivity and other single-field methods remain open; any threshold must respect the
      zeros in its domain.
    * Bounded-witness-coordinate arguments: for every B infinitely many primes p ≡ 1 (4), gcd(p, 105) = 1 have every solution with
      uk, kC, uC > B (PROVED, `Z60_MS105T.md` Cor 3.4; one coordinate may stay small). The MS105T cover leaves 6275 of 164 736
      classes mod 1 441 440; all 2280 R-zeros in [1 441 440, 3·10⁷] of the
      MS105T zero list (squares included) lie in uncovered classes.
    * Spectral / orbit lower bounds must fail at the 14 global (★)-zero primes at every level 4C (or start above 8 813 281);
      they need not fail at the 24 𝔊*-zeros with R > 0 (e.g. 1621 has R = 4, R° = 2) (`Z60_TRACE.md` §5, `Z60_DYNAMICS.md` §0).
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
* E(N) ≪ N exp(−c(log N)^{3/4}) (INTERNALLY PROVED; `paper/es-threequarter-note`; *z58: the same bound was claimed earlier
  by Kandukoori–Ramesh–Kumar, §1 priority note, and must be cited*), shift-uniform in every interval of length H
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
  primes — vs. ET Thm 1.8's (log p)^{0.549} on a density-1 set of primes. This comparison is **not a priority claim**:
  Akaka (Zenodo 22754703, v0.7, 2026-09-14; unrefereed, declared AI-assisted, Lean certificate claimed, not checked here;
  `LITERATURE_2026.md` §2.4) claims the stronger almost-all-primes statement R_II(p) ≥ c(log p)³ for the full strict
  Type II count, outside O(N/(log N)⁴) primes p ≤ N. PZ concerns only the c = 1 line R(p), which is disjoint from the
  family Akaka's proof actually counts, so his claim does not imply PZ (`paper/es-count-note` §1.4); as a statement about
  f_II or f, PZ is superseded if Akaka's claim is correct. *(z56: written
  up as `paper/es-count-note` Thm C; internal + one cross-model referee, MAJOR REVISION for this omission, applied; not
  posted. z57: second-round cross-model referee MINOR REVISION, no GAP/WRONG main theorem; its three required changes
  (Akaka's full count R_II vs the auxiliary family his proof counts — the full counts are not disjoint, R(p)/2 ≤ R_II(p);
  almost-all lower-bound wording; a sentence splice) applied in a94666aa, not re-refereed.)* Truncation to trial moduli 4uC − 1 ≤ X^{1/4−o(1)}
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
* *(z56, `Z56_FAMTRY.md` Thm A; PROVED rel. Bombieri–Vinogradov and Montgomery's large sieve; cross-model reviewed
  CORRECT.)* #{p ≤ X : R(p) = 0} ≤ X·exp(−0.08√log X) for X ≥ X₀ (ineffective), with the same bound in every interval of
  length X. The argument never uses primality: it bounds the odd n ≤ X avoiding the hit classes at every prime modulus
  ℓ ≤ √X, a set containing all odd squares, so it cannot go below √X. Novelty unverified. Average statement (B6).
* *(z57, `Z57_BFO.md` Thm W; PROVED; cross-model reviewed CORRECT.)* #{p ≤ x prime, p ≡ 1 (4) : R_𝔊*(p) = 0}
  ≪_A x/(log x)^A for every A, for the Theorem V family 𝔊*; details and scope in §7 item 3. Average statement (B6).

**5.2 Unconditional, pointwise — for relaxations or thin families, not ES.**
* The BM main term: M_BM(p) ≥ (3/(16π²) − o(1))(log p)² (Burgess) for every large prime; five-slice analogue
  ≥ (45/(32π²) − o(1))L² ((J)100, (J)105). Main terms only.
  *(z56, `Z56_FAMDESIGN.md` Thm V; PROVED rel. Burgess and Heath-Brown's quadratic large sieve; cross-model reviewed
  CORRECT.)* The genus main term: M_gen(p) ≥ (5/(4π²) − o(1))log²p = (5/6 − o(1))M₀(p) for every large prime p ≡ 1 (4)
  (29/(30π²) ≈ 0.0979 with Burgess only, effective p₀), M₀ = (3/(2π²) + o(1))log²p the expected (★) count. Main term
  only; see §7 item 3.
  *(z57, `Z57_BFII.md`; internal hostile review + cross-model review ACCEPT-WITH-FIXES, Theorem G and Appendix A
  CORRECT; `Z57_SUMMARY.md` §4.)* **Full Type II: f_II(p) ≥ 1 for all large p NOT proved.** With
  N_II(n) := #{(a, b, c, d) ∈ ℕ⁴ : 4abcd = a + b + nc} (ET (2.15), no gcd condition):
  * Exact forms (PROVED): for a prime p, N_II(p) ≥ 1 ⟺ f_II(p) ≥ 1 (Lemma 1.0; for composite n the ET correspondence needs
    gcd(abd, n) = 1). Target-set form (Lemma 1.1(d)): N_II(n) = Σ_{f ≡ 3 (4)} #{(a, c) : ac | m_f, a·c⁻¹ ≡ −n (mod f)},
    m_f = (f + 1)/4; every two-parameter slice is one integer's divisor problem (n + 4a²d, cn + a, 4c²dn + 1).
  * **Theorem G (PROVED, Burgess + Pólya–Vinogradov only; effective, p₀ not computed).** The genus main term G(p) of the
    Type II sub-family with witness f = 4acd − 1 < p satisfies G(p) ≥ 10⁻¹⁰(log p)³ for every sufficiently large prime
    p ≡ 1 (4), already on the box of odd squarefree coprime a, c with p^{0.004} < a ≤ p^{0.006}, p^{0.080} < c ≤ p^{0.085},
    p^{0.90} < f ≤ p^{0.99}. Genus part only: nothing about N_II(p), no upper bound for G; the comparison with a c = 1
    genus mean ≍ log²p is heuristic. The order-≥3 remainder (B2) is untouched.
  * CERTIFIED: N_II(n) = 0 for odd n ≤ 10⁷ exactly at the odd squares and at n = 4545; every odd prime ≤ 10⁷ has
    N_II ≥ 1; every prime p ≡ 1 (4) below 10⁹ and in [10¹², 10¹² + 10⁸) has a Type II witness f ≤ 3263 (largest least
    witness at p = 605 531 161); the cross-review reran these with the inspected code, not a new independent engine.
    EVIDENCE (primes p ≡ 1 (4)): mean N_II ≈ 0.076 log³p; c ≥ 2 carries 86 % of solutions on [10⁶, 10⁷) and rescues all
    14 (★)-zero primes p ≡ 1 (4) ≤ 10⁷.
  * Assessment: c is not a free variable at fixed p in these representations; it buys a log p in the genus main term and,
    empirically, a constant factor in relative fluctuation — not a proved impossibility of other uses of c.
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
* *(z56, `LEAN_Z56.md`; Lean 4 + mathlib, no `sorry`/`native_decide`, standard axioms, 31 theorems audited; no cross-model
  review.)* Machine-checked in `lean/ES/ES/HC.lean`: the five slot identities (certificate ⟹ ES); FABLE Thm 1's coordinate form in
  both directions for every n ≡ 1 (4); Z53_UPPER Lemma 1.1 lines U/T; Theorem Q (4 | m, p = 5m² + 1 prime ⟹ HC(p) ≥ 7);
  HCKILL Lemma 1.1 for every n ≡ 1 (8); UPPER2 Prop 3.1 (HC(p) ≤ 8 for primes p > 7, p ≡ 1 (4), outside the six classes
  mod 840). Elementary statements only; infinitude claims and censuses are not formalised.

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
* *(z57, `Z57_BFII.md` Prop 2.2, Cor 2.4, Props 3.1–3.2; PROVED; cross-model reviewed.)* **Type II witness barrier.** Every
  solution of 4abcd = a + b + nc at odd n has (n/f) = −1 for both witness moduli f = 4acd − 1, f′ = 4bcd − 1; hence
  N_II(m²) = 0, and at primes p ≡ 1 (4) both witness moduli are ≥ n_p, the least quadratic non-residue: an argument that
  always produces a witness ≤ g(p) proves n_p ≤ g(p) (g = p^θ with θ < 1/(4√e) would beat Burgess). Literature lower
  bounds for n_p (Graham–Ringrose, Montgomery) were quoted from memory and are not part of the PROVED inventory. No finite
  set of witness moduli covers all primes (Prop 3.2, Dirichlet); the only complete moduli are finitely many, f = 3, 7, 15
  below 4000 (CERTIFIED list), giving f_II(p) ≥ 1 whenever p is a non-residue mod 3, 5 or 7 (Mordell-type).

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
* *(z57, `Z57_BFII.md` §5.5; implication PROVED, hypothesis non-standard.)* Hypothesis SB: for every large prime
  p ≡ 1 (4) there is F ∈ [p^{0.9}, ½p^{0.99}] with A_F(p) ≥ ½G_F(p), where A_F counts actual Type II solutions with witness
  f ∈ (F, 2F] and G_F is its genus expectation. SB ⟹ f_II(p) ≥ 1 for all large p (via Z57_BFII.md §5.5 and Appendix A
  Lemmas 3 and 5).
  SB is consistent with T1 (both sides vanish at m²); no implication from GRH or standard AP estimates is established.

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
* (z56) Union over size windows of the (★) count, via the exact links of Lemma L or a pointwise variance across windows →
  `Z56_FAMATTACK.md` Lemma L, Prop V, F1 (method-scoped, not a theorem killing union or variance routes): the analysed links
  are positive (the switch maps a hit at u to one at u′ = B), size-only, quadratic or congruence-level; a pointwise variance
  criterion implies a weighted first-moment lower bound (PROVED); EVIDENCE: some negative window pairs, but net positive
  residual covariance and excess joint emptiness. Not covered: non-size windows, signed cross-level identities, other links.
* (z56) A transfer X ≥ −(1 − ε)M_gen asserted uniformly for all non-square n ≡ 1 (4) → false: 285 non-square composites
  n ≤ 7 999 801 have R(n) = 0 (CERTIFIED counts); floating-point genus evaluation gives M_gen ≈ 24.3 at
  810 001 = 241·3361 (EVIDENCE; `Z56_FAMATTACK.md` §3.5). Eventual statements are not refuted; the known prime zeros
  separately refute an all-primes version without a lower cutoff.
* (z56) Bounds on the whole-integer avoider set of (★) → `Z56_FAMTRY.md` §3.5(i), §4.4: it contains (1/2 + o(1))√X odd
  squares up to X, so such bounds stop at √X (PROVED); log L(Q) ≍ √log Q is optimal for that specific large-sieve
  denominator only. Sieves counting primes, prime weights and off-square refinements are not covered.
* (z56) Central-slice asymptotics (CNT-type) as a route to gap 1 → `Z56_CENTRAL.md` Thm L, Cor L1 (CONDITIONAL on EPC): a
  uniform, length-decoupled CNT_unif would give SID, a pointwise power-saving asymptotic for Σ_{x<n≤x+x^{1/4}} d(n), not
  established in the checked sources (Assessment). The fixed tied/prime CNT is not shown equivalent to SID.
* (z56) One-component data-only semi-linear sieve for S-membership → `Z56_K4LIT.md` Lemma P / Prop P′ (PROVED, P′
  relative to Iwaniec 1976 Thm 1): for nonnegative parity-forced sequences with admissible density
  g(q) = (1 + c_q)/(q + c_q), 0 ≤ c_q ≤ C/q, counterexamples with the prescribed local density and stated remainder bounds
  exist at every fixed level < 1/2; above 1/2, the stated support and remainder hypotheses force S-mass. Endpoint open.
  Not covered: joint two-component data, switching, primality of p.
* (z56) Multiplicative comparison model for Type II on a\*_n = r\*(n + 4)r\*(4n + 1)·1[n ≡ 97 (120)] → `Z56_K4BILIN.md` Lemma N (PROVED):
  fails every Type II hypothesis with logarithmic saving (inert-prime shift classes). W-tricked or other comparison models
  are not ruled out.
* (z57) Statistical complementarity of certificate families ((★), b = 1, Type I a = 1, c = 2, 3 lines, 𝔊*, its corner) →
  `Z57_COMPLEMENT.md` (scoped negative, over primes; first draft REJECTED by the cross-review, corrected): no robustly
  negative full-pair count association after local controls (EVIDENCE, 10⁸–10¹³ plus rough semiprimes); same-integer
  slices with nonempty admissible unit-class sets positively coupled (Thm C(i), PROVED for bounded shifts, M-coprime divisors ≤ x^θ, θ < 1/4); positive covariance
  does not forbid pointwise coverage. Pointwise complementarity at primes is not excluded for five pairs (§7 item 3).
* (z57) Split-and-complement of (★) by the parity of C → `Z57_SYNTH.md` §3.II: on a domain it is full-family positivity
  ((MS) itself), the halves are positively associated (corr ≈ +0.29 at 10⁷–10⁸, EVIDENCE), no disjointness mechanism
  found. Not excluded.
* (z57) Additive-character expansion of the 𝔊* hit count over moduli d → `Z57_BFF.md` §2 (Assessment for this
  implementation): no estimate for the weighted error supplied for d ≤ p^{1/3}; uniform positivity H(p; D) ≥ 1 for all
  large primes is impossible when D ≤ c·log p (Linnik example, PROVED); for d ≥ p^{1/3} it is B2 in tied form. Larger-d routes are not excluded.
* (z58) Character-layer expansion of the (★) hit indicator (L₀ + L₂ + L_r + L_n) → `Z58_TRYF.md`. Burgess bounds only the
  Jacobi layer L₂ (Thm 2.1, PROVED). No bound is proved for L_r or L_n, and HCE is stronger than the target. An L_r bound
  via Shiu + Pólya–Vinogradov looks feasible; it is not excluded.
* (z58) Surrogate main term M₂ plus exponential sums on boxes (van der Corput, Weil/Salié/Karatsuba, Erdős–Turán) →
  `Z58_TRYF2.md` §4 (Assessment for these attempts): the errors are too large for the polylog per-box main term. Thm A
  (M₂ ≥ c₀ log²p) stands; E₂ > −M₂ is open. Other analytic arguments are not excluded.
* (z58) Fixed-character / least-non-residue covering of 𝔐 by a fixed prime q with (p/q) = −1, no threshold →
  `Z58_TRYO.md` §3.3 (CERTIFIED by the screen zeros, for each q ∈ [11, 47]). Thresholded or eventual variants are not
  excluded. TRYO Thm 2 and `Z58_CONVF.md` Thm 3.1 (almost-all, PROVED) are already covered in substance by the earlier, stronger `Z56_FAMTRY.md` Thm A.
* (z58) Designed counterexample search for (MS) (square-class, near-square, avoidance and CRT designs) →
  `Z58_DISPROOF.md`.
  * Result: no R- or 𝔊*-zero among 868 562 sampled primes ≤ 7.31·10¹⁵ (CERTIFIED decisions).
  * Fixed-y square-class kills fade with p (model, Assessment). Fixed-offset line kills remove only O_k(L) mass, assuming
    line mass ≍ L/u.
  * The zero-law tail is a scenario, not a bound. Slowly decaying mixtures, growing offsets, other polynomial families
    and a non-local "prime T1" are not excluded.

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
* (z56) Fixed finite coverings of the primes ≡ 1 (8) by solvable (★) classes, or finite polynomial menus → `Z56_FAMTRY.md`
  Prop 2.2 (PROVED): every such finite menu (polynomial menus: with eventual positive integral validity on the stated
  classes) misses all primes ≡ 1 (mod 8·lcm q_i). Growing/infinite congruence families and
  prime-sensitive arguments are not excluded.
* (z56) The tried algebraic families for P(4,15) → `Z56_K4TRY.md` §4.1–4.2: p(m, n) = (n² − m² + 4)² + m² − 4 has both
  shifts sums of two squares; its parameter-count heuristic suggests a thinner family than a² + b⁴, and no applicable
  prime-value theorem was located (Assessment); fixing (u, s) gives lattice lines
  (Theorem Q is one); "automatic confinement" of SL₂(ℤ)-norms is false (PROVED counterexample). Scoped to these
  parametrisations; other algebraic families and methods are not excluded.
* (z57) Covering rigidity plus explicit least non-residue with finitely many moduli → `Z57_SYNTH.md` Prop A.3 (PROVED, a
  corollary of `Z55_HCF.md` T3.1): SMCR(D, g) (every unit avoider of all (★) hit classes with modulus ≤ D is a QR mod
  every odd prime ≤ g) is false for every finite D ≥ 3 and every g ≥ 11. Size-controlled variants are not excluded.
* (z57) Bounded-order character data and finite witness menus → `Z57_BFO.md` Lemma 2.3 (PROVED: characters of orders
  dividing k recover a unit residue class exactly only modulo divisors of an explicit Λ(k); the methodological reading is
  Assessment); `Z57_BFII.md` Prop 3.2 (PROVED: no finite set of Type II witness moduli covers all primes). Growing or
  p-dependent witness families are not excluded.
* (z58) Witness selectors for (MS) (least d, q, m3, u, C, s; congruence, n_p-rooting, CF(√p), two-square data) →
  `Z58_WITNESS.md`.
  * Fixed-congruence selectors fail on 𝔐 (PROVED), and bounded-coordinate menus fail i.o. (CONDITIONAL on Dickson).
  * The CF, two-square, parity and n_p-rooting predictors are null (EVIDENCE).
  * Structural selectors only, not arbitrary algorithms. Growing-coordinate rules (CONJECTURE W) are open.
* (z58) Finite (★) case splits on Mordell class 1, and global polynomial certificates in p = x² + 840y² →
  `Z58_MORDELL.md` Cor S2, Prop C1 (PROVED; §3 z58). The other five classes and non-polynomial uses of (x, y) are open.
* (z58) Rigid modulus-4 slices and inheritance for Type II → `Z58_WILDCARD.md` §§2, 4–5.
  * Inheritance to multiples needs divisibility (PROVED; 4545).
  * r-spectrum multiplicativity is false (4 ∉ ℛ(409)).
  * The slices only give Z(N_II) ∩ odd ⊂ S₃, a pointwise sieve event that reciprocity does not resolve.
* (z58) Constructions for CONV-II at primes → `Z58_CONVF.md` §4(A–H) (Assessment: failed attempts, *not* barriers).
  These were non-residue witnesses, Pell numerators, CRT cofactors, norm forms, character correlations across shifts,
  descent, re-encoding and divisor-pair distribution. Lemma 1.4 (PROVED) kills only finite fixed (a, c, d) sets.
* (z58) Size-controlled symmetric covering with bounded D, and threshold-free exact mechanisms on 𝔐 →
  `Z58_LADDER.md` Cor 1.3 (PROVED) and the CERTIFIED zero lists. Covering scales p^{0.15}–p^{2/3} and thresholded
  counting are not excluded.

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
* (z58) Positive-integral BM / étale descent / coordinate fibrations as a sufficient criterion for (★) or Type II points →
  `Z58_STRUCT.md` Cor A′, `Z58_STRUCT2.md` §5.2 (PROVED + CERTIFIED). BM detects exactly T1, and BM-nonempty does not imply
  a point. Not excluded: further hypotheses, the open S°, equidistribution on fibres, an eventual IHP_BM.
* (z58) Fixed-level automorphic and ternary-theta support proxies → `Z58_AUTOMORPH.md` Cor A1, `Z58_TERNARY.md` Thm F
  (PROVED in scope; §3 z58). Escapes E1/E2/E3 and E1′, the cusp route and off-𝒞₁ classes remain.
* (z58) Fixed-degree, large-q function-field positivity → `Z58_FFIELD.md` Cor 3.2 (PROVED rel. Chebotarev). The residue-blind
  local route is dead (Prop 3.1). Fixed-q methods remain.
* (z58) Logic shortcuts → `Z58_LOGIC.md`.
  * IOpen plus residues cannot prove MS⁺★(P) (Thm 6.2, PROVED).
  * No natural-proofs barrier was established. An ineffective eventual Σ₂ theorem would not finish the (★) route
    (Assessment).
* (z59) Single-eigensystem cusp/Waldspurger positivity for ternary-theta proxies on 𝔐, and termwise recipe lattices on the
  square class → `Z59_WALDS.md` Thm W1, Lemma W0, §6.1 (PROVED in scope; §3 z59). For p ∈ 𝒞₁(2N), a non-zero
  single-eigensystem restriction has g(p) ≠ 0 iff L(G_φ ⊗ χ_p, ½) ≠ 0 (under W1′'s anchor with non-zero restriction, or
  (H2) with K_φ(g) ≠ 0); only for valid g does this force R(p) > 0. The "every p" version is false at 13 explicit
  𝒞₁-primes (six in 𝔐) for the tested conductor-84 twist; eventual failure only CONJECTURE (rational G_φ, residue-class
  CKRS refinement with a positive constant, not stated in CKRS). Escapes (E-a)–(E-e) remain.
* (z59) Local means / dead moduli as a proof device for (MS⁺) → `Z59_MSPLUS.md` Thm 1, Remark 2.3 (the fixed-Q leading
  coefficient is Jacobi-blind; R₈ has the same odd local factors and half the coefficient; Assessment that these leading
  means alone are no route; square-sensitive main terms and other density inputs are not excluded). Unconditional closure-based reductions between (MS) and
  (MS⁺) (products, divisors, q²-scaling) fail (CERTIFIED examples); witness-shape-conditioned reductions are not excluded.
* (z59) Inheritance / numerator ladder / ET dilation as a source of Type II solutions at primes → `Z59_CONV2.md` Prop 4.1
  (PROVED: no descent into a prime within equation-scaling transports). Non-monomial or adaptive maps are not excluded.
* (z59) "Some prime factor of N_ρ = (p + ρ)/4 escapes the quadratic kernel ⟹ ρ works" → `Z59_CONVO.md` §4 (refuted by
  4545 and at p = 8 803 369; CERTIFIED). Other bounded-order character arguments are not excluded.
* (z59) Tryhard routes for pointwise (★) / Type II (least non-residue, near-squares, Pell / norm forms, Vieta, prime
  witnesses, Zagier-type involutions, fixed small C, short-interval divisor sums) → `Z59_MSPF.md` §3, `Z59_CONVO.md` §7
  (Assessment: failed attempts, *not* barriers). MSPF's (★) attempts stop at "some n + k has a divisor ≡ −1 (mod 4k)".
  CONVO's full Type II attempts stop at the ratio criterion: for some j ≥ 0, (p + 3)/4 + j has positive divisors a, b with
  ab dividing it and a + b ≡ 0 (mod 4j + 3). These are related tied-divisor problems, not the same positivity statement.
* (z60) Fixed-level theta-class signed minorants (finite real combinations of positive-lattice theta series plus cusp
  forms) in weight 3/2 (one or finitely many quadratic ψ) and weight ≥ 5/2 (one ψ) as an escape from T1 → `Z60_SIGNED.md`
  S1–S3 (PROVED rel. cited inputs; §3 z60): either the proxy is eventually negative at all 𝒞₁-primes, or only
  Gauss-exceptional components survive on squarefree 𝒞₁. Non-genus Eisenstein / general polynomial-growth objects are not
  classified. Mixed ψ in weight ≥ 5/2 is *not* closed (counterexample, off 𝔐); multi-eigensystem
  support proxies are not dead (S5: cancellation is avoidable; missing are non-degeneracy and a validity mechanism).
* (z60) A p-independent "branch A fails up to X ⟹ branch B fires by g(X)" law for U_II → `Z60_LOPEZ.md` Prop D (PROVED in
  the modulus coordinate, CONDITIONAL on Dickson in the shift / middle-letter coordinates). Adaptive links not excluded.
* (z60) Bounded congruence covers / fixed witness menus for (MS⁺₁₀₅)-type or López statements → `Z60_MS105T.md` §§3–4,
  `Z60_LOPEZT.md` Lemma 1.2 (PROVED; prior `Z55_HCF` Thm 3.1). Unconditional good × good closure and scaling ascent → refuted
  (2929 = 29·101; 12 538 801; `Z60_MS105.md` §5, CERTIFIED); conditional gluing / descent not excluded.
* (z60) Positive-density algebraic zero families along non-square univariate polynomials (as a disproof route for
  (MS⁺₁₀₅)) → `Z60_MS105.md` Thm 3 (PROVED: density 0). Density-zero and sporadic zero families remain possible.
* (z60) Ring-class / class-number / small-prime-splitting information in one field ℚ(√(−Cp)) → `Z60_RAYCLASS.md` Props
  3.1–3.2, 5.1 (PROVED; for p ∤ 4C, on all ideals coprime to modulus and conductor, ring classes give only the visible
  layer GV_C, which every non-square has). Not all class-group methods; information on the divisor set of a fixed β and
  cross-field data are not excluded.
* (z60) Weil-completion (Fourier-ℓ¹) or modular-surface minorants for the single-orbit encoding → `Z60_DYNAMICS.md` Prop 3 /
  Cor 3, Prop 4′ (PROVED); rate-based margins CONDITIONAL-constrained (Prop 4). Target-specific cancellation not excluded.
* (z60) Worst-case Deligne certificates in the Γ(4C) trace identity → `Z60_TRACE.md` Cor 4.3 (necessary alignment
  condition, CONDITIONAL on Lemma 3; finite non-firing evidence at C = 2, 3). Not a theorem that spectral positivity is
  impossible.
* (z60) Tryhard re-derivations (López union via Type I/II parametrisations, coverings, explicit / prime / composite
  witnesses, counting; MS105 via character expansion, small shifts, quadratic fields, factoring n) → `Z60_LOPEZT.md` §3,
  `Z60_MS105T.md` §5 (Assessments: failed attempts, *not* barriers, beyond the fixed-menu lemmas).

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
   *(z56, `Z56_CENTRAL.md`; internal hostile reviews + cross-model review; calibration, upper-bound only; `Z56_SUMMARY.md`
   §4.)* How hard is the central slice? SID: D(x, y) = Main(x, y) + O(x^{(1−η)/4}) for some
   η > 0, uniformly for all large real x and y ∈ [x^{1/4}/K, Kx^{1/4}], with K ≥ 1 fixed. Throughout these reductions,
   0 < δ < 1/4.
   * Thm L (PROVED identity): D(x, y) − Main = E_band(δ) − 2F_L + O(1), with E_band the band m ∈ (x^{1/2−δ}, x^{1/2+δ}] and
     F_L = Σ_{m≤x^{1/2−δ}}[ψ((x+y)/m) − ψ(x/m)]. CONDITIONAL on EPC: F_L ≪ x^{1/4−δ/2+ε}; hence SID ⟺ a power saving for
     some central band, and CNT_unif ⟹ SID (likewise CNT_poly, constants polynomial in the band position).
   * CNT_unif / CNT_poly are stronger than TDCAL's CNT (all real x, length decoupled from position, uniform thresholds);
     CNT_unif contains CNT provided K > max(1, 2c₂, 1/(2c₁)); this is a sufficient condition, not a necessary threshold.
     The fixed tied/prime CNT is not shown equivalent to SID.
   * Cor L3 (PROVED; Trudgian–Yang pair (715/10238 + ε, 7955/10238 + ε), ε > 0 sufficiently small): this argument gives
     the equivalence unconditionally for 6387/28960 < δ < 1/4 (lower threshold ≈ 0.2205; finite pair search, no
     optimality claim).
   * Thm U (PROVED implication): power-saving short-interval asymptotics for τ_t(n) = Σ_{de=n}(d/e)^{it}, uniformly in
     |t| ≤ x^c, imply CNT_unif. Thm E (CONDITIONAL on EPC): the converse. So under EPC, CNT_unif ⟺ the x^{1/4}
     short-interval asymptotic for the small-twist family τ_t (t = 0: SID), existence of exponents only.
   * Prop P (PROVED rel. de la Bretèche–Tenenbaum 2025 Cor 1.2): |E1(p, U)| ≪ U(log log U)^{5/2} pointwise for primes p
     in the fourth-root range c₁p^{1/4} ≤ U ≤ c₂p^{1/4}, 16U³ ≤ p (was U^{1+ε}).
     Cor P2 (PROVED implication, localized Fejér): TD(η) ⟹ DC(2U^{−η}) with a (log log U)^{5/2} loss.
   * SID "not established" is Assessment (search-limited): the cited Ivić–Zhai bounds help only for lengths ≥ x^{1/3},
     Jutila's conjecture is open, and Δ = Ω(x^{1/4}) blocks the endpoint route. Remark H: the dual phase's Hessian has rank
     one (PROVED); non-applicability of 2D methods is Assessment.
   * EVIDENCE: identity residual ≤ 0.632 at 10¹⁰ (2 400 cases); slice errors at the √y scale, no slice distinguished.
   * Assessment: the count enters gap 1 only as a zero mode, for which Prop P suffices; CNT-type asymptotics are
     SID-hard (modulo EPC and uniformity) and should not be on the route to TD/NC.
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
   *(z56, four lanes on unconditional K(4) = P(4,15), each with internal hostile and cross-model review; `Z56_SUMMARY.md`
   §2.)* **K(4) NOT proved; narrowed.** Theorem U (z55) remains the unconditional state for the fixed pair (4, 1).
   * **Generic shifts (`Z56_K4TRY.md` Thm AA; PROVED, unconditional; rel. Barban–Davenport–Halberstam, the linear beta
     sieve, Ford's upper sieve).** For every ε ∈ (0, 1) there are η ∈ (0, 1/10], c > 0, x₀ such that for x ≥ x₀ and
     H = x^{1−η}, all but at most εH² admissible pairs (a, b) ∈ [1, H]² (a ≡ 0 (4), b ≡ 1 (4), 3 | ab(a − b)) have
     #{p ≤ x : p ≡ 1 (8), p + a ∈ S, 4p + b ∈ S} ≥ c·x/(log x)². It never selects a fixed pair; nothing about (4, 1).
   * **Dense sequence (`Z56_K4BILIN.md`).** a\*_n := r\*(n + 4)r\*(4n + 1)·1[n ≡ 97 (120)]; a\*_p > 0 ⟺ p is a P(4,15)
     prime in that class.
     * Lemma T\* (PROVED rel. FI 2009 Lemma 4.1 = Smith): level x^{1/6−ε} for moduli coprime to 30, density
       g\*(ℓ) = 1/(ℓ + 2χ₋₄(ℓ)).
     * Prop P (PROVED): ≫ x/(log x)⁹ integers n ≤ x, n ≡ 97 (120) with n + 4, 4n + 1 ∈ S, Ω(n) ≤ 12 and all prime
       factors > x^{1/13} (roughness holds for this constructed subset only). No ES content: n is not required to be
       prime.
     * Lemma N (PROVED, negative): see §6. The implication (TII_W) ⟹ P(4,15) (V′) is only proposed: it also needs two
       unproved model lemmas (model Type I, model prime mass) and a weighted Harman sieve.
     * Assessment (one architecture): the FI full-range budget is > 3/4 for primes in CRT-mixed classes; dispersion
       gives ≈ 0.617 for a single fixed residue (Lichtman; abstract-only tag), 1/2 + δ for mixed residues. Diagnostics to
       10¹⁰ cannot validate an all-coefficient Type II statement.
   * **Chen-type switching on 4p + 1 (`Z56_K4CHEN.md`).** Lemma D (PROVED, under its stated parameter
     hypotheses): an exact counting inequality with T₁, direct and switched terms, and repeated-𝒬-factor error
     E ≪ x^{1−ζ}. Prop K6: C(6) (≫ x/(log x)² primes p ≤ x, p ≡ 1 (8), p + 4 ∈ S, Ω_𝒬(4p + 1) ≤ 6) in the BV-level
     model, CONDITIONAL numerical witness on Hypothesis MT and the stated numerical inequality (MT: BV-type remainder
     control for the structured switched sets and local-factor/main-term evaluation ≤ 2.35 × model); the enclosure is
     evaluated in floating point, not interval-certified. Model (Assessment): 10 → 6 surviving pen 2.35, 4 only on
     a knife-edge; C(2) grid witnesses at level 0.68 (0.65 with switched sums at level θ); no C(0) witness through level 1
     (P415's ≈ 0.996 stands). **No unconditional explicit Ω_𝒬 bound follows.**
   * **Literature calibration (`Z56_K4LIT.md`; Assessment from provenance-tagged sources, bounded searches).** Neither
     P(4,15) nor its det-1 analogue was located as an unconditional theorem. FI 2009 Thm 4 (Σ Λ(n)r(n−2)r(n+2) ≍ x) has its
     lower bound under A(θ) for one fixed θ < 1 sufficiently close to 1 (upper bound unconditional); Sedunova 2026 still
     calls it conditional. Nath–Xie v3: Ω(p + 2) ≤ 9 (P415 cited v1's 11). No 2018–2026 result located supplies the input.
     * Lemma P + Prop P′ (PROVED; P′ rel. Iwaniec 1976 Thm 1): for one parity-forced semi-linear component with admissible
       density and the stated nonnegativity, support and remainder hypotheses, data at every fixed level < 1/2 cannot
       guarantee an element of S; at every fixed level > 1/2 they force
       S-mass ≫ X(log x)^{−1/2}. Endpoint open; nothing for joint data.
     * (★K) (BV for {r\*(4p+1)} in classes p ≡ −4 (mod d), semi-linear weights): an incomplete research specification,
       not a proved implication.
     * Assessment: every exact two-component sieve implementation audited needs EH-strength input (Theorem Q's
       Bunyakovsky route is a different hypothesis). Not a theorem that K(4) is hard.
   * **Hybrid route (`Z56_K4TRY.md` §2; Assessment, model only).** r\* on one shift, semi-linear sieve + switching on the
     other: model level 0.908 (pen 1) / 0.958 (pen 2.35). No conditional theorem (the hypothesis is only outlined; local
     densities and Lemma S unproved). The det-1 comparison is an analogy, not a reduction.
   * CERTIFIED (`Z56_K4TRY.md` §5, cross-review byte-identical): among the 2 769 023 primes p ≡ 1 (8), p ≤ 2·10⁸, 232 258
     have p + 4, 4p + 1 ∈ S. EVIDENCE: model switched masses agree in order only (relative deviations −1 % to −19.5 %).
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
   *(z56, three lanes on a big-main-term family and on full (★) positivity, each with internal hostile and cross-model
   review; `Z56_SUMMARY.md` §3.)* **(★) at every large prime NOT proved.** M₀(p) = (3/(2π²) + o(1))log²p is the expected
   (★) count.
   * **Big family (`Z56_FAMDESIGN.md`).** Solutions (o, e, C), o odd, e even, p = 4oeC − o − e;
     𝔊* := {(o, e) : max(o, e)⁴ > min(o, e)·p} (integer inequality, o = 1 allowed).
     * Theorem V (PROVED; Burgess + Heath-Brown's quadratic large sieve): for every η > 0 and every prime p ≡ 1 (4),
       p ≥ p₀(η, λ), the genus main term of the pairs of 𝔊* with min(o, e) > p^λ is ≥ ((3/π²)·area(G_λ) − η)log²p,
       where, in log coordinates, G_λ = {(a,b) ∈ (0,1)² : a+b < 1, max(a,b) > (1+min(a,b))/4, min(a,b) > λ}, with
       λ > 0 fixed before p → ∞.
       With Burgess only (λ = 1/15): 29/(30π²) ≈ 0.0979, effective p₀; with HB the constant → 5/(4π²) ≈ 0.1267 as λ → 0.
       Hence M_gen(p) ≥ (5/(4π²) − o(1))log²p = (5/6 − o(1))M₀(p), 18.5 × Thm U's constant. On compact rectangles inside
       the region it is an asymptotic. Cor V1: 64/(45π⁴) ≈ 0.0146 on Thm U's admissible trapezoid.
     * The excluded density-area sixth is the Burgess corner max(o, e) ≤ (min(o, e)·p)^{1/4} (C ≳ p^{1/3}), where the
       cross terms are not controlled by this argument (no impossibility or optimality theorem). Every solution with
       64C³ ≤ p lies in 𝔊* (PROVED).
     * CERTIFIED: R_𝔊*(p) = 0 at exactly 38 primes p ≡ 1 (4) ≤ 10¹⁰, the last 564 661 441 (R = 2, its unique solution in
       the corner); none at the 57 806 sampled primes above 10¹⁰ up to 10¹⁴. Burgess-only family: 317 zeros ≤ 10¹⁰, last
       6 122 428 657. The cross-review reproduced the stored unions and the four zeros above 10⁷ but did not rescan
       (10⁶, 10¹⁰].
     * EVIDENCE: mean R_𝔊*/log²p ≈ 0.134 → 0.126 (≤ 10⁷ → 10¹⁴), var(hits)/E[hits] 2.4 → 4.9, where
       hits = R_𝔊*/2. Assessment (crude two-parameter fit): expected-count crossover ~10^{8.3}, vs ~10¹¹⁸ for the standard Thm U window.
     * Main term only: the order-≥3 remainder (B2) is untouched. Assessment: 𝔊* and its complete-level part
       H3 = {64C³ ≤ p} are the recommended targets for problem CROSS.
   * **Joint attack (`Z56_FAMATTACK.md`).**
     * Prop T (PROVED, effective): tiled Thm U gives M_gen ≥ (64/(45π⁴) − ε)log²p (as Cor V1; superseded in size by
       Thm V). Prop T′ (PROVED): tiled GENUSX Thm X gives an exact-class density main term ≥ (28/(75π⁴) − ε)log²p ≈ 0.0038
       log²p with T_u = O(p^{−δ}log p) on every tile. Lower-bound coefficients, not ceilings.
     * Thm J (PROVED reduction): R(p) ≥ Σ_t M^cls_t + Σ_t E_t over a finite tiling, so eventual (★) follows from the tiled
       exact-layer bound (CU_𝒯): Σ_t (T_w + T_uw)_t ≥ −(1 − ε)Σ_t M^cls_t (CONJECTURE-strength; sufficient, not
       necessary; vacuous at odd squares).
     * Lemma L, Prop V (PROVED) and F1 (EVIDENCE): see §6. The registered F1 kill condition was not met.
     * CERTIFIED counts: among n ≡ 1 (4), 5 ≤ n ≤ 7 999 801, R(n) = 0 exactly at 13 primes, all 1 413 odd squares in that
       range, and 285 non-square composites. EVIDENCE (floating-point evaluations of exact finite sums): composite-zero
       M_gen reaches 24.3 at 810 001 = 241·3361; at the prime zero 8 813 281, M_gen ≈ 29.1.
     * Assessment: every joint inequality found reduces to (CU_𝒯), B2 in tied form.
   * **Tryhard (`Z56_FAMTRY.md`).** Theorem A (PROVED; §3.5, for X ≥ X₀ ineffective): #{p ≤ X : R(p) = 0} ≤ X·exp(−0.08√log X), B6. Lemma 1.4
     (PROVED): R(p) ≥ 1 iff some d ≡ 3 (4) has (−p mod d) nonzero and dividing (d + 1)/4. Prop 2.1 (PROVED): p ≡ 5 (8),
     2 (3), 5 or 6 (7) ⟹ R(p) ≥ 1. EVIDENCE: 422 primes p ≡ 1 (8) in [10⁷, 10⁸] have no prime-modulus hit — finite only;
     no theorem here forces composite or linear-size moduli eventually.
   *(z57, three lanes on R_𝔊* ≥ 1 and on complementarity, each with internal hostile and cross-model review;
   `Z57_SUMMARY.md` §§2, 3, 5.)* **R_𝔊*(p) ≥ 1 for every sufficiently large prime p ≡ 1 (4) NOT proved** (neither
   eventually nor effectively with p₀ ≤ 10¹⁰).
   * **Theorem W (`Z57_BFO.md` §3; PROVED rel. Montgomery's arithmetic large sieve, Dirichlet–Mertens in fixed
     progressions and an elementary Rankin-type bound; cross-model reviewed CORRECT).** For K ≥ 1 and
     κ_K := Σ_{C≤K} 1/φ(4C) (≥ ¼ log K): #{p ≤ x prime, p ≡ 1 (4) : R_𝔊*(p) = 0} ≪_K x/(log x)^{1+κ_K}, x ≥ 2; hence
     ≪_A x/(log x)^A for every A > 0. Only the complete levels C ≤ K are used: the bound holds for the primes with no hit
     at any level C ≤ K, a set containing every 𝔊*-zero p > 64K³. Assessment: weaker than Vaughan-type bounds for the
     whole ES equation; growing K gives at best exp(−c√log x) (heuristic). Average statement (B6).
   * BFO structure (PROVED): Lemma 2.2 — the class condition of a fibration is decided by quadratic characters only for
     modulus 4m | 24 (the eight integers p + 1, p + 2, p + 3, p + 6, 4p + 1, 8p + 1, 12p + 1, 24p + 1); Lemma 2.3 — see §6.
     Assessment: in the routes tried, reciprocity → characters mod p → Burgess reaches only the genus layer; no reduction
     of the target to GRH, EH or Hypothesis H was found.
   * **Defect form (`Z57_BFF.md` Theorem 1 = Lemmas 1.2–1.3; PROVED).** For integers d ≥ 3, d ≡ 3 (4), p ∤ d, let n_d, C_d be the least
     positive residues of −p and −(4p)⁻¹ mod d. Then 4n_dC_d ≡ 1 (mod d), and HIT(d) :⟺ 4n_d | d + 1 ⟺ 4C_d | d + 1 ⟺
     4n_dC_d = d + 1; HIT(d) gives the (★) solution (n_d, (p + n_d)/d, C_d). R_𝔊*(p) ≥ 1 ⟺ some integer d ≥ 3,
     d ≡ 3 (4), d ≤ ⌊p^{3/4}⌋ + 1, has HIT(d) and max(n_d, m)⁴ > min(n_d, m)·p, m = (p + n_d)/d; a hit with d⁴(d + 1) ≤ 4p³ (e.g.
     d ≤ p^{3/5}) is automatically in 𝔊* (sufficient, not necessary). **Lemma 1.4 (PROVED):** HIT(d) ⟹ (−n_d/d) = −1,
     (p/d) = −1, (d/p) = −1; hence no hit at odd squares (T1). For fixed 0 < ε < 3/4 and p^{1/4+ε} ≤ D ≤ p, Burgess gives
     D/8 + O_ε(D^{1−δ}) non-residues d ≡ 3 (4) below D, for some δ = δ(ε) > 0; neither this nor BGHS's positive density from p^{1/(4√e)+ε} (all d) says anything about HIT.
     Assessment: d ≤ p^{1/3} is where this lane's additive-character attack stops; "narrowed" = reformulation.
   * **Census (CERTIFIED).** BFF's independent decider (by d, integer-exact membership) re-certifies z56's range and finds
     no 𝔊*-zero in (10¹⁰, 10¹²]: R_𝔊*(p) = 0 at exactly 38 primes p ≡ 1 (4) ≤ 10¹², the last 564 661 441 (hence R(p) ≥ 1
     for every prime p ≡ 1 (4) in (10¹⁰, 10¹²], since R(p) ≥ R_𝔊*(p)). Provenance: the cross-review exhaustively reran [5, 10⁹] and parsed and spot-checked
     all 192 blocks, not the full 10¹² run; BFO's run of the z56 decider separately covers (10¹⁰, 2·10¹⁰] (cross-review
     reproduced prime counts and exceptional rows, not the full solution census). Side result: the Burgess-only family
     𝔊*_{1/15} has a new zero 11 406 999 713. EVIDENCE: the largest least-hit modulus is d = 787 439 ≈ p^{0.705} on (10⁸, 10⁹];
     per-block maxima stay below p^{0.64} on (10⁹, 10¹²]; the zeros lean towards pseudo-squares (least prime non-residue ≥ 11 at 20/38), but 8
     have it equal to 2. Model tails beyond 10¹² are extrapolations only.
   * **Complementarity (`Z57_COMPLEMENT.md`; corrected after a cross-model REJECT).** Menu: (★), b = 1 line, Type I a = 1
     slice (with boundary words), c = 2, 3 Type II lines, 𝔊*, its corner. Lemma W (PROVED): all are cells of the word sets
     W(p) = {tuv − u − v = p} or W(cp); on interior words of W(p) the (★), b = 1, Type I cells are exactly the
     Jacobi-(−1) words. Theorem C (PROVED via Bombieri–Vinogradov; fixed U ≥ 1, 0 < θ < 1/4,
     4·lcm(1..U) | M, gcd(a, M) = 1; averages over primes p ≤ x, p ≡ a (M); fixed nonempty sets of unit classes modulo
     q, q′ dividing M; divisors m ≤ x^θ coprime to M; fixed positive u ≤ U, b, c): (i) class counts on the same integer p + u, u ≤ U, have
     covariance ≥ κ(log x)³ − C(log x)²; (ii) on different integers p + u, cp + b (cu ≠ b), provided every prime of
     b·c·(cu − b) divides M, covariance −Θ((log x)²) (CRT exclusion, correlation ≍ −1/log x). Not about a single p (B6).
     Prop F (CERTIFIED, census n ≡ 1 (4), 5 ≤ n ≤ 4·10⁶): for every pair of {(★), b = 1, Type I a = 1, c2, c3} there are
     non-square composite joint zeros; at primes "R_A = 0 ⟹ R_B ≥ 1" is false for (★)⇒c2 (102001), (★)⇒c3 (577, …),
     b=1⇒c2 (193, 2521), b=1⇒c3 (193), and the reverses. Census (CERTIFIED counts): at primes Type I a = 1 never vanishes
     and no prime zero of the union of the three, or of all five, families occurs; at non-square composites the union
     (★) ∪ b=1 ∪ Type I vanishes only at 105 and the five-family union never (c2(105) = 1). EVIDENCE: all 21 certificate pairs
     have positive residual correlations after local controls except c2–c3 at 10¹³ (−0.004, within one nominal s.e.); rough semiprimes show the same joint law. Not
     excluded: pointwise complementarity at primes for (★)&b=1, (★)&Type I, b=1&Type I, Type I&c2, Type I&c3 (no joint
     prime zero ≤ 4·10⁶). Assessment: a union theorem over this menu would need a new exact relation between divisor
     classes of different integers (none known); not a necessity theorem.
4. **CLOSED (z53).** `Z53_GENUSLVAL.md` Thm U (PROVED, unconditional, effective; cross-model reviewed CORRECT): M_gen(p) ≥
   (2/(3π⁴) − o(1))(log p)² ≈ 0.0068 log²p at every sufficiently large prime p ≡ 1 (4). It uses Burgess for cube-free conductors on Thm 5.4's
   subfamily with sharp windows. The square-sensitive step is that ηχ_{−4up} is non-principal because p divides its
   conductor, and this is the step that fails at odd squares. Still open: the transfer X(p) ≥ −(1 − ε)M_gen(p), which is
   ES-(★) strength (see item 3), and the sharp constant (observed min 0.084, sample-specific). *(z56: the proved asymptotic
   lower-bound constant is now 5/(4π²) ≈ 0.1267, i.e. (5/6 − o(1))M₀, by `Z56_FAMDESIGN.md` Thm V; effectivity is established
   here for the Burgess-only constant 29/(30π²); effectivity of the HB constant was not audited. The sample minimum 0.084
   at p = 8089 lies below both asymptotic coefficients, which does not contradict an eventual lower bound.)* *Original item:* **A polylog lower bound
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
    *(z56, `Z56_PRIMET1.md`; EVIDENCE lane; internal hostile review + cross-model review; `Z56_SUMMARY.md` §5.)* A
    search with 16 initially registered invariant families and one added by amendment (local git provenance); the primary
    block was held out, but later analyses reuse data and include in-sample nuisance fits: h(−4p)
    and its 2-, 3-, 5-parts; h(p); regulator and Pell period; L(1, χ_p) beyond q ≤ 1000; least non-residue; ord_p 2, ord_p 3;
    Frobenius in x³ − x − 1 and x⁴ − x − 1; Gaussian/Eisenstein Hecke angles; the Sato–Tate angle of 11a1; p-adic depth;
    Legendre symbols beyond 1000; smoothness of p ± 1; generalised near-squares. Data: 6.7·10⁶ primes p ≡ 1 (24) in
    [10⁷, 10¹⁰] with exact R, 25 000 at 10¹²–10¹³, the hardest 0.01 % of (10⁹, 10¹⁰], the 14 zeros, HC at 10¹². Real-field
    class-number/L-value computations use GRH-conditional PARI output; the R counts are exact.
    * Most detected associations beyond the pre-registered local model track local data, the BM or genus-layer L-values
      (h(−4p): ≈ +4.7 % of E[R] per SD given exact BM, missing from the BM-only model), near-squares, or the u = 1 / B = 1
      tickets 2τ₃(p + 1). The remaining tested families show no significant *linear* association in A5/A6 after the
      stated local and L-value adjustments; a small nonlinear Hecke-angle signal is consistent with square-offset
      near-squares (augmented-null replication pending). S4b-r’s nuisance residual and tail threshold were fitted in-sample.
    * One unexplained candidate association (A9): large prime factors of p − 1, ≈ +0.6 % of E[R] per SD. Pre-specified
      two-feature confirmation on B₂₃: p_Holm = 0.01397 over 2 tests; post-hoc complete-null robustness 0.004058 over 2,
      0.03043 over 15 rerun families (not a second independent confirmation; the robust rerun excludes 337 B₂₃ rows previously used
      in S2); underpowered at 10¹²–10¹³ (p ≈ 0.87). No
      mechanism; confounding by local data at larger moduli unresolved. A small bulk association, not an observed kill.
    * Invariant-free test T2T (sensitivity analysis, not a bound): the disjoint ticket families 4Cp + 1 and p + u show no
      positive residual correlation given local data (ρ̂ = −0.005, nominal Fisher 99 % CI [−0.011, 0.001], conditional on
      fitted means and sampling assumptions); opposite-sign factors can
      mask coupling, so this excludes no common factor.
    * All Holm levels are blockwise; no study-wide alpha plan. Rare, nonlinear, density-zero or unsampled-range mechanisms
      (10¹⁰–10¹² mostly unsampled) are not excluded. Assessment: consistent with "local main term × lottery" in the
      sampled ranges; nothing about a fixed prime (B6).
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
18. *(z58, `Z58_SUMMARY.md` §5; none of these is a lead.)* **Targets and named escapes from the (MS) probe.**
    * **CONV-II (hot target, statement level; CONJECTURE).** Every odd non-square n ≠ 4545 has N_II(n) ≥ 1 (§2.4).
      * Prime form: (MS-II) for p > 10¹⁷ in 𝔐.
      * It is equivalent to IHP_BM for the positive-integral Type II model at every odd n ≠ 4545 (`Z58_STRUCT2.md` §5.1).
      * *Why:* at the z58 checkpoint it was singled out as the only carried target whose statement passes F1–F4 (§4) in
        the tested ranges (statement-level, not a mechanism). z59 adds the smaller-family CONJECTURE U_II with explicit
        exceptions {105, 4545} (item 19).
      * PROVED witness constraint: for odd positive n, every positive Type II witness supplies f = 4acd − 1 with
        (n/f) = −1. Assessment / proposed strategy: seek a pointwise Type II construction using non-squareness and
        resolving the tied divisor-class event (B2). This is not a necessity theorem about how every proof of CONV-II,
        (MS-II) or ES must be organised; no such mechanism was found. Using c ≥ 2 is a strategy, not forced at 10¹⁷.
      * Sub-targets: the a = 1 line (López's "Type A"; prime zeros 193, 2521, 66529) and its union with c = 1, which has
        no prime zero ≤ 10⁸ (`Z58_CONVF.md`, CERTIFIED). Also CONV-II-15 (coprime ET form for gcd(n, 15) = 1) and eventual positivity of
        N^{(K)}. And a composite genus analysis that survives the conductor cancellation seen at 4545 = 505·3², u = 505.
    * **(MS⁺) (CONJECTURE).** R(n) ≥ 1 for non-square n > 17 401 609 in 𝔐 (§2.4).
      * A primality-blind proof would suffice, and the data (to 10¹¹, one engine) allow it.
      * Calibration (`Z58_LOGIC.md` Thm 3.1, rel. Buss): an S¹₂ proof of (MS) yields a polynomial-time
        hit-or-nontrivial-factor-pair algorithm on n > 10¹⁷ with n mod 840 ∈ 𝔐. It must find hits at those primes and
        split any composite R-zeros in that domain (not a general factoring algorithm).
    * **Remainders behind proved surrogates.**
      * E₂(p) > −M₂(p) pointwise (`Z58_TRYF2.md`). A mechanism coupling hits across C or u would count as a lead there.
      * A rigorous bound for the real layer L_r (`Z58_TRYF.md`; Shiu + Pólya–Vinogradov suggested). The non-real layer L_n
        is open.
    * **Named escapes from the z58 scoped no-gos (§3).**
      * AUTOMORPH: E1, half-integral weight (Prop C is CONDITIONAL on the unproved (H_E)); E2, coefficients outside 𝓗; E3,
        higher depth; effective signed minorants.
      * TERNARY: cusp nonvanishing on 𝔐, which for one eigenform is Goldfeld-type when the root number is +1. The
        Waldspurger screen (ψ = 1, Cor 2 with anchors) found no valid and effective single-eigensystem R-support proxy
        among 15 L-functions (EVIDENCE); it does not constrain Type II support. *(z59: superseded on 𝒞₁ by
        `Z59_WALDS.md` W1 + W4 — only Gauss-exceptional eigensystems survive; remaining escapes in item 19.)* Also E1′ (a thin-set Heegner
        hypercycle-incidence theorem) and off-𝒞₁ classes.
      * STRUCT/STRUCT2: the Brauer set of S°; fibre arithmetic (factorisation of kCn + 1, n + u); equidistribution on
        fibres.
      * MORDELL: the five non-unit Mordell classes (5-/7-adic coordinates).
      * WITNESS/LOGIC: CONJECTURE W (min(u, B, C) ≤ (log p)² for p > 8 813 281) and CONJECTURE FQ_u(A); growing polylog
        (u, B) menus.
      * FFIELD: fixed-q eventual MS_q (CONJECTURE, N₀(q) → ∞); a faithful C-parity / 𝔊* model.
      * LADDER: cap rungs k ≥ 2; covering scales p^{0.15}–p^{2/3}.
    * **Disproof side** (`Z58_DISPROOF.md`): a slowly decaying zero-law mixture, growing offsets, other polynomial families,
      or a non-local "prime T1" (cf. item 15).
19. *(z59, `Z59_SUMMARY.md` §5; none of these is a lead.)* **Sharper targets after the survivor probe.**
    * **CONJECTURE U_II / (MS-U)** (`Z59_CONV2.md`; §2.4 z59). Every odd non-square n ∉ {105, 4545} has U_II(n) ≥ 1, U_II = (c = 1) ∪
      (a = 1); equivalently some Tn + 1 has a divisor ≡ −1 (mod L_T), L_T = T (4 | T), 4T (else). CERTIFIED to 10¹⁰; at primes
      López's Conjecture 1. (MS) ⟹ (MS-U) ⟹ (MS-II). *Why:* in the certified range the screens do not need the full Type II
      family beyond U_II (only at n = 105), so a fixed-p argument for **one line** T ↦ E(Tp + 1, L_T) suffices for (MS-II); the
      a = 1 branch itself uses c ≥ 2. U_II asks for more than CONV-II; that it is harder to prove is not claimed. EVIDENCE: in the
      ≤ 10⁷ mask experiment all three non-zero T mod 4 classes are needed to recover the full-U_II zero set (T ≡ 0 is
      redundant for a = 1 rescue by Prop 3.1); finite evidence, not an eventual necessity theorem.
    * **(MS⁺) and its primality-free variants** (`Z59_MSPLUS.md`; CONJECTURE). (MS⁺) is CERTIFIED to 10¹² (one engine).
      (MS⁺₁₀₅): all classes with gcd(n, 105) = 1, threshold 29 210 401; (R⁺_y), y ≥ 47: all prime factors > y, threshold
      8 813 281; both CERTIFIED to 10¹⁰. *Why:* clean screens, no Mordell input, negligible model tails (EVIDENCE, model
      only). Reusing an (MS) proof for fixed-y-rough non-squares requires every primality-dependent step to remain
      valid, and initially gives only the Mordell domain and threshold 10¹⁷; the all-class (R⁺_y) also needs removal of
      any Mordell-class dependence and coverage down to 8 813 281 (the census to 10¹⁰ does not cover a gap up to 10¹⁷); a
      proof needing y(n) → ∞ is not a proof of (R⁺₄₇). Versions allowing 3 | n keep zeros past 10¹⁰ (9 with 105 | n in [10¹⁰, 10¹¹]).
    * **Zero-law questions** (`Z59_MSPLUS.md` §3; EVIDENCE): derive the true second-order class mean (the proposed one was
      withdrawn); explain the ≈ 6× excess of 𝔐-prime zeros at 10⁶–10⁷ and the ≈ 1.4–1.5× under-prediction in later decades
      (the ≈ 1.5× fit concerns only the four large training groups; OOS g21 ≈ 3×, held-out g7 ≈ 17× off).
    * **Half-integral-weight escapes** (`Z59_WALDS.md` §7): (E-a) levels with several Gauss-exceptional φ and a validity
      identity proved from independent arithmetic or structural input, rather than assumed from the desired eventual
      positivity (none supplied; W5 is an equivalence, not an exclusion of independently proving an equivalent statement); (E-b) coset thetas / theta series with
      characteristics (Thm F, W0 unproved there); (E-c) mixed-ψ signed combinations; (E-d) higher half-integral weight;
      (E-e) off-𝒞₁ classes remain open; for a strategy relying on termwise recipe lattices, a fixed finite level menu
      misses primes ≡ 1 (mod 8∏ℓ), so reaching every hard prime by this mechanism needs growing/adaptive levels with some
      odd level prime ℓ, (p/ℓ) = −1 (hence ℓ ≥ n_p; B2 again). Not a necessity theorem for arbitrary signed
      multi-eigensystem proxies.
    * **ρ-residues** (`Z59_CONVO.md` §3–§4): control the residues mod ρ of the individual prime factors of (p + ρ)/4 beyond
      the quadratic colouring (ℓ/p). Witnessing ρ is ≤ 107 for p ≡ 1 (24) ≤ 10⁸ (CERTIFIED) but unbounded under Dickson.
20. *(z60, `Z60_SUMMARY.md` §5; none of these is a lead.)* **Sharper targets after the clean-statement attack.**
    * **CONJECTURE U₇ / (MS-U₇)** (`Z60_LOPEZ.md` §4.2; §2 z60). Every odd non-square n ∉ Z₇ = {105, 1465, 3865, 4545, 10305,
      12145, 39361, 67425} has some f ≡ 7 (mod 8) with (−n mod f) | f + 1. CERTIFIED to 10¹⁰ (all odd n) and on 𝔐 to 10¹² (one
      engine above 10⁶). *Why:* sign-free and branch-free (one congruence class of moduli, divisor targets of f + 1), T1
      automatic; on n ≡ 1 (4) it sits between (★) and U_II, so (MS) ⟹ (MS-U₇) ⟹ (MS-U) ⟹ (MS-II). It asks for more than U_II
      (8 zeros vs 2); that it is easier is not claimed. Constraints on the full CONJECTURE U₇ (not on (MS-U₇), which starts above
      10¹⁷): U⁽⁸⁾ ⊂ U₇ (at its in-domain U⁽⁸⁾ failures use the targets with v₂((f+1)/8) < v₂(r) < 3); the eight
      composite zeros; no p-independent branch link (Prop D); adaptive links / counting not excluded.
    * **(MS⁺₁₀₅) survives the near-square threat** (`Z60_MS105.md`, `Z60_MS105T.md`; CONJECTURE). Open: finiteness of zeros in
      any family, density-zero non-algebraic families, sporadic zeros. Missing input (Assessment): pointwise lower bounds for
      divisors of n + k or 4Cn + 1 in progressions whose modulus grows with the shift; a proof must use C odd somewhere (the
      certified in-𝔐 R₈ zeros near 10¹⁰ are coprime to 105 and above 29 210 401, hence in the domain). Depth-bounded strengthenings of non-squareness only fix where the witness search starts.
    * **Automorphic** (`Z60_SIGNED.md` §§5, 7): an independent validity mechanism for sums of Gauss-exceptional Shimura
      components (structural weighted certificate; termwise lattice / coset recipes excluded on 𝒞₁, cosets CONDITIONAL);
      pointwise non-degeneracy S(p) ∉ W (under W1′'s non-zero-L-anchor / (H2) hypotheses, with Λ the full span of the
      exceptional lines **and W = 0**, this is (𝒟_N): for every prime p ∈ 𝒞₁ above the threshold there exists an exceptional
      G_φ, possibly depending on p, with L(½, G_φ ⊗ χ_p) ≠ 0; in general a linear condition on signed square roots of central
      values); whether a mixed-ψ signed proxy in weight ≥ 5/2 can be positive at all large 𝔐-primes; objects where (Dom)
      fails; non-quadratic nebentypus; varying / adaptive levels (open; the q ≥ n_p requirement is only for the termwise
      recipe-lattice / off-𝒞₁ strategy, not a necessity theorem for arbitrary signed or multi-eigensystem proxies). The "≥ 5 independent rational lines" CKRS summability
      argument is heuristic.
    * **Encodings from RAYCLASS / DYNAMICS / TRACE** (none supplies positivity): (E1) a non-CFT relation linking individual
      prime factors of 1 + r√(−t₀p) across levels C (shared primes q | C − C′), twist averaging via the Prop 5.2 box identity,
      cross-field characters as sieve input (Prop 4.1's quartic identification sample-certified only); target-specific
      cancellation on the QNR half-orbit (n ≡ 1 (4)) and orbit holes;
      single-N trace bounds (odd k) sharper than Deligne with slack ≪ (ε∞/2)·ES at Mordell-hard primes. **Prove `Z60_TRACE.md`
      Lemma 3** (local f-sum / embedding identity; CERTIFIED on 21 044 cases) to make the Γ(4C) trace identity a theorem.
    * **López union, P* form** (`Z60_LOPEZT.md` §3.4): at an S₈-zero prime inside a theorem's range, S₄/P* witnesses
      must use g ≡ 3 (8) or a non-liftable U5 divisor (an eventual claim may exclude these finite failures by its threshold); least
      witness g* ≥ (1/5 − o(1)) log p infinitely often (PROVED), ≤ 10487 for p ≡ 1 (24) < 10⁸ (CERTIFIED).

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
* **Wave z58** (`Z58_SUMMARY.md`): `Z58_{WITNESS,FFIELD,AUTOMORPH,MORDELL,LADDER,WILDCARD,STRUCT,STRUCT2,LOGIC,DISPROOF,
  LIT,TRYO,TRYF,TRYF2,TERNARY,CONVF}.md`; cross-model reviews `data/z58/xreview/`; falsifier screens `data/z58/screens/`.
* **Wave z59** (`Z59_SUMMARY.md`): `Z59_{CONV2,CONVO,WALDS,MSPLUS,MSPF}.md`; cross-model reviews `data/z59/xreview/`; data
  `data/z59/<lane>/`; papers changes `data/z59/papers/CHANGES.md`.
* **Wave z60** (`Z60_SUMMARY.md`): `Z60_{LOPEZ,LOPEZT,MS105,MS105T,SIGNED,RAYCLASS,DYNAMICS,TRACE}.md`; cross-model reviews
  `data/z60/xreview/`; data `data/z60/<lane>/`; scripts `scripts/z60_<lane>_*`.
* **Reviews:** `reviews/` (hostile reviews per result), `reviews/agent-reports/` (task reports O1–O279), novelty audits
  `reviews/novelty-audit-2026-10*.md`.
