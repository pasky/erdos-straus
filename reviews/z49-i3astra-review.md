# Hostile review of I3_DEEP_ASTRA.md (branch side-agent/z49-i3astra, commit 6aeb18a9)

Reviewer: cross-model hostile review, wave z49. Independent checks:
`scripts/z49_revi3astra_check.py` and an inline census/shared-modulus script (contents recorded below). Both ran under
`ulimit -v 8000000`, each in under 3 s.

## Verdict: **SOUND** (no fatal or major error found), with minor repairs and a sharp novelty downgrade for §§2, 4, 5 and 8.5.

I re-derived every step of Thms 8.3, 8.4, 8.6 and 8.8, Lemmas 8.1, 8.2 and 8.7, and Prop 8.5 by hand. I also re-derived
Thm 3.3, Thms 2.1/2.2 and Thm 4.1/Cor 4.2, and checked the atomic-Janson theorem (es-subexp-note, thm:janson) and the
energy lemma (POINTWISE_OMEGA10 Cor 3.5/4.1) that these proofs import. I could not break any of them. The substantive
content is §8.3, §8.4, §8.6 and §8.8. All of it is about the sign-free count I3, so none of it touches ES or ES₅, and
the document says so correctly.

## Point-by-point (focus items)

**Thm 8.4 (δ₃(H) ≤ exp(−cL²/(log L)²)): correct.**
- *Atomicity.* The family uses squarefree, Y-rough, coprime u ∈ [H^{1/16}, H^{1/8}] and v ∈ [H^{1/2}, H]. Each event
  depends only on (n mod p)_{p | uv}, so it is atomic on independent uniform coordinates, with P(E) = 1/(uv).
  Distinctness holds because equal modulus and equal residue force equal sums, since 0 < u+v < uv.
- *Decomposition.* I checked u = gja, v = hkb, u′ = gkc, v′ = hjd and D = ghjk = gcd(uv, u′v′). The four compatibility
  congruences are exactly D | (u+v) − (u′+v′), reduced modulo g, h, j, k in turn. They fix c modulo hj and d modulo gk.
  The joint probability is 1/(D·abcd), since uvu′v′ = D²abcd.
- *Shared modulus D ≤ 4V′.*
  - Unequal sums: D ≤ |u+v−u′−v′| < 4V′.
  - Equal sums: u ≠ u′ and h | u − u′, so D = (gj)·k·h ≤ u·u′·|u−u′| ≤ H^{3/8} < V′.
  - Endpoint separation really is needed here. With overlapping ranges I found equal-sum dependent pairs with
    D/max(v, v′) up to 14. With separation (u ≤ v^{1/3}, tested on 2 146 pairs) the maximum was 0.149. The inequality
    D ≤ uu′|u−u′| held on all 44 589 equal-sum dependent pairs tested.
- *Pair sum Δ.* The per-quadruple bound is O(1/D² + 1/(DU′) + 1/(DV′) + 1/(U′V′)). The 4^{ω(D)} sums give
  O(1/Y + L⁴H^{−1/16}) per box, and there are O(L⁴) boxes. So Δ ≪ L⁴/Y + L⁸H^{−1/16} = O(L^{−4}), i.e. Δ = o(1).
- *Mass.* μ ≫ L²/(log Y)² = L²/(64 log²L). The fundamental-lemma step and the alternative odd-order Bonferroni
  truncation (k = C log L, with Y^{k+1} = H^{o(1)} error terms) are both fine. The shared-prime correction is
  O(L²/Y).
- *Atomic-Janson hypotheses.* P(E) ≤ H^{−9/16}. The conflict mass is at most
  ω(uv)·max_p w_p ≤ (2L/log Y)·2(1+L)²/Y = o(1). So x_E = 2P(E) satisfies the lopsided-LLL condition and K ≤ e^{1/3}.
- *The imported theorem.* I re-read the proof of thm:janson. Lemma `compat` replaces Harris, and the step
  P(B_i | E_i) ≥ P(B_i^d) − Σ P(E_j′ ∩ B_i^d) is correct. I also tested it independently on 300 random atomic
  instances: max of (μ − KΔ) − (−log P(Av)) was −4·10⁻⁷, so the inequality was never violated.

**Thm 8.3 (δ₃(H) ≥ exp(−CL⁶/log L)): correct.**
- *Envelope.* On n ≡ 1 (mod Q) an event survives iff D = gcd(uv, Q) divides u+v+1, and then P_Q(E) = D/(uv). This is
  at most s_uv = gcd(uv, u+v+1)/(uv) at every stage.
- *gcd identity.* gcd(uv, u+v+1) = gcd(u, v+1)·gcd(v, u+1) holds by valuations; I also checked it numerically for all
  u, v < 400.
- *Lemma 8.1.* The key observation m = ab | u+v+1 bounds the progression sum by 3 + log(H/u). The Ingham-type bound
  Σ_{u≤X} τ(u)τ(u+1) ≪ X log²X is standard. Numerically S♯/L⁴ = 0.082, 0.068, 0.058, 0.054 at H = 10², 3·10², 10³ and
  2·10³. That is consistent with the bound; a heuristic suggests the true order is also L⁴.
- *Cost accounting.* A step (p, j) is triggered only when log p < (2L/(c₀ j))·Σ_{p^j | uv} s_E. Summing over (p, j)
  gives exactly (2L/c₀)·Σ_E s_E·h(uv). The worst case h ≪ L/log L is correct. So log Q ≪ L⁶/log L.
- *LLL step.* Pinning only toward the class of 1, which lies in no event, means no event's support ever empties. At
  termination each event's neighbourhood mass is at most c₀ = 1/16. That gives Π(1 − x) ≥ e^{−1/7} > 1/2 and
  P(no event | fibre) ≥ exp(−3S).

**Prop 8.5 (raw Bonferroni cluster bound fails): correct, but a straw man.**
- The events (3, v) with v | P and v ≡ 2 (mod 3) survive the pinning at 3. On the fibre they reduce to n ≡ −3 (mod v).
- The bound log S_j ≥ (3 − o(1))·log P ≈ 1.5L is correct, against O(log²L) for the proposed right-hand side.
- Failure of raw factorial-moment bounds on divisor-closed clusters is folklore. It refutes a premise that nobody had
  established (see m3).

**Thm 8.6 (transfer to actual integers): correct, relative to POINTWISE_OMEGA10 Cor 4.1.**
- *BRW minorant.* B ≤ F pointwise holds for any u_j: when P_i = 1 all earlier A_j vanish, and otherwise the summand is
  a square. The error is E(F − B) = Σ_i E[A_i(Σ_{j<i} A_j(P_j − u_j))²] ≤ m²·Σ_j P(A_j)·2^{−(d+1)/k}. Here u_j is the
  degree-d Efron–Stein truncation in the space pinned at A_j, which is again a width-k single-value system.
- *Width and event count.* The widths satisfy k ≤ L/log L because all primes ≤ L² are pinned. Splitting into
  single-value events gives log m = O(L²/log L).
- *Degree.* d = O(k(S + log m)) = O(L⁵/log L).
- *Coefficient ledger.* The total coefficient mass is exp(O(dL + log m)) = exp(O(L⁶/log L)), and each cell is a single
  congruence class. Both are correct.
- *Energy lemma, independent test.* On 300 random single-value systems with widths ≤ 3, non-uniform product measures
  and alphabets ≤ 4, I computed exact Efron–Stein energies. The maximum of Σ_U 2^{|U|/k}·‖F^{=U}‖² was 0.999996 ≤ 1.
- *Corollary.* The κ ≤ 1/6 corollary follows.

**Thm 8.8 and Lemma 8.7 (E₃(N) ≪ N exp(−c(log N)^{2/3}/(log log N)^{1/3})): correct.**
- *Atoms.* An atom (k, q, u) hits at n ≥ 3KX; this gives the word ((kq+1)/u, u, (n+u)/(kq)).
- *Activity.* An atom is active iff u ≡ −c (mod k), and activity forces (c, k) = 1.
- *Same-q exclusivity.* Two active atoms at the same q have distinct classes mod q: equal u gives u | k − k′, and
  u > U₀ > K forces k = k′. With CRT across q > K this makes Z_X, conditional on c, a sum of independent Bernoullis.
  The factorial moments are then exact rather than assumed.
- *Mass (8.11).* The Cauchy–Schwarz BV/BT error estimate (Σ r²/φ ≪ T⁴) is fine, and h(J_c) ≥ 1 because 1 ∈ B.
- *Rough multipliers.* The bound h(J_c) ≥ h(B)(1 − Z(c)) holds because k/p ∈ B. The exponential moment gives
  P(Z > ½) ≤ e^{4−y/2}.
- *Bonferroni.* Q_r(z) ≤ 1[z=0] + binom(z, r+1), and r = O(M₀) gives e^{−cM₀}.
- *Ledger and optimisation.* The ledger is exp(O(T³/log T)). The choice T ≍ (log N·log log N)^{1/3} gives the stated
  exponent.
- *Prime/rough refinement.* The selector costs 2^{π(y)} = exp(O(T²/log T)), so the bound
  N exp(−c(log N)^{2/3}) at primes also holds.
- *§8.7 checks.* The non-transfer examples check out: I3(21) = 1, I3(42) = 0, I3(6336) = 0, and the Vaughan identity
  5·6336 + 3 = 179·177 holds.

**Earlier sections.** Thm 3.3 (large sieve with Rankin truncation), Lemma 3.2, Prop 5.1/5.2 and Thms 2.1, 2.2 and 4.1
are all correct. My independent numerical checks agree with the document:

| Check | Result |
|---|---|
| Direct triple enumeration vs divisor method | agree at every n ≤ 1500 |
| AP-sieve census | exactly 111 zeros on [3, 10⁵], last 36078 |
| I3(2433600) | 0 |
| I3(8813281) | 84 |
| Hard-prime table (193 … 66529) | reproduced |
| I3(17), I3(241), I3(121) | 0, 2, 2 |
| I3(49), I3(1225), I3(1600) | 0, 0, 0 |
| δ₃(H) for H = 3…7 | 32/36, 108/144, 2207/3600, 1699/3600, 70807/176400, exactly as tabulated |
| Thm 4.1 inequality | holds on 36 random intervals |

## Fatal
None.

## Major
None.

## Minor / novelty and scope

- **m1. Several "theorems" are trivial and should be relabelled as observations or lemmas.**
  - *Thm 2.1* is pigeonhole: there are B²(B+1)/2 triples and 2B³ target integers. It says nothing about the
    full count.
  - *Thm 2.2* is the standard "smallest coordinate ≤ (9n/7)^{1/3}, then divisor bound" argument.
  - *Thm 4.1/Cor 4.2 is exactly a congruence-family count, as suspected.* Each fixed pair of small coordinates is
    one arithmetic progression of modulus ≤ H. An AP meets any interval of length H at least ⌊H/modulus⌋ times. The
    only extra ingredient is the one-line disjointness of the three wedges.
  - Cor 4.2 therefore uses no arithmetic beyond the equidistribution of APs with modulus ≤ H in intervals of length H.
    At polylog H it gives (log log n)² per integer, against a mean of ½log²n.
  - The section's promise of "arbitrarily slowly growing H" adds nothing; the §4 Assessment already concedes that no
    pointwise or almost-all statement follows.
  - *Props 5.1/5.2* are superseded by §8 and are elementary.
- **m2. Stale headline (§0).** §0 still lists the §3 bound N exp(−c√log N) and the §5 bounds
  exp(−(2+o(1))H) ≤ δ₃ ≪ exp(−c√log log H) as the results. Only the round-2 banner says they are superseded. §0 should
  be rewritten to lead with Thms 8.3, 8.4, 8.6 and 8.8, and to mark §3 and §5 as superseded inline.
- **m3. Prop 8.5 is a straw man.** No cited campaign document proves or relies on the raw bound (8.8) for these
  events. It is a reasonable caution, but it should not count as "refuting a campaign conjecture". Under the z49
  proof-step rules it is not a deliverable.
- **m4. Dependency on internal unrefereed lemmas.**
  - Thm 8.6 rests entirely on POINTWISE_OMEGA10 Cor 4.1 (C-1, by polarization plus deletion–contraction) and on the
    BRW identity. Thm 8.4 rests on es-subexp-note thm:janson.
  - I re-checked both proofs and they look right, and my random tests pass. The labels "PROVED relative to …" are
    therefore appropriate.
  - The §8.1 phrase "upper Haar argument" (meaning the upper bound on δ₃, i.e. the lower bound on −log δ₃) is
    confusing next to "lower estimate for −log δ₃". Use one convention.
- **m5. Possible cheap improvement (not an error).**
  - Thm 8.3 charges every event the worst case h(uv) ≪ L/log L. A weighted bound on Σ_E s_E·h(uv) might give roughly
    L⁵·log log L, and κ correspondingly larger in Cor 8.6. I have not verified this.
  - Lemma 8.1's L⁴ itself appears to be the true order, so the loss comes only from h.
- **m6. Novelty.**
  - Thm 8.4 closely follows the structure of es-subexp-note's Haar lower bound: rough squarefree atoms, atomic Janson,
    and a shared-modulus Δ bound. The I3-specific new ingredient is the equal-sum case, handled via endpoint
    separation.
  - Thm 8.8 is an adaptation of the es-threequarter-note conditional-CRT and Bonferroni architecture, with a new atom
    family that is checked correctly.
  - Thm 8.3 (adaptive quarantine with the gcd envelope) and Cor 8.6 are genuinely new within the campaign. I know of
    no literature result covering them, but I have not done a literature search.
- **m7. Relevance to ES.** Everything here concerns I3, which is sign-free, all-integer and Haar-based. It proves no
  ES₅ statement at primes; the document says so. The prime-input bound #{p ≤ N : I3(p) = 0} ≪ N exp(−c(log N)^{2/3})
  concerns the existence of a forest edge with t ≥ 3, not a bichromatic edge. Do not cite it as an ES exceptional-set
  result.

## Bottom line
The round-2 results (Thms 8.3, 8.4, 8.6, 8.8) are SOUND as stated. What they show is the following.
- c·L²/(log L)² ≤ −log δ₃(H) ≤ C·L⁶/log L.
- Explicit integer avoiders of all bounded-endpoint words exist up to H = exp((log x)^{1/6}).
- The I3 exceptional set obeys E₃(N) ≪ N exp(−c(log N)^{2/3}/(log log N)^{1/3}) for all integers, and
  ≪ N exp(−c(log N)^{2/3}) at primes.

The first-round §§2, 4 and 5 are correct but trivial or superseded; the short-interval bound is a congruence-family
count. Required repairs are editorial: m1 (relabel), m2 (rewrite §0), m3 (downgrade Prop 8.5).

## Inline script used (census to 10⁵ and separated equal-sum check)
The census enumerates the AP n ≡ −u (mod tu−1), starting at 3(tu−1) − u, for every (t, u) with 3(tu−1) − u ≤ 10⁵.
The large-n counts use divisor enumeration over the coordinate ≤ (9n/7)^{1/3}. The equal-sum check uses u ∈ [5, 10],
v ∈ [1000, 4000], squarefree and coprime.
