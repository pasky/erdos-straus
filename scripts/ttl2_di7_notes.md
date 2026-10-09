Deshouillers–Iwaniec, “Kloosterman sums and Fourier coefficients of cusp forms” (Invent. Math. 70 (1982)); PDF p. k = journal p. 218+k.

1. Theorem 7 and its proof
- Theorem 7 is (1.41), journal p. 233 (PDF 15): for Q,N,X ≥ 1 and ε>0,
  Σ_{q≤Q} Σ_{λ_j exceptional for Γ₀(q)} X^{4iκ_j} |Σ_{n≤N} ρ_{j∞}(n)|² ≪ε (QN)^ε (Q+N+√(NX))N.
  The implied constant depends on ε alone. Exceptional means 0<λ_j<1/4, κ_j=i|κ_j|, so X^{4iκ_j}>0.
- Proof is §8.2, journal pp. 276–278 (PDF pp. 58–60). It proves (8.17) first for characteristic sequences of intervals, N≤N₁≤2N. Apply the earlier averaged Kuznetsov identity (8.7), partial summation and Theorem 14 to obtain (Q N)^ε-type losses; then use the Y-aspect device (8.18), and induction on Q in (8.19), finishing by scaling in Y. In the final induction, the epsilon losses are explicitly combined into (QN)^{5ε}; since ε is arbitrary this is renamed (QN)^ε in (8.17)/(1.41). The supporting Theorem 6 argument is §8.2, pp. 273–275: recurrence (8.5), induction on Q (8.12), and the large sieve Theorem 2. Theorem 7's proof is not simply a divisor-bound argument: the loss is the flexible ε-loss in the Kloosterman-sum estimate (Theorem 14) and the induction/absorptions; no τ(c) Weil bound is the source. Nor is it a fixed logarithmic loss or a constant-per-step induction loss.
- The proof gives an arbitrary-power loss (QN)^ε, not an effective quantitative dependence on ε. It does not establish replacement by exp(C log(QN)/log log(QN)) or by a fixed power of log(QN); those are stronger, specific subpower bounds and do not follow from the ε-notation/induction as presented. The factor multiplies the entire parenthesis, so the loss applies to all three Q, N, and √(NX) contributions, not just one.
- No additional restriction such as X≤Q or N≤Q is imposed in Theorem 7: it states Q,N,X≥1. In the proof, intermediate ranges are handled by the Y-argument and induction; the theorem's bound is unrestricted.
- Smooth weights: not literally verbatim, since the proof is stated for interval characteristic sequences and the theorem itself for n≤N. But partial summation from the interval-prefix bound gives the same estimate (up to a constant depending on a fixed smooth w, e.g. its bounded total variation) for a_n=w(n/N); no new spectral argument is needed. The q-summands are nonnegative (X^{4iκ_j}>0 and absolute square ≥0), so a sum over any subset of levels q≤Q is bounded by the full sum, with the same right-hand side.

2. Fourier-coefficient normalization
- Journal p. 226 (PDF 8), (1.15): for a cusp form u and cusp a,
  u(σ_a z)=y^{1/2} Σ_{m≠0} ρ_a(m) K_{i|κ|}(2π|m|y)e(mx).
  The paper defines the Fourier coefficients ρ_a(m) using this expansion. At the cusp ∞ this gives ρ_{j∞}(n) in Theorem 7. (The printed (1.15) uses K_{i|m|}; the index is the spectral parameter, not the Fourier index.)
- The basis is orthonormal for the usual Petersson/L² inner product on Γ₀(q)\H, using hyperbolic measure dx dy/y² on a fundamental domain; it is not probability-normalized. Journal p. 225 (PDF 7) specifies the Petersson inner product as integration over a fundamental domain, and p. 231 (PDF 13), (1.34), gives for the full modular group the corresponding expansion u_j(z)=√y Σ_{m≠0}ρ_{j∞}(m)K_{iκ_j}(2π|m|y)e(mx). No extra level-volume normalization is inserted.

3. Theorem 2 (general spectral large sieve)
- Journal p. 230 (PDF 12), (1.28)–(1.30): for K≥1, N≥1/2, ε>0, a complex sequence a_n, and a cusp a of Γ₀(q), each of the three quantities
  Σ_{2≤k≤K, k even} ((k−1)!/(4π)^{k−1}) Σ_{1≤j≤θ_k(q)} |Σ_{N<n≤2N} a_n n^{(k−1)/2} ψ_{jk}(a,n)|²,
  Σ_{|κ_j|≤K} (1/(cosh πκ_j)) |Σ_{N<n≤2N} a_n ρ_{ja}(n)|²,
  Σ_{−K≤r≤K} ∫ |Σ_{N<n≤2N} a_n n^{ir} φ_{ca}(1/2+ir)|² dr
  are each ≪ε (K²+μ(q)N^{1+ε}) ||a_N||₂².
  Here ||a_N||₂²=Σ_{N<n≤2N}|a_n|² (p. 230); μ(q) is defined in (1.1). The ε occurs only on N^{1+ε}; K² has no ε-loss. In (1.29) the sum is over |κ_j|≤K, so it includes exceptional eigenvalues (κ_j imaginary, with |κ_j| in the interval); the printed cosh denominator is positive for these as well. Theorem 2 says “each” expression separately, not their sum.
