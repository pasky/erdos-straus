# Hostile referee report (v2): `paper/sieve-limits-note.tex`

Subject: v2 of the sieve-limits note, branch `side-agent/sieve-paper-v2`
(commit `d8ccdf1`), changelog `reviews/agent-reports/SIEVE_PAPER_V2.md`.
Sources checked (all on `main`): `EXCEPTIONAL_KARY.md` (Thms 2.5, 4.1, 4.5,
§§1–5) with `reviews/exceptional-kary-review.md` and `-review-2.md`;
`EXCEPTIONAL_TWIN.md` (§4: Prop 4.1, Lemma 4.2, Cor 4.3), `EXCEPTIONAL_TWIN2.md`
(Setting 3.0, Lemma 2.1), `EXCEPTIONAL_TWIN4.md` (Lemma 2.3, Thm 7.1, §9,
Thm 10.4, §§11–12); `EXCEPTIONAL_NONCRT.md` (§§2–4, 8); the v1 report
`reviews/sieve-limits-note-review.md` (D1–D14).

Scope: the sections new or rewritten in v2 (abstract, §1, §§6–9, §11 additions,
§§12–14, bibliography). §§2–5 and §10 are unchanged from v1 (diff checked) and
were refereed in v1.

## 0. Compilation

`pdflatex` ×3 in a scratch directory: 33 pages; no errors, no undefined
references or citations, no overfull boxes. Three underfull boxes (lines
1611–1617, 2308–2310, 2352–2354), harmless. The changelog's claim is
confirmed.

## 1. §8, the weighted k-ary comparison theorem (KARY §§1–3)

**Faithfulness.** Setting, plain activation rule, Lemma 8.x avoidance/inflation
(= KARY 2.1), locality (= 2.2), extrapolation (= 2.3 + (3.1)), thinned law
(= 2.4), Thm kcomp (= 2.5, including `Φ ≥ 0` via `B ≥ 1`, review-2 E1),
Cor kmean (= 2.6, same `t = d/(m̄+4d)`, same constants `C₀ = 4e^{4.31}`),
Remark kweighted (= Remark 2.8 and §5). The phantom rule and the cruder bound
(2.1) are omitted; neither is used. Statuses match: weighted form PROVED,
unweighted Conj 6.4 OPEN, `kary_check.py` EVIDENCE. The renaming
`ν → ϖ`, `M → m`, `R → J`, `n → z` avoids a clash with the majorant `ν`.

**Proofs re-derived.**
* Lemma kavoid (2): `P(y_ℓ=a | past) = ϖ(a)1{a∉F}(1 + p/(1−p)) = ϖ(a)1{a∉F}/(1−p)`. Correct.
* Lemma kextrap. Symmetrisation: the `Sym(z)`-average of `ρ^S` is
  `C(K,|S|)/C(z,|S|)`, so the average is `Q(K)` with `deg Q ≤ d`, `Q ≥ 0` on
  `{0..z}`, `Q(z) = g(1)`, `E Q(K) = E_{Bern(t)} g`. Interpolation
  `Q(z) = Σ ℓ_y(z)Q(y) ≤ max(|ℓ_y(z)|/ψ(y))·Σψ(y)Q(y)`. `B ≥ 1` from
  `Σ ℓ_y(z) = 1 ≥ Σ ψ(y)`. Correct.
  I re-derived (eq:kB) = KARY (3.1) in all three cases:
  - *(i) `z ≤ d`*: `Y = {0..z}`, `B ≤ t^{−z} ≤ t^{−d}`.
  - *(ii) `z > d`, `zt ≤ 2d`*: `Y = {0..d}`, `|ℓ_i(z)| ≤ z^d/(i!(d−i)!)`,
    `C(z,i) ≥ z^i/(i!e^i)`, `(1−t)^z ≥ e^{−1.151zt} ≥ e^{−2.31d}`
    (`−log(3/4)/(1/4) = 1.1507`), so the ratio is
    `≤ z^{d−i}e^{i}e^{2.31d}/((d−i)!t^i)`. Then `z ≤ 2d/t` and
    `(2d)^k/k! ≤ (2ed/k)^k ≤ (2e)^d` for `k ≤ d` (`x ↦ x log(2ed/x)` increases
    on `(0,2d]`) give `≤ (2e^{4.31}/t)^d`.
  - *(iii) `m₀ = zt > 2d`*: `h = ⌊√(m₀/d)⌋ ≥ ½√(m₀/d)`, nodes
    `⌈m₀⌉ − ⌊dh/2⌋ + ih`. Deviations: below by at most `dh/2 ≤ ½√(dm₀)
    < m₀/(2√2)`, above by at most `dh/2 + 3/2`. So the nodes lie in
    `[0.646m₀, 1.354m₀+1.5] ⊆ [1, z−1]` (`z ≥ 4m₀`, `m₀ > 2`) and
    `8y_i ≤ 22m₀`. Exponent `(4/3)(y−m₀)²/m₀ ≤ d/3 + 2√(d/m₀) + 3/m₀
    < d/3 + 2.92`. `|ℓ_i(z)| ≤ 2^d z^d/(h^d d!) ≤ (2ez/(dh))^d ≤
    (4e√(z/(td)))^d`. Total
    `d log(4e^{4/3}√(z/(td))) + 2.92 + ½log(22m₀)`, below (eq:kB).
  So (eq:kB) is **correct**; but the paper does not show this (D3).
* Lemma kthin: `P_ρ(y^ρ = x | ω) ≤ Π φ_ℓ` (at a replaced ℓ the two events are
  disjoint); `E[φ_ℓ | past] = ϖ(x_ℓ)(1 + 1{light} t p_ℓ 1{x_ℓ∉F}/(1−p_ℓ)) ≤
  ϖ(x_ℓ)D_ℓ` with `D_ℓ` predictable; supermartingale; `Π D_ℓ ≤ e^{(4/3)tm}`.
  Correct. (The source's remark "if `ϖ(x) = 0` both sides vanish" is dropped;
  harmless, the ratio `φ_ℓ/ϖ_ℓ(x_ℓ)` needs it — nit.)
* Thm kcomp and Cor kmean: re-derived. `E z = E m` (each light ℓ is replaced
  with conditional probability `p_ℓ`); Jensen on the concave
  `z ↦ d log(C₁'(1/t + √(z/(td)))) + ½log(22tz+22)`; with the stated `t`,
  `√(E z/(td)) ≤ √(m̄(m̄+4d))/d ≤ (m̄+4d)/d`, `C₀ = 2C₁'`. Correct.
* Remark kweighted example: `E M = εμ = 1`, `E_σ f ≥ εμ² = μ`,
  `E_ϖ f = ε·m·(3/16) = 3/4`; ratio `4μ/3`. Correct; `f` is 3-local.

**Defects here:** D3, D4 (below).

## 2. §9, the main theorem (KARY §4)

**Faithfulness.** Thm wseq = KARY Thm 4.1 (setting, (S_w), `Φ_j ≥ 0`, leak
`≤ 1/2`, conclusion with `log 2 + 2ΣEΦ`). The sequential step is KARY's
(plain rule, `ϖ = U`, `δ_ℓ = ℓ^{−1/2}`, `t_j(h)` fixed before the block).
Lemma kmoments = KARY 4.2(1), 4.2′ (incl. `K(W,B)`, block
`{s < log ℓ ≤ 2s}`, `s ≥ log W`), 4.2(3) (the `(2+B)²` absorbed into
`C(ε,B)`), 4.3. Thm karycap = KARY Thm 4.5 with every hypothesis: B fixed,
`W = W₀(B)`, `λ ≥ λ₀(B)`, ℛ(M)-classes with `M ≤ P(M)^{1+B}` of any shape,
plus W-smooth ℛ(M)-classes, base `R_W`, all primes `> W` charged; constants
untracked. Review-2 E2 (the index I) is incorporated. The "superseded" list
(Conj 6.4/K2/Prop 6.5's `log λ`, Thm resolved's residual) matches KARY §4.3
and review-2 E3. Thm main keeps cases (i) and (ii) separate and states that
mixed families are not covered, as in KARY "Still not covered" and
DISCOVERIES (D)17. No strengthening found.

**Thm 4.5 assembly, re-derived as presented.**
* Blocks: singletons on `(W, e^{s₁}]`, dyadic `V_i` for `2^i s₁ < λ/2`
  (cover `(e^{s₁}, e^{λ/2}]` exactly), top block `(e^{λ/2}, e^λ]`, singletons
  above `e^λ` (f does not see them: cost 0). Every class is decided at its
  top prime (other primes earlier or in `Q₀`). ✓
* Leak: union over heavy tops (light tops are avoided, Lemma kavoid(1);
  heavy `y_ℓ = c_ℓ ~ U`), Markov `E[p1{p>δ}] ≤ ℓ^{1/2}E p²`, second moment
  `ℓ^{−2+1/4}`: `Σ_{ℓ>W} ℓ^{−5/4} ≪ W^{−1/4}`. ✓
* Singletons: TW Prop 4.1 (step cost `−log(1−p) ≤ (4/3)p`, mass
  `≤ K'((1+B)s₁)³`, factor 2 included) — checked in TW §4.2. Top block:
  TW Lemma 4.2/Cor 4.3, `2log(1+3e^{−λ/4})`, factor 2 included — checked
  in TW §4.3 (one prime per term since two primes `> e^{λ/2}` exceed λ). ✓
* `V_i`: `s = 2^i s₁ < λ/2` so `d_i = ⌊λ/s⌋ ≥ λ/(2s) ≥ 1`; Cor kmean per h,
  Jensen over h (concavity of `m ↦ log(C₀(m+4d)/d)`); Lemma kmoments(2):
  `E m_{V_i} ≤ K(2(1+B)s)³ = K₁s³`; `E m/d ≤ 2K₁s⁴/λ = 2K₁16^i`;
  `d_i ≤ λ^{3/4}2^{−i}`; `log 16 = 2.773 ≤ 2.78`; `I ≪ log λ` blocks give the
  `O(log²λ)`. ✓ The bound is `≪_B λ^{3/4}`. ✓
* Lemma kmoments(2) proof: Shiu range needs `Σ h(e)/φ(e) < ∞` (`h(p) ≤ 2`
  for the finitely many `p ≤ W`, `h(ℓ) ≤ 2ℓ^{−1/2}` above), tail needs
  `Σ h(e)e^{−3/4} < ∞` (Euler factors `1 + O(p^{−5/4})`). ✓
* Thm main: Cor budgetlevel at level `(A+2)log N` with Thm karycap at
  `λ = (A+2)log N ≥ λ₀(B)`; a majorant of level `≤ λ` has level λ. ✓ modulo D2.
* Remark after Thm main: "case (i) with `B = C`" ✓ (`P(M) ≥ M^{1/(1+C)}` ⇔
  `M ≤ P(M)^{1+C}`); the twin moduli of Lemma balancedsupply have
  `M ≤ P(M)^{(2+4η)/(1+η/2)} ≤ P(M)^{2+3η}`, so `B = 2` covers them ✓.

**Lemma 2.9 hypotheses.** KARY lists them as: slice primes `≤ N^{O(1)}`,
`Σ|a_i| < N`, the family hypothesis at every λ in the range. The paper has
(A3), (A2), and Cor budgetlevel needs the cap only at `(A+2)log N`. ✓

**Defects here:** D1, D2, D4 (below).

## 3. Defects found in §§8–9

* **D1 (MINOR, hypotheses: finiteness).** Thm karycap, Lemma kmoments and
  Results item 1 say "every family". The proof needs a **finite** family:
  `Q₀` is a common multiple of the W-smooth parts of all moduli, and the
  process of Thm wseq runs over finitely many blocks. The infinite version
  is not implied: for an infinite family the integer avoider set can be
  much smaller than its profinite closure, so a periodic `ν` may be `< 1`
  on residue classes that contain no integer avoider; the argument then
  says nothing. (Standard example of the phenomenon: one class per integer
  with huge prime moduli covers ℤ with no finite subcover.) KARY has the
  same implicit assumption, so this is a clarity fix, not a faithfulness
  error. Thm main is safe: (A3) and `M ≤ P(M)^{1+B}` give
  `M ≤ N^{A(1+B)}`, finitely many moduli. *Fix:* "every finite family" in
  Thm karycap and Results item 1, and one sentence in Thm main (ii)
  noting that (A3) and B make the family finite. The W-smooth classes may
  be infinite, but `R_W` avoids them whatever `Q₀` is (Lemma QR(1)).

* **D2 (MINOR, proof gap in Thm main).** The level conventions do not
  match. Thm karycap charges **all** primes `> W`, and Cor dominant all
  primes `> w₀`. Lemma budget and Cor budgetlevel truncate only the
  *slice* primes, and (A3) bounds only the family primes. A majorant may
  use primes `> N^A` that divide no modulus. Lemma budget leaves them
  untouched, so the truncated `ν'` need not have level
  `≤ (A+2)log N` in Thm karycap's sense. *Fix (one sentence):* first
  replace `ν` by its conditional expectation over the CRT coordinates of
  the primes that divide no modulus and not `Q₀`. The avoider set is a
  union of full fibres in those coordinates, so the result is still
  `≥ 0`, `≥ 1` on `A`, has the same mean and does not increase
  `Σ|a_i|`. After that every remaining prime is a family prime, and (A3)
  applies. The same sentence repairs case (i). Case (i) dates from v1,
  but v2's Thm main uses both cases.

* **D3 (MINOR, sketch marking: the key new lemma).** Lemma kextrap is
  labelled [proved] and has a full `proof` environment. Its bound
  (eq:kB), which is all that Cor kmean and Thm karycap use, is only
  sketched ("use three node sets [KA §3]"). The changelog's point 1
  concedes this. The lemma is advertised in the abstract as the key new
  tool, so for a journal the computation should be printed. It is
  correct: re-derived in §1 above, case (ii) `≤ (2e^{4.31}/t)^d`, case
  (iii) `d log(4e^{4/3}√(z/(td))) + 2.92 + ½log(22zt)`. It takes about 15
  lines and needs only Lemma binom, which is already in the paper. Two
  alternatives: print it, or mark the (eq:kB) part "Proof sketch;
  details [KA §3]". Also make the case conditions disjoint: case (ii) is
  "`z > d` and `zt ≤ 2d`".

* **D4 (MINOR, notation / undefined symbol).**
  - `K'` in the proof of Thm karycap ("cost `≤ (8/3)K'(1+B)³λ^{3/4}`") is
    never defined. It is TW Prop 4.1's `K'(W,B)`, the constant in
    `Σ_{W<ℓ≤e^{s₁}} E p_ℓ ≤ K'((1+B)s₁)³`, and could also be taken from
    Lemma kmoments(2).
  - `m` clashes inside one sentence of Remark kweighted:
    "coordinates `Z_1,…,Z_m`, `μ = m/4`, … `E m(ω) = 1`". Rename the
    number of coordinates (e.g. `k`).
  - `J` is used for the replaced set `J(ω)` (§8), the number of blocks
    (Thm wseq) and the large-sieve sum (Lemma roughBT proof). Suggest
    `Rep(ω)` or `𝒥` for the replaced set.

## 4. Abstract, §1, §§6–7 (reframing)

**Faithfulness.** The abstract and Results item 1 state Thm karycap with
`B` fixed, ℛ(M) only, and the architecture class with "the admissible set
specified there". Case A is "modulo" Elsholtz–Tao, and the twin, prime-power
and comparable-scale shapes are listed. "No power of `log log N` can be
gained" is the last sentence of Thm main. §6 is now only a pointer
paragraph. §7 calls Thms gapped/resolved special cases of Thm karycap
(true: their families satisfy `M ≤ P(M)^{1+B}`), and the closing paragraph
of §7 matches TW §4 and KARY §4.3. The Λ² scope in the abstract
("fixed number of prime factors above `(log X)^8`, no condition relating M
to P(M), level `O(log X)`") matches TW4 Thm 10.4. The v1 defects D1, D4, D5
and D11 (scope drops) have not regressed.

* **D5 (MINOR, provenance and labels).**
  (a) §1 says that every [proved] result outside §2 "appears in one of
  eight internal working documents". Two v2 statements do not:
  Remark L2vsmain (the changelog calls it "my observation") and the
  case-(ii) assembly of Thm main. Both are correct. For L2vsmain I checked
  that TW2 Setting 3.0 charges all primes, so `g²` (with `g ∈ V_{λ/2}`)
  is `≥ 0` of level λ; that it is `≥ 1` on avoiders ⊇ avoiders in `R_W`;
  and that the family is ℛ(M) with `M ≤ P(M)^{1+B}`, `M ≤ X`. Its
  citation, TW4 §11, is a coordination note labelled SKETCH/Assessment,
  written while KARY was "under review". *Fix:* label Remark L2vsmain
  [proved] (observation of this note, one-line proof given). Cite TW4 §11
  as "anticipated in", not as the source. Amend the §1 sentence to
  "…or is assembled here from such results".
  (b) Results item 1 says "every nonnegative majorant of level λ **of the
  avoider set**", while Thm karycap is stated for the avoider set **in
  `R_W`** and `λ ≥ λ₀(B)`. Item 1 does follow, since a majorant of `A` is
  ≥ 1 on `A ∩ R_W`, but the paper never says this, so a reader comparing
  item 1 with Thm karycap sees a stronger claim. *Fix:* either add that
  line after Thm karycap or restate item 1 with "in `R_W`" and
  `λ ≥ λ₀(B)`. Abstract and item 1 write `O_B`, but the constant depends
  on A as well (Thm main: "depending on A, B"); write `O_{A,B}` (nit).

## 5. §11 additions (TW4)

**Faithfulness.** Lemma roughBT = TW4 Lemma 2.3: same hypotheses
(`x ≥ q2^{s+1}`, `(b,q) = 1`), same constant `3(s+1)ΣH^i/(φ(q)log Y)`.
I re-derived the proof: `R = dn` with `Ω(d) ≤ s−1`; then `d ≤ Z^{s−1}` gives
`x/(dq) ≥ Z²`, the large sieve with `ω(p) = 1`, and van Lint–Richert gives
`J ≥ (φ(q)/q)log Z`. Correct. Thm rprime = TW4 Thm 7.1, Prop 9.1 and
Lemma 9.2/Cor 9.3 in the text, and Thm noB = TW4 Thm 10.4: hypotheses
(fixed r, `M ≤ X`, `w₂ = (log X)^8`, `λ ≤ A₀L`, the `330 log L` add-on with
the extra fibre-law event) and bounds are reproduced exactly. The proof
sketches are marked "Proof sketch" and cite precisely. The (D)/(H)/(G) split
and `B = 33r−1` match TW4 §10. The TW4 §11 B-removal is marked SKETCH and
not claimed (§14), as it should be.

* **D6 (MINOR, label).** Two passages state as fact that the middle range
  `ε log L/log log L < r < 330 log L` "carries most of the
  `α^{−3}`-weighted mass": the end of §11 and §14 "Many large primes".
  TW4 §9.3 is headed "(Assessment)", and the claim rests on a
  Poisson-type heuristic: the number of primes in `(L^8, e^{L^{1/4}}]` has
  mean `≈ ¼ log L`. *Fix:* label this clause *Assessment*. The
  surrounding [open] for the hub-count and pair-sum statements is right.

## 6. §12, beyond CRT evaluation (NONCRT)

**Faithfulness.** The scope sentence is correct: the section covers
finite prime-slice families of Cor sliceCap only, and not the sequential
or balanced settings (NC §2.4). Prop highlevel = NC Prop 2.1 (sketch
marked). Lemma walshfourier = NC Lemma 2.2; I re-derived the proof: the
Fourier support of `g` is in `Θ_S` with `|ĝ| ≤ Q₀^{−1}Πp_ℓ`, then
Parseval, and the `Θ_S` are disjoint. Thm perfreq = NC Thm 2.3 + Cors
2.4–2.5: the weights `log(1/(2p⁺))`, `s_* = log 2`,
`ε ≤ e^{−λ}R_1`, `λ_N = 2log(4N)`, and the cap
`C(log N)^{3/4} + log(P/φ(P))` with no size bound on the slice primes.
The paper's Case-A label "proved mod ET Prop 1.4" is more careful than
NC's "PROVED", correctly inherited from Cor sliceCap. The "not covered"
list (Vaaler/ψ, floor/ceiling, exact `|S_N|`, smooth windows,
dispersion over moduli) and `(H_eq)` CONDITIONAL match NC §§2.3–2.5.
Thm primemaj (1),(2) = NC Lemma 3.1, Thms 3.2, 3.3, including the
`≪ log λ` loss in the budget lemma and the `O((log log N)²)` cost of
primality. Prop 4.1, Prop 4.2, Thm 8.1, Lemma 8.2/Cor 8.3 and Prop 8.4
match the source. The withdrawn Conj 8.5 is reported as withdrawn,
Cor 8.7 as CONDITIONAL on `H_node`, and §8.3 as EVIDENCE. Remark 3.4 is
an Assessment; the paper labels both bullets that way, which is more
conservative than NC and acceptable.

* **D7 (MINOR, faithfulness: dropped provisos).** For prime moments
  beyond level `A log N`, NC Prop 4.1 requires three provisos: (i) every
  high-level term costs `≥ |a_i|` (the Remark 3.4 Assessment), (ii)
  `Σ_high|a_i| < π(N)`, (iii) slice primes `≤ N^{O(1)}`. NC also notes
  that Thm 3.2 + Prop 4.2 alone leave a gap. §12 "Moment methods" and
  §13 item 3 say "only under the Assessment", which suggests the
  Assessment alone suffices. *Fix:* "only under the Assessment of
  [NC, Rem 3.4] together with `Σ_high|a_i| < π(N)` and slice primes
  `≤ N^{O(1)}` [NC, Prop 4.1]".

* **D8 (MINOR, precision in §12).**
  (a) Thm perfreq omits the quantifier "for all `λ ≥ s_*`, `α > 0`" from
  the displayed inequality.
  (b) Thm primemaj (1) states only `|F_ℓ(c)∖{0}| < ℓ−1`. NC Thm 3.2 also
  needs `|F_ℓ(c)∖{0}| ≤ (ℓ−1)/4`, which the paper leaves implicit in "in
  place of `p_ℓ(c)`". State it.
  (c) Cor 8.7's conclusion "beating 3/4 needs `k ≥ (log N)^{3/4+o(1)}`"
  also needs `m = E_int H ≥ 16(log N)^{3/4+δ}`. NC supports this for the
  full Case-B family only by the review's enumeration and a heuristic,
  so it should be stated as an added hypothesis or labelled
  [evidence].
  (d) "this holds at every level `λ ≤ c(log N)^{4θ/3}`": the dichotomy
  of Thm 8.1 holds at every λ. What the range restricts is where branch
  (D) is non-vacuous, i.e. where `Φ̄(λ) < s − log(8Q₀/|R|)`. Rephrase
  as in NC §8.1.
  (e) Nit: NC Prop 8.4 gives `≤ (N+1)(1+log N)²/4` pairs, so the mean
  is `≤ ¼(1+1/N)(1+log N)²`, not `≤ ¼(1+log N)²`.
