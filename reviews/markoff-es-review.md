# R202 — hostile review of O202 (MARKOFF_ES.md)

Reviewer: R202 side agent. Document reviewed: MARKOFF_ES.md as merged from `side-agent/markoff-es` (checkpoint 1),
report reviews/agent-reports/AGENT_REPORT_O202.md. From-scratch scripts: `scripts/review_mk_*.py`.
Sources fetched for this review (arXiv full texts, pdftotext): `sources/r202/{1706.06712v3,1807.10223,1808.01584,2202.07142}.{pdf,txt}`.

**Repairs applied** (author silent ≥ 1 h after checkpoint report): M1, M2, m1, m2, m3, m4, m6, m7 inserted into
MARKOFF_ES.md marked "(R202 repair …)", plus an M1/m7 note in AGENT_REPORT_O202.md SHARP 1. Not applied (wording/
rigor only, left to author): m5, m8–m11.

## Summary verdicts

| Claim | Verdict |
|---|---|
| §1 literature (GS, LM, CTWX, Dao; Dao erratum) | SOUND (checked against full texts) |
| Prop 2.1 (smooth, one A₂ point, conic bundle, Vieta fix C) | SOUND |
| Prop 2.2 (Pic, Br₁ = (ℤ/2)², no transcendental part) | SOUND-AFTER-REPAIRS (m1 independence proof, m2 scope of (c): D non-square) |
| Lemma 3.1 (admissible D) | SOUND (0 mismatches, 1350 (n, D), independent ℓ-adic search) |
| Cor 3.2 (T1 fibrewise local) | SOUND |
| Prop 3.3 (family BM via (−1, D)) | SOUND-AFTER-REPAIRS (m3: W_∞ must contain D > 0, else false as written) |
| Prop 3.4 (no BM on admissible fibres) | SOUND-AFTER-REPAIRS (m4: "(∏W_v)^{Br} = ∏W_v" false; "≠ ∅" is what is proved) |
| Thm 4.1 (norm form) | SOUND (m5 wording) |
| Thm 4.2 (CF dictionary) | SOUND-AFTER-REPAIRS (m6: N non-square hypothesis; harmless). 0 misses / 0 extras, odd n ≤ 299 |
| Thm 4.3 formulas Q₁, Q₂, Q₃, (p₂, q₂); B = 1 ⟺ k = 3 for μ > 2n | SOUND (0 failures, odd n ≤ 299, 2n < μ ≤ 5n) |
| "ES's shot family is exactly depth 3" (title, §8.3, report SHARP 1) | **GAP — false as stated (M1)**: the j = 1 shots (A = 2, μ ≤ 2n) are at depth 1; "every B > 1 at depth ≥ 5" false (m7) |
| Thm 5.1 (no polynomial families) | SOUND (m8, m9 rigor) |
| §6 EVIDENCE | SOUND (3 cells, 2 spot checks, 1 depth reproduced exactly) |
| Prop 6.1 | Assessment label OK; m10, m11 overstatements |
| Prop 7.1 (a), (b) | SOUND (scope μ > 2n; add μ ≤ 2n after M1) |
| Prop 7.1 (c) + §7 Reading "composition does not reach ES" | **GAP (M2)**: labelled PROVED, not proved; composition does land exactly on ES points (n = 59, μ = 126, D = 63 = 3·3·7) |

No FATAL defects. Overall: the geometry/Brauer computations and the CF dictionary are correct and independently
reproduced; the two "sharp" structural slogans (ES = depth 3; composition never reaches ES) need re-scoping.

### Defect list
* **M1 (MAJOR)** §4 title, Thm 4.3 title/statement "B = 1 ⟺ k = 3" read as global, §7 Reading, §8 item 3, report
  SHARP 1: ES shot family = depth 1 (j = 1, A = 2) ∪ depth 3 (j ≥ 2). Repair text in the Thm 4.3 section below.
* **M2 (MAJOR)** Prop 7.1(c)/§7 Reading/§8: composition claim overclaimed; counterexample n = 59, μ = 126. Relabel
  Assessment and rephrase (text below).
* m1 Prop 2.2(b) independence via Prop 3.4 needs admissible D; use residues in ℚ(A, B).
* m2 Prop 2.2(c) needs D non-square (D = 1: (A, B) + (2, A) unramified along L).
* m3 Prop 3.3: W_∞ must include D > 0 (λAB > 1/2).
* m4 Prop 3.4: "=" → "≠ ∅".
* m5 Thm 4.1: bijection wording (points ↔ (x, z), x ∈ ℤ).
* m6 Thm 4.2: add "N non-square"; square-N points only occur for 3μ² ≤ 4n (proof in section below).
* m7 "every B > 1 solution at depth ≥ 5": the ι_B partners of ES points are at depth 3.
* m8, m9 Thm 5.1 rigor (non-square f argument; non-normal R).
* m10 Prop 6.1(a) "provable half-dimensional sieve statement" unsupported; m11 Prop 6.1(c) literature-negative claim.

## §1 Literature — SOUND

Checked against the arXiv full texts (sources/r202/).
* GS (1706.06712v3): Thm 1.1 (compact fundamental sets F_k^± for generic k), consequence (c) h_M(k) ≪ |k|^{1/3+ε},
  (1.6) Σ h^± ∼ C_± K (log K)², (1.7) numerics θ ≈ 0.8875 for 0 < k < 6·10⁸, Thm 1.2(i) ≥ √K (log K)^{−1/2},
  Thm 1.2(ii) almost perfect, Rem 1.3(d) method (small x₁, tentacles, [BG06]/[Nie10]), (1.8) with a_jj = ±1, and the
  "F₀ reducible ⇒ full, proofs in a forthcoming paper" remark: all stated as in the text. ✔
* LM (1807.10223): Thms 1.1–1.5 and the (log B)^{−1/4} → (log B)^{−1/2} correction of GS, (ℤ/2)³ for general m,
  Prop 2.4 (Br Ū ≅ ℚ/ℤ(−1) unless Eckardt; (Br Ū)^{G} = ℤ/2): as stated. IMRN 2021 no. 18, 14086–14122 ✔.
* CTWX (1808.01584): Thm 1.1 (non-density away from any finite S, by reduction theory only), Cor 1.2 (m ≠ 0, 4) ✔.
* Dao (2202.07142v4): author **Quang-Duc Dao** (arXiv metadata and title page), JNT 254 (2024) 65–102,
  doi 10.1016/j.jnt.2023.07.007. Thm 1.3: #{k ∈ ℤ⁴, |k_i| ≤ M : ∅ ≠ U(A_ℤ)^{Br₁} ≠ U(A_ℤ)} ≍ M⁴ — i.e. algebraic-BM
  explained failures of strong approximation, as O202 says ✔. The erratum for LITERATURE_AUTOMORPHIC.md l. 408
  ("Qian Dong Dao") is correct.
* Nuance (no defect): "fullness is trivial" is even stronger than stated — the point (1, 1, D + n + 1) lies on the
  Pell conic of the fibre C = D + n + 1, which is infinite unless (D + n + 1)² − 4n is a square, so v_F(D) = ∞ for
  almost every D.

## Prop 2.1 (shape) — SOUND

Re-derived: ∇F = (2nA − BC, 2B − AC, −AB) vanishes only at A = B = 0, not on U (D ≠ 0). Closure
F̄ = ABC − W(nA² + B²) − DW³: at W = 0 the partials BC, AC, AB, nA² + B² vanish simultaneously only at [0:0:1:0]
([1:0:0:0], [0:1:0:0] have ∂_W = −n, −1 ≠ 0); in the chart C = 1 the local equation AB = DW³ + W(nA² + B²) has
rank-2 quadratic part AB and AB = DW³ + (higher) after completing, so A₂ ✔. Fibre over C = c: nA² − cAB + B² = −D ✔;
ι_A, ι_B are the root-swaps of that quadratic in A resp. B, so both fix C ✔. Boundary lines L_±, M_± ✔.
Wording only: ι_A is a ℚ-involution, integral only when n | BC (cf. R201 m2), so on integral points the relevant
group is ⟨ι_B⟩ ⋉ (norm-1 units of ℤ[√(c² − 4n)]); "ι_A ι_B is the Pell automorph" holds over ℚ. Harmless.

## Prop 2.2 (Pic, Br) — SOUND-AFTER-REPAIRS (scope of (c), independence argument of (b))

(a) Re-derived. On L_± one has ∂F/∂B = 2B − AC = ±2√−D ≠ 0, so (A, C) are local coordinates and ord_{L_±}(A) = 1,
B|_{L_±} = ±√−D is a unit; symmetric for M_±. Units: div(A^iB^j) = i(L₊ + L₋) + j(M₊ + M₋) ⇒ i = j = 0 ✔.
Pic Ū = ℤ⁴/⟨(1,1,0,0),(0,0,1,1)⟩ with [L₋] = −[L₊], Galois acting through Gal(ℚ(√−D)/ℚ) resp.
Gal(ℚ(√(−D/n))/ℚ) = Gal(ℚ(√−nD)/ℚ) by −1 ✔.
(b) H¹(ℚ, ℤ(χ)) = H¹(Gal(K/ℚ), ℤ⁻) = ℤ/2 (inflation is an iso since Hom(G_K, ℤ) = 0) ✔; H³(ℚ, G_m) = 0 and
ℚ̄[U]^* = ℚ̄^* give Br₁/Br₀ ≅ (ℤ/2)² ✔. Residues: (A, −D) along the ℚ-irreducible divisor L (function field
ℚ(√−D)(C), A a uniformiser): −D ∈ κ(L)^{*2} ✔; along M: A, −D units ✔. (B, −nD) along M: −nD = n²·(−D/n), a square
in ℚ(√(−D/n)) ✔. So both classes lie in Br U.
*Defect m1 (MINOR, Prop 2.2(b) proof).* Non-constancy/independence is deduced from Prop 3.4, whose evaluation needs a
prime ℓ ≡ 3 (4) with v_ℓ(D) odd and (−n/ℓ) = 1, i.e. admissible D; but Prop 2.2 is stated for every D ≥ 1. Repair
(valid for all D): in ℚ(U) = ℚ(A, B) (A, B algebraically independent), the residue of α₁ + εα₂ along the divisor
A = 0 of A²_{A,B} is [−D] ≠ 0 in ℚ(B)^*/ℚ(B)^{*2}, and the residue of α₂ along B = 0 is [−nD] ≠ 0; constant classes
have no residues, so α₁, α₂, α₁ + α₂ are all non-constant.
(c) Re-derived with Dao §1's residue convention ∂(f, g) = (−1)^{v(f)v(g)} g^{v(f)}/f^{v(g)}: ∂_L(A, B) = [B|_L] =
[±√−D], a constant, hence trivial over ℚ̄ ⇒ Br Ū = ℚ/ℤ(−1) (purity on the smooth Ū) and (Br Ū)^{G_ℚ} = ℤ/2
(complex conjugation acts by −1) ✔. A lift restricts on G_m² to (A, B) + (χ, A) + (χ', B) + c (structure of
Br of a split torus) ✔; along L the term (χ', B) has no residue (B a unit, χ' unramified), (χ, A) has residue
χ|_{K(C)}, so one needs χ|_{G_K} = [√−D] (sign irrelevant: 2-torsion, and [−√−D] = [√−D] + [−1] is handled because
the residue is taken on the ℚ-irreducible L whose two geometric components carry ±√−D — the condition is the same
on both). If FK = K((−D)^{1/4}) with F/ℚ abelian then ℚ((−D)^{1/4}) is abelian over ℚ, impossible when x⁴ + D is
irreducible and ℚ((−D)^{1/4}) ∌ i ✔.
*Defect m2 (MINOR, scope of (c)).* The argument uses D ≡ 3 (mod 4) ("ℚ(√−D) = ℚ(i) impossible"), which is not a
hypothesis of Prop 2.2. For D = c² it genuinely breaks along L: D = 1 gives ℚ((−1)^{1/4}) = ℚ(ζ₈), abelian, and
(A, B) + (2, A) is unramified along L ([√−1] + [2] = [2i] = [(1+i)²] = 0). (The class is then still obstructed along
M when n is not a square, so (c) is probably true for non-square n and all D, but that is a different argument.)
Repair: add "D not a square (e.g. D ≡ 3 mod 4, the only case used)" to Prop 2.2(c), or add the M-divisor argument.

## Lemma 3.1 (admissible D) — SOUND

Re-derived (ℓ = 2: 1 + D ≡ 0 mod 4 and A = 2, B = 1 converse; ℓ | D odd: AB = 0 is excluded by W_ℓ, ℓ | A or ℓ | B
makes the left side a unit, so ℓ ∤ ABn and −n ≡ (B/A)² mod ℓ^{v_ℓ(D)}; ℓ ∤ 2D: A = B = 1). Condition (ii) is
implied by (iii) (Legendre symbol = 1 forces ℓ ∤ n) — harmless redundancy.
Check `scripts/review_mk_local.py 150 13 17 21 29 9 25 45 49 105` (independent ℓ-adic integer search at every
ℓ | 2nD): **0 mismatches** with the closed-form criterion over 9 × 150 = 1350 pairs (n, D); 76 admissible D.

## Cor 3.2 — SOUND
(−m²/ℓ) = (−1/ℓ) for ℓ ∤ m; an integer ≡ 3 (4) has a prime ℓ ≡ 3 (4) to an odd power; if ℓ | m it fails (iii)
anyway ✔. Script: n = 9, 25, 45(non-square, control), 49: n = 9, 25, 49 have 0 admissible D ≤ 150 ✔.

## Prop 3.3 (family BM via (−1, D)) — SOUND-AFTER-REPAIRS (archimedean condition)

Re-derived: V_n : nA² + B² + D(1 − 2λAB) = 0 is smooth (∇ = 0 forces 2λAB = 1 and DAB = 0 ⇒ D = 0 ⇒ A = B = 0,
contradiction); D is regular, its zero divisor is E = {D = 0, nA² + B² = 0}, ℚ-irreducible with κ(E) =
ℚ(√−n)(A, λ), and ∂_B = 2B ≠ 0 on E, so D is a uniformiser; residue of (−1, D) is [−1] ∈ κ(E)^*/κ(E)^{*2}, trivial
iff i ∈ ℚ(√−n) iff n ∈ ℚ^{*2} ✔. Local invariants for n = m²: ℓ = 2 forces D ≡ 3 (4) (D(2λAB − 1) ≡ 1 mod 4), odd
ℓ: v_ℓ(D) ≥ 1 forces −n ≡ □ mod ℓ, so (−1/ℓ) = 1 ✔. `review_mk_local.py` also brute-checks these two facts at
ℓ ∈ {2, 3, 5, 7, 11, 13} for n = 9, 25, 49: no violation.
**Defect m3 (MINOR, but the proposition is false as written).** W_∞ = {A, B, λ > 0} (from §3) does NOT force D > 0
on real points of the 3-fold: D = (nA² + B²)/(2λAB − 1) < 0 whenever 0 < λAB < 1/2. With D_∞ < 0 one has
inv_∞ β = 1/2 and Σ_v inv_v β = 0, so with the stated W_∞ the BM set is non-empty and there is no obstruction.
"inv_∞ = 0 (D > 0)" silently adds D > 0. Repair: put W_∞ := {A, B, λ, D > 0} (equivalently λAB > 1/2; integral
points with λ, A, B ≥ 1 satisfy it). Also "for non-square n the class is ramified and gives nothing" should read
"β ∉ Br V_n, so β gives nothing" (other classes of Br V_n are not examined — that is fine, Prop 3.4 is the fibre
statement).

## Prop 3.4 (no BM obstruction on admissible fibres) — SOUND-AFTER-REPAIRS (displayed equality is false)

Evaluation re-derived: A, B ℓ-units, v = v_ℓ(D) odd: (A, −D)_ℓ = (A/ℓ), (B, −nD)_ℓ = (B/ℓ), B ≡ ±rA (mod ℓ^v)
gives (B/ℓ) = ±(r/ℓ)(A/ℓ) and (−1/ℓ) = −1 ⇒ all four pairs ✔ (no Hensel needed: v_ℓ(nA² + B²) ≥ v already makes λ
ℓ-integral). `review_mk_local.py`: for all 76 admissible (n, D) above, the prime ℓ realises all four pairs ✔.
**Defect m4 (MINOR, false as written).** "(∏_v W_v)^{Br S_{n,D}} = ∏_v W_v" is false: since α₁ takes both values
at ℓ, adelic points with Σ inv α₁ = 1/2 exist and are NOT in the BM set. What is proved (and all that is used) is
(∏_v W_v)^{Br} ≠ ∅ (indeed it meets every fibre of the projection forgetting the ℓ-component). Repair: replace "="
by "≠ ∅", also in §8 item 2 wording ("empty BM obstruction" is fine).

## Thm 4.1 (norm form) — SOUND (wording)
Identity (μA − B)² − (μ² − n)A² = nA² − 2μAB + B² ✔; B·B' = nA² + D gives gcd(B, n) = 1 ✔; |x| < μA gives B > 0 ✔.
Wording (m5): the bijection is points ↔ (x, z) with x ∈ ℤ (B = μA − x); each unordered {±x} gives the ι_B-pair of TWO
points. "in bijection with pairs {±x}, z" should read "in 2-to-1 correspondence … / in bijection with (x, z), x ∈ ℤ".

## Thm 4.2 (CF dictionary) — SOUND-AFTER-REPAIRS (hidden non-square hypothesis; small-μ caveat confirmed)
Lagrange/Legendre (|x² − Nz²| < √N, gcd 1 ⇒ convergent) and the sign rule ✔; D ≤ μ < √N ⇔ 3μ² > 4n ✔.
**Brute force** (`scripts/review_mk_cf.py 3 299 100 4`, own code; log `logs/review_mk_cf_299.log`): all odd
3 ≤ n ≤ 299, V_n points with A, B ≤ 100 and μ ≤ 4n found by divisor search (1049 points) vs CF hits:
**0 misses, 0 extras**; the excluded range 3μ² ≤ 4n and the square-N values were solved exhaustively
(Nagell-bound class representatives + orbit walk, resp. factorisation): 50 points there.
* m6 (MINOR): Thm 4.2 needs N = 4(μ² − n) non-square (else there is no infinite CF / "Q_k"). It is harmless for
  3μ² > 4n: if μ² − n = s², a point needs (x − 2sz)(x + 2sz) = −D with z ≥ 1, so 4s ≤ D + 1 ≤ μ + 1, whence
  4n/3 ≥ (15μ² − 2μ − 1)/12 > μ² — i.e. square-N points live only in the excluded range. They do occur there
  (e.g. n = 35, μ = 6, N = 4: (A, B, D) = (2, 11, 3), (2, 13, 3); 14 such points for n ≤ 299). Add the hypothesis
  and this one-line remark.
* The exclusion μ ≤ √(4n/3) is genuinely needed (author's caveat confirmed): n = 47, μ = 7, N = 8, D = 7 > √8 has
  the points (A, B) = (2, 13), (2, 15), (4, 23), (4, 33), (8, 45), (8, 67), none of which is a convergent.

## Thm 4.3 (depth 3) — formulas SOUND; headline "ES is exactly depth 3" FALSE as stated (MAJOR, easy repair)
CF steps re-derived by hand (a₀ = 2μ − 1 iff μ > n + 1/4; a₁ = 1 iff μ > 2n + 1/4; m₂ = 2μ − 4n, Q₂ = 4n,
a₂ = j − 1 with remainder 4t − 1, m₃ = 2nj − 2t, Q₃ = 4tj − 1; p₂² − Nq₂² = 1 − 4tj ✔) and checked: formulas hold
for every odd n ≤ 299 and 2n < μ ≤ 5n (0 failures); every B = 1 point with μ > 2n is at k = 3 (154 points).
**Defect M1 (MAJOR, scope).** The theorem itself is restricted to μ > 2n, but §4's title ("ES is depth 3"), the
theorem title ("ES's shot family is exactly depth 3"), §8 item 3, §7 Reading and report SHARP 1 assert it for the
whole shot family. That is false: if B = 1 and A ≥ 4 then 2μA = nA² + 1 + D gives μ > 2n, so the B = 1 points with
μ ≤ 2n are exactly A = 2, and there x/z = (2μ − 1)/1 = a₀ is the convergent of index 0, **depth k = 1**, with
D = Q₁ = 4μ − 1 − 4n = 4t − 1 (μ = n + t). These are the j = 1 shots "(4t − 1) | 4n + 1" — the most classical ES
shots of all. Data (`scripts/review_mk_depthtally.py`): 208 B = 1 points with μ ≤ 2n, all at k = 1 (n ≤ 299).
Repair: "ES's shot family = depth 1 (A = 2, j = 1) ∪ depth 3 (A = 2j, j ≥ 2); uniformly: the B = 1 point with
A = 2j is the convergent (2μj − 1)/j, of index 0 for j = 1 and index 2 for j ≥ 2; the divisibility is
(4tj − 1) | n + 4t² for all j ≥ 1 (for j = 1 this is (4t − 1) | 4n + 1)." The parallel with DEDEKIND (J)9
("length 3") should be re-stated accordingly or dropped.
**Defect m7 (MINOR).** "every B > 1 solution at depth ≥ 5" (report SHARP 1: "every overflow solution (B > 1) is at
depth k ≥ 5") is false even for μ > 2n: the ι_B-partner B = 4μj − 1 of every ES point is at depth 3 (154 cases).
For μ ≤ 2n, B > 1 points occur at depth 1 (172 non-partner) and 3 (546). Repair: "for μ > 2n, every point at depth
k ≥ 5 has B > 1, and the only B > 1 points at depth ≤ 3 are the ι_B-partners B = 4μj − 1 of ES points".
* §4 "Reading" (Euclid pattern) is correctly labelled Assessment; not checked further.

## Thm 5.1 (no polynomial families at fixed D) — SOUND (two small rigor gaps)
Re-derived. N(η) = μ² − f = n, N(α) = (B − μA)² − fA² = nA² + B² − 2μAB = −D ✔; rank R^* ≤ 1 (two ℚ-rational places
at ∞ since deg f = 2 deg μ is even with square leading coefficient D² lc(λ)²) ✔; N(ε) ∈ ℚ[s]^* = ℚ^* ✔; parity
argument ✔ (b < 0 harmless).
* m8 (MINOR): "f has coprime non-constant factors, so f is not a constant times a square" is a non-sequitur as
  written (coprime factors can each be squares). Correct argument: if μ − √n = c₁g₁², μ + √n = c₂g₂² then
  c₂g₂² − c₁g₁² = 2√n factors as (√c₂g₂ − √c₁g₁)(√c₂g₂ + √c₁g₁) = const, forcing g₁, g₂ constant.
* m9 (MINOR): R = ℚ[s, y]/(y² − f) may be non-normal (f can have repeated roots); say "R^* ⊂ O(C̃)^*, rank ≤ 1"
  (units of R are units of the normalisation; geometric integrality from f ∉ ℚ̄·ℚ̄[s]²).

## §6 EVIDENCE table — SOUND (3 cells + 2 spot checks + 1 depth reproduced exactly)
Local criterion re-derived (odd p | μ² − n: p ∤ D automatically, x² ≡ −D (mod p^{v}) ⇔ (−D/p) = 1, z = 1 lifts;
p = 2: 8 | N iff λ odd, then x² ≡ −D (mod 8) ⇔ D ≡ 7 (8); λ even: 4 ∥ N, take z ≡ (D + 1)/4 (mod 2)) ✔. The sign remark
("principal ⇒ generator of norm −D automatically, D ≡ 3 mod 4") ✔ — note ℤ[√N] has no unit of norm −1, so this is a
genuine narrow-class point that the author handled correctly.
`scripts/review_mk_fibre.py` (own CF scan over 1–2 periods for D < √N, Nagell-bound search otherwise, factorisation
for square N; sympy only for factoring μ² − n):
| case | O202 | R202 |
|---|---|---|
| n = 13, D = 7, λ ∈ [1, 301) | 49/63 | 49/63 (one square-N λ, λ = 1, handled) |
| n = 17, D = 3, λ ∈ [3000, 3300) | 58/87 | 58/87 |
| n = 105, D = 19, λ ∈ [30000, 30300) | 34/45 | 34/45 |
| n = 13, D = 7, λ ∈ [10⁵, 10⁵+100) | 11/15 | 11/15 |
| n = 17, D = 3, λ ∈ [10⁵, 10⁵+100) | 11/25 | 11/25 |
| n = 13, D = 7, λ = 10005: depth / period | 2329 / 21012 | 2329 / 21012 |
"global ⇒ local" never failed. EVIDENCE label appropriate.

## Prop 6.1 — labels OK (Assessment), two overstatements
* m10 (MINOR): (a) "The local layer of this main term is a provable half-dimensional sieve statement" is asserted
  without proof or precise citation; I could not check it here. Either cite the exact theorem (Iwaniec's
  half-dimensional sieve, Acta Arith. 29 (1976), and verify that its hypotheses cover "all prime factors of
  λ²D² − n lie outside a set of primes of relative density 1/2") or downgrade to "expected (Assessment)".
* m11 (MINOR): (c) "No unconditional technique proves even that …" is a literature-negative claim with no search
  record; phrase as "to our knowledge". The identification "RD subfamily = n | λ" is right up to finitely many μ
  (d = μ² − n = m'² + r', r' | 4m', |r'| ≤ m' with m' = μ − c forces c² ≤ n), and n | λ is impossible for every odd
  n (R201 m2; my brute force: 0 hits with n | λ in 1049 points).

## Prop 7.1 — (a), (b) SOUND (scope as in M1); (c) OVERCLAIMED: composition CAN land exactly on ES points
(a) A | 1 + D ✔. (b) multiplication by a norm-1 unit shifts the convergent index by the period (twice the period if
it is odd) ✔; with Thm 4.3, μ > 2n ✔. After M1, add the μ ≤ 2n case (B = 1 only at k = 1, A = 2).
**Defect M2 (MAJOR, label/claim).** (c) is labelled PROVED but only norm multiplicativity is proved; the operative
claims "lands at depth 3 only by coincidence", "composition move[s] AWAY from depth 3", "O201 spark 3 (composition)
does not give ES" (Reading, §8 item) are not proved, and the ideal-theoretic picture says the opposite: if the ES
ideal of norm D = D₁D₂D₃ factors into ideals that carry V_n points at the same μ, then (choosing conjugates = ι_B
partners) the ES element IS ±unit·α₁α₂α₃. Explicit instance found by `scripts/review_mk_compose.py 301 6`:
n = 59, μ = 126 (t = 8, j = 2), ES point (A, B, D) = (4, 1, 63); the same order has V_n points with D = 3 (A ≈ 3.7·10¹⁰)
and D = 7 (A ≈ 3.9·10²⁵), and the script verifies the ES element equals a unit times a product of the three
(3·3·7, with conjugations). Second instance n = 185, μ = 378, D = 63. (Only 2 such cases for n ≤ 301, μ ≤ 6n, so
composition is rare and, as the example shows, uses factors far deeper than the target — it is no route to ES.)
Repair: label (c) as Assessment; replace "lands at depth 3 only by coincidence" by "the ES element is a product of
V_n points of the same order iff its ideal factors into V_n-represented ideals (e.g. n = 59, μ = 126, D = 63 =
3·3·7); the factors are much deeper than the product, so composition gives no constructive route to depth 3".
