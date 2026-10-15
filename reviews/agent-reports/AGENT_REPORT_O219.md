# AGENT_REPORT_O219 — FF class-divisor machinery over ℤ: explicit sterile Mordell points (STERILE_EXPLICIT.md)

Status: checkpoint 2 (deliverable finished, self-reviewed, repairs applied, tables regenerated with the repaired engine).
Nothing here proves ES or any case of it. Sterility = "in no class of the seven ET Prop 1.9 families".

**SHARP:**
1. **Theorem 3.4 (PROVED, computer-assisted): for every prime r ≥ 2³² ≈ 4.3·10⁹ the r-generic line has sterile points in the
   non-residue cells, so no finite ET covering handles all large primes with least quadratic non-residue r.** (J)26 had this only
   for an ineffective/tower r₀. Certificate: measure criterion (S) with max S = 0.48670 < 0.49999 (`data/se/r0_certify.txt`, regenerated tables), `scripts/se_certify.sh` replays everything (~3.5 h, 2 cores).
2. **Coppersmith interpolation (Cor 1.4, PROVED, elementary via Minkowski):** divisors of n of size n^β in a unit class mod n^ρ
   number ≤ n^{max(0, β(1−β)−ρ)+o(1)} with explicit lattice constants (cut the size window into J pieces). Below the
   Coppersmith threshold it replaces the divisor function.
3. **With it, the ℤ P-count (Type II solutions of 4/r^K) has exponent 2/5 (ET's) with *no* divisor-function loss except 2^{ω(e)} = N^{o(1)} (R222 repair m6) and a τ₃
   envelope on the single integers (N+e)/4, tolerated up to η = 0.3** (grid EVIDENCE). ET's own argument tolerates η ≈ 1/18 —
   that is why (J)26's r₀ was a tower.
4. **FF feedback (grid EVIDENCE):** interpolation + divisibility-averaged pairs (#{(v₁,w₁): w₁ | T^{s−2}+v₁} ≤ q^{max(deg)})
   give O216's exponent −0.083 at q = 27 (closes r = 3 at exponent level; O220 has since closed q = 27 by its "division trick",
   whose ℤ twin is exactly my averaged-pair routes), and exactly 0.000 at q = 3, 9 (thirds corner).
5. Exact dictionary of equations (R222 repair m7: side conditions differ, T ∥ w, C in (B) vs r ∤ abcde in-cell): O216 Case B tuples (m', g', w, C, v) ↔ ℤ P-data (4d, c, a, b, e); O216 Lemma 1.1(i) ↔ ef = N + 4a²d.

## What limits r₀ = 2³², and r = 13, 17
* At r ≈ 2³² the dominant term is the level-1 Q term 2D_Q(r)/r ≈ 0.35 (Type I solutions of 4/r bounded by box sums with
  exponent ≈ 0.6 but (log r)² boxes; true count is a few hundred). P at K = 1: 0.025; P tail beyond N = 2^{600}: ≈ 0.1.
  The certificate fails at b = 31.5 (S = 0.58).
* r = 13: all six non-residue cells are covered at level 1 (POINTWISE_MORDELL §1) — no sterile 13-generic point. r = 17: union
  bounds of any known kind need a P-count constant ≲ 2.5 at θ = 0.4 (M17D §1); the certified engine's bound/√N peaks ≈ 931 near N ≈ 2^{38.75} (R222 repair m4: was 820).
  Not reachable by this method; honest negative (Assessment).

## Self-review (codex deep, `reviews/sterile-explicit-review.md`)
No FATAL. M1 (floating point not provably outward-rounded; non-finite values not fail-closed) and M2 (no provenance of tables)
repaired: dyadic exact-power boxes only, directed 1e-15 padding of every lower/upper bound before floor/ceil, 64-bit long double
checked, error budget stated in se_box.c header, NaN/duplicate/domain checks in se_r0.py, `se_certify.sh` + `data/se/MANIFEST.txt`,
tables regenerated. Minors (negative Q tail exponents — capped at 0; τ notation → monotone envelopes; wording) repaired.
**A fresh hostile review by the parent is still needed**, especially of se_box.c route bounds and se_tail.py's all-N argument.

## Files
STERILE_EXPLICIT.md (§0 log, §1 lemmas, §2 route table, §3 certificate/Theorem 3.4, §4 FF feedback (renumbered from §5, R223)); scripts se_box.c (engines,
validation mode), se_box_check.py (exact counts vs per-box bounds: 0 violations), se_cop_check.py (Cor 1.4 vs brute force: 0
violations), se_tail.py, se_r0.py, se_certify.sh, se_rate*.py / se_ff_rate.py / se_proto.py (steering only); data/se/.

## Sparks
* Lower r₀ further: a sharper level-1 Q count (Type I solutions of 4/r for prime r) — e.g. exploit r prime, or certify level 1
  per-r for r in [10⁶, 2³²) by enumeration plus the general bound for k, K ≥ 3 (the K = 3 P term is fine from r ≈ 10⁸).
* Rigorous FF certificate of §4 (was §5) for q = 27 (now superseded by O220?) and the q = 3, 9 thirds corner with a sub-exponential count.
* The P tail threshold 2^{600} costs ≈ 0.1 of S at r = 2³²; a finer tail mesh (M = 48) would buy room for b = 31.
