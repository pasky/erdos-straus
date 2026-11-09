#!/bin/bash
# z67 K11: batch replay of the rational-slice coverings of Z67_K11.md §3 (writes one certificate file per slice).
# Each certificate lists family parameters and the class "m r".  The run fails (non-zero exit) unless every slice is
# covered (0 survivors) and a fresh certificate was written.
set -euo pipefail
ulimit -v 4000000
D=data/z67/k11/slice_certs
run() {  # q, label, exponents...
  local q=$1 lab=$2; shift 2
  local f=$D/${lab}_q$(echo $q | tr '/' '_').txt
  rm -f "$f"
  local out
  out=$(timeout 900 uv run --with sympy --with numpy python scripts/z67_k11_tbox.py 100000 $q "$@" --cert "$f")
  echo "$out" | sed -n 2p | sed "s|^|q=$q $lab: |"
  echo "$out" | sed -n 2p | grep -q ": 0/" || { echo "FAIL: q=$q $lab not covered" >&2; exit 1; }
  [ -s "$f" ] || { echo "FAIL: no certificate for q=$q $lab" >&2; exit 1; }
}
for q in 2 6 7 8 10 1/2 1/6 2/3 3/2 -1 -3 -4 -5 -9 1/7 5/2 2/5 18 24 3/7 10/3; do run $q T7 6 3 2 2; done
for q in 4 9 2 3 -1; do run $q T13 4 2 1 1 2 2; done
