<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="91c459331">
A separate reviewer subagent was asked to review the changes in `git log 91c459331..`. Its request and review follow.

Request: review changes since 91c459331 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Full hostile cross-lab Claude Opus ROUND 2 review of notes/z82/WALKS_FIBRES.md §§7–11 and all new R2 scripts/data. Check every proof step, especially exact-depth-two sieve (absolute constants/order of limits), saturation/BLMV, explicit W plane moves, rank certificates, rank-four Picard argument, MW and dyadic/linked bounds. Verify finite computations. Replay R2 only, ≤15 min total; do NOT rerun the already-reviewed R1 corridor scan or other R1 censuses. Serial replay, use §11 limits (ulimit -v 6000000; uv run --offline --no-project python -B) and cache PYTHONPATH from R1 if needed. No repository edits or agent-start. Return full nonempty verdict with issues, scopes, and checks.

Commit log:
commit 2130d2131b45a7386ab53467dc9e311ff2c453ce
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 20:47:31 2026 +0100

    Mark R2 Opus review pending on provider reauthentication

 notes/z82/WALKS_FIBRES.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

commit e77d082e9baf9a5ba17752e14fe6cb0ac3f63451
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 20:46:53 2026 +0100

    z82 R2: sieve exact depth two, quantify closure, and escape W on symmetric rank-two planes

 data/z82/walks_fibres/r2-hcert.txt     |  15 +++++
 data/z82/walks_fibres/r2-mw.txt        | 104 +++++++++++++++++++++++++++++++++
 data/z82/walks_fibres/r2-sat.txt       |   1 +
 data/z82/walks_fibres/r2-secants.txt   |   7 +++
 data/z82/walks_fibres/r2-symfamily.txt |   1 +
 data/z82/walks_fibres/r2-wplanes.txt   |   6 ++
 notes/z82/WALKS_FIBRES.md              |  83 +++++++++++++++++++++++++-
 scripts/z82_wf_atw.py                  |  28 +++++++++
 scripts/z82_wf_hcert.py                |  28 +++++++++
 scripts/z82_wf_mw.py                   |  50 ++++++++++++++++
 scripts/z82_wf_saturation.c            |  14 +++++
 scripts/z82_wf_secant.py               |  41 +++++++++++++
 scripts/z82_wf_symfamily.py            |  42 +++++++++++++
 13 files changed, 418 insertions(+), 2 deletions(-)

Review:
# Verdict: R2 of `notes/z82/WALKS_FIBRES.md` (§§7–11), commits `e77d082e9`, `2130d2131`

**Substance: I found no mathematical error in §§7–11.** Every R2 output replays byte for byte, and I independently re-derived or recomputed each certificate the note relies on. The labels (PROVED rel. …, CERTIFIED) and BARRIER-SCOPED with "STATUS delta: none" are appropriate. Nothing here amounts to an ES claim, and the note does not suggest one. There are no blocking issues. Seven form and scope fixes are recommended, two of them before export (items 1–2 below).

## Replay (R2 only, serial, under `ulimit -v 6000000`, about 2.5 minutes in total)
- I did not rerun R1's corridor scan or any R1 census, as instructed.
- For the PARI scripts I set `PYTHONPATH` to the cached `cypari2-2.2.4` (cpython-312 build), `cysignals-1.12.6` and `sympy-1.14.0`.
- The C saturation engine (`sat`) compiles with no warnings and runs in 6.6 s.
- The five Python scripts took 1.0 s (`hcert`), 0.1 s (`mw`), 1.0 s (`symfamily`), 135 s (`atw`) and 4.9 s (`secant`), each under 75 MB.
- All six outputs are identical to the committed `r2-{sat,hcert,mw,symfamily,wplanes,secants}.txt`.
- The repository is unchanged. No master files were touched, which is correct for lane work.

## Independent checks (my own code, not the lane's)
- **Saturation census:** there are 395 primes ≡1 (mod 840) up to 10⁶, and Σ(p−1)/2 = 96,616,380, matching the engine. A separate Python breadth-first search (sympy divisors) gives closure = all nonresidues at 28 of those primes, including the largest, 997081.
- **§8 I, planted exit:** I ran a toy version with q=73, s=157, v=443, building p by CRT (36-digit primes, 5 instances). In each, q is the least nonresidue, N is negative, s divides p+N with (s/p)=−1, sv divides p+s+v, (v/p)=+1, and t≥2.
- **§9 J, rank certificate:** I recomputed point counts by brute force at 7, 17 and 19, and the columns 4(W−O) and 4(T−O). The progression 4201, 2988721, 14926801 gives identical data (12; (13,11),(4,10); identity,(4,14)). No relation over F₅ survives both primes. This confirms that the reduction is constant along the progression.
- **§9 K, 2-descent at 8813281:** I used exact squarefree kernels instead of Legendre masks. All 7 nontrivial products of [X(W−O)], [X(T−O)] and [B] are nonsquares, and A²−4B is not a square. So rank ≥2 holds. The hit's ratio y/x is 20989, not p.
- **Factorisations:** p+1 at the six panel primes has odd part made only of primes ≡1 (mod 4): 5·41, 17², 13·97, 41², 51001, 433·10177. This is consistent with the empty ratio-p panels.
- **BLMV source:** I fetched the paper. Thm 1.10 states κ₇(log log log N)^{−κ₂/100}-density for (ab,N)=1, with κ₂=1/2 when (a,b)=1. The exponent 1/200 and the "absolute constant" claim are correct.

## Proof audit (line by line, no gap found)
- **H (saturation and growth):**
  - The subgroup-labelling certificate (y^h labels cosets of the unique order-h subgroup) is correct.
  - Adjoining only residues m is required, because H lies inside the residues. The script tests all cosets, which is conservative.
  - The z80 B text really does start from |H|≥p^δ.
  - In the BLMV step, an interval of length 3ε contains a radius-ε ball, and Y² ≪ (log₃p)^{1/200}. The product count gives log|R| ≫ log₂p·(log₃p)^{1/500}/log₄p.
  - The Linnik range and the C(t,r) ≥ (t/r)^r ≈ p^{ε/(2+ε)} step both check out.
- **I (exactly depth two; constants and order of limits):** all correct.
  - The CRT choices are units, q is the least nonresidue, and the character signs come out as claimed.
  - Lower sieve: V(z) ≍ log q/log z and 1/φ(2M) ≍ log q/M, both with absolute constants. Bombieri–Vinogradov remainders (including the Siegel–Walfisz term) are fine at fixed M.
  - Root loss: the four classes mod q are right. The two roots of the two-dimensional sieve are distinct since l∤qu. The harmonic mass ≪1/q per dyadic block, summed over log X blocks, is ≪1/q.
  - Depth one: v' ≡ q (mod d) with j≥1, giving O(X log X/z).
  - The order "fix q > C/c, then X→∞" is correct.
- **J (W to T on a symmetric plane):** the plane, both quadratic roots, the slope identity w=(p+1)²/s, the converse (s | p+1, from gcd(s,z)=1) and the density argument via divergence of Σ1/s over s≡3 (4) all check. The 5-torsion and independence logic is the same as R1 D and is sound.
- **K (integral normals and the 8813281 hit):** the r | (x+y−b−pb) criterion, the evenness of c, and the rank-2 normal lattice are correct. The 2-descent logic holds: the image of torsion in E/2E has dimension dim E[2] = 1, (0,0) is not a double, and the Kummer map kills 2E.
- **Rank-four pencil:** this is a rational elliptic surface with ρ=10, and Pic → Pic(E_η) is surjective with kernel exactly the vertical classes.
  - Plane sections of the pencil are integral because of skewness. The four node curves are vertical and independent, giving 10−5−1 = 4, consistent with Shioda–Tate for four A₁ fibres.
  - The sections' coefficients on the three base exceptionals give independence. Testing the nine rational lines is sufficient, and the skewness determinant test is correct.
- **L (Mordell–Weil points and height):** I verified the inverse map algebraically. The script asserts the round trip and the equation on every off-axis row. The bound w/(2d) ≪ p⁴d³ gives d ≫ (k/p)^{1/4}, and combined with Thm D (d ≪ p⁴) this gives k ≪ p¹⁷.
- **M (dyadic pivot):** the share valuations are (−2,−2,−1). Using the pivot formula u↦1−u, others ×u/(1−u) (derived from CAP_TO_ES A), valuations are invariant when all are negative, and the half-share pivot fixes W.

## Issues and recommended fixes (non-blocking; 1–2 before export)
1. **Dependency on an unmerged branch.** L relies on `CAP_TO_ES` Thm D at `16390995a`, which is only on `side-agent/z82-cap-to` and is not an ancestor of HEAD. The §0 Label should name it explicitly ("rel. CAP_TO_ES D"), and the pointer must resolve on main at export.
2. **The §0 Label is incomplete.** It names BV and the sieves, but folds BLMV, BGK (z80 B), Linnik, Furstenberg, Bertini/Picard, the z80 ET enumerator and the CAP_TO_ES D input into "the cited … inputs". List them.
3. **The headline drops the quantifiers.** It should read "for every sufficiently large fixed prime q≡1 (840), ≫_q X/log²X primes in (X,2X] with least nonresidue q". The threshold C/c is unspecified, so no explicit q is certified.
4. **J's scope is understated.** "Fails at e.g. 409" should say that J is vacuous at **all six** panel primes (verified above). The density-one family is exactly the classical s≡3 (4) | p+1 coverage. It would also help to record that the empty ratio-p panels in K are consistent with J.
5. **M has no file pointer.** "Lane 1B A" has no pointer; state the pivot formula inline.
6. **Minor algebra redundancy in I (and in R1 C).** −2 is a square mod q≡1 (mod 8), so "a nonsquare other than −2" and "D=N would require a≡−2" are automatic. Harmless, but simplify.
7. **Form:**
   - Fragments such as "Neither a new density theorem … nor a diameter bound." and "Direct small-prime/coset tests, no use …" should be full sentences.
   - The replay loop sends five outputs to one stdout stream. Give per-file redirects.
   - The script name `atw` does not match its output `wplanes`.
   - The "least normal through H=100" data in `r2-wplanes.txt` is never used in the note. Interpret it or drop it.

## Challenges considered and rejected
- **I: does the planted exit at s count as depth one?** No. s does not divide p+q (it would contradict z-roughness), so the depth-one bound is not circular.
- **J: is the reduction really constant on the progression?** Yes. I checked it empirically at two further primes, and the formulas are regular there.
- **K: could the 2-descent mask confuse E/2E with the isogeny quotient?** No. It only needs 2E to lie in the kernel, and it does.
- **L: does the result conflict with W having d=2?** No. The z'=p/2 case is handled separately.

## Status
Once items 1–4 are addressed, the Review line can read "R2 Opus cross-review: no mathematical errors; replayed". Export should still wait for the item-1 pointer to be resolvable on main.
</code-review>