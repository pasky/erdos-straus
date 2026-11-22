#!/usr/bin/env python3
"""z81 LIT (copy of z71_lit_arxiv.py): deterministic arXiv sweep. Fetch every listing in given categories over a date window
via the arXiv API (paged), write a TSV (id, date, primary, cats, authors, title, abstract).
Usage: z81_lit_arxiv.py OUT.tsv FROM(YYYYMMDD) TO(YYYYMMDD) QUERY
  QUERY is an arXiv search_query fragment, e.g. 'cat:math.NT' or 'all:"unit fractions"'.
"""
import sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
out, d0, d1, q = sys.argv[1:5]
NS = {'a': 'http://www.w3.org/2005/Atom', 'x': 'http://arxiv.org/schemas/atom'}
query = f'({q}) AND submittedDate:[{d0}0000 TO {d1}2359]'
start, page, rows, total = 0, 200, [], None
while True:
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode(dict(
        search_query=query, sortBy='submittedDate', sortOrder='descending', start=start, max_results=page))
    for attempt in range(6):
        try:
            data = urllib.request.urlopen(url, timeout=90).read()
            root = ET.fromstring(data)
            ents = root.findall('a:entry', NS)
            total = int(root.find('{http://a9.com/-/spec/opensearch/1.1/}totalResults').text)
            if ents or start >= total:
                break
            total = None  # empty page below reported total: retry
        except Exception as e:
            print('retry', attempt, e, file=sys.stderr)
        time.sleep(5 + 5 * attempt)
    else:
        print(f'FAILED at start={start} (total={total})', file=sys.stderr)
        sys.exit(2)  # non-zero: caller must record the query as FAILED, not as zero hits
    for e in ents:
        g = lambda t: ' '.join((e.find(t, NS).text or '').split())
        rows.append('\t'.join([
            g('a:id').rsplit('/', 1)[-1], g('a:published')[:10],
            e.find('x:primary_category', NS).get('term'),
            ','.join(c.get('term') for c in e.findall('a:category', NS)),
            '; '.join(' '.join(a.find('a:name', NS).text.split()) for a in e.findall('a:author', NS))[:300],
            g('a:title'), g('a:summary')]))
    start += len(ents)
    print(f'{start}/{total}', file=sys.stderr)
    if start >= total or not ents:
        break
    time.sleep(3.1)
open(out, 'w').write('\n'.join(rows) + '\n')
print(f'wrote {len(rows)} rows (total reported {total}) to {out}')
