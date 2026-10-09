# AGENT REPORT O119 — consolidation (verify blocks + STATUS/SUMMARY)

Branch `side-agent/consolidate-oct10`. No new mathematics; no label changed.

## (1) verify.py blocks (eo)–(er) (+ ~47 s)
* (eo) EXCEPTIONAL_MN4: R117 `review_emn4_lemma11/forms/exponents.py` + author `emn4_checks.py` (11 s).
* (ep) EXCEPTIONAL_TYPEI_LOGLOG2: R116 `review_ttl2_analytic.py`, `review_ttl2_exponents.py 100000` (reduced; the
  script got an optional sample-size argument, default unchanged 4·10⁵), R116-B `review_ttl2b_*` (21 s).
  Note: the R116 exponent script reports a handful of (b2) "violations" ≤ 3·10⁻⁴ in exponent at any sample size;
  these are the reviewer's deliberate O(1) cells (review V5). The block asserts (b3)/(b5) = 0 and (b2) excess ≤ 3·10⁻⁴.
* (eq) POINTWISE_MORDELL13E: R107 `review_m13e_parity.py 400 1` (0/71 failures); m13e_es.c = m13b_es.c at N = 1859,
  24167 (918, 3529 solutions); chunked = unchunked at 1859; `m13e_inv.py` at 1859: x** no box, x* positive control =
  I2 (125,88,11999), II3 (8,33,11999) (11 s; gcc parts skip without gcc).
* (er) POINTWISE_TYPEI7: R109 `review_typei7_check.py` (Thm 2.1/2.4 families, tower, orders, Comp 2.5 table) and
  `review_typei7_lemma11.py 400000` (64 certs, 1442 checks, 0 failures) (4 s).
* Full `verify.py` (ulimit -v 8e6, 2 threads, scipy + mpmath): **all checks passed**, ≈ 8.7 min; log
  `logs/o119_verify.log`.

## (2) STATUS.md / CAMPAIGN_SUMMARY.md
* STATUS refresh 8: new top "Headline results of the current phase" (m-uniform 3/4 rel. note; density transition
  U/L′ and sharp order under SEL_m; ET Type I o(N log²N log log N) unconditional rel. DI Thm 7/Drappeau 4.10,
  ≪ N log²N under SEL or (EFF); x* refuted / x** survives to 2.59·10¹⁰; TYPEI7 negative result; papers — the new
  results are in no paper yet). TYPEI_LOGLOG bullet updated with (D)32a and MN4; TYPEI7 and MORDELL13E bullets;
  Housekeeping bullet (eo)–(er).
* CAMPAIGN_SUMMARY: title, §1, §2.6 (MN4), §2.7 (retitled; (D)32a), §3 (TYPEI7, MORDELL13E), table rows E33/E34,
  P58/P59 (E32 wording fixed), §5 not-audited list, §6 open problems, §7 reading guide.

Commits: 32ddabf … (see `git log main..`). Not merged.
