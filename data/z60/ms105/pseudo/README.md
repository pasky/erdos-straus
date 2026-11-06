# z60 MS105 — Lehmer pseudosquares
`A002189.txt`: the 52 distinct values of OEIS A002189 b-file (Greathouse, from Bernstein; up to 4.24·10^24).
`inputs.txt` (`scripts/z60_ms105_pseudo_gen.py 20`, seed 60105): each L_k (tag PS:k:depth) + 20 controls L + 840t,
|t| ≤ 10^6 (tag CT; for small L the controls are much larger than L).  `out_1e7.txt`: `scripts/z60_ms105_dec128.c 10^7`
("n first_d u C nhits LIM tag").  Zeros: 2641, 18001 only (known).  First hit ≥ Jacobi depth always.
