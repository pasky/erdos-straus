#!/bin/bash
# z59 MSPLUS structured search: generate family FAM (COUNT, SEED) and decide with z59_msplus_dec (LIM = 1e7).
set -u
FAM=$1; COUNT=$2; SEED=$3
gcc -O2 -o /tmp/z59_msplus_dec_$FAM scripts/z59_msplus_dec.c || exit 1
ulimit -v 4000000
timeout 1800 uv run --with sympy python scripts/z59_msplus_gen.py $FAM $COUNT $SEED | timeout 1800 /tmp/z59_msplus_dec_$FAM 10000000 | gzip -9 > data/z59/msplus/struct/${FAM}_${SEED}.txt.gz
echo "exit=${PIPESTATUS[*]}" > data/z59/msplus/struct/${FAM}_${SEED}.status
