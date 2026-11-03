# z54 cross-model review — EXACTSPIN

Reviewed `side-agent/z54-exactspin` at `706b2555b3424282b9b2266dfc300301d244f1fe`.
**Verdict: ACCEPT-WITH-FIXES.** The corrected algebra and scoped “narrowed” verdict survive.
The memo obtains no cancellation bound for the exact layer. **ES remains OPEN.**
This is an independent re-derivation and numerical audit, not adoption of the internal review's conclusions.

## Per-claim audit

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| §1 layer identity and conditional ES implication | CORRECT | Orthogonality gives the non-real-character remainder; `T_uw=R−G−T_u`. With the stated Thm X/U hypotheses, `G=M+T_w` and `R=G+S₂+S_o` give the asserted conditional lower bound. No unconditional implication is claimed. |
| Lemma 3.1(a,b) | CORRECT | `G²=A₂²×A_o`. Add/subtract `1[x∈G²]1[x_o=1]/|A₂²|`; Fourier expansion selects respectively `ψ₂²≠1` and `ψ₂²=1, ψ_o≠1`, exactly `4|ord ψ` and its non-real complement. |
| Lemma 3.1(c), square localisation | CORRECT | Both terms vanish off `G²`. At squares, `2wc=m²+u` and `(u,m)=1` imply `(c,m)=1`; reciprocity gives `(−c/u)=(u/c)=(−m²/c)=−1` for `c≡3 (4)`. The memo's abbreviated coprimality inference needs the shell equation, not merely `(c,u)=1`. |
| Lemma 3.2, including `Δ₆=−Δ₃` off genus | CORRECT | The annihilator sum is `|G/G^d|1[x∈G^d]`; Möbius inversion isolates exact order. If `4|k`, every contributing `d` is even. For `k=6`, the even terms vanish and the remaining terms are the negative of the `k=3` sum. |
| Lemma 3.3 | CORRECT | Equality of projections forces `G^K={1}`, equivalently every `ℓ−1|K`; the eligible prime list is finite. With `g=|G|, h=|G/G^K|`, the first/second moments are `1/g,h/g²`, giving `(h−1)/(g−1)≤h/g`. Fixed `K` gives `u^(−1+o(1))`. This is non-reconstruction, not a theorem excluding other arithmetic input. |
| Lemma 4.1 | CORRECT | Degree-one reduction identifies the surjective power map with a generator of the order-k characters; summing its primitive powers gives the Ramanujan sum. Shell congruence gives the factorisation. Only Frobenius values agree, not Kummer fields. On the intended `k≥3`, large-p window, `p>ℓ>k`, and the second radicand has p-valuation 1 while the first is a p-unit. |
| Lemma 4.2(a–c) | CORRECT | Cubic reciprocity for primary factors exchanges each unramified rational numerator/denominator; `−1` is a cube and the factor at 3 must remain. Conjugation inverts `μ₃`; split primes give `χ(π/π̄)`, inert primes give `(π/π̄)^(−(q+1)/3)`. On the norm-one group the rational symbol is `Ξ_q²=Ξ_q⁻¹`, nontrivial. The mod-9 supplementary assertion remains finite CERTIFIED evidence as labelled. |
| Lemma 4.3 | CORRECT | The unit norm map is onto; trace-surjective lifting gives equal-size kernel fibres. Summing the restricted nontrivial cubic character to exponent `e` vanishes unless `3|e`; CRT proves the result, including the cube exception. The quartic restriction is quadratic, hence vanishes when some `e` is odd. |
| Lemma 4.4(a–c) | CORRECT | The two quartic reciprocity signs at conjugate primes over `p` cancel. Replacing an odd rational `w≡3 (4)` by `−w` gives exactly the displayed supplementary sign. Writing `A=(π/ρ)₄, B=(π̄/ρ)₄`, the rational symbol is `A/B=A²/(AB)=(π/ρ)₂(ℓ/ρ)₄⁻¹`; the κ formula follows from `ℓ≡−p mod q`. |
| Lemma 4.5; Corollary 5.1(i) | CORRECT-WITH-FIX | `d≥4u−1` implies `u<d`, so fixed `d` fixes `u`; norm representations are bounded by units times `τ(u)`. For the shell use `w>Y≥U₁` and `c>4U₁`, then fixed `u` leaves divisors of `p+u`. Explicitly import these standing hypotheses from GENUSX §4; §1 currently states only the exponent gap. |
| Proposition 4.6 | CORRECT | CRT/local norm kernels give `|𝔑(c)|=c∏(1−χ₋₃(q)/q)`. The disc has at most one lattice representative per coset since `c>2√U₁`. The two conjugate primary primes each contribute `2 Re(symbol)/(ℓ−1)`, recovering the shell's `Δ₃` term. Non-cube fibres alone have mean zero; the cube count bound is correct. |
| Corollary 5.1(ii), theorem matching | CORRECT-WITH-FIX | No identification with the cited spins or theorem for these shell weights is supplied. The quadratic base fields have only involutions, incompatible with KM's inverse-free condition. But the proposed FRONTIER synopsis incorrectly assigns FIMR's totally-real/cyclic restriction to KM too; see fix 1. |
| Corollary 5.1(iii) | CORRECT-WITH-FIX | `ν≤1/[n²(12n+1)]` is correct. A relative saving tending to zero needs `ν log x→∞`; this implies `n=o((log x)^(1/3))`, not an equivalence with `n≲(log x)^(1/3)`. The upper bound on ν gives no sufficient range. |
| Proposition 5.2 | CORRECT-WITH-FIX | With non-cubes, the zero mode vanishes. Scaling gives `|f̂_r(m)|≪r²(1+r|m|)^(−B)`; the 2D lattice sum costs `r^(−2−A)`. Thus the relative upper bound is `C^((1−θ)(2+A)−δ)`, requiring `δ>(1−θ)(2+A)` for this estimate to decay. This does not bound the actual prime/window-weighted layer. Clarify the cube and expected-count wording in fix 3. |
| §5 hermitian identity / other escape hatches | CORRECT-WITH-FIX | The determinant and shear invariance are exact. Metaplectic applicability and conductor-uniform box estimates are honestly speculative. The split-prime factor in the inverse quartic product needs conjugating; see fix 4. |
| §§6–8 finite evidence and “narrowed” verdict | CORRECT-WITH-FIX | Decisive figures reproduce below. Sample-average diagnostics do not falsify an `o(log²p)` target merely by detecting nonzero standardized bias. The scoped obstruction statements support “narrowed,” not “dead.” |

## Required fixes, in priority order

1. **Correct the exported literature synopsis.** §8's proposed FRONTIER text says “FIMR / Koymans–Milovic … quadratic spins in totally real cyclic fields of degree ≥3.” This is false for KM: its dihedral theorem is over a totally complex degree-8 field, and its joint-spin theorem allows general Galois fields, including totally complex ones. Preserve the actual obstruction: no matching spin representation, quadratic-field involutions, nonmatching shell weights, and missing conductor/order uniformity. Replace unqualified “no theorem … exists” by “none is supplied/located.”
2. **Repair the falsifier's logical target.** §6 Design says a nonzero standardized mean would make `(Sp-k)` false or require a main term. Not so: a bias of size `b log p` with model standard deviation `log p` has nonzero mean z but is still `o(log²p)`. Detecting a residue-class bias is not falsifying the stated cancellation estimate; that requires a lower bound on the `log²p` scale along an unbounded sequence. The reported lack of individual-sample significance also does not erase the explicitly reported pooled `3.0 se` offset.
3. **Keep expected quantities separate from bounds in Props 4.6/5.2.** Specify a nonnegative bump of positive integral if assigning an “expected size” to `N_f`; no lower bound for `N_f` is proved. The cube term `O(r²C^(4/3+o(1)))` bounds the sum of **zero Fourier modes**, not the whole contribution of cube moduli in a shrinking disc. Keep cubes excluded or control their other modes separately. Justify the eventual expected count `<1` using the strict gap `1−γ−α₁>0`; `c>4U₁` alone does not absorb the unbounded Euler product.
4. **Fix the quartic escape-hatch product.** In §5 hatch 2, the factor in `∏_{q|w}(π_u/q)₄⁻¹` for split `q=κκ̄` is `(π_u/κ)₂·(−p/κ)₄`, not `(π_u/κ)₂·(−p/κ)₄⁻¹`. Lemma 4.4(c) itself correctly describes the non-inverted symbol. Distinguish the two in the synopsis.
5. **Make minor hypotheses/quantifiers explicit.** Import `Y≥U₁`, sufficiently large `p` with `8U₁X≤p`, and `k≥3` where ramification is discussed. Replace the growing-degree “i.e.” with the necessary little-o condition in the table; retain its heuristic label. In the square proof explicitly use `2wc=m²+u` for coprimality.

## Recomputations

All shell commands used `ulimit -v 6000000`, a CPU limit, and `timeout`; subprocesses inherit the limits and have explicit timeouts. Largest exhaustively enumerated ring: `125²` elements, streamed, not a large Cartesian-product array.

- Both supplied summary scripts reproduce `stats.txt` and `table.md` byte for byte.
- Independently reading all **9,800** unique rows gives maximum `|R−G−S₂−S_o|=1.0000000019161348e−6` (serialization rounding), and zero `badsplit` counters. All nonsquare rows are prime; all random-prime rows satisfy `p≡1 (24)`.
- All **600** square controls have `R=G=S₂=S_o=0`, every listed `4|k` layer zero, and `Δ₆=−Δ₃`. Mean `|Δ₃|`: **0.240016565, 0.262222455, 0.213670980**.
- Largest `|mean z(Δ_k)|`: **0.177699872** (`k=6`, near-squares `10¹⁰`); largest `|mean z|/se`: **2.884025818** (`k=24`, random `10¹²`). Pooled random `z(R−G)`: **0.032530966 ± 0.010836788**, `N=8,600`.
- Endpoint marginal-variance shares: **0.460479518 → 0.229724140**; variance shares of the selected sums: **0.473089025 → 0.237384014**. These are genuinely different statistics, correctly distinguished in the revised memo.
- Fresh engine runs reproduce every serialized field at `1000278361`, `1000106612521`, `100263186896737`, and square `1000002000001`. Separate exact-rational divisor enumeration reproduces `R,G,S₂,S_o` and shell counts at the first and last (263/137 and 3021/1526 shell/filtered points).
- All **24** dictionary runs reproduce from fresh shell dumps: **3,817 cubic; 7,822 quartic; 1,941 cubic cofactor; 8,093 split-factor checks**, all mismatch counters zero. The stored certificate has one duplicate line; counts here deduplicate by p, matching the memo.
- An additional global supplementary-factor check covers both primary conjugates at **181 distinct cubic u**, all **9** primary classes mod 9, with no conflicting values. The supplied checker alone resets this table at each p.
- Independent direct character enumeration checks **364 group elements** across `u=5,13,21,65,105,385`, verifying both character-support identities and exact-order Möbius inversion. Direct finite-ring residue-symbol computation checks **2,237 unit norm fibres**, including nonsquarefree/composite moduli and cube exceptions.

Reproduction after archiving the reviewed branch to `/tmp/xrev_EXACTSPIN` and compiling its engine there:
```sh
ulimit -v 6000000; ulimit -t 240
timeout 210s uv run --with sympy python scripts/z54_xrev_exactspin_check.py /tmp/xrev_EXACTSPIN /tmp/xrev_EXACTSPIN/engine
timeout 300s uv run --with sympy python scripts/z54_xrev_exactspin_check.py /tmp/xrev_EXACTSPIN /tmp/xrev_EXACTSPIN/engine --dictionary
```

## Decisive source checks

Read the actual PDFs: [FIMR, Thm 1.1 and introduction](https://arxiv.org/pdf/1110.6331), [KM joint spins, Thm 1 and §2.3](https://arxiv.org/pdf/1809.09597), and [KM dihedral spins, introduction and Thm 1](https://arxiv.org/pdf/1611.10337). They confirm the quoted exponents/conditionality and the correction in fix 1. Reciprocity conventions and formulas agree with [Booher, Thm 16](https://www.math.canterbury.ac.nz/~j.booher/expos/reciprocity.pdf) and [Dummit, Quartic Reciprocity in Z[i]](https://dummit.cos.northeastern.edu/teaching_sp21_4527/4527_lecture_31_quartic_reciprocity.pdf). These verify the laws used, not the memo's unverified Ireland–Rosen chapter pinpoint. The non-decisive broader literature survey is not independently certified here.

**Disposition:** preserve the decomposition, dictionaries, norm-fibre lemma, and explicitly scoped Fourier calculation. Apply the wording/sign/hypothesis fixes before exporting the FRONTIER text. No universal spin/Type-I no-go, fixed-p cancellation, or ES result is established.
