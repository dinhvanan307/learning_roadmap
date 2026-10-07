# Example from python/01-data-and-objects.md; keep in sync with the lesson.
from copy import deepcopy

original = {"tags": ["python"], "minutes": 0}
alias = original
shallow = original.copy()
deep = deepcopy(original)

shallow["tags"].append("oop")
assert original["tags"] == ["python", "oop"]
assert deep["tags"] == ["python"]
assert alias is original
assert shallow == original and shallow is not original

names = [" An ", "", " Binh "]
clean = [name.strip() for name in names if name.strip()]
assert clean == ["An", "Binh"]
assert original["minutes"] is not None
print("P01 OK:", clean, deep["tags"])
