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

