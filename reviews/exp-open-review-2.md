# EXP_OPEN (O246) — hostile review #2 (R258), round 1

Reviewer R258. Round 1: no edits to the author's files. Scripts written from scratch: `scripts/review_r258_*.py`
(no z19_/z15_/z14_ imports). Document reviewed: EXP_OPEN.md at side-agent/exp-open (merged into this branch).

## Summary verdicts
| claim | verdict |
|---|---|
| Theorem 3.1 (ES for every 63·2^s + 1) + Theorem 2.3 | **SOUND** (minor wording defects D1–D3) |
| Theorem W, Lemmas 1.1–1.5, Comp 1.6 | **SOUND** (scope wording D4; implicit shrinkings D5) |
| Cor 1.7 (constant ratio) | **SOUND** |
| Prop 2.1, Reduction 2.5, Prop 4.1, Comp 4.2, labels, novelty | (pending) |

## 1. Theorem 3.1 / Theorem 2.3 — SOUND

Independent checker `scripts/review_r258_cert63.py` (pure `fractions`, no sympy; reads only (M, r, xyz) from the JSON,
ignores the author's `fam/exps/L_M` metadata). Run: `uv run python scripts/review_r258_cert63.py 1500` — all PASS:
* (A) all 18 classes: identity 4xyz = n(xy + yz + zx) as polynomials in n over ℚ; integer-valuedness on n = r + Mt via
  Newton forward differences (complete for polynomials); positivity for n ≥ 63·2^10 + 1 by Taylor-shifting to
  n = 64513 + u and checking every coefficient ≥ 0 (stronger and cleaner than the author's Cauchy bound); for every M,
  v₂(M) ≤ 10 and ord_{odd(M)}(2) | 2520, so n_s mod M is periodic of period | 2520 on s ≥ 10; r ≡ 1 (mod 2^{v₂(M)}).
* (B) coverage: the 18 classes cover every s mod 2520 except **{0, 840, 1680}** — all ≡ 0 (mod 24), hence covered by the
  moving class. (See D1: the text says the ET part leaves "exactly s ≡ 0 mod 2520"; that is the z15_tree statement, not
  this certificate.)
* (C) moving class: c·n = 4abcd − a − b checked as a polynomial identity in Y (n = 63Y³ + 1), which is equivalent to
  4/n = 1/(abd) + 1/(acdn) + 1/(bcdn) after multiplying by abcdn. Integrality re-derived by hand: Y = 2^{8j}, j ≥ 1;
  2^8 = 256 ≡ 1 (mod 85) (ord₅2 = 4, ord₁₇2 = 8), and 4 | Y; so Y ≡ 1 (mod 85), Y ≡ 0 (mod 4), whence
  21Y + 64 ≡ 85 ≡ 0 and 63Y³ + 3Y² − 9Y + 28 ≡ 85 ≡ 0 (mod 85), both ≡ 0 (mod 4): 340 | both, for ALL j ≥ 1 (also
  checked over the unique residue Y mod 340). Positivity: 63Y³ + 3Y² − 9Y + 28 > 0 for Y ≥ 1. The author's algebra
  f = 340b − n = 3(Y² − 3Y + 9), f′ = 340c − 1 = 21(Y + 3), ff′ = 63(Y³ + 27) = n + 1700 = n + 4a²d, and
  (4abd − n)(4acd − 1) = 4ad(4abcd − b − cn) + n re-derived: correct.
* (D) explicit exact solutions for every s = 0..1500 (10 by bounded search for s ≤ 9, 62 moving, 1429 ET-only); at
  every s ≥ 10 EVERY applicable ET class (not just the first) was evaluated and verified exactly.
* (E) squares: (m − 1)(m + 1) = 63·2^s with gcd 2 forces 2^{s−2}v = u ± 1, uv = 63; the only solutions are s = 0 (n = 64,
  even) and s = 8 (n = 127²) — confirmed numerically for s < 400. 127² lies in D₁₂₇ (s ≡ 1 mod 7) whose formula is a
  genuine solution, and s = 8 < 10 is brute-forced anyway. T1 control: every non-divisor class has r a NON-square mod M
  (all 14 checked), divisor classes have r = 0.
* Unit-square point: at μ = 0, n → 64 = 8² at every odd place and n → 1 at 2, so n_μ is a square in Ẑ; every
  ET/divisor class has r a non-square or q | n (q odd, q ∤ 64), so none contains μ = 0 (consistent with (B): residue 0
  uncovered). The moving class does contain μ = 0, so it is genuinely outside the ET/divisor menu (and is visibly not
  polynomial in n: x = (n − 1 + 3Y² − 9Y + 28)/4).
* Context the author omits (not a defect of the proof): mod 840, n_s ≡ 1 (mod 168) and n_s ≡ 3·2^s + 1 (mod 5), so
  Mordell's classical identities already settle every s ≢ 0 (mod 4); only s ≡ 0 (mod 4) (n ≡ 169 mod 840) is
  "hard". Worth one sentence in Scope.

Defects:
* **D1 (MINOR)** Thm 3.1 proof (b): "ET/divisor classes alone leave exactly s ≡ 0 mod 2520 (`z15_tree.py …`)" is placed
  as if describing the certificate; the certificate's 18 classes leave {0, 840, 1680} mod 2520. Repair: "the 18 classes
  leave s ≡ 0, 840, 1680 (mod 2520), all ⊂ {s ≡ 0 mod 24}; (a larger z15_tree run leaves only s ≡ 0 mod 2520)".
* **D2 (MINOR)** Theorem 2.3 says "s ≡ 0 (mod 24), s ≥ 6"; effectively s ≥ 24 (s = 0 fails: c = 85/340). Repair: "s ≥ 24".
* **D3 (MINOR)** Thm 3.1 checker description "positivity (Cauchy bound below 63·2^10)": fine, but also state that
  n_s mod M is periodic only for s ≥ v₂(M) (max v₂(M) = 3 here), which is why the cut is s ≥ 10.

## 2. Theorem W (Lemmas 1.1–1.5, Computation 1.6) and Cor 1.7 — SOUND

Every lemma re-derived by hand:
* **L1.1.** 4/n − 1/x = m/(nx), so N = nx = n(n + m)/4. With g = gcd(y, z): mg = (N/y′z′)(y′ + z′), y′z′ | N.
  N(1) = 4^{J−1}(4^J + m) is prime to m (m odd), and N(Y) ≡ N(1) mod m once Y ≡ 1 mod m (shrink C), so m | y′ + z′.
  y·V = z·U with gcd(U, V) = 1 in ℚ[Y] gives y′ = U(Y)/gcd(U(Y), V(Y)) (U, V primitive in ℤ[Y]); that gcd divides
  Res(U, V) and depends only on Y mod Res — constant on a smaller C (Y ≡ 0 at 2, ≡ 1 at the odd part). The "d₁d₂ | N in
  ℚ[Y]" step (remainder R/(d₁d₂) has bounded denominator and → 0) is correct. Also m > 0 is forced (m/N = 1/y + 1/z > 0),
  which is used tacitly in L1.2's positivity.
* **L1.2.** Positivity of ρᵢ (no positive real roots of n, n + m; positive leading coefficients) ✓. ρᵢ ∈ ℤ[1/2] by the
  "only if" half of MENU_LADDER Lemma 2.1 (a p-adic limit argument; correct). m ≡ 3 (mod 4) since n ≡ 1 (mod 4) on C.
  For q | M: m ≡ −4^J (q), (m/q) = (−1/q), reciprocity with m ≡ 3 (4) gives (q/m) = 1; q ∤ m. Then
  (2/m)^{e₁−e₂} = (−1/m) = −1 ⇒ (2/m) = −1, e₁ − e₂ odd, and with m ≡ 3 (4): m ≡ 3 (mod 8). ✓
* **L1.3.** k + m ≡ 1 + 3 = 4 (mod 8), so N(0) = k(k + m)/4 is a 2-adic unit; dᵢ(0) ∈ ℤ_(2) (incl. d₃ = N/(d₁d₂),
  integer-valued since y′z′ | N) multiply to it, so each is a unit. Roots of n + m: v₂(α) = 2/D > 0 ⇒ each contributes
  −2/D; roots of n: v₂(α) = 0, v₂(1 − α) ≥ 0, total 2J. With n irreducible, νᵢ ∈ {0, 2J}. ✓
* **L1.4 (Capelli).** For X^D − a: reducible iff a ∈ ℚ^p (p | D prime) or 4 | D and a ∈ −4ℚ⁴. With a = −K, K > 0,
  v₂(K) = 2: p = 2 impossible (negative), odd p impossible (2 ≢ 0 mod p), so K = 4β⁴, v₂(β) = 0, and β = w/u gives
  u⁴ | 4c₀, u odd ⇒ u⁴ | c₀ ⇒ u = 1. ✓  m = 4c₀w⁴ − k is automatically ≡ 3 (mod 8).
* **L1.5.** Both cases re-derived (u ≥ v: a₁ ≥ m/2^{e+1}, a₂a₃ ≤ 2^{e+1}r, m | 2^e4^J + a₂²a₃; v > u: a₁a₃ < 2r,
  m | 2^e a₁²a₃ + 4^J). B(m) is decreasing in m, so the cut "first w with m > B(m)" is valid. E = 2J + 2 is the right
  range for |e₁ − e₂| since eᵢ ∈ [−2, 2J]. ✓
* **Theorem W assembly.** νᵢ even ⇒ 2δᵢ ∈ ℤ; e₁ − e₂ odd ⇒ some δᵢ = ½ ⇒ x has a factor of degree D/2 ⇒ L1.4. ✓
  Irreducibility of c₀Y^D + k for all D for the six pairs: −k/c₀ ∈ {−1/15, −33/31, −57/7, −1/63, −17/47, −9/55} is
  negative (no p = 2), not an odd perfect power, and k/c₀ ∉ 4ℚ⁴ (v₂ = 0). ✓
* **Computation 1.6 — replayed from scratch** (`scripts/review_r258_thmW.py`, no sympy). STRICT = exactly Theorem W's
  conditions (incl. e₁ − e₂ odd); LOOSE = any eᵢ ∈ [−2, 2J] (ignores the Newton-polygon structure). w-ranges in the
  bound agree with the author's (3, 5, 9, 5, 5, 5); 4 further odd w past the cut also scanned. Results: all six target
  pairs **0 STRICT relations**; controls (3,1) m = 11, (7,9) m = 19, (23,41) m = 51, (39,25) m = 131 only — exactly as
  claimed (e.g. (7,9): ρ = (7, 5/2) appears). Note LOOSE has 12 relations for (47,17) at m = 171 and for (55,9) at m = 211,
  so L1.3's Newton-polygon restriction is load-bearing there (it is proved, so fine).
  Superset claim for `z19_thmW.py`: it enumerates all (a₁, a₂, δ, placement) combos *without* imposing e₁ − e₂ odd
  (the `odd` flag is unused), i.e. a superset of the STRICT set — claim verified. It also iterates m = −29 for (7,57)
  (harmless; reported as such).
* **Cor 1.7.** ε = 4t − 1; dᵢ ∈ {λᵢ, λᵢn}; constant dᵢ integer, dᵢ = λᵢn needs v₂(λᵢ) ≥ 0 (value k·λᵢ at Y = 0), so
  ρᵢ ∈ ℤ, 2-power = v₂(t)-share + {0, 2J}. Odd q | t: (q/ε) = 1; 2 | t ⇒ ε ≡ 7 (8), (2/ε) = 1; t odd ⇒ all 2-powers
  even. (ρ₁ρ₂/ε) = 1 ≠ (−1/ε). ✓ (Rational t reduces to t ∈ ℕ near μ = 0 since odd q ∤ n there.)

Defects:
* **D4 (MINOR, scope overclaim)** §1 Setting: "(Every exponential-polynomial identity near μ = 0 has this form after
  reparametrisation …)" is asserted without proof and is false as stated for exponential polynomials with polynomial-
  in-s coefficients or other bases (s·2^s, 3^s, …). The theorem is about *root families* (x, y, z ∈ ℚ[2^{s/D}]) and the
  Scope paragraph's "constant-gap / constant-ratio exponential classes of any degree" must be read that way. Repair:
  delete the parenthetical or replace by "(rational functions of Y reduce to polynomials since integer values at
  Y = 2^t force the remainder to vanish; families involving other exponentials or s itself are not covered)".
* **D5 (MINOR)** L1.1/L1.2 use "Y ≡ 1 (mod m)" and "dᵢ(Y) ≡ dᵢ(1) (mod m)"; the latter needs Y ≡ 1 modulo m times the
  odd denominators of dᵢ. Both are achieved by shrinking C (μ = 0 stays inside); say so once.
