# Review R73 of EXCEPTIONAL_LARGESIEVE7.md (hostile reviewer, branch side-agent/review-ls7)

Status: round 1 complete. No FATAL defect; one MAJOR (D1, citation, repaired); rest MINOR.
All repairs D1–D8 applied by reviewer to `EXCEPTIONAL_LARGESIEVE7.md` in this branch (marked "R73"). Reviewed text: `EXCEPTIONAL_LARGESIEVE7.md` as merged from
`side-agent/residue-dispersion` (commit 6bae2a4). From-scratch scripts: `scripts/review_ls7_*.py`.

## Verdict summary (per claim)

| claim | verdict |
|---|---|
| Lemma 1.1 | SOUND (proof re-derived; brute force M<20000) |
| Lemma 1.2 | SOUND (re-derived; brute force all p \| M, M<20000) |
| Lemmas 2.1–2.2 | SOUND-AFTER-REPAIRS (D1 citation: Shiu's class M not literally satisfied; Nair–Tenenbaum fixed-ε form needed; D2 constant) |
| Thm 3.1 | SOUND (given D1 repair; D3 minor: C depends on W, needs γ ≤ 1, N large) |
| Prop 4.1 | SOUND (re-derived; 135 exact toy instances incl. brute-force H* = k) |
| Remark 4.2 | Assessment, honest; but §4 summary bullet overclaims (D6) |
| Thm 4.3 | SOUND-AFTER-REPAIRS (D1; D5 hidden hypothesis \|P\| ≤ z^{1/2}/3, δ bookkeeping) |
| Prop 5.1 | SOUND-AFTER-REPAIRS (D4: displayed lower bound wrong for small γt_p; conclusion unaffected) |
| (RD′) / §5 sketch | (RD′) implication SOUND; "sufficient for LS6's route" is Assessment (D7); §5 (a,D)/Case A sketch correctly Assessment |
| Cor 6.1, §7 | Cor 6.1 SOUND; §7 EVIDENCE reproduced, but it measures the triple proxy (D8) |

## Defects

(numbered below as found)

**D1 (MAJOR, misapplied citation; repairable). §2 Lemma 2.1, last paragraph of proof.**
Shiu 1980 Thm 1 (checked against `sources/shiu-1980.pdf`, p. 162–163) requires `f ∈ M`:
(i) `f(p^l) ≤ A₁^l`, and (ii) **for every ε > 0** `f(n) ≤ A₂(ε)n^ε` for all n. The function
`f(n) = 1[P(n) ≤ 2Q]Γ(n)n^η` with fixed `η = 1/log 2Q > 0` **violates (ii) for every
ε < η** (take `n = 2^m`, m → ∞). The text's "η ≤ 1/log z ≤ ε/2 for N large" only gives (ii)
for each *fixed* ε once N ≥ N₀(ε) — not the "for every ε" hypothesis — so Thm 1 does not
apply as cited. The conclusion is nevertheless correct: Nair–Tenenbaum 1998
(`sources/nair-tenenbaum-1998.pdf`, Thm 1 with k = 1, class `M₁(A,B,ε)` with a **single
fixed** ε, `0 < ε < 1/8`, constant depending only on A, B, ε, δ; progressions via the
uniformity in the coefficients of Q, their remark after Thm 1) covers it with `A = 8e`,
`B = B(ε)`, ε = 1/16 say, uniform in Q because `η ≤ 1/log z ≤ ε/2`; alternatively "Shiu's
proof uses (ii) only for one ε = ε(α, β)". *Repair:* cite NT98 Thm 1 (or Shiu's proof, with
that remark) instead of Shiu Thm 1 as stated, and change "PROVED given Shiu 1980 Thm 1" to
"PROVED given Shiu's theorem in the fixed-ε form (Nair–Tenenbaum 1998, Thm 1)" in Lemma 2.1,
Thm 3.1, Thm 4.3 and the summary table. (Applied by reviewer.)

**D2 (MINOR, constant). §2 Lemma 2.1 proof.** "`f(ℓ^l) ≤ 3e^l`" and "`γ'(ℓ) ≤ 3`" are false
at small primes: K2 §2 sets `γ'(p) = γ(p)` for `p ≤ W`, with `γ(2) = 8` (whence K2's
`Γ(m) ≤ 8·3^{ω(m)}`); also `(1−2^{−1/2})^{−1} ≈ 3.41`. Correct: `f(ℓ^l) ≤ 8e^l`, `A₁ = 8e`.
Harmless. *Repair applied:* `3e` → `8e`.

**D3 (MINOR, hidden hypotheses in a constant). §3 Thm 3.1 statement.** "There is an absolute
C": C inherits `C(α, W)` from Lemma 2.1 (W = K2's small-prime threshold), the collection
step uses `γ^{−3} ≤ γ^{−5}` and `(log z/γ)^r` with `γ ≤ 1`, `K^{2β} ≤ e^γ` needs
`K ≤ z^{γ/2}`, and D1's uniformity needs `N ≥ N₀`. *Repair applied:* "absolute C" →
"C depending only on W (for `0 < γ ≤ 1`, `K ≤ z^{γ/2}`, N large)".

**D4 (MINOR, wrong displayed inequality). §5 Prop 5.1 display.**
`Σ_q w_q/(qℓ) ≍ ℓ^{−1}∫_{t_p}^∞e^{−2γt}dt/t = ℓ^{−1}E₁(2γt_p)`, and `E₁(x) ≥ c e^{−x}/x` is
**false as x → 0** (`E₁(x) ~ log(1/x)`; e.g. `E₁(0.01) ≈ 4.04` vs `e^{−0.01}/0.01 ≈ 99`).
So "`≥ c e^{−2γt_p}/(γt_pℓ)`" fails when `γt_p` is small. Correct: `E₁(x) ≥ ½e^{−x}log(1+2/x)
≥ e^{−x}/(2(1+x))`, i.e. `≥ c e^{−2γt_p}/((1+γt_p)ℓ)`. The final comparison (`≥ e^{−O(γT)}/(Tz)`
vs `(log N)^C z^{−γ₀T}`, T fixed) is unaffected. *Repair applied.*

**D5 (MINOR, hidden hypothesis / bookkeeping). §4 Thm 4.3 proof (iv), (v).**
(v) `Π_{p∈P}γ′(p) ≤ e^{2|P|z^{−1/2}} ≤ 2` needs `|P| ≤ (log 2/2)z^{1/2}`, not in the
hypotheses ("P a finite set of primes > z"). Harmless for `|P| ≤ (log N)^C`. (iv) `W_y(n) ≤
C_δP̄^δ·P̄/(UVT)`: `n` ranges up to `CP̄^{2+6.2α}`, so `Γ(n) ≪ n^δ` gives `P̄^{2.1δ}`, and with
`δ = η/10` the exponent is `0.042η + 0.21η − 2η/3 ≈ −0.41η`, **not** `≤ −η/2`. Take
`δ = η/30` (then `≈ −0.55η`). *Repairs applied:* hypothesis `|P| ≤ z^{1/2}/3` added;
`δ = η/10` → `δ = η/30` with `C_δP̄^{2.1δ}`.

**D6 (MINOR–MAJOR, overclaim contradicting Remark 4.2). §4 "What the three results say
together", third bullet.** "for short cofactors `y < n < P̄^{1/2}` a single class already weighs
`≍ 1/n`, so no bound of the form `Π p^{−γ₀}` can hold without an extra condition" — this asserts
a disproof, while Remark 4.2 (correctly) says the existence of a class with `H* > P̄^κ` and
short cofactor is **open**, and in any case only cofactors `n < P̄^{γ₀}` (not all `n < P̄^{1/2}`)
would beat `P̄^{−γ₀}`. *Repair applied:* bullet rewritten conditionally ("if such classes exist
— open, Remark 4.2 — no bound … can hold for cofactors `n < P̄^{γ₀}`"). Same fix in the §0 table
row "Remark 4.2" (already says "open in both directions", consistent).

**D7 (MINOR, label). §0 table row (RD′) and §5 "the statement actually needed".** "(and
sufficient for LS6's route)" is an unproved Assessment: LS6's (DCC) combinatorics is not
written, and the multi-prime (RD′) may itself fail for short cofactors (Remark 4.2 applies to
`μ_a` verbatim). *Repair applied:* "(Assessment: what LS6's route appears to need)".

**D8 (MINOR, description of numerics). §7.** `scripts/largesieve7_dispersion.py` sums over
**divisor triples with multiplicity** and cuts each triple by `min(max(u,v),4u²t,4v²t)`, i.e. it
measures the right side of (3.0), not `μ^{ℛ,>}_a(p)` (distinct classes, cut by the true `H*`).
Reviewer's `scripts/review_ls7_toy.py` reproduces the proxy (0.2951, 0.2190, 0.1030 at p = 101,
211, 401) and computes the actual quantity with exact brute-force H*: 0.2432, 0.1786, 0.0914 —
smaller, same trend, maxima at least-height labels just above the cut (`−4`, `−1/4`, `−16`).
*Repair applied:* sentence added to §7.

## Per-claim notes

### Lemmas 1.1, 1.2 — SOUND
Re-derived: `g = gcd(D,A)`, `u = D/g`, `v = A/g` is coprime, `u | Av` ⇒ `u | A`, `uv | A`;
injectivity via `gcd((A/v)u, A) = A/v`; `4A ≡ 1 (M)` gives the three congruent labels, all of
the admissible form `−r/s`, `r ≥ 0`, `s ≥ 1`, `gcd(s,M) = 1` (LS6 §6.2 definition of H*), so
the H* bound is immediate. Lemma 1.2: `uvt = A ≡ 1/4 (p)` for odd `p | M`. Correct.
`scripts/review_ls7_triples.py` (from scratch; `uv run --with sympy --with numpy`): for all
`M ≡ 3 (4)`, `M < 20000`: set equality `{−4D : D | A²} = {−u/v}`, the bijection, `D = u²t`,
`A²/D = v²t`, all three label congruences, and Lemma 1.2's pinning at every prime `p | M`
(310815 (triple, prime) pairs) — 0 failures. Additionally (not checked by the author) the
H* upper bound `H* ≤ min(max(u,v), 4u²t, 4v²t)` against a brute-force least-label-height
for all `M < 4000` (22502 triples; equality in 20608) — 0 failures; Remark (a)'s example
`M = 167`, class 131, `H* = 13` via `−13/5` confirmed. (The author's "159390 triples" counts
triples, not (triple, prime) pairs — consistent.)

### Lemmas 2.1, 2.2 — SOUND-AFTER-REPAIRS (D1, D2)
Re-derived line by line: dyadic split `P(n) ∈ (Q,2Q]`, `Q ≥ y/2` covers `P(n) > y`;
`ℓ^η ≤ e` for `ℓ ≤ 2Q`; `e^x ≤ 1 + ex` on `[0,1]` gives `f(ℓ)/ℓ ≤ γ'(ℓ)/ℓ + eγ'(ℓ)η log ℓ/ℓ`;
Mertens gives `exp(Σ) ≪_W log 2Q·Π_{ℓ|k,ℓ≤2Q}(1−1/ℓ)` (using `e^{−x} ≤ (1−x)e^{x²}`, x ≤ 1/2);
`φ(k)^{−1}Π_{ℓ|k,ℓ≤2Q}(1−1/ℓ) = k^{−1}Π_{ℓ|k,ℓ>2Q}(1−1/ℓ)^{−1}`; the absorption
`2/(Q log 2) ≤ 1/(2 log 2Q)` holds for `Q ≥ z/2` large. Shiu's other hypotheses at the
parameters used: `x = 2Y`, interval length `Y = x/2 > x^β` (any β < 1/2), `k ≤ Y^{1−α}`,
`gcd(c,k) = 1` — fine; small x absorbed in the constant. Lemma 2.2: `Σ_i i^{r−1}e^{−i/(2L)}
≤ C_r L^r(1+log L)`, then `Σ_j j^s e^{−2γ j log 2/log z} ≤ C_s(log z/γ)^{s+1}`, `K^{2β} ≤ e^γ`
(needs `K ≤ z^{γ/2}`, as in K2) — correct. Only defects: D1 (citation), D2 (constant).

### Theorem 3.1 — SOUND (after D1; D3 wording)
Re-derived every step. (3.0): `n = M/p`, `w_{P(M)} = w_{P(n)}` as `P(n) > p`, `Γ(M) ≤ 2Γ(n)`
(`γ'(p) ≤ 2` for `p ≥ z`), every class is hit by ≥ 1 triple, all three heights `≥ H*`, so the
triple sum dominates. Boxes: `n ∈ [3Y_B, 32Y_B)` and `n > p` ⇒ `UVT > p²/32` (so `Y_B > p/32`,
`Y ≥ 2` in Lemma 2.1). Case L_u: for fixed `(v,t)`, `u ↦ n` is a bijection onto the
progression `n ≡ −p^{−1} (mod 4vt)` (reduced since `p ∤ 4vt` by Lemma 1.2), `k = 4vt ≤
16VT ≤ Y_B^{1−α}`; the dyadic Y covering `[3Y_B, 32Y_B)` all lie in `[Y_B, 32Y_B]` ✓. Pair
counts `min(V(T/p+1), 2T(V/p+1)) ≤ 2VT/p + 2min(V,T)` ✓; support condition
`4v²t < 32V²T ≤ 32max³`, `32^{1/3} < 4` ✓. Cases L_v, L_t ✓ (L_t uses `max(u,v) > p^{1/4}`).
Case S: `UVT < 16^{3/(1−3α)}p^{3(1−α)/(1−3α)}`, `2.97/0.97 = 3.062 ≤ 3.07` ✓; side
`< 16p^{1−α}(UVT)^α ≤ Cp^{1.0207}` ✓; count `≤ 2(1+Cp^{0.021})²min(U,V,T)` ✓;
`W_p(n) ≤ Γ(n)/n` uses `w_q ≤ 1` (true for `q ≥ z`, `K ≤ z^γ`) ✓; exponent
`1.042 + δ − 4/3 < −0.28` ✓; `(C log p)³` boxes ⇒ `≤ Cp^{−1/4}` ✓. Summation: boxes with a
given dyadic Y in `[Y_B, 32Y_B]` have `UVT/p ∈ [Y/32, Y]`, ≤ 6 values of `log₂UVT`, each
≤ `(s+2)²` factorisations ✓; Lemma 2.2 with r ≤ 2 ✓; `Σ_{max(V,T)=2^k}` has `2k+1` pairs ✓.
Final collection: `γ^{−5}(log p)^7/p ≤ γ^{−5}(log p)^6p^{−1/12}` and `γ^{−3}(log p)^4p^{−1/12}`
≤ the same for γ ≤ 1 ✓. The claimed independence of X is genuine (the sum is over all M).

### Proposition 4.1 — SOUND
Re-derived: `j ≡ −(P̄r)^{−1} (mod 4k)` is solvable (`P̄r` odd, `k ∉ P`, `r > y > 4y^{1/4} ≥ k`);
`4k | M+1` so `M ≡ 3 (4)` and `−1/k = −4D`, `D = A/k | A²` (Lemma 1.1, `(u,v) = (1,k)`); residue
`−1/k` at each `p ∈ P`; top `= r` (`j ≤ y < r`); `H* = k` by LS5 Lemma 1.2 compatibility (`k <
√(M/2)` as `M ≥ y·y^{7/8}`). FL: modulus `4k ≤ 16y^{1/4}`, `x/(4k) ≥ y^{5/8}/16 ≥ z^9` for
`y ≥ z^{16}`; sifting the odd primes `≤ z` (none divide 4k since `k > z`) gives `≫ x/(k log z)`
uniformly in the (unit) class — correct. `Σ_j 1/j ≫ log y/(k log z)`, `Σ_r 1/r ≫ 1/log y`;
consequence: `m ≥ ⌈1/(2γ₀)⌉+1` ⇒ `mγ₀ ≥ 1/2 + γ₀`, ratio `≥ y^{1/4+γ₀}/(log N)^{O(1)}` ✓.
Remarks (not defects): j may share a prime with P (then `p² | M`); the (RD) weight uses gain
`p` per prime regardless, so the bound is unchanged. `k ∉ P` existence: `≫ y^{1/4}/log y ≫
(log N)^C` primes in the k-window ✓.
`scripts/review_ls7_counterex.py` (from scratch): 135 random toy instances (`|P| ≤ 3`, primes
< 60, `M ≤ 3·10⁶`): `M ≡ 3 (4)`, `−1/k ∈ ℛ(M)`, residues `−1/k` at all p, and brute-force
`H* = k` whenever `2k² < M` — 0 failures.

### Proposition 5.1 — SOUND-AFTER-REPAIRS (D4)
Re-derived: rough part `x ≡ −4ℓ (pq)`, `x ≡ −pq (ℓ)`; a label `−r/s` of height
`H < pq/(4ℓ+1)` forces `r = 4ℓs`, then `ℓ | s` — contradiction ✓; weight `w_qΓ(pqℓ)/(qℓ)` ✓;
smooth part 4 (p, q, ℓ > z), presence iff `c ≡ −pq (mod 4)` — one class of q mod 4 for each
odd c (fibres of the forced mixtures have c odd; for even c the class is absent — harmless,
noted). Only the displayed lower bound is wrong for small `γt_p` (D4). The (a,D) family is the
ET Lemma 3.2 family (K2 §1: any `a, D ≥ 1`), so `a = pq` is admissible ✓.
`scripts/review_ls7_counterex.py`: all prime triples `3 ≤ ℓ < p < q < 90` with `ℓ < 30`,
`p < 60` (1218 instances): residues and brute-force `H*(x mod pqℓ) ≥ pq/(4ℓ+1)` — 0 failures;
min `H*(4ℓ+1)/(pq) = 1.011`, so the bound is essentially tight.

### Theorem 4.3 — SOUND-AFTER-REPAIRS (D1, D5)
CRT pinning (i) ✓ (t ↦ v: `2^{|P|}` square roots); pair counts `2^{|P|}(VT/P̄ + min(V,T))` ✓;
cut ⇒ `max ≥ P̄^{κ/3}/4` ✓; L-case summation as in Thm 3.1 with `log p → log P̄`, Lemma 2.1 at
α = η/100 (constant `C_η`) ✓. Case S: `(3−3α)/(1−3α) ≤ 3+6.2α`, sides `≤ CP̄^{1+2.1α}` ✓;
`UVT > P̄n/32 ≥ P̄^{3/2+η}/32` ✓; exponent fixed by D5. `4^{|P|} ≤ P̄^{2/log z}` ✓ (e² > 4).
The L-cases do not use the long-cofactor hypothesis; only Case S does — consistent with
Remark 4.2's diagnosis.

### Remark 4.2 — honest Assessment (but see D6 for the §4 summary bullet).

### (RD′) and §5 sketch
Implication H*-cut ⇒ (RD′): a label `λ ≡ b_C (G_C)` of height `≤ H₀` reduces to an element of
`R_P(H₀)` mod P̄, so `a ∉ R_P(H₀)` forces `H*(C) > H₀` ✓ (LS6's label convention requires
`gcd(s, G_C) = 1`, a fortiori `gcd(s, P̄) = 1`). Prop 4.1's residue lies outside
`R_P((max P)^{1/4})` by compatibility (`H₂ ≥ P̄/(2k)`) ✓. The (a,D)/Case-A paragraph is
explicitly "Assessment; not proved", correctly labelled. Only D7.

### Corollary 6.1 — SOUND
Fibre weight `Γ(M_r)P̄/M_r` times `π_s(c ≡ λ) ≤ Γ(s)/s` equals the full weight
`Γ(M)P̄/M` (Γ multiplicative on coprime `s, M_r`); a label mod M is a label mod `M_r`, so
`H*_{M_r} ≤ H*_M` and the fibre cut gives a sub-sum ✓; deduplication of rough parts only
lowers the fibre sum ✓. The "not proved" paragraph (no single exceptional event for all
(P,a)) is honest.

### §7 numerics — EVIDENCE, reproduced (D8).

## Overall assessment
The note's main content holds up: the triple parametrisation and pinning (Lemmas 1.1–1.2) are
correct and brute-force verified; Theorem 3.1 ((RD) at one prime for ℛ(M), rate `p^{−1/12}`,
uniform in X, short cofactors included) is correct line by line, *conditional on* the
Shiu-type input, which must be cited in its fixed-ε form (D1 — the literal Shiu Thm 1 class M
excludes the Rankin-tilted f). Both refutations (Prop 4.1: LS6's max-prime cut fails for
several primes; Prop 5.1: the H*-cut fails at one prime with (a,D) classes) are correct and
numerically confirmed with exact H*. Theorem 4.3 needs a stated `|P|` bound and a smaller δ
(D5). Labels after repair are honest; the "sufficient for LS6's route" and the short-cofactor
bullet were overclaims (D6, D7), now Assessment/conditional. ES is not solved; (DCC), (RD) for
(a,D)/Case-A classes, multi-prime short cofactors, and the fibre-uniform exceptional event
remain open, as the note itself says.

Replay (reviewer scripts):

    ulimit -v 8000000
    timeout 1800 uv run --with sympy --with numpy python scripts/review_ls7_triples.py 20000 4000
    timeout 1200 uv run --with sympy --with numpy python scripts/review_ls7_counterex.py
    timeout 1500 uv run --with sympy --with numpy python scripts/review_ls7_toy.py 10 101 211 401
