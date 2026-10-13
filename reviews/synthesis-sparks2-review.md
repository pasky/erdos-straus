# R193 — hostile review of SYNTHESIS_SPARKS2.md (O192, spark synthesis II)

Reviewer branch side-agent/review-synthesis-two (merged side-agent/synthesis-two at the O192 checkpoint-1 commit).
From-scratch scripts: `scripts/review_syn2_sqden.py` (§2, plain ℚ arithmetic + own Hilbert symbols),
`scripts/review_syn2_eis.py` (§3, own ℤ[ω] arithmetic, own cubic residue / tame symbols). Neither imports the
author's scripts or `tw_eis.py`; sympy is used only for integer factoring and primality.

## Summary verdicts

| claim | verdict |
|---|---|
| §2 definition of ES^□, Lemma 2.1 | SOUND |
| §2 Prop 2.2 | SOUND (m1: actually Q < r) |
| §2 quantitative remark (GRH), label Assessment | SOUND |
| §2 Reading 2 ("positive proportion"; seed (ii) answer) | GAP — MINOR m2 |
| §3 Prop 3.1 | SOUND |
| §3 Definition + (N_q) remark | SOUND (m3) |
| §3 Lemma 3.2 | SOUND |
| §3 Thm 3.3 | SOUND (m4) |
| §3 Cor 3.4 | SOUND; hedge removable (u1) |
| §3 Thm 3.5 | SOUND |
| §3 EVIDENCE (1)–(4) | reproduced from scratch (m5 on (4)) |
| §4 (J)23 citation fix | SOUND (m6) |
| §4 "W" clash | SOUND (m7) |
| §1 dead verdicts X1, X5, X6, X9, X10 | SOUND as Assessments; X3 wording m8 |
| Recalibration "T1-bearing variant ⇒ weak evidence" | FAIR (scope caveat m8) |

Overall: **SOUND-AFTER-REPAIRS (minor only)**. No FATAL, no MAJOR.


## §2 — ES^□

**Definition.** S = all odd primes ∤ n; ES^{(S)}'s condition "v_q(z) even when negative, q ∈ S" together with
z ∈ ℤ[1/S] is exactly "z > 0 rational, denominator odd, coprime to n, and a perfect square". Matches the author's
displayed definition. ES ⊂ ES^{(S)} ⊂ ES^□ for finite S ∌ primes of 2n: correct.

**Lemma 2.1 — SOUND.** Re-derived. UNIT_ORBIT_ES Lemma 1.1 is purely local at q (cases (i)–(iii); only (i) uses
evenness of w), so it holds at every q ∤ 2n; a given solution involves finitely many q, so Hilbert reciprocity is
a finite sum. In Cor 1.2 the list of places is: ∞ (½, positivity), 2 (0, z ∈ ℤ_(2)), q ∤ 2n (0: either z q-integral,
Thm 2.1(b), or muted, Lemma 1.1), ℓ | n (variables ℓ-integral since the denominator is prime to n, so Thm 2.1(d)
applies). The class "odd ℓ ∉ S, ℓ ∤ n" is now empty, which is harmless. Nothing else in Cor 1.2 uses finiteness of S.
*Numerics (`review_syn2_sqden.py`, part C).* Brute force of ES^□(m²), x ≤ 2n, y ≤ 30n, every z with odd square
denominator prime to n: n = 9, 25, 49, 81, 225 give 72, 183, 336, 900, 5313 solutions, **0** with Type I/II shape
at every prime of m (n = 225: 3186 have it at one of 3, 5 — consistent, Lemma 2.1 only forbids "every prime").
On every solution I computed all Hilbert symbols (own implementation, ∞, 2, all odd primes): product formula holds,
inv_∞ = ½, inv_2 = 0, inv_q = 0 at every mute q, Σ_{ℓ|n} inv_ℓ = ½ — 0 failures. *Control* (odd **non-square**
denominators prime to n allowed): n = 9: 1597 / 2967 solutions are Type I/II at 3; n = 25: 16120 / 23087 at 5, with
nonzero mute invariants. So the square normalisation is exactly what carries the T1, as claimed.

**Prop 2.2 — SOUND.** Re-derived: n = n₀m² with n₀ > 1 squarefree, n₀ ≡ n ≡ 1 (mod 4) (m² ≡ 1 mod 8); CRT class
a mod 4n₀ with a ≡ 3 (4), (a/n₀) = −1; Dirichlet prime r ≡ a, r ∤ m; (n/r) = (n₀/r) = (r/n₀) = −1 by Jacobi
reciprocity (n₀ ≡ 1 mod 4, both positive odd); (−n/r) = +1, so 4Q² ≡ −n (mod r) is solvable with Q ≢ 0 (r ∤ n).
Of the two roots s, r − s exactly one is odd; adjusting by 2r makes Q prime to n (no prime of n divides 2r).
UNIT_ORBIT_ES Prop 2.1 uses r only through g ≡ 3 (mod 4), g | n + 4Q², and gcd(Q, n) = 1 (the parity step uses
q ∤ a, which follows from q | Q, q ∤ n). Part (a) (n ≡ 3 mod 4, Q = 1, g = n + 4) is UNIT_ORBIT_ES Prop 3.1. ✓.
Remark (MINOR m1): for p prime the odd root is < r, so the proof gives Q < r(p) (and needs no hypothesis p > 2r:
gcd(Q, p) = 1 holds whenever Q < p, and Q < r < p unless r > p, which happens only for tiny p). The stated
"Q < 2r for p > 2r" is true but slack.
*Numerics (part A, B).* All 17 982 primes 5 ≤ p < 2·10⁵ solved by my own implementation of the recipe, every
solution verified exactly (equation in ℚ, x, y ∈ ℤ_{>0}, z > 0 with odd square denominator prime to p, Type II shape);
max r(p) = 79 (p = 141 157), max Q = 77 < r; r(p) = 3, 7, 11, 19, 23, … for 4505, 2254, 1130, 561, 283, … primes
(geometric ratio ½, as for independent characters). n = 825: r = 7, odd roots < 14 are 3, 11 (both share a factor
with 825), least admissible Q = 17 — the self-review counterexample is correct. Re-run to 10⁶ (partA(10⁶), 2.7 s): 78 496 primes, max r(p) = 131 at p = 880 993, r-distribution
19 611, 9 825, 4 948, 2 444, 1 191, 624, … — identical to the author's figures; max Q = 97 < r.

**Quantitative remark (Assessment) — SOUND as labelled.** The least prime r with χ₋₄(r) = −1 and (n₀/r) = −1,
r ∤ n, is ≪ (log n)² under GRH (Bach / Lagarias–Montgomery–Odlyzko-type bound for a prescribed Frobenius in the
biquadratic field ℚ(i, √n₀); not re-derived, standard). Linnik gives n^{O(1)} unconditionally (one could even
cite Burgess-type bounds; immaterial). |S| ≪ π(2r) ≪ (log p)²/log log p ✓.

**Reading 2 — GAP (MINOR m2, an overclaim inside an Assessment).** "primes ≤ log p would need r(p) ≤ log p/2,
which is false for a positive proportion of p by the usual least-non-residue statistics". (i) *False as stated:*
heuristically and by the Chebotarev density of the independent characters, #{p : r(p) > y} / #{p} ≈ 2^{−π(y; 4, 3)},
which → 0 when y = (log p)/2 → ∞; the exceptional set has density 0, not positive density. Numerics (part D):
the fraction of p ≡ 1 (4) with r(p) > (log p)/2 is 0.50 near 10⁴–10⁶ (threshold between 3 and 7… i.e. "r(p) ≥ 7")
and drops to 0.25 near 10⁸ (threshold 9.2, "r(p) ≥ 11"), exactly 2^{−#{3, 7}}. The correct statement is "for
infinitely many p" (e.g. under GRH by a Linnik/CRT construction p ≡ square mod every r ≡ 3 (4) up to y with
log p ≲ (1 + ε)y; unconditionally only with a smaller constant). (ii) *Mechanism-specific:* "would need r(p) ≤ log p/2"
is a statement about the Q < 2r construction. Seed (ii) allows any Q ∈ ⟨primes ≤ log p⟩ with Q ≤ p^{O(1)}, and then r
can be large (one needs only −p/4 ∈ ⟨S⟩² mod r for some prime r ≡ 3 (4)); that question is not answered either way.
*Repair:* replace by "the Q < 2r(p) construction would need r(p) ≤ (log p)/2, which fails for infinitely many p
(density-zero set; Assessment); whether S = {primes ≤ log p} with larger Q ∈ ⟨S⟩ works is OPEN (an Artin-type
question with |S| growing)". The same overstatement sits in the report's SHARP 1 ("weaker than seed (ii)'s log p")
— fine if read as "we only proved the weaker form".

## §3 — order-3 TES over ℤ[ω]

All numerics below: `PYTHONPATH=scripts uv run --with sympy python scripts/review_syn2_eis.py 6000 100000 200 100`
(1.8 s; own ℤ[ω] arithmetic, own cubic residue symbols via reduction to F_p / F_{q²}, own tame symbols
((−1)^{v(A)v(B)}A^{v(B)}B^{−v(A)})^{(N−1)/3}, computed at **every** non-λ place, including the anchor 2).

**Prop 3.1 — SOUND.** Re-derived line by line: g₀ = 10 + ω ≡ 1 + ω = −ω² (mod 9) and ≡ ω (mod 2); gE ≡ n (mod 9)
⇒ E ≡ −ωn ⇒ 9 | ωn + E; ωg + 1 = ω(g + ω²) = 9ωa ⇒ gx = ωna + 2D ⇒ ω²x + 2D = x(g + ω²) − ωna = a(9x − ωn) = aE ⇒
ω²/y + 2/z = E/(nx) = 9/n − ω/x. Mod 2: a ≡ ω + ω² = 1, E ≡ ω⁻¹ = ω², x ≡ 1, y ≡ Z ≡ 1. Shape: π | n ⇒ π ∤ n + 18D
⇒ π ∤ E ⇒ π ∤ x. (Unstated but true: x ≠ 0, since x = 0 would give ωna = −2D, odd = even mod 2.) Numerically
verified exactly in K on all 1536 recipe solutions (below).

**Definition / remark on (N_q) — SOUND.** Re-derived: q | Q ⇒ q ∤ g, v_q(ωna) = s, v_q(2Q³) = 3c; s < 3c ⇒
v_q(x) = s, v_q(z) = 2s − 3c; s ≥ 3c ⇒ v_q(z) ≥ 0; q ∤ x ⇔ s = 0 ⇒ v_q(z) = −3c. Note (MINOR m3) that the weaker
normalisation is *necessary* for the shot family, not a cosmetic relaxation: on my 1536 recipe solutions, 68 of the
3044 mute places have v_q(z) < 0 with 3 ∤ v_q(z) (all with q | x). At order 2 this never happens (v_q(z) = 2s − 2c is
always even), so X11's "slightly weaker than O186's" undersells the asymmetry: at order 3 the strong normalisation would
reject Thm 3.5's own solutions. Suggest one sentence saying so.

**Lemma 3.2 — SOUND.** Re-derived: v_q(z) = −w < 0 ⇒ ω/x + ω²/y is q-integral ⇒ v_q(x) = v_q(y) = V;
v(A) = v(B) = V + w; symbol (−1)^{v}(ωx/y)^{v}, −1 a cube. V = 0: (N_q) ⇒ 3 | w = v. V > 0: v(ωy + ω²x) ≥ 2V ⇒
ω²y/x ≡ −1 (mod q^V) ⇒ ωx/y ≡ −1 ⇒ symbol (−1)^{2v} = 1. The order-2 parenthetical is UNIT_ORBIT_ES Lemma 1.1 case (ii),
which indeed does not use parity. Numerically: tame symbol 0 at all 3044 mute places.

**Thm 3.3 — SOUND.** The list of places in TWISTED_T1 Thm 3.2's proof: 2 (z ∈ 1 + 2O₂ since D ≡ 1 mod 2 — the
anchor computation uses only u_i ∈ U^{(1)}·c_i^{-1}, ✓), λ (u_i ∈ O_λ as S ∌ λ, ✓), tame v ∉ S ∪ {primes of n}
(integral ✓), v ∈ S (Lemma 3.2), π | n (π ∉ S so variables π-integral, DRINFELD_ES Thm 3.3's argument applies). ✓
*Numerical cross-check of the whole place list:* on all 1536 solutions inv_π = ω² ("2"), inv₂ = ω ("1"), every other
tame symbol 0, Σ_{non-λ} = 0 — hence inv_λ = 0 by reciprocity, independently confirming the partner step for
non-integral z. MINOR m4: Thm 3.3 is stated for n = π^{3k}; Thm 3.5's last sentence ("if n is a cube, none of Type I/II
shape at every prime (Thm 3.3)") needs the (immediate) extension to composite cubes: each π | n with 3 | v_π(n)
and Type I/II shape contributes inv_π = 0, contradicting Σ ≠ 0. Say so.

**Cor 3.4 — SOUND; and the hedge can be removed (upgrade).** The proof (Hecke prime π ≡ t (mod r), π ≡ 1 (mod 2)
in the ray class mod 2r; r ∤ 18 since r ≡ 2 (mod λ) and ≡ ω (mod 2); Prop 3.1 with D = 1, g = r at n = π³;
contradiction with TWISTED_T1 Thm 3.2(b)) is correct. The author's open point "K(∛18) ⊂ L (constancy on the class)
plausible, not checked" is in fact true by a standard conductor computation: K(∛18)/K is tamely ramified at 2
(v₂(18) = 1, conductor exponent 1) and at λ has v_λ(18) = 4 prime to 3, so the local Kummer extension of ℚ₃(ω)
(e = 2) has upper ramification break e·p/(p−1) = 3 and conductor exponent 4; hence the conductor divides
2λ⁴ = (18), K(∛18) ⊂ L, and (18/·)₃ is a character of the ray class group mod 18. *Numerics:* over all degree-1
primes N ≤ 10⁵ (all 6 associates), (18/r)₃ is a well-defined function of r mod 18 (0 conflicts, 162 classes),
consistent along μ₆-orbits; on the class g₀ it equals ω² for all 354 such r (author: 27 up to 6000, reproduced).
Suggested repair: replace "(A direct derivation … was not done.)" by the conductor argument (still label the value ω²
as EVIDENCE unless derived), and simplify Thm 3.5's proof (L' = L). A Cor-3.4-free remark worth adding: the
T1₃ control (3) is forced a priori — every prime r | π³ + 18Q³ has (18/r)₃ = 1 (−18 ≡ (π/Q)³), so every divisor g has
(18/g)₃ = 1 ≠ (18/g₀)₃.

**Thm 3.5 — SOUND.** Re-derived: h_K = 1 and μ₆ ↪ (O/18)^* make "generator ≡ g₀" one ray class; non-cube ⇒ some
π ∤ 6 with 3 ∤ v_π(n) (units ≡ 1 mod 2 are ±1, cubes); M = K(∛n) ramified at π, L' unramified outside 6 ⇒ L' ∩ M = K;
Chebotarev in the abelian L'M/K gives 𝔯 = (r), r ≡ g₀, r ∤ 6n, with (n/r)₃ = (18/r)₃ ⇒ −n/18 ≡ Q³ (mod r), Q ≢ 0;
CRT adjusts Q to be ≡ 1 (mod 2) and prime to 3n (all these primes ≠ r); Prop 3.1 with D = Q³ gives a TES^{□₃}
solution with Type II shape at every π | n and (N_q) at every q | Q. No quantifier problems: S = all primes ∤ 6n is
part of the definition of TES^{□₃}. *Numerics (from-scratch recipe):* all 1536 2-primary split primes N(π) ≤ 6000
(both 2-primary associates of all 768 prime ideals) solved, 0 failures (exact equation in K, 2-primarity of x, y, Z,
D, Type II shape at π, (N_q), tame census as above); least admissible r: max N(r) = 3187 (= author's figure);
my Q choice differs from the author's (max Q = 5327 vs 3671; immaterial).

**EVIDENCE items (3), (4).** (3) Extended: all 2-primary associates of all π with N(π) ≤ 200, D = Q³ for every
2-primary Q ∈ O with N(Q) ≤ 100 prime to 6N(π): 1632 shots, **0** divisors in the class g₀. *Control* with D = Q
(not a cube; Prop 3.1 still applies formally): 112 of 1632 shots have such a divisor — the cube in D is what carries
T1₃. (4) MINOR m5: "fires for only 52 of the 768" depends on which of the two 2-primary associates ±π is taken
(π + 18 and −π + 18 are different shots). Using the author's associate convention (`tw_eis.normalise` then the
first 2-primary unit multiple) my own divisor search reproduces 52/768; over all 1536 2-primary associates it is
117/1536, and 90 of the 768 prime ideals fire for at least one associate. Repair: state the convention, or report
"117 of 1536 (90 of 768 ideals)".

**§3 Reading — fair as Assessment**, with the m2-type caveat: "with a fixed finite S, it is an Artin problem (m = 3:
… CONJECTURE)" is correctly labelled. "TES finiteness is OPEN" ✓.

## §4 — ledger audit (X12)

**(J)23 citation — SOUND (already applied upstream).** Section (A) of DISCOVERIES has 9 items; "(A)19" does not exist.
(D)19 is the large-sieve cap (EXCEPTIONAL_LARGESIEVE, PROVED conditional on KARY2 Thm 5.1), (D)22 the prime-only
majorants (EXCEPTIONAL_PRIMELAW, PROVED), (D)24 removes the (log log N)^{3/4} loss in (D)18–(D)20, (D)22 (KARY3,
PROVED given K2/EK). The merged DISCOVERIES already carries the fix (commit 65f155f1, "citation corrected per O192").
MINOR m6: the new ledger wording "((D)19/(D)22/(D)24, conditional on KARY2 Thm 5.1)" attaches the KARY2
condition to all three; only (D)19 carries it in its own entry ((D)22: PROVED; (D)24: PROVED given K2/EK). Repair:
"((D)19, conditional on KARY2 Thm 5.1; (D)22; (D)24 for the form without the log log factor)".

**"W" clash — SOUND, and sharper than stated (MINOR m7).** Confirmed: (J)10 and (J)14 use W(n) for the signed
single-slice count; (J)15 and (J)20 use (W) for the sign-free Lorenzini property; (H)19/(H)22 (and (A)8, (A)9,
(C)16) use W(p) for the witness size. The audit misses that **(J)15 itself writes "W(n) is sign-free: n = xyz − x − z"**
(DISCOVERIES l. 632). So the same symbol W(n), not only the parenthesised (W), carries two meanings in adjacent
entries. Renaming (J)10/(J)14's count W_sl(n) and writing (W)(n) or Lor(n) in (J)15 would fix both.

**"Consistent on overlaps" list — spot-checked, SOUND.** (J)19 (1, 2, 0) = my inv₂ = 1, inv_π = 2, inv_λ = 0 on
1536 solutions (§3 above). (J)25 Cor 2.3 vs O188 §5 and (J)20 Prop 8.1 (p ≥ 13) read as stated in DISCOVERIES.
The others were checked by reading only.

## §1 — cross-combination screens (spot-check of the dead verdicts)

All §1 verdicts are declared Assessments in the §1 preamble; read as such, none is an overreach that would be
FATAL or MAJOR. Details:
* **X1 — SOUND (scoped).** Re-derived the conversion criterion: in UNIT_ORBIT_ES Prop 2.1 with g = r prime,
  v_q(z) = 2s − 2c for s = v_q(r + 1) < 2c and ≥ 0 otherwise, so z ∈ ℤ ⟺ s ≥ c for all q | Q ⟺ Q | (r + 1)/4
  (Q odd) ⟺ r ≡ −1 (mod 4Q), = UNIT_ORBIT_ES Prop 6.1. "Other transformations are not excluded" is correctly stated.
* **X5 — SOUND as Assessment.** disc[r, 4Q, (n + 4Q²)/r] = 16Q² − 4(n + 4Q²) = −4n ✓; (n/r) = −1 with r ≡ 3 (4)
  ⟺ (−n/r) = +1 (Heegner) ✓; the T1 remark (no prime ≡ 3 (4) splits in ℚ(i)) ✓. The ES cube-point form
  [h, 4cd, de] of discriminant −4dp encodes he − 4c²d = p; I did not re-derive its correspondence with (J)25's cube
  points (read only). "A ≡ −1 (mod B)" is not an SL₂(ℤ)-class invariant at all, so "seen only through its genus
  shadow" is if anything generous; "Dead" is fine as Assessment.
* **X6 — SOUND after the author's self-review repair** (scope reduced to the five SQ₅ slices). "Not pursued".
* **X9 — SOUND (scoped).** By the X1 computation the ES version of Q = 3^m needs 3^m | (r + 1)/4, a modulus growing
  with m: B2 as claimed, within the orbit family.
* **X10 — SOUND.** |Box(k)| ≤ #{(c, j) : cj | k} = τ₃(k) = k^{o(1)} ✓.
* **X3 wording — MINOR m8.** "its lesson is negative for ES (T1 is never the difficulty; orbit size is)" is an
  unqualified universal in a §1 headline; §3's own Reading has the scoped version ("in every mechanism of this shape
  … my reading (Assessment)"). For ES the barrier ledger (B1, B5) says T1 is exactly what kills congruence-covering
  proofs, so "never" contradicts established ledger content unless scoped to shot/character mechanisms. Repair:
  "(in shot mechanisms of this shape the T1 step is one character value; the difficulty is orbit size — Assessment)".

## Labels and the recalibration

* Labels are accurate: Lemma 2.1, Prop 2.2, Prop 3.1, Lemma 3.2, Thm 3.3 PROVED; Cor 3.4 PROVED rel. Hecke (+ TWISTED_T1
  Thm 3.2, itself reviewed); Thm 3.5 PROVED rel. Chebotarev; GRH remark Assessment; ω² value EVIDENCE (upgradeable to
  "constant on the class: PROVED" by the conductor argument, value still EVIDENCE); seed answers Assessment. No label
  claims a case of ES; the "ES is not solved" line is present.
* **Recalibration "a T1-bearing variant being provable is, by itself, weak evidence about ES" — FAIR.** Prop 2.2 and
  Thm 3.5 genuinely show that once the mute set is unrestricted the T1-bearing variant falls to one Dirichlet/Hecke
  prime, so the existence of *some* provable T1-bearing variant carries little information; and (J)23's content is
  correctly located in the fixed-S (Artin/sieve) restriction. Two caveats the author should keep visible: (a) this does
  not devalue (J)23 Thm 2.4 as a theorem (fixed S is strictly harder, and is the regime nearest ES); (b) "the T1 is not
  the difficulty" is true *inside shot/character mechanisms*, not for ES in general (m8) — for ES, B1/B5 say T1 is
  precisely what any covering-type proof must evade, and (J)25 says ES has no infinite orbit for the character
  mechanism to act on. The §3 Reading states it with the right scope; §1 X3 and the report's SHARP 1 phrase
  ("all of (J)23's analytic content … is the restriction to a FIXED finite S") are fine.

## Numbered defects

No FATAL, no MAJOR.

* **m1 (MINOR, §2 Prop 2.2(b) last sentence).** The proof gives Q < r(p) (odd one of s, r − s), and Q < p already
  ensures gcd(Q, p) = 1; "Q < 2r(p) for p > 2r(p)" is true but slack. Repair: "one can take 0 < Q < r(p) (whenever
  r(p) < p)".
* **m2 (MINOR, §2 Reading 2; report SHARP 1).** "r(p) ≤ log p/2 … false for a positive proportion of p" is false:
  the exceptional set has density 0 (≈ 2^{−π(y;4,3)} with y = (log p)/2 → ∞; numerics 0.50 at 10⁶, 0.25 at 10⁸).
  Also the "would need" is specific to the Q < 2r construction; seed (ii) with arbitrary Q ∈ ⟨primes ≤ log p⟩ is OPEN,
  not answered negatively. Repair text in §2 above.
* **m3 (MINOR, §3 Definition remark / X11).** The weak normalisation (N_q) is *necessary* for the shot family at
  order 3 (68/3044 mute places in the recipe solutions have v_q(z) < 0, 3 ∤ v_q(z), q | x), unlike order 2 where the
  strong one holds automatically. Add one sentence; "slightly weaker" undersells it.
* **m4 (MINOR, Thm 3.3 / Thm 3.5 last sentence).** Thm 3.3 is stated for π^{3k}; Thm 3.5 invokes it for arbitrary
  cubes. State the (immediate) composite-cube version.
* **m5 (MINOR, §3 EVIDENCE (4)).** "52 of 768" depends on the choice of 2-primary associate ±π; state the convention
  or report 117/1536 (90 of 768 ideals for some associate).
* **m6 (MINOR, DISCOVERIES (J)23 as fixed).** KARY2 condition belongs to (D)19 only.
* **m7 (MINOR, §4).** (J)15 itself uses "W(n)" for the sign-free property; mention when proposing the rename.
* **m8 (MINOR, §1 X3).** "T1 is never the difficulty" unscoped; scope to shot mechanisms (Assessment).
* **Upgrade u1 (optional, §3 Cor 3.4 remark / Thm 3.5 proof).** K(∛18) ⊂ L (conductor of K(∛18)/K divides
  2λ⁴ = (18)); so (18/·)₃ is a ray class character mod 18, constant on the class of g₀; the "not checked" hedge and the
  L(∛18) device can be dropped (keeping L(∛18) is also harmless). Also note the T1₃ control (3) is forced a priori.
