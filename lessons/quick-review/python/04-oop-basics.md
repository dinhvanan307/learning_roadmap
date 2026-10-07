# P04 · Class, object và OOP trong Python

[Mục lục](../README.md) · [Bài trước](03-modules-files-errors.md) · [Bài sau](05-oop-design.md)

**Mục tiêu:** gắn dữ liệu và hành vi đúng chỗ, hiểu object đang giữ state gì. **Thời lượng đọc:** khoảng 20 phút.

## Kiến thức cần nhớ

Class định nghĩa một kiểu cùng hành vi; instance là object cụ thể của kiểu đó. `self` là tham số nhận instance trong instance method. Gọi `obj.method(x)` cung cấp instance cho method. `__init__` khởi tạo trạng thái sau khi instance được tạo; không phải phương thức trả về instance mới.

| Thành phần | Vai trò |
| --- | --- |
| Instance attribute | Dữ liệu thuộc từng object, ví dụ danh sách tag của một note |
| Class attribute | Dữ liệu được tra ở class, có thể dùng chung; cẩn thận collection mutable |
| Instance method | Làm việc với `self`, đọc/sửa trạng thái của instance |
| `@classmethod` | Nhận `cls`; hữu ích cho constructor thay thế như `from_dict` |
| `@staticmethod` | Không tự nhận `self`/`cls`; hàm tiện ích liên quan class, đôi khi hàm module rõ hơn |
| Dunder | `__repr__`, `__eq__`, `__len__`… nối object vào protocol của Python |
| `dataclass` | Sinh mã thường lặp lại cho class dữ liệu; không tự validate mọi field |

## Ví dụ

```python
from dataclasses import dataclass, field

@dataclass
class StudyNote:
    title: str
    tags: list[str] = field(default_factory=list)

    def add_tag(self, tag: str) -> None:
        if not isinstance(tag, str) or not tag.strip():
            raise ValueError("tag must be non-empty text")
        normalized = tag.strip()
        if normalized not in self.tags:
            self.tags.append(normalized)

    @classmethod
    def from_title(cls, title: str) -> "StudyNote":
        return cls(title=title.strip())

first = StudyNote.from_title("  Python  ")
second = StudyNote("OOP")
first.add_tag("language")
assert first.tags == ["language"]
assert second.tags == []
assert first == StudyNote("Python", ["language"])
assert first is not StudyNote("Python", ["language"])
print("P04 OK:", first)
```

[File chạy được](../examples/p04.py). `default_factory=list` tạo list riêng cho từng instance. `dataclass` ở đây sinh `__init__`, `__repr__` và so sánh theo field. Ví dụ giả định title từ nội bộ; nếu nhận input ngoài, thêm validation title rõ ràng.

## Lỗi dễ gặp

- Đặt `tags = []` ở class thường rồi mọi instance cùng append vào list chung.
- Tưởng `dataclass` sẽ từ chối `StudyNote(123)` chỉ vì annotation là `str`.
- Tạo class cho mọi hàm dù không có state, invariant hay giao diện cần gom lại.
- Hiểu `frozen=True` là bất biến sâu: field chứa list vẫn có thể có nội dung mutable.

## Tự kiểm

1. `first == second` và `first is second` hỏi hai điều gì khác nhau?
2. Vì sao method thêm tag cần self nhưng `from_title` nhận cls?
3. Khi nào dict đã đủ thay vì dataclass?

<details>
<summary>Đáp án ngắn</summary>

1. So giá trị theo `__eq__` / cùng instance. 2. Một method thao tác instance đã có; method kia tạo instance qua class được gọi. 3. Dữ liệu ad hoc hoặc ở boundary JSON đơn giản; dùng class khi tên field, hành vi và contract đem lại sự rõ ràng.

</details>

**Bài tập 15 phút:** thêm method `rename` từ chối tên rỗng, test hai note không chia sẻ tags và giải thích invariant của class.

**Nguồn:** [Python Classes](https://docs.python.org/3/tutorial/classes.html), [dataclasses](https://docs.python.org/3/library/dataclasses.html). Đi sâu theo [A.2](../../../ROADMAP.md#a-2).
