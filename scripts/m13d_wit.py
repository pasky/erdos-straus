"""Python driver for the C complete-witness engine scripts/m13d_wit.c (task O103).

Engine(binary) keeps one subprocess; query(x, L, req=1, all=False) -> list of (fam, (p1,p2,p3)) in
mordell_lib conventions (I1 found via g is converted: f = (4a^2d+1)/g).
"""
import subprocess, os

HERE = os.path.dirname(os.path.abspath(__file__))
BIN = os.environ.get('M13D_WIT', '/tmp/o103/wit')


def build(path=BIN):
    src = os.path.join(HERE, 'm13d_wit.c')
    if not os.path.exists(path) or os.path.getmtime(path) < os.path.getmtime(src):
        subprocess.check_call(['gcc', '-O2', '-o', path, src])
    return path


class Engine:
    def __init__(self, path=None):
        self.p = subprocess.Popen([build(path or BIN)], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  text=True, bufsize=1)

    def query(self, x, L, req=1, all=False):
        self.p.stdin.write(f"{L} {x % L} {req} {1 if all else 0}\n")
        self.p.stdin.flush()
        h = self.p.stdout.readline().split()
        assert h[0] == 'N', h
        out = []
        for _ in range(int(h[1])):
            fam, a, b, c = self.p.stdout.readline().split()
            a, b, c = int(a), int(b), int(c)
            if fam == 'I1g':
                N = 4 * a * a * b + 1
                assert N % c == 0
                fam, c = 'I1', N // c
            out.append((fam, (a, b, c)))
        return out

    def close(self):
        self.p.stdin.close()
        self.p.wait()
