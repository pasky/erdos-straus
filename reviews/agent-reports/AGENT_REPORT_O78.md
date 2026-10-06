# Agent report O78 — summary refresh 2 (branch `side-agent/summary-refresh-2`)

Base: main at `7eeee90` (ledger through (D)28 follow-up 3 and (H)33). No new
mathematics; labels copied from `DISCOVERIES.md`.

## CAMPAIGN_SUMMARY.md (one commit per section)
* Title/§1: refreshed to (D)28/(H)33; audit 10b cited; exceptional line now
  mentions all-level large-sieve caps ((D)27, (D)28), (A)9 INTERNALLY PROVED,
  open doors TC^alt_θ, (A*)/(RD′), weak SPW (fixed-σ SPW and fixed-η RSPW
  refuted), non-CRT input; pointwise line: Haar exponent 3 with log-free lower
  bound, tail exponent 3 over primes ((H)33), 1/4 ceiling up to
  `(log log p)^{1/4}`, Wiener-norm barrier, LS ⇒ 1/3 (LS a CONJECTURE), SAP
  open, m/n.
* §2: (A)9 relabel; sieve-limits v5 (R65); new bullets for LS3 and LS4
  (+ LS5–LS7 follow-ups, (RD) false as stated, (RD′) target); SPW2 exact
  requirement; §2.4 open list rewritten.
* §3.3: m/n (MN/MN2); Haar `≫𝓛³` (CEILINGS_UNIFIED Prop 1.1); ceiling at
  `c𝓛⁴`; OMEGA15 barrier; CEILINGS_UNIFIED Thm 4.1/4.3 with exact scope;
  OMEGA16; OMEGA17/SAP; new "typical size" block ((A)9 + (H)33); TYPEI2;
  W>4095 data; write-ups (subexp v5; v6 noted as in preparation, O77, not
  merged). §3.4: WINDOW3 faithful model (EVIDENCE/Assessment).
* §4: rows E21–E25 (SPW2, LS3, LS4, LS5–7, cubic tail) and P39–P45 (OMEGA15,
  CEILINGS_UNIFIED, OMEGA16, OMEGA17, TAIL, MN/MN2, TYPEI2); P37 → v4–v5.
* §5: new audit-10b block (no-internet caveat, verdicts, recommended
  wording, list of files audited by neither pass); planting-lemma note.
* §6: re-ranked; θ>3/4 split into *opening* (TC^alt, weights < 1, non-CRT)
  vs *closing* ((A*)/(DCC)/(RD′), weak SPW) questions; 1/3 routes (LS, SAP,
  smaller gaps); WINDOW3 gap; TYPEI2; audit must-checks.
* §7: reading-guide rows for all new files and audit 10b.

## STATUS.md
* Header date/ledger range; "Open target" bullet; pointwise paragraph
  rewritten as five short bullets (it previously said "modulo Thorner–Zaman
  and Elsholtz–Tao", which was stale); "Exceptional-set exponent: where it
  stands" rewritten (proved caps / open, with closing vs opening); papers
  list (sieve-limits wording fix, subexp v6 note).

## Flags for the parent (not acted on)
1. POINTWISE_HAAR Conj 3.1 (`log(1/δ*) ≍ 𝓛³/log 𝓛`, ledger (H)25) seems
   inconsistent with CEILINGS_UNIFIED Prop 1.1 (`≫ 𝓛³`, (H)29) if the
   normalisations agree; likewise (H)25's Monte Carlo fit to `𝓛³/log 𝓛`.
   The ledger does not mark the conjecture refuted, so the summary only says
   "close the `(log 𝓛)^5` gap". Worth a one-line ledger note.
2. es-subexp v6 exists on branch `side-agent/subexp-paper-v6` (O77) but is
   not on main; both files call it "in preparation". Update after merge.
3. `verify.py` housekeeping lines in STATUS were not touched (no new blocks
   on main since (dn)–(ds) that I could see for LS7/MN2/TAIL).
