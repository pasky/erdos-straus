# Z57_SUMMARY — wave z57 "big fish": R_𝔊* ≥ 1, full Type II ≥ 1, complementarity, the minimal missing statement

**ES is OPEN.** Every result here is internal. Wave z57 (brief `z52bbriefs/z57_lanes.md`) ran six lanes: two tryhard twins
on the Theorem V family 𝔊* (BFO, Opus; BFF, Fable), a tryhard on the full Type II family (BFII), two structured-depth lanes
(COMPLEMENT: joint zero structure of different certificate families; SYNTH: the minimal missing statement), and a
second-round referee of both papers (REREF). Each lane memo had internal hostile review(s) and a cross-model review
(`data/z57/xreview/REVIEW_<LANE>.md`). BFO, BFF, BFII and SYNTH were ACCEPT-WITH-FIXES. **COMPLEMENT's first draft was
REJECTED as written** (a false five-family union claim and a false PROVED covariance formula; §5); it was corrected
(commits 919284fd, 2a1d2164) and merged. All required fixes were applied in the memos; none of the corrected memos was
re-reviewed by the cross-model reviewer. This summary carries scopes only loosely; each memo's own statement governs.

## 0. Bottom line

**The big fish was not caught.** The following target statements of the brief all remain open:
* **R_𝔊*(p) ≥ 1 for every sufficiently large prime p ≡ 1 (mod 4)** (BFO, BFF) — not proved, neither eventually nor
  effectively with p₀ ≤ 10¹⁰;
* **f_II(p) ≥ 1 (a Type II solution exists) for every sufficiently large prime p ≡ 1 (mod 4)** (BFII) — not proved;
* **a complementarity theorem** "R_A(p) + R_B(p) ≥ c·(main)" or "R_A(p) = 0 ⟹ R_B(p) ≥ 1" at a single p for two certificate
  families (COMPLEMENT) — none proved; no anti-correlated candidate pair was found;
* **the minimal missing statement (MS)** (SYNTH) — stated precisely, not proved.

Consequently full (★) positivity at every large prime, and ES, remain open. B2 (the tied-modulus divisor event at one
integer) did not move. **Nothing has been posted.** What the wave produced:

* **(MS), one sentence (SYNTH; §1).** *Every prime p > 10¹⁷ with p mod 840 ∈ {1, 121, 169, 289, 361, 529} has an integer
  d ≥ 3, d ≡ 3 (mod 4), such that r = (−p mod d) ∈ {1, …, d − 1} divides (d + 1)/4.* Equivalent to R(p) ≥ 1; (MS) ⟹ ES
  (PROVED relative to Mordell's reduction and Salez's verification to 10¹⁷). Sufficient, not necessary.
* **The numerator-8 screen became concrete (SYNTH; CERTIFIED).** The C-even half of (★) is exactly the c = 1 line of 8/p;
  it vanishes at exactly 12 primes p ≡ 1 (4) in [10¹⁰, 1.1·10¹⁰], four of them in Mordell's classes. Any argument for
  (MS) at threshold 10¹⁰ must contain a step that fails on that sub-line.
* **Effectivity calibration (SYNTH, BFO; Assessment, model-based).** Within a hypothetical Burgess envelope and fitted
  zero-tail models, a "main term − explicit error" proof of (MS) with crossover below 10¹⁷ faces a trade-off between
  envelope and family size.
* **Theorem W (BFO; PROVED).** #{p ≤ x prime, p ≡ 1 (4) : R_𝔊*(p) = 0} ≪_A x/(log x)^A for every A. An average statement (B6).
* **Theorem 1 / Lemma 1.4 (BFF; PROVED).** Exact "defect/hyperbola" form of R_𝔊*(p) ≥ 1 over moduli d ≤ ⌊p^{3/4}⌋ + 1
  together with the 𝔊* inequality, and every hit has (d/p) = −1.
* **𝔊* census extended (BFF, BFO; CERTIFIED).** R_𝔊*(p) = 0 at exactly 38 primes p ≡ 1 (4) ≤ 10¹², the last 564 661 441.
* **Theorem G (BFII; PROVED, effective, p₀ uncomputed).** The genus main term of full Type II (witness f < p) is
  ≥ 10⁻¹⁰(log p)³ at every large prime p ≡ 1 (4): c buys a log p in the **genus main term only**.
* **COMPLEMENT: narrowed, scoped negative (statistical, over primes).** No robustly negative association between the
  counts of any two certificate families after local controls (EVIDENCE); same-integer slices are positively coupled
  (Theorem C, PROVED for bounded shifts and small divisors, over primes in a fixed class); four implications
  "R_A(p) = 0 ⟹ R_B(p) ≥ 1" are refuted at primes (CERTIFIED). Pointwise complementarity is not excluded for five pairs.
* **Papers.** Second-round cross-model referee: both MINOR REVISION, no GAP/WRONG. Count note: round-2 fixes applied
  (a94666aa). HC note: mathematical content accepted; the required stable public supplement still does not exist —
  **needs the user**.

## 1. SYNTH — the minimal missing statement (`Z57_SYNTH.md`; cross-review ACCEPT-WITH-FIXES)

Notation (FRONTIER §2.1, `Z56_FAMDESIGN.md` §1): R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n}; M_gen = genus (order ≤ 2) part
of R; X := R − M_gen; L := log p; 𝔐 := {1, 121, 169, 289, 361, 529} ⊂ ℤ/840 (Mordell's classes, all ≡ 1 (8));
c_V := 5/(4π²) ≈ 0.12665.

**(MS)** *For every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 there is an integer d ≥ 3, d ≡ 3 (mod 4), such that the least
residue r = (−p mod d) ∈ {1, …, d − 1} divides (d + 1)/4.* Necessarily d ≤ (4p + 1)/3. Positivity of d is essential
(read literally, d = −1 would give r = 1 | 0; cross-review fix 1).

* **Equivalent forms (PROVED).** Lemma A.1 (essentially `Z56_FAMTRY.md` Lemmas 1.1–1.4) is a bijection d ↔ (u, B, C):
  d = 4uC − 1, u = r, C = (d + 1)/(4r), B = (n + r)/d. Hence for a prime p, (MS) at p ⟺ R(p) ≥ 1 ⟺ X(p) > −M_gen(p)
  (Lemma 1.2: definitions; the same holds for every subfamily).
* **Sufficiency (PROVED relative to the cited results).** Mordell's identities reduce ES to primes p ≡ 1 (4) with
  p mod 840 ∈ 𝔐 (re-proved for p ≡ 1 (8) as UPPER2 Prop 3.1 / Lean `HC.lean` (d)); R(p) ≥ 1 gives
  4/p = 1/(uBC) + 1/(pBC) + 1/(puC); Salez (arXiv:1406.6307) verifies ES for n ≤ 10¹⁷ (the cross-review checked Salez
  §§4.1–4.3, not only the abstract). This is sound relative to Salez's computation, not a fresh certification through
  10¹⁷. *Internal-census variant:* threshold 10¹⁰ also suffices, using R(p) ≥ 1 for primes p ≡ 1 (4) in
  (8 813 281, 10¹⁰] (CERTIFIED, FRONTIER §2.1) and the (★) ∪ López-line census to 10⁸ ((J)89) for the 14 (★)-zeros.
* **Scope.** (MS) is a *sufficient* target for ES by the (★) route, not a necessary one (other Type II lines, Type I or
  a non-counting proof could prove ES). "Weakest sufficient target among the (★) subfamily-positivity statements" is
  Assessment, restricted to that menu; strict logical separation of the eventual statements above 10¹⁰ is not claimed.
  The proved main terms do not weaken (MS) logically (Lemma 1.2). To finish ES by this route (MS) is needed at *every*
  p > 10¹⁷: an eventual statement with unspecified or astronomical p₀ does not suffice (§1.4; a statement about this
  route, not a necessity theorem).

**The ladder (Proposition 1.1, PROVED; statements for primes p > P in Mordell's classes).**

| rung | statement | data (zeros among primes p ≡ 1 (4)) | at P = 10¹⁰ |
|---|---|---|---|
| L0 | ES(p) | none known; verified ≤ 10¹⁷ (Salez) | true ≤ 10¹⁷ |
| **L2 = (MS)** | R(p) ≥ 1 | 14 zeros, last 8 813 281; none in (8 813 281, 10¹⁰] (CERTIFIED); fit x* ≈ 10^{7.3} | consistent |
| L3 | R_𝔊*(p) ≥ 1 | 38 zeros ≤ 10¹⁰ (≤ 10¹², §3), last 564 661 441; fit ≈ 10^{8.3} | consistent |
| L3′ | R_odd(p) ≥ 1 (C odd) | 423 zeros ≤ 10⁸, 156 in [10⁷, 10⁸) | not tested above 10⁸ |
| L3″ | R₈(p) ≥ 1 (C even = c = 1 line of 8/p) | 12 zeros in [10¹⁰, 1.1·10¹⁰], 4 in Mordell's classes | **false** |
| L4 | R_H3(p) ≥ 1 (complete levels 64C³ ≤ p) | 873 zeros ≤ 10¹⁰, last 9 466 909 909; fit ≈ 10^{12.6} | at risk (model) |
| L5 | X_𝔊* ≥ −(1 − ε)M_𝔊*, fixed 0 < ε < 1 | false at every 𝔊*-zero with M_𝔊* > 0; vacuous where M_𝔊* = 0 (p = 37) | not refuted |
| L6(η) | X(p) ≥ −(c_V − η)L², η > 0 | η = 0 diagnostic fails at 7 non-Mordell primes in (10⁷, 10⁸] | not refuted |

Arrows: L4 ⟹ L3 ⟹ L2 (monotonicity; H3 ⊂ 𝔊*); L3′ ⟹ L2; L3″ ⟹ L2; for fixed ε > 0, L5 ⟹ L3 wherever M_𝔊*(p) > 0; for
fixed η > 0, L6(η) ⟹ R(p) ≥ ηL²/2 > 0 for p ≥ p_V(η) (Theorem V). **No arrow L6 ⟹ L5 or L5 ⟹ L4 is claimed.** L5 needs
P ≥ 564 661 441 for 𝔊* (P ≥ 8 813 281 for the full family): both zeros are in 𝔐 and have positive genus mass in 𝔊*.

**Numerator-8 screen (§2.1).**
* Lemma 2.1 (PROVED): (u, B, 2C′) solves (★) iff 8/p = 1/(uBC′) + 1/(pBC′) + 1/(puC′). So R = R_odd + R₈, where R₈ (C even)
  is the c = 1 Type II line of numerator 8. (A zero of R₈ is a zero of that one line, not a failure of 8/p.)
* CERTIFIED to 10⁸ (two engines agree on [10³, 2·10⁶]; the cross-review reran the scan byte-identically): R₈ = 0 at
  1 270 primes p ≡ 1 (4) ≤ 10⁸ (last 99 671 381); R_odd = 0 at 423.
* **CERTIFIED above 10¹⁰.** Over all 21 668 737 primes p ≡ 1 (4) in [10¹⁰, 1.1·10¹⁰], R₈ = 0 at exactly 12 primes;
  "exactly twelve" rests on one audited exhaustive engine; all twelve were re-verified by two independent enumerators
  (and again by the cross-review). Four are in Mordell's classes — 10 301 993 881, 10 529 331 121, 10 532 106 649,
  10 868 474 401 — each with R > 0; the largest zero is 10 917 229 157.
* *Screen consequence.* "R₈(p) ≥ 1 for all primes p > 10¹⁰ in Mordell's classes" is false. An argument for (MS) at
  threshold 10¹⁰ that remains valid on the C-even sub-line proves a false statement; it must contain a step that fails
  for that sub-line, or a larger threshold for it. These zeros lie above the internal 10¹⁰ full-(★) census range, below
  Salez's 10¹⁷, and **do not refute (MS)**.
* Model (Assessment): P(R₈ = 0) ≈ exp(−0.627 − 0.0260 L²) on [10⁵, 10⁸]; predicted 11.1 zeros in the interval (12 found);
  ≈ 0.003 expected zeros above 10¹⁷, crossover x* ≈ 10^{14.4}. At the Salez threshold the screen therefore reverts to the
  qualitative FRONTIER §4 item 2.

**Uniform form L6 (§2.3; EVIDENCE — long-double evaluation of exact finite genus sums).** All 334 primes p ≡ 1 (4) in
(10⁷, 10⁸] with R(p) ≤ 8 were tested. The η = 0 diagnostic X ≥ −c_V L² fails at exactly 7 of them, **all outside 𝔐**
(p mod 840 ∈ {241, 257, 409, 577}). It holds at all 249 tested Mordell-class primes (closest +0.0064 L² at 72 690 361),
where M_gen/L² ∈ [0.101, 0.135] with mean 0.117 < c_V: at these sizes the asymptotic constant of Theorem V is not reached
in Mordell classes. The violation count is a lower bound (R > 8 untested). No eventual statement is refuted.

**Effectivity calibration (§3.I; PROVED lemmas + model Assessment).**
* Lemma E1 (PROVED, elementary): on a Theorem-V slice at Burgess margin μ := b − (1 + a)/4, the optimised Burgess bound
  saves at most p^{−μ²/(1+a)} — **for the worst allowed conductor in this single Burgess bound expression**; not a bound
  on true cancellation, at smaller actual conductors, or for other arguments.
* Lemma E2 (PROVED, geometry): the margin set S_μ has area 2μ/3 + 4μ²/3 (0 < μ ≤ 1/12).
* Proposition E3 (PROVED arithmetic; sufficient budget, not necessary): R ≥ M − E with M ≥ mL², E ≤ KL^k p^{−δ} certifies
  R(p) ≥ 1 once δ > [log(K/m) + (k − 2)log L]/log p; with m = 0.10, (K, k) = (1, 2) needs δ > 0.0588 at p = 10¹⁷.
* **Assessment E4 (hypothetical envelope + fitted model).** Uniform-margin subfamilies F_μ ⊂ 𝔊*_{1/15}; zero counts and
  fits on all primes p ≡ 1 (4) in [10⁵, 10⁸] (Mordell-domain refit as a diagnostic); double-precision membership, so
  model families. Raising the margin lowers the envelope crossover but raises the family's fitted zero tail:

  | share of area(G_{1/15}) | envelope crossover (K,k) = (1,2) | fitted x*, all / Mordell |
  |---|---|---|
  | 90 % | 10^{521.2} | 10^{12.0} / 10^{10.9} |
  | 79 % | 10^{162.8} | 10^{14.4} / 10^{14.2} |
  | 74 % | 10^{118.1} | 10^{15.4} / 10^{15.3} |
  | 50 % | 10^{39.3} | 10^{23.9} / 10^{23.3} |

  Conditionally on x* increasing as the kept share decreases (and the envelope crossover decreasing in μ), max(envelope
  crossover, x*) ≳ 10^{23.9} (Mordell domain ≈ 10^{23.3}) for every uniform-margin family. These are envelope crossovers
  and model extrapolations, **not lower bounds on the threshold of any actual theorem**; slice-varying envelopes have
  different families with no fitted tails. Separately, the remainder X has no explicit-constant input at all in z53–z56.
  Falsifier: an explicit-constant estimate for a (★) sub-family with polylog main term, model-positive above 10¹⁷,
  crossing below 10¹⁷. Theorem V's actual explicit constants were not computed.
* Escape hatches named (none developed): GRH-explicit main terms; a high-multiplicity encoding keeping the tie; larger
  certified ranges (illustrative only); a non-counting proof.

**Mechanisms II and III (prior in shape; new content is diagnostics).**
* II, split-and-complement (not killed): Lemma S1 (PROVED; C-parity split, López lifting classes). C-parity
  complementarity above 8 813 281 is full-family positivity on the same domain (CERTIFIED to 10¹⁰), hence (MS) restricted
  to its domain; the halves are positively associated (corr ≈ +0.29 at 10⁷–10⁸, EVIDENCE). No mechanism found.
* III, covering rigidity + explicit least non-residue: Lemma A.1(b) (PROVED): every hit class has Jacobi symbol −1, so
  squares never hit. Prop A.2 (PROVED, p ≡ 1 (8) only): SMCR(D, g) and n_p ≤ g ⟹ R(p) ≥ 1. **Prop A.3 (PROVED, a
  corollary of `Z55_HCF.md` T3.1): SMCR(D, g) is false for every finite D ≥ 3 and every g ≥ 11.** CERTIFIED complement
  via R(329 617) = 0. Size-controlled variants are not excluded; none was formulated. The variant "R(p) = 0 ⟹ n_p > 2 log²p"
  fails at all 14 (★)-zeros (n_p < 2 log²p there).

**Verdict: narrowed.** (MS) pinned down with its ladder; numerator-8 screen concrete; calibrated, model-based effectivity
trade-off; B2 did not move.

## 2. BFO — tryhard on R_𝔊* ≥ 1 (`Z57_BFO.md`; cross-review ACCEPT-WITH-FIXES, Theorem W CORRECT)

**Target not reached.** 𝔊* := {(o, e) : max(o, e)⁴ > min(o, e)·p} (`Z56_FAMDESIGN.md` §1).
* **Theorem W (PROVED rel. Montgomery's arithmetic large sieve with the Montgomery–Vaughan constant, Dirichlet–Mertens in
  fixed progressions, and an elementary Rankin-type bound proved in full).** For K ≥ 1 put κ_K := Σ_{C≤K} 1/φ(4C)
  (≥ ¼ log K). Then for x ≥ 2: #{p ≤ x prime, p ≡ 1 (4) : R_𝔊*(p) = 0} ≪_K x/(log x)^{1+κ_K}; hence ≪_A x/(log x)^A for
  every A > 0. It uses only the complete levels C ≤ K and their prime divisors ℓ ≡ −1 (mod 4C): the bound holds for the
  primes with no hit at any level C ≤ K, a set containing every 𝔊*-zero p > 64K³. Assessment: weaker than Vaughan-type
  exceptional-set bounds for the whole ES equation; letting K grow gives at best exp(−c√log x) savings (heuristic). An
  upper bound for a count; nothing about a prescribed p (B6).
* **PROVED reformulations (Lemmas 1.1–1.6, checked numerically):** shift form R(n) = #{(s, t) : 4st | n + s + t} (odd
  n ≥ 3); divisor-in-class form; level form; complete levels 64C³ ≤ p lie in 𝔊*; mod-p small-solution form (R(p) ≥ 1 ⟺
  p | 4oeC − o − e with 0 < 4oeC − o − e < 2p, unrestricted R); Jacobi lemma (`Z55_CROSSO` §1).
* **PROVED structure (Lemmas 2.1–2.3).** 2.1: all three fibrations collapse to "a divisor of a p-shifted integer in a
  class tied to the fibre". 2.2: the class condition is decided by quadratic characters only for modulus 4m | 24, i.e.
  the eight integers p + 1, p + 2, p + 3, p + 6, 4p + 1, 8p + 1, 12p + 1, 24p + 1. 2.3: characters of order dividing k
  recover a class exactly only modulo divisors of Λ(k) (finitely many moduli). The methodological consequence ("reciprocity
  → Burgess sees only the genus layer") is **Assessment**, not a theorem about all methods.
* **CERTIFIED (Z56 decider unchanged; four complete runs):** R_𝔊*(p) ≥ 1 (and R(p) ≥ 1) for all 213 578 615 primes
  p ≡ 1 (4) in (10¹⁰, 2·10¹⁰]. The cross-review reproduced the four chunk prime counts, all 20 exceptional rows and
  4·10⁶ integers of reruns; it did not repeat the full solution census. Side result: the Burgess-only family
  F4L = 𝔊*_{1/15} has a new zero 11 406 999 713 (independently confirmed).
* **EVIDENCE.** The 38 𝔊*-zeros lean towards pseudo-squares (least prime non-residue ≥ 11 at 20/38 vs ≈ 6.3 % of random
  p ≡ 1 (4) in [10⁷, 10⁸)), but 8 zeros (p ≡ 5 (8)) have q(p) = 2: no uniform pseudo-square lemma covers them; eventual
  versions are not excluded. Level-K no-hit rates match the sieve dimension κ_K for K ≤ 3.
* **Assessment (§4.2, effectivity).** Even with constant 1 in Burgess, the relative bound at length q^{1/3} is 0.995 at
  q = 10¹⁰ (0.857 at q^{0.4}); it drops below ½ only near q ≈ 10^{67.2} (θ = 1/3), 10^{23.7} (θ = 0.4), 10^{9.4}
  (θ = 1/2). So Theorem V's architecture does not give p₀ ≤ 10¹⁰ — a calibration of the displayed model bound, not a
  theorem about every Burgess-based argument. Pólya–Vinogradov-strength tools save only for fixed θ > 1/2 (density main
  term ≤ 1/(2π²) per log²p there), and no finite p₀ follows from the displayed constants.
* **Assessment (§2.6):** no reduction of the target to GRH, EH or Hypothesis H was found (GRH has pointwise consequences,
  but none was turned into the order-≥3 divisor-in-class event).
* Restrictions (cross-review): Pólya–Vinogradov claim limited to fixed θ > 1/2; GRH not described as averaging-only.

## 3. BFF — tryhard twin on R_𝔊* ≥ 1 (`Z57_BFF.md`; cross-review ACCEPT-WITH-FIXES)

**Target not reached; "narrowed" means reformulation, not analytic progress.** p ≡ 1 (4) prime throughout.
* **Theorem 1 / Lemmas 1.2–1.3 (PROVED, elementary).** For d ≡ 3 (mod 4), p ∤ d, let n_d := least positive residue of −p
  mod d and C_d := least positive residue of −(4p)⁻¹ mod d. Then 4n_dC_d ≡ 1 (mod d), and HIT(d) :⟺ 4n_d | d + 1 ⟺
  4C_d | d + 1 ⟺ 4n_dC_d = d + 1 ⟺ n_dC_d ≤ (d − 1)/2. HIT(d) gives the (★) solution (n_d, (p + n_d)/d, C_d); each
  solution arises from exactly two d. **R_𝔊*(p) ≥ 1 ⟺ some d ≡ 3 (4), d ≤ ⌊p^{3/4}⌋ + 1, has HIT(d) and
  max(n_d, m)⁴ > min(n_d, m)·p**, m = (p + n_d)/d; HIT(d) with d⁴(d + 1) ≤ 4p³ (e.g. d ≤ p^{3/5}) is automatically in
  𝔊* (sufficient, not necessary).
* **Lemma 1.4 (PROVED).** HIT(d) ⟹ (−n_d/d) = −1, (p/d) = −1 and (d/p) = −1. Cor 1.5: no hit at odd squares (T1). For
  D ≥ p^{1/4+ε}, Burgess gives D/8 + O(D^{1−δ}) non-residues d ≡ 3 (4) below D (corrected from D/4); a positive proportion
  of non-residues among *all* d ≤ D is known from p^{1/(4√e)+ε} (Banks–Garaev–Heath-Brown–Shparlinski Thm 2.1), while
  equidistribution in d ≡ 3 (4) is known from p^{1/4+ε}. Neither says anything about HIT; the p^{1/4} threshold is
  sufficient for the quadratic condition, not a proven obstruction below it.
* **Lemma 1.6 (PROVED, standard):** failure of levels 1, 2, 3 as primitive norm-form conditions on 4p + 1, 8p + 1,
  12p + 1; all 38 zeros satisfy them.
* **§2 (PROVED identities; Assessment conclusions).** H(p; D) := #{d ≡ 3 (4), d ≤ D : HIT(d)} = A(D) + E(p; D) with
  A(D) = (1/8)log²D + O(log D) (not a proven prime-conditioned mean). Sufficient (PROVED implications, none proved):
  (S1) some d ≡ 3 (4), d ≤ p^{3/5}, has (−p mod d)·(−(4p)⁻¹ mod d) < 5d/4; (S2) divisor form with d ≤ p^{3/5};
  (S3) some level C ≤ (p/64)^{1/3} has a divisor ≡ −1 (mod 4C) of 4Cp + 1. Linnik example (PROVED): for every large p₀
  there are primes p ∈ [p₀, p₀^{C′}] with H(p; c·log p) = 0. Assessment: d ≤ p^{1/3} is where *this lane's*
  additive-character attack stops; larger-d routes are not excluded; the sieve bullet is implementation-scoped.
* **CERTIFIED (independent decider: by d, not by levels C, integer-exact membership).** It re-certifies z56's range
  (exactly 38 𝔊*-zeros ≤ 10¹⁰) and extends it: **no 𝔊*-zero in (10¹⁰, 10¹²]**, so R_𝔊*(p) = 0 at exactly 38 primes
  p ≡ 1 (4) ≤ 10¹², the last 564 661 441 (18 803 924 340 primes decided). Provenance: the cross-review exhaustively reran
  [5, 10⁹] (same 38 zeros), parsed all 192 block files (contiguous coverage, sums), re-verified the 192 extremal first-hit
  witnesses and the window [999 999 900 001, 10¹²]; it did not repeat the full 10¹² exhaustion. BFO's run (§2)
  independently covers (10¹⁰, 2·10¹⁰].
* **EVIDENCE.** First-hit exponents θ₁ = log d₁/log p: median 0.060 / 0.053 / 0.085 at 10⁸ / 10⁹ / 10¹⁰; exhaustive
  maximum d₁ = 787 439 ≈ p^{0.705} on (10⁸, 10⁹]; per-block maxima below p^{0.64} on (10⁹, 10¹²]. Model tail beyond 10¹²
  ≈ 6·10⁻¹⁴ expected zeros — a model extrapolation only. All 38 zeros have (p/3) = +1; least *odd* prime QNR in
  {5, …, 29} (2 is a QNR at the 8 zeros ≡ 5 (8)); they are not confined to Mordell's classes.
* Restrictions (cross-review): Burgess count D/8; BGHS distinction; "decisive range" only an attack choice; no universal
  sieve-impossibility; "least odd prime QNR"; model limits kept.

## 4. BFII — tryhard on full Type II (`Z57_BFII.md`; cross-review ACCEPT-WITH-FIXES, Theorem G CORRECT)

**f_II(p) ≥ 1 for all large p NOT proved; lane outcome: narrowed / target unresolved.** N_II(n) := #{(a, b, c, d) ∈ ℕ⁴ :
4abcd = a + b + nc} (ET (2.15), no gcd condition).
* **Exact forms (PROVED).** Lemma 1.0: for a prime p, N_II(p) ≥ 1 ⟺ f_II(p) ≥ 1 (for composite n the ET correspondence
  needs gcd(abd, n) = 1; n = 63, (3, 6, 1, 1) is a non-Type-II N-point). Lemma 1.1(d), **target-set form:**
  N_II(n) = Σ_{f ≡ 3 (4)} #{(a, c) : ac | m_f, a·c⁻¹ ≡ −n (mod f)}, m_f = (f + 1)/4 — a Type II solution exists iff
  −p mod f ∈ T_f for some f ≡ 3 (4). Slice forms (e): every two-parameter slice is one integer's divisor problem
  (n + 4a²d, cn + a, 4c²dn + 1). (f): N_II = Σ_c R_c with R_1 = R.
* **QNR witness (PROVED).** Lemma 2.1, Prop 2.2: every solution at odd n has (n/f) = −1 for both witness moduli
  f = 4acd − 1, f′ = 4bcd − 1. Cor 2.3: N_II(m²) = 0 (T1). Cor 2.4 (witness barrier): at p ≡ 1 (4) every solution has
  4acd − 1 ≥ n_p and 4bcd − 1 ≥ n_p, so an argument always producing a witness ≤ g(p) proves n_p ≤ g(p) (f ≤ p^θ with
  θ < 1/(4√e) would beat Burgess). The quoted Graham–Ringrose / Montgomery lower bounds for n_p are from memory and are
  **not** in the PROVED inventory.
* **Complete moduli and coverings (PROVED; list CERTIFIED below 4000).** Prop 3.1: f = 3, 7, 15 are complete
  (−T_f = all Jacobi non-residue units), no other f < 4000 is, and only finitely many f are; hence f_II(p) ≥ 1 whenever p
  is a non-residue mod 3, 5 or 7 (Mordell-type, explicit). Prop 3.2: no finite set of witness moduli covers all primes
  (p ≡ 1 mod 4·lcm(f_i), Dirichlet).
* **Theorem G (PROVED; Burgess + Pólya–Vinogradov only; effective, p₀ not computed; Appendix A audited CORRECT by the
  cross-review).** The genus main term G(p) of the Type II sub-family with witness f < p satisfies
  **G(p) ≥ 10⁻¹⁰(log p)³** for every sufficiently large prime p ≡ 1 (4), already on the box of odd squarefree coprime
  a, c with p^{0.004} < a ≤ p^{0.006}, p^{0.080} < c ≤ p^{0.085}, p^{0.90} < f ≤ p^{0.99}. Identity behind it: the genus
  weight depends on (a, c) only through u = ac, so G is the τ(u)-weighted (★)-genus term in f-coordinates. **Genus part
  only:** nothing about N_II(p); no upper bound for G; the c = 1 genus mean ≍ log²p comparison is heuristic. At odd squares
  A = G = X = 0, which says nothing about the size of X(p).
* **§5.5 (CONDITIONAL; the implication PROVED).** Hypothesis SB: for every large prime p ≡ 1 (4) some
  F ∈ [p^{0.9}, ½p^{0.99}] has A_F(p) ≥ ½G_F(p) (actual vs genus count of solutions with witness in (F, 2F]). SB ⟹
  f_II(p) ≥ 1 for all large p. SB is non-standard; no implication from GRH or standard AP estimates is established.
* **CERTIFIED.** N_II(n) for all odd n ≤ 10⁷: zero exactly at the odd squares (1580 of them in (1, 10⁷], plus n = 1) and
  at n = 4545; every odd prime p ≤ 10⁷ has N_II(p) ≥ 1. Least-witness scan: every prime p ≡ 1 (4) below 10⁹
  (25 423 491) and in [10¹², 10¹² + 10⁸) has a witness f ≤ 3263 (max at p = 605 531 161); least witness ≥ n_p throughout.
  Cross-review: decisive computations rerun with the inspected code (not a new independent engine).
* **EVIDENCE.** Mean N_II ≈ 0.076 log³p; min N_II/log³p ≈ 0.013 (f_II: 0.012) on [10⁶, 10⁷); c ≥ 2 carries 86 % of
  solutions and rescues every (★)-zero ≤ 10⁷ (N_II ∈ [14, 156] there). In one witness block at p ≈ 10⁷: mean
  |A − G|/G = 0.20 (Type II) vs 0.36 (c = 1), min A/G = 0.30 vs 0.
* **Assessment.** c is not a free variable at fixed p in these representations; the order-≥3 remainder involves
  characters of unbounded order with no sufficient aggregate bound supplied — not a proved impossibility. c gains a log p
  in the genus main term and, empirically, a constant factor in relative fluctuation. Proved barriers are only Prop 3.2
  and Cor 2.4.

## 5. COMPLEMENT — joint zero structure of certificate families (`Z57_COMPLEMENT.md`; cross-review REJECT as written, corrected)

**Cross-review outcome (`data/z57/xreview/REVIEW_COMPLEMENT.md`).** The first draft was REJECTED for recording: (1) its
"five-slice union vanishes at 105" was the *three*-family union STAR ∪ B1 ∪ I1; c2(105) = 1 ((t, u, v) = (24, 3, 3) ∈ W(210),
4/105 = 1/27 + 1/1890 + 1/1890), and **the five-family union STAR ∪ B1 ∪ I1 ∪ c2 ∪ c3 has no non-square zero
n ≡ 1 (4), 5 ≤ n ≤ 4 000 001**; (2) Theorem C(ii)'s displayed covariance formula was false without the hypothesis that
every prime of b·c·(cu − b) divides M (counterexample U = 1, M = 4, b = 3); (3) Corollary C1's exact identity fails for
small p (p = 17); (4) decade-only joint-zero predictions did not control residues. Pairwise falsifiers do not refute
unions, and positive covariance does not forbid pointwise coverage ((1,0), (0,1), (10,10) equiprobable: Cov = 179/9 > 0).
All fixes were applied; only the corrected claims are recorded below and in FRONTIER. The corrected memo was not
re-reviewed by the cross-model reviewer.

Menu: STAR = (★); B1 = b = 1 (López Type A) line; I1 = ET Type I slice a = 1 (with boundary words); c2, c3 = ET Type II
c-lines; 𝔊* and its Burgess corner K; QR = Jacobi-(+1) interior words (placebo, not certificates).
* **Lemma W (PROVED).** Every menu family is a set of words of W(p) = {tuv − u − v = p} or W(cp) (STAR = {4 | t},
  B1 = {4 | u or v}, I1 = {4 | tu − 1 or tv − 1}, c-lines = {4c | t} in W(cp)). On interior words of W(p) the three
  certificate slices are exactly the Jacobi-(−1) words (DEDEKIND_ES Thm 4.5; re-derived by the cross-review);
  STAR ∩ I1 = ∅; apart from the boundary word t = 1, slice membership is a function of (m mod 4u, p mod 4u) (shift form)
  or of p mod 4uv (pair form).
* **Theorem C (PROVED, Bombieri–Vinogradov; over primes p ≤ x, p ≡ a (M), 4·lcm(1..U) | M, divisors m ≤ x^θ, θ < 1/4,
  coprime to M).** (i) Two class counts on the *same* integer p + u (u ≤ U) have covariance ≥ κ(log x)³ − C(log x)² and
  correlation ≥ c₀ > 0. (ii) On *different* integers (p + u and cp + b, cu ≠ b), **provided every prime dividing
  b·c·(cu − b) divides M** (automatic for two shifts u′ ≤ U), the covariance is −Θ((log x)²) (CRT exclusion; correlation
  ≍ −1/log x). Corollary C1 (slices STAR, B1, I1, QR) holds for p > U·x^θ; the initial segment is negligible in the
  moments. A theorem about the distribution over primes in a fixed class (B6), for bounded shifts and small M-coprime
  divisors; not about a single p.
* **Proposition F (CERTIFIED; census ≤ 4·10⁶).** For every pair in {STAR, B1, I1, c2, c3} there are non-square composites
  n ≡ 1 (4) with both counts zero (e.g. 105, 4545 for STAR & B1); at primes, R_STAR = R_c2 = 0 at 102001;
  R_STAR = R_c3 = 0 at 577, 5569, 83449, 1 134 241, 1 726 201; R_B1 = R_c2 = 0 at 193, 2521; R_B1 = R_c3 = 0 at 193. So
  "R_A(p) = 0 ⟹ R_B(p) ≥ 1" is false at primes for STAR ⇒ c2, STAR ⇒ c3, B1 ⇒ c2, B1 ⇒ c3 (and the reverses). For STAR & B1,
  B1 & I1 and I1 & c2 every composite falsifier found is divisible by 3.
* **Zero census, n ≡ 1 (4), 5 ≤ n ≤ 4 000 001 (CERTIFIED counts; independence predictions EVIDENCE, stratified by decade ×
  n mod 840).** Primes (141 502): I1 never vanishes; STAR 12 and B1 3 zeros, none shared; no prime zero of the three- or
  five-family union. Non-square composites: the three-family union vanishes only at 105; the five-family union never.
  Joint prime zeros c2 & c3: 53 vs 35.7 predicted; 𝔊* & K: 12 vs 10.4 (not significant after stratification).
* **EVIDENCE (10⁸–10¹³ windows/samples, plus 42 000 rough semiprimes).** All 21 certificate pairs have positive residual
  correlation after local controls at every scale except c2–c3 at 10¹³ (−0.004, within one nominal s.e.); joint low-tail
  ratios 0.88–4.71, > 1 in all but three entries (within noise). Truncated-Euler-product L-value proxies load with the
  same sign on every certificate family. Rough semiprimes reproduce the prime joint law. Nominal z-values, not calibrated
  tests for heavy-tailed counts with fitted residuals. Registered leads (12 band pairs) are attributed to CRT exclusion:
  three tested against the exact local model, the rest Assessment.
* **Verdict: narrowed (scoped negative; statistical, over primes).** No robustly negative full-pair count association was
  observed; pointwise complementarity at primes is **not excluded** for STAR & B1, STAR & I1, B1 & I1, I1 & c2, I1 & c3 (no
  joint prime zero ≤ 4·10⁶). Within one word set certificates and QR are the two Jacobi halves; R_{STAR∪B1∪I1} ≥ 1 is ES₅
  (λ(p) ≤ 3) for p ≡ 1 (8) (DEDEKIND_ES Cor 4.6) — the exact partition does not show QR is the only route to a union
  theorem. Assessment: a union theorem over the menu would need a new exact relation between divisor classes of different
  integers (none known); not a necessity theorem.

## 6. Papers (REREF; second-round cross-model referee; nothing posted — the user decides)

* **`paper/es-count-note`** (`paper/es-count-note.XREFEREE2.md`): **MINOR REVISION**, no GAP or WRONG main theorem; the
  former MAJOR (Akaka priority) "substantially resolved". Required: (1) distinguish Akaka's full count R_II from the
  auxiliary family F his proof counts (the full counts are *not* disjoint: R(p)/2 ≤ R_II(p); the construction is
  disjoint from the line R); (2) "almost-all lower bound on the scale of the known mean of f_II", not a two-sided
  estimate; (3) a sentence splice. All three applied in a94666aa (record in `paper/es-count-note.REVIEW.md` "Round 2");
  the round-2 revision itself was not re-refereed. The historical 65-slice PARI experiment was not regenerated.
* **`paper/es-hc-note`** (`paper/es-hc-note.XREFEREE2.md`): **MINOR REVISION — supplement completion only.** All
  mathematical, attribution and error-handling requests satisfied; every result CORRECT (conditional ones relative to
  their hypotheses; Computation 7.1 as limited evidence, the full 10¹² census not independently rerun). Outstanding,
  **needs the user**: a stable public supplement (URL/DOI, immutable revision, build/run commands, manifest, outputs,
  checksums). Also open: the §7 SHA-256 manifest is described as covering "all these files" but omits
  `paper/es-hc-note.census-rerun.txt`, the census wrapper and `paper/es-hc-note.check.py` — add them or narrow the
  sentence. Not yet done.

## 7. Honest assessment

Wave z57 aimed at pointwise positivity directly and again moved reformulations, averages, censuses and calibrations, not
positivity at a prescribed prime. Durable outputs:
* (MS) with its ladder (SYNTH) — the one-sentence target for ES by the (★) route, with the numerator-8 sub-line as a
  certified screen at threshold 10¹⁰ and a model calibration of what an effective proof would face;
* Theorem W (BFO): 𝔊*-zeros ≪_A x/(log x)^A (B6);
* the defect/hyperbola form and the Jacobi necessity of every hit (BFF), and the 𝔊* census to 10¹² (38 zeros, last
  564 661 441);
* Theorem G (BFII): a log³p genus main term for full Type II, effective, genus part only; the witness barrier and the
  no-finite-covering theorem;
* COMPLEMENT's scoped negative: same-integer positive coupling (Theorem C) and certified pairwise falsifiers; five
  prime pairs remain open as pointwise implications;
* paper referee rounds closed except the HC note's public supplement.

In every lane the missing step is the same: the order-≥3 remainder at one integer (B2), now also for full Type II. No
unconditional theorem guaranteeing positivity at an arbitrary prescribed prime, or at every sufficiently large prime, is
obtained. ES remains OPEN.
