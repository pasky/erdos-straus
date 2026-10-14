# R212 — hostile review of O212 FOUR_SPECIFIC.md (+ BRAINSTORM/y4_*.md, AGENT_REPORT_O212)

Reviewer worktree branch `side-agent/review-four-specific`, merged `side-agent/four-specific` at c82ebf63.
From-scratch scripts: `scripts/review_r212_*.{py,c}` (none of the author's `y4_*` code reused).

## Summary verdicts
(filled in as the review proceeds; see per-claim sections)

| claim | verdict |
|---|---|
| Prop 1.1 / Cor 1.2 (T1 ⟺ M ≡ 0, 3 mod 4; M^□ at non-squares for all M) | SOUND (one sign typo in memo, D1) |

---

## C1. Prop 1.1 / Cor 1.2 — T1-bearing numerators

**Re-derivation.** Write ψ(g) = (−M/g) (Jacobi, g odd > 0, g ≡ −1 mod M, so gcd(g, M) = 1).
* M ≡ 3 (4): ψ(g) = (−1/g)(M/g) = (−1/g)·(g/M)·(−1)^{((M−1)/2)((g−1)/2)} = (−1/g)·(−1/M)·(−1/g) = (−1/M) = −1. ✓
* M ≡ 0 (4): O208 (∗) — re-checked: (4/g)=1, 8 | M ⇒ g ≡ 7 (8), odd ℓ | M gives (ℓ/g) = 1, (−1/g) = −1. ✓
* M ≡ 1 (4): ψ(g) = (−1/g)(−1/M) = (−1/g); odd g ≡ −1 (M) are g = 2Mi − 1, and g ≡ 3 or 1 (mod 4) as i is even or odd. Non-constant. ✓ (M = 9, 25: still fine since (9/g) = 1.)
* M = 2M′ ≡ 2 (4): g ≡ −1 (mod 2M′) leaves g mod 8 free (M′ odd); (M′/g) depends only on g mod 4·M′ through g mod 4 and g mod M′, while (−2/g) is 1 at g ≡ 1 and −1 at g ≡ 5 (mod 8). Non-constant. ✓
The set {g : ψ(g) = s} is a union of coprime classes mod 4M (ψ is 4M-periodic), so Dirichlet gives primes in either sign class when ψ is non-constant.

**Cor 1.2 (a), M^□ at odd non-squares n prime to M, every M ≥ 3.** Fix g mod 4M in the class −1 (mod M); (−M/g) =: s is then fixed. (n/g) = (n₀/g) = (g/n₀)·ε(g mod 4) with n₀ > 1 odd squarefree, gcd(n₀, 4M) = 1, so CRT + non-triviality of (·/n₀) + Dirichlet give a prime g ∤ 2n with **(n/g) = s = (−M/g)**, i.e. (−Mn/g) = 1, −n/M ≡ σ² (g). Q ≡ ±σ (g), Q odd, Q prime to n (CRT), Lemma 1.0 ⇒ M^□(n). ✓ SOUND.
*Note:* the memo `y4_t1_numerators` Cor 2(a) writes "(n/g) = −(−M/g)" — wrong sign (D1). The FOUR_SPECIFIC text only says "(Dirichlet)", so the main document is unaffected.

**Cor 1.2 (b), T1 for odd g when M ≡ 0, 3 (4).** Every prime ℓ | k² + MQ² (k² odd, gcd(k, M) = gcd(Q, k) = 1) with ℓ odd has ℓ ∤ MQ and (−M/ℓ) = 1, so every odd divisor g has (−M/g) = 1, contradicting ψ ≡ −1. ✓. Even-g remark: an even g ≡ −1 (mod M) needs M odd; for −M a discriminant the Kronecker symbol χ_{−M} is a character mod M (even when −M is non-fundamental, e.g. M = 27), χ_{−M}(−1) = −1, χ_{−M}(2) = +1 iff M ≡ 7 (8); hence even g are impossible for M ≡ 7 (8) and possible for M ≡ 3 (8) (M = 3: g = 2 | 25 + 3). ✓

**Converse (no T1 for M ≡ 1, 2 mod 4), explicit shots at odd squares** (prime g ≡ −1 (M) with (−M/g) = +1, Lemma 1.0
recomputed and verified in exact rationals, den(z) an odd square prime to n):
* M = 5, g = 29, n = 49, Q = 5: 5/49 = 1/11 + 1/294 + 25/3234.
* M = 9, g = 17, n = 49, Q = 15: 9/49 = 1/19 + 1/98 + 225/1862.
* M = 6, g = 5, n = 49, Q = 1: 6/49 = 1/10 + 1/49 + 1/490 (here even a genuine unit-fraction solution).
* M = 10, g = 19, n = 9, Q = 1: 10/9 = 1/1 + 1/18 + 1/18.
In `review_r212_t1.py` (3) this is done for every M ≡ 1, 2 (mod 4), 5 ≤ M ≤ 38, at 11 odd squares each: all succeed.

**Numerics (from scratch, `scripts/review_r212_t1.py`, < 1 s).**
(1) Jacobi constancy of (−M/g) on odd g ≡ −1 (M), g < 40M, for M = 3..80: constant −1 exactly for M ≡ 0, 3 (4); 0 mismatches.
(2) Brute force odd squares k ≤ 59, Q ≤ 29, all g ≡ −1 (M): odd-g shots = 0 exactly for M ≡ 0, 3 (4) (M = 3..40); even-g
shots occur exactly for M ≡ 3 (8) (3, 11, 19, 27, 35) and odd M ≡ 1 (4) — matches the memo's statement.
(4) Cor 1.2(a) construction carried out and verified for all M = 3..30, odd non-squares n < 400 prime to M (4275 cases).
(5) 11/37 = 1/8 + 1/148 + 49/296: exact identity ✓ (unit-fraction insolubility checked in C2).

**Verdict C1: SOUND.** The label PROVED is right; it is elementary and (as the author says) folklore-level — the
"discriminant" reformulation is just "χ_{−M} has modulus M and is odd". Minor presentational point (D2): Cor 1.2's "for
M ≡ 1, 2 (mod 4) the relaxation holds at squares too" should say "*the shot mechanism* reaches every odd square prime to
M"; M^□ itself holds at most odd squares for *every* M by non-shot solutions (SYNTHESIS_SPARKS3 Rem (o): 8/9).

---

## Defects
1. **D1 (MINOR)** `BRAINSTORM/y4_t1_numerators.md`, Cor 2(a): "(n/g) = −(−M/g)" must be "(n/g) = (−M/g)" (so that
   (−Mn/g) = 1). Repair: flip the sign.
2. **D2 (MINOR)** FOUR_SPECIFIC §1 Cor 1.2 last clause / memo Cor 2(c): "the relaxation holds at squares too" →
   "the M-shot family reaches every odd square prime to M (so the relaxation is shot-provable there)"; M^□ holds at most
   odd squares for all M anyway.
