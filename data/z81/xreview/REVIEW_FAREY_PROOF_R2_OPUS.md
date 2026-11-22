<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile second Claude Opus review of z81-farey-proof, particularly additions §§7–11 of notes/z81/FAREY_PROOF.md at d44491830 and fixes to R1. Audit the moving-cohort sphere valuations (joint avoidance, first dyadic branch, precision up to all d∈C, prime and ES persistence), PW, Lag and internal Dirichlet WITHIN the power cut, restricted-height error gap (B) at P, choice of fresh residue ξ in closure of divisors of h≤H³ giving no least hit, coinitial bad-prime optional queue and order/positivity during replay. Verify §1's parameter-free Pell descent, falsifier table and top summary with no pooling. Return concrete corrections, including scope or missing hypotheses. No compute necessary; cap any computational replay to ≤15 min.

Commit log:
commit d444918305348e826ce59528bb8ad440a58038b2
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 15:01:25 2026 +0100

    Add fixed-cut four-square and prime tasks; locate internal Farey and least-divisor failures

 data/z81/xreview/REVIEW_FAREY_PROOF_R1_OPUS.md | 106 +++++++++++++++++++++++++
 notes/z81/FAREY_PROOF.md                       | 100 ++++++++++++++++++++---
 2 files changed, 193 insertions(+), 13 deletions(-)

commit 2a54bd0dfc5e07cab47a2975fb70a911b64c6777
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 14:32:09 2026 +0100

    Combine Bézout and supplied Pell windows at an ES-failing prime via a fixed subpower cut

 notes/z81/FAREY_PROOF.md | 90 ++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 90 insertions(+)

Review:
**Verdict: ACCEPT WITH FIXES.** I found no mathematical error in §§1–11 that breaks a theorem. The problems are pooling of model variants, a ladder that contradicts §11, missing explicit hypotheses, and triage. Nothing in the note claims ES, and ES remains OPEN.

I did no compute beyond about 1 minute of sympy: the §9 identity below and the §10 tail bound both check.

## Verified (hostile pass)

**§1 Pell descent.** It is correct.
- Parity and the coprime-square split are fine, and the factor coprimality holds in Bézout domains: gcd(a,z)² = gcd(a², ab) = a.
- In the descent, w² = (u+1)/2 gives 1 < w < u, and w stays above 1 at every step.
- In the induction block, the certificate "w ≤ u−j" strictly decreases, and at j = u only the negative solution can remain. The bounded witnesses and the openly-invalid and composite escapes are all fine.
- The step from short vectors to norm p is right: a² + b² ≤ 2p cannot be 2p, because p is a nonsquare prime.

**§4 flag.** With t above D₁, L = t! and H = 2^L, we get D₁ ⊂ C, L ∈ C, and d | L for every d ∈ D₁⁺. The specialization only needs q odd and L² ∈ C. The three CRT conditions and the "4 > 3" strictness are correct.

**§7 moving cohort.**
- **Entry bound.** The isotropic vector, the UV + q split, degree ≤ 3E+1, and U ≠ 0 giving a smooth nonzero point (also at s̄ = 0) are all sound. PA proves the existence uniformly for each standard E, so PA can choose points for a nonstandard set of new primes.
- **Dyadic branch.** Rychlik gives r ≡ x₀ (mod 4). The PA root is ≡ x₀ (mod 4), so v(r+x) = v(2) and v(r−x) ≥ v(8D⁴d) − 1 ≥ v(d). Both PA roots x and x + 2^{N−1} work.
- **Frozen values.** Values below M_e·v_l(D) are preserved, because the next modulus is divisible by D^{M_e+1} and coordinate moves are at least that large.
- **Avoidance.** New primes avoid all tasks ≤ m and give them value 0, which is the baseline. Later rotations move centres by valuation ≥ 1, so that value is kept.
- **Other checks.** The look-ahead thresholds, the PA scalar profile gcd(b, D^{M_e}), the invariant-2 precision and the sandwich with a loss in C all check out.

**§7 Lag and Dirichlet within the cut.** Sphere coordinates are bounded by √s. For Dirichlet, H′ is at most a constant times (H+|a|+|N|+1), so both Y and the new prime a+mY lie in the cut. Primitivity comes from digits 0/1, and the prime is a geometric prime, hence prime in T by Bézout.

**§8 gap (B).**
- At the seed, every nonconstant element has size ≥ H/c, so in-cone entries are scalars. Transcendence of θ̄ then gives error ≉ 0.
- On free lines and rows, the k-th derivative test keeps the pair in the cone because the scales are ≥ 1. On spheres, the weights s^{deg/2} are ≥ 1.
- The Farey and reduction arithmetic checks: |x−θY| ≤ 2/√P; |V| ≤ (4/3)^{1/4}·S < 2S; |U−θV| < 4/S.
- I also checked that (B) does not clash with the §10 approximants. The pairs (∏(s_i+1), ∏s_i) have error about 1/s_next, and 1/s_next is still above 1/c for c = s_next ∈ C.

**§10.**
- h ≤ H³, and each d_J divides h.
- The cofinal sequence s_{i_j} ≤ k exists, because s_{k+1} > √H.
- The tail after s is at most 1/(1−s⁻²) < 1 + 1/s, so distinct digit sequences are separated by a positive element of F.
- The upper divisors exceed P. Any scalar divisor t > P has residue ≠ ξ, so a late upper divisor lies strictly between P and t.

**§11.**
- The replay over K(q) is valid, and A[q] ∩ K(q) = K[q].
- Positivity is clopen and semialgebraic on intervals with endpoints in rc(K), so it does not need q to dominate K. The square-CRT step applies to the specialization at q.
- Under ES in ℕ, every member of C has its witnesses in C. So any failure lies above C, and the queue puts a smaller failing prime below it.

**R1 fixes.** All eight are applied, except that the file name is unchanged and triage is still HEADLINE.

## Corrections required

1. **Pooling of variants.** The note builds at least these models: T₀ (with L = 840 or flagged), T₊, the §10 seed-choice variants T^ξ, and the §11 queue T₊^{ξ,Q}.
   - The Result line, the Scope line, the STATUS delta and the ladder merge them. For example, "a power cut has … Lag …" is true only of T₊, and "A seed choice also refutes L(Div)" is true only of T^ξ.
   - "P≡1 (d) ∀d∈D₁⁺" and non-vacuous factorial strings need the flag.
   - Fix: name the variants. Add an explicit one-line compatibility lemma: the flag, the §10 residue and the §11 queue can be imposed together on T₊. §11's "rel. §§2–10" implies this but never states it. Then quote properties per named model.

2. **§9 ladder.**
   - The row "Numerical leastness … not tested" contradicts §11. Replace it with: T₀ UNKNOWN; T₊^{Q} FAILS, CONDITIONAL on ES in ℕ, and holds with a standard least member otherwise; IE₁⁻ not addressed.
   - Change "L(Div): FAILS with §10 choice" to "UNKNOWN for generic θ̄; FAILS in T^ξ".
   - Add a row "TS / −1 a square mod P: FAILS in both". For T₊ this needs the sentence that T/PT embeds in R/PR (quotients are bounded) plus the z80 §10 regularity argument on the P fibre. Today it appears only as a parenthesis in §10.
   - Add a row "§1 at other horizontal primes: UNKNOWN", with a caveat that it is not vacuous in general. At radicand P²+4 (≡ 5 mod 8), X = (P³+3P)/2 and Y = (P²+1)/2 lie in T and satisfy X² − (P²+4)Y² = −1 (checked symbolically). The vacuity in §9 is special to P and to primes born linear (q-lines, Dirichlet primes, P+j), where K[√ℓ] is a polynomial ring.

3. **§0 Label.**
   - §11 is CONDITIONAL, so the label must be composite.
   - "rel. … the fixed-cut refinements below" is circular; drop it.
   - Add Hensel–Rychlik and henselization, z80 §§9.1–9.3 and §17.
   - In the Scope line, "(§8)" also covers BCM, which is proved in §5.

4. **STATUS delta.**
   - Name the target row. The z75–76 row already has IOpen + Lag + full supplied-unit PW + ¬ES(P), so the novelty is PW together with Bézout, global (Sep) and internal Dirichlet in T₊, not PW + Lag + ¬ES.
   - The z80 row is already 5 lines, so this addition has to be compressed.
   - Say "(external) z80 §1 factorial-string conclusion", not "passes the test".
   - Suggested text: "z81 (separate, `notes/z81/FAREY_PROOF.md`): a power cut T₊ has IOpen+Bézout+(Sep)+Lag+internal Dirichlet+full supplied-unit PW, ¬ES(P), P≡1 (d) for all d in a nonstandard PA cut, and the z80 §1 factorial-string conclusion over every non-initial PA subring. It has no cofinal PA subring, and fails prime short vectors already at P (slope P/H), full Farey, variable reduction, BCM, TS and IE₁⁻. A seed-residue choice also fails L(Div)."

5. **Triage.** HEADLINE should become RECORD, as a row qualification. This is a new combination inside a listed relaxation, and it dies at the same first Farey rung as z80. For Screen 18, phrase the test generally: "Dirichlet approximation for in-model ratios of size about 1, e.g. P/H with a scalar H comparable to P".

6. **§7 presentation.** The mathematics is fine, but these hypotheses are only implicit and should be stated:
   - Every prime of C eventually enters, because every d ∈ C⁺ is requested.
   - The primes that never enter are exactly the PA primes outside C, and they are all odd, so the multiplicative baseline applies there.
   - Residue fields at entered primes are F_l by the old invariant 2. This is what justifies the phrase "internal PA prime field".
   - Rewrite the step as a numbered algorithm: new modulus D′ = D^{M+1}·d·(look-ahead factorial); cohort; avoiding centres; rotation with parameter D′; freeze. This replaces the three alternative phrasings ("Equivalently expand D first…", "More explicitly…").
   - Drop "choose the best residue", which is unnecessary.

7. **§8 minor fixes.**
   - State that a/P is reduced (P prime, 0 < a < P), which is needed for z79 §4's exclusion of the exact branch.
   - Change "C unit" to "F-relative unit".
   - ≪_C is non-standard notation; define it as "C·|x| < H".
   - Note that the §4 row order u = bHη′ uses the global H as its scale.

8. **§10 hypotheses.**
   - The Cauchy host must contain the limits of F-Cauchy ω-sequences; F has countable cofinality via s_{i_j}.
   - The old residue field is countable because B is.
   - The construction needs H = 2^N with N nonstandard; the flag supplies this, plain L = 840 does not.
   - "Infinitely many ones" is redundant, since transcendence already excludes finite sequences.

9. **Notation collisions.**
   - q is the specialization value in §4 and the new prime in §11.
   - h means b! in §2, the divisor product in §10, and a scalar near √y in §11.
   - s means (u−1)/2, the sphere target, the digits s_m, and 2^{2^i}.

10. **§1 Assessment.** "Requiring k even … would imply C-even (★)" is asserted without proof. Cite a z75 Prop. 3 variant or drop it.

11. **Git.** The branch is behind main. `git diff main..` shows about 15k deleted z81-lit lines only because main later merged `9313b724d`. The branch touches only `FAREY_PROOF.md` and the R1 file, so do a normal merge or rebase; do not restore files from the branch.

After the fixes, the Review line can cite this as the second Opus cross-lab review, covering §§7–11.
</code-review>
