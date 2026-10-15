"""R247: check on the brute-force census that no tuple has v_T(E + 1 + cT) >= s - 2 (no 'structured' tuples at x*_c),
and print the max of v_T(E + 1 + cT) - (s - 2) over the census."""
import sys
def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return [x%3 for x in r]
def add(a,b):
    n=max(len(a),len(b)); return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%3 for i in range(n)]
f=lambda x:[int(ch) for ch in x]; worst=-99; n=0
for l in open(sys.argv[1]):
    s,m,g,w,C,v=l.split(); s=int(s); n+=1
    E=add(mul(mul(mul(f(g),f(m)),[0,1]),f(w)),[2])
    for c in (1,2):
        d=add(E,[1,c]); dep=next(i for i,x in enumerate(d) if x)
        worst=max(worst,dep-(s-2))
print('tuples',n,'max dep-(s-2) over c=1,2:',worst)
for l in open(sys.argv[1]):
    s,m,g,w,C,v=l.split(); s=int(s)
    E=add(mul(mul(mul(f(g),f(m)),[0,1]),f(w)),[2])
    for c in (1,2):
        d=add(E,[1,c]); dep=next(i for i,x in enumerate(d) if x)
        if dep>=s-2: print('structured-depth tuple: s',s,'c',c,"m' g' w1 C1 v1 =",m,g,w,C,v,'dep',dep)
