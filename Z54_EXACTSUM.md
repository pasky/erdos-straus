# Z54_EXACTSUM — the exact-divisor layer R − G on the Thm U family, exponential-sum angle

Status: z54 depth lane EXACTSUM (brief `z52bbriefs/z53_depth.md`, kickoff `z52bbriefs/z54_lanes.md` § EXACTSUM).
Internal, internally reviewed only (§8). **ES is OPEN; nothing here proves or disproves ES or (★) at any infinite set of
primes.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts
`scripts/z54_exactsum_*`, data `data/z54/exactsum/` (≈ 1 MB). Builds on `Z53_GENUSX.md` (cited **GX**: §1, Lemma 1,
Lemma 2, Theorem X, Lemma 4.1) and `Z53_GENUSLVAL.md` (cited **GL**: Theorem U).

## 0. Summary

* **Question (kickoff).** GX Lemma 4.1 writes the exact family count R_𝔉 as a sum over the free variable w of a
  function of (p mod w, ⌊p/w⌋). The kickoff asks to expand the class condition into exponential sums in w with phase p/w,
  and to find window and frequency ranges where they bound the order-≥3 part T_uw nontrivially. Even |T_uw| = o(log²p)
  on one window family with M_𝔉 ≫ log²p would give (★).
* **Exact decompositions (PROVED, §3).**
  * *Frequency form.* R_𝔉/2 = Σ_q Σ_{a mod* q} W(a,q). Here W(a,q) sums e(a(⌈p/w⌉ + 2)/(2q)) with weight u⁻¹ over the
    free variables (u, w), with q | u.
  * *Conductor form.* R_𝔉 − G_𝔉 = Σ_{f>1} D_f, where D_f collects the primitive non-real characters mod f of the
    level divisor w″.
  * *Squares (Lemma 3.3).* At odd squares, R, G, M and M^cls all vanish. Hence **T_u = T_w = T_uw = 0 at squares**, and
    T1 imposes no constraint on upper bounds for T_uw. In this route the square-sensitive input is Theorem U's lower
    bound for M_𝔉.
* **What exponential sums in p/w control (§4).**
  * *Lemma 4.1 (PROVED relative to an exponent pair (κ, λ) with κ > 0).* Take a dyadic box u ∼ U, k ∼ K
    (k = ⌈p/w⌉ on the shell), with K² ≤ p and 2U ≤ p. The exact number of pairs with f | u, k ≡ c (mod q) and
    k | p + u equals its density up to O(E_{f,q} + 1), where
    E_{f,q} = (p^κK^{λ−κ})^{1/(1+κ)}·f^{−κ/(1+κ)}q^{−λ/(1+κ)} ≤ E := (p^κK^{λ−κ})^{1/(1+κ)}.
  * *Prop 4.3 (windows; PROVED arithmetic).*
    * Some windows satisfy, simultaneously, Theorem U, Theorem X and Lemma 4.1's exponent condition at the worst box.
      Here Theorem X is used with GX's hypothesis (C4) replaced by the weaker inequality (C4′) that its proof actually
      uses.
    * Such windows exist with a classical van der Corput pair. Example: A³B(0,1) = (1/30, 13/15) with
      (α₀, α₁, β, γ) = (0.200, 0.204, 0.7925, 0.7955).
    * Every such window sits in a corner where class hits have level C ≤ p^{(1−2κ−λ)/(4(λ−κ))}. This is ≤ p^{0.025} for
      every non-conjectural pair tabulated, and C ≤ p^{0.0075} in the example.
  * *Certified range.* Lemma 4.1 certifies only the low-conductor blocks; the GX conductor-d blocks need
    d^{(2+κ−λ)/(1+κ)} ≤ p^{−δ}U/E.
    * Explicit window: d ≤ p^{0.00036}.
    * Under the exponent-pair conjecture with K ≈ U: d ≤ U^{1/3}.
    * This is a sufficient range for this implementation, not a proved barrier.
    * Lemma 4.1 concerns the *plain* shell. Its transfer to the GX layers (squarefree w, weights) is Assessment.
* **Scoped no-go (Theorem N, PROVED, §5).** Fix a window with α₁ ≤ β. Consider bounds for the conductor blocks D_f, or
  for the frequency sums W(a,q), that hold uniformly over the integers n ≡ 1 (mod 24) in [P, 2P]. Van der Corput,
  Bombieri–Iwaniec, Huxley and Bourgain bounds are of this kind: they depend on n only through its size.
  * For every prime f ≡ 1 (4) in (U₁/3, U₁] we construct such an n with D_f(n) ≥ 1. The block D_f sees only the single
    integer n + f.
  * Hence such bounds, combined by the triangle inequality, total ≥ (1/3 − o(1))U₁/log U₁ = P^{α₁ − o(1)}. That exceeds
    every power of log P, whereas the target is o(log²P).
* **Falsifier (EVIDENCE, §6).**
  * Data: 1 000 random primes p ≡ 1 (24) at 10⁹–10¹⁴, near-squares, 150 odd squares, 50 composites, the 14 (★)-zero
    primes and the item-14 test primes.
  * In dyadic u-slices, blocks fed by one integer p + u carry 0.90–1.03 of var(R − G). Blocks fed by ≤ 3 integers,
    taken together, carry 0.96–1.02; blocks fed by ≥ 16 integers carry ≤ 0.003.
  * Conductors f < u^{1/2}, taken together, carry ≤ 1.7 % of var(R − G) in every window tested.
  * For q ≥ 11 the frequency sums W(a,q) have median rms_a|W| equal to 0.98–1.04 × the random-phase benchmark √(Σu⁻²).
  * At the (★)-zero primes with G > 0, the deficit R − G = −G sits predominantly at the top conductor f = u.
  * Across u, var(R − G)/mean(Σ_u t_u²) = 0.83–1.19: the per-u terms look uncorrelated, i.e. random-model
    cancellation only.
* **Verdict: narrowed.**
  * *Dead as a scoped theorem.* Bounding the kickoff's exponential sums block by block with n-uniform estimates fails by
    P^{α₁−o(1)} (Theorem N).
  * *Proved, small.* Lemma 4.1 and Prop 4.3 give low-conductor control of the plain shell on windows compatible with
    Theorems U and X. That control certifies only a negligible part of the measured variance (EVIDENCE).
  * *Survives (Assessment).* Cross-u cancellation inside dyadic slices, i.e. among the different integers p + u: B2 in
    tied form.
* **ES remains OPEN.**

## 1. Setting and the precise statements attacked

Notation of GX §1.
* p ≡ 1 (4) is prime. Windows: U_i = p^{α_i}, Y = p^β, X = p^γ, with 8U₁X ≤ p and Y ≥ U₁.
* 𝒰 = {u squarefree : u ≡ 1 (4), U₀ < u ≤ U₁} and 𝒮_u = {w odd squarefree : gcd(w, up) = 1}.
* The shell is 𝔖 = {(u, w) : u ∈ 𝒰, w ∈ 𝒮_u ∩ (Y, X], w | p + u}. On it, w″ = (p + u)/(2w) is odd and
  k := 2w″ = ⌈p/w⌉ (GX Lemma 4.1).
* GX §1 (level form):
  * R_𝔉 = 2#{𝔖 : w″ ≡ −1 (mod 4u)};
  * G_𝔉 = Σ_𝔖 (2·2^{ω(u)}/φ(u))·1[w″ ≡ 3 (4), −w″ ∈ □ (mod u)].
* GX Lemma 1: X_𝔉 = R_𝔉 − M_𝔉 = T_u + T_w + T_uw and R_𝔉 − G_𝔉 = T_u + T_uw. On Theorem X windows,
  T_u = O(p^{−δ}log p).

When an odd n ≡ 1 (4) replaces p (controls; §5), the same formulas are used with gcd(u, n) = 1 and gcd(w, un) = 1.

**Targets (CONJECTURE-strength; not claimed).**
* (X-uw): T_uw ≥ −(1 − ε)M_𝔉 + o(log²p) on some window family with M_𝔉 ≫ log²p. With (X-w) and Theorem X this gives
  (★) for all large p (GX §1).
* (X-uw)₂: the two-sided |T_uw| = o(log²p).

**What this lane attacks** (the kickoff's programme):
1. expand the class condition (r_w = u, ⌈p/w⌉ ≡ −2 (8u)) into exponential sums over the free variables, with phase p/w
   and frequencies h/(8u);
2. determine which window and frequency ranges admit nontrivial bounds, and prove a theorem there or the exact scoped
   no-go;
3. run a falsifier at 10⁹–10¹⁴.

## 2. Why this is not already closed

* GX controls the density layer T_u (Theorem X) and proves structure identities for the exact layers. It decomposes them
  neither by frequency nor by conductor, and says nothing about exponential sums in w or about window compatibility.
* The closed "low-conductor universality" item (FRONTIER §7.1) concerns smooth hyperbola blocks and the pair modulus m.
  This lane concerns other objects: characters mod u of the level divisor on the *exact shell* of the Thm U family. It
  asks two questions not treated there:
  * which of those conductors exponential sums in p/w can control on windows where Theorems U and X also hold (§4);
  * where the variance and the deficit live (§6).
* HYPKLOOST Thm B (frequency certificates of degree < q_max/2 have mean ≤ 0) concerns positive-mean certificates for the
  full count. Theorem N (§5) concerns n-uniform bounds for the conductor and frequency blocks of the exact layer, a
  different class of arguments.

## 3. Exact frequency and conductor decompositions (PROVED)

**Proposition 3.1 (frequency form).** Let Y ≥ U₁. Then
  R_𝔉/2 = Σ_{q odd squarefree} Σ_{a mod q, (a,q)=1} W(a, q),
  W(a, q) := Σ_{u∈𝒰, q|u} u^{−1} Σ_{w ∈ 𝒮_u∩(Y,X], w | p+u, ⌈p/w⌉ ≡ 6 (8)} e(a(⌈p/w⌉ + 2)/(2q)).

*Proof.*
1. On 𝔖, ⌈p/w⌉ = 2w″ (GX Lemma 4.1; this uses Y ≥ U₁). Since u is odd,
   w″ ≡ −1 (4u) ⟺ [w″ ≡ 3 (4) and u | w″ + 1] ⟺ [⌈p/w⌉ ≡ 6 (8) and u | (⌈p/w⌉ + 2)/2].
2. Expand 1[u | m] = u^{−1}Σ_{h mod u} e(hm/u). Writing h/u = a/q in lowest terms, q runs over the divisors of u and a
   over (ℤ/q)^×.
3. Sum over 𝔖 and exchange the order of summation. Divisors of squarefree u are odd and squarefree. ∎

*Reading.* In W(a,q), u runs over the progression u ≡ 0 (q) in 𝒰 and w over the divisors of p + u in (Y, X]. The phase
is a(⌈p/w⌉ + 2)/(2q) = a/q + a(p + u)/(2qw), i.e. phase p/w at frequency a/(2q): the kickoff's h/(8u) reduced to lowest
terms. The factor e(a/q) does not affect |W(a,q)| but matters when summing over a. Two pieces are worth naming:
* the q = 1 term, which is the plain shell sum Σ_u u^{−1}#{w : ⌈p/w⌉ ≡ 6 (8)};
* the conductor-q block P_q := Σ_{a mod* q} W(a,q) = Σ_{u: q|u} u^{−1}Σ_w c_q(w″ + 1), where c_q is the Ramanujan sum.

**Proposition 3.2 (conductor form).** For odd squarefree f and gcd(m, f) = 1 put
  Φ*_f(m) := Σ_{χ primitive mod f, χ non-real} χ(m) = ∏_{ℓ|f}((ℓ − 1)1[m ≡ 1 (ℓ)] − 1) − (m/f)   (Jacobi symbol).
Then Φ*_1 = 0 and
  R_𝔉 − G_𝔉 = Σ_{f>1} D_f,  D_f := Σ_{(u,w)∈𝔖, f|u} (2/φ(u))·1[w″ ≡ 3 (4)]·Φ*_f(−w″).

*Proof.* Let u be odd squarefree and gcd(m, u) = 1.
1. Every χ mod u is induced by a unique primitive χ* mod some f | u, and χ(m) = χ*(m).
2. A primitive character mod squarefree f is a product of non-trivial characters mod the primes ℓ | f. Hence
   Σ_{χ prim mod f} χ(m) = ∏_{ℓ|f}((ℓ − 1)1[m ≡ 1 (ℓ)] − 1).
3. The real primitive character mod f is unique: the Jacobi symbol (·/f) for f > 1, the trivial character for f = 1.
   So Σ_{f|u}Σ_{χ prim mod f, real} χ(m) = Σ_{f|u}(m/f) = ∏_{ℓ|u}(1 + (m/ℓ)) = 2^{ω(u)}1[m ∈ □ (u)].
4. Hence φ(u)1[m ≡ 1 (u)] − 2^{ω(u)}1[m ∈ □ (u)] = Σ_{f|u} Φ*_f(m).
5. Take m = −w″ (gcd(w″, u) = 1 by GX Lemma 4.4), multiply by (2/φ(u))1[w″ ≡ 3 (4)] and sum over 𝔖. The left side
   becomes R_𝔉 − G_𝔉 by the level forms of §1. ∎

CERTIFIED: Σ_f D_f = R − G at every shell point of every run in §6 (max error 4.4·10⁻¹⁶).

**Lemma 3.3 (all layers vanish at odd squares).** Let n = m² be an odd square, with the family taken at n. Then
R_𝔉(n) = G_𝔉(n) = 0. With GX §3 Remark 3 (M^cls_𝔉(m²) = 0, and M_𝔉(m²) = 0 termwise) it follows that
T_u = T_w = T_uw = 0 at n.

*Proof.* Take a shell point with w″ ≡ 3 (4).
1. gcd(w″, n) = 1: a common prime divides n + u − 2ww″ = u, but gcd(u, n) = 1.
2. u = 2ww″ − n ≡ −n (mod w″), so (u/w″) = (−1/w″)(m/w″)² = −1 (Jacobi symbols).
3. Jacobi reciprocity (u ≡ 1 (4)) gives (w″/u) = (u/w″) = −1, so (−w″/u) = (−1/u)(w″/u) = −1.
4. Hence −w″ is not a square mod every ℓ | u, and the genus indicator vanishes.
5. Class hits lie in the genus, so R(n) = 0. ∎

*Consequence (Assessment).*
* T1 imposes no constraint on upper bounds for |T_uw|: the T_uw target is T1-neutral.
* In this route the square-sensitive input is Theorem U's lower bound M_𝔉 ≫ log²p. It uses primality, since p divides
  the conductor of η·χ_{−4up}.
* It does not follow that a T_uw bound may ignore primality. Composite non-square n with R_𝔉(n) = 0 and G_𝔉(n) large are
  not excluded (none is known to us), and Theorem X is proved only for prime p.

## 4. What exponential sums in p/w can control

**Exponent pairs.** We use the standard definition (Graham–Kolesnik Ch. 3; Trudgian–Yang arXiv:2306.05599 §1.1). Sources
are checked in `data/z54/exactsum/LIT_CHECK.md`. An exponent pair (κ, λ) satisfies 0 ≤ κ ≤ 1/2 ≤ λ ≤ 1, and the
following holds.
* *Phase class.* For s > 0, the phase class contains every φ on (N, 2N] whose derivatives satisfy
  φ^{(r+1)}(x) = (d/dx)^r(y x^{−s})·(1 + O(ε₀)), r < R₀.
* *Bound.* For every such φ with y ≥ N^s, and uniformly over subintervals I ⊂ (N, 2N],
  Σ_{n∈I} e(φ(n)) ≪_{κ,λ} (y/N^s)^κ N^λ.
* *Use here.* We take s = 2. For a phase with φ′ ≈ −y x^{−2} the definition is applied to −φ; complex conjugation does
  not change the absolute value.

Pairs used:
* A^nB(0,1) = (1/(2^{n+2} − 2), 1 − (n+1)/(2^{n+2} − 2)), classical van der Corput; e.g. (1/6, 2/3), (1/14, 11/14),
  (1/30, 13/15);
* Huxley–Watt (9/56 + ε, 37/56 + ε), Proc. LMS 57 (1988);
* Huxley (32/205 + ε, 269/410 + ε), Proc. LMS 90 (2005);
* Bourgain (13/84 + ε, 55/84 + ε), JAMS 30 (2017), Thm 6.

**Lemma 4.1 (dyadic shell count in progressions; PROVED relative to an exponent pair (κ, λ) with κ > 0).**
*Hypotheses.*
* q ≥ 1, f | q with f odd, and c ∈ ℤ with gcd(c, f) = 1.
* U, K ≥ 1 with 2U ≤ p and K² ≤ p.
* Put E_{f,q} := (p^κK^{λ−κ})^{1/(1+κ)}·f^{−κ/(1+κ)}q^{−λ/(1+κ)} and
  H* := (K^{1−λ+2κ}p^{−κ}f^κq^{λ−1−κ})^{1/(1+κ)}. Assume H* ≥ 1 and K ≥ qJ₀, where J₀ = J₀(κ, λ) is large enough for
  the derivative closeness below and the dyadic splitting.

*Statement.* Put
  N_c := #{(u, k) : U < u ≤ 2U, f | u, K < k ≤ 2K, k ≡ c (mod q), k | p + u}.
Then
  N_c = (U/f)·Σ_{K<k≤2K, k≡c (q)} 1/k + O_{κ,λ}(E_{f,q} + 1).
In particular the error is ≤ O(E + 1) with E := (p^κK^{λ−κ})^{1/(1+κ)}, uniformly in q, f and c.

*Proof.*
1. *Reduction to a sawtooth sum.* Fix k ≡ c (q); then gcd(k, f) = 1. Write u = fv with v ∈ (A, B], A = U/f, B = 2U/f.
   Then k | p + fv ⟺ v ≡ v_k := −p f̄ (mod k), where f̄ is the inverse of f mod k. With ψ(x) = x − ⌊x⌋ − 1/2,
   #{v ∈ (A,B] : v ≡ v_k (k)} = (B − A)/k − ψ((B − v_k)/k) + ψ((A − v_k)/k).
2. *Reciprocity.* f̄/k + k̄/f ≡ 1/(fk) (mod 1), where k̄ is the inverse of k mod f; the numerator ff̄ + kk̄ − 1 vanishes
   mod f and mod k. Hence −v_k/k ≡ p f̄/k ≡ p/(fk) − p k̄/f (mod 1).
   * Since f | q, the residue k̄ mod f depends only on c. So θ_c := p c̄/f (mod 1) is constant on the progression.
   * Therefore N_c − (U/f)Σ 1/k = S(p + U) − S(p + 2U), where S(Z) := Σ_{K<k≤2K, k≡c (q)} ψ(Z/(fk) − θ_c).
   * Here p ≤ Z ≤ 2p, because 2U ≤ p.
3. *Vaaler.* For H ≥ 1, Vaaler's trigonometric approximation to ψ gives
   |S(Z)| ≤ (K/q + 1)/(2H + 2) + Σ_{1≤h≤H}(1/(πh) + 1/(H + 1))|T_h|,  T_h := Σ_{K<k≤2K, k≡c (q)} e(hZ/(fk)).
   (The constant θ_c multiplies T_h by a unimodular factor.)
4. *Exponent-pair bound for T_h.* Write k = c₀ + qj with 1 ≤ c₀ ≤ q. The phase is φ(j) = y·(j + c₀/q)^{−1} with
   y = hZ/(fq), and j runs over at most two pieces of dyadic ranges (J, 2J], J ≍ K/q.
   * −φ′(x) = y(x + c₀/q)^{−2}. Its derivatives are within a factor 1 + O(1/J) of those of y x^{−2}, so −φ lies in the
     class for J ≥ J₀.
   * Scale: y/J² ≍ hZq/(fK²) ≥ 1, since Z ≥ p ≥ K² and q ≥ f.
   * Hence |T_h| ≪ (hZq/(fK²))^κ (K/q)^λ ≤ 2h^κ p^κ f^{−κ} K^{λ−2κ} q^{κ−λ}.
   * Since K ≥ qJ₀, each piece lies in a dyadic range (N, 2N] with N ≥ J₀/2. The exponent-pair bound is uniform over
     subintervals, so short boundary pieces need no separate treatment.
5. *Summation over h.* Since κ > 0, Σ_{h≤H}(1/h + 1/H)h^κ ≪_κ H^κ. Hence
   |S(Z)| ≪ (K/q)/H + 1 + H^κ p^κ f^{−κ} K^{λ−2κ} q^{κ−λ}.
6. *Choice of H.* Take H := ⌊H*⌋ ≥ 1. Then (K/q)/H ≍ E_{f,q} and H^κ p^κ f^{−κ}K^{λ−2κ}q^{κ−λ} ≍ E_{f,q}, by direct
   substitution. The last claim holds because f, q ≥ 1 and κ, λ ≥ 0. ∎

**Corollary 4.2 (low-conductor plain blocks).** Assume Lemma 4.1's hypotheses for every c coprime to q. Let g be a
function on (ℤ/q)^× with |g| ≤ 1 and mean ĝ₀. Then
  Σ_{U<u≤2U, f|u} Σ_{K<k≤2K, (k,q)=1, k|p+u} g(k) = ĝ₀ (U/f)(φ(q)/q) log 2 + O(φ(q)(E_{f,q} + 1) + φ(q)U/(fK)).
*Proof.* Sum Lemma 4.1 over c, using Σ_{k≡c (q), K<k≤2K} 1/k = (log 2)/q + O(1/K) uniformly in c. ∎

The main term of a block is ≍ (U/f)(φ(q)/q). The corollary therefore *certifies* a block whenever
q(E_{f,q} + 1) ≤ p^{−δ}U/f, i.e. f^{1/(1+κ)}q^{(1+κ−λ)/(1+κ)} ≤ p^{−δ}U/E and q ≤ p^{−δ}U/f. This is the range this
implementation certifies. It is not a proved barrier for other arguments.

**Proposition 4.3 (window reconciliation; PROVED arithmetic, `scripts/z54_exactsum_window.py` →
`data/z54/exactsum/window_check.txt`).** Parameters: r ≥ 3 an integer, 0 < ε < 1/100, and τ := (r + 1)/(4r) + rε. This
is the inflated τ of GL §2.7 and GX Theorem X; GL's theorem statement uses the uninflated τ_r with margins.

(a) *Theorem X under (C4′).* In GX's proof of Theorem X, hypothesis (C4) α₁ < 1/5 is used only in step (i), to deduce
(C4′): (1/2 − ε)(β − α₁) ≥ α₁ + ε/2. So Theorem X holds under (C1), (C2*) and (C4′).

(b) *Reconciled windows exist.* Let 𝔚(κ,λ) be the set of windows satisfying:
* Theorem U: (C1) γ < 1 − α₁, (C2) β > τ(1 + α₁) + 4ε, (C3) α₀ > τ²(1 + α₁) + 3ε;
* Theorem X: (C2*) β > 2α₁ + τ + 4ε and (C4′);
* α₀ < α₁ ≤ β < γ;
* (E) κ + (λ − κ)(1 − β) < α₀(1 + κ).

Condition (E) is Lemma 4.1's condition E ≤ U p^{−η} at the worst box U = p^{α₀}, K = p^{1−β}. The dual range is
k ∈ (p^{1−γ}, 2p^{1−β}]; on it K² ≤ p and K > U hold for large p (dyadic endpoints cost factors 2).

𝔚(1/30, 13/15) ≠ ∅. Example: (α₀, α₁, β, γ) = (0.200, 0.204, 0.7925, 0.7955), r = 100, ε = 10⁻⁵, τ = 0.2535.
* All conditions hold exactly in rationals. The slacks, in script order, are 0.0005, 0.4872, 0.1226, 0.1310, 0.0902,
  0.003, 0.004 and 1/2400 (reviewer's independent recomputation).
* η = 1/2480 ≈ 0.0004.
* H* ≥ 1 for f = q = 1 holds at every box, with the hardest case at the smallest K: (1 − λ + 2κ)(1 − γ) = 0.0409 ≥ κ =
  0.0333.
* Window constant: c = (8/π⁴)(γ − β)(α₁ − α₀) ≈ 9.86·10⁻⁷ > 0.

(c) *Shape.*
* (C1) and (C2*) force α₁ < 1/4.
* Since 1 − β > α₁ > α₀ and the left side of (E) increases in 1 − β, (E) forces α₀ > κ/(1 + 2κ − λ). By pair:
  * A^nB: 1/(n + 3);
  * Huxley–Watt: 9/37;
  * Bourgain: 13/55 (limiting values as the pair's ε → 0).
* Solving (E) gives 1 − β − α₀ < (α₀(1 + 2κ − λ) − κ)/(λ − κ). With α₀ < 1/4 this is < (1 − 2κ − λ)/(4(λ − κ)). The
  bound is 0.025 for A²B, 0.020 for A³B, ≤ 0.018 for Huxley–Watt, Huxley and Bourgain, and 1/4 under the exponent-pair
  conjecture.
* Every class hit has level C = (w″ + 1)/(4u) ≤ (1 + o(1))p^{1−β−α₀}. So on reconciled windows from these pairs,
  C ≤ p^{0.025}; in the example C ≤ p^{0.0075}.

(d) *Certified conductors for the GX blocks.* A conductor-d block D_d (Prop 3.2) requires f = d, and a function of
k mod 8d (it fixes w″ = k/2 mod 4d, hence both w″ mod 4 and the character of w″ mod d), so q = 8d. Apply Lemma 4.1 to
the classes c mod 8d with gcd(c, d) = 1. By the criterion after Cor 4.2 it is certified when
d^{(2+κ−λ)/(1+κ)} ≪ p^{−δ}U/E.
* In the example, (2 + κ − λ)/(1 + κ) = 35/31, so d ≤ p^{0.00036}.
* Under the exponent-pair conjecture (κ, λ) → (0, 1/2) with K ≈ U: U/E ≈ U^{1/2}, so d ≤ U^{1/3}.
* The inequality E ≥ K^{(κ+λ)/(1+κ)} ≥ K^{1/2} (using p ≥ K² and λ ≥ 1/2) is correct. Following the review, it is not
  turned into a barrier.

*What this buys (scoped).* On 𝔚 windows:
* T_u = O(p^{−δ}log p) (Theorem X);
* M_𝔉 ≥ (c − o(1))log²p (Theorem U);
* the *plain* shell, twisted by characters of conductor ≤ p^{η′}, matches its density with a power saving (Cor 4.2).

*Transfer (Assessment, not carried out).* The GX layers carry, beyond Cor 4.2:
* the weights 2^{ω(u)}/φ(u) and squarefree u, which reduce to divisor expansions with small moduli plus trivial tails;
* the congruence w″ ≡ 3 (4);
* *squarefree w*. This needs a count of integers in (p + U, p + 2U] divisible by e² with e > p^{η}, of
  Filaseta–Trifonov type, with U = p^{0.2}. That input is not verified here.

If the transfer holds, then on these windows X_𝔉 reduces to the conductor > p^{η′} parts of T_w and T_uw. By §6 that is
essentially all of the measured variance.

## 5. Top conductors are single integers: the scoped no-go (PROVED)

Fix window exponents 0 < α₀ < α₁ ≤ β < γ. For a large parameter P put U_i = P^{α_i}, Y = P^β and X = P^γ, and assume
8U₁X ≤ P, U₁ > 3U₀ and X ≥ 12Y. For odd n ∈ [P, 2P] with n ≡ 1 (24), form 𝔖(n), D_f(n) and W(a,q)(n) with this fixed
window. Here Y ≥ U₁, so Prop 3.1 applies at n.

**Theorem N.** There is P₀ (depending on the exponents) with the following property. For P ≥ P₀ and every prime
f ≡ 1 (mod 4) with U₁/3 < f ≤ U₁, some n ∈ [P, 2P] with n ≡ 1 (mod 24) satisfies D_f(n) ≥ 1 and
P_f(n) = Σ_{a mod* f} W(a,f)(n) ≥ 1/2. Consequently:
(a) If |D_f(n)| ≤ B_f for all f > 1 and all such n, then Σ_f B_f ≥ (1/3 − o(1))U₁/log U₁.
(b) If |W(a,q)(n)| ≤ B_{a,q} for all such n, then Σ_{q>1}Σ_{a mod* q} B_{a,q} ≥ (1/6 − o(1))U₁/log U₁.
Both totals are P^{α₁ − o(1)}, which exceeds every fixed power of log P. For comparison, the target is
|T_uw| = o(log²P) for primes on Theorem U windows, where M_𝔉(p) ≥ (c − o(1))log²p. In the data R − G fluctuates by
≍ √(R + G) (§6).

*Proof.*
1. *Only u = f feeds the block.* Since f ≡ 1 (4) and every u ∈ 𝒰 is ≡ 1 (4), a multiple u = fv ∈ 𝒰 has v ≡ 1 (4). So
   u = f or u ≥ 5f > U₁. Hence D_f and P_f involve only u = f, i.e. only the integer n + f.
2. *Choice of w.* Choose a prime w ∈ (Y, 2Y] ⊂ (Y, X/6] with w ≡ −(1 + f)/2 (mod 4); this is an odd class. It exists
   for P ≥ P₀ by the prime number theorem in progressions mod 4. Then w > Y ≥ U₁ ≥ f and w > 3.
3. *Choice of w″.* Choose w″ such that:
   * w″ ≡ −1 (mod 4f);
   * w″ ≡ (1 + f)(2w)^{−1} (mod 3) (f ≠ 3, 3 ∤ w);
   * (P + f)/(2w) ≤ w″ ≤ (2P + f)/(2w).

   The congruences fix w″ modulo 12f. The interval has length P/(2w) ≥ 3P/X ≥ 24U₁ > 12f, because X ≤ P/(8U₁). So such
   a w″ exists.
4. *The integer n.* Put n := 2ww″ − f ∈ [P, 2P].
   * n ≡ 1 (3) by the choice of w″ mod 3.
   * n ≡ 1 (8): w″ ≡ 3 (4) and w ≡ −(1 + f)/2 (4) give ww″ ≡ (1 + f)/2 (4), so 2ww″ ≡ 1 + f (8).
5. *Membership in the family.*
   * gcd(f, n) = gcd(f, 2ww″) = 1, since w″ ≡ −1 (f) and w ≠ f.
   * gcd(w, n) = gcd(w, f) = 1.
   * w is an odd prime in (Y, X] dividing n + f = 2ww″. So (f, w) ∈ 𝔖(n), with level divisor w″ ≡ −1 (mod 4f): a class
     hit.
6. *Value of D_f.* For prime f, a shell point of u = f with w″ ≡ 3 (4) contributes (2/(f − 1))(a − (s/f)), where
   s ≡ −w″ (mod f), a = f − 2 if s ≡ 1, and a = −1 otherwise.
   * The hit contributes 2(f − 3)/(f − 1).
   * Each other point contributes ≥ −4/(f − 1), and there are at most τ(n + f) − 1 of them.
   * So D_f(n) ≥ 2 − 4τ(n + f)/(f − 1) ≥ 1 once f ≥ 4τ(n + f) + 1. This holds for P ≥ P₀, since
     τ(N) ≤ N^{O(1/log log N)} and f > P^{α₁}/3.
7. *Value of P_f.* Here P_f(n) = f^{−1}Σ_{w′} c_f(w′″ + 1), with c_f(m) = f·1[f | m] − 1. So
   P_f(n) ≥ (f − τ(n + f))/f ≥ 1/2.
8. *Consequences.* (a) follows from B_f ≥ D_f(n_f) ≥ 1 and the prime number theorem mod 4 on (U₁/3, U₁]. For (b),
   Σ_a B_{a,f} ≥ Σ_a |W(a,f)(n_f)| ≥ |P_f(n_f)| ≥ 1/2. ∎

*Numerical check (reviewer).* (P, U₀, U₁, Y, X) = (10⁹, 10, 200, 1000, 625000), f = 197, w = 1009, w″ = 495651 give
n = 1000223521 with D₁₉₇ = 1.918 and P₁₉₇ = 0.959.

**Scope.**
* *Excluded.* Any bound on R − G (hence on T_uw) of the form Σ_f (n-uniform bound for |D_f|) or Σ_{a,q} (n-uniform bound
  for |W(a,q)|). This covers bounding the kickoff's exponential sums one frequency or conductor at a time by any
  estimate that depends on n only through its size.
* *Not excluded:*
  * bounds that use arithmetic of the prime p (e.g. Legendre-symbol cancellation, as in Theorems U and X);
  * one-sided estimates;
  * bounds that combine several blocks before taking absolute values (cross-u cancellation), e.g. an n-uniform bound on a
    whole dyadic slice Σ_{u∼U} t_u(n);
  * transformations other than the frequency or conductor decomposition.
* Theorem N exhibits one subclass of single-integer blocks: prime f > U₁/3. Blocks with composite f, or with f ≤ U₁/3,
  are not covered by the construction.

*What survives (Assessment).* Let t_u(n) be u's contribution to R − G. A dyadic slice T^{(U)} = Σ_{u∼U} t_u(n) sums over
≍ U different integers n + u, recording in which class mod 4u the level divisors of n + u fall; the modulus moves with
the shift. Bounding it requires cancellation across those integers, i.e. B2 in tied form. Exponential sums enter only
after a divisibility is expanded into complete sums (Kloosterman fractions, reciprocity). That is the HYPKLOOST route,
whose standard implementations are scoped there.

## 6. Falsifier: conductor profile and frequency-sum sizes at 10⁹–10¹⁴ (EVIDENCE; identities CERTIFIED)

**Engines and commands.**
* *Conductor profile.* Engine `scripts/z54_exactsum_cond.c` (`gcc -O2 -o /tmp/z54es scripts/z54_exactsum_cond.c -lm`);
  driver `scripts/z54_exactsum_run.py OUT TAG WINDOW @list`.
  * Windows: std (U₀ = p^{1/12}, U₁ = p^{1/3}/2, Y = p^{1/3}, X = p^{2/3}/4) and thx (α₁ = 19/120, α₀ = (1 + α₁)/16,
    β = 2α₁ + 1/4, X = p^{1−α₁}/8, i.e. the limiting Theorem X optimum).
  * Dyadic slices: dyad (u ∈ (U₁/2, U₁], U₁ = p^{1/3}/2) and dyad16 (U₁ = p^{1/3}/32).
  * None of these is a reconciled 𝔚 window: those are numerically empty at feasible p, since c ≈ 10⁻⁶. Extrapolating
    the data to 𝔚 windows is Assessment.
  * For each n the engine enumerates the shell (segmented factorisation of n + u) and accumulates every D_f.
  * Mass is bucketed by relative conductor ρ = log f/log u and by m_f = #{u ∈ 𝒰 : f | u}, the number of integers n + u
    feeding block f.
  * Statistics: `scripts/z54_exactsum_stats.py` → `data/z54/exactsum/stats_profile.txt`. Merged buckets are variances of
    the *summed* bucket, covariances included.
* *Frequency sums.* `scripts/z54_exactsum_wsum.c` computes W(a,q) for odd q ≤ 99; `scripts/z54_exactsum_wstats.py` →
  `wsum_std_summary.txt`.

**Samples.**
* Random primes p ≡ 1 (24) in [10^k, 2·10^k]: the GX lists at k = 9…12 (200, 200, 150, 150), and 150 new ones each at
  k = 13, 14 (`scripts/z54_exactsum_primes.py`, seed 5400). The reviewer verified all 1 000 as distinct primes
  ≡ 1 (24).
* Controls: 60 near-squares each near 10¹⁰ and 10¹²; 150 odd squares; 50 composites near 10¹⁰ (GX lists).
* The 14 (★)-zero primes and the item-14 test primes 193, 2521, 66529, 3361, 5101441 (`prof_hard_std.tsv`).

**Identity.** Σ_f D_f = R − G at every shell point of every run, max error 4.4·10⁻¹⁶ (CERTIFIED to rounding). R and G
agree with GX's engine on the tested primes.

**Variance by block** (fractions var(bucket)/var(R − G) across random primes; merged buckets include covariances):

| window | scale | var(R−G) | var/mean(R+G) | f = u | ρ < 1/2 | m_f = 1 | m_f ≤ 3 | m_f ≥ 16 |
|---|---|---|---|---|---|---|---|---|
| dyad | 10¹⁰ | 0.85 | 0.96 | 0.71 | 0.009 | 0.90 | 0.96 | 0.001 |
| dyad | 10¹² | 0.82 | 0.80 | 1.01 | 0.006 | 1.03 | 1.00 | 0.003 |
| dyad | 10¹⁴ | 1.62 | 1.18 | 0.72 | 0.002 | 0.97 | 0.99 | 0.002 |
| dyad16 | 10¹² | 0.95 | 0.89 | 0.86 | 0.012 | 0.95 | 0.99 | 0.000 |
| dyad16 | 10¹⁴ | 1.23 | 0.92 | 0.73 | 0.006 | 0.97 | 0.97 | 0.001 |
| std | 10¹⁰ | 6.49 | 1.07 | 0.83 | 0.009 | 0.28 | 0.55 | 0.080 |
| std | 10¹² | 8.28 | 0.85 | 1.00 | 0.008 | 0.19 | 0.41 | 0.33 |
| std | 10¹⁴ | 12.74 | 0.87 | 0.80 | 0.007 | 0.28 | 0.41 | 0.45 |
| thx | 10¹² | 2.31 | 0.87 | 0.79 | 0.005 | 0.58 | 1.00 | 0 |
| thx | 10¹⁴ | 3.56 | 0.87 | 0.81 | 0.008 | 0.44 | 0.93 | 0 |

Full table (all scales, near-squares, composites, hard primes): `stats_profile.txt`.

**Readings.**
* Across all dyadic-slice samples: m_f = 1 carries 0.90–1.03, m_f ≤ 3 carries 0.96–1.02, and m_f ≥ 16 carries ≤ 0.003.
* Over all groups, ρ < 1/2 carries ≤ 0.017 (maximum 0.0163, std composites).
* In the standard window the long blocks (m_f ≥ 16) carry a growing share, 0.08 → 0.45 from 10¹⁰ to 10¹⁴. Each long
  block is dominated by its smallest u, because the weights are 1/φ(u). The dyadic slices remove this effect.
* The ratio var(R − G)/mean(R + G) lies in 0.84–1.07 (std), 0.80–1.18 (dyad), 0.84–1.00 (dyad16) and 0.55–0.87 (thx),
  roughly swap-Poisson.
* The per-u triangle ratio mean(Σ_u|t_u|)/mean(R + G) is 0.84–0.90 (std), 0.99–1.00 (dyad) and 0.52–0.82 (thx): little
  cancellation inside a single u.

**Cross-u structure (the survivor; `data/z54/exactsum/diag_crossu.txt`).** Let t_u be u's part of R − G. Compare
var(R − G) = var(Σ_u t_u) with the diagonal mean(Σ_u t_u²), over the same random primes.
* Ratios: 1.19, 0.97, 0.92 (std, at 10¹⁰, 10¹², 10¹⁴) and 0.99, 0.83, 1.15 (dyad); mean(R − G) is within ±0.44.
* Within sampling error (150–200 primes per cell), the per-u terms behave as uncorrelated with mean ≈ 0. The data show
  no systematic cross-u (anti)correlation that a structural argument could exploit.
* So the slice sums cancel only at the square-root (random-model) level: |R − G| ≈ √(Σ_u t_u²) ≍ log p against the
  target o(log²p).
* Assessment: proving even this weaker-than-needed cancellation across the integers p + u is the B2 content of the
  survivor.

**Odd squares.** R = G = 0, and indeed the conductor pieces cancel across f | u at each shell point (Lemma 3.3). They do
not cancel blockwise: mean Σ_f |D_f| is 3.31 (std window) and 0.96 (dyadic).

**(★)-zero primes** (std window). G > 0 at 329617, 712321, 1134241, 1724209, 1726201, 5212561 and 8813281. At 83449 and
102001 the shell has one point each but R = G = 0. Where G > 0 we have R − G = −G, carried predominantly by f = u
(0.67–1.01 of it) and entirely by blocks fed by ≤ 3 integers. At p = 5101441 (item 14), R − G = +0.48.

**Frequency sums W(a,q)** (30 primes each at 10¹² and 10¹⁴, std window; medians over (p, q)):

| scale | q | #terms | max_a|W|/W_triv | rms_a|W| / √(Σu⁻²) | |P_q|/W_triv |
|---|---|---|---|---|---|
| 10¹² | 3–9 | 230 | 0.36 | 1.97 | 0.35 |
| 10¹² | 11–29 | 74 | 0.40 | 1.01 | 0.63 |
| 10¹² | 31–99 | 19 | 0.61 | 0.98 | 1.00 |
| 10¹⁴ | 3–9 | 1293 | 0.31 | 2.83 | 0.40 |
| 10¹⁴ | 11–29 | 427 | 0.28 | 1.04 | 0.42 |
| 10¹⁴ | 31–99 | 116 | 0.37 | 0.99 | 0.67 |

Here W_triv = Σ u⁻¹ is the trivial bound. For q ≥ 11 the median rms is 0.98–1.04 × the random-phase benchmark. For
q ≤ 9 there is an excess (2–2.8×), which we have not analysed. The square controls at the head of the squares list are
near 10⁸ and have 2–5 terms per q, so they are uninformative here.

**Reading (EVIDENCE).**
* The class-within-genus layer fluctuates roughly like swap-Poisson draws.
* In dyadic slices its variance sits in conductor blocks that each see one (or at most three) integers p + u.
* The low-conductor part, which exponential sums in p/w certify (§4), carries ≤ 1.7 % of the variance in every window
  tested.
* Across u, the per-u terms look uncorrelated, so the slice sums show only random-model cancellation.

## 7. Screens, verdict, FRONTIER text, bottom line

**The four FRONTIER §4 hard screens** (for Lemma 4.1/Cor 4.2 on 𝔚 windows, and for the route):
1. *T1 (squares): not binding.* By Lemma 3.3 all of T_u, T_w and T_uw vanish at squares. The route's square-sensitive
   step is Theorem U, which is PROVED. Lemma 4.1 is uniform in n and true at squares, as it must be: it concerns the
   plain shell.
2. *8/131: not applicable.* These are structure and upper-bound statements on the numerator-4 family.
3. *Tied modulus (B2): fails — this is where the route ends.* The variance-carrying blocks are single-integer tied events.
   PROVED for the n-uniform block bounds of Theorem N (prime f > U₁/3); EVIDENCE in §6.
4. *Fixed p: passes.* Every statement holds at fixed p, or uniformly in n.

**Verdict: narrowed.**
* *Dead as a scoped theorem.* Bounding the kickoff's exponential sums frequency by frequency, or conductor by conductor,
  with n-uniform estimates and the triangle inequality, costs ≥ P^{α₁−o(1)} (Theorem N).
* *Strengthened (small, plain shell only).*
  * Lemma 4.1 and Cor 4.2 control the plain exact shell in progressions, with a power saving uniform in the modulus.
  * Prop 4.3 shows that windows where Theorem U, Theorem X (under (C4′)) and this control coexist exist already with
    classical van der Corput pairs.
  * All such windows sit in the corner C ≤ p^{(1−2κ−λ)/(4(λ−κ))}, which is ≤ p^{0.025} for the tabulated non-conjectural
    pairs.
  * Transferring this control to the GX layers (squarefree w) is Assessment.
* *Survives (Assessment).* Cross-u cancellation within a dyadic slice, among ≍ U different integers p + u with moving
  moduli 4u: B2 in tied form.
  * The certified range of the implementation is conductor d ≤ p^{0.00036} on the explicit window, or ≤ U^{1/3} under the
    exponent-pair conjecture.
  * The variance-carrying blocks have conductor comparable to u.

**Proposed FRONTIER §7 text** (append to item 1, "Genus exact layers"):
> *(z54, `Z54_EXACTSUM.md`, internal review.)* Exponential sums in p/w on the exact layers.
> * *Identities (PROVED).* R_𝔉/2 = Σ_{q, a mod* q} W(a,q), with W(a,q) = Σ_{q|u} u⁻¹ Σ_w e(a(⌈p/w⌉ + 2)/(2q)) over the
>   shell. Also R_𝔉 − G_𝔉 = Σ_{f>1} D_f, where D_f is the part from primitive non-real characters mod f of the level
>   divisor. All of T_u, T_w and T_uw vanish at odd squares, so T1 does not constrain upper bounds for T_uw.
> * *Scoped no-go (PROVED).* n-uniform bounds per conductor block or per frequency (any estimate depending on n only
>   through its size) sum to ≥ (1/6 − o(1))U₁/log U₁. For each prime f ≡ 1 (4) in (U₁/3, U₁], an explicit n gives
>   D_f(n) ≥ 1, and that block sees the single integer n + f.
> * *Positive, plain shell (PROVED relative to an exponent pair).* The dyadic shell count in progressions has error
>   (p^κK^{λ−κ})^{1/(1+κ)}, uniformly in the modulus. Windows satisfying Thm U, Thm X (with (C4) relaxed to the
>   inequality its proof uses) and this control exist with classical pairs, e.g. A³B and
>   (α₀, α₁, β, γ) = (0.200, 0.204, 0.7925, 0.7955). All such windows have level C ≤ p^{0.025}. Transfer to the
>   squarefree-w layers is open.
> * *EVIDENCE (10¹⁰–10¹⁴).* In dyadic u-slices about 90 % or more of var(R − G) sits in conductor blocks fed by one
>   integer p + u, and ≤ 1.7 % sits at conductor < u^{1/2}. For q ≥ 11 the frequency sums have median size equal to the
>   random-phase benchmark.
> * *Survives (Assessment).* Cross-u cancellation: B2 in tied form.

**Bottom line.** The exponential-sum angle on the exact layer of the Thm U family can be carried out, but what it
certifies is not where the difficulty is.
* Exponential sums in p/w control the low-conductor part of the plain shell, and on suitable windows they do so
  compatibly with Theorems U and X.
* The measured variance, the deficit at the (★)-zero primes and the T1 cancellation sit in conductor blocks fed by one
  or a few integers p + u. For such blocks no n-uniform bound can be small (Theorem N, for prime f > U₁/3).
* Assessment: what remains is cancellation across the different shifted integers p + u, i.e. B2 in tied form.

**ES remains OPEN.**

## 8. Review log

**Internal hostile review** (deep-mode subagent; report `data/z54/exactsum/REVIEW_INTERNAL.md`). Verdict "REJECT as
written, with a substantial salvageable core". The exact decompositions, Lemma 3.3, the GX (C4′) relaxation, the
explicit window and Theorem N (with explicit window assumptions) survive.

The reviewer reproduced:
* the saved summaries;
* the window arithmetic, independently in rationals;
* the A^nB pairs;
* the primality of all 1 000 inputs;
* engine runs at three scales;
* the 19 hard inputs, with exact rational genus weights;
* Theorem N's construction numerically (n = 1000223521, D₁₉₇ = 1.918).

Fixes applied:
* R1 (MAJOR) Lemma 4.1 lacked 2U ≤ p (needed for Z ≤ 2p; a CRT counterexample otherwise). Added and propagated.
* R2 Exponent-pair definition: the derivative convention is now stated precisely (applied to −φ). κ > 0 is required.
  λ ≥ 1/2 is part of the standard definition. J₀ is enlarged for the splitting.
* R3 (MAJOR) The "reach fq ≤ U^{1/2}" barrier was a sufficient estimate presented as necessary.
  * Lemma 4.1 now keeps the modulus factors, E_{f,q} = E f^{−κ/(1+κ)}q^{−λ/(1+κ)}.
  * The certified range is stated as such, with no barrier claim.
  * The GX blocks use f = d, q = 8d.
  * The coprimality hypothesis is relaxed to gcd(c, f) = 1, which is all the proof uses.
* R4 τ, r, ε defined locally. The H-condition is checked at the smallest K (0.0409). η ≈ 0.0004 and the slacks are
  recorded.
* R5 (MAJOR) §7 had substituted the example's p^{0.0075} for the general level bound p^{0.025}. Fixed; "u ≈ k/8" replaced
  by the power-range statement.
* R6 (MAJOR) Theorem N now assumes α₁ ≤ β (Y ≥ U₁), which is needed for w > U₁ and for Prop 3.1. "M ≍ log²P" is
  replaced by the prime/Theorem U benchmark. The scope now says one-sided and prime-sensitive estimates are not covered.
* R7 Phase factor e(a/q) restored in the Reading, §0 and the FRONTIER text.
* R8 (MAJOR) Merged buckets were sums of separate variances. They are now recomputed as variances of summed buckets
  (stats script rewritten; table updated).
* R9 (MAJOR) The claims "≥ 98 %", "exactly the blocks of Theorem N" and "can only come from" were removed. Theorem N is
  described as exhibiting a subclass. Cross-u is Assessment. The square cancellation is described as per-shell-point
  across f | u.
* R10 Rounding: "≤ 1.7 %" (max 0.0163), "about 90 % or more" (0.896), and Poisson ratios given per window.
* R11 (MAJOR) The plain-shell versus GX-layer distinction is kept everywhere. The tested windows are not 𝔚 windows, so
  extrapolation is Assessment. Frequency-sum claims are medians, with no "exactly random" and no attribution of the
  low-q excess.
* R12 (★)-zero paragraph: "positive G at …"; the deficit sits "predominantly" at f = u (0.665 at 1724209).
* R13 Stats script: undefined ratios at R + G = 0 are no longer regularised. Squares are reported by mean |bucket|, and
  triangle ratios are ratios of aggregate means.

A cross-model review is to follow.
