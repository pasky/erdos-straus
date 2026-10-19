# FRONTIER — the Erdős–Straus problem as of 2026-10-19: where to start

*Audience: a strong number theorist (or a fresh AI team) who has never seen this repository and wants to start from the current
frontier instead of rediscovering it. Task O279 (consolidation C3). No new mathematics here: every statement is a summary of a
repository file, with a pointer. When a summary and its source disagree, the source wins.*

> **The Erdős–Straus conjecture (ES) is not solved — not here, not anywhere.** No case of "ES for all large primes" is
> proved here, conditionally on any standard conjecture or otherwise. The literature was checked through 2026-09-28
> (`LITERATURE_2026.md`) and spot-checked on 2026-10-18; every recent claimed proof has an identifiable gap.

**Labels** (as in `DISCOVERIES.md`). PROVED = complete proof in the repo, possibly *relative to* named published theorems;
CONDITIONAL = proved assuming a named hypothesis (GRH, Dickson, Hypothesis H, SEL, …); CERTIFIED = an exact finite computation,
independently reproduced; EVIDENCE = numerics or heuristics only; CONJECTURE = stated, open; Assessment = a judgement or
interpretation, not a theorem. Everything PROVED here is *internally* reviewed (hostile reviews in `reviews/`), and **none of it
is externally refereed.** Pointers like (J)100 are entries in the ledger `DISCOVERIES.md`.

**One-paragraph summary.** After ~280 tasks, 13 phases and two advisory boards with seats from three labs, every route the
campaign or its sibling (`../erdos-straus-astra`) tried ends at one statement: *a single specific integer, determined by p,
must have a divisor in a residue class whose modulus is itself part of the solution* ("B2", the tied-modulus divisor
event), with only polylog(p) expected winners. In counting form this is a **one-sided lower tail at one integer**,
R(p) ≥ ε·M_BM(p), where the main term M_BM(p) ≫ (log p)² is now an unconditional theorem and the odd-square obstruction
(T1) is built into it exactly. No standard conjecture is known to imply this lower tail, and no technique in the literature
proves an every-n statement of this shape (polylog main term, no averaging). §3 maps the barriers as theorems with scopes,
§4 turns them into a five-minute screening checklist, §7 lists well-posed sub-problems.

## 1. The problem and the known landscape

**The problem.** ES: for every integer n ≥ 2, 4/n = 1/x + 1/y + 1/z has a solution in positive integers. A solution for n
gives one for every multiple of n, and the classes n ≡ 0, 2, 3 (mod 4) have identities, so ES reduces to **primes
p ≡ 1 (mod 4)**, in practice p ≡ 1 (mod 24). Mordell's identities reduce further: a counterexample must lie in
n ≡ 1, 121, 169, 289, 361, 529 (mod 840) — the square classes mod 840. These "Mordell-hard" primes are where all difficulty
sits (`AMPLIFY_EXCEPTION.md` §0, `LITERATURE_2026.md`).

**Verification.** ES holds for all n ≤ 10¹⁷ (Salez); Mihnea–Dumitru (arXiv:2509.00128, 2025, unrefereed preprint) report
10¹⁸ (`DISPROOF_AVENUES.md:63`). Internally (EVIDENCE): f_I(p) ≥ 1 and f_II(p) ≥ 1 for every prime 5 ≤ p ≤ 10⁸ (Type I and Type
II separately); min f_II/log³p ≈ 0.012 (STATUS, phase (I)). Adversarial searches at 10¹⁸–10²⁵ never approached failure: the
hardest prime found, p = 2054098191162848070241, still has 870 solutions on its cheapest 1024 e-slices alone
(`DISPROOF_AVENUES.md:246–290`, EVIDENCE).

**Parametrisations (Elsholtz–Tao, ET = J. Aust. Math. Soc. 94 (2013)).** For a prime p every solution is Type I (p divides
exactly one denominator) or Type II (two). In divisor form (`CONDITIONAL_ES.md` §1, PROVED):
* Type I ⟺ f | p² + 4c²d with f ≡ −p (mod 4cd); Type II ⟺ ff′ − 4c²dp = 1 with f ≡ f′ ≡ −1 (mod 4cd).
* e-slice form: ES(p) ⟺ ∃ e ≡ −p (mod 4) with −1 ∈ {ab⁻¹ mod e : ab | N}, N = (p+e)/4 (Type II) or (pe+1)/4 (Type I).
* Counts: Σ_{p≤N} f(p) is ≍ N log²N up to a log log N (ET Thm 1.1); the average of f(n) over all n is ≍ log³n; for almost
  all n, f(n) ≥ (log n)^{log 6 + o(1)} (Elsholtz–Planitzer). Expected solutions per prime are therefore *polylogarithmic*.

**The odd-square obstruction T1** (ET Prop 1.6; Yamamoto 1965; Bright–Loughran Cor 1.3–1.4). For odd m,
f_I(m²) = f_II(m²) = 0: odd squares have no Type I/II solutions, although all local, genus and spinor conditions hold there
(`reviews/redteam-automorphic.md` §4, phase (I) Prop 8.3). (ES(m²) is of course true, via ES(m).) T1 is the single most
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
§5, CERTIFIED; the 8/n failures are known, PW Table 1). 5/n and 7/n have no known exception (7/n: none in [3, 10¹³], PW).
This matters for §4: numerator 4 must be used.

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

**Census** (CERTIFIED, two engines): among primes p ≡ 1 (4), (★) fails at exactly **14 primes ≤ 10¹⁰**, from 409 to
8 813 281 ((J)89, `B1_LINE.md` §3.6); the b = 1 line (López 2024 Type A: p + 4d has a divisor ≡ −1 (mod 4d)) fails exactly
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

*Two normalisations of "the main term".* `PARITY_AUDIT.md` Lemma 2.1 writes R(p) = M(p) + E(p) with the trial-count main term
M(p) = Σ_𝓡 1/(4uC − 1) = (log p)²/8 + O(log p) (PROVED); `BM_CORRECTED_COUNT` uses the prime-averaged pair series M₀ ∼ 0.152
(log p)². These are different expansions; the repo does not reconcile the constants (1/8 vs 3/(2π²)), and nothing below
depends on the constant. Observed R(p) = 44, 52, 68 at p ≈ 10⁸, 10⁹, 10¹⁰ (EVIDENCE).

### 2.3 The exact theta-quotient normal form (PROVED; `METAPLECTIC_ES.md` Thm K, (J)101)

Fix the level t ≥ 2 and count *ES words of level t*, R_t(n) := #{(u, v) : u, v ≥ 2, tuv − u − v = n} (for 4 | t, t = 4C,
these are the (★) triples with that C, up to the boundary u or B = 1). Put X = q^{t−1}, Q = q^t, θ(x) = (x; Q)_∞(Q/x; Q)_∞,
D_t^∓(N) := #{d | N : d ≡ ∓1 (mod t)}, σ_χ(N) = Σ_{d|N} χ(d). Then (K1′)
  q^{t−2}(Q;Q)_∞² θ(X²)/θ(X)² = Σ_{n≥0} (D_t⁻ − D_t⁺)(tn + 1) qⁿ = −(2/φ(t)) Σ_{n≥0} Σ_{χ mod t odd} σ_χ(tn + 1) qⁿ,
and R_t(n) = D_t⁻(tn+1) − β_t(n) with the explicit boundary term β_t(n) = 2·1[(t−1) | (n+1)] − 1[n = t−2] (K2). So **each level series is an exact Kronecker theta quotient: Eisenstein
data only, no cusp forms.** For 4 | t, T1 is an exact cancellation (D_t⁻(tm² + 1) = 0). The all-level word series is
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

*Numerics for H⁻_BM* (EVIDENCE, primes ≤ 10⁶): min M_BM/L² = 0.062 (far above the proved 0.019), mean 0.149; P(R = 0 | M)
is ≈ 1.5–2.8 × the swap-Poisson value e^{−M/2} at M ≤ 22, possibly fatter beyond (6 zeros). Whether log P(0 | M(n))/log n → −∞
is "exactly the open question; nothing at 10⁶ decides it." Precedent for caution: for Markoff surfaces (same (log m)²
class-number scale) there are infinitely many integral Hasse failures *with non-empty BM set* (Loughran–Mitankin Thm 1.5;
Ghosh–Sarnak).

*Related exact reductions.* Five-slice ES (ES₅; λ(p) ≤ 3 in continued-fraction length) has a T1-exact BM main term with
principal constant **45/(8π²)** and unconditional Burgess bound M(p) ≥ (45/(32π²) − o(1))L² (`BOARD2_SLATE.md` Thm 3.5, (J)105;
this *corrects* the board memo's 33/(8π²), so cite BOARD2_SLATE, not the memo). In level coordinates
M_t^lev(n) = (τ(N) − σ_{χ_{−t}}(N))/φ(t) ≥ 0 (N = tn + 1), and **some 4 | t ≤ 4ℓ(n) has M_t^lev(n) > 0 iff n is not a
square** (ℓ(n) = least odd prime with (n/ℓ) = −1; `SYNTHESIS_SPARKS9.md` Prop 2.2, (J)103): *the BM layer is pointwise free.*
What remains is the class of the divisor inside the coset {χ_{−t} = −1} (size φ(t)/2), where the other genus and higher-order
characters are active. The expected number of "hit" levels is ≈ (0.44 → 0.97)·log p for p ≤ 3·10⁶ (EVIDENCE): critical, not
supercritical.
