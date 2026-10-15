#!/bin/bash
# z17_rrun.sh (O242): box data for the r-generic line, r prime, through depth DMAX (P K <= 2DMAX-1, Q/U k <= DMAX odd).
# usage: scripts/z17_rrun.sh r DMAX OUTDIR      (memory/time bounded; run from the repo root)
set -e
r=$1; D=$2; O=$3; REPO=$(pwd); mkdir -p $O
ulimit -v 8000000
gcc -O2 -o $O/zre scripts/z17_renum.c
for k in $(seq 1 2 $D); do
  [ -s $O/Q$k.txt ] || timeout 20000 $O/zre $r Q $k 2>>$O/log | sort -u > $O/Q$k.txt
  [ -s $O/U$k.txt ] || timeout 20000 $O/zre $r U $k 2>>$O/log | sort -u > $O/U$k.txt
done
for K in $(seq 1 2 $((2*D-1))); do
  [ -s $O/p$K.txt ] || ZR=$r timeout 40000 uv run --project $REPO python scripts/z17_penum.py $K 2>>$O/log | sort -u > $O/p$K.txt
done
echo done >> $O/log
