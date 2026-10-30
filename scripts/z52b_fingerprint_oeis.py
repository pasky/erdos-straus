"""OEIS lookup helper with on-disk cache and rate limiting (>=2 s between requests).
Usage: lookup(list_of_ints) -> list of (A-number, name) ; caches in data/z52b/oeis_cache.json"""
import json, time, os, urllib.request, urllib.parse, sys
CACHE = os.path.join(os.path.dirname(__file__), '..', 'data', 'z52b', 'oeis_cache.json')
_last = [0.0]
def _load():
    try: return json.load(open(CACHE))
    except Exception: return {}
def lookup(seq, n=None, raw=False):
    terms = [int(t) for t in seq][: (n or 20)]
    q = ','.join(map(str, terms))
    c = _load()
    if q not in c:
        dt = time.time() - _last[0]
        if dt < 2.1: time.sleep(2.1 - dt)
        url = 'https://oeis.org/search?q=' + urllib.parse.quote(q) + '&fmt=json'
        for attempt in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'es-research/0.1'}), timeout=40) as r:
                    data = json.loads(r.read().decode())
                break
            except Exception as e:
                time.sleep(5); data = {'error': str(e)}
        _last[0] = time.time()
        res = []
        if isinstance(data, list):
            res = [('A%06d' % d['number'], d['name']) for d in data[:8]]
        elif isinstance(data, dict) and data.get('results'):
            res = [('A%06d' % d['number'], d['name']) for d in data['results'][:8]]
        elif isinstance(data, dict) and 'error' in data:
            res = [('ERR', data['error'])]
        c = _load(); c[q] = res
        json.dump(c, open(CACHE, 'w'), indent=0)
    return c[q]
if __name__ == '__main__':
    print(lookup(sys.argv[1].split(',')))
