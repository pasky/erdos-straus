# Agent report O58 — CAMPAIGN_SUMMARY.md refreshed to (D)26 / (H)27

Branch `side-agent/summary-refresh`. Only `CAMPAIGN_SUMMARY.md` changed (plus this report).
No new mathematics; labels copied from `DISCOVERIES.md`.

Changes, one commit per section:
* Title: "refreshed to main after ledger (D)26 and (H)27".
* §1: 3/4 sharp with no loglog loss; remaining exceptional doors (TC^alt, H_LS∞,
  weak SPW, non-CRT); pointwise rate `exp(c(log p)^{1/4}…)`, Haar exponent 3, 1/4 ceiling,
  window parity.
* §2.2: KARY3 (D)24 (sharp `(log N)^{3/4}` cap, local moment via Shiu; §§6–7 parent-checked only).
* §2.3: LARGESIEVE2 (D)25 incl. band-family escape; INTERFREQ2 + SPW refutation (D)26;
  TUPLES2 (D)23 (forced zeros, TC^alt); PRIMELAW without the log factor.
* §2.4: open doors rewritten.
* §3.3: table rows OMEGA8–OMEGA13; method story (BRW sandwich → Gallagher transfer → C-1 →
  graded quarantine → modulus-weighted moments → β-LLL + Jacobi square classes); TRANSFER;
  Haar exponent 3 (HAAR + OMEGA13 Thm 3.4); OMEGA14 ceiling and what 1/3 needs; Type-I map
  (TYPEI); superseded routes (OMEGA2 Haar bound, HC*/HC_Π, OMEGA7 archived).
* §3.4: XWIN (half-set lemma, stacking, exact orders) and WINDOW2 (Thm P1, model fake), window note.
* §4: rows E15–E20, P27–P38; loglog factors in E10/E12/E13 marked as dropped.
* §5: novelty of the sub-exponential machinery: sandwich/switching known; C-1 vs Lecomte–Tan;
  Janson-type one-hot inequality; β-weighted LLL = asymmetric LLL (no claim); planting lemma =
  LP duality of lower-bound sieves (no claim); (D)23–26 and XWIN/WINDOW2/TYPEI not audited.
* §6: re-ranked (refereeing; θ>3/4 doors; pointwise 1/3; E1/E2; a_min ≥ 11; Type-I; …).
* §7: reading guide with the new files and the four new/updated papers.

Points for the parent to check:
* `paper/README.md` still says "es-subexp-note v4 not yet refereed", while STATUS.md and the
  merge log cite R56 (`reviews/es-subexp-note-review-v4.md`, minor revision). The summary follows
  STATUS (refereed internally four times).
* §6 item 5 mentions POINTWISE_WINDOW3 as "was in progress" (ledger wording); no such file is on main.
