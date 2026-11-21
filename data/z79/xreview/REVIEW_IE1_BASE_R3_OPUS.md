<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="e14e1f8e0">
A separate reviewer subagent was asked to review the changes in `git log e14e1f8e0..`. Its request and review follow.

Request: review changes since e14e1f8e0 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Round-3 review of notes/z79/IE1_BASE.md new §§10–13 and §0. Check positive face rigidity in a nonarchimedean ordered domain, CRT scope, integral rows and remaining locks, PA affine factorial-slope primitive odd-square specialization (including Type I/II gcd/sign and the PA versus true-arithmetic distinction), factor-contraction divisor lattice/precise least tests, field quotients, parameter-free quaternion descent and stable range, continuum-axis cardinal claim. Look for any fatal overclaim or missing hypotheses. Give concise full report, commit and verdict. Do not modify files or run unbounded computations.

Commit log:
commit 96dd1612f12c5e73deac5e44eb63ca6acb380a68
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 14:19:47 2026 +0100

    Split the zero-divisor fibre and realize prime-primary extraction at the bad prime shift

 notes/z79/IE1_BASE.md | 77 ++++++++++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 73 insertions(+), 4 deletions(-)

Review:
**Verdict: ACCEPT WITH MINOR FIXES.** I reviewed commit `96dd1612f` (`notes/z79/IE1_BASE.md`: new §0, §§10–13). I found no fatal overclaim and no missing hypothesis that breaks a PROVED claim. I checked every proof step by hand. I modified no files and ran no computations.

## What I checked

**§10: rigidity at the product fibre (correct)**
- Positivity spreads to the whole nonnegative orthant over the real closure: wherever all denominators are positive, each is at least `p/k ≥ 1/k`, so the positive set is both open and closed, and the orthant is convex.
- On each face `x_j=0` the right-hand side is the constant `k`. Restrict to a line and let one coordinate go to `+∞`: nonconstant terms tend to 0, so only constant terms survive. This works over nonarchimedean real closed fields too.
- Lines through the positive open are Zariski dense, so each `g_i` is constant on each face, with the same constant at the origin.
- Divisibility by each `x_j` gives divisibility by `x₁⋯x_l`, because each `x_j` is a nonzerodivisor. This holds coefficientwise.
- **Two-factor seed.** `e(P)=1+ρ(J)=1`. `C[U,V]/(1+UV)≅C[U,U⁻¹]`, so `P` is prime. Integrality comes from `ρ⁻¹(S)=B`, and the three positive `c_i∈B` would give `4≤3`.
- **2 and 3 at `P−1`.** `(U−a)/3` and `(V−m)/2` are arithmetic, so `U` is coprime to 3 and `V` to 2. `(U,V)=1` needs the optional row. The `|U−a|` lock is valid.
- **Product decomposition.** `I=I₂∩I_o` and `I₂+I_o=B` are correct.

**§11: slope seed (correct)**
- `C[X]/(1+JX)=C[1/J]`. The rows at `X` and at `P` are compatible because each pivot is a unit modulo the other. Both quotients stay domains through floors, spheres and rows, so both fields are correct.
- **Square specialization.**
  - `4d|J` holds because `d∈D<T`. `1+J/2` is coprime to `Jd`, `s²≡1+J mod Jd` (since `J²/4≡0`), and `z≡1 mod d`.
  - The coprimality of `s` to `M·∏F_i(0)` is correctly split into the part over `Jd` and the rest.
  - Divisibility of `G_i(n)` by `n` exactly when `F_i(0)=0` is correct, as is the "at least one, not all three" step.
- **Type I/II gcd and sign.**
  - Type I: `n|4w−1` uses `gcd(n,YZ)=1`. In Type II, `gcd(d',w)=gcd(n,w)=1`.
  - `U'=d'Y²/(Y+Z)>0`, `(d'Y−w)(d'Z−w)=w²`, `g|w`, and `−g` is a square modulo `d'`. The Jacobi computation checks out: `(l/d')=(l/n)`, `(−1/d')=−(−1/n)`, hence `(−g/n)=−1`.
  - One implicit step: `d'≡−n mod 8` in Type II needs `w` even. This follows from `2|g|w`; please state it.
- **PA versus true arithmetic.** This is handled correctly. The no-strict-square theorem is provable in PA, and `B⊨PA`. ES at odd squares is never used, and the nonstrict example `4/9=1/3+1/10+1/90` is correct.
- **Divisors at `H`.** Factor contraction gives exactly `{d, dX : d|J in B}`, and the lattice is the divisor lattice of `J` times a two-element chain. The least hits are `X`, or the full `r`-part of `J` (smaller than any `dX`). (Sep) for switches from `B` works through comaximality of `X` with nonzero scalars.
- **Exact limit.** The lock at `X−1` and the nonprincipal `(X−1,J)` are valid.

**§12 (correct)**
- The descent is standard Euler–Lagrange. The bound `n'<n` comes from `N(v)≤(n−1)²`, and `v=0` would force `n|p`. The level invariant `n+k≤m+1` is well founded. The bounded factorization alternative keeps the step uniform.
- Unit progressions: the CRT construction is correct, as is the claim of stable range one in `R/hR`.

**§13 (correct; the hypotheses are stronger than needed)**
- The 2-adic tree of comaximal cell products gives an ascending chain along each path with proper union. A maximal ideal can contain only the path cell, so distinct paths give distinct minimal primes over `hR`, without (Sep).
- Only comaximality of coprime elements of `B` inside `R` and nonunit primes are used. IOpen, discreteness and the domain hypothesis are unnecessary, which is harmless.
- The `L` extension correctly needs uniqueness of the maximal ideal above each prime (§8).

## Critique and challenges

1. **Scope nuance for STATUS (substantive).** The lock at `X−1` equals `(P−1−T!)/T!`. The 2–3 split also fails at `P−1−T!`, since every factorization is a scalar times a zero-marked element. So the remaining lock is still an affine expression in `P` with old coefficients, inside `B[P]`. Read alone, "every prime-primary least test at P−1 holds; the lock moves to X−1" could suggest the arithmetic near the bad prime is repaired. It is not. State this explicitly in the STATUS delta. The same applies to `|U−a|` in §10.
2. **§0 Review field is out of date.** It does not mention the Round-3 sections, yet Triage already says "RECORD (§11 supersedes §7)". Under the gate this must read "cross-review owed" until this review is recorded.
3. **Unclear STATUS wording.** "Global Bézout, full Farey and global (Sep) are still not tested by this non-forcing result" is confusing, because they do fail in the model. Better: "extractions needing them are not refuted." Also consider dropping the §7 clause to stay within the 6-line cap.
4. **Dangling reference.** "CRT gives the product stated in the question" points to an external prompt. Replace it with `S≅B/I₂×B/I_o`.
5. **Minor wording fixes:**
   - §11 says "(H,J)=(J) even when the image of J is zero", but the image of `J` is always zero.
   - The §11 Theorem says "(Sep) holds for coprime switches from B" without saying where. Add "at H"; it is in fact true for every `h∈B∪{H}`.
   - §10's "Equivalently compare degrees after clearing" is asserted without support. The limit argument is enough, so drop it.
   - §13 states "(Sep) and Bézout" in one place and "(Sep)" alone in another. Comaximality is all that is used.
   - The §0 Result phrase "zero-divisor split" is jargon. Say "coprime split of T! whose images are zero divisors in S".
   - §12 should mention that signs are encoded when packing the initial vector, as §9 does.
6. **Form.** The commit touches only the note, which is correct for a lane. No master-file corrections are owed, since nothing was refuted or downgraded.
</code-review>
