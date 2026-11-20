"""Prepare sorted exact jobs, or consume and validate one positive per job."""
import sys
from pathlib import Path

jobs = []
for line in Path(sys.argv[1]).read_text().splitlines():
    tag, n = line.split()
    assert tag in {'8', 'R'}, ('unresolved beyond scan cap, not a zero', tag, n)
    jobs.append((8 if tag == '8' else 4, int(n)))
assert len(set(jobs)) == len(jobs)
jobs.sort()
if len(sys.argv) == 2:
    for k, n in jobs:
        print(k, n)
else:
    lines = Path(sys.argv[2]).read_text().splitlines()
    assert len(lines) == len(jobs)
    for line, job in zip(lines, jobs):
        k, n, u, b, c = map(int, line.split())
        assert job == (k, n) and 0 < u <= b and c > 0 and k*u*b*c-u-b == n
    print(f'validated {len(lines)} positive fallback triples')
