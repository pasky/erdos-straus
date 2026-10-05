# Hostile review of EXCEPTIONAL_LARGESIEVE3.md (task R59)

Reviewer branch `side-agent/review-ls3`; author branch `side-agent/hls-sparse`
(merged ff at review start). Scripts: `scripts/review_ls3_*.py` (from scratch).

## Verdict summary

| claim | verdict |
|---|---|
| Thm 1.1 | SOUND (Rem 1.1(a) overclaims: D2) |
| §4 "equivalence" | GAP: only sufficiency proved (D1) |
| Lemma 2.1 | SOUND (minor D6) |
| Thm 3.1 | SOUND (conditional on reviewed internal K2 inputs + ElT Prop 1.4, as labelled) |
| Lemma 4.1 | SOUND |
| Lemma 4.2 | SOUND (computation); "symmetric route fails" is Assessment (D3) |
| §4.3 | Assessment, correctly labelled; the ℓ² Parseval peeling identity re-derived (correct) |

## Claim-by-claim

### Thm 1.1 (smooth–rough splitting): SOUND

Re-derived line by line.
* Decomposition `𝒜 mod M₀ = {(c,r): c∈𝒜_s, r∈𝒜_c}`: a class `b mod G` with
  `G_r>1` contains `(c,r)` iff `c≡b (G_s)` and `r≡b (G_r)`; correct.
* HY step: with `f(c)=M_sπ_s(c)π̂_c(θ_r)` one has `f̂(θ_s)=π̂(θ_s+θ_r)`;
  HY on `ℤ/M_s` (normalised Haar on the group, counting measure on the dual,
  `1<p≤2`) gives `‖f̂‖_{p'} ≤ ‖f‖_{L^p}`;
  `E_c|f|^p = Σ_cπ_s(c)(M_sπ_s(c))^{p−1}|π̂_c|^p ≤ ρ^{p−1}E_{π_s}|π̂_c|^p`;
  `(p−1)p'/p = 1` (since `p' = p/(p−1)`), so the density enters exactly to the
  first power; Jensen `(E X^p)^{p'/p} ≤ E X^{p'}` as `p'/p ≥ 1`. Correct.
  Non-uniformity of π_s is harmless: only `sup π_s ≤ ρ/M_s` is used.
* Hölder: `|π̂|² = |π̂|^{p'/(1+β)}` and
  `Σ w|π̂|² = Σ w^{β/(1+β)}(w|π̂|^{p'})^{1/(1+β)}`; correct. `Σw≤1` (LS Fact
  4.0), `w≤1/N` (LS Fact 1.1), distinct θ, `π̂=0` off `den θ | M₀` (π lifted
  uniformly on unresolved digits, LS Rem 3.3 sharpening). Correct.
* Final algebra `log(N/B) ≤ (β log N + log 𝓡)/(1+β)` checked.
* Brute force (from scratch): `scripts/review_ls3_thm11.py` — see §Numerics.

Remark 1.1(c) (level-split form): re-derived. Low part: Cauchy–Schwarz
`|E_π h|² ≤ E_π|h|² = Σ_cπ_s(c)E_{π_c}|h(c,·)|²`; for fixed c, `|h(c,·)|²` has
rough frequencies of rough level ≤ 2λ', so the comparison applies;
then `≤ e^{S_r}ρ E_U|h|² ≤ ρe^{S_r}/N` (LS2 Lemma 2.2, Δ=1). High part:
`|π̂(θ)| ≤ E_{π_s}|π̂_c(θ_r)| ≤ (e^{S_r}/N)^{1/2}` (no ρ). Total
`(ρ+1)e^{S_r}/N`, so `log(N/B) ≤ log ρ + S_r + log 2` (ρ ≥ 1). SOUND, but the
hypotheses must hold for **every** c in supp π_s (not on average, unlike the
Hölder form); the doc says this implicitly ("for c in a set of probability
≥ 7/8" in §4 is then absorbed through the event E of Lemma 2.1 — fine, but
see D2).

### Lemma 2.1 (density of the z-smooth part): SOUND (minor presentational gaps)

* Failure probabilities: leak `Σ_ℓ E[p_ℓ1{p_ℓ>ℓ^{−1/2}}] ≤ 1/8` bounds
  `Q'(∃ℓ: y_ℓ∈F_ℓ)` (light coordinates never land in F_ℓ); `Q'(∃ℓ:p_ℓ>1/2)
  ≤ Σ4Ep_ℓ²`; Markov; plus `Q'(E)≤1/8`: total ≤ 1/2. Correct.
* Support: on G every class with z-smooth modulus is avoided (W-smooth ones
  by K2 Lemma 2.3(1); others are decided at their top prime ≤ z and can only
  be hit by `y_ℓ∈F_ℓ`). Classes with a prime > z are never activated at ℓ ≤ z.
  Correct.
* Density: `Q'(c) = base(c_W)·Π_{W<ℓ≤z}P(y_ℓ|past)`, each factor
  `≤ ℓ^{−E_ℓ}(1−p_ℓ)^{−1}` (light) or `= ℓ^{−E_ℓ}` (heavy);
  `−log(1−p) ≤ 2p` for `p ≤ 1/2` (true: `log 2 < 1`); conditioning on an event
  determined by c with probability ≥ 1/2 at most doubles. Correct.
* Inputs checked against K2: (Q1) = K2 §3 Step 1 + Cor 3.7 (`𝔐` is over the
  **universe** 𝔘, so uniform in 𝔊, `y ≥ y₀(W)`); (Q2),(Q3) = K2 Lemma 4.3
  ("every family 𝔊 ⊆ 𝔘", `C(W) ≤ C(log W)^c`, B-free); (Q4) = K2 §2 end
  (`γ'(ℓ) = (1−ℓ^{−1/2})^{−1}` from the caps); base = K2 Lemma 2.3(2). All
  match. K2 Thm 5.1 / Lemmas 2.3, 4.3 were reviewed SOUND
  (`reviews/exceptional-kary2-review-2.md`).
* Minor: see D6 (Q₀ vs M_s).

### Thm 3.1 (rough-slice mixtures): SOUND (conditional on K2 Cor 3.7, Lemma 4.3 — internal, reviewed; Case A via ElT Prop 1.4)

* "Fibre forbidden sets are exactly K2's activated sets at ℓ > z": a class
  with exactly one prime ℓ > z has top prime ℓ and z-smooth cofactor, so its
  activation depends on c only, and it is activated at ℓ iff c meets the
  cofactor class — i.e. iff its fibre class lies in `𝔊_c`. Correct. Hence
  `p^r_ℓ(c)` is a function of c with the Q'-law of K2's `p_ℓ`, and (Q2), (Q4)
  apply.
* `Q'(E₁) ≤ Σ_{ℓ>z}ℓ^{1/2}Cℓ^{−7/4}(log ℓ)^c ≪ z^{−1/4}(log z)^c`; Markov for
  E₂. Correct.
* Local bound: for uniform on the complement of a set of density p in
  `ℤ/ℓ^{E}` (lifted classes mod `ℓ^v`, v ≤ E), `|φ(a)| ≤ p/(1−p)` and
  `Σ_{a≠0}|φ|² = p/(1−p)` hold verbatim; `g^{1+2β} ≤ 2p·2^{2β}ℓ^{−2β(1−κ)}
  ≤ 4pℓ^{−α}`. Checked numerically (script).
* J: partial summation correct (boundary term `−z^{−α}𝔐(z) ≤ 0`,
  `𝔐(y)y^{−α} → 0`), `α∫_0^∞t³log³(e+t)e^{−αt}dt ≍ α^{−3}log³(1/α)` with
  `α = (log N)^{−1/4}/2`: gives `(log N)^{3/4}(log log N)³`. Correct.
* Assembly: `β log N = (log N)^{3/4}`, `16𝔐(z) ≤ 16K₃(log N)^{3/4}((1/4)log log N)³`,
  `64J`. Correct. N must be large enough that `z ≥ max(W₁, y₀)` and
  `Q'(E₁) ≤ 1/16`; implicit in "C".

### Lemma 4.1 (two-copy form): SOUND

`Σ_{a mod ℓ^E, a≢0}e(a(x−y)/ℓ^E) = ℓ^E1[x≡y (ℓ^E)] − 1` is right; the
product over S and the σ⊗σ average give `P_S`; Möbius/Parseval mod `M_T`
gives the collision identity; `|σ̂|^{2+2β} ≤ s_S^{2β}|σ̂|²` termwise.
Verified from scratch on random non-product measures mod `9·5·7` and
`4·3·5·7` (prime powers included), all S, β ∈ {0.05, 0.25, 0.5}:
`scripts/review_ls3_lemmas.py` (b).

### Lemma 4.2 (residue concentration): SOUND as a computation; the heading claim is an Assessment (D4)

* `−4 ∈ ℛ(M)`: definitional (K2 Def 2.0 / notes Lemma 18.1, `D = 1 | A²`).
  Re-verified forcedness from scratch through notes (16.1) with
  `u = w = 1, v = A`: for `n ≡ −4 (M)`, `s = (nA+1)/M ∈ ℤ` and
  `4/n = 1/s + 1/(nsA) + 1/(nA)` exactly, 959 pairs `(M,n)`, `M ≤ 159`.
  (A naive `x = kA` identity fails, e.g. `M = 3, n = 5` — irrelevant to
  the doc, noted only because it shows the check is not vacuous.)
* `m*(p,−4) = Σ_{M'}1/M' ≍ log X/log z`: correct up to the constant
  (`Σ_{M'≤X, z-rough}1/M' ~ e^{−γ}log X/log z`; the "half in the right class
  mod 4" is fine at the ≍ level). Numerically `1.91` vs `log X/log z = 4.27`
  for z = 30, X = 2·10⁶, p = 10007 — consistent with a constant `≈ 0.45`.
  Note: requires `M'` composite with many rough primes; with `X = N^A` this is
  allowed in the family.

## Numerics (from scratch, reviewer)

    ulimit -v 8000000
    timeout 600 uv run --with numpy python scripts/review_ls3_thm11.py
    timeout 900 uv run --with numpy python scripts/review_ls3_lemmas.py

* `review_ls3_thm11.py`: `M_s = 60`, `M_r = 7·11·13`; 180 random families
  of classes `b mod G`, `G | M₀` (**including multi-rough-prime classes**,
  which the author's check omits), correlated non-product π_s (random,
  heavy-tailed "spiky", uniform), fibre laws random or Dirac (worst case).
  Core inequality `𝓡_{p'}(π) ≤ ρE_{π_s}𝓡_{p'}(π_c)`: max ratio 0.970
  (spiky), **equality 1.000000** attained for π_s uniform on `ℤ/M_s` and a
  c-independent fibre law (so the constant ρ is sharp). π supported on 𝒜
  always. Hölder step with random weights (`w ≤ 1/N`, `Σw ≤ 1`): max ratio
  0.475.
* `review_ls3_lemmas.py`: (a) Lemma 4.2 forcedness + Mertens number; (b)
  Lemma 4.1; (c) Thm 3.1 local bound (`|φ| ≤ g`, Parseval `= g`,
  `Σ|φ|^{p'} ≤ g^{1+2β} ≤ 4pℓ^{−α}` for unions of classes mod `ℓ^v` in
  `ℤ/ℓ^E`, E ≤ 2): worst ratio 0.797.

## Defects

No FATAL defect. No error found in any PROVED proof (Thm 1.1, Lemma 2.1,
Thm 3.1, Lemmas 4.1, 4.2). The defects are scope/label overclaims in the
surrounding text and in the agent report.

**D1 (MAJOR, overclaim; §4 first paragraph and AGENT_REPORT_O59 item 4).**
"By Theorem 1.1 … H_LS∞ for forced families is now **equivalent** to …
(H_rough)" / report "H_LS∞ ⇔ (H_rough)". Only the direction
(H_rough) ⇒ cap is proved (Thm 1.1 / Rem 1.1(c) + Lemma 2.1). Nothing shows
that a cap (or LS2's H_LS∞, which asks for *one* π on 𝒜 with sup decay)
yields fibre measures π_c with the stated `ℓ^{p'}` or comparison property;
LS2 §5 itself records that the Hölder-type and sup-type criteria are
incomparable. *Repair:* replace "equivalent to" by "implied by" / "reduces
to (sufficient condition)", and "⇔" by "⇐" in the report and in any ledger
entry.

**D2 (MAJOR, overclaim; Rem 1.1(a) and AGENT_REPORT_O59 item 3).**
Rem 1.1(a): "the part of (E1) … coming from denominators with many prime
factors ≤ z is closed as soon as log ρ is small"; report: Thm 3.1 "closes
(E1) for all frequencies whose high level comes from primes
≤ exp((log N)^{1/4})". What is proved:
(i) for **rough-slice mixtures** (Thm 3.1), all frequencies; (ii) for an
**arbitrary** family, frequencies with **z-smooth denominators only**
(`θ_r = 0`): then `π̂(θ_s) = π̂_s(θ_s)` and HY gives
`Σ|π̂_s|^{p'} ≤ ρ` — *provided* `𝒜_c ≠ ∅` for all `c ∈ supp π_s`, which is
not guaranteed for families with multi-rough-prime classes (rough classes
can cover a whole fibre; Lemma 2.1's π_s does not see rough classes).
For mixed frequencies `θ_s + θ_r` with `θ_r ≠ 0` of small rough level in a
general family one still needs a fibre measure satisfying the rough-level
comparison of Rem 1.1(c)(a) for every `c ∈ supp π_s` — a K2-Lemma-1.1-type
statement for the fibre family `𝔊_c`, uniform in c (or on a set of
Q'-probability ≥ 7/8 absorbed into E), which is **not** proved (fibre
families are not of the four K2 types, and K2's first moments are only
averaged over c). *Repair:* state (i) and (ii) with the nonemptiness
proviso; label the general mixed-frequency statement CONJECTURE / part of
(H_rough).

**D3 (MINOR, label; §4.2 heading, text before Lemma 4.2, report item 4).**
"Why the symmetric (LLL/Kotecký–Preiss) route fails" and report "Lemma 4.2
(PROVED): the symmetric … route fails". Lemma 4.2 proves only that
`m*(p, −4 mod p) ≍ log X/log z` for the family `{−4 mod pM'}`; that the KP
criterion "needs, for each p and **each** b, `m*(p,b)` small" is a property
of one particular polymer model, and failure of a sufficient criterion is
not failure of the route (e.g. non-uniform activities, first conditioning
on the residues where concentration occurs, or polymers = rough primes
rather than classes). *Repair:* keep Lemma 4.2's computation as PROVED;
relabel the "route fails" conclusion as Assessment.

**D4 (MINOR, hidden hypothesis; §4 sparsity statements).** "average over b
this is the mass at p, ≪ (log N)^{O(1)}/p", the (Sp) statement, and §4.2's
"average influence ≪ Σ_{C∋p}1/G_r ≪ (log N)^{O(1)}/p" need a bound on the
moduli (e.g. `G ≤ N^A`): over the universe, `Σ_{M≡3(4), p|M}τ(A_M²)/M`
diverges. Theorem 3.1 (correctly) avoids this through top-prime smoothness
(𝔐 counts only ℓ-smooth cofactors), but §4 is stated for the same "any
moduli" setting. *Repair:* add "moduli ≤ N^{A}" to these Assessment
sentences (and to Lemma 4.2's family, which already has `M' ≤ X = N^A`).

**D5 (MINOR, wording; Rem 3.1(a), report item 3 "strictly extends LS Cor
4.2").** On Cor 4.2's own families Thm 3.1 is *weaker*: LS Cor 4.2 gives
`C'(C)(log N)^{3/4}` with no `(log log N)³`, Thm 3.1 has the Rankin loss
(acknowledged in Rem 3.1(b)). The extension is in scope (no `q₀ ≤ ℓ^C`,
no `ℓ₀'`), not in strength. *Repair:* "extends the scope of LS Cor 4.2 at
the price of `(log log N)³`"; optionally note that under bounded B
(`G ≤ P(G)^{1+B}`) K2 Thm 5.2's first moment `≤ C(B)(log y)³` should remove
the loss (not checked).

**D6 (MINOR, presentation; Lemma 2.1).** (a) K2's base lives mod
`Q₀ = lcm(8P_W, W-smooth parts of moduli)`, which need not divide `M_s`
(the `8P_W` factor); LS3 writes "`Q_W`" (undefined). π_s should be the
marginal on `ℤ/M_s` (or replace `M_s` by `lcm(M_s, Q₀)`); the density bound
is preserved by marginalisation. (b) The summary table says
"costs `≤ 2T₁ + O(1)`, `T₁ ≍ 𝔐(z)`" whereas Lemma 2.1 proves
`log ρ ≤ 16𝔐(z) + 2W₁ + log 2`; make them consistent. (c) Thm 1.1 tacitly
needs `𝒜_c ≠ ∅` for `c ∈ supp π_s` (automatic in Thm 3.1 since
`p^r_ℓ < 1` off E₁); say so.

**D7 (MINOR, numerics coverage).** The author's check (1) uses rough-slice
mixtures only, while Thm 1.1 is claimed for arbitrary fibre families. The
reviewer's `scripts/review_ls3_thm11.py` covers multi-rough-prime classes,
Dirac fibre laws and spiky π_s, and shows equality is attained (ρ sharp).
Optional: cite it or extend the author's script.

## Overall

Thm 1.1, Lemma 2.1, Thm 3.1 and Lemma 4.1 are SOUND as stated and labelled
(Thm 3.1 conditional on K2 Cor 3.7 / Lemma 4.3 — internal, reviewed SOUND —
and ElT Prop 1.4 for Case A; the "PROVED (same inputs)" label is honest).
Lemma 4.2 is a correct (essentially definitional) computation. The
"please check" items: HY with non-uniform base — correct, factor exactly ρ
and sharp; Lemma 2.1's use of K2 second moment and leak — correct; "fibre
forbidden sets are exactly K2's p_ℓ for ℓ > z" — correct (one rough prime ⇒
top prime with z-smooth cofactor); partial summation for J — correct.
Required before ledger entry: D1, D2 (overclaims of equivalence and of
closing (E1) beyond rough-slice mixtures / purely smooth frequencies).
