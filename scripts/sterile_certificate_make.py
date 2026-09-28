"""Save the (sterile) component of the hub fibre of x at p as a certificate.

PYTHONPATH=scripts uv run --with python-flint python scripts/sterile_certificate_make.py P X OUT.json.gz
With X=seed, certifies the whole seed component instead. Otherwise refuses to write unless the full component is exhausted and has no positive vertex."""
import gzip, json, sys
from pointwise_fibres_big import BigFibreOracle, exhaust_component
from pointwise_refactor import seed
p, x, out = int(sys.argv[1]), sys.argv[2], sys.argv[3]
O = BigFibreOracle(p)
if x == "seed":   # certify the whole seed component (positive vertices allowed)
    S, pos = exhaust_component(O, seed(p))
    kind = "seed"
else:
    x = int(x)
    S, pos = exhaust_component(O, sorted(O.fibre(x))[0])
    assert pos == 0, f"component has {pos} positive vertices"
    kind = "sterile"
json.dump({"p": str(p), "hub": str(x), "size": len(S), "kind": kind, "positive": pos,
           "vertices": [[str(a) for a in v] for v in sorted(S)]}, gzip.open(out, "wt"))
print(p, x, len(S))
