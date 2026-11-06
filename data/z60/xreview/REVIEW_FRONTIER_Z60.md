# z60 FRONTIER / summary consistency review

**Verdict: ACCEPT-WITH-FIXES. ES is OPEN.** Reviewed `side-agent/z60-summary` at
`99bd3828bd967d3da981182e84b30c4165be9513` against main at
`0be0402eadb7d79b22864898cd454947df24cac9`: both export files, all eight final
`Z60_<LANE>.md` memos and corresponding `data/z60/xreview/REVIEW_<LANE>.md`, and
`/home/pasky/projects/math/z52bbriefs/z60_summary.md`. Checked the retained z58/z59
qualifications as well. Locations below refer to that export snapshot; **S** means
`Z60_SUMMARY.md`, **F** means `FRONTIER.md`. Review filenames below are under
`data/z60/xreview/` unless specified otherwise.

The central outcome is supported: no HOT LEAD, no positivity mechanism, B2 unchanged,
and all named ES-related conjectures remain open. The principal census totals agree
with the memos. The corrections concern lost hypotheses, finite-versus-eventual scope,
several misattributed counts, and review caveats that did not survive compression.

## Corrections — priority ordered

1. **P1 — Restore the non-square restriction in the U₇ and U⁽⁸⁾ zero counts.**
   - **Location:** S:31,75,105–106; F:349–350,892.
   - **Current:** “zeros ≤ 10¹⁰ exactly Z₇”; “All odd n ≤ 10⁸: zeros exactly Z₇”; “no zero” in the n ≡ 1 (4) extension; “547 zeros n ≡ 1 (4) ≤ 10⁸”.
   - **Corrected:** “The odd non-square U₇-zeros ≤ 10¹⁰ are exactly Z₇. Among odd non-squares n ≤ 10⁸ the zeros are exactly Z₇; there is no non-square zero with n ≡ 1 (4) in (10⁸,10¹⁰]. U⁽⁸⁾ has 547 non-square zeros with n ≡ 1 (4), n ≤ 10⁸.” Keep the skipped-square counts separately. Also qualify S:75's “U₇-zeros = Z₇” as “odd non-square U₇-zeros ≤ 10¹⁰ = Z₇”.
   - **Source:** `Z60_LOPEZ.md:239–242,259–271`, Lemma 7(ii) and the explicitly non-square conjecture/census; `REVIEW_LOPEZ.md:37–40`; `Z59_CONV2.md:49`. Every odd square is a zero; skipping it computationally does not remove it from the mathematical zero set.

2. **P1 — The L-value disjunction requires W = 0, not just the full line span.**
   - **Location:** S:66,168–169; F:765–766,2448–2449.
   - **Current:** “for the full line span: some exceptional G_φ”; “CONDITIONAL on the W1′ dictionary and the full line span”; “with full line span: (𝒟_N)”.
   - **Corrected:** “Under W1′'s nonzero-L-anchor/(H2) hypotheses, with Λ the full span of the exceptional lines **and W = 0**, S(p) ∉ W becomes (𝒟_N): for every prime p ∈ 𝒞₁ above the stated threshold, there exists an exceptional G_φ (possibly depending on p) with L(½,G_φ ⊗ χ_p) ≠ 0. In general the criterion is a linear condition on signed square roots of central values, not their mere nonvanishing.” Retain the independent-validity requirement.
   - **Source:** `Z60_SIGNED.md:319–329`, S5 consequence 3; `REVIEW_SIGNED.md:19`. Nonzero S(p) may still belong to a nonzero W. The omitted hypothesis is explicitly required by the lane review. Preserve ∀p ∃φ, not one φ nonvanishing at every prime.

3. **P1 — Restore the theta-class scope and the negative alternative of S1–S3.**
   - **Location:** S:35–38,66 (especially “Killed”),89–91; F:843–845,1491–1493.
   - **Current:** “in weight 3/2 the signed form of T1 … is as strong as the support form”; “signed proxies … on squarefree 𝒞₁: only Gauss-exceptional components survive”.
   - **Corrected:** “For fixed-level theta-class proxies (finite real combinations of positive-lattice theta series plus cusp forms), in weight 3/2 with one or finitely many quadratic ψ, and weight ≥ 5/2 with one ψ, signed T1 forces either eventual negativity at all 𝒞₁-primes, or the support-form structure, with only Gauss-exceptional components remaining on squarefree 𝒞₁.” Use this scoped dichotomy in the short checklist and dead-end formulations too.
   - **Source:** `Z60_SIGNED.md:48–52,71–79,111–112,195–205,447–452,475–476`; `REVIEW_SIGNED.md` S1–S3 audit. Case E(1) < 0 can be a valid but useless signed minorant; it does not have vanishing genus part. Non-genus Eisenstein/general polynomial-growth objects are not classified here.

4. **P1 — Do not reintroduce the universal varying-level necessity removed in z59.**
   - **Location:** S:66; F:769–770,2450.
   - **Current:** “varying level (needs q ≥ n_p, B2)”; “needs a level prime q with (p/q) = −1, q ≥ n_p”; “varying level (B2 / n_p wall)”.
   - **Corrected:** “Varying/adaptive levels remain open. For the termwise recipe-lattice/off-𝒞₁ strategy, reaching a hard prime outside the level's square class requires an odd level prime q with (p/q) = −1, hence q ≥ n_p. This is not a necessity theorem for arbitrary signed or multi-eigensystem proxies.”
   - **Source:** retained F:719–722,2423–2432; `data/z59/xreview/REVIEW_FRONTIER_Z59.md`, correction 15; `Z60_SIGNED.md` S5 and §7.1. SIGNED's informal §7.1 shorthand is itself too broad; its formal results do not supersede the older qualification.

5. **P1 — Finite numerator-8 failures constrain claimed ranges, not every eventual proof.**
   - **Location:** S:75,81,95–96,162,174; F:891–896,2441–2442,2457–2458.
   - **Current:** “a proof of the P*-form must use g ≡ 3 (8) or a non-liftable divisor”; “witnesses … are forced by S₈”; “Parity-blind orbit … and trace … certificates transfer verbatim to R₈ and are screened out there”; unqualified U₇ extra-target requirements alongside (MS-U₇).
   - **Corrected:** “At an S₈-zero prime included in the theorem's range, an S₄/P* witness must use g ≡ 3 (8) or a non-liftable **U5** divisor (on B4, the shift divisor is odd). An eventual claim may instead exclude these finite failures by its threshold. Likewise a transported C-even positivity claim is refuted only if its asserted range contains a certified R₈ zero. The examined orbit completion bounds also fail for the C-even target; the per-C trace identity alone does not imply that an existential all-C argument transports to even C. Eventual C-even positivity remains open. The full CONJECTURE U₇ must use targets outside U⁽⁸⁾ at its in-domain U⁽⁸⁾ failures; this finite screen alone imposes no such requirement on (MS-U₇), which starts above 10¹⁷.”
   - **Source:** `Z60_LOPEZT.md:95–100,190–195`; `Z60_TRACE.md:258`; `REVIEW_TRACE.md:59`; `REVIEW_MS105T.md` F2; retained F:874–889; `Z59_CONV2.md:49`. Do **not** remove the odd-C requirement for the fixed-threshold (MS⁺₁₀₅) at S:166/F:2444: the certified in-𝔐 R₈ zeros near 10¹⁰ are coprime to 105 and above 29 210 401, hence in that conjecture's domain. They justify that requirement; the 281 large UNK alone would not. S:162's composite warning concerns an extension to composites, not a prime-only theorem whose domain excludes them.

6. **P1 — Restore n ≡ 1 (4) in the orbit's Jacobi-sign statements.**
   - **Location:** S:68 (Lemma 2 and Prop 6),81; F:805,846–847.
   - **Current:** “hits in the χ_n = −1 coset”; “Σ χ_n(x)1_T = −R°(n)”; “the hits of the DYNAMICS orbit lie in the χ_n = −1 coset”.
   - **Corrected:** “For n ≡ 1 (4), orbit hits lie in the χ_n = −1 coset and Σ_x χ_n(x)1_T(x,x̄) = −R°(n). The negative-character coset is empty iff n is a square.”
   - **Source:** `Z60_DYNAMICS.md:86–93,211–214`; `REVIEW_DYNAMICS.md` Lemma 2/Prop 6 audit; retained F:740–741. Direct counterexample without the hypothesis: n = 19 has (u,B,C) = (2,3,1), hence x = 7 and (7/19) = +1. The summary even compares target mass at 10007 ≡ 3 (4), so a blanket QNR statement is misleading there.

7. **P1 — Scope the ring-class criterion to p ∤ 4C and all coprime ideals.**
   - **Location:** S:67; F:791–793,924–927; preserve this qualification in the abbreviated §6 claim at F:1502–1503.
   - **Current:** “event class-determined in some order only if C ∈ {1,2,3,6}”; “Ring classes of one imaginary quadratic order decide the event only for C ∈ {1,2,3,6}”.
   - **Corrected:** “For prime n = p with p ∤ 4C, the indicator [N𝔞 ≡ −1 (mod 4C)] on **all ideals coprime to the modulus and conductor** can be class-determined in some order only if C ∈ {1,2,3,6}, and even then not necessarily. The residue information is at most the real-character shadow GV_C. This does not exclude additional information on the particular divisor set of a fixed β.”
   - **Source:** `Z60_RAYCLASS.md:136–143,171–175`; `REVIEW_RAYCLASS.md:16,33,63`. Without p ∤ 4C the general criterion also allows −1 ∉ G_M, when the indicator is identically zero; p = C = 5, K = ℚ(i), is an example. The all-ideals/divisor-set caveat was specifically required for export.

8. **P1 — Keep the quantitative orbit-margin hypotheses and define the ratio.**
   - **Location:** S:68,199–200; F:803–804.
   - **Current:** “CONDITIONAL (Γ\G rate p^{−1/2+θ}, θ = 7/64, Sobolev norm, compact support): margin/rate ≤ p^{−1/6−θ+o(1)}”.
   - **Corrected:** “CONDITIONAL on a Γ\G rate ε ≍ p^{−1/2+θ+o(1)}, θ = 7/64, with an L²-Sobolev norm S ≥ c_K‖·‖∞ on a **fixed compact K**, and a certificate supported in K, normalized by max_hits f = 1: the relative margin (∫f − εS(f))/(εS(f)) is ≤ p^{−1/6−θ+o(1)}/c_K. The resulting orbit-hole condition is necessary, not an impossibility theorem.” Name the fixed support and normalization in the do-not-export item too.
   - **Source:** `Z60_DYNAMICS.md:160–176`; `REVIEW_DYNAMICS.md:51` explicitly requires these hypotheses in every quantitative export. Merely saying “compact support” permits K to vary with p; an undefined absolute margin can be rescaled.

9. **P1 — Update the stale largest in-𝔐 R₈ zero and qualify the level.**
   - **Location:** S:79.
   - **Current:** “an R₈ version of S5 must start above 10 868 474 401 (largest in-𝔐 R₈ zero)”.
   - **Corrected:** “For levels whose 𝒞₁ contains 𝔐, an R₈ version of S5 effective for p > P₀ requires P₀ ≥ 23 296 553 281, the largest currently certified in-𝔐 R₈ zero. This is a lower bound on a possible threshold, not positivity above it.”
   - **Source:** retained F:864–879; `Z58_SUMMARY.md:81,185`; `Z58_DISPROOF.md` §4. `Z60_SIGNED.md:492–498` and its review inventory discuss only the original twelve-prime screen. The additional z58 zeros 20 840 951 041 and 23 296 553 281 are both in 𝔐. Arbitrary levels need not include these primes in 𝒞₁.

10. **P2 — Prop 4.2 is an Artin product identity, not an exclusion of all other relations.**
    - **Location:** S:67; F:795–796.
    - **Current:** “CFT relations on β's factors are total-product relations”.
    - **Corrected:** “Prop 4.2 proves Artin total-product identities for abelian extensions whose conductor is coprime to (β). On the odd-r a = 1 branch with even Nβ, the odd-part formula is an elementary norm identity, not Art((β)). No additional forcing relation was found (Assessment); this is not a theorem excluding other relations among individual factors.”
    - **Source:** `Z60_RAYCLASS.md:206–221`; `REVIEW_RAYCLASS.md:19,36,65`. Preserve the E1–E3 escape hatches rather than turning a negative research finding into a universal CFT no-go.

11. **P2 — Do not equate composite López Type A with the A-line.**
    - **Location:** S:31; F:347–348 (and terminology in F:352).
    - **Current:** “U₇ = (★) ∪ (Type A with cd even)” on n ≡ 1 (4).
    - **Corrected:** “On n ≡ 1 (4), U₇ = (★) ∪ (A-line words with cd even). The A-line agrees with López Type A at primes, not at arbitrary composites.”
    - **Source:** `Z60_LOPEZ.md:9–11,241,252–253`; `REVIEW_LOPEZ.md`, required fix 1. The source's detailed lemma says Type A **word**; its compressed summary is loose. López's composite definition admits inherited solutions at squares (4/25 example). The export already acknowledges this in notation/do-not-export, so the equality should use the same terminology.

12. **P2 — The 42-zero count belongs to a union, not to the A-half alone.**
    - **Location:** F:352–353.
    - **Current:** “The f ≡ 3 (8) half of Type A alone would leave the prime 9601 and 42 zeros ≤ 10⁷.”
    - **Corrected:** “The union (★) ∪ (A-line with f ≡ 3 (8)) leaves 42 non-square zeros with n ≡ 1 (4), n ≤ 10⁷, including the sole prime 9601.”
    - **Source:** `Z60_LOPEZ.md:274`, the explicit variant-census row. Its abbreviated opening prose is not a different census of the A-half alone.

13. **P2 — R₈ was run on 106 kernels through 1000, not the expanded R domain.**
    - **Location:** F:366–367,894–895; clarify the abbreviated comparison in S:77 as well.
    - **Current:** “The same R₈ kernel census”; “The R₈ analogue of the MS105 kernel census”, following the s ≤ 10⁵ R census.
    - **Corrected:** “The R₈ control covers the 106 admissible kernels s ≤ 1000 and 6 086 436 506 inputs, not the expanded kernel-≤10⁵ domain. It leaves 281 UNK above 10¹⁰, up to 1.84·10¹⁹ (no C-even witness d ≤ 10⁸; not certified zeros). R has no UNK above 10⁶ on this domain, or on its larger census.”
    - **Source:** `Z60_MS105.md:42–48,78–86`; `REVIEW_MS105.md:48–52`. The larger R census has 11 061 kernels and 67 872 056 404 inputs. S:123–124 already states the smaller R₈ scope correctly.

14. **P2 — Restore n ≡ 1 (4) to MS105T's zero census.**
    - **Location:** S:78,128–129; F:370.
    - **Current:** “361 non-square zeros ≤ 3·10⁷”; “14 full-family prime zeros”.
    - **Corrected:** “For n ≡ 1 (4), n ≤ 3·10⁷: 361 non-square R-zeros and 2739 odd squares; 38 non-square zeros are coprime to 105 (14 primes, 24 composites). The 14-prime list is for p ≡ 1 (4).”
    - **Source:** `Z60_MS105T.md` §0 and its domain; `REVIEW_MS105T.md:57–60`; `scripts/z60_ms105t_zeros.c:1,7–8`. These are not counts over every odd integer/prime. Keep the existing distinction from the separate 38-prime 𝔊* screen.

15. **P2 — Preserve the prime domains of the S₈ and U₇-half counts.**
    - **Location:** S:75,116; F:982.
    - **Current:** “S₈ prime zeros ≤ 4·10⁶: 45”; “two branch halves fail at 14 resp. 12 primes ≤ 10⁸”.
    - **Corrected:** “S₈ has 45 zero primes p ≡ 1 (4), p ≤ 4·10⁶ (same list independently verified through 10⁸). U₇'s B- and A-target halves have respectively 14 and 12 zero primes p ≡ 1 (4), p ≤ 10⁸.”
    - **Source:** `Z60_LOPEZ.md:272–273`; `REVIEW_LOPEZT.md:43,64`. S₈ has 61 zeros over all odd primes ≤ 10⁸, not 45. The export's longer S₈ discussion correctly distinguishes them; the census bullet must too.

16. **P2 — Exchangeability is a limiting prime law, not exact finite-sample symmetry.**
    - **Location:** S:62,183–184; F:357–358.
    - **Current:** “branch vectors exchangeable in law for each fixed X”; “fixed-X exchangeability”.
    - **Corrected:** “For each fixed X, the truncated branch vectors are exchangeable in the **limiting prime distribution** (over 𝔐-primes or p ≡ 1 (24)). This is neither exact finite-sample symmetry, independence, uniformity for growing X, nor rescue at the same prime.”
    - **Source:** `Z60_LOPEZ.md:126–139`; `REVIEW_LOPEZ.md:14,29`. The proof uses the prime number theorem in fixed progressions. The surrounding finite census makes omission of “limiting” particularly misleading.

17. **P2 — Restore the smallest tail sample: ten joint events in T.**
    - **Location:** S:62; F:356.
    - **Current:** “59–107 joint events”.
    - **Corrected:** “59–107 joint events at the deepest a/f thresholds; only 10 in the T-coordinate, so these extreme-tail ratios are rough.”
    - **Source:** `Z60_LOPEZ.md:182`. Keep the dependence reading EVIDENCE and the causal reading a hypothesis; the pooled ratios do not imply positive dependence in every individual stratum.

18. **P2 — Restore the profinite obstruction's parameter hypotheses.**
    - **Location:** S:65; F:779–780.
    - **Current:** “profinite x with x_q = r, q > 3r + 1, x_ℓ = 1 else”.
    - **Corrected:** “For an odd prime q and a positive integer r with q ∤ r and q > 3r + 1, the profinite point x_q = r, x_ℓ = 1 for every prime ℓ ≠ q lies in no good class.”
    - **Source:** `Z60_MS105T.md:96–97`, Theorem 3.2; `REVIEW_MS105T.md` proof audit. In particular positivity of r was lost. Keep the already-correct ∀M ∃ infinitely many p qualification and the limited q = 5,7 example scope.

19. **P2 — State the same-modulus anti-multiplicativity result, with the right coprimality.**
    - **Location:** S:64; F:787–788.
    - **Current:** “coprime d-form hits a, b give a hit ab only if (a/d)(b/d) = −1 (necessary, not sufficient)”.
    - **Corrected:** “For d ≡ 3 (4), if a and b are both d-form hits at the same d, their product is **not** a hit there. More generally, for gcd(ab,d) = 1, a product hit requires (a/d)(b/d) = −1, a necessary but insufficient condition.”
    - **Source:** `Z60_MS105.md:189–197`; `REVIEW_MS105.md:18`. Coprimality is with d, not between a and b; two hits each have sign −1, so their product cannot satisfy the necessary sign. No obstruction to all conditional gluing/descent is proved.

20. **P2 — Correct the near-square search scope and the contradictory “No UNK” sentence.**
    - **Location:** S:121; F:363–365.
    - **Current:** “c ∈ ±{8, …, 200}”; “No UNK in high-m windows …, near squares … (UNK only at 15 known zeros …), all 52 Lehmer pseudosquares … (zeros only 2641,18 001) or locally-square inputs …”.
    - **Corrected:** “High-m windows on the 106 admissible kernels s ≤ 1000 contain 3 876 571 898 inputs to n ≈ 10³⁷, with no UNK. Near squares m² + c, c ∈ ±{8,16,…,200}, odd m ≤ 10⁹, restricted to positive non-squares coprime to 105, have UNK only at 15 known zeros ≤ 1.26·10⁷. Among all 52 Lehmer pseudosquares ≤ 4.24·10²⁴, only 2641 and 18 001 are zeros. The sampled locally-square inputs to ≈ 4·10³⁵ have no UNK.”
    - **Source:** `Z60_MS105.md:53–70`; `REVIEW_MS105.md:50–54`. Windows/samples are not interval completeness to the quoted largest n. The ≈ 8.3·10¹⁰ aggregate is input **occurrences**, not necessarily distinct integers.

21. **P2 — Do not strengthen the rank-5 example to exclusive positivity or proved invalidity.**
    - **Location:** S:192–193.
    - **Current:** “positive only at p ≡ 17 (24), off 𝔐, not valid”.
    - **Corrected:** “Proved positive at every p ≡ 17 (24), a class outside 𝔐; no R-validity is established, nor positivity at all large 𝔐-primes.”
    - **Source:** `Z60_SIGNED.md:224–232`; `REVIEW_SIGNED.md:39–42`. “Every prime in this class” does not mean “only this class”; lack of a validity proof is not a proof of invalidity. F:758's “not shown valid” is already correct.

22. **P2 — The conditional coset result still needs one underlying genus/determinant class.**
    - **Location:** S:66,193; F:759.
    - **Current:** “Cosets: CONDITIONAL on (SWc), class by class only.”
    - **Corrected:** “Coset genus conclusions are CONDITIONAL on (SWc), for one underlying genus/determinant class, and hold class by class only; no global or cusp dichotomy is proved. The termwise-recipe exclusion is also conditional on (SWc).”
    - **Source:** `Z60_SIGNED.md:234–250`; `REVIEW_SIGNED.md:16`. This is another hypothesis explicitly called essential by the lane review.

23. **P2 — Preserve eventual-validity escape hatches in the finite S₁ and L = 420 screens.**
    - **Location:** F:983–984; S:79,194–195.
    - **Current:** “A single-field (d = 1) argument must survive the 160 prime zeros”; “L = 420 … non-zero at other zeros … ⟹ not prime-valid”; the caveat gives numerical/BSD status but no validity-threshold warning.
    - **Corrected:** “An all-prime positivity claim for the specific d = 1 family S₁ is refuted by its 160 zero primes p ≡ 1 (4), p ≤ 10⁷. Eventual S₁ positivity and other single-field methods remain open; any threshold must respect the zeros in its domain. The L = 420 line failures are numerical/BSD-dependent, with line identification EVIDENCE, and do not exclude prime-validity required only beyond a larger threshold.”
    - **Source:** `Z60_RAYCLASS.md:30–39,47,49–51`; `REVIEW_RAYCLASS.md:62`; `Z60_SIGNED.md:422–431`; `REVIEW_SIGNED.md:66–69`. S:139 and S:171 already retain the S₁ eventual-positivity scope; FRONTIER should agree.

24. **P2 — The R₈ genus screen covers the original twelve primes, not all known zeros.**
    - **Location:** S:80.
    - **Current:** “GV holds at 16–38 even levels C ≤ 200 at each R₈-zero prime, hits none”.
    - **Corrected:** “At each of the 12 original R₈-screen primes, GV holds at 16–38 even levels C ≤ 200, with no hits; the two additional z58 zeros were not included in this screen.”
    - **Source:** `Z60_RAYCLASS.md:167–168`; `REVIEW_RAYCLASS.md:46`; retained F:864–870. A sample screen must not silently expand when integrated with a larger known-zero inventory.

25. **P2 — Retain the arithmetic conditions in the compressed exact encodings.**
    - **Location:** F:798–799,905–906; S:85.
    - **Current:** “minus continued fractions of n/A of length 3, [[c,m,s]], 4 | m”; “shell index c … a divisor ≡ −1 (mod c)”; ideal norm “≡ −1 modulo the level”.
    - **Corrected:** “For odd n ≥ 5, R° counts A with 1 ≤ A < n, gcd(A,n) = 1 and minus continued fraction n/A of length exactly 3, [[c,m,s]], 4 | m. A shell hit requires 4 | c and d | cn+1 with d ≡ −1 (mod c), d ≤ n−1 and (cn+1)/d ≤ n−1. In the ideal dictionary for (★) at level C = t₀s², r = 2s, the norm modulus is **4C = t₀r²**, in an order containing β_r.”
    - **Source:** `Z60_DYNAMICS.md:68–81`; `Z60_RAYCLASS.md:84,95–96`. Omitting gcd permits n = 95, A = 35 or 55 despite R°(95) = 0; omitting factor bounds includes the boundary factorization 69 = 3·23 at n = 17,c = 4. “Modulo the level” risks dropping the factor 4 in the (★) dictionary.

26. **P2 — State the weight scope of the TRACE obstruction and its numerical screen.**
    - **Location:** S:69; F:810–813.
    - **Current:** “a worst-case Deligne certificate fires only if the average normalised eigenvalue exceeds …”; “it never fired at C = 2 (n ≤ 3000) or C = 3 (n ≤ 600)”.
    - **Corrected:** “For **odd k ≥ 3**, conditional on Theorem 2/Lemma 3, the worst-case Deligne certificate B = D requires the displayed average condition (with only (k,Q) = (3,4) lacking a ρ-free constraint). The non-firing data at C = 2,n ≤ 3000 and C = 3,n ≤ 600 are for **k = 3**. The explicit refutation of a level-uniform absolute square-root bound is also conditional on Theorem 2, for fixed odd k ≥ 3 and all levels/all n; its n ≡ 5 (8) family is outside the Mordell-hard domain.”
    - **Source:** `Z60_TRACE.md:165–169,188–208,225–233`; `REVIEW_TRACE.md` Cor 4.3 and explicit-family audit. The average formula is not stated for even weights, and the finite screen is not over every weight. The export correctly retains the main conditional identity and finite-versus-universal non-firing distinction; keep those qualifications.

27. **P2 — Reconcile the cross-field information escape with the old parity slogan.**
    - **Location:** F:921–927; S:198, with the Prop 4.1 row at S:67.
    - **Current:** the old checklist says higher-residue-symbol forcing “delivers only the quadratic layer”; the addition says “Cross-field data can carry quartic information … but no forcing relation … is known”; the do-not-export list omits the arithmetic-instance limitation.
    - **Corrected:** “The earlier total-product/forced-progression barriers are scoped forcing statements, not a universal restriction on all information in joint class data. Cross-field class data can carry information beyond the per-field quadratic shadow (Prop 4.1, group theory PROVED). The particular quartic cyclotomic identification is sample-certified only; no (★)-internal configuration was constructed and no forcing relation on individual factors was found.” Add the last sentence to S's RAYCLASS caveats.
    - **Source:** `Z60_RAYCLASS.md:179–204`; `REVIEW_RAYCLASS.md:18,35`; F:483–498 for the actual older barrier scopes. The export should not leave these adjacent statements looking like contradictory universal theorems.

28. **P3 — The MS105 R₈ control did receive a cross-model review.**
    - **Location:** S:188–189.
    - **Current:** “the R₈ control was completed after internal review (not reviewed)”.
    - **Corrected:** “The R₈ control was completed after the internal review and was subsequently checked by the cross-model review; no full census replay was performed.” Keep the overall statement that the post-review fixes were not re-reviewed.
    - **Source:** `Z60_MS105.md:298` is a stale internal-review chronology note; `REVIEW_MS105.md:22,57–59,68` explicitly audits §2.6, independent slices, late witnesses and F2 counts. S:124–126 already describes that later audit.

29. **P3 — Repair short dictionary/numerical abbreviations.**
    - **Location:** S:63,67; F:806–807 (and the general encoding shorthand at S:86/F:906).
    - **Current:** “U5: S iff p or p⁻¹ mod g ∈ −Div((g+1)/4)”; “S₁/L(1,χ₋₄ₚ) Spearman 0.875”; “0.053 (all of R: 0.426; small but nonzero, p ≈ 5.9·10⁻⁶)”; “positive split points”.
    - **Corrected:** “U5: S iff there exists g ≡ 3 (4), gcd(g,p) = 1, with p or p⁻¹ mod g in −Div((g+1)/4).” “Spearman correlation of S₁ with L is 0.875; the non-square-C part of R has correlation 0.053 (p-value ≈ 5.9·10⁻⁶), while all of R has correlation 0.426.” “Positive split or repeated-root points (repeated roots occur only at even n).”
    - **Source:** `Z60_LOPEZT.md:78–87`; `Z60_RAYCLASS.md:260–271`, `REVIEW_RAYCLASS.md:43`; `Z60_TRACE.md:70–76,154–155`. The U5 modulus is existential; the correlation is not a ratio; the p-value belongs to 0.053. TRACE includes n = 2,C = 1, Γ = 3I, not just distinct-root points; “split” alone is sufficient when the statement is explicitly restricted to odd n.

## Checks and limits

Source-number greps confirm the headline totals: U₇'s 7 071 222 859 non-squares and
342 375 LATE certificates; 6 354 932 joint-run primes; the 719 781-prime least-g sample
and record 10487; MS105's 67 872 056 404 inputs, 3 876 571 898 window inputs,
11 361 904 661 near-square occurrences and 321 = 40 + 281 R₈ misses; MS105T's
6275/164736 cover and 3024 square classes; S₁'s 160/25 zeros and 0.875/0.426/0.053
correlations; TRACE's 21 044 local cases and 137/12229 firing count. Their certification
and independent-check coverage must remain as stated, not upgraded to second full censuses.
Small bounded integer checks confirm the n = 19 Jacobi counterexample, the non-coprime
95/A continued fractions, and the quoted census arithmetic. No large census, modular-form
computation or primary-source theorem audit was rerun for this export consistency review.

Independent lane checks were consolidated and their proposed corrections checked against
the cited source passages. The eight-composite exception set, corrected López branch
labels, 14/38/24 screen distinction, polynomial theorem's density-zero/univariate scope,
UNK-versus-zero distinction, conditional TRACE identity, and model-versus-arithmetic labels
are otherwise carried faithfully. In particular the ≈ 4·10⁻³ expected-zero figure is
explicitly a model estimate, not an arithmetic zero bound. Only this review file is changed.
