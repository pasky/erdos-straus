# EXSET_CHAR_FORCING — pointwise character forcing "(q/p) = −1 ⟹ ES(p)" with a growing reach

*Wave z51, lane 2c, slug `forcing`. Brief: `/home/pasky/projects/math/z51briefs/2c_opus_forcing.md`. ES is OPEN; nothing
here claims it proved or disproved. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Scripts `scripts/z51_forcing_*`, data `data/z51_forcing/`, reviews `reviews/z51-forcing-*`.*

## 0. Summary table

| # | claim | label | review |
|---|---|---|---|
| 1 | audit: what the Linnik route needs, which gate (G2–G4) each item attacks | Assessment | (pending) |
| 2 | window criterion and deterministic covering lemma | (pending) | (pending) |
| 3 | per-window failure rates; G4 checked | (pending) | (pending) |
| 4 | joint failure across windows; G2 loss | (pending) | (pending) |
| 5 | robust Linnik confinement | (pending) | (pending) |
| 6 | full Type I/II forcing reach, numerics to 10¹⁰, fits | (pending) | (pending) |
| 7 | least-QNR lines, n₂(p) = 17 | (pending) | (pending) |
| 8 | remaining gap | Assessment | — |

**Bottom line.** (pending)

## 1. Audit

### 1.1 The route and the input it needs

Notation. p ≡ 1 (mod 8) prime (p ≡ 5 (8) and p ≡ 3 (4) are classical). For a prime q ∤ 2p, (q/p) = (p/q) by
reciprocity. n₂(p) is the least quadratic non-residue (odd prime here). ES(p) means 4/p = 1/x + 1/y + 1/z.

**Forcing hypothesis F(R).** For every large prime p and every prime q ≤ R(p): (q/p) = −1 ⟹ ES(p).

**Observation 1.1 (PROVED, standard inputs; this is G3 made exact).**
(a) ES ⟹ F(R) for every R (trivially).
(b) F(R) with R(p) ≥ (log p)^A, A > 2, ⟹ #{p ≤ X : ES(p) fails} ≤ X^{2/A+o(1)}.
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
inputs that still feed Linnik (§5 below gives one: a *majority* of q suffices), and (iii) quantitative versions of the
gates.

### 1.2 Which gate each item attacks, and the door

* Item 1 (windows): G4 directly (per-window failure), then G2 (joint loss). Door: none new — the window mechanism is
  CAP_POINTWISE Thm 1.1; what is new is the exact failure law (§§2–3) and its interaction with G2 (§4).
* Item 2 (reach): G3. The reach is a *counterfactual* (profinite) statement: "every non-residue class of p mod q, with
  p's residues at all moduli prime to q kept, carries a certificate". It implies F at q, is not implied by ES, and its
  failure set is a congruence-avoidance set with supply ≍ (log p)³/q per class (§6). Door used by Linnik: primality of
  the exceptional moduli (z50 B §4.2; outside the CRT caps).
* Item 3 (lines): G3 at fixed q = 17; finite coverings are dead there in the (J)70/MORDELL17 sense, so only
  p-dependent (non-congruence) data can help (§7).

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

## 5. Robust Linnik confinement: a majority of q suffices

G3 and Observation 1.1 ask for confinement at *every* q ≤ (log p)^{2+δ}. Linnik's dual sieve does not need that:
it needs only a *bias* of the quadratic character on the small primes.

**Proposition 5.1 (biased characters are rare; PROVED, multiplicative large sieve + a moment trick).** Let X ≥ 3,
y ≥ 17, S := {primes q ≤ y}, m := |S|, 0 < η ≤ 1/2, and r := ⌊2 log X / log y⌋. Then
`  #{p ≤ X prime : Σ_{q∈S, q≠p} (q/p) ≥ 2ηm}  ≤  y + 2y·(log X/(2η²))^r.`
For y = (log X)^A and fixed η (or η ≥ (log X)^{−o(1)}) the right side is X^{2/A+o(1)}; for η = (log X)^{−θ} it is
X^{2(1+2θ)/A+o(1)}. The same holds with S replaced by the primes q ≡ 3 (mod 4) up to y (constants change).
*Proof.* Primes p ≤ y contribute ≤ y. For p > y put ε_q = (q/p). Let a_n := #{(q₁, …, q_r) ∈ S^r : q₁⋯q_r = n}.
Then Σ_n a_n (n/p) = (Σ_{q∈S} ε_q)^r ≥ (2ηm)^r on the bad set. By unique factorisation, a pair of r-tuples with
equal product consists of a tuple and one of its at most r! rearrangements, so Σ_n a_n² ≤ r!·m^r. All n ≤ y^r ≤ X².
The multiplicative large sieve restricted to primes and their Legendre characters gives
Σ_{p≤X} |Σ_n a_n (n/p)|² ≤ (X² + X²)·Σ a_n². Hence the number of bad p > y is ≤ 2X²·r!·m^r/(2ηm)^{2r}
= 2X² r!/((2η)^{2r} m^r). Since m ≥ y/log y and y^{r+1} > X², m^r ≥ X² y^{−1} (log y)^{−r}, so the count is
≤ 2y·r!(log y)^r/(2η)^{2r} ≤ 2y·(r log y/(4η²))^r ≤ 2y·(log X/(2η²))^r. With y = (log X)^A,
(log X)^r ≤ exp(2 log X·log log X/log y) = X^{2/A}, and (2η²)^{−r} = X^{o(1)} for η ≥ (log X)^{−o(1)}. ∎

This is the standard moment method for large character sums over primes; the point here is the consequence.

**Theorem 5.2 (robust Linnik reduction; PROVED from Prop 5.1).** Fix A > 2 and η ∈ (0, 1/2]. For every set 𝔈 of
primes,
`  #(𝔈 ∩ [1, X]) ≤ X^{2/A+o(1)} + #{p ∈ 𝔈 ∩ [1, X] : #{q ≤ (log X)^A : (q/p) = −1} > (½ − η)·π((log X)^A)}.`
So for 𝔈 = {p : ES(p) fails}, a power saving for ES is *equivalent* to a power saving for the exceptional primes
whose quadratic character is balanced on the primes up to (log X)^{2+δ}. Each such prime has at least
(½ − η)·π((log X)^A; 4, 3) − O(1) **forced windows** q ≡ 3 (mod 4), q ≤ (log X)^A (apply Prop 5.1 to that subset).
That is ≫ (log X)^A/log log X forced windows, all of which must fail (§§2–4).

**Corollary 5.3 (the weakest pointwise forcing input for Linnik; CONDITIONAL as stated).**
(a) Hypothesis MF(A, η): every large prime p for which ES(p) fails has #{q ≤ (log p)^A : (q/p) = −1} ≤
(½ − η)·π((log p)^A). If MF(A, η) holds for some A > 2 and η > 0, then #{p ≤ X : ES(p) fails} ≤ X^{2/A+o(1)}.
(b) MF(A, η) follows from the *majority-reach hypothesis* MR(A, η): for every large prime p ≡ 1 (mod 8), the
counterfactual reach (§6, Definition 6.1) holds at at least (½ + η)·π((log p)^A) primes q ≤ (log p)^A.
*Proof.* (a) Prop 5.1 with X replaced by dyadic ranges (for p ∈ (X^{1/2}, X], (log p)^A ≍_A (log X)^A; adjust η).
(b) Reach at q and (q/p) = −1 give ES(p) (the actual residue of p mod q is one of the reached non-residues). So an
exceptional p is a residue at every q where reach holds, and has ≤ (½ − η)·π QNRs. ∎

*How much weaker is this than G3's input (Assessment).* F(R) of §1 asks that every q ≤ (log p)^{2+δ} with
(q/p) = −1 force a certificate; MF asks only that exceptional primes be QR-*biased* there, with any fixed bias. Under
GRH, F at reach 2 log²p is equivalent to ES (Obs 1.1(c)). MF(A, η) with 2 < A < 4 is not known to imply ES even under
GRH: GRH bounds Σ_{q≤y}(q/p) log q by O(√y log²p), which excludes a fixed bias only for y ≫ (log p)^4. So MF is a
genuinely weaker input than F, and Theorem 5.2 is the exact form in which Linnik's door uses character data: it
excludes biased primes and nothing else (for the moment polynomial (Σ_q ε_q)^r; other polynomials in the signs
ε_q = (q/p) detect other *common* sign patterns, e.g. bias on a fixed subset of S, which is the same statement for a
smaller S). What it cannot use is p-dependent structure: QR on a set T_p ⊂ S that varies with p and has
|T_p| ≤ m/2.

*Is MF plausible, and is it circular? (Assessment.)* Heuristically the counterfactual reach is ≈ c(log p)³/log log p
(§6), so an exceptional prime would be QR at *every* q below that, and MF would hold with η = ½ − o(1) for any A < 3.
But "MF for all but X^{1−c} primes" is circular in the sense of G3: the exceptions to MF are themselves ES-exceptional.
Only a pointwise proof of MF (or of MR) breaks the circle. The gain over G3 is that the pointwise statement needed is a
majority statement, which is a natural target for averaging over q *at fixed p* (a single prime, many moduli),
rather than an every-q statement. §6 measures how far MR is from being true at accessible p.

## 6. Full Type I/II forcing reach (work item 2)

### 6.1 Definition and the forcing implication

Elsholtz–Tao classes (checked identities, `scripts/z51_forcing_reach_verify.py`):
* Type II (a, b, e), e | a + b: every n ≡ −e (mod 4ab) has 4/n = 1/(abd) + 1/(acdn) + 1/(bcdn), c = (a+b)/e,
  d = (n+e)/(4ab).
* Type I (b, c, e), e | b + c: every n ≡ −e⁻¹ (mod 4bc) has 4/n = 1/(nbck) + 1/(gb) + 1/(gc), k = (en+1)/(4bc),
  g = k(b+c)/e.
These are cubic families (three free parameters); they are subfamilies of all ES certificates.

**Definition 6.1 (counterfactual reach).** Let n ≡ 1 (mod 4) and q an odd prime, q ∤ n. A unit residue r mod q is
*reached at (n, q)* if some Type II class (a, b, e) with a = q·a₁, q ∤ a₁be, or some Type I class (b, c, e) with
b = q·b₁, q ∤ b₁ce, has class modulus 4q·a₁b (resp. 4q·b₁c) ≤ n, contains n modulo 4a₁b (resp. 4b₁c), and has residue
r at q (r ≡ −e, resp. −e⁻¹). In words: the profinite point "n at every modulus prime to q, r at q" lies in a
certificate class of modulus ≤ n. *Reach(n, q)* holds if every quadratic non-residue r mod q is reached.
(The modulus bound makes the notion finite: it forces e ≤ n/4 + 1 for both types. Our runs use E₂ = n/4, exact
for Type II, and E₁ = n/12 for Type I; the Type I tail e ∈ (n/12, n/4] needs b₁ = 1 or c = 1 and carries a negligible
part of the supply — at p = 10⁸ all e > 10⁷ together carry < 0.1 %.)

**Lemma 6.2 (reach forces; PROVED, trivial).** If Reach(p, q) and (q/p) = −1 then ES(p).
*Proof.* p ≡ 1 (4), so (p/q) = (q/p) = −1 and r := p mod q is a reached non-residue: the class contains p itself. ∎

Reach is *not* implied by ES (it is a statement about counterfactual points), and Lemma 6.2 is the only way it is
used. It is the natural formalisation of "congruence-certified forcing at q": any forcing statement for the line
(q/p) = −1 proved from certificate congruence classes that see p only through its residues at moduli prime to q is a
reach statement.

### 6.2 An upper bound for reach: reach is at most polylogarithmic (PROVED)

**Proposition 6.3 (PROVED modulo Shiu's Brun–Titchmarsh theorem for multiplicative functions).** Uniformly for primes
3 ≤ q ≤ (log X)^C,
`  Σ_{n ≤ X, n ≡ 1 (4)} #{r mod q : r reached at (n, q)}  ≪_C  X (log X)³.`
*Proof.* Each reached residue comes from a tuple (type, a₁, b, e) with a₁b ≤ X/(4q), e | qa₁ + b, and n in one class
modulo 4a₁b; so the sum is ≤ 2Σ_{a₁,b} τ(qa₁ + b)(X/(4a₁b) + 1). Group by n′ = qa₁ + b:
Σ_{a₁<n′/q} 1/(a₁(n′ − qa₁)) = (1/n′)Σ (1/a₁ + q/(n′ − qa₁)) ≤ (1/n′)(2 + 2 log n′ + q/r₀(n′)), where
r₀(n′) ∈ [1, q] is the least positive value of n′ − qa₁. Hence Σ_{a₁,b} τ(qa₁+b)/(a₁b) ≤ Σ_{n′≤X} τ(n′)(2 + 2 log n′)/n′
+ Σ_{r=1}^{q} (q/r) Σ_{n′ ≡ r (q), q < n′ ≤ X} τ(n′)/n′. The first sum is ≪ (log X)³. In the second, Shiu's theorem
(q < (n′)^{1/2}) gives Σ_{n′≡r (q), q² < n′ ≤ X} τ(n′)/n′ ≪ (log X)²/q for r ≢ 0, the range q < n′ ≤ q² contributes
≪ q^{ε−1} log q, and r = q (n′ ≡ 0) contributes ≪ (log X)²; so the second sum is ≪ (log X)² log q. The "+1" terms
give Σ_{a₁b≤X/(4q)} τ(qa₁ + b) ≤ (X/(4q))·Σ τ/(a₁b) ≪ X(log X)³/q. ∎

**Corollary 6.4 (PROVED from Prop 6.3).** Uniformly for 3 ≤ q ≤ (log X)^C:
(a) #{p ≤ X prime : Reach(p, q)} ≪ π(X)(log X)⁴/q. So for q ≥ (log X)^{4+ε}, reach at q fails for almost all p.
(b) For A > 4 and η > 0, the number of p ≤ X with Reach(p, q) for at least η·π((log X)^A) primes q ≤ (log X)^A is
≪ π(X)(log X)^{4−A+o(1)}/η. So MR(A, η) of Cor 5.3 is *false* (for almost all p) when A > 4.
(c) If S is a set of primes q ≤ (log X)^C such that Reach(p, q) holds for every q ∈ S for at least half of the
primes p ≤ X, then |S| ≪ (log X)⁴ log log X. For such S, the integers ≤ X² composed of primes from S number at most
Ψ(X², π⁻¹(|S|)) = X^{3/2+o(1)} (the count is largest for the first |S| primes), so Linnik's bound
(X² + X²)/|𝒜| for confinement to S cannot beat X^{1/2−o(1)}.
*Proof.* (a) A reach at q needs all (q−1)/2 non-residues reached; Markov over n ≤ X with Prop 6.3, and
π(X) ≍ X/log X. (b) Sum (a) over q ≤ (log X)^A (Σ 1/q ≪ log log X) and divide by η·π((log X)^A). (c) Sum (a) over
q ∈ S: |S|π(X)/2 ≤ Cπ(X)(log X)⁴ Σ_{q∈S} 1/q ≤ Cπ(X)(log X)⁴·O(log log X). ∎

**Reading (T2-barrier, exact scope; Assessment on PROVED inputs).** Linnik confinement fed by *congruence-certified*
forcing (reach in the sense of Def 6.1: ET Type I/II classes of modulus ≤ p) has, for most p, at most (log X)^{4+o(1)}
moduli q to work with. With the multiplicative large sieve over S-smooth sequences it therefore cannot give a bound
better than X^{1/2+o(1)} for the exceptional set (Cor 6.4(c)), and the robust form (Thm 5.2, Cor 5.3(b)) is limited to
A ≤ 4 in the same way. This does not prevent a power saving (X^{1/2} would be a power saving); it says that
congruence-certified forcing plus Linnik is capped at the square-root level, and, by the numerics below
(reach ≈ c(log p)³/log log p), heuristically at X^{2/3}. The cap concerns the method; the true forcing statement F(R)
holds for every R if ES is true.

### 6.3 Numerics (EVIDENCE; `scripts/z51_forcing_reach.c`, `…_reach_batch.sh`, `…_reach_summary.py`)

36 primes p ≡ 1 (mod 8): eight each near 10⁵, 10⁶, 10⁷ ("exact": E₂ = p/4, E₁ = p/12, see Def 6.1), four near 10⁸ (exact), four
near 10⁹ (e ≤ 2·10⁷) and four near 10¹⁰ (e ≤ 10⁷); all odd primes q ≤ 1000. The truncation at e ≤ 10⁷ loses ≈ 3 % of
the supply (at p = 10⁸: 42 %, 72 %, 89 %, 97 %, 99.97 % of the exact supply from e ≤ 10³, 10⁴, 10⁵, 10⁶, 10⁷). 2 682
randomly sampled witnesses (1 274 Type I, 1 408 Type II) were rebuilt into explicit 4/n identities and checked with
exact rationals: 0 failures. Per-prime table: `data/z51_forcing/reach_summary.txt`; raw per-q data:
`data/z51_forcing/reach/`.

Statistics: q* = least q with an unreached non-residue class; S_e = supply, the mean over q ∈ [11, 300] of q times
the mean number of distinct productive (type, e) per non-residue class (each (type, e) feeds exactly one class mod q);
R_maj = largest R ≤ 1000 such that reach holds at ≥ 60 % of the odd primes q ≤ R.

| p ≈ | log p | median q* | median S_e | S_e/(log p)³ | median R_maj | q*/(log p)² | q*/((log p)³/log log p) |
|---|---|---|---|---|---|---|---|
| 10⁵ | 11.6 | 17 | 49 | 0.032 | 34 | 0.13 | 0.027 |
| 10⁶ | 13.9 | 29 | 86 | 0.032 | 43 | 0.15 | 0.029 |
| 10⁷ | 16.2 | 36 | 128 | 0.030 | 67 | 0.14 | 0.024 |
| 10⁸ | 18.4 | 50 | 202 | 0.032 | 96 | 0.15 | 0.023 |
| 10⁹ | 20.7 | 60 | 318 | 0.036 | 141 | 0.14 | 0.020 |
| 10¹⁰ | 23.0 | 93 | 422 | 0.035 | 186 | 0.18 | 0.024 |

* **Supply is cubic.** S_e/(log p)³ stays in [0.027, 0.044] for all 36 primes; the least-squares exponent of the
  medians is 3.15. This confirms the brief's "cubic supply" for the full ET Type I/II families with modulus ≤ p.
* **The coupon model fits.** In dyadic q-bands the unreached fraction of non-residue classes matches the Poisson
  prediction exp(−λ_q), λ_q = (distinct productive e per class), within 10–20 % relative (e.g. p ≈ 10¹⁰,
  q ∈ [128, 256): 0.142 observed vs 0.123; q ∈ [256, 512): 0.387 vs 0.361).
* **Fits of the reach.** The first-hole statistic q* grows with exponent 2.29 in log p; q*/(log p)² drifts up
  (0.13 → 0.18) and q*/((log p)³/log log p) stays at 0.020–0.029. The range 10⁵–10¹⁰ (log p ratio 2) cannot separate
  the two laws by the first-hole statistic alone; the supply law plus the validated coupon model favour
  R(p) ≈ c·(log p)³/log log p with c ≈ 0.02–0.03 (heuristic, Assessment).
* **Majority reach is far below (log p)^{2+δ} at accessible p.** R_maj ≈ 0.35 (log p)² at 10¹⁰. In the coupon model
  with S_e ≈ 0.033 (log p)³, reach at q ≈ (log p)^{2+δ} needs 0.033 (log p)^{1−δ} ≳ log q; for δ = 0.1 this happens only
  for log p ≳ 200 (p ≳ 10⁸⁷). So MR(2 + δ, η) — the input Cor 5.3 needs — is numerically false at every accessible p
  and heuristically true only for astronomically large p. MR(A) for A > 3 fails heuristically for all large p, and for
  A > 4 provably for almost all p (Cor 6.4).
* Lane B (z50) measured q* ≈ 11–29 with W1 words only; with all ET Type I/II classes q* is 17–37 at 10⁶–10⁷, 43–83
  at 10⁸–10⁹ and 83–101 at 10¹⁰.
* **Controls** (`data/z51_forcing/reach_controls/`, exact): hard primes 193, 409, 577, 2521, 3361 have q* = 11 (the
  size bound modulus ≤ p leaves few classes); 5569: 17; 9601: 13; 66529: 23; 8813281: 29. The odd squares
  1002001 = 1001² and 9018009 = 3003² give q* = 31 and 29, like primes of that size: reach is congruence data and is
  blind to T1 (at a square every q is a residue, so Lemma 6.2 never fires there, consistent with T1). Numerator 8:
  Def 6.1 uses the 4/n identities only; nothing here transfers to 8/n.

### 6.4 "A reach for all p outside a set you can bound" (Assessment)

For each q and non-residue r, the set {n : r unreached at (n, q)} is a congruence-avoidance set over n's residues off q,
with supply ≈ S_e/q ≍ (log n)³/q. Any bound for its size obtained by CRT methods is subject to the supply law of
z50 A Thm 2.1 for that reduced family, so it is weaker than the corresponding bound for ES itself. Moreover
{p : Reach(p, q) fails} ⊇ {p : ES(p) fails, (q/p) = −1} (Lemma 6.2). So "Reach for all p outside a bounded set", fed
into Linnik, returns an exceptional-set bound no better than the bound already needed for the reach-failure set: the
route is circular unless reach is proved pointwise, as G3 says. What §§5–6 add is quantitative: the pointwise input
can be weakened to a majority (Cor 5.3), but the majority input is false for A > 4 and heuristically needs p ≳ 10⁸⁷
for A slightly above 2.

## 7. Least-QNR lines (work item 3)

(pending)

## 8. Hostile reviews

(pending)

## 9. Remaining gap

(pending)
