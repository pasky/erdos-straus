"""Save the (sterile) component of the hub fibre of x at p as a certificate.

PYTHONPATH=scripts uv run --with python-flint python scripts/sterile_certificate_make.py P X OUT.json.gz
Refuses to write unless the full component is exhausted and has no positive vertex."""
import gzip, json, sys
from pointwise_fibres_big import BigFibreOracle, exhaust_component
p, x, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
O = BigFibreOracle(p)
S, pos = exhaust_component(O, sorted(O.fibre(x))[0])
assert pos == 0, f"component has {pos} positive vertices"
json.dump({"p": str(p), "hub": str(x), "size": len(S),
           "vertices": [[str(a) for a in v] for v in sorted(S)]}, gzip.open(out, "wt"))
print(p, x, len(S))
