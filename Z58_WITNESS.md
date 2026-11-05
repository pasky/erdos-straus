# Z58_WITNESS — the raw d-statement of (MS): which witnesses fire, in what order, at what size

Status: z58 lane WITNESS (brief `z52bbriefs/z58_lanes.md` §WITNESS, common rules `z52bbriefs/z53_depth.md` with
z53 → z58). Internal; **ES is OPEN; nothing here proves or disproves ES, (★) or (MS).** Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z58_witness_*`, data `data/z58/witness/`.
**CHECKPOINT 1 (≈ 40 min in).** Sections marked (TODO) are not yet done.

## 0. Falsifier table (MANDATORY; the "idea" of this lane = a deterministic witness rule p ↦ (u, C) or p ↦ d)

| screen | how a witness rule behaves | where primality must enter |
|---|---|---|
| **F1 odd squares** | No rule can fire: R(m²) = 0, every hit class is a Jacobi non-residue mod d (Z57_SYNTH Lemma A.1(b)). Any rule whose output depends only on p mod M (fixed M) fails on the squares of that class; all six classes of 𝔐 are squares mod 840, so *no congruence-only rule exists on 𝔐* (PROVED, trivial: m² in the class of p has the same residues mod every d \| M). | A proof that the rule fires must contain a step producing a divisor d of p + u (or of 4Cp + 1) with **Jacobi (p/d) = −1** (Lemma 1.1 below). That is the identifiable square-killing step; for a rule reading the factorisation of p + u it is "p + u has a prime factor ℓ with (ℓ/p) = −1 in the right class". |
| **F2 C-even sub-line** | A rule must be allowed to output odd C. On the 12 R₈-zeros in [10¹⁰, 1.1·10¹⁰] every rule restricted to C even (equivalently d = 4uC − 1 ≡ −1 (mod 8u)) fails. The rules studied here (least d, least u, least C, least 4uB) range over both parities; their parity split is reported in §3 (TODO). | Same as F1 plus: the argument must not be a statement about the c = 1 line of 8/p. |
| **F3 composites** | All least-witness rules output nothing at the 285 composite zeros. 214/285 are divisible by 3, 36 more by 5, 15 by 7 (CERTIFIED, `data/z58/screens/composite_zeros_le8e6.txt` + sympy): **at composite n every modulus d sharing a factor with n is dead** (u \| (d+1)/4 forces gcd(d, u) = 1, and n ≡ −u (d) then forces gcd(d, n) = 1). Primality enters by keeping *all* d < p alive. This is a genuine but weak use: composites with least prime factor ≥ 29 (e.g. a zero with least factor 443) lose almost no moduli and are still zeros. | Beyond "all moduli alive", no step of any rule here uses primality. |
| **F4 known zeros** | At the 14 (★)-zeros no witness exists in any ordering (CERTIFIED by the scan, all four orderings report "none"). At the 38 𝔊*-zeros witnesses exist but are huge in the d- and C-orderings (e.g. 564 661 441: d_min = 2 741 075, C_min = 76 141). A rule "fires within bound F(p)" must have F(p) above the observed record curve (§2), and any proof must have threshold > 8 813 281. | — |

Bottom line of the table (Assessment): a witness rule is just (MS) with a search order; it passes F1/F4 only if its
proof contains a Jacobi-sign step and a threshold, and it passes F3 only through the "all moduli coprime to p" property.
No rule found so far survives as a HOT LEAD.

## 1. Precise statements and first lemmas

For p prime ≡ 1 (4) (also any odd n) define, over the (★) solution set S(p) = {(u, B, C) : 4uBC − u − B = p}:
* d_min(p) = min over S of min(4uC − 1, 4BC − 1) = least d ≡ 3 (4) with (−p mod d) \| (d + 1)/4 (raw d-form);
* u_min(p) = min over S of min(u, B) = least u with a divisor of p + u in −1 + 4uℤ (u-form);
* C_min(p) = min over S of C = least C with a divisor of 4Cp + 1 in −1 + 4Cℤ (divisor/level form);
* q_min(p) = min over S of 4uB (pair form p ≡ −(u+B) mod 4uB); m3(p) = min(d_min, q_min) = least of the three moduli.
All equal "none" iff R(p) = 0. (PROVED: the definitions via S and the single-form searches agree by Lemma A.1 of
Z57_SYNTH; CERTIFIED cross-check: brute-force enumeration of S(p) for all primes p ≡ 1 (4) ≤ 20 000, 1 125 primes,
0 mismatches in all four quantities, `scripts/z58_witness_scan.c` vs an independent Python enumerator.)

**Lemma 1.1 (PROVED; the n_p claim of the brief, made precise).** Let p ≡ 1 (8) be prime, (u, B, C) ∈ S(p). Then each of
the three moduli 4uC − 1, 4BC − 1 and uB has a prime factor ℓ with (ℓ/p) = −1; hence d_min(p) ≥ n_p, q_min(p) ≥ 4n_p,
and every solution has uC ≥ (n_p + 1)/4 and BC ≥ (n_p + 1)/4. No such bound holds for u_min or C_min alone.
*Proof.* d = 4uC − 1 divides p + u, so p ≡ −u (mod d) and (p/d) = (−u/d) = −1 (Lemma A.1(b)); by multiplicativity of
the Jacobi symbol some prime ℓ \| d has (p/ℓ) = −1, and (ℓ/p) = (p/ℓ) by reciprocity (p ≡ 1 (4)). Same for 4BC − 1 by
the symmetry u ↔ B. For uB: 4uBC = p + u + B gives p ≡ −(u + B) (mod 4uB), and χ_{−4uB}(−(u+B)) = −1
(BM_CORRECTED_COUNT Thm 1.1, PROVED there), so χ_{−4uB}(p) = −1; for odd p ≡ 1 (4) this Kronecker symbol is the
Legendre symbol (−4uB/p) = (uB/p), and (2/p) = 1 for p ≡ 1 (8), so an odd prime factor ℓ of uB has (ℓ/p) = −1. ∎
*Consequence.* A rule producing a witness with d = 4uC − 1 ≤ g(p) proves n_p ≤ g(p) on its domain; g = polylog is
GRH-strength (Bach), g = p^θ with θ < 1/(4√e) beats Burgess. A rule with small u alone (or small C alone) proves nothing
about n_p. (The data below show neither small-u nor small-C rules exist anyway.)

## 2. Exhaustive census to 10⁹ (CERTIFIED computation; EVIDENCE for the growth reading)

`scripts/z58_witness_scan.c` (d-loop with early exit; u- and C-forms by Pollard–Brent factorisation of p + u, 4Cp + 1;
pair form by a doubling box search), all 25 423 491 primes p ≡ 1 (4) ≤ 10⁹ (six chunks, ≈ 4 min), aggregated by
`scripts/z58_witness_agg.py` → `data/z58/witness/agg1e9_{summary,records}.txt`, `agg1e9_hard.txt.gz`.
* R(p) = 0 exactly at the 14 known primes (re-confirmed, independent engine).
* **Typical sizes do not grow.** Mean log d_min over 𝔐-primes is 3.739, 3.749, 3.755, 3.760, 3.762, 3.764 on the
  half-decades 10⁶ … 10^8.5 (non-𝔐: 1.906 throughout). Reason (PROVED, trivial): for fixed d the event "d fires" is a
  union of |H_d| residue classes mod d, of fixed density among primes; so d_min(p) has a *limiting distribution*
  (Dirichlet), and only its tail matters.
* **The tail is polynomial in every ordering** (records over p ≤ 10⁹; value @ p, 𝔐 marked *):
  * d_min: 2 953 943 @ 85 664 329* (≈ p/29); 2 741 075 @ 564 661 441* (the last 𝔊*-zero).
  * u_min: 1, 2, 4, 6, 19, 26, 78, 131, 410 @ 4 160 641*, **469 @ 53 325 721*** (max to 10⁹).
  * C_min: 76 141 @ 564 661 441*; 41 027 @ 85 664 329*.
  * q_min: 37 223 480 @ 743 804 881* (≈ p/20).
  * m3 = least of the three moduli: 193 763 @ 413 490 001* (≈ 0.35 p^{2/3}; the trivial bound is 1.93 p^{2/3}).
* In 𝔐, n_p ≥ 11 always (𝔐 ⊂ squares mod 840), and d_min = n_p (the least non-residue prime itself fires) for 22.8 %
  of 𝔐-primes in (10^8.5, 10⁹].

* **The least coordinate s(p) := min(u_min, C_min) = min over S(p) of min(u, B, C)** (every solution has a coordinate
  ≤ ((p + u + B)/4)^{1/3}). Records over p ≤ 10⁹: 1, 2, 3, 5, 11, 16, 18, 36, 44 @ 963 481*, 67 @ 42 691 489*,
  **201 @ 413 490 001*** (CERTIFIED). max s(p)/log²p = 0.511 and max s(p)/log p = 10.1, both at 413 490 001; no prime
  p ≡ 1 (4), 10⁵ < p ≤ 10⁹, with R(p) ≥ 1 has s(p) > 0.52 log²p. Extension to (10⁹, 10¹⁰]: §5.

### 2.1 First-firing dynamics in d-order (CERTIFIED counts; EVIDENCE for the fitted laws)
`scripts/z58_witness_surv.py`, `data/z58/witness/surv_1e8_1e9.txt`, `surv_3e6_3e7.txt`.
* *Limit law (PROVED, Dirichlet).* For fixed D, P(d_min(p) > D) over 𝔐-primes tends to the CRT avoider density
  δ_𝔐(D) of the classes avoiding H_d for all d ≤ D. The empirical survival agrees across p-ranges for D ≲ p^{1/2}
  (e.g. D = 10³: 1.63 % on (3·10⁶, 3·10⁷], 1.70 % on (10⁸, 10⁹]) and drifts upward (fatter) for D ≳ p^{1/2}.
* *Not Poisson.* With E(D) := Σ_{d ≤ D} dens_𝔐(d) (exact Dirichlet density of "d fires" on 𝔐; mean number of firing
  moduli ≤ D), the ratio −log S(D)/E(D) falls from 1.1 (D = 18) to 0.84 (10³), 0.77 (10⁴), 0.71 (10⁵): the firing
  events are positively associated (clustered), and S(D) ≈ exp(−0.087 log²D) for 10³ ≤ D ≤ 10⁵ (EVIDENCE fit; 0.0854,
  0.0868, 0.0880, 0.0869 at D = 10³, 10^{3.5}, 10⁴, 10⁵) while E(D) ≈ (0.10 → 0.12) log²D.
* *Semi-local law* (`scripts/z58_witness_semi.py`, `semilocal_1e6_1e9.txt`): over 𝔐-primes in three decades
  10⁶–10⁹, P(u_min > U) ≈ exp(−κ log p·log(U+1)) with κ_u = 0.13 (at U = 32–128: 0.124–0.135 in all three decades),
  κ_C ≈ 0.10, κ_s ≈ 0.17 (s = min(u_min, C_min)). The per-u probability is *not* a power of p at small u: P(u_min > 1)
  = 0.577, 0.539, 0.506 by decade, i.e. ∝ (log p)^{−1/2} (the half-dimensional sieve for "(p+1)/2 has no prime factor
  ≡ 3 (4)"); the power-law form is a fit over moderate U only.

## 3. Where the solutions of hard primes sit (EVIDENCE; CERTIFIED solution lists)

Solutions listed by `scripts/z58_witness_sols.c` (three-loop enumerator, validated against brute force for all odd
n ≤ 6000, 0 mismatches). Hard set: the 270 primes p ≡ 1 (4) ≤ 10⁹ with 1 ≤ R(p) ≤ 4 (from `z57_synth_tri.c` run to 10⁹,
`data/z58/witness/tri1e9_R6.txt`; its census line reproduces the 14 zeros), restricted to p ≥ 10⁶ (103 primes, 188
unordered solutions) or ≥ 10⁷ (45, 82). Controls: 341 𝔐-primes spread over [10⁷, 10⁹] (8 493 solutions). Log-coordinates
x, y, z = log P, log Q, log C over log(p/4) (P < Q the pair; x + y + z ≈ 1). `scripts/z58_witness_loc.py`,
`loc_lowR4_vs_ctrl2*.txt`, `scripts/z58_witness_disp.py`, `disp_ctrl2.txt`.
* **Controls follow the uniform law on the simplex.** P(min(x, y, z) > t) = 0.477, 0.302, 0.164, 0.066 at
  t = 0.1, 0.15, 0.2, 0.25 against (1 − 3t)² = 0.490, 0.303, 0.160, 0.062 (only t = 0.05 deviates: 0.701 vs 0.722,
  the O(1)-parameter excess).
* **Hard primes' solutions are central.** P(min > 0.1) = 0.82 (≥ 10⁶) / 0.85 (≥ 10⁷) against 0.48; KS on the min
  coordinate p ≈ 4·10⁻²¹ / 6·10⁻¹¹ (asymptotic KS, solutions treated as independent — indicative only). The record
  prime 413 490 001 has exactly the two solutions (241, 2134, 201) and (458, 1101, 205): every coordinate lies in
  [201, 2134], within a factor 4.6 of (p/4)^{1/3} ≈ 469.
* **Mechanism (EVIDENCE): boundary clustered, centre near-Poisson.** For the controls at t = 0.1 the boundary count
  (min coordinate ≤ t) has mean 13.0, var/mean 3.25, P(empty) = 0.3 % (Poisson e^{−13} ≈ 2·10⁻⁶); the centre count has
  mean 11.9 and var/mean 1.16 (1.09 at t = 0.15). Boundary solutions are divisor-class events of *one* integer p + u
  or 4Cp + 1 and come in clusters (an integer with many divisors fires many times); centre solutions involve distinct
  integers. Hardness is therefore "boundary empty, then a thin Poisson lottery in the centre". (Cf. FAMDESIGN §4.2:
  CROSSF's window near-Poisson, full count overdispersed — consistent; the boundary/centre split by the least
  coordinate is the new reading.)
* **Rooting at n_p fails on hard primes.** Some solution has n_p dividing one of its three moduli at 338/341 control
  primes but only at 45/103 hard primes (17/45 for p ≥ 10⁷). A rule "search moduli divisible by n_p" misses most hard
  primes (CERTIFIED for those primes, from the complete solution lists).
* **C-parity at hard primes:** 44–48 % of their solutions have C even (controls 49.5 %): no parity selection.

**Proposition 3.1 (CONDITIONAL on Dickson's prime k-tuples conjecture; bounded-coordinate rules die).** For every
S ≥ 1 there are infinitely many primes p ≡ 1 (mod 840) (so p ∈ 𝔐) with s(p) > S, i.e. every (★) solution of p has
min(u, B, C) > S. Explicitly: let L_S = lcm(840, 4u(u + 1), 4u(4u + 1) : 1 ≤ u ≤ S) and p = 1 + L_S k; if
p, q_u := (p + u)/(u + 1) (1 ≤ u ≤ S) and r_C := (4Cp + 1)/(4C + 1) (1 ≤ C ≤ S) are all prime, then s(p) > S.
*Proof.* (i) u ≤ S. Since (u + 1) | L_S, q_u = 1 + (L_S/(u + 1))k is an integer, and 4u | L_S/(u + 1) because
4u(u + 1) | L_S, so q_u ≡ 1 (mod 4u). For p > (u + 1)² we have q_u > u + 1, so the divisors of p + u = (u + 1)q_u are
g and g·q_u with g | u + 1, all ≡ g (mod 4u). As 1 ≤ g ≤ u + 1 < 4u − 1, none is ≡ −1 (mod 4u). By Lemma A.1 (u-form)
no solution has u ≤ S, and by the symmetry u ↔ B none has B ≤ S. (ii) C ≤ S. (4C + 1) | L_S gives
r_C = 1 + (4C L_S/(4C + 1))k ≡ 1 (mod 4C); for p large r_C > 4C + 1, so the divisors of 4Cp + 1 = (4C + 1)r_C are
≡ g (mod 4C) with g | 4C + 1, g ≤ 4C + 1; g ≡ −1 (mod 4C) would force g = 4C − 1, which is coprime to 4C + 1 (both odd,
difference 2) and > 1, so does not divide it. No solution at level C ≤ S. (iii) The 2S + 1 forms 1 + a_i k all equal
1 at k = 0, so no prime divides their product for every k (admissible); Dickson gives infinitely many k. ∎
*CERTIFIED instances* (`scripts/z58_witness_dickson.py`, `dickson.txt`, verified by the scan, `dickson_scan.txt`):
S = 1: 9 241, 15 121, 51 241; S = 2: 1 202 041 (s = 6), 1 564 921 (4), 2 532 601 (4); S = 3: 94 807 441 (s = 11),
2 682 912 961 (6), 26 678 957 761 (4). (S = 4, L_4 = 1 113 840: none with k ≤ 3·10⁶.) All have R(p) ≥ 1.
*Scope.* This kills every witness rule that inspects only solutions with some coordinate ≤ S for a fixed S — a
*multiplicative* menu (the factorisations of p + u and 4Cp + 1), not a congruence menu, so it extends B1/Prop A.3 of
Z57_SYNTH to non-congruence finite menus (conditionally). It is the (★)-analogue of CAP_BOUNDED Thm 1.3 (windows) and
the forest results of FRONTIER §3 (same Dickson technique). *Escape hatch:* S growing with p. The construction needs
2S + 1 simultaneous primes of size ≍ p, heuristically available only while S ≲ log p/(2 log log p).
