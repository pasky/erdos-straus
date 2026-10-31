#!/bin/bash
# z52c RESIDUE_HARDNESS: all tuple-count windows of z52c_rh_types.c, 20-way a-striding in parallel, partial sums added.
# Output /tmp/rh/<prefix>_{TI,TIw,TII,TIIw,RS[,TIwq,TIIwq]}.f32 (binary float32, index v - lo; not committed).
set -euo pipefail
mkdir -p /tmp/rh/parts
gcc -O2 -o /tmp/rh/types scripts/z52c_rh_types.c
ulimit -v 8000000
K=20
run() { # lo hi prefix q0
  local lo=$1 hi=$2 pre=$3 q0=$4 pids=()
  for j in $(seq 0 $((K-1))); do
    timeout 10000 /tmp/rh/types $lo $hi /tmp/rh/parts/${pre}_$j $q0 $K $j & pids+=($!)
  done
  for p in "${pids[@]}"; do wait $p; done
  uv run --with numpy python -c "
import numpy as np, glob
for k in ['TI','TIw','TII','TIIw','RS'] + (['TIwq','TIIwq'] if $q0 else []):
    fs = sorted(glob.glob('/tmp/rh/parts/${pre}_*_'+k+'.f32')); assert len(fs) == $K, (k, len(fs))
    s = sum(np.fromfile(f, np.float32).astype(np.float64) for f in fs)
    s.astype(np.float32).tofile('/tmp/rh/${pre}_'+k+'.f32')
print('${pre} done')"
  rm -f /tmp/rh/parts/${pre}_*
}
run 101 200000 t2e5full 0
run 200001 1000000 t1e6 0
run 1000001 2000000 t2e6 0
run 1000001 2000000 q7e6 7
run 5000001 10000000 t1e7 0
