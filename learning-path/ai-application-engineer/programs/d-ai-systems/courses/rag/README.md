# D2 · Ingestion, Retrieval và RAG

[Program](../../README.md) · [Tiến độ](../../../../../../PROGRESS.md)

**Đầu vào:** D1, SQL và quyền dữ liệu.

**Khối lượng:** 40–60 giờ dự kiến, gồm thực hành và review. Học theo năng lực đầu vào; người đã có artifact tương đương có thể xin review để rút phần ôn.

## Course Learning Outcomes

| CLO | Kết quả thể hiện | Đóng góp vào program |
| --- | --- | --- |
| CLO1 | Giải thích ingestion/OCR/vision, chunking, embedding, indexing, retrieval và reranking. | PLO1 |
| CLO2 | Xây pipeline giữ nguồn, phiên bản, vị trí trích và ACL từ đầu đến cuối. | PLO2 |
| CLO3 | Đánh giá retrieval tách khỏi answer quality trên tập query/evidence cố định. | PLO3 |
| CLO4 | Chẩn đoán lỗi thiếu nguồn, sai phiên bản, chunk/rank và phát biểu vượt bằng chứng. | PLO4 |

## Units và topics

| Unit | Topics chính | Đầu ra |
| --- | --- | --- |
| [1. Tài liệu thành record](units/01.md) | parsing; OCR; vision; table extraction; metadata; provenance; incremental ingestion | Corpus manifest, records và reject report. |
| [2. Tìm kiếm có đánh giá](units/02.md) | chunking/overlap; embedding; BM25; vector index; hybrid; RRF; top-k; reranker; ACL | Retrieval report, qrels và cấu hình chunk/index. |
| [3. Sinh câu trả lời và kiểm chứng](units/03.md) | grounding; citation; supported claim; abstention; stale evidence; context budget; prompt injection | Answer rubric, citation span và error analysis. |

## Bài nộp và đánh giá

Gộp output của các unit thành một milestone của [running project](../../running-project/README.md). Trước review, gửi file/repo+commit, lệnh chạy, fixture và kết quả thật.

- CLO1: giải thích concept qua ví dụ, không chỉ đọc định nghĩa.
- CLO2: demo artifact đúng contract.
- CLO3: chạy ca lỗi/biên; ghi expected và actual.
- CLO4: sửa một biến thể hoặc giải thích trade-off, ghi mức trợ giúp.

Các tiêu chí cụ thể của unit và outcome của course được dùng để kết luận; bốn dòng trên là cách thu bằng chứng, không thay thế nội dung CLO.

## Tài liệu và ghi chú

Nguồn gắn trực tiếp trong mỗi unit; xem thêm [danh mục nguồn](../../../../../../docs/RESOURCES.md). Tạo `docs/` trong course khi có ghi chú, báo cáo hoặc tài liệu được phép lưu; đặt tên theo nội dung/ngày, rồi liên kết từ review. Không sao chép toàn văn tài liệu bên ngoài vào repo.
