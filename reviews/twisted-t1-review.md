# R182 — hostile review of O182 (TWISTED_T1.md, BRAINSTORM/bsI_*.md)

Reviewer: R182 (side agent). Status: in progress. **ES is not solved here.**
From-scratch scripts: `scripts/review_tw_*.py` (own ℤ[ω] arithmetic, own cubic residue / tame / λ-adic symbols).

## Summary verdicts
(filled in below, claim by claim)

## Defects

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
