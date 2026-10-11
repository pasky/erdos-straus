# Hostile review R136 of O136 (`LONGSHOT_FIBRED.md`, `AGENT_REPORT_O136.md`, `scripts/lsb_*`)

Reviewer branch `side-agent/review-longshot-fibred`, merged `side-agent/longshot-fibred` at review start.
**ES is not solved; nothing here changes that.** The author's document was not edited. Repairs that the author should
paste in are marked "(R136 repair)". From-scratch scripts: `scripts/review_lsb_*.py`.

## Summary verdicts (filled in claim by claim)

| claim | verdict |
|---|---|
| Lemma 1.2, 1.3 | SOUND (trivial) |
| Lemma 2.1 (rigidity) | SOUND |
| Lemma 2.2 (Borel density) | SOUND (hypothesis wording: see D7) |
| Thm 2.3 (a) | SOUND |
| Thm 2.3 (b) | SOUND-AFTER-REPAIRS (D3: self-contradictory "else E_i = ∅") |
| Thm 2.3 (c) | GAP → SOUND-AFTER-REPAIRS (D2: hidden hypothesis φ_i(V_i) ⊂ ES variety) |
| Cor 2.4 | SOUND-AFTER-REPAIRS (D4: step (i) "finite fibres ⇒ curve" needs the generic-fibre-dimension argument; D' must be an lcm over patterns) |

## Defects

(numbered below; FATAL / MAJOR / MINOR)

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
