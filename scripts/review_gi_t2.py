"""R170: brute-force T2(n) = #{(a,b,c,d): 4abcd = a+b+nc} at odd squares (doc §0 'Control')."""
def T2(n):
    cnt = 0
    d = 1
    while (4 * d - 1) ** 2 <= 4 * d * n + 1:
        a = 1
        while (4 * a * d - 1) * (4 * d - 1) <= 4 * d * n + 1:
            b = 1
            while (4 * a * d - 1) * (4 * b * d - 1) <= 4 * d * n + 1:
                D = 4 * a * b * d - n
                if D > 0 and (a + b) % D == 0:
                    cnt += 1
                b += 1
            a += 1
        d += 1
    return cnt

print("T2 at odd squares k<=45:", [T2(k * k) for k in range(1, 46, 2)])
print("T2 sanity (non-squares 5,7,13,17,73):", [T2(n) for n in (5, 7, 13, 17, 73)])
