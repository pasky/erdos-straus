# R31: residue-level check of the Thm 6.1 covering, mod 840 (and conditions p≡1 (24), p≡2,3 (5), 7∤p)
certs=[(5,1,3),(5,1,7),(10,1,7),(5,2,7)]
unc=[]
for p in range(840):
    if p%24!=1 or p%5 not in (2,3) or p%7==0: continue
    ok=[(c,k,D) for c,k,D in certs if (p+D)%(4*c*k)==0 and (p*p+4*c*k*k)%D==0]
    if not ok: unc.append(p)
print("uncovered classes mod 840:",unc)
