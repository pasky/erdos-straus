# Review 3 of POINTWISE_OMEGA8.md — §6 only (R30c, hostile)

Reviewer: side agent `review-omega8c`. Scope: §6 (6.1 ledger, Lemma 6.1,
Thm 6.3, §6.4, §6.5, Prop 6.6) of POINTWISE_OMEGA8.md as on
`side-agent/haar-primes-2`. §§1–5 were reviewed in
`pointwise-omega8-review.md` and `-review-2.md` and are taken as given
except where §6 changes their inputs.

## Summary verdicts

| claim | verdict |
|---|---|
| §6.1 ledger (Thm 4.3 bookkeeping) | SOUND (but cites a non-existent Lemma 6.2: M1) |
| Lemma 6.1 (spectral bookkeeping) | SOUND (re-derived; numerics clean; m1, m2 cosmetic) |
| Thm 6.3 (`W ≥ exp(c(log p/log log p)^{1/13})`, mod TZ + ET) | SOUND; label correct |
| §6.4 counterexample (q-ary DT switching false) | SOUND-AFTER-REPAIRS (constant fix m3; ESW-consistency wording m4) |
| §6.4 "ESW would give exponent 1/11" | GAP (M1: needs Lemma 6.2 *and* a q-ary M_1 bound) |
| §6.5 ceilings (Assessment) | SOUND as heuristic after rewording (m5: "any minorant", "ceiling under ET") |
| (D) `Σ_{p≤x,p≡3(4)}τ(((p+1)/4)²) ≫ π(x)(log x)²` | true and standard (BV + Brun–Titchmarsh, ET §5 pattern); write out (m6) |
| Prop 6.6 (`S ≫ 𝓛²`) | SOUND modulo (D); label OK; can be strengthened to `log(1/δ) ≥ S1 ≫ 𝓛²` (m7) |
| §6.6 Consequence / report's "one opening" | Assessment; partly misleading (m8) |

No FATAL defects. One MAJOR (M1). Thm 6.3 stands.

## Defects

**M1 (MAJOR) — "ESW ⇒ exponent 1/11" is unsupported; Lemma 6.2 is
missing.** Locations: §6.1 item 2 ("Lemma 6.2 removes it" — no Lemma 6.2,
no §6.2/§6.3 exist); §6.4 parenthesis "`d≪𝓛⁵, K≪𝓛⁵log𝓛, log Z≪𝓛⁶`, i.e.
exponent 1/11"; header item 6; AGENT_REPORT_O30 §6.4 bullet. (i) `K≪𝓛⁵log𝓛`
requires Lemma 6.1's spectral M_1 bound, whose proof uses
`‖f̂_ρ‖₁≤2^{DT(f_ρ)}` and the bit-level *decision-tree* switching lemma; ESW
is an energy statement and gives no ℓ¹ control, so with ESW alone M_1 goes
through Lemma 3.2 and `K≍d𝓛≍𝓛⁶`. (ii) `log Z≪𝓛⁶` ignores
`log Q_Π≍k²S*𝓛≍𝓛⁷/log𝓛`, which only the absent Lemma 6.2 would lower (the
log-weighted-threshold remark after Thm 6.3 shows the obvious attempt does
not). As written ESW gives `𝓛¹³/log𝓛` (no real gain over 1/13).
*Repair:* replace "would give 1/11" by "would give 1/11 provided also (a) a
q-ary analogue of Lemma 6.1's ℓ¹ bound for ES truncations
(`log M_1 ≪ d log𝓛`) and (b) `|𝓑| ≪ kS*` (a Lemma 6.2, not yet proved)";
delete or supply Lemma 6.2; fix the header and report accordingly.

**m1 (MINOR) — Lemma 6.1 should say g_j is a function of the coordinates
outside supp E_j.** It is (F^{(j)} does not depend on them, so neither do its
Fourier truncation nor the blockwise pull-back; verified in the toy), and
Lemma 3.1's `E[A_je_j²]=P(E_j)E(F^{(j)}−g_j)²` needs it. Add one sentence.

**m2 (MINOR) — notation.** In Lemma 6.1, `ĝ_j(S)` should be the coefficient
of g̃_j (g_j lives on residues, not bits); d is used both for the degree and
for moduli `d_i` (Thm 6.3's `log Z` line). Rename the degree (e.g. D_0).

**m3 (MINOR) — §6.4 constants.** With `p=1/(2C)` and width k=2, the
hypothetical bound `(Cpk)^s` equals 1, so the example does not refute it as
written. Take `p:=1/(4C)` (any `p<1/(2C)`; then `(C(2p+q^{−1/2}))^s→0`
geometrically while `Pr[DT_q≥pN/2] ≥ c>0`; numerically ≈0.61 vs 10^{−37}
at q=10⁶, C=1). Also `Pr[fixed values distinct] ≥ e^{−1/2}−o(1)`, not just
`e^{−1}`.

**m4 (MINOR) — §6.4 "nearly constant in ℓ²".** At the typical `s≍pN`,
`Pr[f_ρ=1] ≲ Ns/q ≍ p`, a constant, not small; and `W^{≥1}≤Pr[f_ρ=1]` says
nothing about the `s`-geometric decay ESW requires. The exact ES weights
(q=49…144) do decay in the level, so the example is plausibly consistent
with ESW, but the stated justification is not an argument. Reword along the lines of: "the ES weight of f_ρ decays geometrically in
the level (ratio ≲s²/q in exact toys), although its decision depth is s";
proving this for the example would be a useful sanity check of ESW.

**m5 (MINOR) — §6.5 wording.** (a) "holds for any minorant" — there is no
argument that every PO-Thm-4.1 minorant needs junta ≳S; say "for minorants
of Brun/BRW type (heuristic)". (b) "≈1/9 is the ceiling under ET" (also
header item 6, report): ET gives an *upper* bound on S; 1/9 is what the
present bookkeeping yields with S only bounded by S*, not a ceiling. The
supported ceiling is via Prop 6.6 (`S1≫𝓛²` ⇒ exponent ≤1/4, Assessment).
(c) "log p ≳ S² up to logs" vs "S·S𝓛": per junta prime the cost is between
`log z` and `𝓛`, and 𝓛 is not a "log" in this bookkeeping; write
`log p ≳ S²·log z`. (d) "K≥log(1/μ)≈S": only `≥S1` is rigorous.

**m6 (MINOR) — (D) and partial summation.** (D) is correct and standard,
but (i) write out the 6-line BV argument (main term
`Σ_{d≤x^{1/3}}2^{ω(d)}/φ(4d)≍(log x)²`; error by Cauchy–Schwarz with
Brun–Titchmarsh and BV, exactly as ET §5 (5.7)–(5.8)); (ii) state it on
dyadic ranges `(x/2,x]` — the cumulative form plus "partial summation"
only yields `≫𝓛`, not `≫𝓛²`, without a matching upper bound. Label
"PROVED modulo (D) (standard; sketched)" is acceptable. The report's
"mass ≍𝓛²" also needs the (equally standard) upper bound; say `≫`.

**m7 (MINOR, improvement) — Prop 6.6 states less than it proves and than is
used.** The proof bounds the *distinct-class* single mass S1, so it gives
`S ≥ S1 ≫ 𝓛²` for the distinct-event mass S of Thm 3.4 (not just the atom
count S_tot), and, singles at distinct primes being independent,
`δ ≤ ∏(1−g_ℓ) ≤ e^{−S1}`: `log(1/δ*) ≫ 𝓛²` and `K ≥ log(1/μ) ≫ 𝓛²`
rigorously (mod D). State that; §6.5/§6.6 use exactly this.

**m8 (MINOR) — §6.6 Consequence / report "one opening".** Splitting off
the singles (Brun for singles, BRW for the rest) cannot lower K: any
minorant B≤F has `μ≤δ≤e^{−S1}`, so `K≳𝓛²` regardless; only `log Z` could
shrink. Also `log Z≥log ℓ_aux>𝓛`, so PO Thm 4.1's sufficient condition can
never be met below `log p≈𝓛³` on this route. Say so, so that the successor
does not chase `S_{≥2}` expecting to beat the K-side.

### Working notes, Lemma 6.1 (re-derived)

* Restriction identity: for ρ=(I,z), S⊆I, f̂_ρ(S)=Σ_{T⊆I^c} f̂(S∪T)χ_T(z),
  so E_z f̂_ρ(S)=f̂(S). Then Σ_S p^{|S|}|f̂(S)| = Σ_S E_I[1_{S⊆I}|E_z f̂_{I,z}(S)|]
  ≤ E_ρ‖f̂_ρ‖_1. Re-derived; correct (this is Mansour's argument).
* ‖f̂_ρ‖_1 ≤ #leaves ≤ 2^{DT(f_ρ)} (|f|≤1, path indicators have spectral
  norm exactly 1). E 2^{DT} ≤ Σ_s 2^s Pr[DT≥s] ≤ Σ_s 2^{-s} = 2 with
  p=1/(4C_H w). Correct (Håstad in O'Donnell's form holds for all s≥0).
* Σ_{|S|<d}|ĝ̃(S)| ≤ p^{-(d-1)}·2 ≤ 2(4C_H w)^d. Correct.
* M_1 accounting: PO Thm 4.1 has M_1=Σ|c_i|/φ(d_i), i.e. Haar-weighted ℓ¹;
  a bounded function h of a coordinate set J, expanded over the unit cells
  on J, has M_1 = E_Haar|h| exactly. With |χ̃_S|≤1 (conditional expectation
  of a ±1 function) and h=A_iA_jA_{j'}χ̃_Sχ̃_{S'}, M_1(h) ≤ E[A_iA_jA_{j'}] ≤ 1.
  Total: 1 + m + 2m²·‖ĝ̃‖_1 + m³‖ĝ̃‖_1² ≤ 1+m+4m²X+4m³X² ≤ 10m³X²,
  X=(4C_Hw)^d, so log M_1 ≤ 3log m + 2d log(4C_Hw) + log 10 ≤ … + 4. Correct.
* Independence needed for E[A_je_j²]=P(E_j)E[(F^{(j)}−g_j)²]: g_j must be a
  function of the coordinates outside supp E_j only. True if the encoding is
  applied to F^{(j)} as a function of those coordinates (as Lemma 4.1 says).
  Not stated in Lemma 6.1 — see MINOR defect m1.
* From-scratch numerics (`scripts/review_o8c_spectral.py` →
  `data/review_o8c/spectral.txt`). Part A: 36 random DNF/p cases on 5–7
  bits, exhaustive over all restrictions with exact decision-tree depth:
  restriction identity exact (error 0), `Σp^{|S|}|f̂(S)| ≤ E‖f̂_ρ‖₁ ≤ E2^{DT}`
  and `‖f̂_ρ‖₁ ≤ 2^{DT(f_ρ)}` pointwise hold in all cases. Part B: q-ary toy
  (3 coordinates on [3], 2-bit encoding with non-uniform fibres), pulled-back
  Fourier truncations at d∈{2,3,5}, 24 cases: every χ̃_S satisfies |χ̃_S|≤1,
  depends only on the blocks touched by S and never on supp E_j; Jensen
  `E_{π*}(F−g)² ≤ E(F̃−g̃)²` holds; `B≤F` pointwise; cell-expanded
  `M_1(B) ≤ 1+m+2m²L+m³L²` (L = truncated ℓ¹ norm). No failures.

### Working notes, §6.4 counterexample (re-derived + numerics)

* Masses: per-coordinate `(N−1)/q ≤ q^{−1/2}`, total `C(N,2)/q ≤ 1/2`. Correct.
* Adversary argument re-derived: with the N−s fixed values distinct, answering
  each query with a value distinct from all fixed and earlier answers
  (possible since N+s<q) leaves f_ρ non-constant until the last query
  (last free coordinate can still hit or avoid). So `DT_q(f_ρ)=s`. Exact
  minimax DT_q (`scripts/review_o8c_counterex.py` → `data/review_o8c/counterex.txt`)
  confirms `DT_q(f_ρ)=s` for q∈{9,16,25}, all s tested.
* Quantitative failure: with `p=1/(4C')`, `Pr_ρ[DT_q ≥ pN/2] ≈ 0.61` for
  q=10⁴…10⁸ while `(C'(2p+max w_ℓ))^{s_0}` is 10^{−3.5}…10^{−376}. The
  counterexample is valid **after a constant fix** (defect m3: with the
  doc's `p=1/(2C)` and k=2 the hypothetical bound `(Cpk)^s` equals 1).
* ES level weights of f_ρ (exact, q=49…144): W^{=1} dominates and W^{=r}
  decays in r (e.g. q=49,s=4: 1.0e−1, 1.2e−1, 8.2e−2, 1.4e−2, 1.7e−3 for
  r=0…4, r=0 being the squared mean). So the example is plausibly
  consistent with ESW, but the doc's justification is too weak (m4):
  `Pr[f_ρ=1] ≲ Ns/q ≈ p` at the typical `s≍pN` is a constant, not "nearly
  constant"; and `W^{≥1} ≤ Pr[f_ρ=1]` says nothing about the
  geometric decay in s that ESW demands for s≥2.

### Working notes, §6.1 ledger and Thm 6.3

* Ledger rows re-derived with `z=𝓛²`, `k≍𝓛/log𝓛`, `b≈2log₂T`,
  `S≤S*≪𝓛⁴log𝓛`: `w=kb≍𝓛²/log𝓛`; `k_0≍S+log m≍S*`; `t=2C_Hwk_0≍𝓛⁶`;
  Lemma 3.2 gives `log M_1≍t𝓛≍𝓛⁷`; `log max d_i≤(3k+2t)𝓛≍𝓛⁷`;
  `log Q_Π≤(π(z)+64k²S*)𝓛+4≍𝓛⁷/log𝓛`; `K≍𝓛⁷`, `log p≍𝓛¹⁴`. All correct.
* PO Thm 4.1 uses `K=1+log(M_1/μ)`, `log x ≥ C_1K·max(log Z,K)`. With
  Lemma 6.1, `μ≥0.99δ≥0.99e^{−2.2S}`: `K ≤ 3log m+2d log(4C_Hw)+2.2S+6`
  (1+4+log(1/0.99)<6). `d=4C_Hwk_0=2t≪𝓛⁶`, `log(4C_Hw)≪log𝓛`,
  `log m≤(k+2)𝓛≪𝓛²`: `K≪𝓛⁶log𝓛`. Moduli on `≤3k+2(d−1)` primes:
  `log Z≤log Q_Π+2(3k+2d+1)𝓛≪𝓛⁷`. `log p≪𝓛¹³log𝓛`, which inverts to
  `𝓛≫(log p/log log p)^{1/13}`. Correct. The gain is real: Lemma 3.2's
  `log M_1≍t𝓛` becomes `≍t log𝓛`; `log Z` is unchanged in order (d=2t).
* Lemma 3.3 (twist) uses only `E[F−B]≤EF/100`, `w_ℓ≤1/(64k)` and that B is
  a cell combination whose ψ-twist equals `E[Bψ]`; all unchanged. (I) and the
  class-of-one argument do not see u_j. So Thm 6.3 inherits §§3–4 verbatim.
* **Lemma 6.2 does not exist** in the document (§6.1 item 2 cites it; there
  is no §6.2/§6.3 heading either). This matters for the "ESW ⇒ 1/11"
  claim: see M1.

### Working notes, Prop 6.6 and input (D)

* Atoms (O2 §4/§11): `M≤T`, `M≡3 (4)`, `D|A_M²`, survives Π iff `m_Π|4D+1`
  and `r_Π>1`; weight `1/φ(r_Π)`. For `M=ℓ∉Π` prime: `m_Π=1`, `r=ℓ`,
  survives every Π not containing ℓ; weight `1/(ℓ−1)`. Correct.
* Distinct classes: D≤A_ℓ ⇒ `4D∈[4,ℓ+1]`, so `−4D mod ℓ` are distinct and
  nonzero; their number is exactly `(τ(A_ℓ²)+1)/2` (A_ℓ² a square).
  Verified for the first 400 ℓ≡3 (4) (`scripts/review_o8c_divsum.py`).
* Quarantine loss: each removed ℓ>√T costs `≤τ(A_ℓ²)/(ℓ−1) ≤ T^{−1/2+o(1)}`;
  `T^{1/3}` of them cost `o(1)`. `|𝓑|≤64k²S*≤T^{o(1)}` unconditionally
  (O2 Lemma 11.1). Correct.
* (D) is true and standard. Re-derived: `τ(n²)=Σ_{d|n}2^{ω(d)}` (check at
  `p^a`: `2a+1=1+2a`); `d|(p+1)/4 ⟺ p≡−1 (4d)`; keep `d≤x^{1/3}`; main term
  `li(x)Σ_{d≤x^{1/3}}2^{ω(d)}/φ(4d) ≍ π(x)(log x)²`; error
  `Σ2^{ω(d)}|E(x;4d,−1)| ≤ (Σ4^{ω(d)}·x/d)^{1/2}(Σ|E|)^{1/2} ≪ x(log x)^{2−A/2}`
  by Brun–Titchmarsh + BV. Same pattern as Elsholtz–Tao §5 (their (5.7)–(5.8),
  checked in sources/elsholtz-tao-1107.1010.pdf: BV + Cauchy–Schwarz on a
  divisor-weighted sum of D(N;q)). Not literally stated there; a 6-line proof
  should be written out (m6).
* Partial summation: (D) as a *cumulative* lower bound does not by itself
  give the dyadic lower bounds needed for `Σ_{ℓ∈(√T,T]}τ/ℓ ≫ 𝓛²` (it only
  gives `≫𝓛` via `(A(T)−A(√T))/T`). The BV argument gives (D) on each
  `(x/2,x]` equally, so this is a wording fix (m6).
* Numerics (`data/review_o8c/divsum.txt`, T up to 10⁸, exact): the m=1 single
  mass `S1(T)=Σ_{ℓ∈(√T,T]}(τ(A_ℓ²)+1)/(2(ℓ−1))` has `S1/𝓛²` =
  0.051, 0.050, 0.048, 0.047, 0.047 at T=10³,10⁴,10⁶,10⁷,10⁸; the (D)-ratio
  `Σ_{p≤T,3(4)}τ/(π(T)𝓛²)` ≈ 0.19→0.217 and its dyadic version ≈ 0.235,
  both stable. Consistent with `S1≍𝓛²` (heuristic constant ≈0.04).
* Strengthening worth stating: singles at distinct free primes are
  independent, so `δ = E F ≤ ∏_ℓ(1−g_ℓ) ≤ exp(−S1)`; hence
  `log(1/δ*) ≫ 𝓛²` and, since `μ≤δ`, `K ≥ log(1/μ) ≫ 𝓛²` *rigorously*
  (mod D). This is what §6.5/§6.6 actually use; the Prop as stated (about
  `S_tot`, an atom count with multiplicity) is weaker than what is proved.

### Working notes, "ESW ⇒ 1/11" (§6.4 end, header item 6, report)

The chain `d≪𝓛⁵, K≪𝓛⁵log𝓛, log Z≪𝓛⁶ ⇒ 1/11` has two unsupported links.
(i) `K≪𝓛⁵log𝓛` needs Lemma 6.1's *spectral* bound on M_1, and that bound
uses `‖f̂_ρ‖₁ ≤ 2^{DT(f_ρ)}` plus Håstad's *decision-tree* lemma on the bit
encoding. ESW is an energy statement in the q-ary product space; it gives
no ℓ¹/M_1 control (and §6.4 shows the decision-tree route is false q-arily).
With ESW alone, M_1 must go through Lemma 3.2: `log M_1≍d𝓛≍𝓛⁶`, so
`K≍𝓛⁶`. (ii) `log Z≪𝓛⁶` ignores `log Q_Π≍k²S*𝓛≍𝓛⁷/log𝓛`; lowering it
needs the non-existent "Lemma 6.2". With both as written, ESW gives
`log p≪𝓛⁶·𝓛⁷/log𝓛 = 𝓛¹³/log𝓛`, i.e. essentially still 1/13; with a
Lemma 6.2 but no q-ary spectral bound, `𝓛¹²` (1/12). 1/11 needs ESW **and**
an M_1 bound `log M_1≪d log𝓛` for q-ary ES truncations **and** Lemma 6.2.

### Working notes, §6.5 (Assessment)

* "K≥log(1/μ)≈S": only `K≥log(1/μ)≥log(1/δ)≥S1` is rigorous (see Prop 6.6
  notes); `log(1/δ)≈S` for multi-prime events is heuristic (no FKG for
  cell events). Fine under the Assessment label, but say so.
* "junta ≳ S/log(junta/S) … holds for any minorant": no argument is given
  that *every* minorant consumed by PO Thm 4.1 needs junta ≳ S; this is a
  heuristic from Brun/fundamental-lemma level requirements. "any minorant"
  is an overclaim even for an Assessment.
* "≈1/9 is the ceiling under ET" (§6.5, header item 6, report): ET gives an
  *upper* bound `S≤S*`; a ceiling needs a *lower* bound on S. What 1/9 is:
  the best this bookkeeping can give when S is only known to be ≤S*. The
  actual ceiling statement supported by the doc is Prop 6.6's `S1≫𝓛²` ⇒
  `log p ≳ 𝓛⁴·log z` ⇒ exponent ≤1/4 (Assessment). Also `log p ≳ S²
  "up to logs"` vs. the ideal-junta value `S·S𝓛` differ by a factor between
  `log z` and `𝓛` per junta prime; `𝓛` is not a "log" in this exponent
  bookkeeping (it is the variable). State the bound as `S²·log z ≲ log p`.

## Replay (from-scratch reviewer scripts)

```
export PYTHONPATH=scripts
(ulimit -v 8000000; uv run python scripts/review_o8c_spectral.py 1)   # ~2 min -> data/review_o8c/spectral.txt
(ulimit -v 8000000; uv run python scripts/review_o8c_counterex.py)    # ~1 min -> data/review_o8c/counterex.txt
(ulimit -v 8000000; uv run python scripts/review_o8c_divsum.py 8)     # ~1 min, ~1 GB -> data/review_o8c/divsum.txt
```

Sources: Elsholtz–Tao checked in `sources/elsholtz-tao-1107.1010.pdf` (§5,
lower bound for Σ f_II(p) via BV). Håstad / O'Donnell / LMN not re-opened
(not in sources/); their use in Lemma 6.1 is the textbook Mansour-type
argument, which I re-derived and tested numerically.
