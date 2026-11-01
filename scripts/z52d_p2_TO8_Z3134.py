# z52d P2 TO8 Z3134: exception sets E(a,b,c,d)={n<=NN : n != a t u v - b u - c v + d for all t,u,v>=3}
# Solve for v: value = (a t u - c) v - b u + d  (v>=3). Enumerate t,u with 3(atu-c)-bu+d <= NN.
import sys
NN = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
def exc(a, b, c, d):
    S = set()
    t = 3
    while True:
        any_u = False
        u = 3
        while True:
            base = a * t * u - c
            if 3 * base - b * u + d > NN: break
            any_u = True
            v = 3
            while True:
                val = base * v - b * u + d
                if val > NN: break
                if val >= 1: S.add(val)
                v += 1
            u += 1
        if not any_u and 3 * (a * t * 3 - c) - 3 * b + d > NN: break
        t += 1
    E = [n for n in range(1, NN + 1) if n not in S]
    return E
for abcd in [(1,1,1,0),(1,1,1,1),(1,1,1,-1),(1,2,1,0),(1,1,2,0),(2,1,1,0),(1,2,2,0),(1,1,3,0)]:
    E = exc(*abcd)
    print("Z3134", abcd, f"exceptions n<={NN}: {len(E)}; largest 6: {E[-6:]}; density in last third: {sum(1 for x in E if x>NN*2//3)/(NN//3):.4f}")
