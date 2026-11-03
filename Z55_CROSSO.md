# Z55_CROSSO — Problem CROSS, tryhard lane O: R_𝔉(p) ≥ 1 for all large p?

Status: z55 tryhard lane CROSSO. Internal; hostile-reviewed by a subagent (§7). **ES is OPEN. The target (R_𝔉(p) ≥ 1
for every large prime p ≡ 1 (4)) is NOT proved here.** What is proved is an averaged-over-p version: a positive
proportion statement (Theorem P, unconditional) and an almost-all statement conditional on an explicit, purely
arithmetic (prime-free) variance bound (Theorem A | HV), with the reduction steps proved. Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / Assessment. Scripts `scripts/z55_crosso_*`, data `data/z55/crosso/`.
Definitions as in `Z53_GENUSX.md` §1 and Lemma 4.1 (Theorem U family 𝔉 = 𝔉(p), windows U_i = p^{α_i}, Y = p^β, X = p^γ).

## 0. Summary

* **Reformulation (PROVED, §1).** (u, w) ∈ 𝔉 is a hit (8uw | p + u + 2w) iff 4Cp + 1 = (4uC − 1)(8wC − 1) with
  C = (p + u + 2w)/(8uw); every hit has Jacobi symbols (d/p) = (e/p) = −1 for both factors d = 4uC − 1, e = 8wC − 1
  (this is exactly the square obstruction: at n = m² the same computation gives a contradiction, so R(m²) = 0).
  CERTIFIED on 60 primes near 10⁶ (engine = brute force; all 29 hits have (d/p) = (e/p) = −1) and 200 odd squares (R = 0).
* **Pointwise attack (§2, Assessment).** Each of the three fibrations (fix u / fix w / fix C) turns R(p) into "a single
  integer (p + u, p + 2w or 4Cp + 1) has a divisor in a residue class whose modulus is tied to the fibre variable". I found
  no pointwise handle on that; identity-type constructions (e.g. via p = a² + b²) are excluded by the T1 obstruction.
  Everything below averages over p.
* **Theorem P (PROVED, unconditional; §3).** For any exponents 0 < α₀ < α₁ < β < γ with θ := α₁ + γ < 1/2 — in particular
  for Theorem-U-admissible windows such as (α₀, α₁, β, γ) = (0.075, 0.1, 0.29, 0.39) — a positive proportion of the primes
  p ≡ 1 (4) in every dyadic interval (x/2, x], x ≥ x₀, have **R_𝔉(p) ≥ 2** (R is even). Explicit proportion
  ≥ 2μ(1 − 2θ)/(2(1 − 2θ) + 32μ) − o(1), μ = ¼·log(α₁/α₀)·log(γ/β) (≈ 0.0012 for the example window).
  Inputs: Bombieri–Vinogradov, Brun–Titchmarsh, Mertens; the subfamily with u, w prime.
* **Theorem A (CONDITIONAL on HV; §4).** For the same windows, with M̃(p) the explicit mod-8 density of the family
  (M̃(p) ≥ c₀ log²p, PROVED, Lemma 4.2), PROVED (Lemma 4.1, dual large sieve):
  Σ_{x/2<p≤x} |R_x(p) − M̃(p)|² ≤ x·V₈(x), where V₈(x) is an explicit prime-free pair sum (the Haar variance of the
  family). **If V₈(x) = o(log³x) (hypothesis HV)**, then R_𝔉(p) ≥ (1 − ε)M̃(p) ≫ log²p for all but o(π(x)) primes p ≤ x.
  EVIDENCE for HV: Var(R − M̃) ≈ 2·M̃ (Poisson value for the even count R) over random primes, at four window scales (§4.4).
* **Verdict: target not reached (ES remains OPEN).** Banked: Theorem P (unconditional, positive proportion);
  Theorem A as a clean reduction of "almost all p" to a prime-free combinatorial variance bound.

## 1. Reformulations and the square obstruction (PROVED; CERTIFIED checks)

Notation: p prime, p ≡ 1 (4); (u, w) ∈ 𝔉 means u ≡ 1 (4) squarefree in (U₀, U₁], w odd squarefree in (Y, X],
gcd(w, up) = 1; q = 8uw, a = −(u + 2w); R_𝔉(p) = 2#{(u, w) ∈ 𝔉 : p ≡ a (mod q)} (`Z53_GENUSX` §1).

**Lemma 1.1.** For (u, w) ∈ 𝔉 the following are equivalent: (i) p ≡ a (mod 8uw); (ii) w | p + u and
w″ := (p + u)/(2w) ≡ −1 (mod 4u); (iii) C := (p + u + 2w)/(8uw) is a positive integer, and then
  4Cp + 1 = (4uC − 1)(8wC − 1),  4uC − 1 = w″,  p + u = 2w(4uC − 1).
For a hit, put d = 4uC − 1, e = 8wC − 1. Then the Jacobi symbols satisfy (d/p) = (e/p) = −1.
*Proof.* (i)⇔(iii) is the definition of C (C > 0 since p + u + 2w > 0). Expanding,
(4uC − 1)(8wC − 1) = 32uwC² − 4C(u + 2w) + 1 = 4C(8uwC − u − 2w) + 1 = 4Cp + 1, and
2w(4uC − 1) = 8uwC − 2w = p + u. (ii)⇔(iii): if w | p + u, w″ is an odd integer (p + u ≡ 2 (4), w odd), and
w″ ≡ −1 (4u) ⇔ w″ = 4uC − 1 for an integer C ≥ 1 ⇔ p + u = 2w(4uC − 1) ⇔ (iii).
Symbols: d | 4Cp + 1, so 4Cp ≡ −1 (d), i.e. −Cp ≡ (2⁻¹)² is a square mod d and (−Cp/d) = 1. Write C = 2^k c, c odd.
d ≡ 3 (4) gives (−1/d) = −1; if k ≥ 1 then 8 | 4C and d ≡ −1 (8), so (2/d) = 1; and by reciprocity
(c/d) = (d/c)(−1)^{((c−1)/2)((d−1)/2)} = (−1/c)(−1)^{(c−1)/2} = 1 (d ≡ −1 mod c, (d − 1)/2 odd). So (−C/d) = −1, hence
(p/d) = −1, and (d/p) = (p/d) = −1 by Jacobi reciprocity (p ≡ 1 (4), d odd, gcd(d, p) = 1). e ≡ −1 (mod 4C) and
e ≡ −1 (8), so the same computation applies to e. ∎

**Corollary 1.2 (T1; PROVED).** For odd n = m², R(n) = 0 for every window: a hit would give (−Cm²/d) = 1, and
gcd(m, d) = 1 (a prime ℓ | m, d would divide 4Cm² + 1 − 4Cm² = 1), so (−C/d) = 1, contradicting (−C/d) = −1. Thus any
argument proving R_𝔉(p) ≥ 1 pointwise must use that p is not a square; in Lemma 1.1 the place is (p/d) = −1 being
*possible*. (Classical; recorded because §3–§4 must be checked against it, see §5.)

**Checks (CERTIFIED / EVIDENCE).** `scripts/z55_crosso_R.c` computes R_𝔉 via `Z53_GENUSX` Lemma 4.1 (loop over w);
`scripts/z55_crosso_checks.py` (output `data/z55/crosso/checks.txt`), standard window (p^{1/12}, p^{1/3}/2, p^{1/3}, p^{2/3}/4):
(1) engine = brute force over (u, w) on the 60 primes p ≡ 1 (4) above 10⁶: 0 mismatches; also p = 100000049: R = 2 both
ways (matches `Z53_GENUSX` §5); (2) all 29 hits satisfy 4Cp + 1 = de, p + u = 2wd, (d/p) = (e/p) = −1;
(3) 200 odd squares m² (m ∈ [1001, 1399]) give R = 0 in the standard window and in a wide window; (4) 48 of 200 composite
non-squares near 10⁶ have R > 0.

## 2. The pointwise attack (Assessment)

The three exact fibrations of the hit set {(u, w, C) : p = 8uwC − u − 2w} are:
* fix u: hits ↔ divisors w″ ≡ −1 (mod 4u) of (p + u)/2 in a range (R ≈ Σ_u #{divisors of p + u in a class mod 4u});
* fix w: hits ↔ divisors 8Cw − 1 of p + 2w, the cofactor being u ∈ 𝒰 (`Z53_GENUSX` Lemma 4.1: one u per w);
* fix C: hits ↔ divisors d ≡ −1 (mod 4C) of 4Cp + 1 (the cofactor is then automatically ≡ −1 mod 4C).
In every fibration the modulus of the class is tied to the fibre variable, and the integer whose divisors are counted
depends on it, so no averaging over the fibre variable produces an equidistribution statement (what Theorem U and
`Z53_GENUSX` Theorem X do is average the *density* ρ_u(w), not the divisibility). I tried: (a) short-interval divisor
asymptotics (the u-range p^{α₁} is far below the p^{0.31} needed even for plain τ(p + u), and the class condition is
not a divisor-function twist); (b) parametrising p = a² + b² and looking for an identity 4C(a² + b²) + 1 = (4CA − 1)(4CB − 1)
with polynomial A, B, C: at b = 0 it would represent odd squares, contradicting Cor 1.2 unless positivity fails there,
and a² + b² + (lower order) is irreducible in a, so no such identity with C independent of a exists; (c) the least
quadratic non-residue: Lemma 1.1 says every hit lives on non-residues d, but producing a non-residue (Burgess) does not
produce the divisibility d | 4Cp + 1. None gave a pointwise statement; I therefore turned to averages over p, where the
remainders R − M can be controlled, which is the brief's "natural line" with p as the averaging variable.

## 3. Theorem P: a positive proportion of primes (PROVED)

**Setting.** Fix exponents 0 < α₀ < α₁ < β < γ with θ := α₁ + γ < 1/2. For x large put
  𝒰_x := {u prime : u ≡ 1 (4), x^{α₀} < u ≤ (x/2)^{α₁}},  𝒲_x := {w prime : x^β < w ≤ (x/2)^γ},  𝒫_x := 𝒰_x × 𝒲_x.
**Inclusion.** For every prime p ∈ (x/2, x], 𝒫_x ⊂ 𝔉(p): u is squarefree, u ≡ 1 (4), p^{α₀} ≤ x^{α₀} < u ≤ (x/2)^{α₁} < p^{α₁};
w is odd squarefree, p^β ≤ x^β < w ≤ (x/2)^γ < p^γ; gcd(w, u) = 1 since w > x^β > x^{α₁} ≥ u (β > α₁) and both are prime;
gcd(w, p) = 1 since w < x/2 < p. (Also (C1) γ < 1 − α₁ holds as θ < 1/2.) Hence
  R_𝔉(p) ≥ R_x(p) := 2#{(u, w) ∈ 𝒫_x : p ≡ a_{uw} (mod q_{uw})},  q_{uw} = 8uw, a_{uw} = −(u + 2w).
For (u, w) ∈ 𝒫_x, gcd(a, q) = 1 (a is odd; u | a would force u | 2w; w | a would force w | u) and
φ(q) = 4(u − 1)(w − 1). Moreover a ≡ −(1 + 2) ≡ 1 (mod 4), so R_x(p) = 0 for p ≡ 3 (4).

**Theorem P.** Put μ := ¼·log(α₁/α₀)·log(γ/β). As x → ∞,
  #{p ∈ (x/2, x] prime : R_𝔉(p) ≥ 2} ≥ (μ/(2 + 32μ/(1 − 2θ)) − o(1))·(π(x) − π(x/2)).
Since the primes ≡ 1 (4) in (x/2, x] number (½ + o(1))(π(x) − π(x/2)), a proportion ≥ 2μ(1 − 2θ)/(2(1 − 2θ) + 32μ) − o(1)
of them has R_𝔉(p) ≥ 2; summing over dyadic intervals, the set has positive lower relative density among primes ≡ 1 (4).

*Example (Theorem U admissible).* (α₀, α₁, β, γ) = (0.075, 0.1, 0.29, 0.39): θ = 0.49; Theorem U's (C1) γ < 1 − α₁,
(C2) β > τ_r(1 + α₁) + 4ε = 0.2800 and (C3) α₀ > τ_r²(1 + α₁) + 3ε = 0.0713 hold with r = 100, ε = 2·10⁻⁵
(τ_r = (r+1)/(4r) + rε = 0.2545, as in `Z53_GENUSLVAL` §2.1); μ ≈ 0.02131, proportion ≥ 0.00118. (Non-admissible windows with small α₀ give larger constants; the theorem needs only
θ < 1/2 and β > α₁.)

*Proof.* Write Π := π(x) − π(x/2) and N(u, w, u′, w′) := #{p ∈ (x/2, x] : p ≡ a (q), p ≡ a′ (q′)} (primed quantities refer
to (u′, w′)). Sums over p are over all primes in (x/2, x].

(1) *First moment.* E₁ := Σ_p R_x(p) = 2Σ_{𝒫_x}(π(x; q, a) − π(x/2; q, a)). The map (u, w) ↦ q = 8uw is injective on 𝒫_x
(unique factorisation, u < w), and q ≤ 8x^{θ} ≤ x^{1/2}(log x)^{−B} for x ≥ x₀(B). Bombieri–Vinogradov
(Σ_{q ≤ x^{1/2}(log x)^{−B}} max_{(a,q)=1} max_{y≤x} |π(y; q, a) − li(y)/φ(q)| ≪_A x(log x)^{−A}, B = B(A)) gives
  E₁ = 2(li(x) − li(x/2))·Σ_{𝒫_x} 1/φ(q) + O(x(log x)^{−3}).
Σ_{𝒫_x} 1/φ(q) = ¼·(Σ_{u∈𝒰_x} 1/(u − 1))·(Σ_{w∈𝒲_x} 1/(w − 1)). By Mertens' theorem for primes ≡ 1 (4)
(Σ_{ℓ≤t, ℓ≡1(4)} 1/ℓ = ½ log log t + c + O(1/log t)) and Σ_{ℓ>T} (1/(ℓ − 1) − 1/ℓ) ≤ 2/T,
Σ_{𝒰_x} 1/(u − 1) = ½log(α₁/α₀) + o(1) =: S_u + o(1), and likewise Σ_{𝒲_x} 1/(w − 1) = log(γ/β) + o(1) =: S_w + o(1).
With li(x) − li(x/2) = (1 + o(1))Π (PNT): **E₁ = (μ + o(1))Π**, μ = S_uS_w/2.

(2) *Second moment.* E₂ := Σ_p R_x(p)² = 4Σ_{(u,w),(u′,w′) ∈ 𝒫_x} N(u, w, u′, w′). Four cases.
– (u′, w′) = (u, w): contributes 4Σ_{𝒫_x}(π(x; q, a) − π(x/2; q, a)) = 2E₁.
– w′ = w, u′ ≠ u: a solution p needs u ≡ u′ (mod w) (reduce a ≡ a′ mod w), impossible as 0 < |u − u′| < (x/2)^{α₁} < w. N = 0.
– u′ = u, w′ ≠ w: a solution needs a ≡ a′ (mod 8u), i.e. 2w ≡ 2w′ (mod u) and w ≡ w′ (mod 4), i.e. w′ ≡ w (mod 4u); and
then N ≤ #{n ≤ x : n ≡ b (mod 8uww′)} ≤ x/(8uww′) + 1. For fixed u, w, the w′ ∈ (x^β, x^γ] with w′ ≡ w (4u) form a
progression t₀ + 4uj (j = 0, 1, …, t₀ > x^β, 4uj ≤ x^γ), so Σ 1/w′ ≤ 1/t₀ + Σ_{1≤j≤x^γ/(4u)} 1/(4uj) ≤ x^{−β} + (1 + γ log x)/(4u);
and the number of triples (u, w, w′) is ≤ Σ_u x^γ(x^γ/(4u) + 1). So this case contributes at most
  4Σ_u Σ_w Σ_{w′} (x/(8uww′) + 1) ≤ (x/2)Σ_u (1/u)(x^{−β} + (1 + γ log x)/(4u))·Σ_w 1/w + 4Σ_u x^γ(x^γ/(4u) + 1)
  ≪ x(log x)·x^{−α₀} + x^{2γ}log x + x^{α₁+γ} = o(x/log x),
using Σ_u 1/u² ≤ x^{−α₀}, Σ_w 1/w ≪ 1, and 2γ < 2θ < 1.
– u′ ≠ u and w′ ≠ w: then {u, w} ∩ {u′, w′} = ∅ (u′ ≠ w since u′ < x^{α₁} < x^β < w, and similarly u ≠ w′), so
gcd(uw, u′w′) = 1 and a solution exists only if a ≡ a′ (mod 8), in which case the two congruences are equivalent to one
class b mod L := 8uwu′w′, L ≤ 64x^{2θ}. Brun–Titchmarsh in the Montgomery–Vaughan form π(y; L, b) ≤ 2y/(φ(L)log(y/L))
(1 ≤ L < y) gives, with log(x/L) ≥ ((1 − 2θ)/2)log x for x ≥ x₀, N ≤ 4x/((1 − 2θ)φ(L)log x) and φ(L) =
4(u − 1)(w − 1)(u′ − 1)(w′ − 1). So this case contributes at most
  4·Σ 4x/(4(1 − 2θ)log x·(u − 1)(w − 1)(u′ − 1)(w′ − 1)) = (4x/((1 − 2θ)log x))·(S_uS_w + o(1))².
Since x/log x = (2 + o(1))Π and S_uS_w = 2μ: **E₂ ≤ (2μ + 32μ²/(1 − 2θ) + o(1))Π.**

(3) *Cauchy–Schwarz.* E₁² = (Σ_p R_x(p)·1[R_x(p) ≥ 1])² ≤ #{p : R_x(p) ≥ 1}·E₂, so
#{p ∈ (x/2, x] : R_x(p) ≥ 1} ≥ E₁²/E₂ ≥ (μ²/(2μ + 32μ²/(1 − 2θ)) − o(1))Π. R_x is even, and R_𝔉 ≥ R_x. ∎

*Remarks.* (1) The u′ = u case is where p ≡ 1 (4) and the window ordering matter; the "w′ = w" case is
`Z53_GENUSX` Lemma 4.1's injectivity. (2) Only R ≥ 1 is obtained: the subfamily has bounded mean μ. For R ≥ c log²p on a
positive proportion one would use the full squarefree family, where the same scheme needs the upper bound
Σ_{compatible pairs} 1/φ(lcm(q, q′)) ≪ log⁴x (Assessment: true, by a six-variable congruence count; not written out).
(3) Primality of p enters through BV and BT; see §5 for T1.

## 4. Almost all primes, conditionally on a prime-free variance bound (reduction PROVED; HV CONDITIONAL/EVIDENCE)

**Setting.** Same exponents (0 < α₀ < α₁ < β < γ, θ = α₁ + γ < 1/2). Fixed-window squarefree family
  𝔉_x := {(u, w) : u ≡ 1 (4) squarefree in (x^{α₀}, (x/2)^{α₁}], w odd squarefree in (x^β, (x/2)^γ], gcd(u, w) = 1}.
As in §3, 𝔉_x ⊂ 𝔉(p) for every prime p ∈ (x/2, x] (gcd(w, p) = 1 as w < p), so R_𝔉(p) ≥ R_x(p) := 2#{(u, w) ∈ 𝔉_x : p ≡ a (q)}.
For (u, w) ∈ 𝔉_x: gcd(a, q) = 1 (a odd; gcd(u + 2w, u) = gcd(2w, u) = 1; gcd(u + 2w, w) = gcd(u, w) = 1) and
φ(q) = 4φ(u)φ(w). Define the mod-8 density
  M̃_x(p) := Σ_{(u,w)∈𝔉_x} (2/(φ(u)φ(w)))·1[p ≡ a (mod 8)]   (depends on p only through p mod 8),
and Q := 8(x/2)^{α₁}(x/2)^γ ≥ max q, so Q² ≤ x/2 for x ≥ x₀ (2θ < 1).

**Lemma 4.1 (dual large sieve reduction; PROVED).** For x ≥ x₀,
  Σ_{x/2<p≤x} |R_x(p) − M̃_x(p)|² ≤ x·V₈(x),   V₈(x) := Σ_{pairs} 1[a ≡ a′ (8)]·(φ(h)·1[a ≡ a′ (h)] − 1)/(φ(uw)φ(u′w′)),
the sum over ordered pairs ((u, w), (u′, w′)) ∈ 𝔉_x², h := gcd(uw, u′w′). Pairs with h = 1 contribute 0, and V₈ ≥ 0.
*Proof.* For p > Q prime, 1[p ≡ a (q)] = φ(q)⁻¹Σ_{χ mod q} χ̄(a)χ(p). Each χ mod q is induced by a unique primitive χ*
of conductor f | q, χ(n) = χ*(n)1[(n, q) = 1]; so χ(p) = χ*(p), χ̄(a) = χ̄*(a) ((a, q) = 1), and the order is preserved.
Hence R_x(p) = Σ_{χ*} c(χ*)χ*(p) with c(χ*) := 2Σ_{(u,w)∈𝔉_x, f(χ*) | q} χ̄*(a)/φ(q), the sum over primitive χ* of conductor
≤ Q. The χ* with f | 8 are exactly the four characters mod 8 and 8 | q always, so their part is
Σ_{(u,w)} (2/φ(q))Σ_{χ mod 8} χ̄(a)χ(p) = Σ (8/φ(q))1[p ≡ a (8)] = M̃_x(p). Thus R_x(p) − M̃_x(p) = Σ_{f(χ*)∤8} c(χ*)χ*(p).
The dual form of the multiplicative large sieve (Iwaniec–Kowalski Thm 7.13 plus the duality principle, IK §7.1):
for any interval I of N integers and complex b(χ*) indexed by primitive characters of conductor ≤ Q,
Σ_{n∈I} |Σ_{χ*} b(χ*)χ*(n)|² ≤ (N + Q²)Σ_{χ*} |b(χ*)|². (Duality: the operator a ↦ (√(f/φ(f))Σ_n a_nχ*(n))_{χ*} has norm²
≤ N + Q² by the large sieve inequality Σ_{f≤Q}(f/φ(f))Σ*_{χ mod f}|Σ_{n∈I}a_nχ(n)|² ≤ (N + Q²)Σ|a_n|²; its adjoint has the
same norm, and f/φ(f) ≥ 1.) Drop the non-primes in I = (x/2, x]: the left side of the lemma is ≤ (x/2 + Q²)Σ_{f∤8}|c(χ*)|²
≤ x·Σ_{f∤8}|c(χ*)|². Expanding,
Σ_{f∤8}|c|² = 4Σ_{pairs}(φ(q)φ(q′))⁻¹·Σ_{χ*: f | g, f∤8} χ̄*(a)χ*(a′),  g := gcd(q, q′) = 8h.
Characters mod g ↔ primitive characters of conductor dividing g, so Σ_{f|g} χ*(a′ā) = Σ_{χ mod g} χ(a′ā) = φ(g)1[a ≡ a′ (g)],
and the f | 8 part is Σ_{χ mod 8} χ(a′ā) = 4·1[a ≡ a′ (8)]. With φ(g) = 4φ(h), φ(q) = 4φ(uw), and
"a ≡ a′ (8h)" ⟺ "a ≡ a′ (8) and (h)", we get Σ_{f∤8}|c|² = V₈(x). It is ≥ 0 as a sum of squares; for h = 1 the bracket
is φ(1)·1 − 1 = 0. ∎
(Precise reference for the large sieve: Montgomery–Vaughan's form Σ_{q≤Q}(q/φ(q))Σ*_{χ}|Σ_{M<n≤M+N}a_nχ(n)|² ≤ (N − 1 + Q²)Σ|a_n|²,
Iwaniec–Kowalski Theorem 7.13.)

**Lemma 4.2 (the density main term; PROVED).** There is c₀ = c₀(α₀, α₁, β, γ) > 0 with M̃_x(p) ≥ c₀ log²x for every
p ≡ 1 (4) and x ≥ x₀. (Explicitly c₀ ≈ 0.002·(α₁ − α₀)(γ − β) works.)
*Proof.* Let e₂ := 3 if p ≡ 1 (8) and e₂ := 1 if p ≡ 5 (8). If u ≡ 1 (8) and w ≡ e₂ (4) then u + 2w ≡ 1 + 2e₂ ≡ −p (8),
i.e. p ≡ a (8). Let K := 15015 = 3·5·7·11·13 and
  A″ := {u ≡ 1 (8) squarefree, gcd(u, K) = 1, U₀ < u ≤ U₁},  A′ := {u ∈ A″ : Σ_{ℓ|u} 1/ℓ ≤ 3/10},
  B := {w ≡ e₂ (4) squarefree, Y < w ≤ X}  (U₀ = x^{α₀}, U₁ = (x/2)^{α₁}, Y = x^β, X = (x/2)^γ).
Then M̃_x(p) ≥ 2Σ_{u∈A′}(1/u)Σ_{w∈B, (w,u)=1} 1/w (as φ(n) ≤ n).
*Squarefree counts.* For a fixed modulus k and a unit class e mod k, #{n ≤ t : n squarefree, n ≡ e (k)} =
(6/π²)k⁻¹∏_{ℓ|k}(1 − ℓ⁻²)⁻¹·t + O_k(√t) (write 1_{sqfree}(n) = Σ_{d²|n}μ(d); for d coprime to k the class condition and
d² | n define one class mod kd², counted as t/(kd²) + O(1); d sharing a prime with k contributes nothing; sum over
d ≤ √t). Partial summation gives Σ_{n∈(T₀,T₁], sqfree, n≡e (k)} 1/n = c·log(T₁/T₀) + O_k(T₀^{−1/2}) with that density c.
For w (k = 4): c = (6/π²)(1/4)(4/3) = 2/π², so Σ_B 1/w = (2/π²)log(X/Y) + O(1). For A″ (the condition gcd(u, K) = 1
and u ≡ 1 (8) is a union of φ(K) unit classes mod 8K): density κ = (1/π²)∏_{ℓ|K} ℓ/(ℓ + 1) = (1/π²)(3/4)(5/6)(7/8)(11/12)(13/14)
≈ 0.04716, so Σ_{A″} 1/u = κ log(U₁/U₀) + O(1).
*Inner sum.* For u ∈ A′ and an odd prime ℓ | u (ℓ ≤ U₁ < Y): Σ_{w∈B, ℓ|w} 1/w ≤ ℓ⁻¹Σ_{odd w′ ∈ (Y/ℓ, X/ℓ]} 1/w′ ≤
ℓ⁻¹(½log(X/Y) + 1). Hence Σ_{w∈B,(w,u)=1} 1/w ≥ (2/π²)log(X/Y) − (3/10)(½log(X/Y) + 1) − O(1) ≥ 0.0526·log(X/Y) − O(1)
(2/π² − 3/20 = 0.0526).
*Outer sum.* Σ_{u∈A″∖A′} 1/u ≤ (10/3)Σ_{u∈A″}(1/u)Σ_{ℓ|u}1/ℓ ≤ (10/3)Σ_{ℓ≥17}ℓ⁻²·(½log(U₁/U₀) + 1)
(primes ℓ | u ∈ A″ are ≥ 17; Σ_{u∈A″, ℓ|u} 1/u ≤ ℓ⁻¹Σ_{odd u′ ≤ U₁/ℓ, u′ > U₀/ℓ} 1/u′ ≤ ℓ⁻¹(½log(U₁/U₀) + 1)).
Σ_{ℓ≥17} ℓ⁻² = 0.452247 − (1/4 + 1/9 + 1/25 + 1/49 + 1/121 + 1/169) = 0.016547, so this is ≤ 0.02758·log(U₁/U₀) + O(1), and
Σ_{A′} 1/u ≥ (0.04716 − 0.02758)log(U₁/U₀) − O(1) = 0.01958·log(U₁/U₀) − O(1).
Multiplying: M̃_x(p) ≥ 2·0.01958·0.0526·log(U₁/U₀)log(X/Y) − O(log x) ≥ 0.002(α₁ − α₀)(γ − β)log²x for x ≥ x₀. ∎

**Hypothesis HV.** V₈(x) = o(log³x) as x → ∞ (for the fixed exponents).

**Theorem A (CONDITIONAL on HV).** Under HV, for every ε > 0,
  #{p ∈ (x/2, x] prime, p ≡ 1 (4) : R_𝔉(p) < (1 − ε)M̃_x(p)} = o(π(x) − π(x/2)),
so R_𝔉(p) ≥ (1 − ε)c₀log²p for all but o(π(x)) primes p ≡ 1 (4) up to x; more precisely the exceptional set in (x/2, x]
has size ≤ x·V₈(x)/(ε²c₀²log⁴x).
*Proof.* R_𝔉(p) ≥ R_x(p); by Lemma 4.1, Chebyshev and Lemma 4.2,
#{p : R_x(p) < (1 − ε)M̃_x(p)} ≤ Σ_p |R_x − M̃_x|²/(εc₀log²x)² ≤ xV₈(x)/(ε²c₀²log⁴x) = o(x/log x). ∎

### 4.3 What is known about V₈ (PROVED parts / Assessment)

* *Diagonal* (PROVED): the pairs with (u′, w′) = (u, w) contribute Σ_{𝔉_x}(φ(uw) − 1)/φ(uw)² ≤ Σ 1/φ(uw) ≪ log²x.
* *Probabilistic meaning* (PROVED identity): let N be the lcm of all q and, for c ∈ {1, 5}, let n be uniform on the units
  of ℤ/N with n ≡ c (8); let H(n) := #{(u, w) ∈ 𝔉_x : n ≡ a (q)}. Given n mod 8, n mod uw is uniform on units, so
  P(A_{uw}) = 1[a ≡ c (8)]/φ(uw) and P(A_{uw} ∩ A_{u′w′}) = 1[a ≡ a′ ≡ c (8)]·φ(h)1[a ≡ a′ (h)]/(φ(uw)φ(u′w′)). Hence
  **V₈ = Var_{c=1}(H) + Var_{c=5}(H)** = ¼Σ_c Var_c(R) — the variance of the family's own count under the Haar model,
  with no primes. HV says this variance is o(log x) times the mean (which is ≍ log²x).
* *Off-diagonal* (Assessment, not proved): pairs with h > 1 split as (i) pairs sharing only primes ≤ z := (log x)²:
  there φ(h)1[a ≡ a′ (h)] − 1 has mean zero over the residues of the unshared cofactors (u ≡ 1 (4) squarefree, resp.
  w odd squarefree, in a class mod a z-smooth modulus), which range over intervals long compared to h except for a sparse
  set of large z-smooth h, so this part should be o(log³x); (ii) pairs sharing a prime ℓ > z: the "−1" part has weight
  ≤ Σ_{ℓ>z}(Σ_{ℓ | uw} 1/φ(uw))² ≪ log⁴x·Σ_{ℓ>z}ℓ⁻² ≪ log²x/log log x (PROVED, elementary), while the
  "φ(h)1[·]" part is the Haar probability of two hits sharing a large prime; writing u = g₁₁k₁, u′ = g₁₁v,
  w = g₂₂k₂, w′ = g₂₂t (no cross-sharing) the compatibility is k₁ ≡ v (mod g₂₂), k₂ ≡ t (mod g₁₁), and counting the pairs
  (k₁, v), (k₂, t) jointly gives ≪ [min(1, g₁₁/U₀) + log²x/g₂₂]·[min(1, g₂₂/Y) + log²x/g₁₁]/(g₁₁g₂₂), whose sum over
  g₁₁g₂₂ having a prime > z is ≪ log²x + log⁴x/z. The general case adds the cross-shares gcd(u, w′), gcd(w, u′) (a
  4-cycle of congruences among k₁, v, k₂, t). Writing (i) and the general (ii) out is the missing step; not completed in
  the time box. (A pointwise-in-(u, w) version of the count is too lossy: it must be done jointly.)

### 4.4 EVIDENCE for HV (`scripts/z55_crosso_var.c` → `data/z55/crosso/var_scaling.txt`)

Monte Carlo over n ∈ [10¹⁸, 2·10¹⁸], n ≡ 1 (4): fixed-window squarefree family (u ≡ 1 (4) sqfree in (U₀, U₁], w odd sqfree in
(Y, X], gcd(u, w) = 1), R(n) and M̃(n) exactly per n; seed 7. Command:
`gcc -O2 -o /tmp/z55var scripts/z55_crosso_var.c; /tmp/z55var U0 U1 Y X 1000000000000000000 S 7`.

| (U₀, U₁, Y, X) | samples | mean M̃ | primes: mean R | primes: Var(R − M̃)/M̃ | primes: P(R=0) | integers: Var/M̃ |
|---|---|---|---|---|---|---|
| (5, 100, 200, 5000) | 2000 | 0.731 | 0.751 | 2.08 | 0.687 | 1.31 |
| (5, 300, 400, 40000) | 2000 | 1.538 | 1.590 | 1.99 | 0.445 | 1.41 |
| (8, 1000, 1500, 3·10⁵) | 1000 | 2.415 | 2.514 | 2.00 | 0.276 | 1.45 |
| (8, 3000, 4000, 2·10⁶) | 400 | 3.528 | 3.725 | 2.33 | 0.155 | 1.54 |

R counts each hit twice, so a Poisson number of hits gives Var(R)/E(R) = 2: over primes the variance is at the Poisson
value at every scale (no growth with the mean), consistent with V₈ ≍ (mean) ≍ log²x, far inside HV. (Over integers mean R
is lower because n can share factors with q; irrelevant for primes.) The windows here are not exponent windows and the
sizes are small; this is evidence about the variance structure, not about the asymptotic constant.

## 5. T1 audit and screens

* **T1.** Theorem P and Theorem A are density statements, which are not contradicted by squares (they are 0 % of
  integers), so T1 does not bite them directly; still, the arguments use primality essentially: Theorem P via
  Bombieri–Vinogradov/Brun–Titchmarsh for primes in progressions (the analogous statement "a positive proportion of
  odd squares m² have R(m²) ≥ 1" is false by Cor 1.2, and indeed squares do not equidistribute in the classes a mod q,
  which are non-square classes by Lemma 1.1), Theorem A via the restriction to n = p coprime to every q (needed for
  χ(p) = χ*(p)). Lemma 4.1 itself holds over all integers coprime to all q; the information "R(m²) = 0" is consistent with
  it since the squares in (x/2, x] number O(√x).
* **Pointwise target:** not reached; no claim implies ES for any explicit prime.
* **8/131, tied modulus (B2), fixed p (B6):** Theorems P and A are averages over p (they do not pass B6 in the pointwise
  sense, by design); §2 records the B2 wall at fixed p.

## 6. Verdict

* PROVED: Lemma 1.1/Cor 1.2 (hits ↔ factorisations 4Cp + 1 = de, both factors non-residues mod p; squares have none);
  **Theorem P** (positive proportion of primes p ≡ 1 (4) with R_𝔉(p) ≥ 2, for Theorem-U-admissible windows with α₁ + γ < 1/2);
  Lemma 4.1 (large-sieve reduction of the variance over primes to the prime-free V₈) and Lemma 4.2 (M̃ ≫ log²x).
* CONDITIONAL: **Theorem A** (almost all p have R_𝔉(p) ≥ (1 − ε)M̃(p) ≫ log²p) on HV: V₈(x) = o(log³x).
* EVIDENCE: HV holds with room (Var ≈ Poisson); §4.4.
* NOT PROVED: the target R_𝔉(p) ≥ 1 for every large p. **ES remains OPEN.**

## 7. Review log

(filled after the hostile review)
