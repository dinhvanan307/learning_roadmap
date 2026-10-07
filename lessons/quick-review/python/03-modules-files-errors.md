# P03 · Module, file và exception

[Mục lục](../README.md) · [Bài trước](02-functions-and-contracts.md) · [Bài sau](04-oop-basics.md)

**Mục tiêu:** tổ chức luồng đọc → kiểm → xử lý để lỗi không biến mất. **Thời lượng đọc:** khoảng 15 phút.

## Kiến thức cần nhớ

Module là đơn vị import, thường là một file `.py`; package tổ chức các module dưới một namespace. Với package thông thường, `__init__.py` đánh dấu thư mục package; Python cũng có namespace package không cần file này. Import thực thi phần top-level khi module được nạp lần đầu trong tình huống thông thường. Dùng `if __name__ == "__main__":` để tách việc chạy script khỏi định nghĩa có thể import.

Trong ứng dụng nhỏ, tách hàm đọc file, hàm validate và hàm xử lý là đủ. Logic thuần nhận dữ liệu đã đọc nên dễ test bằng fixture, không cần file thật trong mọi test.

| Lỗi | Ý nghĩa thường gặp | Cách xử lý ở boundary |
| --- | --- | --- |
| `FileNotFoundError` | Không tìm được đường dẫn | Báo đúng file đang cần, không trả dữ liệu giả |
| `JSONDecodeError` | Nội dung không parse được thành JSON | Giữ thông tin lỗi cú pháp |
| `ValueError` | Dữ liệu parse được nhưng không đáp ứng contract | Chỉ rõ field/quy tắc bị vi phạm |

## Ví dụ file tạm, chạy không làm bẩn repo

```python
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
```

[File chạy được](../examples/p03.py). `with` gọi cleanup khi rời block, kể cả do exception. Không cần tự `close()` ở từng nhánh.

## Lỗi dễ gặp

- Relative path được hiểu theo working directory; không nhất thiết theo thư mục chứa file code.
- `except Exception: pass` xóa dấu hiệu thất bại. Chỉ bắt lỗi ở nơi thực sự biết cách xử lý.
- Log cả dữ liệu nhạy cảm hoặc secret để debug.
- Mở network/file ngay lúc import khiến test/import có side effect ngoài ý muốn.

## Tự kiểm

1. File là JSON hợp lệ nhưng title sai kiểu thì lỗi parse hay validation?
2. Có cần bắt mọi exception bên trong `read_title` không?
3. Đọc file JSON lớn có tự streaming từng record không?

<details>
<summary>Đáp án ngắn</summary>

1. Validation. 2. Không; để lỗi truyền tới boundary biết cách báo hoặc phục hồi. 3. Không; `json.load` đọc để dựng object, cần chọn định dạng/cách đọc khác khi muốn xử lý từng record.

</details>

**Bài tập 15 phút:** bổ sung ca file thiếu, JSON sai cú pháp và title chỉ có dấu cách. Ghi riêng expected cho từng loại lỗi.

**Nguồn:** [Modules](https://docs.python.org/3/tutorial/modules.html), [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html), [JSON](https://docs.python.org/3/library/json.html). Đi sâu theo [A.1–A.2](../../../ROADMAP.md#a-1).
