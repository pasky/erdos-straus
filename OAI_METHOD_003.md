# OAI_METHOD_003 — what the seven-eighths method actually controls

**Assessment, 2026-10-28. Verdict: PARTIAL; promise for B2: 1/5.** The new mechanism is a cubic-theta reflection/Poisson recursion for very special sextic character families, followed by an amplified zero detector. It is not a generic improvement of the Dirichlet large sieve. It gives useful additional campaign consequences, including obstruction-side improvements missed in `OAI_DUMP_IMPACT.md`, but no fixed-prime divisor-class lower bound.

**Status convention.** ES remains OPEN. All deductions using the release are **CONDITIONAL on OAI-003 (quasi-RH 7/8)**, even when an implication is proved below. “Unconditional if accepted” does not mean independently established here. CLAIMED means an assertion of the unrefereed release; CERTIFIED means the explicitly described finite/static check only; Assessment means a methodological judgment. Classical inputs and campaign proofs retain their own published/internal status.

## 1. Sources and what was audited

**CERTIFIED source inventory.** Checkout `/home/pasky/projects/math/oai-math`, commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`. Abbreviations below refer to its `preprints/` directory:

| name | source | scope |
|---|---|---|
| S | `The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex` and `paper.pdf` | 7/8; 16,677 source lines; two-stage argument |
| O | `The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex` and `paper2.pdf` | **11/12**, not a replacement 7/8 proof; 3,988 source lines |
| L | `Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/paper.tex` and `paper.pdf` | separate interpolation-determinant proof of a logarithmic real-zero gap |

**Assessment of audit depth.** I read the proof overviews, exact moment hypotheses, compensation, continuation and endpoint calculations in S; the full five-step outline and reduction in O; and all of L. PDF text extraction agrees with the cited source formulas. I traced the Lean endpoint and main assembly, and scanned its complete local import closure. This is not a line-by-line referee check of the roughly 21,000 analytic source lines, nor a compilation of the roughly 3,000-module formal proof. In particular, the long two-Poisson induction and general twisted cusp transformation remain independently unverified here. No concrete mathematical gap was found in the checked chain; that is a limited sanity check, not certification of quasi-RH.

## 2. The analytic method

### 2.1 The arithmetic device: turn Möbius into cubic theta, then sextic into quadratic

**CLAIMED method, with classical ingredients identified.** Work over the Euclidean Eisenstein ring \(\mathcal O=\mathbb Z[\omega]\), \(F=\mathbb Q(\sqrt{-3})\). Write \(q_a=Na\), use primary generators, and set \(\chi_n(u)=(u/n)_6\), **zero on nonunits**. For squarefree primary \(n\), normalized Gauss sums obey

\[
 \mu(n)\gamma_{-1}(n)
 =\chi_n(-1)G(n)^{-1}\overline{\alpha(n)}\gamma_2(n),
 \quad \alpha(n)=n/|n|,
\]

with \(G\) a fixed ray-class factor (O lines 301–350). Thus Poisson summation of a sextic-twisted Möbius family turns the coefficients into cubic Gauss sums, which are coefficients of Kubota–Patterson's cubic theta function. This identification, Gauss–Jacobi identities, and the underlying theta function are classical, not the new theorem.

The theta transformation applies to **completed indices \(cn^3\)**, \(c\) squarefree. One must not impose \((c,n)=1\). Fixed target and ray phases act on the whole index. At a squarefree row prime, the Fourier factor and theta factor combine as

\[
 \chi^{-1}\chi^{-2}=\chi^{-3}=\chi^3,
\]

so the reflected twist is quadratic. Goldmakher–Louvel's quadratic large sieve supplies \(M+N\), rather than the higher-order \(M+N+(MN)^{2/3}\). The completed reflection, with arbitrary fixed ray twists, ramified rows, shared factors and zero extensions retained, is a central proof obligation (S §5; O §§6, 8).

**CLAIMED genuinely additional work.** Completion cannot be removed by dropping its extra terms: they can cancel the squarefree part. The papers invert the cube completion and control its long tail by **two Poisson transforms**, enlarging an intervening positive row sum so that the next row range is shorter. Smooth seminorms, frozen moduli and missing Euler factors must survive the recursion. This is substantially more than an application of a known large sieve to arbitrary coefficients.

### 2.2 The particularly transparent 11/12 proof in O

**CLAIMED inequality chain (O §2, §§3–7).** Fix one finite-order Hecke target \(\nu\), a smooth annular \(W\), and

\[
 A_u(D)=\sum_{\mathfrak n}\mu(\mathfrak n)\nu(\mathfrak n)
       \chi_{\mathfrak n}(u)W(N\mathfrak n/D).
\]

Their special mean-square theorem is

\[
 \sum_{0<Nu\le H}|A_u(D)|^2\ll_{\nu,W,\vartheta,\epsilon}
       D^{1+\epsilon}H,\qquad H=D^{1+\vartheta},\quad 0<\vartheta\le1/10.       \tag{2.1}
\]

For a prime ideal generator \(\varpi\) of norm \(\asymp H^{1/6}\),
\(\chi_n(\varpi^6)=1_{\varpi\nmid n}\), hence
\(A_{\varpi^6}(D)=A_1(D)+O(DH^{-1/6})\). There are
\(\asymp H^{1/6}/\log H\) such rows, by the ordinary prime ideal theorem. Keeping them in (2.1) yields

\[
 |A_1(D)|^2\ll D^{1+\epsilon}H^{5/6}+D^2H^{-1/3},
 \qquad A_1(D)\ll D^{11/12+5\vartheta/12+\epsilon}.                  \tag{2.2}
\]

Choose \(\vartheta\) after the requested exponent loss. Smoothed dyadic Mellin summation continues \(1/L_F^S(s,\nu)\) to \(\Re s>11/12\). Here \(11/12=(1+5/6)/2\) comes from the sixth-power amplification, not from a classical zero-density exponent.

**CLAIMED proof of (2.1), not an arbitrary-weight analogue.** After the first Poisson transform the schematic target is

\[
 E(H_1,X)=X^{-1}\sum_{Nh\ll H_1}|B_h(X)|^2\ll X^{1+\epsilon},
 \quad H_1\asymp D^{1-\vartheta},\ X\asymp D.
\]

Completed theta energy gives
\(\sum_{Nh\ll H_1}|T_h(X)|^2\ll(H_1X)^\epsilon(H_1+H_1^2/X)\).
Cube inversion is the exact identity

\[
 P_h(X)=\sum_d\frac{\mu(d)w_h(d)}{Nd}T_h(X/(Nd)^3),\qquad P_h=X^{-1/2}B_h,
\]

with completely multiplicative \(w_h\). Short cubes up to
\(H_c=\min(X^{1/3},(X/H_1)^{2/3})\) cost
\(H_1+H_1^2H_c^3/X\le O(X)\). The long cubes reduce, by the two transforms, to

\[
 E(H_1,L)/X\ \prec\ 1+E'(H_1L/X,L)/L,\quad L=X/(Nb)^3,
\]

preserving \(H_1/X\) and reducing both parameters by at least the fixed power \(D^{2\vartheta}\). Thus only \(O_\vartheta(1)\) stages occur. The full proof adds a squarefree label \(f\), a fourth-power residue twist, masks and divisor-bounded weights; the schematic recursion alone is not a proof with those data.

### 2.3 S's common continuation principle and first stage

**PROVED analytic implication, conditional on its two probe estimates** (S Proposition 2.1, lines 363–519). Let \(\beta_*\) be the supremum of \(1/2\) and the zero real parts of **all** primitive finite-order Hecke targets. Suppose \(\beta_*>\sigma_0\). For each target construct

\[
 f_\eta(Z)=\frac1{2\pi i}\int_{(2)}Z^{C(s)}e^{(s-5/6)^2}
            \frac{H_\eta(s)}{L_F^S(s,\eta)}\,ds,\qquad C(s)=s+c,
\]

where \(H_\eta\) is holomorphic and \(|H_\eta-1|\le1/2\) throughout \(\Re s>\sigma_0\). If

\[
 |J_\eta(Z)|\ll_\eta Z^{C(\sigma_0)+\omega},\quad
 |J_\eta(Z)-f_\eta(Z)|\ll_\eta Z^{C(\beta_*)-\sigma},
 \quad 0<\omega<\beta_*-\sigma_0,\quad\sigma>0,                    \tag{2.3}
\]

with **target-independent exponents**, then
\(|f_\eta|\ll_\eta Z^{C(\beta_*)-\epsilon_*}\),
\(\epsilon_*=\min(\beta_*-\sigma_0-\omega,\sigma)>0\).
Its Mellin transform continues the reciprocal across \(\beta_*\) by the common distance \(\epsilon_*\), contradicting the definition of the supremum. Attainment of the supremum is unnecessary. Gaussian decay, a rightward contour shift at \(Z\downarrow0\), and Fourier inversion justify the Mellin identification without crossing a zero.

**CLAIMED first-stage application.** Balanced scales \(X=Y=Z^{1/2}\), reflected quadratic energy, a planar additive large sieve and Cauchy–Schwarz give low exponent \(1/4\). Poisson frequencies are \(ua^6\), \(u\) sixth-power-free. The \(u=1\) Euler quotient has the reciprocal target as its principal signal; nonprincipal rows are grouped by zeros in buffered rectangles and bounded by sextic-sieve counts. Here \(C_I(s)=s-2/3\), so \(C_I(11/12)=1/4\). This establishes the first strip before the second-stage bootstrap. It is not exactly the same physical probe or proof presentation as O's simpler Möbius extraction.

### 2.4 The new moments and prime compensation for 7/8

**CLAIMED exact useful hypotheses** (S §§17–18, lines 9218–9355 and 12477–12595). Centrally normalized polynomials are

\[
 M_u(Z^r)=Z^{-r/2}\sum_n\mu(n)\psi_u(n)W(q_n/Z^r),\quad
 S_u(Z^r)=Z^{-r/2}\sum_n\psi_u(n)W(q_n/Z^r),
 \quad\psi_u(n)=\nu(n)\chi_n(u)^{\pm1}.
\]

For disjoint, row-independent prime supports of total length \(z=\sum z_i\), write \(Q_u\) for the product of their normalized prime sums. The marked inverse bound is

\[
 \sum_{0<Nu\ll Z^m}|M_u(Z^r)Q_u|^2\ll Z^{m+\epsilon},\qquad
 r+2z\le m-c_1,\quad2r+8z\le3m-c_2,\quad c_1,c_2>0.             \tag{2.4}
\]

Prime coefficients may be arbitrary bounded numbers **independent of the row**, not arbitrary coefficients of the Möbius polynomial. The canonical induction explicitly forbids an additional arbitrary residual column weight (S lines 9310–9321).

The plain fourth moment has effective width \(M=m+q\), where \(Z^q\) bounds the **displayed moving conductor radical before cancellation**:

\[
 \sum_{k\in\mathcal R_z}|S_k(Z^{n_1})S_k(Z^{n_2})Q_k|^2\ll Z^{M+\epsilon}.     \tag{2.5}
\]

With slots it requires \(n_1+n_2+6\kappa z\le M\), sufficiently fine individual slot lengths, and \(\beta_*\le(1+\kappa)/2\) if \(\kappa<1\). Positive-slot coefficients are fixed finite ray-character combinations, not arbitrary bounded coefficients. Positive-slot rows must exclude the finite inducing-character family \(\Theta\); zero-slot rows exclude only principal characters and allow all bounded length ranges. A centered equal-product-scale difference cancels volume main terms for the exceptional transformed rows. The final estimate is for the original uncentered product. These exclusions and the distinction between primitive conductor and redundant zero masks are essential.

**CLAIMED compensation** (S §12, lines 6810–6916). At each selected prime \(\varpi\), replace the original probe by

\[
 \overline{\eta(\varpi)}I_{\eta;\varpi}(X,Y,Zq_\varpi)
       -q_\varpi^{-3/2}I_\eta(X/q_\varpi,Y/q_\varpi,Z).
\]

The first term marks \(\varpi\mid cn^3\). The subtraction cancels a scalar Euler term, leaving a sextic prime amplitude to which (2.4)–(2.5) apply. All slots retain their original windows under every rescaling. On the principal residue the local factor is
\(-1+O(q_\varpi^{-7/8})\); the normalizer is nonzero and of size \((\log Z)^{-K}\), using prime counting in a **fixed** ray class. The target's excluded primes eventually leave the growing windows. This is not uniform prime counting in a moving ray conductor.

**Assessment of novelty.** Zero detection via long reciprocal/plain polynomials, moment-to-large-values counting, mollifier-type Möbius coefficients, contour shifting, quadratic/cubic large sieves and amplification are classical technology. The asserted advance is their special closed arithmetic recursion: completed cubic theta reflection, exact masks, prime-compensated probe, simultaneous saturated witnesses, and the two marked moment theorems. There is no Halász theorem in this proof of the strip. Halász is a separate classical *downstream* tool in the campaign's BM-main-term deduction. Nor does S import the release's Patterson prime first-moment result (family 023), or the GRH-conditional prime asymptotic of Dunn–Radziwiłł.

### 2.5 Exactly where 7/8 comes from

**CLAIMED inequalities; CERTIFIED algebraic endpoint check.** Put

\[
 \Delta=\beta_*-7/8\in(0,1/24],\quad\kappa=3/4+2\Delta,\quad
 b=1/8,\ h=13/16,\ \ell=1/6,\ l_x=17/48,\ l_y=23/48.
\]

The reflected-energy/additive-Gram Cauchy–Schwarz calculation gives

\[
 |I_{\eta,\mathrm{modified}}(Z)|\ll Z^{l_x/2+b/12+\epsilon}
 =Z^{3/16+\epsilon}.
\]

For a rescaled subset of total length \(d\), the extra exponent is
\(d-3d/2-d/2=-d\le0\). The principal residues give

\[
 C_{II}(s)=l_x/2+s-1+h/6=s-11/16.
\]

Thus matching the low scale with the reciprocal signal gives
\(\sigma_0-11/16=3/16\), i.e. **\(\sigma_0=7/8\)**. This choice also has to satisfy the high-side inequalities; matching alone proves nothing.

For a row norm \(U=Z^d\), zero-bin real part \(a\), \(\delta=2a-1\le\kappa\), prime-amplitude mean \(q\in[0,\delta/2]\), and row cardinality \(\ll U^{R+\epsilon}\), the relative exponent is (S §20.2)

\[
 E(d)=-\frac1{48}+\frac23\delta+\frac q6-h(1-R)
       +(d-h)(R+\delta/2-17/50).                                \tag{2.6}
\]

Above the floor \(\delta_0=1/50\), put \(x=q/\delta\), \(\alpha=5/6\),

\[
 D_x=3-17x/9,\quad P_x=2-26x/9+8x^2/9,\quad
 \mathcal J=(\alpha-\delta)D_x+\delta P_x,
 \quad t=1+\frac{\delta P_x}{2\mathcal J}.
\]

The inverse/plain counts balance at

\[
 R_*=1-\delta+(\alpha-\delta)(t-1)
     =1-\delta+\frac{\delta P_x}{D_x}(3/2-t).
\]

The actual capacity is \((1-2m)/(6\kappa)\), not its \(\Delta=0\) value. Replacing it by that baseline costs at most \(\Delta/4\) in the row exponent. The paper proves

\[
 -E_*(h)\ge\frac{49}{440640}>10^{-4},\qquad
 E_{\rm actual}(h)-\Delta
 \le-\frac{49}{440640}-\frac{51}{64}\Delta+\epsilon_{\rm total}.   \tag{2.7}
\]

For completeness the polynomial certificate, with \(y=1/2-x\), \(v=51+41y\), is

\[
\begin{split}
10368v\mathcal J(-E_*)={}&(3+5y)\{(4v\delta-79)^2+49\}\\
 &+4y\{4v\delta[(1+3y)(15+32y)\delta+9-13y]+265+3485y\}.
\end{split}
\]

Every summand is nonnegative on the specified rectangle. The script checks this identity by exact polynomial coefficients, not floating-point sampling. **Subtracting \(\Delta\)** in (2.7) is indispensable: the required high bound is relative to \(C(\beta_*)\), not to \(3/16\).

The other ranges are checked separately: floor \(E(h)\le-7/1200\); middle \(d\le1/2\) gives \(E\le-49/14400\); small rows have saving \(63/800\); large rows use an arbitrarily far absolute contour. Principal contour margins are \(23/960\) and \(13/9600\). Slots supply total length at least \(8/39>7/37\) near \(d=h\). Choose all real losses and slot mesh before the target, then choose target-dependent height exponent \(\tau\) and tail order \(N\) so

\[
 |J-f|\ll_{\eta,N}Z^{C(\beta_*)-m}(1+Z^\tau)^{A_\eta}
                 +Z^{B_\eta-N\tau}\ll_\eta Z^{C(\beta_*)-m/2}.
\]

Together with \(\omega=\Delta/2\), (2.3) contradicts \(\beta_*>7/8\).

**Assessment: uniformity means uniform zero-free boundary, not a supplied uniform conductor constant for every internal estimate.** Constants, finite exclusions, height orders and starting scales may depend on the fixed target. Only the positive continuation distance must not. Treating those internal \(\ll_\eta\) constants as uniform while \(\eta\) runs through all characters modulo \(4uv\) would be a quantifier error.

### 2.6 Dirichlet transfer and the separate Siegel method

**PROVED classical transfer, conditional on the Hecke result.** Norm pullback gives, away from finitely many nonzero Euler factors in \(\Re s>0\),

\[
 L_F(s,\chi\circ N)=L(s,\chi)L(s,\chi\chi_{-3}).
\]

A zero in the stated half-plane would be a zero of the Hecke product; the possible pole at 1 is treated separately using classical nonvanishing there. Imprimitive Euler factors introduce no zeros in this half-plane. This covers all moduli, not just prime moduli or real characters.

**CLAIMED independent method in L, not an input proving 7/8.** A real zero with \(\delta=(1-\beta)\log q\) small forces

\[
 \sum_{H<r\le U,\,\chi(r)=-1}\frac{\log r}{r}
 \ge\log U-C\log q-C\delta(\log U)^2/\log q-C_H.
\]

This follows classically from the positive logarithmic derivative of \(\zeta L\). In \(K=\mathbb Q(\sqrt d,\sqrt2)\), form an evaluation determinant on an \(N^4\) integer box, with three conjugate coordinates. The new rectangular interpolation lemma guarantees full rank for separate-degree product \(\gg N^4\), uniformly in the map and its aspect ratio, when its kernel coordinates are rationally independent. Greedy row order \(\alpha_1+H\alpha_2+H\alpha_3\) gives total exponents \(S_2/S_1=O(1/H)\).

At an inert prime \(r>H\), \(\theta^r\equiv\sigma\theta\) or \(\sigma\tau\theta\pmod r\); replacing \(\theta^{rk}\) by \((\theta^r-g_r\theta)^k\) lowers all correction row weights and extracts \(r^{\sum\lfloor\alpha_1/r\rfloor}\) without changing the determinant. Its nonzero integer norm then satisfies

\[
 S_1[\log U-C\log q-C\delta(\log U)^2/\log q-C_H]-CMU
 \le\tfrac14\log|N\Delta|\le
 (S_1+S_2)(\log N+\tfrac12\log q+O(1))+\tfrac M2\log M,
\]

where \(U=N^{4/3}\), \(M=N^4\). Choose \(H\) large, then \(N=\lceil q^\gamma\rceil\) with fixed large \(\gamma\). A sequence \(q\to\infty,\delta\to0\) would give \(1\le13/16+1/16=7/8\). This last **7/8 is an unrelated contradiction constant**, not the quasi-RH boundary. No divisor-class information appears in the determinant. The full strip already implies the real-gap conclusion with \(c=(\log3)/8\); the converse is false as an implication of the stated regions.

## 3. Lean: a genuine endpoint, not an independent run here

**CERTIFIED static scope.** `lean/docs/003.md` links four comparator challenges. Their JSON files point to actual solutions, not to the challenge files' intentional `sorry` stubs:

| endpoint | solution module under `OAI.NumberTheory` | local OAI import closure |
|---|---|---:|
| Dirichlet, ζ | `DirichletL.Nonvanishing` | 2,924 each |
| Hecke over F | `DirichletL.Hecke.Nonvanishing` | 2,925 |
| real-zero gap | `SiegelZeros.Main` | 306 |

The actual Dirichlet theorem is

```
{q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q) {s : ℂ}
(hs : (7 / 8 : ℝ) < s.re) (hpole : ¬ (χ = 1 ∧ s = 1)) :
  _root_.DirichletCharacter.LFunction χ s ≠ 0
```

This is Mathlib's actual `LFunction`, not an abstract function assumed to satisfy the desired result. Its conclusion has **no remaining moment or GRH assumption**. The chain is `Nonvanishing` → `Detector.FinalAssemblyUnconditional` → `FinalAssemblyCertifiedBands` → fine/chosen moment inputs → common probe → continuation. `Energy.CertifiedExistence.terminal_certificate` supplies the bands by finite width induction. The unused fine-mesh argument in the top assembly is not a detected defect: `FinalAssemblyCertifiedBands.source_moments` subsequently uses the mesh to build the marked moment input. The lower-level certificate itself has weaker prerequisites.

The Hecke endpoint uses a bespoke finite residue character, trivial on global units, with continuation defined by a theta Mellin transform and division by six. Its semantic identification with conventional Hecke functions requires the accompanying definitions/identities; it is not literally a Mathlib Hecke theorem. The ζ endpoint even includes the totalized value at 1 via `riemannZeta_one_ne_zero` (`Hecke/Dirichlet.lean:176`); that is not an assertion that ζ has no pole. The Dirichlet statement excludes the pole explicitly.

**CERTIFIED, limited.** A fresh recursive import scan, stripping nested comments, finds no missing local imports and no lexical `sorry`, `admit`, `sorryAx`, or `axiom` in these solution closures. Configurations permit only `propext`, `Quot.sound`, `Classical.choice`; `enable_nanoda` is false. `lean`, `lake`, and `elan` are unavailable on PATH. I did **not** run the comparator, compile, execute `#print axioms`, audit Mathlib's closure, or verify the bespoke Hecke definition equivalence. Thus “Lean-formalized per release, endpoint independently inspected” is warranted; “independently kernel-verified here” is not. Docs exclude the later applications, including the campaign deductions below, and do not list O as a separate comparator target.

**Assessment, gap check.** The most dangerous proof obligations are (i) zero-preserving theta reflection at shared/ramified primes; (ii) closing both recursions without allowing row-dependent arbitrary coefficients; (iii) genuine principal-signal noncancellation; (iv) target-independent exponent margins despite target-dependent height bounds. The text explicitly addresses all four. I checked the continuation logic, numerical certificate, capacity correction, nonzero normalization and order of choices; I did not independently re-prove all prerequisites. No identified flaw licenses dismissing the theorem, and the source scan does not license accepting it as a checked theorem either.

## 4. Transfer to B2: exact statements and exact losses

### 4.1 Correct the character decomposition first

**PROVED, elementary.** For the campaign pair family \(\mathcal P(p)\), write \(q_i=4uv\), \(a_i=-u-v\). All relevant \(p,a_i\) are units modulo \(q_i\). Orthogonality gives

\[
 R(p)=\sum_i\frac1{\varphi(q_i)}\sum_{\psi\bmod q_i}
             \psi(p)\overline{\psi(a_i)}.
\]

The principal and Brauer character give \(M_{BM}\), but

\[
 R=M_{BM}+Y_{\mathrm{other\ real}}+X_{\mathrm{nonreal}}
   =M_{\mathrm{gen}}+X_{\mathrm{nonreal}}.                       \tag{4.1}
\]

Thus the remainder after the main term specified in the question is **not only non-real characters**. A bound on the non-real part alone does not finish that decomposition.

**CERTIFIED counterexample to omitting other real characters.** At \(p=61\), pair \((u,v)=(2,3)\) is admissible, \(q=24\), \(a=19\). Every character mod 24 is real. Yet \(\chi_{-24}(61)=-1\), so the BM pair contributes \(1/4\); \(61\not\equiv19\pmod{24}\), so its exact contribution is zero. The other real characters contribute \(-1/4\), with **no non-real remainder at all**. This is a decomposition counterexample, not an ES counterexample.

### 4.2 Strongest direct restricted-family transfer located

**PROVED implication of the claimed sextic sieve.** For squarefree primary ideal sets \(\mathcal U,\mathcal V\), norms at most \(K,D\), fixed row-independent \(c_n\), and arbitrary \(b_u\), S's sextic sieve gives

\[
 \left|\sum_{u\in\mathcal U}b_u\sum_{n\in\mathcal V}c_n\chi_n(u)^{\pm1}\right|
 \ll(KD)^{\epsilon/2}[K+D+(KD)^{2/3}]^{1/2}
          \|b\|_2\|c\|_2.                                    \tag{4.2}
\]

Proof: Cauchy–Schwarz in \(u\), then S's sextic large sieve (lines 4707–4724). Arbitrary subsets are allowed by extending coefficients by zero. Equations (2.4)–(2.5) improve particular coefficient families beyond this norm bound, with exactly their stated restrictions.

**Assessment, exact specialization failure.** There is no established map from all \(\psi\bmod4uv\) to this fixed-target sextic family. Such \(\psi\) have unbounded orders; \(\chi_n(u)\) has order dividing six. Fixing a separate target for each \(\psi\) changes the datum and its constants and loses the family estimate. More importantly, the incidence coefficients for divisors of \(4Cp+1\) depend on the row/level. The canonical moment explicitly disallows such weights. An arbitrary mask encoding \(n\mid4Cp+1\) is not the common coprimality puncture allowed in (2.4)–(2.5).

Even in a favorable rectangular sextic model \(K=D=T\), unit coefficient norms make (4.2) only \(O(T^{5/3+\epsilon})\), versus \(T^2\) trivial size. At \(T=\sqrt p\), that is \(p^{5/6+\epsilon}\), still a factor \(p^{5/6+\epsilon}/\log^2p\) above the desired scale. This is a **model budget**, not an estimate asserted for B2. The special inverse moment would give \(O(H\sqrt D)\) for an outer sum of \(H\) unit rows, not positivity of a divisor count.

O does recover a fixed target from an average, so simply saying “averages cannot help” would miss its main idea. Its recovery uses many rows \(\varpi^6\) carrying almost the **same Möbius polynomial**, with the discrepancy supported on multiples of \(\varpi\). No analogous replication of \(R(p)\) is supplied: replacing \(p\) by \(p\varpi^6\) changes every side integer and admissible region, and the error is not an omitted Euler factor. That precise missing replication identity is why its average-to-pointwise step does not transfer.

### 4.3 Sharp one-point norm obstruction

**PROVED transfer/no-go lemma (no OAI assumption).** Let \(\mathscr F\) be any multiset of unit-valued character evaluations at a fixed integer \(p\), with positive weights \(w_j\), and \(B=\sum_jw_j\). Then

\[
 \left|\sum_j w_jc_j\psi_j(p)\right|
 \le\sqrt B\left(\sum_jw_j|c_j|^2\right)^{1/2}.                 \tag{4.3}
\]

The constant \(\sqrt B\) is **exact**, attained by \(c_j=\overline{\psi_j(p)}\). Therefore no zero-free region, zero-density theorem, or universal large-sieve theorem can replace it by a smaller constant for arbitrary such coefficients. This refutes an arbitrary-coefficient one-point saving, not a target-specific theorem for B2's special phases.

For pair-labelled residual characters \(w_{i,\psi}=1/\varphi(q_i)\), with principal and Brauer removed,

\[
 B=\sum_i\frac{\varphi(q_i)-2}{\varphi(q_i)}
   =|\mathcal P(p)|-2M_0(p)\asymp p\log p.
\]

Here \(|\mathcal P(p)|\asymp p\log p\) follows by counting coprime opposite-parity pairs in \(uv\ll p\); \(M_0\asymp\log^2p\). The actual coefficients \(\overline{\psi(a_i)}\) have norm squared \(B\). Thus (4.3) gives only \(|R-M_{BM}|\le B\), missing the required \(\log^2p\) scale by **\(\asymp p/\log p\)**. This also explains the singleton-column diagonal obstruction to an improved generic large sieve: a length-one sequence has no character-sum cancellation whatsoever. Grouping duplicate moduli can exploit special phases, but it is no longer an arbitrary-coefficient norm argument; that new arithmetic estimate is what is missing.

**PROVED further restrictions.** A universal two-sided polylogarithmic error for the actual B2 coefficients is false by the campaign's Linnik construction, independently of 003. A universal no-threshold positive lower bound is false already at \(p=409\): the exact check gives \(R(409)=0\), \(M_{BM}(409)=6918053/2311155\approx2.99333\). Neither refutes an eventual **one-sided** theorem. The best existing absolute bound \(p^{2/5+o(1)}\) from divisor counting is much better than (4.3), but still exceeds \(\log^2p\); no improvement to it is deduced here.

### 4.4 A genuine moving-moduli transfer, with its density cost retained

**PROVED, CONDITIONAL on OAI-003.** For any finite family of moduli \(q_i\) and Fourier polynomials \(f_i(a)=\sum_\psi c_{i,\psi}\psi(a)\), define
\(B_i=\sum|c_{i,\psi}|\), principal coefficient \(\delta_i\). The smoothed explicit formula gives, uniformly in this family,

\[
 \sum_i\sum_{n\le X}\Lambda(n)(1-n/X)f_i(n)
 =\frac X2\sum_i\delta_i+
 O\!\left(X^{7/8}\sum_iB_i\log(2q_i)
       +\log(2X)\sum_iB_i\log(2q_i)\right).                    \tag{4.4}
\]

Proof: sum the individual explicit formulas; for imprimitive characters remove prime powers dividing the inducing modulus. The zero sum is bounded using
\(\sum_\rho|\rho(\rho+1)|^{-1}\ll\log(2q_i)\), since functional equation plus the strip places zeros in \([1/8,7/8]\). Prime powers can be removed at cost \(O(\sqrt X\log^2(2X)\sum B_i)\). No modulus is required to be fixed as \(X\) grows. Uniformity here comes from the *conclusion plus classical zero counting*, not uniform internal constants of the theta recursion.

For a single class, \(B_i=1\), \(\delta_i=1/\varphi(q_i)\). Freeze the entire pair family at scale \(p\), and then average a **different variable** \(n\le X\). It has \(\sum B_i\asymp p\log p\), \(\sum\delta_i=M_0(p)\asymp\log^2p\), and \(\sum B_i\log(2q_i)\asymp p\log^2p\). Consequently the error/main ratio from (4.4) is

\[
             O(pX^{-1/8}).                                    \tag{4.5}
\]

At \(X\asymp p\), this is a **\(p^{7/8}\)** loss; to make this particular majorization small requires \(X\gg p^8\). That long free-prime average does not determine its prescribed coefficient at \(n=p\), even if the ratio became tiny. Restricting to a single progression rather than summing the pair family retains the familiar cost \(X\gg[\varphi(q)\log q]^8\), not \(\log^8q\).

**Assessment, strongest conclusion of this transfer audit.** Equations (2.4)–(2.5), (4.2) and (4.4) are real usable estimates with moving arithmetic data. None supplies the absent row-independent encoding, repeated-signal amplification, or target-sensitive one-sided cancellation for (4.1). The sharp negative lemma (4.3) rules out the coefficient-blind proposed strengthening. It does **not** prove a logical nonimplication “003 cannot imply ES.”

## 5. Additional campaign consequences missed by OAI_DUMP_IMPACT

**Scope.** The inventory below separates newly discharged hypotheses, weaker replacements, and effectivity-only changes. It includes named older results as well as current-frontier ones, but not every duplicate ledger mention. Searches covered tracked campaign Markdown, `notes.md`, and the cited paper sources for GRH, Siegel/exceptional zeros, SW, BV and ineffectivity. The previous memo already contains QNR/square roots in P, \(r,q^*,e^*\ll\log^8\), \(M_{BM}\sim3\log^2p/(2\pi^2)\), the genus lower bound, Thm U and the moving-window Thm 8.5. Those are not new entries here.

### 5.1 Discharged zero-gap premise: better obstruction-side tail

**PROVED implication, CONDITIONAL on OAI-003 and the campaign's named inputs.** `POINTWISE_TAIL.md` Theorem 3.3, R76 D4, becomes applicable without its additional real-zero hypothesis. With \(\mathcal L=\log T\), its range remains \(\log x\ge C\mathcal L^4\log\mathcal L\), but

\[
 \#\{p\le x:\ p\text{ Mordell-hard},\ W(p)>T\}
 \ge\pi(x)\exp[-C\mathcal L^3(\log\mathcal L)^2\log\log\mathcal L],        \tag{5.1}
\]

instead of the cubic \((\log\mathcal L)^3\) loss. Proof: \(1-\beta\ge1/8\) implies the required \(c_0/\log q\) gap; the leaf's exceptional-zero factor is at least \(1/2\), leaving only its square-class and residual-mass costs. This is a real quantitative missed consequence, not just effectivity.

### 5.2 A stronger infinite-sequence nonresidue obstruction, with a weaker constant than GRH

**PROVED, CONDITIONAL on the Dirichlet part of OAI-003.** For every \(\epsilon>0\), infinitely many Mordell-hard primes satisfy

\[
 r(p)>\left(\frac1{8\log2}-\epsilon\right)\log p\log\log p.      \tag{5.2}
\]

Hence the same lower bound applies to `POINTWISE_TYPEI.md`'s \(ck_{\min}\), \(H_4\), and every witness parameter known in `HARDNESS_MAP.md` A2–A4 to dominate \(r(p)\). This upgrades the \(\log p\log_3p\) order on these sequences, **not** to the original GRH constant \(1/(2\log2)\).

Proof: take the splitting detector of \(\mathbb Q(i,\sqrt\ell:\ell\le y)\), degree \(d=2^{\pi(y)+1}\), conductor divisors of \(F=8\prod_{3\le\ell\le y}\ell\). Its Fourier norm is 1 and density \(1/d\), with \(\log F=O(y)\). A nonnegative smooth dyadic prime sum has main \(\asymp x/d\) and error \(O(x^{7/8}\log F)\); higher powers cost \(O(\sqrt x\log^2x)\). Choose \(y=c\log x\log\log x\), \(c<1/(8\log2)\). Then \(d=x^{c\log2+o(1)}\), so the main dominates. A split prime in \([x/2,x]\) has \(r(p)>y\), and the signs of 2,3 and −1 force \(p\equiv1\pmod{24}\) (indeed all small prime signs force Mordell-hardness). Let \(x\to\infty\).

### 5.3 Actual bounded-exponent covering by all small primes

**PROVED, CONDITIONAL on OAI-003.** `FORCED_WINDOW.md` Proposition 5.1 has the replacement

\[
 \text{every }a\in\mathbb F_q^*\text{ is }\prod_{\ell\le C\log^8q,\ \ell\ne q}
                    \ell^{e_\ell},\qquad e_\ell\in\{-1,0,1\}.   \tag{5.3}
\]

This is stronger than merely subgroup generation, but concerns **all** small primes, not the factors of a prescribed window integer. Its old \(\log^4q\) GRH scale is not discharged. A naive unsmoothed substitution gives exponent 16; smoothing gives 8:

For each nonprincipal \(\chi\), (4.4) with \(X=C\log^8q\) gives
\(\sum_{\ell\le X}\log\ell(1-\ell/X)(1-\Re\chi(\ell))\ge cX\), and the total weighted prime mass is \(X/2+o(X)\). With \(C\) large, a positive fraction of this mass lies where the argument of \(\chi(\ell)\) is at distance at least \(1/6\) from an integer. There are \(\gg X/\log X\) such primes. On each,
\(|(1+\chi(\ell)+\overline\chi(\ell))/3|\le2/3\).
Fourier inversion for independent uniform exponents \(-1,0,1\) gives a positive probability for every target once
\((q-2)(2/3)^{cX/\log X}<1\). This holds. No repeated prime exponent or factorization oracle is used.

### 5.4 One non-Dirichlet consequence: the cubic case of the forcing–generation obstruction

**PROVED implication, CONDITIONAL on the finite-order Hecke part of OAI-003 and its conventional identification.** The \(\ell=3\) instance of `FORCED_WINDOW.md` Proposition 5.2 no longer needs Kummer-field GRH: for any \(c<1/(8\log3)\), infinitely many primes \(q\equiv7\pmod{12}\) have **every** rational prime \(s\le c\log q\log\log q\) a cube modulo \(q\).

Proof: over \(F=\mathbb Q(\omega)\), the extension
\(F(i,s^{1/3}:s\le y)\) is abelian of degree at most \(2\cdot3^{\pi(y)}\). Select the element trivial on the cubic radicals and nontrivial on \(i\); the quadratic extension is disjoint from the odd-degree cubic extension. All its Artin characters are finite-order Hecke characters **over this same F**. Their conductors have logarithm \(O(y)\): outside 2 and 3 ramification is tame and supported over the primes \(s\); at 2 and 3 the bounded exponent-six local character groups give an absolute conductor-exponent bound. Apply the Hecke analogue of the smoothed formula over the fixed quadratic base field. Main \(\gg x/3^{\pi(y)}\), error \(O(x^{7/8}y)\). Degree-two prime ideals and prime powers cost \(O(\sqrt x\log^2x)\). The choice \(y=c\log x\log\log x\) works as above, yielding degree-one primes with the specified Frobenius. This supplies the desired rational primes in \([x/2,x]\).

This **does not** discharge Proposition 5.2 for all odd \(\ell\): then the natural base is \(\mathbb Q(\zeta_\ell)\), outside 003. Nor does one fixed cubic case supply the all-index exclusion required by Hooley/Artin or one-fixed-mute-prime theorems. It is a genuine limited use of 003's Hecke scope, rather than mislabelling every Kummer field as Dirichlet.

### 5.5 Other replacements and effectivity inventory

**PROVED implications conditional on 003, relative to the existing campaign proofs.** The numerical strip gives effective SW and, by the classical large-sieve/Vaughan-identity proof, effective BV at its usual level \(x^{1/2}/\log^B x\) for each fixed requested saving. It is **not** obtained by summing individual \(x^{7/8}\) errors to that level. Weighted divisor-bounded BV variants follow by the same effective Cauchy–Schwarz/divisor-moment arguments. This removes precisely SW/BV/BDH ineffectivity, not unrelated ineffective theorems.

| missed item | exact change if 003 is accepted |
|---|---|
| `SYNTHESIS_SPARKS9.md` Prop. 2.2 | a positive level-BM term occurs at some \(4\mid t\ll\log^8(2n)\) for each odd nonsquare n; use the least **odd prime coprime to n** with \((n/\ell)=-1\), then \(t\le4\ell\). The \(\log^2 n\) GRH scale is not recovered; still no divisor-class hit. |
| `ASTRA_BRIDGE.md` §6 forced prime \(r\equiv3\pmod4\), \((r/p)=-1\) | the cited ineffective power bound becomes effective polylogarithmic, \(r\ll\log^8p\), by a fixed-density quadratic detector; no lattice intersection follows. |
| `EXCEPTIONAL_PRIMELAW.md` Prop. 4.3 | its exact signed prime-sum conclusion holds with coefficient budget \(T\le N^{1/8-\epsilon}\), instead of \(N^{1/2-\epsilon}\). Proof: error \(O(TN^{7/8}\log^2N)=O(N^{1-\epsilon}\log^2N)\) beats its \(N\exp[-O((\log N)^{3/4}(\log\log N)^{3/4})]\) main; removing \(|F|\le N^{1/2}\) primes costs only \(|F|T\). The original larger budget is not discharged. |
| `POINTWISE_XWIN.md` Thm. 1.5, Thm. 2.2 and Cor. 2.3 | all thresholds/constants become effective. In §3.3's suggested floor improvement one may use \(y=(\log N)^B\) rather than \(\exp((\log N)^\delta)\), with B large depending on θ and the desired error: summing progression errors over classes costs at most \((\log N)^{2\theta-B/8+o(1)}\). This removes the fixed δ-loss in the sieve's reciprocal-prime mass, leaving log-log losses; it does not extend the entropy range θ<θ*. |
| `notes.md` Thms. 12.2, 13.2, 13.11, 14.4, 14.8, 14.9 and supporting Lemma 13.8/stack estimates | effective versions with their existing exponents/ranges. These old exceptional/window theorems were already unconditional in truth, but SW-ineffective. |
| `notes.md` Prop. 52.3 | effective uniform all-slice bound for fixed θ, ε, \(h\le(\log X)^\theta\): \(\#\{p\le X:p\equiv a\pmod Q,M_{c,k}(p)=0\}\ll X/[\varphi(Q)(\log X)^{1+2(1-\epsilon)/\varphi(h)}]\), \(Q=\mathrm{lcm}(24,h)\). No exceptional conductor deletion is needed; no stacking conclusion is added. |
| `paper/es-threequarter-note.tex` main theorem and supply theorem | effective constants in \(E(N)\ll N\exp[-c(\log N)^{3/4}]\); the note expressly attributes ineffectivity to BV, with moduli at most \(4x^{1/3}\). Growing moment order does not introduce a new ineffective theorem: BV is used in the fixed supply input before the combinatorial assembly. |
| `EXCEPTIONAL_SHORT.md` interval/progression theorems; `EXCEPTIONAL_MN.md` Thm. A and its corollaries; corresponding `paper/es-mn-short-note` statements | the inherited constants/thresholds become effective, retaining the same interval-length, progression and numerator ranges. These are more consequences than just the Thm U item in the old memo, but no exceptional-set exponent increases. |
| `EXCEPTIONAL_WEIGHTS2.md` Prop. 3.1 and Cor. 3.2 | effective \(\mathrm{dens}(\mathcal A)\le\exp[-c(\log Y)^2]\) and its stated consequence; weighted BV was the ineffective input. Does not make the conjectured aligned-window estimate true. |
| `CEILINGS_UNIFIED.md` Props. 1.1, 4.2 and their dependent obstruction bounds | effective constants in \(\log(1/\delta^*(T))\gg(\log T)^3\) and the note-atom minorant threshold \(\log D\le c(\log T)^4\); they inherit the same BV supply. |
| `POINTWISE_OMEGA16.md` Prop. 4.1(b) | effective \(\log(1/\delta)\gg T^{1/2}(\log T)^{-8}\) for product subsets, via effective BDH/SW. The separate LS conjecture and its 1/3 implication remain conditional. |
| `UNIT_ORBIT_ES.md` Thm. 2.4; `FROBENIUS_FIRING.md` Thm. 4.2; `EXPONENT_CAP.md` Thm. 3.2 | effective thresholds for the stated at-least-four-fixed-mute-prime / growing-mute and subpolynomial-overflow constructions. Their sieve is effective once BV is; the multiplicative-independence exceptional-prime bound is elementary. No one-mute conclusion from this replacement. |
| `PHASE_DIAGRAM.md` Thm. 5.1; `CAP_INTERPOLATION.md` Thm. 2.1 | effective thresholds in the existing subpolynomial cap family and almost-all cap theorem, respectively; keep the existing n,A,η or cap dependence and all quantifiers. The pointwise GRH Thm. 4.2 is different and remains undischarged. |

**Assessment / cautious additional candidates, not promoted to proved campaign theorems.** `BOARD2_SLATE.md` §3 labels its full five-slice principal constant and GRH asymptotic as Assessment (Dirichlet-series sketch). For each fixed 2-adic sector the old memo's Halász argument applies also to \(\chi_p\) times a fixed mod-\(2^k\) character; it therefore removes that sector's quadratic twist at \(o(\log^2p)\) cost. The advertised full asymptotic \(45\log^2p/(8\pi^2)\) still needs the sketch's principal-term and sector-tail bookkeeping; 003 alone does not upgrade its existing proof status. `CONSTRUCTIVE_ES.md` §4's recalled Pizer/Ibukiyama auxiliary prime can now be found deterministically in polynomial time, and its small-modulus square root by exhaustive search, giving the stated input data. The note's stronger quoted supersingular/maximal-order algorithm runtimes were not proved there and are not re-certified here. `PHASE_DIAGRAM.md`'s Gallagher-range “should give” remark remains an uncarried-out argument, not a theorem whose conditional premise can simply be deleted.

**Assessment / exclusions reviewed.** No upgrade to ES, \(H_4\) upper bounds, cap zero, \(V_\phi\), general one-fixed-mute-prime Artin, arbitrary Kummer GRH, Selberg eigenvalues/SEL, EH, the exact GRH logarithmic-square cap, or the original GRH coefficient budgets follows from this audit. Schinzel H, Dickson, W, EQ, S, LS and H⁻BM remain extra hypotheses. “Siegel” in the ineffective integral-point theorem for windmills is Siegel's theorem on integral points, not a Siegel zero; 003 does not make it effective. Already-effective obstruction results are not counted again.

## 6. Decision and reproducibility

**Assessment.** The most promising *methodological* transfer would be a B2-specific replication/amplification identity playing the role of O's sixth-power rows, or a class-sensitive one-sided variant of the marked moment with the actual divisor incidence coefficients. Neither is present. Writing the forbidden row-dependent weight into (2.4) or replacing the whole character group by a sextic family is not progress. Even granting the release, existing T1/numerator-8 tests, Linnik spikes and the finite failures survive. Small-prime sign supply and subgroup covering are useful, but factor/exponent budgets remain the bottleneck.

**Next steps (Assessment).** First run the actual 003 comparators and axiom audit in a provisioned Lean environment, then independently audit the theta/cube-removal and centered plain-moment inductions. For the campaign, retain (5.1)–(5.4) as explicit conditional consequences; the cubic case deserves a conventional-Hecke semantic check. Do not pursue B2 through a generic large-sieve strengthening refuted by (4.3). A proposed new route must state a concrete replication identity or a one-sided estimate for the **exact** remainder (4.1), including the other real characters.

**CERTIFIED checks.** `scripts/z48_oai003_check.py` records source hashes, release commit, all four comparator configurations and local import-closure counts; verifies the endpoint polynomial by rational coefficient arithmetic; and replays the \((61,2,3)\) decomposition counterexample and \(R(409)=0<M_{BM}(409)\). Output: `data/z48_oai003/checks.json`. These checks do not validate analytic estimates or Lean proof terms.

```sh
ulimit -v 8000000
timeout 180 uv run python scripts/z48_oai003_check.py
```

**Final status: CONDITIONAL tool/obstruction upgrades; no new B2 bound, no ES proof.**
