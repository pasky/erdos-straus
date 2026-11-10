#!/bin/bash
# z70 CLASS corrected-null runs (Z70_CLASS.md §1.9).  Usage: bash scripts/z70_class_run2.sh CHAIN (P | Q)
cd "$(dirname "$0")/.." || exit 1
ulimit -v 6000000
OUT=data/z70/class
fail=0
job() {  # mode d tag P0 P1 seed
  timeout 1800 uv run --with sympy --with numpy python scripts/z70_class_nullfix.py $1 $2 200 $6 range $4 $5 > $OUT/i1_FIX$1_d$2_$3.txt.tmp 2>&1
  rc=$?; if [ $rc -eq 0 ]; then mv $OUT/i1_FIX$1_d$2_$3.txt.tmp $OUT/i1_FIX$1_d$2_$3.txt; else fail=1; fi
  echo "done FIX-$1 d=$2 $3 rc=$rc"
}
W1="F1 24000 30000|F2 202000 206000|F3 1001000 1004000|F4 4000000 4003000|G1 500000 503000|G2 2000000 2003000|G3 8000000 8002000|H1 3000000 3003000|H2 6000000 6002000"
W2="F1 24000 30000|F2 202000 210000|F3 1001000 1005000|G1 500000 510000|G2 2000000 2006000|H1 3000000 3006000"
W3="F1 24000 30000|F2 202000 210000|F3 1001000 1005000|H1 3000000 3010000"
W57="F1 24000 30000|F2 202000 210000|F3 1001000 1005000"
case "$1" in
P) IFS='|'; for w in $W1; do IFS=' '; set -- $w; job CS 1 $1 $2 $3 811; job ALL 1 $1 $2 $3 812; IFS='|'; done ;;
Q) IFS='|'; for w in $W2; do IFS=' '; set -- $w; job CS 2 $1 $2 $3 821; job ALL 2 $1 $2 $3 822; IFS='|'; done
   IFS='|'; for w in $W3; do IFS=' '; set -- $w; job CS 3 $1 $2 $3 831; job ALL 3 $1 $2 $3 832; IFS='|'; done
   IFS='|'; for w in $W57; do IFS=' '; set -- $w; job CS 5 $1 $2 $3 851; job CS 7 $1 $2 $3 871; IFS='|'; done ;;
esac
exit $fail
