# Hostile citation/claims review: Z58_LIT.md

Reviewed 2026-11-05. **No BLOCKER found in the cited exceptional-set statement or Prop I. Eight MAJOR findings; corrections required before exporting the memo's conclusions.** ES remains open. `Z58_LIT.md` is untouched.

Evidence: independently opened the two archived PDFs; queried GitHub, arXiv, Zenodo and Crossref; downloaded/read Chiang–Ciou–Tsai, Conrad, Koymans–Pagano, Dao, Bright–Loughran, Rickards–Stange, Lenstra and Hales PDFs. Network commands used `timeout 120`. Temporary extracts/API responses are under `/tmp/z58-review/` (not a permanent archive). Both probe scripts were rerun under `ulimit -v 4000000`; no Lean build was attempted.

## Findings

1. **MAJOR — Finite F3 data cannot refute finitely many exceptions.**
   - **Location:** §0, lines 47–48; thin-orbit table row, line 66; repeated in §3.
   - **Claim:** “Every non-square n except a finite sporadic set” contradicts the composite data; Rickards–Stange-shaped mechanisms therefore fail F3; the zeros are “apparently unbounded.”
   - **Problem:** All 285 observed composites can belong to a finite exceptional set. Increasing counts in a finite range do not establish infinitely many zeros. This is a logical error even under an EVIDENCE/Assessment label.
   - **Evidence:** The file contains only finitely many inputs, maximum 7,753,881. Rickards–Stange, arXiv:2401.01860v3, Thm 2.8 really does describe squares plus the finite set `{3,6,7,10,12,15,18,19,27,31,34,55,63,99,115}` for its particular orbit; it does not prescribe the exceptional set for an unidentified ES transfer.
   - **Fix:** Say F3 refutes *exception-free* nonsquare positivity, or a specified exceptional list/threshold omitting an observed zero. Mark infinitude of composite zeros CONJECTURE, not a falsifier already established.

2. **MAJOR — The mechanism-elimination conclusion is much stronger than the screens.**
   - **Location:** §0 lines 71–76; §3 lines 254–258, proposed FRONTIER lines 289–290, bottom line 292–295.
   - **Claim:** F3 kills all primality-blind reciprocity/character/thin-orbit mechanisms; a viable mechanism “must be prime-specific AND threshold-bearing”; the literature contains no mechanism that *could* prove (MS).
   - **Problem:** Finite zeros constrain the domain/conclusion of a proposed theorem, not the entire proof technology. A criterion not explicitly using primality can hold for all sufficiently large primes and some composites while excluding these composites. Likewise an all-primes theorem in another family can admit a size-dependent transfer to (★). No exhaustion theorem is supplied. Finding 1 also invalidates a principal premise.
   - **Evidence:** The screens specify failed inputs only. None identifies a necessary hypothesis for all possible character, reciprocity or orbit arguments. The memo itself correctly says “a verbatim port” in the Pell row, then silently drops that qualification in its verdict.
   - **Fix:** Retain only the scoped Assessment: no *direct, verified transfer supplying (MS)* was found. State precisely which proposed positivity statements the finite screens refute; remove “kills,” “must,” and “could” at mechanism-class level.

3. **MAJOR — Dao's essential local hypothesis is omitted.**
   - **Location:** §2.6 lines 231–233; §0 integral-HP row.
   - **Claim:** Dao Thm 5.2 gives local points and an algebraic BM obstruction for `k = ℓ²` with ℓ in a congruence class.
   - **Problem:** The congruence condition alone is not the theorem's hypothesis.
   - **Evidence:** arXiv:2504.10992v2, p. 22, Thm 5.2 requires **both** `ℓ > 0, ℓ ≡ 1 mod P` and `(p,13)_p = 0` for **every prime divisor p of ℓ**, for the explicitly defined MK3 family. The research note `q3_hasse_squares.md` retained this second condition; the memo dropped it. A condition on the product ℓ modulo P does not impose this condition on each prime factor.
   - **Fix:** Restore both assumptions, or say “a restricted square-parameter family satisfying the congruence and prime-factor Hilbert-symbol hypotheses.” Label as a cited PROVED theorem, not a general square-parameter assertion.

4. **MAJOR — The quoted divisor upper bounds lose necessary coprimality hypotheses.**
   - **Location:** §2.5 lines 222–223; §0 divisor row.
   - **Claim:** Lenstra gives at most 11 divisors in a class “when s > n^(1/3)”; CHN similarly supplies an upper bound when `s > n^α`.
   - **Problem:** As stated, Lenstra's numerical assertion is false. Calling these *upper* bounds is correct, but the hypotheses cannot be reduced to the modulus-size inequality.
   - **Evidence:** Lenstra's theorem, p. 331, assumes `0 < r < s < n` and `gcd(r,s)=1`. Hales Thm 4.2 additionally states `gcd(s,n)=1` and `n > n₀(α)`. Counterexample to the memo's unqualified Lenstra sentence: `n=115500, r=100, s=200`; `s > n^(1/3)`, but the 16 numbers `100d`, for `d | 1155`, are divisors congruent to 100 modulo 200.
   - **Fix:** Restore the coprimality/range hypotheses (already present in `q2_single_integer.md`). Keep the correct conclusion that these results do not force a divisor to exist.

5. **MAJOR — Exact public-priority and independence claims exceed the timestamp evidence.**
   - **Location:** opening; §2.1 lines 129–143; proposed FRONTIER lines 285–288; bottom line.
   - **Claim:** The result “was public on 2026-07-30,” was the “first public” 3/4 result, and the campaign's result is an “independent” proof.
   - **Problem:** The checked evidence establishes an earlier **dated Git commit containing the claim**, not its first public availability or literature-wide first priority. Git author/committer dates are not publication attestations. Separate development/independence is also not established by two commit dates. This distinction matters because the memo directs changes to priority statements.
   - **Evidence:** GitHub root commit `268ebdbfe19f52fd70ae4d7172fda7d492eb5b79` has no parents and author/committer date 2026-07-30; its `saving` really has exponent 3/4. The repository API says created 2026-07-12 and **currently** public, not when this commit first became publicly accessible. The campaign file was added in `4ecb5cb1` on 2026-09-06. No contemporaneous public release/archive or development-independence evidence is cited.
   - **Fix:** Cite K-R-K and correct the outdated literature assessment now, but phrase chronology as “the currently public repository contains a 3/4 claim in a commit dated July 30, earlier than our September 6 first commit.” Obtain a dated public snapshot/release before asserting exact public priority; use “separate internal proof” unless independence is documented.

6. **MAJOR — A restricted sieve ceiling is presented as a universal CRT ceiling.**
   - **Location:** §2.1 lines 142–143.
   - **Claim:** “3/4 is the limit of CRT/coefficient-sum sieves,” agreeing with K-R-K Remark 1.2.
   - **Problem:** The campaign theorem has a restricted class of families/majorants, not all CRT or coefficient-sum sieves. K-R-K's remark explains an achievable exponent under mass/overlap/level assumptions; it does not prove a ceiling or optimality.
   - **Evidence:** `EXCEPTIONAL_KARY3.md`, Cor. 4.2, applies to “every method in the class of K2 Cor 6.1” with specified whole-avoider majorants and coefficient-sum rounding. K-R-K Remark 1.2 says mass `(log X)^k` plus the stated overlap/level conditions gives exponent `k/(k+1)`; nothing there excludes another family with larger k.
   - **Fix:** State the exact audited-method scope. Describe Remark 1.2 as consistent with the *mass-to-exponent calculation*, not independent confirmation of a sharpness theorem.

7. **MAJOR — The negative-Pell “no link” conclusion is contradicted by the unconditional probe totals.**
   - **Location:** §0 lines 51–56; §2.6 line 247.
   - **Claim:** The zeros are “not enriched in negative-Pell (2-class-group) failure”; the probe “found no link” between composite zeros and negative-Pell failure.
   - **Problem:** The conditional all-1-mod-4 sample does not support a population-level absence claim, and the unqualified later sentence ignores the very strong elementary obstruction included in the same data. These data are not size-matched or a test of absence of association.
   - **Evidence:** Reproduction gives 259/285 zeros with a 3-mod-4 prime factor, plus 6/26 Pell failures among the remainder: **265/285 = 93.0% negative-Pell failure overall**. Controls give 15459 such factors plus 1502/4541 remaining failures: **16961/20000 = 84.8% overall failure**. Conditional failures are 6/26 versus 1502/4541; 6/26 has a Wilson 95% interval roughly 0.11–0.42, including the control 0.331. Above 10⁵ there are only 17 eligible zeros.
   - **Fix:** Say “no observed *additional* enrichment after conditioning on all prime factors being 1 mod 4; small, unmatched samples do not establish absence of an association.” Distinguish the unconditional enrichment, elementary local obstruction, and genuinely class-group-related question. Label EVIDENCE throughout.

8. **MAJOR — Quadratic nonresidues and Jacobi-character nonresidues are conflated.**
   - **Location:** §0 least-QNR row, F1 cell.
   - **Claim:** “A non-residue exists iff n is not a square.”
   - **Problem:** False for ordinary quadratic residues modulo a composite: 2 is a quadratic nonresidue modulo the square 9. The intended statement concerns the **Jacobi character on units of an odd modulus**, not square classes in the unit group or arbitrary cited prime-modulus results.
   - **Evidence:** Squares modulo 9 are 0,1,4,7; nevertheless the Jacobi character modulo 9 is principal. For odd n, `(a/n)` is nonprincipal precisely when n is nonsquare. LLS's quoted corollary has prime modulus, so it does not itself state this square/composite dichotomy.
   - **Fix:** Explicitly say “an a coprime to odd n with Jacobi symbol `(a/n)=-1` exists iff n is nonsquare.” Keep prime-only least-QNR results separate from that elementary character observation.

9. **MINOR — Dirichlet is not the theorem giving natural prime-pattern frequencies.**
   - **Location:** §2.3 lines 189–190.
   - **Claim:** “By Dirichlet's theorem in APs” the limiting frequencies are equal, followed by “PROVED relative to PNT in APs.”
   - **Problem/evidence:** Dirichlet's infinitude theorem does not establish the natural relative frequencies in question; PNT in APs does. Ventas Thm 6.1 uses the latter. The second half of the memo already names the correct theorem.
   - **Fix:** Replace the first attribution with “By the prime number theorem in arithmetic progressions.” This is an unconditional classical input, not an unproved condition. The corollary itself is valid.

10. **MINOR — Prop I needs an explicit domain; “n* is huge” is not universal.**
    - **Location:** §2.3 lines 177–178, 185–186, 194.
    - **Claim:** Inversion is stated for x without a unit restriction; the cutoff breaks “since n* is huge.”
    - **Problem/evidence:** `(4x)^(-1)` is undefined for nonunits. Use positive `d ≡ 3 mod 4`, `x ∈ (Z/dZ)×`, and positive n,n* when interpreting actual (★) solutions. Fixed-D symmetry never breaks; what is absent is a guarantee that the *complete n-dependent search ranges* agree. An inverse representative need not always be huge, and n* can be chosen in infinitely many ways.
    - **Fix:** Add the domains and state the actual limitation: no preservation of the two complete cutoffs is proved. The supplied proof of the involution and the u↔C swap is otherwise correct.

11. **MINOR — The half-decade presentation omits nine zeros.**
    - **Location:** §0 lines 38–39.
    - **Claim:** The displayed half-decade counts accompany the 285-total screen.
    - **Problem/evidence:** The listed bins are individually correct but sum to 276. Missing bins are `[10^1.5,10²):1`, `[10²,10^2.5):3`, `[10^2.5,10³):5`. The stated range starts at k=3, so this is incompleteness, not a false bin count. The 71 mod-24 and 15 Mordell counts are correct.
    - **Fix:** Include the three bins or explicitly say the displayed breakdown excludes nine values below 1000. The rising *absolute* counts are not density/non-thinning evidence: the bin widths grow geometrically.

12. **MINOR — The 58% citation changes the population, and the table overextends it.**
    - **Location:** §2.6 lines 241–243; §0 Pell row, “positive proportion of the rest.”
    - **Claim:** Conrad directly supports 58% among squarefree numbers with all prime factors 1 mod 4; the table speaks of the rest of the nonsquare composites without squarefreeness.
    - **Problem/evidence:** Conrad Remark 3.6 and Koymans–Pagano Thm 1.1 as stated count squarefree d with prime factors **1 or 2 mod 4**. This is not literally the odd-only population used in the memo, and neither quoted statement covers arbitrary nonsquarefree controls. An odd-only refinement may be true, but it needs a justification/citation rather than an altered paraphrase. For nonsquarefree n, solvability of `x²−ny²=-1` includes an order/conductor restriction; it is not simply the squarefree field question.
    - **Fix:** Quote the proved population exactly, or supply the odd-subfamily refinement. Restrict the table's positive-proportion claim to the cited squarefree population. Also write “squares n>1” if allowing arbitrary integer x,y: n=1 has `(x,y)=(0,1)`.

13. **MINOR — Akaka's count and constants are paraphrased too broadly.**
    - **Location:** §0 exceptional-set row; §2.2 lines 160–162.
    - **Claim:** It counts “all Type II solutions,” and 12 primes are “far below the allowed ≈ X/(log X)^4.”
    - **Problem/evidence:** Zenodo explicitly defines **distinct strict ordered triples** `x<y<z`, with p dividing y,z but not x; it is not literally an unrestricted count of all representations. The record explicitly disclaims numerical constants/onset. Its unknown C and X₀ do not give a numerical allowance at 10¹⁰.
    - **Fix:** Say “the full strict Type-II family, not just the c=1 line,” and retain the valid non-conflict argument on that basis. Remove the numerical allowance or mark it only a scale illustration, not a certified application at 10¹⁰.

14. **MINOR — “Verified” merges source claims, CI evidence, and inherited records.**
    - **Location:** opening labels; §2.4 “Status changes (verified)” / “Unchanged (arXiv API)” list, especially Bradford and Chamberland; §2.5–2.6 cited results.
    - **Claim:** The blanket presentation makes all entries freshly source-verified, with the named epistemic labels applied consistently.
    - **Problem/evidence:** The q1 notes identify Bradford/Chamberland journal metadata as inherited from `LITERATURE_2026.md`; they are not results of the arXiv version API batch. Direct journal access in this review failed DNS, so these two records remain independently unchecked here. Conversely, K-R-K's successful public CI and faithful definitions really were independently checked; they should not be demoted to a mere subagent assertion. Many cited statements have no explicit PROVED/CERTIFIED/source-claim label despite the announced convention.
    - **Fix:** Split bibliographic CERTIFIED/API facts, cited theorem statements (PROVED in cited source, proof not audited), author claims (Akaka), inherited records (EVIDENCE, previously recorded), and Assessments. Say “no additional axioms beyond Lean's three standard axioms” rather than literally “axiom-free.” Do not imply that this lane rebuilt Lean.

15. **MINOR — Search absence is not exhaustive literature coverage.**
    - **Location:** §1 Q1; §2.4 line 209; §3 bottom line.
    - **Claim:** Every 2024–2026 item is within scope; no ES preprint after the named Ventas paper.
    - **Problem/evidence:** I reproduced the `all:Straus`, submitted-date-sorted query; Ventas is the latest relevant returned item. That verifies the search result, not completeness for papers without that indexed string or non-arXiv sources. The scoped function-field “none found (bounded search)” wording is appropriately cautious.
    - **Fix:** Say “no later ES item returned by this query/search.” Preserve the distinction between requested exhaustive scope and achieved bounded coverage.

16. **MINOR — A shortened Ventas quotation is presented as a complete verbatim sentence.**
    - **Location:** §2.3 line 174.
    - **Claim:** “The identities do not establish universal Grid coverage.”
    - **Problem/evidence:** The archived introduction continues “…or a reduction of that question to four ordinary prime classes.” The extracted fragment conveys the right warning, but its new terminal period is not the source's quoted sentence.
    - **Fix:** Quote the full sentence or use an ellipsis/paraphrase. No mathematical consequence changes.

## Checks that passed (not objections)

- **K-R-K statements and Lean:** Archived PDF SHA-256 `20a3290be4c1ea58ea39378cafe9287f7a338703d19512474a346bb468702acb`; Theorems 1–2, prime corollary, Remark 1.2, and Thm 5.2 match the memo's mathematical statements. Example 1.1 checked with exact fractions. At `f6c99eaa`, `ErdosStraus/Paper.lean` states the claimed bound with no theorem hypotheses; `Basic.lean` counts actual exceptional integers in `[2,N]`, uses real exponent 3/4, and positive existential c,C; `Congruences/Certificates.lean` defines positive natural denominators with rational equality. No statement-substitution defect found.
- **K-R-K CI/history:** GitHub run `41075205124` at `f6c99eaaca6ec7a7226a7a16bef1cd2b09e36660` succeeds; jobs API specifically reports both Build and Check axioms successful. The workflow checks five outputs for exactly `[propext, Classical.choice, Quot.sound]`. README quote matches. Root commit `268ebdbf` has the 3/4 definition; its `FORMALIZATION.md` explicitly lists nine analytic axioms. These substantiate current CI certification, not the separate public-date inference in finding 5.
- **Campaign comparisons:** `git log --diff-filter=A -- paper/es-threequarter-note.tex` gives September 6. Its abstract has the earlier-improvement wording; `FRONTIER.md:61` really says INTERNALLY PROVED; `LITERATURE_2026_UPDATE.md:7` really says no new bound shown to surpass Vaughan. Updating the latter substantive assessment is justified. No interval/progression **exceptional-count theorem** or uniform-in-m exceptional-count improvement is stated in the K-R-K PDF; Theorem 2 is fixed-m. Its many uniform auxiliary estimates should not be confused with such an extension.
- **Akaka:** Zenodo 22905042 is v0.8, publication date September 22, title and quoted inequality match; certificate language is correctly reported as the author's claim. The record explicitly warns independent specialist review is outstanding.
- **Ventas/Prop I:** The archived PDF (`140b8a75a92cf0304993282119765c6dc2bf520146fa5e562061e88c301d12e3`) agrees on eqs. (1),(6), Thms 3.1/6.1 and Prop 4.1. For prime n the Grid certificate is indeed Type I: a hit has `t≤(n−1)/2`, `gcd(n,4t)=1`, and `i=(n+r)/(4t)<n`; if n divided k, `rk=n+i` would force n to divide i. Thus only ntk is divisible by n. The modular proof of Prop I, u↔C swap, and positive-integer corollary are valid. Required run `ulimit -v 4000000; timeout 600 uv run python scripts/z58_lit_inversion.py` reports **0 violations through d=20000**, with pairs `{1,289},{121,169},{361,529}`. For the frequency corollary extend inversion on the odd part of `lcm(840,L_D)` by keeping the residue 1 mod 8; CRT and PNT in APs then give the stated finite-pattern law.
- **Metadata:** Crossref confirms Ramanujan J. 69(2), article 31, January 14, 2026, DOI `10.1007/s11139-025-01312-2`. arXiv confirms versions 2509.00128v1, 2610.32302v1, 2605.23601v2, 2605.04551v3, 2609.09204v2; Jiang's abstract page explicitly says withdrawn (the API comment alone only says “some errors”). GitHub confirms leochlon/erdstrau 404, formal-conjectures 242.lean last-touch September 18, carlok last commit September 21. The live erdosproblems page lists Vaughan's bound and MiDu25 and does not mention K-R-K; it does not explicitly pronounce a “current record.”
- **Pell proof:** Correct after saying “least nontrivial positive solution.” Mod 4 forces y even and x odd. Coprime `(x−1)/2,(x+1)/2` have product `p(y/2)²`, so one is a square and the other p times a square. The orientation `x+1=2a²` gives `a²−pb²=1` with `1<a<x`, contradicting minimality; the other gives norm −1. Chiang–Ciou–Tsai Example 4 contains the quoted prime statement. The prime probe has no failures below 200000. No Pell proof error found.
- **BM/orbit citations:** Bright–Loughran Thms 1.1/1.8 genuinely give no BM obstruction to positive-integral existence for the full ES surface (and do not prove existence); Thm 1.9 is a different, strong-approximation failure. Rickards–Stange's quoted orbit shape is accurate; its use as an F3 falsifier is not. No transfer of the full ES BM theorem to the (★) subfamily is justified or supplied.

## Recomputed F3 ledger

Total 285; minimum 57; maximum 7,753,881 (the stated 7,999,801 is the screen endpoint, not claimed to be the largest zero). Half-decade start k/count: `1.5/1, 2/3, 2.5/5, 3/12, 3.5/12, 4/25, 4.5/35, 5/45, 5.5/50, 6/62, 6.5/35` (last bin partial). Exactly 71 are 1 mod 24.

All 15 Mordell entries and factorizations:

```text
1969    = 11·179
2641    = 19·139
5161    = 13·397
18001   = 47·383
23881   = 11·13·167
90889   = 97·937
112849  = 11·10259
199369  = 193·1033
345361  = 29·11909
349609  = 13·26893
510169  = 11·19·2441
539281  = 23·23447
897961  = 443·2027
2956321 = 211·14011
3210601 = 19·37·4567
```

`timeout 1200 uv run --with sympy python scripts/z58_lit_negpell_f3.py`, under the memory limit, exactly reproduces `negpell_f3.txt`: 0.909 / 20 of 26 overall; 0.911 / 12 of 17 for the 192 zeros ≥10⁵; controls 0.773 / 3039 of 4541. The arithmetic is sound; finding 7 concerns the interpretation.
