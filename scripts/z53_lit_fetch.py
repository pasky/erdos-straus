#!/usr/bin/env python3
"""z53 LIT: fetch arXiv PDFs + API metadata and extract text for theorem verification.

Usage: uv run --with pypdf python scripts/z53_lit_fetch.py ID [ID ...]
Writes /tmp/z53pdf/<ID>.pdf, <ID>.txt (pypdf text), <ID>.meta (version, dates, title, authors, abstract).
Text extraction is only an aid for locating statements; quotes in Z53_LIT.md were read off these texts.
"""
import sys, os, time, re, urllib.request
from pypdf import PdfReader

D = "/tmp/z53pdf"
os.makedirs(D, exist_ok=True)


def get(url, path):
    req = urllib.request.Request(url, headers={"User-Agent": "z53-lit-sweep (research; contact via arXiv API etiquette)"})
    with urllib.request.urlopen(req, timeout=90) as r, open(path, "wb") as f:
        f.write(r.read())


for aid in sys.argv[1:]:
    meta = os.path.join(D, aid + ".meta")
    if not os.path.exists(meta):
        get("https://export.arxiv.org/api/query?id_list=" + aid, meta + ".xml")
        x = open(meta + ".xml").read()
        e = re.search(r"<entry>(.*?)</entry>", x, re.S).group(1)
        g = lambda t: " ".join(re.search(rf"<{t}>(.*?)</{t}>", e, re.S).group(1).split())
        auth = ", ".join(re.findall(r"<name>(.*?)</name>", e))
        open(meta, "w").write(f"id: {g('id')}\npublished: {g('published')}\nupdated: {g('updated')}\ntitle: {g('title')}\nauthors: {auth}\nabstract: {g('summary')}\n")
        time.sleep(3)
    pdf = os.path.join(D, aid + ".pdf")
    if not os.path.exists(pdf):
        try:
            get("https://arxiv.org/pdf/" + aid, pdf)
        except Exception as ex:  # noqa
            print("PDF FAIL", aid, ex)
            continue
        time.sleep(3)
    txt = os.path.join(D, aid + ".txt")
    if not os.path.exists(txt):
        try:
            r = PdfReader(pdf)
            with open(txt, "w") as f:
                for i, pg in enumerate(r.pages):
                    f.write(f"\n=== PAGE {i+1} ===\n")
                    f.write(pg.extract_text() or "")
        except Exception as ex:  # noqa
            print("TEXT FAIL", aid, ex)
            continue
    print(aid, open(meta).read().splitlines()[0], "|", open(meta).read().splitlines()[3][:100])
