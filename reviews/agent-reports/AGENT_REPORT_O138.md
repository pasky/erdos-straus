# AGENT_REPORT O138 — barrier note: long-shot results added

Branch `side-agent/barrier-note-longshots`. File `paper/es-automorphic-barrier-note.tex` / `.pdf`, now **24 pp**
(was 18). It compiles cleanly, three passes: no errors, no overfull boxes, no undefined references. One cosmetic
`Underfull \vbox (badness 6396)` remains from page breaking, and the `pdfTeX font expansion` warning was already there.
**ES is not proved; the paper says so throughout.**

## What was added
New **§6 "Two non-counting escapes that fail"** sits between §5 (gaps) and the hatches. The old §§6–7 are now §§7–8.
* **§6.1 Covering in the e-slices** (source LONGSHOT_PIGEONHOLE.md, review R135):
  * Lemma 6.1 (e-slice), including the R135 D1 remark: V → solutions is onto, and injective once gcd(a,b) = 1.
  * Lemma 6.2 (genus inside a slice, ℓ = 2 included).
  * Lemma 6.3 (collisions give signed solutions).
  * Prop 6.4 (Kneser criterion). Its sharpness is stated only for criteria that depend on orders/counts (R135 D2).
  * One paragraph on regimes, forcing cost (LP Lemma 2.1) and the modulus ceiling (LP Lemma 2.3).
  * Def 6.5: TCC with index ≤ 2e^θ (R135 D3).
  * **Thm 6.6** (PROVED relative to PNT in APs, BT, Shiu, Nicolas–Robin). The proof sketch follows the source's
    steps (a)–(d), with the Shiu range e < X^{3/4} from R135 D4.
  * Remark 6.7: extension to all θ < 1, labelled as the reviewer's derivation (R135 D6).
  * A scope paragraph stating the coset-size restriction (R135 D5).
  * **Conjecture 6.8 PH** with its EVIDENCE: exceptions 3529 and 110881, and the "theorem is qualitative" caveat.
* **§6.2 Fibred encodings** (source LONGSHOT_FIBRED.md, review R136):
  * Setup and c(n) = Σ c_s.
  * Lemma 6.9 (rigidity) plus Borel density.
  * Thm 2.3 consequences, including the D2 hypothesis (φ_i maps into the ES variety) and the D3 caveat (only pieces
    as given).
  * Cor 6.10 (D4 generic-flatness version, sketch; attribution to ET Props 1.8–1.9 / Mordell–Schinzel).
  * Thm 6.11 (orbit weights, PROVED relative to (C)), with the D9 wording. The F4 example uses growth ≍ H (D10); Pell
    orbits are included.
  * The note says explicitly that **DRS/EM/EMS/BR/CTX statements were checked only second-hand**.
  * Prop 6.12, the odd-square test under (U), with the D12 third alternative (the place p alone).
  * Earnest spinor control.
  * Prop 6.13 (𝔊⁻_d), with the f-form [f,4ad,de] (D5), the 19/40 caveat (D6) and "invalid = per-level false,
    aggregate vacuous".
  * **Thm 6.14**: items 1, 2, 4 PROVED; **item 3 CONDITIONAL** (CTX hypotheses fail for the pair space, D14);
    normalisation by max w_θ (D13); item 4 uniformity.
  * An exact-scope paragraph covering (E-a)–(E-d). It says plainly: **"not a theorem about all large-fibre
    encodings"**, and the T8 blind spot is closed only for continuous fibres (D1).
* **Other updates:**
  * Abstract: two sentences.
  * Intro list: a new item.
  * After Prop 4.4 (scale constraint): one sentence pointing to §6.2.
  * Hatches: the intro mentions §6. The non-escapes remark says covering reduces to H-A/H-B and fibring leaves
    (E-a)–(E-d) open. H-A and H-B are unchanged.
  * Summary: one sentence.
  * Bibliography: [LP], [LF], [Kn], [TV], [MV], [Sh], [NR], [DRS], [EM], [EMS], [BR], [CTX], [Ea].
  * `paper/README.md`: an update line.

## Cuts made to fit 24 pp
To stay within the page budget, some material from the sources was shortened or left out:
* Dropped:
  * the random-residue heuristic (the brief's "log₃ q");
  * the Type I hyperboloid and quaternion examples;
  * the bilinear-sieve remark in the fibred scope.
* Shortened to one sentence each:
  * Lemma 2.1 (forcing cost) and Lemma 2.3 (modulus ceiling);
  * Cor 2.5 (growing families).
* Not included:
  * Table 3.1 / 3.2 numerics (only summarised);
  * the "Answer to the brief" text.

## Points for the referee
* The **bibliographic details** were not re-verified against the papers here:
  * DRS/EM/EMS/BR/CTX are flagged in the text as checked second-hand;
  * Kneser, Tao–Vu, Montgomery–Vaughan, Nicolas–Robin and Earnest are standard references (Earnest checked against
    `sources/r136`).
* **Thm 6.6 statement.** It uses "positive lower density" (of all primes). The source states the bound relative to
  π(x;q₀,1) and derives the density ≥ (1 − 2C·Y^{…})/φ(q₀).
* **Prop 6.4 sharpness.** The paper says the criterion "reads k ≥ m" in the ℤ/2m example. I checked that the
  conditions at the other subgroups H ∌ m are implied by it.
* **Thm 6.14 item 1** lists R = O(log n) for Pell orbits. Those orbits are not power-fibred (δ = 0). This follows the
  source.
