<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="c69a4cddf">
A separate reviewer subagent was asked to review the changes in `git log c69a4cddf..`. Its request and review follow.

Request: review changes since c69a4cddf carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Full hostile Round-2 cross-lab Claude Opus review of Wave z82 Lane 4: notes/z82/GAP11_JLL.md §§6–10 and §0, scripts/z82_gap11_r2_cert.py. Try to falsify Theorem 5's unweighted four-inert-factor supply, Pan's precise hypothesis and modulus-independence, Mertens, ordering and gamma constants, pinned Buchstab recurrence remainder budget and outward rounding; Theorem 6's conditional D(.957) enhanced Selberg denominator, good roots, normalizations, numerical sign. Check Type I vs gated Type II and the Lane 3 §2 reconciliation at 38ebd2fcc. Record what you substantively checked and every required fix. No file edits; if replaying use ulimit -v 6000000, timeout ≤900, uv run --offline --no-project python -B, ≤2 compute processes. Cap all replays at ≤15 min.

Commit log:
commit 0309e3f8e508f1a602d68888a21bd3546c030161
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 20:47:54 2026 +0100

    Mark Round 2 cross-review blocked pending Opus reauthentication

 notes/z82/GAP11_JLL.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

commit b150709ff3d7de9ef9f795c0beef4b01dbfa40cb
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 20:36:17 2026 +0100

    Bound the second-window inert multiplicity by four and lower the ordinary prime level to .957

 data/z82/gap11_jll/r2_cert.txt |   4 ++
 data/z82/gap11_jll/r2_scan.txt |  10 ++++
 notes/z82/GAP11_JLL.md         |  88 ++++++++++++++++++++++++++--
 scripts/z82_gap11_r2_cert.py   | 129 +++++++++++++++++++++++++++++++++++++++++
 scripts/z82_gap11_r2_scan.py   |  39 +++++++++++++
 5 files changed, 266 insertions(+), 4 deletions(-)

Review:
**Verdict: ACCEPT with minor fixes.** I found no substantive error in Theorem 5, Theorem 6, the §9 Type I proposition or the certificate. Theorem 6 is still CONDITIONAL on D(.957), and it reached that label correctly. Neither theorem bears on ES itself, and no ES claim is made. What needs changing is form, plus one stale pointer to Lane 3.

## Replays (each under ulimit -v 6000000, well within the time cap)
- **`scripts/z82_gap11_r2_cert.py`:** finishes in about 1.5 minutes and reproduces `r2_cert.txt` byte for byte.
- **My own floating-point recomputation** (separate code):
  - **Semilinear functions:** my tables match the closed form `f=A·asinh√(s−1)/√s` and `F(2)=A/√2` to about 1e-6. I also checked `J₁(a)=2H₂(1/a)` by direct double integration: 0.159228 vs 0.159227.
  - **Theorem 5 costs:** (4) comes out at 0.41128 against the certified bound <0.41234. The sum of (5) over even h≥6 comes out at 0.007280 against <0.00730. For reference, H₂, H₄, H₆ at 1/b are 1.626, 0.153 and 0.00228.
  - **Buchstab array, reimplemented in floats at g=2000:** the root lower bound is 0.42348 against the certified >0.42113. Lower never exceeds upper at any node.
  - **Theorem 6:** the continuous margin is +0.00129 at τ=.9569; the certificate gives >0.00100. The margin is −0.032 at τ=.95 and +0.0018 at τ=.957, so the threshold sits near .9568, consistent with the note.

## Theorem 5: what I checked
- **Delay equation for H_h.** I derived it by differentiating the simplex integral by hand. This confirms `K_h(z)=H_h(1/z)`, including the 2^{h−1}·h! normalization and the `1/(2√(u(u−1)))` kernel. `F=A·H_even/√s` and `f=A·H_odd/√s` agree with the semilinear (β=1) delay equation.
- **The last prime R needs no 1/2 density.** On p≡1 (840), `x₃≡1 (210)` and `x₇/2≡1 (105)`, so `χ_q(x_q/c)=+1`. With h even, R is therefore automatically bad.
- **Pan's theorem.** I checked it against the on-disk Nath–Xie Thm 3.1: f is O(1) and independent of the modulus and residue, supported on m≤x^{1−ε}, (m,q)=1, with level √x/log^B and max over y≤x. The modulus `Q≤210·X^{.4995}` fits. The weights are fixed before Pan, and the w(l) argument is sound: every polynomial used is pointwise nonnegative and the law at each prime is a product law.
- **Constants agree with the already-reviewed results.**
  - (4) at s=2 reduces to the §4.1 form `A²√(a/2)J/(level)`.
  - (5) at h=2, converted to U units, is `(3/4)(2/τ)^{3/2}J₁(b)`. That is Theorem 3's tail, with the denominator power going from 5/2 to 1 because the level is now X rather than Y.
  - The `τ/2<a` condition is used correctly, and so is the parity argument giving exactly h=2 at q=3.
- **Buchstab recurrence.** The signs are right: the lower parent uses the upper child at (K,I), the upper parent uses the lower child at (K,I+1), and r is deleted from its own sieve. The coefficient ½log(i/(i−1)) is right, the depth is at most g/(2B), and every remainder fits ordinary BV at level 999/2000. The code's indices match the text.
- **Outward rounding in the script.** I went through it line by line and every direction is correct:
  - `sq` and `sq+1` bracket the square root.
  - Kernel cell bounds: dl and dl+3 bracket the cell integral; the lower bound divides by √v, the upper by √u.
  - Lookups round the argument down, using monotone f and F.
  - The log bounds are alternating Taylor sums, and `loglo` is a genuine lower bound.
  - The γ and e^γ brackets are sound, and the Machin partial sums give π from both sides.
  - `3*Eu//2` happens to be exact.
- **Vector sieve substitution.** Plugging bounds into `f₃F₇+F₃f₇−F₃F₇` is valid, because the expression increases in each f and decreases in each F.

## Theorem 6: what I checked
- **The extra roots are valid.** With r the least bad prime and r ≥ X^.35, we get `x_q=c·m·r·r′` with `m<X/r²≤X^{v}`. So good-at-q primes in `(X^v,B]` cannot divide x_q, and since B<X^.35 the bad roots below B are covered too.
- **Sieve details.** `h₀=(e+f)/(ℓ−1−e−f)`, and Δ(ℓ)=1/ℓ+O(1/ℓ²) in both the f=0 and f=1 cases. I re-derived the delay equation for V(w) by hand, and G₀ is consistent with C_V. The cost per cell, `2(t₁−t₀)/(t₀(τ−t₁)V)`, is right, and rounding w down is conservative.
- **Level.** All moduli satisfy `840·r·B²≤840·X^τ`. z81's D(θ) takes the maximum over reduced residues, so D(.957) covers every class used. The Selberg weights depend on the cell, not on r.
- **Comparison claims hold.** The concavity bound `(2/3)cosh²(1/2)=.84769` is correct, and so is the remark about symmetric cutoffs at .486.

## Type I vs gated Type II (§9)
- JLL's own text (lines 335–342 of the on-disk source) says x^{0.41} is only a convenience below FT's level `√y/log^B y`. So the condition θ+2ν<1/2 is legitimate, and d|u+1 is absorbed into the residue class mod dq. If (d,q)>1 the progression is empty, since 4(u+1)−(4u−3)=7. ν=.007 is fine.
- The scope is correct: this bounds only the Type I discrepancy. No positive θ is claimed for gated Type II.
- The 1+λ_ℓ≤0 observation is right, and so is the `L^.48` tariff, matching JLL Lemma 6.3's `S≤exp(C L^.98)`.

## Lane 3 reconciliation (§10)
- At 38ebd2fcc, §10's paraphrase of Lane 3 matches Thm A. The Markov costs s/1000 and s/30, the O(K^{1/3}) remainder, the `K·l^{−A+30 log s}` discard and the elementary symmetric moment bound ≤μ^m/m! all check out.
- **However, 38ebd2fcc is not an ancestor of HEAD, and it is stale.** Lane 3's tip (24f432dd4) leaves §2 unchanged. But its header now proposes G/G′ to supersede A, with stronger bounds: `l^{1/(2e)}` at K=L and `L^{2/3}l^{1/6}` at K=L^{log 3}. G/G′ is unreviewed and held pending review.

## Required fixes
1. **§10:** cite Lane 3's tip and say that Lane 3's A (reviewed) is the one to export unless G/G′ passes review. GAP11 Theorem 4 is superseded either way. Relabel §10 as "Assessment (reconciliation)" rather than PROVED, since it restates Lane 3's proof.
2. **Script:** the docstring says the π bracket is "checked at startup", but nothing asserts it. Add a `pl/ph` bracket assert, or drop the word. Also update the memory docstring, which refers to g=1200 while the run uses g=2000.
3. **Dependency lists:** Theorem 5 and the product-switch lemma should also name Shiu, the Nath–Xie presieve used in §4.1, and z81 §11's C_m normalization. They should note that Pan is cited through Nath–Xie's restatement, because Pan's original paper is not on disk.
4. **Optional clarity, §6:** replace "the sign of R is automatically negative" with the χ_q(x_q/c)=+1 parity argument.

Until the orchestrator applies the fixes and records this review, Theorems 5 and 6 stay out of STATUS, as the note's header already says.
</code-review>