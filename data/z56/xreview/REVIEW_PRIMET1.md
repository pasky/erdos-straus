# PRIMET1 cross-model statistics/evidence review

**Verdict: ACCEPT-WITH-FIXES.** Reviewed `side-agent/z56-primet1` at `a2f8ba5b`.
The numerical A9 signal survives replay; the finite-range statistical verdict “narrowed” is reasonable.
Do not record a theorem, a study-wide 5% discovery guarantee, or an exclusion of prime-T1 mechanisms.
ES remains OPEN. Required wording/inference fixes are below.

## Per-claim audit

| Claim | Classification | Independent finding / required qualification |
|---|---|---|
| §1: a (★)-zero prime p ≡ 1 (4) must be 1 (24) | CORRECT (PROVED) | For p ≡ 5 (8), take (u,B,C)=(1,2,(p+3)/8); for p ≡ 2 (3), take (1,(p+1)/3,1). Otherwise p ≡ 1 (8), 1 (3). The citation is RESIDUE_HARDNESS §0 item 6, not a numbered §0.6. |
| R even; u=1/B=1 ticket removal | CORRECT | Swapping u,B has no fixed triple for odd p, since u=B gives even p. For u=1, B(4C−1)=p+1: divisors d ≡ 3 (4) give exactly τ₃(p+1) triples. The two slices do not overlap at odd p. Thus Y loses exactly τ₃. |
| Primary / amendment registration content | CORRECT-WITH-FIX | Actual git content agrees with the repaired §6 ledger, not the misleading subjects. Completion timestamps alone are insufficient to establish prospective registration; see chronology below. |
| Held-out splits | CORRECT-WITH-FIX | Independently recomputed all hash memberships and uniqueness. B₂₃ originally has 337 S2 overlaps; S2 has 330 fitting-split primes. The robust rerun drops all 337. High is reused, not a fresh confirmatory sample. |
| Holm calculations | CORRECT numerically | Recomputed primary 32, A-block 38, A5 30, A6 26, A7/A9 2, S1/S5 16, robustness 15: agreement within table rounding. These are blockwise, not a single study-wide error budget. |
| Registered A9 on B₂₃ | CORRECT (EVIDENCE) | Full replay: n=789181, p−1 F=4.964, raw p=0.006987, Holm=0.01397, coefficients +0.02475,+0.02675 z/SD. p+1 F=1.248, Holm=0.2872. |
| Complete-null, overlap-excluded A9 robustness | CORRECT (EVIDENCE) | Full replay: n=788844, 888 null columns; PM1 robust LM=12.4004, raw p=0.002029, Holm over two=0.004058; coefficients +0.02768,+0.02997. PP1 raw p=0.4891. Across all 15 rerun families PM1 Holm=0.03043, still significant. |
| “Candidate under the amended rule,” §4.3 | CORRECT-WITH-FIX | A prospectively specified B₂₃ test succeeds. However h₃′ is exploratory discovery data, not the registered S1 replication; High A9 p≈0.87. The Q₀=2000 refit was not performed. Do not present the retrospective clause-by-clause reinterpretation as literal compliance with the original rule. |
| A9 excludes F-type/local alternatives | GAP if read as exclusion | The cited shift lemma does not control the total association after selection/adjustment. One fixed weighted aggregate through 20000 is not arbitrary large-modulus local adjustment. “Not absorbed by the tested null” is supported; “not a sum of local effects” is not established. |
| T2T S₃ arithmetic / control | CORRECT (EVIDENCE) | Full replay: n_eval=176733, ρ=−0.00496080, Fisher 99% CI [−0.0110880,0.00116676], p(H₀:ρ≤.005)=0.999986; sieve comparisons: 0 mismatches. Planted σ=.05,.1 estimates .00252,.01017 reproduce. |
| T2T High / interval calibration | CORRECT-WITH-FIX | Independently refitted: n_eval=12474, ρ=−0.0121043. Sandwich 99% intervals are [−0.0109891,0.00106753] on S₃ and [−0.0343614,0.0101528] on High; close to Fisher, conditional on fitted means and iid sampling. High is exploratory. |
| T2T SD(H) / density limits | CONDITIONAL sensitivity only; GAP as exclusion | Approximately 1–3% is a working-model conversion, not an identified upper confidence bound on arbitrary hidden factors. Negative covariance can mask positive coupling; a non-rejection of ρ>.005 is not acceptance of independence. |
| S4b-r “cross-fit / out of sample” | CORRECT-WITH-FIX | `robust.py` fits the nuisance residual on the entire h₃′ sample; `s4r.py` splits only the boosting stage and uses a full-sample tail quantile. This is not a wholly held-out pipeline. |
| G12 nonlinear association “explained” by square offsets | GAP | The exploratory decomposition and B₂₃ contrasts support a near-square interpretation, not demonstrated absorption of the omnibus. The necessary augmented-null replication is explicitly not done (§6 last item). |
| PC2 / precision claims | CORRECT-WITH-FIX | The repaired one-feature idealised benchmark is honestly labelled, not familywise power for rare/collinear features or amended nulls. Generic 0.02% SEs cannot exclude arbitrary interactions or subclasses. |
| Census / exceptional minimum | CORRECT on inspected artifacts | Independently streamed all three stored binary censuses: 14 listed zeros ≤10⁸, none in [10⁷,10⁹] or (10⁹,10¹⁰]; last range has 50521668 primes and unique min R=2 at 1397190001. Recompiled rone independently returns (R,A1,A2,A3)=(2,2,0,0) there. Full sieve generation was not repeated. |
| “Four orders too small,” §3.8 / §4.3 | WRONG as a quantitative inference | A sub-percent mean association and an exponentially small baseline zero probability are different quantities. No derivation gives this ratio or rules out a rare deterministic zero subclass. Delete the numerical comparison. |
| ES scope / final “narrowed” | CORRECT-WITH-FIX | No ES theorem or fixed-prime conclusion is claimed. Retain a finite-sample evidence verdict, not “all extra associations explained” or exhaustive restrictions on where a prime T1 must live. |

## Registration and sample provenance

Checked the memo blobs, author/commit chronology, scratch mtimes, and the producing session's tool-call order.
All times below are 2026-11-04 CET; these are local provenance records, not externally timestamped registration.
- `6ddab6c0` 18:56:24 contains the initial 16-family protocol; `345fbe79` 19:26:44 first contains Amendment 1.
- `45c5895f` 19:44:22 still has only Amendment 1; `da4971f4` 19:46:11 has an EMPTY memo.
- `4fa8b3a6` 19:47:19 first contains Amendments 2–4. High T2T was invoked at 19:46:40 and finished 19:46:48: exploratory.
- A-block/A5 were queued sequentially at 19:44:53; A-block output was 20:00:19. Thus the A5 command was scheduled before its git registration, but its execution followed A-block completion, after registration. A5's final output is 20:19:21.
- S₃ T2T was invoked 19:57:44 and finished 19:58:26, after Amendment 3. S4 began 19:47:23, after Amendment 4.
- Amendment 5 is in `b1d357c3` 20:04:14; A6 invoked 20:43:22, output 20:45:56.
- Amendment 6 is in `1789ce0c` 20:51:54; A7 output 20:52:26. Amendments 7–8 first appear in `073515c3` 21:13:27.
- The actual A9 command explicitly runs `git commit ... && ... g16c.py pred_b2h3.npy`; output 21:13:54. The decisive association test follows registration, despite the short gap.
- B₂₃'s prediction artifact existed at 20:58 and S2 had already used 337 of its primes. “Never touched/fresh” was not literally true. Post-review exclusion repairs direct row overlap, not the historical description.
- D/C/h2 sizes: 1568230/1566421/1568224; h₃′=1175949 (hash mod16 ∈{7,11,15}); S₃=353214 (mod16=3, p≥10⁸). All match, with disjoint specified memberships.
- A-block and A5 reuse h2 under prospectively specified batteries. A7 reuses T2T counts; h₃′ is repeatedly explored; B₂₃ is reused for post-review tests. Distinguish fresh associations, fresh rows, and wholly independent replication.

## Required fixes, priority order

1. **Bound the inference, not a hypothetical prime T1.** Keep the T2T numbers as sensitivities and remove “must have density ≲10⁻⁴ / act only above 10¹³” from standalone summaries/FRONTIER text. The ranges between bulk and the two small High windows are not exhaustively sampled.
   A concrete countermodel: independent Gaussian H,K with rates μ₁exp(H+K−(vH+vK)/2), μ₂exp(H−K−(vH+vK)/2) and conditionally independent Poisson counts have covariance μ₁μ₂(exp(vH−vK)−1). Arbitrarily large vH is compatible with zero/negative covariance when vK≥vH. §4.5 acknowledges this possibility; the summaries must preserve it.
2. **Separate detection from explanation.** Replace claims that the nonlinear G12 signal “is explained” or that no association survives in those families with “consistent with square-offset near-squares; augmented-null replication pending.” Label S4b-r's nuisance fit as in-sample. For an OOS claim, fit nuisance coefficients and the tail threshold on training rows only, then evaluate a fixed model on untouched rows.
3. **State exactly what A9 confirms.** Use “pre-specified two-feature B₂₃ confirmation, with post-hoc complete-null robustness,” retain both p=.01397 and .004058, and also disclose the 15-test Holm=.03043. Do not call h₃′ an independent S1 replication or the robust rerun a second independent confirmation. State explicitly which original decision clauses were superseded and when; no literal Q₀=2000 validation exists.
4. **Keep multiplicity scope explicit.** Every stated Holm FWER is conditional on valid input tests and pertains to its named block. No alpha-spending plan covers all amendments, post-review family searches and square-offset contrasts. The square-offset contrasts also use the overall residual SD, not subgroup-robust uncertainty; their nominal z-values are not calibrated familywise confirmations.
5. **Remove unsupported numerical/causal language.** Delete “four orders too small” and the §3.8 comparison of mean effects to exp(−Θ(log²p)) zero probabilities. Say “small bulk association, not an observed kill.” Describe larger-q confounding as unresolved, and the “complete known null” as a chosen finite additive model, not the best possible local predictor.
6. **Tighten provenance/reproducibility.** Keep the corrected blob ledger and High exploratory label prominently, give command start/order as well as completion times, and list exact post-review commands. §7 currently omits the robust and S4b-r invocation details needed to recreate headline revisions.

## Replays and reproducibility

All review shell commands used `ulimit` and `timeout`; statistical runs used ≤6000000 KiB virtual memory and two BLAS threads.
Inputs: `/home/pasky/scratch_z56_primet1`; reviewed scripts/data were archived to `/tmp/xrev_PRIMET1`.
Replayed `z56_primet1_g16c.py pred_b2h3.npy model_B2.npz ...` without changing its code.
Replayed `z56_primet1_robust.py pred_b2h3.npy feat_b2h3.npy feat2_b2h3.npy cf4_b2h3.txt model_B2.npz ... --tau3 --a9 --exclude s2_setp.npy` with its default 15 families.
Replayed `z56_primet1_t2t.py s3t_rone.txt ... --sieve s3t.npy`; independent script also refits both T2T samples and derives a sandwich interval from the correlation influence function.
Audit script: `scripts/z56_xrev_primet1_audit.py SCRATCH ARCHIVE --t2t` (uv dependencies numpy/scipy).
It checks git content, independently implements splitmix64 and Holm, streams the censuses, and bounds dense designs to fitting chunks.
Raw review outputs remain in `/tmp/xrev_PRIMET1`; decisive values are preserved here. No full invariant recomputation, full primary regression replay, or 10¹⁰ sieve regeneration is claimed.

**Bottom line:** reproducible evidence for a small p−1 association and no detected positive two-ticket coupling; useful narrowing of specified fitted-model hypotheses, not a lottery proof or exclusion of unsampled/nonlinear/rare mechanisms.
