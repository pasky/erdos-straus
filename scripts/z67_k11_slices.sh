#!/bin/bash
# z67 K11: batch replay of the rational-slice coverings of Z67_K11.md §3 (writes one certificate file per slice).
# Each certificate lists family parameters and the class "m r"; survivors 0 = CERTIFIED finite covering.
set -e
ulimit -v 4000000
D=data/z67/k11/slice_certs
for q in 2 6 7 8 10 1/2 1/6 2/3 3/2 -1 -3 -4 -5 -9 1/7 5/2 2/5 18 24 3/7 10/3; do
  f=$D/T7_q$(echo $q | tr '/' '_').txt
  timeout 900 uv run --with sympy --with numpy python scripts/z67_k11_tbox.py 100000 $q 6 3 2 2 --cert $f | sed -n 2p | sed "s|^|q=$q T={2,3,5,7}: |"
done
for q in 4 9 2 3 -1; do
  f=$D/T13_q$(echo $q | tr '/' '_').txt
  timeout 900 uv run --with sympy --with numpy python scripts/z67_k11_tbox.py 100000 $q 4 2 1 1 2 2 --cert $f | sed -n 2p | sed "s|^|q=$q T={2..13}: |"
done
