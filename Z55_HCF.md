# Z55_HCF — Problem HC (pointwise polylog bound for HC(p)), lane HCF

Brief: `/home/pasky/projects/math/z52bbriefs/z55_tryhard.md`, Problem HC: **prove HC(p) ≤ (log p)^A for every
sufficiently large prime p ≡ 1 (mod 4), for some A.** Scripts `scripts/z55_hcf_*`, data `data/z55/hcf/`.

Notation (from `Z53_UPPER.md` §1). p ≡ 1 (mod 4) prime; a *word* of p is (t, u, v) ∈ ℕ³ with tuv − u − v = p;
𝒞_p := {x ∈ ℕ : x ≡ 0 (mod 4) or x ≡ −p (mod 8)}; HC(p) := least element of 𝒞_p that is a coordinate of a word.
By Z53_UPPER L1.1, for c ∈ 𝒞_p: c is a coordinate ⟺ p + c (line U) or cp + 1 (line T) has a positive divisor
d ≡ −1 (mod c); such a d is a *certificate divisor* for c, and (c, d) a *certificate*. (·/·) is the Jacobi symbol.
For p ≡ 5 (mod 8), HC(p) = 3 (Z53_UPPER P2.1), so everything below concerns p ≡ 1 (mod 8), where
𝒞_p = 4ℕ ∪ (7 + 8ℕ₀). Facts used: L1.1, L1.3 and the reciprocity constraint L3.1 of Z53_UPPER
(every certificate divisor d of p, for c ∈ 𝒞_p with c < p, has (d/p) = −1).

---------------------------------------------------------------------------------------------------------------------

## 0. Verdict

**The target is not proved.** It implies the Erdős–Straus conjecture for all large primes (Z53_UPPER §0, §5.1), and
every route I pushed ends at the same wall: a pointwise statement needs a divisor of one *specific* integer
(p + c or cp + 1, c ≤ (log p)^A) in a *specific* class mod c, and no information about p other than congruences and
"p is not a square" (reciprocity) is available; congruence information is useless by the square-class obstruction, and
the non-square information gives one non-residue prime ℓ_p with no control on which shifted number it divides.

What is proved here (all elementary, all checked numerically):

| # | statement | status |
|---|-----------|--------|
| P1.1 | symmetric criterion for line U: c (2 ≤ c < p) is a u-coordinate ⟺ ∃ v ≥ 1 with cv ∣ p + c + v ⟺ p + c has a divisor ≡ −p (mod c) | PROVED |
| P1.2 | if p + c = s·q with q prime, q ∤ s, then c is certified on line U ⟺ s has a divisor ≡ −1 or ≡ −p (mod c); on line T (cp + 1 = s·q) ⟺ s has a divisor ≡ −1 (mod c) | PROVED, CERTIFIED (39 695 cases) |
| L2.1 | for c ∈ {7, 15} and p ≡ 1 (8): c is a coordinate ⟺ the odd part of p + c or of cp + 1 has a prime factor q with (q/c) = −1 (the reciprocity constraint L3.1 is *sufficient* at these c) | PROVED, CERTIFIED (8 932 cases) |
| **T3.1** | **for every finite set S of primes ≥ 11, every 1 ≤ R < (min S − 1)/3, and every C, Y: infinitely many primes p ≡ 1 (mod 8) with p ≡ R (mod ℓ^{J}) for ℓ ∈ S and p ≡ 1 (mod ℓ′^{a}) for the other primes ℓ′ ≤ Y have no certificate (c, d) with c ≤ C and d supported on S ∪ {primes ≤ Y}** | PROVED, CERTIFIED (§5) |
| C3.2 | no finite family of certificate congruences covers {p ≡ 1 (mod 840), p ≡ R (mod ℓ)} for any prime ℓ ≥ 11 and non-residue R < (ℓ−1)/3 — a class **containing no squares**, on which the Jacobi obstruction alone no longer excludes divisors with an odd power of ℓ | PROVED |
| C3.3 | profinite form: the point (1 at primes ∉ S, R at primes of S) lies in no HC certificate class, for any set S of primes ≥ 11 and R < (min S − 1)/3 (e.g. R = 2, S = all primes ≡ ±3 (mod 8), ≥ 11: a point that is a non-residue at every prime of S) | PROVED |
| P3.4 | (Linnik) for every A there are infinitely many p ≡ 1 (8) that are non-residues modulo every prime ℓ ≡ ±3 (8) in [11, κ′_A log p] and for which every certificate with c ≤ κ_A (log p)^A has a prime factor > κ′_A log p | PROVED |
| §4 | where a proof must use primality; the "square test" of the brief is necessary but not sufficient for *covering-type* arguments (T3.1 gives a second test) | Assessment |

T3.1 is the one new theorem (new in this campaign; no literature search was made). Its proof is elementary (one
page) and uses the Jacobi constraint only to force a prime of S into the certificate divisor; the rest is a
Diophantine analysis of d ≡ −1 (mod c), d ∣ p + c with the small primes pinned. It kills the natural
"small non-residue ⟹ small HC" plan in its covering form: a bound HC(p) ≤ F(ℓ_p) (ℓ_p the least non-residue prime)
proved by a finite certificate family for each value of ℓ_p is impossible — already ℓ_p = 11, p ≡ 2 (mod 11) is
uncoverable — so the GRH route (ℓ_p ≤ 2 log²p, which with a polynomially growing F would give the target) cannot be
completed by coverings. It is the HC analogue of the sterile points of `LORENZINI_W.md` Thm 4.2 /
`BRAINSTORM/bsG_sterile_set.md` (for the (W) families), and it is complementary to Z53_UPPER C3.2 (which needs all
of d's primes to be residues mod p and in exchange needs no bound on c).

---------------------------------------------------------------------------------------------------------------------

## 1. Two reformulations (PROVED)

**Proposition 1.1.** Let 2 ≤ c < p. The following are equivalent: (i) (t, c, v) is a word of p for some t, v;
(ii) ∃ v ∈ ℕ with cv ∣ p + c + v; (iii) ∃ v ∈ ℕ with v ∣ p + c and c ∣ p + v; (iv) p + c has a positive divisor
v ≡ −p (mod c); (v) p + c has a positive divisor d ≡ −1 (mod c).

*Proof.* (i)⟺(ii): tcv − c − v = p ⟺ cv ∣ p + c + v, with t the quotient. (ii)⟹(iii): cv ∣ p + c + v gives
v ∣ p + c and c ∣ p + v. (iii)⟹(ii): g := gcd(c, v) divides v ∣ p + c and c, hence g ∣ p, and g ≤ c < p forces g = 1;
so v ∣ p + c + v and c ∣ p + c + v give cv ∣ p + c + v. (iii)⟺(iv): c ∣ p + v ⟺ v ≡ −p (mod c). (iv)⟺(v): put
d := (p + c)/v, so vd = p + c ≡ p (mod c); since gcd(p, c) = 1, v ≡ −p ⟺ d ≡ −1 (mod c), and v ↦ d is a bijection of the
divisors of p + c. (For c ≥ p nothing is lost: if HC(p) < ∞ then HC(p) ≤ p − 1 by Z53_UPPER L1.2.) ∎

(So on line U the coordinate c has the two *cofactor* descriptions: a divisor in class −1, or in class −p. For the
T line, cp + 1 ≡ 1 (mod c), and the cofactor of d ≡ −1 is again ≡ −1.)

**Proposition 1.2 (prime cofactor).** Let c ∈ 𝒞_p, 3 ≤ c < p, and suppose p + c = s·q with q prime and q ∤ s.
Then c has a certificate divisor on line U iff s has a divisor ≡ −1 (mod c) or a divisor ≡ −p (mod c). If
cp + 1 = s·q with q prime, q ∤ s, then c has a certificate divisor on line T iff s has a divisor ≡ −1 (mod c).

*Proof.* The divisors of sq are the s′ and s′q with s′ ∣ s. s′q ≡ −1 (mod c) ⟺ s′ ≡ −q^{−1}; and q ≡ p s^{−1}
(mod c) on line U (sq ≡ p), so s′q ≡ −1 ⟺ s′ p s^{−1} ≡ −1 ⟺ s/s′ ≡ −p (mod c), and s/s′ runs over the divisors of
s. On line T, sq ≡ 1, so s′q ≡ −1 ⟺ s/s′ ≡ −1 (mod c). ∎

Meaning: when the "unknown" part of p + c is a single prime, whether c is a coordinate is decided by the *known*
part s alone (a congruence condition on p). Any pointwise proof has to beat the configuration "every p + c and cp + 1
(c ∈ 𝒞_p ∩ [3, X]) is (small known part) × (prime)", which no current method excludes for a single p; Prop 1.2 says
that in this configuration HC(p) > X is a pure congruence condition on p, satisfied e.g. by all p in a square class
(§4).

---------------------------------------------------------------------------------------------------------------------

## 2. The 2-adic box at odd c (PROVED)

For odd c ∈ 𝒞_p (c ≡ 7 (mod 8), p ≡ 1 (mod 8)) both p + c and cp + 1 are ≡ 0 (mod 8): the factor 2³ is known.

**Lemma 2.1.** Let p ≡ 1 (mod 8) be prime, p > 15, and c ∈ {7, 15}. Then c is a coordinate of a word of p iff the
odd part of p + c or the odd part of cp + 1 has a prime factor q with (q/c) = −1.

*Proof.* (ℤ/c)^× has order 6 resp. 8; ⟨2⟩ = {1, 2, 4} resp. {1, 2, 4, 8}, which is exactly the kernel K of the
Jacobi character (·/c) (index 2; (2/7) = 1; (2/15) = (2/3)(2/5) = 1 and (·/15) is nontrivial on {7, 11, 13, 14}).
Note (−1/c) = −1 in both cases, so −1 ∉ K and the class −1 lies in the coset −K = {x : (x/c) = −1}.
(⟸) Let N ∈ {p + c, cp + 1}, N = 2^a₀ m with m odd, a₀ ≥ 3, and q ∣ m with (q/c) = −1. Then −q^{−1} mod c lies in
K = ⟨2⟩, so −q^{−1} ≡ 2^a (mod c) for some 0 ≤ a ≤ 3 (ord_c(2) ≤ 4), and d := 2^a q divides N with d ≡ −1 (mod c).
(⟹) If d ∣ N with d ≡ −1 (mod c), write d = 2^a m′ with m′ odd; (m′/c) = (d/c)(2/c)^{−a} = (−1/c) = −1, so some prime
q ∣ m′ ∣ m has (q/c) = −1. ∎

So at c = 7 and c = 15 the reciprocity constraint of Z53_UPPER L3.1 is also *sufficient*: the only obstruction to
c being a coordinate is the absence of a non-residue (mod c) prime factor in the odd parts. Euclid then gives the
classical coverings: the odd part m of p + c satisfies 2^{a₀} m ≡ p (mod c), so (m/c) = (p/c); hence (p/7) = −1 ⟹
HC(p) ≤ 7 and (p/15) = −1 ⟹ HC(p) ≤ 15 (both already contained in the mod-840 covering: (p/15) = (p/3)(p/5)).
For c = 23, 31, 39, 47, … the box {2^a : a ≤ v₂(N)} is in general too small to reach the whole kernel, and the
equivalence genuinely fails: (c, p) = (23, 73), (31, 41), (39, 73), (47, 73) have a non-residue prime factor in an odd
part (5 ∣ 23·73 + 1, 3 ∣ 72, 7 ∣ 112, 5 ∣ 120) but no certificate for c (checked). (The box can occasionally be large enough,
e.g. 2^{10} ∣ 3049 + 23.) The general statement about which non-residue primes can be used is T3.1.

---------------------------------------------------------------------------------------------------------------------

## 3. Theorem N: profinite points that no finite certificate family covers (PROVED)

**Theorem 3.1.** Let S be a nonempty finite set of primes, ℓ₀ := min S ≥ 11, and R an integer with
1 ≤ R < (ℓ₀ − 1)/3 (no quadratic condition on R). Let C ≥ 3 and Y ≥ 2 be arbitrary. Define
  𝒫 := ({primes ≤ Y} ∖ S) ∪ {2}; for ℓ′ ∈ 𝒫 let a(ℓ′) be the least integer with ℓ′^{a(ℓ′)} > C + 1, except
  a(2) := max(3, least a with 2^a > C + 1); M := ∏_{ℓ′ ∈ 𝒫} ℓ′^{a(ℓ′)}; for ℓ ∈ S let J_ℓ be the least integer with
  ℓ^{J_ℓ} > R(C + 1).
Then every prime p > C with p ≡ 1 (mod M) and p ≡ R (mod ℓ^{J_ℓ}) for all ℓ ∈ S satisfies: **no certificate (c, d)
of p with c ∈ 𝒞_p, c ≤ C has d supported on 𝒫 ∪ S** (all prime factors of d in 𝒫 ∪ S). There are infinitely many
such primes (Dirichlet; the class is coprime to M∏ℓ^{J_ℓ}), all ≡ 1 (mod 8).

*Proof.* Let p be such a prime and suppose (c, d) is a certificate with c ∈ 𝒞_p, 3 ≤ c ≤ C, d ≡ −1 (mod c),
d ∣ p + c (line U) or d ∣ cp + 1 (line T), and d = L·s with L := ∏_{ℓ ∈ S} ℓ^{j_ℓ} (j_ℓ ≥ 0), gcd(s, L) = 1, every
prime factor of s in 𝒫.

*Step 1: s ∣ c + 1 and p ≡ 1 (mod s).* Let ℓ′ ∣ s, b := v_{ℓ′}(s), a := a(ℓ′). If b > a then ℓ′^a ∣ d, so
ℓ′^a ∣ p + c resp. cp + 1, and p ≡ 1 (mod ℓ′^a) gives ℓ′^a ∣ c + 1, impossible since 0 < c + 1 ≤ C + 1 < ℓ′^a.
Hence b ≤ a for every ℓ′ ∣ s, so s ∣ M and p ≡ 1 (mod s). Then s ∣ p + c resp. s ∣ cp + 1 gives s ∣ c + 1 in both
cases. Put m := (c + 1)/s ∈ ℕ.

*Step 2: L > 1.* By Z53_UPPER L3.1 (c ∈ 𝒞_p, c < p), (d/p) = −1. For odd ℓ′ ∈ 𝒫, (ℓ′/p) = (p/ℓ′) = (1/ℓ′) = 1
(p ≡ 1 (mod 4) and p ≡ 1 (mod ℓ′)); (2/p) = 1 as p ≡ 1 (mod 8). So (s/p) = 1, and L = 1 would give (d/p) = 1.
Hence L > 1, so L ≥ ℓ₀ ≥ 11.

*Step 3: L ≡ −m (mod c).* From d = Ls ≡ −1 (mod c) and sm = c + 1 ≡ 1 (mod c): L ≡ Lsm ≡ −m (mod c). (★)

*Step 4: c ≡ −R (mod L) on line U, Rc ≡ −1 (mod L) on line T.* Fix ℓ ∈ S with j := j_ℓ ≥ 1 and put
j₀ := min(j, J_ℓ). On line U, p ≡ −c (mod ℓ^{j₀}) and p ≡ R (mod ℓ^{j₀}) give c ≡ −R (mod ℓ^{j₀}); on line T,
cp ≡ −1 gives cR ≡ −1 (mod ℓ^{j₀}). If j > J_ℓ then j₀ = J_ℓ and: (U) c + R > 0 is a multiple of ℓ^{J_ℓ}, so
c ≥ ℓ^{J_ℓ} − R > R(C+1) − R = RC ≥ C; (T) Rc + 1 > 0 is a multiple of ℓ^{J_ℓ}, so Rc + 1 > R(C + 1), c > C. Both
contradict c ≤ C. So j ≤ J_ℓ and the congruence holds modulo ℓ^{j_ℓ} for every ℓ ∈ S; by the Chinese remainder theorem
it holds modulo L.

*Step 5: line U is impossible.* c + R = (i + 1)L for some integer i ≥ 0. Reducing modulo c with (★):
(i + 1)(−m) ≡ R, i.e. (i + 1)m + R ≡ 0 (mod c); as (i+1)m + R ≥ R + 1 > 0, (i + 1)m + R = kc with k ∈ ℕ. Since
m ∣ c + 1, (i+1)m = kc − R divides (i+1)(c+1); put g := (i+1)(c+1)/(kc − R) ∈ ℕ. Then (i+1)(c+1) = g(kc − R), i.e.
  c(gk − i − 1) = i + 1 + gR.                                                                  (†)
The right side is positive, so e := gk − i − 1 ≥ 1; and k ≥ 1 gives g ≤ gk = e + i + 1. Hence by (†)
  ce = i + 1 + gR ≤ i + 1 + R(e + i + 1) = Re + (R + 1)(i + 1),  so  (c − R)e ≤ (R+1)(i+1),  so
  c ≤ R + (R+1)(i+1).
But c = (i+1)L − R. Therefore (i+1)L ≤ 2R + (R+1)(i+1), i.e. L ≤ R + 1 + 2R/(i+1) ≤ 3R + 1 < ℓ₀ ≤ L
(as 3R < ℓ₀ − 1). Contradiction.

*Step 6: line T is impossible.* Rc + 1 = nL for some n ∈ ℕ. Reducing modulo c with (★): n(−m) ≡ 1, so
nm + 1 ≡ 0 (mod c) and nm + 1 = kc with k ∈ ℕ. Since m ∣ c + 1, nm = kc − 1 divides n(c + 1); put
g := n(c+1)/(kc − 1) ∈ ℕ. Then n(c + 1) = g(kc − 1), i.e.
  c(gk − n) = g + n.                                                                            (‡)
So e := gk − n ≥ 1 and g ≤ e + n; hence ce = g + n ≤ e + 2n, (c − 1)e ≤ 2n, c ≤ 2n + 1. But
c = (nL − 1)/R, so nL − 1 ≤ R(2n + 1), L ≤ 2R + (R+1)/n ≤ 3R + 1 < ℓ₀ ≤ L. Contradiction. ∎

Remarks. (a) The hypotheses c ∈ 𝒞_p and c < p enter only through L3.1 (Step 2), which is also the only place where
the primes of 𝒫 are required to be residues mod p (p ≡ 1 (mod ℓ′)); Steps 3–6 are pure arithmetic in (c, d) and
use about the primes of S only p ≡ R (mod ℓ^{J_ℓ}). In particular R may be a residue or a non-residue mod the
primes of S; the non-residue case is the one that the Jacobi obstruction does not already cover (Cor 3.2).
(b) ℓ₀ ≥ 11 is sharp: for S = {ℓ}, ℓ ∈ {3, 5, 7} and R the least non-residue, the admissibility equations of
Steps 5–6 *do* have solutions (ℓ = 3: (c, d) = (4, 3), (4, 15), (7, 6); ℓ = 5: (8, 15), (7, 20); ℓ = 7: (4, 7),
(4, 35); script §5), examples of the certificates appearing in Mordell's mod-840 covering.
(c) The single-prime case S = {ℓ} with (R/ℓ) = −1 gives Steps 2 and 4 in the form "j odd, j ≤ J" (as in the first
version of this memo); the set version costs nothing extra.

**Corollary 3.2 (no finite covering of a non-residue class).** Let ℓ ≥ 11 be prime and R a quadratic non-residue
mod ℓ with 1 ≤ R < (ℓ − 1)/3 (such R exists for every ℓ ≥ 11: R = 2 for ℓ = 11, 13, 19, R = 3 for ℓ = 17, and for
ℓ ≥ 23 the least non-residue n is < √ℓ + 1 ≤ (ℓ−1)/3 — classical: with m := ⌈ℓ/n⌉, 0 < mn − ℓ < n is a residue, so m is a
non-residue, m ≥ n, and n(n−1) < ℓ). For every C ≥ 3 and every finite set 𝒟 ⊂ ℕ there are infinitely many primes
p ≡ 1 (mod 840), p ≡ R (mod ℓ) (so (ℓ/p) = −1) having no certificate (c, d) with c ≤ C and d ∈ 𝒟.

*Proof.* Take S = {ℓ}, Y ≥ 7 at least the largest prime factor of any element of 𝒟, and apply T3.1 (3, 5, 7 ∈ 𝒫,
so p ≡ 1 (mod 3·5·7·8)). ∎

**Corollary 3.3 (profinite form).** Let S be a set of primes ≥ 11 (finite or infinite), ℓ₀ = min S, 1 ≤ R < (ℓ₀−1)/3,
and let x = (x_q)_q ∈ Ẑ = ∏_q ℤ_q be the point with x_q = 1 for q ∉ S and x_ℓ = R for ℓ ∈ S. Then x lies in no
certificate class {n : n ≡ −c (mod d)} or {n : cn ≡ −1 (mod d)} with c ∈ 4ℕ ∪ (7 + 8ℕ₀), c ≥ 3, d ≡ −1 (mod c);
and for every C and finite 𝒟 there is a clopen neighbourhood U of x (the class of T3.1 with S ∩ [1, Y] in place of
S) such that no prime in U has a certificate with c ≤ C, d ∈ 𝒟.

*Proof.* A certificate class containing x is clopen, hence contains all primes p ≡ x (mod M∏_{ℓ ∈ S, ℓ ≤ Y}ℓ^{J_ℓ})
for Y, M, J large; with C ≥ c and Y ≥ the primes of d, T3.1 (applied to S ∩ [1, Y]) excludes them. ∎

**Proposition 3.4 (non-residue-rich primes still need a large prime in every bounded certificate).** Let L₀ be an
admissible Linnik exponent (least prime in a coprime class mod N is ≤ C₀N^{L₀}; L₀ = 5 is admissible, Xylouris 2011).
For every A ≥ 0 there are constants κ_A, κ′_A > 0 and infinitely many primes p ≡ 1 (mod 8) such that
(i) (ℓ/p) = −1 for every prime ℓ ≡ ±3 (mod 8) with 11 ≤ ℓ ≤ Y := κ′_A log p (so p is a non-residue modulo roughly
half of the primes up to κ′_A log p), and
(ii) every certificate (c, d) of p with c ≤ κ_A (log p)^A has a prime factor of d larger than Y.
One may take κ′_A = 1/(L₀(1.02 + 1.26(A + 1))) and κ_A = (κ′_A)^A /2 for large p.

*Proof.* Let Y be large, R := 2, S := {primes in [11, Y]}, 𝒫 = {2, 3, 5, 7}, C := ⌊Y^A⌋ (C := 3 if A = 0), and let
N := M∏_{ℓ∈S} ℓ^{J_ℓ} be the modulus of T3.1. The least power of ℓ′ exceeding C + 1 is ≤ ℓ′(C+1), so
M ≤ 210(C+1)⁴ (2^{a(2)} ≤ 2(C+1) as C ≥ 3) and ℓ^{J_ℓ} ≤ 2ℓ(C + 1). Hence, using C + 1 ≤ 2Y^A,
  log N ≤ log 210 + 4 log(C+1) + θ(Y) + π(Y) log(2(C+1)) ≤ 1.02 Y + 1.26 (Y/log Y)(A log Y + 1.39) + O(A log Y)
       ≤ (1.02 + 1.26A) Y (1 + o(1))
(Rosser–Schoenfeld: θ(Y) < 1.02Y, π(Y) < 1.26 Y/log Y). By Linnik there is a prime p in the class of T3.1 with
p ≤ C₀N^{L₀}, so log p ≤ L₀(1.02 + 1.26A)Y(1 + o(1)), i.e. Y ≥ κ′ log p with κ′ := 1/(L₀(1.02 + 1.26(A+1))) for
Y large; and for A > 0, C = ⌊Y^A⌋ ≥ Y^A/2 ≥ (κ′ log p)^A/2 = κ_A (log p)^A (for A = 0 take κ₀ = 3). (i): p ≡ 2 (mod ℓ) for ℓ ∈ S, and (2/ℓ) = −1 for
ℓ ≡ ±3 (mod 8), so (ℓ/p) = (p/ℓ) = −1 for those ℓ. (ii) is T3.1: a certificate with c ≤ C whose d is supported on
𝒫 ∪ S = {primes ≤ Y} does not exist. Letting Y → ∞ gives infinitely many p (p > N → ∞). ∎

Compare Z53_UPPER P3.3: there, p ≡ 1 (mod 8∏_{ℓ≤Y}ℓ) (a square-like point: all small primes are residues) and the
conclusion holds for *every* c; here p is a non-residue modulo about half of the primes up to Y and the conclusion
holds for c ≤ (log p)^A. The large prime factor q > Y of the certificate divisor is in both cases the entire content
of the certificate, and it is not determined by p modulo any number built from the primes ≤ Y.

**What T3.1 rules out.** The class of squares is the classical sterile set for ES congruence coverings
(Mordell–Schinzel; Z53_UPPER C3.2 in the HC setting: on p ≡ 1 (mod 8m) no certificate divisor is 2m-smooth). On the
class p ≡ R (mod ℓ) with (R/ℓ) = −1, p is a *non*-residue mod ℓ, so (d/p) = −1 is attainable with ℓ ∣ d, and the
Jacobi obstruction only says that ℓ must appear in d to an odd power. T3.1 shows the obstruction persists:
a certificate containing ℓ must satisfy d ≡ −1 (mod c) *and* d ∣ p + c, and with all other prime factors of d forced
into divisors of c + 1 (Step 1), the two conditions have no common solution unless L ≤ 3R + 1. Consequences for the
target problem:
1. "HC(p) ≤ F(ℓ_p)" with ℓ_p the least non-residue prime is **not** provable by a finite certificate family for
   each value of ℓ_p, whatever F: already ℓ_p = 11, p ≡ 2 (mod 11) is uncoverable. So the GRH route (ℓ_p ≤ 2 log²p,
   Ankeny; F of polynomial growth would give the target) cannot be completed by coverings; it would need certificates
   whose divisors involve primes outside every fixed finite set, i.e. factorisation information about p + c or cp + 1
   that is not a congruence condition on p. (T3.1 says nothing about arguments with growing moduli or unbounded
   certificate families.) Prop 3.4 makes this quantitative: even with ≍ log p/log log p small non-residue primes
   at hand, no certificate with c ≤ (log p)^A is built from primes ≤ κ′ log p.
2. For covering-type arguments the brief's "square test" (the argument must fail at odd squares n = m²) is necessary
   but not sufficient: a finite covering must also fail at the profinite points of Cor 3.3, which are not squares
   (with R = 2 and S = {primes ≡ ±3 (mod 8), ≥ 11}, x_ℓ is a non-residue at every ℓ ∈ S). A covering of the class {p ≡ 1 (840), p ≡ 2 (11)} with bounded c
   must use an *unbounded* set of primes in its certificate divisors.

---------------------------------------------------------------------------------------------------------------------

## 4. Where a pointwise proof has to use primality (Assessment; the PROVED parts are cited)

By L1.1 the target is: for large p ≡ 1 (mod 8), some c ∈ 𝒞_p ∩ [3, (log p)^A] has a divisor of p + c or of cp + 1 in
the class −1 (mod c). The available inputs about p and what each gives:

* *Congruences p mod M.* They determine the ℓ-adic valuations of p + c and cp + 1 for ℓ ∣ M up to the precision of M
  (exactly, if M is taken with large enough exponents relative to the valuation in question), hence by Prop 1.2 they
  decide the question when the cofactor of the known part is prime; and the set of p (mod M) on which they force a
  certificate is never everything: the square classes (Z53_UPPER C3.2) and the non-residue points of C3.2 above are
  uncovered for every M. Any argument whose only input is p mod M is dead.
* *p is not a square* (⟺ p is prime, for the purposes of the reciprocity law). Via L3.1 this is the statement that a
  certificate divisor must contain a prime ℓ with (ℓ/p) = −1; the least such ℓ_p is ≤ p^{1/(4√e)+ε} (Burgess), ≤ 2log²p
  under GRH. The information "ℓ_p = ℓ, p ≡ R (mod ℓ)" is again a congruence, and T3.1 says it is not enough.
* *Primality itself* enters the HC problem only through non-squareness (reciprocity, L3.1) and through coprimality
  gcd(p, c) = 1 for c < p (used in P1.1, P1.2, L1.1); the HC lines make sense for every n ≡ 1 (mod 4) coprime to c,
  and the sieve/exceptional-set theorems of Z53_UPPER §4 use primality only through Bombieri–Vinogradov /
  Siegel–Walfisz for the *count* of p. A pointwise argument would need a property of the specific integers p + c,
  cp + 1 that is not a congruence: their factorisation. Prop 1.2 shows the relevant unknown is exactly whether the
  cofactor of the known small part is prime or splits with a factor in a prescribed class; there is no known tool
  that controls this for one given p and (log p)^A shifts.

I therefore record no CONDITIONAL theorem either: every hypothesis I could formulate that implies the target
("some p + c, c ≤ (log p)^A, has a prime factor ≡ −1 (mod c)", "some (p + c)/s_c splits with a factor in class …")
is a stronger sufficient hypothesis of the same pointwise divisor-in-class type, not a recognised conjecture. The
honest status of Problem HC is: it implies ES for all large primes (no converse is established), with the heuristic
margin of §5.4 of Z53_UPPER (true size of the worst case ≍ log p) and the exceptional-set theorems T4.1–T4.3 there.

---------------------------------------------------------------------------------------------------------------------

## 5. Computations (CERTIFIED)

`scripts/z55_hcf_thmN_check.py` → `data/z55/hcf/thmN_check.txt`:
* (a) admissibility equations of T3.1 Steps 5–6: for each ℓ ∈ {3, 5, 7, 11, …, 47}, R the least non-residue, all
  c ≤ 2000 in 4ℕ ∪ (7 + 8ℕ₀), j ∈ {1, 3, 5}, all s ∣ c + 1: solutions of ℓ^j s ≡ −1 (mod c) with c ≡ −R or
  c ≡ −R^{−1} (mod ℓ^j). Result: **0 solutions for every ℓ ≥ 11**; for ℓ = 3, 5, 7 the solutions listed in Remark (b).
* (b) direct test: for ℓ ∈ {11, 13, 17}, Y = 23, C = 40, 20 random primes in the class of T3.1 (moduli ≈ 10^{22});
  every certificate divisor d of every c ≤ 40 (2 071 / 2 399 / 2 291 divisors, found by factoring p + c and cp + 1)
  has a prime factor outside {ℓ} ∪ {primes ≤ 23}. **0 violations.**

`scripts/z55_hcf_thmN_multi.py` → `data/z55/hcf/thmN_multi.txt`: the set form of T3.1 with S = all primes in
[11, Y], R ∈ {2, 3}: (Y, C) = (23, 40), (31, 24), (23, 40); 10 primes each in the class of T3.1 (moduli ≈ 10^{19}–10^{24});
all 1 168 / 1 653 / 1 170 certificate divisors with c ≤ C have a prime factor > Y. **0 violations.** (For R = 2 the
primes are non-residues modulo 11, 13, 19 (, 29).)

`scripts/z55_hcf_lemmas_check.py` → `data/z55/hcf/lemmas_check.txt`: Lemma 2.1 for all p ≡ 1 (8), p < 2·10⁵,
c ∈ {7, 15}: 8 932 cases, 0 mismatches. Prop 1.2 (line U, 4 ∣ c ≤ 64, every prime q ∥ p + c, s = (p+c)/q) for
p < 5·10⁴: 39 695 cases, 0 mismatches.

`scripts/z53_upper_hc.c` (unchanged, rerun with X = 2·10⁹, no reciprocity/sieve checks) → `data/z55/hcf/hc_2e9.txt`:
**HC(p) ≤ 64 for all 49 109 660 primes p ≡ 1 (mod 4), p ≤ 2·10⁹**; the record HC = 64 at p = 21 841 is not beaten
(extends the 10⁸ census of Z53_UPPER §6 by a factor 20). Histogram tail among p ≡ 1 (8): HC = 32: 16, 36: 10, 39: 7,
40: 2, 44: 6, 47: 3, 52: 1, 56: 1, 64: 1. Consistent with the heuristic "worst case ≍ log p" of Z53_UPPER §5.4
(2·10⁹ ≈ e^{21.4}); any A ≥ 1 in the target has a large numerical margin.
