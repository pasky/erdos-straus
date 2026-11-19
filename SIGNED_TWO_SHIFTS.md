# Can either of two denominators use the same signed shift?

**Answer.** For primes `p≡1 (24)`, not always: at 193 no prime shift of the required sign works in either denominator, in any slot. No composite shift works there either **if a root is required**; several work if only a Jacobi sign is required. **193 is not one of Mordell's six residues** `{1,121,169,289,361,529} mod 840`. Within `1 mod 840` we give an exact factorization obstruction at the least eligible shift 11, a density-one positive result for the least eligible prime, and a conditional obstruction to trying any fixed number of successive eligible shifts. None settles the individual-prime, unrestricted-shift problem on that class.

## The test and its finite boundaries (PROVED)

Throughout `d>0`, `d≡3 (4)`, `gcd(p,d)=1`. Prime eligibility means `(p/d)=-1`, equivalently `−p` is a square mod `d`. For composite `d` distinguish **J** (Jacobi `(p/d)=-1`) from **R** (unit square root of `−p mod d`). R implies J, not conversely. R requires a square mod *each* prime factor, sufficient also for all prime powers by unit-root lifting. Quadratic reciprocity gives `(p/d)=(d/p)` here.

Put `K=(p+d)/4`, `N=(pd+1)/4`. Fixing `s=K` leaves `d/(pK)`; requiring both remaining denominators to be `p`-multiples instead tests `d/K` before multiplying them by `p`. Fixing `s=pN` leaves `d/N` (Type I); this is **not** the literal `4s/p−1=d`, which fixes `s=p(d+1)/4` and leaves `d/s`. For a reduced residual `d/H`,

```
(dy−H)(dz−H)=H²,        y=(H+t)/d,        z=(H+H²/t)/d.
```

It suffices that `t|H²` and `t≡−H mod d`; the complementary congruence is automatic. Equivalently `−1∈B_d(H)`, where `B_d(H)={∏q^i mod d : |i|≤v_q(H)}` (one coordinate per prime). This is a **signed** exponent test, not just subgroup membership.

There is no finite bound on eligible *inputs* `d`; here are finite, lossless bounds on all possible successes. Sort a triple `x≤y≤z`. Then `p/4<x≤3p/4`. For each integer `x` there, put `h=px, c=4x−p`. Independently of the factorization,

```
max(x, ⌊h/c⌋+1) ≤ y ≤ ⌊2h/c⌋,    z=hy/(cy−h).
```

Alternatively use exactly `max(1,cx−h)≤t≤h`, `t|h²`, `c|(t+h)`. These bounds follow respectively from `y≥x`, positivity and `y≤z`; `x<p` and `c` is prime to `h`. Conversely every such `t` gives one sorted solution. For fixed `x` the **sharp** `z` upper endpoint is `(h+h²/t_min)/c` for the least retained `t`, or the row is empty. Without any factorization a safe advance bound is `z≤⌊h L/(cL−h)⌋`, `L=max(x,⌊h/c⌋+1)`, since `hy/(cy−h)` decreases. Take the maximum over nonempty rows; all denominators are bounded, not just the smallest. To get exact shift bounds, from **each** slot `s` retain `4s−p` if `p∤s`, and `(4s/p−1)/p` if `p|s` and this is integral (then remove nonunits). The maxima of these finite lists are the attained bounds whenever nonempty. Do not apply the smallest-denominator bound `c≤2p` to other slots.

## 193 (CERTIFIED, two independent enumerations)

`11` is the least eligible prime (`−193 mod 3,7,11` is `2,3,5`); `19` is the next. At 11 the complete divisor lists project as follows. The literal test is included only to expose a normalization pitfall.

|slot and residual test|H|# positive divisors of H²|residues of the divisors mod 11|target|
|---|---:|---:|---|---:|
|51, unrestricted|3·17·193|27|1,3,4,5,6,7,8,9,10|2|
|51, Type II only|3·17|9|1,3,5,6,7,9,10|4|
|102483, Type I|3²·59|15|1,3,4,5,9|8|
|579, literal|3·193|9|1,3,5,6,7,9,10|4|

The two smaller primes `1 mod 24` are 73 and 97: their least eligible prime is 7 and the direct slot occurs in `(20,219,4380)` and `(26,388,5044)`. At 193 both the integer `y` loop and the complementary-factor loop give exactly these six triples (`49≤x≤144`):

```
50  1380  1331700       52  676  65234
50  1450    27985       52  772   5018
50  1930     4825       58  290  27985
```

**All successful shifts, no cutoff:** direct `7,15,39,967,2511,5327,5607`; Type I `3,7,143`. Thus the exact unrestricted slot maximum is `1331700`, the exact coprime direct shift maximum `5607`, the Type I shift maximum `143`. The exact prime lists are `{7,967}` and `{3,7}`; none is eligible. Among composites, J selects **15,39,5327,5607**, all direct; R selects **none**. For instance `d=15` gives `s=52` but `−193` is nonsquare modulo 3. The other composite factorizations are `39=3·13, 2511=3⁴·31, 5327=7·761, 5607=3²·7·89, 143=11·13`. Dropping the sign allows 7 in both families. The *literal* family actually has a root-eligible prime hit `d=103, s=5018`; folding that into Type I would change the answer.

**Why J is an easier repair (PROVED corollary of the known character identity).** In *every Type I triple* the two `p`-free denominators `s,s′` satisfy `(ss′/p)=−1` (`HARDNESS_MAP.md`, A2: they are `ack,bck`, with `(ab/p)=−1`). Exactly one of them already yields a J-eligible direct shift: `(p/(4s−p))=((4s−p)/p)=(s/p)` by reciprocity. This converts a Type I solution into a signed direct success without choosing a prime factor. It does not produce a Type I solution, a prime shift, or a root mod the composite shift; 193 shows the last two distinctions are necessary.

## Exact signed two-family theorem at 11 (PROVED)

For `p≡1 (840)` with 11 eligible, it is the least eligible prime. Define

```
Q=(p+11)/12,   R=(11p+1)/12=11Q−10;   K=3Q,   N=3R.
```

`Q≡p, R≡1 mod 11`. In the statements below, count prime factors with multiplicity and use residues mod 11.

* **Direct fails iff** `p≡2 or 6`, and after removing all `1`-class factors of `Q` exactly **one occurrence** remains, of class `p`.
* **Type I fails iff** either all factors of `R` are quadratic residues, or, after removing all `1`-class factors of `R`, **exactly one 2 and one 6** remain.

The conjunction, not an independence heuristic, is the exact obstruction. In particular every such prime `p≡7,8,10 mod 11` has a direct solution at its least eligible shift **without factoring** `K` or `N`.

*Direct proof.* Eligible residues are `2,6,7,8,10`. The signed factors `3,p` already supply `−1` in the last three cases (`3·7≡−1`, `8/3≡−1`, `10≡−1`). In the first two cases (2 and 6 are inverses), the complement of `{−3^i p^j: i,j=−1,0,1}` is exactly `{1,2,6}`. Failure means the *entire* signed set of `Q` fits in those three classes. Each non-1 prime occurrence must then have residue 2 or 6; two such occurrences can both be oriented to 2, producing forbidden 4. At least one is required since `Q≡p`. Conversely the specified shape has just the three allowed ratios.

*Dual proof.* Use base-2 logs mod 10, with target 5; `3` has log `−2`. If all prime logs in `R` are even we miss. With an odd log, `5` or `±3` fires immediately using at most the one reserved factor 3. Otherwise all odd logs are `±1`. If a nonzero even log occurs too, its signed choices together with those of the reserved `−2` attain **every even log** (the new log is `±2` or `±4`); hence we hit. With only `±1` and zero logs in `R`, three odd occurrences suffice: orient three to `+1` and the reserved factor to `+2`. If fewer are present, `R≡1` implies exactly a cancelling pair or none. A pair and the reserved factor can have total absolute log at most four, so indeed miss. This exhausts cases even for repeated prime powers. ∎

**CERTIFIED examples.** At the *first* hard-class prime 2521, `Q=211≡2`, `R=2311≡1` are prime: both tests fail, as at 19. At 23 direct succeeds with `(636,69748,131876031)`; even the genuinely root-eligible composite `55` succeeds with `(644,30252,1217643)`. At 12601, both 11 and 55 fail in both families, though 23 works. At 3361 only the dual rescues 11, e.g. `(936,8216,31065723)`. These are actual denominator checks, not negative phase certificates.

## How far can one push successive eligible shifts?

**PROVED (positive, density not pointwise).** For a set of relative natural density one among the primes `p≡1 (840)`, **both** denominators at the *least* eligible prime shift complete. Here one need not compare divisor counts. Fix a candidate prime `d>7`, `d≡3 mod 4`. For direct success it suffices to have a prime `q≡−1 mod d`, `q∤840d`, dividing `K`; this forces `−1` in its signed set. For dual use such a `q|N`. For each `q`, the required residue of `p mod q` is respectively `−d` or `−1/d`, a unit. For each family separately, CRT and PNT in fixed progressions give an upper relative density of misses bounded by `∏(1−1/(q−1))` over any finite list of these `q`. This tends to zero by divergence of prime reciprocals in the progression. Both miss sets thus have density zero, without needing independence between families. For any fixed finite initial list of `m` candidate primes `d>7`, the hard-class primes with none eligible have relative density `2^(−m)` by CRT. The others are good at their least eligible `d`, off a finite union of density-zero sets. Send `m→∞`. This is an elementary almost-all consequence, not a new exceptional-set bound.

**CERTIFIED survey.** All 3426 primes `p≡1 (840)` through ten million have a hit in at least one family at some eligible prime `d≤199`. The unique one needing 199 is `6348721`: both fail at `43,67,127,131,151,179`, direct works at `199`, with `(1587230,50637599020,287937832988251324)`. These are also the only R-eligible shifts up to 199 for this `p` (smallest R-eligible prime `3 mod 4` is 43 and `5·43>199`; its square is too large). At 11 among 1711 eligible primes in the survey, `(neither, dual only, direct only, both)=(158,86,983,484)`.

**CONDITIONAL on Dickson for linear forms.** For each `k≥1` there are infinitely many primes `p≡1 (840)` whose **first k eligible shifts**, even allowing J-composites, are distinct primes and all fail in both families. Thus no fixed number of retries would prove a pointwise theorem on this class under Dickson. This does **not** assert failure at all shifts, or up to `(log p)^A`.

*Construction/admissibility.* Put `B=4k+41`. Take `X` sufficiently large, and `k` primes `d_i∈(X,2X)` that are `3 mod 8` and `1` at every odd prime `≤B` (CRT and PNT in this fixed progression). Prescribe `p` modulo 8 and all odd primes `ℓ≤2X` as follows:

1. At 8 and the odd `ℓ≤B`, set `p≡1`. All `K_i,N_i` are odd; modulo small odd primes both numerators are 2.
2. At larger unselected `ℓ`, choose a nonzero **square** avoiding `−d_j,−1/d_j` for all `j`. There are more than `2k` choices before exclusions.
3. At `ℓ=d_i`, choose a **nonsquare** `u`, avoiding the same bad classes for `j≠i` and all equations `u^(a+b)=−4^b` with `a,b∈{−1,0,1}`. For `a+b=0` the equation is impossible at these large primes; the nonconstant equations exclude at most eight roots in total (sum the absolute exponents). There are enough nonsquares. The matching forms `K_i,N_i` are automatically units there.

The resulting progression `p=p_0+Mt` has `p≡1 mod 840`. The `2k+1` forms `p,K_i=(p+d_i)/4,N_i=(d_i p+1)/4` are positive-leading integral linear polynomials in `t`, pairwise nonproportional (their roots in the `p` coordinate are `0,−d_i,−1/d_i`). At primes dividing `M` they are all units; at primes outside `M` their product excludes at most `2k+1` roots, fewer than the prime. Dickson now supplies arbitrarily large primes for all forms at once. For each `i`, the unrestricted direct ratios reduce to `p^a K_i^b ≡ u^(a+b)/4^b`, all missing `−1` by construction; the dual `N_i≡1/4` alone generates only squares and `−1` is nonsquare. Up to `2X` any Jacobi-negative integer must contain a `d_i`, and no odd composite multiple of one lies in this interval. Each selected prime actually satisfies R, so this proves both versions. Without Dickson the CRT prescription is unconditional, the simultaneous primality is not. ∎

## Cross-checks and scope

* `Z73_PROBE_FORCING.md` proves no `A=1` Type II certificate at 193, and gives a two-factor certificate at 15. Our unrestricted 193 list tests both denominator families; the success at 15 is J only. The signed-11 classification uses the extra `p` factor for the unrestricted direct test and a different linked factorization for the dual.
* `PHASE43_DENOMINATORS.md` tests unrestricted **direct** completion, not this Type I slot. On its negative row `p=12395549472601`, `N=23·41·152203·928409`. Remarkably **both** normalized boxes are the same punctured group: `B_43(pK)=B_43(N)={1,…,41}`. Even unioning the two boxes of size 41 misses only the target 42. The first R-eligible success in either family is 59 (the known direct hit at 47 is ineligible). On its positive row `349219296721`, the direct box is full but `N=3754107439751` is prime and its three ratios miss. No phase bound is used.
* At `Z73_COMPOSITE_PHASE.md`'s `p=3117161329,d=715` (in the six classes, **not** `1 mod 840`), R actually holds. The direct and Type I boxes have sizes 12 and 27, neither contains `−1`; `N=19·67·437700383`. At its `1201,d=39` the boxes have sizes 24 and 9, first succeeds only; this shift satisfies J, not R. The Dickson construction above obstructs a *list of different eligible primes*, not componentwise CRT assembly inside one composite shift.
* **Falsifiers.** Odd squares have no J-eligible coprime shift. Numerator 8 changes the link and is not asserted here. For composite inputs the sorted bounds still apply with the two complementary congruences both checked; no prime-case character conclusion is used there. Restricted (★) and gstar zeros do not imply either fixed denominator fails and no theorem here concerns those counts.

Replay (independent trial factorization, no dependency or campaign solver):

```
(ulimit -v 800000; timeout 60 uv run --no-project python scripts/signed_two_shifts.py)
```
