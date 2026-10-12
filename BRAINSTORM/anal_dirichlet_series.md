# anal_dirichlet_series — Dirichlet series of f_I, f_II and of the sterile indicator (O151, angle (a))

Labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010. EXF = EXACT_FORMULA.md (O131), read first;
nothing below repeats its identities. ES is not solved here.

## 1. Idea

Attach to the solution counts the Dirichlet series

* `D_I(s) = Σ_n f_I(n) n^{−s}`, `D_II(s) = Σ_n f_II(n) n^{−s}` (all n, or restricted to primes: `D_•^P`);
* the **sterile series** `Z(s) = Σ_{n : f(n)=0} n^{−s}` and its prime part `P_E(s) = Σ_{p sterile} p^{−s}`,
  where "sterile" = `f_I(p) + f_II(p) = 0` (for p prime this is ¬ES(p), since every solution for a prime is Type I/II).

Hope: analytic continuation / poles / a functional equation of `D_•`, plus a Tauberian or positivity theorem
(Landau: a Dirichlet series with non-negative coefficients is singular at the real point of its abscissa),
would force `P_E` to be a Dirichlet polynomial, i.e. finitely many sterile primes.
Sub-idea (a′): at **fixed p**, the regularised level series `Λ_p(s) = Σ_{c,d} A_{c,d}(p)(cd)^{−s}`
(A as in EXF §3.1), entire, with `Λ_p(0) = 2f_II(p) − diag`; expand by characters and read `Λ_p(0)` as a sum of
"finite parts" at s = 0 of pieces that individually have poles.

## 2. Literature anchor

* Landau's theorem on non-negative coefficients: standard (Montgomery–Vaughan, *Multiplicative Number Theory I*,
  Thm 1.7) — from memory, unverified page reference.
* ET Thm 1.7: `Σ_{n≤N} f_•(n) ≍ N log³N`; for primes `N log²N ≪ Σ_{p≤N} f_•(p) ≪ N log²N log log N`; the
  campaign removed the log log for Type I ((D)32, internal). So `D_•` has abscissa 1 and, if it has a pole there,
  it is of order 4 (all n) / 3 (primes).
* First-order structure of `D_II` (elementary): with `n = 4abd − e`, `e | a+b`, expand
  `(4abd − e)^{−s} = (4abd)^{−s}(1 + O(se/abd))`; the main piece is `4^{−s} ζ(s) Σ_{a,b} τ*(a+b)(ab)^{−s}`
  (τ* = divisor count with the ET gcd filters), a Tornheim/shifted-convolution double series. Continuation of
  such series past Re s = 1 is classical in spirit (Estermann; Motohashi; spectral theory of shifted
  convolutions) — from memory, not verified for this exact series. Height-zeta technology for **integral**
  points (Chambert-Loir–Tschinkel, partial equivariant compactifications, Duke 2012) does not literally apply:
  n is a rational function on the ET variety, not a height. I found no paper studying `D_•` (search not done
  online; Assessment).

## 3. Barrier screen

**Prop A.1 (exact reformulation; PROVED, elementary).** Let E be the set of sterile primes. Then E is finite
⟺ `P_E` continues analytically along the real half-line from (1,∞) to a neighbourhood of s = 0.
*Proof.* Finite ⇒ entire. If E is infinite, `P_E(σ)` diverges at σ = 0, so its abscissa `σ_E ∈ [0,1]`, and by
Landau `P_E` is singular at `σ_E`. ∎
So ES-for-large-p is literally a statement about **Re s ≤ 0**. Known: `σ_E ≤ 1`, nothing better: the best
exceptional bound `E(N) ≪ N exp(−c(log N)^{3/4})` ((B)11) is `N^{1−o(1)}`, and `σ_E < 1` ⟺ `E(N) ≪ N^{1−δ}`
(a power-saving exceptional set), which no ES result has. The CRT-admissible large-sieve cap
(EXCEPTIONAL_LARGESIEVE Thm 3.1: savings `≤ C(log N)^{3/4}` for every forced-class mixture at level N^{O(1)})
excludes even `σ_E < 1` by those methods.

**Prop A.2 (invisibility of thin zero sets; PROVED, elementary).** Let S be any set of primes of convergence
exponent 0 (`Σ_{p∈S} p^{−ε} < ∞` ∀ε > 0, e.g. one prime in each `[2^{2^k}, 2^{2^{k+1}})`), and let g agree
with f off S, with `0 ≤ g(p) ≤ p^{o(1)}` on S (e.g. g = 0 on S). Then `D_g − D_f` is holomorphic on Re s > 0.
Hence **every** statement about `D_f` on Re s > 0 (continuation, location and order of poles, residues,
growth on vertical lines, a functional equation relating regions inside Re s > 0) is equally true for a
function vanishing on an infinite set of primes. ∎
Consequence: a Dirichlet-series route must control `D_f^P` (or `P_E`) on Re s ≤ 0, i.e. pointwise information
(Perron at σ < 0 recovers individual coefficients). There is no known mechanism for `D_•` there; even its
continuation to Re s > 1/2 is unproved (and for the all-n series it **must** see the odd squares, below).

**B1–B6, T1/T7.**
* B6/T7 (decisive). Every *linear* datum of `D_•` (values, residues, contour integrals at Re s > 0) is an
  average of f over n with weights `n^{−s}`; Prop A.2 makes the average leak exact. FAIL.
* Non-linear version. `1_{f(n)=0} = Σ_k (−1)^k binom(f(n),k)`, and `Σ_n binom(f(n),k) n^{−s}` is the series of the
  k-fold fibre product of solution sets (k-tuples of solutions of the same n). Truncating at depth r is exactly the
  Bonferroni/factorial-moment assembly (B)7/(B)11; CEILINGS_UNIFIED shows that route is capped at saving
  `≍ λ^{3/4}` (λ = level), i.e. again `σ_E ≤ 1` only. COLLAPSES to the 3/4 ceiling (B3/B4 form).
* B5/T1. For the all-n series, `Z(s) ⊇ Σ_{m odd} m^{−2s} = (1 − 2^{−2s})ζ(2s)` (ET Prop 1.6), so `Z` has a pole at
  s = 1/2 and "the zero set is finite" is false for all-n Dirichlet arguments: the failing step is any claim of
  holomorphy of `Z` at s = 1/2 (for f_II alone EXF Prop 2.1 even gives all squares). Prime-restricted series pass
  T1 vacuously, but then the input is a prime-values statement about a height-type series — the same
  restriction-to-primes that every averaged ES result already performs, with no pointwise content.
* B2. Sub-idea (a′): `Λ_p(s)` is a finite sum; its character pieces `(1/φ(4cd))Σ_χ χ(−1)σ_χ(4c²dp+1)(cd)^{−s}`
  diverge at s = 0 individually (EXF §3.4: the principal piece grows like log²C), so `Λ_p(0)` is a sum of finite
  parts whose poles cancel. Positivity of a sum of finite parts is a signed-cancellation statement: hatch H-E,
  with the EXF negative result (no structurally positive part). Also the finite part depends on the regulariser
  `(cd)^{−s}` vs any other `w(c,d)^{−s}`, so no canonical "main term" exists (Assessment). COLLAPSES to B2/H-E.
* B3: not reached (no certificate is produced).

## 4. Experiments

None needed for the PROVED items. (The data in `anal_moments_structured.md` §4 show that even the *distribution*
of f(p) at accessible p is dominated by factorisations of a few shifted integers, which `D_•` averages out.)

## 5. Viability Assessment

**COLLAPSES to B6/T7** (linear functionals of D; Prop A.2 makes the leak exact) and, for the inclusion–exclusion
version, **to the 3/4 Bonferroni ceiling** (B3/B4); sub-idea (a′) **collapses to B2/H-E**.
By-products (PROVED, elementary, modest): Prop A.1 (ES-for-large-p ⟺ analytic continuation of the sterile prime
series to s = 0; no known result even gives abscissa < 1, which would be a power-saving exceptional set),
Prop A.2 (Dirichlet-series data on Re s > 0 cannot see a zero set of convergence exponent 0).
Open side question (UNCLEAR, low value for ES): does `D_II(s)` continue to Re s > 1/2, with the odd-square
vanishing visible as a cancellation in the ζ(2s)-type part? It would give an asymptotic for Σ_{n≤N} f_II(n) with a
power-saving error, which is an average and irrelevant to pointwise ES.
