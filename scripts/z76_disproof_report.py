"""Check matched controls & late hits independently; no censoring as zeros."""
from collections import Counter, defaultdict
from math import isqrt
from pathlib import Path
import sys
from z75_push2_prime_report import isp, smooth, profile
from z75_obstruct_controls import full8

D = Path(sys.argv[1])
M = 32*27*25*49
FLOOR = 1511088831001
AP = ('ap11', 'r361', 'r121', 'r529', 'r169', 'r289')
CLASSES = (1, 121, 169, 289, 361, 529)


def words(n, fs, hard=False):
    for tag, f in zip('RAZSE', fs, strict=True):
        if hard and tag == 'E':
            assert f == 0  # not tested in this detector
            continue
        assert f > 0, (n, tag)
        u = (-n) % f
        if tag == 'A' and u == 1:
            u = f+1
        b, rz = divmod(n+u, f)
        t, sz = divmod(f+1, u)
        assert rz == sz == 0 and min(t,u,b)>0 and n == t*u*b-u-b
        assert {'R': t%4 == 0, 'A': u%4 == 0, 'Z': f%8 == 7,
                'S': min(t,u,b) >= 2 and (n+t)*u*b*t%8 == 0,
                'E': t%8 == 0}[tag]


def panels():
    # Independent finite list of positive R8 congruences through the endpoint.
    # Keep the individual (f,u), not just the modulus. Residue compatibility
    # for square shifts is a one-modulus test; different entries need not
    # admit a common root. A square anchor automatically passes this filter.
    shots = sorted((8*a*c-1, a) for a in range(1,126) for c in range(1,125//a+1))
    residues = {f:{i*i%f for i in range(f)} for f in set(f for f,a in shots)}
    compatible = {(f,a) for f,a in shots if (-a-1)%f in residues[f]}
    adjusted = defaultdict(dict)
    matched, drops = defaultdict(dict), Counter()
    distances = defaultdict(list)
    seen = set()
    for line in (D/'match.txt').read_text().splitlines():
        if line.startswith('# incomplete'):
            drops[line.split()[2]] += 1
        if line.startswith('#'):
            continue
        tag, *row = line.split()
        p,n,*fs = map(int,row)
        assert isp(n) and n%840 == 1 and n%M == p%M and n not in seen
        assert n//10**12 == p//10**12 and abs(p-n)*1000 <= p
        seen.add(n)
        if tag in ('sq','sq_ctl'):
            assert (tag=='sq') == (isqrt(n-1)**2 == n-1)
            assert smooth(n-1) == smooth(p-1) and isp(12*n+1) == isp(12*p+1)
        else:
            assert tag in ('sm+', 'sm-', 'rough+', 'rough-')
            assert isqrt(n-1)**2 != n-1 and smooth(n-1) == tag.startswith('sm')
            assert isp(12*n+1) == tag.endswith('+')
        words(n,fs)
        # Independent reconstruction of the binary primary outcome, not just
        # the cited positive witness. r may be recovered from 8*a*c-1=f.
        hits = [(f,a) for f,a in shots if (n+a)%f==0]
        assert (fs[-1] if fs[-1]<=1000 else None) == (hits[0][0] if hits else None)
        if tag in ('sq','sq_ctl'):
            adjusted[tag][p] = [not hits, not any(a!=1 for f,a in hits),
                                not any(h in compatible for h in hits)]
            if tag=='sq':assert all(h in compatible and h[1]!=1 for h in hits)
        assert p not in matched[tag]
        matched[tag][p] = fs
        distances[tag].append((abs(p-n),abs(p-n)*1e6/p))
    assert drops['quartet'] + len(matched['sm+']) == 2048
    assert drops['pair'] + len(matched['sq']) == 720
    print('M',M,'dropped',dict(sorted(drops.items())))
    print('arm rows max_abs_distance max_ppm f>1000:R,A,U7,S,R8 maxfR8')
    for tag,arm in matched.items():
        ds = distances[tag]
        print(tag,len(arm),max(d[0] for d in ds),round(max(d[1] for d in ds),3),
              *(sum(v[i]>1000 for v in arm.values()) for i in range(5)),max(v[4] for v in arm.values()))
    for t,u in [('sm+', 'rough+'),('sm-', 'rough-'),('sm+', 'sm-'),('rough+','rough-'),('sq','sq_ctl')]:
        assert matched[t].keys() == matched[u].keys()
        ds = [int(f[4]>1000)-int(matched[u][p][4]>1000) for p,f in matched[t].items()]
        print('discordant 10/01',t,u,ds.count(1),ds.count(-1))
    for i,lab in enumerate(('all','u!=1','compatible')):
        x,y=adjusted['sq'],adjusted['sq_ctl'];ds=[x[p][i]-y[p][i] for p in x]
        print('square diagnostic',lab,'sq / ctl',sum(v[i] for v in x.values()),
              sum(v[i] for v in y.values()),'discordant',ds.count(1),ds.count(-1))


def hunts():
    hard,zeros = set(),set()
    target_logs=[(d+'_'+t,d,t) for d in ('squares','smooth') for t in ('C','R','A')]
    for tag,domain,mode in ([(a,'ap','C') for a in AP]+target_logs):
        hs,ms=set(),set(); summary=None
        for line in (D/(tag+'.txt')).read_text().splitlines():
            ty,*row=line.split()
            if ty=='#':
                summary=dict(field.split('=') for field in row);continue
            n,*rest=map(int,row)
            assert n>FLOOR and isp(n) and n not in hs and n not in ms
            if tag=='ap11':assert n%1320==1
            elif domain=='squares':assert isqrt(n-1)**2==n-1 and n%840 in CLASSES
            elif domain=='smooth':assert smooth(n-1) and isqrt(n-1)**2!=n-1 and n%840==1
            else:assert n%840==int(tag[1:])
            if ty=='H':
                a,b,c=rest
                assert min(a,b,c)>0 and (8 if mode=='C' else 4)*a*b*c-(4 if mode=='A' else 1)*a-b==n
                hs.add(n)
            else:
                assert ty=='MISS' and not rest and mode=='C'
                ms.add(n)
        if summary:
            assert int(summary['miss'])==len(ms) and int(summary.get('hard',summary.get('hard_primes')))==len(hs|ms)
        if domain!='ap':
            caps={int(l.split()[1]) for l in (D/(domain+'.txt')).read_text().splitlines() if l.startswith(mode+' ')}
            assert hs|ms==caps
        hard.update(hs|ms);zeros.update(ms)
    hardrows=set(); maxima=[0]*4
    for line in (D/'hard.txt').read_text().splitlines()[1:]:
        tag,*v=line.split();p,n,*fs=map(int,v)
        assert tag=='hard' and p==n and n not in hardrows
        words(n,fs,True);hardrows.add(n)
        maxima=[max(a,b) for a,b in zip(maxima, fs[:4])]
    assert hard==hardrows
    print('hard unique, max f R A U7 S',len(hard),*maxima)
    assert zeros==set(map(int,(D/'records.txt').read_text().split()))
    z58 = [list(map(int,l.split())) for l in (D/'z58.txt').read_text().splitlines() if not l.startswith('#')]
    assert {x[0] for x in z58} == zeros and all(x[8]>0 and x[9]==0 for x in z58)
    factor = (D/'factor.txt').read_text().splitlines()
    assert sorted(factor) == sorted(f'{n} unordered R8 0' for n in zeros)
    py_counts = {}
    for line in (D/'pycheck.txt').read_text().splitlines():
        n,prime_label,k,unordered,num,first,*_ = line.split()
        assert (prime_label,unordered,first)==('prime','unordered','first')
        py_counts[int(n),int(k)] = int(num)
    assert py_counts == {(x[0],k):x[i]//2 for x in z58 for k,i in ((4,8),(8,9))}
    for n in sorted(zeros):
        assert n%840 in CLASSES
        a,b,c,d=full8(n)
        assert 8*a*b*c*d==a+b+n*c
        fac=profile(n-1);shift=profile(12*n+1)
        print('R8-MISS',n,'mod840',n%840,'p-1',fac,'12p+1',shift,'full8',a,b,c,d)

if __name__=='__main__':
    panels()
    hunts()
