# Z57_SYNTH — the minimal missing statement for ES at large primes, three new mechanisms, the effectivity pincer

Status: z57 lane SYNTH (brief `z52bbriefs/z57_lanes.md` §SYNTH, common rules `z52bbriefs/z53_depth.md`). Internal, internally
reviewed only. **ES is OPEN; nothing here proves or disproves ES, (★) or any family positivity at any infinite set of
primes.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z57_synth_*`,
data `data/z57/synth/`.

*CHECKPOINT 1 (skeleton; sections marked [TODO] are filled in later commits).*

## 0. Summary [TODO]

## 1. The minimal missing statement

Notation as `Z56_FAMDESIGN.md` §1 and FRONTIER §2.1: R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n} (both orders),
M_gen(n) its genus (order ≤ 2) part, X(n) = R(n) − M_gen(n) the order-≥3 remainder; 𝔊* = {(o, e) : max(o,e)⁴ > min(o,e)·p}.
L := log p. The six Mordell classes: 𝔐 := {1, 121, 169, 289, 361, 529} (mod 840).

**(MS) Minimal missing statement.** *For every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 there is an integer d ≡ 3 (mod 4)
such that the least positive residue r of −p modulo d is a divisor of (d + 1)/4.*

Equivalent forms (PROVED; FAMTRY Lemma 1.4 and FRONTIER §2.1; the bijection is (u, B, C) ↦ d = 4uC − 1, r = u):
(MS) ⟺ R(p) ≥ 1 ⟺ ∃C ≥ 1 ∃ d | 4Cp + 1 with d ≡ −1 (mod 4C) ⟺ ∃u ≥ 1: p + u has a divisor ≡ −1 (mod 4u)
⟺ X(p) > −M_gen(p).

**Why (MS) implies ES (PROVED relative to the literature).** (i) ES for n reduces to primes p ≡ 1 (mod 4) and, by
Mordell's identities, to p mod 840 ∈ 𝔐 (classical; for p ≡ 1 (8) re-proved as UPPER2 Prop 3.1, Lean `HC.lean` (d)).
(ii) R(p) ≥ 1 gives the Type II solution 4/p = 1/(uBC) + 1/(pBC) + 1/(puC) (Lean `HC.lean` (a)). (iii) ES holds for all
n ≤ 10¹⁷ (Salez, arXiv:1406.6307, abstract checked 2026-11-05: "checking up to N = 10¹⁷"); 10¹⁸ is reported by
Mihnea–Bogdan, arXiv:2509.00128 (abstract checked; unrefereed). With only the campaign's own certified range, the same
statement with threshold 10¹⁰ suffices (R(p) = 0 has no prime solution in (8 813 281, 10¹⁰], CERTIFIED, FRONTIER §2.1).

[TODO: §1.2 minimality ladder; §1.3 what proved results buy (tautology); §1.4 effectivity pincer; §1.5 data checks.]

## 2. Data checks (first falsifiers)

### 2.1 Numerator 8: the C-even half of (★) is the c = 1 line of 8/p (PROVED identity) and keeps failing (CERTIFIED)

*Identity (PROVED).* (u, B, C) with C = 2C′ even solves (★) iff 8uBC′ − u − B = p, i.e. iff
8/p = 1/(uBC′) + 1/(pBC′) + 1/(puC′). So R(p) = R_odd(p) + R₈(p), R₈ := #{(★) solutions with C even} = the c = 1 Type II
count for numerator 8, and R_odd := #{C odd}.

*Scan (CERTIFIED, one engine; `scripts/z57_synth_tri.c`, sieve-style enumeration of all triples with 4uBC − u − B ≤ N,
validated by reproducing the 14 known (★)-zeros exactly).* Among the 2 880 504 primes p ≡ 1 (4), p ≤ 10⁸:
R = 0 at exactly the 14 known primes (last 8 813 281); **R₈ = 0 at 1 270 primes** (including the 14 R-zeros), per decade 1, 3, 12, 48, 115, 235, 384,
**472 in [10⁷, 10⁸)** (last below 10⁸: 99 671 381); R_odd = 0 at 423 primes (including the 14), 156 of them in [10⁷, 10⁸) (last 99 111 841).
Primes p ≡ 3 (4) ≤ 10⁸ with R₈ = 0: 1 161 (131 among them; 8/131 has no solution at all).
`data/z57/synth/tri_1e8.{txt,log}`.

*Model (Assessment; same binned Poisson-ML fit as `Z56_FAMDESIGN` §4.4, `scripts/z57_synth_zerofit8.py`,
`zerofit8.txt`).* P(R₈ = 0) ≈ exp(−0.627 − 0.0260 L²) on [10⁵, 10⁸] (1 091 zeros): expected R₈-zeros beyond 10¹⁰ ≈ 331,
beyond 10¹² ≈ 41, beyond 10¹⁷ ≈ 0.003; crossover x* ≈ 10^{14.4}. Same fit for R: x* ≈ 10^{7.3}.

*Reading.* "R₈(p) ≥ 1 for all p > 10¹⁰" is, in this model, false (hundreds of exceptions expected in (10¹⁰, 10¹⁵)), while
(MS) with threshold 10¹⁰ is consistent with all data. So the numerator-8 screen (FRONTIER §4 item 2) becomes concrete:
**an argument for (MS) at threshold 10¹⁰ must contain a step that is false for the C-even sub-line** (equivalently for the
numerator-8 c = 1 line), or carry a threshold ≳ 10^{14.4} for it. The two halves are not complementary: corr(R_odd, R₈)
= +0.25 (10⁶–10⁷) and +0.29 (10⁷–10⁸) (EVIDENCE, `tri_1e8.log`), and the mean of R/L² at R₈-zeros above 10⁷ is 0.082
against the unconditional R_odd mean 0.088 — mild positive coupling, no compensation.

### 2.2 Least non-residues at the zeros (CERTIFIED; `scripts/z57_synth_lnr.py`, `lnr_zeros.txt`)

n_p := least prime q with (q/p) = −1. At the 14 (★)-zeros n_p ∈ {5, 7, 11, 13, 17, 19, 23} (e.g. 329 617: n_p = 5;
409, 23 929, 1 134 241: n_p = 7; 5 212 561: n_p = 11). At the 38 𝔊*-zeros n_p ∈ {2, 5, 7, 11, 13, 17, 19, 23, 29}
(37, 157, 1 621, … have n_p = 2; 564 661 441: n_p = 13). Six of the fourteen (★)-zeros are outside the Mordell classes.
Consequence in §3.A.

### 2.3 The uniform-constant form [TODO: M_gen at the 334 primes p ∈ (10⁷, 10⁸] with R(p) ≤ 8]

## 3. Three mechanisms not tried in z53–z56 [TODO]

* **A. Covering rigidity + explicit least non-residue** (inverse B1; T1-native; effective via Bach/Burgess). Pushed.
* **B. Fixed-p level sieve (free level of distribution in C) + anatomy forcing.**
* **C. Effective explicit-constant closure (the effectivity pincer).**

## 4. Verdict, screens, proposed FRONTIER text, bottom line [TODO]

## 5. Review log [TODO]
