# G1 · Linux, Container, Cloud và CI/CD

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** B và bản build F.

**Khối lượng:** 30–45 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Debug process/port/env/file permission và giao tiếp container. | PLO1 |
| CLO2 | Đóng gói app và triển khai trên một target với cấu hình tách khỏi code. | PLO2 |
| CLO3 | Chạy CI/CD và diễn tập rollback/restore trong môi trường lab. | PLO3 |
| CLO4 | Giải thích IaC, Kubernetes/GitOps và lý do dùng hoặc chưa dùng. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. Linux và container](units/01.md) | shell/bash; process; permissions; env; DNS/port; image/container; volume/network; Compose | Compose/config mẫu và runbook debug. |
| [2. CI/CD và cloud](units/02.md) | workflow; build artifact; immutable version; staging; secret; cloud compute/storage/IAM; IaC plan/state | Workflow, deployment config và ADR target. |
| [3. Phục hồi và mở rộng](units/03.md) | health/readiness; rollback; backup/restore; migration; Kubernetes; GitOps; drift | Biên bản phục hồi và sơ đồ deployment. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
