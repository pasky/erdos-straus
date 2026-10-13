# AGENT REPORT O194 — is TES a finite search; non-T1 failures of T1-bearing ES analogues

Branch `side-agent/tes-finite` (merged `side-agent/synthesis-two` first). Main file `TES_FINITE.md`; scripts
`scripts/tf_*`. ES is not solved; no infinite case of ES is claimed.

## SHARP:
(R194 repair, D2/D3: item 1's insolubility at 131, 241 is Pomerance–Weingartner arXiv 2511.16817, Table 1
(m = 8: all exceptions n ≤ 10^13 are 1, 2, 3, 11, 17, 131, 241), and the no-BM half is BL Remark 1.10; Cor 5.4 / B7
is an immediate consequence of these, already witnessed at
n = 3. The new content is the TES half, items 2 and 4.)
1. **"Brauer–Manin + T1 is the only obstruction" is FALSE for Erdős–Straus-type integral models — already over ℚ,
   with positivity, order 2, and the same ℚ-surface as ES.** Schinzel's 8/n = 1/x + 1/y + 1/z (x, y, z ∈ ℕ) has
   the real anchor and an order-2 T1 at odd squares (Prop 5.1; inv₂ vanishes because v₂(8) = 3), the Brauer group
   of BL (ℤ/2, ℚ-isomorphic surface), **no Brauer–Manin obstruction at n = 131, 241 (explicit adelic
   certificates, Thm 5.3), and no solution at n = 131, 241 (certified complete search, Thm 5.2)**. Failing n ≤ 299:
   {2, 3, 11, 17, 131, 241}; failing odd primes ≤ 2·10⁵: {3, 11, 17, 131, 241}.
2. **TES(π) is a finite search** (Prop 1.1: one archimedean place + triangle inequality + two-term divisor problem;
   positivity is NOT what makes ES(p) finite) and **TES fails at 16 primes** N(π) ∈ {7, 13, 19, 61, 79, 97, 103,
   151, 193, 211, 367, 409, 769, 2029, 2239, 26893} (complete census N ≤ 30000, two independent solvers), with
   **no Brauer–Manin obstruction from Br U = Br K + ⟨α_ω, α_{−1}⟩** at any of them (Thm 3.1, certificates).
3. **Sibling barrier (B7).** PROVED part (Cor 5.4): no family-uniform "BM (incl. T1) is the only obstruction to
   positive integral points" principle holds for BL's Erdős–Straus/Schinzel models, so ES cannot follow from one.
   Assessment only: an ES proof must use something specific to the model 4/n (8/n is its all-even-denominator
   sub-problem), e.g. a pointwise count lower bound; Cor 5.4 does not exclude "solvable for p > p₀" arguments.
   Mean positive-solution count over primes in [100, 300): 32.8 (m = 4, min 6) vs 13.5 (m = 8, 2 zeros) vs 7.2 (m = 12).
4. The late TES failure N = 26893 has (χ_π(ω), χ_π(2), χ_π(λ)) = (0, 0, 0): all small data are cubes mod π — the
   analogue of ES's Mordell-hard class (O182's "failures need χ_π(ω), χ_π(2) ≠ 0" is refuted).

## Self-review (hostile reviewer subagent, R-O194) — repairs applied
B7 weakened to its proved content (above); false character-restriction removed; "open for N > 2239" corrected
(26893 refutes it); BL injectivity now cited as Cor 2.9 (normality alone is insufficient, BL Rem 2.10); tf_brute
int64 bounds now asserted a priori in Python ints (re-run: all 16 zeros and A = B on N ≤ 2500 reproduced); T1
statement for TES phrased via Type I/II shapes; minor counts fixed. Reviewer reproduced: A/B agreement N ≤ 6000,
both solvers 0 at 26893, all 16 TES BM certificates (symbols cross-checked with tw_eis), 8/n failures n ≤ 299,
679 Hilbert-symbol controls, 0 Type I/II at q².

## Results (labels)
* Prop 1.1 / Cor 1.2 (PROVED, elementary): t/n = Σ c_i/x_i over ℤ or an imaginary quadratic O with c_i n/t ∉ O
  has finitely many solutions; some N(x_i) ≤ 9N(c_i)N(n)/N(t) (TES: N(x) ≤ N(n)/9 or N(y) ≤ N(n)/9 or N(z) ≤ 4N(n)/9),
  then a divisor problem. Infinite families exist iff a two-term subsum can vanish. Goal (3) of the brief is void.
  The O192 Q³-shot family lives in TES^{□₃} (z ∉ O), consistent.
* Thm 2.1 (CERTIFIED): the 16 failures above; all other π, N(π) ≤ 30000 (split; inert p ≤ 173) solvable; all
  solutions at primes have Type I/II shape (21042/7038). Method A (`tf_exact.py`, own ℤ[ω] arithmetic, divisor
  enumeration) and method B (`tf_brute.py`, numpy lattice brute force, no factorisation, memory-chunked) agree on
  all 394 solution sets N ≤ 6000 (4160 solutions) + 4 primes near 26893; B confirms 0 at all 16 failures; O182's
  window solutions are a subset (in fact equal) at 6 tested primes.
* Thm 3.1 (PROVED per π by certificate, modulo Bright–Loughran Prop 2.6 + Cor 2.9 over k = ℚ(ω): Br U/Br K ≅ μ(K)^∨ = ℤ/6): the
  integral BM set with the 2-primary condition is non-empty at all 16 failures; e.g. N = 103: base point
  (−7 − 14ω, 5 + 4ω, z), bad only at 𝔮 = (49 − 33ω) (N𝔮 = 5107), replaced by a 𝔮-integral point with the same
  invariants (0, 0); cross-checked with O182's independent tame-symbol code.
* §4 (CERTIFIED): complete sets at π³ (N(π) = 7, 13, 19, 31, 37, 43): only "other" shapes (T1₃ control);
  TES(π³) solvable even where TES(π) is not.
* §5: Prop 5.1 (PROVED; BL's p-local Lemmas 3.2/3.4/3.5/3.9 use 4 only as a p-unit, so they hold verbatim for 8 — reviewer please re-read;
  Type II half elementary via POINTWISE_MN Lemma 1.1(d)); numerics: 0 Type I/II at q², q ≤ 100 (592 sols);
  controls m = 5, 6 have many. Thm 5.2 (CERTIFIED, divisor search + Fraction brute force). Thm 5.3 (certificates,
  modulo BL Thm 1.6 for the ℚ-isomorphic surface).
* Novelty: the 8/n failures are a trivial computation and may be in the Schinzel/Sierpiński literature (OEIS has
  no sequence 2,3,11,17,131,241 or 3,11,17,131,241; literature not searched further). The new content is the
  framing: T1-bearing + BM-unobstructed + insoluble.
  (R194 repair, D2: they ARE in the literature — Pomerance–Weingartner 2511.16817 Table 1, m = 8, n ≤ 10^13; PW Thm 3.1
  proves many failing primes for every m ≥ 8. OEIS indeed has no such sequence, re-checked by R194.)

## Not done / caveats
* Obstructions beyond BM (étale BM / descent on covers of the open log-K3 surface; π₁^{ét}(Ū) not computed) are not
  excluded; Br U° (classes ramified along the lines) not considered (the integral BM set used is BL's).
  Assessment: failures thin out with the mean count ("lottery"), but TES's isolated zero at N = 26893 (mean ≈ 20,
  all cubic characters trivial) shows a heavy lower tail, concentrated (one example) in the hard class.
* m = 8 census extended: failing odd primes ≤ 2·10⁵ are exactly {3, 11, 17, 131, 241} (`tf_schinzel.py 8 200000`).

## Suggested ledger entry
(J)26 TES_FINITE (O194): Prop 1.1 finiteness (PROVED); TES insoluble at 16 primes N ≤ 30000 (CERTIFIED), not BM
(PROVED by certificates mod BL); Schinzel 8/n: T1 at odd squares (PROVED, BL local lemmas verbatim), insoluble at
131, 241 (CERTIFIED), not BM (certificates) ⇒ no family-uniform "BM is the only obstruction" principle for ES-type
models (B7, proved part); the "ES needs model-specific/quantitative input" reading is Assessment.

## Sparks (not pursued)
* Descent/étale-BM for ES-type log-K3 models: is there a finite étale cover of U° whose BM explains 8/131, 8/241?
  (Would turn the "lottery" failures into structure; the size-dependence argues against.)
* Count law in m: mean count of m/p seems ∝ 1/m (32.8, 13.5, 7.2). A precise asymptotic c_m log³p with explicit c_m
  would predict the last failure of each m/n; ES's "luck" = c_4 large. Compare with ET's average.
* Hard classes for 8/n: 241 ≡ 1 (mod 240); 131 ≡ 3 (mod 8). Which residue classes are covered by polynomial
  identities for 8/n (Mordell analogue), and are all large-n failures in the uncovered classes?
* TES's mean count grows like ES's but is ~3× smaller at equal norm; the anchor normalisation (2-primary, density
  1/3 per variable) costs a factor ≈ 27 in raw count — is that the whole difference?
* For the order-3 family: a T1-bearing TES-variant with larger numerator multiplicity (e.g. 9·(unit) replaced by
  27) might have failures disappear sooner/later — the counts, not the structure, decide.
