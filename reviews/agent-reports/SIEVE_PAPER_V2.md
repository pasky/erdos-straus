# SIEVE_PAPER_V2 — changelog for paper/sieve-limits-note.tex (task O15)

Status: in progress.

## Sources read
* EXCEPTIONAL_KARY.md (Thm 2.5, Cor 2.6, Thm 4.1, Lemma 4.2', Thm 4.5) + reviews -review.md, -review-2.md
* EXCEPTIONAL_TWIN4.md (Lemma 2.3 large sieve, Thm 7.1, Prop 9.1, Cor 9.3, Thm 10.4; §9.3/§12 OPEN; §11 SKETCH) + review
* EXCEPTIONAL_NONCRT.md + review (pending)

## Scope notes (do not overclaim)
* KARY Thm 4.5: general majorants, R(M)-classes only, B fixed, plus W-smooth classes; level λ ≥ λ0(B).
  Not covered: log M/log P(M) unbounded; (a,D)/Case-A mixed in.
* TWIN4 §11 (B removal for general majorants) is SKETCH only — not to be claimed.
* TWIN4 Thm 10.4: Λ² only, fixed r, no B.

## Plan (v2 structure)
§1 intro/abstract rewritten around KARY Thm 4.5; §§2–5 unchanged (forced classes, architecture,
sieve-limit theorem, profiles); §6 dominant-prime families (old cap section, minus main thm);
§7 QR base + capped sequential measure (old gapped section; gapped/resolved theorems kept as
special cases); §8 NEW weighted k-ary comparison (KARY §§1–3: Lagrange extrapolation,
supermartingale); §9 NEW main theorem (KARY Thm 4.1, Lemmas 4.2/4.2'/4.3, Thm 4.5, architecture
theorem); §10 campaign; §11 Λ² (+TWIN4: large-sieve rough-partner BT, Thm 7.1, Prop 9.1,
Cor 9.3, Thm 10.4); §12 NEW non-CRT (NONCRT); §13 exclusions; §14 open.
Notation changes vs KARY: product law ϖ (ν is the majorant), replaced set J(ω), light mass m(ω),
coin count z.

## Progress
* [x] §8 k-ary comparison (new), §9 main theorem (new; Thm main moved here, case (ii) now KARY Thm 4.5)
* [x] gapped section reframed (tools + special cases)
* [x] Λ² section: TWIN4 (Lemma rough-partner BT via large sieve, Thm r-prime, Prop 9.1, Cor 9.3, Thm 10.4); Remark: Λ² caps under B superseded by Thm 4.5
* [x] §12 non-CRT (new)
* [ ] exclusions, open problems, intro/abstract, campaign cross-refs
