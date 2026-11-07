# Z61 TRANSPORT — CRT/reservoir rule DEAD; broader astra-1 DORMANT

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

The sections above are the pre-test registration, committed in `347514c6`. Final results follow.

## 4. Verdict

**Assessment: the frozen candidate is DEAD; astra-1 more generally is DORMANT, not disproved. ES remains OPEN.**
The exact kill is **termination at an illegal STUCK endpoint**, not a failed conservation identity or an infinite loop. At n=193 the source (f,ℓ,e)=(183,173,1) has no permitted destination, even with every numerator slot initially free. The rule cannot route this token to any of the actual hits f=15,39,103. There is also a guarded-implementation no-hit composite failure at n=105, (f,ℓ,e)=(103,101,1). Neither recorded failure is a timeout or matching-order artifact, but the composite diagnostic has the guard-order qualification below.

PROVED: the interior arithmetic, guarded valuation accounting and finiteness of the candidate list. **Not proved, and false as an unconditional property of this rule:** exhaustion only at a hit or a proper factor. The proposed potential therefore does not meet the requested legal-termination condition. No new moves were fitted after this kill.

The n=193 example does **not** refute a lemma conditional on *absence of every hit*: that premise is false there. What it refutes is the explicitly proposed unconditional local routing rule. Salvaging an absence-dependent boundary theorem would require a new independent argument. Declaring that some remote hit must exist is exactly the excluded endpoint assumption. Under the implemented guard order, the n=105 test additionally shows that actual absence of hits plus availability of proper factors does not make this rule total.

**Preregistration ambiguity, disclosed after hostile review:** §1 step 2 says “attempted destination,” whereas step 3 requires membership in F and the original stratum. The implementation checks those guards **before** applying destination gcd tests. The registration did not state that precedence unambiguously; it is not silently rewritten here. At n=105 the rejected raw proposal f′=17223 itself gives gcd(105,17223)=3, so testing raw proposals first would rescue that token. The composite example is therefore only a guarded-implementation diagnostic, not an interpretation-robust preregistered kill. The prime n=193 kill survives both interpretations: no raw proposal can produce a proper factor of a prime. No moves were enlarged after the kill.

## 5. What the construction genuinely establishes

### 5.1 Gcd-safe interior carry (PROVED)

Write f+1=gh, n+k=gc. Then

    a = kh−c,   gcd(h,c)=1,   M=8/gcd(g,8) divides h.

Thus gcd(a,h)=1 and gcd(a,M)=1. For a token q=ℓ^e|a:

- If ℓ|k, then ℓ|c, hence ℓ|n. Since k<n, ℓ is an explicit proper factor, not a formal sink.
- Otherwise ℓ∤c (else ℓ|h, contradicting gcd(h,c)=1), so gcd(ℓ,kMc)=1.
- In particular there is **no missing ℓ=2 case**: 2|a forces M=1 and k odd, unless the already certified factor exit applies.

Let R=rad(c), u=(kMR)⁻¹ mod q, and v equal u or u−q. At h′=h+MRv, every prime dividing c sees h′≡h, so gcd(h′,c)=1. Also gMR is divisible by 8. Provided the new f′=gh′−1 remains in the same quotient block and the allowed range,

    gcd(n+k,f′+1)=g,   a′=kh′−c=a+kMRv≡1 (mod q).

This is a real denominator-to-numerator carry, not a freely assigned valuation. Each fixed signed translation is injective in a fixed (k,g,ℓ,e) stratum. **The two signed choices together, and the reservoir, are not assumed jointly injective**: the explicit occupied-slot set enforces capacity across all of them.

Why the gcd padding matters: at n=53, f=31 gives (k,g,a)=(2,1,9). The naive step f′=39 makes the raw remainder 25≡1 (mod 3), but the new gcd is 5, so a′=5 and 3∤a′−1. Ignoring normalization invents a cancellation. The frozen rule avoids that error, at the cost of often enormous displacements. This example was part of the pre-test derivation, not an additional post-kill candidate.

### 5.2 Exact boundary reservoir (PROVED)

At k′=1 we necessarily have f′=n+r′. Write r′=g′A with g′|n+1 and C=(n+1)/g′. Then

    gcd(r′,f′+1)=g′ gcd(A,C).

Consequently the reservoir conditions in §1 give exactly the k′=1 columns carrying a q-numerator slot or a hit. They are not a heuristic fit. The upper bound g′A≤n+1 is the complete f≤2n+1 cutoff.

Implementation optimization, **not a new move**: after solving n+g′(1+qt)≡7 (mod 8), the admissible progression is A=A₀+qPt with P=8/gcd(g′q,8). If gcd(A₀,qP,C)>1, every term violates gcd(A,C)=1, so skip the entire progression. This avoids wasting the operational probe cap on, for example, odd g′ (where both A and C are necessarily even). An initial unoptimized run reached that cap; it was not counted as a mathematical failure. The optimized final run has **zero resource-capped tokens** and the same finite mathematical candidate set.

The 100000-probe operational guard remains: a future resource exhaustion is labelled `budget`, never `stuck`. None occurs in the archived final run.

### 5.3 Conserved flux and the failed potential (PROVED / Assessment)

For each prime ℓ let Dℓ be the number of initial denominator layers, Cℓ the number of consumed distinct finite numerator slots, Hℓ the tokens actually sent to an explicitly verified hit, Eℓ those actually sent to a verified proper factor, and Lℓ unresolved/live tokens. At every step,

    Dℓ = Cℓ + Hℓ + Eℓ + Lℓ,       Cℓ ≤ Σ_f,a_f>1 vℓ(a_f−1).

A move changes only which account holds the same labelled token; it never relabels ℓ. Factor exits accept foreign labels because their actual route has produced a compositeness certificate. This is a bookkeeping identity with certified failure of the prime hypothesis, **not** an identity asserting that a factor's own column contains those valuations. The square preflight sends every source token to its actual square-root certificate; its full flux is recorded in `squares.json`.

If no hit exists, no proper factor exists, and Lℓ=0 for all ℓ, the ledger implies vℓ(Q)≥0 for all ℓ, hence Q is an integer. Since 0<Q<1, that would contradict absence of a hit. The unsupplied ingredient is precisely L=0 at legal termination; the bookkeeping does not supply it.

For an active token there are at most two interior candidates and Σ_{g′|n+1}(1+floor(((n+1)/g′−1)/q)) reservoir proposals before filters. The number of source tokens is finite. Lexicographically, remaining source tokens and remaining candidates decrease. Thus the rule halts, but may halt **STUCK**. Advertising this as a potential proving *factor-or-hit termination* would conceal the exact missing theorem.

### 5.4 Exact kill and a larger-layer obstruction (PROVED; finite values CERTIFIED)

At n=193, f=183:

    k=2, r=a=173, g=1, h=184, c=195, M=8, R=195;
    kMR=3120≡6 (mod 173), u=29.

The proposed translated f values are 45423 and −224457, both outside F. In fact the failure is stronger than those two choices:

1. **No finite numerator slot labelled 173 exists anywhere in the complete table.**
2. Every same-(k,g)=(2,1) column has a=2h−195≡13 (mod 16), so none is a hit.
3. At k=1 a hit would have f=193+g′ for g′|194. The divisors 1,2,97,194 give no f≡7 (mod 8).
4. 193 is prime, so a proper-factor exit is impossible.

Thus even arbitrary destinations within this source's entire (k,g) stratum and the entire k=1 reservoir cannot finish the token. The complete hit list f=15 (r=2, word (2,8,13)), f=39 (r=2, word (2,20,5)) and f=103 (r=13) lies outside those destinations. There is no capacity contention to blame: `kill.json` starts with an empty occupied-slot set.

**Large-layer lemma (PROVED).** If n≡1 (mod 8), n≥41 and ℓ=n−20 is prime, then f=n−10 has k=2, g=1 and a=ℓ, but no nonzero numerator a_f−1 anywhere in F is divisible by ℓ.

*Proof.* At this source gcd(n−20,n−9)=gcd(ℓ,11)=1, so a=ℓ. At k=1, r is even and g≥2, hence a−1≤(n−1)/2<ℓ. At k≥3, f<n/2, so a−1<f<n/2<ℓ. At k=2, r and g are odd, so a−1 is even and at most n−5; its least possible positive multiple of the odd prime ℓ is 2ℓ=2n−40>n−5. ∎

This is **not** a no-go for all transports: it says a conserved ℓ-token in this family must reach a hit or a factor, rather than be cancelled against any finite numerator. At the prime 193 it must reach a hit. No infinitude of primes n with n−20 prime is claimed.

A separate cross-block warning, also checked independently: the complete n=193,k=3 block is

| f | g | a |
|---:|---:|---:|
| 71 | 4 | 5 |
| 79 | 4 | 11 |
| 87 | 4 | 17 |
| 95 | 4 | 23 |

Its 17-token cannot cancel or hit anywhere in that block, even if all gcd strata there are allowed. A cross-block rule is genuinely needed for some tokens; that fact does not construct one.

At n=105, f=103 gives k=2,g=1,a=101. The source gcd tests are all 1; both signed interior proposals, 17223 and −69233, are outside F, and there is no reservoir destination. Full enumeration certifies no hit anywhere and no finite 101-numerator slot. The implementation rejects both raw proposals before factor testing. But gcd(105,17223)=3: the raw arithmetic **does** expose a factor if out-of-range proposals are allowed to terminate there. This is a genuine no-hit failure of the guarded implementation, not a robust kill under the alternative reading of §1 step 2. The final verdict relies on n=193, which is unaffected by this ambiguity.

## 6. Tests and mandatory falsifier table

**CERTIFIED finite computation, not an all-input theorem.** Final run: 502 distinct inputs; 190 complete nonsquare token tables, 308 source-sampled nonsquare tables, 4 square preflights. A large-input sample uses at most 84 columns: f≤511 and five columns around each of n/3, n/2, n and 2n+1. The eight U₇-zero composites are always complete, even above the usual complete threshold 2000. Each sampled token's candidate list is searched exactly; the untested source tokens remain untested.

Results: **301 inputs have an actual STUCK token, 197 route all tested tokens, 4 exit at square factors**. No resource-capped token remains. “Routes all tested tokens” is deliberately not “proves U₇” or “complete transport” for a sampled input. An unrelated hit found by the separate witness scan does not change the routing verdict. Groups below overlap.

| mandatory screen | target check | frozen transport result | label |
|---|---|---|---|
| Odd squares 169,289,361,529 | complete U₇ zeros; exact rational products satisfy 0<Q<1 | explicit factors 13,17,19,23; every denominator label goes to that preflight certificate | PROVED + CERTIFIED; preflight is not new prime-specific content |
| Numerator-8 union control 131 | complete U⁽⁸⁾ zero; U₇ hit f=7,r=2 | all 34 denominator tokens reach hits; e.g. the actual reservoir hit f=135,r=4 is **not** a U⁽⁸⁾ hit (4∤17 and 8∤4) | CERTIFIED; the rule does use extra U₇ targets |
| All 12 C-even R₈-zero primes in `r8_zeros_1e10.txt` | 12 fresh U₇ certificates; R₈-zero status inherited from the screen, not re-proved here | 6 fail, 6 route the tested tokens; source samples only | CERTIFIED sampled routing; no numerator-8 theorem |
| All 285 R-zero composites | 277 fresh U₇ certificates; exactly the 8 below remain zeros (complete checks for those) | 261 fail, 24 route tested tokens; mixture of complete and sampled tables | CERTIFIED; not a universal composite-factor rule |
| Eight U₇ composite zeros | 105,1465,3865,4545,10305,12145,39361,67425: complete no-hit tables | all 8 have unresolved tokens, despite many actual proper-factor exits | CERTIFIED kill, including genuine no-hit inputs |
| All 14 (★)-zero primes | all have fresh U₇ hits | all 14 fail the frozen transport | CERTIFIED, complete for 409/577, sampled for larger members |
| All 38 𝔊*-zero primes | all have fresh U₇ hits | 28 fail, 10 route tested tokens | CERTIFIED; mixed complete/sampled |
| All 167 odd primes ≤1000 | all have fresh U₇ hits | 8 complete-table failures: 73,193,313,337,409,457,577,673 | CERTIFIED; no U₇ counterexample |

The numerator-8 union U⁽⁸⁾ and the C-even R₈ sub-line are distinct controls. Only the small union control is recomputed as a zero here; the twelve large R₈ zeros retain their cited z58 certification.

Detailed complete no-hit composite ledgers (columns count tokens, not distinct primes):

| n | actual factor-bound flux | finite matches | STUCK flux |
|---:|---:|---:|---:|
| 105 | 25 | 2 | 6 |
| 1465 | 467 | 83 | 83 |
| 3865 | 1469 | 182 | 185 |
| 4545 | 2238 | 64 | 143 |
| 10305 | 5327 | 135 | 286 |
| 12145 | 5492 | 344 | 438 |
| 39361 | 17763 | 1732 | 1696 |
| 67425 | 39059 | 647 | 1578 |

Reproduction of the board's restricted-exit objection:

| n | primes carried by nonunit columns' own a_f | overlap with positive global denominator surplus |
|---:|---|---|
| 169 | 3,13 | none |
| 289 | 3,7,13,17 | 17 |
| 361 | 3,5,7,19 | 7,19 |
| 529 | 3,11,23 | 11 |

At 169 the nonunit columns are exactly (f,a)=(39,13),(143,13),(247,39). The preflight foreign-token exit is legitimate because it produces 13, but it does not furnish a cancellation identity valid at composites. This resolves the *interpretation* of such an exit for this explicit rule; it does not resolve the missing prime-input routing mechanism in the board dispute.

## 7. Artifacts, reproduction and audit

- `scripts/z61_transport_rule.py`: frozen arithmetic rule, exact candidate enumeration, slot accounting, source scopes and fixture runner; standard library only.
- `scripts/z61_transport_check.py`: independent arithmetic implementation; does not import the engine. Checks archived explicit certificates, recomputes complete denominator ledgers and finite numerator capacities, multiplies the square products as exact Fractions, and proves the main kill by exhaustive permitted-destination enumeration.
- `data/z61/transport/fixtures.jsonl`: every input, category, factorization, separate U₇ witness, scope, per-ℓ ledger, endpoint counts and up to three route examples of each kind. Metadata factorizations and independently located hits are **not** available to `route` as exits.
- `summary.json`, `squares.json`, `kill.json`, `audit.json`: compact aggregates, square defects/flux, empty-capacity prime kill plus explicitly scoped composite diagnostic, and independent audit.

Commands (all computations use the prescribed limits):

```sh
ulimit -v 4000000
timeout 1800 uv run --no-project python scripts/z61_transport_rule.py
timeout 1800 uv run --no-project python scripts/z61_transport_check.py > data/z61/transport/audit.json
```

The independent checker verifies 502 inputs, 490 explicit U₇ certificates, 12 complete U₇ zeros, 190 complete token tables, the sources and positive endpoints of 3214 stored route examples, and four exact square products. It does not independently re-enumerate every archived STUCK route: it independently establishes the decisive prime obstruction and the guarded-composite diagnostic, verifies that the latter has an out-of-range raw factor exit, and checks the n=53 normalization trap. The code uses bounded LRU factorization caches and per-input token/slot structures, never O(n) storage on the ≈10¹⁰ fixtures.

**Assessment / stopping decision:** the constructive work produced a sound local carry, a sound boundary reservoir, and exact evidence that their union is not a factor-or-hit transport. The pre-registered kill fired well before the four-hour ceiling, so the attempt stops rather than adding adaptive moves to chase fixtures. There is no claimed new pointwise ES/U₇ mechanism. A future revival needs a genuinely new capacity-controlled gcd/quotient transition, not a renamed global hit search.

## 8. Hostile review and disposition

Deep-mode hostile reviewer, independent of the derivation, reviewed commits `347514c6` and `c898f950`; report in `data/z61/transport/review_hostile.md`. Recommendation: **retain DEAD / DORMANT, with documentation corrections**. No fatal error found in the prime kill, conservation, reservoir completeness, 2-adic argument or large-layer lemma.

Corrections applied: (1) disclosed the preregistration's factor-test/guard-order ambiguity and demoted n=105 to an interpretation-dependent diagnostic; its rejected raw proposal really yields factor 3; (2) added the omitted n=193 hit f=39. Neither changes the prime kill or routing data. No post-kill arithmetic move was added.

Reviewer independently checked all category memberships, aggregates, factorizations and scopes; 2507 positive route legalities; replayed 184 complete inputs ≤2000 with identical ledgers, including 2163 nonfactor 2-tokens; checked all square ledgers and the numerator-8 control. I checked the review's two findings directly: 193=2·20·5−2−5, and gcd(105,17223)=3. The final checker also records the raw-proposal caveat explicitly. This is an internal hostile review, not external mathematical certification.

**Final status: committed, reviewed, WAIT. No merge requested or performed. ES remains OPEN.**
