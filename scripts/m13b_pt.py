"""print u11 u13 (mod 11^16, 13^16) for rationals given as 'p/q' strings. usage: m13b_pt.py u11 u13"""
import sys
from fractions import Fraction as Fr
def red(s, m):
    f = Fr(s); return f.numerator * pow(f.denominator, -1, m) % m
print(red(sys.argv[1], 11 ** 16), red(sys.argv[2], 13 ** 16))
