# D · AI Application, RAG và Agent Systems

[Learning path](../../README.md) · [Tiến độ](../../../../PROGRESS.md)

**Vai trò:** giai đoạn chính theo mindmap. **Đầu vào:** B và C; thống kê đánh giá tối thiểu, vector/cosine được ôn trong D1.

## Phạm vi kiến thức của Phase D

- [D.1 · LLM Fundamentals và kiến trúc model](../../../../ROADMAP.md#d-1)
- [D.2 · AI Application Architecture và LLM Integration](../../../../ROADMAP.md#d-2)
- [D.3 · RAG System](../../../../ROADMAP.md#d-3)
- [D.4 · Agent System, Tool và MCP](../../../../ROADMAP.md#d-4)
- [D.5 · Đánh giá kỹ thuật và an toàn ứng dụng AI](../../../../ROADMAP.md#d-5)

Xem checklist topics, thực hành và độ sâu tại các liên kết trên. Hoàn thành toàn bộ phần bắt buộc và gate của phase; ghi bằng chứng trong [tracker từng phần](../../../../progress/PHASES.md).

## Program Learning Outcomes

Sau chương trình, người học có thể:

- **PLO1:** Giải thích luồng inference, retrieval và agent, phân biệt model với runtime ứng dụng.
- **PLO2:** Tích hợp model qua contract và xây pipeline tài liệu có nguồn/phiên bản/quyền.
- **PLO3:** Đánh giá chất lượng, chi phí, latency và lỗi trên bộ dữ liệu cố định.
- **PLO4:** Kiểm soát tool, state, ngân sách và dừng/escalate khi thiếu dữ kiện hoặc vượt phạm vi.

## Courses và khối lượng

| Course | Giờ dự kiến | Milestone |
| --- | ---: | --- |
| [D1 · LLM Architecture và Integration](courses/llm-integration/README.md) | 25–40 | Tạo adapter model với schema output, timeout và dữ liệu lỗi giả lập. |
| [D2 · Ingestion, Retrieval và RAG](courses/rag/README.md) | 40–60 | Xây pipeline giữ nguồn, phiên bản, vị trí trích và ACL từ đầu đến cuối. |
| [D3 · Agent Loop, Harness và MCP](courses/agents/README.md) | 35–55 | Xây agent nhỏ có state và tool contract rõ, giới hạn số bước/chi phí. |

**Tổng tham chiếu:** 100–155 giờ, gồm đọc, thực hành, test và review. Đây là ước lượng thiết kế mới, cần điều chỉnh theo bài làm đầu vào; không phải số giờ do mindmap xác nhận.

## Running project

Prototype hỏi đáp dữ liệu du lịch có nguồn, kèm agent chỉ đọc hoặc đề xuất thay đổi để người dùng duyệt.

Chi tiết: [mốc sản phẩm và tiêu chí nghiệm thu](running-project/README.md).

## Gate kết thúc

Có baseline, split/rubric cố định, citation truy về nguồn, negative tests quyền và tool budget; kết quả nêu cả ca thất bại.

Mỗi PLO cần liên kết tới bài làm, kết quả chạy và phần giải thích. Dùng [mẫu review](../../../../templates/REVIEW.md); chưa có bài làm thì không đánh dấu đạt.

## Học theo nhu cầu

Các mục `CORE`, `PRACTICE`, `AWARENESS`, `OPTIONAL` được giải thích trong [danh mục concept](../../../../docs/CONCEPTS.md). Hoàn thành số tuần không tự xác nhận cấp bậc nghề nghiệp.
