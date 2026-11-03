# Hostile cross-review: Z55_TDO

Reviewed `side-agent/z55-tdo` at `0011e787e6280817bac2b95b46ad7593c8b113d8`.
**Verdict: ACCEPT-WITH-FIXES (minor proof/citation endpoint fix, not a substantive gap).**
Theorems M and A survive independent re-derivation. Pointwise TD is not proved; ES remains OPEN.

## Per-claim findings

| Claim | Classification | Independent check / qualification |
|---|---|---|
| Lemma 1.1, one point per m | CORRECT | For U ≥ 5, 4U < U² < m; the s-window lies in one complete residue interval. Its sole possible representative is (−n mod m), and k=(n+s)/m is positive. |
| Lemma 1.2, phases and discriminants | CORRECT | w=2B−s=s−2u and hs is integral. Given integral m=(s²−D)/4, recover k uniquely. Divisibility is understood in the integers; parity alone would not ensure integral m (see clarification below). |
| Lemma V | CORRECT-WITH-FIX | Curvature and both geometric sums are correct; explicitly dispose of singleton blocks before invoking the cited theorem, whose interval-length hypothesis is omitted in the memo. |
| Theorem M | CORRECT | Reduced fractions remove repeated frequencies; denominator-q coefficient is O(√(hU)/q), so coefficient energy is O(hU log U), and dual large sieve gives the claimed bound. |
| Lemma 4.1 | CORRECT | The phase and discriminant restriction do not depend on U. Every point in the symmetric difference crosses one of the four listed s/m boundaries. |
| Lemma 4.2 | CORRECT | Fourier expansion is legitimate since 8U₀ < U₀². Both interval-collision and reciprocal-multiple estimates give precisely the displayed boundary energy. |
| Theorem A, including every U at once | CORRECT | The mesh covers all admissible integral U, the frequency union costs H₀², and the three final exponents are absorbed for strictly η<1/8. No primality input is hidden. |
| Remark 4.3 | CORRECT | Ordered enlarged-box pairs majorize unordered cycles; summing each divisibility condition costs ≤ X/(uB)+1. Markov at the fixed threshold followed by the same mesh gives XU_*^(−1+4η). |
| Table 5.1, Lemma V grid, square controls, sanity example | EVIDENCE AGREES | All 1,108 stored scan rows and five Lemma V grid outputs reproduce; independent enumeration checks representative rows at every scale. These are not certificates for arbitrary p or h. |
| §6 obstruction/Poisson discussion | Assessment, not a theorem | Its final disclaimer is essential. The unproved double-Poisson sketch and exponent-pair comparison do not establish necessity of any method, or kill pointwise TD. |

## Proof audit details

1. **Lemma V.** On w≈2^j, the integer span is O(4^j/√m), and
   λ_j=4hm·2^(−3(j+1)) bounds |g″| from below, with ratio at most 8 above.
   Blocks with 4^j≤√m contain at most one point and contribute O(log U).
   For other blocks with at least two points, remove the first point and apply the test on their real span:
   O(√h·2^(j/2)+2^(3j/2)/√(hm)), with the removed point absorbed in the first term.
   Summing 2^j<4U gives O(√(hU)+√(U/h)); h≥1 absorbs this and O(log U).
   Singleton large-j blocks obey the same bound trivially. There is no logarithmic loss beyond this.
2. **Theorem M.** The sign is consistent: −b/m=a/q and f̂_m(−am/q)=S_m(−a/q)/m.
   Each reduced a/q appears once after summing all m divisible by q; q=1 includes the zero frequency.
   The harmonic sum on (A,4A] is ≤1+log 4 even when A<1, so |C(a/q)|≤2.39 C_V√(hU)/q.
   Summing φ(q)/q²≤1+log Q gives ≤5.72 C_V²hU(1+log Q).
   Distinct reduced fractions, including wraparound at zero, are Q^(−2)-separated.
   The sieve factor N−1+Q² (or the sufficient weaker N+Q²) is uniform in the starting integer N₀.
3. **Lemma 4.2.** For a union S of at most two integer intervals, each residue has at most |S|/q+2 members.
   Thus Σ_a|E_S(a/q)|²=q·#{s≡s′}≤q|S|(|S|/q+2); dropping coprimality only increases the sum.
   For B¹ the resulting energy is O(G²+G log U₀).
   For B², weight ≤15G/(U₀q)+2/U₀² and |S₀|≤6U₀ give energy
   O(G²Σ(q^(−2)+(U₀q)^(−1))+U₀^(−3)Σ(U₀+q))=O(G²+U₀), since q≤16U₀².
   The union's possible double counting is harmless: B≤B¹+B², followed by (x+y)²≤2x²+2y².
4. **Theorem A.** G≈U_*^(1−3η), H₀≈U_*^η, and there are O(U_*^(3η)) grid points.
   Per-grid exceptional counts are O(XU_*^(−1+4η)log U_*) and
   O(X(U_*^(−4η)+U_*^(−1+2η))). The G log U_* term is absorbed by G² for large X.
   Their mesh union is O(X[U_*^(−1+7η)log U_*+U_*^(−η)+U_*^(−1+5η)]).
   The strict inequality 8η<1 absorbs the logarithm; 6η<1 absorbs the last term.
   The complement gives |T_{n,U}(h)|≤2U_*^(1−η)≤2U^(1−η), simultaneously for every admissible U,h.
   Dividing the integer exceptional bound by the dyadic prime count gives the stated prime fraction.
5. **Remark 4.3.** The enlarged box has O(U_*²) pairs and bounded Σ1/(uB), so its first moment is O(X).
   The mesh union costs XU_*^(−1+4η), smaller than XU_*^(−η) here. Thus the lack of new downstream
   content for the almost-all version of the balanced-block upper bound is correctly acknowledged.

## Citation verification

- Titchmarsh, *The Theory of the Riemann Zeta-function*, Thm 5.9, printed p.104, checked in the
  [primary scan](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf) (PDF p.57).
  It states the quoted O(α(b−a)√λ+λ^(−1/2)) bound, but also requires **b≥a+1**.
- The exact additive large-sieve statement and duality were checked in
  [Kedlaya, Theorem 15.5 and Lemma 15.4](https://kskedlaya.org/ant/chap-largesieve.html#T-large-sieve).
  Its proof gives N+δ^(−1), already sufficient here; its statement gives N−1+δ^(−1).
  The original Montgomery–Vaughan repository PDF returned HTTP 403, so primary-source retrieval for that
  attribution is not claimed. The available theorem/proof verifies the actual application and hypotheses.

## Numerical audit

All execution used `ulimit -v 6000000`, a CPU limit, and an enclosing timeout (at most 240 seconds).
The original C programs were rebuilt and rerun: 200 primes at each of 10^8,10^10,10^12,10^14;
300 consecutive integers at 10^12; and all eight odd squares. Every stored output row agrees exactly.
The 4096-frequency Lemma V check also agrees exactly: 3.369, 3.308, 3.766, 4.178, 3.333.
Recomputed Table 5.1 tuples (candidate mean/U, mean max/√U, maximum max/√U, mean square/U):

| Sample | Recomputed tuple |
|---|---|
| primes 10^8 | 1.513000, 1.993815, 3.896900, 1.519655 |
| primes 10^10 | 1.520538, 1.923711, 3.499586, 1.454204 |
| primes 10^12 | 1.543970, 2.008372, 3.127176, 1.533136 |
| primes 10^14 | 1.535944, 2.002370, 3.527283, 1.533583 |
| all integers 10^12 | 1.629137, 2.023887, 3.705873, 1.575360 |

Square ranges are [0.994157,2.594333] and [0.704332,2.710039]; all memo rounding agrees.
The sanity example gives |E1|=253, |E1⁺|=159, N₂=1.
`scripts/z55_xrev_tdo_check.py` independently scans levels k rather than residues modulo m and evaluates
h=1,…,8 for one row from each of the six datasets, agreeing within the stored 0.001 precision.
It also passes 150 small-input strip/phase checks, 180 boundary inclusions, and residue-collision checks
for four boxes, including G=1 and G=U₀. Storage is bounded by the individual sparse strip/interval sets.

## Required fix and clarifications (priority order)

1. **Required, minor:** In Lemma V's large-j paragraph, handle |R_j|≤1 trivially before applying Thm 5.9;
   include b−a≥1 in the quotation. This case actually occurs: U=5,m=89,j=2 has R_j={20}, while 16>√89.
   No statement, exponent, or subsequent proof changes.
2. **Clarification:** Write D≡s² (mod 4), or explicitly require m∈ℤ, in N_D's definition. The current formula
   is valid with ordinary integer divisibility; s≡D (mod 2) alone is not a sufficient integrality test.
3. **Scope wording:** Replace §6's “frequencies … must be summed with absolute values” by “the attempted
   implementation sums frequencies with absolute values.” Its Assessment disclaimer prevents a formal
   overclaim, but no universal necessity or theorem about the sketched two-variable sum has been proved.

**Lane outcome:** strengthened averaged theory, with the pointwise target still unresolved—not dead.
Accept the proved mean-square/almost-all results after the minor endpoint repair; retain all heuristic labels.
