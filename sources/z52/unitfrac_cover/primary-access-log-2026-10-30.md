# Primary-source access log — 2026-10-30

This note records what was directly opened on 2026-10-30 for the z52 L2 dossier. “Abstract page opened” does not mean the proof was read. Source access can be audited at the URLs listed below.

## Unit fractions

- Croot, `math/0311421`: https://arxiv.org/html/math/0311421 — full HTML opened. Main Theorem (intro): for `C⊂C'(N,N^{1+δ};θ)` with `δ+θ<1/4`, if `Σ_{n∈C}1/n>6`, then some subset sums to 1. Proof makes `E(h)=∏(1+e(h/n))` and bounds major/minor arcs. Coloring corollary: any r-colouring `[2,b^r]` has monochromatic subset reciprocal sum 1. Engine: smoothness restrictions, Fourier/circle orthogonality, and divisor/cancellation structure; not a generic density increment.
- Bloom, `2112.03726v2`: https://arxiv.org/html/2112.03726 — full HTML opened. Theorem 2: positive upper density A yields a finite subset with reciprocal sum 1. §3 explicitly calls its engine Fourier analytic, detects subset sums `1/k` via Fourier expansion, and adapts Croot; proof prunes to near-smooth denominator sets. Appendix says proof formally verified in Lean with Bhavik Mehta. Engine directly checked from full text.
- Liu–Sawhney, `2404.07113v1`: https://arxiv.org/html/2404.07113 — full HTML opened. Theorem 1.1: reciprocal mass at least `(log N)^{4/5+o(1)}` suffices for a subset summing to 1. §3, Proposition 3.2 uses random inclusion probabilities and Fourier expansion; major/minor arc split. §6 applies smooth-number sieve and pruning; the paper calls this refinement of Croot/Bloom. Engine directly checked.
- Conlon–Fox–He–Mubayi–Pham–Suk–Verstraëte, `2404.16016v2`: https://arxiv.org/html/2404.16016 — full HTML opened. Theorem 1: for fixed positive rational x, exact number of subsets of `[n]` summing reciprocals to x is `2^{c_x n+o(n)}`. Introduction explicitly says engine is entropy upper/lower bounds plus absorption, with modular inverse subset sums to repair denominators (Theorem 2). The title exists as “A Question of Erdős and Graham on Egyptian Fractions.” Search for the proposed compound “Set-coloring Ramsey / Erdős–Graham” title found no such combined paper; Conlon's author page lists Set-coloring Ramsey numbers as a separate work, unrelated topic.
- Chen–Elsholtz–Jiang, `1108.6118v1`: https://arxiv.org/abs/1108.6118 — full arXiv record opened. Abstract/Theorem claims: odd-denominator k-term counts, and for multiplicative semigroup denominators whose reciprocal sum exceeds 1, nonzero representation counts for infinitely many k in finitely many arithmetic progressions. Journal ref Acta Arith. 154 (2012), 109–123.
- Sawin, `2607.15419v1`: https://arxiv.org/abs/2607.15419 — arXiv page opened. Abstract gives positive-density sets avoiding pairs whose reciprocal average is a unit fraction; no proof method assigned from abstract.
- Korsky, `2607.04157v2`: https://arxiv.org/abs/2607.04157 — arXiv v2 record opened; updated 2026-10-08. Abstract gives gap `exp(-c sqrt(K log K))` below 1 from a finite multiset with total >K; abstract itself says combine equal fractions, Fourier estimate on comparable-contribution groups, elementary divisor counts.
- Kovač–Tang, `2607.28387v2`: https://arxiv.org/abs/2607.28387 — arXiv v2 record opened; updated 2026-08-04. Abstract gives eventual greedy best underapproximations for every positive rational, with/without repetitions; optimal-control/Bellman function method.
- van Doorn–Tang, `2512.22083v2`: https://arxiv.org/abs/2512.22083 — arXiv v2 record opened; updated 2026-05-24. Abstract gives `v(k)≥exp(c k²)` for smallest denominator omitted from all distinct k-term decompositions of 1; accepted for Math. Proc. Cambridge Philos. Soc.
- Bloom, `2305.02689v1`: https://arxiv.org/abs/2305.02689 — arXiv record previously opened via export API, not full text; abstract-level claims only.
- Martin, `math/9811112`: https://arxiv.org/abs/math/9811112 — arXiv page opened via API record search; abstract-level claims only: dense Egyptian fractions, representation length proportional to maximum denominator, exceptional largest denominators density zero.
- Elsholtz, “Sums of k Unit Fractions,” Trans. AMS 353 (2001), 3209–3227 — journal metadata searched, primary full paper not accessed; do not quote an exact theorem here.

## Covering systems

These entries were opened today through their arXiv abstract pages / source abstracts; no proof text was read unless noted in the dossier. Exact statements and bibliographic details are in §1 below.
- Hough, https://arxiv.org/abs/1307.0874
- Balister–Bollobás–Morris–Sahasrabudhe–Tiba, squarefree Erdős–Selfridge, https://arxiv.org/abs/1901.11465
- Cummings–Filaseta–Trifonov, https://arxiv.org/abs/2211.08548
- Klein–Koukoulopoulos–Lemieux, https://arxiv.org/abs/2212.01299
- BBMST, “The structure and number of Erdős covering systems,” https://arxiv.org/abs/1904.04806
- BBMST, “On the Erdős Covering Problem: the density of the uncovered set,” https://arxiv.org/abs/1811.03547
- Lopez, “A Complete Congruence System for the Erdos-Straus Conjecture,” https://arxiv.org/abs/2404.01508
- Filaseta–Kalogirou–Klein, https://arxiv.org/abs/2610.34541

## Additive combinatorics

Sources/access levels are recorded in §1. The equivalence to subset sums after discrete logarithms is elementary and proved in the dossier, not attributed to a cited paper. Primary source pages opened: Vu, https://arxiv.org/abs/math/0506483; Savchev–Chen, https://arxiv.org/abs/math/0602568; Gao–Geroldinger, https://doi.org/10.1016/j.exmath.2006.07.002 (metadata); BBG, https://doi.org/10.1112/S0024610706022721 (journal record). Claims requiring theorem statements not accessible in these sources are explicitly marked not verified rather than reconstructed from memory.