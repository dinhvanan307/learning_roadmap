# Running project · AI Application, RAG và Agent Systems

[Chương trình](../README.md) · [Dự án xuyên suốt](../../../../../projects/RUNNING_PROJECT.md)

## Mục tiêu và output

Prototype hỏi đáp dữ liệu du lịch có nguồn, kèm agent chỉ đọc hoặc đề xuất thay đổi để người dùng duyệt.

Đây là đầu ra cần thực hiện, chưa phải sản phẩm đã có mã hoặc đã chạy. Có thể giữ code ở repo bài tập riêng và ghi commit trong bằng chứng.

## Năng lực được đánh giá

| PLO | Bằng chứng cần nộp |
| --- | --- |
| PLO1 · Giải thích luồng inference, retrieval và agent, phân biệt model với runtime ứng dụng. | Sơ đồ hoặc giải thích kèm ví dụ cụ thể, chỉ ra input/output và ranh giới. |
| PLO2 · Tích hợp model qua contract và xây pipeline tài liệu có nguồn/phiên bản/quyền. | Artifact chạy được, README và commit tương ứng. |
| PLO3 · Đánh giá chất lượng, chi phí, latency và lỗi trên bộ dữ liệu cố định. | Test/report cho ca đúng, ca lỗi và giới hạn kết luận. |
| PLO4 · Kiểm soát tool, state, ngân sách và dừng/escalate khi thiếu dữ kiện hoặc vượt phạm vi. | Demo, một biến thể mới, lý do thiết kế và ghi rõ mức trợ giúp. |

## Mốc theo course

- [ ] D1: Tạo adapter model với schema output, timeout và dữ liệu lỗi giả lập. — [yêu cầu course](../courses/llm-integration/README.md).
- [ ] D2: Xây pipeline giữ nguồn, phiên bản, vị trí trích và ACL từ đầu đến cuối. — [yêu cầu course](../courses/rag/README.md).
- [ ] D3: Xây agent nhỏ có state và tool contract rõ, giới hạn số bước/chi phí. — [yêu cầu course](../courses/agents/README.md).

## Nghiệm thu

Có baseline, split/rubric cố định, citation truy về nguồn, negative tests quyền và tool budget; kết quả nêu cả ca thất bại.

Ghi môi trường, input, lệnh chạy, expected/actual, commit, lỗi còn lại, người review và quyết định tiếp tục/bổ sung. Một artifact có thể chứng minh nhiều CLO/PLO, nhưng phải chỉ rõ phần nào hỗ trợ kết luận nào.
