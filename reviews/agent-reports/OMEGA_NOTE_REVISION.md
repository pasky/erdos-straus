# Revision of `paper/es-omega-note.tex` against the referee report (R1–R17)

## Scope

* **Referee report.** `side-agent/review-omega:reviews/es-omega-note-review.md`
  (MINOR REVISION).
* **Base.** `side-agent/pointwise-omega`, merged at `fc4da33`. That commit is a WIP left by an
  interrupted session and already carried part of the repairs.
* **This revision.** Commit `980a06c` finishes the repairs.
* **Faithfulness check.** Every change was checked against `POINTWISE_OMEGA.md` (§§4–6, 9;
  Prop 6.3; Thm 9.4; the D8 scope note in §2) and against POINTWISE_SIZE §11.1. No statement was
  strengthened, and all status labels stay in the theorem and remark headers.
* **Build.** `pdflatex` ×3 is clean: 0 errors, 0 warnings, 0 over- or underfull boxes, no
  undefined references. The PDF has 13 pages, and the string "TODO" does not occur in it.

### Build fixes

The base version, as committed, was not quite clean. It had two problems that the referee's
log check missed:

* a pdfTeX "font expansion" warning;
* an underfull `\vbox` after the edits.

Fixes:

* **The warning.** It is a pdfTeX/microtype interaction, triggered by math superscripts in the
  bibliography (I bisected it to the McCurley, Obláth and Salez items). The fix selects the
  footnotesize superscript text font once, invisibly, after `\maketitle`. A `%` comment explains
  why.
* **The box.** Fixed with `\raggedbottom`.

## Item-by-item

| Item | Status | What was done |
|---|---|---|
| **R1** (necessity claimed) | Abstract: done in the WIP. §1: FIXED. | The abstract reads "isolate a purely combinatorial hypothesis that suffices". The §1 sentence now reads "Beyond it, this route needs a pointwise minorant that handles atoms with several large prime factors (a 'hypergraph' minorant); Thm 7.5 shows that such a minorant suffices." The "need" is only the content of Prop 7.3 (ceiling), namely that a design above exponent 2 is not prime-local. Nothing is claimed to be necessary in general. |
| **R2** ("by this route" dropped) | Remark: in the WIP. FIXED here. | The WIP added Remark 7.2 ("The previous record; proved modulo Chang Cor. 11"), with the 3-line computation `log L*(T)=(2/3+o(1))T`. **This revision:** (a) Chang's actual hypothesis is now stated (`log ℓ=o(log q)` for `ℓ|q`, checked in the archived Cor. 11), replacing "T-smooth"; (b) hardness (`840|L*`) and infinitude (`p>L*>T`) are added; (c) the last paragraph is reworded. The WIP's "(so that `log p≪log Q`)" read as a lower bound. It now says that a least-prime theorem certifies `log p` only through an upper bound `O(log Q)`, so it certifies at most `W(p)≫log p`, and "with Chang's exponent, no more than 5/8 by this route" (POINTWISE_SIZE §11.1 wording). The paragraph keeps "a class c≠1 may contain primes below Q". |
| **R3** (unlabelled Bonferroni claim) | Prop: in the WIP. FIXED here. | The WIP promoted the claim to **Proposition 7.6 [Proved]**, with the full proof of POINTWISE_OMEGA Prop 6.3. I re-checked the threshold `(2√2θ/log4)²≈4.16θ²≤4.2θ²`, `4y²≤T`, `N≥r²≥2J−1` and the measure `(2y)^{−2r}`. **This revision:** the lead-in "the obvious minorant fails" is made precise ("plain event-level Bonferroni truncation over the raw atom list fails"), and Prop 7.6 is added to the Summary of status. The follow-up "hub-adapted minorant appears necessary" is explicitly marked "this is not proved". |
| **R4** (hidden ET dependency) | Remark: in the WIP. FIXED here. | The WIP turned the sentence into **Remark 9.3 [Conditional; the implication is proved modulo ET Prop. 1.4]**, with the exact relative hypothesis `w_ℓ(T,z)≤log z/(8 log T)` and `z=(log T)^C`. **This revision:** (a) adds "for all large T", as in the source's second bullet; (b) adds the proof sketch from Thm 9.4: `x_E=2/φ(r_E)≤1/2`, at most `log T/log z` primes per event, `∏(1−x_{E'})≥exp(−4Σw_ℓ)≥e^{−1/2}`, `P≥exp(−4S_tot)`, quarantine cost `π(z)log T`; (c) states that without ET the argument gives only `exp(−T^{o(1)})`, via Lemma 9.2; (d) labels the remark and lists it in the Summary of status. |
| **R5** (10¹⁸ credit) | Already fixed in WIP | `\cite{MD}` (Mihnea–Dumitru, arXiv:2509.00128) for 10¹⁸, Salez for 10¹⁷, PW §6 as "see". The arXiv number and title were checked against the archived PDF `sources/lit2026/arxiv-2509.00128.pdf`. |
| **R6** (Mordell reference) | Already fixed in WIP; page range declined | The entry is now "Pure and Applied Mathematics 30, Academic Press, 1969", and Obláth (Mathesis 59 (1950), 308–316) is added and cited. **Declined:** the page range. The book is not archived, and ET ref. [44] gives none, so we do not invent one. |
| **R7** (Thm 5.1 proof gaps) | Partly in WIP; FIXED | Each point is now explicit: **(a)** `λ_*>0` via `log β*≥1−1/β*>2(β*−1)>(β*−1)log x` with `log x≥12 log Z>2` and `β*>1/2`; the claim "λ is common to all i by Lemma 4.2's second claim" was already in the WIP. **(b)** `q*_Q\|Q` because q* divides some `Qd_j` with `gcd(d_j,Q)=1`, so `q*\|q_i⟺q*'\|d_i`; `χ_1=χ*` on units (Lemma 4.2), and `χ*(a_i)=χ*_Q(1)χ*'(b_i)=ψ(b_i)` since `a_i≡1 (q*_Q)` and `a_i≡b_i (q*')`; ψ is real primitive (a coprime-conductor factor of a real primitive character) with conductor `>1`, coprime to Q and dividing some `d_i`, so the twist condition applies; the no-severe-pair case is covered explicitly. **(c)** `φ(Qd_i)=φ(Q)φ(d_i)` by `gcd(Q,d_i)=1`; `E_1` is now defined before the display that uses it. **(d)** `C_1≥12`, using `K≥1` (as `M_1≥μ`), gives `x≥Z^{12}`. **(e, extra)** One line shows why `E_1,E_2≤μ/(8(C_0+1)M_1)=e^{1−K}/(8(C_0+1))` holds for large `C_1`: the three exponents are `≥C_1K`, `≥C_1^{1/2}K` and `≥C_1K/52`. |
| **R8** (twist constant) | Constant in WIP; FIXED here | The WIP restored `e^{−15S−6}`. **This revision** writes out the two-case bound, so the constant can be checked line by line: `\|μ_ψ\|≤15^{−r}V+16^{−r}S^{J−r}/(J−r)!`. For `r≤J/2` the second term is `≤(e/11)^{J/2}≤e^{−0.69J}≤e^{−15S−6}`. For `r>J/2` it is `≤16^{−J/2}e^S≤e^{−1.38(22S+10)+S}≤e^{−15S−6}`. The two cases combine to `≤(1/15+e^{−6})V≤0.07V≤μ/4`. (The source's "`≤e^{−29S}`" in the second case is loose, and is not used.) |
| **R9** (numerics scope) | Partly in WIP; FIXED | Remark 3.4 now says explicitly that `y=√T` does **not** instantiate Thm 1.1: there `max g≈0.08–0.33>1/16`, and the twist condition can fail (numerically it does at `T=10^4`, per the D8 note). With the theorem's `y`, `y<T` (so `𝒰≠∅`) only when `log T>e^6≈403`. |
| **R10** | Already fixed in WIP | Lemma 4.2's third claim now reads "If `q∈𝒬` and no severe pair has `q*\|q`". |
| **R11** | Already fixed in WIP | The proof of Thm 8.6 notes the preprint numbering of LW Prop. 5.1 and the translation `χ_p(q)=(q/p)` by reciprocity for `p≡1 (4)`, including `q=2`. |
| **R12** | WIP; extended | Cor 8.5: L is divisible by the modulus of the given class (hence by 24). **This revision** completes the deduction: the class `p mod L` lies in the given class; Prop 8.4 gives `(p/ℓ)=1`, hence `(ℓ/p)=1` by reciprocity; `(2/p)=(3/p)=1` because `p≡1 (24)`; so `n_p>T`. Thm 1.2(a) now says "supported, among large primes, on …". |
| **R13** | Already fixed in WIP | "Contradict the random model" now reads "exceed the random-model prediction `max n_p≍log x log log x`", and the unsourced "numerically … small power of log T" sentence is dropped. |
| **R14** (iff) | WIP; rewritten | Both directions now rest on one displayed identity, `(ha−p)(hb−p)−N=h(k(4abc−1)−p(a+b))`. This identity is also the one-line check of `k(4abc−1)=p(a+b)` the referee asked for. Also shown: `f≡−p (h)` via `gcd(p,h)=1`; positivity of e and f from `pa,pb<4abck`. The identity was verified by hand. |
| **R15** | Already fixed in WIP | "(as `y³>T`)" is added. μ′ is a product measure (Haar conditioned on a product set), and the dependency graph is explicit. `Σ_{E'∼E}x_{E'}≤2(w'_{ℓ_1}+w'_{ℓ_2})=T^{−3ε+o(1)}` gives `∏(1−x_{E'})≥1/2`. |
| **R16** | Already fixed in WIP | The intro says 5/8 needs the modulus `lcm(24, M≤T, M≡3 (4))`. |
| **R17** | FIXED (as instructed) | The author stays "Anonymous". The only marker is the pure comment `% TODO(submission): replace "Anonymous" by the author metadata …`, which does not appear in the PDF (`pdftotext \| grep -i todo` is empty). |

## Not changed

* No theorem statement was altered except by the referee's requested weakenings/precisions (R1, R2,
  R10, R12).
* No new mathematical claims were made. Prop 7.6 and Remark 9.3 transcribe POINTWISE_OMEGA
  Prop 6.3 and Thm 9.4, with their source labels.

## Numbering

New labelled items now shift the numbering in §7. Current numbering:

| Item | Number |
|---|---|
| Prop (complete certificates) | 7.1 |
| Remark (5/8 record) | 7.2 |
| Prop (ceiling) | 7.3 |
| Hyp H_min | 7.4 |
| Thm (H_min ⇒ 1/θ) | 7.5 |
| Prop (Bonferroni failure) | 7.6 |

The referee's "Thm 7.4" is the current Thm 7.5.
