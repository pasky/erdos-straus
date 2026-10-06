#!/bin/bash
# O72: compare certificate sets (ck <= X) from typei2_signcheck (ck-graded) and typei3_fsearch (f-graded).
# usage: SIGNCHECK=/path/signcheck FSEARCH=/path/fsearch typei3_cmp.sh r w X ; exits 1 on any difference.
set -euo pipefail
r=$1; w=$2; X=$3
SC=${SIGNCHECK:-/tmp/signcheck}; FS=${FSEARCH:-/tmp/fsearch}
[ -x "$SC" ] && [ -x "$FS" ] || { echo "missing binaries $SC $FS" >&2; exit 2; }
d=$(mktemp -d)
"$SC" $r $w $X 100000000 > $d/sc.raw
"$FS" $r $w 1 $(python3 -c "import math;print(math.isqrt(4*$X*$X//$r+1)+2)") > $d/fs.raw
grep -q 'unforced slices' $d/sc.raw && grep -q 'f tested' $d/fs.raw || { echo "engine did not finish" >&2; exit 2; }
(grep '^CERT' $d/sc.raw || true) | sed 's/ck=[0-9]* //' | awk '{print $2,$3,$4}' | sort -u > $d/sc.txt
(grep '^CERT' $d/fs.raw || true) | awk -v X=$X '{split($9,a,"=");if(a[2]+0<=X)print $2,$3,$4}' | sort -u > $d/fs.txt
n1=$(wc -l <$d/sc.txt); n2=$(wc -l <$d/fs.txt)
if diff -q $d/sc.txt $d/fs.txt >/dev/null; then echo "r=$r w=$w X=$X signcheck $n1 fsearch $n2 IDENTICAL"; rm -r $d
else echo "r=$r w=$w X=$X signcheck $n1 fsearch $n2 DIFFER (see $d)"; exit 1; fi
