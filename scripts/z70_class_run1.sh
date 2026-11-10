#!/bin/bash
# z70 CLASS item 1 — registered runs (Z70_CLASS.md §1.2).  Usage: bash scripts/z70_class_run1.sh CHAIN   (CHAIN = A | B | C | D)
# Each job: ulimit -v 6000000, timeout 1800; outputs data/z70/class/i1_<null>_d<d>_<tag>.txt
cd "$(dirname "$0")/.." || exit 1
ulimit -v 6000000
OUT=data/z70/class
job() {  # null d R seed tag spec...
  local null=$1 d=$2 R=$3 seed=$4 tag=$5; shift 5
  timeout 1800 uv run --with sympy --with numpy python scripts/z70_class_null.py "$null" "$d" "$R" "$seed" "$@" > "$OUT/i1_${null}_d${d}_${tag}.txt" 2>&1
  echo "done $null d=$d $tag rc=$?"
}
case "$1" in
A) job PSC 1 200 101 F1 range 24000 30000
   job PSC 1 200 102 F2 range 202000 206000
   job PSC 1 200 103 F3 range 1001000 1004000
   job PSC 1 200 104 F4 range 4000000 4003000 ;;
B) for d in 2 3 5 7; do
     job PSC $d 200 $((200+d)) F1 range 24000 30000
     job PSC $d 200 $((210+d)) F2 range 202000 210000
     job PSC $d 200 $((220+d)) F3 range 1001000 1005000
   done ;;
C) job PSC 1 200 301 z69w1 range 20000 24000
   job PSC 1 200 302 z69w2 range 200000 202000
   job PSC 1 200 303 z69w3 range 1000000 1001000
   job PSC 3 200 304 z69w1 range 20000 24000
   job PSC 5 200 305 z69w1 range 20000 24000
   # power check: plain prime swap without CS (positive controls must fire)
   job PS 1 200 306 F1 range 24000 30000
   job PS 3 200 307 F2 range 202000 210000 ;;
D) job PSC 1 200 401 hard list 409 577 5569 9601 23929 83449 102001 329617 712321 1134241 1724209 1726201 5212561 8813281 2521 3361 21841 76441 $(awk '!/^#/ && $1<1000000 {print $1}' data/z58/screens/gstar_zeros.txt)
   job PSC 3 200 403 hard list 409 577 5569 9601 23929 83449 2521 3361 21841 76441 $(awk '!/^#/ && $1<100000 {print $1}' data/z58/screens/gstar_zeros.txt) ;;
esac
# --- PSF (Z70_CLASS.md §1.4), chains E | F
case "$1" in
E) for w in "F1 24000 30000" "F2 202000 206000" "F3 1001000 1004000" "F4 4000000 4003000" "G1 500000 503000" "G2 2000000 2003000" "G3 8000000 8002000"; do
     set -- $w; timeout 1800 uv run --with sympy --with numpy python scripts/z70_class_psf.py 1 200 $((500+${2:0:2})) range $2 $3 > $OUT/i1_PSF_d1_$1.txt 2>&1; echo "done PSF d=1 $1 rc=$?"; done ;;
F) for w in "F1 24000 30000" "F2 202000 210000" "F3 1001000 1005000" "G1 500000 510000" "G2 2000000 2006000"; do
     set -- $w; timeout 1800 uv run --with sympy --with numpy python scripts/z70_class_psf.py 2 200 $((600+${2:0:2})) range $2 $3 > $OUT/i1_PSF_d2_$1.txt 2>&1; echo "done PSF d=2 $1 rc=$?"; done
   for w in "F1 24000 30000" "F2 202000 210000" "F3 1001000 1005000"; do
     set -- $w; timeout 1800 uv run --with sympy --with numpy python scripts/z70_class_psf.py 3 200 $((700+${2:0:2})) range $2 $3 > $OUT/i1_PSF_d3_$1.txt 2>&1; echo "done PSF d=3 $1 rc=$?"; done ;;
esac
