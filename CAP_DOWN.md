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
W_η := ∏ f_χ^{a_χ}. Then the least prime q ∤ f with ξ(q) ≠ 0 is ≪_{n,ε,L} W^{1/4} f^ε (ineffective: Siegel, p. 19 of
the PDF). First screen: the O236 window class is (χ₋₄, χ_{±8}, χ_{n₀})(q) = (−1, −1, −1), a single Frobenius class
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
