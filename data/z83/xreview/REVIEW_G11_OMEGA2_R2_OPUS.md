<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="8aef255ed">
A separate reviewer subagent was asked to review the changes in `git log 8aef255ed..`. Its request and review follow.

Request: review changes since 8aef255ed carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus Round 2 review of notes/z83/G11_OMEGA2.md §§7–10 and scripts/z83_g11_{curve,weighted,four}.*. Challenge literal Zhang/Polymath8a/Maynard matches, exact MR weights and capped recurrence, all signs/ranges/constants, primitive Eisenstein lattice Poisson error, W normalization and four-first-pins DP. Independently recompute key signs including the .18 weighted result and .578 curve, verify some/all outputs, cap total replay at 15 min. Respect 2 processes, ulimit -v 6000000; do not modify tracked files or leave artifacts. Include verdict and fixes.

Commit log:
commit 510d863a5843cecffc7ea231985e63b77e4e225d
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 04:15:03 2026 +0100

    Give signed mixed root rectangles and lower weighted two-factor level to .18 by norm lattice switching

 data/z83/g11_omega2/curve.txt      |  16 ++++++
 data/z83/g11_omega2/four.txt       |   4 ++
 data/z83/g11_omega2/roughcurve.txt |   6 +++
 data/z83/g11_omega2/shapes.txt     |   8 +++
 data/z83/g11_omega2/weighted.txt   |  16 ++++++
 notes/z83/G11_OMEGA2.md            | 108 ++++++++++++++++++++++++++++++++++++-
 scripts/z83_g11_curve.c            |  53 ++++++++++++++++++
 scripts/z83_g11_curve.py           |  23 ++++++++
 scripts/z83_g11_four.py            |  15 ++++++
 scripts/z83_g11_weighted.py        |  47 ++++++++++++++++
 10 files changed, 294 insertions(+), 2 deletions(-)

Review:
**Verdict: ACCEPT with fixes.** The changes since `8aef255ed` (commit `510d863a5`) contain no sign, rounding or normalization error that I could find. Every certificate replays exactly. The key numbers were checked against the z82 reference engine or my own independent recomputations. What needs fixing is scope and §0 form, listed below. No ES claim is made, and none is implied.

## Replay
All runs used `ulimit -v 6000000`, at most 2 processes, about 4 minutes of compute in total, in a temp directory. No tracked files were touched and the temp files were removed (the shared `/tmp/r2rev` already held another session's files, so I deleted only mine).

- **Outputs:** `curve.txt`, `shapes.txt`, `roughcurve.txt` (with `G11_H=6`), `weighted.txt` and `four.txt` all match byte for byte. The largest run took 11.6 s and 103 MB RSS.
- **.578 cross-check:** I ran the reviewed z82 Python `arraytable` engine, a separate implementation from the new C code, at J=2312, B=360, i=1611, τ′=.49999.
  - lower .50104 (C engine .49988), C₃ .29359, C₇(h≥4) .20628, net **+.00118** (C engine +.0000150).
  - At J=2308 both engines are negative.
  - So .578 holds in both engines, and the C port is the more conservative one.
- **Theorem E cross-check:** the Python engine at G=6000, B=422, i=2185, h≥6 gives net **+.00218** (C engine +.00110).
- **.18 weighted result, my own float DP:** I implemented it from the §9 text alone, with exact ½log pin masses and my own V_κ. At t=.18, b=.154: lower 1.0641865, upper 1.05413, margin **+.0101**. The certificate's upper of 1.05946 sits above this, as it should. At a finer mesh (G=8000) the margin is +.024. At t=.175, b=.15 it is negative in both.
- **V_κ:** direct quadrature gives V(2)=1.05642 and V(3)=1.15018. The script's integer values (1.05628, 1.14994) are lower bounds, as required. I re-derived V′=(1−1/w)^κ V(w−1)/(2w) by endpoint differentiation and rescaling.
- **H₄:** singularity-free quadrature gives H₄(1/.07)=.0978043, inside the certified [.0976847, .0979152]. At b=.187 and .188 the values .00098327 and .00092585 are also inside their brackets. So C₄ crosses .00331495 strictly between .187 and .188.

## Substance checks (all pass)
- **Normalization M·C_p = e^{−γ}C_W:** I redid this by hand.
  - The local ratio is (ℓ²−1)/(ℓ²+χℓ) = 1−χ/ℓ.
  - The small-prime densities are 3/4, 6/9, 6/25, 6/49.
  - With L(1,χ)=π/(3√3), the total comes to exactly 1.
  - I also confirmed that the factor 2 in C_W=(2/192)∏(…) is genuine. It comes from R vanishing on n≡2 mod 3; a naive Euler product misses it.
- **Densities:** h=1/(ℓ+χ) and g=h/(1−h)=1/(ℓ−1+χ) both match Lane 4's g_prim. The lower function 2 asinh√(t/b−1)/√(πt) is f_{1/2} written in U_w units. The terminal charge Γ(5/2)/η^{3/2} follows from the Selberg asymptotic with C=C_pV, since (1−h)(1−g)=1−2h.
- **Lattice Poisson error:**
  - The two-variable Gauss sum has an s-independent unimodular phase, which leaves a Kloosterman sum.
  - The per-q error is (X/q²)·2^ω√q·(q/√X)² ≍ √q, including when q<√X, by rapid decay.
  - The total is Q^{3/2+ε}, with 1.5·.6665 < 1.
  - Pins times the Selberg level stay ≤ X^{.6665}, and η=C/2 ≤ i keeps every sieve test valid.
- **Four-pins DP:**
  - The partition by the first four bad primes is exhaustive.
  - R=1−s−(4−k)i correctly bounds the good part, so the extra good roots above X^R are legitimate.
  - The range of the last bin is covered, and the sentinel and early-exit choices are conservative.
  - All bounds are rounded outward and all signs are positive.
- **MR⁻ and capped recurrence:**
  - The vector inequality L₀U₃U₇+U₀L₃U₇+U₀U₃L₇−2U₀U₃U₇ ≤ 1 holds; it is decreasing in each U≥1, and ≤0 if any factor fails.
  - The Buchstab child directions are right: superset at i−1 for the lower parent, subset at i for the upper.
  - The C engine's half-log bounds x/2 and x/2−x²/4 are valid.
  - The rectangle caps are path-independent, since the pins spend J−c.
  - I checked that the caps are monotone: tightening C₃ or C₇ only lowers the net.
  - D(θ) for θ>.578 does imply MR⁻.
- **Literal theorem matches:** I fetched both papers.
  - Zhang (2.5), (2.9) D₁=x^{1/1168}, Thm 2 (2.12) for each fixed i, and k₀=3.5·10⁶ are all literal.
  - Polymath8a Thm 1.1 (one class per prime, combined by CRT), Def 2.1 (1≤R≤yn), Def 2.2, Claim 2.3 (a coprime to P_I, I may vary), Thm 2.4(i) (600ϖ+180δ<7) and Lemma 2.10(iii) are all literal.
  - The {0,3,7} parity argument is correct.

## Required fixes
1. **§0 Result overstates G.** "a primitive-weight lower sum at .18 suffices for two factors" puts G alongside F. G actually gives W-mass ≫X/L^{3/2}, hence ≫X/L³ *distinct* primes, with bad factors ≥X^{.154}; F gives ≍X/L² with ≥X^{.09}. State G's count and cutoff in the Result line.
2. **§0 Review and Triage are stale.** They describe R1 only. Mark §§7–10 as "cross-review owed" until this review is recorded, and add E (RECORD), F (conditional) and G to Triage.
3. **Dangling pointers.** `THIN_DISP.md`, "Lane 4 §3/§9/(17)/(21)/(23)" and `32c0fe00d` exist only on `main`, which this branch does not contain. Merge main before export and write the paths as `notes/z83/THIN_DISP.md`.
4. **Undefined convention.** "(η,η′) in the requested per-axis convention" is never defined. From the data, η is the d₇ exponent and η′ is the d₃ exponent minus ½, and "(.18,0)" is really (.18,−.00025) because C₃=1999/4000. Define the convention in the note.
5. **"This gives precisely the union …"** should read "the support is contained in". The note itself says later that these are support upper bounds only.
6. **§8, small-a recipe.** Formula (1) needs a>τ′/2, so at a<7/180 the 2.8 figure is not a valid bound. The conclusion still holds a fortiori, because a Selberg cutoff ≤X^a only raises the cost to ∝1/(2a−b). Say so, and label the passage Assessment only.
7. **§8, randomization weight.** The weight is 2^{−ω₂(q)}, where ω₂ counts primes with two available roots, not 2^{−ω(q)}.
8. **§10, unnamed conditional theorem.** It re-instantiates an observation already in THIN_DISP line 165 (ν=.0225). Name it, credit it as a Lane 4 corollary, and either add it to the §0 Label or downgrade it.
9. **Replay writes into a tracked directory.** `curve.py` hard-codes `data/z83/g11_omega2/curve.bin`. Take the binary path from an environment variable or a temp directory instead.
10. **Unlabelled data.** `weighted.txt` has no column labels (they are t, b, lower, upper, margin).
11. **Notation collisions.** W_X (the §7 weight list), W_p (the §9 weight), Lane 4's Theorem W and §3's W (largest good-prime exponent) clash. So do U₀ (presieve polynomial vs §3's U₀), h (bad count, H index, local density h(ℓ)) and g (gap vs density). Rename W_X at least.

## Non-blocking observations
- E's cutoff 211/3000 and F's .578 are limited by the engine, not by the method. The z82 Python engine has about .001 more margin at both points, mostly from the cruder half-log bound in the C code. Either a finer C bound or quoting the Python result would be stronger. Not claiming optimality is correct as written.
- The rectangle and shapes rows (for example d₃≤X^{.49975}, d₇≤X^{.18} at total .675) are sufficient conditions on lists that no published theorem covers. The note already says this.
</code-review>