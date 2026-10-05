# AGENT_REPORT_O56 — es-subexp-note v4 (checkpoint 1: full draft, compiles)

Branch `side-agent/subexp-paper-v4`. File: `paper/es-subexp-note.tex` / `.pdf` (39 pp., v3 had
27). `pdflatex` twice: 0 undefined references, 4 overfull boxes < 11pt.
Not merged into main.

## Headline results of v4
* **Thm 1.1 (main):** `W(p) ≥ exp(c(log p)^{1/4}(log log p)^{−1/4})` i.o. over hard primes;
  `log p ≤ C𝓛^4 log𝓛` for some hard `p>T` with `W(p)>T`. Proved modulo Gallagher (Thm 5.2,
  with Landau–Page Thm 5.1) and **Nair–Tenenbaum** (Thm 3.1). Elsholtz–Tao is no longer used.
  Source: POINTWISE_OMEGA13 Thm 5.1 ((H)26).
* **Thm 1.2 (Haar exponent 3):** `c𝓛³/log𝓛 ≤ log(1/δ*(T)) ≤ C𝓛³(log𝓛)^5`. Upper: Thm 3.3
  (mod NT; OMEGA13 Thm 3.4). Lower: Thm 4.4 (mod fundamental lemma; POINTWISE_HAAR Thm 2.1),
  now **proved in the paper** (v3 only cited it as internal work).
* **Thm 1.3 = Thm 10.6 (ceiling):** every fibre with `log Q ≤ T^{0.05}`: no minorant of
  `1[W>T]` of level `log D ≤ c𝓛^4/log𝓛` has positive Haar mean (mod Gallagher, effective Page,
  fundamental lemma; OMEGA14 Thm 4.5). Cor 10.7 (OMEGA14 Cor 4.6, proved implication with
  explicit scope): 1/4 is the ceiling of minorant + transfer arguments, up to `(loglog p)^{1/2}`.
  Cor 10.8 (new packaging of OMEGA14 Cor 3.1, now derived from Thm 10.6 instead of the dense
  Thm 2.4): the energy tail of Thm 7.9 cannot be improved beyond `(log𝓛)²` for this purpose.
* **Remark 10.9 (Assessment):** heuristic 1/3 and what input it would need (prime input that
  is not a bounded-level minorant: Type II / parity-sensitive information for a sieve of
  dimension ≍𝓛³ below its sieving limit).

## v4 change list (for the referee)
Section numbers refer to v4.
1. **Title/abstract/§1** rewritten: exponent 1/4; three headline theorems; "Versions" paragraph
   (v1 1/14, v2 1/7, v3 1/5, v4 1/4); method sketch for the square-class quarantine and the
   ceiling; literature paragraph "The local lemmas" (β-LLL, Janson-type, planting; BGP/PYY/Tao
   cited, no novelty claimed for planting); status conventions now list NT and the fundamental
   lemma as cited inputs and add the label "Proved implication".
2. **v3 Thm 1.2 (unconditional `loglog·logloglog`) dropped**: Thm 1.1 now needs only
   Gallagher + the published NT theorem. Stated in "Versions".
3. **§2 (new; replaces v3 §2 graded quarantine):** Lemma 2.1 atoms (unchanged); **Lemma 2.2
   Jacobi lemma** (OMEGA13 L3.1, with proof; computer check to 2·10⁵ mentioned as unused
   evidence); Lemma 2.3 class of one (now a corollary of 2.2); **Def. 2.4 square-class
   quarantine** `(Q,r)`, survival `−4D≡r (gcd(M,Q))`, `M∤Q`; Lemma 2.5 reduction (i), weights
   (ii), hardness of `p≡r (Q)` when `105|Q` (iii); **Remark 2.6** explains why the graded
   class-of-one quarantine is superseded (g-inflation, ET, log-weighted threshold) and omitted;
   Lemma 2.7 classical LLL (moved from v3 §7, now with the general conditional bound for
   subfamilies); **Lemma 2.8 β-weighted LLL** (OMEGA13 L1.1); the **square-class process**
   (with the forced steps at 3,5,7); **Lemma 2.9 bookkeeping** (OMEGA13 L3.2 (a)–(d),
   supermartingales, optional stopping, pair potential Π for late primes).
4. **§3 (new; replaces v3 §3 ET moment):** Thm 3.1 NT (cited; statement transcribed from
   Henriot (1.1), checked against `sources/henriot-1102.1643.pdf`; specialised to
   `Q_1=n, Q_2=4n−1`, `α=δ=1/2`, `ε=1/200`); **Lemma 3.2 Haar masses** (OMEGA13 L3.3: (A) mod NT
   incl. the R48b-D1 repair `log M_Y ≤ log Y·τ(M_Y)`, (B) elementary second moment, `Ξ≪𝓛^{C_0}`
   uniform in Y); definition of δ*(T) (HAAR normalisation, factor 2 remark); **Thm 3.3 Haar
   upper bound** (good realisation via three bad events of probability ≤1/4 each).
5. **§4 (new):** Lemma 4.1 compatible events, Lemma 4.2 lopsided LLL, **Thm 4.3 Janson-type
   inequality**, Thm 4.4 Haar lower bound with Lemmas 4.5–4.7 (mass, LLL hypothesis, pair sum)
   — POINTWISE_HAAR §§1–2 transcribed (Prop 1.5 packing barrier and §3 Monte Carlo omitted;
   the MC fit is mentioned as unused evidence).
6. **§5 Gallagher:** unchanged, plus one sentence on the range condition for Lemma 10.4.
7. **§6 linear transfer:** generalised to a coset `rH`, r≡1 (8) and a QR mod every odd prime
   of Q; consistency `b_i≡r (gcd(d_i,Q))`; in (c) `ψ_1(n)=ψ_1(r)=1` on H (OMEGA13 I3).
   Conclusion `p≡r (Q)`. Case A/B otherwise verbatim.
8. **§7 energy bound:** unchanged.
9. **§8 sandwich:** setting is now `(Q,r)` of Thm 3.3 with eq. (4) `w̃_ℓ≤η`; label `eq:lllhyp`
   now records `η≤0.19` (T≥e^{33}); digits below `a_ℓ` are those of r; cells consistent with
   r; Lemma 8.1 Haar means with the auxiliary class `r'≡r (Q)`, `r'≡1 (ℓ')`; v3's Cor. `cor:lll`
   (`x_E=2P(E)`, 1/64 thresholds) removed; **twist Lemma** re-proved with Lemma 2.8's
   conditional bound: `|E[Fψ]|≤β^{-1}w̃_{ℓ0}EF'≤ηEF'`, total `≤(0.01+η/(1−η))δ≤0.245δ<μ/4`
   (OMEGA13 I1(b)).
10. **§9 assembly:** `S_1=C𝓛³log𝓛`, `τ=2𝓛⌈log₂(100T⁴(S_1+1)e^{3S_1})⌉` (uses
    `δ≥e^{−4S_β/3}≥e^{−3S_1}`); auxiliary prime with `r'≡1 (ℓ_aux)` (R48c m1/R48d D1) so
    `p>T`; hardness from Lemma 2.5(iii). Proof of Thm 1.1: `log Z ≪ 𝓛³(log𝓛)^5+𝓛^4log𝓛`.
    v3's Cor. `cor:haar` (Haar side) and Remark `rem:haarlower` (cited lower bound) are replaced by Thms 3.3/4.4.
    Remark 9.2 (exponent) rewritten: junta `𝓛S` is the bottleneck, see §10.
11. **§10 (new) ceiling:** Lemma 10.1 planting (OMEGA14 L1.1, proof with the index range
    `j+a−1≤2k+1` made explicit), Lemma 10.2 level barrier in the deterministic form (OMEGA14
    Thm 1.3 + L4.1 merged; finite spaces, so no measurability remarks needed), uniqueness
    family with `ε≤1/20` (so that `p*≤T^{−1/2}` follows directly from the unique-v count),
    Lemmas 10.3–10.5 (OMEGA14 L4.2–4.4), Thm 10.6 (OMEGA14 Thm 4.5), Cor 10.7 (Cor 4.6) with
    scope paragraph, Cor 10.8 (energy tail optimality), Remark 10.9 (heuristic 1/3).
    OMEGA14 §2 (dense-minorant Thm 2.4, BV-based Lemma 2.2, m-copy Lemma 2.3, Prop 2.7) is
    **not** included: Thm 4.5 supersedes it for the paper's purposes.
12. **§11 status** rewritten. **Bibliography:** added NT (checked on archived PDF), Henriot
    (arXiv archived; journal data from memory), Erdős–Spencer, Janson, Friedlander–Iwaniec,
    BGP, PYY, Tao 254A (memory; flagged in a `TODO(verify, v4)` comment); removed the internal
    [Haar] item. README entry updated.


## Deviations from sources / things the referee should check
* Lemma 2.9(d) proof: I wrote out the pair potential for events `F=E^{(ℓ)}` (non-atoms) and
  defined `p_i` via the fibre measure μ_i (0 for dead atoms), which makes "survival" automatic.
* Lemma 3.2(B): the bound for Ξ is stated with `2^{ω_Y}≤2^ω` and `f(p^k)≤C(k+1)^C`; I did not
  compute `C_0` explicitly (source: `81/2+8+o(1)` with a `(log Y)^{O(1)}` factor; uniform in Y is
  what matters, and Y is chosen after C_0).
* Lemma 10.4 (class-uniform primes): `Err_G` is "the right-hand side of Thm 5.2 times C_G";
  the two exceptional/non-exceptional forms are as in Thm 5.2 here (which is MV III's form).
* Cor 10.7's proof phrased as a statement about the certified relation between x and T.
* Not claimed: anything about ES; the 1/3 heuristic; arguments outside Cor 10.7's scope.

## Remaining / not done
* No independent re-derivation of NT constants or of OMEGA14 numerics (exact LP checks) — the
  paper cites none of them as inputs.
* Memory citations listed in the bibliography TODO comment need checking before submission.
