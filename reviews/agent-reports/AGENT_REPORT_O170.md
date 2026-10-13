# AGENT_REPORT O170 — exact identities with growing level (checkpoint 1)

Branch side-agent/growing-identities. Main file GROWING_IDENTITIES.md; scripts scripts/gi_*.
**ES is not solved; no infinite case of it is claimed.**

## Results (labels as in DISCOVERIES.md)
1. **PROVED (elementary): exact growing-level rewrites.** Type I a = 1 / Type II as negative continuants
   (n = K⁻(c,g,f), cn = K⁻(a,4cd,b)); W-certificates with all entries ≥ 2 ↔ m ≡ 0 (4) with n/m of
   Hirzebruch–Jung length 3 (Lemma 1.1; boundary words with an entry 1 are extra and are the only certificates
   at n = 5, 17, 41, 65, 209, 241, 265 among n ≡ 1 (4) ≤ 300 — R170 repair). Two inequivalent growing-level divisor sums for the same cubic (fibre by g vs by c; Lemma 1.2).
   Swapping summation (brief idea (a)) produces a congruence modulo the summation variable — no telescoping.
2. **PROVED: the sign at ∞ is the genus character at n (Prop 4.1).** For n ≡ 1 (4), t ≡ 3 (4), tn+1 = m m'',
   4 | m, m'' ≡ ε (t): (m''/n) = ε. Hence W(n) = Σ_{D*(n)} (1 − (m''/n))/2 over the finite sign-blind set D*(n) = D(n) minus the trivial m'' = 1
   (all its elements have t ≤ n + 2; R170 repair — D(n) itself is infinite): a T1-respecting
   identity at level n·t (outside Thm 9.1), but positivity = "the genus character at n is not constant on D(n)"
   = the H-B spin event of O165. Checked on 519508 pairs (n ≤ 4000), 0 exceptions.
3. **PROVED relative to Cohen's Eichler–Selberg formula (implemented, scripts/gi_trace.py, transcription
   checked against genus X₀(N), X₁(q), S₁₂(1), 11a):** ES = sign-odd part of the split-hyperbolic (cusp fixed
   point) term (Prop 2.1); the ES class −1 always comes with class +1 (incl. the trivial divisor) and the sign is
   visible only to odd weight. Prop 2.2 (R170 repair: PROVED part = trivial bounds only; rest Assessment): the
   ES term is typically small (not at genus-0 levels, where A₂ = −A₃ exactly); certifying it needs the cusp
   trace ≍ kq-fold (dim S_k(Γ₁(q))/(φ(q)/2); earlier "q²" was off by ≍ φ(q)) below Deligne at one N. Weight 1
   (outside Cohen's k ≥ 2) heuristically corresponds to O131's finite Eisenstein identities.
4. **Assessment (§3):** KH re-sums shifted class numbers because the shift t is a theta-series variable and
   holomorphic projection lands in a finite-dimensional space; ES shifts gN + 1 are multiplicative (U_g-type,
   levels ≍ g²), so no analogous re-summation exists in that framework.
5. EVIDENCE: sign-blind total S(n) is of equal size at primes and odd squares; at squares class −1 mass moves to
   class +1. Not an exact conservation law. (R170 repair: the original census was for n ≡ 17 (24), mislabelled
   ≡ 1 (24); corrected n ≡ 1 (24), 4001..6000: primes total 30.0 with class −1 mean 7.2, squares total 29.8.)

## Honest verdict
No positive exact identity. The three outcomes (relabelling; subdominant term; reduction to H-B spin) are the
precise reasons. The most informative new item is Prop 4.1 + Prop 2.1 together: *every geometric count is
sign-blind, and the sign is exactly the quadratic character at n* — this unifies O128 Prop 8.3, O131 Prop 4.1,
O165 Lemma 1.3 for slice a = 1.

## Sparks (not pursued)
* Odd-weight / spin-structure Lefschetz: a geometric object on X₁(q) that *does* see P vs −P (theta
  characteristic, the line bundle ω of odd weight); a holomorphic Lefschetz formula for ω^{odd} with a positive
  main term would be the first sign-seeing count. At weight 1 elliptic terms vanish (Prop 2.2) — study what
  replaces cusp traces there (Serre duality pairs S₁(χ) with S₁(χ̄)).
* Kudla special cycles for the *indefinite* binary T = 4·[−dp, 1, c²] in the signature-(2,1) lattice
  ((I)4): the cycle is empty, the arithmetic (derivative) version might carry the sign.
* Dedekind sums at prime p restricted to m ≡ 0 (4): exact class-number main terms (h(−p), h(−4p)) with uncapped
  HJ weights; HJ length 3 is the certificate. Only r − s is Dedekind-sum-determined; a second exact statistic
  fixing r would make this live.
* Is S(n) (sign-blind total) exactly expressible by local data after a natural weighting (e.g. min(m,m'')
  weights from weight-2 A₃ summed over t)? If so ES ⟺ class(+1) < S.
