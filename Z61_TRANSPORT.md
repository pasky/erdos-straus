# Z61 TRANSPORT — preregistered factor-or-hit construction

**ES is OPEN. U₇ at every odd prime is CONJECTURE, not a theorem.**
Lane z61 TRANSPORT; board F2 = astra-1. Scope: one bounded construction attempt, not a campaign lane.
Started 2026-11-07 02:02 UTC; budget at most approximately four hours, with early stopping on a decisive kill.
This checkpoint precedes the lane's test runs. The derivation already exposes boundary risk at n=193; this is not a blind validation claim.

## 1. Target and pre-registration

For odd n ≥ 3 let F contain f ≡ 7 (mod 8), 7 ≤ f ≤ 2n+1, with r=(-n mod f)>0.
Set k=ceil(n/f), g=gcd(r,f+1)=gcd(n+k,f+1), a=r/g and Q=∏(a−1)/a.
PROVED (board reduction / Z60_LOPEZ §4.2): U₇(n) iff Q(n)=0. If F is nonempty and there is no hit, 0<Q<1.
A token is a denominator valuation layer (f,ℓ,e), 1≤e≤vℓ(a). A finite numerator slot is (f′,ℓ,e), with ℓ^e | a(f′)−1 and a(f′)>1.

**Frozen candidate: gcd-safe signed CRT carry with a k=1 divisor reservoir.**
No later enlargement of its moves after a failed test.

1. A square preflight s=isqrt(n), s²=n, s>1 returns the explicit proper factor s. This is deliberately elementary, not evidence for a prime-specific transport.
2. At a source or attempted destination, test gcd(n,f) and gcd(n,k); a gcd strictly between 1 and n is a proper-factor exit. Also test gcd(n,ℓ) at a source. Factors need not equal ℓ.
3. Interior move: write f+1=g h, n+k=g c, a=k h−c, M=8/gcd(g,8), R=rad(c). For q=ℓ^e, if gcd(ℓ,k)>1 this produces a proper factor. Otherwise put u=(kMR)⁻¹ mod q. Try the two translations h′=h+MRu and h′=h+MR(u−q), in order of increasing absolute displacement (positive first in a tie). A translated column is accepted only if it lies in F and has the original k and g. Check for a factor or hit, then consume its q-slot if unused.
4. Boundary completion: enumerate g′|n+1 in increasing order and A=1+qt, t≥0 in increasing order, subject to g′A≤n+1, n+g′A≡7 (mod 8), and gcd(A,(n+1)/g′)=1. Destination f′=n+g′A has k′=1, actual gcd g′ and a′=A. A=1 is an explicit hit, not an assumed endpoint. Otherwise consume its unused q-slot. These are arithmetic progressions with finite bounds, not a search of all witness columns.
5. If neither rule finds a free numerator slot, hit, or factor, return **STUCK**, an illegal endpoint and a kill certificate. No cycle, arbitrary remote-hit lookup, or free boundary sink is permitted.

Slots shared between different source tokens have unit capacity. Source order is increasing f, ℓ, e. A hit/factor absorbs only tokens actually sent to its certificate, except the explicitly specified square preflight. Tests will inspect token routes even when some other route already found a hit; otherwise success would merely report a witness search and never test the transport's local totality. Zero columns have no denominator tokens; their presence is reported separately, never used as an arbitrary global sink.

**Proposed potential:** finite remaining source tokens, then finite remaining candidate destinations for the active token (lexicographic). It proves termination including STUCK, not termination at legal exits. The distinction is a mandatory audit point.

**Ledger to verify:** for every ℓ, initial denominator tokens = matched numerator slots + hit-bound tokens + factor-bound tokens + unresolved/live tokens. No factor-exit capacity is inferred from its column's own ℓ-valuation. Under no hits/factors and no unresolved tokens this gives the desired denominator-cancellation inequalities. The missing assertion is totality of the rule, not this bookkeeping identity.

**Pre-registered kill:** any conservation/capacity error; nontermination; a STUCK token; or a purported proof of legal exhaustion that merely assumes a hit exists. The candidate dies on any such event. Broader astra-1 becomes dormant, not disproved. No forced repair or additional move fitting.

## 2. Planned mandatory falsifiers and bounded runs

- Odd squares: 169, 289, 361, 529 must return the explicit factors 13,17,19,23. Independently enumerate their nonzero Q ledgers and the board's restricted-exit obstruction.
- Numerator 8 / even sub-line: all 12 `data/z58/screens/r8_zeros_1e10.txt` primes, plus small genuine U⁽⁸⁾-zero controls. Distinguish R₈ from U⁽⁸⁾. Verify U₇ hits but do not claim a transport success from those hits alone.
- Composites: all 285 supplied R-zero composites, specifically the eight U₇ zeros 105,1465,3865,4545,10305,12145,39361,67425. Complete U₇-zero checks for those eight.
- Known prime zeros: all 14 (★)-zero primes and 38 𝔊*-zero primes; also a small-prime range. These are zeros of restricted families, not U₇ zeros.
- Complete token tables for small inputs; explicitly labelled source samples and exact individual certificates for large ones. Do not build an O(n) table for n≈10¹⁰. No global integrality claim from a source sample.

Scripts: `scripts/z61_transport_*`; outputs: `data/z61/transport/`. Python via uv; every computation timeout ≤1800 seconds and `ulimit -v 4000000`. Standard-library exact integer arithmetic; streaming/bounded candidate enumeration; no dense Cartesian products.

## 3. Status at checkpoint

CONDITIONAL: the interior injection and reservoir formulas have been derived but not yet independently audited. Assessment: boundary capacity is the probable kill. One independent deep-mode derivation corrected a suspected 2-adic obstruction: gcd(a,h)=1 and M|h imply gcd(a,M)=1. It also supplied the n=193,k=3 local-block deficit; this must be checked independently before banking it.

Final verdict, results, proofs and hostile review will be appended after the frozen test.
