# AGENT REPORT O130b — quaternionic / supersingular route, checkpoint 2

Branch `side-agent/quaternion-es`. File `QUATERNION_ES.md` (§§3.2–6 new). Scripts: `scripts/quat_typeI.py` and
`scripts/quat_residual.py` (new).

## Answers to the three requests
1. **Type II (§3).** Lemma 3.1, `(2ai+j)(2bi−j) = −e(1+2ck)` in `(−d,−p)`, was checked by explicit quaternion
   multiplication on all 3303 ordered Type II solutions with p < 1500.
   * Ideal reading (PROVED, local). `ℤ⟨i,j⟩` has discriminant 4dp. At primes ℓ of e, Type II means
     `im β̄ = ker ᾱ` in `ℙ¹(ℤ/ℓ^k)`: two composable cyclic e-isogeny structures, i.e. a Brandt `T_e` adjacency.
   * **Decisive answer: the residual condition is SPLIT** (Prop 3.2, PROVED). Type II at level d holds iff
     `m = (p+e)/4d` has a divisor a with `a + m/a ≡ 0 (mod e)`, i.e. `X² − Y² = 4m`, `e | X`. This is the same divisor
     problem as Type I.
   * The ES elements lie on the line `{2xi + j}`, where the norm is the one-variable polynomial `4dx² + p`. So no
     definite form arises, and the level-aspect quantification has nothing to act on (§6).
   * §3.3 gives the supersingular reading: disc −4dp CM points, i.e. E with a degree-d isogeny to `E^{(p)}`
     (standard facts, cited). ES-goodness is a property of a form representative, not of the CM point, so it cannot
     factor through reduction mod p.
2. **ET Prop 1.6 and square-mimicking primes (§4, PROVED).**
   * Both dictionaries fail at n = p², via the genus characters. For Type I the algebra is unramified at p; for
     Type II, `(n/f) = −1` is impossible.
   * Hence everything quaternionic here is congruence/genus data, inside the scope of Theorems M/C.
   * Square-mimicking primes are consistent with this and give nothing new.
3. **GZ/GKZ sum over x (§5, Prop 5.1; R130 repair).** The GZ local-factor citation was misapplied: GZ assumes coprime
   fundamental discriminants. It is replaced by a direct PROVED count. The weighted number of pairs (E, Λ ↪ End E) is
   `#{maximal orders ⊇ Λ} = ∏_{ℓ^k∥e} N_ℓ`, which equals `2^{ω(e)}` for squarefree e (Eichler level ℓ at ℓ ∥ e) and is
   independent of p and m.
   * Explicit counterexample: `(d,e) = (5,23)`. Here p = 313 has ES at that (d,e) and p = 73 does not, yet e, the
     characters and the x = 2 count (= 2) are the same.
   * Summing over (d,e) gives a congruence-weighted divisor sum in e. The class-number product of the full GZ
     quantity needs the ≍ √(dm) values of x, and forcing x = 2 kills it.
   * EVIDENCE (`quat_residual.py`), for p ≡ 1 (24), p < 1500, d ≤ 12, e < 60, with all collision/genus data in place:
     the divisor condition holds in 40/93 Type I cases and 120/450 Type II cases.

## Verdict (Assessment; PROVED parts listed in QUATERNION_ES §6)
The quaternionic dictionaries exist and are exact: Type I is an x = 2 collision (relative-trace-1 order of reduced disc pe) in `B_{p,∞}`, and Type II is a
non-commutative factorisation in `(−d,−p)` with matched level-e structures. But the level-p object carries only
congruence/genus data. The ES difficulty stays in an isotropic divisor-in-residue-class problem whose modulus e is
a coordinate of the solution. Michel/EMV/Kane/LMY have nothing to equidistribute that is not automatic.

Scope of the negative statement: these encodings, i.e. p entering as ramified prime / Frobenius and the witness being
CM endomorphisms with fixed relative trace. It is not a theorem about all conceivable quaternionic encodings.

Recommendation: close O130 as a precise negative result with a nice structural dictionary (Prop 1.3 is worth one
ledger entry). No claim about ES itself.
