# Hostile review of O219, commits 16fcb549..b7edeb14

## Verdict

**No FATAL mathematical counterexample found. Two MAJOR certification/reproducibility gaps prevent accepting Theorem 3.4 as a certified computer-assisted proof as written.** The algebraic strategy looks sound and the reported numerical result reproduces. Distinguish an unproved numerical certificate from a refutation of the underlying theorem: I have not refuted the theorem, and the 0.01499 margin makes repairs plausible.

Reviewed every added source/document, the table coverage and overlaps, the imported reduction, and the specific finite/tail bounds. Did not regenerate the large tables. All executed checks used `ulimit -v 8000000` and timeouts; no large se_box range was run.

## Findings

### M1 — MAJOR: “outward-rounded, fail-closed” is not established by the implementation

Locations: `STERILE_EXPLICIT.md:118-122,131-135,149-160`; `scripts/se_box.c:6-8,14-15,44-48,80-90,108-120,148-160,167-177`; `scripts/se_tail.py:9,29-30,44-52,55-62`; `scripts/se_r0.py:40,45,82-85`.

The C code uses round-to-nearest arithmetic with selected multiplicative padding, not directed/interval arithmetic. In particular:

- `N0`, `lam`, and successive box boundaries are un-enclosed `powl` results. Integer counts, pruning inequalities, `a0`, `a1`, and `ceil/floor` decisions are evaluated before any general outward-rounding step. For nonintegral box ratios, independent evaluations of the upper endpoint `lam*X` and next lower endpoint `powl(2,s*(i+1))` are not even guaranteed to make a gap-free cover.
- The `1e-12` Coppersmith margin is useful, but does not certify these other decisions. A final `1e-9` inflation cannot by itself prove that no populated box was discarded.
- `se_tail.py:9` says **all exponents/constants are rounded upward by 1e-9**. This is false: `mul`, `LA`, coefficients, and exponent arithmetic use ordinary floats. There are special cushions in `lC`, `lcw`, and `kap`, and the combiner subsequently rounds exponents upward; these are not the claimed general rounding policy.
- There is no documented error budget, libm accuracy assumption, required `long double` precision/range, compiler setting, or check of exceptional floating-point results. Thus the mathematical justification for the safety cushions is absent.

This is a proof-certification issue, not evidence that the present tables are numerically wrong. With dyadic/integral boxes, this platform's extended precision, and generous margins, many concerns may be dischargeable by a short explicit error analysis. But those restrictions, the error bounds for discontinuous decisions, and the generation environment must actually be stated and checked. Alternatively regenerate using interval/directed-rounding arithmetic, use exact dyadic boundaries and conservative integer counts, and fail on non-finite intermediates.

The fail-closed claim also fails as software behavior: `se_r0.load` accepts NaN/negative numbers and duplicate indices (`:15-20`); `table_max([{0: (float('nan'), 1)}], 0, 1)` returns zero, because `max(0.0, nan)` retains zero (`:33`). `S >= lim` is false for NaN (`:84`). The committed tables are finite and positive, so this does not demonstrate a bad committed row; it demonstrates that “fail closed” needs real validation, not just comments.

### M2 — MAJOR: the finite certificates have no replay/provenance specification

Locations: `data/se/P_q4.txt`, `P_q1.txt`, `P_q1_hi.txt`, `Q_q4.txt` (whole files); `STERILE_EXPLICIT.md:155-164`; `scripts/se_box.c:4-5,142-148`.

The theorem's supplied tables contain 1,352 distinct finite cells (1,373 rows before removing the 21-row overlap). The checked-in data contain only outputs. No committed command records their `g`, `T`, or `W`, compiler/flags, floating-point platform, or generator version. These parameters change the boxes and bounds. The documented `se_r0.py 32 600` only *trusts and combines* the supplied numbers; its one-line output is not an independent verification of them. The small enumerator also does not verify these range tables.

Add an exact replay script/manifest (including range splits and environment), preferably a lightweight certificate checker that verifies route witnesses and all coverage/rounding conditions without rerunning an unconstrained search. At minimum, make the claimed computation reproducible and attach the numerical error argument from M1.

Evidence against overstatement of this finding: I regenerated just cell `j=128`, P and Q, with `q=4,g=1,T=1000,W=24`; both match the committed lines exactly. All table indices are complete and the overlapping P octaves agree exactly. Thus there is no detected missing or conflicting table cell, only missing provenance and certification.

### m1 — minor, but an actual false proof premise: not every tail term increases in N

Locations: `STERILE_EXPLICIT.md:158-159`; `scripts/se_tail.py:120-123`; `scripts/se_r0.py:70,79`.

With the actual W=40 settings, the aggregated Q list includes

`74 N^(-1/16) + 56 N^(-1/8) + 40 N^(-3/16) + 26.5 N^(-1/4) + 14.5 N^(-5/16) + 6.5 N^(-3/8) + 2 N^(-7/16)`.

These terms decrease, so “evaluate every term at the top of the N-range because every term increases” is false. **This is repairable without changing the resulting bound:** the *whole* Q tail majorant is increasing. For example, its positive term `2554.5 N^(1/16)` alone has derivative with respect to ln N greater than 12,151 at N=2^100, whereas the combined absolute negative derivative of all the terms above is less than 0.062 there. The former increases and the latter decreases thereafter. No other selected terms have negative derivative. Add this verified total-monotonicity argument/check, or cap negative exponents at zero and regenerate the combiner log. I do not claim that the current endpoint value actually underbounds the entire Q majorant.

Also `STERILE_EXPLICIT.md:135` says every Q exponent is ≤0.75; the raw maximum is **0.7500001**, and the combiner's rounded maximum is **0.750001**. Both are safely below 1, but the literal stated inequality is false.

### m2 — minor: Table 2 applies the divisor function to an upper endpoint as if it were monotone

Locations: `STERILE_EXPLICIT.md:86-93` (especially τ₃ row `:91`).

`τ₃((N+E1)/4)` is not a valid upper bound for all `τ₃((N+e)/4)` with e≤E1: τ₃ is not monotone, and that endpoint need not even be an integer. Likewise `cop(n,...)=min(...,τ(n))` cannot use τ of an upper bound on the integer being factored. The implementation correctly uses the **monotone envelopes** `min_eta C_k(eta) x^eta`, not these literal functions. State the envelopes in the table, or a maximum over the actual integer range. This does not invalidate the implemented τ routes.

### m3 — minor: certificate driver accepts configurations outside its proved domain

Locations: `scripts/se_r0.py:48,57-61,64,72,73,81-88`.

There is no requirement `Bmax >= 600`, although the advertised extension from the last checked range to all larger r relies on every N being in both tail ranges. There is no `B0 <= Bmax` check (a reversed interval can print success without checking any r). The 100,000 iteration caps have no failure branch if convergence was not reached, and proof-critical assertions disappear under `python -O`. Validate the supported domain, use explicit failures, and check termination. These defects do not occur in the reproduced `32 600` invocation.

The `1e-20` remainder is not a defect for the actual invocation; its justification is supplied below. It should become a checked bound rather than a magic constant in a general-purpose driver.

### m4 — minor: scope and presentation

- `STERILE_EXPLICIT.md:168` and `reviews/agent-reports/AGENT_REPORT_O219.md:21-22`: “no 13-generic sterile point exists at all” needs **in the non-residue cells**. Covering those cells says nothing about residue-cell points; x=1 itself is 13-generic and cannot belong to an ET class (that would give a positive-integer solution of 4/1).
- `STERILE_EXPLICIT.md:137-149`: §5 is inserted between §3.3 and §3.4. Move it after the theorem. `:12` refers to nonexistent “Table 1.2”; `:101` calls the now-committed Q script a `/tmp` prototype. The interim report's level-1 diagnosis is explicitly a checkpoint, but conflicts with the final diagnosis and should link to the final status.
- `se_box.c:6` says Q boxes are in `(a,d,f)`; actual boxes are `(c,d,f)`.
- The continuum/grid scripts are appropriately labelled evidence, not proofs. Preserve that qualification for the “exactly 2/5” and q=27 headlines. The finite-exponent asymptotic derivation in Corollary 1.4 should state 0<β<1 and handle endpoint/trivial cases separately; this is not a problem with the finite lemma used by the certificate.

## Substantive checks that pass

### 1. Lemma 1.3 and Corollary 1.4

The finite statements are sound. Removing primes dividing s gives n1 coprime to s and retains every unit-class divisor E. The shifted linear polynomial is correct modulo n1. Every basis polynomial is divisible by E^m at the associated integer root; the triangular leading coefficients give exactly `n1^(m(m+1)/2) X^(w(w-1)/2)`. Minkowski yields the coefficient bound (at volume equality, take a limiting sequence of slightly larger cubes); strict (Cop) then forces an ordinary polynomial zero. Degree and injectivity give w−1. There is no missing LLL loss or algorithmic short-vector assumption.

Partitioning into J intervals proves the finite corollary; shared endpoints only overcount. For 0<β<1, letting m grow sufficiently slowly, choosing w/m appropriately, and allowing arbitrarily small exponent slack gives the stated asymptotic interpolation; if the interval in the auxiliary variable is bounded, treat that case separately instead of dropping the +1/2 in X. No use of the asymptotic heuristic is needed in `se_box.c`.

Replayed the exact-rational test: 200 eligible cases, zero violations, 69 tight.

### 2. Finite routes, units, and coverage — valid in exact arithmetic

For P (`se_box.c:79-103`): all ten route constructions are valid. E0,E1,b0,b1 and the f-window follow from Lemma 1.2 with 2 replaced by lam. H counts triples. A counts the congruence for e over (a,d). C,D,E use the three factorisation identities and their correct worst-case integer sizes. F counts (e,a), then either b or its cofactor d; G counts (e,d), then square-root classes for a (or b). The τ₃ route counts ordered triple factors. I fixes (c,e,a), hence d; J fixes (c,e,d), giving a quadratic with at most two roots (its extra Omega factor is harmless).

For P, gcd(e,abd)=1 and e odd follow as stated, so the F classes and cofactor classes are units, and the G square-root bound is ≤2^omega(e). C,D,E use −1 classes. The explicit divisor constants correctly restrict primes to p≤k^(1/eta); the binomial-ratio sequence decreases, justifying the stopping rule after passing the maximum.

For Q (`:107-138`): from `c(4abd−1)=F(a+b)` and a≤b, obtain cd≤F; from `fb=aF+c` and c≤2b obtain f≤F+2. These justify both outer and inner loop cutoffs. The displayed a,e,b windows are conservative, including `b0=max(a0,E0 F0/(4 a1 lam D))`. AD uses the valid at-most-two-divisors argument of M17C. The fa, AC, CD, Ea, Ed, τ₃, fac, fca, fda routes all reconstruct their tuples and use the correct moduli. In particular `4abd=eF+1` makes e odd and coprime to abd; `ef=4a²d+1` makes f odd and coprime to 2ad; in-cell r∤acd makes f coprime to F and the −F classes modulo 4ac and 4cd units. Thus the inverse-F and square-root f-routes are legitimate.

Row aggregation (`:166-175`) is also valid: for each actual fixed pair (a,d), respectively (c,d), a distinct datum has a distinct divisor f of the stated one integer. Taking a uniform τ envelope times the number of pairs bounds the whole row, so the minimum with the box sum is legitimate. The imax range covers every variable because P has a,c,d≤N and Q has c,d≤F, f≤F+2. The reservation is numerical coverage/rounding in M1, not an algebraic missing route or row.

The existing exact enumerator gave P(4913)=32 and Q(4913)=73, with zero box/row violations. It only checks the minimum bounds at small occupied boxes, not every individual route, every empty-region pruning decision, or large range computations; it is evidence, not certification.

### 3. Tail lists for all N≥N0 — exact-arithmetic derivation checks out

P's capped exponents are safe: dropping factors 1/2 from `2a²d≤N` enlarges the coordinate ranges, and using `min(sum of capped exponents,1)` for acd is legitimate. The f lower bound is `4N^s−1≥3N^s`; the F/G integer sizes are ≤(N+e)/(4a)≤N/(2a), and similarly for d. The τ₃ factor is correctly `C3(0.3)(N/2)^0.3`, since e≤N. The omega constant product includes p=2 even though e is odd; that only overestimates. Its omitted primes have factors ≤1.

For Q, cd≤N implies c²d≤N², giving the CD argument ≤5N² even in boxes extending past the feasible region. The a window obeys `.25 N^(1−xc−xd−2u) ≤ a ≤ .5 N^(1+u−xc−xd)`; the AC integer upper bound follows because N^u≥2 at the stated threshold. The logarithmic harmonic estimate in fac is conservative. All loops cover the feasible normalized coordinates. Negative exponents are allowed in valid upper bounds; their endpoint use is the separate issue m1.

Here is the missing explicit explanation of `se_tail.cop`: let g(L)=g0+s0(L−L0) and B=w(w−1)/2. The tests ensure g(L)<0 for all L≥L0, so Xmax=exp(−g(L)/B)>1. Choosing J=ceil(N^kap), k1 controls the slope and k2 controls the value at L0 of

`ln(c1/cs) + (x1−xs−kap)L + g(L)/B`.

It is negative thereafter. Hence window/(sJ)<Xmax and `X_J < (Xmax+1)/2 < Xmax`; (Cop) follows. Also J(w−1)≤(w−1)(N^kap+1), precisely the emitted list. Thus the linear-in-ln N argument is sound, subject to certified numerical evaluation of its strict tests.

Recomputed W=40: P has 4,913 boxes, 13,393 terms, max exponent 0.4796876; Q has 2,601 boxes, 8,587 terms, max exponent 0.7500001. After combiner aggregation the exponents are ≤0.479688 and ≤0.750001. Every relative-decay test passes, with minimum slacks >8.44 and >16.32 respectively.

### 4. Combiner weights, lookup, r-tail, and remainder

P's weight `2 r^(-(K+1)/2)` and Q's weight `2 r^(-k)` are correct; both loops use odd positive indices. For the actual b-grid, all bit endpoints are exact quarter-integers, so the table walk covers every required cell. P quarter-octaves are j=124..799, P octaves 200..599, Q quarter-octaves 124..399; the P files overlap at 400..420 with identical entries. No gaps, negative values, NaNs, or duplicate indices occur in the committed files. Using the maximum across cells and the largest weight is conservative; at a table/tail crossing, taking the maximum of the two region bounds is correct.

For a weighted monomial, differentiation with respect to ln r gives `K(e−h)+p/ln r`, with an additional −1/2 for P. The relative-decay condition at N0 makes this nonpositive whenever r^K≥N0. Hence the extension beyond r=2^600 is justified, once the endpoint bound in m1 is properly explained.

The remainder can be bounded independently. A successive-odd-index ratio for the separated-endpoint bound is

`rho <= 2^(2(e(b+1/4)−hb)) (1+2/K)^p`.

For P use e≤0.479688, p≤2, Kb≥600 and `(1+2/K)^p≤exp(4b/600)`: uniformly for b≥32 this gives rho<0.60. For Q use e≤0.750001, p≤1, kb≥100: rho<0.00004. Thus after a term below 1e−30 the total omitted P+Q contribution is <1.6e−30, comfortably below 1e−20. This also verifies decay for the endpoint-separated bound, not just for the true r-dependent expression. The iteration cap is nowhere relevant to the actual parameters.

Replayed `uv run python scripts/se_r0.py 32 600`: **max S=0.485006 at b=32, zero failures**, exactly matching `data/se/r0_certify.txt`.

### 5. Reduction to (S), including general odd r

The citations suffice and the imported proofs remain valid for general odd prime r; this is not a hidden r≡1 mod 4 assumption. I checked M17 Lemmas 1.1, 1.3, 2.1–2.3, 5.1, 5.2 and §6, M17B Lemma 1.1, M17C Lemma 2.1(iv), and R187 §1.1.

The Jacobi calculation is at the odd denominator f≡−1 mod 4d, not an assumption on r: `(-d/f)=-1`, while `(-d/g)=1`, implies `(-d/r)^k=-1`. Thus Q has odd k and non-square centres, so sqrt-Q is empty. The analogous P calculation gives `(r^K/f)=-1`, ruling out even K. Reflection gives Q inverse closure. U containment uses valuations and the same parity argument; U inverses are absorbed by P inverse closure. In-cell P excludes r|ab because that would give centre 1; Q excludes r|c because it too gives centre 1, while the original Q level requires r∤e. These are exactly the primitivity hypotheses used by the route engines.

Two orientations per a≤b datum give the factors 2, the non-residue cells have measure (r−1)/(2r), and the finite-covering implication follows by a clopen neighbourhood and Dirichlet, requiring 8·3·product of primes below r in its away-from-r modulus. This matches the general-r argument in R187. No ES existence claim is smuggled into this reduction.

## Recommended disposition

Keep the mathematical lemmas and numerical evidence. Do not advertise the checked-in tables as a completed outward-rounded certificate until M1 and M2 are discharged. Fix the small literal errors and record the total-Q monotonicity and geometric-remainder proofs. There is substantial evidence that the advertised threshold survives these repairs, but reproducing the number alone is not the missing certification argument.
