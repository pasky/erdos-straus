# Hostile review of da7b8a9ff..a27d0bf0d (z76 DISPROOF_DEEP / DISPROOF_COMP)

Reviewer: Claude (Anthropic, Opus-class, run as a Claude Code subagent; I can't see the exact version string). This counts as
the "other lab" review only if the z76 lane authors were Astra. The commits do not record which model wrote them.
Scope: DISPROOF_DEEP.md Thms 1–3, §3 cover claim (3) and the single-algebra detector; DISPROOF_COMP.md R₈ record, matched
controls, subsample, hunts; the new scripts and data. Not reviewed: the z75 inputs that these build on (the patch lemma, Prop F/T), the
completeness of the AP sieve beyond spot checks, and the ap11/r121/r169/r289/r529 runs (not rerun).
Verdict: ACCEPT-WITH-FIXES. I found no mathematical error. The fixes are about form, interpretation and citations.

## Independent computations (all in data/z76/opus_review/, sequential, ulimit -v 6000000, timeout ≤1800)
* `verify_r8.py` is my own code and reuses no repository engine. For p=1,590,284,203,561 it proves primality by trial division to √p. For every u with
  ku²−2u≤p it fully factors p+u: a sieve over all primes ≤√(p+U), with each factorization re-multiplied to check it. It then enumerates every
  divisor f≡−1 (mod ku) with N/f≥u, and separately iterates C directly for u≥20000.
  Result: **R₈=0 and R=52** (26 unordered, first (15,26984,982239)), agreeing with the stored results. Calibration: 1,485,418,095,001 gives 18 unordered (= subfactor.txt).
  The old floor 1,511,088,831,001 gives R=44 and R₈=0. Output is in `verify_r8.txt` and `verify_r8_calib.txt`.
* The full-8 witness (2,101507502355,3,1), the identity 8/p=1/abd+1/pacd+1/pbcd and the factorizations of p−1 and 12p+1 all check out.
* Rebuilt and reran `panel` (match.txt, squares.txt), `factor`, `cap check` (squares_C) and the **r361 AP run** (79 s). All are byte-identical.
  The AP engine re-finds both z75 zeros, 1,218,367,081,201 and 1,511,088,831,001, on 10⁹-wide windows (`cap_calib.txt`).
* `z76_disproof_report.py` and `z76_disproof_subsample.py summarize` reproduce report.txt and subreport.txt byte-for-byte.
* `check_match.py` re-derives the controls with my own MR and my own 61-smoothness test. All 720 square anchors, plus 60 complete and 40 dropped quartets,
  match the stated rule exactly: nearest unused eligible candidate at ±jM, with + before −, in anchor order. Every dropped cell really has no eligible control.
  **All 883 quartet dropouts lack the sm− cell** (smooth p−1, composite 12p+1). The other cells were never the cause.
* `fibre_extra.py` checks even c≤1000. r=1,5,9,17,21 have no points. r=3 has points only at c=2,6,34,198 (ratio →3+2√2, as Thm 1 predicts). r=13 has points only at c=2,10,58,338.

## Mathematics
* Thm 1: I checked it line by line and it is correct. The steps checked were (1); both Vieta products; the termination inequalities as t≤v; (2) using w≥2; the exclusion of d=e=1; e≡−n (mod 4);
  the hyperbolicity of the trace 4de²−2; the invariant form vanishing on the eigenlines; and the O(log X) count. Optional strengthening: the same argument gives
  **no points for all even c at r∈{1,5,9,17,21}**. For r≡1 (mod 4) we have e≡3 (mod 4), so e=3 is forced. For r=17 or 21, d=1 is also forced, and then (c−6a)²=32a²−(3+r) is impossible mod 8.
* Thm 2: correct, including acde≤n, the e≤D / ad≤D split and e(4acd−1)=n+4a²d. The upper limit α<2/3 is not needed for the count. It is only
  there for the comparison with the strip bound, so say so. Otherwise the statement looks weaker than what was proved.
* Thm 3: correct. The n=4adec−4a²d−e line, |g|≪L^{β−1}, g″≍L^{β−2}, the sublevel length 4√(h/κ) and the two pieces all check out. The remark "One can take α=1/4 or any smaller…" is odd,
  since the theorem holds for every fixed 0<α<1.
* §3 (3): correct, but it is literally the z75 "Sharper opposite endpoint" (DISPROOF_OBSTRUCT.md l.47, itself a refinement of Z58_STRUCT2 Prop T)
  plus functoriality. **Cite those as the source** and do not re-present it as a new result. The note calls it tautological, which is right.
* The single-algebra detector: correct for the m=2 patch B′=q²B. I checked y_q=±q exactly, the twist rigidity via local–global for squares, (L,−1)_v=+1 for L≡1 (mod 4),
  (L,±q)_q=(L/q)=(q/L)=−1, and π*(ψ,x/x(P))=(2ψ,y). The patch quadruples (4545,11,13), (131,7,5) and (241,7,5) satisfy the conditions.
  Caveat to add: with the q⁴ repair, the level-4 lift is rejected again by (L,z) with z⁴=x/x(P). "Avoids this detector" is true only at level 2.

## Evidence and controls (COMP)
* The record is sound, and nothing in it relies on a cap or a truncated detector. A STATUS row is justified once the lab gate is met.
* Control selection is faithful to the description, but the selection is heavy. The common support is "anchors with a smooth composite-shift neighbour within 0.1% at
  step M". This favours anchors with large 2,3,5,7-parts of p−1, and the sm− controls sit at the caliper edge (999.97 ppm). Within-quartet comparisons are fair. Say in
  one sentence *which* cell drops: it is always sm−.
* Statistics: the discordances are given without tests. McNemar gives roughly p≈0.03 for 214:170 and p≈0.002 for 212:153. The two smoothness contrasts share sm+ anchors and are
  post hoc after z75. "Retains a smaller excess" is acceptable only with that caveat.
* **Square diagnostic interpretation (main substantive critique).** The 367:522 reversal is forced mechanically. On a compatible shot, m²≡−(u+1) (mod f)
  has 2^{ω(f)} roots, so square shifts hit compatible shots about twice as often as uniform residues do. The filtered control detector is therefore not
  like-for-like. A cleaner statement: under the local models, the expected number of shots f≤1000 hit is 0.82 for square shifts against 2.89 for unit-uniform residues.
  The empirical means are 0.67 and 2.03 (`shot_expect.txt`). So the late-witness excess is a deterministic local-density effect. Replace "the deleted classes more than
  account…" with this. The 367:164 (u≠1) figure is fine.
* "Only residues 1 and 121 realised" for m²+1 is forced (4·3·5 | m and m≡0,±1 (mod 7)). Add that one line, so the result is not read as a finding.
* Taken together, z75 r8c (1 mod 840 to 3.25e12) and z76 (the other five classes to 3.1e12) sweep all of 𝔐 in (1.511e12, 3.1e12] with a single sieve design, and exactly one
  zero turns up. It could be stated as a single-engine EVIDENCE sweep. As written, the note correctly claims no census. The unswept gaps should be stated: 121 and 361 in
  (1.288e12, 1.511e12), and 169, 289 and 529 below 1.511e12.

## Form
* Both notes claim the same RECORD and propose *different* STATUS texts for the same row. DEEP's §0 Result, Label and Triage should drop the R₈ record and
  point to COMP. DEEP's Result line omits Thms 2 and 3 and (3).
* DEEP §4 "No 15th R-zero or 4th Type A zero found" needs the scope "among the 7,723 exact-fallback primes".
* The proposed STATUS replacement drops the earlier zeros and the checker count. Keep "11 certified in-𝔐 zeros; the floor is now …; four checks (incl. cross-lab)".
* The replay wrapper is still not run end-to-end. The ap11 run has 2.2e9 slots under a 1800 s per-command timeout, and its runtime is unrecorded.
* No priority claims; no master files touched (correct for a lane).
