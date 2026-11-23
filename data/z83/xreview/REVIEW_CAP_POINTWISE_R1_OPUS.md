<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of Wave z83 Lane 5 (notes/z83/CAP_POINTWISE.md). Scrutinize every pointwise packet/donor/carrier construction, every character-sum and least-prime input (literal hypothesis match), uniformity in all parameters, and every conditional implication with extreme rigor. Cap any replay at ≤15 min.

Commit log:
commit df55cc4687e40d1902d82dca263ffff7eb6c4eab
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 03:21:46 2026 +0100

    Bound multi-band capped CRT majorants and mixed prescribed carrier menus

 data/z83/cap_pointwise/check.txt |  6 +++
 notes/z83/CAP_POINTWISE.md       | 79 ++++++++++++++++++++++++++++++++
 scripts/z83_cap_check.py         | 98 ++++++++++++++++++++++++++++++++++++++++
 3 files changed, 183 insertions(+)

Review:
**Verdict: ACCEPT WITH MINOR FIXES.** I found no mathematical error in W, M, M′, Lemma S, Theorem S or the group diagnostic. The fixes needed are about labels, scope wording and the replay's value as a check. The triage (BARRIER-SCOPED, STATUS delta none) is right.

This covers the single commit `df55cc468`, which adds `notes/z83/CAP_POINTWISE.md`, `scripts/z83_cap_check.py` and `data/z83/cap_pointwise/check.txt`. No master files are touched, as lane rules require.

## What I re-derived

**Lemma W is correct.**
- Each term's expected value under the mixed law is a polynomial of degree at most `Σ floor(σs_i) ≤ σH`.
- For `z ≤ 1/e`, the density is at most `1 + z^k p/(1−p)`. Since `z^k ≤ e·e^{−σs}` (and this also holds at `k=0`), you get the stated exponential factor.
- Interpolating at `j/(ed)` gives `Σ|ℓ_j(1)| = (ed)^d 2^d/d! ≤ (2e²)^d`, so `C = log(2e²)`.
- Independence of the coordinates is essential, and the note states it. W is a simpler weighted-degree relative of `thm:kcomp`/`cor:kmean` in `paper/sieve-limits-note.tex`, not a restatement.

**Theorem M is correct.**
- Pinning unit fibres costs `O(log L)` by Mertens.
- Given a fibre, the pivot lists are independent by CRT, because the cofactors contain no pivot primes.
- Jensen over fibres is applied in the right direction.
- Each atom contributes at most `1/(φ(k)ℓ) ≤ H₀(f)/f`, and `ℓ^{−σ} ≤ f^{−v}`.
- I checked the shifted-weight step against UB: `(loglog 10u)² ≪ u^w/w`, then `w=v/2` with `ζ(1+v/2) ≍ 1/v` reduces the sum to `T(v/2)`. The truncated version gives `T(v/4)`.
- The parameter choices fit: UB's `w` gives `Lw` (needs `v ≤ 1/2`, true in every branch). The supercritical case falls back to `σ=2b`, giving `O(L)`.
- The `E=1` case gives `L^{4/5}`, consistent with C.
- Attainment is inherited from UB, because UB's class sits inside M's with `b=2C₀` and `δ=3/4`.

**M′ is correct.**
- Every class in `C_E(f)` has Jacobi symbol −1 at `f`. I checked this directly: `(q/f)=1` for `q|A`, `(2/f)=1` when `A` is even, and `(−1/f)=−1`. So each forbidden set has probability at most 1/2 with no light assumption.
- Pairwise coprimality makes the charged cost at most the true prime cost.
- Truncation with `D ≤ f^b` gives `D^{−v/(2b)}`, so only constants change, as claimed.

**Lemma S and Theorem S are correct.**
- The paid-power condition `v_q(K) ≥ max(1, j−2E)` follows from `v_q(A)=v_q(K)` on the `u` side and `v|K` on the other.
- Neutrality `(K,mp)=1` is automatic once `(m,p)=1`, so it costs nothing.
- (4): I re-checked the `C>p` branch: `m>3C`, `b₁v ≤ W₁`, `C_u | pb₁+v`, and `v ≤ W₁`.
- In Theorem S, the vector list is fixed before sampling, uniformly over all `p ≤ Y^{Ak}`. A hit forces `p ≡ −m (mod s)` on the whole support, giving probability at most `(2/(Y−1))^t`. The union bound is `Y^{−2/3+o(1)}`. The empty vector is correctly excluded.

**The group diagnostic is correct.** In `C₂×C₄` the element `(0,2)` is unreachable, while the Davenport constant is 5.

**The cited inputs match their sources literally:**
- z81 Corollary P: it needs `p ≡ 1 (8)`, which every hard class satisfies. Modulus `4t`, so Chowla gives `Y^{1+ε}`.
- HC windows and HC+GRH⇒cap one: consistent with z81 CAP_ZERO §6.
- z80 §11's `2L` corrections: consistent with z80 BEYOND_34.
- The 14 (★) zeros: the data file has 14 entries.
- The pointwise ledger matches STATUS rows 78–79.

**Replay.**
- The lane script finished in 0.4 s, and its output is byte-identical to `data/z83/cap_pointwise/check.txt`.
- My own check (`/tmp/z83rev/s_check.py`) is not a lane script and is not committed. It builds packets from scratch over `p ≤ 2500` (1 mod 8), `m ≤ 400`, five support primes, with legality computed from the Fraction itself. It found 506 legal neutral packets. All satisfy (4) and the paid-power claim, and none has support outside `K`.

## Issues to fix

1. **The §0 label leaves out the CONDITIONAL content.** §3's "PROVED (transfer…; conditional companion to Q)" includes a Chowla-conditional bound `e ≪ Y^{1+ε}`. Split it into PROVED for the unconditional `Y^L` and CONDITIONAL on Chowla for the rest, in both §3 and §0.
2. **The label inherits U's unrefereed input without saying so.** M's attainment rests on z82 U, which is PROVED only relative to the internal unrefereed (G)-consequence. "Matching construction in U/UB" should name that dependency.
3. **The F2 replay tests nothing relevant.** It tests numerator four on 11, 17, 131, 241 and the R₈ zeros, but those are numerator-8 controls. Either drop F2 from the CERTIFIED counts or state that it is vacuous. Also, F1 only asserts there are no `r>1` hits; by the Jacobi argument it could assert there are no hits at all.
4. **The CERTIFIED W check only tests the degree claim.** It confirms that `P(z)` has degree at most 8 on one toy example, not inequality (1). The note should say so, or add a tiny LP check of (1).
5. **Theorem M's hypotheses contradict its claims.** The statement says "1≤E≤λ" and then asserts the `λ≤E≤λ²` bound. Restate the hypothesis as `1≤E≤λ²`, with (2) for `E≤λ`.
6. **The Result line says "separated" bands, but M needs no separation.** Lemma W explicitly allows none. Say "distinct pivot scales under a fixed pivot/cofactor partition" instead.
7. **Two terms are undefined or leaked.**
   - "Neutral" and "nonneutral window" are never defined; say δ_p=0 as in z81 T.
   - "posited in the question" and "the proposed fourth-power corrections" are prompt leaks. Attribute them or remove them.
8. **Some sentences are unclear or misfiled.**
   - "M includes a square base and never forces a unit square hit" is unclear.
   - The STATUS-delta field carries a FRONTIER instruction.
   - Symbols collide: `W` names both Lemma W and the charging cutoff, and `b`, `B`, `b₁` overlap.
9. **M's selector scope is narrower than its proof.** The proof's unit restriction works for selectors at any non-pivot primes up to `N^a`, not just cofactor primes. Saying so makes containment of U's configuration obvious.

## On the substance

- M is a real but narrow strengthening. It shows that the single-band wall survives any number of pivot scales under a fixed pivot/cofactor partition. The natural escape, pivots reappearing inside other cofactors, is honestly left open.
- S is a clean counting obstruction: the menu primes are of size about `p^{1/O(k)}`, and only `Y^{o(1)}` targets are reachable against about `Y` classes per prime. It is not a lower bound on `e*(p)`, as the note says.
- Nothing here bears on ES itself. No claimed proof or disproof of ES is made or implied.
</code-review>