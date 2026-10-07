# Theo dõi tiến độ

Kế hoạch: [ROADMAP.md](ROADMAP.md). Bảng khởi tạo ngày 07/10/2026, chưa có kết quả học được nhập từ dashboard. `NOT_STARTED` ở đây nghĩa là chưa ghi nhận bắt đầu trong repo, không kết luận người học chưa biết chủ đề đó.

## Quy ước trạng thái

| Trạng thái | Ý nghĩa |
| --- | --- |
| NOT_STARTED | Chưa ghi nhận bắt đầu tuần trong repo |
| IN_PROGRESS | Đang học hoặc làm bài |
| SUBMITTED | Đã có bài và bằng chứng, chờ review |
| NEEDS_REVISION | Review chỉ ra phần cần bổ sung/sửa |
| VERIFIED | Có bằng chứng đáp ứng tiêu chí, giải thích và kết luận review được ghi rõ |

Luồng thường dùng: `NOT_STARTED → IN_PROGRESS → SUBMITTED → VERIFIED`. Nếu cần sửa: `SUBMITTED → NEEDS_REVISION → SUBMITTED`. `VERIFIED` phải có link kết quả review, người review và mức hỗ trợ; review bằng AI hoặc tự review cần ghi đúng loại, không thay tên thành mentor review.

Nhãn mô tả bằng chứng: `DIRECT` — quan sát từ bài làm/kết quả chạy; `GUIDED` — hoàn thành có hướng dẫn; `SELF_REPORTED` — tự khai; `NOT_TESTED` — chưa chạy kiểm tra; `UNKNOWN` — chưa đủ thông tin. Các nhãn này không thay thế trạng thái tuần.

## Tiến độ theo tuần

| Tuần | Trọng tâm | Giờ dự kiến | Trạng thái | Ngày bắt đầu | Giờ thực tế | Bằng chứng và review |
| --- | --- | ---: | --- | --- | --- | --- |
| [W0](weeks/W00.md) | Prerequisites (chỉ Full-track) | 20 | NOT_STARTED | — | — | — |
| [W1](weeks/W01.md) | LLM Foundations & Model Selection | 22 | NOT_STARTED | — | — | — |
| [W2](weeks/W02.md) | Prompt & Context Engineering | 22 | NOT_STARTED | — | — | — |
| [W3](weeks/W03.md) | AI App Architecture → P1 | 22 | NOT_STARTED | — | — | — |
| [W4](weeks/W04.md) | Embedding & Vector Retrieval | 22 | NOT_STARTED | — | — | — |
| [W5](weeks/W05.md) | Advanced RAG & Failure Modes | 22 | NOT_STARTED | — | — | — |
| [W6](weeks/W06.md) | KMS / RAG System → P2 | 22 | NOT_STARTED | — | — | — |
| [W7](weeks/W07.md) | Tool Calling & Agent from Scratch | 20 | NOT_STARTED | — | — | — |
| [W8](weeks/W08.md) | Orchestration: Graph, State, Multi-Agent | 20 | NOT_STARTED | — | — | — |
| [W9](weeks/W09.md) | MCP & Tool Ecosystem → P3 | 23 | NOT_STARTED | — | — | — |
| [W10](weeks/W10.md) | Evaluation & Observability | 22 | NOT_STARTED | — | — | — |
| [W11](weeks/W11.md) | Security, Cost, Scale + Fine-tuning | 24 | NOT_STARTED | — | — | — |
| [W12](weeks/W12.md) | CAPSTONE & Deploy | 27 | NOT_STARTED | — | — | — |

**Tổng kế hoạch:** 288 giờ. Giờ thực tế chưa được ghi nhận; không cộng giờ dự kiến của checkbox thành giờ đã học.

## Phiên học tiếp theo

- Tuần / hạng mục: chọn sau khi đối chiếu W0.
- Ngày dự kiến: chưa đặt.
- Việc nhỏ cần hoàn thành: ghi bài làm đã có hoặc bắt đầu một hạng mục W0.
- Đầu ra cần nộp: file/repo kèm ghi chú kiểm chứng.

## Các mốc review

| Mốc | Phạm vi | Kết luận | Bằng chứng / người review |
| --- | --- | --- | --- |
| Đầu vào | W0 | Chưa review | — |
| AI Chat P1 | W1–W3 | Chưa review | — |
| Knowledge System P2 | W4–W6 | Chưa review | — |
| Agent System P3 | W7–W9 | Chưa review | — |
| Capstone | W10–W12 | Chưa review | — |

## Cập nhật sau mỗi buổi

Lưu một [nhật ký](templates/WEEKLY_REVIEW.md) trong `evidence/`, tick các hạng mục đã thực hiện ở file tuần, rồi cập nhật trạng thái/giờ thực tế/link ở bảng trên. Chỉ cộng thời gian đã thực sự ghi nhận. Nếu có bài cũ đáp ứng tiêu chí, liên kết bài đó và review trước khi công nhận.
