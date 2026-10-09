#!/bin/bash
# usage: scripts/m13e_run.sh NLO NHI OUTDIR [CHUNK]  — complete ES enumeration (m13e_es, chunks of CHUNK x-values,
# 2 parallel workers, ulimit -v 8e6, timeout 6h per chunk) + inversion/point test (m13e_inv) for every
# {11,13}-unit N with NLO < N <= NHI.  Logs commands and results to OUTDIR/log.
NLO=$1; NHI=$2; OUT=$3; CH=${4:-250000000}; mkdir -p $OUT
gcc -O2 -march=native -o $OUT/es scripts/m13e_es.c -lm || exit 1
echo "# $(date) m13e_run.sh $*  (git $(git rev-parse --short HEAD))" >> $OUT/log
NS=$(python3 -c "print(' '.join(str(11**i*13**j) for i in range(12) for j in range(12) if $NLO<11**i*13**j<=$NHI and 11**i*13**j>1))")
for N in $(echo $NS | tr ' ' '\n' | sort -n); do
  [ -f $OUT/inv_$N.pkl ] && continue
  python3 -c "
N=$N; lo=N//4+1; hi=3*N//4; c=$CH
while lo<=hi: print(N, lo, min(hi, lo+c-1)); lo+=c" > $OUT/tasks_$N
  xargs -P 2 -L 1 bash -c 'f='$OUT'/es_$0_$1.txt; tail -1 $f 2>/dev/null | grep -q "^# N=" || (ulimit -v 8000000; timeout 6h '$OUT'/es $0 $1 $2 > $f)' < $OUT/tasks_$N
  FILES=$(awk -v o=$OUT '{printf "%s%s/es_%s_%s.txt", (NR>1?",":""), o, $1, $2}' $OUT/tasks_$N)
  (ulimit -v 8000000; PYTHONPATH=scripts timeout 6h uv run python scripts/m13e_inv.py $N $FILES $OUT/inv_$N.pkl) >> $OUT/log 2>&1
done
echo "# $(date) done" >> $OUT/log
