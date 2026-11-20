# Cross-lab hostile review (Claude Opus) of lane Z72PHASE: phase criteria, small support, extremal triples, orbits

Result: every PROVED claim in the seven notes was re-derived; no mathematical error found. Every decisive finite claim
was recomputed by independent code, and all agree. One significance statement is overstated (the "cap of 123" in
`counter_tail/README.md`).   Label: Assessment (review)
Scope: `Z72_PAIR_PHASE.md`, `PHASE43_DENOMINATORS.md`, `EXTREMAL_ES.md`, `data/z72/mixproof.md`,
`data/z72/counter_tail/{README,ROUND2,ROUND3}.md` (with their CSV/JSON data), `Z73_COMPOSITE_PHASE.md`,
`Z73_PROBE_FORCING.md`. All of it is ordinary-integer work: no weak theories, no independence claims. ES is OPEN, and no
note says otherwise.
Review: this file (cross-lab: the author is GPT Astra, the reviewer Claude Opus). Astra's audit scripts were re-run but
not relied on.   Verdict: **ACCEPT-WITH-FIXES** for all seven notes.

## 1. Per-note verdicts

| note | verdict | main fix |
|---|---|---|
| `Z72_PAIR_PHASE.md` | ACCEPT-WITH-FIXES | The claimed "independent replay to 5·10⁷" has no script in the repo; the review's by-p replay now covers all of 5·10⁸. Reword "arbitrary shifts"; the density-one statement is elementary |
| `PHASE43_DENOMINATORS.md` | ACCEPT-WITH-FIXES | Label the paired example CERTIFIED (it was "PROVED") |
| `EXTREMAL_ES.md` | ACCEPT-WITH-FIXES | Note that (X,Y,Z) is exactly the strict-greedy triple; add literature context (Kovač; Kovač–Tang) |
| `data/z72/mixproof.md` | ACCEPT-WITH-FIXES | §0 block only; the dependence on Z70_CLASS SR/FR′ was re-derived |
| `data/z72/counter_tail/` (README, ROUND2, ROUND3) | ACCEPT-WITH-FIXES | README: "refutes a uniform cap of 123" is not new. Small primes already have first shifts 323 (p=66529), 1551 (p=370228321, with p ≡ 1 (840) and (p+1)/2 prime) and 2695 (p=44407609) |
| `Z73_COMPOSITE_PHASE.md` | ACCEPT-WITH-FIXES | §0 block. The review adds an explicit prime instance for s=2 |
| `Z73_PROBE_FORCING.md` | ACCEPT-WITH-FIXES | §0 block only |

None of the notes had the AGENTS.md §0 block. All fixes are applied (§4) and tagged "(z74 Opus xreview fix)".

## 2. Per-claim table

| # | claim (note) | verdict | what I checked |
|---|---|---|---|
| P1 | Two-factor criterion: T>1, or T=1 with v or w odd ⇒ hit; at T=1, miss ⇔ ord(a)=2V, ord(b)=2W, gcd(V,W)=1 (Z72) | CORRECT | Re-derived. Λ*=ℤ²+ℤ·2a⃗/m; the label functionals are D₀(2a⃗/m)+2L*, with min ℓ¹ = 2T. Gauss basis: one odd vector gives λρ ≤ √2/sinθ ≤ √(8/3); two odd vectors give (1+s²−2st)/(1−t²) ≤ 2 ⇔ 1−s²+2t(s−t) ≥ 0. In the equality case s=1, t=0 and the basis is axis-aligned with unit vectors, so Λ=Vℤ×Wℤ with odd V,W of coprime order. The converse holds. q,r≠c is automatic (c∤n ⇒ c∤K). Brute force (`group`): 778,900 boxes with c ≤ 83, the full (a,b) range and v,w ≤ 5. Every firing case hits; the 16 equality misses are exactly the order/coprimality cases |
| P2 | General finite abelian version; a non-square t forces V,W odd (Z73_COMPOSITE) | CORRECT | Character extension and the identification "label functional ↔ character of H with χ(t)=−1" re-derived. The Gauss-basis step needs only the lattice and the label. Brute force over G=ℤ/m₁×ℤ/m₂ (9 groups, every t of order 2, every q,r, v,w ≤ 4): 201,984 cases with 0 discrepancies, and 480 equality misses, exactly the q^V=r^W=t direct-product cases |
| P3 | Triple (K, nADE, nBDE); 1009 example (Z72) | CORRECT | Identity re-derived. At 1009: logs (4,9), T=1, triple (255,102918,30270) |
| P4 | 1201: successful shifts {23,31,39,47} with min ω = 3,3,2,3; no prime shift has support ≤ 2 (Z72) | CORRECT (CERTIFIED) | Bound c ≤ (p+4)/3 re-derived. The table was recomputed by unrestricted coprime enumeration. Scope: this concerns the Type II certificate shape only, as the note says |
| P5 | Support ≤ 2 on a relative-density-one set of primes 1 (4), via c=3 and c=2r+1 (Z72) | CORRECT | Identities and integrality (h/r ≡ 3 mod 4) checked on 10,932 cases. The density argument (fixed finite lists, ∏(1−1/(r−1)) → 0) is sound. It is elementary, and much weaker than the classical fact that almost all n satisfy ES (Vaughan 1970). "Arbitrary shifts" means shifts not restricted to primes |
| P6 | Sieve: every prime p ≡ 1 (4) below 5·10⁸ (13,176,808 primes) has ω(AB) ≤ 2 (Z72) | CORRECT (CERTIFIED) | The authors' engine was rebuilt and re-run (45 s): 0 misses out of 13,176,808. **Independent by-p engine** (`scripts/z74_xrev_z72phase_bypsieve.py`, shares no code, 23 s): all 13,176,808 pass. A separate numpy count confirms the prime count. The authors' claimed 5·10⁷ replay has no script in the repo; this review replaces it |
| P7 | Paired rows at c=43: same phase costs, opposite outcomes; the negative row has no completion at any c ≤ 43 (PHASE43) | CORRECT (CERTIFIED) | Primality, class 1 mod 840, Euler signs, logs (−10,−1,7,∓7), the cost list, the missing ratio set {4,11,14,40,42}, and the divisor classes of H² missing exactly 30=−H. Direct test with the reduced fraction at all 11 shifts c=3..43, including composite c: none completes. None of the 203 admissible divisors d of H² (those with 4d>n) is a denominator of any triple. The c=47 triple was checked. The complementation lemma was re-derived |
| P8 | §1: for n ≡ 1 (24) with no prime factor 3 (4), (X,Y,Z) is the unique closest nonexact triple (EXTREMAL) | CORRECT | Re-derived every inequality: e₀<1/(3n⁴), x<n, y ≤ 3B/A, s ≤ 2B, (1), (2), F convex with F ≤ 1/5 for A ≥ 7, A=3 ⇒ s ≡ 2 (3). Independent exact band enumeration E ≤ e₀ for 16 n from 25 to 2521 (including the composites 25, 625, 1105): only (X,Y,Z). (X,Y,Z) is the strict-greedy triple |
| P9 | §2: no exact triple contains Z; the X and Y gates are iff tests; a prime Y closes the Y gate (EXTREMAL) | CORRECT | s ≠ 1 via A(4y−n)=n²+4s. MX−nY=2. The gates agree with direct completion tests at 8 primes. Gate values at 73, 409, 577 and 2521, the X gate at 10156800001 (13·199·981523), and n=25 (open through 5) all reproduced |
| P10 | 73: bottleneck H=1/44913834, strict band of 6,939 vertices with no exact triple in the extremum's component (EXTREMAL) | CORRECT (CERTIFIED) | Own band enumeration (finiteness asserted on every fibre) and union-find over shared denominators: 6,939 vertices; the extremum's component (6,296) has no exact triple. The path errors are exactly e₀, H, 1/131702220, 0 |
| P11 | n<73: 10 survivors, each with a unique optimum one move from a solution; D-energy trap at 17, escaping at cap 3 (EXTREMAL) | CORRECT (CERTIFIED) | Recomputed independently, including the |D| ≤ h bounds |
| P12 | d=1: CRT glues roots, not divisors (409); constructive forcing on subprogressions; mixed hit at 1.5·10¹⁶; 9601 ranking (mixproof) | CORRECT | Root/divisor equivalence and the complementation sign swap re-derived. The forcing construction is sound: ℓ ∤ L, so the menu is unaffected. All numbers recomputed with my own menu builder and form reduction |
| P13 | d=2: on p ≡ 9601 (M), p ≡ −8 (31), p > 2·5783557², no menu word is good while A=31 is good (mixproof) | CORRECT | SR (Z70_CLASS: min(A,B,2e) ≤ √(2(2p+(p+8)/7))) and FR′ (Nm<2p ⇒ equal primitive ideals) re-derived; the even norm 2e is excluded. Certificate rerun with my own menu: 710 words, 103 norms. **An actual prime in the cell**, p=527397324177878694549601 (proved prime by Pocklington): same menu, no word passes the membership test, and the A=31 triple (2b, 8p, 8bp) was verified |
| P14 | counter_tail README: shifts 3,7,11 blocked unrestricted; late first shifts 79/83/111/127 and control 87; quantile table | CORRECT (CERTIFIED) | Local lemma re-derived. All five late rows recomputed by p with GNU factor. First shifts of 300 random CSV rows recomputed; all 7,168 triples checked exactly, each regenerated from its recorded (A, B, first_c); quantiles reproduced |
| P15 | README: "refutes a uniform cap of 123" | CORRECT but OVERSTATED | My 5·10⁸ replay already refutes a *uniform* cap at **p=66529 (first shift 323)**. Among primes with p ≡ 1 (840) and (p+1)/2 prime it is refuted at **p=370228321 (1551)**. The target progression p ≡ 1 (L) itself has no primes below 5·10⁸, so no within-progression comparison is possible. The maximum is 2695 at p=44407609. No growth trend is inferred. The certified cohort contrast (targets vs controls) stands as DATA |
| P16 | ROUND2: exact shift-15 obstruction and the ⟨2⟩ index-2 mechanism | CORRECT | Re-derived (j ∈ [−2,2] covers ℤ/4, AB | 4q). All 2,048 rows of c15.csv: Q refactored, criterion ⇔ no support-≤2 certificate at 15; 823 blocked (540 with composite Q), median 23, max 119 |
| P17 | ROUND2/ROUND3: closed components at 14281 (O), 101641 (O and T, disjoint) and 1009 (T) | CORRECT (CERTIFIED) | **Own** divisor-based pair-move generator. Each listed component is closed and has no mergeable pair. Vertex/edge/layer counts match: 92/641, 20/47, 65/306, layers as stated, and even-denominator layers as stated. A truncated list fails (negative control, in the script) |
| P18 | Census: from O, 52 of the 53 Mordell-class primes < 20000 merge and 14281 is closed; 277 pretrap paths; nested-seed paths; universal seed (ROUND2/3) | CORRECT (CERTIFIED) | Own BFS reproduces every first-merge depth in four_orbit.csv. All 277 paths (exactly the Mordell-class primes < 101641) were checked step by step, and so were the nested paths (101641 gives (25434, 27214380, 307344088620)). The five universal-seed moves were re-derived |
| P19 | Fixed K=779290511 at c=715: no ES triple contains K; the pairwise components are solvable but the joint one is not (ROUND3, Z73_COMPOSITE) | CORRECT (CERTIFIED) | Signs, (p/c)=−1, the Mordell class, all 27 divisors of (pK)², joint T=0, and the c=11 triple |
| P20 | Unbounded minimal obstruction (any even s); the prime variant is CONDITIONAL on Dickson (Z73_COMPOSITE) | CORRECT | Parity system and proper-subset solvability re-derived. n ≡ 1 (840), (n/c)=−1 and n ≡ 4 (ℓ₀) verified; Dickson admissibility checked. **Explicit unconditional instance for s=2**: ℓ=(2521,211,3361), q=(2816655498511, 66076508762723), n=744459046915736043727401721, proved prime by Pocklington (the direct test needs n prime). No triple contains x=K |
| P21 | PROBE §1–2: same sign rule; A=1,B=2r incompatibility; E=2 compression; 193 first without an A=1 certificate (PROBE) | CORRECT | Re-derived; brute force for p < 3·10⁴ / 6·10⁴. 193 confirmed (16 shifts) |
| P22 | PROBE §3: sharp support theorem on s ≡ 15 (16) and the E=5 prime-power criterion | CORRECT | Case analysis re-derived in (ℤ/16)* and (ℤ/20)*. Brute force on all 2,500 values s < 40000 (composite s included): 0 discrepancies, and min ω ≤ 3 always. Table rows checked: the E=4 minima, the E=5 yes/no, and the unique B for 959/2911. The 2911 extras were checked too |
| P23 | PROBE §4: three forced nonresidues; at 4319 none of 7, 59, 5399 occurs in any support-≤2 AB | CORRECT (CERTIFIED) | Pairwise coprimality and Jacobi signs re-derived. Exhaustive k=q^i r^j enumeration with c = −p mod 4k; a positive control (19 at 2911) passes |
| P24 | PROBE §5: the ⟨2⟩ = Jacobi-kernel lemma and the c=7 corollary | CORRECT | Re-derived. Every hypothesis-satisfying (p<3·10⁵, 20 shifts c ≡ 7 (8) with ord_c(2)=φ(c)/2, composites included) has a certificate. All family primes with 7 | s (s < 2·10⁵) pass at c=7 |

Falsifier tables (Z72, PROBE, README) were reproduced by re-running the authors' scripts (not independently). They are
screens, not load-bearing.

## 3. Labels, scope, priority
* No overclaim about ES anywhere. Every note says that its finite results are not ES verifications and that its
  counterexamples are to methods, not to ES. No weak-theory or independence content.
* **Z72 "arbitrary shifts" (WAVES/FRONTIER)** is accurate but easy to misread as "at every shift". Better: "shifts not
  restricted to primes". The density-one statement is elementary (two fixed identities) and should not be read as
  progress on the all-prime question.
* **"Independently replayed to 5·10⁷"** (Z72, WAVES, FRONTIER): no such script exists in the repository. The review's
  by-p engine now independently covers the whole range to 5·10⁸.
* **PHASE43** labels an existential statement witnessed by a certified pair as "PROVED". CERTIFIED is the right label.
* **EXTREMAL priority.** The extremal triple is the strict-greedy (Sylvester/Fibonacci) underapproximation. The theorem
  says that for these n the greedy 3-term underapproximation is also the unique best two-sided approximation. Related
  literature: Kovač, *J. Number Theory* (2025), on eventually greedy best underapproximations, and Kovač–Tang,
  arXiv:2607.28387 (abstract checked), who prove eventual greediness for every rational. Neither appears to contain this
  explicit 3-term, two-sided statement, but I did no full search. No priority should be claimed.
* STATUS.md quotes none of these notes. Nothing here meets the STATUS gate, so **STATUS delta: none**.

## 4. Required fixes, in priority order (note-level ones applied, tagged "(z74 Opus xreview fix)")
1. **counter_tail/README.md (significance).** Add a scope erratum: the uniform cap of 123 is already refuted at
   p=66529 (first support-≤2 shift 323). Among primes with p ≡ 1 (840) and (p+1)/2 prime it is refuted at p=370228321
   (1551); the L-progression itself has no primes this small. The maximum below 5·10⁸ is 2695 (p=44407609). The ≥10¹⁸ run is a cohort comparison (DATA), not a
   new refutation. *Applied.*
2. **Z72_PAIR_PHASE.md (replay provenance).** Replace "An independent implementation … checked the first 50,000,000 …
   single-engine run" with a pointer to the review's full-range by-p replay. Keep the authors' statement as history.
   *Applied.*
3. **Z72_PAIR_PHASE.md (wording).** Say "shifts not restricted to primes (c=3 or c=2r+1)" and "elementary". State that
   the c=31 sharpness example is at the group level. *Applied.*
4. **PHASE43_DENOMINATORS.md.** Change "PROVED (local obstruction)" to "CERTIFIED (paired counterexample; the direct test
   is PROVED)". *Applied.*
5. **EXTREMAL_ES.md.** Add the greedy remark and the literature context of §3. *Applied.*
6. **ROUND3.md.** "No congruence invariant can prove…" becomes "no argument can show that one of O, T always reaches a
   merge at a nonsquare". *Applied.*
7. **§0 blocks** for all seven notes (README, ROUND2 and ROUND3 each get one). *Applied.*
8. Optional, also applied: record the review's explicit s=2 prime instance in Z73_COMPOSITE_PHASE, and the large prime
   in the d=2 cell in mixproof.

## 5. Master-file corrections recommended (orchestrator; I did not edit master files)
**WAVES.md, z72 entry.** Current:
> `+` PROVED: a sharp two-factor criterion at a prime shift (`Z72_PAIR_PHASE.md`). With *arbitrary* shifts, support ≤ 2
>     Type II holds on a relative-density-one set of primes p ≡ 1 (4). An exact sieve to 5·10⁸ (replayed to 5·10⁷) finds
>     no failure. There is no all-prime implication.

Replacement:
> `+` PROVED: a sharp two-factor criterion at a prime shift (`Z72_PAIR_PHASE.md`). With shifts not restricted to primes,
>     support ≤ 2 Type II holds on a relative-density-one set of primes p ≡ 1 (4) (elementary). An exact sieve to 5·10⁸
>     finds no failure (two independent engines over the full range). There is no all-prime implication.

Current: `` `−` … Frozen class-group menus miss a d = 2 fibre (`data/z72/mixproof.md`). `PHASE43_DENOMINATORS.md`. ``
Replacement: `` … (`data/z72/mixproof.md`). Equal phase costs, opposite fixed-x outcomes at c = 43 (`PHASE43_DENOMINATORS.md`). ``

Current: `` `R` Authored by Astra. Not cross-reviewed (no STATUS headline). ``
Replacement: `` `R` Authored by Astra. Opus cross-review: all ACCEPT-WITH-FIXES, fixes applied (`data/z74/xreview/REVIEW_Z72PHASE_OPUS.md`). ``

**WAVES.md, z73 `R` line.** Append: "Composite-shift notes and `counter_tail/ROUND3.md`: Opus ACCEPT-WITH-FIXES
(`REVIEW_Z72PHASE_OPUS.md`)."

**FRONTIER.md line 2772 (z72 update).** Current fragment: "With arbitrary shifts the support-≤2 Type II property holds
on a relative-density-one set of primes `1 mod 4` and in an exact sieve to 500,000,000 (independently replayed to
50,000,000)". Replacement: "With shifts not restricted to primes the support-≤2 Type II property holds on a
relative-density-one set of primes `1 mod 4` (elementary: shifts 3 and 2r+1) and in an exact sieve to 500,000,000
(two independent engines, the second `scripts/z74_xrev_z72phase_bypsieve.py`)". Also add to the paragraph's opening
"(Opus cross-review ACCEPT-WITH-FIXES, `data/z74/xreview/REVIEW_Z72PHASE_OPUS.md`)". The paragraph is itself a stacked
"zNN update" block, contrary to AGENTS.md §4. Fold it into the relevant §6 lines at the next export.

**FRONTIER.md line 2774 (z73 update).** After "…give composite-shift forcing criteria and their obstructions", add "(Opus
ACCEPT-WITH-FIXES, `REVIEW_Z72PHASE_OPUS.md`)". Nothing else changes.

**STATUS.md:** no change.

## 6. Reproduction
```
ulimit -v 6000000; timeout 1800 uv run --offline --no-project --with sympy --with numpy \
    python scripts/z74_xrev_z72phase_checks.py            # 44 checks, 86 s; log data/z74/xreview/z72phase_checks.log
ulimit -v 6000000; timeout 1800 uv run --offline --no-project --with numpy \
    python scripts/z74_xrev_z72phase_bypsieve.py 1 500000000   # 23 s; log data/z74/xreview/z72phase_bypsieve.log
```
The authors' replay commands (all 11) were also re-run, and all passed (2 processes at most, 6 GB virtual limit; log
`data/z74/xreview/z72phase_author_replays.log`). The authors' sieve engine was rebuilt and run to 5·10⁸; its output line is
appended to the by-p log. SymPy `isprime` is deterministic below 2⁶⁴, and the two larger primes are Pocklington-proved.
A self-review by a separate subagent found the issues fixed in this version: the 'same family' wording of P15, and
weak spots in several checks (now asserted).
