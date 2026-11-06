# z60 cross-model hostile review — MS105

**Verdict: ACCEPT-WITH-FIXES.** The principal proofs and census survive. Required fixes concern the falsifier table and reproduction claims, not a mathematical counterexample. **ES and (MS⁺₁₀₅) remain OPEN / CONJECTURE.**

Reviewed `side-agent/z60-ms105` at `e998fcbb02881a6601edf74d3fc6ab64d51a96b6`, including `Z60_MS105.md`, engines, runners, and committed data. This reviews the expanded kernel-≤100000 claim, not just the originally requested kernel-≤1000 claim. No full 83-billion-input replay is claimed.

## Per-claim findings

| Claim | Classification | Finding |
|---|---|---|
| Claim 0 | CORRECT | Reciprocity signs cancel for the odd part; when 2 divides t, d≡7 (8) supplies (2/d)=1. Coprimality follows from d≡−1 (4t). |
| Lemma 1, including sharpened sign | CORRECT | gcd(d,n)=gcd(d,u)=1; hence (n/d)=(s/d)=−1. If s divides uC, Claim 0 forces +1. Swapping u,B is valid. For g=gcd(s,uC), (g/d)=1 gives ((s/g)/d)=−1. Squarefreeness is unnecessary here. |
| Lemma 2 | CORRECT | g divides n; division gives the stated primitive solution and inverse. Terms s∣g vanish by Lemma 1. R₈ needs 2g∣C′; restricting to odd n makes the memo's inherited R₈ formulation valid. |
| Theorem 3(a),(b) | CORRECT | The univariate, nonconstant, positive-leading-coefficient theorem follows by the six steps checked below. No finiteness or single-input positivity follows. |
| Theorem 3 remarks | CORRECT | Affine substitution preserves nonsquareness; arbitrary composition need not. The corrected composition qualification is essential. R₈ needs both f and 2f nonsquare. No multivariate theorem is asserted. |
| §5.1 scaling and count | CORRECT | Only simultaneous scaling is classified. C≤(a+2)/4 excludes lifting from the smaller factor in the stated range. Full corrected primitive census replay agrees. Other transports are explicitly allowed. |
| §5.2 prime-d sieve | CORRECT | For admissible s and prime d≡3 (4), each distinct r∣(d+1)/4 gives two distinct m-classes iff (s/d)=−1. Relative prime density 1/2 is correct. The finiteness limitation is explicitly Assessment, not an impossibility theorem. |
| Proposition 4 | CORRECT | Every hit has Jacobi sign −1, including composite d; two hits multiply to sign +1. Opposite signs are necessary, not sufficient. The d=7, 29·17 counterexample to sufficiency checks. |
| §5.4 progression union | CORRECT | C≥1 gives exactly the stated progression and cutoff. No progression contains a square. The absence of a known descent is not a no-descent theorem. |
| §6 depth implication | CORRECT | A negative Jacobi symbol supplies a prime nonresidue divisor, so depth≤d_min. A uniform polylogarithmic witness bound would imply the stated depth strength; bare positivity need not give that bound. |
| §2 kernel census | CORRECT on audited engine/logs | Exact domain and coverage agree; independent slice and extremal-hit replays agree. See limits below. |
| §2.6 R₈ control | CORRECT | 321 cutoff misses split into 40 exact small zeros and 281 unresolved large inputs. Four late witnesses and all 12 F2 screen counts independently reproduce. |
| §0 F4 entry | GAP in screen reporting | Its “38 known zeros” are 14 primes + 24 composites, not the mandatory 38-prime 𝔊* screen. The entry does not explicitly report that separate screen. See required fix 1. |
| §8 runner-hardening claim | WRONG as a blanket claim | The committed runners do not uniformly enforce timeouts or propagate failures to their caller. This does not invalidate the independently reconciled completed logs. See required fix 2. |
| “narrowed; no HOT LEAD; B2 untouched” | SUPPORTED Assessment | Excludes positive-density nonsquare polynomial zero families, not thin families, sporadic zeros, or all possible composite constructions. No conjecture upgrade is justified. |

## Theorem 3: independent proof audit

1. In Q[u,t], f(t)+u has prime quotient Q[t]; Gauss yields irreducibility over Q(u). For a root α, K=Q(α), u=−f(α), and α is transcendental over Q. Thus i∉K. Also √(−u)∈K iff f is a square in Q(t), equivalently in Q[t]. This handles repeated factors and nonsquare constant multiples correctly.
2. Apply HIT to the entire Galois closure of K(i,√−u), after deleting the finite branch/bad-specialization locus. Full-fibre specialization preserves the subgroup action and both quadratic non-inclusions, not just an abstract group order. Cohen's O(√N log N) thin-set bound leaves primes q≡3 (4), since their count is asymptotic to N/(2 log N).
3. F=K_q∩Q(ζ₄q) is abelian. Its Galois group has elementary 2-primary part. Nontrivial conjugation would be detected by a quadratic character, producing an imaginary quadratic subfield in K_q. The only possibilities are Q(i), Q(√−q), both excluded. Thus F is real.
4. Restriction Gal(N/K_q) onto Gal(Q(ζ₄q)/F) is surjective. A lift of conjugation fixes a root; its conjugates still fix some root and still restrict to conjugation. Chebotarev therefore supplies a positive-density prime set with ℓ≡−1 (4q) and a root of f+q modulo ℓ, excluding finitely many bad primes.
5. For a root residue, u=q, C=(ℓ+1)/(4q), B=(f(t)+q)/ℓ give the exact positive witness once f(t)+q≥ℓ.
6. For fixed z, CRT gives the product of (1−1/ℓ) over these primes ≤z, with O_z(1) counting error and finitely many small t. Take T→∞ first, then z→∞; reciprocal-prime divergence makes the upper density zero.

**Source verification:** read Serre's actual [Harvard notes PDF](https://www.ms.uky.edu/~sohum/ma561/notes/workspace/books/serre_galois_theory.pdf), §3.3, Proposition 3.3.1 and polynomial form 3.3.5, and Theorem 3.4.4 (printed pp. 23–24, 27). Proposition 3.3.1 requires K-irreducibility, not geometric irreducibility: the constant field containing i is not a gap. For R₈ the same argument uses ζ₈q, whose four imaginary quadratic subfields are exactly the four listed in the memo; excluding f and 2f squares handles them.

## Census scope, exhaustiveness, and replay

**Exact searched domain:** squarefree s≡1 (4), gcd(s,105)=1, 13≤s≤100000; odd m coprime to 105 with 1≤m≤isqrt((2⁶⁴−1)//s). Thus n=s·m² is strictly below 2⁶⁴. There is no admissible nontrivial kernel below 13. This is complete input coverage, **not** an exhaustive enumeration of all witnesses at large n: each input stops at its first hit, or at d=10⁸.

The d-form itself is exhaustive: n≥3u−1 gives u≤(n+1)/3 and d=(n+u)/B≤(4n+1)/3; u<d identifies u with (−n mod d). Conversely every scanned hit reconstructs a positive triple. For R₈ exactly d≡7 (8), r∣(d+1)/8 is required. All actual production products, endpoints, increments, modular operations, and 128-bit checks fit their integer types. UNK alone is not a zero beyond the complete d-bound. The 16 R exceptions are all below 10⁶, so their 10⁸ scans are complete.

Independently regenerated every kernel, endpoint, and odd/coprime count; checked no duplicates/omissions and every logged maximum/late witness by Python integers. Window coverage and near-square counts were independently checked using interval arithmetic and residues modulo 210, with positivity/square corrections.

| Domain | Summary rows | Input occurrences | UNK occurrences / distinct n | Largest first d |
|---|---:|---:|---:|---:|
| kernels ≤1000 | 106 | 6,086,436,506 | 2 / 2 | 3,048,771 |
| 1000<kernel≤100000 | 10,955 | 61,785,619,898 | 14 / 14 | 6,637,967 |
| eight m-windows, k=10…17 | 848 | 3,876,571,898 | 0 / 0 | 2,512,619 |
| c∈±{8,16,…,200}, odd m≤10⁹ | 50 | 11,361,904,661 | 27 / 15 | 15,110,783 |
| R₈, kernels ≤1000 | 106 | 6,086,436,506 | 321 / 321 | 99,944,711 |

Kernel total **67,872,056,404**; first four rows total **83,110,532,963** occurrences, not necessarily distinct n. Every R UNK in these rows is in the 38-reference-zero list. Beyond 2⁶⁴ only the specified windows are covered, not all m up to 10¹⁷ or all n up to 10³⁷.

**Independent reruns:** `scripts/z60_xrev_ms105_audit.py` passes under `ulimit -v 4000000; timeout 1800 uv run python … /tmp/xrev_MS105`, after extracting the reviewed branch there. It runs sequentially, with subprocess timeouts ≤300 seconds and bounded segmented-factorization arrays (~53,000 entries for F2).
- Compared **97,942** individual R first-hit/UNK results against independent Python arithmetic: low m≤2001 and final 2001-wide m-intervals for all 106 small kernels, plus low slices at s=6217,92989. Also compared **1,371** high-window and **1,140** R₈ slice inputs.
- Replayed both kernel-census record first hits and the four s=29 R₈ late hits: d=128300223,145290191,102600159,100345783. Those four large UNK are therefore demonstrably not zeros.
- Independently solved individual n by segmented factorization of n+u for u≤B, enumerating divisors d=4uC−1 and restoring symmetry. This is algorithmically different from the production modulus scan. It reproduces all 38 reference zeros, all 40 small R₈ zeros, all 285 F3 zeros, and all F2/F4 counts discussed below.
- Replayed the existing N=6000 lemma check: **78,200 (solution,s) pairs, zero violations**. Full corrected primitive census at 2·10⁷ is byte-identical: prime/composite means 41.118/39.954, composite imprimitive mean 0.6679, exactly the six listed inheritance-only composites.
- Recompiled dec128 and replayed all **1,092 pseudosquare/control** and **1,000 locally-square/control** inputs; every first-hit/count record agrees. These are same-engine replays, not independent large-number oracle proofs.

## Mandatory falsifiers

| Screen | Independent finding |
|---|---|
| F1 odd squares | Lemma 1 with s=1 gives the contradiction directly. Excluding s=1 from the search is honest, not evidence for positivity on squares. Theorem 3 deliberately excludes square polynomials from (b). |
| F2 numerator 8 | All 12 screen primes have exactly the stored R counts and R₈=0 by the independent factorization solver. In the small-kernel control, bins ≤7.5·10⁷, (7.5·10⁷,10¹⁰], (10¹⁰,10¹⁴], (10¹⁴,10¹⁸], >10¹⁸ contain **40,0,1,73,207** misses. Largest n=18371040829044899437; 110 large misses are 1 mod 8. Only the first 40 are certified zeros. The lemmas and density theorem do not separate R from R₈; the memo acknowledges this. |
| F3 composites | All **285** supplied composites independently have R=0; **20** are coprime to 105, the other 265 are outside this conjecture's domain. The census does not erase these finite exceptions. Density zero and same-modulus anti-multiplicativity make no contrary prediction. |
| F4 prime screens | All **14 (★)-zero primes** independently have R=0. Of the **38 𝔊*-zero primes**, exactly those same 14 have R=0; the other **24 have R>0**. These 38 primes are not the memo's 38-entry MS105 reference list. The proposed theorem makes no individual-prime positivity prediction. |

## Required fixes, in priority order

1. **Complete F4 explicitly.** State the preceding 14/38-prime comparison, and distinguish it from the separate 38 MS105 zeros (14 primes, 24 composites). The present table's replacement of the mandatory 𝔊* screen by a same-sized but different list is insufficient screen reporting, although the actual checks reveal no counterexample.
2. **Correct §8 / runner claims.** `z60_ms105_r8ctl_run.sh` has no per-engine timeout; its loop can mask an earlier failure, and bare `wait` does not propagate child failure. `sm2_run.sh` likewise ends with bare `wait`; `sm2_big.sh` records `EXIT $e` but then returns the successful `mv` status; the window runner also does not propagate aggregate failure. Either actually harden these or explicitly withdraw the blanket “failure propagation/per-job timeout” claim. Do not use shell exit status alone as a certificate. Also supply §2.1's missing OUTDIR argument to `sm2_big.sh` (the §8 command already has it).

**Final assessment:** accept the proved univariate density theorem, kernel bookkeeping, and same-modulus obstruction after these reporting fixes. The complete small-kernel census is supported by engine audit, exact log reconciliation, and independent bounded slices—not by a full independent census. “Narrowed; no HOT LEAD” is proportionate. Thin infinite zero families and counterexamples above 29,210,401 remain possible; **(MS⁺₁₀₅) stays CONJECTURE**.
