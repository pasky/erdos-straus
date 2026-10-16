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

## 1. Bounded windows are dead at every cap (conditional), via a Jacobi transfer

**Lemma 1.1 (Jacobi transfer; PROVED, elementary).** Let p ≡ 1 (mod 4) be prime, m ≡ 3 (mod 4) positive with p ∤ m,
K = (p + m)/4. Then (Jacobi symbols mod m):
(a) (s/m) = (s/p) for every odd prime s | K; (b) (2/m) = (2/p) if K is even; (c) (p/m) = (m/p); (d) (−1/m) = −1.
*Proof.* s | K and s | m would give s | 4K − m = p; so s ∤ m, and s ≠ p (else p | m). (a) Reciprocity for coprime odd
positive s, m with (m−1)/2 odd: (s/m) = (−1)^{(s−1)/2}(m/s) = (−m/s); 4K = p + m gives −m ≡ p (mod s), so (s/m) =
(p/s) = (s/p). (b) 8 | p + m, so m ≡ −p (mod 8), and (2/·) is even under x ↦ −x mod 8. (c) Jacobi reciprocity,
p ≡ 1 (4). (d) m ≡ 3 (4). ∎
**Corollary 1.2 (parity law; PROVED).** Every window certificate satisfies
`  ∏_{s | 2K} (s/p)^{δ_s} · (m/p)^{δ_p} = −1`
(take Jacobi symbols mod m of ∏ s^{δ_s} ≡ −1). So it puts an odd total exponent on {primes of 2K that are
non-residues mod p} ∪ {p, if (m/p) = −1}. (At δ_p = 0 this is CAP_POINTWISE's forcing read backwards, and at odd
squares it is CAP_DOWN §3's T1 argument.)

**Theorem 1.3 (bounded windows fail at every cap, infinitely often; CONDITIONAL on Dickson's prime k-tuples
conjecture).** For every M ≥ 3 there are infinitely many primes p ≡ 1 (mod 8) for which no window m ≤ M carries a
certificate at any cap (e = ∞ included). Equivalently, every ES^{(y)} solution of 4/p with p ∤ x has x > (p + M)/4.
*Proof.* Let Λ := lcm(1, …, M + 1) and L := 16·Λ·∏_{ℓ ≤ M+1} ℓ, so v_ℓ(L) ≥ v_ℓ(m + 1) + 1 for every prime ℓ ≤ M + 1
and v₂(L) ≥ v₂(m + 1) + 2, for every m ≤ M. For each window m ≤ M, m ≡ 3 (4), put L_m := L/(m + 1) and consider the
linear forms f(t) = Lt + 1 and f_m(t) = L_m t + 1. They are distinct and the family is admissible: for ℓ ≤ M + 1 every
form is ≡ 1 (mod ℓ) (ℓ | L_m); for ℓ > M + 1 the ≤ M/4 + 1 < ℓ forms have at most one root each. Dickson gives
infinitely many t with p := f(t) and all R_m := f_m(t) prime. Fix such t. Then p ≡ 1 (mod 8) and p + m = (m + 1)R_m,
so K_m = ((m + 1)/4)·R_m, R_m > M + 1 is prime, and gcd(m, p) = 1 (p ≡ 1 (mod m)), K_m < p. Symbols mod p of all
generators: every prime ℓ ≤ M + 1 has (ℓ/p) = 1 (p ≡ 1 (mod 8ℓ)); this covers 2, the primes of (m + 1)/4, and the
primes of m, so (m/p) = 1. For R_m: R_m ≡ 1 (mod 4) and R_m ≡ 1 (mod m) (all primes of m divide L_m), and
p = (m + 1)(R_m − 1) + 1 ≡ −m (mod R_m), so (R_m/p) = (p/R_m) = (−m/R_m) = (m/R_m) = (R_m/m) = 1. Hence the left side
of Corollary 1.2 is +1 for every exponent vector: no certificate exists at window m, at any cap. The windows of
ES^{(y)} solutions with p ∤ x are exactly m = 4x − p (CAP_DOWN Lemma 3.1; x > p/4 always). ∎
*Remarks.* (1) Scope: Lemma 3.1's full family (δ_p ≠ 0 included); Type I (p | x) is not covered. CAP_INTERPOLATION
Prop 4.1 (Linnik) and redteam-automorphic-2 Thm 2.2(iii) are the cap-limited / cap-0 analogues for covering
arguments; the point here is "every cap, e = ∞ included, and every exponent vector": for these p the window
picture is literally that of n = 1 (K_m ≡ (m + 1)/4 on all small primes, R_m ≡ 1 (mod m)). (2) Unconditionally the
same computation shows: if p ≡ 1 (mod L), a certificate at window m ≤ M must put an odd exponent on a prime factor of
the rough part R_m := K_m/((m+1)/4) that is a non-residue mod p. (3) Consequence for goal (A): a proof of e*(p) ≤ C
must, for some p, use windows m → ∞ together with non-residue primes from the rough part of K_m — at a single prime
window the worst case over K is exactly the forced level (q − 3)/4 (CAP_DOWN Prop 4.1(a)). That is the B2 lottery.
