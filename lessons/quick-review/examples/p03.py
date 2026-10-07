# Example from python/03-modules-files-errors.md; keep in sync with the lesson.
import json
from pathlib import Path
from tempfile import TemporaryDirectory

def read_title(path: Path) -> str:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict) or not isinstance(data.get("title"), str):
        raise ValueError("title must be a string in a JSON object")
    title = data["title"].strip()
    if not title:
        raise ValueError("title must not be empty")
    return title

with TemporaryDirectory() as directory:
    path = Path(directory) / "note.json"
    path.write_text('{"title": "  Python  "}', encoding="utf-8")
    assert read_title(path) == "Python"
    path.write_text('{"title": 123}', encoding="utf-8")
    try:
        read_title(path)
    except ValueError as error:
        print("P03 OK:", error)
    else:
        raise AssertionError("invalid title accepted")
