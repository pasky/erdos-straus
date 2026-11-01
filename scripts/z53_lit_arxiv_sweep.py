#!/usr/bin/env python3
"""z53 LIT: systematic arXiv API sweep.

Usage: uv run python scripts/z53_lit_arxiv_sweep.py QUERYFILE OUT.tsv [--since YYYY]
QUERYFILE: one line per query, "area<TAB>arxiv search_query string" (API syntax, e.g. abs:"modular hyperbola").
Writes TSV: area, query, id, version, published, updated, in_repo, title, authors, abstract(400 chars).
Only entries published >= since (default 2020) are kept. Sleeps 3 s between requests (arXiv API etiquette).
"""
import sys, time, urllib.request, urllib.parse, xml.etree.ElementTree as ET, re, os

NS = {"a": "http://www.w3.org/2005/Atom"}
REPO_IDS = set(open(os.path.join(os.path.dirname(__file__), "..", "data", "z53", "lit", "repo_arxiv_ids.txt")).read().split())


def fetch(q, start=0, n=100):
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "start": start, "max_results": n, "sortBy": "submittedDate", "sortOrder": "descending"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read()
        except Exception as e:  # noqa
            print("retry", q, e, file=sys.stderr)
            time.sleep(10)
    raise SystemExit("arXiv API failed for " + q)


def main():
    qfile, out = sys.argv[1], sys.argv[2]
    since = int(sys.argv[sys.argv.index("--since") + 1]) if "--since" in sys.argv else 2020
    seen = {}
    with open(qfile) as f:
        queries = [l.rstrip("\n").split("\t", 1) for l in f if l.strip() and not l.startswith("#")]
    rows = []
    for area, q in queries:
        data = fetch(q)
        root = ET.fromstring(data)
        k = 0
        for e in root.findall("a:entry", NS):
            full = e.find("a:id", NS).text.rsplit("/abs/", 1)[1]
            m = re.match(r"(.*?)(v\d+)$", full)
            aid, ver = (m.group(1), m.group(2)) if m else (full, "")
            pub = e.find("a:published", NS).text[:10]
            upd = e.find("a:updated", NS).text[:10]
            if int(pub[:4]) < since:
                continue
            title = " ".join(e.find("a:title", NS).text.split())
            auth = ", ".join(a.find("a:name", NS).text for a in e.findall("a:author", NS))
            abst = " ".join(e.find("a:summary", NS).text.split())[:400]
            key = aid
            k += 1
            if key in seen:
                continue
            seen[key] = 1
            rows.append([area, q, aid, ver, pub, upd, "REPO" if aid in REPO_IDS else "new", title, auth, abst])
        print(f"{area}\t{q}\t{k} hits", file=sys.stderr)
        time.sleep(3)
    with open(out, "w") as f:
        f.write("area\tquery\tid\tversion\tpublished\tupdated\tin_repo\ttitle\tauthors\tabstract\n")
        for r in rows:
            f.write("\t".join(x.replace("\t", " ") for x in r) + "\n")
    print(len(rows), "unique rows", file=sys.stderr)


if __name__ == "__main__":
    main()
