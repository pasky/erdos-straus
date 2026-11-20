#!/usr/bin/env bash
# Run from repository root. No background/parallel compute or network needed.
set -eu -o pipefail
ulimit -v 6000000
export PYTHONDONTWRITEBYTECODE=1 LC_ALL=C
D=data/z75/push2prime
T=$(mktemp -d "$D/.replay.XXXXXX")
r() { timeout 1800 "$@"; }
ap() { local dst=$1; shift; r "$T/ap" "$@" >"$T/$dst.txt"; cmp "$T/$dst.txt" "$D/$dst.txt"; }
r cc -O3 scripts/z75_push2_prime_ap.c -lm -o "$T/ap"
r cc -O3 scripts/z75_push2_prime_factor.c -lm -o "$T/factor"
r cc -O3 scripts/z58_disproof_eng.c -lm -o "$T/z58"
r cc -O3 scripts/z75_push2_prime_modcheck.c -o "$T/modcheck"
r c++ -O3 scripts/z75_push2_prime_panels.cpp -o "$T/panel"
ap r8a 8 840 1190476191 280000000 40000
ap A   4 840 119047620 100000000 40000
ap r8b 8 120 8333333334 2400000000 40000
ap Ab  4 120 833333334 1000000000 40000
ap r8c 8 840 1470476191 2400000000 40000
ap Aall 4 24 4166666667 4166666667 12000
ap Rall 1 24 416666667 3750000000 12000
r "$T/modcheck" 1 100000000001 200000000000 >"$T/A2.txt"
r "$T/modcheck" 0 10000000001 100000000000 >"$T/R2.txt"
awk '$1=="MISS" {print $2}' "$T"/r8{a,b,c}.txt >"$T/records.txt"
mapfile -t records <"$T/records.txt"
r "$T/factor" "${records[@]}" >"$T/factor.txt"
EXACT=1 r "$T/z58" list <"$T/records.txt" >"$T/third.txt"
r uv run --offline --no-project python scripts/z75_obstruct_check.py "${records[@]}" >"$T/pycheck.txt"
r "$T/panel" >"$T/panels.txt"
awk '$1=="MISS"||$1=="H" {print $2}' "$T"/r8{a,b,c}.txt "$T"/{A,Ab,Aall,Rall}.txt >"$T/nums"
sort -un "$T/nums" >"$T/uniq"
r "$T/panel" hard <"$T/uniq" >"$T/hard.txt"
r uv run --offline --no-project python scripts/z75_push2_prime_report.py "$T" >"$T/report.txt"
for f in A2 R2 records factor third pycheck panels hard report; do cmp "$T/$f.txt" "$D/$f.txt"; done
rm -- "$T/"*.txt "$T/"{nums,uniq,ap,factor,z58,modcheck,panel}; rmdir -- "$T"
echo 'All checked.'
