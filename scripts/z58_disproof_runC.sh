#!/bin/bash
# z58 DISPROOF batch C: decision-mode targeted search (R, R8, R_odd, H3 decided; exact enumeration only when undecided)
# in the hardest designs at 1e12-1e14.  6 processes, timeout 1750 s each, ulimit -v 6e6.  Output data/z58/disproof/runC/
set -e
D=$(dirname "$0")/../data/z58/disproof/runC; mkdir -p "$D"; cd "$D"
gcc -O2 -o /tmp/z58engC ../../../../scripts/z58_disproof_eng.c -lm
ulimit -v 6000000
# k = 1680 kills lines u = 1, 2, 10, 14, 21, 35 (Lemma 2.3); p = m^2 + 1680 is a square mod 1680 (in M if gcd(m,210)=1)
nohup timeout 1750 /tmp/z58engC nsq 1000000000000 10000000 1680 1 31 > K1680_z31_e12.txt 2> K1680_z31_e12.err &
nohup timeout 1750 /tmp/z58engC nsq 10000000000000 10000000 1680 1 23 > K1680_z23_e13.txt 2> K1680_z23_e13.err &
nohup timeout 1750 /tmp/z58engC ap 1000000000000 10000000 840 1 61 > SM61_e12.txt 2> SM61_e12.err &
nohup timeout 1750 /tmp/z58engC ap 10000000000000 10000000 840 1 47 > SM47_e13.txt 2> SM47_e13.err &
nohup timeout 1750 /tmp/z58engC ap 100000000000000 10000000 840 1 37 > SM37_e14.txt 2> SM37_e14.err &
nohup timeout 1750 /tmp/z58engC nsq 100000000000000 10000000 840 1 13 > K840_z13_e14.txt 2> K840_z13_e14.err &
