# C2 · SDLC, Spec-driven Development và CI

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** B có luồng chạy được; C1 hoặc quy trình AI tương đương.

**Khối lượng:** 18–27 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Phân biệt requirement, spec, design, implementation, verification và release. | PLO1 |
| CLO2 | Viết spec/ADR/tasks cho một feature có tiêu chí nghiệm thu. | PLO2 |
| CLO3 | Thiết lập review và CI kiểm contract thay vì chỉ build thành công. | PLO3 |
| CLO4 | So sánh Spec Kit, AWS AI-DLC và Scrum ở mức quy trình, không coi là chuẩn bắt buộc chung. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. Yêu cầu và thiết kế](units/01.md) | problem statement; user story; acceptance criteria; non-goal; ADR; dependency | Spec một trang và ADR hai phương án. |
| [2. Quy trình có AI](units/02.md) | Spec-driven Development; AWS AI-DLC; backlog; Sprint Goal; Definition of Done | Sơ đồ spec → plan → implement → test → review. |
| [3. Git, CI và review](units/03.md) | branch/commit/PR; code review; CI job/artifact; regression; release note | PR hoặc review local, CI log và release note. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
