# PARITY hostile cross-review — ACCEPT-WITH-FIXES

Reviewed `side-agent/depth-parity` at `a223a23373daa32297359a723dba1b6a5dbec757`, including its cited rigidity/surface lemmas, source literature, C enumeration and statistical code. ES remains OPEN.
**Decision:** the core finite-group obstruction and parity reduction survive. “Narrowed” follows; an unrestricted class-number or fixed-modulus obstruction does not. Repair the quantitative hypothesis and scope statements before recording the results.

## Per-claim audit

| Claim | Classification | Independent derivation / finding |
|---|---|---|
| §2.1 finite generator menus give an all-element menu | CORRECT | In a fixed finite group, a shortest word has no repeated partial product, hence length < group order; level-preserving compositions remain affine over Q(n). Varying groups still require the explicitly fixed common menu. |
| §2.1 squares subgroup and odd-order elements | CORRECT | The quotient by all squares has exponent 2, hence is an elementary abelian 2-group; its characters separate points. Thus the squares subgroup is the intersection of index-≤2 subgroups. Odd-order elements are squares. |
| Lemma A: fixed proper Z, generic action id/swap | CORRECT | Off Z₀ a used map preserves P identically. A degenerate map sends x into Z₁; the inverse group element uses the same menu, forcing x into Z₂. Images have dimension ≤2. Symmetrising preserves properness. Poles/rank exceptions remove only finitely many levels. |
| Affine classification used in A | CORRECT | For F=tuv−u−v−n, cubic terms force a monomial linear part, quadratic terms force translations zero, and n≠0 forces multiplier 1. Linear terms fix u,v up to swap; the cubic coefficient then fixes t. This works over Q(n), including composed words. |
| (A,B,t) n-independent extension | CORRECT | Scaling by r/s≠1 can preserve integral X only when t divides r−s; add finitely many planes. Pull Z back by the dominant morphism (t,u,v)↦(tu−1,tv−1,t); properness and swap invariance survive. No n-dependent SL₂ claim follows. |
| Lemma B(i)–(iv) | CORRECT | Orbits have size ≤2, so stabilisers contain squares. Injectivity on each swap-pair forces the two stabilisers to coincide. Fixed-point sets and singleton-orbit points are swap-stable; without x₀ they therefore have even size. |
| Lemma D(b),(c), existence of line | CORRECT | A polynomial vanishing on every positive grid point t≡1(4), u≡23(24) vanishes identically. Thus some vertical line escapes Z. With q=tu−1, v=(p+u)/q≡0(4), P=p, and the two A-values are 2 and 3 mod 4. A proper closed subset of that line is finite. |
| Lemma D(a), “Dirichlet only” density | CORRECT-WITH-FIX | q≡2(4), gcd(u,q)=1 and −u≡1(24) make the CRT class reduced. Dirichlet gives infinitude; PNT in fixed arithmetic progressions gives the claimed natural relative density φ(24)/φ(lcm(24,4q)). |
| Theorem C | CORRECT-WITH-FIX | For R1, squares fix x_p, contradicting x_p∉E. For R2, its orbit has size 1 or 2 (size 1 if Γ=Γ^(2)), is nonzero mod m under the stated hypotheses, and contains no E-point. Thus F∩P is finite. Only the density attribution needs the preceding fix; no unproved hypothesis is needed. |
| Theorem D: E(p)∩Z≠∅ | CORRECT | If x₀ were generic, its singleton orbit would violate either rule, so x₀∈Z. Under R1′ subtract the even generic fixed-point count from the odd total. Under R2′ subtract the even generic singleton count from the odd total of odd-orbit points; an odd orbit remains wholly in invariant Z and meets E. |
| D: unconditional/no-cylinder and H consequences | CORRECT | The cited surface theorem needs only the fixed-Z conclusion, not an actual involution. Off finitely many axis lines, noncylindrical components contribute O(N^(2/3)) points; finite-integer-point cylinders reduce to lines. The same hypotheses and the specified α₀ apply. |
| D: quantitative BH consequence “in the precise form of Thm 6.1(d)” | GAP | The cited source itself conflates a weak lower bound >C_Z Y^(2/3) with a BH-order lower bound. The former does not imply ≫N/(log N)^s after deleting O(N^(2/3)) exceptions. The latter does. See required fix 1. |
| §2.7 general finite-symmetry principle / §2.8 exclusions | CORRECT | Generic orbits lying in H-orbits have size ≤|H|; excluding certificates still needs a separate analogue of Lemma D. Arbitrary subsets need not contain its line points or be swap-invariant. External odd-modulus counts are not excluded. |
| §3.1: X=2NE+1 and R even | CORRECT | A diagonal word has u=v dividing p; only u=1 is possible, giving x₀. Swap has no fixed point on the t≡0(4) words: u(4uC−2)=p has no positive solution for u=1 or p. |
| §3.1: f_II even and unordered interpretation | CORRECT | c divides a+b, so swapping a,b preserves gcd(a,c)=1. A diagonal forces a divides p; a=1 gives c(4d−p)=2, impossible for p≡1(4), and a=p gives c(4pd−1)=2. Thus ordered pairs come in twos. |
| §3.1 bichromatic/five-slot identity | CORRECT | Av=p+u gives (A/p)=(u/p)(v/p). The cited mod-8 five-slot identity supplies the sign equivalence; the small independent enumeration and all saved mismatch columns agree. This is five-slice ES, not unrestricted ES. |
| §3.1 quartic-2 identity and §3.2 class-number inputs | CORRECT | Original Barrucand–Cohn criterion verified below. Expanding (−4)^((p−1)/8) gives (−1)^((p−1)/8)2^((p−1)/4); the latter factor is ±1 for p≡1(8). This gives exactly the stated XOR. |
| §3 numerical nonassociation and finite-law exclusion | CORRECT as EVIDENCE / bounded CERTIFIED statement | Decisive recomputations agree below. Determinism is excluded for M dividing 6160, not for arbitrary M or arbitrary class-group data. |
| §§3.5–3.6, 4, 6 stronger statistical prose | CORRECT-WITH-FIX | Nonreplication does not prove the deviations were noise, and common-OR intervals do not bound every interaction or future-range association. “No fixed-modulus law exists” exceeds the certified scope. |

## Decisive computations reproduced

All execution used `ulimit -v 6000000` and explicit timeouts (≤400 seconds per computational command). The independent script uses O(N) arrays and a 5-million-byte segmented sieve, not Cartesian-product allocations.

- Fresh `gcc -O2 -Wall -Wextra` build; enumeration through 10⁶ reproduces all **9,732 rows byte-for-byte**.
- The lane's independent direct-word / direct-Type-II / reduced-form brute checker agrees on all six counts at **89 primes ≤6000**, zero mismatches.
- Fresh Lemma D sanity run through 3·10⁶: progression counts **2701, 1516, 1227, 95, 37**, matching the five quoted frequencies and certificate failures.
- New `scripts/z52d_xrev_parity_check.py` imports none of the lane's analysis code. Its segmented sieve independently verifies **every prime row**, completeness, order and uniqueness through 2·10⁸: **719,781 + 664,109 = 1,383,890**.
- Independent CMH, generalized CMH and RBG interval calculations reproduce the class-bit tables on both ranges and pooled. Initial NE vs b16|b8: **−2.795306** (mod 16), **−2.821485** (mod 6160); replication: **+0.937086**, **+0.867190**.
- Initial UII vs b8 **−2.098823**, replication **+0.041977**. NE vs hq: χ² **10.015591**, p **0.018434**; replication χ² **1.021855**, p **0.795964**.
- Pooled largest class-bit |log OR| **0.0073373434**; largest nominal 95% interval endpoint magnitude **0.0167684247**. These agree at the memo's precision; use 0.0074 if an actual upper bound rather than rounding is intended.
- For **each** of the five bits, all **1,920** occupied (p mod 6160,h mod 16) classes contain both values, independently verified at ≤10⁷ and on (10⁸,2·10⁸]. These are genuine finite counterexamples to every claimed law with M dividing 6160.
- All **1,383,890** stored rows satisfy the quartic-2 XOR identity, even f_II, h divisible by 4 and zero five-slot/sign mismatches. Exactly the stated **14 R-zeros** occur below 10⁸; none in the replication range.
- Fully reran `z52d_parity_corr.py` separately on both ranges: each output is **byte-identical** to its committed `corr_1e8.txt` / `corr_2e8.txt`. This also reproduces the controls, representation checks, heterogeneity/twist tests and all five replication outcomes.
- Git records preregistration in `32f1adce` before replication data were committed in `bed7b0d0`; this verifies commit ordering, not whether running output was unseen.
- Limit: the full six-count arithmetic enumeration was not rerun through 2·10⁸; full-range statistics use the stored rows, with fresh small-range enumeration, code inspection and independent prime completeness checks.

Reproduction after extracting the lane files to `/tmp/xrev_PARITY`:
```
ulimit -v 6000000
timeout 300 uv run --with numpy --with scipy python scripts/z52d_xrev_parity_check.py /tmp/xrev_PARITY
```

## Source verification

- **Barrucand–Cohn**, original 1969 paper, pp. 67–70, read from the Göttingen scans linked by [EuDML](https://eudml.org/doc/183503). On p. 67 equations (1)–(4), and p. 68 Main Theorem (6b),(6d),(6e), the hypotheses are precisely p≡1(8), and the equivalence is x²+32y² ↔ eighth-power residuacity of −4 ↔ 8 dividing the class number of Q(√−p). Its discriminant here is −4p. No missing congruence hypothesis.
- Scan entry: [p. 67](https://manifests.sub.uni-goettingen.de/iiif/image/gdz:PPN243919689_0238:00000071/full/1400,/0/default.jpg); subsequent pages are image indices 72–74. This removes the memo's reliance on search snippets for the decisive criterion.
- **Koymans**, [arXiv:1809.07167](https://arxiv.org/html/1809.07167), introduction, Theorem 1.1, §4: checked the 1/16 density over all primes, the known 8-rank governing field, 4|h iff p≡1(8), and the paper's statement that 16-rank governing-field existence/nonexistence was unknown. The paper does **not** supply the progression-mod-3 density; the memo correctly labels 1/4 there expected/observed. Its historical “unknown” statement is not a survey of subsequent literature.

## Required fixes, in priority order

1. **MAJOR — quantitative hypothesis.** In Theorem D and every cross-reference to the “precise” weak bound of INVOLUTION_ES2 6.1(d), assume the BH-order lower bound `#admissible y≤Y ≫ Y/(log Y)^|S|` for the quantitative conclusion. Subtracting O(Y^(2/3)) then proves it. A weaker `≫Y^(2/3+δ)` gives a correspondingly weaker count, not the stated BH-order count. Flag the inherited mismatch for the parent; do not propagate it as a theorem.
2. **MAJOR — scope/labels.** Replace §6's “no fixed-modulus law exists” with “no law Y=f(p mod M,h mod 16) with M dividing 6160.” A modulus larger than the entire finite sample can distinguish every sampled prime, so finite data cannot rule out all moduli. Replace “Any association is below…” by “the tested common-OR estimates and nominal intervals are…”. Replace “were multiple-testing fluctuations” by “did not replicate; consistent with fluctuations.” These do not rule out untested interactions, other class-group bits, or an auxiliary set.
3. **MINOR — density attribution.** Replace “only Dirichlet” by “Dirichlet for infinitude; PNT in fixed arithmetic progressions for natural density” in Lemma D/Theorem C and summaries. The result remains entirely unconditional.
4. **MINOR — statistical/literature precision.** State that χ² survival probabilities are evaluated numerically, while the χ² null approximations and 95% intervals are asymptotic/nominal, not exact finite-sample or simultaneous guarantees. In §3.6 say the 8-rank has a governing field and the 16-rank has a conjectural one, rather than asserting the whole 2-power part is known fixed-tower Frobenius data. Cite the original Barrucand–Cohn pages now verified.

**Final verdict: ACCEPT-WITH-FIXES.** Record the narrowly quantified finite-group theorem after these repairs. “Narrowed” is justified; “dead” applies only to Theorem C's specified rules on the full X with a fixed common finite affine menu. The parity case retains its stated conditional residue, and the class-number experiment remains negative evidence, not a universal obstruction or an ES result.
