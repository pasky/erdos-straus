# ec_survey.py — for odd k <= kmax, find least L (from a list) admitting an ET exponent covering of k*b^m + c,
# and report square-obstruction survivors otherwise.  Usage: ec_survey.py b c kmax Mmax [Ls...]
import sys, functools
import mordell_lib as ML
import ec_cover as EC
from ec_screen import survivors, admissible_prime_powers, primes_upto
ML.residue_table = functools.lru_cache(maxsize=None)(ML.residue_table)
b, c, kmax, Mmax = map(int, sys.argv[1:5])
Ls = [int(x) for x in sys.argv[5:]] or [12, 24, 36, 48, 60, 72, 120, 144, 180, 240, 360]
P = primes_upto(200000)
import os
ONLY3 = os.environ.get("ONLY3") == "1"
PP = {L: admissible_prime_powers(b, L, PRIMES=P) for L in Ls}
for k in range(1, kmax + 1):
    if k % b == 0 or k % 2 == 0 or (ONLY3 and k % 3):
        continue
    found = None
    sv = None
    for L in Ls:
        sv = survivors(k, b, c, L, PP[L])
        if sv:
            continue
        ch = EC.search(k, L, Mmax, b, c, verbose=False)
        if ch:
            found = (L, len(ch))
            break
    print(k, 'COVER L=%d classes=%d' % found if found else 'none; square-survivors@%d=%s' % (Ls[-1], sv[:6]), flush=True)
