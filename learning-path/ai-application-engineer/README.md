# Learning path AI Application Engineer

[Roadmap A–G](../../ROADMAP.md) · [Cấu trúc và learning outcomes](../../docs/FORMAT.md) · [Concepts](../../docs/CONCEPTS.md)

## Kết quả cuối lộ trình

Người học có thể làm rõ một bài toán, xây luồng ứng dụng có dữ liệu/AI, đo chất lượng và lỗi, triển khai có khả năng phục hồi và giải thích quyết định kỹ thuật bằng bài làm. Đây là mục tiêu đánh giá, không phải tuyên bố đã đạt.

## Danh mục chương trình và khóa học

| Program | Course | Đầu vào cụ thể | Giờ dự kiến |
| --- | --- | --- | ---: |
| [A · Python Programming for AI](programs/a-python/README.md) | [A1 · Python Programming và testing](programs/a-python/courses/python-programming/README.md) | Đối chiếu đầu vào Python. | 30–45 |
| [A · Python Programming for AI](programs/a-python/README.md) | [A2 · Python Libraries for Data and AI](programs/a-python/courses/python-libraries/README.md) | A1: đọc/kiểm dữ liệu và test được. | 20–30 |
| [B · Data và Full-stack Web Development](programs/b-fullstack/README.md) | [B1 · Database và Data Modeling](programs/b-fullstack/courses/database/README.md) | A1; biết đọc bảng và viết hàm. | 30–45 |
| [B · Data và Full-stack Web Development](programs/b-fullstack/README.md) | [B2 · Internet Basics và FastAPI](programs/b-fullstack/courses/fastapi/README.md) | B1 và async trong A1. | 40–60 |
| [B · Data và Full-stack Web Development](programs/b-fullstack/README.md) | [B3 · React, Next.js và Tailwind CSS](programs/b-fullstack/courses/frontend/README.md) | B2; ôn JavaScript/TypeScript, HTML/CSS khi chưa có bài làm. | 35–50 |
| [C · AI trong quy trình phát triển phần mềm](programs/c-ai-sdlc/README.md) | [C1 · Concept AI và làm việc với coding assistant](programs/c-ai-sdlc/courses/ai-coding/README.md) | A1; chọn một phần code đã tự hiểu. | 12–18 |
| [C · AI trong quy trình phát triển phần mềm](programs/c-ai-sdlc/README.md) | [C2 · SDLC, Spec-driven Development và CI](programs/c-ai-sdlc/courses/spec-driven/README.md) | B có luồng chạy được; C1 hoặc quy trình AI tương đương. | 18–27 |
| [D · AI Application, RAG và Agent Systems](programs/d-ai-systems/README.md) | [D1 · LLM Architecture và Integration](programs/d-ai-systems/courses/llm-integration/README.md) | API, async và kiểm thử; ôn vector/xác suất nếu cần. | 25–40 |
| [D · AI Application, RAG và Agent Systems](programs/d-ai-systems/README.md) | [D2 · Ingestion, Retrieval và RAG](programs/d-ai-systems/courses/rag/README.md) | D1, SQL và quyền dữ liệu. | 40–60 |
| [D · AI Application, RAG và Agent Systems](programs/d-ai-systems/README.md) | [D3 · Agent Loop, Harness và MCP](programs/d-ai-systems/courses/agents/README.md) | D1; D2 nếu agent dùng tìm tài liệu; có API tests. | 35–55 |
| [E · Nghiên cứu và lựa chọn dự án](programs/e-research/README.md) | [E1 · Problem Discovery và Experimental Design](programs/e-research/courses/project-research/README.md) | Có thể chạy một prototype; chưa cần tuyên bố nhu cầu sản phẩm đã xác nhận. | 20–35 |
| [F · Xây dựng sản phẩm và Ownership](programs/f-product/README.md) | [F1 · MVP Implementation và Product Review](programs/f-product/courses/product-delivery/README.md) | Project brief E và các năng lực kỹ thuật thực sự dùng trong MVP. | 45–70 |
| [G · Deployment, DevOps và LLMOps](programs/g-delivery/README.md) | [G1 · Linux, Container, Cloud và CI/CD](programs/g-delivery/courses/devops/README.md) | B và bản build F. | 30–45 |
| [G · Deployment, DevOps và LLMOps](programs/g-delivery/README.md) | [G2 · Observability, SRE và LLMOps](programs/g-delivery/courses/llmops/README.md) | D evaluation và G1 deployment lab. | 25–40 |
| [ML · Machine Learning Foundations](programs/ml-foundations/README.md) (mở rộng) | [ML1 · Math for Machine Learning](programs/ml-foundations/courses/math/README.md) | A2 và phép toán cơ bản. | 20–35 |
| [ML · Machine Learning Foundations](programs/ml-foundations/README.md) (mở rộng) | [ML2 · Machine Learning và Evaluation](programs/ml-foundations/courses/classical-ml/README.md) | ML1 hoặc kiến thức tương đương. | 30–45 |
| [DL · Deep Learning và Model Adaptation](programs/dl-foundations/README.md) (mở rộng) | [DL1 · Neural Networks và PyTorch](programs/dl-foundations/courses/neural-networks/README.md) | ML1–ML2 hoặc đầu vào tương đương. | 25–40 |
| [DL · Deep Learning và Model Adaptation](programs/dl-foundations/README.md) (mở rộng) | [DL2 · Computer Vision và Fine-tuning](programs/dl-foundations/courses/adaptation/README.md) | DL1, dữ liệu được phép và ngân sách tính toán được chốt. | 25–45 |

## Một vòng học

Course README → unit → nguồn đọc → bài làm → tests/report → milestone → review CLO/PLO. Nguồn đặt ở từng unit; ghi chú mới lưu trong thư mục `docs/` của course khi phát sinh. Không cần đọc tất cả tài liệu tham khảo trước khi làm bài đầu tiên.

Theo dõi ở [tracker](../../PROGRESS.md) và [ma trận CLO](../../progress/OUTCOMES.md).
