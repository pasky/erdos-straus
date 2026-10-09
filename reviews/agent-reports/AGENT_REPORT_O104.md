# AGENT_REPORT_O104 — density transition added to `paper/es-mn-short-note.tex`

Branch `side-agent/mn-note-transition`. Source: `EXCEPTIONAL_MN2.md` (DISCOVERIES (D)31 follow-up;
reviews `reviews/exceptional-mn2-review-A.md`, `-B.md`). No new mathematics; this is a write-up task.

## What changed (paper now 25 pp, was 19 pp as built in this worktree; R97 said 18)

* **§8 "The density transition"** (was: proof of Cor D + "The other side" + Assessment 8.1):
  * §8.1 notation (L, A, π*, ρ_exc, ρ_rep), Cor D proof unchanged, one paragraph on why it loses
    (log m)^{4/3} (integers → primes).
  * §8.2 **Theorem U** — full proofs: Lemma 8.1 (reduced CRT model = MN2 L1.1; uses Lemma 3.3(2),(3),
    Cor 5.2, [TQ] Lemma 8.1), Lemma 8.2 (multiplicities via Shiu = MN2 L1.2), Theorem 8.3 (= MN2 Thm 1.3,
    BV at level N^{0.45}, BT, PNT recentring, Cauchy–Schwarz), proof of Theorem U; remark that the
    Cor D rate ρ_exc ≪ 1/L is *not* improved (R102A/B repair kept).
  * §8.3 **Theorem L** — PW Cor 2.2/2.4 setup; Lemma 8.4 (two harmonic sums; (a) and (b) condensed but
    with every step named, (b) in the corrected Rankin+Shiu form), Prop 8.5 (Type II, full, ET §9
    three-way split), Lemma 8.6 (ET Prop 1.4 + Pólya–Vinogradov: **proof sketch with exact pointers**
    ET pp. 30–32, (7.11), Cor 7.4, Rem 1.5; includes the square-q slip remark), Prop 8.7 (Type I,
    condensed), Lemma 8.8 (very large m), proof of Theorem L incl. the consequence (I added the
    explicit check that the log m > L/10 range gives m^{10C/log L − 1} → 0).
  * §8.4 gap (m log m/φ(m))^{1/3} (derivation via log L ≤ ½ log m), PW comparison ((PWrange) and the
    PW quotes retained; improvement factor min(log m, L/log m)), Elsholtz 2001 Rem 7.3 (saving
    ≥ 1 only for log N ≫ m^{1/2}), Pomerance 2026 talk (new bib item [P]) per novelty audit 10c §1.
  * §8.5 numerics (EVIDENCE; 6-column even-m table taken verbatim from MN2 §2.1, L_.75−L_.25
    computed from MN2's quartiles; odd-m parity effect; overdispersion) and **Conjecture C2**
    (CONJECTURE, starred environment, statement verbatim from MN2).
  * Assessment 8.1 ("why the shapes") kept unchanged.
* **Abstract**: transition sentence replaced (U, L, gap, numerics, C2); status sentence now says the
  lower side is relative to ET, not [TQ].
* **Intro**: Cor D retitled "via integers"; Theorems U and L stated (starred environments with
  labels PROVED relative to …, effective/ineffective), discussion paragraph replaces the old PW one.
  Status/novelty: exception for Theorem L, MN2 reviews, Lemma 8.6 not machine-checked; what-we-add
  sentence. Organisation updated.
* **Literature** closing paragraph and **open problems** (gap problem rewritten with MN2 §4 (i)–(iii);
  new Problem "the profile" = C2 + parity effect).
* Bib: [MN2], [P] (Pomerance talk) added.
* `reviews/es-mn-short-note-referee.md`: "Post-referee addition (O104)" section; `paper/README.md` updated.

Compiled twice: no undefined references, no overfull boxes (6 pre-existing hyperref
"Token not allowed" warnings from math in section titles; not new in kind).

## Points for the referee

1. Lemma 8.6 is a sketch relative to ET's proof; MN2 itself only has it checked against ET by R102B.
2. Lemmas 8.4 and Prop 8.7 are condensed from MN2 §3 (some constants/ranges abbreviated, e.g. the
   small-box count in 8.7); check that nothing load-bearing was dropped.
3. Labels: U = "proved relative to [TQ], with Bombieri–Vinogradov and Shiu" (MN2: rel. MN Cor 3.2, BV, BT,
   PNT, Shiu); L = "proved relative to ET Thm 7.1 and the proof of ET Prop 1.4, with Brun–Titchmarsh and
   Shiu" (+ Pólya–Vinogradov, classical). Abstract lower-side wording is "proportion → 1 when
   log N/(φ(m)/log m)^{1/3} → 0" (I avoided an unquantified "ε").
4. The PW improvement claim "factor min(log m, L/log m)" compares with PW's *unsimplified* Type I count.

STOP — waiting for the parent / referee.
