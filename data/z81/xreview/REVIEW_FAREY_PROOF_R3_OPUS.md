<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="d44491830">
A separate reviewer subagent was asked to review the changes in `git log d44491830..`. Its request and review follow.

Request: review changes since d44491830 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Final targeted hostile Claude Opus check on be1159b26 after R2: audit new §12 (local valued embedding for determinant −4/conditional TS and exact z79 §3 cut height windows), R2 fixes, optional quadratic horizontal prime in §9 and variants table. Pay particular attention to hidden cofinal PA or earlier shrinking reserve assumptions, and no pooling. No compute needed; if using any replay cap to ≤15 minutes. Please focus on genuine gaps rather than proposing a new theorem.

Commit log:
commit be1159b260e0bf723a188b7c2e1846e999681ccb
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 15:24:46 2026 +0100

    Separate all model variants and verify retained determinant-one reduction and height windows

 data/z81/xreview/REVIEW_FAREY_PROOF_R2_OPUS.md | 127 +++++++++++++++++++++++++
 notes/z81/FAREY_PROOF.md                       |  78 +++++++++------
 2 files changed, 178 insertions(+), 27 deletions(-)

Review:
**Verdict: ACCEPT, with form fixes.** I found no mathematical gap in §12, in the R2 fixes or in the new §9 material. I found no hidden cofinal-PA assumption, no shrinking reserve and no pooling of models in the arguments. The problems are in the §0 block, the variants table and notation. I ran no computation; I checked the identities below by hand.

## Substance checked (hostile pass)

**§12, local embedding.** The setup is sound. Because `B≡ℤ`, `(B,l)` embeds elementarily into `ℤ^U` with a named prime, so `tp(l)` is realized by standard primes. Each pair `(ℤ,ℚ_λ)` is henselian, and "integral elements have integer representatives mod any `m`" is a first-order statement, so it transfers. By invariant 1, every value is the value of a scalar, so valued diagrams reduce to statements of the form `v(x/γ)=0`.
- **`l∈C`, lines:** a late centre `Y↦s_m` is a ring map, and constant-term dominance gives `v(f(s_m))=w_l(f)`. This also holds for polynomials frozen before `l` entered, because avoidance at entry and the next multiplier give dominance.
- **`l∈C`, spheres:** the old henselization embeds into the henselian field sort. The value of `f` at a late centre is stable because later rotations move coordinates by more than any frozen value (§7, step 4).
- **`l∉C`:** such a prime is odd, nonstandard, never enters and keeps the Gauss/monic baseline.
  - The residue field of the field sort is pseudofinite and infinite, so avoiding finitely many proper closed subsets works.
  - `w_l(s)≤1`, so at worst the reduction is the rank-four cone; a smooth non-vertex point plus simple-root Hensel lifts it.
  - A row chart has a unit pivot, because the PA gcd was already removed.
- **Square-tested lines** (the seed and the §11 `q`-lines) are handled by restriction from the auxiliary `Z`.
- **Congruence premise.** One compactness argument is made per prime. The conclusion `∀l|h ∃r` is then true in `B` for every actual element, so internal PA CRT is legitimate. No coded family of embeddings is used. The scope disclaimer ("not every ambient residue class lifts") is correct.

**§12, reduction.**
- The orientation step is sound: `v₂(u²+1)≤1` by invariant 2 at 4.
- The Gaussian algebra over `K(i)` is unchanged by the z81 edges, since the seed and the §11 lines are polynomial.
- `λ∈B⁺` because `q` is primitive.
- The determinant and Gram identities hold: `det = Im(zw) = 1`, dot product `Re(zw) = u`, squared lengths `a` and `c`.
- The restriction to the cut is sound because `|z_i|²≤a`. A cut prime stays prime in the uncut ring because any factorization would be cut-bounded.
- I tested for a clash with (B). A prime `p=x²+y²` with a root of −1 could only contradict (B) if it already had `x,y≪_C H` with `x−θy≈0`, which is circular. Example: `P²+H²` is a primitive horizontal prime that is a sum of two squares, but its pair `(P,H)` is not `≪_C H`. So there is no clash.

**§12, z79 §3 windows.** Heights in `C` lie in `B`. Heights above `C` get `B` approximants at any standard relative precision (§4). The witnesses are polynomially bounded and the matrices are open, so the windows restrict to `T*`. The note says plainly that `B` is not cofinal in the cut.

**§9 additions.**
- The `P²+4` identity holds, and `5|P²+4` because `P≡1 (5)`.
- `π=1+(LP)²`:
  - it is irreducible because −1 is not a square in `K`;
  - it is primitive: it is ≡1 at initial primes, has unit leading coefficient `L⁶` elsewhere, and avoidance covers newly entered primes;
  - `(LP)²−π=−1`, and `π≡1 (4)`.
- Squareclasses at `P`: `T/PT→R/PR` is injective, and `R/PR` embeds in the `P`-fibre field. `K` is relatively algebraically closed in that fibre field: the lines and rows give rational extensions and the rank-four spheres are geometrically integral. So −1 and 2 are nonsquares mod `P`, and TS fails at `P` (`P` is not a sum of two squares).

**§1 additions.** `aa'=4kp+1` gives `4kuv−u−v=p`. The four representations are correct: `11=9+2`, `17=9+8`, `131=81+50`, `241=169+72`.

**§7 numbered algorithm.** The entry bound and look-ahead are correct: every new prime `l` with `l∤D` exceeds `N_prev` because `N_prev!` divides `D`. Frozen values satisfy `<M·v_lD<v_lD'`.

## Required fixes (form and scope)

1. **Review line (§0).** §12, the squareclass lemma, the `π` example and the compatibility paragraph were all added after R2. The line currently implies they are covered by R2's "fixes applied". Add "§12 and new §9 material: R3 (this review)". Cross-lab review by Astra is still owed if this note is to reach STATUS.
2. **Label (§0).** §12 depends on z80 §§12.1 and 15, z79 §3 items 2–3, ultraproducts/Łoś and PA Gaussian arithmetic. None of these is in the composite label.
3. **Result, Scope and STATUS delta.** These list only failures, plus "variable Gauss reduction fails". STATUS's z80 Model 2 row explicitly lists "proper reduction at discriminant −4" and the balanced-norm and elliptic windows. A reader of the delta would wrongly infer that `T*` lost these. Fixes:
   - add "retains disc −4 proper reduction, the root ⇔ two-squares criterion and the z79 §3 norm/elliptic windows (§12)";
   - update the delta's pointer from §§2–11 to §§2–12;
   - flag to the orchestrator that this STATUS item is already about 5 lines, so the addition needs compression to stay within the 6-line cap.
4. **Variants table.** Add a row for §12: disc −4 reduction, root ⇔ two squares, and the z79 windows. `T*`: HOLDS. `T₀`/`T₊`: either "same proof (needs only `B≡ℤ`)" or UNKNOWN, but state one explicitly.
5. **`π` example in §9.** Say which models carry the first-digit option and that it is compatible with `T*`. Rename `D₁'`: it collides with the PA cut `D₁` and with §7's `D'`.
6. **Unclear sentence in §12, bullet 1.** "Arbitrarily large initial moduli in the real order are irrelevant…" should be explained or deleted.
7. **Notation collisions remain.**
   - `M`: the §3 multiplier, the §4 common denominator, and the §7 loss bound.
   - `q`: the §9 odd horizontal prime, the §11 new failing prime, and the §12 horizontal prime.
   - `z`: the §7 digits and the §12 Gaussian factor.
   - `h`: §2, §10 and §12.
8. **Wording in §12.** "Any finite field stage of the uncut tower in §11" should read "of the uncut tower of `T*`".

None of this affects ES, which remains OPEN. The note claims nothing about ES beyond the scoped model results.
</code-review>
