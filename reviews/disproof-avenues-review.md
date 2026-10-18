# R274 — hostile review of O262 (DISPROOF_AVENUES.md, BRAINSTORM/z32_*, scripts/logs z32_*)

Reviewer branch `side-agent/review-disproof`; author files merged from `side-agent/disproof-avenues`.
From-scratch scripts: `scripts/review_r274_*`. Labels as in DISCOVERIES.md. ES is not solved; nothing below changes that.

(Work in progress — verdict table filled claim by claim.)

## Verdict table

| # | claim | verdict |
|---|---|---|
| 1 | §1–2 citations (BL Thms 1.6/1.8/1.9, Rem 1.10; Markoff; Lyczak; Mihnea–Dumitru 10¹⁸; PW) | SOUND-AFTER-REPAIRS (D1, D2, D3) |
| 2 | Prop 3.1 (n = 1 shadow) | SOUND-AFTER-REPAIRS (statement true; proof has two small gaps D4, D5; existence clause D6; attribution D7) |
| 3 | §4.1–4.3 ladder counts, zero law, crossover law | pending (counts SOUND so far) |
| 4 | §4.4 expected-failure numbers | pending |
| 5 | §4.5 heavy tails self-refuting | pending |
| 6 | §5 adversarial search, hardest prime | pending |
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
Salez 10¹⁷ bound (the β-table changes only marginally — checked in Claim 5 below).

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
