# CAP_POINTWISE — the minimal exponent cap e*(n) pointwise (task O236, spark relay Z6)

Status: in progress (O236). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on EXPONENT_CAP ((J)34: Def 1.1, Prop 1.2), CAP_INTERPOLATION (O234, §4: e*(n), Prop 4.1, Thm 4.2),
POINTWISE_SIZE §8 (windows q = 4x − p, Cor 8.3(b)), LITERATURE_2026 (vii) "test case". Scripts `scripts/z12_*`.

Normalisation (checked against EXPONENT_CAP Def 1.1): ES^{(y,e)}(n) is 4/n = 1/x + 1/y + 1/z, x, y ∈ ℤ_{>0},
z ∈ ℚ_{>0}, den z = q², q odd, gcd(q, n) = 1, rad q | y, v_ℓ(q) ≤ e. **e*(n) := min{e : ES^{(y,e)}(n)}; ES(n) ⟺
e*(n) = 0.** Hence "numerically e*(p) = 0 for all p ≤ 10^{17}" is just the known ES verification; the numerics of
goal (3) are only informative for *restricted constructions* (§3).

## 0. Iteration log

(Z6-1) Construction first. The obstacle to an unconditional pointwise cap in FROBENIUS_FIRING Thm 4.2 /
CAP_INTERPOLATION Thm 4.2 is the *Artin-type* step "⟨S⟩ ⊇ (F_r^*)² for a FIXED mute set S" (BV/Siegel–Walfisz, or GRH).
Hypothesis to violate: "S fixed, independent of the certificate". Modification: let the certificate generate its own
mute set — S := prime factors of x, with the window q = 4x − n the (small, prime) cofactor. Then n ≡ 4x (mod q)
makes −n/4 ≡ −x ∈ ⟨S⟩·(−1), and the only group-theoretic requirement left is −1 ∈ ⟨S⟩ mod q, which is FORCED by
the Legendre symbol (POINTWISE_SIZE Cor 8.3(b), parity of the 2-part of a cyclic group of order 2·odd). The
exponent budget, which is the ES obstruction ("F3", notes §70), is exactly what the cap e relaxes (EXPONENT_CAP
Prop 1.2). Result: Thm 1.1, a deterministic, unconditional, effective pointwise cap e*(n) < q(n).

## 1. The window theorem: an unconditional effective pointwise cap

**Theorem 1.1 (self-generated mute set; PROVED, elementary given EXPONENT_CAP Prop 1.2).** Let n ≡ 1 (mod 4) be
odd and not a square. Let q be a prime with
`  (i) q ∤ n,   (ii) q ≡ 4 − n (mod 8),   (iii) (q/n) = −1 (Jacobi symbol).`
Put K := (n + q)/4 and S := {primes s | K}. Then K is odd, gcd(K, qn) = 1, and there are exponents
0 ≤ a_s < ord_q(s) such that Q := ∏_{s∈S} s^{a_s} satisfies q | n + 4Q². With g := (n + 4Q²)/q,
`  x = K = (n+q)/4,   y = n(g+1)/4,   z = n·x·(g+1)/(4Q²)`
is an ES^{(y,e)}(n) solution with e ≤ max_s a_s − 1 ≤ q − 3. In particular **e*(n) ≤ q − 3.**
*Proof.* (ii) gives q + n ≡ 4 (mod 8): K is an odd integer, and q ≡ −n ≡ 3 (mod 4). If a prime s | K divides n then
s | q, s = q, contradicting (i); s = q | K would give q | n. So gcd(K, qn) = 1.
*Group step.* Mod q, n ≡ 4K − q ≡ 4K. Legendre: (−n/q) = (−1/q)(n/q) = −(n/q), and (n/q) = (q/n) by Jacobi reciprocity
(n ≡ 1 (4), n > 0), so (−n/q) = +1 by (iii); hence (−K/q) = (−n/4 / q) = 1 and (K/q) = −1. By multiplicativity some
s₀ ∈ S is a non-residue mod q. F_q^* is cyclic of order q − 1 = 2u, u odd; ord(s₀) is even, so s₀^{ord/2} = −1 ∈ H :=
⟨S mod q⟩. K = ∏ s^{v_s(K)} ∈ H, so −K ∈ H. −K is a square, so its order o divides u (odd), and
−K = ((−K)^{(o+1)/2})² with (−K)^{(o+1)/2} ∈ H. Write that element as ∏ s^{a_s} with 0 ≤ a_s < ord_q(s) and put
Q := ∏ s^{a_s} ∈ ℤ. Then Q² ≡ −K ≡ −n/4, i.e. q | n + 4Q².
*Shot step.* Q is odd and gcd(Q, n) = 1. g ≡ 3 (mod 4) since n + 4Q² ≡ 1 and q ≡ 3 (mod 4). For s | Q: s | K gives
q ≡ −n (mod s), and gq = n + 4Q² ≡ n (mod s), so g ≡ −1 (mod s) (n invertible mod s). Hence g ≡ −1 (mod 4 rad Q)
and (Q, g) is a shot datum (EXPONENT_CAP §1: Q ≥ 1, gcd(Q, n) = 1, g ≡ 3 (4), g | n + 4Q²) with cofactor
m = (n + 4Q²)/g = q, so x = (n + m)/4 = K. EXPONENT_CAP Prop 1.2: the solution lies in ES^{(y,e)} iff
g ≡ −1 (mod 4Q^{(e)}), Q^{(e)} = ∏ ℓ^{max(1, v_ℓ(Q) − e)}; with e := max a_s − 1 we have Q^{(e)} = rad Q. a_s ≤ q − 2. ∎

**Corollary 1.2 (all odd n; PROVED).** For every odd n > 1, e*(n) ≤ q*(n) − 3 (or 0), where:
(a) if some prime ℓ ≡ 3 (4) divides n, e*(n) = 0 (ES(ℓ) by 4/ℓ = 1/((ℓ+1)/4) + 1/(ℓ(ℓ+1)/2) + 1/(ℓ(ℓ+1)/2), scaled);
(b) if n is a non-square with all prime factors ≡ 1 (4), q*(n) := least prime with (i)–(iii) (exists by Dirichlet:
the conditions are one Frobenius class in Gal(ℚ(i, √2, √n)/ℚ) ≅ (ℤ/2)³, n ≡ 1 (4) non-square — see Remark 1.4);
(c) if n = a² (a odd, all primes ≡ 1 (4)), fix a prime p | a and let q*(n) := least prime with (i)–(iii) for p and
additionally q ≢ −p (mod ℓ) for every prime ℓ | a, ℓ ≠ p. Apply Thm 1.1 to p: gcd(K, n) = 1, so q is prime to n,
and 4/n = 1/(kx) + 1/(ky) + 1/(kz) (k = n/p) keeps den(kz) = q², rad q | ky.
*T1 check.* For n = a², (q/n) = 1 for every q ∤ n, so condition (iii) is never met at n itself: Thm 1.1 never fires at
an odd square (consistent with T1 / FROBENIUS_FIRING Thm 4.2(b)); (c) routes through the non-square divisor p.

**Theorem 1.3 (size of q*(n); PROVED relative to the cited theorems).**
(a) *Unconditional, explicit (n squarefree, e.g. n = p prime).* For squarefree n in case (b), (i)–(iii) say that q is
unramified in L := ℚ(i, √2, √n) with one prescribed Frobenius (q mod 8 fixes Frob on ℚ(ζ₈) = ℚ(i, √2); (q/n) = (n/q)
fixes it on √n). Conductors of the 8 characters: 1, 4, 8, 8, n, 4n, 8n, 8n, so d_L = 2^{16}n⁴. Ahn–Kwon (*Ann. Inst.
Fourier* 69 (2019), Thm 1.1, "sans aucune restriction": for Galois L ≠ ℚ and any conjugacy class C there is an
unramified prime with Frobenius C and norm ≤ d_L^{12577}) gives q*(n) ≤ (2^{16}n⁴)^{12577}, hence
**e*(n) < 2^{201232}·n^{50308} for every squarefree odd n > 1** (and for every odd n with a prime factor ≡ 3 (4),
e*(n) = 0). (Citation level: statement taken from the abstract; the exponent is irrelevant for the qualitative claim.)
(b) *Unconditional, effective (all odd n > 1).* In cases (b), (c) the conditions are implied by q lying in one
fixed class a mod 8·rad(n) (choose a mod 8; a mod rad(n) coprime to it with (a/n₀) = −1 in case (b), n₀ := squarefree
kernel of n — so (q/n) = (q/n₀) = −1 and q ∤ n; in case (c): (a/p) = −1 and a ≢ 0, −p mod ℓ for ℓ | a, ℓ ≠ p, possible
as ℓ ≥ 5). Linnik's theorem (effective; exponent 5 by Xylouris 2011) gives q*(n) ≪ (8 rad n)^5, so
**e*(n) ≪ rad(n)^5 ≤ n^5 for every odd n > 1, with an effectively computable implied constant.**
(c) *Under GRH* for ζ_L: Bach–Sorenson (*Math. Comp.* 65 (1996); as recalled: a prime with prescribed Frobenius and
norm ≤ (4 log d_L + 2.5[L:ℚ] + 5)², to be checked against the paper) gives for squarefree n
q*(n) ≤ (16 log n + 4·16 log 2 + 25)² ≤ (16 log n + 70)², so **e*(n) ≤ (16 log n + 70)² under GRH** — explicit,
slightly sharper than CAP_INTERPOLATION Thm 4.2(a) (C_ε(log p)^{2+ε}), and with no Artin/Hooley step.
*Proof.* Thm 1.1 / Cor 1.2 with the cited bounds. ∎

**Remark 1.4 (how B6 and B3 are evaded; Assessment).** B6 (averages over p say nothing at a single p) is evaded
because nothing is averaged: the existence of the window q is a Chebotarev statement in a field of conductor ≍ n
(one prime suffices), and the existence of Q is a deterministic group-theoretic consequence of a Legendre-symbol
identity (parity of the 2-part of a cyclic group). B3 (scale constraint for e = 0 main terms) is evaded because the
certificate is not counted at all; the price is paid in the exponent budget, a_s up to ord_q(s). B2 is visible: the
modulus g = (n + 4Q²)/q is astronomically large (≈ n·Q²/q) and depends on the solution; the cofactor q is small.
EXPONENT_CAP Thm 2.1 (rigidity, g ≤ 2nQ₁²(n + Q₁²)) is respected: Q₁ is of size up to K^{O(q)}.

**Remark 1.5 (relation to known material; Assessment).** The window computation is POINTWISE_SIZE Cor 8.3(b) and
LITERATURE_2026 (vii) "test case" (q = 4x − p a prime non-residue, x = (p+q)/4: −x ∈ ⟨primes of x⟩ mod q needs only
−1 ∈ ⟨primes of x⟩). What is new here is the observation that the exponent cap of EXPONENT_CAP Def 1.1 is exactly the
relaxation of that window's exponent budget, so the subgroup-level success — which is forced — is already an
ES^{(y,e)} solution with e < q. This answers CAP_INTERPOLATION's "unconditionally no bound on e*(n) in terms of n is
known" with a polynomial bound, and with an explicit (log n)² bound under GRH.
