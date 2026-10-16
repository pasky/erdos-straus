# z21 — one lattice per slice: Astra's line Y = 1 meets Claude's lines M | 2h at ES (O249 spark memo)

Status: memo (Assessment unless stated). Source: ASTRA_BRIDGE Thm 3.4 (PROVED).
For a slice g ≡ 3 (4), h = (g+1)/4, ρ² ≡ −p (mod g): L_ρ(g) = {Y ≡ ρM (mod g)}. Astra sources = (m, 1); Claude shots
= (2k, Y), k | h, overflow Y (self-mute: rad Y | h); ES = (2k, 1), k | h.
Sparks (not pursued):
1. **Moving the slice.** Every move inside a fixed L_ρ(g) is a lattice translation; ES needs the slice g itself to
   satisfy 4k | g + 1 for a k with 2kρ ≡ 1. Is there a natural map g → g′ (e.g. composition of the ideal above g with
   a fixed ideal of norm ℓ in ℤ[√−p]) that carries a Claude point (2k, Y) to a point with smaller |Y| and still
   k′ | h′? Composition in Cl(−4p) multiplies the forms; the divisibility k | (g+1)/4 is not a class invariant — test
   whether it is *forced* for some composition chain (it is a B2 event a priori).
2. **Reduced forms.** The reduced form of disc −4p in the class of 𝔤 has a minimal vector (M, Y) with D ≤ √(4p/3);
   when is M even with M/2 | h? This would be a deterministic small-D source; quantify over the h(−4p) classes.
3. **Two slices at once.** A Type II ES point has two slices (g for y, g′ for z) and one window. Claude and Astra
   each use one slice. Do the two slice lattices of the same point determine each other (they must: z = ...);
   a two-lattice formulation might expose a parity constraint that forces one of them.
