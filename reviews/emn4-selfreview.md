# MN4 hostile self-review

Reviewed baseline `86a09a989fa9a975b4bcd22ad49fdb63d997b6e6` through `ff2d752b7464dd4bd0476ed442924bfbc10a0d36`: all eight commits, comprising `EXCEPTIONAL_MN4.md`, `scripts/emn4_checks.py`, and its recorded output. Locations below refer to that tip. Read STATUS/ledger label conventions, MN2, MN3, and TTL, including the actual TTL §8 assembly rather than just its theorem statement.

**Verdict: sound conditional transfer after minor repairs. No FATAL or MAJOR defect found.** This is relative to the stated, previously reviewed TTL/MN3 inputs and their cited analytic theorems, not an independent external certification of the entire campaign. In particular, it is not an unconditional removal of ET's logarithm. I found one incorrect displayed inequality, an omitted endpoint in the explicit assembly, and presentation/replay defects. None needs a new analytic estimate: repairs are given below. The main-term coprimality accounting survives scrutiny; merely declaring polynomial m-losses harmless would not have sufficed, but the document does substantially more than that.

## Findings

### R1 — MINOR: a missing `1/m` in the crucial (b5) display

**Location:** `EXCEPTIONAL_MN4.md:522–524`, §4(2b), complementary Brun–Titchmarsh case of (b5).

The intermediate expression starts with `N g(m)`, but its subsequent bound is `N g(m)h/m`. Applied to that intermediate expression, §3.2(c) gives only `O(N g(m)h) = O(N)`. That displayed chain is incorrect as written, precisely at a point where losing m would be unacceptable.

**Repair:** replace the intermediate prefactor by `N g(m)/m`. Indeed

`1/φ(mcdf) ≤ 1/[φ(m)φ(c)φ(d)φ(f)]`

and hence the unsaved cell mass is at most

`(N g(m)/m) · (Σ_{c≍C} g(c)/c) · D^{-1} Σ_{d≍D} g(d) Σ_{f≍F} ρ_{md}(f)/φ(f)`

`≪ (N g(m)/m)h = N/m`.

BT then supplies `O(1/k')`. This is a local transcription error, not a missing coprimality lemma: the required factor is already present in the original modulus. Retain this calculation explicitly rather than appealing to “every term multiplied by 1/m.”

### R2 — MINOR: explicitly close the bounded-c endpoint

**Location:** `EXCEPTIONAL_MN4.md:515–532`, especially the `1/j` expressions at lines 520, 530, 532. Compare TTL Lemma 1.1's explicit `j=0` remark.

The replacement list does not explicitly treat `c=1` (or, depending on dyadic conventions, the bounded initial c-block). Starting the sums at `j=1` misses this block; including `j=0` makes (b4) and the displayed sums undefined. TTL's endpoint discussion is not one of its numbered §8 steps, so “steps (1)–(5)” is not an explicit substitute for it.

**Repair, using existing lemmas:** isolate `c=O(1)` and retain the same low-D and band treatments. For `k≤C₁ log L`, use the trivial c-count and §3.3(a2): here A and D are large, and each whole layer costs `O(hADL) ≤ O((N/m)L)`. The total is `O((N/m)L log L)`. For larger k, (b1)/(b3) cost `O((N/m)L/k)` per layer, again totaling `O((N/m)L log L)`. In (b2), the condition `δ≥2γ+O(1/L)` holds once k is large because γL is bounded; sum its per-cell estimate over at most O(L) cells. For (b5), the existing per-cell `O((N/m)/max(k,k'))` bound sums to `O((N/m)L)`. All fit inside `O(NL²/m)`.

Thus there is an omitted endpoint paragraph, not an uncovered positive-width region or a renewed log-log loss. Also specify the index convention (`k=⌊δL⌋`, `k'=⌊(β−1)L⌋`, and j dyadic in c); log-base constants only change the absolute splitting constants.

### R3 — MINOR: Lemma 0.1 overattributes its range and points to a nonexistent section

**Location:** `EXCEPTIONAL_MN4.md:12–13,21–25`.

The numerical inequality in Lemma 0.1 is correct. Its density consequence for every `m>L^5`, however, is not solely MN3 Thm L': MN3 requires `log m≤L/10`. The parenthesis acknowledges this but sends the reader to “§9,” which does not exist here. The full argument is actually §5.1(i).

**Repair:** split the lemma's consequence into the MN3 range and the MN2 Lemma 3.5 range, citing §5.1(i), or say “MN3 Thm L' together with MN2 Lemma 3.5.” Do the same in the summary. No change to the cutoff or to exponent −0.35 is needed.

### R4 — MINOR: contradictory range wording and stale proof-status prose

**Location:** `EXCEPTIONAL_MN4.md:19,63,500,535–538,573–585`; STATUS's existing m=4-only description.

“§3.2(c) is false in all ranges” literally contradicts the correctly restricted lemma. What is false is its *extension to all ranges*. The draft heading “superseded ... once written,” the assertion “No existing repository file was changed,” and the internal declaration “No mass/BT issue remains” are unedited handoff prose, not mathematical status information.

The remark that m enters “only through h” in main terms also needs to say **retained regular sieve main terms**: the displayed theorem still contains `log² m`, and §3.3(a3) deliberately pays `log m` in the separately summed low-D contribution. The restriction `m≤L^5` is used in absorbing those mass errors as well as in the spectral remainders.

**Repair:** say “the all-ranges extension of §3.2(c) is false”; remove obsolete handoff language; qualify the main-term remark; attach an actual review status. Once adopted, synchronize STATUS/ledger so they no longer say the m-uniform extension was not attempted. Preserve the explicit CONDITIONAL label and the distinction between matching orders and a sharp threshold constant. No mathematical claim here should be advertised as externally refereed.

### R5 — MINOR: the finite-check script cannot fail the replay

**Location:** `scripts/emn4_checks.py:49–62,75–88,91–117,120–127,153–158`.

`check1` and `check3` merely print failure counts; `check2` prints a minimum without checking it; `check4` prints occurrences without requiring one. The process exits successfully even after a mathematical check fails. This matters if “replay green” is used as a gate for subsequent changes.

**Repair:** make these existing exact checks assert their invariants, or return failure counts and exit nonzero. Do not turn `check5`'s empirical ratios into a theorem-like tolerance test. There is no need to duplicate the existing tests.

### R6 — MINOR: identify the gain experiment as outside the proved range

**Location:** `EXCEPTIONAL_MN4.md:594–596`; `scripts/emn4_checks.py:134–150`.

The gain experiment has `D=F=300`. It cannot satisfy both `m≤L^5` and `D,F≥L^{100}` for any tested m: these conditions imply `L^{100}≥m^{20}≥4^{20}>300`. The current EVIDENCE/not-proof label is good, but readers should not mistake this for a numerical instance of the restricted uniform lemma.

**Repair:** explicitly call it a small-range heuristic diagnostic for the h-scaling, outside §3.2(c)'s hypotheses. Do not propose enumerating at `L^{100}` to fix this; the proof, not a large brute-force test, is the relevant validation.

## Substantive audit

### 1. Uniform main terms: the apparent Euler-factor problem is actually paid

I challenged each place where `1/φ(m)` could silently replace `1/m`.

* **Sieve denominator (§3.5).** The estimate `G(z)≳[φ(2mcs)/(2mcs)]log z` is uniform, including when the excluded modulus exceeds z. The probability argument is valid: for squarefree Euler-product weights the inclusion probability of ℓ is ν(ℓ), so the expected log-product is `Σν(ℓ)log ℓ≪ε log z`. Truncation at r<z retains a fixed fraction of the product. The remaining Euler factors differ from Mertens' product by an absolutely convergent product. No extra `log m` is required.
* **Fixed a (§§2.6,3.5).** Here one should not replace the Poisson main term by an arbitrary divisor estimate. Its exact mass is `Dφ(ma²)/(ma²)`, and `g(2mca)φ(ma²)/(ma²)≤2g(c)` gives direct cancellation. This is stronger than merely absorbing g(m) into a remainder. Primes dividing d must not be dynamically excluded in this varying-d sequence; the document correctly uses the fixed modulus `2mac`.
* **Fixed d (§3.5).** The q=1 comparison `Xσ≤#σ+|rσ(1)|` is legitimate for nonnegative weights. Weighted (a1) gives hADL for a layer, and weighted (b) gives hAD for a small-cusp cell. Multiplying by `g(2mcd)≤2g(m)g(c)g(d)` cancels h without demanding a lower bound for any individual spectral model mass. The extra weighted q=1 error is indeed a remainder, where polylogarithmic losses are harmless.
* **Short-modulus acf fibres (§3.1).** The gain comes from `(f,m)=1`, not from the modulus: expanding `1/φ(f)` and using the coprime harmonic sum is valid. The other two harmonic variables each cost O(L).
* **ab fibres (§§3.1,3.2(b)).** Divisor pairing must use the m-free part of a+b. The supplied argument does so. Pairing divisors of a+b itself would be invalid. The error `A√B log B` is absorbable when B≥T; the small-B boxes total only `O((log L)³)` before the common BT factor and do not reintroduce g(m) at leading order.
* **cdf fibres (§§3.1,3.2(c)).** The large-range root sum retains h. The D<T and F<T parts of the global short-modulus sum are separately bounded by `O(L(log L)²)` before the c-sum, versus the allowed hL². Since `g(m)≤L^{o(1)}`, this is genuinely lower order. There is no application of the restricted lemma to these small ranges.
* **(b4) (§4).** BT's weight is `g(m)g(a)g(d)`; the needed input is (a2), not the one-weight (a1). The document uses (a2). Its size condition holds where (b4) is selected: for δ≤1/3, `min(A,D)≍(N/(mC))^{1/2}N^{-δ/2}≥N^{1/3−η/2}L^{-5/2}`, hence ≥N^{1/4} for fixed small η and large N. For k>L/3, use the spectral/Weil bound alone as TTL does; do not extend (b4) into tiny D.
* **(b5).** The complementary BT modulus really is `mcdf≍N^{2−β}`: substituting `acd≍N/m` cancels m. Its denominator therefore saves `1/k'`, not `1/(k'−log m)`. The per-cell harmonic bound is correct after R1's prefactor repair. D>T and the bad-region lower bound for f ensure §3.2(c) applies.

**Conclusion:** no hidden leading `g(m)` or `log m` loss found. The polylogarithmic restriction on m is not, by itself, the reason this works; the explicit cancellations above are indispensable.

### 2. The new root-sum lemma is not a disguised nonuniform character estimate

**Locations:** §§3.2(c),3.3,3.5 (`EXCEPTIONAL_MN4.md:357–434,484–492`).

The most dangerous tempting shortcut would be to import TTL's bounded-D character argument uniformly in m. The document does not do that.

For `Y≤Y₀=D/log²(2D)`, the mean-square expansion has square terms bounded by

`D Σ_{rr'=square}1/(rr')=O(D)`.

For nonsquares, `(−m/rr')` is either zero or a unit factor, and PV in d costs `O(√(rr')log(2rr'))`; the total is `O(Y log(2Y))`. For larger Y, the PV tail in r costs

`O(√(m/D) log(2mD) log²(2D))=O(1)`

when `m≤L^5`, `D≥L^{100}`, `D≤3N`. Thus the potentially dangerous √m is actually controlled.

The hyperbola/inclusion–exclusion error `J√(HV/F)` need not itself contain h. This is not a defect: (3.2.2) handles `F≤D/L^{20}`, while in the complementary range (3.2.1) has error at most `O(L^{14}D^{-1/4})=o(h)`. All factors of H and √m have room to spare. Cauchy–Schwarz with `Σg(d)²≪D` preserves the weighted statement.

The 2-adic extension also survives: for odd md, roots modulo powers of 2 are bounded by four, and adjoining one factor 2 increases the root count by at most two. Thus the factor-four convolution majorant and squarefree-r inequality used in the proof remain valid; imposing an unjustified odd-f restriction would have been wrong.

In (a1)/(a2), the weighted series with additional `t^{2/3}` and `r^{1/3}` converge. This is why using the second MN3 Λ-bound removes `log m` in the retained region. For low D, (a3) instead permits `log m`, but summing only `O(log L)` D-blocks and reciprocal-log c-weights costs

`(N/m)L log(2m)(log L)² ≪ (N/m)L(log L)³ ≪ NL²/m`.

This is a valid aggregated substitute for a false all-ranges per-cell bound. The CRT counterexample to that all-ranges bound is sound and lies outside the retained large-D/large-F range.

### 3. Spectral transfer: normalization and level checked

**Locations:** §§2.1–2.7 (`EXCEPTIONAL_MN4.md:89–300`).

I do not find a missing parity index or a new spectral conjecture beyond the explicitly enlarged family.

1. With t=md, `[f,2ta,te]` has discriminant −4t exactly, and the full set is `ef−ta²=1`, including negative/zero a before weights. `Γ⁰(t)` preserves both `2t|B` and `t|V`. Scaling first by t and then by q gives `Γ₀(t)∩Γ(q)` and finally the stated subgroup of `Γ₀(tq²)`. The converse matrix calculation works too. Its infinity width is one.
2. Adjoining −I produces the quotient `(Z/q)×/{±1}` and precisely the even characters mod q. The separate q=1 convention is necessary and correctly included. `Γ₁(M)` is contained in the resulting group, so Selberg for all `Γ₁(M)` implies the required absence of exceptional spectrum. A theorem uniform in all m means this family is assumed simultaneously, not merely for m=4.
3. I visited the cited [Drappeau source](https://arxiv.org/html/1504.05549#Thmthm1), checking its Fourier expansion and §4.2.2, (4.23)–(4.25). The bound is indeed `(K²+q₀^{1/2}μ(∞)N₀^{1+ε})||a||²`, with `μ(∞)=1/M`. Its `√nρ(n)` differs by the constant 1/2 from TTL's coefficient, since `W_{0,it}(4πny)=2√(ny)K_{it}(2πny)`. There is no hidden √n or M-loss. No coprimality between the character modulus and M is required.
4. The separation argument is discriminant arithmetic and retains the same absolute constant. Content-two forms do occur for odd t≡3 mod 4, but their good-prime reductions remain nondegenerate, so the density calculation remains valid. Their primitive quotients require the `h(−t)` term; the document includes it.
5. The one-orbit-per-integral-class bound in §2.5 is stronger than TTL's looser r(d) bound, but is justified. Keeping **both** congruences forces the second column into the radical line of the Gram matrix modulo t. A unit leading coefficient makes that kernel a free rank-one direct summand, including modulo prime powers, not just over fields. At primes dividing t the matrix is nonzero of rank one; content two is harmless since then t is odd. There is no extra factor r(md) to carry into the remainder.
6. Re-deriving the summed error gives exactly

   `L^C Q²[(mD/A)^{1/2}(1+A/F')^{1/2}+F'^{1/2+ε}/A]`.

   The m^{1/4} from the square-root class-number sum combines with the first cusp factor to give √m, and cancels against the second cusp factor. The document normalizes by AD, not by a possibly very small actual mass for a particular d.
7. The q-power repair in §2.4 is real: keeping `q^{ε−1/2}A^{-ε}` avoids the unwarranted `q≲A` condition. Likewise the weaker (b3) exponent `N^{-δ/4}` is sufficient; there is no need to defend TTL's stronger displayed exponent. In (b2)/(b5), the growing-period factor is paid by δ≥2γ or β−1≤δ/2, and the other cusp term has an absolute power margin. All chosen cells satisfy `A√(md)≥𝓛³` for large N.

The effective crossover is only at D=A **up to polylogarithmic losses** for varying m: √m occurs in the spectral error and in the Weil comparison. This does not create a positive-width gap. The `k≤C₁ log L` BT treatment absorbs the logarithmic displacement. In contrast, replacing the SEL hypothesis by Kim–Sarnak leaves a positive-width strip, so the unconditional disclaimer is appropriate.

### 4. Coverage of every TTL §8 component

| TTL component | MN4 replacement and assessment |
|---|---|
| Type I reduction and w-tuple identities | §1. Forward injection plus y/z swap suffice; no converse parametrization of all relaxed tuples is needed. |
| Large c, §8(1) | §3.4. Counts tuples, not only represented primes. The removed `L≤√m` hypothesis is replaced legitimately by `L log² L≪L²`. Tiny boxes retain BT's `1/L` when X≤N^{1/2}; the tail above that is negligible. |
| Three short moduli, §8(2a) | §§3.1–3.2. Additive/nonreduced-fibre errors are power-small. Other moduli are long automatically; m shifts the exponent inequalities by only O(log L/L). |
| Smooth cells and ordinary bands | §§2.7,3.5. Bands use the per-cell root bound, not the layer divisor bound. |
| TTL's D≤64 band | Replaced, not forgotten: all D≤L^{100} are removed and summed by §3.5's final argument. |
| (b1) | §§2.6,2.7 and fixed-a mass cancellation in §3.5. |
| (b2) | e-cusp for sufficiently large k versus j; otherwise whole-layer (b4). |
| (b3) | Smaller divisor cusp; κ=1/4 remains sufficient. |
| (b4) | §3.3(a2) plus BT; valid in its stated δ≤1/3 range. |
| (b5) | Both alternatives covered, with the per-cell mass rather than an extra factor L; correct the display in R1. |
| Sieve/model mass comparison | §3.5; q=1 error stays a remainder. |
| Small k | §4(4), O((N/m)L(log L)²), with R2's bounded-c supplement. |
| Large k and final double sum | Same `1/max(j,k)` or `1/max(k,k')` counting as TTL. For k>L/3 only the spectral/Weil bound is needed. |
| Bounded-c endpoint | Not explicit in MN4's list; R2 supplies the missing argument. |

There is no missing third analytic treatment near D=A, no forgotten β>1 strip, and no need for TTL's retired small-divisor Proposition 7.2. Smooth positivity permits bounded enlargements and dropping the original normalization restrictions; the resulting divisor masses are exactly those bounded in §3.

### 5. Lemma 0.1, Theorems 5.1–5.2, and overclaiming

After R3's reference/range repair, the global case analysis works.

* If `m>L^5` in the MN3 range, the two terms are bounded by `m^{-2/5}log m` and `m^{-3/5}log³m`, both `O(m^{-0.35})`. MN3's other hypothesis `L≤√m` follows automatically.
* If `log m>L/10`, §5.1(i)'s large-L choice makes `CL/log L≤0.65 log m`. For bounded L, representability forces `m≤3N`, giving a genuinely bounded set of relevant m; an absolute implied constant handles it. One must not simply invoke MN3 in this case.
* If `m≤L^5`, for sufficiently large N one has `m<N/2` and `log m≤L/10`; the usual prime Type I/II classification and MN2's Type II bound apply. Division by `π*(N)≳N/L` gives exactly the claimed density bound; `m^{-0.98}` is absorbed by `m^{-0.35}`. Small N in this branch also bounds m.
* Theorem 5.2 is a correct quantifier consequence. Choose cε to control the cubic term, then mε to control the other two terms. The upper half is MN2 Thm U and remains ineffective and unconditional relative to its stated inputs. No monotonicity of the finite-N density is assumed.

The conclusion is matching **orders** for low and high representable density. It does not prove a limiting profile, a threshold constant, or a vanishing-width transition window; the final remarks correctly avoid those claims. The small-A `O(A³)` range stated at line 566 also checks: for A≫m^{-0.11}, both `m^{-0.35}/A³` and `m^{-1/3}log²m/A` tend to zero.

## Replay and limits

Inspected the script before execution: its quadratic form-pair loop is streamed by `itertools.combinations`, the largest quadric enumeration is over primes ≤13, and the D=F=300 root checks use bounded nested loops, not a dense Cartesian-product allocation. Ran the existing replay with a 2 GB virtual-memory cap and a 90-second timeout:

`ulimit -v 2000000; timeout 90 env PYTHONPATH=scripts uv run python scripts/emn4_checks.py`

It completed and reproduced the checked-in output: 252 prime-input pairs with zero Type I failures; 36,802 separation pairs with exact minimum 3/2; 924 density cases with zero failures; content-two examples for all 15 tested t; the eight recorded gain ratios. Because of R5, this conclusion comes from inspecting the output, not merely from the exit status. The tests do not certify the spectral argument, class-orbit counting, uniform large-range mass lemma, or final asymptotic theorem.

Only this review file is changed. Recommended disposition: apply R1–R6, retain the conditional theorem and its precise hypothesis family, and describe the result as internally reviewed relative to the cited inputs—not as an unconditional or externally certified resolution.
