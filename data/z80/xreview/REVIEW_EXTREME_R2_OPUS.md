# Hostile cross-lab review, round 2: `notes/z80/EXTREME.md` §§6–9 (commit 7c22eced2)

Reviewer: Claude Opus (cross-lab, author lane GPT-6.2 Astra). Internal review only, not externally refereed.
Scope: the commits in `git log main..` (c72d66110, 62fefacf8, 7c22eced2). Round 1 (§§1–5) was reviewed in
`REVIEW_EXTREME_OPUS.md`. I confirmed that its fixes F1–F8 are present in the text: the F1 triage, the F2 gcd wording,
the F3 Lemma CT pointer, the F4 c/a bound, the F5 3/4-vs-4x−p note, the F6 pointers and the F7 delta. This round
concentrates on the new §§6–9 and the new round-2 paragraph in §0. I did not modify the author's files and did not commit.

## Verdict

* **Theorem G (§6): ACCEPT as PROVED.** I checked it line by line: the Fourier majorant, the multiplication across
  windows, the randomized Selberg upper sieve, the Markov truncation, the remainder bound and the Mertens product. I
  found no gap. The hypotheses are adequate and the quantifiers correct. It is an upper bound only, and the text says so.
* **Complement P⁺(x) ≤ p^{1/2+ε} (§6): ACCEPT** relative to Lane 3 §4 (`101e82f00`). The chart, cube, period bound and
  size of b check out. Caveat: the source is an unmerged side-agent branch (F6 below).
* **Lane 1 compatibility (§6): ACCEPT.** It follows trivially from relative null sets. It is correct.
* **Theorem T (§8): ACCEPT as PROVED** relative to z75 `DISPROOF_OBSTRUCT.md` §3. The two-bit necessity is correct. One
  sentence is dangling (F4).
* **§7 gap records: CONFIRMED, now by two independent full engines.** My independent engine shares no code with the
  author's. It reproduces the author's 9-row table exactly over **all** 𝔐 primes up to 5·10¹². The author's engine
  also replays byte-identically.
* **§9 (MS⁺₁₀₅) on (10¹¹, 2·10¹¹]: CONFIRMED** by a full replay of both z75 engines; the outputs are identical to
  `ms1.txt`/`ms2.txt`. The arithmetic of the totals also checks. **The R₈ 1 mod 120120 AP: CONFIRMED** by a full replay
  identical to `r8high.txt`, and all 2,396 H certificates were checked independently.
* **§7 `checks.csv` (123 rows) and §8 `tower.txt`: CONFIRMED** by independent implementations.
* The remaining issues are form and scope: F1–F8 below, none blocking. The (MS⁺₁₀₅) STATUS delta is incomplete as
  proposed (F7).

No claim of ES, or of ES for large primes, is made or implied. The labels are appropriately scoped.

## 1. Theorem G: line-by-line check

*Reduction.* With k = 4x − p and a, b ≥ 1, ab | x, k | a + b, put d = x/(ab) and c = (a+b)/k. Then 4abd = p + k, and
the denominators abd, pacd, pbcd form a Type II solution with smallest denominator x (b ≤ x < p). Coin-flip squarefree
divisors d₁, d₂ with d₁/d₂ ≡ −1 (mod k) give coprime a, b after removing the gcd, with ab | x and a + b ≡ 0. So failure
gives Pr = 0 in every truncated experiment. Correct.

*Fourier.* For each retained prime ℓ the ratio factor is ℓ, ℓ⁻¹ or 1 with probabilities ¼, ¼, ½, so
E χ = ½ + Re χ(ℓ)/2 = h_χ(ℓ) ∈ [0, 1]. We have Pr(ratio = −1) = φ(k)⁻¹ Σ_χ χ(−1) ∏ h_χ. If this is 0, then
Σ_{odd} ∏ h_χ = Σ_{even} ∏ h_χ ≥ 1, since the principal term is 1 and the other terms are ≥ 0. Odd characters exist
because k ≥ 3. Correct. The real point is this: no exceptional primes in the "bad" classes need separate handling, in
contrast with POINTWISE_WINDOW Lemma 6.1, since h_χ(ℓ) < 1 simply weakens the majorant. This is why the log-log losses
of the §6 Assessment disappear.

*Product over windows.* Every factor is nonnegative, so 1 ≤ ∏_j Σ_{χ_j odd}(…). There are finitely many tuples. Correct.

*Sieve.*
* The classes 0, −k₁, …, −k_J are distinct mod ℓ for ℓ > max kⱼ.
* For odd ℓ, ℓ | xⱼ ⇔ ℓ | p + kⱼ.
* The survival probability at a prime p > z is exactly ∏_j ∏_{ℓ | xⱼ} h_{χⱼ}(ℓ), by independence across ℓ and j.
* Selberg holds for arbitrary ν_ℓ ≤ J + 1 < ℓ, with g(ℓ) = ν_ℓ/(ℓ − ν_ℓ).
* G(∞) = ∏(1 − ν_ℓ/ℓ)⁻¹, and the normalized measure includes ℓ with probability ν_ℓ/ℓ.
* E log d ≤ (J+1)(log z + O(1)). With z = X^{1/(64(J+1))} and D = X^{1/8}, Markov gives mass ≤ 1/4 above D, so in fact
  G(D) ≥ ¾ G(∞).
* The remainder is Σ_{d,e≤D} (J+1)^{ω([d,e])} ≪ D²(log X)^{O_J(1)} = X^{1/4+o(1)}.
* Averaging over the independent sieve coins gives ∏(1 − (1 + Σⱼ(1 − h_{χⱼ}(ℓ)))/ℓ).
* Σ_{ℓ≤z} Re χⱼ(ℓ)/ℓ = O(1), by L(1, χ) ≠ 0.

Total ≪ X(log X)^{−1−J/2}. **Correct.** The constants depend on the shifts, as stated.

*Scope.* "g(p) > 4J − 1" is covered because total failure implies Type II failure. Restricting to arbitrary J shifts is
fine. It is an upper bound only, and §6 says so explicitly ("does not promote the opposite lower bound"). The
J-nonuniformity is stated.

*Challenge (novelty).* The J = 1 case is notes Thm 70.9 / classical. For fixed J the result is the "standard"
upper-sieve statement which POINTWISE_WINDOW §6 labelled Assessment. Theorem G is a clean, short rigorous version of it,
and the character-majorant device is neat. External priority was not checked; the text should say "external priority
unverified" for G, as round 1 does for §1 (F5).

## 2. Complement and Lane 1 separation

Lane 3 §4 (`R_BELOW_619.md` at `101e82f00`) gives Chebyshev concentration on each fixed interior cube of the s = 2 trial
chart. Its hypotheses are coordinates ≥ X^g and periods ≤ X^θ with θ < 1/2; the mean is ≍ L² and the variance O(L²).
Here a, d ∈ [X^{1/4−2η}, X^{1/4−η}], so 4ad − 1 < X^{1/2−η}. A hit p ≡ −a (mod 4ad − 1) gives the word
4abd − a − b = p with b ≪ X^{1/2+4η} and x = abd (b < p). Hence P⁺(x) ≤ max(a, b, d) ≪ p^{1/2+ε}. **Correct.** It is
correctly called "almost all", not all primes.

The Lane 1 D separation holds: a prime-density-zero set stays relatively null on any positive-density family. The I/II
"gap = f, e" identification is right: in II, 4abd − p = e; in I, 4acd − p = f. The CRT-fibre remark follows by fixed-
modulus Dirichlet.

## 3. Theorem T

The proof of the even-tower equivalence checks out:
* Even characters kill exactly {±1} ⊂ ℤ₂^×, so orthogonality ⇔ tᵢ = ±1.
* The equation at the single place 2 then holds for the rational integers εᵢQᵢ.
* Conversely, a signed integral triple gives a D-point, with a positive real point at ∞ (3n/k, 3n/k, 3n/k works).

Sign bits: on the real-positive domain an odd 2-power character on a coordinate monomial evaluates to the 𝔽₂-linear form
Σ aᵢεᵢ. Any odd character gives the same bit on {±1}.

The numerator-8 census has both weight-1 and weight-2 patterns. All six such patterns are then attainable by
permutation. One form has a 4-element kernel and so passes. Two forms must have common kernel {000, 111}. **Correct.**
It is also correct that not every two-bit pair works: x₁ and x₂ alone leave 001.

The "image not closed" remark is correct. It follows from the z75 §3 m-power repairs, whose hypothesis s ∉ {1, 2} holds
for 131 and 241. The height bound kH³ + 3nH² ≥ 2^j is correct: tᵢ ≡ 1 (2^j) gives 2^j | kQ₁Q₂Q₃ − nΣQᵢQₗ, and this is
nonzero at a failed input. See F4 for the last sentence of the proof.

## 4. Independent computations (exact coverage)

All runs used `ulimit -v 6000000` and `timeout ≤ 1800`, with at most 2 concurrent processes. The scripts are in
`scripts/z80_xr2_opus_*` and the outputs in `data/z80/xreview/r2_opus/`. All binaries were compiled into the scratch
directory and deleted afterwards.

**4.1 Author's engines, full replays.**

| run | result |
|---|---|
| `z80_gap_sieve.c 5000000000000 32768` | 12 min 47 s. Output identical to `deep.txt`: the same 9 RECs, `postbootstrap_exact=12751672`, `max=127`. |
| `z80_gap_sieve.c 500000000000 32768` | Identical to `records.txt`. |
| `z75_push2_comp.c R 1 100000000001 200000000000` | 6 min 18 s. Identical to `ms1.txt`. |
| `z75_push2_comp_verify.c 100000000001 200000000000` | 47 s. Identical to `ms2.txt` (unk = 0 in both). |
| `z76_disproof_ap.c 120120 1 6955940568722 99999999999999` | 4 min 26 s. Output byte-identical to `r8high.txt`: 774,592,569 slots, 2,396 hard primes, miss = 0. |

**4.2 Independent g engine** (`scripts/z80_xr2_opus_gap.c`, no shared code). It uses its own segmented sieve on the six
classes, its own Pollard–Brent and deterministic Miller–Rabin, and a different window criterion: −s mod m lies in the
residue set of divisors of **s²**, computed by a doubled-exponent DP. It does no crossing; it computes the exact g of
every 𝔐 prime. Ranges [3, 10⁸], [10⁸, 6·10¹⁰] and [6·10¹⁰, 1.25·10¹¹], with 179,468 + 78,686,559 + 80,508,685 𝔐 primes:

* Records: 1009 (3), 1129 (11), 1201 (23), 21169 (31), 118801 (59), 8803369 (107), 119945383009 (111).
* No other g > 107 below 1.25·10¹¹.
* Full g-histograms are in `og_*.txt`.

**4.3 Independent threshold census** (`scripts/z80_xr2_opus_gapsieve.c`), T = 107, on [1.25·10¹¹, 5·10¹²] in five
chunks, covering 5,380,907,924 𝔐 primes.
* Crossing uses positive certificates only: every prime q ≤ 2·10⁶, and every composite d ≤ 10⁵ coprime to 210, with
  q or d ≡ −1 (mod m) for m ≤ 107, crossing p ≡ −m mod q (or d).
* About 6% of primes survive, and the exact g of each survivor comes from the §4.2 engine.
* Validation: on [10⁹, 4·10⁹] with T = 39 the sieve count 1180 equals the brute-force histogram tail exactly.

Complete list of 𝔐 primes ≤ 5·10¹² with g > 107:

    119945383009 111, 654730707409 111, 761403297769 111,
    1889389369729 119, 2136658683721 111, 2256169600129 111, 3153419441929 127, 3441110949721 127,
    4915408451209 119

Together with §4.2, which gives g ≤ 107 for every 𝔐 prime below 119945383009, with equality first at 8803369, the strict successive maxima are therefore exactly the author's table. The ties (111 ×5, 127 ×2, 119 ×2) are new
information the note does not record. The census is consistent with the Witteveen/A400619 statement that no prime in
(1.2·10¹¹, 4·10¹¹) has g ≥ 112. **This makes §7 a two-engine, cross-lab census of 𝔐 to 5·10¹².**

**4.4 `checks.csv`** (`scripts/z80_xr2_opus_recs.py`, output in `r2_opus/r2_recs_check.txt`).
* All 123 rows pass. For each: p is prime (PARI proven); x = (p + g)/4; the printed triple satisfies the equation with
  x ≤ y ≤ z; window g succeeds; and **every** window m < g fails. The window test uses divisor pairs u, v | s with
  u + v ≡ 0 (mod m), a third criterion distinct from the author's h | s² checker. Each successful window also has an
  explicit coprime-pair triple.
* The U₇ certificates were rechecked: f ≡ 7 (8), r | f + 1, tuv − u − v = p, 8 | tr.
* The L40e{18,24,30,36} rows are exactly the first 16 primes 1 mod lcm(1..40) above 10^e, so there is no outcome
  selection. The L rows equal the prime entries of `panel.csv`. The 26 R₈ controls are distinct.
* The maxima per tag match the note: 127/31/27/19/11/19/11.
* Small point: 11 of the 26 R₈ controls are outside the six 840-classes, e.g. 28154878561 ≡ 481. The note does not claim
  otherwise, but "R₈-zero controls" next to an "in-𝔐 floor" could mislead.

**4.5 `tower.txt`** (`scripts/z80_xr2_opus_tower.py`). This is a third enumeration with a different finiteness argument:
order by |x₁| ≤ |x₂| ≤ |x₃|, so |x₁| ≤ 3n/k and |x₂| ≤ 2/|k/n − 1/x₁|. Counts by number of negatives (0/1/2/3):
* 8/131: 0/11/11/0
* 8/241: 0/60/56/0
* 4/131: 32/48/16/0
* 4/241: 8/117/98/0

These are identical to the author's two engines, with the same extremal examples. The author's script also replays.

**4.6 Other checks** (`scripts/z80_xr2_opus_misc.py`).
* `fit.txt` is reproduced: 12.277/4.258/0.232/1.007 with RMSE 0.379/0.289/0.329/0.387, on the 10 endpoints.
* All 2,396 `r8high.txt` H lines satisfy 8abc − a − b = n, with n prime, n ≡ 1 (120120) and n in range. The slot count
  774,592,569 is reproduced.
* The admissible nonsquares in (10¹¹, 2·10¹¹] number 11,428,541,488 = nonM.n + M.n. M.n = 714,285,714 − 29,940 squares,
  and 29,940 is also the `ms2` squares count.

## 5. Findings (form/scope; none blocking)

* **F1 (misleading §0 sentence).** "even the full procyclic tower misses both numerator-8 failures until sign information
  is supplied" contradicts §8 ("the full tower *is* a profinite-valued reciprocity obstruction"). Only the even subtower
  (Galois group 1 + 4ℤ₂, which is the procyclic part) misses. Say "the whole *even* 2-power subtower".
* **F2 (one-sided wording).** §0 says the J-window tail "costs (log X)^{−J/2}". Say "is O_J((log X)^{−J/2}) (upper
  bound; no matching lower bound for J ≥ 2 unconditionally)".
* **F3 (label mixing in §6 "Consequences / limits").** The block is labelled PROVED but contains Assessment sentences:
  that Gallagher/GRH do not give the tuples, that the BV-level two-large-bad-factors tail is uncontrolled, and the
  dimension-one lower sieve remark. Mark them Assessment.
* **F4 (dangling sentence in the proof of T).** "The stronger bounded-cover blindness uses the z77 theorem … not the
  whole upstairs group" proves nothing stated in Theorem T. Delete it, or state the claim it supports with a pointer.
* **F5 (priority).** Add "external priority unverified" for Theorem G. It is a natural fixed-J upper-sieve statement and
  may be folklore, e.g. near Elsholtz–Tao or FHRSS 2025.
* **F6 (provenance).** The complement and the separation rest on unmerged side-agent commits (`101e82f00`,
  `93e2729db`). At export, make sure those notes land on main at those versions. Otherwise relabel the dependent claims
  CONDITIONAL on those lanes' reviewed statements.
* **F7 (STATUS delta incomplete; consistency duty).** Extending (MS⁺₁₀₅) to 2·10¹¹ must also update the other places
  that quote "certified to 10¹¹":
  * STATUS §2 item 1 (line ≈178);
  * FRONTIER line ≈966;
  * OPERATIONS line ≈60;
  * STATUS §1F line ≈165, the provenance "two engines on (10¹⁰, 10¹¹]" → "(10¹⁰, 2·10¹¹]; `notes/z80/EXTREME.md` §9".

  The §7 gap census is not a STATUS-listed census (AGENTS §3). Its triage should be DATA/WAVES (with an optional
  FRONTIER pointer), not RECORD, unless the orchestrator opens a §1F row. The note currently proposes no row, so only the
  triage word needs changing.
* **F8 (minor clarity).**
  * e* and the "cap relaxation"/"Lane 2's upper bound" are undefined and have no file pointer in this note. The e* = 0
    certificate is vacuous once an integral solution exists; this is fine but it barely merits a CERTIFIED line.
  * "The six workers here are sequential residue loops": say "single-threaded; six residue classes processed per block".
  * §7 could list the ties (§4.3 above) and cite this second engine. The CERTIFIED label can then read "two-engine
    census (author C engine + independent Opus engine, `REVIEW_EXTREME_R2_OPUS.md`)".
  * In the replay line `cc -O3 scripts/z80_gap_sieve.c …`, the include of `z52d_p2_ZF0_Z0932_minx.c` resolves relative
    to `scripts/`. This works, but it is an inherited 48-line dependency and is worth naming as such.

## 6. Recommendation

* Theorem G and Theorem T: accept as PROVED with the scopes given, after F1–F5.
* §7 records to 5·10¹² over 𝔐: CERTIFIED, now by two engines (author's and mine), with ties as listed.
* (MS⁺₁₀₅) to 2·10¹¹: promotable after this cross-lab review, with the full consistency edit set of F7.
* R₈ 1 mod 120120 AP to 10¹⁴: CERTIFIED with a single sieve engine plus an independent check of the certificates
  (the sieve-crossed slots rely on that single engine). No STATUS change.
