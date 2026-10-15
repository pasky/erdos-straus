# AGENT_REPORT_O221 — spark relay Y10: T1 deformed to polynomially-near squares (checkpoint 1)

Branch side-agent/near-square. Deep file NEAR_SQUARE.md; memos BRAINSTORM/y10_*.md (8, indexed in README);
scripts scripts/ns_*. ES is not solved; no infinite case of ES is claimed beyond what explicit polynomial identities
give (each verified family is an identity valid on a residue class of m).

## SHARP
1. **The sterile set of polynomial ES families on p = m² − j is "m − √j is a square in ℚ(√j)", one level finer than
   the congruence sterile set "p is a square in ℚ".** Thm 3.4 (PROVED, Hilbert reciprocity in K = ℚ(√j)): the K-adic
   square set Z_K⁺ meets no family's class. At j = 8 the classes left uncovered by all congruence families plus all 76
   escaping families found are *exactly* the classes meeting Z_K⁺ (unit squares) at L = 8064 and 4480 (2-adic m ≡ 3 mod 8 from
   m − 2√2 ≡ (a + b√2)² mod 4√2; inert 3, 5; split 7 = both m ∓ 1 squares). CONJECTURE Y10-S: equality in general.
2. **Sign of k = the archimedean place.** Above the squares (k > 0) every Type I/II polynomial family in m has a
   witness that is a fixed character of n — polynomial families are no stronger than congruences at locally-square m
   (Thm 2.2, PROVED by exhaustive shape analysis; every escaping shape needs (Λ−1)·N(ρ + √−k) + N(r + √−k) = 0).
   Below (k < 0) escaping families exist (e.g. 4/2801 = 1/29421704 + 1/702 + 1/283608 from the family a = 1,
   c = (m+1)/2, d = (m−1)/2, f = 7 on m ≡ 53 mod 56, whose class contains m with n ≡ 1 mod every L).
3. **Witness dictionary (PROVED, Lemmas 1.1/1.3).** Every Type I solution of n ≡ 1 (4) has (d/n) = −1, every Type II
   (f/n) = −1 (and (de/n) = −1 if gcd(n, 2ad) = 1) — ET Prop 1.6's mechanism as a per-solution χ = −1 witness; on p = m² + k it is the quadratic residue
   symbol (D(−√−k)/(m + √−k)) of ℚ(√−k) (Prop 1.4).
4. **Positivity propagation (PROVED, Lemma 3.2/Thm 3.3).** Coordinates of any family are positive above the largest
   real root of n; so any integer point above it where n is an odd square kills every family on its class (recovers
   ET/Schinzel for linear n; distinguishes m₀ = 3 from −3 for m² − 8).

## Self-review (R-O221, deep reviewer subagent; repairs applied, marked "R-O221" in NEAR_SQUARE.md)
No FATAL. MAJOR items repaired: Lemma 1.3's de-witness needs gcd(n, 2ad) = 1 (counterexample n = 21) — the witness is
now f; Thm 3.4 restated for unit squares (closure included; coprimality and denominators handled); Conjecture Y10-S
restricted to n(m*) ∈ Ẑ^×; Prop 4.1's "iff" is generic (gcd-exceptional classes are essential: m² + 8, m = 3); Thm 2.2
gained the a ≤ b normalisation (reviewer: all 6 + 10 degree distributions covered, impossibility algebra correct) and a
positivity kill of the Type II (a, c linear) shape; "escape" algebraic vs character-theoretic distinguished; family
counts corrected (80/161/263 candidates, 76/97/111 with computed classes and verified; script now reports skips);
overclaims ("true sterile set", "exactly as well") removed; §5 relabelled descriptive. Lemma 1.1 now unconditional.

## Deliverables vs task
(a) Classification of deterministically clean levels for quadratic families: 4A − tΔ = □ (Prop 4.1, PROVED both
directions); per prime, T1-type = principal-form part of clean (82 % of clean words; 0 χ = −1 among 432 677 clean-level
words, 10⁵–10⁶). Relation to Type I/II: Thm 2.2 / 3.4 (not just the five slices).
(b) Hardness model (EVIDENCE, §5): within adelic cells (p mod 8, (r/p) r ≤ 31, lnr), exact cleanliness explains
N₋/N (corr −0.57), T1-type adds nothing beyond it; but a monotone archimedean gradient in K0 = p − ⌊√p⌋² exists
(−0.05 at K0 < 17 … +0.0035 at K0 ≥ 300; K0 = 24: −0.15), and about half survives removing all clean-level words
(−0.0045 ± 0.0008 even at K0 ∈ [100, 300)) — mechanism unidentified. Hard primes: 3361 = 58² − 3 and
1 249 921 = 1118² − 3 sit next to the T1 point m₀ = 2 (anecdotal). The (J)26 sterile Mordell points were not related
to families (not done).
(c) Explicit polynomial identities on p = m² + k exist (Aurifeuillean Type I, e.g. k = 1, f = m² + 2m + 3, c = 1,
d = 2, m ≡ 2 mod 4) but only where a fixed character of n is −1; the exact obstruction is Z_k^□ (Thm 2.2), non-empty
iff k ≡ 0, 1, 5 (mod 8) (Lemma 2.3). For k < 0 the obstruction is Z_K⁺ ∪ {integer T1 points}.

## Checks
ns_witness_check (1 561 solutions, 0 failures; odd-square control 0); ns_verify_families (99 702 family instances,
0 failures); ns_polyfam for k = 1, 16, 24 (0 escaping, consistent with Thm 2.2). Fingerprints: odd squares (k = 0) are
ET Prop 1.6 = Lemma 1.1 at χ(n) = +1; 105 not used.

## Caveats for the reviewer
* Thm 2.2's shape analysis is by hand (degrees from ET Lemma 2.8); the numerics only cover roots in ½ℤ ∩ [−3, 3]
  (−8: [−8, 8]) and 16 leading coefficients. Please re-derive the Type II deg e = 0 / 1 cases.
* "Polynomial family" is defined in ET-parametrised form; reduction from (x, y, z) ∈ ℚ[m]³ needs Bunyakovsky.
* Thm 3.4 uses the order ℤ[√j]; I restricted to gcd(n, 2j) = 1.
* §5 residuals are within-cell means; no multiple-testing correction; the beyond-clean effect could still be an
  unmodelled adelic effect at primes > 31.

## Sparks (not pursued)
S1. Prove "⊆" of CONJECTURE Y10-S: build, for each m* ∉ Z_K⁺, a family with witness α ∈ K having (α, π_{m*})_v = −1
    at one v (P6 shape with f = j − r² and the Λ > 1 P5 shapes give rational parameter families — moduli grow with the
    denominators of r, ρ). If true, ES for m² − j holds outside any Ẑ-neighbourhood of Z_K⁺.
S2. Identify the beyond-clean archimedean depletion (§5): candidate structure tp + 1 = tm² + (tK + 1) with tK + 1 near
    a square, or levels whose words' A are forced into the principal genus.
S3. Two-variable deformation p = m² + kj² with Pell levels; and p = 2m² + k (tk + 1 = 2□): same dichotomy in sign?
S4. Hard-prime ranking by "K-adic square depth" of m − √j over small |j| (both signs) vs o*, N₋.
S5. For k > 0 the sterile set of non-escaping families may still be smaller than Z_k (it contains (J)26-type sterile
    points only if they are values m² + k): compare with STERILE_EXPLICIT.
