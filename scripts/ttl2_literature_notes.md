# Exceptional-Maass large-sieve literature notes

## Pascadi (most directly relevant)
- Alexandru Pascadi, “Large sieve inequalities for exceptional Maass forms and the greatest prime factor of \(n^2+1\),” arXiv:2404.04239 (2024), https://arxiv.org/abs/2404.04239 (PDF: https://arxiv.org/pdf/2404.04239). Formulas/theorem numbering below are from the arXiv text.
- **Theorem 2**, individual level: for \(\epsilon,X>0,N\ge1/2,\alpha\in\mathbb R/\mathbb Z,q,a\in\mathbb Z_{>0}\), with its level/cusp notation and canonical scaling matrix,
  \[
  \sum_{\lambda_j<1/4} X^{2\theta_j}\left|\sum_{n\sim N}e(n\alpha)\rho_{j,\mathfrak a}(an)\right|^2
  \ll_\epsilon (qaN)^\epsilon(1+aN/q)N,
  \]
  provided \(X\ll \max(N,aq)/\min_{t\ge1}(t+N\|t\alpha\|)\). In particular valid uniformly in \(\alpha\) for \(X\ll\max(N,a\sqrt{qN})\). Smooth weight \(\Phi(n/N)\) is permitted. The forms here have trivial nebentypus; coefficients are exponential phases (smoothly weighted), not arbitrary \(a_n\).
- In the discussion immediately after Theorem 2 (arXiv p. 5), Pascadi records DI [9, Thm. 7]: for \(a=1,\mathfrak a=\infty\), \(\alpha\) independent of level, the same type of bound averages over \(q\sim Q\) in range \(X\ll\max(N,Q^2/N)\). He says DI stated \(\alpha=0\), while the proof is uniform in \(\alpha\).
- **Theorem J**, §3 (equation (3.34)–(3.35), arXiv pp. 18–19), gives the explicit DI level-average consequence: for \(X>0,N,Q\ge1/2,\omega\in\mathbb R/\mathbb Z\), cusp infinity and identity scaling matrix,
  \[
  \sum_{q\sim Q}\sum_{\lambda_j(q)<1/4}X^{2\theta_j(q)}\left|\sum_{n\sim N}e(n\omega)\rho_{j,\infty_q}(n)\right|^2
  \ll_\epsilon (QN)^\epsilon(Q+N)N,
  \quad X\ll\max(N,Q^2/N).
  \]
  Theorem J states exponential-phase coefficients; as noted, interval/constant coefficients are a specialization. This displayed bound does not expose the sharper \(\sqrt{NX}\) term of DI Thm. 7 mentioned in the task.
- **Theorem 13** (5.3) is Pascadi’s general individual-level inequality, not a level-average or nebentypus theorem. For complex coefficients \(a_n=f(n/N)\check\mu(n)\), bounded-variation measure \(\mu\), it bounds the exceptional sum by \((qaNX)^{2\epsilon}(1+aN/q)A^2\), under (5.4) \(A\gg\|a_n\|_2+\sqrt{\gcd(a,q)N/(q+aN)}|\mu|(\mathbb R/\mathbb Z)\) and (5.5) \(X\ll\max(1,q/(aN))\max(1,A^2/I_N(\mu))\). Epsilon-loss is explicit as displayed (with the usual adjustable epsilon convention). This theorem is stated in the trivial-character framework.

## Drappeau: explicit nebentypus analogue
- Sary Drappeau, “Sums of Kloosterman sums in arithmetic progressions, and the error term in the dispersion method,” Proc. LMS 114 (2017), arXiv:1504.05549: https://arxiv.org/abs/1504.05549 (PDF https://arxiv.org/pdf/1504.05549).
- §4.2.3, **Lemmas 4.8–4.10** (arXiv pp. 15–16) explicitly adapt DI exceptional-spectrum inequalities to \(\Gamma_0(q)\) with Dirichlet multiplier \(\chi\) modulo \(q_0\), where \(q_0\mid q\); \(\mathcal B(q,\chi)\) denotes the corresponding basis, and \(a=\infty\) has level-independent scaling matrices. Set
  \[
  E_{q,a}(Y,(a_n))=\sum_{f\in\mathcal B(q,\chi),\,t_f\in i\mathbb R}Y^{2|t_f|}\left|\sum_{N<n\le2N}a_n n^{1/2}\rho_{f,a}(n)\right|^2.
  \]
  For arbitrary complex sequence \((a_n)\), **Lemma 4.9** states, for \(Y\ge1,Q\ge q_0\),
  \[\sum_{q\le Q,\ q_0\mid q} E_{q,\infty}(Y,(a_n))\ll_\epsilon (QN)^\epsilon(Qq_0^{-1}+N+NY^{1/2})\|a\|_2^2.\]
  **Lemma 4.10** strengthens this when \(a_n\) is the characteristic function of an interval:
  \[\sum_{q\le Q,\ q_0\mid q} E_{q,\infty}(Y,(a_n))\ll_\epsilon (QN)^\epsilon(Qq_0^{-1}+N+(NY)^{1/2})N.\]
  Thus the twisted setting does allow level averaging over all levels divisible by the character modulus; it is not a sum over a dyadic range of the cofactor alone. \(q_0\) is fixed as the character modulus in this formulation. Lemma 4.8 is the individual-level counterpart: \(E_{q,a}\ll_\epsilon(1+(\mu(a)NY)^{1/2})(1+(q_0\mu(a)N)^{1/2+\epsilon})\|a\|_2^2\), with \(\mu(a)=(w,q/w)/q\) for cusp equivalent to \(u/w\), \(w\mid q\).
- Drappeau’s \(Y^{2|t_f|}\) is exactly the exceptional growth weight (for \(t_f=i\theta_f\), it is \(Y^{2\theta_f}\)); the displayed coefficient normalization includes \(n^{1/2}\rho_{f,a}(n)\). These lemmas are the clearest source for a nebentypus level-average statement, with explicit \((QN)^\epsilon\) loss.

## Density results / surrounding references
- Peter Humphries, “Density theorems for exceptional eigenvalues for congruence subgroups,” Algebra & Number Theory 12 (2018); arXiv:1609.06740: https://arxiv.org/abs/1609.06740 (PDF https://arxiv.org/pdf/1609.06740). **Theorem 1.5**, formulae (1.6)–(1.8), counts weight-zero forms with \(it_f\in(\alpha_0,1/2)\), i.e. exceptional eigenvalues, on \(\Gamma_1(q)\), \(\Gamma(q)\), and \(\Gamma_0(q)\) with nebentypus \(\chi\). For empty prime set \(P\), the first two bounds are \(\ll_\epsilon \operatorname{vol}(\Gamma_1(q)\backslash\mathbb H)^{1-3\alpha_0+\epsilon}\) and \(\ll_\epsilon \operatorname{vol}(\Gamma(q)\backslash\mathbb H)^{1-8\alpha_0/3+\epsilon}\); (1.8) gives the analogous \(\Gamma_0(q),\chi\) bound with exponent \(1-4\alpha_0+\epsilon\), multiplied by \(\min(\dot Q^{4\mu_0\alpha_0},\ddot Q^{1-4\mu_0\alpha_0})\). With nonempty \(P\), the powers acquire the additional \(\sum_{p\in P}\mu_p\log(\alpha_p)/\log p\) term exactly as (1.8). This is a single-level density/counting theorem, not a Fourier-coefficient large sieve. Theorem 1.9 improves the exponents for squarefree \(q\). The paper explicitly obtains Γ1/Γ(q) by character orthogonality and treats nebentypus.
- Henryk Iwaniec, “Small eigenvalues of Laplacian for \(\Gamma_0(N)\),” Acta Arith. 56 (1990), 65–82, https://eudml.org/doc/206300 (journal DOI https://doi.org/10.4064/aa-56-1-65-82). Relevant as an earlier small-eigenvalue counting/density result for \(\Gamma_0(N)\); it is not a general-coefficient exceptional Fourier large sieve and does not supply the requested nebentypus/Γ1 level-average formula.
- Blomer–Milićević, “Kloosterman sums in residue classes,” JEMS 17 (2015), 51–69, arXiv:1410.4538 https://arxiv.org/abs/1410.4538. This is a Kloosterman-sum-in-progressions paper, not a stated exceptional-Maass Fourier-coefficient large sieve/density theorem; relevant methodologically, but no direct theorem matching the requested weighted level-average formulation identified.

## Other requested citations
- Jared Duker Lichtman, arXiv:2211.09641 https://arxiv.org/abs/2211.09641. The paper cites/uses Deshouillers–Iwaniec Kloosterman-sum estimates (e.g. its Lemma 7.5, citing DI Thm. 12), but the text search did not identify a DI Thm. 7 exceptional-Maass large sieve or a nebentypus version used there. The relevant result is not a replacement for the above level-average inequality.

## Applicability boundary relevant to the proposed levels
- Drappeau’s formula averages levels \(q\le Q\) divisible by fixed character modulus \(q_0\), with the \(Q/q_0\) main level term. It does not state an average restricted to levels \(4dq^2\) with varying dyadic \(d\) and a separately fixed small \(q\), nor does it state a restriction to an arbitrary subset of levels. The Selberg/Kuznetsov theorem’s stated divisibility condition is precisely \(q_0\mid q\). For the proposed \(M=4dq^2\), the character-modulus/divisibility alignment must therefore be checked before claiming direct applicability; none of the sources above states that specialized family verbatim.
