#!/bin/bash
set -euo pipefail
ulimit -v 6000000
D=data/z75/push2
T=$(mktemp -d "$D/replay.XXXXXX")
trap 'rm -f "$T/comp" "$T/verify" "$T/check"; rmdir "$T"' EXIT
gcc -O3 scripts/z75_push2_comp.c -lm -o "$T/comp"
gcc -O3 scripts/z75_push2_comp_verify.c -lm -o "$T/verify"
gcc -O3 scripts/z75_push2_checks.c -o "$T/check"
c(){ timeout 1800 "$T/comp" "$@"; }
py(){ timeout 500 uv run --offline --no-project python "$@"; }
c R 1 10000000001 20000000000 | cmp - "$D/ms105new.txt"
c R 1 20000000001 100000000000 | cmp - "$D/ms105decade.txt"
timeout 1800 "$T/verify" 10000000001 100000000000 | cmp - "$D/ms105verify.txt"
c 7 1 10000000001 20000000000 | cmp - "$D/u7all.txt"
timeout 1800 "$T/verify" 10000000001 20000000000 7 | cmp - "$D/u7verify.txt"
c 7 15 10000000001 20000000000 | cmp - "$D/u7new.txt"
c R 955049953 1000000000001 1000000000000000 | cmp - "$D/bigdead.txt"
{ for m in 2431 46189 1062347 30808063 955049953; do c R "$m" 10000000001 1000000000000; done; for m in 105 1155 15015 4545; do c 7 "$m" 10000000001 50000000000; done; } | cmp - "$D/composite.txt"
py scripts/z75_push2_height.py | cmp - "$D/height.txt"
py scripts/z75_push2_theory.py | cmp - "$D/theory.txt"
timeout 1800 "$T/check" | cmp - "$D/checks.txt"
