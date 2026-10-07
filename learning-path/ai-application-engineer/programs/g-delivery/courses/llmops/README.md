# G2 · Observability, SRE và LLMOps

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** D evaluation và G1 deployment lab.

**Khối lượng:** 25–40 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Phân biệt logs/metrics/traces, SLI/SLO và chất lượng AI. | PLO1 |
| CLO2 | Theo dõi request/model/prompt/dataset version cùng latency và cost. | PLO2 |
| CLO3 | Phát hiện regression, lỗi task và vượt budget bằng diễn tập. | PLO3 |
| CLO4 | Viết runbook và chọn mức tự động hóa AIOps/ChatOps phù hợp quyền. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. Quan sát hệ thống](units/01.md) | structured log; metric; trace/span; correlation ID; SLI/SLO; p95; error budget | Dashboard hoặc report tái lập và định nghĩa chỉ số. |
| [2. LLMOps và MLOps](units/02.md) | prompt/model/data version; eval regression; serving; drift; token/cost; hard budget; canary | Release comparison và điều kiện rollback. |
| [3. Reliability và vận hành](units/03.md) | retry/backoff; DLQ; idempotency; transactional outbox; reconciliation; incident; AIOps/ChatOps | Fault report, runbook và postmortem. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
