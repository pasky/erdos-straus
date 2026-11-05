# z58 falsifier screens (mandatory for every z58 lane)

Files (all CERTIFIED; sources in the headers):
* `star_prime_zeros.txt` — the 14 primes p ≡ 1 (4) ≤ 10¹⁰ with R(p) = 0 (9 of them in Mordell's classes 𝔐).
* `gstar_zeros.txt` — the 38 primes p ≡ 1 (4) ≤ 10¹⁰ with R_𝔊*(p) = 0 (20 in 𝔐).
* `r8_zeros_1e10.txt` — the 12 primes in [10¹⁰, 1.1·10¹⁰] with R₈(p) = 0 (C-even half of (★) = c = 1 line of 8/p); R(p) ≥ 12 there.
* `composite_zeros_le8e6.txt` — the 285 non-square composites n ≡ 1 (4), n ≤ 7 999 801, with R(n) = 0.
* Odd squares: R(m²) = 0 for every odd m (Lemma A.1(b) of Z57_SYNTH: every hit class is a Jacobi non-residue mod d).

Recompute R(n) for all n ≤ N: `gcc -O2 -o rstar scripts/z58_screens_rstar.c && ./rstar 9000000` (prints n ≡ 1 (4) with R(n) = 0,
tagged P / SQ / C). Faster engines for single large p: `scripts/z56_famdesign_decide.c`, `scripts/z57_synth_dec8.c`, `scripts/z57_synth_tri.c`.
𝔐 = {1, 121, 169, 289, 361, 529} mod 840.
