# run s6_expclass.solve on the (J)62 residual exponents s = 124 (mod 360), 844 (mod 2520)
import sys; sys.argv=['x','105','0','0','9','45','2000']
exec(open('s6_expclass.py').read().split('un=[]; sig={}')[0])
for s in sorted(set(list(range(124,3000,360))+list(range(844,8000,2520)))):
    print(s, solve(s), flush=True)
