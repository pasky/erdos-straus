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
| **F1 odd squares** | Squares are the *template* the designs imitate. Lemma 2.2 (PROVED): if n is a square modulo M, no (★) solution at n has any of its three moduli 4uB, 4uC−1, 4BC−1 dividing M. At n = m² this holds for every M, so R = 0. A prime can be a square mod M only for M ≤ p (in practice M ≲ p^{1/2} to leave a supply of primes), so the design kills exactly the solutions with a modulus dividing M. **Primality enters the model only through the supply: a prime cannot be a square modulo all M; the "unbounded M" limit is the square itself.** The zero law is fitted on primes; it is not applied to squares (it would predict R(m²) > 0 with high probability, i.e. the model is wrong at squares exactly because squares are the M = ∞ design). |
| **F2 C-even sub-line** | Used as the *calibration sibling*: R₈ has CERTIFIED zeros at 10¹⁰ (12 in [10¹⁰, 1.1·10¹⁰]). The same designs are run on R₈ and R; the design boost of the R₈ zero rate (measurable) is compared with the boost predicted from the mean depression. What distinguishes the halves for the model: only the size of the mean (R₈ ≈ 0.075 L², R ≈ 0.15 L²) — so the model says nothing structural about C odd vs even, and a design that zeroes R₈ above 10¹⁰ is *expected*, not news. |
| **F3 composites** | Composites are not in the search domain. Profile (§3) checks whether the 285 composite zeros are "square-like" (square mod many small moduli / small square part) — they serve as a second calibration of "local square-likeness ⇒ zero". The generator never claims positivity at composites. |
| **F4 known zeros** | The zero law is *fitted on* the 14 + 38 zeros (and the R₈ zeros); it predicts them by construction and must not be read as positivity there. Profile (§3): local data of the zeros (class mod 840, n_p, square depth) vs controls. |

## 1. Statements attacked (precise)

* **(MS)** (`Z57_SYNTH.md` §1.1): every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 has R(p) ≥ 1. Internal variant: threshold 10¹⁰.
* **(D1) Counterexample search.** Find a prime p ∈ 𝔐, 10¹⁰ < p ≤ 10¹⁴, with R(p) = 0 (or R_𝔊*(p) = 0), searching only
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

**Lemma 2.2 (square-class shadow; PROVED; the T1 mechanism made modular — essentially known, cf. `Z53_UPPER.md` C3.2,
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
*Reading.* n = m² is the case "every u, c = u, t = 1" (T1). A near-square n = m² + k keeps only the lines with
k + u ∈ c·□, c | u: a *truncated* T1.

**Proposition 2.4 (what a fixed offset can kill).** Let k ≥ 1 and K(k) := {u ≥ 1 : k + u = c t² for some c | u, t ≥ 1}.
(i) (PROVED) c | u and c | k + u force c | k, so #(K(k) ∩ [1, U]) ≤ Σ_{c | k} #{t : k < c t² ≤ k + U} ≤ τ(k)(√(U + k) + 1).
(ii) (Assessment) If line u carries mass ≍ L/u (the log-uniform density, EVIDENCE §4.4), the killed mass is
≪ L Σ_{c | k} Σ_{t > √(k/c)} 1/(c t² − k) = O_k(L), a share O_k(1/L) of the ≍ L² total: near-square polynomial
families lose their depression as p → ∞ (measured at 10¹⁰ in §4.3). At k = 0 every c works — T1.

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
  never extreme (no zero has sd > 23, while the controls ≤ 9·10⁶ contain primes with sd up to ≈ 50). This matches the
  model of §6: deep square-mimicking slices are too thin to host the zeros; the dominant slice is n_p ≈ 13–17.
* R₈-zeros show **no** mod-3 preference (half have sd = 3): the modulus 3 enters (★) only through d = 3 = 4·1·1 − 1 at
  C = 1 (odd), which is not on the C-even line. This is the F2 distinction in local terms: the C-even sub-line lacks the
  odd-C small moduli (3, 11, 19, …), so its square-class shadow is weaker and its zeros are spread over all classes.
* Composite zeros are even more square-like (71 % □840) — and 214/285 are divisible by 3 (0 is a square mod 3; for
  ℓ | n no m₂ or m₃ is divisible by ℓ, since ℓ | m₂ | n + u forces ℓ | u, contradicting m₂ ≡ −1 mod u). Composites get
  local square-likeness "for free" through small prime factors; a prime pays a factor 2 per Legendre condition (F3).

## 4. Designs and the depression ρ (exact counts; `scripts/z58_disproof_eng.c`, `runA/`, `runB/`)

### 4.1 Exact means at 10¹⁰–10¹² (CERTIFIED counts; ratios EVIDENCE)
EXACT=1 runs (full enumeration at every prime), consecutive primes of the design from the start point; ρ := mean(R/L²)
over the design / that of C0 at the same start.

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
y-smooth integer, by Hensel and CRT) keeps exactly the solutions none of whose three moduli is y-smooth. Prediction:
ρ(y) ≈ surv(y, p) := share of the solutions of a *generic* prime with no y-smooth modulus.
* Exact share at 300 C0 primes ≈ 10¹⁰ (relative to the 3-smooth baseline that p ≡ 1 (24) already kills): y = 7: 0.936,
  13: 0.882, 31: 0.767, 61: 0.664, 97: 0.592, 199: 0.433, 499: 0.279.
* Monte-Carlo of the log-uniform solution density (`survmc_quick.txt`): 0.945, 0.896, 0.792, 0.688, 0.608, 0.458, 0.294
  at 10¹⁰ (agrees within ≈ 3 %), and at 10¹⁷: 0.982, 0.966, 0.932, 0.898, 0.870, 0.812, 0.730.
* Check against designs (table §4.1): D2 0.745 predicted / 0.748 measured; SM61 0.703 / 0.725; SM97 0.692 / 0.730;
  SM31 at 10¹² 0.785 / 0.786. The y = 31 design weakens from 0.748 at 10¹⁰ to 0.786 at 10¹², as predicted; SM97 (at
  10^{11.2}–10^{13.2}) is no deeper than SM61 — the fading with p cancels the extra square conditions.
* **The square-class kill fades with p at fixed y** (smooth moduli become rare among moduli of size p^{Θ(1)}), and the
  supply of y-square-mimicking primes is 2^{−π(y)+1}, so y can grow only like π(y) ≲ log₂(#primes) ≈ 1.44 log x.

### 4.3 Near-squares: a line-kill effect, not a real-place effect (EVIDENCE)
NSQnear by offset k = p − m²: k = 840: mean R/L² = 0.1136, k = 1680: 0.1056, k = 2520: 0.1325; NSQfar (same algebraic
shape, k ≈ 8.4·10⁷): 0.1324. So *proximity to a square in ℝ does nothing* (k = 2520 equals the far control), while
k = 840, 1680 are depressed by 14 % and 20 %. Lemma 2.3 explains this quantitatively: 840 + u ∈ c□ (c | u) for
u = 1 (29²), 5, 7, 24, 27, 35; 1680 + u for u = 1 (41²), 2 (2·29²), 10, 14, 21, 35; 2520 for no u ≤ 40 with both
weights > 0. The predicted killed share from the measured line masses (§4.4) is 0.141 (k = 840) and 0.179 (k = 1680)
vs measured 0.143 and 0.203 (`kbest.txt`). The PRIMET1 "square-offset near-squares look harder" signal is
consistent with this line-kill mechanism.

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
  L_D = lcm{d ≡ 3 (4), d ≤ D} with log L_D ≈ D/2 (prime number theorem in progressions), so D ≲ 2 log p ≈ 64 at 10¹⁴;
  in 𝔐, P(A_63) ≈ 0.32 already. The enrichment over plain 𝔐 is ≈ 3, i.e. (log p)^{O(1)}, against a zero probability
  e^{−0.4μ}, μ ≍ L² (§6). Selecting on *observed* avoidance (d_min > D by sieving) is conditioning, not design: it is a
  cheap search filter but cannot raise the number of zeros that exist (Assessment).

### 5.2 Decision-mode targeted search at 10¹²–10¹⁴ (pending batch C)

## 6. Zero model and the tail (Assessment unless marked)

### 6.1 A zero law in the local mean (EVIDENCE; `scripts/z58_disproof_cells.c` → `cells_2e8.txt`, `scripts/z58_disproof_zerolaw.py`)
All primes p ≡ 1 (4) in [10⁴, 2·10⁸] (5.54·10⁶ primes; exact R and R₈ by the triple sieve, which reproduces the 12
(★)-zeros in [10³, 2·10⁸] and 1 388 R₈-zeros), cells = p mod 840 × Legendre signs at 11, 13, 17, 19, 23 × half-octave,
smoothed cell mean μ = κ(class) · t(bin) · L². Binomial ML fit P(count = 0 | μ) = exp(−a μ^β):
* R₈: a = 0.398, β = 1.014 (1 339 zeros); calibrated across μ ∈ [4, 30] (observed / predicted per μ-bin: 11/11.7,
  83/75.6, 106/121.5, 145/152, 260/261, 469/456, 265/261).
* R alone: a = 0.403, β = 0.972 (10 zeros) — the same law. The R₈ law predicts 4.1 R-zeros for 10 observed.
* **Not universal across classes.** Observed/predicted R₈-zeros: class of one mod 840 95/61, other Mordell classes
  264/181, non-Mordell 980/1089; for R: 3/0.23, 4/0.79, 3/3.0. The excess sits in the square classes.

### 6.2 The excess is square-mimicking heterogeneity (EVIDENCE)
Model (`scripts/z58_disproof_tail.py`): the class of one mod 840 split into slices by n_p = ℓ (share 2^{−k} for the k-th
prime ℓ ≥ 11), slice mean μ₁(x) · surv(ℓ⁻, x)/surv(7, x) (§4.2; μ₁ = measured class-of-one mean, 0.1146 L² at 10^{6.5},
0.1286 L² at 10¹⁰, frozen above 10¹⁰), and the §6.1 law per slice. Predicted class-of-one (★)-zeros: [10⁴, 10⁵): 1.41,
[10⁵, 10⁶): 1.09, [10⁶, 10⁷): 0.39, total ≥ 10⁴: 2.95 — **observed 0, 1, 2; total 3.** With the n_p heterogeneity
the law is calibrated in the hardest class (κ ≈ 1), so the class excess of §6.1 is explained by local quadratic data.
The dominant slice is n_p = 13–17 at every size — matching the profile of §3.

### 6.3 The model tail (Assessment; `tail.txt`)
For p ≡ 1 (840) (all six Mordell classes ×6, pro-zero):

| a | β | E[10⁵, 10⁷) | E[10⁷, 10¹⁰) | E(> 10¹⁰) | E(> 10¹⁷) |
|---|---|---|---|---|---|
| **0.398** | **1.014** (fit) | 8.8 (obs. 6 in 𝔐) | 0.37 (obs. **0**, CERTIFIED) | 1.1·10⁻⁵ | **4.6·10⁻²⁴** |
| 0.30 | 1 | 47 | 13 | 0.05 | 10⁻¹² |
| 0.25 | 1 | 110 | 76 | 2.0 | 3·10⁻⁸ |
| 0.20 | 1 | 276 | 529 | 92 | 9·10⁻⁴ |
| 0.16 | 1 | 604 | 3 012 | 2 818 | 3.8 |
| 0.80 | 0.70 | 25 | 45 | 60 | 5.2 |
| 2.0 | 0.50 | 2.3 | 6.7 | 1.3·10⁶ | 1.3·10⁶ |

* Every law in this family that puts ≳ 1 expected zero beyond 10¹⁷ predicts ≥ 6.7 zeros in [10⁷, 10¹⁰) in 𝔐, where
  the CERTIFIED census has none (Poisson probability ≤ e^{−6.7} ≈ 10⁻³) — the (★)-specific version of
  `DISPROOF_AVENUES.md` §4.5.
* The structured families of §4 are *sub-populations* of this model: restricting to a family cannot raise the expected
  number of zeros above the population's, and the families' heterogeneity (square-mimicking slices; line kills) is the
  heterogeneity that §6.2 integrates. Line-kill heterogeneity (§4.4) is inside the cell variance that the fitted law
  absorbs; its share per line decays like 1/L, so the fitted law is, if anything, pessimistic at large p (Assessment).

## 7. Verdict, screens, proposed FRONTIER text, bottom line (pending)
