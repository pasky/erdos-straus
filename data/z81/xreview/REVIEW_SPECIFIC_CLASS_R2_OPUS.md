<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="b349d18b1">
A separate reviewer subagent was asked to review the changes in `git log b349d18b1..`. Its request and review follow.

Request: review changes since b349d18b1 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Second hostile Claude Opus review: verify repairs to R1 and the NEW single-prime-population transfer WP (one-cofactor dimension-2 upper-bound sieve), square obstruction in superlog bands, radical-lcm extension to Theorem P and Laplace-weighted prime hybrid. Validate every exponent and scope; is the 4-specific physical modulus identification correct? Do not write files. No external communications; cap computations at 3 minutes. Please focus on actual mathematical defects, not stylistic polishing.

Commit log:
commit b57c615a4b7921eab21927327aea14f3995d8b94
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sun Nov 22 15:18:12 2026 +0100

    z81: transfer true large-modulus windows to primes and audit the radical budget

 data/z81/xreview/REVIEW_SPECIFIC_CLASS_R1_OPUS.md | 88 +++++++++++++++++++++++
 notes/z81/SPECIFIC_CLASS.md                       | 40 +++++++----
 2 files changed, 113 insertions(+), 15 deletions(-)

Review:
**Verdict: ACCEPT with minor fixes.** I re-derived every repair and every new piece (WP, the superlog-band square warning, the radical/lcm extension of P, the Laplace-weighted hybrid $K_{\rm mix}$) and found no mathematical defect. No CLAIMED proof of ES; nothing needs flagging to the user.

**Replay check (finished in under 3 minutes).** 3,000 random pairs $(n=4t+1,\ q\equiv3\bmod 4)$ and 1,450 odd squares $s^2$:
- $D_q(m)=m^{-1}\{d\bmod q: d\mid m^2\}$ held with 0 mismatches.
- 5,992 coprime witnesses all satisfied $4abcd=a+b+nc$, $(4acd-1)\mid cn+a$, $\min$ modulus $\in(n/q,2n/q+1]$, and $4/n=1/(abd)+1/(nacd)+1/(nbcd)$ exactly.
- No square window hit $-1$.

## Repairs to R1
All seven substantive points and the form items were addressed:
- (DR) now follows from $C^k$-multiplicativity: $\prod_q(1+C(z-1)p_q)=\exp(o(J))=X^{o(1)}$.
- The superlog square warning is added.
- The LM screen is now a labelled Assessment line.
- $\delta<I_*/2=0.0020774$ is correct, with $I_*=0.0041548$.
- $F_q$ is switched to the $-1$-miss indicator. $\mathrm{DR}_{\rm all}\Rightarrow\mathrm{DR}_{\rm spec}$ up to $X^{o(1)}$, because the numerators are ordered and both $\prod m_q$ are $X^{o(1)}$. Failures still contribute $z^J$.
- WP covers primes.
- A limited priority check is added.
- The $(q,b)$ automatic clause is correct both ways: $q\mid a\Rightarrow q\mid b\Rightarrow q\mid n$; and coprimality.

## WP (prime population)
The proof is correct:
- $n=4m-q=4bu-q$.
- Deleted residues: $\nu(2)=0$. At $p=q$ one class ($u\equiv0$, since $(4b,q)=1$ and $q<R$). At odd non-band $p\nmid b$, one class. At band $p\nmid b$, two distinct classes (distinct because $q\not\equiv0$). At $p\mid b$, only $u\not\equiv0$, because $4bu-q\equiv-q\ne0$.
- So $\nu\le2$, $\nu(3)\le1$, and dimension 2 holds.
- The remainder $\sum_{d<X^{1/3}}6^{\omega(d)}$ is $X^{1/3+o(1)}$, which is negligible against $X^{1-4/l}/L$.
- The main term is $\ll Xe^{-H}/(bL)$, uniform in $b$ and $q$. Dividing by $\#\mathcal P_X\asymp X/L$ reproduces W's per-$b$ domination exactly, so the Poisson mixture and its exponent $hI(a/h)$ carry over.
- Tails: $L\cdot L^{-1.77}=L^{-0.77}$ and $L e^{-L^e}$, both far below $L^{-0.0174}$.
- Markov then gives the Corollary on primes.
- The 8.5 comparison is fair. WP is "new in shape only" and dominated as an exceptional-set bound (cf. `FORCED_WINDOW.md` §8.6). One sentence saying that would help.

## The 4-specific physical modulus
The identification is **correct**. It matches `Z57_BFII.md` Lemma 1.1(a)/(c) exactly:
- $e=q$, $4abd=n+e$, $m=abd=x$, $c=(a+b)/q$.
- $f=4acd-1$ divides $cn+a$ with cofactor $b$, and symmetrically with $a\leftrightarrow b$.
- $\min f=(n+q)(a+b)/(q\max(a,b))-1$. Both ends of the interval are actually strict.
- Type II at prime $n$ holds because $m<n$ when $q<3n$.

## Square obstruction in superlog bands
Correct. F1 (quadratic reciprocity, including $2\mid m\Rightarrow q\equiv7\ (8)$, and $q\mid s$) forces misses at every window. This gives $K\ge X^{-1/2}\prod(z/m_q)$, where $J\log z=\sigma L^\beta/(2\beta)$ and $\sum\log m_q=o(J)$ by S. The claim that the per-coordinate ratio increases with $\sigma$ is right: $z/(1+(z-1)p)$ is increasing in $z$. At $\beta=1$ the squares contribute $X^{\sigma/2-1/2}$, which is within the budget, so $\beta=1$ is exactly the critical band (for $\beta<1$, $z^J=X^{o(1)}$).

## Radical/lcm extension of P
Correct:
- Shift differences are below $L^b/4<T$, so each rough prime is private to one window.
- The $p^2$ bad set is $O(1/(T\log T))$ per pair.
- The smooth-part mean is $\log T+O(1)$; Markov gives $O(l/L^u)\to0$.
- Rough parts are squarefree and pairwise coprime, so $\sum\log\mathrm{rough}(d_q)\le\log\mathrm{rad}(\mathrm{lcm})\le CL$.
- At most $CL^{1-u}=o(J)$ windows exceed the cutoff. Elsewhere $d_q\le e^{2L^u}$, which still satisfies $Y<X/Y$.
- The threshold $b_*$ is unchanged. Deleting "not a cap on lcm methods" from the Scope is justified.

## Laplace hybrid $K_{\rm mix}$
All arrows check:
- $K_{\rm mix}\le(X/\#\mathcal P_X)K\asymp LK$.
- $H^-_{\rm BM}$ gives $R\ge\varepsilon\cdot0.019L^2$ (FRONTIER Thm 2.2), so the damping $e^{-cLl}$ beats $z^J=e^{\sigma L/2}$.
- An exceptional prime has $R=0$ and $F\equiv1$, so the prime count is $\ll X^{1-\sigma/2+\lambda+o(1)}$, and Rankin gives $\delta<\sigma/2-\lambda$.
- The $X^{1-d}$-row separation arithmetic is right.

**Challenge:** the $H^-_{\rm BM}\Rightarrow K_{\rm mix}$ arrow is logically near-vacuous. $H^-_{\rm BM}$ alone already gives (★), hence ES, at all large primes. The only real content is that $K_{\rm mix}$ is weaker than (DR) at the level of input data, and the note should say so plainly.

## Minor fixes owed
1. The $K_{\rm mix}$ label "PROVED rel. §2" is ambiguous. The arrows actually use the §1 window identity, PNT mod 4, the BM Thm 2.2 lower bound and Rankin. The BM lower bound is also missing from the §0 input list.
2. Triage BARRIER-SCOPED fits P only. W/S/WP are window theorems and (DR)/$K_{\rm mix}$ are an open sub-problem. Per R1, these should be split into a FRONTIER §7 line plus a §6 line.
3. In the (DR) Assessment, the note's "$b$" is Lemma 1.1's $c$, and "$m=4ab-1$" overloads $m$ (the first denominator). Rename it $f$.
4. The "CERTIFIED" label is still attached to identity controls. There is no replay for WP or the radical extension. That is fine, but the note should not imply it.
5. Priority: the $m^2$ reformulation makes Erdős–Hall-type results for divisors of squares/powers (exponent $\log 3$) the natural place for prior art. The check is honestly labelled limited, but it remains owed.
</code-review>
