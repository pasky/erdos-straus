<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of Wave z83 Lane 6 (notes/z83/BEYOND34_MOMENTS.md). Scrutinize every moment/concentration inequality (independence or dependency-graph hypotheses!), every sieve and large-sieve step, uniformity of constants in all growing parameters, and whether each claimed bound contradicts the campaign's own CRT-law sharpness results. Independently recompute key exponents. Cap any replay at ≤15 min.

Commit log:
commit 32f72b1ca2d4e5be33ff5773c93eeadf5cb9cbee
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 02:52:49 2026 +0100

    Match the bounded-gap CRT phase curve and separate balanced pair moments on intervals

 data/z83/b34_moments/checks.txt |   6 ++
 notes/z83/BEYOND34_MOMENTS.md   | 142 +++++++++++++++++++++++++++++++++++++
 scripts/z83_b34_checks.py       | 152 ++++++++++++++++++++++++++++++++++++++++
 3 files changed, 300 insertions(+)

Review:
**Verdict: ACCEPT WITH MINOR FIXES.** I found no fatal error and nothing that contradicts the campaign's earlier CRT-law sharpness results. The main risk is inherited: V rests on the internal, unrefereed comparison and LP-duality machinery (`sieve-limits-note` `kcomp`/`wseq`, z80 LM), not on anything new in this note. This is one cross-lab review; the RECORD claim for I still needs the gate.

## What I checked independently

**Exponents, by hand and numerically:**
- **Row 3 of V.** Maximising u(h) = (1−β+βh)/3^h gives 1−β+βh = β/log 3. That yields u = β/(z log 3), z = 3e·3^{−1/β}, and h ∈ (0,1) exactly when b₀ < β < log 3.
- **The phase line.** β(1−h) + uz = 1 holds on the whole interval to machine precision.
- **Balance point.** Setting K^{1−h}s^z/√l = L gives s* = L^u l^{1/(2z)} and W = L^{1−u} l^{−1/(2z)}.
- **Rows 1 and 4.** Row 1: B s*³ = L gives W = L^{2/3}B^{1/3}, and B³ ≤ W holds exactly when B ≤ L^{1/4}. Row 4: K^{1−h}s*^{3^h−3} = O(1) with h = 1 − 1/√l, giving L^{2/3} l^{1/6}. Both match z82 G/G′.
- **Corollary I.** β − uI(z) = 1 − u, which is z81 Thm C's δ. The l-powers come to (z−1) + (1/(2z)−1)(z−1) − 1/2 = −1/(2z). The transfer condition MT ≍ c·c₀^z·L holds. At β = 1, 1−u = 0.665142, which is z81's δ₀.
- **Monotonicity in β.** d log u/dβ = (β − log 3)/β² < 0, so W increases with β. Rows 3 → 4 → 1 are monotone (l^{−1/(2z)} → l^{1/6} → l^{1/3}).

**No conflict with earlier CRT results:**
- **z82 B.** Its truncated-void exponent d = β − uI(a/u) needs d + u < 1, which forces u < u* and hence d < 1 − u*. So B's polynomial-level majorant is consistent with V's model floor.
- **noBcap and row 2.** Row 2's L^{3/4} is consistent with the full-ES CRT ceiling of `noBcap`.
- **V's law.** It is an LP-dual law, not Haar, so the small Haar mass of the void is irrelevant to it.

**Concentration and independence steps** (the specific hostile ask):
- **§2.** It explicitly avoids any independence assumption; costs are charged through inflation bounds of the form Γ(m)/m.
- **Lemma P domination.** One window's rough-prime bits are stochastically dominated by independent Bernoullis with b_t = γ_t/t. This is a valid sequential coupling. It is applied only to the *increasing* quantity min(1, A·3^J), and only then is the pointwise, non-monotone damped bound used. The order is correct.
- **Lemma P tilt.** The tilted Bernoulli parameters, the characteristic-function bound exp(−2 sin²(ξ/2)Σb′(1−b′)), and the factor 3^{−min(h,1−h)|y|} are all correct. Because that factor's constant is ~1/min(h,1−h), restricting row 3 to fixed β is necessary, and the note does so.
- **M.** It uses exact conditional independence given the small digits on integer CRT, which is legitimate: hits at one r are disjoint by z75's distinctness argument (w | k−k′ with w > K). The Bernoulli mgf bound gives (Ct²j)^j for j ≤ c₂t².
- **The repair trick in M.** Resetting nonunit multiplier digits to 1 is what makes z75 (2) hold uniformly with h(J) = h(J₀). It is correct, and the majorant ≥ 1_{Z<c₁t²/2} holds pointwise on all integers.
- **M's saving.** Recomputing j·log(t²/(C′j)) gives F as stated in both regimes.
- **Lemma S.** I checked the τ(a+b) hyperbola step, the Rankin tail at 1/4, the Z_y⁴ localisation with dyad sum O((log y)²), the heavy-leak union bound Σ r^{1/2}E p_r² ≲ Σ r^{−5/4}(log w log r)^C → 0, and that the dependence on w is explicit. All fine.
- **D.** ∑_n Z² ≤ X^{1.316+o(1)} is below X^{1.352−.01}. In the large-gcd case, a′ ≡ a (mod g) forces d′ ≡ d, giving mass ≪ 1/g + 1/A + 1/D + g/(AD). The explicit pair has q′ = q+4 and (b−b′)q = 4b′−1 with 0 < 4b′−1 < q, so it is empty. z80's Haar lemma does give an additive X^{−κ} error.
- **EH step for D.** The Cauchy step over τ(q+1) multiplicities is fine.

**Replay:** `scripts/z83_b34_checks.py` runs in 0.3 s and its output is identical to `checks.txt`. The 3,200 and 672 counts check out. The four clause combinations 00/01/10/11 all occur, so clause 2 is genuinely needed.

## Issues to fix

1. **The "Interpretation" paragraph is labelled PROVED but is only a sketch.** It is the step that embeds z82 G/G′ into the unit-marginal class. It covers the 1/r → 1/(r−1) change, the 1/(r−J) odds, the envelope signs and "no nonunit small digit to repair" only in prose. Either write it as a short lemma or relabel it "PROVED (sketch)". The *lower* half (no polynomial-level test can beat W) follows from V alone. Only "the rates are attained" needs z82.
2. **Triage.** M is a positive trade-off theorem, not a METHOD-CX. For γ < 1/3 it is implied by z75 except for the height restriction exp(Ct). Suggest NULL/DATA, or RECORD for the γ > 1/3 tail only.
3. **D is oversold in the Result line.** "Separates … already at order two" is close to tautological once lcm(q_i, q_j) ≈ X^{1.35} exceeds X: it is a counting argument, realised pairs ≤ X^{1.32} against ≈ X^{1.35} cells of similar Haar mass. The body admits that S_X depends on the interval. The Result line should say "with an interval-selected coefficient set of size X^{1.3+}".
4. **The STATUS delta needs scoping.** Add "on the numerator-four window chart, exact unit marginals on moduli ≤ X^{A₀}; model lower bound" to the sharpness sentence. The target row (STATUS l. 110–111) is already at or near the 6-line cap, so propose a compression rather than an addition.
5. **Notation overload hurts reviewability:**
   - V is the theorem, the avoider set and the dyad scale in (1).
   - D is the theorem, D_h, the lcm in (2) and r^v.
   - w is the small-prime base, the rectangle width .0001 and the odd label in M.
   - h, u, M and W also each carry two or three meanings.

   Rename locally.
6. **Minor points:**
   - In (2), the √V remainder needs Σ_{h≤V^{1/4}} g(h)√V ≪ V^{5/8+ε} ≪ V/D. It is true but not stated.
   - In Lemma P, the 2·r^{−1} translate/inverse factor is redundant (the script shows t ∈ {1, n, n^{−1}} already covers it). It is harmless and worth one clause.
   - Label line: mark `sieve-limits-note` explicitly as internal/unrefereed.
   - Result line: it is two claims; AGENTS asks for one sentence.

## Debate points (not defects)

- **V adds little beyond z80 LM.** Its genuinely new content is Lemma P: distinct-digit counting with a 3^h tilt and the 1/√H anti-concentration. That lemma is what makes the l-powers match G′ exactly, which is a strong internal consistency check.
- **I is the obvious interpolation of G′.** It is G′ at s = z instead of s = e, so the risk is low but so is the novelty. It improves z81 only by the factor l^{3/2 − 1/(2z)}, and no primary exponent changes.
- **Endpoint jump at β = log 3.** The jump l^{1/6} → l^{1/3} between rows 4 and 1 is real (the totient sum K^{1−h} blows up for β > log 3), and it matches z82. It deserves one sentence in the note so readers don't take it for a typo.
</code-review>