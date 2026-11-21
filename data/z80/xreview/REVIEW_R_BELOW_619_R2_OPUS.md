<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review. The author is a GPT-6.2 Astra lane. Re-derive every stationary-phase step, range condition, exponent-pair application and rational exponent optimisation of notes/z80/R_BELOW_619.md; check cited theorems against published hypotheses. Focus on all R2 additions at 101e82f00, §§1.3,5.1–5.2. Prior three reviews cover everything else. Stress-test signed D and k transforms and the scoped barrier, conditional normal order incl matching upper, unconditional BT central bound, parity split/conic at 2, transferred Type II inverse atom, disjointness, optimized constants/levels incl witness BV/BT. Flag all required wording, arithmetic and replay fixes. Read-only. Python only under ulimit -v 6000000; timeout <=1800 uv run --offline --no-project python -B. Return a full verdict by theorem.

Commit log:
commit 101e82f00951df4733193d101ebf0fc381e79051
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 18:49:28 2026 +0100

    Pool the disjoint four-prime phases and isolate the central prime moment; split both parities and enlarge Type I/II charts

 data/z80/r2_central.txt   | 11 ++++++
 notes/z80/R_BELOW_619.md  | 69 ++++++++++++++++++++++++++++++++++---
 scripts/z80_r2_central.py | 86 +++++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 161 insertions(+), 5 deletions(-)

commit 365f218852303c4755a5f29ef7a8293bc11cac4b
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 18:25:56 2026 +0100

    Check the BM-relative reading against the archived prime window

 data/z80/r_below_619.txt   |  1 +
 notes/z80/R_BELOW_619.md   |  2 +-
 scripts/z80_r_below_619.py | 14 +++++++++++++-
 3 files changed, 15 insertions(+), 2 deletions(-)

commit b123a3c6fe1d00cdec3407b91180291783bef46c
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 18:24:20 2026 +0100

    Quantify the remaining loss even for square-root individual lift estimates

 notes/z80/R_BELOW_619.md   | 2 +-
 scripts/z80_r_below_619.py | 2 ++
 2 files changed, 3 insertions(+), 1 deletion(-)

commit e072ed09d53749ec0680ada2f157d30c719226c2
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 18:23:18 2026 +0100

    Calibrate the signed enlarged norm and state the BM-relative lower tail

 data/z80/r_below_619.txt   |  5 +++++
 notes/z80/R_BELOW_619.md   |  6 +++---
 scripts/z80_r_below_619.py | 38 ++++++++++++++++++++++++++++++++++++--
 3 files changed, 44 insertions(+), 5 deletions(-)

commit 3511ec8cab50776c5fda7743bd0d622b25d40ff0
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 18:21:18 2026 +0100

    Apply final Opus fixes and replay mixed kernels and the disjoint chart count

 data/z80/r_below_619.txt                     |  17 ++--
 data/z80/xreview/REVIEW_R_BELOW_619_OPUS3.md | 120 +++++++++++++++++++++++++++
 notes/z80/R_BELOW_619.md                     |  34 ++++----
 scripts/z80_r_below_619.py                   |  77 ++++++++++++++++-
 4 files changed, 225 insertions(+), 23 deletions(-)

commit 97c86735e81bb9a1e470abb683ef8a434a02ce91
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 18:07:15 2026 +0100

    Control primitive mixed traces and improve the intermediate numerator range

 data/z80/r_below_619.txt   |  9 +++++++-
 notes/z80/R_BELOW_619.md   | 56 ++++++++++++++++++++++++++++++++++++++++++++--
 scripts/z80_r_below_619.py | 46 ++++++++++++++++++++++++++++++++++---
 3 files changed, 105 insertions(+), 6 deletions(-)

commit 695bfb2b06db5e2adc5de5003e21f4905cd6e408
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 17:51:40 2026 +0100

    Archive second independent Opus acceptance and clarify partial-pin scope

 data/z80/r_below_619.txt                     |   2 +-
 data/z80/xreview/REVIEW_R_BELOW_619_OPUS2.md | 108 +++++++++++++++++++++++++++
 notes/z80/R_BELOW_619.md                     |  28 +++----
 scripts/z80_r_below_619.py                   |   2 +-
 4 files changed, 125 insertions(+), 15 deletions(-)

commit d21e482f5ded562f70498ce36ea0551e3f1625c4
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 17:33:59 2026 +0100

    Reverse the partial pin to control mixed-period collisions in balanced boxes

 data/z80/r_below_619.txt   |  1 +
 notes/z80/R_BELOW_619.md   | 30 ++++++++++++++++++++++++++++++
 scripts/z80_r_below_619.py | 29 +++++++++++++++++++++++++++--
 3 files changed, 58 insertions(+), 2 deletions(-)

commit b11b31cdb3966358823f51ec6c00504ff994340c
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 17:31:24 2026 +0100

    Apply Opus scope and provenance fixes and archive full review

 data/z80/xreview/REVIEW_R_BELOW_619_OPUS.md | 90 +++++++++++++++++++++++++++++
 notes/z80/R_BELOW_619.md                    | 18 +++---
 2 files changed, 100 insertions(+), 8 deletions(-)

commit f2c0476308d36df42fbbdcee5e9619d368bde6ea
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 17:11:30 2026 +0100

    Transfer centered word moments with an upper sieve; gain for large numerators

 data/z80/r_below_619.txt   |  17 +++++++
 notes/z80/R_BELOW_619.md   | 109 +++++++++++++++++++++++++++++++++++++++++++++
 scripts/z80_r_below_619.py |  96 +++++++++++++++++++++++++++++++++++++++
 3 files changed, 222 insertions(+)

Review:
**Verdict: ACCEPT with minor fixes.** I found no mathematical error in the R2 additions at 101e82f00 (§§1.3, 5.1, 5.2 and (I)). I re-derived every step listed below by hand and replayed `scripts/z80_r2_central.py` under `ulimit -v 6000000`. Its output is byte-identical to `data/z80/r2_central.txt`. The fixes are wording, scope, provenance and replay detail.

## §1.3, signed pooling in D and the common-integer barrier — ACCEPT (METHOD-CX)

**What checks out:**
- **Setup.** UVW = P¹⁹ ≍ n, and E = P²W/V = P. D = hR − h′Q ≍ P³ is positive and determines (h,h′), because Q | h−h₂ and |h−h₂| < δP < Q.
- **Windows are primitive.** Since h < 2δP < q, r, no window frequency is divisible by a local prime.
- **Poisson in x.** Σ_x g·F = Σ_k c_k ∫F e(kx/m), with the sign convention matching (S).
- **Stationary point (re-derived).** φ′ = 0 forces k < 0 with |k| = nD/(4x²) ≍ P¹⁰. The critical value is −√(nD|k|)/m exactly, T = P¹², and the leading term is W/√T with error O(W T^{−3/2}) (Hörmander 7.7.5 on a compact family).
- **Error budget.** With |c_k| ≪ m^{−1/2} at every k for disjoint pairs (single-trace bound from (K)), the error is P¹⁰·P²·P^{−14}/P² = P^{−4}. ✓
- **Poisson in h.** I re-derived the formula, including u = j − ℓQ, the periodicity of χ_Q(f(x,·)) and ŵ evaluated at (u₀−u)E/Q. (S′) is exactly the original x-sum, with 1/E² absorbed. The script matches to about 1e-16.
- **Barrier.** ŵ(0) ≫_δ 1 because Φ̂ is near Φ̂(0) > 0 at the small argument hV/(4QC) ~ δ. For x ≢ 0 mod p, f(x,·) has degree 2; for x ≡ 0 it is −4u + n², which is nonzero. So there are ≤ 2 roots per prime p ≍ P in a window of length 2cP < p. This gives a cost ≫ WP/P² = W/P against the budget W/P², a loss of P. With √P cancellation per x the cost is W/P^{3/2}. ✓
- **Scope.** The barrier is correctly limited to the absolute u = v triangle, with the signed u = v sum left open. Note that this sum is essentially a Jacobi-symbol sum of (4xu−n)² − 4u along the hyperbola 4xu ≈ n, a natural direct target.

**Required fix.** The parenthetical "(restrict to t near 6/19 so T→∞)" gives the wrong reason. In general T ≍ n^{2t}, which tends to infinity for every t > 0. The (S′) lower bound uses no stationary phase and needs only t < 1/3. The real constraint is on the stationary-phase replacement in (S): its error is m^{1/2}T^{−1/2} = n^{2−7t}, and the budget is n^{7t−2}. Both require t > 2/7. Restate the parenthetical in those terms.

## §5.1 (G), geometry — ACCEPT

- Corners have mass θ²; the complement is a reflected simplex of side 2−3θ.
- F(1/2) = 3/4, F(4/7) = 45/49, F(2/3) = 1.
- The density K₂L²/4 per unit planar area, times area ½, gives 3L²/(2π²) = M₀. This is consistent with §4's 9/(8π²).

**Wording fix:** "six permutations" should be "three two-letter charts".

## §5.1, conditional on (H) (lower bound and matching upper bound) — ACCEPT (CONDITIONAL)

- **Lower bound.** Expanding the prime variance gives exactly the Haar variance plus the left side of (H). The §4.1 lemma at v = 2 gives Haar variance O(L²) on rectangles away from the axes and tie planes, for any polynomial period size.
- **Sieve form.** Positivity, P_zG ≪ 1/L and the o(L³) and o(L^{−1}) scales all check out.
- **Upper direction.** Brun–Titchmarsh (Montgomery–Vaughan) gives the cell factor 2/((1−log q/L)φ(q)). The bound q/φ(q) ≤ 2(a/φ(a))(b/φ(b)) holds. The r ≤ D^{1/2} split costs O(D^{−1}log D) plus τ(q)D^{−1/2+o(1)}, so each dyadic box has O(1) harmonic mass. Strip mass is O(ηL²), then Markov, then η → 0.
- **Partition and unit cells.** Words decompose exactly into rectangle counts plus strips under the largest-letter assignment. The unit-cell claim for prime p holds.
- **Noted:** for θ < 1/2, (H) is already a theorem by (5), consistent with F = 3θ².

## §5.1, unconditional Brun–Titchmarsh central bound — ACCEPT

- The mass of {max < u} is (3u−1)², so the density is 6(3u−1).
- B_c = 12∫_{1/3}^{1/2}(3 − 1/u) du = 6 − 12 log(3/2) ≈ 1.1344.
- The tail bound min(1, B_c/s) and the mean bound 3/4 + B_c ≈ 1.884 are correct.

**Advisory:** the tail bound only bites for s > B_c, i.e. thresholds of about 1.88·m_*. Saying so would stop it being read as near-sharp.

## §5.2, parity split — ACCEPT

- **Trial charts.** d is a small coordinate and 4ad−1 is odd. Restricting d's parity leaves the period's residues at odd primes unchanged (CRT), so the harmonic sum halves up to a power-small error.
- **Pair chart.** The target −a−b+4jab is a unit mod 8ab, and φ(8ab) = 2φ(4ab) since exactly one of a, b is even.
- **The odd-factor claim needed a check, and it holds.** One might worry that the slope 4ja−1 vanishes mod an odd prime r. But odd primes of the period 8ab divide ab, and there 4jab ≡ 0. So the target agrees with the unsplit −a−b at every odd prime power that matters.
- **At 2.** The target is uniform on odd residues, as it is unsplit.
- **Spike and stripping.** k′/(2,k′) divides 4ab and 4a′b′, so compatibility still forces the sum congruence. ✓

**Wording fix:** state explicitly that j ≡ d mod 2.

## (I), the multiplier Type I/II chart — ACCEPT; constants verified

- **Identities.** Type II: 4abcd = c(p+e) = pc + a + b. Disjointness: (4ab)(4acd−1) = 4a(a+cp) > X. With 4ab ≤ 4Y^{21/19} < X^{1/v} and trial periods < X^{1/v}, the product is < X at v = 2 with strict margins.
- **Haar laws coincide.** Inverting units maps the cell n ≡ −e^{−1} to n ≡ −e, so the Type I and Type II Haar laws agree, including all factorial moments.
- **Injectivity.** It holds, and swapped witnesses fall outside the chart because b > u.
- **K.1 ranges.**
  - The BV constraint e ≤ x^{1/2−δ} needs γ < 1/3.
  - Distinct targets at each ℓ need γ < 2/3 and 2K² < Y^β.
  - The K⁴/Y^β term needs β > 4/19.
  - The K²/Y^β completion term is negligible.
  - The level condition is (4Y^{21/19})^v < X^{1−δ}, i.e. λ < 19/(21v).
- **Center.** I recomputed log(3/2)·(γ−β)/(14·19²ζ(3)). The identity 2(19/21)³(1/3−4/19)/(14·19²) = 1/(3·21³) is exact.
- **Fixes:**
  - "Optimized" is inaccurate. In this constraint family the continuous maximum of log(1/α)(α/2−4κ)κ²/(1+2κ)³ is at κ ≈ 0.0545, α ≈ 0.691, which is about 0.5% larger. Say "near-optimal rational choice".
  - State the magnitude: b₂ ≈ 1.52·10⁻⁶ against 1/(112ζ(3)) ≈ 7.43·10⁻³, about +0.02%. A reader of STATUS should not mistake this for a substantive gain.
  - (I) supersedes §4's Type I coefficient. b_v is about 16.6 times 2C_I(25/(26v))³ for every v. So the §0 Result clause "an eightfold Type I endpoint gain" is now stale. Mark §4's Type I paragraph "superseded by (I)" and drop or reword that clause in §0.

## Form, provenance and replay fixes (required)

1. **§0 Review line.** It still describes only the three earlier reviews. Add that §§1.3, 5.1, 5.2 and (I), plus the post-OPUS3 commits e072ed09d, b123a3c6f and 365f21885, are "cross-review owed", or cite this review.
2. **§0 Triage.** §5.1 has no class. Suggest METHOD-CX/BARRIER-SCOPED for the level assessment, a TARGET candidate for "(H) at θ = 2/3 implies point-mass normal order", and no STATUS §1 row for the conditional result.
3. **F2 provenance.** `notes/z80/EXTREME.md` is not in this tree. It exists only at commit c72d66110 on `side-agent/z80-extreme`. Give the full path and branch, and mark it unmerged. Also, "all 42 words are odd-d" follows automatically from R₈ = 0; say "hence".
4. **Replay wording.**
   - The test windows check only the h-Poisson step, once per window (centers c = .7 and −.9), not the x/k transform. Replace "check both signed transforms in (S′)" with "check the h-Poisson identity for both windows".
   - The text cites "the listed cutoffs" (a < 80, b < 81, d ≤ 10, 2-power valuations 1–5), but they appear neither in the note nor in the data file. Print them.
   - `multiplier()` checks the parameter identities, not injectivity; rename its printed label.
5. **STATUS delta.** It is accurate as written: rates log^{−2}/log^{−3} at v = 2, and log^{−v}/log^{−3v/2} in general. Add "(≈ +2·10⁻⁴ relative)" after b₂.

## Earlier commits (outside my brief, spot-checked)

- The b123a3c6f exponent 4(1−3t) − t/2 equals 1/19 at t = 6/19 and 0 at t = 8/25. ✓
- The 365f21885 control against reading §5 as a threshold is properly scoped.
- The BM-relative one-sided bound (3/4 − ε)M_BM follows from (6) and §5. ✓
</code-review>
