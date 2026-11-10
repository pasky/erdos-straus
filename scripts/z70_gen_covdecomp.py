# z70 GEN — GEN2 coverage decomposition (same-norm exclusivity).  usage: python3 scripts/z70_gen_covdecomp.py DIR (unpacked runs_W123)
import json, collections, math, sys
DIR = sys.argv[1] if len(sys.argv) > 1 else '/tmp/z70gen/raw'
for d in (1, 2, 7):
    recs = [json.loads(l) for f in ('W1', 'W2', 'W3') for l in open('%s/run_%s_d%d.jsonl' % (DIR, f, d))]
    tot = collections.Counter(); good = collections.Counter()
    for r in recs:
        for a, (u, g) in r['ahist'].items(): tot[int(a)] += u; good[int(a)] += g
    hk = collections.Counter(); ek = collections.Counter(); samenorm = 0; samenorm_both = 0; esame = 0.0
    for r in recs:
        if r['G'] == 0: continue
        sd = r['seeds']['GEN2']; probs = []; h = 0
        byal = collections.defaultdict(list)
        for al, w, hit, mn in sd:
            if al > 5000: continue
            u0, g0 = r['ahist'].get(str(al), [0, 0]); T_ = tot[al] - u0; G_ = good[al] - g0
            rho = G_ / T_ if T_ else 0; probs.append(rho); h += hit; byal[al].append((hit, rho))
        for al, l in byal.items():
            if len(l) >= 2:
                samenorm += 1; samenorm_both += sum(x for x, _ in l) >= 2
                # expected P(>=2 hits) under independence
                p0 = math.prod(1 - q for _, q in l); p1 = sum(q * math.prod(1 - q2 for j, (_, q2) in enumerate(l) if j != i) for i, (_, q) in enumerate(l))
                esame += 1 - p0 - p1
        hk[min(h, 3)] += 1
        # Poisson-binomial distribution of #hits
        dist = [1.0]
        for q in probs:
            nd = [0.0] * (len(dist) + 1)
            for k, v in enumerate(dist): nd[k] += v * (1 - q); nd[k + 1] += v * q
            dist = nd
        for k, v in enumerate(dist): ek[min(k, 3)] += v
    print('d=%d GEN2 #hit units per prime: obs %s  exp %s | same-alpha seed groups %d, with >=2 hits obs %d exp %.1f'
          % (d, dict(sorted(hk.items())), {k: round(v, 1) for k, v in sorted(ek.items())}, samenorm, samenorm_both, esame))
