# R257 — hostile review #1 of EXP_OPEN (O246), round 1

Reviewer: R257 (side-agent/review-exp-open). Author branch merged: side-agent/exp-open. From-scratch scripts:
`scripts/review_r257_*.py` (no z19_/z15_/z14_ imports).

## Summary verdicts
| claim | verdict |
|---|---|
| **Theorem 3.1 — ES for every 63·2^s + 1 (PROVED, computer-assisted)** | **SOUND** (from-scratch replay; MINOR D1) |
| Theorem 2.3 (moving-gap cubic Type II class, s ≡ 0 mod 24) | **SOUND** (MINOR D1) |
| Lemmas 1.1–1.5, Theorem W, Computation 1.6, Cor 1.7 | **SOUND** for the stated menu (MINOR D3 scope wording) |
| Prop 2.1 (cubic family for 3·2^s + 1) | **SOUND** (MINOR D2: "iff" wrong, class is larger) |
| Reduction 2.5 (II-ad limit algebra) | **SOUND** (algebra re-derived; used only as an EVIDENCE filter) |
| Prop 4.1 (windows at 297's μ = 3) | **GAP** (MAJOR D4: 19 ∣ m untreated; local⇒global step missing, repaired here for 19 ∤ m) |
| Comp 2.2, Map 2.4, Comp 4.2 | EVIDENCE, labels appropriate (not replayed) |
| Labels | appropriate except Prop 4.1 (PROVED → should be PROVED for 19 ∤ m + GAP, see D4) |
| Novelty of Thm 3.1 | Assessment: brief web search (3 queries) found no prior ES result for 63·2^s + 1 or any k·2^s + 1 family; non-exhaustive |

No FATAL defects. One MAJOR (D4, Prop 4.1 only — does not touch the headline). Repairs NOT applied: the author's last
commit (db1b591f) was ~10 min before this review finished, so the author is not quiet; defects forwarded instead.

## 1. Theorem 3.1 / Theorem 2.3 — from-scratch replay

`scripts/review_r257_cert63.py data/z19/cert63_et.json 1500` (pure Fractions; reads only the polynomial DATA of the
certificate). Output:
* Theorem 2.3: Type II identity cn + a + b = 4abcd verified as a polynomial identity in Y; the three factorisation claims
  (n + 4a²d = 63(Y + 3)(Y² − 3Y + 9), 4abd − n = 3(Y² − 3Y + 9), 4acd − 1 = 21(Y + 3)) verified.
  Integrality re-derived by hand: 340 = 4·85; for j = s/3 ≥ 2, Y = 2^j ≡ 0 (mod 4) and the numerators are ≡ 28, 64 ≡ 0
  (mod 4); ord₈₅(2) = lcm(ord₅ 2, ord₁₇ 2) = lcm(4, 8) = 8, so s ≡ 0 (24) ⇔ 8 | j ⇒ Y ≡ 1 (mod 85) ⇒ numerators ≡ 85,
  85 ≡ 0 (mod 85). So b, c ∈ ℤ for EVERY s ≡ 0 (mod 24), s ≥ 24 (for s = 0, Y = 1 fails mod 4: c = 85/340 — correctly
  excluded; s = 0 is handled by brute force). Positivity trivial (all of a, b, c, d > 0 for Y ≥ 1). Among j mod 8 only
  j ≡ 0 works (script: j ∈ [2, 10) → {8}), so the class is exactly s ≡ 0 (mod 24). **SOUND.**
* 18 classes: identity 4xyz = n(xy + yz + zx) verified for each; integer-valuedness on n ≡ r (mod M) verified by
  forward differences of p(r + Mt); positivity for n ≥ 63·2^10 + 1 verified by Taylor shift (all shifted coefficients
  ≥ 0, constant > 0 — stronger than the author's Cauchy bound); odd part of every M has ord(2) | 2520 (periods
  4, 7, 9, 10, 12, 14, 18, 24, 28, 140, 210), 2-part ≤ 2³ and r ≡ 1 mod the 2-part (consistent with n_s ≡ 1 mod 2^s).
  Hence n_s mod M depends only on s mod 2520 for s ≥ 10.
* Coverage: every s ∈ [2520, 5040) with s ≢ 0 (24) lies in some class → no uncovered residue. (The 18 classes even cover
  102 of the 105 residues s ≡ 0 (24); the three left are s ≡ 0, 840, 1680 (mod 2520), i.e. s ≡ 0 (mod 840) — consistent
  with the profinite unit-square point μ = 0.)
* Exact solutions with verified 4xyz = n(xy + yz + zx), all entries > 0, for every 0 ≤ s ≤ 1500 (62 moving, 1429 ET,
  10 brute force for s ≤ 9 with my own brute-force search).
* T1: 63·2^s + 1 = t² for s < 4000 only at s = 0 (n = 64, even) and s = 8 (127²). By hand: t ± 1 = 2A, 2(A + 1) with
  A(A + 1) = 63·2^{s−2}; consecutive integers with odd part 63 split as {63, 64} or {7·9 split…} — only 63·64 (s = 8)
  works. s = 8 is handled by brute force and lies in the divisor class D₁₂₇ (n ≡ 0 mod 127). No T1 tension.

**Verdict Theorem 3.1: SOUND** (computer-assisted proof replayed from scratch; minor wording issues D1–D2 below).
**Verdict Theorem 2.3: SOUND.** The class is genuinely outside the ET/divisor menu: x = 85b = (63Y³ + 3Y² − 9Y + 28)/4 is
not a polynomial in n = 63Y³ + 1, and the class contains s ≡ 0 (mod 840), which (as the replay shows) the 18 fixed-modulus
classes miss — consistent with EXPONENT_COVERING Cor 1.5 (63 + 1 = 4³, so n_s → 64 = 8² at every odd place and n_s → 1
2-adically as s → μ = 0: a profinite unit-square point, no ET/divisor covering).

## 2. Theorem W, Lemmas 1.1–1.5, Corollary 1.7 — re-derivation

Re-derived line by line:
* L1.1: m = 4x − n > 0 since 1/x < 4/n. Rav step correct; N ≡ N(1) = 4^{J−1}(4^J + m) (mod m) is a unit mod m because
  m is odd and gcd(m, 4^J + m) = 1. y′ = U(Y)/gcd(U(Y), V(Y)) and the gcd divides a fixed resultant-type integer R
  (R = AU + BV), so it depends only on Y mod R, constant on a smaller neighbourhood. Division argument d₁d₂ | N ✓.
* L1.2: positivity (factors with positive leading coefficient of n, n + m have no root in (0, ∞)) ✓; ρᵢ ∈ ℤ[1/2] by the
  q-adic limit Y → 1 (and m | ρ₁ + ρ₂ by closedness of m-ideals in ℤ_q) ✓; quadratic reciprocity step:
  q | M ⇒ m ≡ −4^J (q) ⇒ (q/m) = (−1/q)(−1)^{(q−1)/2} = 1 ✓ (q ∤ m since q | 4^J otherwise). Conclusion m ≡ 3 (8),
  e₁ − e₂ odd ✓.
* L1.3: N(0) = k(k + m)/4 is odd since k + m ≡ 4 (8) ✓; dᵢ(0) ∈ ℤ₂ by the 2-adic limit Y → 0, product a unit ⇒ each a
  unit ✓; root valuations: roots of n + m have v₂(α) = 2/D > 0 (contribution −2/D each), roots of n are units
  (contribution ≥ 0, total v₂(4^J/k) = 2J) ✓; n and n + m coprime and squarefree ✓.
* L1.4 (Capelli): −K, K = (k + m)/c₀ > 0, v₂(K) = 2: not a square (negative), not an odd p-th power (v₂ = 2), so only
  −4ℚ⁴, 4 | D ✓; β = w/u, u odd, u⁴ | c₀ ⇒ u = 1 ✓. Note D ≡ 2 (4) is also excluded (x irreducible) ✓.
* L1.5: both cases re-derived; the bound uses only a₁a₂a₃ = M and M ≡ 4^J (mod m), so it holds for ARBITRARY odd
  divisors aᵢ (any fixed-prime splits, any mixed sub-products). This is exactly what repairs the R253 D1 gap of EXP_105
  Cor 2.8: the 2-power exponents are now bounded by the Newton polygon (eᵢ ∈ [−2, 2J], E = 2J + 2), not by the piece
  shapes. B depends on m through r = M/m ≤ 1 + 4^J, but B(m) is decreasing and m increasing in w, so the cutoff is a
  genuine finite bound ✓.
* Theorem W assembly: νᵢ ∈ {0, 2J} (n irreducible), eᵢ ∈ ℤ ⇒ 2δᵢ ∈ ℤ; e₁ − e₂ odd ⇒ exactly one δᵢ = ½ ⇒ L1.4 ✓.
  Hypotheses checked for all six pairs: c₀ ∈ {15, 31, 7, 63, 47, 55} odd and 4th-power-free; k ∈ {1, 33, 57, 1, 17, 9}
  ≡ 1 (8); c₀ + k ∈ {16, 64}; c₀Y^D + k irreducible for all D (k/c₀ not ± an odd prime power-ratio, v₂(k/c₀) = 0 ≠ 2).
* Cor 1.7: ε = 4t − 1; n irreducible ⇒ dᵢ ∈ {λᵢ, λᵢn}, λᵢ ∈ ℤ_{>0} (2-adic integrality from n(0) = k odd), λ₁λ₂λ₃ = t;
  odd q | t ⇒ (q/ε) = 1; 2 | t ⇒ ε ≡ 7 (8); so (ρ₁ρ₂/ε) = 1 ≠ −1 ✓. (x/n constant forces an integer ratio: an odd
  denominator would have to divide n ≡ 4^J near μ = 0.)

**From-scratch finite check** `scripts/review_r257_thmW.py` (own divisor enumeration; superset: does NOT impose
m ≡ 3 (8) or e₁ − e₂ odd; `--strict` imposes them; `--wmax W` ignores the bound B and scans all odd w ≤ W):
* all six pairs: 0 relations (default, strict, and unbounded w ≤ 61).
* positive controls: (3,1) m = 11 (12 relations), (7,9) m = 19 (6), (23,41) m = 51 (4), (39,25) m = 131 (4) — identical
  counts to the author's data/z19/thmW.txt; nothing else up to w = 61.
The author's "superset" claim is confirmed independently (my enumeration is weaker than theirs and still finds 0).

**Verdict Theorem W + Cor 1.7: SOUND** for the stated menu (root families in ℚ[Y], Y = 2^{s/D}). Scope caveat D3 below.

## 3. Proposition 4.1 (windows at μ = 3 of 4^s + 297)

Re-derived: Y = 4^{(s−3)/D}, n = 64Y^D + 297 (irreducible ✓), N(1) = 361(361 + m)/4, m ≡ 3 (4) ✓; roots of n, n + m have
v₂(α) = −6/D, −4/D < 0 (when m ≡ 3 (8)) so all eᵢ = 0 ✓; m ≡ 7 (8): (2/m) = 1, so 2-powers are irrelevant ✓;
q | 361 + m, q ≠ 19 ⇒ (q/m) = 1 ✓. So the LOCAL statement is right: *if 19 ∤ m*, any Rav decomposition near μ = 3 must
carry 19 to an odd power in ρ₁ρ₂.
Two holes (defect D4, MAJOR):
(a) **19 | m is not treated.** Then N(1) = 361(361 + m)/4 is not prime to m and the Lemma 1.1 step "m | y′ + z′" fails
    near μ = 3 (only m/19^α | y′ + z′ survives, and m/19^α may be ≡ 1 (4), killing the Jacobi argument). This case is not
    vacuous at the limit: 4/361 = 1/95 + 1/3610 + 1/3610 has m = 4·95 − 361 = 19.
(b) **Local ⇒ global step missing.** The proof shows a property of the Rav divisors on a small neighbourhood C′ ⊂ C of
    μ = 3, but every small neighbourhood already lies in {s ≡ 3 (9)}; the claim "C ⊆ {s ≡ 3 (mod 9)}" is about the
    whole class C and needs an argument at points of C far from μ = 3.
Repair of (b) for 19 ∤ m (R257, checked by hand): fix primitive integer normalisations of the irreducible factors;
then dᵢ = λᵢ·(factors), and at a *generic* point s ∈ C (19 ∤ n(n + m), i.e. 4^{s−3} mod 19 ∉ {1, c}, c the root of
n + m mod 19) every factor value is a 19-unit, so v₁₉(dᵢ(Y)) = lᵢ := v₁₉(λᵢ), l₁ + l₂ + l₃ = 0; at Y = 1 only the
n-factor (value 361) and nothing in the x-part (19 ∤ (361 + m)) carries 19, so v₁₉(ρ₁ρ₂) = l₁ + l₂ + 2[n ∈ d₁d₂].
Jacobi forces this odd ⇒ l₁ ≠ l₂. As rational functions y = g d₁, z = g d₂, g = d₃(d₁ + d₂)/m, so at a generic point
v₁₉(z) = l₃ + l₂ + min(l₁, l₂) and v₁₉(y) = l₃ + l₁ + min(l₁, l₂); the one with the larger lᵢ has valuation
min − max < 0 — not integral. So C has no generic points; since 4^{s−3} mod 19 runs through the subgroup of μ₉ generated
by 4^L, which has ≥ 3 elements unless 9 | L, this forces 9 | L, i.e. C ⊆ {s ≡ 3 (9)} ✓. Constant ratio x = tn with
19 | ε = 4t − 1: pairs (λ₁n, λ₂) would need λ₁n + λ₂ ≡ 0 (19) for ≥ 2 values of n mod 19 (n ≡ 7Y^D + 12 is injective in
Y^D), impossible since 19 ∤ t; pairs (λ₁, λ₂) die by Cor 1.7's Jacobi argument — fine, but should be said.
(a) remains open: I found no quick argument for 19 | m.
**Verdict Prop 4.1: GAP** (sound for 19 ∤ m after the repair above; 19 | m unproved). The "Consequently…" sentence and
the *Reading* paragraph inherit the gap.

## 4. Prop 2.1, Reduction 2.5
* Prop 2.1: identity re-derived (3Y³ + 81 = 3(Y + 3)(Y² − 3Y + 9), 320d − 1 = 21(Y + 3)); `scripts/review_r257_prop21.py`
  verifies 4xyz = n(xy + yz + zx), positivity and integrality for s = 36, 72, …, 2124. But 7 | Y² − 3Y + 9 ⇔
  (Y − 1)(Y − 2) ≡ 0 (7), i.e. Y ≡ 1 OR 2 (mod 7): the integrality set is j = s/3 ≡ 0, 4 (mod 12) (script: j ∈ [6, 30)
  → {12, 16, 24, 28}), i.e. s ≡ 0, 12 (mod 36). Statement (sufficient direction) is correct. **SOUND** (D2).
* Reduction 2.5: (4abd − n)(4acd − 1) = 4ad(4abcd − b − cn) + n = n + 4a²d ✓; roots of B are 2-adic units since k + T is
  odd ✓; dividing jj′q² − jq − 4^J j′q = 4a²d by q = a₁d₁ gives jj′a₁d₁ = 2^E a₁ + j + 4^J j′ ✓; j = j′ = 1, k = 1:
  T = z(z + c₀ + 2), (1 + T)/c₀ = u^p ⇔ c₀(u^p − z) = (1 + z)² ✓; (63,1): z = 20, 441/63 = 7, 27 = 3³ ✓. **SOUND**.

## 5. Defects

**D1 (MINOR) — Theorem 3.1 proof (b) and Theorem 2.3 statement.** (i) "(ET/divisor classes alone leave exactly
s ≡ 0 mod 2520, `z15_tree.py …`)": the 18 certificate classes leave s ≡ 0, 840, 1680 (mod 2520) uncovered among
s ≡ 0 (24) (replay) — harmless since the moving class takes all s ≡ 0 (24), but the sentence reads as a statement about
the certificate. *Repair:* "(the certificate's 18 classes in fact cover all s ≢ 0 (mod 840); a larger z15_tree supply
leaves only s ≡ 0 mod 2520 — EVIDENCE)". (ii) Theorem 2.3 "s ≡ 0 (mod 24), s ≥ 6": replace by "s ≥ 24" (s = 0 fails:
c = 85/340). (iii) Scope line "the integer square 63·2^8 + 1 = 127²" — fine; add that s = 0, 8 are the only squares (A(A+1)
= 63·2^{s−2} forces {A, A+1} = {63, 64}).

**D2 (MINOR) — Prop 2.1 proof.** "7 | Y² − 3Y + 9 iff Y ≡ 1 (mod 7)" is false (Y ≡ 2 also). *Repair:* "if Y ≡ 1 (mod 7)
(the exact integrality class is s ≡ 0, 12 mod 36)"; also "s ≥ 18" → "s ≥ 36" (or s ≥ 12 with the enlarged class).

**D3 (MINOR) — Theorem W setting/scope.** "(Every exponential-polynomial identity near μ = 0 has this form after
reparametrisation…)" is an unproved remark; it is really the *definition* of the menu (ℚ-polynomials in a single
Y = 2^{s/D}). Families using other bases (3^s), s-polynomial coefficients, or non-polynomial parametrisations are not
covered. *Repair:* replace by "We call a family of this form a root family; the results below concern only this menu",
and in *Scope* say "constant-gap / constant-ratio root families in ℚ[2^{s/D}]".

**D4 (MAJOR) — Prop 4.1 proof (and the "Consequently …" / *Reading* sentences).** See §3: (a) the case 19 | m is not
handled (Lemma 1.1's coprimality N(1) ⊥ m fails; not vacuous at the limit, 4/361 = 1/95 + 2/3610 has m = 19);
(b) the passage from the local Rav structure near μ = 3 to the global "C ⊆ {s ≡ 3 (mod 9)}" is not argued.
*Repair:* add the generic-point 19-adic valuation argument of §3 (proves the claim for 19 ∤ m, incl. constant ratio),
and either prove the 19 | m case or add the hypothesis 19 ∤ m to the statement (label: PROVED for 19 ∤ m; 19 | m OPEN).

**D5 (MINOR) — Lemma 1.2 proof.** "Y ≡ 1 (mod m) on a neighbourhood gives m | ρ₁ + ρ₂": the dᵢ may have coefficients
with denominators divisible by primes of m, so congruence mod m of dᵢ(Y) and dᵢ(1) is not literal. *Repair:* say "by
q-adic continuity (Y → 1 in ℤ_q, values in ℤ_q, and q^v ℤ_q closed)".
