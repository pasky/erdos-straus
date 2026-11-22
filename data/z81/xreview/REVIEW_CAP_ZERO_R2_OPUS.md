<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="4221e82c3">
A separate reviewer subagent was asked to review the changes in `git log 4221e82c3..`. Its request and review follow.

Request: review changes since 4221e82c3 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Round 2 hostile cross-lab Claude Opus check of ONLY the post-R1 additions to notes/z81/CAP_ZERO.md: Corollary P (specified nonresidue), its counterpart under H, and Corollary S′ (density on the actual z80 ST profile). Verify proof, exact congruences, rho bounds, Z-range and novelty/scope. Check whether R1 fixes are sufficient as well. Return concise verdict. Please DO NOT write or commit ANY files yourself, including scripts, data or tmp files; parent records your returned text. Any Python use `ulimit -v 6000000; timeout 120 uv run --offline --no-project python -B` and ≤2 processes.

Commit log:
commit 899a29e3936bc5fa64c6c0e00cc33996301e7d2e
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 15:22:09 2026 +0100

    Prescribe the overflow prime via a smaller progression and test root three on the ST profile

 data/z81/cap_zero/probe.txt |  1 +
 notes/z81/CAP_ZERO.md       | 18 +++++++++++++++---
 scripts/z81_cap_probe.py    | 20 ++++++++++++++++++++
 3 files changed, 36 insertions(+), 3 deletions(-)

Review:
**Verdict: ACCEPT WITH FIXES.** Corollary P and its counterpart under H are mathematically correct. Corollary S′ is correct but oversold: its existence conclusion already follows from known almost-all-ES results. The R1 fixes are adequate for what R1 covered, but §0 was not updated for the post-R1 additions. I wrote no files.

## Corollary P — correct
- **Congruences:** all hold.
  - (s/q) = (−q/s) for any odd s when q≡3 mod 4, and (−q/s) = (p/s) = (s/p) = −1. So q | s^j+1 with j=(q−1)/2 odd.
  - If q divided both F_5 and F_13, then ord_q(s) | 2. That gives F_a≡1 mod q when s≡1, and F_5≡5, F_13≡13 mod q when s≡−1. So the collision is impossible.
  - F_a ≡ 1 mod 4 in both classes of s (a≡1 mod 4), and F_a ≡ 1−s mod s². Lifting changes p+q by −qs mod s², which is nonzero, so s∥K.
  - p∤F_a: ord_p(s) | 2a would have 2-part at most 2, but a nonresidue mod p≡1 mod 8 has 2-part at least 8.
  - qF_a | s^{aj}+1 because a and j are both odd and gcd(q,F_a)=1. Also h is odd, z has denominator s^{h−1} and the root is s^{(h−1)/2}.
- **Bound:** e = (aj−1)/2 ≤ 13(q−1)/4. Linnik at modulus 4s (a reduced class) gives e = O(s^L).
- **Replay:** I ran an inline check, nothing written. It covered 3,069 (s,p) pairs with s<200, p<4,000, including 65 lifts and 99 cases with a=13, plus 85 exact Fraction checks. The denominator was exactly s^{h−1} every time. The probe's case (4201, 23, 31, 13) checks out by hand: 31 | F_5 and 23² | 4232.
- **Slack (minor):** when there is no lift, h=j already works and gives cap (q−3)/4, which is exactly CAP_DOWN Prop 1.3. The lift is only needed when v_s(K) is even; for odd v_s(K)≥3, Prop 1.3 applies directly.
- **Novelty:** only the z75 planted carrier improves, from modulus 4s² and e ≪ s^{2L} to modulus 4s and e ≪ s^L. That is a constant change in the exponent. The "bounded root when s≤B" claim already followed from z75, and none of this beats any record. Triage it as METHOD/NULL, not RECORD.

## Counterpart under H — correct
- **Logic:** cap ≤ C plus H gives h ≤ 4C + log_s(p+1) ≤ J. Since s|K, p ≡ −m mod s, and for each h the divisors of s^h+1 hit at most τ(s^h+1) classes mod s.
- **Divisor bound:** taking N ≤ s^J+1 gives a union of at most s^{4c·log 2+o(1)}, about s^{0.28}, classes. That is well below the (s−1)/2 nonresidues.
- **Linnik modulus:** M·s = s^{2+o(1)}, so A is absolute.
- **Edge case:** certificates with c=0 are outside H's pattern. They are harmless anyway: an even h makes every odd divisor of s^h+1 ≡ 1 mod 4, so no m≡3 mod 4 exists.
- **Scope:** correctly stated (prescribed s, not a bound on e*). The condition p≡1 mod M is only decoration that makes the least QNR large; the cap lower bound does not use it.

## Corollary S′ — proof correct, framing oversold
- **Proof:** the profile parameters (T, w, M) match z80 §15. M = Z^{1/3+o(1)} and Mℓ₁ℓ₂ ≤ Z^{0.54}. TZ Thm 1.4 over ℚ, as quoted in z80 §3, gives a two-sided uniform relative error of exp(−c·log Z) at log T = (log Z)², and clean Z kills the exceptional term. The −4/9 class is reduced, μ ~ (1/4)·log log Z, and the second moment plus Chebyshev bound is fine. At a hit, (ℓ/p) = −1 and (K/p) = −1.
- **The substantive objection:** Vaughan's exceptional set is ≪ T·exp(−c(log T)^{2/3}) (cited in FRONTIER l.1158). The profile has population T·exp(−(1/3+o(1))(log T)^{1/2}), so integral ES (r=1) already holds for all but a relative o(1) of ST-profile primes.
  - The headline "on the actual z80 ST profiles… r=3 exactly (not merely a family…)" is therefore strictly weaker than what is known. The closing hedge ("in these specified windows") does not fix the headline.
  - The rate is also very weak: the exceptional fraction is only O(1/log log Z).
  - **Fix:** restate S′ as a method statement: the one-window S mechanism fires almost surely on the ST profile, consistent with ST's "fewer contacts not excluded". Cite Vaughan explicitly, and triage it NULL/METHOD.

## Form issues in the post-R1 additions
1. The §0 Review line says "ACCEPT in substance" via R1, but P, the counterpart and S′ came after R1. Mark them "R2 pending".
2. §0 Triage lists none of P, the counterpart or S′, and the proposed FRONTIER §6 deltas omit the counterpart. That belongs as a BARRIER-SCOPED entry, merged with H.
3. §0 Scope says "All integers n>1", but P, the counterpart and S′ concern primes only.
4. The Label should add effective Linnik for P and the counterpart, and fixed-modulus PNT/Mertens for S′.
5. In the Assessment, "Items 5–7: no average over the prescribed p" now contradicts S′. Add "except S′".
6. The F1 cell's "as T1 requires" points to CAP_DOWN's falsifier name, which is undefined in this note.
7. The probe floor-divides `K=(p+m)//4` without asserting 4 | p+m in its modular-only branch. This is harmless, since the maths guarantees it.

## R1 fixes
- Fixes F1–F8 and points 1–4 are incorporated and correct. Most notably, M now includes 2^(H+3), the scale Y was renamed, and H is applied to Theorem I's carriers.
- Point 5 (the "CAP_ZERO" name) was not addressed. It is acceptable to keep the path, but say so.
- Both review files still name `scripts/z81_xrev_cap_zero_opus.py`, which was renamed to `z81_cap_xreview_opus.py`. This needs an erratum or a pointer fix.
</code-review>
