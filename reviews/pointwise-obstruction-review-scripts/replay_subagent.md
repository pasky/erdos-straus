# Replay test report

Working directory: `/home/pasky/projects/math/erdos-straus-claude-agent-worktree-0005`; commands run from repository root. Heavy Python commands used `ulimit -v 8000000`, `timeout`, `PYTHONPATH=scripts`, and `uv run --with python-flint python` (except dependency-free checks); concurrency was at most four jobs/cores. No repository files were intentionally changed; the `.venv` created by `uv` was moved to `/tmp` after the runs. Test-built executables, fibre output, and this report are under `/tmp`.

## Results table

| Item | Command used | Works as written? | Result | Time |
|---|---|---|---|---:|
| `pointwise_seed_check.py` | `PYTHONPATH=scripts uv run --with python-flint python scripts/pointwise_seed_check.py` | Y with stated `scripts/` path | 8 tests pass, `OK` | 8.58s |
| `pointwise_fibres_check.py` | `... python scripts/pointwise_fibres_check.py` | Y only with `scripts/` prefix; paper's bare filename fails | 8 tests pass, `OK` | 5.46s |
| `pointwise_incidence.py 297049` | `... python scripts/pointwise_incidence.py 297049` | Y only with `scripts/` prefix | 1,143 vertices; seed-to-positive path in 3 moves | 3.44s |
| `depth3_check.py` | `... python scripts/depth3_check.py` | Y with `scripts/` path | 5 tests pass, `OK` | 4.00s |
| `depth3_validate.py 13 30000` | `... python scripts/depth3_validate.py 13 30000` | Y only with `scripts/` prefix | checked 1,610; 0 mismatches; dist>2=0 | 18.93s |
| `depth5_branches.py 13 3000000` | `... python scripts/depth5_branches.py 13 3000000` | Y only with `scripts/` prefix | primes by p mod 24 `{13:27096,17:27088,5:27115,1:26983}`; no H-branch `{1:1463}`; no branch `{1:689}` | 15.23s |
| `depth3_allp.cpp` | `g++ -O2 -std=c++17 scripts/depth3_allp.cpp -o /tmp/depth3_allp`; run no args | Compile Y; survey not run; needs compilation | Builds; prints `usage: P0 P1 THREADS` | 0.95s compile |
| `depth3_sieve.cpp` | `g++ -O2 -std=c++17 scripts/depth3_sieve.cpp -o /tmp/depth3_sieve`; run no args | Compile Y; survey not run; needs compilation | Builds; prints `usage: S Q0 Q1 THREADS` | 0.79s compile |
| `depth3_batch.py` | `... python scripts/depth3_batch.py --help` | Y with `scripts/` prefix; requires positional file for run | Usage prints (`file`, `--jobs`, `--all`, `--skip9`); no survey launched | 0.77s |
| `formal2_verify.py` (full) | paper's two input paths; also `... formal2_verify.py --help` | Invocation starts but full verification deliberately stopped; usage works | Valid invocation made progress with no output within 60s, stopped by timeout (124). `--help` gives usage and shows default `--jobs 14`, optional `--cert` | 60.03s timeout; help under 60s |
| `formal2_verify_extra.py` | `... python scripts/formal2_verify_extra.py data/formal_closure/lam_final.json data/formal_closure/closure_final.json.gz` | Y | `OK:true`; 9,961 nondead denominators; auxiliary factors in S=7,364; all checks true | 271.51s (4m31.5s) |
| `review_fc_global.py` | `PYTHONPATH=scripts ... python scripts/review_fc_global.py` | Y | all checks pass; 7,883 vertices, one component, C3 1,271 primes/0 failures | 27.89s |
| `review_fc_fibres.py` | `PYTHONPATH=scripts ... python scripts/review_fc_fibres.py --all --jobs 4 --out /tmp/review_fc_fibres_all.json` | Y | `equal=9961`, `exceptions=0`, all other failure counts 0; pass(A)=533,011,471; output JSON created | 501.34s (8m21s) |
| `formal2_iter.py` | `... python scripts/formal2_iter.py --help`; then `... formal2_iter.py init --help` | Script exists, but top-level `--help` fails; subcommand help works | Top-level raises `KeyError: '--help'`; `init --help` documents invocation. Must pass `init`, `explicit`, `analyze`, or `finalize` | <1s |
| `formal2_realq.py` | `... python scripts/formal2_realq.py --help` | Y with `scripts/` prefix and python-flint | Usage prints (`lamfile dump`, options); no computation launched | <1s |
| `sterile_certificate_check.py` | `... python scripts/sterile_certificate_check.py data/sterile/certs/*.json.gz` | Y as invocation/path; not completed | Data glob resolves to 7 tracked certificate files, but full run exceeded 1,200s timeout; no buffered result before stop | 1,200.01s timeout (124) |
| `windmill_*.py` | `... python scripts/windmill_misc_checks.py lam` | Y with `scripts/` path (this is one quick representative) | `732 {'NII/2': 380, 'NI/2': 350, 'N/2': 370}` | 0.51s |
| `windmill_singleton.cpp` | `g++ -O2 -std=c++17 scripts/windmill_singleton.cpp -o /tmp/windmill_singleton`; then `/tmp/windmill_singleton 10000` | Compiles and runs when given required `T`; no-arg invocation segfaults | `T=10000 candidates(...)=6523 hits=0 hits_with_p_prime=0` | 0.24s compile; <0.01s run |

## Command/output log (trimmed)

All Python commands below were run from the repository root under the stated environment/limits. `...` below means `ulimit -v 8000000; export PYTHONPATH=scripts; timeout <limit> uv run --with python-flint python`.

1. `... scripts/pointwise_seed_check.py` — 8 unit tests `ok`; `Ran 8 tests ... OK` (8.58s).
2. `... scripts/pointwise_fibres_check.py` — 8 tests `ok`; `Ran 8 tests ... OK` (5.46s).
3. `... scripts/pointwise_incidence.py 297049` — `p=297049`, 1,143 signed vertices / 67 positive; shortest seed-to-positive path is 3 moves (3.44s).
4. `... scripts/depth3_check.py` — 5 tests `ok` (4.00s).
5. `... scripts/depth3_validate.py 13 30000` — `checked 1610 mismatches 0 primes with A-hits 1609 with B-hits 1162 dist>2: 0` (18.93s).
6. `... scripts/depth5_branches.py 13 3000000` — completed; summarized in table. It printed many `no branch: <p>` intermediate lines (15.23s).
7. C++ compile commands above all succeeded. No-argument usage works for both depth3 C++ programs. Compiled `windmill_singleton` has no argc guard: invoking without T exited 139; supplying `10000` succeeds.
8. `... scripts/depth3_batch.py --help` — usage displayed; survey not run.
9. `... scripts/formal2_verify.py data/formal_closure/lam_final.json data/formal_closure/closure_final.json.gz` — timeout after exactly 60.03s, exit 124, no error/output; this only tests start-up, not correctness. `... scripts/formal2_verify.py --help` prints valid usage in under a minute. **The full ~2h50 verification was not run.**
10. `... scripts/formal2_verify_extra.py data/formal_closure/lam_final.json data/formal_closure/closure_final.json.gz` — output: `{"entry_flags_ok":true,"one_component":true,"nondead_Z":9961,"aux_factors_in_S":7364,"c_r_primes_in_LAM":true,"needE_recomputed_equal":true,"E_max":17,"log10_M":12087.8,"OK":true}` (271.51s).
11. `... scripts/review_fc_global.py` — output reports all boolean checks true/zero failures; `C3: {'primes_checked': 1271, 'failures': []}`; 27.89s total.
12. `... scripts/review_fc_fibres.py --all --jobs 4 --out /tmp/review_fc_fibres_all.json` — final summary `n=9961`, `equal=9961`, `exceptions=0`, `prec_fail=0`, `c_r_outside=0`, `aux_precision_fail=0`, `aux_not_in_S=0`, `errors=0`, `passA_total=533011471`, `time=500`; 501.34s wall time.
13. `... scripts/formal2_iter.py --help` errors with `KeyError: '--help'`; `... scripts/formal2_iter.py init --help` works and prints subcommand usage. `... scripts/formal2_realq.py --help` works.
14. `... scripts/sterile_certificate_check.py data/sterile/certs/*.json.gz` — timed out at 1,200s (124), with no visible output. Seven matching certs exist (tracked under `data/sterile/certs/`).
15. `... scripts/windmill_misc_checks.py lam` — `== lam` then `732 {'NII/2': 380, 'NI/2': 350, 'N/2': 370}` (0.51s).
16. C++ `depth3_batch --help` and C++ usage checks as above; no full 10^12 survey run.
17. Bare-path check: `uv run python pointwise_fibres_check.py` fails (`can't open file .../pointwise_fibres_check.py`); the script is actually `scripts/pointwise_fibres_check.py`.

## Replay wording / data notes

- The appendix's blanket “All commands run from the repository root” is not enough to disambiguate commands listed as bare filenames. Only some bullets include `scripts/`; root-level Python invocation of `pointwise_fibres_check.py` demonstrably fails. The executable paths should consistently be written `scripts/<name>` (or explicitly say `cd scripts`). C++ commands also need compiler commands and arguments; merely listing source filenames is not an invocation.
- The specified certificate glob exists and expands to seven files. Its checker run is unusually slow in this environment (>20 minutes), so no per-certificate OK result was obtained.
- `data/formal_closure/certificate.json.gz` exists (350K), as do `lam_final.json` (61K) and `closure_final.json.gz` (498K). The section says the certificate file contains the closure data. The main verifier and extra verifier replay commands take **lam_final + closure_final**, not `certificate.json.gz`; `formal2_verify.py --cert` is an optional *output* option, not an input-certificate flag. In contrast, the independent `review_fc_global.py` and `review_fc_fibres.py` load `certificate.json.gz` internally through `review_fc_common.py` as well as loading closure/lam files. This distinction should be clarified in the paper's replay prose.
- Runtime claims: `formal2_verify_extra.py` took 4m31s here, versus the stated 4m (close but ~32s slower); global review was 28s, consistent with “under one minute”; fibre review found exactly 9961/9961 equal fibres and took 8m21s with 4 jobs, faster than the stated 12m on 8 cores (different machine/core count likely explains this). The 2h50 main verifier claim was not independently tested beyond confirming startup/usage.
- `formal2_iter.py --help` itself is broken because the script dispatches directly on `sys.argv[1]`; a subcommand such as `init --help` works. Mention `init`/etc. rather than advertising a top-level CLI help command.
