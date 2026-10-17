# R266 — hostile review of O253 (AMPLIFY_EXCEPTION.md, Direction 2: amplifying one exception)

Reviewer: R266 (Claude side agent, branch side-agent/review-amplify-exception). Reviewed state: author branch
side-agent/amplify-exception at b59c8699 (merged into the review branch as 33bce15e).
From-scratch scripts: `scripts/review_r266_*.py` (no author code reused). ES remains OPEN.

**Repairs applied:** the author had been quiet since 18:12 with the report finished, so I applied all repairs below
directly to AMPLIFY_EXCEPTION.md and reviews/agent-reports/AGENT_REPORT_O253.md, each marked "(R266 repair)".

**Overall: no FATAL.** Every mathematical claim I re-derived holds, and every number I recomputed from scratch
matches exactly: E_k for 8 ≤ k ≤ 25, the 37-pair square table, k = 10 / p = 61, all 61 single-source fixture
entries at 97–5209 (incl. 3361 ← 281: 0/17, 11/17 invisible), the 49-prime Mordell list, Thm 3.2 on 35 435
representations, and 121. There are three MAJOR defects, all about presentation and credit rather than
correctness:
(1) D-T32a: the SHARP headline Thm 3.2 is the classical Mordell–Schinzel / ET Prop 1.6 square-class obstruction
(the campaign's T1) and is uncited. Only Cor 3.3's recombination/locality reading is new, and it is folklore-level.
(2) D-ASTRA: Thm 1.3(a), 1.4(d) and the framing of Prop 2.1(a)/Thm 2.2(b) duplicate Astra d7300f8 without credit.
(3) D-R: in places the R1–R8 table states as "iff" what the document proves only one way, and it lists a §5
NOT-SUCCESS progression as the "best law".
On the shared core the result is honestly WEAK-to-STRONG-PARTIAL (d). The Deliverable-1 theorems are sharp and
correct but elementary. The obstruction is correct with an exact scope, but it is classical at its core.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Thm 2.5 (numerator models) | SOUND-AFTER-REPAIRS (numbers all reproduced; population of (b) undisclosed → D-T25a) |
| Thm 2.3 (n = 121) | SOUND (verified) |
| Thm 3.1 (exact gate) | SOUND (near-tautological given the definition; proof detail D-T31) |
| Thm 3.2 (T1 adversary) | SOUND mathematically (minor proof wording D-T32b); **novelty overclaimed → D-T32a (MAJOR)** |
| Cor 3.3 (joint recombination) | SOUND within its stated scope; modest new packaging of a classical fact |
| Fixture / Mordell numerics (§3.1) | SOUND (all spot checks reproduced exactly) |
| Thm 1.1 (counting criterion) | SOUND (the "iff" is relative to an unspecified c₀ and to counting alone; D-R) |
| Rem 1.2 | SOUND |
| Thm 1.3 (a) polylog ceiling | SOUND (= Astra RESET §4 test 3, uncredited: D-ASTRA) |
| Thm 1.3 (b) threshold b ≥ rA | SOUND (sufficiency and model both checked; quantifier of "never suffices" D-NS) |
| Thm 1.3 (c) additive gaps | SOUND for sufficiency; converse is counting-only (stated in doc, oversold in R1: D-R) |
| Thm 1.3 (d) growing branching | SOUND |
| Thm 1.4 | SOUND (weak but correct; 1.4(d) = Astra test 1) |
| Thm 1.5 | SOUND-AFTER-REPAIRS ((c) needs prime blocks: D-T15) |
| Prop 2.1 | (a) SOUND; (b) correctly labelled Assessment |
| Thm 2.2 | SOUND (transport algebra re-derived) |
| Thm 2.4 | SOUND |
| Prop 3.4 | SOUND (patterns and m = 3 reproduced; D-T25b) |
| Prop 3.5 | SOUND (folklore; it is the core's §5 "NOT SUCCESS" category, which R2 should say: D-R) |
| R1–R8 table | SOUND-AFTER-REPAIRS (D-R, D-T32a, D-ASTRA) |

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

**D-R (MAJOR for the comparison — R1–R8 table oversells in places).** Location: AGENT_REPORT_O253.md table.
(i) R1: "F ⊆ E contradicts Vaughan iff ∀c > 0 …" and "one forced successor in (p, p + f(p)] suffices iff
f = e^{o((log p)^{2/3})}": the document itself proves only "if"; the "only if" halves are "no contradiction by
counting against (K4) with an unspecified constant" (Thm 1.1(b), 1.3(c) last sentence), and for (c) no model is
constructed (it would need primes ≡ 1 (840) in intervals of length e^{c(log p)^{2/3}}, far below any known
short-interval result). Repair: "suffices iff (for the converse: relative to Vaughan with unspecified c₀ and
counting alone)"; for (c) "suffices if …; for larger f no counting contradiction (no model)". (ii) R1/R4 "never
suffices" for Thm 1.3(a) should carry the doc's caveat "(when all outputs stay among primes of 𝓜; otherwise Rem 1.2
already gives a contradiction)". (iii) R2(i): Prop 3.5 is a classical fixed-modulus progression (Thm 2.2(a) with
H ≤ X) into the relaxation E_X; under core §5 this is explicitly "NOT SUCCESS (classical Type-I/II congruence
progressions relabelled as propagation)". R2 should say so in one clause, otherwise a side-by-side reader sees a
"total" law. (iv) R4/R6/SHARP: attribution per D-T32a. (v) R7 "every congruence-mediated reduction is blocked by
the T1 adversary" → add "that must accept every supplied source witness (favourable-witness proofs and
size-reading lifts are not covered)". (vi) R5: the core asks for tests on all Mordell-class primes ≤ 10^5; the
recombination gate was run only on the 49 such primes with (p+1)/2 prime — say so explicitly ("other Mordell
primes not tested"). Everything numerical in R5 that I re-ran is exact.

**D-NS (MINOR — quantifier in the definition of "never suffices").** Location: §1 preamble vs Thm 1.3(b). The
preamble defines "never suffices" as: a set E′ satisfying (K1)–(K4′) "consistent with the conclusion of every law
of the given shape". In 1.3(a) the model is E′ = T(p₀) for the *given* law (strong, per-law). In 1.3(b) the model
is an abstract configuration with its *own* edge map: it shows that the shape (b, r, A) does not force a
contradiction, not that a given law σ with these properties has a model (a given σ may have many more successors).
Repair: define both notions ("per-law" vs "shape-level") and label 1.3(b),(d) as shape-level.

**D-T15 (MINOR).** Thm 1.5(c) ("disjoint blocks of bounded length L inside every window (p, p + f(p)] give
Thm 1.3(c) with f + L"): if a hit is composite the chain cannot continue upward (the law is only for primes and
the hit's prime factors are ≤ hit/3, typically far below p). Repair: "blocks consisting of primes (or a law
available at every n ∈ E)", consistent with the caveat already added to 1.5(a).

**D-41 (MINOR — repeats the defect R207 D1 found in (J)41).** Location: end of Thm 2.5 ("a k-uniform argument is
refuted by these finite computations") and R6/R7. Finite computations at p < 2000 (and, for (b), p > 3k) refute
only k-uniform arguments *without a threshold*; an argument valid for p > p₀(k) (p₀(8) > 241, say) is untouched.
Repair: "refutes k-uniform arguments whose validity range includes the tested p (no threshold)", cf. R207 D1.

**D-P35 (MINOR).** Prop 3.5 last sentence "by Thm 3.2 the residues at primes ℓ with (p₀/ℓ) = 1 carry no
information at all" is rhetoric; Thm 3.2 says only that no ET witness of p₀ has modulus supported there.
Repair: replace by that statement or mark Assessment.

## Per-claim notes

### §1 (Thm 1.1–1.5, Rem 1.2) and §2 (Prop 2.1, Thm 2.2–2.4)
Re-derived by hand; numerical parts in `scripts/review_r266_thm13.py` → `logs/review_r266_thm13.txt`.
* Thm 1.1: (a) contradiction at c = c₀; ∀c is needed because c₀ is unspecified; limsup (not lim) suffices since
  (K4) holds for every N. (b) a finite limsup implies a finite sup, so F satisfies (K4)'s inequality with (C₁, c₁).
  (c) partial summation is right; the example F(N) = ⌊N e^{−√(log N)}⌋ is a genuine counting function (derivative
  of N e^{−√L} is e^{−√L}(1 − 1/(2√L)) ∈ (0, 1), so increments ≤ 1), has Σ1/n < ∞ and satisfies (1.1). The "iff" is
  meaningful only as stated in (b): relative to an unspecified c₀ and to counting alone (an explicit c₀ would make
  every F with c₁ < c₀ contradictory). Fine in the document, oversold in R1 (D-R).
* Rem 1.2: all four landing criteria correct (n < p₀ is applied at p₀ = min E, which is prime by (K3)).
* Thm 1.3(a): generation-k elements ≥ p₀^{μ^k}; the union bound needs no distinctness. (d): every q ≤ N, q ≠ p₀,
  has a parent ≤ N^{1/μ} with ≤ N^{δ/μ} children; unrolling gives ≤ K + 2 terms each ≤ N^{δΣμ^{−j}} = N^{δ/(μ−1)}.
  Correct. (b) sufficiency: |T_{k+1}| ≥ (b/r)|T_k| (edges from T_k ≥ b|T_k|, in-degree ≤ r); for b/r ≥ A, T(N) ≥
  N/(A p₀), positive lower density, contradicting E(N) = o(N). Model: children of a level-k parent lie in
  [X_{k+1}, (1+δ)X_{k+1}] ⊆ (p, Ap] because A > (1+δ)²; cyclic slot assignment gives distinct children (m_{k+1} ≥ b)
  and in-degree ≤ ⌈b m_k/m_{k+1}⌉ ≤ r. I built the model from scratch for (b, r, A) = (3, 1, 4), (5, 2, 3), (2, 3, 2)
  with primes ≡ 1 (840) near 10^6–10^{10}: out-degree exactly b and window (p, Ap] at every parent, max in-degree
  1, 2, 2 (≤ r), level sizes as predicted. The "iff b ≥ rA" is a genuine shape-level threshold (D-NS).
  (c): chain bound p_i ≤ p₀ + i f(N) gives ≥ (N − p₀)/f(N) chain elements; the ∀c liminf condition is equivalent
  (diagonal argument) to "log f(N) = o((log N)^{2/3}) along one sequence", as R1 states. Converse counting-only.
* Thm 1.4: (b) R(N) ≤ (1 + log₂ N)^s is right; it is very weak (Astra's Rankin semigroup bound, RESET §4 test 2,
  is the relevant complement: the whole semigroup generated by a sparse prime set is still sparse, so composites
  never add counting power beyond Thm 1.1 applied to E itself). "Sharp: R = {p₀^k}" is a statement about the
  combinatorial inequality only (p₀^k ∈ E is not known) — harmless, but say so.
* Thm 1.5(a),(b): correct (route D = least-element argument). (c): D-T15.
* Prop 2.1(a): contrapositive, correct; (b) properly an Assessment (Vaughan's method cited from memory).
* Thm 2.2(a): Type II H | q−p ⇒ H | p + e; Type I ⇒ H | pe + 1; switched: p(qe + 1) ≡ p + e and p(q + e) ≡ 1 + pe
  (mod H) — all verified; isolation of exceptional primes is immediate (W(p) = ∅). (b) tautology argument correct.
* Thm 2.4: p ≡ 9 (16) ⇒ (p−1)/2 ≡ 4 (8) even, (p+1)/2 ≡ 5 (8) ∉ 𝓜; I re-checked that every n ≡ 5 (8) has the
  polynomial solution 4/n = 1/((n+3)/4) + 1/(n(n+3)/8) + 1/(n(n+3)/4), so (K2)'s "all integers" reading is right here.
  (b) the sieve dimension 2·6/192 = 1/16 is right; correctly flagged heuristic.
* Prop 3.4: (a) the valuation case analysis is complete (one zero valuation: (≥2,0,0) = ET Type I, (≥2,≥2,0) =
  Type II, (≥2,1,0) mixed; no zero: p·W(p)); from scratch for 3 ≤ p < 80 only (2,1,0), (2,1,1), (2,2,1) occur and
  (2,1,0) occurs for every p. (b) identity re-derived: 1/u + 1/v = m(A + pB′)/((A + pB′) z p²) = m/(p²z) = 4/p² − 1/z.
  (c) re-derived (p² + 3 ≡ 4 (8), all odd prime divisors ≡ 1 (3)); from scratch: no p ≡ 1 (3), p < 3000, has divisors
  A, B′ of (p²+3)/4 with 3 | A + pB′.

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
