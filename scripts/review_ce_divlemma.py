"""R199: brute-force check of the divisibility step in Cor 2.2 (iv)=>(i):
ab = 1 (mod t) and t^2 | (1+a)(1+b)  ==>  t | 1+a and t | 1+b.   (Only these two hypotheses are used.)"""
bad = 0
for t in range(1, 61):
    for a in range(1, 1500):
        for b in range(1, 1500):
            if (a * b - 1) % t == 0 and ((1 + a) * (1 + b)) % (t * t) == 0:
                if (1 + a) % t or (1 + b) % t:
                    bad += 1
                    print('counterexample', t, a, b)
print('t<=60, a,b<1500: counterexamples', bad)
