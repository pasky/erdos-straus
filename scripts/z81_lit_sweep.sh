#!/bin/sh
# z81 LIT: run all arXiv API sweeps (sequential, polite). Outputs in data/z81/lit/.
cd "$(dirname "$0")/../data/z81/lit" || exit 1
S="uv run --no-project python ../../../scripts/z81_lit_arxiv.py"
CATS='(cat:math.NT OR cat:math.AG OR cat:math.CO OR cat:math.DS OR cat:math.GR OR cat:math.LO OR cat:cs.CC OR cat:cs.LO)'
$S lo.tsv 20261110 20261122 'cat:math.LO'
run() { $S "kw_$1.tsv" 20261101 20261122 "$CATS AND ($2)"; sleep 3; }
run egypt 'all:"Erdos-Straus" OR all:"Erdős-Straus" OR all:"Erdos Straus" OR all:"Egyptian fraction" OR all:"Egyptian fractions" OR all:"unit fraction" OR all:"unit fractions" OR all:Sierpinski OR all:Schinzel'
run divisors 'all:"divisors in residue classes" OR all:"divisors in arithmetic progressions" OR all:"moving moduli" OR all:"shifted primes" OR all:"Kloosterman fractions" OR abs:"divisors in arithmetic progression"'
run sieve 'abs:"half-dimensional sieve" OR abs:"semi-linear sieve" OR abs:"primes represented by" OR (abs:sieve AND abs:"quadratic form") OR abs:"binary quadratic form"'
run geom 'abs:"Brauer-Manin" OR abs:"Brauer–Manin" OR abs:"integral points" OR abs:"cubic surface" OR abs:Markoff OR abs:Vieta OR abs:"strong approximation"'
run comb 'abs:"sum-product" OR abs:"subset products" OR abs:"subset product" OR abs:"Davenport constant" OR (abs:pointwise AND abs:expansion) OR abs:"covering radius" OR abs:"inhomogeneous minimum"'
run logic 'abs:"weak arithmetic" OR abs:"open induction" OR abs:"bounded arithmetic" OR abs:"IOpen" OR abs:"IDelta_0" OR abs:"bounded existential" OR abs:"Shepherdson"'
run erdos 'abs:"Erdos problem" OR abs:"Erdős problem" OR abs:"Erdos problems" OR abs:"Erdős problems" OR abs:"erdosproblems"'
run kloost 'abs:Kloosterman OR abs:"Bombieri-Vinogradov" OR abs:"level of distribution" OR abs:"smooth moduli" OR abs:"norm form" OR abs:"norm forms"'
