<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="7984da0831a59ac93e1ff937ecaad371e32451d2">
A separate reviewer subagent was asked to review the changes in `git log 7984da0831a59ac93e1ff937ecaad371e32451d2..`. Its request and review follow.

Request: review changes since 7984da0831a59ac93e1ff937ecaad371e32451d2 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Full hostile cross-lab Claude Opus Round-2 review of Wave z82 Lane 1A, notes/z82/CAP_CONST.md §§6–9, §0 and scripts/z82_cap_uniform.py. Check every proof step, quantifier, scope, label, source input and falsifier. Audit U (growing cap, collision deletion, Gallagher, repaired weighted centered moments); UB/UP (uniform matched exponents, shifted multiplier distortion, coefficient budget and scope); Q including quantitative endpoint and least-prime lifted carrier count, PM, J and its linked cubefree separation. Check numerical measures, replay correctness and hard controls, note any requested fixes with precise locations. Cap any computational replay at ≤15 minutes, ulimit -v 6000000, ≤2 compute processes; Python via uv run --offline --no-project python -B. Write no repository files. Return the full written verdict.

Commit log:
commit 7b25c9b53b8b2251f04a373c0e16d0654fe78a66
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 20:47:10 2026 +0100

    z82 cap R2: remove multiplier distortion and strengthen endpoint carrier supply

 notes/z82/CAP_CONST.md | 14 +++++++++-----
 1 file changed, 9 insertions(+), 5 deletions(-)

commit d882f670db467a880f60ebda92b361cfe3d00550
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 20:37:03 2026 +0100

    z82 cap R2: uniform composite and prime sieve curves, Chowla rate and linked 5/6

 data/z82/cap_const/uniform.txt |   8 +++
 notes/z82/CAP_CONST.md         | 119 +++++++++++++++++++++++++++++++++--
 scripts/z82_cap_uniform.py     | 138 +++++++++++++++++++++++++++++++++++++++++
 3 files changed, 260 insertions(+), 5 deletions(-)

Review:
# Cross-lab hostile review, Round 2: Wave z82 Lane 1A, `notes/z82/CAP_CONST.md` §§6–9, §0 and `scripts/z82_cap_uniform.py`

Range reviewed: commits `7984da08..7b25c9b` (d882f670 and 7b25c9b). Neither commit touches a master file, which complies with the lane rules.

## Verdict
**ACCEPT WITH MINOR FIXES** for U, UB, UP, Q (including the endpoint), PM and J.

- **No mathematical error found** that breaks a stated theorem. I re-derived every quantitative step listed below.
- **Fixes needed:** one scope sentence is now false after 7b25c9b (F1). The rest are form, labelling and replay hygiene. Without F1–F5 the export wording is not ready; the theorems themselves are.
- **No ES claim** is made or implied. All scopes are method-, relaxation- or hypothesis-bounded.

## Replay
- From the repository root, `ulimit -v 6000000; timeout 900 uv run --offline --no-project python -B scripts/z82_cap_uniform.py` finished in 0.3 s. Its output is **byte-identical** to `data/z82/cap_const/uniform.txt`.
- Run from `scripts/`, it **crashes** (FileNotFoundError). Line 37 opens `Path('data/z58/...')` relative to the working directory, so the script depends on where it is launched (fix S2).
- **Independent check (mine, /tmp only):** I wrote a separate script that does not use the lane's chart predicate. It built U-type labels D = a·∏s^{c_s}: a squarefree, even colours 2..2g for g = 2, 3, 4, all A < 400 including A with v_s(A) ≥ 2. It put no coprimality condition between n and a, so shared primes were tested. Result: **81,697 packets, 0 illegal** under the raw definition (den z a square, coprime to 2n, radical divides y, valuations ≤ 2E), plus the exact identity and x > 0 every time. This confirms "shared primes with a are harmless" and the colour legality at v_s(A) ≥ 2.
- I confirmed the example 4/92 = 1/195 + 1/1380 + 45/1196 exactly.

## Substance audit

**U (§6, l.133–162). Verified.**
- *Supply and level:* 4ma ≤ e^{10αt} ≤ T₀ = e^{12αt}, and T₀ ≥ e^{√(2t)} meets Gallagher's lower range. log x/log T₀ ≥ 1/(24α), so η ≤ 1/6 for small absolute α.
- *Exceptional modulus:* removing one odd p₀ ∤ Q correctly avoids it. Conductors 4 and 8 have no real zero near 1, as in CAP_INTERPOLATION Prop 1.2.
- *Collision deletion:* there are at most e^{11αt} labels and O(g) band primes per difference, so the relative loss is g·e^{36αt−t/2} → 0. Recovery of a, m and the colouring by unique factorisation, and of k from kℓ ≡ −1 (mod Q) with k < Q, is correct.
- *Weighted mean:* w_a/φ(Q) = 1/(2aφ(m)). The a-count main term carries φ(m)/m, which cancels. The error √U_a·τ(m′) is negligible against U_a/(k·log m).
- *Inner sum:* the Rankin/Lemma 1.1 bound gives [c·log M/(g log 2g)]^g. The ratio bound holds uniformly over subsets. The costs of removing primes ≤ g, primes outside G, p₀ and primes of k (≤ gD₀) are correctly accounted.
- *Centered moment:* (Y−μ_c)^{2j}/(c₁S)^{2j} is ≥ 1 on any repaired void and ≥ 0 everywhere. Integrating Bernstein gives [Cj/S]^j for j ≤ S/C.
- *No full-fibre lookup:* this is correct, because μ_c is itself a sum of per-atom terms mod kℓ. The coefficient budget is e^{C₁jt} ≤ N^{1/3}.
- *Exponent bookkeeping:* S/j ≫ (A₀ g log 2g)³ (cA₀)^g, because the t² in S exactly cancels L^{−3/(g+3)}. The saving is ≍ L·e^{−λ/(E+4)}/log(2g). The truncated case gives an extra 1/g.
- *Range λ < E ≤ λ²:* h log(g/2h) ≥ 4λ for u ≥ 8. log(S/Cj) ≥ λ − O(1). The saving is ≍ L·u/log g. The "h/g < .001" is a per-step loss. Its total log cost is h²/g, which is o(h·log(g/h)), so the bound is fine as used.

**UB (§7, l.164–188). Verified.**
- *Majorant comparison:* the unit-fibre cost is O(log t), which is ≪ Lρ. `thm:kcomp` applies with Jensen. min(2m, d·log(1+m/d)) is concave, so replacing m_c by its mean M_* is legitimate.
- *Atom weight:* 1/(ℓφ(k)) ≤ H₀(f)/f holds.
- *Shifted-weight estimate:* proof checked, including the reduced-or-absent class for 4uj ≡ 1 (mod e). The factor 1 + σ·log²t is ≪ e^{tσ} in both regimes.
- *(13):* the untruncated case checks. In the truncated case the digit set {1, 2, 4, …, 2g} has b = B−1 elements, minimal valuations ≥ 2 give O(p^{−2}), and ∏j = 2^g·g! ≥ b!.
- *Choice of σ:* Kρ (and Kρ/B truncated) works, using Br = λ − r. Bounded r works with σ = K′/log B, and the truncated case by the rad(D) Euler product. For λ < E ≤ λ² the split at w = B^{1/(1+σ)} gives O(w/log w + w/(σ log w)) < λ/2. If σ > 1, the trivial O(L) bound applies.
- *Matching:* the orders of U and UB match in all three regimes.
- *7b25c9b:* it legitimately removes the k/φ(k) ≤ C₀ hypothesis.

**UP (l.190–204). Verified.**
- F_E = 1*h_E with h_E(p) = B−1 and h_E(p^a) = 2 for a ≥ 2.
- The Brun–Titchmarsh dyadic bound m^{−σ}·log(2+1/σ)/φ(m) holds.
- The leading coefficient drops to B−1. The extra O(log λ) cost is O(B) precisely because E ≥ log λ, which is why that range is needed.
- Attainment: S′/j ≫ (A₀g log 2g)²(cA₀)^g. The collision fraction is o(1) because t/λ → ∞. Failures avoid only the G-supported classes used, which is correct.
- Ratio claim: e^{λ/((E+3)(E+4))} → ∞ iff E = o(√λ). Correct.

**Q and endpoint (§8, l.206–220). Verified.**
- *Moduli:* there are y^{1−1/C−o(1)} moduli d, and Chowla at 4d gives at most y^{2ε+o(1)} odd quotients b. Pigeonholing gives P ≥ Y^{1/2+4γ} iff C > 2.
- *Exponent:* (q−1)/2 | h with h odd, so t | s^h+1. log h ≪ (log U)^C.
- *New carrier supply via q_* = p·2^a:* classes with negative symbol and s ≡ 1 (mod 4) make up at least 1/4 of the units. Each has a prime ≤ C_ε·q_*^{1+ε} ≤ X.
- *Endpoint:*
  - b ≪ log^J(8d) holds because the least-prime bound is applied at the actual d. This is correct, even though y/d can be as large as 2^v.
  - P/√Y ≫ U^{10 log(K/60) − o(1)}.
  - The bad count is X·√(2Y)·U^{−3.9l}, which is X·exp(−Ω(U/log₂U)) and well below X/log^{J+1}X.
  - The floor in l costs only √(2Y).
  - The "X^{.998} would not suffice" remark is correct.

**PM (l.224–228). Verified.**
- The Rankin divisor count gives H₂(α) at v = log((1−α)/α). Sharpness via a primorial is correct.
- The P-moment with j = ⌊U/log Y⌋ and the union over e^W choices of h both check. The e^W loss is o(U/log₂U).
- K = (1+δ)/log 2 is consistent with z81's τ(h) ≥ U budget.

**J (§9, l.234–236). Verified.**
- The legal digits are 0..2a+d₀, which is F(p^a) of C with E = d₀. Jacobi is −1 whenever all label primes divide A, whatever the parity.
- The exponents 1..d₀+2 are distinct, and their sum b(b+1)/2 ≤ 1 + b(b−1).
- A tag of 3 at a simple prime gives valuation −1, so 5/6 at d₀ = 2. Literal cap one is contained in linked d₀ = 2; neither of linked d₀ = 2 and cap 2 contains the other.
- The colours 2..d₀+2 carry over to U.

**HC j = 1 slice (l.222).** The arithmetic is correct:
- p + k ≡ 1 (mod 4) forces j ≡ 3 (mod 4).
- j ≫ p^{.005} uses d > p^{.010}.
- k ≥ p^{.010}/2.

## Requested fixes
- **F1 (substance/scope, l.240).** "Q … applies Chowla *only to auxiliary moduli*" is false after 7b25c9b. §8 (l.214, l.216) applies Chowla, or the quantitative least-prime bound, at q_* = p·2^a, which contains the input's hard prime. Reword to: "applies least-prime bounds to auxiliary d and to moduli p·2^a at the fixed input; no distribution over inputs".
- **F2 (label/export, l.206 and STATUS delta l.5).** Say explicitly that z80's §12 Montgomery hypothesis implies both GRH and Chowla (take x = h^{1/θ}). So Q's U = log₂R branch **reproduces** the (log₃R)^{C} Montgomery-branch rate under weaker hypotheses (and the endpoint improves it slightly to (log₃R·log₄R)²). The genuinely new part is (log₂R)^C on Chowla alone. Without this note a STATUS reader could mistake the rate for a new one.
- **F3 (effectivity, §0 and l.133).** The old STATUS delta said "ineffective"; the new one is silent. U uses Gallagher, Vaughan and deletion of p₀, which looks effective, unlike H's BV. Either state the effectivity or write "effectivity not asserted".
- **F4 (label, §0 l.1 and l.133).** U also rests on internal unrefereed inputs. These are the CAP_INTERPOLATION (G)-consequence and Lemma 1.1 (as repaired in R237), and the z79 repair, which U's heading omits. Add them.
- **F5 (dangling pointer, l.238).** `notes/z82/CAP_TO_ES.md` and commit `16390995a` exist only on `side-agent/z82-cap-to`, not in this tree. The "PROVED (relation to Lane 1B)" algebra (D = a²r³w) cannot be replayed here. Keep the label at Assessment until that branch is merged.
- **F6 (form, l.9).** The Notation paragraph covers only §§1–3. §§6–9 reuse several symbols:
  - K: multiplier bound in U, Rankin constant in UB, constant in Q.
  - D: label, and carrier exponent in Q's X = exp(DU).
  - A: (f+1)/4, and exponent in Q's y = U^A.
  - J: prime-power product in U, least-prime exponent in the endpoint, theorem name, and H's truncation degree.
  - U: theorem name, log R in Q, and dyad length U_a.
  - h, l, M, M_*, C₀ (UB's height constant versus `cor:kmean`'s C₀): each also used in two senses.

  Add one line.
- **F7 (form, l.182).** "p^{−1−σj}" is really p^{−1−σ(j+1)}. The stated bound is a valid upper bound; say "bounded by".
- **F8 (clarity, l.158).** "The g from the centered moment recovers one full factor…" compares against H's binomial truncation. Against CAP_INTERPOLATION Thm 2.1 the extra factor of κ comes from **untruncation**: Montgomery's large sieve already gives k·log(S/k). Say so, so the source of the gain is not misattributed.
- **F9 (HC paragraph, l.222).** Inside HC's windows s ≤ p^{1.005}, so at fixed p finiteness is immediate. The τ-count and the s ≪ p^6 cutoff matter only for cubic packets outside the window. "Not just too sparse for the proposed asymptotic" has no clear referent. Clarify, or demote to a one-line remark.
- **F10 (export, l.7).** The Assessment/export paragraph is still R1-only. Add the R2 FRONTIER deltas:
  - UB/UP: merge into the growing-cap prime-sieve threshold entry together with L.
  - PM: merge with P.
  - J: the 5/6 versus 4/5 method separation.

## Replay and controls (S1–S4)
- **S1 (§9 CERTIFIED, l.242).** Report the actual screen counts: squares 0/65, F2 6/6, F3 3/8, F4 20/24 (14 (★) primes + 10 others). Also say that the synchronized packet (17, 37, 131, 1365) uses the b = 1 donors {131, 71}, not the most-frequent b = 3 pool. Its input, p = 17, is also a trivially soluble one.
- **S2 (script l.37).** Resolve the data path relative to `__file__`.
- **S3 (script l.112).** The comment says "first and fourth" moments; the code computes the 2nd and 4th. The moment check itself only verifies the identity E(X+Y)⁴ = EX⁴ + EY⁴ + 6EX²EY² for centered independent variables, so it tests nothing about the theorem. Describe it as an arithmetic identity check. The `mu ==` assertion, which catches target collisions, is the meaningful part.
- **S4 (hard control, optional).** J has no nonunit negative control, i.e. a linked tag-3 prime shared with n. Harmless, because the theorem makes the nonlinear tags G-supported, but worth a line.

## Open points (scope is honest, but the wording should keep them visible)
1. UB's sharpness is for **light single-band** majorants only. At growing E, multi-band or heavy designs could beat the (E+4) exponent. This is stated, but the §0 Result's "sharp" should read "sharp in the light single-band architecture" wherever it is exported. It already does in §0.
2. U's λ < E ≤ λ² regime gives a fixed power saving N^{−cη/(1+η)} at E = λ^{1+η}. This is consistent with L and with EXSET_LINNIK_CAPS, but it has not been compared against the EXSET_LINNIK_CAPS exponents. No record claim is made, which is correct.
3. The Triage line calls Q a RECORD. Given F2, the honest description is "conditional rate under a weaker hypothesis pair". That is fine for STATUS §1B as a qualifier, not as a new headline.

**STATUS delta.** Acceptable once F2 and F3 are applied. Cross-review requirement: this R2 review covers §§6–9. A second review is owed only if the note asserts a published-record comparison, which it does not.
</code-review>