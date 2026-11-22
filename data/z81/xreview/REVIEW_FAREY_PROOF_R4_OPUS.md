<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="149c22c10">
A separate reviewer subagent was asked to review the changes in `git log 149c22c10..`. Its request and review follow.

Request: review changes since 149c22c10 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile Round 2 Opus cross-review of notes/z81/FAREY_PROOF.md §§13–16 + §0 at f5dd1850a. Check PA compactness/Skolem hull preserving the non-PA cut, simultaneous archimedean host vs valuations, honest internal sorting of scalar and horizontal divisor lists (no identification of arithmetic integers with host integers), full Boolean affine-over-affine minimization including the exception-list complement and progression index argument, fixed (★) levels. Check shifted seed P=H+Jη, validity of actual short pair, higher-degree and later-edge gap, exact parameter-free Thue cut, BCM power-cut obstruction, −20 Gauss calculation and F1–F4. No pooling, no full L(Div) or IE₁ independence. No compute needed (≤15 min if any). Give specific corrections or downgrade if a substantive gap exists.

Commit log:
commit f5dd1850a0842cb49d0e4dd0396e853f0f3dd10e
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 16:29:09 2026 +0100

    Separate affine divisibility minima and repair the named Farey vector in fixed-cut towers

 notes/z81/FAREY_PROOF.md | 85 +++++++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 81 insertions(+), 4 deletions(-)

Review:
**Verdict: ACCEPT WITH FIXES.** I found no substantive gap in §§13–16, so nothing needs downgrading. The fixes below are about scoping, triage and wording. I worked from the diff `149c22c10..f5dd1850a`, which touches only `notes/z81/FAREY_PROOF.md`, and read §§1–12 for context. No compute was needed and I wrote no files.

## What I checked and accept

**§13 auxiliary PA host**
- **Skolem hull keeps C initial.** Item 1 is a pigeonhole over 2c+2 pieces, so the loss stays in C, and it handles every Skolem term. That makes the hull an elementary extension with C still initial. Item 2 loses at most half each step with c=16(c₀+1).
- **The new residue is transcendental.** An ordered extension of a real-closed residue field contains no new algebraic elements.
- **The Cauchy-host condition holds.** Host floors of scaled bounded elements land in C, by initiality.
- **Valuations are not mixed with the host.** The host only supplies an ordered field embedding. Valuations and CRT digits are built separately. Arithmetic integers are not identified with host integers except on B itself. (P is sent to the host integer z, but nothing uses that.)

**Sorting lemma**
- The bound τ(b)∈C is correct: τ(b)^m ≤ K·b holds in ℤ, hence in B, and then take m=i(j+1).
- The index lists are old because C is initial in D∞.
- A divisor is a scalar s dividing c(h) times one of finitely many horizontal δ of content 1. Monomial divisibility splits into a scalar-content test plus a horizontal test, since content is multiplicative and A is a UFD with units K*.
- Real-closed-field quantifier elimination makes order comparisons on the indices D∞-definable. Minimising by value order rather than index order is handled correctly.

**Affine filters and fixed-level (★)**
- The one-witness reduction m | aδ(s−s₀) ⇔ m′ | (s−s₀) is correct. A horizontal m′ forces s=s₀.
- (4ku−1)(4kv−1)=4kn+1 checks, and so does the complementary class −1 mod 4k.

**Affine-over-affine scheme**
- The identity a(ct+d)=cs+Δ is correct, and the atom is equivalent to: s | Δ, a | (s−b), a | (c+Δ/s).
- Outside the exception lists, every nondegenerate atom off its pole is false, so the complement can be read off from the lists.
- Within each cell, positive congruences define at most one coset. Negative congruences each remove at most one coset in the index coordinate. After splitting off the ordinary periods, the remaining periods are infinite, hence greater than j+1.
- Inspecting (j+1)(N+1) indices then yields at least N+1 survivors, which beats the at most N listed exceptions.
- The (t+b) | G(t) extension (via remainder G(−b)) is correct.

**§14**
- The seed hull check for P=H+Jη is correct.
- The degree argument works: in η the two entries occupy degrees 0–2 and 3–5, which do not overlap. The later-edge derivative induction carries over with scales ≥1.
- Both the late-edge (B) gap and the exact Thue cut are correct. For n>C, the Dirichlet task with N=n² gives B₀ of about n², which is much larger than √n. Neither primality nor reducedness is used.

**§15** The algebra is correct: j·d_i − i·d_j = j−i, any common divisor is ordinary, divides k! and hence 1, and Bézout then gives a lower bound by the product.

**§16** The −20 reduction is right: only [1,0,5] and [2,±2,3] are reduced. The mod-5 square and nonsquare check works because 2·(2v²±2vw+3w²) = (2v±w)²+5w².

**F-table** The arithmetic checks: 241=14²+5·3², 131=9²+2·5², 409=2²+5·9², and every class in 𝔐 is a unit square mod 5.

## Required corrections

1. **§0 Review line:** add "§§13–16 (f5dd1850a): Round 2 cross-review [this file]". At the moment §§13–16 look covered by the R1–R3 reviews, which never saw them.
2. **§13, first bullet: self-contradiction.** The bullet says "nor unrestricted searches 0<t<H₀ with a modular predicate are asserted". The later affine-over-affine PROVED block asserts exactly that for constant-modulus affine congruences. Reword to: "not asserted in this guarded item; for affine/constant-modulus predicates see the scheme below; arbitrary modular predicates not asserted."
3. **§14 "repair" is trivial, and the Thue cut supersedes it.**
   - Since a<3J<√P, the vector (a,1) is the trivial short vector for any residue below √P. Delete "not just removal of the old proof of nonexistence", or say plainly that the shifted residue is trivially short.
   - T_shift has Dirichlet lines, so the exact Thue cut already gives ¬Th(P) at the same prime. The degree argument is only needed for Dirichlet-free shifted variants; say so.
   - In the §0 Scope, "recentering P fixes the specific §8 vector" should read "…makes the §8 residue trivially short; Th still fails at P and at every n>C".
4. **Thue cut wording.** "Holds exactly for the nonnegative members of C" is false as written: Th(n) is vacuously true for every n<0, including n<−C. State it as "for n≥0, Th(n) ⇔ n∈C".
5. **Step 1, Δ=0 case.** Say explicitly that off the pole the atom is the constant truth value a|c.
6. **Triage for §15.** BARRIER-BROAD is overstated. §15 is an elementary no-go for one countermodel architecture (power cuts), not a new class of excluded ES proofs. It is the weak-ring analogue of lcm(1..H)≈e^H, cf. z75 §5. Use BARRIER-SCOPED (FRONTIER §6 line). §16's triage is unstated; it is NULL/Assessment, a classical computation.
7. **Connect §15 to §13 in the triage/assessment.** By §15, T_g and every power-cut variant lack BCM. So §13's fragment is a RECORD only for the PW+Lag+Bézout+(Sep) relaxation and cannot approach the BCM+TS+L(Div) target. The STATUS-delta clause should say "(power cuts never carry BCM, §15)" so it does not read as progress toward that target.

## Optional improvements

- **§9 compatibility table.** It has no T_g or T_shift columns. Its short-vector row cites only "§8, slope P/H"; add "§14 exact Thue cut: fails at every n>C".
- **STATUS delta.** The strongest new fact is the exact Thue cut: Th holds on C and fails at every n>C, and ¬Th is an E₂ set with no least element. It is more informative than "short vectors fail at P". Consider replacing that phrase within the 6-line cap.
- **"Square of the divisor count".** Each s determines r, so τ(c(Δ)) times an ordinary constant suffices. The square is harmless but unexplained.

## Scope check

The note does not pool T*, T_g and T_shift. §13's choice is correctly stated as incompatible with ξ: §10 refutes L(t>y ∧ t|h) exactly where T_g proves it. Neither full L(Div) nor IE₁ independence is claimed. ES, full L(Div) under BCM+TS, and IE₁⁻ versus ES remain OPEN, and the note says so.
</code-review>
