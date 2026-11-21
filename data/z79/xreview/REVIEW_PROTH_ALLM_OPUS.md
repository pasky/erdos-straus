<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab review of notes/z79/PROTH_ALLM.md and scripts/z79_proth_* and their certificates. Verify cubic sign identity and implications for density and all-s covers; independently check finite claims. Return complete review as tool output, do not edit. Use uv run --offline --no-project python -B, timeout ≤1800 and ulimit -v ≤6000000 on any Python run; do not spawn side agents. State your actual model/lab.

Commit log:
commit 2b9b181a0fc4c098167819829f8c82e7a454d430
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 13:51:26 2026 +0100

    Isolate the first cubic CRT sign and certify all Proth exponents through m=12

 data/z79/proth/indices.txt            | 19 +++++++++
 data/z79/proth/period-11-166320.json  |  1 +
 data/z79/proth/period-11-3825360.json |  1 +
 data/z79/proth/period-12-55440.json   |  1 +
 data/z79/proth/replay.txt             |  4 ++
 notes/z79/PROTH_ALLM.md               | 72 +++++++++++++++++++++++++++++++++++
 scripts/z79_proth_check.py            | 40 +++++++++++++++++++
 scripts/z79_proth_indices.py          | 50 ++++++++++++++++++++++++
 8 files changed, 188 insertions(+)

Review:
**Hostile review of `notes/z79/PROTH_ALLM.md`, `scripts/z79_proth_{check,indices}.py` and `data/z79/proth/*` (commit 2b9b181)**

**Reviewer: Claude (Anthropic, Opus family).** The worktree is named `claude-agent-…`. If this note came from a Claude lane, this is **not** the cross-lab review that the STATUS gate requires; an OpenAI/Astra review would still be owed.

**Verdict: ACCEPT with minor revisions.** I found no mathematical error. Every finite claim replays, and the main ones also pass checks I wrote separately from the author's scripts. I made no edits.

---

### 1. Substance

**Theorem 1 (the cubic sign identity): correct. I checked it by hand and by computation.**
- **Factorisation.** H factors as w−1 times the N_i, and these factors are pairwise coprime. Each prime of H is assigned to exactly one factor by the order of w at that prime.
- **Evaluation on each factor.** On N_i, with η=w³ of order 3^{i−1}, the product ∏(1+Tη^v)=1+T^{3^{i−1}} gives L(2^{3^{i−1}},z)^{3^{j−i}}. For i≥2 the denominator is the same expression, because 8^{3^{i−2}}=2^{3^{i−1}}. For i=1 we have L(2,z)=−1, since 1+2z²=−(1+2z). On w−1 every factor is 3/3=1.
- **Class count.** One of 1±dt is ≡0 mod 3, and the same choice of sign works in both F's, so inverting both is legitimate. The zero residue mod q has gcd exactly q, a power of 3, so it is admissible in R₃. This gives (G₁/G₀)^{q/3}=g^{q/3}, using G₁=[B₃]=[9]=g². The j=1 case (second F empty) is also right.
- **Independent check** (my own PARI script using `matsolvemod` membership in R₃, not the author's code). For h=3,9,15,21,27,33,39,45,51,57,63,75,81,99,105, Z is the claimed sign and Z·3^{−q/3}∈R₃. Composite d is included (75, 105).
- **Bound is not sharp.** ord(g) is 2 when 3∥h and 6 when 9∥h. At h=27 and h=81 the actual order is also 6, against the bound 2·3^{j−1}=18 and 54. This matches the z78 census (index 6) and supports g⁶=1 on the tower. The note correctly does not claim that; it could cite this as EVIDENCE.
- The caveat that the bound for pure 3^j already follows from the doubling orbit is correct, so the new content is independence from d.

**Theorem 2 (the two tests): correct.**
- **Test 1.** Multiplying the telescope by 2=B₁/B₋₁ gives −1 of class g^b. The slots Φ₂(2)=3, Φ₆(2)=3 and B_m (gcd(m,h)=1, B_m | k, ≡1 mod 16 for m≥4) each have class g.
- **Test 2.** Here −1/c=1−2^a=2^a∏B_{2^i}, of class g^b=1 when L | b. The edge case b=0 is impossible for h≥9, which is harmless.
- **Computational confirmation.** Test 1 holds at h=33, 57, 99. Test 2 instances found by search all pass R₃ membership: (h,a,b)=(33,17,4), (57,29,8), (69,5,6), (129,65,6).
- **Gap to fix: Test 1 is empty for 27 | h.** If 2^b≡−1 mod h then 2^b≡−1 mod 3^j, which forces b≡3^{j−1} mod L. So b mod L≤3 holds exactly when j≤2. The note says Test 1 "includes" 3∥h and 9∥h but never says it is empty for j≥3. State that only Test 2 reaches j≥3.
- **Infinite classes.**
  - h=3·11^r and 9·11^r work: 2 is a primitive root mod 11^r, and b=15·11^{r−1} is ≡3 mod 6.
  - The Test 2 construction checks out: v₂(o)=2 from (2/a)=−1, 3∤o, and the CRT conditions are compatible. h has exact 3-valuation j, a | h+1, and L | b.
- **Density argument.** It is sound as scoped:
  - The fresh-prime factors (1+X^{g'ℓ})/(1+X^{g'}) are disjoint from each other and from Φ₂ and Φ₆.
  - The degree D contains q, and s/(rD) is odd.
  - The mod-7 fallback covers 3∤s.
  - The gap at 0<v₃(s)<j is honestly disclosed.

**§3 Proposition (index of R divisible by 6 when 9|h): PROVED and correct.**
- I reproduced the logs mod 7 (base 3) and mod 73 (base 5).
- The parity of log₇ and the value of (log₇−log₇₃) mod 3 are constant on the gcd classes mod 9.
- Equal gcd with h implies equal gcd with 9, and B_a mod 511 depends only on a mod 9. So the result holds for every h with 9 | h.
- This strengthens z78 §4's proved lower bound ("index even"). It belongs in §0's Result line rather than under triage DATA.
- **EVIDENCE table.** `z79_proth_indices.py` reproduces `indices.txt` exactly. My separate algorithm (HNF over all CRT components with no primary split, same PARI engine) gives the same indices for all 12 h. It also gives index 6 at h=45, 63, 81, 99. The label can become "two implementations, one engine".

**Theorem 3 (all s for m=11, 12): CERTIFIED replay is good.**
- The documented replay finishes with 0 misses. It matches `replay.txt`.
- **Independent replay** (my own big-integer code, no import of the z78 checker):
  - Coverage of every residue is recomputed separately.
  - For every non-X row, I built and cross-multiplied an explicit triple at the first two exponents ≥64 in its class. This covers D, II, K and W; all five W cases (4 dividing u, t, v, A or tv−1) have explicit identities, so no Jacobi symbol is needed. M rows were tested against Mordell's six classes or by scaling from 5 or 7.
  - For the X rows I built an explicit A and triple for **every** unit source (12 for m=11, 22 for m=12), at real exponents s=4eℓ.
- Intermediate file: `period-11-166320.json` has left=[24, 83184], as stated. The D row 47 on s≡1 mod 23 is simply z78's "s≡1 mod 2m+1" rule.

**Corollary (transfer to m≡11 mod T): correct, and I tested it.**
- The fixed-row part of T is 956340. Running the z78 checker with m=11+956340 and m=11+2·956340, with X removed, leaves 28 residues uncovered. All are ≡0 mod 41580.
- My explicit-triple sampler also passes for every row at m=956351.
- The dyadic part (n≡1 mod 2^{≤64}) and the size monotonicity are fine. The s<64 step via n_{11,s} | n_{m,s} is fine.
- **Missing falsifier-screen line.** At transferred m the square exponent s=2m+2 is ≥64 and is handled by a fixed row. It is consistent only because 23 | T forces 47 | 2^{2m+1}−1, so the D row 47 catches the square. Add this to F1; at present F1 covers only Theorem 3.
- The wording "containing infinitely many m" should be "every m≡11 mod T". The claim could also be strengthened: only 28 of the 92 lifts of 0 mod 41580 are uncovered.
- There is no conflict with z78 Cor 9.1: T is even, so m is odd and is never a multiple of lcm(1,…,R).

### 2. Form and consistency
1. **Theorem 3's label omits dependencies.** W rows rely on the good-word theorem (DEDEKIND_ES Thm 4.5 / Z64_SDEEPF Thm 2.1) and II rows on THIN_CYCLO §1, as z78 Thm 3 lists them. Add them.
2. **Triage.** "HEADLINE" overstates the note. Both items extend existing STATUS §1C rows, so RECORD is right. The STATUS delta is consistent with the current STATUS lines 85–96.
3. **Missing statements.** There is no "external priority unverified" line.
4. **Unclear wording.**
   - "Reflected cubic norm" and "common binomial class" in the Result line are not defined in the body.
   - Symbols clash: g (the class) vs g′ (a gcd), and D (the degree) vs D rows vs d.
   - The second sentence of F2 is cryptic.
5. **Sanity check scope.** `z79_proth_check.py` checks only the *value* of the sign Z, not the class identity [Z]=g^{q/3}. Say so in the replay description. The class identity is confirmed above for h≤105.
6. **Data presentation.**
   - `data/z79/proth` has no README.
   - Mark `period-11-166320.json` as an intermediate, non-certificate file.
   - In `indices.txt` the per-prime lines print *before* their `h=` header, and q=73 is always printed (a debug artefact).
7. **Branch hygiene.**
   - The branch is one commit behind main (c66c0b62c). The `main..` diff therefore shows a spurious reversal in `notes/z78/ANALYTIC_WILD.md`; the three-dot diff is clean. Rebase before merging.
   - No master files were edited, which is correct for a lane.

### 3. Bottom line
I found no errors in Theorems 1–3, the §3 Proposition or the Corollary. The finite claims hold up under the author's checker, a separate big-integer replay that builds explicit triples, and a separate group-quotient computation. The fixes needed are clarifications: Test 1 is empty for j≥3, F1 needs a line for the transferred m, dependency labels need completing, and the note needs better presentation. None of this proves ES in general, and the note claims nothing of the kind.

My scratch scripts are in `/tmp/rev_z79/`: `quot.py`, `idx.py`, `t2.py`, `indep.py`, `xall.py`, `transfer.py`, `indep_tr.py`. Every run used `ulimit -v` ≤6000000 and `timeout` ≤1800.
</code-review>
