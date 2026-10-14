# R214 — hostile review of O209 (TWO_FIBRES.md, BRAINSTORM/y1_*.md, AGENT_REPORT_O209.md)

Reviewer: R214 side agent (branch side-agent/review-two-fibres; merged side-agent/two-fibres at its tip).
From-scratch scripts: `scripts/review_r214_*` (none of the author's `y1_*` scripts or `si_census.c` reused).
Status: round 1 complete. Repairs applied: none (author worktree still live; defects forwarded via parent).

## Summary verdicts
| claim | verdict |
|---|---|
| Thm A (H1), incl. nM^# ⊂ ℤ³ and the congruence | **SOUND** (MINOR D1, D2) — 0 mismatches on 35 184 words n ≤ 1500, 27 340 words of primes ≤ 3000; (iv) direct on 7 939 words n ≤ 451 |
| Thm B (H2), incl. f off the conic | **SOUND** (MINOR D3) — 2 844 words of odd squares ≤ 19 881 all embed with Gram G_w |
| Cor A1 (H3) | **SOUND** (MINOR D4) |
| Prop A2 (H4), 𝔊⁺_p = image of P¹/S₄ | **SOUND**; CERTIFIED counts true but incomplete — non-injective already at p = 71, 79 (D5) |
| Props G, G′ | **SOUND-AFTER-REPAIRS**: conclusion true and in fact *unconditional* (size at primes, no T1, no ℓ₀) (MAJOR D6); the ℓ₀ hypothesis fails for Ad(tetrahedral) — "we do not know whether such π exist" is wrong (MAJOR D7); MINOR D8 |
| G1, G2, G3 | **SOUND** (MINOR D10, D11) |
| K1 | **SOUND** |
| R1 | **SOUND** (parity verified to 10⁶) |
| R3 | **GAP** (label/precision; trivial once stated, D12) |
| EVIDENCE: sign dominance fails at 2 402 primes; N₋ mod 8 equidistributed; per-class ratios | **reproduced exactly** over the full range p < 10⁶; "near squares" description wrong (D9) |
| Cerednik–Drinfeld reading | Assessment label correct; count inconsistency (D13) |
| Novelty / labels | no external claim (correct); classical attributions should be explicit (D2) |

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

### Props G, G′ (memo y1_gl3_cuspidal; TWO_FIBRES Summary, §4) — SOUND-AFTER-REPAIRS (the conclusion is true and in fact holds *without* the ℓ₀ hypothesis; the T1 mechanism and the "not covered" leftover are mis-stated — D6, D7)
Step-by-step re-derivation of the author's proof:
* (1) d_k(ℓ₀^{N}; ψ…) = binom(N + k − 1, k − 1) when all ψ(ℓ₀) = 1 ✓ (d₀ := 1 as in Prop 2.3).
* (2) λ_π(ℓ^N) = h_N(α₁, …, α_m) for unramified unitary π (Shintani/Casselman–Shalika) ✓; h_N = Σ_j P_j(N)α_j^N with
  deg P_j = (multiplicity of α_j) − 1; in a = N/2 the bases are α_j² ✓. α_j ≠ 0 ✓.
* (3) linear independence of a^r β^a ✓; top-degree induction gives C_k = 0 (k ≥ 2) ✓. Under G′ (1 at most a simple
  squared parameter) the base-1 coefficient is constant, so only K = C₀ + C₁ survives ✓. The Ad(σ) translation:
  squared parameters {α⁴, 1, α⁻⁴}; α⁴ ≠ 1 ⟺ a = α + α⁻¹ ∉ {0, ±2} ✓ (twisting by a quadratic ψ′ does not change squares ✓).
* (4)–(5) mean of C over primes ℓ ≡ 1 (L) is o(1): orthogonality of characters mod L + PNT for the cuspidal π_i ⊗ ψ̄
  (m_i ≥ 2) ✓ (input: Jacquet–Shalika non-vanishing on Re s = 1 *plus* the standard Rankin–Selberg/Tauberian step and a
  bound |α| < ℓ^{1/2} to discard prime powers — "relative to JS" is the usual shorthand; cite e.g. Iwaniec–Kowalski Thm 5.13,
  MINOR D8). N₋(p) ≥ ω₃(p + 1) for p ≡ 1 (4): the word (1, q + 1, (p + 1)/q + 1) has n = q·(p+1)/q − 1 = p, A = q,
  χ = (−q/p) = (p/q) = (−1/q) = −1 ✓; distinct q give distinct words ✓. Divergence of the mean: Dirichlet in finitely many
  progressions, letting the set of q grow (BV not needed, as the memo itself concedes) ✓. N₋ ≥ 0 lets one pass from
  p ≡ 1 (lcm(4, L)) to p ≡ 1 (L) ✓.
* Numerics (`scripts/review_r214_census.c`, from scratch): N₋(p) ≥ ω₃(p + 1) at every prime p ≡ 1 (4) < 10⁶ (0
  failures); mean N₋ over p ≡ 1 (8) is 38.75 (X = 10⁴), 91.96 (X = 10⁶) — matches the memo's 38.8 / 92.0.

**The real mechanism (D6, MAJOR — steering).** On primes ℓ ≡ 1 (L), ℓ ∤ L, *every* term of E is constant:
d_k(ℓ; ψ₁, …, ψ_k) = Σ_j ψ_j(ℓ) = k. Hence E(ℓ) = Σ_{k,i} k·c_{k,i} + (d₀-part) =: K′ for all such ℓ, with no T1 and no
ℓ₀ hypothesis. If N₋ = E + C, then the mean of N₋ over primes ℓ ≡ 1 (L), ℓ ≤ X, is K′ + o(1) by step (4), contradicting
step (5). So **Prop G′ holds unconditionally (relative to the same PNT input), for every finite family {π_i} on any GL(m_i ≥ 2)
and any characters** — the exponential-polynomial/T1 analysis at ℓ₀^{2a} (steps (1)–(3)) and the genericity hypothesis
are superfluous for the conclusion "≠ N₋". The killer is *size at primes* (exactly O205's own remark under Thm 2.2: "the
mechanism is size, not T1"), not T1. Consequences: the memo title ("T1 also kills GL(3) … cuspidal additions"), the
TWO_FIBRES §0 (I4)/§4 phrasing, the AGENT_REPORT SHARP 2 and the README row ("under a common one-prime genericity
hypothesis") mis-attribute the mechanism and understate the result; the "Not covered" list (families with no common ℓ₀)
is in fact covered. What steps (1)–(3) *do* prove is a different, T1-specific fact: under the ℓ₀ hypothesis, any
E + C vanishing on odd squares has E ≡ K on the semigroup S_L — keep it as a lemma if wanted, but it is not what kills the
identity. (Same remark applies to O205 Prop 2.3's "In particular E ≠ N₋", which also follows from E(ℓ) = const on
primes ≡ 1 (L) plus divergence of the mean of N₋ over those primes; flag to the O205 owner, not a defect of O209.)

**The ℓ₀ hypothesis is not satisfiable in general (D7, MAJOR as a statement about scope).** The memo says "we do not know
whether cuspidal such π exist". They do, inside the very class G′ advertises (self-dual orthogonal GL(3)): let σ be a
tetrahedral weight-one newform (projective image A₄; modular by Langlands–Tunnell) and Π = Ad(σ), cuspidal on GL(3) by
Gelbart–Jacquet (σ not dihedral). Let K₃ be the cyclic cubic field fixed by V₄ ⊲ A₄ and take L divisible by its conductor
(the identity may contain characters of that conductor). For every unramified ℓ ≡ 1 (L), Frob_ℓ is trivial on K₃, so its
projective image lies in V₄ and Ad(σ)(Frob_ℓ) has eigenvalues {1, 1, 1} or {1, −1, −1}: **1 is a triple squared parameter
at every admissible ℓ₀**, and the G′ argument at ℓ₀^{2a} gives nothing (a degree-2 polynomial in a can absorb rank ≤ 3
Eisenstein terms). Similarly D₄-type dihedral weight-one GL(2) forms (ring-class character of order 4, L divisible by the
genus-field conductor) have squared parameters {1, 1} at every ℓ ≡ 1 (L). So, as stated, G′ does **not** cover all
self-dual orthogonal GL(3) π; with the D6 argument it covers them all anyway.
*Suggested repair:* replace Props G/G′ by "Prop G″ (PROVED rel. PNT for GL(m) cusp forms): no finite combination E + C
equals N₋, because on primes ℓ ≡ 1 (L) E is constant, C has mean o(1), and N₋ has divergent mean (ω₃ bound)"; demote the
ℓ₀ analysis to a remark about S_L; change the memo title/steering reading to "size at primes kills it; T1 is not used";
delete the "Not covered (no common ℓ₀)" item; keep "not covered: infinite sums, shifted/derivative/non-standard
normalisations, growing level, non-automorphic objects".

### EVIDENCE items (§3.2, §3.4, R2) — reproduced exactly; one description overstated (D9)
From-scratch census (`scripts/review_r214_census.c`, words enumerated by t and divisor pairs A·A* = tp + 1 with
A ≡ A* ≡ −1 (t), χ = (−A/p); checks χ(t, u, v) = χ(t, v, u) on every word), **full range p < 10⁶** (90 s):
* primes p ≡ 1 (4), 5 < p < 10⁶: **39 174; N₋ < N₊ at 2 402** — exactly the author's numbers. Spot values 2521 (4, 33),
  9601 (8, 45), 1249 (10, 43), 3361 (8, 39), 70 249 (20, 85), 297 049 (24, 125), 871 249 (46, 185) all reproduced; N₊(5) = 5,
  Σ_w r(T_w, I₃)/48 = 6 at p = 5 and r(T_{(7,1,1)}, I₃) = 96 reproduced (§3.3 repair confirmed).
* N₋(p) mod 8 for p ≡ 1 (8): 4896/4805/4835/5016; p ≡ 5 (8): 4780/5021/4873/4949 — identical to R2. (χ² = 5.4 resp. 6.5
  on 3 d.o.f., p ≈ 0.15 / 0.09: "equidistributed" is a fair EVIDENCE description.)
* Σ N₋/Σ N₊ per p mod 8 = 1.547, 2.246, 2.123, 5.424 — matches §3.4. Mean N₋ over p ≡ 1 (8) = 91.96 at 10⁶ ✓.
* Parity R1: N₋(p) ≡ [p ≡ 3 (4)] (mod 2) at every prime 3 ≤ p < 10⁶ (0 failures).
* **"The worst all near squares" (D9):** the 13 primes < 10⁶ with N₊ ≥ 4N₋ are 1249, 2521, 3049, 3361, 9601, 13 249,
  29 401, 70 249, 225 289, 297 049, 361 321, 871 249, 925 369. Several are *not* archimedeanly near a square:
  29 401 = 171² + 160 (gap to 172² is 183), 225 289 = 474² + 613 (gap 336), 871 249 = 933² + 760 (gap 1 107) — the last is
  even quoted in §3.2 as "just above a square". What all 13 share is arithmetic: **p ≡ 1 (24) and (p/5) = +1** (and
  mostly (p/7) = +1), i.e. p is a quadratic residue modulo the small moduli the short words see — which is the (J)27
  reading, not "near m²". Several are values of other small forms (29 401 = 6·70² + 1, 871 249 = 2·660² + 7²).

### G1–G3 (y1_gamma8_trace) — SOUND (G3 is a tautology, D10)
* G1: from-scratch (`scripts/review_r214_small_facts.py`, letters < 48, M_w recomputed and checked = [[n, −A*], [A, −t]]):
  mod 4: 30 keys / 6 480 clashes; mod 8: 236 keys / 0 clashes; mod 16: 1 880 / 0 — matches. The proof rests on CHI_FLIP
  Cor 1.2 (χ a cell function mod 8, previously reviewed) + this finite check; "PROVED (finite cell check)" is fair.
* G2: (1, 3, 3) n = 3 χ = +1 and (3, 3, 1) n = 5 χ = −1, conjugate by cyclic rotation ✓ — but both have **trace 2, i.e.
  are parabolic**, not hyperbolic (MINOR: pick a hyperbolic pair for the "hyperbolic classes" story; the 88 pairs presumably
  contain some).
* G3: χ(w) = (−1/n)·Π_ℓ (A/ℓ)^{v_ℓ(n)} is just multiplicativity of the Jacobi symbol (−A/n); calling (A/ℓ) a genus
  character of T_w is correct (T_w represents A, ℓ ∤ A). PROVED but content-free; fine as a dictionary.
* B3 bound: #{(a, b, c) : abc − a − b − c = T} ≪ T^{1/3+ε} via (ab − 1)(ac − 1) = aT + a² + 1 ✓. **TWO_FIBRES §4 still says
  "T^{−1+o(1)} fraction"** while the Summary/memo carry the R209 repair T^{−2/3+ε} (D11).

### K1 (y1_heegner_level_t) — SOUND (elementary)
4 − 4tu ≡ 2² (mod 4t) ✓; [t, 2, u] has discriminant −4A ✓; τ = (−1 + i√A)/t ✓; (DD* − 16)/(4t) = 4(AA* − 1)/t = 4n ✓;
(−A/p) = (−A*/p) since AA* ≡ 1 (p) ✓. The local-height reading is correctly labelled Assessment, imprimitive caveat
((2, 2, 3): [2, 2, 2]) correct. Collision numerics re-done from scratch: 2 212 primes p ≡ 1 (24) < 2·10⁵, max least
t = 11 (at p = 14 281) ✓.

### R1, R3 (y1_reciprocal_parity) — R1 SOUND; R3 GAP in label (D12)
R1: u = v ⇒ n = u(tu − 2) ⇒ u ∈ {1, p} ⇒ (p + 2, 1, 1) or (p = 3) (1, 3, 3) ✓; χ(t, u, v)χ(t, v, u) = (AA*/n) =
((tn + 1)/n) = 1 ✓; parity verified to 10⁶ (above). (p + 2, 1, 1) trace = (p + 2) − (p + 4) = −2 ✓ parabolic.
R3 ("rotation changes n except on a thin set, and rotation flips χ on whole cells, so it does not act on X_p with a fixed
sign") is imprecise and its reason is off target. Precisely: the rotation (t, u, v) ↦ (u, v, t) changes n by u − t, so it
preserves n iff u = t, and then (t, t, v) ↦ (t, v, t) **is the reversal** of R1 (likewise (t, u, v) ↦ (v, t, u) needs v = t and
gives (t, u, t) ↦ (t, t, u), again the reversal). So on X_p the rotation is not a new symmetry and *preserves* χ there; the
"flips χ on cells" remark concerns n-changing rotations and is irrelevant to X_p. Suggested repair: state R3 as this one-line
fact (PROVED, trivial) or drop it.

### Cerednik–Drinfeld reading (y1_cerednik_swap, TWO_FIBRES §1 "Reading") — Assessment label correct; internal count inconsistency (D13)
The memo says the χ = +1 side has "≈ (p + 1)/12 edges = P¹(𝔽_p)/A₄", while Prop A2 (and my count) give ≈ (p + 1)/24
classes = image of P¹/S₄, with further identifications (D5). Both can be right only with different meanings of "edge"
(oriented/unoriented, Γ_p vs its normaliser, w_p) — the R209 caveat says this is not pinned down; the two documents should
at least not state different numbers without saying so. F3 masses: (p − 1)/4 and (p + 1)/12 (units mod ±1) ✓, ratio → 3 ✓.

### Novelty and labels
No external novelty is claimed, correctly: (i) ⟺ (iii) of Thm A is the classical fact that a positive binary form is
represented by the one-class genus of x² + y² + z² iff it is represented locally everywhere (Gauss, *Disq.* art. 288–292;
Mordell 1930; Ko 1937; Siegel), specialised to T_w; Thm B and Prop A2 are standard one-class-genus/maximal-lattice
arguments (A2 = Eichler orders of level p in the Hurwitz order ↔ P¹(𝔽_p) mod units, as in LPS/Brandt-matrix literature).
The quaternion-order proof is a valid re-proof. Labels: Thm A, B, A1, A2, K1, R1 PROVED ✓; A2 counts CERTIFIED ✓ (list
incomplete, D5); sign-dominance refutation is an exact finite computation and could be labelled CERTIFIED rather than
EVIDENCE; G′ "rel. JS + BV" — BV unnecessary (memo concedes), JS shorthand acceptable (D8); R3 over-labelled (D12);
Cerednik–Drinfeld reading Assessment ✓.

## Numbered defects
* **D6 (MAJOR, steering/scope) — Props G/G′, memo y1_gl3_cuspidal (title, Prop G, Prop G′, "Not covered"), TWO_FIBRES
  Summary bullet "Proposition G′", §0 (I4), §4 last bullet, AGENT_REPORT SHARP 2, README y1 row.** The ℓ₀ hypothesis and the
  T1 exponential-polynomial analysis are not needed: on primes ℓ ≡ 1 (L), every d_k(ℓ; ψ…) = k, so E is constant there; C has
  mean o(1) (PNT for π_i ⊗ ψ); N₋ has divergent mean (ω₃). Hence no finite E + C equals N₋, unconditionally (rel. PNT for
  GL(m)). The killer is size at primes, not T1. *Repair:* restate as Prop G″ (unconditional) with this 5-line proof; demote
  the ℓ₀/T1 analysis to a remark on S_L; fix the steering text ("size kills it; T1 unused"); delete the "no common ℓ₀" leftover.
* **D7 (MAJOR, false scope statement) — memo "Not covered … we do not know whether cuspidal such π exist"; Summary
  "including the self-dual orthogonal (Sym²/Ad) class".** Under the hypothesis as stated, Ad(σ) for tetrahedral weight-one σ
  (cuspidal on GL(3), self-dual orthogonal) with L divisible by the conductor of the cyclic cubic subfield has 1 as a triple
  squared Satake parameter at *every* ℓ ≡ 1 (L); D₄-type dihedral GL(2) forms likewise. So G′ as written does not cover the
  whole orthogonal class. *Repair:* subsumed by D6 (the unconditional argument covers them); if the ℓ₀ version is kept, record
  these examples.
* **D5 (MINOR) — TWO_FIBRES Prop A2 CERTIFIED line, memo H4, AGENT_REPORT CERTIFIED line, §5 table.** Only p ≡ 1 (4) were
  tested; #classes < #orbits already at p = 71 and 79 (also 107, 109, 113, 127). *Repair:* "for all primes 5 ≤ p ≤ 127 the
  map is onto; injective except at p = 71, 79, 107, 109, 113, 127 (R214)".
* **D9 (MINOR) — TWO_FIBRES §3.2 and Summary "the worst all near squares"; "871 249 … just above a square".** False as an
  archimedean statement (29 401, 225 289, 871 249 are mid-gap). *Repair:* "the worst cases are p ≡ 1 (24) with (p/5) = +1
  (mostly also (p/7) = +1): p is a square modulo the small moduli the short words see ((J)27); several are also m² + 24 or
  m² − 3".
* **D11 (MINOR) — TWO_FIBRES §4 B3/B6 bullet.** Stale "T^{−1+o(1)}"; should be T^{−2/3+ε} (R209 repair in memo/Summary).
* **D13 (MINOR) — y1_cerednik_swap C1 "≈ (p + 1)/12 edges = P¹/A₄" vs Prop A2 "≈ (p + 1)/24, image of P¹/S₄".** State which
  object each counts (oriented edges of Γ_p\𝒯_p vs conjugacy classes of Eichler orders vs lattice classes) or drop the number.
* **D12 (MINOR) — y1_reciprocal_parity R3.** Imprecise "PROVED"; on X_p the n-preserving rotation is the reversal and
  preserves χ. *Repair:* state the one-line fact or drop.
* **D10 (MINOR) — y1_gamma8_trace G2/G3.** G2's example pair has trace 2 (parabolic) in a section about hyperbolic classes;
  G3 is multiplicativity of the Jacobi symbol. *Repair:* give a hyperbolic pair; call G3 a reformulation.
* **D3 (MINOR) — Thm B proof, H2.** "maximal classical integral lattice … (O'Meara §91)": O'Meara's maximal lattices are
  norm-maximal; add "ℤ³ is norm-maximal in I₃ ⊗ ℚ, so gen(maximal) = gen(I₃)". Same in Prop A2.
* **D2 (MINOR) — TWO_FIBRES §1 / memo Literature.** Say explicitly that (i) ⟺ (iii) is the classical local–global principle
  for binary forms represented by the one-class genus I₃ (Gauss/Mordell/Ko/Siegel) — the novelty is only the word-level packaging.
* **D1 (MINOR) — Thm A(iii) congruence.** "x × y ≡ x + y" holds for a suitably *oriented* lift (an improper signed permutation
  turns it into x × y ≡ −(x + y)); add "after composing with a reflection if necessary". Checked for all 2 088 lifting words
  n ≤ 451 (author: n ≤ 151).
* **D4 (MINOR) — Cor A1.** Cite where ES-five(p) ⟺ N₋(p) ≥ 1 is proved.
* **D8 (MINOR) — memo G proofs.** "PNT for cuspidal L(s, π ⊗ ψ), i.e. Jacquet–Shalika": add the Rankin–Selberg/Tauberian
  step and the bound |α_j(ℓ)| < ℓ^{1/2} needed to pass from Λ-weighted sums to primes (cite e.g. Iwaniec–Kowalski Thm 5.13);
  drop BV from the label.

No FATAL defects. All PROVED core claims (Thm A, Thm B, A1, A2, K1, R1) survive re-derivation and from-scratch brute force.
