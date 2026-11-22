<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of Wave z82 Lane 2B (notes/z82/BCM_LDIV.md). Verify every model-theoretic/algebraic/valuation/order/induction step rigorously. Cap any replay at ≤15 min.

Commit log:
commit e1c7a866abc060edd7f17e9ab77cd33ef68a998a
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 19:45:57 2026 +0100

    Remove the quadratic search guard and give a parameter-free universal control

 notes/z82/BCM_LDIV.md | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)

commit 60fc7e74f48c3712a38d043255aba62d8d326904
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 19:45:19 2026 +0100

    Separate quadratic from affine divisibility search in a PA-host power cut

 data/z82/bcm_ldiv/matching.txt |  1 +
 notes/z82/BCM_LDIV.md          | 94 ++++++++++++++++++++++++++++++++++++++++++
 scripts/z82_bcm_matching.py    | 34 +++++++++++++++
 3 files changed, 129 insertions(+)

Review:
**Verdict: ACCEPT WITH MINOR FIXES.** I found no mathematical error in the four PROVED blocks, and the replay of the script passes. The fixes needed are about how the result is stated (scope, labels, wording), not about the proofs. One block (the `U₁` control in §4) is correct but adds very little.

Scope of the review: both commits in `main..`, read against z81 `FAREY_PROOF` §§2–5, 7, 10–15, z75 `BCM4_PUSH2` §§1–4 and z78 `IE1_UNITS` (§0 package, §§1–3).

**Replay.** `scripts/z82_bcm_matching.py` runs in a few seconds and its output matches `data/z82/bcm_ldiv/matching.txt`. I checked the band condition against `I_j`, the planted residue `−h/(pq) mod p` (which equals `−h_p/q`), and the four products: 594437 > 412163 > 338699 > 304679. It is only a finite check, and it is labelled EVIDENCE accordingly.

## Substance, checked step by step

**§1 (the quadratic divisibility test (Q) in a `T_g` schedule): correct.**
- **Bounds.** `A=L` lies in `C`, and `h ≤ H²` already follows from the binomial bound.
- **Reservoir.** If `r` primes of `S` divide `D∈C⁺`, then `r·log A ≤ log D < A/k` for every standard `k`. So only infinitesimally many primes of each band are used up.
- **Local test.** A hit forces `t | h`. Divisors of `h` are scalar, and the interval `(A²,4A²)` forces exactly two prime factors. Cancelling gives `t | h/t + Y`, which is equation (1). Residues of `S` mod `p` are distinct, so `q ↦ −h_p q⁻¹` is injective and each prime points to at most one partner. Divisibility by a scalar prime is exactly `w_p ≥ 1`, and the residue of `Y` is fixed when `p` first enters.
- **Digit count.** At most `E` bad partners per prime in each direction, so `n(n−1) > 2En` holds for `n = 2E+2`.
- **Other new primes.** Each must avoid `|S|−1` partner residues plus `E` chart roots, and `|S|+E < r`, so this is possible. The choice is made in PA for the whole batch, then combined by CRT in `B`.
- **Bands.** They are disjoint and move downward, since `1+3·2^{−j−2} < 1+2^{−j}`. So the hits form a decreasing sequence with no least element.
- **Single atom.** At `u=0` the gcd of `A` and `h` is 1, so there is no hit. Hits with `u ≥ 3A²` are all larger. Correct.
- **Affine scheme survives.** z81 §13 builds valuations and digits independently of the order host, so restricting the digits keeps the affine least scheme. There is no conflict with z81's affine or `(t+b)|G(t)` cases, because here the modulus `t` varies with a nonscalar slope `Y`. This answers z81's "full `L(Div)` unknown in `T_g`" negatively for one schedule.

**§2 (z78 BCM tower): correct, and a genuine sharpening of z78 §3b.**
- **No least divisor above `y`.** Divisors of `x_j` are units of the punctured ring, so they have the form `F*·t(λ)` with `λ ∈ [0, 2^{−j}]`. When `λ` is strictly inside that range, every `c·t(λ)` with `c>0` has `w>0`, so it lies in `M ⊂ D'`. The value fibre `F^{>0}·x_{j+1}` has no least element above `x_{j+1}`.
- **BCM bound at `P`.** For `w(b)=0`, the singleton content gives `c ∈ D₀` divisible by every ordinary prime, which is impossible in a PID. For `w(b)>0`, `x_j` divides `b`.
- **Transfer.** The resulting statement is first-order with bounded searches, so it transfers to elementary copies and to convex subrings containing `P`.

**§3 (residue surjectivity and infinite unit rank): correct.**
- Floors give `z ≤ t/H ≤ z+1/d` for every `d`, so the residues cover `k^{>0}`.
- The independence construction works: all odd prime factors of `a_i²−2` are new, `l_i ∤ a_j²−2` for `j>i` because `l_i | a_j`, and the valuations at the two places above `l_i` differ. `F ∩ ℚ(√2) = ℚ` holds when `√2 ∉ F`.
- The z78 consistency check is right: the localization gives the punctured ring `B°`, whose units modulo `F*` have rank 1.

**§4: correct, with one block of little value.**
- **Guarded induction.** Replacing composite `r` by a proper factor works because `r/2+1 ≤ r`. The prime case goes through (i) and (ii), and at `j=s` only the first two alternatives survive. The ES witness bound `2(s+1)^4` is right.
- **Definable-cutoff version.** Fine.
- **Least divisor ⇒ least failure is prime.** Fine.
- **The `U₁` control.** The decoding `m=⌊√v⌋` is unique, and `n=⌊v^{1/3}⌋ > C` with code `< 5n² < v`. But it follows immediately from two known facts: parameter-free least-`U₁` implies `IE₁⁻` by the standard least-counterexample argument, and `T_g` is already known to fail `IE₁⁻` (z81 §14, `Th(n)` fails for `n > C`). It is an explicit instance of a known failure, not a new separation. It should be relabelled as a remark or NULL rather than PROVED with emphasis.

## Fixes needed (form and scoping)

1. **§0 Result and STATUS delta are now out of date.** Commit 2 strengthens §1 to a single atom with no comparisons, `(A²+u)² | h+(A²+u)Y`, but §0 still says "on an interval" and "one t²|h+tY interval". Update both. Also say "in one `T_g` valuation schedule" rather than "in general".
2. **§0 Label is incomplete.**
   - §4 depends on z80 §§1,7,18 and z79 §4, and contains a CONDITIONAL (on ES in ℕ) Assessment; neither is listed.
   - §3 relies only on integer-part floors.
3. **§4 contains a confusing sentence:** "adding that scheme as specified there does not alter its numerical leastness question." As written it contradicts the line just before it, since adding `L(t>y∧t|h)` does give "least failure ⇔ least failing prime". Clarify what "that scheme" refers to, or delete the sentence.
4. **Screen paragraph:** "the z78 axis has a nonzero prime conductor under two old prime ideals" is unclear. Replace it with the exact obstruction: the axis prime `{w>0}` lies in maximal ideals over both 2 and 3, so z79 §8 `(Sep)` fails, and hence `IE₁⁻` fails.
5. **§3 Assessment wording:** "lies below just one maximal" should read "lies in a unique maximal ideal".
6. **Possible extra STATUS delta (optional).** §2 bears on the STATUS open item "`L(Div)` in a BCM+TS ES-countermodel". It sharpens z78's "fails `L(Div)`" to "fails plain `L(t>y∧t|h)` below every BCM bound at `P`, in all elementary copies and convex subrings containing `P`". Consider proposing this for the z78 row.
7. **§1 digit-placement paragraph:** the aside about reusing the Dirichlet line `(1,1)` is unnecessary, since the note then uses a separate free edge anyway. Drop it, or count the extra forbidden root `Y ≡ −1` inside `E`.

**Triage.** BARRIER-SCOPED is appropriate for §§1–3; the §4 `U₁` block should be treated as NULL. Cross-review is still owed, and the note correctly says so.
</code-review>