#!/bin/bash
# Run the G* decider over [A, B] in chunks of size CH, J parallel jobs; outputs data/z57/bff/decide_<lo>_<hi>.txt
# usage: z57_bff_run_decide.sh A B CH J
A=$1; B=$2; CH=$3; J=$4
ulimit -v 6000000
gcc -O2 -o /tmp/z57dec scripts/z57_bff_decide.c -lm || exit 1
lo=$A
while [ $lo -lt $B ]; do
  hi=$((lo+CH)); [ $hi -gt $B ] && hi=$B
  while [ $(jobs -r | wc -l) -ge $J ]; do sleep 5; done
  ( timeout 1780 /tmp/z57dec $((lo+1)) $hi > data/z57/bff/decide_${lo}_${hi}.txt 2> data/z57/bff/decide_${lo}_${hi}.err; echo "exit=$?" >> data/z57/bff/decide_${lo}_${hi}.err ) &
  lo=$hi
done
wait
