# AI Application Engineer Learning Roadmap

Lộ trình học theo **7 Phase A–G của mindmap**, chia thành **29 phần kiến thức**. Mỗi phần liệt kê topics/concepts cần nắm, bài thực hành và course để học; mỗi phase có output và điều kiện hoàn thành rõ ràng.

## Bắt đầu ở đâu

| Bạn cần | Mở tài liệu |
| --- | --- |
| Xem từng phase gồm những kiến thức gì | [Roadmap A–G và checklist chi tiết](ROADMAP.md) |
| Hiểu cách chia program, course, unit, PLO/CLO | [Cấu trúc chương trình](docs/FORMAT.md) |
| Học và tra các concept thường gặp | [Danh mục concept](docs/CONCEPTS.md) |
| Xem bài tập và nguồn cho từng course | [Learning path](learning-path/ai-application-engineer/README.md) |
| Biết mỗi giai đoạn làm ra gì | [Running project](projects/RUNNING_PROJECT.md) |
| Theo dõi từng phần kiến thức | [Tracker 29 phần](progress/PHASES.md) |
| Ghi tiến độ course, bài nộp và phản hồi | [Progress tracker](PROGRESS.md) |
| Xem sơ đồ và outline của lộ trình | [Mindmap Markdown](docs/MINDMAP.md) |

**Bước đầu:** làm [đối chiếu đầu vào](docs/ENTRY_REVIEW.md), chọn một unit cần học, làm bài rồi lưu review. Nếu đã có artifact đáp ứng yêu cầu, dùng artifact đó để review thay vì học lại theo lịch máy móc.

## Các giai đoạn

| Phase | Trọng tâm | Output để review |
| --- | --- | --- |
| [A · Programming Language](ROADMAP.md#phase-a) | Python nền tảng, OOP/advanced, async, testing, NumPy/Pandas/visualization | CLI, bộ test, báo cáo dữ liệu |
| [B · Web Development](ROADMAP.md#phase-b) | Internet/OS, database/SQL/NoSQL, FastAPI, HTML/CSS/JS/TS, React/Next.js | Web có luồng UI → API → DB |
| [C · AI-assisted SDLC](ROADMAP.md#phase-c) | Concept AI, spec, Agile, Git workflow, code review và CI | Feature từ spec đến review |
| [D · AI Application](ROADMAP.md#phase-d) | LLM, kiến trúc ứng dụng AI, RAG, agent/MCP, evaluation và security | Prototype có nguồn, quyền, eval và giới hạn tool |
| [E · Nghiên cứu dự án](ROADMAP.md#phase-e) | Problem framing, dữ liệu, thiết kế thử nghiệm và phân tích kết quả | Problem brief, thử nghiệm và quyết định phạm vi |
| [F · Xây dựng sản phẩm](ROADMAP.md#phase-f) | Kiến trúc, tích hợp hệ thống, E2E, product review và bàn giao | MVP có luồng hoàn chỉnh, demo và regression tests |
| [G · Deployment](ROADMAP.md#phase-g) | Linux/Docker, cloud/IaC, CI/CD, observability/SRE và LLMOps | Release, rollback/restore và runbook |

Ví dụ **Phase A — Programming Language** gồm A.1 Python nền tảng, A.2 OOP và Advanced Python, A.3 Concurrency/Async, A.4 Môi trường/Debugging/Testing, A.5 Python Libraries. Trong A.2 có class/object, composition, module/package, iterator/generator, closure/decorator, context manager và type hints. [Mở đầy đủ kiến thức Phase A](ROADMAP.md#phase-a).

Nhánh **Machine Learning / Deep Learning** có chương trình riêng khi cần đi sâu mô hình. Các nền tảng vector, metric và đánh giá cần cho AI Application vẫn nằm trong nhánh chính.

## Cách tổ chức repo

```text
README.md / ROADMAP.md / PROGRESS.md
learning-path/ai-application-engineer/
  README.md
  programs/<program>/
    README.md                     # PLO, đầu vào, courses, gate
    courses/<course>/
      README.md                   # CLO, units, bài nộp
      units/01.md, 02.md, 03.md    # topics, bài tập, output, nguồn
      docs/                       # tạo khi có ghi chú/bài làm thực tế
    running-project/README.md     # milestone và nghiệm thu
concepts/                         # giải nghĩa, cách dùng, tự kiểm
projects/                         # dự án xuyên suốt và các mốc
progress/                         # tracker từng phần, ma trận CLO và review
templates/                        # mẫu unit, course, review
resources/                        # dữ liệu mẫu/manifest do người học bổ sung
archive/dashboard-v1/             # bản W0–W12 nguyên trạng
```

**7 phase · 29 phần kiến thức · 139 mục checklist**, học qua **9 programs · 18 courses · 54 units**. Trong đó 7 programs/14 courses thuộc nhánh chính; 2 programs/4 courses ML/DL là mở rộng. Phần kiến thức là cách chia nhỏ phase, không phải thêm course hoặc cộng thêm số giờ. Các file là kế hoạch và đề bài; bài làm, kết quả chạy và năng lực đã đạt được ghi riêng trong tracker.

## Cách học và review

1. Chọn một phần kiến thức trong phase, mở course/unit và nguồn tương ứng; giải thích concept bằng ví dụ nhỏ.
2. Làm bài và kiểm ca hợp lệ, biên, lỗi; lưu file/repo và commit.
3. Demo milestone, giải thích code kể cả phần AI viết, xử lý một biến thể mới.
4. Ghi phản hồi, giờ thực tế và việc tiếp theo theo [mẫu review](templates/REVIEW.md); cập nhật [từng phần](progress/PHASES.md) và CLO.

Chuyển phase khi toàn bộ phần bắt buộc đạt ở độ sâu đã ghi, đủ bài làm và gate tích hợp. Những mục nhận biết hoặc mở rộng được nêu rõ trong từng phase.

Chuẩn bị một buổi review mỗi tuần theo gợi ý mindmap; ngày/giờ cụ thể cần tự sắp xếp. Kết quả có thể là tiếp tục, bổ sung hoặc đổi phạm vi. Hoàn thành tài liệu hoặc tick checkbox không tự xác nhận cấp bậc nghề nghiệp.

[Đối chiếu mindmap](docs/SOURCE.md) · [Nguồn học chính thức](docs/RESOURCES.md) · [Bản cũ](archive/dashboard-v1/README.md)
