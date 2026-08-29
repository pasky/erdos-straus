# Wave-15 unit reports

## Unit A15 (§43 general-m)

# UNIT A15 report

- Added §43, “General numerators: the multiplier identity is m-uniform and the exceptional-set machinery transfers.”
- Lemma 43.1 (proved): the multiplier identity holds for every integer numerator `m >= 3`.
- Lemma 43.2 (proved): exact multiplier-thinning factors are `eta_1(m)=prod p/(p+1)` and `eta_2(m)=prod p^2/(p^2+p-1)`.
- Lemma 43.3 (proved): the §16 class mass transfers with the explicit factor `eta_1(m)/phi(m)`.
- Theorem 43.4: complete internal Layer-1 proof, externally CLAIMED/PROVISIONAL; saving coefficient `(eta_1(m)/phi(m))^(1/3)`.
- Layer-1 uniformity: primes for `m <= (log N)^(2-epsilon)`, all denominators for `m <= (log N)^(1-epsilon)` via the divisor/semigroup transfer.
- Lemma 43.5 (proved): c-free coupling, deduplication, distinct large-prime coordinates, and CRT density are unchanged.
- Lemma 43.6 gives the general-m §39 mass profile and the exact `eta_2(m)/phi(m)` atom mass.
- Provisional Theorem 43.7 threads `muv` through the pruned cubic prime slice; it inherits Theorem 34.8.
- Theorem 43.8 is CLAIMED/PROVISIONAL: `E_m(N) << N exp(-c eta_1(m)(log N)^(3/4)/phi(m))`.
- Layer 2 is stated uniformly and nontrivially for `m <= (log N)^(3/4-epsilon)`.
- Failure log 43.9 declines an unaudited m-dependent Bonferroni retuning and any short per-residue equidistribution claim.
- PW Theorem 1.3 is transcribed as (43.32); the exact crossover is (43.34), reducing to `phi(m) <= (log N)^(1/8)` when fixed local factors are suppressed.
- Added `verify.py (ap)`: 364 exact identity checks, an `m=5` atom census, and informational local-factor numerics.
- Full `uv run --with sympy,numpy,scipy python verify.py` passes; AST, whitespace, and control-byte checks pass.


## Unit C15 (§44 slice conspiracies)

# UNIT C15 report

## Outcome

Added §44, “Slice conspiracies: joint vanishing structure of the ray-character mass,” and verifier block `(aq)`.

- **Exact vanishing theorem:** the `(c,k)` slice vanishes exactly when the bounded exponent box of the factorization of `p²+4ck²` misses the grade `−p mod 4ck`. The equivalent character coefficient, quadratic-root progression union, and finite-set conspiracy locus are explicit in (44.2)–(44.7).
- **New proved obstruction:** if the squarefree core of `c` is `1, 2, 3`, or `6`, every such slice vanishes for every hard prime. This extends the `c=1` Gaussian obstruction; it forces 80 of the 111 slices with `ck≤30` to zero identically.
- **Structured-prime result:** every prime `p≡97 (mod 120)` has a positive `(5,1)` slice, witnessed by `D=3`.
- **Moving-divisor obstruction:** joint vanishing of `(5,1)` and `(7,1)` is not determined by their natural modulus 840: `193≡1033 (mod 840)`, but both slices vanish at 193 while `(5,1)` survives at 1033 through the moving divisor 67.
- **GRH audit:** the exact `k=1` principal mass is between logarithmic and subpower size. Standard GRH does not estimate the selected divisors of each moving `pa+1`; even an additional idealized square-root cancellation across the `O(p)` fibres leaves a `p^(1/2+o(1))` error against a `p^o(1)` principal term.

## Exact census

For all 385 primes `p≡1 (mod 24)`, `p<30000`, verifier block `(aq)` checks all 111 slices `ck≤30` by exact factor-grade dynamic programming and literal divisor enumeration.

- Vanishing depths range from 99 to 111.
- Fifteen primes vanish on all 111 slices: `2521, 9601, 12289, 13729, 15289, 18481, 19009, 20089, 21121, 21169, 21841, 27361, 27481, 28921, 29569`.
- Thus 2521’s known `k=1` zero is accompanied by vanishing of every slice in this box.
- The full histogram and cutoff table are recorded in (44.16)–(44.18) and hard-asserted in `verify.py`.

## Failure log

No finite small-box positivity theorem survives: all slices through `ck≤4` vanish identically, 161 primes still vanish through `ck≤10`, and 15 still vanish through `ck≤30` in the stated range. The exact conspiracy locus remains an infinite union/complement involving actual moving divisors, so it yields no new effective all-large-prime or exceptional-set bound. No claim is made about Erdős–Straus witness nonexistence.

## Files

- `notes.md`: §44 plus repair of one pre-existing eaten-`\r` artifact in (31.23).
- `verify.py`: exact memory-bounded block `(aq)`; `(ap)` remains reserved for the parallel unit.
- `UNIT_REPORT.md`: this report.

## Validation

- `python3 -c "import ast; ast.parse(open('verify.py').read())"`
- `uv run --with sympy,numpy,scipy python verify.py` — all checks passed in 78.93 seconds.
- `notes.md` control-byte count: zero; eaten-`\\r` pattern count: zero.

## Unit D15 (§45 endpoint vs Kloosterman fractions)

# UNIT D15 report

## Outcome

The Kloosterman-fraction technology does **not** close (40.19).  Section 45 gives an exact endpoint matrix

\[
G_{4c^2s,p}=\sum_q \kappa(pq)/q
\]

with every roughness, cofactor, canonical, and retention condition carried.  Its full Parseval norm is exactly \(\mathcal V_X^{\rm end}\).  The key audit result is that DFI/BC permit arbitrary separate one-variable sequences, not the joint coefficient matrix \(G_{m,p}\).  Exact singular-value decomposition makes DFI applicable but introduces a nuclear norm; summing the complete \(h\)-range then overwhelms the scalar saving.

The cofactor orientation also fails exactly: reciprocity changes the modulus from \(p\) to \(m=4c^2s\), while the valid lift has modulus \(pq\).  It never produces modulus \(q\) in general.

## Proved additions

- `notes.md` §45: exact reduction Lemma 45.1, coefficient \(\ell^1/\ell^2\) audit, exact DFI and BC quantifiers and scale windows, DFI nuclear-norm Lemma 45.2, strongest assembled partial Proposition 45.3, and three exact failure logs.
- `verify.py (ar)`: independently reconstructs the toy endpoint systems, forms the joint matrix, checks both reciprocity identities and exact Parseval equality, and reports exact rational coefficient norms.
- `sources/bettin-chandee-1502.00769.pdf`: arXiv PDF archived with SHA-256 provenance in `sources/README.md`.

A legitimate full open DFI copy was not found.  Springer is paywalled and the ProQuest open result exposes only a one-page preview, so no incomplete PDF was committed as the paper.

## Remaining status

The strongest closed family remains fixed-polylogarithmic primes plus at most \(O(L^{3/2}/\log L)\) prescribed fixed-\(s\) fibres.  The moving-\(s\) range \(L^B<p\le X/z\), (40.19), and (37.27) remain open.  Even closing them would leave (40.28), (37.19), (33.16), and the internal refutation of \(H_{\rm PF}'\) open; this arc does not settle the Erdős–Straus conjecture.

## Verification

- `ast.parse(verify.py)`: pass.
- Control-byte scan of `notes.md`: zero.
- `uv run --with sympy,numpy,scipy python verify.py`: pass, including block (ar).

## Unit B15 (Theorem 34.8 independent re-derivation)

# UNIT B15 report

Verdict: **CONFIRMED-AFTER-REPAIRS** (internal review only).

- Independently re-derived Theorem 34.8 and the Lemma 34.7 incidence moment.
- Checked Shiu's 1980 source hypotheses directly; the fixed-relative boxes and modulus \(k<K<U^{1/10}\) are safely admissible for both functions used.
- Confirmed the power-sized box error is relative \(O(K^2/H)=O(K^{-8})\), with \(z>K^{20}\) exactly requiring \(\kappa<1/240\) at the lowest block.
- Confirmed pruning loses \(o((\log z)^2h(\mathcal J))\) uniformly; \(1\in\mathcal J\) supplies \(h(\mathcal J)\ge1\).
- Confirmed \(W_{\rm good}(q)\le(\log X)^{D\log2+4}\), BV at level \(x^{1/3}\), and same-prime class distinctness.
- Confirmed both (34.18) and (34.19).
- Confirmed §39's full inheritance chain for data-dependent \(\mathcal J_c\), canonical boxes, and \(h(\mathcal J_c)\gg\log K\) when \(Z(c)\le\eta\).
- Found no mathematical break.
- Added minimal wave-15 repairs to §34 for source-level Shiu conditions and compressed BV/deduplication bookkeeping.
- Added §34.5 attestation and the full audit in `reviews/wave15-thm34.8-rederivation.md`.

The CLAIMED/PROVISIONAL register remains unchanged; this is not external review.
