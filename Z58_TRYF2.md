# Z58_TRYF2 — tryhard lane F2: "some p+u has a divisor ≡ −1 (mod 4u)"

Lane: TRYF2 (wave z58). Fresh, unprimed attack per `z52bbriefs/z55_tryhard.md` (z55→z58). Only external data used:
`data/z58/screens/`. Scripts: `scripts/z58_tryf2_*`; data: `data/z58/tryf2/`.

**Status line (updated at every commit):** NO PROOF of the target; no HOT LEAD. Deliverable: the exact split
R(p) = M₂(p) + E₂(p) (§3) with **Theorem A (PROVED): M₂(p) ≥ c₀ log² p for all large primes p ≡ 1 (4)**, M₂ ≡ 0 at
squares (primes only; composites not proved), and the open core isolated as the single inequality E₂(p) > −M₂(p)
(not reachable by two-bounded-coordinate arguments, Prop. 2.1; false on the C-even sub-family at 12 primes near 10¹⁰, §4(b)/F2). Everything below is labelled PROVED / CONDITIONAL / CERTIFIED /
CONDITIONAL. No HOT LEAD yet.

Notation. For n ≡ 1 (mod 4) put R(n) := #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n} = #{(u,d) : u ≥ 1, d | n+u, d ≡ −1 (mod 4u)}
(matches `scripts/z58_screens_rstar.c`). The target is R(p) ≥ 1 for all large primes p ≡ 1 (24).

## §0 Falsifier behaviour of the line of attack (written at the first commit; revised after the hostile review; re-stated in §7)

The line of attack (§1–§4) is: (i) rewrite R(p) in equivalent ways that expose where primality enters, (ii) prove
that no argument whose hits have two bounded coordinates can work (Prop. 2.1), (iii) split R = M₂ + E₂ where M₂ is
the count predicted by equidistribution of the Jacobi-non-residue divisors of 4pC+1 over the φ(4C)/2 admissible
classes, prove M₂(p) ≫ log² p for every large prime (Theorem A), and (iv) isolate E₂ > −M₂ as the open core.

* (F1) odd squares n = m². Lemma 1.3 gives (d/n) = (−C/d) for every d | 4nC+1 coprime to n; for n = m² the left side
  is +1 while d ≡ −1 (mod 4C) forces (−C/d) = −1, so R(m²) = 0. M₂(n) counts divisors with (d/n) = −1, so
  M₂(m²) = 0 identically. In Theorem A the non-squareness enters at one identifiable step: Pólya–Vinogradov for the
  non-principal character (·/p) gives the weight w_d = 1[(d/p) = −1] positive density (Step 5). ✔ consistent.
* (F2) C even only. The split R₈ = M₂^{even} + E₂^{even} and Theorem A's proof (with 8p in place of 4p) apply to
  the C-even sub-family, and at the 12 F2 primes E₂^{even} = −M₂^{even} (at the two evaluated ones the truncated
  values are M₂^{even}(C ≤ 1500) = 11.1 and 15.6). These are finite counterexamples; they do not disprove an
  *eventual* C-even statement. What they do establish: no argument in this lane proves E₂ > −M₂ (nothing here does),
  and any future argument proving E₂ > −M₂ for all p ≥ p₀ that applies unchanged to the C-even sub-family must have
  p₀ > 10 917 229 157 (the largest F2 prime). ✔ consistent (nothing is proved that
  would transfer to the false statement).
* (F3) 285 composite non-square zeros n ≤ 8·10⁶. Theorem A is proved for primes only; its extension to composite
  non-squares is NOT proved here (the density of units in (ℤ/n) and imprimitive characters need separate treatment).
  M₂(57) = M₂(105) = 0 exactly and M₂(2305) = 2.25 (computed). A positivity statement for composites would need a
  threshold beyond the largest composite zero, which is unknown. ✔ consistent.
* (F4) 14 prime zeros 409 … 8 813 281. They are zeros of R, not of M₂: all have M₂(C ≤ √p) ∈ [1.1, 16.4] > 0 and
  E₂ = −M₂. Theorem A (a lower bound for M₂, not R) is unaffected; any positivity theorem for R must have threshold
  > 8 813 281. ✔ consistent.

Conclusion of §0: the line can only close by proving E₂(p) > −M₂(p) for every individual large prime; §4 records why
the estimates attempted here (exponential sums, zero-sum arguments, couplings between different C) do not reach it.

## §1 Equivalent forms of a hit (all PROVED, elementary)

Throughout n ≡ 1 (mod 4) is a positive integer (n = p prime in the target), and a *hit* is a triple (u,B,C) ∈ ℕ³ with
4uBC − u − B = n. Put d := 4uC − 1, N_C := 4nC + 1.

**Lemma 1.1 (five faces of a hit).** The following sets are in explicit bijection:
(a) {(u,B,C) : 4uBC − u − B = n};
(b) {(u,d) : u ≥ 1, d ≡ −1 (mod 4u), d | n+u} via d = 4uC−1, B = (n+u)/d;
(c) {(u,B) : 4uB | n+u+B} (symmetric in u ↔ B) via C = (n+u+B)/(4uB);
(d) {(C,d) : d | 4nC+1, d ≡ −1 (mod 4C)} via (4uC−1)(4BC−1) = 4nC+1, i.e. the second factor is N_C/d;
(e) {d ≥ 3 : d ≡ 3 (mod 4), d ∤ n, r_d | (d+1)/4} where r_d := (−n mod d) ∈ [1,d−1]; here u = r_d, C = (d+1)/(4r_d).
*Proof.* (a)⇔(b): B(4uC−1) = n+u. (a)⇔(c): n+u+B = 4uBC. (a)⇔(d): expand (4uC−1)(4BC−1) = 16C²uB − 4C(u+B) + 1
= 4C(4uBC−u−B) + 1; conversely a divisor d ≡ −1 (4C) of N_C has cofactor N_C/d ≡ d⁻¹ ≡ −1 (4C), so both factors are
of the form 4xC−1. (b)⇔(e): if d | n+u and d ≡ −1 (4u) then u ≤ (d+1)/4 < d, so u = (−n mod d) = r_d and 4u | d+1;
conversely r_d | (d+1)/4 gives u := r_d, C := (d+1)/(4u) ≥ 1, d | n+u. ∎
(Also: with k := (n+r_d)/d, (e) reads "k·d − n = r_d divides (d+1)/4", and (c) reads "4r_d·k | n + r_d + k".)

**Remark 1.2 (continued-fraction face).** For u ≥ 3, B ≥ 2 the Euclidean algorithm on (n,d) runs n = (B−1)d + (d−u),
d = 1·(d−u) + u, d−u = (4C−2)u + (u−1), u = 1·(u−1) + 1, (u−1) = (u−1)·1, so n/d has regular continued fraction
[B−1; 1, 4C−2, 1, u−1] (for u = 2 the third division already terminates: d−u = (4C−2)·2 + 1, 2 = 2·1, giving [B−1; 1, 4C−2, 2])
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
gcd(d,n) = 1 because d | 4nC+1. (iii): t ↦ (−C/t) on odd t coprime to C is a character mod 4C, nontrivial
because −C < 0 is not a square; its kernel has index 2. ∎
Numerically verified (`scripts/z58_tryf2_jacobi_check.py`): identity holds for all 32 374 distinct pairs (C ≤ 400, d | 4nC+1)
at n ∈ {5, 13, 409, 577, 841, 1225, 57, 105, 2305, 10009, 9601, 12841}; h_C ≤ m_C (notation of §4) throughout.

In Theorem A's proof non-squareness enters only through the non-principality of the character (·/n): every hit is a
Jacobi non-residue, and squares have none.

## §2 No argument with two bounded coordinates can work (PROVED), and how non-local the hits are (EVIDENCE)

Call a hit (u,B,C) *U-local* if at least two of u, B, C are ≤ U. By Lemma 1.1 the three "two-small" regions are
(u,C ≤ U) [then d ≤ 4U² is small and the hit is the congruence d | n+u], (u,B ≤ U) [the congruence 4uB | n+u+B] and
(B,C ≤ U) [mirror of the first]. Whether n has a U-local hit depends only on n modulo
L_U := lcm{4uC−1, 4uB : u,B,C ≤ U}.

**Proposition 2.1.** For every U ≥ 1 there are infinitely many primes p ≡ 1 (mod 840) (hence p ∈ 𝔐) with no U-local
hit; indeed every prime p ≡ 1 (mod 840·L_U) has none. In particular, there are infinitely many primes all of whose
hits have at least two coordinates ≥ c·√(log p) (c > 0 absolute).
*Proof.* p ≡ 1 (mod 4uC−1) means p + u ≡ 1 + u ≢ 0 (mod 4uC−1) as 1 ≤ 1+u < 4uC−1 for all u,C ≥ 1 (for u = C = 1:
2 < 3); p ≡ 1 (mod 4uB) means p+u+B ≡ 1+u+B ≢ 0 (mod 4uB) since 1 ≤ 1+u+B < 4uB. Dirichlet gives infinitely many
such primes. For the last clause: every modulus in L_U is ≤ 4U², so L_U | lcm(1,…,4U²) and log L_U ≤ ψ(4U²) = O(U²)
(Chebyshev). By Linnik's theorem there is a prime p ≡ 1 (mod 840 L_U) with p ≤ (840 L_U)^{L}, i.e. log p = O(U²), so
U ≥ c√(log p) is admissible. ∎
(Scope: this excludes arguments whose produced hit has two coordinates bounded in terms of nothing, e.g. all
"polynomial identity" constructions and all finite coverings by congruence classes; it does **not** exclude a fixed
finite set of u's with B, C unbounded (for u = 1 that would be "p+1 has a divisor ≡ 3 (mod 4)", which fails whenever
p+1 = 2q with q ≡ 1 (4) prime — believed to happen infinitely often, but not provably so). Numerically u ≤ 8 with
B, C free has 254 zeros among primes ≤ 2·10⁶ (198 of them in 𝔐), Data 2.2.)

**Data 2.2 (EVIDENCE, `scripts/z58_tryf2_lambda.c`, `data/z58/tryf2/lambda_4e6.txt`).** Λ(p) := min over hits of the
second-smallest coordinate (∞ if R(p) = 0; the script caps at 255). Over the 141 502 primes p ≡ 1 (4), p ≤ 4·10⁶:
Λ ≤ 2 for 87.6 %, but 769 primes have 20 ≤ Λ < 255 and the largest finite values are Λ(764 017) = 143,
Λ(1 265 617) = 135, Λ(427 249) = 131; the script's cap 255 is reached by the 12 zeros ≤ 4·10⁶ and by p = 1 426 489,
whose only hits are (3, 356, 334) and its mirror, so Λ(1 426 489) = 334 (≈ p^{0.41}). No 𝔐-prime has Λ ≤ 2: Λ ≤ 2 needs two coordinates
in {1,2}; (u,C) or (B,C) ∈ {1,2}² means d ∈ {3,7,15} divides p+u, i.e. p ≡ 2 (3), p ≡ 5 or 6 (7), or p ≡ 13 (15),
all excluded for p ∈ 𝔐 (p ≡ 1 (3), p a QR mod 5 and mod 7); (u,B) ∈ {1,2}² means 4 | p+2, 8 | p+3 or 16 | p+4,
excluded for p ≡ 1 (8). (u = 1 itself is fine for 𝔐-primes: 4201 = 4·1·382·3 − 1 − 382 has Λ = 3.)
Sub-family zero counts for primes ≤ 2·10⁶ (`data/z58/tryf2/subfam_2e6.txt`): full R: 12 zeros (the F4 list
≤ 2·10⁶); hits with d prime: 117 zeros; u,C ≤ 8: 4266 zeros; u,B ≤ 8: all 4519 𝔐-primes are zeros (local, as
predicted); u ≤ 8 (B,C free): 254 zeros; C = 1: 17 597 zeros; u = 1: 9308 zeros; "middle" hits with d, B ≥ n^{1/4}:
31 zeros; C even: 518 zeros.

## §3 Decomposition R = M₂ + E₂ and the provable half (Theorem A)

Fix n ≡ 1 (4) and C ≥ 1; N_C = 4nC+1 is odd, every divisor is coprime to 2. Define
  h_C := #{d | N_C : d ≡ −1 (mod 4C)}  (so R(n) = Σ_C h_C, the sum is finite: C ≤ (n+2)/4),
  m_C := #{d | N_C : (d/n) = −1},    m₂,C := #{d | N_C : 4C−1 ≤ d < √N_C, (d/n) = −1}.
By Lemma 1.3, hits pair up (d ↔ N_C/d, both ≡ −1 mod 4C; d = N_C/d is impossible, since d² = 4nC+1 with d = 4uC−1
would give n = 4Cu² − 2u even), every hit has (d/n) = −1, and no d < 4C−1 can hit. If the
pair-representatives d < √N_C with (d/n) = −1 and d ≥ 4C−1 were uniformly distributed over the φ(4C)/2 classes of
O_C, the expected value of h_C would be 2·m₂,C/(φ(4C)/2). Define accordingly
  **M₂(n) := Σ_C 4·m₂,C/φ(4C),   E₂(n) := R(n) − M₂(n).**
M₂ is a *surrogate* (model) main term: the uniform-distribution assumption behind it is not proved, and the split is a
tautology (R ≥ 1 ⇔ E₂ > −M₂ because R is a non-negative integer); no bound on E₂ is claimed anywhere in this memo.
M₂(m²) = 0 for every odd m (no d has (d/m²) = −1). E₂ is the aggregate deviation of the exact class −1 from the
coset average.

**Theorem A (PROVED below).** There are absolute constants c₀ > 0, p₀ such that for every prime p ≡ 1 (mod 4), p ≥ p₀:
  M₂(p) ≥ c₀ log² p.
(With the proof's choices, c₀ = 1/300 works for p ≥ p₀(ε) with ε = 1/10; no attempt at optimisation.)

Hence R(p) ≥ 1 for all large primes **⇐** E₂(p) > −M₂(p), i.e. the exact class −1 receives, summed over C ≤ (p+2)/4,
more than zero of its coset-average share. (The stronger R(p) ≥ δM₂(p) — a positive *fraction* of the share — is what
the numerics in Data 3.1 suggest for most primes, but is not needed.) This is the whole open content; §4 records why
the methods tried here do not reach it and what F2 says about it.

### Proof of Theorem A
Fix ε ∈ (0, 1/10]. All implied constants are absolute. Write χ := (·/p) (a non-principal real character mod p).

*Step 1 (the counted pairs).* For X ≥ 1 and D ≥ 1 let
  S(X,D) := #{(C,d) : X ≤ C < 2X, D < d ≤ 2D, d | 4pC+1, χ(d) = −1}.
If D ≥ 8X and 2D ≤ √(4pX), then every (C,d) counted satisfies d ≥ 8X > 4C−1 and d ≤ 2D ≤ √(4pX) < √(4pC+1), so (C,d)
contributes to m₂,C; also φ(4C) ≤ 4C < 8X. Therefore
  M₂(p) ≥ Σ_{(X,D)} S(X,D)·(4/(8X)) = Σ_{(X,D)} S(X,D)/(2X),                                              (3.1)
the sum over any family of pairwise disjoint boxes [X,2X)×(D,2D] with 8X ≤ D and D ≤ √(pX) (then 2D ≤ 2√(pX) ≤ √(4pX)).

*Step 2 (one box).* Let X ≥ p^{1/2+ε}, 8X ≤ D ≤ √(pX) (so D ≤ p/8 < p). For odd d ∈ (D,2D], gcd(d,4p) = 1 (d < p), let
c_d := (−\overline{4p} mod d) ∈ [1,d−1], the unique C mod d with d | 4pC+1. Since 2X ≤ D/4 < d, the C ∈ [X,2X) with
d | 4pC+1 is unique and exists iff c_d ∈ [X,2X). Hence
  S(X,D) = #{d ∈ (D,2D] odd : χ(d) = −1, c_d ∈ [X,2X)}.
Put η := p^{−ε/4}, D_j := D(1+η)^j and keep the K := ⌊(log 2)/log(1+η)⌋ complete blocks B_j = (D_j, D_j(1+η)],
0 ≤ j < K, all inside (D,2D] (the remainder of (D,2D] is discarded; K ≥ (log 2)/η − 1 since log(1+η) ≤ η). For d ∈ B_j,
[X/D_j, 2X/(D_j(1+η))) ⊆ [X/d, 2X/d), so with I_j := [X/D_j, 2X/(D_j(1+η))) (length ≥ (X/D_j)(1−2η)),
  S(X,D) ≥ Σ_j #{d ∈ B_j odd : χ(d) = −1, {ξ_d} ∈ I_j},   ξ_d := −\overline{4p}/d  (mod 1),  {ξ_d} = c_d/d.   (3.2)

*Step 3 (reciprocity).* For gcd(a,b) = 1, a\bar a + b\bar b ≡ 1 (mod ab) (check mod a and mod b), so
\bar a/b + \bar b/a ≡ 1/(ab) (mod 1). With a = 4p, b = d: ξ_d ≡ \bar d/(4p) − 1/(4pd) (mod 1), where \bar d is the
inverse of d mod 4p. Thus e(hξ_d) = e(h\bar d/(4p))·e(−h/(4pd)); the second factor has derivative in d of size
= πh/(2pd²) ≤ 2h/(pD²), so its total variation over B_j is ≤ ηD_j·2h/(pD²) ≤ 4h/(pD) ≤ 1 for h ≤ D (as p ≥ 4).

*Step 4 (complete and incomplete sums).* For w ∈ {1, χ} and integers h, k, the complete sum
  T_w(h,k) := Σ_{d mod 4p, gcd(d,4p)=1} w(d)·e((h\bar d + k d)/(4p))
factors by CRT (4p = 4·p, p odd) as a product of a sum mod 4 (absolute value ≤ 2) and a sum mod p of the form
Σ_{d mod p}^{*} w(d) e((h'\bar d + k'd)/p). For w = 1 this is a Kloosterman sum, |K(h',k';p)| ≤ 2√p·gcd(h',k',p)^{1/2}
(Weil); for w = χ it is a Salié sum, |Σ χ(d)e((h'\bar d+k'd)/p)| ≤ 2√p (Salié's explicit evaluation; or Weil–Deligne
for twisted Kloosterman sums). Here h' ≡ h·(inverse of 4 mod p)-type units times h, so gcd(h',p) = gcd(h,p) = 1 for
1 ≤ h < p. Hence |T_w(h,k)| ≤ 4√p for 1 ≤ h < p and all k. By completion (write 1_{B}(d) via its discrete Fourier
transform mod 4p: 1_B(d) = (1/4p)Σ_k \hat{1_B}(k)e(−kd/4p) with Σ_k|\hat{1_B}(k)| ≤ 4p·(2 + log(4p))),
  |Σ_{d ∈ B'} w(d)·1_{d odd}·e(h\bar d/(4p))| ≤ 4√p·(2 + log 4p)                                                 (3.3)
for every interval B' ⊂ (0,p) and 1 ≤ h < p (the summand is defined as 0 unless gcd(d,4p) = 1, which for d < p is the
same as d odd; all intervals used lie in (0,2D] ⊂ (0,p)). By partial summation with Step 3 (total variation ≤ 1 for h ≤ D < p),
  |Σ_{d ∈ B_j odd} w(d) e(hξ_d)| ≤ 2·4√p·(2 + log 4p) ≤ 16√p log p   (p ≥ p₀).                                   (3.4)

*Step 5 (Erdős–Turán on one block).* Let w_d := ½(1 − χ(d))·1_{d odd} ∈ {0,1} (indicator of "odd and χ(d) = −1" for
d < p), W_j := Σ_{d ∈ B_j} w_d. By Pólya–Vinogradov, W_j = ¼ηD_j + O(√p log p) (count odd d in B_j: ½ηD_j + O(1);
subtract ½Σ_{d ∈ B_j odd} χ(d), and Σ_{odd d ∈ B'} χ(d) = Σ_{d∈B'} χ(d) − χ(2)Σ_{d' ∈ B'/2} χ(d') ≪ √p log p).
Since w_d ∈ {0,1}, apply the Erdős–Turán inequality (Montgomery, *Ten Lectures on the Interface between Analytic Number
Theory and Harmonic Analysis*, Ch. 1: for x₁,…,x_N ∈ ℝ/ℤ and any interval I, |#{i: x_i ∈ I} − |I|N| ≤ N/(H+1) +
3Σ_{h≤H} h⁻¹|Σ_i e(hx_i)|) to the sequence (ξ_d)_{d ∈ B_j, w_d = 1} of length W_j: for every H ≥ 1
  #{d ∈ B_j : w_d = 1, {ξ_d} ∈ I_j} ≥ |I_j|·W_j − W_j/(H+1) − 3Σ_{h=1}^{H} (1/h)|Σ_{d∈B_j} w_d e(hξ_d)|.
Each exponential sum is ½(Σ_{odd} e(hξ_d) − Σ_{odd} χ(d)e(hξ_d)) ≤ 16√p log p by (3.4). Take H := ⌈p^{ε/4}·D_j/X⌉; then
H ≤ p^{ε/4}·2D/X + 1 ≤ D (as X ≥ p^{1/2+ε} ≥ 4p^{ε/4} and D ≥ 2), so H ≤ D < p as required in Steps 3–4. Then
  #{…} ≥ (X/D_j)(1−2η)·W_j − W_j·X p^{−ε/4}/D_j − 48√p·log p·(1 + log D).
Insert W_j = ¼ηD_j + O(√p log p) and use X/D_j ≤ 1/8: the right side is
  ≥ ¼ηX(1 − 2η − p^{−ε/4}) − O(√p log p) − O(√p log² p) = ¼ηX(1 − 3η) − O(√p log² p)   (η = p^{−ε/4}).
Since ¼ηX·η = ¼X p^{−ε/2} ≥ ¼p^{1/2+ε/2} ≫ √p log² p, the O-term is ≤ ¼ηX·η for p ≥ p₀(ε), and so
  #{d ∈ B_j : w_d = 1, {ξ_d} ∈ I_j} ≥ ¼ηX(1 − 4η)   for every j.
Summing over the K ≥ (log 2)/η − 1 blocks, (3.2) gives S(X,D) ≥ ¼X(log 2 − η)(1 − 4η) ≥ ¼X(log 2)(1 − 7η), hence
  S(X,D) ≥ X/6     (p ≥ p₀(ε); note ¼ log 2 = 0.1733… > 1/6).                                                 (3.5)

*Step 6 (summing the boxes).* Put Λ := (½−ε)log₂ p and take X_i := 2^i·p^{1/2+ε} for 0 ≤ i ≤ I := ⌊Λ − 6⌋ (so
X_i ≤ p/64), and for each i the dyadic D_{i,j} := 8X_i·2^j, 0 ≤ j ≤ J_i := ⌊log₂(√(p/X_i)/8)⌋ (so D_{i,j} ≤ √(pX_i)).
These boxes are pairwise disjoint and satisfy the hypotheses of Steps 1–5. By (3.1) and (3.5),
M₂(p) ≥ Σ_i Σ_j (X_i/6)/(2X_i) = (1/12)Σ_{i=0}^{I}(J_i + 1). Since log₂(p/X_i) = Λ − i, J_i + 1 ≥ ½(Λ − i) − 3, so
  Σ_{i=0}^{I}(J_i+1) ≥ (I+1)(½Λ − 3) − ¼I(I+1) = (I+1)(½Λ − 3 − ¼I) ≥ (Λ−6)(¼Λ − 3/2) = ¼(Λ − 6)²,
using I ≤ Λ − 6 and I + 1 ≥ Λ − 6. Hence M₂(p) ≥ (Λ − 6)²/48 = ((½−ε)log₂ p − 6)²/48 ≥ c₀ log² p with
c₀ = (½−ε)²/(48 (log 2)²)·(1 − o(1)); for ε = 1/10 this is ≥ 1/300 for p ≥ p₀. ∎

*Where primality was used.* (i) χ = (·/p) is non-principal, so Pólya–Vinogradov makes the QNR weight w_d have positive
density — at n = m² the weight is identically 0 and M₂ = 0; (ii) Weil/Salié bounds for the complete sums mod p with
gcd(h,p) = 1 for h < p. *Composite non-squares n (NOT PROVED here).* One expects the same statement with (·/n) in
place of (·/p) and Weil's bound for composite moduli, but three things change and were not worked out: d < n no
longer forces gcd(d,n) = 1 (the weight must be restricted to units, whose density φ(n)/n has no absolute lower bound,
so c₀ could at best depend on n through φ(n)/n), the Jacobi character (·/n) may be imprimitive, and the twisted
complete sums mod 4n need the composite-modulus bounds with their gcd factors. Theorem A is therefore claimed for
primes only.

**Data 3.1 (EVIDENCE, `scripts/z58_tryf2_mterm.c`, `data/z58/tryf2/mterm_*.txt`).** Full-range (C ≤ (n+2)/4) values:
| n | R | M₂ | E₂/M₂ |
|---|---|---|---|
| 409, 577, 5569, 9601, 23929, 83449, 102001 (zeros) | 0 | 2.24, 1.44, 6.24, 6.98, 7.64, 9.94, 6.49† | −1 |
| 57, 105, 2305 (composite zeros) | 0 | 0.00, 0.00, 2.25 | −1 / n.a. |
| 841, 1225, 2209 (squares) | 0 | 0 | n.a. |
| 90 primes ≡ 1 (4) in [10⁵, 1.02·10⁵] | min 4, median 22 | min 10.4, q10 13.4, median 17.0, q90 24.8, max 39.7 | min −0.63, q10 −0.31, median +0.19, q90 +0.75, max +1.63 |
| 10 868 474 401, 10 156 800 001 (F2 primes), C ≤ 1500, C even only | 0 | 11.1, 15.6 | −1 |
| same, C odd only | 10, 38 | 17.1, 36.6 | −0.41, +0.04 |
(† 102001 with C ≤ √n only; the 14 zeros with C ≤ √n have M₂ = 1.8, 1.1, 4.9, 5.3, 5.5, 7.2, 6.5, 8.4, 10.5, 14.5, 12.5,
14.3, 16.4, 16.3, versus 18–51 for the eight size-matched primes computed, `data/z58/tryf2/mterm_zeros_sqrt.txt`;
the F2 values are truncated at C ≤ 1500 and grow with the cutoff, e.g. 12.7 and 17.4 at C ≤ 3000. All M₂ decimals are
rounded to 2–3 places; q10/q90 are the lower empirical order statistics (9th and 81st of 90 sorted values).) So on this
sample the model is roughly centred (median E₂/M₂ ≈ 0.2 with the crude "uniform on O_C" prediction), the zeros are primes with a comparatively
*low supply* of hit-capable QNR divisors that are additionally unlucky (E₂ = −M₂), and the C-even sub-family shows
E₂ = −M₂ on a sub-family with M₂^{even} ≳ 11–16 at p ≈ 10¹⁰.

## §4 Why the methods tried here do not reach E₂, and what F2 says about it (author's assessment, not theorems)

(a) *Scale.* In any box u ~ U, d ~ D (faces (b)/(e)) the expected number of hits is Σ_{u~U} Σ_{d~D, d ≡ −1 (4u)} 1/d ≈
(log 2)²/4 — an O(1) quantity; the total log² n comes from ≈ (log n)²/(2 log² 2) such boxes. Every estimate attempted
in this lane (van der Corput for e(hn/d), Weil/Salié/Karatsuba for e(h\bar n/d), Erdős–Turán) carries an error term
that is a positive power of n and therefore evaluates only counts with power-sized main terms. Theorem A is provable
because the main term S(X,D) ≍ X is power-sized and the 1/C weight is applied afterwards; in E₂ the class condition
d ≡ −1 (mod 4C) sits *inside* the divisor count and leaves a polylog main term. This is a limitation of these
estimates, not a proof that no analytic argument can succeed (cancellation across boxes or a reorganisation could
in principle do better; none was found).
(b) *What F2 says.* On the sub-family C even the same decomposition R₈ = M₂^{even} + E₂^{even} holds, and Theorem A's
argument gives M₂^{even}(p) ≫ log² p after routine changes (C = 2C′, d | 8pC′+1, cutoff 8C′−1, weight 4/φ(8C′), modulus
8p in Steps 3–4). At the 12 F2 primes E₂^{even} = −M₂^{even}. These are finitely many counterexamples below 1.1·10¹⁰;
they do not disprove an eventual C-even statement, and they do not prove that a future argument "must" couple
different C. They do show that an argument proving E₂ > −M₂ for all p ≥ p₀ which applies unchanged to C even needs
p₀ > 10 917 229 157, and heuristically (P(R₈(p) = 0) decays like a power of 1/log p per fixed-C condition, cf. §5) that such
counterexamples should keep occurring, in which case per-C or per-parity additivity is genuinely insufficient.
Couplings looked for and not found: gcd(4pC+1, 4pC′+1) divides C′−C, so two values of C share a divisor only through
C′−C, and a shared prime q with q ≡ −1 (mod 4C) and q ≡ −1 (mod 4C′) forces 4C, 4C′ | q+1, i.e. both C, C′ ≤ (q+1)/4;
nothing forces the second congruence from the first.
(c) *Zero-sum view.* For fixed u, "no hit" means the multiset of residues mod 4u of the odd prime factors of n+u (those
coprime to u) has no sub-product ≡ −1. Such multisets exist in every (ℤ/4u)^× (e.g. all residues in the kernel of an
odd character), so no zero-sum theorem forces a hit without extra information on the factorisation of n+u, which is
not available for an individual n. Only the length Ω(n+u) ≤ log₂(n+u) is known, and it is far below φ(4u) once
u ≫ log n.

## §5 Other attacks tried (the attempted implementations failed; recorded so nobody repeats them as is)

* Polynomial identities in p for 𝔐: any fixed finite menu of identities covering all target primes is impossible
  (Prop. 2.1 / F1). Identities using one extra datum (a prime q with
  (p/q) = −1): a prime hit d = q requires p ≡ −r (mod q) with r | (q+1)/4, which is a τ((q+1)/4)-element subset of the
  (q−1)/2 non-residues — "QNR" is necessary (Lemma 1.3), far from sufficient (409 ≡ 3 mod 7 is a QNR but not in
  G₇ = {5,6}).
* p = a² + b² (p + 2ab = (a+b)², u = 2ab): needs a divisor of (a+b)² in the class −1 (mod 8ab); candidates are
  d = 8abk−1 ≤ (a+b)², i.e. k ≤ (a+b)²/(8ab), and no mechanism makes any of them divide (a+b)². Square values of
  4pC+1: 4pC+1 = x² forces x = 2pt±1, C = t(pt±1); the divisor d = x fails (x+1 ∈ {2pt+2, 2pt}, not divisible by
  4t(pt±1)); other divisors of x² were not analysed, and the family's expected count Σ_t τ(x²)/(4C) ≪ Σ_t p^{o(1)}/(pt²)
  is bounded, so it cannot carry a log² p main term. (The norm −1 unit of ℚ(√p) was considered as a source of such C
  and abandoned for the same reason.)
* Descent / Vieta: the surface 4xyz − x − y = p is linear in each variable, so no non-trivial involutions; for fixed C the
  solutions are the factorisations of 4pC+1.
* Fixed-shape sub-families: (u = C), (B = u+1), (k = r+1 in face (e)) all have expected count Σ_u O(1/u²) < ∞ (heuristic);
  (C = 1), (u = 1), (u ≤ U₀) are expected to fail on a (log p)^{−α} proportion of primes (standard shifted-prime
  sieve heuristics: e.g. C = 1 fails iff 4p+1 has all prime factors ≡ 1 (4)); EVIDENCE in Data 2.2 (17 597, 9308, 254
  zeros below 2·10⁶ respectively).
* Continued fractions (Remark 1.2): same scale obstruction as (a) of §4.

## §6 Verdict

No proof, no HOT LEAD. The lane's net contribution is the split R = M₂ + E₂ with Theorem A: the square-sensitive main
term M₂(p) ≫ log² p is PROVED for all large primes, using the two square-sensitive inputs that were found (non-principality
of (·/p); Weil/Salié bounds mod p), and all remaining difficulty is the single inequality E₂(p) > −M₂(p), which
(i) is not implied by finitely many congruence conditions on p (Prop. 2.1, for arguments whose hit has two bounded
coordinates), (ii) fails on the C-even sub-family at 12 primes near 10¹⁰ (F2), so that any argument which would also prove
C-even positivity at all primes ≥ 10¹⁰ is false (parity-dependent bounds whose *sum* proves R ≥ 1, or a successful odd-C
contribution, are not excluded; see §4(b)), and (iii) is numerically a fluctuation of relative size ±1 about 0, with the 14
zeros at the low end of the M₂ values computed. A HOT LEAD would be any mechanism coupling hits at different C (or
different u) for the same p; none was found.

## §7 Falsifiers, restated at the end

* (F1) squares: M₂(m²) = 0 identically (Lemma 1.3), so Theorem A's conclusion fails at squares exactly because (·/m²)
  is principal; the step "Pólya–Vinogradov gives w_d positive density" (Step 5) is where non-squareness is used.
  ✔ consistent.
* (F2) C even: the decomposition and Theorem A's argument survive restriction to C even (with 8p for 4p), and the
  needed inequality E₂ > −M₂ fails on that sub-family at 12 primes near 10¹⁰ (verified at two of them: M₂^{even}(C ≤ 1500)
  = 11.1, 15.6 with R₈ = 0). The lane proves nothing that would transfer to the C-even statement, since it proves
  nothing about E₂ at all. ✔ consistent; F2 is now a concrete statement about E₂ (§4(b)).
* (F3) composite zeros ≤ 8·10⁶: Theorem A is claimed for primes only; the composite case is explicitly NOT PROVED.
  M₂(57) = M₂(105) = 0, M₂(2305) = 2.25 (computed). ✔ consistent.
* (F4) 14 prime zeros ≤ 8 813 281: they are zeros of R with M₂ > 0 (E₂ = −M₂), not counterexamples to Theorem A, which
  bounds M₂, not R. Any positivity theorem for R would need threshold > 8 813 281; none is claimed. ✔ consistent.
* (F4′) the 38 𝔊*-zeros (`data/z58/screens/gstar_zeros.txt`): recomputed R(p) for all 38 with
  `scripts/z58_tryf2_gstar_check.c` (`data/z58/tryf2/gstar_zeros_R.txt`): 14 have R = 0 (the F4 list) and 24 have R > 0
  (e.g. R(37) = 2, R(1621) = 4, R(564 661 441) = 2). So the full-family statement is not contradicted, and nothing in this
  memo transfers to the restricted family 𝔊*: Theorem A is proved for the full (★) family only; a restricted-family
  surrogate would need its own cutoffs and proof. ✔ consistent.

## §8 Cross-model review (`data/z58/xreview/REVIEW_TRYF2.md`, verdict ACCEPT-WITH-FIXES) — what was fixed

1. §6(ii): the blanket "no per-C or per-parity argument valid down to 10¹⁰" was replaced by the correct statement: only
   arguments that would also prove C-even positivity at all primes ≥ 10¹⁰ are excluded.
2. F4 completed with the 38 𝔊*-zeros (F4′ above; R recomputed by this lane: 14 zeros, 24 with R > 0), and the explicit
   remark that Theorem A does not transfer to restricted families.
3. Prior attribution (per the reviewer's `git grep`; this lane did not read those memos by instruction): the five hit faces,
   the Jacobi/square obstruction, the finite-covering obstruction, the CF dictionary, the "main term + remainder,
   positivity iff remainder > −main" architecture, the C-even/8-p counterexamples, and pointwise square-sensitive log² p
   main-term bounds for other surrogates (genus terms) are PRIOR in the repository (Z56_FAMTRY, Z57_SYNTH, Z56_FAMDESIGN,
   Z57_BFII, Z53_HYP2CYCLE, Z55_CROSSU, Z52_BANKED). What is incremental here: the particular cutoff/pair-corrected
   surrogate M₂ = Σ 4m₂,C/φ(4C), its reciprocal-Kloosterman/Salié box proof (Theorem A), the Λ and M₂ diagnostics, and the
   packaging of the C-divisor Jacobi identity. No comparison with the prior genus terms is proved; Theorem A is an
   alternative main-term proof, not a new reduction of the missing pointwise remainder bound.
4. Headings/claims narrowed: "all dead" → attempted implementations failed; "polynomial identities impossible" → any
   fixed finite menu covering all target primes; Jacobi-script pair count corrected to 32 374 distinct pairs; quantile
   convention and rounding stated in Data 3.1.
5. §3: the no-diagonal parity argument (d = N_C/d impossible) recorded; M₂ explicitly called a surrogate/model main term
   with the tautological nature of the split spelled out.
Net status after the review: Theorem A and the diagnostics stand; **no progress on the required pointwise remainder bound
E₂ > −M₂; no HOT LEAD; ES remains OPEN.**
