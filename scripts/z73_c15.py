"""Test the exact c=15 coset obstruction in a fresh consecutive prime-cluster cohort."""
import csv
from itertools import islice
from fractions import Fraction
from collections import Counter
from z72_counter_tail import candidates, fact_many, scan, ROOT, L
from z72_tail_audit import box

H={1,2,4,8}

def block(ps):
    for p,fs in zip(ps,fact_many([(p+15)//16 for p in ps])):
        assert p%L==1 and all(q%15 in {1,2,4,7,8,11,13,14} for q in fs)
        yield all(q%15 in H for q in fs),fs

def run():
    old=[r for r in csv.DictReader((ROOT/'cluster.csv').open()) if r['arm']=='target']
    assert all(miss==(int(r['first_c'])>15) for r,(miss,_) in zip(old,block([int(r['p']) for r in old])))
    ps=list(islice(candidates(6*10**18,[1,2,3]),2048))
    flags=list(block(ps)); res=scan(ps,2047)
    assert len(res)==len(ps)
    with (ROOT/'c15.csv').open('w') as f:
        w=csv.writer(f,lineterminator='\n'); w.writerow(['p','blocked15','factors_Q4','first_c','A','B','x','y','z'])
        for p,(miss,fs) in zip(ps,flags):
            c,a,b,x,y,z=res[p]
            assert miss==(c>15) and Fraction(4,p)==sum(Fraction(1,d) for d in (x,y,z))
            if c>63:
                assert not any(box(p,j) for j in range(3,c,4)) and box(p,c)
            w.writerow([p,int(miss),' '.join(map(str,fs.elements())),*res[p]])
    vals=sorted(res[p][0] for p,(m,_) in zip(ps,flags) if m)
    print(len(vals),'blocked, of which composite Q4',sum(m and sum(fs.values())>1 for m,fs in flags),'median/max',vals[(len(vals)-1)//2],vals[-1]);print(Counter(vals));print(ps[-1])

if __name__=='__main__':run()
