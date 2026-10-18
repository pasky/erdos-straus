# AGENT REPORT O265 — mod-p power-residue reciprocity / Gaussian-representation certificates (spark relay on O263 sparks 1, 4)

Branch side-agent/modp-reciprocity (O263's branch side-agent/class-forcing is merged in, as instructed). Main file
`MODP_RECIPROCITY.md`; memos `BRAINSTORM/z35_*.md` (8, indexed in BRAINSTORM/README.md); scripts `scripts/z35_*`; logs
`logs/z35_*` (tiny). **ES is not solved; no infinite case of ES is claimed.** A self-review by a separate subagent (no FATAL;
7 MAJOR on wording/scope, all repaired in commits "repairs …") preceded this report. R272's notes on O263 (Thm 6.1 FATAL,
"parity never class" overclaim) are taken into account: nothing here relies on CLASS_FORCING Thm 6.1.

## SHARP: none in the breakthrough sense. Mildly sharp, for the orchestrator to judge:
1. **Window selection rule of a representation (Prop 5.1, PROVED, 0 exceptions to 10⁶).** If p = x² + Dy² (or 4p = x² + Dy²,
   gcd(x, Dy) = 1), then every odd b = 1 window m | y is sterile, and an odd window m | x is sterile iff (D/m) = +1; if
   (D/m) = −1 the Jacobi obstruction disappears (firing rate ≈ 1.8–2.1 % vs ≈ 1.25 % controls). This is where p's canonical
   √p-size data (a, b; x² + 2y²; x² + 3y²; the cubic Jacobi sum 4p = L² + 27M²) meet the balanced range of the b = 1 line,
   and their whole visible effect beyond congruences is quadratic.
2. **Non-abelian data: inert for fixed finite witness sets, complete at unbounded level (Prop 2.1/2.2).** The order-4 characters
   χ_π at the primes q ≡ 3 (4) determine π (a two-line Dirichlet argument). So the "independent non-abelian part" of R272 D2 is
   independent only for fixed finite witness sets; no independence barrier can be proved at unbounded level. (The quadratic
   symbols also determine p, so this is a framing correction, not a deep fact.)
3. **Square levels d = k² are favoured (1.07 % vs 0.88 %, EVIDENCE), explained by an algebraic factorisation of the witness**,
   4j²k² − 1 = (2jk − 1)(2jk + 1) (naive prediction ratio 1.19, observed 1.22): a Sophie-Germain-type effect on the witness, not
   on p.

## What was done (labels as in the file)
* §1 (PROVED): b = 1 line in mod-p coordinates: 4md − g = p, g | m + 1 (the height-one solution of 4md ≡ g (mod p));
  equivalently "(−p mod 4m) | m + 1", or the e-slice form. Residue-symbol content of a certificate: the quadratic part consists
  of Jacobi symbols among the parameters (forced; the T1 sign); the quartic part is a function of (a, b) modulo the parameters
  (Gauss–Dirichlet–Burde; Burde's law checked on 2158 pairs; (q/p)_4 as a function of (a, b) mod (4q, 8q) checked for q ≤ 37).
  Answer to goal (1) (Assessment): we found no power-class reformulation of the target; it is additive.
* §2: Prop 2.1 (Chebotarev), Prop 2.2 (Dirichlet). EVIDENCE 2.3: quartic data of 2, 3, 5, 7, 11, 13 do not move b = 1 hit
  rates at levels d ≤ 40 (240 stratified tests, max |z| 2.46); the canonical quartic bit (2w/p)_4 of witnesses (p ≡ 5 (8)) is
  balanced 49.9/50.1 % over 5.6·10⁵ witnesses — no "quartic T1".
* §3: the brief's premise that (J)78/(J)79 do not apply to identities in (a, b) is incorrect: (J)3 Thm 3.2, (J)78 Thm 1.1 and
  (J)79 Cor 3.2 are stated in the norm-form variables. Lemma 3.2 (local T1, PROVED): windows modulo which p is a unit square are
  sterile (with a 2-adic condition for even windows). Prop 3.3 (PROVED, whole-class form only): polynomial families in the
  √−1 lift (X, N), X² + 1 = pN, are T1-barred on every class n ≡ 1 (M); sectors and least lifts are not covered (would need
  equidistribution of roots of X² ≡ −1 mod s²). EVIDENCE 3.4: no Gaussian-canonical quantity is a better level than
  neighbour-prime controls.
* §4 (spark 4): Prop 4.1 (PROVED): at d = k², (p/ℓ)_4 = (k/ℓ) and (ℓ/p)_4 = (k/ℓ)((a c_ℓ − b e_ℓ)/ℓ) (Burde); every term of the
  product formula involves the unknown ℓ, so there is no p-only constraint. Spark 4 closes negatively.
* §5 (goal 4): Prop 5.1 for D = 1, 2, 3, 7 and the cubic Jacobi-sum datum (D = 27); cubic data behave exactly like quartic
  data.
* Numerator-8 check: moot (nothing positive claimed). T1: all statements are negative or dictionaries; at squares there is
  nothing to check beyond ET Prop 1.6.

## Points for the reviewer
* Prop 1.2(b) for q ≡ 3 (4) uses biquadratic reciprocity with the primary normalisation; the exact sign bookkeeping is
  delegated to the numerical single-valuedness check (z35_quartic_function), not written out.
* Prop 2.1's scope is fixed finite (d, w) sets; a fixed level with unbounded witness is only EVIDENCE.
* Prop 3.3 is whole-class only (the sector version is an open technical point).
* EVIDENCE 3.4's z-values use a naive variance with correlated neighbour controls; they are indicative only.

## Sparks (not pursued)
1. The free quartic bit β(w) = (2w/p)_4 of b = 1 witnesses (p ≡ 5 (8)) is a canonical ±1 function on each prime's certificate
   set. Is it the sign of an involution on certificates, or a quartic Hilbert-symbol / Brauer–Manin-type pairing on the ES
   surface? An exact law for Σ_w β(w) would be a new invariant, even though β is not forced.
2. Prop 5.1 at all class-number-one D at once (D = 1, 2, 3, 7, 11, 19, 43, 67, 163, when p is represented): the permitted
   windows m | x_D with (D/m) = −1 form a canonical, p-dependent, non-congruence menu in the balanced range. Its union firing
   probability at large p is ≈ p^{−1/2+o(1)} per balanced ticket — dead as stated, but a genus-theory version (non-principal
   forms, all D ≤ p^ε) might give p^{ε}-many tickets.
3. Sector version of Prop 3.3 via Hooley/DFI equidistribution of roots of X² ≡ −1 (mod s²) for prime-square moduli.
4. The square-level excess (§4) suggests ranking b = 1 levels by Σ_c 1/φ(4cd − 1): levels whose witnesses 4cd − 1 have
   algebraic factorisations (cd a square, or 4cd − 1 = a cyclotomic value) are systematically richer. Does the least successful
   level of the hard primes (193, 2521, 66529) or of the (★) failures sit at such levels?
