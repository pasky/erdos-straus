## §0
Result: ES holds on the three previously unclosed Proth families `(4^m−1)2^s+1`, m=4,5,6, and on infinitely many pairs `c·2^s+d` with distinct odd coefficients c and no finite ET/divisor covering. Label: PROVED (computer-assisted, rel. Mordell reduction, the word criterion, and the classical square-unit obstruction)
Scope: Every s≥0; n may be prime or composite. Good (S) words on the moving-core rows, not on all exponents. The infinite-pair result varies d; it does not prove infinitely many multipliers with d=1, or ES in general. Secondary §4 lower-tail corollary: PROVED rel. z75 (BV, BT, Mertens), reviewed at sketch level, not proposed for STATUS.
Review: cross-model (Claude Opus, `notes/z77/REVIEW_PROOF_S_WILD_OPUS.md`; A and B accepted, form fixes and independent finite checks incorporated)
Triage: HEADLINE
STATUS delta: extend §1C Proth list to all `(4^m−1)2^s+1` for `1≤m≤6`; infinitely many distinct pairs `(c,d)` at fixed base 2 with no finite ET/divisor cover (§3). New cases computer-assisted, not Lean.

# Moving products, not just moving primes

## 1. Three more Mersenne multipliers

**Theorem A.** For `k=255,1023,4095` and every integer `s≥0`, ES holds at `n=k·2^s+1`. None of these three sequences admits a finite covering by ET Prop. 1.9 classes and fixed prime-divisor classes, even allowing finitely many initial exceptions. On the X rows below the result is stronger: n has an interior length-three word with negative Jacobi symbol. In particular these give (S) even on progressions whose closure contains a square unit.

Here and below a good word is `n=tuv−u−v` with `t,u,v≥2`, `(tu−1/n)=−1` (Jacobi). It gives ES for n≡1 mod 4 by `DEDEKIND_ES.md` Thm 4.5, and its sign is negative iff `8|(n+t)tuv` (`Z64_SDEEPF.md` Thm 2.1).

**Core lemma.** Put `u=k−1=2(2^h−1)`, with h respectively 7,9,11, and let p be the unique prime dividing h. Fix an odd degree m and suppose `4m|s`, s>0. Set

    r = (s/m) / p^{v_p(s/m)},     x=2^r,     j=r mod h.

Thus `16|x` and `s/(mr)` is odd. For each d|m let `F_d(X)=Φ_{2d}(X)`, so the positive integers `F_d(x)` multiply to `x^m+1 | 2^s+1`. Suppose, at this j, that some c|k and subset T of divisors of m satisfy

    c ∏_{d∈T} F_d(x) ≡ 7u−1 (mod 8u).                         (1)

Then this product A divides `n+u=k(2^s+1)`, and `t=(A+1)/u≡7 (8)`, `v=(n+u)/A` produce a good word. Indeed each `F_d(x)≡1 mod 16`, because its constant term is 1. For the listed k, `7u−1≡1 mod 16`; more importantly `7u−1>k` and `0<7u−1<8u`, so (1) selects a nonempty product and t≥7. Indeed `u≡6`, `A≡1` and `n≡1` mod 8 force `v≡7 mod 8`. Thus v≥2, the sign criterion holds and `n=vA−u=tuv−u−v`. For a direct ES identity put `D=(tv−1)/4`: the denominators are `ADn, uD, AuD`, since `4ADu=u+n(A+1)`. No information about prime factors of the cyclotomic values is used. Unlike a single `Φ₆`, their subproducts give many more attainable residues. Dividing out an *unbounded* p-part preserves divisibility but removes the unusable residue 0 at the square limit.

| k | m on X rows | s classes (residue mod period) | h |
|---:|---:|---|---:|
|255|315|0 mod 5040|7|
|1023|1155|0,13860,41580 mod 55440|9|
|4095|315|0,25200,30240 mod 55440|11|

For example k=255, j=3: one can take `c=1, T={1,3,7,21,35,45,63,105,315}`. The checker does not assume the discovery implementation of `Φ`. For each possible unit j mod h it picks `x₀≡0 (16), x₀≡2^j (2^h−1)` (CRT, hence `x₀≡x (8u)`). In increasing d|m it divides `x₀^d+1` by all earlier `F_e(x₀)` with e|d, updating the attainable residues `B ← B ∪ F_d(x₀)·B` starting with `B={c mod 8u:c|k}`. It checks (1) in all 6,6,10 unit residues respectively. This is a finite check on h, **not** a periodicity assertion about `v_p(s)`.

## 2. Proof off the core

The proof objects are `data/z77/proth/{255-5040,1023-55440,4095-55440}-0.json` and `{1023-55440,4095-720720}-extra.json` in the same directory. Each row is a rule for one `s≡j mod P`. For s<32 the checker verifies all 96 explicit integer triples by cross-multiplication, using the reviewer's small-input divisor search (`z77_review_small_s.py`). It also verifies a triple for every D-row divisor. For s≥32, `scripts/z77_proth_verify.py` (standard library only, independent of discovery routines) checks the following:

* M: n mod 840 is outside the subgroup of unit squares. Mordell reduction and scaling apply to composites: otherwise every prime divisor would be a unit square mod 840; if 2,3,5 or 7 divides n, scale directly.
* D: a fixed integer `2≤q<20000` divides n. Scale the verified triple for q.
* W: `A|n+u`, `u|A+1`, giving the integral word above; test the sign using n mod 8A, t,u≥2 and n+u≥2A. The verifier also checks explicitly that at least one of `t,u,v,A,tv−1` is 0 mod 4, giving a five-slice identity.
* II: `4ab|f+1`, `bn≡−a mod f`. This is the fixed Type II rule of `notes/z75/THIN_CYCLO.md` §1 (the row's b is the c-parameter there). With `d=(f+1)/(4ab)`, `e=(n+4a²d)/f` is integral since `gcd(b,f)=1`. Moreover `b'=(n+e)/(4ad)` is integral because `f≡−1 mod 4ad`; `be=a+b'`, `4ab'd=n+e`. Denominators `ab'd, abdn, b'bdn` work by multiplication.
* K: `f≡3 mod 4`, `K=(n+f)/4`, `K₀|K`; two positive divisors D,E of nK are specified as `d n^i(K/K₀)^j`, `d|K₀`, `i,j=0 or 1`. If `f|D+E`, take denominators `K,(nK/D)(D+E)/f,(nK/E)(D+E)/f`. No coprimality of D and E is needed.

The checker freezes the *actual* modulus M required for each rule (including division by K₀ when used) by testing `k 2^{s₀}(2^P−1)≡0 mod M` at the first `s₀≥32` in that class. For W the checked representative of `(n+u)/A` is sufficient mod 8. For each (possibly refined) period the union is checked on **every** residue, not on a random sample:

|k| final period| M | D | W | II | K | X | uncovered |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|255|5040|8|5|24|6|0|1|0|
|1023|55440|11|2|16|9|12|3|0|
|4095|720720|0|34|69|46|112|3|0|

For no finite ET/divisor covering invoke `EXPONENT_COVERING.md` Cor. 1.5: at large s divisible by all odd unit orders in a proposed menu modulus, n≡k+1 is a power-of-four square unit at the odd part, and n≡1 at the 2-part. This is why mere extension of a finite ET search could not have proved A.

## 3. Varying the coefficients without losing the unit-square obstruction

**Theorem B (fixed base, infinitely many pairs).** Let Q be the lcm of 255, 127, the odd parts of all fixed moduli in the 255 certificate (their lcm is `61500575996988381601913565`), and `255·2^s+1` for `1≤s<32`. Put `J=4+i·ord_Q(2)`, `i≥0`, and

    c_J=2^{2J−1}+127,    d_J=2^{2J−1}−127.

Then every `N=c_J·2^s+d_J`, s≥0, has ES. For each J the family admits no finite ET/divisor covering. For s>0 divisible by 5040 it has a good word. For i>0 these are not the Proth families of A or base replacements in z75: the positive odd offsets vary, `c_J−d_J=254`, and the coefficients are coprime (`d_J≡1 mod 127`).

*Proof.* `c_J≡255, d_J≡1 mod Q`, and also mod 128, since `2J−1≥7`. Every fixed modulus of the 255 certificate has 2-part ≤128 (verified); hence N inherits the fixed positive rule at every s≥32 off core. In W, size is monotone since `N≥255·2^s+1`. For 1≤s<32 it is a multiple of the old n by the definition of Q. At s=0 use `N=4^J`. On core `N+254=c_J(2^s+1)` with `255|c_J`, so *the very same divisor A* works. The proof of v≥2 and the sign use only N≡1 mod 8. Finally, for any proposed finite menu take s large and divisible by all unit orders of 2 at its odd part: `N≡c_J+d_J=4^J` there, a unit square, and at the 2-part `N≡d_J≡1 mod 8`, again a unit square. Such an N is outside every member (`EXPONENT_COVERING.md` Thm 1.4, square-unit part). This transfer keeps an actual unbounded divisor, not just its output residue. ∎

The restriction to d varying is essential to *this transfer*. At fixed u and the identity `N+u=c(2^s+1)`, imposing d=1 forces c=u+1. No result here for all Mersenne multipliers. Repo priority check: `MENU_STERILITY.md` Prop 4.3 had a scoped negative test at 255, not an ES theorem there. `EXP_OPEN.md` and `paper/es-exponential-families.tex` give the earlier 3 and 63 proofs. No external novelty claim.

## 4. Restricted U₇ witnesses; screens

`Z68_U7O.md` Theorem A **already** implies Conjectures B and C in relative density one: the constructed f is prime, not just ω(f)≤2. For a quantitative interpolation there is another corollary of the z75 proof:

**Corollary (relative to `notes/z75/ANALYTIC_PUSH2.md` §§1–3).** In every positive-integer interval of length H, all but `O(H exp(−c√(log H log log H)))` primes have `≫√(log H log log H)` distinct U₇ witnesses f with ω(f)≤2. For the prime-witness subfamily the same argument gives `√log H` instead in both places. No claim at an individual prime or of improvement to the unrestricted U₇ tail.

*Proof.* In that proof take its notation `t=log X`, `K=⌊X^{1/480}⌋` and `a=1,b=2`. Use `J₀={1}∪{odd primes ≤K}` as the allowed multipliers, so every `f=kℓ` has at most two prime factors. Its uniform estimate (2) gives `μ_c ≍ t h(J)` in each CRT fibre, where `h(J)=∑_{k∈J₀,(k,c)=1}1/k`. Take the rough selector `S=1_{(n,P_y)=1}` with `m=t log t`, `y=m`. To retain the harmonic mass from primes *above* y on selected fibres, use the z75 tail bound for `W=∑_{y<p≤K,p|n}1/p`: except on relative measure `O(exp(−y/2))`, it is at most 1/2. For this multiplier set removal costs *exactly W*, so `h(J)≍log log K≍log t` by Mertens. Always `μ_c≪m`. Conditional Bernoulli independence at the large ℓ and the same truncated Taylor majorant of degree O(m) now give mean `O(exp(−c₁m))` and transfer error `exp(O(mt))`, since there are no more atoms than in z75 and the selector has ≤`2^{π(y)}` terms. Choose `t=α√(log H/log log H)` with fixed sufficiently small α. The transfer error is ≤√H, and at most y primes were excluded. For prime witnesses alone take `J₀={1}`, `S=1`, `m=t`, `t=α√log H`; no harmonic-weight deletion at all. This second case parallels `Z56_FAMTRY.md` Thm A on prime moduli; not a claim of new sieve technology. ∎

**Adversarial panel (finite positive certificates, not an exhaustive new census).** Took all 1 mod 8 primes from the stored z76 hard-panel n column, the star/gstar and R₈ screens, plus the named controls. `z77_u7_panel.py` finds `f=cq≤5·10^6`, `c=1,3,5`, for 7762 of 7771 distinct primes; six of the nine survivors exceed 10^12. For each of those six a separate shifted-divisor search found a positive certificate, largest returned `f=872633129255=5·174526625851`. The three small survivors are exactly the previously certified C exceptions 3361,21841,76441 (each satisfies B, z68). Thus **no new counterexample to B or C** on this panel. Data list p,f (0 means bounded miss only); six follow-up rows give p,search letter,f,c. F1: a good word has negative Jacobi, impossible at an odd square; M,D may scale instead. F2: no inference of 8/131 or 8/241; the C-odd witnesses of the analytic corollary deliberately do not require even C. R₈ zeros and 241 are included where p≡1 mod 8. F3: A,B have no primality requirement, but do not force a good word at 4545; the prime corollary does not apply there. F4: the prime claim allows pointwise failures; the panel tests the actual borrowed-cofactor target, not a star witness. No new Rédei-rank forcing or orbit theorem; track 1 was the productive route.

Replay from repo root, with assertions enabled:

```
ulimit -v 1000000
export PYTHONDONTWRITEBYTECODE=1
timeout 90 uv run --offline --no-project python scripts/z77_proth_verify.py
timeout 90 uv run --offline --no-project python scripts/z77_u7_panel.py
timeout 90 uv run --offline --no-project --with cypari2 python scripts/z77_u7_follow.py
```

The Proth checker requires no PARI, SymPy, discovery-code import or unverified search hypothesis. Discovery: `z77_proth_cover.py` at (k,H)=(255,5040),(1023,55440),(4095,55440); `z77_proth_extra.py` at (1023,55440,55440),(4095,720720,55440). `data/z77/proth/15-5040-1.json` is discovery data only and not an input to any theorem: the incomplete (S)-only attempt at 15 left 19/5040 residue classes; these are *not* (S) failures.
