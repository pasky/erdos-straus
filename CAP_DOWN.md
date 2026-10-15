# CAP_DOWN — pushing the unconditional pointwise cap e*(n) down (task O237, spark relay Z7)

Status: in progress (O237). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on CAP_POINTWISE (O236, branch side-agent/cap-pointwise: Thm 1.1/1.1′/1.3, Lemma 3.1), EXPONENT_CAP (Def 1.1,
Prop 1.2). Scripts `scripts/z13_*`. Normalisation: ES(n) ⟺ e*(n) = 0 (EXPONENT_CAP Def 1.1: den z = q₀², q₀ odd,
gcd(q₀, n) = 1, rad q₀ | y, v_ℓ(q₀) ≤ e).

## 0. Iteration log

(Z7-1) Goal 1 (q* ≪ n^{1/4+ε}). Literature: Pollack, *Prime splitting in abelian number fields and linear
combinations of Dirichlet characters*, IJNT 10 (2014) 885–903, **Thm 1.4** (read from the author's PDF
pollack-math.net/generalsplit6.pdf): X a finite group of primitive characters, conductor f, exponent | n;
ξ ∈ ℤ[X] with ξ(0) = ±1 (coefficient of the trivial character), length ≤ L; W := max(W_{ξ⁺}, W_{ξ⁻}),
W_η := ∏ f_χ^{a_χ}. Then the least prime q ∤ f with ξ(q) ≠ 0 is ≪_{n,ε,L} W^{1/4} f^ε (ineffective: Siegel, Prop 3.3, printed p. 11). First screen: the O236 window class is (χ₋₄, χ_{±8}, χ_{n₀})(q) = (−1, −1, −1), a single Frobenius class
in a (ℤ/2)³ group; its detector ξ = (1−χ₋₄)(1−χ_{±8})(1−χ_{n₀}) has two characters of conductor ≍ n₀ in each of ξ±,
so W ≍ n₀² and Pollack gives only q* ≪ n₀^{1/2+ε} (already a power improvement over rad(n)⁵). Hypothesis of the
"1/4" obstruction: the accepted Frobenius set is a single class mod 8. The 1/4 exponent needs ξ = (1−χ₋₄)(1−χ_{n₀}),
i.e. the window must fire for **every** prime q ≡ 3 (mod 4) with (q/n) = −1, both classes mod 8. Modification
(§1): the windows with K = (n+q)/4 EVEN, discarded in O236 (K odd was imposed so that Q is odd), fire too once the
general Type II divisor d = 2^{v₂(K)}·Q′² (odd 2-exponent allowed, ≤ 2v₂(K): no 2-adic denominator) replaces the
square shot d = Q². This succeeds for n ≡ 1 (mod 8) (all q ≡ 3 (4) fire) and fails, precisely, for n ≡ 5 (mod 8)
(q ≡ 3 (8) with v₂(n+q) odd is not forced).

## 1. Even windows: the 2-adic repair

**Lemma 1.1 (general Type II window with cap; PROVED, elementary).** Let n be odd, m ≥ 1 with m ≡ −n (mod 4),
gcd(m, n) = 1, K := (n+m)/4, S := {primes s | K} (2 allowed), b_s := v_s(K). Let d = ∏_{s∈S} s^{c_s} with
d ≡ −K (mod m), and suppose (i) gcd(K, n) = 1, (ii) c₂ ≤ 2b₂, (iii) for odd s: c_s ≤ 2b_s or c_s is even. Put
A := (K+d)/m, x := K, y := nA, z := nKA/d. Then 4/n = 1/x + 1/y + 1/z, x, y ∈ ℤ_{>0}, and den z = ∏_{s odd, c_s > 2b_s}
s^{c_s − 2b_s}: an ES^{(y,e)}(n) solution with **e = max_{s odd} (c_s/2 − b_s)⁺**. (d = Q² is CAP_POINTWISE Lemma 3.1.)
*Proof.* 4/n − 1/K = m/(nK) and 1/(nA) + d/(nKA) = (K+d)/(nKA) = m/(nK). For s ∈ S, s ∤ m (else s | n). v_s(A) =
v_s(K+d) = min(b_s, c_s) if b_s ≠ c_s, ≥ b_s if b_s = c_s. So v_s(nKA) − c_s = b_s + v_s(A) − c_s is ≥ 0 if c_s ≤ b_s,
≥ 0 if c_s = b_s, and = 2b_s − c_s if c_s > b_s. Hence the s-part of den z is s^{(c_s − 2b_s)⁺}; for s = 2 it is 1 by
(ii); for odd s it is an even power by (iii); it is prime to n by (i); and s | A (v_s(A) ≥ 1 when b_s, c_s ≥ 1), so
rad den z | y. ∎

**Theorem 1.2 (even windows fire; PROVED).** Let n ≡ 1 (mod 4) be a non-square, q a prime with q ≡ 3 (mod 4), q ∤ n,
(q/n) = −1 (Jacobi), K = (n+q)/4 = 2^t K′ (K′ odd). Suppose **(E) q ≡ 7 (mod 8), or t is even.** Then ES^{(y,e)}(n)
holds with e ≤ q − 3. In particular this holds for **every** such q when n ≡ 1 (mod 8); when n ≡ 5 (mod 8) exactly the
q ≡ 3 (mod 8) with v₂(n+q) odd are excluded.
*Proof.* gcd(K, qn) = 1 as in CAP_POINTWISE Thm 1.1 (s | K, s | n ⇒ s | q; q | K ⇒ q | n). Mod q, 4K ≡ n, so
(K/q) = (n/q) = (q/n) = −1 (reciprocity, n ≡ 1 (4)), and (K′/q) = (2/q)^t·(K/q) = −1 under (E). F_q^* is cyclic of
order 2u, u odd. H := ⟨odd primes of K′⟩ contains the non-residue K′, so −1 ∈ H; −K′ ∈ H is a residue, of odd order o,
so −K′ = h², h := (−K′)^{(o+1)/2} ∈ H. Write h ≡ ∏ s^{a_s} (0 ≤ a_s < ord_q s) and put d := 2^t ∏ s^{2a_s}. Then
d ≡ 2^t·(−K′) = −K (mod q); c₂ = t ≤ 2t; odd exponents are even. Lemma 1.1: e = max (a_s − b_s)⁺ ≤ q − 3. If
n ≡ 1 (8): q ≡ 3 (8) gives n + q ≡ 4 (8), t = 0; q ≡ 7 (8) satisfies (E). If n ≡ 5 (8): q ≡ 7 (8) satisfies (E);
q ≡ 3 (8) gives t ≥ 1 and (E) ⟺ t even. ∎
*Why the excluded case is genuinely not forced:* n ≡ 5, q ≡ 3 (8), t odd: (2/q) = −1, (K′/q) = +1, the forced
non-residue of S is the prime 2 itself, and using it costs a 2-exponent that is uncontrolled (c₂ ≤ 2t is required:
2-adic denominators are not allowed in ES^{(y,e)}). Example of a dead case: K′ prime and −2^j ∉ ⟨K′⟩ for |j| ≤ t.
*T1:* (q/a²) = 1, so no such window exists at an odd square (as in O236).

**Proposition 1.3 (one-prime witness: cap ≤ (q−3)/4; PROVED).** In Thm 1.2 (and in CAP_POINTWISE Thm 1.1) let s be
any odd prime with s | K′, b := v_s(K) odd and (s/q) = −1 (one exists: (K′/q) = −1). Let o := ord_q(s); then o/2 is
odd and s^{o/2} ≡ −1 (mod q). **d := K·s^{o/2}** satisfies Lemma 1.1 with cap e = max(0, (o/2 − b)/2) ≤ (q − 3)/4.
In particular cap 0 (an ES solution) whenever v_s(K) ≥ ord_q(s)/2 for such s (e.g. s ≡ −1 (mod q): the classical
"K has a prime factor ≡ −1 (mod q)").
*Proof.* F_q^* has order 2u, u odd, s is a non-residue, so v₂(o) = 1 and s^{o/2} = −1. d ≡ −K (mod q). Exponents:
c₂ = t; c_{s′} = b_{s′} for s′ ≠ s; c_s = b + o/2, which is even (b, o/2 odd) and exceeds 2b iff o/2 > b, with overflow
(c_s − 2b)/2 = (o/2 − b)/2. Lemma 1.1 applies; o ≤ q − 1, b ≥ 1. ∎
So O236's bound e ≤ q − 3 improves to e ≤ (q−3)/4 with an explicit, discrete-log-free witness.
*Check (`scripts/z13_even_windows.py 1000000`, data/z13_even_windows_1e6.txt; 12 s):* all 39 175 primes p ≡ 1 (4)
≤ 10⁶: at the least Thm-1.2 window q_new(p), both the Thm 1.2 witness (BFS discrete log) and the Prop 1.3 witness
are rebuilt and checked with exact rationals against Def 1.1 (square odd den, rad | y, coprime to p, cap as claimed,
4e ≤ q − 3). Also all 18 633 non-squares n ≤ 2·10⁵, n ≡ 1 (4), all primes ≡ 1 (4) (data/z13_even_windows_all_2e5.txt).
Odd squares: 0 windows. Statistics (EVIDENCE): p ≡ 1 (8): mean least window 13.46 (O236) → 7.62, max 227 → 131;
p ≡ 5 (8): 21.33 → 14.64, max 199 → 191. Max Prop 1.3 cap at q_new: 32 (p ≡ 1 (8)), 47 (p ≡ 5 (8)). For p ≡ 5 (8) the
least prime q ≡ 3 (4) with (q/p) = −1 is in the excluded case for 9161 of 19 623 primes (it is mostly q = 3 with
v₂(p+3) odd).

## 2. Goal 1: power savings for q*(n) via Pollack's detector-form theorem

**Corollary 2.1 (PROVED relative to Pollack IJNT 2014 Thm 1.4; ineffective).** Let n be odd, not a square, all prime
factors ≡ 1 (mod 4) (otherwise e*(n) = 0), n = n₀m² with n₀ > 1 squarefree. For every ε > 0:
(a) if n ≡ 1 (mod 8): **e*(n) ≪_ε n₀^{1/4+ε} ≤ rad(n)^{1/4+ε}**;
(b) if n ≡ 5 (mod 8): **e*(n) ≪_ε n₀^{1/2+ε}**.
(In fact e*(n) ≤ (q−3)/4 for the prime q produced.)
*Proof.* For q ≡ 3 (4) prime, q ∤ n automatically and (q/n) = (q/n₀) = χ_{n₀}(q), χ_{n₀} the primitive quadratic
character of conductor n₀ (n₀ ≡ 1 (4) is a fundamental discriminant). (a) X = {1, χ₋₄, χ_{n₀}, χ_{−4n₀}}, f = 4n₀,
exponent 2, ξ = (1 − χ₋₄)(1 − χ_{n₀}) = 1 + χ_{−4n₀} − χ₋₄ − χ_{n₀}: ξ(0) = 1, length 4, W_{ξ⁺} = W_{ξ⁻} = 4n₀. For q ∤ f,
ξ(q) ≠ 0 ⟺ q ≡ 3 (4) and (q/n₀) = −1; by Thm 1.2 (n ≡ 1 (8): no exclusion) every such q is a window, so
e*(n) < q ≪_ε (4n₀)^{1/4}(4n₀)^ε. (b) X = ⟨χ₋₄, χ₈, χ_{n₀}⟩, f = 8n₀, ξ = (1 − χ₋₄)(1 + χ₈)(1 − χ_{n₀}) detects
q ≡ 7 (8), (q/n₀) = −1 (Thm 1.2 (E) holds); ξ⁺ = 1 + χ₈ + χ_{−4n₀} + χ_{−8n₀}, ξ⁻ = χ₋₄ + χ₋₈ + χ_{n₀} + χ_{8n₀},
W = 256 n₀², W^{1/4} = 4n₀^{1/2}. ∎
*Remarks.* (1) This replaces O236's Linnik exponent 5 by 1/4 (n ≡ 1 (8)) and 1/2 (n ≡ 5 (8)); the price is
ineffectivity (Siegel, inside Pollack's proof). O236's Thm 1.3(a)/(b) remain the effective/explicit statements
for general n — but see Cor 2.2 for primes p ≡ 1 (8) and squares (R242 repair). For prime n, the analytic input of (a)
is stated in the literature: Pollack, *The least prime quadratic nonresidue in a prescribed residue class mod 4*,
J. Number Theory 187 (2018) 403–414, §1: n₃(p) ≤ p^{1/4+o(1)}, ineffective (R242 repair: citation added).
(2) Without the even windows of Thm 1.2, the O236 class (one class mod 8) only gives n₀^{1/2+ε} for both residues:
the 1/4 for n ≡ 1 (8) is exactly the 2-adic repair. (3) *Divisor routes (after R239's simpler route for squares).* If d | n, rad(n/d) | d, then gcd(K_d, n/d) = 1
(K_d is prime to d), so scaling a Thm-1.2 solution for d by k = n/d keeps den z, rad den z | ky, and coprimality to n:
e*(n) ≤ e*_win(d). Hence Cor 2.1 applies with n replaced by any such non-square d (bound in terms of the squarefree
part of d, exponent 1/4 if d ≡ 1 (8)). Odd squares n = a²: d = n/p (p | a) has squarefree part p and d ≡ p (mod 8),
so **e*(a²) ≪_ε p^{1/4+ε} if a has a prime factor p ≡ 1 (8), and ≪_ε p^{1/2+ε} for any p | a otherwise.** Likewise
n ≡ 5 (8) gets exponent 1/4 (in terms of the squarefree part of d) whenever some u | n with rad u | n/u, u ≡ 5 (8),
yields d = n/u non-square. (4) Exponent 1/4
is Burgess's barrier (the method is Burgess + Vinogradov–Linnik); GRH gives (log n)² as before.

**Corollary 2.2 (effective and explicit for primes p ≡ 1 (8) and some squares; PROVED relative to Pollack, JNT 187
(2018), Thm 1; R242 repair).** (a) For every prime p ≡ 1 (mod 8): **e*(p) ≤ (p − 5)/8.** (b) For every odd a with a
prime factor p ≡ 1 (mod 8): **e*(a²) ≤ (p − 5)/8.**
*Proof.* Pollack's Thm 1 (genus theory for discriminant −4p; elementary, effective) gives, for p ≡ 1 (4), a prime
q ≡ 3 (4) with (q/p) = −1 and q ≤ (p+1)/2 (his proof: q divides an odd coefficient a ≤ (p+1)/2 of a reduced form in the
non-principal genus). (a) Thm 1.2 has no exclusion for p ≡ 1 (8), and Prop 1.3 gives e*(p) ≤ (q−3)/4 ≤ (p−5)/8.
(b) d := a²/p is a non-square with squarefree part p, d ≡ 1 (8), (q/d) = (q/p) = −1, q ∤ d; apply (a)'s argument to d
and Remark (3). ∎ (Supersedes O236 Thm 1.3(a)/(b) on these classes.)

(Z7-2) Can (b) reach 1/4? Hypothesis to violate: "bad windows (n ≡ 5, q ≡ 3 (8), v₂(n+q) odd) are dead". Tried:
(i) all D₁ at fixed x (Lemma 3.1 below: includes the c_p ∈ {0, 2} "Type-I-at-x" family −4 ∈ box); (ii) odd prime
powers q^{2j+1} and odd products of bad primes (they do reach v₂ even, but then the window is q^{2j+1} with j up to 3, or a product of three bad
primes, and the available bounds give only n₀^{3/4+ε} or worse — no gain over 1/2);
(iii) n-primes inside D₁. In every variant the forced non-residue of a bad window is the prime 2 itself, and every
use of it needs a 2-exponent ≈ ord_q(2)/2, while c₂ ≤ 2v₂(K) is mandatory (no 2-adic denominators in ES^{(y,e)}).
Detector side: accepting only {q ≡ 7 (8)} ∪ {q ≡ 3 (8), v₂(n+q) even} forces two conductor-n₀ characters into each
of ξ± (W ≥ n₀²; a short-form ξ with max(‖α⁺‖, ‖α⁻‖) ≤ 1 must be 1 ± ψ, whose support is ≥ half of (ℤ/2^k)^*);
equivalently the main-term sum is a character sum of χ_{−4n₀}(a² − 2b²) over a box, i.e. a 2-dim Burgess problem with
nontrivial range only at side ≥ n₀^{1/4} (x ≥ n₀^{1/2}). So (b) stays at 1/2 (Assessment: method barrier, not a proof
of necessity). *Remark:* if 2-adic denominators were allowed (variant ES^{(y,e)}_2 with den z = 4^j q₀²), the
excluded windows would fire too: there q ≡ 3 (8), so 2 is a non-residue, o₂ := ord_q(2) has o₂/2 odd, and
d = K·2^{o₂/2} has c₂ = t + o₂/2 even (t odd), 2-adic den 2^{(o₂/2 − t)⁺}·… of even exponent (R-O237 self-review repair:
only in the excluded case; elsewhere the Thm 1.2 witnesses apply); so (a) would hold for all non-square n in that variant.

## 3. The full fixed-x picture and the cap-0 slice

**Lemma 3.1 (all ES^{(y,e)} solutions with given x; PROVED).** Let n be odd, x ≥ 1 with m := 4x − n > 0,
gcd(m, n) = 1 = gcd(x, n), N := nx. Solutions 4/n = 1/x + 1/y + 1/z (y ∈ ℤ_{>0}, z ∈ ℚ_{>0}) are in bijection with
D₁ ∈ ℤ_{>0}, D₁ ≡ −N (mod m), via y = (N + D₁)/m, z = Ny/D₁ ((my − N)(mz − N) = N²). Such a solution lies in
ES^{(y,e)}(n) iff D₁ = ∏_{s | 2nx} s^{c_s} with c_s ≤ 2v_s(N) for s | 2n, and for odd s | x: c_s ≤ 2v_s(x) or
(c_s even and c_s ≤ 2v_s(x) + 2e).
*Proof.* A prime ℓ of den z divides D₁ and y, so ℓ | my − D₁ = N. The local computation of Lemma 1.1 at s | N with
b := v_s(N): den exponent (c_s − 2b)⁺ (cases c < b, c = b, c > b). It must vanish at s | 2n (den z odd and prime to
n) and be even and ≤ 2e at odd s | x; rad den z | y is automatic (s | y when c_s > b ≥ 1). ∎
*Reading.* Writing D₁ = N·∏ s^{δ_s}: **−1 ≡ ∏_{s | 2nx} s^{δ_s} (mod m)** with |δ_s| ≤ v_s(nx), plus overflow
δ_s ∈ v_s(x) + 2ℤ_{>0} at odd s | x (cap = (δ_s − v_s(x))/2). For n = p prime and e = 0 the δ_p = 0 part is the
campaign's e-slice condition −1 ∈ Σ_m(K) (c_p = 1: p divides both y and z, Type II); δ_p = +1 (c_p = 2) gives p | y, p ∤ z, and δ_p = −1 (c_p = 0) gives
p ∤ y, p | z (R-O237 self-review repair; e.g. n = 5, x = 2, D₁ = 50: y = 20, z = 4). These p-divides-one-of-y,z families
read −4^{∓1}·(box element) ≡ 1 via p ≡ 4x (mod m) and are not touched by the forced parity, which only ever
concerns δ_p = 0 (Lemma 1.1 is the case D₁ = n·d).
**T1 for Lemma 1.1 (PROVED).** At n = a² no window m (any m ≡ 3 (4), coprime to n) has a Lemma-1.1 solution at any
cap: d ≡ −K gives (d/m) = (−1/m)(4K/m) = −(a²/m) = −1, while for every prime s | d (s | K): if s odd, m ≡ −a² (mod s)
so (s/m) = (m/s)(−1)^{(s−1)/2} = 1 ((m−1)/2 odd); if s = 2, K is even and m ≡ −a² ≡ 7 (8), (2/m) = 1. So (d/m) = 1.
Contradiction. (The δ_p ≠ 0 part of Lemma 3.1 is not covered by this argument.)

## 4. Goal 3 (multi-window gluing): the one-prime forced witness does not improve under CRT

**Proposition 4.1 (PROVED, elementary).** (a) At a single forced prime window q the one-prime bound of Prop 1.3 is
sharp: if K = s is an odd prime with ord_q(s) = q − 1 (q > 3), the least Lemma-1.1 cap at q is exactly (q−3)/4.
(b) (R-O237 self-review repair: hypotheses added, formula corrected.) Let m = ∏ q_i^{k_i} be a forced composite window
(CAP_POINTWISE Thm 1.1′) and s | K an odd prime with b := v_s(K) odd and o_i := ord_{q_i^{k_i}}(s) even for every i
(this need not exist: forcing makes K, not one prime of K, a non-residue in every component — e.g. n = 5,
m = 567 = 3⁴·7, K = 11·13). Then the one-prime witness d = K·s^j needs s^j ≡ −1 (mod m), i.e. j an odd multiple of
L := lcm_i(o_i/2), and its least cap is max{0, (L − b)/2} ≥ the corresponding cap max{0, (o_i/2 − b)/2} at each
component modulus q_i^{k_i} with the same K. (Comparison with the separate windows q_i, whose K_i = (n+q_i)/4 differ, is
not claimed.)
*Proof.* (a) S = {s}, b = 1: d = s^c ≡ −s needs s^{c−1} = −1, c − 1 ≡ (q−1)/2 (mod q−1), so c − 1 is odd and ≥ (q−1)/2
(c − 1 ∈ [−1, 1] is impossible for q > 3); c = 1 + (q−1)/2 is even, cap (c − 2)/2 = (q−3)/4. *Check* (`scripts/z13_check_sharp41.py`, 2006 cases q ∈ {11, …, 83}, n prime ≤ 4·10⁵ with K prime primitive mod q):
the exhaustive Lemma-1.1 cap at q equals (q−3)/4 in all. (b) −1 ≡ (−1, …, −1) in
∏ (ℤ/q_i^{k_i})^*; each component has 2-part ℤ/2, so s^j = −1 componentwise iff j ≡ o_i/2 (mod o_i) for all i. ∎
*Reading (Assessment).* The forced mechanism lives entirely in the 2-torsion E = (ℤ/2)^r of (ℤ/m)^*; the overflow
is the *odd* part of a discrete logarithm. Gluing windows (composite m, or several x — impossible anyway: one solution
has one x and K(m) = (n+m)/4 is affine, not multiplicative, in m) acts on E and combines odd orders by lcm. Cancelling
overflow means a short relation ∏ s^{δ_s} = −1 in the odd part, i.e. the lattice/B2 lottery (CAP_POINTWISE Lemma 2.1).
**Where T1/B2 bite.** Cap 0 at window m is −1 ∈ Σ_m(K) with |δ_s| ≤ v_s(K) (Lemma 3.1, δ_n = 0) — B2 with the modulus m
part of the solution; at n = a² no window has a Lemma-1.1 solution at any cap (T1, §3). So any gluing that lowers the
cap must (i) leave the forced 2-torsion level (which is all that is provable pointwise) and (ii) be false at odd
squares on the Type II side — consistent with the fact that only divisor routes (Cor 2.1 Remark 3) reach squares.

## 5. Goal 4 (numerics): exact window caps with the full Lemma 1.1 family

`scripts/z13_window_caps.py N M EMAX VER [all]` computes, for each n, the least Lemma-1.1 cap over ALL windows
m ≤ M, m ≡ 3 (4), gcd(m, n) = 1 = gcd(K, n) (no forcing assumed; K even allowed), and rebuilds the best solution
with exact rationals against Def 1.1 (VER = 1: every n).
* Primes p ≡ 1 (4) ≤ 10⁶ (39 175; data/z13_window_caps_1e6.txt, 1.4 s): **best cap 0 for all**, i.e. a Type II ES
  solution at a window ≤ **63** (record p = 87 481); cap ≤ 1 already at m ≤ 51. (O236's "max 3" was the square-shot
  sub-family d = Q², K odd; the general divisor d of Lemma 1.1 collapses it to 0.)
* All non-square n ≡ 1 (4) ≤ 10⁶ with all prime factors ≡ 1 (4) (87 759; data/z13_window_caps_all_1e6.txt, 7 s):
  cap 0 for all but **n = 3985 = 5·797** (best cap 1, at m = 19; ES(3985) holds via 5 | n — the gcd(K, n) = 1 rule
  removes windows); least cap-0 window ≤ 103.
* Odd squares a² ≤ 10⁶: no window m ≤ 400 with any cap ≤ 3 (T1 of §3, as proved).
* Forced windows only (data/z13_even_windows_1e6.txt): Prop 1.3 cap at the least forced window ≤ 32 (p ≡ 1 (8)),
  ≤ 47 (p ≡ 5 (8)); best Lemma-1.1 cap at that window ≤ 16 / 37.
*Reading (EVIDENCE + Assessment).* "Cap ≤ 1 impossible via windows" never happens below 10⁶ for primes; the window
proxy for e*(p) is just ES's Type II verification with tiny windows. The gap between what is provable pointwise
(cap ≈ ord_q(s)/4 at the least forced window) and the truth (cap 0 at m ≤ 63) is the whole lottery: the forced level
uses one character value; cap 0 needs a short relation among the primes of K mod m (B2/B3). Mordell-hard classes:
not separated by these statistics (O236 found q* only mildly larger there).

## 6. Goal 5 (order 3 over ℤ[ω]): a necessary condition — the TES anchor constant must be self-generated

Setting: SYNTHESIS_SPARKS2 §3 (TES(n): 9/n = ω/x + ω²/y + 2/z; shot Prop 3.1: g | n + 18Q³, g ≡ g₀ = 10 + ω (mod 18),
cofactor E = (n + 18Q³)/g, x = (ωn + E)/9, y = na, a = (g + ω²)/9, z = nxa/Q³).
**Proposition 6.1 (self-mute window at order 3; PROVED, elementary).** Take the cofactor to be a small prime window
E = r (so x = (ωn + r)/9 is fixed by r) and let the mute primes be S := primes of x not above 3 (as in SYNTHESIS_SPARKS2; assume x prime to 3,
else restrict further) (for s | Q, s ∤ 3n: s | a ⟺ s | x, the
TES analogue of "s | K ⟺ g ≡ −1 (mod s)"). Then r | n + 18Q³ with Q ∈ ⟨S⟩ mod r forces
`  Q³ ≡ −ω²x/2 (mod r),   hence   2 ∈ ⟨S⟩·μ₆ (mod r).`
*Proof.* 9x ≡ ωn (mod r) gives n ≡ 9ω²x, so −n/18 ≡ −ω²x/2; Q³ ∈ ⟨S⟩ and x ∈ ⟨S⟩·μ₆ (x is a unit times a product of primes of x; R-O237 self-review repair).
This is only a NECESSARY condition: firing needs −ω²x/2 ∈ ⟨S⟩³. For s | a ⟺ s | x: gr ≡ n (mod s), so s | a ⟺
g ≡ −ω² ⟺ n + ω²r ≡ 0 ⟺ s | ω²(ωn + r) = 9ω²x. ∎
*Reading (Assessment).* In ES the window n + m = 4x and the shot n + 4Q² carry the SAME constant 4, which cancels:
the condition is −K ∈ ⟨S⟩², and only the 2-torsion (−1) must be generated — forced by reciprocity. In TES the window
9x = ωn + r and the shot n + 18Q³ differ by 2ω (μ₃-part harmless if a forced non-cube puts μ₃ in ⟨S⟩), and the
residual constant **2 — the numerator of TES's 2/z, i.e. its tame anchor — must lie in ⟨primes of x⟩·μ₆ (mod r)**. That is not a character value of n (cubic reciprocity sees only the cubic class of 2, constant on the
class of r mod 18, R193), but membership of a fixed element in a self-generated subgroup: a lottery, dead e.g. whenever
x is a prime element with 2 ∉ ⟨x⟩μ₆ (mod r). So within this window shape the self-generated-mute trick has no forced order-3 analogue: the necessary condition is
already a subgroup-membership lottery, and the constant that must be generated is the anchor numerator (other shapes
not examined). In ES the anchor is the real place
(positivity) and the wild partner's constant 4 = 2² is invisible at order 2 — the "degree-2 accident" of (J)19 reappears
here as the reason Thm 1.1 exists at all. (An order-3 variant would need a normalisation whose shot constant equals
the window constant up to μ₃ — e.g. a cube; within the anchor calculus such a normalisation pins inv = 0 (Lagrangian),
i.e. loses T1₃. Assessment, not proved.)

## 7. Verdict (O237 checkpoint 1)

1. **Even windows (Thm 1.2, PROVED):** the O236 restriction "K odd" was unnecessary. The general Type II divisor
   d = 2^{v₂(K)}Q′² keeps the 2-adic denominator trivial, and every prime q ≡ 3 (4) with (q/n) = −1 is a *forced*
   window, except (n ≡ 5, q ≡ 3 (8), v₂(n+q) odd). In the excluded case the forced non-residue is 2 itself, which is
   unusable; (R242 repair) excluded windows are not forced but often still fire (R242 scan, n ≤ 2·10⁵, q ≤ 200:
   36 446 of 37 522 excluded pairs fire at some cap, 1 076 are dead, e.g. n = 5, q = 67).
2. **One-prime witness (Prop 1.3, PROVED):** d = K·s^{ord_q(s)/2} gives cap ≤ (q−3)/4 (was q − 3). It needs no
   discrete logarithm and is sharp at a single window (Prop 4.1(a)).
3. **Power saving (Cor 2.1, PROVED relative to Pollack IJNT 2014 Thm 1.4; ineffective):**
   * e*(n) ≪_ε n₀^{1/4+ε} for non-square n ≡ 1 (8), where n₀ is the squarefree part. O236 had rad(n)^5 (Linnik).
   * e*(n) ≪_ε n₀^{1/2+ε} for n ≡ 5 (8).
   * Odd squares a²: p^{1/4+ε} or p^{1/2+ε} via d = n/p, according to whether p ≡ 1 or 5 (mod 8).
   * The 1/4 exponent for n ≡ 1 (8) is exactly the 2-adic repair. For n ≡ 5 (8), 1/2 is a barrier of the method:
     the problem becomes 2-dim Burgess (Assessment).
4. **Negatives with scope:**
   * Composite/CRT gluing does not improve the one-prime forced witness (Prop 4.1(b)).
   * At order 3, the self-mute window needs the TES anchor constant 2 ∈ ⟨primes of x⟩μ₆ (Prop 6.1). That is a
     subgroup-membership lottery, so there is no forced analogue in that shape.
   * T1 holds for every Lemma-1.1 window at odd squares.
5. **Numerics (EVIDENCE, exact checks):** every prime p ≡ 1 (4) ≤ 10⁶ has a cap-0 (Type II ES) window ≤ 63. Forced
   windows give Prop 1.3 caps ≤ 47. The window proxy for e*(p) is therefore ES's Type II verification. The
   provable/true gap is the odd-part discrete-log lottery (B2/B3).
ES is untouched, and no infinite case of ES is claimed.
