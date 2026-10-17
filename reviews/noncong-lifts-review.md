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
