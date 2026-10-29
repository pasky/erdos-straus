#!/bin/bash
# batch of FF-U enumerations; output appended to data/z51_ffield/enum.txt
ulimit -v 8000000
gcc -O2 -o /tmp/z51enum scripts/z51_ffield_enum.c || exit 1
out=data/z51_ffield/enum.txt
for pn in "19 4" "23 4" "31 4" "43 4" "47 4" "59 4" "7 5" "11 5" "19 5" "23 5" "31 5" "7 6" "11 6" "19 6" "7 7" "11 7" "7 8" \
          "3 5" "3 6" "3 7" "3 8" "3 9" "3 10" "3 11" "3 12" "3 13" "3 14" "3 15"; do
  timeout 3000 /tmp/z51enum $pn >> $out
done
