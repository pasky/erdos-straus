"""Assessment only: full-grid hierarchical Beta-binomial, explicitly stationary.
No inference about an infinite arithmetic tail is identified by finite sibling data.
"""
import gzip,json,re
from pathlib import Path
import numpy as np
from scipy.special import betaln,logsumexp
out=Path('data/z52b/pass2/ZF0/Z1890')
rows=[]
# Original complete witness files; small n=2..8 supplied by reviewed Z52_BANKED T2.
with gzip.open('data/z52_bank/pencil_km4_witness_n9_1e5.txt.gz','rt') as f:
    pencil=[(int(l.split()[0]),'FAIL' in l) for l in f if l.strip()]
pencil=[(n,n==2) for n in range(2,9)]+pencil
with open('data/z52_bank/gauss_q1_first_le1e4.txt') as f: gauss=[(int(l.split()[2]),'FAIL' in l) for l in f if l.strip()]
with gzip.open('data/z52_bank/gauss_q1_first_1e4_1e6.txt.gz','rt') as f:gauss += [(int(l.split()[2]),'FAIL' in l) for l in f if l.strip()]
text=Path('data/bs_ident/mn_exceptions_3000.txt').read_text(); line=next(l for l in text.splitlines() if 'm=8 ' in l); fail8=[int(v) for v in line.split('#')[0].split() if int(v)>=2]
for name,values,source in [('pencil_minus4',pencil,'data/z52_bank/pencil_km4_witness_n9_1e5.txt.gz; Z52_BANKED.md T2 for n<9'),('Gaussian_Q1',gauss,'data/z52_bank/gauss_q1_first_le1e4.txt; data/z52_bank/gauss_q1_first_1e4_1e6.txt.gz'),('eight_over_n',[(n,n in fail8) for n in range(2,3001)],'data/bs_ident/mn_exceptions_3000.txt')]:
    assert len({n for n,f in values})==len(values)
    rows.append({'sibling':name,'trials':len(values),'failures':sum(f for n,f in values),'range':[min(n for n,f in values),max(n for n,f in values)],'failure_values':[n for n,f in values if f],'source':source,'bins':[{'range':[lo,hi],'trials':sum(lo<=n<=hi for n,f in values),'failures':sum(lo<=n<=hi and f for n,f in values)} for lo,hi in [(2,1000),(1001,10000),(10001,100000),(100001,1000000)]]})
(out/'sibling_counts.json').write_text(json.dumps(rows,indent=2))
# Independent per-sibling latent rates; grid prior uniform in log10(mu),log10(kappa).
mu=10**np.linspace(-8,-.3,181);kap=10**np.linspace(-1,7,181);M,K=np.meshgrid(mu,kap,indexing='ij');A=M*K;B=(1-M)*K
ll=np.zeros_like(A)
for r in rows:ll+=betaln(A+r['failures'],B+r['trials']-r['failures'])-betaln(A,B)
w=np.exp(ll-logsumexp(ll))
def quant(arr):
    order=np.argsort(arr.ravel());v=arr.ravel()[order];cdf=np.cumsum(w.ravel()[order]);return [float(v[min(np.searchsorted(cdf,q),len(v)-1)]) for q in [.025,.5,.975]]
pred=[]
for H in [1,1000,1000000,10**9]:
    nofail=np.exp(betaln(A,B+H)-betaln(A,B));pred.append({'future_trials':H,'prob_any_failure':float(np.sum(w*(1-nofail)))})
res={'label':'Assessment','model':'yi|theta_i ~ Binomial(Ni,theta_i); theta_i|mu,kappa ~ Beta(mu*kappa,(1-mu)*kappa); independent siblings, exchangeable new ES rate','prior':'log10(mu) uniform [-8,-0.3], log10(kappa) uniform [-1,7], 181x181 grid','mu_95CI_and_median':quant(M),'kappa_95CI_and_median':quant(K),'posterior_mean_mu':float((w*M).sum()),'grid_boundary_mass':float(w[0,:].sum()+w[-1,:].sum()+w[:,0].sum()+w[:,-1].sum()),'finite_predictive':pred,'P_ES_counterexample_beyond_1e18_stationary_model':1.0,'reason':'A Beta distribution has theta_ES>0 almost surely; infinitely many independent future trials then fail almost surely. This is a MODEL ARTEFACT, not evidence ES is false. The threshold 1e18 does no work in a stationary model.','spike_at_zero_sensitivity':[{'prior_P_ES_true':p,'posterior_P_any_failure_in_infinite_tail':1-p} for p in [.1,.5,.9]],'nonidentifiability':'An independent ES-specific zero-rate indicator has identical sibling likelihood under both states, so its prior is unchanged. Finite data do not determine decay/extrapolation of arithmetic failure probabilities; the siblings have incompatible domains and visibly nonstationary bins. No valid real-world P(ES false) is claimed.'}
(out/'posterior.json').write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
