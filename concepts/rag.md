# RAG và quản trị dữ liệu nguồn

[Danh mục concept](../docs/CONCEPTS.md) · [Roadmap](../ROADMAP.md)

**Học trong:** [D2](../learning-path/ai-application-engineer/programs/d-ai-systems/courses/rag/README.md).

Các mức ưu tiên là lựa chọn của roadmap cho phạm vi ứng dụng này; không phải bảng xếp hạng độ phổ biến trên thị trường.

| Concept | Hiểu ngắn gọn | Khi dùng | Câu hỏi tự kiểm | Mức |
| --- | --- | --- | --- | --- |
| Ingestion | Đưa dữ liệu từ nguồn vào record/index có quy trình xử lý. | PDF, web, bảng và tài liệu nội bộ được phép. | Một nguồn lỗi có bị mất dấu hoặc nhập nửa chừng? | PRACTICE |
| OCR, vision và parsing | OCR nhận dạng chữ; vision xử lý thông tin ảnh; parsing đọc cấu trúc biểu diễn. | Scan, bảng hoặc tài liệu hỗn hợp. | Vì sao PDF có text không nhất thiết cần OCR? | CORE |
| Provenance và version | Ghi nguồn, phiên bản, vị trí và biến đổi của record. | Citation, cập nhật và audit. | Truy từ chunk về đúng bản tài liệu gốc được không? | PRACTICE |
| Chunking và overlap | Chia tài liệu thành đoạn; overlap giữ phần ngữ cảnh lân cận. | Cân bằng retrieval và context budget. | Chia cắt bảng/điều kiện có làm mất nghĩa? | PRACTICE |
| Indexing | Tổ chức record/biểu diễn để truy vấn, khác với chỉ lưu tài liệu. | Search và incremental updates. | Xóa nguồn đã xóa cả nội dung cũ khỏi truy hồi chưa? | PRACTICE |
| Sparse/BM25 và dense retrieval | Tìm theo tín hiệu từ vựng hoặc vector học được. | Baseline và so sánh truy hồi. | Loại câu hỏi nào mỗi cách bỏ lỡ? | CORE |
| Hybrid search và RRF | Kết hợp nhiều bộ xếp hạng; RRF gộp dựa trên vị trí rank. | Lexical và vector bổ sung cho nhau. | Lợi ích có được đo trên cùng query set? | PRACTICE |
| Vector index và ANN | Cấu trúc tìm lân cận, thường đánh đổi recall với tốc độ/bộ nhớ. | Corpus lớn cần truy hồi hiệu quả. | Có baseline exact hoặc cấu hình mặc định để so? | AWARENESS |
| Reranking | Sắp xếp lại tập ứng viên bằng mô hình/điểm khác. | Tăng độ phù hợp của context. | Reranker không thể cứu tài liệu chưa được lấy vào candidate set. | PRACTICE |
| Metadata filter và ACL | Hạn chế kết quả theo thuộc tính và quyền người dùng. | Multi-tenant, nguồn riêng, phiên bản. | Filter nằm trước khi dữ liệu đi vào model/tool output không? | PRACTICE |
| Ground truth và qrels | Nhãn tham chiếu cho câu hỏi/tài liệu liên quan hoặc evidence cần thiết. | Evaluation retrieval. | Nhãn có tiêu chí, nguồn và review hay do model tự bịa? | PRACTICE |
| Citation support và completeness | Nguồn phải hỗ trợ claim; đầy đủ còn đòi các điều kiện/ngoại lệ cần thiết. | QA có bằng chứng. | Retrieved/cited có thật sự hỗ trợ câu trả lời không? | CORE |
| Abstention | Không kết luận hoặc hỏi thêm khi thiếu cơ sở phù hợp. | Nguồn thiếu, mâu thuẫn, ngoài phạm vi. | Có ca đáng trả lời nhưng hệ thống từ chối quá mức? | PRACTICE |
| Incremental update và deletion | Theo dõi thay đổi để đồng bộ record/index/cache. | Dữ liệu thường xuyên đổi. | Một câu trả lời còn dùng phiên bản đã bị thu hồi? | PRACTICE |

## Nguồn đối chiếu

[Microsoft RAG Overview](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), [scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html), [OWASP LLM Applications](https://owasp.org/projects/top-10-for-large-language-model-applications).

[Microsoft Hybrid Search](https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview), [Microsoft Semantic Ranking](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview).

Bảng là diễn giải phục vụ học tập; bài thực hành và câu hỏi tự kiểm là thiết kế của repo. Đọc đúng phần được chỉ trong unit, sau đó giải thích bằng code hoặc ví dụ thay vì học thuộc bảng.
