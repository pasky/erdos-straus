# R117 — hostile review of EXCEPTIONAL_MN4.md (task O117)

Reviewer: R117 (side agent, branch `side-agent/review-emn4`). Reviewed tip: merge of
`side-agent/mn-sel-transition` at `478a57e` (O117 report). I read EXCEPTIONAL_MN4.md in full, plus
AGENT_REPORT_O117.md, reviews/emn4-selfreview.md, EXCEPTIONAL_TYPEI_LOGLOG.md §§4–8, MN3 §2 (Lemma 2.1,
Prop 2.3, Prop 2.5, Thm L'), MN2 (Prop 3.2, Lemma 3.5, Thm U), and the (b3) passage of
paper/es-typei-heegner-note.tex (ll. 1485–1531).
External source: I checked Drappeau arXiv:1504.05549v4, §4.2.2, Proposition 1 (HTML via r.jina.ai).
It states `O_ε((T² + q₀^{1/2}μ(𝔞)N^{1+ε})‖a‖²)` for a singular cusp of `Γ₀(q)` with multiplier mod `q₀`.
That is exactly the level-uniform form MN4 §2.2 uses, and no `(q,M)=1` condition appears.
I did not re-access DI 1982 or ET.

From-scratch scripts (none reuse the author's code), run under `ulimit -v 4000000` + `timeout`:
* `scripts/review_emn4_lemma11.py` → `.out.txt`. This enumerates **all** ordered Type I m-solutions with exact
  rationals, for m = 4..13 and n ≤ 120.
  - `f_{I,m}(n) ≤ 2Σ_c w_{c,m}(n)` holds.
  - For primes, a Type I solution exists iff some `w_{c,m}(n) ≥ 1`.
  - Every one of 4027 w-tuples maps back to a solution satisfying all of (1.1) and `b ≥ a/2`.
  - Failures: 0.
* `scripts/review_emn4_forms.py` → `.out.txt`:
  - (1) Over 42,184 pairs, `disc(Q−Q') = 8t(cosh−1)` holds **exactly**, `4t | disc`, and min cosh = 3/2.
  - (2) Quadric count `ℓ²+χℓ` and the constrained counts for **both** cusps hold in 1340 (ℓ,t,c) cases. I also
    checked SL₂(𝔽_ℓ)-transitivity on the quadric.
  - (3) The content is in {1,2}, and content 2 occurs only for odd a with t ≡ 3 (4) (574 such forms seen).
    For t ≤ 60 and every reduced form of discriminant −4t (any content), at most one point of `ℙ¹(ℤ/t)`
    puts `Q₀∘γ` in `𝓕_t`. The condition is independent of the coset representative. Totals equal
    `h(−4t)+[t≡3(4)]h(−t)` (255 = 255), so the bound in §2.5 is attained.
  - (4) The majorants `ρ_{md}(f) ≤ 4·1_{(f,m)=1}(1∗χ_d)(f)` and `ρ(rf') ≤ 2^{ω(r)}ρ(f')` hold, including the
    2-adic cases.
  - (5) The `τ_m` small-divisor inequality holds.
  - Failures: 0.
* `scripts/review_emn4_exponents.py` → `.out.txt` (sympy):
  - Exact exponent algebra for §2.7 (b2), (b3), (b5) and for TTL (b3). It also exhibits a (b3) cell inside
    `R_bad(2η₁)` with tiny D.
  - A Lemma 0.1 grid.
  - A numerical check of the §3.5 sieve denominator `G(z)/(h(M)log z)`, which lies in [0.75, 1.50] for M up to the primorial of 23.
  - The (3.2.2) residue-class identity.
  - The §3 "Issues" CRT example: m = 167319652, d = 2, and every odd squarefree f ∈ (12,24] has `ρ = 2^{ω(f)}`.
  - Failures: 0.

## Verdicts

| Claim | Verdict |
|---|---|
| Lemma 0.1 (m > L^5 reduces to MN3 L' / MN2 3.5) | **SOUND** |
| Lemma 1.1 + (1.1) + coprimality facts (general m) | **SOUND** (re-derived; brute-forced) |
| §2.1 Lemma 2.2_m (set equality, separation cosh ≥ 3/2, Γ⁰(t)-stability, no parity) | **SOUND** |
| §2.2 groups / (SEL_m) / Drappeau input | **SOUND** (source checked); see D3 (elliptic elements; documentation) |
| §2.3 Lemma 6.1_m local densities, both cusps | **SOUND** |
| §2.4 Thm 6.2_m (incl. the `q^{ε−1/2}A^{−ε}` repair of TTL's `λ^{−ε} ≤ F^ε`) | **SOUND** (conditional) |
| §2.5 Lemma 6.3_m (content-2, one orbit per class, `≪ √(md) log`) | **SOUND** |
| §2.6 Prop 7.1_m (K_a), `X_a = Dφ(k)/k·…` | **SOUND** |
| §2.7 (2.7), (b1), (b2), (b3), (b5) remainders | **SOUND** (conditional); D1 sharpened the (b3) remark |
| §3.1 BT outside R_bad with gain h | **SOUND** |
| §3.2(b) τ_m-weighted sum | **SOUND** |
| §3.2(c) (D, F ≥ L^{100}): mean square, hyperbola, (3.2.1)/(3.2.2) split | **SOUND**; the CRT counterexample to the all-ranges version is also sound |
| §3.3 (a1), (a2), (a3), (b) | **SOUND** relative to MN3 Prop 2.3 (hypotheses re-checked) |
| §3.4 large c, dropping `L ≤ √m` | **SOUND** (see D4, cosmetic) |
| §3.5 sieve denominator, fixed-a/fixed-d main terms, bands, aggregated low-D | **SOUND** |
| Thm 4.1 (Thm I_m), incl. (2b-0) c = 1 and (b5) | **SOUND, CONDITIONAL on (SEL_m)** relative to TTL's cited inputs; see D2 (wording) |
| Thm 5.1 (Thm L'') | **SOUND** (conditional for m ≤ L^5, unconditional above) |
| Thm 5.2 (matching orders) | **SOUND**; the lower half is conditional and the upper half is MN2 Thm U (ineffective) |
| §6 unconditional ingredients and status | **SOUND**; labels accurate |
| Author's claim that TTL (b3)'s `N^{−δ/2}` is not supported | **CORRECT**. TTL (D)32 needs a one-line erratum, but Thm 8.1 is unaffected (D1) |

**Overall: no FATAL or MAJOR defect.** Thm 4.1, 5.1 and 5.2 stand with the stated labels.

## Defects

**D1 (MINOR; TTL erratum).** Locations: TTL §8 (b3), `EXCEPTIONAL_TYPEI_LOGLOG.md` l. 488; MN4 §2.7 (b3).

Re-derivation, with `AD ≍ N/(mc)` and `A/D = N^δ`:
* The cusp term is `F'^{1/2+ε}/A ≪ m^{3/8+ε}N^{2ε−(1−γ)/8−3δ/8}`.
* Its gap to `−δ/4` is `(1−γ+δ)/8 − 2ε`. This gap is uniformly positive, so MN4 is right.
* Its gap to `−δ/2` is `(1−γ−δ)/8 − 2ε = (log_N D)/4 − 2ε`. This is negative when `D < N^{8ε}`.
* For m = 4, TTL's own display gives a ratio to `N^{−δ/2}` of `N^{ε}D^{−1/4}`. This exceeds 1 for `D < N^{4ε}`.
* Such cells exist in `R_bad(2η₁)` and in the (b3) range. An example is γ = 0, α = 0.996, β = 0.998 (script).

Also, TTL's intermediate bound `≤ N^{−1/9}` does not imply `N^{−δ/4}` once `δ > 4/9`, and δ can approach 1 − γ when D < A. The direct comparison `(1−γ−3α)/4 + ε = −δ/4 − α/4 + ε` is what works. The paper `es-typei-heegner-note` (l. 1514–1519) already uses exactly this comparison and states `N^{−δ/4}`.

Since TTL step (3) already uses κ = 1/4 for (b3), **Thm 8.1/(D)32 is unaffected**; only the displayed (b3) exponent is wrong.

*Repair (applied, R117 repair/erratum):* I added an erratum line in TTL (b3) and a precise version of MN4's remark in §2.7 (b3).

**D2 (MINOR; wording).** Location: MN4 §4 (2b-0).
* "(b2) applies since γ = 0" is vacuous: for c = 1 the (b2) range `α ≤ β < α+γ` is empty. The cells with `a/2 ≤ b < a` lie in the band `|β−(α+γ)| ≤ C₀/L`. Nothing is lost.
* The factor `g(m)` in "trivial c-count … `hADL·g(m)`" is superfluous, because no BT is used. It is harmless as an upper bound.

*Repair (applied):* the (b2) clause now says it is vacuous. I left the `g(m)` as is.

**D3 (MINOR; documentation of a genuine difference from TTL).** Location: MN4 §2.2.
* For m = 4, TTL's levels satisfy `4 | M`, so its groups are torsion-free mod ±I.
* MN4's levels `md` (q = 1) can have elliptic elements, e.g. Γ₀(5), Γ₀(7), Γ₀(10).
* I checked that TTL §4 (orbifold weights `e_z`, Lemma 4.2/Prop 4.3 for general finite-index Γ') and §5 (Parseval/Kuznetsov for general Γ₀(M), χ) never use torsion-freeness.
* Moreover `e_z = 1` for all Heegner points here, since `Stab(z_Q) ⊂ SO(Q) = {±I}` for discriminants −4t and −t with t ≥ 4.
* So this is not a gap, but it was unstated.

*Repair (applied):* I added a remark after "The infinity cusp has width 1".

**D4 (MINOR; cosmetic).** Location: MN4 §3.4, last paragraph.
* In the range `c > N^η`, every block has `mad < 3N^{1−η}`. So the BT denominator is `≥ ηL/2` in every block, not only for `X ≤ N^{1/2}`.
* The split at `N^{1/2}` and the "weaker BT denominator ≳ 1" are therefore unnecessary. They are correct as written.
* No repair is needed. Optionally, simplify.

**D5 (MINOR; status line).** Location: MN4 §0, "no independent hostile review yet".
*Repair (applied):* this now points to this review.

## Notes on the focus items (no defect found)

* **§3.2(c).** I re-derived each step:
  - The mean square uses PV in d for the nonprincipal `(·/rr')`. The coefficient vanishes when `(m,rr')>1`.
  - The tail `Y > Y₀` costs `√(mD)log³/D = o(1)` for `m ≤ L^5` and `D ≥ L^{100}`.
  - In the hyperbola step, χ_d already kills `(r,m)>1`. The coprime count is `hx + O(H)`, and the optimal `U = √(uV/H)` needs `u ≥ V/H`; the other case is handled.
  - The (3.2.2) per-class count is `Σ_{x∈(ℤ/f)^×}Σ_{d≡−(mx²)^{−1}} g(d) ≪ φ(f)[D/f + log 2D]`. I checked the identity numerically.
  - In the split at `F = D/L^{20}`, the relative error is `L^{14}D^{−1/4} = o(h)`.
  - Weakest point: the `h`-gain in (3.2.1) comes only through `|L(1,χ_d)|` in mean square. This is fine because the main term carries h exactly, from the coprime count of the second variable.
* **§3.5.**
  - The Markov/Euler-product argument for `G(z) ≥ c·h(M)log z` is correct and uniform in M, including when `M > z`. It needs `ν(ℓ) ≥ 1/ℓ − 2/ℓ²`, which I verified for `(ℓ−1)/(ℓ²+χℓ)` and `(ℓ−1)/ℓ²`. A numerical ratio of ≥ 0.75 also checks out.
  - `g(2mca)φ(ma²)/(ma²) ≤ 2g(c)` is exact.
  - The aggregated low-D bound uses (a3): for `t ∈ (D,2D]` the enlarged length-2 boxes cost only `O(log m)` relative, even at D ≍ 1. Its total is `(N/m)L log(2m)(log L)² ≪ NL²/m`.
* **§4, c = 1 and (b5).**
  - In the (b5) BT branch, the modulus `mcdf ≍ N^{2−β}` has m cancelling, because `mcd ≍ N^{1−α}`.
  - `1/φ(mcdf) ≤ g(m)g(c)g(d)/(mcd·φ(f))`, and §3.2(c) gives `N g(m)h/m = N/m` per cell, with saving `C/k'`. The R1 display is now correct.
  - For c = 1: (b4) degenerates to counting (one n per (a,d,f)), (b1)/(b3) are summed over k with `1/k`, and (b5) is summed over `1/max(k,k')`. All terms are `≪ (N/m)L log L`.
* **Uniformity in m.**
  - Spectral constants: separation, Sobolev and Drappeau are all level-uniform.
  - m enters as `m^{1/2}` in (2.7) and (b1), and as `τ(ma²)`, `2^{ω(m)}` and `g(m)` elsewhere. These are all `L^{O(1)}` under `m ≤ L^5`.
  - Characters mod m appear only via `χ_{−4md}`, inside the D ≥ L^{100} mean square.
  - R_bad shifts by `O(log L/L)`.
  - I found no constant that secretly depends on m.
* **Quantifiers.**
  - Thm 4.1 uses fixed absolute η, η₁, ε, so N₀ is absolute.
  - In Thm 5.1, the case (i) choice `L₀ = e^{20C}` gives `CL/log L ≤ 0.5 log m`. Bounded L forces bounded m (`L ≥ log(m/3)`).
  - In case (iii), MN2 Prop 3.2 needs only `log m ≤ L/10`, not `L ≤ √m`. I checked this in MN2.
  - Thm 5.2 chooses `c_ε` first and `m_ε` second, which is correct.

Recommendation: accept MN4 with the CONDITIONAL labels as stated, and the TTL (D)32 erratum D1 (statement-level only).
STATUS/ledger may record MN4 as "hostile-reviewed (R117), no FATAL/MAJOR".
