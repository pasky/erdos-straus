#!/usr/bin/env python3
"""Stream a regenerated HCWIN scan, independently of its numpy/pandas analyzer.

Run with timeout and ulimit; accepts one or more chronologically ordered files.
--allow-truncated-last skips only an incomplete final record of a file, reporting it.
This supports resuming a timed-out scan at the last COMPLETE prime plus eight.
Memory use is constant in the number of primes.
"""
import argparse
import math

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--allow-truncated-last", action="store_true")
parser.add_argument("files", nargs="+")
args = parser.parse_args()
windows = (8, 12, 16, 20, 24, 28, 32, 40, 48, 64)
failures = [0] * len(windows)
dead = [0] * len(windows)
predicted = [[0.0, 0.0] for _ in windows]
max_s = [0.0] * len(windows)
count = skipped = last = 0
for path in args.files:
    with open(path) as f:
        for line in f:
            a = line.split()
            if len(a) != 32 or not line.endswith("\n"):
                assert args.allow_truncated_last and not f.read(1), (path, count)
                print("Skipping incomplete final record:", path)
                skipped += 1
                continue
            p, hc = map(int, a[:2])
            assert p > last, (p, last)
            last = p
            count += 1
            for i, x in enumerate(windows):
                fail = hc == 0 or hc > x
                failures[i] += fail
                deterministic = int(a[4 + 3 * i])
                assert not (fail and deterministic)
                if deterministic:
                    continue
                e, l = float(a[2 + 3 * i]), float(a[3 + 3 * i])
                if e + l == 0:
                    dead[i] += fail
                    continue
                predicted[i][0] += math.exp(-e - l / 2)
                predicted[i][1] += math.exp(-e - l)
                if fail:
                    max_s[i] = max(max_s[i], e + l / 2)
print("Complete rows:", count, "incomplete rows skipped:", skipped, "last prime:", last)
for i, x in enumerate(windows):
    print(f"X={x}: failures={failures[i]} genus-dead={dead[i]} class={failures[i]-dead[i]} "
          f"pred(cL=0.5,1)={predicted[i][0]:.6f},{predicted[i][1]:.6f} maxS={max_s[i]:.6f}")
