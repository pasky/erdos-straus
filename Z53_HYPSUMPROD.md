# Z53_HYPSUMPROD — depth lane HYPSUMPROD (FRONTIER §7.1): sum-product / incidence tools on the tied hyperbola, block-shape map

ES is OPEN. Nothing here proves or disproves it. Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Internal results are internally reviewed only (not refereed).

Brief: `z52bbriefs/z53_depth.md`, lane kickoff `z52bbriefs/z53_lanes.md` §HYPSUMPROD. Scripts `scripts/z53_hypsumprod_*`,
data `data/z53/hypsumprod/`.

**STATUS: CHECKPOINT 1 (skeleton).** Sections marked (TODO) are filled in the final version.

## 0. Setting and notation

For an integer n ≥ 3 (the case of interest is a prime p ≡ 1 (mod 24)) a (★) triple is (u, B, C) ∈ ℕ³ with
4uBC − u − B = n; R(n) is their number. Block: 𝔅(U,V) = (U, 2U] × (V, 2V], N(U,V) = N(U,V; n) = #{(u,B) ∈ 𝔅 : 4uB | n+u+B}
(Z52D_HYPERBOLA §0). Put W := n/(4UV); a block solution has C = (n+u+B)/(4uB) ∈ [n/(16UV), (n+2U+2V)/(4UV)], i.e. C ≍ W.
Exponents: U = n^α, V = n^β, W ≍ n^γ, γ = 1 − α − β; the block simplex is Δ = {α, β ≥ 0, α + β ≤ 1}. The trivial (elementary,
Z52D Thm 1) bound is N ≤ n^{o(1)} min(U, V, W + 1), exponent t(α,β) := min(α, β, γ); max t = 1/3 at the **cube point**
α = β = γ = 1/3, which is where R(n) ≪ n^{1/3+o(1)} comes from.

Three *fibrations* of the same point set (all PROVED, elementary; Z52D §2):
* u-fibre: (4uC − 1)·B = n + u — a divisor d = 4uC − 1 ≡ −1 (mod 4u) of the single integer n + u, d ≍ 4uW;
* B-fibre: symmetric, a divisor ≡ −1 (mod 4B) of n + B;
* C-fibre: (4Cu − 1)(4CB − 1) = 4Cn + 1 — a divisor x ≡ −1 (mod 4C) of the single integer 4Cn + 1, x ≍ 4CU;
  equivalently a point of the modular hyperbola 𝓗 = {xy ≡ 1 (mod 4n)} at **height** C = (xy − 1)/(4n), with the **tie**
  x ≡ −1 (mod 4C) (which forces y ≡ −1 (mod 4C)).

## 1. Statements attacked (precise)

**(S1) Block-shape map, upper side.** For every (α, β) ∈ Δ determine the best exponent θ_known(α,β) such that a known tool
(elementary, divisor-in-residue-class (Lenstra / Coppersmith–Howgrave-Graham–Nagaraj / Bernstein), divisor sums in APs and
short intervals (Shiu), modular-hyperbola box counts and concentration bounds (Weil/Kloosterman, Cilleruelo–Garaev,
Bourgain–Garaev, Kerr–Shparlinski–Wu–Xi, Shkredov), exponential sums (van der Corput, Erdős–Turán), determinant method /
dimension growth) proves N(U,V; p) ≪ p^{θ+o(1)} for every large prime p, **with the tie included**. Question: is
θ_known < t(α,β) anywhere (a power saving over trivial)? In particular: does any tool improve |E(p)| ≤ R(p) + M(p) ≪ p^{1/3+o(1)}?
(Note: since R ≥ 0 and M ≍ log²p, |E(p)| ≪ p^θ ⟺ R(p) ≪ p^θ for θ > 0; the question is a pure *upper-bound counting* problem.)

**(S2) Block-shape map, lower side.** Where do LOWER-bound tools (Weil/Kloosterman asymptotics in large boxes, Selberg–Hooley
divisor sums in APs mod 4p, every-λ box solvability) apply to the tie-free counts, which relaxations of the tie they can carry,
and exactly how the tie breaks them.

**(S3) Integer-uniform falsifier.** Is the trivial bound attained (up to n^{o(1)}) by some *integers* n, so that every argument
uniform in n is capped at t(α,β)? (If yes: power savings must use primality; if no: the obstruction is technique only.)

## 2. Why this is not already closed

* Z52D_HYPERBOLA closed, at the **balanced block** u, B ≍ p^{1/4}: one-step fixed-conductor dualization (Thm 5), the
  Erdős–Turán/Fejér route with max|S_h| input (Thm 6), dispersion in the function variable (Prop 2), low-conductor main terms
  (Thm 3, Cor 4). It left open: unbalanced blocks, short-segment bounds, the Z1855 piece analysis in unbalanced blocks, and it
  did not survey *incidence / sum-product / divisor-in-class* tools nor the *lower-bound* side.
* This lane works on the whole simplex Δ (not one block), with the tool classes above, and in *counting* (upper-bound) form,
  which is the form in which the §7.1 target "improve E(p) ≪ p^{1/3}" is actually posed. None of the closed items covers:
  λ-uniform hyperbola concentration bounds, Lenstra-type fibre bounds, Shiu-type averaged fibre bounds, the
  integer-uniform question (S3), or the lower-bound/partial-tie question (S2).

## 3. First results (checkpoint 1)

**Lemma A (tie floor for Type II; PROVED, elementary).** Let n ≥ 1 and let (x, y) ∈ ℕ² with xy ≡ 1 (mod 4n); put
H = (xy − 1)/(4n) (the height). The Type II quadruples (a, b, c, d) ∈ ℕ⁴ with 4abcd − a − b = cn and
(4acd − 1, 4bcd − 1) = (x, y) correspond bijectively to factorisations H = c²d with x ≡ −1 (mod 4cd).
*Proof.* (⇒) (4acd − 1)(4bcd − 1) = 4cd(4abcd − a − b) + 1 = 4c²dn + 1, so H = c²d and x ≡ −1 (mod 4cd).
(⇐) Given H = c²d with 4cd | x + 1: xy = 4c²dn + 1 ≡ 1 (mod 4cd) and x ≡ −1 give y ≡ −1 (mod 4cd). Put a = (x+1)/(4cd),
b = (y+1)/(4cd) ∈ ℕ. Then 16abc²d² − 4cd(a + b) + 1 = 4c²dn + 1, i.e. 4abcd − a − b = cn. The two maps are inverse. ∎
(★) is c = 1, d = H: the full tie x ≡ −1 (mod 4H). The weakest admissible tie has modulus 4cd = 4√(H·d) ≥ 4√H.

**Corollary A′ (fixed congruences certify only finitely many heights; PROVED).** If the only information about a point
(x, y) ∈ 𝓗 is xy ≡ 1 (mod 4n) and x ≡ −1 (mod q) for a fixed q, then that information implies a Type II quadruple for (x, y)
via Lemma A exactly when some factorisation H = c²d has 4cd | q; then 16H | q², so H | q²/16 (at most τ(q²) heights).
*Proof.* 4cd | q ⇒ 16c²d² | q² ⇒ 16H·d | q². If no factorisation has 4cd | q, then x ≡ −1 (mod q) does not imply
x ≡ −1 (mod 4cd) for any of them (the residue of x mod lcm(q, 4cd) is not determined), so the information does not imply
a quadruple. ∎
*Reading.* A lower-bound count (Weil, Kloosterman, Selberg–Hooley) of hyperbola points in a region with a fixed congruence can
only certify Type II solutions at the ≤ τ(q²) fixed heights H | q²/16; at a fixed height the points are the factorisations
of the single integer 4Hn + 1, where no box/equidistribution tool acts. Any certification at growing heights needs a tie of
modulus ≥ 4√H that moves with the point. (Finitely many fixed congruences: same, with q = their lcm.)

**Proposition B (λ-uniform floor; PROVED, elementary).** Let m = 4p, I, J ⊂ ℤ intervals of lengths L_I, L_J, and
H_λ := #{(x,y) ∈ I × J : xy ≡ λ (mod m)}. Then max_{λ ∈ (ℤ/m)^×} H_λ ≥ φ(m)⁻¹·#{x ∈ I : (x,m) = 1}·#{y ∈ J : (y,m) = 1}
≥ (L_I/2 − 2)(L_J/2 − 2)/(2(p − 1)).
*Proof.* Σ_λ H_λ counts the pairs with both coordinates units; average and use #{x ∈ I : (x, 4p) = 1} ≥ L_I·(p−1)/(2p) − 2. ∎
*Application.* The (x, y) = (4Cu − 1, 4CB − 1) image of 𝔅(U,V) lies in a box with L_I ≍ WU, L_J ≍ WV, L_I L_J ≍ Wp, so the
floor is ≍ W. Every bound for N(U,V) that is obtained from a bound for H_1(box) **valid uniformly in λ** — Weil/Kloosterman
box counts, Cilleruelo–Garaev concentration (GAFA 21 (2011), Thm 1: I₂(M;K,L) < M^{4/3+o(1)}p^{−1/3} + M^{o(1)}, uniform in
λ, K, L), Bourgain–Garaev / KSWX / Shkredov-type bilinear inputs as used for box counts — is ≥ cW ≥ c·min(U, V, W): it can
never beat the trivial bound by a power, in any block. (Full map entry and the shift-uniform analogue: §5, TODO.)

**First falsifier (S3; EVIDENCE/CERTIFIED computation).** `scripts/z53_hypsumprod_rmax.c` computes R(n) for **every** integer
n ≤ 5·10⁸ and Q(n) := #{(★) triples with min(u, B, C) ≥ n^{1/3}/4} (the near-cube region, where the trivial bound is
≍ n^{1/3} ≈ 800 at the top). Result (`data/z53/hypsumprod/rmax_5e8.txt`): max Q(n) over all n ≤ 5·10⁸ is **22**
(n = 199 582 860); over primes n ≡ 1 (4) it is 16. Dyadic maxima of Q grow from 6 (n ≈ 10³) to 20–22 (n ≈ 3·10⁸), i.e.
like a power of log, not like n^{1/3}. max R(n) over all n ≤ 5·10⁸ is 439 (mean ≈ 51 at the top). So no integer comes near
the trivial bound in the near-cube region: the cap t = 1/3 is not witnessed by any integer in range, and an integer-uniform
power saving is *not refuted* by examples. (Status of (S3): no integer-uniform obstruction found; the wall is technique.)

## 4. Plan for the rest (TODO)
1. Full block-shape map (upper side) with a PROVED bound and the tool attaining it per region; Lenstra/CHN/Bernstein fibre
   regions; Shiu averaging ⇒ R(n) ≪ n^{1/3} log n.
2. Shift-uniform class-blind floor; Z1855 pieces in unbalanced blocks reduce to B-fibres.
3. Lower side: Weil/Selberg–Hooley ranges (γ > 1/2), how much the tie costs, Lemma A consequences.
4. Numerics per block at primes with controls (odd squares, near-squares, FRONTIER §4 item 14 primes).
5. Screens, verdict, proposed §7 text, review.
