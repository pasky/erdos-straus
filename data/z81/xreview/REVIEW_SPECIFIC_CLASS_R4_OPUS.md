<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="35c8495c0">
A separate reviewer subagent was asked to review the changes in `git log 35c8495c0..`. Its request and review follow.

Request: review changes since 35c8495c0 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus R4: audit ONLY Round 2 (notes/z81/SPECIFIC_CLASS.md §§6–8). Check degree-growing marked-set coupling (no hidden k-dependent constants), Henriot 2014 erratum New Thms 5/6 applications and fixed-k joint LOWER/specific-hit subtraction, prime upper, rare-window exponent, the .751 character-kernel shifted-function conditional (M), scope and necessity, square tests, and especially the unconditional 4/5 Record for constant cap one with composite reduced root C1 (valuation dictionary at composites, (10) lattice at each pin, incidence/BV, disjointness and finite transfer). Check whether (M) in its uniform arbitrary-function form could be refuted; recommended restrictions if appropriate. Verify distinction from a single overflow prime and no false integral ES improvement. Do not write files; cap any computations at 5 minutes, use memory limit. Please report any real gaps, not just cross-refs; distinguishes RECORD for relaxed family only.

Commit log:
commit 6df48876a14bbad4c271f6fe3db4c5e684a5ac4d
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 16:19:36 2026 +0100

    z81: prove joint window laws and a four-fifths bound for squarefree overflow

 data/z81/specific_class/capcube.txt |  2 +
 notes/z81/SPECIFIC_CLASS.md         | 78 +++++++++++++++++++++++++++++++++++--
 scripts/z81_spec_capcube.py         | 48 +++++++++++++++++++++++
 3 files changed, 124 insertions(+), 4 deletions(-)

Review:
## Verdict on Round 2 (§§6–8 of `notes/z81/SPECIFIC_CLASS.md`, commit 6df48876)

I found no fatal gap in the mathematics. C1, the 4/5 bound for the cap-one relaxation, holds up as a record for the relaxed family only. J, WP-for-J, the rare-window bound and the step from (M) to the .751 exponent also hold as stated. But there is one significant process problem, and (M) and several form issues need fixing.

### What I ran (no files written, memory-capped, under 5 min)
- **Script replay:** `scripts/z81_spec_capcube.py` matches `capcube.txt` byte for byte.
- **Independent C1 dictionary check:** 20,000 random squarefree pairwise-coprime triples (u,v,w), with f = jQ−1 (so σ≥2 cases occur) and n ≡ −4D (mod f) including composite n. Zero mismatches against the predicted root ∏{s | w, s∤n, s‖A}; 3,513 of the roots were composite. At ℓ = 1000003 the classes −4D were pairwise distinct.
- **Numerical constants:** μ = 0.4705286; the T3 exponent is −0.00178; the T1 rate hI(α/h) ≈ 5.0·10⁻⁷; the rare-window optimum is r−1 = 0.582306, also confirmed by brute force; b* = 0.52349; I* = 0.0041548.
- **Henriot:** I read `sources/henriot-erratum-2014.pdf`. New Thm 5 (upper bound with ρ̆) and New Thm 6 (lower bound for F ≫ η^{Ω}) exist as cited.

### C1 (unconditional 4/5 at cap one, composite root)
- **Valuation dictionary at composite n:** I re-derived it by hand.
  - At s | u or s | v the valuation of z is ≥ 0.
  - At s | w with s | n: s | V, so v_s(x) ≥ 2 and v_s(z) ≥ 0.
  - At s | w with s ∤ n and σ = 1: v_s(z) = −2. For σ ≥ 2 it is ≥ 0.
  - So the root is squarefree, odd, coprime to n, and rad r | y. This matches the cap definition in `EXSET_LINNIK_CAPS.md` §1.
- **Lattice (10):** correct at each pinned unit. Two caveats:
  - The phrase "the proportion of v,w coprime to their product" is garbled. It should say "coprime to ∏_{p≤P₀}p".
  - The losses O(1/P₀) and (log P₀)⁻⁵ do beat the (log P₀)⁻³ starting density.
- **Incidence/BV:** correct. The Cauchy step gives error ≪ H·t^{(C₁−B−1)/2}, uniformly in c₀.
- **Disjointness:** correct. D < H^{.014} < ℓ, D determines (u,v,w) through valuations 1, 2, 4, and k < Q forces k = k′.
- **Transfer:** correct. The repair is vacuous on failures, the degree is t⁴ and the boundary costs exp(O(t⁵)), which gives 4/5.
- **Squares:** correct. (−4D/f) = −(u/f) = −1, and no p | k divides D.
- **No false integral improvement:** the cap-zero subfamily needs w² | A, which costs 1/w² and kills the fourth logarithm. The note says this correctly.

### Real issues

1. **Duplicate result (process and priority).** The sister branch `side-agent/z81-cap-zero` (commit 518e2a6cc, 11 minutes later) proves the same bound as Theorem V of `notes/z81/CAP_ZERO.md`. It uses a different class family (−ar³/v, root exactly r) and adds a prime-root bound, N·exp(−cL^{3/4}(log L)^{1/4}). Both notes propose a STATUS §1B delta. The orchestrator must merge these into one row, credit both derivations (they corroborate each other), and keep the prime-root refinement.
   - `CAP_ZERO.md` (cited in §8 as "Prop. S") does not exist in this branch, so the reference dangles until merge.
   - `notes/z81/LIT.md`, cited in §3/§4, is also missing. That predates Round 2.

2. **Single overflow prime is not distinguished clearly enough.**
   - §8's O(√(L log L)) Trybushnyi-model cap covers only the m | r²n+4 packet. Read alone, it could suggest that one overflow prime yields only √(L log L). CAP_ZERO V shows L^{3/4}(log L)^{1/4} for prime root. §8 should cross-reference this explicitly.
   - Rephrase "One cannot substitute a single r" as "this proof with prime w gives only t³·log t". As written it reads like an impossibility claim.

3. **(M) is too broad and too precise as stated.**
   - **Refutation attempts:** I found none. Local factors are exact because B-primes exceed the shift diameter and f = 1 below exp(L^e), which also excludes Maier-matrix small-prime effects. Each window is already Shiu-bounded. I tried pinning to the common size of t using f supported near X with bounded cofactors. The events then have probability far below M(f) (≈ L^{−h}), so any size-mixing gain stays e^{O(k)}.
   - **Fragility:** (M) is unproved and beyond current methods once k grows. The whole saving rests on T1's rate of about 5·10⁻⁷ per window (at most about 5·10⁻⁶ for admissible α > 0.9967). Any loss of exp(10⁻⁶·kl) in (M) destroys the conclusion.
   - **Recommended restriction:**
     - Replace (M) by the finite character-kernel family actually used: f ∈ {w^{ω_B}, c·∏|.4+.6 Re χ_i(p)| with χ_i mod q_i and c ∈ {1, 2.12}}.
     - Better still, state only the single summed inequality E∏_i(T1+T2+T3)_i ≤ e^{ηkl}∏_i(Σ c·M), with an explicit η < hI(α/h). This avoids uniformity over all q^k term choices.
     - Keep the arbitrary-function version only as a named stronger variant.
   - **Scope:** say explicitly that (M)'s new content is J's coupling extended past Z = exp(L/(Bkl)) up to X. That extension is what raises the harmonic mass from (1−κ)l to about l.

4. **J and the rare-window bound are sound.**
   - **Coupling:** constants are explicit. With C = 200 and B = 10⁵, the errors are X^{−0.99} and e^{−600kl}, and no k-dependent constants are hidden.
   - **Fixed-k lower bound via Henriot:** valid. This covers the progression modulo 2^D·∏_{p≤k}p, bad-prime products of L^{o(1)}, and Chernoff and hit subtraction giving relative savings of L^{(α+ε)log3−β}.
   - **Prime upper bound:** the fixed-dimension upper sieve is valid, and the remainder X^{1/4} is absorbed per list.
   - **Form fixes:**
     - J's label omits Shiu and the fixed-dimension upper sieve.
     - "Uniformly in the offset choices." is a sentence fragment.
     - "κ ≤ β" should read "k ≤ number of band primes".

5. **Minor form issues.**
   - C1's label should say that the z79/TQ transfer is internal and unrefereed.
   - The script uses only tiny labels (including u = 1) and tests no disjointness or uniqueness. It is a valid identity check only, as the note says.

**Recommendation:** ACCEPT WITH FIXES. C1 can count as one cross-lab review toward a RECORD for the relaxed family only, merged with CAP_ZERO V into a single STATUS row. It is no ambient or integral ES improvement, and the ambient 3/4 stands. (M) should stay CONDITIONAL, with the restricted form above made primary.
</code-review>
