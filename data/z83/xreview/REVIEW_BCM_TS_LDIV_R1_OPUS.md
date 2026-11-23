<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of Wave z83 Lane 2 (notes/z83/BCM_TS_LDIV.md). Scrutinize every model-theoretic/valuation/order/unit-rank/specialization/induction step with extreme rigor; check every label and scope. Cap any replay at ≤15 min.

Commit log:
commit c06c8940d9f31be3b46c87c8bc867089f41b8120
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 03:06:27 2026 +0100

    Test bounded and solvable residue repairs and realize the insufficient BCM unit blueprint

 data/z83/bcm_ts_ldiv/sparse.txt | 14 +++++++++
 notes/z83/BCM_TS_LDIV.md        | 69 +++++++++++++++++++++++++++++++++++++++--
 scripts/z83_bcm_sparse.py       | 44 ++++++++++++++++++++++++++
 3 files changed, 124 insertions(+), 3 deletions(-)

commit b26602cb275973fe44f63daafae0640219ecfbc0
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 02:45:52 2026 +0100

    Separate quintic from affine minimization uniformly in Farey power cuts

 notes/z83/BCM_TS_LDIV.md | 82 ++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 82 insertions(+)

Review:
## Review of z83 Lane 2, `notes/z83/BCM_TS_LDIV.md` (commits b26602cb, c06c8940)

**Verdict: accept with fixes.** I found no mathematical error in what I could check. Six form and scope problems need fixing before export. The cross-lab review is still owed for the record claims in §3 and §4.1, which depend on other notes.

**Replay:** `uv run … scripts/z83_bcm_sparse.py` takes 0.13 s and its output is byte-identical to `data/z83/bcm_ts_ldiv/sparse.txt`. The script uses a quadratic test residue `4 mod p`, which is a unit. The brute-force least-hit check runs only on `(3,11)`, the greatest-root assertion holds on all 12 root profiles, and both lists satisfy `p_{i+1} > (prefix)²`.

### Substance, step by step

**§1, the main constant-modulus result: correct.** I checked each step:
- **Product bound:** `∏_{i≤j}p_i < 2^{j+2^{j+1}} ≤ x_j³`, which needs `j ≤ 2^j`. Then `x_m² > H` follows from `2^{m+1} > L`.
- **Cofinality:** for `c ∈ C`, the first `x_i ≥ c` gives `c < p_i < 2·max(2,c²)`, which stays in C.
- **Large-prime step:** if `t²−P` is a unit mod p, cancelling twice gives `p² | t`.
- **Lower bound:** the set `{i : p_i² ∤ b}` is a PA-coded set of scalars, so a last q exists inside B. That gives `c ∈ C`.
- **Smaller hit:** the competitor `t' = Mz < h²/q < h²/c ≤ t` works.

The point is that the repeated factor `q²` beats the choice `z < q` that you cannot control. With a squarefree modulus the argument collapses, which is consistent with the positive result in z82 BCM_LDIV §6, so there is no conflict.

**§1, the greatest-rooted-prime lemma: correct.** It needs integer division in R and only a unit root, which can be nonscalar. The bound `c < p_{next}` comes from `x_{i+1} = x_i⁸`.

**§2, which towers satisfy the hypotheses: correct as far as it can be checked against z81/z82.**
- **Residue field:** at `p > C` the restricted Gauss residue field is exactly `k_p(S)`. The note says only "because p∤L"; the actual reason is that `L ∈ C < p` (L is a log-size element). Please state that.
- **Edges keep regularity:** free lines and row charts are purely transcendental. Rank-4 spheres are geometrically integral even at target 0, and the residue characteristic is externally zero.
- **Root test only needs a map:** a unital map `R/pR → κ` is enough; injectivity is never used.
- **Variant without specified valuations:** the saturation step "unit constant term ⇒ nonzerodivisor mod a" is correct (McCoy's theorem). Nonzero fibres follow from contraction.
- **Coverage of the z82 §§6–7 schedules:** they are covered, because every prime those schedules enter (i.e. builds into a valuation modulus) lies in C (BCM_LDIV §6 step 1).
- **No conflict with z82:** the (C1) embedding into a host `D∞/pD∞` does not create arithmetic roots. The four-squareclass remark is right.

**§2.1, the bounded-degree repair: correct.**
- **Galois setup:** the Kummer group is `{±1}^N`. The stabilizer of `θ_σ` is `{1,σ}` because the basis is an annihilator basis. So the orbit polynomials are irreducible of degree `2^{N−1}` over `k_p(S)`.
- **Small primes:** the Frobenius-fixed specialization and the translate-by-1 trick give a nonzero scalar root.
- **Cleaner justification available:** "∀ odd q ∀y ∃x≢0 with `q | F_N(x,y)`" is a single true sentence of arithmetic, so it transfers to B directly. Saying this would remove the need for the Frobenius discussion.

**§2.2, the S₅ resolvent: correct.** The 120 monomials in the orbit of M are distinct, so the stabilizer of `θ_J` is exactly J. The core of a cyclic subgroup is trivial, so each orbit factor has Galois group S₅, which is not solvable. Every Frobenius cycle type has splitting degree dividing 60.
- **Unproved aside:** the claim that the original tower has five independent large residues ("e.g. use five cut-height Dirichlet coordinates…") sits inside a PROVED block with no proof. Either prove it or relabel it as Assessment. The theorem itself does not depend on it.

**§3, the joint Farey + affine least-search model: plausible, but a compressed sketch.**
- **Why it is plausible:** the z81 §13 sorting lemma needs only three things. The factor calculus is preserved because paired edges are polynomial (z82 §8). The host freshness is stronger than z82 requires. The obstruction branch keeps a finite prefix together with its finite host chain.
- **What I could not check:** the z82 §§8–10 temporary-completion arguments under the z81 §13 residue choices. This is exactly where the cross-lab review is owed.
- **Syntax claim:** "lexicographic guarded ⇒ LE₁ ⇒ IE₁" is fine as a reference to Wilmers.

**§4, the BCM successor tests: correct.**
- **Reduction and signs:** the midpoint step, the coprime reduction `H = lab`, `t = la²`, and the opposite signs in the Bézout valuation rings all check out.
- **Rank survives deletion:** both signs follow from `⋂A_M = A` and `A ∩ O = F`. The finite-support corollary follows from the leading-term argument (characteristic zero).
- **Single-valuation no-go:** it really needs no Bézout.
- **Hahn example:** `√2 ∈ Frac R` is right. Global BCM holds when Γ has no largest archimedean class, because `1/d` has support in the convex subgroup `G_γ`.

**§4.1, the control example (residues and scales do not suffice): correct modulo the cited lemmas.**
- **Divisors and the missing successor:** the unit/monomial-cone description gives degree-one divisors of the form `fH, fHz^{±1}` only. Exact lifts at residues in F reduce the residue-one case to `1+ε`, and each new ε dominates every earlier increment. So there is no minimum.
- **TS and Lag:** landing in `±1` plus the mod-4 congruence carried by the retraction gives TS. `e(H−1) = −1` kills Lag.
- **Persistence:** the step "the residue field does not grow past stage 1, via `⌊Hx⌋`" is right.

### Form and scope fixes required

1. **§0 contradicts §5.** §0 gives a STATUS delta, but §5 ends with "No proposed master-file edits by this lane." Remove one of them.
2. **Undefined labels in §5.** "Part (a)/(b)/(c)" and "the three results" refer to the lane brief, not the note. Name the sections instead.
3. **§1 theorem statement reads as universal.** "for a single positive squarefree scalar h" sounds like any such h, which is false (take `h=1`). Write "there is a positive squarefree scalar h ≤ H³ (constructed below)".
4. **Entry screen is not actually done.** "Screens 1–3,14,15 are tested below" is never carried out; §5 has only F1–F4. Do the screens or change the claim.
5. **STATUS delta is incomplete.** Row §1E/143 still says "Full `L(Div)` in another variant is open", and z82 FAREY_IE1 §11 lists `T_F`'s full L(Div) as UNKNOWN. The delta should replace that phrase, scoped to "outside reserve-Gauss/regular-residue schedules", rather than add sentences beside it. It should also note that the z82 UNKNOWN is now decided; that is an upgrade, so it goes in at export.
6. **Triage label for §3 is generous.** Calling §3 a "RECORD" overstates it: it combines two existing properties in one model. The stronger STATUS-worthy item is the uniform L(Div) failure, which is BARRIER-BROAD. That needs a proposed FRONTIER §3/§4 line, and none is given.

### Labels and scope
The labels (PROVED relative to the cited notes; Assessment for the limits) and the scope sentences are accurate. Nothing here is phrased as an ES claim or an IE₁⁻ claim.
</code-review>