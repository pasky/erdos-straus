"""z67 ELL0: cross-check z66_ucover_swords.c against the independent brute force z66_ucover_sbrute.py at gap primes.
Checks brute (good, unit residues, levels <= K) subset of exact.  Usage: ... ELL AMAX UVMAX K"""
import subprocess, sys
ell, AMAX, UVMAX, K = map(int, sys.argv[1:5])
b = subprocess.run(["uv", "run", "--with", "sympy", "python", "scripts/z66_ucover_sbrute.py", str(ell), str(AMAX), str(UVMAX)],
                   capture_output=True, text=True, check=True).stdout.split("\n")
brute = set()
for line in b:
    if line.strip():
        k, r, w = line.split(); k, r = int(k), int(r)
        if k <= K and r % ell:
            brute.add((k, r))
exact = set()
for k in range(1, K + 1):
    out = subprocess.run(["/tmp/zsw", str(ell), str(k)], capture_output=True, text=True, check=True).stdout
    for line in out.splitlines():
        t = line.split(); r = int(t[1])
        if r % ell == 0: continue
        nonres = pow(r % ell, (ell - 1) // 2, ell) == ell - 1
        if (t[0] == "W1" and k % 2 == 1 and nonres) or (t[0] == "W2" and t[4] == "1"):
            exact.add((k, r))
print(f"ell={ell} AMAX={AMAX} UVMAX={UVMAX} K={K}: brute {len(brute)}, exact {len(exact)}, brute-not-exact {len(brute - exact)}")
