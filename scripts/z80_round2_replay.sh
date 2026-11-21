#!/usr/bin/env bash
# Round 2; for complete z80 source replay start with bash scripts/z80_crush_replay.sh all.
set -euo pipefail
ulimit -v 6000000
D=$(mktemp -d data/z80/r2replay.XXXXXX); trap 'rm -r -- "$D"' EXIT
B=data/z80/crush2
P(){ timeout 1750 uv run --offline --no-project python -B "$@"; }
for stage in ${1:-layers local qwalk p15 p16};do case $stage in
layers) timeout 60 gcc -O3 scripts/z80_fullprefix.c -o "$D/p11";timeout 60 gcc -O3 scripts/z79_shiftwide.c -o "$D/shift";for r in 83 73 79 71 67 61 59;do for i in 0 1 2 3;do timeout 1700 "$D/p11" $r $i 32;done;done |diff - "$B/p11.txt";for j in 33 35;do rs='83 79 73 71 67 61 59';if ((j==35));then rs='79 71 67 61 59';fi;for r in $rs;do for k in 13 15;do timeout 1750 "$D/shift" $r $r $k $j;done;done |diff - "$B/shift$j.txt";done;;
local) timeout 60 gcc -O3 scripts/z80_pshift.c -o "$D/ps"; timeout 60 gcc -O3 scripts/z80_xr_cf.c -o "$D/cf";for r in 83 79 73 71 67 61 59;do timeout 500 "$D/ps" $r 9 29;done |diff - data/z80/xreview/xr_prefix_lo.txt
 for r in 83 79 73 71 67 61 59; do sort -nu data/z78/exact/r${r}_{p1,q1}.txt > "$D/digits"; timeout 1000 "$D/cf" $r 9 536870912 "$D/digits"; done |diff - data/z80/xreview/xr_cf_lo.txt
 P scripts/z80_budget2.py | diff - "$B/local.txt"; P scripts/z80_crush_checks.py;;
qwalk) P scripts/z80_qwalk.py 39 | diff - "$B/qwalk.txt";;
p15|p16) L=${stage#p};timeout 60 gcc -O3 scripts/z80_ep15.c -lgmp -o "$D/ep";timeout 60 gcc -O3 scripts/z80_epfast.c -lgmp -o "$D/fast";
 if ((L==15));then E=20000;J=50000000;V=20000;Y=1000000000;else E=12000;J=450000000;V=130000;Y=3500000000;fi
 P scripts/z80_ep_bounds.py "$L" "$E" "$J" "$V" "$Y"
 { for mode in e J HZ Hd;do for p in 1 5;do q=$((6-p));case $mode in
 J|Hd) C=$J; if [[ $mode == Hd ]]; then C=$Y;fi; timeout 1750 "$D/fast" "$L" "$p" "$mode" "$C";;
 e|HZ) C=$E;sz=500;if [[ $mode == HZ ]];then C=$V;sz=100000; fi; if [[ $mode != e || $p == 1 ]]; then
 timeout 60 "$D/ep" "$L" "$p" "$q" "$mode" "$C" 1 >"$D/keys";split -d -l "$sz" "$D/keys" "$D/piece"; : >"$D/fac";for f in "$D"/piece??;do timeout 1600 factor <"$f" >>"$D/fac";rm "$f";done; fi
 timeout 1200 "$D/ep" "$L" "$p" "$q" "$mode" "$C" 0 <"$D/fac";; esac;done;done; } |diff - "$B/p$L.txt";;
*)exit 2;;esac;done
sha256sum -c "$B/SHA256SUMS"
