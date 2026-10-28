# H4_NOT_POLYLOG — simultaneous super-polylogarithmic forest and covering gaps

**PROVED, effective, relative to classical Gallagher input (G) stated in §5 and the internally proved energy lemma (OMEGA10 Theorem 3.4 / OMEGA11 Lemma 1.1):** there are infinitely many primes p ≡ 1 (mod 840) for which

    H₄(p) > exp((log p)^(1/7)),
    A_min(p) > exp((log p)^(1/7)).

In fact any fixed exponent κ < 1/6 works. The same primes have **no edge whatsoever** with larger endpoint between 4 and exp((log p)^κ). The only edges in this initial box are {1,2} and {2,3}. The original ordinary-PNT proof, retained below independently of (G), gives κ < 1/12 (in particular 1/13); **GRH** gives κ < 1/6 without (G). These exponents are deliberately not optimized. The exact archived formulation and provenance caveat for (G) are given in §5; the internal energy dependency remains unrefereed.

**Scope:** this refutes FOREST_H4 Conjecture H₂ and every fixed-polylogarithmic bound on both forest endpoints or on the covering coordinate. It says nothing about ES existence, eventual ES₅, or bounds on only one endpoint. ES remains open. Proofs and their review are internal and unrefereed.

The main new arithmetic input is an elementary bound on the *class-of-one inflated mass*. It replaces the proposed smooth/rough analysis. The transfer uses a low-modulus one-sided approximation, **not** an unproved Poisson bound for high intersections. The possible exceptional real zero is retained throughout. The effective Page–Landau bound suffices, so both unconditional versions are effective: their absolute constants and sufficiently-large thresholds are computable, though not numerically evaluated here. Siegel's ineffective theorem is not used.

## 1. Precise statement and coordinates

Throughout, logs are natural; H is an integer tending to infinity and L = log(3H). For a prime p ≡ 1 (mod 24), H₄ is the least larger endpoint of a certificate edge, with ∞ allowed. Define A_min using precisely FOREST_DEEP_FABLE Proposition 3.1:

    G_A = {−d mod A : d | A+1, 1 ≤ d < A, (−d/A_odd) = −1},
    A_min(p) = min{A ≥ 2 : p mod A ∈ G_A}.

Set A_min(p)=∞ if this set is empty. This is not the window minimum a_min or the least smaller endpoint u_min.

### Theorem 1 (PROVED, effective)

There is an effectively computable absolute C and an effective threshold such that for every sufficiently large H there is a prime

    H² < p ≤ exp(C L^12 (log L)^2),       p ≡ 1 (mod 840),             (1)

with both properties:

* the induced forest on [1,H] has exactly the two edges {1,2}, {2,3};
* p mod A ∉ G_A for every 2 ≤ A ≤ H.

**Stronger unconditional version, PROVED relative to classical (G):** the upper bound in (1) improves effectively to exp(C L^6 log L). **CONDITIONAL on GRH:** the same improvement follows without (G).

Consequently the ordinary-PNT route gives every κ < 1/12, and the Gallagher route gives every κ < 1/6, unconditionally, with both minima greater than exp((log p)^κ) at infinitely many such primes. GRH gives the latter range independently of (G). The constants in the cutoff do not matter because these are strict inequalities below the limiting exponents. Distinctness is guaranteed by p > H², not by assuming either minimum finite.

**Novelty / dependency audit (Assessment).** The fixed-H avoidance and logarithmic Linnik lower bound are already in FOREST_H4 §3.1 and FOREST_DEEP_FABLE §3.2. The local-lemma/energy/prime-transfer architecture appears in POINTWISE_OMEGA8–13 for a different Type-II witness modulus W. No inequality transferring that W-bound to H₄ or A_min is assumed here. We instead verify a new pair of event families, prove their inflated-mass bound, extend the graded argument to the prime 2, and give a coefficient-norm transfer using ordinary uniform PNT in progressions. The original proof avoids the stronger Gallagher transfer. The review follow-up additionally verifies its interfaces explicitly in Lemma 7b below, using POINTWISE_OMEGA9 Theorem 1.1 and the overlapping-modulus extension in POINTWISE_OMEGA11 Lemma 3.1. No additional divisor estimate or hypothesis about ES is used.

## 2. The two congruence families and their safe point

### Lemma 2 (PROVED: exact encoding)

Use the following bad events on prime-Haar units n:

    E_(a,v): n ≡ −a−v (mod av),  1 ≤ a < v ≤ H, gcd(a,v)=1,

omitting (a,v)=(1,2),(2,3); and

    C_(A,d): n ≡ −d (mod A),  2 ≤ A ≤ H, d | A+1, d < A,

omitting (A,d)=(2,1),(3,2). All classes are reduced. Every modulus is ≤ T := H², and the combined number of indexed events is O(H²). Duplicate events may be removed.

The unit n=1 belongs to none of these events. If a prime p>H² avoids all of them and is 1 modulo 840, it has both conclusions of Theorem 1.

*Proof.* For coprime a,v the edge condition is exactly av | p+a+v, equivalently the two congruences p ≡ −a (mod v), p ≡ −v (mod a). Every edge with endpoints below p has coprime endpoints: a common divisor divides p. To test n=1, v | a+1 with a<v forces a=v−1. The other congruence then gives v−1 | 2, hence precisely the two omitted edges.

For the covering events gcd(A,d)=1 because d | A+1. A safe-point failure requires d=A−1 | A+1, hence A=2 or 3 and exactly the omitted pairs. Neither omitted pair belongs to G_A: A_odd=1 for A=2, and (−2/3)=+1 for (A,d)=(3,2). Thus avoiding the larger, colour-free shadow family implies avoidance of every G_A. Finally p ≡ 1 (mod 840) forces the two omitted edges to exist and to be non-certifying: p ≡ 1 (mod 24) gives labels (p+3)/2 ≡ 2 (mod 4) and (p+5)/6 ≡ 1 (mod 4), respectively. ∎

**PROVED smooth-part check.** Let Y≥3 and

    L_Y = ∏_(ℓ≤Y, prime) ℓ^(floor(log_ℓ H)+2).

If n ≡ 1 (mod L_Y), both Y-smooth endpoints a<v≤H divide L_Y. The preceding proof again gives only (1,2),(2,3). The extra powers include 8 and 3, so their slot tests are non-certifying; there is no lost 2-adic or 3-adic case. This validates step 1 of the brief, but does not justify its asserted rough-mass or high-intersection estimates.

## 3. The arithmetic gain: inflated mass is polynomial in log H

Write g(m,b)=gcd(m,b−1), using any representative for b. For a congruence n ≡ b (mod m) consistent with n ≡ 1 (mod Q), its conditional Haar probability is exactly

    φ(gcd(m,Q))/φ(m)

and therefore at most

    s(m,b) := C log log(3T) · g(m,b)/m.                           (2)

Indeed gcd(m,Q) | b−1, φ(gcd(m,Q))≤g(m,b), and m/φ(m)≪log log(3T). The bound holds uniformly over every Q reached by conditioning on further digits of 1. Inconsistent events have probability zero.

### Lemma 3 (PROVED: new mass estimates)

For the edge and shadow families, even before removing their omitted pairs,

    Σ_(a<v≤H) gcd(av,a+v+1)/(av) ≪ L^4,                         (3)
    Σ_(A≤H, d|A+1, d<A) gcd(A,d+1)/A ≪ L^3.                   (4)

Consequently the sum S♯ of (2) over the combined family is

    S♯ ≪ L^4 log L.                                             (5)

*Proof of (3).* Coprimality may be dropped for this upper bound. Put s=a+v+1. Then

    gcd(av,s)=gcd(a(a+1),s),     s≤2v  (since a<v).

Using gcd(k,s)=Σ_(d|k,d|s) φ(d), positivity, and enlarging the s-range,

    Σ_(a<v≤H) gcd(av,a+v+1)/(av)
      ≤ 2 Σ_(a≤H) (1/a) Σ_(s≤2H+1) gcd(a(a+1),s)/s
      ≤ 2(1+log(2H+1)) Σ_(a≤H) τ(a)τ(a+1)/a.                  (6)

Here Σ_(s≤X,d|s) 1/s≤(1+log X)/d and φ(d)/d≤1.

For completeness, Σ_(n≤X) τ(n)τ(n+1)≪X log²(3X) has an elementary proof: use

    τ(n) ≤ 2 Σ_(d≤sqrt(X), d|n) 1,
    τ(n+1) ≤ 2 Σ_(e≤sqrt(X+1), e|n+1) 1.

Only coprime d,e contribute. The number of n in each pair of classes is at most X/(de)+1. Summing the main terms gives O(X log²(3X)); the O(1) terms sum to O(X). Partial summation now gives Σ τ(a)τ(a+1)/a≪L³, proving (3).

*Proof of (4).* Write A+1=dk. Then

    gcd(A,d+1)=gcd(d+1,k+1),       1/A≤(3/2)/(dk)  (A≥2).

Enlarge to all dk≤H+1, d,k≥1, and use symmetry to restrict to d≤k, with a factor 2. For each q|d+1, q≤d+1≤2d. Along k ≡ −1 (mod q), k≥d, comparison with the harmonic integral gives

    Σ_(d≤k≤K, k≡−1 mod q) 1/k ≤ 1/d + (1/q)log(max(1,K/d))
                                         ≤ (2+log(3H))/q.

After expanding the gcd as Σφ(q), the resulting bound is

    ≪ L Σ_(d≤sqrt(H+1)) τ(d+1)/d ≪ L³.

The last estimate follows from Σ_(n≤X)τ(n)≪X log(3X) and partial summation (replace d by n−1). Terms with dk<3 only enlarge the positive upper bound. Equations (2)–(4) prove (5). ∎

**Assessment.** This controls inflation on *every* intermediate class-of-one fibre. It is weaker than the brief's desired conditional exponent 2 but stronger in the uniformity needed for an adaptive local lemma. No estimate on events sharing a specified large prime, no smooth-number asymptotic, and no shifted-divisor theorem beyond the elementary calculation above is used.

## 4. Graded conditioning and a one-sided low-modulus approximation

The following details specify the nonstandard internal input rather than hiding it behind “Bonferroni”. Put ℒ=log T; since T=H², ℒ≍L. All probability measures in this section are Haar measures on units, conditioned on a class of 1.

### Lemma 4 (PROVED: graded local lemma, including even moduli)

For any reduced congruence family with m≤T, no event at n=1, and uniform weights (2) summing to S♯, there is Q divisible by 840 such that

    log Q ≪ 1+ℒ²S♯,       S:=Σ_live P(E)≤S♯,
    Σ_(ℓ∈supp E) w_ℓ ≤ c:=1/64 for every live E,                (7)

where w_ℓ=Σ_(E using free digits at ℓ) P(E). There is no deterministic live event. If F is the indicator of avoiding them on this fibre, then

    δ:=E F ≥ exp(−3S).                                          (8)

*Proof.* Start with Q=840 (a₂=3, a₃=a₅=a₇=1). **Include 2 in the procedure**, unlike the odd-modulus notation in POINTWISE_OMEGA11. For a prime ℓ, let a_ℓ=v_ℓ(Q), and let f_ℓ be the maximum exponent used in any original event. While a_ℓ<f_ℓ and

    w_ℓ > c(a_ℓ+1)logℓ/ℒ,

fix one more digit to that of 1 by increasing a_ℓ. Remove inconsistent events. The procedure terminates. An event cannot become deterministic and true: that would give m|Q and b≡1 (mod m), contradicting the safe point.

At termination, an event using ℓ has v_ℓ(m)≥a_ℓ+1, so summing the thresholds gives (7). A step costs logℓ, at most ℒw_ℓ/[c(a_ℓ+1)]. Charge it to the uniform s(E) of its incident events. Each pair (ℓ,a) is stepped at most once; thus

    log(Q/840) ≤ (ℒ/c) Σ_E s(E) Σ_(ℓ|m_E) H_(v_ℓ(m_E))
                ≤ (ℒ/c) Σ_E s(E) Ω(m_E) ≪ ℒ²S♯.

For the local lemma take x_E=2P(E). Each P(E)≤c because the support is nonempty, and the neighboring x-sum is ≤2c. Thus

    ∏_(E'∼E)(1−x_E') ≥ exp(−2c/(1−2c)) > 1/2.

The asymmetric Lovász Local Lemma gives δ≥∏(1−x_E)≥exp(−3S). The same estimates hold for every subfamily, and its usual conditional bound gives, for any cylinder D,

    P(D | avoid subfamily) ≤ P(D)∏_(E∼D)(1−x_E)^−1.              (9)

This last statement follows directly by separating the subfamily into events meeting supp D and events independent of D, then using the chain rule and the LLL conditional bound. ∎

### Energy input (PROVED internally; precise imported statement)

For a good indicator f of any family of prime-power prefix cylinders with original moduli ≤T, and also after conditioning on one such cylinder, let f^{=U} be its orthogonal Efron–Stein components over the remaining independent prime-power digits. For a digit set U define the *absolute* modulus

    m_U=∏_ℓ ℓ^(1+max{i:(ℓ,i)∈U}),

omitting empty prime factors. Then

    Σ_U 2^(log(m_U)/(2ℒ)) ||f^{=U}||₂² ≤ 1,
    Σ_(log m_U>τ) ||f^{=U}||₂² ≤ 2^(−τ/(2ℒ)).                  (10)

This is POINTWISE_OMEGA11 Lemma 1.1, derived from POINTWISE_OMEGA10 Lemma 3.1 and Theorem 3.4. It needs neither small masses nor an analytic assumption. Its finite hypergraph inequality is proved by polarization and deletion–contraction, not conjectured. The argument is prime-agnostic, so it includes 2. The base digit is uniform on units; subsequent digits are uniform. Fixed initial digits, including those fixed by another cylinder, merely move the first free index. In particular the weight at that index is its **absolute** prime power, not its relative digit number.

**Proof synopsis / dependency check.** The cover bound majorizes the weighted Efron–Stein energy by E_x Q_μ(𝓗(x)), where 𝓗(x) consists of the supports of the events true at x and Q_μ=Σ_V μ^V N(V)² for the signed cover count N. Polarization writes Q_μ as an average of Θ_λ(𝓗_P)², with Θ_λ(𝒞)=Σ_(J⊂𝒞)(−1)^|J|λ^(∪J). Deletion–contraction at a vertex of a selected edge gives |Θ_λ|≤∏_(E in a matching)(λ^E−1) whenever each λ^E≤2; hence Q_μ≤1. For prefix digits use independent tail blocks, at most one per prime, and increments of λ_ℓ^(i+1), with λ_ℓ=2^(logℓ/(2ℒ)). Every cylinder has ∏λ_ℓ^(2v_ℓ)≤2, giving (10). The cited notes contain the full algebra, including empty and repeated edges and conditioned systems. The proof-design reviewer independently rechecked this derivation before its use here.

### Lemma 5 (PROVED: explicit coefficient budget)

Let N≤T² be the number of live distinct events. There is a real function B, a finite linear combination of reduced congruence cells, such that on the fibre n≡1 (mod Q)

    B≤F,       E(F−B)≤δ/100,       μ:=E B≥0.99δ,
    log D + log(2+K) ≪ ℒ(S+ℒ),                                  (11)

where D is its largest cell modulus and K is the **unweighted** sum of absolute cell coefficients. Every cell is consistent with Q and uses only primes from the original family. If N=0, take B=1.

*Proof.* Order the event indicators A_i. On E_j approximate the indicator F_<j of avoiding earlier events by its Efron–Stein truncation u_j to log m_U≤τ, where

    τ=2ℒ ceil(log₂(100 N²(S+1)e^(3S))),       R=e^τ.

Equation (10) makes the conditional squared error ≤e^(−3S)/(100N²(S+1)). Extend u_j off E_j by ignoring the digits fixed by that conditioning. Set

    B=1−Σ_i A_i(1−Σ_(j<i) A_j u_j)².                            (12)

The elementary Bazzi–Razborov–Wigderson identity (POINTWISE_OMEGA8 Lemma 3.1) says

    F−B=Σ_i A_i(Σ_(j<i)A_j(F_<j−u_j))² ≥ 0,
    E(F−B)≤N²Σ_j P(E_j) E[(F_<j−u_j)² | E_j]≤δ/100.

For the coefficient count, a fixed modulus d=m_U admits at most ∏_(ℓ^v||d)2^(v−1)≤d digit sets U. There are therefore at most R² digit sets with m_U≤R. Each component f^{=U} has sup norm ≤2^|U|≤R, by the alternating conditional-expectation formula, and is a function on at most R residues modulo m_U. Its cell coefficient norm is ≤R². Expanding over **all Q-consistent residues**, not only those satisfying E_j, gives

    K(u_j)≤R^4.

Intersecting two cells gives one cell or the empty set, so unweighted coefficient norms multiply submultiplicatively. Expansion of (12) gives

    K(B)≤1+N+2N²R^4+N³R^8,       D≤T³R².

The cells use no new primes. Since N≤T², the two logarithmic budgets in (11) follow. This is a bound on a representation; merging identical cells only improves it. ∎

### Lemma 6 (PROVED: free real-character twist)

For every real primitive character ψ whose conductor f is not a divisor of Q, the coefficient relevant to the cell expansion satisfies

    |E[Bψ]|≤μ/4,                                                (13)

unless it is zero automatically. The expectation is taken on an enlarged finite unit product if necessary.

*Proof.* Because 8|Q, a real primitive conductor not dividing Q has an odd prime ℓ₀∤Q. Split ψ into its Q-supported part (identically 1 on our fibre) and its coprime part. If a prime of that latter part occurs in no cell, its mean is zero. Otherwise choose ℓ₀ in that part and let F' avoid the events not using ℓ₀. Averaging ψ over the independent uniform unit coordinate ℓ₀ gives

    |E[Fψ]|≤Σ_(E∋ℓ₀) p_(ℓ₀)(E) P((E with ℓ₀ removed) ∩ F').

The cylinder with ℓ₀ removed has neighborhood x-mass ≤2c by (7), so (9) bounds its conditional probability by exp(2c/(1−2c)) times its unconditional probability, a factor below 1.04. Also w_(ℓ₀)≤c: some incident event exists, and its support sum bounds this mass. Therefore

    |E[Fψ]|≤1.04c E F',       E F≥(1−1.04c)E F'.

Together with E|F−B|≤δ/100 and μ≥0.99δ, this proves (13) with ample slack. If the free conductor does not divide any cell modulus, all individual twisted cell means vanish instead. ∎

## 5. Transfer to primes, with the exceptional zero retained

**Classical analytic inputs (PROVED in the literature).** We use the standard uniform prime number theorem in progressions with the Landau–Page exception. There are absolute c₀,c₁>0 such that, for all q≤exp(c₀ sqrt(log x)) and (a,q)=1,

    θ(x;q,a)=x/φ(q)−1_(f|q) ψ(a)x^β/(βφ(q))
                         +O(x exp(−c₁ sqrt(log x))).             (14)

Here one single primitive real exceptional pair (ψ,β), if present, is chosen uniformly for the entire modulus range, with β close to 1; otherwise the second term is absent. **Precise published citation:** Montgomery–Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge Studies in Advanced Mathematics 97 (2007), **Corollary 11.20, equations (11.32) and (11.34), p. 381**, combined with **Corollary 11.10 (Page), p. 369**. The former is the per-modulus θ formula; the latter makes its exception global after absorbing zeros below the common threshold, as derived next. Effectivity of the underlying constants is explicitly stated on p. 380 following Corollary 11.17. These statements were checked directly in the [author-hosted chapter 11](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/15.0_pp_358_396_Primes_in_arithmetic_progressions_II.pdf), DOI [10.1017/CBO9780511618314.013](https://doi.org/10.1017/CBO9780511618314.013).

**Derivation of the required uniformity.** Put U=exp(c₀ sqrt(log x)). Landau–Page gives at most one primitive character of conductor ≤U with a real zero β>1−c/log U. Truncate each primitive-character explicit formula at height exp(a sqrt(log x)), for a fixed small a>0. The standard region Re s≤1−c'/log(q(|Im s|+2)) bounds all nonexceptional zeros in this range; any other real zero is bounded by the Landau–Page threshold instead. Their total contribution is O(x exp(−c₁ sqrt(log x))), after absorbing powers of log x. Character orthogonality averages, rather than sums, these individual errors over the φ(q) characters. The unique primitive exception induces exactly one character modulo each q divisible by its conductor f and none otherwise, giving (14). Removing prime powers costs O(sqrt(x) log²x), inside the same error. Thus the exception is **global**, not a potentially different character for every q. The usual paired treatment of a real zero near 0 and the explicit-formula constant avoids any spurious 1/(1−β) error.

We use the **effective Page–Landau bound**, verified in the same published source, **Corollary 11.12, p. 370**:

    1−β ≥ c₂ / (sqrt(f) (log f)²),        f≥3,                   (15)

with an effectively computable absolute c₂>0 for an exceptional real zero of a primitive quadratic character of conductor f. Nonexceptional real zeros already have the stronger zero-free-region bound. In particular (15) implies 1−β≥c₃/f with an effective c₃, since (log f)²/sqrt(f) is bounded on f≥3. The original use of Siegel's ineffective theorem was unnecessary. Deleting the exception or applying Siegel–Walfisz outside its range would still be invalid.

Under GRH replace (14) by θ(x;q,a)=x/φ(q)+O(sqrt(x) log²(qx)), uniformly in reduced classes, with no exceptional term. Bertrand's postulate supplies an auxiliary prime below.

### Lemma 7 (PROVED, effective: ordinary-PNT transfer)

For the system of Lemmas 4–6 there is a prime avoiding the original events, congruent to 1 modulo Q, exceeding T, with

    log p ≪ [log Q + log D + log(2+K) + S + log T + 1]².           (16)

Under GRH the square on the right can be removed (enlarging the constant).

*Proof.* Append a prime r∈(T,2T] to Q, fixing n≡1 (mod r); write Q'=Qr. The event and cell moduli have prime support ≤T, so the product law, μ, δ and K do not change. Any prime in this class exceeds r>T. This device also removes every nonunit input from consideration.

Write B=Σ_i c_i 1_(n≡b_i mod d_i) on the original fibre. Combining each cell with n≡1 (mod Q') gives one reduced class modulo q_i=lcm(Q',d_i)≤Q'D. Sum (14) with coefficients c_i. Set ν=E[Bψ] on the class of 1 modulo Q', enlarging the product by any conductor primes needed. Then

    Σ_(p≤x, p≡1 mod Q') B(p)log p
      = [xμ−x^βν/β]/φ(Q') + O(K x exp(−c₁ sqrt(log x))).         (17)

The coefficient identity for ν follows by averaging a primitive character over each cell: its mean vanishes unless f|q_i, and otherwise it is its value on that cell times the cell probability.

If f∤Q', Lemma 6 gives |ν|≤μ/4 or ν=0. Its proof remains valid after appending r: a conductor factor r is fixed to 1, and any other new factor absent from B averages to zero. For x large and β>1/2 the numerator in (17) is at least xμ/2.

If f|Q', then ψ≡1 on our fibre, so ν=μ **exactly**. The numerator is

    xμ[1−x^(β−1)/β]
      ≫ xμ min(1,(1−β)log x)
      ≫ xμ exp(−C log Q')                                       (18)

for x sufficiently large, by (15). The bracket estimate uses log x≥4 and β>1/2; it is capped at 1. Thus even the worst Siegel-zero class keeps a positive main term. The factor 1/φ(Q') in (17) must also be paid for.

Choose

    sqrt(log x)=C₃[log Q' + log D + log(2+K) + S + log T + 1]

with a sufficiently large effectively computable absolute constant and threshold, using the effective constant in (15). This puts every q_i in the range of (14) and makes the absolute error in (17) smaller than half the lower bound (18)/φ(Q'). Hence the sum is positive. Since B≤F and every prime in the progression is a unit for all the original moduli, some prime has F(p)=1.

Under GRH the absolute error is O(K sqrt(x) log²(Q'Dx)); choosing log x a sufficiently large constant times the displayed budget gives the same positivity without (18). This proves (16) and its GRH version. ∎

### Lemma 7b (PROVED relative to classical (G), effective: linear transfer)

For the same system there is a prime p>T avoiding the original events, p≡1 (mod Q), such that

    log p ≪ log Q + log D + log T + 1.                           (16b)

This removes the square in (16) **without GRH**. It imports POINTWISE_OMEGA9 Theorem 1.1 through POINTWISE_OMEGA11 Lemma 3.1, not a new unproved prime-distribution conjecture. We state the exact analytic input and verify the overlap and character interfaces here.

**Input (G), exact form used.** Write ϑ(x;χ)=Σ_(p≤x)χ(p)log p. For absolute effective constants c≥1, C_G and one fixed sufficiently large admissible κ_G, whenever 1<U^(6c)≤x,

    Σ_(q≤U) Σ*_(χ mod q) |ϑ(x;χ)−1_(q=1)x|
      ≤ C_G x [exp(−log x/(κ_G log U))+(log x/log U)²/U].         (G0)

If there is an exceptional real primitive character ψ with zero β satisfying 1−β<1/(κ_G log U), replace its summand by |ϑ(x;ψ)+x^β/β| and replace the right side by

    C_G (1−β)(log x) x [exp(−log x/log U)+log x/(U log U)].       (G1)

The star means primitive characters, including the trivial character of conductor 1. Crucially the factor (1−β)log x multiplies **both** terms in (G1). Page's uniqueness theorem is used with κ_G sufficiently large and its height restriction respected.

**Provenance and qualification.** This is Gallagher's classical large-sieve/Linnik theorem in the formulation **Montgomery–Vaughan, Multiplicative Number Theory III (draft), Theorem 28.19, pp. 229–232**, in the already archived `sources/omega9/montgomery-mnt3.pdf`; those pages were rechecked for this follow-up. The attribution is Gallagher, “A large sieve density estimate near σ=1”, *Invent. Math.* 11 (1970), 329–339. The original paper and its theorem numbering have not been independently checked here. We use exactly the fixed sufficiently large κ_G justified in POINTWISE_OMEGA9 §1, including its repair of the draft's parameter-range slip and omitted height qualifier. Thus this stronger version is **PROVED relative to the stated classical input (G)** and the internal energy lemma, not a claim that this task re-proves Gallagher or audits the whole draft. The ordinary-PNT version of Theorem 1 does not depend on (G).

*Proof and interface audit.* Append r∈(T,2T] and put Q'=Qr as in Lemma 7. Let ℕ=lcm(Q',d₁,d₂,…) and Z=Q'D, enlarging D to 1 if necessary. All expectations below are on the unit fibre n≡1 (mod Q'). Since B≤F and E(F−B)≤δ/100,

    B⁻≤F−B,       𝒜:=E|B|/μ≤1+2/99<1.03.                     (20)

Unlike the original coprime-modulus statement of OMEGA9 Theorem 1.1, our d_i can share primes and powers with Q'. The extension of OMEGA11 Lemma 3.1 applies: each cell is consistent with 1 modulo gcd(d_i,Q'), 8|Q', and the Haar mean is taken on the fibre. Explicitly, extend B·1_(n≡1 mod Q') to the unit group modulo ℕ and expand in characters. Its coefficients satisfy

    c(χ)=E[Bχ̄]/φ(Q'),       |c(χ)|≤𝒜μ/φ(Q'),
    c(χ₀)=μ/φ(Q'),         c(χ)≠0 ⇒ cond(χ)≤Z.                  (21)

The conductor assertion follows term by term: a cell, combined with Q', is a coset modulo lcm(Q',d_i)≤Z. A fixed primitive character induces at most one character modulo ℕ; thus the number of nonzero coefficients is ≤Σ_(q≤Z)φ(q)≤Z². No coprimality between Q' and d_i is needed.

For a real character with conductor f|Q', its coefficient is exactly μ/φ(Q'). If f∤Q', the coefficient is at most μ/(4φ(Q')) in absolute value by Lemma 6, which remains valid after appending r. Alternatively split its primitive conductor into its Q'-supported part and its coprime part: the former divides Q' because 8|Q' and odd real primitive conductors are squarefree; its value on the fibre is 1. This is precisely the exceptional-character dichotomy required by OMEGA9.

The prime sum omitting p|ℕ equals the character sum with coefficients (21). Passing from induced to primitive prime sums costs at most

    R₁ ≪ Z² (𝒜μ/φ(Q')) log ℕ ≪ Z³𝒜μ/φ(Q'),                   (22)

since log ℕ≤log Q'+log lcm(1,…,floor D)≪Z. This harmless finite-support correction is the only place the number of characters enters.

To see explicitly why (G) gives a linear logarithmic budget, choose a sufficiently large fixed B₀, set x=Z^C and U=x^(1/(κ_G B₀)), and take C sufficiently large effectively. Then U≥Z, U^(6c)≤x, and (G0), multiplied by the coefficient bound in (21), is less than μx/(100φ(Q')). In the exceptional case put u=(1−β)log x<B₀. Formula (G1) instead bounds the error by

    C_G 𝒜 u (μx/φ(Q')) [exp(−κ_G B₀)+κ_G B₀/U]
       ≤ (μx/(100φ(Q'))) min(u,1),                              (23)

after choosing B₀ and C. If the exceptional character occurs with conductor dividing Q', the main term is

    (μx/φ(Q')) [1−x^(β−1)/β] ≥ (μx/(2φ(Q'))) min(u,1).

Moreover (15) and f≤Q'≤Z give min(u,1)≫Z^(−1/2)(log Z)^(−2). Thus (22) is also smaller than this main term for x=Z^C with C sufficiently large (C>5 suffices for this correction). If the exceptional conductor does not divide Q', Lemma 6 leaves at least μx/(2φ(Q')) instead; an exceptional character absent from the expansion contributes nothing. The prime sum is positive in every case.

Every counted prime is 1 modulo r, hence exceeds r>T. The cell prime support is ≤T, so B(p)≤F(p) is valid there. Some prime therefore avoids the original events. Finally log x=C log Z≪log Q+log D+log T+1, proving (16b). All constants used in (G), (15), the finite algebra, and these choices are effective. ∎

### Proof of Theorem 1 (PROVED, effective)

Apply Lemma 3 to the joint family in Lemma 2. Lemma 4 gives

    S≪L^4 log L,          log Q≪L^6 log L.

Lemma 5 gives log D+log(2+K)≪L^5 log L. The largest term in (16) is therefore O(L^6 log L). Lemma 7 proves (1), and its GRH variant, simultaneously for the edge and covering families. Independently of GRH, Lemma 7b gives log p≪L^6 log L relative to (G), proving the stronger unconditional version. Q is a multiple of 840. Lemma 2 supplies the forest and covering conclusions. ∎

## 6. Exact consequences and non-consequences

**PROVED corollaries.** Along the same sequence, for every fixed A>0,

    H₄(p)/(log p)^A → ∞,       A_min(p)/(log p)^A → ∞.

Thus FOREST_H4 Conjecture H₂ is false. More generally no all-large-prime certificate theorem can require both endpoints ≤C(log p)^A, for any fixed C,A. The attachment target in FOREST_DEEP_FABLE §6, including its sign-free sufficient form with both endpoint/cofactor bounds, is false. The covering statement “some A≤C(log p)^A₀ meets G_A” is also false for every fixed C,A₀. Repeated use of A as a cutoff exponent and a modulus is avoided in the last formulation by writing A₀.

**Not touched (PROVED scope distinctions).** The argument does not refute bounds for u_min, v07min, the least López vertex, or H_(★)(A) of LOWERTAIL_DEEP_FABLE §5. A fixed small vertex may have a partner of order p; its existence is a factorization condition on p+u, not a congruence with both endpoints fixed below H. Likewise a bound on the number of shifts or on a level t is not a bound on both endpoints or on the covering modulus A. No inference to nonexistence of forest certificates, ES solutions, or any numerator-8 representation is made.

### Haar-model bounds (PROVED / limitations)

Let δ_joint(H) be the probability, under prime-Haar with n≡1 (mod 24), of avoiding the joint family. Lemmas 3–4 give

    δ_joint(H) ≥ exp(−C L^6 log L).                              (19)

Indeed the subfibre n≡1 (mod Q) has relative mass φ(24)/φ(Q), and (8) applies within it. This also lower-bounds the ordinary certificate-survival probability δ(H), defined under prime-Haar with n≡1 (mod 24).

The same *conditional* bound exp(−C L^6 log L) holds after fixing n≡1 (mod L_Y) for any Y≥3: begin the graded procedure at lcm(840,L_Y). Only the *additional* conditioning cost is charged, still O(ℒ²S♯); the extra fixed 5,7 residues cost at most a constant. Equation (2) remains uniform. This provides a rigorous replacement for the brief's unproved exp(−C log²H) conditional survival claim, with a weaker exponent.

**PROVED existing upper bound only:** δ(H)≪(log H)^(−1/2), from the independent root-1 certificate events at primes q≡3 (mod 4), q≤H (FOREST_H4 Theorem 3.5). For the colour-free no-edge survival, all prime q≥5 yield forbidden root-1 edges and give the stronger upper bound ≪1/log H. Neither estimate matches (19). **Conjecture S's exponent 2 remains open.** The parent's 10⁹-draw CRT data are evidence for it, not an input to any theorem here.

**Assessment: why not the suggested Bonferroni proof?** The smooth lemma is correct. What was not supplied is a uniform bound S_j≤(Cμ)^j/j! for growing-order intersections, nor the proposed late-prime conditional mass bound. Shared-prime clusters prevent deducing either from a first moment or a dependency graph alone. Rather than assume these statements, (10)–(12) replace alternating intersection truncation by squared approximation error. This is the precise repair, not a claim that the suggested inequalities have been disproved for these particular events.

## 7. Checks, controls, and review

**Validation protocol.** New scripts live under scripts/z49_h4lower_*, outputs under data/z49_h4lower/. They check only the new arithmetic and interfaces, reusing existing square, fraction and energy suites where those already cover a behavior. All commands have timeouts and an 8,000,000-KiB virtual-memory ceiling. Numerical probabilities are **EVIDENCE**, exact finite identities and primality/edge audits are **CERTIFIED** only within their checked ranges.

**CERTIFIED finite checks (checks.json):** 93,622 instances of the two new gcd identities; 378 independent comparisons of pair enumeration, parent enumeration and the joint congruence union; 50 actual prime fixtures n≡1 (mod L_Y), at (H,Y)=(4,3),(8,3),(12,5),(24,5),(40,7), including primes up to 333,396,000,001. The smooth-endpoint lemma and both exceptional-edge slot tests pass. The graded process passes at H=16,32,64, including additional 2-adic steps. These small instances end with **zero live events**; they do not experimentally exercise a nonempty residual LLL system.

**CERTIFIED controls:** full divisor enumeration reproduces (H₄,A_min)=(5,5),(7,7),(5,5),(29,29),(29,29),(17,34),(19,37),(26,39),(51,111) at the nine required hard primes, in the order 193,409,577,2521,3361,5569,9601,66529,8813281. At 17 and 241 there are numerator-4 certificates but no 8-slot edge. The unchanged z43 suite checks 24,389 edges, 21,135 exact fraction identities, and 17,372 edges at all 499 odd squares through 999², with no square certificates. Our mechanism is avoidance, so it need not distinguish squares in order to force a solution: it forces no solution at all.

**Existing energy-suite finite checks:** 100 ordinary and 75 nondegenerate conditioned prefix systems pass the proved weighted-energy bound (maximum 0.995593 and 1.000000). The additional rho1 experiment in the reused script is not used in the proof. The hostile reviewer also ran 20 fresh-seed BRW trials, maximum identity discrepancy 1.78×10⁻¹⁵. These are numerical checks of finite algebra, not analytic proof certification.

**EVIDENCE (model.json):** an independent exact-finite-group CRT sampler uses 10,000 draws for each of 15 (H,Y) settings, with uniform unit residues and full powers at primes ≤Y fixed to 1. At Y=13 it records:

| H | no nontrivial edge | H₄>H | A_min>H | joint edge/shadow avoidance |
|---:|---:|---:|---:|---:|
| 64 | 396 | 1335 | 1413 | 384 |
| 128 | 36 | 296 | 425 | 30 |
| 256 | 1 | 54 | 91 | 0 |

The all-edge target is visibly stronger than certificate avoidance. A zero sampled count is not zero probability. The unconditioned H₄ counts at H=64,128,256 are 56,12,0; the parent's much larger simulation remains the informative source for the unconditioned tail. No fitted constant or model independence across actual primes enters Theorem 1.

**Hostile internal review:** a fresh deep reviewer read the complete proof, its internal energy dependencies, checker and outputs, independently reproduced checks.json, and returned **SOUND, no blocking mathematical defect**. It specifically rechecked inflated mass, the even-prime extension, absolute digit weights, the unweighted coefficient budget, the free-character twist, and both exceptional-zero cases. Its two presentation repairs (the ∞ convention for A_min and replacing this pending validation paragraph) are applied; its request for a more precise explanation of the global PNT exception is addressed by the derivation in §5. A separate earlier deep proof-design audit supplied the even-prime and coefficient-extension repairs already incorporated in the first full draft. Review provenance is retained in data/z49_h4lower/review.txt.

**Cross-model review and follow-up:** the Opus review at `reviews/z49-h4lower-review.md` on branch `side-agent/z49-rev-h4lower` returned **SOUND** for the original theorem, with the minor repairs now applied: effective Page–Landau input, precise published citations, s≤2v, visible internal-energy dependency, and explicit normalization of δ(H). The published analytic statements and the archived (G) formulation were checked directly; details are in `data/z49_h4lower/analytic_inputs.md`. After adding Lemma 7b, a separate fresh deep reviewer audited only the new transfer and effectivity changes and returned **SOUND relative to the explicitly stated (G) and internal energy lemma**. It rechecked overlapping moduli, the bounded L¹/mean ratio, auxiliary-prime support, both exceptional terms, the primitive-character correction and the effective parameter choices. The κ<1/6 extension is therefore not silently covered by the earlier reviews of κ<1/12.

**Reproduction:**

```sh
set -euo pipefail
ulimit -v 8000000
timeout 240 env PYTHONPATH=scripts uv run python scripts/z49_h4lower_check.py --mode checks > data/z49_h4lower/checks.json
timeout 300 env PYTHONPATH=scripts uv run python scripts/z49_h4lower_check.py --mode model --samples 10000 > data/z49_h4lower/model.json
timeout 240 env PYTHONPATH=scripts uv run python scripts/z43_astra_check.py > data/z49_h4lower/existing_square_checks.txt
timeout 180 uv run python scripts/omega11_filtration.py 490049 100 > data/z49_h4lower/existing_energy_checks.txt
```

No analytic theorem is certified by finite computation.

**Remaining gap (Assessment).** The requested non-polylogarithmic lower bound is proved by the stated inputs. What remains open is the sharp exponent (in particular the predicted 1/2 extreme scale), a matching exponent-2 Haar tail, and every ES-existence target. No new standard or nonstandard conjecture is assumed in the unconditional theorem.
