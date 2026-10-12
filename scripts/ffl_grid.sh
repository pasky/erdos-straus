#!/bin/bash
# usage: ffl_grid.sh q A nmin nmax [tmax_seconds]  -> appends to data/ffl/grid.txt; failure lists in data/ffl/fail_*.txt
# Runs n = nmin..nmax, stops after the first run exceeding tmax (default 900 s).  ulimit -v 8000000, 1 core.
q=$1; A=$2; nmin=$3; nmax=$4; tmax=${5:-900}
cd "$(dirname "$0")/.."
[ -x /tmp/ffl_es ] || gcc -O2 -o /tmp/ffl_es scripts/ffl_es.c -lm
for n in $(seq $nmin $nmax); do
  t0=$(date +%s)
  out=$( ulimit -v 8000000; timeout 7200 /tmp/ffl_es $q $A $n 0 1 data/ffl/fail_q${q}_A${A//,/_}_n${n}.txt )
  t1=$(date +%s); echo "$out time=$((t1-t0))s" >> data/ffl/grid.txt
  [ -s data/ffl/fail_q${q}_A${A//,/_}_n${n}.txt ] || rm -f data/ffl/fail_q${q}_A${A//,/_}_n${n}.txt
  [ $((t1-t0)) -gt $tmax ] && break
done
