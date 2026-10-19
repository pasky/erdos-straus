# AGENT REPORT O279 — consolidation C3: FRONTIER.md for a fresh expert

Branch `side-agent/frontier-doc`. Deliverable: `FRONTIER.md` (≈ 10 000 words, ≈ 11–12 rendered pages; self-contained).
**ES is not solved; the document says so up front and claims nothing new.**

## What was done
* Sources read: STATUS.md (all wave headlines), DISCOVERIES.md (J)57–(J)108 (two research subagents extracted the entries
  verbatim with line numbers), the barrier files (CONDITIONAL_ES, PARITY_AUDIT, CLASS_FORCING, TWO_POWER_LADDER,
  B2_ACROSS_FIELDS, BM_CORRECTED_COUNT, SINGLE_P_COUNT, METAPLECTIC_ES, SYNTHESIS_SPARKS9, LOWER_TAIL_ASTRA/FABLE,
  DISPROOF_AVENUES, AMPLIFY_EXCEPTION), both board memos, BOARD2_SLATE, paper/README, LITERATURE_2026, ASTRA_BRIDGE, plus
  POINTWISE_SIZE, redteam-automorphic §4 and the brainstorm brief (for the canonical B1–B6 wording). The central objects
  (BM_CORRECTED_COUNT §§1–3, PARITY_AUDIT §2–3, METAPLECTIC Thm K, POINTWISE_SIZE §0) I read myself.
* Structure as briefed: §1 landscape; §2 the (★) count, its exact forms, M_BM ≫ log²p, Theorem K, H⁻_BM; §3 barrier map
  (B1–B6/T1, finite search, tied modulus, reciprocity-parity + Stickelberger m = 2, privacy, positivity, numerator blindness,
  no-BM/disproof shape, flat power ladder, M1a–M5 pattern, Dickson-conditional root/window failures) each with statement /
  scope / rules out / does NOT rule out / pointer; §4 a 16-item screening checklist + profile; §5 partial and conditional
  results by label; §6 ≈ 35 dead ends with one-line reasons; §7 15 open sub-problems with "why"; §8 pointers.
* Self-review: one deep hostile fidelity review (`review` tool, reviewer sampled > 40 statements). It found 24 defects, no
  claim that ES or a case of it is proved; all 24 repaired (commits "review repairs §1–§7"). The substantive ones:
  (1) my §7 item "|comp(1)| ≫ log²p unconditionally" (Fable's spark) is **false under Dickson** (LOWER_TAIL_ASTRA Thm 3.1:
  comp(1) has 8 vertices i.o.; Fable itself retracted the growth claim) — rewritten as a warning plus the open growing-root
  question; (2) SIBLING certification was level-1 survival, not Conj 4.2; (3) power ladder: the rungs coincide as
  predicates on n (all true for every n ≥ 2 by scaling), the "one bit" is mechanism, the index {1,2} is by choice of prime;
  (4) Theorem K: only the odd-character component is the theta quotient; (5) "no signed → positive move" and "ℤ[√p]
  windows never forced" restored to their hypotheses; (6) the checklist is now explicitly a screen for the mapped classes
  of arguments, not a set of necessary conditions for every proof; (7) labels restored (45/(8π²) is Assessment, Burgess
  bound PROVED; Zaremba is *claimed*; adversarial primes are BPSW-probable; PH evidence is sampled).

## Things the parent should know
* `BOARD2_SLATE.md` supersedes the lower-tail board memo's five-slice constants (memo: 9/(16π²), 33/(8π²); slate: principal
  45/(8π²), Burgess 45/(32π²)); FRONTIER cites the slate and says so.
* Unreconciled in the repo (flagged in FRONTIER §2.2 and §7 item 16, not resolved): the (★) main-term constants
  (log p)²/8 (PARITY_AUDIT Lemma 2.1, trial expansion) vs 3/(2π²)(log p)² ≈ 0.152 (log p)² (BM_CORRECTED_COUNT Thm 2.2,
  prime-averaged pair series). My reading (Assessment, not checked): different expansions/averages; nothing in FRONTIER
  depends on which constant is right, but a fresh reader will notice.
* STATUS's "PH: EVIDENCE to 3.7·10⁷" is stronger than LONGSHOT_PIGEONHOLE Conj 5.1's own wording (sampled primes;
  exceptions 3529, 110881 below 10⁶); FRONTIER follows the source file.
* No new mathematics, no computations beyond greps.

Waiting for the parent's review.
