#!/usr/bin/env python3
"""Build data/z52b/tools.jsonl and BRAINSTORM/z52b_tools.md from item batch files.

Items live in scripts/z52b_tools_items_*.py, each defining ITEMS = [I(...), ...].
`kw` (optional) is a keyword; if `git grep -il kw -- '*.md'` hits, the item gets a
`seen:<first file>` tag (cheap prior-art pointer, not a dedup decision).
"""
import glob, importlib.util, json, os, re, subprocess, collections, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "tools"


def load():
    items = []
    for f in sorted(glob.glob(os.path.join(ROOT, "scripts", "z52b_tools_items_*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        items.extend(m.ITEMS)
    return items


_seen_cache = {}


def seen(kw):
    if not kw:
        return []
    if kw in _seen_cache:
        return _seen_cache[kw]
    r = subprocess.run(["git", "grep", "-il", "--", kw, "--", "*.md"], cwd=ROOT,
                       capture_output=True, text=True, timeout=60)
    files = [x for x in r.stdout.split("\n") if x and not x.startswith("BRAINSTORM/z52b_")]
    # prefer BRAINSTORM memos, then top-level
    files.sort(key=lambda x: (x.endswith("README.md"), 0 if x.startswith("BRAINSTORM/") else 1 if "/" not in x else 2, x))
    out = ["seen:" + files[0]] if files else []
    _seen_cache[kw] = out
    return out


def main():
    items = load()
    titles = collections.Counter(i["title"].strip().lower() for i in items)
    dups = [t for t, c in titles.items() if c > 1]
    if dups:
        print("DUPLICATE TITLES:", dups, file=sys.stderr)
        sys.exit(1)
    out = []
    for k, it in enumerate(items, 1):
        d = dict(it)
        kw = d.pop("kw", None)
        d["tags"] = list(dict.fromkeys(d["tags"] + seen(kw)))
        d = {"id": f"{SLUG}-{k:04d}", **d}
        out.append(d)
    os.makedirs(os.path.join(ROOT, "data", "z52b"), exist_ok=True)
    with open(os.path.join(ROOT, "data", "z52b", f"{SLUG}.jsonl"), "w") as fh:
        for d in out:
            fh.write(json.dumps(d, ensure_ascii=False) + "\n")
    # markdown
    hdr_path = os.path.join(ROOT, "scripts", "z52b_tools_header.md")
    hdr = open(hdr_path).read() if os.path.exists(hdr_path) else ""
    tagc = collections.Counter(t for d in out for t in d["tags"] if not t.startswith("seen:"))
    nseen = sum(1 for d in out if any(t.startswith("seen:") for t in d["tags"]))
    conf = collections.Counter(d["confidence_not_nonsense"] for d in out)
    eff = collections.Counter(d["effort"] for d in out)
    lines = [hdr.replace("{{N}}", str(len(out))).rstrip(), "",
             f"**Stats.** {len(out)} items; confidence_not_nonsense {dict(conf)}; effort {dict(eff)}; "
             f"{nseen} items carry a `seen:` prior-art pointer.", "",
             "**Tag histogram (tags used ≥ 4 times).** " +
             ", ".join(f"{t} {c}" for t, c in tagc.most_common() if c >= 4), "",
             "## Items", ""]
    for k, d in enumerate(out, 1):
        lines.append(f"{k}. **{d['title']}** [{d['id']}; {d['confidence_not_nonsense']}/{d['effort']}] — "
                     f"{d['connection']} — *First step:* {d['first_step']}")
    with open(os.path.join(ROOT, "BRAINSTORM", f"z52b_{SLUG}.md"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print(len(out), "items;", nseen, "seen")


if __name__ == "__main__":
    main()
