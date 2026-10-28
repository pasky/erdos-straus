# LOWERTAIL_DEEP_ASTRA — fixed-prime character kernels and the lower tail

**Status: PARTIAL / NEGATIVE for the proposed mechanism. Assessment: promise 1/5 as an ES proof route.**
**ES remains open. No implication GRH ⇒ ES, or OAI-003 ⇒ ES, is established here.**

This is one focused attempt at the fixed-prime lower tail, not a survey of other ES approaches. The successive objects are the same certificate indicator: a local character minorant, its genus quotient, a compressed positive square, the dual large sieve, and finally a kernel coupling the different moduli. The attempt produces elementary, scoped obstruction lemmas and a precise sufficient **nonstandard** moment hypothesis. It does not produce the required arithmetic inequality.

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

**Assessment.** A theorem controlling only \(X_{\rm nr}^T\) relative to M is not automatically enough: the remaining real contribution must also be accounted for. Conversely a relative lower bound against \(M_{\rm gen}^T\), together with its divergence, would suffice for positivity. The existing OAI-003/GRH lower bound for the star genus term is only of log-log size. I do not silently replace it by the proved log-square BM bound.

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

**Exact remaining possibility.** A genuinely p-dependent growing menu may have a different lower envelope, or a kernel using non-real information across moduli may be better. Nothing in Theorem 6.1 or the finite tables excludes it. Proving that it is positive at each prescribed p is the unfilled step; OAI-003's small nonresidue does not prove it.

## 7. A precise sufficient hypothesis, and why it is not a standard one

No clean standard hypothesis was found to supply (LT). The following isolates how much **one-sided**, growing-order information would suffice without confusing a density result with a pointwise theorem.

Fix constants c>0, C>0, δ>0. Put L=log X,

\[
 m_X=cL^2,\qquad k_X=\left\lceil\frac{(1+\delta)L}{\log L}\right\rceil,
 \qquad D_X(p)=(m_X-T(p))_+.
\]

### Hypothesis H⁻mom(c,C,δ)

**CONJECTURE / nonstandard, not derived from GRH or OAI-003.** For every sufficiently large X,

\[
 \sum_{\substack{X<p\le2X\\p\equiv1\ (4)}}D_X(p)^{2k_X}
 \le \pi(2X)\,(C k_X m_X)^{k_X}.                              \tag{14}
\]

The centre m_X is just a fixed small log-square scale; it need not be the exact mean. One may take c well below the known BM lower-bound constant. The hypothesis is a negative-part sub-Gaussian moment estimate to a specified, growing order. It is **not** an existing named equidistribution conjecture.

### Theorem 7.1 — H⁻mom implies the requested eventual lower bound

**CONDITIONAL on H⁻mom only; PROVED implication.** For every fixed 0<η<1, all sufficiently large primes satisfy T(p)≥ηm_X in their dyadic block. Consequently T(p)≥εM(p) for some ε>0, and ES holds for all sufficiently large p≡1 (mod 4).

*Proof.* The number of primes in a block with T(p)<ηm_X is at most

\[
 \pi(2X)\left(\frac{Ck_X}{(1-\eta)^2m_X}\right)^{k_X}.          \tag{15}
\]

The logarithm of the parenthesized factor is

\[
 -\log L-\log\log L+O(1).
\]

Using π(2X)≤2X and k_X=(1+δ)L/log L+O(1), the logarithm of (15) is at most −δL+o(L). Thus (15)<1 eventually. Its integer-valued counting function is then zero. Finally M(p)≪log²p and log p∼L on the block convert this to (LT). ∎

**Assessment / weakest order in this stated mechanism.** With m_X≈L² and the right side in (14), orders k=aL/log L give an exponent −aL+o(L) in the Markov factor. The elementary π(2X)≤2X step needs a>1 for a fixed power margin. Fixed-order moments cannot eliminate one exceptional prime. This is a calibration of the sufficient *moment mechanism*, not a claim that (14) is the weakest possible hypothesis implying ES.

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

**EVIDENCE / finite moment calibration, not verification of the hypothesis.** A second census includes all p≡1 (mod 4) through 10⁷. On the 15 complete dyadic blocks X=2⁸,…,2²², take c=0.15 and δ=1/4, and normalize each moment by the number of these primes *in the block*, which is smaller than π(2X). The empirical constants needed in (14) range from 0.00884 to 0.60605; their absolute-moment counterparts range from 7.07539 to 41.17095. On the last block there are 133,975 primes, k=7, m_X=34.88089, and 1,137 positive deficits; the constants are 0.52162 and 41.17094 respectively. This illustrates why a two-sided norm is a poor surrogate. A bounded finite list of fitted constants says nothing about their eventual boundedness, and supplies no standard-conjecture implication.

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

**PROVED scope of the negative results.**

- A positive-average **local singleton minorant** cannot omit a Fourier frequency or improve the ℓ¹/mean budget below the group size.
- BM/genus conditioning changes the group to an allowed coset; it does not remove the singleton problem inside it.
- A compressed positive square can represent the full indicator, but its strict excess over the pedestal remains the certificate count.
- A generic dual large sieve at one integer has a sharp diagonal norm. It does not supply a lower bound for the ES coefficient vector.
- For the tested finite global menus, the optimal quadratic-character minorant has exact zeros in all Mordell-hard genus fibres.

**Not proved:** that every positive-kernel argument fails, that every use of GRH fails, that B2 is necessary for every ES proof, or that the growing global lower envelope is always zero. None of those claims follows from this work.

**The exact unfilled assertion:** control the *negative* part of the coherent, target-dependent character sum at the single prescribed p, after keeping all necessary real information, with an improvement over the tautological bound \(X\ge-M\). Equivalently for a compressed-square construction, show a strict excess over the summed pedestals. The local kernel lemmas do not provide cross-modulus arithmetic; the dual large sieve supplies no such sign; the zero-free strip does not supply the needed coefficient/zero correlation.

**CONDITIONAL conclusion actually obtained:** H⁻mom(c,C,δ), as explicitly quantified in (14), implies eventual (LT) and eventual ES. This is a sufficient new hypothesis formulation, **not** a proof from a clean standard hypothesis and not claimed easier than ES. It cannot be replaced by the analogous two-sided moment bound.

**Assessment / honest verdict: PARTIAL, promise 1/5.** The useful output is the sharper local Fourier obstruction, the compressed-kernel pedestal audit, the exact one-point norm analysis, and the distinction between a genus average and its optimal global lower envelope. The finite bound T≥M/16 is a substantial numerical check of the intended target, but no infinite lower-tail estimate is proved. OAI-003 changes the available quadratic tools, not the remaining class-sensitive step.

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
```

The corpus census is exact integer arithmetic. Main-term tables use floating sums and are labelled as such; only the explicitly outward-rounded U bound is used for the complete finite inequality. The C programs are compiled without fast-math. The finite Fourier tests do not replace the proofs in §§2–7.
