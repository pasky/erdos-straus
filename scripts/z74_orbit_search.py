"""Seek simultaneous finite closed components, screening the cheaper 3/p seed first."""
import csv
from sympy import primerange
from z73_four_orbit import ROOT, orbit


def other(p):
    assert p%3==1
    b=(p+2)//3
    return tuple(sorted((b,p,p*b,p*b)))


def search(limit):
    with (ROOT/'two_seed_scan.csv').open('w') as f:
        w=csv.writer(f,lineterminator='\n'); w.writerow(['p','T_status','T_depth','T_states','O_status','O_depth','O_states'])
        for p in primerange(3,limit):
            if p%840 not in {1,121,169,289,361,529}:continue
            t=orbit(p,8,160,other(p))
            o=orbit(p,12,700) if t[1]=='closed' else ['', '', '', '']
            w.writerow([p,*t[1:4],*o[1:4]]); f.flush()
            if o[1]=='closed': print(p,t,o,flush=True);break

if __name__=='__main__':search(1200000)
