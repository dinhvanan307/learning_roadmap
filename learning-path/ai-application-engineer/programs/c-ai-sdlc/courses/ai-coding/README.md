# C1 · Concept AI và làm việc với coding assistant

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** A1; chọn một phần code đã tự hiểu.

**Khối lượng:** 12–18 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Phân biệt sáu concept instruction/prompt/context/memory/skill/hook bằng tình huống. | PLO1 |
| CLO2 | Đưa context có phạm vi và contract cho AI xử lý một thay đổi nhỏ. | PLO2 |
| CLO3 | Tìm và sửa lỗi AI đề xuất bằng test độc lập với lời giải. | PLO3 |
| CLO4 | Giải thích quyền công cụ, nguồn dữ liệu không tin cậy và giới hạn tự động hóa. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. Prompt và context](units/01.md) | instruction; prompt; context window; example; retrieved context; context budget | Prompt và bảng thông tin cần/không cần cung cấp. |
| [2. Memory, skill và hook](units/02.md) | persistent memory; reusable skill; tool; lifecycle hook; permission | Bảng phân biệt sáu concept và một quy trình review có thể làm thủ công. |
| [3. Review và sửa code AI](units/03.md) | diff review; test oracle; negative test; regression; provenance; human-in-the-loop | Diff trước/sau, test fail/pass và nhật ký hỗ trợ. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
