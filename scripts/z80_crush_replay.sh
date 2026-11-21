#!/usr/bin/env bash
# Rebuild z80 stages from the inherited reviewed z78/z79 inputs.
set -euo pipefail
ulimit -v 6000000
B=data/z80/crush
D=$(mktemp -d data/z80/replay.XXXXXX); trap 'rm -r -- "$D"' EXIT
C(){ timeout 60 gcc -O3 scripts/"$1".c -o "$D/$2"; }
P(){ timeout 1750 uv run --offline --no-project python -B "$@"; }
run(){ timeout 1750 "$@"; }
rs='127 113 109 107 103 101 97 89 83 79 73 71 67 61 59 53 47 43 41 37 31 29 23 19 17'
if [[ ${1:-} == all ]]; then bash "$0"; exec bash scripts/z80_round2_replay.sh; fi
for stage in ${1:-prefix cf q shifts runs ledger}; do case $stage in
prefix) C z80_pshift ps; for r in 139 131 127 113 109 107 103 101 97 89; do run "$D/ps" "$r" 9 29; done | diff - "$B/prefix.txt";;
cf) C z78_r2cf cf; for r in 101 103 107 109 113 97 89; do sort -nu data/z78/exact/r${r}_{p1,q1}.txt > "$D/digit"; run "$D/cf" "$r" 9 536870912 1 9999999999 "$D/digit" > "$D/pairs"; echo "$r $((2*$(wc -l < "$D/pairs")))"; done | diff - "$B/cf.txt";;
q) C z78_r2q5shift qs; C z80_qboth qb; for r in 139 131 $rs; do run "$D/qs" "$r" "$r" 0; done | diff - "$B/qs.txt"; while read -r r k E T rest; do run "$D/qb" "$r" "$k" "$E" "$T"; done < "$B/qboth.txt" | diff - "$B/qboth.txt";;
shifts) C z79_shiftwide wide; for J in 28 31; do ks='9 11 13'; f=shift; if ((J==31)); then ks='11 13'; f=shift31; fi; for r in $rs; do for k in $ks; do run "$D/wide" "$r" "$r" "$k" "$J"; done; done | diff - "$B/$f.txt"; done;;
runs) C z79_runs runs; P scripts/z79_runtables.py "$D/runs" 97 89 83 79 73 71 67 61 59 53 47 43 41 37 31 29 23 19 17 | diff - "$B/runs.txt";;
ledger) P scripts/z79_r2budget.py | diff - data/z79/r2/ledger.txt; P scripts/z80_crush.py | diff - "$B/ledger.txt"; P scripts/z80_crush_checks.py; sha256sum -c "$B/SHA256SUMS";;
*) exit 2;; esac; done
