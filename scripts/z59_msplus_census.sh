#!/bin/bash
# z59 MSPLUS: extend the in-Mordell-class (n mod 840 in M) exact R(n)>=1 census beyond 1e11, using the z58 LADDER
# decider scripts/z58_ladder_mdec.c unchanged (exact for composites; every n in M is coprime to 105).
# Usage: scripts/z59_msplus_census.sh LANE NLANES START_E10 END_E10   (chunks of 5e10 = 5 units of 1e10)
# Chunk k covers (START + 5k)*1e10 + 1 .. (START + 5k + 5)*1e10; chunks are dealt round-robin to lanes.
set -u
LANE=$1; NL=$2; S=$3; E=$4
OUT=data/z59/msplus/census
gcc -O2 -o /tmp/z59_msplus_mdec_$LANE scripts/z58_ladder_mdec.c -lm || exit 1
ulimit -v 4000000
k=0
for ((a=S; a<E; a+=5)); do
  if (( k % NL == LANE )); then
    A=$(( a * 10000000000 + 1 )); B=$(( (a + 5) * 10000000000 ))
    f=$OUT/mdec_${a}e10_$((a+5))e10.txt
    if [ -f $f.status ] && grep -q 'exit=0' $f.status; then k=$((k+1)); continue; fi
    timeout 1800 /tmp/z59_msplus_mdec_$LANE $A $B > $f; echo "exit=$? args=$A $B" > $f.status
  fi
  k=$((k+1))
done
