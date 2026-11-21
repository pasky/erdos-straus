#!/usr/bin/env bash
# Replay one stage or all (each subprocess capped; only owned scratch paths).
set -eu -o pipefail
ulimit -v 2000000
base=data/z79
D=$(mktemp -d "$base/replay.XXXXXX")
trap 'rm -r -- "$D"' EXIT
C(){ timeout 60 gcc -O3 "scripts/$1.c" -o "$D/$2"; }
P(){ timeout 1750 uv run --offline --no-project python -B "$@"; }
rs=$(awk '$1>=17 && $1<=283{print $1}' data/z78/r2/ledger.tsv)
for stage in ${1:-'p7 low q5 layer ledger'}; do
 case $stage in
 p7) C z78_r2p7exact se; C z78_r2exact dep; C z78_r2cf cf
 for r in $rs; do
  (( r>=223 )) || continue
  E=$((3*r*r*r)); timeout 1750 "$D/se" "$r" "$E" >"$D/s"
  timeout 1750 "$D/dep" "$r" --dump-prefix "$D/u" >/dev/null
  tail -n+2 "$D/u.L1.tsv" >"$D/digits"
  T=$(( (r**7/E+1)/2 )); timeout 1750 "$D/cf" "$r" 7 "$E" 1 "$T" "$D/digits" >"$D/l"
  echo "$r $((2*($(wc -l <"$D/s")+$(wc -l <"$D/l"))))" | diff - "$base/p7new/$r.txt"
 done;;
 low) C z78_r2p7exact se; C z78_r2cf cf; C z79_p9small p9; C z78_exact_enum enum
 P scripts/z79_low.py "$D" 17 19 23 29 31 37 41 43 47 53 | diff - "$base/low/rows.txt";;
 q5) C z78_r2q5shift q5
 while read -r r _; do timeout 1750 "$D/q5" "$r" "$r" 1; done <"$base/q5shift.txt" | diff - "$base/q5shift.txt";;
 layer) C z79_player pl
 for k in 7 9 11 13 15 17; do R=$rs; if ((k>=15)); then R=$(echo "$rs"|awk '$1<101'); fi
 timeout 1750 "$D/pl" data/z78/r2/log16.txt "$k" 7 $R | diff - "$base/layer/$k.txt"
 done;;
 ledger) P scripts/z79_pbudget.py |diff - "$base/ledger.txt"; awk '$1==233 || $1>=241{if($9<=0)exit 1;n++}END{if(n!=10)exit 1}' "$base/ledger.txt";;
 *) echo "unknown stage" >&2; exit 2;;
 esac
done
