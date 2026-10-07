# Example from ai/06-tools-agents.md; keep in sync with the lesson.
notes = {"n1": "Python lists are mutable."}

def execute_tool(name, arguments):
    if name != "read_note":
        raise PermissionError("tool not allowed")
    if not isinstance(arguments, dict) or set(arguments) != {"note_id"}:
        raise ValueError("expected only note_id")
    note_id = arguments["note_id"]
    if not isinstance(note_id, str):
        raise TypeError("note_id must be text")
    if note_id not in notes:
        raise LookupError("unknown note")
    return notes[note_id]

# Đề xuất cố định để học cơ chế; không phải output của LLM.
proposals = [
    ("read_note", {"note_id": "n1"}),
    ("delete_note", {"note_id": "n1"}),
    ("read_note", {"note_id": "n1"}),
]
trace = []
for step, (name, args) in enumerate(proposals):
    if step >= 2:  # Ngân sách ở demo đếm cả lần thử bị từ chối.
        trace.append("budget_stop")
        break
    try:
        trace.append(execute_tool(name, args))
    except (PermissionError, ValueError, TypeError, LookupError) as error:
        trace.append(type(error).__name__)
assert trace == [notes["n1"], "PermissionError", "budget_stop"]
assert "n1" in notes
print("AI06 OK:", trace)
