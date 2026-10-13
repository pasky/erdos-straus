# FROBENIUS_FIRING — is ES firing a Frobenius condition? The box-vs-group scale (task O196, spark relay Q)

Status: in progress (O196). **ES is not solved here, nor any infinite case of ES or ES_q.** Labels as in DISCOVERIES.md.
Builds on FF_MUTE.md (O195, CLAIMED, under review R195), FIXED_MODULUS_SHOTS.md ((J)25), UNIT_ORBIT_ES.md ((J)23),
KUDLA_ES.md ((J)13). Scripts `scripts/ff_frob_*`, outputs `data/ff_frob/`.

Notation as in FF_MUTE: q a prime power, R = F_q[T], F = F_q(T), A monic of degree k ≥ 1, P monic irreducible of degree n,
P ∤ A. Over ℤ: p an odd prime, h a Type II modulus (h ≡ 3 mod 4), k_h = (h + 1)/4, Box(k) = {c/j : cj | k}.

## 0. Iteration log

(Q1) The literal question ("is Fire(p) a Frobenius set in a fixed extension?") has a trivial negative answer: Fire(p)
is finite (Prop 1.2). The meaningful questions are (a) *sufficient* Frobenius conditions with a range cut-off, which
need an exponentially complicated field (Thm 1.4, effective no-go), and (b) the *per-modulus* structure: Frobenius
firing is what you get by flipping a per-modulus firing set that is a union of cosets of a *bounded-index* subgroup
(Lemma 1.5). §2 makes (b) quantitative over F_q[T]: Weil certifies firing through an algebraic family iff the
firing set at a degree-d modulus has size ≳ n·q^{d/2} (square-root threshold); the ES box has size q^{o(d)}.

## 1. Framework, and the trivial and effective no-go theorems

**Definition 1.1 (firing).** A *firing relation* is a set Fire ⊂ {inputs} × {moduli}. For ES (Type II, prime
moduli; FIXED_MODULUS_SHOTS Thm 3.1/4.2): (p, h) ∈ Fire iff h ≡ 3 (mod 4) and −p ∈ Box(k_h) (mod h). For ES_q
(Type II; FF_MUTE Prop 5.2(b)): (P, f) ∈ Fire iff f ≡ −1 (mod A) and P ≡ −A·a²d (mod f) for some monic a, d with
ad | (f + 1)/A. For the mute variant ES_q^{(s)} (FF_MUTE Prop 5.2(a)): f ≡ −1 (mod A) and −P/A ∈ ⟨s² mod f⟩.
Fire(P) := {f : (P, f) ∈ Fire} (per input); 𝔉(f) := {P mod f : (P, f) ∈ Fire} ⊂ (R/f)^* (per modulus).
A *sufficient Frobenius condition* for P is a pair (L, C): L/K a finite Galois extension (K = ℚ or F), C ⊂ Gal(L/K)
a nonempty union of conjugacy classes, such that every prime f unramified in L with Frob_f ∈ C lies in Fire(P).
(This is exactly what a Chebotarev/RH existence proof needs.)

**Proposition 1.2 (Fire(p) is finite, so no sufficient Frobenius condition exists; PROVED).**
(a) For p prime, every Type II modulus is ≤ (p + 1)(p + 5)/4 and every Type I modulus is < 3p² (FIXED_MODULUS_SHOTS
Prop 6.1). For ES_q, every Type II modulus has degree ≤ 2n − k (FF_MUTE Prop 5.1).
(b) Hence for every finite Galois L/K and nonempty C, infinitely many unramified primes f with Frob_f ∈ C do not
fire. **No (L, C) is a sufficient Frobenius condition for ES(p) or ES_q(A, P)**, whatever L (fixed or depending on p).
(c) In contrast, for ES_q^{(s)} the pair L = F(√(−PA)), C = {Frob restricted as in Lemma 3.2 of FF_MUTE}, joined with
the Dirichlet condition mod A, is sufficient *on the primes f at which s is a primitive root* — a condition on Frob_f
in the infinite Kummer tower F(μ_∞, s^{1/∞}) (it is not a finite-level condition, but Thm 3.5 of FF_MUTE handles it
by Weil sums at one prime degree d).
*Proof.* (a) cited. (b) Chebotarev (over F: with RH, for the geometric part; constant-field part is a condition on
deg f mod some e, satisfied by infinitely many degrees) gives infinitely many such f. (c) FF_MUTE Lemmas 3.1, 3.2. ∎

So the literal question has a trivial answer; the content is quantitative. Two refinements: a *range-restricted*
condition (only f in the range where certificates live), and the *per-modulus* structure.

**Theorem 1.3 (effective no-go over F_q[T]; PROVED relative to the cited effective Chebotarev theorem).** Let L/F be
a finite Galois extension with group G, constant field F_q (geometric), genus g_L, and let C ⊂ G be nonempty and
conjugation-stable. If every prime f of degree d, unramified in L, with Frob_f ∈ C fires for ES_q(A, P) (Type II),
for *one* degree d ≥ 2n − k + 1, then
`q^{d/2} ≤ c₀·(g_L + |G|·(1 + deg 𝔡_L))`,
where 𝔡_L is the ramification divisor of L/F (absolute constant c₀; with d the least admissible degree,
`g_L + |G|(1 + deg 𝔡_L) ≥ q^{n − k/2}/c₀`).
*Proof.* Effective Chebotarev for function fields (Murty–Scherk, *C. R.* 319 (1994); Fried–Jarden, *Field Arithmetic*,
Prop. 6.4.8; Rosen Thm 9.13B): the number of degree-d primes unramified in L with Frob in C is
(|C|/|G|)·q^d/d + O((|C|/|G|)(g_L + |G|(1 + deg 𝔡_L))q^{d/2}/d). If q^{d/2} > c₀(g_L + |G|(1 + deg 𝔡_L)) this is > 0,
but no prime of degree ≥ 2n − k + 1 fires (Prop 1.2(a)). ∎
*Reading.* A sufficient Frobenius condition valid in the degree range just beyond the certificate range needs genus
(or degree × ramification) exponential in n = deg P, i.e. polynomial in |P| = q^n. The mute field
F(√(−PA)) has genus ≤ (n + k)/2 and the Kummer layers F(μ_ℓ, s^{1/ℓ}) have genus O(ℓ·deg s); FF_MUTE Thm 3.5 uses
moduli of degree d ≈ 2 log_q n. (Caveat on scope: Thm 1.3 asks the condition to be sufficient at one degree beyond
2n − k; a condition sufficient only at degrees ≤ 2n − k is not excluded by Thm 1.3 — see Thm 1.4 for that range.)

**Theorem 1.4 (range-restricted no-go over ℤ; CONDITIONAL on GRH for Dedekind zeta functions).** Let p be a large
prime and X ≥ 3p². Suppose (L, C) is such that every prime h ≤ X unramified in L with Frob_h ∈ C fires (Type I or II).
Then, with G = Gal(L/ℚ) and an absolute c₁, **either** log d_L + |G| log X ≥ X^{1/2}/(6c₁ log X) **or**
|G|·(p^{1+o(1)} + 2 log d_L) ≥ X/(6 log X). In particular the condition cannot hold with [L:ℚ] ≤ p^{1−ε} and
log d_L ≤ p^{1−ε} (p ≫_ε 1).
*Proof.* Under GRH, |π_C(x) − (|C|/|G|)Li(x)| ≤ c₁(|C|/|G|)x^{1/2}(log d_L + |G| log x) (Lagarias–Odlyzko 1977,
Serre 1981 Thm 4). Fire(p) has at most #(Type I/II solutions) ≤ p^{1+o(1)} elements (each solution has one modulus;
Type II: x ≤ p/2 and (y′, z′) is determined by a divisor of x², Type I similarly — FIXED_MODULUS_SHOTS Lemmas 1.1, 4.1).
So π_C(X) − π_C(X/2) ≤ p^{1+o(1)} + ω(d_L) ≤ p^{1+o(1)} + 2 log d_L. With the GRH formula (|C| ≥ 1),
(|C|/|G|)[X/(3 log X) − 2c₁X^{1/2}(log d_L + |G| log X)] ≤ p^{1+o(1)} + 2 log d_L for large X. If the first
alternative fails, the bracket is ≥ X/(6 log X), giving the second. For the last claim: X^{1/2} ≥ √3·p makes the
first alternative false, and |G|(p^{1+o(1)} + 2p^{1−ε}) ≤ p^{2−ε+o(1)} < X/(6 log X) makes the second false. ∎
(Unconditionally, Thorner–Zaman-type lower bounds π_C(x) ≫ (|C|/|G|)Li(x), valid for x ≥ d_L^{c} with an absolute
c, give the same contradiction for every L with d_L ≤ p^{2/c}; much weaker. Citation form not re-checked.)
*(Assessment: Thms 1.3–1.4 are B2/B3 in Chebotarev language: certificates are finitely many and polynomially
bounded, while Chebotarev sets are infinite and equidistributed at the scale √(conductor). They contain no new
arithmetic; their role is to fix the scale against which §2 measures "how mute".)*

## 2. The per-modulus scale over F_q[T]: the square-root threshold

Over F the "flip" from a condition on P mod f to a condition on f is geometric, not only reciprocity: a prime f of
degree d is a Frobenius orbit of roots α ∈ F_{q^d} (F_q(α) = F_{q^d}), T ↦ α identifies R/f with F_{q^d}, and
**P mod f ↦ P(α), an algebraic function of the point α ∈ 𝔸¹(F_{q^d})**. Hence membership of P mod f in a subset S of
G_d := F_{q^d}^* is the condition P(α) ∈ S, and Weil applies to characters of G_d of *every* order — not only to
orders m | q − 1, where it is the reciprocity law of FF_MUTE Lemma 3.2. (Over ℤ, "p mod h" is not a function on a
curve; only bounded-order reciprocity is available. See Remark 2.5.)

**Theorem 2.1 (Weil count for subgroup membership; PROVED).** Let d ≥ 1, m | q^d − 1, B ∈ R monic of degree b, and
P ∈ R irreducible of degree n with P ∤ B. Then
`N_m := #{α ∈ F_{q^d} : B(α)P(α) ≠ 0, P(α)/B(α) ∈ G_d^m}` satisfies `|N_m − (q^d − n − b)/m| ≤ (n + b − 1)q^{d/2}`.
*Proof.* 1_{G^m}(x) = (1/m)Σ_{χ^m = 1} χ(x). For χ ≠ 1 of order e | m, e > 1, χ(P/B) = χ(P·B^{e−1}); the polynomial
P·B^{e−1} has the root set of P with multiplicity 1, so it is not a constant times an e-th power in F̄_q[T], and
Weil's bound (Lidl–Niederreiter Thm 5.41) gives |Σ_α χ(P(α)B(α)^{e−1})| ≤ (#distinct roots of PB − 1)q^{d/2}
≤ (n + b − 1)q^{d/2}. The trivial character contributes q^d − #{roots of PB in F_{q^d}} ∈ [q^d − n − b, q^d]. ∎
(α of degree < d are ≤ 2q^{d/2} in number and can be discarded at that cost; each degree-d prime f contributes d
values α, all with the same membership status since G^m is Frobenius-stable.)

**Proposition 2.2 (the threshold for the expansion method; PROVED).** Let S ⊂ G_d be any subset and write
1_S = Σ_χ ŝ(χ)χ on G_d (ŝ(χ) = |G_d|^{−1}Σ_{x∈S}χ̄(x)), ‖ŝ‖₁ := Σ_χ |ŝ(χ)|. Then for P, B as in Thm 2.1
`|#{α : P(α)/B(α) ∈ S} − |S|·(q^d − n − b)/(q^d − 1)| ≤ (‖ŝ‖₁ − ŝ(1))·(n + b − 1)q^{d/2}`,
and ‖ŝ‖₁ ≥ 1 (Fourier inversion at any x ∈ S). In particular this "character expansion + Weil" argument proves
existence of α only if `|S| > (‖ŝ‖₁ − ŝ(1))(n + b − 1)q^{d/2}`; the necessary condition `|S| ≳ (n + b − 1)q^{d/2}`
holds for every S with ‖ŝ‖₁ ≥ 2ŝ(1) (i.e. every S with |S| ≤ |G_d|/2, as ‖ŝ‖₁ ≥ 1 ≥ 2|S|/|G_d|).
*Proof.* As in Thm 2.1, term by term. ∎
Examples: S = coset of a subgroup of index m: ‖ŝ‖₁ = 1, threshold m < q^{d/2}/(n + b) (Thm 2.1). S = {s^{2j} :
0 ≤ j < J} with s a primitive root (an exponent interval): ‖ŝ‖₁ ≪ log q^d, threshold J ≫ d·(n + b)q^{d/2}.
S = a box {∏ g_i^{e_i} : |e_i| ≤ κ_i} in exponent coordinates (a generalised arithmetic progression of the
discrete logs): ‖ŝ‖₁ ≪ ∏(1 + log(2κ_i + 1)), threshold |S| ≫ (n + b)q^{d/2}·∏ log.
**So structure only buys a logarithmic Fourier norm; the binding constraint is size: Weil-type firing at modulus
degree d requires a firing set of size ≳ n·q^{d/2} (square root of |G_d|), which must moreover be a FIXED algebraic
datum (S, B independent of α).**

**Proposition 2.3 (the ES box is below the threshold at every modulus degree; PROVED).** For ES_q Type II,
𝔉(f) = −A·{a²d : ad | (f + 1)/A} has |𝔉(f)| ≤ τ₃((f + 1)/A) (FF_MUTE Prop 5.2(b)), where τ₃(N) = #{ordered monic
factorisations N = abc}. For deg N = D: τ₃(N) ≤ 3^{Ω(N)} ≤ 3^D, and τ₃(N) ≤ τ(N)² ≤ q^{(2 log 2 + o(1))·D/log_q D}
as D → ∞ (FF divisor bound). Hence |𝔉(f)| < (n + k − 1)q^{d/2}/2 for every d ≥ k when q ≥ 9 and n + k ≥ 3 (3^{d−k} ≤ q^{(d−k)/2} < q^{d/2}), and for every d ≥ d₀(q) when q < 9 (d₀ independent of n). So the expansion method of Prop 2.2
cannot certify an ES_q firing at such d, even for a single P, with any fixed S ⊆ 𝔉(f); a fortiori the box, which
moreover varies with f (its generators are the prime factors of f + 1, not fixed polynomials), is not a
Weil-countable datum.
*Proof of the bounds.* τ₃(N) = ∏_i C(e_i + 2, 2) over N = ∏ g_i^{e_i}, and C(e + 2, 2) ≤ 3^e. The asymptotic form is the
divisor bound τ(N) ≤ |N|^{(log 2 + o(1))/log_q D} over F_q[T] (same proof as over ℤ: split primes by degree at
log_q D) and τ₃(N) = Σ_{a|N} τ(N/a) ≤ τ(N)². ∎
(Small d: the box has O(1) elements while the threshold is ≥ n√q^k; for n large the comparison holds at every d.)

**Remark 2.4 (mute place as a Weil-countable datum; reading of FF_MUTE Thm 3.5).** In ES_q^{(s)} the firing set is
−A⟨s(α)²⟩: its generator is the FIXED polynomial s evaluated at α, so the set is "algebraic in α"; when s(α) is a
primitive root it is the index-2 subgroup (‖ŝ‖₁ = 1), far above the threshold, and Thm 2.1 with m = 2, B = A
counts the α with −P(α)/A(α) a square. The primitive-root condition on s(α) is itself a Weil count (FF_MUTE Lemma
3.4). The interpolating structures between ⟨s⟩ and the box are therefore measured by one number — the size of the
largest fixed algebraic sub-structure of 𝔉(f) — with the threshold ≍ n q^{d/2}.

**Remark 2.5 (ℤ has no geometric flip; Assessment).** Over ℤ the analogue of Thm 2.1 would be a bound for
Σ_{h ≤ X} χ_h(p), χ_h a character of order m of (ℤ/h)^*, uniformly in m up to √h — a sum over moduli with the
input fixed. For m | (small fixed) this is reciprocity (a character of h mod 4p, then Dirichlet/Siegel–Walfisz); for
growing m there is no such tool (it is the "Artin problem with moving order"; the large sieve controls it only on
average over p — B6). So over ℤ Frobenius firing needs *bounded* index uniformly; over F index up to q^{d/2}/n is
allowed. Even the F version leaves ES out by Prop 2.3.
