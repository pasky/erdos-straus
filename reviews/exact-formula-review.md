# R131 — hostile review of O131 (EXACT_FORMULA.md, AGENT_REPORT_O131{,b}.md, scripts/exf_*)

Reviewer branch: side-agent/review-exact-formula (merged side-agent/exact-formula at review time).
All numerical checks below use reviewer code written from scratch (`scripts/review_r131_*`), except where stated
that the author's dump was *read* for comparison.

## Summary verdicts

| claim | verdict |
|---|---|
| Lemma 1.1 (Type I completion for composite n) | SOUND |
| Lemma 1.2 (signed Type II) | SOUND |
| Prop 2.1 (T2⁺(m²) = 0 for all m) | SOUND |
| Prop 4.2 (T1±(2^k) = 0) | SOUND |
| §3.1 dictionary (A_{c,d} = character sum) | SOUND (= O128 Prop 9.1, credited) |
| §3.2 exact theta identities for cd | 6 | SOUND (identity); one false side remark (D2) |
| Prop 4.1 signed decomposition, −2 boundary | SOUND (checked n ≤ 3000 on support, full box n ≤ 60) |
| Lemma 5.1 (ideal divisors of α ↔ divisors of N(α)) | SOUND |
| Thm 5.2 (Type I CM torus) | SOUND-AFTER-REPAIRS (D3, D4: notation + missing p | cd case) |
| §2.3 rank search, "dim(span E ∩ span C) = 0" | SOUND as EVIDENCE; now upgraded to CERTIFIED (exact ℚ-rank, R131) for the 54-column dictionary, n ≤ 2·10⁴; headline wording overclaims (D1) |
| §3.3–3.4 genus-vs-orbit numerics | SOUND (all numbers reproduced from scratch); one conclusion overclaimed (D7) |
| §5.3 class bias in means (EVIDENCE) | not re-checked (context budget) |
| Overlap/credit with O128 | ACCURATE for §3; two missing credits (D6) |

**Overall: no FATAL or MAJOR defect. The negative verdict and all PROVED labels stand. Eight MINOR defects, all
repaired in EXACT_FORMULA.md (marked "(R131 repair)").**

## Checks

### C1. Lemma 1.1 — SOUND
Re-derived: from `b(4acd − n) = na + Sc`, f = 4acd − n divides na + Sc; and `c·4a²d = a(n + f) ≡ an (mod f)`, so
`f | c(4a²d + S)`. With h = gcd(f, 4a²d + S), gcd(f/h, (4a²d+S)/h) = 1 gives k = f/h | c; dividing the equation by
k gives the solution (n/k, a, b, c/k, d) with f' = h | 4a²d + S. Converse: dividing/multiplying the equation by k. ✓
Numerics (`scripts/review_r131_brute.c`: direct search of the four equations with explicit bounds, no
parametrisation; `scripts/review_r131_compare.py`): for n ≤ 3000 the brute-force solution *sets* (not only counts)
of T1⁺, T1⁻, T2⁺, T2⁻ are identical to the author's `exf_engine` + `expand_T1` output (184 869 / 235 265 / 48 693 /
46 939 tuples); the Lemma 1.1 decomposition (k | c, k | n, rescaled tuple is a solution with h | 4a²d + S) holds
for every brute-force tuple, and every k-scaling of a k = 1 tuple is in the brute-force set. 0 failures.

### C2. Lemma 1.2 — SOUND
(qa − 1)(qb − 1) = qcn + 1 > 0 forces a, b of equal sign; a = 0 ⇒ b = −cn; a, b ≤ −1 gives
4a'b'cd + a' + b' = nc, i.e. T2⁻. The Type I remark (a, b ≤ 0 forces a = 0) also re-derived. ✓

### C3. Prop 2.1 — SOUND
Re-derived: X = 4cda − 1 > 0, X | 4c²dm² + 1 ⇒ gcd(X, 2cm) = 1 and −d ≡ (2cm)^{−2} (mod X) ⇒ Jacobi (−d/X) = 1.
For odd X > 0, (−4d/X) = (−d/X); the Kronecker symbol (−4d/·) is a character mod 4d with value −1 at −1 (negative
discriminant, also for non-fundamental −4d), and X ≡ −1 (mod 4d). Contradiction. No gcd hypothesis used. ✓
Numerics: T2⁺ zeros n ≤ 3000 = all squares plus {288, 336} (matches the stated "3 non-squares" up to 2·10⁴ as far
as checked). T2⁻ zeros n ≤ 3000 = exactly {1,2,3,4,7,8,12,15,24,44,108,168} ✓. T1⁺(9) = 2 ✓,
T1⁺(p²) = T1⁺(p) for all primes 3 ≤ p ≤ 53 ✓.

### C4. Prop 4.2 — SOUND
Re-derived: h | 4a²d ± 1 is odd, so m = 4ac'd − h is odd; for n = 2^j, m | n forces m = 1. S = +1: the solution of
m = 1 needs h = 4ac'd − 1 | a + c', but 4ac'd − 1 − a − c' ≥ (4a − 1)c' − a − 1 > 0. S = −1: bh = a − c' with
h > |a − c'| forces a = c', b = 0. ✓ Numerics: zeros of T1⁺ and of T1⁻ for n ≤ 3000 are exactly {2^j} ✓.
The "conversely" remark is correct for every divisor m | n (scaling by n/m), not only odd m.

### C5. §3.1–3.2 — SOUND (identity), side remark false
Re-derived: M = 4c²dn + 1 is prime to q = 4cd, so orthogonality on (ℤ/q)^× gives
`#{X | M : X ≡ −1} = φ(q)^{−1} Σ_χ χ̄(−1)σ_χ(M)` (χ̄(−1) = χ(−1)); for q ∈ {4, 8, 12, 24} every character is real,
so this is the 2^{−k} Σ_{χ quadratic} formula — it is a tautology of orthogonality, correctly called "elementary".
Numerics (`scripts/review_r131_slices.py`, own code: real characters found by brute force as ±1 homomorphisms,
divisors via sympy): for all nine (c,d) with cd | 6 and **all n ≤ 3000** (not only primes): A = 2·T2⁺_{c,d} − δ⁺ =
character formula, 27 000 cases, 0 failures; A_{1,1}(n) = (τ(4n+1) − r₂(4n+1)/4)/2 with r₂ counted by brute force,
0 failures. See D2 for the false "vanishes exactly on a union of square classes" remark.

### C6. Prop 4.1 — SOUND
Re-derived: positive divisors X ≡ 1 (mod q) of N are X = 1, X = N (a = 0 pair) and −X = qa − 1 with a ≤ −1, i.e.
T2⁻ (ordered, so 2T2⁻ − δ⁻); X ≡ −1 gives 2T2⁺ − δ⁺. A₊₁ ∓ A₋₁ = (2/φ)Σ_{χ odd/even}σ_χ(N) by orthogonality,
so both displayed formulas hold, and each bracket vanishes exactly when the (c,d) slice is empty (finite support). ✓
Numerics (same script): per-slice identities A₊₁ = 2 + 2T2⁻_{c,d} − δ⁻, A₋₁ = 2T2⁺_{c,d} − δ⁺ on every (c,d) in the
support for all n ≤ 3000 (143 012 slices), and for n ≤ 60 on the full box c ≤ n + 1, d ≤ n/2 + 1 (which contains
all solutions: T2⁺ has c ≤ a + b ≤ 2b ≤ 2(n+1)/3, d ≤ (n+2)/4; T2⁻ has d < n/4, c < n), with the summed totals
2(T2⁻ ∓ T2⁺) − (δ⁻ ∓ δ⁺) reproduced exactly. 0 failures. (The author checked n ≤ 40 only.)

### C7. Lemma 5.1 / Theorem 5.2 — SOUND-AFTER-REPAIRS
Lemma 5.1 re-derived: in O_K with d ≡ 3 (mod 4), α = (p − 2c) + 4c·(1+√−d)/2 is still primitive (an odd m | α
needs m | p, m | 2c; m = 2 needs p even). Every ℓ | N(α) is odd and ℓ ∤ d, hence unramified and prime to the
conductor of ℤ[√−d]; inert ℓ would divide α; so ℓ splits and exactly one of 𝔩, 𝔩̄ divides α, to full power. ✓
Thm 5.2: (i) f = 4cda − p ≡ −p and g = N/f ≡ p²/(−p) = −p (mod q), so the ordered divisor count is right;
(β) ≡ 1 mod 4cd ⇒ N(β) ≡ 1, so the condition is a ray-class function factoring through the norm ✓.
(ii)/(iii): Fourier support of a function factoring through Norm is {χ∘N} ✓; pairing χ ↔ χχ_{−4d} uses
χ_{−4d}(X) = 1 for every divisor X of N(α) (all are norms, coprime to 4d) ✓.
Numerics (same script; primes 5 ≤ p ≤ 3000, all (c,d) in the support plus the box c < 8, d < 40, p ∤ 2cd;
131 863 cases): #{f | p² + 4c²d : f ≡ −p (mod 4cd)} = 2T1⁺_{c,d}(p) − δ; nonzero only when (−4d/p) = −1 (inert);
(−4d/f) = 1 for **every** divisor f of N(α). 0 failures. I did not re-run the PARI ideal-factorisation check
(the elementary argument above suffices). See D3, D4.

### C8. §2.3 rank search — SOUND, upgradeable to CERTIFIED; validity questions answered
*Is a mod-p rank valid for real-coefficient relations?* Real relations among rational vectors exist iff rational
ones do, so ℚ is the right field. For an integer matrix rk_p ≤ rk_ℚ, hence rk_p(C∪E) is a valid **lower** bound
for rk_ℚ(C∪E), but rk_p C, rk_p E are only lower bounds for rk_ℚ C, rk_ℚ E, so `rkC + rkE − rk(C∪E)` computed mod p
is *not* a rigorous upper bound for the ℚ-intersection dimension (dim_ℚ ≤ (rk_ℚC − rk_pC) + (rk_ℚE − rk_pE)).
The author's code (`exf_nullspace.py`) does only the mod-p computation, although its docstring says "then exact
verification" (none is performed). *Is the 500-random-row restriction valid?* Yes in the direction claimed, but
only if the restriction π is injective on span E: a relation Eu = Cw on all rows restricts to the subset, and
π(Eu) ≠ 0 needs injectivity; for 5 of the 6 row sets rk E < #E columns, so this has to be checked.
**R131 check (`scripts/review_r131_rank.py`, own code):** I regenerated the author's columns
(`exf_engine`, `exf_hurwitz`, `exf_columns.py`) and spot-checked them: all 56 ES columns equal my brute-force values
for n ≤ 3000; 12H(D) equals my reduced-form count for D ≤ 3000 and 300 random D ≤ 1.4·10⁶; H(n), H(4n), τ(4n+1),
τ(n²+4), Σ_x H(4n − x²) (n ≤ 600), τ(n): 0 mismatches. Then, on 500 **own** random rows per set (all 267 rows for
p ≡ 1 (24) — the author's "500 random rows of each row set" is not literally true there), fraction-free exact
ℚ-ranks:

| rows | rk_ℚ C | rk_ℚ E | rk_ℚ(C∪E) | dim_ℚ ∩ | ker_ℚ E(subset) kills all rows of the set |
|---|---|---|---|---|---|
| all n ≥ 2 | 46 | 56 | 102 | 0 | (trivial kernel) |
| odd n | 41 | 52 | 93 | 0 | yes (dim 4) |
| primes ≥ 5 | 27 | 50 | 77 | 0 | yes (dim 6) |
| p ≡ 1 (4) | 22 | 47 | 69 | 0 | yes (dim 9) |
| p ≡ 3 (4) | 22 | 49 | 71 | 0 | yes (dim 7) |
| p ≡ 1 (24) | 18 | 45 | 63 | 0 | yes (dim 11) |

(rk C for p ≡ 1 (4) is 22 on my rows vs 23 on the author's; immaterial.) Since π is injective on span E, a nonzero
v ∈ span E ∩ span C on the full row set would restrict to a nonzero element of the subset intersection.
Therefore: **CERTIFIED (R131): for each of the six row sets ⊂ [2, 2·10⁴], no nonzero linear combination (real
coefficients) of the 56 ES columns equals a linear combination of the 54 classical columns.** This is the correct
scope: a finite dictionary on a finite range — it says nothing about classical functions outside the dictionary
(e.g. Σ_{c,d} twisted divisor sums at 4c²dn + 1, which Prop 4.1 shows *do* give exact identities).

### C9. §3.3–3.4 numerics — reproduced
`scripts/review_r131_genus.py` (own code): Σ_{c≤C} A_{c,1}, Σ G_{c,1} for p = 101, 1009, 2003 and C ∈ {10, …, 2000}
reproduce the §3.4 table exactly; §3.3 rows (1,5), (1,7), (5,2) reproduce (mean|A−G| for (1,5) is 0.25 vs printed
0.26, rounding). The identity "genus average = projection on characters with χ² = 1" re-derived ✓.

### C10. Overlap with O128 and citations
O128 Prop 9.1 (character expansion + Eisenstein identification), Prop 9.2 (genus pairing) and Prop 8.3 (a = 0
trivial factorisation; sign at ∞) are as stated and are credited in §3. ET Prop 1.6 (sources/elsholtz-tao-1107.1010.pdf,
l. 275) is "for any odd perfect square n, f_I(n) = f_II(n) = 0": Prop 2.1's "without the gcd hypotheses" (and for
even m) is an accurate description of the extension. Missing credits: D6.

## Defects (all MINOR; repaired in EXACT_FORMULA.md, marked "(R131 repair)")

1. **D1 (MINOR, §0 bullet "No identity with classical functions", §2.3).** Scope and rigour overstated/understated:
   the claim is for a 54-column dictionary and n ≤ 2·10⁴ only; the mod-p rank does not rigorously bound the
   ℚ-intersection from above (C8); the 500-row restriction needs injectivity on span E; p ≡ 1 (24) has only 267
   rows; `exf_nullspace.py` docstring claims an exact verification it does not do. *Repair:* scope the headline;
   add the R131 exact-ℚ certification (C8), which makes the statement CERTIFIED.
2. **D2 (MINOR, §3.2 "Every slice with cd | 6 vanishes exactly on a union of square classes").** False:
   A_{1,1}(n) = 0 iff 4n + 1 has no prime factor ≡ 3 (mod 4); e.g. A_{1,1}(3) = 0 but A_{1,1}(12) > 0
   (49 = 7²), both n ≡ 0 (mod 3). The zero set lies inside the residue classes not covered by Mordell's
   congruences but is not itself a congruence set. *Repair:* reword.
3. **D3 (MINOR, Thm 5.2 notation).** `T1_{c,d}(p)` in §5 is the *ordered* count 2T1⁺_{c,d}(p) − δ, whereas T1 is
   defined with a ≤ b; diagonal solutions exist (c = 2a, p = 4a²d − 1). Also (iii) for non-squarefree d is about
   the ring class group of ℤ[√−d]. *Repair:* define T1^{ord}; note.
4. **D4 (MINOR, Thm 5.2 hypothesis p ∤ 2cd vs. "Answer" about all of T1(p)).** Needed: (c,d) with p | cd carry no
   Type I solution. *Proof (R131):* p | d ⇒ p | c (as c = 4abcd − p(a+b)); c = pc₁ ⇒ 4abc₁d = a + b + c₁, a Type II
   solution for n = 1, impossible by Prop 2.1 (m = 1). Numerically 0 such tuples for p ≤ 3000. *Repair:* add.
5. **D5 (MINOR, §0(c), Prop 4.1).** "checked n ≤ 40" — now checked n ≤ 3000 (C6). *Repair:* update.
6. **D6 (MINOR, credit).** Prop 4.1's boundary reading (a = 0, divisor 1 in class +1, sign at ∞) is O128 Prop 8.3,
   not credited in §4; §5's conclusion (class-group characters cancel, only genus data survive) parallels O128
   §9.3 for the Type II CM theta series of ℚ(√−dp). *Repair:* add credits.
7. **D7 (MINOR, §0 Siegel–Weil bullet).** "Hence no 'Eisenstein main term + small cusp error' formula exists for
   the total count" is an Assessment: §3.4 shows only that the *untruncated* genus mass diverges and §3.3 that
   the per-slice error is as large as the main term. *Repair:* relabel as Assessment.
8. **D8 (MINOR, §2.3 text).** "Exact rank computation mod 2³¹−1" — the computation is modular, not exact over ℚ.
   *Repair:* covered by the D1 note.
