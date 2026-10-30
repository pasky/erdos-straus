#!/usr/bin/env python3
"""Build data/z52b/free_fable.jsonl from data/z52b/free_fable_parts/*.jsonl and render BRAINSTORM/z52b_free_fable.md.

Each part file holds one JSON object per line (without ids, or with ids that will be overwritten).
Ids are assigned sequentially: free_fable-0001, ...
"""
import glob, json, os, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = sorted(glob.glob(os.path.join(ROOT, "data/z52b/free_fable_parts/*.jsonl")))
OUT = os.path.join(ROOT, "data/z52b/free_fable.jsonl")
MD = os.path.join(ROOT, "BRAINSTORM/z52b_free_fable.md")
HEADER = os.path.join(ROOT, "data/z52b/free_fable_parts/HEADER.md")
TOP = os.path.join(ROOT, "data/z52b/free_fable_parts/TOP.md")

REQ = ["title", "connection", "why", "first_step", "refs", "tags", "confidence_not_nonsense", "effort"]
items = []
titles = set()
for part in PARTS:
    with open(part) as f:
        for ln, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except Exception as e:
                sys.exit(f"{part}:{ln}: bad json: {e}")
            for k in REQ:
                if k not in o:
                    sys.exit(f"{part}:{ln}: missing {k}")
            assert o["confidence_not_nonsense"] in ("low", "med", "high"), (part, ln)
            assert o["effort"] in ("cheap", "medium", "big"), (part, ln)
            t = o["title"].strip().lower()
            if t in titles:
                print(f"WARNING duplicate title {part}:{ln}: {o['title']}", file=sys.stderr)
            titles.add(t)
            items.append(o)

for i, o in enumerate(items, 1):
    o["id"] = f"free_fable-{i:04d}"

with open(OUT, "w") as f:
    for o in items:
        f.write(json.dumps({"id": o["id"], **{k: o[k] for k in REQ}}, ensure_ascii=False) + "\n")

tagc = collections.Counter(t for o in items for t in o["tags"])
conf = collections.Counter(o["confidence_not_nonsense"] for o in items)
eff = collections.Counter(o["effort"] for o in items)

lines = []
lines.append("# z52b — lane free_fable: unpigeonholed free association for Erdős–Straus\n")
lines.append("**ES is OPEN.** Nothing here proves anything; these are candidate *connections* (breadth-first, nonsense-filter only).\n")
lines.append(f"**Item count: {len(items)}.** Confidence: {dict(conf)}. Effort: {dict(eff)}.\n")
lines.append("Data: `data/z52b/free_fable.jsonl` (rendered by `scripts/z52b_free_fable_build.py`).\n")
if os.path.exists(TOP):
    lines.append(open(TOP).read().rstrip() + "\n")
lines.append("\n## Tag histogram (top 60)\n")
lines.append(", ".join(f"`{t}`:{c}" for t, c in tagc.most_common(60)) + "\n")
if os.path.exists(HEADER):
    lines.append("\n" + open(HEADER).read().rstrip() + "\n")
lines.append("\n## Items\n")
for i, o in enumerate(items, 1):
    seen = [t for t in o["tags"] if t.startswith("seen:")]
    tagtxt = " ".join(f"`{t}`" for t in o["tags"] if not t.startswith("seen:"))
    seentxt = (" (" + ", ".join(seen) + ")") if seen else ""
    lines.append(
        f"{i}. **{o['title']}** [{o['confidence_not_nonsense']}/{o['effort']}] — {o['connection']} "
        f"*Why:* {o['why']} *First step:* {o['first_step']}"
        + (f" *Refs:* {'; '.join(o['refs'])}" if o["refs"] else "")
        + f" {tagtxt}{seentxt}\n"
    )
with open(MD, "w") as f:
    f.write("\n".join(lines))
print(f"{len(items)} items -> {OUT}, {MD}")
print("top tags:", tagc.most_common(25))
