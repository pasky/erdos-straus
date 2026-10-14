# SYNTHESIS_SPARKS4 — "ES must imitate the archimedean place": the three-bit law, the signed n-adic relaxation SQ_±, and where positivity actually acts (task O218, synthesis IV)

**ES is not solved here, and no infinite case of it is claimed.** Labels as in DISCOVERIES.md. Memos:
`BRAINSTORM/s4_*.md` (8); scripts `scripts/s4_*`. Notation: words w = (t, u, v) ∈ ℤ³ with tuv − u − v = n (X_n),
A = tu − 1, B = tv − 1 (AB = tn + 1, A ≡ B ≡ −1 mod t), χ(w) = (−A/n), path form Q_w (det n), certificate = the
2-adic five-slice condition (4 | A, B, t, u or v). "Positive" = t, u, v > 0; "signed" = t u v ≠ 0, not positive.
(R219 repair, D1: (R_n) and SQ_± below quantify over **all** points with t u v ≠ 0, positive ones included — this is what
`s4_sqpm.c` computes and what makes ES-five(n) ⇒ (R_n) trivial; "strictly signed" = not positive is reported separately.)

## 0. Iteration log (construction → kill → which hypothesis → modification)
(I1) Goal (1): make "positivity-blind" precise. Construction: put the ∞-bit on the variety itself. → L1 (positive ⟺
Q_w definite) and L2 (the positive locus D is one connected component of X_n(ℝ)); inv_∞ of the CHI_FLIP class is ½
exactly on D. (§1.)
(I2) Classify tools by which bit they control. Symmetric geometry of numbers, pigeonhole, wide classes, strong
approximation, θ-positivity, IVT, SOS: all act on a layer identical at odd squares (memos s4_minkowski_sail,
s4_real_analytic_tools). Killed by T1, as expected.
(I3) Steering: the barrier hypothesis is "the argument also applies to signed words". Modification: drop positivity
but keep the *n-adic* bit instead of the 2-adic one. → the signed n-adic relaxation (R_n), which keeps T1
automatically. Is it a theorem? (§2.) Result: finite (|t| ≤ n + 3), no forcing (PROVED), but empirically far easier
than ES and *without the 105 exception*: CONJECTURE SQ_±, EVIDENCE to 10⁷.
(I4) Steering again: (R_n) has a fixed-modulus genus structure on |t| ≤ 6 (PROVED slot table, §2.3) — but no forcing
(§2.2) and no finite t-set suffices (CONDITIONAL on Dickson — R219 repair D3, §2.4). So "positivity is the anchor, not the
bottleneck": the lottery survives the removal of positivity. (§2.5.)
(I5) Positivity-using reduction theory (Selling/Voronoi): certificates are lattices of the χ = −1 genus on a Voronoi
wall with two unit conorms (s4_selling_voronoi_wall). Locates, does not force (B2).
(I6) Cross-combinations (O218 (3)): Kudla × ∞ (s4_kudla_green_infinity), full-T1 × χ-fibre × ∞ (s4_two_and_infinity),
Maslov × length 3 (s4_maslov_inertia), c_∞-imitation × mute place (s4_mute_infinity). All exact dictionaries; none
forces.

## 1. The meta-statement (goal 1)
**L1 (PROVED).** For n > 0 and an integral point with t u v ≠ 0: Q_w positive definite ⟺ w positive; else indefinite.
(Leading minors v, tv − 1, n.)
**L2 (PROVED).** D = {v > 0, tv > 1} ∩ X_n(ℝ) is a connected component of X_n(ℝ), ≅ ℝ²_{>0}, and equals the positive part.
**Three-bit law (PROVED for all words, signed included — R219 repair D5; previously CERTIFIED n ≤ 1001).** certificate ⟺
χ·s_∞ = −1, s_∞ = +1 iff w positive. *Proof (R219).* CHI_FLIP Thm 1.1's local computation ε_ℓ = (−A/ℓ)^{v_ℓ(n)} (ℓ odd)
uses no positivity, so Hilbert reciprocity gives χ = ε₂ε_∞ for every word (ε = isotropy signs); ε_∞ = −1 ⟺ positive
(L1); ε₂ is a function of w mod 8 (CHI_FLIP Cor 1.2) and the certificate one of w mod 4; on positive words certificate ⟺
ε₂ = +1 (MODEL_SPECIFIC 3.1(a)), and every odd-n cell mod 8 contains positive words, so certificate ⟺ ε₂ = +1 for all
words; for signed words χ = ε₂. ∎ (From-scratch check: `scripts/review_r219_threebit.py 1001`, 77 658 words, 0 violations.)
Equivalently ε_∞ε₂ε_n = 1 with ε_∞ ↔ positivity (L1), ε₂ ↔ certificate, ε_n ↔ χ; here ε_∞ = −(−1)^{ind_−(Q_w)/2} = −s_∞
(R219 repair of sign convention: (−1)^{ind_−/2} is TRANSPORT's Hilbert-product factor, s4_maslov_inertia Lemma I),
all-or-nothing on the five slices.
**Meta-statement (PROVED as stated; the reading is Assessment).** ES-five(n) ⟺ X_n(ℤ) ∩ (D × Ω₂) ≠ ∅. Hence:
 (a) (Assessment; R219 repair D6 of the quantifier) any argument whose conclusion is "X_n(ℤ) meets R × Ω₂" with
     R ⊇ X_n(ℝ) ∖ D (or which is insensitive to swapping D for X_n(ℝ) ∖ D) proves a statement that is *true at every odd
     square* (signed certificates exist there: PROVED, w = (−1, 1, −(n + 1)/2) has B = (n − 1)/2 ≡ 0 (mod 4) for
     n ≡ 1 (8); FRIEZE §3), so it cannot prove ES — this is the precise sense of "positivity-blind";
 (b) blind tool classes (each argued in the memos): centrally symmetric geometry of numbers (Minkowski, Thue, Siegel's
     lemma: central symmetry = the c_∞ involution A ↦ −A), pigeonhole differences, wide ray classes / even
     characters, strong approximation and real topology on X_n(ℝ), finite-ring friezes, SOS, θ-positivity (which
     re-proves the product formula, i.e. supplies T1 and nothing more);
 (c) but positivity is *not the bottleneck*: §2.

## 2. Deep dive: the signed n-adic relaxation (R_n) and CONJECTURE SQ_±

### 2.1 Definition and the T1 part
(R_n): ∃ w ∈ X_n(ℤ), t u v ≠ 0 (positive words allowed), gcd(A, n) = 1, χ(w) = −1. (gcd(A, n) = 1 is automatic: AB = tn + 1.)
**Prop 2.1 (PROVED).** (a) At odd squares (R_n) fails: Jacobi symbols mod m² are +1. (b) The search is finite:
A, B ≠ −1 and A ≡ B ≡ −1 (mod t) give |A|, |B| ≥ |t| − 1, so |t| ≤ n + 3. (c) (R_n) holds for every odd n ≢ 1 (mod 8)
(n not a square): n ≡ 3 (4): w = (−1, −2, n − 2) (A = 1, χ = (−1/n) = −1); n ≡ 5 (8): t = −1, A = −2, B = (n − 1)/2,
w = (−1, 1, −(n+1)/2) (χ = (2/n) = −1). (Check: (−1)(1)(−(n+1)/2) − 1 + (n+1)/2 = n.)
(Positive ES-five is equally easy off n ≡ 1 (8); the content is n ≡ 1 (8).)

### 2.2 No forcing (PROVED)
For every t: χ(A)χ(B) = (AB/n) = ((tn + 1)/n) = 1. For n ≡ 1 (4) and an odd prime q | tn + 1, q ∤ n (R219 D4: the prime
2 contributes (2/n)^{v₂(tn+1)}, trivial for n ≡ 1 (8)):
χ(±q) = (q/n) = (n/q) = (−t/q). So for each t the sign is a genus character ψ_t(q) = (−t/q) of the prime factors of
|tn + 1|, with ∏ψ_t over the full factorisation trivial: the sign must come from a proper sub-product (B2/B4 shape).

### 2.3 The unit slots |t| ∈ {1, 2, 3, 4, 6} at n ≡ 1 (8) (PROVED; CERTIFIED on all 4 900 non-squares n ≡ 1 (8) ≤ 4·10⁴,
0 mismatches, `scripts/s4_slots.py`)
Here (ℤ/t)* = {±1}, so the sign of A can always be chosen to meet A ≡ −1 (mod t), and the slot holds iff |tn + 1| has a
prime factor q in the class below:
| t | number | q must satisfy | | t | number | q must satisfy |
|---|---|---|---|---|---|---|
| 1 | n + 1 | q ≡ 3 (4) | | −1 | n − 1 | never |
| 2 | 2n + 1 | q ≡ 5, 7 (8) | | −2 | 2n − 1 | q ≡ 3, 5 (8) |
| 3 | 3n + 1 | q ≡ 2 (3), q odd | | −3 | 3n − 1 | q ≡ 5, 7 (12) |
| 4 | 4n + 1 | q ≡ 3 (4) | | −4 | 4n − 1 | never |
| 6 | 6n + 1 | (−6/q) = −1 | | −6 | 6n − 1 | (6/q) = −1 |
The positive (ES-five) slots are the t > 0 half of this table, with positivity costing nothing at t = 1, 2, 3, 4 (R219
repair D2: at t = 6 the positive slot needs a divisor of 6n + 1 ≡ 17 or 23 (mod 24); it differs from the signed t = 6
slot at 694 of the 4 900 n, e.g. n = 41, 6n + 1 = 13·19); the signed
problem adds the numbers sn − 1. Each number's total character is +1 (2.2), so each slot is "one prime factor in the
non-principal genus" — a lottery with failure probability ≍ (log n)^{−1/2} per slot (Landau-type heuristic).

### 2.4 No finite t-set (CONDITIONAL on Dickson's prime k-tuples conjecture; R219 repair D3: complete argument)
*(R219 repair.)* Fix T; let P = ∏ of odd primes p ≤ 2T + 1 and take n ≡ 0 (mod P), n ≡ r (mod 2^K) with r ≡ 1 (8),
K large. For p | P, tn + 1 ≡ 1 (mod p); for p > 2T + 1 the 2T linear forms (tn + 1)/2^{v₂(tn+1)} cannot cover ℤ/p; so
Dickson gives infinitely many such n with every |tn + 1| (1 ≤ |t| ≤ T) equal to 2^a·(prime q_t). For n ≡ 1 (8),
(2/n) = (−1/n) = 1 and (q_t/n) = (|tn + 1|/n) = 1, so every divisor A has (−A/n) = +1: no word (signed or positive)
with |t| ≤ T has χ = −1; n − 1 = 2^a q excludes all but finitely many squares. (Illustration:
`scripts/review_r219_dickson.py 3`: n = 7 665, 29 505, 202 545.)
*Original sketch (superseded):* Under H, infinitely many n ≡ 1 (8) make every |t|n ± 1 (|t| ≤ T) equal to (bounded power of 2 and 3) × prime, the
tuple being admissible after fixing n modulo a suitable modulus (to be checked per T). For such n each slot has only
factorisations with A or B in a bounded set, whose signs are fixed by congruences and, for n chosen in the right class,
are +1 or excluded (A or B = −1). So (R_n) needs |t| > T. EVIDENCE consistent with this: failures of |t| ≤ 6 among
odd non-squares number 15 (≤ 10⁵), 62 (≤ 10⁶), 403 (≤ 10⁷); of |t| ≤ 12: 8 (≤ 10⁷), e.g. 34 489, 97 185, 4 884 441.

### 2.5 Numerics and CONJECTURE SQ_± (EVIDENCE)
`scripts/s4_sqpm.c` (C, early exit, odd squares skipped by Prop 2.1(a)):
* (R_n) holds at **every odd non-square n ≤ 10⁷**, least |t| record 18 (n = 4 884 441), 15 (n = 97 185) below 10⁶
  (these numbers include positive words; R219 reproduced all of §2.4–2.5 with `scripts/review_r219_sqpm.c`).
* (R219 repair D1) **Strictly signed** words alone (not positive): also 0 failures ≤ 10⁷, but least |t| record
  19 @ 60 369 (≤ 10⁵), 30 @ 297 465 (≤ 10⁶), 54 @ 9 817 305 (≤ 10⁷); |t| > 6 needed at 1 277 n, |t| > 12 at 156 n (≤ 10⁷).
* Positive ES-five on the same range: fails only at 105 (SQ₅'s known exception), least-t record 231 (n = 702 585).
* Failures restricted to |t| ≤ 6: signed 403 vs positive 10 550 (≤ 10⁷); |t| ≤ 12: 8 vs 996.
**CONJECTURE SQ_±.** For odd n > 1: some point of X_n with t u v ≠ 0 has χ = −1 ⟺ n is not a square. (R219 repair D1:
"signed point" replaced; the strictly-signed version is also supported to 10⁷, see above, but is not implied by ES-five.)
It is the n-adic, positivity-free twin of SQ₅ (the 105 exception disappears: 105 has signed χ = −1 words) and, like
SQ₅, numerator-free.

### 2.6 What SQ_± teaches (Assessment)
* Removing positivity in the n-adic form keeps T1 (2.1(a)), keeps the search finite (2.1(b)), keeps the divisor
  sub-product lottery (2.2) and keeps "no finite slot set" (2.4). It only doubles the slots (sn − 1 joins sn + 1).
  (R219 caveat D1: the "403 vs 10 550" gain is ES-five's tickets *plus* signed ones; signed tickets alone need |t| up
  to 54 ≤ 10⁷ — still far below ES-five's 231, so the qualitative reading stands.)
  **So the archimedean place is ES's T1 anchor, not its bottleneck.** A tool that "uses positivity" is necessary to
  respect T1 but buys nothing on the lottery; conversely a lottery-breaker would have to work equally on SQ_±.
* Steering rule (new): **any proposed ES mechanism should first be tried on SQ_±**, which has T1, no positivity, the
  same finite box and twice the tickets. If it cannot prove SQ_±, positivity will not rescue it (valid because
  ES-five(n) ⇒ (R_n) with the inclusive definition; R219 D1). (SQ_± is not a
  harness *failure* case — it is believed true — but a strictly easier target sharing every barrier.)
* SQ_± does not imply anything for 8/n or for ES (it is weaker than ES-five); the falsification harness (8/131,
  8/241, 11/37, TES, ES_q) is untouched because SQ_± is numerator-free.

## 3. Second deep item (short): positivity-using reduction theory
s4_selling_voronoi_wall, Lemma S (PROVED): Q_w = (x₁ − x₂)² + (x₂ − x₃)² + (v − 1)x₁² + (t − 2)x₂² + (u − 1)x₃²
(t ≥ 2): path bases = obtuse superbases with a face of conorms (1, 1, 0). ES-five(p) ⟺ some lattice in the χ = −1
genus (≍ p classes) lies on a Voronoi wall (two zero conorms) with two unit conorms. Conorm multisets are invariant
(3000 random conjugates, 0 mismatches). This is the most "archimedean" form of the certificate set found here; it is
a re-parametrisation (B2) and gives no forcing.

## 4. Cross-combination table
See s4_mute_infinity: every relaxation classified by (bit dropped) × (shots finite/infinite) × (c_∞-modulus
fixed/moving) × T1 × status. Every PROVED variant has a fixed c_∞-modulus and infinitely many shots; (R_n) has
neither and is the easiest open row; ES^{[2]} has infinitely many shots but a moving modulus and is open.

## 5. Falsification harness and controls
* Odd squares: every positive claim (SQ_± evidence, slot table) respects T1 by Prop 2.1(a); the 2-adic signed
  relaxation is shown *false* as a T1 carrier (PROVED, R219 D6: (−1, 1, −(n + 1)/2) is a signed certificate at every n ≡ 1 (8); also CERTIFIED at all 24 odd squares ≤ 2501).
* 8/131, 8/241, 11/37, TES, ES_q: no claim here transfers to other numerators; s4_two_and_infinity explains why the
  archimedean bit is numerator-free (all numerator data is 2-adic).
* Primes: SQ_± checked at all odd n ≤ 10⁷ (primes included); slot table at all n ≡ 1 (8) non-squares ≤ 4·10⁴.

## 6. Verdict
Goal (1) is achieved as a precise statement (§1). Goal (2): every archimedean tool examined either acts on the
real/genus layer (identical at squares) or re-parametrises the certificate set (sail, Selling wall); none forces.
The main new finding is negative-but-steering: **positivity is the anchor of T1, not the obstacle** — the signed
n-adic twin SQ_± keeps T1 and every barrier, is empirically much easier and exception-free, and should be the first
test bed for any lottery-breaking idea. No route to ES.
