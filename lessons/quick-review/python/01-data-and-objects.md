# P01 · Dữ liệu, collection và object

[Mục lục](../README.md) · [Bài sau](02-functions-and-contracts.md)

**Mục tiêu:** đọc code và dự đoán được dữ liệu nào thay đổi. **Thời lượng đọc:** khoảng 15 phút.

## Kiến thức cần nhớ

Tên biến được gắn với object. Phép `b = a` không sao chép object: hai tên có thể cùng trỏ tới một list. Khi đó `append` sửa list chung; gán `b = []` chỉ đổi object mà tên `b` tham chiếu.

| Kiểu/concept | Cách hiểu và lúc dùng |
| --- | --- |
| `int`, `float`, `bool`, `str`, `None` | Số nguyên, số gần đúng, đúng/sai, văn bản và giá trị biểu diễn chưa có dữ liệu |
| `list` | Dãy có thứ tự, sửa được; dùng khi cần giữ thứ tự các bản ghi |
| `tuple` | Dãy không gán lại được phần tử; object mutable nằm bên trong vẫn có thể bị sửa |
| `dict` | Tra cứu theo key; key cần hashable, value có thể là object bất kỳ |
| `set` | Tập phần tử hashable không trùng; không dùng thứ tự duyệt làm contract |
| `if`, `for`, `while` | Chọn nhánh, duyệt iterable, lặp theo điều kiện; luôn xác định trường hợp dừng |
| Slicing/comprehension | Lấy đoạn hoặc biến đổi/lọc collection khi biểu thức vẫn dễ đọc |
| `==` / `is` | So bằng nhau theo hành vi của kiểu / kiểm cùng một object; thường dùng `is None` |

`if value` kiểm truthiness: `0`, `False`, chuỗi/list rỗng và `None` đều falsy. Nếu số 0 là dữ liệu hợp lệ, đừng dùng truthiness để kết luận “không có giá trị”. Copy nông chỉ tạo container ngoài mới; copy sâu xử lý cả các object lồng bên trong phù hợp cơ chế copy của kiểu.

## Đọc và dự đoán trước khi chạy

```python
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
```

[File chạy được](../examples/p01.py). `original` bị đổi vì `shallow["tags"]` vẫn là list cũ; `deep` giữ list riêng trong ví dụ này.

## Lỗi dễ gặp

- Gán `result = items.sort()`: `sort()` sửa list tại chỗ và trả `None`; `sorted(items)` trả list mới.
- Dùng `is` so chuỗi/số vì tình cờ thấy đúng trên vài input.
- Dùng `dict.copy()` rồi tưởng dữ liệu lồng đã độc lập hoàn toàn.
- Coi `float` là biểu diễn chính xác mọi số thập phân; cần chọn cách biểu diễn phù hợp nếu contract đòi độ chính xác thập phân.

## Tự kiểm

1. Nếu chạy `alias = {}`, `original` có đổi không?
2. Khi nào chọn dict thay cho list để tìm bản ghi theo ID?
3. `if not minutes` có phân biệt 0 với None không?

<details>
<summary>Đáp án ngắn</summary>

1. Không; chỉ gắn lại tên `alias`. 2. Khi cần mapping ID → record; phải quyết định rõ ID trùng xử lý thế nào. 3. Không, cả hai đều falsy; dùng kiểm tra tường minh theo contract.

</details>

**Bài tập 10 phút:** viết `unique_names(rows)` trả danh sách tên đã trim, bỏ rỗng và loại trùng nhưng giữ thứ tự xuất hiện; input không bị sửa. Thử input rỗng và tên lặp sau trim.

**Đọc thêm đúng phần:** [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html), [copy](https://docs.python.org/3/library/copy.html). Đi sâu theo [A.1](../../../ROADMAP.md#a-1).
