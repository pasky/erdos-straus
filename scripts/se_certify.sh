#!/bin/bash
# O219 replay of Theorem 3.4 (STERILE_EXPLICIT.md §3.4). Regenerates all certified tables and runs the combiner.
# ~3.5 h on 2 cores. Memory-bounded. Writes data/se/{P_q4,P_q1,Q_q4}.txt, MANIFEST.txt, r0_certify.txt.
set -euo pipefail
cd "$(dirname "$0")/.."
ulimit -v 8000000
gcc -O2 -o /tmp/se_box_cert scripts/se_box.c -lm
{ echo "date: $(date -u)"; gcc --version | head -1; uname -m; sha256sum scripts/se_box.c scripts/se_tail.py scripts/se_r0.py; } > data/se/MANIFEST.txt
( /tmp/se_box_cert P 124 799 4 1 64 24 > data/se/P_q4.txt ) &
( /tmp/se_box_cert Q 124 399 4 1 64 24 > data/se/Q_q4.txt && /tmp/se_box_cert P 200 599 1 1 64 24 > data/se/P_q1.txt ) &
wait
echo "commands: se_box P 124 799 4 1 64 24; se_box Q 124 399 4 1 64 24; se_box P 200 599 1 1 64 24" >> data/se/MANIFEST.txt
python3 scripts/se_r0.py 32 600 | tee data/se/r0_certify.txt
