# Theorem G: an effective cubic-logarithmic lower bound

## 1. Statement

For every sufficiently large prime p ≡ 1 (mod 4),

**G(p) ≥ 10⁻¹⁰ (log p)³.**

The threshold p₀ is absolute and effective. No numerical value for p₀ is asserted. In fact this bound holds using only the ordered pairs (a,c) and moduli f in the following region:

- p^{0.004} < a ≤ p^{0.006}, p^{0.080} < c ≤ p^{0.085};
- a and c odd and squarefree, gcd(a,c) = 1;
- p^{0.90} < f = 4acd − 1 ≤ p^{0.99}.

Here d is a positive integer, and each summand is the original genus weight, with its original factor 1/φ(f). Put α := 0.091, so u := ac ≤ p^α. All logarithms are natural. The rather asymmetric a,c ranges are intentional: cancellation in the L-value average is required only in c. This permits enough saving in the progression calculation to sum its absolute errors over every pair (a,c).

## 2. Inputs and conventions

**Burgess.** For a primitive nonprincipal character ξ of cube-free conductor Q, integer r ≥ 2, and ε > 0,

|Σ_{M<n≤M+T} ξ(n)| ≤ C(r,ε) T^{1−1/r} Q^{(r+1)/(4r²)+ε},  T ≥ 1,

with an effective constant, uniformly in real M ≥ 0. Reference: Burgess, *On character sums and L-series II*, Proc. LMS (3) 13 (1963), 524–536; Iwaniec–Kowalski, *Analytic Number Theory*, Theorem 12.6 (cube-free-conductor form). Complex characters are allowed. We use ε = 10⁻⁶, r = 2 for progression slices, and r = 20 for the outer average.

**Pólya–Vinogradov.** A primitive nonprincipal character of conductor Q has every interval sum bounded by C√Q log(2Q), with an absolute effective C. This standard effective version, not an optimal constant, suffices.

We use `Z53_GENUSLVAL.md`, Lemma 2.1, for Burgess tails and Lemma 2.2(b), with r = 2, for the principal-character hyperbola calculation. Their proofs use only the character-sum bounds and absolute values, so apply to complex characters too. We explicitly prove the mixed Pólya–Vinogradov/Burgess variant needed for other characters. The local convolution is the one in `Z56_FAMDESIGN.md`, Proposition 3.4; it is recomputed below. Neither memo's window proposition is quoted for our progression: its hypotheses concern a different projector. Neither memo's outer-average proposition is quoted for our two-variable squarefree restriction: that average is proved below. No large sieve, zero-free region, Siegel theorem, or nonvanishing theorem is used.

The supplied elementary reciprocity lemma, (u/f) = 1 for f ≡ −1 (mod 4u), is used in the T1 audit.

Notation p^{o(1)} always means a positive quantity bounded, for each fixed η > 0, by C_η p^η with an effective constant. Only logarithms, divisor functions of integers ≤ p², and explicitly bounded convergent Euler products are absorbed this way. The elementary effective estimate τ(n) ≪_η n^η follows by separating the finitely many primes ℓ ≤ 2^{2/η} and using e+1 ≤ ℓ^{η e/2} at the others. It also bounds any fixed power of τ(n), by decreasing η. All implied constants below are effective.

## 3. Lemmas with proofs

### Lemma 1. The character and its local factorization

Let u be odd squarefree, u ≤ p^α. Define χ(n) = χ_u(n) to be zero on even n and to be the Jacobi symbol (−pu/n) on odd n. It is a real Dirichlet character, zero exactly at integers not coprime to 2up. Its primitive conductor divides 4up, is cube-free, and is divisible by p. More precisely the primitive discriminant is −4up if u ≡ 1 (4), and −up if u ≡ 3 (4); in the second case the Euler factor at 2 is removed.

Set

 g(n) := 1[(n,2up)=1] · (n/φ(n)) ∏_{ℓ|n}(1+χ(ℓ)).

Then g = 1 ∗ χ ∗ h, where h is multiplicative and its prime-power coefficients are:

- ℓ | 2up: h(ℓ)=−1 and h(ℓʲ)=0 for j≥2;
- ℓ ∤ 2up: h(ℓ)=(1+χ(ℓ))/(ℓ−1), h(ℓ²)=χ(ℓ)[1−(1+χ(ℓ))ℓ/(ℓ−1)], and h(ℓʲ)=0 for j≥3.

For t = 1/3,

 Σ_n |h(n)| n^{t−1}(1+log n)² = p^{o(1)}.                       (3.1)

Moreover, writing H := Σ h(n)/n and B_u := ∏_{ℓ∤2up}(1+χ(ℓ)/ℓ²),

 H = [∏_{ℓ|2up}(1−1/ℓ)] B_u,
 H/φ(4u) = (1−1/p)B_u/(4u),                                   (3.2)
 B_u ≥ 1/2,   L(1,χ) ≥ 0.                                     (3.3)

*Proof.* The discriminants follow from the elementary classification of quadratic characters, or directly from quadratic reciprocity. At a good prime the local series of g is

 1 + [(1+χ(ℓ))ℓ/(ℓ−1)] Z/(1−Z).

Multiplication by (1−Z)(1−χ(ℓ)Z) gives the displayed coefficients. At a bad prime χ(ℓ)=0 and the local series of g is 1, giving 1−Z. At good odd primes, |h(ℓ)|≤2/(ℓ−1), |h(ℓ²)|≤2. Thus the good-prime absolute product in (3.1), without its logarithm, is bounded by

 ∏_{ℓ≥3}(1+2ℓ^{−2/3}/(ℓ−1)+2ℓ^{−4/3}) < ∞.

Bad primes contribute at most 2^{ω(2up)}. The logarithmic factor follows by the same argument with t increased slightly, say to 3/8, since (1+log n)² ≪ n^{1/24}. Evaluation at Z=1/ℓ gives 1+χ(ℓ)/ℓ² at good primes. Since φ(4u)=2φ(u), (3.2) follows. Finally

 B_u ≥ ∏_{ℓ odd}(1−ℓ⁻²) ≥ 1−Σ_{j≥3, j odd}j⁻² > 3/4 > 1/2.

Here Σ_{j≥3, j odd}j⁻²=π²/8−1<1/4; finite product inequalities followed by limits justify the middle inequality. For real s>1 the Euler product gives L(s,χ)>0. Burgess tails give convergence and continuity at s=1, hence L(1,χ)≥0. Strict positivity is unnecessary. ∎

### Lemma 2. A mixed hyperbola estimate

Suppose F is primitive nonprincipal of conductor ≤4u, and G is a nonprincipal character whose primitive conductor is cube-free and ≤4up, with any removed primes dividing 2u. Put

 K_F := max(1, C₁√(4u)log(8u)),
 K_G := max(1, C₂τ(rad(2u))(4up)^{3/16+10⁻⁶}),

where C₁,C₂ are sufficiently large absolute effective constants. For 0<y≤p let

 Φ(y) := Σ_{ab≤y} F(a)G(b)/(ab),
 E(y) := (K_F K_G²/y)^{1/3}.

Then

 Φ(y) = L(1,F)L(1,G)
        + O(E(y)(1+log p+|log y|)²).                           (3.4)

For F≡1 and the same G, put E₀(y):=(K_G²/y)^{1/3}. Then

 Φ(y) = L(1,G)(log y+γ_E)+L′(1,G)
        + O(E₀(y)(1+log p+|log y|)²).                          (3.5)

*Proof.* Pólya–Vinogradov and Abel summation give

 |Σ_{n>t}F(n)/n| ≤ K_F/t.

Burgess with r=2, inclusion–exclusion over removed primes, and `Z53` Lemma 2.1 give

 |Σ_{n>t}G(n)/n| ≤ K_G t^{−1/2},  t≥1.

If E(y)≤1, take z=(K_F²y/K_G²)^{1/3}. Then z=K_F/E≥1 and y/z=(K_G/E)²≥1. In the exact weighted hyperbola identity, replace both partial harmonic character sums by their full L-values minus their tails. The error is at most

 K_G y^{−1/2}Σ_{a≤z}a^{−1/2}
 + (K_F/y)Σ_{b≤y/z}1
 + K_F K_G/(√y√z)
 ≤ 2K_G√(z/y)+K_F/z+K_F K_G/(√y√z)
 = 3E+E² ≤ 4E.

This proves (3.4) in that case. For (3.5), if E₀≤1 take z=(y/K_G²)^{1/3}=1/E₀ in `Z53` Lemma 2.2(b), r=2. Its bound is at most 20K_G√(z/y)(1+log y)+2/z, hence O(E₀(1+log y)).

For E>1 or E₀>1 use |Φ(y)|≤(1+log y)² when y≥1, and Φ(y)=0 for y<1. All L-values here are O(log p), and their derivatives at 1 are O((log p)²). To check these last bounds, their character moduli are at most 4up: split the series at that modulus, bound the head absolutely, and bound the tail and logarithmic tail by periodicity and Abel summation. Each nonprincipal character has period with sum zero, so its partial sums are bounded by its modulus. The asserted error then bounds the main terms too, including L(1,G)log y for y<1. ∎

### Lemma 3. The full progression slice, including its local factors

Uniformly for odd squarefree u≤p^α, define

 S_u(Y,X) := Σ_{Y<f≤X, f≡−1 (mod 4u)} g(f)/f,
 Y=p^{0.90}, X=p^{0.99}.

Then

 S_u(Y,X) = [(1−1/p)/(4u)] B_u L(1,χ_u) log(X/Y)
             + O(p^{−0.14}).                                 (3.6)

The error is effective and absolute.

*Proof.* Put q=4u. Every character ψ modulo q is induced by a unique primitive character ψ*. Since g is supported on integers coprime to q, ψ(n)g(n)=ψ*(n)g(n). Complete multiplicativity and Lemma 1 give

 ψ*(n)g(n) = (ψ* ∗ (ψ*χ_u) ∗ (ψ*h))(n),

where ψ*h in the third factor denotes pointwise multiplication, not convolution. For every ψ, the primitive conductor of G=ψ*χ_u divides 4up and is divisible by p: ψ* has conductor dividing 4u, while χ_u has a nontrivial quadratic component at p. At each odd prime dividing u the conductor exponent is at most one, and at 2 it is at most two. Thus this conductor is cube-free. Additional removed primes divide 2u. **In particular G is never principal.** These statements also hold for non-real ψ.

For ψ≠ψ₀ apply (3.4) to the first two convolution factors; ψ* is nonprincipal. Summing over the third factor and using (3.1) gives, for T∈{Y,X},

 Σ_{n≤T}ψ(n)g(n)/n
 = L(1,ψ*)L(1,ψ*χ_u) Σ_{k≥1}ψ*(k)h(k)/k
   + O(p^{o(1)}(K_F K_G²/T)^{1/3}).                           (3.7)

Here the formula is applied with y=T/k, including k>T, where Φ(y)=0; the extension is justified by (3.1), since the error has the factor k^{1/3} and at most squared logarithms. The constant term is absolutely convergent in k. Subtracting T=Y from T=X kills it.

For ψ=ψ₀, ψ*≡1. Equation (3.5), with the identical summation argument, gives

 Σ_{n≤T}g(n)/n = H L(1,χ_u)log T + C_u
                  + O(p^{o(1)}(K_G²/T)^{1/3}),

where C_u=H[γ_E L(1,χ_u)+L′(1,χ_u)]−L(1,χ_u)Σ_k h(k)log k/k is independent of T. Its series converges absolutely. Again the constant cancels in the window.

For T≥Y and u≤p^α the exponent in the nonprincipal error is at most

 [α/2 + 2(3/16+10⁻⁶)(1+α) − 0.90]/3
 = −0.148457606… < −0.14.

The principal error is smaller, with the α/2 term absent. The effective p^{o(1)} factors can therefore be absorbed into p^{0.008}, for all sufficiently large p. Orthogonality gives

 S_u(Y,X) = (1/φ(q)) Σ_{ψ mod q} overline{ψ(−1)}
                         Σ_{Y<n≤X}ψ(n)g(n)/n.

There are exactly φ(q) characters, all coefficients have absolute value 1, and the factor 1/φ(q) is retained. Consequently the error remains O(p^{−0.14}), not φ(q) times this error. The principal main term is H L(1,χ_u)log(X/Y)/φ(q); now use (3.2). ∎

### Lemma 4. There is enough squarefree coprime harmonic mass

Put A₀=p^{0.004}, A₁=p^{0.006}, C₀=p^{0.080}, C₁=p^{0.085}, and let ℬ be the set of ordered pairs in these intervals with a,c odd squarefree and gcd(a,c)=1. For sufficiently large effective p,

 M := Σ_{(a,c)∈ℬ}1/(ac) ≥ (10⁻⁵/16)(log p)².                (3.8)

*Proof.* Write L_A=log(A₁/A₀)=0.002 log p and L_C=0.005 log p. For odd t≤W and V≥1,

 Σ_{V<n≤W, n odd, t|n}1/n = log(W/V)/(2t)+O(1/V).            (3.9)

This follows by substituting n=tk and the elementary odd harmonic-sum estimate; the estimate is uniform also when V/t<1, where its error O(t/V) before division by t is sufficient.

The unrestricted odd-pair mass is L_A L_C/4+o(1). Exclude pairs for which some odd prime ℓ has ℓ²|a, ℓ²|c, or ℓ|gcd(a,c), using a union bound. Put S=Σ_{j≥3, j odd}j⁻²=π²/8−1<1/4. By (3.9), the first exclusion costs at most

 (L_A L_C/4)S + O(L_C√A₁/A₀ + L_A/C₀ + 1/A₀),

with harmless smaller terms absorbed; the second has the analogous bound with A,C interchanged. Both error bounds tend to zero because 0.006/2<0.004 and 0.085/2<0.080. For the common-prime exclusion, ℓ≤A₁, and multiplication of the two instances of (3.9) gives cost at most

 (L_A L_C/4)S
 + O((L_A/C₀+L_C/A₀)(1+log A₁)+A₁/(A₀C₀)).

This error also tends to zero. Thus M≥(1−3S)L_A L_C/4−o(1). Since 1−3S>1/4, for sufficiently large effective p this is at least L_A L_C/16, which is (3.8). ∎

### Lemma 5. An effective two-variable L-value lower bound

For the same set ℬ,

 Σ_{(a,c)∈ℬ} L(1,χ_{ac})/(ac)
 ≥ (10⁻⁵/32)(log p)²                                       (3.10)

for sufficiently large effective p.

*Proof.* Here use r=20, κ=1/20, θ=21/1600+10⁻⁶=0.013126 and N=p^{0.29}. For every (a,c)∈ℬ, the character in Lemma 1 has primitive conductor ≤4p^{1+α} and at most the prime 2 removed. `Z53` Lemma 2.1 gives

 L(1,χ_{ac}) = Σ_{n≤N, n odd}(−p/n)(a/n)(c/n)/n
                + O(p^{θ(1+α)−0.29κ+o(1)}).

The exponent is

 θ(1.091)−0.29/20 = −0.000179534 < 0.                      (3.11)

Since Σ_{a,c}1/(ac) ≪ (log p)², the total weighted tail is o(1), effectively.

For odd nonsquare n write n=n₁s², with n₁>1 odd squarefree. For a fixed admissible a, set

 V_a(n) := Σ_{C₀<c≤C₁, c odd, μ²(c)=1, (c,a)=1}(c/n)/c.

We claim

 |V_a(n)| ≪ τ(rad(2as)) n^θ C₀^{−κ}.                       (3.12)

Indeed (c/n)1[(c,2a)=1] equals the primitive character (c/n₁) multiplied by 1[(c,2as)=1]. The character (·/n₁) has conductor n₁, which is cube-free and >1. Expand μ²(c)=Σ_{e²|c}μ(e). Terms with e not coprime to 2asn₁ vanish. In the remaining terms put c=e²v and remove the condition (v,2as)=1 by inclusion–exclusion over t|rad(2as). Burgess bounds the unweighted sum up to T by

 C τ(rad(2as)) n₁^θ T^{1−κ} Σ_{e≥1}e^{−2+2κ}
 ≤ C ζ(2−2κ) τ(rad(2as)) n^θ T^{1−κ}.

The factors t^{−1+κ} are ≤1; terms with T/(e²t)<1 are empty. Partial summation on (C₀,C₁] bounds the weighted sum by at most (2+1/κ) times this constant times C₀^{−κ}, proving (3.12).

Interchange the finite a,c,n sums. The absolute contribution from all nonsquare n is, using |(−p/n)(a/n)|≤1,

 ≪ p^{o(1)} C₀^{−κ} Σ_{n≤N}n^{θ−1}
 ≪ p^{0.29θ−0.080κ+o(1)} = p^{−0.00019346+o(1)} = o(1).     (3.13)

The sum over a with weight 1/a, its divisor factors, and τ(s) are absorbed by the stated effective divisor bounds. The elementary inequality Σ_{n≤N}n^{θ−1}≤1+N^θ/θ is sufficient.

For n=m² every term is nonnegative: the Jacobi symbols are products of coprimality indicators, and (−p/m²) is 0 or 1. Retain only n=1; its contribution is exactly M. Therefore the left side of (3.10) is at least M−o(1). Apply (3.8), and weaken its constant by a factor two to obtain (3.10). All limits and thresholds are effective by (3.11)–(3.13). ∎

## 4. Proof of Theorem G

For each (a,c)∈ℬ, u=ac is odd squarefree and ≤p^{0.091}. Every integer f≡−1 (mod 4u) in (p^{0.90},p^{0.99}] has the unique positive integer d=(f+1)/(4u). Also f<p and gcd(f,2up)=1: coprimality with 2u follows from the progression, and with p from 0<f<p. The stipulated genus-weight identity gives

 γ(a,c,d) = g(f)/f.

Different ordered triples remain different summands, even if they have the same u or f. Nonnegativity permits restriction to this region, and Lemma 3 gives

 G(p) ≥ 0.09 log p · Σ_{(a,c)∈ℬ}
             [(1−1/p)B_{ac}/(4ac)] L(1,χ_{ac})
          − O(p^{0.091−0.14}).                               (4.1)

The number of ordered pairs is at most A₁C₁=p^{0.091}, which justifies the absolute total-error estimate; no cancellation over pairs is assumed. For p≥2, Lemma 1 and nonnegativity of L give

 [(1−1/p)B_{ac}/(4ac)] L(1,χ_{ac})
 ≥ L(1,χ_{ac})/(16ac).

By Lemma 5, (4.1) is at least

 [0.09·10⁻⁵/(16·32)](log p)³ − O(p^{−0.049})
 = 1.7578125·10⁻⁹ (log p)³ − O(p^{−0.049}).

Increase the absolute effective threshold so that this is ≥10⁻¹⁰(log p)³. This proves the asserted theorem and region. ∎

## 5. T1 audit: why odd squares give zero instead

Replace p by an odd square m². If gcd(f,m)>1, the square-unit test has weight zero. Otherwise, for f≡−1 (mod 4u), the supplied reciprocity lemma gives (u/f)=1 and (−1/f)=−1, so (−m²u/f)=−1. If all the local square tests passed, their Jacobi product would be +1, a contradiction. Thus every genus weight vanishes.

The exact failing step of the proof is the bold assertion in Lemma 3 that **ψ*χ_u is never principal, because its conductor contains p**. At m², the character on units is instead χ_{−u}, induced from a character η modulo 4u, with additional zeros at primes dividing m. Take that nonprincipal character η modulo 4u as ψ. Then ψ*χ_u is principal on its support; it has no Burgess cancellation. Thus Lemma 2 and (3.7) cannot be applied to this ψ. This is a second pole, not a negligible window error. Indeed χ_{−u}(−1)=−1 and η(n)=1 on the support of g, since every prime dividing such n is split. Consequently its twisted window equals the principal twisted window exactly, while its progression coefficient is −1. The two terms cancel. If m shares primes with u, the same argument holds on units with the relevant extra zeros; no nontrivial prime-conductor component remains. The failure is therefore precisely at the conductor/nonprincipality step, not at an unmentioned positivity assumption.

## 6. Numerical check summary

The script `scripts/z57_bfii_thmG_check.py` checks exact weights in the f-window (⌊p/20⌋,⌊9p/10⌋], for (a,c)=(1,1),(1,5),(3,5). These are checks of the slice residue and all its local factors, not a claim that the theorem's very narrow exponent box is populated at these sizes. The predicted quantity is exactly

 (1−1/p)L(1,χ_u)B_u log(X/Y)/(4u).

L-values are computed with the exact half-period formula for an odd primitive quadratic character ξ of conductor Q:

 L(1,ξ)=π Σ_{1≤n≤Q/2}ξ(n)/[(2−ξ(2))√Q],

followed by removal of the Euler factor at 2 when required. This numerical identity follows from the standard finite Fourier expansion of a primitive quadratic character and the Fourier series of the sawtooth function; it is used only for the check, not as an input to the proof. Character values and the finite character sum are computed as integers. The B-product is truncated at X; its omitted logarithmic tail has absolute value at most 2/X. The exact genus sum uses a smallest-prime-factor sieve, not an Euler-product approximation.

| p | u=1 ratio | u=5 ratio | u=15 ratio | pooled ratio |
|---:|---:|---:|---:|---:|
| 1000033 | 1.004098 | 1.001113 | 0.988935 | 1.001326 |
| 5212561 | 1.000363 | 0.998776 | 0.995762 | 0.999717 |
| 8813281 | 0.999571 | 1.000957 | 0.990541 | 0.999652 |

“Ratio” means exact/predicted. Pooling the three slices is also a check of an averaged quantity. All slice ratios are within 1.2% of 1; there is no factor-two discrepancy. Full output: `data/z57/bfii/thmG_check.txt`. Arrays use less than 200 MB, character sums are streamed in chunks of 250000, and the run uses a 6 GB process virtual-memory limit. The script needs only NumPy and SymPy and can be run with `uv run --with numpy --with sympy`.

## 7. List of gaps

**None identified in the proof above.** The threshold is effective but uncomputed, and the finite-size checks are evidence for local-factor bookkeeping, not substitutes for the analytic estimates. No asymptotic for the whole G(p), no upper bound for G(p), and no statement about actual Erdos–Straus solution counts is claimed.
