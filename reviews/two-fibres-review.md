# R214 — hostile review of O209 (TWO_FIBRES.md, BRAINSTORM/y1_*.md, AGENT_REPORT_O209.md)

Reviewer: R214 side agent (branch side-agent/review-two-fibres; merged side-agent/two-fibres at its tip).
From-scratch scripts: `scripts/review_r214_*` (none of the author's `y1_*` scripts or `si_census.c` reused).
Status: IN PROGRESS.

## Summary verdicts
(filled in claim by claim below)

## Claim-by-claim

### Thm A (TWO_FIBRES §1; memo H1) — SOUND (minor wording repairs, see D1, D2)
Re-derived every step:
* (ii)⇒(iii). In C₀(L_w) with e₁² = v, e₂² = t, e₃² = u, B(e₁,e₂) = B(e₂,e₃) = −1, B(e₁,e₃) = 0: α = e₁e₂, β = e₂e₃
  have trd α = trd β = −2, nrd α = tv, nrd β = tu, so i = 1 + α, j = 1 + β are trace-zero with nrd A*, A; a direct
  Clifford computation gives βα = −tγ − 2α − 2β − 4 (γ = e₁e₃), αβ = tγ, hence ij + ji = −2 ✓, and
  (1 − i)(1 − j) = αβ = tγ with trd γ = 2B(e₁,e₃) = 0 ✓. B_{2,∞} = (−1,−1)_ℚ has type number 1 (one conjugacy class of
  maximal orders, the Hurwitz order H); trace-zero elements of H are exactly ℤi + ℤj + ℤk (the elements with all
  coordinates in ½ + ℤ have real part ±½) ✓; trace-zero elements of tH are tℤ³ ✓. pq = −p·q + p × q for pure
  quaternions gives (1 − i)(1 − j) = z − x − y ✓.
* (iii) ⇒ (iv). Recomputed: γ·x = −(A* + 1)/t = −v, γ·y = −u, |z|² = AA* − 1 = tn, z ⊥ x, y, so
  |γ|² = (tn + A + A* + 2)/t² = uv ✓. adj(G_w) = [[A, u, 1], [u, uv, v], [1, v, A*]], which is the Gram of (y, −γ, x) ✓.
  M ⊂ ℤ³ ⊂ M^#, [M^# : M] = n², [ℤ³ : M] = n ⇒ [M^# : ℤ³] = n ⇒ nM^# ⊂ ℤ³ ✓; Gram of nM^# is n²(nG_w⁻¹)⁻¹ = nG_w ✓.
* (iii) without congruence ⇒ (ii), and (iv) ⇒ (ii): similarity invariance of C₀ in odd rank ✓. Since (ii) ⇒ (iii) gives
  the congruence version, the cycle (iii⁻) ⇒ (ii) ⇒ (iii⁺) ⇒ (iv) ⇒ (ii) closes and all four are equivalent ✓.
* (i) ⟺ (ii) is SIGN_IDENTITY Prop 4.1(b) (previously reviewed, (J)39) ✓.

**From-scratch numerics** (`scripts/review_r214_lift.c`; Diff computed from Hilbert symbols of (−A*, −tnA*) at all
primes | 2tnA*, *not* from the author's formula; lift search: canonical x up to signed permutation for the smaller norm,
then exact solution of the quadratic for y on the plane x·y = 1; cross-checked against a naive exhaustive Python search,
`scripts/review_r214_brute_small.py`, 607 words n ≤ 61, 0 mismatches; |Diff| odd on every word):
| check | range | words | result |
|---|---|---|---|
| (iii) ⟺ Diff = {2} | all odd n ≤ 1500 | 35 184 | 8 231 Diff = {2}, 8 231 lift, **0 mismatches**; 3 128 words with χ = +1, Diff ⊋ {2} correctly do not lift |
| (iii) ⟺ χ = +1 (primes) | primes 3 ≤ p ≤ 3000 | 27 340 | 8 408 / 8 408, **0 mismatches**; χ = +1 ⟺ Diff = {2} on all |
| (iii) with x × y ≡ ±(x + y) (mod t) | odd n ≤ 451 | 7 939 | all 2 088 lifting words admit a congruent lift (the ± is the O(3) orientation: a reflection flips x × y) |
| (iv) n·G_w ∈ Gram(ℤ³) ⟺ Diff = {2}, direct search for (a, b, c) | odd n ≤ 451 | 7 939 | 2 088 / 2 088, **0 mismatches** |
Word counts agree with the author's (7 934 for 3 ≤ n ≤ 451; mine include n = 1's 5 words).

### Thm B (TWO_FIBRES §2; memo H2) — SOUND (citation wording D3)
Re-derived: L_w ⊗ ℚ has square determinant, is positive, and C₀ ≅ B_{2,∞} (Prop 4.1(d)); a ternary ℚ-space is
determined by signature, discriminant and C₀, so L_w ⊗ ℚ ≅ I₃ ⊗ ℚ ✓. Every lattice with integral norms lies in a
norm-maximal lattice; all norm-maximal lattices on a space form one genus (O'Meara 91:2); ℤ³ is norm-maximal in I₃ ⊗ ℚ
(an index-2 overlattice would need x/2, x ∈ ℤ³ ∖ 2ℤ³ with |x|² ≡ 0 (4), impossible), so that genus is gen(I₃), which has
one class ✓. Index = √det = m ✓. Prime m = q: M = ker(f mod q); if f·f ≡ 0 (q) then f ∈ M, f/q ∈ M^# ∖ ℤ³, and
M^#/M ⊇ ⟨ℤ³/M, f/q⟩ ≅ (ℤ/q)², contradicting cyclicity of M^#/M (G_w has the 2×2 minor
det[[−1, 0], [t, −1]] = 1, so its Smith form is (1, 1, n)) ✓.
**Numerics** (`review_r214_lift.c B`): every word of every odd square m² ≤ 141² = 19 881 (2 844 words): Diff = {2}
(T1) and an explicit (a, b, c) ∈ (ℤ³)³ with Gram G_w found — **0 failures**.

### Cor A1 — SOUND
χ(w) = −1 ⟺ ¬(iii) ⟺ ¬(iv) by Thm A at n = p, and (iii) is literally "T_w is represented by I₃"; combined with the
campaign's ES-five(p) ⟺ N₋(p) ≥ 1 (CONSTRUCTIVE/SIGN_IDENTITY, not restated in TWO_FIBRES — MINOR D4). Nothing beyond Thm A.

### Prop A2 / H4 (χ = +1 genus = conic/S₄ image) — SOUND; CERTIFIED claim TRUE as stated but incomplete (D5)
Re-derived: L(p) ⊗ ℚ has det p⁴ (square) and C₀ ≅ B_{2,∞}, so L(p) ↪ ℤ³ (as for Thm B) with index p². Totally
isotropic image mod p has dim ≤ 1; [ℤ³ : M + pℤ³] = p^{3−d} ≤ [ℤ³ : M] = p² forces d = 1 **and M ⊇ pℤ³** (the text
says "the index forces M = pℤ³ + ℤℓ̃" — correct, this is the one-line reason). Converse (integrality via ℓ·ℓ ≡ 0, det
p⁴/p³ = p, isotropy at p from C₀) ✓. #C(𝔽_p) = p + 1 and −1 ∈ O(ℤ³) acts trivially on ℙ², so the effective group is S₄ ✓.

**From-scratch certification** (`scripts/review_r214_conic.py`: orbits of signed permutations on C(𝔽_p); canonical
isometry form = lexicographically minimal Gram over all bases realising the successive minima; the genus 𝔊⁺_p enumerated
*independently* from all forms with a ≤ b ≤ c, abc ≤ 2p, 2|f| ≤ a, 2|e| ≤ a, 2|d| ≤ b, det p, filtered by isotropy at p
via counting zeros mod p): for **all** primes 5 ≤ p ≤ 127, image of the L_ℓ = 𝔊⁺_p (onto ✓). #orbits vs #classes:
equal for every p ≤ 67 and for 73, 83, 89, 97, 101, 103; **strictly fewer classes at p = 71 (3 → 2), 79 (4 → 3),
107 (5 → 4), 109 (6 → 5), 113 (6 → 5), 127 (6 → 5)**. The author's list (13, 17, 29, …, 101, 109) contains only
p ≡ 1 (4) and misses the first non-injective cases 71, 79; the statement "onto, not always injective" is right, the
implied "p = 109 is the exception" is not. In every collapse two size-24 orbits merge (consistent with the second unimodular
overlattice of pℤ³ + ℤℓ̃, i.e. the Atkin–Lehner w_p swap of the edge's two ends) — Assessment, not checked further.

