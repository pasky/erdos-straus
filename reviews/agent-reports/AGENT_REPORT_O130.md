# AGENT REPORT O130 — quaternionic / supersingular reformulation (checkpoint 1)

Branch `side-agent/quaternion-es`; file `QUATERNION_ES.md`; script `scripts/quat_typeI.py` (log `logs/quat_typeI_3000.txt`).
(Branch also contains the merges of side-agent/geometry-es and side-agent/typeii-spectral, as instructed.)

## Results so far
1. **Type I dictionary exists (PROVED, Prop 1.3).** Every Type I solution `(a,b,c,d)` gives the order
   `Λ = ℤ⟨u,v⟩`, `u² = −d`, `v² = −ab`, `uv+vu = 1`, of reduced discriminant `4abd − 1 = pe`, inside an algebra
   that is **exactly `B_{p,∞}`** (Hilbert-symbol proof; the step at primes of e uses `e | 4a²d+1`). So the CM points
   of discriminant −4d and −4ab collide mod p, with **x = 2**: `(D₁D₂ − 4)/4 = pe` (R130 repair: x is GZ/Lauter–Viray
   notation only; GZ's theorem assumes coprime fundamental discriminants, which −4d, −4ab are not; `p ∤ e` made
   explicit in the proof).
   EVIDENCE: all 19690 Type I solutions (ET-normalised triples) with p < 3000 (log `logs/quat_typeI_3000.txt`); other splits
   (ad|b, bd|a, 1|abd) fail in 27–42% of cases.
2. **Isogeny form (PROVED, §2).** ES Type I ⟺ supersingular E, E', `u ∈ End E` (u² = −d), orthogonal
   `φ₁, φ₂ ∈ Hom(E',E)` with `tr(uφ₂φ̂₁) = 1`, such that the index e of `L = ⟨φ₁,φ₂,uφ₁,uφ₂⟩` in `Hom(E',E)`
   (Gram `[a,1,bd] ⊥ [b,−1,ad]`) divides `deg(φ₁+φ₂) = a+b`.
3. **Negative structural finding (PROVED, Prop 2.2).** The quaternionic side is congruence data: for fixed (d,e)
   the collision exists automatically once `p ≡ −e^{−1} (mod 4d)` and the genus conditions hold, and
   `m = ab = (pe+1)/4d` is then determined. All ES content is the split divisor problem
   "m has a divisor a with a + m/a ≡ 0 (mod e)" (`X² − Y² = 4m`, `e | X`) — the same shrinking-target shape as
   GEOMETRY_ES Prop 4.1. Assessment (R130 repair: heuristic, not part of the PROVED content): theta/Siegel-theta
   coefficients of `B_{p,∞}` do not absorb it (the condition selects which Gram matrices to sum over). Assessment: for Type I, "p as level" is a re-encoding, not a new regime.
4. **Type II is genuinely quaternionic (PROVED identity, Lemma 3.1).** In `(−d,−p)` (i²=−d, j²=−p, k=ij):
   Type II ⟺ `(2ai + j)(2bi − j) = −e(1 + 2ck)`, with norms ef, ef', ff' = 1 + 4c²dp (O128's shell). Type I is
   the commutative analogue `(1+2ai)(1+2bi) = e(2ci + j²)` (ET dilation `1 ↔ j`).

## Next steps (if the parent wants me to continue)
* §3: develop Lemma 3.1 as an ideal-theoretic statement in the level-4dp order `ℤ⟨i,j⟩` (left ideals of norm e;
  Brandt-matrix/Hecke reading of "αβ ∈ e·ℤ[k]"); test whether Type II's residual condition is *also* split
  (expected by GEOMETRY Prop 3.2, which would give a Type II analogue of Prop 2.2) or whether non-commutativity
  gives a genuinely definite (theta-coefficient) condition.
* Check against ET Prop 1.6 (n = p²) and square-mimicking primes explicitly (Type I: automatic via (−d/p)).
* Level-aspect quantification (Michel / EMV / Kane / Liu–Masri–Young) only if §3 yields a definite condition.

No claim about ES itself; nothing here is CONDITIONAL on unproved hypotheses.
