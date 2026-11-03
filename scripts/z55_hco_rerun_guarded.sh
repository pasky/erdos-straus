#!/bin/bash
# Re-run census chunks that were produced before the tau-guard was added (start < 3.02e11) with the guarded binary
# and compare (sorted) output with the archived files.
set -e
mkdir -p /tmp/z55rerun
for f in data/z55/hco/census_*.txt; do
  r=$(grep -o 'RANGE \[[0-9]*,[0-9]*)' $f | tr -d 'RANGE[)' | tr ',' ' ')
  set -- $r; a=$1; b=$2
  [ "$a" -ge 302000000000 ] && continue
  thr=44; [ "$a" -eq 0 ] && thr=40
  out=/tmp/z55rerun/$(basename $f)
  ( ulimit -v 6000000; OMP_NUM_THREADS=20 timeout 1800 /tmp/z55_hco_census $a $b $thr > $out )
  if cmp -s <(sort $f) <(sort $out); then echo "IDENTICAL $a $b"; else echo "DIFFER $a $b"; fi
done
