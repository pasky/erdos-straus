# loader for the binary feature file written by scripts/z52d_p2_TO7_feat.c (16-byte records)
import numpy as np
DT = np.dtype([("p","<u4"),("k","<u2"),("type","u1"),("omega","u1"),("flags","u1"),("pad","u1"),("pad2","<u2"),("P1","<u4")])
def load(path="/tmp/feat_1e6.bin"):
    return np.fromfile(path, dtype=DT)
def bits(a):
    f = a["flags"]
    return dict(dh=(f&1)>0, sqf=(f&2)>0, gen=(f&4)>0, sp=(f&8)>0)
