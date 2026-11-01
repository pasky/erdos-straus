"""Z0615 (pass 2, SK0): feature matrix from data/z52b/dividing.jsonl tags; depth-<=3 decision tree predicting the
recorded outcome tag. Features exclude outcome:* tags. Items with no outcome tag are dropped. Leave-one-out-free: 5-fold CV."""
import json, collections
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import cross_val_score
R = [json.loads(l) for l in open('data/z52b/dividing.jsonl')]
outs = lambda r: [t.split(':', 1)[1] for t in r.get('tags', []) if t.startswith('outcome:')]
rows = [(r, outs(r)) for r in R]
rows = [(r, o[0]) for r, o in rows if len(o) == 1]
allt = collections.Counter(t for r, _ in rows for t in r['tags'] if not t.startswith('outcome:'))
feats = sorted(t for t, c in allt.items() if c >= 5)
X = [[1 if t in r['tags'] else 0 for t in feats] for r, _ in rows]
y = [o for _, o in rows]
print("items with exactly one outcome tag:", len(rows), "features (>=5 uses):", len(feats))
print("outcome counts:", collections.Counter(y).most_common())
base = max(collections.Counter(y).values()) / len(y)
clf = DecisionTreeClassifier(max_depth=3, random_state=0)
cv = cross_val_score(clf, X, y, cv=5)
print("majority baseline:", round(base, 3), "depth-3 tree 5-fold CV accuracy:", round(cv.mean(), 3), [round(c, 3) for c in cv])
clf.fit(X, y)
print(export_text(clf, feature_names=feats, max_depth=3))
