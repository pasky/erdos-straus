<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="849f46ddf">
A separate reviewer subagent was asked to review the changes in `git log 849f46ddf..`. Its request and review follow.

Request: review changes since 849f46ddf carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Round-3 review of notes/z79/WILD_ES.md and scripts/z79_*... Specifically verify the self-contained HJ κ<1/3 quarantine/energy proof (closing Round-2 F2) and all new Round-3 theorems! Audit every §9 interface (terminal f class, optional stopping, pair drift & late loads incl 2, LLL, prefix-energy/combinatorial identity and minorant, both prime transfers), §10 cubic every coefficient and degeneracy branch, fresh-conductor pruning through binary quadratic norm equations and transfer. Give explicit F2 verdict and any required fixes. Replay ledger and any independent checks under ulimit -v 6000000; timeout <=1800 uv run --offline --no-project python -B. No side agents or edits. Return full text.

Commit log:
commit 82a91e8263887cae23a5fe9104ddb0ee9f0c3eda
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 14:15:51 2026 +0100

    z79: prove the HJ height interface and all-cubic pullback by discriminant pruning

 data/z79/wild_round3.txt   |  6 +++
 notes/z79/WILD_ES.md       | 97 ++++++++++++++++++++++++++++++++++++++++++++--
 scripts/z79_wild_round3.py | 47 ++++++++++++++++++++++
 3 files changed, 147 insertions(+), 3 deletions(-)

Review:
# Round-3 hostile review: `notes/z79/WILD_ES.md` §§9–10 and `scripts/z79_wild_round3.py` (commit 82a91e826)

**Verdicts.** F2 is **closed in substance**: §9 is a self-contained and, as far as I can find, correct proof of the HJ quarantine/energy step, and I found no mathematical gap. CUB3 (§10) is **accepted** as PROVED relative to §§1–3 and §6, the density input and elementary quadratic-field theory. Promotion should wait for the form and label fixes below. Two of them are required: R1, where §8 still says this review is owed, and R2, where the §0 label drops inputs that §8 still uses.

## Replay and independent checks
All runs used `ulimit -v 6000000`, `timeout ≤1800` and `uv run --offline --no-project python -B`.

- **Ledger replay.** `scripts/z79_wild_round3.py` runs in 0.45 s and its output is byte-identical to `data/z79/wild_round3.txt`. The count of 725 + 54 = 779 is π(6000) − 4, so every prime in the range was tested.
- **(6) and the Θ bound.** My own scripts are in `/tmp/r3rev/`, not committed.
  - On 4000 random hypergraphs with a^E ≤ 2, |Θ| ≤ 1 and the matching bound always held; the worst value was exactly 1, so the bound is tight.
  - I computed exact weighted energy on a 6-axis digit space: 2-adic indices 3 and 4, digits 0 and 1 at both 3 and 5, and random prefix atoms with moduli up to 7200.
  - The maximum of the left side of (6) was 0.9933 with every prime unstarted and 0.9938 with the first digit at 3 started. Both satisfy ≤ 1.
  - Shrinking L to L/3, which breaks the hypothesis a^E ≤ 2, gives 1.00006. So the hypothesis is the operative one and the inequality is close to sharp.
- **HJ atom encoding.** For all 1115 primes p ≡ 1 (mod 840) below 3·10⁶, every interior good word (t,u,v ≥ 2, (A/p) = −1) lies in a listed atom at its denominator A.
- **Cubic algebra.**
  - 2000 random cases confirm 3W = 81a²v²·disc(F + u/v) and 4P³ − J² = 27a²·disc F, in exact rationals.
  - The fresh-prime lemma had 0 violations in 7321 tests with C₀ ≠ 0. A dedicated test of the C₀ = 0 branch (F = (j − r)²(aj + s)) checked 10069 fresh primes: each is coprime to uv and has odd valuation in W.

## §9: interface-by-interface audit
1. **Terminal class.** Correct.
   - f ≡ 5 or 7 (mod 8): u = 2 works, since (−2/f) = −1.
   - f ≡ 3 (mod 8): u = (f+1)/4 works, since u ≡ 4⁻¹ is a square and (−1/f) = −1.
   - f ≡ 1 (mod 8): (q/f) = (−1/q) for odd q dividing f+1, which gives the stated iff.
   - Admissibility is also *necessary* for f to be the least good denominator, so HJ3 relative to (G) is sharp in f. The odd-square remark is trivially true.
2. **Budget (5).** Correct.
   - The Hölder exponents 1/(1−a), 2/a, 2/a are conjugate.
   - The Euler factor above Y is β^z = 1 + O(1/log L), giving L^{1+o(1)}.
   - The bound 1 + log m_Y ≤ (1 + log Y)τ(m_Y) holds.
   - C₀ in (5) is independent of K, so choosing K > C₀ + 5 is legitimate.
3. **Optional stopping.**
   - At a first digit, the square choice gives drift exactly 2, which halving 2^{b} pays for. Higher digits, including the binary digits at 2, are martingale steps. The base cost is at most 192.
   - The decision time τ_{q,a} is a stopping time, and x is evaluated before the step. The charge per atom is Σ log q = log m_Y.
4. **Pair drift and late loads.**
   - Checked: a first-digit step that constrains both atoms gives (q−1)²·(2/(q−1))/(q−1) = 2, and a later step gives q²·(1/q)/q = 1. The diagonal case E = E′ is covered. R_end ≥ 1.
   - The base-prime prefix counts at 2 cost at most a constant.
   - The bound φ(g/l^{v_l(g)}) ≤ (m/l, m′/l) = Σ_{d|·}φ(d) holds. The Cauchy step and the regrouping to (1+L)Ξ/Y = o(η²) are correct.
   - One point is correct but deserves a sentence in the note: inconsistency of E and E′ at l is harmless, because one bounds products of *marginals*, not joint events.
5. **LLL.**
   - For x ≤ 1/4, 1 − x ≥ e^{−4x/3} (at x = 1/4: 0.288 ≤ 0.333). With η = (3/4) log β this gives β^{−s}, so the asymmetric LLL condition holds.
   - The cylinder inequality is the standard conditional LLL bound.
   - Every live atom keeps an unfixed prime (fully fixed atoms are killed by the Jacobi sign), so x_E ≤ η.
6. **Energy (6) and the minorant.** I re-derived every step.
   - The telescoping eigenvalue is λ^{1+max U_q}.
   - In the inclusion–exclusion, only intersections touching every selected block survive.
   - Σ b^V 1[V ⊆ A]1[V ⊆ B] = a^{A∩B}, and the random-P identity holds.
   - The recursion Θ(C) = a_vΘ(C/v) − (a_v − 1)Θ(C − v) and the matching induction hold.
   - a^E ≤ λ^{2v}, and over all primes ≤ 2^{log m/L} ≤ 2.
   - In the minorant B ≤ F₀. E(F₀ − B) ≤ n₀²·S·2^{−τ/(2L)} ≤ e^{−3S}/100 ≤ δ/100. E|B| ≤ 1.0202μ. log D ≪ L(L + S).
7. **Prime transfers.**
   - **Clean scales.** Correct, with the condition Cc > 9 sufficient; the note uses 12.
   - **The (G) route.** It matches H4 Lemma 7b. The re-derived Lemma-6 analogue (the F′ argument, |E[Bψ]|/μ < 1/4) is correct. Both exceptional-sign cases are handled and the Page bound absorbs the Z³ correction.

## §10 (CUB3)
- **Coefficients and conductor.** P, J, C₀ and W are correct. The bound |W| ≪ h^{2.21e} holds, and 4q|3W| ≪ h^{3.83e} < Q.
- **Root detection.** The Stickelberger detector (a nonsquare discriminant forces exactly one root) is valid for ℓ ∤ 6av.
- **The P = 0 identity.** 27a²F = (3aj + b)³ + (27a²d − b³) holds when b² = 3ac, and the cube map is bijective on ℓ ≡ −1 (mod 12).
- **Case C₀ ≠ 0.** W ≡ C₀v² (mod u) and W ≡ −(27a²u)² (mod v), so a fresh prime ramifies in the twist. The norm-equation count holds:
  - at most τ(N) ideals of the given norm;
  - at most 6 associates in imaginary fields;
  - O(log h) associates in real fields, from the unit gap log φ with φ = (1+√5)/2.
- **Case C₀ = 0.** W = −27a²u(2Jv + 27a²u) holds. Bounding only the linear factor is the right choice, because primes dividing u can be absorbed by χ mod q. This gives h^{.56e+o(1)}.
- **Twist pruning.** Conductor 1 being on the list correctly removes pairs where 3W is a square or nearly so. The losses are o(h/log h).

## Required fixes
- **R1 (F2 bookkeeping).** §8 still says "A dedicated second review of this inherited interface is owed", and §8 still routes through O13 Lemmas 3.2–3.3 and H4 Lemma 5. Mark these sentences as superseded by §9, or say §8's HJ paragraph is an alternative sketch.
- **R2 (label, §0).** The new §0 label removed "the separate §8 result also imports the O13/z78 interfaces". §8's **seven-chart** Theorem F still uses the z78 Thm G minorant, i.e. O13/OMEGA10, H4 Lemma 5, ET, Shiu and Pólya–Vinogradov. §9 re-derives only the HJ quadratic-mass case. Restore these inputs for Theorem F.
- **R3 (§0 completeness).**
  - The Result and Scope lines do not mention HJ3: every admissible prime f relative to (G), and a subsequence without it.
  - There is no Round-3 paragraph analogous to Round 2.
  - The HJ3 label "rel. the classical prime estimates specified below" should list them:
    - (G) in the formulation of H4 §5, i.e. the MV III draft Thm 28.19 with the POINTWISE_OMEGA9 repair, original paper unchecked;
    - Montgomery's density theorem;
    - Landau–Page;
    - the zero-free region;
    - Page's bound on 1 − β;
    - the smoothed explicit formula;
    - Bertrand;
    - fixed-modulus PNT.
- **R4 (notation in §9).**
  - τ is both the divisor function and the truncation threshold in the same section.
  - U is both the digit index set and the clean scale.
  - u is both an HJ letter and the truncations u_j.
  - w denotes three different things.
  - K differs between §2 and §9; C₀ differs between §9 (the Ξ exponent) and §10.
  - In §10, "h = 3" and "h the block height" appear in adjacent sentences.
  - D has three meanings across §§1, 9 and 10.
- **R5 (citation).** §2, which CUB3 imports, still cites the MV III draft Thm 28.6 with log⁶, while §9.3 now cites LNM 227 with log⁹. Unify on the published source; the list-size bound h^{.02e} survives log⁹. I could not verify "Thm 12.2" offline (it may be 12.1).

## Recommended, minor
- **Triage.** HJ3 is a lower bound on an invariant of the HJ method, so it reads as BARRIER-SCOPED or METHOD-CX rather than RECORD. The RECORD triage should rest on CUB3. Its priority is unverified, and CUB3 should cite Z60_MS105's qualitative higher-degree result for comparison, as B does for quadratics.
- **Script.** The gcd assertion (`disc or J`) only partially tests the lemma, and the norm-equation counting is not checked. The CERTIFIED claims stay modest, so this is acceptable.
- **Wording.**
  - "Expected combined factor ≤ 2" should say "for p·p′·R, before the 2^{b+b′} weight".
  - The Review line "dedicated follow-up supplied in §9" should say it is self-supplied.
  - Masters (WAVES, STATUS, FRONTIER) were correctly left untouched by this lane commit; the orchestrator owes the export.

No CLAIMED proof of ES appears, and the scope statements are accurate: parameter counts in intervals, and no pointwise claim.
</code-review>
