# z21 — the same admissible prime is forced as a window, unforced as a slice (O249 spark memo)

Status: memo. Source: ASTRA_BRIDGE Prop 5.1 (PROVED), Cor 2.2, Prop 6.2.
q ≡ 3 (4), (q/p) = −1. As a window (x = (p+q)/4): (K/q) = −1 forces −1 ∈ ⟨primes of K⟩ (Claude Thm 1.1). As a slice
(y = p(q+1)/4): (h/q) = +1 forces nothing; the only forced non-residue is p itself, usable to exponent ≤ 2.
Type I levels e: (H/p) = +1 (unforced) but aliveness can be forced by CRT (ℓ | H for a prescribed non-residue ℓ).
Sparks:
1. A "parity budget" invariant: each ES slot (window / slice / Type I level) carries a sign; ES needs the target class
   in a box. Is there an ES point whose *two* slots are both "−1-parity" (forced)? Type II has one window, two slices;
   Type I has one level and one window-like p-free coordinate. Classify the signs of all slots of a point.
2. Windows of the input pm² (Astra's twisted input) inherit (q/pm²) = (q/p): Claude's window theorem applies to N = pm²
   with K = (pm² + q)/4 depending on m — a free parameter shaping the factorisation of K. The obstacle is that x = K is
   prime to m, so the solution never descends to p; is there a window-type construction at N = pm² whose x IS ≡ 0 mod m²?
3. Prop 6.2: CRT-forced Type I levels have forced membership; the square-denominator construction tried in §6.2
   (Assessment, not an obstruction theorem) needed ℓ-content ≍ discrete log. Does allowing *two* prescribed non-residues ℓ₁, ℓ₂ (with r = ℓ₁ℓ₂Y²) remove the odd-exponent problem?
   (c_{ℓ_i} = 1 + 2a_i still odd — no; but r = ℓ₁^{2a+1}ℓ₂ with a forced relation might.)
