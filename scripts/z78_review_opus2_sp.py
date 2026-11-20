"""Numerical check of §7's B-process formula: for the shifted correlation
S(Q)=sum_x a(t/W) e(A/(x(x+hQ))), t=x+hQ/2, compare with
  sum_m (-1)^{m hQ} W a(y*) e(T phi(y*)+1/8)/sqrt(T phi''(y*))   [exact critical value]
and with the quadratic-in-Q model  T phi0 + xi_m Q^2  (xi_m from the note)."""
import numpy as np
from math import pi
def bump(y, lo=0.7, hi=2.6):
    out = np.zeros_like(y); m = (y > lo) & (y < hi)
    u = (y[m]-lo)/(hi-lo); out[m] = np.exp(-1/(u*(1-u)))*np.exp(4); return out
W = 4000; Y = 12.0; T = W*Y; A = T*W**2; h = 1
x = np.arange(int(0.3*W), int(3.0*W))
def S_exact(Q):
    t = x + h*Q/2.0
    return np.sum(bump(t/W)*np.exp(2j*pi*A/(x*(x+h*Q)*1.0)))
def crit(mu, s):
    # solve 2y/(y^2-s^2)^2 = mu by Newton
    y = (2/mu)**(1/3)
    for _ in range(60):
        f = 2*y/(y*y-s*s)**2 - mu
        fp = 2/(y*y-s*s)**2 - 8*y*y/(y*y-s*s)**3
        y -= f/fp
    phi = 1/(y*y-s*s) + mu*y          # phase T*(1/(y^2-s^2) - (m/Y)y), m=-|m|: +mu y with mu=|m|/Y
    phi2 = -2/(y*y-s*s)**2 + 8*y*y/(y*y-s*s)**3
    return y, phi, phi2
def S_pred(Q, quad=False):
    s = h*Q/(2.0*W); tot = 0j
    for M in range(1, int(40*Y)):
        mu = M/Y; y, phi, phi2 = crit(mu, s)
        if quad:
            y0 = (2/mu)**(1/3); phi0 = 1/y0**2 + mu*y0
            xi = A*h*h/(4*W**4)*(mu/2)**(4/3)     # note's xi_m
            ph = T*phi0 + xi*Q*Q
        else:
            ph = T*phi
        a = bump(np.array([y]))[0]
        if a == 0: continue
        tot += (-1)**(M*h*Q % 2) * W*a*np.exp(2j*pi*(ph+1/8))/np.sqrt(T*phi2)
    return tot
print('W',W,'Y',Y,'T',T,'h',h)
for Q in (20, 21, 40, 41, 80, 81, 160):
    e = S_exact(Q); p = S_pred(Q); pq = S_pred(Q, True)
    s = h*Q/(2*W)
    print(f'Q={Q:4d} |S|={abs(e):9.3f} |S-pred|={abs(e-p):7.4f} |S-quadpred|={abs(e-pq):8.4f} Tsigma^4={T*s**4:.2e} trivial W/sqrtT*Y={W/np.sqrt(T)*Y:.1f}')
