# Hostile review, pass 2 — Z55_CROSSU.md at 6d057464

**Verdict: accept with fixes.** The main mathematical repairs and regenerated prime statistics pass. Six localized issues remain; do not describe all 13 original findings as completely resolved yet. ES is explicitly OPEN and the memo repeatedly, appropriately says no mechanism was found.

## Independent checks
- All Python checks ran with `ulimit -v 4000000; timeout 300 uv run python ...`; only small lists/streamed enumeration were used. Scratch script/results: `/tmp/z55-pass2.EdwXEy/check.py`, `check.txt`.
- §4.1: checked all 2,025 squarefree u ≡ 1 (4) in [5,10000]. Only u=5 has q_u<3 (q_5=2); the minimum for u>5 is 3. Universally, q_u=∏(ℓ−1)/2≤2 forces prime factors among {3,5}, leaving only u=5 under u>1, u≡1 (4). The elementary inequalities are correct.
- §4.2: the partial-involution domain, j′=2p⁻¹j⁻¹, and hit/genus sign criteria are correct, with the stated requirement w≡3 (4) for the switched point to remain in S₃. The final multiset claim is not: see R2.
- §4.6: K(1−γ)>1 correctly uses the lower divisor scale. For bounds up to constants this is an asymptotic sufficient condition with a strict margin, not a necessary threshold.
- §4.10: reciprocity gives (d/p)=(p/d)=(−u/d)=−(d/u)=−(j/u) on S₃. The constancy on each fixed-u genus coset and inner product −(R−G) follow.
- Independently trial-factored p=1,000,345,561 (prime, 1 mod 24) and enumerated the legal window (5,500,1000,250057): 220 shell points, 112 in S₃. All 112 satisfy the Jacobi identity (64 symbols −1, 48 symbols +1); all 220 satisfy A's inverse/floor identities and B's remainder relation. All 168 switchable shell points satisfy the switching congruence.
- Compiled the current C engine; its complete S₃ dump agrees with the independent enumeration. `badA` really checks all three stated identities, including divisibility; `badB` checks only the inverse relation for the second remainder, exactly as §5.1 says. All 1,339 TSV rows have badj=badA=badB=0 and nA=nsh3; total 3,014,093.
- Recomputed statistics independently from main.tsv; also reproduced stats.txt byte-for-byte. Prime-sample mean range [−0.673355,+0.589434], sd-ratio [0.875410,1.176515], z range [−2.485329,+1.914420] agree with the memo's rounded figures.
- Maximum |corr| by prime sample: .238412,.215916,.206476,.267788,.244167,.236197; maximum involving c=1 is .253339. Histogram maximum deviations: .001844,.003497,.001423,.000902,.000778,.000530. All quoted rounded values agree.
- Pooled z values agree: c=1 −1.611455; −1 +2.157839; 2 −.124502; 4 −.047323; 12 +2.043449; 25 +2.349833; full range [−1.777461,+2.349833]. All six c=1 z/sd-ratios also agree.
- Hard-prime description is correct: five empty STARZERO shells, two singleton off-genus shells, seven positive G values .10–1.903824; exceptions 3361 and 5101441 as stated. Residual mean −.387880, sample sd .677588, maximum shell size 26.
- Every §5.2 count, percentage, interval and mean agrees with pairs_1e12_1e13.txt after rounding. Source inspection confirms no-replacement sampling, correct window endpoint/singleton means, and prime-level bootstrap of paired hit/null summaries. I did not regenerate the 300 dumps or rerun that simulation.

## Disposition of the original 13 findings
1. PARTIAL: q≥3 repair and elementary bound pass; one overbroad scope sentence survives (R1).
2. PARTIAL: switching domain/sign repairs pass; multiset “iff” remains false (R2).
3. ADDRESSED: corrected lower-endpoint threshold; unsupported typical-count assertion removed.
4. ADDRESSED: precise Vieta restriction retained; general tool exclusions replaced by Assessments and explicit limitations.
5. ADDRESSED: engine/stats use class-specific V_c with the independence assumption stated.
6. ADDRESSED for the requested prime populations: every regenerated numerical range checks out; control prose needs R3.
7. SUBSTANTIALLY ADDRESSED: descriptive set-valued null, bugs and uncertainty repaired; reproducibility instructions still incomplete (R6).
8. ADDRESSED: histogram claims are explicitly marginal, integer squares are correctly described, unanalysed shape acknowledged.
9. ADDRESSED: false orthogonality replaced by the correct Jacobi identity and inner product.
10. ADDRESSED: “determine,” exact equality, exclusion of u=1 and nonunit convention are correct.
11. PARTIAL: §5.1 accurately lists finite checks, but §3's blanket certification remains (R4).
12. ADDRESSED: hard-prime emptiness and sample-sd wording corrected.
13. SUBSTANTIALLY ADDRESSED: identities, empirical evidence, conditional implication, conjecture and Assessments are distinguished; review reference/disclaimers fixed. R4 prevents a clean finite-certification label audit.

## Remaining findings (severity and fix)
**R1 — MAJOR, §4.1, line 109: the “bounded multiplicity and bounded q” exclusion still does not follow.**
The bound excludes a single negative point per hit, not bounded-size groups: at q=3, 2/3−1/3−1/3=0. Bounded q does not obstruct bounded multiplicity.
**Fix:** replace the scope sentence by “excludes hit-to-single-nonhit pairing and gives the stated lower bound on group size.” A uniform bounded-group obstruction requires q_min→∞. Replace “needs many points” in the bottom line by the precise bound.

**R2 — MAJOR, §4.2, line 119: preservation of a shell index multiset's genus count is not equivalent to 2p∈□_u.**
A switch permutes its switchable point set, hence preserves that multiset's genus count regardless. Concrete legal S₃ example from my enumeration: u=33, (w,d,j)=(8731,57287,1) ↔ (57287,8731,26). Here 2p⁻¹≡26 is nonsquare mod 33, yet the multiset {1,26} has one genus index before and after.
**Fix:** say the unit-group map j↦2p⁻¹/j preserves the square subgroup *setwise* iff 2p∈□_u; otherwise it sends that subgroup to a different coset. Do not claim an iff about observed multiset counts.

**R3 — MINOR, §5.1 controls and §6 T1: “the non-square classes fluctuate” omits two identically zero classes.**
stats.txt/main.tsv have N_c=G_c=V_c=0 also for c=−1,−4 on every square control. The quoted .84–1.08 range is over the other eleven classes with positive variance, not all nonsquare integers c. Near-square/composite sd-ratios are .714–1.245, .853–1.147 and .784–1.281, not literally the prime range. The selected eighteen classes also “share,” not “partition,” the shell.
**Fix:** list all seven vanishing classes; restrict the fluctuation claim to the remaining eleven. Say control spreads are broadly comparable but wider; replace “partition” by “share.”

**R4 — MINOR, §3 heading, line 47: “identities checked on every point of every run” is still too broad.**
The engine does not check Lemma C, the SL₂ matrix product, or the complete length-three characterization. §5.1 now correctly says what was checked, but does not make the blanket heading true.
**Fix:** “PROVED; specific finite checks listed in §5.1.” Keep PROVED algebra and CERTIFIED run assertions distinct.

**R5 — MAJOR, §4.11, line 173: an arbitrary map to hits anywhere does not imply (CU′).**
A constant map can collapse all genus points onto one hit; moreover, that hit may lie outside the selected family defining R. Assessment is not a license for this false implication.
**Fix:** distinguish full-(★) positivity (a transfer from nonempty genus support suffices) from R_𝔉≥εG_𝔉 (requires targets in the same family and a uniform weighted multiplicity bound).

**R6 — MINOR, §5.2: the requested pair-run reproduction recipe is still absent.**
The memo names the optional dump argument and sample but supplies neither the exact regeneration command nor a dump manifest; run_main.log is empty.
**Fix:** document commands selecting the p1e12/p1e13 rows from main.tsv, passing each stored window to the engine's dump argument, then invoking the pair script with REP=20, BOOT=200 (fixed seed 1). No need to store the large dumps.

These fixes leave the substantive verdict unchanged: useful elementary identities and descriptive computations, no cross-u cancellation mechanism, no resolution of ES or (CU).
