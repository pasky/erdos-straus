# EXSET_CHAR_FORCING — pointwise character forcing "(q/p) = −1 ⟹ ES(p)" with a growing reach

*Wave z51, lane 2c, slug `forcing`. Brief: `/home/pasky/projects/math/z51briefs/2c_opus_forcing.md`. ES is OPEN; nothing
here claims it proved or disproved. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Scripts `scripts/z51_forcing_*`, data `data/z51_forcing/`, reviews `reviews/z51-forcing-*`.*

## 0. Summary table

| # | claim | label | review |
|---|---|---|---|
| 1.1 | F(R) ⟺ ES on {n₂(p) ≤ R}; F((log p)^A), A > 2 ⟹ X^{2/A+o(1)} exceptions (dyadic Linnik); under GRH F(2 log²p) ⟺ ES (large p) | PROVED (standard inputs) | R1: SOUND after dyadic repair |
| 2.1 | window criterion: ES at x ⟺ −1 ∈ R(px) mod 4x − p; Type II at x ⟺ −1 ∈ R(x) | PROVED (classical) | R1: SOUND (odd p) |
| **2.2** | **Kneser covering lemma**: in a cyclic group of order 2u (u odd), −1 ∉ ∏{g_j^{±1}, 1} ⟹ stabiliser H ≤ U, no g_j ∈ −H, #{g_j ∉ H} ≤ [U:H] − 1; sharp | PROVED; CERTIFIED (u ≤ 45) | R1: SOUND |
| 2.3 | anatomy of a failing forced window: all but ≤ d − 1 primes of x in an odd-order subgroup of index 2d ≥ 2ℓ_q; q = 3, and q = 7 for p ≡ 1 (8), never fail | PROVED; 936 643 checks | R1: SOUND |
| **3.1** | **fixed q: forced-window failure rate ≤ (log X)^{−1+1/(2ℓ_q)+o(1)} ≤ (log X)^{−5/6+o(1)}**, vs integer density (log X)^{−1/2} of the Landau mode that kills unforced windows; sharp for integers (3.2) | PROVED mod Henriot (upper bound only) | R1: SOUND-WITH-MINOR |
| 3.4 | G4 checked: refined at fixed q (upper bound); growing-q threshold heuristic (0.205); provable per-window range q ≤ (log X)^{0.4226} (Fourier, real/non-real split — R1's improvement) | PROVED pieces + Assessment | R1: MAJOR → repaired |
| 4.1 | fixed number of windows: product of single-window rates | PROVED mod Henriot (k + 1 forms) | R1: SOUND-WITH-MINOR |
| 4.2 | multiplying the two known per-window envelopes saves at most exp(−c(log X)^{0.4226−ε}) even loss-free; the many-window route is an RLD-*like* lower-tail problem | Assessment (exact arithmetic, specified envelopes) | R1: MAJOR (1/3 cap withdrawn) → repaired |
| 4.3 | joint failure of forced windows below the independence model in samples to 10¹²; hard primes have few or no successful forced windows (193: 0 of 18) | EVIDENCE | R1: wording repaired |
| 5.1–5.2 | **biased characters are rare**: #{p ≤ X : Σ_{q≤y}(q/p) ≥ 2ηπ(y)} ≤ X^{2/A+o(1)} (classical), ≤ X^{1/A+o(1)} for y = (log X)^A, any A > 0 (Heath-Brown); at scale P = C log X, ≪ X exp(−c log X/log log X) (Montgomery–Vaughan moments) | PROVED (mod HB 1995 / Lau–Wu Lemma 1) | R2: SOUND (5.1); 5.1′ is R2's; 5.2 new after R2 |
| 5.3–5.4 | robust reduction: ES power saving ⟸ *bias* of exceptional primes at scale (log p)^{1+δ} (MF); near-power bound X e^{−c log X/log log X} ⟸ bias at scale C log p (MF₁); both implied by majority reach (MR, MR₁). No GRH-equivalence with ES is known for MF₁ or MF(A ≤ 2) (MF(A > 2) is GRH-equivalent) | PROVED reduction; consequences CONDITIONAL on new, unproved sufficient hypotheses (not a counted T2-cond) | R2, R3: SOUND-WITH-MINOR after relabelling |
| **5.5** | **T2-lite: #{p ≤ X : e*(p) > (log X)^A/4} ≪ X^{1/A+o(1)} for every A > 1** (CAP_BOUNDED had A > 2, X^{2/A}); **#{p ≤ X : e*(p) > (C/2) log X} ≪ X e^{−c log X/log log X}** — transfers of Heath-Brown/Baier and Montgomery–Vaughan/Lau–Wu technology | PROVED mod Heath-Brown / Lau–Wu Lemma 1 (+ CAP_BOUNDED Lemma 3.1) | R3: SOUND / SOUND-WITH-MINOR; "T2-lite reached" fair |
| 6.1–6.2 | counterfactual reach for two ET subfamilies (height ≤ p, level 1 / all levels); Reach + (q/p) = −1 ⟹ ES | definitions; PROVED | R2: scope repaired |
| **6.3–6.4** | **reach is polylogarithmic on average**: for q ≤ (log X)^C, Σ_{p≤X} #reached ≪ π(X)(log X)³(log log X)², so Reach(p, q) holds for a ≪ (log X)^{3+o(1)}/q fraction of p; MR(A) false for A > 3 (two ET subfamilies, height ≤ p, all levels) | PROVED mod Shiu + Brun–Titchmarsh | R2 (6.3: SOUND); R3 (6.3′: MAJOR → completed with R3's argument) |
| 6.3num | reach numerics, 36 primes 10⁵–10¹⁰, q ≤ 1000: supply S_e ≈ 0.033 (log p)³ (fit 3.15); coupon comparison; q* ≈ 0.02–0.03 (log p)³/log log p; MR₁(½) at all 36, MR₁(1) at all p ≥ 10⁶; 2 682 witnesses exact | EVIDENCE / CERTIFIED (witnesses) | R2: reproduced |
| 7 | 17-line: Reach(p, 17) for 285/286 primes in [10⁶, 2·10⁶] and all 120 later samples; the failure (p = 1 240 009) misses the generic survivor cell 5, yet ES(p) holds by an actual-cell certificate; growing coverings need B2 events | EVIDENCE + Assessment | R2: dictionary corrected |
| 9 | remaining gap | Assessment | — |

**Bottom line.**
* No z51 target T1/T2-full is reached; ES remains open. There is no proof of any forcing reach, no Linnik
  confinement and no unconditional power saving for ES.
* **T2-lite reached (PROVED modulo Heath-Brown's quadratic large sieve):** the cap relaxation e*(p) ≤ (log p)^{A}/4
  holds outside X^{1/A+o(1)} primes for every A > 1 (CAP_BOUNDED needed A > 2), and e*(p) ≤ C log p outside
  X exp(−c log X/log log X) primes (Montgomery–Vaughan moments; this improves the cap exceptional-set bound at caps of
  order log p, a range CAP_INTERPOLATION Remark 3.2(c) lists as open for its own architecture). These are transfers of
  established least-non-residue technology (Heath-Brown/Baier, Montgomery–Vaughan/Lau–Wu) to the forced-window cap
  mechanism, found with the R2 referee.
* **A proved reduction with new conjectural inputs (not a counted T2-cond, R3):** if ES-exceptional primes are
  QR-biased on the primes in (C log p, 2C log p] (MF₁), then E_ES(X) ≪ X exp(−c log X/log log X), beyond the 3/4 CRT
  cap. MF₁ follows from a pointwise majority-reach hypothesis MR₁, which holds on every sampled prime (C = ½) and is
  predicted for all large p by the coupon model; MF₁ itself cannot be tested numerically (its antecedent is "ES
  fails"), and neither is shown visibly weaker than the conclusion. Proving MR₁ pointwise is a B2 statement.
* **G4 made exact at fixed q** (Kneser anatomy, upper bound (log X)^{−1+1/(2ℓ_q)}); the window route through G2 is
  limited to exp(−(log X)^{0.42}) by the known envelopes; **reach is polylogarithmic on average** (≪ (log p)^{3+o(1)}
  reached moduli q ≤ (log p)^C per prime on average, MR false above (log p)³), with supply consistent with cubic growth.

## 1. Audit

### 1.1 The route and the input it needs

Notation. p ≡ 1 (mod 8) prime (p ≡ 5 (8) and p ≡ 3 (4) are classical). For a prime q ∤ 2p, (q/p) = (p/q) by
reciprocity. n₂(p) is the least quadratic non-residue (odd prime here). ES(p) means 4/p = 1/x + 1/y + 1/z.

**Forcing hypothesis F(R).** For every large prime p and every prime q ≤ R(p): (q/p) = −1 ⟹ ES(p).

**Observation 1.1 (PROVED, standard inputs; this is G3 made exact).**
(a) ES ⟹ F(R) for every R (trivially).
(b) F(R) with R(p) ≥ (log p)^A, A > 2, ⟹ #{p ≤ X : ES(p) fails} ≤ X^{2/A+o(1)}. (With Heath-Brown's quadratic large
sieve, Prop 5.1′, A > 1 suffices and gives X^{1/A+o(1)}; with Prop 5.2, R(p) ≥ 2C log p gives X exp(−c log X/log log X).)
(c) Under GRH, F(R) with R(p) ≥ 2 log²p ⟹ ES(p) for all large p.
*Proof.* (b) Work on dyadic ranges (Z, 2Z]. If ES(p) fails there, then (q/p) = +1 for all q ≤ y := (log Z)^A.
Linnik's large sieve in the form of CAP_BOUNDED Thm 3.2, with 𝒜 = squarefree products of primes q ≤ y (no
congruence restriction on q), N = 4Z², |𝒜 ∩ [1, N]| ≥ N^{1−1/A−o(1)}, gives ≤ (N + 4Z²)/|𝒜| = Z^{2/A+o(1)} such p
(p > y, so no generator vanishes mod p). Summing over the O(log X) ranges gives X^{2/A+o(1)}; finitely many p below
the threshold of "large" cost O(1). (R1 repair: the earlier one-step split at X^{1/2} lost the exponent for A > 4.)
(c) Under GRH the least quadratic non-residue is < 2 log²p (Bach 1990, recalled); it is prime, and odd for
p ≡ 1 (8). ∎

Exact form (R1 repair): F(R) is equivalent to "ES(p) for all large p with n₂(p) ≤ R(p)" (for the other p the
implication in F(R) is vacuous). So F at reach ≍ log²p is, modulo GRH, *equivalent* to ES for large p; unconditionally
F((log p)^A) gives ES outside the Linnik set {n₂(p) > (log p)^A}. Note that F concerns **all** primes q, whereas the
forced windows of §§2–4 exist only at q ≡ 3 (mod 4); windows alone never supply F. Any proof of F at that reach is a pointwise ES theorem on the generic part of the
primes. This is why the brief asks also for (i) a reach for "all p outside a power-small set", (ii) weaker pointwise
inputs that still feed Linnik (§5: a *bias* suffices, and with Heath-Brown's or the Montgomery–Vaughan large sieve the
scale drops to (log p)^{1+δ} or C·log p), and (iii) quantitative versions of the gates.

### 1.2 Which gate each item attacks, and the door

* Item 1 (windows): G4 directly (per-window failure), then G2 (joint loss). Door: none new — the window mechanism is
  CAP_POINTWISE Thm 1.1; what is new is the anatomy of failures and a fixed-q upper bound (§§2–3), and the joint calculus (§4).
* Item 2 (reach): G3. The reach is a *counterfactual* (profinite) statement: "every non-residue class of p mod q, with
  p's residues at all moduli prime to q kept, carries a certificate" (for two ET subfamilies, height ≤ p). It implies
  F at q, is not implied by ES, and its failure set is a congruence-avoidance set with measured supply ≈ 0.033(log p)³/q
  per class (§6). Door used by Linnik: primality of
  the exceptional moduli (z50 B §4.2; outside the CRT caps).
* Item 3 (lines): G3 at fixed q = 17; finite coverings of the 17-generic line are conjecturally impossible (sterility
  at 17 is conditional on SIBLING Conj 4.2, (J)77), so p-dependent data are expected to be needed (§7).

Controls run on every mechanism below: odd squares (no windows exist at squares, CAP_POINTWISE Cor 1.2), numerator 8
at n = 17, 241, and the hard primes 193, 409, 577, 2521, 3361, 5569, 9601, 66529, 8813281.

## 2. The window and a sharp deterministic covering lemma (gate G4)

**Lemma 2.1 (window criterion; PROVED, classical).** Let p be an odd prime and x an integer with p ∤ x and 4x > p; put
m := 4x − p. Then 4/p = 1/x + 1/y + 1/z has a solution in positive integers y, z iff there are divisors d₁, d₂ of px
with m | d₁ + d₂. All divisors of px are units mod m (a common prime of x and m divides p, and p ∤ x;
gcd(p, m) = gcd(p, 4x) = 1), so the condition reads
`  −1 ∈ R(px) := R(x) ∪ p·R(x) ∪ p⁻¹·R(x),   R(x) := { ∏ s^{e_s} : |e_s| ≤ v_s(x) } ⊂ (ℤ/m)^×.`
The part −1 ∈ R(x) is *equivalent* to the existence of a solution with p | y and p | z ("Type II at x"; conversely
y = pa, z = pb give m/x = 1/a + 1/b, and the criterion produces divisors of x). The parts p^{±1}R(x) give solutions
with exactly one of y, z divisible by p (the three parts may overlap). ES(p) holds iff some x > p/4 with p ∤ x works.
*Proof.* a/b = 1/y + 1/z ⟺ ∃ d₁, d₂ | b with a | d₁ + d₂ (⟸: y = b(d₁+d₂)/(a d₁), z = b(d₁+d₂)/(a d₂);
⟹: with g = gcd(y, z), y = g y₁, z = g z₁ one gets y₁z₁ | b and may take d₁ = b/z₁, d₂ = b/y₁). Apply this to
a/b = 4/p − 1/x = m/(px). If d₁, d₂ | x then y = p·(x/d₁)(d₁+d₂)/m is divisible by p, likewise z. The case with p
dividing exactly one of d₁, d₂ (after cancelling a common p) is −1 ∈ p^{±1}R(x). Every solution has a denominator
prime to p (if p divided all three, 4 would be a sum of three unit fractions, which is ≤ 3). ∎

**Forced windows** (CAP_POINTWISE Thm 1.1). If m = q is prime with q ≡ 3 (mod 4) (so x = (p+q)/4 ∈ ℤ for
p ≡ 1 (4)) and (q/p) = −1, then x ≡ p/4 is a non-residue mod q, so some prime of x is a non-residue and
−1 ∈ ⟨primes of x⟩. Throughout, G := F_q^× (cyclic of order 2u, u = (q−1)/2 odd), U := (G)² (order u); −1 ∉ U.

**Lemma 2.2 (Kneser covering lemma; PROVED).** Let G be cyclic of order 2u, u odd, U its index-2 subgroup and −1 its
element of order 2. Let g₁, …, g_k ∈ G (repetitions allowed) and B := ∏_j {g_j⁻¹, 1, g_j}. If −1 ∉ B, then the
stabiliser H := {h : hB = B} satisfies
(i) H ≤ U (|H| is odd); (ii) no g_j lies in −H; (iii) n_out := #{j : g_j ∉ H} ≤ [U : H] − 1.
(iii) is sharp: for every d | u, d > 1, the multiset of d − 1 copies of a generator of G has −1 ∉ B and H = {1}
inside the quotient ℤ/2d (in logs, B = [−(d−1), d−1] ∌ d). (R1 repair) To get equality for a prescribed H of index d
in U inside G itself, add enough generators lying in H that their box covers H; the full box is then the inverse image
of the quotient box, with stabiliser exactly H and n_out = d − 1.
*Proof.* 1 ∈ B, so H ⊆ B and −1 ∉ H; |H| divides 2u and is odd, so H ≤ U (a cyclic group has one subgroup of each
order). (ii) If g_j = −h with h ∈ H, then g_j ∈ B (take 1 in the other factors), so −1 = g_j h⁻¹ ∈ g_jH ⊆ B.
(iii) Kneser's theorem for k summands gives |B| ≥ Σ_j |B_jH| − (k − 1)|H| with B_j = {g_j⁻¹, 1, g_j}. If g_j ∈ H then
|B_jH| = |H|. If g_j ∉ H, the cosets g_j⁻¹H, H, g_jH are distinct unless g_j² ∈ H. G/H is cyclic of even order
2[U:H] and its unique involution is the image of −1, so g_j² ∈ H with g_j ∉ H forces g_j ∈ −H, which (ii) excludes.
Hence |B_jH| = 3|H| and |B| ≥ (1 + 2n_out)|H|. B is a union of H-cosets that misses the coset −H, so
|B| ≤ |G| − |H| = (2[U:H] − 1)|H|. Therefore n_out ≤ [U:H] − 1. ∎

**Corollary 2.3 (anatomy of a failing forced window; PROVED).** Let q be a forced window of p, x = (p+q)/4 = ∏ s^{v_s},
and suppose −1 ∉ R(x) (no Type II solution at x). Then there are d | u with d > 1 — so d ≥ ℓ_q, the least prime
factor of u — and the subgroup H_d ≤ U of index d such that
`  1 ≤ Ω_out(x) := Σ_{s ∉ H_d} v_s(x) ≤ d − 1,   and no prime factor of x lies in −H_d.`
Conversely, every x = s·h with h composed of primes in H_d and s ∉ ±H_d prime fails, since R(x) ⊆ H_d ∪ sH_d ∪ s⁻¹H_d.
*Proof.* Apply Lemma 2.2 to the prime factors of x with multiplicity; R(x) is exactly B. The stabiliser has index
d in U. d = 1 would put every prime of x in U, contradicting (x/q) = −1; the same fact gives Ω_out ≥ 1. ∎

Consequences.
* (a) q = 3 (u = 1) never fails (classical).
* (b) q = 7: u = 3 and H = {1}. For p ≡ 1 (8) we have 2 | x with log 2 = ±2 in ℤ/6, and a non-residue prime has odd
  log; ±2 ± 1 hits 3, so the window q = 7 never fails for p ≡ 1 (8) (a Mordell case).
* (c) Forcing removes the dominant index-2 failure mode, in which every prime of x lies in U (for integers this
  Landau-type event has density ≍ (log X)^{−1/2}; for shifted primes we only have the upper bound, and it is what
  dominates *unforced* windows, cf. FORCED_WINDOW §8.6 for q = 3). It also removes the other even-parity failures:
  e.g. p = 353, q = 11, x = 91 = 7·13 has two non-residue primes, x is a residue and R(x) = {1, …, 9} misses −1
  (R1 example). Every forced failure needs all but at most d − 1 prime factors of x in a subgroup of index 2d ≥ 2ℓ_q
  in G (R1 repair: "exactly" withdrawn).
* (d) *Limit of this bound (R1 repair: not a limit on window information).* For H = {1} (d = u) the necessary
  condition of Cor 2.3 includes only Ω_{≢1 (q)}(x) ≤ (q − 3)/2, which holds automatically once q > 2 log₂ x + 3 (the
  "no prime factor in −H" condition remains). So this necessary condition, in its Rankin form (§3), yields nothing once
  q ≳ 2 log log X. That is a limitation of the relaxed upper bound, not a theorem that windows carry no further
  deterministic structure (forced parity, the factor 2, and the −H condition are not exploited by it).

*Checks (CERTIFIED).* `scripts/z51_forcing_kneser.py 15 4` and `… 41 3`: all 629 507 multisets of at most 4
(resp. 3) logs in ℤ/2u for odd u ≤ 15 (resp. ≤ 41); in the 468 185 cases with −1 ∉ B, (i)–(iii) hold. (R1 repair:
the first version's "sharpness" loop only checked the quotient example; the script now builds the lifted example for
every d | u, d > 1, and certifies −1 ∉ B, Stab(B) = H_d exactly and n_out = d − 1, for all odd u ≤ 45.) The R1 referee re-ran
`z51_forcing_kneser.py 9 3` (no violations). `scripts/z51_forcing_windows.c` verifies Cor 2.3 on every failing forced window of 77 724 primes p ≡ 1 (8)
(all p ∈ [10⁶, 2·10⁶] and 20 000-prime samples in [10^k, 1.1·10^k] for k = 8, 10, 12; forced windows q ≡ 3 (4),
q ≤ 400): 936 643 Kneser checks, 0 violations. q = 3 and q = 7 never fail, as proved.

## 3. Per-window failure: a fixed-q upper bound, and G4

### 3.1 Fixed q: the upper-bound exponent 1 − 1/(2ℓ_q)

**Theorem 3.1 (PROVED modulo Henriot's uniform Nair–Tenenbaum bound, New Thm 5 of the 2014 erratum, exactly as used
in FORCED_WINDOW Lemma 8.3; plus Mertens in progressions).** Fix a prime q ≡ 3 (mod 4), q ≥ 7, put u = (q−1)/2 and
let ℓ_q be the least prime factor of u. Then
`  #{p ≤ X : p ≡ 1 (4), −1 ∉ R((p+q)/4) mod q, (q/p) = −1}  ≪_q  (X/log X)·(log X)^{−(1 − 1/(2ℓ_q))}·(log log X)^{ℓ_q − 1}.`
The same bound holds a fortiori for full-window failure (−1 ∉ R(px), Lemma 2.1).
*Proof.* For d | u, d > 1, let H_d ≤ U be the subgroup of index d and ω_d(n) := #{primes s | n : s ∤ 2q, s ∉ H_d}.
By Cor 2.3 a failing forced window has, for some such d, ω_d(x) ≤ Ω_out(x) ≤ d − 1 (excluding 2 only lowers the count).
For 0 < y ≤ 1, 1[ω_d(x) ≤ d − 1] ≤ y^{ω_d(x) − (d−1)}. The function f(n) = y^{ω_d(n)} is multiplicative with
0 ≤ f ≤ 1 and f(ℓ^a) = f(ℓ). FORCED_WINDOW Lemma 8.3 (proved there for f(ℓ^a) = g_χ(ℓ); its proof uses only these two
properties, the factor at 2 is bounded because 4n − q is odd, and dropping the conditions p ≡ 1 (8), q ≡ 3 (8) only
enlarges the left side) gives, after summing dyadic ranges,
`  Σ_{p ≤ X, p ≡ 1 (4)} f((p+q)/4) ≪ (X/log X)·exp(−Σ_{ℓ ≤ X, ℓ ∤ 2q} (1 − f(ℓ))/ℓ).`
(R1: the referee re-checked this transfer against Henriot's definitions and the erratum: F(n₁, n₂) = f(n₁)·1[P⁻(n₂) > √M]
is in M₂(1, 1, ε) uniformly in y, New Thm 5 needs no lower bound on F, and even x is harmless.)
Primes are equidistributed among the q − 1 classes and H_d is a union of u/d of them, so
Σ_{ℓ≤X, ℓ∉H_d} 1/ℓ = (1 − 1/(2d)) log log X + O_q(1). Hence the d-part of the failure count is
≪_q y^{−(d−1)} (X/log X)(log X)^{−(1−y)(1−1/(2d))}. Take y = (d−1)/((1 − 1/(2d)) log log X) to get
≪_q (X/log X)(log X)^{−(1−1/(2d))}(log log X)^{d−1}. Summing over the finitely many d | u, d > 1, the term d = ℓ_q
dominates. ∎

**Proposition 3.2 (the exponent is sharp for integers; PROVED, Wirsing).** For fixed q as above,
#{n ≤ Y : (n/q) = −1, −1 ∉ R(n)} ≫_q Y (log Y)^{−(1 − 1/(2ℓ_q))} log log Y.
*Proof.* With d = ℓ_q and H = H_d, count n = s·h with s ≤ Y^{1/2} a prime in a non-residue class outside −H (such
classes exist because |−H| = u/d < u) and h ≤ Y/s composed of primes in H. Wirsing's theorem gives
#{h ≤ Z} ≍_q Z (log Z)^{1/(2d) − 1}, and summing over s gives the claim. The representation is unique (s is the only
prime factor of n outside H), n is a non-residue, and n fails by Cor 2.3 (converse part). ∎

For shifted primes x = (p+q)/4 the matching lower bound is a lower-bound sieve of dimension 1 − 1/(2ℓ_q) for primes
with all but one prime factor of p + q in H. We do not prove it; the numerics below are consistent with it
(EVIDENCE only, see the caveat on scales).

**Reading (R1 repair: upper bounds only).** Forcing removes the dominant index-2 failure mode. For unforced windows
that mode (all prime factors of x in U) is a Landau-type event of integer density ≍ (log X)^{−1/2}; this is the
"(log X)^{−1/2}" of G4. For a forced window at fixed q, Thm 3.1 bounds the failure *rate* (relative to the ≍ X/log X
primes) by (log X)^{−1 + 1/(2ℓ_q) + o(1)} ≤ (log X)^{−5/6 + o(1)}. This is an upper bound. For integers it is sharp
(Prop 3.2); for shifted primes no matching lower bound is proved, and for some (q, p mod 8) the rate is identically 0
(q = 7 on p ≡ 1 (8), §2(b)). Upper-bound exponents: q = 19, 31, 43, 67, 79, … (3 | u) give 5/6; q = 11, 71, 131 give
9/10; q with u prime (11, 23, 47, 59, 83, 107, …) give 1 − 1/(q−1).

### 3.2 Growing q: what can be proved, and the random-box regime

* **Kneser–Rankin.** The idealised Rankin optimisation in the proof of Thm 3.1 has a minimiser y < 1 only while every
  d | u, d > 1, satisfies d − 1 < (1 − 1/(2d)) log log X; since d = u always divides u, this needs q ≲ 2 log log X.
  (R1 repair) This is a limitation of that relaxed bound. Uniformity in q (Mertens remainders, the sum over d | u, the
  d-dependent constants, the dominance of d = ℓ_q) is *not* proved here even in that range.
* **Fourier L¹ majorant** (FORCED_WINDOW §8, Lemmas 8.1–8.4): failure ⟹ Σ_{χ ≠ 1} G_χ(x) ≥ 1. (R1 repair, the
  referee's improvement.) Lemma 8.2 gives mean g_χ = 2/3 for the unique real χ ≠ 1 and mean ≤ 1/√3 for the q − 3
  non-real χ. Running Lemmas 8.3–8.4 separately on the two groups gives, uniformly for q in any fixed polylogarithmic
  range, a failure rate ≪ L^{−1/3+ε} + q·L^{−a+ε}, with a := 1 − 1/√3 = 0.4226… and L = log X. This is non-trivial for
  q ≤ L^{a−2ε}, not only for q ≤ L^{1/3}.
* **Random box (heuristic; Assessment, R1-corrected).** For q = (log X)^β the box R(x) has at most τ(x²) and
  typically about 3^{ω(x)} elements, about half of them in the coset −U (the parity is free at a forced window). In a
  random-target model, success needs 3^{ω(x)} ≳ q. With the Sathe–Selberg law P(ω ≈ α log log X) = (log X)^{−Q(α)+o(1)},
  Q(α) = 1 − α + α log α, this gives: P(fail) ≈ (log X)^{−Q(β/log 3)} for β < log 3 ≈ 1.10; failure of order 1
  near β ≈ 1.1; P(success) ≈ max_α (log X)^{−Q(α)}·min(1, (log X)^{α log 3 − β}), which equals (log X)^{−Q(β/log 3)}
  for log 3 < β < 3 log 3 ≈ 3.30 and (log X)^{2−β} = (log X)²/q only for β > 3 log 3 (the first moment
  E 3^{ω} ≍ (log X)² is carried by ω ≈ 3 log log X). P(fail) ≪ (log X)^{−1/2} needs β ≲ 0.2051 in this model. All
  of this assumes equidistribution of the box relative to the target −1; none of it is proved.

### 3.3 Numerics (EVIDENCE; `scripts/z51_forcing_windows.c`, `data/z51_forcing/win_1e{6,8,10,12}_perq.txt`)

Forced Type-II failure rate (−1 ∉ R(x)) per window, at four scales (all p ≡ 1 (8) in [10⁶, 2·10⁶]; 20 000-prime samples
near 10⁸, 10¹⁰, 10¹²); "slope" is −Δlog(rate)/Δlog log p between the first and last scale; "asym" is 1 − 1/(2ℓ_q):

| q | q mod 8 | ℓ_q | 10⁶ | 10⁸ | 10¹⁰ | 10¹² | slope | asym | unforced 10⁶ → 10¹² |
|---|---|---|---|---|---|---|---|---|---|
| 11 | 3 | 5 | 0.261 | 0.221 | 0.188 | 0.165 | 0.69 | 0.900 | 0.642 → 0.468 |
| 19 | 3 | 3 | 0.443 | 0.385 | 0.312 | 0.293 | 0.62 | 0.833 | 0.654 → 0.470 |
| 23 | 7 | 11 | 0.144 | 0.116 | 0.106 | 0.092 | 0.67 | 0.955 | 0.483 → 0.341 |
| 31 | 7 | 3 | 0.234 | 0.135 | 0.140 | 0.125 | 0.94 | 0.833 | 0.475 → 0.318 |
| 43 | 3 | 3 | 0.681 | 0.624 | 0.557 | 0.502 | 0.46 | 0.833 | 0.768 → 0.600 |
| 47 | 7 | 23 | 0.308 | 0.250 | 0.219 | 0.197 | 0.67 | 0.978 | 0.611 → 0.450 |
| 71 | 7 | 5 | 0.411 | 0.350 | 0.318 | 0.272 | 0.62 | 0.900 | 0.711 → 0.517 |
| 103 | 7 | 3 | 0.552 | 0.485 | 0.440 | 0.403 | 0.47 | 0.833 | 0.686 → 0.494 |
| 131 | 3 | 5 | 0.843 | 0.791 | 0.738 | 0.697 | 0.28 | 0.900 | 0.956 → 0.832 |
| 199 | 7 | 3 | 0.700 | 0.623 | 0.557 | 0.514 | 0.46 | 0.833 | 0.823 → 0.630 |
| 383 | 7 | 191 | 0.814 | 0.760 | 0.678 | 0.637 | 0.37 | 0.997 | 0.919 → 0.759 |

* q = 3 and q = 7 never fail, as proved. q ≡ 7 (mod 8) windows fail less: x is even, and 2 is a forced extra generator.
* Forced windows always fail less than unforced ones at the same q, by a factor that grows with p.
* The rates decay slowly (local exponents 0.3–0.9 in log p). The asymptotic regime of Thm 3.1, where the
  (log log X)^{ℓ_q−1} factor is negligible, is not visible below 10¹²; mean Ω(x) is only 3.6 (q ≡ 3 (8)) or 5.6
  (q ≡ 7 (8)) at 10¹². Numerics cannot confirm an exponent here; they confirm the ordering forced < unforced and the
  slow decay.

### 3.4 Verdict on the parent estimate in G4 (R1-revised)

G4: "per-window failure probability is ≪ (log X)^{−1/2} only for q ≤ (log X)^ε, which with G2 gives exp(−(log X)^ε)".
* *Refinement at fixed q (PROVED upper bound).* At fixed q the forced failure rate is ≤ (log X)^{−1+1/(2ℓ_q)+o(1)}
  (Thm 3.1), much smaller than (log X)^{−1/2}. The (log X)^{−1/2} rate is the integer density of the Landau mode,
  which only unforced windows suffer. Fixed q lies inside "q ≤ (log X)^ε" for every ε, so this does not contradict the
  parent's restriction; it sharpens the rate inside it. No matching shifted-prime lower bound is proved.
* *Growing q (heuristic only).* In the random-box model the threshold for a failure rate ≪ (log X)^{−1/2} is
  q ≤ (log X)^{0.205}; provable per-window bounds reach q ≤ (log X)^{0.4226−ε} (Fourier, real/non-real split). The
  consequence for the joint route is quantified, for specified envelopes only, in §4.2.

## 4. Many windows: what joint bounds can and cannot give (gate G2)

### 4.1 Fixed number of windows

**Proposition 4.1 (PROVED modulo Henriot New Thm 5 with k + 1 linear forms; constants depend on k and on all q_i).**
Fix distinct primes q₁, …, q_k ≡ 3 (mod 4), all ≥ 7. Then
`  #{p ≤ X : p ≡ 1 (4), and for every i: (q_i/p) = −1 and −1 ∉ R((p+q_i)/4) mod q_i}`
`      ≪ (X/log X) ∏_i (log X)^{−(1 − 1/(2ℓ_{q_i}))} (log log X)^{ℓ_{q_i} − 1}.`
*Proof.* Write p = 4m + 1 and use the forms Q₀(m) = 4m + 1 (weight 1[P⁻(Q₀) > √M], as in FORCED_WINDOW Lemma 8.3) and
Q_i(m) = m + (1 + q_i)/4 = (p + q_i)/4; they are primitive and pairwise non-proportional. For each choice (d₁, …, d_k)
of indices from Cor 2.3, the product of the Rankin weights y_i^{ω_{d_i}(Q_i(m))} with the roughness indicator of Q₀
is in Henriot's class M_{k+1}(1, 1, ε), uniformly in the y_i. At a good prime s ≤ √M (s ∤ 2∏q_i ∏(q_i − q_j)) the
root-avoidance factor times the auxiliary Euler factor is
(1 − (k+1)/s)(1 + Σ_i f_i(s)/s) = 1 − [1 + Σ_i (1 − f_i(s))]/s + O_k(s^{−2}) (R1 repair: the "1" is primality and gives
the factor 1/log X). Primes above √M change the product by a bounded factor; the finitely many bad primes cost
O_{k,q}(1); primes ≤ k + 1 are omitted from Henriot's avoidance product. Optimise each y_i as in Thm 3.1 and sum over
the finitely many (d_i). ∎

For fixed k this is a product of the single-window rates. Uniformity in k and in the q_i is not controlled. Note also
(R1) that Prop 4.1 counts p for which *every chosen* window is forced and fails; the event relevant to Linnik, "every
forced window q ≤ R fails", lets the chosen windows be unforced, so a joint estimate must also sum over character
profiles.

### 4.2 Growing number of windows: what multiplying the known envelopes gives (Assessment; R1-revised)

**Calculation 4.2 (exact arithmetic for two specified scalar envelopes; not a barrier theorem).** Suppose, beyond
what is known, a joint bound uniform in k *and* in the q_i that multiplies per-window envelopes with only a C^k loss,
including a joint factorisation for the Fourier weights (a separate hypothetical statement). Then:
(a) Kneser–Rankin envelopes are usable only for q ≲ 2 log log X, i.e. for ≍ log log X/log₃X windows, each saving at
most (log X)^{1}: the total saving is at most exp(C (log log X)²/log₃X).
(b) With the Fourier envelopes b_q = min(1, C(L^{−1/3+ε} + q L^{−a+ε})), a = 1 − 1/√3: for q ≤ T := c L^{a−ε} each
b_q is bounded away from 1, and ∏_{q≤T} b_q ≥ exp(−Σ_{q≤T} log(T/q) − O(T/log T)) = exp(−O(T/log T)). So multiplying
these envelopes saves at most exp(−c′ L^{a−ε}/log L), a = 0.4226….
(R1 repair: the earlier "structural 1/3 cap" is withdrawn. The referee showed that the same Fourier majorant with the
real and non-real characters separated already gives a = 0.4226 > 1/3, so the exponent belongs to the chosen envelope,
not to the majorant family. Better envelopes may exist.) Both numbers are far below Vaughan's 2/3 and the internal 3/4,
so these envelopes cannot contribute to a power saving or to the existing exceptional-set bounds; nothing here excludes
other uses of windows.

**Why single-window majorants cannot carry the large windows (heuristic; Assessment).** In the random-target model a
window q ≥ (log X)^{1.1+ε} succeeds with probability → 0 (typical box ≈ 3^{ω(x)} = (log X)^{1.1+o(1)}; the success
probability is ≈ E min(1, 3^{ω}/q), see §3.2), so a majorant of its failure indicator has mean close to 1. Such windows
can only help *collectively*: about (log X)^{A}/log log X weak divisor events with total mean of order (log X)^{1.1}·
log(A/1.1) in that model. The model's joint failure exp(−(log X)^{1.1−o(1)}) is super-polynomially small, so it
predicts no exceptional primes at all; it is a heuristic, not a derived law. A proof would be a lower-tail statement
for many low-probability divisor events across the shifts p + q. This is *analogous* to the RLD problem of z50 C1
(door (vii)); it is not a proved reduction to RLD-U (event family, probability space, forcing and uniformity differ).

### 4.3 Numerics: in the samples, joint failure is below the independence model (EVIDENCE)

`scripts/z51_forcing_joint.py`, `scripts/z51_forcing_lowertail.py`, `data/z51_forcing/joint_summary.txt`,
`lowertail.txt`. "All forced windows q ≤ R fail" (vacuous if there is none), observed fraction against the model
mean_p ∏_{forced q ≤ R} f_q, with f_q the empirical per-q rate:

| p ≈ | R = 50 obs / model | R = 128 obs / model | R = 200 obs / model | R = 400 obs / model |
|---|---|---|---|---|
| 10⁶ | 1.53e-2 / 2.01e-2 | 2.39e-3 / 3.72e-3 | 2.85e-4 / 1.32e-3 | 1.1e-4 (2 primes) / 3.8e-4 |
| 10⁸ | 1.38e-2 / 1.70e-2 | 1.74e-3 / 2.36e-3 | 3.97e-4 / 6.48e-4 | 5.0e-5 (1) / 1.1e-4 |
| 10¹⁰ | 1.11e-2 / 1.51e-2 | 8.5e-4 / 1.63e-3 | 2.5e-4 / 3.4e-4 | 0 / 4.1e-5 |
| 10¹² | 1.08e-2 / 1.27e-2 | 8.5e-4 / 1.20e-3 | 0 / 2.0e-4 | 0 / 1.7e-5 |

With full windows (−1 ∉ R(px)) there are no all-fail primes at R = 400 at any scale. The number of successful
forced windows q ≤ 400 has mean 6.46 at 10⁶ and 9.18 at 10¹². Its variance is below the Poisson-binomial model
(4.00 vs 4.68; 5.71 vs 6.50), and its lower tail is thinner (P(≤ 2) = 9.0e-4 vs 1.8e-3 at 10¹²). In these samples the
independence model over-predicts the lower tail; this is not a proof of negative correlation or of stochastic domination
(R1 repair), and the R = 400 tail counts rest on 0–2 primes. Hard primes (controls), forced windows q ≤ 400, number
forced / Type-II successes / full successes: 193: 18/0/0; 409: 22/3/4; 577: 18/2/3; 2521: 23/1/1; 3361: 20/0/1;
5569: 19/4/6; 9601: 24/3/6; 66529: 19/1/4; 8813281: 21/6/7. So at p = 193 *every* forced window up to 400 fails even in
full form (ES(193) uses other x), and at 3361 every forced window fails at Type II level. The hard primes are exactly
where forced windows are thin; the windows give no pointwise guarantee even at tiny p.

## 5. Robust Linnik: bias suffices, down to the scale (log p)^{1+δ} and even C·log p

G3 and Observation 1.1 ask for confinement at *every* q ≤ (log p)^{2+δ}. A dual large sieve needs only a *bias* of
the quadratic character on a set of small primes, and (R2, Astra's observation) the quadratic large sieve of
Heath-Brown, or the Montgomery–Vaughan moment large sieve, lower the scale. Throughout, p runs over odd primes and
χ_p(n) = (n/p) for odd n; S(y) := {odd primes q ≤ y}, m := |S(y)|.

**Proposition 5.1 (biased characters are rare, classical large sieve; PROVED).** Let X ≥ 3, y ≥ 17, 0 < η ≤ 1/2,
r := ⌊2 log X/log y⌋ ≥ 1. Then
`  #{p ≤ X : Σ_{q∈S(y), q≠p} (q/p) ≥ 2ηm}  ≤  y + 2y·(log X/(2η²))^r.`
For y = (log X)^A, A > 0 fixed, this is X^{2/A+o(1)} for fixed η (and X^{2(1+2θ)/A+o(1)} for η = (log X)^{−θ}).
*Proof.* p ≤ y contribute ≤ y. For p > y let a_n := #{(q₁, …, q_r) ∈ S^r : q₁⋯q_r = n}; then
Σ_n a_n χ_p(n) = (Σ_{q∈S} χ_p(q))^r ≥ (2ηm)^r on the bad set, and Σ_n a_n² ≤ r!·m^r (a tuple has at most r!
rearrangements). All n ≤ y^r ≤ X². Keeping only the Legendre characters of primes in the multiplicative large sieve,
Σ_{p≤X} |Σ_n a_n χ_p(n)|² ≤ 2X²·Σ a_n². With m ≥ y/log y and y^{r+1} > X², m^r ≥ X² y^{−1}(log y)^{−r}, so the bad
p > y number ≤ 2X² r!/((2η)^{2r} m^r) ≤ 2y (r log y/(4η²))^r ≤ 2y (log X/(2η²))^r; finally (log X)^r ≤ X^{2/A}. ∎
(R2: verified line by line; standard moment method.)

**Proposition 5.1′ (Heath-Brown's quadratic large sieve; PROVED modulo Heath-Brown, Acta Arith. 72 (1995), Thm 1 /
Cor 2).** Same notation, with r := ⌊log X/log y⌋ ≥ 1. For every ε > 0,
`  #{p ≤ X : Σ_{q∈S(y), q≠p} (q/p) ≥ 2ηm}  ≪_ε  y + X^{2ε}·y·(log X/(2η²))^r,`
which is X^{1/A+o(1)} for y = (log X)^A with any fixed A > 0 and fixed η.
*Proof (R2's argument).* Heath-Brown's inequality for real primitive characters with arbitrary coefficients reads
Σ_{m≤M}^{*} |Σ_{n≤N} a_n (n/m)|² ≪_ε (MN)^ε (M + N) Σ_{n₁n₂ = □} |a_{n₁}a_{n₂}| (m odd squarefree). Take the same
ordered-tuple coefficients with N = y^r ≤ X. An ordered 2r-tuple of primes with square product admits a perfect
matching of equal primes, so Σ_{n₁n₂=□} a_{n₁}a_{n₂} ≤ (2r − 1)!!·m^r ≤ (2r)^r m^r. On the bad set the signal is
≥ (2ηm)^r, so the bad p > y number ≪_ε X^{2ε}·2X·(2r)^r m^r/(2ηm)^{2r}; with m^r ≥ X y^{−1}(log y)^{−r} this is
≪ X^{2ε} y (2r log y/(4η²))^r ≤ X^{2ε} y (log X/(2η²))^r = X^{1/A+2ε+o(1)}. ∎
For the least non-residue itself this is Baier's improvement of Linnik's A > 2 to A > 1 (as quoted by Lau–Wu, IJNT 4
(2008), [2]; recalled).

**Proposition 5.2 (scale C log X; PROVED modulo the Montgomery–Vaughan moment large sieve for real characters, in the
form of Lau–Wu 2008, Lemma 1; R3-quantified).** Lau–Wu Lemma 1 (checked against the HAL manuscript by R3):
Σ_{d ∈ D(Q)} |Σ_{P<ℓ≤2P} χ_d(ℓ)/ℓ|^{2j} ≪ Q(6j/(P log P))^j + (6P/(log P)²)^j, uniformly for 2 ≤ P ≤ Q and integers
j ≥ 1, absolute constant, over fundamental discriminants of either sign with |d| ≤ Q. For every odd prime p,
d = p* := (−1)^{(p−1)/2} p ∈ D(Q) represents the Legendre character: χ_{p*}(ℓ) = (ℓ/p) for odd ℓ. Restricting ℓ to a
fixed subset 𝒮 of the primes is legitimate by rerunning the coefficient argument (the restricted tuple counts satisfy
0 ≤ a′_j ≤ a_j, the square-correlation part is bounded by the unrestricted a_{2j}(n²), the other part by
(Σ_{P<ℓ≤2P} ℓ^{−1/2})^{2j}); it is *not* a pointwise comparison of character sums. Let 𝒮 have relative density δ
(π_𝒮(t) ~ δπ(t)), so σ_𝒮 := Σ_{ℓ∈𝒮, P<ℓ≤2P} 1/ℓ = (δ log 2 + o(1))/log P, and put a := δ log 2, κ := a²/(12e). Then
for fixed η ∈ (0, 1], fixed C > 0, P = C log X and X large,
`  #{p ≤ X : Σ_{ℓ∈𝒮, P<ℓ≤2P} (ℓ/p)/ℓ ≥ η σ_𝒮}  ≪  X exp(−κη²C log X/log log X) + X^{κη²C(1+o(1))}.`
κ = (log 2)²/(12e) ≈ 0.0147 for all primes, κ = (log 2)²/(48e) ≈ 0.0037 for 𝒮 = {q ≡ 3 (mod 4)}; for C ≤ 1 the second
term is ≤ X^{0.015} and is absorbed.
*Proof.* Divide the moment bound by (ησ_𝒮)^{2j}: count ≪ X[6j log P/(η²a²P)·(1 + o(1))]^j + [6P/(η²a²)·(1 + o(1))]^j.
With j = ⌊κη²P/log P⌋ the first base tends to 1/(2e) < e^{−1}, giving X e^{−j}; the second is exp(j(log P + O(1))) =
X^{κη²C(1+o(1))}. ∎ (R3: the earlier endpoint constant c₀ = (log 2)²/(6e) is replaced by κ with slack.)

**Theorem 5.3 (robust reduction; PROVED from Props 5.1′ and 5.2; R2/R3-repaired).** Let 𝔈 be any set of odd primes.
(a) For fixed A > 1 and 0 < η < 1/2:
`  #(𝔈 ∩ [1, X]) ≤ X^{1/A+o(1)} + #{p ∈ 𝔈 ∩ [1, X] : #{q ∈ S((log X)^A) : (q/p) = −1} > (½ − η)·m}.`
(b) For fixed C ∈ (0, 1] and η ∈ (0, 1]:
`  #(𝔈 ∩ [1, X]) ≪ X exp(−κη²C log X/log log X) + #{p ∈ 𝔈 ∩ [1, X] : Σ_{P<q≤2P} (q/p)/q < η Σ_{P<q≤2P} 1/q},  P = C log X.`
The remainders are the primes of 𝔈 that are *not QR-biased* (a one-sided condition; two-sided balance follows by the
same argument with |Σ|). *Forced windows (R2/R3 repair).* Remove in addition the X^{1/A+o(1)} (resp.
X exp(−c log X/log log X)) primes that are QR-biased with a fixed threshold, say ½, on the subset {q ≡ 3 (mod 4)} of the
range. Every remaining p ≡ 1 (mod 4) has ≫ (log X)^A/log log X (resp. ≫ log X/log log X) **forced windows**
q ≡ 3 (mod 4) in the range, all of which fail if ES(p) fails.

**Corollary 5.4 (PROVED reduction; CONDITIONAL consequences of new, unproved sufficient hypotheses — not a counted
conditional target under the CONTEXT hypothesis-quality rule, R3).** η is fixed throughout.
(a) MF(A, η): every large p with ES(p) failing has #{q ≤ (log p)^A : (q/p) = −1} ≤ (½ − η)π((log p)^A). If MF(A, η)
holds for some A > 1, η > 0, then #{p ≤ X : ES(p) fails} ≤ X^{1/A+o(1)}.
(b) MF₁(C, η): every large p with ES(p) failing has Σ_{P<q≤2P} (q/p)/q ≥ η Σ_{P<q≤2P} 1/q, P = C log p. If MF₁(C, η)
holds for some C ∈ (0, 1], η > 0, then #{p ≤ X : ES(p) fails} ≪ X exp(−c log X/log log X) — beyond the CRT caps
(3/4 for ES), i.e. the shape of z50 Target 3 with θ → 1, conditionally.
(c) MF follows from the majority-reach hypothesis MR(A, η): Reach(p, q) (Def 6.1) at ≥ (½ + η)·π((log p)^A) odd primes
q ≤ (log p)^A, for every large p ≡ 1 (8); MF₁ follows from MR₁(C, η): the q ∈ (C log p, 2C log p] with Reach(p, q)
carry ≥ (1 + η)/2 of Σ 1/q there.
*Proof.* (a), (b): on each dyadic range (Z, 2Z] the scale (log p)^A (resp. C log p) equals (log Z)^A(1 + o(1)) (resp.
the endpoints C log p, 2C log p move by O(C), affecting O_C(1) primes of reciprocal weight O_C(1/log Z) against a
total ≍ 1/log log Z); deleting the primes between the two scales changes the bias by o(1), so the hypothesis gives
bias ≥ η/2 at the fixed scale of the range; apply Theorem 5.3 with X = 2Z and sum over ranges (R2 repair: genuine
dyadic ranges). (c) Reach at q and (q/p) = −1 give ES(p) (Lemma 6.2), so an exceptional p is a residue at every q
where reach holds. ∎

**Status of the hypotheses (Assessment; R2/R3-corrected).**
* *GRH.* For fixed A > 2, GRH (Lagarias–Odlyzko effective Chebotarev for ℚ(√p)) gives #{q ≤ (log p)^A : (q/p) = −1}
  = (½ + o(1))π((log p)^A) uniformly, so under GRH MF(A, η) is *equivalent* to eventual ES (R2; the round-1 claim
  that this needed A > 4 is withdrawn). For A ≤ 2, and for MF₁, GRH gives no such control (its error term
  √y log p exceeds y = (log p)^A), so no GRH-equivalence with ES is known for MF(A) with 1 < A ≤ 2 or for MF₁ (this
  is absence of a known equivalence, not a proof of independence).
* *Necessity.* MF and MF₁ are *sufficient*, not necessary: a power-small infinite set of unbiased exceptional primes
  would be compatible with the conclusion. "MF for all but a small set" is itself a sufficient exceptional-set
  statement; whether it is as hard as the conclusion is an Assessment, not a theorem.
* *Testability (R3).* MF and MF₁ are implications with antecedent "ES(p) fails"; every tested prime satisfies ES, so
  numerical tests of MF/MF₁ are vacuous. Neither MF₁ nor MR₁ is shown to be visibly weaker than the target
  exceptional-set bound; they are new research conjectures that isolate a useful scale, not accepted hypotheses.
* *Reach versions.* MR is a stronger, counterfactual requirement; it is *false* for A > 3 (Cor 6.4). At the small
  scales it is numerically robust (R3 reproduced these numbers independently from the raw files): on all 36 sampled
  primes (10⁵–10¹⁰, §6.3) the weighted reach fraction at C = ½ is 1, so MR₁(½, η) holds on the sample for every
  η ≤ 1; at C = 1 the fraction is ≥ 0.62 at every sampled p ≥ 10⁶, so MR₁(1, 0.2) holds there; six of the eight
  primes near 10⁵ fail the 0.6 test of the recorded (truncated, lower-bound) search, which is not a proof that full
  reach fails. `scripts/z51_forcing_mr1.py`, `data/z51_forcing/mr1_summary.txt`. In the coupon model of §6.3 the
  probability that Reach(p, q) fails for some q ≤ 2C log p is ≈ exp(−c(log p)²), summable over p, so the model
  predicts MR₁(C, η) for all large p at every fixed C (a model prediction, not a verified tail law). Proving it pointwise is still B2: for each non-residue class r mod q one
  needs an e ≡ −r (mod q) with p + e (or ep + 1) carrying a suitable divisor pair.

**Corollary 5.5 (T2-lite: lower cap thresholds; PROVED modulo Heath-Brown 1995, resp. Lau–Wu Lemma 1).** Let e*(p)
be the minimal exponent cap of EXPONENT_CAP/CAP_POINTWISE (e*(p) = 0 iff ES(p)).
(a) For every fixed A > 1: #{p ≤ X : e*(p) > (log X)^A/4} ≪ X^{1/A+o(1)}.
(b) For every fixed C ∈ (0, 1]: #{p ≤ X : e*(p) > (C/2) log X} ≪ X exp(−c log X/log log X), c = c(C) > 0.
*Proof.* CAP_BOUNDED Lemma 3.1: e*(p) = 0 for p ≢ 1 (8), and e*(p) ≤ (q₃(p) − 3)/4 for p ≡ 1 (8), where q₃(p) is the
least prime q ≡ 3 (mod 4) with (q/p) = −1. (a) e*(p) > (log X)^A/4 forces (q/p) = +1 for every q ≡ 3 (4) up to
y = (log X)^A. Apply Heath-Brown's inequality to 𝒜 = squarefree products of r = ⌊log X/log y⌋ distinct such q
(odd squarefree, all ≤ X, character value 1 at every such p): the count is ≪_ε X^{1+2ε}/|𝒜| and
|𝒜| ≥ X^{1−1/A−o(1)} (as in CAP_BOUNDED Thm 3.2). (b) e*(p) > (C/2) log X forces (q/p) = +1 for all q ≡ 3 (4) in
(P, 2P], P = C log X: full bias η = 1 on 𝒮 = {q ≡ 3 (4)}; apply Prop 5.2 with κ = (log 2)²/(48e) (the second term is
≤ X^{0.004}). ∎ (R3: SOUND.)
*Value (R3-qualified).* (a) lowers CAP_BOUNDED Thm 3.2(a) (A > 2, exponent 2/A) to A > 1 with exponent 1/A; the
qualitative A > 1 power saving for caps was already sketched by another route in CAP_INTERPOLATION Remark 3.2(b), so
(a) is a complete proof with an explicit exponent. (b) improves the cap exceptional-set bound at caps of order log p,
with a near-power saving (not a power saving); it does not settle the architecture-specific ceiling question of
CAP_INTERPOLATION Remark 3.2(c). Both are direct transfers of established least-non-residue technology — Heath-Brown's
quadratic large sieve as used by Baier for n₂ (A > 1), and the Montgomery–Vaughan moments behind Lau–Wu Theorem 2,
which already proves the near-power shape for n_χ with P ≥ C₀ log Q — to the forced-window cap mechanism; no
ES-specific input beyond CAP_BOUNDED Lemma 3.1. This is the brief's T2-lite
target ("lowering its cap threshold … toward A > 1 or below"); it is a statement about the relaxation ES^{(y,e)},
not about ES.

## 6. Forcing reach for two Elsholtz–Tao subfamilies (work item 2)

### 6.1 Definition and the forcing implication

Elsholtz–Tao classes used (identities checked, `scripts/z51_forcing_reach_verify.py`):
* Type II (a, b, e), e | a + b: every n ≡ −e (mod 4ab) has 4/n = 1/(abd) + 1/(acdn) + 1/(bcdn), c = (a+b)/e,
  d = (n+e)/(4ab).
* Type I (b, c, e), e | b + c: every n ≡ −e⁻¹ (mod 4bc) has 4/n = 1/(nbck) + 1/(gb) + 1/(gc), k = (en+1)/(4bc),
  g = k(b+c)/e.
These are two cubic subfamilies of the ES certificates (the U and U⁻¹ box types of POINTWISE_MORDELL17 Lemma 1.1;
the P, Q, Q⁻¹ types and the general Type I family e | k(b+c) are *not* included — R2).

**Definition 6.1 (counterfactual reach, level 1, height n).** Let n ≡ 1 (mod 4) and q an odd prime, q ∤ n. A unit
residue r mod q is *reached at (n, q)* if some Type II class (a, b, e) with a = q·a₁, q ∤ a₁be, or some Type I class
(b, c, e) with b = q·b₁, q ∤ b₁ce, has class modulus 4q·a₁b (resp. 4q·b₁c) ≤ n, contains n modulo 4a₁b (resp. 4b₁c),
and has residue r at q (r ≡ −e, resp. −e⁻¹). *Reach(n, q)* holds if every quadratic non-residue r mod q is reached.
The modulus bound (the height) makes the notion finite: it forces e ≤ qu + v ≤ quv + 1 ≤ n/4 + 1. (R2 repair:) the
runs below use E₂ = n/4 for Type II (missing only e ∈ (n/4, n/4 + 1]; e.g. p = 89, q = 11, e = 23 > 89/4) and
E₁ = n/12 for Type I, which is a genuine truncation (e.g. p = 100049, q = 23, b₁ = 499, c = 2, e = 11479 > p/12; the
earlier claim that the tail needs b₁ = 1 or c = 1 is false). R2's independent complete search at p = 100049 found 21
valid tuples beyond these cutoffs (q ≤ 60) and no additional reached non-residue cell. All runs therefore give lower
bounds for reach; "exact" below means "with these cutoffs".

**Lemma 6.2 (reach forces; PROVED, trivial).** If Reach(p, q) and (q/p) = −1 then ES(p).
*Proof.* p ≡ 1 (4), so (p/q) = (q/p) = −1 and r := p mod q is a reached non-residue: the class contains p itself. ∎

Reach is not implied by ES (it concerns counterfactual points), it is sufficient and not necessary for ES on a line
(a certificate only has to hit p's actual cell; see p = 1 240 009 in §7), and it formalises *one* kind of
congruence-certified forcing: this class menu, this height, level 1. (R2 repair: the earlier claim that every
congruence-certified forcing statement is a reach statement is withdrawn.) Classes with q ∤ modulus certify p
directly and are irrelevant once p is assumed exceptional.

*Definition 6.1\* (all levels).* Reach\*(n, q): every q-adic unit u with (u/q) = −1 lies in some class of Def 6.1's
shape with a = q^k a₁, q ∤ a₁be (resp. b = q^k b₁), any k ≥ 1, modulus 4q^k a₁b ≤ n, containing n modulo 4a₁b; such a
class covers the box u ≡ r (mod q^k), of additive Haar mass q^{−k}. Reach ⟹ Reach\*, and Lemma 6.2 holds for Reach\*.
The numerics use level 1 only.

### 6.2 Upper bounds for reach (PROVED)

**Proposition 6.3 (integers; PROVED modulo Shiu's theorem).** Uniformly for primes 3 ≤ q ≤ (log X)^C,
`  Σ_{n ≤ X, n ≡ 1 (4)} #{r mod q : r reached at (n, q)}  ≪_C  X (log X)³.`
*Proof (with R2's bookkeeping).* Each reached residue comes from a tuple (type, u = a₁, v = b, e) with uv ≤ X/(4q),
e | qu + v, and n in one class modulo 4uv (for Type I, no class or one class). So the sum is ≤ 2Σ_{uv≤X/(4q)}
τ(qu + v)(X/(4uv) + 1). Put t = qu + v ≤ X. From 1/(u(t − qu)) = (1/t)(1/u + q/(t − qu)),
Σ_{u<t/q} 1/(u(t−qu)) ≤ (1/t)(2 + 2 log t + q/r₀(t)), r₀(t) ∈ [1, q] the least positive value of t − qu. Hence
H_q := Σ τ(qu+v)/(uv) ≤ Σ_{t≤X} τ(t)(2 + 2 log t)/t + Σ_{r=1}^{q} (q/r) A_r, A_r := Σ_{q<t≤X, t≡r (q)} τ(t)/t. The first
sum is ≪ L³ (L = log X). For r ≢ 0 and t > q², Shiu's theorem on dyadic blocks (T, 2T] (modulus q ≤ T^{1/2}, constants
uniform) gives Σ_{T<t≤2T, t≡r} τ(t) ≪ (T/q) log 2T, hence ≪ L²/q for that part of A_r; the range q < t ≤ q²
contributes ≪_ε q^{ε−1} log q; and A_0 ≤ (2/q)Σ_{v≤X/q} τ(v)/v ≪ L²/q. So H_q ≪ L³ + L² log q + q^{ε}(log q)², and with
ε = min(½, 1/C) (so q^ε ≤ L) H_q ≪_C L³. The "+1" terms are ≤ (X/(4q))·H_q. ∎

**Proposition 6.3′ (primes; PROVED modulo Shiu's theorem and Brun–Titchmarsh π(x; k, a) ≤ 2x/(φ(k) log(x/k));
proof completed with R3's all-level argument).** Uniformly for primes 3 ≤ q ≤ L^C (L = log X), with μ_q the Haar mass
of the covered non-residue units (Def 6.1\*),
`  Σ_{p ≤ X} #{r mod q : r reached at (p, q)} ≪_C π(X) L³ (log L)²,    Σ_{p ≤ X} μ_q(covered) ≪_C π(X) L³ (log L)²/q.`
*Proof.* *Tuples and Brun–Titchmarsh.* Write u = a₁ (or b₁), v = b (or c), Q = q^k the q-power at level k. A prime p
counted by a Type II tuple satisfies 4Quv ≤ p and p ≡ −e (mod 4uv); if d = gcd(e, 4uv) > 1 then d | p with
d ≤ 4uv < p, impossible, so such tuples contribute nothing (this uses the height before it is dropped). For Type I,
ep ≡ −1 (mod 4uv) forces gcd(e, 4uv) = 1. The surviving tuples are bounded by τ(Qu + v) per pair (u, v), and each
contributes ≤ π(X; 4uv, c) ≤ 2X/(φ(4uv) log(X/(4uv))).
*Level one (Q = q).* Fix θ = 1/12. Split uv dyadically, uv ∈ (T, 2T], use 1/φ(4uv) ≪ (log L)/T, and bound
V(T) := Σ_{uv∈(T,2T], q∤v} τ(qu + v) for T ≥ X^{3θ}: (i) for u ≤ TX^{−θ} the v-interval has length T/u ≥ X^θ and its
endpoint is a fixed power of X, so Shiu (modulus 1) gives ≪ (T/u)L, summing to ≪ TL²; (ii) for u > TX^{−θ}, v < 2X^θ;
for fixed v enlarge u to the full interval (T/v, 2T/v] (the cutoff could leave a short interval), so t = qu + v runs
over a progression with coprime residue v mod q, of length qT/v comparable to its endpoint, and Shiu gives
≪ (T/v)L, summing to ≪ TL². So the block contributes ≪ X L²(log L)/log(X/(8T)); the denominators are ≥ log(q/2) ≥
log(3/2) and spaced by log 2, so the dyadic sum is ≪ X L² (log L)². Products uv < X^{3θ}: apply Prop 6.3's harmonic
argument with t ≤ 2qX^{3θ} + 1 (height Y = 8qX^{3θ}); the BT denominator is ≫ L there, giving ≪_C X L²(log L).
*All levels.* For Q = q^k the harmonic argument gives, for fixed δ ∈ (0, 1), H_Q := Σ_{uv≤X/(4Q), q∤uv} τ(Qu+v)/(uv)
≪_δ L³ + Q^δ L² uniformly for Q ≤ X/4 (t = Qu + v is prime to Q; Shiu dyadically mod Q above Q², Q/φ(Q) ≤ 3/2;
τ(t) ≪ t^{δ/2} below Q²). If Q > X^θ, every admissible pair has log(X/(4uv)) ≥ log Q > θL, and BT gives incidence
count ≪ X[L²(log L) + Q^δ L(log L)]. If Q ≤ X^θ, repeat the level-one dyadic proof: in case (ii) the progression has
length QT/v ≥ (Q/2)X^{2θ} > Q², within Shiu's range, so V_Q(T) ≪ TL². Hence per level
F_Q(X) ≪_δ π(X)[L³(log L)² + Q^δ L² log L]. Each level-Q box has Haar mass Q^{−1}; summing masses (subadditively,
overlaps allowed) over k gives Σ_p μ_q ≪_δ π(X)[L³(log L)²/q + L²(log L)·q^{−1+δ}], and with δ = min(½, 1/C)
(q^δ ≤ L) the second term is absorbed. ∎ (R3: the earlier "same argument with q^k" did not check Shiu's range at
large levels and dropped a log L; both repaired here.)

**Corollary 6.4 (PROVED from Prop 6.3′).** Uniformly for 3 ≤ q ≤ L^C:
(a) #{p ≤ X : Reach\*(p, q)} ≪ π(X) L³ (log L)²/q. So for any prescribed q = q(X) in this range with
q ≥ L³(log L)³, reach at q fails for almost all p ≤ X.
(b) For A ∈ (3, C] and η > 0 fixed, #{p ≤ X : Reach\*(p, q) for at least η·π(L^A) primes q ≤ L^A} ≪
π(X) L^{3−A+o(1)}/η. So MR(A, η) is false for A > 3 (for almost all p, in any fixed progression), for these two
subfamilies at height ≤ p.
*Proof.* (a) Reach\* needs μ_q(covered) ≥ (q − 1)/(2q) ≥ 1/3; Markov. (b) Sum (a) over q ≤ L^A (Σ 1/q ≪ log L),
Markov at η·π(L^A); the p-dependent scale (log p)^A is handled dyadically as in Cor 5.4. ∎
These are *average* statements: they do not say that no prime has a reached q above (log p)³, nor that the reached
q form an initial segment (R3).

*What this does and does not say (Assessment; R2/R3-repaired).* For a prescribed q ≤ L^C the counterfactual reach of
these families is available only on a ≪ L³(log L)²/q fraction of primes, so on average a prime has reach at
≪ L^{3+o(1)} moduli q ≤ L^C, and MR(A) is false for A > 3. This is a statement about these two subfamilies at height ≤ p and level structure; it
says nothing about the selected population of exceptional primes, about other ES families, or about the best large
sieve. In particular it is **not** a barrier for Linnik-type arguments: with Heath-Brown's sieve (Prop 5.1′) the reach
needed is only at scale (log p)^{1+δ}, and with Prop 5.2 at scale C log p, far below (log p)³. (The round-1/round-2
draft's "X^{1/2} cap for Linnik fed by congruence-certified forcing" is **withdrawn** — R2 rated it FATAL as an
unrestricted claim: it froze the classical large-sieve constant and transferred a positive-density hypothesis to the
exceptional set.)

### 6.3 Numerics (EVIDENCE; `scripts/z51_forcing_reach.c`, `…_reach_batch.sh`, `…_reach_summary.py`)

36 primes p ≡ 1 (mod 8): eight each near 10⁵, 10⁶, 10⁷ and four near 10⁸ (cutoffs E₂ = p/4, E₁ = p/12, Def 6.1), four
near 10⁹ (e ≤ 2·10⁷) and four near 10¹⁰ (e ≤ 10⁷); all odd primes q ≤ 1000; level-1 reach of the two subfamilies of
Def 6.1 only (lower bounds). Truncation calibration at p = 10⁸: e ≤ 10³, 10⁴, 10⁵, 10⁶, 10⁷ capture 42 %, 72 %, 89 %,
97 %, 99.97 % of the supply with the standard cutoffs. If the loss scales with the absolute cutoff, the 10⁹/10¹⁰ runs
miss < 1 %; if it scales with e/p, they miss up to ≈ 3 % (10⁹) and ≈ 11 % (10¹⁰) (R2: not a certified error
estimate; a small supply loss can move a first hole). 2 682 randomly sampled witnesses (1 274 Type I, 1 408 Type II)
were rebuilt into explicit 4/n identities and checked with exact rationals: 0 failures (independently re-checked by
R2). Per-prime table: `data/z51_forcing/reach_summary.txt`; raw per-q data: `data/z51_forcing/reach/`.

Statistics: q* = least q with an unreached non-residue class; S_e = supply, the mean over q ∈ [11, 300] of q times
the mean number of distinct productive (type, e) per non-residue class (each (type, e) feeds exactly one class mod q);
R_maj = largest prime R ≤ 1000 such that reach holds at ≥ 60 % of the odd primes q ≤ R.

| p ≈ | log p | median q* | median S_e | S_e/(log p)³ | median R_maj | q*/(log p)² | q*/((log p)³/log log p) |
|---|---|---|---|---|---|---|---|
| 10⁵ | 11.6 | 17 | 49 | 0.032 | 34 | 0.13 | 0.027 |
| 10⁶ | 13.9 | 29 | 86 | 0.032 | 43 | 0.15 | 0.029 |
| 10⁷ | 16.2 | 36 | 128 | 0.030 | 67 | 0.14 | 0.024 |
| 10⁸ | 18.4 | 50 | 202 | 0.032 | 96 | 0.15 | 0.023 |
| 10⁹ | 20.7 | 60 | 318 | 0.036 | 141 | 0.14 | 0.020 |
| 10¹⁰ | 23.0 | 93 | 422 | 0.035 | 186 | 0.18 | 0.024 |

(R2 reproduced all medians and the fitted slopes 3.147 and 2.286 from the raw files.)
* **Supply consistent with cubic growth.** S_e/(log p)³ stays in [0.027, 0.044] for all 36 primes; the least-squares
  exponent of the medians is 3.15. This is a fit over a factor 2 in log p for the two searched subfamilies, consistent
  with the brief's "cubic supply" and with the upper bound of Prop 6.3′; it is not an asymptotic law.
* **Coupon comparison.** In dyadic q-bands the unreached fraction of non-residue classes is close to the Poisson
  prediction exp(−λ_q), λ_q the number of distinct productive e per class, averaged over the classes of each q: for the
  single prime p = 10 000 000 033, q ∈ [128, 256): 0.142 observed vs 0.123; [256, 512): 0.387 vs 0.361 (R2's
  cell-weighted average over the four 10¹⁰ primes: 0.136 vs 0.122 and 0.379 vs 0.356). Evidence of fit in the measured
  bands, not of the extreme tail.
* **Fits of the reach.** q* grows with exponent 2.29 in log p; q*/(log p)² drifts up (0.13 → 0.18) and
  q*/((log p)³/log log p) stays at 0.020–0.029. The range cannot separate the two laws; the supply fit plus the coupon
  comparison favour R(p) ≈ c(log p)³/log log p, c ≈ 0.02–0.03 (Assessment), consistent with Cor 6.4 (MR false above
  (log p)³).
* **Majority reach at the scales §5 needs.** R_maj ≈ 0.35 (log p)² at 10¹⁰, i.e. above (log p)^{1.6}. MR₁(1/2, η)
  holds at all 36 primes and MR₁(1, η) at all sampled p ≥ 10⁶ (§5). For the classical-sieve scale (log p)^{2+δ} the
  coupon model needs 0.033 (log p)^{1−δ} ≳ (2 + δ) log log p, i.e. log p ≈ 840 for δ = 0.1 (R2's correction of an
  earlier arithmetic slip); with Props 5.1′/5.2 that scale is no longer needed.
* Lane B (z50) measured q* ≈ 11–29 with W1 words only; with the two ET subfamilies q* is 17–37 at 10⁶–10⁷, 43–83 at
  10⁸–10⁹ and 83–101 at 10¹⁰.
* **Controls** (`data/z51_forcing/reach_controls/`, standard cutoffs): hard primes 193, 409, 577, 2521, 3361 have q* =
  11 (the height bound modulus ≤ p leaves few classes); 5569: 17; 9601: 13; 66529: 23; 8813281: 29. The odd squares
  1002001 = 1001² and 9018009 = 3003² give q* = 31 and 29, like primes of that size: reach is congruence data and is
  blind to T1 (at a square every q is a residue, so Lemma 6.2 never fires there, consistent with T1). Numerator 8:
  Def 6.1 uses the 4/n identities only; nothing here transfers to 8/n.

### 6.4 "A reach for all p outside a set you can bound" (Assessment; R2-revised)

For each q and non-residue r, {n : r unreached at (n, q)} is a congruence-avoidance set in n's residues off q, with
supply ≈ S_e/q per class. We have no nontrivial upper bound for it, and a bound proved by CRT majorants would be
subject to the supply law of z50 A Thm 2.1 for that reduced family (an Assessment: its hypotheses were not verified
here). Since {p : Reach(p, q) fails} ⊇ {p : ES(p) fails, (q/p) = −1}, a bound for the reach-failure sets is at least as
strong as the corresponding statement for ES on the line (q/p) = −1. A power-small bound for reach failures at a
majority of q ≤ C log p would, through Cor 5.4, give the near-power ES bound; it would be genuine progress, and we do
not have it. The quantitative content of §§5–6 is: the needed reach scale drops to C log p (Prop 5.2), where reach is
numerically ubiquitous, while above (log p)³ reach provably disappears (Cor 6.4).

## 7. Least-QNR lines (work item 3)

### 7.1 What is known, and how it relates to reach (R2-revised)

* *Generic line.* (J)70 Comp 4.1 (CERTIFIED, exhaustive) shows that on the r-generic line (off-r coordinates all equal
  to 1) every non-residue cell mod r is covered at level 1 by the seven ET families for r ≤ 13, while for r = 17 the
  level-1 survivors are the cells {5, 7}. Sterile points on the r-generic line are PROVED for r ≥ 2^{21.4375} ≈ 2.84·10⁶
  ((J)70); for r = 17 sterility is conditional on the uniform-multiplicity Conjecture 4.2 of `SIBLING.md` ((J)77).
* *The whole least-QNR line.* The brief's "ES is known when n₂(p) ≤ 13" is, in the campaign's sources, a statement
  about the generic line; POINTWISE_MORDELL distinguishes the full n₂-line from its generic point and records open
  covering searches there (R2). Classically n₂(p) ∈ {3, 5, 7} is covered (Mordell). We do not use, and do not claim,
  a covering theorem for all primes with n₂(p) ∈ {11, 13}.
* *Dictionary (R2 correction).* Def 6.1 uses only the U and U⁻¹ box types; level-1 reach of these two families at the
  generic point is a *subset* of the seven-family level-1 coverage. R2's exhaustive generic-point computation for the two
  families finds missed non-residue cells {2, 6} at q = 11, {2, 5, 7, 8} at 13 and {3, 5, 6, 7} at 17 (seven families:
  none, none, {5, 7}). So a cell missed by all seven families is missed by ours, not conversely.
* *Growing coverings.* A p-dependent certificate for each prime on the 17-line proves ES there; it only has to hit p's
  actual cell, may use other families, higher levels or larger moduli. Pointwise Reach(p, 17) for every line prime is
  one *sufficient* target (Lemma 6.2), strictly more demanding than ES on the line.

### 7.2 Numerics on the 17-line (EVIDENCE; `scripts/z51_forcing_line17.sh`, `data/z51_forcing/line17_*.txt`)

All primes p ≡ 1 (8) with (3/p) = (5/p) = (7/p) = (11/p) = (13/p) = 1, (17/p) = −1 in [10⁶, 2·10⁶] (286 primes), every
third in [10⁷, 1.1·10⁷] (84) and every sixth in [10⁸, 1.01·10⁸] (36 primes); level-1 reach with the standard cutoffs
(Def 6.1), q ≤ 61. (R2 reproduced the table aggregates.)

| range | Reach(p,13) | **Reach(p,17)** | Reach(p,19) | Reach(p,23) | Reach(p,29) | Reach(p,31) |
|---|---|---|---|---|---|---|
| [10⁶, 2·10⁶] | 284/286 | **285/286** | 273/286 | 239/286 | 178/286 | 146/286 |
| [10⁷, 1.1·10⁷] | 84/84 | **84/84** | 84/84 | 84/84 | 71/84 | 76/84 |
| [10⁸, 1.01·10⁸] | 36/36 | **36/36** | 36/36 | 35/36 | 36/36 | 36/36 |

* The single failure of Reach(p, 17) is p = 1 240 009 (n₂(p) = 17), and the unreached cell is r = 5, one of the
  seven-family generic survivor cells {5, 7}. R2 confirmed this with an independent complete search (also without the
  cutoffs). p ≡ 12 (mod 17) lies in a reached cell, so ES(p) holds by an actual-cell certificate, e.g. (R2)
  q = 17, b₁ = 1, c = 4, e = 7: 4/1240009 = 1/2690839370144 + 1/1627512 + 1/382944 (checked exactly) — a concrete case
  of ES on the line without Reach(p, 17). Heuristic reading: p − 1 = 2³·3·7·11²·61, so p is close to the generic point
  at the small moduli that carry most of the supply. The two Reach(p, 13) failures (1 160 041, 1 487 641) miss one
  cell each; omitted families, the cutoffs or higher levels may each account for this.
* In the coupon model the expected number of unreached cells at q = 17 is ≈ 8·exp(−S_e(p)/17), S_e ≈ 0.033 (log p)³;
  Σ_p exp(−c(log p)³) < ∞, so the model predicts finitely many failures of Reach(p, 17) (a first-moment heuristic;
  the model's tail near generic obstructions is unproved). The samples agree (1/286 at 10⁶, none in the later samples).

### 7.3 What a proof would need (Assessment)

* *All p with n₂(p) = 17.* By Comp 4.1, if p ≡ 1 modulo a 17-free L, no level-1 class whose entire off-17 modulus
  4a₁b divides L covers the generic survivor cells; a level-1 certificate for p in those cells must use off-17 data not
  fixed by L, i.e. a p-dependent divisor event of B2 type. Higher levels and the other families cover parts of the
  cells (POINTWISE_MORDELL17), and full sterility at 17 is conditional, so this is not a theorem that no congruence
  argument can work. Prop 6.3′ is an *upper* bound on supply and does not show that any particular cell is supplied at
  a given p (R2 repair).
* *All p with n₂(p) ≤ R outside a power-small set.* For R = (log X)^A, A > 1 (or R = C log X) the primes with
  n₂(p) > R are X^{1/A+o(1)} (resp. X exp(−c log X/log log X)) by Props 5.1′/5.2, so the target is the exceptional-set
  problem on an essentially full set; Cor 5.4 gives the sufficient pointwise inputs. For fixed R it is an
  exceptional-set problem on a positive-density, congruence-defined set.
* *Forced windows on the 17-line.* 17 ≡ 1 (mod 4) is not a prime window for p ≡ 1 (4); at m = 51 the window
  x = (p + 51)/4 is a non-residue mod 17 but a residue mod 3 on the line, so the target −1 is not forced mod 3. The
  forced prime windows of line primes are at q₃(p) ≥ 19; §3's fixed-q bounds are averages over all primes and do not
  automatically transfer to this thin subpopulation.

## 8. Hostile reviews

* **R1 (Astra, `openai-codex/gpt-6-astra:high`, §§1–4; `reviews/z51-forcing-r1-astra.md`, check script
  `reviews/z51-forcing-r1-astra-check.py`).** Verdict: MAJOR revisions, no FATAL flaw; Lemma 2.2, Cor 2.3, Thm 3.1,
  Prop 3.2 and Prop 4.1 survive (the Henriot transfer was checked against the primary PDFs); the independent numerical
  audit matched all 7 423 window pairs. Repairs applied: dyadic Linnik in Obs 1.1(b) and the exact equivalence; odd p
  and the Type II equivalence in Lemma 2.1; lifted sharpness (now certified by the script); "exactly" withdrawn in 2(c)
  (with the referee's unforced example p = 353, q = 11); 2(d) recast as a limitation of the relaxed bound; "exact
  exponent" language replaced by upper-bound statements (q = 7 has rate 0 on p ≡ 1 (8)); growing-q uniformity marked
  unproved; the referee's real/non-real split of the Fourier majorant (a = 1 − 1/√3) adopted and the "1/3 cap"
  withdrawn; random-box truncation corrected (β > 3 log 3); RLD link labelled an analogy; correlation language weakened.
* **R2 (Astra, §§5–7 and whole document; `reviews/z51-forcing-r2-astra.md`, check script
  `reviews/z51-forcing-r2-astra-check.py`).** Verdict: MAJOR revisions; the advertised general "X^{1/2} cap for Linnik
  fed by congruence-certified forcing" FATAL as an unrestricted claim; Prop 5.1, Prop 6.3, Cor 6.4(a)–(b) and all
  numerics survive (independent reach enumeration at p = 100049 matched all 16 q; p = 1 240 009 and all 2 682
  witnesses re-verified; fits reproduced). Repairs applied: GRH status of MF corrected (GRH makes MF(A > 2) equivalent
  to ES); Heath-Brown's quadratic large sieve adopted (Prop 5.1′, the referee's argument), which lowers the robust
  scale to A > 1 and led to Prop 5.2 and Cor 5.5; Thm 5.3's forced-window clause repaired (separate exceptional set
  for q ≡ 3 (4), η < ½, one-sided bias); genuine dyadic proof of Cor 5.4; reach scope stated (two subfamilies, height,
  level) and the universal characterisation withdrawn; cutoff counterexamples recorded (E₁ = p/12 is a truncation);
  Prop 6.3 bookkeeping (ε = 1/C) and the level-k error of Remark 6.5 corrected (now inside Prop 6.3′); the X^{1/2}
  barrier withdrawn; numerics relabelled (subfamilies, consistent-with-cubic, coupon aggregation, prime R_maj,
  crossover log p ≈ 840); §7 dictionary corrected (two vs seven families; generic point vs whole line; growing
  coverings ≠ Reach; conditional sterility and correct citations).
* **R3 (Astra, the post-R2 additions: Props 5.1′, 5.2, Thm 5.3, Cors 5.4–5.5, Prop 6.3′, Cor 6.4;
  `reviews/z51-forcing-r3-astra.md`).** Verdict: MAJOR revisions, no FATAL; **the cap theorems (Cor 5.5) survive and
  "T2-lite reached" is fair** under the CONTEXT definition; Prop 5.1′, Lau–Wu Lemma 1 (checked against the primary
  manuscript), the subset restriction, Thm 5.3, Cor 5.4 and the GRH paragraph are SOUND or SOUND-WITH-MINOR; the MR₁
  numbers were reproduced independently from the raw files. Repairs applied: Prop 6.3′'s all-level argument completed
  with R3's Q ≤ X^θ / Q > X^θ split, Shiu-range checks and the restored log L; BT coprimality and boundary cases;
  average-vs-maximum wording in §§0, 6, 9; MF₁/MR₁ relabelled as new conjectural sufficient inputs (not a counted
  conditional target; MF₁ tests are vacuous); Prop 5.2 made quantitative with slack constants κ and p*; Thm 5.3 domain
  (p ≡ 1 (4) for windows, subset threshold ½); novelty credited to Heath-Brown/Baier and Montgomery–Vaughan/Lau–Wu;
  MR₁ evidence stated with η = 0.2 and as lower-bound tests.

## 9. Remaining gap

* **Pointwise forcing is still B2.** Every route here needs, at some point, a certificate for a *given* p in a
  *given* class: reach at a majority of q ∈ (C log p, 2C log p] (MR₁), or bias of the exceptional primes (MF₁). MR₁
  holds on every sampled prime (C = ½) and the coupon model predicts it for all large p, but no argument produces,
  for a fixed p and a fixed non-residue class r mod q, an e ≡ −r (mod q) with the needed divisor pair of p + e or
  ep + 1.
* **What the reductions buy.** By Thm 5.3(b), after removing X exp(−c log X/log log X) primes (those QR-biased at scale
  C log X, and separately those QR-biased on the q ≡ 3 (mod 4) of that range), the exceptional-set problem is the
  problem for exceptional p ≡ 1 (4) that have ≫ log X/log log X forced windows q ≡ 3 (4) in (C log X, 2C log X], all
  failing. At q ≍ log X a forced window fails when the ≈ (log X)^{1.1} divisor-ratio *choices* of (p + q)/4 (not
  distinct elements: the group has order ≍ log X) miss −1 — heuristically unlikely; but the per-window bounds we can
  prove (Kneser–Rankin for q ≲ 2 log log X; Fourier for q ≤ (log X)^{0.42}) do not reach q ≍ log X, and joint bounds
  over many windows are the G2 problem (Calc 4.2). A per-window failure bound at q ≍ log X whose saving survives
  multiplication over ≍ log X/log log X windows would give the near-power ES bound.
* **Counterfactual reach is polylogarithmic on average** (Cor 6.4): for the two tested ET subfamilies at height ≤ p, a
  prescribed q ≤ (log X)^C is reached for a ≪ (log X)^{3+o(1)}/q fraction of primes, and MR(A) fails for A > 3. The
  scales §5 needs (C log p, (log p)^{1+δ}) are far below that, so the obstruction is the pointwise proof, not the
  amount of supply.
* **Least-QNR lines.** ES on the 17-line by growing coverings is supported numerically (Reach(p, 17) at all but one of
  406 sampled line primes, and ES at that one by an actual-cell certificate); a proof needs p-dependent divisor events
  in the generic survivor cells {5, 7} (B2); full sterility at 17 is itself conditional.
