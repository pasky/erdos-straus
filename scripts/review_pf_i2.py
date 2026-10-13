"""R165: check the I2 composition identity (p + 2c√-d)(1 + 2cdt + pt√-d) = p + (2c + tN)√-d, N = p^2 + 4c^2 d,
and whether c' = c + tN/2 is an integer (needs t even since N is odd for odd p)."""
bad = odd_t_nonint = 0
for p in (5, 13, 101):
    for c in range(1, 8):
        for d in range(1, 8):
            N = p * p + 4 * c * c * d
            for t in range(1, 6):
                a1, b1, a2, b2 = p, 2 * c, 1 + 2 * c * d * t, p * t      # x + y√-d
                re, im = a1 * a2 - d * b1 * b2, a1 * b2 + b1 * a2
                if re != p or im != 2 * c + t * N: bad += 1
                Np = re * re + d * im * im
                if Np % N: bad += 1
                if im % 2: odd_t_nonint += 1; assert t % 2 == 1
print("identity/divisibility failures:", bad, "; cases with c' non-integer (all odd t):", odd_t_nonint)
