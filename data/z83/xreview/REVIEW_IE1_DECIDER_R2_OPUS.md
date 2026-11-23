<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="8ef750588">
A separate reviewer subagent was asked to review the changes in `git log 8ef750588..`. Its request and review follow.

Request: review changes since 8ef750588 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Full hostile Round-2 Claude Opus cross-lab review of Wave z83 Lane 1, notes/z83/IE1_DECIDER.md §§6–10 (Outcome A record candidate). Try to break every valuation, uniform ACVF QE/scalar profile/disc CRT, per-place pair embedding, resultant top coefficient and ordering, mixed scalar/horizontal support, ES descent, entire z82 full-Farey proof interface, and Lane 2 residue comparison. Audit also the ordinary E1 induction-rule and conservation proof (free-cut elimination and bounds), numerical leastness claim, labels and the requested R1 m1–m5. Replay only as needed, ≤15 min of replay, ulimit -v 6000000, ≤2 compute processes, timeout≤1800, Python via uv run --offline --no-project python -B. Return a nonempty report with explicit verdict and every required fix. Read only; do not edit.

Commit log:
commit 852dcb457b67f528dd25d4d5a1c1137f13d92168
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 03:52:47 2026 +0100

    z83 R2: absorb all radical-supported digit lifting in a full-Farey ES countermodel

 data/z83/ie1_decider/mixed.txt |   2 +
 notes/z83/IE1_DECIDER.md       | 125 +++++++++++++++++++++++++++++++++++++----
 scripts/z83_ie1_mixed.py       |  52 +++++++++++++++++
 3 files changed, 168 insertions(+), 11 deletions(-)

Review:
**Verdict: ACCEPT WITH FIXES.** I found no fatal gap in §§6–10. The T_Π record candidate (Outcome A) holds at the level of an interface audit against z81 §3 and z82 §§7–11. None of the required fixes changes a theorem. They are about scope, §0 bookkeeping and spelling out steps that are currently implicit. Under AGENTS §3 this review can count as the one cross-lab review; promotion should wait until the fixes are applied.

## What I tried to break, and the result

| Target | Result |
|---|---|
| **§6, `IE₁⁻ ⊢ DL`** | Holds. The refinement step `t ≡ −q (mod g)` is valid, `dg | h`, and the progress measure `d ≥ j` is unchanged. The Jacobson-radical form of "no escape" is correct in a Bézout ring. My replay of `scripts/z83_ie1_mixed.py` matches `mixed.txt` exactly. |
| **§7, the branch** | Holds. At a prime `l | h` the reduction of `f` is linear, so the integral root `α_l` is unique even over the algebraic closure. The pullback `x ↦ α_l + hT` is injective, and the henselization adds no new values or residues. |
| **§7, invariant 1 (one scalar profile)** | Holds. `N` and `V` are the same polynomials at every place, so a single resultant and a single ACVF formula work for all `l`. ACVF elimination holds in every residue characteristic, including nonstandard `l`. Each surviving test is a comparison of provisional profiles, so it is PA-definable, and the chosen value is integral because the extension is immediate. |
| **§7, invariant 2 (disc digits and CRT)** | Holds. The test is constant on the whole disc around `z`. The Gauss minimum lies in `[0, n·v(d)]`: if it were larger, every coefficient of the primitive polynomial would be in the maximal ideal. So coefficients modulo `d^(1+n)` decide the test, and that precision is in `C`. A witness found in the larger local host reflects down to `B`. The PA part off `h` (clear poles, then undo the multiplier) is correct. |
| **§8, resultant top coefficient** | Holds. The product formula plus "actual value ≥ Gauss value" for each factor forces equality factor by factor, even with repeated or non-integral roots. The `U^n` coefficient is `b_n (hD)^n`, which gives `b_n h^n D^n ∈ R_A`. |
| **§8, ordering** | Holds. Placing `x = hHξ` is necessary: with `x = Hξ` the bound only gives size `H^n/(hD)^n`, which is not large enough when `h ≥ H`. With `hHξ`, every non-constant integral polynomial lies outside the `Frac C` hull. |
| **§8, mixed scalar/horizontal moduli** | Holds. "No escape" is equivalent to every prime of the modulus dividing `b`. Horizontal multiplicities are ordinary (the upper ring is a finite-type UFD), the fixed-point iteration gains a factor `b` per step, and the CRT combination is valid. |
| **§8, ES descent** | Holds. Reducing at `x = ∞` kills the positive-degree reciprocals, and positivity then forbids any of them. The protected prime `P` stays prime with −1 a non-square. |
| **z82 interface** | Consistent with the text. §7's passing test uses the actual localized ring. §8 needs content × horizontal-prime factor calculus, which invariant 1 plus the UFD supply. §§9–10 need only that the new birth is an affine line, the per-place embeddings, and the content valuations. |
| **§9, Lane 2 comparison** | Holds. At primes `l > C` the new places are immediate over a Gauss line, so the residue field gains only a rational parameter and `P̄` stays a non-square. Lane 2's §1 hypotheses are kept. |
| **§10, the induction rule** | Holds. The hereditary characterization is right: forward by parameter packing, reverse by the deduction theorem. |
| **§10, conservation** | The free-cut translation step works: `¬W` is open, and `δ` and `V` are `E₁`. Hence `IE₁` is `∀E₁`-conservative over `U`. |
| **Numerical leastness** | Correctly marked CONDITIONAL. "No least failure anywhere, unconditionally ⇒ ES in ℕ" is correct. |
| **R1 fixes m1–m5** | All applied. Only cosmetic problems remain (fixes 6 and 7). |

## Required fixes

1. **§0 omits §10's main consequence.** `U`, `IE₁⁻` and `IE₁` have the same `∀E₁` consequences. Since ES is `∀E₁`, this gives **`IE₁⁻ ⊢ ES` iff `IE₁ ⊢ ES`**. This merges two open questions that STATUS line 171 lists separately.
   - Add it to §0 Result, Scope and Triage, with a label.
   - Cite the polynomial witness bound that makes ES `∀E₁` (z76; FRONTIER line 866).
   - Add a priority caveat: this is the bounded analogue of the known rule-versus-axiom conservation for `IΣ₁` (Parsons, Beklemishev) and of Jeřábek's free-cut argument. No novelty claim.
   - Propose a STATUS §2 item 4 edit.
2. **§0 Scope and the title still describe Round 1 only.** Add: "`T_Π` (§§6–8) satisfies the full DL scheme, including Π globally; its `IE₁⁻` status is unknown; nothing is said about `IE₁⁻ ⊬ ES`."
3. **STATUS delta.**
   - Mark "fails Lane 2's quintic least test" as relative to BCM_TS_LDIV §§1–2. That note has only an R1 review.
   - Add "fails BCM; no `IE₁⁻` assertion", so readers do not take the new model as an induction model.
4. **§6.**
   - In the DL statement, write `≡` instead of `=`, and say the escape is certified by a Bézout row.
   - The construction theorem is "rel. §§7–9", but it depends only on §§7–8.
5. **§7, invariant 2.** Spell out two implicit steps:
   - The PA test `Ψ(l,·)` is periodic modulo `l^(v_l d)` on `B`, which is what licenses PA least selection and CRT.
   - The reflection uses that `B` is an elementary substructure of the host's arithmetic sort (z81 §12).
6. **§2 item 2 (m4).** It handles only free, row and sphere edges, while item 3 introduces floor edges. Say that floor completions are z81 line/row edges (z81 §3: "we only need line and row edges").
7. **§3 (m5).** Remove the stray comma before "(also the inertia at infinity…)".
8. **Pinned files outside this branch.** `REVIEW_IE1_DECIDER_PI_OPUS2.md` (9b61b3866) and BCM_TS_LDIV at e82519e23 are not ancestors of HEAD. Merge them before the export.
9. **§8 (clarity).** Note that `(T−s_m)/D_m` is integral at every place and every depth by the z81 refinement. The leading-coefficient bound uses this.

## Debate points (no fix needed)

- **Is T_Π a real advance or a re-encoding?** It is a real advance. It is exactly the different arithmetic sandwich that Lane 2 §2 said any repair above `C` would require, and it is built non-PID.
- **What remains open.** DL only lifts existing simple roots and never forces new residues. So the surviving obstruction (Lane 2's fine residues) and the open induction loops beyond DL are stated correctly in §10's table as "unknown".
</code-review>