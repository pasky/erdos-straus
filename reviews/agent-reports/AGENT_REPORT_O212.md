# AGENT_REPORT_O212 — Spark relay Y4: hunting 4-specific inputs (branch side-agent/four-specific)

Deliverables: `FOUR_SPECIFIC.md` (deep file), 6 memos `BRAINSTORM/y4_*.md` (indexed), scripts `scripts/y4_*`
(all ≤ a few minutes; y4_oddslice.c to 10⁷ took ~1 min). ES is not solved; no infinite case of ES is claimed.

## SHARP:
1. **T1-bearing numerators = discriminants (FOUR_SPECIFIC Prop 1.1, PROVED).** The M-shot family (g | n + MQ²,
   g ≡ −1 mod M, odd g) has T1 ⟺ M ≡ 0, 3 (mod 4), i.e. ⟺ −M is a discriminant (χ_{−M} has conductor | M). M^□ is a
   theorem at all non-squares for every M. **7 is the non-trivial T1-bearing, failure-free sibling of 4**, and it has
   none of 4's slice/character structure (S₇(p) = ∅ at 10 primes; not a function of simple Jacobi data). Every
   "4-specific" proposal should now be run against 7 as well as 8. New harness entry: 11/37 = 1/8 + 1/148 + 49/296.
2. **Certificates of a fixed n are 2-adically indistinguishable (Thm 2.3, PROVED relative to the 2-adic symbol
   classification).** Every χ = −1 path form satisfies Q_w ⊗ ℤ₂ ≅ ⟨1, −1, −n⟩. The one-odd vs all-even (= 8/n) split of the
   certificates is v₂ of a "pentagon quantity" (Q(e_i) or a det of adjacent planes: ≡ 4 vs ≡ 0 mod 8), so it is marking
   data, not lattice data. S₄^{odd}(p) ≠ ∅ for all primes ≤ 10⁷ while S₈ fails 27 times (same 140/240 cell size).
3. **Mordell's 840 is exactly the reach of universal one-slot χ-witnesses (Thm 4.2, PROVED).** The non-square A for
   which "(−A/p) = −1 ⇒ p has a word with slot A" (p ≡ 1 mod 4) are exactly {2, 3, 5, 7, 8, 15, 20}, because
   τ(A+1) ≥ φ(A)/2 is needed. Their reach is the complement of Mordell's six square classes. Checked to 10⁶.
4. **4 is the unique M ≥ 3 with a slice e ∈ {1, 3} ((ℤ/e)^* = {±1}) at every prime (Prop 3.1, PROVED).** For ES the
   e = 3 slices are non-triviality events, not hitting events. Both e = 3 slices are still empty for 9.1% of p ≡ 1 (12) < 10⁶.

## Results by goal
(a) Catalogue (y4_catalogue, FOUR_SPECIFIC §7): the only 4-specific fact with input character is still the χ-fibre /
2-adic isotropy ((J)32/(J)33, i.e. SQ₅). The rest are descriptions (one-odd, Mordell, e ≤ 3) or not 4-specific (T1).
(b) One-odd half: Lemma (parity = v₂ of slot), cells 100/100/40, Thm 2.3. Census: S₄^{odd} ≠ ∅ at primes ≤ 10⁷. False at
composites 321, 4545, 5481, 8745, 9121, 13041, 25305, 57481, 169425 (≤ 2·10⁵). One-odd ES to 10⁶ reproduced. The 8/p
failures all sit in p ≡ 1, 3 (mod 8), where 8 has no e ≤ 3 slice. Verdict: description, strictly harder than SQ₅.
(c) Numerators: Prop 1.1 / Cor 1.2 and the 7-control (y4_t1_numerators, y4_seven_control).
(d) Harness on hatches (y4_harness_hatches): all MIXED (uniform skeleton + lottery). Uniform H-F ("BM-only for all
m/n") is false. Only SQ₅/χ-flip passes as a stated 4-specific input.

## Labels / caveats for the reviewer
* Thm 2.3 cites the 2-adic symbol classification (Conway–Sloane SPLAG Ch. 15 / O'Meara §93) from memory. The argument
  (an isotropic unimodular ternary splits a unimodular plane of oddity 0) should be checked. Numerical oddity
  cross-check: n ≤ 401.
* Thm 4.2's tail bound uses Rosser–Schoenfeld φ(n) > n/(e^γ log log n + 3/log log n) (n ≥ 3), quoted from memory, and the
  image-size count (≥ φ(A)/2 residues) for even A. The finite part is the exact class check A ≤ 3000.
* The S₇ "no simple Jacobi refinement" is a finite feature test (n ≤ 601), not a theorem.
* "Failures avoid e = 3 classes" (FOUR_SPECIFIC §3.3) is EVIDENCE with an independence-based Assessment only.
* After the orchestrator's FYI, 11/3 was dropped as a harness entry (11/3 > 3 is trivial). BM was not computed for 11/37.
* The research subagent did the hatch survey (goal d). I re-read Rem 10.4 and the H-E statement myself, and the verdicts
  are mine.

## Sparks (not pursued)
1. **7/n's own input.** Find any structure that is true for 7 and false for 11 (both T1-bearing), e.g. a 7-adic analogue
   of (J)33 (is some slice set of 7/n a 7-adic isotropy fibre of a twisted form?).
2. **Marked 2-adic flip.** By Thm 2.3 a χ-flip cannot be detected 2-adically on the lattice. Look for flips on *marked*
   lattices: moves that change which pentagon quantity carries the factor 4, e.g. via the Gauss pentagram recurrence on
   (v, A*, t, A, u).
3. **e = 3 double-failure primes** (241, 409, 769, …, 9%): characterise which slice then fires first (t ≤ 7?), and test
   whether the double failure is exactly "p is a cube residue pattern" (both N ≡ 1 mod 3 with only primes ≡ 1 mod 3: a
   condition in ℚ(ω)). That could link to the TES order-3 picture.
4. Prove or refute: the S₄^{odd}-empty composites are exactly n with a specific factorisation pattern (321 = 3·107,
   9121 = 7·1303; most are divisible by 3).
5. Two-slot universal witnesses: pairs (A, A′) covering their joint χ classes. Is the reach still exactly 840 (B1
   predicts a finite level)?
