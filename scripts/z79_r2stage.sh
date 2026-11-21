#!/usr/bin/env bash
# Called by z79_replay.sh (from repo root); alternate stage standalone via the driver.
set -eu -o pipefail
ulimit -v 2000000
D=$1; stage=$2; R=data/z79/r2
C(){ timeout 60 gcc -O3 "scripts/$1.c" -o "$D/$2" "${@:3}"; }
P(){ timeout 1750 uv run --offline --no-project python -B "$@"; }
case $stage in
 r2flat) C z79_cheb cheb;for k in 9 11 13 15;do rs=$(awk -v k=$k '$1>=97&&$1<=239&&(k<15||$1<239){print $1}' data/z79/ledger.txt);timeout 1750 "$D/cheb" data/z78/r2/log16.txt $k 5 $rs |diff - "$R/layers/$k.txt";done;;
 r2runs) C z79_runs runs; P scripts/z79_runtables.py "$D/runs" 239 229 227 223 211 199 197 193 191 181 179 173 167 163 157 151 149 139 137 131 127 113 109 107 103 101 |diff - "$R/runs.txt";;
 r2high) C z79_high high -lgmp;for a in 117 137 157 177 197 217;do timeout 1750 "$D/high" data/z78/r2/log16.txt $a $((a+19));done|diff - "$R/high.txt";;
 r2shifts) C z78_r2shift shift;for r in 179 173 167 163 157 151 149 139 137 131; do for k in 9 11;do timeout 1750 "$D/shift" $r $r $k 32;done;done|diff - "$R/shift.txt"; C z79_shiftwide wide;for a in '157 13 32' '157 11 34' '139 13 32' '139 11 33' '131 13 32'; do set -- $a;timeout 1750 "$D/wide" $1 $1 $2 $3;done|diff - "$R/wide.txt"; C z78_r2q5shift q;for r in 131 137 139 149 151 157 163 167 173 179;do timeout 900 "$D/q" $r $r 2;done|diff - "$R/qs.txt"; P scripts/z79_qsplit.py "$R/qs.txt" |diff - "$R/qbound.txt";;
 r2ledger) P scripts/z79_r2budget.py |diff - "$R/ledger.txt"; awk '($1==137||$1>=149)&&$1<=283{if($9<=0)bad=1;n++}END{exit (bad||n!=28)}' "$R/ledger.txt";;
 r2point*) C z79_endpoint ep -lgmp;LV=${stage#r2point};for L in ${LV:-'12 13 14'};do bash scripts/z79_pointstage.sh "$D" "$L" |diff - "$R/point/$L.txt";done; P scripts/z79_r2check.py "$D/ep" |diff - "$R/point/check.txt";;
 *) exit 2;;
esac
