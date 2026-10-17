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
the class, but (R-O256 repair 4) in the class −p mod 8P it can afford essentially only the index condition (Assessment 2.3,
Lemma 2.5). Barrier: the characters of order ≤ M are a fraction ≤ M²/N of all characters, and
the extremal (balance-deciding) character has order ≍ N in practice (§6). Hypothesis violated by the brief's route:
"imbalance is driven by small-order (index) obstructions".
(I2) *Modification: see all orders, give up classes.* Fejér-weighted collision counting bounds the large-order pretentious
primes globally (Prop 3.1, no 2^k loss) but not in a class of density 1/φ(8P): the P-loss, exactly (Cor 3.3). Hypothesis
violated next: "no input about classes" → isolate the weakest class/sparsity input: EQ (Thm 4.1) or the p-free, class-free S
(Thm 4.2) ⇒ (log₂p)^{13/2}, (log₂p)^{9/2}.
(I3) *Violate "q − 1 has a large prime factor" (the hypothesis of Prop 2.2):* windows with q − 1 smooth make each prime-power
component Frobenius-visible, but the joint law is still in a field of degree ≈ N^{k+1}; smooth shifted primes with u → ∞ are
unknown anyway (z27_smooth_shift_crt).
(I4) *Violate "the window group has large exponent":* composite windows with U_m of exponent | E make covering automatic at
cap ≈ E; a Linnik adversary on the menu forces E ≳ log p i.o. (z27_small_exponent_windows).
(I5) *Large sieve over moduli on the S-unit box:* S-units too sparse (z27_large_sieve_sunits).

## 1. Exact dictionary: balance ⟺ no nontrivial character is ℓ¹-pretentious to 1 on S

**Lemma 1.1 (dual lattice = character group; PROVED, standard).** The map ψ ↦ θ(ψ) := (θ_s(ψ))_{s∈S} + ℤ^S is an isomorphism
Ĥ ≅ Λ*/ℤ^S. In particular ℤ^S ⊂ Λ* with index |H|, and a vector y ∈ Λ* ∖ ℤ^S is the same thing as a nontrivial character ψ of H
together with a choice of real lifts θ_s ∈ ℝ of its angles.
*Proof.* x ↦ g^x := ∏ g_s^{x_s} induces ℤ^S/Λ ≅ H. Characters of ℤ^S are x ↦ e(y·x), y ∈ ℝ^S/ℤ^S; such a character factors
through ℤ^S/Λ iff y·x ∈ ℤ for all x ∈ Λ, i.e. y ∈ Λ*. The factored character is ψ with ψ(g_s) = e(y_s). ∎

**Definition 1.2 (ℓ¹-pretentious distance on S).** For ψ ∈ Û_q (characters of the whole U_q; R-O256 repair 1) put 𝔻_S(ψ) := Σ_{s∈S} ‖θ_s(ψ)‖ (the least ℓ¹-norm in the coset
θ(ψ) + ℤ^S), and 𝔻_min(q) := min_{ψ ∈ Û_q, ψ ≠ 1} 𝔻_S(ψ). (Restricted to Ĥ, 𝔻 is never 0 on ψ ≠ 1; on Û_q it vanishes exactly
when H ≠ U_q, Cor 1.4(c). When H = U_q, Ĥ = Û_q and Lemma 1.1 applies verbatim.) (Compare Granville–Soundararajan's 𝔻(χ, 1; y)² = Σ_{s≤y}(1 − Re χ(s))/s:
here the weights are flat, the angle enters linearly, and only the k primes of S count.)

**Proposition 1.3 (transference; PROVED, Banaszczyk + elementary).** Assume H = U_q. Then λ₁^{(1)}(Λ*) = min(1, 𝔻_min(q)) and
`  1/(2 min(1, 𝔻_min))  ≤  μ_∞(Λ)  ≤  k^{3/2}/(2 min(1, 𝔻_min)).`
Consequently (FORCED_WINDOW Prop 4.1): L_min(q) ≤ ⌈k^{3/2}/min(1, 𝔻_min)⌉, and always L_min(q) + 1 ≥
1/min(1, 𝔻_min). (If H ≠ U_q, L_min = ∞ and 𝔻_min = 0: the statement extends with 1/0 = ∞.)
*Proof.* Lower: let y ∈ Λ* ∖ {0} and z ∈ ℝ^S with y·z ≡ ½ (mod 1). If z = λ + b with λ ∈ Λ, b ∈ [−r, r]^S, then y·b ≡ ½
and |y·b| ≤ r|y|₁, so r ≥ 1/(2|y|₁). Nonzero vectors of Λ* are either in ℤ^S (|y|₁ ≥ 1) or lifts of ψ ≠ 1 (|y|₁ ≥ 𝔻_S(ψ)).
Upper: μ_∞ ≤ μ_2 ≤ k/(2λ₁^{(2)}(Λ*)) (Banaszczyk, *Math. Ann.* 296 (1993), his formally proved covering-radius transference bound μ_2(Λ)·λ₁(Λ*) ≤ k/2, valid for every k; R269 repair: theorem number not verified, Thm 2.2 to the reviewer's recollection) and
λ₁^{(2)} ≥ λ₁^{(1)}/√k. Prop 4.1(i) of FORCED_WINDOW needs μ_{(L,…,L)} ≤ 1, i.e. μ_∞ ≤ L/2; Prop 4.1(ii) gives μ_∞ ≤ (L+1)/2
when W_L = U_q. ∎
**Corollary 1.4 (scales; PROVED).** (a) (Minkowski for the cross-polytope, vol = 2^k r^k/k!; R-O256 repair 1: needs
|H| > k!, so that the Minkowski vector has ℓ¹-norm < 1 and is not in ℤ^S) if H = U_q and N > k!, 𝔻_min(q) ≤ (k!/|H|)^{1/k}
≤ (k/e)(e√k)^{1/k}|H|^{−1/k} (k! ≤ e·k^{k+1/2}e^{−k}): some nontrivial character is always ℓ¹-pretentious at scale k|H|^{−1/k}.
(b) Hence **q is balanced at the random-lattice scale (L_min ≤ k^{O(1)}N^{1/k}) ⟺ (up to k^{O(1)}) no ψ ≠ 1 of U_q has
𝔻_S(ψ) ≤ N^{−1/k}k^{−C}**; precisely (R269 repair): 𝔻_min ≥ k^{−C}N^{−1/k} ⇒ L_min ≤ ⌈k^{C+3/2}N^{1/k}⌉, and
L_min ≤ k^{C}N^{1/k} ⇒ 𝔻_min ≥ 1/(L_min + 1) ≥ k^{−C}N^{−1/k}/2; i.e. the Minkowski-extremal character is not much more pretentious than forced by pigeonhole.
(c) Exact zero: 𝔻_S(ψ) = 0 for some ψ ≠ 1 ⟺ H ≠ U_q ⟺ for some prime ℓ | N all s ∈ S are ℓ-th powers mod q (the index
obstruction of FORCED_WINDOW Prop 5.2).
*Proof.* (a) Minkowski's first theorem: a symmetric convex body of volume > 2^k·det(Λ*) = 2^k/|H| contains a nonzero point
of Λ*; the ℓ¹-ball of radius r has volume (2r)^k/k!; Stirling; a nonzero point of ℓ¹-norm < 1 is not in ℤ^S, so it is a lift of some ψ ≠ 1 (Lemma 1.1). (b) Prop 1.3. (c) ψ ≠ 1 trivial on all g_s ⟺ H ⊂ ker ψ ⊊ U_q;
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
Hence (R-O256 repair 5: an *abstract-vector* statement) no implication "visible data ⇒ L_min ≤ L" that is valid for **all
generating vectors a ∈ (ℤ/N)^S with the given visible data** exists once N₂ > L + 1 — in particular when some prime
ℓ | q − 1 exceeds max(M, L + 1). (Whether the fake a′ is realised as the discrete-log vector of the fixed primes S at some actual
prime q is not addressed; an argument exploiting arithmetic constraints on which vectors occur is not excluded.)
*Proof.* Pick s₀ ∈ S. Choose a′ ≡ a (mod N₁), a′_{s₀} ≡ 1 and a′_s ≡ 0 (s ≠ s₀) (mod N₂) (CRT). a′ generates: mod each
prime ℓ | N₁ because a does, mod ℓ | N₂ because a′_{s₀} ≡ 1. Every x ∈ Λ′ has x_{s₀} ≡ 0 (mod N₂), so y := e_{s₀}/N₂ ∈ Λ′*
with |y|₁ = 1/N₂ < 1, i.e. 𝔻_min ≤ 1/N₂, and Prop 1.3 (lower bound; and Prop 4.1(ii) of FORCED_WINDOW) gives
L′_min + 1 ≥ 2μ_∞(Λ′) ≥ N₂. By Prop 2.1(b) a and a′ have the same visible data. ∎
*Reading.* The fake a′ is the extreme Prop 5.2-type degeneracy (all s ≠ s₀ are N₂-th powers) placed entirely in the
invisible part. Prop 2.2 is a statement about information, not probability: a certificate of balance built only from the
low-order Frobenius data, uniformly over the vectors compatible with it, is impossible at windows with P⁺(q − 1) above both M
and L. A proof along the brief's route must therefore either (i) restrict to q with q − 1 being max(M, L)-smooth and then control
the *joint* law of the prime-power components (z27_smooth_shift_crt), or (ii) bound the invisible part statistically over q
(§3) — or use arithmetic information about the specific vectors a(q) that this proposition does not model.

**Assessment 2.3 (GRH accounting for the visible part; R-O256 repair 2/4: demoted from "Theorem" — the general small-angle
version needs a careful conjugacy-class count, compositum conductor lcm(8P, m) and linear-disjointness proof that are not
supplied).** The event "some ψ ≠ 1 of order dividing m has 𝔻_S(ψ) < ε" is a union of Frobenius conjugacy classes in
Gal(ℚ(ζ_{lcm(8P,m)}, √p, S^{1/m})/ℚ) (Prop 2.1(a)); the number of Kummer vectors b ∈ (ℤ/m)^S involved is ≤ φ(m)·#{c ∈ ℤ^S : |c_s| ≤ εm}.
Under GRH (Serre 1981, Thm 4: π_C(x) = (|C|/|G|)li(x) + O(|C|x^{1/2}(log d_F/n_F + log x)), |C| = number of elements) each level
m costs an error ≍ (number of bad elements)·√x·log(pPMx), against the class main term ≍ x/(φ(8P) log x) ≍ √x log² p/log x in the
regime x ≍ φ(8P)² log⁴ p used in §4. So GRH can afford only (log p)^{O(1)} bad elements in total: for ε below 1/M this is the
index condition alone (Prop 2.4(a)), while for εm ≥ 1 a single level m already carries ≈ φ(m)(2εm)^k bad vectors,
exponential in k. In short (Assessment, not a theorem): **GRH-Chebotarev in the
class −p mod 8P controls little beyond the index condition**, i.e. characters of order ≲ 1/ε with 𝔻 = 0, plus at most
(log p)^{O(1)} further Kummer vectors; a negligible part of Û_q (|Û_q| = N ≍ x). (R269 repair: refined GRH error terms —
Murty–Murty–Saradha 1988, Bellaïche 2016 (Littlewood complexity) — replace |C| by roughly the Fourier ℓ¹-norm of 1_C, ≲ φ(m)(c log(2εm + 2))^k
for the Kummer part; at k ≍ y/log y, M ≥ y this is still ≈ exp(log₂p·log₄p) ≫ log p, so the conclusion stands. The vector count
above is for characters of exact order m.)

**Proposition 2.4 (PROVED).** (a) If ψ ≠ 1 has order d and 𝔻_S(ψ) < 1/d, then 𝔻_S(ψ) = 0 (angles lie in (1/d)ℤ); so for
ε ≤ 1/M "no ψ ≠ 1 of order ≤ M with 𝔻 < ε" is exactly "no prime ℓ ≤ M, ℓ | N, with S ⊂ (F_q^*)^ℓ" (take ψ^{d/ℓ}).
(b) The number of characters of U_q of order ≤ M is < M² (Prop 2.1(c)), a fraction < M²/N of Û_q.

**Lemma 2.5 (the index obstruction in the class; CONDITIONAL on GRH for the Dedekind zeta functions of
F_ℓ := ℚ(ζ_{lcm(8P,ℓ)}, √p, S^{1/ℓ}), ℓ odd prime; R-O256 repair 3).** Let S = odd primes ≤ y, P = ∏S, p > z a prime ∤ 8P,
and fix σ₀ := (class a mod 8P, sign of χ_p). For odd primes ℓ ≤ z,
`  #{q ∈ (x/2, x] : q ↦ σ₀, ℓ | q − 1, S ⊂ (F_q^*)^ℓ}  ≤  (li(x) − li(x/2))/(2φ(8P)ℓ^k) + O(√x·(k log ℓ + log(8Pp) + log x)).`
*Proof.* For odd ℓ, ℚ(ζ_n, a^{1/ℓ}) is abelian over ℚ only if a² is an ℓ-th power in ℚ (Schinzel, *Abelian binomials, power
residues and exponential congruences*, Acta Arith. 32 (1977)); for a = ∏_{s∈S} s^{e_s} with ℓ ∤ e this fails, so by Kummer theory
[ℚ(ζ_n, S^{1/ℓ}) : ℚ(ζ_n)] = ℓ^k for every n with ℓ | n; and √p ∉ ℚ(ζ_{lcm(8P,ℓ)},
S^{1/ℓ}) because that field's maximal abelian subfield is ℚ(ζ_{lcm(8P,ℓ)}) (R269 repair: Gal = (ℤ/ℓ)^k ⋊ (ℤ/n)^* with u acting by multiplication by u mod ℓ; for u ≢ 1 (ℓ) the
commutators (u − 1)v exhaust (ℤ/ℓ)^k, so the abelianisation is (ℤ/n)^*) and p ∤ 8Pℓ. Hence
|G| = [F_ℓ : ℚ] = 2φ(lcm(8P, ℓ))ℓ^k ≥ 2φ(8P)ℓ^k. The q in question are those whose Frobenius restricts to σ₀ on ℚ(ζ_{8P}, √p),
to the identity on ℚ(ζ_ℓ, S^{1/ℓ}): F_ℓ is the compositum, so this is a set C with |C| ≤ 1 (empty if σ₀ forces q ≢ 1 (mod ℓ)).
Serre's GRH form of Lagarias–Odlyzko (Publ. IHÉS 54 (1981), Thm 4) gives the count (|C|/|G|)(li(x) − li(x/2)) +
O(|C|√x(log d_F/n_F + log x)), and log d_F/n_F ≤ log n_F + Σ_{r ram} log r ≤ (k + 1) log ℓ + log(2φ(8P)) + log(2ℓp·8P)
(Serre, loc. cit., Prop. 6). ∎

## 3. What class-blind counting gives: a Fejér pair count, and the P-loss in exact form

**Proposition 3.1 (class-blind count of pretentious primes; PROVED, elementary).** Let x ≥ 16, 0 < ε < 1, P = ∏S, and
`  Bad₁(ε) := {q prime : some ψ ≠ 1 of U_q has 𝔻_S(ψ) < ε and ord(ψ) > 1/ε}`
(R269 repair: q ranges over primes q ≡ 3 (mod 4), q ∤ P, as in the Notation; Thms 4.1/4.2 need only q ≡ 3 (mod 8), and EQ, S
may be read with that restriction.)
Let B ≥ 1 be an integer with (B + 1)^k ≥ 2x(2B + 1)ε. Then
`  #{q ∈ (x/2, x] ∩ Bad₁(ε)}  ≤  4B(2B + 1)·xε·log P / log(x/2).`
With B := ⌈(6xε)^{1/(k−1)}⌉ (valid once 6xε ≥ 1) the right side is ≤ 48·(6xε)^{(k+1)/(k−1)} log P/log(x/2).
*Proof.* Fix q ∈ (x/2, x] in Bad₁(ε), ψ the character, d := ord ψ > 1/ε, y ∈ ℝ^S a lift of θ(ψ) with |y|₁ = 𝔻_S(ψ) < ε.
For x′ ∈ Box := [0, B]^S ∩ ℤ^S, ψ(g^{x′}) = e(y·x′) with |y·x′| ≤ Bε; the d-th roots of unity in that arc number
≤ 2Bεd + 1, and ψ: U_q → μ_d has fibres of size N/d (N := (q−1)/2 < x/2), so g^{Box} lies in a set of size
≤ N(2Bε + 1/d) < (x/2)(2B + 1)ε. By Cauchy–Schwarz the number of pairs (x′, x″) ∈ Box² with g^{x′} = g^{x″} is
Π(q) ≥ (B + 1)^{2k}/((x/2)(2B + 1)ε) ≥ 4(B + 1)^k (hypothesis on B), so Π(q) − (B + 1)^k ≥ ¾Π(q) ≥ 3(B+1)^{2k}/(2x(2B+1)ε).
On the other hand, Σ_{q ∈ (x/2, x]} (Π(q) − (B + 1)^k) = Σ_{h ≠ 0} w(h)·#{q ∈ (x/2, x] : q | N_h}, where w(h) :=
∏_s (B + 1 − |h_s|)_+ (so Σ_h w(h) = (B + 1)^{2k}) and N_h := ∏_{h_s>0} s^{2h_s} − ∏_{h_s<0} s^{−2h_s} ≠ 0, |N_h| < P^{2B}; hence
#{q ∈ (x/2, x] : q | N_h} < 2B log P/log(x/2) and the sum is < (B + 1)^{2k}·2B log P/log(x/2). Divide. For the second form:
(B+1)^{k−1} ≥ 6xε gives (B + 1)^k ≥ 6xε(B + 1) ≥ 2x(2B + 1)ε, and B ≤ 2(6xε)^{1/(k−1)}, 4B(2B+1) ≤ 12B². ∎
(This is the dual form of CAP_INTERPOLATION Thm 4.2 (iv) / PHASE_DIAGRAM Step 2; the Fejér weighting removes their 2^k–6^k.)

**Proposition 3.2 (the visible remainder; PROVED).** If ψ ≠ 1 has 𝔻_S(ψ) < ε and ord ψ ≤ 1/ε, then 𝔻_S(ψ) = 0 and there is a
prime ℓ ≤ 1/ε, ℓ | N, with every s ∈ S an ℓ-th power mod q. Hence {q : 𝔻_min(q) < ε} ⊂ Bad₁(ε) ∪ Bad₂(1/ε), Bad₂(z) :=
{q : ∃ prime ℓ ≤ z, ℓ | N, S ⊂ (F_q^*)^ℓ}, and Bad₂ is a finite union of Chebotarev sets (Lemma 2.5).
*Proof.* Angles of ψ lie in (1/d)ℤ, so each nonzero ‖θ_s‖ ≥ 1/d ≥ ε > 𝔻_S(ψ) (R269 repair). Then ψ is trivial on H; take ψ^{d/ℓ}. ∎

**Corollary 3.3 (the P-loss, exact; PROVED + arithmetic).** In a single class a mod 8P the GRH count of candidate windows is
≍ x/(φ(8P) log x). Prop 3.1 bounds Bad₁ in that class only by its total, so it excludes Bad₁ from the class only when
48(6xε)^{(k+1)/(k−1)} log P ≤ c·x/φ(8P), i.e. ε ≍ x^{−2/(k+1)}(φ(8P) log P)^{−(k−1)/(k+1)}, and then Prop 1.3 gives
`  L ≍ k^{3/2}/ε ≍ k^{3/2}·x^{2/(k+1)}·(P log P)^{(k−1)/(k+1)}  ≥  P^{1−o(1)}`
— exactly the P-loss of z12_grh_lattice_gap; optimising y (with x ≥ P^{2+o(1)}(log p)^{2+ε} for the √p-condition) returns
e*(p) ≤ exp(O(√(log₂p·log₃p))), i.e. CAP_INTERPOLATION Thm 4.2(b), now as the dual/pretentious statement "a class mod P cannot
be shown to avoid the ε-pretentious primes unless the total number of such primes is < π(x)/φ(8P)".
*Reading.* Prop 3.1 is lossy against the random model by the factor 2B log P/log x per relation (each N_h is charged with all
its possible prime factors of size x instead of probability ≈ 1/x); but the loss that matters is the factor φ(8P), which
no class-blind bound can recover. GRH-Chebotarev is class-sensitive but, in the class, affordable only for the index condition and (log p)^{O(1)} further
Kummer vectors (Assessment 2.3; Prop 2.2 for the information-theoretic side);
Prop 3.1 sees all orders but no classes. **The two tools see complementary halves of the problem, and the extremal character
(order ≍ N, §6) falls in the half that only class-blind tools see.**

## 4. The exact missing input, and a conditional (log₂p)^{O(1)} cap from GRH + an upper-bound equidistribution hypothesis

**Hypothesis EQ (upper-bound equidistribution of pretentious primes at the forcing modulus).** There are absolute C, A such
that for all large x, every y with P := ∏_{3≤s≤y} s ≤ x^{1/2}, every ε ∈ (0, 1) and every reduced class a mod 8P,
`  #{q ∈ (x/2, x] ∩ Bad₁(ε) : q ≡ a (8P)}  ≤  (C/φ(8P))·#{q ∈ (x/2, x] ∩ Bad₁(ε)}  +  x^{1/2}(log x)^A.`
EQ involves no p: it says that the primes at which some character of large order is ε-pretentious to 1 on S do not
over-concentrate (beyond a constant factor and a square-root error) in any class modulo the product of S itself. It is an
*upper-bound* statement (Brun–Titchmarsh/Bombieri–Vinogradov shape at a single modulus ≈ √x), different in form from (no logical comparison is proved with)
Hypothesis W (an existence statement in the p-dependent class −p mod P with χ_p(q) = −1, at a near-optimal L).

**Theorem 4.1 (CONDITIONAL on GRH + EQ; PROVED relative to them).** Assume GRH for Dirichlet L-functions and for the Dedekind
zeta functions of ℚ(ζ_{lcm(8P,ℓ)}, √p, S^{1/ℓ}) (ℓ odd prime), and Hypothesis EQ. Then for every prime p ≥ p₀,
`  e*(p) ≤ (log₂ p)^{13/2 + o(1)}.`
*Proof.* p ≢ 1 (8): e* = 0 (classical, as in FORCED_WINDOW). Let p ≡ 1 (8), y := log₂p·log₃p, S = odd primes ≤ y, k = |S|,
P = ∏S, x := C₀φ(8P)² log⁴ p (C₀ large). Then log P = (1 + o(1))y, k = (1 + o(1))y/log y, log x = (2 + o(1))y.
*Good class count (GRH):* G := #{q ∈ (x/2, x] : q ≡ 3 (8), q ≡ −p (P), (q/p) = −1} = (1 + O(C₀^{−1/2}))(li(x) − li(x/2))/(2φ(8P)) ≥ c₂ x/(φ(8P) log x) (R269 repair: the asymptotic form is what the Bad₂
comparison below uses; FORCED_WINDOW
Thm 4.3, dyadic version). *Bad₂:* by Lemma 2.5 with z := 1/ε (ε fixed below), the q in the class with some prime
ℓ ≤ z, ℓ | N, S ⊂ (F_q^*)^ℓ number ≤ ((li(x) − li(x/2))/(2φ(8P)))Σ_{ℓ≥3} ℓ^{−k} + O(z√x log p) (R-O256 repair 3; the
log p term dominates the error of Lemma 2.5 since k log z, log P, log x = y^{1+o(1)} = o(log p)). Σ_{ℓ≥3} ℓ^{−k} ≤ Σ_{ℓ≥3} ℓ^{−3} < 0.05 (and → 0 as k → ∞; R269 repair), so the
main term is ≤ G/8, and the error is ≍ G·z log x/log p = G·y^{O(1)}/log p = o(G) since G ≍ √x log² p/log x and z = y^{O(1)}. *Bad₁ (EQ + Prop 3.1):* the class contains
≤ (C/φ(8P))·48(6xε)^{(k+1)/(k−1)} log P/log(x/2) + x^{1/2}(log x)^A elements of Bad₁(ε). The error term is ≤ G/8 since
√x/φ(8P) ≍ log² p ≫ (log x)^{A+1} = y^{O(1)}. The main term is ≤ G/8 for
`  ε := (1/6x)·(c₃ x/(C log P))^{(k−1)/(k+1)},   i.e.  1/ε = 6x^{2/(k+1)}(C log P/c₃)^{(k−1)/(k+1)} ≤ y^{4+o(1)}·y`
(the factor log P/log(x/2) of Prop 3.1 against 1/log x in G leaves log P; x^{2/(k+1)} = exp((4 + o(1)) log y)). So some q in
the class lies outside Bad₁(ε) ∪ Bad₂(1/ε); by Prop 3.2 𝔻_min(q) ≥ ε > 0, so H = U_q (Cor 1.4(c)) and
μ_∞(Λ_q) ≤ k^{3/2}/(2ε) (Prop 1.3): q is (y, L)-balanced (Def 4.2 of FORCED_WINDOW) with L := ⌈k^{3/2}/ε⌉ ≤ y^{5+3/2+o(1)}.
FORCED_WINDOW Thm 4.3 (with this q in place of the one supplied by W) gives e*(p) ≤ L − 1 ≤ y^{13/2+o(1)} = (log₂p)^{13/2+o(1)}. ∎
*Remarks.* (1) The exponent is not optimised: 4 = 2·2 comes from x^{2/(k+1)} (Prop 3.1 controls the dual only at the square
of the random-lattice scale x^{1/k}) and log x ≈ 2 log P; 1 from log P; 3/2 from transference. Under W with the random-model
L one gets 2 + o(1) (FORCED_WINDOW Cor 4.4). (2) Where each input is used: GRH — the class count with χ_p(q) = −1, and the
index (Chebotarev-visible) part Bad₂; EQ — only to transfer the class-blind Prop 3.1 into the class −p mod 8P. (3) EQ is
needed only for the single modulus 8P(y) with y ≍ log₂p·log₃p, x ≍ P² log⁴ p, and only up to a constant factor.

**Hypothesis S (sparsity of large-order pretentious primes; p-free AND class-free).** There is A such that for all large x
and every y with P(y) ≤ x^{1/2} (k = |S(y)|):  #{q ≤ x : q ∈ Bad₁(x^{−3/(2k)})} ≤ x^{1/2}(log x)^A.
*Random-model status (Assessment).* If the discrete-log vectors a(q) were uniform, each q would carry ≈ N·vol{ℓ¹-ball of
radius ε} = N(2ε)^k/k! characters with 𝔻 < ε, so #Bad₁(ε) ∩ [1, x] ≈ x²(2ε)^k/(2k!·log x) = x^{1/2}·2^k/(2k! log x) at
ε = x^{−3/(2k)} — a rare-event heuristic up to constants (R-O256 minor: characters come in ± pairs and low orders sit on finite
grids; the exact expectation is a divisor sum Σ_{d|N} φ(d)A_k(d, ε)/d^k): S is the random-model prediction, with room. It is NOT
known at the required square-root level: its index-degenerate part alone
(index ≥ x^{3/(2k)}) is known only with exponent 1 − 1/(2k) − O(1/k²) in place of 1/2 (Prop 3.1 / PHASE_DIAGRAM Step 2), and
GRH-Chebotarev cannot reach it (per prime ℓ the error is already ≍ √x log x).
**Theorem 4.2 (CONDITIONAL on GRH + S; PROVED relative to them).** (R269 repair: GRH as in Thm 4.1 — Dirichlet L-functions
and the Dedekind zeta functions of ℚ(ζ_{lcm(8P,ℓ)}, √p, S^{1/ℓ}), ℓ odd prime.) e*(p) ≤ (log₂p)^{9/2+o(1)} for p ≥ p₀.
*Proof.* As Thm 4.1 with ε := x^{−3/(2k)}: the class contains ≤ x^{1/2}(log x)^A ≤ G/8 elements of Bad₁(ε) (no EQ needed: the
total is already below the class main term G ≍ √x log² p/log x), Bad₂(1/ε) is handled by Lemma 2.5 as before (1/ε = y^{3+o(1)}), and
L = ⌈k^{3/2}x^{3/(2k)}⌉ = y^{3/2+3+o(1)}. ∎
*Reading.* S ⇒ EQ at the parameters used (the class count is bounded by the total). Hence the clean statement:
**GRH reduces "e*(p) ≤ (log₂p)^{O(1)} for every p" to a p-free, class-free sparsity statement about primes q at which the
first k odd primes are nearly multiplicatively dependent through a character of large order** — the multiplicative-
dependence analogue of bounding the primes q for which a fixed integer has small order (Erdős–Murty / Kurlberg–Pomerance
type), in rank k ≍ log x/log log x and at the square-root level. Neither EQ nor S is a standard named hypothesis; I know of no
standard conjecture (GRH, Elliott–Halberstam, Artin-type) that implies either, because Bad₁ is neither a set of primes in
progressions nor determined by Frobenius data in Kummer–cyclotomic fields of degree (log p)^{O(1)} (Prop 2.2, in its
abstract-vector sense; R269 repair: Prop 2.2 does not show that Bad₁ is not a Chebotarev set).
**Remark 4.3 (almost all p under GRH alone; CONDITIONAL on GRH, Assessment-level bookkeeping).** EQ holds trivially *on
average over classes*: at most φ(8P)/C classes a can carry more than (C/φ(8P))·#Bad₁. Since −p mod 8P equidistributes as p
varies, GRH alone gives e*(p) ≤ (log₂p)^{13/2+o(1)} for all p outside a set of relative density O(1/C) (any fixed C; freeze
y on dyadic blocks of p so that 8P is constant on each block, then let C → ∞ slowly), i.e. for almost all p. This is weaker than the known unconditional almost-all bound (CAP_INTERPOLATION §2: e ≍ log₂N with
≤ N^{1−c/(log₂N log₃N)} exceptions), so it is recorded only as a consistency check — answer to the brief's question (i): **no
new almost-all statement**.

## 5. Cap 0, and the barrier screen

**Proposition 5.1 (the forced sub-box is useless at cap 0; PROVED; R-O256 repair 6 — narrowed).** At a forced window q
with P | K_q, the cap-0 parity box of FORCED_WINDOW Lemma 1.1 restricted to the forced primes s ∈ S with b_s = 1 is {0, 1}^S
(2^k elements). For the windows of Thms 4.1–4.2 (q ≍ φ(8P)² log⁴ p, 2^k = P^{o(1)}) this guaranteed sub-box is far smaller
than |U_q| = (q − 1)/2, so the balance bounds at positive cap say nothing about cap 0: a cap-0 certificate must come from the
uncontrolled part of the box (other primes of K, higher valuations) hitting the single target, i.e. the closest-vector event of
FORCED_WINDOW Prop 4.5 — in the window variable a least-residue event (Prop 2.1 there), the B2 divisor event.
*Proof.* Box size vs group order. ∎ (Not claimed: that cap 0 fails at such windows — e.g. p = 409, q = 11, K = 105 = 3·5·7 is
forced and the cap-0 parity box {3^{2j₁}5^{2j₂}7^{2j₃}} = {1, 3, 4, 5, 9} = U₁₁ covers; the reviewer's example. Small windows
can be covered at cap 0; the windows of §4 are not small.)

*Barrier screen (Assessment).* B1 (congruence/CRT): the forcing q ≡ −p (P) is congruence data, but the balance input is not —
Prop 2.2 is a precise statement that it cannot be. B2: Thms 4.1/4.2 are at cap ≥ 1 by design (Prop 5.1); bounded or
(log₂p)^{O(1)} cap is not ES. B3: the certificates are coverings (all targets), not main-term counts at a single target; the
scale constraint is Prop 4.1(iii) of FORCED_WINDOW (L ≥ (log q)^{1−o(1)}), consistent with (log₂p)^{O(1)}. B5/T1: the route has an explicit step that is false at n = m²: the GRH count of forced windows uses a
non-principal χ_n(q) = (q/n), and for n = m² one has (q/n) = 1 for all q ∤ m — there are no forced windows, as T1 requires
of any Type-II-shaped route (cap 0 at odd squares is excluded, CAP_DOWN §3; at cap ≥ 1 e*(n) < ∞ is already PROVED for all odd
n, CAP_POINTWISE Thm 1.1, so T1 does not test cap ≥ 1 bounds). B6: Thms 4.1/4.2 are pointwise in p; the only averaging is over windows q
in a p-dependent class, and EQ/S are exactly the statements that make that averaging honest at a single class.

## 6. Numerics (EVIDENCE)

`scripts/z27_dual.py y QLO QHI SAMPLE SEED [classes]`: exact 𝔻_min(q) by brute force over all N − 1 characters of U_q
(q ≡ 3 (8), S = odd primes ≤ y), the order of the extremal character ψ_min, P⁺(N), and the same for a uniformly random
discrete-log vector (random-lattice model). ν := 𝔻_min·N^{1/k} (Minkowski: ν ≤ (k!)^{1/k}; balance ⟺ ν not small).
* **ν matches the random model** (data/z27/dual_1e6.txt, 3000 random q ≤ 10⁶ each; dual_1e7.txt, 400 q ∈ [9·10⁶, 10⁷] each):
  quantiles (conditioned on 𝔻_min > 0; R269 repair) 1/10/50/90 % true vs random: k = 3, q ≤ 10⁶: 0.267/0.563/1.011/1.375 vs 0.265/0.577/1.026/1.372; k = 4:
  0.454/0.784/1.208/1.532 vs 0.381/0.743/1.194/1.535; k = 5: 0.597/0.985/1.389/1.714 vs 0.611/0.979/1.392/1.711; near 10⁷ the
  same to ±0.07. Index-degenerate (ν = 0) counts also match (k = 3: 52 vs 61 of 3000).
* **The extremal character has large order: P⁺(N) | ord ψ_min in > 99 %, ord = N in ≈ 75 % (R269 repair: "≍ N" holds only in
  this sense) (the SHARP observation; statistics conditioned on generation, 𝔻_min > 0 — R-O256
  repair 7; reruns with exact integer 𝔻 reproduce the tables).** ord ψ_min = N in 73–78 %, ≥ N^{0.9} in 86–88 %,
  ≤ N^{1/2} in ≤ 0.3 %, ≤ N^{3/(2k+4)} (a nominal "visible" range; R-O256 repair 4: not an established GRH cutoff) in ≤ 0.07 % (0 of 400 near 10⁷ for every k);
  **P⁺(N) | ord ψ_min in 99.4 %–100 %** — identical to the random model. Balance is decided by the largest prime factor of
  q − 1, the part Frobenius cannot see (Prop 2.2).
* **Worst q** (smallest ν, non-degenerate): k = 3: q = 237 971, ν = 0.058, ord = N = 118 985, P⁺(N) = 449; k = 5: q = 423 883,
  ν = 0.108. Near 10⁷: q = 9 842 267 (k = 3, ν = 0.185, ord = N).
* **Per class mod 8P** (dual_classes_y7.txt, all 6450 q ≤ 3·10⁵, 48 classes mod 840): every class has a q with ν ≥ 1.48 (best per
  class: min 1.481, median 1.575), while the per-class worst is 0 (degenerate) in most classes — consistent with z24's L_min test.
* **Hypothesis EQ at toy scale** (`scripts/z27_eqcheck.py`, R-O256 repair 7: Bad₁ is now *existential* — some ψ with
  𝔻 < ε = tN^{−1/k} and ord ψ > 1/ε — 𝔻 in exact integers, and a 300-fold permutation null preserving class populations).
  eqcheck_y7.txt (all 19 609 q ≡ 3 (8) ≤ 10⁶, 48 classes mod 840): Bad₁ at t = 0.3 / 0.5 / 0.7: 250 / 1272 / 3463 q,
  χ² = 49.5 / 28.0 / 29.8 (df 47), permutation p = 0.33 / 0.97 / 0.86 — no over-concentration. The *full* set "some ψ ≠ 1 with
  𝔻 < ε" (including small-order and index-degenerate q): χ² = 214 / 96 / 65, p = 0.003 / 0.003 / 0.007 — strongly class-correlated
  (ℓ | N needs q ≡ 1 (ℓ)), exactly the Chebotarev-visible part that GRH handles (Lemma 2.5). (The existential/minimiser distinction
  matters rarely: e.g. q = 74 419 has a degenerate order-3 minimiser and a qualifying order-12 403 character with 𝔻 ≈ 0.0079.)
  eqcheck_y11.txt (all 37 217 q ≤ 2·10⁶, 480 classes mod 9240): Bad₁ at t = 0.3 / 0.5 / 0.7: 72 / 653 / 2513 q, χ² = 543.5 /
  474.2 / 405.8 (df 479), permutation p = 0.033 / 0.44 / 0.93; full set p = 0.003 / 0.12 / 0.71. The one marginal value (72
  events spread over 480 classes, max 3 per class) is the sparsest cell; not significant after the 6 tests per k. (R269 repair: the 3 events are all in class 6931 ≡ 1 (mod 1155), the extreme class
  where P | N; a pre-specified re-test on fresh q ∈ (2·10⁶, 8·10⁶] finds 0/202 there vs 1/198 in a control class — a fluke;
  the class a ≡ 1 (mod P) is the natural worst case for EQ in future tests.) EVIDENCE for EQ only at P ≤ 1155, nowhere near P ≈ √x.
* *T1 control:* not applicable to these p-free statistics; the construction's T1 step (no forced windows at n = m²) is
  algebraic (§5). Odd-square cap-0 absence was checked in z24.

## 7. Verdict (O256 checkpoint 1)

1. **GRH alone: not by this route, and the reason is explicit** (R269 repair: partly Assessment 2.3). Balance at q is decided
   by a character of large order (§6: P⁺(q−1) | ord in > 99 %, ord = N in ≈ 75 %). Frobenius in Kummer fields ℚ(ζ_m, S^{1/m}) of GRH-manageable size sees only characters of order
   ≲ 1/ε plus (log p)^{O(1)} Kummer vectors in the class (Prop 2.4, Assessment 2.3), and no function of that data,
uniformly over compatible discrete-log vectors, certifies L_min below the M-rough part of q − 1 (Prop 2.2,
   PROVED). The only tool seeing all orders is class-blind counting (Prop 3.1), which cannot see a class of relative density
   1/φ(8P) and so returns the P-loss exp(O(√(log₂p log₃p))) (Cor 3.3). No GRH *barrier* is claimed (R264 D8): another method
   could still work; what is proved is that the brief's Hooley/Kummer route certifies only the index condition plus a negligible
   fraction of characters.
2. **GRH + one isolated hypothesis does it.** GRH + EQ (no over-concentration of large-order pretentious primes in classes mod
   8P) ⇒ e*(p) ≤ (log₂p)^{13/2+o(1)} (Thm 4.1); GRH + S (a p-free, class-free sparsity statement, the random-model prediction)
   ⇒ (log₂p)^{9/2+o(1)} (Thm 4.2). Both are alternative sufficient hypotheses to W (no logical comparison proved) and involve no p. Neither is standard.
3. (i) Almost all p: nothing new (Remark 4.3). (ii) Cap 0: balance is irrelevant (Prop 5.1; B2). (iii) Numerics: §6.
4. **Bounded/slowly growing cap is not ES**: all statements are at cap ≥ 1; cap 0 is the B2 divisor event.
