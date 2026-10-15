# R234 — hostile review of O233 (GLOBAL_FANO.md, BRAINSTORM/z9_*.md)

Reviewer: R234 side agent. Status: round 1 complete. No FATAL; 1 MAJOR (attribution, D2); 11 MINOR.

## Summary verdicts
See the table after C9.

## Claim-by-claim

### C1. Thm 1.1 / z9_frobenius_layers Lemma 1 (loops = representations of 2; r_L(m) for m < p/4)
Re-derivation (reviewer, independent):
* Trace-zero step. O = End E maximal in B_{p,∞}; P = {x ∈ O : p | nrd x} is the unique two-sided prime over p, and x̄ = trd x − x ∈ P
  for x ∈ P, so trd x ∈ P ∩ ℤ = pℤ. With nrd x = mp, |trd x| ≤ 2√(mp) < p ⟺ m < p/4. So all such x lie in E⁰ and CONSTRUCTIVE_ES
  Prop 3.1 gives r_L(m) = #{x ∈ End(E, C) : nrd x = mp}. Correct.
* (r_L(2) > 0 ⟹ loop.) ε ∈ End(E, C), ε² = −2p (needs 2 < p/4, i.e. p ≥ 11 among p ≡ 1 (4): p ≥ 13). ε(C) ∈ {0, C}; ε(C) = C is
  impossible because ε² = −2p kills E[2]. deg ε = 2p and E[p] = 0, so the inseparable degree is exactly p; writing ε = σ∘π_p
  (σ separable of degree 2), ker ε(𝔽̄_p) has order 2 and contains C, so equals C; hence ε = θ∘φ_C with θ: E/C → E of degree p and
  trivial point kernel, so θ = (iso)∘Frobenius and E ≅ (E/C)^{(p)}, i.e. E/C ≅ E^{(p)} (j ∈ 𝔽_{p²}). Correct.
* (loop ⟹ r_L(2) > 0.) E/C ≅ E^{(p)}: ε = ι∘π∘φ_C kills C, degree 2p, trace 0 by the step above. E/C ≅ E with j ∉ 𝔽_p: φ_C gives
  a degree-2 endomorphism, disc ∈ {−4, −7, −8}, all class number 1 and maximal, so by Deuring lifting j ∈ {1728, −3375, 8000} ⊂ 𝔽_p;
  contradiction. Correct. (Loop-ness is w₂-invariant, so it is a property of the class in 𝔊⁻_p, as needed.)
* Side claim "edges representing both 1 and 2 are ⟨1⟩ ⊥ [[2, 1], [1, (p+1)/2]] = word (1, (p+3)/2, 3)": re-derived — a norm-1
  vector splits, L = ⟨1⟩ ⊥ M; a norm-2 vector is either (±1, m) with Q(m) = 1, giving ⟨1, 1, p⟩ (isotropic at p for p ≡ 1 (4),
  so not in 𝔊⁻_p), or lies in M, giving M ≅ [[2, 1], [1, (p+1)/2]]; this class is in 𝔊⁻_p iff (−2/p) = −1 iff p ≡ 5 (8).
  So the "79" is just the number of primes p ≡ 5 (8) in [5, 2000] (see recount below). Correct.

From-scratch recertification (`scripts/review_r234_lib.py`, `review_r234_loops.py`, `review_r234_quat.py`; no z9/ce code):
classes of det p enumerated from Minkowski-type reduced Grams and canonicalised by successive-minima bases; 𝔊⁻_p selected by the
p-adic test (−d/p) = −1 on the binary quotient of L/pL; class counts reproduce 4, 7, 9, 15, 69 at p = 37, 73, 97, 193, 1009.
Loop test on the lattice side = isometry of the two vertex overlattices L + ℤx/2 (maximal-order types = j up to Frob).

**C1 addendum (quaternion side).** `scripts/review_r234_quat.py 200 55`: for every class of 𝔊⁻_p, p ≡ 1 (4), p ≤ 200, the Eichler order
E(L) was built from scratch (even Clifford algebra with reversal as standard involution; unique index-2 overorder found among the
15 candidates, uniqueness asserted) and all x ∈ E(L) with nrd x = mp enumerated: **for all 1 ≤ m < p/4: #{x : nrd x = mp} = r_L(m)
and every such x has trace 0 — 6471 (L, m) checks, 0 failures**; for m ≥ p/4, 275 (L, m) pairs have elements of nonzero trace, so the
bound m < p/4 is the operative one (the memo's Verschiebung remark is consistent).

### C2. Thm 2.1 / z9_depth_walks Lemma 1, Cor 2, Prop 3 (depth = conic-marked walk)
Re-derivation (reviewer):
* Vertex step. F = F_j has Q integral, B half-integral, det_B F = p/4, so b = 2B mod 2 on F/2F is alternating of rank 2 with
  radical r, and q(r) = 1 (q is nondegenerate because F is maximal at 2; numerically: exactly 3 classical index-2 sublattices at every vertex visited). A hyperplane H ⊂ F/2F is classical (B|H integral) ⟺
  b|H = 0 ⟺ r ∈ H (if r ∉ H, b|H is the nondegenerate quotient form). The 3 hyperplanes through r are {0, r, c, c + r} with
  q(c + r) = q(c) + 1, so each contains exactly one of the 3 conic points: hyperplanes ⟷ conic points. Hence "unique classical
  index-2 sublattice through z′" holds iff z̄′ ≠ r; the conic marking (q(z̄′) = 0) is one sufficient way to exclude r.
* Reviewer addition: for a *primitive* x with 4 | Q(x), x/2 is **never** ≡ r in F₁/2F₁ (r ≡ x/2 would force B(x, L) ⊂ 2ℤ, i.e.
  x ∈ 2L at 2, contradicting primitivity). So **without the marking every pointer has a unique continuation** — confirmed
  numerically: all 720 depth-2 pointers (p ≤ 200) have exactly one unmarked classical continuation through x/2. This strengthens
  the author's repair (the unmarked walk never stops at the first vertex, so the marking is not merely "needed in one example",
  it is the whole content of the step count).
* Step count: edge→vertex from L_j needs k − 2j + 2 ≥ 2, vertex→edge from F_j needs k − 2j ≥ 1; ⌊k/2⌋ + ⌊(k−1)/2⌋ = k − 1. Correct.
  Non-backtracking and primitivity arguments are correct (odd-prime primitivity is unaffected by 2-power index changes).
* Cor 2: k ≥ 3 ⟺ 8 | Q(x) ⟺ marked walk ≥ 2 half-steps — a restatement (near-tautological once Lemma 1 is in place); its content
  is the reading "two distinct edges at F₁ = non-backtracking 2-path = cyclic 4-isogeny", which is correct. Wording "a point of
  X₀(4)" is fine as a datum of G_p (Deuring), not a CM statement.
* Prop 3 (i)–(iii): correct as stated (v₂A + v₂A* = v₂(AA*) = v₂(tp + 1); f, f* are the two distinct even classes of FOUR_ADIC
  Lemma 1.1, so if both are isotropic they are the two isotropic classes and point at different overlattices; total s − 2).
  Examples re-checked by hand: 293 = 3·37·3 − 40 (A = 110, A* = 8, split (1,3) ∈ S₈); 293 = 3·7·15 − 22 (A = 20, A* = 44, split
  (2,2) ∉ S₈); 97: (2, 7, 8) ∈ S₈ (8 | v), (2, 20, 3) ∉ S₈; 131: s(t) = 2, 1, 4, 1, 2, 1, 3 for t = 1, 3, …, 13; (5, 1, 33): A = 4,
  A* = 164 = 4·41. All correct. Labels PROVED are justified (elementary).

From-scratch certification (`scripts/review_r234_depth.py`; own HNF/sublattice code; asserts: z primitive in L_j, det(F_j) = p/4,
det(L_{j+1}) = p, exactly 3 classical index-2 sublattices of F_j, exactly one through z′, no backtracking): **all 1190 pentagon
pointers of all χ = −1 words, odd primes 5 ≤ p ≤ 200, 0 violations, walk length = k − 1** (1196 including p = 3; 368 for p ≡ 1 (4)).
The author's "1190" is over all odd primes 5..200, not only p ≡ 1 (4) — say so (MINOR, D-list).

**Verdict C2: SOUND** (with the MINOR wording items below).

### C3. §3 / z9_brandt_screen: L1 (PROVED, narrow), L2/L3 placements
Re-derivation of L1 (reviewer). T_ℓ (ℓ ∤ 2p) acts on functions on X₀(2)^{ss}(𝔽̄_p) as the ℓ-isogeny adjacency; it commutes with Frob and
w₂, so it acts on ⟨Frob, w₂⟩-invariant functions = ℂ[𝔊⁻_p]. The Brandt self-adjointness weights 1/e(E, C) (e = |End(E,C)^×/±1|)
descend to w(L) = |orbit|/e = 4/(|Stab|·e). With Aut L = ±1 × SO(L), SO(L) ≅ N(E)/ℚ^× (Skolem–Noether) and
[N(E) : ℚ^×E^×] = |Stab_{⟨Frob,w₂⟩}| (Atkin–Lehner elements of norm 2 and p), |Aut L| = 2e|Stab|, so w(L) = 8/|Aut L| — **the mass
weights are indeed the right inner product**; the author's one-line proof silently uses this identification (MINOR: state it).
Simplicity of the eigenvalue ℓ + 1: connectedness of the ℓ-isogeny graph on X₀(2)^{ss} (strong approximation) + Perron–Frobenius,
or Ramanujan–Petersson for the cuspidal part (|a_ℓ| ≤ 2√ℓ < ℓ + 1). **But only for ℓ ∤ 2p**: the memo says "one ℓ ≠ p … true for
every ℓ"; at ℓ = 2 the operator on 𝔊⁻_p is not the standard T_ℓ (level 2 sits at 2) — MINOR, restrict to ℓ ∤ 2p.
The orbit-counting identity Σ_L #(ordered path bases)/|Aut L| = #{χ = −1 words} is correct (Aut L acts freely on ordered bases;
the Gram determines (t, u, v); reversal counted as a separate word).
L2: Siegel's Hauptsatz for representations of a rank-2 form by a rank-3 genus (m = n + 1) carries Siegel's factor ε = 1/2;
"Σ r_L(M)/|Aut L| = mass · ∏ α_v(M)" omits it (MINOR; positivity, the only thing used, is unaffected). The local condition
"−p v⁻¹ ≡ □ (mod tv − 1)" re-derived: adj M = [[t, 1], [1, v]] ≡ v⁻¹(x + vy)² (mod tv − 1), so the glue norm −p must be v⁻¹·□;
this is only the odd part of the local condition (2- and p-adic conditions are not written) — MINOR. L3: Schiemann, Math. Ann.
308 (1997) 507–517 does state that positive definite ternary integral forms are determined by their theta series (citation
correct); placement is a correct Assessment.
**Verdict C3: SOUND-AFTER-REPAIRS (minor): L1 PROVED as narrowed, with ℓ ∤ 2p and the weight identification made explicit; L2/L3
are placements (Assessment), correctly labelled in GLOBAL_FANO §3 table ("PROVED placement" for L2 should read "placement of a
PROVED local criterion", MINOR).**
**Result: all 9489 edge classes of all p ≡ 1 (4), 5 ≤ p ≤ 2000: loop ⟺ r_L(2) > 0 with 0 mismatches; 1191 loops; 1573 path
classes, 449 of them loops; 79 classes representing both 1 and 2, all path classes** — every number reproduces the author's
exactly (incl. p = 5, 13 below the p ≥ 11 hypothesis). (Runtime 126 s.) The trace-zero/representation identity
r_L(m) = #{x ∈ E(L) : nrd x = mp} (all x, any trace) is checked separately with an independently built Eichler order (even Clifford
algebra C₀(L), its unique index-2 overorder found by brute force over the 15 candidates): see the C1 addendum below.

Enrichment statistic (spot-check): from the author's data file the pooled shares are 449/1573 = 28.5 % vs 1191/9489 = 12.6 %
(p ≤ 2000, reproduced independently above), 26.7 % vs 10.2 % (p ≤ 3000), 22.6 % vs 5.8 % (p ≤ 10⁴). The "4×" is the ≤ 10⁴ pooled
ratio of *shares*; it is dominated by small primes (pooling weights primes by their class counts) and drifts with the range
(2.3× at 2000, 2.6× at 3000, 3.9× at 10⁴) — MINOR: state it as range-dependent and pooled.

Novelty: the core implication "d-isogeny E → E^{(p)} ⟺ trace-zero μ ∈ End E with μ² = −dp, via p | trace and |trace| ≤ 2√(dp)"
is **Chenu–Smith, "Higher-degree supersingular group actions" (MathCrypt 2021 / HAL hal-03288075), Prop. 1–2** (verified in
the PDF: μ = π_p∘ψ, P_μ = T² − rdT + dp, p | r and |r| ≤ 2√(p/d) ⟹ r = 0); the count of such curves via Cl(ℤ[√−dp]) is their
Thm 2 (so "layer m is class-number sized ≍ h(−4mp)" is known for squarefree m). Arpin et al. ("Adventures in Supersingularland",
arXiv 1909.07779 §5) study 2-isogenous conjugate pairs = loops of G₂/Frob empirically. New in O233: only the level-2 (edge)
packaging through the Gross-type lattice L = (E⁰)^#(p) and the loop ⟺ "L represents 2" phrasing. The memo's "standard type of
statement … not found in the campaign" undersells the attribution — MAJOR (attribution only), see D2.
**Verdict C1: SOUND** (mathematics and certification); attribution must be repaired (D2).

### C5. z9_order3_fano: TES χ₃ test (13 failure primes N ≤ 787; c_i = 2 radius; "bit failures")
Radius re-derived: from T = c_iπ/(uv) + c_j/u + c_k/v and |T| ≥ 1 (T ∈ O ∖ 0), with m = min(|u|, |v|): m² − (|c_j| + |c_k|)m −
|c_i||π| ≤ 0 and |c_j| + |c_k| ≤ 3, so m ≤ (3 + √(9 + 4|c_i||π|))/2 with **|c_i| = 2 when c_i = 2** — the repaired bound is correct.
χ₃ invariance: α depends only on the ratios u₁/u₃, u₂/u₃, which are unchanged by the common scaling x_m ↦ (T/9)x_m, so χ₃ of a
word equals the invariant a TES point built from it would carry; Thm 3.2(c) makes χ₃ = −⟨ω, 2⟩₂ necessary. Correct.
From-scratch re-run (`scripts/review_r234_tes.py`: own ℤ[ω] arithmetic, divisor enumeration by norms, tame symbol at π, cubic
character via r^{(N−1)/3}; no tf_core/tw_eis/z9 code), all 67 split primes 7 ≤ N ≤ 787:
* calibration: 35 Type II TES solutions found (at 28 primes), all with χ₃ = 2 (the target) ✓; 0 solutions at the 13 failure primes ✓
  (consistent with TES_FINITE Thm 2.1); 26 of the 54 solvable primes have no Type II solution ✓;
* P(v_λ(T) ≥ k | χ₃), k = 1..4: χ₃ = 2: 0.2564, 0.0615, 0.0132, 0.0030; χ₃ = 0: 0.2264, 0.0527, 0.0110, 0.0016 — identical to the
  author's to the printed digits; χ₃ = 1 and 2 have identical statistics ✓;
* target-χ₃ words at the 13 failures: **214–685** (author: 428–1370); λ⁴ | T target words at exactly 61, 79, 97, 151, 211, 367, 769 ✓
  (counts 3, 1, 1, 1, 2, 1, 1; author's 6, 2, 2, …). **The author's word counts are exactly 2× mine at every prime** (also the
  totals, e.g. N = 97: 2620 vs 1310): z9_tes_words counts each word twice (the equation c_iπ + c_jv + c_ku = Tuv with (j, k, u, v) and
  (k, j, v, u) is the same word). MINOR (D-list): halve the counts or define the counting convention; no conclusion changes.
Label check: "TES failures are bit failures" is shown only in one Type II slice (Type I words, which are 75 % of all TES
solutions per TES_FINITE, are not enumerated) and the "bit" reading is an analogy (the anchor condition "2-primary" is itself a
mod-2 trit on three denominators, not a 2-adic depth). The memo labels it correctly (EVIDENCE one slice + Assessment), but
GLOBAL_FANO §0 (I7) states it in bold as a conclusion ("So TES failures are **bit failures**") and the agent report lists it under
SHARP — MINOR overclaim, add "(in the Type II slice; Assessment)" there.
**Verdict C5: SOUND** as EVIDENCE (numbers reproduced exactly up to the 2× convention), reading = Assessment.

### C6. §5 control 105
Re-run (`scripts/review_r234_105.py`, own BFS over overlattices / classical index-2 sublattices): 105 has 11 words (ordered),
**none 2-adically isotropic**; the 2-neighbour component of ⟨1, 3, 35⟩ has 4 vertex classes, 4 edge classes, degrees 1, 2, 2, 3,
no path class. All as claimed. The weakened wording ("refutes forcing from graph existence alone") is the right scope.
Comment (not a defect): the 105 graph is a graph of the *wrong* genus for the words (all 11 words have χ = +1, i.e. live in
2-adically anisotropic genera with no 2-neighbour graph at all), so the control shows "words can avoid the graph's genus
entirely", which for primes is excluded by CHI_FLIP/SQ₅ only conjecturally. **Verdict C6: SOUND.**

### C4. §4 / z9_heegner_layers: forward algebra, level-t ring condition, necessity only
Forward algebra re-derived by hand: with trd i = trd j = 0, i² = −A*, j² = −A, ij + ji = −2: conj(ij) = ji, so
nrd(1 + ij) = 1 + (ij + ji) + i j² i = 1 − 2 + AA* = tp and trd(1 + ij) = 2 − 2 = 0, hence ε² = −tp; trd(εj̄) = trd(j + ij²) = 0;
(1 + ε)j = −ij·j = Ai, so i = (1 + ε)j/A; nrd i = (1 + tp)A/A² = A*. Also (reviewer) ij = −1 − ε, ji = −1 + ε, and the ring
condition is (1 − i)(1 − j) = −(i + j + ε) ∈ t·E. All PROVED; additionally verified in exact arithmetic inside independently built
E(L) (`scripts/review_r234_heegner.py`, assertions trd i = 0, nrd i = A*, ij + ji = −2, ε = −(1 + ij) on every witness found).
Deuring lifting of ((E, C), ε): C lifts uniquely (2 ≠ p, reduction is injective on E[2] and compatible with endomorphisms), so the
statement is fine; "p ramified in ℚ(√−tp)" needs p ∤ t (t ∈ {p, p + 1, p + 2} occur for boundary words) — MINOR.
(b) "≍ h(−4tp) up to bounded local factors at 2 and t": the non-optimal embeddings add Σ_{f² | 4tp} h(−4tp/f²), which is not
"bounded local factors" when t has a large square part — MINOR wording.

**Edge-wise test of the class condition without the ring condition (reviewer, new).** For every class L ∈ 𝔊⁻_p, p ≤ 110 (then 200),
t ≤ 5 (6): search ε, j ∈ E(L)⁰ with nrd ε = tp, j ⊥ ε, nrd j = A | tp + 1, A ≡ −1 (mod t), i = (1 + ε)j/A ∈ E(L).
p ≤ 110: 69 classes, 49 path classes; the condition holds at 44 classes, of which **3 are not path classes** (p = 61, 89, 101);
the ring condition holds at 41, never at a non-path class (consistent with Cor 2.2(iv) ⟹ (i)); every path class with letter t ≤ 5
is found. Explicit example: **p = 61, L = ⟨1⟩ ⊥ [[7, −3], [−3, 10]]** (not a path class), t = 4, A = 7, A* = 35 (the numbers of the
χ = −1 word (4, 2, 9), whose path class [[9, −1, 0], [−1, 4, −1], [0, −1, 2]] is a different class, canonical key (2, 4, 9, −1, 0, −1)):
ε, j, i all lie in E(L) but (1 − i)(1 − j) ∉ 4E(L). So the author's repaired reading (necessary, not sufficient) is not just
cautious but **necessary at the edge level**: the "ideal of norm A ≡ −1 (mod t) dividing tp + 1" condition is satisfied by
non-certificate edges. The author's own counterexample ((3, 1, 7), p = 13 with i, j ↦ −i, −j) is only a *data-level* failure on a
certificate edge (the edge is still a certificate via (i, j)), so it does not by itself show edge-wise insufficiency —
MINOR: replace/augment it with an edge-level example such as the one above.
(c) itself: given j ∈ E with nrd j = A, the binary lattice E ∩ (ℚ(ε))j trivially represents A, so "the class contains an ideal of
norm A" carries content only through the unproved identification of that binary lattice's class with the CM point's ideal class
in Cl(ℤ[√−tp]) (Gross–Zagier/Dorman-type, here for an Eichler order of level 2 and the ramified prime p | disc). Labelled
Assessment — correct; but GLOBAL_FANO §4 bolds it as the description of certificate edges. MINOR: say "(Assessment; the
class-group identification is not proved)".
**Verdict C4: SOUND-AFTER-REPAIRS (minor)**: forward algebra PROVED; converse correctly withdrawn; dictionary = Assessment.

**C4 addendum (reviewer lemma + primitive re-run).** All 5 non-path witnesses for p ≤ 200, t ≤ 6 (p = 61, 89, 101, 173 ×2) have
**t = 4 and ε = 2ε₁ imprimitive** (ε₁ a spine element of nrd p; all five classes are ⟨1⟩ ⊥ binary). Re-run requiring ε/2 ∉ E(L)
(`H.PRIM = True`): p ≤ 200, t ≤ 6: 174 classes, condition holds at 78, ring condition at the same 78, **0 non-path classes**.
This is explained by a short sign lemma (reviewer, PROVED): *let ℓ be an odd prime, E_ℓ ≅ M₂(ℤ_ℓ), i, j ∈ E⁰ with i² ≡ j² ≡ 1
(mod ℓ) and ij + ji = −2. Then (1 − i)(1 − j) ∈ ℓE_ℓ or (1 + i)(1 + j) ∈ ℓE_ℓ.* Proof: mod ℓ, ī ~ diag(1, −1);
j̄ = [[x, y], [z, −x]] with x² + yz = 1, and īj̄ + j̄ī = 2x = −2 gives x = −1, yz = 0; then (1 − ī)(1 − j̄) = [[0, 0], [−2z, 0]] and
(1 + ī)(1 + j̄) = [[0, 2y], [0, 0]]. ∎ Since (i, j) ↦ (−i, −j) preserves ε = −(1 + ij), ij + ji and all norms, **for t = 1 or t an odd
prime the class condition of (a) (with i, j ∈ End(E, C)) is also sufficient edge-wise** (then C₀(L_w) ⊂ E(L) has index 2, so
E(L) = E(L_w) and L ≅ L_w). The ring condition is a genuine extra condition only through (i) the 2-part of t, including imprimitive
ε (the t = 4 witnesses above), and (ii) incompatible sign choices at ≥ 2 distinct odd primes ℓ ∥ t (and prime powers ℓ^k, k ≥ 2,
not analysed). So the author's sign-flip example ((3, 1, 7), p = 13) shows nothing edge-wise — at t = 3 the edge-wise converse is
true — and the doc should state the converse as: TRUE for t = 1 and t odd prime (sign lemma), FALSE in general (t = 4, p = 61
above), open for primitive ε with composite t (see the t ≤ 15 re-run below).
Primitive re-run, p ≤ 110, t ≤ 15 (ε/2, ε/3 ∉ E(L) when 4 | t, 9 | t): 69 classes; condition at 54, ring condition at 48, **6
non-path classes satisfy the condition** — witnesses only at **t = 8, 12, 15** (p = 41: t = 8, A = 7 and t = 15, A = 14; p = 73, 89,
97: t = 8; p = 97: t = 15, A = 14; p = 109: t = 12, A = 11), never at t ∈ {1, 3, 5, 7, 11, 13} (sign lemma) nor at t = 9 in range.
t = 15 = 3·5 is exactly the predicted "two odd primes, incompatible signs" failure; 8 and 12 are 2-part failures. So the precise
edge-wise statement is: **converse TRUE for t ∈ {1} ∪ {odd primes}, FALSE for t = 4 (imprimitive), 8, 12, 15 (primitive)**; the
ring condition carries real information exactly through the 2-part of t and the CRT sign pattern over odd ℓ | t. This sharpens
z9_heegner_layers' repaired (a) — recommended as a repair (D6).
**Verdict C4 (final): SOUND-AFTER-REPAIRS (minor).**

### C8. z9_triangle_shapes (triangle decoupling, 47 of 329 primes ≤ 5000)
Determinant re-derived: det [[a, e, e], [e, b, e], [e, e, c]] = abc − a − b − c + 2e³ = abc − a − b − c ± 2; c(ab − 1) = p + a + b − 2e;
for e = −1, (ab − 1)(ac − 1) = a(p + a + b + 2) − (ab − 1) = ap + (a + 1)². Correct.
From-scratch run (`scripts/review_r234_triangle.py 5 5000`; enumeration a ≤ b ≤ c, own canonical forms and p-adic test): 329 primes;
327 with a χ = −1 triangle class; **47 decoupled primes, first 61, 181, 349, 421, 541** ✓; 312 primes with a χ = −1 triangle class
that is not a path class ✓. Two wording defects (MINOR, D12): (i) "the two exceptions (109, 229) have none at all" — false as
written: every p has the triangle (a, b, c, e) = (1, 2, p + 5, −1) ≅ ⟨1, 1, p⟩ (χ = +1); at 109 and 229 there are 2 resp. 4 triangle
classes, all χ = +1; they have no **χ = −1** triangle class. (ii) "At 312 some triangle class is not a path class" must say "some χ = −1
triangle class" — with any χ it holds at all 329 primes trivially (⟨1, 1, p⟩). The scope sentence in the Assessment is correct.
**Verdict C8: SOUND** (EVIDENCE; minor wording).

### C7. z9_pointer_parity ("no parity law": 47.6 % even P(p); odd vertices; both-end pointers at 17 primes)
From-scratch spot-check (`scripts/review_r234_pointers.py`, all 116 primes p ≡ 1 (4), p ≤ 1500): P(p), path loops, odd-degree vertices
of the path subgraph and "both-end" counts agree with `data/z9/stats_p1mod4_1e4.txt` **at every prime (0 mismatches)**; even P(p) at
56/116 = 48.3 %; no odd vertex only at 5, 13 in this range (2521 is beyond it; the author's data file shows it); both-end absent at
5, 13, 37, 193, 421, 577, 673, 1153, 1249, 1489 (= the author's list below 1500). The aggregate 47.6 % (290/609) is read off the data
file. EVIDENCE label is fine.
Definitional defect (MINOR, D11). The author's "pointer to both ends" uses the pointed **vertex classes**, so it is identically
impossible on loop path classes. Reviewer lemma (PROVED): *L ∈ 𝔊⁻_p is a loop ⟺ Aut(L) swaps the two isotropic classes of L/2L.*
(⇒: a trace-zero ε ∈ E(L) with nrd ε = 2p lies locally at 2 in w·E₂^× (w = [[0, 1], [2, 0]]: trace zero and v₂(nrd) = 1 force
ε = [[a, b], [2c, −a]] with a even, bc odd), at p in the maximal order of the division algebra, so ε normalises E(L), and conjugation
by ε is an isometry of L = (E⁰)^#(p) exchanging the two maximal overorders. ⇐: an automorphism exchanging the ends comes from a
normaliser element exchanging the two maximal orders, i.e. an isogeny E → E/C composed with an isomorphism E/C ≅ E or E^{(p)}.)
Numerically: Aut(L) swaps the ends exactly at the loop classes at all 116 primes. So "which end a pointer points at" is
well-defined **only for non-loop path classes**, and at 5, 13, 2521 (all path classes loops) the both-end statistic is vacuous;
among the 17 "absences" the loop share of path classes is 1/1, 2/2, 3/4, 4/5, 3/6, 4/9, 4/7, 8/11, 2/5, 4/8, 2/2, 10/15, 4/8, 0/4,
2/7, 2/8, 2/4 (author's data, p = 5 … 9601) — i.e. the statistic is partly, not wholly, a loop artefact (3361 is a genuine case). Repair: restrict the pointer
statistics to non-loop path classes and say so.
**Verdict C7: SOUND** as EVIDENCE for "no parity law" (the parity statistic is unaffected); the pointer statistic needs the scope fix.

### C9. Novelty (Deuring / Kaneko / Gross–Zagier-type facts)
* Thm 1.1: core known (Chenu–Smith Prop 1–2 and Thm 2; Arpin et al. §5 for the loop/conjugate-pair phenomenon; Kaneko 1989's
  "two embeddings ⟹ d₁d₂ ≥ 4p" is a related, not identical, mechanism — not checked against the paper, from memory). Edge-level packaging new. → D2.
* Prop 3.1-type "θ_L counts trace-zero elements of p-divisible norm": Gross 1987 §12 (Gross lattice) — already attributed in
  CONSTRUCTIVE_ES; fine.
* Depth walks: Bruhat–Tits / Eichler orders of level 2^k ⟷ non-backtracking paths (Serre, Trees) — cited; the conic-marking
  lemma is elementary and, as packaged, new to the campaign. Fine.
* Heegner dictionary: Deuring lifting, Gross–Zagier "On singular moduli" (reduction of CM points; there the ramified case p | D
  is not the main case), Elkies — cited as background; no claim of novelty beyond the campaign. The "ideal class contains an ideal
  of norm A" identification is *not* in those sources in this form and is unproved here (C4). Fine as Assessment.
* L1/L2/L3: standard (Brandt self-adjointness, Siegel, Schiemann), correctly presented as placements.

## Summary verdicts
| # | claim | verdict |
|---|---|---|
| C1 | Thm 1.1 / frobenius_layers Lemma 1: loops ⟺ L represents 2; r_L(m) = #{x ∈ End(E, C) : deg x = mp}, m < p/4, trace 0 | **SOUND** (recertified from scratch, 9489/9489 edges p ≤ 2000; 6471 quaternion checks p ≤ 200); attribution MAJOR (D2) |
| C1′ | 4× enrichment statistic | SOUND as EVIDENCE; range-dependent pooled ratio (D3) |
| C2 | Thm 2.1 / depth_walks Lemma 1, Cor 2, Prop 3(i)–(iii) | **SOUND** (1190/1190 pointers p ≤ 200, own code); marking is the whole content (strengthened) |
| C3 | L1 (narrow), L2/L3 placements | **SOUND-AFTER-REPAIRS** (minor: ℓ ∤ 2p, weights, Siegel ε, label wording) |
| C4 | Heegner dictionary: forward algebra; level-t ring condition; necessity only | **SOUND-AFTER-REPAIRS** (forward algebra PROVED; converse: TRUE for t ∈ {1, odd primes} by a sign lemma, FALSE at t = 4, 8, 12, 15 — author's example is not edge-level) |
| C5 | TES χ₃ test, radius, "bit failures" | **SOUND** as EVIDENCE (all rates reproduced exactly; counts doubled by the author's convention, D9); "bit failures" = Assessment, one slice (D10) |
| C6 | 105 control | **SOUND** |
| C7 | no parity law (47.6 % even, odd vertices, both-end pointers) | **SOUND** as EVIDENCE (116/116 primes ≤ 1500 identical); both-end statistic ill-defined on loops (D11) |
| C8 | triangle decoupling 47/329 | **SOUND** (exact reproduction); wording (D12) |
| C9 | novelty | see D2 |
No FATAL defects. No positive ES claim is made, and none is needed for the labels used.

## Defects
* **D1 (MINOR) depth_walks / GLOBAL_FANO §2:** "1190 pentagon pointers … p ≤ 200" are over all odd primes 5 ≤ p ≤ 200 (368 for
  p ≡ 1 (4)); say so. Add the reviewer remark: for primitive x, x/2 is never the radical, so without marking every pointer
  continues — the marking is the entire content of the step count. *Repair:* one sentence each.
* **D2 (MAJOR, attribution) frobenius_layers Lemma 1 / GLOBAL_FANO Thm 1.1 / AGENT_REPORT SHARP 1:** the d-isogeny-to-conjugate ⟺
  √−dp ∈ End E statement with the same trace argument is Chenu–Smith (Prop 1–2; counts via Cl(ℤ[√−dp]), Thm 2). *Repair:* label
  "PROVED; known in substance (Chenu–Smith 2021, Prop 2; Arpin et al. §5); new: the edge (level-2) form via L = (E⁰)^#(p)", and
  cite Chenu–Smith Thm 2 for "layer m ≍ h(−4mp)".
* **D3 (MINOR) frobenius_layers / AGENT_REPORT:** "4× enrichment" is the pooled ≤ 10⁴ share ratio (22.6/5.8); it is 2.3× at ≤ 2000
  and 2.6× at ≤ 3000. *Repair:* state pooled and range.
* **D4 (MINOR) brandt_screen L1:** restrict to ℓ ∤ 2p; state that the Brandt self-adjointness weights descend to 8/|Aut L|
  (|Aut L| = 2e·|Stab_{⟨Frob,w₂⟩}|), which is what makes the mass functional the right one.
* **D5 (MINOR) brandt_screen L2 / GLOBAL_FANO §3 table:** Siegel's formula for rank 2 in rank 3 carries ε = 1/2; the written local
  condition is only the odd part; "PROVED placement" → "placement of a PROVED local criterion (Assessment)".
* **D6 (MINOR) heegner_layers (a) / GLOBAL_FANO §4:** the (3, 1, 7)/p = 13 sign-flip example is not an edge-level counterexample
  (at odd prime t the edge-wise converse is TRUE by the sign lemma in C4). *Repair:* replace by: converse true for t ∈ {1} ∪
  {odd primes}; false in general (p = 61, L = ⟨1⟩ ⊥ [[7, −3], [−3, 10]], t = 4, A = 7, imprimitive ε; primitive failures at
  t = 8, 12, 15, e.g. p = 41, t = 15, A = 14).
* **D7 (MINOR) heegner_layers (b):** "p ramified in ℚ(√−tp)" needs p ∤ t; "bounded local factors" ignores the sum over
  conductors f² | 4tp.
* **D8 (MINOR) GLOBAL_FANO §4 bold sentence:** add "(Assessment: the identification with an ideal class of ℤ[√−tp] is not proved;
  given j the binary complement trivially represents A)".
* **D9 (MINOR) order3_fano numbers / AGENT_REPORT SHARP 2:** all word counts (428–1370, 2620 at N = 97, etc.) are 2× the number of
  distinct words (each word counted with (j, k, u, v) and (k, j, v, u)); rates unaffected. *Repair:* halve (214–685) or define
  the convention.
* **D10 (MINOR) GLOBAL_FANO §0 (I7), §5, AGENT_REPORT SHARP 2:** "TES failures are bit failures" stated as a conclusion; add "in
  the Type II slice (Type I = 75 % of TES solutions not enumerated); reading = Assessment".
* **D11 (MINOR) pointer_parity / GLOBAL_FANO (I1):** both-end pointers are undefined on loop classes (loop ⟺ Aut(L) swaps the
  ends, C7 lemma); restrict the statistic to non-loop path classes.
* **D12 (MINOR) triangle_shapes:** 109/229 have χ = +1 triangles (⟨1, 1, p⟩ always is one); "312 … some triangle class" must be
  "some χ = −1 triangle class".

## Reproduction (reviewer scripts, no author code imported)
`cd scripts; PYTHONPATH=. uv run --with sympy python <script>`:
`review_r234_loops.py 5 2000` (126 s) · `review_r234_quat.py 200 55` (≈ 40 min) · `review_r234_depth.py 200 0` · `review_r234_pointers.py`
(via `run(primes_1mod4(5, 1500))`) · `review_r234_triangle.py 5 5000` · `review_r234_105.py 105` · `review_r234_tes.py 787` ·
`review_r234_heegner.py` (`run(200, 6)`, with `PRIM = True`, and `run(110, 15)`). Library: `review_r234_lib.py`.
