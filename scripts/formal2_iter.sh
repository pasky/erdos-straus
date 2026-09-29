#!/bin/bash
# usage: iter.sh i   (uses /tmp/fcl/L$i.json, produces A$i, X$i, B$i, L$((i+1)))
set -e
i=$1; j=$((i+1))
cd /home/pasky/projects/math/erdos-straus-claude/scripts
ulimit -v 80000000
R="timeout 20000 uv run --with python-flint python"
$R formal2.py --lam-file /tmp/fcl/L$i.json --jobs 14 --dump /tmp/fcl/A$i.json.gz > /tmp/fcl/A$i.log
tail -2 /tmp/fcl/A$i.log
$R formal2_iter.py explicit /tmp/fcl/A$i.json.gz /tmp/fcl/X$i.txt
$R formal2.py --lam-file /tmp/fcl/L$i.json --jobs 14 --explicit /tmp/fcl/X$i.txt --dump /tmp/fcl/B$i.json.gz > /tmp/fcl/B$i.log
tail -2 /tmp/fcl/B$i.log
$R formal2_iter.py analyze /tmp/fcl/B$i.json.gz /tmp/fcl/L$i.json /tmp/fcl/L$j.json | tee /tmp/fcl/an$i.txt
