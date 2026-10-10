# R124 — hostile review of POINTWISE_TERNARY.md (O124)

Reviewer branch `side-agent/review-ternary`, merged `side-agent/ternary-embed` at review time.
From-scratch scripts: `scripts/review_tern_sweep.py`, `scripts/review_tern_qd.py`, `scripts/review_tern_ratio.py`;
logs `logs/review_tern_*.txt`. Sources checked: ET arXiv:1107.1010v6 (local PDF; Thm 1.1 p.4, remark p.5, Prop 1.6
p.6, definition p.7–8, Prop 1.9 p.8, (2.1)–(2.22) pp.11–14); Pila, Astérisque 228 (1995) 183–187 (downloaded from
numdam, Theorem A read verbatim). NOT accessed: Mordell's book pp. 287–290, Schinzel [68], Duke–Schulze-Pillot,
Blomer, Golubeva–Fomenko, HKK (these enter only through (M), which ET restate, and through hypothesis (R)).

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.3 (level sets) | SOUND |
| Lemma 2.1 (fibre count, definite, incl. k ≥ 4 slicing) | SOUND (MINOR m3) |
| Pila input (P) | SOUND — matches Pila Thm A (uniform in the variety; `H^{n−1+1/d}·exp(12√(d log H log log H))`) |
| Prop 2.2 | SOUND |
| (M), Lemma 3.1, Cor 3.2 | SOUND (MINOR m2 on the "consequence of Prop 1.6" parenthetical) |
| Thm 4.1 (a), (b) | SOUND; constants uniform in `p`; exponent `(k−2)/2 − 1/4 + ε` re-derived |
| Cor 4.2 (`𝒫_R ⊆ U`), ε₀ < 1/4 | SOUND relative to (R) (MINOR m1 wording "exactly") |
| Cor 7.1 (sterile points) | SOUND (square part is immediate from Cor 4.2; x** part imported from MORDELL13E, not rechecked) |
| Lemma 5.1, Prop 5.2, Cor 5.3, Pell example | SOUND (MINOR m3, m4) |
| Comp 6.1 (57 substructures, all isotropic, unique rank-3 `Q_d`) | SOUND — reproduced exactly with an independent ideal/saturation setup |
| Prop 6.2 | SOUND-AFTER-REPAIRS (MINOR m5: "not mild" proof sketch is not a proof as written) |
| §8 Step 4 EVIDENCE | SOUND — reproduced exactly (10⁶ failures, 10⁷ table, 10⁸ extremal prime, 10⁸ 1/20 sample, ratio) |
| Scope / novelty Assessments | Essentially right, but understated in two places (MAJOR M1, MINOR m6) |

No FATAL defects. One MAJOR (scope presentation), six MINOR.

## Re-derivations (what I checked and how)

**Def 1.1/1.2 — is the setting rigged?** No. `S_j` is arbitrary (conditions involving `p` can be encoded through
`p = (Q(v)−η)/κ`), maps are rational of bounded degree, and the degenerate/nondegenerate split is exhaustive (some
coordinate ∉ ℚ(Q) or all ∈ ℚ(Q)). The *real* restriction is that `Q, κ, η, J, D` are fixed independently of `p`;
see M1. Degeneracy is algebraic (not relative to `S_j`): the author's own example (`v₁ = 1` on `S`) shows a piece that is
functionally degenerate on `S` but algebraically nondegenerate; the theorem still handles it correctly by counting.

**Lemma 1.3.** (i) `Q − m` (m ≠ 0) has homogenisation of rank `k+1 ≥ 4`, so it is irreducible; generic fibre
geometrically integral ⇒ ℚ(Q) algebraically closed in ℚ(v). (ii) Constancy on a dense subset ⇒ `A − x_m B ∈ (Q−m)`
(closed condition), so `dX ∧ dQ` vanishes on the smooth `E_m`; infinitely many coprime `Q − m` divide each minor
numerator ⇒ `dX ∧ dQ ≡ 0`. (iii) Jacobian criterion. Correct.

**Lemma 2.1 / Prop 2.2 / Thm 4.1 exponent.** Pila Thm A (verbatim): irreducible affine `V` of dim `n`, degree `d` in
`𝔸^N`: `#{integral points of height ≤ H} ≤ c(n,d,N) H^{n−1+1/d} exp(12√(d log H log log H))`, constant uniform in `V`.
For `n = 1`, `d ≥ 2`, `H = B_m ≍ √m`: `≪ m^{1/4+ε}`, uniform in `p` because only the degree `≤ 2D` enters. Non-real
components: real points ⊂ `C ∩ C̄`, `≤ (deg C)²` each (generic projection + Bézout), total `≤ 4D²`. Real lines are
impossible on a bounded real quadric. k ≥ 4: I re-derived the slicing: `≪ m^{(k−3)/2}` slices; good slices
`≪ m^{1/4+ε}` each; bad slices lie on a nonzero hypersurface of degree `≤ D_1(D)` in `t` (Schwartz–Zippel count
`≪ m^{(k−4)/2}`), each with `≪ m^{1/2+ε}` points (fix `v₁`, binary positive definite equation with fixed quadratic
part, divisor bound). Totals `m^{(k−2)/2−1/4+ε}` and `m^{(k−3)/2+ε}`; correct. Note the division remainders `R_0, R_1`
depend on `m`, but only their degree in `t` is used, so uniformity holds. Prop 2.2: `#{values of X_j} ≤ f(p)` since
distinct first coordinates come from distinct solutions; `𝔐_j` finite and fixed. Correct.
Thm 4.1(b): `f(p) ≥ #R(p)/(C p^{(k−2)/2−1/4+ε/2}) ≫ p^{1/4−ε₀−ε/2}`; ET Thm 1.1 (checked p.4–5:
`Σ_{p≤N} f(p) ≪ N log²N log log N`) + Markov on dyadic ranges gives `≪ N^{3/4+ε₀+ε/2} log³N`. Correct, and
`ε₀ < 1/4` is exactly what makes this `o(N/log N)` in Cor 4.2.

**(M), Lemma 3.1, Cor 3.2.** ET p.7–8 define "solvable by polynomials" with rational coefficients and positive
integer values for large `n` in the class — exactly the author's (M), and ET p.8 states square classes are not
solvable (citing Mordell [44], Schinzel [68]). Lemma 3.1's polynomiality (`|S/T| < 1/δ` but `∈ δ^{−1}ℤ`) and
periodicity mod `δ` arguments are correct; the class of a prime `p > δ` is primitive. Correct.

**Cor 4.2 / Cor 7.1.** Dirichlet + Thm 4.1(b) ⇒ no primitive class mod `lcm(L,q*)` in `𝒫_R ∖ U`. Correct. Cor 7.1:
square points are excluded directly (a square point is a square mod `q*`, and `U` has no square class). The
general sterile statement uses ET Prop 1.9, whose actual text (p.8) is: if `r mod q` is Type I (resp. II) solvable
then *all sufficiently large primes in the class* lie in finitely many classes of the listed families — exactly
what the proof uses. Correct.

**§5.** Lemma 5.1: a ℚ-line in `{Q = m}` ⇔ 2-dim totally isotropic subspace of `Q ⊥ ⟨−m⟩` not inside `{w₄ = 0}`;
Witt index 2 in dim 4 forces `≅ H ⊥ H`, determinant 1 mod squares. Correct (but see m4 on conventions). Prop 5.2:
correct (see m3). Cor 5.3 Pell example re-checked by hand: `y = 1`, `p = 3`, `x² − 2z² = 2` has infinitely many
solutions (2,1),(10,7),…, output `(1,6,6)` and `1 + 1/6 + 1/6 = 4/3`. Valid, nondegenerate, unbounded.
`Q_d` signature (1,2), `n > 0` ⇒ two-sheeted hyperboloid, no real lines. Correct.

**Comp 6.1 (CERTIFIED) — independent recomputation.** `review_tern_sweep.py` does NOT use the author's 4-generator
ideal: it writes `T^I, T^II` as graphs of ET's parametrisation by `(a,b,c,d)` (ET p.11 and the Prop 2.6 proof),
saturates by the product of all coordinates and `a+b`, eliminates by lex Gröbner basis, checks every eliminant
numerically on random points of `T`, and tests isotropy of binary forms by a square test on `−det(Hessian)` over
ℚ(params). Result (`logs/review_tern_sweep.out.txt`): 11 + 11 = 22 of 30 subsets give `n ∈ ℚ(V)` (the other 8: 4 with
`V` algebraically dependent, e.g. `ce = a+b`, `ef = 4a²d+1`; 4 with `n` quadratic over ℚ(V)); **57** quadratic
substructures, ranks {1: 2, 2: 54, 3: 1}; all 56 non-rank-3 ones isotropic (binary: square discriminant; ternary of
rank ≤ 2: degenerate); unique rank-3 = Type II, `(a,d,e,f)`, `d` fixed: `n = ef − 4da²`. Identical to the author's
log. (Hessian determinant is `8d`; the text's `det Q_d = d` is the Gram convention — m4.)

**Prop 6.2.** (i) `Q_d(n,1,0) = n`, primitive. Correct. (iii) matches ET Prop 1.9 family `−4a²d mod f`, `4ad | f+1`,
and ET (2.18),(2.19). Correct. (ii) see m5.

**§8 Step 4 (EVIDENCE) — independent re-run.** `review_tern_qd.py` (own divisor search; every hit verified as an exact
ES identity `4/p = 1/(abd) + 1/(acdp) + 1/(bcdp)`, ET (2.22)):
* N = 10⁶, DMAX = 4, AMAX = 100: failures exactly {3361, 7681}, as claimed.
* N = 10⁷, DMAX = 8, AMAX = 200: 20513 primes, histogram {1: 19634, 2: 682, 3: 160, 4: 21, 5: 11, 7: 1, 8: 2,
  9: 1, 13: 1}, worst 13 at 733321 — identical to the author's table.
* N = 10⁸: `a_min(84525841) = 22` (with `d = 3`), `a_min(733321) = 13`; a 1/20 sample (8974 primes) has no failure,
  worst 6. (Full 10⁸ run not repeated.)
* Ratio claim (first 2000 hard primes, d = 1, a ≤ 50): 14109 / 562792 = 0.0251, identical.

## Defects

### MAJOR

**M1 (scope presentation; the brief's "does the scope exclude the natural routes" question).** Location: §0 first
bullet, Cor 4.2 bold sentence, §7 *Interpretation*, suggested ledger entry in AGENT_REPORT. Theorem 4.1 is correct,
and its setting is not rigged: arbitrary `S_j` and rational recipes are generous. But `Q, κ, η, J, D` are fixed
independently of `p`, and **no ES route actually in use has this form**. ES's only rank-3 quadratic piece `Q_d` is
indefinite, so Thm 4.1 does not apply to it, and §5 needs extra counting inputs. It also works only with `(a, d)`
unbounded. The author's own Step 4 shows `a_min` growing (22 at 84525841), and the ET Type I/II families with `a, d`
free are exactly the growing-parameter families of §9.1, which are only an Assessment. Two statements therefore hold
only for a single fixed embedding: the headline "representation theorems contribute nothing beyond finite polynomial
coverings", and the §7 sentence "Theorem 4.1 shows that this extra length is wasted". Neither covers a family
`(Q_t)_{t ≤ T(p)}` used as a multiplier, which is the natural route. §9 says this, but §0 and the ledger entry do not.
*Repair:* in §0 bullet 1, Cor 4.2, §7 and the ledger entry, add: "for one fixed `(Q, κ, η)` and fixed `(J, D)`. Not
covered: families with a parameter growing with `p`, which includes every known ES parametrisation (ET Type I/II with
`a, d` unbounded)". Keep the §9.1 Assessment label.

### MINOR

**m1.** Cor 4.2, bold sentence: "the primes on which (R) delivers ES are **exactly** primes that a finite polynomial
covering already handles". What is proved is an inclusion. Replace "exactly" with "among the".

**m2.** §3, (M): "a consequence of ET Prop 1.6". Prop 1.6 says `f_I(n) = f_II(n) = 0` at odd squares. To deduce (M)
from it, you also need that the polynomial solution at a large odd square `n` in the class is of Type I or II. That
requires `gcd(P_i(n), n) = 1` for every `P_i` with a nonzero constant term, which is not automatic for composite `n`.
ET p.8 say "also follows" without proof. *Repair:* cite Mordell [44] and Schinzel [68] (via ET p.8) as the primary
source, and either drop the parenthetical or say "essentially follows".

**m3.** Prop 5.2's bound `C T^{1/2+ε} + 4D²` leaves out the up to `2D` real lines not defined over ℚ. Each carries at
most 1 integer point, as the proof itself says. *Repair:* `+ 4D² + 2D`.

**m4.** Lemma 5.1, §5 Remark, Comp 6.1: "det" is used without fixing a convention. The criterion
`−m·det Q ∈ ℚ^{×2}` needs the Gram matrix of `B(x,y) = ½(Q(x+y) − Q(x) − Q(y))`. The Hessian convention multiplies
det by `2^k`, which for `k = 3` changes the square class by 2. Both scripts report `det = 8d`, while the text says
`det Q_d = d`. This is harmless for `Q_d`, where the sign alone decides, but Lemma 5.1 should state its convention.

**m5.** Prop 6.2(ii) argues that "a finite union of lattice cosets has a fixed positive density or zero". This does
not prove non-mildness: in boxes `{a ≍ A}`, a finite union of cosets of rank-2 lattices also has proportion `≍ 1/A`.
*Repair:* argue by slices. For `S = {4ad | f+1}`, the slice `S ∩ {a = a₀}` is `{f ≡ −1 (mod 4a₀d)}`, and its
`f`-period `4a₀d` is unbounded. For a finite union of cosets `v_i + L_i`, every slice is a union of cosets of the
finitely many lattices `L_i ∩ {a = 0}`, so the periods are bounded. Separately, "`Σ τ(n+4da²) ≍ A log A`" for fixed
`n` has a constant that depends on `n`. Either cite it (Erdős/Hooley-type) or replace it by `≫ A`, which is all
that is used.

**m6.** Novelty (§0): ET make two relevant remarks, not one. The first (p.5, after Thm 1.1) is about polylog `f(p)`
and the circle method. The second (p.6, after Prop 1.6) is that vanishing at odd squares "rules out many strategies
(e.g. a finite set of covering congruence strategies, or the circle method)". The square-point parts of Cor 3.2 and
Cor 7.1 restate the second remark. The genuine additions are two. First, a version for methods valid only at primes,
which ET's square argument does not directly constrain. Second, the fibre-count formalisation. *Repair:* cite both
remarks. "Modest" is accurate, arguably generous.

**m7.** §5 Remark: "Prop 5.2 applies to the Type II recipe on (Q_d). It is consistent only because the side condition
`4ad | f+1` is thin". For fixed `d`, the Type II map `(a,b,c,d,e,f) ↦ (abd, acdp, bcdp)` is injective: ET p.14 call it
injective modulo the dilation (2.10), and that dilation moves `d`. So `#R(p) ≤ f(p)` holds trivially for this piece,
and the fibre bound says nothing there. *Repair:* say so. It also makes the "divisor problem, not representation
problem" point more cleanly.

**m8.** Comp 6.1: "So ES carries no positive definite (or anisotropic) quadratic substructure in ET's coordinates".
The sweep only records quadrics in which `n` is a quadratic polynomial. Quadrics that do not involve `n` are dropped
as "V dependent". For example, Type I's `ef − 4da² = 1` is the same form `Q_d` at level 1. The conclusion stands,
since `Q_d` is isotropic, but the claim should be scoped: "among substructures where `n` is a quadratic polynomial
in the free coordinates".

## Honest assessment of the two questions in the brief

* **Does the scope exclude the growing-parameter families?** Yes, completely (M1). The theorem is a correct
  obstruction for one fixed form with a bounded-complexity recipe. The natural ES routes lie outside it: Type I/II
  with `d, a` growing, and multiplier families `Q_t`. The author correctly diagnoses why the extension fails. The
  exceptional levels `𝔐_{t,j}` are not uniform in `t`, as the perturbation `(Q_t − m_t)v₁` shows. I see no quick fix,
  and the §9.1 Assessment label is right.
* **Is "novelty modest" right?** Yes. ET's two remarks (m6) anticipate the conclusion heuristically, and the
  Bombieri–Pila fibre count is standard dimension-growth technology. What is new is:
  * the clean dichotomy: a degenerate piece is a Mordell identity, a nondegenerate one has `p^{−1/4}`-thin fibres;
  * the prime-only formulation;
  * the explicit thin-set counterexample, which shows that the obstruction concerns representation *theorems*, not
    embeddings.
