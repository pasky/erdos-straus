# POINTWISE_TRANSFER — Haar avoidance ⇒ prime avoidance (task O42)

Branch `side-agent/avoid-transfer`. Status labels as in DISCOVERIES.md.
Source of all machinery: `paper/es-subexp-note.tex` (cited below as [SN],
with its lemma names), i.e. POINTWISE_OMEGA8 §§1–5 + POINTWISE_OMEGA9 §§1–3.
This file *abstracts* that machinery; nothing here is about 4/n until §5.

Cited inputs (same as [SN]): Gallagher's theorem in the form [MV3, Thm 28.19]
with Landau–Page (= [SN] Thms `thm:G`, `thm:xz`), Håstad's switching lemma
([SN] `thm:hastad`). "Proved modulo G+H" means: proved here assuming these.

## 0. Setting

* `Q ≥ 1` a modulus, `a` a unit mod `Q` (the *target class*).
* `𝒫` a finite set of *free* primes, `ℓ ∤ Q`, `N = |𝒫| ≥ 1`. For `ℓ ∈ 𝒫` an
  exponent `e_ℓ ≥ 1`; `T ≥ 2` with `ℓ^{e_ℓ} ≤ T` for all `ℓ ∈ 𝒫`.
* Coordinates `X_ℓ(n) = n mod ℓ^{e_ℓ}`, valued in `G_ℓ = (ℤ/ℓ^{e_ℓ})^×` for
  `n` coprime to `ℓ`. **Haar measure** `ℙ`: the `X_ℓ` independent uniform on
  `G_ℓ` (= the uniform measure on units mod `∏ ℓ^{e_ℓ}`).
* A *congruence event* `E` is a nonempty set `supp E ⊆ 𝒫` with `|supp E| ≤ k`
  together with an **arbitrary nonempty** subset of `∏_{ℓ∈supp E} G_ℓ`; equivalently a
  set of unit classes modulo `d_E = ∏_{ℓ∈supp E} ℓ^{e_ℓ}`. An integer `n`
  coprime to `d_E` *lies in* `E` if `(X_ℓ(n))_{ℓ∈supp E} ∈ E`.
  Typical case: `E = {n ≡ b (mod d)}` with `d | ∏ℓ^{e_ℓ}`, `gcd(b,d)=1`,
  `supp E` = primes of `d`, `ℙ(E) = 1/φ(d)`.
* Family `E_1,…,E_m` (`m ≥ 1`), `S = Σ_i ℙ(E_i)`,
  `w_ℓ = Σ_{i: ℓ∈supp E_i} ℙ(E_i)`, `F = 1[no E_i occurs]`, `δ = 𝔼F`.
  `i ∼ j` iff `supp E_i ∩ supp E_j ≠ ∅`.
* (LLL) weights `x_i ∈ [0,1)` with `ℙ(E_i) ≤ x_i ∏_{j∼i, j≠i}(1−x_j)`;
  `δ_L := ∏_i (1−x_i)` (so `δ ≥ δ_L` by the local lemma).
* (Tw) *twist hypothesis*: for every real primitive character `ψ` whose
  conductor `f > 1` divides `∏_{ℓ∈𝒫} ℓ^{e_ℓ}`, `|𝔼[Fψ]| ≤ δ/5`.
  (Here `ψ(n)` is a function of the coordinates `X_ℓ`, `ℓ | f`.)

* *Atoms*: the distinct cells `{X_I = σ}` (`I = supp E_i`, `σ ∈ E_i`) occurring
  in the events; `m_a` = their number. Always `m_a ≤ Σ_{j≤k} C(N,j)T^j ≤ 2(NT)^k`.

Parameters:
```
b   = ⌈log₂(4NT)⌉
k₀  = ⌈log₂(400·m_a²·(S+1)/δ_L)⌉        (≤ 2k·log₂(NT) + log₂(1/δ_L) + log₂(S+1) + 12)
t   = 10·k·b·k₀
```

## 1. Statements

**Theorem 1.1 (abstract transfer; proved modulo G+H).** In the Setting, with
(LLL) and (Tw), there is a prime `p` with `p ≡ a (mod Q)`, `p > T`, `p` lies
in no `E_i`, and
```
log p ≤ C₇ · ( log Q + (3k+2t)·log T + 1 ),
```
`C₇` absolute and effective (given effective constants in G and H).

*No* hypothesis bounds the number of residue classes inside an event or the
number of events (only `log m_a ≤ k log(NT)+1` enters), or the size of `∏ℓ^{e_ℓ}`; no single-value,
codegree, or Siegel-zero hypothesis is needed. Coprimality: events are sets of
*unit* classes; a non-unit class `n ≡ b (d)`, `g = gcd(b,d) > 1`, contains no
prime `> T` (a prime in it is divisible by, hence equal to, a prime
factor of `g`, and those are free primes, hence `≤ T`) and may simply be deleted. Moduli must be supported on free
primes (prime-power parts dividing `Q` must first be decided by the target
class — the "survival" reduction of [SN] §2).

**Lemma 1.2 (sufficient condition for (Tw); proved).** Put
`η_ℓ = Σ_{i: ℓ∈supp E_i} ℙ(E_i) ∏_{j∼i}(1−x_j)^{−1}`. If `η_ℓ ≤ 1/6` for all
`ℓ ∈ 𝒫`, then (Tw) holds.

**Corollary 1.3 (local-density form; proved modulo G+H).** Suppose only that
every event lies on `≤ k` free primes and `w_ℓ ≤ 1/(64k)` for all `ℓ ∈ 𝒫`.
Then there is a prime `p ≡ a (Q)`, `p > T`, in no `E_i`, with
```
log p ≤ C₈ · ( log Q + k·log T·log(4NT)·(S + k·log(4NT)) ).
```
(Take `x_i = 2ℙ(E_i)`: `log(1/δ_L) ≤ 2.2S`, and Lemma 1.2 applies; see §2.)
In particular with `N ≤ T`: `log p ≪ log Q + k(log T)²(S + k log T)`.

*Benchmark (single class, Linnik).* Without the theorem the only general route
is to pick one surviving class `c mod Q·D₀`, `D₀ = ∏_{ℓ∈𝒫} ℓ^{e_ℓ}`, and apply
Linnik: `log p ≪ log Q + log D₀`, and `log D₀ ≍ Σ_ℓ e_ℓ log ℓ`, typically
`≍ N log T`. Corollary 1.3 replaces `N log T` by a polynomial in the *local*
data `(k, log T, S)` with only `log N` dependence.

## 2. Proofs

**Step 1 (atoms; the role of "single value").** Replace the family by the list
`C_1,…,C_{m_a}` of its distinct atoms, in any order. This does not change `F`
(an integer coprime to the free primes lies in some `E_i` iff it lies in some
atom). The local lemma is used only through `δ ≥ δ_L` and (Tw), which are
properties of `F`; so the LLL weights are attached to the *original* events,
while the sandwich below runs over atoms. Splitting into single values is
needed for exactly one step: [SN] `lem:brw` requires, for `u_j` a function of
the coordinates off `supp C_j`, that conditioning on `C_j` *fixes* the
coordinates inside `supp C_j`, leaving the others uniform (so `F^{(j)}` is defined and `𝔼[A_j e_j²] = ℙ(C_j)𝔼(F^{(j)}−u_j)²`).
Its cost is `log m_a ≤ k log(NT) + 1` in `k₀`.

**Step 2 (sandwich).** With `A_j = 1_{C_j}`, `F_{<j} = ∏_{i<j}(1−A_i)`,
`F^{(j)}` = `F_{<j}` with `X_{supp C_j}` fixed to the values of `C_j`,
`u_j = (F^{(j)})^{≤t}` (Efron–Stein truncation), `v_i = Σ_{j<i} A_j u_j`, put
`B = 1 − Σ_i A_i(1−v_i)²`. By [SN] `lem:brw` (verbatim; it is stated for
arbitrary cells and arbitrary `u_j`): `B ≤ F` pointwise for *every* assignment
of 0/1 values to the `A_i`, hence for every integer `n` (with
`A_i(n) = 1[n ∈ C_i]`), and `𝔼[F−B] ≤ m_a² Σ_j ℙ(C_j)·En(F^{(j)};t)`.

**Step 3 (tail).** `F^{(j)}` is the avoidance indicator of the restrictions of
the atoms `C_i` (`i<j`) compatible with `C_j`, each on `≤ k` coordinates (or
`F^{(j)} ≡ 0`). [SN] `lem:tail` gives `En(F^{(j)};10kbk₀) ≤ 4·2^{−k₀}` once
`2^b ≥ 4NT`. (Remark: the proof there only uses that each event is a Boolean
function of the `≤ kb` bits encoding its `≤ k` coordinates, hence a DNF of
width `≤ kb`; so it holds verbatim for arbitrary events, not only cells.)
Hence, as `Σ_j ℙ(C_j) ≤ S` (atoms of one event are disjoint; dedup only lowers
the sum) and `δ ≥ δ_L`,
`𝔼[F−B] ≤ m_a²·S·4·2^{−k₀} ≤ S δ_L/(100(S+1)) ≤ δ/100`.

**Step 4 (cells, ℓ¹).** [SN] `lem:size`: `B` is a real combination of unit
cells on `≤ 3k+2t` free coordinates, so every modulus `d_i ≤ T^{3k+2t}` and is
supported on `𝒫`. [SN] `lem:l1` with `η = 1/99`: `μ := 𝔼B ≥ 0.99δ > 0` and
`A := 𝔼|B|/μ ≤ 1 + 2/99 < 1.03`.

**Step 5 (twist).** Let `ψ` be real primitive with conductor `f > 1`, `f | d_i`
for some `i`. Then `f | ∏ℓ^{e_ℓ}`, `ψ` is a product of characters `ψ_ℓ` of the
coordinates `X_ℓ`, `ℓ | f`, and as in [SN] `lem:twist`,
`μ_ψ := Σ_{i: f|d_i} c_iψ(b_i)/φ(d_i) = 𝔼[Bψ]`. So
`|μ_ψ| ≤ 𝔼[F−B] + |𝔼[Fψ]| ≤ δ/100 + δ/5 = 0.21δ ≤ 0.2122μ < μ/4`
(explicitly `0.21δ ≤ 0.2122μ`). (The paper's "`f` odd squarefree" is not
needed: one only uses that `ψ` factors over the coordinates.)

**Step 6 (transfer).** Let `R = max(T, Q, max_i d_i)` and pick a prime
`ℓ' ∈ (R, 2R]`; then `ℓ' ∤ QD` and `ℓ' ∉ 𝒫`. Put `Q' = Qℓ'` and let `a'` be the
class `≡ a (Q)`, `≡ 1 (ℓ')`. Apply [SN] `thm:transfer` with `(Q', a')` in
place of `(Q, 1)` and target `1[n ∈ no E_i]` in place of `1[W(n)>T]`. Its proof
uses about the target only the pointwise inequality `B ≤ target` on
`n ≡ a' (Q')`, `gcd(n,D)=1` (Step 2). The change `1 ↦ a'`: every coefficient
acquires the factor `χ̄_{Q'}(a')` of modulus 1, which is harmless in Case 0 and
in Case B (only `|c(χ)|` is used). In Case A (`χ_D` principal, `χ = χ_1`
induced from a real character mod `Q'`), `c(χ) = χ_1(a')μ/φ(Q')` with
`χ_1(a') = ±1`; for `+1` the proof is verbatim, for `−1` the main terms
combine to `(1 + x^{β_1−1}/β_1)μx/φ(Q') ≥ μx/φ(Q')`, which is better.
Hypotheses: `gcd(d_i,Q') = 1`, `b_i` units (Step 4), twist (Step 5),
`A ≤ 1.03 ≤ Z^{1/4}`. With `Z = Q'·max d_i`,
`log Z ≤ 2log Q + 2(3k+2t)log T + log 2`, the theorem yields a prime
`p ≤ x`, `log x = C₂(1+log 1.03)log Z`, with `p ≡ a' (Q')`, `p ∤ D`,
`B(p) > 0`. Then `F(p) = 1`, i.e. `p` lies in no `E_i`, and `p > ℓ' > T`
since `ℓ' | p−1`. This proves Theorem 1.1 with `C₇ = 2C₂(1+log1.03)+1`. ∎

*Proof of Lemma 1.2.* Fix `ψ` as in (Tw) and a prime `ℓ₀ | f` such that the
`ℓ₀`-component `ψ₀` of `ψ` is a nontrivial character of `X_{ℓ₀}` (exists as
`f > 1`). Let `F'` be the avoidance indicator of the events not containing
`ℓ₀`. Given `X_{−ℓ₀}`, `F = F'·1[X_{ℓ₀} ∉ Forb(X_{−ℓ₀})]`, where `Forb` is the
set of values of `X_{ℓ₀}` putting `n` into some `E_i ∋ ℓ₀`. As `𝔼_{X_{ℓ₀}}ψ₀ = 0`,
`|𝔼[Fψ]| = |𝔼[F'·∏_{ℓ≠ℓ₀}ψ_ℓ·𝔼_{X_{ℓ₀}}[ψ₀1_{Forb}]]| ≤ 𝔼[F'·ℙ_{X_{ℓ₀}}(Forb)]
≤ Σ_{i∋ℓ₀} ℙ(F'=1, E_i) ≤ 𝔼F'·Σ_{i∋ℓ₀} ℙ(E_i)∏_{j∼i}(1−x_j)^{−1} = η_{ℓ₀}𝔼F'`,
by the conditional local lemma ([SN] `lem:lll`, second part, applied to the
subfamily defining `F'` — the (LLL) hypothesis passes to subfamilies — with
`B = E_i`, whose `Γ(E_i)` in the subfamily is contained in `{j ∼ i}`).
Likewise `𝔼F' − 𝔼F = 𝔼[F'ℙ_{X_{ℓ₀}}(Forb)] ≤ η_{ℓ₀}𝔼F'`, so
`𝔼F' ≤ δ/(1−η_{ℓ₀})`. With `η_{ℓ₀} ≤ 1/6`: `|𝔼[Fψ]| ≤ (1/5)δ`. ∎

*Proof of Corollary 1.3.* Take `x_i = 2ℙ(E_i) ≤ 2w_ℓ ≤ 1/32`. For each `i`,
`Σ_{j∼i} x_j ≤ 2Σ_{ℓ∈supp E_i} w_ℓ ≤ 1/32`, so `∏_{j∼i}(1−x_j) ≥ 31/32` and
`ℙ(E_i) ≤ x_i∏_{j∼i,j≠i}(1−x_j)` holds; `δ_L ≥ e^{−2.2S}` (`1−x ≥ e^{−1.1x}` on
`[0,1/32]`); `η_ℓ ≤ e^{1.1/32}w_ℓ ≤ 1.04/(64k) < 1/6`. Then
`k₀ ≤ 2k log₂(NT) + 3.2S + log₂(S+1) + 12 ≪ S + k log(4NT)` (as `k ≥ 1`),
`t ≪ k log(4NT)(S + k log(4NT))`, and Theorem 1.1 gives the bound (the
`3k log T` and `+1` terms are dominated). ∎

## 3. Remarks on the hypotheses

**3.1 (Any density lower bound will do; proved).** The local lemma enters the
proof of Theorem 1.1 only through `δ ≥ δ_L` in Step 3. So Theorem 1.1 holds
verbatim with `δ_L` replaced by *any* `δ_* ∈ (0, δ]` in `k₀` (still assuming
(Tw)). In particular Haar-side density bounds obtained by other methods
(sieve, distortion method, exact computation) transfer as well.

**Lemma 3.2 (Haar-side criterion for (Tw); proved).** For `ℓ₀ ∈ 𝒫` let
`δ^{(ℓ₀)}` be the Haar density of the set avoiding all `E_i` with
`ℓ₀ ∉ supp E_i`. If `δ^{(ℓ₀)} ≤ (6/5)δ` for every `ℓ₀ ∈ 𝒫`, then (Tw) holds.
*Proof.* In the proof of Lemma 1.2 the first chain gives
`|𝔼[Fψ]| ≤ 𝔼[F'·ℙ_{X_{ℓ₀}}(Forb)] = 𝔼F' − 𝔼F = δ^{(ℓ₀)} − δ ≤ δ/5`. ∎
(Lemma 1.2 is the special case where the local lemma certifies this.) So
(Tw) is implied by: *no single free prime carries more than a 1/6 share of the
avoidance constraint.* It is a Haar statement, checkable exactly by computer
for toy systems (`scripts/transfer_toy.py`, §6).

**3.3 (Role of the exceptional zero).** No Siegel-zero hypothesis is made.
The possible exceptional real character `χ₁` (unique for conductors
`≤ Q_G = x^{1/(κL)}`) is handled in two ways ([SN] `thm:transfer`):
(A) if `χ₁` lives on `Q'` (the fixed part), it multiplies the main term by
`λ = 1 ∓ x^{β₁−1}/β₁`; `λ ≥ min(u,1)/2` and the effective Page bound
`1−β₁ ≫ q₁^{−1/2}(log q₁)^{−2}` only serve to absorb the conductor-drop error
`R₁ ≪ AZ³μ`. (B) if `χ₁` has a component on the free primes, its coefficient
is the twisted mean `μ_ψ/φ(Q')`, and (Tw) makes it `≤ μ/4`. Case B cannot
be treated like Case A *by this argument*: the error `(A−1)μ` from `|c(χ)| ≤ Aμ/φ(Q')` would have to be `≤ λμ`
with `λ` possibly as small as `≍ Z^{−1/2}` (Page scale)
; since `A−1` is only controlled through `𝔼[F−B] ≈ 2^{−k₀}`, this needs
`2^{−k₀} ≤ Z^{−1/2}`, i.e. `k₀ ≫ log Z ≍ t log T = 10kbk₀ log T`,
impossible. So (Tw) is the price of not assuming "no exceptional zero". If
one assumes that no real primitive character of conductor `≤ x` has a zero
in `[1 − 1/(κ log Q_G), 1)` (e.g. GRH for quadratic characters), (Tw) can be
dropped (Case 0 always applies). *Assessment:* whether (Tw) is genuinely
needed for the conclusion (rather than for the proof) is unclear; without it
a Siegel zero for `ψ` biases small primes towards `ψ(p) = −1`, which hurts
exactly when `F` concentrates on `ψ = +1`.

**3.4 (Where the losses are; Assessment).** Write `ℒ = log(1/δ_*)`. Heuristic
truth (random model): `log p ≈ log Q + ℒ + O(log T)`. Theorem 1.1 gives
```
log p ≪ log Q + k·log T·log(NT)·(ℒ + k·log(NT) + log(S+2)).
```
Losses: (i) `log T` per cell prime (cell moduli are products of
`≤ 3k+2t` prime powers `≤ T`); (ii) the bit width `b = log₂(4NT)` from the
binary encoding before the switching lemma; (iii) the factor `k` (DNF width
`kb`); (iv) `k log(NT)` in `k₀` from `log m_a²` (the Cauchy–Schwarz `m²` of
the BRW sandwich after splitting into atoms). Loss (ii) would disappear with a
switching lemma for product spaces with alphabet `T` directly (not checked;
we do not claim such a lemma is available). For `k = 1` (sifted sets) the
theorem is presumably far from optimal: a prime-local system is a sifted set,
and we expect (but have not worked out) a bound of the shape
`log Q + log T + ℒ` from sieve + Linnik-type arguments ([SN] cites EGLNV for
the "combinatorial rectangle" analogue on the independence side).

## 4. Comparison with known results (honest scope)

Checked sources: only `sources/` and `LITERATURE_2026.md` (no internet). Items
marked *[memory]* are from memory / the bibliography of [SN] (whose own
bibliographic details for these items are flagged "from memory" there) and
have **not** been checked against the papers.

**4.1 Linnik / Thorner–Zaman (single class).** For one class `c mod q`:
`p ≪ q^{L}` (Linnik), so avoidance via a single surviving class modulo
`Q·D₀` gives `log p ≪ log Q + log D₀`, `log D₀ = Σ_{ℓ∈𝒫} e_ℓ log ℓ`. Thorner–
Zaman's refinement (arXiv:2108.10878, in `sources/lit2026/`) applied cell by
cell to a signed minorant (the route of POINTWISE_OMEGA2/OMEGA8 v1) costs
`log x ≫ K·max(log Z, K)`, `K = 1 + log(Σ|c_i|/φ(d_i) / μ)` ([SN] Rem.
`rem:linear`) — the `ℓ¹` *mass* of the cell expansion, not `𝔼|B|`, enters,
which squares the final exponent (14 vs 7 in the ES application).
Theorem 1.1 instead depends only on `A = 𝔼|B|/μ ≤ 1.03` and the largest cell
modulus. **Gain:** `log D₀ ≍ N log T` is replaced by
`k log T log(NT)(ℒ + k log(NT))`; useful exactly when `N` (number of free
primes) is much larger than the local complexity.

**4.2 Least prime in a union of classes / Chebotarev** *[memory]*
(Lagarias–Montgomery–Odlyzko 1979; Thorner–Zaman 2017 explicit). The set
avoiding the system is a union of classes mod `Q·D₀`, i.e. a union of
Frobenius classes in `ℚ(ζ_{QD₀})/ℚ`. LMO-type bounds are powers of the
*discriminant*; for cyclotomic fields `log d_L ≍ φ(q) log q`, so they give only
`log p ≪ φ(QD₀)log(QD₀)` — worse than Linnik. Conductor-based (abelian, Hecke
= Dirichlet) versions give `log p ≪ log(QD₀)`. We do not know a
version of them whose exponent improves with the *structure* (bounded-width
events) of the set rather than its density. We could not check whether such
structure-sensitive bounds exist in the literature.

**4.3 Jacobsthal-type (integers).** Iwaniec's bound (secondary-source verified
in `sources/jacobsthal-literature/`, Costello–Watts): every interval of length
`≪ (k log k)²` contains an integer avoiding one prescribed class at each of
`k` primes. This is the `k = 1`, one-class-per-prime case and for **integers**;
for integers the least avoider of any finite system is trivially bounded by
CRT. The prime analogue (least *prime* avoiding the system) is what
Theorem 1.1 addresses; Ford–Konyagin–Maynard–Pomerance–Tao (sieved sets, in
`sources/`) treat bounded numbers of classes per prime and prove *lower*
bounds (long gaps); they give no upper bound for composite-modulus systems
(per the README there).

**4.4 Covering systems** *[memory]*. Erdős–Selfridge type questions; Filaseta–
Ford–Konyagin–Pomerance–Yu (JAMS 2007) use the local lemma for lower bounds on
the uncovered density; Hough (Annals 2015) solved the minimum-modulus problem;
Balister–Bollobás–Morris–Sahasrabudhe–Tiba (Invent. 2022) developed the
"distortion method" for the density of the uncovered set. All these are
**Haar-side** statements (density of integers not covered). By Remark 3.1
any such lower bound `δ_*` can be fed into Theorem 1.1 — subject to (Tw), to
working on units (non-unit classes deleted; the *unit* density is what
matters), and to `k ≤ log₂ X`, `T ≤ X` for moduli `≤ X`. We did not check the
exact hypotheses/forms of these density bounds, so we state no corollary
quoting them; Remark 3.1 is the generic form with `δ_*` as input.

**4.5 Independence side.** The sandwich is Bazzi/Razborov; "polylog
independence fools DNF/AC⁰" (Bazzi, Razborov, Braverman) *[memory]*. The
transfer principle here is: *a Dirichlet-character expansion of a sandwich
minorant with small Haar `ℓ¹` norm makes primes "fool" bounded-width
congruence DNFs, at cost polynomial in the width.* We know of no prior
statement of this form, but our search was limited to the above; no priority
claim. Novelty audit for the underlying ES application:
`reviews/novelty-audit-omega8.md`.

**4.6 Other benchmarks: coarsening, quarantine, Bonferroni (Assessment).**
Three cheaper competitors use the same transfer ([SN] `thm:transfer`, cost
`log Q + log(max modulus)` when `A = O(1)`):

* **(C) Coarsen + union bound.** Replace each event by a superset (e.g. a
  sub-cell on fewer primes). If the coarsened system has mass `S_c ≤ 1/5`,
  the minorant `1 − Σ 1_{E^c_i}` has `μ ≥ 4/5`, `A ≤ 1 + 2S_c/μ ≤ 2` and the transfer gives
  `log p ≪ log Q + k log T` (no Siegel issue: twisted means are `≤ S_c ≤ μ/4`, so the twist condition holds).
* **(Q) Quarantine.** Add a prime set `Π'` to `Q` and choose the target class
  so that the events through `Π'` are decided; cost `Σ_{ℓ∈Π'} e_ℓ log ℓ`.
* **(B) Bonferroni.** Odd truncation `B_j = Σ_{i≤j}(−1)^iC(N,i)`
  (`N` = number of events containing `n`). Pointwise
  `B_j = 1[N=0] − C(N−1,j)1[N≥1] ≤ F`, so `𝔼|B_j| = δ + 𝔼[C(N−1,j);N≥1]`, and
  the transfer gives `log p ≪ log Q + jk log T` once
  `𝔼[C(N−1,j);N≥1] ≤ δ/100` (plus twist bounds). For codegree-spread systems
  (`𝔼C(N,i) ≤ (cS)^i/i!`) `j ≍ S + log(1/δ)` suffices:
  `log p ≪ log Q + k(S + ℒ)log T`, **better than Theorem 1.1** by `≈ log(NT)`.
  In general `𝔼C(N,i)` depends on codegrees, not on `S` and `w_ℓ`.

Combinations (Q)+(C)+(B) are the natural benchmark.

*Hub examples do not separate Theorem 1.1 from this benchmark.* (i) Single
or multiple hubs (events `E'_{h,j} ∩ {X_{ℓ_h} = σ_h}`, cluster mass
`S' = q₀/(128k)`, `3k ≤ H ≤ q₀/100`): plain Bonferroni needs `j ≳ S' ≍ q₀/k`
(heuristic Poisson computation), but (Q) on the `H` hubs kills every event
at cost `H log T`, which beats Corollary 1.3's
`≳ (H/128)log T log(4NT) + k² log T log²(4NT)` (R42 MAJOR-1; my earlier
claim that this example shows an advantage was wrong). (ii) Pair-hubs on a
matching (`H` disjoint prime pairs `(a_h,b_h)`, `|G| = q`, hub cell of mass
`q^{−2}`, cluster mass `S' ≈ q` so that `S = O(1)`): now (Q) costs `≍ H log T`
and plain (B) costs `≍ (q²/H)k log T`, so for `H ≍ q ≫ k² log²(NT)` both exceed
Theorem 1.1's `≍ k² log T log²(NT)` — but (C) wins: replacing each cluster by
its hub cell gives mass `H/q² ≍ 1/q ≤ 1/5`, hence `log p ≪ k log T`.
More generally, any heavy cluster sitting on a common sub-cell is beaten by
coarsening to that sub-cell or quarantining it.

**Status: no system is known to us on which Theorem 1.1 provably beats the
best combination of (Q), (C), (B).** A separating example would need every
coarsening to keep mass `≫ 1`, every killing quarantine set to be large, and
`𝔼C(N,j)` to stay large up to depth `≫ log T·log(NT)·(S + k log NT)/S`; we have
not constructed or ruled out such a system. For the ES witness system itself
we have not computed what (Q)+(C)+(B) would give; [SN] reports that the
alternating (Bonferroni-type) expansion of POINTWISE_OMEGA2, *with* its
quarantine, was limited to fixed powers of `log p`, which is evidence (not
proof) that the sandwich helps there. Theorem 1.1's distinguishing feature
is that it needs **no** codegree information and no choice of coarsening or
quarantine beyond `w_ℓ ≤ 1/(64k)`; whether that ever buys more than
bookkeeping convenience is open.

## 5. Applications

### 5.1 The witness modulus for m/n (Sierpiński m = 5 and general m)

Fix an integer `m ≥ 4`. For `M ≡ −1 (mod m)`, `M ≥ 3`, put `A_M = (M+1)/m`
(so `gcd(A_M, M) = 1`, `mA_M ≡ 1 (M)`). If `uvw = A_M`,
`n ≡ −uv^{−1} (mod M)` and `s = (nv+u)/M`, then (direct verification:
`nv+u+s = m·suvw` ⇔ `s(m·uvw−1) = nv+u`)
```
m/n = 1/(suw) + 1/(nsvw) + 1/(nuvw).                      (5.1)
```
These are Type II solutions (`n | y, z`) in the parametrisation of
Elsholtz–Tao §2 with `4 ↦ m` (ET: `e(macd−1) = n + m a²d`, i.e. `M = macd−1`,
class `−m a²d`; ET Remark 1.10 notes their analysis extends to numerators
`m ≠ 4`, "considered first by Sierpiński and Schinzel"). Define
```
W_m(n) = min{ M ≡ −1 (m), M ≥ 3 : n mod M ∈ R_m(M) },  R_m(M) = {−mD mod M : D | A_M²}.
```

**Lemma 5.0 (completeness of (5.1) for Type II; proved — proof due to the R42
reviewer, `reviews/pointwise-transfer-review.md`, MINOR-1).** Let
`m/n = 1/x + 1/(ny') + 1/(nz')` with `gcd(x,n) = 1` (for prime `n > m ≥ 4`
this covers every solution with exactly two denominators divisible by `n`;
all three is impossible as it would force `m ≤ 3`). Then the solution has
the form (5.1); in particular `n mod M ∈ R_m(M)` for `M = m·uvw − 1`.
*Proof (R42).* Put `w = gcd(x,y',z')`, `x = wX`, `y' = wY`, `z' = wZ`. Then
`m·wXYZ = nYZ + XY + XZ`, so `X | nYZ`, hence `X | YZ` (`gcd(X,n) = 1`); likewise
`Y | XZ`, `Z | XY`. As `X,Y,Z` have no common prime, at each prime one exponent
vanishes and the other two are equal, so `X = su`, `Y = sv`, `Z = uv`.
Dividing by `suv`: `m·suvw = nv + s + u`, i.e. `s(m·uvw − 1) = nv + u`, which
is (5.1). ∎ (This is ET Prop 2.6's argument, numerator-independent.)
Machine check by the reviewer: `scripts/review_tr_typeII.py` (branch
`side-agent/review-transfer`) enumerates all solutions of `m/n` for
`m ∈ {4,5,6,7}`, primes `n ≤ 400`, and `m ∈ {8,11}`, `n ≤ 250`; every Type II
solution has the form (5.1). **Consequence:** for prime `p > m`, `W_m(p) > T`
iff `m/p` has no solution with exactly two denominators divisible by `p` and
`m·uvw − 1 ≤ T` — so Cor 5.2 concerns *all* Type II solutions of `m/p`.

**Lemma 5.1 (atoms and class of one for m/n; proved, machine-checked for
`m ∈ {4,5,6,7,8,11}`, `M ≤ 3000`).** (i) `{−uv^{−1} mod M : uvw = A_M} = R_m(M)`;
(ii) `1 ∉ R_m(M)`; (iii) `D ↦ A_M²/D` preserves `gcd(M, mD+1)`.
*Proof.* (i) As [SN] `lem:atoms` with `4 ↦ m`: `v^{−1} ≡ muw`, so
`−uv^{−1} ≡ −m·u²w`, and every `D | A²` is `u²w` with `uvw = A`.
(ii) `−mD ≡ 1` ⇒ (× `A`) `D ≡ −A (M)`; `D ↦ A²/D` preserves this, so WLOG
`D ≤ A`, and then `0 < D + A ≤ 2A < mA − 1 = M` (as `m ≥ 4`, or `m = 3`,
`A ≥ 2`), contradicting `M | D + A`. (iii) If `q^a | M`, `q^a | mD+1`, then
`D ≡ −A (q^a)` and `A²/D ≡ −A`, so `q^a | m·A²/D + 1`; symmetric. ∎
(`scripts/transfer_mn.py`.)

**Corollary 5.2 (proved modulo G+H and ET Prop 1.4 with `κ = m`).** For each
fixed `m ≥ 4` there is `c_m > 0` such that for every large `T` there is a
prime `p ≡ 1 (mod lcm(1..⌊(log T)²⌋))` with `p > T`, `W_m(p) > T` and
`log p ≤ C_m (log T)^7`. Hence `W_m(p) ≥ exp(c_m(log p)^{1/7})` for infinitely
many primes `p`. Without ET Prop 1.4: `log W_m(p) ≥ (1/log2 − o(1))
log log p·log log log p` i.o. (proved modulo G+H).

*Proof.* Repeat [SN] §2 with `4 ↦ m`, `M ≡ 3 (4) ↦ M ≡ −1 (m)`:
atoms `(M,D)`, survival `m_Π | mD+1`, events `n ≡ −mD (mod r_Π)` (unit
classes on free primes, `≤ k = ⌊ℒ/log z⌋` of them). Mass bound
(`lem:qmass`): with `g = gcd(M, mD+1)`, `D = sr²`, `A = srh`,
`M = msrh − 1 ≥ (m−1)srh`: Lemma 5.1(iii) gives the `D ≤ A` reduction,
`g | gcd(msr²+1, r+h)` (from `g | msr(r+h)`, `gcd(g, msr) = 1`), and
ET Prop 1.4 with `κ = m` bounds `Σ τ(msr²+1)` exactly as for `κ = 4`; so
`S*_m ≪_m ℒ⁴ log ℒ` (and `S*_m ≤ exp((log2+o(1))ℒ/log ℒ)` unconditionally).
Iterated quarantine (`lem:iterq`, unchanged) with `z = ℒ²`, `c₀ = 1/(64k)`.
Reduction (`lem:system`(iv)) uses Lemma 5.1(i),(ii) in place of
`lem:atoms`, `lem:one`. Now apply Corollary 1.3 with `Q = Q_Π`, `a = 1`,
`N ≤ T`, `S ≤ S*_m`: `log p ≪ log Q_Π + k ℒ²(S*_m + kℒ)`, with
`log Q_Π ≪ (π(z) + k²S*_m)ℒ ≪ ℒ⁷/log ℒ` and
`kℒ²(S*_m + kℒ) ≪ (ℒ/log ℒ)·ℒ²·ℒ⁴log ℒ = ℒ⁷`. Unconditional version as in
[SN] Thm `thm:uncond`. ∎

*Remarks.* (a) For `m = 4` this is [SN] Thm 1 (the hard-prime condition
`p ≡ 1 (840)` is automatic as `840 | lcm(1..ℒ²)`). (b) The only `m`-specific
inputs are Lemma 5.1 and the `κ = m` case of ET Prop 1.4; the `log(1+κ)` factor
affects the `m`-dependence of the constants, which we do not track. (c) As for
`m = 4`, this is an Ω-result for *one explicit family*; it says nothing about
solvability of `m/p` (other representations may exist). The heuristic
truth for `m = 4` is `log W ≍ (log p)^{1/3}` (POINTWISE_SIZE §7); we have not
redone that heuristic for general `m`.

### 5.2 Generic witness-modulus Ω-theorem (application (c))

Let `R(M)` (`M ≥ 2`) be any family of sets of **unit** classes mod `M` with
`1 ∉ R(M)` for all `M`, and `W_R(n) = min{M : n mod M ∈ R(M)}`. Put
```
S^♮(T) = Σ_{M ≤ T} Σ_{r ∈ R(M)} gcd(M, r−1)/φ(M).
```
**Corollary 5.3 (proved modulo G+H).** If `S^♮(T) ≤ (log T)^α` for all large
`T` (some fixed `α ≥ 0`), then for every large `T` there is a prime
`p ≡ 1 (mod lcm(1..⌊(log T)²⌋))`, `p > T`, with `W_R(p) > T` and
`log p ≪_α (log T)^β/log log T`, where `β = max(α+3, 5)`. Hence
`W_R(p) ≥ exp(c_α (log p log log p)^{1/β})` ≥ `exp(c(log p)^{1/β})`
for infinitely many primes. If only `log S^♮(T) ≤ σ(T)`, then
`log log p ≤ σ(T) + O(log log T)`.

*Proof.* [SN] §2 abstracted: `z = ℒ²`, `k = ⌊ℒ/log z⌋`. An *atom* is `(M,r)`,
`r ∈ R(M)`; for a prime set `Π ⊇ {ℓ ≤ z}`, `M = m_Π r_Π`, the atom survives if
`r ≡ 1 (m_Π)` and `r_Π > 1`, giving the event `n ≡ r (mod r_Π)` on `≤ k`
free primes (prime factors `> z` of `M ≤ T`), weight `1/φ(r_Π) ≤ m_Π/φ(M) ≤
gcd(M,r−1)/φ(M)`. So `S ≤ S* ≤ S^♮(T)` for every `Π` (this is the first line
of `lem:qmass`). Iterated quarantine (`lem:iterq`, verbatim) gives `Π` with
`|Π∖{ℓ≤z}| ≤ 64k²S^♮` and `w_ℓ ≤ 1/(64k)`. Reduction: if `n ≡ 1 (Q_Π)` and
`n mod M ∈ R(M)`, `M ≤ T`, then `r := n mod M ≡ 1 (m_Π)`; `r_Π = 1` would give
`1 ∈ R(M)`; so `n` lies in a surviving event. Corollary 1.3 with
`Q = Q_Π`, `a = 1`: `log p ≪ (π(z) + k²S^♮)ℒ + kℒ²(S^♮ + kℒ)
≪ ℒ^{α+3}/log ℒ + ℒ⁵/(log ℒ)² ≪ ℒ^β/log ℒ` (the `π(z)ℒ ≪ ℒ³/log ℒ` term is
dominated; the `ℒ⁵` term is `kℒ²·kℒ`, from `log m_a` in `k₀`, and dominates
for `α < 2`). Then `ℒ^β ≫ log p·log ℒ ≫ log p·log log p`. ∎

*Remarks.* (i) ES: `R(M) = {−4D : D | A_M²}` for `M ≡ 3 (4)` (empty
otherwise). The proof of [SN] `lem:qmass` bounds exactly `S^♮`:
`S^♮ ≪ log ℒ·Σ g/M ≪ ℒ⁴ log ℒ` (mod ET Prop 1.4). With `S^♮ ≪ ℒ⁴log ℒ` the
displayed computation gives `log p ≪ ℒ⁷` (the `log ℒ` cancels), i.e. [SN]
Thm 1 / exponent `1/7`; Corollary 5.2 (`m/n`) is the case
`R(M) = R_m(M)`. Any family whose mass is `ℒ^{α}` gets exponent `1/(α+3)`.
(ii) Trivial baseline: Linnik with `p ≡ 1 (lcm(1..T))` gives only
`W_R(p) ≫ log p`; the corollary needs only polylog *mass*, no structure.

### 5.3 Prime Jacobsthal-type statements (application (b))

**Corollary 5.4 (composite-modulus prime avoidance; proved modulo G+H).**
Let `y ≥ 2`, `T ≥ y`, and let `𝒟` be a set of moduli `d`, each a product of
`≤ k` prime powers `ℓ^a ≤ T` with `ℓ ∈ (y, T]`, each `d` carrying a set `R_d`
of unit classes. Let `Q` be coprime to all `d`, `a` a unit mod `Q`, and
suppose `Σ_{d∈𝒟: ℓ|d} |R_d|/φ(d) ≤ 1/(64k)` for every prime `ℓ`. Then there
is a prime `p ≡ a (Q)`, `p > T`, with `p mod d ∉ R_d` for all `d ∈ 𝒟`, and
`log p ≪ log Q + k(log T)²(S + k log T)`, `S = Σ_d |R_d|/φ(d)`.
*Proof.* Corollary 1.3 with `𝒫` = primes in `(y,T]` dividing some `d`
(`N ≤ T`), `e_ℓ` = max exponent, and one event per `d` (the lift of `R_d`
to `∏_{ℓ|d}G_ℓ`; same Haar weight). ∎

*Instances.* (1) Shifted primes with forbidden residue patterns: for
`h₁,…,h_r` and moduli `d = q₁q₂` of two primes in `(y,T]`, forbid
`p + h_i ≡ c_{i,d} (mod d)` for prescribed unit classes `c_{i,d}`;
(2) "p + h avoids small prime factors in prescribed classes", e.g. no prime
factor `q ≡ 1 (4)`, `q ∈ (y,T]`, of `p + h` (`k = 1`, `R_q = {−h}`).

**Honest scope.** (a) If `S ≤ 1/3` and `Q` is small (Siegel–Walfisz range), the union bound
with Brun–Titchmarsh already gives a prime with `log p ≪ log Q + k log T`
(for large `Q` the Linnik-range lower bound for `π(x;Q,a)` may lose a
Siegel factor; not pursued); Corollary 5.4 is only of
interest for `S ≫ 1`, where the avoiding set may have density as small as `e^{−Θ(S)}`.
(b) For `k = 1` (instance 2, and any "`p + h_i` free of primes from a set"
condition), the avoiding set is a sifted set and classical lower-bound sieves
with Bombieri–Vinogradov (Halberstam–Richert-type almost-prime results,
*[memory]*) give, for small fixed `Q` and bounded `r`, `p ≤ T^{O(1)}`, i.e. `log p ≪ log T`, far
better than `(log T)³`. *Monotone* events ("`d | p + h`") reduce to `k = 1`
(avoid one prime factor of each `d`) and are likewise sieve territory.
(c) *Assessment (unverified).* The theorem can only be of interest for
non-monotone, composite-modulus events with `S ≫ 1` that resist cheap
coarsening and quarantine and have large codegrees; for such systems no sieve
(the avoiding set is not a product set) applies directly, and Linnik on a
single class costs `log ∏ℓ^{e_ℓ} ≍ N log T`. But §4.6: we know **no** system
on which Theorem 1.1 provably beats quarantine + coarsening + Bonferroni with
the same Gallagher transfer, and we have not checked whether the ES witness
system is such a system (the POINTWISE_OMEGA2 experience is only evidence).
(d) We did not find (in `sources/`) a prior "least prime avoiding a
composite-modulus congruence system" bound with polylogarithmic dependence
on the local data; see §4 for what we could not check.

## 6. Toy checks and Replay

* `scripts/transfer_mn.py` (stdlib, ~10 s): Lemma 5.1 (i)–(iii) and identity
  (5.1) for `m ∈ {4,5,6,7,8,11}`, all `M ≤ 3000`, `M ≡ −1 (m)`. All pass.
* `scripts/transfer_toy.py` (numpy, ~1 min): exact Haar computations on
  `∏_{ℓ∈{5,7,11,13,17}}(ℤ/ℓ)^×` (46080 points) for 6 random systems of
  *general* events (width ≤ 2, up to 4 classes per event, 15–30 atoms),
  `t ∈ {1,2,3}`. Asserted and passing: `B ≤ F` pointwise; the identity
  `F − B = Σ_i A_i(Σ_{j<i}A_je_j)²`; `𝔼[F−B] ≤ m_a²Σ_jℙ(C_j)En(F^{(j)};t)`;
  `𝔼|B| ≤ 𝔼B + 2𝔼[F−B]`; and the Lemma 3.2 chain
  `|𝔼[Fψ]| ≤ δ^{(ℓ₀)} − δ` for all 31 real primitive `ψ` and all `ℓ₀ | f`.
  Observed `A = 𝔼|B|/𝔼B ∈ [1, 1.23]` at `t = 1`, `∈ [1, 1.0022]` at `t ≥ 2` (the
  toy has only 5 coordinates). Seed 2 has `max_ψ |𝔼[Fψ]|/δ = 1.0`: a width-1
  event forbidding both non-residues mod 5 puts `F` on `ψ₅ = +1` — (Tw)
  fails there. Heavy local mass (`w₅ = 1/2`) can, but need not, break (Tw)
  (forbidding `{1,2}` mod 5 keeps the quadratic twist 0); Lemmas 1.2/3.2 are sufficient conditions only. The least-prime
  column is a sanity check only (all systems are tiny).

Replay:
```
PYTHONPATH=scripts uv run python scripts/transfer_mn.py
ulimit -v 8000000; PYTHONPATH=scripts timeout 600 uv run --with numpy python scripts/transfer_toy.py
```

## 7. Status summary

* Theorem 1.1, Corollary 1.3, Corollaries 5.2–5.4: **PROVED modulo G+H**
  (Gallagher's theorem as quoted from the MV3 draft with Landau–Page, and
  Håstad's switching lemma); Cor. 5.2 also modulo ET Prop 1.4 (`κ = m`), its
  weaker version without. All proofs are re-assemblies of [SN] lemmas; the
  new content is the abstraction (arbitrary events; atoms only inside the
  sandwich; general target class; any density lower bound; Haar criterion
  Lemma 3.2 for (Tw); `f` need not be squarefree) and the `m/n` and generic
  witness-family corollaries.
* Lemma 1.2, Lemma 3.2, Lemma 5.1: **PROVED** (5.1 also machine-checked).
* §3.3, §3.4, §4.6: **Assessment** (method comparisons, not theorems about
  least primes).
* Novelty: no priority claim. §4 lists exactly what was and was not checked.
