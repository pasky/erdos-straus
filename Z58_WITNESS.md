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

*Reading (Assessment).* No ordering has a polylog worst case on the data: the worst primes have only a handful of
solutions and those sit at polynomial height in every coordinate. A deterministic rule would need a structural reason
for *where* the few solutions of a hard prime lie. §3 tests that (TODO).

## 3. Where the solutions of hard primes sit (TODO)
## 4. Witness vs continued fractions / Farey / two-square data (TODO)
## 5. Verdict (TODO)
