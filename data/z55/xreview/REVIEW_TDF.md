# TDF hostile cross-model review

Reviewed `side-agent/z55-tdf` at `478d3e21c402c464513f98c49956711526c9b794` (`Z55_TDF.md`).
**Verdict: ACCEPT-WITH-FIXES.** The averaged theorem and pointwise constant-factor bound survive; §3.3 needs substantive corrections before recording its implication chain. ES remains OPEN.

## Per-claim audit

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| Lemma 0.1; §0 strip identification | CORRECT | Set s=km−n; conversely k=(n+s)/m. Interval length 2U<m gives uniqueness in s for each m, including U=2. |
| §0 divisor upper bound and lcm example | CORRECT | Sum over s of τ(n+s), then n≍U⁴ gives U^{1+ε}. At n=L−4U every m supports s=4U; exactly m=4U² has D=0, leaving 3U²−1 terms. |
| Lemma 2.1 | CORRECT | Expand the congruence by additive orthogonality, reduce b/m, and collect each denominator d dividing m. The sign is positive in both n and s. |
| Lemma 2.2 | CORRECT | Γ is the unnormalised finite Fourier transform of A; Parseval gives dΣ|A|² and discarding nonprimitive b only decreases the left side. |
| Lemma 2.3 | CORRECT | There are at most floor(4U²/d) multiples, each weight <U⁻²; hence 4ν/d. The occupancy bounds follow from the interval length. |
| Lemma 2.4′ | CORRECT | The increments θ are monotone in one integer gap. The cotangent variation is ≤2cot(πλ); Abel gives 2cot(πλ)+2≤2/λ. Empty/singleton sums are harmless. |
| Lemma 2.4 | CORRECT | The near-D=0 segment has ≤4h²d+1 terms. On the remainder, hd/(2U)≤abs(φ′)≤1/2; apply 2/λ to all partial sums, then decreasing-weight Abel to obtain 4/(hdU). |
| Lemma 2.5 | CORRECT | The three d-ranges give 32U log(2U), <45U, and ≤486h⁴U+725. Their sum is below the stated 2700h⁴U+32U log(2U). No primality assumption enters. |
| Full-period identity for 𝒢 | CORRECT | Every reduced denominator divides L; distinct characters are orthogonal over L. The identity does not require actually enumerating L. |
| Theorem LS | CORRECT | Circular spacing of reduced fractions is ≥Q⁻², Q=4U². The dual additive large sieve gives (N+Q²−1)𝒢, hence the displayed weaker bound. Translation by any signed M only rotates coefficients. Source checked below. |
| Corollary 2.2 | CORRECT | Union/Chebyshev gives U^{2η−2}Σ_{h≤H}Σ_n abs(T_n(h))²; Σh⁴≤H⁵ yields the claimed expression. |
| Corollaries 2.3–2.4 | CORRECT | N=O(U⁴), H=floor(U^η) give O(U^{3+7η}log U). Dividing by U⁴/log U tends to zero precisely for the stated η<1/7. PNT applies on a fixed-ratio interval; U is fixed for each exceptional set, not simultaneously quantified. Z54 Cor T then applies at each good prime. |
| §2.5 first-moment comparison | CORRECT | For each ordered (u,B), product divisibility selects one residue class modulo uB, giving ≤N/(uB)+1. Summation is O(N+U²), and Markov beats the displayed LS-based N₂ bound. |
| Proposition 2.6 | CORRECT | Two-cycle vertices are disjoint; N₂≤abs(dom f)/2. Floor subtraction gives Ulog2 plus two ψ-sums. Pair (1/14,11/14) gives h^{1/14}U^{13/14}; Vaaler and H≈U^{1/15} give U^{14/15}. Constants depend only on the fixed fourth-root range. |
| §3.2 elementary exponent inequality | CORRECT | κ≥0 and λ≥1/2 imply (1/2−2κ)/λ≤1; equality forces (0,1/2). The heuristic displayed bound cannot save a power when K≥16U. This is not a theorem excluding joint-variable methods. |
| §3.3 h-square expansion and kernel bound | CORRECT | Expand abs(T)², interchange finite sums, then apply the geometric-sum bound and triangle inequality; interpret inverse distance at zero as infinity. |
| §3.3 DC(1/H) ⇒ h-mean-square bound | CORRECT | DC includes total mass O(U). Each 1/H annulus around each point contains O(U/H) points; weighting by H/j and summing gives O(U²log(2H)). Cauchy and Theorem T yield the advertised half-exponent saving. |
| §3.3 DC(U⁻η) ⇒ N₂≪U^{1−η} | CORRECT-WITH-FIX | Only inclusion of cycle levels in the integer-square event is needed. The asserted equality of these sets is WRONG: block-root restrictions are missing. Explicit admissible prime counterexample below. |
| §3.3 TD(η) ⇒ DC(U⁻η) | GAP | Nonzero Fourier control does not bound the zero coefficient M=abs(E1⁺). Only M≪εU^{1+ε} is proved; DC as defined also requires M≪U. Neither Erdős–Turán nor the local majorant removes this missing input. |
| §3.3 equal-discriminant multiplicity | CORRECT | m divides both n²−s² and s²−D, hence n²−D; a given m determines s and k. Here n²−D>0. Thus r(D)≤τ(n²−D). |
| §3.1–3.4 method assessments | CORRECT-WITH-FIX | Self-duality and stationary-phase sizes remain assessments, not universal impossibility results. Do not call DC a proved weakening of TD until the gap is repaired. |

## Required fixes, in priority order

1. **Remove or repair TD ⇒ DC at its stated normalisation.** Write M=abs(E1⁺), H=floor(U^η), B=U^{1−η}. A local nonnegative Fourier majorant gives, for arcs of length t≥1/H,
   `#(w mod 1 in I) ≪ t(M+HB) ≪ t(M+U)`.
   The memo supplies M≪εU^{1+ε}, not M≪U. A valid replacement is DCε: `#(I) ≪ε U^{1+ε}|I|`, implying N₂≪εU^{1−η+ε}; alternatively add the genuinely additional hypothesis M≪U. Update the opening paragraph, §1 item 3, and §3.3 accordingly. This is a proof gap, not an arithmetic counterexample to TD or DC. Repeated equally spaced phases have arbitrarily large M and vanishing first H Fourier modes, illustrating why the cited Fourier theorem alone cannot supply the missing zero mode.
2. **Replace “exactly” by “a subset” for square discriminants.** At U=10, p=16139 (prime), k=77, m=210, s=31, D=121, all strip conditions and p≥16U³ hold, but the roots are 10 and 21, neither in (10,20]. This is a square point, not a block two-cycle. Keep the bound DC ⇒ N₂: its proof requires only the valid injection. Z54 Lemma A explicitly retains the omitted root restrictions.
3. **Scope labels and numerical extrapolation.** Replace “only the two ... marked PROVED” (§3 introduction and §5 table) by a list or “explicitly marked claims”: there are more than two, including the gap above. Replace numerical evidence “at every scale” by “on these sampled short windows”; three small-U Farey runs and two mean-square windows do not justify that universal wording. The opening almost-all-prime summary should explicitly repeat “for each fixed U”.

## Numerical reproduction and independent checks

All shell invocations used `ulimit -v 6000000` (one initial navigation command used a smaller limit) and an outer `timeout`; no full Cartesian-product arrays were allocated.
The original scripts were inspected before execution and extracted to `/tmp/xrev_TDF` at the reviewed commit. No CERTIFIED claims occur; floating-point results remain EVIDENCE.

| Check | Result |
|---|---|
| Original Farey script: (U,h,N)=(6,1,3000),(10,1,2000),(10,3,2000) | All stored output reproduced, including discrepancies 1.61e−11, 2.08e−10, 1.72e−10 and LS ratios 0.1270, 0.01201, 0.01256. |
| Independent CRT computation of full-period mass (no FFT) | 𝒢=9.4059091964, 15.8419220926, 16.1280142628; agrees with all three stored masses. Uses event-intersection density 1/lcm(m,m′) when gcd(m,m′) divides s−s′, zero otherwise. |
| Independently recomputed mass for d≤2U | 9.298%, 6.821%, 8.847%, respectively; agrees with the stated 6.8–9.3% range. |
| Pointwise script, U=300 and 1000, h=1..8, all four primes per U | All eight rows reproduce; E1⁺ ranges 398–465 and 1472–1596, and abs(T) ranges 2.0–39.9 and 6.7–87.3. |
| Mean-square script, U=100, N=4000 | 222 primes; mean E1⁺=152.13; six means 151.9,149.7,149.6,158.0,150.8,150.7; prime means reproduce. |
| Mean-square script, U=300, N=3000 | 124 primes; mean E1⁺=441.58; six means 428.6,440.0,451.6,446.2,439.1,432.9; prime means reproduce. |
| Exact square-event counterexample | Trial-division primality and all integer strip/root conditions checked by `scripts/z55_xrev_tdf_check.py`. |

Reproduction: original Farey arguments as in the table; numerics arguments `point 300 8`, `point 1000 8`, `meansq 100 6 100000000 4000`, `meansq 300 6 8100000000 3000`.
Use `ulimit -v 6000000; timeout 240s uv run --with numpy python /tmp/xrev_TDF/scripts/<script>.py <args>` per run.
Independent check: `ulimit -v 6000000; timeout 120s uv run python scripts/z55_xrev_tdf_check.py` (passed; dependency-free, ≤2805 support records, streamed pairs).

## Source checks and overall disposition

- [Kedlaya, Notes on analytic number theory, Ch. 15](https://kskedlaya.org/ant/chap-largesieve.html): read Theorem 15.5, duality Lemma 15.4, and the proof. They verify the exact hypotheses and the needed N+δ⁻¹ dual bound. The attempted original Montgomery–Vaughan PDF returned HTTP 403; this accessible source supplies the proof, not merely a search snippet.
- [Baier, Lectures on exponential sums](https://www.atmschools.org/sites/default/files/Baier-Lectures_on_expo_sums.pdf): downloaded/read Theorem 5 and Lemma 6 (pp. 5–6), Theorem 14 (p. 12), and §6.1–6.2 (pp. 23–27). These verify the Vaaler ψ-bound, derivative scale L=abs(f′), A-process formula, pair (1/14,11/14), and the reciprocal-phase substitution. Independently, Theorem 14 with q=2, Q=4, abs(f⁽⁴⁾)≍h/U gives the same main term h^{1/14}U^{13/14}; its auxiliary terms U^{7/8} and h^{−1/8}U^{11/16} are smaller. Thus the derivative hypotheses and omitted terms do not obstruct Proposition 2.6. The memo's Kusmin–Landau proof was checked directly and does not depend on its book citation.

The justified verdict is **strengthened in n-average, still narrowed/unresolved pointwise**, not “dead”. LS proves a uniform long-window mean-square upper bound, not an asymptotic and not an individual-prime estimate. Proposition 2.6 gives a genuine constant-factor pointwise improvement, not a power saving. The exceptional-set quantifiers are honest in the corollaries. No assertion about existence of Erdős–Straus solutions follows. Accept the main results subject to the explicit §3.3 fixes; do not record the uncorrected TD ⇒ DC implication as PROVED.
