# AGENT REPORT O124: embedded quadratic forms and pointwise ES

Branch `side-agent/ternary-embed`. Deliverable: `POINTWISE_TERNARY.md`. Scripts: `scripts/tern_sweep.py` (symbolic
sweep), `scripts/tern_qd.py` (numerics). Logs: `logs/tern_sweep.out.txt`, `logs/tern_qd_1e7.out.txt`,
`logs/tern_qd_1e8.out.txt`.

## Outcome: a precise negative result (obstruction theorem with explicit scope)

1. **Thm 4.1 (PROVED, given Pila 1995 / Bombieri–Pila, Mordell–Schinzel's "square classes are not polynomially
   solvable", and ET Thm 1.1).** Setting: `Q` positive definite in `k ≥ 3` variables, and an ES recipe of bounded
   complexity `(J, D)`: piecewise rational maps on arbitrary side-condition sets, applied to representations
   `Q(v) = κp + η`.
   * Degenerate pieces (output a function of `Q(v)` only) are Mordell-type polynomial identities on a finite union
     `U` of non-square classes.
   * Off `U`, the recipe uses only `≤ C f(p) p^{(k−2)/2−1/4+ε}` representations.
2. **Cor 4.2.** If the representation input (R) holds on a congruence set `𝒫_R` (with `ε₀ < 1/4`), then `𝒫_R ⊆ U`. So
   DSP/Kloosterman/circle-method inputs do no work beyond a finite polynomial covering.
   **Cor 7.1:** no sterile point (square points, x**, unless x** lies in an ET class of level ≥ 2.59·10¹⁰) lies in the
   closure of `𝒫_R`.
3. **Indefinite ternary (§5).** The same fibre bound holds in balls when the level set is line-free, which is all `m`
   outside one square class. Positivity forces thin admissible sets, not bounded ones. Split level sets and `k ≥ 4`
   indefinite forms are a stated gap.
4. **Step 1 (CERTIFIED symbolic).** All 57 quadratic substructures of ET's Type I/II charts are isotropic. The only
   rank-3 one is `Q_d = ef − 4da²` (Type II, `d` fixed). It represents every integer (no local or spinor content). Its
   level sets are line-free, and its side condition `4ad | f+1` is not mild. So ES escapes the obstruction only
   through thin side conditions.
5. **Step 4 (EVIDENCE).** Every Mordell-hard prime `≤ 10⁸` is solved via (Q_d) with `d ≤ 8`, `a ≤ 22` (≈10 s). This is
   a divisor search of growing length.

## Review status

One self-review (codex, deep mode) found:
* a FATAL overclaim in the first draft of Cor 4.2: thin nondegenerate pieces can cover primes outside `U` (explicit
  example now in the text);
* a missing `ε₀ < 1/4`;
* a wrong "split-line" explanation of Q_d;
* "positivity forces boundedness" (false; Pell example);
* §9 families overclaimed (now Assessment);
* the k = 4 anisotropic-valuation claim;
* a script isotropy-flag bug (fixed; all 57 entries now flagged isotropic);
* profinite wording.

All of these are repaired. The reviewer confirmed that Lemma 1.3, Lemma 2.1 (including the slicing), Prop 2.2,
Lemma 3.1, Lemma 5.1, Prop 5.2 and the Thm 4.1 mechanism are sound. A from-scratch hostile review by the parent is
still needed.

## Suggested ledger entry (for the parent)

(H)/(F)-type negative result: "Representation theorems for definite (and line-free indefinite ternary) forms plus
bounded-complexity ES recipes reduce to finite Mordell-type coverings (POINTWISE_TERNARY Thm 4.1, Cor 4.2; PROVED rel.
Pila, Mordell–Schinzel, ET Thm 1.1). ES's only rank-3 quadratic piece is `ef − 4da²` with a non-mild side condition
(Comp 6.1 CERTIFIED)." Novelty is modest (it formalises ET's remark on the circle method).

## Open / not done

* Families with a growing parameter: only an Assessment. Exceptional levels are not uniformly controlled.
* The exact coset+cone forms of the DSP/Blomer/HKK theorems were not re-verified; they enter only through the
  hypothesis (R).
* No input from O126 was received.
