"""z52b pass1 L00 Z0222: summarise data/z52b/pass1/L00/es_counts.csv (output of z52b_p1_L00_es_count.py) by dyadic bins of p.
Prints mean f(p) per bin, mean/log^2 p, mean/log^3 p, and the local exponent d ln(mean)/d ln(ln p) between bins."""
import csv, math
rows = [(int(a), int(b)) for a, b in list(csv.reader(open("data/z52b/pass1/L00/es_counts.csv")))[1:]]
print("primes", len(rows), "max p", max(p for p, _ in rows))
print("%14s %5s %8s %8s %8s %8s" % ("bin", "n", "mean f", "mean/L2", "mean/L3", "slope"))
prev = None
lo = 100
while lo < 12800:
    hi = 2 * lo
    xs = [f for p, f in rows if lo <= p < hi]
    if xs:
        m = sum(xs) / len(xs)
        L = math.log(math.sqrt(lo * hi))  # ln of geometric centre
        slope = ""
        if prev:
            slope = "%.2f" % (math.log(m / prev[1]) / math.log(L / prev[0]))
        print("%14s %5d %8.2f %8.3f %8.4f %8s" % (f"[{lo},{hi})", len(xs), m, m / L**2, m / L**3, slope))
        prev = (L, m)
    lo = hi
