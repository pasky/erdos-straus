# R287 — hostile review of POWER_LADDER_ES.md (O276, k-th power relaxation ladder)

Reviewer branch side-agent/review-power-ladder (merged side-agent/power-ladder-es @ 32fa2bfc). All checks below are
from-scratch (scripts/review_r287_*.py, logs/review_r287_*.txt); the author's scripts were read only to learn the
TES 2-primary normalisation convention.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Def 1.1 / Remark 1.2 (exact definition, lowest terms forced) | **SOUND** |
| Thm 2.1 / Cor 2.2 (odd k: mod-4 covering, T1 dead) | **SOUND** (MINOR D2, D3) |
| Thm 2.3 / Lemma 2.4 / Cor 2.5 (even k = ES^□; all n) | **SOUND** |
| Prop 3.1 (index formula; repair of (J)107 §3.2) | **SOUND** (formula PROVED; repair is a fair Assessment) |
| §4 cap relation | **SOUND** |
| Thm 5.1 / CERTIFIED / Prop 5.2 (one mute prime) | **SOUND** (Lenstra not accessed; CONDITIONAL label adequate) |
| §6 TES_(k) bits + EVIDENCE table | **SOUND-AFTER-REPAIRS** (MINOR D5, D6) |
| §7 fixed shot r = 3, 11 | **SOUND-AFTER-REPAIRS** (MINOR D4) |
| §2.3 / §7 numerics | **SOUND** (every number reproduced from scratch) |

## Numerical reproduction (from scratch)
* `scripts/review_r287_flat.py 1000000` (42 s, `logs/review_r287_flat_1e6.txt`): own implementation, exact Fraction check of
  4/n = 1/x + 1/y + 1/z, den z recomputed and tested to be Q^k (Q odd, gcd(Q, n) = 1), shape recomputed from valuations.
  * odd k = 1, 3, 5, 7 (Thm 2.1): all 78 497 odd primes ≤ 10⁶, 499 odd squares, 49 odd cubes: OK, Type I at every prime
    of n in all 79 045 cases, max Q over primes = 3.
  * even k = 2, 4, 6, 8, 12 (Thm 2.3): all primes p ≡ 1 (4) ≤ 10⁶ solved with Type II shape both by the first firing
    r ≡ 3 (4) and by the theorem's r ((p/r) = −1, r ≢ 1 mod odd primes of k). Max theorem-r: 131 (k = 2, 4, 8), 251
    (k = 6, 12) — matches the author's 131 / 251. (First-firing r for k = 6 can be ≡ 1 (3) when −p/4 happens to be a
    cube: max 191.)
  * T1 control: 0 shots fire at the first 200 odd squares × 200 primes r ≡ 3 (4) for k = 2, 4, 6.
  * §7 fixed shots (k, r) = (3, 3), (3, 11), (5, 3), (5, 23), plus (7, 3), (9, 11): every prime/odd square/odd cube ≤ 10⁶
    prime to r solved, Type II everywhere. (My max Q differs from the author's (23 vs 11 for r = 3) only because I do not
    exclude squares divisible by 11; immaterial.)
* `scripts/review_r287_tes.py 3000` (`logs/review_r287_tes.txt`): own ℤ[ω] arithmetic; table of §6 reproduced exactly
  (k = 1: 412/412 primes and cubes; k = 2: 209/412 both; k = 3: 134/412 primes, 0/412 cubes), all Type II, and the
  firing set agrees exactly with the criterion "−n/18 ∈ (F₇₃^×)^k" (ω ↦ 8). Lowest terms gcd(Q, Z) = 1 verified;
  a = (g + ω²)/9 = −1 for g = −8 + ω. All class primes g ≡ 10 + ω (18) with N(g) ≤ 3000 have N(g) ≡ 1 (18).
* `scripts/review_r287_mute.py 1000000 1000000` (`logs/review_r287_mute.txt`): 19 564 primes q ≡ 1 (12) ≤ 10⁶ all have a
  witness g ≡ 3 (4) with q a primitive root, max least g = 179 at q = 432 793 (= author); q = 13, g = 11: 78 914 n (all odd
  primes ≠ 11, 13 and odd squares prime to 143, ≤ 10⁶) solved exactly with den z a power of 13, max c = 9 (= author);
  Prop 3.1(a) index formula: 0 mismatches by brute force over all odd squarefree U < 200, k ≤ 12; all six explicit
  identities of §2.3/§5.2 (numerator 8 at 131, 241; 4/5 = 1/58 + 1/5 + 13²/290) are exact with the stated den z.
* `scripts/review_r287_counts.py 1000000` (`logs/review_r287_counts.txt`): least r for k = 2: 3, 7, 11, 19 for 19 611,
  9 825, 4 948, 2 444 primes, max 131; Q = 1 shot fails at 9 841 primes p ≡ 1 (4) — all equal to §2.3.

## Claim-by-claim

### Def 1.1, Remark 1.2 — SOUND
* Def 1.1 is exactly UNIT_ORBIT_ES §1's ES^{(S)} normalisation (v_q(z) ∈ 2ℤ whenever v_q(z) < 0, z ∈ ℤ[1/S], S odd and
  prime to n) with 2 → k and S = all odd primes ∤ n; for k = 2 it is literally SPARKS2's ES^□. So it is the natural
  reading of "third denominator carrying a k-th power factor", not a looser one.
* Remark 1.2 re-derived: A/B (lowest terms) = Q^k/Z with Z ∈ ℤ ⟺ Z = BQ^k/A ∈ ℤ ⟺ A | Q^k (gcd(A, B) = 1); Q = A works.
  So dropping gcd(Q, Z) = 1 makes the rung k-independent ("numerator of 4/n − 1/x − 1/y odd and prime to n"), and every
  stricter reading (Q tied to y, Q bounded, Q from a fixed S) is a different relaxation (treated in §4–§5). The
  definitional question raised in the brief is therefore answered correctly: the odd-k collapse is NOT an artefact of a
  sloppy definition — it is the genuine content of the lowest-terms k-th-power rung, and it is trivial because ES_(1) is
  (and Q^k ≡ Q (mod 4)), as the author says.
* Monotonicity ES_(k) ⊂ ES_(j) for j | k: immediate (Q^k = (Q^{k/j})^j).

### Thm 2.1, Cor 2.2 — SOUND
Re-proved: Q odd ⇒ Q^k ≡ Q (mod 4) for odd k, so 4 | n + Q^k; 1/(2x) + 1/(2x) + Q^k/(nx) = (n + Q^k)/(nx) = 4/n; q | Q,
q | x ⇒ q | 4x − Q^k = n, contradiction, so the third term is in lowest terms with den = Q^k, Q odd, prime to n — a valid
ES_(k) instance in the exact sense of Def 1.1. Type I at every ℓ | n (ℓ ∤ 2x, v_ℓ(nx) = v_ℓ(n)). Even n and 2^a: checked
(4/2^a = 1/2^{a−1} + 1/2^a + 1/2^a). Numerically: Type I at every prime for all primes, odd squares, odd cubes ≤ 10⁶,
k = 1, 3, 5, 7 — the T1 death at odd k is directly witnessed (squares with Type I shape), consistent with UNIT_ORBIT_ES
Lemma 1.1 case (i) with w odd. Defects: D2 (distinct-denominator variant loses the shape), D3 (wording "finite covering").

### Thm 2.3, Lemma 2.4, Cor 2.5 — SOUND
Re-proved every step. n₀ ≡ 1 (4) squarefree > 1 has a prime ≥ 5 (n₀ = 3 is ≡ 3 (4)). The class a: at ℓ = 3 | gcd(n₀, k′)
the only class ≠ 0, 1 is 2 with (2/3) = −1; at ℓ ≥ 5 the classes ≠ 0, 1 contain the residue 4 and non-residues, so the
total Jacobi sign can be fixed; ℓ | L get a ≡ 2. Jacobi reciprocity with n₀ ≡ 1 (4) gives (n₀/r) = (r/n₀) = −1, and
r ∤ m gives (n/r) = −1, so −n/4 is a non-zero square mod r ((−1/r) = −1). (r − 1)/2 odd and prime to k′ ⇒ gcd(k, r − 1)
= 2 ⇒ (F_r^×)^k = (F_r^×)². Identity: 4rx = r(n + e) = n(r + 1) + 4Q^k, and 1/x + 1/y + 4Q^k/(nx(r + 1)) =
(n(r + 1) + 4x + 4Q^k)/(nx(r + 1)) = 4x(r + 1)/(nx(r + 1)) ✓; e ≡ −n (4) since r ≡ 3 (4); den z = Q^k exactly because
q | Q, q | x ⇒ q | n(r + 1). The self-repair "for n ≡ 3 (4) such an r need not exist" is correct (n = 3, k = 6: r ≡ 2 (3)
and r ≡ 3 (4) force r ≡ 11 (12) and then (3/r) = +1). Lemma 2.4: m odd, Q prime to m ⇒ gcd(m, 2Q^{k/2}) = 1 ⇒ no prime
factor ≡ 3 (4) ✓ (and 0 firings observed). Cor 2.5: n = s^{2^j}, s non-square; scaling by n/s (a power of s, prime to Q)
preserves lowest terms ✓. The scaled solution at a square is not Type I/II-shaped at the primes of s (v_ℓ(x·n/s) =
v_ℓ(n/s) ∉ {0} ∪ [v_ℓ(n), ∞)), so no conflict with T1 — the author's remark that the ledger's "ES^□ at every non-square"
is the scope of the shaped construction, not of the truth of ES^□, is correct and worth a ledger note.

### Prop 3.1 and the (J)107 repair — SOUND
(a) G ≅ C₂ × ∏_{ℓ | U} C_{ℓ−1} and [C_m : C_m^k] = gcd(k, m) ✓ (brute force agrees). (b) single-shot index gcd(k, g − 1)
✓, = gcd(k, 2)·gcd(k, (g − 1)/2) as (g − 1)/2 is odd ✓. (c) index 1 ⟺ k odd ✓. The D8 asymptotic ratios quoted in §7
re-derived: k = 3: ½; k = 4: ½ log 8/log 3 = 0.946; k = 6: ½ log 12/log 3 = 1.131; k = 8: (7/4) log 2/log 3 = 1.104 ✓.
The repair: LOWER_TAIL_FABLE §3.2 itself identifies its H = squares rung with ES^□ ("that relaxation (ES^□ of (J)28)"),
so identifying its H = k-th-powers rungs with ES_(k) is the faithful reading, and then its conclusion "the only provable
member of the ladder is k = 2" is refuted by Cor 2.5 (every k is a theorem at every n). The diagnosis (the solver chooses
the modulus; calibrate at the best single modulus, index 1 or 2) is a fair Assessment and consistent with R286 D7.

### §4 cap relation — SOUND
CAP_POINTWISE normalisation (den z = r², r odd, gcd(r, n) = 1, rad r | y, v_ℓ(r) ≤ e) gives ES^{(y,e)} ⊂ ES_(2) and the
stated ES_(4) intersection ✓. The constructions have gcd(Q, x) = gcd(Q, y) = 1 (Thm 2.1: y = 2x; Thm 2.3: gcd(Q, n(r+1)) = 1
and q ∤ x), so they are never cap solutions ✓. The key repaired point (ii) re-derived from UNIT_ORBIT_ES Lemma 1.1: if
q | y and v_q(z) < 0 then case (iii) is impossible, so q | x (case (ii)), −y/x ≡ 1 (mod q) and inv_q = 0 for ANY w — the
cap tie kills the parity bit; T1 survives odd exponents under the tie ✓.

### Thm 5.1, CERTIFIED, Prop 5.2 — SOUND
All three branches re-derived: q ≡ 3 (4): 4x = n + q, q ∤ x; q ≡ 2 (3): 3x = n + 1 (ES) / 3x = n + q, 4/n = 1/n + 1/x +
q/(nx); witness g: UNIT_ORBIT Prop 2.1 with Q² → q^c works for every n prime to g, even or odd (e·g ≡ n (4), g ≡ 3 (4)
⇒ e ≡ −n (4)), den z | q^c. Leftover n = t^a m by scaling ✓; t^a alone by ES ✓. Certificate reproduced exactly (above).
Prop 5.2: example exact; with g ≡ 3 (4), −m²/4 is a non-residue ✓; the "sufficient route" phrasing after self-repair is
accurate (note ord_g(q²) = (g − 1)/2 also allows ord_g(q) = (g − 1)/2, not only primitive roots — consistent with the text).
Lenstra 1977 (Invent. Math. 42) was NOT accessible to me; the label CONDITIONAL "citation-level" is appropriate and the
claim is never used (each q ≤ 10⁶ is certified). My own sanity check of non-vanishing of the density: the conditions are
Frobenius ≠ 1 on ℚ(i) and on every ℚ(ζ_ℓ, q^{1/ℓ}); the only quadratic entanglement is ℚ(√q) ⊂ ℚ(ζ_q), and ℚ(i, √q) has
group C₂ × C₂, so the two conditions at 2 are compatible — no obvious obstruction.
