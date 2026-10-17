# R267 — hostile review of O257 NONCONG_LIFTS.md (non-congruential lifts, numerator-model laboratory)

Reviewer branch `side-agent/review-noncong-lifts`, merged `side-agent/noncong-lifts` at 3b74594d.
From-scratch code: `scripts/review_r267_*.{c,py}` (none of the author's scripts reused).
ES is OPEN; nothing reviewed proves ES or an infinite case of it.

## Summary verdicts (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Thm 2.6 (a), (b), (c) | SOUND (minor scope/wording defects D1–D3) |

## Claim-by-claim

### Thm 2.6 (§5) — x_{ℓ,2} lies in no witness class for 4 | k ≥ 8; k = 4 iff ℓ ∈ {3, 5}

**Re-derivation (independent, line by line).** Membership of the profinite point in the class of slice (θ, a, b, c)
depends only on the slice (d plays no role), and with m = v_ℓ(ab), H′ = kab/ℓ^m (ℓ ∤ k is needed here) it reads
II: e ≡ −1 (H′), e ≡ −2 (ℓ^m); I: e ≡ −1 (H′), 2e ≡ −1 (ℓ^m). So "no class" is genuinely over ALL slices
(unbounded a, b, c; d irrelevant). I re-derived every branch:
* Case 0: e ≥ kab − 1 > a + b ≥ e for k ≥ 4. ✓
* Case A, II: a + 2c = Lg, c(e+2) = L(g+b₀), Lh = e + 2 ≡ 1 (mod kab₀), Lh ≥ 3 ⇒ Lh ≥ kab₀ + 1; Lh = 2L(g+b₀)/(Lg−a).
  a ≤ Lg/2 ⇒ kb₀ + 1 ≤ 4 + 4b₀/g ⇒ b₀(k − 4/g) ≤ 3 (uses a ≥ 1); a > Lg/2 ⇒ (k/2)gb₀ < g + b₀, false for k ≥ 4. ✓
* Case A, I: 2a + c = Lg, 2e + 1 = Lh ≡ −1 (mod 2kab₀); 2a ≤ Lg/2 ⇒ 2kab₀ − 1 ≤ 2 + 4b₀ (false k ≥ 4);
  2a > Lg/2 ⇒ L(g+2b₀) > (k/2)Lgb₀ − 1, and since both sides are integers (k even!) g + 2b₀ ≥ (k/2)gb₀, false for
  k ≥ 8 (4gb₀ − g − 2b₀ ≥ 2b₀ − 1 > 0). ✓ (Note: the integrality step uses k even; see D3.)
* Case B: ℓ ∤ e forces ℓ^i | c; c₀e = a₀ + ℓ^n b₀; n = 0 is Case 0; n ≥ 1 is Case A for (a₀, b₀, ℓ^n, c₀) (all congruences
  used are implied), plus ℓ^{2i} | h from the full ℓ^{2i+n} congruence. ✓
* (b) k = 4: I re-ran every sub-branch (II: a = 1; g = 1 gives h(2c−1) ≤ 3 → (L,h,c) = (3,3,1), (5,1,2), h = 1 at c = 1
  gives b₀ = 0 (silently discarded in the text — fine); g ≥ 2 forces b₀ = 1, g(L−2) ≤ 3, L = 3, g = 3, fails mod 4.
  I: g = 1 ⇒ c = 1 ⇒ L + 1 = b₀(4Lt − 4t − 2L) ⇒ (L, b₀) ∈ {(3,2), (5,1)}; g = 2, b₀ = 1 impossible. Case B: h ∈ {3,1} (II),
  {5,3} (I), ℓ^{2i} ∤ h.) All ✓. The representative x = 17 checks.
* (c) x_{ℓ,2} mod L is a non-square unit class iff (2/ℓ) = −1 (other components are 1); a covering class of modulus
  H | L would contain the point. ✓ 4 | k is used only through the meaning of "complete"/T1, not in (a)/(b).

**From-scratch numerics** (`scripts/review_r267_x2.c`; two independent membership tests per slice — CRT-component
congruences and an explicit CRT representative x mod H with 128-bit products — 0 disagreements):
* a ≤ b ≤ 300, **every** k ∈ {4, 5, …, 32} (not only 4 | k), every odd prime ℓ < 60: for ℓ ∤ k the only hits are
  k = 4: (II/I, 1, 6, c = 1, e = 7) at ℓ = 3; (II, 1, 5, c = 2, e = 3), (I, 2, 5, c = 1, e = 7) at ℓ = 5 — exactly (b) —
  and k = 5: (II/I, 1, 3, c = 1, e = 4) at ℓ = 3. No hit at all for ℓ ∤ k, 6 ≤ k ≤ 32.
* ℓ | k (outside the theorem's hypotheses) there ARE hits: e.g. k = 12, ℓ = 3: (1, 6, e = 7), H = 72. So the hypothesis
  ℓ ∤ k is necessary, not cosmetic (see D1).
* a ≤ b ≤ 1000 for k = 4 and k = 8, ℓ < 60: see addendum below.

**Verdict: SOUND.** The proof is correct and complete; the mechanism is indeed the size inequality (Case A,
a ≤ Lg/2 branch for II; Case A, 2a > Lg/2 for I — the latter needs k ≥ 8 *and* k even, not b₀(k − 4/g) ≤ 3).

### Complete-level dictionary (§2.4) and "every Mordell-class prime is a square mod every 7-smooth level"

**Definition used (made precise).** k | L; L is *complete* iff every unit class r mod L that is not a square mod L
lies in some witness class with H = kab | L, i.e. r ≡ −e (mod H) (II) or re ≡ −1 (mod H) (I), e = (a + b)/c, c | a + b.
(d is irrelevant: every prime in such a class gives d = N/H ≥ 1.) This is what the text says; fine.

**From-scratch recomputation** (`scripts/review_r267_complete.py`, own covering enumeration over all (a, b, c) with
kab | L, own square test, numpy masks; T1 asserted: 0 covered square unit classes at every level):
* k = 4, all L = 4m ≤ 1600: 59 complete levels, **all 7-smooth** ✓.
* k = 4, all 7-smooth L ≤ 6000: complete ⟺ (3 | L ⟹ 8 | L) ∧ (7 | L ⟹ 24 | L), **0 rule violations** ✓
  (840 complete — Mordell).
* k = 8 (L ≤ 3200) and k = 12 (L ≤ 4800): **no complete level** ✓.
* Deficits at L = 105k / 210k: k = 8: 96/52; 12: 178/213; 16: 276/322; 20: 346/460; 24: 464/699 — **identical** to the text.

**"If" direction (PROVED claim).** Re-derived: for a rule-satisfying 7-smooth L put L₀ = 2^{min(v₂L,3)}·rad_odd(L); if
v₂(L) = 2 the rule forces 3, 7 ∤ L, so L₀ ∈ {4, 20} with v₂(L₀) = v₂(L); otherwise 8 | L₀. In both cases a unit is a
square mod L iff it is a square mod L₀ (odd ℓ: square mod ℓ^v ⟺ mod ℓ; 2: mod 4 when v₂ = 2 on both sides, ≡ 1 (8)
when v ≥ 3), and covering classes mod H | L₀ pull back. The base levels satisfying the rule are complete by
computation (my run includes all 16 levels 4s, 8s, s | 105). **SOUND.**

**Mordell-class squareness.** 𝓜 = {1, 121, 169, 289, 361, 529} mod 840 = squares of 1, 11, 13, 17, 19, 23; p ∈ 𝓜 ⟹
p ≡ 1 (8) and (p/3) = (p/5) = (p/7) = 1 ⟹ p is a square mod every 2^a3^b5^c7^d by Hensel. Trivially **SOUND**.

**Verdict: SOUND (CERTIFIED parts reproduced; "if" PROVED).** Defect D4 (logic of "k = 8 has none at all, because
already ℓ = 3, 5, 7 carry uncovered points").

### §1: Def 1.1, Thm 1.2, Prop 1.3, Prop 1.4

* **Def 1.1** — coherent; "with the same w′" makes the level a property of the pair (rule, w′). Fine.
* **Thm 1.2 (with gcd(p, M) = 1).** Re-derived. (i) The Dirichlet step is correct: progression p + M(t₀ + s·rad(kab)),
  first term coprime to the difference (primes of M: gcd(p, M) = 1; ℓ | kab, ℓ ∤ M: choice of t_ℓ). The parenthetical
  "ℓ = p does not divide kab by ET normalisation" is unnecessary (if p | kab the bad class for ℓ = p is t ≡ 0, which
  is excluded anyway) — harmless. Type I uses gcd(e, kab) = 1 from kabd = pe + 1 ✓. (ii) p ≡ s² (mod M), H | M, H even ⟹ s odd
  ⟹ the odd square s² lies in the witness class; the identity (abd, acdn, bcdn) / (abdn, acd, bcd) is valid for every n,
  so this is a parametric solution at n = s² — excluded by the local square-class obstruction. My
  `review_r267_complete.py` asserts exactly this local statement (no square unit class covered) at every level
  ≤ 6000 (k = 4), ≤ 3200 (k = 8), ≤ 4800 (k = 12): 0 violations. ET Prop 1.6 checked in the PDF ("For any odd perfect
  square n, f_I(n) = f_II(n) = 0", proof via the point equations, i.e. slice-local) ✓. **SOUND** (classical in
  substance, as the text now says).
* **Prop 1.3.** The k = 5 counterexample checks (1/(t+1) + 2/(2n(t+1)) = (n+1)/(n(t+1)) = 5/n for n = 5t + 4; 4 ≡ 2²
  mod 5). "Valid for infinitely many t ⟹ identity in ℚ(t)" ✓. Schinzel 2000 not accessible to me (no PDF in
  sources/); I rely on the O223 citation audit (DISCOVERIES (J)49 SHARP 2, (J)55). **SOUND (classical; Schinzel's).**
  The NEAR_SQUARE sentence after it is garbled — D5.
* **Prop 1.4.** All four coefficient comparisons re-derived (II←II λ = α, e = αe′ − β; II←I λ = α/e′, e = α/e′ − β;
  I←II e = 1, αe′ − β = 1; I←I e(α − βe′) = e′, λ = αe/e′). The α = 1 list is complete (I←I with δ ≠ 0 has no solution:
  δ > 0 makes 1 − δe′ ≤ 0, δ < 0 makes e < 1). Examples check: q = 37 (II, 1, 5, 2, d = 2, e′ = 3, N = 40) ↦ p = 13
  (I, same slice, e = 3, 13·3 + 1 = 40); q = 23 (II, 1, 6, 7, 1), p = 17, e = 7: (1, 6, 1) works, (1, 13, 2) needs 52 | 24.
  The "reselecting ⟺ (θ, e) ∈ Spec(p)" statement is a tautology once stated (fine, it is labelled algebra).
  **SOUND.**
