# Replaying the finite Proth certificates

The four `period-*` files with empty `left` are proof objects, not discovery logs. From the repo root run

```
ulimit -v 1500000
timeout 120 uv run --offline --no-project python -B scripts/z78_proth_check.py small groups census shift period-7-55440.json period-8-12252240.json period-9-411863760.json period-10-55440.json
```

This checks every residue of each period, all 1,920 small triples, all compressed core witnesses, bounded-mask hits and fixed-row coverage in the common-period census. `shift` verifies the positive degree-one progressions, not completeness. Independent review/replays are recorded in `../xreview/REVIEW_PROTH_ALLM_OPUS.md`. `replay.txt` is the run without the supplementary `shift` switch.

Discovery recipe (optional; use a scratch checkout because the search overwrites intermediate files). Each line below gives script suffix and integer parameters; execute in sequence as `ulimit -v 2200000; timeout 600 uv run --offline --no-project --with cypari2 python -B scripts/z78_proth_SUFFIX.py ARGS`. The checker needs no PARI.

```
period 7 55440 30000
finish 7 55440 55440
period 8 55440 30000
finish 8 55440 55440
finish 8 55440 720720
finish 8 720720 12252240 12000
square 8 12252240
period 9 55440 30000
finish 9 55440 55440
finish 9 55440 942480 12000
square 9 942480
finish 9 17907120 17907120 16000
target 9 17907120 1500000
finish 9 17907120 411863760 18000
period 10 55440 30000
finish 10 55440 55440
```

The `group`, `exact_core`, `census`, `small` and `shift` suffixes take no arguments. Absence of a bounded-mask hit in the census is not a method impossibility theorem. The finite-index evidence uses PARI; the positive products do not depend on trusting the factorization/discrete-log engine.
