# AGENT REPORT O113 — final consolidation of the 2026-10-09 round

Branch `side-agent/consolidate-oct9b`. Not merged.

## (1) verify.py blocks (el)–(en)
Reviewers' scripts come first; inline checks are added where they are cheap. Added runtime is about 42 s.
* **(el) EXCEPTIONAL_MN3.**
  * R108 `review_emn3_prop23.check_pointwise` at full size: 0 failures.
  * Six R108 sum rows replayed; they are identical to the stored table.
  * `emn3_coprime.py 120` (§2.6) gives ratios in [0.81, 1.11]. It takes 6 s, not the "~3 min" the Replay section says.
  * R108 `review_emn3_sec3.py`: brute force for p < 180, with 0 identity failures and 0 violations.
  * Inline: the Prop 3.3 exponent table, and the "all moduli ≥ 1−η ⇔ R_bad(η)" check on random rational points (η = 0, 1/20).
  * Inline: the areas **exactly** (slice 1, R_bad 1/6, R** 7/72), by rational polygon clipping.
* **(em) EXCEPTIONAL_TYPEI_LOGLOG.**
  * R111 `review_ttl_sep.py`: Lemma 2.1 exact, Lemma 2.2 cosh ≥ 3/2 with the bound attained, parity group.
  * The author's `ttl_separation.py`.
  * `o112_checks.py 5 20 40` (reduced size). The script now takes optional CMAX AMAX DMAX; the defaults reproduce the recorded run.
  * R111 `review_ttl_local.py` in full: Lemma 6.1 transitivity and g formulas, Lemma 6.3 r(d) bound.
* **(en) POINTWISE_MORDELL13D.**
  * `m13d_wit.c` (gcc) gives the same witness sets as `m13c_witness.witness_all` for every unit mod 9240 and mod 10920. There are 113942 and 132276 incidences; the first count equals R100's figure in (eh).
  * Every witness class was checked, and the first mode is consistent.
  * The req = 13 mode is exact (26424 incidences).
* **Full run:** `verify.py` printed "all checks passed" and exited 0, in about 8.5 min (2 threads, ulimit 8 GB). Log: `logs/o113_verify.log`.
* STATUS has a new Housekeeping bullet for these blocks.

## (2) paper/es-mn-short-note.tex
* **Theorem L → Theorem L′:** `ρ_rep ≪ (L³+L² log² m) log L/m + m^{−0.35}`. Its dependencies now include PV.
* **Lemma 8.6** is now MN3 Prop 2.3 with a full proof (coprime harmonic sums, the indicator, the four r-ranges, PV and Kronecker-PV).
* **New Remark 8.7:** the comparison with ET, plus the §2.6 EVIDENCE.
* **Prop 8.8** is now MN3 Prop 2.5. For m ≤ m₀ the bound is trivial.
* **Proof of L′:** φ(m) is replaced by m.
* **Gap:** now `(log L)^{1/3} = (log log N)^{1/3}`, updated in the abstract, intro and §8.4. The PW comparison factor is `(m/φ(m)) min(log m, L/log m)`.
* **New Remark 8.10:** cites [TTL] Thm 8.1 = (D)32 as CONDITIONAL, for m = 4 only. It says the m-uniform extension has not been carried out.
* **Other updates:** the open problem on the gap, status/novelty, and the bibliography entries [MN3] and [TTL].
* **Hyperref:** I wrapped three pre-existing section titles in `\texorpdfstring`.
* **Build:** 26 pp. Two compiles with 0 warnings, 0 undefined references and 0 overfull boxes.
* `reviews/es-mn-short-note-referee.md` has a "Post-referee addition (O113)" section. **These changes have not been refereed.**

## (3) STATUS.md and CAMPAIGN_SUMMARY.md
* Both now refer to the ledger through (D)32. They cover MN3, TTL, MORDELL13D, the coverings note (29 pp, R106) and the es-mn-short-note O113 changes.
* CAMPAIGN_SUMMARY gains a new §2.7 (TTL), table rows E31, E32 and P57, and updates to the open problems, the not-audited list and the reading guide.

## Flags for the parent
* **Ledger vs document disagree:** (D)32 says the unconditional strip is `0 < 2α−1+γ ≲ 0.1`, but the O112-repaired TYPEI_LOGLOG §0 says `≲ 7/32 ≈ 0.22` (`≥ 0.16`). The summaries now say "a strip of positive width" with no number. The ledger should be fixed.
* **Stale runtime:** the MN3 Replay section's "~3 min" for `emn3_coprime.py 120` is out of date; it takes 6 s.
