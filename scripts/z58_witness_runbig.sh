#!/bin/bash
# z58 WITNESS: chunk i of 12 over (1e9, 1e10], least coordinate s = min(u_min, C_min) only (d- and pair-loops off).
# Fail-closed (cross-model review fix 2): pipefail propagates scan/timeout failure; the chunk is accepted only if the
# scan exits 0, there are zero NOS rows, and the processed count equals the independent prime count of the chunk
# (EXPECT_i below: the per-chunk prime counts, independently confirmed by the cross-model reviewer's separate progression sieve; total 202 099 784 = π(1e10;4,1) − π(1e9;4,1)).
# Usage: seq 0 11 | xargs -P 6 -I{} scripts/z58_witness_runbig.sh {}     (needs /tmp/z58scan built from z58_witness_scan.c)
set -o pipefail
i=$1; lo=$((1000000001 + i*750000000)); hi=$((1000000000 + (i+1)*750000000))
EXPECT=(17832659 17464604 17220133 17038210 16892161 16773156 16674577 16582433 16501228 16437157 16369802 16313664)
ulimit -v 6000000
DCAP=0 QCAP=0 timeout 1700 /tmp/z58scan $lo $hi | awk '!/^#/ {s=($8<$10)?$8:$10; L=log($1); if($8<0||$10<0) {print "NOS",$0; fflush(); next} r=s/(L*L); if(r>m){m=r; print "REC",r,$0; fflush()} if(s>=30) {print "BIG",s,$0; fflush()} n++} END{print "DONE",n,m}' > big_$i.txt 2> big_$i.err
st=$?
n=$(awk '$1=="DONE"{print $2}' big_$i.txt); nos=$(grep -c '^NOS' big_$i.txt)
if [ $st -ne 0 ] || [ "$nos" -ne 0 ] || [ "$n" != "${EXPECT[$i]}" ]; then
  echo "CHUNK $i [$lo,$hi] FAILED: status=$st NOS=$nos count=$n expected=${EXPECT[$i]}" >&2; exit 1
fi
echo "CHUNK $i [$lo,$hi] OK count=$n"
