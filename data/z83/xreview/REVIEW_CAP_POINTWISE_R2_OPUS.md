<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="e19e0758d">
A separate reviewer subagent was asked to review the changes in `git log e19e0758d..`. Its request and review follow.

Request: review changes since e19e0758d carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus Round 2 review of Wave z83 Lane 5 (notes/z83/CAP_POINTWISE.md §§5–8, header, atlas and independent verifier). Scrutinize all 5 tags including noncoprime and p|m cases, wheel coverage, pseudosquare table and density exponents; two-aux Burgess/Lenstra–Pomerance and Brun–Titchmarsh literal ranges and constants; adaptive neutral barrier profile quantifiers, large C tail and per-prime summation. Try to refute. Ensure every conditional implication and record scope is rigorous. Cap any replay at ≤15 min, ulimit -v 6000000, ≤2 processes, Python via uv run --offline --no-project python -B. Do not edit repository.

Commit log:
commit 3497e78aae3b5d7afd0d7d2ad8a58facf4ea5f99
Author: Petr Baudis <pasky@ucw.cz>
Date:   Mon Nov 23 04:49:02 2026 +0100

    Certify cap ten through the 379-pseudosquare and bound adaptive windows

 data/z83/cap_pointwise/atlas.txt        |  71 ++++++++++++++++
 data/z83/cap_pointwise/twoprime.txt     |   1 +
 data/z83/cap_pointwise/verify.txt       |   1 +
 data/z83/cap_pointwise/witnesses.txt.gz | Bin 0 -> 852370 bytes
 notes/z83/CAP_POINTWISE.md              |  93 +++++++++++++++++++--
 scripts/z83_cap_atlas.py                | 143 ++++++++++++++++++++++++++++++++
 scripts/z83_cap_twoprime.py             |  41 +++++++++
 scripts/z83_cap_verify.py               |  87 +++++++++++++++++++
 8 files changed, 432 insertions(+), 5 deletions(-)

Review:
# Hostile cross-lab R2 review of z83 Lane 5 (CAP_POINTWISE §§5–8, atlas, verifier), commit `3497e78aa`

**Verdict: accept with minor fixes.** I tried hard to refute it and could not find a mathematical error in Proposition B, Theorem A, Theorem T or Theorem N. The fixes are about labels, scope and three garbled sentences. No claim about ES itself is made, and none is implied. I did not edit the repository; my replay scripts are in `/tmp`.

## What I replayed (all under `ulimit -v 6000000`, at most 2 processes)
- **Verifier:** `z83_cap_verify.py` passes in about 2 s: 71 rows, 82,832 records, 1,960,153,020 cells, max cap 10. I recomputed the cell count as Σ(q−1)q/2·1260 over the 71 primes from 11 to 379, and it matches.
- **Generator:** I regenerated the atlas into `/tmp` (5 min 10 s). `atlas.txt` is identical and the decompressed witness file is identical. The `.gz` bytes differ only because gzip stores the output filename in its header.
- **Table:** the note's 71 cap entries match `atlas.txt`. The verifier does not check this itself; I did.
- **Two-prime example:** `z83_cap_twoprime.py` reproduces `twoprime.txt` (200 checks, 141 nonzero adjustments).
- **My own semantic check (new):** I wrote a replay that shares no code with either lane engine. For each input it rebuilds (x, y, z) from the witness record as exact `Fraction`s. It then checks 4/p = 1/x + 1/y + 1/z, that y is integral, and that den z = r² with r odd, (r,p) = 1, rad r | y and every valuation of r at most the row cap. It searches all of a row's witnesses for a cover. It passed on:
  - 8,962 random probable primes in wheel cells across all 71 rows. Of these, 4,347 were placed adversarially, with p ≡ −m (mod q²) for an N-type witness, so that q² | K.
  - All 19,878 primes in the six hard classes mod 840 in (2·10⁶, 1.2·10⁷].

  One early "uncovered" hit was my own sampling artefact: a composite p divisible by 17. After switching to prime sampling there were no failures.

## Substance, re-derived

**Proposition B is correct in both directions.**
- A prime dividing D but not B would force a denominator prime that does not divide y, so it is excluded.
- At t | B the denominator exponent is max(0, d_t − b_t). I checked the cases d_t < 0, d_t = 0 (where v_t(y) can exceed b_t) and d_t > 0 separately.
- At p ∤ x one gets g = 1.

**The five tags are correct.**
- **D and I:** with f = kq and p ≡ −4D or p ≡ −(4D)⁻¹ (mod f), f divides pA+D or A+pD. gcd(f, pA) = 1 because the class is a unit, and p > A holds below the 2·10⁶ fallback, since A ≤ 1,044,619.
- **N, plus, minus:** I recomputed the reduced z as pK(u+v)/(mu), K(K+pu)/(mu) and p(pv+Ku)/(mu).
  - In each case the parenthesis is divisible by m because m | u+v, m | 4u+1 or m | u+4v respectively.
  - So only u can create denominator debt, and this holds even when p | m and p | K. gcd(m, K) | p always.
  - The legality tests `b+j`, `j` and `2b+j` against 2b and 2b+2E are exact. In the plus tag the case j = b gives v_s(K+pu) ≥ b, which is harmless.
  - No support prime can divide m, and q ∤ m is enforced by `c ∈ nr`.

**The wheel and the verifier logic are correct.**
- The six hard classes mod 840 are exactly the primes ≡ 1 (mod 8) that are nonzero squares mod 3, 5 and 7. This gives 2·3·10·21 = 1260 base digits mod 176400, and q ≥ 11 follows automatically.
- The valuation of K is read correctly at each depth: mod 8/16 at 2, mod s/s² at s = 3, 5, 7, and mod q/q² at q.
- Checking all b up to |j|+2e+5 is enough, because every test is constant in b beyond that point.
- The bookkeeping for two distinct exceptional q²-lifts is sound.

**Sorenson's pseudosquare bound.** I checked the arXiv PDF of 1001.3316v2.
- It gives L₃₇₃,₂ = 4235025223080597503519329 and L₃₇₉,₂ > 10²⁵.
- Its definition is: ≡ 1 (mod 8), Legendre symbol +1 at every odd prime up to the subscript, and not a perfect square.
- So a hard prime with least nonresidue n_p > 379 is at least L₃₇₉,₂ > 10²⁵, and every prime p ≤ 10²⁵ has n_p ≤ 379.
- The densities 2⁻⁷¹ and 2⁻⁷⁶ are right (71 primes from 11 to 379, and 6/192 = 2⁻⁵).

**Theorem T is correct.**
- **Signs:** I re-derived (b_i/s) = (−s/b_i) = (q/b_i) = −1, the sign patterns (−,+) for K and (+,−) for K/b₁, the 2-primary projection argument, and the parity of overflow after reducing exponents mod the even λ(m), which gives cap ≤ λ(m)/2.
- **Lenstra–Pomerance Lemma 11.2:** its literal statement (archived in UNIT_REPORT_ADJ51) takes the maximum over y ≤ x. So a single s(T) covers both endpoints T/2 and T.
  - Q = 8y² lies in [T^{1/3} log T, √T] eventually.
  - The error term √T·Q·log⁵T is about T/log²T, so the bad pairs carry weight o(1).
  - Deleting one odd prime of s(T), or relying on v₂(8b₁b₂) = 3 when s(T) is a power of 2 of size at least √log T, is correct.
- **Brun–Titchmarsh:** the modulus 8b₁²b₂ ≤ 8y³ is at most T/y. So log(T/modulus) ≍ log T, the spoilers are ≪ 1/b₁ of the total, and an absolute B₀ suffices.
- **Burgess supply:** the argument excluding a fixed number of primes, with B₀ absolute, is uniform.
- **The headline exponent:** α + 4α² ≈ 0.2436.

**Theorem N is correct.**
- **Neutral Jacobi forcing:** the identity (t/m) = (t/p) for t | K, together with (2/m) = 1 when 2 | K, forces q into the support.
- **Density per vector:** the bound 2/φ(s^a) holds, and the factor at 2, 3, 5, 7 is absolute.
- **Small C:** for C ≤ X^{1/3}, BT at [M,C] ≤ X^{1/2} against fixed-modulus PNT gives a uniform absolute constant.
- **Large-C tail:** (4) gives G ≪ X, there are (log X)^t vectors, and each class contains at most X^{2/3}+1 integers. This is needed and correct.
- **Summation over primes:** τ ≪ G^δ with δ = C₀/log log q (using u+v ≥ √q), and G/C ≤ Y^{2Et}. The total is q^{−1+O(A₀c)+o(1)} for (E+1)t ≤ c log log q.

**The GRH and Chowla clauses are correct.** Linnik is unconditional at the polylog modulus; only the auxiliary nonresidues use GRH.

## Fixes requested

1. **Label the 10²⁵ range by what it rests on.** It depends on Sorenson's external, unreplayed six-month sieve. Write "CERTIFIED rel. Sorenson's published computation", not "PROVED rel. Sorenson's tabulation". Consider adding his published ANTS-IX (LNCS 6197, 2010) version; I have not verified those details.
2. **Fix three garbled sentences:**
   - "The same proof at 373 gives the requested strict cutoff": this looks like a leftover from a request, and the 373 cutoff is not needed. Delete it or state what it gives.
   - "a general end of genus confinement does not imply the same valuation bound at m≪p^.187": .187 is unexplained and the claim is unanchored. Cite its source or drop it.
   - "consistent at zero with a full Type II rather than a (★)-line model" is opaque.
3. **Scope "two distinct / independent engines".** Both engines were written by the same lane and share conventions. State that, and cite this cross-lab Fraction-level replay as the semantic check.
4. **Narrow the STATUS delta.**
   - Theorem T's cap ≪ p^{0.244} is dominated by z75/z81 I. Its novelty is the short simultaneous window, a method feature that fails the STATUS test. Keep it in the note or FRONTIER only.
   - For Theorem A, use wording like: "CERTIFIED (two lane engines + cross-lab Fraction replay) rel. Mordell, ES verification < 2·10⁶, Sorenson L₃₇₉,₂ > 10²⁵: e*(p) ≤ 10 for all primes with n_p ≤ 379, in particular p ≤ 10²⁵. This is a relaxation; ES needs cap 0."
   - Say explicitly that z81 P already gave bounded cap for n_p ≤ Q qualitatively. The new content is the explicit constant 10.
5. **Replay hygiene.**
   - The replay command rewrites the committed `.gz`. It is deterministic (mtime=0), and byte-identical only when the output path is the same.
   - The verifier should also assert that the note's table matches `atlas.txt`.

Triage of RECORD for A (repository comparison only) and BARRIER-SCOPED for M, S and N is appropriate once these are applied. This review is the R2 cross-lab review owed in the note's §0 Review line. N's scope disclaimers (support only, neutral, coprime window, sparsity) are accurate and not overstated.
</code-review>