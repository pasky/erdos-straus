# Z58_TRYF2 — tryhard lane F2: "some p+u has a divisor ≡ −1 (mod 4u)"

Lane: TRYF2 (wave z58). Fresh, unprimed attack per `z52bbriefs/z55_tryhard.md` (z55→z58). Only external data used:
`data/z58/screens/`. Scripts: `scripts/z58_tryf2_*`; data: `data/z58/tryf2/`.

**Status line (updated at every commit):** NO PROOF of the target; no HOT LEAD. Deliverable: the exact split
R(p) = M₂(p) + E₂(p) (§3) with **Theorem A (PROVED): M₂(p) ≥ c₀ log² p for all large primes p ≡ 1 (4)**, M₂ ≡ 0 at
squares, and the open core isolated as the single inequality E₂(p) > −M₂(p) (shown to be non-local, Prop. 2.1, and
not sub-family-stable, §4(b)/F2). Everything below is labelled PROVED / CONDITIONAL / CERTIFIED /
CONDITIONAL. No HOT LEAD yet.

Notation. For n ≡ 1 (mod 4) put R(n) := #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n} = #{(u,d) : u ≥ 1, d | n+u, d ≡ −1 (mod 4u)}
(matches `scripts/z58_screens_rstar.c`). The target is R(p) ≥ 1 for all large primes p ≡ 1 (24).

## §0 Falsifier behaviour of the line of attack (first commit; re-stated in §9)

The line of attack (§1–§4) is: (i) rewrite R(p) in three equivalent ways that expose where primality enters,
(ii) prove that *no* argument using only finitely many congruence conditions on p can work, (iii) isolate the
exact "non-local" statement that must be proved, (iv) try to prove it by exploiting the Jacobi identity
(d/p) = (−C/d) for d | 4pC+1 and a square-corrected main term.

* (F1) odd squares n = m². The Jacobi identity (§1, Lemma 1.3) gives (d/n) = (−C/d) for every divisor d of
  4nC+1 coprime to n; for n = m² the left side is +1 while d ≡ −1 (mod 4C) forces (−C/d) = −1, so R(m²) = 0.
  The square-corrected main term of §4 is Σ_C [τ(4nC+1) − r_{χ_n}(4nC+1)]/φ(4C), which vanishes *termwise* at
  n = m² (χ_n trivial ⇒ r_{χ_n} = τ). So the step that must use non-squareness is: "χ_n is a non-principal character,
  hence Σ_C r_{χ_n}(4nC+1)/φ(4C) = o(Σ_C τ(4nC+1)/φ(4C))". Identifiable, and it genuinely fails at squares.
* (F2) C even only. Nothing in §1–§3 distinguishes C even from C odd; the main term of §4 restricted to C even is
  exactly half the full one. So the line is only *compatible* with F2 if the final inequality is quantitative with
  a constant that does not survive halving the main term — i.e. an argument of the form "main − |error| > 0" where
  |error| is not o(main). Any claimed proof in this lane that does not have such a quantitative step is wrong by F2.
  (As of this commit there is no such step; see status line.)
* (F3) 285 composite non-squares n ≤ 8·10⁶ with R(n) = 0. The line uses nothing about primality beyond
  non-squareness, so it can at best prove the statement for all large non-square n ≡ 1 (4); F3 is then consistent
  only because "large" must exceed 8·10⁶ — i.e. any argument must be explicitly asymptotic with an effective threshold.
* (F4) 14 prime zeros 409 … 8 813 281. Same remark: the threshold must exceed 8.8·10⁶; a "for all p > 10¹⁰" claim
  would need an explicit error term.

Conclusion of §0: the line can only succeed as a quantitative asymptotic argument with an error term that is
provably < main term for every individual large non-square n. §2–§3 show precisely which range of (u,d) that
error term must control.

## §1 Equivalent forms of a hit (all PROVED, elementary)

Throughout n ≡ 1 (mod 4) is a positive integer (n = p prime in the target), and a *hit* is a triple (u,B,C) ∈ ℕ³ with
4uBC − u − B = n. Put d := 4uC − 1, N_C := 4nC + 1.

**Lemma 1.1 (five faces of a hit).** The following sets are in explicit bijection:
(a) {(u,B,C) : 4uBC − u − B = n};
(b) {(u,d) : u ≥ 1, d ≡ −1 (mod 4u), d | n+u} via d = 4uC−1, B = (n+u)/d;
(c) {(u,B) : 4uB | n+u+B} (symmetric in u ↔ B) via C = (n+u+B)/(4uB);
(d) {(C,d) : d | 4nC+1, d ≡ −1 (mod 4C)} via (4uC−1)(4BC−1) = 4nC+1, i.e. the second factor is N_C/d;
(e) {d ≥ 3 odd : r_d | (d+1)/4} where r_d := (−n mod d) ∈ [1,d−1]; here u = r_d, C = (d+1)/(4r_d).
*Proof.* (a)⇔(b): B(4uC−1) = n+u. (a)⇔(c): n+u+B = 4uBC. (a)⇔(d): expand (4uC−1)(4BC−1) = 16C²uB − 4C(u+B) + 1
= 4C(4uBC−u−B) + 1; conversely a divisor d ≡ −1 (4C) of N_C has cofactor N_C/d ≡ d⁻¹ ≡ −1 (4C), so both factors are
of the form 4xC−1. (b)⇔(e): if d | n+u and d ≡ −1 (4u) then u ≤ (d+1)/4 < d, so u = (−n mod d) = r_d and 4u | d+1;
conversely r_d | (d+1)/4 gives u := r_d, C := (d+1)/(4u) ≥ 1, d | n+u. ∎
(Also: with k := (n+r_d)/d, (e) reads "k·d − n = r_d divides (d+1)/4", and (c) reads "4r_d·k | n + r_d + k".)

**Remark 1.2 (continued-fraction face).** For u,B ≥ 2 the Euclidean algorithm on (n,d) runs n = (B−1)d + (d−u),
d = 1·(d−u) + u, d−u = (4C−2)u + (u−1), u = 1·(u−1) + 1, so n/d has regular continued fraction [B−1; 1, 4C−2, 1, u−1]
and Hirzebruch–Jung expansion n/d = B − 1/(4C − 1/u). Hence R(n) − 2·#{d | n+1 : d ≡ 3 (4)} equals the number of
d < n coprime to n whose canonical regular continued fraction is d/n = [0; a₀, 1, a₂, 1, a₄] with a₄ ≥ 2, or
[0; a₀, 1, a₂, 2] (the case u = 2), with a₂ ≡ 2 (mod 4). (The subtracted term counts the hits with u = 1 or B = 1.)
PROVED by the four displayed divisions and uniqueness of canonical expansions; verified for all n ≡ 1 (4), n < 3000
by `scripts/z58_tryf2_cf_check.py` (0 mismatches). This face is recorded because it puts the problem into the
Gauss–Kuzmin/Kloosterman framework for fractions with fixed denominator n; §4 explains why that framework still
cannot see a set of size log² n.

**Lemma 1.3 (Jacobi identity; the square obstruction).** Let n ≡ 1 (4), C ≥ 1, d | 4nC+1, gcd(d,n) = 1. Then
(d/n) = (−C/d) (Jacobi symbols). Consequently: (i) every hit d (face (d)) satisfies (d/n) = −1, i.e. is a quadratic
non-residue "mod n" in the Jacobi sense; (ii) R(m²) = 0 for every odd m; (iii) for n prime, the hit classes
mod 4C lie in the coset O_C := {t ∈ (ℤ/4C)^× : (−C/t) = −1}, which has exactly φ(4C)/2 elements.
*Proof.* 4nC ≡ −1 (mod d) gives −nC ≡ (2⁻¹)² (mod d), so (−nC/d) = 1, i.e. (n/d)(−C/d) = 1. Since n ≡ 1 (4),
quadratic reciprocity for Jacobi symbols gives (n/d) = (d/n). Hence (d/n) = (−C/d). For (i): if d ≡ −1 (mod 4C)
then (−1/d) = −1 (d ≡ 3 mod 4) and (C/d) = 1: for C odd, (C/d) = (d/C)·(−1)^{(C−1)(d−1)/4} = (−1/C)·(−1)^{(C−1)/2} = 1
(as d ≡ 3 mod 4 and d ≡ −1 mod C); for C = 2^a C' with C' odd, d ≡ −1 (mod 8) gives (2/d) = 1 and the odd part as
before. So (−C/d) = −1. (ii): for n = m², (d/n) = (d/m)² = 1 for gcd(d,m) = 1, contradicting (i); and a hit d has
gcd(d,n) = 1 because d | n+u with 1 ≤ u < d. (iii): t ↦ (−C/t) on odd t coprime to C is a character mod 4C, nontrivial
because −C < 0 is not a square; its kernel has index 2. ∎
Numerically verified (`scripts/z58_tryf2_jacobi_check.py`): identity holds for all 40 000+ pairs (C ≤ 400, d | 4nC+1)
at n ∈ {5, 13, 409, 577, 841, 1225, 57, 105, 2305, 10009, 9601, 12841}; h_C ≤ m_C (notation of §4) throughout.

So the *only* way non-squareness can enter a proof is through the non-principality of the character (·/n) — every
hit is a Jacobi non-residue, and squares have none.

## §2 No local (finite-congruence) argument can work (PROVED), and how non-local the hits must be (EVIDENCE)

Call a hit (u,B,C) *U-local* if at least two of u, B, C are ≤ U. By Lemma 1.1 the three "two-small" regions are
(u,C ≤ U) [then d ≤ 4U² is small and the hit is the congruence d | n+u], (u,B ≤ U) [the congruence 4uB | n+u+B] and
(B,C ≤ U) [mirror of the first]. Whether n has a U-local hit depends only on n modulo
L_U := lcm{4uC−1, 4uB : u,B,C ≤ U}.

**Proposition 2.1.** For every U ≥ 1 there are infinitely many primes p ≡ 1 (mod 840) (hence p ∈ 𝔐) with no U-local
hit; indeed every prime p ≡ 1 (mod 840·L_U) has none. In particular, there are infinitely many primes all of whose
hits have at least two coordinates ≥ c·√(log p) (c > 0 absolute).
*Proof.* p ≡ 1 (mod 4uC−1) means p + u ≡ 1 + u ≢ 0 (mod 4uC−1) as 1 ≤ 1+u < 4uC−1 (u,C ≥ 1 except u = C = 1, where
1+u = 2 ≢ 0 mod 3); p ≡ 1 (mod 4uB) means p+u+B ≡ 1+u+B ≢ 0 (mod 4uB) since 1 ≤ 1+u+B < 4uB. Dirichlet gives
infinitely many such primes. For the last clause note L_U ≤ (4U²)^{U²}·(4U²)^{U²} = exp(O(U² log U)), so by Linnik's
theorem there is such a prime ≤ L_U^{O(1)}, i.e. U ≍ √(log p / log log p) is admissible; √(log p) up to the
log log factor. ∎
(Any proof must therefore use hits in which two of (u,B,C) are unbounded — equivalently, by Lemma 1.1(b), a divisor
d of p+u with both d and (p+u)/d unbounded, in the exact class −1 (mod 4u). "Polynomial identity" approaches are dead
on arrival for the target classes; this is the formal content of F1.)

**Data 2.2 (EVIDENCE, `scripts/z58_tryf2_lambda.c`, `data/z58/tryf2/lambda_4e6.txt`).** Λ(p) := min over hits of the
second-smallest coordinate. Over primes p ≡ 1 (4), p ≤ 4·10⁶: Λ ≤ 2 for 62 %, but 769 primes have Λ ≥ 20 and the
maximum is Λ(764 017) = 143, Λ(1 265 617) = 135, Λ(427 249) = 131. No 𝔐-prime has Λ ≤ 2 (they are all ≡ 1 mod 3,
mod 8 and QR mod 5, 7, so u = 1,2 cannot work). Sub-family zero counts for primes ≤ 2·10⁶
(`data/z58/tryf2/subfam_2e6.txt`): full R: 12 zeros (the F4 list ≤ 2·10⁶); hits with d prime: 117 zeros; u,C ≤ 8:
4266 zeros; u,B ≤ 8: all 4519 𝔐-primes are zeros (local, as predicted); C = 1: 17 597 zeros; u = 1: 9308 zeros;
"middle" hits with d, B ≥ n^{1/4}: 31 zeros; C even: 518 zeros.

## §3 Decomposition R = M₂ + E₂ and the provable half (Theorem A)

Fix n ≡ 1 (4) and C ≥ 1; N_C = 4nC+1 is odd, every divisor is coprime to 2. Define
  h_C := #{d | N_C : d ≡ −1 (mod 4C)}  (so R(n) = Σ_C h_C, the sum is finite: C ≤ (n+2)/4),
  m_C := #{d | N_C : (d/n) = −1},    m₂,C := #{d | N_C : 4C−1 ≤ d < √N_C, (d/n) = −1}.
By Lemma 1.3, hits pair up (d ↔ N_C/d, both ≡ −1 mod 4C), every hit has (d/n) = −1, and no d < 4C−1 can hit. If the
pair-representatives d < √N_C with (d/n) = −1 and d ≥ 4C−1 were uniformly distributed over the φ(4C)/2 classes of
O_C, the expected value of h_C would be 2·m₂,C/(φ(4C)/2). Define accordingly
  **M₂(n) := Σ_C 4·m₂,C/φ(4C),   E₂(n) := R(n) − M₂(n).**
M₂(m²) = 0 for every odd m (no d has (d/m²) = −1). E₂ is the aggregate deviation of the exact class −1 from the
coset average.

**Theorem A (PROVED below).** There are absolute constants c₀ > 0, p₀ such that for every prime p ≡ 1 (mod 4), p ≥ p₀:
  M₂(p) ≥ c₀ log² p.
(With the proof's choices, c₀ = 1/300 works for p ≥ p₀(ε) with ε = 1/10; no attempt at optimisation.)

Hence R(p) ≥ 1 for all large primes **⇐** E₂(p) > −M₂(p), i.e. the exact class −1 receives at least a positive
fraction (any fraction > 0, uniformly) of its coset-average share, summed over C ≤ (p+2)/4. This is the whole open
content; §4 explains why it is invisible to exponential-sum methods and why F2 shows it is not sub-family-stable.

### Proof of Theorem A
Fix ε ∈ (0, 1/10]. All implied constants are absolute. Write χ := (·/p) (a non-principal real character mod p).

*Step 1 (the counted pairs).* For X ≥ 1 and D ≥ 1 let
  S(X,D) := #{(C,d) : X ≤ C < 2X, D < d ≤ 2D, d | 4pC+1, χ(d) = −1}.
If D ≥ 8X and 2D ≤ √(4pX), then every (C,d) counted satisfies d ≥ 8X > 4C−1 and d ≤ 2D ≤ √(4pC+1), so (C,d)
contributes to m₂,C; also φ(4C) ≤ 4C < 8X. Therefore
  M₂(p) ≥ Σ_{(X,D)} S(X,D)·(4/(8X)) = Σ_{(X,D)} S(X,D)/(2X),                                              (3.1)
the sum over any family of pairwise disjoint boxes [X,2X)×(D,2D] with 8X ≤ D and D ≤ √(pX) (then 2D ≤ 2√(pX) ≤ √(4pX)).

*Step 2 (one box).* Let X ≥ p^{1/2+ε}, 8X ≤ D ≤ √(pX) (so D ≤ p/8 < p). For odd d ∈ (D,2D], gcd(d,4p) = 1 (d < p), let
c_d := (−\overline{4p} mod d) ∈ [1,d−1], the unique C mod d with d | 4pC+1. Since 2X ≤ D/4 < d, the C ∈ [X,2X) with
d | 4pC+1 is unique and exists iff c_d ∈ [X,2X). Hence
  S(X,D) = #{d ∈ (D,2D] odd : χ(d) = −1, c_d ∈ [X,2X)}.
Put η := p^{−ε/4} and cut (D,2D] into K ≤ 1 + (log 2)/log(1+η) ≤ 2/η blocks B_j = (D_j, D_j(1+η)]. For d ∈ B_j,
[X/D_j, 2X/(D_j(1+η))) ⊆ [X/d, 2X/d), so with I_j := [X/D_j, 2X/(D_j(1+η))) (length ≥ (X/D_j)(1−2η)),
  S(X,D) ≥ Σ_j #{d ∈ B_j odd : χ(d) = −1, {ξ_d} ∈ I_j},   ξ_d := −\overline{4p}/d  (mod 1),  {ξ_d} = c_d/d.   (3.2)

*Step 3 (reciprocity).* For gcd(a,b) = 1, a\bar a + b\bar b ≡ 1 (mod ab) (check mod a and mod b), so
\bar a/b + \bar b/a ≡ 1/(ab) (mod 1). With a = 4p, b = d: ξ_d ≡ \bar d/(4p) − 1/(4pd) (mod 1), where \bar d is the
inverse of d mod 4p. Thus e(hξ_d) = e(h\bar d/(4p))·e(−h/(4pd)); the second factor has derivative in d of size
≤ 2πh/(4pd²) ≤ h/(pD²), so its total variation over B_j is ≤ ηD_j·h/(pD²) ≤ h/(pD) ≤ 1 for h ≤ D.

*Step 4 (complete and incomplete sums).* For w ∈ {1, χ} and integers h, k, the complete sum
  T_w(h,k) := Σ_{d mod 4p, gcd(d,4p)=1} w(d)·e((h\bar d + k d)/(4p))
factors by CRT (4p = 4·p, p odd) as a product of a sum mod 4 (absolute value ≤ 2) and a sum mod p of the form
Σ_{d mod p}^{*} w(d) e((h'\bar d + k'd)/p). For w = 1 this is a Kloosterman sum, |K(h',k';p)| ≤ 2√p·gcd(h',k',p)^{1/2}
(Weil); for w = χ it is a Salié sum, |Σ χ(d)e((h'\bar d+k'd)/p)| ≤ 2√p (Salié's explicit evaluation; or Weil–Deligne
for twisted Kloosterman sums). Here h' ≡ h·(inverse of 4 mod p)-type units times h, so gcd(h',p) = gcd(h,p) = 1 for
1 ≤ h < p. Hence |T_w(h,k)| ≤ 4√p for 1 ≤ h < p and all k. By completion (write 1_{B}(d) via its discrete Fourier
transform mod 4p: 1_B(d) = (1/4p)Σ_k \hat{1_B}(k)e(−kd/4p) with Σ_k|\hat{1_B}(k)| ≤ 4p·(2 + log(4p))),
  |Σ_{d ∈ B'} w(d)·1_{d odd}·e(h\bar d/(4p))| ≤ 4√p·(2 + log 4p)                                                 (3.3)
for every interval B' ⊂ (0,4p) and 1 ≤ h < p (the condition "d odd, gcd(d,p)=1" is built into the complete sums, and
d < p guarantees gcd(d,p) = 1 for the odd d in B'). By partial summation with Step 3 (total variation ≤ 1 for h ≤ D < p),
  |Σ_{d ∈ B_j odd} w(d) e(hξ_d)| ≤ 2·4√p·(2 + log 4p) ≤ 16√p log p   (p ≥ p₀).                                   (3.4)

*Step 5 (Erdős–Turán on one block).* Let w_d := ½(1 − χ(d))·1_{d odd} ∈ {0,1} (indicator of "odd and χ(d) = −1" for
d < p), W_j := Σ_{d ∈ B_j} w_d. By Pólya–Vinogradov, W_j = ¼ηD_j + O(√p log p) (count odd d in B_j: ½ηD_j + O(1);
subtract ½Σ_{d ∈ B_j odd} χ(d), and Σ_{odd d ∈ B'} χ(d) = Σ_{d∈B'} χ(d) − χ(2)Σ_{d' ∈ B'/2} χ(d') ≪ √p log p).
Since w_d ∈ {0,1}, apply the Erdős–Turán inequality (Montgomery, *Ten Lectures on the Interface between Analytic Number
Theory and Harmonic Analysis*, Ch. 1: for x₁,…,x_N ∈ ℝ/ℤ and any interval I, |#{i: x_i ∈ I} − |I|N| ≤ N/(H+1) +
3Σ_{h≤H} h⁻¹|Σ_i e(hx_i)|) to the sequence (ξ_d)_{d ∈ B_j, w_d = 1} of length W_j: for every H ≥ 1
  #{d ∈ B_j : w_d = 1, {ξ_d} ∈ I_j} ≥ |I_j|·W_j − W_j/(H+1) − 3Σ_{h=1}^{H} (1/h)|Σ_{d∈B_j} w_d e(hξ_d)|.
Each exponential sum is ½(Σ_{odd} e(hξ_d) − Σ_{odd} χ(d)e(hξ_d)) ≤ 16√p log p by (3.4). Take H := ⌈p^{ε/4}·D_j/X⌉ ≤ D
(valid: D_j/X ≤ 2D/X and p^{ε/4}·2D/X ≤ D once X ≥ 2p^{ε/4}). Then
  #{…} ≥ (X/D_j)(1−2η)·W_j − W_j·X p^{−ε/4}/D_j − 48√p·log p·(1 + log H).
With W_j = ¼ηD_j + O(√p log p): the main term is ≥ ¼ηX(1 − 2η − p^{−ε/4}) − O((X/D_j)√p log p), and the error is
O(√p log² p). Since X ≥ p^{1/2+ε} and η = p^{−ε/4}: ¼ηX ≥ ¼p^{1/2+3ε/4}, while the errors are O(p^{1/2}log² p) +
O(p^{1/2+ε−... }·): precisely (X/D_j)√p log p ≤ (1/8)√p log p and √p log² p are both ≤ ηX·p^{−ε/4} for p ≥ p₀(ε).
So #{d ∈ B_j : w_d = 1, {ξ_d} ∈ I_j} ≥ ¼ηX(1 − 4p^{−ε/4}) for every j, and summing over the K ≥ (log 2)/log(1+η) − 1
≥ (log 2)/η − 2 blocks, (3.2) gives
  S(X,D) ≥ ¼X·(log 2)(1 − 5p^{−ε/4}) ≥ X/6     (p ≥ p₀(ε)).                                                  (3.5)

*Step 6 (summing the boxes).* Put Λ := (½−ε)log₂ p and take X_i := 2^i·p^{1/2+ε} for 0 ≤ i ≤ I := ⌊Λ − 6⌋ (so
X_i ≤ p/64), and for each i the dyadic D_{i,j} := 8X_i·2^j, 0 ≤ j ≤ J_i := ⌊log₂(√(p/X_i)/8)⌋ (so D_{i,j} ≤ √(pX_i)).
These boxes are pairwise disjoint and satisfy the hypotheses of Steps 1–5. By (3.1) and (3.5),
M₂(p) ≥ Σ_i Σ_j (X_i/6)/(2X_i) = (1/12)Σ_{i=0}^{I}(J_i + 1). Since log₂(p/X_i) = Λ − i, J_i + 1 ≥ ½(Λ − i) − 3, so
  Σ_{i=0}^{I}(J_i+1) ≥ (I+1)(½Λ − 3) − ¼I(I+1) = (I+1)(½Λ − 3 − ¼I) ≥ (Λ−6)(¼Λ − 3/2) = ¼(Λ − 6)²,
using I ≤ Λ − 6 and I + 1 ≥ Λ − 6. Hence M₂(p) ≥ (Λ − 6)²/48 = ((½−ε)log₂ p − 6)²/48 ≥ c₀ log² p with
c₀ = (½−ε)²/(48 (log 2)²)·(1 − o(1)); for ε = 1/10 this is ≥ 1/300 for p ≥ p₀. ∎

*Where primality was used.* (i) χ = (·/p) is non-principal, so Pólya–Vinogradov makes the QNR weight w_d have positive
density — at n = m² the weight is identically 0 and M₂ = 0; (ii) Weil/Salié bounds for the complete sums mod p with
gcd(h,p) = 1 for h < p. For composite non-square n the same proof goes through with (·/n) (non-principal, conductor ≤ n)
and Weil's bound for composite moduli (extra factor τ(4n)·gcd(h,n)^{1/2}, harmless after Σ_h 1/h), so Theorem A holds for
all large non-square n ≡ 1 (4); this is consistent with F3 (the threshold p₀ is far beyond 8·10⁶).

**Data 3.1 (EVIDENCE, `scripts/z58_tryf2_mterm.c`, `data/z58/tryf2/mterm_*.txt`).** Full-range (C ≤ (n+2)/4) values:
| n | R | M₂ | E₂/M₂ |
|---|---|---|---|
| 409, 577, 5569, 9601, 23929, 83449, 102001 (zeros) | 0 | 2.24, 1.44, 6.24, 6.98, 7.64, 9.94, 6.49† | −1 |
| 57, 105, 2305 (composite zeros) | 0 | 0.00, 0.00, 2.25 | −1 / n.a. |
| 841, 1225, 2209 (squares) | 0 | 0 | n.a. |
| 90 primes ≡ 1 (4) in [10⁵, 1.02·10⁵] | min 4, median ≈ 22 | min 10.4, q10 13.4, median 17.0, q90 24.8, max 39.7 | min −0.63, q10 −0.31, median +0.19, q90 +0.75, max +1.63 |
| 10 868 474 401, 10 156 800 001 (F2 primes), C ≤ 1500, C even only | 0 | 11.1, 15.6 | −1 |
| same, C odd only | 10, 38 | 17.1, 36.6 | −0.41, +0.04 |
(† 102001 with C ≤ √n only; the 14 zeros with C ≤ √n have M₂ = 1.8, 1.1, 4.9, 5.3, 5.5, 7.2, 6.5, 8.4, 10.5, 14.5, 12.5,
14.3, 16.4, 16.3, versus 18–51 for typical primes of the same size.) So the model is centred (median E₂/M₂ ≈ 0.2 with
the crude "uniform on O_C" prediction), the zeros are primes with a *low supply* of hit-capable QNR divisors (M₂ at or
below the 10th percentile) that are additionally unlucky (E₂ = −M₂), and the C-even sub-family shows E₂ = −M₂ on a
sub-family with M₂ ≈ 11–16 at p ≈ 10¹⁰.

## §4 Why E₂ is out of reach of exponential-sum methods, and what F2 says about it

(a) *Scale.* In any box u ~ U, d ~ D (faces (b)/(e)) the expected number of hits is Σ_{u~U} Σ_{d~D, d ≡ −1 (4u)} 1/d ≈
(log 2)²/4 — an O(1) quantity; the total log² n comes from ≈ (log n)²/(2 log² 2) such boxes. Any asymptotic evaluation
of the hit count must therefore carry an error o(1) per box or o(log² n) in aggregate. Exponential-sum methods
(van der Corput for e(hn/d), Weil/Karatsuba for e(h\bar n/d)) have errors ≥ n^{δ} and can only evaluate counts whose main
term is a power of n. This is exactly why Theorem A is provable (the main term S(X,D) ≍ X is power-sized and the 1/C
weight is applied afterwards) and E₂ is not: in E₂ the class condition d ≡ −1 (mod 4C) is imposed *inside* the
divisor count, leaving a polylog main term.
(b) *F2 is a theorem about E₂.* On the sub-family C even, the identical decomposition R₈ = M₂^{even} + E₂^{even} holds,
Theorem A's proof gives M₂^{even}(p) ≫ log² p verbatim (C = 2C′, d | 8pC′+1: run Steps 2–6 with 8p in place of 4p), and the 12 F2
primes have E₂^{even} = −M₂^{even}. So "E₂ > −M₂" is not a per-C, per-parity, or per-sub-family statement; a proof of it
must exploit interactions between different C — e.g. that hits at C and at C′ are not independent — which no identity
in §1 provides. Concretely, for the *same* prime, C ≡ C′ (mod q) couples 4pC+1 and 4pC′+1 only through the common prime
factor q, and q ≡ −1 (mod 4C) and q ≡ −1 (mod 4C′) are incompatible for C′ = C + jq (j ≥ 1). No coupling found.
(c) *Zero-sum view.* For fixed u, "no hit" means the sequence of residues mod 4u of the prime factors of (n+u)/2^a has no
sub-product ≡ −1. Since Ω(n+u) ≤ log₂ n ≪ φ(4u) for u ≫ log n, Davenport-constant arguments can force nothing beyond
u ≪ log n, which is a local range (Prop. 2.1 with U ≍ √(log p) blocks it only partially, but §2's covering remark blocks
any finite-u argument outright).

## §5 Other attacks tried (all dead; recorded so nobody repeats them)

* Polynomial identities in p for 𝔐: impossible (Prop. 2.1 / F1). Identities using one extra datum (a prime q with
  (p/q) = −1): a prime hit d = q requires p ≡ −r (mod q) with r | (q+1)/4, which is a τ((q+1)/4)-element subset of the
  (q−1)/2 non-residues — "QNR" is necessary (Lemma 1.3), far from sufficient (409 ≡ 3 mod 7 is a QNR but not in
  G₇ = {5,6}).
* p = a² + b² (p + 2ab = (a+b)²): needs a divisor of (a+b)² that is ≡ −1 (mod 8ab); only d = 8ab−1 is in range and only
  if a ≥ 5.8b; no control. Unit of norm −1 (x² − py² = −1): the resulting C = y²-type values give 4pC+1 = (2pt±1)²,
  whose divisors never lie in −1 (mod 4C) (checked for d | 2pt±1; the remaining divisors have finite total expectation).
* Descent / Vieta: the surface 4xyz − x − y = p is linear in each variable, so no non-trivial involutions; for fixed C the
  solutions are the factorisations of 4pC+1.
* Fixed-shape sub-families: (u = C), (B = u+1), (k = r+1 in face (e)) all have finite expected count Σ 1/u²; (C = 1),
  (u = 1), (u ≤ U₀) fail on a (log p)^{−α} proportion of primes (data in §2).
* Continued fractions (Remark 1.2): same scale obstruction as (a) of §4.

## §6 Verdict

No proof, no HOT LEAD. The lane's net contribution is the split R = M₂ + E₂ with Theorem A: the square-sensitive main
term M₂(p) ≫ log² p is PROVED for all large primes (and all large non-squares), using exactly the two square-sensitive
inputs available (non-principality of (·/p); Weil/Salié bounds mod p), and all remaining difficulty is the single
inequality E₂(p) > −M₂(p), which (i) cannot be attacked box-by-box or sub-family-wise (F2), (ii) cannot be attacked by
finitely many congruences (Prop. 2.1), and (iii) is numerically a fluctuation of relative size ±1 about 0 with the 14
zeros sitting at the bottom of the M₂ distribution. A HOT LEAD would be any mechanism coupling hits at different C (or
different u) for the same p; none was found.

## §7 Falsifiers, restated at the end

* (F1) squares: M₂(m²) = 0 identically (Lemma 1.3), so Theorem A's conclusion fails at squares exactly because (·/m²)
  is principal; the step "Pólya–Vinogradov gives w_d positive density" is where non-squareness is used. ✔ consistent.
* (F2) C even: the decomposition and Theorem A survive restriction to C even, but the needed inequality E₂ > −M₂ is
  *false* on that sub-family at 12 primes near 10¹⁰ (verified at two of them, M₂^{even} ≈ 11–16 with R₈ = 0). So the
  lane proves nothing that would also prove the false C-even statement; any future proof of E₂ > −M₂ must use the
  full C-range non-additively. ✔ consistent, and it sharpens the falsifier into a statement about E₂.
* (F3) 285 composite zeros ≤ 8·10⁶: Theorem A holds for large non-squares with an ineffective-in-practice threshold
  p₀(ε) ≫ 8·10⁶ (the proof needs p^{ε/4} ≥ 5 log² p-type inequalities); M₂(57) = M₂(105) = 0 exactly (no hit-capable
  QNR divisor at all for such small n), M₂(2305) = 2.25. ✔ consistent.
* (F4) 14 prime zeros: all have E₂ = −M₂ with M₂ ∈ [1.1, 16.4] (C ≤ √p), i.e. they are genuine fluctuations of E₂,
  not contradictions of Theorem A. ✔ consistent.
