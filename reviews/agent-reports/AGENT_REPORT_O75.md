# AGENT REPORT O75 — verify.py blocks (dn)–(ds)

Branch `side-agent/verify-blocks-5`. Not merged into main.

## What was added

Six replay blocks in `verify.py`, written in the style of (dj)–(dm), plus header entries and a
STATUS.md bullet. Each block is deterministic, has clear assertion messages and prints a one-line
summary.

| block | document | what is replayed | time |
|---|---|---|---|
| (dn) | EXCEPTIONAL_LARGESIEVE4 | Lemma 1.1: identity `Σ_S w_S P_S = E_T R_2(σ_T)` (author, 3 seeds × 2 weight modes) and the damped inequality `R_{2+2β} ≤ E_T R_2` under (A_w) (R62 toy, seeds 0–3, 8 laws, max ratio 0.998). Also the Lemma 2.1 η formula, Lemma 5.1 (author + R62), Prop 4.1 and Lemma 3.2 (16226 (Q,v)). Cor 5.3 residue counts: R62 plus an inline check over 106 primes, H = z^{1/4}/2 up to z = 20736. The named small-height classes lie in R(M) for M < 4000 | ~6 s |
| (do) | EXCEPTIONAL_LARGESIEVE5 | Lemma 1.2: the R67b brute force at G ≤ 600 (6792 classes, 1444997 congruent distinct-label pairs, min H₁H₂/g = 1.0017 ≥ 1/2, low-height uniqueness). An inline check of the R(M) label formula and the height bound M+1 for all M ≡ 3 (4), M < 6000 | ~3 s |
| (dp) | EXCEPTIONAL_LARGESIEVE6 | Prop 4.2 (4.1) and Thm 5.1 with its three sub-bounds on R71 exact toys: pool (2,3,5,7) with 8 classes, seed 2; pool (2,3,5) with 8 classes, seeds 1–4. Max \|σ̂\|/P4.2 = 0.20 and max \|σ̂\|/T5.1 = 0.11. The author's MC toy on pool (3,5,7,11) (Prop 2.2/4.2, 42230 Lemma 4.1 pointwise checks). R71 cube checks of Lemmas 2.1 and 4.1 | ~9 s |
| (dq) | POINTWISE_OMEGA17 | Lemma 5.2: R68b exact planted laws (192 instances: marginals, ν ≥ 0, ν(0) = 0, \|dν/dP−1\| ≤ s−1, with equality reached). An inline check of the closed form `e_{k+1−|y|}(r_{∖y})/e_{k+1}(r) ≤ s−1` on 390 odds vectors | ~1 s |
| (dr) | POINTWISE_TYPEI2 | Both C checkers (`typei2_signcheck.c`, `review_ti2_check.c`) are compiled into a tempdir (the step is skipped if there is no gcc/cc). At ck ≤ 10⁶, r = 7, w = 9 they find 1533438 slices and 0 certificates. Also run: w = −7, 25, 41 and r = 23, 31, 47, plus sanity certificates at w = 1, r = 11, 19. The R69 factoring engine over all slices ck ≤ 2000. Lemma 3.1 checked by direct search over every square (F, c, k), F ≤ 20001, r ∈ {7, 23, 31, 47}; I confirmed the search finds Prop 4.1's certificates for r = 11, 19. The 2-adic inputs. The Prop 4.1(i) identity for all 571 primes r ≡ 3 (8) below 20000 | ~4 s |
| (ds) | POINTWISE_MN | Lemma 1.1: author `mn_jacobi.py 50000 4 5 6 7 10` (0 failures; the §1 square-consistency counts match exactly) and R63 for 11 values of m (M ≤ 3000). Inline sympy check of (d) for m ≡ 0 (4) and of M ≡ 7 (8) ⇒ −1. The 4 smallest square-consistent examples | ~11 s |

The full `uv run --with scipy python verify.py` passes under `ulimit -v 8000000` with 2 threads:
296 s wall, 553 MB peak, "all checks passed". The new blocks add about 33 s.

## Notes for the parent

* All of these are EVIDENCE or brute-force replays of PROVED statements. No labels changed.
* (dr) needs a C compiler for the 10⁶ checker part. Without one it prints a skip and still runs
  the Python parts.
* Script edge case, not fixed (scripts are not mine to change): `review_ls6_exact_toy.run(3,
  (2,3,5,7), 8)` fails its own assertion `lhs <= pin*(1+1e-9)`, with lhs = 8e-17 and pin = 0.
  This is a floating-point Fourier zero against a purely relative tolerance. It is not a
  mathematical counterexample. (dp) avoids that configuration. An absolute slack of 1e-12 in the
  script would fix it.
* Scripts with top-level `sys.argv` parsing are run with a patched argv (runpy) or as
  subprocesses, so `verify.py` does not depend on its own command line.
