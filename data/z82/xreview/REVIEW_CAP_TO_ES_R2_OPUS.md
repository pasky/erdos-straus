<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="16390995a">
A separate reviewer subagent was asked to review the changes in `git log 16390995a..`. Its request and review follow.

Request: review changes since 16390995a carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Full hostile cross-lab Claude Opus review of Wave z82 Lane 1B Round 2: notes/z82/CAP_TO_ES.md §§6–10 and §0, scripts/z82_c2es_{min,round2}.py, data/z82/cap_to_es/{min,r2}.txt. Check every proof step, hypothesis, quantifier, number, label, scope and falsifier. Verify Lane 1A single-f transfer and whole-avoider ceiling against 7984da083, Lane 5 against 271ba2444. Check minimum search and rectangle. Cap all computational replay at ≤15 minutes, ulimit -v 6000000, timeout ≤900, ≤2 processes, uv run --offline --no-project python -B. Do not write repository files. State actual independent-check coverage and all issues found.

Commit log:
commit 215660b667fdb80dd2bf48088ae24786f6b6e421
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 20:50:56 2026 +0100

    Record pending R2 cross-review after reviewer authentication failure

 notes/z82/CAP_TO_ES.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

commit 915267272ae10313b8b1ebdc5eba920586ad50e9
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 20:50:22 2026 +0100

    Classify linked minima branches, transpose rectangles and separate CRT ceilings

 data/z82/cap_to_es/min.txt |  48 +++++++++++++++++++
 data/z82/cap_to_es/r2.txt  |  26 ++++++++++
 notes/z82/CAP_TO_ES.md     |  82 ++++++++++++++++++++++++++++++--
 scripts/z82_c2es_min.py    |  89 +++++++++++++++++++++++++++++++++++
 scripts/z82_c2es_round2.py | 115 +++++++++++++++++++++++++++++++++++++++++++++
 5 files changed, 356 insertions(+), 4 deletions(-)

Review:
**Wave z82 Lane 1B Round 2 review (cross-lab Opus): `CAP_TO_ES.md` §§0, 6–10 and the new scripts and data, commits 16390995a..215660b66**

**Verdict: ACCEPT WITH FIXES.** I found no mathematical error in §§6–10. One certificate is not complete as written (issue 1). The remaining issues are about labelling and wording. No claim to have proved ES is made or implied, and ES remains open. The commits change only the note, scripts and data; no master file was edited. I wrote nothing to the repository; all my work stayed in `/tmp`.

### What I checked by hand
I checked every algebraic step below, line by line.

- **§6, F:** all three branches hold.
  - The identity `4tAB=pC(D+t)` and the product form of (2).
  - The inequality `(1/3+1)·2<4`.
  - The launchpad converse.
  - The reduced fraction `(Dt/h)/(Z/h)`.
- **§6, G:** holds.
  - The bound `t≤pD/(2D−p)<p` when `D>p`.
  - When `t=1` the output is integral and Type II, and the seed lemma then gives a carrier below `p`.
- **§6, integral-seed lemma:** holds.
  - `λ=p` is impossible because `p≡1 (4)`.
  - `D≡3 (4)`.
  - In the Type II case `λ<p`.
  - In the Type I case `p∤D` rests on the cited z81 sign result, which I checked numerically (below).
- **§6, unlinked identity:** holds.
- **§7, H:** holds.
  - The four merged triples, including (3).
  - The carrier criterion "`4|a+b` and `p²∤a`".
  - The transposed data `D'=a, t'=b, A'=gD, B'=gt`.
- **§7, sublinear bound:** `2gR²−R≤p` holds.
- **§7, progression:** holds.
  - The identity `a+pb₀=4DtJ` by direct expansion (both sides equal `1546688J²+20436J` after multiplying by 7).
  - `b₀≡1 (4)`, and coprimality at 11 and 13.
  - `D/p→1.857`.
  - At 13 the valuations go from (0,0,0) to (1,1,−1) to (0,1,1). The squareclass (W) invariant therefore excludes the final triple from the pivot orbit.
- **§8, I:** the multiplier `(Mx_i−n)/n` is a unit at `l|M`, and the 2-adic valuations of W stay fixed.
- **§8, J:** holds.
  - Both values of `j` are coprime to `g`.
  - The congruence on `e` alone gives integrality of both coordinates.
  - `(Z,D)=1` holds exactly when `(e,D)=1`.
  - Lane 5 E at 271ba2444 matches; I re-derived its divisor argument at `x=b`.
- **§9, K against Lane 1A at 7984da083:** holds.
  - The substitutions match: `x=VA−J` and `v_s(x)=a` when `d>a`.
  - The debt is `max(0,d−2a)`.
  - Linkage allows `d≤2a+M`; full clearability allows `d≤2a+min(M,a)`.
  - With exponents 1,…,b the height condition is still met, since `b(b+1)/2 ≤ 1+b(b−1)`.
  - Tag 1 stays linear, so the activation class argument in H carries over.
  - The classes keep Jacobi symbol −1, because J is supported on the primes of A.
  - The multiplicity bounds are `F(s)=M+3` (linked) and `F(s)=4` (clearable). Lane 1A C's proof uses only `F(p)`, `F(p^a)≤B^a`, `F≪n^ε` and `F⁴` under Shiu.
  - So the exponents are (M+3)/(M+4) for the linked dictionary and 4/5 for the clearable one. At M=1 the two dictionaries coincide.
- **§10, L (conditional on Dickson):** holds.
  - The base case `T(2D−1)≤D` holds.
  - The linear forms are admissible because each takes value 1 at `v=0`.
  - Removing the large primes from a divisor pair keeps residues mod `jD`, and it keeps the coordinates mod `D`.
- **§10, search:** both slice equations and the range argument are correct.

### Independent checks
- **Byte-identical replay** of `min.txt` and `r2.txt`: the same engine, run in 2.2 s and 0.4 s.
- **New independent code** (full factorization by trial division, my own Miller–Rabin):
  - **J test** at 5, 41, 109, 409, 577, 2521, 3361, 5569, 9601, 21841 and 8813281: results match the note, with every non-hit list empty.
  - **Brute force without divisor search** at 8/11 and 8/241: no packet with `D=3`, and the `D=5` witnesses are reproduced. Hits also confirmed at 8/17 and 8/131 (`D=3`) and at 4/9 (`D=5`) and 4/25 (`D=3`).
  - **Census:** there are 19,552 primes `p≡1 (8)` up to 10⁶. On every 7th one (2,794 primes), my own search finds a `D=3` hit within 12 offsets.
  - **Dickson control at 10311841:** the three primalities hold, `p≡1 mod 27720`, the first offset misses and the second offset gives the same hit as the note.
  - **Rectangle** at `j=0` and `j=1`.
  - **Seed lemma** on all 8,334 integral solutions for primes `p≡1 (4)` below 3000: no failures, including `p∤D` at Type I.
- **Not independently checked:** the analytic content of Lane 1A H/C, z81 V, BV/BT/Shiu, and KARY2/3. I treated these as cited inputs.

### Issues found
1. **Certificate defect (medium).** In `z82_c2es_round2.py`, `lanes()` builds the divisors of `g²` with `divs(((g,2),))`. At `p=8813281`, `g≈3.9·10¹³` is at least 10⁹, so `factors` only trial-divides up to 500. It returns `{433:1, 89692760737:1}`, where the second entry is the composite `10177·p`. Only 9 of the 27 divisors of `g²` are tried. So the §8 claim "CERTIFIED (complete…)" is not supported by the script at that prime. My complete run confirms the result is still empty. Fix: pass `((p,2),(b,2))` as the parts.
2. **§0 Label and Triage are incomplete.** The Label names Schinzel H only. It omits Dickson (needed for L), z81 B2_DUALITY §3 H (seed lemma, Type I) and Lane 5 E (J). Triage does not classify F, L or the seed lemma.
3. **The RECORD triage sits oddly with "STATUS delta: none".** The note should say explicitly why K/D/E are not proposed for STATUS, or propose the FRONTIER-only placement.
4. **§7 "four possible carriers" needs a sentence.** Exchanging at the `p`-bearing side `b` (with `p∥b`, `4|a+b`) gives a valid linked packet with carrier `b₀=b/p`, outside the `p|Z` chart. The qualifier "without p-cancellation" covers this, but the sublinear bound ignores `b₀` as a candidate, so the omission should be stated.
5. **Understatements (harmless).**
   - At 4545, 10305 and 67425, `D=7` is the least eligible odd carrier (3 and 5 divide `n`). These are true minima but are labelled "upper"; the labelling rule in `min.py` is ad hoc.
   - The "outside the pivot orbit" argument in §7 holds for every `j`, since `J≡2 (13)` and 13 never divides `b₀` or `p`, not only at `j=0`.

### Debate points
- The census (`D₊=3` at every tested prime, including all the hard controls) combined with L invites a "`D₊(p)=3`" target. The note rightly states no such target, because the seed lemma's converse is open. If one is ever posed, it must first pass the FRONTIER §4 screens.
- K's 5/6 is a rate for a weaker relaxation, which contains Lane 1A cap one. It should not be read as an improvement on 4/5.
- §0 still says Round 2 cross-review is owed. This review can supply it once issues 1–2 are fixed.
</code-review>