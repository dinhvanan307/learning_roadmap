# Example from python/06-python-patterns.md; keep in sync with the lesson.
from contextlib import contextmanager
from functools import wraps
from io import StringIO

def traced(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("calling", function.__name__)
        return function(*args, **kwargs)
    return wrapper

@contextmanager
def text_source(text):
    handle = StringIO(text)
    try:
        yield handle
    finally:
        handle.close()

def nonempty_lines(handle):
    for line in handle:
        if line.strip():
            yield line.strip()

@traced
def read_titles(text):
    with text_source(text) as handle:
        titles = nonempty_lines(handle)
        result = list(titles)
        assert list(titles) == []
    assert handle.closed
    return result

assert read_titles("Python\n\nOOP\n") == ["Python", "OOP"]
assert read_titles.__name__ == "read_titles"
print("P06 OK")
