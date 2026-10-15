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
is an ES^{(y,e)}(n) solution with e ≤ max(0, max_s a_s − 1) ≤ q − 3. In particular **e*(n) ≤ q − 3.**
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
g ≡ −1 (mod 4Q^{(e)}), Q^{(e)} = ∏ ℓ^{max(1, v_ℓ(Q) − e)}; with e := max a_s − 1 we have Q^{(e)} = rad Q (if all a_s = 0, Q = 1 and the solution is an ES solution, e = 0). a_s ≤ q − 2. ∎

**Corollary 1.2 (all odd n; PROVED).** For every odd n > 1, e*(n) ≤ q*(n) − 3 (or 0), where:
(a) if some prime ℓ ≡ 3 (4) divides n, e*(n) = 0 (ES(ℓ) by 4/ℓ = 1/((ℓ+1)/4) + 1/(ℓ(ℓ+1)/2) + 1/(ℓ(ℓ+1)/2), scaled);
(b) if n is a non-square with all prime factors ≡ 1 (4), q*(n) := least prime with (i)–(iii) (exists by Dirichlet:
one class mod 8·rad(n), see Thm 1.3(b));
(c) if n = a² (a odd, all primes ≡ 1 (4)), fix a prime p | a and let q*(n) := least prime with (i)–(iii) for p and
additionally q ≢ −p (mod ℓ) for every prime ℓ | a, ℓ ≠ p. Apply Thm 1.1 to p: gcd(K, n) = 1, so q is prime to n,
and 4/n = 1/(kx) + 1/(ky) + 1/(kz) (k = n/p) keeps den(kz) = Q₁², rad Q₁ | ky (Q₁ := the denominator root of the p-solution, built from primes of K, hence prime to n).
*T1 check.* For n = a², (q/n) = 1 for every q ∤ n, so condition (iii) is never met at n itself: Thm 1.1 never fires at
an odd square (consistent with T1 / FROBENIUS_FIRING Thm 4.2(b)); (c) routes through the non-square divisor p.

**Theorem 1.1′ (composite windows; PROVED, elementary).** Thm 1.1 holds verbatim for any positive integer m
(in place of q) with m ≡ 4 − n (mod 8), gcd(m, n) = 1, **every prime factor q_i of m satisfying q_i ≡ 3 (mod 4) and
(q_i/n) = −1**; then e ≤ λ(m) − 2 < m (λ = Carmichael).
*Proof.* K = (n+m)/4 is odd, gcd(K, mn) = 1 as before. G := (ℤ/m)^* = ∏(ℤ/q_i^{k_i})^*, each factor {±1} × (odd
order) since q_i ≡ 3 (4); so G = E × U with E ≅ (ℤ/2)^r the sign part and U = G² of odd order, and an element is a
square iff its image in E is trivial. Image of K in E: (K/q_i) = (n/q_i) (as 4K ≡ n mod q_i) = (q_i/n) = −1 for all i, i.e.
K ↦ (−1, …, −1), the image of −1. Write K = εu (ε ∈ E, u ∈ U) with ε = image of −1; for o := ord(u) (odd),
K^o = ε^o = ε = −1 (as −1 ∈ E is the element (−1, …, −1)). So −1 ∈ H := ⟨S⟩, −K ∈ H ∩ U, and an odd-order element of
H is a square of an element of H: Q² ≡ −K (mod m) with Q ∈ ⟨S⟩. The shot step is unchanged (it used only s | K ⇒
m ≡ −n (mod s), and g ≡ 3 (4)). ∎
*Remark.* The prime factors of m are all ≡ 3 (mod 8) or ≡ 7 (mod 8); m ≡ 4 − n (mod 8) with an odd number of factors
forces at least one prime factor in the class 4 − n mod 8. So the least composite window is never smaller than q*(n);
composite windows add *many more* windows (useful for small e, §3), not a smaller bound.

**Theorem 1.3 (size of q*(n); PROVED relative to the cited theorems).**
(a) *Unconditional, explicit (all non-square n of case (b)).* In case (b) every prime of n is ≡ 1 (4) and q ≡ 3 (4), so q ∤ n
automatically and (q/n) = (q/n₀), n₀ := squarefree part of n, n = n₀f² with n₀ squarefree, n₀ > 1, n₀ ≡ 1 (4) (R-O236 repair 4; (R238 repair) "part", not "kernel" = rad n: (q/325) = (q/13) ≠ (q/65)). So (i)–(iii) say that q is
unramified in L := ℚ(i, √2, √n₀) with one prescribed Frobenius (q mod 8 fixes Frob on ℚ(ζ₈) = ℚ(i, √2); (q/n) = (n/q)
fixes it on √n₀). Conductors of the 8 characters: 1, 4, 8, 8, n₀, 4n₀, 8n₀, 8n₀, so d_L = 2^{16}n₀⁴ ≤ 2^{16}n⁴. Ahn–Kwon (*Ann. Inst.
Fourier* 69 (2019), Thm 1.1, "sans aucune restriction": for Galois L ≠ ℚ and any conjugacy class C there is an
unramified prime with Frobenius C and norm ≤ d_L^{12577}) gives q*(n) ≤ (2^{16}n⁴)^{12577}, hence
**e*(n) < 2^{201232}·n^{50308} for every odd non-square n > 1** (and for every odd n with a prime factor ≡ 3 (4),
e*(n) = 0). (R238 repair: Ahn–Kwon Thm 1.1 checked by R238 against the primary text — "for every finite extension K of ℚ,
every finite Galois extension L (≠ ℚ) of K … there exists a prime ideal p in P(C) [unramified, degree one, Frobenius C]
which satisfies N_{K/ℚ}p ≤ d_L^{A₁} with A₁ = 12577".)
(b) *Unconditional, effective (all odd n > 1).* In cases (b), (c) the conditions are implied by q lying in one
fixed class a mod 8·rad(n) (choose a mod 8; a mod rad(n) coprime to it with (a/n₀) = −1 in case (b), n₀ := squarefree
part of n (R238 repair) — so (q/n) = (q/n₀) = −1 and q ∤ n; in case (c): (a/p) = −1 and a ≢ 0, −p mod ℓ for ℓ | a, ℓ ≠ p, possible
as ℓ ≥ 5). Linnik's theorem (effective; exponent 5 by Xylouris, Dissertation Bonn 2011) gives q*(n) ≪ (8 rad n)^5, so
**e*(n) ≪ rad(n)^5 ≤ n^5 for every odd n > 1, with an effectively computable implied constant.**
(c) *Under GRH* for ζ_L: the least unramified prime with prescribed Frobenius is ≪ (log d_L)² (Lagarias–Montgomery–
Odlyzko, *Invent. Math.* 54 (1979); explicit versions: Oesterlé ≤ 70(log d_L)², Bach–Sorenson *Math. Comp.* 65 (1996)
(4 log d_L + 2.5[L:ℚ] + 5)² — (R238 repair) formula confirmed second-hand (quoted in Ahn–Kwon, AIF 69 (2019) p. 1412: degree-one
prime, GRH for ζ_L); Bach–Sorenson's primary text and theorem number were not accessed). For non-square n of case (b),
log d_L ≤ 4 log n + 16 log 2, so **e*(n) ≪ (log n)² under GRH**, explicitly e*(n) ≤ (16 log n + 70)² with the recalled
Bach–Sorenson constant — slightly sharper than CAP_INTERPOLATION Thm 4.2(a) (C_ε(log p)^{2+ε}), with no Artin/Hooley
step. (Odd squares, case (c): the extra exclusions q ≢ −p (mod ℓ) are not Frobenius conditions in L, so under GRH
only the Linnik-type bound of (b) is claimed there.)
*Proof.* Thm 1.1 / Cor 1.2 with the cited bounds. ∎

**Remark 1.4 (how B6 and B3 are evaded; Assessment).** B6 (averages over p say nothing at a single p) is evaded
because nothing is averaged: the existence of the window q is a Chebotarev statement in a field of conductor ≍ n
(one prime suffices), and the existence of Q is a deterministic group-theoretic consequence of a Legendre-symbol
identity (parity of the 2-part of a cyclic group). B3 (scale constraint for e = 0 main terms) is evaded because the
certificate is not counted at all; the price is paid in the exponent budget, a_s up to ord_q(s). B2 is visible: the
modulus g = (n + 4Q²)/q is astronomically large (= (n + 4Q²)/q ≈ 4Q²/q) and depends on the solution; the cofactor q is small.
EXPONENT_CAP Thm 2.1 (rigidity, g ≤ 2nQ₁²(n + Q₁²)) is respected: Q₁ is of size up to K^{O(q)}.

**Remark 1.5 (relation to known material; Assessment).** The window computation is POINTWISE_SIZE Cor 8.3(b) and
LITERATURE_2026 (vii) "test case" (q = 4x − p a prime non-residue, x = (p+q)/4: −x ∈ ⟨primes of x⟩ mod q needs only
−1 ∈ ⟨primes of x⟩). What is new here is the observation that the exponent cap of EXPONENT_CAP Def 1.1 is exactly the
relaxation of that window's exponent budget, so the subgroup-level success — which is forced — is already an
ES^{(y,e)} solution with e < q. This answers CAP_INTERPOLATION's "unconditionally no bound on e*(n) in terms of n is
known" with a polynomial bound, and with an explicit (log n)² bound under GRH. (R238 repair) Consequence: Thm 1.1 +
Cor 1.2 give ES^{(y)}(n) = ES^{(y,∞)}(n) for every odd n > 1 by an elementary argument, superseding the linear-sieve/BV
(ineffective) proof of FROBENIUS_FIRING Thm 4.2(a),(c). Thm 4.2(b) (T1) is a shape statement and is not contradicted by
Cor 1.2(c): the scaled solution has v_p(x) = 2v_p(a) − 1, not Type I/II shape at every prime of a.

## 2. Goal 2 (GRH, e* ≤ C log log p): where the window method stops

**Lemma 2.1 (the cap below the covering threshold is a divisibility lottery; PROVED, trivial).** For a window m of n,
cap(m) ≤ e ⟺ m | n + 4Q² for some Q ∈ Box_e(K) := {∏ s^{a_s} : a_s ≤ v_s(K) + e}, K = (n+m)/4.
(Since 4K ≡ n (mod m).) For e = 0 this is the *square-shot* ES condition at the window (a sub-case of the Type II window condition, which allows any d | K² with d ≡ −K (mod m)); for e ≥ ord-bound it is automatic (Thm 1.1).
*Reading (Assessment).* Thm 1.1 uses only *subgroup-level* information (a Legendre symbol and cyclicity), which is
Chebotarev-visible and therefore effective/GRH-controllable. Any cap e below the box-covering threshold
(∏_s (v_s(K) + e + 1) ≳ |⟨S⟩| ≍ m for a balanced lattice) asks for m to divide one of the explicit integers
n + 4Q², Q ∈ Box_e(K) — the B2 divisor lottery; no Frobenius/Kummer condition in a fixed field expresses "the
discrete logarithm of −K lies in a box". So a GRH proof of e*(p) ≤ C log log p must certify the *lattice shape*
of Λ_m = ker(ℤ^S → F_m^*) at a window m with |S| ≍ log m/log log m forced primes (those are the s with
m ≡ −n (mod s), a Dirichlet condition of modulus P = ∏S ≈ m^{1/2}).
**Where this covering argument breaks (Assessment, tentative; R-O236 repair 5).** Windows in the class mod P number
≍ X/(P log X) under GRH (X ≥ P²·polylog). Unbalanced lattices (λ₁ ≤ B) occur only at primes dividing one of the
≍ (2B+1)^{|S|} relation numbers ∏s^{c⁺} − ∏s^{c⁻} (each of height O(B log P), so ≪ B^{|S|+1} log P/log X such primes
— the extra factor B as in CAP_INTERPOLATION Thm 4.2); these numbers do not depend on n, but their prime factors are
not known to equidistribute mod P, so the bad count cannot be divided by P. With B^{|S|+1} ≲ X/P, Minkowski II
gives a covering budget λ_{|S|} ≲ X^{2/(|S|+1)}·P^{1−o(1)}, i.e. this *sufficient* covering argument needs cap ≈ P —
the loss behind CAP_INTERPOLATION Thm 4.2(b) (e ≤ exp(O(√(log₂p log₃p)))). The window method reproduces, but does not
improve, that bound. This is a limitation of whole-lattice covering, NOT a necessity theorem: a proof hitting the
single target −K need not certify covering. *Input that would remove the P-loss in this argument:* equidistribution
mod P ≈ X^{1/2} of the primes q ≤ X at which a short multiplicative relation among the first k primes holds
(heuristically true). The C log log p conjecture would further need box side ≍ log X ≍ log₂p in k ≍ log X/log₂X
dimensions. Nothing of this kind is known even under GRH (prime factors of a structured family of integers in
progressions: B6 at level P). *R237 calibration (CAP_INTERPOLATION Remark 3.2):* the almost-all side is stronger than
O234 said — with the full 𝒟_e(ℓ) family the prime-modulus large sieve already gives a power saving at e ≥ (log N)^{1+ε};
so the almost-all/pointwise meeting point is not the log log scale, and pointwise the known bounds are polynomial
(unconditional, Thm 1.3) and (log n)² (GRH) against the (log₂p)^{1−o(1)} covering barrier (CAP_INTERPOLATION Prop 4.1).

## 3. Numerics (goal 3): window caps for all primes p ≡ 1 (mod 4) below 10⁶

**Lemma 3.1 (exact cap of a window shot; PROVED).** In Thm 1.1/1.1′ with Q = ∏ s^{a_s} (actual exponents) and
b_s := v_s(K): the shot solution has den z = Q₁² with v_s(Q₁) = (a_s − b_s)^+, so its cap is max_s (a_s − b_s)^+;
**cap 0 ⟺ Q | K (an ES solution of Type II shape; only the square-shot sub-family d = Q² of the Type II window condition d | K², d ≡ −K (mod m)).**
*Proof.* g + 1 = 4(K + Q²)/m, s ∤ 2m, so σ_s := v_s(g+1) = v_s(K + Q²) = min(b_s, 2a_s) if 2a_s ≠ b_s, and ≥ b_s = 2a_s
if 2a_s = b_s. EXPONENT_CAP Prop 1.2: v_s(Q₁) = (a_s − σ_s)^+, which is 0 if 2a_s ≤ b_s and (a_s − b_s)^+ otherwise. ∎
So the window cap is cap(m) := min{e : −K ∈ {∏ s^{2a_s} : 0 ≤ a_s ≤ b_s + e} mod m}, and e*(n) ≤ min_m cap(m).

`scripts/z12_window_scan.py 1000000 1000 200` (data/z12_window_scan_1e6.txt; 0.5 min): all 39 175 primes
p ≡ 1 (4), p ≤ 10⁶; windows m ≤ 1000 (prime and Thm 1.1′ composite; (R238 repair) allowing every m ≡ 4 − p (8), gcd(m, p) = 1, the best cap
histogram is 0: 34 933, 1: 4184, 2: 57, 3: 1, max still 3, at p = 18 013, m = 271); every 200th prime's solutions rebuilt and
checked with exact rationals against Def 1.1 (756 checks; cap formula of Lemma 3.1 confirmed in all).
* q*(p) (least prime window) exists ≤ 227 for every p; record q* = 227 at p = 867 793 (log²p = 186); max q*/log²p = 2.84 (at p = 4349, q* = 199; also 2.73 at p = 29, 2.70 at p = 5, 2.54 at p = 2221 —
  R-O236 repair 3; the earlier "≤ 1.3" was false) (EVIDENCE that the GRH bound (16 log p + 70)² is very generous; q* behaves like a least
  prime non-residue in a class mod 8).
* Cap at the least window q*: histogram 0: 24 266, 1: 9012, 2: 2448, 3: 912, 4: 699, 5: 998, …, max 41
  (p = 575 717, 589 997; q* = 167). Always ≤ q* − 3 (Thm 1.1; asserted). The guaranteed cap behaves like a discrete
  logarithm: it is large exactly when K has few prime factors.
* Best cap over all windows m ≤ 1000: 0: 32 043, 1: 6887, 2: 238, **3: 7 (max)**; over prime windows only also max 3 (0: 31 850, 1: 7063, 2: 255, 3: 7; R-O236 repair 1: an earlier run searched prime
  windows only up to the composite best and misreported 4 primes, max 5).
  So "e*_win(p) ≤ 3 using windows ≤ 1000" for all p ≤ 10⁶ (EVIDENCE). (True e*(p) = 0 by ES itself; 7132 primes have
  no cap-0 *square-shot* window ≤ 1000; this says nothing about general Type II windows, e.g. p = 241: window m = 11,
  K = 63 has square-shot cap 1 but the general Type II window gives 4/241 = 1/63 + 1/1446 + 1/30366 (checked exactly) —
  R-O236 repair 2.)
* T1 control: no odd square a² ≤ 10⁶ has any window (Cor 1.2 T1 check), as proved.

## 4. Goal 4: Type I shape adds no forced dimension — the window dichotomy

**Proposition 4.1 (Type I windows are not forced; PROVED, elementary).** Let p ≡ 1 (mod 4) be prime, k′ a prime with
a := (pk′ + 1)/4 ∈ ℤ (so k′ ≡ 3 (mod 4)), and consider ES^{(y,e)}(p) solutions of Type I shape x = pa, y = a·w,
z = aw/(k′w − 1) (w ≥ 1; every Type I-shape solution with a | y has this form, as 4/p − 1/(pa) = k′/a).
(R238 repair) (b) holds for every solution with x = pa, without a | y: see the remark after the proof.
(a) For every odd prime s | a: (s/k′) = (s/p). And (a/p) = +1 always (4a ≡ 1 mod p).
(b) If every odd prime s | a has (s/p) = +1, and a is odd or k′ ≡ 7 (mod 8), there is no such solution for any
e ≤ ∞. In particular this happens whenever a is an odd prime.
*Proof.* (a) pk′ ≡ −1 (mod s), so (k′/s) = (−1/s)(p/s); reciprocity with k′ ≡ 3 (4): (s/k′) = (k′/s)(−1/s) = (p/s) = (s/p).
(b) A solution needs D := k′w − 1 = G·q² with G = gcd(D, a), q odd, rad q | a (den z = D/G must be q², and
rad q | y = aw with gcd(q, w) = 1). Then D is a product of primes of a, all squares mod k′ by (a) and the hypothesis
on 2, while D ≡ −1 is not ((−1/k′) = −1). ∎
*(R238 repair) Arbitrary y.* For x = pa and any y, z = ay/D with D = k′y − a > 0. A prime t | D with t ∤ ay would divide
den z but not y, so t | ay; t | y and t | D give t | a; and 2 | D forces 2 | a (den z odd). So D is supported on primes of
a, hence a square mod k′ under (b)'s hypotheses, while D ≡ −a ≡ −4⁻¹ (mod k′) is not. So (b) kills every solution with
x = pa (checked by R238 for all y ≤ 2·10⁴ in the 95 windows: none).
*Check:* `scripts/z12_typeI.py 400 60 20000`: 612 symbol identities (a); in all 95 predicted-empty windows no solution
with w ≤ 2·10⁴; solutions found in 149 of the others.
**Dichotomy (PROVED; reading Assessment).** In a Type II window (x = (n+q)/4) the parity identity is (K/q) = −1:
an *odd* number of prime factors of K are non-residues, which forces −1 ∈ ⟨S⟩ and hence ES^{(y,q)} (Thm 1.1). In a
Type I window (x = pa) the parity identity is (a/p) = +1: an *even* number, possibly zero, so nothing is forced, and
the window can be dead at every cap. The ES sign χ = −1 of the campaign ((J)10, (J)32) is exactly what makes Type II
forced; Type I carries the opposite sign. So the cap opens no free Type I dimension at the subgroup level; Type I's
contribution to ES^{(y,e)} is a genuine lottery (factorisation of (pk′+1)/4 into non-residues mod p), whereas
Type II's subgroup level is free and only its exponent budget is a lottery (Lemma 2.1).
* **Exact verification of Thm 1.1 (EVIDENCE for the code; the theorem is proved):** `z12_window_scan.py 1000000 230 1`
  (data/z12_window_scan_1e6_exact.txt): for every prime p ≡ 1 (4) ≤ 10⁶ the q*-window solution and 127 735 window
  solutions in total rebuilt and checked against Def 1.1 with exact rationals. `z12_selfmute.py 200000`
  (data/z12_selfmute_2e5.txt): all 49 776 odd non-squares n ≡ 1 (4) ≤ 2·10⁵ (composite n included), least window
  ≤ 263, solution verified exactly, cap ≤ 55 at the least window.
* Mordell-hard classes (p mod 840 ∈ {1, 121, 169, 289, 361, 529}; `z12_qstar_hard.py 1000000`): mean q* = 22.7
  (2370 primes, max 139) vs 17.1 elsewhere (36 805 primes, max 227) — q* only feels the small-prime residue pattern
  (3, 7 are residues there), and the overall record is not Mordell-hard. Odd squares: e*(a²) = 0 numerically (ES);
  windows never exist at a² (T1), Cor 1.2(c) routes through a prime p | a.

## 5. Verdict (O236 checkpoint 1)

1. **First unconditional *polynomial* pointwise cap (Thm 1.1, Cor 1.2, Thm 1.3; PROVED, elementary + Linnik/Ahn–Kwon;
   finiteness of e*(n) was FROBENIUS_FIRING Thm 4.2, ineffective; the subgroup mechanism is POINTWISE_SIZE Cor 8.3(b) —
   the new step is connecting it to the overflow dictionary):**
   e*(n) < q*(n) for every odd n > 1, where for non-square n q*(n) is a least prime in one Frobenius class of
   ℚ(i, √2, √n₀) (n₀ the squarefree part), and for odd squares a least prime in one class mod 8·rad(n) (Cor 1.2(c))
   (R238 repair); hence
   e*(n) ≪ rad(n)^5 effectively (Linnik–Xylouris), e*(n) < 2^{201232}n^{50308} explicitly for non-square n (Ahn–Kwon),
   e*(n) ≪ (log n)² under GRH for non-square n (explicit (16 log n + 70)² with the recalled Bach–Sorenson constant). Mechanism: the window
   q = 4x − n generates its own mute set (primes of x); the Legendre identity (x/q) = −1 forces −1 ∈ ⟨primes of x⟩, so
   the window fires at the subgroup level and the cap e absorbs the exponent budget. Deterministic; no averaging (B6
   evaded), no counting (B3 evaded); the shot modulus g is solution-dependent and huge (B2 respected).
2. **Composite windows (Thm 1.1′)** fire under the same sign condition on every prime factor.
3. **Below the covering threshold the cap is a divisor lottery (Lemma 2.1).** GRH ⇒ C log log p is NOT reached by
   the window or fixed-S covering arguments; an input that would remove their P-loss is equidistribution mod P ≈ X^{1/2} of primes carrying a short
   multiplicative relation among the first k primes (§2, Assessment). The window method reproduces but does not
   improve exp(O(√(log₂p log₃p))).
4. **Type I/Type II window dichotomy (Prop 4.1, PROVED):** Type II windows carry the forced parity (K/q) = −1, Type I
   windows (a/p) = +1, so Type I-shape windows are never forced and are dead at every cap whenever (pk′+1)/4 is prime.
5. Numerics (EVIDENCE): all primes p ≤ 10⁶ have q* ≤ 227 (q*/log²p ≤ 2.84); best window cap over m ≤ 1000 is ≤ 3;
   cap at q* ≤ 41. e*(p) itself is 0 (ES).
ES untouched; no infinite case of ES is claimed. The theorem is about ES^{(y,e)} with e ≈ n^{O(1)}, a relaxation
that is far from ES (e = 0).
