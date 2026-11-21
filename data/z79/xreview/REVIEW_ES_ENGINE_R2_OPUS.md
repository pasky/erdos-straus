<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="e2b129c9f">
A separate reviewer subagent was asked to review the changes in `git log e2b129c9f..`. Its request and review follow.

Request: review changes since e2b129c9f carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Round-2 review of notes/z79/ES_ENGINE.md and scripts/z79_* (changes since e2b129c9f). Verify that every new construction has genuinely moving A,u,t and cannot be imitated by a single fixed AP! Distinguish exact-depth G from unsifted mere ES and check the entire uniform sieve, multiplicities, algebra and falsifiers; check F closure and parameter growth. Return full review; do not write any files. For Python use ulimit -v 1000000; timeout 180 uv run --offline --no-project python -B ... .

Commit log:
commit 93da212cfb5bd93ae0d7f2577afd5d1087066274
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 15:19:54 2026 +0100

    z79 round 2: variable-base cyclotomics and exact growing divisor depth at a moving shift

 data/z79/es-engine/round2.txt |  4 +++
 notes/z79/ES_ENGINE.md        | 64 ++++++++++++++++++++++++++++++++++--
 scripts/z79_es_engine_r2.py   | 76 +++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 142 insertions(+), 2 deletions(-)

Review:
# Round-2 review of `notes/z79/ES_ENGINE.md` §§5–7 and `scripts/z79_es_engine_r2.py` (since e2b129c9f)

**Verdict:** the algebra is correct, and the sieve proof of Theorem G is sound (it is a standard argument). Scope and framing need fixes: the "exact depth" claim is overstated, and both "non-AP" stories are thinner than the note presents them. STATUS delta "none" and Triage DATA are appropriate. I wrote no files.

## What I checked

- **Replay:** `scripts/z79_es_engine_r2.py` reproduces `data/z79/es-engine/round2.txt` exactly.
- **F algebra:** `b²−b+2=(4z²−3z+1)(4z²+5z+2)` holds. Also `n+u=(u+1)(b^s+1)`, `Φ₆(b)|b^s+1` for s≡3 (6), `t≡4 (8)`, and n≡1 (840) since `v₂(b)=1`, s≥3 and 105|z. The triple and the Jacobi sign are correct.
- **G algebra:** the rectangle identities `n+u=rv(Kh−1)`, `r(Kh−1)=tu−1` and `t=(rs)²h−1` hold. The U₇ triple `(wf, tnw, tnwf)` sums correctly. `(A/n)=(−u/A)=−1` follows from 8|u and A≡−1 (u).
- **Packet:** with λ‖u, g at λ of order 2d and g≡−1 at u/λ, we get `g^i=−1` on 0≤i≤d only at i=d. Further:
  - v≡g (u) gives v≡−1 (M), hence M|s and n≡1 (M).
  - (s,r)=1 holds.
  - All T-primes are distinct and coprime to K.
  - The row is reduced: n≡−u (mod T) and n≡1−rs (mod K).
- **Sieve:**
  - g(l) is `1/(l−1)` off the modulus, `1/l` at T-primes (a condition mod l²), and 0 on K-primes, including 2.
  - The dimension-one bound is uniform, since ∏(1+1/(l(l−2))) converges.
  - f(δ/γ)>0 for δ>2γ, and β+δ<1/2 keeps the moduli D₀qe within the BV range.
  - Each modulus is repeated O(1/α) times; Siegel–Walfisz is used only for Σ_{q≡g (u)} 1/q.
  - The prime count X/(log X)^{2+o(1)} and the integer count X/(log X)^{1+o(1)} both follow.
- **Counter-row:** forcing b|L with b≡−1 (u) gives a depth-one word in the same unsifted row (script: b=359). So the sieve is genuinely needed for exclusivity.

## Substantive objections

1. **"Exact depth" holds only for divisors ≤ Y = X^γ.** The theorem body says so. But the §0 Result ("exact unbounded subproduct depth at one moving shift"), the §6 title ("exact subproduct depth at primes") and the §6 preamble definition of depth do not.
   - Above Y, L is only Y-rough, with up to (1−β)/γ prime factors and L≡g (u). A factor ℓ|L with ℓ≡−1 (u) is a depth-one word at the same shift.
   - I built one on the toy packet: `n₂=T·ℓ₁ℓ₂−72` with ℓ₁=226392132721751≡−1 (72) and ℓ₁>T. `check(n₂,72,ℓ₁)` passes, and n₂ is a Fermat probable prime to bases ≤13. So that n₂ has a depth-one word and also the depth-3 words below Y.
   - Global exactness at this shift would need L prime, which is a parity-type problem. The fix is to add "among divisors ≤X^γ" everywhere depth is asserted.

2. **The rectangle identity is decorative for G.** The proof only uses three things:
   - n≡−u (mod T) with planted residues;
   - (n+u)/T is Y-rough;
   - n≡1 (M) and 8|u.

   A plain CRT choice, n≡1 (M) and n≡−u (T), with the same sieve gives the identical theorem and a smaller modulus (no K). The r, s, h, K story and the remark that "A draws essential factors from both s−1 and Kh−1" add no mathematical content. G is a Halberstam–Richert-type rough-shift sieve with planted residues. The note should say so plainly and not present the rectangle as the mechanism.

3. **Parameter growth is very slow and not stated.** u ≤ exp(√log log X), which the note admits is sublogarithmic. Unstated: log v ≳ 2j log u and log K ≈ 2 log v, so the budget forces j ≲ (log log X)^{1/4}, i.e. **d ≪ (log log X)^{1/4}**. Only A and t move as powers of X.
   - The note misses a lemma that would support its own claim that u must move. A minimal subproduct equal to −1 contains no proper product-one subsequence, so depth ≤ D((ℤ/u)^×)−1. Hence growing d forces u→∞, and no fixed-u family can imitate G. Add this.

4. **F is the Round-1 template on a new rational curve.** With s≡3 (6), write `n−1=(u+1)b^{s−3}·b³`. Then `(u+1)b^{s−3}≡u+1 (mod Φ₆(b))` because b⁶≡1 mod Φ₆(b). I checked this numerically.
   - So every member lies in the classical Type II class n≡−u_z (mod A_z) with cube divisor b³, exactly Thm A's shape (h=0). "No class selection on k modulo A" and the §5 title "without the cofactor congruence" are misleading: the congruence holds automatically.
   - For fixed z, all s lie in one AP. The family avoids being a single AP only because of the artificial truncation s≤z.
   - The only gain over the trivial `b=4u−2, A=4u−1, t=4` family (verified) is that t moves too.
   - F has no prime count and no density. I would label it a reparametrisation of the surface ut=b²−b+2 (NULL/DATA), not a separate theorem.

5. **Minor:** "each n counted at most O(1/α) times" is actually *at most once*. A second q′<Y dividing n+u would divide L, contradicting roughness.

## Form issues

- **§0 Review line:** it cites only the Round-1 Opus review ("proofs accepted"), which reads as if Round 2 were reviewed. Add "Round 2: none — cross-review owed".
- **§0 Label:** the Round-2 label is buried in the Result sentence; there is no separate Label field.
- **§5 preflight:** the Z68_U7O Thm B / x²+y⁴ remark is irrelevant. Neither F nor G has an irreducible leading form, so Thm B is not engaged; the remark is noise.
- **§7 F2 row:** "start its dyadic blocks at X>2¹⁴¹" is an unexplained magic constant.
- **Script G toy:**
  - n is **composite** (I checked), while the theorem is about prime n. Requiring a probable-prime n would be trivial to add.
  - The neutrals are not ≡1 mod r (only gcd(r,s)=1 is asserted).
  - q is not in a power range.

  It is a consistency control only, which the note does say.
- **Other cross-references:** Z68_U7F Conjecture B (over all shifts) and WILD_ES §6 (all solutions) are correctly distinguished. G contradicts neither.

## Answers to the challenge questions

- **Moving A, u, t:**
  - G: yes. A and t move as powers; u moves (log X)^{o(1)}-slowly, and must move by the Davenport bound.
  - F: all three move with z, but each z-row is one classical Type II AP truncated by fiat.
- **Exact-depth G versus unsifted ES:** this distinction is real and correctly argued by the counter-row. ES itself is already trivial in the unsifted row via the rectangle word `A=rBL`.
- **Sieve, multiplicities, algebra:** correct.
- **Falsifiers:** pass, since both families are ≡1 (840) and sign −1 is impossible at odd squares.
- **F closure:** 1 is in the closure, but the family does not converge to 1, as the note correctly says. G does converge to 1 profinitely.

**Bottom line:** keep STATUS delta "none". Fix the scope in items 1 and 4 and the Review line before any export.
</code-review>
