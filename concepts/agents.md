# Agent, tool và orchestration

[Danh mục concept](../docs/CONCEPTS.md) · [Roadmap](../ROADMAP.md)

**Học trong:** [D3](../learning-path/ai-application-engineer/programs/d-ai-systems/courses/agents/README.md).

Các mức ưu tiên là lựa chọn của roadmap cho phạm vi ứng dụng này; không phải bảng xếp hạng độ phổ biến trên thị trường.

| Concept | Hiểu ngắn gọn | Khi dùng | Câu hỏi tự kiểm | Mức |
| --- | --- | --- | --- | --- |
| Workflow và agent | Workflow có luồng do code thiết kế; agent có phần quyết định bước/hành động do model điều khiển. | Chọn mức tự động hóa theo độ bất định. | Workflow đơn giản đã xử lý task đủ tốt chưa? | CORE |
| Agent loop | Chu kỳ nhận trạng thái, quyết định, thực thi và quan sát cho tới điều kiện dừng. | Nhiệm vụ nhiều bước. | Bước nào có thể thất bại hoặc quay vòng? | PRACTICE |
| Harness | Phần mềm bao quanh model: công cụ, context, state, giới hạn, kiểm tra và thực thi. | Runtime của agent; thuật ngữ có phạm vi khác nhau theo tài liệu. | Chính xác phần nào trong hệ thống là harness? | CORE |
| Tool contract | Tên, args/schema, kết quả, lỗi và quyền của một hành động. | Giao model khả năng gọi chức năng. | Model có gọi được tool không nằm trong allowlist? | PRACTICE |
| MCP | Giao thức tương tác host/client/server cho capability như tools, resources, prompts. | Kết nối công cụ theo một giao diện chung. | MCP không tự xác nhận ai được đọc/ghi dữ liệu nào. | PRACTICE |
| State machine và checkpoint | Mô tả trạng thái/chuyển trạng thái; lưu mốc để tiếp tục. | Agent dài hạn hoặc có approval. | Checkpoint nằm trước hay sau side effect? | PRACTICE |
| HITL và approval | Đưa con người vào quyết định cần kiểm soát. | Ghi/xóa/thay đổi bên ngoài hoặc quyết định thiếu dữ kiện. | Approval gắn đúng payload, thời điểm và phạm vi? | PRACTICE |
| Permission và least privilege | Chỉ cấp quyền cần cho nhiệm vụ. | Tools, service account và tenant boundary. | Prompt nói được phép có thay thế policy server? | CORE |
| Budget và stopping criteria | Giới hạn số bước, thời gian, chi phí và điều kiện dừng. | Tránh loop/cost không kiểm soát. | Hết budget trả trạng thái gì và giữ được công việc nào? | PRACTICE |
| Prompt injection | Nội dung không tin cậy cố biến dữ liệu thành chỉ dẫn hành động. | Web, retrieved docs và tool outputs. | Hệ thống giữ policy/quyền ngoài model thế nào? | PRACTICE |
| Multi-agent và delegation | Chia nhiệm vụ cho nhiều agent với phối hợp và chi phí bổ sung. | Bài toán thực sự có phần độc lập hoặc vai trò rõ. | Có tốt hơn single-agent cùng ngân sách và task set? | OPTIONAL |
| Compensation và reconciliation | Sửa tác động đã xảy ra hoặc đối soát trạng thái không chắc chắn. | Workflow có dịch vụ ngoài, timeout sau hành động. | Không nhầm rollback state nội bộ với hoàn tác side effect ngoài. | AWARENESS |

## Nguồn đối chiếu

[Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents), [MCP Architecture](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture), [OWASP LLM Applications](https://owasp.org/projects/top-10-for-large-language-model-applications), [Celery Tasks](https://docs.celeryq.dev/en/stable/userguide/tasks.html).

Bảng là diễn giải phục vụ học tập; bài thực hành và câu hỏi tự kiểm là thiết kế của repo. Đọc đúng phần được chỉ trong unit, sau đó giải thích bằng code hoặc ví dụ thay vì học thuộc bảng.
