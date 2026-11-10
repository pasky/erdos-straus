"""Independent 35-digit contour check of Theorem F (no lane-code imports).
Run with uv run --with mpmath python ... M re im.
Small-t Mellin expansion is asymptotic: compare switches/degree, not a certificate.
"""
import sys
import mpmath as m
m.mp.dps = 35
M = int(sys.argv[1]); a = m.mpf(M-1)/M
z = m.mpc(sys.argv[2], sys.argv[3])*m.mpf('1.6')/(M-1)**2
cut = m.mpf(sys.argv[4]) if len(sys.argv)>4 else m.mpf('0.00025')
N = 64
roots = {sgn: m.exp(2j*m.pi*sgn*a) for sgn in (-1,1)}
poly = {sgn: [m.polylog(-k,r) for k in range(N)] for sgn,r in roots.items()}
facs = [(2j*m.pi)**k/m.factorial(k) for k in range(N)]
def dual(tau, s, t):
    if abs(tau)<cut:
        return m.polyval(list(reversed([facs[k]*poly[s][k]*poly[t][k] for k in range(N)])),tau)
    # Exact two-strip identity, omitting only m,n > K. The omitted absolute
    # tail is at most exp(-b*(K+1)**2)/(1-exp(-b*(K+1)))**2.
    b=2*m.pi*tau.imag; K=int(m.ceil(m.sqrt(120/b)))
    bound=m.exp(-b*(K+1)**2)/(1-m.exp(-b*(K+1)))**2
    assert bound<m.mpf('1e-42')
    q=m.exp(2j*m.pi*tau); qm=q; pu=roots[s]; pv=roots[t]; total=0j
    qK=q**(K+1); qKm=qK; rvK=roots[t]**(K+1)
    for n in range(1,K+1):
        total+=pv*roots[s]*qm/(1-roots[s]*qm)+pu*rvK*qKm/(1-roots[t]*qm)
        qm*=q;pu*=roots[s];pv*=roots[t];qKm*=qK
    return total
w=-1/(M*M*z)
# Deliberately different contour from lane: angle -arg(w)/3, below t=1.
rot=m.exp(-1j*m.arg(w)/3)
end=110/(2*m.pi*(w*rot).imag)
def integrand(s):
    t=s*rot; tau=t*w
    plus=dual(tau,1,1)+dual(tau,-1,-1)
    minus=dual(tau,1,-1)+dual(tau,-1,1)
    return rot*t*(plus/(t-1)-minus/(t+1))
breaks=sorted(set([m.mpf(0),cut/abs(w)]+[end/2**j for j in range(31)]))
psi=1j/(2*m.pi*M*M*z)*m.quad(integrand,breaks,method='gauss-legendre',maxdegree=6)
E=1j/(2*m.pi*M*M*z)*(-m.euler-m.log(-2j*m.pi*M*M*z)-2*m.digamma(a))+(m.mpf('.5')-a)**2
rhs=dual(w,1,1)/(M*M*z)+E+psi
lhs=0j
for A in range(M-1,10000000,M):
    term=m.exp(2j*m.pi*A*(M-1)*z)/(1-m.exp(2j*m.pi*A*M*z));lhs+=term
    if abs(term)<m.mpf('1e-42'):break
err=abs(lhs-rhs)/abs(lhs)
print('M',M,'z0',sys.argv[2:4],'dps',m.mp.dps,'cut',cut,'L',m.nstr(lhs,25),'relative',m.nstr(err,12),flush=True)
assert err<m.mpf('1e-15'), err
