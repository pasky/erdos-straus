# LOWERTAIL_DEEP_ASTRA — fixed-prime character kernels and the lower tail

**Status: PARTIAL / NEGATIVE for the proposed mechanism. Assessment: promise 1/5 as an ES proof route.**
**ES remains open. No implication GRH ⇒ ES, or OAI-003 ⇒ ES, is established here.**

This is one focused attempt at the fixed-prime lower tail, not a survey of other ES approaches. The successive objects are the same certificate indicator: a local character minorant, its genus quotient, a compressed positive square, the dual large sieve, and finally a kernel coupling the different moduli. The attempt produces elementary, scoped obstruction lemmas, a precise sufficient **nonstandard** moment hypothesis, and a conditional positive result: **any fixed zero-free strip gives M_gen(p)≥(2/π⁴−o(1))log²p** (§5.4). It does not produce the required lower bound for the actual certificate count.

Labels: **PROVED** means a proof is supplied below, or an explicitly named existing result is used; **CONDITIONAL** names its hypothesis; **CERTIFIED** refers only to the specified finite computations; **EVIDENCE** is numerical extrapolation; **Assessment** is a judgement. No literature-priority claim is made for the elementary Fourier lemmas.

## 1. Target and normalization

**PROVED / existing definitions.** For a prime p ≡ 1 (mod 4), use the ordered count

\[
 R(p)=\#\{(u,v,C)\in\mathbb N^3:4uvC-u-v=p\}.
\]

Use a second line, with its own multiplicity convention,

\[
 B(p)=\#\{(x,y,C):p=4xyC-4x-y,\quad y\ge3\text{ odd}\},\qquad T(p)=R(p)+B(p).
\]

This is a **sum of certificate counts**, not the cardinality of a disjoint union of rational solutions. Duplicates are harmless for positivity. R is ordered and even; B counts each pair (4x,y) once. The formulas are

\[
 (u,v,C)\longmapsto(uvC,pvC,puC),
\]
\[
 (x,y,C)\longmapsto\bigl(x(Cy-1),\ pCx,\ pCx(Cy-1)\bigr).
\]

For the second formula, the sum of reciprocals is
\((p+y)/(px(Cy-1))=4/p\). All denominators are positive. The omitted y=1 case would give p ≡ 3 (mod 4), so loses nothing here. At primes all the relevant pair coordinates are coprime and smaller than p.

**Assessment / target choice.** The 14 known R-zeros do not logically refute *eventual* positivity of R; they are finite exceptions. Nevertheless I use T throughout the final sufficient condition, rather than asking a single line to do everything. The two-line choice also makes the requested numerical controls meaningful.

Let M denote **the existing star-line BM main term**, not a newly asserted asymptotic main term for T:

\[
 M(p)=\sum_{\mathcal P(p)}\frac{1-\chi_{-4uv}(p)}{\varphi(4uv)},
\quad
 \mathcal P(p)=\{(u,v):(u,v)=1,\ u+v\text{ odd},\ 4uv-u-v\le p\}.
\]

**PROVED / imported:** `BM_CORRECTED_COUNT.md`, Theorem 2.2, gives

\[
 (3/(16\pi^2)-o(1))\log^2p\le M(p)\ll\log^2p.
\]

The weaker PV constant 1/(32π²) would suffice. Thus the target

\[
                 T(p)\ge\varepsilon M(p)                         \tag{LT}
\]

for every sufficiently large prime p ≡ 1 (mod 4) implies eventual ES. No GRH assumption is needed for this implication.

**CONDITIONAL on OAI-003 (quasi-RH 7/8):** the deduction in `OAI_DUMP_IMPACT.md` §3.3 gives \(M(p)\sim3\log^2p/(2\pi^2)\). This is an improvement to M, **not** to T. The same distinction holds under GRH.

### 1.1 A necessary correction to the proposed non-real-character target

**PROVED / exact bookkeeping.** With q=4uv, a=−u−v, G=(ℤ/q)×, and s=|G/G²|,

\[
 1[p=a\pmod q]=\frac1{\varphi(q)}\sum_{\psi\in\widehat G}\psi(p)\overline{\psi(a)}.
\]

Removing only 1 and χ_{−4uv} leaves **other real characters as well as non-real characters**. The exclusively non-real remainder is instead

\[
 R=M_{\rm gen}+X_{\rm nr},\quad
 M_{\rm gen}=\sum_{\mathcal P(p)}\frac{s(q)}{\varphi(q)}1[pa^{-1}\in G^2],
\]
\[
 X_{\rm nr}=\sum_{\mathcal P(p)}\frac1{\varphi(q)}
       \sum_{\psi^2\ne1}\psi(p)\overline{\psi(a)}.                \tag{1}
\]

For B the same expansion uses a=−4x−y, q=4xy and its finite pair domain. Let \(M_{\rm gen}^T\) be the sum of the two genus contributions. Then \(T=M_{\rm gen}^T+X_{\rm nr}^T\) exactly.

**Assessment.** A theorem controlling only \(X_{\rm nr}^T\) relative to M is not automatically enough: the remaining real contribution must also be accounted for. Conversely a relative lower bound against \(M_{\rm gen}^T\), together with its divergence, would suffice for positivity. The previously available OAI-003/GRH lower bound for the star genus term is only of log-log size. Section 5.4 below supplies a separate fixed-strip proof of a log-square genus lower bound; this is **not** obtained by silently substituting the BM main term.

## 2. First attempt: optimize a local Fourier minorant

The starting hope was to replace the full orthogonality sum by a positive or Beurling–Selberg-type kernel with a cheaper character expansion, retain a positive main term, and control only its negative remainder at p.

### Theorem 2.1 — sharp Fourier budget of a point minorant

**PROVED.** Let G be a finite abelian group of order h, a∈G, and F:G→ℝ satisfy F≤1_{a}. Normalize

\[
 \widehat F(\eta)=h^{-1}\sum_{g\in G}F(g)\overline{\eta(g)},\qquad
 \mu=\widehat F(1).
\]

If μ>0, then for **every** character η,

\[
 \left|\frac1h-\eta(a)\widehat F(\eta)\right|\le\frac1h-\mu,
 \qquad
 \Re\bigl(\eta(a)\widehat F(\eta)\bigr)\ge\mu.                 \tag{2}
\]

Consequently:

1. Every Fourier coefficient is nonzero; indeed \(|\widehat F(\eta)|\ge\mu\).
2. \(\sum_\eta|\widehat F(\eta)|/\mu\ge h\).
3. Equality in item 2 occurs only for \(F=h\mu\,1_a\).
4. If even **one** Fourier frequency is omitted, then μ≤0.

*Proof.* Put H=1_a−F≥0. Its mean is 1/h−μ and

\[
 \widehat H(\eta)=\overline{\eta(a)}/h-\widehat F(\eta),\qquad
 |\widehat H(\eta)|\le\widehat H(1).
\]

This proves the disk inequality, hence the real-part inequality. Summing the modulus bound proves item 2. Equality forces all the phase-adjusted coefficients to equal μ, and Fourier inversion gives item 3. Item 4 follows immediately. ∎

**Assessment / relationship to prior work.** `SINGLE_P_COUNT.md` Lemma 5.2 excludes pointwise-positive minorants whose frequencies lie in a proper subgroup of the dual. The statement here concerns **positive average**, and applies to any omitted frequency, even if the retained frequencies generate the entire dual group. It is not a claim that such a minorant is everywhere nonpositive. For example on C₄, F(j)=cos(πj/2) is a minorant of 1_{0}, positive at 0, with mean zero and Fourier support generating the dual.

### Corollary 2.2 — BM and genus restriction do not remove the budget

**PROVED.** In a BM-allowed pair put H=ker χ_{−4uv}; after translating by a, p/a belongs to H. A positive-average minorant on this allowed coset must use all |H|=φ(q)/2 quotient frequencies and has Fourier ℓ¹/mean ratio at least φ(q)/2.

After conditioning on **all** genus characters, H=G² and the corresponding bound is

\[
                         |H|=\varphi(q)/s(q).                    \tag{3}
\]

*Proof.* Apply Theorem 2.1 to the restricted function on H. Characters of H are restrictions of characters of G, with two extensions identified in the BM case and s(q) in the genus case. All real characters of G restrict trivially to G², but its other frequencies are still required. ∎

**Assessment.** This precisely locates the loss. The QNR detector (1−χ)/2 has fixed-density support. A certificate detector is a singleton *inside* that allowed support. Conditioning correctly handles T1 but does not turn the singleton into a fixed-density target.

### Proposition 2.3 — weighting a certificate locally does not flatten its spectrum

**PROVED.** For any function w:G→ℝ,

\[
                         w(g)1_a(g)=w(a)1_a(g).
\]

Thus a termwise nonnegative weighting depending only on that pair's residue cannot alter the flat absolute Fourier coefficients of its certificate indicator. Multiplying by the BM or genus projector leaves the indicator unchanged. A nonnegative pointwise minorant is simply c1_a, 0≤c≤1.

**Scope.** This does not cover weights depending on p through other moduli, or inequalities valid only after summing pairs. Those are the global attempt in §6. Nor does Theorem 2.1 forbid a *compressed nonlinear representation* of a full-spectrum kernel; §3 checks that loophole explicitly.

### 2.4 A concrete hard-prime cell

**PROVED and CERTIFIED.** At p=409, the pair (u,v)=(1,14) has

\[
 q=56,\quad a=41,\quad G^2=\{1,9,25\},\quad pa^{-1}=25.
\]

It is genus-allowed, contributes 1/3 to M_gen, and is not a certificate. On this C₃ the full restricted-character sum is

\[
                       1+\omega+\omega^2=0.
\]

The two ordered pairs contribute 2/3 to the genus main term and −2/3 to the non-real remainder. Moreover the **same cell** is a nonhit for every prime p≡73 (mod 168), an infinite set by Dirichlet. This is a counterexample to any per-cell rule “large prime + genus permission + zero-free L-functions forces the target”, not to the growing all-pairs target.

## 3. Second attempt: compressed positive squares, not frequency truncation

A full Fourier support need not require h separately estimated amplitudes. This is a real loophole in an overbroad reading of §2, so it was tested rather than dismissed.

### Proposition 3.1 — the pedestal cost

**PROVED.** Let S⊂Ĝ have J elements and

\[
 K(g)=\left|\sum_{\eta\in S}b_\eta\eta(g)\right|^2,\qquad K(e)=1.
\]

Write A=E_G K=Σ|b_η|² and c=max_{g≠e}K(g). For h>1,

\[
 A\ge1/J,\qquad
 c\ge\frac{hA-1}{h-1}\ge\frac{h/J-1}{h-1}.                    \tag{4}
\]

If c<1, then F=(K−c)/(1−c)≤1_e. If the difference set S S^{-1} misses a character, Theorem 2.1 gives E F≤0.

*Proof.* Cauchy–Schwarz at e gives 1≤JΣ|b|². Also hA=1+Σ_{g≠e}K(g)≤1+(h−1)c. The minorant and its Fourier support follow directly. ∎

**Assessment.** A J≈√h amplitude representation can carry a background of order 1/J while the desired singleton mean is only 1/h. It has not removed that background by being positive. After its necessary subtraction, a lower-bound proof must resolve a signal smaller by roughly √h. This is a budget calculation, not an impossibility theorem for special cross-modulus cancellation.

### 3.2 Exact difference-set experiment

**PROVED by the displayed finite difference identity; CERTIFIED independently.** On C₂₁ take

\[
                         S=\{0,1,4,14,16\}.
\]

Every nonzero residue occurs exactly once among s−t, s≠t. Hence, for z²¹=1,

\[
            |1+z+z^4+z^{14}+z^{16}|^2=4+21\,1[z=1].           \tag{5}
\]

Five amplitudes have generated all 21 frequencies. This saturates the pedestal bound: after subtracting 4 and dividing by 21, one recovers the **exact** point indicator.

There is an actual ES cell of this shape at the same hard prime:

\[
 p=409,\ (u,v)=(1,86),\ q=344,\ a=257,\quad |G^2|=21,
\]
\[
 pa^{-1}=193=9^{18}\pmod{344},\qquad 9\text{ generates }G^2.
\]

At this nonhit the squared amplitude in (5) is exactly 4. The positive square supplies precisely the pedestal and no excess.

**Assessment / outcome.** This experiment prevents the false conclusion “all frequencies ⇒ no compressed positive kernel exists.” Such kernels do exist. What has not been supplied is a lower bound for their sum **strictly above the sum of their pedestals** at the given prime. For a difference-set kernel that excess is identically the certificate count. Merely renaming it a positive quadratic form adds no inequality.

### 3.3 Power-projector hierarchy

**PROVED.** For any positive integer k define

\[
 K_{k,q}(p,a)=\frac1{\varphi(q)}\sum_{\psi^k=1}\psi(p)\overline{\psi(a)}
 =\frac1{|G^k|}1[pa^{-1}\in G^k].                              \tag{6}
\]

These are nonnegative kernels; k=2 gives the genus term. If k divides l the support shrinks, but the height on surviving points increases. Thus K_l is **not** a lower approximation to K_k or to the certificate indicator. Once k is divisible by the group exponent it is the exact indicator, not a new estimate.

**CERTIFIED / floating sums, exact support tests.** For the complete pair domains at the following small R-zeros (all q≤65,536), the sums of (6) are:

| p | R | k=2 | k=6 | k=12 | k=60 |
|---:|---:|---:|---:|---:|---:|
| 409 | 0 | 3.999068 | 2.051160 | 1.908303 | 1.108303 |
| 577 | 0 | 5.352387 | 2.361927 | 1.088118 | 1.088118 |
| 5569 | 0 | 6.240721 | 5.964787 | 5.325052 | 5.470757 |
| 9601 | 0 | 7.926241 | 5.845152 | 5.008648 | 4.925921 |

The increase from k=12 to k=60 at 5569 is a useful check against a mistaken monotonicity argument. Exact rational image-set enumeration independently checks the k=2,6,12,60 values at 193,409,577. The same bounded-modulus kernels were evaluated at all 114 selected inputs, including the 14 R-zeros and eight odd squares.

## 4. Third attempt: use the large sieve in the dual direction

### Theorem 4.1 — the exact one-point norm

**PROVED.** Let \(\{\psi_j\}\) be any finite indexed family of characters, all nonzero at p, and let w_j>0. Then

\[
 \sup_{c\ne0}\frac{|\sum_j\sqrt{w_j}c_j\psi_j(p)|^2}{\sum_j|c_j|^2}
                         =\sum_jw_j.                           \tag{7}
\]

*Proof.* Cauchy–Schwarz gives the upper bound; take \(c_j=\sqrt{w_j}\overline{\psi_j(p)}\) for equality. ∎

**PROVED / consequence for a generic dual-large-sieve argument.** The one-point evaluation operator is rank one. Primality of p and a zero-free strip do not reduce its norm. In the usual multiplicative large sieve, taking the integer sequence to be the single atom at p makes

\[
 \sum_{q\le Q}\frac q{\varphi(q)}\sum_{\psi\bmod q}^{*}|\psi(p)|^2
\]

a positive diagonal sum, not an oscillatory character sum. For instance q=8ℓ with ℓ an odd prime contributes 2(ℓ−2) primitive characters. Summing such q in a dyadic band already gives \(\gg Q^2/\log Q\) characters. Thus even this subfamily retains the Q² exponent in the large-sieve constant.

**Scope.** The maximizing coefficients in (7) are not claimed to be the ES coefficients. Equation (7) rules out an improvement based only on the family and an unrestricted coefficient norm. It does **not** rule out exploiting the exact coefficients \(\overline{\psi(-u-v)}\).

### Proposition 4.2 — the modulus family is not sparse

**PROVED.** Every multiple q=8j≤p occurs in the star pair family: take (u,v)=(1,2j), for which the onset is 6j−1≤p. In fact this works through q≤4(p+1)/3.

**Assessment.** “Structured moduli 4uv” is useful multiplicative structure, but not sparsity of the *set of moduli*. A sparse-moduli large sieve cannot be invoked merely from that notation.

### Proposition 4.3 — what the direct weighted Cauchy bound measures

**PROVED.** At a prime p, applying Cauchy to (1), with one index for each pair and character and weight 1/φ(q), yields

\[
 |X_{\rm nr}(p)|\le D(p),\qquad
 D(p)=\sum_{\mathcal P(p)}\frac{\varphi(q)-s(q)}{\varphi(q)}.    \tag{8}
\]

Both vector norms squared are D(p); the same bound applies to the negative real part. In contrast, local orthogonality and nonnegativity give the sharper but tautological lower bound \(X_{\rm nr}\ge-M_{\rm gen}\).

**CERTIFIED / numerical diagnostic.** At 409, D=225.622314 and M_gen=3.999068. At an R-zero the negative correlation measured against these norms is only −M_gen/D, not anything close to −1. The larger hard-prime values are in `detail.csv`.

### 4.4 A zero count is not a large character bias

**PROVED.** On any allowed group H of order h and any g≠e,

\[
 \sum_{\eta\ne1}\eta(g)=-1,
 \qquad \frac1{h-1}\sum_{\eta\ne1}\eta(g)=-\frac1{h-1}.        \tag{9}
\]

Furthermore, η(g), as η ranges uniformly over Ĥ, is uniform on the ord(g)-th roots of unity. Its moments of orders 1,…,ord(g)−1 vanish exactly.

*Proof.* Character orthogonality and the surjective evaluation homomorphism \(\widehat H\to\mu_{\operatorname{ord}(g)}\). ∎

**Assessment / failed inverse step.** A nonhit can have perfect cancellation in every low character moment. The bias that cancels its singleton main term is only 1/(h−1). Therefore “if the lower tail fails, many characters must be unusually aligned, so a zero-density/Siegel theorem detects them” does not follow. In the standard Hilbert norm the deficit is tiny, not a near-extremizer to which an inverse large-sieve theorem automatically applies.

### 4.5 Same-modulus packets do not restore a fixed-density target

**PROVED.** Fix an even m and include all coprime splittings uv=m. There are \(2^{\omega(m)-1}\) unordered splittings. Their sums u+v are distinct and lie strictly between 0 and 4m, so they give that many distinct target classes modulo 4m. Every class has ordered multiplicity two.

For any set A⊂G and F≤1_A with positive mean μ,

\[
       \frac{\sum_\eta|\widehat F(\eta)|}{\mu}\ge\frac{|G|}{|A|}.\tag{10}
\]

*Proof of (10).* Off A, F≤0. Hence |G|μ≤Σ_{a∈A}F(a)≤|A|‖F‖∞, and Fourier inversion gives ‖F‖∞≤Σ|F̂|. Distinctness of sums follows from uniqueness of the two roots of X²−(u+v)X+m. ∎

Thus the packet detector still has a Fourier budget at least

\[
 \frac{\varphi(4m)}{2^{\omega(m)-1}}=m^{1-o(1)}.
\]

Adding the second line contributes at most another \(2^{\omega(m)}\) classes at the same modulus. The bound changes by a constant factor, not a power. For genuine overlapping target sets use the set cardinality in (10); this avoids assuming disjointness of the two lines.

**Assessment.** This does not exclude a structured packet estimate using more than its Fourier ℓ¹ norm. It excludes the hope that grouping a few unitary-divisor targets makes the free-prime detector fixed-density.

## 5. Fourth attempt: use OAI-003 or GRH to control the fixed argument

### 5.1 The useful consequences, kept conditional

**CONDITIONAL on OAI-003 (quasi-RH 7/8).** As derived in `OAI_DUMP_IMPACT.md`, fixed-density quadratic patterns have a detected prime of size O(log⁸Q), the least QNR is O(log⁸p), and M has its full log-square asymptotic. A separate uniform Siegel exclusion is unnecessary once the fixed numerical strip is assumed.

For a detector f=Σc_χχ of positive mean δ and Fourier cost B=Σ|c_χ|, the smoothed explicit-formula mechanism has the sufficient scale

\[
                    x^{1-\theta}\gg (B/\delta)\log Q.          \tag{11}
\]

Here θ=7/8 for OAI-003 and θ=1/2 for GRH. This is a theorem about a **free auxiliary prime**, averaged up to x, not about a prime p already fixed by the problem.

**PROVED / application of §2 to this mechanism.** A singleton minorant, even after genus conditioning, has B/δ≥|G²|. Inserting a smooth minorant cannot remove that density cost from (11). Moreover (11) still would not force the prime obtained to divide a prescribed side integer.

### Proposition 5.2 — a zero-free strip alone is insensitive to a local Euler phase

**PROVED, with deliberately limited scope.** Fix a Dirichlet character χ, a prime p not dividing its conductor, and any z with |z|=1. The modified Euler product

\[
 L_z(s)=L(s,\chi)\frac{1-\chi(p)p^{-s}}{1-zp^{-s}}
\]

has exactly the same zeros and poles as L(s,χ) in Re s>0. In particular it has the same zero-free strip there, although the coefficient at the prime p is z instead of χ(p).

*Proof.* Both extra factors are holomorphic and nonzero in Re s>0, since |p^{−s}|<1. ∎

**Scope / warning.** L_z is generally **not a Dirichlet L-function** and does not retain its functional equation. This is not a counterexample to “GRH implies ES,” and not a logical independence result. It shows only why a proposed deduction using nonvanishing alone must identify an additional arithmetic input before it can control the Euler coefficient at one prescribed prime. The omitted periodicity/functional-equation information cannot be assumed to do the missing work without an argument.

### 5.3 Trying to isolate p in the explicit formula

**PROVED bookkeeping, conditional on a strip for the explicit-formula estimate.** To isolate Λ(p)χ(p), take a smooth weight supported in (p−Δ,p+Δ), Δ<1/2, equal to 1 at p. Its Mellin transform has typical size \(\Delta p^{\sigma-1}\) and effective height \(T\asymp p/\Delta\). Bounding its zero sum term by term with Re ρ≤θ and the usual zero count gives an error of scale at most

\[
                         O(p^\theta\log(qp/\Delta)),            \tag{12}
\]

rather than an error smaller than log p. Indeed the \(\Delta p^{\theta-1}\) transform size is multiplied by roughly \((p/\Delta)\log(qp/\Delta)\) zeros; smooth decay controls the remaining tail. This is a bound delivered by that method, not a lower bound on the true error.

**Assessment / exact missing step.** Averaging these zero sums with the ES character coefficients might conceivably improve (12). Neither GRH nor the zero-free strip asserts the required *signed correlation of zeros with those coefficients at this p*. Calling the character average “dual” does not supply such a correlation. No such theorem was proved in this attempt.

### 5.4 A genuine conditional gain: the full genus main term is log-square

The prime-only genus witnesses leave a log-log lower bound. Passing to **squarefree products** permits a two-L-function Euler product. This does not estimate the non-real remainder, but it upgrades the correctly defined main term in (1).

### Theorem 5.4 — a fixed zero-free strip gives a log-square genus lower bound

**CONDITIONAL on H_θ; PROVED implication.** Assume that for some fixed 1/2≤θ<1, every primitive nonprincipal Dirichlet L-function is zero-free in Re s>θ. Then, as p tends to infinity through primes p≡1 (mod 4),

\[
             M_{\rm gen}(p)\ge\left(\frac{2}{\pi^4}-o(1)\right)\log^2p.
                                                               \tag{G}
\]

In particular OAI-003 with θ=7/8, or GRH, suffices. This is a theorem about **M_gen, not R or T**. The proof uses only a fixed strip; it does not assume conductor-aspect Lindelöf throughout the critical strip.

#### Step A: the limited uniform L-bound actually needed

**CONDITIONAL on H_θ.** Put κ=(1−θ)/8 and σ₀=1−κ. For fixed A,K and q≤p^A,

\[
       L(\sigma_0+it,\chi)=p^{o(1)}\qquad (|t|\le K\log p)    \tag{18}
\]

uniformly in nonprincipal characters modulo q. Principal characters satisfy the same upper bound on this line.

*Proof.* The standard explicit formula under H_θ gives

\[
 \sum_{\ell\le x}\chi(\ell)\log\ell
                       \ll_\theta x^\theta\log^2(qx)
\]

for nonprincipal χ; passing from prime powers to primes costs no larger order. Imprimitive characters add only omitted ramified Euler factors. Hence the prime series for log L converges for Re s>θ. Split it at

\[
                  Y=(\log p)^{4/(1-\theta)}.
\]

The initial segment is bounded absolutely by O(Y^{1−σ₀})=O(√log p). Partial summation bounds the tail by

\[
 O\bigl((1+|t|)Y^{\theta-\sigma_0}\log^2(qY)\bigr)
                         =O((\log p)^{-1/2})
\]

in the stated height range. Prime powers of exponent at least two contribute O_θ(1), since σ₀>1/2. Thus log|L|=O_{θ,A,K}(√log p), which proves (18). For a principal character use ζ(s) times its omitted Euler factors; ζ on this fixed line has polynomial height growth and the omitted factors are q^{o(1)}. ∎

For Mellin integrals below, the tails |t|>K log p are negligible: Γ(s) decays exponentially and ordinary polynomial bounds for Dirichlet L-functions suffice, with K chosen large enough. Thus no unsupported all-height uniformity is hidden in (18).

#### Step B: an exactly genus-allowed multiplicative subfamily

Choose fixed positive exponents

\[
 0<\alpha_0<\alpha_1,\qquad 0<\beta<\gamma,\qquad\alpha_1+\gamma<1.
\]

Take squarefree u≡1 (mod 4) in U₀=p^{α₀}<u≤U₁=p^{α₁}, and odd squarefree w coprime to pu. Use the two ordered pairs (u,2w) and (2w,u). Put D=−4up, a negative fundamental discriminant. Their genus permission is **exactly**:

\[
 \chi_D(\ell)=+1\quad(\ell\mid w),\qquad
 (w/\ell)=(-2p/\ell)\quad(\ell\mid u),\qquad
 \chi_{-4}(w)=-\chi_8(pu).                                  \tag{19}
\]

Indeed the odd-prime conditions are p/(−u−2w) square at each prime dividing uw. The 2-adic condition is p+u+2w≡0 (mod 8), giving the last equality. The genus weight of the **two ordered pairs** is

\[
                         \frac{2\,2^{\omega(u)+\omega(w)}}{\varphi(u)\varphi(w)}.
\]

The conditions on w modulo 4u form one quadratic-sign coset. Its indicator has the expansion

\[
 \frac1{2^{\omega(u)+1}}\sum_{\eta^2=1\bmod4u}\epsilon_\eta\eta(w),
 \qquad \epsilon_1=1,\quad |\epsilon_\eta|=1.                  \tag{20}
\]

All these statements are exact; no random-sign assumption enters.

#### Step C: the Euler product and its sole pole

For η in (20), let

\[
 B_{u,\eta}(s)=
 \sum_{\substack{w\ge1\ \mathrm{squarefree}\\
                 \chi_D(\ell)=1\ (\ell\mid w)}}
        \frac{2^{\omega(w)}w}{\varphi(w)}\frac{\eta(w)}{w^s}.
\]

The split-prime condition automatically excludes primes dividing 2up. Direct multiplication of local factors gives

\[
 B_{u,\eta}(s)=L(s,\eta)L(s,\eta\chi_D)H_{u,\eta}(s),          \tag{21}
\]

where H is holomorphic and uniformly bounded on each half-plane Re s≥1/2+ε. At a split unramified prime ℓ its factor is

\[
 \left(1+\frac{2\ell}{\ell-1}\eta(\ell)\ell^{-s}\right)
                 (1-\eta(\ell)\ell^{-s})^2,
\]

and at an inert prime it is 1−η(ℓ)²ℓ^{-2s}. These are 1+O(ℓ^{-1−Re s}+ℓ^{-2Re s}); the ramified factor at p is 1−η(p)p^{-s}, and primes dividing 2u contribute 1.

**Crucial prime-input fact:** ηχ_D is never principal, because its conductor retains p whereas η has modulus 4u and p∤4u. Thus only η=1 has a pole at s=1. Its residue is

\[
 A_{u,p}=\frac1{\zeta(2)}\prod_{\ell\mid2up}\frac{\ell}{\ell+1}
                    L(1,\chi_D)
 =\frac4{\pi^2}\frac p{p+1}
       \prod_{\ell\mid u}\frac{\ell}{\ell+1}L(1,\chi_D).       \tag{22}
\]

For clarity, at s=1 both the split and inert unramified H-factors equal 1−ℓ^{-2}; this is why the residue has a uniform positive Euler factor rather than an uncontrolled product of splitting probabilities.

#### Step D: smooth the w-range without losing positivity

Use the nonnegative weight

\[
 f_p(w)=e^{-w/p^\gamma}-e^{-w/p^\beta},\qquad 0\le f_p(w)\le1.
\]

Mellin inversion of (21), shifted from Re s>0 to Re s=−κ, gives uniformly in the chosen u and η

\[
 \sum_{w\ \mathrm{squarefree}}\frac{2^{\omega(w)}}{\varphi(w)}\eta(w)
       1[\chi_D(\ell)=1\ \forall\ell\mid w]f_p(w)
 =1[\eta=1]A_{u,p}(\gamma-\beta)\log p
       +O(p^{-\kappa\beta+o(1)}).                             \tag{23}
\]

Explicitly, the integral before shifting is

\[
 \frac1{2\pi i}\int_{(c)}\Gamma(s)(p^{\gamma s}-p^{\beta s})
                          B_{u,\eta}(1+s)\,ds,\qquad c>0.
\]

The two L-functions in (21) have moduli at most 4up≤4p^{1+α₁}; on the shifted line their real argument is σ₀. The multiplier Γ(s)(p^{γs}−p^{βs}) has value (γ−β)log p at s=0, giving the residue in (23). Estimate (18), the uniform bound on H, and the exponential Γ-tail justify the error. This is a sum over a **free variable w**, where the L-function estimate really does apply—not an attempted estimate of ψ(p) at one point.

Only w≤p/(8u) is needed to ensure the certificate height cutoff. The omitted tail of f_p is exponentially small, uniformly in u, since

\[
 \frac{p/(8u)}{p^\gamma}\ge\tfrac18p^{1-\alpha_1-\gamma}\longrightarrow\infty.
\]

The elementary divisor bounds on 2^{ω(w)}/φ(w) make the total tail negligible. Apply (20) and multiply by the two-pair weight. The factor 2^{ω(u)+1} **cancels** the projector denominator. Summing the errors costs only p^{o(1)}, because Σ_{u≤U₁}2^{ω(u)}/φ(u)=p^{o(1)}. Therefore

\[
 M_{\rm gen}(p)\ge(\gamma-\beta)\log p
                     \sum_u\frac{A_{u,p}}{\varphi(u)}-o(1).   \tag{24}
\]

Since u is squarefree, (22) gives the exact simplification

\[
 \frac{A_{u,p}}{\varphi(u)}
 =\frac4{\pi^2}\frac p{p+1}\frac{L(1,\chi_{-4up})}{u}
                      \prod_{\ell\mid u}(1-\ell^{-2})^{-1}
 \ge\frac4{\pi^2}\frac p{p+1}\frac{L(1,\chi_{-4up})}{u}.      \tag{25}
\]

Here L(1,χ_D)>0, the usual positivity for a real nonprincipal quadratic character.

#### Step E: average L(1), rather than use its worst-case lower bound

Uniformly in these u, another Mellin shift using (18) yields, for any fixed ν>0 and Y=p^ν,

\[
 L(1,\chi_{-4up})=
       \sum_{n\ge1}\frac{\chi_{-4up}(n)}n e^{-n/Y}
                     +O(p^{-\kappa\nu+o(1)}).                \tag{26}
\]

Choose ν<α₀. For odd n,

\[
                 \chi_{-4up}(n)=\chi_{-4p}(n)(u/n).
\]

If n is not a square, elementary periodic cancellation and μ²(u)=Σ_{d²|u}μ(d) give

\[
 \sum_{u\le V\atop u\equiv1\ (4)}\mu^2(u)(u/n)\ll\sqrt{nV}.
\]

To see this without invoking any extra character-sum hypothesis, split d at √(V/n). Each inner sum along 1 (mod 4) has zero complete-period mean and is O(n); the remaining d use the trivial V/d² bound. This also gives the stated bound when n>V. Partial summation then gives

\[
 \sum_{U_0<u\le U_1\atop u\equiv1\ (4)}
          \frac{\mu^2(u)}u(u/n)\ll\sqrt{n/U_0}.               \tag{27}
\]

Summing the nonsquare terms of (26) with (27) costs O(√(Y/U₀))=o(1). All square terms are nonnegative, and the n=1 term alone yields

\[
 \sum_{U_0<u\le U_1\atop \mu^2(u)=1,\ u\equiv1\ (4)}
             \frac{L(1,\chi_{-4up})}{u}
 \ge\left(\frac2{\pi^2}+o(1)\right)\log(U_1/U_0).            \tag{28}
\]

The density 2/π² of squarefree integers in 1 (mod 4) follows directly from the same μ² expansion. The error in (26), summed with 1/u, remains o(1). No distribution assertion about the Euler coefficient at the fixed p has been used.

Combining (24), (25), and (28) proves

\[
 M_{\rm gen}(p)\ge
 \left(\frac8{\pi^4}(\gamma-\beta)(\alpha_1-\alpha_0)-o(1)\right)\log^2p.
\]

Let α₀ and β tend to zero and α₁,γ tend to 1/2 from below, always choosing fixed exponents before taking p→∞. This proves (G). ∎

**T1 audit.** For an odd square input p=m², coprime to u, the character χ_D is induced by η₀=χ_{−4u}, a character modulo 4u. On its split-prime support η₀(w)=1, so B_{u,η₀}=B_{u,1}. But the target signs (19) give

\[
 \epsilon_{\eta_0}=\bigl[-\chi_8(u)\bigr](-2/u)=-1
                         \qquad(u\equiv1\pmod4).
\]

Thus the two contributions cancel, including their equal poles: η₀χ_D now is principal up to omitted Euler factors. The “sole pole” step fails on the square locus exactly where it must. The proof has not manufactured a genus lower bound for squares.

**CERTIFIED identity checks / EVIDENCE for the asymptotic.** `z48_ltastra_genusproof.py` checks (19) and the entire projector (20) against the existing square-unit test, including primes p≡5 (mod 8) and the cancelling character on odd-square controls. It independently checks the normalization L(1,χ_D)=πh(D)/√|D| by reduced binary quadratic forms versus exact character sums. All 106 prime inputs in `detail.csv` satisfy M_gen/log²p≥0.0778293, above 2/π⁴≈0.020532. These samples do not certify an eventual threshold. The recorded small-p smoothed subcounts can be below their pole expressions; no finite-point error constant is asserted.

**What this changes, and what it does not.** Under a fixed strip, a one-sided estimate

\[
 X_{\rm nr}^T(p)\ge-(1-\varepsilon)M_{\rm gen}^T(p)
\]

would now imply the requested log-square lower bound for T using a separately proved main-term bound. The missing estimate is **still this non-real remainder bound**. Equations (23) and (26) average genuinely free multiplicative variables to estimate a quadratic projector; they do not estimate the singleton certificate or its non-real phases. Thus (G) is real conditional progress on the main-term bookkeeping, not a conditional ES proof.

## 6. Fifth attempt: couple the moduli before taking a minorant

The local obstruction does not apply to the Fourier transform of a **sum** of target classes. This is the most important surviving loophole in §§2–5, and was tested exactly.

### Theorem 6.1 — the optimal subgroup-invariant lower envelope

**PROVED.** Let C:G→ℝ be any finite count function and H≤G. Among all H-invariant functions F≤C, the pointwise greatest one is

\[
                         L_H(g)=\min_{h\in H}C(gh).             \tag{13}
\]

The Fourier support of such functions lies in H⊥. In particular the optimal all-real-character minorant of C is the minimum on each square coset, not its average.

*Proof.* Every H-invariant F has F(g)=F(gh)≤C(gh) for all h. The displayed minimum is itself H-invariant and ≤C. The Fourier statement is the standard subgroup orthogonality identity. ∎

**Assessment.** This converts the global positivity proposal into a concrete finite problem. A positive genus average does not solve it. A positive lower envelope does give a valid congruence certificate, and so this test does not prejudge the answer negatively.

### 6.2 Exact experiment

**CERTIFIED.** For each Q in the table, form C_Q=R_Q+B_Q from every pair whose modulus q divides Q. For p>Q all these pairs lie in their admissible domains; hence C_Q(p)≤T(p). Restrict to units r≡1 (mod 24), and group them by their Legendre signs at every prime ℓ≥5 dividing Q. These are exactly the global genus fibres within the restriction.

The C program computes the minimum, mean and maximum of C_Q on each fibre. The Python check independently regenerates the pair menu and checks **every reported zero-envelope residue** against it.

| Q | genus fibres | fibres with min R_Q=0 | fibres with min C_Q=0 | largest mean C_Q in a zero-minimum fibre |
|---:|---:|---:|---:|---:|
| 840 | 4 | 4 | 1 | 0 |
| 120120 | 16 | 16 | 4 | 3.466667 |
| 720720 | 16 | 16 | 4 | 5.173148 |
| 12252240 | 32 | 32 | 8 | 6.646412 |
| 24504480 | 32 | 32 | 8 | 7.051794 |
| 38798760 | 64 | 64 | 16 | 5.527623 |
| 103062960 | 16 | 16 | 4 | 5.241356 |

Additional checked Q: 9240, 1441440, 2042040, 2162160, 3603600, 7927920, 9369360, 36756720, 134774640, 159279120. All raw fibre tables are retained.

**CERTIFIED / scope of the observed pattern.** For every tested Q, the union lower envelope is zero exactly on the fibres with (r/5)=(r/7)=+1. Adding higher primes and higher prime powers raises means but does not remove these zero fibres. This is a finite observation, **not** a theorem for arbitrary Q. The nonzero fibres recover congruence coverage; they are not an all-prime lower-tail advance.

For a concrete non-square genus fibre, Q=120120, r=3361 has negative signs at 11 and 13, positive signs at 5 and 7, zero C_Q, and genus mean 3.466666…. At Q=38798760 a fibre with four negative signs still has a zero minimum and mean 5.527623….

**PROVED consequence of each certified zero residue.** Since gcd(r,Q)=1, Dirichlet supplies infinitely many primes p≡r (mod Q), p>Q, with exactly that genus profile and no certificate from this finite q|Q menu. Thus even *global* quadratic conditioning cannot turn that menu's positive conditional mean into a lower bound on that fibre.

### 6.3 Follow-up: remove the prime-power cutoff from this experiment

**PROVED, computer-assisted using the certified anchors below.** Let S={2,3,5,7,11,13,17,19}. Let Q be **any** multiple of 24 supported on S, with arbitrarily large exponents. For every unit r≡1 (mod 24) whose signs at 5 and 7 are positive, the genus lower envelope of C_Q is zero. The same conclusion holds for any nonnegative weighting or subfamily of these certificate classes.

Consequently, even allowing Q to depend on p and grow arbitrarily fast, a genus-only pointwise minorant using only moduli supported on S cannot be positive on these Mordell-hard inputs. This statement does not cover non-real frequencies or adding primes outside S.

*Proof.* A finite anchor n with no S-smooth-modulus certificate has C_Q(n)=0 for **every** such Q. At either line, the least positive residue a is its onset: q−u−v for R, or q−4x−y for B. These lie strictly between 0 and q. Thus n≡a (mod q), n>0, would give an actual positive certificate at n, not a spurious negative-C congruence. A star certificate at n has q≤4(n+1)/3. A B certificate has q≤3(n+3)/2, since

\[
 \tfrac32\bigl((4xy-4x-y)+3\bigr)-4xy
                    =(y-3)(2x-\tfrac32)\ge0.
\]

So absence of *all* S-smooth certificates at a fixed anchor is a finite check.

The following anchors, all units at S and ≡1 (mod 24), realize every allowed sign pattern. A mask records negative signs at (5,7,11,13,17,19) in bits 0,…,5. No anchor has a certificate on either line with S-smooth modulus.

| mask | anchor n | mask | anchor n |
|---:|---:|---:|---:|
| 0 | 1 | 32 | 59929 |
| 4 | 12601 | 36 | 28921 |
| 8 | 111841 | 40 | 122761 |
| 12 | 57481 | 44 | 243601 |
| 16 | 48049 | 48 | 55969 |
| 20 | 88321 | 52 | 2521 |
| 24 | 36961 | 56 | 184321 |
| 28 | 520801 | 60 | 555601 |

Choose an anchor matching r's signs at primes dividing Q; signs at unused primes can be completed arbitrarily, with the 5 and 7 signs positive. Then r/n is a square unit modulo every prime power dividing Q: the 2-adic condition is equality modulo 8; the odd-prime conditions are equality of Legendre signs. Thus r and n lie in the same square coset modulo Q. Theorem 6.1 gives lower envelope zero. Nonnegative weights still vanish at the same anchor. ∎

**CERTIFIED audit.** `z48_ltastra_anchors.py` first marks every smooth-modulus pair onset through n≤10⁶, with no imposed exponent cap. It then checks the selected anchors by direct smooth-pair divisibility and by the **existing independent** `(u,C)` / ET-line enumerators, rejecting any witness whose modulus is S-smooth. The same search finds star-only anchors for 63 of 64 sign patterns; mask 63 has no anchor in this search and is **not** claimed impossible or covered. The union theorem needs only the 16 displayed patterns, all found.

**Exact remaining possibility.** A growing prime alphabet or a kernel using non-real information across moduli may have a different lower envelope. Neither the finite tables nor the bounded-alphabet theorem excludes it. Proving positivity at each prescribed p remains unfilled; OAI-003's small nonresidue does not do so. In particular, identifying a nonresidue among 11,13,17,19 cannot by itself repair this genus-only construction even when all powers of those primes are allowed.

## 7. A precise sufficient hypothesis, and why it is not a standard one

No clean standard hypothesis was found to supply (LT). The following isolates how much **one-sided**, growing-order information would suffice without confusing a density result with a pointwise theorem.

Fix constants c>0 and C>0. Put L=log X,

\[
 m_X=cL^2,\qquad k_X=\left\lceil\frac{L}{\log L}\right\rceil,
 \qquad D_X(p)=(m_X-T(p))_+.
\]

### Hypothesis H⁻mom(c,C)

**CONJECTURE / nonstandard, not derived from GRH or OAI-003.** For every sufficiently large X,

\[
 \sum_{\substack{X<p\le2X\\p\equiv1\ (4)}}D_X(p)^{2k_X}
 \le \pi(2X)\,(C k_X m_X)^{k_X}.                              \tag{14}
\]

The centre m_X is just a fixed small log-square scale; it need not be the exact mean. One may take c well below the known BM lower-bound constant. The hypothesis is a negative-part sub-Gaussian moment estimate to a specified, growing order. It is **not** an existing named equidistribution conjecture.

### Theorem 7.1 — H⁻mom implies the requested eventual lower bound

**CONDITIONAL on H⁻mom only; PROVED implication.** For every fixed 0<η<1, all sufficiently large primes p≡1 (mod 4) satisfy T(p)≥ηm_X in their dyadic block. Consequently T(p)≥εM(p) for some ε>0, and ES holds for all sufficiently large p≡1 (mod 4).

*Proof.* The number of primes in a block with T(p)<ηm_X is at most

\[
 \pi(2X)\left(\frac{Ck_X}{(1-\eta)^2m_X}\right)^{k_X}.          \tag{15}
\]

The logarithm of the parenthesized factor is

\[
 -\log L-\log\log L+O(1).
\]

Using π(2X)≤2X and k_X=L/log L+O(1), the logarithm of (15) is at most

\[
 -\frac{L\log\log L}{\log L}+O\!\left(\frac L{\log L}\right),
\]

which tends to −∞. Thus (15)<1 eventually. Its integer-valued counting function is then zero. Finally M(p)≪log²p and log p∼L on the block convert this to (LT). ∎

**Assessment / refinement to the weakest leading order of this mechanism.** Orders k=aL/log L give a leading exponent −aL in the Markov factor. A fixed a>1 gives a power margin, but the extra −log log L term shows that **a=1 already suffices**, independently of the fixed constants c,C. This weakens the initial (1+δ)L/log L formulation. Proposition 7.3 shows that no fixed leading constant a<1 suffices on the moment information alone; no claim of an absolutely weakest hypothesis implying ES is made.

### Proposition 7.2 — replacing the negative part by an absolute moment is false

**PROVED relative to the existing Linnik construction.** The analogous bound with |T(p)−m_X| in place of D_X(p), at the orders k_X above, fails infinitely often.

*Proof.* `BM_CORRECTED_COUNT.md` Proposition 3.1 gives an infinite sequence with

\[
 T(p)\ge R(p)\ge\exp(c_1\log p/\log\log p)
\]

for some fixed c₁>0. Take a dyadic X with p∈(X,2X]. The logarithm of this one prime's contribution to the absolute 2k_X moment is

\[
 \gg (\log X)^2/(\log\log X)^2.
\]

The logarithm of the proposed upper bound π(2X)(Ck_Xm_X)^{k_X} is only O(log X). Contradiction for large members of that sequence. ∎

**Assessment / attempted derivation of (14).** Expanding ordinary moments gives correlations of congruence events at products/lcms of many moving moduli. At k≈L/log L, even moduli of a fixed power size produce products of size exp(Θ(L²/log L)); GRH estimates for individual progression sums do not give the required errors. Lcms can be smaller for overlapping events, so this product observation is not an impossibility theorem. It identifies the missing correlation estimate, not a proof of it. Using absolute moments to simplify that estimate is ruled out by Proposition 7.2. Using a bounded number of moments leaves the integer-count bound above 1. No route from a standard zero-free hypothesis to the required negative-part moments was found.

### Proposition 7.3 — sharpness of the leading order for this moment criterion

**PROVED, mechanism scope.** Replace k_X in (14) by ⌈aL/log L⌉ with any fixed 0<a<1. The resulting moment condition, on its own, permits infinitely many zero counts.

*Proof.* Construct an abstract nonnegative integer-valued function on primes. Choose primes p_j≡1 (mod 4) with p_{j+1}>4p_j, set F(p_j)=0, and set F(p)=⌈c(log p)²⌉ at all other primes. A dyadic block contains at most one p_j, and its negative-part moment is at most m_X^{2k_X}. By the PNT,

\[
 \log\frac{\pi(2X)(Ck_Xm_X)^{k_X}}{m_X^{2k_X}}
                         =(1-a)L+o(L)>0
\]

for every fixed C>0 and all sufficiently large X. Thus F obeys the weaker moment condition while having infinitely many zeros. This F is not asserted to be an ES count; the result identifies what the moment inequality itself can exclude. ∎

**EVIDENCE / finite moment calibration, not verification of the hypothesis.** A second census includes all p≡1 (mod 4) through 10⁷. On the 15 complete dyadic blocks X=2⁸,…,2²², take c=0.15 and the critical k_X of (14), and normalize each moment by the number of these primes *in the block*, which is smaller than π(2X). The empirical constants needed in (14) range from 0.00949 to 0.57091; their absolute-moment counterparts range from 8.05965 to 40.65180. On the last block there are 133,975 primes, k=6, m_X=34.88089, and 1,137 positive deficits; the constants are 0.48763 and 40.65180 respectively. This illustrates why a two-sided norm is a poor surrogate. A bounded finite list of fitted constants says nothing about their eventual boundedness, and supplies no standard-conjecture implication.

## 8. Numerical tests of the actual lower-tail target

### Lemma 8.1 — inexpensive upper bounds for checking M

**PROVED.** Let

\[
 U(p)=\frac12\sum_{\substack{m\le(p+1)/3\\2\mid m}}
                  \frac{2^{\omega(m)}}{\varphi(m)}.
\]

Then M(p)≤U(p). Also, for every prime p≥5,

\[
                         M(p)<2(1+\log p)^2.                   \tag{16}
\]

*Proof.* From 4uv−u−v≤p and u+v≤uv+1, one gets uv≤(p+1)/3. For even m there are 2^{ω(m)} coprime ordered splittings, and φ(4m)=4φ(m). Since 1−χ≤2, enlarging to all such splittings gives M≤U.

Alternatively φ(4uv)=4φ(u)φ(v) on the star pair domain, so

\[
 M\le\tfrac12\left(\sum_{n\le p}\frac1{\varphi(n)}\right)^2.
\]

The positive divisor identity

\[
 \frac1{\varphi(n)}=\frac1n\sum_{d\mid n}\frac{\mu^2(d)}{\varphi(d)}
\]

gives \(\sum_{n\le p}1/\varphi(n)\le A(1+\log p)\), with

\[
 A=\sum_d\frac{\mu^2(d)}{d\varphi(d)}
   =\frac{\zeta(2)\zeta(3)}{\zeta(6)}<2.
\]

This proves (16). The bound A<2 follows, for example, from ζ(2)<1.65, ζ(3)<1.21, and ζ(6)>1. ∎

### 8.2 Complete requested census

**CERTIFIED.** The AP-marking census covers **all 82,887 primes p≡1 (mod 24), p≤10⁷**. It counts R and B exactly. It also checks all 1,580 odd squares from 9 through 10⁷, for which both restricted counts vanish.

| prime range | primes | R=0 | B=0 | T=0 | least T/log²p, at p |
|---|---:|---:|---:|---:|---|
| ≤10⁴ | 143 | 4 | 2 | 0 | 0.0237863, 9601 |
| (10⁴,10⁵] | 1038 | 2 | 1 | 0 | 0.0311492, 83449 |
| (10⁵,10⁶] | 8551 | 3 | 0 | 0 | 0.0275315, 712321 |
| (10⁶,10⁷] | 73155 | 5 | 0 | 0 | 0.0379238, 2031121 |

The R-zeros are

```
409 577 5569 9601 23929 83449 102001 329617 712321
1134241 1724209 1726201 5212561 8813281
```

The B-zeros are 193, 2521, 66529.

**CERTIFIED quantitative statement:** throughout this whole prime range,

\[
                       T(p)\ge U(p)/16\ge M(p)/16.              \tag{17}
\]

Here U is computed with **outward-rounded upper bounds**, not an assumed BM asymptotic: each positive rational summand and each addition is rounded upward using `nextafter`. The executable checks IEEE binary64, the evaluation method, and round-to-nearest. The smallest observed T/U_upper is 0.0774393489 at 9601, safely above 1/16. Exact rational sums independently check the upper-bound direction at 193,409,577.

**CERTIFIED extension:** the supplementary census of **all 332,180 primes p≡1 (mod 4), p≤10⁷** gives the same 14 R-zeros, three B-zeros, no T-zero, and the same outward-bound minimum. Thus (17) holds on that larger finite set as well. Its compressed complete table is `census_mod4.csv.gz`.

**Assessment.** Equation (17) is finite verification, not evidence that the constant 1/16 is eventually valid. The upper bound is deliberately loose; no claim about the actual minimum of T/M over the whole range is made.

### 8.3 Hard primes and near-squares beyond the census

**CERTIFIED, using the existing independent segmented divisor engine `scripts/z29_census.c`.** All 17 single-line failure primes are independently reproduced. Its star count is unordered and is multiplied by two when compared with R.

Nine additional primes around 10¹² were counted completely, not searched only to a convenient first-witness cutoff:

| p | R | B | T |
|---:|---:|---:|---:|
| 1000174007593 | 82 | 64 | 146 |
| 1000194009433 | 90 | 75 | 165 |
| 1000354031353 | 148 | 78 | 226 |
| 1000374034993 | 94 | 75 | 169 |
| 1000570081249 | 110 | 80 | 190 |
| 1000650105649 | 88 | 57 | 145 |
| 1000726131793 | 112 | 73 | 185 |
| 1000734134713 | 66 | 55 | 121 |
| 1002125860849 | 82 | 63 | 145 |

The first eight are m²+24 with odd m; the last is the campaign's hard forest-height example. All are below 2⁴⁰. Since log p<28, (16) gives M<1682, while 16T>1682 in every row. Thus they also satisfy T≥M/16 without computing an enormous Legendre sum. Primality is checked with SymPy's deterministic sub-2⁶⁴ path.

**CERTIFIED controls.** The existing general-numerator enumerator gives zero on both corresponding numerator-8 lines at 11,17,131,241. No step in this note promotes a positive kernel or a BM main term into an actual numerator-8 solution. The purely harmonic-analysis lemmas are numerator-blind; any successful arithmetic input would still need either a justified numerator-dependent threshold or a numerator-4-specific argument.

### 8.4 What was and was not numerically checked

**CERTIFIED:** exact AP counts for the full requested range; independent full pair enumeration at 114 selected inputs; exact rational power-image sums at three small inputs; exact difference-set identities; the finite global lower envelopes and independent zero witnesses; existing-engine counts at all hard inputs; directed upper bounds establishing (17).

**EVIDENCE only:** treating finite distributions as predictions of an eventual lower tail. The moment hypothesis (14), GRH, and OAI-003 are not numerically verified by these computations. The large-prime table is a selected adversarial sample, not a census through 10¹².

## 9. Exact gap and verdict

**CONDITIONAL positive result:** Theorem 5.4 proves M_gen(p)≥(2/π⁴−o(1))log²p from any fixed Dirichlet zero-free strip, including the explicitly conditional OAI-003. The sole-pole argument, Euler residue, conductor-uniform smoothing, and averaged L(1) lower bound are supplied in full. This removes the previously log-log-sized main-term bottleneck for the exclusively non-real remainder formulation. It does **not** control that remainder.

**PROVED scope of the negative results.**

- A positive-average **local singleton minorant** cannot omit a Fourier frequency or improve the ℓ¹/mean budget below the group size.
- BM/genus conditioning changes the group to an allowed coset; it does not remove the singleton problem inside it.
- A compressed positive square can represent the full indicator, but its strict excess over the pedestal remains the certificate count.
- A generic dual large sieve at one integer has a sharp diagonal norm. It does not supply a lower bound for the ES coefficient vector.
- For the tested finite global menus, the optimal quadratic-character minorant has exact zeros in all Mordell-hard genus fibres. The anchor argument extends this to **all powers** of the fixed prime alphabet through 19, including p-dependent cutoffs.

**Not proved:** that every positive-kernel argument fails, that every use of GRH fails, that B2 is necessary for every ES proof, or that the growing global lower envelope is always zero. None of those claims follows from this work.

**The exact unfilled assertion:** control the *negative* part of the coherent, target-dependent character sum at the single prescribed p, after keeping all necessary real information, with an improvement over the tautological bound \(X\ge-M\). Equivalently for a compressed-square construction, show a strict excess over the summed pedestals. The local kernel lemmas do not provide cross-modulus arithmetic; the dual large sieve supplies no such sign; the zero-free strip does not supply the needed coefficient/zero correlation.

**CONDITIONAL conclusion actually obtained:** H⁻mom(c,C), as explicitly quantified in (14), implies eventual (LT) and eventual ES. This is a sufficient new hypothesis formulation, **not** a proof from a clean standard hypothesis and not claimed easier than ES. It cannot be replaced by the analogous two-sided moment bound.

**Assessment / honest verdict: PARTIAL, promise 1/5.** The useful output is the conditional log-square genus theorem, the sharper local Fourier obstruction, the compressed-kernel pedestal audit, the exact one-point norm analysis, and the distinction between a genus average and its optimal global lower envelope. The finite bound T≥M/16 is a substantial numerical check of the intended target, but no infinite lower-tail estimate is proved. OAI-003 changes the available quadratic tools, not the remaining class-sensitive step.

## 10. Reproduction and audit boundaries

The governing context and all requested prerequisites were read completely: `FRONTIER.md`, `BREADTH_Z45.md`, the PR-B index/arithmetic/covers notes, `OAI_DUMP_IMPACT.md`, `BM_CORRECTED_COUNT.md`, `SINGLE_P_COUNT.md`, `METAPLECTIC_ES.md` (including Theorem K), `PARITY_AUDIT.md`, `CONDITIONAL_ES.md`, and the 20261018 lower-tail board memo. The board's superseded five-slice constants are not used. The theta-quotient identity is not treated as an Eisenstein-plus-small-cusp estimate: its competing coefficients are the same divisor-class indicators, so it supplies no missing inequality here.

No contact or coordination with the independently assigned lower-tail researcher was used. Existing line/count/genus verification functions were reused; the added mathematical checks target the new kernels and bounds.

All retained new files are this document, `scripts/z48_ltastra_*`, and `data/z48_ltastra/` (under 20 MB). Commands run from the repository root:

```sh
ulimit -v 8000000
cc -O3 -Wall -Wextra -Werror -o /tmp/z48_ltastra_census scripts/z48_ltastra_census.c -lm
cc -O3 -Wall -Wextra -Werror -o /tmp/z48_ltastra_cover scripts/z48_ltastra_cover.c
cc -O3 -Wall -Wextra -Werror -o /tmp/z48_ltastra_detail scripts/z48_ltastra_detail.c -lm
timeout 300 /tmp/z48_ltastra_census 10000000 data/z48_ltastra/census.csv
timeout 300 /tmp/z48_ltastra_census 10000000 data/z48_ltastra/census_mod4.csv 4
gzip -f -9 data/z48_ltastra/census_mod4.csv
# Each cover uses at most 8Q bytes; largest Q here is 159279120.
for q in 840 9240 120120 720720 1441440 2042040 2162160 3603600 \
         7927920 9369360 12252240 24504480 36756720 38798760 \
         103062960 134774640 159279120; do
  timeout 300 /tmp/z48_ltastra_cover "$q" > "data/z48_ltastra/cover_${q}.csv" || exit
done
timeout 90 uv run python scripts/z48_ltastra_analyze.py
timeout 1800 /tmp/z48_ltastra_detail < data/z48_ltastra/detail_inputs.txt > data/z48_ltastra/detail.csv
cc -O3 -o /tmp/z48_ltastra_existing_count scripts/z29_census.c -lm
timeout 1800 /tmp/z48_ltastra_existing_count countlist 1003000000000 \
  < data/z48_ltastra/large_inputs.txt > data/z48_ltastra/large_counts.txt
timeout 90 uv run python scripts/z48_ltastra_analyze.py
OPENBLAS_NUM_THREADS=1 timeout 600 uv run python scripts/z48_ltastra_checks.py
timeout 900 uv run python scripts/z48_ltastra_anchors.py
timeout 900 uv run python scripts/z48_ltastra_genusproof.py
```

The corpus census is exact integer arithmetic. Main-term tables use floating sums and are labelled as such; only the explicitly outward-rounded U bound is used for the complete finite inequality. The C programs are compiled without fast-math. The finite Fourier tests do not replace the proofs in §§2–7.
