#!/bin/sh
# O156: re-run O152(a)'s GF(2) windmill-signature test restricted to rows n = 1 (mod 24) only
# (an identity (W) need only hold on a congruence-defined family). Input: O152's all-n solution dump.
set -e
mkdir -p /tmp/o156
awk '$1%24==1' /tmp/bsinv/sol20k_1mod4.txt > /tmp/o156/sol20k_1mod24.txt   # from bs_invol_enum 5 20000 4 1
ulimit -v 8000000
for M in 24 120 168; do
  PYTHONPATH=scripts timeout 900 uv run python scripts/bs_invol_signature2.py /tmp/o156/sol20k_1mod24.txt 20000 $M | grep -A1 ALL-n
done
