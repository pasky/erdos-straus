#!/bin/bash
# z58 DISPROOF batch B (6 processes, each timeout 1750 s, ulimit -v 6e6); output data/z58/disproof/runB/
set -e
D=$(dirname "$0")/../data/z58/disproof/runB; mkdir -p "$D"; cd "$D"
gcc -O2 -o /tmp/z58engB ../../../../scripts/z58_disproof_eng.c -lm
ulimit -v 6000000
EXACT=1 nohup timeout 1750 /tmp/z58engB ap 10000000000 100000 840 1 61 > SM61.txt 2> SM61.err &
EXACT=1 nohup timeout 1750 /tmp/z58engB ap 10000000000 100000 840 1 97 > SM97.txt 2> SM97.err &
EXACT=1 nohup timeout 1750 /tmp/z58engB nsq 10000000000 100000 840 3 0 > NSQnear.txt 2> NSQnear.err &
J0=100000 EXACT=1 nohup timeout 1750 /tmp/z58engB nsq 10000000000 100000 840 3 0 > NSQfar.txt 2> NSQfar.err &
EXACT=1 nohup timeout 1750 /tmp/z58engB ap 1000000000000 100000 24 1 0 > C0_12.txt 2> C0_12.err &
EXACT=1 nohup timeout 1750 /tmp/z58engB ap 1000000000000 100000 840 1 31 > SM31_12.txt 2> SM31_12.err &
