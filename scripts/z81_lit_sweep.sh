#!/bin/sh
# z81 LIT: replay driver for every arXiv API query family used in notes/z81/LIT.md (Rounds 1-2).
# Usage: scripts/z81_lit_sweep.sh [OUTDIR]   (default data/z81/lit/replay; the committed TSVs in data/z81/lit/ are the
# original 2026-11-22 runs and are never overwritten). Each query's status (OK rows / FAILED) goes to OUTDIR/SWEEP_LOG.tsv.
# Exit status is non-zero if any query failed. Round-2 (a)-(c) subagent queries are documented in
# data/z81/lit/notes/R2a-R2c (with their own HTTP-429 failures) and are replayed here in the R2* block.
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${1:-$ROOT/data/z81/lit/replay}"
mkdir -p "$OUT"; cd "$OUT" || exit 1
LOG=SWEEP_LOG.tsv; : > "$LOG"; FAIL=0
run() { # name from to query
  if uv run --no-project python "$ROOT/scripts/z81_lit_arxiv.py" "$1.tsv" "$2" "$3" "$4" >/dev/null 2>"$1.err"; then
    printf '%s\t%s\t%s\tOK\t%s\t%s\n' "$1" "$2" "$3" "$(wc -l < "$1.tsv")" "$4" >> "$LOG"
  else
    printf '%s\t%s\t%s\tFAILED\t-\t%s\n' "$1" "$2" "$3" "$4" >> "$LOG"; FAIL=1
  fi
  sleep 4
}
CATS='(cat:math.NT OR cat:math.AG OR cat:math.CO OR cat:math.DS OR cat:math.GR OR cat:math.LO OR cat:cs.CC OR cat:cs.LO)'
# Round 1: complete category listings
run nt 20261110 20261122 'cat:math.NT'
run lo 20261110 20261122 'cat:math.LO'
# Round 1: keyword sweeps
run kw_egypt    20261101 20261122 "$CATS AND (all:\"Erdos-Straus\" OR all:\"Erdős-Straus\" OR all:\"Erdos Straus\" OR all:\"Egyptian fraction\" OR all:\"Egyptian fractions\" OR all:\"unit fraction\" OR all:\"unit fractions\" OR all:Sierpinski OR all:Schinzel)"
run kw_divisors 20261101 20261122 "$CATS AND (all:\"divisors in residue classes\" OR all:\"divisors in arithmetic progressions\" OR all:\"moving moduli\" OR all:\"shifted primes\" OR all:\"Kloosterman fractions\" OR abs:\"divisors in arithmetic progression\")"
run kw_sieve    20261101 20261122 "$CATS AND (abs:\"half-dimensional sieve\" OR abs:\"semi-linear sieve\" OR abs:\"primes represented by\" OR (abs:sieve AND abs:\"quadratic form\") OR abs:\"binary quadratic form\")"
run kw_geom     20261101 20261122 "$CATS AND (abs:\"Brauer-Manin\" OR abs:\"Brauer–Manin\" OR abs:\"integral points\" OR abs:\"cubic surface\" OR abs:Markoff OR abs:Vieta OR abs:\"strong approximation\")"
run kw_comb     20261101 20261122 "$CATS AND (abs:\"sum-product\" OR abs:\"subset products\" OR abs:\"subset product\" OR abs:\"Davenport constant\" OR (abs:pointwise AND abs:expansion) OR abs:\"covering radius\" OR abs:\"inhomogeneous minimum\")"
run kw_logic    20261101 20261122 "$CATS AND (abs:\"weak arithmetic\" OR abs:\"open induction\" OR abs:\"bounded arithmetic\" OR abs:\"IOpen\" OR abs:\"IDelta_0\" OR abs:\"bounded existential\" OR abs:\"Shepherdson\")"
run kw_erdos    20261101 20261122 "$CATS AND (abs:\"Erdos problem\" OR abs:\"Erdős problem\" OR abs:\"Erdos problems\" OR abs:\"Erdős problems\" OR abs:\"erdosproblems\")"
run kw_kloost   20261101 20261122 "$CATS AND (abs:Kloosterman OR abs:\"Bombieri-Vinogradov\" OR abs:\"level of distribution\" OR abs:\"smooth moduli\" OR abs:\"norm form\" OR abs:\"norm forms\")"
# Round 1: authors
run authors 20260915 20261122 'au:Dahan OR au:Bettin OR au:Chandee OR au:Radziwill OR au:Maynard OR au:Drappeau OR au:Pascadi OR au:Lichtman OR au:Sawhney OR au:Elsholtz OR au:Stange OR au:Rickards OR au:Trudgian OR au:Paredes OR au:Sasyk OR au:Kandukoori OR au:Trybushnyi OR au:Weingartner OR au:Pomerance OR au:Jerabek OR au:Boughattas OR au:Thorner OR au:Zaman OR au:Shparlinski OR au:Ford OR au:Koukoulopoulos OR au:Granville OR au:Soundararajan OR au:Heath_Brown OR au:Browning OR au:Wilsch OR au:Kingsbury_Neuschotz OR au:Bourgain OR au:Fouvry OR au:Kowalski OR au:Michel'
# Round 1: targeted (all years)
run tgt_sumsq   20100101 20261122 'cat:math.NT AND (abs:"sums of two squares" OR abs:"sum of two squares") AND (abs:"shifted primes" OR abs:"p+1" OR abs:"p-1" OR abs:"p+2" OR abs:"x^2+y^2+1" OR abs:Linnik OR abs:"half-dimensional")'
run tgt_halfdim 20100101 20261122 'abs:"half-dimensional sieve" OR abs:"semi-linear sieve" OR abs:"sieve of dimension 1/2"'
run tgt_fhrss   20250401 20261122 'abs:"shifted quadratic form" OR abs:"shifted quadratic forms" OR (abs:"Apollonian" AND abs:primes) OR abs:"Rickards"'
# Round 2 (d): weak arithmetic (author re-run, complete on 2026-11-22)
run r2d_kw 20240101 20261122 'abs:"open induction" OR abs:"bounded existential induction" OR abs:"discretely ordered ring" OR abs:"discretely ordered rings" OR abs:"integer part" OR abs:"integer parts" OR abs:"Shepherdson" OR abs:"bounded arithmetic" OR abs:"weak arithmetic" OR abs:"IDelta_0" OR abs:"Bezout domain"'
run r2d_au 20240101 20261122 'au:Jerabek OR au:Boughattas OR au:Thapen OR au:Kolodziejczyk OR au:D_Aquino OR au:Berarducci OR au:Otero OR au:Wilkie OR au:Macintyre OR au:Adamowicz OR au:Zdanowski OR au:Krajicek OR au:Pudlak OR au:Atserias OR au:Moniri OR au:Glivicky OR au:Pich OR au:Kaye OR au:Thamrongthanyalak'
# Round 2 (a)-(c): representative subagent queries (full list with outcomes in notes/R2a-R2c)
run r2a_twoprime 20240101 20261122 'abs:"products of two primes" AND abs:"residue class"'
run r2a_mclosed  20240101 20261122 'all:"multiplicatively closed sets" AND all:"primes"'
run r2b_generation 20250101 20261122 'all:"multiplicative subgroup generated by" OR all:"generation of multiplicative groups" OR all:"subset products"'
run r2c_rank     20240101 20261122 'abs:"8-rank" OR abs:"16-rank" OR abs:"4-rank"'
run r2c_governing 20240101 20261122 'abs:"governing field"'
cat "$LOG"
exit $FAIL
