# Hostile referee report: `paper/sieve-limits-note.tex`

Subject: `paper/sieve-limits-note.tex` at branch `side-agent/sieve-limits-paper`
(checked out into this worktree together with `reviews/agent-reports/AGENT_REPORT_O8.md`).
Sources: `EXCEPTIONAL_THETA.md` [ET], `EXCEPTIONAL_BALANCED.md` [EB],
`EXCEPTIONAL_TWIN.md` [TW], `EXCEPTIONAL_TWIN2.md` [TW2],
`EXCEPTIONAL_TWIN3.md` on `side-agent/twin-equidist` [TW3], their reviews, and
`paper/es-threequarter-note.tex` [TQ].

Verdict: **MINOR REVISION** (14 numbered defects D1–D14; no mathematical error; see §6).

## 0. Compilation

`pdflatex` ×3 in a scratch copy: 22 pp, 0 errors, 0 overfull boxes, 0
undefined references/citations. Three harmless underfull hboxes (lines
1277–1283, 1581–1583, 1591–1593 — the last two are bibliography entries
with long `\texttt` file names). **Compiles clean.**

## 1. §§1–3: introduction, forced classes, architecture class

Checked line by line against ET §§0–1, 2.4 (scope remark), 2.7, 3, ETrev
item 3, notes.md Lemma 18.1 / Thm 3.1, LL Lemma 2.1, TQ §2.

**Proofs re-derived (all correct).**
* Lemma 2.1 (identity): numerators over `nsuvw` are `nv, u, s`; sum
  `s(M+1) = 4suvw`. ✓
* Lemma 2.2 (ℛ(M)): `v⁻¹ ≡ uwA⁻¹ ≡ 4uw (mod M)` since `(v,M) | (A,4A−1) = 1`;
  converse exponent split ✓.
* Lemma 2.3 ((a,D)): `(n+4D)/a = 4gj−1`, `D | g² | A²` ✓.
* Lemma 2.4 (Case A): `g(d) | z₀ ⇒ d | z₀²`; `m | 4d+1+nm = 4(d+z₀)` and m
  odd ⇒ `m | d+z₀`; y integral because `d·[z₀(d+z₀)/d] ≡ 0 (mod m)` and
  `(d,m)=1`; `1/x+1/y = m(z₀+d)/(z₀(d+z₀)) = m/z₀` ✓.
* **Lemma 2.6 (Mordell/Jacobi).** `D = sr²`, s squarefree; `v_p(D) ≤ 2v_p(A)`
  gives `v_p(r)+1 ≤ v_p(A)` for `p | s`, so `sr | A` and `4s | M+1`.
  `(−4D/M) = (−1/M)(s/M) = −(s/M)`. s odd: reciprocity with `(M−1)/2` odd
  gives `(s/M) = (−1)^{(s−1)/2}(M/s) = (−1)^{(s−1)/2}(−1/s) = 1`. s = 2s':
  `8 | M+1 ⇒ (2/M) = 1`, and s' as before. Consequence: `(n/M) = 1 ≠ −1`.
  **Correct.**
* **Lemma 3.4 (= ET Lemma 2.9, budget ⇒ level).** Verbatim from ET §2.7 /
  ETrev item 3 (Lemma R). Re-derived: a negative term of level > λ has
  `d_i ≥ e^λ`; a truncated positive term keeps a prefix of level
  `> λ−Λ₀` (prefix + next prime > λ, next prime ≤ Λ₀), so
  `a_i/d'_i ≤ a_i e^{Λ₀−λ}` (also fine when the prefix is empty);
  `ν' ≥ ν` pointwise so ν' is a majorant; `λ = Λ₀+log T+log(1/Eν)` gives
  `T e^{Λ₀−λ} = Eν`. **Correct.**
* Cor 3.5: `λ' ≤ A log N + log N + s`, `s − log 2 ≤ Cλ'^{3/4} + C'`; split
  `s ≤ (A+1)log N` vs. `s > (A+1)log N` (then `s ≤ C(2s)^{3/4}+O(1)`, so
  s = O(1)). **Correct** — but see D2 for the form of the hypothesis it
  is fed with.
* Remark 3.6 (positivity on ℤ): faithful to ET §2.4 scope remark.

**Faithfulness.** Definitions 3.1–3.3 match ET §1 and the review's
repaired architecture (ETrev SC1 fix: "final bound `N·Eν + Σ|a_i|`,
family moduli ≤ N^{O(1)}"). (A1)–(A3) are a faithful rendering. Nothing
strengthened in §§2–3.

**Defects found here.**

* **D1 (MINOR, status labels / abstract).** The abstract overstates two
  scopes relative to the body and the sources:
  * "a Λ² cap … twin moduli included, for families whose moduli have at
    most two prime factors above (log X)^8" drops *four* hypotheses of
    TW2 Cor 5.2 / TW3 Cor 4.2: ℛ(M)-classes only, `M ≤ P(M)^{1+B}` with B
    fixed, `M ≤ X`, level `λ ≤ A₀ log X` (and no budget ⇒ level reduction,
    as the paper itself says after Thm 10.7). Read literally the abstract
    claims a Λ² cap for (a,D)/Case-A classes and for unbounded
    `log M/log P(M)`, which is not proved.
  * "for the classes ℛ(M), for families of gapped moduli" drops
    "(η,B)-gapped, B fixed" and, in both cases, "with the admissible set
    of Cor 6.2 / the QR base" (the Main Theorem has these; the abstract
    and Results item 2 do not).
  * Also: abstract says "family moduli ≤ N^{O(1)}", (A3) says "slice primes
    ≤ N^A". Harmless (the abstract's version is stronger as a hypothesis)
    but should agree.
  *Fix:* add "of ℛ(M)-classes with `M ≤ P(M)^{1+B}`, B fixed, at level
  O(log X)" to the Λ² sentence; "(η,B)-gapped" and "with a bounded-saving
  admissible set of the specified form" to the other.
* **D2 (MINOR, proof assembly).** Cor 3.5 needs the hypothesis "every
  majorant of level λ has saving ≤ Cλ^{3/4}+C'" for λ up to
  `(A+1)log N + s`, which can exceed `A log N`. But Cor 6.1 and Cor 6.2
  are stated only for `λ ≤ A log N` with right side `C(A,C)(log N)^{3/4}`.
  The Main Theorem's one-line proof ("Cor 3.5 applied with Cor 6.2")
  therefore feeds Cor 3.5 a statement of the wrong shape. The gap is
  cosmetic: the proofs of Cor 6.1/6.2 give `≪_C λ^{3/4}` for every λ (the
  window sum is `≪_C λ^{3/4}` with no reference to N), and ET's own
  "Consequence" paragraph after Lemma 2.9 implicitly uses the λ-form. ETrev
  item 3 notes "Level ≤ A log N is literal in Cor 3.4/3.6". *Fix:* state
  Cor 6.1/6.2 as `log(1/Eν) ≤ C(C)λ^{3/4} + (R-term)` for all λ ≥ 1 (or ≥
  log w₀) and derive the `(log N)^{3/4}` form; or restate Cor 3.5 with
  "for all λ ≤ (A+2)log N" and handle `s > log N` separately (`s ≤ log(1/Eν)`
  then contradicts the cap at λ' ≤ 2s+…).
* **D3 (MINOR, citation).** §1: "Vaughan proved … with Montgomery's large
  sieve [M]" cites a 1978 survey for a 1970 proof. Vaughan's paper is not
  archived (`sources/vaughan-1970-access-log.md`); `sources/README.md`
  says claims about his method are to be attributed through PW §4, which
  says "Exploiting the large sieve, the proof is largely derivative of
  Vaughan's theorem" (`sources/pw.txt` l. 72, 455). *Fix:* "with the
  large sieve (see the reconstruction in [PW, §4]); for the inequality
  see [M]".


## 2. §§4–6: sieve-limit theorem, profiles, the 3/4 cap

Checked against ET §§2.1–2.7, 3, 3.7 and ETrev items 1–4.

**Faithfulness.** Lemmas 4.1–4.3, Prop 4.4, Thm 4.5, Remarks 4.6–4.7,
Thm 4.9, Lemma 4.10 are ET Lemmas 2.1–2.3, Prop 2.4, Thm 2.5 (with its two
caveats), Thm 2.7, Lemma 2.8, essentially verbatim, hypotheses intact
(`|F_ℓ(c)| ≤ ℓ/4` only for `ℓ ≤ e^λ`, `< ℓ` always; truncated mass; G).
Lemmas 5.1–5.3 are ET Lemmas 3.1, 3.2 (profile part), 3.7, with Lemma 5.3
correctly labelled *proved mod* Elsholtz–Tao Prop 1.4. Lemma 5.1 adds an
explicit elementary `d = 1` case (Shiu is quoted for `q ≥ 2`); this is a
correct tightening, consistent with TQ §3. Cor 6.1 = ET Cor 3.4,
Cor 6.2 = ET Cor 3.6 (+ ET §3.7 for Case A), Thm 6.3 = ET "Consequence"
paragraph after Lemma 2.9 + TW Thm 2.7. Verified against
`sources/elsholtz-tao-1107.1010.pdf` (text l. 318–321): Prop 1.4 is quoted
verbatim (`A,B > 1`, `k ≪ (AB)^{O(1)}`, bound `AB log(A+B) log(1+k)`).

**Proofs re-derived.**
* Prop 4.4 Step 1: `2^G s_* > λ` since `G = ⌊log₂(λ/s_*)⌋+1`, so the bands
  cover every `s_i ≤ λ`. Step 5: `Σ_g 19α j_g s_g ≤ 19αλ`. ✓
* Thm 4.5: fibre reduction `Eν ≥ (|R|/Q₀) avg_c E[ν|c]` uses only ν ≥ 0;
  `{c}×{x=0} ⊆ 𝒜` with positive probability. ✓
* Remark 4.8 (large sieve): the added condition `p_ℓ(c) ≤ 1/2` is exactly
  what makes `g_ℓ = p/(1−p) ≤ 2p`, and ETrev item 3.4 already reads the
  Rankin step "for `p_ℓ ≤ 1/2`". The author's `% TODO` (report point 1)
  is resolved in the author's favour.
* Cor 6.2 R-term: `c ≡ 1 (mod L')` avoids every w₀-smooth condition by
  Lemma 2.5, so `|R|/Q₀ ≥ 1/L'`; `P(c≡a (q) | R) ≤ L'·P(c≡a (q) | (c,P_{w₀})=1)
  ≤ L'/φ(q)`. (U): `ℓ(M) > √M` occurs once and the cofactor primes are
  `≤ ℓ^C`, i.e. in an earlier window `(e^{s_{j'}}, e^{s_{j'}/C}]` or in Q₀. ✓
* **Main Theorem 6.3 assembly.** Case (i): Lemma 3.4 with `Λ₀ = A log N`
  (all charged primes are ≤ the dominant prime ≤ N^A), Cor 3.5, Cor 6.2
  with R-term `O_C(1)`. Case (ii): same with Thm 7.6, R-term
  `Σ_{p≤W₀(B)} log(2p/(p−1)) = O_B(1)`, constant `≪ η^{−1}` inside, so the
  final constant depends on `A, B, η` (report point 3 — correct; the
  bootstrap does not preserve linearity in η^{−1}). Majorants with a
  *larger* admissible set R' ⊇ R are majorants of the smaller avoider set,
  so the cap covers them too (TWrev item 8 makes the same point); a
  smaller R' is outside (exclusion 5). The assembly is **correct modulo
  D2** (shape of the Cor 6.1/6.2 hypothesis).

**Defects.**

* **D4 (MINOR, status labels).** Cor 6.1 and Cor 6.2 are headed
  `\lab{proved}` but their statements include Case-A classes (Cor 6.1,
  first bullet "or a Case-A class"; Cor 6.2 "and Case-A classes (modulo
  G = 4rh)"). The Case-A profile is Lemma 5.3, *proved mod*
  Elsholtz–Tao Prop 1.4. In ET, Cor 3.4/3.6 are Case-B statements and the
  Case-A extension sits in §3.7 with the "modulo Prop 1.4" qualification.
  The Main Theorem header gets this right; the two corollaries feeding it
  do not. *Fix:* "\lab{proved}; for Case-A classes \lab{proved mod}
  Elsholtz–Tao Prop 1.4", as in Thm 6.3.
* **D5 (MINOR, Results list).** Results item 1 says the sieve limit holds
  "+ O(log²λ)". That is only true under `s_* ≫ 1`, `log μ̄ ≪ log λ`
  (Remark 4.6); in general the error is `≍ λ log λ` (ET §2.4 "Size of the
  error term"). *Fix:* add "(in all applications here)" or cite
  Remark 4.6.
* **D6 (NIT).** Remark 4.8: delete the `% TODO` comment; cite ETrev
  item 3.4 for the `p_ℓ ≤ 1/2` reading.
* **D7 (NIT).** §7.1, "for every η ≤ min(η₀, 1/C−1)": η₀ is never
  defined in the paper (EB: "η₀ < 1 fixed"). Define or drop it (η < 1 is
  already assumed).

## 3. §§7–8: gapped moduli; the campaign sieves

Checked against EB §2 (Lemma 2.1, Lemma 2.4, Lemma 2.5a, Thm 2.5 window
sum), TW §§1–2, 4 (Lemma 1.3, Lemmas 2.1–2.2, Thm 2.3, Lemma 2.4, Cor 2.5,
Lemma 2.6, Thm 2.7, Lemma 4.0, Prop 4.1, Lemma 4.2/Cor 4.3, Thm 4.4), TWrev
(both rounds), ET §4, TQ §§2, 8, 10.

**Faithfulness.** All §7 statements match the sources with hypotheses
intact: `(η,B)`-gapped with `P(M) > W`, B fixed, `0 < η < 1`, `W = W₀(B)`,
caps `δ_ℓ = ℓ^{−1/2}`, \ℛ(M)-classes only, plus W-smooth \ℛ(M)-classes.
The scope paragraph after Thm 7.6 reproduces TW §2.3 "Scope" exactly.
Thm 7.7 = TW Thm 4.4 (`λ ≥ (2 log W)^4`, `M ≤ P(M)^{1+B}`, window-resolved
in `(e^{λ^{1/4}}, e^{λ/2}]`) and is correctly marked as stated-with-
proof-cited. §8 matches ET Lemmas 4.1–4.4 / Cor 3.5; TQ citations checked
by label numbering (Lemma 2.2 = lem:CRT, Cor 4.3 = cor:fibremass,
Thm 8.2 = thm:assembly, §10 = heuristic ceiling with θ = 𝓑/(𝓑+1)):
`|F_ℓ(c)| ≤ z_j² ≤ ℓ^{1/3}` (TQ l. 222), `T_abs ≤ N^{1/2}`, "convenient but
not necessary" (TQ l. 1195–1196), `Q_r(0) = 1`, `Q_r(h) = C(h−1,r) ≥ 0`.

**Proofs re-derived.**
* Lemma 7.1 (gapped ⇒ (U)) ✓. Lemma 7.2 (QR base): odd `p ≤ W` factor has
  `p^{e−1}(p−1)/2` of `p^e` elements, so `γ(p) = 2p/(p−1)`; (1) is
  Lemma 2.6 since `c mod Q₀` determines `c mod M` for W-smooth `M | Q₀`. ✓
* Lemma 7.3 and Thm 7.4 (capped measure): the induction, the
  `f̃(0) = 0` case, and the final Jensen on `Q'(·|𝒜)` with
  `Q'(𝒜) ≥ 1/2` giving `½e^{−2E S}` (uses `S ≥ 0`) ✓.
* Lemma 7.5: `E N_ℓ² ≪ ℓ^{ε/2} Σ_{m≤ℓ^{2B}} 3^{ω(m)}τ(m²)/m ≪ ℓ^ε`; leak by
  Markov `E[p 1{p>δ}] ≤ E p²/δ`, `Σ_{ℓ>W} ℓ^{−5/4} ≪ W^{−1/4}` ✓.
* **Thm 7.6 constants** (from EB Thm 2.5): `X(s*) = 19λ/s*`, so
  `2X(s*)/η = 38λ/(ηs*)`; above `s*`, `log⁺(X_j s_j/19λ) = 4 log(s_j/s*)
  ≤ 4(k+1)log(1+η)`; `Σ_k(1+η)^{−k}(1+4(k+1)log(1+η)) ≤ (1+η)/η +
  4(1+η)²/η ≤ 18/η`; `38 + 19·18 = 380` ✓; then
  `380λ/(ηs*) = 380(C₄K(1+B)³/19)^{1/4} η^{−1} λ^{3/4}` and ×2 ✓.
* Lemma 8.2 (Bonferroni depth): Chebyshev `P(H ≤ r) ≤ P(|H−μ| ≥ 2√μ) ≤ 1/4` ✓.
* Cor 8.3: `t = ut₀`, second entry `≤ (38λ/(ut₀))(1 + log⁺(Cu³))` ✓.

**Defects.**

* **D8 (NIT, wording).** §8.2: "its bound cannot exceed
  exp{−C(log N)^{2/3}(log log N)^{1/3}}" is backwards as English (the
  *saving* cannot exceed `C(log N)^{2/3}(log log N)^{1/3}`, i.e. the bound
  cannot be *smaller* than `N exp{−C…}`). Inherited from ET Lemma 4.4.
  *Fix:* rephrase in terms of saving.
* **D9 (NIT).** Lemma 8.1 statement "equals 1 on 𝒜": correct (`S_y = 1`,
  `H_X = 0` there), but TQ Thm 8.2 only asserts "≥ 1 on exceptional
  primes". Add "(since `Q_r(0) = 1`; ETrev item 3.1)" so the reader sees
  this is the whole-avoider-set property the architecture needs, which the
  note itself does not state.

*Addendum to D2.* A one-line repair that needs only the `(log N)`-form of
Cor 6.1/6.2: apply Lemma 3.4 with `λ = (A+2) log N`; then
`Eν' ≤ Eν + T e^{Λ₀−λ} ≤ Eν + N·N^{A}·N^{−A−2} = Eν + N^{−1}`, so
`min(s, log N) − log 2 ≤ C₈(A+2,C)(log N)^{3/4} + O(1)`, hence
`s ≪ (log N)^{3/4}` for large N. Either fix is fine.

## 4. §§9–11: exclusions, Selberg-type majorants, open problems

Checked against ET §§3.8, 5.6, 5.7, 6, 6.1; TW §§4.4, 6.3, 6.6, 6.8;
TW2 §§1–5 and its review (rounds 1–2); TW3 (current `main` version,
commit 874be8d) and its review (current `main`, rounds 1–2).

**Faithfulness.**
* §9 list = ET §6.1 items 1–5, 7, 8, updated for TW Thm 2.7/4.4 and
  TW2/TW3. ET item 6 (the prime-slice requirement of Cor 3.4) is folded
  into item 7 "Large multipliers"; acceptable.
* Lemma 9.1 = ET Lemma 3.8 (η ∈ (0,1/480], the stated ranges, `Y =
  x^{1/(2+4.5η)}`); proof is a marked sketch citing ET §3.8 / ETrev
  item 4.2 (SOUND). The lattice input is LL Lemma 3.1 = TQ eq. (latlower) ✓.
* Thm 10.1 = ET Thm 5.5; proof re-derived: `P(A) ≤ ⟨g, Π_V 1_A⟩ ≤
  ‖g‖‖Π_V 1_A‖`, and on `c(T) ≤ λ/2`, `1 ≤ e^{αλ/2}e^{−αc(T)}`, giving
  `‖Π_V1_A‖² ≤ e^{αλ/2}P(A∩A')`; `Ξ ∈ [0, log 1/P(A)]` since `T_ρ ⪰ 0` and
  `P(A∩A') ≤ P(A)`. ✓ Cor 5.6 factor `1 + ρp/(1−p) ≤ 1 + (4/3)ρp` ✓.
* Hyp 10.2 = ET H_MS^{Sel} (open), conditional consequence labelled
  \lab{conditional} ✓. The fibre counterexample ✓.
* Lemma 10.3 = TW Lemma 6.6 (uniform P; proof re-derived:
  `⟨h,T_ρh⟩ = Q_F Σ π_c² e^{Ξ_c}`, optimum `π ∝ e^{−Ξ}`, Jensen) and
  TW2 Lemma 2.1 (general P; reviewed SOUND) ✓.
* Thm 10.4 = TW2 Thm 1.4 (`w_ℓ ≤ δ ≤ 1/16`, constant `1+25δ`) ✓;
  Thm 10.5 = TW2 Thm 5.1 (`A₀L^{3/4}/2 + C_B L^{3/4}(log L)^C +
  11E_PΣρ_jS_j`) ✓; Setting = TW2 Setting 3.0 (`W₁ = L^{1/2}`, `w₂ = L^8`,
  `α = L^{−1/4}`, `log‖dP/dU‖ ≤ 4L^{1/2}`) ✓.
* Thm 10.6 = TW3 Thm 4.1, marked "Proof sketch"; the sketch matches TW3
  (2.1), Lemma 2.1, Lemmas 3.1–3.4 (`C₀ ≥ 6`, `Σ_a V² ≪ (log L)^6`) ✓.
* Thm 10.7 = TW2 Cor 5.2 + TW3 Cor 4.2 with all hypotheses (\ℛ(M), `M ≤ X`,
  `M ≤ P(M)^{1+B}`, ≤ 2 primes above `(log X)^8`, `λ ≤ A₀ log X`) ✓. The
  Scope paragraph and Remark 10.8 match TW2 "Bottom line" and TW3 E5
  ("bypassed, not proved") ✓.
* Hyp 11.1, Conj 11.2, Prop 11.3 (conditional on Conj 6.4 **and** K2, per
  TWrev T10), Conj 11.4 = ET §5.6 and TW Conj 6.4, Prop 6.5, Conj 6.8 ✓.

**Defects.**

* **D10 (MINOR, faithfulness: stale and overstated status of TW3 §6).**
  The "Three or more large primes" paragraph of §11 was written against
  the pre-round-2 TW3. It says the TW3 §6 results are "not yet
  hostile-reviewed" and that TW3 gives, for ternary moduli, "a proof of all
  star sums except one residual, vertex stars whose two partner primes are
  balanced with each other and whose divisor triples are balanced". The
  current TW3 (`main`, after review round 2) says:
  * Lemmas 6.1–6.2: PROVED, review R2 **SOUND**; Prop 6.3: PROVED as an
    implication, **SOUND after E10**. So "not yet hostile-reviewed" is now
    false.
  * Prop 6.4: **SKETCH**, "conditional on the unwritten any-arity fibre
    law" (`w₂ = L^{10}`, strengthened G_L/(H_δ)) — review **E11**. So "a
    proof of all star sums except one residual" overstates the source.
  * The residual is corrected (**E12**) to vertex stars with
    `ℓ_a ≤ ℓ_b < w₂q`, `q = 4·(two shorter of u,v,t)` (BFI range); the
    proved part is *every* triple with `ℓ_b ≥ w₂q`. "Two partner primes
    balanced with each other" is not the corrected condition.

  *Fix:* "Partial results [TW3 §6], hostile-reviewed [TW3rev, round 2]:
  any-arity noise stability with codegree terms and free codegree
  quarantine (Lemmas 6.1–6.2, proved); a reduction of the general case to
  arithmetic star sums (Prop 6.3, proved as an implication); for ternary
  moduli with B fixed, a *sketch* (Prop 6.4) of all star sums, conditional
  on an unwritten any-arity fibre-law step, except the residual
  `ℓ_a ≤ ℓ_b < w₂q`, which is open."
* **D11 (MINOR, body scope drops; companion of D1).** Two body summaries
  of Thm 10.7 drop its hypotheses: §9 item 4 ("Theorem 10.7 covers twin
  \ℛ(M)-moduli with at most two prime factors above (log X)^8") and §11
  opening ("(i) is closed for moduli with at most two prime factors above
  (log X)^8"). Both omit `M ≤ P(M)^{1+B}` (B fixed) and level
  `λ ≤ A₀ log X`; the §11 one also omits "\ℛ(M)". Since the Scope
  paragraph stresses that the B-restriction "is genuine", the summaries
  should carry it. *Fix:* add "with `M ≤ P(M)^{1+B}`, B fixed, at level
  O(log X)".
* **D12 (NIT, attribution of a new remark).** The sentence "the coarsening
  of Lemma 3.4 does not preserve the square form g², so the reduction …
  is not available here as stated" is correct (a coarsened g² is a
  majorant but not a square, and truncating the signed g destroys `g ≥ 1`
  on 𝒜), but it is not in TW2/TW3; only a `%` comment, invisible in the
  PDF, says it is the author's. Put "(observation of this note)" in the
  text, since every other claim carries a source.

## 5. Citations

**Checked and accurate.**
* Elsholtz–Tao Prop 1.4: verbatim against `sources/elsholtz-tao-1107.1010.pdf`
  (arXiv v6, text l. 318–321). The `k ≪ (AB)^{O(1)}` range as used in
  Lemma 5.3 was checked in ETrev item 4.1.
* Pomerance–Weingartner: title and arXiv number match
  `sources/pomerance-weingartner-2511.16817/abstract.xml`.
* Shiu: J. reine angew. Math. 313 (1980), 161–170; `sources/shiu-1980.pdf`
  is a 10-page scan (= pp. 161–170). The form quoted is TQ §3's, with
  `q ≥ 2` (Lemma 5.1's separate `d = 1` treatment is therefore needed and
  present).
* LL Lemma 2.1 (identity), LL Lemma 3.1 (lattice lower bound =
  TQ eq. (latlower)); notes Lemma 18.1 and Thm 3.1(B); TQ Lemma 2.2,
  Cor 4.3, Thm 8.2, §§2, 3, 10 — numbering confirmed from the TQ source.
* Every internal item number cited from ET, ETrev, EB, TW, TWrev, TW2,
  TW2rev, TW3, TW3rev was looked up and points to the stated content.
* MacWilliams–Sloane Ch. 10 Lemma 7 (binomial entropy bound) and
  Davenport Ch. 28 (Bombieri's theorem) are standard and correctly
  located; Montgomery, Bull. AMS 84 (1978) is the right survey.

**Defects.**
* **D3** (above): Vaughan/Montgomery attribution.
* **D13 (MINOR, stale locations).** [TW3] is cited as
  `EXCEPTIONAL_TWIN3.md` on "branch side-agent/twin-equidist", and
  [TW3rev] on "branch side-agent/review-twin3". The branch
  `side-agent/twin-equidist` no longer exists; both files are on `main`
  (merges 6ce44e1, f7c6ff3), and the review now has two rounds (the
  second is the one behind D10). *Fix:* cite `EXCEPTIONAL_TWIN3.md` and
  `reviews/exceptional-twin3-review.md` (rounds 1–2), this repository.
* **D14 (NIT, attribution).** §7.3 calls the capped measure "a variant of
  the distortion method of BBMST". TW §2 (the source) attributes the
  method to Hough (Ann. Math. 181 (2015)) and BBMST. The author dropped
  Hough for lack of an archived copy (report, checkpoint 2), which is
  fine for pages but not for credit. *Fix:* "the distortion method of
  Hough, in the form of BBMST [BBMST]" (Hough cited without pages, or
  just named).

## 6. Summary and verdict

No mathematical error found. Every proof given in full was re-derived:
the forced-class lemmas, the Jacobi/Mordell lemma, Lemma 3.4
(coefficient budget ⇒ level) and Cor 3.5, Prop 4.4 / Thm 4.5,
Cor 6.2, the assembly of the Main Theorem 6.3, Lemmas 7.1–7.5, the
constants of Thm 7.6, Lemma 8.2, Thm 10.1 and Lemma 10.3. Every statement
was compared with its source. The only strengthenings are in summaries
(abstract, Results list, §9/§11 recaps) and in the stale TW3 §6 status.
The main theorems themselves carry their exact hypotheses.

| # | severity | where | issue |
|---|---|---|---|
| D1 | MINOR | abstract, Results item 2 | Λ² cap scope drops \ℛ(M), `M ≤ P(M)^{1+B}`, level; gapped scope drops B and the admissible set |
| D2 | MINOR | Cor 3.5 / Thm 6.3 proof | Cor 6.1/6.2 stated only for `λ ≤ A log N`; Cor 3.5 needs the λ-form (two one-line fixes given) |
| D3 | MINOR | §1 | Vaughan's method attributed via a 1978 survey; route through PW §4 |
| D4 | MINOR | Cor 6.1, 6.2 headers | `proved` but they include Case A (mod Elsholtz–Tao Prop 1.4) |
| D5 | MINOR | Results item 1 | `O(log²λ)` stated without Remark 4.6's conditions |
| D6 | NIT | Rem 4.8 | remove `% TODO`; ETrev item 3.4 confirms `p ≤ 1/2` |
| D7 | NIT | §7.1 | η₀ undefined |
| D8 | NIT | §8.2 | "bound cannot exceed exp{…}": phrase in terms of saving |
| D9 | NIT | Lemma 8.1 | "equals 1 on 𝒜" is not stated by TQ; cite ETrev item 3.1 |
| D10 | MINOR | §11, ≥3 primes | TW3 §6 status stale and overstated (now reviewed; Prop 6.4 SKETCH; residual corrected, E11/E12) |
| D11 | MINOR | §9 item 4, §11 opening | Thm 10.7 summaries drop B and level |
| D12 | NIT | after Thm 10.7 | own observation marked only in a `%` comment |
| D13 | MINOR | bibliography | TW3/TW3rev branch locations stale; now on `main` |
| D14 | NIT | §7.3 | distortion method credit (Hough) |

Report points: (1) confirmed, see D6; (2) the routing of growing
selectors via Cor 6.1 is stated after Thm 6.3 and is correct; (3) the
η-dependence remark is correct; (4) sketches are marked (Lemma 9.1,
Thm 10.6) or presented as cited descriptions (Thm 7.7, 10.4, 10.5);
(5) bibliography checked, see §5; (6) confirmed for the theorem
statements, with the exceptions D1, D4, D10, D11.

**Verdict: MINOR REVISION.** D1, D4, D10, D11 and D13 must be fixed
before circulation: each is a status or scope statement that is stronger
than, or no longer matches, its source. The rest are presentation fixes.
No re-review of the mathematics is needed after the fixes; a diff check
suffices.
