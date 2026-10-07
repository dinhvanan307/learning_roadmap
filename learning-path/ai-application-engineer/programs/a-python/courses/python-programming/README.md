# A1 · Python Programming và testing

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** Đối chiếu đầu vào Python.

**Khối lượng:** 30–45 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Giải thích mutability, scope, generator, context manager và async bằng ví dụ nhỏ. | PLO1 |
| CLO2 | Viết CLI có validation, tách I/O khỏi logic và giữ contract khi refactor. | PLO2 |
| CLO3 | Viết test biên/lỗi và kiểm tra timeout/cancellation với fake I/O. | PLO3 |
| CLO4 | Đọc diff, giải thích lỗi do AI tạo và sửa biến thể schema mới. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. Dữ liệu và contract](units/01.md) | Kiểu dữ liệu; control flow; list/tuple/dict/set; mutability; hàm/scope; exception; type hint; file; môi trường | Hàm, bảng input/expected và tests cho dữ liệu hợp lệ/lỗi. |
| [2. Tổ chức code và tính năng Python](units/02.md) | Class/object; inheritance/composition; module/package; scope/closure; iterator/generator; decorator; context manager; dataclass | CLI, README chạy lại và commit refactor. |
| [3. Async và kiểm chứng](units/03.md) | coroutine/task; event loop; I/O-bound/CPU-bound; timeout; cancellation; concurrency limit | Timeline, tests và giải thích khi nào async không giúp. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
