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
