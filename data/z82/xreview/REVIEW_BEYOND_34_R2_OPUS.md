<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="38ebd2fcc">
A separate reviewer subagent was asked to review the changes in `git log 38ebd2fcc..`. Its request and review follow.

Request: review changes since 38ebd2fcc carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Full hostile Round-2 Claude Opus cross-lab review of notes/z82/BEYOND_34.md §§6–10, its §0, and scripts/z82_b34_gaps.py. Audit every step in G/G′: physical vs reciprocal gap, exact-list selection and uniqueness, two-sided relative block envelopes, unit repair and CRT transfer, BV uniformity, collisions and product cutoffs, endpoint log factors, scope/distinctness and provenance. Audit §9 trimmed moments/GRH and §10 phase defect, plus F1–F4 screens. Identify mathematical gaps, scope/attribution errors and needed corrections. No worktree edits. Cap replays at 15 min, Python only via `ulimit -v 6000000; timeout 120 uv run --offline --no-project python -B`. Return your full critique even if all results stand.

Commit log:
commit 24f432dd4496e40f1c637f8f1733ded8ff666783
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 20:53:43 2026 +0100

    Hold Round 2 gap results from export pending authenticated Opus review

 notes/z82/BEYOND_34.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

commit 4a68f4700fe7511f5034be0398e303ded93f953b
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 20:43:11 2026 +0100

    Interpolate prime gap tails to three quarters via uniquely matched seeds and relative block sieving

 data/z82/beyond_34/gap_checks.txt |   5 ++
 notes/z82/BEYOND_34.md            | 100 ++++++++++++++++++++++++++++++++++++--
 scripts/z82_b34_gaps.py           |  89 +++++++++++++++++++++++++++++++++
 3 files changed, 189 insertions(+), 5 deletions(-)

Review:
**Opus Round-2 hostile review of `notes/z82/BEYOND_34.md` §0 and §§6–10, and `scripts/z82_b34_gaps.py` (commits 4a68f4700 and 24f432dd4)**

## Verdict
**Accept with fixes.** I found no mathematical gap that breaks G or G′. The fixes needed are about scope, attribution and pointers. This counts as the first cross-lab review of §§6–10. G/G′ stay held from export until these fixes are applied, and any further gate the orchestrator requires.

Replay: `z82_b34_gaps.py` runs deterministically under the stated limits. Its output matches `gap_checks.txt` exactly (686, 2496, 182/89/93, 1536).

## Audit of G / G′, step by step
1. **Physical vs reciprocal gap: correct.**
   - A hit gives coprime $uA, vB$ with $uvAB\mid m=(p+e)/4$ and $e\mid uA+vB$. That is the §1 witness, so $g(p)\le 4m-p=e$.
   - I checked the old-chart identity $4x-p=(p+4u^2w)/f\ge p/f$ by hand and by script. So the 3/4 note's own witness indeed has a huge gap.
   - In §8 the Type I chart has gap $(pa+c)/b$, so inverting the *law* rather than the input is the right move.
2. **Exact-list selection and uniqueness: correct.**
   - The targets $\{-v/u\}$ are distinct and their inverses are disjoint from them: products are at most $K^{2\gamma}<K^\eta\le e$, and $uu'>vv'$.
   - So the opposite vector can never match, and matches are unique up to collisions.
   - The collision bound uses the Smith form of the $2\times j$ ternary matrix ($d_1=1$, $d_2\in\{1,2\}$, image $G\times d_2G$), giving $\le|G[2]|/\varphi(e)$. This holds for non-cyclic $G$ too.
   - The $o(1)$ condition holds exactly when $(\eta-2\gamma)\beta>\log3$. My computation $3H=l-4\log l+O(1)$ matches "$L^{\log3+o(1)}$".
3. **Two-sided block envelopes: correct.**
   - $U_b=\binom{D_b-1}{s}\ge0$. For the lower envelope, any $b$ with $D_b>0$ has $V_b\le0$, so that term alone cancels $\prod U$.
   - Relative errors: $\mathbb E\binom{D_b}{s}/v_b\le e^{C_5m}(eC_5m/s)^s$, compounded over $O(l)$ blocks.
   - Term count: $\sum_b s(T2^{-b}+\log 2m)=O(MT)+O(Ml^2)$, and $l^2=o(T)$ in every row.
4. **Unit repair and CRT transfer: correct.**
   - The repaired activation is a *disjoint* union of at most $\tau(uv)$ classes, so it is positive with no sign issues. Prime rows are untouched because $p>K^\gamma$.
   - Avoiding the joint small pin is essential in row 2, where that modulus would be $\exp(K^\gamma)\gg X$. I suggest one sentence saying so.
   - Independent-bit conditioning reproduces the categorical law exactly (odds $1/(r-J)$) with probability $\ge1/2$.
5. **BV uniformity: correct.**
   - The discrepancy sum is $O((\log R)^{1-A})$ at level $K\le R^{1/20}$.
   - Bad-$e$ removal goes through Cauchy with (6) and $e/\varphi(e)\ll\log B$.
   - The likelihood ratio over the $j\asymp l$ coordinates is $(1+O(l^{-3}))^l$.
6. **Collisions and product cutoff: correct.**
   - BT gives $\sum_{r\equiv c}\log r/r\ll T/\varphi(e)$ for $r>R$. Conditional Markov at $O(jT/H)=O(T)$ holds for every residue vector.
   - The repeat probability $j^2/(RH)$ is far below $1/K$.
7. **Endpoint log factors: correct.** I recomputed each:
   - $K=L$: $b=+1/(2e)$ gives $L^\delta l^{-1/(2e)}$ with $WT\asymp c_0^eL$.
   - $K=L^{\log3}$: $e^{2H}\asymp L^{2/3}l^{-7/3}$, times $l^{5/2}$ from $\sqrt l$ dyads, gives $l^{1/6}$. The layers $[3H-5\sqrt l,3H-4\sqrt l]$ keep constant Poisson mass, and $4\log3>1$ keeps $3^{\omega(d)+j}<q$.
   - Row 1: $BT^2\asymp L^{2/3}l^{1/3}$. Row 2: $L^{(2+\alpha)/3}$, needing $T/B\to\infty$, i.e. $\alpha<1/4$. Row 3: $B^3$ against $B^4\le cL$.

## Required corrections (scope, attribution, pointers)
1. **The §3 budget is now contradicted unless it is scoped.**
   - §3 says a rare-hit transfer with $\mu\log Z\le O(L)$ has mean budget $\le L^{2/3+o(1)}$. Row 2 has exactly that shape ($W\cdot T\le cL$) and reaches $L^{(2+\alpha)/3}$.
   - The reason: §3 assumes the single target $-1$, private letters only, and one dyadic polylog window band ($\sum1/\varphi(q)\ll1$). G adds seeds ($B^2$) and a logarithmic range of windows ($B$).
   - Fix: rewrite §3 in place to state that scope and point forward to G. Otherwise exporting "B, BARRIER-SCOPED" would carry a false barrier into FRONTIER.
2. **The Lane 4 pointer is dangling.** `GAP11_JLL.md` is not in this tree; it exists only on branch `side-agent/z82-gap11-jll`. Use the full path `notes/z82/GAP11_JLL.md` and state that it is unmerged. Its Theorem 4 does match the claimed $l^{\epsilon}$-loss versions of A.
3. **The alternative endpoint in §8 is misattributed.**
   - z79 Theorem L is proved on primorial fibres of depth $0<\sigma<\delta_G$, and on all primes by mixing. It is not at "$Q=1$".
   - The alternative also depends on Gallagher (G) and K.1's one-hit-per-ℓ argument, re-run for $n\equiv-e \pmod{\ell}$ (it does hold).
   - Fix the Theorem G label to "endpoint alternatively rel. z79 K.1/L and (G)", and drop "at $Q=1$".
4. **Gaps in the §0 Label and Triage.**
   - The Label omits §9's result conditional on Dirichlet GRH: $K_{\rm sub}\ll\log^2p$.
   - The Triage omits §9 entirely. I suggest §9.1–9.3 as BARRIER-SCOPED, merged into the S line.
   - §9.4 should be CONDITIONAL, with a FRONTIER §6 line next to the effective $K_{\rm sub}\ll p^{0.198}$ quoted there. It is a near-textbook Chebotarev/Bach–Sorenson consequence, so no record claim.
   - §9.2 is "rel. Bettin–Chandee via z80 §5.3"; the word "unconditional" should carry that qualifier.
5. **Corollary G′ label.** It also uses §6.2's conditioned comparison and product cutoff, so it should read "rel. A, §§6.2–6.3".

## Minor and form issues
- The Result phrase "with logarithmic-scale tails in G/G′" is vague. Name the three $K$ endpoints.
- "(★) need not be positive" in the Preflight is unclear. It should say that $R(p)=0$ rows are counted among the exceptions.
- In §9.1 "even $a$" is unnecessary; it is harmless, but say so or drop it.
- The Preflight says the 19-item screen is applied to §§9–10 but never runs it. One line per section would do.
- The script's "unique-list" control re-derives the same divisor-pair condition, so it is not an independent test. It never checks the distinctness or inverse-disjointness lemma (the structural core of G) or activation. I suggest asserting that the $2|\mathcal A_e|$ units are distinct for all labels with $K^{2\gamma}<e$ on a small grid.

## §§9–10 and F1–F4
- **§9.1 holds.** The $c_h$ are distinct primes, so $f=c_hD$ are distinct, $f\equiv-1 \pmod{4a}$, $4abd=p+a+b$, and every letter is $>U$.
- **§9.2 holds.** $(x,s)=(.01,.002)$ satisfies (W): $.01<.0217$. Winsorizing gives $|Z'-m|^v\le m^{v-2}|Z-m|^2$.
- **§9.3 holds.** Lenstra's exponents are $.29>1/4$ and $.34/1.34\approx.2537>1/4$. The matching bound $Z/(3\Delta)$ is fine.
- **§9.4 holds.** I checked the step that is not obvious: $(p/s)=+1$ follows only because $s<q$ (every prime below $q$ is a residue mod $p$), and $(b/s)=-(p/b)=-1$. With $q\equiv1\bmod8$, $s\equiv3\bmod4$, the 2-quotient is $C_{2^k}\times C_2$ and $p,b$ span its Frattini quotient. The direct Chebotarev bound is right too.
- **§10 Lemma F holds.** The missing cell is $M/2$, the involution. $D\ll q^{-2/5}$, $3/5>7/12$, $t$ is an integer, and the parameters land in C's band. It is correctly scoped as pointwise only.
- **F1–F4:** odd squares are excluded by the Jacobi argument (correct for composite $e$). The bound $X e^{-cL^{3/4}}\gg\sqrt X$ respects the square floor. Nothing is claimed at specified zeros. LM is consistent, since no exponent exceeds 3/4. I see no screen violations.

Priority: z79 J/L cover $f_{II}$ and $f_I$ tails in the large-gap orientation. Row 3 being a corollary of K.1/L is disclosed correctly. External priority for gap tails remains unverified, as stated.
</code-review>