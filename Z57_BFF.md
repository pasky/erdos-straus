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

## 2. The attack and where it stops

### 2.1 The count and its "expected" size (PROVED identity; heuristic size)

By Lemma 1.2, for D ≥ 3 put
  H(p; D) := #{d ≡ 3 (mod 4), 3 ≤ d ≤ D : HIT(d)} = Σ_{n ≥ 1} Σ_{C ≥ 1, 4nC − 1 ≤ D} 1[(4nC − 1) | p + n].
By Lemma 1.3, H(p; p^{3/5}) ≥ 1 ⟹ R_𝔊*(p) ≥ 1, and R_𝔊*(p) ≥ 1 ⟹ H(p; ⌊p^{3/4}⌋ + 1) ≥ 1. Writing
1[d | p + n] = d⁻¹Σ_{a mod d} e(a(p + n)/d) and S_d(a) := Σ_{n | (d+1)/4} e(an/d),
  H(p; D) = Σ_{d ≤ D, d ≡ 3 (4)} τ((d+1)/4)/d  +  Σ_{d ≤ D, d ≡ 3 (4)} d⁻¹ Σ_{a=1}^{d−1} e(ap/d) S_d(a).        (2.1)
The first sum is Σ_{k ≤ (D+1)/4} τ(k)/(4k − 1) = (1/8)log²D + O(log D) (PROVED, elementary); it is the mean of H over p
in the naive model "p mod d uniform". The second sum E(p; D) is an exact function of the residues p mod d, d ≤ D; the
target is E(p; p^{3/5}) > −(1/8)log²p·(1 − o(1)) for every large prime p ≡ 1 (4), or merely H(p; p^{3/4}) ≥ 1.
(The genus main term of `Z56_FAMDESIGN` Thm V is the part of (2.1) that Burgess/Heath-Brown can evaluate at every p; its
value (5/(4π²))log²p counts both orders over all of 𝔊*, while (1/8)log²(p^{3/4}) = 0.0703 log²p counts each 𝔊* solution
via d_P (and some corner solutions); the two bookkeepings agree in size: 0.0703 ≈ 0.0633 + corner share.)

### 2.2 Why the d-sum cannot be bounded at a single p (Assessment, with the computations)

* **d ≤ p^{1/3−ε}.** For fixed a ≠ 0, Σ_{d ~ D} e(ap/d) has phase derivative ap/d² ≥ p^{1/3+2ε} ≫ 1; the van der
  Corput / exponent-pair bounds give (ap/D)^{1/2} + (D³/ap)^{1/2}, which exceeds D for D < (ap)^{1/3}. There is no
  cancellation to be had, and in fact none exists in general: by the Chinese remainder theorem and Dirichlet's theorem
  any prescription of the residues p mod d for all d ≤ D₀ (modulus lcm(1..D₀) = e^{(1+o(1))D₀}) is realised by primes
  p ≍ e^{(1+o(1))D₀}, so for D₀ ≤ (1 − ε)·log p there are primes with H(p; D₀) = 0 and (2.1) is uninformative. Between
  log p and p^{1/4} the only known single-p information is quadratic (Burgess: (d/p) is −1 for ~half of the d ≥ p^{1/4+ε});
  Lemma 1.4 shows this is necessary for a hit but it is far from sufficient (HIT(d) has probability ≈ 2τ((d+1)/4)/φ(d)
  among d ∈ QNR(p)).
* **p^{1/3} ≤ d ≤ p^{3/4}.** Here one can sum e(ap/(4nC − 1)) over C for fixed small n and a, but the a-sum runs over
  all residues mod d; grouping by n instead, Σ_C 1[(4nC − 1) | p + n] is the number of divisors of the single integer
  p + n in the class −1 (mod 4n) and size range [p^{1/3}, p^{3/4}], equivalently of its divisors m ≡ −(p + n) (mod 4n) in
  [p^{1/4}, p^{2/3}]. No method evaluates the divisor function of one integer in a residue class; this is B2 in tied form
  (`Z56_FAMDESIGN` §5 item 1).
* **Fixing a quadratic non-residue.** Let ℓ be the least prime with (p/ℓ) = −1 (ℓ ≤ p^{1/(4√e)+ε} by Burgess; ℓ ≥ 5 at
  every 𝔊*-zero, and ℓ ∈ {5, …, 29} at the 38 of them, `data/z57/bff` via `z57_bff_zeros_local.py`). The d with
  (d/p) = −1 include all d = ℓk with (k/p) = +1, but HIT(ℓk) ⟺ 4n_{ℓk} | ℓk + 1 is again a divisibility of a residue of p
  by a structure of k; the knowledge of ℓ removes an obstruction (Lemma 1.4) and provides nothing positive.
* **Norm forms (Lemma 1.6).** Failure of levels C ≤ K means that the K integers C(4p + 1) − (C − 1) all lie in thin
  multiplicative sets (density (log)^{−1/2} or thinner). This is the Elsholtz–Tao-type sieve input and yields "almost
  all p" with a quantitative exceptional set (dimension ≍ K/2, so exceptional set ≪ X·exp(−c√(log X)·log log X)-type for
  K ≍ √log X); it cannot reach every p because the sieve bound never drops below X^{1−o(1)}·(log)^{−K/2} while K is
  limited to o(log X/log log X) by the level of distribution.
* **Multiplicative links between different d.** For coprime d₁, d₂: n_{d₁d₂} ≡ n_{d_i} (mod d_i), but 4n_dC_d = d + 1 is a
  statement about the *integer* n_dC_d (branch k = 1 of 4n_dC_d = kd + 1, k ≡ 1 (mod 4)), not about residues; HIT(d₁) and
  HIT(d₂) say nothing about HIT(d₁d₂) (at p = 100 000 037 the 26 hits d ≤ p^{3/4} have 0 of their 48 pairwise products
  ≤ p^{3/4} in the hit set; 9 of the 36 pairs a | b of a hit b and a 3 (mod 4) divisor a are both hits, 5 of them with
  a = 3 — the trivial effect of p ≡ 2 (mod 3); `z57_bff_hitset_closure.py`). The only closure is within an n-line:
  the divisors of p + n in the class −1 (mod 4n) are closed under taking divisors in that class — a restatement. The switch (n, m, C) ↦ (m, n, C) (`Z56_FAMATTACK` Lemma L(a)) maps HIT(d_P) to
  HIT(d_Q) with d_Pd_Q = 4Cp + 1 — it maps a hit to a hit and an empty set to an empty set.

### 2.3 What would suffice (the minimal statement, in this lane's coordinates)

Any of the following implies the target (PROVED implications via Lemmas 1.2–1.3), and each fails at odd squares only
through Lemma 1.4:
 (S1) for every large p ≡ 1 (4) there is d ≡ 3 (4), d ≤ p^{3/5}, with (−p mod d)·(−(4p)⁻¹ mod d) < 5d/4;
 (S2) for every large p ≡ 1 (4) there is n ≤ p^{1/3} such that p + n has a divisor in the class −(p + n) (mod 4n) lying in
      [p^{1/4}, p^{2/3}] (then d = (p+n)/m ≤ p^{3/4}, m ≥ p^{1/4}; the 𝔊* check is the inequality of Lemma 1.3);
 (S3) for every large p ≡ 1 (4) some C ≤ (p/64)^{1/3} has 4Cp + 1 ∉ 𝒮_C, where 𝒮_C is the set of integers ≡ 1 (mod 4C)
      none of whose sub-multisets of prime factors multiplies to −1 (mod 4C).
No proof of any of them is offered. (S1) is the sharpest: the branch structure 4n_dC_d ∈ {d + 1, 5d + 1, 9d + 1, …}
means the hit is the event "n_dC_d is below the second branch", a gap of factor 5 — a lower bound of the form
#{d ≤ D : n_dC_d < 5d/4} ≥ 1 for one p is a *small-product* statement on the modular hyperbola 4xy ≡ 1 across all moduli
d ≤ D at the single point x ≡ −p, and no equidistribution statement for points on modular hyperbolas (which are proved
for a fixed modulus and varying points, or varying moduli with averaged weights) applies to a fixed residue class of a
fixed p across moduli. This is the exact shape of the obstruction.

## 3. Computations

### 3.1 Engines (CERTIFIED for the stated ranges)

* `scripts/z57_bff_engine.py` (numpy): for one p, scans d ≡ 3 (4) up to ⌊p^{3/4}⌋ + ⌊p^{1/12}⌋ + 10, tests
  4n_d | d + 1 (Lemma 1.2), rebuilds (n_d, m, C_d), asserts 4n_dmC_d − n_d − m = p, and keeps the unordered solutions
  with max⁴ > min·p. Validation (`z57_bff_validate.py`): equals the z56 F4 (= 𝔊*) hit count at 437 primes of
  `data/z56/famdesign/zeros_le1e8.txt` (all 37 zeros ≤ 10⁸ plus 400 random rows) and at 60 random primes of
  `decide_1e7_1e10.txt` (10⁷ < p ≤ 10¹⁰), 0 mismatches; R_𝔊*(564 661 441) = 0.
* `scripts/z57_bff_decide.c`: segmented sieve of the primes p ≡ 1 (4) in [A, B]; for each p scans d = 3, 7, 11, … up to
  ⌊p^{3/4}⌋ + 1 (⌊p^{3/4}⌋ computed as the largest D with D⁴ ≤ p³ in 128-bit integers), stops at the first d with
  4n_d | d + 1 whose solution satisfies max(n_d, m)⁴ > min(n_d, m)·p (exact in unsigned 128-bit; Q ≥ 2³² is accepted
  outright since then Q⁴ ≥ 2¹²⁸ > P·p). By Lemma 1.3 "no such d" is exactly R_𝔊*(p) = 0. Validation: on [5, 10⁸] it
  prints exactly the 37 zeros of `Z56_FAMDESIGN` (`decide_le1e8.txt`, diff-identical to `gstar_zeros_le1e8.txt`;
  2.8 s), on (10⁸, 10⁹] exactly {564 661 441} (31 s). (Note that this decider is independent of z56's: it enumerates
  by d instead of by levels C, and uses no floating-point membership test.)
* `scripts/z57_bff_firsthit.c`: first-hit statistics on samples (d₁(p) := least d with HIT(d) and the solution in 𝔊*;
  d₁^prime(p) := least prime such d, scanned to p^{0.8}).

### 3.2 Results

* **Zero-free range (CERTIFIED).** No 𝔊*-zero in (10¹⁰, 10¹¹]: all 1 831 497 005 primes p ≡ 1 (4) there have a
  𝔊* hit (`decide_1e10_1e11_summary.txt`; ten blocks of 10¹⁰, ≈ 11 min each on a loaded machine; the prime counts per
  block are listed, and 2 880 504 + 22 542 987 = 25 423 491 = π(10⁹; 4, 1) on the validation ranges). With z56's
  exhaustive 10¹⁰ result: **R_𝔊*(p) = 0 at exactly 38 primes p ≡ 1 (4) ≤ 10¹¹, the last 564 661 441.** The largest
  first-hit d in (10¹⁰, 10¹¹] is 2 923 999 ≈ p^{0.600} (p = 61 032 630 877); per block the maxima are 0.8–2.9·10⁶,
  i.e. every prime up to 10¹¹ has a 𝔊* hit with d ≤ p^{0.71} (and the decider needs on average ≈ p^{0.09} steps).
  Extension to 5·10¹¹: EXT_PLACEHOLDER
* **First hit (EVIDENCE; `firsthit_1e8/1e9/1e10.txt`).** Exponent θ₁ := log d₁(p)/log p over the primes p ≡ 1 (4) in
  [10⁸, 10⁸ + 4·10⁵] (10 819 primes), [10⁹, 10⁹ + 4·10⁵] (9 613), [10¹⁰, 10¹⁰ + 10⁵] (2 150):
  mean θ₁ = 0.109, 0.097, 0.088; median 0.060, 0.053; P(θ₁ > 0.2) = 9.5 %, 7.4 %, 4.8 %; P(θ₁ > 0.3) = 1.6 %, 1.0 %,
  0.2 %; P(θ₁ > 0.4) = 0.17 %, 0.05 %, 0; max 0.49, 0.50, 0.34. Exhaustive maxima of d₁: 157 055 (p = 94 704 157,
  θ₁ = 0.651) on [5, 10⁸]; 787 439 (p = 231 507 061, θ₁ = 0.705) on (10⁸, 10⁹]. The tail decays with p roughly like the
  model exp(−c·(1/8)·θ²log²p) (c ≈ 1–1.5 fitted); at the 38 zeros θ₁ > 3/4 by definition. First hits restricted to *prime* d:
  mean exponent 0.12, 0.6 % above 0.5, and 9 of 10 819 primes near 10⁸ have no prime-d hit below p^{0.8} at all
  (composite d are essential: prime-d hits number only ≍ log p in expectation, Assessment).
* **Local data of the zeros (`z57_bff_zeros_local.py`).** All 38 have (p/3) = +1 (p ≡ 2 (3) gives the hit d = 3) and
  least prime QNR in {5, 7, 11, 13, 17, 19, 23, 29}; 6 of them are ≡ 1 (mod 840), 30 are ≡ 1 (mod 8). They are not
  confined to Mordell's six classes mod 840 (e.g. 37, 157, 577 have (p/5) = −1): the classical identities for those
  classes produce (★) solutions in the Burgess corner (e.g. p ≡ 5 (mod 8): (o, e, C) = (1, 2, (p + 3)/8)), or non-(★)
  shapes.

## 4. Screens, verdict, bottom line

* **T1 (odd squares).** Passes by construction: Corollary 1.5 shows every reformulation is false at N = M² and
  identifies (d/p) = −1 as the unique entry point of primality. No argument in §2 produces a hit, so there is nothing
  to audit beyond this.
* **Fixed-p / 8/131 / B2.** Not applicable (no positivity claim). The 38 zeros satisfy every necessary condition
  derived here (Lemma 1.6 at levels 1–3 checked; (p/3) = +1 for all).
* **Verdict: narrowed, not proved.** The lane's contribution is (i) the exact and symmetric defect/hyperbola form of the
  target — "some d ≡ 3 (4) below p^{3/4} has (−p mod d)·(−(4p)⁻¹ mod d) < 5d/4" — with its two coordinates being the
  n-lines and C-levels of z56; (ii) the proof that primality enters only through (d/p) = −1 and that the Burgess
  threshold p^{1/4} is where the quadratic obstruction disappears, which explains the 𝔊* boundary of Thm V from the
  d-side; (iii) the identification of the decisive range d ≤ p^{1/3} where single-p information is provably absent
  below c·log p and unavailable above it; (iv) a certified zero-free range to 10¹¹ by an independent decider.
  **ES is OPEN; R_𝔊*(p) ≥ 1 for all large p is not proved, and no weaker pointwise theorem beyond the classical
  identity classes was found.**
* **For SYNTH/FRONTIER (proposed text, not applied):** "Z57_BFF: R_𝔊*(p) ≥ 1 ⟺ ∃ d ≡ 3 (4), d ≤ ⌊p^{3/4}⌋ + 1, with
  4·(−p mod d)·(−(4p)⁻¹ mod d) = d + 1 and the 𝔊* inequality (automatic for d ≤ p^{3/5}); every such d has (d/p) = −1
  (the T1 mechanism). CERTIFIED: no 𝔊*-zero in (10¹⁰, 10¹¹]."
