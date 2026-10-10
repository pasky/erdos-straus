# Red team 2 + synthesis for the automorphic / geometric attack on pointwise ES (task O132)

Second, independent red team. Scope: (1) collapse tests T1–T8 (defined in
`reviews/redteam-automorphic.md` §4, merged here from branch `side-agent/redteam-automorphic`) applied to
O123 (`POINTWISE_SPECTRAL.md`), O128 (`POINTWISE_TYPEII_SPECTRAL.md`), O131 (`EXACT_FORMULA.md`) and O130
(`QUATERNION_ES.md`, merged from `side-agent/quaternion-es`); second-reviewer audit of the headline negative
conclusion; (2) a unifying "divisor-class reduction" statement with exact scope; (3) escape hatches.

Labels as in DISCOVERIES.md. Nothing here proves or disproves ES.

Notation. `n_p` least quadratic non-residue; `W(p)` least Type II witness modulus (notes (51.1)–(51.2));
X5 = the Ω-result `W(p) > exp(c(log p)^{1/4}(log log p)^{-1/4})` i.o.; `𝓛 = log p`.

## 1. Collapse tests on O123, O128, O131, O130

(in progress)

Overall: all four negative conclusions **survive** T1–T8. Two scope findings (one T3, one wording) and one
small T2 lemma are new; nothing is FATAL. Details per document, then a summary table (§1.5).

### 1.1 O123 (`POINTWISE_SPECTRAL.md`: SL₂/Heegner Type I at fixed p)

* **T1 PASS.** The step false at odd squares is named: the genus factor `1 + χ_{−4d}(−p)` (Lemma 2.4; exact
  identity in EXACT_FORMULA Thm 5.2(iii)).
* **T2 PASS (diagnosed by the author).** Single `(c,d)` targets have expectation ≍ L/(cd), > 1/2 for small cd, and
  Prop 5.3 empties any one of them i.o. under H. The verdict correctly demands aggregation.
* **T3 FINDING (new; scope of the illustrative sufficient statement).** §5's example of a sufficient hypothesis is
  `Σ_{d≤L²} #(T_p Heeg_d(−4d) ∩ ⋃_a R'_a) ≥ (1−o(1))M(p)`. For `p ≡ 1 (4)`, a Type I solution at level d needs
  `χ_{−4d}(−p) = 1`, i.e. `−(−d/p) = 1`, i.e. `(d/p) = −1`. So d has a prime factor `≥ n_p`, and the statement
  implies `n_p ≤ (log p)²` for all large `p ≡ 1 (4)`. Unconditionally only Burgess `n_p ≪ p^{1/(4√e)+ε}` is known;
  under GRH Bach gives `n_p < 2 log²p`, which does not even reach the constant 1. Same phenomenon as SHT
  (red team 1, Prop 7.2). Repair: anchor the level window at `n_p` (`d ≤ n_p·L^{O(1)}`) or say "under GRH, with
  `d ≤ 3L²`". This does not affect the verdict (the example is illustrative and not claimed).
* **T4 PASS** (automatic through the level: d carries the non-residue, as just shown).
* **T5** not binding (Type I). The Type I analogue (`ck_min ≫ log p·log₃p` i.o.) is respected: no lower bound at
  bounded height is claimed.
* **T6** x̂₉: the route sees fresh primes (high SL₂ points, TYPEI3 `f ≥ 10¹²`); no claim is affected.
* **T7 PASS, and the best item in O123.** Thm 5.1 uses the average over p only for an *upper* bound (Markov),
  correctly. Prop 5.4 (thickening by K/p = averaging the ET count over `|n−p| ≤ K`) is the exact form of the
  average leak, PROVED.
* **T8 PASS** (Prop 3.2: point-in-wedge ⟺ Type I, exact).
* **Wording (overclaim check).** Verdict reason 1 as first written ("every such hypothesis enters with a loss
  `X^ε`") was false for averaged GRH use; R123 repaired it by reduction to reason 2. Reason 2 ("even under
  Ramanujan + Lindelöf the Hecke-orbit spectral error exceeds the main term by ≈ p") is a statement about the
  Cauchy–Schwarz-over-the-spectrum *method*, not about the hypotheses. The only rigorous scale statements are
  Prop 5.4 and the observation that a smooth minorant of a tube of width ≍ 1/p must have Sobolev scale ≳ p.
  The ledger's "(Assessment) … by this route" is the right label; it must not be shortened to "no standard
  hypothesis suffices". Logically, if ES is true then every hypothesis implies it. The only meaningful negative
  statements are about *mechanisms*.

### 1.2 O128 (`POINTWISE_TYPEII_SPECTRAL.md`: Type II shells, level dp)

* **T1 PASS.** Lemma 6.1 `(p/f) = −1`, so the genus `χ_{−4d} = −1`. Prop 8.3 (Q₀ solves everything except the
  sign at ∞) shows precisely that the genus character is the only locally forced restriction.
* **T2 (small new lemma; the Type II twin of O123 Prop 5.3).**
  **Lemma 1.2.1 (CONDITIONAL on Dickson's conjecture for two linear forms).** For every fixed `(c,d)` there are
  infinitely many primes p for which the `(c,d)` shell piece is empty, although its mean is `≍ log p/φ(4cd)`.
  *Proof.* The piece counts divisors `f ≡ −1 (mod 4cd)` of `4c²dp + 1` (O128 Prop 8.1). The pair `X, 4c²dX + 1` has
  no fixed prime divisor: for ℓ = 2 the second form is odd; for odd `ℓ | 4c²d` it is `≡ 1`; for odd `ℓ ∤ 4c²d`, at
  most 2 of the `ℓ ≥ 3` residues are excluded. Dickson then gives infinitely many p with `4c²dp + 1` prime. Its only
  divisors 1 and `4c²dp + 1` are `≡ 1 (mod 4cd)`, and `1 ≢ −1` since `4cd ≥ 4`. ∎
  O128 reports this numerically (§5, §10: the whole d = 1 family is empty for 135–198 primes per block) but states
  no lemma. With the lemma, every fixed finite union of shells is excluded *as a target* only under H (finitely many
  polynomials at once; the fixed-prime-divisor condition must be checked for the family). So the sufficient
  statement must aggregate over a growing set of `(c,d)`, as (TS) does.
* **T3 PASS.** (TS) allows `c, d ≤ p^{o(1)}`, with no bound on the witness f. Prop 6.2 of red team 1 and X5 force
  `f ≥ W(p)` i.o. large, which is compatible with (TS) since `f | 4c²dp+1` may be large. No claim is made below
  `log T ≍ 𝓛^{1/4}`.
* **T4 PASS** via `(p/f) = −1` (Lemma 6.1 = Lemma CT for Type II).
* **T5 PASS (nothing claimed).** On the X5 fibre, the count of Type II solutions with `f ≤ T` is 0. The exact
  Eisenstein expansions (Props 9.1–9.2) are identities, not main terms, so they are not contradicted. Any
  *truncated* shell count with a low-conductor main term would be. O128 makes no truncated claim.
* **T6** not binding: Type II, and x̂₉ has `W = 7`.
* **T7 PASS.** §3 shows that the average over p collapses the incidence into BV/BT. The author flags this as an
  average, not a pointwise tool.
* **T8 PASS** (Prop 8.1 exact; the lift is the divisor).
* **Overclaim check.** "No existing or GLH-conditional equidistribution theorem reaches (TS)" is a bookkeeping
  Assessment. It is correctly hedged (D7/D8: not a proof that no L-function input could work). "Cancellation
  across ≍ |D| spectral terms, beyond GLH" is the correct *mechanistic* reading, since GLH bounds terms
  individually. The summary claim "**No automorphic pointwise route** comes out of this structure" (§0, §9) should
  carry "(Assessment)" inline, as it does in the ledger.

### 1.3 O131 (`EXACT_FORMULA.md`: exact identities, CM torus)

* **T1 PASS.** T2⁺(m²) = 0 (Prop 2.1). Thm 5.2(iii) gives the genus factor as an exact identity.
* **T2/T3/T5/T6** not applicable: no counting lower bound is claimed.
* **T7 PASS, explicitly.** §5.3: class-group structure appears only in averages over p (the small-norm bias).
* **T8** n/a.
* **Overclaim check.** Thm 5.2 is PROVED and is the cleanest statement in the whole wave. Within one `(c,d)` slice,
  non-genus class-group characters have coefficient exactly 0. Scope: Thm 5.2 is per slice. The slice parameters
  `(c,d)` are coordinates of the solution, so summing over slices is again a divisor-in-class event, now with a
  moving modulus (§3 below). The rank test (CERTIFIED) is correctly scoped to the 54-column dictionary
  (R131 repair). §5.4 (Brandt / weight 3/2 not computed beyond round 1) is correctly an Assessment.

### 1.4 O130 (`QUATERNION_ES.md`: GZ x = 2 collision, (−d,−p) factorisation)

* **T1 PASS** (§4: both dictionaries fail at odd squares through genus characters).
* **T2** n/a (no count claimed). Prop 2.2 is the decisive fact: for admissible `(d,e)` the collision is
  *automatic*, and all the content is a divisor of `m = (pe+1)/4d` in the classes `±√−m (mod e)`.
* **T3 PASS.** Type I collisions need `(−d/p) = −1`, so `d ≥ n_p` for `p ≡ 1 (4)`. Type II has no
  level constraint, consistent with X5 (the witness f is a different coordinate).
* **T4 PASS** (through d for Type I, through `(p/f) = −1` for Type II).
* **T7 PASS, and a clean instance.** The class-number size of the full GZ/GKZ quantity comes from summing over
  the GZ parameter x (`≍ √(dm)` values). The ES problem fixes x = 2. This is exactly "an average over a parameter
  that the pointwise statement fixes" (Prop 5.1).
* **T8 PASS** (Prop 2.1 exact).
* **Minor proof gap (new; trivially repaired).** Prop 1.3's ramification step "at p: `(−d,−dpe)_p = (−d/p)`" needs
  `v_p(dpe)` odd, i.e. `p ∤ e` (if `v_p(e)` were odd, B would split at p). This holds: `e | 4a²d + 1`
  (Lemma 1.1), so `p | e` would give `(−d/p) = +1`, contradicting `(−d/p) = −1` (GEOMETRY_ES Prop 5.1). Insert
  the line. Sanity check `scripts/rt2_pdivides_e.py` (p < 60, a, d < 4p): no Type I solution has `p | e`.
* **Prop 5.1** "PROVED modulo the cited shape of the GZ local factor". The proof uses only that the x = 2 term is
  a function of `n = pe` and the ε-characters at `ℓ | n`, and that for p inert the p-factor is constant in p. The
  explicit pairs then separate ES status. This is fine as stated. The robust content is already Prop 2.2, which
  needs no GZ input.
