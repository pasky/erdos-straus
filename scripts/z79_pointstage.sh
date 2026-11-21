#!/usr/bin/env bash
set -eu -o pipefail
ulimit -v 2000000
D=$1; L=$2
# Each bound is separately verified by z79_r2check.py. Files reused only within one stage.
case $L in 12) E=60000; J=1000000; HZ=1500; Hd=3000000;;
13) E=160000; J=3000000; HZ=11000; Hd=7400000;;
14) E=160000; J=8000000; HZ=70000; Hd=29000000;;
*) exit 1;;esac
for mode in e HZ Hd J; do
 C=$E; case $mode in HZ) C=$HZ;; Hd) C=$Hd;; J) C=$J;; esac
 for p in 1 5; do q=$((6-p)); args=($L $p $q $mode $C)
 if [[ $mode != Hd ]]; then
 if [[ $mode != e || $p == 1 ]]; then
 timeout 1750 "$D/ep" "${args[@]}" 1 > "$D/keys"
 if [[ $L == 14 && $mode == e ]]; then
   split -l 10000 "$D/keys" "$D/piece."; : >"$D/factors"
   for f in "$D"/piece.*; do timeout 1500 factor <"$f" >>"$D/factors"; rm "$f"; done
 else timeout 1750 factor <"$D/keys" >"$D/factors"; fi; fi
 timeout 1750 "$D/ep" "${args[@]}" 0 <"$D/factors"
 else timeout 1750 "$D/ep" "${args[@]}" 0 </dev/null; fi
 done
done
rm -f "$D/keys" "$D/factors"
