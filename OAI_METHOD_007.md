# OAI_METHOD_007 — ordinary two-point cancellation versus a large fixed slope

**Assessment, z48 / oai007, 2026-10-28. Verdict: PARTIAL; promise for the fixed-p H-B hatch: 1/5.**

**ES remains OPEN.** Family 007 claims a genuinely stronger ordinary-average theorem than logarithmic two-point Chowla. Its useful new machinery is a weighted, centered divisibility graph with quantitative finite-residue comparison and a coefficient-independent *combinatorial* forest code. Neither the latter uniformity nor the absolute logarithmic exponent is a density-relative estimate on a progression of modulus comparable to the input.

**CONDITIONAL on the quantitative proof of OAI-007:** the special prime-slope family admits the following modest strengthening of the stated black box, with absolute constants C,c>0:

\[
 \left|\sum_{n\le X}\lambda(4pn+1)\lambda(n)\right|
 \le \min\left(\lfloor X\rfloor,\frac{CpX}{(\log X)^c}\right)
 \quad(p\text{ odd prime},\ X\ge3).                                      \tag{U}
\]

Section 4 proves this by tracking the source proof, including its thresholds. Thus the special implied constant can be taken **O(p)**, not an unspecified function of p. This gives simultaneous cancellation for p≤(log X)^(c−ε), but is trivial for X=p^θ, every fixed θ>0, and for X=(log p)^B. It supplies no estimate for the tied-modulus divisor count. This is the strongest explicit coefficient-dependent estimate established in this audit, not a claim of optimality for all adaptations of the method.

## 1. Sources and status

**CERTIFIED (source inspection only).** The source checkout is `/home/pasky/projects/math/oai-math`, commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`. The primary manuscript is:

`preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf`.

Below, `Q/` abbreviates that directory's `build/quantitative/`; `E/` abbreviates `build/qualitative/`. The PDF has quantitative §§2–9, qualitative §§10–17, and affine §18. The audit reads the full quantitative TeX proof, the qualitative setup, analytic transfer, affine consequences, and the seven-page `reasoning_traces/ordinary-two-point-correlations.pdf`; it does not independently referee every qualitative trace lemma. The reasoning summary describes attempted repairs and ends with explicit qualifications about the required witness, forest, finite-law, and spectral bounds. It is provenance, not an additional proof.

**CERTIFIED (source inspection only).** `lean/docs/007.md` links two comparator endpoints. `ComparatorChallenges/OrdinaryTwoPointCorrelations.json` selects `OAI.NumberTheory.TwoPointCorrelations.FinalMain`; its three theorems forward to `TwoPoint/Main.lean`. They assert the stated affine Liouville saving and qualitative shifted/affine Elliott limits without extra hypotheses at the final endpoint. `TwoPoint/Statements.lean` explicitly orders the quantifiers as ∃c>0, ∀coefficients, ∃C>0, ∀X≥3. The general functions are genuinely multiplicative, not required to be completely multiplicative. Comparator templates' `sorry` bodies are not the solution modules.

**Assessment (verification limit).** Neither `lake` nor `lean` is on PATH. No compilation, kernel/axiom audit, or complete definition-equivalence audit is claimed here. The earlier lexical inventory in `OAI_DUMP_IMPACT.md` is not such a check either. All analytic consequences attributed to the release, including (U), are **CONDITIONAL on OAI-007**, an unrefereed claim; elementary deductions and exact identities below are marked PROVED. No OAI-003 hypothesis is used.

**CERTIFIED (campaign reading).** The required `z48briefs/CONTEXT.md`, `FRONTIER.md`, `BREADTH_Z45.md`, the public research map with its arithmetic/covers supplements, and `OAI_DUMP_IMPACT.md` were read. The requested `FRONTIER/PARITY_AUDIT.md` does not exist in this checkout; the relevant file is top-level `PARITY_AUDIT.md`, read here. Its repaired distinction between a bound for R−M and a single-box Weil benchmark is retained.

## 2. Exactly what is claimed

### 2.1 Quantitative Liouville

**CONDITIONAL on OAI-007, Theorem 1.1.** For fixed integers a₁,a₂≥1, b₁,b₂≥0, a₁b₂−a₂b₁≠0,

\[
 \sum_{n\le X}\lambda(a_1n+b_1)\lambda(a_2n+b_2)
   \ll_{a_1,a_2,b_1,b_2}X(\log X)^{-c},\qquad X\ge3,
\]

with one absolute c>0, all real cutoffs, and no coprimality restrictions. The paper explicitly says the constants need not be effective and asserts no growing-coefficient uniformity. Its proof chooses

\[
 \delta=1/200,\quad A\ge1000,\quad W\ge10,\quad
 c=\frac{\delta}{6WA}.
\]

A must dominate the fixed-depth bounded-independence exponent; W is chosen after the graph constant C₃ so that e⁵C₃/√W≤e⁻¹. No usable numerical value of c is supplied. This is a logarithmic saving, **not** a power saving X^(1−ε), and it holds at every scale rather than outside an exceptional set of scales.

**CONDITIONAL on OAI-007, Proposition 2.1.** The intermediate estimate is

\[
 F_{h,l,b}(Y):=Y^{-1}\sum_{m\le Y}1_{m\equiv b\ (l)}
                    \lambda(m)\lambda(m+h)
       \ll_{h,l}(\log Y)^{-c}.                                  \tag{2.1}
\]

Here h,l≥1 are fixed and b is any residue, including zero or a nonunit. The normalization is **Y**, not Y/l. Independence of the representative b follows by taking a maximum over the l residues, not by supplying a growing-modulus estimate.

### 2.2 Corrected Elliott

**CONDITIONAL on OAI-007, Theorem 1.2 and Corollary 1.3.** Let f₁,f₂:N→C be multiplicative and |fᵢ|≤1. At least one original factor must satisfy, for every fixed Dirichlet character χ,

\[
 \inf_{|t|\le N}\sum_{q\le N,\ q\ \mathrm{prime}}
 \frac{1-\Re(f(q)\overline{\chi(q)q^{it}})}q\longrightarrow\infty.
                                                                    \tag{2.2}
\]

Then ordinary two-point shifted and nonproportional affine correlations are o(N), also after any fixed progression restriction. The prime cutoff and twist-height bound are the **same N**. The character is fixed before taking the limit; equivalently one can minimize over any fixed finite family of characters. This is not uniformity in conductors up to N. Merely excluding each one fixed twist χn^(it) is insufficient. Complex values and zeros are allowed; conjugation of a factor gives the conjugated formulation. No rate is asserted.

**CONDITIONAL on OAI-007, §18.3.** Liouville satisfies the exact condition with lower bound D≥¼√log log N−Oχ(1). Since μ(q)=λ(q) at primes, Möbius and mixed μ–λ correlations inherit the qualitative conclusion. The displayed quantitative theorem is only for λ–λ.

**Assessment of the example g.** For fixed p and fixed 1-bounded multiplicative g, the theorem gives Σ_{n≤X}λ(4pn+1)g(n)=o_p,g(X). It does not give a rate uniform over a p-dependent family g_p. For unrestricted bounded g there cannot be any such statement: choosing g(n)=λ(4pn+1) gives exactly ⌊X⌋. Divisor weights are neither unrestricted admissible test weights nor automatically multiplicative functions of n.

## 3. Method: what supplies the new step

All proof descriptions in this section are **Assessment of the claimed OAI-007 proof**, with displayed estimates **CONDITIONAL on its lemmas**. They are not independent certification of the claimed breakthrough.

### 3.1 Comparison with the predecessors

Tao's entropy decrement obtains useful approximate independence at a selected scale; logarithmic averaging is compatible with multiplicative dilations across scales. Matomäki–Radziwiłł controls most short means, and Matomäki–Radziwiłł–Tao (MRT) controls averaged short exponential sums and correlations averaged over shifts. Neither input by itself supplies one fixed shift at each terminal scale. Tao–Teräväinen's almost-all-scale conclusion likewise leaves exceptional scales. The paper's closest technical ancestors are **Helfgott–Radziwiłł's divisibility expansion and Pilatte's composite centered-step/nonbacktracking machinery**, not a new version of entropy decrement alone.

The claimed advance is to recover ordinary terminal-scale bias from a large supply of dilations **in narrow multiplicative bins**, while paying the cost of all bins by padding anti-concentration. Signed singleton cancellation survives deletions via jointly present witnesses, and a universal forest code controls low-rank repeated-prime patterns. Quantitative finite-residue comparison allows the graph to grow with the original cutoff rather than taking that cutoff to infinity first.

### 3.2 Quantitative construction, with the relevant budgets

1. **Dilate without losing the terminal scale** (`Q/01-setup.tex`, PDF §2). At ambient cutoff Y put L=(log Y)^(1/A), J=⌊δ log L/(6W)⌋, η=e^(−J), K=e^(4J). There are J disjoint prime supplies Pᵢ, each of harmonic mass Vᵢ∈[W,2W], with primes between exp(L^.995) and exp L. They use primes ≡1 mod 5 and omit primes dividing lh. A tuple d takes one prime from each supply; d≤e^(2L). The disjoint padding supply Q uses the other primes, with u(q)=4^ω(q) on squarefree products and vertex weight w(n)=5^ω_Q(n). Its harmonic mass is S=∏_{q∈Q}(1+4/q).

2. **Keep a large reciprocal mass near the same original cutoff.** Restrict ω(q)≤100 log L, log(dq)≤100L, and bin log(dq) in intervals of width η. There are O(L/η) bins, with total mass S₀≥SV*/2, V*=∏Vᵢ≥W^J. The raw divisibility term in the centered bin sum becomes, on writing n=qdm,

   \[
    \frac{u(q)}{qd}F_{h,l,b}(T_j/(qd)),\quad
    Ye^{-\eta}<T_j/(qd)\le Y.
   \]

   Bounded summands give F(T_j/(qd))=F(Y)+O(η+Y⁻¹). This is the ordinary-average bridge: it does not replace the desired terminal average by an average of widely separated scales.

3. **Center and delete with controlled cost** (`Q/03-analytic.tex`, PDF §4). Each tuple prime contributes (1_{q|n}−1/q). MRT's input is

   \[
   \sup_\alpha\int_0^Z\left|\sum_{x\le n\le x+H}
       \lambda(n)e(\alpha n)\right|dx
   \ll HZ\left(\frac{\log\log H}{\log H}+(\log Z)^{-1/700}\right).
   \]

   The supremum stays **outside** the integral. A rough-shift multiplier B(α)=Σ_{z∈Z}e(hzα)/z satisfies ‖B‖∞≪L^−.99 and ∫|B|⁴≪D⁻¹L^−3.96 for Z⊂[D,2D) rough at e^(L^.99), D≥½e^(L^.995). A frequency split gives rough-shift correlation O_h(L^−21/20). Summing bins and centered subsets costs η⁻¹2^J L^−1/20 after normalization. Under the tilted padding law, the collision probability of two padding logarithms in a bin is O_{h,l}(1/L). Cutting bin mass at K/L and cutting large degrees therefore costs O_{h,l}(2^J(K⁻¹+L⁻100+e^(−2WJ))). The essential 1/L cancels the L in the number of bins.

4. **Replace the huge joint CRT period by bounded independence** (`Q/02-finite-law.tex`, Lemma 3.1). The period of all selected primes is much larger than the averaging interval. Only residue tests described by fixed-depth circuits are needed: depth≤20, size≤exp(L⁶). Encode each residue with randomized binary digits; CRT makes each t-bit marginal close to uniform. Subtract its low-degree Fourier coefficients and add a small constant to preserve nonnegativity, obtaining an exactly t-wise independent law. Braverman's theorem then compares the circuit expectations to independent residues with error e^(−L¹⁰). Signed scalar expansions cost at most exp(O(L⁵)). This is finite-scale transfer, not a claim that all arithmetic data are independent.

5. **Control the centered graph** (`Q/04-paths-trace.tex` through `06-forest.tex`, PDF §§5–7). On blocks of length M=⌈e^(103L)⌉, edges have displacement hqd and normalized weight Lu(q)/√(w(n)w(n+hqd)), with progression and endpoint cutoffs. The nonbacktracking operator H forbids adjacent repetition of the whole tuple d. For k=⌊L⌋ the target is

   \[
      \mathbb E\|H^k\|_{HS}^2\le[K(C_2\sqrt W)^J]^{2k}.          \tag{3.1}
   \]

   The trace uses signed integration **before** absolute values. Many unlit occurrences supply extra inverse primes. High rank supplies independent divisibility savings without assuming a real nonsingular matrix stays invertible modulo the primes. Many singletons force a common hybrid residue configuration containing positive deletion witnesses; private labels and triangular elimination yield independent savings. The remainder has few unlit occurrences, few singletons, and low rank. Quotienting out the exceptional span gives independent line directions; their incidence graph is a forest. Nonbacktracking segments are recovered from their endpoints, giving exp(O(Jk)) patterns uniformly over all numerical padding coefficients. Padding is summed afterward in one common residue environment with cost K^(2k). **This forest is a graph of trace-word incidences, not the ES certificate forest F_p.**

6. **Test the operator and close** (`Q/07-spectral.tex`, PDF §8). A noncommuting self-adjoint transfer lemma converts the nonbacktracking moment into an adjacency norm. Test against √w λ, average overlapping blocks, then sum bins. The final normalized estimate is

   \[
   |F(Y)|\ll_{h,l,W}\eta+\eta^{-1}2^JL^{-1/20}
   +2^J(K^{-1}+L^{-100}+e^{-2WJ})
   +\frac K\eta(C_3/\sqrt W)^J+e^{-L^{.9}}+Y^{-1}.              \tag{3.2}
   \]

   W is fixed sufficiently large after C₃; every term is O(e^−J), which is O((log Y)^−c). No scale is discarded.

### 3.3 Qualitative proof and why it does not secretly provide a rate

`E/graph-setup.tex` and `analytic-transfer.tex` fix an auxiliary B first. Core primes satisfy B^(1−η₀)<log q≤B, center primes B^(1−ε₀)<log q≤B^(1−η₀), with ε₀=10⁻⁴ and η₀=ε₀/100. Core weight A₀ is a very large fixed constant; center weight is one. Vertex normalization is (1+A₀)^ω_C(n)2^ω_Z(n), so the center factor is **1_{q|n}−1/(4q)**, not a mean-zero factor in isolation. The two endpoint normalizers make the leading singleton terms cancel in the trace.

A persistent bias γ produces raw mass ≫γ L₀/B in one short multiplier interval. The graph gives O(L₀B^(−1−c*/2)), c*=10⁻⁶, while analytic centering costs O(L₀(B^(−1−ε₀)+J/P₀)). First take the long average with **all B-data fixed**, then increase B. Finite changes to prime values cost at most 2Σ_{q∈S}1/q in squared pretentious distance. Consequently MRT applies uniformly over the finite-prime twists for fixed B, but (2.2) supplies no rate as B or character conductors grow. This order of limits is essential, not a quantitative assertion in disguise.

## 4. Coefficient dependence: exact accounting and a uniform deduction

### 4.1 The exact affine conversion

**PROVED (complete multiplicativity).** Put l=a₁a₂, b=min(a₂b₁,a₁b₂), h=|a₁b₂−a₂b₁|. With P_{h,l,b}(Y)=YF_{h,l,b}(Y),

\[
 \sum_{n\le X}\lambda(a_1n+b_1)\lambda(a_2n+b_2)
 =\lambda(l)[P_{h,l,b}(lX+b)-P_{h,l,b}(b)].                    \tag{4.1}
\]

This holds for real X as written. Thus a progression constant C_prog and threshold Y₀ yield an eventual affine constant bounded by

\[
 C_{\rm prog}(l+b/3)+|P_{h,l,b}(b)|\sup_{X\ge3}\frac{(\log X)^c}{X},
\]

once lX+b≥Y₀; extending over earlier X additionally costs a power of the logarithm of that threshold. The constants C_prog(h,l), Y₀(h,l) are not evaluated in the manuscript.

**CERTIFIED (Lean source).** `TwoPoint/QuantitativeAffineTransfer.lean:130–187` makes this same dependency explicit with the slightly looser eventual constant

`C * (l + b) * 2^c + d`, where `d = ‖residuePrefix u l b b‖`.

Its `real_log_saving_extend` at lines 95–128 adds `(log(max(B,3)))^c + 1`, with B an existential eventual threshold. There is no polynomial coefficient bound in that formal endpoint. The local source inspection independently confirmed these formulas; they were checked again against the file here.

**PROVED (specialization).** For λ(4pn+1)λ(n), the determinant is −1, not of size p:

\[
 h=1,\quad l=4p,\quad b=0,\qquad
 S_p(X)=\lambda(4p)P_{1,4p,0}(4pX).                            \tag{4.2}
\]

There is no initial endpoint term. Even an absolute ambient estimate |P(Y)|≤CY/log^cY becomes |S_p(X)|≤4CpX/log^c(4pX). This loses a factor 4p against the actual number X of sampled terms.

### 4.2 Where each hidden dependence enters

**Assessment (source audit).** The following table distinguishes real losses from merely fixed-parameter wording.

| Step | Displayed dependence | Consequence for h=1,l=4p,b=0 |
|---|---|---|
| §2 prime supplies | Remove prime divisors of lh; fixed-data PNT threshold | Only 2 and p are removed. Their theta contribution is ≤log 2+log x, uniformly in p; no growing-conductor PNT is used (the analytic modulus is 5). |
| Lemma 3.1 finite law | Decoding error 2^(1−B)(l+Σq), B=⌈L¹⁵⌉; CRT marginal error ≤l exp(tL)/N | The printed simplifications absorb fixed l. They are uniformly valid for l≤e^L. For l a power of the ambient cutoff the printed simplifications are not valid. |
| Lemma 4.4 short Fourier bound | Additive progression expansion has total coefficient norm 1; constants O_h | This part is uniform in l and b. It does **not** yield an extra factor 1/l. |
| Proof of Lemma 4.1 | Split rough z into up to l residue classes to make bz mod l constant | Potential O(l) loss in general. **Absent here:** b=0 makes every bz equal to zero; do not charge p for this step. |
| Lemma 4.5 padding | O_{h,l}(1) in the prime harmonic integral after deleting factors of lh | Uniform here: removing 2,p costs ≤2(1/2+1/p) in the oscillatory reciprocal-prime sum. |
| §§5–7 trace | Congruence coefficients involve h; progression restrictions are nonnegative and independent of P-residue draws | h=1, so coefficient-size bounds are absolute. l only remains in the finite-law comparison. The forest code counts the union over numerical coefficients, not arithmetic progression densities. |
| §7.4 trace completion | Explicitly **drop progression restrictions** in the positive majorant | The resulting operator bound has no density 1/l. |
| §8.3 testing | Average test-vector squared norm ≤2MS, not 2MS/l | Gives a bin error on the ambient population, not relative to the sparse progression. |
| §9 affine transfer | Multiply ambient cutoff by l=a₁a₂ | Exact factor 4p in (4.2). |

### 4.3 A uniform prime-slope estimate extracted from the method

**PROVED implication, CONDITIONAL on the estimates proved in OAI-007 §§2–8.** There are absolute C,c>0 such that (U) holds. The following supplies the uniform-threshold argument; it is not inferred just from the words “absolute exponent.”

**Step 1: uniform nontrivial ambient regime.** Let L=(log Y)^(1/A) and assume 4p≤e^L. Keep exactly the manuscript's absolute choices of A,W. All sufficiently-large-L thresholds can be chosen independently of p in this special family:

* The fixed-modulus-5 PNT and all prime-mass estimates stay uniform after removing 2,p: at x≥2 the removed theta mass is O(log x). The centered primes start at exp(L^.995), so removal from a band has vanishing reciprocal mass uniformly in p.
* Every padding product upper bound can only decrease under removing primes. The needed lower bound on the oscillatory prime sum loses an absolute constant, since only 2,p are removed. Hence the anti-concentration and deletion constants are absolute.
* In Lemma 3.1, l≤e^L gives `l+Σq≤exp(3L)` for large absolute L. For t=⌈L^C₁⌉ the CRT product is at most exp((t+1)L); with N≥exp(L^A/2) this is within the printed exp(2tL−L^A/2) error. The bit count, Fourier correction, circuit sizes, and scalar-expansion budgets are unchanged. Thus the lemma has an absolute threshold in this range.
* Lemma 4.4 uses a Fourier expansion of norm one; h=1 is fixed. In Lemma 4.1 skip splitting z modulo l, because b=0. All z already have the same required residue. The remaining split has at most two dyadic pieces. Its centering constant is therefore absolute.
* The exceptional-word enumeration, rank, singleton, and universal forest bounds use absolute constants when h=1. Restrictions modulo l remain predicates independent of the centered-prime residue draws; they do not change any pattern count and are ultimately dropped. The finite-origin comparison is now uniform by the preceding bullet. The block-boundary error has R_L=e^(100L+1), with no p factor.

Consequently (3.2) holds with an absolute implied constant and an absolute threshold for **h=1,b=0, l=4p≤e^L**, and

\[
 |P_{1,4p,0}(Y)|\le C Y(\log Y)^{-c}.                         \tag{4.3}
\]

This uses the claimed combinatorial lemmas as inputs; it does not newly verify those lemmas' correctness.

**Step 2: extend the ambient bound to every p.** If 4p>e^L, the zero-class trivial bound is

\[
 Y^{-1}|P_{1,4p,0}(Y)|\le\frac{\lfloor Y/(4p)\rfloor}{Y}
 \le\frac1{4p}<e^{-L}\ll L^{-\delta/(6W)}=(\log Y)^{-c}.
\]

The remaining bounded range Y≥3 below the absolute threshold is absorbed into an absolute C using |P(Y)|≤Y. Thus (4.3) holds **simultaneously for all odd primes p and all Y≥3**. In the large-modulus range it says less than the trivial bound; that is deliberate, not hidden cancellation.

**Step 3: return to the sampled length.** Apply (4.3) at Y=4pX in (4.2), use log(4pX)≥log X, and combine with |S_p(X)|≤⌊X⌋. This proves (U), with the factor 4 incorporated into C. In particular the special affine constant is O(p) at **all X≥3**, not just beyond an unspecified p-dependent threshold. ∎

**CONDITIONAL corollary.** For any fixed 0<ε<c,

\[
 \sup_{p\le(\log X)^{c-\varepsilon}}\frac{|S_p(X)|}{X}
       \ll(\log X)^{-\varepsilon}\longrightarrow0.
\]

Equivalently one can force a small relative error at a fixed p by taking log X≫(p/error)^(1/c). This is a vastly longer average than any ES search permits. A nonquantitative finite-maximum/diagonal uniformity could already be deduced from the fixed-form theorem; (U) is stronger because it specifies O(p) and a logarithmic coefficient range. No numerical effective value for its absolute constants is asserted.

### 4.4 What fails on the requested scales

**PROVED (comparison of scales).** At X=p^θ with θ>0 fixed, the bound in (U) divided by X is min(1, O_θ(p/(log p)^c))=1 for sufficiently large p. At X=(log p)^B it is likewise trivial. Thus this adaptation proves **no o(X) bound, fixed fractional saving, or other nontrivial relative cancellation** in those regimes. It is not a proof that such bounds are false.

**Assessment (exact blocking step).** The decisive loss is not a large determinant, a Siegel zero, or the two excluded primes. It is replacing a density-relative statement by an ambient operator bound: §4.3 drops the progression indicator in deletion costs, §7.4 explicitly drops it from the trace majorant, and §8.3 tests with an ambient norm. Equation (4.2) then multiplies that ambient error by l when measured per sampled n. A saving which is only a power of log Y cannot absorb l≈p. Fixing the finite-law threshold alone does not repair this.

**Assessment (finite-law obstruction is narrower).** For X=p^θ and Y=4pX, the printed bit decoding and the simplification of `l exp(tL)/N` in Lemma 3.1 fail at its stated absolute parameters. But the underlying CRT error is approximately exp(tL)/X; since tL=o(log Y), it still tends to zero for fixed θ. A more economical encoding of the large residue coordinate might repair this part. It would not produce the missing factor 1/l in the spectral bound. At polylogarithmic X, exp(tL)/X is already far too large with the paper's parameters based on Y, so even the finite-residue comparison needs new scales or a different argument. These are limitations of the displayed proof, not impossibility theorems about all possible graph methods.

**Assessment (why simply condition on the progression is insufficient).** For b=0 the original vertices lie in n≡0 mod 4p, but an edge ends at n+hqd with (qd,4p)=1 and h=1. The graph does not preserve that progression. Conditioning all vertices into it destroys the very edges whose spectral expansion is used. A new conditional/bipartite estimate must control both the sparse starting side and its differently distributed endpoints. Restricting a test vector and using Cauchy–Schwarz generally only supplies a square root of a density, which still costs a power of p after rescaling. No relative graph estimate is proved in 007.

## 5. Why even a stronger two-point estimate is not R(p)

### 5.1 Exact class detector and the weight mismatch

**PROVED (character orthogonality).** Since gcd(4Cp+1,4C)=1,

\[
 D_C(p):=\#\{d\mid4Cp+1:d\equiv-1\ (4C)\}
 =\frac1{\varphi(4C)}\sum_{\chi\bmod4C}\overline{\chi(-1)}
       (1*\chi)(4Cp+1),\qquad R(p)=\sum_C D_C(p).              \tag{5.1}
\]

For each fixed χ, 1*χ is a multiplicative divisor convolution, generally unbounded. Here the character itself varies with C and the modulus is tied to the index. There are not two fixed 1-bounded multiplicative functions on two fixed forms. Normalizing by τ(4Cp+1), truncating τ, or inserting an arbitrary mask does not make the resulting C-sequence a permitted multiplicative factor, nor preserve the count with an acceptable error.

**PROVED (range).** If d=4Cu−1 and its cofactor is 4Cv−1, then p=4Cuv−u−v. Its minimum over positive u,v is 4C−2 (increasing either variable increases the expression). Hence every contributing C satisfies C≤(p+2)/4. Taking X to the enormous range where (U) becomes nontrivial is not an allowed amplification of R(p): the new levels are empty of these certificates.

**PROVED (parity is not the class).** Even at level C=1 and primes ≡1 mod 4, equal total Liouville signs can coexist with opposite class outcomes: 4·13+1=53 has λ=−1 and no divisor ≡3 mod 4; 4·41+1=165=3·5·11 also has λ=−1 and has such divisors. More generally λ(N) sees total Ω(N), not which subset of the factor multiset occupies −1 modulo 4C. Two-point λ cancellation does not identify the missing character contributions in (5.1).

### 5.2 The required precision

**Assessment using the campaign's PROVED reduction.** The relevant lower bound is one-sided R(p)≥εM_BM(p), with M_BM(p)≫log²p and M_BM vanishing at odd squares. A uniform two-sided polylog error is false infinitely often by the Linnik construction; no such target is proposed here. The current pointwise |R−M|≪p^(2/5+o(1)) from `PARITY_AUDIT.md` is a divisor bound, not cancellation. The single-box Weil p^(1/2+o(1)) benchmark is not a bound for the full tied-modulus sum.

Even a hypothetical coefficient-uniform O(X/log^cX) correlation at X=p^θ would be much larger than log²p. It cannot simply be substituted as an absolute error in (5.1). A genuine reduction might normalize, exploit sparsity, or count a different family, but it must prove its own total error below the negative lower-tail budget. The present proof does none of this. At polylog X a logarithmic saving could be interesting for a correctly weighted sparse detector; no such detector or transfer is supplied here.

### 5.3 What remains usable, and what does not

**Assessment.** The genuinely reusable idea is **joint witness control before absolute values**: an apparent singleton cancellation can be destroyed by deleting bad vertices, so one proves that a nonzero mixed difference forces several witnesses simultaneously in the same residue environment. The universal forest code avoids counting padding choices separately before summing their weights. These are potential design principles for a new class-aware incidence argument.

They are not presently such an argument. The graph's prime supplies are chosen freely, its averages run over many integer origins, and its CRT comparison controls limited-complexity tests of selected small primes. R(p) needs the actual divisor factor multiset of each 4pC+1, including large factors and the changing modulus. Encoding the full detector as a circuit would require its precise depth, size, modulus, and signed-error budget to satisfy the finite-law lemma; none is demonstrated. “Bounded independence fools circuits” is not a theorem that it fools arbitrary factorization predicates at one prescribed integer.

The graph estimate does allow arbitrary bounded **vertex test functions once the specific centered graph and its edge weights are fixed**. This is not arbitrary-weight cancellation in the original affine correlation. Multiplicativity and MRT enter the raw-to-centered transfer, and a C-dependent divisor-class weight need not survive that transfer. Confusing these two uses of “arbitrary test functions” would incorrectly claim a divisor-weighted theorem.

## 6. H-B verdict and adversarial screens

**Assessment.** 007 does not reopen the fixed-p H-B hatch with an established input. It improves ordinary two-point parity on free averages, not the tied-modulus event. The fair correction to an overly broad “missing sequence variable” objection is that **C really is a free summation variable at fixed p**. The trouble is its large coefficient, the density-relative precision, and the modulus 4C moving with C—not the absence of any variable whatsoever.

| Screen | Assessment of a proposed 007→ES inference |
|---|---|
| T1 / odd squares | The same λ correlation machinery applies with coefficient 4m². Yet the Type II divisor count at n=m² is zero. A λ estimate alone supplies no square-sensitive lower bound. The BM/Jacobi factor must remain in a new detector. |
| Numerator 8 | The affine method is not 4-specific and could be used for 8pC+1 as well. It has no step excluding the certified 8/11, 8/17, 8/131, 8/241 controls. Any transport claiming unconditional three-term existence would fail this test. |
| Keep p fixed | The derivation of (U) keeps p fixed or takes a supremum over p; there is no average over p. Almost-all-p replacements would be a different result. |
| Coefficients | h=1 helps; l=4p is the actual cost. The uniform deduction is nontrivial only at enormous C-lengths outside the certificate box. |
| Moving target | Characters in (5.1) change with C; 007 has no such weight theorem. |
| Scale / one-sidedness | X/log^cX at power X is not a log²p lower-tail error. No false two-sided asymptotic for R is asserted. |
| Fixed menus / large factors | No finite slice menu, CRT menu, or collision of private large primes is promoted to a witness. The graph's controlled primes are not forced to supply the actual divisor class. |
| Existing counterexamples | R(409)=R(577)=0, although ES holds. No claim of positivity at every prime or every fixed level is made. An eventual R theorem would need a threshold past all restricted-line failures. |

**Assessment: promise 1/5 for ES; method worth retaining, not a live proof route.** The new content of this audit is (U), its proof-level coefficient accounting, the identification of the missing progression-density factor, and the distinction between repairable finite-law thresholds and the real sparse-target loss. It is not progress on the lower bound for R(p).

## 7. Next steps and stopping criteria

1. **Assessment — prerequisite:** independently execute the 007 comparator and audit the semantic definitions and crucial graph lemmas, especially the common-hybrid witness elimination, coefficient-independent forest code, and finite-law comparison. The reasoning summary itself singles these out as obligations. A successful source-level transfer audit is not verification of the claimed Chowla breakthrough.
2. **Assessment — focused analytic experiment:** seek a *density-relative* version of the centered-graph testing/deletion estimates for h=1, b=0, l=4p, preserving p throughout. State the target as |P_{1,4p,0}(4pX)|≤ε(X)X, not ε(X)·4pX. First test X=p^θ. Merely re-encoding the large modulus in Lemma 3.1 is insufficient; a result losing √p is also insufficient for a logarithmic saving.
3. **Assessment — separate transfer obligation:** only after that, specify a class-aware bounded/truncated model for (5.1), quantify its discarded mass at a single p, and prove a one-sided error below log²p. This is a stronger and different task from two-point Chowla. Do not call an assumption giving that error “a consequence of 007.”
4. **Assessment — stop condition:** without a new density-relative estimate or an exact divisor-weight transfer, park the H-B proposal. OAI-003, even if separately assumed, improves character nonpretentiousness and BM main terms but does not restore either missing factor or the tied class.

**Validation record.** Primary TeX labels and PDF theorem numbers were cross-checked; the affine identity and both cases in the proof of (U) were checked algebraically. A separate fresh-context deep reviewer inspected all eight quantitative TeX files, challenged the uniform-threshold deduction and the density-loss diagnosis, and found no substantive defect; its one TeX control-character finding was repaired. This is review of the conditional extraction, not independent verification of OAI-007's underlying graph theorems. No numerical experiment would establish the asserted analytic uniformity, so none is substituted for the proof. This deliverable changes only this document; the release and campaign source files remain untouched.
