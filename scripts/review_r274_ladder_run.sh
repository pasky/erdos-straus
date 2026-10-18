#!/bin/bash
# R274: from-scratch ladder counts to X for m given as args; keeps only prime-indexed counts.
X=${X:-100000000}
cd /tmp/r274
for m in "$@"; do
  ( ulimit -v 8000000; timeout 3000 ./lad $m $X full_$m.bin ) || { echo "m=$m FAILED"; continue; }
  timeout 600 uv run --project /tmp --no-project --with numpy python - <<PY
import numpy as np
P = np.load('/tmp/r274/primes_1e8.npy')
c = np.fromfile('/tmp/r274/full_$m.bin', dtype=np.uint32)
np.save('/tmp/r274/f$m.npy', c[P])
PY
  rm -f full_$m.bin; echo "m=$m done $(date +%T)"
done
