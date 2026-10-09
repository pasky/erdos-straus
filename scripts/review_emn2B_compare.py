"""R102B: per-prime comparison of the author's scanner (/tmp/r102b/scan, compiled from
scripts/emn2_scan.c, count=2 mode prints exceptional primes) with the from-scratch brute force
review_emn2B_brute.representable.  Usage: review_emn2B_compare.py m1-m2 P1 P2 [extra_m,...]
Exit status 1 on any mismatch."""
import sys, subprocess
from review_emn2B_brute import representable, primes_in

lo, hi = map(int, sys.argv[1].split('-'))
P1, P2 = int(sys.argv[2]), int(sys.argv[3])
ms = list(range(lo, hi + 1)) + ([int(x) for x in sys.argv[4].split(',')] if len(sys.argv) > 4 else [])
ps = primes_in(P1, P2)
bad = 0; tot = 0; texc = 0
for m in ms:
    out = subprocess.run(['/tmp/r102b/scan', str(m), str(P1), str(P2), '2'], capture_output=True, text=True).stdout
    scan_exc = {int(l.split()[1]) for l in out.splitlines() if l.startswith('E ')}
    mine = {p for p in ps if m % p and not representable(m, p)}
    tot += sum(1 for p in ps if m % p); texc += len(mine)
    if mine != scan_exc:
        bad += 1
        print('MISMATCH m=%d only_brute=%s only_scan=%s' % (m, sorted(mine - scan_exc)[:10], sorted(scan_exc - mine)[:10]))
print('m-values %d, (m,p) pairs %d, exceptional pairs %d, mismatching m %d' % (len(ms), tot, texc, bad))
sys.exit(1 if bad else 0)
