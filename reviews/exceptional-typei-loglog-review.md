# Hostile review R111 of EXCEPTIONAL_TYPEI_LOGLOG.md (O111, branch side-agent/heegner-typei)

Reviewer: side-agent/review-ttl. Scope: all claims of AGENT_REPORT_O111.md, with emphasis on the R1
repairs (not re-reviewed by the author). From-scratch scripts: `scripts/review_ttl_*.py`.
Status: round 1 COMPLETE.

**Summary.** No FATAL defect in the repaired document. Lemma 2.1, Lemma 2.2, the parity group, Lemma 4.x/
Prop 4.3, Lemma 6.1, Lemma 6.3 and Lemma 1.1 are SOUND (brute-force confirmed where possible); Prop 5.1,
Thm 6.2 and Prop 7.1 are SOUND at outline level (cited large sieves checked against DI 1982 scan and
Drappeau arXiv:1504.05549 Prop 4.7). Thm 8.1 has a **coverage gap** (D1, MAJOR, easily repairable) and
two unwritten steps (D2, D3). **Label: Thm 8.1 = CONDITIONAL on (SEL), outline — not yet a proof.**
The unconditional-strip assessment is right in substance but its numbers/DI-Thm-5 application are off (D4).

## Verdicts per claim

**V1. Lemma 2.1 (distance formula) — SOUND.** Re-derived; `scripts/review_ttl_sep.py` checks
`cosh−1 = disc(Q−Q')/(8d)` in exact rationals for every pair in 𝓕_d, d ≤ 30, A ≤ 40.

**V2. Lemma 2.2 (uniform separation) — SOUND.** `4d | disc(Q−Q')` re-derived (B ≡ B' (2d) ⇒ 4d² | (B−B')²;
d | C−C' ⇒ 4d | 4(A−A')(C−C')) and checked by brute force. The constant 3/2 is **sharp** on 𝓕_d
(attained for d = 1, 5, 11, 19, 29 in the window), and the Type I subset has min cosh = 3 as the author
observed. Injectivity of Q ↦ z_Q (A fixed by disc) correct.

**V3. Parity/invariance group (§6 'Parity') — SOUND.** On the z-side the Type I set is stable under
`Γ⁰(2d)∩Γ₀(2)` (0 failures in random tests, d ≤ 30), i.e. `Γ₀(2d)∩Γ⁰(2)` on the w-side; R1's
counterexample reproduced (`[1,8,18] ↦ [27,44,18]`, B = 44 ≢ 0 mod 8). Conjugating
`Γ₀(2d)∩Γ(2q)` by `u = w/(2q)` gives `{γ ∈ Γ₀(4dq²): p ≡ s ≡ 1 (2q)}` ⊇ Γ₁(4dq²), cusp width 1, so the
character decomposition over even χ mod q (= mod 2q) with `M = 4dq²` is right (see D-list for the
normalisation factor).

**V4. Lemma 6.1 (main-term factorisation) and the §6 densities — SOUND.** `scripts/review_ttl_local.py`:
for all odd primes ℓ ≤ 23, ℓ ∤ d, the quadric `B²−4AC = −4d` has `ℓ²+χℓ` points and SL₂(𝔽_ℓ) is
transitive on it (orbit size = quadric size; directly: the stabiliser of Q̄ is SO(Q̄), a torus of order
`ℓ−χ`, and `ℓ(ℓ²−1)/(ℓ−χ) = ℓ(ℓ+χ)`). The 'Witt' justification is imprecise (SL₂ maps onto the
spinor-kernel Ω ⊂ SO, not SO), but the conclusion is true. Both g_{c,d}(ℓ) formulas verified. The
orbit-stabiliser/strong-approximation bookkeeping is correct as a *ratio*; `[Γ'_1:Γ'_q]` as Möbius
groups is `|SL₂(ℤ/q)|/2` (−I ∈ Γ(2), −I ∉ Γ(2q)), which only affects the constant in Thm 6.2's last line
(minor D10).

**V5. Lemma 6.3 (r(d), incl. 2-adic) — SOUND (with room to spare).** Brute force over every primitive
reduced form of disc −4d, d ≤ 150: `#{(t:s) ∈ ℙ¹(ℤ/d): Q₀(t,s) ≡ 0 (d)} ≤ ∏ p^{⌊k/2⌋}` with **no**
extra factor 4 at p = 2 (max ratio 1.0). Re-derivation of the 2-adic case: Q₀ primitive ⇒ WLOG A odd;
B = 2B'; `4A·Q₀(t,1) = 4((At+B')² + d)` so `2^k | Q₀(t,1)` ⇔ `At+B' ≡ 0 (2^{⌈k/2⌉})`, and points
`(1:s)`, 2 | s, give `Q₀ ≡ A` odd. The factor 6 = [Γ₀(d):Γ₀(2d)∩Γ(2)] is correct for odd d and is 4 for
even d. `Σ_{d≤D} r(d) ≪ D log D`, so the final bound even holds with `(log D)²`. Note that the per-d
relative error is **not** uniform in d (Siegel: `#Λ(1)` can be ≈ d^{1/2−ε}); the proof correctly avoids
this by summing absolute errors via Cauchy–Schwarz — the paper should say so explicitly (D11).

**V6. Lemma 1.1 — SOUND.** `#{(j,k) ∈ [1,L]²: max(j,k) = m} = 2m−1`, so the identity and `≤ 2L` hold;
the application (m_{jk} ≪ NL per (c-block, a-block), from ET (8.2)-type mass) is consistent. j = 0
(c ≍ 1, no BT saving) costs only `Σ_k NL·C/k ≪ NL log L` — harmless, but not mentioned (minor).

**V7. Prop 4.3 / Lemmas 4.1–4.2 (Sobolev duality, uniform in Γ') — SOUND (modulo ±I bookkeeping).**
`h(t) = (5/4+t²)^{−2}` is holomorphic in `|Im t| < √5/2 > 1/2` with `t^{−4}` decay, so the pre-trace
kernel is legitimate; `1−Δ = −Δ − s(1−s)` at `s = φ`, so the decay rate `e^{−φr}` (times `r` for the
square) is right; packing only uses the separation radius, hence uniform in Γ', d, q. The pairing
`ν(P₀) = ⟨(1−Δ)P₀,(1−Δ)^{−1}ν⟩` is fine (resolvent kernel has a log singularity, in L²). If −I ∈ Γ' the
kernel sum double-counts (factor ≤ 2). P_ψ ∈ L² since ψ has compact y-support (vanishes high in every cusp).

**V8. Thm 6.2 (per-d count) — SOUND at outline level, given Prop 5.1.** Re-derived the bookkeeping:
`#Λ(q)^{1/2} ≈ q #Λ(1)^{1/2}`, main `≈ 𝔐_d/q`, relative error per q `≈ q²[(d/A)^{1/2} + F'^{1/2}/A]`,
summed absolutely over d via Lemma 6.3 + Cauchy–Schwarz. Main-term density checked numerically from
scratch (`scripts/review_ttl_perd.py`: d = 101, 1009, A = 2·10⁴, F' ≈ A√d/2, c ∈ {1,2,3,5}, q ≤ 23 —
all counts within ~±2σ of `g_{c,d}(q)·N_d(1)`, including the `ℓ | c` cases, e.g. g = 0 for c = q = 3,
d = 1009). Weak evidence (sharp cut-offs, small sizes) but it confirms the orbital density is the
arithmetic one. Defects: D5 (cusp-width/period inconsistency F ≥ 8A vs f' ≥ A/8), D10.

**V9. Prop 7.1 ((K_a), fixed a) — SOUND at outline level (the restriction min(E,F) ≥ N^{c₀} is
necessary and sufficient for its use).** Re-derived: (0,0) term = `g'(q)·S_a(1)` main term (density
`φ(m)/m²` × `(ℓ−1)/ℓ²` resp. `1/ℓ`, verified in `review_ttl_local.py`); h = 0 ≠ k: the k-sum is the error
of replacing `Σ_{(f,m)=1}` by `(φ(m)/m)∫`, giving relative `O(τ(m)·q/F)` (and symmetrically `q/E`); hk ≠ 0:
Weil for prime-power moduli `|S(h,k;p^β)| ≤ 2p^{β/2}(h,k,p^β)^{1/2}`, `≪ (mq)²/(EF)` effective pairs,
the gcd sum is `≪ HK` (multiples of δ > H don't occur), total `≪ τ³ 3^{ω(q)} q m^{1/2} = O(qa)`. E or F > m
is harmless (then only h = 0 resp. k = 0 survive and the bound only improves). From-scratch numerics
(`scripts/review_ttl_ka.py`, smooth weights): for `E,F ≥ 131`, `|S_a(q) − g'(q)S_a(1)| ≤ 0.1·qa` for all
q ≤ 41, a ∈ {3,7,10}, c ∈ {1,5}; for `E = 3` (tiny e, a = c = 1) the deviation is `37·qa` at q = 5 (R1's
failure reproduced; consistent with the `qD/E` term). Inside R_bad(η₁) one indeed has
`e, f ≥ N^{1/2−3η₁/2}` (re-derived from MN3 Prop 3.3: β ≥ (1−η)/2 from α+β ≥ 1−η, α ≤ β; and
`1+α−β ≥ max(1−α−γ−η, α−η)`), so Prop 7.1 applies throughout the fixed-a part of R_bad. Defect D6
(stale reference to the retired Prop 7.2 inside the proof).

**V10. Prop 5.1 (variance of the box Poincaré series, under SEL) — SOUND at outline level; minor gaps
D7–D9.** Checked against the sources:
* DI Thm 2 (scan p. 230, (1.29)): `Σ_{|κ_j|≤K} (ch πκ_j)^{−1}|Σ_{N<n≤2N} a_n ρ_{ja}(n)|² ≪_ε (K² + μ(a)N^{1+ε})‖a‖²`,
  `N ≥ 1/2`, with (1.34) `u_j = √y Σ ρ_j(n) K_{iκ_j}(2π|n|y) e(nx)` — exactly the author's normalisation.
* Drappeau (arXiv:1504.05549, downloaded by me): the nebentypus version is **Prop 4.7** (§4.2.2), bound
  `(T² + q₀^{1/2} μ(a) N^{1+ε})‖a‖²` for `(1+|t|)^{±κ}/cosh(πt)·|Σ a_n √n ρ(n)|²` and the Eisenstein
  analogue over singular cusps; expansion via `W_{0,it}(4π|n|y) = 2(|n|y)^{1/2}K_{it}(2π|n|y)`, so
  `ρ^{DI} = 2√|n| ρ^{Dr}`; for even χ, κ = 0. The author's "q^{1/2}M^{−1}" term and "immaterial" remark are
  correct; μ(∞) = 1/M for Γ₀(M).
* Index normalisation: `Γ₀(M)/±Γ'' ≅ (ℤ/q)^×/±1` (order φ(q)/2 = number of even χ); with
  `P_χ = |G|^{−1}P_{ψ,χ}` one gets `‖P‖²_{Γ''} = (2/φ(q))Σ_χ‖P_{ψ,χ}‖²_{Γ₀(M)}` — the author's (2) is right,
  and the sum over χ of the per-χ large sieve exactly cancels it.
* n = 0 / Eisenstein: `Σ_𝔠|φ_{𝔠∞}(½+it)|² = 1` (unitary scattering matrix, also with nebentypus) gives
  `≪ λ²/Y` per χ, fine. Small `|t_j|` via Mellin at `σ₀ = 1/𝓛`: `Y^{−2σ₀} ≤ e²` because `Y ≥ λY`; the
  coalescing Gamma poles cost `𝓛²` in `sup_j|G(s,t_j)|` — polylog, fine. Unit-interval/Gallagher step for
  `|n|^{−it}` fine (`𝓛²` loss).
* Plausibility: the bound is the Poisson-level variance (`V·mean = area`) plus the Kloosterman/cusp
  term `1/(MY)`, the natural truth — no sign of an over-strong claim.

**V11. Thm 8.1 (assembly) — GAP (not FATAL).** Re-derived step by step:
* (1) c > N^η: BT on 4ad, `Σ_{j≥ηL} NL²/j ≪ log(1/η)·NL²` — fine (author's η^{−1} is a valid over-bound).
* (2b) savings: Prop 7.1 gives relative `Q²A/D = Q²N^{−δ}` (κ = 1), Thm 6.2 `Q²(D/A)^{1/2} = Q²N^{−δ/2}`
  (κ = ½); cusp term `Q²(D/A²)^{1/4} ≤ Q²N^{−δ/4}A^{−1/4} ≤ Q²N^{−δ/2}` because `A ≥ N^δ` ⇔ `α ≤ 1−γ`. OK.
* (3) `Q = z² = N^{κδ/4}` ⇒ remainder `L^C N^{−κδ/2}` ✓; main `X/(θL) = 8X/(κδL)` with `δL ≈ 2k log 2` ⇒
  saving `C/k` ✓; the Selberg sieve densities `g ≤ 1/ℓ` (`(ℓ−1)/(ℓ²+χℓ) ≤ 1/ℓ`) ✓ dimension 1.
* (4)–(5) with Lemma 1.1: `Σ_{j,k} NL·min(1/j, C/k) ≪ NL²`; layers `k ≤ C log L`: `NL(log L)²` ✓; thin strip
  `β ∈ [α, α+γ]`: `≈ j` e-blocks × L a-blocks × N per block, BT 1/j ⇒ `ηNL²` ✓.
* **But** (D1) the case analysis does not cover all of R_bad, (D2) step (2a) is unwritten, (D3) the
  weighted-mass step is only sketched. None of these looks fatal: D1 has an easy repair (second BT
  modulus + Lemma 1.1), D2/D3 are routine-looking but are genuinely missing proofs.
**Honest label for Thm 8.1: CONDITIONAL on (SEL), at outline level — "conditional outline, not yet a
proof"** (gaps D1–D3, plus the outline-level Props 5.1/7.1). No FATAL defect found in the repaired
version; I agree with R1 that the strategy is sound.

**V12. The unconditional strip / "no unconditional improvement" (§3.2, §9) — Assessment, correctly
labelled in substance; the numbers are off (D4).** The statement is correct **as a statement about
this method** (on the strip `0 < δ = 2α−1+γ < δ₀` there are cells with no power saving, of positive
logarithmic mass ⇒ `Σ_j Σ_{k≤δ₀L} NL/j ≍ δ₀ NL² log L`), and must not be read as "no unconditional
improvement is possible" (the report's wording "so there is no unconditional improvement of ET" should say
"this argument gives no unconditional improvement"). Kim–Sarnak 7/64 does apply to nebentypus forms.
Quantitatively: with `F' ≤ 2A√D`, `1/Y ≍ qF'√d` reaches `≍ N` at the worst cells, so the loss factor on
the error is up to `N^{7/64} ≈ N^{0.109}` against the saving `N^{−δ/2}`: the strip is `δ ≲ 7/32 ≈ 0.22`
(≥ 0.16 even for the smallest F' in R_bad), not "≲ 0.1". DI Thm 5 should be applied per dyadic n-block
with `X = 1/(N₀Y)` (weight `(nY)^{−2σ}`), not `X = 1/Y`; then the extra variance factor is
`≈ 1 + (F'/(q√d))^{1/2}` (μ = 1/M, M = 4dq²), still fatal near α = ½ once `F' ≫ √d·(A/d)²` — conclusion
unchanged. DI Thm 6 / Humphries claims: not re-derived (I did not check these).

## Defects

**D1 (MAJOR — coverage gap in Thm 8.1 (2b)).** Location: §8 step (2b), "This needs `f' ≥ A/8`. That
fails only on the thin strip `a ≤ b < 8ca`". False: `f' = min(e,f) = f < a` iff `β > 1`, and R_bad(η₁)
allows `β ≤ 1+η₁` (MN3 Prop 3.3). Example: η₁ = 0.1, γ = 0, α = 0.55, β = 1.05 lies in R_bad ∩ {D < A}
with `f ≍ N^{0.5} < a ≍ N^{0.55}`; the region `{1 < β ≤ 1+η₁, (β−γ−η₁)/2 ≤ α ≤ β, D<A}` has area ≍ η₁/2,
i.e. positive logarithmic mass ≍ η₁NL² per c-block; with BT on 4ad alone it costs `≍ η₁ NL² log L`
(a log log). Switching to the e-cusp does not help near `α = (1−γ)/2` (cusp term `N^{(β−1−δ)/2}`).
*Repair:* on `β > 1` use BT on the modulus `4cdf` (exponent `2−β`, saving `1/((β−1)L) = 1/k'`) together
with 4ad (saving 1/j) and Lemma 1.1 in `(j,k')`; or treat full x-periods (λ > 1/4) via the incomplete
Eisenstein series (no cusp-form contribution) and prove a separate statement. Either must be written.

**D2 (MAJOR/GAP — step (2a) unproved, inherited).** §8 (2a): BT outside R_bad needs the weighted
harmonic sums over the 7 moduli that MN3 §3.3 calls routine but never wrote (only 4ad = ET (8.2) is
available). Until written, Thm 8.1 is conditional on these too. *Repair:* write them (at least for
`4bd, 4ab, 4acf, 4cdf`, which need ρ-multiplicities and `1/φ(modulus)` sums), or state Thm 8.1 as
conditional on (SEL) **and** this lemma.

**D3 (MINOR-to-MAJOR — weighted masses in step (3)).** `Σ_σ X_σ s/φ(s) ≪ AD L` via MN3 Prop 2.3 with
`4k`, `4k²`: Prop 2.3(a)/(b) need `kB² ≤ A^l` / `kA ≤ B^l` and `A ≥ ω(k)+2`, which fail for `k` close to D
(resp. A) where the reduced variable is bounded; that tail must be handled separately (trivially it is
`≪ AD N^ε Σ_{k>D^{1−ε}} k^{−2}`, fine). Also X_σ for the fixed-d sequences is the orbital term 𝔐_d, so
"`≤` count + remainder" must be applied with the weight d/φ(d) on the remainder. Write it.

**D4 (MINOR — strip numerics, §3.2/§9, report).** "≲ 0.1" should be ≈ 0.16–0.22 (worst `1/Y ≍ N`, loss
`N^{7/64}`); DI Thm 5 must be applied with `X = 1/(N₀Y)` per dyadic block (factor `1+(F'/(q√d))^{1/2}`,
not `F'A^{−1/2}d^{−1/4}`); rephrase "no unconditional improvement of ET" as "this argument gives no
unconditional improvement".

**D5 (MINOR).** Thm 6.2 assumes `F ≥ 8A`; step (2b) uses it for `f' ≥ A/8` with "O(1) periods". Prop 5.1
needs `λ ≤ 1/4`; for small q with `λ = A/(qF') > 1/4` the splitting loses `√(#periods)` (harmless only
because #periods ≤ 32). State Thm 6.2 for `F ≥ A/8` with this splitting.

**D6 (MINOR).** Prop 7.1 proof ends "cells with `min(E,F) ≤ 𝓛^{C'}` are treated by Prop 7.2 instead" —
Prop 7.2 is retired; replace by the R_bad bound `e,f ≥ N^{1/2−3η₁/2}`.

**D7 (MINOR).** Drappeau citation: it is Prop 4.7 (§4.2.2) of arXiv:1504.05549, normalisation
`ρ^{DI}(n) = 2√|n|ρ^{Dr}(n)`; "Prop. 1" is wrong (published numbering not checked).

**D8 (MINOR).** Prop 5.1 step (5): the tails `|t_j| > 𝓛` and `|n| > 𝓛/λ` are called negligible because
`Ŵ`, `φ̂` decay rapidly — but that decay is only `𝓛^{−B}` at the cut-off, and pointwise K-Bessel bounds
lose `e^{π|t|/2}` against `cosh(πt_j)` (polynomial in N at `|t| ≈ 𝓛`). Needs: dyadic large sieve in
`K` and `N₀` (K² growth vs |t|^{−B}), and a uniform bound `|K_{it}(x)| ≪ e^{−π|t|/2}(…)`; polynomial decay
suffices since `λ/Y`, `1/(λY)`, `M` are polynomially related in all applications. Routine; write it.

**D9 (MINOR).** Inconsistent statements: §0(iii) cusp term `(Yλ)^{−ε}/(Y·level)` vs Prop 5.1
`q^{1/2}M^{−1}(𝓛/λ)^{1+ε}`; §5 `M = dq²` vs §6 `M | 16dq²` (the conjugated group is
`{γ ∈ Γ₀(4dq²): p ≡ s ≡ 1 (2q)}`, so `M = 4dq²`).

**D10 (MINOR).** Lemma 6.1/Thm 6.2: as Möbius groups `[Γ'_1:Γ'_q] = |SL₂(ℤ/q)|/2` (−I ∈ Γ(2) \ Γ(2q));
the ratio statement is unaffected, the constant in "`#Λ(q) = g|SL₂(ℤ/q)|#Λ(1)`" is off by 2. "Witt": SL₂
maps onto Ω ⊂ SO; transitivity follows from `|Stab| = ℓ−χ` instead.

**D11 (MINOR).** Say explicitly that per-d relative errors are not uniform (Siegel; `#Λ_d(1)` may be
`d^{1/2−ε}`) and that the proof only uses absolute errors summed via Lemma 6.3 and Cauchy–Schwarz.

**D12 (MINOR).** Lemma 1.1 application omits j = 0 (c ≍ 1, no BT saving); costs `≪ NL log L`, harmless.

**D13 (MINOR).** Lemma 6.3: the factor 4 at p = 2 is unnecessary (exact `2^{⌊k/2⌋}`, brute force
d ≤ 150); `(log D)³` can be `(log D)²`.

## Not checked / not accessible
ET Prop 2.2/Lemma 2.8 reduction (inherited from MN3, not re-reviewed here); DI Thm 6 and Humphries
Thm 1.5 numerics in §3.2/§9; Jia 2012 (not accessed). Drappeau's published (Proc. LMS) numbering.

---

# Round 2 (after O112 repairs, branch side-agent/ttl-repair merged)

**Final label: Thm 8.1 is a complete CONDITIONAL proof on (SEL)** (Selberg's eigenvalue conjecture for
`Γ₀(4dq²)` with even nebentypus mod q), relative to the cited results: ET Prop 2.2/Lemma 2.8/(8.1)–(8.2)
and MN3 Thm 3.8(1) (the reduction to `w_c` and the part with `c > N^η`; inherited, and **not re-reviewed by me**),
MN3 Prop 2.3 (reviewed earlier, in R108), the DI Thm 2 / Drappeau Prop 4.7 large sieve (statements and normalisations
checked by me in round 1), the spectral theorem with nebentypus, Brun–Titchmarsh (Montgomery–Vaughan),
Selberg's sieve, Weil and Pólya–Vinogradov. I found no FATAL or MAJOR defect in the repaired text. Two
MINOR wording gaps are fixed in place, marked "(R111 r2)". The unconditional status is unchanged and
correctly stated: this argument gives no unconditional improvement.

## Round-1 defects
* **D1 — RESOLVED.** (b5) covers `1 < β ≤ 1+2η₁` on the `D < A` side.
  * If `k' ≤ k/2`: the f-cusp with `λ = A/(qf) > 1`. The `n = 0` loss is `(A/f)^{1/2} = N^{(β−1)/2} ≤ N^{δ/4}`,
    and the cusp term is `f^{1/2+ε}/A ≤ A^{−1/2+ε}`.
  * Otherwise: BT on `4cdf`, with saving `1/k'` (per-cell weight `Σ_c 1/φ(c)·Σ_d φ(d)^{−1}Σ_f ρ_d(f)/φ(f) ≪ 1`
    by Lemma 8.3(c)).
  * In both cases the saving is `C/max(k,k')` and the per-cell mass is `≪ N` (Lemma 8.4(b)). The total is
    `Σ_{k,k'} N/max(k,k') ≪ NL` per c-block, which I verified.
* **D2 — RESOLVED.** I re-derived §8.0:
  * The identities `4abd = ne+1`, `bf = na+c` and `n/4 < acd ≤ 3n/4 ⇔ 0 < f ≤ 2n` hold, so `b ≥ a/2`.
    Hence `4ad` and `4bd` are long for `c ≤ N^η`.
  * The fibres acf/cdf/ab are injective, each lands in one class (resp. ρ_d(f) classes) mod `m_T`, and BT
    applies.
  * The weight sums `Σ 1/φ`, Lemma 8.3(b) (τ(n) ≤ 2#{δ | n, δ ≤ √n}; the count `2B(l,δ)/(lδ)+1`) and
    Lemma 8.3(c) are correct. For 8.3(c) I checked `ρ_d ≤ 1∗χ_d`, the Jacobi/PV mean square for
    `Y ≤ D/log²D`, and the PV tail beyond `Y₀`.
  * From scratch: `D^{−1}Σ_{d≍D} g(d)Σ_{f≍F}ρ_d(f)/φ(f)` is 0.61–1.94 for D ∈ {50, 400} and F from 1 to 3000
    (`scripts/review_ttl_r2.py`), so it is bounded uniformly in F as claimed.
* **D3 — RESOLVED.** Lemma 8.4:
  * (a1): the hypotheses of MN3 Prop 2.3 are checked, including the large-k tails (enlarging the variable
    range to ≥ 2).
  * (a2): the tail `k > A^{1/2}` costs `N^ε AD A^{−1/2}`, fine since `A, D ≥ N^{1/4}`. This holds where it is
    used (`k ≤ L/3` ⇒ `δ ≤ 1/3`).
  * (b): `ρ_d(f)(A/f+1) ≤ 9ρ_d(f)A/f` for `f ≤ 8A`.
  * `X_σ ≤ #σ + |r_σ(1)|` is correct.
* **D4 — RESOLVED.** 7/32, 21/128, `X = 1/(N₀Y)`, and the rephrasing.
* **D5 — RESOLVED, by a better route than I suggested.** The periodised ψ has Fourier coefficients
  `λφ̂(λn)` for every λ. For λ > 1 every `n ≠ 0` term is `≪ λ^{−B}`, so only the `n = 0` term `λ²/Y` survives.
  The resulting factor `(1 + A/(qF))` carries no `N^ε`.
* **D6–D13 — RESOLVED** (checked each spot).

## Newly written proofs
* **Prop 5.1 (Steps 0–7) — SOUND.**
  * Step 1: `P_ψ = (2/φ(q))Σ_χ P_χ` and the norm identity are re-derived.
  * Step 3, Stirling bound (b): with `Re w = −1/2` the Gamma factors give `e^{−π max(|v|,|t|)/2}` and
    denominators `≥ 1/2`, so the claimed `e^{−π|t|/2}(1+|t|)^{−2}(1+|v|)^4` follows in both ranges.
  * Step 5: the residues at `s = ±it_j` are `½Γ(±it)𝒲(±it)(πY)^{∓it}B(±it)`, and no other poles lie in
    `−1 < σ < 1/𝓛`.
  * Step 6:
    * the block weights `w_{N₀} = 1+|log λN₀|` give `Σ w^{−2} ≪ 1`;
    * `Σ_{N₀} w²λ²N₀ min(1,(λN₀)^{−2B}) ≪ λ`, and the cusp part gives `q^{1/2}λ^{−ε}/M`;
    * Gallagher's step on each unit interval is valid. For Eisenstein, apply it to `B(t,τ)` on the diagonal.
    * Reflection to χ̄ for `n < 0` is fine (Kuznetsov/large sieve hold for any orthonormal basis).
    * The `log|n|` factor is `≤ 𝓛 + |log λ|n||` for λ < 1, and `≤ log(λ|n|)` for λ > 1.
* **Prop 7.1 (i)–(v) — SOUND.**
  * The congruence `a n = f(ce−a) − c` is correct.
  * `T_ℓ = e(uc̄a/ℓ)S(uc̄,vc;ℓ)` resp. `ℓ·1[u≡0]`.
  * The Ramanujan step is `|c_m(k)| ≤ (k,m) ≤ Σ_{δ|(k,m)}δ`.
  * The gcd-sum `Σ_δ δ^{1/2}(r/δE)(r/δF)` also covers `δE > r` via `(r/δE)^B ≤ r/δE`.
  * Round-1 numerics (`review_ttl_ka.py`) are consistent.
* **Thm 6.2 for all λ and the e-cusp variant — SOUND.**
  * `[e,4ad,df] ∈ 𝓕_d^I` is the same point set. In the coordinates `(A, B, C/d)` the two conditions `A = cB`
    and `C/d = cB` give the same quadric equation, so `g_{c,d}` is unchanged.
  * From scratch (`review_ttl_r2.py`): sieved counts over `(a, e)`, including `A/E = 4` and `10` (λ > 1),
    are within ±2.6σ of `g_{c,d}(q)N(1)` for d ∈ {101, 1009}, c ∈ {1, 3}, q ≤ 17.
* **Thm 8.1 bookkeeping (2a)–(5) — SOUND.**
  * (b2): `k ≥ 2j` ⇒ `δ ≥ 2γ` ⇒ `(A/e)^{1/2} ≤ N^{γ/2} ≤ N^{δ/4}`. The per-(j,k) (b2) mass is `≈ jN ≤ NL`
    (≈ j β-cells of mass N each). The (b2) total is `Σ_j Σ_{k≥2j} jN/k ≪ η²NL² log(1/η)`, fine.
  * (b3): the cusp exponent combined with `Q² = N^{δ/8}` is `(1−γ−4α)/8 < 0`, and `cusp ≤ N^{−δ/4}` ⇔ `α ≥ 0`.
  * (b4): the 4ad progression over `c ≍ 2^j` has length `4ad·2^j`, so `log(y/m) = j log 2`.
  * Sieve exponents: `Q² = N^{κδ/2}` gives remainder `N^{−κδ/2} ≤ 1/k` once `k ≥ C₁ log L` with C₁ large
    (κ ≥ 1/4).
  * Bands: O(L) cells of mass ≪ N per c-block. c ≍ 1 (j = 0): harmless.

## Round-2 minor items (all fixed in place by me, "(R111 r2)")
* **R2-1.** Step (3) cites only `g ≤ 1/ℓ`; the lower bound `G(z) ≫ (φ(2cs)/2cs) log z` also needs
  `g(ℓ) ≥ 1/ℓ − 2/ℓ²`. It holds for both density families, and the text now says so.
* **R2-2.** (b2) is stated for `α ≤ β`, but §8.0 only gives `b ≥ a/2`. Cells with `a/2 ≤ b < a` have
  `e < 2a/c` and are covered by the same treatment; now said explicitly.
* §0's "awaits a round-2 review" is replaced by a pointer to this review.

## Residual caveats (not defects)
* (SEL) is a deep open conjecture, and it is needed uniformly for all levels `4dq²` with `d ≤ N`.
* The ET/MN3 reduction (`f_I ≤ 2Σ_c w_c`, MN3 Thm 3.8(1)) is inherited and was not re-checked in R111.
* DI Thm 6 / Humphries numerics in §3.2/§9 are labelled as not re-checked. They only affect the
  unconditional Assessment.
