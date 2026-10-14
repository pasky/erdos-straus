# R208 — hostile review of O210 FRIEZE_ES.md (+ BRAINSTORM/y2_*.md)

Reviewer: R208 (side-agent/review-frieze). Reviewed at merge of side-agent/frieze-es @ 7bb85625.
From-scratch scripts: `scripts/review_r208_*.py`; logs `logs/review_r208_*.txt`.
**ES is not solved; nothing below changes that.**

**Repairs applied (author quiet):** D1–D15 applied directly to FRIEZE_ES.md, BRAINSTORM/y2_{even_edge,
twoadic_tree_transport, positivity_is_T1, farey_complex_lifting, hexagon_degeneration, parity_involution,
zamolodchikov_forcing}.md and AGENT_REPORT_O210.md, each marked '(R208 repair)' / 'R208'. D8 upgrades the §4
CONJECTURE to PROVED.

## Summary verdicts (filled in claim by claim)

| # | claim | verdict |
|---|---|---|
| 1 | Lemma 1.1 (parity rigidity: exactly two adjacent even cluster variables) | SOUND |
| 2 | Thm 1.2 (even-edge sign law), 3-case proof; Cor 1.3, 1.4 | SOUND (typo D2) |
| 2′ | Novelty: "extends DK Thm 4.5 to formal words and N ≡ 3 (4)" | GAP — already MODEL_SPECIFIC Thm 3.1(a) (D1) |
| 3 | Transport law (h′/N) = −(2/o) for N ≡ 1 (8) (and the general two-branch law) | SOUND (proof text D3, wording D4) |
| 4 | 2-adic Bruhat–Tits cherry-depth reading | SOUND (restatement) |
| 5 | §0/§3: SVZ citation, F₄ odd walks strongly contractible, "T1 lives in positivity" | SOUND-AFTER-REPAIRS (D5–D7) |
| 6 | §4 hexagon identity, r = 2/4/≡0 (4), witnesses r ≤ 12, Thm 4.1 | SOUND-AFTER-REPAIRS (D8–D11); r ≥ 4 CONJECTURE is PROVED (D8) |
| 7 | memos: parity involution / Zamolodchikov / coefficients model | SOUND-AFTER-REPAIRS / SOUND-AFTER-REPAIRS / SOUND (D12, D13) |
| 8 | Literature (CHJ, SVZ, Böhmler–Cuntz, MGO, Guo, BHS, MSW) | SOUND with minor fixes (D14) |

No FATAL. Two MAJOR (D1 novelty, D5 label), one MAJOR-positive upgrade (D8). ES is not solved; nothing claimed here
changes that.

## Claim 1 — Lemma 1.1 (re-derived)
Ptolemy relations (P) re-derived from N = mcs − c − s, h = cm − 1, h′ = ms − 1 (all five are polynomial identities).
Mod 2 with N odd, all five read q_i q_{i+1} ≡ 1 + q_{i+3} (indices mod 5): checked for each i (the N in relations 1, 4
and the N·q₃ in relation 5 reduce to 1 resp. q₃). Memo proof: if all odd, q_{i+3} even — contradiction; if q_i even,
relations at i−1, i force q_{i+2}, q_{i+3} odd, and relation at i+3 gives q_{i−1} ≡ 1 + q_{i+1}; applying the same
to the even neighbour gives exactly two evens. Correct. No positivity used (only N odd) — correct as stated.
CERTIFIED independently (`scripts/review_r208_even_edge.py 100000 1000000 10000000`, 20 s): all 5 115 860 odd-N
formal words N ≤ 10⁵ (count and all five edge-position counts agree with the author's log exactly), plus 10⁶ random
words with letters ≤ 10⁷ (N up to ~10²¹): 0 failures.

## Claim 2 — Theorem 1.2 (re-derived line by line)
Positivity used: every Jacobi symbol in the proof has a positive odd bottom (N, h, c′, h″, s, m all ≥ 1), and
gcd(h′, N) = gcd(h, N) = 1 from hh′ = 1 + Nm, so no symbol vanishes.
* Case A {c, m}: h ≡ −1 (mod 2^{a+b}), a + b ≥ 2 ⇒ h ≡ 3 (4). Step 2 reciprocity sign (−1)^{(h−1)/2·(N−1)/2} = (−1/N) ✓.
  Step 3: N ≡ −c (h), (−1/h) = −1 ✓. Step 4: (c′/h)(h/c′) = (−1/c′) since h ≡ 3 (4), and (h/c′) = (−1/c′) ⇒ (c′/h) = 1 ✓.
  Step 5: a + b ≥ 3 ⇒ h ≡ 7 (8); a = b = 1 ⇒ cm ≡ 4 (8), h ≡ 3 (8), (c/h) = (2/h) = −1 ✓. Final sign bookkeeping
  −(−1)^{[cm≡4(8)]} = (−1)^{[8|cm]} uses 4 | cm ✓. Mirror {m, s} by reversal, using (h/N) = (h′/N) ✓.
* Case B {h′, c}: s ≡ −N (4) from h′c ≡ 0 (4) ✓; step 5 exponent ((h″−1)/2)((N−1)/2 + (s−1)/2 + 1) even since
  N + s ≡ 0 (4) ✓; step 7 Ns = Nh′c − N² ≡ h′c − 1 (mod 8) (uses (N − 1)h′c ≡ 0 (8)) ✓. In the "otherwise" branch
  the text says "b = v₂(c) = 1"; it should read "b = v₂(h′) = 1 (and v₂(c) = 1)" (D2).
* Case C {h, h′}: m ≡ −N (4) from hh′ = 1 + Nm ✓; (N/h″) = (−1/h″)(m/h″) uses ms ≡ 1 (h″) ⇒ (s/h″) = (m/h″) ✓;
  (h′/m) = (−1/m) from h ≡ −1 (m), hh′ ≡ 1 (m) ✓; step 7 Nm = hh′ − 1 exactly ✓.
* The five edges {h′,c}, {c,m}, {m,s}, {s,h}, {h,h′} are covered by A, A-mirror, B, B-mirror, C ✓.
Corollaries 1.3 (8 | ee′ ⟺ some q_i ≡ 0 (4), since both even letters have v₂ ≥ 1 and the others are odd) and 1.4
(N = M²: (h′/N) = (−1/N) = 1) ✓. Odd-square control: my count is 8 073 words vs the author's 8 068 — the difference
is exactly N = 1 (5 words; 1 is an odd square), which the author's control evidently excludes; all 8 073 have
ee′ ≡ 4 (8). Not a defect beyond wording.
**Verdict: SOUND.** The proof is complete, elementary and self-contained (no Dedekind sums, no cell enumeration).

## Claim 2′ — novelty of Thm 1.2 (D1)
FRIEZE_ES §1 Remark / §6 and memo y2_even_edge say Thm 1.2 "extends [DK Thm 4.5] to formal words and to N ≡ 3 (4)".
But MODEL_SPECIFIC Thm 3.1(a) ((J)32, on main) already states, for *every word incl. boundary words and every odd n*:
"a word lies in S₄ ⟺ χ(w) = −1", χ = (−A/n) = (−h′/N), S₄ = "some cluster variable ≡ 0 (mod 4)" — and notes "for
n ≡ 3 mod 4 it is new in this form". Since (−h′/N) = (−1/N)(h′/N), Thm 1.2 ⟺ "χ = −1 ⟺ 8 | ee′" ⟺ (by Lemma 1.1)
MODEL_SPECIFIC 3.1(a). So the *statement* of the extension is not new; CHI_FLIP Cor 1.2 (R198 repair) also gives a
self-contained proof of the same cell law. What IS new: (i) Lemma 1.1 (mod-2 rigidity, the even edge as a locating
device); (ii) a short computation-free proof of MS 3.1(a), avoiding DK Cor 4.1 (Hirzebruch–Zagier + Rademacher) and
any 512/320-cell enumeration. **Verdict: GAP (overclaim of novelty), repairable by rewording.**

## Claim 3 — transport law §2 (re-derived)
With o = q_{i+3} for the even edge (q_i, q_{i+1}) — o = h for {c,m}, h′ for {m,s}, s for {h′,c}, c for {s,h}, m for {h,h′}:
* Case A: (h′/N) = −(−1/N)(c/h), and (c/h) = (2/h)^a = (2/h) always (if a ≥ 2 then h ≡ 7 (8)). So
  (h′/N) = −(−1/N)(2/o) with o = h ✓ (mirror: o = h′).
* Case B: (h′/N) = (2/(Ns))^b(−1/s) = −(−1/N)(2/N)(2/s)·(2/(Ns))^{b−1}; if b ≥ 2 then 8 | h′c and Ns ≡ 7 (8), so the
  last factor is 1 and (h′/N) = −(−2/N)(2/o), o = s ✓. Case C identical with o = m ✓.
* N ≡ 1 (8) ⇒ (−1/N) = (−2/N) = 1 ⇒ (h′/N) = −(2/o) ✓.
My derivation (above) is cleaner than the memo's one-line "proof" (which compares (2/o) with (2/−στ⁻¹) without
defining σ, τ); suggest replacing it (D3). CERTIFIED independently: the full two-branch law (all N mod 8) holds on all
5 115 860 words N ≤ 10⁵ and 10⁶ random words (`review_r208_even_edge.py`, check TR/TR8; 0 failures).
Caveat (Assessment wording, D4): o is not "small" in general (o = h or h′ can be ≍ N); and given N mod 8, (2/o) is
simply a rewriting of v₂(ee′) through one Ptolemy relation, so "the character of N is carried by the character of 2 at
o" is a reformulation of Thm 1.2, not extra information. **Verdict: SOUND** (as a corollary of Thm 1.2).

## Claim 4 — 2-adic Bruhat–Tits "cherry depth" reading
For primitive u, v ∈ ℤ², v₂(det(u, v)) = max{k : u ≡ λv (mod 2^k), λ ∈ ℤ₂^×} = Gromov product of the ends [u], [v]
at v₀ = [ℤ₂²] (standard; Serre, *Trees* II.1 — from memory). The five V_i of LENGTH_THREE Prop 1.1 are primitive
(gcd(h,m) = gcd(N,h′) = 1). The quiddity at V_j is λ_{j−1,j+1}, so q_j even ⟺ V_{j−1}, V_{j+1} leave v₀ along the
same edge. Sides odd ⇒ adjacent ends leave along different edges; Lemma 1.1 gives the colour pattern (a,b,a,b,c) on
(V_{i−1},…,V_{i+3}) with a, b, c the three distinct neighbours, hence two cherries of depths v₂(q_i), v₂(q_{i+1}) and
a lone end V_{i+3} = the vertex carrying o ✓. "Sign ⟺ depth sum ≥ 3" and "T1 ⟺ depths (1,1)" are correct
restatements of Thm 1.2 / Cor 1.4; "depth ≥ 2 ⟺ the two ends agree mod 4 up to sign" ✓ (units mod 4 are ±1).
Small point: the depth-1 (k = 1) colour argument needs only that the three classes of P¹(F₂) are distinct, ✓.
**Verdict: SOUND** (a correct restatement; no new content beyond Thm 1.2).

## Claim 5 — §0 (I1) / §3 / memo y2_farey_complex_lifting: SVZ citation, F₄, "T1 lives in positivity"
* **SVZ citation.** Fetched arXiv:2312.12953 (Short–Van Son–Zabolotskii, *Frieze patterns and Farey complexes*) and read
  §1. Thm 1.6 verbatim: "A tame semiregular frieze F over ℤ/Nℤ lifts to a tame frieze over ℤ of the same width if and
  only if any path γ in F_N corresponding to F is a strongly contractible closed path." Strong contractibility = reducible
  to a point by spur removals ⟨v,u,v⟩ → ⟨v⟩ and triangle shortcuts ⟨u,v,w⟩ → ⟨u,w⟩ (u, v, w mutually adjacent). The paper's
  own example, the non-contractible 4-path 0/1 → 1/1 → 2/1 → 3/1 → 0/1 in F₄, is as quoted. Citation **correct**. Minor
  precision: Thm 1.6 is for *semiregular* friezes (second row all 1); the mod-4 pentagon at N ≡ 3 (4) has a boundary
  entry −1 and must first be normalised (SVZ §1, R^×\FR_n ≅ FR*_n) — harmless, but the memo should say so (D7).
* **F₄ = octahedron, odd closed walks strongly contractible.** From scratch (`scripts/review_r208_f4.py`,
  `logs/review_r208_f4.txt`): F₄ has 6 vertices, 12 edges, 8 triangles, and the 8 triangles are exactly the images of
  Farey triangles {u, v, u ± v}, so every triangle is a face. Closed walks of length 3…7: 48, 288, 960, 4 224, 16 128
  (= tr A^L, eigenvalues 4, 0³, (−2)²); strongly contractible: 48, 264, **960, 4 080, 16 128**, identically under a based
  and a cyclic reading of the moves. Matches the memo (960/960, 16 128/16 128, 264/288). Spur/antipode dictionary
  (q_i ≡ 0 (4) ⟺ spur, ≡ 2 ⟺ antipodal neighbours, odd ⟺ adjacent) holds on all 6 805 odd-N words N ≤ 400; it is also
  immediate from det(V_{i−1}, V_{i+1}) = q_i for primitive vectors. **SOUND.**
* **Signed friezes at odd squares.** The memo/§3 cite only a box search (EVIDENCE). It is in fact PROVED by an explicit
  family: for every odd M ≥ 3 the signed word (c, m, s) = (4, −(M² + 3)/4, −1) has N = M² and quiddity c = 4 (all five
  Ptolemy relations are polynomial identities; checked M < 2000 in `scripts/review_r208_signed.py`). Suggest upgrading
  (D6). So positivity is genuinely necessary for Thm 1.2/Cor 1.4. **SOUND (and can be strengthened).**
* **"T1 = the archimedean factor of Hilbert reciprocity" (§3).** As an interpretation this is right, but it is not new:
  CHI_FLIP Thm 1.1 already proves χ = −ε₂(Q_w) with ε_∞ = −1 *because G_w is positive definite*, and CHI_FLIP §2 says
  "inv_∞ β(w) = ½ on the positive cone" / "T1 as Brauer–Manin"; DISCOVERIES (J)13 likewise. §3 should cite CHI_FLIP for
  this and present the frieze version as a restatement (D5).
* **Label overclaim (D5).** §3's header "PROVED by inspection" covers three different things: (a) "positivity is
  needed" — PROVED (by the explicit family above); (b) "positivity is used only in the reciprocity steps" — true by
  inspection of *this* proof, but says nothing about other proofs; (c) "**Any frieze-theoretic ES proof must use the
  positivity of the frieze archimedeanly**" and "SVZ / finite-ring frieze theory is T1-blind" — these are Assessments
  (heuristic barrier statements; e.g. "frieze-theoretic proof" is undefined). Moreover (c) is close to tautological:
  the ES output must be a *positive* word, and signed 4-quiddity words exist at every odd square, so any argument
  that never distinguishes signs proves nothing about ES. The precise, provable statement is the B1-type one: a
  criterion depending on N only through N mod n (any n) cannot separate odd squares M² from primes p ≡ M² (mod n),
  hence cannot yield a −1 word at all such primes while respecting Cor 1.4. "Finite-ring frieze theory is N-blind
  beyond N mod 8" (§3 bullet 2, memo) is literally false — a frieze over ℤ/n sees N mod n — and should be replaced by
  that statement.
* SVZ "T1-blind": correct but for a trivial reason — SVZ Thm 1.6 is about lifting to *unit*-boundary tame (signed)
  friezes of the same width, a different lifting problem from "lift to a positive frieze with boundary (1,1,1,1,N)".
  The memo itself says so (iteration 1). Fine as Assessment.
**Verdict: SOUND-AFTER-REPAIRS** (relabel (c) as Assessment; cite CHI_FLIP; fix the "N mod 8" sentence).

## Claim 6 — §4 polygon size, hexagon identity, Thm 4.1 (memo y2_hexagon_degeneration)
From scratch: `scripts/review_r208_polygon.py` (log `logs/review_r208_polygon.txt`), `scripts/review_r208_hexnum.py`.
* **Hexagon identity** 4/N = 1/k + 1/(k(2k−1)) + 1/((2k−1)(3k−2)) + 1/(N(3k−2)), N = 4k − 3: re-derived by telescoping
  (partial sums 2/(2k−1), 3/(3k−2), then (3N + 1)/(N(3k−2)) = 4/N), and checked in exact rationals for 2 ≤ k < 3000.
  K(2,2,2,k) = 4k − 3 and the quiddity at V₆ is 4 (my polygon code). **SOUND.**
* **r = 2** (xy = N + 1 ≡ 2 (4); the four quiddities are x, y, x, y) **SOUND**. **r = 4** **SOUND**.
  **r ≡ 0 (4)** family (2^{r−1}, k): K = rk − r + 1, quiddity r at V_{r+2} (checked r ≤ 20); N ≡ 1 (mod r) contains
  (r+1)² with k = r + 3 ≥ 2. **SOUND.**
* **Witnesses r ≤ 12:** my independent search finds exactly the author's first odd-square witnesses (r = 5: 25;
  6: 49; 7: 81; 8: 9; 9: 49; 10: 81; 11: 225; 12: 25) and none for r = 2, 3 up to N = 49². **CERTIFIED.**
* **The CONJECTURE "for all r ≥ 4" is in fact PROVED (R208).** For r ≥ 5 take the interior word
  w = (2, 2, 2, 4, 2^l, k), l = r − 5. With the prefix p = (2,2,2,4,2^l): K(2^j, 4, 2^l) = 2jl + 3j + 3l + 4, so
  Q := K(p) = 9l + 13 and K(p⁻) = Q − 9 (j = 3). Then K(w) = kQ − (Q − 9) ≡ 9 (mod Q), so with M = 2Q + 3 (odd),
  N = M² ≡ 9 (mod Q) and k = (N + Q − 9)/Q ≥ 2 is an integer. The letter 4 is a quiddity (b_i = λ_{i,i+2}).
  So Z_r(M²) holds for every r ≥ 4. Checked for 5 ≤ r ≤ 60 (`family_all_r` in my script). Suggest replacing the
  CONJECTURE/EVIDENCE line and the "(for r ≤ 12 and r ≡ 0 (4); CONJECTURE beyond)" qualifier (D8).
* **Definition gap (D9).** "The zero locus is (not) a Jacobi fibre" is never defined. The intended meaning is surely:
  among interior length-r words at N ≡ 1 (4), {some quiddity ≡ 0 (4)} = {(A/N) = −1}. A witness at an odd square
  only shows the zero locus ⊄ {(A/N) = −1}; that suffices for "≠", but the statement "not contained in a Jacobi fibre"
  needs also ⊄ {+1}, which is only EVIDENCE (r = 4, both signs, memo). r = 2 must be handled separately: its zero
  locus is empty, which differs from the non-empty −1 fibre (e.g. N = 5, (x,y) = (2,3), A = 3) — fine, but say so.
* **Thm 4.1.** Geometry re-derived: triangles containing the N-side are cut by h = λ₁₄ and h′ = λ₂₅, leaving the
  quadrilateral (1,1,1,h) i.e. cm = h + 1, and N = hs − c ✓; h = 4: cm = 5 ⇒ (1,5)/(5,1), N = 4s − 1 or 4s − 5 ≡ 3 (4) ✓.
  Interior words at 4 are exactly (4), (2,2,2) ✓ (length 2: xy = 5; length 3: m = 2 forces (2c−1)(2s−1) = 9; m ≥ 3 gives
  K ≥ 8; length ≥ 4 gives K ≥ 5). Two inaccuracies: the "otherwise" bullet "hs = N + 4w" is right only for c = 4w; for
  m = 4w the relation is hh′ = 1 + 4wN and for s = 4w it is ch′ = N + 4w (memo says "product = N + const", also wrong
  for m). And "leaves a divisor event" is not a mathematical predicate — Thm 4.1's PROVED content is the piece
  identification; "divisor event / B2" is Assessment (D10).
* **Numerics** (`review_r208_hexnum.py`, N ≤ 5000): r = 4 fails only at 3, 7, 15 ✓; r = 3 fails at 34 odd squares and 13
  non-squares ✓, but the non-squares are 3, 5, 7, 11, 15, 23, 27, 35, 39, 55, 99, 105, 119 — the memo's description
  "N ≡ 3 (4) cases and 105" omits N = 5 (≡ 1 (4), L₃(5) = ∅) (D11).
* Mod-2 patterns: re-derived — closed 6-walks on K₃ = P¹(F₂) are step sequences ε ∈ {±1}⁶ with Σε ≡ 0 (3), i.e. all equal
  or three of each sign; up to dihedral symmetry that gives exactly the four patterns (1⁶), (0,1,1,0,1,1),
  4-even, (0⁶) ✓; for the pentagon Σε = ±3 forces one sign change pair, i.e. Lemma 1.1 again ✓.
**Verdict: SOUND-AFTER-REPAIRS** (and the conjecture upgrades to PROVED).

## Claim 7 — memos y2_parity_involution, y2_zamolodchikov_forcing, y2_coefficients_model
Script `scripts/review_r208_parity.py 3000` (log `logs/review_r208_parity.txt`).
* **Parity involution, Lemma 2.** Re-derived: c = s gives c(mc − 2) = p, so (c, m) = (1, p + 2) or (p, 3/p). Hence the
  fixed point is unique for every prime **p ≠ 3**; at p = 3 there are two, (1,5,1) and (3,1,3) (my run confirms: p = 3 is
  the only prime < 3000 with ≠ 1 fixed point). Harmless for the p ≡ 1 (4) conclusion, but the Lemma says "at a prime p"
  (D12). For p ≡ 1 (4): fixed point has even edge {p+1, p+1}, ee′ ≡ 4 (8), sign +1 by Thm 1.2 ✓; the reflection
  preserves the sign since (h/N) = (h′/N) ✓; so #F odd, #F₊ odd, #F₋ even ✓. EVIDENCE line re-checked exactly: 211 primes,
  all #F odd, all #F₋ even, split 101/110 mod 4; #F₋ = 0 at all odd squares < 3000 ✓.
  Lemma 1 is PROVED only in the narrow sense "no Vieta involutions (each variable appears linearly) and the only
  dihedral symmetry fixing the N-side is the reflection"; the Iteration sentence "the only involutions are the dihedral
  ones" is not proved (arbitrary bijections of the finite set F(N) exist) — Assessment (D12).
* **Zamolodchikov.** Twisted Lyness relations in cycle order (c, h, m, h′, s) re-derived: (α, β) =
  (1,1), (N,1), (1,1), (1,N), (1,N) for the centres h, m, h′, s, c ✓. Laurent claim ✓ (m = h/c + 1/c,
  s = N/h + c/h, h′ = N/c + N/(ch) + 1/h). "Mod 4 non-forcing (PROVED)" is a meta-statement without a defined notion of
  "dynamical statement … can force"; the correct precise content is: for every k, N ↦ (integral orbits at N mod 2^k)
  cannot be a function of N mod 2^k with a forced 0-mod-4 term, because at N = M² no orbit has one (Cor 1.4) while N ≡ M²
  (mod 2^k) contains primes with −1 words. Relabel as Assessment or state precisely (D13).
  *Upgrade available:* the hexagon "(0⁶) ⇒ some quiddity ≡ 0 (4)" (EVIDENCE in the memo) is PROVED by the tree picture of
  §2: all six quiddities even ⇒ the ends V₁, V₃, V₅ leave v₀ by one edge (to a vertex a), and a has only two further
  neighbours, so two of the three ends share a second edge ⇒ their determinant (a quiddity q₂, q₄ or q₆) ≡ 0 (4).
* **Coefficients model.** Count formula #F(N) = Σ_m #{h | mN+1 : h ≡ −1 (m), (mN+1)/h ≡ −1 (m)} re-derived
  (h = cm − 1, h′ = ms − 1, hh′ = mN + 1) and the values at primes 5…37 (11, 13, 17, 15, 19, 21, 25, 25, 23, 19) reproduced
  both by direct word count and by the divisor formula ✓. Props 1–2 are relabelling/dictionary (as the memo itself
  says); Prop 3 is correctly labelled Assessment. Nothing overclaimed.
**Verdicts:** parity involution SOUND-AFTER-REPAIRS (p = 3; Lemma 1 scope); Zamolodchikov SOUND-AFTER-REPAIRS (label);
coefficients model SOUND.

## Claim 8 — literature and novelty
* **Cuntz–Holm–Jørgensen**, *Frieze patterns with coefficients*, arXiv:1909.02332, Forum Math. Sigma 8 (2020) e17 —
  authors, title, journal verified via the arXiv API; the abstract has "cutting out subpolygons" and the realisability
  question ("which frieze patterns with coefficients can be obtained in this way … solve this problem completely for
  triangles") ✓. The Zamolodchikov memo's "CHJ Prop. on glide symmetry" is CHJ **Theorem 2.11** (PDF read) (D14).
* **SVZ** arXiv:2312.12953 — verified in the PDF (Claim 5).
* **Böhmler–Cuntz** arXiv:2407.12596 (*Frieze patterns over finite commutative local rings*) and **Morier-Genoud–Ovsienko**
  arXiv:1811.01229 (*Farey boat I*) — titles/authors verified via the arXiv API ✓.
* **Guo**, *On tropical friezes associated with Dynkin diagrams* — exists, arXiv:1201.1805 ✓ (IMRN 2013 journal data not
  verified). Caution (D14): Guo's tropical friezes satisfy the max-plus exchange relation *with equality*; the 2-adic
  valuation pattern of an integral frieze is NOT such an object (e.g. q₁q₂ = N + q₄ with q₄ odd gives
  v₂(q₁) + v₂(q₂) ≥ 1 > 0 = min(v₂N, v₂q₄)). Only the four-point (ultrametric) condition holds, as the memo correctly says;
  the citation should be "cf." not an identification. Also y2_even_edge's pointer to a memo "y2_tropical_2adic" is
  dangling — the memo is y2_twoadic_tree_transport (D14).
* **Beardon–Hockman–Short**, *Geodesic continued fractions*, Michigan Math. J. 61 (2012) 133–150 — bibliographic data
  verified by web search (Project Euclid / ORO); content not read; nothing depends on it.
* **Musiker–Schiffler–Williams**, *Positivity for cluster algebras from surfaces*, arXiv:0906.0748 (Adv. Math. 2011) ✓
  exists; used only for the classical "frieze entry = number of perfect matchings of a snake graph", which is standard.
* **Novelty of Thm 1.2** — see Claim 2′/D1: the statement for all words and all odd N is MODEL_SPECIFIC Thm 3.1(a) and
  DISCOVERIES (J)33 already records CHI_FLIP as "a citation-free proof of the mod-8 sign law of (J)9 / (J)32". What the
  even-edge proof adds over CHI_FLIP is: no Hilbert-reciprocity-for-ternary-forms machinery and **no cell enumeration**
  (CHI_FLIP still identifies the χ = −1 cells with the 4-slices by enumerating 320 cells).
* **Missed corollary (positive, D15).** Thm 1.2 + Cor 1.3 show that χ = (−h′/N) is a function of (c, m, s) **mod 4**
  (8 | ee′ ⟺ some q_i ≡ 0 (4), and N, q_i mod 4 are functions of the letters mod 4). Checked: on all odd-N words with
  letters < 80, χ is constant on each of the 40 odd-N cells mod 4 (30 cells with χ = −1). So "the period is 8"
  (CHI_FLIP Cor 1.2) and DK's 512-cell/mod-8 framing are not sharp: 8 is a period, 4 is the minimal one. Likewise §0 (I1)
  "it must be 2-adic of depth 3" is misleading — the sign is the mod-4 spur property (depth 2 on one cherry), cf. y2_farey
  "(h′/N) = −1 ⟺ the mod-4 walk has a spur". The 80 classes per N mod 8 of y2_lift8 are correct (my count: 80 each).
**Verdict: GAP on novelty (D1), citations otherwise SOUND with minor fixes (D14).**

## Numbered defects

**No FATAL defects.** Every mathematical theorem labelled PROVED re-derives; every numerical claim I re-ran from scratch
reproduces exactly.

**D1 (MAJOR, novelty overclaim).** FRIEZE_ES §1 Remark ("this gives a 3-case proof of DK Thm 4.5 and extends it to formal
words and to N ≡ 3 (4)"), §6 verdict bullet 1, memo y2_even_edge Theorem 2 / Assessment ("extends that equivalence to formal
words and to N ≡ 3 (4)"), AGENT_REPORT SHARP 1. The extension is MODEL_SPECIFIC Thm 3.1(a) ((J)32), which already covers
all words incl. boundary words and all odd n, and CHI_FLIP gives an enumeration-light proof ((J)33: "citation-free proof
of the mod-8 sign law of (J)9 / (J)32"). *Repair:* say "a short, computation-free proof of MODEL_SPECIFIC Thm 3.1(a)
(= DK Thm 4.5 for interior words, N ≡ 1 (4)); new are Lemma 1.1 (the even edge) and the proof".

**D2 (MINOR, typo).** §1 Case B step 7: "Otherwise b = v₂(c) = 1" → "Otherwise v₂(h′) = v₂(c) = 1, so b = 1".

**D3 (MINOR, proof presentation).** §2 / memo y2_twoadic_tree_transport Thm 2 "Proof": σ, τ undefined. Replace by the
two-line derivation in Claim 3 above (Case A: (c/h) = (2/h); Cases B, C: (2/(No))^{b−1} = 1 because b ≥ 2 forces
No ≡ 7 (8)).

**D4 (MINOR, wording).** §2 / AGENT_REPORT SHARP 2: "the character of 2 at the *small* modulus o" — o can be h or h′,
of size ≍ N. Say "at the opposite vertex o".

**D5 (MAJOR, label).** §3 header "PROVED by inspection" and the bolded "Any frieze-theoretic ES proof must use the
positivity of the frieze archimedeanly" (also AGENT_REPORT SHARP 3 "Steering rule"). The last is an Assessment (undefined
notion of "frieze-theoretic proof"), and the archimedean reading is CHI_FLIP Thm 1.1's (ε_∞ = −1 by positive definiteness;
(J)13, (J)33). *Repair:* split into (a) PROVED: positivity is necessary — explicit signed family (D6); (b) inspection:
this proof uses positivity only in reciprocity steps; (c) Assessment: the steering rule; cite CHI_FLIP Thm 1.1.

**D6 (MINOR, upgrade).** §3 / memo y2_positivity_is_T1: "signed friezes at odd squares have zero-mod-4 quiddities"
is EVIDENCE (box search) but PROVED by the family (4, −(M² + 3)/4, −1) at N = M².

**D7 (MINOR, precision).** y2_farey_complex_lifting: SVZ Thm 1.6 is for *semiregular* friezes; at N ≡ 3 (4) the mod-4
pentagon has boundary entry −1 and must be normalised first (SVZ §1). Also §3 bullet 2 / memo "finite-ring frieze theory
is N-blind beyond N mod 8" is literally false (it sees N mod n); replace by "a criterion depending on N only through
N mod n cannot separate odd squares from primes ≡ M² (mod n) (Dirichlet), hence cannot force a −1 word (Cor 1.4)".

**D8 (MAJOR-positive, conjecture is a theorem).** §4 "CONJECTURE: the same holds for all r ≥ 4 (EVIDENCE: r ≤ 12)",
"(for r ≤ 12 and r ≡ 0 (4); CONJECTURE beyond)", AGENT_REPORT SHARP 4 and Spark 1. PROVED for all r ≥ 5 by the word
(2, 2, 2, 4, 2^{r−5}, k) at N = (2Q + 3)², Q = 9(r − 5) + 13 (Claim 6). Replace the CONJECTURE by this family.

**D9 (MINOR, definition).** §4: define "the zero locus is a Jacobi fibre" (suggest: among interior length-r words at
N ≡ 1 (4), {some q_i ≡ 0 (4)} = {(A/N) = −1}); note that witnesses at squares refute "⊆ {−1}"; r = 2 is "≠" because
its zero locus is empty while the −1 fibre is not.

**D10 (MINOR, label/accuracy).** Thm 4.1: "hs = N + 4w" holds only for c = 4w (m = 4w: hh′ = 1 + 4wN; s = 4w: ch′ = N + 4w);
memo's "product = N + const" likewise. "Leaves a divisor event" is not a mathematical predicate: PROVED part = piece
identification + "(4), (2,2,2) are the only interior words at 4"; the B2 reading is Assessment.

**D11 (MINOR, numerics text).** y2_hexagon_degeneration Cheap numerics: r = 3 non-square failures are
3, 5, 7, 11, 15, 23, 27, 35, 39, 55, 99, 105, 119 — "N ≡ 3 (4) cases and 105" omits N = 5.

**D12 (MINOR).** y2_parity_involution Lemma 2: the fixed point is unique for primes p ≠ 3 (p = 3 has (1,5,1) and (3,1,3)).
Lemma 1's PROVED content is "no Vieta involution; the only dihedral symmetry fixing the N-side is the reflection"; the
Iteration's "the only involutions are the dihedral ones" / AGENT_REPORT "the only involution is the reflection" is not
proved (Assessment).

**D13 (MINOR, label).** y2_zamolodchikov_forcing "Mod 4 non-forcing (PROVED)" — a meta-statement; state precisely or
label Assessment. Optional upgrade: hexagon pattern (0⁶) ⇒ a quiddity ≡ 0 (4) is PROVED by the Bruhat–Tits pigeonhole
(Claim 7; checked on 11 575 words N ≤ 3000, `scripts/review_r208_hex06.py`).

**D14 (MINOR, citations).** CHJ glide symmetry is Theorem 2.11; Guo's tropical friezes are "cf." (the 2-adic valuation
pattern is not a tropical frieze); y2_even_edge cites a non-existent memo "y2_tropical_2adic"; Cor 1.4 square-control count
8 068 excludes N = 1 (5 words) — say so.

**D15 (MINOR, missed sharpening).** Thm 1.2 implies χ is a function of (c, m, s) mod 4 (40 odd-N cells, 30 with χ = −1); the
§0 (I1) "must be 2-adic of depth 3" should read "a mod-4 (spur) property that is not a homotopy invariant". Worth one
sentence in §1 (and a pointer for CHI_FLIP Cor 1.2's "the period is 8": 4 is the minimal period).
