# F1 · MVP Implementation và Product Review

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** Project brief E và các năng lực kỹ thuật thực sự dùng trong MVP.

**Khối lượng:** 45–70 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Lập backlog có dependency, acceptance criteria và Definition of Done. | PLO1 |
| CLO2 | Giao một luồng end-to-end đáp ứng contract và phạm vi đã chọn. | PLO2 |
| CLO3 | Kiểm chức năng, quyền, dữ liệu và degradation khi AI/provider lỗi. | PLO3 |
| CLO4 | Tiếp nhận phản hồi, sửa một vấn đề có bằng chứng và trình bày ownership. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. Scope và kế hoạch](units/01.md) | MVP; user flow; task breakdown; dependency; risk; ADR; DoD | Backlog và sơ đồ dependency. |
| [2. Tích hợp end-to-end](units/02.md) | contract test; E2E; authorization; validation; fallback; feature config | Demo, E2E report và artifact release candidate. |
| [3. Review và bàn giao](units/03.md) | feedback; bug triage; regression; changelog; runbook; ownership | Case study ngắn, release note và README chạy lại. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
