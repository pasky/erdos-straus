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
| **T3.1** | **for every prime ℓ ≥ 11 and every quadratic non-residue R mod ℓ with R < (ℓ−1)/3, and every C, Y: infinitely many primes p ≡ 1 (mod 8), p ≡ R (mod ℓ) have no certificate (c, d) with c ≤ C and d supported on {ℓ} ∪ {primes ≤ Y}** | PROVED, CERTIFIED (§5) |
| C3.2 | no finite family of certificate congruences covers {p ≡ 1 (mod 840), p ≡ R (mod ℓ)} for any prime ℓ ≥ 11 — a class **containing no squares**, on which the Jacobi obstruction alone no longer excludes divisors with an odd power of ℓ; equivalently, the profinite point (1 at all primes ≠ ℓ, R at ℓ) lies in no HC certificate class | PROVED |
| §4 | where a proof must use primality; the "square test" of the brief is necessary but not sufficient for *covering-type* arguments (T3.1 gives a second test) | Assessment |

T3.1 is the one new theorem (new in this campaign; no literature search was made). It kills the natural
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

## 3. Theorem N: a non-residue class that no finite certificate family covers (PROVED)

**Theorem 3.1.** Let ℓ ≥ 11 be a prime and R an integer with 1 ≤ R < (ℓ − 1)/3 and (R/ℓ) = −1 (such R exists for
every ℓ ≥ 11: R = 2 for ℓ = 11, 13, 19, R = 3 for ℓ = 17, and for ℓ ≥ 23 the least non-residue n is < √ℓ + 1 ≤ (ℓ−1)/3 —
classical: with m := ⌈ℓ/n⌉, 0 < mn − ℓ < n is a residue, so m is a non-residue, m ≥ n, and n(n−1) < ℓ).
Let C ≥ 3 and Y ≥ 2 be arbitrary. Define
  𝒫 := {primes ℓ′ ≤ Y, ℓ′ ≠ ℓ} ∪ {2}; for ℓ′ ∈ 𝒫 let a(ℓ′) be the least integer with ℓ′^{a(ℓ′)} > C + 1, except
  a(2) := max(3, least a with 2^a > C + 1); M := ∏_{ℓ′ ∈ 𝒫} ℓ′^{a(ℓ′)}; J := the least integer with ℓ^J > R(C + 1).
Then every prime p > C with p ≡ 1 (mod M) and p ≡ R (mod ℓ^J) satisfies: **no certificate (c, d) of p with
c ∈ 𝒞_p, c ≤ C has d supported on 𝒫 ∪ {ℓ}** (i.e. with all prime factors of d in 𝒫 ∪ {ℓ}). There are infinitely
many such primes (Dirichlet; the class is coprime to Mℓ^J), all ≡ 1 (mod 8) with (ℓ/p) = −1.

*Proof.* Let p be such a prime and suppose (c, d) is a certificate with c ∈ 𝒞_p, 3 ≤ c ≤ C, d ≡ −1 (mod c),
d ∣ p + c (line U) or d ∣ cp + 1 (line T), and d = ℓ^j s with j ≥ 0, gcd(s, ℓ) = 1, every prime factor of s in 𝒫.

*Step 1: s ∣ c + 1 and p ≡ 1 (mod s).* Let ℓ′ ∣ s, b := v_{ℓ′}(s), a := a(ℓ′). If b > a then ℓ′^a ∣ d, so
ℓ′^a ∣ p + c resp. cp + 1, and p ≡ 1 (mod ℓ′^a) gives ℓ′^a ∣ c + 1, impossible since 0 < c + 1 ≤ C + 1 < ℓ′^a.
Hence b ≤ a for every ℓ′ ∣ s, so s ∣ M and p ≡ 1 (mod s). Then s ∣ p + c resp. s ∣ cp + 1 gives s ∣ c + 1 in both
cases. Put m := (c + 1)/s ∈ ℕ.

*Step 2: j is odd.* By Z53_UPPER L3.1 (c ∈ 𝒞_p, c < p), (d/p) = −1. For odd ℓ′ ∈ 𝒫, (ℓ′/p) = (p/ℓ′) = (1/ℓ′) = 1
(p ≡ 1 (mod 4) and p ≡ 1 (mod ℓ′)); (2/p) = 1 as p ≡ 1 (mod 8); (ℓ/p) = (p/ℓ) = (R/ℓ) = −1. Multiplicativity gives
(d/p) = (−1)^j, so j is odd; in particular j ≥ 1.

*Step 3: ℓ^j ≡ −m (mod c).* From d = ℓ^j s ≡ −1 (mod c) and sm = c + 1 ≡ 1 (mod c): ℓ^j ≡ ℓ^j s m ≡ −m (mod c). (★)

*Step 4: j ≤ J.* Put j₀ := min(j, J). On line U, p ≡ −c (mod ℓ^{j₀}) and p ≡ R (mod ℓ^{j₀}) give c ≡ −R (mod ℓ^{j₀});
on line T, cp ≡ −1 gives cR ≡ −1 (mod ℓ^{j₀}). If j > J then j₀ = J and: (U) c + R > 0 is a multiple of ℓ^J, so
c ≥ ℓ^J − R > R(C+1) − R ≥ C; (T) Rc + 1 > 0 is a multiple of ℓ^J, so Rc + 1 ≥ ℓ^J > R(C + 1), c > C. Both contradict
c ≤ C. So j ≤ J and the congruences hold modulo ℓ^j.

*Step 5: line U is impossible.* c + R = (i + 1)ℓ^j for some integer i ≥ 0. Reducing modulo c with (★):
(i + 1)(−m) ≡ R, i.e. (i + 1)m + R ≡ 0 (mod c); as (i+1)m + R ≥ R + 1 > 0, (i + 1)m + R = kc with k ∈ ℕ. Since
m ∣ c + 1, (i+1)m = kc − R divides (i+1)(c+1); put g := (i+1)(c+1)/(kc − R) ∈ ℕ. Then (i+1)(c+1) = g(kc − R), i.e.
  c(gk − i − 1) = i + 1 + gR.                                                                  (†)
The right side is positive, so e := gk − i − 1 ≥ 1; and k ≥ 1 gives g ≤ gk = e + i + 1. Hence by (†)
  ce = i + 1 + gR ≤ i + 1 + R(e + i + 1) = Re + (R + 1)(i + 1),  so  (c − R)e ≤ (R+1)(i+1),  so
  c ≤ R + (R+1)(i+1).
But c = (i+1)ℓ^j − R ≥ (i+1)ℓ − R. Therefore (i+1)ℓ ≤ 2R + (R+1)(i+1), i.e. ℓ ≤ R + 1 + 2R/(i+1) ≤ 3R + 1 < ℓ
(as 3R < ℓ − 1). Contradiction.

*Step 6: line T is impossible.* Rc + 1 = nℓ^j for some n ∈ ℕ. Reducing modulo c with (★): n(−m) ≡ 1, so
nm + 1 ≡ 0 (mod c) and nm + 1 = kc with k ∈ ℕ. Since m ∣ c + 1, nm = kc − 1 divides n(c + 1); put
g := n(c+1)/(kc − 1) ∈ ℕ. Then n(c + 1) = g(kc − 1), i.e.
  c(gk − n) = g + n.                                                                            (‡)
So e := gk − n ≥ 1 and g ≤ e + n; hence ce = g + n ≤ e + 2n, (c − 1)e ≤ 2n, c ≤ 2n + 1. But
c = (nℓ^j − 1)/R ≥ (nℓ − 1)/R, so nℓ − 1 ≤ R(2n + 1), ℓ ≤ 2R + (R+1)/n ≤ 3R + 1 < ℓ. Contradiction. ∎

Remarks. (a) The hypotheses c ∈ 𝒞_p and c < p enter only through L3.1 (Step 2); Steps 3–6 are pure arithmetic in
(c, d). (b) ℓ ≥ 11 is sharp in the sense that for ℓ ∈ {3, 5, 7} the admissibility equations of Steps 5–6 *do* have
solutions (ℓ = 3: (c, d) = (4, 3), (4, 15), (7, 6); ℓ = 5: (8, 15), (7, 20); ℓ = 7: (4, 7), (4, 35); script §5), and
these are examples of the certificates appearing in Mordell's mod-840 covering. (c) The proof does not use that the primes
ℓ′ ≠ ℓ are *residues* mod p in any way beyond Step 2; Step 1 uses only p ≡ 1 (mod ℓ′^{a}), which forces the
ℓ′-part of d to divide c + 1 and so to be bounded.

**Corollary 3.2 (no finite covering of a non-residue class).** Let ℓ ≥ 11 be prime and R as in T3.1. For every
C ≥ 3 and every finite set 𝒟 ⊂ ℕ there are infinitely many primes p ≡ 1 (mod 840), p ≡ R (mod ℓ) (so (ℓ/p) = −1)
having no certificate (c, d) with c ≤ C and d ∈ 𝒟. Profinite form: the point x = (x_q)_q ∈ Ẑ = ∏_q ℤ_q with x_q = 1
for q ≠ ℓ and x_ℓ = R lies in no certificate class {n : n ≡ −c (mod d)} or {n : cn ≡ −1 (mod d)} with
c ∈ 4ℕ ∪ (7 + 8ℕ₀), c ≥ 3, d ≡ −1 (mod c); and for every C and finite 𝒟 there is a clopen neighbourhood U of x
(namely {n ≡ 1 (mod M), n ≡ R (mod ℓ^J)} of T3.1) such that no prime in U has a certificate with c ≤ C, d ∈ 𝒟.

*Proof.* Take Y ≥ 7 at least the largest prime factor of any element of 𝒟 and apply T3.1 (3, 5, 7 ∈ 𝒫, so
p ≡ 1 (mod 3·5·7·8)). For the profinite form: a certificate class containing x would contain all primes
p ≡ x (mod Mℓ^J) for M, J large (it is clopen); choosing C ≥ c and Y ≥ the primes of d, T3.1 excludes them. ∎

**What T3.1 rules out.** The class of squares is the classical sterile set for ES congruence coverings
(Mordell–Schinzel; Z53_UPPER C3.2 in the HC setting: on p ≡ 1 (mod 8m) no certificate divisor is 2m-smooth). On the
class p ≡ R (mod ℓ), p is a *non*-residue mod ℓ, so (d/p) = −1 is attainable with ℓ ∣ d, and the Jacobi obstruction
only says that ℓ must appear in d to an odd power. T3.1 shows the obstruction persists: a certificate containing ℓ must satisfy d ≡ −1 (mod c) *and*
d ∣ p + c, and with all other prime factors of d forced into divisors of c + 1 (Step 1), the two conditions have no
common solution unless ℓ ≤ 3R + 1. Consequences for the target problem:
1. "HC(p) ≤ F(ℓ_p)" with ℓ_p the least non-residue prime is **not** provable by a finite certificate family for
   each value of ℓ_p, whatever F: already ℓ_p = 11, p ≡ 2 (mod 11) is uncoverable. So the GRH route (ℓ_p ≤ 2 log²p,
   Ankeny; F of polynomial growth would give the target) cannot be completed by coverings; it would need certificates
   whose divisors involve primes outside every fixed finite set, i.e. factorisation information about p + c or cp + 1
   that is not a congruence condition on p. (T3.1 says nothing about arguments with growing moduli or unbounded
   certificate families.)
2. For covering-type arguments the brief's "square test" (the argument must fail at odd squares n = m²) is necessary
   but not sufficient: a finite covering must also fail at the profinite points of C3.2, which are not squares.
   A covering of the class {p ≡ 1 (840), p ≡ 2 (11)} with bounded c must use an *unbounded* set of primes in its
   certificate divisors.

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

`scripts/z55_hcf_lemmas_check.py` → `data/z55/hcf/lemmas_check.txt`: Lemma 2.1 for all p ≡ 1 (8), p < 2·10⁵,
c ∈ {7, 15}: 8 932 cases, 0 mismatches. Prop 1.2 (line U, 4 ∣ c ≤ 64, every prime q ∥ p + c, s = (p+c)/q) for
p < 5·10⁴: 39 695 cases, 0 mismatches.

`scripts/z53_upper_hc.c` (unchanged, rerun with X = 2·10⁹, no reciprocity/sieve checks) → `data/z55/hcf/hc_2e9.txt`:
**HC(p) ≤ 64 for all 49 109 660 primes p ≡ 1 (mod 4), p ≤ 2·10⁹**; the record HC = 64 at p = 21 841 is not beaten
(extends the 10⁸ census of Z53_UPPER §6 by a factor 20). Histogram tail among p ≡ 1 (8): HC = 32: 16, 36: 10, 39: 7,
40: 2, 44: 6, 47: 3, 52: 1, 56: 1, 64: 1. Consistent with the heuristic "worst case ≍ log p" of Z53_UPPER §5.4
(2·10⁹ ≈ e^{21.4}); any A ≥ 1 in the target has a large numerical margin.
