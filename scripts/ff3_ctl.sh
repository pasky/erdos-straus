#!/bin/bash
# ff3_ctl.sh (O173): control for §3 — random slice points u == 1+T (mod T^m), complete j-range, deg L' <= lmax;
# prints the number of distinct Case B families per point.  Needs: gcc -O2 -o /tmp/ff3_caseB scripts/ff3_caseB.c
m=$1; n=$2; lm=$3; s0=$4
for s in $(seq 1 $n); do
 u=$(python3 -c "
import random; random.seed($s+$s0); d=[1,1]+[0]*($m-2)+[random.randrange(3) for _ in range(70)]; print(' '.join(map(str,d)))")
 h=$(/tmp/ff3_caseB 3 2 1 $lm -1 $u | grep HIT | awk '{print $3,$4,$6,$7,$8}' | sort -u | wc -l)
 echo $h
done
