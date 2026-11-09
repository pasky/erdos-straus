# Hostile internal review: Z68 PC2

## Scope and verdict

Reviewed all three commits in `8e5ecfaa8..97ca497a4`: the memo, all added Python/shell scripts, and the saved outputs. Checked ET Proposition 1.9 and §10 against `sources/elsholtz-tao-1107.1010.pdf`, the reductions in `Z67_K11.md`, the parity argument in `Z66_UCOVER.md`, and EXSET Corollary 5.4. Independently consulted Lagarias–Odlyzko Theorem 1.1 at <https://aareyanmanzoor.github.io/assets/articles/lagarias-odlyzko.pdf>.

**Verdict: the central reduction and counting argument survive this review, but the memo needs substantive corrections before its full verdict/FRONTIER text can be endorsed.** I found no counterexample to Theorems A/E, Lemmas Q/P/V, the exact product law, or the sparse-support union bound. The principal problems are overclaims in the bridge boundary regime, a misinterpretation of Corollary K, and conflation of finite-level and infinite-level survivals. ES remains open. None of the computations certifies an infinite-level survival at 17 or 19.

**Provider/auth/quota errors: NONE.** All mathematical replay commands completed successfully. Commands were memory-limited to 6,000,000 KiB and time-limited to at most 1800 seconds; no large Cartesian product was allocated.

There were already uncommitted changes in `Z68_PC2.md` when this review began. I did not modify them. They repair the unjustified `y < F(y)` in B(i), spell out the Dedekind-zeta GRH hypothesis, and qualify the literature comparison. Those repairs are appropriate, but are not in the reviewed commits and do not resolve the findings below. This report is the only project file changed by the review.

## MAJOR findings

### M1. Theorem B(iv) and the headline/bottom line overclaim at the square-root boundary

Locations: `Z68_PC2.md` §4 B(iv), the answer following B(v), §5 and the proposed FRONTIER text; especially “in every regime where its moduli are below exp(√y)”.

The proof establishes a **power-separated sufficient condition**: `log F(y) ≤ y^(1/2−ε)` implies eventual ES under GRH. It does not establish the asserted dichotomy at `exp(√y)`, nor does `A ≤ 2` imply that PC with the particular function F has no GRH implication.

Here is a concrete counterexample to the classification of B(iv), using its own GRH estimate. Set

```
log F(y) = sqrt(y)/(log y)^2.
L = log p;  y = L^2 (log L)^3.
```

Then `log F(y) ~ L/(4 sqrt(log L)) < L`, hence `F(y) < p`. Meanwhile the GRH error relative to the main term is

```
O(log p · log y / sqrt(y)) = O((log L)^(-1/2)) = o(1).
```

Thus PC with this F **does imply eventual ES under GRH**. Nevertheless F belongs to the stated `y^(1/2−o(1))` boundary regime and satisfies B(ii) with A = 2, but with no fixed A > 2. Conversely, merely `F(y) < exp(√y)`, e.g. `log F(y) = 0.9√y`, does not make the displayed GRH error small in the permitted range. This is not just terminology: the memo puts a demonstrably GRH-ES-strength PC into its purported non-ES regime.

There is a second distinction: a bound `m ≤ F(y)` does not say every covering class has modulus **between** `exp(√y)` and `exp(y^(1−ε))`. Smaller moduli can be part of the same covering. The statement concerns the allowable maximum, not a minimum for every certificate.

**Fix:** state the A > 2 implication as proved; discuss fixed power laws `log F(y) = y^(c+o(1))` with c < 1/2 versus c > 1/2; explicitly leave c = 1/2 to a logarithmic-scale analysis. A general sufficient GRH criterion is a choice `y=y(p)` with `F(y)<p` and `sqrt(y)/(log p·log y) → ∞`. Replace “the only non-ES-strength regime” by “the regimes not settled by this particular implication”, with the qualifications above. Do not claim an equivalence between PC and ES: only PC ⇒ MF, and conditional equivalence of MF(A > 2) with eventual ES, is supplied.

### M2. Corollary K does not prove that certificates must use y^(1/5) components at once; the strategic rejection is broader than the theorem

Locations: §4 answer (“any covering must use ≥ y^(1/5) components at once”), §5 verdict and bottom line; §0 K3.

Corollary K is a correct obstruction to a **low NR-count threshold**: there are uncovered profiles with about `y^(1/5−δ)` NR coordinates. It does not imply that a class catching a denser profile must have that many primes in its support, or that the covering mechanism must use that many components in an individual event. A union of bounded-support events can, in principle, cover all sufficiently dense profiles while leaving sparse ones uncovered. There is no certificate-support lower bound in the proof.

Likewise `s/(s1 s2) → 1` rules out a fixed factor κ < 1 improvement in the *survival ratio*. It does not exclude a large gain relative to the tiny caught masses, or accumulation of mixed catches over a growing number of components. The memo itself acknowledges that it does not control Γ at the product scale of the single-prime caught-mass upper bounds. A limit in which both single-prime survivals approach 1 is not a theorem ruling out all useful many-component effects.

**Fix:** retain the precise “no uniform κ < 1 survival-ratio improvement” theorem and the lower bound on a universal NR-count threshold. Delete “components at once”. Label parking the implementation as an **Assessment**, not as a proved negative answer to all per-component or many-component routes to PC. State explicitly that PC with a linear-in-π(y) threshold remains untouched by these obstructions.

### M3. The numerical s^U values are truncated survivals, and are demonstrably not the defined infinite-level s^U

Locations: §2.3 final sentence (“reproduce UCOVER's s^U: 17: 0.19118 …”), §3.5 last table column, and the opening description of `scripts/z68_pc2_survive.py`.

By §1, `s_l^U` is survival against **all** levels. The listed single-prime values only use levels ≤ 2. This is not a merely hypothetical distinction. Re-running `events1` at level 3 gives:

* 17: survival `396/2312 = 99/578 = 0.1712802768`, strictly below `0.1911764706` at level 2;
* 19: survival `902/3249 = 0.2776238843`, strictly below `0.3040935673` at level 2.

These losses already appear in UCOVER's level-3 table. Consequently the claimed identification with `s_l^U` is false. The exact `0.1080` ratio at (17,19) is a **finite-level** ratio (also equal to the finite pure-menu ratio here), not a certified ratio involving the infinite `s_l^U`. A finite numerator divided by finite denominators need not bound the limiting ratio in either direction.

**Fix:** introduce `s_l^U(K)` and `s^(K1,K2)`, and use them in all computational tables and script documentation. Write “reproduces UCOVER's level-2 survival”. The finite-level numbers themselves are correct; preserve their CERTIFIED label with that scope. The existing finite-level caveat is good but does not justify using a symbol already defined to mean the infinite quantity.

## MINOR findings and proof repairs

### m1. The fixed-first-prime assertion of Corollary G needs an upper-limit argument and a small-prime constant

Location: §3.3, second bullet of Corollary G.

A lower bound whose right-hand side tends to 1 proves `liminf ≥ 1`, not the asserted equality of the limit. For finite ℓ₂, `s1^pure` can exceed `s_l1^U`; one cannot silently upper-bound the ratio by 1.

The result is repairable. Approximate the single-prime caught set in measure by a finite union of classes. All sufficiently large ℓ₂ divide none of their moduli, so all these classes occur in the pure menu. Hence

```
s_l1^U ≤ s1^pure(l2) ≤ s_l1^U + ε
```

for all sufficiently large ℓ₂. Together with `s ≤ s1^pure`, `s_l2^U → 1`, and the lower bound, this proves the asserted limit when `s_l1^U > 0`.

Also G(b)'s coefficient 4 requires `l1^θ ≥ 2`, which need not hold for a fixed small prime. Direct summation gives a constant proportional to `1/(1−l1^(−θ))`. Use `O_(l1,δ)(l2^(−θ))`, or explicitly use exponent slack to recover the displayed eventual coefficient. Restrict the useful parameter range to `0 < δ < 1/5`; otherwise the geometric-series hypotheses are empty.

### m2. “Injective image of a Q-point” is not the literal map being used

Locations: Theorem A headline, proof of injectivity, D1, FRONTIER text.

For I-3, one Q-point can produce several roots/cylinders; the same Q-point can also be used for different families. Different parameterizations can produce the same residue class. What is proved is reconstruction of a parameter tuple from a **family-tagged split and Q-point**, with an additional root choice for I-3. That supplies the needed upper bound, not an unqualified one-to-one correspondence between classes and bare Q-points.

**Fix:** say “every class is obtained from a family-tagged split, a Q-solution, and (for I-3) a root choice; there are at most 2^ω(F) such choices”. If an injection is desired, select one canonical parameterization per class and include the labels/root. Theorem E already counts the correct multiplicities, so its estimate is not invalidated.

### m3. The composite falsifier explanation is false

Location: F3 in §0.

For nonsquare composite n, `(n/l)` is governed by a quadratic Dirichlet/Kronecker character associated with its squarefree part. For example n = 65 gives a nonprincipal quadratic character. GRH does provide a prime NR asymptotic in the appropriate range. Squares are the principal-character exception.

**Fix:** explain the actual primality dependence: `m < p` guarantees `gcd(m,p)=1`, whereas `m < n` need not imply `gcd(m,n)=1` for composite n. The unit-profile replacement can therefore fail to transfer a class back to n. Do not deny the existence of the composite quadratic character.

### m4. Endpoint, weighted-hypothesis, and “only known” statements need qualification

Location: §4 B(iv)–(v) and the answer after B(v).

* The supremum `A* = sup{A : log F(y) < y^(1/A) eventually}` need not be attained. For example `log F(y)=2y^(1/A*)` satisfies every smaller exponent but not A*. Claim MF for each admissible A, not automatically MF(A*). A limiting exceptional-set exponent can be discussed separately.
* The weighted `(PC1)` is not actually defined. Specify the interval `(y,2y]`, the reciprocal-prime weights, the NR threshold, the modulus bound, and the constant range matching EXSET Cor 5.4(b). It does not follow from the unweighted PC as currently defined.
* `exp(c log²p)` is a sufficient scale supplied by the cited classical unconditional estimate; calling it the **only known** scale, or concluding a general “no unconditional route”, needs more justification than this estimate. State a limitation of the input used, not a universal barrier.
* The lower bound `F(y) ≥ sqrt(y)` is valid but unnecessarily weak: choosing the NR set among primes in `(cy,y]`, with fixed `c < 1/2+η`, yields `F(y)>cy` eventually by the same parity argument and the PNT. This improvement is optional and does not repair the bridge-boundary overclaim.

The committed B(i) proof's `y < F(y)` is unjustified (F has no such assumed lower bound). The pre-existing worktree edit correctly removes it. In B(ii), explicitly mention reciprocity for p ≡ 1 mod 4 and classical ES for p ≡ 3 mod 4 when transferring `(p/l)` to MF's `(l/p)`.

### m5. The general-purpose “complete” Q solver uses a non-certified floating cutoff

Location: `scripts/z68_pc2_events.py:39`.

`int((4*al*be/3)**0.4)+2` is safe at the replayed sizes, but does not certify completeness for arbitrary integer inputs. Floating rounding error can exceed 2 at sufficiently large inputs, and conversion can overflow.

**Fix:** compute an integer upper bound t by the exact condition `9*t^5 ≥ 16*(al*be)^2` (integer root or monotone correction), and use that bound for all searches. No replayed finite-level result was found to be affected. The same distinction should be made for floating comparisons in `qcheck`: it is a small-range test, not the mathematical proof.

### m6. The kill tests should fail the process, and compare should use the bounded sets symmetrically

Locations: `events.py` selftest and compare modes; `z68_pc2_compare.sh`.

`selftest` and `compare` print mismatches but return exit status 0, so `set -e` does not make them effective automated kill tests. Also `miss` tests membership in the entire unbounded reduction output, not in `small_ev`: a brute cylinder found by reduction only with a modulus above MMAX would evade that check. In the saved outputs the matching cardinalities plus zero extras independently establish equality of the bounded cylinder sets, so this did **not** falsify the reported comparisons.

**Fix:** compare `set(br)` directly against `small_ev` in both directions and exit nonzero on any difference. Optionally compare minimum moduli too. Say explicitly that the comparison validates **deduplicated cylinders**, not every parameter tuple or every family-class occurrence; `Rec` intentionally forgets those distinctions. Candidate and brute enumeration are independent, but they share `Rec.test`, CRT, and root helpers, so they are not wholly independent end-to-end implementations.

### m7. Restrict the auxiliary “union bounds cannot go further” assessment

Location: end of §3.4.

The displayed divergence of `sum_(sqrt(y)<l≤y) (log l)^B/l` is correct for fixed B > 0, but not B = 0, where the sum tends to log 2. More importantly, failure of a chosen upper envelope does not prove that every union-bound refinement fails. Qualify both the exponent and the scope; retain Assessment rather than a barrier theorem.

## Detailed mathematical audit: what passed

### A: all seven families, including parameters outside the modulus

The catch conditions agree with K11 Lemma M. The algebra for I-2 and I-4/II-1 is exact. For II-2, `z | a+c` and `Fz=4acd−1` give `4acdw=F(a+c)+w` with a,c,d unrestricted. There is **no** legitimate S-free restriction on those three parameters, and the code correctly imposes none. Likewise the I-4/II-1 branch does not require its e=z to be S-free, and the separate I-1 branch does not require f to be S-free. These were the most plausible reduction failure modes; they are handled correctly.

For I-3/II-3, reducing `zs=4A²Dx²y+1` and `Fz+1=4xyt` modulo 4xy gives `s ≡ −F (mod 4xy)`. Thus `u=(s+F)/(4xy)` is a positive integer, and substitution yields `4xtuy=A²DFx+Ft+u`. Recovery is unique at the parameter level. For I-1, `C(4a²d+1)−A²Dx·f=C+A²Dx`, so f divides the latter and gives the stated w and Q-equation. The products are indeed `αβ=NF` and `αβ=N²/D`, both ≤ N².

The script's candidates come from these two Q-shapes. The separate literal brute force does not feed the candidate list. S-part filters are family-specific in exactly the places requested for scrutiny.

### Q: identities, determining quantities, size cases, and exponent

The three identities `EP=α+4βY²W`, `ER=β+4αX²W`, and `PR=αβ+4Z²W` expand correctly. Each fixed single quantity or pair determines at most one solution for each selected divisor/ordered factorization.

In case A, `α/4 < YZW ≤ 2α/3` follows from the equation and `4XYW−1 ≥ 3XYW`. A1 gives `(PXYW)²=P²·(XY)(YW)(XW) ≤ (4α/3)²`. A2 gives `(PXZW)²=P²·(XZ)(ZW)(XW) < (4αβ/3)²`. These are products of **five factors counting P twice**, hence the 2/5 exponent is correct. The symmetric B cases cover every remaining solution, including the stated equality boundaries.

When a fixed pair product is ≤ T, each variable is ≤ T and terms such as `Y²W` and `Z²W` are ≤ T². Consequently the divisor arguments are bounded by the advertised `M=9(α+1)(β+1)(T+1)²`. There are two single-quantity types and six ordered-pair types, with at most `T(1+log T)` pairs per type. This justifies the coefficient 8. Since M is polynomial in αβ and the divisor bounds are uniform, the resulting `(αβ)^(2/5+o(1))` bound is genuine, including very unbalanced α and β. I found no missing case or hidden parameter dependence.

### E/G/K: counting and measure

There are at most τ₃(N) ordered three-slot splits per shape; overlap/gcd restrictions only reduce the number. The family/root factor `6+2^ω(N)` is correct. A cylinder has full unit-Haar mass `1/φ(N)`; if it meets B_S its B_S-relative mass is exactly `2^ω(N)/φ(N)`, with no factors from unused primes of S. Thus the o(1) can depend on N alone, not |S| or the prime pattern.

Pure events depend on only one coordinate, so the exact product law holds even though pure menus are not necessarily the full single-prime menus. The mixed tail follows by geometric summation with the stated hypotheses. Corollary K's product sum is valid uniformly in S: caught mass ≤ `exp(2 sum l^(−θ))−1`; at sum ≤ 1/5 the surviving mass is at least `2−exp(0.4)=0.5081753… > 1/2`. Choosing the k largest primes supplies the claimed sparse uncovered profiles. The y^(1/5−o(1)) notation is justified by the family of fixed-δ bounds (or a sufficiently slow diagonal choice). This does not yield a support-size theorem for individual certificates.

### P: parity

The Jacobi/reciprocity steps check out. In particular, the I-2 step `(−ac/z)=1` uses `a≡−c mod z` and gcd(ac,z)=1; `(−xy/f)=−1` uses `f≡−1 mod 4xy`. In I-4/II-1, `(xy/e)=1` follows from the same Jacobi fact and e≡3 mod4, while `(ABxy/e)=−1` follows from `Ax≡−By mod e`. For I-3, existence of a unit root gives `(−4c²d/f)=1`, hence `(D/f)=−1`. For II-3, the product of the two characters is `−(−d/e)²=−1`. S-free local factors and the 2-component are 1 at the specified profiles. If the alleged parity set were empty (or all exponents even), the identity itself precludes an event. No sign reversal was found.

### V/B: positive solutions and the valid bridge

All seven four-coordinate formulas satisfy their Type-I/II core identities. Positivity holds for every n≥1 in the class, including I-1's only non-obvious coordinate `te−a`; there is no hidden large-n threshold. Both denominator maps are correct.

The pointwise bridge is valid after removing the unnecessary `y<F(y)` inference. MF follows with the reciprocity/classical-case clarification above, and EXSET Cor 5.4 supplies the stated exceptional-set exponent. Lagarias–Odlyzko Theorem 1.1 explicitly assumes GRH for ζ_L and gives the displayed error involving `sqrt(y) log(Δ_L y^n_L)+log Δ_L`. For L=Q(√p), p≡1 mod4, the relative error at y=(log p)^A tends to zero for A>2. The textbook ψ bound indeed suffices with the weaker A>4 threshold. These implications are correct; the boundary classification is not.

## Computational replay and number audit

The following checks were re-run, not merely read from saved logs:

* `selftest 60 60`: **0 mismatches** against complete bounded brute force.
* `qcheck 120 120`: passed; maximum reported ratio **5.662113910164856**.
* Rebuilt `(11,13),(2,2)` and `(17,19),(2,2)` event lists into `/tmp`: **2509** and **4200** cylinders. All keys and minimum `(m,r)` representatives match the saved lists.
* Literal brute force at modulus **10^6** for all four boxes: **534, 1000, 840, 682** cylinders respectively; no missing or extra bounded cylinders.
* Audited all **26,209 saved rows** across the four two-prime lists for primitivity, level, off-S congruence, cylinder residues, and absence of an all-residue cylinder: passed. This is a row count across overlapping lists, not 26,209 distinct global events.
* Named representatives: `(1,1;6,7)` has `(m,r)=(21736,20521)`, i.e. −1215; `(1,2;2,2)` has `(12670944,12650497)`, i.e. −20447.
* Exact finite survivals reproduced: **15/4290**, **146/23256**, **98/47190**, with the reported pure products and Γ values.
* Independently rebuilt level-(1,1) at (401,409): **876** mixed NR×NR cylinders, mass **0.0214705882**, Γ **0.0145588235**, and Γ/(c1c2) **0.7105263158**. The other level-(1,1) rows were inspected, not all regenerated. Their rounded table values and stated 0.14–0.97 range agree with the saved log; the proposed asymptotic trend remains EVIDENCE only.
* `validity.py 300 3000 1`: **65,456** positive-integer exact-rational checks passed, with all seven families represented.
* Additional single-prime level-3 replay gives the strict survival decreases used in M3.

No numerical mismatch was found in the finite data. The central positive contribution is real: the two-shape reduction plus a uniform 2/5 Q-count closes the previously unbounded mixed-event count. The required corrections concern exact logical scope, boundary scales, asymptotic versus finite quantities, and executable certification—not a claimed resolution of ES.

## Second pass

Reviewed all of `d9c15ca19..3dca97428`, reading this report first. **MAJOR: none remaining. ES is OPEN. Provider/auth/quota errors: NONE.** M1–M3 are substantively repaired: B(iii)'s general criterion is sufficient (the additional relative-error term `(log y)²/√y` also tends to zero), B(iv)'s power-law/boundary distinction is correct, Cor K concerns thresholds rather than certificate supports, and the numerical survivals are explicitly finite-level. Cor G's finite-union upper-limit argument and fixed-prime constant resolve m1. Recovery, composite transfer, admissible-exponent/withdrawn weighted claims, failure exits, and the restricted union-bound assessment resolve the substance of m2–m4/m6–m7. Remaining issues:

* **MINOR — m5 only partially fixed (`scripts/z68_pc2_events.py:39–42`).** The cutoff still starts with floating division/exponentiation: `qsolve(10**400, 1)` immediately raises `OverflowError: integer division result too large for a float` (reproduced). The upward correction certifies the inequality when it terminates, but does not produce the claimed *smallest* T: at αβ = 10⁶⁰ its seed already exceeds the exact ceiling by 3,440,060,282. Use an entirely integer fifth-root/binary search; §7's assertion that m5 is fixed remains too strong. No replay-sized result is affected.
* **MINOR — inverted exceptional-set exponent (D3, line 37).** `X^{1/c+o(1)}` should be `X^{c+o(1)}`, as in B(iv) and the proposed FRONTIER text. For `1/2 < c < 1` the printed bound is worse than trivial, not a new bound. The limiting exponent follows from all fixed admissible A < 1/c; it does not require attaining A = 1/c.
* **MINOR — bridge proof precision (B(ii), B(v)).** MF counts q = 2 whereas PC counts only odd primes, so the counts do not literally agree for every p ≡ 1 mod 4. Explicitly dispose of p ≡ 5 mod 8 by classical ES, leaving (2/p) = 1 for exceptional primes. The new `F(y) > cy` argument needs fixed `0 < c < 1/2 + η` to supply enough NR primes. Also F was not assumed monotone/invertible: replace `y < F^{−1}(p)` by the actual conditions `F(y) < p` and hence `y < p/c`.
* **MINOR — Cor K rounding.** The constructed profile has exactly `floor((1/5)(y/2)^θ)` NR coordinates. The displayed failure statement is therefore for thresholds at most that floor, unless k′ is explicitly restricted to integers. The asymptotic threshold conclusion is unaffected.
* **MINOR — residual notation/scope polish.** §3.5's last-column numerator should be `s^{(K₁,K₂)}`, not bare s (defined as infinite-level); the survive script's introductory input description likewise still says `s^U` before its corrected finite-level definition. The §5 bottom line's “above that it is open” should explicitly preserve the logarithmic boundary qualification: `√y/(log y)²` lies above every fixed power-separated regime but still satisfies B(iii). The main verdict and proposed FRONTIER text otherwise have the appropriate survival-ratio and Assessment scope.

Replay: `selftest 60 60`, all four modulus-10⁶ comparisons (including minimum moduli), and all three §3.5 survivals passed. Injected selftest mismatch and compare missing/extra/above-bound/minimum-modulus faults all exited 1; equality exited 0. `git diff --check` passed. All commands used timeout ≤ 1800 seconds and `ulimit -v 6000000`; only this report was edited.
