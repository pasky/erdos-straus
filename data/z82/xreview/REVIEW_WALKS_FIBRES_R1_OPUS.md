<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Claude Opus review of Wave z82 Lane 5 (notes/z82/WALKS_FIBRES.md). Verify every proof step, trap/escape construction, elliptic-fibre algebra, and finite computation. Cap any replay at ≤15 min.

Commit log:
commit 271ba244486a2a2a1f931d70d35e2b22a2f77492
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 19:58:38 2026 +0100

    z82: bound reciprocal walk closures and delays; cross rank-two fibres to the sharp slice denominator

 data/z82/walks_fibres/ap120120.txt  |   4 ++
 data/z82/walks_fibres/ap840.txt     |   3 +
 data/z82/walks_fibres/chords.txt    |  12 ++++
 data/z82/walks_fibres/controls.txt  |  42 ++++++++++++
 data/z82/walks_fibres/corridor.txt  |   3 +
 data/z82/walks_fibres/dickson19.txt |   2 +
 data/z82/walks_fibres/examples.txt  |   2 +
 data/z82/walks_fibres/fibres.txt    |   6 ++
 data/z82/walks_fibres/largeq.txt    |   5 ++
 data/z82/walks_fibres/panel.txt     |  28 ++++++++
 data/z82/walks_fibres/planes.txt    |   6 ++
 notes/z82/WALKS_FIBRES.md           | 128 ++++++++++++++++++++++++++++++++++++
 scripts/z82_wf_bfs.c                |  59 +++++++++++++++++
 scripts/z82_wf_chords.py            |  28 ++++++++
 scripts/z82_wf_controls.py          |  25 +++++++
 scripts/z82_wf_examples.py          |  29 ++++++++
 scripts/z82_wf_fibres.py            |  70 ++++++++++++++++++++
 scripts/z82_wf_planes.py            |  20 ++++++
 18 files changed, 472 insertions(+)

Review:
**Verdict: the substance holds up. I found no mathematical error and no failed replay.** Three things need fixing before export: one real scope gap in §5 G, an oversold headline, and two small replay-documentation errors. The label and the `BARRIER-SCOPED` triage are appropriate. The single commit touches only the note, scripts and data; no master files are modified, which is correct for a lane.

## What I replayed (≈11 min of compute in total)

All outputs are byte-identical to the committed data files:

- **Walk censuses:** `panel`, `ap840`, `ap120120`, `largeq`, `dickson19`, and the full `corridor` run (10m15s) all match. Every histogram sums to its "tested" count.
- **Other scripts:** `examples`, `fibres`, `controls`, and (with the PYTHONPATH from the note) `planes` and `chords` all match.

**Independent checks:**

- **Walk search:** I wrote a separate Python breadth-first search (sympy divisors, Euler-criterion characters). It reproduces shortest depth 5 at 14571481 with (t,v)=(2919,128), and depth 4 at 2521, 5569 and 183783601. It also gives depth 1 at 212574092116681 via s=101, v=1487. That prime is beyond the C engine's 1.25·10¹³ size limit, so this is new coverage. The histogram over p≡1 mod 840 up to 3·10⁶ matches the C engine exactly.
- **Weierstrass map:** a symbolic sympy check confirms that the §4 point map, with weights (1,1,w), sends the plane section onto Y²=X(X²+AX+B). The remainder modulo the curve equation is zero. So the u=1 rank certificate genuinely applies to the plane section; even a non-birational map would carry independence back.
- **ET triple counts:** a brute-force enumeration gives 15, 18, 9, 15 and 61 positive triples at 409, 577, 2521, 3361 and 102001, matching what the z80 enumerator feeds into `planes` and `chords`. I did not check 8813281.

## Proofs checked line by line, with no error found

- **A (closure size):**
  - The closure C equals the union of doubling orbits, and the stabilizer lemma holds (y must be negative because H consists of residues).
  - 3∈H follows directly, since every ⟨2⟩-coset has a representative below p/2.
  - The Furstenberg compactness step is right: a Hausdorff limit is still invariant, finite limits are permuted, and the distance doubling with 4η separation forces each approximant into K.
  - The squares-of-primes product count works, and the 14477 reduced 7-smooth fractions separate mod p for p>10⁹.
- **B (depth exactly one):**
  - The constants check: 101≡1 mod 4, (101/73)=−1, 1487≡3 mod 4, 1487≡73 mod 101, p≡1 mod 8 is forced, and the characters come out as claimed.
  - The FHRSS application is valid. Taking the pair d=L=1 (1 is primitively represented) gives gcd(129, 202Q)=1, and Lemma 3.6 does force m′ to be odd with all prime factors ≡1 mod 4. The parity caveat about Thm 1.1 alone is correct.
  - In the general-q version, q≡1 mod 840 is a sufficient condition, not a necessary one; it is there to avoid 3, 5 or 7 dividing p+q. That is fine.
- **C (long delays under Dickson):**
  - The corridor algebra holds: the x_i are integers, odd and negative; s divides p+x_L; (p/s)=−1 and (v/p)=+1.
  - Dickson admissibility holds at 2, at q, s and v, and at primes above q.
  - The single-path argument holds, and the height test p≥3x_i−2 against x_i>p/2 is correct.
- **D (second plane):**
  - Vieta gives T_Q·T_W=w; the degeneration at t=0 is v·[j·yz − g·v(y+z)]; the gluing values are −kg and −(p+1); the valuation-matrix independence and the use of Silverman specialization are all correct.
  - The F₅ rank certificate logic is sound: no 5-torsion, the six projective pairs are covered, and only good-reduction primes are used.
- **E (b and pb never occur):** I re-derived both slice congruence chains and the height bound H, including the difference p⁴/16−3p²/4−3p/4−1/3.
- **F (transverse planes):** k must divide k′, the divisibility equivalence holds, and MD≠g² follows from S≥1 together with E.

## Required fixes

1. **§5 G has a scope gap.** The bound k≤2H_s assumes the auxiliary A is a signed solution with all coordinates nonzero. But the cubic 4xyz=p(xy+yz+zx) contains the integral axis points (n,0,0), (0,n,0) and (0,0,n), and §4 itself uses O_u as the group origin. For such an A, |A_x| is unbounded and the argument fails.
   - The finite panel is unaffected, because `chords.py` reports zero axis third-points.
   - The general statement should read "A with nonzero coordinates", or the axis case needs a separate argument.
2. **The headline oversells D.** W=(b, pb, p/2) is just the classical split 2/p = 1/b + 1/(pb). The plane is constructed through Q and W after the fact (w=T_Q·T_W). The note does concede this in §4, but the Result line should lead with what is actually new:
   - the sharp slice obstruction E;
   - the bounds in F and G;
   - the rank-≥2 transverse fibre.

   "Reduces the denominator to 2" should be framed as the trivial point W lying on a rank-two fibre.
3. **Replay documentation.**
   - The note says SymPy is needed only for `examples`, but `controls.py` also imports sympy.
   - The PYTHONPATH relies on cache hashes (`archive-v0/<hash>`) specific to this machine, so other machines cannot replay `planes`/`chords` as written. Add the cypari2 version or the actual install step.
   - The claim that "z81's Python search independently returned the same path and pop count" has no artifact behind it. My independent BFS confirms the path and depth, but not the pop count.

## Minor points

- In §3 C, the parenthesis about nonproportional forms is garbled. The correct reason is that the ratios intercept/slope differ by q/(A_i·M).
- In C, "the only positive proper divisor" should say that "positive" means character +1; otherwise it is easily misread.
- E is a nice, crisp elementary lemma. Its novelty or priority was not checked, and it is plausibly folklore; the note makes no novelty claim, which is correct.
- A cross-lab review is still owed before any promotion beyond `BARRIER-SCOPED`. `STATUS delta: none` is appropriate.

Replay outputs are in `/tmp/rv82/`.
</code-review>