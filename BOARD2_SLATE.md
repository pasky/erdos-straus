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
`logs/z42_five_slice_1e6.txt` (491 primes ≡ 1 (4) in [10⁶, 1.04·10⁶)), `logs/z42_five_slice_ladder.txt` (30 primes, 10⁴–10⁸).

**Setting.** n ≡ 1 (mod 4). Interior pairs P(n) := {(u, v) ordered : u, v ≥ 2, gcd(u, v) = 1, 2uv − u − v ≤ n}. For
(u, v) ∈ P(n) write uv = 2^k w (w odd), a := −(u + v), and, at a hit uv | n + u + v, t := (n + u + v)/(uv) ≥ 2.
`R(n) := #{(u, v) ∈ P(n) : uv | n + u + v, (uv/n) = −1}` (Jacobi symbol).

**Lemma 3.1 (R = N₋ of DEDEKIND_ES Thm 4.5; PROVED).** Ordered pairs at hits ↔ length-3 words n/A = [[v, t, u]],
A = tu − 1, n = tuv − u − v. If gcd(uv, n) = 1 then (A/n) = (uv/n). Hence R(n) = #{interior five-slice words}.
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

**Proposition 3.3 (PROVED).** (a) M(n) ≥ 0; each term is 0, 2/φ(w) or 1/φ(w). (b) **T1:** M(m²) = 0 for every odd m
(gcd(m, uv) = 1 gives (uv/m²) = 1, so non-square-w terms vanish; for w = □, (a/w) = 1 and (2/m²) = 1 give ε = +1, inactive).
(c) Mean-preserving: for fixed (u, v) and fixed n mod 2^{max(k,3)}, the average of the term over the reduced classes n mod w
equals 1[active]/φ(w), the density of the hits that R counts. ∎ EVIDENCE: M = R = 0 at 49², 99², 105², 997² (M₀ ≠ 0 there:
13.65, 10.64, 5.00, 82.4 — the principal part alone fails T1, as argon/astra said).

**Proposition 3.4 (the principal density; Assessment = standard Dirichlet-series computation, + EVIDENCE fit).** Let
M₀(n) := Σ_{active} 1/φ(w) (depends on n only through its size and n mod 2^k). Averaged over n ≡ 1 (4) the per-pair
weights (relative to 1/φ(u′)φ(v)) are: odd–odd 1 on the three good classes; k = 1: 1/2 (half the n mod 8);
k = 2: 1[v ≡ 3 (4)]; k ≥ 3: 1[v ≡ 3 (4)]·2^{2−k}. With Σ_{m ≤ x odd} 2^{ω(m)}/φ(m) ∼ (3/(2π²)) log² x this gives
`M₀ ∼ [ 9/(8π²) (odd–odd) + 3/(2π²) (k = 1) + 3/(2π²) (k = 2) + 3/(2π²) (k ≥ 3) ] L² = (45/(8π²)) L² ≈ 0.570 L²`
(ordered pairs; each even sector counts both orientations). Fit a L² + b L + c over 10⁴…10⁸ (6 primes per decade):
odd–odd a = 0.1140 (pred. 0.1140), k = 1: 0.1519, k = 2: 0.1519 (pred. 0.1520), k ≥ 3: 0.118 with a positive L-term
(slow: cutoff p/2^{k+1} and p mod 2^k fluctuation). **Correction to the board:** the opposite-parity sector is
3 × (3/(2π²)) L², not 2 × — the k ≥ 2 sectors are automatically active (Lemma 3.2). So fable's principal 33/(8π²) is wrong;
the correct principal constant is **45/(8π²)**. Ruling (c)'s suspicion was right; 9/(8π²) for ordered odd–odd stands.

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
o(1) after partial summation. Hence the bound is κ(u′)(D β L + O(1)), β = 1/4 + ε. With PV, β = 1/2 and T₀ = √p L².
Then use Σ_{u′ odd ≤ X} φ(u′)/u′² = (4/π²) log X + O(1), Σ φ(u′) log u′/u′² = (2/π²) log² X + O(log X) and
Σ κ(u′)/u′ = (6/π²) log X + O(1). The same holds with u′ restricted to a class mod 4 (halve each constant). ∎
*Families (pairwise disjoint subsets of P(p); every term is ≥ 0, and c_{u,v} ≥ (1 − χ(uv))/(u′v), except for w = □
pairs at p ≡ 5 (8), whose total is O(1)):*
* even sectors, u′ ≤ √p short, v long (both orientations (2^k u′, v) and (v, 2^k u′), disjoint by parity), v ≤ p/(2^{k+1}u′):
  k = 1 with S = the two active classes of v mod 8 (D = 1/4); k = 2 with v ≡ 3 (4) (D = 1/4); k ≥ 3 with v ≡ −p (mod 2^k)
  (D = 2^{−k}, Σ_{k≥3} = 1/4, truncated at k ≤ K → ∞ slowly). Each of the three sectors × 2 orientations gives
  (1/4)(3/4)/π² = 3/(16π²) at δ = 1/2, β → 1/4. Total 18/(16π²).
* odd–odd, one orientation, u ≤ √p short, v ≤ p/(2u): for u ≡ 1 (4), v ≡ 3 (4) (D = 1/4); for u ≡ 3 (4), all odd v
  (D = 1/2). Total (1/4 + 1/2)·(1/2)·(3/4)/π² = 9/(32π²).
Sum: 36/(32π²) + 9/(32π²) = 45/(32π²). PV: the template factor max_{δ≤1/2}(δ − 2δ²) = 1/8 replaces 3/4, i.e. 1/6 of the
Burgess value. ∎
*Check of the template main part (EVIDENCE):* Σ_{u′ odd ≤ √p} Σ_{v ≡ 3 (4), v ≤ p/(8u′), (v,u′)=1} 1/(u′v) = 7.34 / 10.03 at
p = 1 000 033 / 10 000 121, against (1/4)(3/2)L²/π² = 7.25 / 9.87.
*Comparison.* Argon's 33/(64π²) ≈ 0.052 rested on the unverified 2·M_BM identification; astra's 9/(64π²) (unordered good
odd–odd) is consistent with our odd–odd family, but the Burgess saving here is larger. The class restriction is put inside
the initial segment, where the trivial bound scales with the density D; this is the only new device. The theorem gives
1/4 of the principal constant, versus 1/8 for M_BM in BM_CORRECTED Thm 2.2. It concerns the **main term only**. It
does not give R(p) > 0: as in BM_CORRECTED §3, the remainder can be ≥ M i.o. (Linnik-type), and B3 is untouched.

**Numerics (EVIDENCE).**
* 491 primes p ≡ 1 (4) in [10⁶, 1.04·10⁶): mean R/L² = 0.472, mean M/L² = 0.450, mean M₀/L² = 0.450; min R = 26,
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
* Zeros: HJ_DEEP (S) already gives R(n) > 0 for every non-square n ≡ 1 (4), n < 10⁸, except n = 5, 105. Here min R = 26 on
  the 10⁶ sample.

**Labels.** Lemma 3.1, 3.2, Prop 3.3, Thm 3.5: PROVED (Thm 3.5 uses Burgess; o(1) ineffective in practice like
BM_CORRECTED's). Prop 3.4's constant: Assessment (Dirichlet-series sketch) + EVIDENCE fit. Under GRH M ∼ M₀ by the argument
of BM_CORRECTED Prop 2.3 (not re-derived here: Assessment). Value: bookkeeping on an existing object, not a lower-tail
mechanism (the board's verdict stands). The k ≥ 2 automatic activation explains why the five-slice union has a 3.75× larger
principal constant than (★) (45/(8π²) vs 3/(2π²)).
