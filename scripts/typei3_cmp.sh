#!/bin/bash
# usage: cmp.sh r w X
r=$1; w=$2; X=$3
/tmp/t72/signcheck $r $w $X 100000000 | grep '^CERT' | sed 's/ck=[0-9]* //' | awk "{print \$2,\$3,\$4}" | sort -u > sc.txt
Y=$(python3 -c "import math;print(int(math.isqrt(4*$X*$X//$r+1))+2)")
/tmp/t72/fsearch $r $w 1 $Y | grep '^CERT' | awk -v X=$X '{split($9,a,"=");if(a[2]+0<=X)print $2,$3,$4}' | sort -u > fs.txt
echo "r=$r w=$w X=$X signcheck $(wc -l <sc.txt) fsearch $(wc -l <fs.txt) diff $(diff sc.txt fs.txt|wc -l)"
