# Wave 15 hostile review: §45

**Verdict: SOUND-AFTER-REPAIRS**

**WALL CRACKED (sub-range: all incidences with `m=4c^2s \ll L^3/(\log L)^2`; the full moving-$s$ endpoint remains open)**

The exact Kloosterman-matrix reduction and the central diagnosis about DFI/BC are sound.  The unit did, however, miss a genuine moving-$s$ subfamily that follows by combining its own fixed-fibre Frobenius bound with injectivity modulo $p$.  This does not close a new $p$-only range and does not prove (40.19), but it shows that Proposition 45.3 is not the “strongest proved endpoint statement.”

## Source audit and exact theorem statements

I read the archived PDFs, not only BC's quotation of DFI.  The hashes agree with `sources/README.md`:

- DFI: `b56987587a54034ee441bb22fd95be8eeceaadb6e67f299b2589447c5242eb32`.
- BC: `439665281e775e8369e222c959f2cad0221aa57dc7d1338efdae1c99029d7f20`.

The URLs, titles, version statement for BC, and the description of the DFI file as the complete 21-page publisher-typeset paper from Duke's UCLA archive are accurate.  The stale contrary provenance paragraph in §45 was repaired in `notes.md` and marked `(wave-15 review repair)`.

### DFI, actual Theorems 1 and 2

DFI define, for arbitrary complex coefficients on $M<m\le 2M$ and $N<n\le 2N$,

$$
 B(M,N)=\sum_{\substack{m,n\\(m,n)=1}}
 \alpha_m\beta_n e\!\left(a\frac{\bar m}{n}\right),
 \qquad \|\alpha\|_2^2=\sum_m|\alpha_m|^2,
 \quad \|\beta\|_2^2=\sum_n|\beta_n|^2.
$$

For a **positive integer** $a$, their Theorem 1 is

$$
 |B(M,N)|\ll_\varepsilon \|\alpha\|_2\|\beta\|_2
 \left\{(M+N)^{1/2}+
 \left(1+\frac{a}{MN}\right)^{1/2}\min(M,N)\right\}(MN)^\varepsilon.
 \tag{DFI-1}
$$

Their principal amplifier estimate, Theorem 2, is

$$
 |B(M,N)|\ll_\varepsilon \|\alpha\|_2\|\beta\|_2
 (a+MN)^{3/8}(M+N)^{11/48+\varepsilon}.
 \tag{DFI-2}
$$

There is no density hypothesis and no range hypothesis in either theorem.  If $a\ll MN$, DFI themselves state that Theorem 2 improves the trivial $2\|\alpha\|_2\|\beta\|_2(MN)^{1/2}$ when
$N>M^{5/6+\varepsilon}$ and $M>N^{5/6+\varepsilon}$.  With fixed power margins this is

$$
 N^{5/6+\eta}\le M\le N^{6/5-\eta}.
$$

Changing $(M,2M]$ to $[M/2,M]$ and allowing negative $a$ by conjugation are harmless.  Equations (45.10)--(45.11) are therefore accurate.

**Source finding.**  Contrary to the task brief's parenthetical description, the archived DFI paper does **not** state this theorem for a rational $\vartheta=a/q$ under extra conditions.  Its phase numerator is the positive integer $a$.  The nonzero real parameter $\vartheta$ belongs to BC's theorem below.  I found no omitted rational-denominator hypothesis in DFI.

The unit mentions DFI Theorem 1 only as a “different Poisson estimate.”  That is too vague for a range audit, but not a hidden route: inserting (DFI-1) into the same Rademacher/SVD proof replaces $\mathcal K$ by

$$
 \mathcal K_1(P,W)\asymp
 (P+W)^{1/2}+\min(P,W)
 \quad (1\le |h|\le 2P,\ W\ge4),
$$

up to $(PW)^\varepsilon$.  The Parseval output is still
$\mathcal K_1(P,W)^2\|G^{P,W}\|_*^2/P$, and none of (45.7)--(45.9) bounds that projective norm.  Thus Theorem 1 closes no new $p$-range.

### Bettin--Chandee, actual Theorem 1

BC take arbitrary complex $\nu_a,\alpha_m,\beta_n$ supported on
$[A/2,A]$, $[M/2,M]$, and $[N/2,N]$, respectively, and any nonzero real $\vartheta$.  Their Theorem 1 states

$$
\begin{aligned}
&\left|\sum_{\substack{a\sim A,m\sim M,n\sim N\\(m,n)=1}}
 \nu_a\alpha_m\beta_n
 e\!\left(\vartheta a\frac{\bar m}{n}\right)\right| \\
&\quad\ll_\varepsilon
 \|\nu\|_2\|\alpha\|_2\|\beta\|_2
 \left(1+\frac{|\vartheta|A}{MN}\right)^{1/2}
 \left\{(AMN)^{7/20+\varepsilon}(M+N)^{1/4}
 +(AMN)^{3/8+\varepsilon}(AN+AM)^{1/8}\right\}.
 \tag{BC-1}
\end{aligned}
$$

This matches (45.12), including the quantifiers and the absence of balance or density assumptions.  For $|\vartheta|A\le MN$, the first term beats the ambient $\ell^2$ bound exactly when

$$
 \max(M,N)<A^{3/2}\min(M,N)^{3/2},
$$

and the second requires $M+N<MN$ up to margins.  On the top endpoint frequency block $A=N=P$, $M=W=P^w$, the overall scalar saving is

$$
 \delta_{BC}(w)=
 \begin{cases}
 w/8,&0<w\le1,\\
 1/8,&1\le w\le7/4,\\
 3/10-w/10,&7/4\le w<3,
 \end{cases}
$$

so (45.14), $P^\eta\le W\le P^{3-\eta}$, is correct.  Lower $h$-blocks have $A=H<P$, not $A=P$; this only weakens the available scalar estimate and does not rescue the full norm.

## Graded checklist

### 1. Reduction lemma — **CONFIRMED**

For an endpoint incidence put

$$
 x_i=\frac{\kappa(pq_i)}{q_i},\qquad
 t_i=c_i^2s_i,\qquad m_i=4t_i.
$$

Proposition 42.1 gives

$$
 -4D_i\equiv-\overline{4c_i^2s_i}=-\bar m_i\pmod p,
 \qquad \frac{\kappa(pq_i)}{pq_i}=\frac{x_i}{p}.
$$

Therefore additive orthogonality gives, exactly,

$$
 p\sum_a\left(\frac1p\sum_{i:-\bar m_i=a}x_i\right)^2
 =\sum_{h\bmod p}\left|\frac1p\sum_i x_i e_p(-h\bar m_i)\right|^2.
$$

Every positive integer $m/4$ has a unique square-times-squarefree decomposition $c^2s$.  Grouping the incidences with the same $(p,c,s)$ consequently replaces $\sum_i x_i$ by $G_{m,p}$ with neither loss nor multiplicity.  This proves (45.3), not merely a toy analogue.

All endpoint restrictions survive the grouping:

- `retained` is an indicator inside $\mathcal Q_{p,c,s}$, so canonical-fibre deletion and prime-atom deletion are preserved;
- $p>z$ and $P^-(q)>z$ are equivalent here to $P^-(pq)>z$, including $p^e\mid pq$ cases;
- $q>1$ preserves compositeness, $pq\le X$ is $q\le X/p$, and $pq\equiv3\pmod4$ remains explicit;
- $c<p$, $q<4R$, $R=(pq+1)/(4c)$, $s\mid\operatorname{rad}(R)$, and the exact $\kappa(pq)$ weight all remain inside the coefficient;
- the complete sum includes $h=0$ and every $1\le h<p$ exactly once.

The support claims follow from $s\le R$:

$$
 m=4c^2s\le4c^2R=c(pq+1)<p(X+1),
$$

and $(m,pq)=1$ follows from $pq=4Rc-1$, $s\mid R$.  Both reciprocity identities are valid even when $q$ is composite or divisible by $p$:

$$
 -\frac{h\bar m}{p}\equiv-\frac{hq\bar m}{pq}
 \equiv \frac{h\bar p}{m}-\frac{h}{mp}\pmod1.
$$

The tempting modulus-$q$ orientation is genuinely false: $\bar p\equiv-q\pmod{4R}$ does not determine $\bar p\pmod{4c^2s}$ unless the extra divisibility $c^2s\mid R$ happens.

### 2. Coefficient norms — **CONFIRMED**

Since $\kappa\le2$ and $q>z$,

$$
 0<x_i\le2/z,
 \qquad \sum_i x_i^2\le(2/z)\sum_i x_i=2A_p/z.
$$

For the aggregated cells,

$$
 A_p=\sum_mG_{m,p},\qquad F_p^2=\sum_mG_{m,p}^2,
$$

and nonnegativity gives $F_p^2\le A_p^2$ and
$A_p^2\le(\#\operatorname{supp}G_p)F_p^2$.  Hence
$1\le H_p=A_p^2/F_p^2\le\#\operatorname{supp}G_p$.  Aggregation can only increase the edge-level squared norm; §45 correctly keeps the two quantities distinct.

At atom scale,

$$
 \frac{x_i}{p}=\frac{\kappa(pq)}{pq}
 \le\frac2{4Rc-1}\le\frac1R=\frac{h_D}{L}.
$$

There is no missing endpoint $L/p$ tail factor, and (42.9) shows why this pointwise bound does not sum to the target.

For fixed squarefree $s$, Parseval and positivity in each residue bucket give

$$
 \sum_p\frac1p\sum_m|G^{(s)}_{m,p}|^2
 \le \sum_p\frac1p\sum_r
 \left(\sum_{m:\,-\bar m=r}G^{(s)}_{m,p}\right)^2
 =\mathcal V_X^{\mathrm{end},(s)}
 \ll L^3+L^2\log L.
$$

This is the legitimate fibre Frobenius bound (45.9).  It is uniform for one prescribed $s$, but summing residue vectors over $K$ fibres costs $K^2$ in (42.11).  No theorem in §§42 or 45 supplies a global moving-$s$ nuclear norm or a lower bound $H_p\to\infty$.  The failure verdict is therefore not manufactured by an inflated or understated norm.

### 3. Application audit and attacks — **CONFIRMED**

#### Joint coefficient obstruction

On a dyadic block, SVD really does produce rank-one DFI forms.  Rademacher orthogonality gives, for each nonzero $h$,

$$
 \sum_{p\sim P}|Y_{p,h}|^2
 =\mathbb E_\epsilon\left|
 \sum_{p\sim P,m\sim W}\frac{\epsilon_pG_{m,p}}p
 e_p(-h\bar m)\right|^2.
$$

DFI then costs the nuclear norm of $G\operatorname{diag}(\epsilon_p/p)$, at most $P^{-1}\|G\|_*$.  Summing $O(P)$ frequencies proves (45.17).  The argument is exact, and Frobenius control cannot replace the nuclear norm without the rank factor in (45.20).

I tried three decouplings.

1. **Characters after exposing $s$.**  As $s$ is squarefree, $s\mid\operatorname{rad}(R)$ is equivalent to $R=sr$.  With $k=4cs$ the equation is

   $$pq+1=4csr,\qquad pq\equiv-1\pmod k.$$

   On fixed dyadic $p,q$ ranges, character orthogonality gives

   $$
   \mathbf1_{pq\equiv-1(k)}
   =\frac1{\varphi(k)}\sum_{\chi\bmod k}
     \chi(p)\chi(q)\overline{\chi(-1)}.
   $$

   This separates $p$ and $q$ for one fixed $k$, but $k=4cs$ varies with
   $m=ck=4c^2s$.  Thus the would-be $p$ coefficient is $\chi_{k(m)}(p)$ and remains jointly indexed by $(m,p)$.  The cutoff $q\le X/p$, $\kappa(pq)$, roughness, and retention add further coupling.  Möbius or upper-bound-sieve expansions of roughness do not remove the variable character modulus.  Neither DFI nor BC contains the required hybrid large sieve over these varying $k$.

2. **Equation/determinant reformulation.**  The incidence is the fixed determinant equation

   $$pq-(4c)R=-1.$$

   This resembles BC Corollary 1, but that corollary permits two smooth one-variable weights and two arbitrary *separate* sequences for one determinant equation.  Here $p$ is prime, $q$ is rough and reciprocally weighted, $R$ carries the moving subset-divisor and retention data, and the energy has two such equations sharing $p$ plus
   $c^2s\equiv c'^2s'\pmod p$.  No permutation puts these data into the four allowed separated weights.  Dropping all arithmetic indicators by positivity is legal only after returning to the collision form and gives the catastrophic enlarged family already identified in (42.27).  BC's determinant application therefore does not estimate this shifted divisor correlation.

3. **Additive/circle detection.**  Detecting $p\mid4cR-1$ by a complete additive sum moves the incidence into a phase $e_p(a(4cR-1)-h\overline{4c^2s})$ and adds another complete variable.  Detecting the equality $pq+1=4cR$ instead gives a bilinear product phase and still leaves the subset-divisor/retention coefficient.  Neither form has DFI/BC's separated coefficient quantifiers; the detector has moved, not removed, the matrix dependence.

These failures are structural, not an artifact of choosing $p$ rather than $q$ as the displayed modulus.

#### Complete-frequency/output-norm obstruction

At $W=P$, DFI gives $\mathcal K(P,P)=P^{47/48+O(\varepsilon)}$, hence the multiplier
$P^{23/24+O(\varepsilon)}\|G\|_*^2$ in (45.17).  Even rank one is worse than the exact distinct-residue Frobenius contribution $\|G\|_F^2/P$ by $P^{47/24+O(\varepsilon)}$.

The top BC block has $A=N=M=P$.  Its scalar saving is only $P^{1/8}$ after both terms are retained.  Dualizing the $\ell^2(h,p)$ output gives an arbitrary matrix $\eta_{h,p}$; its projective norm can cost $P^{1/2}$, before decomposing $G_{m,p}$.  This is a genuine mismatch.

A one-cell row is the sharp sanity check.  If the only occupied cell has mass $G$, then

$$
 Y_{p,h}=\frac Gp e_p(-h\bar m_0),
 \qquad \sum_{h\bmod p}|Y_{p,h}|^2=\frac{G^2}{p}.
$$

All current facts allow $H_p=1$.  No cancellation estimate for a scalar contraction can make this row Fourier-small.

I also tried two direct substitutes for Parseval.

- The residue maximum gives
  $$
  E_p=\frac1p\sum_r B_{p,r}^2
  \le\frac{A_p}{p}\max_r B_{p,r}.
  $$
  Closing requires a new anti-concentration bound for the largest bucket; neither $H_p$ nor (45.9) supplies one.
- A fourth-moment/large-values split produces the reciprocal additive energy
  $$
  p\!\sum_{\bar m_1+\bar m_2\equiv\bar m_3+\bar m_4(p)}
  G_{m_1,p}G_{m_2,p}G_{m_3,p}G_{m_4,p},
  $$
  which is a stronger codegree problem, not a consequence of DFI/BC.

Multiplicative orthogonality is another exact presentation because $c^2s\ne0\pmod p$.  If retention is dropped, the $s$-sum becomes
$\sum_{s\mid\operatorname{rad}(R)}\chi(s)=\prod_{\ell\mid R}(1+\chi(\ell))$.
But squaring and averaging over $\chi\bmod p$ restores the same subset-product collision, while the endpoint incidence still depends on $p$.  It supplies no free moment saving.

Thus the correct conclusion is: **the DFI/BC scalar pipeline does not bound the full moving matrix in the required output norm.**  This is narrower than saying that Parseval can never be sidestepped; the small-$m$ repair below does sidestep cancellation by exact injectivity.

### 4. Range bookkeeping — **REPAIRED**

Let

$$
 p\asymp P,\quad q\asymp Q,\quad c\asymp C,\quad
 R\asymp U,\quad s\asymp S,\quad m\asymp W.
$$

The exact equation gives the scale relations

$$
 PQ\asymp4CU,
 \qquad U\asymp\frac{PQ}{4C},
 \qquad W\asymp4C^2S,
$$

with

$$
 \begin{gathered}
 L^B<P\le X/z,\qquad z<Q\le X/P,\qquad 1\le C<P,\\
 Q<4U,\qquad 1\le S\le U,\qquad PQ\le X.
 \end{gathered}
$$

Consequently $4\ll W\ll C^2U\asymp CPQ\le PX$.  There is no relation forcing $W$ to be a fixed power of $P$.

For DFI Theorem 2, writing $W=P^w$, comparison with $(PW)^{1/2}$ gives scalar saving exponent

$$
 \delta_{DFI2}(w)=
 \begin{cases}
 (6w-5)/48,&w\le1,\\
 (6-5w)/48,&w\ge1,
 \end{cases}
$$

so the true window is $5/6<w<6/5$.  DFI Theorem 1 handles unbalanced scalar forms, but after the complete $h$-sum its multiplier is $\mathcal K_1(P,W)^2/P$ and no available projective norm makes that useful.  BC has the wider scalar window $0<w<3$ described above, but the top $(h,p)$ dual-rank loss already exceeds its maximum $P^{1/8}$ saving.  Therefore no additional **$p$-only** interval inside $L^B<p\le X/z$ closes from DFI or BC.

**Review flag (wave 15): closable sub-range.**  Let $\mathcal E(W_0)$ be the endpoint subfamily with

$$
 m=4c^2s\le W_0,
 \qquad W_0\ll\frac{L^3}{(\log L)^2}.
$$

Since

$$
 W_0=o(z)=o(p),
$$

two distinct supported integers $m,m'\le W_0$ cannot be congruent modulo any endpoint prime $p>z$.  Inversion preserves injectivity.  Parseval therefore has no cross-cell terms:

$$
 \mathcal V(\mathcal E(W_0))
 =\sum_{p>z}\frac1p\sum_{m\le W_0}G_{m,p}^2.
$$

The unique square-times-squarefree decomposition has $s\le m/4\le W_0/4$.  Summing (45.9) over these squarefree $s$ gives

$$
 \mathcal V(\mathcal E(W_0))
 \ll W_0\bigl(L^3+L^2\log L\bigr)
 \ll \frac{L^6}{(\log L)^2}=\Lambda^2.
$$

This closes a moving-$s$ family across the **entire** endpoint prime range and allows $\asymp L^3/(\log L)^2$ possible fibres, much more than the $O(L^{3/2}/\log L)$ arbitrary-fibre union in Proposition 45.3.  With only the uniform fixed-$s$ norm (45.9), $W_0\asymp\Lambda^2/L^3$ is the widest cutoff this argument proves.  It does not control $m>W_0$ and hence does not prove (40.19).  This mathematical finding is intentionally left as a review flag rather than silently inserted as a new theorem in §45.

### 5. Status register and provenance — **REPAIRED**

The register remains logically correct:

- Corollary 40.4 gives $(40.19)\Longleftrightarrow(37.27)$ after the proved regular-tail estimate.
- Even full (40.19) is only pair-level input and does not imply the multi-coordinate hierarchy (40.28), hence does not imply (37.19).
- The arc concerns the internal hypothesis $H_{\rm PF}'$; it proves or refutes neither that hypothesis nor the Erdős--Straus conjecture.

No §45 line upgrades an open theorem.  The only overstatement is local: Proposition 45.3 is not the strongest assembled subfamily once the small-$m$ injectivity argument is noticed.  The DFI/BC insufficiency and the full OPEN verdict survive.

`sources/README.md` has accurate URLs and hashes.  The stale §45 statement that no full DFI file was archived, plus the indirect “quoted verbatim in BC” wording, was repaired and explicitly marked `(wave-15 review repair)`.

### 6. Verification block (ar) and full suite — **CONFIRMED**

Block `(ar)` rebuilds the retained toy atoms, computes the canonical $R,s,c,m$, preserves each prime divisor $p$ (including prime-power cofactors), checks roughness, $c<p$, $q<4R$, coprimality, both reciprocity identities, and equality of the residue-bucket energy with the grouped $G$-matrix Parseval energy.  It also distinguishes aggregated and edge-level squared norms.  Thus it validates the actual reduction in Lemma 45.1, not an unrelated matrix identity.

Command run:

```text
uv run --with sympy,numpy,scipy python verify.py
```

Result: `all checks passed`; final post-edit run elapsed 1:16.61, peak RSS 327156 KB.  The post-edit control-byte scan reports zero.

## Final assessment

The joint-modulus coefficient and complete-output-norm diagnoses are real, and neither DFI theorem, BC Theorem 1, BC's determinant corollary, character detection, nor a direct $h$-moment split closes the remaining family.  The section is mathematically sound on its main reduction and full OPEN verdict after provenance wording repairs.  It needs a repair round to record the small-$m$ moving-fibre proposition and to weaken “strongest proved endpoint statement” accordingly.
