# Z3135 — required uniform prime-tuples theorem and its two separate gaps

**CONJECTURAL needed theorem; PROVED comparisons to stated results. ES is OPEN.**

Fix k,ε,η>0. For every T→∞ and system L_i(t)=a_i t+b_i with 1≤a_i≤T^(1+ε), |b_i|≤T^(1+ε), primitive (a_i,b_i)=1, distinct nonproportional coefficient pairs, and T^η≤L_i(t)≪T^(2+ε) on a subinterval I⊆[1,T] of length ≍T, put
 ν_ℓ=#{t mod ℓ:∏_i L_i(t)≡0(ℓ)}, S(L)=∏_ℓ(1−ν_ℓ/ℓ)/(1−1/ℓ)^k.
Assume local admissibility ν_ℓ<ℓ for every prime. A sufficient uniform Hardy–Littlewood statement is
 #{t∈I∩Z: all L_i(t) prime}=(1+o_{k,ε,η}(1)) S(L) ∫_I dt/∏_i log L_i(t),
where the relative o(1) is uniform over the entire coefficient class. The ES scheme additionally needs a verified map from these tuples into certificates, a nonempty admissible interval, and an integral main term tending to infinity; if it supplies a much smaller box, the error must instead be relative to that box. A one-sided lower bound of the same scale would suffice, so the full asymptotic is stronger than necessary. Many-to-one parametrisations do not justify extending I beyond the proved feasible parameter range.

**A premise correction beyond coefficient uniformity.** Green–Tao, arXiv:math/0606088, §1 Example 2 (full-text lines 348–351), says explicitly: “any system with d=1 and t>1 has infinite complexity.” Thus several forms in ONE variable are not covered by GTZ even with fixed tiny coefficients: (t,t+2) is twin primes. Pairwise nonproportional affine coefficient vectors do not fix the proportional homogeneous parts. The relevant GTZ theorem instead assumes finite complexity in several independent variables (no two forms affinely related). Its original size is Σ|linear coefficients|+Σ|constant term|/T, bounded by a fixed L (Definition 1.1); the o_{d,k,L}(T^d) is not uniform for L≈T^(1+ε). Treating the fixed p as an averaged second variable changes the quantifier and does not produce a certificate for each p.

**Known genuine uniform improvement.** Pierre-Yves Bienvenu, *A higher-dimensional Siegel–Walfisz theorem*, Acta Arith. 179 (2017), 79–100, arXiv:1607.06625, Theorem 1.3, allows linear coefficients O((log T)^B), constants O(T(log T)^B), with fixed d,k,A,B,L, finite complexity, local admissibility, and convex K of volume ≫T^d(log T)^(−A). This is a real growing-coefficient result and must not be omitted from the comparison. It does not approach polynomial coefficients T^(1+ε), and it does not remove the one-variable infinite-complexity obstruction. Full theorem text was fetched, not just a search snippet.

For a single form qt+b, with 1≤b≤q,(b,q)=1, x≈qT:
* Brun–Titchmarsh gives at most 2x/[φ(q)log(x/q)]≈2qT/[φ(q)log T] primes in the progression (up to endpoint details). It is an upper bound, hence supplies no certificate and no asymptotic lower bound.
* Siegel–Walfisz supplies the asymptotic uniformly for q≤(log x)^A with fixed A; q≈T^(1+ε) is far outside this range.
* Even GRH's standard progression error O(√x log²x) is smaller than the Λ-weighted main term x/φ(q)≈T only when roughly q≪T/(log x)^4. At q=T^(1+ε), its ratio is about T^(ε/2) times logarithms (ignoring the benign φ(q)/q factor), so this standard bound alone is insufficient.
* Average-over-q distribution theorems do not give the required every-coefficient/every-p lower bound. Likewise a least-prime theorem in a progression does not generally put that prime inside the required short parameter interval, nor address a simultaneous prime tuple.

Sources and reproduction: saved `green_tao.txt` from https://arxiv.org/pdf/math/0606088; `bienvenu_full.txt` from https://arxiv.org/html/1607.06625v1 and publisher `bienvenu.txt`. No prime-tuple computation can settle either missing uniformity theorem; the task here was the precise theorem/range comparison, which is complete. No claim that GTZ is merely missing a constant-uniformity refinement in the one-variable case is retained.
