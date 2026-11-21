<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="bda831d3c">
A separate reviewer subagent was asked to review the changes in `git log bda831d3c..`. Its request and review follow.

Request: review changes since bda831d3c carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review, round 3, §11 of notes/z80/IE1_SPLIT.md (and tiny §10 edit). Independently check primary hit, quantifier complexity and use of L(Div) vs BCM, exact p-pure multiplicative group with standard quotient residues, height exact sequence, partial barrier only, other falsifiers. Also look for any missed correctness risk in the earlier §§1–10 that would require a caveat before reporting the cofinal-PA window + Sep + Lag model. Provide commit hash and export verdict, fixes. Do not edit files, no computation necessary.

Commit log:
commit 590d1284b5bfe26e17e6efa656052c2b9f55df00
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 18:16:09 2026 +0100

    Derive private pure-divisor height groups from BCM plus divisibility minimization

 notes/z80/IE1_SPLIT.md | 20 ++++++++++++++++++--
 1 file changed, 18 insertions(+), 2 deletions(-)

Review:
**Review of `590d1284b5bfe26e17e6efa656052c2b9f55df00`** (`bda831d3c..590d1284b`; only `notes/z80/IE1_SPLIT.md` changes: the Review line, one §10 sentence and the new §11)

**Verdict: ACCEPT WITH MINOR FIXES. Export is fine** at the labels the note uses: PROVED for §11, scoped as a necessary test for a BCM + `L(Div)` architecture, not a countermodel. I re-derived every step of §11 and found no substantive gap. This counts as one cross-lab hostile review of §11. I edited no files and ran no computation.

## §11, checked step by step

**Primary hit.**
- The least `t` with `t|H ∧ pt∤H` needs a nonempty set. It is nonempty because `H` itself is a hit: `pH|H` would make `p` a unit. The note does not say this; it should.
- Purity: if `g>1` divides `t` and `p∤g`, then `gcd(g,p)=1`. From `H=tb` with `p∤b`, `p(t/g)|H` would force `p|gb`, which is impossible. So `t/g` is a smaller hit.
- `t>x`, because `pt≤px` lies inside the BCM interval.
- The second minimization gives the least `u>x` with `u|t`. It is pure and greater than 1, so `p|u`, and `u/p≤x` by minimality.
- Comparability: after removing `gcd(a,b)`, the two coprime cofactors are pure, so they cannot both exceed 1. This makes `u` the first pure element above `x` in the whole ring.
- None of this needs `p` to be standard.

**Quantifier complexity and the role of `L(Div)` versus BCM.**
- All three minimizations are instances of z75 `IE1_ES.md` §1's `L(D)`:
  - `t|H ∧ ¬(pt|H)`;
  - `u>x ∧ u|t`;
  - `d|u ∧ d^m≥u` for standard `m`.
- Parameters are allowed there, and the note correctly never minimizes the bounded-universal predicate "pure".
- BCM is used only to supply `H`. Bézout is needed for comparability and cancellation. IOpen is needed only for the integer parts in the exact sequence.
- Because `L(D)` has parameters, §11 is a test for the `L(Div)` target, not for `IE₁⁻`. That is correctly scoped.

**The group `G_p` and its standard residues.**
- Products of pure elements are pure: a divisor of `ab` prime to `p` is coprime to `a`, hence divides `b`, hence is 1.
- Every member of `G_p` is a pure element or its reciprocal, and `p` is the least member above 1.
- The `m`-th root step checks out:
  - take the least `d|u` with `d^m≥u`;
  - put `v=d/p`, so `v^m<u≤p^m v^m`;
  - comparability gives `v^m|u|p^m v^m`;
  - finite cancellation then gives `u=p^j v^m` with `1≤j≤m`.
- Uniqueness follows from the ordering and the absence of members strictly between 1 and `p`.
- The residues are additive, and compatible for `m|m′` (rewrite `p^{r′}v′^{m′}`). So the map `G_p→Ẑ` is a well-defined homomorphism.
- Sanity model: in PA, `G_p≅(M,+)` and the residues are the standard residues of nonstandard exponents. This is consistent, and the map is not injective, as the note says.

**Height exact sequence (standard `p`).**
- The kernel is `p^ℤ`: a pure element of standard size is a standard integer, and divisibility among standard integers agrees with ℤ.
- Surjectivity comes from the integer part plus (PWdiv), since the size ratio is at most `2p`, which is standard. Infinitesimals are handled by inversion.
- The joint direct-product embedding holds: pure elements at distinct primes are coprime, so cancellation works.
- The note's disclaimer that surjectivity is not claimed for nonstandard `p` is the right one.
- PA check: the sequence is `0→ℤ→M→M/ℤ→0`, and `M/ℤ` is divisible. Consistent.

**"Partial barrier only."** The scoping is correct.
- In §§2–6 and §9, (PWdiv) does hold at old primes `p∈B`: the pure elements are `p^k` with `k∈B`. For `x>D`, §6's density lemma gives `m∈B` with `x<m<2x`; then either `p^k≤m` or `p^{k+1}` lies in `(x,px]`.
- At `P`, the pure elements are exactly the standard powers `P^j`, by the factor calculus. So (PWdiv) fails there.
- This is consistent with those models lacking BCM and `L(Div)`.
- Nothing in §11 conflicts with z77, z78 or z79.

**Other falsifiers.** Pure powers and `Ẑ`-residues give no ES extraction at squares, at the `(★)` zeros, or at numerator 8. The note says this.

## Debate points
1. **Purity is not upward-persistent.** It is a bounded-universal property, not an E₁ window, so later edges can destroy it by splitting. That is the real content of "private". The §11 Assessment should say so, because it is what makes (PWdiv) harder than the cofinal-PA windows.
2. **Novelty is modest.** This is the BCM + `L(Div)` analogue of "a power of `p` in every `(x,px]`", which is immediate in PA. The new part is deriving it from these weak axioms plus the `Ẑ` and size-group structure. No priority should be claimed.
3. **The two halves are complementary.** The exact sequence with divisible `Γ` only gives that `ℤ/m→G_p/mG_p` is onto. The unique-remainder theorem adds injectivity, and it also covers nonstandard `p`.

## Required fixes
1. **§0 Result/Scope/Triage:** mention §11, e.g. "§11: in every IOpen + Bézout + BCM + `L(Div)` ring, (PWdiv) and private groups `G_p`, with `Ẑ` residues and size exact sequence; a necessary test, no joint countermodel." Triage: necessary screen, merged with the existing z78/z79 axis-divisor line on the BCM + `L(Div)` target (FRONTIER §4 checklist line). STATUS delta: none, or at most a parenthetical on STATUS §2 item 4.
2. **§0 Label:** add z79 `IE1_BASE.md` §5 and the definition source z75 `IE1_ES.md` §1. Spell out what `L(Div)` means: parameterized, Boolean polynomial divisibility and comparison.
3. **§11 primary hit:** state that `H` is a hit, so the set being minimized is nonempty.
4. **Cosmetic:**
   - Write the sequence in one notation, e.g. `1→p^ℤ→G_p→Γ→1`.
   - In the falsifier paragraph, cite §6's density lemma for the windows at old primes.
   - Move "Thus a tower needs…" out of the PROVED paragraph into the Assessment.

## §10 edit and the earlier sections
- **§10:** the change to "divide a unit of `A`" fixes the dangling antecedent and is correct. A unit divided by its content, and its inverse, both lie in the pullback, so the unit is `±` its content.
- **No new correctness risk in §§1–10.** I re-checked:
  - that BCM still fails in §9 (the `X+j` are distinct horizontal primes even if their contents are nontrivial);
  - that `L(Div)` still fails (units are `K*` after spheres);
  - that Lag is compatible with `−1` being a nonsquare mod `P` (the residue cone is not formally real, and `K` stays relatively algebraically closed);
  - (Sep) and isolation via the factor calculus with spheres.

**Caveats for reporting the cofinal-PA window + (Sep) + Lag model:**
1. The Pell windows are only for nonsquares `d∈B`. Supplied PW fails at `d=P²−1`, so do not write "Pell windows" unqualified.
2. It does not include all the z78 pointed-variety windows.
3. The conditional absence of a least failure needs `B≡ℤ` and ES in ℕ. The unconditional least-`U₁` control is just ¬PW repackaged.
4. Lag + Dirichlet + Bézout + (Sep) with ¬ES already exists in the z76 PID. Only the combination with the cut and the windows is new.
5. The model has no BCM, no `L(Div)` and no `IE₁⁻`, and `IE₁⁻` versus ES stays open.
</code-review>
