# Z54_BILINJAC — depth lane BILINJAC (wave z54, gap 1): bilinear (ℓ, C) cancellation for the square sieve at the balanced block; the quadratic-character (Jacobi-symbol) toolbox

ES is OPEN. Nothing here proves or disproves it. This lane is **upper-bound work only**: even complete success (a power
saving N(balanced) ≪ p^{1/4−η}) would say nothing about positivity of R(p). Its value is the FRONTIER §7.1 benchmark and
the method.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. All results are internal and were
reviewed internally only.

Brief: `z52bbriefs/z53_depth.md` (rules), kickoff `z52bbriefs/z54_lanes.md` §BILINJAC. Predecessor: `Z53_SQSIEVE.md`
(Prop B2, §5.2 Remarks 1–3). Scripts `scripts/z54_bilinjac_*`, data `data/z54/bilinjac/` (< 100 kB). Literature checks:
`data/z54/bilinjac/LIT_CHECK.md` (this lane) and `data/z53/hypkloost/LIT_CHECK.md` (DFI, determinant method).

*Status: full draft, hostile review 1 applied (checkpoint 1 = commit 8003579f; review `reviews/z54_bilinjac_review1.md`).*
**Verdict: narrowed** (§9). In one paragraph:
* The only Jacobi-symbol bilinear form in the problem is the square sieve's (Q, a) form. Two classes of inputs for it
  provably give no saving (Prop M): inputs that see the weights only through the square-class ℓ²-mass, which is how
  Heath-Brown's real-character large sieve sees them, and inputs that see them only through sup-norm, support and range,
  which is how Heath-Brown Cor 4 and other sup-norm bilinear Jacobi bounds see them.
* After Poisson, the (ℓ, C) coefficients are Kloosterman sums, not Jacobi symbols.
* The square sieve at the balanced block reduces sufficiently, with a loss of only Q, to power-saving equidistribution
  of the strip's lattice points modulo small Q (Thm R). This is a twisted short-interval divisor problem at length
  y = x^{1/4}, and its square-root form is a twisted analogue of Jutila's conjecture.
* The literature checked gives no power-saving pointwise bound even for the untwisted strip count. Single-variable
  exponent-pair majorants stop exactly at the trivial exponent.
* Every sum computed is consistent with square-root cancellation (§7).

## 0. Notation (as in SQSIEVE)
(★) 4uBC − u − B = n. The block 𝔅(U,V,W) is u ∈ (U,2U], B ∈ (V,2V], C ∈ (W,2W], and N(U,V,W) is its count; U ≤ V.

*Strip coordinates.* k = uB, s = u + B = 4Ck − n, f(C,k) := s² − 4k (= (u − B)² on solutions).

*Weights and sums.*
* Φ ∈ C_c^∞, 0 ≤ Φ ≤ 1, Φ = 1 on [1,4], supp Φ ⊂ [1/2,5] (SQSIEVE §4.1).
* ω(C,k) := 1_{(W,2W]}(C)Φ((4Ck − n)/V), with 𝒜 := supp ω and |𝒜|_ω := Σω.
* w(a) := Σ_{f(C,k)=a} ω(C,k), a weight on ℤ (w may take values > 1 and lives on positive and negative a).
* 𝒫 = primes in (P,2P], with P₀ := |𝒫|.
* χ_Q = Jacobi symbol mod Q = qq′ (q ≠ q′ ∈ 𝒫), and S_Q := Σ ω(C,k)χ_Q(f(C,k)) = Σ_a w(a)(a/Q).

*The balanced block.* U ≍ V ≍ n^{1/4} and W ≍ n^{1/2}; concretely, in all computations V = n^{1/4} and W = n^{1/2}/16. We
assume W ≥ 2V; in the balanced block W ≍ V².

## 1. Statements attacked
**(T) Target (FRONTIER §7.1 open item).** There is η > 0 with N(U,V,W) ≪ n^{1/4−η} for the balanced block, uniformly in
odd n (or at least at primes p ≡ 1 (24)). The trivial bound is N ≤ n^{1/4+o(1)} (Z52D Thm 1).

**(T′) Square-sieve form.** By SQSIEVE Lemma 1′ and (4.1), (T) follows from max_{q≠q′∈𝒫}|S_{qq′}| ≪ V^{1−η} for some
P = V^{c}, c > 0. The signed average P₀^{−2}Σ_{q≠q′}S_{qq′} would also suffice.

**(B) Task.** Write the bilinear forms exactly, with supports and sizes (§2). Then either prove a power saving for (T′),
or prove a scoped no-go with the exact deficit for each tool class named in the kickoff (§§3–6). The classes are:
Heath-Brown's real-character large sieve; bilinear Jacobi-symbol bounds (Heath-Brown Cor 4, Friedlander–Iwaniec,
Conrey–Farmer–Soundararajan); Duke–Friedlander–Iwaniec Kloosterman fractions; Pólya–Vinogradov/Burgess in either
variable; and the double large sieve.

## 2. Why this is not already closed; and the exact forms

**Not closed.**
* SQSIEVE Prop B2 closes only the k-Poisson implementation. That implementation takes Q ≤ W, applies the triangle
  inequality over ℓ and over c₀ mod Q, and uses per-class majorants for the C-sums.
* SQSIEVE Remark 3 (large sieve) is an unproved Assessment. No real-character bilinear tool has been examined.
* HYPKLOOST covers DFI and Bettin–Chandee in the hyperbola model, and HYP2CYCLE Prop D closes the black-box determinant
  method.
* The Jacobi-symbol tools act on the *character* side (the modulus Q and the values a = f). None of the predecessors
  touched that side.

**Lemma 2.1 (sizes; PROVED).** Assume W ≥ 2V.
(a) Each C carries at most one k with ω(C,k) ≠ 0.
(b) |𝒜| ≤ Σ_{m∈I}τ(m) ≪_ε V n^ε, where I = ((n + V/2)/4, (n + 5V)/4].
(c) Every value a = f(C,k) with (C,k) ∈ 𝒜 satisfies |a| ≤ 25V² + (n + 5V)/W. In the balanced block this is ≪ V².
*Proof.* (a) Consecutive k change s = 4Ck − n by 4C > 4W ≥ 8V, while ω ≠ 0 forces s ∈ [V/2, 5V], an interval of length
less than 8V. (b) The map (C,k) ↦ m = Ck is at most τ(m)-to-one, and ω ≠ 0 forces 4m − n ∈ [V/2, 5V]. (c) f = s² − 4k,
where 0 < s ≤ 5V and 0 < 4k = (n + s)/C ≤ (n + 5V)/W. ∎

No lower bound for |𝒜| is proved. The statement |𝒜| ≍ V is a heuristic (area ≍ V) and a finite-range observation:
|𝒜| ≈ 0.34V for the sharp windows of §7.

**The six exact forms (PROVED identities; sizes from Lemma 2.1).**
* **(F1) Strip / lattice-point form.** S_Q = Σ_{(C,k)} ω(C,k)g_Q(C,k), with g_Q(c,k) := χ_Q(f(c,k)). The function g_Q is
  Q-periodic in each variable, since f mod Q depends only on (c mod Q, k mod Q). The points are the lattice points of a
  hyperbolic strip of area ≍ V and width < 1 in k.
* **(F2) Divisor form** (SQSIEVE Remark 2). S_Q = Σ_m Φ((4m − n)/V) Σ_{C|m, W<C≤2W} χ_Q((4m − n)² − 4m/C). The m-range
  is an interval of length ≍ V ≍ m^{1/4} at m ≈ n/4, and the divisors C range over (W, 2W] with W ≍ √m.
* **(F3) Poisson (ℓ, C) form** (SQSIEVE Lemma P). S_Q = Σ_{ℓ∈ℤ} Σ_{C∈(W,2W]} a_ℓ(C) e(−ℓn/(4CQ)) G^{(Q)}_C(ℓ), with
  a_ℓ(C) = (V/(4CQ))Φ̂(ℓV/(4CQ)) and G^{(Q)}_C(ℓ) = Σ_{k mod Q} χ_Q(f(C,k))e(ℓk/Q). The coefficients are *Kloosterman
  sums* (SQSIEVE Lemma W), not Jacobi symbols. The effective support is |ℓ| ≤ L := (8QW/V)n^ε ≍ QV n^ε and C ∈ (W,2W]:
  ≍ QV³ terms, with |a_ℓ| ≍ 1/(QV) and |G| ≤ 4√Q on good classes.
  * The ℓ¹-mass is ≍ √Q·W ≍ √Q·V² (the trivial bound; the lower bound is the B2 Parseval argument).
  * The random-phase (ℓ²) benchmark is ≍ V^{1/2}.
  * The target is V^{1−η}.
* **(F4) Additive-twist form.** S_Q = Σ_{(a,b) mod Q} ĝ_Q(a,b)T_Q(a,b), where ĝ_Q(a,b) := Q^{−2}Σ_{c,k mod Q}g_Q(c,k)e(−(ac+bk)/Q)
  and T_Q(a,b) := Σ_{(C,k)}ω(C,k)e((aC + bk)/Q).
* **(F5) Real-character bilinear form** (the only Jacobi-symbol bilinear form present). The square sieve needs
  Σ⁽²⁾(w) := Σ_{q≠q′∈𝒫}S_{qq′}(w) = Σ_Q β_Q Σ_a w(a)(a/Q), with β_Q := #{ordered (q,q′): q ≠ q′, qq′ = Q} ∈ {0, 2}.
  * Supports: Q ∈ (P², 4P²], and a ∈ [−X, X] with X ≪ V² (Lemma 2.1(c)).
  * The a-support satisfies |supp w| ≤ |𝒜| ≪ Vn^ε in a range of length ≍ V², so it is sparse.
  * For a < 0, (a/Q) = (−1/Q)(|a|/Q). The transposed form, with the strip value as modulus, arises after splitting off
    signs and powers of 2 and applying reciprocity to the odd part; it is the same kind of object.
* **(F6) Pair form.** N(U,V,W) = #{(u,B) ∈ (U,2U]×(V,2V] : 4uB | n + u + B, (n + u + B)/(4uB) ∈ (W,2W]}. If
  gcd(u,B) = 1, then 4uB | n + u + B is equivalent to [u | n + B, B | n + u, 4 | (n + u + B)/(uB)] (HYP2CYCLE's 2-cycle
  form).
  * gcd(u,B) divides n, so coprimality is automatic at a prime n = p > 4V.
  * Without coprimality the equivalence fails: u = 3, B = 6, n = 15 satisfies the bracket but 72 ∤ 24.
  * Every solution is a factorisation m = 4uBC of an integer m ∈ (n, n + 4V] with u + B = m − n. So any approach to (T)
    concerns the multiplicative structure of the integers in an interval of length 4n^{1/4} (a restatement).

**Lemma 2.2 (the additive weights; PROVED).** For Q = qq′ as above:
(i) Σ_{(a,b) mod Q}|ĝ_Q(a,b)| ≤ Q;
(ii) |ĝ_Q(0,0)| < 1/Q;
(iii) S_Q = ĝ_Q(0,0)·|𝒜|_ω + Σ_{(a,b)≢(0,0)} ĝ_Q(a,b)T_Q(a,b), hence |S_Q| ≤ |𝒜|_ω/Q + Q·max_{(a,b)≢0}|T_Q(a,b)|.

*Proof.*
(i) By Parseval, Σ_{a,b}|ĝ|² = Q^{−2}Σ_{c,k}|g_Q|² ≤ 1. Cauchy–Schwarz over the Q² pairs then gives Σ|ĝ| ≤ Q.
(ii) We have Q²ĝ(0,0) = Σ_{c,k mod Q}(f/q)(f/q′). By CRT in (c,k) this factors as (Σ_{c,k mod q}(f/q))·(Σ_{c,k mod q′}(f/q′)).
By SQSIEVE Lemma W(a), Σ_{c,k mod q}(f/q) = Σ_c K_q(c), and K_q(c) behaves as follows:
* if q ∤ n, K_q(c) is 0 at c ≡ 0, q − 1 at the single class q | 4cn + 1, and −1 at the other q − 2 classes, so the total
  is 1;
* if q | n, there is no class with q | 4cn + 1, so the total is −(q − 1).
Hence |Q²ĝ(0,0)| ≤ (q − 1)(q′ − 1) < Q.
(iii) Expand g_Q in additive characters of (ℤ/Q)² and insert this into (F1). The bound then follows from (i) and (ii). ∎

*EVIDENCE.* For a prime modulus q₀ = 61, Σ|ĝ| ranges over 52.96–53.86 ≈ 0.87–0.88·q₀ in the runs of §7 (the lower value
when 61 | n), so (i) is sharp up to a constant there.

## 3. Proposition M: two norm-only classes of character-side inputs give no saving (PROVED)

**Setting.** Let 𝒫 be any set of P₀ ≥ 2 odd primes. Call a = m² (m ≥ 1) *admissible* if gcd(m, ∏𝒫) = 1.
* For a finitely supported weight w ≥ 0 on ℤ∖{0}, put N_□(w) := Σ_{a admissible} w(a) and σ(a) := Σ_{q∈𝒫}(a/q).
* Heath-Brown's identity is Σ_a w(a)σ(a)² = Σ_a w(a)(P₀ − ν(a)) + Σ⁽²⁾(w), where ν(a) := #{q ∈ 𝒫 : q | a}.
* Admissible squares have σ = P₀, so
  P₀²N_□(w) ≤ P₀‖w‖₁ + Σ⁽²⁾(w).      (3.1)
* An *input* is a function Ψ on a class 𝔚 of weights with Σ⁽²⁾(w) ≤ Ψ(w) for all w ∈ 𝔚. Its *output* is the derived
  bound β_Ψ(w) := (P₀‖w‖₁ + Ψ(w))/P₀² ≥ N_□(w).
* The relation to the block count: M_s(w) := Σ_{m≥1}w(m²) ≥ N_□(w), and N ≤ 2M_s(w) + τ(n) (SQSIEVE Lemma 1′).

**Proposition M.**
(i) If w′ ∈ 𝔚 is supported on admissible squares, then Ψ(w′) ≥ Σ⁽²⁾(w′) = P₀(P₀ − 1)‖w′‖₁.
(ii) *(Sup-norm / support / range inputs.)* Let 𝔚 = 𝔚(X, K, h) := {w : supp w ⊂ [−X, X], |supp w| ≤ K, ‖w‖_∞ ≤ h}, and let
Ψ be constant on 𝔚 (a bound depending only on X, K, h and the parameters of 𝒫). Then Ψ ≥ P₀(P₀ − 1)h·min(K, A(X)), with
A(X) := #{admissible squares ≤ X}. So for every w ∈ 𝔚, β_Ψ(w) ≥ (1 − 1/P₀)h·min(K, A(X)). Since trivially
N_□(w) ≤ h·min(K, A(X)) on 𝔚, **the output is never better than the trivial bound up to the factor 1 − 1/P₀.**
(iii) *(Square-class ℓ² inputs.)* Put D(w) := Σ_{a,a′: aa′ ∈ {m² : m ≥ 1}} w(a)w(a′), and let Ψ(w) = F(D(w)) be valid
for all w, with F non-decreasing. Then:
* F(D) ≥ P₀(P₀ − 1)√D for every D ≥ 0;
* β_Ψ(w) ≥ ‖w‖₁/P₀ + (1 − 1/P₀)√D(w) ≥ √D(w), using ‖w‖₁ ≥ √D(w);
* √D(w) ≥ M_s(w) ≥ max(N_□(w), (N − τ(n))/2), since positive squares pair to squares.
So the output is never below M_s(w). Turning it into a number needs an upper bound D(w) ≤ D₀, and that bound alone
already gives M_s(w) ≤ √D₀, hence N ≤ 2√D₀ + τ(n). **The route adds nothing to its own input.**

*Proof.*
(i) For a admissible, (a/qq′) = 1 for every pair, and there are P₀(P₀ − 1) ordered pairs.
(ii) Let w′ := h·1_𝒮, where 𝒮 is a set of min(K, A(X)) admissible squares ≤ X. Then w′ ∈ 𝔚, so (i) gives Ψ = Ψ(w′) ≥
P₀(P₀ − 1)h|𝒮|. The trivial bound holds because N_□(w) sums at most min(K, A(X)) values, each ≤ h.
(iii) Put w′ := √D·δ₁, which is admissible since gcd(1, ∏𝒫) = 1. Then D(w′) = D, so by (i)
F(D) ≥ Σ⁽²⁾(w′) = P₀(P₀ − 1)√D. Next, D(w) ≤ (Σ_a w(a))² = ‖w‖₁². Finally D(w) ≥ Σ_{a,a′ positive squares}w(a)w(a′) =
M_s(w)². ∎

**Corollary M′ (the named tools; PROVED relative to the statements quoted in LIT_CHECK §1, for their direct use as
inputs).**
(a) *Heath-Brown, Acta Arith. 72 (1995), Cor 2* (large sieve for real primitive characters, arbitrary positive n ≤ N,
norm Σ_{n₁n₂=□}|a_{n₁}a_{n₂}|). This is class (iii). The Jacobi symbols (·/Q), Q = qq′ odd squarefree, are distinct real
primitive characters of conductor Q ≤ 4P². Split w = w⁺ + w⁻ by the sign of a, and write S_Q(w) = S_Q(w⁺) + (−1/Q)S_Q(w̃⁻),
where w̃⁻(|a|) := w⁻(a). Cor 2 applied to each part gives Σ_Q|S_Q(w)|² ≤ 2Σ_Q(|S_Q(w⁺)|² + |S_Q(w̃⁻)|²) ≪
(P²X)^ε(P² + X)D(w), because D(w⁺) + D(w̃⁻) ≤ D(w). Cauchy–Schwarz over Q then gives
Ψ(w) = c_ε(P²X)^ε·P₀·(P² + X)^{1/2}·D(w)^{1/2}, a non-decreasing function of D(w). By M(iii) its output is ≥ √D(w) ≥ M_s(w).
This turns SQSIEVE Remark 3's Assessment into a theorem, in a sharper form: the obstruction is not "worse than trivial"
but "adds nothing to its input".
(b) *Heath-Brown Cor 4* (Σ_{m≤M}^{odd}Σ_{n≤N}^{odd}a_m b_n(n/m) ≪ (MN)^ε(MN^{1/2} + M^{1/2}N), |a_m|, |b_n| ≤ 1). Apply it
after splitting a by sign and by the exact power of 2, absorbing (−1/Q), (2/Q) and β_Q/2 into the Q-coefficients and
normalising w by h. The resulting Ψ depends only on (X, h, P), so it is class (ii): its output is at least
(1 − 1/P₀) × the trivial bound. The same applies to any sup-norm bilinear Jacobi bound valid for all coefficients of
modulus ≤ 1 on given ranges, e.g. a Friedlander–Iwaniec-type bound (its exact statement was not located; LIT_CHECK §2a).
For the record, Cor 4's own value with M = 4P², N ≍ V² gives an output ≫ h(V + V²/P), up to the (MN)^ε loss.
(c) *Conrey–Farmer–Soundararajan, JNT 82 (2000), Thm 1* is an asymptotic for the unweighted sum over the full odd boxes
m ≤ X, n ≤ Y (LIT_CHECK §2b). It does not apply directly to the sparse weight w (Assessment: we see no useful
decomposition of w into full boxes).
(d) *Pólya–Vinogradov / Burgess, direct use.*
* In the a-variable, supp w is not an interval.
* In (C,k)-coordinates each C carries ≤ 1 point (Lemma 2.1(a)) and k = k(C) is not a polynomial in C.
* In the modulus variable (e.g. an "integer square sieve" with Q over an interval), (a/·) is non-principal for non-square
  a. So PV/Burgess bound the *non-square* part Λ_non of Λ := Σ_a w(a)|Σ_Q(a/Q)|² = Λ_□ + Λ_non. An upper bound on Λ_non
  bounds Λ_□ *from below* in terms of Λ, not from above, and an upper bound on Λ is again Σ_{Q,Q′}S_{QQ′} (strip side).
This identity-level remark is PROVED. It is not a no-go for weighted or completed uses of these bounds.

*Reading.* Prop M is the precise form of "the large sieve does not see sparsity" for the square sieve. A bound that is
uniform over all weights with the same square-class mass, or the same sup-norm/support/range, is attained, up to the
factor 1 − 1/P₀, by a weight on squares, and squares are exactly what the sieve counts. A successful character-side
input therefore has to use properties of w beyond these norms, i.e. the strip structure of 𝒜, or a structured
(non-norm) property of the character sums themselves. Neither is excluded here.

## 4. Theorem R: a sufficient strip-side input (PROVED; conditional consequences)

**Hypothesis TS(δ; P) (twisted strip equidistribution).** For every Q = qq′ with q ≠ q′ primes in (P,2P], and every
(a,b) ≢ (0,0) mod Q:
  |T_Q(a,b)| = |Σ_{(C,k)} ω(C,k)e((aC + bk)/Q)| ≤ V^{1−δ}.
This is equivalent, up to factors Q^{O(1)}, to power-saving equidistribution of the strip points among the classes
(C mod Q, k mod Q). It contains *no quadratic character*.

**Theorem R.** Let W ≥ 2V and (log n)² ≤ P ≤ V. Then, uniformly in odd n ≥ n₀(ε):
  N(U,V,W) ≪_ε n^ε [ V/P + P²·max_{Q,(a,b)≢0}|T_Q(a,b)| ].
Consequently:
* for fixed δ ∈ (0,1], TS(δ; V^{δ/3}) ⇒ N(U,V,W) ≪_{ε,δ} n^ε V^{1−δ/3} (a power saving for (T)), taking P = V^{δ/3};
* the square-root version |T_Q| ≪ V^{1/2+ε} for Q ≤ 4V^{1/3} ⇒ N ≪ n^{5/24+ε}, taking P = V^{1/6};
* square-root cancellation in S_Q itself, |S_Q| ≪ V^{1/2+ε} for Q ≤ 4V, ⇒ N ≪ n^{1/8+ε}, taking P = V^{1/2} in the
  square sieve directly (SQSIEVE Remark 1).

*Proof.*
* By SQSIEVE Lemma 1′ and (4.1), N ≤ 2[(4/P₀)S₁ + 4max|S_Q|] + τ(n), with S₁ = |𝒜|_ω ≪ Vn^ε (Lemma 2.1(b)).
* The hypotheses of (4.1) hold: P₀ ≫ P/log P, and 2^{P₀} ≥ 25V² once P ≥ (log n)² and n ≥ n₀. (4.1) restricts only
  positive square values, which are ≤ 25V² by Lemma 1′; negative values carry no square weight. No Q ≤ W condition is
  used.
* Lemma 2.2(iii) gives max|S_Q| ≤ Vn^ε/P² + 4P²·max|T_Q|.
* The three choices of P balance V/P against P²V^{1−δ}, P²V^{1/2} and V^{1/2} respectively.
* Finitely many n < n₀ are absorbed into the constant. ∎

**Proposition R′ (twist-blind bounds imply TS; PROVED).** Call an S_Q-bound *twist-blind* if it bounds |Σω·g| by the
same quantity B_Q for every Q-periodic g with ‖g‖_∞ ≤ 1 and mean zero over (ℤ/Q)². A twist-blind bound B_Q ≤ V^{1−η}
implies |T_Q(a,b)| ≤ V^{1−η} for all (a,b) ≢ 0, i.e. TS(η).
*Proof.* g = e((ac + bk)/Q) has modulus 1 and mean zero for (a,b) ≢ 0. ∎

Thm R makes TS *sufficient*. R′ makes it *necessary only for twist-blind bounds*. Neither says that every successful
argument must pass through TS. Arguments that use the specific Kloosterman structure of ĝ_Q / G_C(ℓ) jointly with the
strip are not covered, nor are weighted Fourier estimates or averages over the moduli. SQSIEVE Prop B2 excludes one such
use: the triangle inequality over (ℓ, c₀) in its implementation class.

## 5. Calibration: TS at the balanced block is a twisted short-interval divisor problem at y = x^{1/4}

**Identity (PROVED).** T_Q(0,0) = |𝒜|_ω = Σ_m Φ((4m − n)/V)τ_{(W,2W]}(m), where τ_{(W,2W]}(m) := #{C | m : W < C ≤ 2W}.
This is a smoothed short-interval sum of a dyadically restricted divisor function. The window
I = ((n + V/2)/4, (n + 5V)/4] has centre x₀ = (n + 11V/4)/4 and length ≍ V ≍ x₀^{1/4}.
* By Poisson in k (Lemma P with Q = 1),
  |𝒜|_ω = Σ_{C∈(W,2W]}(V/(4C))Φ̂(0) + Σ_{C∈(W,2W]} Σ_{h≠0}(V/(4C))Φ̂(hV/(4C))e(−hn/(4C)).
  The second sum is the smoothed analogue of the dyadic ψ-difference Σ_C[ψ(x₁/C) − ψ(x₂/C)].
* For (a,b) ≢ 0, T_Q(a,b) is the same kind of sum with the additively twisted divisor function Σ_{Ck=m}e((aC + bk)/Q)
  (an Eisenstein-type coefficient of level Q).

**(5.1) Comparison with the divisor problem (Assessment; literature-anchored).**
* Li–Yang (arXiv:2308.14859, Thm 1.2; LIT_CHECK §5a) give Δ(x) ≪ x^{θ*+ε} with θ* = 0.3144831…. This yields full
  short-interval asymptotics only for y ≥ x^{θ*+η}.
* If the same exponent held for the dyadic, smoothed strip count (Assessment: a bound for Δ does not automatically bound
  a dyadic piece), the error would be x^{θ*+ε} ≍ V^{4θ*+ε} = V^{1.2579…}. That is worse than the elementary
  |𝒜| ≪ Vn^ε.
* The sources checked supply **no power-saving pointwise error for this strip** (LIT_CHECK §5a: no pointwise
  short-interval result below x^{0.3} found; search-limited, not a non-existence claim). Nothing is claimed here about
  the twisted sums beyond this.
* In exponents of V, the gap between the full-divisor-problem exponent and TS(δ) is 4θ* − 1 + δ = 0.2579 + δ.

**(5.2) Jutila's conjecture (CONJECTURE, literature).** Jutila conjectured
Δ(x + h) − Δ(x) ≪_ε x^ε√h for x^ε ≤ h ≤ x^{1/2−ε} (Ivić, JTNB 21 (2009), (1.13); LIT_CHECK §5b, read from the source).
This is essentially best possible by the Ω-result (1.12): Δ(x+h) − Δ(x) = Ω(√h log^{3/2}(√x/h)) in the same range. The
square-root form of TS at the balanced block, |T_Q(a,b)| ≪ V^{1/2+ε}, is a *twisted, dyadically restricted, smoothed
analogue of Jutila's conjecture at h = x^{1/4}*. With Thm R it would give N_bal ≪ n^{5/24+ε}. No implication between
Jutila's conjecture and TS is proved here.

**(5.3) Exponent-pair majorants (PROVED as a computation of the bound expression; not an exclusion of all
one-variable arguments).** Let a ≢ 0 mod Q. Poisson in k gives
  T_Q(a,0) = Σ_h Σ_{C∈(W,2W]} (V/(4C))Φ̂(hV/(4C)) e(aC/Q − hn/(4C)).
* For a ≢ 0, the h = 0 term is ≪ QV/W by partial summation. (For a = 0 it is the main term ≍ V.)
* For 1 ≤ |h| ≤ (8W/V)n^ε, the phase F(C) = aC/Q − hn/(4C) (|a| ≤ Q/2) has |F′| ≍ |h|. Indeed n/(4C²) lies between 16
  and 64 for W = √n/16, so the h-term dominates a/Q.
* An exponent pair (κ, λ) gives |Σ_C e(F)| ≪ |h|^κW^λ, so the bound expression is
  ≍ Σ_{h ≤ V}(V/W)h^κW^λ ≍ (V/W)(W/V)^{κ+1}W^λ = V^{κ+2λ}.
* Since λ ≥ 1/2, κ + 2λ ≥ 1, with equality only at the conjectural pair (0, 1/2).
* Deficits in V-exponents:
  * Bourgain's (13/84 + ε, 55/84 + ε) gives κ + 2λ = 41/28, a deficit of 13/28 = 0.4643;
  * (1/6, 2/3) gives 3/2;
  * the conjectural pair gives exactly the trivial exponent 1.
* This parallels SQSIEVE Prop B2 in the additive, Q = 1 setting, for implementations using these majorants.

**(5.4) Mean square (literature + EVIDENCE).**
* Ivić (1.9) and (1.14) give ∫_X^{2X}(Δ(x+h) − Δ(x))²dx ≍ Xh log³(√X/h), with leading coefficient 8/π² in (1.14). So the
  root-mean-square over x of the short-interval error is ≍ √(h log³).
* This is a mean-square statement only and is not transferred to the dyadic strips here.
* In our strips (§7) the count error is (1.2–1.6)·√|𝒜| and S_Q, T_Q are ≈ 1·√|𝒜| (rms over Q, (a,b)). This is
  consistent with square-root behaviour in the computed instances.

**(5.5) Other bilinear tools on the strip side.**
* *DFI (Kloosterman fractions; HYPKLOOST LIT_CHECK §3, as corrected there).* Detecting B | n + u or u | n + B by additive
  characters in a (u,B)-box gives numerators a ≍ hn ≥ n ≍ V⁴ (the case h = 1 is the smallest), with M = N ≍ V. Hence
  a/(MN) ≍ V², and with |α|, |β| ≤ 1, ‖α‖‖β‖ ≍ V.
  * DFI Thm 1's term ‖α‖‖β‖(1 + a/MN)^{1/2}min(M,N) ≍ V³ exceeds the trivial MN ≍ V² by V.
  * DFI Thm 2's ‖α‖‖β‖(a + MN)^{3/8}(M + N)^{11/48} ≍ V^{131/48} exceeds it by V^{35/48}.
  * Larger h only make both worse.
  * (PROVED as arithmetic on the cited bounds for box forms with these ranges. The exact form (F6) is not a separable
    box form, so this is the best case for a direct application.)
* *Double large sieve (Bombieri–Iwaniec; Assessment).* Apply it to (F3) with x_ℓ = ℓ (|ℓ| ≤ L ≍ QV) and the Kloosterman
  sum opened, i.e. points y_{C,k} = (4Ck − n)/(4CQ) reduced mod 1 (WQ points). Then XY ≍ QV.
  * Under the generic shape (1 + XY)·(spacing sums), and assuming the y's are spread (not verified) and a_ℓ(C) separable
    at cost n^ε, the bound is ≍ V^{3/2}Q^{1/2}: a deficit of (QV)^{1/2}V^{η}.
  * The diagonal parts alone, Σ|α_ℓ|² ≍ 1/(QV) and Σ|β|² ≥ cWQ (for P large, by Lemma W(a)), make the expression
    ≫ V√Q, already above the trivial V.
  * The inequality's exact constants were not re-verified (LIT_CHECK §4). Opening the Kloosterman sum reverts the Poisson
    step, so the inequality sees only near-coincidences of the y's and no strip structure.
* *Determinant method.* Closed in black-box form by HYP2CYCLE Prop D (criticality V/T = 1).

## 6. Summary of deficits at the balanced block (exponents of V = n^{1/4}; the target is V^{1−η})

| tool class (direct use) | how it enters | output / deficit | status |
|---|---|---|---|
| HB real-character large sieve (Cor 2) | (F5), norm D(w) | output ≥ √D(w) ≥ M_s(w): adds nothing to its input | PROVED (Prop M(iii), M′(a)) |
| HB Cor 4, other sup-norm bilinear Jacobi bounds | (F5), (X, h) | output ≥ (1−1/P₀)·(trivial bound h·min(K, A(X))) | PROVED (Prop M(ii), M′(b)) |
| CFS transition mean values | full boxes only | no direct application to sparse w | Assessment |
| PV / Burgess | a-variable: no interval; Q-variable: bound only non-squares | no direct input | PROVED (identity remark) |
| DFI Thm 1 / Thm 2 | (u,B)-box Kloosterman fractions, a ≍ hn | × V / × V^{35/48} above trivial | PROVED (arithmetic) |
| double large sieve | (F3) opened | ≍ V^{3/2}Q^{1/2} (diagonal alone ≫ V√Q) | Assessment |
| exponent-pair majorants on C-sums | (F3)/(F4) per h or ℓ | V^{κ+2λ} ≥ V; Bourgain V^{41/28}; conjectural pair V^{1} | PROVED (bound expression); cf. B2 |
| full divisor exponent (Li–Yang), if it transferred | T_Q(0,0) only | V^{4θ*} = V^{1.258} (worse than elementary V^{1+o(1)}) | Assessment (lit.) |
| additive expansion + square-root T_Q | Thm R | N ≪ n^{5/24+ε} | CONDITIONAL (twisted Jutila-type) |
| square-root S_Q | (T′) | N ≪ n^{1/8+ε} | CONDITIONAL |
| determinant method (black box) | surface | ≥ trivial | PROVED elsewhere (HYP2CYCLE D) |

## 7. Computations (EVIDENCE unless stated)

Counts and Jacobi symbols use exact integer arithmetic; Fourier data use double precision. The computed weights (a sharp
s-window in §7.2 and a Gaussian in §7.3) differ from the compactly supported Φ of the theorems.

**7.1 Census** (`z54_bilinjac_census.c`; CERTIFIED for the range). For every odd n ≤ 10⁹, put
N_bal(n) := #{(★) triples : n^{1/4}/2 < u, B ≤ 2n^{1/4}}.
* Membership is tested exactly in integers: n < 16·min(u,B)⁴ and max(u,B)⁴ ≤ 16n. Counter saturation is checked.
* The rerun with the exact test is byte-identical to the first run.
* The mean is 0.4802–0.4805 in each decade 10⁵–10⁹, against (ln 4)²/4 = 0.48045.
* The maximum over all odd n ≤ 10⁹ is 20, at n = 635 674 641 = 3·7·30 270 221.
* Over primes p ≡ 1 (24) the maximum is 14, at p = 250 810 249.
* Odd squares give 0 (T1).
* Decade maxima: 6, 8, 8, 12, 16, 20.

The tail is heavier than Poisson: the frequency of N_bal = 20 is about 2·10⁻⁹, against about 10⁻¹³ for Poisson with the
same mean. Still, N_bal is tiny against n^{1/4} ≈ 159 (`census_1e9.txt`). (T) holds by a large margin in the range.

**7.2 Strip statistics** (`z54_bilinjac_strip.c`, `z54_bilinjac_multi.py`, `z54_bilinjac_summarize.py` →
`strip_summary.txt`). Setup:
* Balanced block V = n^{1/4}, W = √n/16, sharp window s ∈ (2V, 4V].
* At each scale: 100 consecutive primes p ≡ 1 (24), 30 odd squares, 30 near-squares m² + 4.
* P ∈ {√V, V/4}, ≤ 300 pairs per n.
* Additive analysis at q₀ = 61.

| scale | V | |𝒜| range | count err rms /√|𝒜| | S_Q rms /√|𝒜| | max S_Q /√|𝒜| | max over 100 sub-rectangles | E(c,k) rms ratio | max_{(a,b)≠0}|T|/√|𝒜| | additive bound / √|𝒜| |
|---|---|---|---|---|---|---|---|---|---|
| 10¹⁰ | 316 | 81–154 | 1.31–1.39 | 0.90–1.00 | 4.33 | 4.72 | 1.01 | 3.44 | 48.1–48.3 |
| 10¹² | 1000 | 283–428 | 1.24–1.64 | 0.93–1.00 | 3.94 | 5.08 | 1.01 | 3.56 | 48.1–48.2 |
| 10¹⁴ | 3162 | 982–1175 | 1.41–1.54 | 0.96–1.01 | 4.27 | 5.32 | 1.01 | 3.54 | 48.2–48.5 |

* Primes, odd squares and near-squares are indistinguishable in every column. This is consistent with the T1-blindness of
  these sums; an n-uniform upper-bound input need not be T1-blind in general.
* The ratio E rms ≈ 1.01 is a weak test: at occupancy |𝒜|/q₀² ≤ 0.32, E rms² = 1 − |𝒜|/q₀² holds exactly when no class
  holds two points, and T rms is tied to ΣN(c,k)² by Parseval. The maxima of |T| and of the sub-rectangle sums are the
  informative columns. They are within the Gaussian-extreme range for the number of samples.
* The additive triangle bound (Lemma 2.2(iii)) overshoots |S_{q₀}| by ≈ 0.8·q₀. This is the Q-loss in Thm R; it is
  harmless for P = V^{δ/3}.
* The test primes of FRONTIER §4 item 14 are ≤ 8.8·10⁶. At their scale the balanced block is nearly degenerate
  (V = 4–54, |𝒜| ≤ 14), so `strip_testprimes.txt` is a formal control only.

**7.3 The actual Poisson (ℓ, C) bilinear form** (`z54_bilinjac_shells.c`; `shells_1e10.txt`, `shells_1e12.txt`). Setup:
Gaussian Φ(t) = e^{−π(t−3)²}. The form was computed term by term over the full (ℓ, C) support: 9.2·10⁸ terms (Q = 143)
and 2.1·10⁹ terms (Q = 323) at 10¹⁰, and 3.1·10⁹ terms at 10¹². Each dual total matches the direct strip sum to
≤ 2.2·10⁻¹¹ (Lemma P check). Instances:
* n = 10¹⁰ + 33 (prime), 100 003² (odd square), 100 003² + 4, with Q = 11·13;
* n = 10¹⁰ + 33 with Q = 17·19;
* n = 10¹² + 177 (prime) and 1 000 001² (odd square), with Q = 3·5.

For each dyadic shell |ℓ| ~ 2^j we record |shell sum|, the random-phase benchmark ℓ² = (Σ|term|²)^{1/2}, and the trivial
ℓ¹. Results:
* Over the 89 shells with ℓ ≠ 0 and |sum| > 10⁻³, |sum|/ℓ² has median 0.75 and maximum 3.08. The ℓ = 0 shell is a main
  term and is not random.
* Totals: ℓ¹ = 45 686 against ℓ² = 5.74 at 10¹⁰ (Q = 143; ℓ¹/ℓ² ≈ 8 000), and ℓ¹ = 151 760 against ℓ² = 8.95 at 10¹²
  (Q = 15; ≈ 17 000).
* Within shells, the joint (ℓ, C) sums are consistent with square-root cancellation in these six instances. The saving
  needed to reach the trivial scale (ℓ¹/V ≈ 145–152) is a small fraction of the saving available to square-root
  cancellation (ℓ¹/ℓ² ≈ 8 000–17 000).
* Partial sums from the top shell down stay at the √|𝒜| scale (cumulative columns).

So in the computed instances the bilinear estimate SQSIEVE asks for holds with room. What is missing is a proof
technology for TS-type equidistribution at y = x^{1/4}.

## 8. FRONTIER §4 hard screens (for Thm R / the (T′) route)
1. **T1 (odd squares).** This is an n-uniform upper bound, valid at m² (where N = 0). It cannot imply positivity. The
   computed sums do not distinguish squares (§7.2).
2. **8/131.** It transfers to other numerators (only the strip geometry is used). Harmless for an upper bound; silent on
   8/131.
3. **Tied modulus.** The tie is encoded as the square condition on f. The square sieve uses only fixed auxiliary moduli
   Q, and the hard part is the short-interval strip (F6). B2 is untouched.
4. **Fixed p.** Passed: pointwise in n. Averages are over (C,k), ℓ, (a,b) and the auxiliary primes only. The census
   (§7.1) is a range statement, not an input.

## 9. Verdict
**Narrowed.** What was proved:
* **Prop M + Cor M′ (PROVED).** Two classes of character-side inputs to the square sieve give no saving:
  * square-class ℓ² inputs (Heath-Brown's real-character large sieve, Cor 2, used directly) return ≥ √D(w) ≥ M_s(w), so
    they add nothing to the bound on D(w) they require;
  * sup-norm/support/range inputs (Heath-Brown Cor 4 and any sup-norm bilinear Jacobi bound, used directly) return at
    least (1 − 1/P₀) × the trivial bound.
  * Direct uses of CFS and PV/Burgess do not apply.
  * After Poisson the (ℓ, C) coefficients are Kloosterman sums, so the "bilinear sums of Jacobi symbols" reading of the
    kickoff applies only to the sieve's (Q, a) form, and there only these norm-only uses are closed.
* **Thm R (PROVED) + Prop R′.** TS(δ), power-saving equidistribution of the strip modulo small Q (no quadratic character,
  loss Q), is *sufficient*. It is necessary for twist-blind bounds. Conditional benchmarks: TS(δ) ⇒ N ≪ V^{1−δ/3+ε};
  square-root TS ⇒ n^{5/24+ε}; square-root S_Q ⇒ n^{1/8+ε}.
* **Calibration.**
  * Square-root TS is a twisted dyadic analogue of Jutila's conjecture at h = x^{1/4}.
  * Exponent-pair majorants give V^{κ+2λ} ≥ V, the conjectural pair exactly trivial.
  * The checked literature gives no power-saving pointwise bound even for the untwisted strip count; the full divisor
    exponent would give V^{1.258} (Assessment).
  * DFI is off by V (Thm 1) or V^{35/48} (Thm 2).
  * The double large sieve is off by ≥ √Q, heuristically (QV)^{1/2} (Assessment).

What survives:
1. A genuinely two-dimensional pointwise short-interval estimate at y = x^{1/4} for (twisted) divisor sums restricted to
   C ≍ √x. This is a Jutila-type pointwise statement beyond the current exponent x^{θ*}, θ* = 0.3145, by x^{0.0645}
   (Assessment).
2. Arguments using the specific Kloosterman structure of G_C(ℓ) jointly with the phase e(−ℓn/(4CQ)) (not excluded by B2
   or R′).
3. Character-side inputs that use structure of w or of the character sums beyond the two norm classes of Prop M.

EVIDENCE (§7) is consistent with square-root cancellation in every computed instance, so none of these routes is
contradicted by the data.

## 10. Proposed FRONTIER §7.1 text (do NOT edit FRONTIER here)
> *(z54, `Z54_BILINJAC.md`; internal.)* **Balanced block: norm-only Jacobi-symbol inputs give nothing; a sufficient
> input is strip equidistribution modulo small Q, a Jutila-type short-interval problem.**
> * Square-mimic theorem (Prop M, PROVED). Square-sieve inputs that see the weights only through square-class ℓ²-mass
>   (Heath-Brown's real-character large sieve, Cor 2, used directly) return ≥ √D(w) ≥ the square mass, adding nothing to
>   the bound on D(w) they need. Inputs that see them only through sup-norm/support/range (Heath-Brown Cor 4 and other
>   sup-norm bilinear Jacobi bounds) return ≥ (1 − 1/P₀) × the trivial bound. Direct uses of CFS and
>   Pólya–Vinogradov/Burgess do not apply.
> * After Poisson the (ℓ, C) coefficients are Kloosterman sums, not Jacobi symbols.
> * Thm R (PROVED): at the balanced block, N ≪ n^ε[V/P + P²·max|T_Q(a,b)|], with T_Q the additively twisted strip sums
>   mod Q = qq′ ≍ P². So power-saving equidistribution of the strip modulo small Q (TS(δ)) suffices for
>   N ≪ p^{(1−δ/3)/4+ε}, and square-root TS gives p^{5/24+ε}. Twist-blind S_Q-bounds imply TS (Prop R′).
> * Square-root TS is a twisted, dyadic analogue of Jutila's conjecture Δ(x+h) − Δ(x) ≪ x^ε√h at h = x^{1/4}.
> * Exponent-pair majorants give V^{κ+2λ} ≥ V (the conjectural pair exactly trivial). The checked literature has no
>   power-saving pointwise bound even for the untwisted strip count (Assessment). DFI misses by V; the double large sieve
>   by ≥ √Q (Assessment).
> * EVIDENCE: S_Q, sub-rectangle sums, T_Q, and the actual (ℓ, C) form shell by shell at 10¹⁰–10¹⁴ are consistent with
>   square-root cancellation, and max N_bal = 20 over odd n ≤ 10⁹.
> * Survives: a 2-D pointwise short-interval estimate at y = x^{1/4}; a joint use of the Kloosterman structure; or
>   character-side inputs that use more than norms.
In §6 add: "Real-character large sieve / sup-norm bilinear Jacobi bounds, used directly as square-sieve inputs → no
saving (square mimic) → `Z54_BILINJAC` Prop M".

## 11. Bottom line
The kickoff hoped that the missing bilinear (ℓ, C) cancellation at the balanced block might be a bilinear sum of Jacobi
symbols, open to Heath-Brown's large sieve and its relatives. After Poisson the coefficients are Kloosterman sums. The
only Jacobi-symbol bilinear form, the sieve's (Q, a) form, is closed for the direct, norm-only uses of those tools by a
short square-mimic argument: a bound that sees the weights only through their norms cannot tell the strip from a set of
squares, which is what the sieve counts.

A sufficient input for the square sieve at the balanced block is power-saving equidistribution of the strip's lattice
points modulo small moduli (Thm R). That is a twisted divisor problem in an interval of length x^{1/4}, whose square-root
form is a twisted analogue of Jutila's conjecture. The literature checked gives no power-saving pointwise bound even for
the untwisted count, and exponent-pair majorants stop exactly at the trivial exponent.

Numerically, every computed instance is consistent with square-root cancellation, and the balanced block holds at most 20
solutions for every odd n ≤ 10⁹. So (T) holds with room in the computed range, but a proof along these lines needs a new
pointwise short-interval estimate or a new joint use of the Kloosterman structure. This is upper-bound work: it can
sharpen the §7.1 benchmark, never positivity. ES remains open.

## 12. Reproduction (all with `ulimit -v 4000000`, or 6000000 for the census; timings on one core)
```
gcc -O2 -o /tmp/z54census scripts/z54_bilinjac_census.c -lm
ulimit -v 6000000; timeout 1500 /tmp/z54census 1000000000 > data/z54/bilinjac/census_1e9.txt          # ~10 s, 2 GB
gcc -O2 -o /tmp/z54strip scripts/z54_bilinjac_strip.c -lm
timeout 900 uv run --with sympy python scripts/z54_bilinjac_multi.py /tmp/z54strip 0 0 0 data/z54/bilinjac/strip_testprimes.txt
for e in 10 12 14; do timeout 1700 uv run --with sympy python scripts/z54_bilinjac_multi.py /tmp/z54strip $e 100 30 \
   data/z54/bilinjac/strip_1e$e.txt; done                                                              # < 1 min total
uv run python scripts/z54_bilinjac_summarize.py data/z54/bilinjac/strip_testprimes.txt data/z54/bilinjac/strip_1e1*.txt
gcc -O2 -o /tmp/z54shells scripts/z54_bilinjac_shells.c -lm
for a in "10000000033 316 6250 11 13" "10000600009 316 6250 11 13" "10000600013 316 6250 11 13" "10000000033 316 6250 17 19"; \
   do timeout 900 /tmp/z54shells $a; done > data/z54/bilinjac/shells_1e10.txt                        # ~4 min
for a in "1000000000177 1000 62500 3 5" "1000002000001 1000 62500 3 5"; do timeout 1500 /tmp/z54shells $a; done \
   > data/z54/bilinjac/shells_1e12.txt                                                                 # ~6 min
```

## 13. Review log
**Hostile review 1** (deep-mode subagent; `reviews/z54_bilinjac_review1.md`). Verdict **FLAWED**: the core lemmas pass
(Lemma 2.1, Lemma 2.2, Prop M(i)–(iii), Thm R, R′, all exponent and DFI arithmetic recomputed; strip and shell runs
reproduced byte-for-byte), but several claims were overstated. Fixes applied:
* F1, F2, F3 (MAJOR): Prop M is now stated and summarised as closing two norm-only input classes in their direct use,
  not "every character-side input".
  * Cor M′(a) gives the direct Cor 2 reduction (sign split, Cauchy–Schwarz over Q) instead of the "grouping" assertion.
  * Cor M′(b) handles signs, powers of 2 and normalisation.
  * Outputs are compared with the trivial bound h·min(K, A(X)) and with M_s(w), with N ≤ 2M_s + τ(n), instead of
    "≥ N"; β_Ψ ≥ √D now follows from ‖w‖₁ ≥ √D.
  * |𝒜| ≍ V is marked heuristic/finite-range.
* F4 (MAJOR): "TS is needed" removed. Thm R gives sufficiency; R′ gives necessity only for twist-blind bounds. The δ range,
  n ≥ n₀ and the last choice of P were added.
* F5 (MAJOR): the (F6) equivalence now assumes gcd(u,B) = 1 (automatic at primes), with the reviewer's counterexample
  noted.
* F6: the Fejér-based necessity claim was removed from §5.3; the h = 0 estimate is restricted to a ≢ 0; Bourgain's value
  is 41/28.
* F7 (MAJOR): §5.1 is now a conditional comparison (no "and twists"; the elementary O(Vn^ε) bound noted). The identity
  uses the smoothed Poisson form, and the window centre is corrected to (n + 11V/4)/4.
* F8: the Jutila/Ivić citation was corrected after re-reading the source (LIT_CHECK §5b rewritten). The mean square is
  Ivić (1.9)/(1.14), and **Jutila's pointwise conjecture (1.13)** is now used as the calibration for square-root TS
  (§5.2).
* F9: double-large-sieve assumptions are explicit (y mod 1, spreading, separability; cWQ).
* F10: numbers corrected (|𝒜| ranges, census decade means 0.4802–0.4805, test-prime V = 4–54 and |𝒜| ≤ 14, g1 range
  52.96–53.86, shell median 0.75, ≤ 2.2·10⁻¹¹).
* F11: the census now uses an exact integer membership test with a saturation check (rerun byte-identical, so CERTIFIED
  stands). The summariser tags the P-choice by run order and prints V, W, |𝒜| ranges.
* F12: the evidence wording was changed to "consistent with"; "as they must be" removed; the weakness of the E rms
  statistic noted; the CFS/PV/Burgess exclusions are scoped to direct application.
