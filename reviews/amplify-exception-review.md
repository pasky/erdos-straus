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

**D-T32a (MAJOR — attribution / overclaimed novelty of the SHARP headline).** Location: AMPLIFY_EXCEPTION.md
Thm 3.2, Cor 3.3; AGENT_REPORT_O253 SHARP 1, R4, R6. Thm 3.2 ("p ≡ □ (mod L) ⟹ no ET witness with H | L") is the
classical Mordell–Schinzel obstruction in local form: a witness slice with H | L is exactly a polynomial ES
identity on the class p mod L, and ET p. 8 state that "a primitive congruence class n = r mod q which is a
perfect square cannot be solved by polynomials (this also follows from Proposition 1.6)" (refs [44], [68] there =
Mordell, Schinzel); ET p. 6 adds that this "rules out … a finite set of covering congruence strategies". In the
campaign this is literally named T1 and is DISCOVERIES (C)2 and (C)7 ("known in substance: Mordell 1969 /
Schinzel 2000"). The document cites neither Schinzel/Mordell, nor ET's remark, nor (C)2/(C)7; the report presents
"T1 adversary / invisible witnesses" as the main new sharp result. What is new is only the *packaging*: (i) the
reading "a source witness informs a congruence-mediated lift only through p mod αH′" (Thm 3.1, near-tautological
from its definition), and (ii) the locality remark that an lcm of invisible moduli is invisible (Cor 3.3), so joint
recombination cannot rescue invisible inputs. Both are correct and useful for the shared-core comparison, but
modest. Repair: in Thm 3.2 add "(classical: Mordell–Schinzel via ET Prop 1.6 and ET p. 8; campaign T1, DISCOVERIES
(C)2/(C)7; the CRT normalisation is the only detail added here)"; relabel the novelty of Cor 3.3 as
"application of T1 to recombination laws; folklore-level"; in SHARP 1 and R4 replace "T1 adversary" as a
headline by "application of the classical square-class obstruction (Mordell–Schinzel/ET Prop 1.6) to route (D):
joint determined recombination cannot use square-class inputs".

**D-ASTRA (MAJOR for the side-by-side comparison — missing credit to Astra prior art at d7300f8).** Location:
§1–§2 of AMPLIFY_EXCEPTION.md (no mention of Astra anywhere). Overlaps I verified:
* POSITIVE_ES_RESEARCH_RESET.md §4, test 3: "fixed branching number b with every successor at least n^{1+ε}
generates only O((log N)^{log b/log(1+ε)}) descendants" = Thm 1.3(a) (the polylog ceiling); test 1 ("ordinary
multiples fail … products cannot simply be declared exceptional") = Thm 1.4(d); test 2 (the multiplicative
semigroup of a set with P(x) ≪ x exp(−c(log x)^θ) still satisfies such a bound with c/2) is a sharper form of the
point of Thm 1.4(b)/(c) (composites built from exceptional primes cannot by themselves contradict the bound); its
"sharper first target" Σ_{P_E} 1/p = ∞ is the target Thm 1.1(c) improves on.
* EXCEPTION_PROPAGATION_GLOBAL.md §1 ("exact all-witness sufficient hypothesis: for every normalized w ∈ W(q),
H(w) | q − p or H(w) | pq − 1") and §8 ("(14) all-input recombination … If even one such factor is known soluble
(or is < p under minimality), that lift proves W(p) nonempty directly") = Thm 2.2(b) and Prop 2.1(a)/Thm 2.4's
framing; §3 ("explicit moving-witness escape in every reduced neighborhood") is the Astra analogue of Prop 3.5's
obstruction and of the adversarial-witness idea (Astra escapes via a non-residue modulus ℓ ≡ 3 (4), O253 via square
classes — different mechanism, same role).
* EXCEPTION_PROPAGATION_OPERATIONS.md §5–§6: target-dependent positive recombination repairs every witness at
97 and (with M = 5) the 157 → 313 obstruction; Astra itself shows unrestricted refinement is equivalent to ES(p).
These are *not* determined lifts (they use known targets at p), so they do not contradict Cor 3.3, but the document
should say so, since "no source is total at any fixture" could otherwise be read as contradicting Astra's "repairs
every witness at 97".
Repair: add a short "Prior art" paragraph: Thm 1.3(a), 1.4(d) = Astra RESET §4 tests 3, 1 (credit); Thm 2.2(b)/
Prop 2.1(a) framing = Astra GLOBAL §1, §8; Thm 3.2 = Mordell–Schinzel/ET (D-T32a); and the remark that Astra's
positive repairs at 97/313 are target-dependent, hence outside the determined-lift scope.

**D-T25a (MINOR).** Thm 2.5(b): the populations are p > 3k (script `z25_models.py`), undisclosed. Without that
restriction the {(p∓1)/2} law also fails at k = 9 (p = 19), so "except 9" is false as stated; the truncated law also
fails for k = 8, 9 (vacuously, e.g. k = 8, p = 17). Repair: state "tested on exceptional p > 3k" or replace
"fails for every k ∈ [10, 25]" / "except 9" by "fails for every k ∈ [8, 25] (for k = 8, 9 only at p ≤ 3k, e.g.
(9, 19))".

**D-T25b (MINOR).** Prop 3.4(d): "likewise for all exceptions p < 400 of 8 ≤ k ≤ 14 except (14, 29)" omits the
exceptions (11, 2), (13, 2), (14, 2) listed in Thm 2.5(a). Repair: "except (11, 2), (13, 2), (14, 2), (14, 29)".

**D-T31 (MINOR).** Thm 3.1(a) proof: existence of t with gcd(t, 4ab) = 1 and p′ + tαH′ prime needs the residue
choice at odd ℓ | 4ab, ℓ ∤ αH′ (avoid t ≡ 0 and p′ + tαH′ ≡ 0; possible since ℓ ≥ 3), then Dirichlet. One line.

**D-T32b (MINOR).** Thm 3.2: statement says "Let p be odd" but the proof uses primality ("since p is prime the
witness is ET-normalised"); say "odd prime (or: odd p and an ET-normalised witness)". In the proof, "for ℓ | L this
is automatic, since m² ≡ p ≢ 0 (mod ℓ)" is false for ℓ = p when p | L (then p ‖ L and p | m); the conclusion
still holds because of the recorded facts p ∤ ab, p ∤ e (II), p ∤ c (I). Repair: "for ℓ | L, ℓ ≠ p, this is
automatic; for ℓ = p use p ∤ abe (II) resp. p ∤ abc (I)", or first replace L by its prime-to-p part (H is
coprime to p).

(further defects below)

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
