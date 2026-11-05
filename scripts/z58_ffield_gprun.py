# Run a GP script through cypari2 (no gp binary on this host).  Usage: uv run --with cypari2 python scripts/z58_ffield_gprun.py file.gp
import sys, cypari2
pari = cypari2.Pari(); pari.allocatemem(400_000_000)
pari('read("%s")' % sys.argv[1])
