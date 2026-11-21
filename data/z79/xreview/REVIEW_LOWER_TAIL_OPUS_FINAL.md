<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Final independent hostile check by Claude Opus required on the explicit records in notes/z79/LOWER_TAIL.md §§4.4–4.5 at efd1ae41e: verify or reject C_s=K_s/(2·4^s s!), s=2,3, all-prime and single-fibre exceptional exponents, full hypotheses and possible hidden dependence on pinned atoms, width of log boxes and monotone comparison with weights. Check power transfer refusal to divide by a Siegel-small normalization except with matching factor. Prefer concise proof audit + necessary fixes only, not new targets. Inspect script and exact panel if useful (timeout ≤1800; ulimit -v 1200000; uv run --offline --no-project python). Write nothing to repo. Need a fresh independent assessment of the refinements, not a summary of previous reviews.

Commit log:
commit efd1ae41ed042b57dbc44c4a87570553f2440cea
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 13:32:01 2026 +0100

    Specify simplex-box hypotheses and the sharp s=2 corollary

 data/z79/xreview/REVIEW_LOWER_TAIL_OPUS_R2.md | 101 ++++++++++++++++++++++++++
 notes/z79/LOWER_TAIL.md                       |  20 +++--
 2 files changed, 113 insertions(+), 8 deletions(-)

commit 19b18e64277c994fa7df5a10ba57cd5a9f5ed6f5
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 13:16:14 2026 +0100

    Recover the almost-all cubic-log constant and quantify fixed-fibre exceptions

 data/z79/lower_tail_checks.txt             |   2 +
 data/z79/xreview/REVIEW_LOWER_TAIL_OPUS.md | 107 +++++++++++++++++++++++++++++
 notes/z79/LOWER_TAIL.md                    |  48 +++++++++----
 scripts/z79_lower_tail.py                  |  11 ++-
 4 files changed, 155 insertions(+), 13 deletions(-)

commit 542ea6ebbc5ae32245d4b46f8c45d0b1084449ab
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 12:56:36 2026 +0100

    Concentrate both ET bulk counts on a growing primorial fibre

 data/z79/lower_tail_checks.txt |  26 ++++++++++
 notes/z79/LOWER_TAIL.md        | 110 ++++++++++++++++++++++++++++++++++++++++
 scripts/z79_lower_tail.py      | 111 +++++++++++++++++++++++++++++++++++++++++
 3 files changed, 247 insertions(+)

Review:
**Verdict: ACCEPT the mathematics of §§4.4–4.5 at efd1ae41e.** I found no proof gap and no hidden dependence on the pinned atom. The fixes needed are to form and to the master-file wording. I re-derived each step myself instead of relying on R1 or R2. I wrote nothing to the repo; my scratch work is in `/tmp/ltr3`.

## Proof audit

**1. The constants C_s = K_s/(2·4^s·s!): verified for s = 2 and s = 3.**
- **Local factors.** At an odd prime q, the factor is E[1_{q∤(a,c)}·(1 + 1_{q|f}/(q−1))] = 1 − 1_{s=3}/q² + t_q/(q−1).
  - For s = 3, t_q = (q−1)²/q³. This gives 1 − 1/q³, and the factor at 2 is 3/4. So K₃ = (6/7)/ζ(3) ≈ 0.71306.
  - For s = 2 the factor is 1 + 1/q², and the factor at 2 is 1. So K₂ = (15/π²)/(5/4) = 12/π².
- **Mean.** The harmonic factor Σ1/(4acd) = (1/4)·vol·L^s and the simplex volume (1/4)^s/s! combine with the swap factor 2. This gives K₃/768 ≈ 9.285·10⁻⁴, above 1/(128π²) ≈ 7.916·10⁻⁴. It also gives K₂/64 = 3/(16π²) ≈ 0.0190, above 1/64.
- **Swap.** The identity ff′ = 16abc²d² − 4cd(a+b) + 1 = 4c²dp + 1 holds. Together with 2θ < 1/2 it keeps the swapped points out of every cube, and it forces a ≠ b, i.e. y ≠ z.
- **Injectivity.** gcd(a,b) = gcd(a,e) = gcd(a,p) = 1.
- **Counting convention.** Z53 §1 defines R(n) = #{(u,B,C)} and gets R ≥ 2N by the same swap. So the factor 2 matches both R's convention and ET's ordered f_II. D₂ is therefore exactly Z53 §9.2's sketched κ.

**2. Theorem E, the weighted row: verified.**
- **Local multipliers.** β_j·φ(g)/φ(f_j) = (1/f_j)·∏_{q≤B} g_q·1_compat·∏_{q>B} φ(g_q)·1_compat. The multiplier at q > B is nontrivial only for q | f_i.
- **Expansion.** The φ-telescoped expansion keeps coefficients ≤ k with k | h | m.
- **No pin dependence in the complete model.** At q > B the expected bracket φ(q^j)/φ(q^j) − φ(q^{j−1})/φ(q^{j−1}) vanishes for every j ≥ 1. So the complete model carries no dependence on the pin. K_s(B) is the same for the base row (m = Q) and for every pinned row, and it does not depend on r. It tends to K_s as B → ∞.
- **Error terms.** Every error term is an absolute power saving, uniform in the pin:
  - small-h completion, X^{−γ/2} and X^{−3γ/20};
  - pin deletion, X^{λ}/V_i;
  - large h in the complete model, X^{−λ};
  - large h on the actual box: 1/h, 1/D and k/(ACh), and k/V through the determinant cut. The cut needs only k/gcd(k,f_i) | Q, which I checked prime by prime.
  - the 1/f_j → 1/(4acd) replacement, relative X^{−γ} times O(L^s).
- **Variance.** E W_J² = Σβ_i²P(i) + E W_J·(M + O(X^{−κ})). This gives Var ≤ E W + O(L^s X^{−κ}).
- **Chebyshev.** Chebyshev then gives L^{−s} per fibre. Per dyadic interval that is X/L^{s+1} exceptions, i.e. π(X)/L^s up to X. So the rate is π(X)/log³X for D and π(X)/log²X for D₂.
- **Comparison with weights.** For the lower bounds no transfer is needed: f_II ≥ 2N ≥ 2W, and the center M^w = (K_s + o(1))·ΣH_J. The two-sided transfer to N about μ₀ is also valid for fixed t, because 1 − O(1/log B) ≤ β ≤ 1.

**3. Box form A′ and the width of the log boxes: verified.**
- **What the proof uses.** It uses only:
  - τ(m) = X^{o(1)};
  - λ = γ/20 and η = γ/5;
  - γ > σ + ε, for k/V ≪ X^{σ+ε−γ};
  - widths ≤ ε, which bound the determinant by X^ε·AC and |d−d_i| by X^ε·D;
  - widths ≥ w₀, for a bounded number of cubes and H_J ≍ L^s;
  - σ > 0, so that B → ∞.
- **Unused hypotheses.** The conditions 12σ < θ and σ + θ < 1/2 are indeed never used. The condition ε < γ/20 is superfluous but harmless.
- **Order of limits.** In D the order is right: ξ fixes the cubes, γ, θ, ε and σ, and only then X → ∞. The boundary strip t_j < γ costs volume O(γ).

**4. Power transfer (§4.2): verified.** The note never divides by a Siegel-small base count unless the numerator carries the matching factor.
- If the exceptional conductor divides Q, F's coefficient at ψ is exactly ψ(r)·E_r F/φ(Q). So F and the base share the same bracket.
- For ψ(r) = +1 that bracket is ≥ (1 − 1/e)·min(u,1), while the (G1) error is ≤ min(u,1)/10, with the u factor applied to both terms.
- For ψ(r) = −1 the bracket lies in [1,2].
- If the exceptional conductor does not divide Q, the base has no exceptional term and F's exceptional term is ≤ vX/φ(Q).
- Theorem E reuses this comparison with v = O(L^s) and a deterministic center; F ≥ 0 is all that is needed.

**5. Replay.**
- The script reproduces `data/z79/lower_tail_checks.txt` byte for byte.
- My own toy test computed exact conditional rows: s = 2, Q = 8·3·5·7·11, a,d ∈ [30,330], 30 pins, 15 of them chosen to have the most large primes. The pinned/base ratio was 0.954–1.055 for W and 0.951–1.060 for N.
  - This is consistent with the theorem but not probative: the box spans a 10× aspect ratio, so it is outside the ε-width regime. It is EVIDENCE only.

## Necessary fixes (form only)

1. **§0 Result line.** Add D₂: R ≥ (3/(16π²) − ξ)·log²p outside O_ξ(π(X)/log²X), rel. BV. The STATUS delta already replaces the R row with it.
2. **§0 Review line.** Replace "independent follow-up on refinements owed" with a pointer to this review, covering A′, D, D₂ and E.
3. **STATUS delta.**
   - Write the labels explicitly: "PROVED rel. BV" for the all-primes part; "rel. (G)" and "CONDITIONAL on GRH" for the fibre parts.
   - Keep the `Z53_PZ.md` / `paper/es-count-note` Thm C pointer for the superseded 1/64 row, plus the existing caveat that Akaka's claim concerns strict full Type II and does not by itself give the R bound.
   - The current wording "Both bulk counts concentrate even on…" is ambiguous; say "at their Haar means on almost all p ≡ 1 (Q_σ) in (X,2X]".
4. **Minor.**
   - The §4.4/§4.5 headings say "(after first review)", but A′ and D₂ were added after the second review.
   - Optionally drop the superfluous ε < γ/20 from A′, or say that it is only a convenience.

No claim about ES is made or implied. Every result is scoped to almost all primes, bulk-truncated counts, and fixed tolerance with ineffective constants, as the note says.
</code-review>
