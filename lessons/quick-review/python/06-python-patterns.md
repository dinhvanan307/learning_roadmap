# P06 · Generator, closure, decorator và context manager

[Mục lục](../README.md) · [Bài trước](05-oop-design.md) · [Bài sau](07-async.md)

**Mục tiêu:** đọc được các cấu trúc Python thường gặp trong code thư viện. **Thời lượng đọc:** khoảng 20 phút.

## Phân biệt bốn cơ chế

| Concept | Cơ chế | Dùng khi |
| --- | --- | --- |
| Iterable / iterator | Iterable có thể cung cấp iterator; iterator trả từng phần tử qua next | Duyệt collection hoặc luồng dữ liệu |
| Generator | Hàm có yield tạo generator; thân hàm chạy khi bắt đầu duyệt và tiếp tục sau mỗi yield | Đọc/xử lý từng record |
| Closure | Hàm giữ khả năng truy cập biến ở scope bao ngoài | Tạo hàm với cấu hình đã gắn |
| Decorator | Nhận callable và trả callable/đối tượng thay thế; cú pháp `@d` áp dụng khi định nghĩa | Bọc logging, timing hoặc policy có chủ đích |
| Context manager | Giao thức vào/ra khối with; thường để quản lý vòng đời tài nguyên | File, lock, session hoặc context tạm |

Generator tiết kiệm phần dữ liệu chưa cần tạo; gọi `list(generator)` vẫn materialize toàn bộ. Một generator đã duyệt hết không tự khởi động lại. Closure thường tra biến khi hàm chạy, nên callback tạo trong vòng lặp có thể cùng đọc giá trị cuối nếu không bind riêng.

## Ví dụ ghép các cơ chế

```python
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
```

[File chạy được](../examples/p06.py). `wrapper` là closure giữ `function`; `wraps` bảo toàn metadata hữu ích. Khối finally đóng stream khi block thành công hoặc lỗi. Ví dụ này không nuốt exception.

## Lỗi dễ gặp

- Return generator đọc file ra ngoài khối with rồi mới duyệt, trong khi file đã đóng.
- Decorator quên `return`, làm kết quả hàm gốc biến thành None.
- Wrapper bắt mọi lỗi rồi bỏ qua, thay đổi contract mà caller không biết.
- Gọi `next()` sau khi iterator hết mà không xử lý `StopIteration` hoặc default phù hợp.

## Tự kiểm

1. Gọi `nonempty_lines(handle)` đã đọc xong stream chưa?
2. Vì sao result được tạo trong khối with?
3. Nếu decorator được áp dụng, exception của hàm gốc có tự mất không?

<details>
<summary>Đáp án ngắn</summary>

1. Chưa, mới tạo generator. 2. Cần duyệt khi stream còn mở. 3. Không; chỉ mất nếu wrapper bắt/biến đổi nó. Ví dụ để exception truyền lên bình thường.

</details>

**Bài tập 15 phút:** thêm một dòng dữ liệu khiến reader raise; chứng minh tài nguyên vẫn được đóng. Làm thêm factory `make_prefixer(prefix)` trả hàm thêm prefix để tự giải thích closure.

**Nguồn:** [Iterator types](https://docs.python.org/3/library/stdtypes.html#iterator-types), [contextlib](https://docs.python.org/3/library/contextlib.html), [functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps). Đi sâu theo [A.2](../../../ROADMAP.md#a-2).
