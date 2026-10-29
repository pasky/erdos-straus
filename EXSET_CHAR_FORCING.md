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
*Proof.* (b) If ES(p) fails then (q/p) = +1 for all q ≤ (log p)^A; for p ∈ (X^{1/2}, X] this includes all
q ≤ (½ log X)^A. Linnik's large sieve in the form of CAP_BOUNDED Thm 3.2 (with 𝒜 = products of primes
q ≤ y = (½ log X)^A, no congruence restriction on q; |𝒜 ∩ [1, X²]| = X^{2(1−1/A)+o(1)}) gives
≤ (X² + X²)/X^{2−2/A+o(1)} = X^{2/A+o(1)} such p; p ≤ X^{1/2} are trivially few. (c) Under GRH n₂(p) < 2 log²p
(Bach 1990, recalled). ∎

So F at reach ≍ log²p is, modulo GRH, *equivalent* to ES for large p; unconditionally it is equivalent to ES outside
the Linnik set {n₂(p) > (log p)^A}. Any proof of F at that reach is a pointwise ES theorem on the generic part of the
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

**Lemma 2.1 (window criterion; PROVED, classical).** Let p be prime and x an integer with p ∤ x and 4x > p; put
m := 4x − p. Then 4/p = 1/x + 1/y + 1/z has a solution in positive integers y, z iff there are divisors d₁, d₂ of px
with m | d₁ + d₂. All divisors of px are units mod m (a common prime of x and m divides p, and p ∤ x;
gcd(p, m) = gcd(p, 4x) = 1), so the condition reads
`  −1 ∈ R(px) := R(x) ∪ p·R(x) ∪ p⁻¹·R(x),   R(x) := { ∏ s^{e_s} : |e_s| ≤ v_s(x) } ⊂ (ℤ/m)^×.`
The part −1 ∈ R(x) gives solutions with p | y and p | z ("Type II at x"); the parts p^{±1}R(x) give solutions with
exactly one of y, z divisible by p. ES(p) holds iff some x > p/4 with p ∤ x works.
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
inside the quotient ℤ/2d (in logs, B = [−(d−1), d−1] ∌ d).
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
* (c) Forcing removes exactly the index-2 failure mode, in which every prime of x lies in U. That Landau-type event
  has probability ≍ (log X)^{−1/2} and is what kills *unforced* windows (FORCED_WINDOW §8.6 for q = 3). Every remaining
  failure needs all but at most d − 1 prime factors of x in a subgroup of index 2d ≥ 2ℓ_q in G.
* (d) *Deterministic limit.* For H = {1} (d = u) the condition is only Ω_{≢1 (q)}(x) ≤ (q − 3)/2, which holds
  automatically once q > 2 log₂ x + 3. So the covering lemma constrains failures only while q is small compared with
  the typical Ω(x) ≈ log log p (precisely: its Rankin form in §3 is non-trivial only for q ≲ 2 log log X). Beyond that
  a window behaves like a random box (§3.3).

*Checks (CERTIFIED).* `scripts/z51_forcing_kneser.py 15 4` and `… 41 3`: all 629 507 multisets of at most 4
(resp. 3) logs in ℤ/2u for odd u ≤ 15 (resp. ≤ 41); in the 468 185 cases with −1 ∉ B, (i)–(iii) hold, and sharpness
holds. `scripts/z51_forcing_windows.c` verifies Cor 2.3 on every failing forced window of 77 724 primes p ≡ 1 (8)
(all p ∈ [10⁶, 2·10⁶] and 20 000-prime samples in [10^k, 1.1·10^k] for k = 8, 10, 12; forced windows q ≡ 3 (4),
q ≤ 400): 936 503 Kneser checks, 0 violations. q = 3 and q = 7 never fail, as proved.

## 3. Per-window failure: the exact exponent for fixed q, and G4

(pending)

## 4. Many windows: what joint bounds can and cannot give (gate G2)

(pending)

## 5. Robust Linnik confinement

(pending)

## 6. Full Type I/II forcing reach (work item 2)

(pending)

## 7. Least-QNR lines (work item 3)

(pending)

## 8. Hostile reviews

(pending)

## 9. Remaining gap

(pending)
