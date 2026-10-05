#!/usr/bin/env python3
"""POINTWISE_WINDOW3 §2.1: continuum F_± of the heuristic one-window law. Usage: window3_cont.py EPS N"""
import numpy as np, sys
# continuum heuristic: Poisson intensity ±1/(2t) on [eps,1], cofactor weight (u-S)^(-1/2)
eps=float(sys.argv[1]); N=int(sys.argv[2])
h=1.0/N; t=np.arange(N+1)*h
for sgn in (+1,-1):
    lam=np.where(t>=eps, sgn*0.5/np.maximum(t,1e-12),0.0)*h  # point masses on grid
    # G = sum_k lam^{*k}/k!  via exp in power series (truncated convolution)
    G=np.zeros(N+1); G[0]=1; term=G.copy()
    for k in range(1,int(1/eps)+2):
        term=np.convolve(term,lam)[:N+1]/k; G+=term
    # F(u) = sum_s G(s) (u-s)^(-1/2), cofactor weight with midpoint fix
    F=[]
    for u in (0.5,0.6,0.7,0.8,0.9,1.0):
        iu=int(round(u*N)); s=t[:iu]; F.append(np.sum(G[:iu]*(u-s+h/2)**-0.5))
    print(sgn, np.round(F,4))
