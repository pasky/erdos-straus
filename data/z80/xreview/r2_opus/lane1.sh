ulimit -v 6000000
B=data/z80/xreview/r2_opus/ogs.bin
for r in "125000000000 1100000000000" "2100000000000 3100000000000" "4100000000000 5000000000000"; do
  set -- $r; ( time timeout 1800 $B $1 $2 107 2000000 ) > data/z80/xreview/r2_opus/ogs_$1_$2.txt 2>&1
done
