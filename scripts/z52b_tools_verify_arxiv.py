#!/usr/bin/env python3
"""Fetch arXiv titles (via arxiv.org/abs pages; export API is rate-limited) for arXiv ids cited in
data/z52b/tools.jsonl, or for ids given on the command line. Output: id<TAB>title, for eyeballing."""
import json, re, sys, time, urllib.request, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "data/z52b/tools_arxiv_titles.tsv")
ids = sys.argv[1:]
if not ids:
    for line in open(os.path.join(ROOT, "data/z52b/tools.jsonl")):
        for r in json.loads(line)["refs"]:
            for m in re.findall(r"arXiv:(\d{4}\.\d{4,5})", r):
                if m not in ids:
                    ids.append(m)
done = {}
if os.path.exists(CACHE):
    for l in open(CACHE):
        i, t = l.rstrip("\n").split("\t", 1)
        done[i] = t
for i in ids:
    if i in done:
        print(f"{i}\t{done[i]}")
        continue
    req = urllib.request.Request(f"https://arxiv.org/abs/{i}", headers={"User-Agent": "Mozilla/5.0 z52b-verify"})
    try:
        page = urllib.request.urlopen(req, timeout=30).read().decode("utf8", "replace")
        m = re.search(r"<title>(.*?)</title>", page, re.S)
        t = html.unescape(" ".join(m.group(1).split())) if m else "?"
    except Exception as e:
        t = f"ERROR {e}"
    print(f"{i}\t{t}", flush=True)
    if not t.startswith("ERROR"):
        with open(CACHE, "a") as fh:
            fh.write(f"{i}\t{t}\n")
    time.sleep(1.5)
