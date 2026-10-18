# BOARD2_SLATE — O273: the board #2 compatible slate

Source: board memo `/home/pasky/.pi/boards/20261018-es-lowertail/memo.md` (finalists 1–4) and the items/rounds/rulings it
cites. None of these items is single-prime lower-tail progress (the board's unanimous bottom line); this file records the
cheap, compatible results with honest labels. ES is not solved.

## (1) Finalist 4 — ABH attribution for λ(p) (DONE; KNOWN)

* Read ABH arXiv:2210.14095v2 myself: Thm 1 (concentration of S(a/N) at (12/π²) log N log log N, window t log N,
  proportion ≪ 1/t, single fixed N), Thm 6 (|D(a/N)| ≥ t log N with proportion ≪ 1/t), identity (5)
  D = −S_alt/12 + O(1) (Barkan/Hickerson). Conventions: a/N = [0; a₁, …, a_r], a_r > 1 — same as ZAREMBA_TRANSFER's c_i.
* Transfer re-derived: Σ_{j even} c_j = (S + S_alt)/2 ≤ (6/π²) L log L + O(L) off a set of proportion < 1/2, which
  therefore contains a QNR; with r(p/A) ≤ 1 + Σ_{j even} c_j(A/p) this gives **λ(p) ≤ (6/π²) log p log log p + O(log p)**.
  Status: **KNOWN (corollary of ABH 2022)**; the campaign's Theorem A (constant 10) is a weaker special case.
* Numerics (EVIDENCE, `scripts/z42_abh_check.py`): the HJ formula holds as r = 1 + Σ_even − δ, δ ∈ {0, 1};
  |S_alt + 12D| ≤ 3; median r over QNR tracks (6/π²)L log L + O(L).
* Argon's "convergent Legendre invariant" (a/p) = ((−1)^i q_iρ_i/p): a one-line consequence of the standard convergent
  congruence; same genus-character fact as DEDEKIND_ES Thm 4.5. Recorded, **not new**.
* Written into `ZAREMBA_TRANSFER.md` §2 directly after Theorem A (existing text kept).

## (2) Finalist 1 — moving-window cap-0 witness corollary (DONE; FORCED_WINDOW §8)

* **Theorem 8.5 (PROVED modulo Henriot 2014 erratum New Thm 5 + Siegel–Walfisz + Mertens; ineffective).** For 0 < α < 1/6,
  all but O(X/L^{4/3−2α−ε}) primes p ≡ 1 (8) in (X, 2X] have Σ_{χ≠1}|A_χ(K_q)| < 1, hence an honest Type II solution
  with window q, at **every** prime q ≡ 3 (8) in [L^α, 2L^α] (forcedness is not needed — the certificate is target-free).
* Henriot's statement was checked from the source: the 2014 erratum (now `sources/henriot-erratum-2014.pdf`) is read, and
  New Theorem 5 is applied with Q₁ = t, Q₂ = 4t − q, F = f(n₁)·1[P⁻(n₂) > √x] ∈ M₂(1, 1, ε); local factors computed exactly.
* Value: dominated (fixed q = 3 alone gives ≪ X/L^{3/2} exceptions; Vaughan; 3/4 chain). New only in shape. Priority:
  nothing found in a limited search (Elsholtz–Tao Thm 1.8 is the fixed-window analogue).
* EVIDENCE: `scripts/z42_window_cert.py`, 990 windows at p ≈ 10⁶: certificate ⇒ explicit solution, 0 violations.

## (3) Finalist 3 — the five-slice union R_III^int and its T1-exact main term

Scripts: `scripts/z42_five_slice.c` (per-n exact count, main term, checks), `scripts/z42_five_slice_fit.py`; logs
`logs/z42_five_slice_1e6.txt` (491 primes ≡ 1 (4) in [10⁶, 1.04·10⁶) — every third of the 1 473 such primes (R284 repair)), `logs/z42_five_slice_ladder.txt` (30 primes, 10⁴–10⁸).

**Setting.** n ≡ 1 (mod 4). Interior pairs P(n) := {(u, v) ordered : u, v ≥ 2, gcd(u, v) = 1, 2uv − u − v ≤ n}. For
(u, v) ∈ P(n) write uv = 2^k w (w odd), a := −(u + v), and, at a hit uv | n + u + v, t := (n + u + v)/(uv) ≥ 2.
`R(n) := #{(u, v) ∈ P(n) : uv | n + u + v, (uv/n) = −1}` (Jacobi symbol).

**Lemma 3.1 (R = N₋ of DEDEKIND_ES Thm 4.5 at primes; PROVED).** Ordered pairs at hits ↔ length-3 words
n/A = [[v, t, u]], A = tu − 1, n = tuv − u − v. If gcd(uv, n) = 1 then (A/n) = (uv/n). Hence **for n = p prime**
R(p) = #{interior five-slice words} = N₋(p). For composite n, R(n) is only the subfamily with gcd(u, v) = 1 = gcd(uv, n)
(review repair: 21/8 = [[3, 3, 3]] is an interior five-slice word, N₋(21) = 1, but (3, 3) ∉ P(21) and R(21) = 0).
*Proof.* (tu − 1)v = n + u ≡ u (mod n), so (A/n)(v/n) = (u/n), and (v/n)² = 1. The word ↔ pair correspondence is
DEDEKIND_ES §4 / ZAREMBA_TRANSFER Lemma C. ∎ (For n = p prime, gcd(uv, p) = 1 and gcd(u, v) = 1 are automatic.)

**Lemma 3.2 (the sign at a hit is forced; PROVED, reciprocity).** At a hit, (uv/n) = ε_{u,v}(n) := (2/n)^k (a/w), and
* odd–odd (k = 0): ε = (−1/u)(−1/v)(−1)^{(u−1)(v−1)/4}, i.e. ε = −1 ⟺ (u, v) ≢ (1, 1) (mod 4) — p-free;
* u = 2^k u′ (k ≥ 1), v odd: ε = (2/n)^k (−1/u′)(−1/v)(2/v)^k (−1)^{(u′−1)(v−1)/4} — depends on n mod 8, u′ mod 4, v mod 8;
* **k ≥ 2: if 2^k | n + u + v then ε = −1 automatically** (and v ≡ 3 (4)).
*Proof.* n ≡ a (mod w) and n ≡ 1 (4) give (uv/n) = (2/n)^k (w/n) = (2/n)^k (n/w) = (2/n)^k (a/w). For u = 2^k u′:
(a/u′) = (−v/u′), (a/v) = (−2^k u′/v); multiply and apply Jacobi reciprocity to (v/u′)(u′/v). Odd–odd is the same with
k = 0. For k ≥ 2, 4 | n + u + v forces v ≡ 3 (4), so (−1/v) = −1 and (−1)^{(u′−1)(v−1)/4} = (−1/u′), giving
ε = −(2/n)^k (2/v)^k; for k even this is −1; for k ≥ 3 odd, n ≡ −v (mod 8) so (2/n) = (2/v) and again ε = −1. ∎
(This is BM_CORRECTED Prop 4.1(b)'s identity χ_{−4xy}(−(4x + y)) = −1 in other coordinates. EVIDENCE: `violeps = 0`,
`autoviol = 0`, `viol45 = 0` at all 491 + 30 primes and the test squares — the formula for ε at every hit, automatic
activation for k ≥ 2 at every 2-adically compatible pair, and Thm 4.5's five conditions ⟺ (uv/n) = −1 at every hit.)

**Definition (T1-exact BM-type main term).** Call (u, v) *active at n* if 2^k | n + u + v and ε_{u,v}(n) = −1. Put
`M(n) := Σ_{(u,v) ∈ P(n), gcd(n, uv) = 1, active} c_{u,v}(n),   c = (1 − (uv/n))/φ(w) if w ≠ □,   c = 1/φ(w) if w = □.`
Equivalently M = Σ 1[2^k | n+u+v]·φ(w)^{−1}(1 + [w ≠ □](n/w)(a/w))·(1 − (uv/n))/2: the orthogonality expansion of
1[n ≡ a (w)] truncated to {principal, Jacobi character (·/w)} (only the principal one when (·/w) is principal), times the
five-slice projector; for non-active pairs this product vanishes identically.
**The three sustained repairs are built in:** (a) gcd(n, uv) = 1 (fable ruling (a): n = 2401, (3, 7) now contributes 0);
(b) square odd part ⇒ principal only (ruling (b): p = 61, (2, 9): w = 9, active since (2/61)(−11/9) = −1, term 1/φ(9) =
1/6, the hit density, not 1/3); (c) opposite-parity activation recomputed from Lemma 3.2 rather than identified with 2·M_BM.

**Proposition 3.3 (PROVED; for composite n it concerns the coprime subfamily R).** (a) M(n) ≥ 0; each term is 0, 2/φ(w) or 1/φ(w). (b) **T1:** M(m²) = 0 for every odd m
(gcd(m, uv) = 1 gives (uv/m²) = 1, so non-square-w terms vanish; for w = □, (a/w) = 1 and (2/m²) = 1 give ε = +1, inactive).
(c) Mean-preserving: for fixed (u, v) and fixed n mod 2^{max(k,3)}, the average of the term over the reduced classes n mod w
equals 1[active]/φ(w), the density of the hits that R counts. ∎ EVIDENCE: M = R = 0 at 49², 99², 105², 997² (M₀ ≠ 0 there:
13.65, 10.64, 5.00, 82.4 — the principal part alone fails T1, as argon/astra said).

**Proposition 3.4 (the principal density; Assessment = standard Dirichlet-series computation, + EVIDENCE fit).** Let
M₀(n) := Σ_{active, gcd(n, uv) = 1} 1/φ(w) (as implemented; at primes the gcd condition is void, and M₀(p) depends on p only
through its size and p mod 2^k). Averaged over primes p ≡ 1 (4) the per-pair
weights (relative to 1/φ(u′)φ(v)) are: odd–odd 1 on the three good classes; k = 1: 1/2 (half the n mod 8);
k = 2: 1[v ≡ 3 (4)]; k ≥ 3: 1[v ≡ 3 (4)]·2^{2−k}. With Σ_{m ≤ x odd} 2^{ω(m)}/φ(m) ∼ (3/(2π²)) log² x this gives
`M₀ ∼ [ 9/(8π²) (odd–odd) + 3/(2π²) (k = 1) + 3/(2π²) (k = 2) + 3/(2π²) (k ≥ 3) ] L² = (45/(8π²)) L² ≈ 0.570 L²`
(ordered pairs; each even sector counts both orientations). Fit a L² + b L + c over 10⁴…10⁸ (6 primes per decade):
odd–odd a = 0.1140 (pred. 0.1140), k = 1: 0.1519, k = 2: 0.1519 (pred. 0.1520), k ≥ 3: 0.118 with a positive L-term
(slow: cutoff p/2^{k+1} and p mod 2^k fluctuation). **Correction to the board:** the opposite-parity sector is
3 × (3/(2π²)) L², not 2 × — the k ≥ 2 sectors are automatically active (Lemma 3.2). So fable's principal 33/(8π²) is wrong;
the correct principal constant is **45/(8π²)**. Ruling (c)'s suspicion was right; 9/(8π²) for ordered odd–odd stands.
(R284 repair: the asymptotic M₀(p) ∼ (45/(8π²))L² holds for *each* prime p ≡ 1 (4), not only on average — in every
sector the active classes have the stated density for each fixed p mod 2^k; only lower-order terms depend on p mod 2^k,
e.g. the k = 1 sector is 24.08 at p ≡ 1 (8) vs 27.60 at p ≡ 5 (8) near 10⁶. This per-p form is what Thm 3.5's "¼ of the
principal constant" comparison uses.)

**Theorem 3.5 (unconditional lower bound; PROVED, Burgess).** For primes p ≡ 1 (4), L = log p:
`M(p) ≥ (45/(32π²) − o(1)) L² ≈ 0.142 L²`  (Burgess);   `M(p) ≥ (15/(64π²) − o(1)) L² ≈ 0.024 L²`  (Pólya–Vinogradov).
*Template lemma.* Let χ = (·/p), β ∈ {1/2, 1/4 + ε}, X = p^δ (δ ≤ 1/2). Suppose for each odd u′ ≤ X we are given a set
S_{u′} of v that is a union of classes mod 2^j (j fixed) of density D (among all integers), and a sign σ_{u′}. Then
`Σ_{u′ ≤ X odd} (1/u′) Σ_{v ≤ p/(c u′), v ∈ S_{u′}, (v,u′)=1} (1 − σ_{u′}χ(v))/v ≥ D (L²/π²)(4δ − 2δ² − 6βδ) − O(L)`.
*Proof.* As BM_CORRECTED Thm 2.2, with one change: the class restriction is carried *inside* the Burgess bound. By
Möbius over d | u′ the main part is ≥ D(φ(u′)/u′) log(p/(cu′)) − O(κ(u′)). For the character part, each inner sum is
Σ_{m ≤ T, m ∈ S′} χ(m)/m with S′ a union of classes mod 2^j of density D. Split at T₀ = 2^j p^{1/4+ε}. The initial segment
is ≤ Σ_{m ≤ T₀, m ∈ S′} 1/m = D log T₀ + O(1). The tail uses Σ_{m ≤ s, m ≡ c (2^j)} χ(m) = χ(2^j) Σ_{i ∈ I} χ(i + c′)
with I an interval of length ≍ s/2^j. Burgess (prime modulus, any interval) gives ≪ s p^{−η} for s ≥ T₀, so the tail is
o(1) after partial summation. (κ(u′) := Σ_{d|u′} |μ(d)|/d = ∏_{ℓ|u′}(1 + 1/ℓ); the O(1) in the initial segment is O(2^j),
hence O_K(1) — the reason K is fixed before p → ∞. R284 repair.) Hence the bound is κ(u′)(D β L + O(1)), β = 1/4 + ε. With PV, β = 1/2 and T₀ = √p L².
Then use Σ_{u′ odd ≤ X} φ(u′)/u′² = (4/π²) log X + O(1), Σ φ(u′) log u′/u′² = (2/π²) log² X + O(log X) and
Σ κ(u′)/u′ = (6/π²) log X + O(1). The same holds with u′ restricted to a class mod 4 (halve each constant). ∎
*Families (pairwise disjoint subsets of P(p); every term is ≥ 0, and c_{u,v} ≥ (1 − χ(uv))/(u′v), except for w = □
pairs at p ≡ 5 (8), whose total is O(1)):*
* even sectors, u′ ≤ √p short, v long (both orientations (2^k u′, v) and (v, 2^k u′), disjoint by parity), v ≤ p/(2^{k+1}u′):
  k = 1 with S = the two active classes of v mod 8 (D = 1/4); k = 2 with v ≡ 3 (4) (D = 1/4); k ≥ 3 with v ≡ −p (mod 2^k)
  (D = 2^{−k}, Σ_{k≥3} = 1/4; prove the bound for fixed K and ε, let p → ∞, then K → ∞ and ε ↓ 0). Each of the three
  sectors × 2 orientations gives
  (1/4)(3/4)/π² = 3/(16π²) at δ = 1/2, β → 1/4. Total 18/(16π²).
* odd–odd, one orientation, u ≤ √p short, v ≤ p/(2u): for u ≡ 1 (4), v ≡ 3 (4) (D = 1/4); for u ≡ 3 (4), all odd v
  (D = 1/2). Total (1/4 + 1/2)·(1/2)·(3/4)/π² = 9/(32π²).
Sum: 36/(32π²) + 9/(32π²) = 45/(32π²). PV: the template factor max_{δ≤1/2}(δ − 2δ²) = 1/8 replaces 3/4, i.e. 1/6 of the
Burgess value. ∎ *(Review repairs: the families must exclude u′-short pairs with v = 1 and odd–odd pairs with u or v = 1
(not in P(p)); deleting them costs O_K(L). With PV, T₀ = √p L² leaves an extra O(log L) per harmonic sum, so the template
remainder is O(L log L) — leading constants unchanged.)*
*Check of the template main part (EVIDENCE):* Σ_{u′ odd ≤ √p} Σ_{v ≡ 3 (4), v ≤ p/(8u′), (v,u′)=1} 1/(u′v) = 7.34 / 10.03 at
p = 1 000 033 / 10 000 121, against (1/4)(3/2)L²/π² = 7.25 / 9.87.
*Comparison.* Argon's 33/(64π²) ≈ 0.052 rested on the unverified 2·M_BM identification; astra's 9/(64π²) (unordered good
odd–odd) is consistent with our odd–odd family, but the Burgess saving here is larger. The class restriction is put inside
the initial segment, where the trivial bound scales with the density D; this is the only new device. The theorem gives
1/4 of the principal constant, versus 1/8 for M_BM in BM_CORRECTED Thm 2.2. It concerns the **main term only**. It
does not give R(p) > 0: as in BM_CORRECTED §3, the remainder can be ≥ M i.o. (Linnik-type), and B3 is untouched.

**Numerics (EVIDENCE).**
* 491 primes p ≡ 1 (4) in [10⁶, 1.04·10⁶) (every third; R284's independent count over all 1 473 gives mean R/L² = 0.470,
  min R = 26 — R284 repair): mean R/L² = 0.472, mean M/L² = 0.450, mean M₀/L² = 0.450; min R = 26,
  min R/M = 0.35, corr(R, M) = 0.44; mean (R − M)²/(2M) = 2.3 (R counts ordered pairs, so Poisson-in-unordered would give 1:
  overdispersed ≈ 2.3×, like (★)). **The board's "≈ 0.39 L² at 10⁶" is not reproduced; we measure ≈ 0.47 L² (ordered,
  u, v ≥ 2).** Fable's decomposition "2R-part 0.30 + odd–odd 0.088" assumed the 2·M_BM identification, which is wrong; our odd–odd
  part is 0.084 L² (M₀ odd–odd 16.0 at 10⁶) and the opposite-parity part ≈ 0.36 L².
* Ladder 10⁴ … 10⁸ (6 primes per decade): mean M/L² = 0.41, 0.44, 0.44, 0.48, 0.47; mean R/L² = 0.44, 0.39, 0.45, 0.45, 0.45.
* T1: R = M = 0 at 49², 99², 105², 997².
* k = 4 vs k = 8 at 131 and 241: R(241) = 6 interior five-slice words (ordered) and 4/241 has 8 solutions; 8/131 and 8/241
  have **no** solution at all (brute force, all x ≤ y ≤ z). Of the interior hits, 0 meet the 8-adic analogue
  (8 | t, 8 | u, 8 | v, 8 | tu − 1 or 8 | tv − 1). p = 131 ≡ 3 (4) lies outside Thm 4.5's range (classical case). There
  R = 2 and the five-condition count is 6; the k = 8 separation is the trivial one (8/131 has no solution).
* Zeros: HJ_DEEP (S) concerns N₋(n), which for composite n is larger than our coprime R(n) (Lemma 3.1); at primes it gives
  R(p) = N₋(p) > 0 for all primes 5 < p < 10⁸. Here min R = 26 on the 10⁶ sample.

**Labels.** Lemma 3.1, 3.2, Prop 3.3, Thm 3.5: PROVED (Thm 3.5 uses Burgess; o(1) ineffective in practice like
BM_CORRECTED's). Prop 3.4's constant: Assessment (Dirichlet-series sketch) + EVIDENCE fit. Under GRH M ∼ M₀ by the argument
of BM_CORRECTED Prop 2.3 (not re-derived here: Assessment). Value: bookkeeping on an existing object, not a lower-tail
mechanism (the board's verdict stands). The k ≥ 2 automatic activation explains why the five-slice union has a 3.75× larger
principal constant than (★) (45/(8π²) vs 3/(2π²)).

## (4) Finalist 2 — far lower-tail diagnostic on the 8/n c = 1 line to 10⁹ (EVIDENCE; across-n, B6 steering only)

Scripts: `scripts/z42_zero_law.c` (modes `mark`, `exact`, `proxy`, `check`), `scripts/z42_zero_law_fit.py`. Logs:
`logs/z42_zero_law_m8_1e9.txt` (bin table + fit), `logs/z42_zero_law_m8_zeros_M26.txt` (the 1 423 identified zeros with exact M ≥ 26:
n, M, M₀), `logs/z42_zero_law_m12_m16_1e7.txt`. Large intermediates (2.75·10⁶ zero list, zero proxies) stayed in a tempdir; regeneration recipe and the exact-M and
population inputs of the fit: `logs/z42_zero_law_RECIPE.md`, `logs/z42_zero_law_m8_{exact_zeros,exact_pop,pop_proxy}.txt.gz`.

**Object.** Line m·uBC = n + u + B (C ≥ 1, gcd(u, B) = 1, u + B odd, n odd), R*_m(n) = #{ordered (u, B) : muB | n + u + B,
muB − u − B ≤ n} (a hit gives m/n = 1/(uBC) + 1/(nBC) + 1/(nuC)). Main term (BM_CORRECTED Prop 4.1(c)):
`M_m(n) = Σ_{pairs, gcd(n, muB) = 1, −(u+B) ∈ (ℤ/muB)^*} (1 − (−uB/n))/φ(muB)` — mean-preserving, 0 at squares.
**The three sustained patches.** (a) AP cutoff muB − u − B ≤ N (the marking loop and the pair set use it; astra's
m = 8, N = 13, (1, 2, 1) is a hit). (b) m = 12: exact φ(12m′) = 8φ(m′) (3 ∤ m′) or 12φ(m′) (3 | m′). Pairs with 3 ∤ uB and
3 | u + B have a non-unit target and are dropped; for m′ = uB ≢ 0 (3) this happens for every splitting iff m′ ≡ 2 (3).
Only n prime to 6 are used. (c) m = 16 (and m = 12) are sub-sampled at 10⁷ only.
**Self-tests.** `check` mode compares brute force over all pairs with the fast code for every admissible n ≤ 3000, m = 8, 12, 16:
0 mismatches in the zero flag and in M, M₀; squares give R* = M = 0. For m = 8, `exact` agrees with BM_CORRECTED's
`z38_mbm.c` (K = 8) to print precision.

**Method and cost.** (1) Marking all odd n ≤ 10⁹ in a bitset (63 MB) took 55 s. It found 2 748 892 zeros among
499 984 188 odd non-squares. (2) A cheap proxy was computed for every zero n ≥ 10⁶ and for 40 000 random admissible n in
[5·10⁸, 10⁹]. The proxy is the exact sum over m′ ≤ 5·10⁴ plus a principal tail with a coprimality factor. It selects the
zeros that get an exact M, and (as proxy + 0.52) it also bins the population sample and the low-M zeros (review
repair: not "only stratification"). (3) The exact M_8 was computed (≈ 0.9 s each at 10⁹) for **every** zero whose proxy could
reach M ≥ 22–26: all zeros in [5·10⁸, 10⁹] with proxy ≥ 22, and all zeros below with proxy ≥ 24, 3 359 in total. It was
also computed for 300 random population members (calibration). Calibration: exact − proxy has median 0.52, rms deviation
0.24 and max deviation 0.58 on the population; median 0.48 and rms 0.27 on the zeros. On this calibration a zero with
M ≥ 26 below the thresholds would need a proxy error ≈ 3–4× the largest observed; this is empirical, not a
deterministic bound, so exhaustiveness is not established (review repair). Total ≈ 2 CPU-hours on ≤ 2 cores, ≤ 1 GB per process, `ulimit -v 4000000`.

**Drop-condition (a): passed.** Zeros with exact M_8 ≥ 26 among odd non-squares ≤ 10⁹: **at least 1 423** identified
(874 in [5·10⁸, 10⁹], 546 in [10⁸, 5·10⁸), 3 below 10⁸; probably all of them, see the calibration caveat). 345 are prime. The largest is n = 575 068 511, M = 34.19.

**Conditional zero law** (window n ∈ [5·10⁸, 10⁹], 2.49995·10⁸ admissible n; P = Z_bin/(N·f_bin), f_bin from the
40 000-sample; M = exact where computed, otherwise proxy + 0.52):

| M bin | zeros | P(0 \| M) | P / E[e^{−M/2} \| bin] |
|---|---|---|---|
| [10, 12) | 144 083 | 7.2·10⁻³ | 1.8 |
| [12, 14) | 137 776 | 3.5·10⁻³ | 2.1 |
| [14, 16) | 10 660 | 1.8·10⁻³ | 2.8 |
| [16, 18) | 5 928 | 7.1·10⁻⁴ | 3.5 |
| [18, 20) | 6 320 | 3.1·10⁻⁴ | 4.1 |
| [20, 22) | 1 780 | 1.7·10⁻⁴ | 6.1 |
| [22, 24) | 934 | 8.5·10⁻⁵ | 7.4 |
| [24, 26) | 560 | 3.7·10⁻⁵ | 9.9 |
| [26, 28) | 395 | 1.8·10⁻⁵ | 13.4 |
| [28, 30) | 425 | 8.3·10⁻⁶ | 16.5 |
| [30, 32) | 51 | 2.7·10⁻⁶ | 11 (± 14 %) |

**Fit.** −log P(0 | M) = A·M^β on M ∈ [10, 30] (10 bins; weights (log P)²/rel², the correct variance of log(−log P) —
review repair of the first version's 1/rel²): **β = 0.884**, A = 0.59. The fit is poor (χ² = 23.7 on 8 dof); the χ²-scaled
statistical SE is 0.006 (not meaningful here: R284's refit of the same table with bin midpoints gives β = 0.896, left edges
0.843, sub-ranges [16,30] 0.877, [20,30] 0.924 — R284 repair), but the systematics (proxy binning of the low-M population, heterogeneity, bin choice) are not
quantified and are clearly larger — the spread of local β suggests ± 0.1. The local
β between consecutive top bins is 0.84 and 1.05. The linear slope d log P/dM is −0.38 (Poisson: −0.50). The excess over
swap-Poisson grows steadily from ≈ 2 at M ≈ 11 to ≈ 13–15 at M ≈ 27–29. This confirms with hundreds of zeros per bin
what BM_CORRECTED §3.2 saw with 6 zeros (4/n, slope −0.23 at 19–27): **the far tail is fatter than Poisson, but on
this range −log P grows like ≈ 0.59 M^{0.88}: faster than any power of 1/M, slower than e^{−cM} for any fixed c > 0
(review repair of a reversed comparison); a finite range establishes neither asymptotically.** In fable's own drop rule
(b) ("β ∈ [0.8, 1] stable across the top three bins"), the result is: record and stop.

**m = 12, 16 (10⁷, sub-sampled).** At N = 10⁷ (window [5·10⁶, 10⁷]): m = 12 has 45 460 zeros among 1 666 357 admissible
n (prime to 6), and m = 16 has 271 201 among 2 499 537. 3 000 random zeros and 3 000 random population members each got
exact M. Both lines only reach M ≲ 12 at this height. P/e^{−M/2} is ≈ 1.0–1.3 (m = 12, M ∈ [4, 12)) and ≈ 0.9–1.3
(m = 16, M ∈ [0, 10)). The fit on the 3–4 populated bins (β ≈ 0.93 ± 0.06 formal, m = 12, 4 bins) is not informative. These rungs do not
reach the far tail at 10⁷, as the ruling anticipated.

**Caveats (Assessment; why this is steering information only).**
(i) Across-n statistic (barrier B6): it says nothing about any single n.
(ii) No finite β fit proves summability or excludes a rare structured family (astra's objection stands). If the fitted
law held with M ≈ 0.067 L², then −log P ≈ 0.054 L^{1.78}, which would be summable over n. Nothing measured here implies it
continues.
(iii) The population is heterogeneous. Low-M bins are dominated by composites with small factors, and the main term is
M_BM, not refined by n mod 2^j. On the m = 8 line the 2-adic class of n decides which pairs can hit at all (modulus
2^{3+v₂(uB)}), so mixing classes inflates the tail. The excess growth may be partly this mixture rather than a
"prime T1". Among zeros with M ≥ 26 that are prime, the residues mod 8 are 84 / 80 / 56 / 125 (for 1 / 3 / 5 / 7), a
visible but modest skew toward 7. A 2-adically refined main term (as in item (3)) is the obvious next control; it was not
run (CPU budget).
(iv) R_prime was not computed (out of the brief's scope).
**Label: EVIDENCE.** ES is not solved; no lower-tail mechanism is implied.
