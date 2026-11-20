# Hostile review (Opus) of d6075a8b1, `notes/z76/QR_TS_BCM.md`

**Bottom line:** I found no fatal error in either headline. My verdict on both is **ACCEPT-WITH-FIXES**. Nearly all the fixes are exposition or bookkeeping. One is a real hole in a proof step (F1, uniformity of the joint open over the rotation parameter), but it can be closed with a single argument. The note is very dense, so my check was step by step on the logic, not a formal line-by-line proof. Some risk remains.

## Target 1: one PID with Dirichlet, Lagrange, full prime QR, universal TS and L(D), and ¬ES(P)

### §1: Hochschild–Serre, Pic and torsion
- **Transgression.** I recomputed the lift cocycle (T↦T, T↦√s/T) in all four cases. The factor is χ_s(g)χ₋₁(h), so the transgression is {−1,s}. This matches the conic kernel ⟨(−1,s)⟩. The only differential leaving (1,1) is a ↦ {a,−1,s}, so the quoted kernel is right.
- **Pic.** Descent with cocycle cU^n gives N(c)sⁿ=1 and shifts n by even integers. So Pic is 0 in the non-norm case and ℤ/2 in the norm case.
- **J = ⟨−1⟩.** For the point divisor, σ(U−1)/(U−1) = −U⁻¹, which has odd exponent on the nontrivial coset. So its Kummer coordinate is the quadratic character of K/F, i.e. −1. Sanity check: over ℝ with s=1, Br(X) = Br(ℝ), as the formula predicts.
- **Cor(z,U) example.** The parameter is N z, which is automatically in the kernel. The residue at infinity is [N z], since the two ends are identified through id and σ. The inert-component residue (−1)^m ż₀ also checks out.

### §2: the subspace W
- β_K = γ + (a,U) holds exactly, because Pic(G_m)=0.
- Under "residues are old", the Gaussian fibre residue c·U^{v_q(a)} forces v_q(a) even, also at s via the V=0 component, where U=2x and the identification is an isomorphism. So a ∈ ℚ*·F*².
- **Case a = ±1.** The class is unramified at P∞, so it lies in Br(C̄), so it equals δ|_X. If δ has order 4, its residue θ has order 4 with 2θ cutting out k(i)/k. That excludes it from W, and the argument is correct.
- The map W/old ↪ ⊕_ℓ 𝔽₂ is therefore right. The key point, which the note should state outright: the ordinary primes ℓ are units in the stage ring A, so vertical residues cannot see them. That is exactly why controls at the marks are needed.

### §2: control lemma
- The jump formula β(bt) − β(b) = (a, δ(t)) holds, with δ(z/ż) = [N z].
- The tests are right: at odd ℓ, a unit z with nonsquare unit norm tests v_ℓ(a); at 2, z = 1+2i with (a,5)₂ = v₂(a).
- The rotation t = (−3+4i)/5 is a 2-adic integral unit, so it preserves integral points. It is also unaffected by the −1/J ambiguity, since (−1, N z)_ℓ = 0.
- The two-step dualization is sound: first fix the bits on W by choosing candidates, possibly at infinitely many ℓ; then adjust the vertical characters modulo old squareclasses; then do the horizontal extension.

### §3: Gaussian skips, parsimony, interfaces
- **Gaussian skip.** It is needed exactly when q is inert and [ā] = [−1]. The supplement then gives q ≡ 1 (4). Only the circle at q can put i into κ_q: roots with [ā] ≠ [−1] and the regular edges cannot. So the TS predicate still fires, and the skip is supplied by that circle.
- **Parsimony.** Doubled local histories give finitely many copies at each depth, so the prefixes cover every copy and parsimony is uniform over copy choices.
- **Interfaces** all check: units ℚ*, the B ∩ F = A normal form, rational Nagata (the generic fibre is a PID), L1, the circle order from `LOGIC_CIRCLE_AUDIT` §2, the L2 descent, and L(D) from `IE1_ES`.

## Target 2: BCM + Lagrange + Bézout + IOpen end extension with full prime QR, and ¬ES(P)

- **Specialization on squareclasses.** I checked the Steinberg relation case by case (w(a) > 0, < 0, = 0 with ā = 1 or ā ≠ 1). Merkurjev then gives a well-defined map.
- **Base identity (B).**
  - The jump at each root, (−1)^{mn}·(signs), is the tame symbol.
  - The bit at 0⁺ equals real_F(sp_w α), because c_j > 0.
  - Each positive root has exactly one positive lift, so the characters agree across twist levels, using the sum over descendants before stabilization.
- **Initial (B).** It follows from (R) of the z75 QR PID, using inv_ℓ = Legendre∘∂_ℓ at ordinary odd ℓ.
- **Extension across upper edges.** On old classes the defect real_E + S_new∘sp_w + Σ vertical vanishes, given index one and κ(w) ⊂ κ(w′). Lines and quadrics have constant unramified 2-torsion.
- **Root-edge axis checks.** The residual diagram is a line with q̄ ≠ 0 inverted. The tree branches only on take/skip, so there is no circularity.
- **§5 prime classification.** Normalizing by the content unit works. q is prime in D′, and D′/q ≅ B°/q via h-invertibility. One step needs a stated proof (F8): in a Bézout domain a principal prime is maximal (localize at a maximal ideal, where it becomes a valuation domain); I verified this. Elements of positive axis value are reducible, and value-zero elements without support are old.
- **Layer descent.**
  - The composite axis, H-mark and discrete-mark maps are ring homomorphisms on integral entries and extend the ancestors' maps.
  - Remainders d are old by endness, so red_q φ_q(p̄) = d mod q.
  - Odd terms vanish on S′-units, and the dyadic bottom gives εε, ε and ω.
  - So (p,q), (−1,p) and (2,p) give QR with both supplements.
- **"Why the modification matters."** This is correct: r(0) < 0, q ≡ −1 modulo every old positive, and the cyclic 2-power tower over F(μ_{2^∞}) contains only one quadratic extension, so 3 or 5 fails. It is a new scoped negative result about the unmodified z75 BCM union.

## Fixes requested

- **F1 (§3, uniformity; substantive).** The sentence "pull back dense opens … for each parameter value" does not show that the bad set and the complexity are independent of t_ℓ. Fix: over F̄_ℓ pick w with w² = t. The map (b,v) ↦ (b, wv) is an isomorphism from the t-fibre to the t=1 joint open, and it carries all pulled-back test functions along, because b′ = b(wv)². So geometric integrality, smoothness, the excluded characteristics and the degree bounds are those of t=1, and Lang–Weil is uniform.
- **F2 (§2).** State W as a kernel and the map W/old ↪ ⊕_ℓ 𝔽₂ as a proposition. Say that rational factoriality is enough for a ∈ ℚ*F*². The Gaussian UFD is genuinely needed only for split TS and the root skip.
- **F3.** Display β(bt) − β(b) = (a, δ(t)) explicitly, with the global H²(X,μ₂) lift and cancellation of the constant term.
- **F4.** Make the skip accounting explicit: the skipped set is exactly {(q,[−1]) : q inert, q ≡ 1 (4)}, and i enters κ_q only through the circle at q. Replace "or it will be there even earlier".
- **F5 (§0).** Write out the STATUS delta text for both §1E rows. At export, update STATUS:132 ("Not claimed … simultaneous QR + universal TS"), the open item at STATUS:156, and FRONTIER:2811. Change "Review: pending" to "none (cross-review owed)". Give the side result its own label and triage (METHOD-CX for the FRONTIER §6 / WAVES line).
- **F6.** Replace every "z75 §N" with the actual file name. In §§3–5 it switches between `BCM4_QR.md` and `BCM4_PUSH2.md`.
- **F7 (§4).** State the first-successor convention explicitly (S_H := inv₂ at 2). Say that "odd PID primes" includes the nonstandard D₀ primes with their z75 characters, and that the bottom identity is derived from (R).
- **F8 (§5).** Add the one-line proof that principal primes in a Bézout domain are maximal.
- **F9 (§1).** Fix the garbled sentence about "characteristic-two coefficient twists". Define "parameter". Mark the infinite-rank paragraph as a side remark.
- **F10 (§4).** State that w′ extends w with the same group G and that κ(w) ⊂ κ(w′) (from the axis checks). This is what makes S_new∘sp_w agree on old classes.

Form overall: the commit is a single new lane note with no master-file edits, which is correct per AGENTS.md. Readability is the main weakness: it is dense to the point that the proof is hard to verify.
