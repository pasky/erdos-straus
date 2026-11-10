#!/bin/bash
# usage: scripts/z70_gen_runwin.sh TAG P0 P1 [OUTDIR]  (all d = 1,2,3,5,7 sequentially; one process; fails on error)
set -e
ulimit -v 6000000
TAG=$1; P0=$2; P1=$3; OUT=${4:-data/z70/gen}
for d in 1 2 3 5 7; do
  timeout 1800 uv run --with cypari2 python scripts/z70_gen_run.py $OUT/run_${TAG}_d$d.jsonl $d range $P0 $P1
done
