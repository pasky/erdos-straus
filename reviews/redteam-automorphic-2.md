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
