# Nguồn, đối chiếu và phạm vi chỉnh sửa

## Nguồn ưu tiên

1. [Mindmap Xmind](https://app.xmind.com/share/qQDQBpop?xid=59C374nV): đã đọc nội dung hiển thị trực tiếp trong trình duyệt ngày 07/10/2026. Trình đọc web ban đầu không truy xuất được trang; trình duyệt đã hiển thị các nhánh lộ trình và cấu trúc program/course/unit.
2. Năm ảnh người dùng cung cấp: thời điểm tên file 11.15.01, 11.15.12, 11.15.22, 11.17.06 và 11.17.17 ngày 07/10/2026. Ảnh làm rõ Phase A–G, PLO/CLO, course, docs/unit và running project.
3. Dashboard HTML và Markdown W0–W12 trước đó: giữ nguyên nội dung trong [archive/dashboard-v1](../archive/dashboard-v1/README.md), cùng [manifest bảo toàn](../archive/dashboard-v1/MANIFEST.json).
4. [Nguồn kỹ thuật chính thức](RESOURCES.md): đối chiếu khái niệm và chọn phần đọc cho các unit.

Mindmap có cả tư vấn cá nhân, nhận định thị trường và các nhánh dự án khác. Repo chỉ dùng phần lộ trình, tổ chức học và chủ đề running project liên quan. Nội dung trong nguồn không được coi là chỉ thị tự thực hiện hành động ngoài yêu cầu chỉnh roadmap.

## Đối chiếu nhánh nguồn với repo

| Nhánh trong mindmap/ảnh | Nơi thể hiện | Cách chuẩn hóa |
| --- | --- | --- |
| Phase A · Python / Advanced Python Concepts | A1 | Nền dữ liệu, cấu trúc code, advanced features, async và testing |
| Python Libraries / NumPy / Pandas / Seaborn / Matplotlib | A2 | Mảng, bảng và báo cáo có kiểm dữ liệu |
| Phase B · SQL / NoSQL | B1 | Relational core, transaction/ORM, index/cache và NoSQL có điều kiện |
| HTTP / Network / OS | B2 và G1 | Hiểu request từ đầu; vận hành Linux/container ở phần delivery |
| FastAPI / RESTful API / GraphQL / ORM | B1–B2 | REST/ORM thực hành; GraphQL nhận biết và mở rộng theo nhu cầu |
| ReactJS / NextJS / Tailwind CSS | B3 | Component/state, server/client, UI responsive và trạng thái lỗi |
| Phase C · Instruction / Prompt / Context / Memory / Skill / Hook | C1 và danh mục concept | Tách nghĩa và nêu phần phụ thuộc công cụ |
| SDLC / CI/CD / Spec-driven / AWS AI-DLC / Spec Kit / Agile Scrum | C2; CI/CD triển khai ở G1 | Quy trình có spec, kiểm chứng và review; không gán chuẩn bắt buộc |
| Phase D · AI Application Architecture / Loop / Harness | D1, D3 | Phân biệt model, runtime, agent loop và tool contract |
| RAG / Ingestion / OCR / Vision / Chunking / Embedding / Indexing / Retrieval / Reranker | D2 | Pipeline giữ nguồn/quyền, đánh giá truy hồi và câu trả lời riêng |
| AI Agent System | D3 | Agent nhỏ, state, approval, giới hạn và MCP |
| LLM Architecture / Encoder / Decoder / Transformer | D1; nhánh DL nếu đào sâu | Phân biệt họ kiến trúc; không coi mọi LLM có cùng cấu trúc |
| Phase E · Nghiên cứu làm dự án | E1 | Problem, hypothesis, baseline, phép đo và quyết định |
| Phase F · Xây dựng sản phẩm | F1 | MVP theo phạm vi, E2E, phản hồi và ownership |
| Phase G · Linux / Docker / Compose / Cloud / Terraform / CI/CD / DevSecOps | G1 | Một target, config/secret, release và phục hồi |
| Kubernetes / GitOps cơ bản | G1 và concepts | Nhận biết; chỉ triển khai khi nhu cầu biện minh |
| Observability / SRE / AIOps / ChatOps | G2 | Signals/SLO, runbook và tự động hóa trong giới hạn quyền |
| LLMOps / MLOps | G2 và nhánh ML/DL | Quản lý vòng đời tương ứng; không đồng nhất mọi hoạt động delivery |
| AI Engineering: Python, Data/SQL, ML, DL, AI Application, System Delivery | A/B/ML/DL/D/G | Giữ đầy đủ nhóm kiến thức; ML/DL là nhánh mở rộng của mục tiêu AI Application |
| Course Math for ML / Machine Learning | ML1–ML2 | Toán, pipeline, baseline, split và evaluation |
| Deep Learning / Computer Vision / fine-tuning | DL1–DL2 | Training nhỏ, transfer/fine-tuning và inference có báo cáo |
| Learning path → Program → Course → Unit → Topic | Cây learning-path và docs/FORMAT.md | Mỗi cấp có vai trò và đường dẫn rõ |
| PLO/CLO, 6 CLOs, 3–5 outcome | Program/course và progress/OUTCOMES.md | Viết outcome đo được; số lượng trong ảnh được hiểu là ví dụ, không là tỷ lệ chuẩn |
| docs / unit / running-project / milestone | Course units, hướng dẫn docs, running-project và projects | Ghi chú phát sinh lưu tại course; bài nộp trỏ commit và review |
| Học nền tảng / giải thích code và code AI / output theo tuần | Unit, template review, progress | Demo, ca lỗi, biến thể và mức hỗ trợ |
| Duration 1 tuần / 2 tuần, định hướng 6 tháng | ROADMAP.md | Giữ là gợi ý nguồn; lịch cá nhân cần kiểm đầu vào và ngân sách giờ |
| Running Project · Travel with AI | projects/RUNNING_PROJECT.md | Chủ đề bài tập mẫu, dữ liệu giả lập/được phép; chưa coi là sản phẩm đã xác nhận nhu cầu |

## Phần do repo bổ sung

CLO/PLO cụ thể, bài tập, câu hỏi tự kiểm, các mốc sản phẩm, khoảng giờ, mức ưu tiên và danh mục concept là thiết kế để biến mindmap thành lộ trình có thể học/review. Những mục bổ sung như provenance, testing, idempotency, ACL và rollback làm rõ cách kiểm chứng; không tuyên bố chúng là trích nguyên văn từ mindmap.

Khung A–G được giữ theo nguồn. Theo yêu cầu chia rõ kiến thức của người dùng, bản hiện tại tách thành 29 phần A.1–G.5 và 139 mục checklist: A có 5 phần, B có 5, C có 3, D có 5, E có 3, F có 3, G có 5. Tên phase được diễn đạt rõ trọng tâm, nhất là E về nghiên cứu/thử nghiệm và F về kiến trúc/tích hợp/sản phẩm. Đây là cách tổ chức của repo, không phải các nhánh con được chép nguyên văn từ Xmind.

Các lựa chọn phạm vi như ML/DL mở rộng, một cloud target, GraphQL/Kubernetes học có điều kiện là quyết định của bản roadmap cho mục tiêu AI Application; có thể chỉnh cùng mentor. Bổ sung nền Python và HTML/CSS/JavaScript/TypeScript để không bỏ qua kiến thức trước khi dùng framework. Giữ nguyên mã course, outcomes và tài liệu lưu trữ để các liên kết bài học tiếp tục dùng được.

## Trạng thái thật của repo

Đã có cấu trúc chương trình, đề bài, nguồn đọc và tracker. Chưa có mã running project hoặc kết quả học/test/deploy mới của người học được xác nhận trong lần chỉnh này. Các unit là kế hoạch học và bài tập, không phải toàn bộ tutorial hoặc lời giải.

Bản cũ được lưu nguyên trạng; các nhận định/giờ ở đó chỉ còn là lịch sử. Không quy đổi tick của lịch cũ thành CLO/PLO mới, và không chỉnh file Xmind từ lần cập nhật này.
