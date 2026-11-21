# Cross-lab hostile review, Round 2: `notes/z79/R17_ALLDEPTH.md` and `scripts/z79_*` at 0b5f80b15

Reviewer: Claude Opus (subagent), cross-lab for the GPT-6.2 Astra author lane. Scope: `git log f93e582bc..0b5f80b15` (one
commit). Constraints observed: at most 2 compute workers, `ulimit -v 2000000`, every process `timeout` ≤ 1750 s,
`uv run --offline --no-project python -B`, no side agents. Review scripts and outputs live in `/tmp/r2rev/` only and are
not committed. This file is the only thing written to the repository.

## Verdict

**No soundness defect found. I recommend acceptance of both Round-2 claims, with the scope the note gives them:**

1. **PROVED (computer-assisted, relative to the SE reduction, the z78 integer ledger lemmas, BBR and the Round-1 lemmas):**
   the r-generic line has positive sterile measure at r=137 and at every prime 149 ≤ r ≤ 283. With z78 (r ≥ 293,
   including z78's own libm qualification for r ≥ 919), this gives every prime r ≥ 149, plus 137.
2. **CERTIFIED:** at r=17, P has no hit at x=5 (both orientations, hence also at 1/5) at L=12, 13 and 14. With the z78
   depth-11 P certificate and the older Q search through k=15, 5 and 1/5 survive all seven families through depth 14.
   This is a statement about the two points, not about whole cylinders.

This counts as one independent cross-lab hostile review for the AGENTS §3 gate. The sterile threshold is a campaign
quantity, not a published record, so one review satisfies the gate.
The inherited z78/R1 lemmas were not re-audited, apart from the places where R2 changes them; see §5. The margins are
thin. At 173 the margin is 3946 ppm, about 1.6 % of the live mass, and every load-bearing input matters (§4). That is a
reason for exact replays, not a defect. Form problems are listed in §6. None of them changes the result.

## 1. Replays of the author's stages (all byte-identical, empty diff, rc=0)

| stage | wall time | result |
|---|---|---|
| `r2ledger` | 15 s | matches `r2/ledger.txt` |
| `r2flat` | 34 s | matches `r2/layers/{9,11,13,15}.txt` |
| `r2runs` | 625 s | matches `r2/runs.txt` |
| `r2high` | 34 s | matches `r2/high.txt` (B=117..236) |
| `r2shifts` | 629 s | matches `shift.txt`, `wide.txt`, `qs.txt`, and `qbound.txt` via `z79_qsplit.py` |
| `r2point12` | 47 s | matches `point/12.txt` and `point/check.txt` |
| `r2point13` | 311 s | matches `point/13.txt` and `check.txt` |
| `r2point14` | 1181 s | matches `point/14.txt`, including the **full L=14 e-factor stage** (37647 keys, GNU factor 9.7), and `check.txt` |

All stages of `z79_replay.sh` that are new in Round 2 were replayed from source. The Round-1 stages were replayed in the
Round-1 review and have not changed.

## 2. Independent point search at 17 (a re-implementation, not a replay)

I wrote `/tmp/r2rev/ip.c` and `/tmp/r2rev/emode.py` from the mathematics, without reading `z79_endpoint.c` beforehand.
The design differs from the author's on purpose:

* **Different cutoffs.** I re-derived the covering lemma: if e>E, J>J₀, HZ>V and Hd>Y for a hit, then
  (E+1)(J₀+1)(V+1)(Y+1)² ≤ e·HZ·J·(Hd)² ≤ K·U², with K=4p³q³h³jz/68³. I then chose cutoffs that make the
  64-bit-factorable domains (J, HZ) and the cheap Hd domain large and the 108-bit e domain small. For the derivation:
  * H ≤ C(1+e/N)U/(68ad) gives ρ ≤ C²(1+e₀/N)/(68Y).
  * J ≥ 1 absorbs the qe/U term.
  * eZ = 17HJ − (q−p)pa ≤ z p²a.
  * The powers of a and d cancel exactly.
* **Own arithmetic.**
  * J and HZ use my own 64-bit factoring: Miller–Rabin with the first 12 prime bases, which is deterministic below
    3.3·10²³, and Pollard–Brent. There is no GNU factor. Asserts guarantee n < 2⁶⁴; this needs V ≤ 1800 at L=14.
  * e-mode uses GNU factor only to *find* factors. Every returned factor is re-checked in gmpy2 (strong BPSW and 50
    Miller–Rabin rounds), and so is the product. All triples a·b·d=(N+e)/4 are then enumerated by exponent splitting.
  * Hd uses a stable long-double small root a = 2K/(t+√(t²−4pK)), widened by a relative margin of 10⁻¹⁷ and an absolute
    margin of 0.05, followed by exact integer verification of every candidate. Here a ≤ 1.2·10¹⁶, and long double carries
    a 64-bit mantissa, so the rounding error is <0.01. For p>q the decreasing branch of a(t−pa) cannot reach a ≤ t/(p+q),
    because (p+q)²(N+e₀) < 4U² (asserted). For p≤q the vertex lies beyond t/(p+q).
* **Exact constants** (`consts.py`, Fractions). 1/K = 628.50, 628.78 and 628.84 at L=12, 13, 14, so the author's 1/500
  has slack. The author's cutoffs pass with E·J₀·V·Y²/(K·U²) = 1.50, 1.85 and 1.67, in both orientations. Σ_{H≤Y}⌊Y/H⌋
  = 45205760, 118188494 and 502779857, which reproduces the `vis` counts in `point/*.txt`.

The cutoffs I used (E,J₀,V,Y), all passing the exact strict test in both orientations:
12=(20000, 600, 500000, 10⁷); 13=(20000, 300000, 30000, 3·10⁷); 14=(20000, 31300000, 1800, 2·10⁸).

**Result: zero hits in every domain, at every level and in both orientations.** At L=14:
* Hd: 3853652258 (H,d) pairs per orientation.
* J: 7825000 keys per orientation.
* HZ: 13788 keys for (1,5) and 2763 for (5,1).
* e: 4706 keys, 12015093 triples.

**Positive controls for my code** (`posctl.py`, `epos.py`). I used the M17B P solution sets at L=2,3 (p3, p5), with
synthesized (p,q)=(p,−pa/b mod U) and e ≤ N. The hit set must satisfy expected ⊆ got ⊆ {all genuine data hits}, and the
seeded tuple must be found. Matches: J 2120, HZ 164, Hd 598, e 250 (exact equality for e).

**Precise independent replay scope for depth 14.** The author's full L=14 pipeline was replayed byte-for-byte (§1). In
addition, the claim "no P point hit at L=12,13,14" was reproduced by an independent implementation with independent
cutoffs. That implementation re-derives the covering lemma but uses the same z78 input e ≤ 466⌈√U⌉, z78 (2.3), which I
did not re-derive. The e-domain at L=14 was independently covered only up to e ≤ 20000. The author's e ≤ 160000 range is
not needed for my covering. Only the author's run covers it, using GNU factor.

**Round-1 algebra re-checked by hand.**
* Q identity pa²+qb²+h=Vab, the reflection descent, and the bound dh ≤ (p+q)/2+√(pq): (1,5) forces dh=4, d=1 (square
  centre); (1,7) forces dh=2, V=0.
* The ℤ₁₇ unit counterexample a=c=1, b=(F+1)/(4d−F) satisfies 4abd=Fe+1, a+b=ce and a+5b≡0 (mod F).

## 3. Positive-measure side: audit of the new bounds

**(a) Hadamard in the monic Chebyshev basis (`z79_cheb.c`, also in `z79_runs.c` and `z79_high.c`).** The proof is correct.
* z76 gives det = V₁^{m(m+1)/2}·∏(z_j−z_i) exactly: the columns are polynomials in Z, so this is the Vandermonde
  itself, not a generalized determinant. Replacing x^j by 2^{1−2j}D^jT_j((2x−2α−D)/D) is a unimodular triangular change.
  The column norms are ≤ √ℓ·D^j·2^{1−2j}, so |∏| ≤ ℓ^{ℓ/2}2^{ℓ−1−2s}D^s.
* The code's gain 16(2s−ℓ+1) − ⌈ℓ⌈16log₂ℓ⌉/2⌉ never exceeds the exact 16·(−log₂ of the bound at D=1). The `lo[l]+(l
  not a power of two)` term is ⌈16log₂ℓ⌉.
* `fekete.py` computes the true maxima from Fekete points (±1 and the zeros of P′_{ℓ−1}) for ℓ ∈ {2,…,6,8,12,16,24}. The
  Hadamard bound always dominates them, with slack 0…10.4 bits.
* `log16.txt` is exact on 1..512: 2^lo ≤ i^16 < 2^(lo+1).
* `mant[h]/256 < 2^{h/16}` (lower, for chunk diameters) and `(mant[h]+32)/256 ≥ (mant[h]+1)/256 ≥ 2^{h/16}` (upper, for
  reverse widths) hold by the construction from `lo`. The fractional chunk test s·k ≤ a+gain−1 is strict, as required.
* The 4·9·25·49 wheel (PER=44100) is a valid squarefree majorant for r ≥ 17. The normalization factors h ∈ {2,3,5,7}
  are units.

**(b) Run recurrence and ordering (`z79_runs.c`).**
* The tie-break partition is right. `first = max(i+(n<m), j+(o<m))` assigns a tuple to the largest grid index, with ties
  going to the smallest coordinate number.
* The `break` on an empty row is valid for every J: `first` does not decrease and `top` does not increase as j grows.
* The DP covers [first, k_end) with no gap.
* Truncation: V₁=min(3N,N+4a_max²d_max) by 4a²d ≤ 2N. Also hi=⌊V₁/f₀⌋, d ≤ (N+hi)/(4A²), acd ≤ ⌊(⌊V₁/E⌋+1)/4⌋, and
  the m=0 progression count ≤ 1+⌊(hi−E)/(4AD)⌋. All of these are correct relaxations. There is no unsigned underflow,
  since each tightened upper edge is ≥ lower+1 after the emptiness tests. There is no 128-bit overflow, since A·C·D ≤ T.
* **Instrumented brute force** (`runs_chk.c`). I enumerated all P tuples with unit a,b,c,d,e, squarefree d and e ≥ E.
  Two checks, both passed:
  * The count in *every* evaluated run box is ≤ the box bound.
  * Every tuple lies in exactly one (m,i,j,row-range). That is, the partition is exact; the check is not just that the
    totals agree.

  Cases: (17,7, step 5 and 2, E=2⁶..2¹⁵), (17,9, step 5 and 12, E=2¹⁴..2¹⁹) and (19,9, step 3, E=2¹⁵..2²⁰). Up to
  1.2·10⁶ boxes per cut. Some singleton boxes are tight (ratio 1.000); none is violated.

**(c) High layers (`z79_high.c`).**
* All log constants are outward:
  * log₂1.5 → 10/16 and 9/16.
  * 4t−1 ≥ 4t·2^{−1/16} for t ≥ 6, used for t ≥ 8. Otherwise 4t−1 ≥ 3t, which is 25/16 bits below.
  * `lgplus` corrections 1, 3, 6, 10 and 16 dominate 16log₂(1+2^{−d/16}).
* The bucket j=⌊(v−lb)/16⌋ is correct, and C truncation toward zero only affects cells with j<jmin, which are skipped
  anyway. bestE ≤ B−jmin ≤ B, so the Horner sum over e=0..B loses nothing.
* **Instrumented brute force** (`high_chk.c`, assert relaxed to B ≥ 20). N=17⁷ (B=29), 19⁷ (B=30), 23⁷ (B=32) and 17⁹
  (B=37, e ≥ 2¹²). Every tuple's cell was visited. The count in each cell is ≤ bestC·2^bestE, and max e in each cell is
  < 2^{j+1}. No violation.

**(d) Short-prefix propagation (`z79_r2budget.py::short`).**
* It mirrors z78 `packed()`: seed v[j] bounds e<2^j (shiftwide prints the running total before adding e ≥ 2^j).
  `fixed(n,j)−fixed(n,j−1)` is the last summand of a cumulative sum, `interval(n,i,j)` bounds [2^i,2^j), and the
  tsum-route condition is copied verbatim.
* `sh` inside `short` is the original packed, so there is no recursion through the monkeypatch. `old.sh=short` changes
  only `z79_pbudget.cost`.
* Using sh(2^b, ·) for N<2^b is inherited and sound: tau_sum, moment and major depend on m only through monotone
  upper-size functions.

**(e) Q5 both-large clipping (`z79_qsplit.py::large`).**
* From 4c²d(ef−1)=(f+F)², each f-band [t,h] has c²d ≤ (F+h)²/(4(tE−1)) = u. V=F²+4c²d ≤ F²+4u, f ≡ −F (mod 4cd), and
  the progression length is ≤ 1+(h−t)/(4CD).
* The restriction to (−d/r)=−1 is valid: both oriented centres −4a²d and −4b²d lie in the class of −d, and only
  nonsquare cells are live.
* C²D ≤ u guarantees c ≥ C and d ≥ D, so there are no negative widths. Dropping z78's τ-min only loosens the bound.

**(f) `z79_shiftwide.c`** is `z78_r2shift.c` with a 128-bit cost/add path, a saturating add (`tot=min(mod,tot+add)`) and a
domain of K ∈ {9,…,15}, r ≤ 157 and N<2¹¹². The diff is exactly that.

## 4. Ledger audit: 173, 149, 137, and what is load-bearing

I recomputed the margins from the printed columns. Charges are rounded up and the margin is rounded down, so they agree.

| r | live mass (ppm) | Σ charges (ppm) | margin (ppm) |
|---|---|---|---|
| 137 | 329105 | 312463 | 16642 (ledger 16645) |
| 149 | 315867 | 301579 | 14288 |
| 173 | 250853 | 246909 | 3944 (ledger 3946) |

Ablation of the inputs of `z79_r2budget.py` (`abl.py`, margin in ppm):

| removed | effect on the newly certified primes |
|---|---|
| `runs.txt` | 137, 149, 151, 157, 163, 167, 173, 179, 191, 197 fail (e.g. 173 → −25718) |
| Chebyshev gain → R1 midpoint gain, in runs | identical to removing runs (137, 149, 157, 173 all fail) |
| Chebyshev gain → R1 midpoint gain, in high | 173 fails (−1126); 137, 149, 157 survive |
| `high.txt` | 137, 149–157, 167, 173, 179 fail |
| shift + wide seeds | 137–179 fail |
| `wide.txt` only | 157 fails (−16856) |
| prefix propagation (`short`) | 157 (−920) and 173 (−2996) fail |
| `qbound.txt` (Q5 clipping) | 137, 149, 151, 157, 167, 173 fail |
| flat Chebyshev layers (`layers/*.txt`) | **no certified prime changes except 233**, which still passes (55136) |

So the Chebyshev–Hadamard bound is load-bearing through `z79_runs.c` and `z79_high.c`. The flat `z79_cheb.c` tables and
the Minkowski line route in them are not load-bearing at any newly certified prime. The note should say this, as Round 1
did (§6, M7).

## 5. What I did not check

* The inherited z78/R1 lemmas: the SE reduction, BBR, the z76 divisor cap lemma as such, the global P/Q tails, `packed`,
  the prime-power sieve logic of `z78_r2shift.c`, `z78_r2q5shift.c`, the libm qualification at r ≥ 919, and z78 (2.3).
* The positive-measure brute-force checks run at small N (2²⁹–2³⁷) and with B ≤ 37 for the high table. The production
  range (B=117..236) uses the same code paths, and I checked those paths for overflow by hand.
* The author's e-domain 20000<e ≤ 160000 at L=14 is covered only by the author's pipeline, which I replayed.

## 6. Form and presentation problems

* **M1, provenance (should fix).** The commit deletes the Round-1 reviewer's evidence under `data/z79/xreview/`: the
  `xp7/` independent P7 data, the `layer_no*` ablation tables and the `replay_*.log` files. Both the Round-1 review
  ("Logs: replay_*.log"; "Files: … xp7/ …") and this note ("CERTIFIED (Opus ablation, full review under
  data/z79/xreview/)") still point at them. An author lane should not delete another lab's review evidence. Add an
  erratum to `REVIEW_R17_ALLDEPTH_OPUS.md` pointing to commit f93e582bc, or restore the files.
* **M2.** `r2ledger` only diffs. Unlike the R1 `ledger` stage, nothing checks that the claimed 28 margins are positive.
  Add `awk '($1==137||$1>=149)&&$1<=283{if($9<=0)exit 1;n++}END{if(n!=28)exit 1}' "$R/ledger.txt"`.
* **M3.** The positive control in `z79_r2check.py` is fragile and narrow.
  * The HZ enumerator, both the author's and mine, does not verify that the key's Z equals the hit's Z. It can return
    duplicates and *genuine hits outside the domain*. Example: `ep 2 31 19 HZ 207` returns (2,88,7), which has HZ=828.
    `got==expected` would therefore fail for some seeds, and passes only for the three seeds that fire per mode.
  * Use expected ⊆ got ⊆ {genuine hits}. This is harmless for completeness.
  * The emax=466⌈√U⌉ path (L ≥ 12) is never exercised positively. Its arithmetic is simple and I checked it.
* **M4.**
  * The R1 replay paragraph ("No external arithmetic package") is now stale: the default replay needs GMP and GNU factor.
  * The R1 table (233: 17614; 239: −21959) sits next to the superseding R2 ledger (233: 140661; 239: 41793). Compress
    the Round-1 sections rather than relying on the single "supersedes" sentence.
* **M5.** "each Hd rectangle search checked 502779857 index pairs": the region is the hyperbola Hd ≤ Y, and the count is
  of (H,d) pairs. The number itself is correct.
* **M6.** `r2point12` alone re-runs `z79_r2check.py`, which validates the committed 13 and 14 files structurally only.
* **M7.** The note should carry the load-bearing map from §4, especially the fact that the flat Chebyshev layer and the
  Minkowski route are not needed, and that the margins at 157/173 depend on the prefix propagation.
* **Counts and wording checked.**
  * Prime counts: 55 primes in [17,283], 28 pass (27 in 149..283, plus 137), 18 new, 27 uncrossed.
  * Live mass at 173: the denominator 5177717 is 173³.
  * Margins at 149, 157, 173 and 139 match the ledger.
  * Depth bookkeeping: P depth L ↔ K=2L−1; Q through k=15 is inherited from z78 PUSH §6.
  * "No libm in new range": no float in any new script.

## 7. Recommended STATUS/FRONTIER wording (if exported)

"Sterile points on the r-generic line for every prime r ≥ 149 and also r=137: PROVED, computer-assisted, rel. z78/R1
lemmas, with z78 for r ≥ 293. Cross-reviewed: Opus R2, byte replay of all new stages and an independent re-implementation
of the depth-12..14 point search. At 17, 5 and 1/5 survive all seven families through depth 14: CERTIFIED, two
independent implementations. 27 primes 17 ≤ r ≤ 139 other than 137 remain uncrossed."

## Files (in `/tmp/r2rev/`, not committed)

* `ip.c`, `emode.py`: independent point search.
* `posctl.py`, `epos.py`: positive controls.
* `consts.py`, `consts2.py`: exact constants and cutoffs.
* `out_*.txt`: logs of the independent runs.
* `runs_chk.c`, `high_chk.c`: instrumented brute force.
* `fekete.py`: Hadamard bound vs Fekete maxima, and `log16` exactness.
* `abl.py`, `nogain/`, `ablation.txt`: ablations.
* `r2*.log`: empty diffs of the author's replays.
