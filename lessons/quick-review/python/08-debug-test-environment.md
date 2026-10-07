# P08 · Debugging, testing và môi trường chạy

[Mục lục](../README.md) · [Bài trước](07-async.md) · [Sang AI cơ bản](../ai/01-ai-map.md)

**Mục tiêu:** biết code đúng vì đã kiểm điều gì. **Thời lượng đọc:** khoảng 15 phút.

## Một vòng debug ngắn

1. Tạo input nhỏ tái hiện lỗi; ghi expected và actual.
2. Đọc loại exception, thông báo và traceback, tìm frame code liên quan.
3. Đặt một giả thuyết; kiểm bằng dữ liệu/log hoặc debugger.
4. Sửa nguyên nhân, thêm regression test và chạy lại ca từng đúng.

Unit test kiểm logic nhỏ; integration test kiểm ranh giới thật như DB/API; E2E kiểm luồng người dùng. Fixture cung cấp dữ liệu/setup; fake là implementation nhẹ thay dependency ở boundary. Fake provider không chứng minh provider thật tương thích.

## Ví dụ test có thể phát hiện bug

```python
import unittest

def normalize_title(value):
    if not isinstance(value, str):
        raise TypeError("title must be text")
    result = value.strip()
    if not result:
        raise ValueError("title must not be empty")
    return result

class TitleTests(unittest.TestCase):
    def test_trims_whitespace(self):
        self.assertEqual(normalize_title("  Python  "), "Python")

    def test_rejects_blank(self):
        for value in ("", "   ", "\n"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    normalize_title(value)

    def test_rejects_wrong_type(self):
        for value in (None, 123, True):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    normalize_title(value)

if __name__ == "__main__":
    unittest.main(verbosity=2)
```

[File chạy được](../examples/p08.py). Kết quả mong đợi: ba test method pass. Nếu bỏ `.strip()`, test trim phải fail; đó là cách kiểm test có nhạy với lỗi đã nhắm tới. Các `assert` trong bài minh họa là kiểm tra ví dụ; validation của ứng dụng cần exception/nhánh xử lý, không dựa vào assert có thể bị tắt bởi `python -O`.

## Môi trường và Git tối thiểu

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python lessons/quick-review/examples/p08.py
git status
git diff
```

Chạy từ repo root trên shell macOS/Linux. Venv tách dependency; không đưa `.venv`, secret hay dữ liệu riêng vào Git. Các ví dụ này không cần cài thêm thư viện. Khi làm project có dependency, khai báo phiên bản phù hợp và ghi lệnh cài/chạy trong README. `unittest` ở đây giúp chạy ngay; course đầy đủ có thêm pytest.

## Tự kiểm

1. Test luôn pass vì `assertTrue(True)` chứng minh gì về hàm?
2. Chạy pass trên fake DB có chứng minh SQL đúng không?
3. Đọc ví dụ và chạy tất cả test mẫu có đồng nghĩa bạn đã tự làm được không?

<details>
<summary>Đáp án ngắn</summary>

1. Không chứng minh hành vi hàm. 2. Không, cần integration test với DB tương ứng. 3. Chưa; tự giải thích và sửa được biến thể mới là bước tiếp theo.

</details>

**Bài tập 15 phút:** thêm giới hạn title 80 ký tự; viết test 79/80/81 ký tự và nêu trim trước hay sau khi kiểm độ dài. Làm test fail trước khi cài quy tắc.

**Nguồn:** [unittest](https://docs.python.org/3/library/unittest.html), [venv](https://docs.python.org/3/library/venv.html). Đi sâu theo [A.4](../../../ROADMAP.md#a-4).
