"""R121B from-scratch numerics: cutoff supports/switch ranges, DI p.257 separation,
exceptional Kuznetsov transform lower bound (LOGLOG3 §4 (ii)/ lemma81 §2.2(c)) incl. non-uniformity near Y=1."""
import mpmath as mp
mp.mp.dps = 40
F = mp.mpf
# --- switched-modulus range: c = 4π√mn/(q x), √mn∈[N,2N]
def crange(qs, xs):  # q in [qs0,qs1]*Q, x in [xs0,xs1]/Y ; C=πNY/Q
    lo = 4*mp.pi*1/(qs[1]*xs[1])/mp.pi; hi = 4*mp.pi*2/(qs[0]*xs[0])/mp.pi
    return lo, hi
print("LOGLOG3 cutoffs c/C in", [mp.nstr(v,8) for v in crange((F(3)/4,F(9)/4),(F(11)/12,F(17)/12))], "64/51=",mp.nstr(F(64)/51,8),"128/11=",mp.nstr(F(128)/11,8))
print("DI pictured supports c/C in", [mp.nstr(v,8) for v in crange((F(1)/2,F(5)/2),(F(1)/2,F(5)/2))])
# --- DI p.257 separation: |b/(2√t)|/|a-u| <= 2θ(√2-1)√N/(2√t) * c / c with θ<2
for name,tmin in [("eta supp [3/4,9/4]",F(3)/4),("DI supp (1/2,3)",F(1)/2)]:
    print("separation ratio", name, mp.nstr(2*2*(mp.sqrt(2)-1)/(2*mp.sqrt(tmin)),6))
# complex disc radius 2^-12 at x=3/4
beta = 2*(mp.sqrt(2)-1)/(2)  # |β| = sup |b|/(2√N |a-u|) with θ<2: 2θ(√2-1)√N/c /(2√N /c)= θ(√2-1) < 2(√2-1)
print("min |1+β z^-1/2| on disc:", mp.nstr(1-2*(mp.sqrt(2)-1)/mp.sqrt(F(3)/4-F(2)**-12),6), ">= 1/64?")
# --- explicit eta from Lemma 1.3
h = lambda x: mp.e**(-1/x) if x>0 else F(0)
I = mp.quad(lambda x: h(F(1)/4+x)*h(F(1)/4-x), [-F(1)/4,0,F(1)/4])
rho = lambda x: h(F(1)/4+x)*h(F(1)/4-x)/I
Rcum = lambda w: F(0) if w<=-F(1)/4 else (F(1) if w>=F(1)/4 else mp.quad(rho,[-F(1)/4,w]))
eta = lambda x: Rcum(2*(x-F(7)/8)) - Rcum(2*(x-F(17)/8))
Psi = lambda u: eta(3*u-2)
print("eta checks: eta(1)=",mp.nstr(eta(1),10)," eta(2)=",mp.nstr(eta(2),10)," eta(0.76)=",mp.nstr(eta(F(0.76)),5)," eta(3/4)=",eta(F(3)/4))
# tabulate Psi on its support for quadrature
mp.mp.dps = 30
us = [F(11)/12 + (F(17)/12-F(11)/12)*k/200 for k in range(201)]
Pv = [Psi(u) for u in us]
def phihat_exc(sig, Y):
    # positive convention: π/(2 sin πσ) ∫ (J_{-2σ}(u/Y) - J_{2σ}(u/Y)) Ψ(u) du/u   (Simpson on tabulated Ψ)
    n=len(us)-1; hstep=(us[-1]-us[0])/n; s=F(0)
    for k,u in enumerate(us):
        w = 1 if k in (0,n) else (4 if k%2 else 2)
        s += w*(mp.besselj(-2*sig,u/Y)-mp.besselj(2*sig,u/Y))*Pv[k]/u
    return mp.pi/(2*mp.sin(mp.pi*sig))*s*hstep/3
for Y in [F(1),F(2),F(10),F(2)**32]:
    row=[]
    for sig in [F(10)**-6, F(10)**-3, F(0.05), F(0.15), F(0.25)]:
        v = phihat_exc(sig,Y)/mp.cos(mp.pi*sig)/Y**(2*sig)
        row.append(mp.nstr(v,5))
    print("Y=",mp.nstr(Y,4)," φ̂(-iσ)/(cos πσ·Y^{2σ}) at σ=1e-6,1e-3,.05,.15,.25:",row)
