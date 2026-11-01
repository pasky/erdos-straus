# Hostile review of Z52D_THINFAMILY.md (lane THINFAMILY)

Reviewer: subagent, hostile mode. Scope: the full memo, checked line by line against the paper (§§ forced budgets, Theorems,
Limits), EXP_15 §2, EXP_OPEN §1–2, MENU_LADDER §2, the five scripts and the logs in data/z52d/thinfamily/.
Every Python run used `ulimit -v 8000000` and `timeout`.

**Verdict: no FATAL defect.** The memo never claims ES, or a new family, is proved. The mathematics of Thms 1, 2, 5,
Prop 3 and Lemmas 4, 6 is correct, apart from one load-bearing citation gap (M4). There are 4 MAJOR defects: one is an
unsupported certified range, one an incomplete survivor list, and two are proof gaps. All four can be repaired.

## Defects

### MAJOR

**M1. The certified range E_max = 3000 is not supported by the log.**
* Where the claim appears: §0 bullet "CERTIFIED for 15·2^s + 1 … any E ≤ E_max = 3000"; §4 Comp. 8(a); §7 FRONTIER
  text "certified empty for v₂(c) ≤ 3000".
* The committed `menuA_15_E3000.log` ends at ".. E = 1200 done" and has no summary line.
* The run is still going (PID 1486291, started 06:03). At review time the working-tree log had reached E = 1600.
* `testA` raises `RuntimeError` when the k-range is too large. So a run can also abort, and then the certified range is
  only the last completed E.
* The memo's hedge "(the completed range is stated in §4)" points to §4, which only says "see the last line". The
  FRONTIER text has no hedge at all.
* Fix:
  * Quote the actual completed E (the final `c0=15 EMAX=…` summary line, or the last ".. E = … done" line) everywhere.
  * Commit the finished log before any "3000" appears.
  * In §7 write "v₂(c) ≤ ⟨completed E⟩" for integer u.

**M2. The survivor lists treat "Ridout-finite" and "certified up to a bound" as dead.**
* Where: §0 "The rest survives", §6 "Surviving", §7 "Open".
* Ridout gives ineffective finiteness, not non-existence. A solution with p ≥ 5 and E > E_max is not excluded.
* Missing survivors:
  * (a) menu A, p ≥ 5, E > E_max. §0 and §6 list only p = 3.
  * (b) menu A′ with integer u (all p, p = 3 included), E > E_max.
  * (c) dyadic A′ (u or w = r/2^i) with e > 66. It is listed in §6 "reduced" but missing from the §0 survivor list and
    from the §7 Open list.
* The §7 text also conflates dyadic A′ (certified only for e ≤ 66) with "v₂(c) ≤ 3000".
* Fix: add (a)–(c) to all three lists. Change §7 to "A, A′ (integer u): certified for v₂(c) ≤ E_done; A′ dyadic: e ≤ 66;
  beyond that A is finite per p ≥ 5 (Ridout, ineffective), A′ (integer u) is finite per p, and the rest is open".

**M3. Even integer u (menu A′, Thm 7) and even integer w (Sophie-Germain A′) are not treated.**
* The integer-u case of Thm 7 says "the roots of B are 2-adic units". That is false for even u: then c = 15u^p − 1 is
  odd, E = 0, and v₂(α) = p·v₂(u)/D > 0.
* The SG integer-w case uses v₂(α) = 2/D, which needs w odd.
* `menuA.py` enumerates only odd u (`u % 2 == 1`, E ≥ 1), and `dyadic.py` only handles i ≥ 1.
* Yet §0 and Comp. 8(a) claim "no A′ family with integer u … any p".
* The gap closes quickly. For even u = 2^k u′:
  * φ₀ is a unit, so v₂(X) = −t with t = pk·deg P/D ∈ [1, pk − 1] for a proper factor. Also X′ ∈ ℤ.
  * z(1) gives X′ ≡ −1 and X ≡ −16 (mod c). So 2^tX = jc − 2^{4+t} and X′ = j′c − 1.
  * Expanding gives jj′c = j + 2^{4+t}j′ + 2^t, hence c ≤ 17·2^t + 1 ≤ 8.5·2^{pk} + 1.
  * But c ≥ 15·2^{pk} − 1. Contradiction.
* Even w = 2^k w′ works the same way: t ≤ 1 + 4k gives c ≤ 1 + 34·16^k, while c = 60·16^k w′⁴ − 1. Contradiction.
* Numerical cross-check (`/tmp/rv/chk.py`, run during this review): even u ≤ 398, p ≤ 11, all t ≤ p·v₂(u) with the Y = 1
  conditions of A′ gave 1 079 090 tests and 0 passes.
* Fix: add this paragraph to Thm 7, and state in Comp. 8(a) that even u is excluded by hand.

**M4. Remark (i) after Thm 2 is load-bearing but its citations do not prove it.**
* What depends on it: "n + c reducible ⇒ Capelli ⇒ 1 + c = c₀u^p", which feeds Lemma 4 item 3, Thm 7, Cor 5.1(a) and
  all of Comp. 8.
* The case f′ constant gives x, y, z as polynomials in n with **rational** coefficients. The cited paper Lemma T1 /
  Cor T1class / EXPONENT_COVERING Thm 1.4 are statements about ET classes: integer parameters κ with the gcd
  bookkeeping of Cor T1class.
* Passing from an arbitrary polynomial-in-n identity to an ET class is exactly ET Prop 1.9. The paper explicitly says
  "we do not need this" and does not prove it.
* Fix, either of:
  * (a) Cite ET Prop 1.9 / CovNote Prop 3.1 precisely, with the hypotheses checked.
  * (b) Give the direct argument. At n = t² (t odd, coprime to c and to the denominators, t² ≡ ρ by CRT):
    * in (A): y/n = (1+X′)/4 ∈ ℤ and z/n ∈ ℤ (since gcd(c, n) = 1);
    * gcd(x, n) divides c, so it is 1;
    * the integer Type II decomposition x = abd, y = acdn, z = bcdn with gcd(abd, n) = 1 then contradicts Lemma T1(ii);
    * (A′) is analogous, through Type I.
* Promote the remark to a labelled lemma, because it carries weight.

### MINOR

**m1. The BM calibration count is wrong.**
* The memo (§2) says "All 3 × 43 sequences pass".
* `bm_calibration.log` has **39** rule-classes: 14 (3·2^s+1) + 2 (cubic) + 23 (63·2^s+1, of which 5 are the II-ad
  classes and 18 the ET/divisor rules). That is 117 sequences, all True/True.
* Fix: replace 43 with 39.

**m2. Two labels in the BM section overclaim.**
* The §0 bullet "Calibration (CERTIFIED)" contains the flat claim "**Minimal** certificates are not C-finite". This is
  EVIDENCE only: L = 12 = len/2 on 24 terms is inconclusive. §2 itself says EVIDENCE.
* In §2, "(an ET class with constant gap)" is attached to the even-s gap-7 class. That class contains μ = 0, so it is a
  constant-gap window with a lottery budget, not an ET class (Thm sterile, Thm W).
* Fix: label the §0 claim EVIDENCE and reword the §2 parenthetical.

**m3. Thm 1 states hypothesis and steps less precisely than the summary claims.**
* The hypothesis takes P_j ∈ ℚ[t]. The §0 summary ("C-finite with roots 2^{ℚ}·ζ") needs one more step: restrict to
  t ≡ 0 mod M, group equal bases, and use Galois invariance to get rational coefficients.
* Step 1 must restrict to the class t ≡ 0. An arbitrary residue would not keep μ = 0 in the closure, and ζ^r would not
  be rational.
* Step 5's modulus should be L·lcm(e, M), not Le.
* Fix: add one sentence for each point.

**m4. Cor 5.1(b): "≈ 3 solutions u per E" for p = 3 is too high.**
* Count: u ≡ β (mod 2^E) with u < 4.09·2^E gives about 4 values, and the exact-valuation condition halves that to ≈ 2.
* The log shows about 1.6 candidates per E summed over all p.
* Fix: "≈ 2".

**m5. Cor 5.1(a) overstates its independent confirmations.**
* It says the result is "also covered by z52d_thinfamily_binom.py and the paper's boxed-equation enumeration".
  binom.py covers only D = p·t with t ≤ 4. The boxed equation covers only integer (a, d).
* The real proof is the E = 2 enumeration, which I re-did independently:
  * candidates (u, p) = (3,3), (11,3), (3,5), (3,7);
  * c_o = 101, 4991, 911, 8201;
  * no divisor pair passes item 4.
* Fix: drop or qualify "also covered".

**m6. Thm 7, Sophie-Germain integer-w case: a typo and unnecessary sub-cases.**
* "2^{|a|}X′ = j′c − 1" should be "X′ = j′c − 1". Only the latter yields the stated jj′c = j + 2^{4+|a|}j′ + 2^{|a|} and
  the equations 300 and 150.
* a ∈ {0, −2} correspond to deg P ∈ {0, D}, i.e. f or f′ constant, which is already excluded. Only a = −1 is live.
  Harmless, but state it.

**m7. Thm 7 leaves two steps implicit.**
* (i) c ∈ ℤ[1/2] ⇒ u (resp. w) has no odd denominator: odd(v)^p | 15 forces v = 1.
* (ii) In the integer-u case φ₀′ is a 2-adic unit because φ₀φ₀′ = 15u^p is odd. This is needed for X′ ∈ ℤ_(2).
* Fix: add one line for each.

**m8. The shape test in the script is not Lemma 6, and the control logs predate it.**
* In `menuA.py`, `shape_any_D` also tries negative ℓ (`for l in (l0, -l0)`), and its `continue` guard is dead code.
  This is a superset of Lemma 6, so it is still sound for killing hits.
* But it does not match the memo. Re-running `menuA.py 3 60`, the c₀ = 3, u = 1 A′ hits *survive* the script's test
  with (1, −1) and (2, −1). They die under Lemma 6 only because ℓ_g > 0.
* The committed control logs `menuA_3_E400.log` and `menuA_63_E400.log` were produced before the shape column existed.
  So "passes Lemma 6" (c₀ = 63) and "Lemma 6 kills [u = 1] for A′" (c₀ = 3) are in no log.
* Fix: restrict to ℓ > 0, re-run the controls, and commit the logs.

**m9. Several claims cannot be reproduced from the repo.**
* "k-loop cross-checked … 2400 cases, 0 mismatches": no script or log.
* binom controls, Ap controls, and the binom 15 run of Comp. 8(c): no logs.
* I re-ran them:
  * my own k-loop vs. divisor comparison, 1200 cases (c₀ ∈ {3,15,63,255}, u < 200, p ≤ 7): 0 mismatches;
  * `binom 63 5 30 1,2 0`: Thm 2.3 family at D = 3, 6;
  * `binom 3 7 40 1,2 1`: c = 80;
  * `binom 15 7 200 1,2,3,4 2`: 152 928 tests, 0 hits;
  * `Ap 3 8 10 7`: c = 80 and SG c = 11.
* Fix: commit the cross-check script and these logs.

**m10. References and numbering are stale or vague.**
* "Thm 3.3 below" appears in the Thm 1 *Reading*.
* The script headers cite "Thms 3.3, 3.4", "Lemma 3.6", "§3.5", but the memo numbers them Thm 5, Thm 7, Lemma 6, Thm 7.
* "the paper's Thm 5.x" is vague.
* "Theorem 2.3" is used without saying which document (it is EXP_OPEN Thm 2.3 = paper Lemma 63class).
* "paper Comp. 5.8" is cited for irreducibility when c₀ = 3, but comp:W does not list (3, 1). Capelli is trivial there,
  so just say so.

**m11. Latent bug in `binom.py`.**
* `factcache` is keyed by (D, u), but `factors()` uses the global p.
* It is harmless for the runs used, because the D-sets {p·t : t ≤ 4} for distinct p are disjoint. It would bite if
  t ≥ 5 were allowed.
* Fix: key the cache by (D, u, p).

**m12. "Repairs … the I-cd dead remark of EXP_OPEN" is unexplained.**
* The memo never says what was wrong with EXP_OPEN's one-line argument.
* Fix: say what is repaired (presumably the 2 | d case and the gcd bookkeeping), or call it "makes rigorous".

**m13. Lemma 4 item 3 is stated more generally than it is proved.**
* It claims u ∈ ℤ for general c₀, but the proof needs c₀ to be p-th-power-free.
* Fix: put that hypothesis in the statement.

## Verified correct (by me)

* **Thm 1, steps 0–6.**
  * The negative-power vanishing argument holds: R(t) ∈ (1/e)ℤ and R(t) → 0.
  * The ℚ[t, Y] identity follows from linear independence of t^k 2^{λjt}.
  * Integrality after t ↦ t₁: (t − t₁) | e(P_j(t) − P_j(t₁)) and e | t − t₁, so G(2^{λt}) ≡ x_t (mod 1).
  * Positivity follows from P_top(t₁) > 0. The identity specialises because n does not involve t. The class
    t ≡ 0 (mod e…) keeps μ = 0 in the closure. (Precision caveats are in m3.)
* **Thm 2.**
  * Coprimality: gcd(x, n) = 1 ⇒ f is coprime to N.
  * The resultant / remainder steps, g ∈ ℚ[Y], and f | d₁ + d₂ all hold.
  * The case analysis is exhaustive. I checked all 9 placements of (n, P) among (d₁, d₂, d₃):
    * both in d₃: constant;
    * n in d₃, P in d₁ or d₂: (A);
    * P in d₃, n in d₁ or d₂: (A′);
    * n and P split between d₁ and d₂: excluded;
    * n and P both in d₁ (or both in d₂): (C).
  * I recomputed y and z in every case. For (A), λ₁λ₂λ₃ = λ′ gives y = n(1+f′)/4 and z = nx(1+f′)/c. I re-derived
    (A′) and (C) the same way.
  * All three converse identities hold. All constants are positive.
* **Prop 3, the full Jacobi argument.**
  * c = 4gw; gcd(x₁z₁, w) = gcd(x₁z₁, n) = 1; gcd(w, n) = 1; w | g; c = 4w²d.
  * (−d/f) = 1 from n² ≡ −4w²d with q ∤ 2wd.
  * f ≡ 3 (mod 4). When 2 | d: f ≡ −1 (mod 8), so (2/f) = 1.
  * Reciprocity gives (−d/f) = −(n/d′), and (n/d′) = 1 near μ = 0. The contradiction is correct.
* **Lemma 4, all items.**
  * φ₀ and φ₀′ are 2-adic units ≡ 3 (mod 4).
  * c ∈ ℤ[1/2] ∩ ℤ_(2), and 4 | c.
  * The 4w⁴ case is impossible by parity.
  * X, X′ ∈ ℤ_{>0}.
  * (F+X)(1+X′) = 2F + FX′ + X + c, which gives the stated equivalence.
  * Item 5 holds. The converse follows from Lemma special. (The Capelli step depends on M4.)
* **Thm 5.**
  * W² = c_o(k²c_o − 4F(k + 2^E)) and (kW)² = A² − Q² are both correct.
  * The factor argument gives |A| ≤ (Q² + 1)/2, and the bound decreases in k.
  * A random sanity check found 0 violations.
* **Cor 5.1 numbers.**
  * 12960 (12960.5 floored).
  * u^p ≤ 3456 < 3457.
  * u ≤ 15, 5, 3 for p = 3, 5, 7, and no u ≥ 3 for p ≥ 11.
  * C_A(2)/16 = 810.03 ≤ 811, and the ratio decreases in E.
  * 2^{3E+10} and the root bound 4.087·2^E.
  * p-th roots in (ℤ/2^E)^× and |u − ζβ|₂ = 1.
  * Ridout applies to integer approximants with exponent > 1: the Subspace computation u·|u − β|₂ < u^{−ε}. For p = 3
    in menu A the exponent is exactly 1, as the memo says.
* **Lemma 6.**
  * β = 1/α are the roots of AZ^D + B. The Gauss factorisation gives ℓ_g | A and g(1) | A + B.
  * Q(1) > 0, so φ₀ = Xℓ/g₁ for every D.
  * Hand checks: for u = 1, c = 14, X = 5 the test kills A and A′. For u = 1/2, c = 7/8, X = 5, the candidates
    φ₀ ∈ {5, 5/3, 5/9} all fail v₂(1+φ₀) ≥ 5.
* **Thm 7.**
  * Integer odd u: c_o | X′ + 1, X ≡ −16, jj′c_o = 2^E + j + 16j′, c_o ≤ 2^E + 17, exponent p/2 > 1 so Ridout holds for
    p = 3 too. Correct.
  * SG integer w (w odd): c ≤ 69, w = 1, c = 59, and the equations (59j − 64)(59j′ − 1) = 300 and
    (59j − 32)(59j′ − 1) = 150 have no solutions.
  * Dyadic case: e = ip resp. 4i − 2, v₂(X) = 0, X″X = 2^{e+4} + c_num, jj′c_num − 2^e j − 16j′ = 1, and
    2^e < 15r^p ≤ 2^{e+1} + 17.
* **Logs and re-runs.**
  * `menuA.py 63 60` (and 63 20): exactly (2, 3, 3, 1700, 21, 84), and it survives the shape test with ℓ > 0, e.g. (7, 9).
    The Thm 2.3 values check: f(1) = 21, f′(1) = 84, k = 13.
  * `menuA.py 15 60`: only u = 1 at E = 1, dead.
  * `menuA.py 3 60`: c = 80 hits.
  * `dyadic.py 30`: one hit, u = 1/2, dead.
  * `dyadic_E66.log`: 451 713 windows. `Ap_general_15.log`: 1064 pairs, 0 hits.
  * BM log: every row is (True, True), with the L values as stated (SG 2/9/7/9, 63-family (4, 4, 8), ET ≤ 4).
  * Minimal-certificate log: gap 3 on odd s ≥ 3, gap 7 on even s ≥ 14, L(y) = 12 on 24 terms.
* **Representation of earlier work.**
  * (BI) ⊆ (A) as shapes (c = 4a²d); the check is z = nx(1+f′)/(4a²d).
  * (A′) = I-ac; I checked f·b = an + c.
  * The descriptions of Remark iiadhyp, Thm iiad3, the EXP_15 §2.4 "superelliptic" sub-branch and EXP_OPEN Map 2.4 are
    accurate.
* **§5.** 4³ + 297 = 19², ord₁₉ 4 = 9, and 19 | n ⇔ s ≡ 3 (mod 9).
