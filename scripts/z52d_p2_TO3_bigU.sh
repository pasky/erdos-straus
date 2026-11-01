#!/bin/bash
# Fix round TO3: count-program runs (U(p), U(m^2), family checks). Needs /tmp/z52/count4 (gcc -O2 scripts/z52b_fingerprint_count.c)
# and /tmp/z52/exists (gcc -O2 scripts/z52d_p2_TO3_exists.c). Results -> /tmp/z52/big/*.txt (large, not committed)
cd /tmp/z52/big
# (a) sample of primes 1 mod 4 near 1e8 (fixed list chosen by scripts/z52d_p2_TO3_pick1e8.py)
cat primes1e8.txt | xargs -P4 -I{} sh -c 'ulimit -v 9000000; /tmp/z52/count4 4 {} {} 0' > U1e8.txt
# (b) U(m^2), odd m <= 600 (and m^2 +- 1, 2 neighbours)
for m in $(seq 3 2 599); do echo $((m*m)); done > sq_list.txt
cat sq_list.txt | xargs -P4 -I{} sh -c '/tmp/z52/count4 4 {} {} 0' > Usq.txt
# (c) 16/p-style: 8/p existence to 1e8
/tmp/z52/exists 8 2 100000000 1 > ex8_1e8.txt
