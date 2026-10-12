"""O155: Maynard-with-theta experiment on the (A)3 slice R(p) = #{(A,B): 4AB | p+A+B}.

At fixed p, theta = A.  Event s_A = #{B | p+A : 4AB | p+A+B}.
Reports per dyadic block of A: #winners, and the 'Maynard weight' test:
restrict A to the progression A = -p (mod M) (so M | p+A, more divisors) and compare
the success rate there with the base rate (gain) against the measure cost 1/M.
Usage: PYTHONPATH=scripts uv run python scripts/bs_tech_maynard_theta.py
"""
import sys
from sympy import divisors, isprime, nextprime

def s_A(p, A):
    n = p + A
    return sum(1 for B in divisors(n) if (n + B) % (4 * A * B) == 0)

def run(p, logX, M):
    blocks = []
    tot = cnt_w = win_w = 0
    for k in range(logX):
        lo, hi = 2 ** k, 2 ** (k + 1)
        w = sum(s_A(p, A) for A in range(lo, hi))
        blocks.append(w)
    # weighted subfamily over the whole range
    base_hits = sum(1 for b in blocks for _ in range(b))
    for A in range(1, 2 ** logX):
        if (p + A) % M == 0:
            cnt_w += 1
            win_w += s_A(p, A)
    return blocks, cnt_w, win_w

if __name__ == "__main__":
    logX = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    M = 3 * 5 * 7 * 11
    ps, q = [], 10 ** 9
    while len(ps) < 6:
        q = nextprime(q)
        if q % 24 == 1:
            ps.append(q)
    print(f"A < 2^{logX}; Maynard-weight modulus M={M}")
    for p in ps:
        blocks, cw, ww = run(p, logX, M)
        tot = sum(blocks)
        print(f"p={p} p%840={p%840} R_X={tot} blocks={blocks}")
        print(f"   weighted: #A={cw} wins={ww}  rate_w={ww/cw:.4f}  base_rate={tot/(2**logX-1):.5f}"
              f"  gain={(ww/cw)/(tot/(2**logX-1)) if tot else float('nan'):.1f}  mass_w={ww} vs mass={tot}")

def weighted_test(p, logX, M):
    """Mass of the congruence-weighted subfamily A = -p (mod M), A < 2^logX, vs fair share (total mass)/M."""
    A0 = (-p) % M or M
    wins = sum(s_A(p, A) for A in range(A0, 2 ** logX, M))
    return wins
