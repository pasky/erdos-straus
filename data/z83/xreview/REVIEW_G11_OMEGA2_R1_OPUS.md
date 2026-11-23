<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of Wave z83 Lane 3 (notes/z83/G11_OMEGA2.md). Scrutinize every sieve dimension, sifting limit, level-of-distribution hypothesis (literal match to the cited published theorem), Buchstab/Harman decomposition sign and numerical integral with extreme rigor; independently recompute the key numerical constants. Cap any replay at ≤15 min.

Commit log:
commit 0ce8a55618404da3ee16d124834773bdd0d22b11
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 03:05:39 2026 +0100

    Improve inert-factor cutoff and two-window levels using mixed Selberg and good-prime peeling

 data/z83/g11_omega2/bv.txt       |   5 ++
 data/z83/g11_omega2/complete.txt |   1 +
 data/z83/g11_omega2/example.txt  |   1 +
 data/z83/g11_omega2/pair.txt     |   1 +
 data/z83/g11_omega2/thin.txt     |   1 +
 notes/z83/G11_OMEGA2.md          | 106 +++++++++++++++++++++++++++++++++++++++
 scripts/z83_g11_cert.py          | 102 +++++++++++++++++++++++++++++++++++++
 7 files changed, 217 insertions(+)

Review:
**Verdict: ACCEPT with minor fixes.** I found no fatal error in substance in commit `0ce8a5561` (`notes/z83/G11_OMEGA2.md`, `scripts/z83_g11_cert.py`, `data/z83/g11_omega2/*`). Every certified margin replays, matches an independent floating-point recomputation, and the sieve logic checks out. Nothing here claims ES, and the scoping is correct throughout.

## Replay and independent recomputation
- **Replay:** `scripts/z83_g11_cert.py` ran with `ulimit -v 6000000` in about 87 s total; the largest run (`bv`) peaked at 185 MB. All five outputs match `data/z83/g11_omega2/*.txt` digit for digit.
- **Float check, my own quadrature** (H_h from its delay equation; J₁ by a closed-form inner integral; V by trapezoid steps on a 1/4000 mesh):

| quantity | certified bound | my float | consistent |
|---|---|---|---|
| 2H₂(1/a) vs J₁(a), a = .36325 / .407 / .433 | — | .220089 / .116961 / .069532 (two methods agree to 1e-6) | ✓ |
| Row A: C₃, C₇(≥6), C₇(≥4) | < .46553, .0028924, .336874 | .46482, .0028845, .33646 | ✓ (bounds sit above) |
| Row B: C₃, C₇(≥4) | < .27575, .20767 | .27440, .20732 | ✓ |
| Thin: lower / cost | > .420151 / < .419652 | .420151 / .417504 (float margin .0026) | ✓ |
| Complete: lower | 1.144583 | 1.144583 | ✓ |
| Complete: z82-style cost / peeled cost | 1.15639 / 1.14383 | 1.15618 / 1.14361 (cert-style); 1.14294 with the exact ½log | ✓ |

- **Not recomputed:** the root lower values .4717 and .4857 come from the z82 `arraytable` engine, already cross-reviewed, so I only replayed them. The engine is scale-free in its indices, so passing `2*(J+1)` as g in `pair` really does only set the top row, as the note says.

## Checks of substance (all pass)
1. **Mixed Selberg bound (3)–(4) is correct.**
   - The expansion h₂ = h₁ + Δ and the coprimality loss G₁(u)/∏(1+h₁) are sound.
   - The identity 1 + v = (1−g₁)/(1−g₂) holds, with v(ℓ) = e₇/(ℓ−3).
   - ∏(1+v) ∼ (C₁/C₂)√(bL), E[log n] = (b/2)L, and the constant e^{−γ}/C₁ (primes ℓ ≤ 7 included) are all right.
   - Using (t)₊ ≥ t is valid, including for u < 1.
   - Dimensions are right: 3/2 up to X^b, 1 from X^b to B, Selberg level B² = X^{τ′}.
   - Since F_{1/2} ≥ 1, the new factor 1/(τ′−b) never exceeds the old one. The other factors (A, √a, 2H₂) carry over unchanged from z82 (4).
   - The l-modified-law majorant uses (1−g₂)^{-1}, which is at least (1−g₁)^{-1}, so it is conservative.
2. **Pan Theorem 3 is cited literally.** Compared with `sources/window2/2501.16723.txt` Thm 3.1: bounded f, m ≤ x^{1−ε}, (m,q)=1 inside the absolute value, q ≤ x^{1/2}/log^B with B = 3A/2+17, maxima over a and y outside. Fixed classes of lR, weights independent of l, τ′ < 1/2. ✓
3. **Theorem C peeling is sound.**
   - Partition by the largest remaining good prime: the pin pays the top of its bin for level, the bottom for remaining size, and the top for the new maximum.
   - Earlier pins are omitted from the extra-root set; good-prime squares are removed.
   - C/2 < .35 ≤ t at every node, and the modulus exponents sum to at most τ.
   - V′ = (w−1)V(w−1)/(2w²) re-derives correctly, and the integer V stepping is a valid lower bound.
   - ½log(h/l) ≤ (h−l)/(2l), and all rounding goes outward.
4. **Theorem D:** switching via z82 (5) at the Pan level is legitimate. (5) bounds a superset (3-rough through X^a), a is a dummy that cancels in U*, and 3b > 1 forces h = 2. The gain over .4846 comes from the (1−t−v)^{-1} versus (1−t−v)^{-5/2} kernel.
5. **Companion theorem:** checked against the Lemke Oliver PDF (fetched).
   - Thm 1 is literal; P_r is squarefree with at most r distinct primes.
   - The quantitative ≫ x/log x comes from W(A,z) in (2.3) and §2.3, and Richert weights satisfy w ≤ 1.
   - Γ_G ≠ 0: G ≡ 2521 (a unit) at every prime dividing M, and G is odd.
   - The identities n+3 = t²+3·29², n+7 = t²+7·19², primitivity, and the j=1 factorization and hit at 3 are verified by the script.
6. **Friedlander–Iwaniec claims** match `fi09-hyperbolic-pnt.txt`: A(θ) "sufficiently close to 1", (6.10) D = x^{θ−1/2−ϑ−ε}, the 1/12−2ε level in §5, and Thm 5 being about T(x) = Σ r(p−4) log p.

## Required fixes (minor)
1. **Lemma scope mismatch.** The switched-cost lemma states 0 < b < min(a, τ′/2) globally, but Theorem D applies (2) with b = .433 > τ′/2. b < τ′/2 is needed only for (1). (2), as in z82 (5), needs only b < a and τ′/2 < a. Split the hypotheses per equation.
2. **Sedunova Thm 2 is misdescribed** as a "squarefree P₇" result. It counts ω(n) ≤ 7 (distinct primes), with no squarefree condition.
3. **Richert comparison label.** It is a method comparison and should be labelled Assessment, not PROVED. Its bound ">.14" is loose (the value is about .276), which is harmless but sloppy.
4. **Incomplete STATUS delta.** It names only the §1D row. The same quoted numbers (.057, D(.957), T₃⁻(.4846)) also appear at STATUS.md:178 (§2 item 6) and FRONTIER.md:1150. The orchestrator must update all three.
5. **Triage of the companion P₂ theorem.** It is a thin-subfamily observation, not a RECORD. It should go to the WAVES line or FRONTIER §6 only, which the delta already implicitly does.

## Form and critique
- The prose is extremely compressed: the screen paragraph's "(4,8–11,15–17)" references, run-on theorem headers, and the FI "r₄" naming (FI write r(n)). This makes hostile review harder than the mathematics warrants. §3 in particular would benefit from a short display of the recursion before (5)–(6).
- In the script, `complete()` has a comment "R=max(1,…)" that the code doesn't implement. `charge(C,R)` takes W, not R, and `peel`'s argument h is depth, which collides with the bin endpoint h in the note.
- **Significance:** these are modest internal-record improvements (.057→.07, .957→.9544, .4846→.455), plus a new D(.58) conditional for at most two factors. D(.58) is still a maximum-over-residue, EH-type hypothesis. §4 correctly refuses to use the BFI, Maynard, Lichtman and Pascadi fixed-residue results (3/5, 5/8, 66/107), since the CRT residue varies with the modulus pair.
</code-review>