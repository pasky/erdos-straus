#!/bin/bash
# z59 MSPLUS out-of-sample test of the zero law: exact zero census on chosen classes mod 840 in [1e10, 1e11].
set -u
gcc -O2 -o /tmp/z59_msplus_cdec scripts/z59_msplus_cdec.c -lm || exit 1
ulimit -v 4000000
O=data/z59/msplus/oos
C105=105,525
C15=45,165,225,285,345,405,465,585,645,705,765,825
C21=$(python3 -c "print(','.join(str(a) for a in range(840) if a%4==1 and a%21==0 and a%5))")
C3=$(python3 -c "print(','.join(str(a) for a in range(840) if a%4==1 and a%3==0 and a%5 and a%7))")
run() { timeout 1800 /tmp/z59_msplus_cdec $2 $3 $4 > $O/$1.txt; echo "exit=$? args=$2 $3 $4" > $O/$1.status; }
run g105_1e10_1e11 10000000001 100000000000 $C105
run g15_1e10_5e10 10000000001 50000000000 $C15
run g15_5e10_1e11 50000000001 100000000000 $C15
run g21_1e10_5e10 10000000001 50000000000 $C21
run g21_5e10_1e11 50000000001 100000000000 $C21
# The pre-registered '3 | n only' row ($C3) was run by the internal reviewer in three chunks with the same binary;
# output in data/z59/msplus/review_g3/ (1 zero: 10234561689).
