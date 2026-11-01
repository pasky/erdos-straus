#!/bin/bash
# exact Type I / Type II counts (bs_corr_count.c) for p ≡ 1 mod 24, p ≤ 1e6; 3 workers, 4 GB each
# usage: z52d_p2_TO2_fIfII.sh primesfile outfile
set -e
cd "$(dirname "$0")/.."
gcc -O2 -o /tmp/bscount scripts/bs_corr_count.c
cat "$1" | xargs -P 3 -I{} sh -c 'echo {} | (ulimit -v 4000000; timeout 600 /tmp/bscount)' > "$2"
