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
| (further claims appended below as checked) | |

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
all solutions: T2⁺ has c ≤ a + b ≤ (n+4)/3·…, d ≤ (n+2)/4; T2⁻ has d < n/4, c < n), with the summed totals
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
