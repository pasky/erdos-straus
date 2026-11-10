# z70 GEN — per-input summary of the falsifier screens (F2: R8 zeros, F4: hard list).  usage: python3 scripts/z70_gen_screens.py FILE...
import sys, json, collections
rows = collections.defaultdict(dict)
for f in sys.argv[1:]:
    for l in open(f):
        r = json.loads(l); rows[r['n']][r['d']] = r
tot = collections.Counter()
print('n  n%840 | per d: |G| ; hits AMB/RED/CYC/GEN2 (exp. alpha-null GEN2) ; item-3 first entry type (I = natural ideal, III = class level, - none)')
for n in sorted(rows):
    parts = []
    anyG = anyHit = 0
    for d in sorted(rows[n]):
        r = rows[n][d]
        if 'skipped' in r: parts.append('d%d: skipped' % d); continue
        f = r['fam']; i3 = r.get('it3', {})
        a, b = i3.get('firstI'), i3.get('firstIII')
        fe = '-' if (a is None and b is None) else ('I@%d' % a if (b is None or (a is not None and a < b)) else 'III@%d' % b)
        h = [f[k]['hit'] if k in f else 0 for k in ('AMB', 'RED', 'CYC', 'GEN2')]
        parts.append('d%d: %d ; %s ; %s' % (d, r['G'], '/'.join(map(str, h)), fe))
        anyG |= r['G'] > 0; anyHit |= sum(h) > 0
        tot['AMB'] += h[0]; tot['frv'] += i3.get('frviol', 0); tot['G0'] += (r['G'] == 0)
        tot['RED'] += h[1]; tot['CYC'] += h[2]; tot['GEN2'] += h[3]
    tot['inputs'] += 1; tot['anyG'] += anyG; tot['anyHit'] += anyHit
    print(n, n % 840, '|', ' || '.join(parts))
print('TOTAL', dict(tot))
