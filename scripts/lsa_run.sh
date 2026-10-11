#!/bin/sh
# O135 census runs (LONGSHOT_PIGEONHOLE §3). ~2-3 min, 1 core.
set -e
gcc -O2 -o /tmp/lsa_census scripts/lsa_census.c
ulimit -v 8000000
timeout 3000 /tmp/lsa_census 2000 < data/lsa/mh_le1e6.txt > data/lsa/cen_mh_le1e6_E2000.txt
for k in 4 5 6 7 8; do timeout 3000 /tmp/lsa_census 5000 < data/lsa/mh_sample_1e$k.txt > data/lsa/cen_sample_1e${k}_E5000.txt; done
timeout 3000 /tmp/lsa_census 20000 < data/lsa/hard.txt > data/lsa/cen_hard_E20000.txt
