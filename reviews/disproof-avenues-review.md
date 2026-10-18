# R274 — hostile review of O262 (DISPROOF_AVENUES.md, BRAINSTORM/z32_*, scripts/logs z32_*)

Reviewer branch `side-agent/review-disproof`; author files merged from `side-agent/disproof-avenues`.
From-scratch scripts: `scripts/review_r274_*`. Labels as in DISCOVERIES.md. ES is not solved; nothing below changes that.

(Work in progress — verdict table filled claim by claim.)

## Verdict table

| # | claim | verdict |
|---|---|---|
| 1 | §1–2 citations (BL Thms 1.6/1.8/1.9, Rem 1.10; Markoff; Lyczak; Mihnea–Dumitru 10¹⁸; PW) | SOUND-AFTER-REPAIRS (D1, D2, D3) |
| 2 | Prop 3.1 (n = 1 shadow) | SOUND-AFTER-REPAIRS (statement true; proof has two small gaps D4, D5; existence clause D6; attribution D7) |
| 3 | §4.1–4.3 ladder counts, zero law, crossover law | data SOUND (reproduced exactly from scratch); fit SOUND; out-of-sample wording GAP (D12: systematic under-prediction ×3–5 at the top μ, the extrapolation direction); crossover SOUND as EVIDENCE (D13 minor) |
| 4 | §4.4 expected-failure numbers | GAP (numbers reproduce, but "every variant" bounds contradict the author's own log: D8; "worst case" is not one: D10) |
| 5 | §4.5 heavy tails self-refuting | GAP (correct inside the one-parameter family only; the "only escape is non-monotone" conclusion is false: D9) |
| 6 | §5 adversarial search, hardest prime | SOUND (numbers reproduce exactly; one MINOR in Reading 5: D11) |
| 7 | labels, P(ES false) < 10⁻³ | pending |

## Claim 1 — citations (§§1–2)

Checked against `sources/bright-loughran-1908.02526.pdf` (full text extracted), `sources/pw.txt`, and arXiv abstract
pages fetched 2026-10-18 (1807.10223 Loughran–Mitankin, 1808.01584 CT–Wei–Xu, 2202.07142 Dao, 2005.14013 Lyczak /
AIF 10.5802/aif.3529, 2509.00128 Mihnea–Dumitru). Full texts of the Markoff papers were NOT accessed (abstracts only).

* BL Thm 1.6 (Br U_n/Br ℚ ≅ ℤ/2, transcendental (−u₁/u₃, −u₂/u₃)): quoted correctly.
* BL Thm 1.8 (1.4), (1.5): quoted verbatim ("For all n ∈ ℕ"). But see D1: the proof (BL §3.8) uses "some prime
  p | n" with surjective local invariant (Lemmas 3.6, 3.7), so it needs n ≥ 2 (Thm 1.1 says n ≥ 2). At n = 1 the
  statement is false: by BL Lemma 3.1/3.5/3.8 the invariant is −1 at ∞ on U₁(ℝ)₊ and +1 at every finite place, so
  (U₁(ℝ)₊ × ∏ U₁(ℤ_p))^{Br} = ∅. n = 1 is BM-obstructed (Thm 1.2 with the empty product).
* BL Thm 1.9 and its proof (non-Zariski-density via (3.6) + Lang–Weil + [6, Lem 6.5]): quoted correctly.
* BL Rem 1.10: quoted correctly, but BL only says "versions of Theorems 1.5, 1.8, and 1.9 also hold" with no
  hypotheses stated (D2).
* PW Table 1 (`sources/pw.txt` l. 840–896): m = 8 exceptions 1, 2, 3, 11, 17, 131, 241 (N = 10¹³); m = 15: 32
  exceptions up to 20 521 (N = 10¹²), including n = 1…5, 8, 16, 34, 122, 226 (composites). Quoted correctly.
  PW §6: m = 5 to 10¹⁸, m = 6, 7, 8 to 10¹³: correct. PW Thm 1.1 (exception n > exp(m^{1/3−ε}) for m ≥ m(ε)) and
  Thm 1.2 (prime in (m², 2m²) for m ≥ 6.52·10⁹): quoted correctly in memo z32_numerator_ladder.
* Mihnea–Dumitru arXiv:2509.00128 exists (Aug 2025), abstract: "improving computational bounds to 10^{18}"; PW §6
  cites it as the record. It is an unrefereed preprint (D3).
* CT–Wei–Xu abstract: strong approximation fails away from any finite set of places; "for m ≠ 0, 4 the Brauer group
  does not control strong approximation". Dao abstract: "counterexamples to the integral Hasse principle which cannot
  be explained by the (algebraic) Brauer–Manin obstruction". Loughran–Mitankin abstract does not itself state the
  "infinitely many non-BM failures" claim; I could not access the body (it is the commonly cited content of LM Thm 1.4 —
  unverified here). Lyczak: AIF 2023, order-5 BM obstructions to integral HP on log K3 surfaces: correct.

## Claim 2 — Prop 3.1 (n = 1 shadow principle)

*Row table re-derived by hand and symbolically* (`scripts/review_r274_shadow.py`, `sym_checks`; all residues 0 modulo
the ET equation): II{c,d} (4cda−1)(4cdb−1) = 4c²dp + 1; **II{a,d}** (4acd−1)(4abd−p) = p + 4a²d; **I{c,d}**
(4cda−p)(4cdb−p) = p² + 4c²d; II{a,c} b(4acd−1) = cp + a; I{a,c} b(4acd−p) = ap + c; **I{a,b}** c(4abd−1) = p(a+b);
I{a,d} (4acd−p)(4abd−1) = p(4a²d+1). The row conditions follow (for I{a,b}: the divisor 4abd − 1 ≡ −1 (mod 4ab) of
p(a+b) is g or pg with g | a+b; the case g is impossible by size, so the row's "pg ≡ −1" is the only one; for I{a,d}
the case p | c gives a second shape f ≡ −1 dividing 4a²d+1, also killed by the size check — the table omits it but
the proof's case list covers it).

*Numerical check from scratch.* Slice counts by direct search in the ET equations (fix two variables, loop a third
over a rigorous range, solve the fourth, verify exactly; cross-checked against a second loop order for all primes
< 300, 0 mismatches). For 19 test sets Θ (each row type incl. II{a,d} (1,1), (2,1), (1,3), (3,2); I{c,d} (1,1),
(1,2), (2,1); I{a,b} (1,1), (1,2), (2,3), (3,5); II{a,c}, II{c,d}, II{a,b}, I{a,c}, I{a,d}; II e = 7 and I e = 11
with the *literal* Q = q·N(1); a 5-slice combination), the first 2–4 primes satisfying the hypotheses with Q = lcm
q_θN_θ(1) all give **0 in every slice**; controls in the same class with a composite cofactor give up to 12
(`logs/review_r274_shadow.txt`). The author's three primes near 2·10¹² are ≡ 1 (mod 9240) with all eight distinct
cofactors prime (checked). Note the controls for I{c,d} were all 0 anyway (thin slice), so the I{c,d} tests are
weak evidence; the proof is what carries that row.

*Proof check.* The core ("p ≡ 1 (mod q_θN_θ(1)) ⟹ P_θ ≡ 1 (mod q_θ) ⟹ every divisor of N_θ(p) is ≡ a divisor of
N_θ(1) and every class condition is the p = 1 one; at p = 1 a size check kills it") is correct for every row. The
size checks: (4ad−1)² − (4a²d+1) = 4ad(4ad − a − 2) > 0 ✓; a + c < 4ac − 1 ✓; (e+5)/4 < e ✓.

*R272-D1 pitfall.* Prop 3.1's existence clause imposes only p ≡ 1 (mod Q) and primality of linear/quadratic
forms — no Frobenius/abelian condition at primes outside Q — so the ℚ(ζ₇)-type counterexample of R272 D1 cannot
occur: Dickson/H is applied with Ω = ℚ, where the R272-corrected HC reduces to plain Dickson. SOUND on this point.

## Defects

**D1 (MINOR→MAJOR for the "Reading", §1 bullet "BL Thm 1.8 (1.4)", §1 Reading 1, §3 Prop 3.1 Reading, §6 last
paragraph).** BL Thm 1.8 holds for n ≥ 2 only; for n = 1 there IS a Brauer–Manin obstruction (all finite
invariants trivial — Lemma 3.5 for odd p ∤ n, Lemma 3.8 at 2 — and inv_∞ = −1 on U(ℝ)₊). Consequences: (i) "no BM
obstruction to ES at any n" must read "at any n ≥ 2" (harmless for ES). (ii) The Prop 3.1 Reading calls n = 1 "the
**archimedean** exceptional point", contrasting it with n = m²; in BL's language both are *Brauer–Manin* points:
n = 1 is the n for which the real invariant −1 cannot be compensated because no prime divides n, and n = m² is
Cor 1.4 (derived from Thm 1.2). So §6's "find a third exceptional point of Ẑ × ℝ" programme should say that both
known exceptional points are BM-obstructed specialisations, and that a prime p can never be BM-obstructed (Thm 1.8,
n = p ≥ 2) — which sharpens, not weakens, the author's conclusion: a "prime T1" would have to be a non-BM
mechanism, unlike both known templates. *Repair:* replace "for every n ∈ ℕ" by "for every n ≥ 2 (BL Thm 1.1; at
n = 1 the Br-set is empty)"; replace "archimedean exceptional point" by "the BM-obstructed point n = 1 (empty
product in Thm 1.2)"; add one sentence to §6.

**D2 (MINOR, §1 Reading 2).** "8/n … 15/n failures with no BM obstruction (Rem 1.10 version of Thm 1.8)" overstates
what BL say: Rem 1.10 gives no hypotheses, and by D1 the m = 4 version already fails at n = 1; small exceptional n
such as 15/n with n = 1, 2, 3, 4, 5 (n ≤ m/3 region) are plausibly BM/real-obstructed. For n = 11, 17, 131, 241
(m = 8) the claim is plausible (prime n, n ∤ m) but not proved in BL. *Repair:* label as Assessment ("presumably not
BM-explained; BL Rem 1.10 states versions of Thm 1.8 without proof") and restrict to the prime exceptions n > m.

**D3 (MINOR, §2 bullet "Verification record", §4.5, §6 table).** "ES holds for all n ≤ 10¹⁸" rests on an
unrefereed arXiv preprint (PW cite it). §4.5's whole self-refutation argument is conditioned on it. *Repair:* say
"reported (Mihnea–Dumitru, arXiv preprint 2025; cited by PW §6)", and note that §4.5 also works with the refereed
Salez 10¹⁷ bound: within the §4.5 family the maximal Poisson-conditioned expectation beyond the verified range is
2·10⁻¹⁰ (10¹⁸) resp. 3·10⁻⁹ (10¹⁷) — `logs/review_r274_extrap.txt` — so nothing hinges on the preprint.

**D4 (MINOR, §3 Prop 3.1 proof, "P_θ > N_θ(1), so the divisors of N_θ(p) are δ and δP_θ").** P_θ > N_θ(1) does
not follow from the hypotheses. Counterexample: θ = II{a,d} = (1,3), Q = q·N(1) = 12·13 = 156, p = 157 (prime,
≡ 1 mod 156): N(p) = 169, N(1) = 13, P = 13 = N(1) (prime). The conclusion still holds (slice empty, checked), because
P ≡ 1 (mod q) implies every divisor P^i m of N(1)·P is ≡ its P-free part m, and the P-free parts of a
complementary pair multiply to M | N(1) with M ≡ N(1) (mod q), so the same size checks apply. *Repair:* replace the
sentence by "every divisor of N_θ(p) = N_θ(1)·P_θ is ≡ (mod q_θ) to a divisor of N_θ(1), and complementary pairs map
to pairs (m, m′) with mm′ | N_θ(1)" (or assume p > N_θ(1)²·Q, which forces P_θ > N_θ(1)).

**D5 (MINOR, §3 Prop 3.1 proof, "N_θ(p) − N_θ(1) is a multiple of p − 1 (it is α(p − 1) or p² − 1)").** False for
the e-slices: (p+e)/4 − (1+e)/4 = (p − 1)/4 and (pe+1)/4 − (e+1)/4 = e(p − 1)/4; also, with only e·N(1) | Q (literal
hypothesis) one does not get N(1) | N(p). The *statement* survives because "P_θ is prime" includes integrality:
from (p+e) = (e+1)P resp. pe + 1 = (e+1)P and p ≡ 1 (mod e) one gets P ≡ 1 (mod e) directly (tested: II e = 7 with
Q = 14, I e = 11 with Q = 33, all 0). *Repair:* add one line for the e-rows: "(p+e) = (1+e)P_θ (resp.
pe + 1 = (1+e)P_θ) and p ≡ 1 (mod e) give P_θ ≡ 1 (mod e)".

**D6 (MINOR, §3 Prop 3.1 existence clause).** (i) For e-slices the cofactor form t ↦ P_θ(1 + Qt) = 1 + Qt/(1+e)
(Type II) resp. 1 + eQt/(1+e) (Type I) has integer coefficients only if (1 + e) | Q; with the stated
q_θN_θ(1) = e(1+e)/4 | Q it may not (e = 7, Q = 14). Require e(1+e) | Q for e-slices (or substitute t → 4t).
(ii) "adding to Q every prime ≤ |Θ| + 1 makes the tuple admissible" is unnecessary: all forms equal 1 at t = 0, so
no prime divides the product for every t. Harmless. (iii) The H-case (I{c,d}) is fine: the cofactor form is (Q²t² + 2Qt + N(1))/N(1), discriminant
4Q²(1 − N(1)) < 0, so it is irreducible over ℚ, and all forms equal 1 at t = 0 (no fixed prime divisor).

**D7 (MINOR, attribution, §3 "Reading": "unifies (J)83 Thm 1.3, (J)90 Thm 4.2, redteam L1.2.1, B1_LINE Prop 4.1;
novelty only in the uniform, row-by-row form").** The closest precedents are not cited: CLASS_FORCING Thm 3.4 ("the
forced rule never fires at the point n = 1", unconditional, b = 1 lines and all e-slices ≤ D, with the same
p ↦ 1 shadow and the same size checks) and Thm 6.1 (R272-repaired; Ω = ℚ is exactly Dickson; prime B-rough cofactors
⟹ no certificate on any e-slice ≤ D), JOINT_BUDGET Prop 4.3, and redteam-automorphic-2 Thm 2.2(iii) ("any finite
set Θ₀ of slice parameters, of any types and rows, fails i.o. under H" — i.e. the *uniform* statement already exists,
under H). What Prop 3.1 adds is (a) the explicit pair rows II{a,d}, II{c,d}, II{a,c}, I{a,c}, I{c,d} and the
congruence rows in the n = 1-shadow form, and (b) Dickson instead of H when no I{c,d} slice is present. *Repair:*
cite these and restate novelty as (a)+(b). Also note that the congruence rows (II{a,b}, I{a,b}, I{a,d}) are killed
by p ≡ 1 (mod q_θ) alone, unconditionally (verified) — worth saying, since it is the only unconditional part.

## Claims 4–5 — §4.4 expected failures, §4.5 heavy tails (`scripts/review_r274_extrap.py`, `logs/review_r274_extrap.txt`)

Independent integration E#[A,B) = ∫ exp(L − a(cL^k)^β) dL/L (prime density 1/L), mpmath in log space.
* §4.5 table reproduces: c = 0.074: β = 0.91 → 3.7·10⁻⁵⁷ below, ≈ 10⁻⁵⁵² beyond (author "0"); β = 0.55 → 1.65 /
  2.2·10⁻¹⁰; β = 0.5 → 493 / 0.71; β = 0.45 → 1.35·10⁶ / 6.5·10⁷; c = 0.037, β = 0.55 → 860 / 0.074. ✓
* Break-even β* 0.528 / 0.594 and q_crit = 11.6/41.45³ = 1.63·10⁻⁴ ✓; q_m ∝ m^{−1.9} (q₄/q₂₄ = 28.5, m ratio 6 →
  exponent 1.87) ✓; m ≈ 60 for q = 1.6·10⁻⁴ ✓.
* §4.4 with ALL primes at the hardest-cell ratio c = 0.037 (pessimistic, my own model): [10⁸, 10¹⁸): 6·10⁻²⁸ (L³),
  10⁻²⁷ (L²), 7·10⁻¹⁸ / 1.1·10⁻¹⁷ (a − 30 %), 5·10⁻⁸ / 9·10⁻⁸ (a = 0.4, β = 0.8). The author's cell-weighted values
  (1.8·10⁻³¹ etc.) are ≈ 1/(#cells) of these — consistent. Worst case μ = 0.0117·L³ = 833 at 10¹⁸, −ln P = 243 ✓.

**D8 (MAJOR, overclaim; §4.4 bullet "Beyond 10¹⁸: < 10⁻⁸⁸ in every variant", §6 table row "lottery failure": "≤ 10⁻²⁰
in every variant, beyond 10¹⁸ < 10⁻⁸⁸", AGENT_REPORT (1d)).** The author's own `logs/z32_extrapolate.txt` contains a
"flatter" variant (a = 0.40, β = 0.80) giving E#[10⁸, 10¹⁸) = 2.4·10⁻¹⁰ / 5.8·10⁻¹⁰ and E#[10¹⁸, ∞) = 7.5·10⁻⁸⁴ /
**5·10⁻³⁷** (μ ∝ L³ / L²); my uniform-c recomputation gives 2·10⁻³⁴ for the latter. The quoted "every variant" bounds
silently drop it. β = 0.8 is not exotic: the author's training windows give β = 0.91–0.93, and the extrapolation is
from μ ≤ 50 to μ ≥ 229 (§4.5 caveat). *Repair:* report the range honestly: "[10⁸, 10¹⁸): 10⁻³¹ (fit) … 10⁻⁹ (β = 0.8,
a = 0.4); beyond 10¹⁸: 10⁻²⁹⁶ … 10⁻³⁶", and drop "every variant"; same in §6 and AGENT_REPORT. Also §6's "< 10⁻⁸⁰"
("Probability that ES is false … astronomically small (< 10⁻⁸⁰)") must become "< 10⁻³⁰ within the variants tried".

**D9 (MAJOR, logic; §4.5 "The only escape is a zero law that is *non-monotone* in L"; "conditioning on none ≤ 10¹⁸,
the expected number beyond is ≲ 10⁻² for every β"; AGENT_REPORT SHARP 2).** The self-refutation is a property of the
one-parameter family exp(−0.535(cL³)^β), whose per-prime probability falls super-polynomially in L for every β ≥ 0.4
tested; within it I confirm (max over β ∈ [0.40, 0.70], c ∈ {0.037, 0.074} of P(none ≤ 10¹⁸)·E#beyond = 2·10⁻¹⁰).
But monotone laws outside the family escape: (i) a floor/mixture P(f = 0) = max(exp(−aμ^β), ε) — e.g. a "conspiracy
class" of relative density ε — with ε = 10⁻¹⁸ gives 0.025 expected failures ≤ 10¹⁸ and 7·10³⁹ in [10¹⁸, 10⁶⁰);
(ii) a polynomial law P = C/p gives expected counts ∝ log log, E[10⁸,10¹⁸) : E[10¹⁸,10⁶⁰) = 0.81C : 1.2C, so
"none ≤ 10¹⁸" says almost nothing about beyond. Both are monotone non-increasing in p. The 10¹⁸ verification only
bounds a floor by ε ≲ 1/π(10¹⁸) ≈ 4·10⁻¹⁷ and says nothing about its continuation. These are exactly the §3/§6
"conspiracy" scenarios, so §4.5 cannot be used to price them (as §6 implicitly does). *Repair:* retitle §4.5 "Within
the stretched-exponential family, heavy tails are self-refuting"; replace "The only escape is a zero law that is
non-monotone in L" by "The escapes are zero laws outside this family — a non-monotone law, a floor (a positive-density-
in-p conspiracy class), or a law decaying only polynomially in p — i.e. a new mechanism"; same in AGENT_REPORT.

**D10 (MINOR, §4.4 "Worst case anywhere").** Using the smallest observed f/L³ (a realised count, the minimum over
≈ 5.8·10⁶ primes) as the *mean* μ in the zero law is a heuristic scenario, not a worst case: the minimum over the
≈ 2.4·10¹⁶ primes below 10¹⁸ would be lower even if the distribution of f/L³ were fixed. *Repair:* call it
"pessimistic scenario"; the floor test (§4.3) is the actual evidence for its stability.

## Claim 6 — §5 adversarial search (`scripts/review_r274_adv.py`, `logs/review_r274_adv.txt`)

Own enumeration (ordered pairs over all divisors, residue-bucketed; tuples checked in the ET equation for e < 200;
first solution checked as 4/p = 1/x + 1/y + 1/z in exact rationals; factorisation by python-flint):
* p = 2054098191162848070241: p ≡ 1 (4), BPSW-prime (sympy strong BPSW and flint agree); **S = 870, S(127) = 160,
  W = 11 (Type II)** — identical to the log. 870/3294 = 0.264 ✓.
* p = 2286893395433206561 (min absolute S): S = 612, S(127) = 108, W = 11 (Type I) ✓.
* control p = 1388097828639363841 (C0): S = 2168, W = 3 ✓.
Max W over the 92 logged primes is 19 ✓. The designs' "D4 = lowest S(127) among 300/3000 D1 primes" selects on
the cheapest slices, so S/C0 for D4 is biased low *by construction* — the author says as much in Reading 4. SOUND.

**D11 (MINOR, §5 Reading 5, "p ≡ □ modulo every prime < 2.8·10⁶ (log p ≳ 2.8·10⁶)").** Requiring (ℓ/p) = +1 for all
ℓ < r is a density-2^{−π(r)} condition, not p ≡ 1 (mod ∏ℓ); heuristically the least such prime has
log p ≈ π(r)·log 2 ≈ 1.4·10⁵ for r = 2.8·10⁶, not 2.8·10⁶. The conclusion (out of reach) is unchanged. *Repair:*
"log p ≳ π(2.8·10⁶) log 2 ≈ 1.4·10⁵ heuristically".

## Claim 3 — §4.1–4.3 ladder (`scripts/review_r274_ladder.c`, `review_r274_zero_law.py`, `logs/review_r274_zero_law*.txt`)

*Counts.* My counter enumerates p = m·abd − k with k | a + b (c = (a+b)/k, gcd(a,c) = 1, ordered (a,b)) — a
different parametrisation from z32_ladder.c — and was checked against a direct (a,b,d)-loop for all primes < 600,
m = 4, 5, 8, 12, 16. All 21 lotteries were recomputed to 10⁸ (≈ 12 min on 2 cores). **Every number in §4.1 is
reproduced exactly**: m = 6: 13 (last 2521); 8: 21 (35 569); 10: 82 (145 441); 12: 169 (1 998 793); 16: 446
(12 895 921; 445 ≤ 10⁷ plus 12 895 921, which I also confirmed with a separate run to 1.4·10⁷); 20: 1162 (94 965 203);
24: 3739; m = 4, 5: none. The q_m, medians, c₀ values (7.03 … 15.74, geometric mean 11.59, m = 4 prediction 1.7·10³),
the floor-test table (min f_II/L³ ∈ [0.0117, 0.0212] over 2¹⁴–2²⁶, 10⁻³-quantile 0.0213 → 0.0279, 10⁻⁴: 0.0187 →
0.0235, median 0.0704 → 0.0554) and the hardest-cell μ/L³ = 0.035–0.038 are reproduced to all printed digits.

*Zero law.* My binomial ML fit on the same units (206 442 units): **a = 0.540, β = 0.907** (author 0.535, 0.91).
Restricting to units with μ ≥ 8, 12, 15, 20 gives β = 0.897, 0.892, 0.900, 0.873 and −ln P(μ = 229) = 69–74 (vs
74.4): no sign of β collapsing toward the break-even 0.53–0.59. NB moment fit: m = 6, [2²⁴, 2²⁶): 48.2 predicted, 0
observed; m = 8: 3.1 vs 0 ✓ (falsification stands).
Calibration by μ-bin (global fit): obs/exp = 0.96–1.16 for μ < 35, but **2.1 at μ ∈ [35, 40) (9 vs 4.2) and 2.4 at
[40, 50) (2 vs 0.8)**; Poisson tail P(≥ 11 | 5.07) = 0.015 for μ ≥ 35.

**D12 (MAJOR, §4.2 "Out-of-sample … mildly optimistic, never off by more than one order of magnitude", "within a
factor ≤ 7 for counts ≤ 5 (m = 12: 0.4 vs 3)"; AGENT_REPORT SHARP 1 "within ×1.5").** (i) Factually: the author's own
log (train p < 2²⁰) has m = 13: 0.1 predicted vs 2 observed (×20; my refit 0.12 vs 2, ×16) and m = 12: 0.4 vs 3
(×7.5 > 7). So "≤ 7" and "never off by more than one order of magnitude" are false. (ii) More importantly, the
misfit is *systematic in the extrapolation direction*: on test units with μ ≥ 35 the law trained on p < 2¹⁸ / 2²⁰ /
2²² predicts 2.0 / 2.8 / 3.9 zeros and **11 / 11 / 9 are observed** (Poisson tail 10⁻⁵ / 1.8·10⁻⁴ / 0.019). The
law under-predicts zeros by ×3–5 at the largest μ where zeros are still seen, and §4.4 extrapolates from there to
μ ≥ 229. This does not by itself move β much (restricted fits stay ≈ 0.87–0.90), and even a ×10⁵ correction leaves
§4.4's numbers astronomically small; but it is exactly what the author's within-cell-heterogeneity caveat
(`z32_lowdev.txt`) predicts, and it must be reported rather than summarised as "mildly optimistic". *Repair:* replace
the out-of-sample sentence by the per-μ table (test μ ≥ 35: predicted ≈ 2–4, observed 9–11), say "under-predicts
zeros at the top of the observed μ range by ×3–5 (significant)", drop "never off by more than one order of
magnitude", and in §4.4 add a model-error factor (e.g. ×10–10³) to the quoted expectations.

**D13 (MINOR, §4.3 crossover law).** (i) c₀ for m = 20, 22 uses last failures at 9.5·10⁷ / 9.4·10⁷, i.e. right-censored
at the 10⁸ search limit; the "constant across m = 6…23" range should exclude or flag them (the author's own
geometric mean already excludes them, the range statement does not). (ii) q_m is measured at [2²⁶, 10⁸] but
compared with p_last ≈ 2.5·10³ … 10⁷ for most m; the m = 4 floor test shows q itself drifts (0.021 → 0.028 over
2¹⁴–2²⁶), so c₀'s constancy is partly a statement about the drift of q. (iii) For m = 4, 5 the law predicts a last
failure ≈ 1.7·10³ / 1.9·10³ and there are no failures at all: the law is not validated at the bottom of the ladder,
which is where ES sits. All three are honest-labelling issues for an EVIDENCE claim; *repair:* state them.
