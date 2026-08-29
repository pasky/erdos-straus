# Hostile review of §54 (wave 20)

**Overall verdict: CONFIRMED-AFTER-REPAIR (applied).** I found no mathematical defect in Theorems 54.1/54.3 or in the two frontier refutations. One low-severity verification-coverage gap was repaired in `verify.py (ba)`: the block now constructs `M(T)` literally, checks small Type-II least primes, and pins an exotic composite-`ell`, `w>1`, `u=v` datum. No repair to §54 itself was needed.

## Per-claim verdicts

### 1. Theorem 54.1 — CONFIRMED

- **All data in `W` are covered.** Definition (51.1)–(51.2) quantifies over all positive `k,ell,u,v,w`, permits composite `ell`, and imposes no ordering (`notes.md:18422-18439`). Put `m=k ell`. Every datum then has `m=3 mod 4`, `uvw=(m+1)/4`, and invertible `v`; nothing in the proof depends separately on `k`, `ell`, or on `w=1`.
- **Size contradiction is complete.** If `p=1 mod m`, a witness gives `m | u+v`. Positivity gives `2 <= u+v`; `(u-1)(v-1)>=0` gives `u+v<=uv+1`; and `uv<=uvw=(m+1)/4` gives `u+v< m` for every `m>=3` (`notes.md:20182-20193`). At `m=3`, necessarily `u=v=w=1`, so `u+v=2<3`. The equality boundaries `u=1` or `v=1`, and `u=v`, do not open a hole.
- **The lcm has the right quantifier.** If integer `m<=T`, then `m<=floor(T)` and `m | M(T)`. Thus `p=1 mod M(T)` implies `p=1 mod m` for every eligible product, including products with composite `ell` (`notes.md:20147-20156`).
- **Linnik arithmetic is correct.** The cited theorem gives the least prime in every reduced class modulo `q` as `p <= C q^5.2`, with an effectively computable implied constant. Direct inspection of Xylouris's theorem statement confirms both exponent `5.2` and effectivity. Since `log M(T)=psi(floor T)=T+o(T)`, `log p <= (5.2+o(1))T`, hence `W(p)/log p >= 1/(5.2+o(1))` (`notes.md:20165-20201`). The decimal `1/5.2=0.192307...>0.19` is correct.
- **Effectivity is not overstated.** Section 54 says `C_0` is effectively computable but does not claim a published numerical value or a fully explicit threshold (`notes.md:20325-20336`). This matches Xylouris. The Rosser–Schoenfeld bounds provide optional numerical linear envelopes; the effective prime number theorem supplies the asymptotic constant.
- **The sequence is genuinely infinite.** Every selected prime is at least `M(T)+1`, and `M(T)` tends to infinity. Therefore selected primes along unbounded `T` cannot remain in a finite set (`notes.md:20198-20201`).

### 2. Theorem 54.3 — CONFIRMED

- `R(T)=4 prod_{ell<=T} ell`, for `T>=3`, so `log R(T)=theta(T)+log 4` exactly (`notes.md:20241-20251`).
- For every odd prime `ell<=T`, `p=1 mod ell` and `p=1 mod 4` give `(ell/p)=(p/ell)=1`. Modulo 24 also gives `(-1/p)=(2/p)=(3/p)=1`. Therefore every negative fundamental discriminant `Delta_s` for squarefree `s<=T`, including even `s`, has `(Delta_s/p)=1` (`notes.md:20275-20288`). The factor 4 contributes symbol one; no 2-adic case is omitted.
- If `ck<=T`, then `sf(c)<=c<=T`, so (50.3) has an empty good-prime class and Theorem 48.1 forces the complete slice mass to zero (`notes.md:20290-20293`; genus implication at `notes.md:17104-17110`).
- Admissibility is valid for **every** positive pair `ck<=T`. Since `R(T)>4T`, one has `p>4T`; then `p` cannot divide `ck`, `3k<=3T<2p`, and `4ck<=4T<2p+k`, exactly the conditions of `B_p` (`notes.md:11669-11671`, `notes.md:20294-20297`). Bertrand suffices: if `q` is the largest prime at most `T`, its successor is below `2q`, so `q>T/2`; hence the primorial exceeds `T` (with the stated small range checked directly).
- The same Linnik/PNT calculation gives the limsup constant. The `+infinity` convention for `ck_min` causes no problem.
- **Prior-result comparison is honest.** Theorem 48.5 excludes bounded fixed-divisor guarantees but expressly does not imply vanishing or an infinite conspiracy sequence (`notes.md:17438-17474`). Theorem 50.5 already gives fixed-`B` genus-forced progressions (`notes.md:18133-18152`). Section 54's new content is the quantitative coupling `B=T` with Linnik, not a claim that the genus geometry itself is new (`notes.md:20318-20323`).

### 3. Frontier corollaries — CONFIRMED (maximum-severity check)

- `H_MOD(A)` requires `W(p)<=(log p)^A` for **every sufficiently large prime** (`notes.md:18632-18640`). Theorem 54.1 supplies unbounded, hence infinitely many, primes with `W(p)>c log p`. For every fixed `0<A<1`, `c log p>(log p)^A` eventually. This is the required infinite sequence of violators, not merely one finite exception (`notes.md:20203-20222`).
- `H_SPF(A)` requires a good prime-factor slice with `ck<=(log p)^A` for every sufficiently large hard prime (`notes.md:18051-18060`). Theorem 54.3 gives infinitely many hard primes with **no positive slice at all** through `T>=c log p`; therefore there is certainly no good prime factor through `(log p)^A` for `0<A<1` (`notes.md:20304-20316`). The normalization is exactly the box in (50.7), not `c`, `k`, or `q` separately.
- **Endpoint `A=1` was attacked and survives.** The lower constant is `1/5.2<1`; `W(p)>c log p` and `ck_min(p)>c log p` do not contradict bounds by `log p`. Section 54 correctly leaves every `A>=1` open and claims no endpoint refutation (`notes.md:20203-20208`, `notes.md:20304-20310`).
- **No conflict with almost-all bounds.** Taking `N` equal to a selected prime makes the exceptional set nonempty at infinitely many heights, while a one-point lower bound is compatible with `o(pi(N))` and with the effective upper envelope (53.37). The provisional label on (51.18) is retained (`notes.md:20211-20237`, `notes.md:20313-20316`).

### 4. Wave-20 pointers — CONFIRMED

- The §48 pointer distinguishes fixed-divisor non-guarantee from genus-forced vanishing (`notes.md:17465-17474`).
- The §50 pointer states exactly the `0<A<1` refutation for `H_SPF` (`notes.md:18062-18073`).
- The §51 pointer states exactly the `0<A<1` refutation for `H_MOD` (`notes.md:18632-18640`).
- All three preserve the result/status register and make no unsupported upgrade from provisional upper tails to proved ones.

### 5. `verify.py (ba)` — CONFIRMED-AFTER-REPAIR (applied)

- The direct harvest enumerates every ordered factorization `uvw=(m+1)/4` for every `m=3 mod 4` through 300, checks invertibility and the complete size chain, and finds residue one absent in all 75 moduli / 982 data (`verify.py:9639-9664`). This is a direct class harvest, not reliance on a sampled factorization.
- Added the explicit hostile datum `(k,ell,u,v,w)=(1,95,2,2,6)`, which simultaneously has composite `ell`, `w>1`, and `u=v` (`verify.py:9666-9674`).
- Added literal `M(T)` constructions and least-prime regressions `(T,M,p)=(3,6,7),(5,60,61),(7,420,421),(11,27720,55441)`, including every eligible modulus at each cutoff (`verify.py:9676-9694`).
- Existing `R(T)` regressions remain `(5,120,241),(7,840,2521),(11,9240,9241)`. They check actual Jacobi/Kronecker symbols and stream every divisor grade for every `ck<=T`, not just the genus prediction (`verify.py:9727-9759`).
- Isolated `(ba)` runtime was 0.0033 s for the function (0.33 s including a fresh `uv`/Python harness), well below 10 s. The full required command passed all blocks `(a)`–`(bb)` in 104.95 s with maximum RSS 333,444 KB:
  `uv run --with sympy,numpy,scipy python verify.py`.

### 6. Hygiene — CONFIRMED

- Section order and numbering are consecutive: (54.1)–(54.10), with no duplicate.
- Cross-references to Theorems 17.3(c), 48.1, 48.5, 50.5, definitions (50.3), (50.7), (50.18), (51.1)–(51.2), and bounds (51.18), (53.37) are accurate.
- `notes.md` and `verify.py` contain zero forbidden control bytes and zero backspace/eaten-backslash bytes.
- `git diff --check` passes.

## Attempted-break log

1. **Exotic Lemma-16.1 datum:** tested `m=95`, `k=1`, composite `ell=95`, `u=v=2`, `w=6`. It yields class `-u/v=-1=94 mod 95`, not residue one. This attacks composite `ell`, a nontrivial unused `w`, and the `u=v` boundary at once.
2. **Equality boundary:** at `m=15`, `(u,v,w)=(1,2,2)` has `u+v=uv+1=3`; it still lies strictly below 15. Thus equality in the middle inequality is harmless.
3. **Small modulus:** at `m=3`, only `(1,1,1)` occurs and gives `u+v=2<3`.
4. **All `k,ell` orderings:** after fixing `m=k ell`, both the factorization condition and witness residue depend only on `m`; splitting 95 as `1*95`, `5*19`, or in reverse cannot introduce omitted data. The full product-modulus harvest is therefore structurally exhaustive.
5. **Even/2-adic genus cases:** replayed `s=2` (`Delta=-8`), `s=6` (`Delta=-24`), and `s=10` (`Delta=-40`). Modulo 24 pins the `-1`, 2, and 3 symbols, while residue one modulo 5 pins the remaining factor; all symbols are +1.
6. **Linnik-constant misuse:** checked the primary theorem statement rather than a secondary citation. It says `P(q) << q^5.2` with an effectively computable implied constant. Section 54 does **not** turn that into a numerical `C_0`, does not drop the constant in finite inequalities, and uses `o(1)` only after effective PNT.
7. **Endpoint `A=1`:** tried both corollaries with the strongest proved constant. Since `1/5.2<1`, neither violates a cutoff `log p`; the endpoint remains open as stated.
8. **Infinitude loophole:** a least prime could repeat for nearby `T`, but not along unbounded `T`, because it is at least the growing progression modulus plus one.
9. **Composite fixed divisor confusion:** compared Theorem 48.5's composite-`d` scope with §54. The former says only “not guaranteed”; §54 correctly obtains actual zeros from Theorem 48.1/50.5 instead.

## Severity-ranked defects

- **Critical / high / medium:** none.
- **Low — repaired:** pre-review `(ba)` harvested all Type-II product classes but did not literally construct `M(T)` or retain a Type-II least-prime regression; it also left composite-`ell` coverage implicit in the product reduction. The added checks at `verify.py:9666-9694` close this test-coverage gap. This was not a gap in the proof at `notes.md:20182-20193`.

## Overclaim scan

No forbidden overclaim remains. In particular, §54 does not claim an Erdős–Straus counterexample, nonsolvability, a bound at `A=1`, a numerical Linnik constant, validation of the provisional cubic upper tail, or novelty for Theorem 50.5's underlying genus progression. “Effective” is used in the computability sense and is explicitly distinguished from extracting numerical `C_0`.

## Scope signature

**Replayed directly:** all elementary congruence/size steps, `M(T)`/`R(T)` identities, admissibility, squarefree and even discriminant cases, frontier quantifiers and inequalities, finite class/slice computations, small least primes, source statement of Xylouris's theorem, and the full verification run.

**Structural inputs accepted rather than reproved:** effective Linnik itself, effective PNT/Chebyshev asymptotics, Bertrand, quadratic reciprocity, and previously proved Theorem 48.1. The internal proofs of the almost-all upper bounds in §§51 and 53 were not re-reviewed here; only their definitions, labels, and logical compatibility with §54 were checked.
