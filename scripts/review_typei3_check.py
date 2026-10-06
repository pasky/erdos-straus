"""R72: convert review_typei3_fs output lines to (c,k,F), verify each against the definition
(POINTWISE_TYPEI2 (2.2)) with exact integers, optionally filter by ck <= H.
Usage: review_typei3_check.py r w [H] < fs_output     prints sorted unique "c k F"; exit 1 on any invalid."""
import sys, re


def val(p, n):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def is_cert(r, w, c, k, F):
    if val(r, c) % 2 == 0:
        return False
    N = 1 + 4 * c * k * k
    h = 4 * c * k
    t = val(2, h)
    vr = val(r, c * k)
    mp = (h >> t) // r ** vr
    return N % F == 0 and (F + 1) % mp == 0 and (F - 1) % r ** vr == 0 and (F + w) % 2 ** t == 0


def main():
    r, w = int(sys.argv[1]), int(sys.argv[2])
    H = int(sys.argv[3]) if len(sys.argv) > 3 else None
    out, bad = set(), 0
    for line in sys.stdin:
        if not line.startswith('C '):
            continue
        d = dict(kv.split('=') for kv in line.split()[1:])
        al, a, c1, ga, b, k1, f, t = (int(d[x]) for x in ('al', 'a', 'c1', 'ga', 'b', 'k1', 'f', 't'))
        c = 2 ** al * r ** a * c1
        k = 2 ** ga * r ** b * k1
        N = 1 + 4 * c * k * k
        assert N % f == 0
        F = f if d['role'] == 'F' else N // f
        assert val(2, 4 * c * k) == t
        if not is_cert(r, w, c, k, F):
            bad += 1
            print('INVALID', c, k, F, file=sys.stderr)
        if H is None or c * k <= H:
            out.add((c, k, F))
    for x in sorted(out):
        print(*x)
    print(f'checked: {len(out)} distinct, invalid {bad}', file=sys.stderr)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
