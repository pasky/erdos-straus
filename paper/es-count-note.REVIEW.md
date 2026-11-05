# es-count-note — referee report and responses

Paper: `paper/es-count-note.tex` / `.pdf` (wave z56, lane PAPERCOUNT). Internal; not posted.
**The Erdős–Straus conjecture is not proved by this paper; the paper says so in the abstract, §1.5 and §7.**

## Sources and name map

| paper | source memo (and its reviews) |
|---|---|
| Thm A / Thm 3.12 (12/37), Thm 3.14 (exponent pairs; 21/65 rel. Bourgain, 4/13 conj.) | `Z53_SQSIEVE.md` Thm A, A′, Cor A″; `data/z53/xreview/REVIEW_SQSIEVE.md` |
| Thm 3.8 (n^{1/3−1/225}(log n)²), first step | `Z53_HYPSUMPROD.md` Thm 1; `data/z53/xreview/REVIEW_HYPSUMPROD.md` |
| Thm B / Thm 4.8 (M_gen ≥ (2/(3π⁴)−ε)log²p) | `Z53_GENUSLVAL.md` Thm U; `data/z53/xreview/REVIEW_GENUSLVAL.md` |
| Prop 4.10 (slice formula) | `Z53_GENUSLVAL.md` Prop C (same review) |
| Thm 4.12 = "Theorem D" (order ≥ 3 mod 8u, density level) | `Z53_GENUSX.md` Thm X; `data/z53/xreview/REVIEW_GENUSX.md` |
| Thm C (R(p) ≥ (1−η)log²p/64 off O(η⁻²π(X)/log X)) | `Z53_PZ.md` Thm A; `data/z53/xreview/REVIEW_PZ.md` |

`Z55_CROSSO.md` Thm P (positive proportion with R_𝔉 ≥ 2) was **not** included: it is implied in spirit by Thm C for R and
would add a second BV argument for a weaker statement on the subfamily.

Scope fixes inherited from the source reviews and respected in the paper: Prop C is stated only for squarefree
u ≡ 1 (4), u ≤ p^α, α < 3/5, with the L′ and H′ terms kept (REVIEW_GENUSLVAL fixes 1–2); no estimate for X(p) and no
per-coset claim; Bourgain instance stated relative to his Theorem 6 (sketched proof, phase class); the balanced-block
discussion is a labelled heuristic, not Prop B2; Lemma C3 / the reverse-direction material of SQSIEVE is omitted; Thm D
requires an integer r and C1, C2*, C4 (and C3 for the lower bound) (REVIEW_GENUSX fix 1); PZ: ET Thm 1.1 mean orders
(only f_II has proved mean ≍ log³), no rate-optimality claim, no priority claim, ET Rem. 1.3 scoped to their methods
(REVIEW_PZ fixes 1–4). The Prop 6.1 spike term of PZ uses the cross-review's simplification Σ_{d|n}φ(d) = n, giving
V ≤ (8ζ(2)/9 + o(1))log³Q and the admissible constant c₀ = 1600 (the memo's 6000 also holds).

## Re-derivation and verification done by the author (before the referee)

* Every proof re-derived while writing (square detection, square-sieve variant, complete sums incl. a direct Kloosterman
  reduction S(2̄ℓ, 2̄ℓd; q), Vaaler + third-derivative discrepancy, Poisson, strip bound, both assemblies; genus subfamily,
  local factors of h, conductors f_F f_G = 4up, hyperbola lemma (a)/(b) error terms, L-average, optimisations 1/12 and
  121/5120; truncation, BV moments, variance identity, one-cell structure, hyperbolic cells, variance bound, final constants).
* Exact exponent bookkeeping: `paper/es-count-note.checks.py` (sympy) prints all vertex deficits for general κ as factored
  rational functions (all ≥ 0 on [0, 1/4)) and checks 12/37, 21/65, 4/13, 17/54 exactly.
* Independent C program `paper/es-count-note.checks.c`: the 14 primes p ≡ 1 (4) ≤ 10⁷ with R(p) = 0 (409 … 8813281) and no odd
  square ≤ 10⁷ with R > 0; M_gen by direct evaluation of (1.4): 3.99907 at 409 (= 18484931/4622310 of REVIEW_GENUSLVAL),
  0.0839 log²p at 8089 (census minimum), 0 at 31², 35², 99².
* PZ model variance recomputed with `scripts/z53_pz_exactV_trial.c` at Q = 10², 10³, 3·10³ (V/log³Q ≈ 0.021).
* Literature (research subagents + own reading): ET arXiv:1107.1010v6 read directly (definitions p. 3, (1.4), Thm 1.1, Rem 1.3,
  Prop 1.6, Prop 1.7, Thm 1.8 incl. the prime statement, Prop 2.6); Shiu Thm 1 (p. 163, OCR of the local scan); Titchmarsh
  Thm 5.11 and Bourgain Thm 6 (primary, per `data/z53/sqsieve/LIT_CHECK.md` and the referee); IK Thm 11.11/Cor 11.12, Thm 12.6,
  Thm 17.1; HLMLT arXiv:2511.17778v2 Thm 1.2; Elsholtz–Planitzer Thm 1; Bright–Loughran Thm 1.1, Cor 1.4; Salez; Trudgian–Yang
  §1.1–1.2. Bibliographic data checked via arXiv metadata where available.
* Priority search (research subagent; arXiv API "Erdos-Straus", "unit fractions 4/n", "Egyptian fractions"; web searches
  on square sieve/Kloosterman/Erdős–Straus counts, almost-all lower bounds, @brianakaka): no prior or concurrent result
  for (a) a pointwise bound below n^{1/3} for R or any Type II family, (b) an unconditional genus main-term lower bound,
  (c) an almost-all (log p)² lower bound. ArXiv ES papers 2024–2026 skimmed (2610.32302, 2609.09204 [withdrawn],
  2511.07465, 2508.07383, 2505.08716, 2502.20935, 2404.01508) are constructive/congruence approaches. The X post by
  @brianakaka ("density-one lower bound for strict Erdős–Straus solution counts", seen only as a search snippet in z53) could
  not be opened; possible concurrent claim, unverified. The paper therefore states only that the search found nothing and
  makes no stronger priority claim.
  **Superseded by the cross-model review (below):** the X-post lead is the public Zenodo record 22754703 (Akaka, v0.7),
  already archived in the repository and discussed in `LITERATURE_2026.md` §2.4. The "search found nothing" account was
  untenable for almost-all lower bounds; the paper now cites and compares that preprint.

## Referee report (hostile, deep mode; verbatim)

# Verdict: MINOR REVISION

I find no fatal gap in the principal proofs after re-deriving the square-sieve/Poisson estimates, the Burgess–hyperbola argument, and the Bombieri–Vinogradov variance calculation. In particular, the constants in Theorems B and C survive scrutiny. There are nevertheless demonstrably false ancillary statements, an incorrect exponent-pair attribution, and several scope and presentation defects to correct. The paper clearly distinguishes the genus density from the actual count and does not prove or claim to prove Erdős–Straus. This verdict is not certification of literature-wide novelty: I checked the accessible primary sources specified below, not every cited book or earlier paper. Locations and numbering below follow the current TeX/PDF, where the strip proposition is **3.11**, not 3.7.

## Issues

1. **MINOR — §3.8, immediately before Theorem 3.14 (TeX 844): incorrect exponent-pair ancestry.** The assertion `$(\frac16,\frac23)=A(0,1)$` is false. With the standard A-process, \(A(k,l)=(k/(2k+2),l/(2k+2)+1/2)\), so \(A(0,1)=(0,1)\). The required identity is \(A(1/2,1/2)=AB(0,1)=(1/6,2/3)\). This is directly checkable against Trudgian–Yang, §1.2, equations (1.10)–(1.11). **Fix:** replace the displayed ancestry; the exponent-pair application itself survives.

2. **MINOR — Abstract and §1.1 (TeX 47–48, 103–115): the Type II description needs its coprimality qualification.** “These form one line inside the Type II solutions” is not true for arbitrary composite \(n\). For example, \(n=6\), \((u,B,C)=(1,1,2)\) gives \((x,y,z)=(2,12,12)\), which is not Type II because \((x,n)>1\). **Fix:** say that the construction lies in the Type II parametrising variety and gives Type II solutions when \((n,uBC)=1\), automatically for prime \(n\). Also, ET equation (2.22) sends \((a,b,d)=(u,B,C)\) to \((uBC,nuC,nBC)\); for the paper’s displayed *ordered* solution use \((a,b,d)=(B,u,C)\), or explicitly interchange the last two denominators.

3. **MINOR — §1.3 and Lemma 2.2 (TeX 189–195, 350–351): domain and proof defect in the pair description.** “For a prime \(p\)” must mean an **odd** prime: \(R(2)=1\), whereas the opposite-parity pair set \(\mathcal P(2)\) is empty. In Lemma 2.2 the final parenthesis invokes \(C\) and the equation of a solution while proving a statement for *every* pair in \(\mathcal P(p)\), including pairs not yielding solutions. **Fix:** restrict the introductory identity to odd primes, and use \(4uB-u-B\ge2uB\), hence \(u,B\le p/2<p\), directly from membership in \(\mathcal P(p)\). Likewise extend the definition of \(N(n)\) in §5.1 to all positive integers, or omit \(p=2\) consistently from its moments.

4. **MINOR — §1.3 (TeX 224–226), Proposition 4.10: an asymptotic formula is advertised as exact.** “An exact evaluation of each genus slice as a signed sum of products” overstates Proposition 4.10: it has an additive \(O(p^{-\delta})\) error, applies only to specified short squarefree \(u\equiv1\pmod4\) slices, and its principal contribution contains \(L'\) and \(H'\), not merely products of values. **Fix:** say “a uniform asymptotic formula, with power-saving additive error, for these slices,” retaining the explicit restrictions and derivative terms.

5. **MINOR — §1.4 and §7(1), §7(4) (TeX 260–261, 1824–1826, 1843–1844): the full mean of \(R\) is asserted without a supporting result.** The phrases “the mean of \(R\)” and “whose mean over primes is of order \((\log p)^2\)” go beyond the proved truncated-count mean. ET Theorem 1.1 establishes the mean order of the *full Type II count*, not this slice. The numerical coefficient \(3/(2\pi^2)\) is described as “expected” but never derived. **Fix:** supply a proof or an exact reference for the full-\(R\) mean-order assertion; otherwise call it the predicted order. Identify \(3/(2\pi^2)\) explicitly as a heuristic prediction and explain its density model. Theorem C does establish the corresponding lower bound on the mean, but not the missing upper bound.

6. **MINOR — §7(3) (TeX 1838–1841): the proposed implication to exponent \(1/4\) is unsupported.** “An upper bound \(R(n)\ll n^{1/4+\varepsilon}\) would follow from such an estimate together with the cube analysis” does not follow from the estimates proved. The cube analysis itself gives \(17/54>1/4\); even the conjectural pair \((0,1/2)\) gives the cube exponent \(5/18>1/4\). Improving only the balanced block therefore leaves a larger obstruction. **Fix:** remove the implication, or specify a new estimate covering the cube and every intervening block and give the resulting optimisation.

7. **MINOR — Cited Theorem 4.3 and bibliography [HLMLT] (TeX 989–1000, 1876–1878): the effective reference does not cover the entire stated parameter range.** HLMLT Theorem 1.2 uses constants tabulated for \(r\ge2\), whereas the paper states the input for \(r\ge1\) and Theorem 4.12 permits \(r=1\). The \(r=1\) estimate is true, effectively, by Pólya–Vinogradov, but is not supplied by that explicit theorem. **Fix:** separate that case and cite/prove the elementary effective bound. Specify arXiv:2511.17778v2 for the quoted \(10^{1143}\) threshold; v1 has \(10^{1145}\). Correct the author order to Hasanalizade, Lin, **Luna Martínez, Martin**, Treviño. No ineffectivity enters Theorem B through this repair.

8. **MINOR — §1.6 (TeX 298–300): the cited power-sieve example concerns higher-dimensional covers, not curves.** The sentence describes the combination as a technique “for counting points on curves” and cites Heath-Brown–Pierce. The cited paper’s stated results concern smooth cyclic covers of \(\mathbb P^{n-1}\), with \(n\ge10\), not a curve-counting theorem. **Fix:** replace “on curves” by “on higher-dimensional varieties,” or supply an actual curve reference. The attribution of the power-sieve/\(q\)-van-der-Corput combination itself is supported by the source.

9. **MINOR — Lemma 5.9 proof (TeX 1687–1690): a displayed infinite sum is divergent as defined.** After defining \(g(t)=\log(Y/(td))/t\), the integral comparison is written with `\sum_{j\ge1}g(u_0+jd)`. Beyond \(Y/d\), this function is negative and the infinite sum diverges to \(-\infty\). The argument plainly needs the preceding finite sum. **Fix:** write \(\sum_{j=1}^{J}\), or define \(g(t)=t^{-1}\log^+(Y/(td))\). With that correction the integral comparisons and the stated constants hold.

10. **MINOR — §6, slice-validation claim (TeX 1806–1811): the stated test population is impossible literally.** The claim describes eighteen slices with \(X_u\ge10^5\), “including the fourteen primes above.” But \(X_u\le(p+1)/6\); for instance \(p=409\) permits no such slice. Several other listed primes also cannot occur in that long-slice population. **Fix:** list the eighteen actual \((p,u)\) pairs, or distinguish the full candidate-prime sample from the subset passing the length cutoff. Do not imply all fourteen exceptional primes passed that test.

11. **NIT — §1.7, §4.3 and Remark 5.11(1) (TeX 312–313, 1003–1006, 1767–1770): notation and dependencies.** “The letters \(\ell\) and \(q\) always denote primes” contradicts \(q=4uB\), arbitrary BV moduli, and integer Poisson frequencies \(\ell\). The scalar Burgess exponent \(\tau\) is used alongside the divisor function \(\tau(e)\); this is decipherable but needlessly hazardous. Finally the fixed-progression exceptional-set bound suppresses its \(\eta^{-2}\) dependence. **Fix:** make the prime convention local, rename the Burgess exponent, and write \(O_W(\eta^{-2}\pi(X;W,b)/\log X)\). Define \(\log^+\) when first used.

## Verified as correct

- **§§2–3:** the elementary identities and odd-square obstruction; square-sieve support and zero-discriminant removal; complete-sum degeneracies, CRT and Kloosterman reduction; Poisson signs and normalisation; all five strip-bound terms. Intervals shorter than one are covered by the added trivial term. Shiu’s original Theorem 1 permits both applications. The exponent-pair phase has the required derivative shape and, in Case 2, the requisite large parameter.
- **Upper exponents:** independently checked the affine optimisation and ran the bounded SymPy checker: \(74/225\), \(12/37\), cube \(17/54\), \(4/(13-4\kappa)\), \(21/65\), and limiting \(4/13\) agree. Bourgain Theorem 6 and Trudgian–Yang §1.1 support the stated phase-class interpretation, subject to the attribution correction above.
- **§4:** local genus factors; primitive conductors \(4^jd\) and \(4^{1-j}(u/d)p\), including omitted Euler factors; both hyperbola identities and tail bounds; uniform power savings and cancellation of constant terms; the nonsquare contribution to the \(u\)-average; Proposition 4.10’s Euler factors and derivative signs; Theorem 4.12’s progression decomposition. The optimisations give \(2/(3\pi^4)\) and \(121/(640\pi^4)\). Fixing the Burgess parameter before taking \(p\to\infty\) preserves effectivity; no Siegel lower bound is used.
- **§5:** compatible CRT classes stay at level \(Q^2\); weighted BV errors, including logarithmic exponent 170, are sufficient. Primitive-character variance, one-cell structure, and the corrected hyperbolic estimate give the stated variance constant. The final ratio is \(2048\zeta(2)/9=374.313885\ldots<375\), so Chebyshev and the discarded small primes do justify **\(c_0=1600\)** with an ineffective threshold.
- **Sources and computations:** directly checked the relevant ET statements and parametrisation, Bright–Loughran Corollary 1.4, Elsholtz–Planitzer Theorem 1, Shiu Theorem 1, Titchmarsh Theorem 5.11, IK’s Kloosterman theorem, Bourgain Theorem 6, and HLMLT v2 Theorem 1.2. Memory-bounded, timed runs reproduce all fourteen zeros below \(10^7\), odd-square vanishing there, and the quoted genus values at 409 and 8813281. Bounded all-cell checks of Lemma 5.9 also pass. The balanced-block discussion is explicitly labelled heuristic, and the limitations concerning prescribed primes are stated honestly.

## Responses

All issues accepted and fixed in the TeX (numbering as in the report).

1. **A(0,1).** Fixed: "(1/6, 2/3) = AB(0,1) = A(1/2, 1/2)", citing GK Ch. 3 and Trudgian–Yang §1.2.
2. **Type II only for gcd(n, uBC) = 1.** Fixed in abstract ("for prime n …") and §1.1, with the counterexample n = 6,
   (u,B,C) = (1,1,2) ↦ (2,12,12). ET correspondence corrected to (a,b,d) = (B,u,C), which gives exactly the ordered solution
   (uBC, nBC, nuC) via ET (2.22).
3. **Odd prime / pair-form proof.** §1.3 now says "odd prime". Lemma 2.2's final step now uses 4uB − u − B ≥ 2uB, hence
   u, B ≤ p/2, directly from membership in 𝒫(p). N(n) in §5.1 is now defined for all n ∈ ℕ (p = 2 is harmless).
4. **"Exact evaluation".** Replaced by "a uniform asymptotic formula, with power-saving additive error, for the genus layer of
   each short slice u ≡ 1 (4) squarefree, u ≤ p^{3/5−ε}, as a principal term (involving L(1, χ_{−4up}) and L′) plus a signed sum
   of products of two quadratic L-values"; abstract reworded the same way.
5. **Mean of R.** §1.4 now proves the order: the number of triples with 4uBC − u − B ≤ X lies between #{uBC ≤ X/4} and
   #{uBC ≤ X/2}, so the average over all n ≤ X is ≍ log²X; over primes, Theorem C gives the lower bound only. §7(1) and
   §7(4) reworded; 3/(2π²) is called "heuristically predicted" and its density model (Σ 1/φ(4uB) over 𝒫(p)) is named.
6. **n^{1/4} implication.** Removed. §7(3) now says that even under the exponent-pair conjecture the cube gives n^{5/18}, so
   n^{1/4} would need new ideas in every block.
7. **Burgess input.** r = 1 is now attributed to Pólya–Vinogradov; HLMLT is cited for r ≥ 2 with "(in v2)" and the v2
   threshold, and the bibliography entry is arXiv:2511.17778v2. *Author order:* we keep the order of the arXiv metadata
   (Hasanalizade, Lin, Martin, Luna Martínez, Treviño), which is what `arxiv.org/abs/2511.17778v2` lists; if the PDF title
   page orders them differently this should be rechecked before any external use.
8. **Heath-Brown–Pierce.** Now "used to count rational points on cyclic covers of projective space".
9. **Lemma 5.9 divergent sum.** Now Σ_{j=1}^{J}.
10. **Slice-validation population.** Now: 65 slices, u ∈ {1,5,13,21}, twenty primes from 409 to ≈ 10⁸; the eighteen slices
    with X_u ≥ 10⁵ involve the primes 712321, 1000033, 1134241, 1724209, 1726201, 5212561, 8813281, 10000169, 99999989,
    100000049 (six of which have R(p) = 0), extracted from `data/z53/genuslval/slice_checks.txt`.
11. **Notation.** The global "ℓ and q are primes" convention is removed and replaced by local conventions (§3.3: q, q′ odd
    primes, ℓ ∈ ℤ a frequency; §4: ℓ prime). The Burgess exponent is renamed ϖ = (r+1)/(4r) + rε throughout §4 (τ is now only
    the divisor function). Remark 5.11(1) shows the η⁻² dependence. log⁺ is defined in §1.7.

Additional change: the balanced-block remark now says the gain region (4/13, 14/41) on the diagonal is "a computation with
the exponents" of the proof (rechecked numerically).

## Status

* Bankable (as stated in the paper, relative to the cited classical inputs): Theorems 3.8, 3.12, 3.14 (general pair; Bourgain
  instance relative to his Thm 6), 4.8 / Theorem B, Prop 4.10, Thm 4.12, Theorem C.
* Not claimed: ES; R(p) ≥ 1 at any prescribed prime; any bound for X(p) = R(p) − M_gen(p) beyond Thm 4.12's density statement;
  the balanced-block barrier (heuristic remark only); priority beyond "the search found nothing".
* Not externally refereed. Nothing has been posted.


## Cross-model referee (`paper/es-count-note.XREFEREE.md`, MAJOR REVISION) and responses

Verdict: all proofs CORRECT (Thm 3.14 CORRECT-WITH-FIX); major revision for the missing literature comparison.

**Required 1 — Akaka, Zenodo 22754703 (v0.7, 14 Sep 2026), Theorem 1. Done.** Read the archived PDF
(`sources/lit2026/akaka-zenodo-22754703-v0.7.pdf`, §§1–5). Changes:
* Abstract: the sentence "improves the almost-all exponent 0.549 of Elsholtz–Tao to 2 for the solution count" is removed and
  replaced by: for the full Type II count Akaka has claimed (unrefereed) the stronger bound ≫ (log p)³ by a related
  variance/BV method; that claim concerns a different, disjoint subfamily and does not bound R(p).
* After Theorem C: its content is the bound for the line R; as a statement about f_II or f it is superseded, if correct,
  by Akaka Thm 1.
* §1.4: new paragraph "Comparison with Akaka's preprint": statement of his Thm 1 (R_II(p) ≥ c(log p)³ off O(N/(log N)⁴)
  primes, strict x < y < z), labelled unrefereed / declared AI-assisted / Lean certificate claimed / not checked by us /
  nothing depends on it; it gives a smaller exceptional set and the true order of f_II. **Disjointness (proved in the
  text):** his family is y = pM, M = 3abu, s = 3a²u, coprime a < b, recovered by M = y/p, s = (4M−1)x − pM, so 0 < s/M = a/b < 1;
  for a triple counted by R(p) this decoder gives s/M = B or u (an integer), so the families are disjoint and a bound for his
  count or for f_II gives none for R. Method comparison: shared truncation to small moduli, primitive-character variance
  over the unit group (his (10) ↔ our Lemmas 5.6–5.7), weighted BV with a divisor-moment multiplicity budget (his Lemma 4 ↔
  our Lemma 5.5); different variance bound (his conductor ranges: Pólya–Vinogradov / determinant collisions / gcd sums;
  ours: one hyperbolic cell per residue class, Lemmas 5.8–5.9).
* §1.6: search account rewritten (no earlier bound below n^{1/3}, no genus result; for almost-all bounds the related item
  is Akaka, which claims more for the full Type II count and nothing for R; no earlier almost-all bound for R itself
  found; "bounded search, not a priority certificate").
* §7(4): the full-Type-II cubic bound is no longer presented as an untouched target; it is "claimed by Akaka; an
  independent check would be worthwhile".
* Bibliography: entry [Akaka] with Zenodo URL, "unrefereed, declared AI-assisted".

**Required 2 — Thm 3.14 rounding. Done.** a = c₀/Q ∈ (0,1] for 1 ≤ c₀ ≤ Q; for W/Q ≥ 1, N = ⌈W/Q⌉ ≤ 2W/Q gives
y/N² ≥ ℓn/(16W²) ≥ n^c/4 ≥ 1; W/Q < 1 (and N < N₀) handled by the trivial bound. No exponent changes.

**Required 3 — overclaims. Done.** §6: the three variance values are now "consistent with V of order log³Q …; three
samples do not establish the order". §7(4): "would require control of correlations at larger level" replaced by a list of
possible routes (remove weights, add fibrations, enlarge truncation — only the last needs correlations beyond level
X^{1/2}).

**Required 4 — HLMLT author order. Done.** Now Hasanalizade, Lin, Luna Martínez, Martin, Treviño (title-page order of v2);
this reverses my earlier response to referee item 7.

**Minor comments.**
* 65-slice percentages not reproducible from the adjacent check files: agreed; §6 now names the generator
  `scripts/z53_genuslval_slice.{c,py}` (needs PARI/GP), its output `data/z53/genuslval/slice_checks.txt`, and says it was not
  regenerated for this note. The claim stays labelled as an internal sanity check, not a result.
* "Theorem D" vs number 4.12: the paper never uses the letter D in text; it refers to Theorem 4.12 throughout and the
  scope sentence reads "Theorems A–C and 4.12". The name "Theorem D" occurs only in this review file (name map above).
* Keep the corrected Type II qualification, odd-prime domain, slice wording, derivative terms, heuristic balanced-block
  remark: kept unchanged.
* Access limits (IK Thm 17.1, GK Thm A.6 via restatements; Heath-Brown Thm 1 not accessed but Lemma 3.2 is proved in full):
  noted; no change needed.

Status after this revision: the bankable list above is unchanged, except that Theorem C is now positioned as a statement
about the line R only; its consequence for f_II and f is (if Akaka's claim is correct) superseded.

## Round 2 (response to `es-count-note.XREFEREE2.md`, MINOR REVISION)

Checked against the archived Akaka v0.7 PDF (`sources/lit2026/akaka-zenodo-22754703-v0.7.pdf`): eq. (1) p.1 defines
R_II(p) as the count of **all** strict Type II triples x<y<z, p|y, p|z, p∤x; §2 (3)–(6) defines the parameter family and
decoder; (7) p.3 states F(p) ≤ R_II(p) for p > Q₀. LITERATURE_2026.md §2.4 agrees.

**Required 1 — full count vs auxiliary family. Done.**
* Abstract: "that claim concerns a different, disjoint subfamily" replaced by: the claim gives no lower bound for R(p);
  his proof counts an auxiliary subfamily of Type II solutions, and it is this construction (not the full Type II family)
  that is disjoint from the line R.
* §1.4 comparison paragraph: "his count is restricted to the family" removed. New text: the full counts are **not**
  disjoint — since 4uBC−u−B is symmetric in u,B and B≠u at odd primes, ordering the two p-divisible denominators maps
  R-triples two-to-one into R_II-triples, so R(p)/2 ≤ R_II(p). His proof obtains the lower bound for R_II by counting the
  auxiliary family F of [Akaka, §2, (7)], F(p) ≤ R_II(p); its decoder has 0 < s/M = a/b < 1, whereas for x=uBC it gives
  s/M = (4BC−1)u−p = B (y=pBC) or u (y=puC). So the construction used in his proof is disjoint from the line R, and a lower
  bound for F(p) (or f_II) gives none for R(p). Theorem C unchanged.

**Required 2 — no implied two-sided almost-all estimate. Done.** §1.4 "it gives the true average order of f_II for almost
all primes" → "an almost-all lower bound for f_II on the scale of its known mean". §7(4) "(its true average order)" →
"(the order of its mean)" for consistency.

**Required 3 — sentence splice. Done.** §6: dangling "So the bound of" deleted; "whose constant is then about 70 times too
large" → "whose upper-bound coefficient is about 70 times the observed ratios".

**Other report items.** Reproducibility note (historical 65-slice PARI experiment not regenerated) already stated in §6; no
change. No other changes; mathematical content of all results unchanged. Rebuilt with two `pdflatex` passes: 25 pages, no
undefined references/citations.
