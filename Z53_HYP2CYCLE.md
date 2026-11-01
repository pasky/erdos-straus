# Z53_HYP2CYCLE — depth lane HYP2CYCLE: 2-cycles of the remainder map in the balanced block (FRONTIER §7.1, R2)

ES is OPEN. Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Internal results are internally reviewed only (not refereed).

Brief: `z52bbriefs/z53_depth.md`; kickoff: `z52bbriefs/z53_lanes.md` §HYP2CYCLE. Scripts: `scripts/z53_hyp2cycle_*`. Data:
`data/z53/hyp2cycle/` (3.6 MB). Builds on `Z52D_HYPERBOLA.md` (Z52D), `LOWER_TAIL_ASTRA.md`, `LENGTH_THREE.md`,
`DEDEKIND_ES.md` (DK).

## 0. Summary

Fix a prime p and an integer U with 2U < p. Let f be the partial map on (U, 2U] that sends x to the unique y ∈ (U, 2U]
with y ≡ −p (mod x), or to ⊥ if there is none. Z52D Prop 2 shows the balanced (★) block is 2N₄, where N₄ counts the
2-cycles {u, B} of f with 4 | k := (p+u+B)/(uB). R2 asks for N₄ ≪ U^{1−η} at U ≍ p^{1/4}. N₂ counts all 2-cycles, i.e.
the count without the 4-condition.

1. **Main new step. R2 reduces to a second-order equidistribution hypothesis (MIX) that needs only a power saving, not
   beyond-square-root cancellation** (Theorem R; the reduction is PROVED, MIX itself is open).
   * f(f(u)) = u holds exactly when the phase pair (θ_u, θ_{f(u)}), θ_x := {−p/x}, lies on the graph of the Gauss map
     x ↦ 1/x − 1 or of x ↦ 1/(1+x) (Lemma G). Both coordinates lie in (1/f(u))ℤ.
   * Hence N₂ ≪ δU + δ^{−1}U^{ε}·max |W(h)| over 0 < |h₂| ≤ H, |h₁| ≤ H, with H ≍ U^{ε}/δ, where
     W(h) = Σ_{u ∈ dom f} e(−h₁p/u − h₂p/f(u)).
   * If |W| ≤ U^{1−η} on that range, then N₄ ≤ N₂ ≪ U^{1−η/2+ε}. So R2 follows from *any* power saving in a sum of
     ≈ 0.69U terms.
   * EVIDENCE at 10¹², 10¹⁶, 10¹⁸ (29 primes): |W| ≈ 1.0–1.2·√U in rms and ≤ 4.7·√U at the maximum. This is
     square-root size, so MIX holds numerically with η ≈ 1/2, and the conditional exponent would be N₂ ≪ U^{3/4+ε}.
   * This improves the sufficient condition (R1) of Z52D. R1 needs beyond-square-root cancellation in a sum of U² terms,
     and Z52D measured it at 1.4–1.8·√(U²), i.e. failing. MIX is not known to be provable. The standard B-process
     lengthens it, and its double-sum form is beyond classical double-sum bounds (Assessment, §5.3).
2. **The standard determinant method is vacuous for (★) in every block (Prop D; PROVED relative to the cited theorems).**
   * For F = kuB − u − B − p, Heath-Brown's affine Theorem 15 (CIME notes, as restated by Reuss and by Browning–Heath-Brown)
     yields T^ε·exp(2√(Π log B_i/log T)) ≥ min(B_i)^{2/√3} auxiliary polynomials. Annals Theorem 14, applied to the
     homogenisation, yields the same exponent.
   * Both exceed the elementary bound min(B_i)·p^{o(1)} (Z52D Thm 1). This closes Z52D's (R3) in its standard form. The
     reason is that the box is *critical*: V/T = 1, so the expected count is O(1).
3. **Where the 4-condition enters (Lemma B, Prop C, Prop S; PROVED).**
   * The 4-condition adds exactly two 2-adic bits at the even vertex: (★) pairs are the mixed cycles
     u ↦ (−(p+u) mod 4u) ↦ u. In the pair-product model N₄ = N₂/5 and N₅ = (3/4)N₂, where N₅ counts the five-slice
     2-cycles.
   * At p ≡ 1 (4), N₅ is the number of bichromatic 2-cycles. At p ≡ 3 (4) it is the number of *monochromatic* ones
     (PROVED relative to DK Cor 4.1 by a 160-cell check, plus 2.8·10⁵ words).
   * T1 lives in the five-slice layer, not in the 2-cycle count. An explicit infinite family of odd squares m² has
     N₂(m², ⌊√m⌋) ≥ 1 (Prop S), and 14.0 % of odd squares near 10¹² have N₂ > 0. So a lower bound for N₂ is T1-blind.
   * For upper bounds the 4-condition is only a bounded thinning, so N₂ is *not* bounded better than N₄: the trivial
     bound U/2 is the same, and no better bound for either is known.
4. **Dynamics of f is the independent-CRT random map (EVIDENCE).**
   * The means of N₂, N₄ and N₃ (3-cycles), the domain size |dom f|/U → log 2, and the second factorial moments all match
     the model. In particular N₂ is under-dispersed (var/mean 0.989) and N₄ over-dispersed (1.009), exactly as the model
     predicts.
   * Exhaustive scan of all 1.9·10⁸ primes < 4·10⁹: max N₂ = 7 and max N₄ = 5. The tails are consistent with the model,
     and the class mod 64 has no effect.
   * No falsifier of a power saving exists in range. The data look like N₂ ≤ p^{o(1)}.
5. **R2 is irrelevant to ES and to the bound R(p) ≪ p^{1/3+o(1)}** (§6; PROVED facts plus Assessment).
   * It is an upper bound; the block's main term is 0.146 < 1; and the balanced block's trivial bound p^{1/4} is already
     below the cube block's p^{1/3}.

**Verdict: narrowed, with one strengthened sufficient condition.**
* Closed (scoped PROVED): the standard (HB Thm 14/15) determinant method for (★) blocks.
* Located: the 4-condition (2-adic) and T1 (five-slice layer).
* Strengthened: R2′ ⟸ MIX, a square-root-regime hypothesis that holds numerically.
* Recommended: retire R2 from FRONTIER §7.1's ES-relevant list. If kept, keep it as an upper-bound methods test, stated
  via MIX.

## 1. Statements attacked

Notation. n is odd ≥ 5 and U ≥ 1 is an integer with 2U < n. Write e(x) = e^{2πix} and θ_x := {−n/x} = (−n mod x)/x
∈ [0,1). The map f(x) is the unique y ∈ (U, 2U] with y ≡ −n (mod x), or ⊥; dom f := {x ∈ (U,2U] : f(x) ≠ ⊥}. A
*2-cycle* is an unordered pair {u, B} ⊂ (U, 2U] with f(u) = B, f(B) = u and uB | n+u+B; at primes the last condition
is automatic (Z52D Prop 2(b)). Its *level* is k := (n+u+B)/(uB).
* N₂(n,U) := #2-cycles.
* N₄ := #2-cycles with 4 | k. At a prime, the balanced (★) block is N(U,U) = 2N₄ (Z52D Prop 2).
* N₅ := #2-cycles satisfying one of the five slices: 4 | k, 4 | u, 4 | B, 4 | ku − 1, 4 | kB − 1.
* N₃ := #directed 3-cycles x → y → z → x of f (used only as a dynamics statistic).

| statement | content | status here |
|---|---|---|
| **R2** (FRONTIER §7.1, Z52D (R2)) | ∃η > 0: N₄(p,U) ≪ U^{1−η} for all primes p, U ≍ p^{1/4} | OPEN; CONDITIONAL on MIX (Thm R) |
| **R2′** | the same for N₂ (implies R2) | OPEN; CONDITIONAL on MIX (Thm R) |
| **MIX(η)** | \|W(h₁,h₂)\| ≤ U^{1−η} for 0 < \|h₂\| ≤ U^η, \|h₁\| ≤ U^η (§5) | OPEN; EVIDENCE: holds with η ≈ 1/2 numerically |
| **R3** (Z52D) | determinant-method power saving | standard HB form vacuous (Prop D, PROVED rel. cited thms) |
| exact identity / falsifier (kickoff) | — | identities §3 (PROVED); no falsifier exists in range (§4) |
| N₂ vs N₄ (kickoff) | is N₂ better bounded? where does 4 enter? | no; §2 (PROVED + EVIDENCE) |

Trivial bound: N₄ ≤ N₂ ≤ U/2. Each u has at most one partner, and 2-cycles are vertex-disjoint (Z52D Thm 1(a), Prop 2).

## 2. Why this is not already closed; where the 4-condition enters

Z52D closed, as scoped theorems, four *cancellation* implementations on the additive-character side. These are fixed-
conductor dualization, ET/Fejér with max |S_h|, Cauchy–Schwarz in the function variable, and low-conductor or
class-conditioned main terms. R2 is an upper-bound counting statement. It can instead be attacked by algebraic counting
(R3, not attempted in Z52D), by the dynamics of f, or by structural identities. None of these is on the closed list or in
FRONTIER §6.

**Lemma B (the 4-condition is two 2-adic bits; PROVED).** Let {u, B} be a 2-cycle at a prime p.
(a) If u and B are both odd, then k is odd.
(b) Otherwise exactly one of them is even, say u = 2^a u′ with a ≥ 1 and u′, B odd. The 2-cycle condition gives
B ≡ −p (mod 2^a). In addition, 4 | k ⟺ B ≡ −(p+u) (mod 2^{a+2}).
(c) The (★) pairs with u even are therefore exactly the u for which g(u) := the lift into (U,2U] of −(p+u) mod 4u exists
and f(g(u)) = u.

*Proof.* gcd(u, B) = 1 by Z52D Prop 2(b).
(a) uB and p+u+B are both odd.
(b) For u even, 4uB | p+u+B ⟺ 4u | p+u+B and B | p+u+B, since gcd(4u, B) = 1.
* 4u | p+u+B ⟺ B ≡ −(p+u) (mod 4u). Reduced mod u this is B ≡ −p (mod u), i.e. B = f(u). Its extra content beyond
  u | p+B is the class of B mod 2^{a+2}, given B mod 2^a.
* B | p+u+B ⟺ f(B) = u.
(c) 4u > 2U ≥ B, so the lift into (U, 2U] is unique. ∎

**Proposition C (pair-product densities; PROVED for the model).** Let M₂(U) := Σ 1/φ(uB) over coprime pairs U < u < B ≤ 2U.
Let M₄ (resp. M₅) be the same sum weighted by the model probability of 4 | k (resp. of a five-slice). The model is
"p uniform over units mod a common multiple of all 4uB", as in Z52D Cor 4.
(a) M₂(U) = (15/(2π²))(log 2)² + O(U^{−1}log³U) = 0.365090… + o(1).
(b) The both-odd pairs carry M₂/5 + o(1) and the odd-sum pairs carry 4M₂/5 + o(1). In the model k mod 4 is uniform on
{1, 3} for both-odd pairs and on ℤ/4 for odd-sum pairs. Hence M₄ = M₂/5 + o(1) = (3/(2π²))(log 2)² + o(1) = 0.073018…, and
the balanced block's mean is 2M₄ = 3(log 2)²/π². This proves the identification that Z52D §3.3 left as EVIDENCE, for its
M₀.
(c) M₅ = (3/4)M₂ + o(1) and M₄/M₅ → 4/15.

*Proof.*
(a) For coprime u, B, 1/φ(uB) = (uB)^{−1} Σ_{d₁|u, d₂|B} μ²(d₁)μ²(d₂)/(φ(d₁)φ(d₂)). Also
1[(u,B)=1] = Σ_{e|(u,B)} μ(e). Interchanging,
2M₂ = Σ_{d₁,d₂,e} μ²(d₁)μ²(d₂)μ(e)/(φ(d₁)φ(d₂)) · Σ_{u∈I, [d₁,e]|u} u^{−1} · Σ_{B∈I, [d₂,e]|B} B^{−1}, with I = (U, 2U].
* The diagonal u = B contributes nothing, because (u,u) = u > 1.
* Σ_{u∈I, D|u} 1/u = D^{−1}(log 2 + O(D/U)) for D ≤ 2U, and = 0 for D > 2U.
* The series Σ |μ²μ²μ|/(φ(d₁)φ(d₂)[d₁,e][d₂,e]) converges: summing over d₁ gives ≪ (log 2e)/e, and Σ_e (log e/e)² < ∞.
  Its tails beyond U, and the O(D/U) errors, are O(U^{−1}log³U).
* The Euler factor at ℓ is (1 + 1/(ℓ(ℓ−1)))² − (1/ℓ²)(ℓ/(ℓ−1))² = 1 + ℓ^{−2}.
* So 2M₂ = (log 2)² ζ(2)/ζ(4) + O(U^{−1}log³U), and ζ(2)/ζ(4) = 15/π².

(b) Restricting u, B to be odd replaces Σ_{u∈I, D|u} 1/u by (2D)^{−1}(log 2 + O(D/U)) for odd D, and by 0 for even D.
The Euler factor at 2 becomes (1/2)² = 1/4 instead of 1 + 1/4. So both-odd = M₂·(1/4)/(5/4) = M₂/5. Coprime pairs
cannot both be even.
* Model probabilities. P(p ≡ −(u+B) (mod uB) and k ≡ c (mod 4)) = P(p ≡ cuB − u − B (mod 4uB)). This equals
  1/φ(4uB) if cuB − u − B is odd, and 0 otherwise; the residue is automatically prime to uB.
* Both-odd pairs: odd ⟺ c odd, and φ(4uB) = 2φ(uB), so c ∈ {1, 3} each carries 1/(2φ(uB)).
* Odd-sum pairs: every c is allowed, and φ(4uB) = 4φ(uB), so each c carries 1/(4φ(uB)).
* Hence M₄ = (1/4)·(4/5)M₂ = M₂/5.

(c) Slice membership given (u mod 4, B mod 4, c):
* Both-odd pairs: no letter is divisible by 4, and ku ≡ 1 (4) ⟺ c ≡ u (4) (u odd). So a slice holds unless
  c ≢ u, B (mod 4). The fraction is 1 if u ≢ B (mod 4) and 1/2 otherwise.
* Odd-sum pairs, u even: if 4 | u a slice holds. If u ≡ 2 (4) the slices are c = 0, or c odd with c ≡ B (4), giving
  fraction 2/4.
* Weights. By the computation of (a) with congruence-restricted inner sums, the odd classes mod 4 carry equal weight.
  The weight of v₂(u) = a among even u is ∝ 2^{−a−1}·2 (density times the 2-part of u/φ(u)), so P(4 | u | u even) = 1/2.
* Both classes therefore average 3/4. ∎

**EVIDENCE (match).** The scans (Lemma A cross-check in §3) give E N₂ = 0.3647 / 0.3664 / 0.3636 / 0.3545 at
10⁸ / 10¹² / 10¹⁶ / 10¹⁸. The model at the same U gives 0.3638 / 0.3649 / 0.3651 / 0.3651 (`…_model.c`). E N₄ and E N₅
match (table below). Exhaustive means for all primes in [10⁹, 4·10⁹): E N₂ = 0.36363, E N₄ = 0.07277.

| sample (U = ⌊n^{1/4}⌋) | E N₂ | E N₅ | E N₄ | E[k≡2 (4)] | E[u+B odd] | P(N₂>0) | P(N₄>0) |
|---|---|---|---|---|---|---|---|
| 2·10⁵ primes from 10⁸ | 0.3647 | 0.2737 | 0.0732 | 0.0730 | 0.2918 | 0.309 | 0.070 |
| 10⁵ primes from 10¹² | 0.3664 | 0.2755 | 0.0749 | 0.0722 | 0.2928 | 0.308 | 0.072 |
| 2·10⁴ primes from 10¹⁶ | 0.3636 | 0.2706 | 0.0722 | 0.0751 | 0.2923 | 0.305 | 0.070 |
| 10⁴ primes from 10¹⁸ | 0.3545 | 0.2635 | 0.0690 | 0.0739 | 0.2885 | 0.296 | 0.066 |
| 10⁵ odd squares m², m ≈ 10⁶ (+2j) | 0.1507 | 0 | 0 | 0.0612 | 0.1203 | 0.140 | 0 |
| 4·10⁴ odd squares, m ∈ [10⁴, 9·10⁴] | 0.1512 | 0 | 0 | 0.0599 | 0.1211 | 0.140 | 0 |
| 10⁵ random odd n ∈ [10¹², 10¹²+10⁹] | 0.2981 | 0.2236 | 0.0594 | 0.0605 | 0.2378 | 0.257 | 0.057 |

**Proposition C′ (five-slice layer = a Jacobi colour condition).** Let n ≡ 1 (4) be prime. A 2-cycle is five-slice ⟺ it is
bichromatic, (u/n) ≠ (B/n). This is LOWER_TAIL_ASTRA Lemma 2.2 with DK Thm 4.5, which cover all length-3 words, including
interior 2-cycles.
* *Companion for n ≡ 3 (4); PROVED relative to DK Cor 4.1.* For a word with n ≡ 3 (4) and unit A = tu − 1:
  five-slice ⟺ (A/n) = +1. At primes p ≡ 3 (4) this means monochromatic.
  * By DK Cor 4.1, (A/n) is a function of (t,u,v) mod 8. `scripts/z53_hyp2cycle_cells3mod4.py` checks all 160 cells with
    n ≡ 3 (4): 0 mismatches.
  * It also checks all 283 977 words with n ≤ 30 000, n ≡ 3 (4) and gcd(A, n) = 1 by direct Jacobi symbols: 0 mismatches.
* In the scans: N₅ = #bichromatic at all 149 869 primes ≡ 1 (4), and N₅ = #monochromatic at all 150 131 primes ≡ 3 (4).
  Possibly already known; not used below.

**Proposition S (N₂ is T1-blind; PROVED).**
* *Construction.* Let q ≡ 1 (mod 4) be a prime ≥ 11. Let a ∈ (q/2, q) satisfy a² ≡ −1 (mod q); one of the two roots lies
  there. Put m := (q+1)(a−1) + 1 and n := m².
* *Claim.* m is odd, U := ⌊n^{1/4}⌋ = ⌊√m⌋ satisfies U < q < q+1 ≤ 2U, and {q, q+1} is a 2-cycle of n at scale U. Its level
  k is ≢ 0 (mod 4), and in fact N₄ = N₅ = 0. So infinitely many odd squares have N₂(n, ⌊n^{1/4}⌋) ≥ 1.

*Proof.*
* m is odd because q + 1 is even.
* m ≡ 1 (mod q+1), so q+1 | m − 1 | m² − 1. Also m ≡ a (mod q), so q | m² + 1.
* Hence q | n + 2q + 1 and q+1 | (m² − 1) + 2(q+1) = n + 2q + 1. Since gcd(q, q+1) = 1, q(q+1) | n + q + (q+1).
* Sizes. From a ∈ (q/2, q), m ∈ ((q+1)(q/2 − 1) + 1, q²), so √m ∈ (q/√2 − 1, q). Thus U ≤ √m < q, and
  2U ≥ 2(√m − 1) > √2·q − 4 ≥ q + 1 for q ≥ 13. The case q = 13 is checked directly; the script asserts U < q and
  q + 1 ≤ 2U for every listed q.
* 4 ∤ k and N₅ = 0 follow from T1 at odd squares.
  * PARITY_AUDIT Lemma 3.2 gives no (★) at squares.
  * For the five slices: n ≡ 1 (8) and every unit is a square mod n, so all edges are monochromatic, and DK Thm 4.5 applies.

CERTIFIED (`scripts/z53_hyp2cycle_sqfamily.py 20000` + `…_scan.c`): all 1 124 squares with q < 20 000 have N₂ ≥ 1 and
N₄ = N₅ = 0. ∎

*Reading.* T1 kills the 4-condition and the whole five-slice (QR) layer, but not the 2-cycles themselves: about 14 % of odd
squares have one. So
* a lower bound for N₂, i.e. one with no 4- or QR-input, is false as an ES tool;
* for upper bounds the 4-condition is a bounded thinning (N₄ ≤ N₂, ratio → 1/5 in the model), so R2 and R2′ are equally
  hard for counting methods.

The ES-relevant content of the 4-condition is the two 2-adic bits of Lemma B on top of the QR colour condition (Prop C′).
That is FRONTIER §4 item 9 ("class, not parity") in its smallest form: the colour fixes the five-slice union, and the
2-adic bits pick (★) inside it.

## 3. Exact forms of the 2-cycle count (PROVED)

The continued-fraction form is already known and is not redone. 2-cycles at level k are HJ words
n/(kB−1) = [[u, k, B]], equivalently n/(kB−1) = [u−1; 1, k−2, 1, B−1] (LENGTH_THREE Prop 1.1, DK Lemma 1.1), with
u, B ∈ (U, 2U]. Equivalently they are the SL₂ matrices [[ku−1, n],[k, kB−1]].

**Lemma A (level form).** Suppose every level occurring in the block exceeds 4U. This holds if n ≥ 16U³, since
k > n/(4U²); for U = ⌊n^{1/4}⌋ it holds for n ≥ 2¹⁶. Then {u,B} ↦ k is injective, and

  N₂(n,U) = #{k : s_k := (−n mod k) ∈ (2U, 4U], D_k := s_k² − 4(n + s_k)/k = w² with w ∈ ℤ_{≥1}, (s_k ± w)/2 ∈ (U, 2U]}.

N₄ is the sub-count with 4 | k.

*Proof.*
* Forward. kuB = n + s with s := u+B ∈ (2U, 4U], so s ≡ −n (mod k). Since s ≤ 4U < k, s = s_k. Then uB = (n+s_k)/k, and
  u, B are the roots of X² − s_kX + uB, whose discriminant is (B−u)² = D_k; w ≥ 1 because u ≠ B.
* Converse. Such k, w give integers u, B (w ≡ s_k mod 2, since D_k ≡ s_k² mod 4) with kuB − u − B = n.
* Two 2-cycles with the same level share s_k and uB, hence coincide. ∎

CERTIFIED cross-check (`…_levelform.c`): per-prime equality with the direct count at 3 000 primes from 10¹² and 3 000 from
10⁸.

*Reading.* The first filter E1 = {s_k ∈ (2U, 4U]} passes ≈ 4 log 2·U = 2.77U levels; measured 2.76U at 10¹² and 10⁸. The
second filter is a square condition of probability ≍ 1/U.
* Lenstra's theorem (Math. Comp. 42 (1984): at most 11 divisors ≡ r mod s when s > n^{1/3}; checked from the source by the
  literature subagent) would give at most 11 divisors per level once k > (kn+1)^{1/3}, i.e. k² > n. The balanced block sits
  exactly at that threshold (k ≍ √n).
* Lemma A already gives at most one pair per level, so Lenstra adds nothing.

**Strip and fixed-difference forms.**
* Strip form: N₂ = #{(k, m) ∈ ℤ² : s := km − n ∈ (2U, 4U], s² − 4m = □, …}. These are lattice points in the hyperbolic
  strip n + 2U < km ≤ n + 4U, i.e. the Dirichlet-divisor geometry, with a square condition on top.
* Fixed-difference form: with w = B − u, N₂ = Σ_{w≥1} #{u : u | n + w, (u + w) | n − w, u, u+w ∈ (U,2U]}.
* Both are restatements: substitute m = uB, s = u + B. All three forms make R2 a count of rare events (≈ 1/U each)
  among ≍ U candidates. None has an obvious cancellation.

## 4. Dynamics of f: it is the independent-CRT random map (EVIDENCE)

Model (Prop C setting): p uniform over units modulo a common multiple of all moduli.
* E|dom f| = Σ_x #{y ∈ (U,2U] : (x,y)=1}/φ(x) → U log 2.
* E N₂ = M₂.
* E N₃ = Σ_{x<y<z pairwise coprime} 2/φ(xyz). Pairwise coprimality is forced at primes: g = (x,y) divides p.
* Second factorial moments: P(both) = 1[a₁ ≡ a₂ mod g]/φ(lcm) for two pairs (`…_pairmoment.c`).

| quantity | model U=100 | primes 10⁸ (U=100) | model U=1000 | primes 10¹² (U=1000) |
|---|---|---|---|---|
| \|dom f\|/U | 0.6968 | 0.6968 | 0.6932 | 0.6931 |
| E N₂ | 0.3638 | 0.3647 | 0.3649 | 0.3664 |
| E N₄ | 0.0726 | 0.0732 | 0.0730 | 0.0749 |
| E N₃ (3-cycles) | 0.0939 | 0.0927 | 0.0924 | 0.0929 |

| dispersion (var/mean) | model U = 100 | model U = 200 | all primes [10⁹, 4·10⁹) (U = 178…251) |
|---|---|---|---|
| N₂ | 0.976 | 0.988 | 0.989 |
| N₄ | 1.0125 | 1.0113 | 1.009 |

* The model predicts the slight under-dispersion of N₂ (the odd part of gcd(q₁,q₂) gives a factor φ(g)/g < 1) and the
  over-dispersion of N₄ (2-adic compatibility). The class mod 64 has no effect: all 32 classes have var/mean(N₄) ∈
  [1.006, 1.011] (`data/z53/hyp2cycle/ms10c_classes.txt`). An earlier attribution of the excess to class mixing was
  tested and is false.
* *Exhaustive scans* (`…_maxsearch.c`, segmented sieve; all primes):

| range | primes | N₂ histogram 0/1/2/…/max | N₄ histogram |
|---|---|---|---|
| [5, 10⁸) | 5 761 453 | 3992175/1489500/251909/25873/1872/122/2 (max 6) | …/433/8 (max 4) |
| [10⁸, 10⁹) | 45 086 079 | 31268483/11541595/2029314/227166/18349/1098/70/4 (max 7) | max 5 (2 primes) |
| [10⁹, 4·10⁹) | 139 114 278 | 96507873/35491903/6319531/729037/61590/4132/199/13 (max 7) | max 5 (8 primes) |
| odd composites < 10⁸ | 44 238 545 | max 6 | max 5 |

  * Against Poisson with the empirical mean, the N₂ tail is *thinner* (61 590 vs 70 451 at N₂ = 4) and the N₄ tail
    *fatter* (273 vs 151 at N₄ = 4). This is consistent with the second moments above, which the CRT model reproduces.
  * **No falsifier of a power saving exists in range.** max N₂ = 7 among 1.9·10⁸ primes, and max N₂ ≤ 6 at 10¹²–10¹⁸ in
    the samples. The growth looks like p^{o(1)}, as in the Poisson model. Constructions of p with many 2-cycles need
    p ≡ −(u_i+B_i) (mod u_iB_i) for many pairs, i.e. prime moduli ≳ p^{1/2}. Assessment: beyond BV-level, and
    sub-power at best.
* *Controls.*
  * FRONTIER §4 item-14 test primes (`data/z53/hyp2cycle/controls.json`): N₂(p, ⌊p^{1/4}⌋) ∈ {0, 1}, N₄ = 0 at all 13.
    These primes are (★)-failures, so every block has N₄ = 0.
  * Near-4th-powers p = U₀⁴ + c, c ≤ 40 (the U-scale analogue of near-squares): 596 primes at 10¹² give E N₂ = 0.324 and
    max 4; 116 primes at 10¹⁶ give 0.388 and max 3. No anomaly. Their structured residues (−p mod (U₀+t) =
    U₀ + t − t⁴ − c) affect only ≈ U^{1/4} values of u.
  * Odd squares: see the table in §2.
* *First order.* |dom f| = U log 2 + O(U^{1−1/15}) uniformly for U ≍ p^{1/4}: the 4th-derivative test for Σ e(hp/u) plus
  Erdős–Turán. This is standard (Z52D (R2) remark) and is not used.

**Reading (Assessment).** At every tested statistic, f behaves as a random partial map whose edge probabilities are the
CRT densities. The functional graph is a forest with rare short cycles. No hidden dynamical structure (CF/Farey/Gauss) is
visible beyond Lemma G below. Fixed-p continued-fraction dynamics sees cylinders, which are intervals in d, so their first-
order statistics are trivial. Joint prefix/suffix cylinders of p/d are boxes on the modular hyperbola dd̄ ≡ ±1 (mod p), at
the Weil scale (Z52D (E5)). The 2-cycle event itself is *exact termination* of p/d's continued fraction at length 5, a
divisor event. Transfer-operator (Vallée) methods average over the numerator; at fixed p no such tool reaches events of
probability ≍ 1/U.

## 5. Main result: R2 reduces to a power-saving second-order equidistribution (Theorem R)

### 5.1 The Gauss-map form of a 2-cycle

**Lemma G (PROVED).** Let n be odd, 2U < n, and u ∈ dom f, B = f(u).
* Either B = uθ_u (branch j = 0; this happens iff θ_u > U/u, and then B < u),
* or B = u(1 + θ_u) (branch j = 1; iff θ_u ≤ (2U−u)/u, and then B > u).
The two branch sets are disjoint. Moreover

  f(B) = u  ⟺  θ_B = Γ_j(θ_u),  with Γ₀(x) = 1/x − 1 (the Gauss map on (1/2, 1)) and Γ₁(x) = 1/(1+x),

and both sides lie in (1/B)ℤ.

*Proof.*
* B ≡ −n (mod u), so B = uθ_u + ju with j ∈ {0,1}, because uθ_u ∈ (0, u), U < B ≤ 2U and u > U. The branch conditions
  are B > U for j = 0 and B ≤ 2U for j = 1. Disjointness: (2U − u)/u < U/u since u > U.
* f(B) = u ⟺ u ≡ −n (mod B), because u ∈ (U, 2U] and the lift is unique ⟺ θ_B = {u/B}.
* For j = 0, u/B = 1/θ_u ∈ (1, 2), since B > U ≥ u/2. So {u/B} = 1/θ_u − 1.
* For j = 1, u/B = 1/(1+θ_u) ∈ (1/2, 1).
* θ_B = (−n mod B)/B and {u/B} both have denominator B. ∎

So 2N₂(p, U) = #{u ∈ dom f : (θ_u, θ_{f(u)}) ∈ Graph Γ₀ ∪ Graph Γ₁} at primes. The u-variable has absorbed the first
divisibility u | p + B exactly, which is the "dynamics" step. What remains is one point of the torus per u and a target
curve. Its δ-neighbourhood has area ≍ δ, and the exact target has width ≍ 1/U.

### 5.2 Theorem R

For h = (h₁, h₂) ∈ ℤ² put **W(h) := Σ_{u ∈ dom f} e(h₁θ_u + h₂θ_{f(u)}) = Σ_{u ∈ dom f} e(−h₁p/u − h₂p/f(u)).**

**Theorem R (PROVED).** For every ε > 0 and A > 0 there are constants C, C′ such that, for every prime p, integer U ≥ 2
with 2U < p, and 0 < δ ≤ 1/2, with H := C′U^{2ε}/δ,

  N₂(p, U) ≤ CδU + CU^{3ε}δ^{−1}·max_{0<|h₂|≤H, |h₁|≤H} |W(h)| + C·U^{−A}.

*Corollary (CONDITIONAL on MIX(η)).* Suppose |W(h)| ≤ U^{1−η} for all 0 < |h₂| ≤ U^{η}, |h₁| ≤ U^{η}. Take δ = U^{−η/2}
(so H ≤ U^{η} for ε < η/8 and U large). Then N₄ ≤ N₂ ≪_ε U^{1−η/2+3ε}. So R2′, hence R2, holds.

*Proof.*
(1) *Majorant.* Fix ψ ∈ C_c^∞(−2, 2), ψ ≥ 0, ψ = 1 on [−1, 1]. Fix ρ₀ ∈ C_c^∞(0.4, 1.1) with ρ₀ = 1 on [1/2, 1], and
ρ₁ ∈ C_c^∞(−0.1, 1.1) with ρ₁ = 1 on [0, 1]. On supp ρ_j the curves Γ₀(x) = 1/x − 1 and Γ₁(x) = 1/(1+x) are smooth with
|Γ_j′| ≤ G := 7 and all derivatives bounded. Put
  χ(x, y) := Σ_{j=0,1} Σ_{(n₁,n₂)∈ℤ²} ψ((y + n₂ − Γ_j(x + n₁))/δ)·ρ_j(x + n₁),
a smooth, nonnegative, ℤ²-periodic function. If (x, y) ∈ [0,1)² with x in the relevant branch interval and y = Γ_j(x),
then χ(x,y) ≥ 1. By Lemma G, 2N₂ ≤ Σ_{u ∈ dom f} χ(θ_u, θ_{f(u)}).

(2) *Fourier coefficients.* Unfolding the periodisation,
χ̂(h) = Σ_j δψ̂(δh₂)·J_j(h), with J_j(h) := ∫_ℝ ρ_j(x)e(−h₁x − h₂Γ_j(x))dx.
* |ψ̂(ξ)| ≪_A (1+|ξ|)^{−A}.
* |J_j| ≤ 1.2.
* If |h₁| ≥ 2G|h₂| + 1, the phase derivative has size ≥ |h₁|/2. Then A-fold integration by parts gives
  |J_j| ≪_A ((1+|h₂|)/|h₁|)^{A}.
* χ̂(h₁, 0) are the Fourier coefficients of χ₀(x) := ∫₀¹χ(x,y)dy = δ‖ψ‖₁(ρ₀ + ρ₁)(x) ≤ 3δ.

(3) *Expansion.* Σ_u χ(θ_u, θ_{f(u)}) = Σ_u χ₀(θ_u) + Σ_{h₂≠0}Σ_{h₁} χ̂(h)W(h).
* The first sum is ≤ 3δ|dom f| ≤ 3δU. W(h₁, 0) is never needed: it carries the domain's main term.
* In the second sum, split the frequencies.
  * |h₂| > U^{ε}/δ: |ψ̂| ≪ U^{−εA′}, and with |W| ≤ U this is ≪ U^{−A} after summing.
  * |h₂| ≤ U^{ε}/δ and |h₁| > U^{ε}(2G|h₂|+1): the J-tail is ≪ U^{−εA′}, again negligible.
  * The remaining (h₁, h₂) number ≪ U^{2ε}δ^{−2}, all with |h₁|, |h₂| ≤ H, and each has |χ̂(h)| ≤ 2.4δ. This gives
    ≪ U^{2ε}δ^{−1}·max|W|. ∎

### 5.3 Status of MIX, and comparison with Z52D's R1

* **EVIDENCE** (`scripts/z53_hyp2cycle_mix.c`; `data/z53/hyp2cycle/mix_*.txt`). |W(h)| normalised by √|dom f| over all
  (h₁, h₂) with h₂ ≠ 0 and |h_i| ≤ H:

| sample | U | H | rms \|W\|/√\|dom f\| | max (over ≈ (2H+1)H freq.) | rms on h₁ = 0 |
|---|---|---|---|---|---|
| 20 primes from 10¹² | 1000 | 20 | 1.024 (mean) | 4.71 | 1.94 |
| 6 primes from 10¹⁶ | 10⁴ | 10 | 1.00–1.10 | 4.06 | 1.86–2.49 |
| 3 primes from 10¹⁸ | 31622 | 6 | 1.17–1.22 | 4.12 | 2.38–2.64 |
| 10 near-4th-power primes ~10¹² | ~1000 | 20 | 0.99–1.06 | 4.69 | 1.46–2.29 |
| 20 odd squares ~10¹² (control) | 1000 | 20 | 0.99–1.08 | 4.94 | 1.62–2.48 |

  * |W| is square-root size: |W| ≈ √U up to a slowly varying factor. The h₁ = 0 column, Σ_r d_U(p+r)e(−h₂p/r), carries
    the variance of the preimage weights d_U.
  * W(h₁, 0), the first-order sum over the domain, is *not* small: |W|/√|dom f| = 5.7, 17.2 and 30.8 at U = 10³, 10⁴ and
    3·10⁴, i.e. ≍ U^{1/2}·√U. Theorem R avoids it.
  * So MIX holds numerically with η ≈ 1/2. The conditional output would then be N₂ ≪ U^{3/4+ε}, far above the true size
    p^{o(1)} but a power saving.
* **Comparison.** Z52D Thm 6(c) needs Δ_H ≤ (UV)^{1/2−η} for the 2D sums S_h over all U² pairs. That is beyond-square-root
  cancellation (R1), and Z52D measured |S_h| ≈ 1.4–1.8·U at 10¹², i.e. R1 fails numerically. MIX needs only a power
  saving in a sum of ≈ 0.69U terms. Lemma G solves the first divisibility exactly instead of Fourier-expanding it, which
  removes one dimension. The target then has the "expected" width 1/U, and square-root cancellation suffices with room.
* **Why MIX is not provable by the standard tools (Assessment).**
  * W is a sum over the lattice points (u, a) of the thin strip U < ua − p ≤ 2U, of e(−h₁p/u − h₂p/(ua − p)). Its phase
    has rank-one-plus-small Hessian in (u, a), and a-derivative ≍ h₂U³ across a strip of a-width < 1.
  * Poisson in a, or Fourier expansion of the h₂-factor in θ_u, produces ≍ h₂U³ dual frequencies with amplitudes
    ≍ (h₂U³)^{−1/2}. That is a double exponential sum of ≍ h₂U⁴ terms which must be bounded by U^{1−η}(h₂U³)^{1/2} ≈
    U^{2.5−η}, against a square-root size of U².
  * Classical double-sum bounds of the shape (MN)^{1/2}F^{1/6} with F ≍ U⁷ give ≈ U^{3.2}: not enough. (Rough order-of-
    magnitude check, not a theorem.)
  * Equivalently, h₁ = 0 gives Σ_{r∈(U,2U]} d_U(p+r)e(−h₂p/r). This is a divisor sum over an interval of length p^{1/4},
    twisted by a smooth phase in the *multiple*. Even the untwisted short-interval divisor problem is open at length
    x^{1/4} for the full divisor function (Huxley's exponent ≈ 0.315). The restriction d ∈ (U, 2U] makes the untwisted
    count first-order, but the twist makes it second-order again.

## 6. Why R2 cannot serve ES (or the global upper bound)

PROVED facts with an Assessment reading.
1. R2 and R2′ are upper bounds, and N₄ ≥ 0 trivially. Any upper bound is consistent with N₄ = 0, which happens for ≈ 93 %
   of primes (Z52D §4 (R4); 92.8 % at 10¹²).
2. Even an asymptotic N₄ = M₄ + O(U^{1−η}) carries no positivity: M₄ → 0.073 < 1 (Prop C).
3. For the global bound, R(p) ≤ Σ_blocks N(U, V) with N(U,V) ≤ p^{o(1)}·min(U, V, p/(UV)) (Z52D Thm 1). That is maximised
   at the cube block U = V = p^{1/3}. The balanced block's trivial bound p^{1/4} is already smaller, so improving it does
   not improve R(p) ≪ p^{1/3+o(1)}.
4. T1 (Prop S) and the counting methods (Prop D, Thm R) are blind to the 4-condition and to the QR layer. They bound N₂, and
   N₂ is positive at infinitely many odd squares.

**Assessment.** FRONTIER §7.1's phrase "even a weak power saving would be the first class-aware single-integer input"
does not apply to R2. A power saving for one balanced block can be (conditionally, Thm R) class-blind, and it is in any
case ES-inert. R2 is worth keeping only as a methods test (MIX).

## 7. Proposition D: the determinant method is vacuous for (★) blocks

**Cited input.**
* (HB15) Heath-Brown, CIME notes (LNM 1891, 2006), Theorem 15, as restated in T. Reuss's thesis (Oxford 2015), Thm 2, and
  in Browning–Heath-Brown, Math. Z. 2005, eq. (3). The CIME chapter itself was paywalled; the two restatements are
  consistent.
  * Statement: for F ∈ ℤ[x₁,…,x_n] absolutely irreducible of degree d ≥ 2 and B_i ≥ 2, with T = max ∏B_i^{e_i} over the
    monomials of F, the points with |x_i| ≤ B_i lie on the zero sets of
    k ≪_{n,d,ε} T^ε exp{(n−1)(∏ log B_i/log T)^{1/(n−1)}}(log‖F‖)^{2n−3} auxiliary polynomials of degree ≤ D(n,d,ε) not
    divisible by F.
* (HB14) Heath-Brown, Annals 155 (2002), Theorem 14 (projective, weighted boxes; checked in arXiv math/0405392 by the
  literature subagent): k ≪ (V^d/T)^{d^{−(n−1)/(n−2)}}V^ε(log‖F‖)^{2n−3}, with V = ∏B_i.

**Proposition D (PROVED relative to HB15 / HB14).** Let F = kuB − u − B − p, which is absolutely irreducible, linear in
each variable. For any box 2 ≤ B₁, B₂, B₃ (for u, B, k), and any translate of it, the number of auxiliary polynomials
supplied by HB15 is at least min(B_i)^{2/√3}. The number supplied by HB14 for the homogenisation
F^h = kuB − uz² − Bz² − pz³ with box (B₁, B₂, B₃, 1) is ≪ V^{2/3^{3/2}+ε}, and V^{2/3^{3/2}} ≥ min(B_i)^{2/√3}. In the
block (U,2U] × (V,2V] × levels, min(B_i) ≍ min(U, V, p/(UV)). So the bound obtainable from either theorem, which is at
least the number of auxiliary curves, exceeds the elementary bound p^{o(1)}·min(U, V, p/(UV)) (Z52D Thm 1) by a power
whenever min(B_i) ≥ p^{ε}.

*Proof.*
* The monomial kuB occurs, and B₁B₂B₃ dominates B₁, B₂ and 1, so T = B₁B₂B₃. Translation x_i ↦ x_i + c_i keeps the
  monomial x₁x₂x₃ with coefficient 1, so T ≥ ∏B_i still.
* With b_i = log B_i and b₁ ≤ b₂ ≤ b₃: ∏b_i/Σb_i ≥ b₁b₂b₃/(3b₃) ≥ b₁²/3. Hence exp(2√(∏b_i/log T)) ≥ e^{2b₁/√3}.
* For HB14 (n = 4, d = 3): V^d/T = V³/V = V² and d^{−3/2} = 3^{−3/2}, so k ≪ V^{2·3^{−3/2}+ε}. Also V ≥ B_min³ and
  3·2·3^{−3/2} = 2/√3.
* Sub-boxes only multiply the count by their number. ∎

*Scope.* This closes Z52D's (R3) for the standard affine and projective determinant method in the (u, B, k) model,
including translations and subdivisions. In the balanced block the (s, w, k) model k(s² − w²) − 4s − 4p and the (k, m, w)
model (km − p)² − 4m − w² give the same ratio ∏b/log T = 1/2. Other embeddings, Salberger's global determinant method, and
congruence-enhanced (p-adic or Coppersmith-type) variants are not covered.

The obstruction is criticality: V/T = 1, the expected count is O(1), and HB-type methods need T ≫ V. Uniform per-curve
bounds would be a second obstacle. Bombieri–Pila gives only B^{1/δ} on curves of degree δ, and no uniform improvement is
known for integral points on general genus ≥ 1 curves. Ellenberg–Venkatesh pose this as open; Mendes da Costa
(arXiv:1301.4116) handles special cubic families only.

## 8. Verdict

**Narrowed, with one strengthened sufficient condition.**
* **Closed (scoped PROVED).** The standard determinant method (HB14/HB15) for (★) blocks: it gives ≥ min(B_i)^{2/√3}
  auxiliary curves (Prop D).
* **Strengthened.** R2′ ⟸ MIX (Thm R, PROVED). MIX is a power-saving (not beyond-square-root) bound for the second-order
  Weyl sums of the remainder map, and it holds numerically with η ≈ 1/2. This replaces Z52D's R1 as the natural sufficient
  condition. R1 was numerically false at 10¹²; MIX is numerically true.
* **Located.**
  * The 4-condition is two 2-adic bits on the even vertex (Lemma B). It is a factor 1/5 in the model (Prop C), and it sits
    inside the QR colour layer (Prop C′).
  * T1 kills the five-slice layer but not the 2-cycles (Prop S, infinite family). So N₂ is *not* bounded better than N₄,
    and any lower bound for N₂ is T1-blind.
* **Dynamics.** f is the independent-CRT random map to second order (EVIDENCE, 1.9·10⁸ primes exhaustively). No falsifier
  of a power saving exists (max N₂ = 7 below 4·10⁹).
* **What is missing for R2.** MIX, i.e. any power saving in Σ_{u ≤ 2U} e(−h₁p/u − h₂p/f(u)) for h₂ ≠ 0. That is
  second-order equidistribution of (p mod u, p mod f(u)), and no method is known (§5.3).
* **For ES.** None of this helps (§6). R2 is an upper-bound methods test.

## 9. The four FRONTIER §4 hard screens (best idea: Theorem R / MIX)

1. **T1 (odd squares).** Not applicable as a lower-bound screen. Theorem R is an upper bound and is equally valid at
   squares; MIX holds numerically there (§5.3 table). It *fails* the ES requirement in the sense that it cannot see T1:
   by Prop S, N₂ > 0 at infinitely many squares. Stated honestly, Theorem R can never be an ES step.
2. **8/131.** Numerator-blind: Theorem R and MIX do not see the 4 at all (N₄ ≤ N₂). Not an ES step.
3. **Tied modulus.** Lemma G handles the tied modulus u | p + B exactly by letting the summation variable *be* the modulus,
   and passes the second divisibility (modulus f(u)) to a phase-on-a-curve condition. This is the one genuinely new
   handling, but it is for an upper bound only.
4. **Fixed p.** Yes. Every statement is at a single p, with no averaging over p, levels or moduli. MIX is a single-p
   exponential-sum statement.

## 10. Proposed FRONTIER §7 text (do NOT edit FRONTIER here)

In §7.1, replace the sentence "Still open: … the 2-cycle count of x ↦ (−p mod x), unbalanced blocks." by:

> Still open: cancellation across conductors/frequencies, unbalanced blocks. *(z53, `Z53_HYP2CYCLE.md`.)* The 2-cycle
> form (R2) is an upper-bound methods test only, and it is ES-inert. A bound N ≪ U^{1−η} for the balanced block would not
> improve R(p) ≪ p^{1/3+o(1)} (the cube block dominates), and could not give positivity (block mean 0.146).
> * PROVED: R2 follows from MIX, a power-saving bound for Σ_{u∈(U,2U]} e(−h₁p/u − h₂p/f(u)) with h₂ ≠ 0 and |h| ≤ U^η.
>   The reason is that f(f(u)) = u iff ({−p/u}, {−p/f(u)}) lies on the graph of the Gauss map (Lemma G / Thm R).
>   MIX needs only a power saving, unlike Z52D's beyond-square-root R1, and it holds numerically with square-root
>   cancellation at 10¹²–10¹⁸.
> * PROVED: the standard determinant method (Heath-Brown's Thm 14/15) yields ≥ min(B_i)^{2/√3} auxiliary curves for
>   kuB − u − B = p in every box, which is more than the trivial bound.
> * PROVED: T1 kills the five-slice layer but not the 2-cycles. There are infinitely many odd squares with a balanced
>   2-cycle (q | m² + 1, q + 1 | m² − 1).
> * PROVED (model): the 4-condition is two 2-adic bits, with density ratio 1/5.
> * EVIDENCE: f is the independent-CRT random map to second order. The maximum 2-cycle count over all primes < 4·10⁹ is 7.

In §6 (*Analytic / counting at one prime*), add:

> * Determinant method (Heath-Brown Thm 14/15) on kuB − u − B = p → ≥ min(B_i)^{2/√3} auxiliary curves in every box, which
>   is more than the trivial bound (critical box, V/T = 1) → `Z53_HYP2CYCLE.md` Prop D (z53).

## 11. Bottom line

The balanced-block 2-cycle count R2 can be read exactly as a dynamical statement. The remainder map f has a 2-cycle at u
exactly when the phase pair ({−p/u}, {−p/f(u)}) lands on the graph of the Gauss map. Solving the first divisibility by f
itself turns R2 into a *power-saving* second-order equidistribution hypothesis (MIX). That is strictly weaker than the
beyond-square-root R1 of Z52D, and the computations at 10¹²–10¹⁸ show it holding with square-root cancellation. So R2 is
"true for the expected reasons", but MIX is a second-order (p mod u, p mod f(u)) problem for which no method is known.
The obvious algebraic alternative, the determinant method, is provably vacuous here because the box is critical.

The 4-condition is two 2-adic bits riding on a QR colour condition. T1 kills the colour layer but not the 2-cycles, so
nothing that bounds 2-cycles, from above or below, can see what ES needs. f itself is, to second order, the independent-
CRT random map, and there is no falsifier: max 7 cycles among 1.9·10⁸ primes.

R2 is an upper bound. It cannot improve R(p) ≪ p^{1/3} and cannot give positivity, so it should be retired from §7.1's
ES-relevant list, or kept as a methods test via MIX. ES remains open.

## 12. Reproduction

```
REPO=$PWD; mkdir -p /tmp/h2c && cd /tmp/h2c; ulimit -v 6000000
gcc -O2 -o scan $REPO/scripts/z53_hyp2cycle_scan.c -lm;  gcc -O2 -o primes $REPO/scripts/z53_hyp2cycle_primes.c
gcc -O2 -fopenmp -o maxsearch $REPO/scripts/z53_hyp2cycle_maxsearch.c -lm
gcc -O2 -fopenmp -o model $REPO/scripts/z53_hyp2cycle_model.c; gcc -O2 -fopenmp -o pairmoment $REPO/scripts/z53_hyp2cycle_pairmoment.c
gcc -O2 -o mix $REPO/scripts/z53_hyp2cycle_mix.c -lm; gcc -O2 -o lvl $REPO/scripts/z53_hyp2cycle_levelform.c -lm
timeout 1200 uv run --with sympy python $REPO/scripts/z53_hyp2cycle_brute.py ./scan        # 59 959 cases, 0 mismatches
./primes 100000000 200000 > p8.txt; ./primes 1000000000000 100000 > p12.txt               # likewise 1e16 (2e4), 1e18 (1e4)
./scan 0 < p12.txt > o12.tsv                                                              # §2 table (also p8, p16, p18)
python3 -c "for m in range(1000001,1200001,2): print(m*m)" | ./scan 0 > osq12.tsv          # squares control
OMP_NUM_THREADS=8 timeout 1750 ./maxsearch 1000000000 4000000000 0 99 99 > ms10c.txt     # ~2 min; also [5,1e8), [1e8,1e9), mode 2
for U in 100 1000; do ./model $U 1; done; for U in 60 100 200; do ./pairmoment $U; done
head -20 p12.txt | ./mix 20; head -6 p16.txt | ./mix 10; head -3 p18.txt | ./mix 6       # §5.3
head -3000 p12.txt | PER=1 ./lvl | grep -v primes                                        # Lemma A cross-check vs ./scan
uv run --with sympy python $REPO/scripts/z53_hyp2cycle_sqfamily.py 20000 | ./scan 0     # Prop S
uv run --with sympy python $REPO/scripts/z53_hyp2cycle_cells3mod4.py 30000             # Prop C' companion
uv run --with sympy python $REPO/scripts/z53_hyp2cycle_controls.py data/z53/hyp2cycle/controls.json
```

## 13. Review log

(pending: hostile internal review, then cross-model review)
