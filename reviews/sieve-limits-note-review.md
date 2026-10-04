# Hostile referee report: `paper/sieve-limits-note.tex`

Subject: `paper/sieve-limits-note.tex` at branch `side-agent/sieve-limits-paper`
(checked out into this worktree together with `reviews/agent-reports/AGENT_REPORT_O8.md`).
Sources: `EXCEPTIONAL_THETA.md` [ET], `EXCEPTIONAL_BALANCED.md` [EB],
`EXCEPTIONAL_TWIN.md` [TW], `EXCEPTIONAL_TWIN2.md` [TW2],
`EXCEPTIONAL_TWIN3.md` on `side-agent/twin-equidist` [TW3], their reviews, and
`paper/es-threequarter-note.tex` [TQ].

Verdict: *(pending — filled in at the end)*

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
