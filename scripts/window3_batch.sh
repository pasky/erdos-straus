#!/bin/bash
# usage: window3_batch.sh OUTFILE TIMEOUT "EPS K THETA ARGS..." ...   (sequential; append JSON lines)
out=$1; to=$2; shift 2
cd "$(dirname "$0")"
ulimit -v 8000000
for job in "$@"; do
  r=$(timeout $to uv run --with scipy python window3_lp2.py $job 2>>"$out.err" | tail -1)
  [ -z "$r" ] && r="{\"job\": \"$job\", \"status\": \"timeout_or_error\"}"
  echo "$r" >> "$out"
done
