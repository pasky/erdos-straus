#!/bin/bash
# z69 MINE — full reproduction driver (intermediates in /tmp/z69mine; every step memory/time bounded).
set -euo pipefail
T=/tmp/z69mine; D=data/z69/mine; mkdir -p $T
ulimit -v 6000000
PY="uv run --with numpy --with sympy --with scipy --with cypari2 python"
gcc -O2 -o $T/W scripts/z69_mine_W.c -lm
gcc -O2 -o $T/allwit scripts/z69_mine_allwit.c
gcc -O2 -o $T/scales scripts/z69_mine_scales.c -lm
gcc -O2 -o $T/tau scripts/z69_mine_tau.c
timeout 1700 $T/W 100000000 100000000 > $T/w1e8full.txt              # census (9 s, ~1 GB)
grep '^P ' $T/w1e8full.txt | awk '{print $2, $3, $4}' > $T/w1e8.tsv
# H / CTRL sets (deterministic seed) and their complete witness lists
timeout 900 $PY scripts/z69_mine_sets.py
timeout 1700 $T/allwit < $D/H.txt > $T/H.wit                        # allwit reads the first number of each line
timeout 1700 $T/allwit < $D/CTRL.txt > $T/C.wit
timeout 1700 $PY scripts/z69_mine_feat.py $D/H.txt $T/H.feat.jsonl
timeout 1700 $PY scripts/z69_mine_feat.py $D/CTRL.txt $T/C.feat.jsonl
# Q1
timeout 1700 $PY scripts/z69_mine_local.py 200 > $D/local_fit.txt
timeout 1700 $PY scripts/z69_mine_hvsE.py > $D/hvsE.txt
timeout 1700 $PY scripts/z69_mine_chi.py > $D/chi_fit.txt
timeout 900 $T/tau 10000000 > $T/tau1e7.txt
timeout 1700 $PY scripts/z69_mine_tau_an.py > $D/tau_fit.txt
timeout 1700 $T/scales 100000000 10000000 0 > $T/scales.txt
timeout 1700 $T/scales 100000000 10000000 1 > $T/types.txt
timeout 1700 $PY scripts/z69_mine_scales_an.py $T/scales.txt > $D/scales_corr.txt
timeout 1700 $PY scripts/z69_mine_scales_an.py $T/types.txt > $D/types_corr.txt
timeout 900 $PY scripts/z69_mine_morph.py > $D/morph.txt
timeout 900 $PY scripts/z69_mine_nprule.py > $D/nprule.txt
timeout 900 $PY scripts/z69_mine_redei.py > $D/redei.txt
timeout 1700 $PY scripts/z69_mine_lemma43_check.py | tail -1
# Q2 phantom tests (at most 2 concurrently in the lane); args: wit cap K seed out [mode] [--big]
timeout 1750 $PY scripts/z69_mine_phantom.py $T/C.wit 3 2 2 $T/ph3_C.jsonl same
timeout 1750 $PY scripts/z69_mine_phantom.py $T/H.wit 8 2 1 $T/ph3_H.jsonl same
timeout 1750 $PY scripts/z69_mine_phantom.py $T/C.wit 3 2 4 $T/phxz3_C.jsonl xz
timeout 1750 $PY scripts/z69_mine_phantom.py $T/H.wit 4 2 1 $T/phm3_H.jsonl match --big 10000000000
timeout 1750 $PY scripts/z69_mine_phantom.py $T/C.wit 2 2 3 $T/phm3_C.jsonl match --big 10000000000
python3 scripts/z69_mine_phantom_an.py $T/ph3_C.jsonl > $D/phantom_same_C.txt
python3 scripts/z69_mine_phantom_an.py $T/ph3_H.jsonl > $D/phantom_same_H.txt
python3 scripts/z69_mine_phantom_an.py $T/phxz3_C.jsonl > $D/phantom_xz_C.txt
python3 scripts/z69_mine_phantom_an.py $T/phm3_H.jsonl --big 1e10 --did $T/phm3_C.jsonl > $D/phantom_match_H_did.txt
python3 scripts/z69_mine_phantom_an.py $T/phm3_C.jsonl --big 1e10 > $D/phantom_match_C.txt
# unconditional size-neighbour shuffle (descriptive only)
timeout 1750 $PY scripts/z69_mine_scan.py $T/H.wit $T/H.feat.jsonl $T/C.wit $T/C.feat.jsonl $D/shuffle_scan.txt
