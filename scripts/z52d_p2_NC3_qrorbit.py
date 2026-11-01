# Z2750: is L3(p) invariant under multiplicative symmetries of F_p^* that preserve the QR set?
# Stabiliser G_p = {s in F_p^*: sL3 = L3}; also test s=-1, inversion x->1/x, and x -> -1/x (PSL2-type on F_p^*).
import sys
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
PM = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
stab_nontriv = []
cnt = 0; inv_ok = 0; neg_ok = 0; negsq = 0; sq_stab = {}
for p in L.primes_upto(PM):
    if p % 8 != 1 or p < 17: continue
    S = set(L.L3(p))
    if not S: continue
    cnt += 1
    G = [s for s in range(1, p) if {(s*A) % p for A in S} == S]
    if len(G) > 1: stab_nontriv.append((p, G))
    inv_ok += all((pow(A, p-2, p)) in S for A in S)
    neg_ok += {(p-A) % p for A in S} == S
    # is L3 contained in a coset of squares structure? fraction of QR (already)
print("primes", cnt)
print("L3 closed under A->A^{-1}:", inv_ok, "/", cnt)
print("L3 closed under A->-A:", neg_ok, "/", cnt)
print("primes with nontrivial multiplicative stabiliser:", len(stab_nontriv), stab_nontriv[:10])
