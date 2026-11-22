# Second independent hostile cross-lab review (Claude Opus, smart mode): Wave z82 analytic headline records

Reviewed on `main` at 932ff71f3:
- `notes/z82/CAP_CONST.md`: Theorems U, H, UB, UP, Q (and its endpoint), and J.
- `notes/z82/BEYOND_34.md`: Theorem G (all three rows) and Corollary G′.
- `notes/z82/GAP11_JLL.md`: Theorems 5 and 6.

Scripts replayed: `scripts/z82_cap_uniform.py`, `scripts/z82_b34_gaps.py`, `scripts/z82_gap11_r2_cert.py`. I also ran my own independent float replicas in `/tmp`.

**Independence.** I formed and wrote down my verdicts below before opening any `data/z82/xreview/REVIEW_{CAP_CONST,BEYOND_34,GAP11_JLL}_R*_OPUS.md`. I read those files only afterwards, to check whether the fixes they requested had been applied (they had) and to look for disagreements (there are none of substance). This review has not been externally refereed. No ES claim is made by any of the three notes, and none is made here.

## Verdicts

| group | verdict | broken step? |
|---|---|---|
| **CAP_CONST** (U, H, UB, UP, Q + endpoint, J) | **ACCEPT WITH MINOR FIXES** | None. The fixes are an export and duplication issue with Lane 1B, plus a stale pointer. |
| **BEYOND_34** (G rows 1–3, G′) | **ACCEPT WITH MINOR FIXES** | None. The fix is one stale pointer. |
| **GAP11_JLL** (Thm 5, Thm 6) | **ACCEPT** | None. Thm 6 is correctly labelled CONDITIONAL on ordinary D(.957). |

These are all scoped results: an exceptional-set or population count, a method ceiling, or a conditional rate. Nothing here is a statement about ES at an individual input. **ES remains OPEN.**

## Replays (ulimit -v 6000000, timeout ≤300 s; total wall time about 1 minute)

| script | result | wall time / peak memory |
|---|---|---|
| `z82_cap_uniform.py` | Exit 0. Linked two-way chart: 22382 labels, 17193 rejected, 68 mixed cubefree packets. Example `4/92=1/195+1/1380+45/1196`. Controls: squares 0/65, F2 6/6, F3 3/8, F4 20/24. Packet `(17,37,131,1365)`. Band: 97 colliding pivots deleted, 230 retained, 91 with D above the pivot. | 0.4 s / 35 MB |
| `z82_b34_gaps.py` | Exit 0. Gap identities 686 and 2496. Unique-list controls 182/89/93. 1536 block-sieve sandwiches. Seed grid: 20/191/6207/88. | 0.2 s / 34 MB |
| `z82_gap11_r2_cert.py` | Exit 0. At (a,b,τ)=(31/80, 57/1000, 999/2000): lower .421136, cost3 .412330, cost7(h≥6) .007296, net **+.001511**. At b=23/400: net with cost7 is −.0027, but lower − cost3 = **+.00434**, matching the note's pure-cutoff claim, which omits the second subtraction. Bare switch at b=.0338: +.00110. Thm 6 (τ=.9569): charge 1.149438, margin **+.001008**. | 32 s / 152 MB |

**Independent float replica** (`/tmp/opus2rev/gap11_float.py`; numpy; written from the note's formulas, not from the script):

| quantity | my float value | certificate |
|---|---|---|
| Thm 5 lower envelope, U₀(a,b) units | .42348 | .42113 |
| cost3 (continuous min over s, optimum s≈2.08) | .41106 | .41234 |
| cost7, h≥6 | .00728 | .00730 |
| Thm 5 net | +.0051 | +.0015 |
| Thm 6 charge | 1.14926 | 1.14944 |
| Thm 6 lower `(2/τ)log(τ/.35−1)` | 1.15045 | — |
| Thm 6 margin | +.00119 | +.00100 |

My lower-envelope replica uses its own semilinear and linear DDE tables and the same Buchstab recursion and vector intersection. The certificate's values are slightly worse throughout, consistent with outward rounding and its coarser choice set: s/10 for cost3, and a finite menu of s₇.

**Integral representation of H_h.** I checked `(2^{h−1}h!)^{-1}∫d√v∏dt_i/t_i/(1−v−Σt_i) = H_h(1/z)` (the identity behind (4)–(5)) against the delay equation by Monte Carlo, 2·10⁷ samples:

| h | z | Monte Carlo | DDE |
|---|---|---|---|
| 2 | .3875 | .079579 | .079632 |
| 2 | .057 | 1.62597 | 1.62606 |
| 4 | .057 | .153054 | .153065 |
| 6 | .057 | .0022845(11) | .0022817 |
| 8 | .057 | 6.616e−6 | 6.604e−6 |

I also checked `J₁(a)=2H₂(1/a)` by quadrature: .159228 vs .159264. The h=6 term dominates cost7. Its 0.1% Monte Carlo excess is about 1e−5 in the margin, far below .0015.

## CAP_CONST

### Theorem U (uniform 1≤E≤λ)

**Chart legality.** D=aJ, and A=(kℓ+1)/4 is divisible by ma.
- At s|m with colour 2c ≤ 2g = 2E+2: a failure is coprime to m because m is G-supported. So s∤V, v_s(x)=v_s(A), and v_s(z)=2v_s(A)−2c. That is even and ≥ 2−2E−2 = −2E. The root is odd, coprime to n, and has radical dividing A|y.
- At s|a (exponent 1 in D): v_s(z) ≥ 0 even if s|n.
- ℓ∤4D, since every prime of D is at most e^{9αt} < ℓ. (D,k)=1. The fibre is a unit at k.

So every genuine hit at a surviving pivot is a legal cap-E packet. A failure therefore has Y_*=0, and P(n) = (μ_c/(c₁S))^{2j} ≥ 1 there. ✓

**Collision deletion.**
- The number of distinct D is at most e^{9αt}·Σ_{m≤M}m ≤ e^{11αt}.
- log|D−D′| = O(gαt), so each pair has O(g) band divisors.
- The global deletion costs at most g·e^{24αt−t/2} per AP, against 1/φ(Q) ≥ e^{−10αt}/4. This is fine for small absolute α and log g = o(t).
- Recovery: D determines (a, J), since a carries exponent 1 and J exponents ≥2; J determines (m, colouring). At fixed ℓ and Q, k is fixed by k ≡ −ℓ̄ (mod Q), k<Q.

The per-pivot Y_ℓ therefore lie in [0,1]: targets are disjoint and w_a ≤ 1. ✓

**Gallagher.**
- Q ≤ 4e^{10αt}, ℓ ≥ e^{t/2}, so log x/log T₀ ≥ 1/(24α). Deleting an odd prime p₀ of the exceptional conductor from m and a gives q₁∤Q. The 2-part of Q is exactly 4, and conductors 4 and 8 have no exceptional zero for large T.
- Two-sided ≍1/φ(Q) with absolute constants, uniform in the class: ✓.
- Weight algebra: w_a/φ(Q) = 1/(2aφ(m)) is exact.
- The a-count in a reduced class mod k, coprime to m′: error √U_a(τ(m′)+1), against main ≫ U_a/(k log m). Fine because e^{4αt} ≫ e^{1.1αt}. ✓

**Mass and parameters.** I recomputed log(S/(Cj)):
- With t = A₀g log(2g)e^{λ/(g+3)} and j ≍ e^λ/t, one gets S/j ≥ c·A₀³g³(cA₀)^g.
- So log(S/(Cj)) ≥ c₄g for large absolute A₀. The saving jg ≍ L·e^{−λ/(E+4)}/log(2B) is exactly (U).
- Side conditions: log M = αt ≥ Cg; t = o(L) uniformly (the worst case is e^{λ/5} at g=2, or about λ log λ at g≈λ).
- At E=1 this recovers z81's 4/5. ✓

**Centered moment.** The per-pivot variables are independent given the fibre, and the variance is at most μ_c. Rosenthal/Bernstein then gives E|Y−μ|^{2j}/(c₁S)^{2j} ≤ (C′j/S)^j for j ≤ S.

μ_c is a sum of functions that are each periodic mod a single k ≤ K. So the polynomial never needs the lcm of all multipliers: every factor has modulus dividing kℓ. The budget is e^{C₁jt} ≤ N^{1/3}. ✓

**Regime λ<E≤λ² (k=1, h primes in (g,g²]).**
- m ≤ g^{2h} ≤ e^{αt} for C₂ ≥ 2/α.
- The label count g^{3h} ≤ e^{3t/C₂} is consistent with the deletion count.
- log S ≥ hu ≥ 4λ, and j ≤ L, so log(S/j) ≥ λ−O(1).
- Saving ≍ Lu/log g. This is a fixed power saving at E = λ^{1+η}, consistent with EXSET_LINNIK_CAPS; no record over it is claimed. ✓

**Uniformity in E.** α, A₀, D₀, C₂ and the Gallagher constants are all absolute. No dimension-dependent BV or Shiu constant enters. I could not break uniformity.

### H, J

H is the fixed-E version. J replaces {1,2,4,…,2E+2} by {1,2,…,d₀+2}:
- The exponent sum is no larger.
- The Jacobi symbol is still negative, since every label prime divides A.
- The local count is 2a+1+d₀, identical to C's F at E=d₀.

Hence J's exponent (d₀+3)/(d₀+4), which is 5/6 at d₀=2, is correct, both for the upper bound and for the matching single-f whole-avoider ceiling. ✓

### UB / UP

I spot-checked:
- the final conversion to O(Lσ) (the cases tσ ≤ 1 and tσ > 1);
- σ = Ke^{−r}/log(2B) with (B+1)r = λ, which gives T(σ) ≪ Lσ through K^{−B}e^{O(B)} ≤ K/log 2B;
- UP's replacement of B by B−1 when primality is retained.

Sharpness is correctly scoped to the light single-band architecture. L's Euler-product bound (E+1)^{1/(1+θ)} = o(λ) holds iff θ > η. ✓

### Q (Chowla) and endpoint

**Carrier count.**
- #d ≥ (w/v)^v = y^{1−1/C−o(1)}. d ≥ y^{1−o(1)} because 2^v = y^{o(1)}.
- b = (q−1)/(2d) is odd (q≡3 mod 4, d odd) and at most y^{2ε+o(1)}. The most frequent b gives distinct q.
- (q−1)/2 = bd divides h, with h/(bd) = 3∏_{p∤d}p odd. So donors are exactly the q with (s/q) = −1. ✓

**Large sieve.**
- The energy bound l!P^l comes from unique factorisation.
- bad ≤ X²(100l/P)^l ≤ X^{1−4γ+o(1)}(2Y)^{1/2+2γ}, which is below X^{1−2γ} since Y = X^{o(1)}.
- The Chowla lift at q_* = p·2^a ≍ X^{1−γ/2} yields ≥ X^{1−γ} distinct carriers. ✓

**Endpoint arithmetic.**
- P/√Y ≳ (√z/(3v log z))^v/log^{3J/2} ≈ (K/60)^{10 log U}/polylog, which exceeds U⁵.
- bad ≤ X·exp(−Ω(U/log₂U)) = o(X/log^{J+1}X).
- log h ≪ z = (K log U log₂U)². ✓

Montgomery ⇒ GRH + Chowla is verified (κ < (1−θ)/2). The conclusion "recovers, does not improve, z80 §12 at U=log₂R" is correct.

### Minor fixes (CAP_CONST)

1. **l.238, stale pointer and an unflagged duplicate.** The note says Lane 1B's note is "not in this tree". But `notes/z82/CAP_TO_ES.md` is now on `main`. Its §0 Result and **Theorem K** (l.188, "rel. Lane 1A H/C at 7984da083") claim exactly J: linked exponent ≤ M, exponent (M+3)/(M+4), 5/6 at M=2, and the same whole-avoider ceiling.
   - J's comparison paragraph mentions only Lane 1B's E (4/5).
   - Fix: cross-reference K and export **one** row for the linked cubefree hierarchy, crediting J's proof as the source and K as the same statement. Do not export two RECORD items.
2. **Triage.** The CAP_CONST §0 triage already describes Q as a qualifier, not a new headline. That is correct; keep it so at export.

## BEYOND_34

### G §6.1 (targets and supply)

**Targets.** −v/u with 1 ≤ v < u ≤ K^γ:
- Targets are distinct, because cross-products are below e.
- They are inverse-disjoint: uu′ < e forces u=v′, v=u′, contradicting v<u.

**Activation.** z ≡ −e (mod 4uv) gives a reduced progression in e with e≡3 (4) and (uv,e)=1.

**Mass.** Σ_e N_e/φ(e) ≍ B³:
- one class mod 4uv contributes harmonic mass ≍ B/(uv);
- Σ 1/(uv) ≍ B².

**Witness.** The two-divisor witness A=uρ₊, B=vρ₋ is coprime, AB|m_e, e|A+B. I re-derived the identity 1/m + qA/(pm(A+B)) + qB/(pm(A+B)) = 4/p and its integrality: (q,A)=1 follows from e|A+B and (A,B)=1. ✓

### G §6.2 (unique match, two-sided probabilities)

**Collision bound.** For a ternary v′ ≠ ±v, some 2×2 minor has determinant ±1 or ±2, so the fibre bound is |G[2]|. Then 3^j|G[2]|K^{2γ}/φ(e) = o(1):
- row 1: 3^j = L^{log 3}e^{O(√l)} against L^{β(η−2γ)}, and (η−2γ)β > log 3 strictly gives the margin;
- row 2: 3^j = K^{o(1)}.

**Comparison law.** Independent bits with parameter 1/(r−J+1), conditioned on at most one mark at every r, give exactly the CRT law. The conditioning probability is at least 1−J²/R > 1/2. Hence the upper bounds b_m ≤ 2(C₃W)^m/m! and E 2^{−S} ≤ 2e^{−c₃W} hold uniformly in the pin.

**Product cap.** The Markov argument (E[Σ log r | residues] = O(jT/H) = O(T) by BT) is correct.

**Arithmetic.** e^{2H} ≍ (T/B)², hence W = BT², MT ≍ c₀³L, saving c₀²B^{1/3}L^{2/3}. That is L^{(2+α)/3} for B = L^α with α < 1/4 (needed for T/B → ∞), and L^{2/3}l^{1/3} for B = βl. ✓

### G §6.3 (relative block envelopes)

- **Upper envelope.** With s even, U_b = binom(D_b−1, s) ≥ 0 when D_b ≥ 1, and U_b = 1 when D_b = 0.
- **Lower envelope.** The telescoping identity, 0 ≤ 1_j ≤ U_j and U_b − 1_b ≤ U_b − V_b give ∏1_b ≥ ∏U_b − Σ_b(U_b−V_b)∏_{j≠b}U_j pointwise. ✓
- **Relative Haar error.** Blocks are independent under CRT given the pins. With v_b ≥ e^{−C₅m}, the relative gap per block is at most e^{C₅m}(eC₅m/s)^s ≤ e^{−A₀M}.
- **Coefficient count.** exp(O(MT)): lists are encoded by squarefree integers ≤ Z^{C₂}; repaired activations give at most two classes per prime; block expansions are bounded by (2+2me^{T2^{−b}})^{s+1}, with Σ_b T2^{−b} ≤ 2T. These counts are independent of c₀. ✓
- **Truncated even binomial ≥ 2^{−S}.** This follows from the Lagrange remainder of (1−x)^S at x=1/2: its sign is (−1)^{M+1}, and its size is at most binom(S,M+1)2^{−M−1}. Signs are respected when substituting envelopes term by term. ✓
- **Repair.** Prime rows are unchanged by the repair, and S(p)=0 is necessary for g(p)>K. ✓

### Row 3 (endpoint)

One private prime in (e^{20B}, e^{40B}], with B = cL^{1/4}. Mean ≍ B³, transfer cost exp(O(B⁴))/X. Monotonicity covers exp(CL^{1/4}), exp(L^α) for α > 1/4, and X^θ. ✓

### G′

**K=L.** Take log Z = L^u l^{b′}. The single-layer mean is L^δ l^{b′(s−1)−1/2}, and the transfer constraint W·log Z ≤ cL forces b′ ≤ 1/(2s). So W = L^{1−1/(e log 3)}/l^{1/(2e)}. ✓

**K=L^{log 3}: verified W = L^{2/3}l^{1/6}.** Take T = c₀L^{1/3}l^{−1/6} and R = L^{20}.
- H = (1/3)l − (7/6)log l + log c₀ + O(1), so e^{2H} ≍ c₀²L^{2/3}l^{−7/3}.
- Supply: about √l/log 2 dyads of [Ke^{−√l}, K], each contributing Σ3^{ω(d)}/q ≫ l². Total ≫ l^{5/2}.
- Layers [3H−5√l, 3H−4√l], with 3H = l − 3.5 log l + O(1). Here 3^{ω(d)+j} ≤ 3^l·e^{−4 log3·√l + O(log l)} < Ke^{−√l} ≤ q, since 4 log 3 ≈ 4.39 > 1. The tilted Poisson(3H) mass on the window is a positive constant (about Φ(−4)−Φ(−5)).
- Hence the mean is ≫ c₀²L^{2/3}l^{−7/3+5/2} = c₀²L^{2/3}l^{1/6}, with WT = c₈c₀³L.

The exponent **L^{2/3}l^{1/6} is correct.**

Structural points in G′:
- The seed targets are determined by the physical pin, whose log P = O(L^{0.0002}) = o(L). So the success indicator is a disjoint sum over exact lists with no residual congruence, and no unique-vector step is needed.
- Thinning to a common W per pin is legitimate.
- The BV loss with reciprocal weight over the dyads is ≪ l^{−A}.

### Unit repair and BV uniformity

The repair only makes the small digits units, so that (6) holds uniformly in z. The BV moduli are window moduli e ≤ K against primes ≥ K^{20}, and the bad-modulus deletions are independent of the pin. ✓

### Minor fix (BEYOND_34)

1. **l.151.** Change "`notes/z82/GAP11_JLL.md` §5 Thm 4 (unmerged in this worktree; `git show side-agent/…`)" to the merged path. GAP11_JLL is on `main` since 932ff71f3.

Optional remark: the G′ layer window at 4–5 standard deviations below the tilted mean gives a tiny but fixed constant. A window such as [3H−2√l, 3H−1.5√l] also satisfies 3^{ω(d)+j} < q (1.5 log 3 > 1). This changes constants only.

## GAP11_JLL

### Theorem 5

**Pan hypothesis.** I checked it against the on-disk Nath–Xie Thm 3.1 (`sources/window2/2501.16723.txt` l.316ff).
- That theorem requires f = O(1) on m ≤ x^{1−ε}, takes the maximum over y and over reduced a outside the m-sum, and has main term Σ_{(m,q)=1} f(m)π(y/m)/φ(q), for q ≤ x^{1/2}(log x)^{−B}.
- The note's use matches:
  - f(l) ≤ (h−1)! is independent of R, Q and the residue;
  - l ≤ X^{1−z} is imposed before Pan;
  - all sieve roots are reduced classes of lR;
  - the level is X^{τ}, τ = .4995 < 1/2;
  - weight multiplicities are handled by Cauchy with Shiu.
- R ≥ X^z/const follows automatically from the product dyad. R's badness follows from χ_q(lR) = +1 together with parity. Ordered h! multiplicity is fine for an upper bound. ✓

**Parity.** For p ≡ 1 (840):
- x₃ ≡ 1 (mod 3);
- x₇ ≡ 2 (mod 7), with (2/7) = 1.

So both bad counts are even. ✓

**l-independent weights.** The modified main law is the product law conditioned on the event "no root at ℓ|l" (deterministically true there). So E_mod[F] ≤ E[F]/P(A) = w(l)E[F] for every nonnegative F. This applies both to the Selberg square and to the product of the presieve and the two upper beta polynomials. ✓

**Pinned Buchstab budget.**
- The recursion uses the upper child at (J−I−1, I) for lower parents and the lower child at (J−I−1, I+1) for upper parents. The pins are excluded from their own tests.
- c_I = ½log((I+1)/I) is correct, since bad primes have density ½.
- The total modulus pins × residual level is at most X^{J_root/g} = X^{.4995}, the depth is bounded, and the multiplicities are divisor-type. Ordinary BV therefore suffices at the root. ✓

**Statement.** After subtracting cost3 and the even h≥6 cost7 (squares are negligible at X^{1−b}), the survivors have complete 3-failure and Ω_{7-inert}(x₇) ∈ {0,2,4}, with all such factors ≥ X^{.057}. My replica confirms the certified signs. ✓

### Theorem 6

**Validity of the new roots.**
- If the least bad prime r ≥ X^{.35} lies in window q, then x_q = c·m·r·r′, so m ≤ X/(2r²) ≤ X^{1−2t₀} ≤ X^v.
- Hence no q-good prime in (X^v, B] divides x_q. The max with η/300 only raises v, and B = X^{(τ−t₁)/2} < r.
- The roots −q at those primes are therefore legitimate exclusions on prime p. ✓

**V(w).**
- h_aug = h₀ + Δ multiplicatively. G_aug = Σ_n Δ(n)G₀(B/n) restricted to coprime l. n has at most 300 primes, each > X^v. G₀(y) ∝ log y. The harmonic measure is ds/(2s).
- Hence V(w) = Σ_j (2^j j!)^{−1}∫(1−Σs_i)∏ds_i/s_i.
- I verified the DDE V′ = (w−1)V(w−1)/(2w²) in closed form on [1,2]: V = 1 + ½(log w + 1/w − 1).
- The script's step is a valid lower bound: left numerator, right squared denominator, delayed left value.

**Cost per cell.** 2(t₁−t₀)/[t₀(τ−t₁)V(w)] follows from N/G_aug = U/(ηV), with r-density dt/(2t) per window. The remainders use moduli 840·r·[d,e] ≤ X^{τ}, under D(.957).

**Lower bound.** f₁(τ/.35) at s = 2.734 ∈ [2,4]. Triple misses are O(X/L^{5/2}) (z80 G), which forces g = 11. ✓

The label CONDITIONAL on ordinary D(.957) is correct, and the note claims no BV/EH-type unconditional result.

No fixes required for GAP11_JLL.

## After reading the earlier reviews

- **CAP_CONST R2 F1–F10** are applied in the current text: the least-prime moduli wording, Montgomery ⇒ GRH + Chowla, "effectivity not asserted", the unrefereed inputs in U's label, notation for §§6–9, and F7's "bounded by". The duplicate with Lane 1B's K is new in this review; it became visible only after CAP_TO_ES merged.
- **BEYOND_34 R2 corrections 1–5** are applied, including the §3 scope and "endpoint alternatively rel. K.1/L and (G)". The Lane 4 pointer is now stale in the other direction, since that note has merged.
- **GAP11 R3 fixes 1–4** are applied, including the π-bracket assert and Pan cited via Nath–Xie.

I find no disagreement with any earlier verdict.
