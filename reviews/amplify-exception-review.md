# R266 — hostile review of O253 (AMPLIFY_EXCEPTION.md, Direction 2: amplifying one exception)

Reviewer: R266 (Claude side agent, branch side-agent/review-amplify-exception). Reviewed state: author branch
side-agent/amplify-exception at b59c8699 (merged into the review branch as 33bce15e).
From-scratch scripts: `scripts/review_r266_*.py` (no author code reused). ES remains OPEN.

## Summary verdicts (filled in progressively)

| Claim | Verdict |
|---|---|
| Thm 2.5 (numerator models) | SOUND-AFTER-REPAIRS (numbers all reproduced; population of (b) undisclosed → D-T25a) |
| Thm 2.3 (n = 121) | SOUND (verified) |
| Thm 3.1 (exact gate) | SOUND (near-tautological given the definition; proof detail D-T31) |
| Thm 3.2 (T1 adversary) | SOUND mathematically (minor proof wording D-T32b); **novelty overclaimed → D-T32a (MAJOR)** |
| Cor 3.3 (joint recombination) | SOUND within its stated scope; modest new packaging of a classical fact |
| Fixture / Mordell numerics (§3.1) | SOUND (all spot checks reproduced exactly) |
| (in progress) | |

## Defects

(in progress)

## Per-claim notes

### Thm 3.1, Thm 3.2, Cor 3.3, §3.1 numerics
From scratch: `scripts/review_r266_t1.py` (own witness/representation enumeration on top of the complete
search of `review_r266_ek.py`; local squareness test cross-checked against brute force for all odd primes
p < 200 and L < 400, 0 mismatches). Logs `logs/review_r266_{thm32,gate,fixtures}.txt`.
* **Thm 3.2 re-proved.** For an ET witness (a,b,c,d) of the prime p with H = 4ab | L and m² ≡ p (mod L): Type II
  d′ = (n + e)/H, (abd′, nacd′, nbcd′) solves 4/n since 1/(abd′) + e/(nabd′) = (n + e)/(nabd′) = 4/n; Type I
  d′ = (ne + 1)/H, (nabd′, acd′, bcd′) solves 4/n. Normalisation: every prime ℓ | ab divides L and ℓ ≠ p, so
  ℓ ∤ m; ℓ | n ∩ d′ forces ℓ | e (II), impossible in Type I since Hd′ ≡ 1 (mod n); ℓ | c, e with ℓ ∤ L is
  excluded by the CRT choice of m. I agree with the proof, including the case p | L (then p ‖ L, p | m, and the
  facts p ∤ e (II), p ∤ c (I) recorded in the proof are exactly what is needed — but see D-T32b for the wording).
  The proof works verbatim for odd composite p if "witness" means ET-normalised solution.
* Numerically: every ET representation of every prime 5 ≤ p < 3000 (35 435 representations) has p a non-square
  mod H — 0 violations. Odd squares m², 3 ≤ m ≤ 41: complete W(m²) enumerated, 0 ET Type I/II solutions (ET
  definition: n | x, gcd(n, yz) = 1, resp. n | y, z, gcd(n, x) = 1).
* Thm 2.3: (121² − 1)/4 = 3660 = 2²·3·5·61, 121 ≡ 121 (mod 840), W(121) has 24 solutions, none ET Type I/II. Verified.
* The p = 1201 caveat (17·71 − 6, H = 68, Type I (1,17,6,53): 68·53 = 3604 = 3·1201 + 1, 1201 ≡ 11 is a
  non-residue mod 17): verified by hand.
* **Thm 3.1** (a) checked: the "only if" needs two primes p′, p′ + tαH′ with gcd(t, 4ab) = 1; such t exist by
  Dirichlet after choosing t mod each odd ℓ | 4ab, ℓ ∤ αH′, outside the two residues 0 and −p′/(αH′) (ℓ ≥ 3), and
  2 | αH′ always. The document asserts this without the residue argument (D-T31, MINOR). Given its definition
  ("a rule whose output slice is valid on the whole class p mod αH′"), Thm 3.1 is essentially a restatement; that is
  fine but it should not be sold as more.
* **Cor 3.3**: locality checked: for odd prime p, p ≡ □ (mod ℓ^v) depends only on (p/ℓ) for odd ℓ ≠ p, on
  p mod 2^{min(v,3)} for ℓ = 2, and needs v ≤ 1 for ℓ = p; v_ℓ(lcm) = max_i v_ℓ(L_i) is attained at some i, so the
  lcm of invisible moduli is invisible. The adversary argument (each source supplies an invisible witness) is
  correct. Scope: "determined lift" = the output slice is valid on the whole residue class of p modulo the
  joint modulus; this is precisely defined (Thm 3.1) and neither vacuous nor overbroad. It does NOT cover lifts
  that read sizes (d, x, y, z) or that are allowed to fail on other members of the class — the document says so.
* Fixtures: **every** single-source entry of the fixture table for 97, 193, 313, 3361, 5209 reproduced exactly
  (61 entries; incl. 3361 ← 281 (×12): 0/17, 11/17 invisible; 97 ← 43 (×2): 3/14, 11/14 invisible; 313 ← 13
  (×24): 1/4). No source is total at any of these; minimum number of invisible witnesses per source = 2, 2, 3, 8,
  16 (so (ii) holds and (iii) follows from (ii) by Cor 3.3; the DFS in (iii) is redundant). Mordell list: 49 primes
  p < 10^5, p ∈ 𝓜, (p+1)/2 prime — reproduced; gate counts reproduced at 1201 (2/16), 4561 (14/27), 8521
  (25/69), 9241 (21/40). 233689 not rerun (not needed; values are of the same nature).
* Minor counting convention: a witness with several (a,b,c,d) representations is "passing" in the single-source
  table if one representation passes, but in the joint search its information is the lcm of all its
  representations' moduli. I checked both conventions: identical pass counts at all fixtures; invisible counts
  differ only at 3361 ← 3359 (276 vs 274) and 9241 ← 4621 (11 vs 9). No effect on any claim.

### Thm 2.5 (numerator models) — SOUND-AFTER-REPAIRS
From scratch: `scripts/review_r266_ek.py` (complete search: x ∈ (n/k, 3n/k], then the two-term equation
A/B = 1/y + 1/z solved via (Ay − B)(Az − B) = B²; cross-checked against a naive y-loop for all 4 ≤ k ≤ 13,
2 ≤ n < 120: 0 mismatches). Logs `logs/review_r266_ek.txt`, `logs/review_r266_laws.txt`.
* E_8 ∩ primes < 2000 = {2, 3, 11, 17, 131, 241}: **reproduced**. k = 12: 16 primes, largest 1873: **reproduced**
  ({2,3,5,7,13,29,31,37,73,97,193,433,577,1129,1657,1873}). All 18 counts/maxima for 8 ≤ k ≤ 25 agree with
  `logs/z25_models.txt`.
* (a) square-law table: my list of (k, p) with p ∈ E_k, p < 400, p² ∈ E_k is **identical** to the 37 pairs printed.
  8/121 = 1/18 + 1/99 + 1/2178 verified; 8/11 has no solution.
* (b) k = 10, p = 61: 930 = 2·3·5·31, 10/31 soluble, 10/61 not — **reproduced**. k = 8, p = 131: 8/65, 8/66
  soluble, 8/131 not — reproduced. BUT the author's script tests (b) only on p > 3k (`z25_models.py` line
  `p > 3 * k`), which the document does not say. Without that restriction the {(p∓1)/2} law also fails at
  k = 9 (p = 19: 9/9 and 9/10 soluble, 9/19 not), so "except 9" is an artefact; and the truncated law also fails
  at k = 8, 9 (e.g. k = 8, p = 17: (17²−1)/4 = 72 has no prime factor > 8, hypothesis vacuous; k = 9, p = 19).
  → D-T25a (MINOR).
* (c) no element of E_8 in (241, 1928]: reproduced.
* Prop 3.4(d) says the k-model square law fails "for all exceptions p < 400 of 8 ≤ k ≤ 14 except (14, 29)";
  the table of 2.5(a) (and my run) also has (11, 2), (13, 2), (14, 2) → D-T25b (MINOR).
