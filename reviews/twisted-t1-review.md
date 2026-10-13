# R182 — hostile review of O182 (TWISTED_T1.md, BRAINSTORM/bsI_*.md)

Reviewer: R182 (side agent). Status: round 1 complete.
**Repairs applied** (author quiet since the checkpoint commit): D1–D8, D10–D13 applied directly as marked
'(R182 repair …)' in TWISTED_T1.md, BRAINSTORM/bsI_anchor_calculus.md and reviews/agent-reports/AGENT_REPORT_O182.md. **ES is not solved here.**
From-scratch scripts: `scripts/review_tw_*.py` (own ℤ[ω] arithmetic, own cubic residue / tame / λ-adic symbols).

## Summary verdicts
| claim | verdict |
|---|---|
| **Thm 3.2** (order-3 T1 for TES; (a) reciprocity law, (b) no Type I/II at π³ (and π^{3k}), (c)) | **SOUND** (minor D1–D5) |
| Lemma 1.1 | SOUND |
| Prop 1.2 | SOUND |
| Cor 1.3 | SOUND (wording D8) |
| Lemma 2.1 | SOUND (D6) |
| Cor 2.2 (incl. (f) conductor bound) | SOUND — (f) verified by exact computation, citation downgraded (D7) |
| Prop 2.3 | SOUND |
| Lemma 3.1 | SOUND |
| Thm 4.1 | SOUND-AFTER-REPAIRS ((c) is not a theorem, D10) |
| **Prop 4.3** | **GAP** — number-field part sound; FF part outside the stated template and the "no odd-square obstruction over F_q[T]" attribution is wrong (m = 2 is outside the template) — MAJOR D11 |
| §3 tables, exponent law, controls (EVIDENCE) | SOUND — reproduced exactly from scratch (t = 3 control within window rounding) |
| §5 census (EVIDENCE) | SOUND-AFTER-REPAIRS — no inert primes were actually included (D12); 18 failures reproduced |
| Labels / Assessments | D10, D11, D13 |

No FATAL defect. One MAJOR (D11, scope/attribution). The headline is a genuine, correctly proved order-3
T1; I independently confirmed the partner vanishing at λ by a direct local norm-group computation on every point.

## Defects
1. **D1 (MINOR) Thm 3.2(b) statement.** States only n = π³; the report and bsI memo claim π^{3k}, which the proof
   (and Thm 4.1(b)) gives. *Repair:* "n = π^{3k}, k ≥ 1".
2. **D2 (MINOR) §3 numerics, validation of inv_λ.** inv_λ was only inferred as −Σ_tame; the "400 random pairs with
   a ∈ U^{(4)}" check exercises only the case where the λ-symbol is trivial. *Repair:* cite R182's direct
   norm-residue computation (inv_λ = 0 on all points; reciprocity cross-check with 189 non-trivial λ-symbols).
3. **D3 (MINOR, framing) "2-primary is the analogue of positivity / monic".** It is a choice of associate only for x
   prime to 2: the normalisation also **forbids denominators divisible by 2**, which positivity/monic never do.
   *Repair:* say "kernel of reduction at the anchor (analogue of the kernel of sign); it also excludes denominators
   divisible by the anchor prime".
4. **D4 (MINOR) search window.** The text says N(X − c_i n/t) ≤ B; the code centres at the *rounded* c_i n/t and
   bounds the offset. Same window for t = 9 rows (identical counts), slightly different for the t = 3 control
   (660/299 vs exact 658/301, cubes 306/164/1493 vs 308/164/1504) and π⁶ (57 vs 56). *Repair:* state the window as
   implemented.
5. **D5 (MINOR) §3 wording.** "Every prime has Type I/II solutions" holds for the 8 tabulated primes only (the census
   has 18 window failures); "TES(π³) is globally solvable" is EVIDENCE for the 5 cubes but PROVED whenever TES(π)
   is solvable (π 2-primary ⇒ (π²x_i) solves TES(π³)). *Repair:* scope + add the one-line inheritance proof.
6. **D6 (MINOR) dangling reference** "see Lemma 2.4" after Lemma 2.1: no Lemma 2.4 exists. *Repair:* point to the
   Thm 3.2 proof at λ / Principle (β) (where the equation pins the partner invariant).
7. **D7 (MINOR) Cor 2.2(f) citation from memory.** Not checkable against sources/. *Repair:* label "standard
   (Fesenko–Vostokov / Serre XIV, not checked); the instance used is verified (R182: ⟨1+λ², 1+λ³⟩_λ = 0 by the
   norm-residue definition; sharp: ⟨1+λ, 1+λ²⟩_λ ≠ 0)".
8. **D8 (MINOR) Cor 1.3 "it is empty".** Means "vacuous"; and non-vacuity on realised degree vectors is DRINFELD's
   EVIDENCE. *Repair:* reword.
9. **D10 (MINOR, label) Thm 4.1(c)** "unconstrained" is not proved. *Repair:* move (c) to a remark.
10. **D11 (MAJOR, scope/attribution) Prop 4.3(i).** See verdict above. *Repair:* (1) restrict Prop 4.3 to number
    fields, add an FF corollary stating the FF template explicitly (∞ ∈ S, monic at ∞) whose proof is Cor 2.2(c) +
    "every place tame"; (2) replace "the structural reason behind FUNCTIONFIELD_ES's 'no odd-square obstruction'"
    by "the odd-m analogue of FUNCTIONFIELD_ES's absence of an odd-square obstruction; for m = 2 the reason is on the
    anchor side ((−1, −1) split over F_q(T); for q ≡ 3 (4) the monic normalisation is not isotropic, giving the
    degree-dependent sign of (J)4 Prop 4.1)"; (3) fix the μ_p parenthetical; same edits in report SHARP 2 and
    bsI_anchor_calculus.
11. **D12 (MINOR) census description.** "and inert p ≤ 77 (746 primes)": the script includes no inert primes
    (746 = 2 × 373 split). *Repair:* correct the description and add R182's inert run (10 primes, all solved).
12. **D13 (MINOR, label) Remark 4.1(4)** "ES's T1 is the m = 2 member of a family whose odd members are strictly
    easier to prove": m = 2 is outside the template; label Assessment.

(D9 withdrawn: I checked whether other degenerate degree configurations escape Lemma 1.1 — all three degrees equal
D > n − k is impossible since then Σ c_i/X_i has no term of degree k − n.)

### Thm 3.2 (headline: order-3 T1 for TES over ℤ[ω]) — **SOUND** (minor repairs D1–D5)
Re-derived from scratch, place by place (K = ℚ(ω): places (2) inert with k = F₄, λ = 1 − ω, primes π | n, other
tame primes, one complex place; c = (ω, ω², 2), u_i = x_i/c_i, α = (−u₁/u₃, −u₂/u₃)_ω):
* **v = 2 (anchor).** x_i ∈ 1 + 2O₂ = U^{(1)}, pro-2, hence cubes; so α ≡ (τ₁, τ₂) = (−2/ω, −2/ω²) mod cubes.
  Expanding: ⟨2,2⟩ = ⟨2,−1⟩ = 0, units pair trivially at a tame place, ⟨2, ω^{−2}⟩ + ⟨ω^{−1}, 2⟩ = 2⟨ω,2⟩ − ⟨ω,2⟩
  = ⟨ω, 2⟩. Tame symbol {ω, 2}₂ = ω^{v(2)}·2^{−v(ω)} = ω mod 2, a non-cube in F₄^* (all of F₄^* has order 3,
  cubes = {1}). ✓ (my code: inv₂ = 1 on every point, same normalisation as the author.)
* **v = λ (partner).** u_i ∈ O_λ (ω, 2 and n are λ-units); for ANY labelling −x = 1 − (9/n)u₁ ∈ U^{(4)}
  (v_λ(9) = 4), and U^{(4)} = (U^{(2)})³ ⊂ K_λ^{*3} (p = 3, e = 2, i > e/(p−1) = 1; Neukirch II (5.5)–(5.8)).
  −1 is a cube, so both Steinberg terms vanish. ✓ The "relabel so v_λ(u₁) is maximal" step is unnecessary but harmless.
  The case u_i + u_j = 0 is in fact impossible for TES (y = −ωx contradicts x ≡ y ≡ 1 mod 2; 2x = −ωz contradicts
  v₂), so Steinberg always applies. **Independent check:** `review_tw_zw.py` computes the λ-adic cubic symbol by
  its *definition* (b ∈ N(K_λ(a^{1/3})^*)·K_λ^{*3}, the norm group found by sampling norms c₀³ + ac₁³ + a²c₂³ − 3ac₀c₁c₂
  and certified exact because it reaches index 3, which local CFT forces), validated against Hilbert reciprocity
  with my own tame symbols on 300 random pairs (189 non-trivial at λ). On all 8 002 TES points of my census and
  all table points, inv_λ = 0 **directly**, not via reciprocity (the author only had −Σ_tame).
* **v tame, v ∤ 6n.** u_i v-integral, 9/n a v-unit; DRINFELD_ES Thm 2.2(i) re-derived (x ≡ −1 unit ⇒ symbol ±1;
  all u_i units ⇒ symbol 1 or y ≡ 1); ±1 are cubes. ✓
* **Complex place** 0; Hilbert reciprocity for the cyclic algebra ⇒ (a); (c) is (a) with one place. ✓
* **(b)** DRINFELD Thm 3.3's argument transposes verbatim (re-derived): Type II, u₁ the π-free one: v_π(x) = −3,
  forcing v_π(u₂) = v_π(u₃), symbol y³; Type I, u₁ the π-divisible one: v_π(x) = 0 ⇒ 1; v_π(x) > 0 ⇒ v_π(u₁) = 3
  and v_π(x) ≥ 3, symbol y^{−3} or y ≡ 1. Both cubes ⇒ inv_π = 0, contradicting (a). The same works for π^{3k}. ✓
* **Normalisation.** "x ≡ 1 (mod 2)" is exactly "x prime to 2 and x ∈ U^{(1)} at (2)"; units ±ω^j surject onto
  F₄^*, so for x prime to 2 it is a choice of associate up to the cube −1, and N̄ = 0 because U^{(1)} is pro-2 — the
  same mechanism that makes ℝ_{>0} pin ⟨−1,−1⟩_∞. Caveat (D3): unlike positivity/monic it also **excludes all
  denominators divisible by the anchor prime 2** — the analogy is "kernel of reduction" ≈ "kernel of sign", not a
  pure choice of generator for every ideal.
* **Tables recomputed from scratch** (`review_tw_tes.py`, exact window N(9X − c_i n) ≤ 81B, every solution verified
  by clearing denominators; logs `logs/review_tw_table_*.txt`, `review_tw_exponents.txt`):

| row | author | R182 |
|---|---|---|
| TES, 8 split primes (same selection), B = 30 | I 117, II 44, other 0, all (1,2,0) | **identical** (λ = 0 by brute force) |
| TES, π³, N(π) ∈ {7,…,37}, B = 30 | 0 / 0 / 87 | **identical**; also B = 300: 0 Type I/II of 98 |
| control (9; 1,1,1) | primes 51/9; cubes 42/6/96 | **identical** |
| control (3; ω, ω², 2) | primes 660/299; cubes 306/164/1493 | 658/301; 308/164/1504 (window rounding, D4); at cubes every Type I/II point has inv_π = 0 and inv_λ ≠ 0 — the predicted compensation |
| π², π⁴ (N = 7), π⁶ (B = 20), 5³, 11³ | I2 II1; I1; 0 of 57; 0/46; 0/192 | same; π⁶: 0 of 56 |

  The proof covers every solution (no window), so "no Type I/II at π^{3k}" needs no numerics; the zero rows are
  consistency checks. That TES(π³) is solvable is PROVED whenever TES(π) is (π 2-primary ⇒ π² ≡ 1 (2), so
  (π²x_i) is a TES(π³) solution) — and TES(π) solvability itself is EVIDENCE for the tested π.

### Lemma 1.1 — **SOUND**
v_Q(A/P) = −e (Q ∤ A); if every v_Q(c_i/X_i) ≥ −e + 1 the sum would too, so some Q^e | X_i, deg X_i ≥ n > n − k.
Re-derived; trivially correct. It kills exactly the literal "all three of degree n − k" configuration (D9 notes the
scope).

### Prop 1.2 — **SOUND**
Re-derived: at ∞, a = −u₁/u₃ has sign −c₃/c₁ and v = d₃ − d₁, b has sign −c₃/c₂ and v = d₃ − d₂; the tame symbol's
odd part is (c₃/c₁)^{d₃−d₂}(c₃/c₂)^{d₁−d₃} (−1 is an m-th power for odd m, so dropping signs is exact), and the log
expands to the stated 3×3 determinant (checked by hand). Consistency with DRINFELD Lemma 3.2 (which computes the
(x, y) Steinberg term in the labelling deg X₁ > n − k): the difference of the two formulas is
w₂(d₃ − d₀) − w₃(d₂ − d₀), d₀ = n − k; by the leading-term identity a lone minimal-degree term has c = 1 (w = 0),
and if d₂ = d₃ = d₀ it is 0 directly — so they agree on every solution, as the author says. ✓

### Cor 1.3 — **SOUND** (wording, D8)
χ_∞ = 0 at Type I/II-shaped points of P = Q^m follows from DRINFELD Thm 3.3 + Lemma 3.1 + reciprocity; the linear
form d ↦ det(1, w, d) is zero iff all w_i are equal mod m. ✓ "It is empty" means "the condition is vacuous". That
the condition actually bites on *realised* degree vectors (not just on ℤ³) is DRINFELD's EVIDENCE tables, not this
proof.

### Lemma 2.1 — **SOUND** (D6: dangling reference)
Re-derived exactly as written (take X₃ = 1, then r = 1 resp. s = 1). Scope: constancy over the whole local family
N_v³, not over the solution set; the doc says so ("normalisation-only anchor") but points to a **non-existent
"Lemma 2.4"**. The odd-m cyclic-sum formula re-derived (⟨−x, y⟩ = ⟨x, y⟩, antisymmetry, ⟨c₃, c₃⟩ = 0). ✓

### Cor 2.2 — **SOUND** ((f) now verified; D7 for the citation)
(a)–(e) re-derived (standard tame-symbol facts; for (c) ⟨T, T⟩_∞ = ⟨T, −1⟩_∞ = class of −1, an m-th power for odd
m; Lagrangian since |N̄|² = |V|). (f): the conductor bound was quoted from memory and I could not access
Fesenko–Vostokov or Serre XIV in sources/. **Verified by exact computation instead** (`review_tw_zw.py`,
`logs/review_tw_zw_selftest.txt`): V_λ = K_λ^*/K_λ^{*3} ≅ ℤ/3 × U^{(1)}/U^{(4)} with basis λ, 1+λ, 1+λ², 1+λ³
(27 distinct classes mod λ⁴ = (9); U^{(4)} ⊂ cubes checked mod λ⁸); by the norm-residue definition
⟨1+λ², 1+λ³⟩_λ = 0, so (alternating, bilinear) ⟨U^{(2)}, U^{(2)}⟩ = 0: N̄ = ±U^{(2)} image (order 9) is isotropic,
hence Lagrangian. The bound is sharp: ⟨1+λ, 1+λ²⟩_λ ≠ 0 (i + j = 3). Also ⟨1+λ, 1+λ³⟩ = ⟨ω, 1+λ³⟩ = 0 and
⟨λ, 1+λ³⟩ ≠ 0, consistent with U^{(3)} = U^{(pe/(p−1))} giving the unramified extension. A one-line hand proof of
what is needed: 1+λ³ ∈ U^{(3)} has unramified Kummer extension, hence pairs trivially with all units.

### Prop 2.3 — **SOUND**
Reciprocity for the constant algebra. (i) symbols of two constants are trivial at every place of F_q(T) (incl. ∞),
so 0 in Br. (ii) unit twists: ⟨ζ^a, ζ^b⟩_λ = ab⟨ζ, −1⟩ = 0 — confirmed numerically: (ω, ω)_λ, (ω, −1)_λ trivial.
For the TES twist the constant algebra (ω, 2) is ramified exactly at {2, λ}: (ω, 2)_λ ≠ 0 by my brute force,
matching "anchor 2, partner λ". (iii) (−1, −1) ramified at {∞, 2}; and I checked from scratch (`review_tw_es2.py`,
2-adic Hilbert symbol) that on all 74 616 labelled ES solutions with n odd < 400, inv₂ α = 0 and Σ_{p|n} inv_p = ½,
consistent with "partner 2, forced by the equation" in Principle (β).

### Lemma 3.1 — **SOUND**
mod 2: ω/x + ω²/y ≡ ω + ω² = −1 ≡ 1, 2/z ≡ 0 (z a 2-unit), 9/n ≡ 1/n. ✓

### Thm 4.1 — **SOUND-AFTER-REPAIRS** (D10)
(a), (b) re-derived as for Thm 3.2: anchor by (A)+Lemma 2.1; v | m ∉ S by (P) (any labelling works); tame v ∉ S,
v ∤ mn by (U) and DRINFELD Thm 2.2(i) (which allows v | t, as it allows ℓ | A); archimedean places contribute
nothing (K is totally complex). The coefficients c_i are units outside S ∪ {v | m}, and n is coprime to S, m, t, c,
so no place is missed. (c) is **not a theorem**: "unconstrained" is an observation (PROVED is only that the proof's
symbol is y^{±e}); it is listed under a PROVED label.

### Prop 4.3 — **GAP (scope/attribution), MAJOR D11**
The number-field statement is correct and nearly tautological: A_S = −Σ_{w∉S}⟨τ₁,τ₂⟩_w and all w ∉ S, w ∤ m
contribute 0 (unit twists, tame). But:
* "(i) over a global function field … no order-m T1 of this template exists" applies a template that Thm 4.1 defines
  **only for number fields** (O_K-integral points, archimedean places). The FF version (integrality away from a set
  of places at ∞ that must lie in S, (A) at ∞ for the monic normalisation) is only sketched in the caveat.
  Correct after stating it; then the claim reduces to Cor 2.2(c) + "every place is tame".
* "the structural reason behind FUNCTIONFIELD_ES's 'no odd-square obstruction over F_q[T]'" is a **misattribution**:
  the odd-square obstruction has order 2 and m = 2 is excluded from the template by the doc's own Remark 4.1(4)
  (tame places give no information for m = 2, so "partner must be wild" is not the operative mechanism). The FF
  m = 2 explanation is the anchor side: (−1, −1) is split over F_q(T) (Prop 2.3(i) works for every m), and for q ≡ 3
  (mod 4) the monic normalisation is not even isotropic for m = 2 (⟨T, T⟩_∞ = ⟨T, −1⟩_∞ ≠ 0), which is the
  degree-dependent sign of (J)4 Prop 4.1 — consistent with (J)18's "pinned degree" Assessment, not with "no wild
  place". The same overclaim is repeated in the report (SHARP 2) and bsI_anchor_calculus.
* "(and μ_m ⊄ K when m = p)": in characteristic p, μ_p = 1, so the template (which needs μ_m ⊂ K) is vacuous for
  m = p; the parenthetical as written is garbled.

### §5 census (EVIDENCE) — **SOUND-AFTER-REPAIRS** (D12)
Reproduced from scratch (`logs/review_tw_census.txt`, B = 60, exact window): the same **18 window failures**
(9 conjugate pairs, identical norms); split primes 5 870 Type I + 1 968 Type II (author 5 849 + 1 968; the
difference is window rounding, D4); every point (1, 2, 0) with λ checked directly. N = 103, 151: no solution for
B = 600; N = 103: none with all X of N(X) ≤ 20 000. The wide search adds nothing for N = 307 (2) and 439 (54).
The 18 failures all have χ_π(ω) ≠ 0 and χ_π(2) ≠ 0 (confirmed). **But the author's census contains no inert
primes**: the loop starts at 101, so "p > 101 and p² ≤ 6000" is empty, and 746 = 2 × 373 split primes. I ran the
10 inert primes 5 ≤ p ≤ 71: all have Type I/II solutions (117 I, 47 II), all (1, 2, 0). Quadratic part (§5,
`tw_eis_quad.py`) **not checked** (Assessment-level anyway).
