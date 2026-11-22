#!/usr/bin/env python3
"""z81 LIT: version check (arXiv API id_list) for papers the campaign leans on.
Usage: z81_lit_versions.py OUT.tsv ID [ID ...]  -> id, latest version, published, updated, title, comment"""
import sys, urllib.parse, urllib.request, xml.etree.ElementTree as ET
NS = {'a': 'http://www.w3.org/2005/Atom', 'x': 'http://arxiv.org/schemas/atom'}
out, ids = sys.argv[1], sys.argv[2:]
url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode(dict(id_list=','.join(ids), max_results=len(ids)))
root = ET.fromstring(urllib.request.urlopen(url, timeout=90).read())
rows = []
for e in root.findall('a:entry', NS):
    g = lambda t: ' '.join(((e.find(t, NS).text if e.find(t, NS) is not None else '') or '').split())
    rows.append('\t'.join([g('a:id').rsplit('/', 1)[-1], g('a:published')[:10], g('a:updated')[:10],
                           g('a:title'), g('x:comment'), g('x:journal_ref')]))
open(out, 'w').write('\n'.join(rows) + '\n'); print('\n'.join(rows))
