# AGENT_REPORT_O207 — TORSION_FIRING (wave Y-d): ES firing as point orders on CM supersingular curves

Branch `side-agent/torsion-firing`; main file `TORSION_FIRING.md`; scripts `scripts/tf_*`; data `data/tf/`.
**ES is not proved, nor any infinite case.** Outcome: the fallback (a scoped no-go for the GL₂ point-order class),
three exact dictionaries, and two numerical facts. Self-reviewed by a deep reviewer subagent (1 FATAL, 3 MAJOR,
minors — all repaired in place, marked "R-O207 repair"; no numerical headline refuted, reviewer reproduced them).

## SHARP:
(R206 repair note: hostile review reviews/torsion-firing-review.md — no FATAL; SHARP 1 holds only for
supersingular-at-f data and the "≤ |Box(k)|" bound is FMS Thm 3.1 for any rule, so it is not a no-go for a GL₂ mute
analogue (D3); SHARP 2 reproduced independently and extended to 10⁸; SHARP 3 is a restatement of divisor conditions
on p + 1 − a — the elliptic curve enters only through its order (D7); Prop 3.3 proved for D = 1 only (D5).)
1. **Torsion–residue orthogonality (Thm 3.1, PROVED, elementary).** Every homomorphism from a group of exponent
   dividing h^s + 1 (supersingular points E(F_{h^s}), the non-split torus, Weil-pairing values) into F_{h^t}^*
   (t odd) has image ⊆ {±1}. The ES divisors live in the (h+1)-world (orders in E(F_h) / T(F_h)), p lives in the
   (h−1)-world (F_h^*); gcd = 2 is exactly the genus layer. Hence the GL₂ analogue of the FF_MUTE mute place
   ("f.g. group of points reduced mod f") amplifies a firing set by at most a factor 2 (Cor 3.2), whereas ⟨s mod f⟩
   in FF_MUTE lives in the same group as p. The only bridges between the two worlds are non-homomorphic
   (integer order ↦ residue: the box; or coordinates: Prop 1.2(b)), i.e. archimedean size conditions.
2. **p = 3361 is the unique prime ≤ 10⁷ with no PRIME-modulus Type II certificate** (exhaustive, tf_primemod.c;
   its 4 ordered certificates have moduli 99, 679, 1159, 33639). Any "supersingular reduction at one prime" route
   to Type II must also handle composite moduli (or Type I).
3. **Hasse-window dictionary at p itself (Props 4.2/4.3, PROVED via Deuring–Waterhouse; EVIDENCE to 10⁸).**
   Type II certificates with j = 1 (resp. small slices 4c²d ≤ 2√p + 1) ⟺ an elliptic curve E/F_p of trace
   a = 1 − c (resp. 1 − 4c²d) has a subgroup of order ≡ −1 (mod 4(1 − a)) (resp. mod (1 − a)/c). The Hasse
   bound costs nothing on the j = 1 face (it is the divisor-pairing bound). Every prime 5 ≤ p ≤ 10⁸ has such a
   witness (the j=1 face misses only 23 primes, the small-slice window only p = 193, never both); odd squares: none.
   So all ES tickets of these kinds are point counts over the single field F_p — a possible home for the (J)35
   isogeny-graph line.

## Results (labels as in the file)
* §1 (PROVED, checked: 1994 group-structure cases, 162 095 (n, h) pairs, 0 mismatches). Group structure of
  y² = x³ + Dx at h ≡ 3 (4) and y² = x³ + B at h ≡ 2 (3). Type II at prime h ⟺ y² = x³ + pd·x has a 2-torsion
  point (x_T, 0) with 2d | x_T, 2x_T | h + 1 (c = x_T/2d) ⟺ cd | #2E_0(F_h) and h | p + 4c²d.
* §2 (PROVED). At a supersingular h, for ANY E and odd ℓ ≠ h, ρ_{ℓ^∞}(Frob_h) ~ companion matrix of x² + h: every
  GL₂-invariant torsion condition at odd ℓ is cyclotomic (2-adic part keeps the E[2^∞] datum). Per modulus, firing
  reads only det = N(π_p) of the CM Frobenius of p on E_0[h] (Prop 2.3).
* §3. Identity forcing of point orders (families over ℚ(t)) serves finitely many slices — Merel/Mazur (Prop 3.3,
  4cd ∈ {4, 8, 12} over ℚ(t)) and Kronecker for Lucas/torus (Prop 3.5, 4cd = 4). Profinite (J)34 extension
  (Prop 3.4, towers unramified outside a finite set): sufficient conditions need empty interior (measure 0 if
  Jordan-measurable); positive-measure sufficient C exist but no equidistribution theorem can hit them without
  hitting infinitely many primes. Iwasawa: anticyclotomic towers split inert primes completely; cyclotomic and CM
  division towers see h only mod ℓ^∞. Density-zero mechanisms screened (Elkies, primitive divisors, sign):
  identities or one quadratic sign (Assessment that the list is exhaustive).
* §5. T1 inside the dictionary = non-cyclicity condition (n/h) = −1 of E_{nd}(F_h) (known genus obstruction,
  translated). Barrier table: B1/B2(iii) for identities, B2 for the integer x_T | (h+1)/2, B3 for the Hasse lottery.

## Which (J)34 hypothesis the task asked to violate, and what happened
(J)34 Prop 1.2 needs L finite. In towers the escape forces int C = ∅ (Prop 3.4), so existence must be density-zero;
every density-zero mechanism found is an identity (bounded by uniform boundedness / Kronecker) or a quadratic sign.
The GL₂ (non-abelian) structure adds nothing at supersingular primes (Prop 2.1) and cannot be transported to p's
residue (Thm 3.1).

## Sparks (not pursued)
1. **Type I dual Hasse dictionary.** For a Type I modulus f ≥ (p − 1)²/4 (f | p² + 4c²d, f ≡ −p mod 4cd), f + p =
   #E(F_f) for curves of trace 1 − p, so Type I firing ⟺ 4cd | #E(F_f); and √−d ≡ p/(2c) mod f makes f split in
   ℚ(√−d) (ordinary CM by ℚ(√−d)). Check what fraction of Type I moduli lie in this window and whether the CM-by-
   ℚ(√−d) curve's Frobenius π_f relates to p + 2c√−d.
2. **Is 3361 the last prime without a prime-modulus Type II certificate?** Count prime-modulus certificates
   (all ranges of h, not only h ≤ P) and their growth (expect ≍ log² p); if so, "prime-modulus Type II" is a
   clean sub-conjecture with one exception, and the supersingular dictionary covers it.
3. **Hasse-window curves in the (J)35 isogeny graph.** All j = 1 tickets are F_p-curves of traces a ∈ [−2√p, 0];
   ask whether the curves whose group has a subgroup of order ≡ −1 (mod 4(1 − a)) cluster in the ℓ-isogeny volcanoes
   (ℓ | 1 − a), i.e. whether "order ≡ −1 mod 4(1−a)" is an End-module (volcano-level) property for some ℓ.
4. The 2-adic Frobenius class at supersingular h (the one part not collapsed by Prop 2.1) vs v₂(h + 1): ES needs
   only 4 | h + 1, so probably nothing, but it is the only non-cyclotomic GL₂ datum left at h.
