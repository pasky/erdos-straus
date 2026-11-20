#!/usr/bin/env bash
# Run from root, one stage at a time. Each constituent job is restartable.
set -euo pipefail
ulimit -v 2000000
R=data/z78/r2
P(){ timeout 1700 uv run --offline --no-project python -B "$@"; }
B(){ timeout 45 gcc -O3 "scripts/z78_r2$1.c" -o "$R/$2.bin"; }
case "$1" in
scale) B scale scale; for b in 148 180 240 320 512 800;do timeout 240 "$R/scale.bin" "$b" $((b*42/100)) 2 2;done|diff - "$R/scale.txt";;
q) for a in 20 30 40 50 60 70;do P scripts/z78_r2qfine.py $(seq "$a" $((a+9)))|diff - "$R/q/$a.txt";done
 P -c 'import sys;sys.path.insert(0,"scripts");from z78_r2qfine import qbound;[print(r,qbound(r**5,r),flush=True) for r in range(17,620) if all(r%i for i in range(2,__import__("math").isqrt(r)+1))]'|diff - "$R/qLocal/q5.txt";;
layer) B layers dyad;P scripts/z78_r2dyad.py $(seq 27 53) $(seq 150 195)|diff - "$R/layer/finite.txt";;
local) B local local;for f in "$R"/local/*.txt;do read -r r k j rest <"$f";timeout 900 "$R/local.bin" "$R/log16.txt" "$k" 4 $(cut -d' ' -f1 "$f")|diff - "$f";done;;
p7) B p7 p7;for a in 17 117 217 317 417 517 619;do hi=$((a+99));((a!=619))||hi=619;timeout 1200 "$R/p7.bin" "$a" "$hi" 3|diff - "$R/p7/$a.txt";done;;
p9) B shift shift;for f in "$R"/p9/*.txt;do lo=$(head -1 "$f"|cut -d' ' -f1);hi=$(tail -1 "$f"|cut -d' ' -f1);j=$(awk 'NR==1{print NF-3}' "$f");timeout 1600 "$R/shift.bin" "$lo" "$hi" 9 "$j"|diff - "$f";done;;
exact7) B cf cf;B p7exact exact7;B exact depth3;for f in "$R"/exact7/*.txt;do read -r r E raw h c <"$f";o=$(P scripts/z78_r2exact7.py "$r");test "$o" = "$r $E $raw $h $c";done;;
near) B highnear near;for l in 9 10 11;do for j in 2 3 4;do timeout 400 "$R/near.bin" "$l" "$j" $((10000000*17**j))|diff - "$R/near/P${l}j${j}.txt";done;done;P scripts/z78_r2neare.py 9 10 11;P scripts/z78_r2near.py;;
ledger) P scripts/z78_r2report.py|diff - "$R/summary.txt";;
*) echo 'choose scale q layer local p7 p9 exact7 near ledger' >&2;exit 2;;esac
