#!/bin/bash
# For every monic A over F_2 of degree kmin..kmax: covering tree (root W = A*T*(T+1)) with family threshold NTH,
# plus exhaustive check of all irreducible P of degree k+1..NTH-1 (ffl_es).  One line per A -> data/ffl/q2_batch.txt
kmin=${1:-1}; kmax=${2:-5}; NTH=${3:-12}
cd "$(dirname "$0")/.."
REF="10*11*111*10*11*1011*1101*10*11*111*10011*11001*11111*10*11"
for k in $(seq $kmin $kmax); do
  for i in $(seq 0 $(( (1<<k) - 1 ))); do
    A="1$(echo "obase=2; $i" | bc | awk -v k=$k '{printf "%0" k "d", $1}')"
    tr=$( ulimit -v 8000000; timeout 1800 /tmp/ffl_tree 2 $A "$A*10*11" "$REF" $NTH 14 5 | tail -1 )
    fails=""; for n in $(seq $((k+1)) $((NTH-1))); do
      f=$( ulimit -v 8000000; timeout 1800 /tmp/ffl_es 2 $A $n 0 1 /tmp/q2fail_${A}_$n.txt | grep -o "FAIL=[0-9]*" ); [ "$f" != "FAIL=0" ] && fails="$fails n=$n:$f[$(tr '\n' ' ' < /tmp/q2fail_${A}_$n.txt)]"
    done
    echo "A=$A | $tr | exhaustive n=$((k+1))..$((NTH-1)) fails:${fails:- none}" >> data/ffl/q2_batch.txt
  done
done
