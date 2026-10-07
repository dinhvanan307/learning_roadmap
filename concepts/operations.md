# DevOps, reliability và LLMOps

[Danh mục concept](../docs/CONCEPTS.md) · [Roadmap](../ROADMAP.md)

**Học trong:** [G1](../learning-path/ai-application-engineer/programs/g-delivery/courses/devops/README.md), [G2](../learning-path/ai-application-engineer/programs/g-delivery/courses/llmops/README.md), [B2](../learning-path/ai-application-engineer/programs/b-fullstack/courses/fastapi/README.md).

Các mức ưu tiên là lựa chọn của roadmap cho phạm vi ứng dụng này; không phải bảng xếp hạng độ phổ biến trên thị trường.

| Concept | Hiểu ngắn gọn | Khi dùng | Câu hỏi tự kiểm | Mức |
| --- | --- | --- | --- | --- |
| Process, thread, permission và environment | Các đơn vị thực thi, quyền truy cập và cấu hình runtime. | Linux/shell, service và container debug. | App chạy khác nhau do env hay do code? | CORE |
| Image, container và Compose | Image đóng gói; container là instance chạy; Compose mô tả nhóm service. | Lab và deployment nhỏ. | Dữ liệu nằm trong volume hay mất theo container? | PRACTICE |
| CI và CD | Tích hợp được kiểm tự động; delivery/deployment tổ chức phát hành với mức tự động khác nhau. | Release có kiểm soát. | Pipeline xanh có chạy đúng tests cần chặn regression? | PRACTICE |
| IaC, plan và state | Mô tả hạ tầng bằng code, xem dự kiến thay đổi và theo dõi tài nguyên quản lý. | Terraform và môi trường lặp lại. | Ai bảo vệ state, secret và thay đổi phá hủy? | PRACTICE |
| Cloud compute/storage/IAM | Tài nguyên chạy, lưu dữ liệu và quản lý danh tính/quyền. | Chọn một môi trường triển khai. | Thứ nào public, thứ nào private, chi phí từ đâu? | CORE |
| Logs, metrics và traces | Sự kiện chi tiết, chuỗi số đo và đường đi request/span. | Điều tra lỗi và quan sát tải. | Từ lỗi UI tìm ra span provider tương ứng được không? | PRACTICE |
| SLI, SLO, SLA và error budget | Chỉ số, mục tiêu, thỏa thuận và khoảng lỗi cho phép theo định nghĩa dịch vụ. | SRE và quyết định release. | Đo uptime có phản ánh câu trả lời AI dùng được? | AWARENESS |
| Health, readiness và liveness | Kiểm sức khỏe, khả năng nhận traffic và còn sống theo mục đích probe. | Deploy và xử lý dependency lỗi. | DB down có nên restart app liên tục? | PRACTICE |
| Rollback, backup và restore | Quay lại phiên bản/cấu hình, giữ bản sao và phục hồi dữ liệu. | Sự cố phát hành. | Đã thử restore hay chỉ thấy backup file tồn tại? | PRACTICE |
| At-least-once và idempotent consumer | Message có thể giao nhiều lần; consumer phải xử lý effect lặp đúng contract. | Worker/queue. | Crash sau DB commit trước ack có ghi lại effect? | PRACTICE |
| Retry, backoff, jitter và DLQ | Thử lại có giới hạn/giãn cách; lưu lỗi không xử lý được để xem lại. | Lỗi tạm thời và job nền. | Lỗi validation có bị retry vô ích? | PRACTICE |
| Transactional outbox | Ghi event cùng business transaction rồi relay phát sau; vẫn có khả năng phát lặp. | Tránh mất event giữa DB commit và publish. | Consumer dedup và đối soát pending ở đâu? | PRACTICE |
| MLOps và LLMOps | Thực hành vòng đời model/dữ liệu; ứng dụng LLM còn quản prompt, retrieval, eval và provider/cost. | Thay đổi AI có thể truy vết. | Deploy API xong đã quản được regression model chưa? | CORE |
| Kubernetes và GitOps | Orchestration container; quản lý trạng thái mong muốn qua Git và cơ chế reconcile. | Khi quy mô/vận hành cần. | Compose hoặc một service có đáp ứng bài toán hiện tại? | OPTIONAL |
| AIOps và ChatOps | AI hỗ trợ vận hành; giao diện hội thoại tích hợp thao tác vận hành. | Tóm tắt incident, truy vấn log, workflow có quyền. | Lệnh ghi có kiểm quyền/approval/audit ngoài câu trả lời AI? | AWARENESS |
| Incident và postmortem | Xử lý sự cố, ghi timeline/nguyên nhân/yếu tố góp phần và hành động phòng ngừa. | Học từ lỗi vận hành. | Action item có chủ đích và kiểm được hiệu quả? | PRACTICE |

## Nguồn đối chiếu

[Docker Compose](https://docs.docker.com/compose/), [GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions), [Terraform Introduction](https://developer.hashicorp.com/terraform/intro), [OpenTelemetry Signals](https://opentelemetry.io/docs/concepts/signals/), [Google SRE Service Level Objectives](https://sre.google/sre-book/service-level-objectives/), [Celery Tasks](https://docs.celeryq.dev/en/stable/userguide/tasks.html), [Kubernetes Overview](https://kubernetes.io/docs/concepts/overview/).

Bảng là diễn giải phục vụ học tập; bài thực hành và câu hỏi tự kiểm là thiết kế của repo. Đọc đúng phần được chỉ trong unit, sau đó giải thích bằng code hoặc ví dụ thay vì học thuộc bảng.
