<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="main">
A separate reviewer subagent was asked to review the changes in `git log main..`. Its request and review follow.

Request: review changes since main carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab review of notes/z79/WILD_ES.md and scripts/z79_*: focus on Theorems A,B and all proof interfaces, especially the quadratic-conductor pruning, incidence estimates, small digit repair, coefficient uniformity, scaling, and falsifier scope. Check ledger independently. Review only lane changes, ignore unrelated main drift. Do not edit files; return full report as text. Python only via ulimit -v 6000000; timeout <=1800 uv run --offline --no-project python -B. No side agents. Identify reviewer model/lab if known.

Commit log:
commit 38a6dbf294dd75675f2655e7e548e6f0a7b8349f
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 12:56:26 2026 +0100

    z79: transfer the ES three-quarter exceptional bound to quadratic values

 data/z79/wild_pullback.txt   | 33 ++++++++++++++++++
 notes/z79/WILD_ES.md         | 80 ++++++++++++++++++++++++++++++++++++++++++++
 scripts/z79_wild_pullback.py | 74 ++++++++++++++++++++++++++++++++++++++++
 3 files changed, 187 insertions(+)

Review:
**Hostile cross-lab review of lane z79 (`notes/z79/WILD_ES.md`, `scripts/z79_wild_pullback.py`, `data/z79/wild_pullback.txt`)**

**Reviewer:** Claude (Anthropic). The exact model version is not visible to me.
**Scope:** only commit 38a6dbf. `git diff main...HEAD` touches just these 3 files. The other files in `git diff main..` (STATUS, FRONTIER and others) are main drift and I ignored them.
**Verdict:** **ACCEPT with minor fixes.** I found no fatal gap in Theorem A or Theorem B. One cross-reference gives the wrong reason for the right conclusion (M1). The other points are about scope wording, compressed proofs and whether the result belongs in STATUS.

---

### 1. What I checked

**§1, the pullback.** Multiplying $F(j)v+u\equiv0\ (\ell)$ by $4Av$ gives $(2Avj+Bv)^2\equiv v(\Delta v-4Au)$, so $D$ is correct. The root count is $1+(D/\ell)$ when $\ell\nmid 2Av$, which holds because $\ell>\sqrt X$ and the coefficients are at most $X^{e/1000}$.

**Reduced class.** In the ratio case, $f\equiv-1\ (q)$ forces $(k,q)=1$. In the word case the target $2^{a+b'}w'-1$ is a unit mod $16w'$, so the same holds. Activity together with $(c_0,k)=1$ gives $(k,uv)=1$. The 2-adic bookkeeping is right: $v_2(y)=b'$ and $q=16w'$ for both shapes.

**§2, untwisted supply.** I compared it against the TQ source (`paper/es-threequarter-note.tex`).
- TQ Lemma `wsecond` is stated for $J\subseteq\{k\equiv1\ (4)\}$, but its proof sums over all $k,k'\le K$, as the note says. Its windows $(K^{10},h^{1/6}]$ contain the note's windows because $K^{10}\le h^{e/50}<h^{.4e}$.
- The rectangular-window version of the lattice lemma is a routine adaptation. With $Y=h^{.4e}$ and $K^2\le h^{e/250}$ the error terms are dominated.
- The BV step works: $\sum W(q)E(q)\le(\sum W^2E)^{1/2}(\sum E)^{1/2}\ll h\,t^{-12}$.

**§2, twist pruning. This holds up.**
- Exponent check: with $Q^2T=h^{20e}$ and $\eta=6e$, the bound is $(Q^2T)^{3\eta/(1+\eta)}\approx h^{360e^2}=h^{.0036e}<h^{.02e}$. I confirmed MV Thm 28.6 / (28.30) in `sources/omega9/montgomery-mnt3.pdf`: $N_2\ll(Q^2T)^{3(1-\theta)/(2-\theta)}\log^6$, valid for $\theta\ge1/2$.
- Conductor: $4q|D|\ll h^{3.21e}<Q=h^{5e}$.
- Fresh-prime lemma. Take an odd $p\nmid2A\Delta$ with $v_p(\Delta v-4Au)$ odd.
  - If $p\mid u$, then $p\mid\Delta v$, so $p\mid v$, contradicting $(u,v)=1$.
  - If $p\mid v$, then $p\mid4Au$, so $p\mid u$, the same contradiction.
  - So $p\nmid qv$ and $v_p(D)$ is odd. Then $\chi\chi_D$ ramifies at $p$ for every $\chi$ mod $q$, which forces $p\mid d$.
  - The resulting count (at most $\tau(2A\Delta d)\cdot h^{.5515e}$ values of $u$ per $v$ for each list entry) is per list entry, not per character. That is correct.
  - The trivial character, square $D$ and $D=0$ are all inside the discard. Lost mass is $\ll K h^{-.42e+o(1)}t=o(1)$.
- Explicit formula: the $O(h^{1-6e}\log)$ zero sum, the $hT^{1-N}$ tail, the imprimitive correction and the prime powers are all fine. Summed over the $Kh^{1.6e}$ triples, the twisted part is $o(h)$.

**§3, disjointness and independence.** For the ratio version: $|uv'-u'v|\le h^{1.6e}<\ell$, so $(u,v)=(u',v')$, and then $q>K$ gives $k=k'$. For the word version, $16w'>K$. So $Z$ is a sum of independent Bernoulli variables given the small-prime fibre, and the moduli are distinct because $\ell>k$ is the largest prime factor of $f$.

**Unit repair (Theorem A).** It works, and it is the one genuinely new device. For $k\in J$ supported on $G$ and a failing $F(j)$, no prime of $k$ divides $F(j)$ (by scaling), so the repaired digits equal the true ones and $Z'=Z_{\rm true}=0$.
- Every repaired $c_0$ is a unit, so every fibre has $\mu\asymp t^3$ with no bad fibres.
- $h_J\asymp t$ follows from Vaughan's bound: the complement of $G$ has convergent $\sum1/p$, giving positive lower density. The union-bound constant can be chosen uniformly.
- The repair rule depends only on $j\bmod k$ and is consistent down each prime tower.

**All-values word case (Theorem B).**
- The bad-fibre bound is used only inside the CRT expectation. The $e^{K}$-size exponential-moment majorant is never transferred to the interval, so there is no hidden boundary cost.
- The content of $F$ contributes $o(1)$. For $p>2$ not dividing the content there are at most 2 roots, so there is no fixed prime divisor above $y$.
- $h_{J_0}\asymp t/\log t$ is correct.

**Finite transfer.**
- The even-$d$ truncation brackets are correct (the Taylor remainder has sign $(-1)^{d+1}$).
- Atoms number $e^{O(t)}$ with at most $2k$ cells each, so the boundary cost is $e^{O(mt)}$.
- The three choices of $t$ match $m=t^3$, $t^2$ and $t^2/\log t$. They give the exponents 3/4, 2/3 and $L$, and the boundary is $\le H^{1/2}$.
- Position-independence in $j_0$ holds.
- The band union bound over $2e^{b(\log H)^{1/4}}$ shifts is absorbed.

### 2. Independent ledger and replay

- **Replay.** `scripts/z79_wild_pullback.py` reproduces `data/z79/wild_pullback.txt` byte-for-byte.
- **My own independent checks** (separate code, sympy, under `ulimit -v 6000000`), all of which passed:
  - Jacobi$(-uv/f)=-1$ for all 22,502 admissible $(f,u,v)$ with $f<4000$, with 0 failures. This confirms the F1 reciprocity argument.
  - Exhaustive search over all words $xyz-x-z=n$ with $4\mid y$ finds **0** at 409, 577 and 5569. This confirms the F4 star-zero claim exhaustively, not only within the bounded panel.
  - 8/131 and 8/241 have no 3-term solution under an exact-fraction enumeration. The control 8/137 has the solution (18, 354, 72747).
  - 300 random nondegenerate quadratics: the root count equals $1+(D/\ell)$ in every case.
  - 20,000 random instances of the fresh-prime lemma: no counterexample.
  - Ratio atom $(7,1,2)$ at 409: $819=7\cdot117$ and $8\mid 8$, so it is a hit.
- **Empirical sanity check (EVIDENCE only).** I compared the twisted sum $\sum(1+(D/\ell))/\ell$ with the untwisted sum over $\ell\in[10^4,2\cdot10^5]$, $u\le20$, $v\le7$, $k=1$:

  | quadratic | twisted/untwisted |
  |---|---|
  | $j^2$ | 0.000 |
  | $j^2+1$ | 0.825 |
  | $j^2-3$ | 1.024 |
  | $j^2+24$ | 0.719 |
  | $3j^2+2j-5$ | 1.060 |
  | $2j^2+1$ | 0.776 |

  This is what the theorem predicts: the degenerate case $\Delta=0$ collapses completely, and the nondegenerate cases stay near 1. The small-$u$ biases sit below the proof's windows ($u>h^e$).

### 3. Findings

**M1 (wrong reason for a true conclusion).** The note says "4|y gives the sign (`Z64_SDEEPF.md`)". By Z64 Thm 2.1, with $(t,u,v)=(y,x,z)$ and $A=f$, the sign is good iff $8\mid(n+y)\,xyz$. Since $n$ is odd and $y$ is even, that means $8\mid xyz$.
- With $4\Vert y$ and $x,z$ odd the sign is $+1$, i.e. bad.
- The claim survives only because both shapes have $v_2(xy)=3$.
- Fix: cite Thm 2.1 and use $v_2(x)+v_2(y)=3$. Also note that the conditions $t,u,v\ge2$ follow from $x>h^e$ and the discard $z\ge2$.

**M2 (scope).** "Strengthens Z60_MS105 Thm 3 on this degree-two domain" is too broad.
- Z60 Thm 3 covers $s\,j^2$ with $s$ a non-square, which has degree 2 but $\Delta=0$. WILD explicitly excludes that case and names it as the next target.
- Say "nondegenerate ($\Delta\ne0$) quadratics with coefficients $\le e^{b(\log H)^{1/4}}$". Z60 is qualitative but applies to any fixed $f$ of any degree.

**M3 (compressed proofs).** These go beyond "routine" and a referee will ask for them written out:
- Re-prove the TQ lattice lemma for two different windows and arbitrary odd $k$. TQ's `lem:h` is only for $k\equiv1\ (4)$, although the note defines $h_J$ directly.
- State explicitly that TQ Lemma `wsecond` is used outside its stated hypothesis $J\subseteq\mathcal K(K)$.
- State the explicit formula with its exact error terms.

The present 80-line text is correct but very hard to audit. It needs a fuller version before any paper use.

**M4 (form).**
- The order of the three cases (all-values word, ES, prime-value word) in the final $t$-assignment sentence is confusing. Tabulate case → $J$ → $h_J$ → $m$ → $t$ → exponent.
- "cannot divide by a prime in G" is garbled.
- The data file has no provenance header (command, commit).
- Theorem B inherits A's coefficient bound $e^{b(\log H)^{1/4}}$, though its own $t$ allows up to $e^{b(\log H)^{1/3}}$. Harmless, but understated.

**M5 (falsifier scope; a suggestion, not an error).** F1 should name the Pell-type family $2j^2+1=m^2$.
- $\Delta=-8\ne0$, yet this family has infinitely many parameters giving odd squares. Those parameters get no ratio atoms and no (★) words.
- This is consistent only because the bound is a per-interval saving, not finiteness. That is the sharpest test of "no pointwise claim" and is worth recording.

**M6 (dependencies).** The "PROVED rel." list should say explicitly that it rests on the internally proved, unrefereed TQ lemmas and on AP2. The phrase "cited internal estimates" is there, but downstream readers will miss it.

### 4. Debate and challenges

- **Is the twist machinery needed?** Yes. Plain BV fails because the splitting condition is a union of about $\varphi(4|D|)/2$ classes. Counting characters trivially ($Q^2=h^{10e}$) instead of using zero density would discard more $u$ than the window contains. So Montgomery's zero-density theorem is genuinely required. The window choices are consistent but fragile, and that should be said.
- **Is it novel?** A quick web search found no prior result on exceptional sets for ES restricted to quadratic values. Priority is still unverified, as the note says, and a proper literature check is owed before STATUS.
- **Does it belong in STATUS?** The test is whether a number theorist reading only STATUS would be misled without it. Probably not.
  - Theorem A is a transfer of TQ's exponent to a thin family. It deserves at most one sub-bullet under §1A, marked "cross-review owed; novelty unverified", rather than a new row.
  - Theorem B should merge into the existing AP2 row as "also on $\Delta\ne0$ quadratic values".
  - "RECORD" is defensible only if no earlier quadratic-values bound exists. FRONTIER §5 may be the better home.
- **Pipeline compliance:** satisfied. The lane edited only its note, script and data; the §0 block is complete; master files are untouched; "Review: none" is honest.

### 5. Required fixes before promotion

1. Correct the sign justification (M1).
2. Restrict the comparison with Z60 to $\Delta\ne0$ (M2).
3. Write out the rectangular-window lattice lemma and state where TQ's `wsecond` is used outside its hypothesis (M3).
4. Add the Pell example to F1 (M5).
5. Record the dependence on the unrefereed TQ/AP2 notes in the label (M6).

A second hostile review is still needed before this becomes PROVED in the master files.
</code-review>
