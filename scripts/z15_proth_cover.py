# O240: ET/divisor covering of 3*2^s+1 for all s mod L except the Theorem-B exponential classes s == 0, 12 (mod 40).
import sys; sys.path.insert(0,'.')
import ec_cover
k=int(sys.argv[1]); L=int(sys.argv[2]); Mmax=int(sys.argv[3])
excl=set(int(x) for x in sys.argv[4].split(',')) if len(sys.argv)>4 else {0,12}
assert L%40==0
res=set(r for r in range(40) if r not in excl)
ch=ec_cover.search(k,L,Mmax,restrict=(40,res))
