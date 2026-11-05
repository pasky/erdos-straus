# z59 FRONTIER / summary consistency review

**Verdict: ACCEPT-WITH-FIXES. ES is OPEN.** Reviewed `side-agent/z59-summary` at
`ae2f0281a59cbca822ea30a1093e90e38c0c157f` against main at
`3f56c38f05df19ddbca27916fccfa83a63669767`. Locations below use that export snapshot.
Read all five final Z59 memos, all five cross-model reviews, `data/z59/papers/CHANGES.md`,
`Z58_SUMMARY.md`, FRONTIER §§1–4, 6–7, and `/home/pasky/projects/math/z52bbriefs/z59_summary.md`.
The following are priority-ordered export corrections, not edits to the lane memos.

The principal census totals, U/U⁽⁸⁾ counts, min-ρ records, 13/6 L-zero distinction, repaired
WALDS ambient-space accounting in summary §3, and papers priority/BM changes agree with the
sources. The withdrawn second-order mean is not promoted back into a theorem. No ES proof is claimed.

## Corrections

1. **P1 — Do not identify the full Type II target with the (★) divisor condition.**
   - **Location:** `FRONTIER.md:1312–1314`, final z59 dead-end bullet.
   - **Current:** “`Z59_MSPF.md` §3, `Z59_CONVO.md` §7 … each stops at ‘some n + k has a divisor ≡ −1 (mod 4k)’.”
   - **Corrected:** “MSPF's (★) attempts stop at ‘some n + k has a divisor ≡ −1 (mod 4k)’. CONVO's full Type II attempts stop at the ratio criterion: for some j ≥ 0, (p + 3)/4 + j has positive divisors a,b with ab dividing it and a + b ≡ 0 (mod 4j + 3). These are related tied-divisor problems, not the same positivity statement.”
   - **Source:** `Z59_MSPF.md` §3; `Z59_CONVO.md` Criterion 3.1, §§7–9; `REVIEW_CONVO.md` proof audit/F4. Full Type II succeeds at all 14 (★)-zero primes, so the stated (★) condition cannot be its equivalent target.

2. **P1 — Disambiguate the new U from FRONTIER's existing U.**
   - **Location:** `FRONTIER.md:317`, all new U/(MS-U) references; compare unchanged §§5.1, 6 and §7 item 12; `Z59_SUMMARY.md:12` notation.
   - **Current:** “U := (c = 1) ∪ (a = 1)” without a notation-collision warning. Older passages discuss U/ES₅, the U word sieve and RLD-U.
   - **Corrected:** “Write U_II := (c = 1) ∪ (a = 1) for CONV2's U (and retain (MS-U) as its conjecture label). This is not the older word-family predicate U in the U/ES₅ and RLD-U passages.” Use U_II consistently in the z59 additions, or at minimum explicitly scope the reused symbol at each entry point.
   - **Source:** `Z59_CONV2.md` notation/Lemma 1; `EXSET_BEYOND_CRT.md` §1.3. The distinction is real: at n = 4545 the old U has word (t,u,v) = (7,14,47), since tuv − u − v = 4545, v ≡ −n (mod 8), tv − 1 = 328 < n + v and u ≥ 2. The new U has no witness there. Old U theorems must not silently be read as theorems about the new union.

3. **P1 — W5 is an eventual equivalence, not the fixed-threshold (MS).**
   - **Location:** `FRONTIER.md:654–655`; `Z59_SUMMARY.md:34`, and the W5 caveat in §6.
   - **Current:** “for a proxy effective on a class, validity at large primes of the class ⟺ (MS) there”; “validity ⟺ (MS) on its class.”
   - **Corrected:** “For g effective on a prime class 𝒞, eventual validity on 𝒞 is equivalent to eventual R(p) ≥ 1 on 𝒞. This does not by itself give (MS), which requires every 𝔐-prime p > 10¹⁷: the effectiveness and validity thresholds must both be ≤ 10¹⁷, or the remaining finite interval must be covered.”
   - **Source:** `Z59_WALDS.md` formal Proposition W5 (both sides say ‘all sufficiently large’), `REVIEW_WALDS.md` W5 audit (maximum of two thresholds); existing `FRONTIER.md` §2.4 definition and warning that unspecified eventual positivity does not finish ES. The memo's informal shorthand is also too loose here; export the formal statement.

4. **P1 — Restore the domain and threshold limits of the MS-to-rough-input proof transfer.**
   - **Location:** `FRONTIER.md:305–307`, `2218–2220`; `Z59_SUMMARY.md:148–150`.
   - **Current:** “A proof of (MS) transfers to (R⁺_y) only if every use of primality follows from non-squareness plus the fixed-y exclusion.”
   - **Corrected:** “Reusing an (MS) proof for fixed-y-rough non-squares requires every primality-dependent step to remain valid. This initially gives only the original Mordell domain and original threshold. The all-class (R⁺_y) statement additionally needs removal of any Mordell-class dependence and coverage down to its threshold 8 813 281; the census to 10¹⁰ does not cover a gap up to 10¹⁷. A proof needing y(n) → ∞ is not a proof of (R⁺₄₇).”
   - **Source:** `Z59_MSPLUS.md` §5.2 explicitly says transfer “on 𝔐”; §1 defines the all-class rough conjecture; `REVIEW_MSPLUS.md` required fix 2. Existing FRONTIER §2.4 fixes (MS)'s threshold at 10¹⁷. The gcd(n,u) counterexample is correctly retained, but is not the only transfer condition.

5. **P1 — Restore coprimality in the ρ-coordinate square-kernel statement.**
   - **Location:** `FRONTIER.md:709–711`; also qualify the compressed generalization in `Z59_SUMMARY.md:70–71`.
   - **Current:** “In every coordinate system tried … all odd prime factors lie in the kernel … ker λ_ρ on (m² + ρ)/4”.
   - **Corrected:** “For the U T-system, every odd prime factor of Tm² + 1 lies in ker χ_{−T}. For the ρ-system, with odd m, ρ ≡ 3 (4) and gcd(m,ρ) = 1, all prime factors of (m² + ρ)/4 lie in ker λ_ρ. Non-coprime squares are excluded instead by CONVO Lemma 2.1; the unit-group/kernel argument does not apply to them.”
   - **Source:** `Z59_CONVO.md` Lemma 3.3(i), §8; `REVIEW_CONVO.md` F1 and closing scope instruction. Counterexample even in 𝔐: m = 11, ρ = 11 gives m² = 121 and (m² + ρ)/4 = 33, with prime factor 11 satisfying λ₁₁(11) = 0, not 1. Summary §2's CONVO table already preserves the distinction; FRONTIER must too.

6. **P1 — Narrow the scope of the means no-go, and retain the factor 1/2.**
   - **Location:** `FRONTIER.md:677–678`, `708–709`, `1303–1305`; `Z59_SUMMARY.md:72–73`.
   - **Current:** “Thm 1 … is square-blind and identical for R₈”; “a mean/density step never supplies the non-square input”; “any mean/density mechanism must get its non-square input elsewhere.”
   - **Corrected:** “The fixed-Q leading residue-class coefficient of Theorem 1 is Jacobi-blind. R₈ has the same odd local factors and half the leading coefficient. These leading means alone supply neither non-square discrimination nor pointwise positivity (Assessment). This does not exclude square-sensitive main terms, other density inputs, or additional arithmetic steps.”
   - **Source:** `Z59_MSPLUS.md` Theorem 1, Corollary 1.1(i), Remark 2.3, F1; `REVIEW_MSPLUS.md` leading-mean/F1 scope. Existing FRONTIER §2.2 has M_BM(m²) = 0 and §7 item 4 has a square-sensitive genus lower bound. Thus ‘any mean/density mechanism’ is broader than the result, and ‘identical’ is numerically false for the means themselves.

7. **P2 — MSPF's 186/118/136 counts exclude the nine full-family zeros.**
   - **Location:** `FRONTIER.md:745–746`; `Z59_SUMMARY.md` §2 MSPF row (`:67`) and §3 “Other” (`:122–124`).
   - **Current:** “For 𝔐-primes ≤ 10⁷, C-even solutions are absent at 186 … C-odd at 118”; “R_prime = 0 at 136”; “d_min = q₁ for 22.6 %”.
   - **Corrected:** “Among the 20 504 𝔐-primes ≤ 10⁷ with R > 0, C-even witnesses are absent at 186, C-odd at 118, and prime-d witnesses at 136; d_min = q₁ at 4636/20504 = 22.6 %. Including the nine R = 0 primes, the zero counts are respectively 195, 127 and 145.” Retain the listed maxima, which are correct.
   - **Source:** `Z59_MSPF.md` §4; `REVIEW_MSPF.md` Numerical reproduction. A fresh streaming recount of `data/z59/mspf/primes_M_1e7.txt` gives 20513 total/20504 positive rows and exactly these restricted/unrestricted counts.

8. **P2 — Six structured-search lines are square controls, not successful witnesses.**
   - **Location:** `Z59_SUMMARY.md:120–122`, §3 “Other”.
   - **Current:** “460 000 structured-search lines … all with verified witness, least hit modulus ≤ 211 403”.
   - **Corrected:** “460 000 structured-search output lines were checked, including six square controls marked UNK. Every non-square input has a verified witness, with least hit modulus ≤ 211 403; there is no non-square UNK. These are sampled/structured inputs, not an interval census.”
   - **Source:** `Z59_MSPLUS.md` §4.1; `REVIEW_MSPLUS.md` Computation and exhaustiveness; `data/z59/msplus/struct/EVAL.txt`. Direct inspection of `semi_2.txt.gz` reproduces six UNK lines, all squares. The current wording contradicts T1.

9. **P2 — The rough-target zero count/last zero is for y = 47, not every y ≥ 47.**
   - **Location:** `FRONTIER.md:305–306`, `807–809`.
   - **Current:** “(R⁺_y), y ≥ 47 … (19 zeros ≤ 10¹⁰, the last 8 813 281)”; threshold list “y ≥ 47 → 8 813 281”.
   - **Corrected:** “For y = 47 there are 19 rough non-square zeros ≤ 10¹⁰, last 8 813 281. For every y ≥ 47 the domain shrinks, so the same cutoff is certified sufficient; the count and actual last zero need not remain the same.” In §4, distinguish a sufficient common cutoff from the exact last zero.
   - **Source:** `Z59_MSPLUS.md` §1 and §5.3 table, whose 19/8 813 281 row is explicitly y = 47; `REVIEW_MSPLUS.md` target-row check. Fresh streaming filtering of the z58 zero file reproduces 19 at y = 47 and zero at y = 8 813 281.

10. **P2 — Do not drop the statistical misses and training/covariate qualifications required by review.**
    - **Location:** `FRONTIER.md:314–316`; `Z59_SUMMARY.md` §2 MSPLUS F2 cell (`:66`).
    - **Current:** “zero law … in a proxy m; it matches the four large composite groups within ≈ 1.5×”; “R₈ zero rate ≈ 5× the R-law near 10¹⁰”.
    - **Corrected:** “EVIDENCE: the fitted law uses proxy m, log n and Jacobi depth as separate covariates. Agreement within roughly 1.5× (worst about 1.63×) concerns the four large training groups only; the OOS g21 row is about 3× off and held-out g7 about 17× off. Later total counts are about 1.4–1.5× low, and 𝔐-prime zeros about 6× low. The R₈ comparison is a rough all-p ≡ 1 (4) assessment at the halved mean, not an in-𝔐 calibrated zero law; only four of the twelve original screen primes are in 𝔐.”
    - **Source:** `Z59_MSPLUS.md` F2/F3, §§3.2–3.5; `REVIEW_MSPLUS.md` required fix 4 and F2. Keep the existing ‘no pre-set criterion/not a passed test’ sentence; that part is correct.

11. **P2 — Preserve W4's nonzero-line, in-class and validity conditions; non-vanishing is not coefficient positivity.**
    - **Location:** `FRONTIER.md:651–653`, `1299–1302`; `Z59_SUMMARY.md` §1 WALDS row.
    - **Current:** “for one such line, positivity at a prime p is L(½, G_φ ⊗ χ_p) ≠ 0”; the §6 dead-end repeats the assertion without its hypotheses.
    - **Corrected:** “For p ∈ 𝒞₁(2N), a nonzero single-eigensystem restriction has g(p) ≠ 0 iff L(½, G_φ ⊗ χ_p) ≠ 0, under the nonzero-L anchor hypothesis of W1′ (with nonzero coefficient restriction), or under (H2) with K_φ(g) ≠ 0. Only if g is valid does g(p) ≠ 0 force R(p) > 0. For several contributing eigensystems under (H2), non-cancellation of the sum is required.”
    - **Source:** `Z59_WALDS.md` W1′ and W4(a)–(d); `REVIEW_WALDS.md` W1′/W4 audit. A zero line has no positivity even when an L-value is nonzero. The L-value dictionary controls g(p) ≠ 0, not the sign of a possibly signed or complex g(p).

12. **P2 — CKRS-based eventual failure is restricted to rational eigensystems and a positive-constant class refinement.**
    - **Location:** `FRONTIER.md:661–663`, `1301–1302`; `Z59_SUMMARY.md` §1 WALDS survivor cell and §6 WALDS caveat (`:173–175`).
    - **Current:** “a residue-class refinement of CKRS … predicts infinitely many zeros”; “Eventual single-line effectiveness … false under a residue-class CKRS refinement.”
    - **Corrected:** “For rational G_φ (elliptic curves), a residue-class refinement of CKRS with a positive constant in the chosen class predicts infinitely many prime-twist zeros. This refinement is not stated in CKRS and is CONJECTURE; irrational eigensystems require a further conjectural extension. The thirteen proved zeros concern the explicitly tested conductor-84 twist, not every eigensystem.”
    - **Source:** `Z59_WALDS.md` §4.1 and §6.1; `REVIEW_WALDS.md` CKRS finding and required scope. The summary's ‘rational φ only’ currently qualifies the identification box search, not this separate conjectural claim.

13. **P2 — Restore the fixed non-square core hypothesis to the twisted-T1 lemma.**
    - **Location:** `Z59_SUMMARY.md:39`, §0 scoped no-gos.
    - **Current:** “Lemma 4.1: no positive-density twisted-T1 family s·m² for (★).”
    - **Corrected:** “For each fixed positive non-square s ≡ 1 (4), the odd m with R(sm²) = 0 have density zero among odd m (PROVED). This does not exclude thin infinite zero subfamilies.”
    - **Source:** `Z59_MSPLUS.md` Lemma 4.1 and its following paragraph; `REVIEW_MSPLUS.md` independent proof audit. If s is a square, every sm² is a square and the claimed unqualified conclusion is false. FRONTIER's longer version already retains the essential hypothesis.

14. **P2 — Failure of unconditional scaling closures does not rule out every scaling-based descent.**
    - **Location:** `Z59_SUMMARY.md:150`, §5 item 2.
    - **Current:** “Descents allowed by (MS⁺) would have to be non-scaling.”
    - **Corrected:** “Unconditional product/divisor/q²-scaling closure rules fail. Witness-shape-conditioned scaling and descents using additional hypotheses are not excluded; Lemma 5.1 gives an actual conditional scaling bijection.”
    - **Source:** `Z59_MSPLUS.md` Lemma 5.1 and §7 narrowed verdict; `REVIEW_MSPLUS.md` labels/final assessment. The source still has loose ‘non-scaling’ prose in §5.2, but its formal lemma and repaired verdict support only the narrower export. FRONTIER §6 already says witness-shape-conditioned reductions are not excluded.

15. **P2 — Scope the level-growth barrier to the recipe-lattice/off-square-class strategy.**
    - **Location:** `FRONTIER.md:2224–2226`; `Z59_SUMMARY.md:152–153`, escape (E-e).
    - **Current:** “off-𝒞₁ classes, needing p-dependent levels with some ℓ ≥ n_p (B2 again)”.
    - **Corrected:** “Off-𝒞₁ classes remain open. For a strategy relying on termwise recipe lattices, a fixed finite level menu misses primes ≡ 1 (mod 8∏ℓ). To reach every hard prime by this off-𝒞₁ mechanism needs growing/adaptive levels, with some odd level prime ℓ satisfying (p/ℓ) = −1 (hence ℓ ≥ n_p). This is not a necessity theorem for arbitrary signed multi-eigensystem proxies.”
    - **Source:** `Z59_WALDS.md` W0(b), §7 E-e; `REVIEW_WALDS.md` W0/scope findings. W0 concerns positive ternary lattices and nonnegative mixtures, not every possible proxy.

16. **P2 — Do not demand that a validity identity be logically inequivalent to eventual validity.**
    - **Location:** `FRONTIER.md:2223–2224`; `Z59_SUMMARY.md:152`, §5 item 4.
    - **Current:** “a validity identity not reducible to validity at large primes”.
    - **Corrected:** “a validity identity proved from independent arithmetic or structural input, rather than assumed from the desired eventual positivity; no such identity is supplied. W5 is an equivalence, not a circularity theorem or an exclusion of independently proving an equivalent statement.”
    - **Source:** `Z59_WALDS.md` §4.2 after W5; `REVIEW_WALDS.md` W5 finding. The memo's E-a shorthand should not undo the explicit W5 warning already retained elsewhere in the export.

17. **P2 — Restore threshold qualifications to prime/sub-line screen conclusions.**
    - **Location:** `FRONTIER.md:814–815`; `Z59_SUMMARY.md:155`, §5 item 6.
    - **Current:** “A U-argument at primes must rescue the 14 (★)-zeros”; “prime-only or single-C-parity witness statements need thresholds above 10⁷”.
    - **Corrected:** “A U theorem whose asserted domain includes the fourteen (★)-zero primes must rescue them via a = 1 with 4 ∤ T. (MS-U), starting at 10¹⁷, need not include them. For a statement over p > P in 𝔐, the ≤10⁷ census requires P ≥ 9 831 889 for prime-d witnesses and P ≥ 9 744 001 for C-odd witnesses; for C-even witnesses it gives P ≥ 9 965 881, strengthened by the z58 screen to P ≥ 23 296 553 281. None of these data refutes eventual positivity.”
    - **Source:** `Z59_CONV2.md` Prop 3.1/(MS-U); `Z59_MSPF.md` §§3.4, 4, 9 F2; existing FRONTIER §4 item 2 and `Z58_SUMMARY.md` DISPROOF data. The ≤10⁷ sample does not force a threshold greater than its upper endpoint.

18. **P3 — The mask evidence uses three nonzero classes, not all four T mod 4 classes.**
    - **Location:** `Z59_SUMMARY.md:146–147`, §5 item 1.
    - **Current:** “The rescue is spread over all T mod 4 classes (mask table)”.
    - **Corrected:** “In the ≤10⁷ mask experiment, all three nonzero T mod 4 classes are needed to recover the full-U zero set; T ≡ 0 (4) is redundant for a = 1 rescue by Prop 3.1. This is finite evidence, not an eventual necessity theorem.”
    - **Source:** `Z59_CONV2.md` §3 mask table and Prop 3.1; `REVIEW_CONV2.md` mask check. The three two-class restrictions have 6/9/18 zeros, versus 2 for the full union.

19. **P3 — Reconcile z58's exclusivity wording with the new carried target.**
    - **Location:** existing `FRONTIER.md:272–273` and `2174`, retained alongside the new §2.4/§7 item 19.
    - **Current:** CONV-II “is the only carried target whose statement passes F1–F4 … in the tested ranges”.
    - **Corrected:** “At the z58 checkpoint CONV-II was singled out as the statement-level hot target, not a mechanism. z59 adds the smaller-family conjecture U_II with explicit exceptions {105,4545} and its sharper census/profile; see item 19.”
    - **Source:** `Z58_SUMMARY.md` §0/§5 versus `Z59_CONV2.md` verdict and `Z59_SUMMARY.md` §§0, 2. Leave dated/ranged old census claims intact, but do not leave a current-tense exclusivity claim contradicting the adjacent new target.

20. **P3 — The short headline must distinguish no new zeros from no zeros at all.**
    - **Location:** `Z59_SUMMARY.md:40`, §0 “New certified data”.
    - **Current:** “(MS⁺) to 10¹² (no zero; one engine)”.
    - **Corrected:** “(MS⁺) to 10¹² (no new non-square zero; the 9 prime and 18 composite zeros remain, last 17 401 609; one production engine for the extension).”
    - **Source:** `Z59_MSPLUS.md` §6; summary's own §3. The hypothesis n > 17 401 609 must not disappear in the compact data headline.

21. **P3 — Carry the special CERTIFIED convention into z59 explicitly.**
    - **Location:** `FRONTIER.md:15–20`, label legend.
    - **Current:** “CERTIFIED = an exact finite computation, independently reproduced” followed by an exception explicitly worded “for z58 data”.
    - **Corrected:** “For z58 and z59 data, CERTIFIED denotes the exact finite computation in the cited memo, with the stated production-engine and independent-check coverage; it does not assert a second full-range census.”
    - **Source:** export brief's label/verification requirement; `REVIEW_MSPLUS.md` one-full-engine audit; `REVIEW_CONV2.md` independent coverage only through 10⁹. The new bullets state the engine limitations correctly, but the global legend currently excludes z59 from its qualification.

22. **P3 — Tighten two WALDS table abbreviations and the bottom-line quantifier.**
    - **Location:** `Z59_SUMMARY.md:18–19` and §1 WALDS row (`:54`).
    - **Current:** “No lane found a mechanism forcing … at a single large prime”; “on 𝒞₁ ⊇ 𝔐”; “Remark W3 (sign constant on 𝒞₁; needs (H2), else CONDITIONAL on (W-loc))”.
    - **Corrected:** “No lane found a mechanism proving positivity at every sufficiently large hard prime beyond established local covering classes.” In the table: “on 𝒞₁ (containing 𝔐 when the odd level primes lie in {3,5,7}); W3 proves constant root number on 𝒞₁, while vanishing of sign-−1 coefficient components needs (H2), or conditionally (W-loc).”
    - **Source:** `REVIEW_CONV2.md` required fix 3 (local positivity must not be erased); `Z59_CONVO.md` Cor 3.4 (e.g. p ≡ 73 mod 168 forces a hit); `Z59_WALDS.md` notation and Remark W3; `REVIEW_WALDS.md` W3 audit. The root-number identity itself does not require (H2); it is coefficient vanishing that needs it.

## Checks and limits

Source-number greps and small streaming checks reproduce the MSPF denominators/counts, the rough-target rows
(38/30/21/19 at y = 7/11/43/47), all 500 non-square entries of the source zero list, and the six structured-search
square controls. The old-U certificate at 4545 was checked by direct substitution. No large census, modular-form
matrix computation or analytic proof was rerun for this consistency review. The main corrected review requirements
(shared-integer scope, incomparable c rescue, full d-even versus R₈, 14/38 zeros, withdrawn mean expansion,
121 pairs/123 comparisons/840 ambient exceptions, finite versus eventual zeros, K-R-K priority) are otherwise
faithfully carried. No changes to the source memos, summary or FRONTIER are made by this review.
