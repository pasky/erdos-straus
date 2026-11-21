#!/usr/bin/env python3
"""Resumable one-prime-at-a-time driver for z78_r2exact.c.

Log format is defined in the note and in each source output: ROW r L1 P3marg
Q3marg P5marg; native moduli are r,r^2,r^3,r^3. Each prime gets one plain
text file, atomically written only after successful completion.
"""
import argparse
import os
import resource
import subprocess
from pathlib import Path


def primes(lo, hi):
    sieve = bytearray(b"\x01") * (hi + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(hi**0.5) + 1):
        if sieve[p]:
            sieve[p*p:hi+1:p] = b"\x00" * (((hi-p*p)//p) + 1)
    return [n for n in range(max(2, lo), hi + 1) if sieve[n]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lo", type=int)
    ap.add_argument("hi", type=int)
    ap.add_argument("--bin", default="data/z78/r2exact/z78_r2exact")
    ap.add_argument("--out", default="data/z78/r2exact/logs")
    args = ap.parse_args()
    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    def limit_memory():
        cap = 2_000_000 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (cap, cap))
    for r in primes(args.lo, args.hi):
        target = outdir / f"r{r}.txt"
        if target.exists() and f"ROW {r} " in target.read_text():
            continue
        run = subprocess.run(["timeout", "1800", args.bin, str(r)],
                             capture_output=True, text=True,
                             preexec_fn=limit_memory)
        if run.returncode:
            print(f"STOP r={r} rc={run.returncode} stderr={run.stderr[-2000:]}", flush=True)
            return run.returncode or 1
        rows = [line for line in run.stdout.splitlines() if line.startswith("ROW ")]
        if len(rows) != 1 or rows[0].split()[:2] != ["ROW", str(r)]:
            print(f"STOP malformed output r={r}: {run.stdout[-2000:]}", flush=True)
            return 2
        tmp = target.with_suffix(".tmp")
        tmp.write_text(run.stdout)
        tmp.replace(target)
        print(rows[0], flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
