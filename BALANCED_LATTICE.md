# BALANCED_LATTICE — from Hypothesis W to GRH? Balanced relation lattices of small primes mod q (task O256)

Status: O256 checkpoint 1 (unreviewed). **ES is not solved here, nor any infinite case of ES.** A bounded or slowly growing
cap is NOT ES: cap 0 is the B2 divisor event (FORCED_WINDOW Prop 2.1, Prop 4.5); everything below is about cap ≥ 1.
Labels as in DISCOVERIES.md. Builds on FORCED_WINDOW (O252: Lemma 1.1, Prop 1.2, Prop 4.1, Def 4.2, Hyp W, Thm 4.3,
Cor 4.4, Prop 5.1, Prop 5.2), CAP_INTERPOLATION Thm 4.2, BRAINSTORM/z12_grh_lattice_gap. Scripts `scripts/z27_*`, memos
`BRAINSTORM/z27_*.md`.

Notation. q prime, q ≡ 3 (mod 4), N := (q − 1)/2 (odd), U_q := (F_q^*)² cyclic of order N. S a set of k odd primes ≠ q,
g_s := s², H := ⟨g_s : s ∈ S⟩ ≤ U_q, Λ = Λ_q(S) := {x ∈ ℤ^S : ∏ g_s^{x_s} = 1} (det Λ = |H|), Λ* := {y ∈ ℝ^S : y·x ∈ ℤ ∀x ∈ Λ}.
For ψ ∈ Ĥ write ψ(g_s) = e(θ_s(ψ)), θ_s ∈ ℝ/ℤ. ‖·‖ = distance to ℤ. μ_∞(Λ) := inf{r : Λ + [−r, r]^S = ℝ^S}.
L_min(q) := least L with W_L := {∏ g_s^{j_s} : 0 ≤ j_s ≤ L} = U_q (FORCED_WINDOW Prop 4.1; ∞ if H ≠ U_q).

## 0. Iteration log

(I1) *Brief's route: certify balance by Frobenius in Kummer fields.* §1 turns balance into a statement about ALL characters of
U_q (ℓ¹-pretentious distance to 1 on S). §2: Frobenius of q in ℚ(ζ_m, S^{1/m}) sees exactly the characters of order dividing
m; under GRH (Lagarias–Odlyzko) one certifies "no ε-pretentious character of order ≤ M" for a positive proportion of q in
the class, but only up to M = x^{O(1/k)}. Barrier: the characters of order ≤ M are a fraction ≤ M²/N of all characters, and
the extremal (balance-deciding) character has order ≍ N in practice (§6). Hypothesis violated by the brief's route:
"imbalance is driven by small-order (index) obstructions".

## 1. Exact dictionary: balance ⟺ no nontrivial character is ℓ¹-pretentious to 1 on S

**Lemma 1.1 (dual lattice = character group; PROVED, standard).** The map ψ ↦ θ(ψ) := (θ_s(ψ))_{s∈S} + ℤ^S is an isomorphism
Ĥ ≅ Λ*/ℤ^S. In particular ℤ^S ⊂ Λ* with index |H|, and a vector y ∈ Λ* ∖ ℤ^S is the same thing as a nontrivial character ψ of H
together with a choice of real lifts θ_s ∈ ℝ of its angles.
*Proof.* x ↦ g^x := ∏ g_s^{x_s} induces ℤ^S/Λ ≅ H. Characters of ℤ^S are x ↦ e(y·x), y ∈ ℝ^S/ℤ^S; such a character factors
through ℤ^S/Λ iff y·x ∈ ℤ for all x ∈ Λ, i.e. y ∈ Λ*. The factored character is ψ with ψ(g_s) = e(y_s). ∎

**Definition 1.2 (ℓ¹-pretentious distance on S).** For ψ ∈ Ĥ put 𝔻_S(ψ) := Σ_{s∈S} ‖θ_s(ψ)‖ (the least ℓ¹-norm in the coset
θ(ψ) + ℤ^S), and 𝔻_min(q) := min_{ψ ≠ 1} 𝔻_S(ψ). (Compare Granville–Soundararajan's 𝔻(χ, 1; y)² = Σ_{s≤y}(1 − Re χ(s))/s:
here the weights are flat, the angle enters linearly, and only the k primes of S count.)

**Proposition 1.3 (transference; PROVED, Banaszczyk + elementary).** With λ₁^{(1)}(Λ*) = min(1, 𝔻_min(q)):
`  1/(2 min(1, 𝔻_min))  ≤  μ_∞(Λ)  ≤  k^{3/2}/(2 min(1, 𝔻_min)).`
Consequently (FORCED_WINDOW Prop 4.1): if H = U_q then L_min(q) ≤ ⌈k^{3/2}/min(1, 𝔻_min)⌉, and always L_min(q) + 1 ≥
1/min(1, 𝔻_min) (when finite).
*Proof.* Lower: let y ∈ Λ* ∖ {0} and z ∈ ℝ^S with y·z ≡ ½ (mod 1). If z = λ + b with λ ∈ Λ, b ∈ [−r, r]^S, then y·b ≡ ½
and |y·b| ≤ r|y|₁, so r ≥ 1/(2|y|₁). Nonzero vectors of Λ* are either in ℤ^S (|y|₁ ≥ 1) or lifts of ψ ≠ 1 (|y|₁ ≥ 𝔻_S(ψ)).
Upper: μ_∞ ≤ μ_2 ≤ k/(2λ₁^{(2)}(Λ*)) (Banaszczyk, *Math. Ann.* 296 (1993), Thm 2.1: μ_2(Λ)·λ₁(Λ*) ≤ k/2) and
λ₁^{(2)} ≥ λ₁^{(1)}/√k. Prop 4.1(i) of FORCED_WINDOW needs μ_{(L,…,L)} ≤ 1, i.e. μ_∞ ≤ L/2; Prop 4.1(ii) gives μ_∞ ≤ (L+1)/2
when W_L = U_q. ∎
**Corollary 1.4 (scales; PROVED).** (a) (Minkowski for the cross-polytope, vol = 2^k r^k/k!) 𝔻_min(q) ≤ (k!/|H|)^{1/k}
≤ (k/e)(e√k)^{1/k}|H|^{−1/k} (k! ≤ e·k^{k+1/2}e^{−k}): some nontrivial character is always ℓ¹-pretentious at scale k|H|^{−1/k}.
(b) Hence **q is balanced at the random-lattice scale (L_min ≤ k^{O(1)}N^{1/k}) ⟺ (up to k^{O(1)}) no ψ ≠ 1 of U_q has
𝔻_S(ψ) ≤ N^{−1/k}k^{−C}**, i.e. the Minkowski-extremal character is not much more pretentious than forced by pigeonhole.
(c) Exact zero: 𝔻_S(ψ) = 0 for some ψ ≠ 1 ⟺ H ≠ U_q ⟺ for some prime ℓ | N all s ∈ S are ℓ-th powers mod q (the index
obstruction of FORCED_WINDOW Prop 5.2).
*Proof.* (a) Minkowski's first theorem: a symmetric convex body of volume > 2^k·det(Λ*) = 2^k/|H| contains a nonzero point
of Λ*; the ℓ¹-ball of radius r has volume (2r)^k/k!; Stirling. (b) Prop 1.3. (c) ψ ≠ 1 trivial on all g_s ⟺ H ⊂ ker ψ ⊊ U_q;
take ψ of prime order ℓ (U_q cyclic). ∎
*Reading.* Balance is a *quantitative non-pretentiousness of all characters of U_q on the k forced primes*, at the
Diophantine scale N^{−1/k} (not at a fixed scale: FORCED_WINDOW Prop 1.3). The index obstruction is the degenerate case
𝔻 = 0 and involves only characters of prime order; balance in general is decided by the **order** of the extremal character
ψ_min, which is the parameter that governs Frobenius-visibility (§2).

## 2. What Frobenius sees: the characters of small order, and nothing else

For odd m let K_m := ℚ(ζ_m, S^{1/m}). For q ∤ m∏S with m | N, fix a character χ_m of F_q^* of exact order m and write
χ_m(s) = e(b_s/m), b = b(q) ∈ (ℤ/m)^S; changing χ_m replaces b by u·b, u ∈ (ℤ/m)^*.

**Proposition 2.1 (Frobenius visibility; PROVED, Kummer theory).** (a) The Frobenius class of q in K_m determines the orbit
(ℤ/m)^*·b(q), hence the set Θ_m(q) := {θ(ψ) : ψ ∈ Û_q, ψ^m = 1} = {(2jb_s/m)_s : j ∈ ℤ/m} ⊂ (ℝ/ℤ)^S, hence every quantity
min{𝔻_S(ψ) : ψ ≠ 1, ψ^m = 1}. (b) Conversely the data {Frob_q in K_m : m | N, m ≤ M} is a function of a(q) mod N₁ only,
where a(q) ∈ (ℤ/N)^S is the discrete-log vector of (g_s) w.r.t. a generator of U_q and N = N₁N₂ with N₁ the M-smooth part
(all prime factors ≤ M) and N₂ the M-rough part. (c) The number of characters of U_q of order ≤ M is ≤ Σ_{d|N, d≤M} φ(d)
< M²; they are a fraction < M²/N of Û_q.
*Proof.* (a) q ≡ 1 (mod m) splits completely in ℚ(ζ_m); for 𝔮 | q in ℚ(ζ_m), Frob_𝔮(s^{1/m}) = (s/𝔮)_m·s^{1/m}, and the
m-th power residue symbol (s/𝔮)_m is the image of s^{(q−1)/m} mod 𝔮 in μ_m, i.e. χ_m(s) for the χ_m attached to 𝔮; another
𝔮 (or the conjugacy class) acts by an automorphism of μ_m, i.e. b ↦ ub. ψ ∈ Û_q with ψ^m = 1 are the χ_m^{2j}|_{U_q}
(m odd), with ψ(g_s) = χ_m(s)^{2j}. (b) m | N and m ≤ M forces m | N₁, and b(q) for χ_m = (χ_{N}-power) is a(q) mod m up
to a unit. (c) Σ_{d≤M} φ(d) < M². ∎

**Proposition 2.2 (indistinguishability; PROVED, elementary).** Let M ≥ 1, N = N₁N₂ as above with N₂ > 1, and let L ≥ 1.
For every a ∈ (ℤ/N)^S with ⟨g_s⟩ = U_q there is a′ ∈ (ℤ/N)^S with a′ ≡ a (mod N₁), generating (ℤ/N), whose lattice
Λ′ := {x : a′·x ≡ 0 (mod N)} has **L′_min + 1 ≥ N₂** (L′_min the least cube side covering ℤ/N by the box sums of a′).
Hence no function of the Frobenius data of q in the fields K_m, m ≤ M, certifies L_min(q) ≤ L at any q whose M-rough part
N₂(q) exceeds L + 1; in particular at any q with a prime factor ℓ | q − 1, ℓ > max(M, L + 1).
*Proof.* Pick s₀ ∈ S. Choose a′ ≡ a (mod N₁), a′_{s₀} ≡ 1 and a′_s ≡ 0 (s ≠ s₀) (mod N₂) (CRT). a′ generates: mod each
prime ℓ | N₁ because a does, mod ℓ | N₂ because a′_{s₀} ≡ 1. Every x ∈ Λ′ has x_{s₀} ≡ 0 (mod N₂), so y := e_{s₀}/N₂ ∈ Λ′*
with |y|₁ = 1/N₂ < 1, i.e. 𝔻_min ≤ 1/N₂, and Prop 1.3 (lower bound; and Prop 4.1(ii) of FORCED_WINDOW) gives
L′_min + 1 ≥ 2μ_∞(Λ′) ≥ N₂. By Prop 2.1(b) a and a′ have the same visible data. ∎
*Reading.* The fake a′ is the extreme Prop 5.2-type degeneracy (all s ≠ s₀ are N₂-th powers) placed entirely in the
invisible part. Prop 2.2 is a statement about information, not probability: it says that at a window with P⁺(q − 1) above
both the Chebotarev range M and the target side L, **balance is not a Frobenius condition of manageable degree**; any proof
must either (i) restrict to q with q − 1 being max(M, L)-smooth (§4), or (ii) bound the invisible part statistically,
over q, without Frobenius structure (§3).

**Theorem 2.3 (what GRH certifies: the visible part of balance; CONDITIONAL on GRH for the Dedekind zeta functions of
F_m := ℚ(ζ_{8P}, √p, K_m), m ≤ M; proof at citation level, Lagarias–Odlyzko as in CAP_INTERPOLATION Thm 4.2).** Let
P := ∏S (S = odd primes ≤ y, k = |S|), p ∤ 8P prime, x large, 0 < ε ≤ ½ and M ≥ 3 with
`  (★)  Σ_{m≤M odd} φ(m)(1 + 2εm)^k  ≤  c₀ √x /(φ(8P) log²(8PpMx)).`
Then #{q ≤ x : q ≡ 3 (8), q ≡ −p (P), (q/p) = −1, and 𝔻_S(ψ) ≥ ε for every ψ ≠ 1 of U_q of order ≤ M} ≥ (c₁ − o(1))·
x/(φ(8P)·log x), with c₁ := ½ − Σ_{m≥3 odd} ((1 + 2εm)/m)^k (positive for k ≥ 3 when εM ≤ ¼).
*Proof sketch.* The bad event at level m is a union of Frobenius classes C_m in Gal(F_m/ℚ) (Prop 2.1(a)) with
|C_m| ≤ φ(m)·#{c ∈ ℤ^S : |c_s| ≤ εm} ≤ φ(m)(1 + 2εm)^k classes of size ≤ 1 times the fixed cyclotomic/√p data (q ≡ 1 (m), the
class mod 8P, χ_p(q) = −1 — all central conditions). For odd m and S a set of primes, [K_m : ℚ(ζ_m)] = m^k (Kummer theory:
S is independent in ℚ(ζ_m)^*/ℚ(ζ_m)^{*m} for odd m; e.g. Moree's survey, *Integers* 12A (2012), §§3–4), and F_m/ℚ(ζ_{8Pm}, √p)
has degree m^k when √p, ζ_{8P} ∉ K_m (as in CAP_INTERPOLATION Thm 4.2: ramification at p). Lagarias–Odlyzko under GRH:
π_C(x) = (|C|/|G|) li(x) + O((|C|/|G|)√x(log d_F + n_F log x)), log d_F ≤ n_F log(n_F·8Ppm∏S); the main term of level m is
≤ li(x)·(1 + 2εm)^k/(m^k φ(8P)) and the total error is O(Σ_m |C_m| √x log(8PpMx)) — absorbed by (★). Subtract from the
GRH count ½ li(x)/φ(8P)(1 + o(1)) of the class (FORCED_WINDOW Thm 4.3). ∎
**Corollary 2.4 (the visible part is the index condition below N^{1/k}; PROVED + arithmetic).** (a) If εM < 1 the
condition of Thm 2.3 at order ≤ M is exactly "no prime ℓ ≤ M, ℓ | N, with all s ∈ S ℓ-th powers" (a character of order
d ≤ M has angles in (1/d)ℤ, so 𝔻 < ε < 1/d forces 𝔻 = 0; Cor 1.4(c)). (b) Balance at the random-lattice scale needs
ε ≍ N^{−1/k}k^{−C} (Cor 1.4(b)); then Σ_m φ(m)(1 + 2εm)^k ≍ (3εM)^k M²/(k + 2) and (★) allows at most
`  M_max ≍ x^{1/k}·( (√x/φ(8P)) / (3^k x^{2/k} log²(8PpMx)) )^{1/(k+2)}  ≤  x^{3/(2k+4)}`
(≤ x^{1/k}·(log p)^{O(1/k)} in the regime x ≍ φ(8P)² log⁴ p of FORCED_WINDOW Thm 4.3; below N^{1/k}, where by (a) only the
index condition is visible, whenever √x/φ(8P) < 3^k x^{2/k}). So Theorem 2.3 controls characters of order ≤ x^{O(1/k)},
a fraction ≤ x^{O(1/k)−1} of Û_q; and by Prop 2.2 it implies no bound on L_min(q) below N₂(q) − 1.
