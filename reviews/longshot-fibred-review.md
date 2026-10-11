# Hostile review R136 of O136 (`LONGSHOT_FIBRED.md`, `AGENT_REPORT_O136.md`, `scripts/lsb_*`)

Reviewer branch `side-agent/review-longshot-fibred`, merged `side-agent/longshot-fibred` at review start.
**ES is not solved; nothing here changes that.** The author's document was not edited. Repairs that the author should
paste in are marked "(R136 repair)". From-scratch scripts: `scripts/review_lsb_*.py`.

## Summary verdicts (filled in claim by claim)

| claim | verdict |
|---|---|
| Lemma 1.2, 1.3 | SOUND (trivial; ET Prop 1.7 bound checked in PDF) |
| Lemma 2.1 (rigidity) | SOUND |
| Lemma 2.2 (Borel density) | SOUND |
| Thm 2.3 (a) | SOUND |
| Thm 2.3 (b) | SOUND-AFTER-REPAIRS (D3) |
| Thm 2.3 (c) | GAP → SOUND-AFTER-REPAIRS (D2, MAJOR: hidden hypothesis `φ_i(V_i) ⊂ X_n`) |
| Cor 2.4 | SOUND-AFTER-REPAIRS (D4, D4b, MINOR); transport-to-odd-square and Dirichlet steps verified |
| Thm 3.1 (a), (b) | SOUND relative to (C); primary sources NOT accessible to R136 (EM, EMS, BR, CTX, DRS) |
| Thm 3.1 (c) | SOUND-AFTER-REPAIRS (D9) |
| F1, F6 | SOUND |
| F2 | SOUND (identity + "ES-dead" re-checked, stronger form, p < 1500) |
| F3 | SOUND-AFTER-REPAIRS (D11: weights use varying Γ'_s) |
| F4 | SOUND-AFTER-REPAIRS (D8 citation, D10: growth ≍ H not H²); trivial stabiliser and `c = κ·F_{c,d}` OK |
| F5 | SOUND (Q₀ at every n; orbit counts at 9, 25, 49 re-derived by hand from divisors of 4n+1) |
| Prop 5.1 | SOUND under (U) after D12 |
| §5.2 spinor control | SOUND (Earnest Prop 5.1(i) checked in source; 29 exceptions reproduced independently) |
| Prop 5.3 (a), (b) | SOUND; numerics reproduced exactly (19/40); D5, D6 MINOR |
| Thm 5.4 items 1, 2, 4 | SOUND-AFTER-REPAIRS (D13, item-4 wording) |
| Thm 5.4 item 3, (E-b) | CONDITIONAL, not PROVED: CTX hypotheses fail for F5 (D14) |
| Scope claim "answers T8 blind spot" / "exact list" §5.5 | **OVERCLAIM (D1, MAJOR)** |
| Labels overall | honest apart from D1, D2, D14. "ES not solved" is stated everywhere. |

No FATAL defects. Two MAJOR (D1 scope/overclaim; D2 hidden hypothesis in Thm 2.3(c)); D14 needs a label change.

## Defects

Numbering is D1–D14 (D7 unused), not in order of appearance; D1 is in the Thm 5.4 section. There are no FATAL defects. The MAJOR ones are D1 and D2, and D14 needs a label change.

### Lemma 2.1 — SOUND
Re-derived. Hypotheses used: V irreducible; E ⊂ V(ℚ) Zariski-dense; φ regular at every point of E (so E ⊂ U = dom φ,
and E dense in V ⇒ dense in U); φ(E) finite. `U = ⋃ φ^{-1}(s_i)` closed cover of irreducible U ⇒ one piece. ℚ-rationality
of s₀: s₀ = φ(e) for e ∈ E ⊂ V(ℚ), φ over ℚ. Note the constancy holds for points over any field extension
(φ factors through Spec ℚ → 𝔸³), which Thm 2.3(c) needs. No hidden hypotheses.

### Lemma 2.2 — SOUND
Borel density for arithmetic Γ in connected semisimple G with no ℚ-simple factor H such that H(ℝ) is compact (the
author's "G(ℝ) without compact factor" is stronger, hence fine). Image of dense set under a morphism is dense in the
image's closure. Note Lemma 2.2 does NOT cover tori (F2) or finite groups (F6); the document does not use it there. OK.

### Thm 2.3 — (a) SOUND; (b) SOUND-AFTER-REPAIRS; (c) GAP, repaired below
(a) is Lemma 2.1 plus the remark above (constancy over every extension field, so `s_i = φ_i(generic point)`).

**D2 (MAJOR, Thm 2.3(c), lines ~105–111).** The conclusion "local solubility of V_i already implies `s_i ∈ Sol(n)`"
does not follow from the stated hypotheses. The only link between φ_i and ES is `φ(E) ⊂ Sol(n)`. In the case that
matters (the counting route has not yet produced a point, so E_i may be empty) this is vacuous, and the local data
give only `s_i ∈ ℤ³` (and `s_i > 0`), not that `s_i` solves `4/n`. Concretely, `V_i = 𝔸¹`, `φ_i ≡ (1,1,1)` satisfies every
stated hypothesis of (c) except for E_i, which is the thing being decided. *(R136 repair)* Add the hypothesis
"`φ_i` maps `V_i` (as a rational map) into the ES variety `X_n : 4xyz = n(xy+yz+zx)`", which is automatic for any
encoding designed so that `φ(V_i(ℤ)∩Ω) ⊂ Sol(n)` whenever V_i(ℤ)∩Ω is Zariski-dense. Then `s_i ∈ X_n(ℚ) ∩ ℤ³_{>0} = Sol(n)`.
Also say explicitly that "`V_i(ℤ_ℓ) ≠ ∅`" means a ℤ_ℓ-point in `dom φ_i` (automatic for polynomial φ_i).

**D3 (MINOR, Thm 2.3(b)).** "if not, `E_i = ∅`" contradicts the standing hypothesis that E_i is Zariski-dense
(hence non-empty). The intended statement is about a *candidate* piece `E_i := V_i(ℤ) ∩ Ω ∩ dom φ_i`. *(R136 repair)*
"Let `E_i := V_i(ℤ)∩Ω∩dom φ_i`. If `E_i` is Zariski-dense in `V_i` then `φ_i ≡ s_i` on it and `s_i` is read off the
equations; if `s_i ∉ Sol(n)` then `E_i` is not Zariski-dense (it lies in a proper closed subset)." Note the
consequence the author does not state: when `E_i` is *not* dense, Lemma 2.1 applies only to the components of its
Zariski closure, which are not part of the data (e.g. `V = X_n × 𝔸¹`, `φ` = projection: `E` = F1, closure
`Sol(n) × 𝔸¹`). Such encodings are still in class X (decompose E along the components of its closure, each with
its relatively dense part), so Thm 5.4 survives, but "counting is idle because the solution is written into the
equations" is true only for the pieces of class X1 *as given*, not for an a-priori chosen V. State it that way.

### Cor 2.4 — SOUND-AFTER-REPAIRS
Re-derived steps (ii)–(iv) line by line; they are correct: `D·r(p)/Q(p) ∈ ℤ`, → 0 ⇒ r = 0; `D x ∈ ℤ[n]` ⇒
`D x(p) ≡ D x(0) (p)`; `x₁(p) ∈ ℤ` because `p x₁(p), D x₁(p) ∈ ℤ` and `p ∤ D`; integrality of `D x₁ ∈ ℤ[n]` values
mod D depends on `n mod D`; `m ≡ m₀ (mod 2)` with `m₀` odd ⇒ `m` odd; `y(m²) ≡ y(0) (mod m)` in `ℤ_(m)` and
`m ∤ D·num(y(0))` ⇒ `m ∤ y(m²)`. ET Prop 1.6 checked against the PDF (`sources/elsholtz-tao-1107.1010.pdf`, l. 275:
"For any odd perfect square n, f_I(n) = f_II(n) = 0"), and ET's Type I/II definitions match the document's.
From-scratch check `scripts/review_lsb_et16.py`: all solutions of `4/m²`, m = 3,…,15 odd, enumerated (6–317 solutions
each); none is Type I or II. Dirichlet use is correct (`gcd(m₀, D') = 1` from `gcd(p, D') = 1`).

**D4 (MINOR, Cor 2.4 step (i)).** "the closure of the image of `(φ,n)` has finite fibres over the infinite set P_cov,
so it is a curve" is not a valid inference as written: the fibre of the *closure* W over p can be larger than the
closure of `φ(𝒱_p)` (closure adds points), and finiteness of fibres over a dense set of n does not by itself bound
`dim W − 1`. *(R136 repair)* "Let `U = dom φ`. By Chevalley/generic flatness applied to `U → (φ,n)(U) → 𝔸¹`, there is a
dense open `𝔸¹° ⊂ 𝔸¹` over which `dim φ(U_n) = dim φ(U_η)` (η the generic point). For `p ∈ P_cov` large, `U_p` is
irreducible (EGA IV 9.7.7, generic fibre geometrically irreducible) and φ is constant on it (Lemma 2.1, `E(p)` dense in
`U_p`), so `dim φ(U_η) = 0`. `φ(U_η)` is irreducible and geometrically irreducible of dim 0 over the char-0 field
ℚ(n), hence a single ℚ(n)-point `s₀`; spreading out, `φ|_{U_p} ≡ s₀(p)` for all but finitely many p." Also,
**D4b (MINOR):** D' as defined depends on the pattern (six patterns); the corollary's single `D'` is the lcm over the
patterns occurring infinitely often (a non-square mod a divisor is a non-square mod the lcm). Say so.

### §5.2 spinor-exception control — SOUND (source checked, re-run from scratch)
Earnest arXiv:2203.02620v1 downloaded (`sources/r136/earnest-2203.02620.pdf`). `3x²+4y²+9z²` is B6 = (3,4,9,0,0,0) in
Table 3 (genus = SG I (3,4,9) ⊔ SG II (1,3,36)); Prop 5.1(i): locally-but-not-globally represented ⟺ n ∈ M₃²
(M₃ = monoid generated by 1 and primes ≡ 1 mod 3). Quoted correctly. `scripts/review_lsb_spinor.py` (independent
method: genus-represented := represented by one of the two genus classes of Earnest's Table 3, not a local test):
N = 5·10⁴ gives exactly 29 exceptions, equal to the predicted list `{w² : w ∈ M₃}` (including n = 1 = 1²), and
(3,4,9) represents nothing outside (1,3,36). Matches the author's 29. The CTX §8 / Schulze-Pillot attributions were
not checked (no access); they are standard and only decorative here.

### §5.3 genus set 𝔊⁻_d — (a), (b) SOUND; numerics reproduced exactly; one MINOR precision defect
(a) re-derived: k represented, `gcd(k, 4dm²) = 1` ⇒ `−4dm² ≡ □ (mod k)` ⇒ Jacobi `(−4dm²/k) = 1 = χ_{−4d}(k)(m/k)²`.
(b) re-derived: `−4dp = (−4d)·p` is a product of two discriminants (p ≡ 1 mod 4), so `χ_{−4d}` is a genus character
and equals `(·/p)` on represented values; non-triviality on the class group via a second assigned character — the
case analysis (`dp ≢ 3 (4)` ⇒ character at 2; else `d ≡ 3 (4)` has a prime `q ≡ 3 (4)`) is right.
`scripts/review_lsb_genus.py` (own reduced-form enumeration + own enumeration of ET (2.15) quadruples) reproduces
**every** number of `data/lsb/genus_minus.out`: h, `h⁻ = h/2` at all 40 (prime, level) pairs, `h⁻ = 0` at all 40
(square, level) pairs, and `F_d(p) = 0` in exactly 19 of 40 pairs.

**D5 (MINOR, §5.3 "A Type II point of level d is a form in 𝔊⁻_d(p)").** Which form must be said: from
`ef = p + 4a²d` there are two natural forms of disc −4dp, `[f, 4ad, de]` (represents f) and `[e, 4ad, df]`
(represents e). `scripts/review_lsb_typeII_genus.py` (60 primes p ≡ 1 (4) in [10³, 6·10³], d ≤ 8, all Type II quadruples):
the f-form has `χ_{−4d} = −1` always (O128 Lemma 6.1, whose proof I re-derived: `(2ad)² ≡ −dp (mod f)`,
`f ≡ −1 (mod 4d)`), but the e-form has `χ_{−4d} = −(d/p)`, i.e. lies in 𝔊⁺_d whenever `(d/p) = −1`.
*(R136 repair)* "…is the form `[f, 4ad, de]` (O128 Lemma 6.1), which lies in `𝔊⁻_d(p)`…".

**D6 (MINOR, §5.3/§6.2 "F_d(p) = 0 at 19 of 40").** The five test primes 1009, 2689, 4729, 9601, 10009 are squares
mod 120 (and mostly mod 840): the hard classes. The 19/40 rate is therefore not representative (on 60 consecutive
primes p ≡ 1 (4) from 10³, F₁(p) > 0 for 55). The *logic* only needs one pair with `𝔊⁻_d(p) ≠ ∅ = F_d(p)`, so
the conclusion stands. *(R136 repair)* add "(primes chosen in the square classes mod 120, where Type II is
sparsest)". Also note precisely what is refuted: the per-level criterion "𝔊⁻_d(p) ≠ ∅ ⇒ a Type II point at level d"
is false. The aggregate criterion "∃d: 𝔊⁻_d(p) ≠ ∅ ⇒ ES(p)" is not false (its conclusion holds numerically). It is
vacuous, because by (b) its hypothesis holds at every p ≡ 1 (4), so it *is* ES for p ≡ 1 (4). "Invalid" in §5.3 should
mean "the mass is not the solution count (h/2 against F_d), and the per-level criterion fails". It should not be
read as "the criterion is false".

### Thm 3.1 — (a) SOUND rel. (C); (b) SOUND for a single Γ'; (c) wording too narrow (D9)
(a) is Lemma 1.2 over the finitely many orbits (Borel–Harish-Chandra finiteness of `Γ'\V(ℤ)` for a closed orbit of a
reductive group: correct use). (b): for compact `H(ℝ)` all stabilisers in one real orbit are `G(ℝ)`-conjugate, so
their Haar volumes are equal; `|Γ'_y| ≤ C` holds uniformly for all subgroups of `G(ℤ)` (finitely many conjugacy
classes of finite subgroups of `G(ℤ)`), so C can be taken independent of n and of Γ' ⊂ G(ℤ). Correct.
**Citations.** I could not access Eskin–McMullen 1993, Eskin–Mozes–Shah 1996, Borovoi–Rudnick 1995, Colliot-Thélène–Xu
2009 or DRS 1993 (no copies in `sources/`, none on arXiv). I could not verify the theorem numbers, and I rely on the
author's subagent for them. What I could check: the *shape* of (C) (`w_O = vol(Γ'_y\H_y)/vol(Γ'\G)`) is the standard
EM/DRS normalisation, and the only quantitative instance used (F4) I re-derived and checked independently (below).
**D8 (MINOR, citation fit for F4).** EM Thm 1.4 is for affine *symmetric* `G/H`; F4 has finite stabiliser, so
`V ≅ G/{±1}` is not of that form. The F4 count is the group case (`#{γ ∈ Γ : ‖v₀γ‖ ≤ H}`), which is classical
(Selberg/Huber/Good; or DRS/EM applied to `(G×G)/Δ`, where `Γ×Γ` is not irreducible, so check that EM's
"weakly irreducible" hypothesis is met or cite the group-case statement directly). *(R136 repair)* cite the group-case
count explicitly. It is not needed for any conclusion, because F4's equal-weights claim follows from left-invariance
of Haar measure (`vol{g : ‖y g₀ g‖ ≤ H} = vol{g : ‖y g‖ ≤ H}`) whenever an asymptotic exists.
**D9 (MINOR, Thm 3.1(c)).** "non-compact (a split torus factor)" is too narrow. Any non-compact stabiliser, e.g. a
semisimple `SO(2,1)` stabiliser of a point on a one-sheeted quaternary hyperboloid, gives arithmetic covolumes
`vol(Γ'_y\H_y(ℝ))` that grow polynomially with the discriminant of y (Siegel), so the weights can vary by powers.
*(R136 repair)* "(c) If `H_y(ℝ)` is non-compact (torus or semisimple), `w_O` is an arithmetic covolume…".

### §4 catalogue — F1, F2, F4, F6 SOUND (F4 after D10); F3 has a weight error (D11)
**F2 re-derived and checked** (`scripts/review_lsb_pell.py`; all 3303 Type II quadruples of all primes `p < 1500`, all
d): `T² − D'(2c)² = 1` holds in every case (algebra: `T² − 4c²D' = 4cd(4abcd − a − b − pc) + 1 = 1`). No power `ε^k`,
k = 2..5, is the unit of *any* Type II quadruple of the same p, for any `(c', d')`. This is stronger than (ii), which only
treats the same d. Over these p, `log(2T)/log p ≤ 1.82`. The argument for (ii) is right as stated (T odd, `T ≡ −1 (2cd)`).
**D10 (MINOR, F4 "`≍ H²`").** The count `#{γ ∈ PSL₂(ℤ) : ‖(Q,S)γ‖ ≤ H}` is `≍ H`, not `≍ H²`. Coefficients are
quadratic in γ, so the condition is `‖γ‖ ≲ H^{1/2}`, and `#{‖γ‖ ≤ T} ≍ T²`. `scripts/review_lsb_f4growth.py` (own
enumeration, Q = [3,4,11], disc −4·29; S = [0,2,1]): counts 152, 300, 602, 1206 at H = 250…2000, i.e. `0.60·H`. The
author's own table (≈ 1800 at H = 3000) is consistent with H, not H². *(R136 repair)* "≍ H" (δ = 1).
**D11 (MINOR, F3 "Thm 3.1(b) applies: c(n) = κ·Σ_O 1/|Γ'_{x_O}|").** F3 uses a *different* group `Γ'_s = Γ(4da_s)`
for each solution, whereas Thm 3.1 assumes one Γ'. The weight of the orbit of `x_s` is
`κ/(|Γ'_{s,x}|·[G(ℤ):Γ'_s])`, and the index `≍ (4da_s)^{dim G}` varies by a power of p across solutions. The
conclusion survives in the form used later: all weights are `≤ κ`, so `c(n) ≤ κ·μ·f(n)` (Thm 3.1(a)), and in Thm 5.4
each `s` is its own X2 piece with its own `w_θ` (R = C). *(R136 repair)* replace the formula by
`c(n) = κ·Σ_O 1/(|Γ'_{s,x_O}|·[G(ℤ):Γ'_{s}])` and add "(weights vary with a_s, but are bounded above by κ; Lemma 1.3 applies with
`w_max = κ`)". Also note that this is a power-varying weight capped by the solution, which is exactly the (E-a)
mechanism of §5.5. That bullet should say F3 is a second instance (besides F2), with weights capped *above* (≤ κ),
which is the direction the scale constraint needs.

### Prop 5.1 — SOUND under (U), with an incomplete disjunction (D12)
Re-derived: under (U), and with `m ≡ m₀ (Q₀)`, `m₀² ≡ p`, every factor at `ℓ ∉ S₀ ∪ {ℓ | m} ∪ {p}` is the
unit value (`m_ℓ > 0`, `E_ℓ = 1`), and every factor at `ℓ ∈ S₀` is the same at p and at m². Label "PROVED under (U)" is
honest. (U) is a real hypothesis and is not verified for any concrete ES family in the file.
**D12 (MINOR, Prop 5.1 conclusion).** The "either `m_ℓ(m²) = 0` for some ℓ | m, or some `E_ℓ(α,m²)`, ℓ | m, differs
from its unit value" is not exhaustive. If every factor at ℓ | m takes its unit value, then
`M(m²) = m_∞ ∏_{ℓ∈S₀} m_ℓ(p) · |B|⁻¹ Σ_α ∏_{ℓ∈S₀} E_ℓ(α,p) · (unit factors)` can still vanish, through
cancellation in the α-sum. Meanwhile `M(p) > 0` because `E_p(α,p) ≠ 1` re-weights that sum. That is "T1 passed purely
at the place p". *(R136 repair)* add a third alternative: "or `E_p(α,p)` (resp. `m_p(p)`) differs from its unit value, i.e.
the place p alone separates p from m²". The Reading ("at the primes dividing m … for n = p the only such place is p")
is unaffected. Also: §0's bullet for 5.1 drops "(U)"; add it. Rename `Q₀ = ∏ ℓ^k` (clashes with the form `Q₀`).

### Thm 5.4 and §5.5 — the scope claim is overstated (D1, MAJOR); items 1, 2, 4 SOUND-AFTER-REPAIRS; item 3 CONDITIONAL
**D1 (MAJOR, AGENT_REPORT l. 56; §0 "Fibring does not escape the scale constraint for any encoding of class X";
§5.5 "exact list").** The red team's T8 blind spot (RT1 §5.5: "the constraint is on `M/μ`; encodings with fibres
`μ ≥ p^{η−o(1)}` … escape") is **not** closed by Thm 5.4. Thm 5.4's bound is `M(n) ≤ 2R·μ(n)·f(n)`, with μ the
number of pieces over one solution and R the weight ratio, both unrestricted in class X (Θ(n) is arbitrary, and R is
*defined* as the ratio). When `Rμ ≥ p^η` the theorem gives no obstruction. That is the T8 situation, moved from "fibre
size" to "number of pieces per solution". Thm 5.4 does prove something narrower and true: the *continuous* fibre
factor `H^δ` contributes nothing. A power-fibred encoding gets past the scale constraint only through discrete
multiplicity (many algebraic pieces or lattice orbits per solution, μ ≥ p^η) or through weight spread (R ≥ p^η), and
never through the size of the fibres. The trivial example: split each F1 fibre `{s} × ℤ^r_{≥0}` into `p` translated
cones. That is class X1 with μ = p. It is "rigged", but nothing in the definition of class X excludes it or its
non-rigged relatives (encodings whose pieces are indexed by a coarse invariant with p^η preimages). *(R136 repair)*
(i) §0: "Fibring does not escape the scale constraint: for every encoding of class X, `M ≤ 2Rμf`, with the fibre
factor `H^δ` cancelling (Thm 5.4). The T8 blind spot (μ or R ≥ p^η) is not closed. It is relocated from fibre size to
the number of pieces per solution and to the weight spread." (ii) §5.5: add **(E-d)** "class-X encodings with
`μ(n) ≥ n^η` pieces over one solution (discrete multiplicity); Thm 5.4 is vacuous for them". (iii) Report l. 56:
replace "answers RT1 §5.5's blind spot" by "shows that continuous (H^δ) fibring does not reach the T8 blind spot; the
blind spot itself (μ ≥ p^η) remains open".

**Is class X rigged?** Not in the bad sense: X1 is very broad (every algebraic piece), X2 is the natural lattice-orbit
class, and the exclusions (E-c: floors/gcds/factorisations) are stated. But (a) X1 contains every set, decomposed into
points (0-dim V_θ). The theorem has content only for decompositions with μ < ∞, i.e. with the `H^δ` growth *inside*
positive-dimensional pieces, and this should be said. (b) R is defined to make item 1 true, so item 1 is a
tautology. Its content is in Thm 3.1(b) (R = C) and F2 (R = O(log p)).
**D13 (MINOR, item 1/2 normalisation).** A counting route proves a bound for `c(n) = Σ_θ c_θ`, not for
`c̃ = Σ_θ c_θ/w_θ`. The w_θ can vary by powers across θ (F3: `w ∝ [G(ℤ):Γ(4da_s)]⁻¹`, D11), so item 2 must be stated as
`M(n) ≤ 2·c(n) ≤ 2Rμ(n)f(n)·max_θ w_θ(n)`. Also, `w_θ := c_θ` for X1 makes `c_θ/w_θ = 0/0` for pieces of
sub-maximal growth; restrict c̃ to pieces of maximal exponent δ*. *(R136 repair)* as stated.
**D14 (MINOR→MAJOR for item 3's label, Thm 5.4(3), (E-b)).** CTX Thm 3.7 (per the author's own literature note)
needs G semisimple simply connected **and H connected**. In F5, the ES-natural genus-full closure, these fail
both ways. With `G = SO(L) ≅ PGL₂` the stabiliser of a pair is trivial but G is not simply connected; with
`G = Spin = SL₂` the stabiliser is `{±I} = μ₂`, which is not connected. So "decided by local and BM data without
counting (CTX)" is not established for F5 (or for F4-type pair spaces). It is established for X_d-type spaces with
`Spin(2,1)` and a torus stabiliser (connected). The F5/𝔊⁻ refutations in item 3 do not use CTX, so they stand.
*(R136 repair)* Label item 3 and (E-b) "CONDITIONAL on the CTX hypotheses (G s.c., H connected), which fail for F5's
pair space (`H = μ₂` in `SL₂`). For representations of binary by indefinite ternary lattices, use instead the
spinor-exception theory (e.g. Hsia–Shao–Xu 1998, *not checked by R136*)".
**Item 4.** Correct via Cor 2.4, applied family by family (lcm of the D'). "Uniform" must mean: each X1 piece is the
fibre `𝒱_{θ,n}` of one family `𝒱_θ → 𝔸¹_n` with geometrically irreducible generic fibre, and `E_θ(p)` is dense in it.
Say so (MINOR).

### §6 numerics — SOUND
F4 orbit bookkeeping re-derived by hand from the divisors of `4n+1`: n = 29 (117: 12 signed odd divisors, ES orbits
A ∈ {3, 39}), 41 (165: 16; {3, 11, 15, 55}), 53 (213: 8; {3, 71}), 9/25/49 (37, 101, 197 prime: 4 orbits, all positive
divisors ≡ 1 (4), so 0 ES orbits). All match the table. Per-orbit count level: own enumeration gives `0.60·H` for a
29-orbit, against the author's 1792–1818 at H = 3000 (`≈ 0.60·H`). Consistent.

### Minor remarks (no defect number)
* Cor 2.4 attribution: the closest printed statement is ET §1 on congruences "solvable by polynomials" (ET Props
  1.8–1.9, with the remark that Prop 1.6 implies the square-class obstruction). Cite those rather than "Mordell 1969 /
  Schinzel 2000 as quoted in ET p. 8".
* The author's report says the CTX/EM/EMS/BR statements were "checked against the primary texts by a research
  subagent". Per house rules, research-subagent verdicts need a review, and R136 could not access any of these texts.
  The theorem numbers remain unverified by an independent reader.

## Scripts (all from scratch, R136)
* `scripts/review_lsb_et16.py`: brute-force Type I/II for odd squares 9…225 (ET Prop 1.6) and primes.
* `scripts/review_lsb_spinor.py`: spinor exceptions of 3x²+4y²+9z² to 5·10⁴ via the two genus classes.
* `scripts/review_lsb_genus.py`: h, `#𝔊⁻_d`, `F_d` (reproduces `data/lsb/genus_minus.out` exactly).
* `scripts/review_lsb_typeII_genus.py` → `data/review_lsb_typeII_genus.out`: genus of the f-form vs the e-form (D5).
* `scripts/review_lsb_pell.py`: F2 identity and non-recurrence of powers across all Type II quadruples, p < 1500.
* `scripts/review_lsb_f4growth.py`: F4 orbit growth exponent (D10).

## Repairs applied (R136, after the author quit)
At the parent's request, all of D1–D14 (including D4b and the item-4 wording) have been applied directly to
`LONGSHOT_FIBRED.md` and `reviews/agent-reports/AGENT_REPORT_O136.md`, each marked "(R136 repair, Dn)":
* the D1 scope rewording appears in §0, at the head of Thm 5.4, as a new (E-d) in §5.5, and in the report;
* D2 adds a hypothesis to Thm 2.3(c);
* D14 relabels Thm 5.4 item 3 and (E-b) as CONDITIONAL;
* the "checked only by the author's research subagent" caveat for EM/EMS/BR/CTX/DRS appears in §0, in the §4
  literature paragraph, and in the report.
