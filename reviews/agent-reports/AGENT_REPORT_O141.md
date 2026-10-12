# AGENT_REPORT O141: brainstorm on logic, definability and complexity

Branch `side-agent/bs-logic`. Four memos are under `BRAINSTORM/`, and the scripts are `scripts/bs_logic_*.py`
(all outputs are tiny). None of this proves any case of ES. No memo is LIVE.

**(a) `logic_weak_arithmetic.md`: PARTIAL; one new elementary theorem.**
* **Thm S (PROVED).** Let M be Shepherdson's model of IOpen. For n ∈ M with no real zero on [0,∞), we have
  M ⊨ ES(n) ⟺ ES(n₀) holds in N, where n₀ ∈ Z is the constant term. If n has a zero on [0,∞), then
  M ⊨ ES(n) by an explicit formula.
* Proof idea: a *sign lemma*. Pole cancellation at the largest real zero of XYZ forces a negative
  denominator just to its right, which contradicts positivity at ∞.
* Hence IOpen ⊬ ES, with witness n = 1+t. ES does not follow even from IOpen plus all true congruence
  facts. If ES is true, IOpen + ES_prime ⊬ ES_all, since M has no nonstandard irreducibles.
* Inside M, signed ES holds everywhere, so positivity is the only obstruction.
* Strongest reason it is not a route: every counterexample sits over the standard unit 1. This is the
  "formal point 1" of Theorem M, realised in an actual model, so the angle never touches the square-class
  hard core (B5). Puiseux layers are ES-conservative (C4).
* Open, logic only: IOpen ⊬ ES_prime. This needs a model with a nonstandard prime ≡ 1 mod everything
  that admits a sign lemma (UNCLEAR).

**(b) `logic_ominimal.md`: COLLAPSES to B3.**
* Pila–Wilkie and the determinant method give only upper bounds, and they are vacuous on algebraic sets.
* Barroero–Widmer lattice counting gives a lower bound only once the volume beats the boundary term. That
  needs thickness δ ≫ q/log N, which turns the count into an interval average (Prop 5.4 / scale
  constraint).
* B5: the thickened count is positive at odd squares while the exact count is 0.

**(c) `logic_complexity.md`: PARTIAL, a dichotomy.**
* Congruence-table search for ES witnesses is provably not polylog-time infinitely often. This is the
  campaign's W(p) Ω-result restated as complexity, PROVED modulo its cited inputs. Its heuristic worst
  case is exp((log p)^{1/3}) (Haar exponent 3).
* Factoring-per-slice search (CONDITIONAL_ES Lemma 1.1, slice t) costs one factorisation per t. On primes
  p ≡ 1 (mod 8·3·5·…·29), which are deep square-mimickers, the mean Tf stays at about 9 while the table
  witness W grows from 28 to 94. This is EVIDENCE that the factors of tp+1 escape the congruence trap.
* CONJECTURE FQ: Tf(p) ≤ polylog(p). It implies ES-SEARCH ∈ FP^{FACTOR} ⊂ FBQP. But FQ ⇒ ES, and FQ is the
  B2 lottery with a polylog *moving* slice set (H-A), so this is no route.
* Factor-leak experiment (EVIDENCE): we enumerated all solutions for semiprimes ≤ 4000.
  * Every pq with p ≠ q has a solution that reveals no factor.
  * Every p² has none (ET Prop 1.6), but √n is easy anyway.
  * So no reduction from FACTOR to ES-SEARCH appears.
* Bounded arithmetic: S¹₂ ⊢ ES would give a poly-time solver, by Buss witnessing. IΔ₀ gives nothing
  extra; it does prove descent.

**(d) `logic_divisibility_lgp.md` (extra memo): COLLAPSES to B5 at a named step.**
* The coprime Type II form makes a strengthening ES'' of ES a Π₂ sentence of (N, +, |) with linear terms
  only.
* Lipshitz's local-to-global principle for divisibility systems was the hoped-for lever.
* D1 (PROVED): the system {e | a+b, 4a | d+e, b | d+e} admits no increasing form. The reason is a size
  cycle (e ≤ a+b, 4ab ≤ d+e), so a decision procedure must case-split into bounded slices (B2).
* D2 (PROVED): the system is locally solvable at every prime for every d, including odd squares, where
  it is globally empty.
* So the failing step is exactly "local ⇒ global". This is the divisibility-logic twin of Prop 8.3.

Process note: twice a Write and a `git commit` sat in the same parallel tool batch, and the commit raced
ahead of the write. Both were caught by `git status` and committed separately afterwards; nothing was lost.
