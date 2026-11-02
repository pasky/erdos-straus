# Z54_BILINJAC — depth lane BILINJAC (wave z54, gap 1): bilinear (ℓ, C) cancellation for the square sieve at the balanced block; the quadratic-character (Jacobi-symbol) toolbox

ES is OPEN. Nothing here proves or disproves it. This lane is **upper-bound work only**: even complete success (a power
saving N(balanced) ≪ p^{1/4−η}) would say nothing about positivity of R(p). Its value is the FRONTIER §7.1 benchmark and
the method.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. All results are internal and were
reviewed internally only.

Brief: `z52bbriefs/z53_depth.md` (rules), kickoff `z52bbriefs/z54_lanes.md` §BILINJAC. Predecessor: `Z53_SQSIEVE.md`
(Prop B2, §5.2 Remarks 1–3). Scripts `scripts/z54_bilinjac_*`, data `data/z54/bilinjac/` (< 100 kB). Literature checks:
`data/z54/bilinjac/LIT_CHECK.md` (this lane) and `data/z53/hypkloost/LIT_CHECK.md` (DFI, determinant method).

*Status: full draft (checkpoint 1 = commit 8003579f).* **Verdict: narrowed** (§9). In one sentence: the Jacobi-symbol
tools act only on the character side, and there they provably cannot beat the trivial bound (Prop M). The square sieve at
the balanced block reduces, with a loss of only Q, to power-saving equidistribution of the strip's lattice points modulo
small Q (Thm R). That is a short-interval divisor problem in residue classes at length y = x^{1/4}. For it, even the
untwisted count has no non-trivial pointwise bound in the literature checked, and single-variable exponent-pair methods
stop exactly at the trivial exponent. Numerically every sum involved shows square-root cancellation (§7).

## 0. Notation (as in SQSIEVE)
(★) 4uBC − u − B = n. The block 𝔅(U,V,W) is u ∈ (U,2U], B ∈ (V,2V], C ∈ (W,2W], and N(U,V,W) is its count; U ≤ V.

*Strip coordinates.* k = uB, s = u + B = 4Ck − n, f(C,k) := s² − 4k (= (u − B)² on solutions).

*Weights and sums.*
* Φ ∈ C_c^∞, 0 ≤ Φ ≤ 1, Φ = 1 on [1,4], supp Φ ⊂ [1/2,5] (SQSIEVE §4.1).
* ω(C,k) := 1_{(W,2W]}(C)Φ((4Ck − n)/V), with 𝒜 := supp ω and w(a) := Σ_{f(C,k)=a} ω(C,k).
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

**Lemma 2.1 (sizes at the balanced block; PROVED).** Assume W ≥ 2V.
(a) Each C carries at most one k with ω(C,k) ≠ 0.
(b) |𝒜| ≤ Σ_{m∈I}τ(m) ≪_ε V n^ε, where I = ((n + V/2)/4, (n + 5V)/4].
(c) Every value a = f(C,k) with (C,k) ∈ 𝒜 satisfies |a| ≤ 25V² + 4(n + 5V)/(4W). In the balanced block this is ≪ V².
*Proof.* (a) Consecutive k change s = 4Ck − n by 4C > 4W ≥ 8V, while ω ≠ 0 forces s ∈ [V/2, 5V], an interval of length
less than 8V. (b) The map (C,k) ↦ m = Ck is at most τ(m)-to-one, and ω ≠ 0 forces 4m − n ∈ [V/2, 5V]. (c) f = s² − 4k,
where 0 < s ≤ 5V and 0 < 4k = (n + s)/C ≤ (n + 5V)/W. ∎

**The six exact forms (PROVED identities; sizes from Lemma 2.1).**
* **(F1) Strip / lattice-point form.** S_Q = Σ_{(C,k)} ω(C,k)g_Q(C,k), with g_Q(c,k) := χ_Q(f(c,k)). The function g_Q is
  Q-periodic in each variable, since f mod Q depends only on (c mod Q, k mod Q). The points are the ≍ V lattice points of
  a hyperbolic strip of area ≍ V and width < 1 in k.
* **(F2) Divisor form** (SQSIEVE Remark 2). S_Q = Σ_m Φ((4m − n)/V) Σ_{C|m, W<C≤2W} χ_Q((4m − n)² − 4m/C). The m-range
  is an interval of length ≍ V ≍ m^{1/4} at m ≈ n/4. The divisors C range over (W, 2W] with W ≍ √m.
* **(F3) Poisson (ℓ, C) form** (SQSIEVE Lemma P). S_Q = Σ_{ℓ∈ℤ} Σ_{C∈(W,2W]} a_ℓ(C) e(−ℓn/(4CQ)) G^{(Q)}_C(ℓ), with
  a_ℓ(C) = (V/(4CQ))Φ̂(ℓV/(4CQ)) and G^{(Q)}_C(ℓ) = Σ_{k mod Q} χ_Q(f(C,k))e(ℓk/Q). The coefficients are *Kloosterman
  sums* (SQSIEVE Lemma W), not Jacobi symbols. The effective support is |ℓ| ≤ L := (8QW/V)n^ε ≍ QV n^ε and C ∈ (W,2W]:
  ≍ QV³ terms, with |a_ℓ| ≍ 1/(QV) and |G| ≤ 4√Q on good classes.
  * The ℓ¹-mass is ≍ √Q·V² (the trivial bound; B2 Parseval argument).
  * The random-phase (ℓ²) benchmark is ≍ V^{1/2}.
  * The target is V^{1−η}. A proof must therefore save a factor √Q·V^{1+η} out of the √Q·V^{3/2} available to
    square-root cancellation.
* **(F4) Additive-twist form.** S_Q = Σ_{(a,b) mod Q} ĝ_Q(a,b)T_Q(a,b), where ĝ_Q(a,b) := Q^{−2}Σ_{c,k mod Q}g_Q(c,k)e(−(ac+bk)/Q)
  and T_Q(a,b) := Σ_{(C,k)}ω(C,k)e((aC + bk)/Q).
* **(F5) Real-character bilinear form** (the only Jacobi-symbol bilinear form present). The square sieve needs
  Σ⁽²⁾(w) := Σ_{q≠q′∈𝒫}S_{qq′}(w) = Σ_Q β_Q Σ_a w(a)(a/Q), with β_Q := #{ordered (q,q′): q ≠ q′, qq′ = Q} ∈ {0, 2}. Its
  supports are Q ∈ (P², 4P²] and a ∈ [−X, X] with X ≍ V². The a-support is *sparse*: |supp w| ≤ |𝒜| ≍ V points in a
  range of length ≍ V². By reciprocity (a/Q) = ±(Q/a), so the transposed form (modulus = strip value) is the same object.
* **(F6) Pair / 2-cycle form** (HYP2CYCLE Prop 2). N counts (u,B) ∈ (U,2U]×(V,2V] with 4uB | n + u + B and quotient in
  (W,2W], i.e. u | n + B, B | n + u and the 2-adic condition. Every solution is a factorisation m = 4uBC of an integer
  m ∈ (n, n + 4V] with u + B = m − n. Any approach to (T) is therefore a statement about the multiplicative structure of
  the integers in an interval of length 4n^{1/4} (Assessment; this is just a restatement).

**Lemma 2.2 (the additive weights; PROVED).** For Q = qq′ as above:
(i) Σ_{(a,b) mod Q}|ĝ_Q(a,b)| ≤ Q;
(ii) |ĝ_Q(0,0)| ≤ 1/Q;
(iii) S_Q = ĝ_Q(0,0)·Σω + Σ_{(a,b)≢(0,0)} ĝ_Q(a,b)T_Q(a,b), hence |S_Q| ≤ |𝒜|_ω/Q + Q·max_{(a,b)≢0}|T_Q(a,b)|, where
|𝒜|_ω := Σω.

*Proof.*
(i) By Parseval, Σ_{a,b}|ĝ|² = Q^{−2}Σ_{c,k}|g_Q|² ≤ 1. Cauchy–Schwarz over the Q² pairs then gives Σ|ĝ| ≤ Q.
(ii) We have Q²ĝ(0,0) = Σ_c Σ_k χ_q(f)χ_{q′}(f). By CRT in (c,k) this factors as (Σ_{c,k mod q}(f/q))·(Σ_{c,k mod q′}(f/q′)).
By SQSIEVE Lemma W(a), Σ_{c,k mod q}(f/q) = Σ_c K_q(c), and K_q(c) behaves as follows:
* if q ∤ n, K_q(c) is 0 at c ≡ 0, q − 1 at the single class q | 4cn + 1, and −1 at the other q − 2 classes, so the total
  is 1;
* if q | n, there is no class with q | 4cn + 1, so the total is −(q − 1).
Hence |Q²ĝ(0,0)| ≤ (q − 1)(q′ − 1) < Q.
(iii) Expand g_Q in additive characters of (ℤ/Q)² and insert this into (F1). The bound then follows from (i) and (ii). ∎

*EVIDENCE.* For a prime modulus q₀ = 61, Σ|ĝ| = 53.86 ≈ 0.88·q₀ in every run of §7, so (i) is sharp up to a constant.

## 3. Proposition M: square-mimic obstruction for every character-side input (PROVED)

**Setting.** Let 𝒫 be any set of P₀ ≥ 2 odd primes. Call a = m² (m ≥ 1) *admissible* if gcd(m, ∏𝒫) = 1.
* For a finitely supported weight w ≥ 0 on ℤ∖{0}, put N_□(w) := Σ_{a admissible} w(a) and σ(a) := Σ_{q∈𝒫}(a/q).
* Heath-Brown's identity is Σ_a w(a)σ(a)² = Σ_a w(a)(P₀ − ν(a)) + Σ⁽²⁾(w), where ν(a) := #{q ∈ 𝒫 : q | a}.
* Admissible squares have σ = P₀, so
  P₀²N_□(w) ≤ P₀‖w‖₁ + Σ⁽²⁾(w).      (3.1)
* An *input* is a function Ψ on a class 𝔚 of weights with Σ⁽²⁾(w) ≤ Ψ(w) for all w ∈ 𝔚. Its *output* is the derived
  bound β_Ψ(w) := (P₀‖w‖₁ + Ψ(w))/P₀² ≥ N_□(w).

**Proposition M.**
(i) If w′ ∈ 𝔚 is supported on admissible squares, then Ψ(w′) ≥ Σ⁽²⁾(w′) = P₀(P₀ − 1)‖w′‖₁.
(ii) *(Sup-norm / support / range inputs.)* Let 𝔚 = 𝔚(X, K, h) := {w : supp w ⊂ [−X, X], |supp w| ≤ K, ‖w‖_∞ ≤ h}, and let
Ψ be constant on 𝔚 (a bound depending only on X, K, h). Then Ψ ≥ P₀(P₀ − 1)h·min(K, A(X)), where A(X) := #{admissible
squares ≤ X}. So for every w ∈ 𝔚, β_Ψ(w) ≥ (1 − 1/P₀)h·min(K, A(X)).
(iii) *(Square-class ℓ² inputs.)* Put D(w) := Σ_{a,a′: aa′ ∈ {m² : m ≥ 1}} w(a)w(a′), and let Ψ(w) = F(D(w)) be valid
for all w, with F non-decreasing. Then F(D) ≥ P₀(P₀ − 1)√D for every D ≥ 0, and β_Ψ(w) ≥ (1 − 1/P₀)√D(w) ≥
(1 − 1/P₀)N_□(w). Moreover, using such an input requires a numerical upper bound D(w) ≤ D₀. Any such bound already
gives N_□(w) ≤ √D₀ directly, because N_□(w)² ≤ D(w) (pairs of admissible squares). So the route adds nothing to its
own input.

*Proof.*
(i) For a admissible, (a/qq′) = 1 for every pair, and there are P₀(P₀ − 1) ordered pairs.
(ii) Let w′ := h·1_𝒮, where 𝒮 is a set of min(K, A(X)) admissible squares ≤ X. Then w′ ∈ 𝔚, so (i) gives Ψ = Ψ(w′) ≥
P₀(P₀ − 1)h|𝒮|. Insert this into β_Ψ.
(iii) Put w′ := √D·δ₁, which is admissible since gcd(1, ∏𝒫) = 1. Then D(w′) = D, so by (i)
F(D) ≥ Σ⁽²⁾(w′) = P₀(P₀ − 1)√D. Hence β_Ψ(w) ≥ (P₀ − 1)√D(w)/P₀. Finally D(w) ≥ Σ_{a,a′ admissible}w(a)w(a′) = N_□(w)²,
since a product of two squares is a square. ∎

**Corollary M′ (the named tools; PROVED relative to the cited statements).**
(a) *Heath-Brown, Acta Arith. 72 (1995), Cor 2.* This is the large sieve for real characters with non-squarefree
variables; its norm is Σ_{n₁n₂=□}|a_{n₁}a_{n₂}| = D(w), verified in LIT_CHECK §1. Used as an input to the square sieve
(directly, after Cauchy–Schwarz over Q, or through the transposed form), it is of type (iii). Its output is
≥ (1 − 1/P₀)√D(w) ≥ (1 − 1/P₀)N_□(w), so it is circular in the sense of M(iii). Thm 1 itself needs squarefree a, so it
applies only after grouping by square classes, which produces exactly D(w). This turns SQSIEVE Remark 3's Assessment into
a theorem, and in a sharper form: the obstruction is not "worse than trivial" but "circular".
(b) *Heath-Brown Cor 4 and every sup-norm bilinear Jacobi bound valid for all |a_m|, |b_n| ≤ 1 on given ranges.* Cor 4 is
Σ_{m≤M}Σ_{n≤N}a_m b_n(n/m) ≪ (MN)^ε(MN^{1/2} + M^{1/2}N) (LIT_CHECK §1). This applies equally to the
Friedlander–Iwaniec-type bound, whose exact statement was not located (LIT_CHECK §2a), so it is treated only through this
clause. Such a bound depends on w only through (X, K, h), so it is of type (ii).
* For the strip, K = |supp w| ≤ |𝒜| and X ≍ V² (Lemma 2.1(c)). The admissible m ≤ √X number at least
  √X(1 − Σ_{q∈𝒫}1/q) − P₀ ≫ V, since Σ_{q∈(P,2P]}1/q ≪ 1/log P. So min(K, A(X)) ≍ V in general, and = K in the
  computed strips (|𝒜| ≈ 0.34V).
* So the output is ≥ (1 − 1/P₀)min(|supp w|, A(X)), which is of the trivial order V: no saving over N ≤ |𝒜|.
* Cor 4's own value with M = 4P², N ≍ V² gives an output ≫ (MN)^ε(V + V²/P), larger still.
(c) *Conrey–Farmer–Soundararajan, JNT 82 (2000), Thm 1* is an asymptotic for the unweighted sum over the *full* odd
boxes m ≤ X, n ≤ Y (LIT_CHECK §2b). The weight w is a sparse subset of density ≍ 1/V; writing it as a combination of
full boxes needs ≥ |supp w| boxes. Inapplicable (Assessment).
(d) *Pólya–Vinogradov / Burgess.* In the a-variable, supp w is not an interval. In (C,k)-coordinates each C carries ≤ 1
point (Lemma 2.1(a)) and k = k(C) is not a polynomial in C, so there is no interval structure to exploit. In the modulus
variable Q (e.g. an "integer square sieve" with Q over an interval), (a/·) is a non-principal character for non-square a.
PV/Burgess therefore bound only the *non-square* part Λ_non of Λ := Σ_a w(a)|Σ_Q(a/Q)|² = Λ_□ + Λ_non. An upper bound on
Λ_non bounds Λ_□ *from below* in terms of Λ, not from above, and an upper bound on Λ is again Σ_{Q,Q′}S_{QQ′} (strip
side). Wrong side; no input (PROVED as stated, an identity-level remark).

*Reading.* Prop M is the precise form of "the large sieve does not see sparsity". Every bound that is uniform over
weights with the same norms is attained, or nearly attained, by a weight on squares, and squares are exactly what the
sieve counts. So the Jacobi-symbol toolbox cannot supply (T′): an input must use the *strip structure* of 𝒜.

## 4. Theorem R: what the strip side must supply (PROVED; conditional consequences)

**Hypothesis TS(δ; P) (twisted strip equidistribution).** For every Q = qq′ with q ≠ q′ primes in (P,2P], and every
(a,b) ≢ (0,0) mod Q:
  |T_Q(a,b)| = |Σ_{(C,k)} ω(C,k)e((aC + bk)/Q)| ≤ V^{1−δ}.
This is equivalent, up to factors Q^{O(1)}, to power-saving equidistribution of the strip points among the classes
(C mod Q, k mod Q). It contains *no quadratic character*.

**Theorem R.** At the balanced block (W ≥ 2V, (log n)² ≤ P ≤ V), uniformly in odd n:
  N(U,V,W) ≪_ε n^ε [ V/P + P²·max_{Q,(a,b)≢0}|T_Q(a,b)| ].
Consequently:
* TS(δ; V^{δ/3}) ⇒ N(U,V,W) ≪_ε n^ε V^{1−δ/3} (a power saving for (T));
* the square-root version |T_Q| ≪ V^{1/2+ε} for Q ≤ 4V^{1/3} ⇒ N ≪ n^{5/24+ε};
* square-root cancellation in S_Q itself, |S_Q| ≪ V^{1/2+ε} for Q ≤ 4V, ⇒ N ≪ n^{1/8+ε} (SQSIEVE Remark 1).

*Proof.*
* By SQSIEVE Lemma 1′ and (4.1), N ≤ 2[(4/P₀)S₁ + 4max|S_Q|] + τ(n), with S₁ = |𝒜|_ω ≪ Vn^ε (Lemma 2.1(b)).
* The hypotheses of (4.1) hold: P₀ ≫ P/log P, and 2^{P₀} ≥ 25V² for P ≥ (log n)².
* Lemma 2.2(iii) gives max|S_Q| ≤ Vn^ε/P² + 4P²·max|T_Q|.
* For the first consequence, choose P = V^{δ/3}; for the second, P = V^{1/6}. ∎

**Proposition R′ (the χ_Q-structure is the only escape; PROVED).** Call an S_Q-bound *twist-blind* if it bounds
|Σω·g| by the same quantity B_Q for every Q-periodic g with ‖g‖_∞ ≤ 1 and mean zero over (ℤ/Q)². A twist-blind bound
B_Q ≤ V^{1−η} implies |T_Q(a,b)| ≤ V^{1−η} for all (a,b) ≢ 0, i.e. TS(η).
*Proof.* g = e((ac + bk)/Q) has modulus 1 and mean zero for (a,b) ≢ 0. ∎

So a power saving at the balanced block via the square sieve needs either TS (strip equidistribution modulo small Q) or a
use of the specific Kloosterman structure of ĝ_Q / G_C(ℓ) that goes beyond the triangle inequality. SQSIEVE Prop B2
excludes the triangle-inequality use for its implementation class.

## 5. Calibration: TS at the balanced block is a short-interval divisor problem at y = x^{1/4}

**Identity (PROVED).** Put x := (n + 3V)/4 (the centre of I in Lemma 2.1) and y ≍ V. Then T_Q(0,0) = |𝒜|_ω =
Σ_m Φ((4m − n)/V)τ_{(W,2W]}(m), where τ_{(W,2W]}(m) := #{C | m : W < C ≤ 2W}. This is a smoothed short-interval sum of a
dyadically restricted divisor function, with y ≍ x^{1/4}. Its error term is the dyadic ψ-sum
Σ_{C∈(W,2W]}[ψ(x₁/C) − ψ(x₂/C)] with x₂ − x₁ ≍ y and C ≍ √x. For (a,b) ≢ 0, T_Q(a,b) is the same sum with the additively
twisted divisor function Σ_{Ck=m}e((aC + bk)/Q) (an Eisenstein-type coefficient of level Q).

**(5.1) Best known pointwise input (Assessment; literature-anchored).** Li–Yang (arXiv:2308.14859, Thm 1.2; LIT_CHECK
§5a) give Δ(x) ≪ x^{θ*+ε} with θ* = 0.3144831…, hence short-interval asymptotics only for y ≥ x^{θ*+η}. We assume the same
methods bound the dyadic ψ-sums above (Assessment). Then the best pointwise error for |𝒜|_ω is x^{θ*+ε} ≍ V^{4θ*+ε} =
V^{1.2579…}. This **exceeds |𝒜| ≍ V itself**: no non-trivial pointwise estimate is known even for the untwisted strip
count. In exponents of V, the deficit to TS(δ) is 4θ* − 1 + δ = 0.2579 + δ. Our literature check found no pointwise
short-interval result below x^{0.3} (LIT_CHECK §5a; search-limited, not a non-existence claim).

**(5.2) Exponent pairs (PROVED as a computation of the bound expression).** Apply Poisson in k (Lemma P with Q = 1 and a
frequency a/Q in C) to T_Q(a,0):
  T_Q(a,0) = Σ_h Σ_{C∈(W,2W]} (V/(4C))Φ̂(hV/(4C)) e(aC/Q − hn/(4C)).
* The h = 0 term is ≪ QV/W by partial summation.
* For 1 ≤ |h| ≤ (8W/V)n^ε, the phase F(C) = aC/Q − hn/(4C) (|a| ≤ Q/2) has |F′| ≍ |h|. Indeed n/(4C²) ≥ n/(16W²),
  which is ≥ 16 for W = √n/16, so the h-term dominates a/Q.
* An exponent pair (κ, λ) gives |Σ_C e(F)| ≪ |h|^κW^λ, so the bound expression is ≍ Σ_{h ≤ V}(V/W)h^κW^λ ≍ V^{κ+2λ}.
* Since λ ≥ 1/2, κ + 2λ ≥ 1, with equality only at the conjectural pair (0, 1/2).
* The deficits in V-exponents: Bourgain's (13/84 + ε, 55/84 + ε) gives V^{0.464}; (1/6, 2/3) gives V^{1/2}; the
  conjectural pair gives V^{0}, i.e. exactly trivial, never a saving.
* This is SQSIEVE Prop B2 in the Q = 1 / additive setting: per-h bounds ≥ c√W cannot save (B2(a), Fejér).

**(5.3) Mean square (EVIDENCE + literature).** Jutila's mean-square asymptotic, as transcribed by Ivić (JTNB 21 (2009);
LIT_CHECK §5b), is ∫_X^{2X}(Δ(x + h) − Δ(x))²dx ~ (8/π²)Xh log³(√X/h). So for typical x the short-interval error is
≍ √(y log³). In our strips (§7) the count error is (1.2–1.6)·√|𝒜|, and S_Q and T_Q are ≈ 1·√|𝒜| (rms). The truth is
square-root, consistent with both.

**(5.4) Other bilinear tools on the strip side.**
* *DFI (Kloosterman fractions; HYPKLOOST LIT_CHECK §3).* Detecting B | n + u or u | n + B by additive characters in the
  (u,B)-box gives numerators a ≍ hn ≥ n ≍ V⁴, with M = N ≍ V. Hence a/(MN) ≍ V². DFI Thm 1's term
  ‖α‖‖β‖(a/MN)^{1/2}min(M,N) ≍ V³ exceeds the trivial MN ≍ V² by V. DFI Thm 2's ‖α‖‖β‖(a + MN)^{3/8}(M + N)^{11/48} ≍
  V^{2+35/48} exceeds it by V^{35/48}. Both fail by a power, consistent with HYPKLOOST's necessary conditions.
  (PROVED as arithmetic on the cited bounds, for forms with these ranges; the exact forms (F6) are not separable box
  forms, so this is the best case.)
* *Double large sieve (Bombieri–Iwaniec).* Apply it to (F3) with x_ℓ = ℓ (|ℓ| ≤ L ≍ QV) and the Kloosterman sum opened,
  y_{C,k} = (4Ck − n)/(4CQ) ∈ [−1/2, 1/2] (WQ points). Then XY ≍ QV. The spacing sums are ≍ L|a|² and ≍ (WQ)²/(QV)
  (the y's are spread), and the bound is ≍ V^{3/2}Q^{1/2}: a deficit of (QV)^{1/2}V^{η} against the target. Even the
  diagonal parts of the spacing sums alone, Σ|α_ℓ|² ≍ 1/(QV) and Σ|β|² ≥ WQ/2, make the expression
  ≥ (QV·(1/(QV))·(WQ/2))^{1/2} ≍ V√Q, already above the trivial V. *Assessment:* the inequality's exact constants
  were not re-verified (LIT_CHECK §4); the computation assumes the generic (1 + XY)·(spacing sums) shape and
  separability of a_ℓ(C) in (ℓ, C), which costs n^ε by a standard separation of variables. Opening the Kloosterman sum reverts the Poisson step, so the double large sieve sees
  only near-coincidences of the y's, i.e. no strip structure.
* *Determinant method.* Closed in black-box form by HYP2CYCLE Prop D (criticality V/T = 1).

## 6. Summary of deficits at the balanced block (exponents of V = n^{1/4}; the target is V^{1−η})

| tool class | how it enters | output / deficit | status |
|---|---|---|---|
| HB real-character large sieve (Cor 2) | (F5), norm D(w) | output ≥ (1−1/P₀)√D(w) ≥ N: circular | PROVED (Prop M(iii)) |
| HB Cor 4, FI-type sup-norm bilinear Jacobi | (F5), (X,K,h) | output ≥ (1−1/P₀)·|supp w| ≍ V: no saving | PROVED (Prop M(ii)) |
| CFS transition mean values | full boxes only | inapplicable to sparse w | Assessment |
| PV / Burgess | a-variable: no interval; Q-variable: bounds non-squares only | no input | PROVED (remark) |
| DFI Thm 1 / Thm 2 | (u,B) Kloosterman fractions, a ≍ hn | × V / × V^{35/48} above trivial | PROVED (arithmetic) |
| double large sieve | (F3) opened | ≍ V^{3/2}Q^{1/2}: × (QV)^{1/2} | Assessment |
| exponent pairs on C-sums (incl. B-process) | (F3)/(F4) per h or ℓ | V^{κ+2λ} ≥ V; Bourgain V^{1.464}; conj. pair V^{1} | PROVED (bound expression) = B2 |
| best pointwise short-interval divisor bound (Li–Yang) | T_Q(0,0) and twists | V^{4θ*} = V^{1.258} | Assessment (lit.) |
| additive expansion + square-root T_Q | Thm R | N ≪ n^{5/24+ε} | CONDITIONAL |
| square-root S_Q | (T′) | N ≪ n^{1/8+ε} | CONDITIONAL |
| determinant method (black box) | surface | ≥ trivial | PROVED elsewhere (HYP2CYCLE D) |

## 7. Computations (EVIDENCE; exact integer arithmetic for counts and Jacobi symbols, double precision for Fourier data)

**7.1 Census** (`z54_bilinjac_census.c`; CERTIFIED for the range). For every odd n ≤ 10⁹, put
N_bal(n) := #{(★) triples : n^{1/4}/2 < u, B ≤ 2n^{1/4}}.
* The mean is 0.4805 in each decade 10⁵–10⁹, matching (ln 4)²/4.
* The maximum over all odd n ≤ 10⁹ is 20, at n = 635 674 641 = 3·7·30 270 221.
* Over primes p ≡ 1 (24) the maximum is 14, at p = 250 810 249.
* Odd squares give 0 (T1).
* Decade maxima: 6, 8, 8, 12, 16, 20.

The distribution has a heavier-than-Poisson tail but N_bal is tiny against n^{1/4} ≈ 159 (`census_1e9.txt`). (T) is true
by a huge margin in the range; the obstruction is purely technological.

**7.2 Strip statistics** (`z54_bilinjac_strip.c`, `z54_bilinjac_multi.py`, `z54_bilinjac_summarize.py` →
`strip_summary.txt`). Setup:
* Balanced block V = n^{1/4}, W = √n/16, sharp window s ∈ (2V, 4V].
* At each scale: 100 consecutive primes p ≡ 1 (24), 30 odd squares, 30 near-squares m² + 4.
* P ∈ {√V, V/4}, ≤ 300 pairs per n.
* Additive analysis at q₀ = 61.

Results (means over n unless "max"):

| scale | V | |𝒜| | count err rms /√|𝒜| | S_Q rms /√|𝒜| | max S_Q /√|𝒜| | max over 100 sub-rectangles | E(c,k) rms / Poisson | max_{(a,b)≠0}|T|/√|𝒜| | additive bound / √|𝒜| |
|---|---|---|---|---|---|---|---|---|---|
| 10¹⁰ | 316 | 108 | 1.31–1.39 | 0.90–1.00 | 4.33 | 4.72 | 1.01 | 3.44 | 48.1–48.3 |
| 10¹² | 1000 | 333–348 | 1.24–1.64 | 0.93–1.00 | 3.94 | 5.08 | 1.01 | 3.56 | 48.1–48.2 |
| 10¹⁴ | 3162 | 1056–1084 | 1.41–1.54 | 0.96–1.01 | 4.27 | 5.32 | 1.01 | 3.54 | 48.2–48.5 |

* Primes, odd squares and near-squares are indistinguishable in every column (T1-blind, as an n-uniform upper-bound input
  must be).
* Class counts are Poisson.
* All maxima are within the Gaussian-extreme range for the number of samples.
* The additive triangle bound (Lemma 2.2(iii)) overshoots |S_{q₀}| by ≈ 0.8·q₀. This is the Q-loss in Thm R; it is
  harmless for P = V^{δ/3}.
* The test primes of FRONTIER §4 item 14 are ≤ 8.8·10⁶. At their scale the balanced block is degenerate (V ≤ 5,
  |𝒜| ≤ 6), so `strip_testprimes.txt` is a formal control only.

**7.3 The actual Poisson (ℓ, C) bilinear form** (`z54_bilinjac_shells.c`; `shells_1e10.txt`, `shells_1e12.txt`). Setup:
Gaussian Φ(t) = e^{−π(t−3)²}. The form was computed term by term over the full (ℓ, C) support: 9.2·10⁸ terms (Q = 143)
and 2.1·10⁹ terms (Q = 323) at 10¹⁰, and 3.1·10⁹ terms at 10¹². Each dual total matches the direct strip sum to
≤ 2.1·10⁻¹¹ (Lemma P check). Instances:
* n = 10¹⁰ + 33 (prime), 100 003² (odd square), 100 003² + 4, with Q = 11·13;
* n = 10¹⁰ + 33 with Q = 17·19;
* n = 10¹² + 177 (prime) and 1 000 001² (odd square), with Q = 3·5.

For each dyadic shell |ℓ| ~ 2^j we record |shell sum|, the random-phase benchmark ℓ² = (Σ|term|²)^{1/2}, and the trivial
ℓ¹. Results:
* Over the 89 shells with ℓ ≠ 0 and non-negligible mass (|sum| > 10⁻³), |sum|/ℓ² has median 0.74 and maximum 3.08. The
  ℓ = 0 shell is the main term ĝ(0,0)-type and is not random.
* Totals: ℓ¹ = 45 686 against ℓ² = 5.74 at 10¹⁰ (Q = 143; ℓ¹/ℓ² ≈ 8 000), and ℓ¹ = 151 760 against ℓ² = 8.95 at 10¹²
  (Q = 15; ≈ 17 000).
* Within shells, the joint (ℓ, C) sums cancel to square-root size. The saving needed to reach the trivial scale
  (ℓ¹/V ≈ 145–152) is a small fraction of the saving available to square-root cancellation (ℓ¹/ℓ² ≈ 8 000–17 000).
* Partial sums from the top shell down wander at the √|𝒜| scale (cumulative columns).

So the bilinear estimate SQSIEVE asks for is true in the computed range with room. The missing ingredient is a proof
technology for TS-type equidistribution at y = x^{1/4}.

## 8. FRONTIER §4 hard screens (for Thm R / the (T′) route)
1. **T1 (odd squares).** This is an n-uniform upper bound, valid at m² (where N = 0). It cannot imply positivity. All
   computed sums are T1-blind (§7.2), as they must be.
2. **8/131.** It transfers to other numerators (only the strip geometry is used). Harmless for an upper bound; silent on
   8/131.
3. **Tied modulus.** The tie is encoded as the square condition on f. The square sieve uses only fixed auxiliary moduli
   Q, and the hard part is the short-interval strip (F6). B2 is untouched.
4. **Fixed p.** Passed: pointwise in n. Averages are over (C,k), ℓ, (a,b) and the auxiliary primes only. The census
   (§7.1) is a range statement, not an input.

## 9. Verdict
**Narrowed.** What was proved:
* **Prop M (PROVED).** Every character-side input to the square sieve is either circular or trivial. Inputs of
  square-class ℓ² type (Heath-Brown's real-character large sieve, Cor 2) return at least √D(w) ≥ N, so they need as
  input a bound that already implies the conclusion. Sup-norm/support/range inputs (Heath-Brown Cor 4, FI-type bilinear
  Jacobi bounds) return at least (1 − 1/P₀)|supp w|, the trivial bound. CFS and PV/Burgess do not apply. This closes the
  "bilinear sums of Jacobi symbols" reading of the kickoff: after Poisson the (ℓ, C) coefficients are Kloosterman sums,
  and the only Jacobi-symbol bilinear form, (F5), is killed by Prop M.
* **Thm R (PROVED) + Prop R′.** The square sieve at the balanced block needs exactly TS(δ), power-saving
  equidistribution of the strip modulo small Q (no quadratic character, loss Q), unless one exploits the specific
  Kloosterman structure beyond the triangle inequality. Conditional benchmarks: TS(δ) ⇒ N ≪ V^{1−δ/3+ε}; square-root TS
  ⇒ n^{5/24+ε}; square-root S_Q ⇒ n^{1/8+ε}.
* **Calibration.** TS at the balanced block is a twisted short-interval divisor problem at y = x^{1/4}. Exponent pairs
  give V^{κ+2λ} ≥ V (the conjectural pair is exactly trivial). The best pointwise divisor technology gives V^{1.258} even
  for the untwisted count (Assessment, literature). DFI is off by V (Thm 1) or V^{35/48} (Thm 2). The double large sieve
  is off by (QV)^{1/2} (Assessment).

What survives: (1) a genuinely two-dimensional (Bombieri–Iwaniec–Huxley-type) pointwise short-interval estimate at
y = x^{1/4} for (twisted) divisor sums restricted to C ≍ √x. This is beyond the current exponent x^{θ*}, θ* = 0.3145, by
x^{0.0645} (Assessment). (2) An argument using the specific Kloosterman structure of G_C(ℓ) jointly with the phase
e(−ℓn/(4CQ)), not via the triangle inequality (not excluded by B2 or R′).
EVIDENCE (§7) says the truth has square-root cancellation everywhere, so neither route is blocked by the truth.

## 10. Proposed FRONTIER §7.1 text (do NOT edit FRONTIER here)
> *(z54, `Z54_BILINJAC.md`; internal.)* **Balanced block: the Jacobi-symbol toolbox is closed; what remains is a
> short-interval divisor problem.** Square-mimic theorem (Prop M, PROVED): every square-sieve input that sees the
> weights only through square-class ℓ² mass (Heath-Brown's real-character large sieve) returns ≥ √D(w) ≥ N (circular).
> Every input that sees them only through sup-norm/support/range (Heath-Brown Cor 4, FI-type bilinear Jacobi bounds)
> returns ≥ (1 − 1/P₀)|supp w| (trivial). Pólya–Vinogradov/Burgess and CFS do not apply. After Poisson the (ℓ, C)
> coefficients are Kloosterman sums, not Jacobi symbols. Thm R (PROVED): at the balanced block,
> N ≪ n^ε[V/P + P²·max|T_Q(a,b)|], with T_Q the additively twisted strip sums mod Q = qq′ ≍ P². So power-saving
> equidistribution of the strip modulo small Q (TS(δ)) gives N ≪ p^{(1−δ/3)/4+ε}, and square-root TS gives p^{5/24+ε}.
> A twist-blind S_Q-bound implies TS (Prop R′). TS is a twisted short-interval divisor problem at y = x^{1/4}:
> exponent pairs give V^{κ+2λ} ≥ V (the conjectural pair exactly trivial). The best pointwise divisor exponent
> (Li–Yang θ* = 0.3145) gives V^{1.258} even untwisted (Assessment). DFI misses by V, the double large sieve by
> (QV)^{1/2} (Assessment). EVIDENCE: the true sums (S_Q, sub-rectangles, T_Q, and the actual (ℓ, C) form shell by shell
> at 10¹⁰–10¹⁴) are all square-root, and max N_bal = 20 over odd n ≤ 10⁹. Survives: a 2-D pointwise short-interval
> estimate at y = x^{1/4}, or a joint use of the Kloosterman structure.
In §6 add: "Real-character large sieve / bilinear Jacobi bounds as square-sieve inputs → circular or trivial (square
mimic) → `Z54_BILINJAC` Prop M".

## 11. Bottom line
The kickoff hoped that the missing bilinear (ℓ, C) cancellation at the balanced block might be a bilinear sum of Jacobi
symbols, open to Heath-Brown's large sieve and its relatives. It is not. After Poisson the coefficients are Kloosterman
sums. The only genuinely Jacobi-symbol bilinear form, the sieve's (Q, a) form, is closed by a short square-mimic
argument: tools that see the weights only through their norms cannot tell the strip from a set of squares, which is
exactly what the sieve counts. What the square sieve really needs at the balanced block is equidistribution, with a power
saving, of ≍ n^{1/4} lattice points of a thin hyperbolic strip modulo small moduli (Thm R). That is a twisted divisor
problem in an interval of length x^{1/4}. Even its untwisted count lies beyond every pointwise bound in the literature we
checked, and single-variable exponent sums stop exactly at the trivial exponent. Numerically all the relevant sums cancel
to square-root size, and the balanced block holds at most 20 solutions for every odd n ≤ 10⁹. So (T) is true with room in
the computed range, but a proof needs a new pointwise short-interval estimate. This is upper-bound work: it can sharpen
the §7.1 benchmark, never positivity. ES remains open.

## 12. Reproduction (all with `ulimit -v 4000000` or 6000000; timings on one core)
```
gcc -O2 -o /tmp/z54census scripts/z54_bilinjac_census.c -lm
ulimit -v 6000000; timeout 1500 /tmp/z54census 1000000000 > data/z54/bilinjac/census_1e9.txt          # ~2 min, 2 GB
gcc -O2 -o /tmp/z54strip scripts/z54_bilinjac_strip.c -lm
for e in 0 10 12 14; do timeout 1700 uv run --with sympy python scripts/z54_bilinjac_multi.py /tmp/z54strip $e 100 30 \
   data/z54/bilinjac/strip_$( [ $e = 0 ] && echo testprimes || echo 1e$e ).txt; done                 # < 1 min total
uv run python scripts/z54_bilinjac_summarize.py data/z54/bilinjac/strip_testprimes.txt data/z54/bilinjac/strip_1e1*.txt
gcc -O2 -o /tmp/z54shells scripts/z54_bilinjac_shells.c -lm
for a in "10000000033 316 6250 11 13" "10000600009 316 6250 11 13" "10000600013 316 6250 11 13" "10000000033 316 6250 17 19"; \
   do timeout 900 /tmp/z54shells $a; done > data/z54/bilinjac/shells_1e10.txt                        # ~4 min
for a in "1000000000177 1000 62500 3 5" "1000002000001 1000 62500 3 5"; do timeout 1500 /tmp/z54shells $a; done \
   > data/z54/bilinjac/shells_1e12.txt                                                                 # ~6 min
```

## 13. Review log
*(to be filled: hostile review 1)*
