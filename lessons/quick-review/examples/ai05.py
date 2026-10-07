# Example from ai/05-embedding-rag.md; keep in sync with the lesson.
from math import isclose, sqrt

def cosine(left, right):
    if len(left) != len(right):
        raise ValueError("dimensions must match")
    norm_left = sqrt(sum(x * x for x in left))
    norm_right = sqrt(sum(x * x for x in right))
    if norm_left == 0 or norm_right == 0:
        raise ValueError("zero vectors have no cosine direction")
    return sum(x * y for x, y in zip(left, right)) / (norm_left * norm_right)

vectors = {"note-python": [1, 0], "note-sql": [0, 1]}
query = [1, 0]
ranked = sorted(vectors, key=lambda key: cosine(query, vectors[key]), reverse=True)
assert ranked == ["note-python", "note-sql"]
assert isclose(cosine([1, 1], [1, 0]), 1 / sqrt(2))
try:
    cosine([0, 0], [1, 0])
except ValueError:
    print("AI05 OK: ranking demonstrated; zero vector rejected")
else:
    raise AssertionError("zero vector must be rejected")
