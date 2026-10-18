# R287 — hostile review of POWER_LADDER_ES.md (O276, k-th power relaxation ladder)

**Repairs applied** (author branch quiet since its final report commit 32fa2bfc): D1–D6 marked '(R287 repair)' in
POWER_LADDER_ES.md (§2.1, §2.2, §6, §7) and AGENT_REPORT_O276.md; D5/D7 also in memos z44_tes_ladder, z44_neutral_odd_mute.
Verdict: no FATAL, no MAJOR, 7 MINOR.

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

### §6 TES_(k) — SOUND-AFTER-REPAIRS
* T1₃ bit: with D = Q^k in lowest terms, v_q(z) = −k·v_q(Q) for every q | Q, so 3 | k ⇒ (N_q) of SPARKS2 §3 holds and
  TES_(k) ⊂ TES^{□₃}; Thm 3.3 applies ✓. For 3 ∤ k the tame symbol (ωx/y)^w is unconstrained ✓ — but this proves only
  "no T1₃ constraint FROM the mute places"; that T1₃ actually FAILS is proved only for k = 1, 2 by the exhibited Type
  II-shaped solutions at cubes (table) — see D5.
* Index bit: Prop 3.1 of SPARKS2 with D = Q^k fires iff Q^k ≡ −n/18 (mod g), O/g ≅ F_ℓ, index gcd(k, ℓ − 1) ✓. Every
  class prime has ℓ ≡ 1 (18): N(g) ≡ N(10 + ω) = 91 ≡ 1 (mod 18) since g ≡ g₀ (18) ⇒ ḡ ≡ ḡ₀ (18) ✓; no inert or ramified
  prime lies in the class (checked: p·unit ≢ 10 + ω). N(−8 + ω) = 73, 72 = 2³·3² ✓. Q may be taken rational odd (rational
  Q cover F₇₃ and are ≡ 1 (mod 2O)), so D ≡ 1 (2) as SPARKS2 Prop 3.1 requires ✓. Lowest terms automatic: a = −1 for this
  g, Z = −nx, and q | Q, q | x ⇒ q | ωna ⇒ q | n ✓ (verified in the script).
* Table reproduced exactly; k = 3, cubes 0/412 is also forced by Cor 3.4 (18 never a cube mod a class prime).
* "Finitely many fixed shots never cover TES_(2)" (CRT on quadratic classes at distinct g_i) ✓ for the g-shot family.
  I also checked the other obvious fixed-modulus family, the x = y identity 9/n = ω/x + ω²/x + 2D/(nx) with
  9x = 2D − n (ω/x + ω²/x = −1/x; x ≡ 1 (2O) automatically): it fires iff n/2 ∈ ((O/9)^×)^k; in (O/9)^× (order 54) the squares have index 2 and the
  cubes index 27 (2 is not a cube — consistent with T1₃ at k = 3), so it does not cover TES_(2) either. So the author's
  conclusion survives one more family, but the general wording overreaches (D6).

### §7 the direct test — SOUND-AFTER-REPAIRS
r = 3: y = n(r+1)/4 = n, e = (n + 4Q³)/3, x = (n + e)/4 = (n + Q³)/3 ✓; 1/x + Q³/(nx) = 3/n ✓; Q ≡ −n (3), odd, prime to n,
lowest terms ✓; Type II ✓ (reproduced for all n ≤ 10⁶ prime to 3, k = 3, 5, 7). r = 11 for 3 | n ✓ (gcd(3, 10) = 1) —
but see D4 for 33 | n. Cubic-residue direction (r ≡ 1 (3)) correctly identified as index 3, unnecessary.

## Numbered defects

No FATAL, no MAJOR. Every theorem was re-proved and every number reproduced from scratch.

* **D1 (MINOR, framing) — §2.2 "Reading", AGENT_REPORT SHARP 1 ("the ladder carries exactly one bit: k mod 2").** By
  Cor 2.5 all rungs coincide AS PREDICATES ON n (all true at every n ≥ 2), so the ladder carries zero bits of truth; the
  k mod 2 bit is mechanism-level (T1 present/absent ⇒ Type I/II-shaped finite covering possible vs. one Dirichlet prime +
  scaling). *Repair:* say "one bit of mechanism (T1 / shaped-covering), zero bits of truth (Cor 2.5)".
* **D2 (MINOR) — Thm 2.1, "distinct-denominator variant".** The split 1/x = 1/(x+1) + 1/(x(x+1)) can destroy the Type I
  shape: n = 13, k = 5, Q = 3, x = 64: 4/13 = 1/65 + 1/4160 + 3⁵/832, and 13 divides all three denominators to the first
  power (not Type I/II at 13). *Repair:* add "(the shape claim refers to the (2x, 2x) form)".
* **D3 (MINOR) — Cor 2.2 "the rung is a finite covering … Q = 7 serves …".** With Q = least Q ≡ −n (4) prime to n, Q is
  unbounded over composite n (n divisible by 3·7·11·19·…), so this is not literally a finite congruence covering.
  *Repair:* a genuine finite covering with Q ∈ {1, 3}: n ≡ 3 (4): Q = 1; n ≡ 1 (4), 3 ∤ n: Q = 3; 3 | n: ES(3)
  (4/3 = 1/1 + 1/4 + 1/12) scaled by n/3; even n by scaling/ES(2^a).
* **D4 (MINOR) — §7 "r = 11 for 3 | n"; valuation formula.** r must not divide n, so r = 11 fails at 33 | n (use r = 23,
  or scaling from ES(3)/ES(11), or simply Thm 2.1). The formula "v_q(z) = 2v_q(r+1) − 3v_q(Q)" holds only when
  v_q(r+1) < 3v_q(Q) (else v_q(z) ≥ 0). *Repair:* "r ∈ {3, 11, 23} (each ≡ 3 (4), ≢ 1 (3)) covers every n prime to 3·11·23
  … or: by scaling"; add the case split.
* **D5 (MINOR, overclaim / missing one-line proof) — AGENT_REPORT SHARP 3 and memo z44_tes_ladder ("T1₃ ⟺ 3 | k").**
  POWER_LADDER §6 proves only ⟸ and "no constraint from the mute places" for 3 ∤ k; failure of T1₃ is exhibited only for
  k = 1, 2. The converse is easy and should be stated with its proof: *if 3 ∤ k, TES_(k) has Type II-shaped solutions at
  cubes.* Proof (relative to Hecke, as SPARKS2 Cor 3.4): fix a class prime g of norm ℓ; H_k = (F_ℓ^×)^k has index d =
  gcd(k, ℓ − 1) prime to 3, the cubes C₃ have index 3, so C₃·H_k = F_ℓ^× and every coset of H_k, in particular −18·H_k, contains a cube t³;
  take (Hecke) a prime π ≡ t (mod g), π ≡ 1 (mod 2), π ∤ 6; then −π³/18 ∈ H_k, the g-shot fires at n = π³ and SPARKS2
  Prop 3.1 gives a Type II-shaped TES_(k)(π³) solution, which T1₃ (Thm 3.3 form) would forbid. *Repair:* add this
  as a Proposition (PROVED rel. Hecke) to §6, or weaken the report/memo wording to "T1₃ for 3 | k; no mute-place T1₃
  for 3 ∤ k".
* **D6 (MINOR, scope) — §6 "Reading" ("'no T1 ⟹ finite covering' is FALSE within fixed-modulus shot families").** Proved
  only for finitely many SPARKS2-Prop-3.1 g-shots. Families with modulus at the anchor (O/2O)^× = F₄^× (odd order 3, so
  squaring is bijective there) or at λ are not excluded by the CRT argument. I checked the x = y family (modulus 9,
  index 2 for k = 2: does not cover either), so the claim survives one more family, but the general wording is
  unproved. *Repair:* "within the g-shot family of SPARKS2 Prop 3.1 (and the mod-9 x = y family)", and keep "OPEN" for
  other identity families.
* **D7 (MINOR, wording) — memo z44_neutral_odd_mute "a T1-bearing rung strictly between ES^□ and ES_(1)".** Strict as solution
  sets, not as predicates on n (Cor 2.5). *Repair:* "strictly between, as solution sets".

## Labels
All PROVED labels (Thm 2.1, Cor 2.2, Thm 2.3, Lemma 2.4, Cor 2.5, Prop 3.1, §4 inspection claims, Thm 5.1 per q,
Prop 5.2, §6 bits, §7) are correct; Thm 2.3/Cor 2.5 rest on Dirichlet (stated). CERTIFIED (q ≤ 10⁶) and EVIDENCE (§2.3,
§6 table, §7 table) are reproduced exactly. CONDITIONAL (GRH/Lenstra) adequately hedged; source not accessed. "Reading"
paragraphs are Assessments and labelled so. Nothing claims ES or an infinite family of ES; the headline "pointwise
ES_{Q³}" is correctly downgraded to "true for a trivial reason".

## Bottom line
O276 is correct. The flat-ladder theorems, the (J)107 calibration repair, the one-mute-prime dichotomy and the TES table
all survive a hostile from-scratch check. Seven MINOR wording/scope defects; the one substantive addition is D5's
three-line proof that T1₃ fails for every 3 ∤ k, which upgrades the report's "T1₃ ⟺ 3 | k" from overclaim to theorem.
