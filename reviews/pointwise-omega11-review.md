# Hostile review R44a of POINTWISE_OMEGA11.md (reviewer 1: §2 graded quarantine, Lemma 3.1 transfer)

Reviewed: branch side-agent/quarantine-bound @ 105a522 (merged into side-agent/review-omega11a).
Status: ROUND 1 COMPLETE.
Scope: §2 (Setting 2.0, Lemmas 2.1–2.2), Lemma 3.1, and the parts of Thm 3.2 / Cor 3.3 that
consume them (Haar side, twist, transfer, cost ledger). §1 (Lemma 1.1, Cor 1.2) is reviewer 2's
scope; I only spot-checked Lemma 1.1's edge-weight inequality (`λ^j≤λ^v≤√2<λ+1`, edge weight
`≤λ·λ^{2(v−1)}≤λ^{2v}`: correct).

## Summary verdicts

| claim | verdict |
|---|---|
| Setting 2.0 (fibre coordinates, independence on `n≡1 (Q)`, event consistency) | SOUND |
| Lemma 2.1 (`P(E)≤C loglogT·g/M` for every Q; S♯ Q-uniform with O2 Lemma 11.1's bound; (I)) | SOUND |
| Lemma 2.2 (termination; `Σ_{ℓ∈supp E}w_ℓ≤c`; `log Q≤9+(𝓛/c)Σs·h≤9+(1+o(1))𝓛²S♯/(c log𝓛)`) | SOUND (minors m1–m2) |
| LLL use with partial quarantine (dependency graph, `δ≥e^{−2.2S}` at c=1/64, `e^{−4S♯}` at c=1/8) | SOUND |
| Lemma 3.1 (O9 Thm 1.1 with fibre cells, `E_H`, twist on the Q-coprime part ψ_2) | SOUND (minors m3–m4) |
| Thm 3.2, the §2/§3.1 inputs: quarantine `≪𝓛^6` under ET, twist via O8 Lemma 3.3 with `w_{ℓ_0}≤1/64`, transfer with `ℓ_aux` | SOUND as an implication from (G), ET Prop 1.4, O10 Thm 3.4 and §1 (Lemma 1.1/Cor 1.2, not in my scope) (minor m5) |
| Cor 3.3 (`log(1/δ*)≤log φ(Q)+4S♯≪𝓛^6`, mod ET) | SOUND |
| §4 H_ω EVIDENCE numbers (T=10⁴,10⁵) | reproduced from scratch (`review_o11a_hmean.py`): mean h 2.324, 2.572; share `ℓ≤𝓛²` 141/172, 308/389 — exact agreement |

No FATAL or MAJOR defect found in my scope. The exponent improvement 1/7→1/6 is, as far as
§2/§3 go, a correct consequence of the inputs listed in Thm 3.2's label.

## Re-derivations and checks

### Re-derivation notes: Setting 2.0, Lemma 2.1 (independent)

* Fibre law. On `n≡1 (Q)` (Haar on `(ℤ/N)^*`), CRT makes `n mod ℓ^{f_ℓ}` independent over ℓ,
  each uniform on `{x mod ℓ^f : x≡1 (ℓ^a)}` (`ℓ^{f−a}` points; units if a=0). For `v>a≥1`,
  `P(X≡c mod ℓ^v)=ℓ^{f−v}/ℓ^{f−a}=ℓ^{−(v−a)}`; for a=0, `1/φ(ℓ^v)` if c is a unit, else 0
  (ℓ|D: event impossible, still ≤ the bound). Both `≤(ℓ/(ℓ−1))ℓ^{min(v,a)}/ℓ^v`. CHECKED.
* Consistency: for `ℓ∈supp`, `ℓ^{a_ℓ}|gcd(M,Q)|4D+1`, so `−4D≡1 (ℓ^{a_ℓ})`. CHECKED.
* `P(E)≤(gcd(M,Q)/M)·M/φ(M)≤C loglogT·g/M`, using survival `gcd(M,Q)|g`. CHECKED.
* `S♯`: the O2 Lemma 4.1/11.1 proof sums `g/M` over *all* atoms; the only non-obvious step,
  the first term of the k-progression, is fine because `g|k+r'`, `k≥r'` force `k≥g/2`, so
  the first term is `≤2/g`. S♯ is Q-independent. CHECKED.
* (I): `n≡1 (Q)`, `n≡−4D (M)` ⇒ `gcd(M,Q)|4D+1`; `M|Q` contradicts Fact 1.1 (PO, `1∉𝓡(M)`);
  else `supp≠∅` (M odd, ℓ-part of Q is `ℓ^{a_ℓ}`) and E occurs, since `v_ℓ(M)≤f_ℓ`. CHECKED.

### Re-derivation notes: Lemma 2.2 (independent)

* Termination: each step raises some `a_ℓ<f_ℓ`; finite. Masses are NOT monotone in Q
  (raising `a_ℓ` multiplies `P(E)` at ℓ by ℓ for atoms with `v_ℓ>a_ℓ+1`), but neither
  termination nor the cost argument needs monotonicity: the cost uses only the Q-uniform
  majorant `w_ℓ(Q_i)≤Σ_{v_ℓ(M)≥a+1}s`. Survival is monotone decreasing in Q (not needed).
* (LLL): at the end, `ℓ∈supp E` ⇒ `a_ℓ<v_ℓ(M)≤f_ℓ`, so the stopping rule applies at ℓ:
  `w_ℓ≤c(a_ℓ+1)logℓ/𝓛≤c·v_ℓ(M)logℓ/𝓛`; summing, `≤c·logM/𝓛≤c`. CHECKED.
* Dependency structure with partial quarantine: E is measurable w.r.t. `{X_ℓ: ℓ∈supp E}`
  (quarantined digits are constants on the fibre); E is mutually independent of all events
  with disjoint support. Neighbours of E are among events with some `ℓ∈supp E∩supp E'`, whose
  total probability is `≤Σ_{ℓ∈supp E}w_ℓ` (w counts atoms, ≥ distinct events). With
  `x=2P`, `x_E≤2c≤1/4` and `∏_{E'∼E}(1−x_{E'})≥1−2c≥3/4≥1/2`. Then
  `−log(1−x)≤(4/3)x` gives `P(no event)≥exp(−(8/3)S_tot)≥exp(−4S♯)`. CHECKED.
* Cost: a step (ℓ,a→a+1) at stage `Q_i` has `logℓ<𝓛w_ℓ(Q_i)/(c(a+1))≤(𝓛/c)Σ_{v_ℓ(M)≥a+1}s/(a+1)`;
  each pair (ℓ,a) at most once; swap sums ⇒ `Σ s·Σ_{ℓ|M}H_{v_ℓ(M)}`. CHECKED.
  `H_v≤log₂(v+1)` (induction, `log₂(1+x)≥x` on [0,1]) and `Σ_ℓlog₂(v_ℓ+1)=log₂τ(M)`. CHECKED.
  Wigert: `log₂τ(M)≤(1+o(1))𝓛/log𝓛` uniformly for `M≤T`. CHECKED.

### Re-derivation notes: Lemma 3.1 (independent, against O9 Thm 1.1 as printed)

* `G=(ℤ/N)^*→(ℤ/Q)^*` is onto (Q|N) with kernel H, so `|H|=φ(N)/φ(Q)` and
  `c(χ)=E_H[Bχ̄]/φ(Q)`. Items 2 and `c(χ_0)=μ/φ(Q)`: CHECKED.
* Item 1: consistency `b_i≡1 (gcd(d_i,Q))` makes `1[n≡b_i (d_i)]1[n≡1 (Q)]` one class mod
  `lcm(d_i,Q)`; its coefficients vanish unless χ is trivial on `1+lcm(d_i,Q)ℤ`, so
  `cond χ | lcm(d_i,Q) ≤ Z`. CHECKED.
* Item 3: real primitive conductors are `2^e·(odd squarefree)`, `e∈{0,2,3}`; with `8|Q`
  every prime-power factor of f at a prime dividing Q divides Q, so `f_1|Q`, `ψ_1≡1` on H,
  and `χ=ψ_2` on H. `f_2` is odd squarefree (coprime to 8|Q), so `f_2∤d_i` gives a prime
  `p|f_2`, `p∤d_i`, `p∤Q`; on H the p-coordinate is uniform on units mod `p^{v_p(N)}` and
  independent of the cell, so the cell's `ψ_2`-mean is 0. `f_2=1`: χ trivial on H, factors
  through `(ℤ/Q)^*`, Case A with `q_1|Q≤Z` and the Page bound unchanged. `f_2>1`: Case B
  with `|c(χ)|=|E_H[Bψ_2]|/φ(Q)≤μ/(4φ(Q))`. CHECKED.
* `log N≤log Q+log D≤log Q+1.04max d_i≤2Z` keeps `R_1` as in O9. CHECKED.
* Cell consistency for the actual B of Thm 3.2: events `X_ℓ≡−4D (ℓ^v)`, `v>a_ℓ`, have
  `−4D≡1 (ℓ^{a_ℓ})`; any function of a fibre coordinate is a sum of cells with fibre values;
  intersections of consistent cells are consistent or empty. So the hypothesis holds, but
  only if the cell representation of `u_j` uses fibre-valued residues (see defect m3).
* Twist (O8 Lemma 3.3) in the graded system: for `ℓ_0|f_2`, `a_{ℓ_0}=0` (since
  `gcd(f_2,Q)=1`) and `ℓ_0≤T` (primes of `d_i` other than `ℓ_aux`, and `ℓ_aux|Q`). The
  conditional LLL step needs neighbourhood sums of `E∖ℓ_0` `≤2Σ_{ℓ∈supp E}w_ℓ≤2c=1/32`, and
  `w_{ℓ_0}≤c·logℓ_0/𝓛≤1/64`, so `1.07/64<0.02`. CHECKED.
* ET Prop 1.4 (checked in sources/elsholtz-tao-1107.1010.pdf, p. 4): `Σ_{a≤A,b≤B}τ(kab²+1)≪AB
  log(A+B)log(1+k)` for `k≪(AB)^{O(1)}`; with k=4 and dyadic (s,r') blocks this gives
  `Σ τ(4sr'²+1)/(sr')≪𝓛³`, hence `S♯≪𝓛^4log𝓛`. CHECKED (blocks with A or B ≤1 need the
  trivial separate treatment; the statement requires A,B>1 — immaterial).

### From-scratch numerics (scripts/review_o11a_graded.py, scripts/review_o11a_toy.py)

`review_o11a_graded.py T c n`: atoms enumerated directly; Lemma 2.2 with *atomic* masses
(batch raising per round — valid, since the cost proof only needs `w_ℓ(Q')>θ` at *some*
stage and the Q-uniform majorant); asserts at every stage `P(E)≤s'=(g/M)∏ℓ/(ℓ−1)` for
each surviving atom, `w_ℓ(Q_i)≤Σ_{v_ℓ(M)≥a+1}s'` at every raise, final `max_EΣw≤c`,
`log Q≤9+(𝓛/c)Σs'h`, `h≤log₂τ`; and (I) *with its converse* (`W(n)≤T` ⟺ some surviving
event occurs) on random `n≡1 (Q)` (n up to 1e30·Q). All assertions pass:

| T | c | rounds | events | S_tot | max_EΣw | log Q | proven bound | (I) samples / W>T |
|---|---|---|---|---|---|---|---|---|
| 100 | 1/8 | 1 | 15 | 0.23 | 0.110 | 42 | 611 | 5000 / 3986 |
| 1000 | 1/8 | 1 | 1256 | 2.86 | 0.105 | 156 | 3497 | 3000 / 174 |
| 1000 | 1/64 | 1 | 123 | 0.18 | 0.0155 | 514 | 27916 | 1000 / 864 |
| 10⁴ | 1/8 | 1 | 23271 | 9.41 | 0.085 | 346 | 12717 | 300 / 0 |
| 10⁴ | 1/64 | 1 | 11852 | 2.47 | 0.0144 | 1944 | 101672 | 50 / 6 |

The atomic iteration at `10⁴, c=1/64` gives `log Q=1944` (293 primes) vs the author's
distinct-event variant 1900 (287 primes), consistent with the author's note that the
atomic rule additionally catches ℓ=1237; `max_EΣw=0.0144` agrees with the author's table.

`review_o11a_toy.py 3000 7`: (a) CRT check that on `n≡1 (Q)` mod `N=8·9·25` the
coordinates are independent and fibre-uniform (50 random `(a_3,a_5)`); (b) exact
fibre probabilities; (c) 393 random graded toy systems (primes 3..11, exponents ≤3,
random partial quarantine, ≤8 events with initial-segment cylinders) meeting
`max_EΣ_{ℓ∈supp E}w_ℓ≤1/8`: exact `P(no event)≥∏(1−2P(E))≥exp(−(8/3)ΣP)` in all.

## Defects (all MINOR)

**m1 (Lemma 2.2, cost bullet).** `log Q ≤ log 840 + log 8 + …` counts `log 8` twice
(`840=8·3·5·7` is the initial Q). Exact: `log Q = log 840 + Σ_steps logℓ`. Harmless (the
constant 9 still holds). Repair: write `log 840` (≤6.74).

**m2 (Lemma 2.2 vs the numerics).** The lemma raises one prime per step; the scripts raise
all violators per round. The proof covers this verbatim (every raise in a round is justified
at the same stage `Q_i`, and the cost inequality uses only `w_ℓ(Q_i)≤Σ_{v_ℓ(M)≥a+1}s`, which
is Q-uniform; the stopping test is at the final Q). Repair: one sentence "any order, and
simultaneous raises at one stage, are allowed". (The text already says this for the
distinct-event variant.)

**m3 (Lemma 3.1 ↔ Thm 3.2: cell consistency of the actual B).** Lemma 3.1 requires every cell
of B to satisfy `b_i≡1 (gcd(d_i,Q))`. Thm 3.2 never checks this for the BRW minorant built
from Cor 1.2's `u_j`. It holds (event cells have `−4D≡1 (ℓ^{a_ℓ})`; `u_j` is a function of
fibre coordinates, so it is a combination of cells with fibre-valued residues mod
`ℓ^{i+1}`, `i≥a_ℓ`; intersections of consistent cells are consistent or empty), but only for
*that* representation — an arbitrary representation by residues mod `ℓ^{i+1}` ignoring
the fibre would not be consistent. Repair: add this sentence to the "Minorant" bullet.

**m4 (Lemma 3.1 statement).** "O9 Thm 1.1 holds without `gcd(d_i,Q)=1`" leaves implicit
that `gcd(b_i,d_i)=1` is still assumed (or that non-unit cells vanish on H and may be
dropped). Repair: say so.

**m5 (Thm 3.2, twist bullet).** `w_{ℓ_0}≤c` uses `θ_{ℓ_0}=c·logℓ_0/𝓛≤c`, i.e. `ℓ_0≤T`;
state that `ℓ_0≠ℓ_aux` because `ℓ_aux|Q` (so `gcd(f_2,Q)=1` excludes it) and all other
primes of the `d_i` are coordinates `≤T`.

## Not checked / caveats
* §1 (Lemma 1.1 in full, Cor 1.2's τ and modulus bookkeeping) — reviewer 2.
* OMEGA10 Thm 3.4, (G), Haeupler–Saha–Srinivasan conditional LLL: taken as cited (O10 Thm
  3.4 reviewed SOUND elsewhere; (G) as in O9 reviews).
* Replay: `PYTHONPATH=scripts uv run python scripts/review_o11a_graded.py T c n` (rows above;
  10⁴ ≈ 2 min), `scripts/review_o11a_toy.py 3000 7` (≈1 min),
  `scripts/review_o11a_hmean.py 10000 100000` (≈10 min), all under `ulimit -v 8000000`.
