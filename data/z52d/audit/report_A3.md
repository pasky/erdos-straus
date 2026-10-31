# z52d audit — shard A3 (13 items; Opus blind redo, then compared with Haiku Pass 1)

ES is OPEN; nothing here bears on a proof. Blind verdicts: `opus_A3.jsonl`; comparison: `compare_A3.jsonl`;
scripts `scripts/z52d_audit_A3_*`, outputs `data/z52d/audit/A3/`.

**Counts by verdict:** AGREE 5 · MISS-MINOR 7 · MISS-MAJOR 1 · HAIKU-WRONG-COVERED 0 · HAIKU-BETTER 0.
Opus outcomes: covered 5, nothing 8 (interesting 0, needs-compute 0, skipped 0). Opus content scores: 0 ×4, 1 ×9; no
item reached 2 — this shard has no lost lead.

**MISS-MAJOR**
- Z1938 (Ramanujan-sum expansion of R): Haiku did not compute the d-contributions and recorded a false inference ("dominated
  by small d"); the actual expansion spreads the T1 cancellation over every d, with 4–8 of the ≈16 main term cancelled only
  by d > 10⁴. Low ES stakes, but the record's conclusion is wrong.

**Borderline MISS-MINOR (calibration lost, verdict unchanged):** Z1445 (prime-factor certificate not run; it fails at 237
primes ≤ 10⁷ vs 14 for (★)), Z1142 (underpowered 40-prime test missed the strong but residue-class-explained spectral
structure), Z3075 (the item's actual local-obstruction test not run; covered verdict correct anyway).

**Patterns in Haiku's failures**
1. *Substitution:* when the given step is slightly fiddly, Haiku runs a nearby easier computation (witness counts for
   d-contributions, C_min for prime-factor certificates, τ-stratified checks) and records the verdict for the item, at
   times with an inference the substitute cannot support (Z1938).
2. *Underpowered samples:* tiny ranges (40 primes, p < 1500, N < 3000), where a minute of compute gives a decisive answer.
3. *Reflexive `skipped` for meta / logic items* (Z1244, Z1603, Z1969, Z2497, Z3001): correct for genuine meta items, but in
   Z2497/Z3001 the question was answerable from the repo, so `covered` with a pointer was the right record.
4. Honesty is good: Haiku says when a sub-step was not run (Z3075, Z1445), and no `covered` verdict was wrong.

**Caveat on blindness:** for Z1892 a repo grep surfaced Haiku's Pass-1 line (ES_CONNECTIONS_TODO.md) before my attempt;
that verdict (MISS-MINOR) is contaminated. All other items were done blind.
