# AI06 · Tool, workflow, agent và cách kiểm một ứng dụng AI

[Mục lục](../README.md) · [Bài trước](05-embedding-rag.md) · [Bài tổng hợp](../MINI_LAB.md)

**Mục tiêu:** phân biệt model đề xuất hành động với code thực thi và kiểm quyền. **Thời lượng đọc:** khoảng 20 phút.

## Các lớp của hệ thống

| Concept | Cách hiểu |
| --- | --- |
| Tool/function calling | Model có thể trả yêu cầu gọi tool cùng arguments; ứng dụng quyết định có thực thi và thực thi thế nào |
| Workflow | Trình tự/nhánh chính được code định trước |
| Agent | Model quyết định một phần bước đi/tool dựa trên trạng thái và quan sát |
| Loop | Lặp quan sát → quyết định → hành động → nhận kết quả cho tới điều kiện dừng |
| Harness | Runtime bao quanh: context/state, kiểm arguments/quyền, chạy tool, trace, budget và điều kiện dừng |
| MCP | Giao thức kết nối ứng dụng AI với tool/resource và các thành phần liên quan; không tự thay thế policy truy cập |

Agent là một cách tổ chức ứng dụng, không mặc định là model thông minh hơn. Dùng workflow khi các bước đã rõ; chỉ thêm quyết định động khi có lý do và đo được lợi ích.

## Ví dụ bộ thực thi tool có giới hạn

```python
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
```

[File chạy được](../examples/ai06.py). Đây là demo harness/tool executor, **chưa phải agent có model**. Allowlist không thay thế authorization theo user/tài nguyên trong ứng dụng nhiều người dùng; ví dụ chỉ có dữ liệu fixture một người dùng.

## Khi thêm AI vào thật

- Giữ giới hạn bước, thời gian và chi phí; có điều kiện dừng khi thiếu dữ kiện hoặc tool lỗi.
- Thao tác ghi cần quyền, xác nhận phù hợp và chống lặp effect khi retry/resume. Tool output là dữ liệu, không tự cấp quyền mới.
- Dùng cùng task set để so agent với workflow đơn giản. Đo task success, lỗi, latency, cost và số lần cần người hỗ trợ.
- Ghi model/prompt/data version; kiểm ca sai input, thiếu nguồn, vượt quyền và lặp hành động. Không kết luận từ một demo thuận lợi.

## Tự kiểm

1. Model trả `delete_note` có nghĩa chương trình phải chạy không?
2. MCP có tự giải quyết quyền xem mọi note không?
3. Tool timeout rồi retry có bảo đảm không ghi hai lần không?

<details>
<summary>Đáp án ngắn</summary>

1. Không; ứng dụng kiểm tool, arguments, quyền và scope. 2. Không. 3. Không; cần contract idempotency hoặc cơ chế đối chiếu phù hợp với tác động.

</details>

**Bài tập 15 phút:** thử tool name lạ, thiếu note_id, ID không tồn tại và budget bằng 0. Với mỗi ca, ghi expected và giải thích vì sao nó phải bị chặn/dừng.

**Nguồn:** [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents), [MCP Architecture](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture). Đi sâu theo [D.4–D.5](../../../ROADMAP.md#d-4).
