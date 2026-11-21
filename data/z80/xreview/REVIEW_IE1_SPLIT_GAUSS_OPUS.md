<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="5c7cfdc09">
A separate reviewer subagent was asked to review the changes in `git log 5c7cfdc09..`. Its request and review follow.

Request: review changes since 5c7cfdc09 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of notes/z80/IE1_SPLIT.md §15 on commit 94780bd5a. Validate all determinant-one proper Gauss reduction and odd-prime root-conditional TS in the EXACT previous §9 true-arithmetic model. Check sign matching at arbitrary nonstandard PA moduli via local transfer and scalar gcd, including 2; Gaussian UFD persistence at each edge, splitting and normalization, and final determinant +1. Check scope labels, no claimed IE1^- or standard ES result. Give hash/verdict and fixes, no edits or computations necessary.

Commit log:
commit 94780bd5ae3ec3665eb955d6ffaa4b59010276d8
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 19:51:39 2026 +0100

    Prove discriminant-minus-four proper reduction throughout the cofinal PA window model

 notes/z80/IE1_SPLIT.md | 20 ++++++++++++++++++--
 1 file changed, 18 insertions(+), 2 deletions(-)

Review:
**Verdict on 94780bd5a (`notes/z80/IE1_SPLIT.md` §15): ACCEPT WITH MINOR FIXES.** I found no gap in the mathematics. The fixes are about form, internal consistency and scope wording. As you asked, I made no edits and ran no computations.

## What I checked (substance)

**Vertical orientation lemma** (for `h∈B⁺` with `h | u²+1` in `R`):
- **Getting an old root.** §12.1 can be used with `L=u`, `f=T²+1`, `d=h`, because `u∈R` is integral-valued and `w_ℓ(u²+1) ≥ v_ℓ h`. §12.1 needs `B≡ℤ`, and the theorem assumes it. The note is right that invariant 2 alone would not do, since `h` can lie above the reserve.
- **Sign matching at odd `ℓ`, arbitrary nonstandard `ℓ` and exponent `e`.** We have `w(u−b)+w(u+b) ≥ e`, and `w(2b)=0` because `b²≡−1`. So both cannot be positive: one is 0 and the other is ≥ e. This holds in a valuation of any rank. The value `v_ℓ c(u−b)` lies in `B`, so `h₊=gcd_B(h,c(u−b))` takes all or none of each odd prime power, computed internally.
- **At 2.** Since `2∈D⊂C`, invariant 2 gives `R/2R=B/2B`. So `u` and `b` are both odd, `w₂(u−b) ≥ 1 = v₂h`, and the whole 2-part lands in `h₊`. Hence `(h₊, h/h₊)=1`.
- **After the CRT correction.** For the corrected `b'`, `w_ℓ(u−b') ≥ v_ℓ h` at every `ℓ`. The pullback definition of `R_A` then puts `(u−b')/h` in `R`. The note's warning that an old root without the sign correction would not suffice is correct and essential.
- **Gaussian gcd.** `α=gcd(h,b'+i)` has norm exactly `h` (PA Gaussian arithmetic):
  - only one split factor of each odd `ℓ|h` can divide `b'+i`, because its imaginary part is 1;
  - `b'²+1 ≡ 0 (h)`;
  - for odd `b'`, `(1+i)` divides `b'+i` exactly once.
- **Conclusion.** `u+i = (b'+i) + h·(u−b')/h`, so `α | u+i`. ✔

**Gaussian UFD persistence at each edge:**
- Free lines: immediate.
- Rows: a common height-one prime of `A[i]` would contract to a height-one prime of `A` (integrality plus flat going-down) containing the coprime pair `a,b`, which is impossible. Nagata is then applied as in §4.
- Spheres: `s−z²−w²` is irreducible for `s≠0`, and `U` is prime. The Laurent chart has units `K(i)*U^n`, so `A'` has units `K(i)*`. Old primes persist because the rank-4 fibre is geometrically integral, including the cone case.
- The directed union is a UFD. ✔

**Splitting of a horizontal prime and normalization:**
- `A[i]/pA[i] ≅ F×F` through the root `ū`, and the two factors are comaximal since `2ū` is a unit. So `p` splits as two non-associate conjugate primes.
- From the unit description, `Nz=λp` with `λ∈K⁺`. After fractional-content normalization, `λ∈B⁺` because `p` is primitive.
- At `ℓ|λ`, both `f` and `g` are units, so `g` is comaximal with `λ` by Bézout.
- `w=fv` gives `λ | w²+1`, and `f+ig ≡ g(w+i) (λ)`. Therefore `z/α∈R[i]` with norm `p`.
- The converse direction (a two-square representation gives a root) and the scalar-prime case are fine. ✔

**Proper equivalence and the determinant sign:**
- `a₀=c(a)` divides `a` in `R`, and the vertical lemma removes it.
- `u+i` and `u−i` are coprime because `2i` is a unit. So exactly one of `z_p`, `conj(z_p)` divides `u+i`, with multiplicity at least `e`.
- The quotient has integral-valued coordinates, since `conj(ζ)/p` does, and `A[i]=A⊕iA` because `E` is formally real. So it lies in `R[i]`.
- Columns `ζ=conj(h)` and `κ=k` give `conj(ζ)κ=hk=u+i`, so the dot product is `u` and the determinant is `Im(hk)=+1`. I verified the sign. It would not matter anyway, because `[1,0,1]` has an improper automorph.
- No bounded enumeration or coded reduction is used. ✔

**Scope labels:** There is no claim of IE₁⁻ or of standard ES. "Cross-review owed" is recorded, and the §0 Scope line is updated correctly. No master file cites `IE1_SPLIT` yet, so no export is pending.

## Fixes

1. **§0 Label.** Add the §15 dependencies to the dependency list: §12.1 (hence `B≡ℤ`, Łoś), Nagata's criterion, and finite flat going-down for the Gaussian ascent. At present only "§§12–13 also use…" is listed.
2. **§0 Triage and STATUS delta are missing for §15.** I suggest triage as a scoped screen-table update with no STATUS row, or at most a clause in the §1E row delta. The reason is that the antecedent is empty at every bad prime, so the result does not touch ES failure.
3. **The note now contradicts itself; rewrite in place.**
   - §10 table, z79 §§4,8 row: "No assertion of conditional two squares at other primes" is now false. Point it to §15.
   - §10 table, z79 §§9,12–13 row: "Global binary-form reduction not proved" should read "…except discriminant −4 (§15)".
   - §13 Ladder and the §14 falsifier table: add the same pointer.
4. **Theorem wording.** Replace "does not prove TS" with "TS fails at `P` (§10); only the root-conditional form holds". Unconditional TS is actually refuted in this model, which is stronger than "not proved".
5. **Assessment.** It names only `P` and `π`. Either state that `−1` is also a nonsquare at the §9.3 primes `p'` and the §12 primes `q` (by the same linear-seed fibre argument), or say explicitly that nothing is claimed there.
6. **"Hence also with the flag of §13".** Justify that `B₁≡ℤ`: `B₀≺B₁` and `B₀` is true arithmetic. §12.1 needs this.
7. **Small proof-text gaps:**
   - Show `f,g ≠ 0` *before* the inverse step: `f²=λp` is impossible because the `p`-order of `f²` is even. Currently this appears only after the step that uses `g≠0`.
   - Spell out the row-unit claim `A[i][1/a] ∩ A[i][1/b] = A[i]`.
   - Replace "at its generic point … étale" with the global decomposition `F×F`.
   - Clarify "both roots agree mod 2" as "`u` and `b` are odd by invariant 2 at `d=2`".

**Assessment of significance (debate point).** This is a genuine positive fragment: two IE₁⁻ consequences from z79 — the root-conditional two-square case (`m=1`) of §4 and discriminant −4 reduction from §9 — hold together with ¬ES. But it is weak as a screen, because the root hypothesis fails at every manufactured bad prime. It shows that this consequence alone cannot force ES; it is not evidence about how ES relates to induction. It should be classed that way and not promoted.
</code-review>
