# CAP_BOUNDED — a bounded cap for every prime? (task O250)

Status: in progress (O250). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on EXPONENT_CAP ((J)34, Def 1.1), CAP_POINTWISE ((J)64), CAP_DOWN ((J)66: Lemma 1.1, Lemma 3.1, Thm 1.2,
Prop 1.3, Prop 4.1), CAP_INTERPOLATION ((J)63), SYNTHESIS_SPARKS7 ((J)78 §2), BRAINSTORM/z12_grh_lattice_gap,
BRAINSTORM/s7_certified_caps. Scripts `scripts/z22_*`, memos `BRAINSTORM/z22_*.md`.
Normalisation: e*(n) as in CAP_POINTWISE (den z = r², r odd, gcd(r, n) = 1, rad r | y, v_ℓ(r) ≤ e); ES(n) ⟺ e*(n) = 0.
Window notation (CAP_DOWN Lemma 3.1): p prime ≡ 1 (4), window m ≡ 3 (4), gcd(m, p) = 1, K = K_m = (p + m)/4 = x,
b_s = v_s(K). A window certificate is an exponent vector δ on the primes of 2pK with
`  ∏_{s | 2pK} s^{δ_s} ≡ −1 (mod m),  δ_s ∈ [−b_s, b_s] (s | 2K),  δ_p ∈ {−1, 0, 1},  or (odd s | K) δ_s ∈ b_s + 2·[1, e]`
(d = D₁ = pK·∏ s^{δ_s}); its cap is max over odd s of (δ_s − b_s)/2 for δ_s > b_s. Lemma 3.1 = all ES^{(y,e)}
solutions with p ∤ x.

Goal (task): (A) e*(p) ≤ C absolute; or (B) cap 0 on an explicit positive-density Chebotarev set by a forced
mechanism; or (C) e*(p) = O(log p) / O(p^ε) unconditionally.

## 0. Iteration log

(Z22-1) *Brief's idea: a smooth K, or a K divisible by all primes ≤ y.* Choose the window so that K ≡ 0 (mod P(y)),
P(y) = ∏_{s ≤ y} s (q ≡ −p (mod 4P(y))). Counting: the cap-C box over the primes ≤ y has (C+3)^{π(y)} elements, the
group has q ≥ P(y) ≈ e^y elements, so covering needs C ≳ y — independent of p! Barrier hit: the box is then a FIXED
finite set of rationals a/b (independent of p), and "−1 ∈ box mod q" ⟺ q | a + b: a fixed finite set of q, hence a
congruence covering of p mod 4P(y) (B1), which T1 kills at p ≡ 1 (mod 4P(y)): there every s ≤ y is ≡ ±1 … more
precisely q ≡ −1 (mod s) and (s/q) = +1, so no box element is −1. Hypothesis satisfied: "bounded support" (the
certificate uses only primes from a set fixed in advance). → The support must grow with p; §1 makes this a theorem
(conditional, any cap) for bounded windows.
(Z22-2) *Uniform (self-generated) elements.* Use only elements polynomial in K, p, 2 (exponents δ_s = j·b_s on all
odd s | K). Classification (§2): at cap 0 they give only the classical windows m | p + 4, m | (p+1)/2, m | p + 2,
m | 2p + 1; at cap e ≥ 1 the only new relation is K^o ≡ −1, i.e. m | p^o + 4^o (o odd), with cap ≤ b_max(o − 1)/2.
This decouples the cap from the window SIZE (q can be ≈ p^o). Barrier hit: p^o + 4^o ≡ 1 (mod 4) for every p, and at
p = a² it is a sum of two coprime squares — the existence of a prime factor ≡ 3 (mod 4) is a Landau-type event, never
congruence-forced (T1/B5).
