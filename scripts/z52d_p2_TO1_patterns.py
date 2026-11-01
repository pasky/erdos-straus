# z52d pass2 TO1 (Z0262/Z0319): 2-adic valuation patterns realised per prime, from the bitmask columns of the full-enumeration table.
# usage: python3 scripts/z52d_p2_TO1_patterns.py data/z52b/pass2/TO1/es_100000.tsv
import sys
rows=[]
for l in open(sys.argv[1]):
    f=l.split(); p=int(f[0]); pat=(int(f[6])<<64)|int(f[7]); rows.append((p,pat))
print("pattern (sorted v2 triple, capped at 4): #primes realising / #primes missing / largest missing p")
for a in range(5):
  for b in range(a,5):
    for c in range(b,5):
      code=a*25+b*5+c
      real=[p for p,pat in rows if (pat>>code)&1]; miss=[p for p,pat in rows if not (pat>>code)&1]
      if a>=1 or (a==0 and b>=1):
        print(f"  {(a,b,c)}: real {len(real):5d}  miss {len(miss):5d}  largest-miss {max(miss) if miss else '-'}")
print("8-world failures (no realised pattern with min>=1 and max>=3):", [p for p,pat in rows if not any((pat>>(a*25+b*5+c))&1 for a in range(1,5) for b in range(a,5) for c in range(b,5) if c>=3)])
