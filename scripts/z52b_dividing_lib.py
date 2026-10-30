"""Helper for lane `dividing` (wave z52b). Items are defined in scripts/z52b_dividing_batch*.py."""
ITEMS = []

def I(title, connection, why, first_step, refs=(), tags=(), conf="med", effort="cheap"):
    assert conf in ("low", "med", "high") and effort in ("cheap", "medium", "big")
    ITEMS.append(dict(title=title, connection=connection, why=why, first_step=first_step,
                      refs=list(refs), tags=list(tags), confidence_not_nonsense=conf, effort=effort))

def C(problem, E, obst, status, mech, why, first_step, refs=(), tags=(), conf="high", effort="cheap"):
    """Catalog entry for the dividing-line table."""
    out = status.split(";")[0].strip()
    I(f"Catalog: {problem}",
      f"{problem} ↔ ES as a small-count existence problem. Expected witnesses/n: {E}. Obstruction: {obst}. "
      f"Status: {status}. Mechanism: {mech}.",
      why, first_step, refs, ["catalog", *tags], conf, effort)
