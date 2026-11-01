#!/bin/bash
# Z0685 extension: U(p) (repo count program, z52b_fingerprint_count.c) for primes p≡1 (mod 840), 1e6<p<=1e7; 4 workers, 4 GB each
cd "$(dirname "$0")/.."
gcc -O2 -o /tmp/fpcount scripts/z52b_fingerprint_count.c -lm
cat "$1" | xargs -P 4 -I{} sh -c '(ulimit -v 4000000; timeout 600 /tmp/fpcount 4 {} {} 1)' > "$2"
