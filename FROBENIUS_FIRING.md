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

## 3. Construction attempts (task (1)): looking for a Frobenius sub-box

Each entry: the idea, which hypothesis of §§1–2 it tries to violate, outcome (Assessments unless a result is cited).

(F1) *Heegner/ideal dictionary.* Type II with a prime modulus f (campaign letters: ff′ − 4c²dp = 1, f ≡ f′ ≡ −1
mod 4cd) ⟺ **some prime 𝔣 of K_d = ℚ(√−dp) of degree 1 divides α_{c,d} := 1 + 2c√−dp and has N𝔣 ≡ −1 (mod 4cd)**
(PROVED: f | Nα = 1 + 4c²dp, f ∤ 2cdp, so f splits and exactly one 𝔣 | f divides α, as f ∤ 1; conversely
f′ = Nα/f ≡ −1 automatically since Nα ≡ 1 mod 4cd). The second condition is a Frobenius condition (Artin symbol in
K_d(ζ_{4cd})/K_d) but with conductor 4cd moving with the shot; the first is divisibility by a fixed element.
Unioning the first over a *multiplicative group* of β's (𝔣 | 1 + β, β ∈ Γ) would give "−1 ∈ Γ mod 𝔣", a Kummer
condition; here β = 2c√−dp ranges over a box (c | (f + 1)/4d), i.e. −1/(2√−dp) mod 𝔣 ∈ {divisors of (f+1)/4d}.
Same box, new coordinates. Violates nothing.

(F2) *Supersingular torsion ("divisors of f + 1" as torsion).* For a certificate (c, d) with prime f: (−d/f) = −1
(FIXED_MODULUS_SHOTS Rem 2.5 with n = d), so f is inert in ℚ(√−d) and **every elliptic curve over ℚ with CM by an
order of ℚ(√−d) (f ∤ conductor, f ≥ 5) is supersingular at f, with #E(F_f) = f + 1 and 4cd | #E(F_f)** (PROVED,
standard: inert ⇒ a_f = 0). Over F_q[T] the same holds for rank-2 Drinfeld modules with CM by an imaginary
quadratic F(√D) at inert f (characteristic polynomial X² + u·f, u ∈ F_q^*, Euler characteristic ∝ f + u). So
"divisors of f + 1" are the orders of F_f-rational torsion subgroups of a supersingular reduction, and "4cd | f + 1"
is a Frobenius condition in ℚ(E[4cd]) — but it is equivalent to the cyclotomic condition f ≡ −1 (4cd) at these f,
with the SAME moving level 4cd. The obstruction of §2 is the moving level / small box, not abelianness: a non-abelian
torsion field of growing level is as useless as a cyclotomic one of growing level. (H-D hatch: no gain here.)

(F3) *Thue/Minkowski with an auxiliary prime (Ankeny-type template).* For a fixed prime h, Type II through h ⟺ the
lattice Λ_h = {(c, j) ∈ ℤ² : c + pj ≡ 0 (h)} (covolume h) has a point with cj | (h + 1)/4 (FIXED_MODULUS_SHOTS
Lemma 1.1). Thue's lemma gives (c, j) ∈ Λ_h with 0 < |c|, |j| < √h — exactly the right size (cj < h) — but the
remaining condition is exact divisibility cj | (h + 1)/4; Λ_h has ≍ log h points under the hyperbola cj ≤ h/4 and
τ₃((h+1)/4) admissible pairs, so a hit has "probability" h^{−1+o(1)} per h (the lottery, B3). Choosing h with very
smooth (h + 1)/4 keeps τ₃ ≤ h^{O(1/log log h)}. The deterministic step (Minkowski) produces size, not divisibility.

(F4) *Group-ify the box: let the mute places be the primes of the solution itself.* Box(k) ⊂ ⟨primes of k⟩ with
the exponent cap |e_ℓ| ≤ v_ℓ(k) (FIXED_MODULUS_SHOTS Cor 3.2). Dropping the cap but keeping the *moving* generators
gives the self-referential variant ES^{(y)} of §4: the mute places are the primes of y (part of the solution, as in
B2), and yet it is a theorem. **Outcome: B2's "the modulus is part of the solution" is not by itself the
obstruction; the exponent cap is.** (§4, PROVED relative to UNIT_ORBIT Thm 2.4's sieve.)

(F5) *Exponent intervals.* Keep one fixed mute place s and cap the s-exponent overflow at e (ES^{(s,e)}, §5).
Firing set at f: the ES box times {s^{2i} : i ≤ σ + e}. By Prop 2.2 the Weil threshold needs an interval of length
≳ d·n·q^{d/2}, i.e. e ≈ n² at the optimal d ≈ 2 log_q n — consistent with FF_MUTE Thm 3.5 Remark 3 (shot height
O(q^d + n)). Numerically a much smaller e suffices (§5): provability threshold ≫ truth threshold.

## 4. The self-mute variant ES^{(y)}: moving mute places are harmless, the exponent cap is the obstruction

**Definition 4.1.** For odd n > 1, ES^{(y)}(n): 4/n = 1/x + 1/y + 1/z with x, y ∈ ℤ_{>0}, z ∈ ℚ_{>0}, and every prime ℓ
with v_ℓ(z) < 0 satisfies **ℓ | y**, ℓ ∤ 2n, and v_ℓ(z) even. (ES ⇒ ES^{(y)}; the allowed denominators depend on the
solution, exactly as the certificate modulus does in B2.)

**Theorem 4.2 (ES^{(y)} for every n; PROVED relative to UNIT_ORBIT Lemma 2.2 (linear sieve + Bombieri–Vinogradov);
ineffective).** (a) For every odd non-square n > 1, ES^{(y)}(n) has a solution of Type II shape at every prime of n.
(b) For n = m², no ES^{(y)} solution has Type I/II shape at every prime of m. (c) ES^{(y)}(n) holds for every odd n > 1.
*Proof.* (a) If n ≡ 3 (4), n + 4 has a prime factor r ≡ 3 (4) and Prop 2.1 of UNIT_ORBIT with Q = 1 gives an ES
solution. Let n ≡ 1 (4); fix four odd primes S = {s₁, …, s₄} ∤ n. Run the proof of UNIT_ORBIT Thm 2.4(a) with
M = 4·rad(n)·s₁s₂s₃s₄ and the class a mod M chosen there, additionally a ≡ −1 (mod s_i) (allowed by Lemma 2.2:
−1 ≢ 1 mod s_i). For r ≡ a (M): r ≡ 3 (4), (n/r) = −1, so −n/4 is a square mod r; and, since (r − 1)/2 is odd and
r ≡ −1 (s_i), (s_i/r) = (r/s_i)(−1)^{(s_i−1)/2} = (−1/s_i)(−1)^{(s_i−1)/2} = 1: each s_i is a square mod r, so
Γ_r := ⟨S mod r⟩ ⊆ (F_r^*)², a group of odd order (r − 1)/2. If Γ_r ≠ (F_r^*)², the index [(F_r^*)² : Γ_r] has an odd
prime factor dividing (r−1)/2, hence ≥ x^{1/4−ε} for the sieved r, so |Γ_r| ≤ x^{3/4+ε}, and Lemma 2.3 (k = 4) leaves
o(x/log²x) such r. So some sieved r has Γ_r = (F_r^*)² and, squaring being bijective on this odd-order group,
{Q² : Q ∈ ⟨S⟩} ∋ −n/4 mod r: r | n + 4Q². UNIT_ORBIT Prop 2.1 gives x, y = n(r + 1)/4, z with v_ℓ(z) ≥ 0 for ℓ ∉ S and
v_{s_i}(z) even when negative; and s_i | (r + 1)/4 | y. (b) An ES^{(y)} solution is an ES^{(S′)} solution with S′ the
(odd, prime to n) primes where v(z) < 0; UNIT_ORBIT Cor 1.2. (c) Scaling as in UNIT_ORBIT Cor 2.5:
4/(kd) = 1/(kx) + 1/(ky) + 1/(kz) keeps ℓ | ky, and S was chosen prime to n. ∎

**Corollary 4.3 (what separates ES from ES^{(y)}; PROVED, from UNIT_ORBIT Prop 2.1/6.1).** In the shot family of
Prop 2.1 (r | n + 4Q², Q ∈ ⟨S⟩) the solution satisfies ES^{(y)} iff **rad(Q) | (r + 1)/4** and is an ES solution iff
**Q | (r + 1)/4**. In Frobenius terms: rad(Q) | (r + 1)/4 is a Dirichlet condition of FIXED modulus 4·∏S
(independent of the exponents of Q), and with it the firing condition "−n/4 ∈ ⟨S⟩² mod r" is a Kummer–Chebotarev
condition; Q | (r + 1)/4 is a Dirichlet condition of modulus 4Q, which moves with the exponents. **The exponent cap
v_s(Q) ≤ v_s((r + 1)/4) is exactly the B2 obstruction; the solution-dependence of the allowed primes is not.**
*Proof.* v_s(z) = 2σ − 2c for σ := v_s(r + 1) < 2c (c = v_s(Q)) and ≥ 0 otherwise (UNIT_ORBIT Prop 2.1). So
z ∈ ℤ_{(s)} iff σ ≥ c; and v_s(z) < 0 is allowed in ES^{(y)} iff s | y = n(r + 1)/4, i.e. iff s | (r + 1)/4. ∎

**Theorem 4.4 (|S| = 1 suffices under GRH, for ES^{(s)} and for ES^{(y)}; CONDITIONAL on GRH for the Kummer fields
ℚ(ζ_m, s^{1/m}); task (4), O195 spark 1).** Let s be an odd prime and n ≡ 1 (4) a non-square with s ∤ n. Let D be the
set of residues a mod M = 4·rad(n)·s used above (for ES^{(y)}: a ≡ −1 mod 4s; for ES^{(s)}: no condition mod s,
but a ≢ 0, 1 mod s), and ask for primes r ≡ a (M) such that s is not an ℓ-th power residue mod r for every odd prime
ℓ | r − 1. Under GRH the set of such r has density
`δ = (|D|/φ(M))·∏_{ℓ odd, ℓ ∤ M}(1 − 1/(ℓ(ℓ − 1))) > 0;`
for every such r, ⟨s⟩ ⊇ (F_r^*)² (r ≡ 3 (4)), so as in Thm 4.2 r | n + 4·s^{2j} for some j, giving ES^{(s)}(n), resp.
(with r ≡ −1 mod s) ES^{(y)}(n), with Type II shape.
*Proof sketch.* Hooley's GRH argument in Lenstra's form (H. W. Lenstra, *Invent. Math.* 42 (1977) 201–224: density of
primes with prescribed Frobenius in a finite Galois field and prescribed Kummer behaviour of a fixed element) gives
δ = Σ_{m odd squarefree} μ(m)·c_m/[ℚ(ζ_M, ζ_m, s^{1/m}) : ℚ], where c_m counts σ restricting to a ∈ D on ℚ(ζ_M) and
to the identity on ℚ(ζ_m, s^{1/m}). For odd m the maximal abelian subfield of ℚ(ζ_m, s^{1/m}) is ℚ(ζ_m) (s prime,
ℓ odd: Gal = ℤ/ℓ ⋊ (ℤ/ℓ)^*), so ℚ(ζ_M) ∩ ℚ(ζ_m, s^{1/m}) = ℚ(ζ_{gcd(m,M)}); c_m = 0 unless a ≡ 1 mod gcd(m, M), which
fails for every odd ℓ | M by the choice of D (a ≢ 1 mod ℓ for ℓ | n, and a ≡ −1 or a ≢ 1 mod s). Hence only m coprime
to M contribute, the fields are linearly disjoint, [ℚ(ζ_m, s^{1/m}):ℚ] = mφ(m), and the sum factors as stated. ∎
(Only odd ℓ are imposed, so the even-m entanglement ℚ(√s) ⊂ ℚ(ζ_{4s}) never enters. Status: the Lenstra/Hooley
input is standard but I did not re-derive its error terms; CONDITIONAL on GRH, citation-level.)
