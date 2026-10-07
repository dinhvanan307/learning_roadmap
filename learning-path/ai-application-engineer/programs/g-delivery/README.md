# G · Deployment, DevOps và LLMOps

[Learning path](../../README.md) · [Tiến độ](../../../../PROGRESS.md)

**Vai trò:** giai đoạn chính theo mindmap. **Đầu vào:** F có release candidate; Linux/process/network cơ bản được bắt đầu từ B.

## Phạm vi kiến thức của Phase G

- [G.1 · Linux và Containerization](../../../../ROADMAP.md#g-1)
- [G.2 · Cloud và Infrastructure as Code](../../../../ROADMAP.md#g-2)
- [G.3 · CI/CD, DevSecOps và phục hồi](../../../../ROADMAP.md#g-3)
- [G.4 · Observability, SRE và reliability](../../../../ROADMAP.md#g-4)
- [G.5 · LLMOps/MLOps và vận hành AI](../../../../ROADMAP.md#g-5)

Xem checklist topics, thực hành và độ sâu tại các liên kết trên. Hoàn thành toàn bộ phần bắt buộc và gate của phase; ghi bằng chứng trong [tracker từng phần](../../../../progress/PHASES.md).

## Program Learning Outcomes

Sau chương trình, người học có thể:

- **PLO1:** Giải thích cấu hình runtime, network, container, storage và secret.
- **PLO2:** Triển khai một môi trường có build/release và quy trình rollback rõ.
- **PLO3:** Theo dõi chất lượng, độ trễ, lỗi, chi phí và khả năng phục hồi.
- **PLO4:** Quản lý thay đổi model/prompt/data và nêu khi nào cần mở rộng hạ tầng.

## Courses và khối lượng

| Course | Giờ dự kiến | Milestone |
| --- | ---: | --- |
| [G1 · Linux, Container, Cloud và CI/CD](courses/devops/README.md) | 30–45 | Đóng gói app và triển khai trên một target với cấu hình tách khỏi code. |
| [G2 · Observability, SRE và LLMOps](courses/llmops/README.md) | 25–40 | Theo dõi request/model/prompt/dataset version cùng latency và cost. |

**Tổng tham chiếu:** 55–85 giờ, gồm đọc, thực hành, test và review. Đây là ước lượng thiết kế mới, cần điều chỉnh theo bài làm đầu vào; không phải số giờ do mindmap xác nhận.

## Running project

Bản release trên một môi trường được chọn, CI/CD, dashboard/report vận hành, backup/restore và runbook.

Chi tiết: [mốc sản phẩm và tiêu chí nghiệm thu](running-project/README.md).

## Gate kết thúc

Có bằng chứng deploy/health, rollback app/config và restore dữ liệu thử nghiệm; monitor chất lượng AI ngoài uptime; chưa triển khai thì ghi NOT_TESTED.

Mỗi PLO cần liên kết tới bài làm, kết quả chạy và phần giải thích. Dùng [mẫu review](../../../../templates/REVIEW.md); chưa có bài làm thì không đánh dấu đạt.

## Học theo nhu cầu

Các mục `CORE`, `PRACTICE`, `AWARENESS`, `OPTIONAL` được giải thích trong [danh mục concept](../../../../docs/CONCEPTS.md). Hoàn thành số tuần không tự xác nhận cấp bậc nghề nghiệp.
