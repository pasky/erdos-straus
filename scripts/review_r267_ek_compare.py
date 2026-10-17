"""Compare R267 solver output (E lines) with the author's logs/z28_Ek_primes_1e*.txt (after removing p=2 and p | k)."""
import sys, re
log, mine = sys.argv[1], sys.argv[2:]
auth = {}
for line in open(log):
    m = re.match(r"k=(\d+): (.*) #(\d+)", line.strip())
    if m:
        k = int(m.group(1)); auth[k] = [int(x) for x in m.group(2).split()]
for f in mine:
    E = {}; P = None
    for line in open(f):
        if line.startswith("E "):
            k, p = (int(t.split("=")[1]) for t in line.split()[1:3]); E.setdefault(k, []).append(p)
        elif line.startswith("k="):
            k = int(line.split()[0][2:]); P = int(line.split()[1][2:]); E.setdefault(k, [])
    for k, lst in sorted(E.items()):
        a = [p for p in auth[k] if p != 2 and k % p and p <= P]
        print(k, "P=%d" % P, "mine=%d last=%s" % (len(lst), lst[-1] if lst else None), "author=%d" % len(a), "MATCH" if a == lst else "DIFF")
