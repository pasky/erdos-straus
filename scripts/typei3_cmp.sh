#!/bin/bash
# O72: compare certificate sets (ck <= X) from typei2_signcheck (ck-graded) and typei3_fsearch (f-graded).
# usage: SIGNCHECK=/path/signcheck FSEARCH=/path/fsearch typei3_cmp.sh r w X ; exits 1 on any difference.
# (R72 repair D1, applied by reviewer) If w<0, the divisor f=-w has infinite role depth (v_2(f+w)=inf) and
# typei3_fsearch correctly aborts there.  We then run the f-engine on [1,-w) and [-w+1, B) and exclude from
# BOTH sets every certificate having -w as one of its two complementary divisors (F or N/F); the numbers of
# excluded certificates are reported.  (For w=-1 the e-role depth at f=1 is infinite too; f=1 is never in the
# f-engine's progression f=1 (mod r), f=-w (mod 4), f>=3.)
set -euo pipefail
r=$1; w=$2; X=$3
SC=${SIGNCHECK:-/tmp/signcheck}; FS=${FSEARCH:-/tmp/fsearch}
[ -x "$SC" ] && [ -x "$FS" ] || { echo "missing binaries $SC $FS" >&2; exit 2; }
d=$(mktemp -d)
B=$(python3 -c "import math;print(math.isqrt(4*$X*$X//$r+1)+2)")
"$SC" $r $w $X 100000000 > $d/sc.raw
EXCL=0
if [ "$w" -lt 0 ] && [ $((-w)) -lt "$B" ]; then
  EXCL=$((-w))
  "$FS" $r $w 1 $EXCL > $d/fs.raw
  "$FS" $r $w $((EXCL+1)) $B > $d/fs2.raw
  grep -q 'f tested' $d/fs.raw && grep -q 'f tested' $d/fs2.raw || { echo "engine did not finish" >&2; exit 2; }
  cat $d/fs2.raw >> $d/fs.raw
else
  "$FS" $r $w 1 $B > $d/fs.raw
fi
grep -q 'unforced slices' $d/sc.raw && grep -q 'f tested' $d/fs.raw || { echo "engine did not finish" >&2; exit 2; }
(grep '^CERT' $d/sc.raw || true) | sed 's/ck=[0-9]* //' | awk '{print $2,$3,$4}' | sed 's/[ckF]=//g' | sort -u > $d/sc.all
(grep '^CERT' $d/fs.raw || true) | awk -v X=$X '{split($9,a,"=");if(a[2]+0<=X)print $2,$3,$4}' | sed 's/[ckF]=//g' | sort -u > $d/fs.all
EXCLPY='
import sys
ex = int(sys.argv[1]); n = 0; out = []
for line in open(sys.argv[2]):
    c, k, F = map(int, line.split()); N = 1 + 4 * c * k * k
    if ex and ex in (F, N // F):
        n += 1; continue
    out.append(line)
open(sys.argv[3], "w").writelines(out)
if ex: print(f"{sys.argv[4]}: excluded {n} certificates with divisor {ex} (infinite depth)")
'
python3 -c "$EXCLPY" "$EXCL" $d/sc.all $d/sc.txt signcheck
python3 -c "$EXCLPY" "$EXCL" $d/fs.all $d/fs.txt fsearch
n1=$(wc -l <$d/sc.txt); n2=$(wc -l <$d/fs.txt)
if diff -q $d/sc.txt $d/fs.txt >/dev/null; then echo "r=$r w=$w X=$X signcheck $n1 fsearch $n2 IDENTICAL"; rm -r $d
else echo "r=$r w=$w X=$X signcheck $n1 fsearch $n2 DIFFER (see $d)"; exit 1; fi
