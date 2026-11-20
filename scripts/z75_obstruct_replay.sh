#!/bin/bash
# Run serially from repository root. Binaries only live in the allowed data dir.
set -euo pipefail
ulimit -v 6000000
D=data/z75/obstruct
mkdir -p "$D"
trap 'rm -f "$D/ap.replay.bin" "$D/pan.replay.bin" "$D/z58.replay.bin"' EXIT
gcc -Wall -O3 scripts/z75_obstruct.c -lm -o "$D/ap.replay.bin"
gcc -O3 scripts/z75_obstruct_panels.c -o "$D/pan.replay.bin"
ap(){ timeout 1800 "$D/ap.replay.bin" "$@"; }
py(){ timeout 1800 uv run --offline --no-project python "$@"; }
ap 840 27740000 5000000 800000 | cmp - "$D/train.txt"
awk '$1=="W" {s=$3" "$4" "$5} $1=="EX"&&$3==1 {print s}' "$D/train.txt" | cmp - "$D/kill.txt"
ap 840 32740000 45000000 1500000 "$D/kill.txt" | cmp - "$D/adapt.txt"
ap 120 194140000 140000000 1500000 "$D/kill.txt" | cmp - "$D/adapt120.txt"
ap 840 119047620 130000000 2000000 "$D/kill.txt" | cmp - "$D/high.txt"
ap 19320 15528000 35000000 2000000 "$D/kill.txt" | cmp - "$D/record23.txt"
ap 120120 2500000 5800000 2000000 "$D/kill.txt" | cmp - "$D/deepap.txt"
ap 598920 1669700 4500000 2000000 "$D/kill.txt" | cmp - "$D/step31.txt"
ap 19320 51760000 100000000 2000000 "$D/kill.txt" | cmp - "$D/trillion.txt"
for pair in 'train:check1' 'adapt120:check120' 'high:checkhigh' 'record23:check23'; do
    log=${pair%:*}; ref=${pair#*:}
    py scripts/z75_obstruct_check.py $(awk '$1=="EX"&&$3==0 {print $2}' "$D/$log.txt") | cmp - "$D/$ref.txt"
done
gcc -O3 scripts/z58_disproof_eng.c -lm -o "$D/z58.replay.bin"
awk '$3==4&&$2=="prime" {print $1}' "$D"/check{120,high,23}.txt | EXACT=1 timeout 1800 "$D/z58.replay.bin" list | cmp - "$D/thirdcheck.txt"
timeout 1800 "$D/pan.replay.bin" | cmp - "$D/panels.txt"
py scripts/z75_obstruct_verify_panels.py | cmp - "$D/panelcheck.txt"
py scripts/z75_obstruct_controls.py | cmp - "$D/controls.txt"
