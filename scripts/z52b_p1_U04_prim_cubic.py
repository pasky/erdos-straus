"""Z0866 follow-up: within p = 1 (mod 12), do primitive-failure primes (repo check up to 2e4) separate by cubic/quartic
characters of small primes? Reads data/z52b/pass1/U04/primitive_check_20000.json. Pure arithmetic, memory-trivial."""
import json, collections
r = json.load(open('data/z52b/pass1/U04/primitive_check_20000.json')); F = set(r['fails'])
def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
P = [p for p in range(13, 20001) if p % 12 == 1 and isprime(p)]
res = {}
for q in (2, 3, 5, 7):
    for k in (3, 4, 6):
        if (q, k) == (2, 4): pass
        c = collections.Counter()
        for p in P:
            if (p - 1) % k: continue
            key = pow(q, (p - 1) // k, p) == 1          # q is a k-th power residue
            c[(key, p in F)] += 1
        n_t = c[(True, False)] + c[(True, True)]; n_f = c[(False, False)] + c[(False, True)]
        res[f"{q}_is_{k}th_power"] = {"yes_fails": c[(True, True)], "yes_n": n_t,
                                      "no_fails": c[(False, True)], "no_n": n_f}
print(json.dumps(res, indent=1))
json.dump(res, open('data/z52b/pass1/U04/prim_cubic_split.json', 'w'), indent=1)
