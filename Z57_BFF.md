# Z57_BFF — tryhard: R_𝔊*(p) ≥ 1 for every large prime p ≡ 1 (mod 4)

Status: z57 lane BFF (brief `z52bbriefs/z57_lanes.md` "The platform" + §BFO/BFF, rules `z55_tryhard.md`; Fable twin).
Internal; hostile line-by-line check in §6. **ES is OPEN. The target statement is NOT proved here.** Labels: PROVED /
CONDITIONAL / CERTIFIED / EVIDENCE / Assessment. Scripts `scripts/z57_bff_*`, data `data/z57/bff/`.
Definitions from `Z56_FAMDESIGN.md` §0–§1 only: p ≡ 1 (4) prime, (★) solutions (o, e, C) with p = 4oeC − o − e,
𝔊* = {(o, e) : max(o, e)⁴ > min(o, e)·p}, R_𝔊*(p) = 2·#{(★) solutions with (o, e) ∈ 𝔊*}.

## 0. Summary

* **Target: prove R_𝔊*(p) ≥ 1 for all large p ≡ 1 (4). Not achieved.** What is proved is a set of exact
  reformulations that make the target a one-line statement about the residues of p, a sharp localisation of where
  primality enters (and therefore where any proof must use it), and a certified extension of the zero-free range.
* **Theorem 1 (PROVED, elementary; §1).** For d ≡ 3 (mod 4), 3 ≤ d < p, let n_d := d − (p mod d) ∈ [1, d−1] (the least
  positive residue of −p) and C_d := the least positive residue of −(4p)⁻¹ (mod d). Then 4·n_d·C_d ≡ 1 (mod d) always, and
  **HIT(d) :⟺ 4n_d | d + 1 ⟺ 4C_d | d + 1 ⟺ 4·n_d·C_d = d + 1** (the point (n_d, C_d) of the modular hyperbola
  4xy ≡ 1 (mod d) lies on its lowest real branch). Every HIT(d) gives the (★) solution (n_d, (p + n_d)/d, C_d), every
  solution (n, m, C) arises from exactly two d's (4nC − 1 and 4mC − 1), and
  **R_𝔊*(p) ≥ 1 ⟺ some d ≡ 3 (4), d ≤ ⌊p^{3/4}⌋ + 1, has HIT(d) with max(n_d, m)⁴ > min(n_d, m)·p**, m = (p + n_d)/d;
  HIT(d) with d⁴(d + 1) ≤ 4p³ (e.g. d ≤ p^{3/5}) is automatically in 𝔊*.
* **Lemma 1.4 (PROVED; where primality enters).** HIT(d) forces the Jacobi symbols (−n_d/d) = −1, (p/d) = −1 and (with
  p ≡ 1 (4)) (d/p) = −1. Hence R(N) = 0 for every odd square N (T1 audit passes: the target is false at odd squares and
  the only place a proof can use primality is the quadratic character of d modulo p). A hit needs d ∈ QNR(p); for
  D ≥ p^{1/4+ε} Burgess gives #{d ≤ D, d ≡ 3 (4), (d/p) = −1} = D/4 + O(D^{1−δ}), so in the Burgess range this is no
  obstruction, while for D ≤ p^{1/4−ε} nothing excludes "p is a QR modulo every d ≤ D" (the 𝔊* boundary of Thm V is
  exactly this threshold, now seen from the d-side).
* **Where the attack stops (§2; Assessment).** The count H(p; D) = #{d ≤ D, d ≡ 3 (4) : HIT(d)} is a sum over the pairs
  (n, C) of 1[(4nC − 1) | p + n]. Its "expected value" (1/8 + o(1))log²D is the a = 0 term of the additive-character
  expansion; the a ≠ 0 terms are Σ_d d⁻¹Σ_{a≠0} e(ap/d)S_d(a) with S_d(a) = Σ_{n | (d+1)/4} e(an/d). For d ≤ p^{1/3−ε} the
  phase ap/d has derivative ≫ 1 in d, so no exponential-sum method bounds the d-sum (the values p mod d for d ≤ p^{1/3−ε}
  are not controllable at a single p: by CRT any prescription of p mod d for all d ≤ c·log p is realised by some prime);
  for d ≥ p^{1/3} the sum is the number of divisors of the single integers p + n in the class −(p + n) (mod 4n), i.e. B2
  in tied form. Three further routes (fixing a QNR prime ℓ of p, norm-form descriptions of level failures, multiplicative
  links between different d) are shown in §2 to give no pointwise inequality. No weaker pointwise theorem beyond the
  classical identity classes is obtained.
* **CERTIFIED (§3).** An independent exhaustive decider built on Theorem 1 (2.8 s for p ≤ 10⁸) reproduces the 38 𝔊*-zeros
  ≤ 10¹⁰ of `Z56_FAMDESIGN` exactly and extends the search: **no 𝔊*-zero in (10¹⁰, 10¹¹]** (see §3 for the exact range
  run and timings). First-hit statistics: the least d with a 𝔊*-hit has median ≈ p^{0.05}, 99.9 % below p^{0.42}, and
  exhaustive maximum 787 439 ≈ p^{0.705} (p = 231 507 061) on (10⁸, 10⁹].
* **Verdict: narrowed.** The target reduces exactly to the pointwise statement "for some d ≡ 3 (4) below p^{3/4} the
  residue −p mod d divides (d + 1)/4", every proof must pass through (d/p) = −1, and the decisive range is d ≤ p^{1/3}
  where single-p information is unavailable. ES is OPEN.

## 1. Exact reformulations (PROVED)

Throughout p ≡ 1 (mod 4) is prime. Solutions are triples (n, m, C) ∈ ℕ³ with 4nmC − n − m = p; since p is odd, n + m is
odd, so {n, m} = {o, e} and the solution set is the (★) solution set of `Z56_FAMDESIGN` §1 with both orders identified.
Write P = min(n, m), Q = max(n, m); the pair is in 𝔊* iff Q⁴ > P·p.

**Lemma 1.1 (shift form).** The map (n, d) ↦ (n, (p + n)/d, (d + 1)/(4n)) is a bijection from
  {(n, d) ∈ ℕ² : d | p + n, d ≡ −1 (mod 4n)}
onto the set of *ordered* solutions (n, m, C) (both orders of each unordered solution), with inverse
(n, m, C) ↦ (n, 4nC − 1).
*Proof.* If d | p + n and d = 4nC − 1 then m := (p + n)/d satisfies (4nC − 1)m = p + n, i.e. 4nmC − n − m = p.
Conversely for a solution, d := 4nC − 1 ≡ −1 (mod 4n) and d·m = 4nmC − m = p + n. The two maps are inverse. ∎
(So R_𝔊*(p) ≥ 1 ⟺ some n ≥ 1 is such that p + n has a divisor ≡ −1 (mod 4n) whose cofactor m satisfies the 𝔊*
inequality; equivalently p + n has a divisor m ≡ −(p + n) (mod 4n).)

**Lemma 1.2 (defect / hyperbola form).** Let d ≡ 3 (mod 4), 3 ≤ d < p. Put n_d := d − (p mod d) (so 1 ≤ n_d ≤ d − 1,
n_d ≡ −p (mod d), gcd(n_d, d) = gcd(p, d) = 1) and C_d := the least positive residue of −(4p)⁻¹ (mod d). Then:
 (i) 4·n_d·C_d ≡ 1 (mod d), so 4n_dC_d ∈ {d + 1, 2d + 1, 3d + 1, …};
 (ii) the following are equivalent: (a) ∃ n ≥ 1 with d | p + n and d ≡ −1 (mod 4n); (b) 4n_d | d + 1; (c) 4C_d | d + 1;
   (d) 4·n_d·C_d = d + 1; (e) n_d·C_d ≤ (d − 1)/2.
 We write HIT(d) for these. If HIT(d), the solution of Lemma 1.1 is (n_d, (p + n_d)/d, C_d).
*Proof.* (i) 4n_dC_d ≡ 4(−p)(−(4p)⁻¹) = 1 (mod d). (a)⟹(b): d ≡ −1 (mod 4n) gives 4n ≤ d + 1, so n ≤ (d+1)/4 < d; with
d | p + n, n is the least positive residue of −p mod d, i.e. n = n_d, and 4n_d | d + 1. (b)⟹(a): take n = n_d.
(b)⟹(d): put c := (d+1)/(4n_d) ∈ [1, (d+1)/4]; then 4n_dc = d + 1 ≡ 1 (mod d), so c ≡ (4n_d)⁻¹ ≡ (−4p)⁻¹ = −(4p)⁻¹
(mod d); as 1 ≤ c < d, c = C_d. (d)⟹(b) and (d)⟹(c) are trivial; (c)⟹(d): the same argument with the roles of n_d and
C_d exchanged ((d+1)/(4C_d) ≡ (4C_d)⁻¹ ≡ −p ≡ n_d). (d)⟺(e): by (i), 4n_dC_d = d + 1 iff 4n_dC_d < 2d + 1 iff
n_dC_d < d/2 + 1/4 iff n_dC_d ≤ (d − 1)/2 (d odd). ∎

*Remarks.* (1) n_d = k ⟺ d | p + k (k < d); C_d = k ⟺ d | 4kp + 1 (k < d). So HIT(d) with n_d = n, C_d = C is the
statement d | p + n with d = 4nC − 1, i.e. d | 4Cp + 1 with d ≡ −1 (mod 4C): the n-lines and the C-levels of
`Z56_FAMDESIGN` §5 are the two coordinates (n_d, C_d) of the same point on the modular hyperbola 4xy ≡ 1 (mod d).
(2) HIT(d) is invariant under p ↦ (4p)⁻¹ (mod d) (it swaps n_d and C_d).

**Lemma 1.3 (the 𝔊* range in d).** Let (n, m, C) be a solution, P = min(n, m), Q = max(n, m), d_P := 4PC − 1,
d_Q := 4QC − 1. Then d_P·Q = p + P and d_Q·P = p + Q. If (P, Q) ∈ 𝔊* then d_P ≤ ⌊p^{3/4}⌋ + 1. Conversely, if HIT(d)
holds and d⁴(d + 1) ≤ 4p³, then the solution (n_d, m, C_d), m = (p + n_d)/d, lies in 𝔊*. Hence
  **R_𝔊*(p) ≥ 1 ⟺ ∃ d ≡ 3 (4), d ≤ ⌊p^{3/4}⌋ + 1 : HIT(d) and max(n_d, m)⁴ > min(n_d, m)·p**, and
  ∃ d ≡ 3 (4), d ≤ p^{3/5} : HIT(d) ⟹ R_𝔊*(p) ≥ 1.
*Proof.* (4PC − 1)Q = 4PQC − Q = (p + P + Q) − Q = p + P; symmetrically for d_Q. Suppose Q⁴ > Pp.
If P ≤ p^{1/3}: d_P = (p + P)/Q < (p + P)/(Pp)^{1/4} = p^{3/4}P^{−1/4} + P^{3/4}p^{−1/4} ≤ p^{3/4} + 1.
If P > p^{1/3}: d_P = (p + P)/Q ≤ (p + P)/P = p/P + 1 < p^{2/3} + 1. In both cases d_P < p^{3/4} + 1, so
d_P ≤ ⌊p^{3/4}⌋ + 1. Conversely, given HIT(d) with d⁴(d+1) ≤ 4p³: n_d ≤ (d + 1)/4 and m = (p + n_d)/d > p/d, so
m⁴ > p⁴/d⁴ ≥ (d + 1)p/4 ≥ n_d·p; whichever of n_d, m is larger, max(n_d, m)⁴ ≥ m⁴ > n_d·p ≥ min(n_d, m)·p. The equivalence follows: a 𝔊* solution has d_P ≤ ⌊p^{3/4}⌋ + 1 and
HIT(d_P) with n_{d_P} = P (P ≡ −p (mod d_P), 1 ≤ P ≤ (d_P + 1)/4 < d_P), and the displayed condition is 𝔊*-membership
of the solution attached to d. For d ≤ p^{3/5}: d⁴(d + 1) ≤ p^{12/5}(p^{3/5} + 1) ≤ 2p³ ≤ 4p³. ∎
(Numerically checked: the engine `z57_bff_engine.py`, scanning d ≤ ⌊p^{3/4}⌋ + p^{1/12} + 10 and testing membership,
reproduces the z56 F4 = 𝔊* hit counts at 437 + 60 primes ≤ 10¹⁰ with 0 mismatches, `z57_bff_validate.py`.)

**Lemma 1.4 (Jacobi symbols of a hit; the use of primality).** If HIT(d) then, with n = n_d,
  (−n/d) = −1,  (p/d) = −1,  and (since p ≡ 1 (mod 4))  (d/p) = −1.
*Proof.* d = 4nC − 1 with C = C_d, so d ≡ 3 (mod 4) and (−1/d) = −1. Write n = 2^k n′, n′ odd. If k ≥ 1 then 8 | d + 1,
d ≡ 7 (mod 8) and (2/d) = 1; so (n/d) = (n′/d). By Jacobi reciprocity for the odd coprime positive integers n′, d, with
(d − 1)/2 odd: (n′/d) = (d/n′)(−1)^{(n′−1)/2} = (−1/n′)(−1)^{(n′−1)/2} = 1, using d ≡ −1 (mod n′). Hence
(−n/d) = (−1/d)(n/d) = −1. Since p ≡ −n (mod d), (p/d) = (−n/d) = −1. Finally (p/d)(d/p) = (−1)^{(p−1)(d−1)/4} = 1. ∎

**Corollary 1.5 (T1 audit).** For an odd square N = M², no d has HIT(d) (with p replaced by N in Lemma 1.2): HIT(d)
gives gcd(N, d) = gcd(n_d, d) = 1 and (N/d) = (M/d)² = 1, contradicting (N/d) = (−n_d/d) = −1. So R(M²) = 0 for all odd
M (consistent with `Z56_FAMDESIGN` §4.3 controls / `Z55_CROSSO` Cor 1.2). *Any proof of the target must therefore use
(d/p) = −1 for the d it produces; this is the only place primality of p (as opposed to p ≡ 1 (4), p non-square) enters.*

**Lemma 1.6 (level failures as norm-form conditions; PROVED, standard).** Let N_C := 4Cp + 1 (≡ 1 mod 4C). The
C-level has no hit (no d | N_C with d ≡ −1 (mod 4C)) iff no sub-multiset of the prime factors of N_C (with
multiplicity) has product ≡ −1 (mod 4C). In particular: level 1 fails ⟺ 4p + 1 has no prime factor ≡ 3 (4) ⟺
4p + 1 = a² + b² with gcd(a, b) = 1 ⟺ p = t(t + 1) + s² for some integers t, s; level 2 fails ⟺ all prime factors
of 8p + 1 lie in {1, 3} (mod 8) or all lie in {1, 5} (mod 8) ⟺ 8p + 1 = a² + 2b² or a² + b² with gcd(a, b) = 1;
level 3 fails ⟺ 12p + 1 = a² + b² or a² + 3b² primitively. (Proof: a divisor ≡ −1 (mod 4C) of N_C is a sub-multiset
product; for the norm forms use that a² + kb² (k = 1, 2, 3) represents N primitively iff −k is a square modulo N, N odd,
and the class number of the corresponding discriminant is 1. For p = t(t+1) + s²: 4p + 1 = a² + b² with a odd forces
b ≡ 2 (mod 4), b = 2s, and p = ((a−1)/2)((a+1)/2) + s².) The 38 𝔊*-zero primes satisfy all of these (checked,
`z57_bff_levels_check.py`, `data/z57/bff/levels_check.txt`), e.g. 564 661 441 = 23 408·23 409 + 4 087²,
8p + 1 = 60 799² + 2·20 258², 12p + 1 = 82 253² + 3 222².
