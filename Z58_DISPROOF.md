# Z58_DISPROOF — what a counterexample to (MS) would look like; a sibling-calibrated targeted search

Status: wave z58 lane DISPROOF (brief `z52bbriefs/z58_lanes.md` §DISPROOF, common rules `z52bbriefs/z53_depth.md` with
z53 → z58). Internal, internally reviewed only. **ES is OPEN; nothing here proves or disproves ES or (MS).** Labels:
PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z58_disproof_*`, data
`data/z58/disproof/`.

*(Checkpoint 1: §§0–2 skeleton, falsifier table, statements, engine validation. Results sections are filled in as runs
finish.)*

## 0. MANDATORY FALSIFIER TABLE

The "idea" of this lane is not a proof mechanism but a *counterexample generator*: structured families of primes
(residue designs, square-mimicking, near-squares) that push R(p) down, plus a calibrated zero law that converts the
measured depression into a model zero tail. The table states how the generator and the model behave on each screen.

| screen | how the counterexample generator / zero model behaves |
|---|---|
| **F1 odd squares** | Squares are the *template* the designs imitate. Lemma 2.2 (PROVED): if n is a square modulo M, no (★) solution at n has any of its three moduli 4uB, 4uC−1, 4BC−1 dividing M. At n = m² this holds for every M, so R = 0. A prime p is a square modulo every y-smooth M iff p ≡ 1 (8) and n_p > y, and it is *never* a square modulo every M (it is a non-square mod any prime ℓ with (p/ℓ) = −1). Heuristically (CRT/Chebotarev on average, not proved pointwise) the primes that are squares mod M have relative density ≈ 2^{−ω(M)}: **primality enters the model through this supply constraint.** The design rules out the solutions with a modulus dividing M (a one-way statement; the remaining solutions are *modelled* as unaffected, §4.2). The zero law is fitted on primes and is not applied to squares (it would predict R(m²) > 0, i.e. the model is wrong at squares by construction). |
| **F2 C-even sub-line** | Used as the *calibration sibling*: R₈ has CERTIFIED zeros at 10¹⁰ (12 in [10¹⁰, 1.1·10¹⁰]). The same designs are run on R₈ and R; the design boost of the R₈ zero rate (measurable) is compared with the boost predicted from the mean depression. What distinguishes the halves for the model: essentially the size of the mean (R₈ ≈ 0.075 L², R ≈ 0.15 L²) — so the model says nothing structural about C odd vs even, and a design that zeroes R₈ above 10¹⁰ is *expected*, not news. |
| **F3 composites** | Composites are not in the search domain. Profile (§3) checks whether the 285 composite zeros are "square-like" (square mod many small moduli / small square part) — they serve as a second calibration of "local square-likeness ⇒ zero". The generator never claims positivity at composites. |
| **F4 known zeros** | The engine reproduces the 14 (★)-zeros and the 𝔊*-zeros tested (§2). The zero law is fitted on the R₈-zeros (1 339) and R-zeros (10) of [≈1.16·10⁴, 2·10⁸] in cells; it is a probability model, gives no positivity statement anywhere, and is not calibrated for R_𝔊*. Profile (§3): local data of the zeros vs controls. |

## 1. Statements attacked (precise)

* **(MS)** (`Z57_SYNTH.md` §1.1): every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 has R(p) ≥ 1. Internal variant: threshold 10¹⁰.
* **(D1) Counterexample search.** Find a prime p ∈ 𝔐, 10¹⁰ < p ≤ 10¹⁴ (searched in the end up to 7.3·10¹⁵), with R(p) = 0 (or R_𝔊*(p) = 0), searching only
  in designed progressions. A find would refute (MS) at threshold 10¹⁰ (not at 10¹⁷; not ES — López/other lines must
  then be checked).
* **(D2) Model question.** Is there a structured family 𝔉 of primes (residue design, square-mimicking, near-square, …)
  whose *model* zero tail E_𝔉(> x) := Σ_{p ∈ 𝔉, p > x} P(R(p) = 0) stays ≥ 1 past x = 10¹⁷? Quantified through the
  design depression ρ_𝔉 := E[R | 𝔉] / E[R | control] at matched size and a zero law fitted on data.

## 2. Elementary structure (PROVED)

**Lemma 2.1 (pair-congruence form; PROVED).** For every n ≥ 1, R(n) = #{(u, B) ∈ ℕ² : 4uB | n + u + B} (then C := (n + u + B)/(4uB) is a
positive integer because n + u + B > 0). Each solution (u, B, C) carries three moduli
m₁ = 4uB, m₂ = 4uC − 1, m₃ = 4BC − 1, and it is equivalent to each of
n ≡ −u − B (mod m₁) [given u, B], n ≡ −u (mod m₂) [given u, C; B = (n + u)/m₂], n ≡ −B (mod m₃) [given B, C].
*Proof.* 4uBC − u − B = n ⟺ n + u + B = 4uB·C; and ⟺ n + u = B(4uC − 1); and ⟺ n + B = u(4BC − 1). Positivity of
the third variable is the size condition, automatic for n ≥ 1. ∎

**Lemma 2.2 (square-class shadow; PROVED — a one-way exclusion; the T1 mechanism made modular — essentially known, cf. `Z53_UPPER.md` C3.2,
`RESIDUE_HARDNESS.md` §3).** Let M ≥ 1 and suppose n ≡ s² (mod M) for some integer s. Then no (★) solution (u, B, C) at
n has m₁ | M, m₂ | M or m₃ | M.
*Proof.* Suppose m_i | M. The solution condition for that (pair of) variable(s) is the congruence of Lemma 2.1 modulo
m_i (the size condition is automatic). Since n ≡ s² (mod m_i), the integer N := (s + t m_i)² for t large satisfies the
same congruence, hence (★) has a solution at the square N, with the same pair of variables, contradicting R(N) = 0 (Lemma A.1(b) of
`Z57_SYNTH.md`: every hit class mod d ≡ 3 (4) is a Jacobi non-residue, so R(m²) = 0 for every m ≥ 1). ∎
*Remarks.* (i) 𝔐 is exactly the set of squares of units mod 840 (units mod 840 squared: 1 mod 8, 1 mod 3, {1,4} mod 5,
{1,2,4} mod 7 — six classes). So (MS)'s domain is the "M = 840 square design" (Mordell's identities cover the rest).
(ii) "p ≡ 1 (mod M)" (class of one) is a special square class.

**Engine (CERTIFIED validation).** `scripts/z58_disproof_eng.c`: per prime, complete levels C ≤ K (S_K), early-exit
decisions of R, R₈, R_odd, R_H3 ≥ 1 by level scans, exact full enumeration (three loops of FAMDESIGN's audited engine)
whenever any is undecided or EXACT=1; the least raw (MS) witness d_min. Validation: reproduces R = 0 at all 14 (★)-zeros,
R_𝔊* = 0 (with R = 2) at the 𝔊*-zeros 11 814 001, 20 445 289, 85 664 329, 564 661 441, and R₈ = 0 with R = 56, 52, 30,
42 at the first four R₈ zeros above 10¹⁰ (exact match with `r8_zeros_1e10.txt`). Speed: 4 ms/prime at 10¹², 12 ms at
10¹³ (decision mode); 12 ms/prime exact at 10¹⁰.

**Lemma 2.3 (line sterility on near-square families; PROVED — elementary, known in kind: `CLASS_FORCING.md` uses
p + 8 = x² + 2y²; `ES_CONNECTIONS_TODO.md` Z1190 the u = 1 line).** Let u ≥ 1, c | u, t ≥ 1, and let n = m² + c t² − u
with gcd(m, c t) = 1. Then (★) has no solution at n with first coordinate u (the "u-line" is empty), and by the u ↔ B
symmetry none with second coordinate u.
*Proof.* A solution with first coordinate u is a divisor d | n + u = m² + c t² with d ≡ −1 (mod 4u) (Lemma 2.1, m₂).
d is coprime to u (d ≡ −1 mod u), hence to c; a prime ℓ | gcd(d, t) would divide m², contradicting gcd(m, t) = 1. So
m² ≡ −c t² (mod d) with t invertible: −c is a square modulo every prime factor of d and the Jacobi symbol (−c/d) = +1.
But c | u | (d + 1)/4, so Lemma A.1(b) of `Z57_SYNTH.md` gives (−c/d) = −1. ∎
*Reading.* n = m² is the case "every u, c = u, t = 1" (T1). On a near-square family n = m² + k, the lines with
k + u = c t², c | u, are empty *for those m with gcd(m, c t) = 1* (a sufficient condition; other lines may also be
empty at a given n): a *truncated* T1. The gcd hypothesis is essential: p = 10 017 408 409 = 100 087² + 840 (13 | m) has
the u = 5 witness (u, B, C) = (5, 256 856 626, 2) although 840 + 5 = 5·13² (review).

**Proposition 2.4 (what a fixed offset can kill).** Let k ≥ 1 and K(k) := {u ≥ 1 : k + u = c t² for some c | u, t ≥ 1}.
(i) (PROVED) c | u and c | k + u force c | k, so #(K(k) ∩ [1, U]) ≤ Σ_{c | k} #{t : k < c t² ≤ k + U} ≤ τ(k)(√(U + k) + 1).
(ii) (Assessment) If line u carries mass ≍ L/u (the log-uniform density, EVIDENCE §4.4), the mass removed *by this
mechanism* is ≪ L Σ_{c | k} Σ_{t > √(k/c)} 1/(c t² − k) = O_k(L), a share O_k(1/L) of the ≍ L² total. This bounds
only the Lemma 2.3 kills for one fixed offset; it does not cover growing offsets, other polynomial families, or other
depression mechanisms. At k = 0 every c works — T1.

## 3. Profile of the zeros (CERTIFIED data, EVIDENCE readings; `scripts/z58_disproof_profile.py` → `profile.txt`)

sd(n) := least odd prime ℓ with (n/ℓ) = −1 (ℓ | n counts as "square"); □840 := n is a square mod 840.

| set | n ≡ 1 (8) | □840 | sd distribution (share) |
|---|---|---|---|
| 14 (★)-zeros | **100 %** | 64 % | 5: .14, 7: .21, 11: .07, 13: .29, 17: .07, 19: .07, 23: .14 |
| 38 𝔊*-zeros | 79 % | 53 % | 5: .29, 7: .11, 11: .18, 13: .13, 17: .16, 19–29: .13 |
| 12 R₈-zeros ≥ 10¹⁰ | 92 % | 33 % | **3: .50**, 5–29: .08 each |
| primes p ≡ 1 (4) ≤ 9·10⁶ (control) | 50 % | 6.2 % | 3: .50, 5: .25, 7: .125, … (geometric) |
| 285 composite zeros | **100 %** | **71 %** | 5: .15, 7: .13, 11: .23, 13: .19, 17: .14, 19: .08, … |
| non-square composites n ≡ 1 (4) ≤ 8·10⁶ | 50 % | 12 % | 3: .31, 5: .27, 7: .18, … |

Readings (EVIDENCE):
* Every (★)-zero is a square mod 8 and mod 3; 9/14 are squares mod 840 (≈ 10× the control rate); the class of one
  mod 840 holds 3 of them (712 321, 1 726 201, 8 813 281). The zeros are *moderately* square-mimicking: sd ∈ [5, 23],
  never extreme (no zero has sd > 23; among the 18 562 𝔐-primes ≤ 9·10⁶, 2.2 % have sd > 23 and the maximum is
  61, at 6 810 301 — `scripts/z58_disproof_npmax.c`, appended to `profile.txt`). This is
  consistent with the model of §6, whose dominant slices are n_p ≈ 11–29 (deep slices are too thin).
* 6 of the 12 R₈-zeros have (p/3) = −1 (small sample; no claim of structural absence). A possible local reading: the
  *direct* certificate d = 3 = 4·1·1 − 1 has C = 1 (odd), and so do the other small direct levels d = 4u − 1 (u = 3: 11,
  u = 5: 19, …), none of which lie on the C-even line; mod-3 effects still enter R₈ through larger moduli (e.g.
  (u, B, C) = (1, 2, 4), p = 29, d = 15). So the C-even line has a weaker small-modulus square shadow (EVIDENCE).
* Composite zeros are even more square-like (71 % □840) — and 214/285 are divisible by 3 (0 is a square mod 3; for
  ℓ | n no m₂ or m₃ is divisible by ℓ, since ℓ | m₂ | n + u forces ℓ | u, contradicting m₂ ≡ −1 mod u). Composites get
  local square-likeness "for free" through small prime factors; a prime pays a factor 2 per Legendre condition (F3).

## 4. Designs and the depression ρ (exact counts; `scripts/z58_disproof_eng.c`, `runA/`, `runB/`)

### 4.1 Exact means at 10¹⁰–10¹² (CERTIFIED counts; ratios EVIDENCE)
EXACT=1 runs (full enumeration at every prime), consecutive primes of the design from the start point, each job cut by
its timeout.

ρ := mean over the design of (R/L²)/c₀(p), c₀ = the C0 mean interpolated in log₁₀ p between 10¹⁰ (0.1467) and 10¹²
(0.1480); ρ₈ the same for R₈; "pred" = 0.877 · surv(y, p)/surv(7, p) (§4.2, Monte-Carlo, interpolated), for the
y-square-mimicking designs (`scripts/z58_disproof_rho.py` → `rho.txt`).

| design | definition | primes | log₁₀ p | ρ | ρ₈ | pred | min R | R₈-zeros |
|---|---|---|---|---|---|---|---|---|
| C0 | p ≡ 1 (24) | 114 544 | 10.00 | 1 | 1 | — | 20 | 0 |
| CM | p ≡ 121 (840) | 115 788 | 10.00–10.02 | 0.899 | 0.879 | — | 14 | 0 |
| D1a | p ≡ 1 (840) | 109 155 | 10.00–10.02 | 0.876 | 0.827 | (0.877) | 14 | 0 |
| D1b | p ≡ 1 (120 120) | 62 796 | 10.00–10.65 | 0.794 | 0.757 | 0.835 | 18 | 1 |
| D1c | p ≡ 1 (4·lcm(1..16)) | 20 137 | 10.00–11.47 | 0.788 | 0.741 | 0.821 | 20 | 1 |
| D2 | p ≡ 1 (840), n_p > 31 | 58 524 | 10.00–10.65 | 0.748 | 0.721 | 0.745 | **10** | 1 |
| SM61 | p ≡ 1 (840), n_p > 61 | 9 877 | 10.00–12.00 | 0.725 | 0.702 | 0.703 | 18 | 0 |
| SM97 | p ≡ 1 (840), n_p > 97 | 730 | 11.22–13.18 | 0.730 | 0.709 | 0.692 | 42 | 0 |
| NSQnear | p = m² + 840j, 1 ≤ j ≤ 3 | 37 826 | 10.00–11.24 | 0.807 | 0.792 | — | 12 | 0 |
| NSQfar | p = m² + 840j, 10⁵ < j ≤ 10⁵ + 3 | 37 802 | 10.00–11.27 | 0.907 | 0.892 | — | 18 | 0 |
| C0_12 | p ≡ 1 (24) | 6 306 | 12.00 | 1 | 1 | — | 36 | 0 |
| SM31_12 | p ≡ 1 (840), n_p > 31 | 6 683 | 12.00 | 0.786 | 0.764 | 0.785 | 36 | 0 |

(D1b's 23 296 553 281 also lies in D1c; the R₈-zero count over distinct primes is 2.) No R- or 𝔊*-zero in any design
(≈ 5.5·10⁵ primes, all exact). The class of one beyond 840 (D1b, D1c) depresses ≈ 5 % more than square-mimicking at the
same primes predicts: being ≡ 1, not merely a square, matters at the partial-gcd moduli.

New R₈-zeros (CERTIFIED by the exact enumeration; both ≡ 1 mod 840): **20 840 951 041** (R = 24) and
**23 296 553 281** (R = 36) — above the z57 interval [10¹⁰, 1.1·10¹⁰]; expected (F2), not news. No R- or 𝔊*-zero.

### 4.2 The surviving-mass law (EVIDENCE; `scripts/z58_disproof_smooth.c`, `scripts/z58_disproof_survmc.py`)
By Lemma 2.2 a y-square-mimicking prime (p ≡ 1 (8), (ℓ/p) = 1 for odd ℓ ≤ y; equivalently p is a square modulo every
y-smooth integer, by Hensel and CRT) has no solution with a y-smooth modulus (PROVED, one-way). *Model* (heuristic,
tested below): the other solutions are unaffected on average, so ρ(y) ≈ surv(y, p) := share of the solutions of a
*generic* prime with no y-smooth modulus.
* Exact share at 300 C0 primes ≈ 10¹⁰ (relative to the 3-smooth baseline that p ≡ 1 (24) already kills): y = 7: 0.936,
  13: 0.882, 31: 0.767, 61: 0.664, 97: 0.592, 199: 0.433, 499: 0.279.
* Monte-Carlo of the log-uniform solution density (`survmc_quick.txt`): 0.945, 0.896, 0.792, 0.688, 0.608, 0.458, 0.294
  at 10¹⁰ (agrees within ≈ 3 %), and at 10¹⁷: 0.982, 0.966, 0.932, 0.898, 0.870, 0.812, 0.730.
* Check against designs (table §4.1): D2 0.745 predicted / 0.748 measured; SM61 0.703 / 0.725; SM97 0.692 / 0.730
  (5 % relative; 730 primes); SM31 at 10¹² 0.785 / 0.786. The y = 31 design weakens from 0.748 at 10¹⁰ to 0.786 at 10¹², as predicted; SM97 (at
  10^{11.2}–10^{13.2}) is no deeper than SM61 — the fading with p cancels the extra square conditions.
* **The square-class kill fades with p at fixed y** (smooth moduli become rare among moduli of size p^{Θ(1)}), and the
  supply of y-square-mimicking primes is heuristically 2^{−π(y)+1} (equidistribution of Legendre symbols on average), so
  y can grow only like π(y) ≲ log₂(#primes in the range) ≈ 1.44 log x (Assessment).

### 4.3 Near-squares: a line-kill effect, not a real-place effect (EVIDENCE)
NSQnear by offset k = p − m² (final files): k = 840: mean R/L² = 0.1151 (14 835 primes), k = 1680: 0.1067 (10 183),
k = 2520: 0.1325 (12 808); NSQfar (same algebraic shape, k ≈ 8.4·10⁷): 0.1336 (37 802), all in [10¹⁰, 1.8·10¹¹]. So at
these offsets *proximity to a square in ℝ shows no effect of its own* (k = 2520 is within 1 % of the far control),
while k = 840, 1680 are depressed by 13.8 % and 20.1 %. Lemma 2.3 accounts for this: 840 + u ∈ c□ (c | u) for
u = 1 (29²), 5, 7, 24, 27, 35; 1680 + u for u = 1 (41²), 2 (2·29²), 10, 14, 21, 35; 2520 + u for no u ≤ 40. A rough
prediction — summed line shares of §4.4 for u ≤ 12, an *imputed* 0.01 per line for 12 < u ≤ 40, ignoring overlaps
between lines and the gcd(m, ct) = 1 exceptions (≈ 21 % of these m are divisible by 11, 13, 29 or 41, which can revive
single lines) — gives 0.141 (k = 840) and 0.179 (k = 1680) (`kbest.txt`), vs measured 0.138 and 0.201. The PRIMET1
"square-offset near-squares look harder" signal is consistent with this line-kill mechanism (Assessment).

### 4.4 Line masses (EVIDENCE; `scripts/z58_disproof_lines.py` → `lines_D1a.txt`, 1 500 D1a primes at 10¹⁰)
Share of R in the lines u and B = u: u = 1: 0.065, 2: 0.077, 3: 0.034, 4: 0.034, 5: 0.038, 6: 0.033, 7: 0.008, 8: 0.018,
9: 0.021, 10: 0.008, 11: 0.017, 12: 0.009 (cumulative 0.36 for u ≤ 12). P(N_u = 0) ≈ 0.47–0.80 — each line is dead at
about half of the class-of-one primes. Killing a line therefore costs only a factor ≈ 2 in supply but removes only
3–8 % of the mass at 10¹⁰, and the share of a fixed line decays like 1/L.

## 5. Avoidance depth and the targeted search above 10¹⁰

### 5.1 Conditional zero rate vs avoidance depth D (CERTIFIED counts; `scripts/z58_disproof_avoid.c` → `avoid_2e7.txt`)
A_D := {p : p mod d ∉ H_d for all d ≡ 3 (4), d ≤ D} = {d_min(p) > D} (Lemma A.1 of `Z57_SYNTH.md`). All primes
p ≡ 1 (4) in [10³, 2·10⁷] (635 090; 39 391 in 𝔐; the raw d-loop is run to (4p+1)/3, so d_min = ∞ ⟺ R = 0):

| D | #A_D (all) | #A_D (𝔐) | share in 𝔐 | zeros in A_D (𝔐) | conditional zero rate in 𝔐 |
|---|---|---|---|---|---|
| 7 | 211 505 | 39 391 | 1 | 9 | 2.3·10⁻⁴ |
| 31 | 79 748 | 19 721 | 0.50 | 9 | 4.6·10⁻⁴ |
| 127 | 23 234 | 6 064 | 0.154 | 9 | 1.5·10⁻³ |
| 511 | 5 212 | 1 485 | 0.038 | 9 | 6.1·10⁻³ |
| 2 047 | 864 | 281 | 7.1·10⁻³ | 9 | 0.032 |
| 8 191 | 130 | 49 | 1.2·10⁻³ | 9 | 0.18 |
| 32 767 | 24 | 14 | 3.6·10⁻⁴ | 9 | 0.64 |
| 131 071 | 13 | 9 | 2.3·10⁻⁴ | 9 | 1 |

* In 𝔐, P(A_D) decays roughly like D^{−1.2} over 31 ≤ D ≤ 8 191 (EVIDENCE); the conditional zero rate is
  P(R = 0)/P(A_D) — enrichment by exactly 1/P(A_D) (all zeros lie in every A_D).
* **CRT avoidance buys only a polylog.** A residue design that *forces* A_D (Prop A.3 of `Z57_SYNTH.md`) needs a modulus
  L_D = lcm{d ≡ 3 (4), d ≤ D}; L_D contains every prime q ≡ 3 (4) up to D and, through d = 3q, every prime q ≡ 1 (4) up
  to D/3, so log L_D ∼ ϑ(D; 4, 3) + ϑ(D/3; 4, 1) ∼ 2D/3 (review fix; was D/2), and D ≲ 1.5 log p ≈ 48 at 10¹⁴. This is
  the cost of the *standard CRT encoding*, not a proved lower bound for every avoiding progression. In 𝔐,
  P(A_31) ≈ 0.50 and P(A_63) ≈ 0.32 already. The enrichment over plain 𝔐 is ≈ 3, i.e. (log p)^{O(1)}, against a zero probability
  e^{−0.4μ}, μ ≍ L² (§6) — "only a polylog" is an Assessment under that model. Selecting on *observed* avoidance
  (d_min > D by sieving) is conditioning, not design: it is a cheap search filter but cannot change the set of zeros.

### 5.2 Decision-mode targeted search at 10¹²–7·10¹⁵ (CERTIFIED decisions; `scripts/z58_disproof_runC.sh`, `runC/`)
Engine in decision mode: R ≥ 1, R₈ ≥ 1, R_odd ≥ 1 and R_H3 ≥ 1 (hence R_𝔊* ≥ 1, H3 ⊂ 𝔊*) decided by complete level
scans with early exit; exact full enumeration whenever any of the four is undecided. Consecutive design primes from the
start point, each job cut by its 1 750 s timeout (partial runs recorded as such). All primes are in 𝔐 by construction.

| job | design | primes | p range | mean S₁₆ | max d_min | full enumerations | zeros R / R₈ / R_odd / H3 |
|---|---|---|---|---|---|---|---|
| SM61_e12 | p ≡ 1 (840), n_p > 61 | 104 918 | 1.0·10¹²–1.1·10¹³ | 18.30 | 459 647 | 7 (R = 32…82) | 0/0/0/0 |
| SM47_e13 | p ≡ 1 (840), n_p > 47 | 113 533 | 1.0·10¹³–1.1·10¹³ | 19.45 | 536 639 | 0 | 0/0/0/0 |
| SM37_e14 | p ≡ 1 (840), n_p > 37 | 41 183 | 1.0·10¹⁴–1.0007·10¹⁴ | 22.41 | 137 939 | 0 | 0/0/0/0 |
| K1680_z31_e12 | p = m² + 1680, n_p > 31 | 9 835 | 1.0·10¹²–7.3·10¹⁵ | 20.27 | 523 815 | 0 | 0/0/0/0 |
| K1680_z23_e13 | p = m² + 1680, n_p > 23 | 19 173 | 1.0·10¹³–1.7·10¹⁵ | 19.80 | 523 815 | 0 | 0/0/0/0 |
| K840_z13_e14 | p = m² + 840, n_p > 13 | 34 864 | 1.0·10¹⁴–2.1·10¹⁴ | 21.41 | 622 775 | 0 | 0/0/0/0 |

305 386 distinct primes (the two K1680 jobs overlap above 10¹³). S₁₆ = # solutions with C ≤ 16 (exact): C0 means are
20.53 (10¹⁰) and 24.85 (10¹²); the designs (at equal or larger p, and S₁₆ grows with p) have 18.3–22.4. **No R-, 𝔊*-,
H3-, R₈- or R_odd-zero.** (The `divides` test is exact for n < 2⁵³ ≈ 9.0·10¹⁵; the largest p searched is 7.3·10¹⁵.)
Model expectation for the whole search: ≪ 10⁻⁶ R-zeros (§6.3 per-prime rates at these μ), ≲ 10⁻² R₈-zeros.

## 6. Zero model and the tail (Assessment unless marked)

### 6.1 A zero law in the local mean (EVIDENCE; `scripts/z58_disproof_cells.c` → `cells_2e8.txt`, `scripts/z58_disproof_zerolaw.py` → `zerolaw.txt`)
All primes p ≡ 1 (4) up to 2·10⁸ (exact R and R₈ by the triple sieve, which reproduces the 12 (★)-zeros in [10³, 2·10⁸]
and gives 1 388 R₈-zeros there); cells = p mod 840 × Legendre signs at 11, 13, 17, 19, 23 × half-octave; the fit uses
the half-octave bins with lower edge ≥ 10⁴ (effective cutoff 2^{13.5} ≈ 11 585; 5.54·10⁶ primes), smoothed cell mean
μ = κ(class, signs) · t(bin) · L². Binomial ML fit P(count = 0 | μ) = exp(−a μ^β):
* R₈: a = 0.398, β = 1.014 (1 339 zeros); calibrated across μ ∈ [4, 30] (observed / predicted per μ-bin: 11/11.7,
  83/75.6, 106/121.5, 145/152, 260/261, 469/456, 265/261). Profile likelihood: β fixed at 0.7 costs Δ(−log lik) = 223,
  β = 0.5 costs 617 — slowly decaying laws are strongly disfavoured *on the R₈ sibling* (within this parametric family
  and cell model).
* R alone: a = 0.403, β = 0.972 (10 zeros) — consistent with the same law. The R₈ law predicts 4.1 R-zeros for 10
  observed. (A pooled R + R₈ fit is a composite likelihood — R = 0 implies R₈ = 0 — and is reported only as a point fit.)
* **Not universal across classes** (`scripts/z58_disproof_lawclass.py`; decade split approximate, half-octave bins
  assigned by lower edge). Observed/predicted R₈-zeros: class of one mod 840 95/61, other Mordell classes 264/181,
  non-Mordell 980/1089; for R: 3/0.23, 4/0.79, 3/3.0. The excess sits in the square classes, *within* cells that already
  fix the Legendre signs up to 23.

### 6.2 A heterogeneity hypothesis for the excess (Assessment; partially calibrated)
Hypothesis: the excess comes from square-mimicking beyond the cell resolution. Model (`scripts/z58_disproof_tail.py`):
the class of one mod 840 split into slices n_p = ℓ (share 2^{−k} for the k-th prime ℓ ≥ 11 — heuristic independence of
Legendre symbols); prefix means f_k := mean over {n_p ≥ ℓ_k} = μ₁(x) · surv(ℓ_k⁻, x)/surv(7, x) (§4.2), exact-slice
means 2f_k − f_{k+1} (law of total expectation; review fix — the first version used f_k for the exact slice);
μ₁ = measured class-of-one mean (0.1146 L² at 10^{6.5}, 0.1206 L² at 10^{7.5}, 0.1286 L² at 10¹⁰), linear in L below
10¹⁰ and *frozen* at 0.1286 above (a scenario, not a proved bound); §6.1 R₈ law per slice. Predicted class-of-one
(★)-zeros: [10⁴, 10⁵): 0.86, [10⁵, 10⁶): 0.63, [10⁶, 10⁷): 0.22, total ≥ 10⁴: 1.75 — observed 0, 1, 2 (total 3;
Poisson P(≥ 3 | 1.75) ≈ 0.26). This improves on the cell law (0.23 predicted for these 3) but is fitted to the same
zeros the hypothesis was built to explain; it is **not** an independent validation, and the conditioning differs from
§6.1 (slices vs cells). Dominant slices: n_p = 11–29.

### 6.3 Model tail under the §6.2 scenario (Assessment; `tail.txt`)
Scenario: all six Mordell classes modelled as the class of one (×6 — an assumption, not a bound), Poisson counts,
sums **truncated at 10³¹** (they are not infinite tails).

| a | β | E[10⁵, 10⁷) | E[10⁷, 10¹⁰) | E[10¹⁰, 10³¹) | E[10¹⁷, 10³¹) |
|---|---|---|---|---|---|
| **0.398** | **1.014** (fit) | 5.1 (obs. 6 in 𝔐) | 0.21 (obs. **0**, CERTIFIED) | 6·10⁻⁶ | **2.6·10⁻²⁴** |
| 0.30 | 1 | 30 | 8.4 | 0.03 | 7·10⁻¹³ |
| 0.25 | 1 | 74 | 51 | 1.3 | 2·10⁻⁸ |
| 0.20 | 1 | 198 | 381 | 67 | 7·10⁻⁴ |
| 0.16 | 1 | 459 | 2 311 | 2 196 | 3.0 |
| 0.80 | 0.70 | 17 | 33 | 49 | 4.4 |
| 1.2 | 0.60 | 8.3 | 26 | 4 083 | 3 794 |
| 2.0 | 0.50 | 1.6 | 5.3 | 1.2·10⁶ (truncated; diverges) | 1.2·10⁶ (diverges) |
| 2.7 | 0.50 | 0.09 | 0.05 | 0.20 (truncated; diverges) | 0.14 (diverges) |

* For β = ½ the per-prime rate is ≈ p^{−a√c₁} (c₁ = 0.1286), so the infinite tail **diverges** whenever a√c₁ < 1
  (a < 2.79) — e.g. a = 2.7 (review): the empty census of [10⁷, 10¹⁰) does *not* exclude it (0.05 expected). That law
  is, however, incompatible with the observed small zeros (0.09 expected in [10⁵, 10⁷) vs 6) and with the R₈ sibling
  (§6.1 profile). What the data cannot exclude is a *mixture*: the fitted law plus a small slowly decaying (floor or
  polynomial) component — exactly the escape `DISPROOF_AVENUES.md` §4.5 records. Such a component needs a mechanism not
  visible in the local data examined here.
* Within the tabulated single-component laws, those with ≳ 1 expected zero in [10¹⁷, 10³¹) predict ≥ 26 zeros in
  [10⁷, 10¹⁰) under the ×6 scenario (none observed) — a statement about these rows, not about all laws.
* "Restricting to a family cannot raise the expected number of zeros" holds *inside one coherent probability model*;
  an empirical population fit is not an upper bound for an exceptional family the fit does not resolve. The designs of
  §4 were measured directly (ρ, R₈-zeros), and their measured depression is what enters the model.

## 7. Verdict, screens, proposed FRONTIER text, bottom line

### 7.1 Verdict: **narrowed** (no counterexample; not a HOT LEAD)
* **Search (D1): negative (CERTIFIED for the primes examined).** No prime with R(p) = 0 or R_𝔊*(p) = 0 among
  ≈ 5.5·10⁵ exactly enumerated design and control primes in [10¹⁰, 1.5·10¹³] and 305 386 design primes in
  [10¹², 7.3·10¹⁵] (decision mode, §5.2); 868 562 distinct primes in all. Two new R₈-zeros (20 840 951 041,
  23 296 553 281; both in 𝔐) — expected by F2.
* **Model (D2): no tested structured family reaches 10¹⁷ in the model (Assessment).** Anatomy suggested by the data: a
  counterexample above 10¹⁰ would most plausibly be a prime in 𝔐, ≡ 1 (8) and ≡ 1 (3) (like all 14 zeros), moderately
  square-mimicking (n_p ≈ 11–29), with several small lines u dead — a generic-looking member of the hardest local
  slices, not an extreme one. The families examined act through two T1 truncations (Lemma 2.2: square classes exclude
  solutions with a modulus dividing M; Lemma 2.3: near-square offsets empty the u-lines with k + u ∈ c□, c | u, when
  gcd(m, ct) = 1), and both weaken: ρ(y, p) → 1 at fixed y under the surviving-mass model (measured 0.748 → 0.786 from
  10¹⁰ to 10¹²), the heuristic supply of y-square-mimicking primes is 2^{−π(y)}, a fixed offset's Lemma 2.3 kills carry
  an O_k(1/L) share (Prop 2.4(ii)), and the standard CRT encoding of avoidance buys a polylog (§5.1). Under the fitted law
  and the §6.2 scenario, E[10¹⁷, 10³¹) ≈ 3·10⁻²⁴ over 𝔐.
* **What this does not cover.** Mixtures with a slowly decaying component, growing offsets / other polynomial families,
  and any non-local mechanism ("prime T1") are not excluded; the model is fitted below 2·10⁸ and extrapolated.
* **Validated pieces (EVIDENCE):** the surviving-mass law predicts square-mimicking depressions within ≈ 0–5 %
  (relative); the line-kill accounting matches the near-square depressions within ≈ 0.3–2 points.

### 7.2 Falsifier table, final (restating §0 with the results)
| screen | outcome |
|---|---|
| F1 odd squares | The designs are T1 truncations: Lemma 2.2 (n square mod M ⇒ no solution with a modulus dividing M) and Lemma 2.3 (n + u = m² + ct², c \| u, gcd(m, ct) = 1 ⇒ line u empty) both contain T1 (every M; k = 0). The zero *model* is fitted on primes and is wrong at squares by construction. Primality enters through supply: a prime is a square modulo every y-smooth modulus iff p ≡ 1 (8) and n_p > y (heuristic density 2^{−π(y)+1}), never modulo every modulus; composite zeros get square-likeness through small factors. |
| F2 C-even line | R₈ is the calibration sibling: the same law (a ≈ 0.40, β ≈ 1) fits R₈ and is consistent with R; two new R₈-zeros found in designs near 2·10¹⁰. Local difference (EVIDENCE, small sample): the C-even line has none of the direct small odd-C certificates d = 4u − 1 (3, 11, 19, …); 6/12 R₈-zeros have (p/3) = −1 vs 0/14 (★)-zeros. The model makes no structural odd/even claim; R₈'s mean is half of R's, which is why its zero tail is far longer (z57 fit 10^{14.4}). |
| F3 composites | Not in the domain. Profile: 285 composite zeros are 100 % ≡ 1 (8), 71 % □840, 75 % divisible by 3 — local square-likeness through divisibility (for ℓ \| n no m₂, m₃ is divisible by ℓ), unavailable to primes. |
| F4 known zeros | The engine reproduces the 14 (★)-zeros and the tested 𝔊*-zeros. The probability model fits the R₈/R zero counts (10 R-zeros in the fit range), gives 1.75 vs 3 class-of-one zeros under §6.2, 5.1 vs 6 in 𝔐 ∩ [10⁵, 10⁷), and 0.21 vs 0 in [10⁷, 10¹⁰); it asserts no positivity anywhere and is not calibrated for 𝔊*. |

### 7.3 Proposed FRONTIER §7 text (do not paste blindly)
> (z58 DISPROOF, `Z58_DISPROOF.md`) Counterexample anatomy for (MS), EVIDENCE + Assessment. Structured prime families
> act through truncated T1: a square class mod M excludes the (★) solutions with a modulus 4uB, 4uC−1 or 4BC−1 dividing M
> (Lemma 2.2), and on n = m² + k the u-lines with k + u = ct², c | u, are empty when gcd(m, ct) = 1 (Lemma 2.3; then
> c | k). Measured depressions (exact counts, ≈ 5.5·10⁵ primes at 10¹⁰–10¹³): class of one mod 840 0.88, mod 120 120
> 0.79, n_p > 31 0.75 (0.79 at 10¹²), n_p > 61 0.73; near-square offsets 840 / 1680 / 2520: 0.86 / 0.80 / 0.99, fully
> accounted for by line kills (real proximity alone shows no effect). A surviving-mass model (share of solutions with
> no y-smooth modulus) predicts the square-mimicking values within ≈ 5 % and → 1 as p → ∞ at fixed y. Zero law
> P(R₈ = 0) ≈ exp(−0.40 μ) (β = 1.01; β = ½ disfavoured), consistent with R; Mordell classes show excess zeros within
> Legendre cells. Model tail E[10¹⁷, 10³¹) ≈ 10⁻²³ over 𝔐 under stated scenarios; slowly decaying mixture components
> are not excluded. Targeted search, 8.7·10⁵ primes in 10¹⁰–7.3·10¹⁵: no R-, 𝔊*-zero; two new R₈-zeros
> (20 840 951 041, 23 296 553 281).

### 7.4 Bottom line
The data point to a counterexample to (MS) above 10¹⁰, if one exists, being a prime that looks locally like the known
zeros — in 𝔐, ≡ 1 mod 24, moderately square-mimicking, a few small lines dead — that then loses a ≍ 0.13 L² lottery
with zero probability ≈ e^{−0.4μ}. The structured ways we built to tilt that lottery (deeper square classes,
square-mimicking, CRT avoidance, near-square polynomial families) are truncations of T1 whose bite was measured,
predicted, and seen to weaken with p; the best designs reach ρ ≈ 0.72 at 10¹⁰–10¹², while under the fitted law ρ ≲ 0.46
would be needed for an expected zero near 10¹⁷ even with every prime of that decade as supply. The targeted search
(8.7·10⁵ distinct primes, 10¹⁰–7.3·10¹⁵) found nothing. This prices the tested local/polynomial disproof routes under
an explicit model; it does not exclude slowly decaying mixtures or a global mechanism, and nothing here proves (MS).

## 8. Commands, files, ranges
Run outputs are stored xz-compressed (`runA/`, `runB/`, `runC/` `*.txt.xz`, ≈ 5 MB); `xz -dk` them before running
`scripts/z58_disproof_rho.py` / `z58_disproof_lines.py`, which read the plain `.txt` files.
All runs: `ulimit -v 6000000`, `timeout ≤ 1750`. Engine `gcc -O2 -o /tmp/z58eng scripts/z58_disproof_eng.c -lm`.
* runA (`data/z58/disproof/runA/*.txt.xz`): `EXACT=1 /tmp/z58eng ap 10000000000 N Q a z` for (Q, a, z) = (24,1,0),
  (840,121,0), (840,1,0), (120120,1,0), (2882880,1,0), (840,1,31).
* runB: `scripts/z58_disproof_runB.sh`; runC: `scripts/z58_disproof_runC.sh` (decision mode).
* Cells: `/tmp/z58cells 200000000` (`scripts/z58_disproof_cells.c`, ≈ 100 s, 500 MB) → `cells_2e8.txt`; fits
  `uv run --with numpy --with scipy python scripts/z58_disproof_zerolaw.py data/z58/disproof/cells_2e8.txt 1e4` → `zerolaw.txt`;
  class split `scripts/z58_disproof_lawclass.py`.
* Surviving mass: `scripts/z58_disproof_smooth.c` (exact, stdin primes), `scripts/z58_disproof_survmc.py 100000`
  → `survmc_quick.txt`; tail `scripts/z58_disproof_tail.py 20000 4` → `tail.txt`; ρ `scripts/z58_disproof_rho.py`.
* Profile `scripts/z58_disproof_profile.py`; lines `scripts/z58_disproof_lines.py runA/D1a.txt 1500 12`; offsets
  `scripts/z58_disproof_kbest.py 3000000`; avoidance `/tmp/z58avoid 1000 20000000` → `avoid_2e7.txt`.

## 9. Review log
* **Hostile internal review** (reviewer subagent, deep mode, on commits ba0f16ca..3a6fc82a; it re-derived the cells and
  avoidance files byte-for-byte, re-ran the fits and the tail model, checked all 18 run files, the 868 562 distinct primes
  and the two new R₈-zeros, and found no engine decision/enumeration bug in the recorded ranges). Verdict "request
  changes", 10 MAJOR + 4 MINOR findings, all applied:
  1–2. Tail sums were truncated at 10³¹ but labelled E(> x); β = ½ laws diverge when a√c₁ < 1, and a = 2.7, β = ½ is not
     excluded by the empty [10⁷, 10¹⁰) census → §6.3 relabelled (finite limits, divergence noted), the blanket
     "heavier laws are refuted" removed; added the R₈ profile likelihood (β = ½ disfavoured by Δ = 617) and the
     observation that a = 2.7 fails the small-p zeros; mixtures stated as not excluded.
  3. n_p-slice means used prefix means for exact slices → fixed to 2f_k − f_{k+1}; class-of-one prediction 2.95 → 1.75
     (observed 3); all tail numbers regenerated.
  4. "The excess is square-mimicking heterogeneity" → stated as a hypothesis; non-independence of the calibration noted.
  5. Lemma 2.3's gcd(m, ct) = 1 hypothesis was dropped in applications (counterexample p = 10 017 408 409, u = 5 witness)
     → restored everywhere, exception share (≈ 21 %) disclosed.
  6. "Exactly" / "only non-local mechanisms remain" / "closes the routes" → one-way statements and scoped Assessments.
  7. log L_D ∼ 2D/3 (not D/2); CRT encoding is a construction, not a lower bound.
  8. F1's false "square mod M only for M ≤ p" replaced (17 ≡ 9² mod 64 etc.).
  9. c₁ freezing and the ×6 Mordell factor labelled as scenarios.
  10. F4 now states what was fitted (10 R-zeros, 1 339 R₈-zeros; no 𝔊* calibration).
  11. NSQ numbers regenerated from the final files (0.1151 / 0.1067 / 0.1325 vs 0.1336); imputed weights and overlaps
     in `kbest.py` disclosed; SM97 5 % discrepancy stated; dominant slices 11–29.
  12. Bin cutoff (2^{13.5}), decade assignment and composite-likelihood pooling labelled.
  13. F2 mod-3 explanation restricted to the *direct* small odd-C certificates.
  14. Engine: m ≥ √A and p ≥ A enforced in `nsq`, J0 recorded in the header, a 2⁵³ guard added (the recorded runs used the
     earlier binary: one or two nsq primes just below A may occur, and the runs' headers do not show J0 — NSQfar used
     J0 = 100000, see `scripts/z58_disproof_runB.sh`).
