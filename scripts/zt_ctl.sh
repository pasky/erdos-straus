#!/bin/bash
# zt_ctl.sh (O227): controls for zt_lop. Runs the complete lopsided search at every polynomial slice point u of
# degree 2..HMAX (u(0)=1, u'(0)!=0) over F_3, k = KK, levels 3..NMAX; prints the HIT and per-level summary lines prefixed by u.
# usage: zt_ctl.sh BINARY NMAX HMAX [KK]
BIN=$1; NMAX=$2; HMAX=$3; KK=${4:-2}
python3 -c "
import itertools
for h in range(2,$HMAX+1):
    for t in itertools.product(range(3),repeat=h):
        if t[0] and t[-1]: print(','.join(map(str,(1,)+t)))
" | while read u; do "$BIN" 3 $KK 3 $NMAX $u | awk -v u="$u" '/^(HIT|N=)/{print "u="u, $0}'; done
