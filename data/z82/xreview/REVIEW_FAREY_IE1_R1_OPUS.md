<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of Wave z82 Lane 2A (notes/z82/FAREY_IE1.md). Scrutinize every model-theoretic/algebraic/order/valuation/specialization/induction step with extreme rigor. Cap any replay at ≤15 min.

Commit log:
commit 011ce92f90a026a62edf250af5ff6ffba90a3a25
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 19:45:12 2026 +0100

    Locate the reduction boundary at scalar determinants and at the ES-failing prime

 notes/z82/FAREY_IE1.md | 187 +++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 187 insertions(+)

Review:
**Verdict: ACCEPT WITH FIXES.** I found no error that changes any theorem. The fixes needed are to form, labels and scope. The note claims no ES proof or disproof, and none is implied. ES in ℕ and IE₁⁻ versus ES remain open, as the note says.

Scope: one commit (`011ce92f9`), which adds only `notes/z82/FAREY_IE1.md`. No master files were touched, which is correct for a lane.

## Replays (well under the 15-minute cap)
- **§1 identity:** `(4ku−j)(4kv−j) − (j²+4kp) = −4k(j(u+v) − 4kuv + p)`. Checked in sympy.
- **§5 coordinate change:** checked symbolically for N = 9, 10, 13, 14:
  - `A = (H−σs)/q` is an integer of B.
  - `U = σsθ − Aδ` and `V = σsη`.
  - The change has determinant 1.
- **§2 local lemma:** I implemented the algorithm exactly as written: clip, divide by the gcd, reflect, scan the h-lines with a ceiling, pick the maximum, build the right neighbour. It agrees with brute-force level-Q Farey brackets on 3000 random cases (Q ≤ 30, K ≤ 5).

## Substance, step by step
1. **§2 (lemma, fixed-modulus equivalence, equivalence of the universal rungs): correct.**
   - The lemma's bounds check out: `h ≤ be ≤ K`, `b ≥ h/e` iff the value is ≤ t, and the neighbour satisfies `z+v > Q`, so `w/z ≤ 1`.
   - Th(n) ⇒ Farey uses K=2. Th(n) ⇐ Farey uses `rz+sv = n`, so `min(r,s) ≤ n/(Q+1)`.
   - Special forms ⇒ Farey: `S ≥ Q/8`, and `|yt−x| < 4/S ≤ 32/Q`.
   - Farey ⇒ reduction: the vector found has `A ≤ 5√d`, and the search box is `|j| ≤ 10`, `|i| ≤ 6`. All verified.
2. **§3.1 (lifting r to a scalar root mod m): correct, including the dyadic case.**
   - The valuation argument works in both cases. If `e ≤ v(D)`, then `⌈e/2⌉ ≥ e − v(k)`. If `e > v(D)`, both roots have value `v(s)`, and the two factors `r±b` cannot both exceed `w(2r) = v(k)`.
   - The sign partition is coded in PA, and the leftover modulus divides 2s, which lies in C.
   - Fix: §3.1 applies the z81 §12 transfer with a nonstandard scalar coefficient D. z81 §12 is stated for *integer* polynomial systems. The extension is valid because the embeddings are over K, but it should be stated explicitly as an extension.
3. **§3.2 (lattice/Hermite step): correct.** I checked the split of each horizontal prime, the orientation, `γ ∈ B⁺`, `det J = γa₀`, `v|w`, `v|b`, `m | r²+D`, and that the final matrix is bounded inside T*.
   - Weak spot (form, not a gap): the factoriality of the algebras after adjoining t is badly written. The sphere sentence (Gaussian field, Laurent chart, Hilbert 90, faithfully flat descent) is garbled.
   - A clean argument exists, and the note should use it:
     - The generic sphere is a smooth affine quadric of rank 4. Its class group is Pic of the projective quadric threefold (ℤH) modulo the irreducible hyperplane section at infinity, so it is 0.
     - Each old prime stays prime, because its fibre is a geometrically integral rank-4 quadric in characteristic 0. Nagata then gives factoriality.
     - Rows: the two pivots stay gcd-coprime by going-down, and Nagata applies at the pivot primes.
   - The units statement (`A_t^× = K(t)^×`, or `K^×` in §4.2) should be stated and proved via units of the generic fibre plus constant contraction. Calling these "scalar units" is misleading.
4. **§3.3 (necessity via Duke): correct.**
   - Duke supplies the forms for d ≡ 3 mod 4 via −d and doubling. The constants can be written as polynomial inequalities, so the statement transfers to B ≡ ℤ. The estimate `|U−ζV| ≤ 2K₁/√s` and the late-line heights are fine.
   - Fixes:
     - Duke 1988 Thm 1 is the Heegner-point theorem; the "(i)" sub-item label needs checking.
     - The constants κ, L are ineffective (Siegel). That is harmless for truth in ℕ but should be said.
5. **§4.1 (fibres mod maximal ideals of B′): correct.**
   - The row fibre needs one of the two reduced pivots to be nonzero mod M. This is properly argued from coprime contents plus primitivity; it is not assumed via faithful flatness, which would be false, since gcd-coprime pivots need not generate the unit ideal.
   - The content bound follows: P has odd order in `k₀(P)`, and `k₀(P)` is relatively algebraically closed in the fibre field.
   - Sanity check: for scalar k, this gives `c(P+k) ∈ C`, which is consistent with the z81 valuations.
6. **§4.2 (determinants −4kP): correct.**
   - At P: the ramified prime t, `v_P(a) ≤ 1`, and `v_t(u+t) = 1`.
   - At the other horizontal primes, the split happens over the generic point of π.
   - Range 1: `m ≤ ke` puts the Farey level in C. Range 2: `m/g′ | se`, verified for each prime.
   - The failure at `k = P` and the sharp slice `s ≤ c√P` both check out. In particular `|U−ζV| ≤ 4/√(s/√P)`.
7. **§5 (coupled edge): correct.**
   - Shortness holds with `N > 4d₀+4`. The hull check works through U, V with independent residues, the descent works through the negative Z-degree valuation, and the Łoś transfer handles first-order items only.
   - §5.1: the necessary-and-sufficient test and the √2−1 example check out; all three weighted coefficients are ≈2.83 or less.
8. **§6 (PA-host restriction): correct.** It uses the bracket uniqueness argument and the radix argument.

## Form fixes required
- **Label line:**
  - Add Łoś for the §5 ultraproduct.
  - Add the CONDITIONAL (host ES at P) part of §6.
  - Add z81 §§10–11: T* = T₊^{ξ,Q}, and the §4.1 induction covers the §11 square-tested lines.
- **Scope line:** it says "three universal rungs", but §2 lists four.
- **STATUS delta:**
  - Add the qualifier D ∈ T*.
  - "All scalar k ≤ P" understates range 1, which is k ≤ cP for some c ∈ C.
- **Missing proposals:**
  - A FRONTIER §6 METHOD-CX line. Within this model, reduction at every ordinary level −4kP coexists with ¬ES(P), so it cannot by itself yield ES(P) over IOpen + Bézout + PW + ….
  - A FRONTIER §6 BARRIER-SCOPED line for the §6 PA-host restriction.
  - A WAVES line.
- **Notation collisions:**
  - s: square-part root in §3, `2^{L/N}` in §5.
  - A: upper algebra, and `(H−σs)/q` in §5.
  - Z: auxiliary variable in z81, and the new edge in §5.
  - M: modulus in §3.1, and maximal ideal in §4.1.
  - t: target, and √−D.
  - θ: in §2 and in §5.
  - B: PA scalars, and the middle coefficient.
  - d: squarefree part, and 4ac−b².
  - e: error, exponent, and member of C.
- **§1:** the "PROVED" j-generalisation is trivial, and the step "if j | 4kuv then j | p" has an unmotivated hypothesis. Either shorten it or explain what it is for.

## Debate and challenge
- **What the results do and don't show:**
  - The real result is a same-model barrier. Reduction at every scalar or squarefree determinant, and at every ordinary level −4kP, survives in a model with ¬ES(P).
  - That model still fails Th(P). By §2, Th(P) is exactly a full level-√P Farey. So the note does **not** separate "reduction plus Th(P)" from ES, and its final Assessment says so correctly.
  - RECORD triage is defensible only as a replacement phrase in the existing T* row, which is already at its 6-line cap.
- **Duke dependence:** I tried to avoid Duke by using `(sU−bV)² + dV²`. That only gives the negative direction when s/√d is above C, so Duke really is needed for the full iff. Suggest stating the Duke-free partial result explicitly.
- **§5 does not touch the open problem:** it repairs every fixed-degree function of θ, but not shortness for residues introduced *after* the repair. The note's Assessment identifies this correctly as the unbuilt edge.

Cross-review owed: this is one cross-lab Opus review. Promotion of the STATUS phrase should wait until the fixes above are applied.
</code-review>