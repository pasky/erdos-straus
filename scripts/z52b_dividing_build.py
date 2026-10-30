"""Build data/z52b/dividing.jsonl and the item list of BRAINSTORM/z52b_dividing.md from batch files.
Usage: uv run python scripts/z52b_dividing_build.py   (header lives in scripts/z52b_dividing_header.md)"""
import importlib, json, sys, os, collections
sys.path.insert(0, os.path.dirname(__file__))
import z52b_dividing_lib as L

batches = sorted(f[:-3] for f in os.listdir(os.path.dirname(__file__)) if f.startswith("z52b_dividing_batch") and f.endswith(".py"))
batches.sort(key=lambda s: int(s.replace("z52b_dividing_batch", "")))
for b in batches:
    importlib.import_module(b)
seen = set()
for i, it in enumerate(L.ITEMS, 1):
    key = it["title"].lower()
    assert key not in seen, f"duplicate title: {it['title']}"
    seen.add(key)
    it["id"] = f"dividing-{i:04d}"
root = os.path.join(os.path.dirname(__file__), "..")
with open(os.path.join(root, "data/z52b/dividing.jsonl"), "w") as f:
    for it in L.ITEMS:
        f.write(json.dumps({k: it[k] for k in ["id", "title", "connection", "why", "first_step", "refs", "tags",
                                               "confidence_not_nonsense", "effort"]}, ensure_ascii=False) + "\n")
hdr = open(os.path.join(os.path.dirname(__file__), "z52b_dividing_header.md")).read()
tags = collections.Counter(t.split(":")[0] if t.split(":")[0] in ("seen",) else t for it in L.ITEMS for t in it["tags"])
hist = ", ".join(f"{t} ({c})" for t, c in tags.most_common() if c >= 3)
hdr = hdr.replace("{{COUNT}}", str(len(L.ITEMS))).replace("{{HIST}}", hist)
lines = [hdr, "\n## Items\n"]
for it in L.ITEMS:
    lines.append(f"{int(it['id'][-4:])}. **{it['title']}** [{', '.join(it['tags'])}; conf {it['confidence_not_nonsense']}, {it['effort']}] — "
                 f"{it['connection']} — *First step:* {it['first_step']}")
open(os.path.join(root, "BRAINSTORM/z52b_dividing.md"), "w").write("\n".join(lines) + "\n")
print(len(L.ITEMS), "items")
