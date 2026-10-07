# Đánh giá, nghiên cứu và sản phẩm

[Danh mục concept](../docs/CONCEPTS.md) · [Roadmap](../ROADMAP.md)

**Học trong:** [D1](../learning-path/ai-application-engineer/programs/d-ai-systems/courses/llm-integration/README.md), [D2](../learning-path/ai-application-engineer/programs/d-ai-systems/courses/rag/README.md), [E1](../learning-path/ai-application-engineer/programs/e-research/courses/project-research/README.md), [F1](../learning-path/ai-application-engineer/programs/f-product/courses/product-delivery/README.md).

Các mức ưu tiên là lựa chọn của roadmap cho phạm vi ứng dụng này; không phải bảng xếp hạng độ phổ biến trên thị trường.

| Concept | Hiểu ngắn gọn | Khi dùng | Câu hỏi tự kiểm | Mức |
| --- | --- | --- | --- | --- |
| Baseline | Phương án so sánh đủ hợp lý để biết thay đổi mang lại gì. | Model, retrieval và workflow. | Đang so với giải pháp thật sự dùng được hay đối thủ quá yếu? | CORE |
| Train, dev và test | Dữ liệu học tham số, chọn cấu hình và đánh giá cuối có vai trò khác nhau. | ML và prompt/retrieval tuning. | Prompt đã được sửa theo các câu test chưa? | CORE |
| Leakage | Thông tin không hợp lệ lọt vào học/chọn cấu hình hoặc đánh giá. | Tránh kết quả tốt giả tạo. | Mẫu gần trùng hoặc preprocessing có nhìn test? | PRACTICE |
| Precision, recall và F1 | Đo đúng trong dự đoán dương, tìm được dương thực tế và trung bình điều hòa tương ứng. | Classification với hậu quả FP/FN khác nhau. | Tính tay từ TP/FP/FN và giải thích trade-off. | PRACTICE |
| Recall@k, MRR và nDCG | Các góc đo bao phủ tài liệu liên quan, vị trí đầu tiên và chất lượng thứ hạng. | Retrieval evaluation. | k, relevance labels và query set được chốt chưa? | PRACTICE |
| Rubric và calibrated judge | Tiêu chí chấm rõ; judge được đối chiếu với đánh giá người trên mẫu phù hợp. | Answer quality khó đo bằng exact match. | Judge có sai lệch và disagreement nào? | PRACTICE |
| Controlled experiment và ablation | Giữ điều kiện chung, thay một yếu tố hoặc bỏ một thành phần để hiểu tác động. | So sánh chunker, reranker, prompt. | Có vô tình đổi dataset/model cùng lúc? | PRACTICE |
| Latency, throughput và cost | Thời gian, số tác vụ trên thời gian và tài nguyên/chi phí theo đơn vị rõ. | Chọn cấu hình và vận hành. | p95 trên bao nhiêu mẫu, dưới mức tải nào? | PRACTICE |
| Hypothesis và evidence | Điều dự đoán cần kiểm khác với quan sát đã thu được. | Nghiên cứu hướng dự án. | Bằng chứng nào sẽ khiến đổi quyết định? | CORE |
| MVP, output và outcome | MVP kiểm giả thuyết ở phạm vi nhỏ; output là thứ tạo ra; outcome là thay đổi quan sát ở người dùng/hệ thống. | Chọn feature và review sản phẩm. | Có demo có đồng nghĩa người dùng giải quyết task tốt hơn? | CORE |
| Reproducibility | Đủ dữ liệu, version, config và quy trình để người khác kiểm lại. | Báo cáo benchmark và portfolio. | Người khác chạy được từ commit và manifest đã ghi? | PRACTICE |

## Nguồn đối chiếu

[scikit-learn Common Pitfalls](https://scikit-learn.org/stable/common_pitfalls.html), [GitHub Spec Kit](https://github.com/github/spec-kit), [Scrum Guide](https://scrumguides.org/scrum-guide.html).

Bảng là diễn giải phục vụ học tập; bài thực hành và câu hỏi tự kiểm là thiết kế của repo. Đọc đúng phần được chỉ trong unit, sau đó giải thích bằng code hoặc ví dụ thay vì học thuộc bảng.
