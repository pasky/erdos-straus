# z31 — Zaremba, thin orbits, continued fractions (O261 field memo 1; DEEP item)

Labels as in DISCOVERIES.md. Sources read by me (O261) are in `sources/lit2026g/` (zaremba_bk.txt, shkredov_zaremba2026.txt,
zhang_zaremba2026.txt, moshchevitin_shkredov.txt). Builds on BRAINSTORM/thin_group_orbits.md, farey_ford_cf.md and
DEDEKIND_ES.md §5.3 (critical exponent 2δ = 1), which already had the scale argument; **new here: the 2026 pointwise
Zaremba theorems (Shkredov; X. Zhang), which the campaign had not seen, and an exact account of why their mechanism needs F2.**

## (a) Counterpart statement and the exact dictionary

* **Zaremba(M):** for every q ≥ 1 there is a, gcd(a, q) = 1, with all partial quotients of a/q at most M.
* **ES-five(p)** (the five X/e-slices of ES; DEDEKIND_ES Cor 4.6, PROVED): for a prime p ≡ 1 (8),
  ES-five(p) ⟺ λ(p) ≤ 3, where λ(p) = min{HJ-length of p/A : (A/p) = −1} and the HJ length is 1 + Σ_{i odd} a_i of the
  regular CF (R169 convention). I.e. **some quadratic non-residue A mod p has p/A with its odd-position partial quotients
  summing to ≤ 2; the even-position quotients are free.** (Type II proper adds the analogous "(★)" slices, PARITY_AUDIT §0.)
* So both are "∃ numerator mod a fixed denominator whose CF lies in a prescribed digit set", and ES adds a quadratic
  character condition (F6). The digit sets are opposite: Zaremba = *long words in a bounded alphabet* (a Cantor set of
  Hausdorff dimension w_M = 1 − 6/(π²M) + O(log M/M²), Hensley; Shkredov 2026 Thm 12); ES-five = *short words (HJ length
  3) with unbounded letters* — a set of dimension 0 whose count up to X is ≍ X log² X, i.e. **critical exponent 2δ = 1**
  (DEDEKIND_ES §5.3, Assessment): ≍ log² p representations per p, matching F2.

## (b) Is the counterpart proved pointwise? By what mechanism?

1. **Bourgain–Kontorovich, Ann. Math. 180 (2014), arXiv:1107.3776** (read): Thm 1.8 — if δ_A > δ₀ then D_A contains almost
   every admissible integer, #(D_A ∩ [N/2, N])/#(admissible ∩ [N/2, N]) = 1 + O(N^{−c/log log N}); each such d has
   multiplicity ≫ N^{2δ_A − 1001/1000}. The main term is S(d)·Π_N(d) with Π_N(d) ≍ N^{2δ−1}. They state (p. 8): pointwise
   control |E_N(d)| ≪ N^{2δ−1−ε} "would conclude the full Conjecture 1.7. We are not able to establish control of this quality
   individually, but do succeed on average" ((1.37), an L² bound). Mechanism: thin-semigroup circle method, major arcs by
   Lalley renewal + Bourgain–Gamburd–Sarnak / Bourgain–Varjú congruence expansion, minor arcs bilinear. **Almost all.**
   Huang (GAFA 2015, arXiv:1310.3772): same with M = 5 (research-agent read; abstract-level).
2. **Moshchevitin–Shkredov, Pacific J. Math 309 (2020), arXiv:1911.07487** (abstract-level, read by research agent): for
   every prime p there is q ≡ 0 (mod p), q = O(p^{30}), with a Zaremba numerator (bounded M). Pointwise, but for a
   *multiple* of p — the classic "fixed modulus" relaxation.
3. **Shkredov, arXiv:2603.14116v2 (June 2026) — PREPRINT** (read pp. 1–8): Cor 1 — "There is an absolute constant M ≥ 2 such
   that for any prime (or square–free) number p there exists a, (a, p) = 1" with all partial quotients ≤ M. Thm 8: for all
   M ≥ M₀ and q in a positive-density set Z ⊇ {sufficiently large primes}, at least **q^{2w_M − 1 − o(1)}** numerators with
   digits ≤ 100M (and a separate lower bound q^{1−O(1/M)}). Mechanism: Moshchevitin's Cantor/Ahlfors–David structure of the
   Zaremba set in ℤ/qℤ (Lemma 13: Z_M(t) is a disjoint union of ≍ t^{2w_M} intervals of length ≥ q/t²), "critical
   denominators" of convergents near √q, and growth in SL₂(ℤ/qℤ) (Helfgott triple-product, Bourgain–Gamburd machine). The
   author notes the method would need only uniform distribution of A^{−1} for A ⊆ ℤ/qℤ a union of intervals of length
   q^{1/9−o(1)} ("much smaller than the square–root barrier 1/2").
4. **X. Zhang, arXiv:2605.02518v2 (May 2026) — PREPRINT** (read pp. 1–2): "Theorem 1.2. Zaremba's conjecture holds" (with
   some large, effectively computable M), by a new growth theory in SL₂(ℤ/qℤ) for general q (Thms 2.1, 2.2, 2.4) plugged into
   Shkredov's Thm 8 framework. Remark 1.4: Bourgain–Varjú's spectral gap is insufficient because the generating set depends
   on q, |S| ≈ q^{2τ}.
   *Status:* both are unrefereed preprints of 2026; I did not check the proofs. If correct, **Zaremba (large absolute M) is a
   POINTWISE theorem** — exactly the kind of non-averaged mechanism the brief asked about.
5. Korobov 1960 (quoted in Shkredov p. 2, Zhang p. 1): every q has a with M(a) ≪ log q — pointwise by exponential sums
   (counting with a power main term once M ≍ log q).

## (c) Does the mechanism apply to B2? Exactly which feature blocks it

The pointwise step in Shkredov/Zhang is: *a congruence modulo the fixed denominator q between two large structured sets*
(numerators whose CF begins in the Cantor set, inverses of those whose CF ends in it), solved by growth/expansion in
SL₂(ℤ/qℤ). Three inputs are essential, and B2 lacks each:
* **Power-size sets (F2).** The two half-sets have ≍ (√q)^{2w_M} = q^{w_M} elements; their "gluing" congruence has expected
  count q^{2w_M−1} → q^{1−O(1/M)}. Shkredov buys this by taking M large (w_M → 1). In ES the alphabet cannot be enlarged: the
  ES digit set is fixed at HJ length 3 (dimension 0), so the halves have p^{o(1)} elements and the gluing count is ≍ log² p.
  Growth theorems (Helfgott/BG) need sets of size ≥ q^{ε}; a set of size polylog in ℤ/pℤ has no growth input at all.
  BLOCKED by F2 — not merely quantitatively: the ES digit set has no "M" knob (DEDEKIND_ES Cor 4.6: longer HJ words are
  not ES certificates).
* **Fixed modulus (F3).** In Zaremba the gluing congruence is mod q and the exact denominator is automatic (a ∈ [1, q)). In the
  ES hyperbola form (E5) the exact height c = (Xε − u)/p is part of the target class X ≡ −1 (mod 4cu); in the CF form the
  modulus is fixed (p), but the price is that the admissible set is a finite-length word set — F3 has been traded for F2.
  (This trade is exactly SYNTHESIS_SPARKS8 Prop 1.4: linearising the Farey least-residue returns the window form.)
* **Character condition (F6).** ES-five also needs (A/p) = −1. With a power-size Zaremba set this would be cheap (a set of
  size q^{1−ε} cannot lie in the residues for structural reasons once it equidistributes in cosets); with a polylog set it is
  the whole problem (T1: at squares the condition is void).
So the Shkredov–Zhang mechanism transfers to **"ES with a Zaremba-sized menu"** — e.g. ES-type statements whose certificate
set at p has dimension > 1/2 — but no such menu is ES: every ES certificate set is a d₃-size divisor sum (critical).

**Sharp check of the brief's question ("Zaremba is a pointwise problem with polylog-ish counts").** It is not: at fixed M the
per-q count is q^{2w_M − 1} (power; for M = 5, w_5 > 5/6 (BK p. 6, citing Jenkinson), so ≥ q^{2/3}). The polylog regime
is δ = 1/2 exactly, and **no thin-orbit local–global theorem at δ = 1/2 is known** (research agent found none; BK's own
Conj 1.7 requires δ_A > 1/2; Hensley's δ > 1/2 conjecture was disproved by BK for congruence-obstructed alphabets).

## (d) Verdict: ANALOGUE (same shape "∃ numerator mod p with CF in a digit set", opposite digit regime).
Not EQUIVALENT, not INSTANCE. Transfer verdict: **NOT SHARP** for ES; **SHARP as a fact the campaign should record**: as of
2026 (preprints), Zaremba is claimed pointwise for all q by expansion — the first "every q" result in the thin-orbit family —
and the reason it does not reach ES is F2 (no alphabet knob at criticality), not F1.
