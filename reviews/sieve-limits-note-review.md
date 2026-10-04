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

