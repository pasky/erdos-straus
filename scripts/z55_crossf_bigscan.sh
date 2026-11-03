#!/bin/bash
# z55 CROSSF: sampled scans of hits(p) at 1e13..1e18 (mode 2 of z55_crossf_cscan: K primes, step S). Each run under timeout/ulimit.
cd "$(dirname "$0")/.." || exit 1
ulimit -v 6000000
D=data/z55/crossf
run() { e=$1; K=$2; S=$3; timeout 1700 /tmp/z55cscan $((10**e)) $K $S > $D/sample_1e$e.txt 2> $D/sample_1e$e.summary; }
run 13 20000 100000
run 14 10000 1000000
run 15 4000 10000000
run 16 1500 100000000
run 17 800 1000000000
run 18 400 10000000000
