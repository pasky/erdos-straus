# AGENT_REPORT O244 — FF family classification / Case A inversion asymmetry (integrity check)

Branch side-agent/ff-inversion. Main file FF_INVERSION_CHECK.md; scripts scripts/zi_*; data data/zi/.

**Verdict.** The brief's suspicion is *half right*. The F_q[T] model does miss a family type: the analogue of ET type I4
("Case A⁻¹", balls u ≡ −1/E), and also ET type II2. But on the slices where all no-covering theorems are proved the missing
types add nothing, so **(J)51, (J)56, (J)67 and Conjecture 0.2 need no repair**.

1. *Classification (PROVED, §1).* Lemma 1.1: the ET parametrisation holds over F_q[T] (every monic solution is Type I,
   A·abd = eP + 1, or Type II, A·abd = P + e, e = (a+b)/c, a, b, c, d monic). Lemma 1.2 / Cor 1.3: a linear family (fixed E = AX − P)
   is the F_q[T] image of II1, II3, I1, I2, I3 only; for I4, E_FF = (aP + c)/b has degree n − (deg b − deg a), for II2
   E_FF = (P + Aa²d)/f. Prop 1.4: I4(a, b, e) is a valid congruence family (class P ≡ −1/e mod Aab, explicit solutions over F₃[T]).
   Lemma 1.6: the families with three of a, b, c, d fixed are exactly II1, II2, I4. (I4 *solution triples* are not linear; its
   validity set may still coincide with a linear one, e.g. e = 1 — the review counterexample; coverage is settled on slices only.) FE3 Lemma 1.1 (A/B) itself is correct and
   complete for linear families; its normalisations lose nothing.
2. *Domination on the slices (PROVED, §2).* II2 is never valid at a slice point (Lemma 2.1). I4 at u ⟹ Case A at 1/u (Lemma 2.2).
   New: a Case A ball lies inside a Case B ball with the same E whenever α + v ≥ k (Lemma 2.3: E | 1 + T^{α+v}(H/b1)·a1'); Case B is
   inversion-closed for every k (Lemma 2.4). Hence on the c-slices (k ≥ 2, via k = 2) and on the k = 1 slices u(0) ∉ F₃^*,
   I4 ⊆ Case B for k ≤ 2, and for k ≥ 3 the level-k ET-covered set lies in the level-2 linear covered set, which is what the
   proofs bound (Thm 2.5). Cor 2.6: all those theorems hold for coverings by all seven ET-type families, same constants.
   Side effect: for k ≤ 2 the Case A terms with monic E are redundant in the union bounds (certificates conservative).
3. *Computations (EVIDENCE, §3).* Exhaustive solution enumeration (q = 3 n ≤ 7, q = 5 n = 4, q = 9 n = 3, k = 1, 2; own GF(q)):
   Lemma 1.1 holds on all ~2,000 solutions; I4-shaped solutions are common. q = 3 depth-9 tree: A + B has 24 balls without a mirror,
   A + B + I4 has 0, Case B alone 0, and survivors are unchanged (every A and I4 ball lies in a census Case B ball; every Case A
   datum has a same-E container). Lemma 2.3 brute-forced at
   q = 3, 5, 9 (k = 1–3, slices and all units): 0 failures when its hypotheses hold; off the slices (α + v < k) it does not apply.
   Even naive double counting of the Case A mass keeps every certificate closed (§3.4; tightest OA Thm 2.2: 3.37 < 4).

**What does need a wording fix (for the parent).** O(q, A) (FE2 §0.1) and every global statement about it are for *linear*
families only; ffl_tree uncovered densities are upper bounds for the ET-uncovered density. "No finite covering" must keep "linear"
or cite Cor 2.6. Suggested ledger line: "(J)?? FF family classification audit (O244): linear families = ET II1, II3, I1–I3; I4 and
II2 omitted; on the sterility slices both are dominated by Case B (Case A ⊂ Case B with the same E), so (J)51/(J)56/(J)67 hold for
all ET-type coverings. PROVED." (R250 repair m-2/m-5: say "hold for coverings by linear, I4 and II2 families (the seven ET
types); coverings by other polynomial families are not addressed". Lines still lacking "linear": SYNTHESIS_SPARKS3.md:119,
STATUS.md:52. Hostile review R250, reviews/ff-inversion-review.md: no FATAL/MAJOR; depth-9 tree reproduced exactly.)

**Not done / scope.** Families fixing other auxiliary quantities than E_FF (beyond the seven ET types) are not classified (Lemma 1.6
scope note). Off-slice I4/II2 coverage (global O) not quantified.

**Self-review.** One deep review pass (codex, via the review tool) found no error in Lemmas 1.1, 2.1, 2.3, 2.4, Thm 2.5; it
flagged an overclaim in Prop 1.4 (validity sets), an unproved global "strict enlargement", a Case B miscount in zi_tree (B read
as allb − A), lost k ≥ 3 qualifications in summaries, and Lemma 1.2 wording. All repaired in place.
