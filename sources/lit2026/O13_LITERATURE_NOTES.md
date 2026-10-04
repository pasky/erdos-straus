# Modular inverses, short Kloosterman sums, and small congruence solutions

Research notes, checked against the extracted text of the archived PDFs listed below (PDF page numbers are printed pagination unless stated). Bounds with `o(1)` have the usual uniform epsilon interpretation. The central distinction is between **translated boxes** and boxes at the origin: Cilleruelo–Garaev’s strongest result is for arbitrary translated intervals, whereas the origin admits an elementary integer-lifting/divisor argument that is especially effective for `s t² ≡ w`.

## Archived arXiv papers and relevant statements

### J. Cilleruelo and M. Z. Garaev, “Concentration points on two and three dimensional modular hyperbolas and applications,” GAFA 21 (2011), 892–904. arXiv:1007.1526v2. Archived `arxiv-1007.1526-cilleruelo-garaev.pdf`; SHA-256 `8d853cffda866282e4988234bfa21dbb7f8c99b158b6fa6cc19f954df8b91bfd`.

The paper defines `I₂(M;K,L)` as the number of `xy ≡ λ (mod p)`, `K+1≤x≤K+M`, `L+1≤y≤L+M`, for prime `p`, `1≤M≤p`, `p∤λ`. **Theorem 1, p. 2** (quoted): “Uniformly over arbitrary integers K and L, we have `I₂(M;K,L) < M^{4/3+o(1)}/p^{1/3} + M^{o(1)}`. When `K=L`, we have `I₂(M;L,L) < M^{3/2+o(1)}/p^{1/2} + M^{o(1)}`.” Consequently it is `M^{o(1)}` for `M<p^{1/4}` in arbitrary boxes. Also **Corollary 1, p. 2** gives `I₂ ≪ M²/p + M^{4/5+o(1)}` (and diagonal `≪M²/p+M^{3/4+o(1)}`). **Theorem 2, p. 3**: if `M≪p^{1/8}`, then uniformly in `L`, the count `I₃(M;L)` for `xyz≡λ (mod p)`, all three variables in `[L+1,L+M]`, is `≪M^{o(1)}`. This is a three-variable product, not `x y²`; it does not imply the same bound for a repeated variable.

**Assessment:** For the simpler product congruence and arbitrary same-side-length translated boxes, this is the strongest particularly relevant pointwise concentration estimate here. It does not treat composite moduli or `x y²` specifically. At origin with unequal side lengths, use the lifting bound in Bottom line; its `xy` specialization also applies. For `x y²` in a prime-field translated box, none of these theorems states the desired result.

### J. Bourgain and M. Z. Garaev, “Sumsets of reciprocals in prime fields and multilinear Kloosterman sums,” arXiv:1211.4184v1. Archived `arxiv-1211.4184-bour-gar-reciprocals.pdf`; SHA-256 `937f881bd7de4bd5937618543a3516ea876232a1ea87e44f89e16d5fe711474d`.

This is a long paper on additive energies/sumsets of reciprocals, with multilinear Kloosterman applications, not a pointwise estimate for a single short interval of inverse squares. **Theorem 1, p. 3**: for fixed positive integer `k`, the number `J₂k` of solutions `x₁⁻¹+…+x_k⁻¹=x_{k+1}⁻¹+…+x_{2k}⁻¹` in an arbitrary nonzero interval `I⊂F_p` satisfies `J₂k < (|I|^{2k²/(k+1)} + |I|^{2k}/p) |I|^{o(1)}`. **Theorem 2, p. 3**: if `|I|<p^{3/46}` and `λ∉I⁻¹∪{0}`, the number of `x,y,z∈I` with `x⁻¹+y⁻¹+z⁻¹=λ` is `<|I|^{2/3+o(1)}`.

**Assessment:** It controls additive structure of reciprocal sets (and sumsets), hence is relevant technology/context for inverse distributions, but neither statement bounds `#{t≤t₀: wt⁻² mod p≤Y}` for every `w`. No direct pointwise `N(q,w)` theorem follows without additional argument.

### J. Bourgain and M. Z. Garaev, “Kloosterman sums in residue rings,” arXiv:1309.1124v1. Archived `arxiv-1309.1124-bour-gar-residue-rings.pdf`; SHA-256 `3746adb39e0a64bdbab19f49596e9623ba943ca505211b95224ed0ca04d8d785`.

**Theorem 1, p. 2** bounds reciprocal additive energy for general modulus `m`: for `I=[1,N]`, `J₂k` counts `x₁*+…+x_k* ≡ x_{k+1}*+…+x_{2k}* (mod m)`, `x_j∈I` (the star is the multiplicative inverse modulo `m`), and
`J₂k < (2k)^{90k³}(log N)^{4k²} ((N^{2k-1}/m)+1) N^k` (exponents `90k³`, `4k²`; corrected after review, checked against the PDF text).
The paper’s introduction (pp. 3–4) discusses its bounds for incomplete and bilinear Kloosterman sums over general moduli, extending the authors’ prime-modulus work; it states the standard complete-sum consequence for incomplete sums as `m^{1/2+o(1)}` when `N<m`, and explains that Korolev treats very short lengths `N=m^{o(1)}`. These are exponential-sum bounds, not a theorem directly bounding the inverse-square occupancy `N(q,w)`.

**Assessment:** Relevant to smooth/composite-modulus reciprocal energies and Kloosterman methods, but no all-`w` short-box theorem for `s t²≡w` is stated. It does not justify transferring prime-field sum-product estimates to arbitrary squarefree composite `q`.

### I. Shparlinski, “Modular Hyperbolas,” Japan. J. Math. 7 (2012), 289–333. arXiv:1103.2879v4. Archived `arxiv-1103.2879-shparlinski-modular-hyperbolas.pdf`; SHA-256 `17862f2f8d9af6cf3f19122d5fe3de8a70b6684230e1757084143aac0aef8524`.

Defines the modular hyperbola `H_{a,m}: xy≡a (mod m)`. **Theorem 13, p. 13** (with its displayed consequence (10)): for `X={U+1,…,U+X}`, `m>X≥1`, and for each `x∈X` an interval `Y_x={V_x+1,…,V_x+Y}`, `m>Y≥1`, arbitrary nonnegative shifts, and `(a,m)=1`,
`# {(x,y)∈H_{a,m}: x∈X, y∈Y_x} = φ(m)XY/m² + O(m^{1/2+o(1)})`.
In particular for a rectangular translated box, same formula. The discussion immediately after (10), p. 14, explicitly notes it is not nontrivial for `XY<m^{3/2}` and calls improving that range apparently out of reach. The survey also reviews bounds for individual points/coordinates and composite moduli.

**Assessment:** It provides an average-size asymptotic for sufficiently large boxes, not useful as an upper bound in the small-origin regime `Yt₀≪q^{3/2}`; the origin lifting method is much stronger there. The formula’s main term for composite `m` is `φ(m)XY/m²`.

### M. Z. Garaev, “On the logarithmic factor in error term estimates in certain additive congruence problems,” arXiv:math/0504280v1. Archived `arxiv-math0504280-garaev-log-factor.pdf`; SHA-256 `397eac372dd9b965a4152e35c14d3cf5f5d80458e13d425a7c0e0d0c64179534`.

This concerns error terms for additive congruence counts and logarithmic factors; it is not an inverse-square small-box theorem. It is relevant background for congruence counts but no cited result here improves the origin lifting bound for `s t²≡w`.

### I. E. Shparlinski, “On small solutions to quadratic congruences,” (author corrected after review; earlier misattributed to Heath-Brown) arXiv:1004.0715v1. Archived `arxiv-1004.0715-shparlinski-small-quadratic.pdf`; SHA-256 `489bcc3810f8b86958a92ab7eff414d95d8ad90e9fe5e1a3ed1e526896031631`.

**Theorem 1, p. 2**: for odd `q≥1` and positive integers `M,N≤q`, `Σ_{c=1}^q Δ(M,N;q,c)² ≤ (M+N)² q^{o(1)}`, where `Δ` is the discrepancy in the number of solutions to `m²−n²≡c (mod q)` in the specified short ranges (defined in the paper). Thus this is a mean-square-over-residue-class result for a quadratic congruence, not an individual bound on the number of roots of `s t²≡w`; averaging and the exact definition of the discrepancy matter.

**Assessment:** Genuine evidence for average-in-the-residue-class control of small quadratic congruence counts. It does not give the requested individual all-`w` bound or an average over moduli for inverse squares.

## Other requested literature (bibliographic pointers; not archived here)

“Not archived” means not downloaded as an additional PDF for this task; arXiv availability is noted where known. These citations are useful background, but should not be mistaken for statements verified here against a local PDF.

- J. Cilleruelo and A. Zumalacárregui, work on the number of solutions to `xy≡a (mod m)` / modular hyperbolas and divisors in short intervals; consult also the references in Shparlinski’s survey. No distinct theorem verified here that treats `xy²` in short boxes.
- T. H. Chan and I. Shparlinski, “On the concentration of points on modular hyperbolas and exponential curves,” *Bull. Lond. Math. Soc.* 42 (2010), 773–784. Uses Bourgain sum-product methods for translated boxes and exponential curves; improved by Cilleruelo–Garaev Theorem 1 above. No `xy²` theorem is inferred from it.
- I. D. Shkredov, work on modular hyperbolas and sum-product applications to inverses (including bounds on additive energies/sumsets of inverses). These are additive-structure results, distinct from a uniform small-box count for `w t^{-2}`.
- A. A. Karatsuba, “New estimates of short Kloosterman sums,” *Mat. Zametki* 54 (1993), and related papers on prime and composite moduli; M. A. Korolev, “Short Kloosterman sums with weights,” *Mat. Notes* 78 (2005), and related papers on Karatsuba’s method / short sums with inverses. For especially short lengths (typically `q^ε` or `q^{o(1)}` subject to hypotheses on modulus/coefficients), these estimate exponential sums, not the pointwise inverse-square occupancy by themselves. Bourgain–Garaev 1309.1124 cites these as antecedents. Full theorem constants/ranges should be checked in the individual papers before relying on a sharper claim.
- D. R. Heath-Brown, “Almost-primes in arithmetic progressions and short intervals,” *Math. Proc. Cambridge Philos. Soc.* 83 (1977), 357–375; foundational divisor/short-interval method used by Cilleruelo–Garaev. Its relevant method is reflected explicitly in their proof, but it is not a general `xy²` translated-box theorem.
- D. R. Heath-Brown, “Arithmetic applications of Kloosterman sums,” *Nieuw Arch. Wisk.* (4) 8 (1990), 25–38; arithmetic applications of Kloosterman estimates, not a direct uniform count for this `N(q,w)`.
- M. Z. Garaev, “On the logarithmic factor in error term estimates in certain additive congruence problems,” *Acta Arith.* 107 (2003), 1–18 (arXiv:math/0504280; archived above).
- A. Kerr and A. Shparlinski, work on bilinear forms with Kloosterman sums; J. Bettin and C. D. J. Chandler [Bettin–Chandee], “Trilinear forms with Kloosterman fractions,” *Adv. Math.* 328 (2018), 1231–1269, arXiv:1502.00769 (already archived at `../bettin-chandee-1502.00769.pdf`); W. Duke, J. B. Friedlander, and H. Iwaniec, “Bilinear forms with Kloosterman fractions,” *Invent. Math.* 128 (1997), 23–43 (already archived at `../dfi-1997-kloosterman-fractions.pdf`). These are deep bilinear/trilinear exponential-sum tools; application to a count requires a suitable completion/weight decomposition and does not immediately yield all-`w` power savings for this box.

## Bottom line: answers to Q1–Q3

**Q1 (pointwise, all `w`).** Put `q≥2`, `(w,q)=1`, and `1≤s≤Y`, `1≤t≤t₀`. Every solution gives an integer `n=s t²≡w (mod q)` with `n≤Yt₀²`; there are at most `⌊Yt₀²/q⌋+1` possible positive integers `n`. For each such `n`, `t²|n` and `s=n/t²`, so
`N(q,w) ≤ (⌊Yt₀²/q⌋+1) max_{n≤Yt₀²} τ(n) = (Yt₀²/q+1)(Yt₀²)^{o(1)}`.
If `s` is restricted to squarefree integers, each `n` has at most one decomposition `n=s t²` with `s` squarefree, giving `N≤⌊Yt₀²/q⌋+1` exactly. This elementary bound is uniform in `w`, needs no primality or squarefreeness of `q`, and for `t₀≈q^{1/2}` becomes `≪(Y+1)q^{o(1)}` (or `≤Y+1` in the squarefree-`s` case). (Review correction: the squarefree-uniqueness argument does NOT extend to `st≡w`; squarefree s makes `st²` unique, not `st`. For `st≡w` only the divisor version `≤(Yt₀/q+1)max τ(n)` holds.) These are origin-box bounds.

For arbitrary translated boxes in the `xy≡λ (mod p)` problem, Cilleruelo–Garaev Theorem 1 above gives `M^{4/3+o(1)}p^{-1/3}+M^{o(1)}` (diagonal improvement stated there); it is for prime `p`, equal side lengths, and arbitrary shifts. No corresponding `xy²` theorem or direct composite-modulus extension is stated in the verified papers. Shparlinski Theorem 13 gives only the `φ(q)XY/q²+O(q^{1/2+o(1)})` asymptotic for arbitrary-modulus translated boxes.

Averages are simpler and exact: averaging over unit classes `w∈(Z/qZ)^×`, `Σ_w N(q,w)` equals the number of pairs `(s,t)` in the ranges with both `s,t` units modulo `q`. Hence
`(1/φ(q))Σ_w N(q,w) = (#s≤Y:(s,q)=1)(#t≤t₀:(t,q)=1)/φ(q)`.
For prime `p` this is exactly `(Y−⌊Y/p⌋)(t₀−⌊t₀/p⌋)/(p−1)`; when `Y,t₀<p`, it is `Yt₀/(p−1)`. For `st≡w`, replace `(s,t)` condition by the same unit-pair count (the same average). This average is much smaller than a worst-case count when `Yt₀≪q`; it is not a pointwise guarantee. No particular average-over-q dyadic theorem for `N(q,w)` was verified in the cited sources; any such assertion needs a specified weighting and range.

**Q2.** Yes: at the origin there is already a direct all-`w` saving from lifting, not a need to force a short-Kloosterman estimate. For `t₀≈q^{1/2}`, it gives `N≪(Y+1)q^{o(1)}`; thus when `Y=q^ε` this is `q^{ε+o(1)}`, a power saving against the trivial `min(t₀,2^{ω(q)}Y)` whenever that trivial bound is larger. It does not promise a saving if the trivial bound is itself `O(Y)` (for example, `2^{ω(q)}Y≤Yq^{o(1)}`), and for unrestricted nonsquarefree `s` the divisor factor is essential. For translated boxes and arbitrary target residues, the prime-modulus Cilleruelo–Garaev result is the strongest directly verified concentration theorem here; the reciprocal sum-product and Korolev/Karatsuba short-Kloosterman results are not plug-and-play pointwise estimates for this `N`.

**Q3.** The lifting observation is immediate from integer representatives and the divisor bound, but the cited papers do not appear to state this exact `s t²≡w` origin-box lemma in the requested form. Cilleruelo–Garaev’s proof explicitly uses Heath-Brown’s idea and short-interval divisor estimates (their §2, pp. 4–5); their theorem is for translated `xy`, not this repeated-variable origin box. Shparlinski’s survey Theorem 13 is a Fourier/Kloosterman translated-box asymptotic and explicitly notes its `XY≳q^{3/2}` limitation, not the lifting argument. Heath-Brown’s quadratic-congruence paper provides a mean-square theorem over residues, not this lemma. Thus cite the elementary proof as an observation, not as a published named theorem.


**Review addendum (2026-10-04).** Cilleruelo–Garaev Theorem 2 (`xyz≡λ (mod p)`, all variables in one interval of length `M≪p^{1/8}`, bound `M^{o(1)}`) does imply the same bound for `st²≡λ` when s,t lie in that common interval (inject `(s,t)↦(s,t,t)`). Its prime modulus and tiny range still do not cover IS.
