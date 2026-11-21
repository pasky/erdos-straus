<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="1c95e7ddd">
A separate reviewer subagent was asked to review the changes in `git log 1c95e7ddd..`. Its request and review follow.

Request: review changes since 1c95e7ddd carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Round-2 review of notes/z79/LOWER_TAIL.md and scripts/z79_lower_tail_r2.py at aa477071b, by independent Claude Opus. Re-derive the FULL UNWEIGHTED factorial (Poisson power-saving) claims, three row estimates, completed/restored Euler mean incl coprimality and tail, signed small/large h, equal-projection pair charged before adding others. Verify the BV arbitrary logarithmic exponent and fixed σ_A/degree quantifiers. Independently check H₂: prior cubic and quadratic supplies actually available for every reduced multiplier digit, has no pinned-prime overlap at ℓ, the nonnegative growing-degree polynomial/level and Gallagher/GRH transfer (especially if Siegel-small base). Assess sign and check script/finite evidence. Return exact verdict and fixes; write nothing in repo. For tests ulimit -v 1200000; timeout ≤1800; uv run --offline --no-project python.

Commit log:
commit aa477071b31351cede309cabfeb2c74112860ec7
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 13:54:42 2026 +0100

    Control mixed-pin factorial moments and subexponential primorial-fibre tails

 data/z79/lower_tail_r2_checks.txt |  9 +++++
 notes/z79/LOWER_TAIL.md           | 80 +++++++++++++++++++++++++++++++++++++++
 scripts/z79_lower_tail_r2.py      | 66 ++++++++++++++++++++++++++++++++
 3 files changed, 155 insertions(+)

Review:
**Verdict: SOUND. I found no blocking mathematical defect, so I'd accept with minor fixes.** I re-derived Theorem F, Theorem G, H₂ and Proposition I, and none of the problems below changes a claimed statement. This was the only commit in `1c95e7ddd..`, aa477071b. I wrote nothing in the repo; my scratch scripts were in `/tmp`.

## Re-derivations
- **Exact row probability (6), unweighted.** I re-derived φ(G)/φ(f) = (G/f)·Σ_{e|f,(e,u)=1} μ²(e)/φ(e), with G = (f,u) and the compatibility test G | a+zc. The signed telescoping is exact at higher prime powers.
- **Completed Euler mean.** For every prime q, whether or not it divides u, the local factor is 1 − 1_{s=3}/q² + t_q/(q−1). So the constant M = H·K_s is the same for every row and every base. Coprimality is handled by a Möbius sum truncated at X^η; the tail is ≪ Σ_{e>T} 1/(eφ(e)). The prime-of-u product is ∏(1 + O(1/q²)) = O(1). There is no tail that depends on the pin. ✓
- **Rows 1–3.**
  - Row 1: with k ≤ h ≤ f ≪ V, bound (3) is O(1) per term, and τ(u)² = X^{o(1)} for fixed v. ✓
  - Row 2: k divides Q·∏k_ν, and each k_ν divides the nonzero determinant ac_ν − a_νc. Then b = 4vsg dominates (v−1)(s−1)g with a large margin. ✓
  - Row 3: h divides Q·(h, f_i), and (h, f_i) divides d − d_i. So h/V ≪ QX^w/(A₀C₀) since σ + w < g. ✓
  - Small h: the completion error X^{3λ+2η−g} is power-saving with λ = g/20, η = g/5. Deleting the pinned projections is done on the actual primitive sum. ✓
- **Ordering of the factorial moment.** Tuples with all projections distinct give (M + O(X^{−κ}))^j by induction on row 2. For the rest, exposing the equal-projection pair first is legitimate because the joint probability is symmetric. The pair costs M·O(X^{−κ}) by row 3, and each further pin costs ≤ X^{o(1)} by row 1. Converting to centred moments via Stirling polynomials leaves (2m−1)!!M^m. ✓
- **BV with an arbitrary log saving.** The level is vθ < 1/2, strictly. Tuple multiplicity is ≤ ρ(l)^v. Hölder plus the split l = fk gives a polylog bound on Σρ^{2v}/φ. π-form discrepancies suffice, and no Siegel–Walfisz is needed at Q = 1. ✓
- **Quantifier order.** A fixes m, which fixes v = 2m, then g (with 12v²g below the level and σ_A < g/4). The constants c_A and κ follow. ✓
- **H₂.**
  - Supply uniformity: Thm `supply` in `es-threequarter-note.tex` and (2) in `ANALYTIC_PUSH2.md` hold for every reduced c with 1 ∈ J. On Haar units every k is active, including at c ≡ 1 mod q for q ≤ B, so the means are ≍ t³ and ≍ t².
  - No overlap at ℓ: ℓ > √Y > K, B, so ℓ shares no prime with Q or the multipliers. Distinct atoms at the same ℓ have distinct unit targets.
  - Polynomial majorant: I checked the even-D Taylor majorant 0 ≤ P_D − 2^{−z} ≤ binom(z, D+1)·2^{−D−1} by exact arithmetic. F ≥ 0 on every residue, not only on primes, which is what the Fourier-coefficient bound needs.
  - Level: the conductor log is σL + O(η^{s+1}L). (G) uses only the Haar L¹ norm, never the coefficient count.
  - Small base from a Siegel zero: at r = 1 the exceptional character's coefficient equals v/φ(Q) exactly. So both the base weight and the F weight carry the same min(u,1) factor. All primes in (X, 2X] exceed every prime factor of the modulus, so induced and primitive character sums agree. ✓
  - The GRH coefficient sum exp(O(η^{s+1}L)) still leaves a power saving. ✓
- **Proposition I.** The ratio φ(9)/φ(3) = 3 is correct. I confirmed it by brute enumeration at Q = 24, a = 71: 56052 units, 346 and 54 hits, 1 joint hit, ratio exactly 3. The corrected rule follows from (4). ✓
- **Script.** `scripts/z79_lower_tail_r2.py` reruns and reproduces `data/z79/lower_tail_r2_checks.txt` byte for byte.

## Fixes (minor, none blocking)
1. **§0 format.** The Result, Label and Review lines still describe only Round 1. The Round 2 results (F, G, H₂, Proposition I) sit in a free paragraph. Update §0, record "Round 2 cross-review: …" in the Review line, and list Proposition I (METHOD-CX: it refutes the rule §5 suggested).
2. **H₂ label.** "rel. the internal multiplier supply theorems below" should name the theorems and their inputs: es-threequarter Thm `supply` (rel. BV, Brun–Titchmarsh (BT), Shiu) and `ANALYTIC_PUSH2` (2) (rel. BV, BT, Mertens). They are cited, not "below", and are internally reviewed only.
3. **§6.1 determinant bound.** For s = 3 it should read k_ν ≪ X^{(s−1)w}·A₀C₀, so the displayed exponent needs v(s−1)w. The conclusion is unaffected.
4. **Script and description.** The "9-gap ratio on three primorials" check only evaluates formula (4) and asserts the gcd. It checks neither base compatibility nor any enumeration, so the note's "Also checked" overstates it. Add the Q = 24 enumeration above, or reword.
5. **§5 "Next experiment" is stale.** It asks for a mixed-pin bound that §6 now partly supplies (in order-dependent boxes). Add a pointer to §6.
6. **Naming and typo.** "H₂" collides with `WILD_ES` Theorem H; rename it. Fix the typo "arbitarily" in §6.2.

## Things that hold but should stay explicit
- **Theorem G's constant.** G trades the explicit constants of D/D₂ for c_A ∝ w^s with w = g/(100v), which is tiny. It neither implies nor is implied by H₂, which has an exponentially small exception rate but only a threshold of L^{α_s} witnesses. The STATUS wording "at c_A instead" is accurate. Akaka's claim is an earlier, unrefereed comparison point; priority is not established.
- **What H₂ adds.** For all primes, H₂ is essentially already in the internal supplies. Its new content is the single fibre p ≡ 1 (Q) with Q = X^σ. The note states this correctly.
</code-review>
