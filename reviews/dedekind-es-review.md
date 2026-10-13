# R169 — hostile review of O169 `DEDEKIND_ES.md` (Parts I–II)

**Repairs applied:** all D1–D10 in DEDEKIND_ES.md (+ matching lines of AGENT_REPORT_O169.md), marked "(R169 repair)".

Reviewer: R169 (side-agent/review-dedekind). Author branch merged: side-agent/dedekind-sums.
From-scratch scripts: `scripts/review_dk_*.py` (none of the author's `dk_*` code reused).

## Summary verdicts (filled in progressively)

| Claim | Verdict |
|---|---|
| Lemma 1.1 (+ Cor 1.2, D2, D3) | **SOUND** (D8 wording) |
| Prop 3.1 | **SOUND** (D7: false side-remark) |
| Thm 4.5 (+ slice identification) | **SOUND** (D10: write out e-slice ES identity) |
| Cor 4.6 | **SOUND-AFTER-REPAIRS** (D1 convention, D2 Farey wording) |
| §8.1, §8.2, §8.3 | **SOUND**; §8.4 **SOUND-AFTER-REPAIRS** (D3: "N₋ even" false at composites) |
| §9.2 lemma | **SOUND** |
| §4.4 / §9.1 EVIDENCE, CONJECTURE SQ₅ | **EVIDENCE reproduced to 10⁶** with independent code; labels correct (D4 wording) |
| §10.1 complexity | **Assessment honest, SOUND-AFTER-REPAIRS** (D5 algorithm, D6 citation) |

**Bottom line.** No FATAL or MAJOR defect. The core result (Thm 4.5 / Cor 4.6) is correct and checked from scratch:
the polynomial mod-8 cell table, 21 430 357 words to 10⁶ (0 failures), and (R) checked against the actual
Rademacher–Grosswald text. All numerical claims I re-ran (counts, lists, records) reproduce *exactly*. Nothing is
overclaimed at the level of the main labels. ES is not solved, and the document says so.

## Defects (all MINOR)

* **D1** Cor 4.6: "five slices ⟺ λ ≤ 3" needs the convention that slice parameters may equal 1 (§4).
* **D2** Cor 4.6 / §4: the HJ length is 1 + (number of L-steps in the Stern–Brocot path), not "number of left turns" (§4).
* **D3** §8.4: "N₋ is even" holds only at primes; N₋(21) = 1 (§5).
* **D4** §9.1: "SQ₅ strengthens SQ" except at n = 105 (§7).
* **D5** §10.1: the algorithm must test the prime factors of tp+1, not enumerate divisor words (§8).
* **D6** §10.1: "CONDITIONAL_ES Thm C" should be POINTWISE_SIZE Thm C / Cor C1, which gives the fixed-T statement only (§8).
* **D7** §3: "equidistributed (≈ 50:50) on other (A,t) mod 4 classes" is false (§9).
* **D8** §2: the "odd-indexed partial quotients" sentence is garbled; correct form `r = 1 + Σ_{i odd} a_i` (§9).
* **D9** §5.2: "exactly the … not integral surgeries" is an overclaim; should be "among" (§9).
* **D10** Thm 4.5: the 4|u, 4|v slices are asserted to give ES solutions without an explicit triple. One is
  `4/n = 1/(wf) + 1/(tnw) + 1/(tnwf)`, verified for all n ≤ 5000 (§3).

**Repairs applied.** All of D1–D10 are applied in `DEDEKIND_ES.md`, each marked "(R169 repair)". D10 now writes
out explicit ES triples for both the 4|u and the 4|v slice. The matching lines of `AGENT_REPORT_O169.md` (D1, D2,
D3, D4, D5, D6, D10) are repaired the same way. D7, D8 and D9 have no counterpart in the report.

## 1. Lemma 1.1, Cor 1.2, (D2), (D3) — SOUND (minor citation/wording repairs)

Re-derived by hand:
* `[[v,t,u]] = v − u/(tu−1) = (tuv−u−v)/(tu−1)`; `(tu−1)(tv−1) = t(tuv−u−v)+1`; `A < n` since
  `n − A = (v−1)(tu−1) − u ≥ u(t−1) − 1 > 0` (the proof only states `tv−1 < n`; the other bound is the same
  by u↔v symmetry). HJ uniqueness ⇒ bijection. Boundary `u = 1`: `n = v(t−1) − 1`, `n/(t−1) = [[v, t−1]]` ✓.
* Cor 1.2 Type I: `4bcd = c + p(b+1)` reduces, with `p+u+v = tuv`, to `(tu−1)(p+v) = u(tp+1)` ✓; `u | p+v` since
  `p+v = u(tv−1)` ✓. Type II: `4abc − a − b = p` with `(a,b,c) = (u,v,t/4)` ✓. Matches CONDITIONAL_ES Lemma 1.1
  (c,f,g) = (v,u,t) exactly.
* (D3): from (D2) for A and n−A plus Riemenschneider `Σ(b_i−2) = r'−1` one gets `12s = r' − r − 1 + (A+A*)/n` ✓.
  On a certificate `r' = t+u+v−5` ✓.

From scratch (`scripts/review_dk_core.py 5000 250`): Lemma 1.1 as a set identity, word `[[v,t,u]]`, `A* = tv−1`,
`AA* = tn+1`, and the exact ES identities of Cor 1.2 and of the e-slice (see Thm 4.5 below) for **all** n ≤ 5000
(not only primes/squares): 0 failures. (D2), (D3), Riemenschneider duality and (R) by the *defining* sawtooth
sum (no reciprocity algorithm) for all coprime pairs with n ≤ 250 (19 022 pairs): 0 failures.

**Citation check.** (R) is in Rademacher–Grosswald, *Dedekind Sums* (Carus Monogr. 16, 1972), Ch. 3 §C, eq. (44),
p. 34: `12k s(h,k) ≡ k + 1 − 2(h/k) (mod 8)` for odd k, (h,k) = 1, attributed to Dedekind — verified in a scanned
copy (webhomes.maths.ed.ac.uk/~v1ranick/papers/rademacher2.pdf, OCR). Statement as used is correct. (D2) I could
not check against Hirzebruch–Zagier 1974 (no access); it is numerically exact on all 19 022 pairs above and is a
standard formula (Zagier/Barkan–Hickerson–Knuth/Myerson form).

## 2. Prop 3.1 — SOUND (one false numerical side-remark)

The proof is (R) + (D2) + a finite mod-8 polynomial check; both inputs are classical and verified above, and the
polynomial `2(A/n) ≡ n+1 − n(t+u+v−9) − (tu−1) − (tv−1) (mod 8)` is a function of (t,u,v) mod 8 (n is a polynomial
in t,u,v). `scripts/review_dk_cells.py` recomputes the 512-cell table independently: 160 admissible cells, the value
is always ±2 mod 8, and it is −2 on every cell with `4 | tu−1` or `4 | t`. No circularity: Prop 3.1 uses nothing
about ES. Credit to redteam-automorphic Lemma 5.2 is correct: there `(d/p) = −1` with d = A/4, and
`(A/p) = (4/p)(d/p) = (d/p)`.

## 3. Theorem 4.5 — SOUND (repair: write out the e-slice ES identity)

* Proof re-done: polynomial cell check (`review_dk_cells.py`, `poly_cells`): 160 admissible mod-8 cells,
  120 with value −1, all of them satisfying one of the five conditions, 40 with value +1, none of them
  satisfying one. 0 failures.
* Brute force with a direct Jacobi symbol, `review_dk_cells.py 1000000`: **21 430 357** words with n ≡ 1 (4),
  n ≤ 10⁶ (the same count as the author's), 0 failures, every mod-8 cell constant (no mixed cell), and 0 slice
  words at odd squares.
* **Slice identification checked.** Conditions 1–3 are Cor 1.2 (Type I, one denominator divisible by n; Type II,
  two). For `4 | u = 4w`, `f = tv−1`: `n + v = u(tv−1) = 4wf`, so `f | N = (n+v)/4` and `f ≡ −1 (mod v)`. This is
  the CONDITIONAL_ES §1 "Type II slice a = 1" (`b | (p+e)/4`, `b ≡ −1 (mod e)`, with b = f, e = v), i.e.
  `−1 ∈ Σ_e(N)` of LONGSHOT_PIGEONHOLE with (a,b) = (f,1). The explicit Type II solution, which the document does
  not write down, is
  `4/n = 1/(wf) + 1/(tnw) + 1/(tnwf)`
  (from `4/n − 1/N = v/(nN)` and `v = (f+1)/t`). It is verified in exact rationals for all n ≤ 5000
  (`review_dk_core.py`). `4 | v` is the u↔v reversal (n is symmetric in u, v).
* The proof is complete relative to (R) and (D2), which are proven classical theorems, so the label PROVED is
  fair. One could make it self-contained by Jacobi reciprocity alone (n = vA − u with n ≡ 1 (4) gives
  `(A/n) = (−u/A)` for odd A, and so on), but this is optional.

## 4. Cor 4.6 — SOUND-AFTER-REPAIRS (precision of "the five slices"; Farey wording)

* λ(p) ≥ 2 ✓ (L₁ = {1}). λ = 2: L₂(p) = {b₂ : b₁b₂ = p+1, b₁,b₂ ≥ 2}; for odd b | p+1, `(b/p) = (p/b) = (−1/b)`, and
  `(2/p) = 1` at p ≡ 1 (8), so some b ∈ L₂ is a QNR ⟺ p+1 has a prime factor q ≡ 3 (4) (q ≤ (p+1)/2 automatically) ✓.
  ⟹ boundary 4.2: u = q, t = (p+1)/q + 1 ≡ 3 (4), tu ≡ 1 (4) ✓.
* λ = 3 ⟺ interior hit, by Thm 4.5 ✓.
* **Precision gap (MINOR, D1).** "The five X/e-slices of ES(p) together hold ⟺ λ(p) ≤ 3" is only true once the slices
  are defined to include their degenerate parameter values (some of t,u,v = 1), at least the v = 1 Type I case. I
  checked every degenerate case for n ≡ 1 (4). Type I with u = 1 or t = 1 forces n ≡ 3 (4), and so does 4|u with v = 1.
  Type II 4|t with u or v = 1 gives `n+1 = v(t−1)` with t−1 ≡ 3 (4). The e-slice 4|u with t = 1 gives
  `n+1 = (u−1)(v−1)` with u−1 ≡ 3 (4). The last two imply λ = 2. So the equivalence holds with the convention
  "parameters ≥ 1", but the document should state that convention.
* The Farey gloss is unchecked and loosely worded (MINOR, D2). With `p/A = [v−1; 1, t−2, 1, u−1]` and Stern–Brocot path
  `R^{a₀}L^{a₁}R^{a₂}⋯`, the HJ length is `1 + Σ_{i odd} a_i`, i.e. **1 + the number of L-steps**. It is not the
  number of "left turns" (direction changes).
* EVIDENCE reproduced exactly (`review_dk_lambda.py 1000000 3000`): 556 primes p ≡ 1 (8) ≤ 2·10⁴ with 395 of λ = 2 and
  161 of λ = 3. All 19 552 primes p ≡ 1 (8) ≤ 10⁶ have an interior −1 word. No odd square ≤ 10⁶ has any interior,
  boundary or L₂ hit. λ computed by brute-force HJ expansion of every A agrees for all n ≡ 1 (4) ≤ 3000.

## 5. §8 — 8.1, 8.2 SOUND; 8.3 SOUND; 8.4 Assessment OK

* 8.1: since 2(A/n) is a polynomial mod 8 in (t,u,v), mod-4 dependence is a finite statement. `poly_cells` plus brute
  force (21.4M words, no mixed mod-8 cell) confirm that there are exactly 20 admissible classes mod 4 and that the
  +1 set is exactly the five listed classes. These are exactly the classes on which all five conditions of Thm 4.5
  fail, so 8.1 and Thm 4.5 agree.
* 8.2: Klein group trivial ✓. Rotation: I re-derived the mod-8 census myself (`review_dk_scale.py`): 40 cells
  −1→−1, 8 cells +1→+1, 0 changes. Brute force over 6 649 274 rotation pairs with n, n' ≤ 10⁶ found 0 sign changes.
  The "conjugacy invariant" reading is fine (cyclic rotation of `T^vST^tST^uS` is conjugation). It holds only on the
  sub-locus n, n' ≡ 1 (4), as stated.
* 8.3: `K(av',t,au') = a²tu'v' − av' − au' = a·K(v',at,u')` ✓, same A ✓, `(A/am) = (A/a)(A/m) = (−1/a)(A/m)` ✓.
  Independent check: 14 820 cases, 0 failures. Wording nit: for u' = 1 or v' = 1 the "word of m" is not an HJ word
  (it has an entry 1, and A can exceed m), so "sign" there means the Jacobi symbol `(A/m)` and nothing more.
* 8.4: "N₋ even (reversal pairs)": reversal fixes a word iff u = v, and then n = u(tu−2), which is composite. For
  composite n with u = v, a self-reversed −1 word would make N₋ odd. So "N₋ even" is **only true at primes**
  (MINOR, D3: either restrict it to primes or drop it).
  Concrete counterexample: n = 21 = 3·7 has L₃(21) = {[[3,3,3]]}, A = 8, `(8/21) = −1`, so N₋(21) = 1.

## 6. §9.2 lemma — SOUND (labels honest)

Re-derived: the scaled word with u' = 1 is `[[av', t, a]]` with `m + 1 = v'(at−1)` and A = at − 1, so A | m+1,
A ≡ −1 (a), and t ≥ 2 ⟺ A ≥ 2a−1. For `A = 2^k A'`: A' | m+1 gives `(m/A') = (−1/A')`, and with m ≡ 3 (4)
reciprocity gives `(A'/m) = (−1/A')·(−1/A') = 1`. Hence `(A/n) = −(2/m)^k`, which is −1 under the stated hypothesis,
and Thm 4.5 applies (n ≡ 1 (4)) ✓. Special family `n = a(at−2)` (A = m+1 ≡ 1 mod m) ✓. It implicitly needs
t ≡ 3 (4); that is part of the hypothesis n ≡ 1 (4).
From scratch (`review_dk_scale.py`): 8 290 lemma instances with a < 80, m < 4000, 0 failures. Coverage reproduced
exactly: 31 143 n, 24 645 inherited (79.1 %). The "Why this is not a proof" paragraph is accurate.

## 7. §4.4 / §9.1 EVIDENCE and CONJECTURE SQ₅ — EVIDENCE REPRODUCED; label correct

Independent code (`review_dk_lambda.py 1000000 3000`; it enumerates words and length-2 pairs, uses a direct Jacobi
symbol, and is cross-checked against full HJ expansion for n ≤ 3000):
* Non-square n ≡ 1 (4), n ≤ 10⁶, with λ(n) > 3: **only n = 105**, and λ(105) = 4 by direct expansion. ✓ This covers
  the full author range, not only a smaller one.
* The boundary criterion of 4.2 (v = 1 search) ⟺ "(n+1)/2 has a prime factor ≡ 3 (4)" ⟺ a −1 word in L₂ holds for
  every n ≡ 1 (4) ≤ 10⁶, composites included (0 mismatches).
* §4.4: a₀ = 0 at 52 non-squares ≤ 2·10⁵ (largest 156 961) ✓. a₀ = a_T = 0 at exactly the 22 listed values ✓, and
  **the same 22 values up to 10⁶** (a₀ = 0 at 61 non-squares ≤ 10⁶, largest 973 345). This extends the author's
  EVIDENCE for the §4.4 CONJECTURE to 10⁶.
* SQ₅ remarks: for n ≡ 5 (8) it is trivial (A = 2), so its content is n ≡ 1 (8) ✓. "Implies ES for all p ≡ 1 (4)" ✓.
  "Strengthening of O146's SQ": strictly, SQ₅ says nothing at n = 105, where SQ must be checked separately
  (MINOR, D4, wording).

## 8. §10.1 complexity reading — Assessment label honest; two repairs

* Literature, from my own knowledge (no source in sources/ checked): Burgess gives `n_p ≪ p^{1/(4√e)+ε}`, and
  1/(4√e) = 0.1516… ✓. Ankeny gives O(log²p) under GRH, and Bach (Math. Comp. 1990) gives `n_p < 2 log²p` ✓.
  Deterministic polynomial-time QNR finding is open unconditionally ✓. I also know of no result that a factoring
  oracle makes it easier. The author flags this as "from memory; not checked", which is honest.
* **Algorithm as stated is not polylog (MINOR, D5).** "Factor tp+1 for t ≤ T, test the words" enumerates the
  divisors A ≡ −1 (mod t) of tp+1, and τ(tp+1) can be `p^{c/log log p}`, which is super-polylogarithmic. The
  fix is easy and makes the claim stronger: if A | tp+1 and `(A/p) = −1`, then some *prime* factor q of A has
  `(q/p) = −1`. So the algorithm only has to test the O(log p) prime factors of each tp+1. That gives poly(log p)
  time plus (log p)^C oracle calls, as claimed. State it this way.
* **Mis-citation (MINOR, D6).** "CONDITIONAL_ES Thm C" does not exist. The H-conditional result is POINTWISE_SIZE
  Thm C / Cor C1, which CONDITIONAL_ES only cites (CONDITIONAL_ES l.139–144, l.205–207). As used it gives "for every
  fixed T, t ≤ T fails i.o." (bounded programs), not anything about polylog T. The sentence should say exactly that.
* EVIDENCE `t_min(p) ≤ 64` reproduced: records (17,2), (41,4), (769,6), (1049,7), (2521,15), (21841,64) for
  p ≡ 1 (8) ≤ 10⁶ (`review_dk_lambda.py`), exactly as stated.
* §10.2 coin statistics: not re-verified (outside the brief's checklist). It is labelled EVIDENCE/heuristic, which
  is appropriate.

## 9. Other items noticed in passing

* §3 "Reading": `12c·s(a,c) ≡ a + a* (mod c)` verified for all odd c < 120 by the defining sum. Combined with (R),
  this makes the mod-8c residue depend only on the stated data ✓.
* §3, numerical side-remark after Prop 3.1 (**MINOR, D7, false as stated**): "equidistributed (≈ 50:50) on the
  other residue classes of (A, t) mod 4". `review_dk_p31stats.py 20000` shows several other classes are
  **deterministic**. For p ≡ 1 (4): (A,t) ≡ (1,1) is always +1 (2650:0); (1,3) and (3,1) are always −1; and (3,3) is
  always −1. Only (1,2), (2,1), (2,3), (3,2) are mixed. This is just Thm 4.5/8.1 seen coarsely. Repair: replace the
  sentence by a pointer to the mod-4 table of 8.1.
* §2 last sentence (**MINOR, D8, wording**): "odd-indexed regular partial quotients … all 1 except …" is garbled.
  Correct statement: `r(n/A) = 1 + Σ_{i odd} a_i` for the regular CF `[a₀; a₁, …]` of n/A, so r = 3 ⟺ the
  odd-indexed regular partial quotients sum to 2 (the pattern `[v−1; 1, t−2, 1, u−1]`, or `[v−1; 2, u−1]` when t = 2).
* §5.2 (outside the brief, **MINOR, D9, overclaim**): "these are *exactly* the short-plumbing lens spaces that are
  not integral surgeries on knots in S³". The linking-form condition (±q a square mod p) is only *necessary* for
  L(p,q) to be a p-surgery. Greene's classification leaves only Berge-type lens spaces, so many QR short-plumbing
  lens spaces are also not surgeries. Repair: "are among the …" / "cannot be integral surgeries".
