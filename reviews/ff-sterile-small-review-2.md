# R221 — hostile review of FF_STERILE_SMALL.md §5 (O220 checkpoint 2: Theorem 5.2, q = 9)

Reviewer: R221 (side agent, branch side-agent/review-ff-small-2). Scope: §5.1 (exact enumeration, `fz_enum.c`), §5.2
(exact masses), Lemma 5.1 (linearised Lemma 4.1, `fz_tail.c` RANK = 1), Theorem 5.2 (`fz_hybrid.c`, `fz_certify9.sh`,
log `data/fz/certify9.txt`), Case A at q = 9, §5.3 (q = 3 s₀ Assessment), labels. §§1–3 were reviewed by R220; §6 not reviewed.
From-scratch scripts: `scripts/review_fz9_enum.c` (own F₉ model and three factoring-free reconstruction routes, full (B)
check), `review_fz9_compare.py`, `review_fz9_rankin.py` + harness `review_fz9_rkdump.c` (Lemma 5.1 constants),
`review_fz9_sum.c` (finite bound sum with OWN Lemma 4.1 on R220's independent route code, optional exact counts),
`review_fz9_tail.c` (tail with OWN linearised Lemma 4.1 on R220's independent tail code). Logs `data/fz/review_r221_*`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| §5.1 completeness of fz_enum's eight routes (incl. the factoring routes M11–M16) | **SOUND** (proved below; pattern-by-pattern agreement with my independent enumerator for all patterns s ≤ 17 [s = 18: see §1]) |
| §5.2 exact masses (per level, Σ_{s≤18} = 0.592177, Σ_{s≤22} = 0.592201) | **SOUND** (s ≤ 17 independently reproduced exactly; s = 18–22 from the author's files, cross-checked only for consistency, see m-2) |
| Lemma 5.1 (linearised Lemma 4.1) and its implementation in fz_tail (RANK = 1) | **SOUND** |
| Hybrid splice (exact s ≤ 22, bounds 23 ≤ s ≤ 80, tail s > 80) | **SOUND** (no double counting, no omitted pattern) |
| Case A at q = 9 (0.17501 + 1.1·10⁻⁵) | **SOUND** |
| Theorem 5.2 (certified total ≤ 3.58 < 8) and its corollaries | **SOUND-AFTER-REPAIRS** (minor: documentation of the regeneration command and of what is independently verified) |
| §5.3 s₀ ≈ 80–85 at q = 3 (Assessment) | (see §6) |
| Labels (Conjecture 0.2 not claimed; ES not claimed) | **SOUND** |

No FATAL, no MAJOR so far.

## 1. §5.1 — exact enumeration (`fz_enum.c`): completeness

**Identities (re-derived).** With L' = m'g', E = L'w − 1, E' = L'C − 1 and (B): EE' = L'²wC − L'(w + C) + 1 =
L'g'(T^s + v) − L'g'v + 1 = **1 + T^s m'g'²** (L'²/m' = L'g'); C·E = L'wC − C = g'(T^s + v) − C = **g'T^s + w**, so (÷T)
**E·C₁ = g'T^{s−1} + w₁**; and from w₁ + C₁ = Tg'v₁: m'w₁(Tg'v₁ − w₁) = T^{s−2} + v₁, i.e. **v₁(Tm'w₁g' − 1) = v₁E =
T^{s−2} + m'w₁²**. E is monic (L', w monic, deg ≥ 1), E + 1 = Tm'g'w₁, so E ≡ −1 modulo Tm'g', Tw₁g', Tm'w₁ (the
pre-filters of modes 2, 3, 4 are necessary conditions). deg E = a + y + z.

**Route-by-route.** Each route enumerates data that every tuple of the pattern possesses, and the data determine the tuple:
* M2: C₁ (all monic, deg b − 1, C₁(0) ≠ 0); deg C₁ = b − 1 ≥ t − 1 > t − 2 so v₁ = −(T^{s−2} mod C₁) (Lemma 1.1); then either
  m' over all monic divisors-candidates of degree z (exact division test) or w₁ = σ + Tv₁h with deg h = a − t and
  lc(h) = lc(v₁)⁻¹ (so w₁ is monic), or w₁ = σ when a − 1 < t − 1. Complete.
* M3: w₁; v₁ = r₀ + w₁h over all h of degree t − 2 − (a − 1) with lc(h) = LC (or v₁ = r₀ if negative); then m' or
  C₁ = σ + Tv₁k, deg k = b − t = y, lc(k) = LC⁻¹. Complete.
* M5: (m', v₁ in its class, g'); w₁, C₁ are the roots of X² − SX + G, S = Tg'v₁, G = (T^{s−2} + v₁)/m'; discriminant
  S² − 4G; `psqrt` determines a square root top-down from a fixed root of the leading coefficient and verifies R² = D, and
  any square root of D equals ±R, so both roots (S ± R)/2 are tried (once if R = 0). Complete (char 3: 2 invertible).
* M11 (w₁ | G), M16 (C₁ | m'C₁), M12 (E | 1 + T^s m'g'²), M13 (E | g'T^{s−1} + w₁), M14 (E | T^{s−2} + m'w₁²): the
  identities above; reconstructions w = (E + 1)/L', C = (g'T^s + w)/E (M12); L' = (E + 1)/(Tw₁), m' = L'/g', C₁ = F/E (M13);
  v₁ = F/E, C₁ = (T^{s−2} + v₁)/(m'w₁) (M14). All are exact for a true tuple.
* Divisor enumeration (`dfs`): each exponent vector is visited along a unique prefix; the callback fires at the first prefix
  reaching the target degree and does not extend it, and every factor has degree ≥ 1, so each monic divisor of the target
  degree is produced exactly once. With a correct complete factorisation this is all divisors. The factorisation is
  checked fail-closed: product = input, factors monic, pairwise distinct, irreducible by Rabin's test (correct form:
  gcd(X^{q^{d/p}} − X, f) = 1 for every prime p | d and X^{q^d} ≡ X mod f) — a deterministic certificate, so a wrong
  factorisation cannot silently lose divisors.
* `check()` tests degrees, monicity, nonzero constant terms of m', w₁, C₁, g', exact lc of v₁, m'w₁C₁ = T^{s−2} + v₁ and
  Tv₁ | w₁ + C₁ with quotient g' monic of degree y, g'(0) ≠ 0 — equivalent to (B) for the pattern via FF_STERILE_PUSH
  Lemma 1.1(iii). Each tuple is found at most once per route (distinct enumeration keys/divisors give distinct data).
**Verdict: complete and exact.** Counting convention (ordered tuples with deg w = a ≤ b = deg C, both orders when a = b,
mult 2 for a < b) matches (Σ) by the w ↔ C symmetry of (B).

**Independent re-enumeration (`review_fz9_enum.c`).** Own F₉ model F₃[α]/(α² − α − 1) (fz_enum uses i² = −1; field
axioms checked), own polynomial code, three factoring-free routes: P ((m', w₁) → v₁ ≡ −T^{s−2} mod m'w₁ → C₁ = (T^{s−2} div
m'w₁) + h), Q ((m', w₁, g') → v₁ = (T^{s−2} + m'w₁²)/(Tm'w₁g' − 1)), R ((w₁, v₁ in class mod w₁, g') → C₁ = Tg'v₁ − w₁,
m' = (T^{s−2} + v₁)/(w₁C₁)); every candidate checked against (B) itself (w, C, v rebuilt; T ∥ w, T ∥ C, T ∤ m'g'). Self-checks:
P = Q = R on every pattern, also without fixing lc(v₁) (q = 3, 5, 7, 9; s ≤ 10). **Result: all 3 + … + 648 patterns of
3 ≤ s ≤ 18 agree with `data/fz/enum9/e_<s>.txt.gz` count for count (0 mismatches;
`data/fz/review_r221_enum9_3_18.txt`).** Per-level masses agree with §5.2 to all printed digits; Σ_{s≤18} = 0.5921770
(text: 0.592177). (s = 19, 20: see §1b.)

## 2. Lemma 5.1 (linearised Lemma 4.1) and `fz_tail.c` RANK = 1

**Proof from scratch.** V_ρ(n) = ∫₀ⁿ r(x) dx where r(x) is the ratio (gain/weight) of the item occupying position x after
sorting all items (P, e) by decreasing ratio (multiplicities I'(j)); r is non-increasing, so V_ρ is concave with V_ρ(0) = 0.
For a concave function, f(n) ≤ f(n₀) + λ(n − n₀) for every n ≥ 0 and every λ ∈ [f'₊(n₀), f'₋(n₀)] (for n > n₀ by f'₊,
for n < n₀ because λ ≤ f'₋). With F of degree n ≤ sN, T ∤ F, and d' = min(d, n − d) ≤ s·min(D, E):
#div ≤ ρ^{−d'}e^{V_ρ(n)} ≤ exp(s(−log ρ·min(D, E) + λ(D + E)) + c) with c = V_ρ(n₀) − λn₀ ≥ 0 (concavity), and c ≤ s·c/S
for s ≥ S. Increasing in D, E since −log ρ ≥ 0, λ ≥ 0. **SOUND.** (The exactness of the item set matters: the
linearisation is used for all n at once, so — unlike the per-n V of fz_sum — the item set may not be truncated at n.)

**Implementation (`init_rankin`).** Items j ≤ NM = 8S + 8 = 648, e·j ≤ NM, gains < 10⁻¹⁸ dropped; λ := ratio of the next
item after filling n₀, then λ(1 + 10⁻⁹) + 10⁻¹⁵, V(n₀)(1 + 10⁻⁹) + 10⁻⁹ + 10⁻¹²n₀. Omitted items have ratio
≤ min(1/(je), ρ^{je}/j) — gain log(1 + y^e/S_{e−1}(y)) ≤ min(1/e, y^e) — so they are harmless iff they lie below λ; the code
does not test this, but my check does it externally:
*`review_fz9_rankin.py` (own Möbius count, own item list with j up to J chosen adaptively so that the omitted-degree bound
min(ρ^j, log 2)/j < λ_true/2, e-cut certified by min(1/(4S), ρ^{4S}) < λ_true):* for all 96 (ρ, n₀) pairs used at q = 9,
S = 80 (dumped from the unmodified fz_tail.c by the harness `review_fz9_rkdump.c`): c_author ≥ V_true(n₀) − λ_true n₀
and λ_author ≥ λ_true: **0 violations** (also q = 3). Brute force over all factorisation types (q = 9, n ≤ 5; q = 3,
n ≤ 10), every d: max count / linearised bound = 0.72 resp. 0.91. **SOUND.**

**Independent tail (`review_fz9_tail.c`):** R220's independent tail code (`review_fz_tail.c`, not derived from fz_tail)
plus my own linearised Lemma 4.1 (ρ ∈ {k/32}, n₀ ∈ {S/2, …, 8S}, items to weight 20 000, λ > omitted bound enforced, exit
otherwise) in every binomial divisor count, plus the R1 alternative m' | F, w₁ | F/m'. q = 9, S = 80, depth 8:
**tail(s > 80) ≤ 0.0703** (author 0.0797). Without Lemma 4.1 the same code gives 9.1·10⁷: the q = 9 tail depends on
Lemma 5.1, which is correct. Every F to which Lemma 4.1 is applied is prime to T (1 + T^s m'g'², g'T^{s−1} + w₁,
T^{s−2} + m'w₁², T^{s−2} + v₁ and its cofactors m'C₁, w₁C₁, m'w₁ … — v₁(0), w₁(0), C₁(0), m'(0) ≠ 0). The box logic
(pattern counts (sw + 1)³, class conditions uniform in s ≥ S, b ≥ a, t ≥ 0 pruning) is unchanged from the version R220
reviewed at q = 27.

## 3. Hybrid splice (`fz_hybrid.c`) and the finite bound part 23 ≤ s ≤ 80

* Pattern set: a ≥ 1, z ≥ 0, b = s − a − z ≥ a, 0 ≤ y ≤ b − 2, t = b − y (≥ 2) — exactly the patterns of (B) by
  FF_STERILE_PUSH Lemma 1.1(ii),(iii); identical loop to fz_sum. Weight mult·q^{1−⌈s/2⌉} ((s + 1)/2 integer division).
* Per pattern either the exact count (if the level file has a line for it) or the route bound — never both; levels
  3 ≤ s ≤ 80 in the finite part, s > 80 in the tail: no overlap, no gap. A file with a wrong line count aborts; a missing or
  duplicated pattern line could at worst fall back to the (valid) bound for that pattern — fail-safe. No SKIP lines in the
  shipped files (checked). **No double counting, no omitted patterns.**
* Route bounds at 23 ≤ s ≤ 80 use Lemma 4.1 per n (`lD`): fz_sum truncates items at e·j ≤ 2048 and n ≤ 2048, which is a valid
  relaxation for each fixed n (an integer solution only uses items with e·deg P ≤ n). Independent re-computation
  (`review_fz9_sum.c` = R220's independent route code + my own per-n Lemma 4.1, ρ ∈ {k/48}, items e·j ≤ n): with the author's
  exact counts for s ≤ 22, finite part **3.6670** (author 3.2872; mine is weaker: no τ-bound, coarser ρ grid). Exact count ≤
  my route bound on every pattern s ≤ 22 (0 violations). Pure bound sum s ≤ 80: 42.76 (author's fz_sum: 41.87).
* Sensitivity (mine): exact ≤ 18 → finite 7.98 (fails together with tail and Case A: 8.22 > 8), exact ≤ 19 → 7.25,
  ≤ 20 → 5.39, ≤ 21 → 4.90, ≤ 22 → 3.67. So with my weaker bounds the certificate needs exact counts through s ≥ 19
  (with the author's bounds through 18: 4.735, as stated). Hence the independent re-enumeration of s = 19, 20 (§1b).

## 4. Case A at q = 9

R218's author-independent `review_fs2_caseA.py` at q = 9: Σ_{α≤40} = 0.17500159866 (fz_caseA: 0.17500159866); with α ≤ 60:
0.17500159876. Lemma 2.1 tail: direct summation Σ_{41≤α≤400} (α+1)³9^{−(α+1)/2}3^{α/2} = 1.0707·10⁻⁵ ≤ 1.0749·10⁻⁵ (script's
geometric majorant, ratio (44/43)³/√3 < 1). Weight q^{2−k−α} = 9^{−α} at k = 2. **SOUND.**
