#!/bin/bash
# runs the HC census in chunks; usage: z55_hco_runcensus.sh START END STEP THR
set -e
BIN=/tmp/z55_hco_census
S=$1; E=$2; STEP=$3; THR=$4
a=$S
while [ "$a" -lt "$E" ]; do
  b=$((a+STEP)); [ "$b" -gt "$E" ] && b=$E
  out=data/z55/hco/census_${a}_${b}.txt
  if [ ! -s "$out" ]; then
    ( ulimit -v 6000000; OMP_NUM_THREADS=16 timeout 1800 $BIN $a $b $THR > $out.tmp && mv $out.tmp $out )
  fi
  a=$b
done
