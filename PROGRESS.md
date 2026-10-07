# Theo dõi tiến độ học

Lộ trình chính: [A–G](ROADMAP.md). Bản khởi tạo lại cấu trúc ngày 07/10/2026 giữ nguyên nguyên tắc không suy diễn năng lực từ tài liệu. Chưa có bài nộp mới được xác nhận. Các hàng `NOT_STARTED` nghĩa là chưa ghi nhận bắt đầu trong cấu trúc mới.

## Trạng thái

| Trạng thái | Điều kiện |
| --- | --- |
| NOT_STARTED | Chưa ghi nhận bắt đầu |
| IN_PROGRESS | Đang làm một unit/course có mục tiêu cụ thể |
| SUBMITTED | Đã gửi bài và bằng chứng, chờ review |
| NEEDS_REVISION | Review yêu cầu bổ sung/sửa |
| VERIFIED | Outcome liên quan được chứng minh, có review và mức trợ giúp rõ |

`NOT_TESTED`/`UNKNOWN` mô tả giới hạn bằng chứng. `DIRECT`/`GUIDED`/`SELF_REPORTED` mô tả nguồn và mức hỗ trợ; không thay thế trạng thái. Tự review hoặc AI review phải ghi đúng loại, không nhận là mentor đã xác nhận.

## Theo phần kiến thức trong phase

Theo dõi **29 phần kiến thức A.1–G.5** tại [progress/PHASES.md](progress/PHASES.md), đối chiếu với [checklist kiến thức](ROADMAP.md). Mỗi phần có trạng thái, artifact/review và việc còn thiếu. Chỉ kết luận phase hoàn thành khi tất cả phần bắt buộc đạt, đủ CLO/PLO và gate tích hợp.

## Theo course

| Course | Trạng thái | Ngày bắt đầu | Giờ thực tế | Bằng chứng / review |
| --- | --- | --- | --- | --- |
| [A1 · Python Programming và testing](learning-path/ai-application-engineer/programs/a-python/courses/python-programming/README.md) | NOT_STARTED | — | — | — |
| [A2 · Python Libraries for Data and AI](learning-path/ai-application-engineer/programs/a-python/courses/python-libraries/README.md) | NOT_STARTED | — | — | — |
| [B1 · Database và Data Modeling](learning-path/ai-application-engineer/programs/b-fullstack/courses/database/README.md) | NOT_STARTED | — | — | — |
| [B2 · Internet Basics và FastAPI](learning-path/ai-application-engineer/programs/b-fullstack/courses/fastapi/README.md) | NOT_STARTED | — | — | — |
| [B3 · React, Next.js và Tailwind CSS](learning-path/ai-application-engineer/programs/b-fullstack/courses/frontend/README.md) | NOT_STARTED | — | — | — |
| [C1 · Concept AI và làm việc với coding assistant](learning-path/ai-application-engineer/programs/c-ai-sdlc/courses/ai-coding/README.md) | NOT_STARTED | — | — | — |
| [C2 · SDLC, Spec-driven Development và CI](learning-path/ai-application-engineer/programs/c-ai-sdlc/courses/spec-driven/README.md) | NOT_STARTED | — | — | — |
| [D1 · LLM Architecture và Integration](learning-path/ai-application-engineer/programs/d-ai-systems/courses/llm-integration/README.md) | NOT_STARTED | — | — | — |
| [D2 · Ingestion, Retrieval và RAG](learning-path/ai-application-engineer/programs/d-ai-systems/courses/rag/README.md) | NOT_STARTED | — | — | — |
| [D3 · Agent Loop, Harness và MCP](learning-path/ai-application-engineer/programs/d-ai-systems/courses/agents/README.md) | NOT_STARTED | — | — | — |
| [E1 · Problem Discovery và Experimental Design](learning-path/ai-application-engineer/programs/e-research/courses/project-research/README.md) | NOT_STARTED | — | — | — |
| [F1 · MVP Implementation và Product Review](learning-path/ai-application-engineer/programs/f-product/courses/product-delivery/README.md) | NOT_STARTED | — | — | — |
| [G1 · Linux, Container, Cloud và CI/CD](learning-path/ai-application-engineer/programs/g-delivery/courses/devops/README.md) | NOT_STARTED | — | — | — |
| [G2 · Observability, SRE và LLMOps](learning-path/ai-application-engineer/programs/g-delivery/courses/llmops/README.md) | NOT_STARTED | — | — | — |
| [ML1 · Math for Machine Learning](learning-path/ai-application-engineer/programs/ml-foundations/courses/math/README.md) (mở rộng) | NOT_STARTED | — | — | — |
| [ML2 · Machine Learning và Evaluation](learning-path/ai-application-engineer/programs/ml-foundations/courses/classical-ml/README.md) (mở rộng) | NOT_STARTED | — | — | — |
| [DL1 · Neural Networks và PyTorch](learning-path/ai-application-engineer/programs/dl-foundations/courses/neural-networks/README.md) (mở rộng) | NOT_STARTED | — | — | — |
| [DL2 · Computer Vision và Fine-tuning](learning-path/ai-application-engineer/programs/dl-foundations/courses/adaptation/README.md) (mở rộng) | NOT_STARTED | — | — | — |

## Review phase và chương trình

| Program | Kết luận PLO / gate | Người review | Bằng chứng |
| --- | --- | --- | --- |
| A · Python Programming for AI | Chưa review | — | — |
| B · Data và Full-stack Web Development | Chưa review | — | — |
| C · AI trong quy trình phát triển phần mềm | Chưa review | — | — |
| D · AI Application, RAG và Agent Systems | Chưa review | — | — |
| E · Nghiên cứu và lựa chọn dự án | Chưa review | — | — |
| F · Xây dựng sản phẩm và Ownership | Chưa review | — | — |
| G · Deployment, DevOps và LLMOps | Chưa review | — | — |
| ML · Machine Learning Foundations | Chưa review | — | — |
| DL · Deep Learning và Model Adaptation | Chưa review | — | — |

## Buổi học tiếp theo

- Việc đầu tiên: làm [đối chiếu đầu vào](docs/ENTRY_REVIEW.md) hoặc liên kết bài cũ tương đương.
- Course/unit chọn: chưa chốt.
- Ngày và ngân sách giờ: chưa chốt.
- Output nhỏ cần nộp: file + test/report + phần giải thích.

Sau mỗi buổi lưu [review](templates/REVIEW.md), cập nhật [phần kiến thức](progress/PHASES.md) và [CLO](progress/OUTCOMES.md), rồi sửa trạng thái course ở đây. Giờ thực tế là thời gian đã ghi nhận, không lấy giờ dự kiến nhân với số checkbox. Lịch tuần W0–W12 cũ chỉ còn trong [archive](archive/dashboard-v1/PROGRESS.md).
