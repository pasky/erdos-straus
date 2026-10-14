"""R208: explicit signed pentagon friezes at every odd square with a quiddity = 4 (no positivity => no T1)."""
for M in range(3, 2001, 2):
    N = M * M
    c, m, s = 4, -(N + 3) // 4, -1
    assert m * c * s - c - s == N
    h, hp = c * m - 1, m * s - 1
    assert hp * c == N + s and c * m == 1 + h and m * s == 1 + hp and s * h == N + c and h * hp == 1 + N * m
    assert 0 not in (h, hp, c, m, s)
print("odd M in [3,2000): signed word (4, -(M^2+3)/4, -1) at N = M^2, quiddity c = 4, all Ptolemy relations OK")
