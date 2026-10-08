#!/bin/bash
# usage: scripts/m13b_run.sh NMAX OUTDIR  — ES enumeration + inversion for every {11,13}-unit N<=NMAX
NMAX=$1; OUT=$2; mkdir -p $OUT
gcc -O2 -o $OUT/es scripts/m13b_es.c
for i in $(seq 0 9); do for j in $(seq 0 9); do
  N=$(python3 -c "print(11**$i*13**$j)"); [ $N -le $NMAX ] && [ $N -gt 1 ] || continue
  [ -f $OUT/inv_$N.pkl ] && continue
  $OUT/es $N > $OUT/es_$N.txt 2>/dev/null
  PYTHONPATH=scripts uv run python scripts/m13b_invert.py $N $OUT/es_$N.txt $OUT/inv_$N.pkl
done; done
