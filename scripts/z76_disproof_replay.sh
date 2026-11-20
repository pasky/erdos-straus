#!/usr/bin/env bash
# Run from root, sequential. No transient output outside the lane data path.
set -eu -o pipefail
ulimit -v 6000000
D=data/z76/disproof/comp
T=$(mktemp -d "$D/.replay.XXXXXX")
export TMPDIR="$PWD/$T" UV_CACHE_DIR="$PWD/$T/uv-cache" PYTHONDONTWRITEBYTECODE=1 LC_ALL=C
r(){ timeout 1800 "$@"; }
py(){ r uv run --offline --no-project python "$@"; }
r cc -O3 scripts/z75_push2_prime_ap.c -lm -o "$T/ap"
r cc -O3 scripts/z76_disproof_ap.c -lm -o "$T/cap"
r cc -O3 scripts/z75_push2_prime_factor.c -lm -o "$T/factor"
r cc -O3 scripts/z58_disproof_eng.c -lm -o "$T/z58"
r c++ -O3 scripts/z76_disproof_match.cpp -o "$T/panel"
r c++ -O3 scripts/z75_push2_prime_panels.cpp -o "$T/hp"
files=(ap11 r361 r121 r529 r169 r289)
r "$T/ap" 8 1320 1144764266 2200000000 40000 >"$T/ap11.txt"
for res in 361 121 529 169 289; do r "$T/cap" 840 "$res" 1511088831002 3100000000000 >"$T/r$res.txt"; done
r "$T/panel" <data/z75/push2prime/panels.txt >"$T/match.txt"
for domain in squares smooth; do
    r "$T/panel" "$domain" >"$T/$domain.txt"
    for mode in C R A; do
        awk -v m="$mode" '$1==m' "$T/$domain.txt" >"$T/list"
        r "$T/cap" check <"$T/list" >"$T/${domain}_${mode}.txt"
        files+=("${domain}_${mode}")
    done
done
# An R or Type A zero would require its OWN exact independent verifier.
for f in "$T"/{squares,smooth}_{R,A}.txt; do if grep '^MISS' "$f"; then exit 1; fi; done
logs=(); for name in "${files[@]}"; do logs+=("$T/$name.txt"); done
awk '$1=="MISS"{print $2}' "${logs[@]}" | sort -un >"$T/records.txt"
mapfile -t nums <"$T/records.txt"
r "$T/factor" "${nums[@]}" >"$T/factor.txt"
EXACT=1 r "$T/z58" list <"$T/records.txt" >"$T/z58.txt"
py scripts/z75_obstruct_check.py "${nums[@]}" >"$T/pycheck.txt"
awk '$1=="MISS" || $1=="H"{print $2}' "${logs[@]}" | sort -un >"$T/hardlist"
r "$T/hp" hard <"$T/hardlist" >"$T/hard.txt"
py scripts/z76_disproof_subsample.py "$T" >"$T/sublist"
mapfile -t sub <"$T/sublist"
r "$T/factor" "${sub[@]}" >"$T/subfactor.txt"
py scripts/z76_disproof_subsample.py "$T" summarize >"$T/subreport.txt"
py scripts/z76_disproof_report.py "$T" >"$T/report.txt"
for name in "${files[@]}" match squares smooth records factor pycheck z58 hard subfactor subreport report; do cmp "$T/$name.txt" "$D/$name.txt"; done
rm -r -- "$T" # solely the successful replay's private mktemp directory
echo 'Replayed.'
