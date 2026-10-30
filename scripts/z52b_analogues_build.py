#!/usr/bin/env python3
"""Build data/z52b/analogues.jsonl and BRAINSTORM/z52b_analogues.md from batch modules.

Batch modules scripts/z52b_analogues_bNN.py each define ITEMS = [T(...), ...].
Order of batches (and of items within) fixes the ids, so only ever append.
"""
import glob, importlib.util, json, os, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "analogues"


def load():
    items = []
    for f in sorted(glob.glob(os.path.join(ROOT, "scripts", "z52b_analogues_b[0-9][0-9].py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        for it in m.ITEMS:
            it["_batch"] = os.path.basename(f)
            items.append(it)
    return items


def main():
    items = load()
    seen_titles = {}
    out = []
    for i, it in enumerate(items, 1):
        t = it["title"].strip()
        if t.lower() in seen_titles:
            sys.exit(f"duplicate title: {t} ({it['_batch']} vs {seen_titles[t.lower()]})")
        seen_titles[t.lower()] = it["_batch"]
        assert it["conf"] in ("low", "med", "high"), it
        assert it["effort"] in ("cheap", "medium", "big"), it
        out.append(dict(
            id=f"{SLUG}-{i:04d}", title=t, connection=it["connection"].strip(), why=it["why"].strip(),
            first_step=it["first_step"].strip(), refs=it["refs"], tags=it["tags"],
            confidence_not_nonsense=it["conf"], effort=it["effort"], world=it.get("world", "")))
    os.makedirs(os.path.join(ROOT, "data", "z52b"), exist_ok=True)
    with open(os.path.join(ROOT, "data", "z52b", f"{SLUG}.jsonl"), "w") as fh:
        for o in out:
            fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    # markdown
    hdr_path = os.path.join(ROOT, "scripts", "z52b_analogues_header.md")
    hdr = open(hdr_path).read() if os.path.exists(hdr_path) else ""
    tagc = collections.Counter(t for o in out for t in o["tags"])
    worldc = collections.Counter(o["world"] for o in out)
    lines = [hdr.rstrip(), "",
             f"## Statistics (auto-generated)", "",
             f"Items: **{len(out)}**. Confidence: " + ", ".join(
                 f"{k} {v}" for k, v in collections.Counter(o['confidence_not_nonsense'] for o in out).items())
             + ". Effort: " + ", ".join(f"{k} {v}" for k, v in collections.Counter(o['effort'] for o in out).items()) + ".", "",
             "Worlds (section → count): " + "; ".join(f"{k} {v}" for k, v in worldc.items()), "",
             "Tag histogram (tags used ≥ 4 times): " + ", ".join(f"`{t}` {c}" for t, c in tagc.most_common() if c >= 4), "",
             "## Items", ""]
    cur = None
    for o in out:
        if o["world"] != cur:
            cur = o["world"]
            lines += ["", f"### {cur}", ""]
        n = int(o["id"].split("-")[-1])
        lines.append(f"{n}. **{o['title']}** [`{o['id']}`; {o['confidence_not_nonsense']}/{o['effort']}] — "
                     f"{o['connection']} — *First step:* {o['first_step']}")
    with open(os.path.join(ROOT, "BRAINSTORM", f"z52b_{SLUG}.md"), "w") as fh:
        fh.write("\n".join(lines).lstrip() + "\n")
    print(len(out), "items;", len(tagc), "distinct tags")


if __name__ == "__main__":
    main()
