# Example from python/02-functions-and-contracts.md; keep in sync with the lesson.
def add_session(minutes: int, history: list[int] | None = None) -> list[int]:
    # Contract: nhận int dương; không nhận bool; không sửa history.
    if type(minutes) is not int:
        raise TypeError("minutes must be an integer, excluding bool")
    if minutes <= 0:
        raise ValueError("minutes must be positive")
    previous = [] if history is None else history
    return [*previous, minutes]

old = [20]
assert add_session(15, old) == [20, 15]
assert old == [20]
assert add_session(5) == [5]
assert add_session(10) == [10]
try:
    add_session(True)
except TypeError:
    print("P02 OK: rejected bool, original unchanged")
else:
    raise AssertionError("bool must be rejected")
