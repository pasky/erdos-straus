#!/usr/bin/env bash
# Round-2 review: replay data/z78/r2exact/rows.tsv with the round-1 reviewer engine
# z78_xr_exact.c (independent of z78_r2exact.c) for primes lo..hi. One process.
set -euo pipefail
lo=$1; hi=$2; out=${3:-/dev/stdout}
gcc -O2 -o /tmp/z78r2rev/xr_exact scripts/z78_xr_exact.c
ulimit -v 2000000
for r in $(seq "$lo" "$hi"); do
  awk -v r="$r" 'BEGIN{for(i=2;i*i<=r;i++)if(r%i==0)exit 1}' || continue
  line=$(timeout 900 /tmp/z78r2rev/xr_exact "$r" | head -1)
  set -- $line
  mine="$r	$6	$8	${12}	${22}"
  ref=$(grep -P "^$r\t" data/z78/r2exact/rows.tsv)
  [ "$mine" = "$ref" ] && echo "$mine	SAME" || echo "$mine	DIFF ref=[$ref]"
done >> "$out"
