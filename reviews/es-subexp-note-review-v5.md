# Referee report R64 — `paper/es-subexp-note.tex` v5

Branch reviewed: `side-agent/subexp-paper-v5` (merged into `side-agent/referee-subexp-v5`).
Scope: everything new/changed in v5 (C1–C11 of AGENT_REPORT_O64): intro/abstract, §§11–13, §14, bib.
§§2–10 unchanged from v4 (refereed R56) — only cross-references checked.

STATUS: COMPLETE (round 1).

## Recommendation
**Minor revision.** No FATAL or MAJOR defect. Every new proof I could re-derive is correct as
written (Prop 11.1, Thm 11.2, Prop 11.3, Lemma 12.1, Thm 12.2, Prop 12.4, Thm 13.1,
Prop 13.2(a)); the statements imported from [TQ], [SL], [O15], [O16] agree with their sources
(numbering of [TQ] and [SL] checked on fresh compiles). Labels are honest: LS is a conjecture
everywhere, ES is nowhere claimed, [TQ]-based results are flagged as resting on an internally
proved, not externally refereed note, and Page/BDH are disclosed as recalled from Davenport.
The six minor defects (D1–D6) are citation precision, label/convention completeness and scope
wording; one nit (N1). Compile: pdflatex ×3 on a clean copy — 51 pp., 0 undefined references,
0 overfull boxes, one hyperref warning (N1).

| claim | verdict |
|---|---|
| C1 §11 imports (A1)–(A3) from [TQ] | SOUND |
| C2 Prop 11.1 Haar lower bound without loss | SOUND |
| C3 Thm 11.2 typical size | SOUND (mod [TQ], Page) |
| C4 Prop 11.3 ceiling at level `cℒ⁴` | SOUND (mod [TQ]) |
| C5 Rem 11.4 unified sieve limit | SOUND-AFTER-REPAIRS (D1, D2) |
| C6 §12 Lemma 12.1, Thm 12.2, Prop 12.4 | SOUND |
| C6 §12 Cor 12.3, Siegel statement | SOUND as statements; label D4 |
| C6 §12 scope / examples | SOUND-AFTER-REPAIRS (D5) |
| C7 Thm 13.1 (LS ⇒ 1/3), LS labelling | SOUND |
| C7 Prop 13.2(a) / (b) | SOUND / statement matches O16, sketch only (D4) |
| C8–C11 intro, abstract, §14, cross-refs, bib | SOUND-AFTER-REPAIRS (D2, D3, D4, D6, N1) |

## Verdicts per claim

**C1 — §11 preamble, imports (A1)–(A3) from [TQ].** SOUND.
Checked against `paper/es-threequarter-note.tex`: (A1) = Lemma 2.2 (`lem:CRT`; distinctness proof
re-derived: `|uv'-u'v|<z_j^2<ℓ` ⇒ `(u,v)=(u',v')`, then `k≡k' (4uv)`, `4uv>4H²>K` ⇒ `k=k'`);
(A2) = Cor 4.3 (`cor:fibremass`, stated for *every* residue c, reduced ⇒ `≍t³`) with Lemma 3.2
(`h(𝒦(K)) = (2/π²)log K+O(1)`); (A3) = Lemma 8.1 + Thm 8.2 (`Q_r` identities, ledger
`log q_max ≤ C_θBt³+r(1+κ)t`, `log T_abs ≤ C_L t⁴`, integer mean for `log N ≥ C_0 t⁴`).
Enlarging `D_B` is harmless in [TQ] (its two conditions on `D_B` are monotone; `c_a=c_v/2` does not
depend on `D_B`; only `C_L, C_0` grow). `X = T^{1/(1+ϰ)}` gives `K_X X ≤ T`; `ℓ > X^{1/2} > K_X`
so `ℓ ∤ L_K`, hence the independence claim. From-scratch check
`scripts/review_r64_atoms.py`: 43 880 atoms in scaled-down families (`z²<ℓ`, `4H²>K`) — zero
residue collisions, `≤ z²` atoms per ℓ, multiplier identity exact (Fractions) on members of each
atom class, activity rule `k | u+cv`, and Bonferroni `Q_r` identities/inequalities (even r
majorant, odd r minorant).

**C2 — Prop 11.1 (Haar lower bound without loss).** SOUND.
Given c: `P(H=0|c)=∏(1-f_c(ℓ)/(ℓ-1)) ≤ e^{-μ_c} ≤ e^{-at³}`; uses (A1) (distinct residues ⇒
`I_ℓ` Bernoulli) and (A2) for every unit c. Conditioning on `n≡1 (24)`: `L_K` is odd (all
`k≡1 (4)`), `3|L_K` (9∈𝒦), so the condition fixes `c mod 3` and an independent `n mod 8` —
the uniform-in-c bound survives. `W(n)>T` ⇒ no atom (modulus `≤K_X X≤T`). Correct; the
md's factor 8 is indeed unnecessary.

**C3 — Thm 11.2 (typical size).** SOUND (modulo [TQ] and Page's theorem, as labelled).
Re-derived: prime count `≤ y + Σ_{p≤x} ν_X(p)`; Case A uses (A3) integer mean with
`log x ≥ C_0t⁴` (forced by `c_1`), and `e^{c_at³/2} ≥ log x`. Case B: `t⁴ ≪ (log log x)^{4/3}` so
all moduli and `Σ|c_i|` are `exp(O((log log x)^{4/3}))`, inside the Page range; the split
`p ≤ √x` / `p > √x` is correct; non-coprime terms are `≤ Σ|c_i| ω(q_i) log x` (the stated bound
is cruder but fine); main terms `x E_*[ν_X(1-εχ̃₁)]` (primitive χ₁ ⇒ class integral is
`χ₁(a)/φ(q)·1[q₁|q]`), `ν_X ≥ 0` on `Ẑ^×` by periodicity, `|1-εχ̃₁| ≤ 3`;
`E_*ν_X ≤ P(H=0)+E(H)_{r+1}/(r+1)! ≤ e^{-at³}+(2eC_ut³/(r+1))^{r+1}` with
`m!e_m(p) ≤ (Σp)^m`, `Σ f_c/(ℓ-1) ≤ 2μ_c`; with `r+1 ≥ D_B t³ ≥ 2e²C_u t³` the tail is
`≤ e^{-(r+1)} ≤ e^{-D_B t³} ≤ e^{-at³}`. Error `x e^{-c_3√log x/2} ≤ π(x) e^{-at³}` because
`e^{at³} ≤ (log x)^{2a/c_a}` in Case B. Note Case B does not use [TQ]'s moment theorem, only (A2).
Page's form (11.1): I could not access Davenport (not in `sources/`); from memory the
statement (Davenport Ch. 20, (9)–(13)) matches, including that the exceptional character is
primitive mod `q₁ | q` and unique for the range. Disclosure in the text is adequate.

**C4 — Prop 11.3 (ceiling at level `cℒ⁴`).** SOUND.
Re-derived against Lemma 10.2 as written: big coordinates `X_ℓ=n mod ℓ`, `ℓ∈(X^{1/2},X]`, `ℓ∤Q`;
small = everything else (c, fibre constants, higher ℓ-adic digits) — independent on units. A
modulus `q ≤ D` has `≤ 2log D/t` distinct prime factors `> X^{1/2}`, so `k=⌊2log D/t⌋`. Each
atom with `ℓ∤Q` reads c (since `k|L_K`) and one big `X_ℓ`; `Ω_ℓ(c)` has exactly `f_c(ℓ)` points
by (A1), so `p_ℓ=f_c(ℓ)/(ℓ-1) ≤ ℓ^{1/3}/(ℓ-1) ≤ 2ℓ^{-2/3} < 2X^{-1/3}`. Big primes dividing Q:
`≤ 2log Q/t ≤ T^{0.05}`; loss `≤ 2T^{0.05}X^{-1/3} = o(1)`. Uniformity over small configurations
is exactly the "every unit c" of (A2) — this is the crucial point and it is supplied by [TQ]
Cor 4.3. `(k+1)+(2k+1)r* ≤ 2(k+1) ≤ at³/2` for `log D ≤ cℒ⁴`, c small. The consequence
`(log log p)^{1/4}` in Cor 10.7 is arithmetic-correct (`ℒ ≪ (log x)^{1/4}` vs Thm 1.1's
`ℒ ≥ c(log p)^{1/4}(log log p)^{-1/4}`).

**C5 — Rem 11.4 (one sieve limit).** SOUND-AFTER-REPAIRS (D1, D2 below).
Matches CEILINGS_UNIFIED Thm 4.1 (L−, L+, U−, U+) and Thm 4.3 as reviewed (and repaired, D9 of
that review: level `c·L·P ≤ λ* ≤ C·L·P + λ_s`; the Remark only says `≍ ℒ⁴`, consistent).
Checked: `(L−)` needs `r* ≤ 1/3` (true here, `r* ≤ 4X^{-1/3}`); `(U+)/(L+)` Bonferroni algebra
re-verified in `scripts/review_r64_atoms.py`. Labels: "conjunction of proved statements;
Assessment as mechanism" — appropriate, but see D1/D2 for citation precision.

**C6 — §12 (Lemma 12.1, Thm 12.2, linear certificates, Cor 12.3, Siegel paragraph, Prop 12.4,
scope).** Lemma 12.1, Thm 12.2, Prop 12.4: SOUND. Cor 12.3 and the Siegel statement:
SOUND as statements (checked against O15 Cor 2.4, Lemma 2.3, Thm 3.1); proofs are sketches with
pointers — label issue D4. Scope paragraph: SOUND-AFTER-REPAIRS (D5).
* Lemma 12.1 re-derived: `E_{σ_J}[∏_I h_b] = −∏_J(γ_b−β_b)∏_{I∖J}γ_b` (telescoping of
  `Σ_{y⊆J}(−1)^{|y|+1}∏β∏γ`), vanishing unless `J⊆I`; `|γ_b| ≤ (1/4+p_b)/(1−p_b) < 1/2`;
  `e_{k+1}(r) ≥ 1` from `a e_a ≥ (R−kr*) e_{a−1} ≥ (k+1)e_{a−1}`; `C(m,k+1)2^{−(m−k−1)} ≤ 2^{k+1}`.
  The reduced-product claims for classes, Dirichlet and additive characters are right (local
  additive factor at `b^v`: Ramanujan sum `c_{b^v}(a')/φ(b^v)`, `|·| ≤ 1/(b−1)`); the new
  "whole ℓ-adic component" convention is what makes `e(an/q)` with `ℓ²|q` a function of one big
  coordinate, and it changes neither `p_ℓ(x)` nor `R(x) ≥ μ*` (events read `X_ℓ mod ℓ`; the
  higher digits were small and uniform before, now they are inside `X_ℓ` and still uniform) —
  author's point 3 is fine. Bits for `ℓ > T^{0.7}` have `p_b=0` and are never set.
  **From-scratch numerics** `scripts/review_r64_planted.py`: builds the planted law on bit
  patterns explicitly, checks `ν ≥ 0`, `ν(b=0)=0`, exact k-wise marginals, then computes
  `E_ρ h` for random reduced products (incl. additive-character-like factors) by summing over
  all bit patterns with directly computed conditional means — independent of the telescoping
  identity. Four configurations (k=1,2; up to 18 coordinates): all bounds hold, `E_ρ h=0` for
  `|I|≤k` to 1e-12; worst ratio to `(4r*)^{k+1}` is `~1e-3` (bound far from tight, as expected).
* Thm 12.2: `E_H B = E_ν B − E_ρ B ≤ −E_ρ B`; `k+1=⌊μ*/2⌋` satisfies the planting condition since
  `μ*r* ≤ μ*/2`; `(8T^{−1/2})^{μ*/2−1} ≤ exp(−cℒμ*)`. Correct.
* Lemma 2.3 of O15 as quoted: re-derived (classes: `max(1−N/U, N/U) ≥ 1/2`; characters/additive:
  Parseval gives `Σ|f̂|² = (#chars)·N(1−N/U)`, so `𝔈² ≥ N(1−N/U) ≥ N/2`). Correct.
* Cor 12.3 sketch (= O15 Cor 2.4): `N_x E_H B > Σ_deep |c_i| 𝔈_i`, `E_H B ≤ η Σ_deep|c_i|`,
  `𝔈_i ≥ 1/2` ⇒ `N_x η > 1/2`. Correct.
* Siegel paragraph: `χ₁h` is again a reduced product (local mean of `χ_{1,b}·e(aX/b^v)` is `0` for
  `v≥2`, Gauss sum `≤ √b/(b−1)` for `v=1`), hence `2(4r*)^{k+1}`; level `≤ T^{0.6(k−s)}` ⇒ `B` and
  `χ₁B` read `≤ k` big coordinates ⇒ `E_{(1−εχ₁)P}B ≤ E_{(1−εχ₁)ν}F = 0`. Correct; the mass caveat
  restored by the self-review is right.
* Prop 12.4 re-derived: `log x < 0.6ℒ(k+1)` ⇒ every `q ≤ x` has `≤ k` big primes ⇒ `E_ν h = E_H h`;
  `N − N_{x,q} ≤ ω(q) ≤ log q/log 2 ≤ 2log x`. The P1 repair (centring at `N_{x,q}`) is consistent.

**C7 — §13 (LS, Thm 13.1, remarks, Prop 13.2).** Thm 13.1: SOUND. LS: correctly labelled a
conjecture everywhere (§13 header "a conjecture", Thm 1.5/13.1 "conditional on LS", §14 Not-claimed
list); intro statement of LS agrees with LS(C) of §13. Prop 13.2(a): SOUND. Prop 13.2(b):
statement matches O16 Prop 4.1(b)/Cor 4.2; proof only sketched (D4). Remarks: SOUND (nit D6).
* Thm 13.1 re-derived. The system `ℰ_T` (all `ℛ(M)` classes, `M ≤ T`, plus the 186 non-square unit
  classes mod 840) has moduli `≤ T` and unit classes (`gcd(4D,M)=1` as `4A_M=M+1`). The quarantine
  modulus Q is *not* put into the system (its modulus may exceed T) — it is used only to lower-bound
  `δ(ℰ_T) ≥ δ/φ(Q)` (units `≡ r (Q)` with `F=1` lie in `S(ℰ_T)` by Lemma 2.5(i), Lemma 2.1 and
  `840|Q`, r a square mod 840). With (4) (Thm 3.3) `log Q, S_β ≪ ℒ³(log ℒ)^5` this gives
  `log p ≤ C(ℒ+Cℒ³(log ℒ)^5)`; `p>T ≥ 840` is coprime to 840, avoids the non-squares, hence is in a
  hard class; `W(p)>T` by Lemma 2.1. `ℒ ≥ c(log p)^{1/3}(log log p)^{−5/3}` uses `log ℒ ≤ log log p`.
  Correct. LS is indeed used once per T.
* LS sanity: I tried the obvious stress cases (single class mod `P(T)`: Linnik; Jacobsthal-type one
  class per prime; a Siegel-zero character with the avoiding set `{χ=−1}`: Linnik's theorem with
  Deuring–Heilbronn still gives primes in `(T,T^C]` for `q ≤ T`) — none refutes it; it remains a
  conjecture, as stated. The two remarks ("`C log T` cannot be dropped", "restriction to moduli
  `≤ T` matters") are correct.
* Prop 13.2(a) re-derived: `y=T^{1/2+ε}`, every atom has at most one prime `>y` (to the first
  power, `M ≤ T`); Lemma 2.2 kills atoms with all primes `≤ y`; `|B_ℓ| ≤ Σ_{v≤T/ℓ}τ(A_{vℓ}²) ≤
  T^{1/2−ε+o(1)}`. Correct asymptotically. **From scratch** `scripts/review_r64_ls_product.py`
  (T=1500): atom-class identity `{−uv^{−1}} = {−4D : D | A_M²}` for all `M ≤ T`; the unit squares
  mod 840 are exactly Mordell's six classes; every prime in `(T, 3·10⁶]` avoiding `ℰ_T` has
  `W(p)>T` by direct evaluation and is hard (and conversely); the product set S of (a) avoids every
  atom (component-wise check). (At T=1500 one has `max|B_ℓ|/ℓ = 0.90 > 1/2` — the `T^{o(1)}` of
  the divisor bound is not yet small; harmless for the asymptotic statement.)
* (b) sketch checked for logic: for each prime `q < ℓ₁/4` a blocked class at `ℓ₁` blocks only that
  q; for each class a mod 4q either all `ℓ₁ ≡ a` or all `ℓ₂ ≡ −a^{−1}` are blocked; BDH on
  average over `q ≤ √T(log T)^{−6}` (range `Q ≥ x(log x)^{−A}`, `x=√T`) supplies the class counts.
  I did not re-derive the exponent −8.

## Defects

**D1 (MINOR; Rem 11.4, "the binomial extrapolation of [SL, Lemma 8.3]").** The majorant bound
`k log(C(P+4k)/k)+O(k+log k)` is not Lemma 8.3 of [SL] (that is the one-dimensional Lagrange
extrapolation `B(z,t,d)`); it is the weighted k-ary comparison [SL, Thm 8.5] + mean cost
[SL, Cor 8.6] (thinned law Lemma 8.4, extrapolation Lemma 8.3) applied fibrewise with
`d=k`, `m̄=P`, `t=k/(P+4k) ≤ 1/4`, as in CEILINGS_UNIFIED Thm 4.1(U−). It also needs
`p_b ≤ 1/4` (true for the atoms). *Repair:* cite "[SL, Thm 8.5 and Cor 8.6 (via Lemmas 8.3–8.4)]"
and add "(for `p* ≤ 1/4`)". Numbering of [SL] checked on a fresh compile of
`sieve-limits-note.tex`: Lemma 8.3 = binomial Lagrange extrapolation, Thm 8.5 = weighted k-ary
comparison, Cor 8.6 = mean cost, Thm 10.14 = "no θ>3/4 for coefficient-sum CRT sieves".

**D2 (MINOR; Rem 11.4, "sharp for coefficient-sum congruence majorants [SL, Thm 10.14]" and
"conjunction of proved statements").** [SL, Thm 10.14] is labelled there "proved; Case A proved
mod Elsholtz–Tao Prop. 1.4, Thm 7.1, Cor 7.4, (7.10)", and its scope is: families of forced
classes (ℛ(M), (a,D), Case-A, selector), CRT majorants `≥ 0` on ℤ, all family primes `≤ N^A`,
`Σ|a_i| < N`. The Remark drops both the proviso and the hypotheses (this was D8 of the
CEILINGS_UNIFIED review; the note inherits it). Also [SL] itself is "internally reviewed, not
externally refereed" (bib says so, but the status conventions in §1 list only [TQ]). *Repair:*
"(for CRT majorants with coefficient sum `< N` and family primes `≤ N^A`; for Case-A classes
modulo Elsholtz–Tao §7)" and add [SL] to the status conventions alongside [TQ].

**D3 (MINOR; paragraph after Thm 11.2, "a matching lower bound in the range
`log T ≤ c(log x)^{1/4}/(log log x)^{O(1)}` would follow from the main term of Thm 6.1 except when
an exceptional character divides the quarantine modulus").** This is an unproved claim with no
label (the preceding sentence is tagged Assessment, this one is not). *Repair:* "(Assessment, not
checked)" or delete.

**D4 (MINOR; labels of Cor 12.3, the Siegel statement and Prop 13.2(b); status conventions §1).**
The conventions say "*Proved* means proved in full here" and define "proved modulo X" only for
the listed inputs; [O15], [O16] (repository working notes, internally reviewed) and [SL] are not
mentioned. Cor 12.3 is labelled "proved implication, same inputs" but its proof here is a
four-line sketch with a pointer to [O15, Cor 2.4] (Prop 2.5 for the averaged remark); the Siegel
statement ([O15, Thm 3.1]) has no label at all. The mathematics is fine (C6), but the label
overstates what the paper itself contains. *Repair:* label Cor 12.3 "proved implication in
[O15, Cor. 2.4]; sketch here", give the Siegel statement a label ("proved in [O15, Thm 3.1]"),
and add one sentence to the status conventions: results quoted from [O15], [O16], [SL] are
internally reviewed working notes, proofs sketched or referenced.

**D5 (MINOR; Prop 12.4, the examples "Bombieri–Vinogradov, Elliott–Halberstam, GRH restricted to
moduli ≤ x", and the intro/abstract lists).** The statements in `𝓘` are unweighted counts of
primes `≤ x` *at the single scale x*, restricted to the fibre H. BV/EH/GRH as usually stated
are for `ψ` (weights `log p`), with `max_{y≤x}`, on all primes. They enter the framework only
through their single-scale unweighted fibre consequences; certificates that combine scales or use
the weight `log p` use the archimedean position of the primes, which the definition of linear
certificate excludes (it is the "support" information of the Scope paragraph). This is the
intended scope (O15 §6 N2), but a reader of the examples will think the full statements are
covered. *Repair:* after the examples add "(in the form of their consequences for the
unweighted counts at the given x; information about several scales or the weight `log p`
uses the position of the primes in `[1,x]` and is outside the framework, see Scope)".

**D6 (MINOR/nit; §13 "Other strengths" (i), and intro sentence on product sets).** "A log-scale
counting form … implies LS(C+1)": the deduction needs `c₀T^{C+1}δ^{−1} ≥ 2log x/1`, i.e.
`T ≥ T₀(c₀,C)`; for small T the constant must be enlarged. Write "implies LS(C′) for some
`C′=C′(C,c₀)`". The intro's "applied to product subsets of the avoiding set, cannot certify more than
`(log p)^{2+o(1)}`" rests on Prop 13.2(b), i.e. modulo BDH (ineffective) — add "(modulo BDH)".

**N1 (nit; §11 title, line 2259).** `\texorpdfstring{$\Lc^4$}{L^4}` triggers "Token not allowed in a
PDF string … removing `superscript`" (bookmark reads "L4"). Use `{L\textasciicircum 4}` or `{L4}`
deliberately.

## Intro / abstract / §14 consistency (C8–C11)
* Thm 1.2 = Thm 11.2, Thm 1.3 = Thm 3.3 + Prop 11.1 (+ Thm 4.4 for the FL-only `ℒ³/log ℒ` form),
  Thm 1.4 = Thm 10.6 + Prop 11.3, Thm 1.5 = Thm 13.1: statements and labels agree.
* The optimality factors are arithmetic-correct: `(log log p)^{1/2}` from `ℒ⁴/log ℒ` vs Thm 1.1's
  `(log p)^{1/4}(log log p)^{−1/4}`; `(log log p)^{1/4}` modulo [TQ].
* Effectivity sentence (only Thm 1.1 effective, [TQ]-based results ineffective; NT constants not
  checked) is accurate; Thm 11.2 Case B uses Page (effective) but Case A uses [TQ] (BV, ineffective).
* §14 lists every new item with the right label; Rem 11.4 and the "heuristic two-sided typical size"
  are in the Assessment list (so D3 is only about the in-text sentence lacking its tag).
  "Not claimed" covers 1/3 unconditionally, the truth of LS, and arguments outside the scopes.
* Bibliography: [TQ] (with numbering date), [SL], [O15], [O16] honestly described as internal
  notes; [Dav] 3rd ed. GTM 74 (2000) correct; Chs. 20 (PNT for APs II, Page term) and 29
  (BDH, "An average result") are, to my memory, the right chapters — I could not access the book
  (not in `sources/`). The v4 TODOs ([ErdosSpencer], [Janson], [FI] numbering) remain open in
  source comments, as the author reports.

## Scripts (from scratch, not reusing the author's code)
* `scripts/review_r64_atoms.py` — [TQ] atom distinctness/activation/identity; Bonferroni `Q_r`.
* `scripts/review_r64_planted.py` — planted law: positivity, zero at `b=0`, k-wise marginals,
  `|E_ρ h| ≤ (4r*)^{k+1}` and `E_ρ h = 0` for `|I| ≤ k` (Lemmas 10.1, 12.1).
* `scripts/review_r64_ls_product.py` — atom classes, Mordell squares mod 840, the LS system `ℰ_T`
  vs direct `W(p)`, and the product set of Prop 13.2(a).
