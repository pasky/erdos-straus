#!/usr/bin/env bash
# From repo root. Run a selected stage; no census command longer than 1600s.
set -euo pipefail
ulimit -v 2000000
s=$1; Z=data/z78
P(){ timeout 1600 uv run --offline --no-project python -B "$@"; }
B(){ timeout 40 gcc -O3 "scripts/z78_$1.c" -o "$Z/replay.bin"; }
C(){ timeout 1600 "$Z/replay.bin" "$@"; }
trap 'rm -f "$Z/replay.bin"' EXIT
case "$s" in
p3|p5) [[ $s == p3 ]] && B p3_exact || B p5
 for a in $(seq 17 1000 7017);do b=$((a+999)); ((b<=7213)) || b=7213
 args=(); if [[ $s == p5 ]];then j=2; ((a>3017)) || j=3;args=("$j");fi
 C "$a" "$b" "${args[@]}" | diff - "$Z/$s/$a.txt";done;;
q3) B q3;for a in $(seq 17 1000 4017) 5001;do b=$((a+999)); ((a!=4017))||b=5000;((a!=5001))||b=5520;C "$a" "$b" 2|diff - "$Z/q3/$a.txt";done
 P scripts/z78_qcap.py 17 5000 2 | diff - "$Z/qcap.txt";P scripts/z78_qcap.py 5001 5520 2 | diff - "$Z/qcap_ext.txt";;
qrows|qscan) B "$s";for a in 17 517 1017 1517;do b=$((a+499)); if [[ $s == qrows ]];then C "$a" "$b"|diff - "$Z/qrows/$a.txt";else C "$a" "$b"|diff - "$Z/qscan/scan$a.txt";P scripts/z78_qleft.py "$a" "$b"|diff - "$Z/qscan/left$a.txt";fi;done;;
p5fine|p7) B "$s"; for a in $(seq 500 100 1400);do j=5;if [[ $s == p7 ]];then j=29;((a<800))||j=30;((a<1100))||j=31;fi; C "$a" $((a+99)) "$j"|diff - "$Z/$s/$a.txt";done;;
layer) for a in $(seq 54 12 138);do P scripts/z78_layer.py $(seq "$a" $((a+11)))|diff - "$Z/layer/$a.txt";done;;
local) for k in 7 9;do P scripts/z78_local.py "$k" 3 953 983 1031 1033 1039 1051|diff - "$Z/local/L$k.txt";done;;
point) P scripts/z78_pointcheck.py|diff - "$Z/point/check.txt";for p in 1 5;do for m in Ha Hd J;do P scripts/z78_point.py 17 11 "$p" $((6-p)) "$m" 1 10000000|diff - "$Z/point/11_${p}_$m.txt";done;done;;
combine) P scripts/z78_deep.py|diff - "$Z/check.txt";;
*) echo 'choose p3 p5 q3 qrows qscan p5fine p7 layer local point combine' >&2;exit 2;;
esac
