# R262 — hostile review of O251 (LATTICE_MEETING.md, BRAINSTORM/z23_*.md)

Reviewer: R262 side agent, branch side-agent/review-lattice-meeting, merged side-agent/lattice-meeting at start.
From-scratch scripts: `scripts/review_r262_*.py` (none reuse z23_* code).

## Verdict summary
Repairs applied: none (author branch side-agent/lattice-meeting active 11 min before this review finished; defects are
wording/attribution only and are left to the author).

| claim | verdict |
|---|---|
| C1 3361 CERTIFIED (two solutions, four non-split slices) + "only such prime ≤ 10⁷" + PROVED split ⟺ d square mod g | **SOUND** |
| C2 Prop 1.1 / Cor 1.2, 99-prime list (and 160 ≤ 10⁷) | **SOUND** (m1) |
| C3 Thm 1.4 (surjection), Cor 1.5 (norm-only; reading Assessment) | **SOUND** |
| C4 §2 composition coordinates, controlled lifts (ES only down), §2.3 k \| 6 genus statement | **SOUND-AFTER-REPAIRS** (m2, m3) |
| C5 Prop 3.1 (≤ 1 forced slot) | **SOUND-AFTER-REPAIRS** (Prop fine; Reading M1, m5) |
| C6 §4 EVIDENCE, JMV citation, z23_cayley limitation | **SOUND-AFTER-REPAIRS** (M2, m6, m7) |
| Labels | correct except the §3/§4 Readings flagged in M1/M2 |

No FATAL. Every headline number was reproduced by from-scratch code (`scripts/review_r262_*.py`).

## Numbered defects
1. **M1 (MAJOR)** LATTICE_MEETING §3 Reading, last sentence ("WINDMILL Prop 10.3 and Cor 1.5 already show the class
   carries no information about the meeting") + BRAINSTORM/z23_parity_budget.md Barrier screen ("Cor 1.5 shows is
   irrelevant"): re-states the non-sequitur retracted by R-O251 in Cor 1.5's own Reading. Repair in C5 below.
2. **M2 (MAJOR)** §4 "Unreached remainder … a code limitation, not a mathematical statement": false for ≥ 4 of 5 lines —
   prime forms of norm ≤ 40 generate an index-2 subgroup at (k, p) = (2,193), (2,577), (3,1061), (3,1493), ES classes in
   one coset. Also §4 Reading "as it must be" and §5 item 6 "under GRH this is forced by expansion" — JMV says nothing
   about generators ℓ ≤ 40 (below (log|Δ|)^{2+ε}). Repair in C6 below.
3. m1 §1 Certified-computation R-O251 parenthesis: the a ≤ √p + 2 scan sees each unordered pair *at least* once (~9 % in
   both orientations; unordered mean 12.19 vs scan mean 13.35). Repair: "at least once".
4. m2 §0 (I3): "for k | 6 every move preserves admissibility" — retracted in §2.3(a); align wording.
5. m3 §2.1: "even M iff v is even" ⇒ "iff vY is even" (Claude points may have even Y).
6. m5 §3 forced-slot definition: drop "ℓ ≡ 3 (4) being" (not needed, not implied for window primes).
7. m6 §4 table: distances are upper bounds from a subgraph (skipped compositions); exact k = 1 histogram 41/91/22/2,
   k = 2 max 7. Mark as upper bounds or replace.
8. m7 §4/§5: "within O(log p) moves" must name the generator set (prime ideals of norm ≤ (log|Δ|)^{2+ε} prime to 2k)
   and the k-dependence of Δ = −16k²p.
9. (suggestion) §1.3 "(The check covers split g only …)" can cite the R262 check over all 286 750 slices incl. non-split.
10. (suggestion) Thm 1.4 proof: add the one line "p ∤ x is automatic" (p | x, y, z would force 4 ≤ 3).

## Claim-by-claim

### C1. p = 3361 (CERTIFIED) and "only such prime ≤ 10⁷"
Independent complete enumeration (`scripts/review_r262_3361.py`, sympy only for factoring/divisors).
Completeness proof used: Type II means p | y, p | z, p ∤ x. Then y, z ≥ p ⇒ 1/x = 4/p − 1/y − 1/z ≥ 2/p, so
x ≤ p/2, and x > p/4. With y = pY, z = pZ, m = 4x − p ≥ 1: (mY − x)(mZ − x) = x², mY − x > 0. So looping over all
x ∈ (p/4, p/2] and all δ | x² with δ ≡ −x, x²/δ ≡ −x (mod m) lists every ordered solution. Result for p = 3361:
exactly two unordered solutions, (x, Y, Z) = (841, 290, 8410) and (850, 25, 170) — matches the document. Slices
g = 4Y − 1, D = 4Z − 1: 1159 = 19·61, 33639 = 3·11213, 99 = 3²·11, 679 = 7·97; −3361 is a non-square modulo each
(checked by brute force over every prime-power factor); gcd(slice, p) = 1 in all four cases. ET parameter
d = gcd(x, Y, Z) is 29 resp. 5, matching (1, 29, 10, 29) and (5, 34, 1, 5).
Spot-check of the ≤ 10⁷ scan (`scripts/review_r262_meet.py`, `scripts/review_r262_split.py`, both from scratch):
* 𝓜(p) = ∅ recomputed by Prop 1.1(iii) over **all** 332 180 primes p ≡ 1 (4) ≤ 10⁷ (SPF sieve to 2·10⁷;
  a ≤ (1 + √(4p+1))/4 suffices because the locus is symmetric in a, b and (4a−1)(4b−1) ≤ 4p+1): exactly **160**
  empty, blocks 22 / 23 / 54 / 61, all ≡ 1 (12) — matches. The 99 primes ≤ 10⁶ match the document's prefix and counts.
* For each of the 160: least ET d with any Type II solution {2: 157, 3: 1, 5: 2}; least d with a solution having a
  split slice (g or D) {2: 148, 3: 9, 5: 2, none ≤ 60: 1 = **3361**} — matches the document (≤ 10⁶: 96/1/2 and 88/8/2).
* Why only the 160 can be candidates (re-derived): if 𝓜(p) ≠ ∅ there is a d = 1 solution and g | p + 4a² with
  gcd(g, p) = 1 (p | g would force p | a, but a ≤ (p+1)/3), so −p ≡ (2a)² is a square mod g. ✓
* p = 3361 rechecked a third way: ET-parameter loop over **all** d ≤ (p+1)/3 (= 1120) and all a ≤ (1+√(4dp+1))/(4d)
  returns exactly the same two solutions, both invisible.
Reason (PROVED, re-derived): for (a, b, c, d) with g = 4acd − 1, (4acd − 1)(4abd − p) = 4a²d + p, so
−p ≡ 4a²d (mod g) and g ≡ −1 (mod 4ad) is prime to 2ad; hence −p is a square mod g ⟺ d is (mod each prime power of g).
Same for D = 4bcd − 1 by the a ↔ b symmetry. ✓

**Verdict C1: SOUND.** (Visibility is *defined* as "slice g = 4y/p − 1 or D = 4z/p − 1 is split"; with that
definition the CERTIFIED label is earned — two independent complete methods here plus the author's.)

### C2. Prop 1.1 / Cor 1.2 and the 99-prime list
Re-derived line by line: (i)⇔(ii) [(2k,1) ∈ L_ρ(g) ⟺ g | 4k²p+1, ρ = (2k)⁻¹ forced; D ≡ −1 (4k) since gD ≡ 1];
(ii)⇔(iii) [gm = 4a(4kab − kp − b) + p = 4a² + p; conversely m ≡ −p (4a), 4a(a+b) = m(g+1)]; the identity
(pk + a + b)/(pkab) = 4/p; bounds (4a−1)(4b−1) ≤ 4p+1, max ≤ (p+1)/3, k ≤ a+b — all correct. Also checked that
gcd(g, p) = 1 is automatic in (iii) (needed for g to be a slice; not stated in the proof). Cor 1.2(a) (ℓ ≡ 3 (4),
ℓ | c² + (2a)² ⇒ ℓ | a, contradicting g ≡ −1 (4a)) and (b) ((a, g) = (1, 3)) correct.
Numerics: 99 empty among 39 175 primes ≤ 10⁶, 22/23/54, all ≡ 1 (12), odd squares ≤ 10⁶ all empty — reproduced.
Independent second method (no Prop 1.1): complete Type II enumeration with the criterion "𝓜(p) ≠ ∅ ⟺ some Type II
solution has gcd(x, y/p, z/p) a perfect square" (ET Prop 2.6 uniqueness + dilation d ↦ d/s²): agrees on all 1 125
primes p ≡ 1 (4) ≤ 2·10⁴.
Mean-count remark (§1, R-O251 repair): reproduced ordered mean 24.37 and scan mean 13.35 (p ≤ 10⁵), **but** the
unordered mean is 12.19, so the sentence "the scan a ≤ √p + 2 sees each unordered {a, b} once in one orientation" is
false — it sees every unordered pair at least once, ~9 % of them in both orientations (defect m1).

**Verdict C2: SOUND** (one MINOR wording defect m1).

### C3. Thm 1.4 (slice criterion, surjection) and Cor 1.5 (norm-only)
Citation checked against sources/elsholtz-tao-1107.1010.pdf: ET Prop 2.6 states every Type II solution of 4/n is
π_n^II(a,b,c,d,e,f) = (abd, acdn, bcdn) with (2.15) 4abcd = a + b + nc, unique under gcd(a,b,c) = 1 — the document's
4-parameter form is exactly this (with the gcd normalisation dropped, which is why the map is not injective). ✓
Proof re-derived: forward 4a²d ≡ −(4ak)²p = −(4h)²p ≡ −p (mod g); b integral since 4a²d ≡ 0 (mod 4ad); p ∤ x is
automatic (p | x, y, z would give 4 = Σ 1/(·/p) ≤ 3 — worth one line, not stated); converse
(4acd−1)(4abd−p) = 4a²d + p, −4k²p ≡ (4acd)²d ≡ d, d ≤ k ≤ h < g. ✓ The case d_k = 0 is correctly excluded.
From-scratch brute force (`scripts/review_r262_slice.py 6000 3000`): **all** 286 750 slices g ≡ 3 (4) ≤ 3000,
gcd(g, p) = 1, p ≡ 1 (4) ≤ 6000 — *including non-split slices*, which the author's check skipped — brute-force set of
Type II solutions with y = ph (x ∈ (ph/g, ph/(g−h)], Z = hx/(gx − ph)) equals the image of the k-map: **0 mismatches**;
ES slices: 5 894 split (= the document's count) + 1 991 non-split; 1 889 non-injective collisions (the p = 29, g = 15
example reproduced). So the parenthetical "(The check covers split g only …)" can now be upgraded.
Lattice reading: Y_k ≡ 2kρ ⇒ Y_k² ≡ −4k²p ≡ d_k ✓; norm of √d + 2k√−p ✓; s²-reduction ✓.
Cor 1.5: correct and (as the R-O251 repair now says) essentially tautological, since E(𝔤) is defined through N𝔤.
"one primitive ideal per root ρ mod g" correct for odd g prime to p. The Assessment label on the reading is right.

**Verdict C3: SOUND.**

### C4. §2 — composition coordinates, controlled lifts, fixed-line reduction, k | 6 genus statement
2.1: L_ρ(g) = gℤ + (ρ + √−p)ℤ ⟺ Y ≡ ρM (g) ✓; (Y + M√−p)(u + v√−p) = (uY − pvM) + (uM + vY)√−p ✓; product of
primitive ideals of coprime norms is primitive of norm gℓ with root ρ′ by CRT ✓ (the image β𝔤 is a sublattice of
index N(β)/ℓ in 𝔤𝔩 — "maps into", fine). **Defect m3:** "goes to a point with even M iff v is even" is only true for
odd Y; Claude points can have even Y (Y is any representative of 2kρ mod g). Correct statement: M′ even ⟺ vY even.
2.2: h | (gu+1)/4 ⟺ u ≡ 1 (4h) ✓ (g ≡ −1 (4h) is a unit); d_k(gu) ≡ d_k(g) (mod g) ✓; d_k(gu) | k ⇒ d_k(gu) < g ⇒
d_k(gu) = d_k(g) ✓; lifting condition gu | 4k²p + d ✓. "ES propagates only down" is PROVED as stated.
2.3: disc of [g, 2Y, D] = 4Y² − 4(4k²p + Y²) = −16k²p ✓ (order of conductor 2k in ℚ(√−p), since ℤ[√−p] has disc −4p) ✓;
D ≡ −Y² (4k) ✓; (a) exponent-2 argument via m₁m₂ = N(α₁ᾱ₂/N𝔞), principal values x² + 4k²py² ≡ x² ≡ 1 (4k) ✓
(needs 𝔞 invertible in the order — true for primitive forms). From-scratch numerical check
(`scripts/review_r262_genus.py`, all reduced primitive forms of disc −16k²p, p ≡ 1 (4) < 400): for k ∈ {1,2,3,6}
0 forms with non-congruent coprime values; for k ∈ {4,5,7} every form fails — consistent with "iff k | 6" and with
WINDMILL Prop 10.3 (exponent 2 ⟺ 4k | 24). The reviewer counter-example p = 5, g = 43, Y = 61 recomputed:
[43,122,87] → [43,36,8] → [8,−36,43] ✓. Landau analogy correctly labelled heuristic. "[g, 2, D], g ≤ D is reduced" ✓.
**Defect m2:** the iteration log (§0, I3, line 20) still says "for k | 6 *every move preserves* admissibility" — the
statement the R-O251 repair retracted in §2.3(a). Repair: "for k | 6 admissibility of coprime first coefficients is a
genus property (not preserved by all reduction moves)".
(b) is a reading (WINDMILL 10.3 parallel), appropriately not claimed as a theorem beyond the swap computation.

**Verdict C4: SOUND-AFTER-REPAIRS** (m2, m3 wording only).

### C5. Prop 3.1 (parity budget)
Re-derived: (a) 4h = g + 1 ≡ 1 (g) ⇒ h ≡ (2⁻¹)² is a square mod every prime ℓ | g (composite g fine) ✓; D likewise
(4bcd = D + 1) ✓. (b) 4x ≡ p (m), m odd (≡ 3 (4)), p ∤ m (else p | x) ⇒ (x/ℓ) = (p/ℓ) ✓. Type I level: x = pH,
(4H − 1)/(pH) = 1/y + 1/z, e = 4H − 1 ⇒ 4H ≡ 1 (e) ✓ (ASTRA_BRIDGE Prop 5.1(b) says the same for the slice). (c) ✓.
The proposition is correct but definitional: "forced" is *defined* by a Legendre symbol of the coordinate, and every
slice coordinate is 4⁻¹ mod its modulus. PROVED is fine; it is a near-tautology and should not be sold as more.
**Defect m5:** "forced at ℓ … if (u/ℓ) = −1: then, ℓ ≡ 3 (4) being prime, … −1 ∈ ⟨u⟩" — the hypothesis ℓ ≡ 3 (4)
is neither part of the definition nor needed (any odd prime: a non-residue has order with full 2-part of ℓ − 1, hence
even order, hence −1 ∈ ⟨u⟩); window primes ℓ | m can be ≡ 1 (4). Repair: drop "ℓ ≡ 3 (4) being".
**Defect M1 (MAJOR, recurrence of a retracted claim):** the Reading after Prop 3.1 ends "where WINDMILL Prop 10.3 and
Cor 1.5 already show the class carries no information about the meeting", and BRAINSTORM/z23_parity_budget.md says the
4-rank/Rédei invariant is something "Cor 1.5 shows is irrelevant". This is exactly the non-sequitur the R-O251 repair
retracted in Cor 1.5's own Reading ("does not exclude class data constraining or guiding the norms produced").
Neither Cor 1.5 (tautological norm-dependence) nor WINDMILL 10.3 (class functions see N𝔞 mod t only up to squares)
says anything about 4-rank/Rédei data of the slice lattice and the meeting. Repair: replace by "… on a non-quadratic
invariant of the slice (4-rank / Rédei symbol), about which nothing is proved here; WINDMILL 10.3 limits class
functions of N𝔞 mod t to the genus shadow, and Cor 1.5 is only norm-dependence of E." Same edit in the memo.

**Verdict C5: SOUND-AFTER-REPAIRS** (Prop correct; Reading overclaims — M1, m5).

### C6. §4 — Cayley distances (EVIDENCE), JMV citation, z23_cayley limitation
Citation (checked against arXiv:0811.0647 = J. Number Theory 129(6) (2009) 1491–1504; bibliographic data ✓):
JMV Thm 1.1 (ray class groups of number fields, generators prime ideals of norm ≤ x) and Thm 3.2 (Cl(O_D) for an
*arbitrary* imaginary quadratic order, generators ideals of prime norm < M with M ≥ (log|D|)^B, B > 2) give, under
GRH, the expander bound (1.7). Thm 3.2 covers the non-maximal orders of conductor 2k used here ✓; expansion ⇒
diameter O(log h) ⇒ any nonempty target within O(log|Δ|) steps ✓.
From-scratch exact re-run (`scripts/review_r262_cayley.py 3000 40 1,2,3,5`: ideal multiplication by ℤ-lattice HNF,
no skipped steps; group axioms spot-tested; same generator set ℓ ≤ 40, ℓ ∤ 2kp, both roots):
| k | mean #classes | no ES class | exact worst-start hist | lines with unreached classes |
|---|---|---|---|---|
| 1 | 55.5 ✓ | 55 ✓ | {1: 41, 2: 91, 3: 22, 4: 2} (doc: 32/94/28/2) | 0 |
| 2 | 111.0 ✓ | 72 ✓ | max 7 (doc ≤ 8) | 2 (p = 193, 577) |
| 3 | 144.6 ✓ | 109 ✓ | max 6 ✓ | 2 (p = 1061, 1493) |
| 5 | 268.6 ✓ | 153 ✓ | max 5 ✓ | 0 |
Class counts and no-ES counts match exactly. **Defect m6:** the document's distance histograms are distances in a
*subgraph* (z23_cayley's `compose` only handles coprime leading coefficients and drops the edge otherwise), so they
are upper bounds, not "worst-start distances" for the stated generator set; e.g. k = 1 true histogram is 41/91/22/2.
Harmless for the qualitative EVIDENCE, but the table should say "upper bounds (edges dropped when composition skipped)"
or be replaced by exact numbers. **Defect M2 (MAJOR as a factual statement about the data):** "'Unreached remainder':
… a code limitation, not a mathematical statement" is **false for at least 4 of the 5 lines**: with exact composition,
the prime forms of norm ≤ 40 generate only an index-2 subgroup of the class group of disc −16k²p for (k, p) =
(2, 193), (2, 577), (3, 1061), (3, 1493) (h = 16, 32, 104, 88; reached 8, 16, 52, 44), and all ES classes lie in one coset —
no walk with those generators reaches the other coset at any length. (Independently, ⟨ℓ ≤ 40⟩ ≠ Cl on 17 of the
844 (k, p) lines.) Consequently the Reading "When an ES class exists on a line, it is a few generator steps from
*every* class — as it must be" is contradicted by the document's own data at fixed generators ℓ ≤ 40. Repair: say
the generators ℓ ≤ 40 are far below the JMV/Bach regime ((log|Δ|)^{2+ε} ≈ 115–200, Bach 6 log²|Δ| ≈ 700–1200 for these Δ) and
need not generate Cl; report the 4 lines as genuine non-generation, and drop "as it must be" (JMV predicts nothing
for ℓ ≤ 40). **Defect m7:** "reach an ES class within O(log p) moves ⟺ (GRH) the line carries an ES class" must name the
generator set (all prime ideals of norm ≤ (log|Δ|)^{2+ε} prime to the conductor 2k, Δ = −16k²p, so the implicit
constant and the generator bound depend on k); as written "O(log p) moves" is unspecified.
T1 at odd squares: Cor 1.2(a)/ET Prop 1.6 make "no ES class" a theorem; fine.
z23_descent (all 1565 starting forms already reduced) not re-run; it is a weak statement (b = 2Y small vs g by
construction of the least-root shot) and labelled EVIDENCE.

**Verdict C6: SOUND-AFTER-REPAIRS** (numbers reproduce; M2 mis-attribution + overclaimed reading; m6, m7).
