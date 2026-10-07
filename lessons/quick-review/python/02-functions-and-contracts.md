# P02 · Hàm, scope, typing và contract

[Mục lục](../README.md) · [Bài trước](01-data-and-objects.md) · [Bài sau](03-modules-files-errors.md)

**Mục tiêu:** viết hàm có đầu vào, đầu ra và hành vi lỗi rõ ràng. **Thời lượng đọc:** khoảng 15 phút.

## Kiến thức cần nhớ

Contract trả lời: nhận dữ liệu gì, trả kết quả gì, có sửa input không và báo lỗi thế nào. Viết contract trước giúp chọn test; tên hàm và type hint chỉ mô tả một phần contract.

| Concept | Điều cần nhớ |
| --- | --- |
| Argument/parameter | Giá trị truyền khi gọi / tên tham số trong định nghĩa |
| Positional/keyword | Truyền theo vị trí / theo tên; `*` trong chữ ký có thể buộc phần sau dùng keyword |
| `*args`, `**kwargs` | Thu nhiều positional/keyword arguments; chỉ dùng khi cần giao diện linh hoạt |
| `return` | Trả kết quả và kết thúc hàm; đi hết hàm không return thì trả None |
| Scope | Tên được tra theo local → enclosing → global → builtins trong trường hợp thông thường |
| Default argument | Được tính khi định nghĩa hàm; list/dict mặc định có thể bị dùng chung giữa các lần gọi |
| Type hints | Giúp người đọc và công cụ kiểm kiểu; không tự chặn dữ liệu sai lúc chạy |
| Pure function | Kết quả phụ thuộc input, không có side effect quan sát được; thường dễ kiểm thử |

## Ví dụ: thêm một buổi học

```python
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
```

[File chạy được](../examples/p02.py). `bool` là subclass của `int`, nên `isinstance(True, int)` là True. Ví dụ chọn kiểm exact type để thực hiện contract này; đó không phải quy tắc bắt buộc cho mọi hàm. `history` được giả định là list số phút đã hợp lệ trong nội bộ; boundary nhận dữ liệu ngoài cần kiểm riêng.

## Lỗi dễ gặp

- `def f(items=[])`: sửa list mặc định rồi dữ liệu rò sang lần gọi sau.
- Tin annotation `minutes: int` sẽ tự raise khi truyền chuỗi.
- Nuốt mọi exception và trả `[]`, khiến người gọi không phân biệt dữ liệu rỗng với xử lý thất bại.
- Sửa tham số list tại chỗ trong hàm được mô tả là “tạo bản mới”.

## Tự kiểm

1. Vì sao dùng None làm default thay vì `[]`?
2. `ValueError` khác `TypeError` trong ví dụ ở đâu?
3. Làm sao biết test không chỉ lặp lại chính cách hàm tính kết quả?

<details>
<summary>Đáp án ngắn</summary>

1. Mỗi lần gọi tự tạo list mới khi cần. 2. Sai loại dữ liệu / đúng loại nhưng giá trị ngoài contract. 3. Chốt expected từ ví dụ nhỏ và quy tắc nghiệp vụ trước, không gọi lại hàm đang kiểm để tính expected.

</details>

**Bài tập 15 phút:** thêm keyword-only `limit` cho số phút tối đa; nêu hành vi với số 0, bool, vượt limit và history rỗng. Viết expected trước code.

**Nguồn:** [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions), [typing](https://docs.python.org/3/library/typing.html). Đi sâu theo [A.1–A.2](../../../ROADMAP.md#a-1).
